"""Binding-derived ENTRY/EXIT state snapshot projection for Semantic Safeguard.

This module adds phase selection to Integration evidence only.  It neither
creates story-state tokens nor changes transition authority: state dimensions,
tokens, and occurrence decisions remain owned by the compiled run contract and
the Shared Transition Authority Projection.
"""

from __future__ import annotations

import copy
import hashlib
import json
from typing import Any, Dict, Mapping, Sequence

from .semantic_alignment import (
    SemanticAlignmentContractError,
    build_shared_transition_authority_projection,
    classify_transition_evidence,
)


SNAPSHOT_PHASES = ("ENTRY", "EXIT")
SNAPSHOT_TRACE_FIELDS = (
    "scene_id",
    "state_dimension",
    "phase",
    "value",
    "source_artifact",
    "source_version",
    "canonical_owner",
    "evidence_pointer",
    "source_kind",
    "source_binding_id",
)
PHASE_ASSERTION_VALUE_FIELDS = (
    "snapshot_contract",
    "required_phase",
    "selected_value",
    "selected_snapshot",
    "projection_hash",
)


class StatePhaseContractError(ValueError):
    """Raised when phase-scoped state evidence is missing or contradictory."""


def _stable_hash(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _require_text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise StatePhaseContractError(f"{field} is required")
    return value


def _fixture(contract: Mapping[str, Any]) -> Mapping[str, Any]:
    if not isinstance(contract, Mapping) or not isinstance(contract.get("fixture"), Mapping):
        raise StatePhaseContractError("compiled_run_contract.fixture is required")
    fixture = contract["fixture"]
    _require_text(fixture.get("fixture_id"), "fixture_id")
    return fixture


def _snapshot(
    *,
    scene_id: str,
    dimension: str,
    phase: str,
    value: Any,
    source_artifact: str,
    source_version: str,
    canonical_owner: str,
    evidence_pointer: str,
    source_kind: str,
    source_binding_id: str,
) -> Dict[str, Any]:
    if phase not in SNAPSHOT_PHASES:
        raise StatePhaseContractError("unsupported snapshot phase")
    return {
        "scene_id": _require_text(scene_id, "scene_id"),
        "state_dimension": _require_text(dimension, "state_dimension"),
        "phase": phase,
        "value": copy.deepcopy(value),
        "source_artifact": _require_text(source_artifact, "source_artifact"),
        "source_version": _require_text(source_version, "source_version"),
        "canonical_owner": _require_text(canonical_owner, "canonical_owner"),
        "evidence_pointer": _require_text(evidence_pointer, "evidence_pointer"),
        "source_kind": _require_text(source_kind, "source_kind"),
        "source_binding_id": _require_text(source_binding_id, "source_binding_id"),
    }


def _validate_snapshot(snapshot: Any) -> Dict[str, Any]:
    if not isinstance(snapshot, Mapping) or set(snapshot) != set(SNAPSHOT_TRACE_FIELDS):
        raise StatePhaseContractError("phase snapshot must contain the exact trace fields")
    copied = copy.deepcopy(dict(snapshot))
    if copied["phase"] not in SNAPSHOT_PHASES:
        raise StatePhaseContractError("phase snapshot has an unsupported phase")
    for field in SNAPSHOT_TRACE_FIELDS:
        if field == "value":
            continue
        _require_text(copied[field], field)
    return copied


def build_state_phase_projection(
    compiled_run_contract: Mapping[str, Any],
    scenes: Sequence[Mapping[str, Any]],
    *,
    source_artifact: str,
    source_version: str,
    canonical_owner: str,
) -> Dict[str, Any]:
    """Project validated scene evidence into attributable ENTRY and EXIT snapshots.

    First-scene ENTRY values originate only from the compiled initial token.
    Subsequent ENTRY values originate only from the previous scene EXIT value.
    EXIT values are scene-local validated output, and a value change is accepted
    only when the existing Shared Transition Authority says it actually occurred.
    """

    fixture = _fixture(compiled_run_contract)
    fixture_id = _require_text(fixture.get("fixture_id"), "fixture_id")
    dimensions = fixture.get("state_dimensions")
    scene_ids = compiled_run_contract.get("scene_ids") if isinstance(compiled_run_contract, Mapping) else None
    if not isinstance(dimensions, list) or not dimensions or not isinstance(scene_ids, list) or len(scene_ids) != len(scenes):
        raise StatePhaseContractError("current binding state dimensions and exact scene sequence are required")
    if [scene.get("scene_id") if isinstance(scene, Mapping) else None for scene in scenes] != scene_ids:
        raise StatePhaseContractError("scene evidence must use the current compiled scene ID sequence")

    try:
        transition_projection = build_shared_transition_authority_projection(compiled_run_contract)
        transition_classification = classify_transition_evidence(transition_projection, scenes, handed_off=False)
    except SemanticAlignmentContractError as exc:
        raise StatePhaseContractError(str(exc)) from exc

    transition_records = transition_projection.get("records")
    if not isinstance(transition_records, list) or len(transition_records) != len(dimensions):
        raise StatePhaseContractError("state dimensions require unambiguous transition authority records")
    occurrences = {
        item.get("scene_index")
        for item in transition_classification.get("occurrence_evidence", [])
        if isinstance(item, Mapping)
    }

    dimension_records: list[Dict[str, Any]] = []
    for dimension_index, (dimension_record, transition_record) in enumerate(zip(dimensions, transition_records)):
        if not isinstance(dimension_record, Mapping) or not isinstance(transition_record, Mapping):
            raise StatePhaseContractError("state dimension and transition records must be objects")
        dimension = _require_text(dimension_record.get("dimension"), "state dimension")
        tokens = dimension_record.get("allowed_tokens")
        if not isinstance(tokens, list) or len(tokens) != 2 or not all(isinstance(token, str) and token for token in tokens):
            raise StatePhaseContractError("state dimension must retain its compiled two-token domain")
        if transition_record.get("state_dimension") != dimension:
            raise StatePhaseContractError("state dimension to transition authority association is inconsistent")
        from_state, to_state = tokens
        previous_exit: Dict[str, Any] | None = None
        scene_records: list[Dict[str, Any]] = []
        for scene_index, scene in enumerate(scenes, start=1):
            if not isinstance(scene, Mapping) or not isinstance(scene.get("state_evidence"), Mapping):
                raise StatePhaseContractError("scene-local state_evidence is required")
            scene_id = _require_text(scene.get("scene_id"), "scene_id")
            exit_value = scene["state_evidence"].get(dimension)
            if exit_value not in tokens:
                raise StatePhaseContractError("scene exit state is outside the compiled token domain")
            locator = _require_text(scene.get("evidence_locator"), "scene-local evidence locator")
            if previous_exit is None:
                entry = _snapshot(
                    scene_id=scene_id,
                    dimension=dimension,
                    phase="ENTRY",
                    value=from_state,
                    source_artifact="compiled_run_contract",
                    source_version="COMPILED_RUN_CONTRACT_V0.1",
                    canonical_owner="Fixture Binding / Compiled Run Contract",
                    evidence_pointer=f"compiled_run_contract#/fixture/state_dimensions/{dimension_index}/allowed_tokens/0",
                    source_kind="COMPILED_INITIAL_STATE",
                    source_binding_id=fixture_id,
                )
            else:
                entry = _snapshot(
                    scene_id=scene_id,
                    dimension=dimension,
                    phase="ENTRY",
                    value=previous_exit["value"],
                    source_artifact=previous_exit["source_artifact"],
                    source_version=previous_exit["source_version"],
                    canonical_owner=previous_exit["canonical_owner"],
                    evidence_pointer=previous_exit["evidence_pointer"],
                    source_kind="PREVIOUS_SCENE_EXIT",
                    source_binding_id=fixture_id,
                )
            exit_snapshot = _snapshot(
                scene_id=scene_id,
                dimension=dimension,
                phase="EXIT",
                value=exit_value,
                source_artifact=source_artifact,
                source_version=source_version,
                canonical_owner=canonical_owner,
                evidence_pointer=f"{locator}/state_evidence/{dimension}",
                source_kind="SCENE_EXIT_VALIDATED_EVIDENCE",
                source_binding_id=fixture_id,
            )
            changed = entry["value"] != exit_snapshot["value"]
            occurrence_here = scene_index in occurrences
            if changed and not (occurrence_here and entry["value"] == from_state and exit_snapshot["value"] == to_state):
                raise StatePhaseContractError("scene exit state changes without an occurred transition")
            if occurrence_here and not changed:
                raise StatePhaseContractError("occurred transition did not advance the scene exit state")
            scene_records.append(
                {
                    "scene_id": scene_id,
                    "entry": entry,
                    "exit": exit_snapshot,
                    "occurred_transition_applied": occurrence_here,
                }
            )
            previous_exit = exit_snapshot
        dimension_records.append(
            {
                "state_dimension": dimension,
                "compiled_token_domain": copy.deepcopy(tokens),
                "records": scene_records,
            }
        )

    core = {
        "projection_type": "STATE_PHASE_SNAPSHOT_PROJECTION",
        "source_binding_id": fixture_id,
        "source_contract_pointer": "compiled_run_contract#/fixture/state_dimensions+scene_ids",
        "phases": list(SNAPSHOT_PHASES),
        "transition_application_rule": "ENTRY_APPLY_OCCURRED_TRANSITIONS_ONLY_EXIT",
        "state_dimensions": dimension_records,
        "shared_transition_classification": copy.deepcopy(transition_classification),
        "ledger_semantics": "SCENE_LEDGER_STATE_SNAPSHOT_IS_EXIT_POST_STATE",
    }
    return {**core, "projection_hash": _stable_hash(core)}


def resolve_state_phase_snapshot(
    projection: Mapping[str, Any],
    *,
    scene_id: str,
    state_dimension: str,
    phase: str,
) -> Dict[str, Any]:
    """Resolve one exact phase snapshot; unavailable evidence fails closed."""

    if phase not in SNAPSHOT_PHASES:
        raise StatePhaseContractError("required phase is unsupported")
    matches: list[Dict[str, Any]] = []
    for dimension_record in projection.get("state_dimensions", []):
        if not isinstance(dimension_record, Mapping) or dimension_record.get("state_dimension") != state_dimension:
            continue
        for record in dimension_record.get("records", []):
            if isinstance(record, Mapping) and record.get("scene_id") == scene_id and isinstance(record.get(phase.lower()), Mapping):
                matches.append(_validate_snapshot(record[phase.lower()]))
    if len(matches) != 1:
        raise StatePhaseContractError("required state phase snapshot is missing or ambiguous")
    return matches[0]


def build_phase_scoped_required_state_value(
    projection: Mapping[str, Any],
    *,
    scene_id: str,
    state_dimension: str,
    required_phase: str,
) -> Dict[str, Any]:
    """Bind a REQUIRED_STATE comparison to one attributable snapshot phase."""

    selected = resolve_state_phase_snapshot(
        projection,
        scene_id=scene_id,
        state_dimension=state_dimension,
        phase=required_phase,
    )
    return {
        "snapshot_contract": "STATE_PHASE_SNAPSHOT_V0.1",
        "required_phase": required_phase,
        "selected_value": copy.deepcopy(selected["value"]),
        "selected_snapshot": selected,
        "projection_hash": _require_text(projection.get("projection_hash"), "projection_hash"),
    }


def phase_scoped_required_state_value(value: Any) -> Any:
    """Validate a phase-bound assertion value and return its selected token.

    Plain legacy values are intentionally returned unchanged so earlier recorded
    contracts remain replayable.  Any object declaring this phase contract must
    satisfy the complete source-trace and phase-binding contract.
    """

    if not isinstance(value, Mapping) or value.get("snapshot_contract") != "STATE_PHASE_SNAPSHOT_V0.1":
        return value
    if set(value) != set(PHASE_ASSERTION_VALUE_FIELDS):
        raise StatePhaseContractError("phase-bound REQUIRED_STATE value has unexpected fields")
    required_phase = value.get("required_phase")
    if required_phase not in SNAPSHOT_PHASES:
        raise StatePhaseContractError("phase-bound REQUIRED_STATE has an unsupported required phase")
    snapshot = _validate_snapshot(value.get("selected_snapshot"))
    if snapshot["phase"] != required_phase:
        raise StatePhaseContractError("phase-bound REQUIRED_STATE selected the wrong snapshot phase")
    if value.get("selected_value") != snapshot["value"]:
        raise StatePhaseContractError("phase-bound REQUIRED_STATE token does not match selected snapshot")
    _require_text(value.get("projection_hash"), "projection_hash")
    return copy.deepcopy(snapshot["value"])
