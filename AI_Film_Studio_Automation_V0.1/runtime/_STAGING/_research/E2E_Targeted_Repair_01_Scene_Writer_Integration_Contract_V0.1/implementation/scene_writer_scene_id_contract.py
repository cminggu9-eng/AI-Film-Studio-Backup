"""Run-scoped Scene Writer machine identity projection.

The compiled run contract, not a fixture global or a previous run, owns the
ordered scene-id sequence.  This module contains no fixture-specific scene ID.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any, Mapping, Sequence


SCENE_ID_CONTRACT_VERSION = "0.1"


class SceneIDContractError(RuntimeError):
    """The compiled run contract cannot authoritatively identify its scenes."""


def _stable_hash(value: Mapping[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def build_scene_id_contract(compiled_run_contract: Mapping[str, Any]) -> dict[str, Any]:
    """Project one exact ordered scene-id contract from one compiled run contract."""

    if not isinstance(compiled_run_contract, Mapping):
        raise SceneIDContractError("compiled run contract is required")
    fixture = compiled_run_contract.get("fixture")
    scene_ids = compiled_run_contract.get("scene_ids")
    if not isinstance(fixture, Mapping) or not isinstance(fixture.get("fixture_id"), str) or not fixture["fixture_id"].strip():
        raise SceneIDContractError("compiled fixture identity is required")
    if not isinstance(scene_ids, Sequence) or isinstance(scene_ids, (str, bytes)):
        raise SceneIDContractError("compiled ordered scene IDs are required")
    ordered_scene_ids = list(scene_ids)
    if not ordered_scene_ids or not all(isinstance(scene_id, str) and scene_id.strip() for scene_id in ordered_scene_ids):
        raise SceneIDContractError("compiled scene IDs must be non-empty strings")
    if len(set(ordered_scene_ids)) != len(ordered_scene_ids):
        raise SceneIDContractError("compiled scene IDs must be unique")
    scene_count = fixture.get("scene_count")
    if not isinstance(scene_count, int) or scene_count <= 0 or scene_count != len(ordered_scene_ids):
        raise SceneIDContractError("compiled scene count must exactly match the ordered scene IDs")
    projection = {
        "contract_version": SCENE_ID_CONTRACT_VERSION,
        "binding_id": fixture["fixture_id"],
        "scene_count": scene_count,
        "ordered_scene_ids": ordered_scene_ids,
        "source_contract_pointer": "compiled_run_contract#/scene_ids",
    }
    projection["contract_hash"] = _stable_hash(projection)
    return projection


def ordered_scene_ids(scene_id_contract: Mapping[str, Any]) -> list[str]:
    """Read and revalidate the exact full-token order from a projected contract."""

    if not isinstance(scene_id_contract, Mapping):
        raise SceneIDContractError("scene-id contract is required")
    scene_ids = scene_id_contract.get("ordered_scene_ids")
    count = scene_id_contract.get("scene_count")
    if not isinstance(scene_ids, Sequence) or isinstance(scene_ids, (str, bytes)):
        raise SceneIDContractError("scene-id contract ordered_scene_ids is required")
    values = list(scene_ids)
    if not values or not all(isinstance(scene_id, str) and scene_id.strip() for scene_id in values):
        raise SceneIDContractError("scene-id contract values must be non-empty strings")
    if len(values) != len(set(values)) or count != len(values):
        raise SceneIDContractError("scene-id contract count and unique ordered values must agree")
    return values


def assess_scene_id_sequence(actual_scene_ids: Sequence[Any], scene_id_contract: Mapping[str, Any]) -> dict[str, Any]:
    """Classify exact sequence conformance without reordering or repairing it."""

    expected = ordered_scene_ids(scene_id_contract)
    observed = list(actual_scene_ids)
    return {
        "expected_ordered_scene_ids": expected,
        "actual_scene_ids": observed,
        "scene_count_matches": len(observed) == len(expected),
        "exact_order_matches": observed == expected,
        "duplicates": sorted({scene_id for scene_id in observed if observed.count(scene_id) > 1 and isinstance(scene_id, str)}),
        "foreign_scene_ids": [scene_id for scene_id in observed if scene_id not in expected],
        "missing_scene_ids": [scene_id for scene_id in expected if scene_id not in observed],
        "result": "PASS" if observed == expected else "FAIL",
    }
