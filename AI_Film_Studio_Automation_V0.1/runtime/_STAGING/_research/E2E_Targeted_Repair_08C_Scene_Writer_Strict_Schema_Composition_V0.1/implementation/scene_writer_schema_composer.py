"""Compose generic compact transport with one compiled fixture contract."""
from __future__ import annotations
import copy
from typing import Any, Mapping
from scene_writer_strict_transport import strict_function_schema, StrictTransportSchemaError
from scene_writer_scene_id_contract import build_scene_id_contract, ordered_scene_ids
from scene_writer_state_field_contract import build_scene_writer_state_projection

def generic_compact_envelope() -> dict[str, Any]:
    return copy.deepcopy(strict_function_schema())

def compose(
    compiled: Mapping[str,Any],
    *,
    scene_id_contract: Mapping[str, Any] | None = None,
    state_field_contract: Mapping[str, Any] | None = None,
) -> dict[str,Any]:
    if not isinstance(compiled.get('strict_schema'),Mapping) or not isinstance(compiled.get('fixture'),Mapping):
        raise StrictTransportSchemaError('compiled fixture contract is required')
    projection = build_scene_id_contract(compiled) if scene_id_contract is None else scene_id_contract
    state_projection = build_scene_writer_state_projection(compiled) if state_field_contract is None else state_field_contract
    return strict_function_schema(projection, state_projection)
