"""Read-only Probe03 regression; no Provider, Executor, or rerun."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
REPAIR_03 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_03_Strict_Structured_Transport_V0.1"
REPAIR_02 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_02_Scene_Writer_Response_Budget_Serialization_V0.1"
REPAIR_01 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1"
REPAIR_07 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1"
REPAIR_08C = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_08C_Scene_Writer_Strict_Schema_Composition_V0.1"
HARNESS_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
for import_path in (str(REPAIR_03 / "implementation"), str(REPAIR_02 / "implementation"), str(REPAIR_01 / "implementation"), str(REPAIR_07 / "implementation"), str(REPAIR_08C / "implementation"), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

from scene_writer_compact_serialization import normalize_compact_scene_writer_output
from scene_writer_integration_contract import assess_scene_writer_integration_contract
from scene_writer_strict_transport import FUNCTION_NAME, validate_required_tool_call_shape, validate_strict_scene_writer_arguments
from fixture_contract_compiler import compile_path
from scene_writer_scene_id_contract import build_scene_id_contract
from scene_writer_state_field_contract import build_scene_writer_state_projection, state_field_name
from scene_writer_schema_composer import compose as compose_scene_writer_schema


EVIDENCE = REPAIR_03 / "evidence" / "SW-CONTRACT-PROBE-03"
RAW_PATH = EVIDENCE / "artifacts" / "scene_writer_provider_response.json"
OUTPUT_PATH = EVIDENCE / "artifacts" / "scene_writer_output.json"
SHOWRUNNER_PATH = HARNESS_STAGE / "evidence" / "E2E-RUN-01-RECOVERY-01" / "artifacts" / "showrunner_output.json"
FIXTURE_BINDING = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1" / "fixtures" / "E2E_FIX_01_Runtime_Binding_V0.1.json"


def run() -> int:
    raw = json.loads(RAW_PATH.read_text(encoding="utf-8"))
    wire = json.loads(raw["raw_provider_response"])
    message = wire["choices"][0]["message"]
    function = validate_required_tool_call_shape(
        assistant_content=message.get("content") or "",
        tool_calls=message.get("tool_calls"),
        function_name=FUNCTION_NAME,
    )
    arguments = json.loads(function["arguments"])
    fixture_contract = compile_path(FIXTURE_BINDING)
    scene_id_contract = build_scene_id_contract(fixture_contract)
    state_field_contract = build_scene_writer_state_projection(fixture_contract)
    state_field = state_field_name(state_field_contract)
    projected_arguments = copy.deepcopy(arguments)
    for scene in projected_arguments["scenes"]:
        legacy = scene["state"]
        scene["state"] = {
            "entity_id": legacy["key"],
            "custody": legacy["custody"],
            "holders": legacy["holders"],
            "reveal": legacy["reveal"],
            "relationship": legacy["relationship"],
            state_field: legacy["clothing_code"],
            "state_display": legacy["clothing_display"],
            "location": legacy["location"],
            "transitions": legacy["transitions"],
        }
    schema = compose_scene_writer_schema(fixture_contract, scene_id_contract=scene_id_contract, state_field_contract=state_field_contract)
    strict = validate_strict_scene_writer_arguments(projected_arguments, parameters_schema=schema, scene_id_contract=scene_id_contract, state_field_contract=state_field_contract)
    showrunner = json.loads(SHOWRUNNER_PATH.read_text(encoding="utf-8"))
    hydrated = normalize_compact_scene_writer_output(
        strict,
        run_id="SW-CONTRACT-PROBE-03",
        required_locks=showrunner["canon_assignment_locks"],
        prohibited_changes=showrunner["prohibited_changes"],
        scene_id_contract=scene_id_contract,
        state_field_contract=state_field_contract,
    )
    contract = assess_scene_writer_integration_contract(hydrated, run_id="SW-CONTRACT-PROBE-03", fixture_contract=fixture_contract)
    persisted_output = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    projected_persisted_output = copy.deepcopy(persisted_output)
    for scene in projected_persisted_output["scene_packages"]:
        state = scene["state_evidence"]
        state["entity_identity"] = state.pop("key_identity")
        state["entity_custody"] = state.pop("key_custody")
        state["machine_state_display"] = state.pop("clothing_visual_state_display")
    results = [
        {"id": "REC-03-01", "result": "PASS" if raw.get("raw_content_sha256") == hashlib.sha256(raw["raw_content"].encode("utf-8")).hexdigest() else "FAIL", "detail": "recorded raw wire evidence remains unchanged"},
        {"id": "REC-03-02", "result": "PASS" if not (message.get("content") or "") and function.get("name") == FUNCTION_NAME else "FAIL", "detail": "recorded formal result remains one named function call without assistant prose"},
        {"id": "REC-03-03", "result": "PASS" if strict["control"]["outcome"] == "SCENE_CREATED" and strict["control"]["outcome"] != "NEEDS_DECISION" else "FAIL", "detail": "recorded primary state remains canonical"},
        {"id": "REC-03-04", "result": "PASS" if strict["control"]["flags"] == "ABSENT" and strict["control"]["handoffs"] == "ABSENT" else "FAIL", "detail": "recorded transport absence remains exact"},
        {"id": "REC-03-05", "result": "PASS" if contract["passed"] and hydrated == projected_persisted_output and arguments != projected_arguments else "FAIL", "detail": "read-only historical transport-shape projection preserves values and passes the current generic bridge"},
    ]
    output = {"classification": "READ-ONLY PROBE03 RECORDED-RESPONSE REGRESSION", "results": results, "passed": sum(item["result"] == "PASS" for item in results), "total": len(results), "provider_calls": 0, "executor_calls": 0, "probe_reruns": 0, "json_auto_repairs": 0}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] == output["total"] else 1


if __name__ == "__main__":
    raise SystemExit(run())
