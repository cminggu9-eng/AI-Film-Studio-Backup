"""One-pass real-provider semantic-verifier matrix; it never generates a scene."""

from __future__ import annotations

import copy
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

from runtime.scene_writer.scene_writer_executor_binding import create_scene_writer_binding  # noqa: E402
from runtime.scene_writer.semantic_assignment_integrity import build_assignment_constraint_ledger  # noqa: E402


def base_assignment() -> Dict[str, Any]:
    return {
        "request_id": "SI-SW-BASE",
        "requested_mode": "CREATE",
        "output_language": "en-US",
        "scene_id": "SEMANTIC-INTEGRITY-MATRIX",
        "canon_locks": ["The absent presenter cannot attend. The specific reason is unknown.", "Lin Yan does not know the reason."],
        "showrunner_locks": ["Chen Mo conditionally accepts if Lin Yan sends all existing materials tonight."],
        "participants": [
            {"name": "Lin Yan", "knowledge": "She knows the presenter cannot attend, but not why.", "constraint": "She may not explain the absent presenter without permission."},
            {"name": "Chen Mo", "capacity": "Can take over the presentation.", "constraint": "He has not agreed immediately."},
        ],
        "character_context": {"relationship": "colleagues under immediate work pressure, not enemies"},
        "required_event": "Lin Yan asks Chen Mo to take tomorrow morning's presentation.",
        "required_information": "The original presenter cannot attend tomorrow morning; the reason is unknown.",
        "required_outcome": "Chen Mo accepts only if all existing materials are sent tonight.",
        "prior_scene_state": "Only Lin Yan and Chen Mo remain in the meeting room after a meeting.",
        "desired_post_state": "Chen Mo conditionally accepts and Lin Yan must send existing materials tonight.",
    }


CONTROL = {
    "primary_state": "SCENE_CREATED",
    "flags": [],
    "handoffs": [],
    "scene_function": "Test semantic assignment compliance.",
    "objectives": "Lin Yan requests; Chen Mo seeks conditions.",
    "resistance": "Chen Mo does not agree immediately.",
    "turn": "A request becomes conditional acceptance.",
}


def verifier_input(case_id: str, content: str, assignment: Dict[str, Any] | None = None) -> Dict[str, Any]:
    source = assignment or base_assignment()
    return {
        "assignment_constraint_ledger": build_assignment_constraint_ledger(source),
        "generated_creative_deliverable": {"kind": "scene", "content": content},
        "relevant_control_data": copy.deepcopy(CONTROL),
        "runtime": {"invocation_id": f"semantic-integrity-suite:{case_id}", "classification": "REAL PROVIDER VERIFIER-ONLY TEST"},
    }


def test_case(case_id: str, content: str, expected_result: str, expected_category: str | None = None) -> Dict[str, Any]:
    return {"id": case_id, "content": content, "expected_result": expected_result, "expected_category": expected_category}


TESTS = [
    test_case("SI-SW-01", "Lin Yan says: 'You are one of the people most familiar with the whole project, so you should take it.'", "FAIL", "UNAUTHORIZED_CAPABILITY_FACT"),
    test_case("SI-SW-02", "Lin Yan says: 'The presenter has a temporary issue, so he cannot come.'", "FAIL", "EXPLICIT_UNKNOWN_NARROWING"),
    test_case("SI-SW-03", "Lin Yan says: 'The materials must be sent by midnight.'", "FAIL", "UNAUTHORIZED_TEMPORAL_SPECIFICITY"),
    test_case("SI-SW-04", "Chen Mo says: 'I know exactly why the presenter cannot attend.'", "FAIL", "CHARACTER_KNOWLEDGE_LEAK"),
    test_case("SI-SW-05", "Lin Yan says: 'We handled the same crisis together last time.'", "FAIL", "UNAUTHORIZED_RELATIONSHIP_FACT"),
    test_case("SI-SW-06", "Lin Yan closes her laptop. Chen Mo sits down, pauses, and lifts his water cup before answering.", "PASS"),
    test_case("SI-SW-07", "Chen Mo looks at the folder and asks, 'This is so sudden?'", "PASS"),
    test_case("SI-SW-08", "Chen Mo says: 'If you send all the existing materials tonight, I will take it for now.'", "PASS"),
    test_case("SI-SW-09", "Lin Yan says: 'I do not know why the presenter cannot attend. Maybe there is a reason, but I will not guess.'", "PASS"),
    test_case("SI-SW-10", "Chen Mo moves the chair back, waits for a beat, then asks, 'Can you send the existing materials tonight?'", "PASS"),
]

PARAPHRASES = [
    test_case("SI-PARA-01", "You know this project best.", "FAIL", "UNAUTHORIZED_CAPABILITY_FACT"),
    test_case("SI-PARA-02", "You are the clearest on the overall situation.", "FAIL", "UNAUTHORIZED_CAPABILITY_FACT"),
    test_case("SI-PARA-03", "No one in the whole group understands it better than you.", "FAIL", "UNAUTHORIZED_CAPABILITY_FACT"),
    test_case("SI-PARA-04", "There are not many people more familiar with this project than you.", "FAIL", "UNAUTHORIZED_CAPABILITY_FACT"),
    test_case("SI-PARA-05", "You are one of the people who understands this project most deeply.", "FAIL", "UNAUTHORIZED_CAPABILITY_FACT"),
]

FALSE_POSITIVES = [
    test_case("SI-FP-01", "Lin Yan asks: 'Can you take it?'", "PASS"),
    test_case("SI-FP-02", "Chen Mo says: 'If you can send it tonight, I will take it.'", "PASS"),
]


def evaluate(bundle, case: Dict[str, Any]) -> Dict[str, Any]:
    response = bundle.semantic_verifier(verifier_input(case["id"], case["content"]))
    categories = [item["category"] for item in response["violations"]]
    passed = response["integrity_result"] == case["expected_result"]
    if case["expected_category"] is not None:
        passed = passed and case["expected_category"] in categories
    usage = bundle.semantic_verifier.usage_for(f"semantic-integrity-suite:{case['id']}")
    return {
        "id": case["id"], "expected_result": case["expected_result"], "expected_category": case["expected_category"],
        "actual": response, "categories": categories, "result": "PASS" if passed else "FAIL", "usage": usage,
    }


def main() -> int:
    if not os.environ.get("DEEPSEEK_API_KEY", "").strip():
        print(json.dumps({"key_status": "NOT AVAILABLE", "results": []}, ensure_ascii=False, indent=2))
        return 1
    bundle = create_scene_writer_binding(execution_classification="REAL PROVIDER VERIFIER-ONLY TEST")
    reports = []
    for case in TESTS + PARAPHRASES + FALSE_POSITIVES:
        try:
            reports.append(evaluate(bundle, case))
        except Exception as exc:
            reports.append({"id": case["id"], "result": "FAIL", "exception": f"{type(exc).__name__}: {exc}"})
            break
    completed = len(reports) == len(TESTS) + len(PARAPHRASES) + len(FALSE_POSITIVES)
    payload = {
        "classification": "REAL PROVIDER SEMANTIC VERIFIER-ONLY TEST; NO SCENE GENERATION",
        "provider": bundle.provider.provider,
        "model": bundle.provider.model,
        "results": reports,
        "passed": sum(item.get("result") == "PASS" for item in reports),
        "total": len(TESTS) + len(PARAPHRASES) + len(FALSE_POSITIVES),
        "completed": completed,
        "pricing_basis": bundle.provider.pricing_basis(),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if completed and payload["passed"] == payload["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
