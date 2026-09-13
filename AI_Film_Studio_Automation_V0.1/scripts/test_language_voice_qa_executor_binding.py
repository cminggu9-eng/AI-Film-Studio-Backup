"""Binding containment tests. Synthetic adapters are test-only and never semantic validation evidence."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.shared_qa.language_voice_qa_binding import CanonicalBinding, CanonicalExecutorRegistry, ExecutorBindingError
from runtime.shared_qa.language_voice_qa_executor import CanonicalLanguageVoiceQAExecutor
from runtime.shared_qa.language_voice_qa_runtime import LanguageVoiceQARuntime
from runtime.shared_qa.model_executor import ModelExecutor, ModelRequest, ModelResponse


VALID_OUTPUT = {
    "decision": "PASS / NO CHANGE", "severity": "LEVEL 0", "route": "Early Exit", "mode": "QA MODE",
    "context_state": "SUFFICIENT", "primary_finding": None, "detector_ownership": "Early Exit",
    "diagnostics": "No locatable language loss.", "meaning_lock_status": "NOT_REQUIRED",
    "benefit_result": "NOT_APPLICABLE", "recommendation": "Preserve Original.", "rewrite_scope": None,
    "revised_text": None, "rewrite_ceiling_status": "NOT_APPLICABLE", "safety_regression": None,
    "secondary_signal": None, "role_handoff": None, "contemporary_state": None,
    "canon_mutation_requested": False, "invoke_dependencies": False,
}


class TestAdapter:
    def __init__(self, content: Dict[str, Any]) -> None:
        self.content = content
        self.calls = 0

    def complete(self, _request: ModelRequest) -> ModelResponse:
        self.calls += 1
        return ModelResponse(json.dumps(self.content, ensure_ascii=False), "test-only", "deepseek-v4-pro", "test", {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2, "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 1}, 1, "disabled")


def bundle(content: Dict[str, Any] | None = None):
    binding = CanonicalBinding.load()
    adapter = TestAdapter(content or VALID_OUTPUT)
    executor = CanonicalLanguageVoiceQAExecutor(skill_path=binding.canonical_path, expected_sha256=binding.sha256, model_executor=ModelExecutor(adapter))
    registry = CanonicalExecutorRegistry(binding)
    registry.register(executor)
    return binding, adapter, executor, registry, LanguageVoiceQARuntime(registry.dispatch)


def main() -> int:
    checks = []
    def check(name, callback):
        try:
            callback()
            checks.append((name, "PASS"))
        except Exception as exc:
            checks.append((name, f"FAIL: {type(exc).__name__}: {exc}"))

    check("EB-01 identity resolution", lambda: (lambda b: (_ for _ in ()).throw(AssertionError()) if b.identity != "language-voice-qa" else None)(CanonicalBinding.load()))
    check("EB-02 version binding", lambda: (lambda b: (_ for _ in ()).throw(AssertionError()) if b.version != "0.1" else None)(CanonicalBinding.load()))
    def real_callable_dispatch():
        _binding, adapter, _executor, _registry, runtime = bundle()
        result = runtime.invoke({"original": "这是一段可保留的文本。", "invocation_id": "eb03"})
        assert result["internal_runtime_result"]["runtime_status"] == "SUCCESS" and adapter.calls == 1
    check("EB-03 registered executor dispatch", real_callable_dispatch)
    def missing_binding():
        registry = CanonicalExecutorRegistry(CanonicalBinding.load())
        result = LanguageVoiceQARuntime(registry.dispatch).invoke({"original": "测试", "invocation_id": "eb04"})
        assert result["internal_runtime_result"]["failure_code"] == "F3"
    check("EB-04 missing executor F3", missing_binding)
    def illegal_registration():
        binding = CanonicalBinding.load()
        class Illegal:
            def canonical_metadata(self): return {"identity": binding.identity, "version": binding.version, "sha256": binding.sha256, "path": str(ROOT / "runtime" / "_STAGING" / "bad.md")}
            def __call__(self, _value): return VALID_OUTPUT
        try: CanonicalExecutorRegistry(binding).register(Illegal())
        except ExecutorBindingError: return
        raise AssertionError("illegal executor registered")
    check("EB-05 illegal executor rejected", illegal_registration)
    check("EB-06 staging fallback rejected", illegal_registration)
    def mismatch():
        binding, _adapter, _executor, registry, _runtime = bundle()
        try: registry.resolve(binding.identity, "0.2", binding.sha256)
        except ExecutorBindingError: return
        raise AssertionError("version mismatch resolved")
    check("EB-07 version mismatch rejected", mismatch)
    def malformed():
        _b, _a, _e, _r, runtime = bundle({"decision": "PASS / NO CHANGE"})
        result = runtime.invoke({"original": "测试", "invocation_id": "eb08"})
        assert result["internal_runtime_result"]["failure_code"] == "F3"
    check("EB-08 malformed output rejected", malformed)
    def idempotency():
        _b, adapter, _e, _r, runtime = bundle()
        first = runtime.invoke({"original": "测试", "invocation_id": "eb09"})
        second = runtime.invoke({"original": "测试", "invocation_id": "eb09"})
        assert first == second and adapter.calls == 1
    check("EB-09 duplicate invocation has no cumulative mutation", idempotency)
    def no_second_authority():
        expected = dict(VALID_OUTPUT, severity="LEVEL 2", route="Model supplied route", diagnostics="Model supplied diagnostic")
        _b, _a, executor, _r, runtime = bundle(expected)
        result = runtime.invoke({"original": "测试", "invocation_id": "eb10"})
        assert executor.output_for("eb10") == expected and result["internal_runtime_result"]["severity"] == "LEVEL 2"
    check("EB-10 executor preserves model decision without second adjudication", no_second_authority)
    for name, status in checks:
        print(f"{name}: {status}")
    return 0 if all(status == "PASS" for _, status in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
