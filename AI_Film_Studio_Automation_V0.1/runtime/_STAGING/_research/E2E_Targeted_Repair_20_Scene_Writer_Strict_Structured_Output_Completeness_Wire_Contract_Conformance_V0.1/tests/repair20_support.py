"""Provider-free support for Repair20 Scene Writer completeness tests."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Dict, Mapping

from jsonschema import Draft202012Validator


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
REPAIR_17 = RESEARCH / "E2E_Targeted_Repair_17_Scene_Writer_Per_Run_State_Field_Bridge_Generic_Contract_Cleanup_V0.1"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
PHASE2 = RESEARCH / "Systemic_Hardening_Phase_2_Runtime_Reliability_Regression_Enforcement_V0.1"
R25 = HARNESS / "evidence" / "E2E-RUN-25"
R25_RAW = R25 / "artifacts" / "scene_writer_provider_response.json"
R25_WIRE = R25 / "artifacts" / "scene_writer_final_wire_payload.json"
R25_TRUNCATION = R25 / "artifacts" / "scene_writer_truncation_detection.json"
R25_VALIDATION = R25 / "artifacts" / "scene_writer_validation_error.json"

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
from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter
from runtime.shared_qa.model_executor import ModelRequest
from scene_writer_scene_id_contract import build_scene_id_contract
from scene_writer_schema_composer import compose
from scene_writer_state_field_contract import build_scene_writer_state_projection
from scene_writer_strict_transport import (
    FUNCTION_NAME,
    build_structured_output_contract,
    validate_strict_scene_writer_arguments,
)
import run_minimal_e2e as e2e


def f3_binding() -> Path:
    return REPAIR_07 / "fixtures" / "E2E_FIX_03_Runtime_Binding_V0.1.json"


def f3_contracts() -> tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    compiled = compile_path(f3_binding())
    scene_ids = build_scene_id_contract(compiled)
    state = build_scene_writer_state_projection(compiled)
    schema = compose(compiled, scene_id_contract=scene_ids, state_field_contract=state)
    return compiled, scene_ids, state, schema


def sample(schema: Mapping[str, Any]) -> Any:
    """Make a complete local test value solely from a schema; never use at runtime."""

    if "enum" in schema:
        return copy.deepcopy(schema["enum"][0])
    if "anyOf" in schema:
        return sample(schema["anyOf"][0])
    if schema.get("type") == "string":
        return "evidence"
    if schema.get("type") == "array":
        return [sample(schema["items"])]
    if schema.get("type") == "object":
        return {key: sample(value) for key, value in schema["properties"].items()}
    raise ValueError(f"unsupported schema shape: {schema}")


def complete_f3_arguments() -> Dict[str, Any]:
    _compiled, scene_ids, _state, schema = f3_contracts()
    payload = sample(schema)
    item_schema = schema["properties"]["scenes"]["items"]
    payload["scenes"] = []
    for scene_id in scene_ids["ordered_scene_ids"]:
        item = sample(item_schema)
        item["id"] = scene_id
        payload["scenes"].append(item)
    return payload


def r25_arguments() -> Dict[str, Any]:
    persisted = json.loads(R25_RAW.read_text(encoding="utf-8"))
    response = json.loads(persisted["raw_provider_response"])
    return json.loads(response["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"])


def r25_response() -> Dict[str, Any]:
    persisted = json.loads(R25_RAW.read_text(encoding="utf-8"))
    return json.loads(persisted["raw_provider_response"])


def r25_wire_payload() -> Dict[str, Any]:
    return json.loads(R25_WIRE.read_text(encoding="utf-8"))["payload"]


def local_errors(arguments: Mapping[str, Any], schema: Mapping[str, Any]) -> list[Dict[str, str]]:
    errors = sorted(Draft202012Validator(schema).iter_errors(arguments), key=lambda item: list(item.absolute_path))
    return [
        {
            "path": "/".join(str(part) for part in error.absolute_path) or "<root>",
            "message": error.message,
        }
        for error in errors
    ]


def r25_hashes() -> Dict[str, str]:
    return {
        name: hashlib.sha256(path.read_bytes()).hexdigest()
        for name, path in {
            "raw": R25_RAW,
            "wire": R25_WIRE,
            "truncation": R25_TRUNCATION,
            "validation": R25_VALIDATION,
        }.items()
    }


def current_wire_audit() -> Dict[str, Any]:
    compiled, scene_ids, state, schema = f3_contracts()
    strict = build_structured_output_contract(schema)
    prompt = e2e.build_system_prompt(
        e2e.role_spec("scene_writer"),
        "READ ONLY",
        structured_function_name=strict.function_name,
        structured_parameters_schema=strict.parameters_schema,
        scene_id_contract=scene_ids,
        state_field_contract=state,
    )
    request = ModelRequest(
        system_prompt=prompt,
        user_prompt="{}",
        model=e2e.MODEL,
        thinking_mode=e2e.THINKING_MODE,
        max_tokens=5000,
        response_format=None,
        structured_output=strict,
    )
    payload, endpoint = DeepSeekProviderAdapter.build_provider_payload(request)
    function = payload["tools"][0]["function"]
    manifest = e2e.scene_writer_schema_identity_manifest(
        compiled_schema=schema,
        final_strict_schema=strict.parameters_schema,
        adapter_projected_schema=function["parameters"],
        wire_schema=function["parameters"],
        local_validator_schema=strict.parameters_schema,
        function_name=strict.function_name,
        wire_function_name=function["name"],
        wire_strict=function["strict"],
        wire_tool_choice=payload["tool_choice"],
    )
    return {
        "compiled": compiled,
        "scene_ids": scene_ids,
        "state": state,
        "schema": schema,
        "strict": strict,
        "prompt": prompt,
        "payload": payload,
        "endpoint": endpoint,
        "manifest": manifest,
    }


def rejects(arguments: Mapping[str, Any], schema: Mapping[str, Any], scene_ids: Mapping[str, Any], state: Mapping[str, Any]) -> bool:
    try:
        validate_strict_scene_writer_arguments(
            arguments,
            parameters_schema=schema,
            scene_id_contract=scene_ids,
            state_field_contract=state,
        )
    except Exception:
        return True
    return False

