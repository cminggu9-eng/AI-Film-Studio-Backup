"""Minimal cross-role State & Evidence Envelope.

This transport contract is deliberately provider-free and role-neutral. It
validates preservation only: it never fills a field, translates a canonical
token, or decides a creative or continuity outcome.
"""

from __future__ import annotations

import copy
import json
from typing import Any, Dict, Mapping


ABSENT = "ABSENT"

ENVELOPE_FIELDS = (
    "source_role",
    "source_record_id",
    "version",
    "timestamp",
    "intended_recipient",
    "handoff_reason",
    "canon_assignment_locks",
    "prohibited_changes",
    "canonical_mode",
    "primary_state_or_outcome",
    "flags",
    "handoffs",
    "required_outcome",
    "unresolved_decisions",
    "relevant_prior_state",
    "current_state",
    "proposed_state",
    "knowledge_timing",
    "relationship_state",
    "visual_state",
    "authority_source",
    "evidence_locator",
)

_REQUIRED_TEXT_FIELDS = {
    "source_role",
    "source_record_id",
    "version",
    "timestamp",
    "intended_recipient",
    "handoff_reason",
    "authority_source",
    "evidence_locator",
}

_TEXT_OR_ABSENT_FIELDS = {"canonical_mode", "primary_state_or_outcome"}
_LIST_OR_ABSENT_FIELDS = {
    "canon_assignment_locks",
    "prohibited_changes",
    "flags",
    "handoffs",
    "unresolved_decisions",
}
_VALUE_OR_ABSENT_FIELDS = {
    "required_outcome",
    "relevant_prior_state",
    "current_state",
    "proposed_state",
    "knowledge_timing",
    "relationship_state",
    "visual_state",
}


class StateEvidenceContractError(ValueError):
    """Raised when a transport packet would hide absence or change structure."""


def _is_json_safe(value: Any) -> bool:
    try:
        json.dumps(value, ensure_ascii=False)
    except (TypeError, ValueError):
        return False
    return True


def _require_text(value: Any, field: str) -> None:
    if not isinstance(value, str) or not value.strip() or value == ABSENT:
        raise StateEvidenceContractError(f"{field} must be a supplied non-empty string, not ABSENT")


def _validate_list_or_absent(value: Any, field: str) -> None:
    if value == ABSENT:
        return
    if not isinstance(value, list):
        raise StateEvidenceContractError(f"{field} must be a list or ABSENT")
    if not _is_json_safe(value):
        raise StateEvidenceContractError(f"{field} must be JSON-serializable")


def _validate_value_or_absent(value: Any, field: str) -> None:
    if value == ABSENT:
        return
    if value is None:
        raise StateEvidenceContractError(f"{field} uses null; absence must be represented exactly as ABSENT")
    if not _is_json_safe(value):
        raise StateEvidenceContractError(f"{field} must be JSON-serializable")


def validate_state_evidence_envelope(envelope: Mapping[str, Any]) -> Dict[str, Any]:
    """Return an exact deep copy after lossless contract validation.

    The caller must explicitly supply every field. A missing upstream value is
    represented by the literal ABSENT and remains ABSENT in the returned copy.
    """

    if not isinstance(envelope, Mapping):
        raise StateEvidenceContractError("State & Evidence Envelope must be an object")
    actual_fields = set(envelope)
    expected_fields = set(ENVELOPE_FIELDS)
    if actual_fields != expected_fields:
        missing = sorted(expected_fields - actual_fields)
        unknown = sorted(actual_fields - expected_fields)
        detail = []
        if missing:
            detail.append("missing: " + ", ".join(missing))
        if unknown:
            detail.append("unknown: " + ", ".join(unknown))
        raise StateEvidenceContractError("Envelope fields must be exact; " + "; ".join(detail))
    if not _is_json_safe(envelope):
        raise StateEvidenceContractError("State & Evidence Envelope must be JSON-serializable")
    for field in _REQUIRED_TEXT_FIELDS:
        _require_text(envelope[field], field)
    for field in _TEXT_OR_ABSENT_FIELDS:
        value = envelope[field]
        if value != ABSENT and (not isinstance(value, str) or not value.strip()):
            raise StateEvidenceContractError(f"{field} must be an exact non-empty token or ABSENT")
    for field in _LIST_OR_ABSENT_FIELDS:
        _validate_list_or_absent(envelope[field], field)
    for field in _VALUE_OR_ABSENT_FIELDS:
        _validate_value_or_absent(envelope[field], field)
    return copy.deepcopy(dict(envelope))
