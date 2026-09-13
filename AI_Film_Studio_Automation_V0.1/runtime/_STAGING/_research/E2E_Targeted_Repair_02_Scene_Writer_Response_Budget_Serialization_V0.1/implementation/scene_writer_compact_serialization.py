"""Lossless compact transport form for the existing Scene Writer integration contract."""

from __future__ import annotations

import copy
import json
from typing import Any, Dict, Mapping, Sequence

from scene_writer_integration_contract import CONTRACT_VERSION, STRUCTURAL_FIELD_NAMES
from scene_writer_scene_id_contract import ordered_scene_ids
from scene_writer_state_field_contract import (
    StateFieldContractError,
    authorized_transition_tokens,
    state_field_name,
    tracked_entity_ids,
    validate_machine_state_token,
)


COMPACT_FORMAT = "scene-writer-integration-compact-v0.1"
COMPACT_TOP_LEVEL_FIELDS = {"format", "control", "state", "scenes"}
COMPACT_CONTROL_FIELDS = {"outcome", "flags", "handoffs", "required_outcome", "unresolved_decisions"}
COMPACT_TOP_STATE_FIELDS = {"prior", "current", "proposed", "knowledge_timing", "relationship", "visual"}
COMPACT_SCENE_FIELDS = {"id", "content", "structural", "state"}
COMPACT_SCENE_STATE_BASE_FIELDS = {
    "entity_id",
    "custody",
    "holders",
    "reveal",
    "relationship",
    "state_display",
    "location",
    "transitions",
}

SCENE_CONTENT_MAX_CHARS = 420
STRUCTURAL_VALUE_MAX_CHARS = 96
STATE_TEXT_MAX_CHARS = 160
TOP_STATE_VALUE_MAX_CHARS = 360


class CompactSerializationError(RuntimeError):
    """The compact transport is malformed or exceeds its declared safe shape."""


def _require_exact_mapping(value: Any, fields: set[str], path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping) or set(value) != fields:
        raise CompactSerializationError(f"{path} field set is invalid")
    return value


def _require_text(value: Any, path: str, maximum: int) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise CompactSerializationError(f"{path} must be non-empty text at most {maximum} characters")
    return value


def _json_size(value: Any) -> int:
    return len(json.dumps(value, ensure_ascii=False, separators=(",", ":")))


def compact_scene_state_fields(state_field_contract: Mapping[str, Any]) -> set[str]:
    """Return the exact current-run compact state field set."""

    return COMPACT_SCENE_STATE_BASE_FIELDS | {state_field_name(state_field_contract)}


def compact_scene_writer_output_schema(state_field_contract: Mapping[str, Any]) -> Dict[str, Any]:
    """Prompt schema only; normalized output remains the frozen contract shape."""

    return {
        "format": COMPACT_FORMAT,
        "control": {
            "outcome": "one exact Scene Writer primary state token",
            "flags": "ABSENT or canonical list",
            "handoffs": "ABSENT or canonical list",
            "required_outcome": "string or ABSENT",
            "unresolved_decisions": "list of strings or ABSENT",
        },
        "state": {
            "prior": "object or ABSENT, at most 360 serialized characters",
            "current": "object or ABSENT, at most 360 serialized characters",
            "proposed": "object or ABSENT, at most 360 serialized characters",
            "knowledge_timing": "object or ABSENT, at most 360 serialized characters",
            "relationship": "object or ABSENT, at most 360 serialized characters",
            "visual": "object or ABSENT, at most 360 serialized characters",
        },
        "scenes": [
            {
                "id": "one exact full token from the compiled current-run scene-id contract, in order",
                "content": "normal zh-CN playable scene material, at most 420 characters",
                "structural": {name: "minimum sufficient zh-CN evidence, at most 96 characters" for name in STRUCTURAL_FIELD_NAMES},
                "state": {
                    "entity_id": tracked_entity_ids(state_field_contract),
                    "custody": "traceable zh-CN custody text, at most 160 characters",
                    "holders": ["zh-CN character names"],
                    "reveal": "NOT_YET_REVEALED or REVEALED_WITH_EVENT",
                    "relationship": "zh-CN state text, at most 160 characters",
                    state_field_name(state_field_contract): {
                        "allowed_machine_tokens": list(state_field_contract["allowed_machine_tokens"]),
                        "source": state_field_contract["state_enum_source_pointer"],
                    },
                    "state_display": "zh-CN display prose, at most 160 characters",
                    "location": "zh-CN presence text, at most 160 characters",
                    "transitions": authorized_transition_tokens(state_field_contract),
                },
            }
        ],
    }


def is_compact_scene_writer_output(value: Any) -> bool:
    return isinstance(value, Mapping) and value.get("format") == COMPACT_FORMAT


