"""Strict provider-neutral Director submission compiled from Repair 09J state authority."""
from __future__ import annotations
import copy
from typing import Any, Callable, Dict, Mapping, Sequence
from runtime.shared_qa.model_executor import StructuredOutputContract
from director_integration_contract import ABSENT, DIRECTOR_CANONICAL_MODES, DIRECTOR_PRIMARY_STATES, DIRECTOR_SEMANTIC_FIELDS
from director_state_object_contract import (
    DYNAMIC_FIELDS,
    EXACT_ABSENT_FIELDS,
    DirectorStateObjectContractError,
    stable_hash,
    validate_director_state_values,
)

FUNCTION_NAME = "submit_director_package"
STATE_DIMENSIONS = ("relevant_prior_state", "current_state", "proposed_state", "knowledge_timing", "relationship_state", "visual_state")
DYNAMIC_OBJECT_STATE_FIELDS = DYNAMIC_FIELDS
JSON_OBJECT_STRING_STATE_FIELDS = DYNAMIC_FIELDS  # Deprecated historical alias; never used by the live contract.
EXACT_ABSENT_STATE_FIELDS = EXACT_ABSENT_FIELDS
RELATIONSHIP_STATE_FIELD = "relationship_state"
SEMANTIC_FIELD_IDS = tuple(field for field, _ in DIRECTOR_SEMANTIC_FIELDS)
OUTER_FIELD_IDS = (
    "selected_mode", "primary_state_or_outcome", "flags", "handoffs",
    "required_outcome", "unresolved_decisions", "state_evidence", *SEMANTIC_FIELD_IDS,
)

class DirectorStructuredSubmissionError(ValueError): pass

def _absence_or_array() -> Dict[str, Any]:
    return {"anyOf": [{"const": ABSENT}, {"type": "array", "items": {"type": "string", "minLength": 1}}]}

def director_submission_schema(state_contract: Mapping[str, Any]) -> Dict[str, Any]:
    schemas = state_contract.get("state_schemas")
    if not isinstance(schemas, Mapping) or set(schemas) != set((*DYNAMIC_OBJECT_STATE_FIELDS, *EXACT_ABSENT_STATE_FIELDS)):
        raise DirectorStructuredSubmissionError("Director compiled state contract is missing exact five-field schemas")
    state_properties = copy.deepcopy(dict(schemas))
    state_properties[RELATIONSHIP_STATE_FIELD] = {"anyOf": [{"const": ABSENT}, {"type": "string", "minLength": 1}]}
    p: Dict[str, Any] = {
        "selected_mode": {"type": "string", "enum": list(DIRECTOR_CANONICAL_MODES)},
        "primary_state_or_outcome": {"type": "string", "enum": list(DIRECTOR_PRIMARY_STATES)},
        "flags": {"const": ABSENT}, "handoffs": {"const": ABSENT},
        "required_outcome": {"type": "string", "minLength": 1}, "unresolved_decisions": _absence_or_array(),
        "state_evidence": {"type": "object", "additionalProperties": False, "required": list(STATE_DIMENSIONS), "properties": state_properties},
    }
    p.update({field: {"type": "string", "minLength": 1} for field in SEMANTIC_FIELD_IDS})
    return {"type": "object", "additionalProperties": False, "required": list(p), "properties": p}

def build_director_structured_output_contract(state_contract: Mapping[str, Any]) -> StructuredOutputContract:
    return StructuredOutputContract(FUNCTION_NAME, "Submit complete Director-owned semantic, control, and source-backed state payload.", director_submission_schema(state_contract))

def director_structured_contract_manifest(schema: Mapping[str, Any], state_contract: Mapping[str, Any] | None = None) -> Dict[str, Any]:
    """One machine-source manifest for prompt, function, and validator identity."""
    source = dict(schema)
    properties = source.get("properties")
    required = source.get("required")
    if not isinstance(properties, Mapping) or not isinstance(required, list) or set(properties) != set(required) or set(required) != set(OUTER_FIELD_IDS) or len(required) != 15:
        raise DirectorStructuredSubmissionError("Director structured contract manifest is invalid")
    manifest = {
        "allowed_fields": list(properties),
        "required_fields": list(required),
        "dynamic_object_state_fields": list(DYNAMIC_OBJECT_STATE_FIELDS),
        "exact_absent_state_fields": list(EXACT_ABSENT_STATE_FIELDS),
        "relationship_state_field": RELATIONSHIP_STATE_FIELD,
        "selected_mode_domain": list(DIRECTOR_CANONICAL_MODES),
        "primary_state_domain": list(DIRECTOR_PRIMARY_STATES),
        "state_schema_hash": stable_hash(source["properties"]["state_evidence"]["properties"]),
        "legacy_string_representation": "UNREACHABLE",
    }
    if state_contract is not None:
        manifest["compiled_state_schema_hash"] = state_contract.get("state_schema_hash")
        manifest["source_trace_hash"] = state_contract.get("source_trace_hash")
    return manifest

