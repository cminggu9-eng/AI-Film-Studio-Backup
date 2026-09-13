"""Strict function transport for one compiled-run Scene Writer integration.

This module owns only response transport.  It derives its field vocabulary from
the accepted Scene Writer integration, state, and compact-serialization
contracts; it neither changes canonical Skill semantics nor repairs output.
"""

from __future__ import annotations

import copy
from typing import Any, Dict, Mapping

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError, ValidationError

from runtime.shared_qa.model_executor import StructuredOutputContract
from scene_writer_compact_serialization import (
    COMPACT_FORMAT,
    COMPACT_CONTROL_FIELDS,
    COMPACT_SCENE_FIELDS,
    COMPACT_TOP_LEVEL_FIELDS,
    COMPACT_TOP_STATE_FIELDS,
)
from scene_writer_integration_contract import ALLOWED_REVEAL_STATUS_CODES, STRUCTURAL_FIELD_NAMES
from scene_writer_scene_id_contract import assess_scene_id_sequence, ordered_scene_ids
from scene_writer_state_field_contract import (
    allowed_machine_tokens,
    authorized_transition_tokens,
    state_field_name,
    tracked_entity_ids,
)


FUNCTION_NAME = "submit_scene_writer_package"
FUNCTION_DESCRIPTION = (
    "Submit one complete compact Scene Writer integration package through the "
    "current compiled-run contract as the sole structured response transport."
)
SCHEMA_VERSION = "0.1"
CANONICAL_PRIMARY_DECISION_STATES = (
    "SCENE_CREATED",
    "SCENE_REVISED",
    "NO_MATERIAL_CHANGE",
    "NEEDS_CONTEXT",
    "UPSTREAM_DECISION_REQUIRED",
    "REQUEST_OUT_OF_SCOPE",
)
CANONICAL_FLAGS_HANDOFFS = (
    "PRODUCTION_REVIEW_REQUIRED",
    "UPSTREAM_HANDOFF_REQUIRED",
    "SHARED_QA_HANDOFF_ELIGIBLE",
    "DIRECTOR_HANDOFF_ELIGIBLE",
    "CHARACTER_ACTING_HANDOFF_ELIGIBLE",
    "EXTERNAL_PRODUCTION_CONSTRAINT_DEFERRED",
    "EXTERNAL_PRODUCTION_CONSTRAINT_RECEIVED",
)
TRANSPORT_ABSENT = "ABSENT"
PROVIDER_STRICT_SCHEMA_LIMITATIONS = {
    "unsupported_keywords": ["minLength", "maxLength", "minItems", "maxItems"],
    "local_enforcement": [
        "exactly_three_scenes",
        "non_empty_text",
        "existing_compact_serialization_character_bounds",
    ],
}


class StrictTransportSchemaError(RuntimeError):
    """Arguments do not satisfy the accepted strict transport contract."""


def _object(properties: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "type": "object",
        "properties": copy.deepcopy(dict(properties)),
        "required": list(properties),
        "additionalProperties": False,
    }


def _string(*, enum: list[str] | None = None) -> Dict[str, Any]:
    value: Dict[str, Any] = {"type": "string"}
    if enum is not None:
        value["enum"] = enum
    return value


def _string_array(*, enum: list[str] | None = None) -> Dict[str, Any]:
    return {"type": "array", "items": _string(enum=enum)}


def _absent_or_canonical_token_array() -> Dict[str, Any]:
    """Keep ABSENT transport-only while limiting array values to canonical tokens."""

    return {"anyOf": [_string(enum=[TRANSPORT_ABSENT]), _string_array(enum=list(CANONICAL_FLAGS_HANDOFFS))]}


def _absent_or_string_array() -> Dict[str, Any]:
    """Retain the pre-existing non-token transport shape for unresolved decisions."""

    return {"anyOf": [_string(enum=[TRANSPORT_ABSENT]), _string_array()]}


