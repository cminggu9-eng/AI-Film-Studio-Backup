"""Provider-free positive tests for one compiled Scene Writer scene-id projection."""
from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path

STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research"
REPAIR_01 = RESEARCH / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1"
REPAIR_02 = RESEARCH / "E2E_Targeted_Repair_02_Scene_Writer_Response_Budget_Serialization_V0.1"
REPAIR_03 = RESEARCH / "E2E_Targeted_Repair_03_Strict_Structured_Transport_V0.1"
REPAIR_07 = RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1"
REPAIR_08C = RESEARCH / "E2E_Targeted_Repair_08C_Scene_Writer_Strict_Schema_Composition_V0.1"
REPAIR_15 = RESEARCH / "E2E_Targeted_Repair_15_Mandatory_Preflight_Environment_Isolation_V0.1"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
PHASE2 = RESEARCH / "Systemic_Hardening_Phase_2_Runtime_Reliability_Regression_Enforcement_V0.1"
for item in (REPAIR_03 / "implementation", REPAIR_02 / "implementation", REPAIR_01 / "implementation", REPAIR_07 / "implementation", REPAIR_08C / "implementation", REPAIR_15 / "implementation", HARNESS, AUTOMATION_ROOT):
    sys.path.insert(0, str(item))

from fixture_contract_compiler import compile_path
from scene_writer_scene_id_contract import build_scene_id_contract
from scene_writer_state_field_contract import build_scene_writer_state_projection
from scene_writer_schema_composer import compose
from scene_writer_strict_transport import FUNCTION_NAME, build_structured_output_contract, validate_strict_scene_writer_arguments
import run_minimal_e2e as e2e


def binding(number: int) -> Path:
    return REPAIR_07 / "fixtures" / f"E2E_FIX_0{number}_Runtime_Binding_V0.1.json"


def sample(schema):
    if "enum" in schema: return copy.deepcopy(schema["enum"][0])
    if "anyOf" in schema: return sample(schema["anyOf"][0])
    if schema.get("type") == "string": return "evidence"
    if schema.get("type") == "array": return [sample(schema["items"])]
    if schema.get("type") == "object": return {key: sample(value) for key, value in schema["properties"].items()}
    raise ValueError(schema)


def payload(compiled, projection, schema):
    value = sample(schema); item_schema = schema["properties"]["scenes"]["items"]; value["scenes"] = []
    for scene_id in projection["ordered_scene_ids"]:
        item = sample(item_schema); item["id"] = scene_id; value["scenes"].append(item)
    return value


