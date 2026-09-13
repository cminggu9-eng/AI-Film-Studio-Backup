"""Repair18 positive alignment, replay, and regression tests."""

from __future__ import annotations

import json

from repair18_support import *


def main() -> int:
    cases = []

    def add(case_id, passed, detail):
        cases.append({"id": case_id, "result": "PASS" if passed else "FAIL", "detail": detail})

    contracts = [compiled(number) for number in (1, 2, 3)]
    identity = [identity_pair(contract) for contract in contracts]
    transitions = [build_shared_transition_authority_projection(contract) for contract in contracts]
    replay = r22_replay()

    add("SAFE-ALIGN-01", all(item[0]["source_contract_pointer"] == "compiled_run_contract#/fixture/tracked_entities" for item in identity), "identity provenance is complete")
    add("SAFE-ALIGN-02", identity[1][1]["representation_namespace"] != identity[1][2]["representation_namespace"] and identity[1][1]["representation_token"] != identity[1][2]["representation_token"], "namespace distinction is explicit")
    add("SAFE-ALIGN-03", all(item[0]["projection_type"] == "CURRENT_RUN_ENTITY_IDENTITY_PROJECTION" and item[0]["derivation"] == "BINDING_RECORD_MEMBERSHIP_ONLY" for item in identity), "binding-derived identity projection is established")
    add("SAFE-ALIGN-04", resolved_identity_match(identity[0][1], identity[0][2]), "Fixture01 identity projection passes")
    add("SAFE-ALIGN-05", resolved_identity_match(identity[1][1], identity[1][2]), "Fixture02 identity projection passes")
    add("SAFE-ALIGN-06", resolved_identity_match(identity[2][1], identity[2][2]), "Fixture03 identity projection passes")
    add("SAFE-ALIGN-07", replay["integration_decision"] == "PASS" and not any(item.get("code") == "REQUIRED_PROP_MISMATCH" for item in replay["findings"]), "R22 legal prop identity no longer false-mismatches")
    two = synthetic_two_entity_contract(); ptwo = build_entity_identity_projection(two)
    foreign_left = resolve_entity_identity(ptwo, namespace="transport.entity_id", token=two["fixture"]["tracked_entities"][0]["entity_id"])
    foreign_right = resolve_entity_identity(ptwo, namespace="assertion.identity_lock", token=two["fixture"]["tracked_entities"][1]["identity_lock"])
    add("SAFE-ALIGN-08", not resolved_identity_match(foreign_left, foreign_right), "foreign prop identity remains rejected")
    add("SAFE-ALIGN-09", len(replay["prop_assertions"]) == 3 and all(resolved_identity_match(item["value"], item["expected"]) for item in replay["prop_assertions"]), "PROP-1/2/3 use resolved identity")
    required_transition_fields = {"transition_id", "state_dimension", "from_state", "to_state", "authorization_source", "allowed_scene_window", "evidence_requirements"}
    add("SAFE-ALIGN-10", all(required_transition_fields <= set(item["records"][0]) for item in transitions), "transition provenance is complete")
    authorized_only = classify_transition_evidence(transitions[1], scene_matrix(contracts[1], occurs=False))
    add("SAFE-ALIGN-11", authorized_only["machine_classification"]["AUTHORIZED"] and not authorized_only["machine_classification"]["OCCURRED"], "AUTHORIZED and OCCURRED remain separate")
    add("SAFE-ALIGN-12", replay["transition"]["projection_hash"] == transitions[1]["projection_hash"] and replay["transition"]["authority"] == transitions[1]["records"][0], "Safeguard consumes shared transition projection")
    add("SAFE-ALIGN-13", replay["transition"]["machine_classification"] == {"AUTHORIZED": True, "OCCURRED": True, "OBSERVED": True, "HANDED_OFF": False} and replay["transition"]["occurrence_evidence"][0]["scene_id"] == "E2E-FIX-02-S02", "R22 transition replay is classified exactly")
    add("SAFE-ALIGN-14", replay["transition"]["machine_classification"]["HANDED_OFF"] is False and replay["historical_status_preserved"], "State Ledger handoff remains evidence-driven and R22 historical status stays BLOCKED")
    add("SAFE-ALIGN-15", len({item["projection_hash"] for item in transitions}) == 3 and all(classify_transition_evidence(item, scene_matrix(contract))["machine_classification"]["OCCURRED"] for item, contract in zip(transitions, contracts)), "cross-fixture transition isolation passes")

    code16, result16 = run_json(REPAIR_16 / "tests" / "run_scene_writer_scene_id_positive_tests.py")
    add("SAFE-ALIGN-16", code16 == 0 and result16.get("passed") == 20 and result16.get("total") == 20, "Repair16 scene-ID regression passes")
    code17, result17 = run_json(REPAIR_17 / "tests" / "run_scene_writer_state_field_positive_tests.py")
    add("SAFE-ALIGN-17", code17 == 0 and result17.get("passed") == 20 and result17.get("total") == 20, "Repair17 state-field regression passes")
    code15, result15 = run_json(REPAIR_15 / "tests" / "run_environment_isolation_positive_tests.py")
    add("SAFE-ALIGN-18", code15 == 0 and result15.get("passed") == 18 and result15.get("total") == 18, "Repair15 environment regression passes")
    preflight = e2e.rerun_preflight()
    add("SAFE-ALIGN-19", preflight.get("passed") is True and len(preflight.get("required_suites", {})) == 15, "Mandatory Preflight passes")
    phase2_code, phase2 = run_json(PHASE2 / "run_systemic_regression_gate.py")
    add("SAFE-ALIGN-20", phase2_code == 0 and phase2.get("overall") == "PASS" and len(phase2.get("records", [])) == 25, "Unified Phase2 Gate passes")

    passed = sum(item["result"] == "PASS" for item in cases)
    output = {
        "classification": "REPAIR18 SEMANTIC SAFEGUARD POSITIVE TEST",
        "results": cases,
        "passed": passed,
        "total": 20,
        "r22_identity_result": "PASS" if replay["integration_decision"] == "PASS" else "FAIL",
        "r22_transition_classification": replay["transition"]["machine_classification"],
        "mandatory_preflight": {"passed": preflight.get("passed"), "suite_count": len(preflight.get("required_suites", {}))},
        "unified_phase2": {"overall": phase2.get("overall"), "total": len(phase2.get("records", []))},
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "live_e2e_runs": 0,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if passed == 20 else 1


if __name__ == "__main__":
    raise SystemExit(main())
