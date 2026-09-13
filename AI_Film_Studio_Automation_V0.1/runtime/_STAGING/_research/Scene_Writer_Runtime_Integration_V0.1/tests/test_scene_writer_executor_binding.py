"""Non-network EB-SW-01–10 binding gates for Scene Writer."""

from __future__ import annotations

import inspect
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
for path in (str(STAGE), str(AUTOMATION_ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)

from runtime.scene_writer.scene_writer_executor import CanonicalSceneWriterExecutor  # noqa: E402
from runtime.scene_writer.scene_writer_executor_binding import (  # noqa: E402
    SceneWriterCanonicalBinding,
    SceneWriterExecutorBindingError,
    SceneWriterExecutorRegistry,
    create_scene_writer_binding,
)
from runtime.scene_writer.scene_writer_runtime import SceneWriterRuntime  # noqa: E402


EXPECTED_HASH = "93e1be12988f8caa6cdd76acb5e6c1bf6ad3ca0dff5806a2ea93511e66052dfb"


def base_input(request_id: str) -> Dict[str, Any]:
    return {"request_id": request_id, "requested_mode": "CREATE", "assignment_language": "en-US", "scene_id": "EB-SW-MALFORMED-01", "scene_purpose": "binding validation"}


def expect_raises(func, error_type=SceneWriterExecutorBindingError) -> None:
    try:
        func()
    except error_type:
        return
    raise AssertionError("expected canonical binding rejection")


def result(case_id: str, function) -> Dict[str, str]:
    try:
        detail = function()
        return {"id": case_id, "result": "PASS", "detail": detail or ""}
    except Exception as exc:  # deliberate: a gate failure must be visible
        return {"id": case_id, "result": "FAIL", "detail": f"{type(exc).__name__}: {exc}"}


def main() -> int:
    if not os.environ.get("DEEPSEEK_API_KEY", "").strip():
        print(json.dumps({"key_status": "NOT AVAILABLE", "results": [], "passed": 0, "total": 10}, ensure_ascii=False))
        return 1

    binding = SceneWriterCanonicalBinding.load()
    bundle = create_scene_writer_binding()  # construction only; no provider completion call
    reports = []
    reports.append(result("EB-SW-01", lambda: "canonical identity" if binding.identity == "scene-writer" else (_ for _ in ()).throw(AssertionError(binding))))
    reports.append(result("EB-SW-02", lambda: "canonical version" if binding.version == "V0.1" else (_ for _ in ()).throw(AssertionError(binding))))
    reports.append(result("EB-SW-03", lambda: "canonical hash" if binding.sha256 == EXPECTED_HASH and bundle.runtime.canonical_binding()["passed"] else (_ for _ in ()).throw(AssertionError(binding))))
    reports.append(result("EB-SW-04", lambda: "shared neutral ModelExecutor" if bundle.executor.model_executor.__class__.__name__ == "ModelExecutor" else (_ for _ in ()).throw(AssertionError(type(bundle.executor.model_executor)))))
    reports.append(result("EB-SW-05", lambda: "DeepSeek adapter resolved" if bundle.provider.provider == "deepseek" and bundle.provider.model == "deepseek-v4-pro" else (_ for _ in ()).throw(AssertionError(bundle.provider))))

    def reject_staging() -> str:
        staged_skill = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Scene_Writer_Phase_5_Production_Skill_V0.1" / "scene-writer" / "SKILL.md"
        staged = CanonicalSceneWriterExecutor(
            skill_path=staged_skill,
            expected_sha256=EXPECTED_HASH,
            model_executor=bundle.executor.model_executor,
            model=bundle.provider.model,
            thinking_mode=bundle.provider.thinking_mode,
        )
        registry = SceneWriterExecutorRegistry(binding)
        expect_raises(lambda: registry.register(staged))
        return "staging path rejected"
    reports.append(result("EB-SW-06", reject_staging))

    reports.append(result("EB-SW-07", lambda: (expect_raises(lambda: bundle.registry.resolve("scene-writer", "V0.0", EXPECTED_HASH)), "version mismatch rejected")[1]))
    reports.append(result("EB-SW-08", lambda: (expect_raises(lambda: bundle.registry.resolve("scene-writer", "V0.1", "0" * 64)), "hash mismatch rejected")[1]))

    def malformed_output() -> str:
        runtime = SceneWriterRuntime(
            executor=lambda _: {"creative_deliverable": None, "control_data": {"flags": [], "handoffs": []}},
            semantic_verifier=lambda _: {"integrity_result": "PASS", "violations": []},
        )
        response = runtime.execute(base_input("EB-SW-MAL-01"))
        assert response["runtime_status"] == "FAIL_SAFE" and response["runtime_failure_code"] == "MALFORMED_EXECUTOR_OUTPUT", response
        return "malformed structured output rejected"
    reports.append(result("EB-SW-09", malformed_output))

    def no_second_authority() -> str:
        source = inspect.getsource(CanonicalSceneWriterExecutor)
        assert source.count("model_executor.execute(") == 1, source
        assert "DeepSeekProviderAdapter" not in source and "base_url" not in source and "DEEPSEEK_API_KEY" not in source, source
        return "executor only loads canonical Skill, transports request, and returns JSON for Runtime validation"
    reports.append(result("EB-SW-10", no_second_authority))

    payload = {"key_status": "AVAILABLE", "classification": "NON-NETWORK BINDING TEST", "results": reports, "passed": sum(item["result"] == "PASS" for item in reports), "total": len(reports)}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["passed"] == payload["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
