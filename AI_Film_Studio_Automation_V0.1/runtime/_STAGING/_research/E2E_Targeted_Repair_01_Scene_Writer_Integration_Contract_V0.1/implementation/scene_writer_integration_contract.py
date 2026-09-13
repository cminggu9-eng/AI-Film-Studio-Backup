"""Compiled-run-scoped Scene Writer Integration Contract.

The contract separates machine-readable state from display prose and keeps the
six frozen structural deliverable names outside normal scene text. It validates
transport shape and exact fixture tokens only; semantic judgement remains the
separate Integration Semantic Safeguard.
"""

from __future__ import annotations

import copy
import hashlib
import json
from typing import Any, Dict, Mapping, Sequence

from scene_writer_scene_id_contract import SceneIDContractError, build_scene_id_contract, ordered_scene_ids
from scene_writer_state_field_contract import (
    StateFieldContractError,
    allowed_machine_tokens,
    authorized_transition_tokens,
    build_scene_writer_state_projection,
    state_field_name,
    tracked_entity_ids,
)


CONTRACT_VERSION = "0.1"
STRUCTURAL_FIELD_NAMES = ("目标", "阻力", "对白行动", "转折", "入场", "出场")
SCENE_FIELDS = {
    "scene_id",
    "content",
    "structural_deliverable",
    "state_evidence",
    "source_attribution",
    "evidence_locator",
}
STATE_EVIDENCE_BASE_FIELDS = {
    "entity_identity",
    "entity_custody",
    "knowledge_holders",
    "reveal_status",
    "relationship_state",
    "machine_state_display",
    "location_presence",
    "authorized_transitions",
}
SOURCE_ATTRIBUTION_FIELDS = {"source_role", "source_record_id", "version", "evidence_locator"}
ALLOWED_REVEAL_STATUS_CODES = {"NOT_YET_REVEALED", "REVEALED_WITH_EVENT"}


class SceneWriterIntegrationContractError(RuntimeError):
    """A structural/state-token contract failure with attributable diagnostics."""

    def __init__(self, diagnostics: Sequence[Mapping[str, Any]]) -> None:
        self.diagnostics = copy.deepcopy([dict(item) for item in diagnostics])
        super().__init__("; ".join(str(item.get("code")) for item in self.diagnostics) or "Scene Writer contract failed")


def _diagnostic(code: str, path: str, detail: str) -> Dict[str, str]:
    return {"code": code, "path": path, "detail": detail, "contract_version": CONTRACT_VERSION}


def _nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def state_evidence_fields(state_field_contract: Mapping[str, Any]) -> set[str]:
    return STATE_EVIDENCE_BASE_FIELDS | {state_field_name(state_field_contract)}


def frozen_contract_sources(fixture_contract: Mapping[str, Any]) -> Dict[str, Any]:
    """Expose run-scoped machine identity from the supplied compiled contract."""

    scene_contract = build_scene_id_contract(fixture_contract)
    state_contract = build_scene_writer_state_projection(fixture_contract)

    return {
        "fixture_id": scene_contract["binding_id"],
        "structural_field_names": list(STRUCTURAL_FIELD_NAMES),
        "scene_ids": ordered_scene_ids(scene_contract),
        "scene_id_contract": scene_contract,
        "state_field_split": [state_field_name(state_contract), "machine_state_display"],
        "state_field_contract": state_contract,
        "exact_machine_tokens": {
            "tracked_entity_ids": tracked_entity_ids(state_contract),
            "initial_state": state_contract["initial_token"],
            "allowed_machine_tokens": allowed_machine_tokens(state_contract),
            "authorized_transitions": authorized_transition_tokens(state_contract),
            "reveal_status_codes": sorted(ALLOWED_REVEAL_STATUS_CODES),
        },
        "source_artifacts": [
            state_contract["state_dimension_source_pointer"],
            state_contract["state_enum_source_pointer"],
            state_contract["transition_source_pointer"],
        ],
    }


