"""Lossless DeepSeek strict-schema projection for the Director contract."""
from __future__ import annotations
import copy
from typing import Any, Dict, Mapping
from jsonschema import Draft202012Validator, ValidationError
from runtime.shared_qa.model_executor import StructuredOutputContract
from director_structured_submission import FUNCTION_NAME, director_submission_schema
from director_state_object_contract import lint_deepseek_strict_schema, stable_hash

PROJECTION_ID = "DIRECTOR_DEEPSEEK_STRICT_COMPATIBILITY_PROJECTION_V0.1"
WIRE_CODEC_ID = "DIRECTOR_DEEPSEEK_TAGGED_UNION_CODEC_V1"
_TAGGED_STATUS = "status"
_TAGGED_ITEMS = "items"


class DirectorProviderWireError(ValueError):
    """A provider argument did not conform to the approved Director wire contract."""


def _is_absent_or_text_array(schema: Any) -> bool:
    """Recognize only the canonical ABSENT | array[text] union shape."""
    if not isinstance(schema, Mapping) or set(schema) != {"anyOf"}:
        return False
    members = schema["anyOf"]
    if not isinstance(members, list) or len(members) != 2:
        return False
    absent = [member for member in members if isinstance(member, Mapping) and member == {"const": "ABSENT"}]
    arrays = [member for member in members if isinstance(member, Mapping) and member.get("type") == "array"]
    return len(absent) == 1 and len(arrays) == 1 and arrays[0].get("items") == {"type": "string", "minLength": 1}


def tagged_union_field_names(state_contract: Mapping[str, Any]) -> tuple[str, ...]:
    canonical = director_submission_schema(state_contract)
    fields = tuple(name for name, schema in canonical["properties"].items() if _is_absent_or_text_array(schema))
    if fields != ("unresolved_decisions",):
        raise DirectorProviderWireError("Director tagged-wire projection is limited to the approved canonical ABSENT | array[text] field")
    return fields


def _tagged_union_wire_schema() -> Dict[str, Any]:
    # `minLength` is deliberately omitted because this is the DeepSeek strict
    # subset; the canonical validator is the authoritative text-quality check.
    return {
        "type": "object",
        "additionalProperties": False,
        "required": [_TAGGED_STATUS, _TAGGED_ITEMS],
        "properties": {
            _TAGGED_STATUS: {"type": "string", "enum": ["ABSENT", "PRESENT"]},
            _TAGGED_ITEMS: {"type": "array", "items": {"type": "string"}},
        },
    }

def deepseek_compatible_schema(state_contract: Mapping[str, Any]) -> Dict[str, Any]:
    """Project only provider-unsupported representation, never role semantics."""
    def project(value: Any) -> Any:
        if isinstance(value, Mapping):
            result = {key: project(item) for key, item in value.items() if key != "minLength"}
            if "const" in result:
                constant = result.pop("const")
                if "enum" in result or "anyOf" in result:
                    raise ValueError("const projection would alter an existing semantic domain")
                if not isinstance(constant, str):
                    raise ValueError("DeepSeek fixed-value projection is limited to string constants")
                if "type" in result and result["type"] != "string":
                    raise ValueError("fixed string projection cannot override an existing non-string type")
                result["type"] = "string"
                result["enum"] = [constant]
            return result
        if isinstance(value, list): return [project(item) for item in value]
        return copy.deepcopy(value)
    canonical = director_submission_schema(state_contract)
    tagged_fields = tagged_union_field_names(state_contract)
    schema = project(canonical)
    for field in tagged_fields:
        schema["properties"][field] = _tagged_union_wire_schema()
    lint_deepseek_strict_schema(schema)
    return schema


def provider_wire_manifest(state_contract: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "codec_id": WIRE_CODEC_ID,
        "canonical_schema_hash": stable_hash(director_submission_schema(state_contract)),
        "wire_schema_hash": stable_hash(deepseek_compatible_schema(state_contract)),
        "tagged_union_fields": list(tagged_union_field_names(state_contract)),
        "canonical_domain": "ABSENT | array[text]",
        "wire_domain": {"status": "ABSENT | PRESENT", "items": "array[text]"},
        "lossless_empty_array": True,
    }


