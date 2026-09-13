from __future__ import annotations

import copy
import json
from pathlib import Path

from director_state_object_test_support import check, compile_fixture, rejected, result_payload, valid_payload
from director_state_object_test_support import IMPLEMENTATION_09B
from director_state_object_contract import compile_director_state_object_contract, stable_hash
from director_structured_submission import (
    assert_director_contract_identity,
    director_prompt_contract_manifest,
    director_structured_contract_manifest,
    director_submission_schema,
    director_validator_contract_manifest,
    make_director_payload_validator,
)


def main() -> int:
    compiled, contract, ledger_records = compile_fixture()
    validator = make_director_payload_validator(selected_mode="PLAN", required_locks=["lock"], prohibited_changes=["prohibition"], state_contract=contract)
    results: list[dict[str, object]] = []
    compiler_source = (IMPLEMENTATION_09B / "director_state_object_contract.py").read_text(encoding="utf-8")
    forbidden = ("A-17", "裂口白瓷碗", "C-09", "许宁", "许曼", "周岚", "周启", "沈泊", "梁音", "E2E-FIX-01", "E2E-FIX-02", "E2E-FIX-03")
    check(results, "DIR-OBJ-NEG-01", not any(item in compiler_source for item in forbidden), "fixture/story literals are absent from compiler source")

    payload = valid_payload(contract)
    first_scene = compiled["scene_ids"][0]
    dimension = next(iter(compiled["state_enums"]))
    payload["state_evidence"]["current_state"][first_scene]["model_dynamic_key"] = "model-value"
    check(results, "DIR-OBJ-NEG-02", rejected(lambda: validator(payload)), "model-defined dynamic key rejected")

    tampered = copy.deepcopy(contract)
    tampered["source_trace"][0].pop("source_contract_pointer")
    tampered["source_trace_hash"] = stable_hash(tampered["source_trace"])
    trace_validator = make_director_payload_validator(selected_mode="PLAN", required_locks=["lock"], prohibited_changes=["prohibition"], state_contract=tampered)
    check(results, "DIR-OBJ-NEG-03", rejected(lambda: trace_validator(valid_payload(tampered))), "trace property without source pointer rejected")

    payload = valid_payload(contract)
    value = payload["state_evidence"]["current_state"].pop(first_scene)
    payload["state_evidence"]["current_state"]["WRONG-SCENE"] = value
    check(results, "DIR-OBJ-NEG-04", rejected(lambda: validator(payload)), "wrong scene key rejected")

    payload = valid_payload(contract)
    value = payload["state_evidence"]["current_state"][first_scene].pop(dimension)
    payload["state_evidence"]["current_state"][first_scene]["wrong_dimension"] = value
    check(results, "DIR-OBJ-NEG-05", rejected(lambda: validator(payload)), "wrong state dimension rejected")

    payload = valid_payload(contract)
    payload["state_evidence"]["current_state"][first_scene][dimension] = "INVALID_ENUM_TOKEN"
    check(results, "DIR-OBJ-NEG-06", rejected(lambda: validator(payload)), "invalid enum rejected")

    conflict = copy.deepcopy(ledger_records[0])
    conflict["state_snapshot"][dimension] = compiled["state_enums"][dimension][-1]
    conflict["source_record_id"] = "TEST/scene_writer/conflict"
    conflict_records = [*ledger_records, conflict]
    check(results, "DIR-OBJ-NEG-07", rejected(lambda: compile_director_state_object_contract(compiled_run_contract=compiled, validated_upstream_state_records=(), run_local_state_ledger_records=conflict_records, required_locks=["lock"], transition_authority_records=())), "source conflict fails compile instead of becoming ABSENT")

    check(results, "DIR-OBJ-NEG-08", rejected(lambda: compile_director_state_object_contract(compiled_run_contract=compiled, validated_upstream_state_records=(), run_local_state_ledger_records=ledger_records[:-1], required_locks=["lock"], transition_authority_records=())), "missing source fails compile instead of becoming ABSENT")

    for test_id, field in (("DIR-OBJ-NEG-09", "proposed_state"), ("DIR-OBJ-NEG-10", "knowledge_timing"), ("DIR-OBJ-NEG-11", "visual_state")):
        payload = valid_payload(contract)
        payload["state_evidence"][field] = {}
        check(results, test_id, rejected(lambda value=payload: validator(value)), f"{field} object rejected")

    payload = valid_payload(contract)
    payload["state_evidence"]["current_state"] = json.dumps(payload["state_evidence"]["current_state"], ensure_ascii=False)
    check(results, "DIR-OBJ-NEG-12", rejected(lambda: validator(payload)), "legacy JSON-object-string rejected")

    payload = valid_payload(contract)
    payload["state_evidence"]["current_state"][first_scene]["additional_nested_key"] = "x"
    check(results, "DIR-OBJ-NEG-13", rejected(lambda: validator(payload)), "additional nested key rejected")

    drift_schema = director_submission_schema(contract)
    drift_schema["properties"]["scene_packages"] = {"const": "ABSENT"}
    drift_schema["required"].append("scene_packages")
    check(results, "DIR-OBJ-NEG-14", rejected(lambda: director_prompt_contract_manifest(drift_schema)), "prompt/function outer manifest drift rejected")

    function_manifest = director_structured_contract_manifest(director_submission_schema(contract))
    validator_manifest = director_validator_contract_manifest(contract)
    drifted_validator_manifest = copy.deepcopy(validator_manifest)
    drifted_validator_manifest["compiled_state_schema_hash"] = "drift"
    check(results, "DIR-OBJ-NEG-15", rejected(lambda: assert_director_contract_identity(function_manifest, function_manifest, drifted_validator_manifest)), "validator/function manifest drift rejected")

    output = result_payload(results, classification="DIRECTOR STATE OBJECT NEGATIVE TESTS")
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["result"] == "PASS" and output["total"] == 15 else 1


if __name__ == "__main__":
    raise SystemExit(main())