def assess_structural_contract(result: Any, *, run_id: str, fixture_contract: Mapping[str, Any]) -> Dict[str, Any]:
    """Check presence, type, exact structure, version, and attribution only."""

    diagnostics: list[Dict[str, str]] = []
    try:
        scene_ids = ordered_scene_ids(build_scene_id_contract(fixture_contract))
        state_contract = build_scene_writer_state_projection(fixture_contract)
        expected_state_fields = state_evidence_fields(state_contract)
        current_state_field = state_field_name(state_contract)
    except (SceneIDContractError, StateFieldContractError) as exc:
        return {"gate": "Scene Writer Structural Contract Gate", "contract_version": CONTRACT_VERSION, "passed": False, "diagnostics": [_diagnostic("COMPILED_RUN_CONTRACT", "fixture_contract", str(exc))]}
    scenes = result.get("scene_packages") if isinstance(result, Mapping) else None
    if not isinstance(scenes, list):
        diagnostics.append(_diagnostic("SCENE_PACKAGES_TYPE", "scene_packages", "scene_packages must be a list."))
        scenes = []
    if len(scenes) != len(scene_ids):
        diagnostics.append(_diagnostic("SCENE_COUNT", "scene_packages", "Scene package count must equal the compiled ordered scene-id contract."))
    for index, scene_id in enumerate(scene_ids):
        path = f"scene_packages[{index}]"
        if index >= len(scenes) or not isinstance(scenes[index], Mapping):
            diagnostics.append(_diagnostic("SCENE_PACKAGE_MISSING", path, "A scene package mapping is required."))
            continue
        scene = scenes[index]
        if set(scene) != SCENE_FIELDS:
            unexpected = sorted(set(scene) - SCENE_FIELDS)
            missing = sorted(SCENE_FIELDS - set(scene))
            diagnostics.append(_diagnostic("SCENE_FIELD_SET", path, f"Missing={missing}; unsupported={unexpected}."))
        if scene.get("scene_id") != scene_id:
            diagnostics.append(_diagnostic("SCENE_ID", f"{path}.scene_id", f"Expected exact scene id {scene_id}."))
        if not _nonempty_text(scene.get("content")):
            diagnostics.append(_diagnostic("SCENE_CONTENT", f"{path}.content", "Human-readable scene material must be non-empty."))
        if scene.get("evidence_locator") != f"scene_packages/{scene_id}":
            diagnostics.append(_diagnostic("SCENE_EVIDENCE_LOCATOR", f"{path}.evidence_locator", "Evidence locator must use the exact scene-local locator."))
        structural = scene.get("structural_deliverable")
        if not isinstance(structural, Mapping):
            diagnostics.append(_diagnostic("MISSING_STRUCTURAL_DELIVERABLE", f"{path}.structural_deliverable", "Structured deliverable mapping is required."))
        else:
            missing_items = [name for name in STRUCTURAL_FIELD_NAMES if name not in structural]
            extra_items = sorted(set(structural) - set(STRUCTURAL_FIELD_NAMES))
            if missing_items or extra_items:
                diagnostics.append(_diagnostic("STRUCTURAL_DELIVERABLE_FIELD_SET", f"{path}.structural_deliverable", f"Missing={missing_items}; unsupported={extra_items}."))
            for name in STRUCTURAL_FIELD_NAMES:
                if not _nonempty_text(structural.get(name)):
                    diagnostics.append(_diagnostic("MISSING_STRUCTURAL_ITEM", f"{path}.structural_deliverable.{name}", "A non-empty minimum sufficient value is required."))
        state = scene.get("state_evidence")
        if not isinstance(state, Mapping):
            diagnostics.append(_diagnostic("SCENE_STATE_TYPE", f"{path}.state_evidence", "State evidence mapping is required."))
        else:
            missing_state = sorted(expected_state_fields - set(state))
            extra_state = sorted(set(state) - expected_state_fields)
            if current_state_field in missing_state:
                diagnostics.append(_diagnostic("MISSING_MACHINE_STATE_CODE", f"{path}.state_evidence.{current_state_field}", "The compiled current-run state field is required."))
            if "machine_state_display" in missing_state:
                diagnostics.append(_diagnostic("MISSING_DISPLAY_PROSE", f"{path}.state_evidence.machine_state_display", "Human-readable display prose is required."))
            if missing_state or extra_state:
                diagnostics.append(_diagnostic("SCENE_STATE_FIELD_SET", f"{path}.state_evidence", f"Missing={missing_state}; unsupported={extra_state}."))
            for field in ("entity_identity", "entity_custody", "reveal_status", "relationship_state", current_state_field, "machine_state_display", "location_presence"):
                if field in state and not _nonempty_text(state.get(field)):
                    diagnostics.append(_diagnostic("SCENE_STATE_TEXT", f"{path}.state_evidence.{field}", "Non-empty text is required."))
            if "knowledge_holders" in state and (not isinstance(state.get("knowledge_holders"), list) or not all(_nonempty_text(item) for item in state["knowledge_holders"])):
                diagnostics.append(_diagnostic("KNOWLEDGE_HOLDERS_TYPE", f"{path}.state_evidence.knowledge_holders", "A non-empty-text list is required."))
            if "authorized_transitions" in state and (not isinstance(state.get("authorized_transitions"), list) or not all(_nonempty_text(item) for item in state["authorized_transitions"])):
                diagnostics.append(_diagnostic("AUTHORIZED_TRANSITIONS_TYPE", f"{path}.state_evidence.authorized_transitions", "A text list is required."))
        source = scene.get("source_attribution")
        if not isinstance(source, Mapping):
            diagnostics.append(_diagnostic("MISSING_SOURCE_ATTRIBUTION", f"{path}.source_attribution", "Source/version/evidence attribution is required."))
        else:
            missing_source = sorted(SOURCE_ATTRIBUTION_FIELDS - set(source))
            extra_source = sorted(set(source) - SOURCE_ATTRIBUTION_FIELDS)
            if missing_source or extra_source:
                diagnostics.append(_diagnostic("SOURCE_ATTRIBUTION_FIELD_SET", f"{path}.source_attribution", f"Missing={missing_source}; unsupported={extra_source}."))
            expected_record = f"{run_id}/scene_writer/{scene_id}"
            if source.get("source_role") != "Scene Writer":
                diagnostics.append(_diagnostic("SOURCE_ROLE", f"{path}.source_attribution.source_role", "Source role must be exact Scene Writer."))
            if source.get("source_record_id") != expected_record:
                diagnostics.append(_diagnostic("SOURCE_RECORD_ID", f"{path}.source_attribution.source_record_id", f"Expected exact source record id {expected_record}."))
            if source.get("version") != CONTRACT_VERSION:
                diagnostics.append(_diagnostic("SOURCE_VERSION", f"{path}.source_attribution.version", f"Expected contract version {CONTRACT_VERSION}."))
            if source.get("evidence_locator") != scene.get("evidence_locator"):
                diagnostics.append(_diagnostic("SOURCE_EVIDENCE_LOCATOR", f"{path}.source_attribution.evidence_locator", "Source attribution must repeat the supplied scene evidence locator exactly."))
    return {"gate": "Scene Writer Structural Contract Gate", "contract_version": CONTRACT_VERSION, "passed": not diagnostics, "diagnostics": diagnostics}


