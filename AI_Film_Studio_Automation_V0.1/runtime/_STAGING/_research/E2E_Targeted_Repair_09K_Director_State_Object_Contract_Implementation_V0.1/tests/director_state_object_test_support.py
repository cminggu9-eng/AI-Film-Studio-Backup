from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Mapping


HERE = Path(__file__).resolve()
AUTOMATION_ROOT = next(parent for parent in HERE.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research"
FIXTURE_ROOT = RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1" / "fixtures"
IMPLEMENTATION_09B = RESEARCH / "E2E_Targeted_Repair_09B_Director_Full_Structured_Submission_Payload_V0.1" / "implementation"
IMPLEMENTATION_09C = RESEARCH / "E2E_Targeted_Repair_09C_Director_Strict_Provider_Compatibility_V0.1" / "implementation"
IMPLEMENTATION_07 = RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1" / "implementation"
IMPLEMENTATION_05 = RESEARCH / "E2E_Targeted_Repair_05_Director_Output_Contract_Transport_Alignment_V0.1" / "implementation"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
for path in (IMPLEMENTATION_09C, IMPLEMENTATION_09B, IMPLEMENTATION_07, IMPLEMENTATION_05, HARNESS, AUTOMATION_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from fixture_contract_compiler import compile_path
from director_state_object_contract import compile_director_state_object_contract
from director_structured_submission import SEMANTIC_FIELD_IDS


FIXTURES = {
    "E2E-FIX-01": FIXTURE_ROOT / "E2E_FIX_01_Runtime_Binding_V0.1.json",
    "E2E-FIX-02": FIXTURE_ROOT / "E2E_FIX_02_Runtime_Binding_V0.1.json",
    "E2E-FIX-03": FIXTURE_ROOT / "E2E_FIX_03_Runtime_Binding_V0.1.json",
}


def records(compiled: Mapping[str, Any]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for sequence, scene_id in enumerate(compiled["scene_ids"], start=1):
        snapshot = {
            dimension: values[0] if sequence == 1 else values[-1]
            for dimension, values in compiled["state_enums"].items()
        }
        output.append({
            "scene_id": scene_id,
            "source_record_id": f"TEST/scene_writer/{scene_id}",
            "source_version": "TEST-V0.1",
            "canonical_owner": "Scene Writer",
            "lifecycle_state": "STATE_LEDGER_COMMITTED",
            "ledger_sequence": sequence,
            "state_snapshot": snapshot,
        })
    return output


def compile_fixture(fixture_id: str = "E2E-FIX-01") -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    compiled = compile_path(FIXTURES[fixture_id])
    ledger_records = records(compiled)
    contract = compile_director_state_object_contract(
        compiled_run_contract=compiled,
        validated_upstream_state_records=(),
        run_local_state_ledger_records=ledger_records,
        required_locks=compiled["fixture"]["decision_locks"],
        transition_authority_records=compiled["fixture"]["authorized_transitions"],
    )
    return compiled, contract, ledger_records


def valid_payload(contract: Mapping[str, Any]) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "selected_mode": "PLAN",
        "primary_state_or_outcome": "DIRECTION_PLAN_PRODUCED",
        "flags": "ABSENT",
        "handoffs": "ABSENT",
        "required_outcome": "Preserve upstream state and deliver the direction plan.",
        "unresolved_decisions": "ABSENT",
        "state_evidence": {**copy.deepcopy(contract["expected_state_values"]), "relationship_state": "ABSENT"},
    }
    payload.update({field: f"{field} verified Director deliverable" for field in SEMANTIC_FIELD_IDS})
    return payload


def read_recorded_arguments(path: Path) -> dict[str, Any]:
    persisted = json.loads(path.read_text(encoding="utf-8"))
    return json.loads(persisted["tool_calls"][0]["function"]["arguments"])


def result_payload(results: list[dict[str, Any]], *, classification: str) -> dict[str, Any]:
    passed = sum(item["result"] == "PASS" for item in results)
    return {
        "classification": classification,
        "passed": passed,
        "total": len(results),
        "result": "PASS" if passed == len(results) else "FAIL",
        "results": results,
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "e2e_runs": 0,
    }


def check(results: list[dict[str, Any]], test_id: str, condition: bool, detail: str) -> None:
    results.append({"id": test_id, "result": "PASS" if condition else "FAIL", "detail": detail})


def rejected(callable_value: Any) -> bool:
    try:
        callable_value()
    except Exception:
        return True
    return False
