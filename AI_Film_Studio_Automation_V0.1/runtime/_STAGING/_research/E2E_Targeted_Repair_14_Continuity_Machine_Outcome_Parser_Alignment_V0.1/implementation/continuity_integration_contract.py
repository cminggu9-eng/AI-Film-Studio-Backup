"""Continuity integration contract aligned to canonical machine identity.

The canonical ``primary_state_or_outcome`` field is the sole primary outcome
identity. Display prose is retained as explanatory evidence and is never
searched, translated, or reconstructed to establish a machine result.
"""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from typing import Any, Mapping, Sequence


ABSENT = "ABSENT"
CONTRACT_VERSION = "CONTINUITY-INTEGRATION-V0.2"

CONTINUITY_TRANSPORT_FIELDS = (
    "primary_state_or_outcome",
    "flags",
    "handoffs",
    "canon_assignment_locks",
    "prohibited_changes",
    "required_outcome",
    "unresolved_decisions",
    "state_evidence",
    "content",
    "scene_packages",
)

STATE_EVIDENCE_FIELDS = (
    "relevant_prior_state",
    "current_state",
    "proposed_state",
    "knowledge_timing",
    "relationship_state",
    "visual_state",
)


class ContinuityIntegrationContractError(ValueError):
    """Attributed Continuity integration-contract failure."""

    def __init__(self, classification: str, stage: str, detail: str) -> None:
        super().__init__(detail)
        self.classification = classification
        self.stage = stage
        self.detail = detail


@dataclass(frozen=True)
class ContinuityValidation:
    payload: dict[str, Any]
    evidence: dict[str, Any]


def canonical_outcomes_from_skill_text(skill_text: str) -> tuple[str, ...]:
    """Read exact outcome tokens from the canonical Capability Outcomes table."""

    marker = "## Capability Outcomes"
    if marker not in skill_text:
        raise ContinuityIntegrationContractError(
            "RUNTIME / HARNESS FAILURE",
            "STAGE C: canonical outcome source",
            "canonical Continuity Capability Outcomes section is unavailable",
        )
    section = skill_text.split(marker, 1)[1]
    if "\n## " in section:
        section = section.split("\n## ", 1)[0]
    outcomes: list[str] = []
    for line in section.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        token = cells[0]
        if token == "Outcome" or not token or set(token) <= {"-", ":"}:
            continue
        outcomes.append(token)
    if not outcomes or len(outcomes) != len(set(outcomes)):
        raise ContinuityIntegrationContractError(
            "RUNTIME / HARNESS FAILURE",
            "STAGE C: canonical outcome source",
            "canonical Continuity outcomes are missing or duplicated",
        )
    return tuple(outcomes)


def validate_continuity_non_strict_transport(*, strict_enabled: bool) -> None:
    if strict_enabled:
        raise ContinuityIntegrationContractError(
            "STRICT TRANSPORT AUTHORIZATION FAILURE",
            "STAGE A: transport",
            "Continuity is not an authorized strict role/function pair",
        )


def _ensure_json_safe(value: Any, *, stage: str) -> None:
    try:
        json.dumps(value, ensure_ascii=False, allow_nan=False)
    except (TypeError, ValueError) as exc:
        raise ContinuityIntegrationContractError(
            "TRANSPORT / PARSER CONTRACT FAILURE",
            stage,
            "Continuity payload is not lossless JSON transport",
        ) from exc


def _validate_transport(payload: Mapping[str, Any]) -> None:
    if set(payload) != set(CONTINUITY_TRANSPORT_FIELDS):
        missing = sorted(set(CONTINUITY_TRANSPORT_FIELDS) - set(payload))
        extra = sorted(set(payload) - set(CONTINUITY_TRANSPORT_FIELDS))
        raise ContinuityIntegrationContractError(
            "TRANSPORT / PARSER CONTRACT FAILURE",
            "STAGE A: transport / JSON parse",
            f"Continuity top-level transport fields are not exact; missing={missing}; extra={extra}",
        )
    _ensure_json_safe(payload, stage="STAGE A: transport / JSON parse")


def _validate_machine_fields(payload: Mapping[str, Any]) -> None:
    outcome = payload.get("primary_state_or_outcome")
    if not isinstance(outcome, str) or not outcome:
        raise ContinuityIntegrationContractError(
            "TRANSPORT / PARSER CONTRACT FAILURE",
            "STAGE B: machine-field validation",
            "primary_state_or_outcome must be a non-empty exact machine token",
        )
    for field in ("canon_assignment_locks", "prohibited_changes"):
        value = payload.get(field)
        if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
            raise ContinuityIntegrationContractError(
                "HANDOFF CONTRACT FAILURE",
                "STAGE B: machine-field validation",
                f"{field} must be a string list",
            )
    unresolved = payload.get("unresolved_decisions")
    if unresolved != ABSENT and (
        not isinstance(unresolved, list)
        or any(not isinstance(item, str) or not item for item in unresolved)
    ):
        raise ContinuityIntegrationContractError(
            "HANDOFF CONTRACT FAILURE",
            "STAGE B: machine-field validation",
            "unresolved_decisions must be a string list or exact ABSENT",
        )
    content = payload.get("content")
    if not isinstance(content, str) or not content.strip():
        raise ContinuityIntegrationContractError(
            "ROLE SEMANTIC FAILURE",
            "STAGE B: display evidence presence",
            "Continuity explanatory content is empty",
        )


