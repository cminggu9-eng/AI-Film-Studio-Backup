from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from director_state_object_test_support import (
    HARNESS,
    RESEARCH,
    check,
    compile_fixture,
    read_recorded_arguments,
    rejected,
    result_payload,
    valid_payload,
)
from director_state_object_contract import TRACE_FIELDS, lint_deepseek_strict_schema
from director_provider_compatibility import deepseek_compatible_schema
from director_structured_submission import (
    assert_director_contract_identity,
    build_director_structured_prompt_instruction,
    director_prompt_contract_manifest,
    director_structured_contract_manifest,
    director_submission_schema,
    director_validator_contract_manifest,
    make_director_payload_validator,
)
import run_minimal_e2e as e2e


PHASE2_GATE = RESEARCH / "Systemic_Hardening_Phase_2_Runtime_Reliability_Regression_Enforcement_V0.1" / "run_systemic_regression_gate.py"
STRICT_LIFE = RESEARCH / "E2E_Targeted_Repair_11_Strict_Transport_Lifecycle_Authorization_V0.1" / "tests" / "run_strict_transport_lifecycle_tests.py"
SCENE_STRICT = RESEARCH / "E2E_Targeted_Repair_03_Strict_Structured_Transport_V0.1" / "tests" / "run_scene_writer_strict_transport_tests.py"
CAPTURES = RESEARCH / "E2E_Targeted_Repair_09K_Director_State_Object_Contract_Implementation_V0.1" / "tests" / "run_director_request_captures.py"
R14 = HARNESS / "evidence" / "E2E-RUN-14" / "artifacts" / "director_provider_response.json"


