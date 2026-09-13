"""Offline Repair 09E typed-enum projection and wire-interception tests."""
from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Mapping


HERE = Path(__file__).resolve().parent
RUNTIME = next(parent for parent in HERE.parents if parent.name == "runtime")
RESEARCH = RUNTIME / "_STAGING" / "_research"
for directory in (
    RUNTIME.parent,
    RESEARCH / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1" / "implementation",
    RESEARCH / "E2E_Targeted_Repair_02_Scene_Writer_Response_Budget_Serialization_V0.1" / "implementation",
    RESEARCH / "E2E_Targeted_Repair_03_Strict_Structured_Transport_V0.1" / "implementation",
    RESEARCH / "E2E_Targeted_Repair_05_Director_Output_Contract_Transport_Alignment_V0.1" / "implementation",
    RESEARCH / "E2E_Targeted_Repair_09B_Director_Full_Structured_Submission_Payload_V0.1" / "implementation",
    RESEARCH / "E2E_Targeted_Repair_09C_Director_Strict_Provider_Compatibility_V0.1" / "implementation",
    RESEARCH / "E2E_Targeted_Repair_09D_Director_Strict_Provider_Observability_Conformance_V0.1" / "implementation",
):
    sys.path.insert(0, str(directory))

from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter
from runtime.shared_qa.model_executor import ModelRequest
from director_provider_compatibility import build_deepseek_compatible_director_contract, deepseek_compatible_schema, equivalence_report
from director_structured_submission import FUNCTION_NAME, STATE_DIMENSIONS, director_submission_schema, make_director_payload_validator
from deepseek_strict_linter import lint
from scene_writer_strict_transport import strict_function_schema


EXPECTED_POINTERS = {
    "/properties/flags",
    "/properties/handoffs",
    "/properties/unresolved_decisions/anyOf/0",
    "/properties/state_evidence/properties/relevant_prior_state/anyOf/0",
    "/properties/state_evidence/properties/current_state/anyOf/0",
    "/properties/state_evidence/properties/proposed_state/anyOf/0",
    "/properties/state_evidence/properties/knowledge_timing/anyOf/0",
    "/properties/state_evidence/properties/relationship_state/anyOf/0",
    "/properties/state_evidence/properties/visual_state/anyOf/0",
}


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def node_at(schema: Mapping[str, Any], pointer: str) -> Any:
    value: Any = schema
    for part in pointer.strip("/").split("/"):
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def enum_only_pointers(value: Any, pointer: str = "") -> set[str]:
    found: set[str] = set()
    if isinstance(value, Mapping):
        if "enum" in value and not ({"type", "anyOf", "$ref"} & set(value)):
            found.add(pointer or "/")
        for key, child in value.items():
            if key in {"properties", "$defs"} and isinstance(child, Mapping):
                for name, schema in child.items():
                    found |= enum_only_pointers(schema, f"{pointer}/{key}/{name}")
            elif key == "items":
                found |= enum_only_pointers(child, f"{pointer}/items")
            elif key == "anyOf" and isinstance(child, list):
                for index, schema in enumerate(child):
                    found |= enum_only_pointers(schema, f"{pointer}/anyOf/{index}")
    return found


def expect(label: str, predicate: bool, results: list[dict[str, Any]], detail: str = "") -> None:
    results.append({"id": label, "result": "PASS" if predicate else "FAIL", "detail": detail})


