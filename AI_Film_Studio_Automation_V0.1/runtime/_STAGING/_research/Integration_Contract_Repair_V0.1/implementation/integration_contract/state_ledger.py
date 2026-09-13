"""Run-local append-only E2E state ledger.

The ledger keeps caller-supplied evidence for one run. It has no database,
network, RAG, Canon-memory, or historical-record mutation behavior.
"""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from typing import Any, Dict, Mapping

from .state_evidence import ABSENT, StateEvidenceContractError, validate_state_evidence_envelope


class StateLedgerError(ValueError):
    """Raised for an invalid local evidence record or comparison request."""


@dataclass(frozen=True)
class LedgerEntry:
    entry_id: str
    sequence: int
    envelope: Dict[str, Any]
    state_snapshot: Dict[str, Any]


class E2EStateLedger:
    """Append evidence only; Continuity may consume comparison inputs, not edit them."""

    def __init__(self, *, run_id: str) -> None:
        if not isinstance(run_id, str) or not run_id.strip():
            raise StateLedgerError("run_id is required for a run-local ledger")
        self.run_id = run_id
        self._entries: list[LedgerEntry] = []

    @staticmethod
    def _copy_snapshot(state_snapshot: Mapping[str, Any]) -> Dict[str, Any]:
        if not isinstance(state_snapshot, Mapping):
            raise StateLedgerError("state_snapshot must be an object supplied by the source")
        try:
            json.dumps(state_snapshot, ensure_ascii=False)
        except (TypeError, ValueError) as exc:
            raise StateLedgerError("state_snapshot must be JSON-serializable") from exc
        return copy.deepcopy(dict(state_snapshot))

    def append(self, *, envelope: Mapping[str, Any], state_snapshot: Mapping[str, Any]) -> LedgerEntry:
        """Append one supplied record without deriving, repairing, or replacing state."""

        try:
            copied_envelope = validate_state_evidence_envelope(envelope)
        except StateEvidenceContractError as exc:
            raise StateLedgerError(str(exc)) from exc
        copied_snapshot = self._copy_snapshot(state_snapshot)
        sequence = len(self._entries) + 1
        entry = LedgerEntry(
            entry_id=f"{self.run_id}:{sequence:03d}",
            sequence=sequence,
            envelope=copied_envelope,
            state_snapshot=copied_snapshot,
        )
        self._entries.append(entry)
        return copy.deepcopy(entry)

    def entries(self) -> tuple[LedgerEntry, ...]:
        """Return copies so callers cannot mutate ledger history."""

        return tuple(copy.deepcopy(entry) for entry in self._entries)

    def _entry(self, entry_id: str) -> LedgerEntry:
        for entry in self._entries:
            if entry.entry_id == entry_id:
                return entry
        raise StateLedgerError(f"Unknown ledger entry: {entry_id}")

    def comparison_input(self, *, dimension: str, prior_entry_id: str, current_entry_id: str) -> Dict[str, Any]:
        """Create evidence for Continuity comparison without making a continuity decision."""

        if not isinstance(dimension, str) or not dimension.strip():
            raise StateLedgerError("dimension is required")
        prior = self._entry(prior_entry_id)
        current = self._entry(current_entry_id)
        prior_value = prior.state_snapshot.get(dimension, ABSENT)
        current_value = current.state_snapshot.get(dimension, ABSENT)
        packet: Dict[str, Any] = {
            "dimension": dimension,
            "prior_entry_id": prior.entry_id,
            "current_entry_id": current.entry_id,
            "prior_value": copy.deepcopy(prior_value),
            "current_value": copy.deepcopy(current_value),
            "prior_authority_source": prior.envelope["authority_source"],
            "current_authority_source": current.envelope["authority_source"],
            "prior_evidence_locator": prior.envelope["evidence_locator"],
            "current_evidence_locator": current.envelope["evidence_locator"],
            "role_decision": "NOT_MADE",
        }
        if prior_value == ABSENT or current_value == ABSENT:
            return {**packet, "comparison_ready": False, "reason": "STATE_ABSENT"}
        return {**packet, "comparison_ready": True, "reason": "EVIDENCE_SUPPLIED"}