def main() -> int:
    compiled = [compile_path(binding(number)) for number in (1, 2, 3)]
    projections = [build_scene_id_contract(item) for item in compiled]
    state_projections = [build_scene_writer_state_projection(item) for item in compiled]
    schemas = [compose(item, scene_id_contract=projection, state_field_contract=state_projection) for item, projection, state_projection in zip(compiled, projections, state_projections)]
    f1, f2, f3 = projections
    prompt = e2e.build_system_prompt(e2e.role_spec("scene_writer"), "READ ONLY", structured_function_name=FUNCTION_NAME, structured_parameters_schema=schemas[1], scene_id_contract=f2, state_field_contract=state_projections[1])
    raw_path = HARNESS / "evidence" / "E2E-RUN-20" / "artifacts" / "scene_writer_provider_response.json"
    raw_hash_before = hashlib.sha256(raw_path.read_bytes()).hexdigest()
    raw = json.loads(raw_path.read_text(encoding="utf-8")); recorded = json.loads(json.loads(raw["raw_provider_response"])["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"])
    replay_rejected = False
    try: validate_strict_scene_writer_arguments(recorded, parameters_schema=schemas[1], scene_id_contract=f2)
    except Exception: replay_rejected = True
    generic_test = subprocess.run([sys.executable, "-X", "utf8", "-B", str(REPAIR_07 / "tests" / "run_fixture_generality_tests.py")], cwd=str(AUTOMATION_ROOT), capture_output=True, text=True, encoding="utf-8")
    generic_payload = json.loads(generic_test.stdout) if generic_test.stdout else {}
    preflight = e2e.rerun_preflight()
    current_hashes = {spec.key: e2e.canonical_skill(spec)[1] for spec in e2e.ROLE_SPECS}
    results = []
    def add(case_id, value, detail): results.append({"id": case_id, "result": "PASS" if value else "FAIL", "detail": detail})
    add("SW-ID-01", all(item["source_contract_pointer"] == "compiled_run_contract#/scene_ids" for item in projections), "scene-id authority provenance is complete")
    add("SW-ID-02", len({item["contract_hash"] for item in projections}) == 3, "one binding derives one deterministic current-run projection")
    add("SW-ID-03", schemas[0]["properties"]["scenes"]["items"]["properties"]["id"]["enum"] == f1["ordered_scene_ids"], "Fixture01 projection compiles")
    add("SW-ID-04", schemas[1]["properties"]["scenes"]["items"]["properties"]["id"]["enum"] == f2["ordered_scene_ids"], "Fixture02 projection compiles")
    add("SW-ID-05", schemas[2]["properties"]["scenes"]["items"]["properties"]["id"]["enum"] == f3["ordered_scene_ids"], "Fixture03 projection compiles")
    add("SW-ID-06", all(scene_id in prompt for scene_id in f2["ordered_scene_ids"]) and not any(scene_id in prompt for scene_id in f1["ordered_scene_ids"] + f3["ordered_scene_ids"]), "prompt has only current-run machine identities")
    add("SW-ID-07", build_structured_output_contract(schemas[1]).parameters_schema == schemas[1], "provider strict schema uses current-run domain")
    add("SW-ID-08", validate_strict_scene_writer_arguments(payload(compiled[1], f2, schemas[1]), parameters_schema=schemas[1], scene_id_contract=f2)["scenes"][0]["id"] == f2["ordered_scene_ids"][0], "validator enforces exact ordered current-run identity")
    forward = [build_scene_id_contract(compile_path(binding(number)))["ordered_scene_ids"] for number in (1,2,3)]
    reverse = [build_scene_id_contract(compile_path(binding(number)))["ordered_scene_ids"] for number in (3,2,1)]
    add("SW-ID-09", forward[1] == f2["ordered_scene_ids"] and len({tuple(item) for item in forward}) == 3, "F01 to F02 to F03 isolation passes")
    add("SW-ID-10", reverse[1] == f2["ordered_scene_ids"] and len({tuple(item) for item in reverse}) == 3, "F03 to F02 to F01 isolation passes")
    legal = payload(compiled[1], f2, schemas[1])
    add("SW-ID-11", validate_strict_scene_writer_arguments(legal, parameters_schema=schemas[1], scene_id_contract=f2)["scenes"][0]["id"] == f2["ordered_scene_ids"][0], "legal Fixture02 first ID is no longer a false negative")
    add("SW-ID-12", replay_rejected, "recorded foreign Fixture03 third ID remains fail-closed")
    add("SW-ID-13", replay_rejected and raw_hash_before == hashlib.sha256(raw_path.read_bytes()).hexdigest(), "R20 corrected replay is read-only and accurately non-conforming")
    add("SW-ID-14", not (HARNESS / "evidence" / "E2E-RUN-20" / "artifacts" / "scene_writer_final_wire_payload.json").exists(), "historical wire-schema provenance is resolved as unavailable, not inferred")
    env_iso = preflight.get("required_suites", {}).get("ENV-ISO-CORE", {})
    add("SW-ID-15", env_iso.get("result") == "PASS" and env_iso.get("passed") == 18 and env_iso.get("total") == 18, "Repair15 environment-isolation regression passes")
    add("SW-ID-16", preflight.get("passed") is True and len(preflight.get("required_suites", {})) == 15, "mandatory preflight passes 15 isolated suites")
    add("SW-ID-17", generic_test.returncode == 0 and generic_payload.get("passed") == 18, "cross-fixture genericity passes")
    add("SW-ID-18", env_iso.get("result") == "PASS", "Unified Phase2 gate remains verified through Repair15 environment-isolation regression")
    add("SW-ID-19", len(current_hashes) == 7 and all(value == e2e.EXPECTED_HASHES[key] for key, value in current_hashes.items()), "canonical integrity passes")
    add("SW-ID-20", FUNCTION_NAME == "submit_scene_writer_package" and build_structured_output_contract(schemas[1]).function_name == FUNCTION_NAME, "Scene Writer strict authorized path remains strict")
    output = {"classification": "SCENE WRITER PER-RUN SCENE-ID POSITIVE TEST", "results": results, "passed": sum(item["result"] == "PASS" for item in results), "total": len(results), "provider_calls": 0, "executor_calls": 0, "role_calls": 0, "recorded_replay": "READ_ONLY"}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] == output["total"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
