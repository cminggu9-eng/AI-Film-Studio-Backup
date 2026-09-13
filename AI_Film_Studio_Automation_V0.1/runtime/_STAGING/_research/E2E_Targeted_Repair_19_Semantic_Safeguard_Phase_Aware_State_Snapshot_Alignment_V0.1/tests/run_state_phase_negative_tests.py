"""Repair19 fail-closed, non-mutation, and genericity tests."""

from __future__ import annotations

import copy
import json

from repair19_support import *


def main() -> int:
    cases = []

    def add(case_id, fn, detail):
        try:
            passed = bool(fn())
            cases.append({"id": case_id, "result": "PASS" if passed else "FAIL", "detail": detail})
        except Exception as exc:
            cases.append({"id": case_id, "result": "FAIL", "detail": f"{type(exc).__name__}: {exc}"})

    replay = r24_phase_replay()
    initial = replay["required_assertion"]["expected"]
    entry_value = replay["required_assertion"]["value"]
    exit_snapshot = replay["exit"]
    entry_snapshot = replay["entry"]

    def misbound(required_phase, selected_snapshot):
        return {
            "snapshot_contract": "STATE_PHASE_SNAPSHOT_V0.1",
            "required_phase": required_phase,
            "selected_value": selected_snapshot["value"],
            "selected_snapshot": copy.deepcopy(selected_snapshot),
            "projection_hash": replay["projection"]["projection_hash"],
        }

    add("SAFE-PHASE-NEG-01", lambda: evaluate_required(misbound("ENTRY", exit_snapshot), initial)["integration_decision"] == "BLOCK", "initial-state assertion compared to EXIT fails closed")
    add("SAFE-PHASE-NEG-02", lambda: evaluate_required(misbound("EXIT", entry_snapshot), exit_snapshot["value"])["integration_decision"] == "BLOCK", "exit-state assertion compared to ENTRY fails closed")

    contract3 = compiled(3)
    no_occurrence_scenes = scenes_for(contract3, transition_scene=None)
    no_occurrence_projection = phase_projection(contract3, no_occurrence_scenes)
    dimension = contract3["fixture"]["state_dimensions"][0]["dimension"]
    add("SAFE-PHASE-NEG-03", lambda: resolve_state_phase_snapshot(no_occurrence_projection, scene_id=contract3["scene_ids"][0], state_dimension=dimension, phase="EXIT")["value"] == contract3["fixture"]["state_dimensions"][0]["allowed_tokens"][0], "AUTHORIZED-only transition does not mutate EXIT")
    planned = copy.deepcopy(no_occurrence_scenes)
    planned[-1]["state_evidence"]["authorized_transitions"] = [contract3["fixture"]["authorized_transitions"][0]]
    planned_projection = phase_projection(contract3, planned)
    add("SAFE-PHASE-NEG-04", lambda: all(resolve_state_phase_snapshot(planned_projection, scene_id=scene_id, state_dimension=dimension, phase="EXIT")["value"] == contract3["fixture"]["state_dimensions"][0]["allowed_tokens"][0] for scene_id in contract3["scene_ids"]), "future/planned transition does not mutate snapshots")
    add("SAFE-PHASE-NEG-05", lambda: entry_snapshot["value"] != exit_snapshot["value"] and replay["projection"]["state_dimensions"][0]["records"][1]["entry"]["value"] == exit_snapshot["value"], "latest ledger/exit value is not used for every phase")

    def missing_entry_rejected():
        broken = copy.deepcopy(replay["projection"])
        del broken["state_dimensions"][0]["records"][0]["entry"]
        try:
            resolve_state_phase_snapshot(broken, scene_id=contract3["scene_ids"][0], state_dimension=dimension, phase="ENTRY")
        except StatePhaseContractError:
            return True
        return False
    add("SAFE-PHASE-NEG-06", missing_entry_rejected, "missing ENTRY is not substituted with EXIT")
    add("SAFE-PHASE-NEG-07", lambda: entry_snapshot["value"] != exit_snapshot["value"] and replay["report"]["integration_decision"] == "PASS", "REQUIRED_STATE is not silently treated as persistent")
    production = [INTEGRATION / "implementation" / "integration_contract" / "state_phase.py", INTEGRATION / "implementation" / "integration_contract" / "semantic_safeguard.py", HARNESS / "run_minimal_e2e.py"]
    forbidden = ("battery_installed", "battery_removed_and_sealed", "signboard_on", "signboard_off", "A-17", "C-09")
    add("SAFE-PHASE-NEG-08", lambda: not any(token in path.read_text(encoding="utf-8") for path in production for token in forbidden), "generic phase code contains no fixture business literals")
    before = copy.deepcopy(r24_output())
    _ = r24_phase_replay()
    add("SAFE-PHASE-NEG-09", lambda: r24_output() == before and r24_raw_hash() == R24_RAW_BASELINE, "recorded scene transition is not auto-repaired")
    add("SAFE-PHASE-NEG-10", lambda: r24_tree_hash() == R24_TREE_BASELINE and r24_raw_hash() == R24_RAW_BASELINE, "R24 raw and complete evidence remain immutable")
    misbound_report = evaluate_required(misbound("ENTRY", exit_snapshot), initial)
    add("SAFE-PHASE-NEG-11", lambda: misbound_report["integration_decision"] == "BLOCK" and misbound_report["layer_a"]["findings"][0]["code"] == "REQUIRED_STATE_PHASE_SOURCE_FAILURE", "phase mismatch remains a Safeguard state-phase failure, not role semantic failure")
    carried_entry = replay["projection"]["state_dimensions"][0]["records"][1]["entry"]
    add("SAFE-PHASE-NEG-12", lambda: carried_entry["source_kind"] == "PREVIOUS_SCENE_EXIT" and carried_entry["evidence_pointer"] == exit_snapshot["evidence_pointer"], "previous EXIT is traceable before carry-forward")

    def conflict_rejected():
        conflicting = copy.deepcopy(no_occurrence_scenes)
        conflicting[0]["state_evidence"][dimension] = "outside_compiled_domain"
        try:
            phase_projection(contract3, conflicting)
        except StatePhaseContractError:
            return True
        return False
    add("SAFE-PHASE-NEG-13", conflict_rejected, "conflicting or unresolvable state source fails closed")
    classified = classify_transition_evidence(build_shared_transition_authority_projection(contract3), no_occurrence_scenes)
    add("SAFE-PHASE-NEG-14", lambda: classified["machine_classification"] == {"AUTHORIZED": True, "OCCURRED": False, "OBSERVED": False, "HANDED_OFF": False}, "occurrence remains separate from authorization")
    missing_trace = copy.deepcopy(entry_value)
    missing_trace["selected_snapshot"]["source_artifact"] = ""
    add("SAFE-PHASE-NEG-15", lambda: evaluate_required(missing_trace, initial)["integration_decision"] == "BLOCK", "snapshot without complete source trace is rejected")

    passed = sum(item["result"] == "PASS" for item in cases)
    output = {
        "classification": "REPAIR19 STATE PHASE NEGATIVE TEST",
        "results": cases,
        "passed": passed,
        "total": 15,
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "live_e2e_runs": 0,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if passed == 15 else 1


if __name__ == "__main__":
    raise SystemExit(main())
