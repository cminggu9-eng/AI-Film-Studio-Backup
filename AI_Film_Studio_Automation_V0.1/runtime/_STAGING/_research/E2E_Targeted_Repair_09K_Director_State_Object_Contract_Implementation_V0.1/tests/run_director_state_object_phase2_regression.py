from __future__ import annotations

import copy
import json

from director_state_object_test_support import check, compile_fixture, rejected, result_payload, valid_payload
from director_state_object_contract import lint_deepseek_strict_schema
from director_provider_compatibility import deepseek_compatible_schema, equivalence_report
from director_structured_submission import director_submission_schema, make_director_payload_validator


def main() -> int:
    compiled, contract, _ = compile_fixture()
    schema = director_submission_schema(contract)
    strict = deepseek_compatible_schema(contract)
    validator = make_director_payload_validator(selected_mode="PLAN", required_locks=["lock"], prohibited_changes=["prohibition"], state_contract=contract)
    payload = valid_payload(contract)
    results: list[dict[str, object]] = []
    state = schema["properties"]["state_evidence"]["properties"]
    strict_state = strict["properties"]["state_evidence"]["properties"]
    check(results, "DIR-OBJ-P2-01", len(schema["required"]) == 15 and set(schema["required"]) == set(schema["properties"]), "outer 15 fields remain exact")
    check(results, "DIR-OBJ-P2-02", state["relevant_prior_state"]["type"] == "object", "prior remains an object")
    check(results, "DIR-OBJ-P2-03", state["current_state"]["type"] == "object", "current remains an object")
    check(results, "DIR-OBJ-P2-04", all(state[field] == {"const": "ABSENT"} for field in ("proposed_state", "knowledge_timing", "visual_state")), "neutral exact ABSENT")
    check(results, "DIR-OBJ-P2-05", all(strict_state[field] == {"type": "string", "enum": ["ABSENT"]} for field in ("proposed_state", "knowledge_timing", "visual_state")), "strict typed ABSENT")
    check(results, "DIR-OBJ-P2-06", lint_deepseek_strict_schema(strict)["result"] == "PASS", "strict schema lint")
    check(results, "DIR-OBJ-P2-07", equivalence_report(contract)["dynamic_object_representation_preserved"], "provider projection preserves objects")
    validated = validator(payload)
    check(results, "DIR-OBJ-P2-08", isinstance(validated["state_evidence"]["current_state"], dict), "downstream carriage stays object")
    legacy = valid_payload(contract)
    legacy["state_evidence"]["current_state"] = json.dumps(legacy["state_evidence"]["current_state"])
    check(results, "DIR-OBJ-P2-09", rejected(lambda: validator(legacy)), "legacy string rejected")
    extra = valid_payload(contract)
    scene_id = compiled["scene_ids"][0]
    extra["state_evidence"]["current_state"][scene_id]["unexpected"] = "x"
    check(results, "DIR-OBJ-P2-10", rejected(lambda: validator(extra)), "closed nested object")
    check(results, "DIR-OBJ-P2-11", contract["legacy_string_path"] == "UNREACHABLE", "legacy path unreachable")
    check(results, "DIR-OBJ-P2-12", contract["authority"]["authority_id"] == "REPAIR_09J_DIRECTOR_STATE_PROJECTION_AUTHORITY_V0.1", "09J is implementation authority")
    output = result_payload(results, classification="SYSTEMIC PHASE2 DIRECTOR STATE OBJECT REGRESSION")
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["result"] == "PASS" and output["total"] == 12 else 1


if __name__ == "__main__":
    raise SystemExit(main())
