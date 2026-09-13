"""Shared provider-free helpers for Repair17 state-field regression suites."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Dict, Mapping


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research"
REPAIR_01 = RESEARCH / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1"
REPAIR_02 = RESEARCH / "E2E_Targeted_Repair_02_Scene_Writer_Response_Budget_Serialization_V0.1"
REPAIR_03 = RESEARCH / "E2E_Targeted_Repair_03_Strict_Structured_Transport_V0.1"
REPAIR_07 = RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1"
REPAIR_08C = RESEARCH / "E2E_Targeted_Repair_08C_Scene_Writer_Strict_Schema_Composition_V0.1"
REPAIR_15 = RESEARCH / "E2E_Targeted_Repair_15_Mandatory_Preflight_Environment_Isolation_V0.1"
REPAIR_16 = RESEARCH / "E2E_Targeted_Repair_16_Scene_Writer_Per_Run_Strict_Scene_ID_Contract_Alignment_V0.1"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
PHASE2 = RESEARCH / "Systemic_Hardening_Phase_2_Runtime_Reliability_Regression_Enforcement_V0.1"
for item in (
    REPAIR_03 / "implementation",
    REPAIR_02 / "implementation",
    REPAIR_01 / "implementation",
    REPAIR_07 / "implementation",
    REPAIR_08C / "implementation",
    REPAIR_15 / "implementation",
    HARNESS,
    AUTOMATION_ROOT,
):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from fixture_contract_compiler import compile_path
from scene_writer_compact_serialization import normalize_compact_scene_writer_output
from scene_writer_integration_contract import assess_scene_writer_integration_contract
from scene_writer_scene_id_contract import build_scene_id_contract
from scene_writer_schema_composer import compose
from scene_writer_state_field_contract import build_scene_writer_state_projection, state_field_name
from scene_writer_strict_transport import validate_strict_scene_writer_arguments


R21_RAW = HARNESS / "evidence" / "E2E-RUN-21" / "artifacts" / "scene_writer_provider_response.json"
R21_SHOWRUNNER = HARNESS / "evidence" / "E2E-RUN-21" / "artifacts" / "showrunner_output.json"
GENERIC_SOURCES = (
    REPAIR_01 / "implementation" / "scene_writer_state_field_contract.py",
    REPAIR_01 / "implementation" / "scene_writer_integration_contract.py",
    REPAIR_02 / "implementation" / "scene_writer_compact_serialization.py",
    REPAIR_03 / "implementation" / "scene_writer_strict_transport.py",
    REPAIR_08C / "implementation" / "scene_writer_schema_composer.py",
)


def binding(number: int) -> Path:
    return REPAIR_07 / "fixtures" / f"E2E_FIX_0{number}_Runtime_Binding_V0.1.json"


def compile_matrix() -> tuple[list[Dict[str, Any]], list[Dict[str, Any]], list[Dict[str, Any]], list[Dict[str, Any]]]:
    compiled = [compile_path(binding(number)) for number in (1, 2, 3)]
    scene_ids = [build_scene_id_contract(item) for item in compiled]
    states = [build_scene_writer_state_projection(item) for item in compiled]
    schemas = [compose(item, scene_id_contract=ids, state_field_contract=state) for item, ids, state in zip(compiled, scene_ids, states)]
    return compiled, scene_ids, states, schemas


def r21_arguments() -> Dict[str, Any]:
    raw = json.loads(R21_RAW.read_text(encoding="utf-8"))
    wire = json.loads(raw["raw_provider_response"])
    return json.loads(wire["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"])


def project_recorded_transport_shape(arguments: Mapping[str, Any], state_contract: Mapping[str, Any]) -> Dict[str, Any]:
    """Project obsolete aliases in a copy; state values and historical evidence remain immutable."""

    projected = copy.deepcopy(dict(arguments))
    field = state_field_name(state_contract)
    for scene in projected["scenes"]:
        legacy = scene["state"]
        scene["state"] = {
            "entity_id": legacy["key"],
            "custody": legacy["custody"],
            "holders": legacy["holders"],
            "reveal": legacy["reveal"],
            "relationship": legacy["relationship"],
            field: legacy["clothing_code"],
            "state_display": legacy["clothing_display"],
            "location": legacy["location"],
            "transitions": legacy["transitions"],
        }
    return projected


def replay_r21() -> Dict[str, Any]:
    compiled, scene_contracts, state_contracts, schemas = compile_matrix()
    fixture = compiled[1]
    scene_contract = scene_contracts[1]
    state_contract = state_contracts[1]
    schema = schemas[1]
    raw_hash_before = hashlib.sha256(R21_RAW.read_bytes()).hexdigest()
    original = r21_arguments()
    raw_tokens = [scene["state"]["clothing_code"] for scene in original["scenes"]]
    projected = project_recorded_transport_shape(original, state_contract)
    strict = validate_strict_scene_writer_arguments(
        projected,
        parameters_schema=schema,
        scene_id_contract=scene_contract,
        state_field_contract=state_contract,
    )
    showrunner = json.loads(R21_SHOWRUNNER.read_text(encoding="utf-8"))
    hydrated = normalize_compact_scene_writer_output(
        strict,
        run_id="E2E-RUN-21-RECORDED-REPLAY-REPAIR17",
        required_locks=showrunner["canon_assignment_locks"],
        prohibited_changes=showrunner["prohibited_changes"],
        scene_id_contract=scene_contract,
        state_field_contract=state_contract,
    )
    assessment = assess_scene_writer_integration_contract(
        hydrated,
        run_id="E2E-RUN-21-RECORDED-REPLAY-REPAIR17",
        fixture_contract=fixture,
    )
    field = state_field_name(state_contract)
    hydrated_tokens = [scene["state_evidence"][field] for scene in hydrated["scene_packages"]]
    return {
        "result": "PASS" if assessment["passed"] and raw_tokens == hydrated_tokens else "FAIL",
        "decision": "RECORDED SCENE WRITER STATE-FIELD BRIDGE SATISFIES CORRECTED CONTRACT" if assessment["passed"] and raw_tokens == hydrated_tokens else "NEXT EXACT FAILURE",
        "state_field": field,
        "raw_machine_tokens": raw_tokens,
        "hydrated_machine_tokens": hydrated_tokens,
        "scene_ids": [scene["id"] for scene in original["scenes"]],
        "raw_response_sha256_before": raw_hash_before,
        "raw_response_sha256_after": hashlib.sha256(R21_RAW.read_bytes()).hexdigest(),
        "raw_arguments_unchanged": original == r21_arguments(),
        "historical_status": "BLOCKED",
        "historical_status_preserved": True,
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "live_e2e_runs": 0,
    }


def generic_source_leaks() -> list[Dict[str, str]]:
    literals = (
        "A-17", "许宁", "许曼", "周岚", "周启", "沈泊", "梁音",
        "E2E-FIX-01", "E2E-FIX-02", "E2E-FIX-03",
        "clothing_visual_state_code", "signboard_state", "camera_battery_state",
        "soaked_uniform", "changed_clothes", "signboard_on", "signboard_off",
        "battery_installed", "battery_removed_and_sealed", "cracked_white_porcelain_bowl",
    )
    leaks = []
    for path in GENERIC_SOURCES:
        text = path.read_text(encoding="utf-8")
        for literal in literals:
            if literal in text:
                leaks.append({"file": str(path), "literal": literal})
    return leaks
