"""Binding-derived identity and transition projections for Semantic Safeguard.

The projection compilers consume only the current compiled run contract and
validated scene-local machine evidence.  They do not infer aliases from token
wording, consult historical fixtures, or mutate creative output.
"""

from __future__ import annotations

import copy
import hashlib
import json
from typing import Any, Dict, Mapping, Sequence


IDENTITY_NAMESPACES = ("transport.entity_id", "assertion.identity_lock")
TRANSITION_CLASSIFICATIONS = ("AUTHORIZED", "OCCURRED", "OBSERVED", "HANDED_OFF")
RESOLVED_IDENTITY_FIELDS = {
    "representation_namespace",
    "representation_token",
    "resolved_binding_entity",
    "source_binding_id",
    "projection_hash",
}


class SemanticAlignmentContractError(ValueError):
    """Raised when current-run identity or transition evidence is unresolvable."""


def _stable_hash(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _fixture(compiled_run_contract: Mapping[str, Any]) -> Dict[str, Any]:
    if not isinstance(compiled_run_contract, Mapping) or not isinstance(compiled_run_contract.get("fixture"), Mapping):
        raise SemanticAlignmentContractError("compiled_run_contract.fixture is required")
    fixture = copy.deepcopy(dict(compiled_run_contract["fixture"]))
    if not isinstance(fixture.get("fixture_id"), str) or not fixture["fixture_id"].strip():
        raise SemanticAlignmentContractError("current binding fixture_id is required")
    return fixture


def build_entity_identity_projection(compiled_run_contract: Mapping[str, Any]) -> Dict[str, Any]:
    """Compile per-run namespace representations onto binding entity nodes."""

    fixture = _fixture(compiled_run_contract)
    entities = fixture.get("tracked_entities")
    if not isinstance(entities, list) or not entities:
        raise SemanticAlignmentContractError("current binding tracked_entities are required")
    records: list[Dict[str, Any]] = []
    seen_by_namespace = {namespace: set() for namespace in IDENTITY_NAMESPACES}
    for index, entity in enumerate(entities):
        if not isinstance(entity, Mapping):
            raise SemanticAlignmentContractError("tracked entity records must be objects")
        entity_id = entity.get("entity_id")
        identity_lock = entity.get("identity_lock")
        if not isinstance(entity_id, str) or not entity_id.strip() or not isinstance(identity_lock, str) or not identity_lock.strip():
            raise SemanticAlignmentContractError("tracked entity_id and identity_lock are required")
        tokens = {
            "transport.entity_id": entity_id,
            "assertion.identity_lock": identity_lock,
        }
        for namespace, token in tokens.items():
            if token in seen_by_namespace[namespace]:
                raise SemanticAlignmentContractError(f"ambiguous {namespace} token in current binding")
            seen_by_namespace[namespace].add(token)
        records.append(
            {
                "binding_entity_node": f"{fixture['fixture_id']}#/tracked_entities/{index}",
                "representations": tokens,
                "authority_source": "compiled_run_contract#/fixture/tracked_entities",
            }
        )
    core = {
        "projection_type": "CURRENT_RUN_ENTITY_IDENTITY_PROJECTION",
        "source_binding_id": fixture["fixture_id"],
        "source_contract_pointer": "compiled_run_contract#/fixture/tracked_entities",
        "entities": records,
        "derivation": "BINDING_RECORD_MEMBERSHIP_ONLY",
    }
    return {**core, "projection_hash": _stable_hash(core)}


def resolve_entity_identity(projection: Mapping[str, Any], *, namespace: str, token: Any) -> Dict[str, str]:
    """Resolve one exact namespace token; unknown or ambiguous values fail closed."""

    if namespace not in IDENTITY_NAMESPACES:
        raise SemanticAlignmentContractError("unsupported identity representation namespace")
    if not isinstance(token, str) or not token.strip():
        raise SemanticAlignmentContractError("identity representation token is required")
    matches = [
        item for item in projection.get("entities", [])
        if isinstance(item, Mapping)
        and isinstance(item.get("representations"), Mapping)
        and item["representations"].get(namespace) == token
    ]
    if len(matches) != 1:
        raise SemanticAlignmentContractError("identity representation is unknown or ambiguous in current binding")
    node = matches[0].get("binding_entity_node")
    if not isinstance(node, str) or not node:
        raise SemanticAlignmentContractError("resolved binding entity node is invalid")
    return {
        "representation_namespace": namespace,
        "representation_token": token,
        "resolved_binding_entity": node,
        "source_binding_id": str(projection.get("source_binding_id")),
        "projection_hash": str(projection.get("projection_hash")),
    }


def resolved_identity_match(value: Any, expected: Any) -> bool:
    """Compare two typed resolutions by authoritative binding identity."""

    if not isinstance(value, Mapping) or not isinstance(expected, Mapping):
        return value == expected
    if set(value) != RESOLVED_IDENTITY_FIELDS or set(expected) != RESOLVED_IDENTITY_FIELDS:
        return False
    if value.get("representation_namespace") == expected.get("representation_namespace"):
        return False
    return (
        value.get("resolved_binding_entity") == expected.get("resolved_binding_entity")
        and value.get("source_binding_id") == expected.get("source_binding_id")
        and value.get("projection_hash") == expected.get("projection_hash")
        and isinstance(value.get("projection_hash"), str)
        and bool(value.get("projection_hash"))
    )


def build_shared_transition_authority_projection(compiled_run_contract: Mapping[str, Any]) -> Dict[str, Any]:
    """Compile the existing binding transition authority without token parsing."""

    fixture = _fixture(compiled_run_contract)
    dimensions = fixture.get("state_dimensions")
    transitions = fixture.get("authorized_transitions")
    if not isinstance(dimensions, list) or not dimensions or not isinstance(transitions, list) or not transitions:
        raise SemanticAlignmentContractError("state dimensions and authorized transitions are required")
    if len(dimensions) != len(transitions):
        raise SemanticAlignmentContractError("transition-to-state-dimension association is ambiguous")
    records: list[Dict[str, Any]] = []
    for index, (dimension, transition) in enumerate(zip(dimensions, transitions)):
        if not isinstance(dimension, Mapping):
            raise SemanticAlignmentContractError("state dimension records must be objects")
        name = dimension.get("dimension")
        tokens = dimension.get("allowed_tokens")
        if not isinstance(name, str) or not name or not isinstance(tokens, list) or len(tokens) != 2 or not all(isinstance(item, str) and item for item in tokens):
            raise SemanticAlignmentContractError("transition occurrence requires one exact two-token state dimension")
        if not isinstance(transition, str) or not transition:
            raise SemanticAlignmentContractError("authorized transition token is required")
        records.append(
            {
                "authority_node": f"{fixture['fixture_id']}#/authorized_transitions/{index}",
                "transition_id": transition,
                "state_dimension": name,
                "from_state": tokens[0],
                "to_state": tokens[1],
                "allowed_scene_window": list(range(1, int(fixture.get("scene_count", 0)) + 1)),
                "authorization_source": fixture["fixture_id"],
                "preconditions": copy.deepcopy(fixture.get("decision_locks", [])),
                "postconditions": copy.deepcopy(fixture.get("prohibited_outcomes", [])),
                "evidence_requirements": ["adjacent_validated_machine_state"],
            }
        )
    core = {
        "projection_type": "SHARED_TRANSITION_AUTHORITY_PROJECTION",
        "source_binding_id": fixture["fixture_id"],
        "source_contract_pointer": "compiled_run_contract#/fixture/state_dimensions+authorized_transitions",
        "records": records,
        "classification_taxonomy": list(TRANSITION_CLASSIFICATIONS),
    }
    return {**core, "projection_hash": _stable_hash(core)}


def classify_transition_evidence(
    projection: Mapping[str, Any],
    scenes: Sequence[Mapping[str, Any]],
    *,
    handed_off: bool = False,
) -> Dict[str, Any]:
    """Classify existing scene-local evidence; authorization alone never means occurrence."""

    records = projection.get("records")
    if not isinstance(records, list) or len(records) != 1 or not isinstance(records[0], Mapping):
        raise SemanticAlignmentContractError("one unambiguous transition authority record is required")
    authority = records[0]
    dimension = authority.get("state_dimension")
    from_state = authority.get("from_state")
    to_state = authority.get("to_state")
    transition = authority.get("transition_id")
    if not scenes:
        raise SemanticAlignmentContractError("validated scene-local evidence is required")
    occurrences: list[Dict[str, Any]] = []
    prior = from_state
    for index, scene in enumerate(scenes, start=1):
        if not isinstance(scene, Mapping) or not isinstance(scene.get("state_evidence"), Mapping):
            raise SemanticAlignmentContractError("scene-local state_evidence is required")
        state = scene["state_evidence"]
        current = state.get(dimension)
        if current not in (from_state, to_state):
            raise SemanticAlignmentContractError("scene machine state is outside shared transition authority")
        locator = scene.get("evidence_locator")
        if not isinstance(locator, str) or not locator:
            raise SemanticAlignmentContractError("scene-local evidence locator is required")
        if prior == from_state and current == to_state:
            occurrences.append(
                {
                    "scene_index": index,
                    "scene_id": scene.get("scene_id"),
                    "prior_state": prior,
                    "current_state": current,
                    "evidence_locator": locator,
                    "evidence_rule": "ADJACENT_VALIDATED_MACHINE_STATE",
                }
            )
        prior = current
    authorized = isinstance(transition, str) and bool(transition)
    occurred = len(occurrences) == 1
    observed = occurred and all(item.get("evidence_locator") for item in occurrences)
    return {
        "transition_id": transition,
        "authority": copy.deepcopy(dict(authority)),
        "machine_classification": {
            "AUTHORIZED": authorized,
            "OCCURRED": occurred,
            "OBSERVED": observed,
            "HANDED_OFF": bool(handed_off),
        },
        "occurrence_evidence": occurrences,
        "projection_hash": projection.get("projection_hash"),
        "source_binding_id": projection.get("source_binding_id"),
    }