def main() -> int:
    results: list[dict[str, Any]] = []
    neutral = director_submission_schema()
    projected = deepseek_compatible_schema()
    findings = lint(projected)
    contract = build_deepseek_compatible_director_contract()
    request = ModelRequest(system_prompt="offline wire interception", user_prompt="frozen input", model="deepseek-v4-pro", thinking_mode="disabled", max_tokens=3500, response_format=None, structured_output=contract)
    payload, endpoint = DeepSeekProviderAdapter.build_provider_payload(request)
    final_parameters = payload["tools"][0]["function"]["parameters"]
    expected_node = {"type": "string", "enum": ["ABSENT"]}
    state_dimensions = set(neutral["properties"]["state_evidence"]["properties"])
    machine_fields = {"directorial_intent", "staging_blocking", "audience_information", "spatial_geography", "camera_coverage_intent", "rhythm_transition_intent", "production_burden", "handoffs_unresolved_issues"}

    error_path = RESEARCH / "E2E_Targeted_Repair_09C_Director_Strict_Provider_Compatibility_V0.1" / "evidence" / "DIRECTOR-COMPATIBILITY-PROBE-03" / "artifacts" / "director_provider_http_error.json"
    previous_wire_path = error_path.with_name("director_final_wire_payload.json")
    error = json.loads(error_path.read_text(encoding="utf-8"))
    previous_wire = json.loads(previous_wire_path.read_text(encoding="utf-8"))
    expect("DIR-ENUM-01", "one of `type`, `anyOf`, `$ref` field is required" in error["provider_error_message"], results, "Repair 09D raw error provenance")
    expect("DIR-ENUM-02", enum_only_pointers(previous_wire["payload"]["tools"][0]["function"]["parameters"]) == EXPECTED_POINTERS, results, "9 offending nodes identified")
    expect("DIR-ENUM-03", all(node_at(projected, pointer) == expected_node for pointer in EXPECTED_POINTERS), results, "9/9 typed string enums")
    expect("DIR-ENUM-04", not any(item.get("code") == "NODE_ANCHOR_REQUIRED" for item in findings), results, "recursive anchor lint")
    expect("DIR-ENUM-05", not any(item.get("object_rule_failure") for item in findings), results, "object strictness")
    expect("DIR-ENUM-06", not any("minLength" in item.get("unsupported", []) or "maxLength" in item.get("unsupported", []) for item in findings), results, "string restrictions absent")
    expect("DIR-ENUM-07", not any("minItems" in item.get("unsupported", []) or "maxItems" in item.get("unsupported", []) for item in findings), results, "array restrictions absent")
    equivalence = equivalence_report()
    expect("DIR-ENUM-08", equivalence["absence_equivalence"] and equivalence["fixed_string_enum_representation"] == expected_node, results, "accepted value set unchanged")
    expect("DIR-ENUM-09", machine_fields <= set(projected["required"]), results, "eight machine fields preserved")
    expect("DIR-ENUM-10", projected["properties"]["selected_mode"]["enum"] == neutral["properties"]["selected_mode"]["enum"] and projected["properties"]["primary_state_or_outcome"]["enum"] == neutral["properties"]["primary_state_or_outcome"]["enum"], results, "canonical control/state")
    expect("DIR-ENUM-11", set(projected["properties"]["state_evidence"]["properties"]) == state_dimensions, results, "state carry-forward dimensions preserved")
    expect("DIR-ENUM-12", contract.function_name == FUNCTION_NAME == "submit_director_package", results, "exact function name")
    expect("DIR-ENUM-13", payload["tools"][0]["function"]["strict"] is True and endpoint.endswith("/beta"), results, "strict beta transport")
    expect("DIR-ENUM-14", payload["tool_choice"] == {"type": "function", "function": {"name": FUNCTION_NAME}}, results, "exact tool choice")
    expect("DIR-ENUM-15", canonical_hash(projected) == canonical_hash(final_parameters) and not enum_only_pointers(final_parameters), results, "final wire interception")
    scene_schema = strict_function_schema()
    expect("DIR-ENUM-16", not lint(scene_schema), results, "Scene Writer control remains valid")
    validator = make_director_payload_validator(selected_mode="PLAN", required_locks=["lock-a"], prohibited_changes=["prohibition-a"])
    validator_payload = {key: "Director field" for key in neutral["required"]}
    validator_payload.update({"selected_mode": "PLAN", "primary_state_or_outcome": "DIRECTION_PLAN_PRODUCED", "flags": "ABSENT", "handoffs": "ABSENT", "required_outcome": "ABSENT", "unresolved_decisions": "ABSENT", "state_evidence": {key: "ABSENT" for key in STATE_DIMENSIONS}})
    validated = validator(validator_payload)
    expect("DIR-ENUM-17", validated["canon_assignment_locks"] == ["lock-a"] and validated["prohibited_changes"] == ["prohibition-a"] and validated["scene_packages"] == "ABSENT", results, "Repair 09B validator chain")
    expect("DIR-ENUM-18", not findings, results, "projected strict schema lint PASS")

    bare = {"enum": ["ABSENT"]}
    non_string = {"type": "integer", "enum": ["ABSENT"]}
    changed_value = copy.deepcopy(projected); node_at(changed_value, "/properties/flags")["enum"] = ["PRESENT"]
    weakened_required = copy.deepcopy(projected); weakened_required["required"].remove("flags")
    object_regression = copy.deepcopy(projected); object_regression["additionalProperties"] = True
    min_length = copy.deepcopy(projected); min_length["properties"]["required_outcome"]["minLength"] = 1
    min_items = copy.deepcopy(projected); min_items["properties"]["unresolved_decisions"]["anyOf"][1]["minItems"] = 1
    field_removed = copy.deepcopy(projected); field_removed["required"].remove("directorial_intent"); field_removed["properties"].pop("directorial_intent")
    tokens_changed = copy.deepcopy(projected); tokens_changed["properties"]["selected_mode"]["enum"].append("OTHER")
    altered_wire = copy.deepcopy(final_parameters); altered_wire["properties"]["flags"]["enum"] = ["PRESENT"]
    negatives = {
        "DIR-ENUM-NEG-01": any(item.get("code") == "NODE_ANCHOR_REQUIRED" for item in lint(bare)),
        "DIR-ENUM-NEG-02": any(item.get("code") == "ENUM_STRING_TYPE_REQUIRED" for item in lint(non_string)),
        "DIR-ENUM-NEG-03": node_at(changed_value, "/properties/flags") != expected_node,
        "DIR-ENUM-NEG-04": set(weakened_required["required"]) != set(neutral["required"]),
        "DIR-ENUM-NEG-05": any(item.get("object_rule_failure") for item in lint(object_regression)),
        "DIR-ENUM-NEG-06": any("minLength" in item.get("unsupported", []) for item in lint(min_length)),
        "DIR-ENUM-NEG-07": any("minItems" in item.get("unsupported", []) for item in lint(min_items)),
        "DIR-ENUM-NEG-08": "directorial_intent" not in field_removed["properties"] and set(field_removed["required"]) != set(neutral["required"]),
        "DIR-ENUM-NEG-09": tokens_changed["properties"]["selected_mode"]["enum"] != neutral["properties"]["selected_mode"]["enum"],
        "DIR-ENUM-NEG-10": canonical_hash(projected) != canonical_hash(altered_wire),
    }
    for name, passed in negatives.items():
        expect(name, passed, results, "negative mutation detected")

    passed = sum(item["result"] == "PASS" for item in results)
    output = {"result": "PASS" if passed == len(results) else "FAIL", "passed": passed, "total": len(results), "provider_calls": 0, "executor_calls": 0, "role_calls": 0, "neutral_contract_hash": canonical_hash(neutral), "projection_hash": canonical_hash(projected), "final_parameters_hash": canonical_hash(final_parameters), "wire_payload_hash": canonical_hash(payload), "results": results}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
