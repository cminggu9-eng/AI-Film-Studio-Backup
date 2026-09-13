"""Per-run Director state object contract compiled from Repair 09J authority."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Mapping, Sequence


ABSENT = "ABSENT"
COMPILER_ID = "DIRECTOR_STATE_OBJECT_SCHEMA_COMPILER_V0.1"
DYNAMIC_FIELDS = ("relevant_prior_state", "current_state")
EXACT_ABSENT_FIELDS = ("proposed_state", "knowledge_timing", "visual_state")
SOURCE_RECORD_FIELDS = {
    "scene_id",
    "source_record_id",
    "source_version",
    "canonical_owner",
    "lifecycle_state",
    "ledger_sequence",
    "state_snapshot",
}
TRACE_FIELDS = {
    "field", "scene", "property", "source_contract_pointer", "source_version",
    "canonical_owner", "source_record_id", "ledger_sequence", "type_source",
    "enum_source", "requiredness_source", "projection_rule",
}
PRIOR_ABSENCE_AUTHORITY_FIELDS = {
    "decision", "source_contract_pointer", "source_version", "canonical_owner", "source_record_id",
}
VALID_LIFECYCLE_STATES = {
    "SEMANTIC_SAFEGUARD_ACCEPTED": 1,
    "STATE_LEDGER_COMMITTED": 2,
}
AUTHORITY_FILENAMES = (
    "Director_State_Projection_Authority_Decisions_V0.1.md",
    "Director_relevant_prior_state_Selection_Contract_V0.1.md",
    "Director_current_state_Selection_Contract_V0.1.md",
    "Director_proposed_state_Selection_Contract_V0.1.md",
    "Director_knowledge_timing_Selection_Contract_V0.1.md",
    "Director_visual_state_Selection_Contract_V0.1.md",
    "Director_State_Source_Winner_Contract_V0.1.md",
    "Director_State_ABSENT_Closure_Contract_V0.1.md",
)


class DirectorStateObjectContractError(ValueError):
    """The per-run state schema or a source-backed payload is invalid."""


def _stable_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def stable_hash(value: Any) -> str:
    return hashlib.sha256(_stable_json(value).encode("utf-8")).hexdigest()


def _research_root() -> Path:
    current = Path(__file__).resolve()
    return next(parent for parent in current.parents if parent.name == "_research")


def load_repair_09j_authority() -> Dict[str, Any]:
    root = _research_root() / "E2E_Targeted_Repair_09J_Director_State_Projection_Authority_Closure_V0.1"
    hashes: Dict[str, str] = {}
    for name in AUTHORITY_FILENAMES:
        path = root / name
        if not path.is_file():
            raise DirectorStateObjectContractError(f"Repair 09J authority contract is missing: {name}")
        hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return {
        "authority_id": "REPAIR_09J_DIRECTOR_STATE_PROJECTION_AUTHORITY_V0.1",
        "contract_root": str(root),
        "contract_hashes": hashes,
        "authority_bundle_hash": stable_hash(hashes),
    }


def _compiled_state_schema(compiled: Mapping[str, Any]) -> Dict[str, Any]:
    try:
        scene_ids = compiled["scene_ids"]
        state_enums = compiled["state_enums"]
        source = compiled["strict_schema"]["properties"]["scene_packages"]["items"]["properties"]["state"]
    except (KeyError, TypeError) as exc:
        raise DirectorStateObjectContractError("compiled_run_contract lacks a closed scene-state schema") from exc
    if not isinstance(scene_ids, list) or not scene_ids or len(scene_ids) != len(set(scene_ids)) or not all(isinstance(item, str) and item for item in scene_ids):
        raise DirectorStateObjectContractError("compiled scene IDs must be unique non-empty strings")
    if not isinstance(state_enums, Mapping) or not state_enums:
        raise DirectorStateObjectContractError("compiled state enums are required")
    expected_properties = {
        key: {"type": "string", "enum": copy.deepcopy(list(values))}
        for key, values in state_enums.items()
    }
    expected = {
        "type": "object",
        "properties": expected_properties,
        "required": list(state_enums),
        "additionalProperties": False,
    }
    if source != expected:
        raise DirectorStateObjectContractError("compiled strict state schema is not identical to state_enums")
    for key, values in state_enums.items():
        if not isinstance(key, str) or not key or not isinstance(values, list) or not values or len(values) != len(set(values)) or not all(isinstance(value, str) and value for value in values):
            raise DirectorStateObjectContractError(f"compiled state enum is not closed: {key}")
    return copy.deepcopy(expected)


def _normalize_records(
    compiled: Mapping[str, Any],
    records: Sequence[Mapping[str, Any]],
    *,
    require_all: bool,
    required_lifecycle: str | None = None,
) -> Dict[str, Dict[str, Any]]:
    if not isinstance(records, Sequence) or isinstance(records, (str, bytes)):
        raise DirectorStateObjectContractError("validated upstream state records must be a sequence")
    scene_ids = list(compiled["scene_ids"])
    dimensions = dict(compiled["state_enums"])
    grouped: Dict[str, list[Dict[str, Any]]] = {scene_id: [] for scene_id in scene_ids}
    for raw in records:
        if not isinstance(raw, Mapping) or set(raw) != SOURCE_RECORD_FIELDS:
            raise DirectorStateObjectContractError("source record does not match the exact projection input contract")
        record = copy.deepcopy(dict(raw))
        scene_id = record["scene_id"]
        if scene_id not in grouped:
            raise DirectorStateObjectContractError(f"source record has a non-compiled scene ID: {scene_id}")
        if record["canonical_owner"] != "Scene Writer":
            raise DirectorStateObjectContractError("current-state source owner must be Scene Writer")
        lifecycle = record["lifecycle_state"]
        if lifecycle not in VALID_LIFECYCLE_STATES:
            raise DirectorStateObjectContractError("source record lifecycle is not validated")
        if required_lifecycle is not None and lifecycle != required_lifecycle:
            raise DirectorStateObjectContractError(f"source record lifecycle must be {required_lifecycle}")
        if not isinstance(record["ledger_sequence"], int) or record["ledger_sequence"] <= 0:
            raise DirectorStateObjectContractError("source record ledger sequence must be positive")
        for field in ("source_record_id", "source_version"):
            if not isinstance(record[field], str) or not record[field].strip():
                raise DirectorStateObjectContractError(f"source record {field} is required")
        snapshot = record["state_snapshot"]
        if not isinstance(snapshot, Mapping):
            raise DirectorStateObjectContractError("source record state_snapshot must be an object")
        for dimension, domain in dimensions.items():
            if dimension not in snapshot:
                raise DirectorStateObjectContractError(f"missing required source dimension: {scene_id}.{dimension}")
            if snapshot[dimension] not in domain:
                raise DirectorStateObjectContractError(f"source dimension is outside its compiled enum: {scene_id}.{dimension}")
        grouped[scene_id].append(record)
    winners: Dict[str, Dict[str, Any]] = {}
    for scene_id in scene_ids:
        candidates = grouped[scene_id]
        if not candidates:
            if require_all:
                raise DirectorStateObjectContractError(f"missing required source record: {scene_id}")
            continue
        best_rank = max((VALID_LIFECYCLE_STATES[item["lifecycle_state"]], item["ledger_sequence"]) for item in candidates)
        finalists = [item for item in candidates if (VALID_LIFECYCLE_STATES[item["lifecycle_state"]], item["ledger_sequence"]) == best_rank]
        projected = [{dimension: item["state_snapshot"][dimension] for dimension in dimensions} for item in finalists]
        if any(value != projected[0] for value in projected[1:]):
            raise DirectorStateObjectContractError(f"STATE SOURCE CONFLICT: {scene_id}")
        finalists.sort(key=lambda item: (item["source_record_id"], item["source_version"]))
        winners[scene_id] = finalists[0]
    return winners


def _scene_object_schema(compiled: Mapping[str, Any], state_schema: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "type": "object",
        "properties": {scene_id: copy.deepcopy(dict(state_schema)) for scene_id in compiled["scene_ids"]},
        "required": list(compiled["scene_ids"]),
        "additionalProperties": False,
    }


def compile_director_state_object_contract(
    *,
    compiled_run_contract: Mapping[str, Any],
    validated_upstream_state_records: Sequence[Mapping[str, Any]],
    run_local_state_ledger_records: Sequence[Mapping[str, Any]],
    required_locks: Sequence[str],
    transition_authority_records: Sequence[Mapping[str, Any]] = (),
    prior_absence_authority: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """Compile the exact five-field schema bundle and expected source values."""
    authority = load_repair_09j_authority()
    compiled = copy.deepcopy(dict(compiled_run_contract))
    state_schema = _compiled_state_schema(compiled)
    upstream_winners = _normalize_records(compiled, validated_upstream_state_records, require_all=False)
    ledger_winners = _normalize_records(compiled, run_local_state_ledger_records, require_all=True, required_lifecycle="STATE_LEDGER_COMMITTED")
    if not isinstance(required_locks, Sequence) or isinstance(required_locks, (str, bytes)) or not all(isinstance(item, str) and item for item in required_locks):
        raise DirectorStateObjectContractError("required locks must be an explicit string sequence")
    if not isinstance(transition_authority_records, Sequence) or isinstance(transition_authority_records, (str, bytes)):
        raise DirectorStateObjectContractError("transition authority records must be a sequence")

    compiled_hash = stable_hash(compiled)
    dimensions = list(compiled["state_enums"])
    scene_ids = list(compiled["scene_ids"])
    current: Dict[str, Dict[str, Any]] = {}
    prior: Dict[str, Dict[str, Any]] | str = {}
    trace: list[Dict[str, Any]] = []

    for scene_index, scene_id in enumerate(scene_ids):
        winner = ledger_winners[scene_id]
        current[scene_id] = {dimension: copy.deepcopy(winner["state_snapshot"][dimension]) for dimension in dimensions}
        if scene_index == 0:
            if scene_id in upstream_winners:
                upstream = upstream_winners[scene_id]
                prior[scene_id] = {dimension: copy.deepcopy(upstream["state_snapshot"][dimension]) for dimension in dimensions}
                prior_source = {
                    "source_record_id": upstream["source_record_id"],
                    "source_version": upstream["source_version"],
                    "canonical_owner": upstream["canonical_owner"],
                    "ledger_sequence": upstream["ledger_sequence"],
                    "pointer_prefix": f"validated_upstream_state_records#/{scene_id}/state_snapshot",
                }
            else:
                prior[scene_id] = {dimension: copy.deepcopy(compiled["state_enums"][dimension][0]) for dimension in dimensions}
                prior_source = {
                    "source_record_id": f"{compiled['fixture']['fixture_id']}/compiled-initial-state",
                    "source_version": compiled_hash,
                    "canonical_owner": "Compiled Run Contract",
                    "ledger_sequence": 0,
                    "pointer_prefix": "compiled_run_contract#/state_enums",
                }
        else:
            previous_scene = scene_ids[scene_index - 1]
            previous = ledger_winners[previous_scene]
            prior[scene_id] = copy.deepcopy(current[previous_scene])
            prior_source = {
                "source_record_id": previous["source_record_id"],
                "source_version": previous["source_version"],
                "canonical_owner": previous["canonical_owner"],
                "ledger_sequence": previous["ledger_sequence"],
                "pointer_prefix": f"run_local_state_ledger_records#/{previous_scene}/state_snapshot",
            }
        for dimension in dimensions:
            trace.append({
                "field": "relevant_prior_state", "scene": scene_id, "property": dimension,
                "source_contract_pointer": f"{prior_source['pointer_prefix']}/{dimension}",
                "source_version": prior_source["source_version"], "canonical_owner": prior_source["canonical_owner"],
                "source_record_id": prior_source["source_record_id"], "ledger_sequence": prior_source["ledger_sequence"],
                "type_source": f"compiled_run_contract#/strict_schema/scene_packages/state/properties/{dimension}/type",
                "enum_source": f"compiled_run_contract#/state_enums/{dimension}",
                "requiredness_source": "Repair09J relevant_prior_state per-scene closure",
                "projection_rule": "COMPILED_INITIAL_OR_PREVIOUS_VALIDATED_SCENE",
            })
            trace.append({
                "field": "current_state", "scene": scene_id, "property": dimension,
                "source_contract_pointer": f"run_local_state_ledger_records#/{scene_id}/state_snapshot/{dimension}",
                "source_version": winner["source_version"], "canonical_owner": winner["canonical_owner"],
                "source_record_id": winner["source_record_id"], "ledger_sequence": winner["ledger_sequence"],
                "type_source": f"compiled_run_contract#/strict_schema/scene_packages/state/properties/{dimension}/type",
                "enum_source": f"compiled_run_contract#/state_enums/{dimension}",
                "requiredness_source": "Repair09J current_state per-scene closure",
                "projection_rule": "OWNER_LIFECYCLE_LEDGER_SEQUENCE_WINNER",
            })

    exact_absent = {"const": ABSENT}
    if prior_absence_authority is not None:
        if not isinstance(prior_absence_authority, Mapping) or set(prior_absence_authority) != PRIOR_ABSENCE_AUTHORITY_FIELDS or prior_absence_authority.get("decision") != "AUTHORIZED_WHOLE_SCOPE_ABSENCE":
            raise DirectorStateObjectContractError("prior absence requires an exact closed source authority record")
        if any(not isinstance(prior_absence_authority[field], str) or not prior_absence_authority[field] for field in PRIOR_ABSENCE_AUTHORITY_FIELDS):
            raise DirectorStateObjectContractError("prior absence source authority fields must be non-empty strings")
        prior = ABSENT
        relevant_schema = copy.deepcopy(exact_absent)
        trace = [item for item in trace if item["field"] != "relevant_prior_state"]
        trace.append({
            "field": "relevant_prior_state", "scene": ABSENT, "property": ABSENT,
            "source_contract_pointer": prior_absence_authority["source_contract_pointer"],
            "source_version": prior_absence_authority["source_version"], "canonical_owner": prior_absence_authority["canonical_owner"],
            "source_record_id": prior_absence_authority["source_record_id"], "ledger_sequence": 0, "type_source": "Repair09J exact ABSENT",
            "enum_source": "State Evidence ABSENT", "requiredness_source": "Repair09J absence closure",
            "projection_rule": "AUTHORIZED_WHOLE_SCOPE_ABSENCE",
        })
    else:
        relevant_schema = _scene_object_schema(compiled, state_schema)

    for field in EXACT_ABSENT_FIELDS:
        trace.append({
            "field": field, "scene": ABSENT, "property": ABSENT,
            "source_contract_pointer": f"Repair09J#/{field}/exact_absent",
            "source_version": authority["authority_bundle_hash"], "canonical_owner": "Repair 09J Authority",
            "source_record_id": ABSENT, "ledger_sequence": 0, "type_source": "State Evidence ABSENT",
            "enum_source": "State Evidence ABSENT", "requiredness_source": f"Repair09J {field} closure",
            "projection_rule": "NO_AUTHORIZED_PROJECTABLE_CONTENT",
        })

    schemas = {
        "relevant_prior_state": relevant_schema,
        "current_state": _scene_object_schema(compiled, state_schema),
        **{field: copy.deepcopy(exact_absent) for field in EXACT_ABSENT_FIELDS},
    }
    expected = {
        "relevant_prior_state": prior,
        "current_state": current,
        **{field: ABSENT for field in EXACT_ABSENT_FIELDS},
    }
    bundle = {
        "compiler_id": COMPILER_ID,
        "authority": authority,
        "compiled_contract_hash": compiled_hash,
        "validated_upstream_records_hash": stable_hash(list(validated_upstream_state_records)),
        "run_local_ledger_records_hash": stable_hash(list(run_local_state_ledger_records)),
        "fixture_id": compiled["fixture"]["fixture_id"],
        "scene_ids": scene_ids,
        "state_dimensions": dimensions,
        "state_schemas": schemas,
        "expected_state_values": expected,
        "source_trace": trace,
        "required_locks_hash": stable_hash(list(required_locks)),
        "transition_authority_hash": stable_hash(list(transition_authority_records)),
        "downstream_representation": "JSON_OBJECT_OR_EXACT_ABSENT",
        "legacy_string_path": "UNREACHABLE",
    }
    bundle["state_schema_hash"] = stable_hash(schemas)
    bundle["source_trace_hash"] = stable_hash(trace)
    bundle["bundle_hash"] = stable_hash({key: value for key, value in bundle.items() if key != "bundle_hash"})
    return bundle


def validate_director_state_values(state_evidence: Mapping[str, Any], contract: Mapping[str, Any]) -> Dict[str, Any]:
    if not isinstance(state_evidence, Mapping):
        raise DirectorStateObjectContractError("Director state_evidence must be an object")
    expected = contract.get("expected_state_values")
    schemas = contract.get("state_schemas")
    if not isinstance(expected, Mapping) or not isinstance(schemas, Mapping):
        raise DirectorStateObjectContractError("compiled Director state contract is incomplete")
    for field in (*DYNAMIC_FIELDS, *EXACT_ABSENT_FIELDS):
        if field not in state_evidence:
            raise DirectorStateObjectContractError(f"Director state field is missing: {field}")
        value = state_evidence[field]
        if field in EXACT_ABSENT_FIELDS:
            if value != ABSENT:
                raise DirectorStateObjectContractError(f"Director state_evidence.{field} must be exact ABSENT")
            continue
        schema = schemas[field]
        if schema == {"const": ABSENT}:
            if value != ABSENT:
                raise DirectorStateObjectContractError(f"Director state_evidence.{field} must be exact ABSENT")
        else:
            if not isinstance(value, Mapping) or set(value) != set(schema["required"]):
                raise DirectorStateObjectContractError(f"Director state_evidence.{field} has wrong scene keys")
            for scene_id, scene_schema in schema["properties"].items():
                scene_value = value[scene_id]
                if not isinstance(scene_value, Mapping) or set(scene_value) != set(scene_schema["required"]):
                    raise DirectorStateObjectContractError(f"Director state_evidence.{field}.{scene_id} has wrong state dimensions")
                for dimension, property_schema in scene_schema["properties"].items():
                    if scene_value[dimension] not in property_schema["enum"]:
                        raise DirectorStateObjectContractError(f"Director state_evidence.{field}.{scene_id}.{dimension} is outside its enum")
        if value != expected[field]:
            raise DirectorStateObjectContractError(f"Director state_evidence.{field} does not match its source projection")
    trace = contract.get("source_trace")
    if not isinstance(trace, list) or not trace or stable_hash(trace) != contract.get("source_trace_hash"):
        raise DirectorStateObjectContractError("Director state source trace is missing or invalid")
    for item in trace:
        if not isinstance(item, Mapping) or set(item) != TRACE_FIELDS:
            raise DirectorStateObjectContractError("Director state source trace item is incomplete")
        for field in TRACE_FIELDS - {"ledger_sequence"}:
            if not isinstance(item[field], str) or not item[field]:
                raise DirectorStateObjectContractError(f"Director state source trace {field} is invalid")
        if not isinstance(item["ledger_sequence"], int) or item["ledger_sequence"] < 0:
            raise DirectorStateObjectContractError("Director state source trace ledger_sequence is invalid")
    observed = {(item["field"], item["scene"], item["property"]) for item in trace}
    for dynamic_field in DYNAMIC_FIELDS:
        if schemas[dynamic_field] == {"const": ABSENT}:
            if (dynamic_field, ABSENT, ABSENT) not in observed:
                raise DirectorStateObjectContractError(f"Director state source trace lacks {dynamic_field} absence authority")
        else:
            for scene_id in contract.get("scene_ids", []):
                for dimension in contract.get("state_dimensions", []):
                    if (dynamic_field, scene_id, dimension) not in observed:
                        raise DirectorStateObjectContractError(f"Director state source trace lacks {dynamic_field}.{scene_id}.{dimension}")
    for absent_field in EXACT_ABSENT_FIELDS:
        if (absent_field, ABSENT, ABSENT) not in observed:
            raise DirectorStateObjectContractError(f"Director state source trace lacks {absent_field} absence authority")
    return copy.deepcopy(dict(state_evidence))


def lint_deepseek_strict_schema(schema: Mapping[str, Any]) -> Dict[str, Any]:
    unsupported: list[str] = []
    invalid: list[str] = []

    def walk(node: Any, path: str) -> None:
        if isinstance(node, Mapping):
            for key in ("const", "minLength", "maxLength", "minItems", "maxItems"):
                if key in node:
                    unsupported.append(f"{path}/{key}")
            if "enum" in node and node.get("type") != "string":
                invalid.append(f"{path}:enum_without_string_type")
            if node.get("type") == "object":
                properties = node.get("properties")
                required = node.get("required")
                if not isinstance(properties, Mapping) or not isinstance(required, list) or set(properties) != set(required) or node.get("additionalProperties") is not False:
                    invalid.append(f"{path}:object_not_closed")
                else:
                    for key, child in properties.items():
                        walk(child, f"{path}/properties/{key}")
            if "anyOf" in node:
                branches = node["anyOf"]
                if not isinstance(branches, list) or not branches:
                    invalid.append(f"{path}:empty_anyOf")
                else:
                    for index, child in enumerate(branches):
                        walk(child, f"{path}/anyOf/{index}")
            if "items" in node:
                walk(node["items"], f"{path}/items")
            if "$ref" in node and not isinstance(node["$ref"], str):
                invalid.append(f"{path}:invalid_ref")
        elif isinstance(node, list):
            for index, child in enumerate(node):
                walk(child, f"{path}/{index}")

    walk(schema, "")
    if unsupported or invalid:
        raise DirectorStateObjectContractError(f"DeepSeek strict schema lint failed: unsupported={unsupported}; invalid={invalid}")
    return {"result": "PASS", "unsupported_paths": [], "invalid_paths": [], "schema_hash": stable_hash(schema)}
