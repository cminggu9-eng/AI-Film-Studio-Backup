"""Deterministic compiler for generic E2E runtime fixture bindings.

This module knows contract structure only. Story facts are supplied by a JSON
fixture binding and are never inferred, translated, or repaired.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

REQUIRED = {"fixture_id", "concept", "scene_count", "characters", "tracked_entities", "knowledge_events", "relationship_constraints", "state_dimensions", "authorized_transitions", "time_conditions", "decision_locks", "prohibited_outcomes", "acceptance_evidence"}
REVEAL_EVENT_CONTRACT_VERSION = "0.1"
REVEAL_STATUS_CODES = ["NOT_YET_REVEALED", "REVEALED_WITH_EVENT"]

class FixtureContractError(ValueError): pass

def load_binding(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or set(data) != REQUIRED:
        raise FixtureContractError("fixture binding must contain the exact generic contract fields")
    if not isinstance(data["fixture_id"], str) or not data["fixture_id"].strip() or not isinstance(data["scene_count"], int) or data["scene_count"] <= 0:
        raise FixtureContractError("fixture_id and positive scene_count are required")
    for name in ("characters", "tracked_entities", "knowledge_events", "relationship_constraints", "state_dimensions", "authorized_transitions", "decision_locks", "prohibited_outcomes"):
        if not isinstance(data[name], list) or not data[name]: raise FixtureContractError(f"{name} must be a non-empty list")
    if not isinstance(data["acceptance_evidence"], dict) or not data["acceptance_evidence"]: raise FixtureContractError("acceptance_evidence is required")
    return copy.deepcopy(data)

def compile_binding(binding: Mapping[str, Any]) -> dict[str, Any]:
    source = load_binding_value(binding)
    scene_ids = [f"{source['fixture_id']}-S{index:02d}" for index in range(1, source["scene_count"] + 1)]
    entity_ids = [item["entity_id"] for item in source["tracked_entities"]]
    state_enums = {item["dimension"]: item["allowed_tokens"] for item in source["state_dimensions"]}
    return {"fixture": source, "scene_ids": scene_ids, "tracked_entity_ids": entity_ids, "state_enums": state_enums, "strict_schema": strict_schema(scene_ids, entity_ids, state_enums, source["authorized_transitions"]), "semantic_safeguard_config": {"tracked_entities": source["tracked_entities"], "knowledge_events": source["knowledge_events"], "relationship_constraints": source["relationship_constraints"], "state_dimensions": source["state_dimensions"], "authorized_transitions": source["authorized_transitions"], "time_conditions": source["time_conditions"], "prohibited_outcomes": source["prohibited_outcomes"], "decision_locks": source["decision_locks"]}, "ledger_tracking": {"entity_ids": entity_ids, "state_dimensions": list(state_enums), "state_enums": state_enums, "authorized_transitions": source["authorized_transitions"], "time_conditions": source["time_conditions"]}, "acceptance_evidence_map": source["acceptance_evidence"], "reveal_event_contract": build_reveal_event_contract(source, scene_ids)}


def build_reveal_event_contract(source: Mapping[str, Any], scene_ids: list[str]) -> dict[str, Any]:
    """Project the binding's accepted reveal event without interpreting scene prose."""

    acceptance = source.get("acceptance_evidence")
    event_id = acceptance.get("reveal") if isinstance(acceptance, Mapping) else None
    events = source.get("knowledge_events")
    if not isinstance(event_id, str) or not event_id.strip() or not isinstance(events, list):
        raise FixtureContractError("acceptance_evidence.reveal must identify a binding knowledge event")
    matches = [event for event in events if isinstance(event, Mapping) and event.get("event_id") == event_id]
    if len(matches) != 1:
        raise FixtureContractError("acceptance_evidence.reveal must identify exactly one binding knowledge event")
    event = matches[0]
    holder = event.get("holder")
    not_before_scene = event.get("not_before_scene")
    if not isinstance(holder, str) or not holder.strip() or not isinstance(not_before_scene, int) or not 1 <= not_before_scene <= len(scene_ids):
        raise FixtureContractError("binding reveal event holder and timing must be valid")
    projection = {
        "contract_version": REVEAL_EVENT_CONTRACT_VERSION,
        "fixture_id": source["fixture_id"],
        "source_owner": "compiled_run_contract",
        "event_id": event_id,
        "holder": holder,
        "not_before_scene": not_before_scene,
        "eligible_scene_ids": copy.deepcopy(scene_ids[not_before_scene - 1:]),
        "reveal_status_field": "reveal_status",
        "allowed_status_codes": copy.deepcopy(REVEAL_STATUS_CODES),
        "required_status_code": "REVEALED_WITH_EVENT",
        "required": True,
        "acceptance_source_pointer": "compiled_run_contract#/fixture/acceptance_evidence/reveal",
        "knowledge_event_source_pointer": "compiled_run_contract#/fixture/knowledge_events",
        "scene_id_source_pointer": "compiled_run_contract#/scene_ids",
    }
    projection["contract_hash"] = hashlib.sha256(json.dumps(projection, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    return projection

def load_binding_value(value: Mapping[str, Any]) -> dict[str, Any]:
    candidate = dict(value)
    if set(candidate) != REQUIRED: raise FixtureContractError("fixture binding must contain the exact generic contract fields")
    # serialize through the same fail-closed validation path without any inference
    temp = json.loads(json.dumps(candidate, ensure_ascii=False))
    if not isinstance(temp["scene_count"], int) or temp["scene_count"] <= 0: raise FixtureContractError("scene_count must be positive")
    for field in ("characters", "tracked_entities", "knowledge_events", "relationship_constraints", "state_dimensions", "authorized_transitions", "decision_locks", "prohibited_outcomes"):
        if not isinstance(temp[field], list) or not temp[field]: raise FixtureContractError(f"{field} must be non-empty")
    return temp

def strict_schema(scene_ids: list[str], entity_ids: list[str], state_enums: Mapping[str, Any], transitions: list[Any]) -> dict[str, Any]:
    return {"type": "object", "additionalProperties": False, "properties": {"scene_packages": {"type": "array", "items": {"type": "object", "additionalProperties": False, "properties": {"scene_id": {"type": "string", "enum": scene_ids}, "tracked_entity_id": {"type": "string", "enum": entity_ids}, "state": {"type": "object", "properties": {key: {"type": "string", "enum": value} for key, value in state_enums.items()}, "required": list(state_enums), "additionalProperties": False}, "authorized_transitions": {"type": "array", "items": {"type": "string", "enum": transitions}}}, "required": ["scene_id", "tracked_entity_id", "state", "authorized_transitions"]}}}, "required": ["scene_packages"]}

def compile_path(path: Path) -> dict[str, Any]: return compile_binding(load_binding(path))