def normalize_compact_scene_writer_output(
    value: Any,
    *,
    run_id: str,
    required_locks: Sequence[str] | None,
    prohibited_changes: Sequence[str] | None,
    scene_id_contract: Mapping[str, Any],
    state_field_contract: Mapping[str, Any],
) -> Dict[str, Any]:
    """Expand transport aliases only; no creative or state-bearing value is rewritten."""

    top = _require_exact_mapping(value, COMPACT_TOP_LEVEL_FIELDS, "compact response")
    if top.get("format") != COMPACT_FORMAT:
        raise CompactSerializationError("compact response format is invalid")
    control = _require_exact_mapping(top.get("control"), COMPACT_CONTROL_FIELDS, "control")
    state = _require_exact_mapping(top.get("state"), COMPACT_TOP_STATE_FIELDS, "state")
    if not isinstance(required_locks, Sequence) or isinstance(required_locks, (str, bytes)) or not all(isinstance(item, str) and item.strip() for item in required_locks):
        raise CompactSerializationError("immutable required locks are unavailable for hydration")
    if not isinstance(prohibited_changes, Sequence) or isinstance(prohibited_changes, (str, bytes)) or not all(isinstance(item, str) and item.strip() for item in prohibited_changes):
        raise CompactSerializationError("immutable prohibited changes are unavailable for hydration")
    for field, item in state.items():
        if item is None or _json_size(item) > TOP_STATE_VALUE_MAX_CHARS:
            raise CompactSerializationError(f"state.{field} is absent or exceeds compact bound")
    expected_scene_ids = ordered_scene_ids(scene_id_contract)
    current_state_field = state_field_name(state_field_contract)
    current_state_fields = compact_scene_state_fields(state_field_contract)
    current_entities = tracked_entity_ids(state_field_contract)
    current_transitions = authorized_transition_tokens(state_field_contract)
    scenes = top.get("scenes")
    if not isinstance(scenes, list) or len(scenes) != len(expected_scene_ids):
        raise CompactSerializationError("scenes must contain exactly the compiled scene-id count")

    normalized_scenes = []
    for index, scene_id in enumerate(expected_scene_ids):
        compact_scene = _require_exact_mapping(scenes[index], COMPACT_SCENE_FIELDS, f"scenes[{index}]")
        if compact_scene.get("id") != scene_id:
            raise CompactSerializationError(f"scenes[{index}].id is not the exact compiled current-run scene ID")
        content = _require_text(compact_scene.get("content"), f"scenes[{index}].content", SCENE_CONTENT_MAX_CHARS)
        structural = _require_exact_mapping(compact_scene.get("structural"), set(STRUCTURAL_FIELD_NAMES), f"scenes[{index}].structural")
        for name in STRUCTURAL_FIELD_NAMES:
            _require_text(structural.get(name), f"scenes[{index}].structural.{name}", STRUCTURAL_VALUE_MAX_CHARS)
        compact_state = _require_exact_mapping(compact_scene.get("state"), current_state_fields, f"scenes[{index}].state")
        for field in ("entity_id", "custody", "reveal", "relationship", current_state_field, "state_display", "location"):
            _require_text(compact_state.get(field), f"scenes[{index}].state.{field}", STATE_TEXT_MAX_CHARS)
        holders = compact_state.get("holders")
        transitions = compact_state.get("transitions")
        if not isinstance(holders, list) or not all(isinstance(item, str) and item.strip() for item in holders):
            raise CompactSerializationError(f"scenes[{index}].state.holders is invalid")
        if not isinstance(transitions, list) or not all(isinstance(item, str) and item.strip() for item in transitions):
            raise CompactSerializationError(f"scenes[{index}].state.transitions is invalid")
        if compact_state["entity_id"] not in current_entities:
            raise CompactSerializationError(f"scenes[{index}].state.entity_id is outside the compiled current-run domain")
        try:
            validate_machine_state_token(compact_state[current_state_field], state_field_contract)
        except StateFieldContractError as exc:
            raise CompactSerializationError(f"scenes[{index}].state.{current_state_field} is invalid") from exc
        if any(item not in current_transitions for item in transitions):
            raise CompactSerializationError(f"scenes[{index}].state.transitions contains a foreign transition")
        locator = f"scene_packages/{scene_id}"
        normalized_scenes.append(
            {
                "scene_id": scene_id,
                "content": copy.deepcopy(content),
                "structural_deliverable": copy.deepcopy(dict(structural)),
                "state_evidence": {
                    "entity_identity": copy.deepcopy(compact_state["entity_id"]),
                    "entity_custody": copy.deepcopy(compact_state["custody"]),
                    "knowledge_holders": copy.deepcopy(holders),
                    "reveal_status": copy.deepcopy(compact_state["reveal"]),
                    "relationship_state": copy.deepcopy(compact_state["relationship"]),
                    current_state_field: copy.deepcopy(compact_state[current_state_field]),
                    "machine_state_display": copy.deepcopy(compact_state["state_display"]),
                    "location_presence": copy.deepcopy(compact_state["location"]),
                    "authorized_transitions": copy.deepcopy(transitions),
                },
                "source_attribution": {
                    "source_role": "Scene Writer",
                    "source_record_id": f"{run_id}/scene_writer/{scene_id}",
                    "version": CONTRACT_VERSION,
                    "evidence_locator": locator,
                },
                "evidence_locator": locator,
            }
        )

    return {
        "primary_state_or_outcome": copy.deepcopy(control["outcome"]),
        "flags": copy.deepcopy(control["flags"]),
        "handoffs": copy.deepcopy(control["handoffs"]),
        "canon_assignment_locks": copy.deepcopy(list(required_locks)),
        "prohibited_changes": copy.deepcopy(list(prohibited_changes)),
        "required_outcome": copy.deepcopy(control["required_outcome"]),
        "unresolved_decisions": copy.deepcopy(control["unresolved_decisions"]),
        "state_evidence": {
            "relevant_prior_state": copy.deepcopy(state["prior"]),
            "current_state": copy.deepcopy(state["current"]),
            "proposed_state": copy.deepcopy(state["proposed"]),
            "knowledge_timing": copy.deepcopy(state["knowledge_timing"]),
            "relationship_state": copy.deepcopy(state["relationship"]),
            "visual_state": copy.deepcopy(state["visual"]),
        },
        "content": "\n\n".join(f"场景 {index}\n{scene['content']}" for index, scene in enumerate(normalized_scenes, start=1)),
        "scene_packages": normalized_scenes,
    }
