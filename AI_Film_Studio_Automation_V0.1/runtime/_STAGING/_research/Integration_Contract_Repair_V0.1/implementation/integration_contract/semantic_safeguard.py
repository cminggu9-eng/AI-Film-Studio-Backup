"""Provider-free two-layer Integration semantic safeguard.

It protects supplied evidence and routes findings. It never calls a model,
rewrites creative output, or replaces role-level canonical states.
"""

from __future__ import annotations

import copy
import hashlib
import json
from typing import Any, Dict, Mapping

from .state_evidence import ABSENT, validate_state_evidence_envelope
from .state_ledger import E2EStateLedger
from .semantic_alignment import resolved_identity_match
from .state_phase import StatePhaseContractError, phase_scoped_required_state_value


INTEGRATION_GATE_LABELS = ("PASS", "FLAG", "BLOCK", "HANDOFF")
ASSERTION_FIELDS = (
    "id",
    "rule",
    "value",
    "expected",
    "authority_source",
    "evidence_locator",
    "authorized_transition",
    "semantic_review_required",
)


class SemanticSafeguardContractError(ValueError):
    """Raised when a would-be safeguard input lacks attributable evidence."""


def _hash_creative_output(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _assertion_copy(assertion: Mapping[str, Any]) -> Dict[str, Any]:
    if not isinstance(assertion, Mapping):
        raise SemanticSafeguardContractError("Each assertion must be an object")
    if set(assertion) != set(ASSERTION_FIELDS):
        raise SemanticSafeguardContractError("Each assertion must contain the exact safeguard assertion fields")
    if not isinstance(assertion["id"], str) or not assertion["id"].strip():
        raise SemanticSafeguardContractError("Assertion id is required")
    if not isinstance(assertion["rule"], str) or not assertion["rule"].strip():
        raise SemanticSafeguardContractError("Assertion rule is required")
    if not isinstance(assertion["authorized_transition"], bool):
        raise SemanticSafeguardContractError("authorized_transition must be boolean")
    if not isinstance(assertion["semantic_review_required"], bool):
        raise SemanticSafeguardContractError("semantic_review_required must be boolean")
    try:
        json.dumps(assertion, ensure_ascii=False)
    except (TypeError, ValueError) as exc:
        raise SemanticSafeguardContractError("Assertion must be JSON-serializable") from exc
    return copy.deepcopy(dict(assertion))


def _finding(assertion: Mapping[str, Any], label: str, code: str, detail: str) -> Dict[str, str]:
    return {
        "label": label,
        "code": code,
        "assertion_id": str(assertion["id"]),
        "detail": detail,
        "authority_source": str(assertion["authority_source"]),
        "evidence_locator": str(assertion["evidence_locator"]),
    }


def _layer_a_findings(assertions: list[Dict[str, Any]]) -> list[Dict[str, str]]:
    findings: list[Dict[str, str]] = []
    for assertion in assertions:
        rule = assertion["rule"]
        value = assertion["value"]
        expected = assertion["expected"]
        authority = assertion["authority_source"]
        locator = assertion["evidence_locator"]
        if rule != "UNKNOWN_STATE" and (authority == ABSENT or locator == ABSENT):
            findings.append(_finding(assertion, "BLOCK", "EVIDENCE_OR_AUTHORITY_ABSENT", "A material assertion lacks authority source or evidence locator."))
            continue
        if rule == "PROP_EQUALS" and not resolved_identity_match(value, expected):
            findings.append(_finding(assertion, "BLOCK", "REQUIRED_PROP_MISMATCH", "Required prop identity differs from supplied evidence."))
        elif rule == "CUSTODY_TRACKED" and value == ABSENT:
            findings.append(_finding(assertion, "BLOCK", "CUSTODY_ABSENT", "Required prop custody is not attributable."))
        elif rule == "KNOWLEDGE_NOT_BEFORE":
            if not isinstance(value, Mapping) or not isinstance(expected, Mapping):
                findings.append(_finding(assertion, "BLOCK", "KNOWLEDGE_TIMING_UNATTRIBUTABLE", "Knowledge timing requires supplied observed and authorized positions."))
            elif value.get("observed_at") < expected.get("authorized_at"):
                findings.append(_finding(assertion, "BLOCK", "KNOWLEDGE_TIMING_EARLY", "Knowledge appears before its supplied authorization point."))
        elif rule == "UNSUPPORTED_NEW_FACT" and authority == ABSENT:
            findings.append(_finding(assertion, "BLOCK", "UNSUPPORTED_NEW_FACT", "Story-relevant new fact has no supplied authority."))
        elif rule == "REQUIRED_STATE":
            try:
                selected_value = phase_scoped_required_state_value(value)
            except StatePhaseContractError as exc:
                findings.append(_finding(assertion, "BLOCK", "REQUIRED_STATE_PHASE_SOURCE_FAILURE", str(exc)))
            else:
                if selected_value != expected:
                    findings.append(_finding(assertion, "BLOCK", "REQUIRED_STATE_MISMATCH", "Required state does not match supplied state evidence."))
        elif rule == "AUTHORIZED_TRANSITION":
            classification = value.get("machine_classification") if isinstance(value, Mapping) else None
            if not assertion["authorized_transition"]:
                findings.append(_finding(assertion, "BLOCK", "UNAUTHORIZED_STATE_CHANGE", "State change has no supplied authorization."))
            elif isinstance(classification, Mapping) and classification.get("AUTHORIZED") is not True:
                findings.append(_finding(assertion, "BLOCK", "UNAUTHORIZED_STATE_CHANGE", "Shared transition authority did not authorize the change."))
            elif isinstance(classification, Mapping) and classification.get("OCCURRED") is not True:
                findings.append(_finding(assertion, "BLOCK", "REQUIRED_TRANSITION_NOT_OCCURRED", "Authorization exists but no scene-local occurrence was supplied."))
            elif isinstance(classification, Mapping) and classification.get("OBSERVED") is not True:
                findings.append(_finding(assertion, "BLOCK", "TRANSITION_NOT_OBSERVED", "Occurrence lacks attributable scene-local observation evidence."))
        elif rule == "RELATIONSHIP_NOT_AUTOMATIC" and str(value).upper() == "RECONCILED" and not assertion["authorized_transition"]:
            findings.append(_finding(assertion, "BLOCK", "UNAUTHORIZED_RELATIONSHIP_UPGRADE", "Relationship was automatically upgraded without authority."))
        elif rule == "UNKNOWN_STATE" and value == ABSENT:
            findings.append(_finding(assertion, "FLAG", "STATE_REMAINS_ABSENT", "Unknown state is routed as absent evidence, not classified as contradiction."))
    return findings


def _layer_b_review_contract(assertions: list[Dict[str, Any]], creative_output: Any) -> Dict[str, Any]:
    candidates = [item["id"] for item in assertions if item["semantic_review_required"]]
    return {
        "layer": "B",
        "independent_review_required": bool(candidates),
        "review_candidates": candidates,
        "allowed_labels": list(INTEGRATION_GATE_LABELS),
        "provider_execution": "NOT_AUTHORIZED",
        "creative_output_sha256": _hash_creative_output(creative_output),
        "review_status": "HANDOFF" if candidates else "PASS",
    }


def evaluate_semantic_safeguard(
    *,
    envelope: Mapping[str, Any],
    ledger: E2EStateLedger,
    creative_output: Any,
    assertions: list[Mapping[str, Any]],
    legacy_verifier_result: str = ABSENT,
    legacy_verifier_only: bool = False,
) -> Dict[str, Any]:
    """Evaluate evidence contracts and prepare independent-review work only.

    The returned report intentionally omits creative_output. The input object is
    not modified, so the safeguard cannot become a rewriting path.
    """

    copied_envelope = validate_state_evidence_envelope(envelope)
    if not isinstance(ledger, E2EStateLedger) or not ledger.entries():
        raise SemanticSafeguardContractError("A non-empty run-local State Ledger is required")
    if copied_envelope["canon_assignment_locks"] == ABSENT:
        raise SemanticSafeguardContractError("canon_assignment_locks must remain attributable for safeguard evaluation")
    copied_assertions = [_assertion_copy(item) for item in assertions]
    findings = _layer_a_findings(copied_assertions)
    if legacy_verifier_only:
        synthetic_assertion = {
            "id": "LEGACY-VERIFIER-SOLE-GATE",
            "rule": "LEGACY_SUPPLEMENTAL_ONLY",
            "value": legacy_verifier_result,
            "expected": ABSENT,
            "authority_source": copied_envelope["authority_source"],
            "evidence_locator": copied_envelope["evidence_locator"],
            "authorized_transition": False,
            "semantic_review_required": True,
        }
        findings.append(_finding(synthetic_assertion, "BLOCK", "LEGACY_VERIFIER_NOT_SUFFICIENT", "Scene Writer legacy verifier may be supplemental only."))
    layer_b = _layer_b_review_contract(copied_assertions, creative_output)
    if any(item["label"] == "BLOCK" for item in findings):
        decision = "BLOCK"
    elif layer_b["review_status"] == "HANDOFF":
        decision = "HANDOFF"
    elif any(item["label"] == "FLAG" for item in findings):
        decision = "FLAG"
    else:
        decision = "PASS"
    return {
        "integration_decision": decision,
        "allowed_labels": list(INTEGRATION_GATE_LABELS),
        "layer_a": {
            "name": "Deterministic Evidence / Contract Gate",
            "findings": findings,
            "source_role": copied_envelope["source_role"],
            "source_record_id": copied_envelope["source_record_id"],
            "version": copied_envelope["version"],
            "locks": copy.deepcopy(copied_envelope["canon_assignment_locks"]),
            "current_state": copy.deepcopy(copied_envelope["current_state"]),
            "authority_source": copied_envelope["authority_source"],
            "evidence_locator": copied_envelope["evidence_locator"],
        },
        "layer_b": layer_b,
        "legacy_verifier_result": legacy_verifier_result,
        "legacy_verifier_role": "SUPPLEMENTAL_SIGNAL_ONLY",
        "creative_output_sha256": _hash_creative_output(creative_output),
        "creative_output_rewrite": "PROHIBITED",
    }