def assess_state_token_contract(result: Any, fixture_contract: Mapping[str, Any]) -> Dict[str, Any]:
    """Check exact compiled-run machine fields and tokens without reading prose."""

    diagnostics: list[Dict[str, str]] = []
    scenes = result.get("scene_packages") if isinstance(result, Mapping) else None
    if not isinstance(scenes, list):
        scenes = []
    try:
        projection = build_scene_writer_state_projection(fixture_contract)
        field = state_field_name(projection)
        allowed = set(allowed_machine_tokens(projection))
        entities = set(tracked_entity_ids(projection))
        transitions = set(authorized_transition_tokens(projection))
    except StateFieldContractError as exc:
        diagnostics.append(_diagnostic("FIXTURE_CONTRACT_INCOMPLETE", "fixture_contract", str(exc)))
        return {"gate": "Scene Writer State Token Gate", "contract_version": CONTRACT_VERSION, "passed": False, "diagnostics": diagnostics}
    try:
        reveal_contract = _validated_reveal_event_contract(fixture_contract)
    except ValueError as exc:
        diagnostics.append(_diagnostic("REVEAL_EVENT_CONTRACT_INCOMPLETE", "fixture_contract.reveal_event_contract", str(exc)))
        return {"gate": "Scene Writer State Token Gate", "contract_version": CONTRACT_VERSION, "passed": False, "diagnostics": diagnostics}
    observed_transition = False
    lawful_reveal = False
    for index, scene in enumerate(scenes):
        state = scene.get("state_evidence", {}) if isinstance(scene, Mapping) else {}
        path = f"scene_packages[{index}].state_evidence"
        if state.get("entity_identity") not in entities:
            diagnostics.append(_diagnostic("ENTITY_IDENTITY_TOKEN", f"{path}.entity_identity", "Binding-derived entity identity is required."))
        if field not in state:
            diagnostics.append(_diagnostic("MISSING_MACHINE_STATE_CODE", f"{path}.{field}", "The compiled current-run state field is required."))
        elif state.get(field) not in allowed:
            diagnostics.append(_diagnostic("INVALID_MACHINE_STATE_CODE", f"{path}.{field}", "Binding-derived machine state is required."))
        scene_transitions = state.get("authorized_transitions", [])
        if any(item not in transitions for item in scene_transitions):
            diagnostics.append(_diagnostic("FOREIGN_TRANSITION_TOKEN", f"{path}.authorized_transitions", "Transition is outside the compiled current-run authority."))
        observed_transition = observed_transition or any(item in transitions for item in scene_transitions)
        if state.get("reveal_status") not in ALLOWED_REVEAL_STATUS_CODES:
            diagnostics.append(_diagnostic("REVEAL_STATUS_TOKEN", f"{path}.reveal_status", "Unsupported reveal-status token."))
        if state.get("reveal_status") == reveal_contract["required_status_code"]:
            scene_id = scene.get("scene_id") if isinstance(scene, Mapping) else None
            if scene_id not in reveal_contract["eligible_scene_ids"]:
                diagnostics.append(_diagnostic("REVEAL_EVENT_TOO_EARLY", f"{path}.reveal_status", "Required reveal status is outside the compiled eligible scene range."))
            else:
                lawful_reveal = True
    if not observed_transition:
        diagnostics.append(_diagnostic("AUTHORIZED_TRANSITION_TOKEN", "scene_packages", "A binding-authorized transition must be evidenced in its actual scene."))
    if reveal_contract["required"] and not lawful_reveal:
        diagnostics.append(_diagnostic("REQUIRED_REVEAL_EVENT", "scene_packages", "At least one compiled-eligible scene must emit the required reveal-status token."))
    return {"gate": "Scene Writer State Token Gate", "contract_version": CONTRACT_VERSION, "passed": not diagnostics, "diagnostics": diagnostics}