def _validate_canonical_outcome(payload: Mapping[str, Any], outcomes: Sequence[str]) -> str:
    outcome = payload["primary_state_or_outcome"]
    if outcome not in outcomes:
        raise ContinuityIntegrationContractError(
            "ROLE SEMANTIC FAILURE",
            "STAGE C: canonical outcome validation",
            "primary_state_or_outcome is not one exact case-sensitive canonical Continuity outcome",
        )
    return str(outcome)


def _validate_state_evidence(payload: Mapping[str, Any]) -> dict[str, Any]:
    state = payload.get("state_evidence")
    if not isinstance(state, Mapping):
        raise ContinuityIntegrationContractError(
            "STATE TRANSPORT FAILURE",
            "STAGE D: six-dimension State Evidence validation",
            "state_evidence must be an object",
        )
    if set(state) != set(STATE_EVIDENCE_FIELDS):
        missing = sorted(set(STATE_EVIDENCE_FIELDS) - set(state))
        extra = sorted(set(state) - set(STATE_EVIDENCE_FIELDS))
        raise ContinuityIntegrationContractError(
            "STATE TRANSPORT FAILURE",
            "STAGE D: six-dimension State Evidence validation",
            f"state_evidence dimensions are not exact; missing={missing}; extra={extra}",
        )
    copied = copy.deepcopy(dict(state))
    for field, value in copied.items():
        if value is None:
            raise ContinuityIntegrationContractError(
                "STATE TRANSPORT FAILURE",
                "STAGE D: six-dimension State Evidence validation",
                f"state_evidence.{field} used null instead of exact ABSENT",
            )
        if value != ABSENT and not isinstance(value, Mapping):
            raise ContinuityIntegrationContractError(
                "STATE TRANSPORT FAILURE",
                "STAGE D: six-dimension State Evidence validation",
                f"state_evidence.{field} must be an object or exact ABSENT",
            )
    _ensure_json_safe(copied, stage="STAGE D: six-dimension State Evidence validation")
    return copied


def _validate_authority_boundary(payload: Mapping[str, Any]) -> None:
    for field in ("flags", "handoffs", "scene_packages"):
        if payload.get(field) != ABSENT:
            raise ContinuityIntegrationContractError(
                "HANDOFF CONTRACT FAILURE",
                "STAGE F: authority-boundary validation",
                f"Continuity {field} must remain exact ABSENT in the current integration contract",
            )


def validate_continuity_integration_output(
    output: Mapping[str, Any],
    *,
    canonical_skill_text: str,
) -> ContinuityValidation:
    """Validate Continuity without deriving machine truth from display prose."""

    if not isinstance(output, Mapping):
        raise ContinuityIntegrationContractError(
            "TRANSPORT / PARSER CONTRACT FAILURE",
            "STAGE A: transport / JSON parse",
            "Continuity output must be a JSON object",
        )
    payload = copy.deepcopy(dict(output))
    _validate_transport(payload)
    _validate_machine_fields(payload)
    canonical_outcomes = canonical_outcomes_from_skill_text(canonical_skill_text)
    outcome = _validate_canonical_outcome(payload, canonical_outcomes)
    state = _validate_state_evidence(payload)
    _validate_authority_boundary(payload)
    evidence = {
        "contract_version": CONTRACT_VERSION,
        "stages": {
            "A_transport_json_parse": "PASS",
            "B_machine_field_validation": "PASS",
            "C_canonical_outcome_validation": "PASS",
            "D_six_dimension_state_evidence_validation": "PASS",
            "E_explicit_contract_derived_signal_validation": "NOT_REQUIRED_NO_SEPARATE_MACHINE_SIGNAL_FIELDS",
            "F_authority_boundary_validation": "PASS",
        },
        "machine_identity_source": "primary_state_or_outcome",
        "canonical_outcome": outcome,
        "canonical_outcomes_source": "canonical Continuity SKILL.md Capability Outcomes table",
        "canonical_outcomes": list(canonical_outcomes),
        "state_evidence_fields": list(state),
        "state_representation": "OBJECT_OR_EXACT_ABSENT_PER_DIMENSION",
        "presence_signal": "CONDITIONAL_CANONICAL_REVIEW_DIMENSION_NOT_SEPARATE_MACHINE_FIELD",
        "authorized_change_signal": "CANONICAL_OUTCOME_IDENTITY_NOT_PROSE_DERIVATION",
        "display_prose_machine_source": False,
        "keyword_heuristics": [],
        "semantic_guessing": 0,
        "semantic_mutation": 0,
        "canonical_token_mutation": 0,
        "authority_actions": ["OBSERVE", "COMPARE", "CLASSIFY", "FLAG", "ROUTE"],
    }
    return ContinuityValidation(payload=payload, evidence=evidence)


def classify_continuity_failure(exc: ContinuityIntegrationContractError) -> dict[str, str]:
    """Expose the exact local failure layer without rewriting the result."""

    return {
        "classification": exc.classification,
        "stage": exc.stage,
        "detail": exc.detail,
        "owner": "Continuity Integration Validator",
    }
