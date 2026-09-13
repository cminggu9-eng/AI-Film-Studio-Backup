"""Provider-free DIR-TYPE-01 through DIR-TYPE-20 for Repair21."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from repair21_support import (
    AUTOMATION_ROOT,
    REPAIR_09K,
    REPAIR_20,
    current_integrity,
    current_wire_audit,
    absent_payload,
    native_array_payload,
    production_source_guards,
    r26_arguments,
    r26_diagnostic_inner_array,
    r26_hashes,
    r26_wire_payload,
    rejects,
    validator_for,
)

REPAIR21_GATES = Path(__file__).resolve().parent / "run_repair21_offline_gates.py"
GATE_REPORT = Path(__file__).resolve().parents[1] / "reports" / "Repair21_Offline_Gates.json"


def run_json(script):
    completed = subprocess.run(
        [sys.executable, "-X", "utf8", "-B", str(script)],
        cwd=str(AUTOMATION_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        payload = {}
    return completed.returncode, payload


def main() -> int:
    audit = current_wire_audit()
    state_contract = audit["state_contract"]
    before = r26_hashes()
    raw = r26_arguments()
    r26_wire = r26_wire_payload()
    function = r26_wire["tools"][0]["function"]
    validator = validator_for(state_contract)
    state_schema = audit["function"]["parameters"]["properties"]["state_evidence"]["properties"]
    gate_code = 0 if GATE_REPORT.is_file() else 1
    gates = json.loads(GATE_REPORT.read_text(encoding="utf-8")) if GATE_REPORT.is_file() else {}
    object_code, object_regression = run_json(REPAIR_09K / "tests" / "run_director_state_object_phase2_regression.py")
    sw_positive_code, sw_positive = run_json(REPAIR_20 / "tests" / "run_scene_writer_completeness_positive_tests.py")
    sw_negative_code, sw_negative = run_json(REPAIR_20 / "tests" / "run_scene_writer_completeness_negative_tests.py")
    after = r26_hashes()
    results = []

    def add(case_id, passed, detail):
        results.append({"id": case_id, "result": "PASS" if passed else "FAIL", "detail": detail})

    type_domains = audit["type_manifest"]["field_domains"]
    expected_type_fields = {
        "flags", "handoffs", "unresolved_decisions", "state_evidence",
        "state_evidence.relevant_prior_state", "state_evidence.current_state",
        "state_evidence.proposed_state", "state_evidence.knowledge_timing",
        "state_evidence.relationship_state", "state_evidence.visual_state",
    }
    mechanics = r26_wire["tool_choice"]
    current_function = audit["function"]
    add("DIR-TYPE-01", audit["compiled"]["fixture"]["fixture_id"] == "E2E-FIX-03" and bool(state_contract["source_trace"]) and state_contract["legacy_string_path"] == "UNREACHABLE", "compiled contract provenance reaches the Director state contract")
    add("DIR-TYPE-02", set(audit["strict"].parameters_schema["required"]) == set(audit["neutral"]["required"]) and len(audit["strict"].parameters_schema["required"]) == 15, "final strict 15-field schema is resolved")
    add("DIR-TYPE-03", audit["projection_equivalence"]["required_fields_preserved"] and audit["projected"] == current_function["parameters"], "DeepSeek projection is resolved and lossless")
    add("DIR-TYPE-04", function["parameters"] == current_function["parameters"], "R26 actual final wire schema is captured and equals the current projection")
    add("DIR-TYPE-05", audit["neutral"]["properties"]["unresolved_decisions"]["anyOf"][1]["type"] == "array" and audit["strict"].parameters_schema == audit["neutral"], "local validator derives its native type domain from the same contract")
    add("DIR-TYPE-06", function["name"] == "submit_director_package" and function["strict"] is True, "actual R26 wire has exact strict function mechanics")
    add("DIR-TYPE-07", mechanics == {"type": "function", "function": {"name": "submit_director_package"}}, "actual R26 wire forces the exact Director function")
    add("DIR-TYPE-08", validator(native_array_payload())["unresolved_decisions"] == ["unresolved-decision"], "native text array passes without coercion")
    add("DIR-TYPE-09", validator(absent_payload())["unresolved_decisions"] == "ABSENT", "exact ABSENT passes without collapse")
    add("DIR-TYPE-10", isinstance(raw["unresolved_decisions"], str) and rejects(raw, state_contract), "stringified R26 array is rejected by the local validator")
    add("DIR-TYPE-11", rejects(r26_arguments(), state_contract) and isinstance(r26_diagnostic_inner_array(), list) and before == after, "immutable R26 replay remains a native-type failure even though diagnostic parsing can inspect its string")
    add("DIR-TYPE-12", set(type_domains) == expected_type_fields and "native JSON object" in type_domains["state_evidence.relevant_prior_state"] and "native JSON object" in type_domains["state_evidence.current_state"] and "native JSON array" in type_domains["unresolved_decisions"], "all Director container and ABSENT fields are schema-derived and audited")
    guards = production_source_guards()
    add("DIR-TYPE-13", all(guards.values()), "no field-level parser, legacy live serializer, adapter normalizer, or provider retry path is reachable")
    reminder = audit["type_instruction"]
    add("DIR-TYPE-14", "Use native JSON types exactly" in reminder and "Never serialize an array or object" in reminder and "E2E-FIX-03" not in reminder and "C-09" not in reminder and "battery" not in reminder, "native-type reminder is derived from the final schema and contains no fixture literal")
    add("DIR-TYPE-15", object_code == 0 and object_regression.get("passed") == 12 and object_regression.get("total") == 12, "Repair09K state-object authority regression passes")
    add("DIR-TYPE-16", sw_positive_code == 0 and sw_positive.get("passed") == 20 and sw_positive.get("total") == 20 and sw_negative_code == 0 and sw_negative.get("passed") == 15 and sw_negative.get("total") == 15, "Repair20 Scene Writer completeness regressions remain green")
    add("DIR-TYPE-17", gate_code == 0 and gates.get("mandatory_preflight", {}).get("passed") is True and gates.get("mandatory_preflight", {}).get("suite_count") == 15, "Mandatory Preflight remains 15/15")
    add("DIR-TYPE-18", gates.get("genericity", {}).get("returncode") == 0 and gates.get("genericity", {}).get("passed") == 18 and gates.get("genericity", {}).get("total") == 18, "GEN fixture generality remains 18/18")
    add("DIR-TYPE-19", gates.get("unified_phase2", {}).get("returncode") == 0 and gates.get("unified_phase2", {}).get("overall") == "PASS" and gates.get("unified_phase2", {}).get("record_count") == 25, "Unified Phase2 remains 25/25")
    integrity = current_integrity()
    add("DIR-TYPE-20", integrity["canonical_hashes_match_r26"] and integrity["production_lock_hashes_match_r26"] and integrity["canonical_count"] == 7 and integrity["production_lock_count"] == 6 and integrity["r26_status"] == "BLOCKED", "canonical skills and production locks remain intact while R26 remains blocked")

    output = {
        "classification": "DIRECTOR NATIVE JSON TYPE POSITIVE TEST",
        "results": results,
        "passed": sum(item["result"] == "PASS" for item in results),
        "total": len(results),
        "type_manifest": audit["type_manifest"],
        "r26_replay": {"raw_unresolved_type": type(raw["unresolved_decisions"]).__name__, "diagnostic_inner_type": type(r26_diagnostic_inner_array()).__name__, "immutable": before == after},
        "offline_gates": gates,
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "live_e2e_runs": 0,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] == output["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