def _validated_reveal_event_contract(fixture_contract: Mapping[str, Any]) -> Dict[str, Any]:
    """Validate the compiler-owned reveal projection; never inspect display prose."""

    contract = fixture_contract.get("reveal_event_contract") if isinstance(fixture_contract, Mapping) else None
    fixture = fixture_contract.get("fixture") if isinstance(fixture_contract, Mapping) else None
    scene_ids = fixture_contract.get("scene_ids") if isinstance(fixture_contract, Mapping) else None
    if not isinstance(contract, Mapping) or not isinstance(fixture, Mapping) or not isinstance(scene_ids, list):
        raise ValueError("compiled reveal-event authority is required")
    required = {"contract_version", "fixture_id", "source_owner", "event_id", "holder", "not_before_scene", "eligible_scene_ids", "reveal_status_field", "allowed_status_codes", "required_status_code", "required", "acceptance_source_pointer", "knowledge_event_source_pointer", "scene_id_source_pointer", "contract_hash"}
    if set(contract) != required:
        raise ValueError("compiled reveal-event contract field set is invalid")
    source = dict(contract)
    supplied_hash = source.pop("contract_hash")
    expected_hash = hashlib.sha256(json.dumps(source, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    if supplied_hash != expected_hash:
        raise ValueError("compiled reveal-event contract hash is invalid")
    if contract["source_owner"] != "compiled_run_contract" or contract["fixture_id"] != fixture.get("fixture_id"):
        raise ValueError("compiled reveal-event contract source is invalid")
    if contract["reveal_status_field"] != "reveal_status" or contract["allowed_status_codes"] != sorted(ALLOWED_REVEAL_STATUS_CODES) or contract["required_status_code"] != "REVEALED_WITH_EVENT" or contract["required"] is not True:
        raise ValueError("compiled reveal-event token domain is invalid")
    event_id = fixture.get("acceptance_evidence", {}).get("reveal") if isinstance(fixture.get("acceptance_evidence"), Mapping) else None
    events = fixture.get("knowledge_events")
    matches = [event for event in events if isinstance(event, Mapping) and event.get("event_id") == event_id] if isinstance(events, list) else []
    if len(matches) != 1 or event_id != contract["event_id"]:
        raise ValueError("compiled reveal-event authority does not match binding acceptance evidence")
    event = matches[0]
    if event.get("holder") != contract["holder"] or event.get("not_before_scene") != contract["not_before_scene"]:
        raise ValueError("compiled reveal-event timing does not match binding knowledge event")
    if not isinstance(contract["not_before_scene"], int) or not 1 <= contract["not_before_scene"] <= len(scene_ids):
        raise ValueError("compiled reveal-event timing is invalid")
    if contract["eligible_scene_ids"] != scene_ids[contract["not_before_scene"] - 1:]:
        raise ValueError("compiled reveal-event eligible scene projection is invalid")
    return copy.deepcopy(dict(contract))


def assess_scene_writer_integration_contract(result: Any, *, run_id: str, fixture_contract: Mapping[str, Any]) -> Dict[str, Any]:
    structural = assess_structural_contract(result, run_id=run_id, fixture_contract=fixture_contract)
    state_token = assess_state_token_contract(result, fixture_contract)
    return {
        "contract_version": CONTRACT_VERSION,
        "fixture_id": build_scene_id_contract(fixture_contract)["binding_id"],
        "structural_gate": structural,
        "state_token_gate": state_token,
        "passed": structural["passed"] and state_token["passed"],
    }


def validate_scene_writer_integration_contract(result: Any, *, run_id: str, fixture_contract: Mapping[str, Any]) -> Dict[str, Any]:
    """Return a deep copy only when both non-semantic gates pass."""

    assessment = assess_scene_writer_integration_contract(result, run_id=run_id, fixture_contract=fixture_contract)
    diagnostics = assessment["structural_gate"]["diagnostics"] + assessment["state_token_gate"]["diagnostics"]
    if diagnostics:
        raise SceneWriterIntegrationContractError(diagnostics)
    return copy.deepcopy(dict(result))


def scene_writer_contract_schema(*, run_id: str, fixture_contract: Mapping[str, Any]) -> Dict[str, Any]:
    """A promptable schema description without any pre-written creative scene text."""

    scene_contract = build_scene_id_contract(fixture_contract)
    state_contract = build_scene_writer_state_projection(fixture_contract)
    field = state_field_name(state_contract)
    return {
        "scene_id_contract": scene_contract,
        "state_field_contract": state_contract,
        "scene_packages": [
            {
                "scene_id": "one exact full machine token from scene_id_contract.ordered_scene_ids, in that order",
                "content": "normal zh-CN scene material only",
                "structural_deliverable": {name: "minimum sufficient zh-CN evidence" for name in STRUCTURAL_FIELD_NAMES},
                "state_evidence": {
                    "entity_identity": tracked_entity_ids(state_contract),
                    "entity_custody": "zh-CN traceable custody description",
                    "knowledge_holders": ["zh-CN character names"],
                    "reveal_status": "NOT_YET_REVEALED or REVEALED_WITH_EVENT",
                    "relationship_state": "zh-CN state description",
                    field: allowed_machine_tokens(state_contract),
                    "machine_state_display": "normal zh-CN display prose; never an alias for the code",
                    "location_presence": "zh-CN presence description",
                    "authorized_transitions": authorized_transition_tokens(state_contract),
                },
                "source_attribution": {
                    "source_role": "Scene Writer",
                    "source_record_id": f"{run_id}/scene_writer/<scene_id>",
                    "version": CONTRACT_VERSION,
                    "evidence_locator": "scene_packages/<scene_id>",
                },
                "evidence_locator": "scene_packages/<scene_id>",
            }
        ]
    }
