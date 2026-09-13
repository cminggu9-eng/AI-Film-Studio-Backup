"""Per-run Scene Writer state-field projection.

The compiled run contract owns field identity, token identity, entity identity,
and transition identity.  No token spelling or story literal is inspected to
infer ownership.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any, Mapping, Sequence


STATE_FIELD_CONTRACT_VERSION = "0.1"


class StateFieldContractError(RuntimeError):
    """The compiled run contract cannot produce one active state projection."""


def _stable_hash(value: Mapping[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def build_scene_writer_state_projection(compiled_run_contract: Mapping[str, Any]) -> dict[str, Any]:
    """Project the one active compact Scene Writer state dimension for a run."""

    if not isinstance(compiled_run_contract, Mapping):
        raise StateFieldContractError("compiled run contract is required")
    fixture = compiled_run_contract.get("fixture")
    if not isinstance(fixture, Mapping):
        raise StateFieldContractError("compiled fixture is required")
    binding_id = fixture.get("fixture_id")
    dimensions = fixture.get("state_dimensions")
    transitions = fixture.get("authorized_transitions")
    entities = compiled_run_contract.get("tracked_entity_ids")
    if not isinstance(binding_id, str) or not binding_id.strip():
        raise StateFieldContractError("compiled binding identity is required")
    if not isinstance(dimensions, Sequence) or isinstance(dimensions, (str, bytes)) or len(dimensions) != 1:
        raise StateFieldContractError("compact Scene Writer transport requires exactly one compiled state dimension")
    dimension = dimensions[0]
    if not isinstance(dimension, Mapping):
        raise StateFieldContractError("compiled state dimension is invalid")
    field_name = dimension.get("dimension")
    tokens = dimension.get("allowed_tokens")
    if not isinstance(field_name, str) or not field_name.strip():
        raise StateFieldContractError("compiled state-field identity is required")
    if not isinstance(tokens, Sequence) or isinstance(tokens, (str, bytes)) or len(tokens) < 2:
        raise StateFieldContractError("compiled state token domain is required")
    allowed = list(tokens)
    if not all(isinstance(token, str) and token.strip() for token in allowed) or len(set(allowed)) != len(allowed):
        raise StateFieldContractError("compiled state tokens must be unique non-empty strings")
    state_enums = compiled_run_contract.get("state_enums")
    if not isinstance(state_enums, Mapping) or state_enums.get(field_name) != allowed:
        raise StateFieldContractError("compiled state dimension and state_enums disagree")
    if not isinstance(transitions, Sequence) or isinstance(transitions, (str, bytes)) or not transitions:
        raise StateFieldContractError("compiled transition authority is required")
    authorized = list(transitions)
    if not all(isinstance(item, str) and item.strip() for item in authorized) or len(set(authorized)) != len(authorized):
        raise StateFieldContractError("compiled transition tokens must be unique non-empty strings")
    if not isinstance(entities, Sequence) or isinstance(entities, (str, bytes)) or not entities:
        raise StateFieldContractError("compiled tracked entity identity is required")
    tracked = list(entities)
    if not all(isinstance(item, str) and item.strip() for item in tracked):
        raise StateFieldContractError("compiled tracked entity identities are invalid")
    projection = {
        "contract_version": STATE_FIELD_CONTRACT_VERSION,
        "binding_id": binding_id,
        "state_dimension_id": field_name,
        "transport_field_name": field_name,
        "allowed_machine_tokens": allowed,
        "initial_token": allowed[0],
        "authorized_transitions": authorized,
        "tracked_entity_ids": tracked,
        "source_owner": "compiled_run_contract",
        "state_dimension_source_pointer": "compiled_run_contract#/fixture/state_dimensions/0",
        "state_enum_source_pointer": f"compiled_run_contract#/state_enums/{field_name}",
        "transition_source_pointer": "compiled_run_contract#/fixture/authorized_transitions",
        "binding_source_pointer": "compiled_run_contract#/fixture/fixture_id",
    }
    projection["contract_hash"] = _stable_hash(projection)
    return projection


def state_field_name(projection: Mapping[str, Any]) -> str:
    field = projection.get("transport_field_name") if isinstance(projection, Mapping) else None
    if not isinstance(field, str) or not field.strip() or field != projection.get("state_dimension_id"):
        raise StateFieldContractError("state projection field identity is invalid")
    return field


def allowed_machine_tokens(projection: Mapping[str, Any]) -> list[str]:
    values = projection.get("allowed_machine_tokens") if isinstance(projection, Mapping) else None
    if not isinstance(values, Sequence) or isinstance(values, (str, bytes)):
        raise StateFieldContractError("state projection token domain is invalid")
    tokens = list(values)
    if not tokens or not all(isinstance(item, str) and item.strip() for item in tokens) or len(set(tokens)) != len(tokens):
        raise StateFieldContractError("state projection token domain is invalid")
    return tokens


def authorized_transition_tokens(projection: Mapping[str, Any]) -> list[str]:
    values = projection.get("authorized_transitions") if isinstance(projection, Mapping) else None
    if not isinstance(values, Sequence) or isinstance(values, (str, bytes)):
        raise StateFieldContractError("state projection transition domain is invalid")
    transitions = list(values)
    if not transitions or not all(isinstance(item, str) and item.strip() for item in transitions):
        raise StateFieldContractError("state projection transition domain is invalid")
    return transitions


def tracked_entity_ids(projection: Mapping[str, Any]) -> list[str]:
    values = projection.get("tracked_entity_ids") if isinstance(projection, Mapping) else None
    if not isinstance(values, Sequence) or isinstance(values, (str, bytes)):
        raise StateFieldContractError("state projection entity domain is invalid")
    entities = list(values)
    if not entities or not all(isinstance(item, str) and item.strip() for item in entities):
        raise StateFieldContractError("state projection entity domain is invalid")
    return entities


def validate_machine_state_token(token: Any, projection: Mapping[str, Any]) -> str:
    if token not in allowed_machine_tokens(projection):
        raise StateFieldContractError("machine state token is outside the compiled current-run domain")
    return token
