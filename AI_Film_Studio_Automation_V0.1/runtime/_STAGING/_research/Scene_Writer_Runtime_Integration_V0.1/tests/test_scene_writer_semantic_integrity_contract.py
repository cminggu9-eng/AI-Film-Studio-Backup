"""Non-network structural gates for semantic Assignment Integrity V0.1."""

from __future__ import annotations

import copy
import inspect
import json
import sys
from pathlib import Path
from typing import Any, Dict


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
for path in (str(STAGE), str(AUTOMATION_ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)

from runtime.compliance.compliance_gate import sha256_file  # noqa: E402
from runtime.scene_writer.scene_writer_runtime import SceneWriterRuntime  # noqa: E402
from runtime.scene_writer.semantic_assignment_integrity import (  # noqa: E402
    SemanticAssignmentIntegrityVerifier,
    SemanticIntegrityError,
    build_assignment_constraint_ledger,
)


EXPECTED_HASH = "93e1be12988f8caa6cdd76acb5e6c1bf6ad3ca0dff5806a2ea93511e66052dfb"


def assignment(request_id: str) -> Dict[str, Any]:
    return {
        "request_id": request_id,
        "requested_mode": "CREATE",
        "output_language": "en-US",
        "scene_id": "SEMANTIC-INTEGRITY-CONTRACT",
        "canon_locks": ["The absent presenter's reason is unknown.", "Lin Yan does not know the reason."],
        "showrunner_locks": ["Chen Mo conditionally accepts if existing materials are sent tonight."],
        "participants": [
            {"name": "Lin Yan", "knowledge": "She knows the presenter cannot attend, but not why.", "constraint": "She may not claim to know why."},
            {"name": "Chen Mo", "capacity": "Can take over the presentation.", "constraint": "He has not agreed yet."},
        ],
        "character_context": {"relationship": "colleagues, not enemies"},
        "required_event": "Lin Yan asks Chen Mo to take the presentation.",
        "required_information": "The presenter cannot attend; the reason is unknown.",
        "required_outcome": "Chen Mo conditionally accepts if materials arrive tonight.",
        "prior_scene_state": "Only Lin Yan and Chen Mo remain in the meeting room.",
        "desired_post_state": "Chen Mo has conditionally accepted.",
    }


OUTPUT = {
    "creative_deliverable": {"kind": "scene", "content": "Lin Yan closes her laptop. Chen Mo asks, 'Can you send the existing materials tonight?' Lin Yan nods."},
    "control_data": {
        "primary_state": "SCENE_CREATED", "flags": [], "handoffs": [],
        "scene_function": "Set a workable condition.", "objectives": "Lin Yan needs a commitment; Chen Mo needs materials.",
        "resistance": "Chen Mo avoids an unsupported commitment.", "before_state": "The meeting just ended.",
        "turn": "Chen Mo makes conditional acceptance possible.", "state_after": "Materials need to be sent tonight.",
        "entry_rationale": "Enter at the request.", "exit_rationale": "Leave after a condition is stated.",
    },
}


def pass_verifier(_: Dict[str, Any]) -> Dict[str, Any]:
    return {"integrity_result": "PASS", "violations": []}


def fail_verifier(_: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "integrity_result": "FAIL",
        "violations": [{
            "category": "UNAUTHORIZED_CAPABILITY_FACT",
            "generated_claim": "unsupported comparative capability",
            "conflicting_or_missing_authority": "CAPABILITY_CONSTRAINTS only grants taking over",
            "location": "creative_deliverable.content",
            "concise_reason": "The generated claim exceeds the assignment.",
        }],
    }


def run_case(case_id: str, function) -> Dict[str, str]:
    try:
        return {"id": case_id, "result": "PASS", "detail": function()}
    except Exception as exc:  # Gate failures must be explicit.
        return {"id": case_id, "result": "FAIL", "detail": f"{type(exc).__name__}: {exc}"}


def main() -> int:
    results = []

    def ledger_fields() -> str:
        ledger = build_assignment_constraint_ledger(assignment("SI-STRUCT-01"))
        required = {
            "LOCKED_FACTS", "EXPLICIT_UNKNOWNS", "CHARACTER_KNOWLEDGE_LIMITS", "TEMPORAL_CONSTRAINTS",
            "RELATIONSHIP_CONSTRAINTS", "CAPABILITY_CONSTRAINTS", "REQUIRED_EVENTS", "REQUIRED_INFORMATION",
            "REQUIRED_OUTCOME", "OPEN_CREATIVE_SPACE",
        }
        assert required <= set(ledger), ledger
        assert ledger["scope"] == "CURRENT_ASSIGNMENT_ONLY", ledger
        assert "unknown" in " ".join(ledger["EXPLICIT_UNKNOWNS"]).lower(), ledger
        return "assignment-only ledger carries all required constraint domains"
    results.append(run_case("SI-STRUCT-01", ledger_fields))

    def unbound_real_rejected() -> str:
        runtime = SceneWriterRuntime(executor=lambda _: copy.deepcopy(OUTPUT))
        response = runtime.execute(assignment("SI-STRUCT-02"))
        assert response["runtime_status"] == "FAIL_SAFE", response
        assert response["runtime_failure_code"] == "SEMANTIC_VERIFIER_UNBOUND", response
        return "real generation cannot bypass an unbound semantic verifier"
    results.append(run_case("SI-STRUCT-02", unbound_real_rejected))

    def enforce_fail() -> str:
        runtime = SceneWriterRuntime(synthetic_executor=lambda _: copy.deepcopy(OUTPUT), semantic_verifier=fail_verifier, test_sandbox=True)
        response = runtime.execute(assignment("SI-STRUCT-03"))
        assert response["runtime_status"] == "FAIL_SAFE" and response["runtime_failure_code"] == "SEMANTIC_INTEGRITY_VIOLATION", response
        assert response["scene_writer"] is None and response["semantic_integrity_validation"]["integrity_result"] == "FAIL", response
        return "FAIL suppresses successful scene delivery without rewrite"
    results.append(run_case("SI-STRUCT-03", enforce_fail))

    def allow_pass() -> str:
        runtime = SceneWriterRuntime(synthetic_executor=lambda _: copy.deepcopy(OUTPUT), semantic_verifier=pass_verifier, test_sandbox=True)
        response = runtime.execute(assignment("SI-STRUCT-04"))
        assert response["runtime_status"] == "SUCCESS", response
        assert response["semantic_integrity_validation"] == {"integrity_result": "PASS", "violations": []}, response
        return "PASS permits exactly one generated scene result"
    results.append(run_case("SI-STRUCT-04", allow_pass))

    def no_retry_or_rewrite() -> str:
        calls = {"generate": 0, "verify": 0}

        def generate(_: Dict[str, Any]) -> Dict[str, Any]:
            calls["generate"] += 1
            return copy.deepcopy(OUTPUT)

        def verify(_: Dict[str, Any]) -> Dict[str, Any]:
            calls["verify"] += 1
            return fail_verifier({})

        response = SceneWriterRuntime(synthetic_executor=generate, semantic_verifier=verify, test_sandbox=True).execute(assignment("SI-STRUCT-05"))
        assert response["runtime_failure_code"] == "SEMANTIC_INTEGRITY_VIOLATION" and calls == {"generate": 1, "verify": 1}, (response, calls)
        return "one generation and one verification only; no resample or rewrite"
    results.append(run_case("SI-STRUCT-05", no_retry_or_rewrite))

    def malformed_verifier_result_rejected() -> str:
        runtime = SceneWriterRuntime(synthetic_executor=lambda _: copy.deepcopy(OUTPUT), semantic_verifier=lambda _: {"integrity_result": "PASS", "violations": ["bad"]}, test_sandbox=True)
        response = runtime.execute(assignment("SI-STRUCT-06"))
        assert response["runtime_status"] == "FAIL_SAFE" and response["runtime_failure_code"] == "SEMANTIC_VERIFIER_FAILURE", response
        return "malformed verifier result fails safe"
    results.append(run_case("SI-STRUCT-06", malformed_verifier_result_rejected))

    def schema_is_strict() -> str:
        verifier = object.__new__(SemanticAssignmentIntegrityVerifier)
        try:
            verifier._validate_result({"integrity_result": "PASS", "violations": [{"category": "UNSUPPORTED_STORY_FACT"}]})
        except SemanticIntegrityError:
            return "strict verifier schema rejects incomplete violation"
        raise AssertionError("incomplete violation was accepted")
    results.append(run_case("SI-STRUCT-07", schema_is_strict))

    def provider_neutrality() -> str:
        source = inspect.getsource(SemanticAssignmentIntegrityVerifier)
        assert "DeepSeekProviderAdapter" not in source and "DEEPSEEK_API_KEY" not in source and "base_url" not in source, source
        assert "model_executor.execute(" in source, source
        return "verifier uses shared ModelExecutor with no provider-specific client"
    results.append(run_case("SI-STRUCT-08", provider_neutrality))

    def no_lexical_arms_race() -> str:
        source = Path(__file__).resolve().parents[1] / "runtime" / "scene_writer" / "semantic_assignment_integrity.py"
        text = source.read_text(encoding="utf-8")
        for forbidden in ("最熟悉", "最了解", "most familiar", "knows better than"):
            assert forbidden not in text, forbidden
        return "semantic verifier contains no capability synonym catalogue"
    results.append(run_case("SI-STRUCT-09", no_lexical_arms_race))

    def frozen_skill() -> str:
        runtime = SceneWriterRuntime()
        assert sha256_file(runtime.canonical_skill_path).lower() == EXPECTED_HASH
        return "canonical scene-writer remains frozen at the approved hash"
    results.append(run_case("SI-STRUCT-10", frozen_skill))

    report = {"classification": "NON-NETWORK SEMANTIC ASSIGNMENT INTEGRITY STRUCTURAL TEST", "results": results, "passed": sum(item["result"] == "PASS" for item in results), "total": len(results)}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] == report["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
