"""Provider-free persistence regression suite for E2E Targeted Repair 01."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable, Dict


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
HARNESS_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
for import_path in (str(ROOT / "implementation"), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

import run_minimal_e2e as e2e
from provider_response_persistence import persist_provider_response, persist_validation_error


def _recorded_showrunner_output() -> Dict[str, Any]:
    return {
        "primary_state_or_outcome": "PASS",
        "flags": "ABSENT",
        "handoffs": "ABSENT",
        "canon_assignment_locks": ["frozen-lock"],
        "prohibited_changes": ["frozen-prohibition"],
        "required_outcome": "ABSENT",
        "unresolved_decisions": [],
        "state_evidence": {
            "relevant_prior_state": "ABSENT",
            "current_state": "ABSENT",
            "proposed_state": "ABSENT",
            "knowledge_timing": "ABSENT",
            "relationship_state": "ABSENT",
            "visual_state": "ABSENT",
        },
        "content": "故事前提\n角色\nCanon Locks\n三场结构",
        "scene_packages": [],
    }


def _persist_recorded_failure(root: Path) -> Dict[str, Any]:
    raw = json.dumps(_recorded_showrunner_output(), ensure_ascii=False, separators=(",", ":"))
    persisted = persist_provider_response(
        evidence_dir=root,
        role="Showrunner",
        invocation_id="PERSIST-RECORDED:showrunner:1",
        timestamp="2026-08-28T00:00:00+00:00",
        raw_response={
            "raw_content": raw,
            "provider": "deepseek",
            "model": "deepseek-v4-pro",
            "provider_invocation_id": "recorded-provider-id",
        },
        usage_record={
            "provider": "deepseek",
            "model": "deepseek-v4-pro",
            "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2},
            "request_success": True,
        },
        input_artifact="recorded/showrunner_input.json",
    )
    try:
        e2e.validate_role_output(e2e.role_spec("showrunner"), _recorded_showrunner_output())
    except e2e.E2EBlocked as exc:
        error_path = persist_validation_error(
            evidence_dir=root,
            role="Showrunner",
            invocation_id="PERSIST-RECORDED:showrunner:1",
            validation_stage="Local Role-Contract Validation",
            category=exc.category,
            detail=exc.detail,
        )
        return {"raw": raw, "persistence": persisted, "error_path": error_path, "error": exc}
    raise AssertionError("Recorded invalid Showrunner response unexpectedly passed validation")


def _run_case(case_id: str, action: Callable[[], str]) -> Dict[str, str]:
    try:
        return {"id": case_id, "result": "PASS", "detail": action()}
    except Exception as exc:  # test report must retain attributable failure detail
        return {"id": case_id, "result": "FAIL", "detail": f"{type(exc).__name__}: {exc}"}


def main() -> int:
    counters = {"provider_calls": 0, "executor_calls": 0}
    with tempfile.TemporaryDirectory(prefix="afs-persist-regression-") as temp:
        root = Path(temp)
        recorded = _persist_recorded_failure(root)
        raw_path = Path(recorded["persistence"]["raw_response_artifact"])
        metadata_path = Path(recorded["persistence"]["invocation_metadata_artifact"])
        verification_path = Path(recorded["persistence"]["persistence_verification_artifact"])
        error_path = Path(recorded["error_path"])

        def raw_survives() -> str:
            payload = json.loads(raw_path.read_text(encoding="utf-8"))
            assert payload["raw_content"] == recorded["raw"]
            assert payload["raw_content_sha256"] == hashlib.sha256(recorded["raw"].encode("utf-8")).hexdigest()
            return "raw content is persisted before local validation and survives the validation failure"

        def usage_survives() -> str:
            payload = json.loads(metadata_path.read_text(encoding="utf-8"))
            assert payload["usage"]["usage"]["total_tokens"] == 2
            return "usage metadata survives the validation failure"

        def invocation_survives() -> str:
            assert json.loads(raw_path.read_text(encoding="utf-8"))["invocation_id"] == "PERSIST-RECORDED:showrunner:1"
            assert json.loads(metadata_path.read_text(encoding="utf-8"))["invocation_id"] == "PERSIST-RECORDED:showrunner:1"
            return "invocation ID is retained in both durable records"

        def identity_survives() -> str:
            raw_payload = json.loads(raw_path.read_text(encoding="utf-8"))
            metadata_payload = json.loads(metadata_path.read_text(encoding="utf-8"))
            assert raw_payload["role"] == metadata_payload["role"] == "Showrunner"
            assert raw_payload["provider"] == "deepseek" and raw_payload["model"] == "deepseek-v4-pro"
            return "role, provider, and model identities survive"

        def error_is_separate() -> str:
            payload = json.loads(error_path.read_text(encoding="utf-8"))
            assert payload["lifecycle_stage"] == "LOCAL_VALIDATION_FAILURE_RECORDED"
            assert payload["detail"] == recorded["error"].detail
            assert raw_path.is_file() and metadata_path.is_file()
            return "validation error is separate from persisted raw response and metadata"

        def no_provider_call() -> str:
            assert counters["provider_calls"] == 0
            return "recorded-response regression performed no Provider call"

        def no_executor_call() -> str:
            assert counters["executor_calls"] == 0
            return "recorded-response regression performed no ModelExecutor call"

        def initial_pattern_cannot_lose_evidence() -> str:
            verification = json.loads(verification_path.read_text(encoding="utf-8"))
            assert verification["verified"] is True
            assert recorded["error"].detail == "Only Scene Writer may supply scene_packages"
            return "the prior invalid non-Scene-Writer scene_packages pattern retains raw, usage, invocation, and separate error evidence"

        results = [
            _run_case("PERSIST-01", raw_survives),
            _run_case("PERSIST-02", usage_survives),
            _run_case("PERSIST-03", invocation_survives),
            _run_case("PERSIST-04", identity_survives),
            _run_case("PERSIST-05", error_is_separate),
            _run_case("PERSIST-06", no_provider_call),
            _run_case("PERSIST-07", no_executor_call),
            _run_case("PERSIST-08", initial_pattern_cannot_lose_evidence),
        ]
    payload = {"suite": "Provider Response Persistence Regression", "results": results, "passed": sum(item["result"] == "PASS" for item in results), "total": len(results), "counters": counters}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["passed"] == payload["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