def director_prompt_contract_manifest(schema: Mapping[str, Any], state_contract: Mapping[str, Any] | None = None) -> Dict[str, Any]:
    return director_structured_contract_manifest(schema, state_contract)

def director_validator_contract_manifest(state_contract: Mapping[str, Any]) -> Dict[str, Any]:
    return director_structured_contract_manifest(director_submission_schema(state_contract), state_contract)

def assert_director_contract_identity(*manifests: Mapping[str, Any]) -> Dict[str, Any]:
    if len(manifests) != 3:
        raise DirectorStructuredSubmissionError("Prompt/Function/Validator identity requires exactly three manifests")
    comparable = [
        {key: value for key, value in manifest.items() if key != "state_schema_hash"}
        for manifest in manifests
    ]
    if any(item != comparable[0] for item in comparable[1:]):
        raise DirectorStructuredSubmissionError("Prompt/Function/Validator manifest drift")
    return {"result": "PASS", "manifest_hash": stable_hash(comparable[0]), "outer_field_count": 15}

def _schema_type_domain(schema: Mapping[str, Any]) -> str:
    """Render a compact JSON-type domain from the supplied schema only."""
    if "anyOf" in schema:
        choices = schema["anyOf"]
        if not isinstance(choices, list) or not choices:
            raise DirectorStructuredSubmissionError("Director type reminder requires non-empty anyOf branches")
        return " | ".join(_schema_type_domain(choice) for choice in choices)
    if "const" in schema:
        return f"exact JSON string {schema['const']!r}"
    value_type = schema.get("type")
    if value_type == "array":
        items = schema.get("items")
        if not isinstance(items, Mapping):
            raise DirectorStructuredSubmissionError("Director array type reminder requires an item schema")
        return f"native JSON array<{_schema_type_domain(items)}>"
    if value_type == "object":
        return "native JSON object"
    if value_type == "string":
        values = schema.get("enum")
        if values == [ABSENT]:
            return "exact JSON string 'ABSENT'"
        return "JSON string"
    raise DirectorStructuredSubmissionError("Director type reminder encountered an unsupported schema domain")


def director_native_json_type_manifest(final_parameters_schema: Mapping[str, Any]) -> Dict[str, Any]:
    """Derive container and ABSENT requirements from final function parameters.

    The manifest deliberately stops at the State Evidence boundary.  The nested
    per-run state-object schema remains the authoritative source for scene IDs
    and values; this generic reminder must never duplicate that runtime data.
    """
    properties = final_parameters_schema.get("properties")
    required = final_parameters_schema.get("required")
    if not isinstance(properties, Mapping) or not isinstance(required, list) or set(properties) != set(required):
        raise DirectorStructuredSubmissionError("Director type reminder requires a closed final function schema")
    field_domains: Dict[str, str] = {}
    for field in required:
        schema = properties[field]
        if not isinstance(schema, Mapping):
            raise DirectorStructuredSubmissionError(f"Director type reminder field is not a schema: {field}")
        domain = _schema_type_domain(schema)
        if "native JSON array" in domain or "native JSON object" in domain or "'ABSENT'" in domain:
            field_domains[field] = domain
    state_schema = properties.get("state_evidence")
    if not isinstance(state_schema, Mapping) or state_schema.get("type") != "object":
        raise DirectorStructuredSubmissionError("Director type reminder requires object State Evidence")
    state_properties = state_schema.get("properties")
    state_required = state_schema.get("required")
    if not isinstance(state_properties, Mapping) or not isinstance(state_required, list) or set(state_properties) != set(state_required):
        raise DirectorStructuredSubmissionError("Director type reminder requires closed State Evidence")
    for field in state_required:
        schema = state_properties[field]
        if not isinstance(schema, Mapping):
            raise DirectorStructuredSubmissionError(f"Director state type reminder field is not a schema: {field}")
        domain = _schema_type_domain(schema)
        if "native JSON array" in domain or "native JSON object" in domain or "'ABSENT'" in domain:
            field_domains[f"state_evidence.{field}"] = domain
    return {
        "source": "FINAL_FUNCTION_PARAMETERS",
        "outer_field_count": len(required),
        "field_domains": field_domains,
    }


