"""Repair19 positive phase-aware snapshot and regression tests."""

from __future__ import annotations

import json

from repair19_support import *


def main() -> int:
    cases = []

    def add(case_id, passed, detail):
        cases.append({"id": case_id, "result": "PASS" if passed else "FAIL", "detail": detail})

    fixture_projections = []
    for number, transition_scene in ((1, 2), (2, 2), (3, 1)):
        contract = compiled(number)
        fixture_projections.append((contract, phase_projection(contract, scenes_for(contract, transition_scene=transition_scene))))
    replay = r24_phase_replay()
    required = replay["required_assertion"]["value"]
    required_snapshot = required["selected_snapshot"]

    add("SAFE-PHASE-01", required_snapshot["source_binding_id"] == "E2E-FIX-03" and required_snapshot["source_kind"] == "COMPILED_INITIAL_STATE", "REQUIRED-STATE provenance is complete")
    add("SAFE-PHASE-02", required_snapshot["phase"] == "ENTRY" and required_snapshot["value"] == replay["required_assertion"]["expected"], "entry snapshot contract resolves from compiled initial state")
    add("SAFE-PHASE-03", replay["exit"]["phase"] == "EXIT" and replay["exit"]["value"] != replay["entry"]["value"], "exit snapshot contract resolves independently")
    add("SAFE-PHASE-04", required["required_phase"] == "ENTRY" and required["selected_value"] == required_snapshot["value"], "REQUIRED-STATE phase binding is explicit")
    add("SAFE-PHASE-05", fixture_projections[0][1]["projection_type"] == "STATE_PHASE_SNAPSHOT_PROJECTION", "Fixture01 phase projection passes")
    add("SAFE-PHASE-06", fixture_projections[1][1]["projection_type"] == "STATE_PHASE_SNAPSHOT_PROJECTION", "Fixture02 phase projection passes")
    add("SAFE-PHASE-07", fixture_projections[2][1]["projection_type"] == "STATE_PHASE_SNAPSHOT_PROJECTION", "Fixture03 phase projection passes")
    add("SAFE-PHASE-08", replay["entry"]["value"] == compiled(3)["fixture"]["state_dimensions"][0]["allowed_tokens"][0], "R24 S01 entry state is correct")
    add("SAFE-PHASE-09", replay["transition"]["machine_classification"] == {"AUTHORIZED": True, "OCCURRED": True, "OBSERVED": True, "HANDED_OFF": False}, "R24 S01 transition occurrence remains separate and valid")
    add("SAFE-PHASE-10", replay["exit"]["value"] == compiled(3)["fixture"]["state_dimensions"][0]["allowed_tokens"][1], "R24 S01 exit state is correct")
    add("SAFE-PHASE-11", replay["report"]["integration_decision"] == "PASS" and not any(item["code"] == "REQUIRED_STATE_MISMATCH" for item in replay["report"]["layer_a"]["findings"]), "R24 false REQUIRED_STATE_MISMATCH is removed without changing recorded output")
    trace_fields = set(("scene_id", "state_dimension", "phase", "value", "source_artifact", "source_version", "canonical_owner", "evidence_pointer", "source_kind", "source_binding_id"))
    all_snapshots = [snapshot for dimension in replay["projection"]["state_dimensions"] for record in dimension["records"] for snapshot in (record["entry"], record["exit"])]
    add("SAFE-PHASE-12", all(set(snapshot) == trace_fields and all(snapshot[field] not in (None, "") for field in trace_fields if field != "value") for snapshot in all_snapshots), "every projected snapshot has complete source trace")
    add("SAFE-PHASE-13", replay["projection"]["ledger_semantics"] == "SCENE_LEDGER_STATE_SNAPSHOT_IS_EXIT_POST_STATE" and replay["ledger"].entries()[0].state_snapshot[compiled(3)["fixture"]["state_dimensions"][0]["dimension"]] == replay["exit"]["value"], "State Ledger retains EXIT/POST semantics")

    code18, repair18 = run_json(REPAIR_18 / "tests" / "run_semantic_safeguard_negative_tests.py")
    add("SAFE-PHASE-14", code18 == 0 and repair18.get("passed") == 15 and repair18.get("total") == 15, "Repair18 transition separation regression passes")
    code17, repair17 = run_json(REPAIR_17 / "tests" / "run_scene_writer_state_field_positive_tests.py")
    add("SAFE-PHASE-15", code17 == 0 and repair17.get("passed") == 20 and repair17.get("total") == 20, "Repair17 state-field regression passes")
    code16, repair16 = run_json(REPAIR_16 / "tests" / "run_scene_writer_scene_id_positive_tests.py")
    add("SAFE-PHASE-16", code16 == 0 and repair16.get("passed") == 20 and repair16.get("total") == 20, "Repair16 scene-ID regression passes")
    code15, repair15 = run_json(REPAIR_15 / "tests" / "run_environment_isolation_positive_tests.py")
    add("SAFE-PHASE-17", code15 == 0 and repair15.get("passed") == 18 and repair15.get("total") == 18, "Repair15 environment regression passes")
    preflight = e2e.rerun_preflight()
    add("SAFE-PHASE-18", preflight.get("passed") is True and len(preflight.get("required_suites", {})) == 15, "Mandatory Preflight passes")
    code_gen, gen = run_json(REPAIR_07 / "tests" / "run_fixture_generality_tests.py")
    add("SAFE-PHASE-19", code_gen == 0 and gen.get("passed") == 18 and gen.get("total") == 18, "GEN passes")
    code_phase2, phase2 = run_json(PHASE2 / "run_systemic_regression_gate.py")
    add("SAFE-PHASE-20", code_phase2 == 0 and phase2.get("overall") == "PASS" and len(phase2.get("records", [])) == 25, "Unified Phase2 Gate passes")

    passed = sum(item["result"] == "PASS" for item in cases)
    output = {
        "classification": "REPAIR19 STATE PHASE POSITIVE TEST",
        "results": cases,
        "passed": passed,
        "total": 20,
        "r24_replay_decision": replay["report"]["integration_decision"],
        "r24_required_state_phase": required["required_phase"],
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