def run_json(script):
    completed = subprocess.run([sys.executable, "-X", "utf8", "-B", str(script)], cwd=str(e2e.AUTOMATION_ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        payload = {}
    return completed, payload


def main() -> int:
    compiled, contract, _ = compile_fixture()
    schema = director_submission_schema(contract)
    strict = deepseek_compatible_schema(contract)
    state = schema["properties"]["state_evidence"]["properties"]
    strict_state = strict["properties"]["state_evidence"]["properties"]
    results: list[dict[str, object]] = []

    check(results, "DIR-OBJ-01", len(contract["authority"]["contract_hashes"]) == 8 and all(contract["authority"]["contract_hashes"].values()), "09J frozen authority contracts loaded and hashed")
    _, second_contract, _ = compile_fixture()
    check(results, "DIR-OBJ-02", contract == second_contract and contract["bundle_hash"] == second_contract["bundle_hash"], "compiler output deterministic")
    check(results, "DIR-OBJ-03", state["relevant_prior_state"]["type"] == "object" and state["relevant_prior_state"]["required"] == compiled["scene_ids"], "prior dynamic scene schema")
    check(results, "DIR-OBJ-04", state["current_state"]["type"] == "object" and state["current_state"]["required"] == compiled["scene_ids"], "current dynamic scene schema")
    check(results, "DIR-OBJ-05", state["proposed_state"] == {"const": "ABSENT"} and strict_state["proposed_state"] == {"type": "string", "enum": ["ABSENT"]}, "proposed exact ABSENT")
    check(results, "DIR-OBJ-06", state["knowledge_timing"] == {"const": "ABSENT"} and strict_state["knowledge_timing"] == {"type": "string", "enum": ["ABSENT"]}, "knowledge exact ABSENT")
    check(results, "DIR-OBJ-07", state["visual_state"] == {"const": "ABSENT"} and strict_state["visual_state"] == {"type": "string", "enum": ["ABSENT"]}, "visual exact ABSENT")
    check(results, "DIR-OBJ-08", all(set(item) == TRACE_FIELDS for item in contract["source_trace"]) and bool(contract["source_trace_hash"]), "source trace complete")

    function_manifest = director_structured_contract_manifest(strict, contract)
    prompt_manifest = director_prompt_contract_manifest(strict, contract)
    validator_manifest = director_validator_contract_manifest(contract)
    identity = assert_director_contract_identity(prompt_manifest, function_manifest, validator_manifest)
    prompt = build_director_structured_prompt_instruction(strict)
    check(results, "DIR-OBJ-09", identity["result"] == "PASS" and "exactly these 15 required fields" in prompt and "JSON-encode" in prompt, "Prompt/Function/Validator identity")
    check(results, "DIR-OBJ-10", lint_deepseek_strict_schema(strict)["result"] == "PASS", "DeepSeek strict schema lint")

    validator = make_director_payload_validator(selected_mode="PLAN", required_locks=["lock"], prohibited_changes=["prohibition"], state_contract=contract)
    downstream = validator(valid_payload(contract))
    envelope = e2e.make_envelope(e2e.role_spec("director"), downstream, "Character & Acting", "Direction constraints", Path(__file__))
    check(results, "DIR-OBJ-11", isinstance(downstream["state_evidence"]["relevant_prior_state"], dict) and isinstance(downstream["state_evidence"]["current_state"], dict) and isinstance(envelope["relevant_prior_state"], dict) and isinstance(envelope["current_state"], dict), "downstream Envelope object carriage")
    legacy = valid_payload(contract)
    legacy["state_evidence"]["current_state"] = json.dumps(legacy["state_evidence"]["current_state"], ensure_ascii=False)
    check(results, "DIR-OBJ-12", contract["legacy_string_path"] == "UNREACHABLE" and rejected(lambda: validator(legacy)) and "JSON-encoded state object" not in prompt, "legacy string live path unreachable")

    capture_completed, captures = run_json(CAPTURES)
    by_fixture = {item["fixture_id"]: item for item in captures.get("captures", [])}
    fixture_contracts = {}
    for test_id, fixture_id in (("DIR-OBJ-13", "E2E-FIX-01"), ("DIR-OBJ-14", "E2E-FIX-02"), ("DIR-OBJ-15", "E2E-FIX-03")):
        fixture_compiled, fixture_contract, _ = compile_fixture(fixture_id)
        fixture_contracts[fixture_id] = (fixture_compiled, fixture_contract)
        capture = by_fixture.get(fixture_id, {})
        exact = set(fixture_contract["state_schemas"]["current_state"]["properties"]) == set(fixture_compiled["scene_ids"])
        check(results, test_id, capture_completed.returncode == 0 and capture.get("result") == "PASS" and exact, f"{fixture_id} compile and final request capture")
    dimensions = [tuple(item[1]["state_dimensions"]) for item in fixture_contracts.values()]
    schema_hashes = [item[1]["state_schema_hash"] for item in fixture_contracts.values()]
    check(results, "DIR-OBJ-16", len(set(dimensions)) == 3 and len(set(schema_hashes)) == 3, "cross-fixture dimensions and schemas remain isolated")

    r14_arguments = read_recorded_arguments(R14)
    r14_rejected = rejected(lambda: validator(r14_arguments))
    exact_absent_violation = any(r14_arguments["state_evidence"][field] != "ABSENT" for field in ("proposed_state", "knowledge_timing", "visual_state"))
    check(results, "DIR-OBJ-17", r14_rejected and exact_absent_violation, "R14 immutable payload classified NON-CONFORMING under new contract")

    strict_completed, strict_payload = run_json(STRICT_LIFE)
    check(results, "DIR-OBJ-18", strict_completed.returncode == 0 and strict_payload.get("passed") == 30 and strict_payload.get("total") == 30, "Repair11 exact role/function lifecycle registry unchanged")
    scene_completed, scene_payload = run_json(SCENE_STRICT)
    check(results, "DIR-OBJ-19", scene_completed.returncode == 0 and scene_payload.get("passed") == 15 and scene_payload.get("total") == 15, "Scene Writer strict regression")
    phase_completed, phase_payload = run_json(PHASE2_GATE)
    check(results, "DIR-OBJ-20", phase_completed.returncode == 0 and phase_payload.get("overall") == "PASS" and phase_payload.get("provider_calls") == 0, "Unified Phase2 Gate PASS")

    output = result_payload(results, classification="DIRECTOR STATE OBJECT CONTRACT TESTS")
    output["capture_summary"] = captures
    output["phase2_overall"] = phase_payload.get("overall")
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["result"] == "PASS" and output["total"] == 20 else 1


if __name__ == "__main__":
    raise SystemExit(main())