def build_director_native_json_type_instruction(final_parameters_schema: Mapping[str, Any]) -> str:
    """Emit a provider-facing reminder without maintaining a role/fixture alias table."""
    import json
    manifest = director_native_json_type_manifest(final_parameters_schema)
    domains = json.dumps(manifest["field_domains"], ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return (
        "NATIVE JSON TYPE INTEGRITY (DERIVED FROM FINAL FUNCTION PARAMETERS): "
        "Use native JSON types exactly as declared by the function schema. "
        "Never serialize an array or object into a JSON string, and never stringify a JSON container before submission. "
        "Each field must preserve its schema-declared JSON type; the exact token ABSENT is not interchangeable with null, an empty string, an empty array, or an empty object. "
        f"Schema-derived container and ABSENT domains: {domains}. "
    )


def build_director_structured_prompt_instruction(final_parameters_schema: Mapping[str, Any]) -> str:
    """Derive the only Director structured prompt contract from final parameters."""
    import json
    final = director_prompt_contract_manifest(final_parameters_schema)
    fields = json.dumps(final["allowed_fields"], ensure_ascii=False, separators=(",", ":"))
    modes = json.dumps(final["selected_mode_domain"], ensure_ascii=False, separators=(",", ":"))
    states = json.dumps(final["primary_state_domain"], ensure_ascii=False, separators=(",", ":"))
    state_schema = final_parameters_schema["properties"]["state_evidence"]["properties"]
    relevant_schema = json.dumps(state_schema["relevant_prior_state"], ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    current_schema = json.dumps(state_schema["current_state"], ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return "".join((
        "DIRECTOR STRUCTURED FUNCTION CONTRACT (DERIVED FROM FINAL FUNCTION PARAMETERS): "
        f"Emit exactly these 15 required fields and no others: {fields}. "
        f"selected_mode must be one of {modes}; primary_state_or_outcome must be one of {states}. "
        "Submit only submit_director_package arguments; do not emit content, canon_assignment_locks, prohibited_changes, or scene_packages. "
        "Locks and prohibitions are carried forward by the runtime from frozen upstream input and must not be repeated as function arguments. "
        f"relevant_prior_state must be a JSON object matching this exact per-run schema: {relevant_schema}. "
        f"current_state must be a JSON object matching this exact per-run schema: {current_schema}. "
        "Copy their source-owned values exactly from director_state_projection; do not select, infer, rename, add, or change a state value. "
        "proposed_state, knowledge_timing, and visual_state must each be the exact string ABSENT. "
        "Never JSON-encode any state object as a string. "
        "relationship_state must be a non-empty string or ABSENT. "
        , build_director_native_json_type_instruction(final_parameters_schema),
        "Place the eight Director deliverables in their matching named fields; do not add a generic content field. "
    ))

def deterministic_display_projection(payload: Mapping[str, Any]) -> str:
    return "\n\n".join(f"{heading}\n{payload[field]}" for field, heading in DIRECTOR_SEMANTIC_FIELDS)

def make_director_payload_validator(*, selected_mode: str, required_locks: Sequence[str], prohibited_changes: Sequence[str], state_contract: Mapping[str, Any]) -> Callable[[Mapping[str, Any]], Dict[str, Any]]:
    carried_locks, carried_prohibitions = list(required_locks), list(prohibited_changes)
    def validate(payload: Mapping[str, Any]) -> Dict[str, Any]:
        schema = director_submission_schema(state_contract)
        if not isinstance(payload, Mapping) or set(payload) != set(schema["required"]): raise DirectorStructuredSubmissionError("Director payload did not match exact required field set")
        result = copy.deepcopy(dict(payload))
        if result["selected_mode"] != selected_mode or result["selected_mode"] not in DIRECTOR_CANONICAL_MODES: raise DirectorStructuredSubmissionError("Director mode is missing or not canonical")
        if result["primary_state_or_outcome"] not in DIRECTOR_PRIMARY_STATES: raise DirectorStructuredSubmissionError("Director primary state is not canonical")
        if result["flags"] != ABSENT or result["handoffs"] != ABSENT: raise DirectorStructuredSubmissionError("Director flags and handoffs must be ABSENT")
        for field in SEMANTIC_FIELD_IDS:
            if not isinstance(result[field], str) or not result[field].strip(): raise DirectorStructuredSubmissionError(f"Director required semantic field is missing: {field}")
        if not isinstance(result["required_outcome"], str) or not result["required_outcome"].strip(): raise DirectorStructuredSubmissionError("Director required_outcome must be explicit")
        if result["unresolved_decisions"] != ABSENT and (not isinstance(result["unresolved_decisions"], list) or not all(isinstance(x, str) and x.strip() for x in result["unresolved_decisions"])): raise DirectorStructuredSubmissionError("Director unresolved_decisions must be ABSENT or text list")
        state = result["state_evidence"]
        if not isinstance(state, Mapping) or set(state) != set(STATE_DIMENSIONS) or any(v is None for v in state.values()): raise DirectorStructuredSubmissionError("Director state evidence is incomplete")
        state = copy.deepcopy(dict(state))
        try:
            state = validate_director_state_values(state, state_contract)
        except DirectorStateObjectContractError as exc:
            raise DirectorStructuredSubmissionError(str(exc)) from exc
        relationship = state[RELATIONSHIP_STATE_FIELD]
        if relationship != ABSENT and (not isinstance(relationship, str) or not relationship.strip()): raise DirectorStructuredSubmissionError("Director state_evidence.relationship_state must be text or ABSENT")
        return {"primary_state_or_outcome": result["primary_state_or_outcome"], "flags": ABSENT, "handoffs": ABSENT, "canon_assignment_locks": copy.deepcopy(carried_locks), "prohibited_changes": copy.deepcopy(carried_prohibitions), "required_outcome": result["required_outcome"], "unresolved_decisions": result["unresolved_decisions"], "state_evidence": copy.deepcopy(dict(state)), "content": deterministic_display_projection(result), "scene_packages": ABSENT}
    return validate