def validate_director_provider_wire_arguments(arguments: Mapping[str, Any], state_contract: Mapping[str, Any]) -> Dict[str, Any]:
    """Validate raw tool arguments against the provider-facing schema before decoding."""
    if not isinstance(arguments, Mapping):
        raise DirectorProviderWireError("Director provider wire arguments must be an object")
    schema = deepseek_compatible_schema(state_contract)
    try:
        Draft202012Validator(schema).validate(dict(arguments))
    except ValidationError as exc:
        raise DirectorProviderWireError(f"Director provider wire schema rejected arguments: {exc.message}") from exc
    result = copy.deepcopy(dict(arguments))
    for field in tagged_union_field_names(state_contract):
        tagged = result[field]
        status, items = tagged[_TAGGED_STATUS], tagged[_TAGGED_ITEMS]
        if status == "ABSENT" and items != []:
            raise DirectorProviderWireError(f"Director provider wire {field} ABSENT requires an empty items array")
        if any(not isinstance(item, str) for item in items):
            raise DirectorProviderWireError(f"Director provider wire {field} items must be native text values")
    return result


def decode_director_provider_wire_arguments(arguments: Mapping[str, Any], state_contract: Mapping[str, Any]) -> Dict[str, Any]:
    """Deterministically map an already-validated tagged wire object to canonical values."""
    result = copy.deepcopy(dict(arguments))
    for field in tagged_union_field_names(state_contract):
        tagged = result.get(field)
        if not isinstance(tagged, Mapping) or set(tagged) != {_TAGGED_STATUS, _TAGGED_ITEMS}:
            raise DirectorProviderWireError(f"Director provider wire {field} is not a tagged union object")
        status, items = tagged.get(_TAGGED_STATUS), tagged.get(_TAGGED_ITEMS)
        if status == "ABSENT":
            if items != []:
                raise DirectorProviderWireError(f"Director provider wire {field} cannot decode ABSENT with items")
            result[field] = "ABSENT"
        elif status == "PRESENT" and isinstance(items, list):
            result[field] = copy.deepcopy(items)
        else:
            raise DirectorProviderWireError(f"Director provider wire {field} has an invalid tagged state")
    return result

def equivalence_report(state_contract: Mapping[str, Any]) -> Dict[str, Any]:
    neutral, projected = director_submission_schema(state_contract), deepseek_compatible_schema(state_contract)
    if neutral["required"] != projected["required"] or set(neutral["properties"]) != set(projected["properties"]):
        raise ValueError("projection removed or weakened a required Director field")
    typed_absence = {"type": "string", "enum": ["ABSENT"]}
    dynamic = ("relevant_prior_state", "current_state")
    projected_state = projected["properties"]["state_evidence"]["properties"]
    if any(projected_state[field].get("type") != "object" for field in dynamic):
        raise ValueError("projection changed a dynamic Director state object representation")
    tagged_fields = tagged_union_field_names(state_contract)
    if any(projected["properties"][field] != _tagged_union_wire_schema() for field in tagged_fields):
        raise ValueError("projection did not install the approved tagged-union wire schema")
    return {
        "projection_id": PROJECTION_ID,
        "required_fields_preserved": True,
        "machine_fields_preserved": [key for key in neutral["required"] if key not in ("selected_mode", "primary_state_or_outcome", "flags", "handoffs", "required_outcome", "unresolved_decisions", "state_evidence")],
        "canonical_enums_preserved": neutral["properties"]["selected_mode"]["enum"] == projected["properties"]["selected_mode"]["enum"] and neutral["properties"]["primary_state_or_outcome"]["enum"] == projected["properties"]["primary_state_or_outcome"]["enum"],
        "absence_equivalence": projected["properties"]["flags"] == typed_absence and projected["properties"]["handoffs"] == typed_absence,
        "dynamic_object_representation_preserved": True,
        "legacy_string_representation": "UNREACHABLE",
        "fixed_string_enum_representation": typed_absence,
        "provider_wire_codec": provider_wire_manifest(state_contract),
        "removed_representation_keywords": ["minLength", "const"],
        "neutral_schema_hash": stable_hash(neutral),
        "projected_schema_hash": stable_hash(projected),
    }

def build_deepseek_compatible_director_contract(state_contract: Mapping[str, Any]) -> StructuredOutputContract:
    equivalence_report(state_contract)
    return StructuredOutputContract(FUNCTION_NAME, "Submit complete Director-owned semantic, control, and source-backed state payload.", deepseek_compatible_schema(state_contract))
