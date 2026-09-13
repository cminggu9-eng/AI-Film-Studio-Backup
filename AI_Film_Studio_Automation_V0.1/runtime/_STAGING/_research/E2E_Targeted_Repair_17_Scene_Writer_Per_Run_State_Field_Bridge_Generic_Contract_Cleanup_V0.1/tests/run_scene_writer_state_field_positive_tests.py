"""Provider-free SW-STATE-01 through SW-STATE-20 for Repair17."""

from __future__ import annotations

import copy
import json
import subprocess
import sys

from repair17_support import (
    AUTOMATION_ROOT,
    PHASE2,
    REPAIR_07,
    compile_matrix,
    generic_source_leaks,
    project_recorded_transport_shape,
    r21_arguments,
    replay_r21,
)

from scene_writer_scene_id_contract import assess_scene_id_sequence, build_scene_id_contract
from scene_writer_state_field_contract import build_scene_writer_state_projection, state_field_name
from scene_writer_strict_transport import FUNCTION_DESCRIPTION, FUNCTION_NAME, validate_strict_scene_writer_arguments
import run_minimal_e2e as e2e


def run_json(script):
    completed = subprocess.run([sys.executable, "-X", "utf8", "-B", str(script)], cwd=str(AUTOMATION_ROOT), capture_output=True, text=True, encoding="utf-8")
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        payload = {}
    return completed.returncode, payload