def strict_function_schema(
    scene_id_contract: Mapping[str, Any] | None = None,
    state_field_contract: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """Return only features documented for DeepSeek strict function schemas."""

    structural = _object({name: _string() for name in STRUCTURAL_FIELD_NAMES})
    current_state_field = state_field_name(state_field_contract) if state_field_contract is not None else "machine_state"
    scene_state = _object({
        "entity_id": _string(enum=tracked_entity_ids(state_field_contract)) if state_field_contract is not None else _string(),
        "custody": _string(),
        "holders": _string_array(),
        "reveal": _string(enum=sorted(ALLOWED_REVEAL_STATUS_CODES)),
        "relationship": _string(),
        current_state_field: _string(enum=allowed_machine_tokens(state_field_contract)) if state_field_contract is not None else _string(),
        "state_display": _string(),
        "location": _string(),
        "transitions": _string_array(enum=authorized_transition_tokens(state_field_contract)) if state_field_contract is not None else _string_array(),
    })
    scene = _object({
        "id": _string(enum=ordered_scene_ids(scene_id_contract)) if scene_id_contract is not None else _string(),
        "content": _string(),
        "structural": structural,
        "state": scene_state,
    })
    state = _object({
        "prior": _object({
            "relationship_state": _string(),
            "knowledge_state": _string(),
            "visual_state": _string(),
        }),
        "current": _object({
            "relationship_state": _string(),
            "knowledge_state": _string(),
            "visual_state": _string(),
        }),
        "proposed": _object({
            "relationship_state": _string(),
            "knowledge_state": _string(),
            "visual_state": _string(),
        }),
        "knowledge_timing": _object({
            "reveal_of_shared_use": _string(),
            "reveal_of_room_content": _string(),
        }),
        "relationship": _object({
            "initial": _string(),
            "after_scene_1": _string(),
            "after_scene_3": _string(),
        }),
        "visual": _object({
            "scene_1": _string(),
            "scene_2": _string(),
            "scene_3": _string(),
        }),
    })
    control = _object({
        "outcome": _string(enum=list(CANONICAL_PRIMARY_DECISION_STATES)),
        "flags": _absent_or_canonical_token_array(),
        "handoffs": _absent_or_canonical_token_array(),
        "required_outcome": _string(),
        "unresolved_decisions": _absent_or_string_array(),
    })
    schema = _object({
        "format": _string(enum=[COMPACT_FORMAT]),
        "control": control,
        "state": state,
        "scenes": {"type": "array", "items": scene},
    })
    return schema


def schema_contract_coverage(
    scene_id_contract: Mapping[str, Any] | None = None,
    state_field_contract: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """Make source coverage reviewable without inventing a fourth contract."""

    schema = strict_function_schema(scene_id_contract, state_field_contract)
    return {
        "schema_version": SCHEMA_VERSION,
        "function_name": FUNCTION_NAME,
        "source_contracts": [
            "Scene_Writer_Integration_Output_Contract_V0.1",
            "Scene_Writer_Integration_State_Contract_V0.1",
            "Scene_Writer_Compact_Serialization_Contract_V0.1",
        ],
        "top_level_fields": sorted(COMPACT_TOP_LEVEL_FIELDS),
        "control_fields": sorted(COMPACT_CONTROL_FIELDS),
        "state_fields": sorted(COMPACT_TOP_STATE_FIELDS),
        "scene_fields": sorted(COMPACT_SCENE_FIELDS),
        "scene_state_fields": sorted(schema["properties"]["scenes"]["items"]["properties"]["state"]["properties"]),
        "structural_fields": list(STRUCTURAL_FIELD_NAMES),
        "scene_ids": ordered_scene_ids(scene_id_contract) if scene_id_contract is not None else "COMPILED_RUN_CONTRACT_REQUIRED",
        "state_field": state_field_name(state_field_contract) if state_field_contract is not None else "COMPILED_RUN_CONTRACT_REQUIRED",
        "state_tokens": allowed_machine_tokens(state_field_contract) if state_field_contract is not None else "COMPILED_RUN_CONTRACT_REQUIRED",
        "schema_top_level_required": schema["required"],
        "provider_strict_schema_limitations": copy.deepcopy(PROVIDER_STRICT_SCHEMA_LIMITATIONS),
    }


def validate_provider_strict_schema(
    scene_id_contract: Mapping[str, Any] | None = None,
    state_field_contract: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """Verify syntax and enforce the currently documented DeepSeek subset."""

    schema = strict_function_schema(scene_id_contract, state_field_contract)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise StrictTransportSchemaError(f"Schema syntax is invalid: {exc.message}") from exc
    unsupported = []

    def walk(value: Any, path: str) -> None:
        if isinstance(value, Mapping):
            for key, item in value.items():
                child_path = f"{path}.{key}" if path else str(key)
                if key in PROVIDER_STRICT_SCHEMA_LIMITATIONS["unsupported_keywords"]:
                    unsupported.append(child_path)
                walk(item, child_path)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                walk(item, f"{path}[{index}]")

    walk(schema, "")
    if unsupported:
        raise StrictTransportSchemaError(f"Provider-unsupported strict-schema keywords present: {unsupported}")
    return {
        "passed": True,
        "provider_strict_schema_subset": "required/enums/strings/arrays/objects/anyOf/additionalProperties=false",
        "unsupported_keywords_absent": True,
        "unsupported_keyword_paths": unsupported,
    }


def build_structured_output_contract(parameters_schema: Mapping[str, Any] | None = None) -> StructuredOutputContract:
    """Build one neutral contract; live callers must supply their compiled schema."""
    schema = strict_function_schema() if parameters_schema is None else copy.deepcopy(dict(parameters_schema))
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise StrictTransportSchemaError(f"Compiled strict schema is invalid: {exc.message}") from exc
    return StructuredOutputContract(
        function_name=FUNCTION_NAME,
        function_description=FUNCTION_DESCRIPTION,
        parameters_schema=schema,
    )


def validate_strict_scene_writer_arguments(
    arguments: Mapping[str, Any],
    *,
    parameters_schema: Mapping[str, Any] | None = None,
    scene_id_contract: Mapping[str, Any] | None = None,
    state_field_contract: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """Validate function arguments only; do not correct, normalize, or retry."""

    if not isinstance(arguments, Mapping):
        raise StrictTransportSchemaError("Function arguments must be a mapping")
    schema = copy.deepcopy(dict(parameters_schema)) if parameters_schema is not None else strict_function_schema(scene_id_contract, state_field_contract)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(arguments), key=lambda item: list(item.absolute_path))
    if errors:
        first = errors[0]
        location = "/".join(str(item) for item in first.absolute_path) or "<root>"
        raise StrictTransportSchemaError(f"JSON Schema validation failed at {location}: {first.message}")
    scenes = arguments.get("scenes")
    if scene_id_contract is not None:
        sequence = assess_scene_id_sequence(
            [scene.get("id") if isinstance(scene, Mapping) else None for scene in scenes] if isinstance(scenes, list) else [],
            scene_id_contract,
        )
        if sequence["result"] != "PASS":
            raise StrictTransportSchemaError(f"Scene IDs are not the exact compiled current-run ordered sequence: {sequence}")
    elif not isinstance(scenes, list) or len(scenes) != 3:
        raise StrictTransportSchemaError("Exactly three scenes are required by the compact contract")
    return copy.deepcopy(dict(arguments))


def validate_required_tool_call_shape(
    *,
    assistant_content: Any,
    tool_calls: Any,
    function_name: str = FUNCTION_NAME,
) -> Mapping[str, Any]:
    """Pure strict-response shape check for static tests; it performs no call or repair."""

    if isinstance(assistant_content, str) and assistant_content.strip():
        raise StrictTransportSchemaError("Ordinary assistant prose cannot replace the required structured function call")
    if not isinstance(tool_calls, list) or len(tool_calls) != 1:
        raise StrictTransportSchemaError("Exactly one required structured function call is required")
    tool_call = tool_calls[0]
    if not isinstance(tool_call, Mapping) or tool_call.get("type") != "function":
        raise StrictTransportSchemaError("Required structured call must be a function call")
    function = tool_call.get("function")
    if not isinstance(function, Mapping) or function.get("name") != function_name:
        raise StrictTransportSchemaError("Required structured function name was not received")
    if not isinstance(function.get("arguments"), str) or not function["arguments"].strip():
        raise StrictTransportSchemaError("Required structured function arguments are unavailable")
    return copy.deepcopy(dict(function))
