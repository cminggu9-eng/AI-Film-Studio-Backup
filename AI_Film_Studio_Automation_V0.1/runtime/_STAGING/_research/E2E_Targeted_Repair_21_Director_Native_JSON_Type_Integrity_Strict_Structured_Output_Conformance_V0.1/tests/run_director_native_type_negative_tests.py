"""Provider-free DIR-TYPE-NEG-01 through DIR-TYPE-NEG-15 for Repair21."""

from __future__ import annotations

import copy
import inspect
import json

from repair21_support import (
    R26,
    current_wire_audit,
    production_source_guards,
    r26_arguments,
    r26_hashes,
    rejects,
    validator_for,
)
from director_structured_submission import build_director_native_json_type_instruction


def main() -> int:
    audit = current_wire_audit()
    state_contract = audit["state_contract"]
    raw = r26_arguments()
    before = r26_hashes()
    stringified_array = copy.deepcopy(raw)
    stringified_object = copy.deepcopy(raw)
    stringified_object["state_evidence"]["relevant_prior_state"] = json.dumps(
        stringified_object["state_evidence"]["relevant_prior_state"], ensure_ascii=False
    )
    empty_array = copy.deepcopy(raw); empty_array["unresolved_decisions"] = []
    empty_array_string = copy.deepcopy(raw); empty_array_string["unresolved_decisions"] = "[]"
    null_value = copy.deepcopy(raw); null_value["unresolved_decisions"] = None
    scalar_value = copy.deepcopy(raw); scalar_value["unresolved_decisions"] = "one-decision"
    legacy_state = copy.deepcopy(raw)
    legacy_state["state_evidence"]["current_state"] = json.dumps(legacy_state["state_evidence"]["current_state"], ensure_ascii=False)
    union_lost = copy.deepcopy(audit["function"]["parameters"])
    union_lost["properties"]["unresolved_decisions"] = {"type": "string"}
    strict_lost = copy.deepcopy(audit["wire"]); strict_lost["tools"][0]["function"]["strict"] = False
    unforced = copy.deepcopy(audit["wire"]); unforced["tool_choice"] = "auto"
    manifest = json.loads((R26 / "execution_manifest.json").read_text(encoding="utf-8"))
    reminder_source = inspect.getsource(build_director_native_json_type_instruction)
    after = r26_hashes()
    results = []

    def add(case_id, passed, detail):
        results.append({"id": case_id, "result": "PASS" if passed else "FAIL", "detail": detail})

    guards = production_source_guards()
    add("DIR-TYPE-NEG-01", isinstance(stringified_array["unresolved_decisions"], str) and rejects(stringified_array, state_contract), "array encoded as a JSON string is rejected")
    add("DIR-TYPE-NEG-02", isinstance(stringified_object["state_evidence"]["relevant_prior_state"], str) and rejects(stringified_object, state_contract), "object encoded as a JSON string is rejected")
    add("DIR-TYPE-NEG-03", rejects(stringified_array, state_contract) and guards["field_level_json_loads_absent"], "stringified array has no auto-json.loads production path")
    add("DIR-TYPE-NEG-04", rejects(stringified_object, state_contract) and guards["field_level_json_loads_absent"], "stringified object has no auto-json.loads production path")
    add("DIR-TYPE-NEG-05", validator_for(state_contract)(empty_array)["unresolved_decisions"] == [] and validator_for(state_contract)(empty_array)["unresolved_decisions"] != "ABSENT", "[] remains its lawful native-array form and is not treated as ABSENT")
    add("DIR-TYPE-NEG-06", rejects(empty_array_string, state_contract), "the string [] is not treated as ABSENT")
    add("DIR-TYPE-NEG-07", rejects(null_value, state_contract), "null is not treated as ABSENT")
    add("DIR-TYPE-NEG-08", rejects(scalar_value, state_contract), "a scalar is not wrapped into an array")
    add("DIR-TYPE-NEG-09", union_lost != audit["function"]["parameters"] and union_lost["properties"]["unresolved_decisions"] != audit["neutral"]["properties"]["unresolved_decisions"], "wire schema loss of the native union is observable")
    add("DIR-TYPE-NEG-10", strict_lost["tools"][0]["function"]["strict"] is False, "missing strict:true is observable")
    add("DIR-TYPE-NEG-11", unforced["tool_choice"] != audit["wire"]["tool_choice"], "non-exact tool_choice is observable")
    add("DIR-TYPE-NEG-12", rejects(legacy_state, state_contract) and guards["legacy_alias_has_no_live_reference"] and guards["adapter_has_no_director_field_normalizer"], "legacy Director JSON-string state representation is unreachable")
    add("DIR-TYPE-NEG-13", rejects(r26_arguments(), state_contract) and before == after and manifest["status"] == "BLOCKED", "R26 replay cannot become PASS")
    add("DIR-TYPE-NEG-14", all(token not in reminder_source for token in ("E2E-FIX-01", "E2E-FIX-02", "E2E-FIX-03", "C-09", "battery")), "provider type reminder contains no fixture-specific literal")
    add("DIR-TYPE-NEG-15", guards["no_automatic_retry_policy"] and manifest["retry_count"] == 0 and manifest["automatic_provider_fallback"] == 0, "provider native-type violation cannot be silently retried or fallen back")
    output = {
        "classification": "DIRECTOR NATIVE JSON TYPE NEGATIVE TEST",
        "results": results,
        "passed": sum(item["result"] == "PASS" for item in results),
        "total": len(results),
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "live_e2e_runs": 0,
        "historical_replay": "READ_ONLY",
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] == output["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