def main() -> int:
    compiled, scene_contracts, state_contracts, schemas = compile_matrix()
    fields = [state_field_name(item) for item in state_contracts]
    replay = replay_r21()
    f2_prompt = e2e.build_system_prompt(
        e2e.role_spec("scene_writer"),
        "READ ONLY",
        structured_function_name=FUNCTION_NAME,
        structured_parameters_schema=schemas[1],
        scene_id_contract=scene_contracts[1],
        state_field_contract=state_contracts[1],
    )
    projected_r21 = project_recorded_transport_shape(r21_arguments(), state_contracts[1])
    wrong_field = copy.deepcopy(projected_r21)
    wrong_field_name = fields[0]
    for scene in wrong_field["scenes"]:
        scene["state"][wrong_field_name] = scene["state"].pop(fields[1])
    wrong_field_rejected = False
    try:
        validate_strict_scene_writer_arguments(
            wrong_field,
            parameters_schema=schemas[1],
            scene_id_contract=scene_contracts[1],
            state_field_contract=state_contracts[1],
        )
    except Exception:
        wrong_field_rejected = True

    forward = [build_scene_writer_state_projection(item) for item in compiled]
    reverse_compiled = list(reversed(compiled))
    reverse = [build_scene_writer_state_projection(item) for item in reverse_compiled]
    foreign_ids = scene_contracts[0]["ordered_scene_ids"]
    current_ids = scene_contracts[1]["ordered_scene_ids"]
    scene_id_regression = (
        assess_scene_id_sequence(current_ids, scene_contracts[1])["result"] == "PASS"
        and assess_scene_id_sequence(foreign_ids, scene_contracts[1])["result"] != "PASS"
    )

    generic_code, generic = run_json(REPAIR_07 / "tests" / "run_fixture_generality_tests.py")
    preflight = e2e.rerun_preflight()
    phase2_code, phase2 = run_json(PHASE2 / "run_systemic_regression_gate.py")
    env_iso = preflight.get("required_suites", {}).get("ENV-ISO-CORE", {})
    leaks = generic_source_leaks()

    results = []
    def add(case_id, passed, detail):
        results.append({"id": case_id, "result": "PASS" if passed else "FAIL", "detail": detail})

    required_projection_fields = {
        "state_dimension_id", "transport_field_name", "allowed_machine_tokens", "initial_token",
        "authorized_transitions", "state_dimension_source_pointer", "binding_id", "contract_hash",
    }
    add("SW-STATE-01", all(required_projection_fields <= set(item) and item["source_owner"] == "compiled_run_contract" for item in state_contracts), "state-field authority provenance is complete")
    add("SW-STATE-02", all(item == build_scene_writer_state_projection(source) for item, source in zip(state_contracts, compiled)) and len({item["contract_hash"] for item in state_contracts}) == 3, "single deterministic current-run state projection established")
    for index, case_id in enumerate(("SW-STATE-03", "SW-STATE-04", "SW-STATE-05")):
        dimension = compiled[index]["fixture"]["state_dimensions"][0]
        add(case_id, fields[index] == dimension["dimension"] and state_contracts[index]["allowed_machine_tokens"] == dimension["allowed_tokens"] and state_contracts[index]["authorized_transitions"] == compiled[index]["fixture"]["authorized_transitions"], f"Fixture0{index + 1} state projection compiles from its binding")
    add("SW-STATE-06", replay["result"] == "PASS" and all(fields[1] in scene["state_evidence"] for scene in replay_r21_hydrated(projected_r21, compiled[1], scene_contracts[1], state_contracts[1])), "hydrator resolves and writes the current-run field")
    schema_state = schemas[1]["properties"]["scenes"]["items"]["properties"]["state"]
    add("SW-STATE-07", fields[1] in schema_state["properties"] and fields[0] not in schema_state["properties"] and fields[2] not in schema_state["properties"], "serializer/provider schema consumes only the current-run projection")
    add("SW-STATE-08", schema_state["properties"][fields[1]]["enum"] == state_contracts[1]["allowed_machine_tokens"], "validator consumes the same field and token domain")
    add("SW-STATE-09", fields[1] in f2_prompt and state_contracts[1]["contract_hash"] in f2_prompt, "prompt state contract is aligned to the projection")
    add("SW-STATE-10", replay["raw_machine_tokens"] == replay["hydrated_machine_tokens"] and set(replay["raw_machine_tokens"]) <= set(state_contracts[1]["allowed_machine_tokens"]), "legal Fixture02 machine states are accepted from compiled authority")
    add("SW-STATE-11", wrong_field_rejected, "legal tokens in the wrong state field are rejected")
    add("SW-STATE-12", [item["contract_hash"] for item in forward] == [item["contract_hash"] for item in reversed(reverse)] and len(set(fields)) == 3, "F01-F02-F03 and reverse-order state isolation pass")
    add("SW-STATE-13", replay["result"] == "PASS" and replay["historical_status_preserved"] and replay["raw_response_sha256_before"] == replay["raw_response_sha256_after"], "R21 corrected hydration replay is evaluated read-only")
    add("SW-STATE-14", "A-17" not in f2_prompt, "Fixture01 business literal is absent from the current generic prompt path")
    add("SW-STATE-15", "E2E-FIX-01" not in FUNCTION_DESCRIPTION and "probe" not in FUNCTION_DESCRIPTION.lower(), "function description is generic production wording")
    add("SW-STATE-16", not leaks and generic_code == 0 and generic.get("passed") == 18 and generic.get("total") == 18, "generic production literal scan is zero and GEN-01 through GEN-18 pass")
    add("SW-STATE-17", scene_id_regression, "Repair16 exact current-run scene-ID contract remains fail-closed for foreign IDs")
    add("SW-STATE-18", env_iso.get("result") == "PASS" and env_iso.get("passed") == 18 and env_iso.get("total") == 18, "Repair15 environment-isolation regression passes 18/18")
    add("SW-STATE-19", preflight.get("passed") is True and len(preflight.get("required_suites", {})) == 15, "Mandatory Preflight passes all 15 isolated suites")
    add("SW-STATE-20", phase2_code == 0 and phase2.get("overall") == "PASS" and len(phase2.get("records", [])) == 25, "Unified Phase2 gate passes 25/25")

    output = {
        "classification": "SCENE WRITER PER-RUN STATE-FIELD POSITIVE TEST",
        "results": results,
        "passed": sum(item["result"] == "PASS" for item in results),
        "total": len(results),
        "state_fields": fields,
        "projection_hashes": [item["contract_hash"] for item in state_contracts],
        "recorded_replay": replay,
        "genericity": {"passed": generic.get("passed"), "total": generic.get("total"), "returncode": generic_code},
        "mandatory_preflight": {"passed": preflight.get("passed"), "suite_count": len(preflight.get("required_suites", {}))},
        "unified_phase2": {"overall": phase2.get("overall"), "passed": sum(item.get("result") == "PASS" for item in phase2.get("records", [])), "total": len(phase2.get("records", []))},
        "generic_literal_leaks": leaks,
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "live_e2e_runs": 0,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] == output["total"] else 1


def replay_r21_hydrated(projected, fixture, scene_contract, state_contract):
    from repair17_support import R21_SHOWRUNNER
    from scene_writer_compact_serialization import normalize_compact_scene_writer_output

    showrunner = json.loads(R21_SHOWRUNNER.read_text(encoding="utf-8"))
    return normalize_compact_scene_writer_output(
        projected,
        run_id="E2E-RUN-21-RECORDED-REPLAY-REPAIR17",
        required_locks=showrunner["canon_assignment_locks"],
        prohibited_changes=showrunner["prohibited_changes"],
        scene_id_contract=scene_contract,
        state_field_contract=state_contract,
    )["scene_packages"]


if __name__ == "__main__":
    raise SystemExit(main())
