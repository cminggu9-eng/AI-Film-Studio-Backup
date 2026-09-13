"""Authoritative Art Director integration machine contract.

The canonical Art Director Skill permits minimum-sufficient, untamplated
records. This module validates only the integration machine contract, exact
canonical tokens, lawful absence representations, and transport-owned
authority boundaries. It does not score prose richness, search for required
words, extract headings, or synthesize missing content.
"""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from typing import Any, Dict, Mapping


ABSENT = "ABSENT"

ART_DIRECTOR_CANONICAL_MODES = ("DESIGN", "REVISE", "DIAGNOSE")
ART_DIRECTOR_PRIMARY_STATES = (
    "CONTEXT_RESOLUTION_REQUIRED",
    "CROSS_ROLE_DECISION_REQUIRED",
    "RESEARCH_DECISION_REQUIRED",
    "PRODUCTION_FEASIBILITY_DECISION_REQUIRED",
    "PARTIAL_OR_DEFERRED_CAPABILITY_LIMIT",
    "DESIGN_RESPONSE_READY",
)

# The canonical Skill's Outputs are selectable records, not display identity.
ART_DIRECTOR_REQUIRED_DISPLAY_HEADINGS: tuple[str, ...] = ()

ART_DIRECTOR_TOP_LEVEL_FIELDS = (
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

ART_DIRECTOR_STATE_FIELDS = (
    "relevant_prior_state",
    "current_state",
    "proposed_state",
    "knowledge_timing",
    "relationship_state",
    "visual_state",
)

ART_DIRECTOR_FAILURE_ALIGNMENT = "INTEGRATION OUTPUT-CONTRACT / VALIDATOR ALIGNMENT FAILURE"
ART_DIRECTOR_FAILURE_MACHINE = "INTEGRATION MACHINE-CONTRACT FAILURE"
ART_DIRECTOR_FAILURE_TOKEN = "CANONICAL TOKEN FAILURE"
ART_DIRECTOR_FAILURE_AUTHORITY = "ART DIRECTOR AUTHORITY-BOUNDARY FAILURE"


class ArtDirectorIntegrationContractError(ValueError):
    """Non-conformance with an attributable integration failure class."""

    def __init__(self, message: str, *, classification: str = ART_DIRECTOR_FAILURE_MACHINE) -> None:
        super().__init__(message)
        self.classification = classification


@dataclass(frozen=True)
class ArtDirectorContractInspection:
    """Machine-contract evidence without semantic mutation or content scoring."""

    content_nonempty: bool
    top_level_fields_exact: bool
    state_fields_exact: bool
    visual_state_representation: str
    unresolved_decisions_representation: str

    @property
    def output_is_permitted(self) -> bool:
        return self.content_nonempty and self.top_level_fields_exact and self.state_fields_exact


def art_director_machine_field_manifest() -> Dict[str, Any]:
    """Return the single manifest shared by prompt, provider schema, and validator."""

    return {
        "contract_version": "ART-DIRECTOR-INTEGRATION-V0.2",
        "output_policy": "MINIMUM_SUFFICIENT_UNTEMPLATED_RECORDS",
        "required_top_level_fields": list(ART_DIRECTOR_TOP_LEVEL_FIELDS),
        "additional_top_level_fields": False,
        "fields": {
            "primary_state_or_outcome": {
                "required": True,
                "type": "string",
                "enum": list(ART_DIRECTOR_PRIMARY_STATES),
            },
            "flags": {"required": True, "const": ABSENT},
            "handoffs": {"required": True, "const": ABSENT},
            "canon_assignment_locks": {"required": True, "type": "array[string]"},
            "prohibited_changes": {"required": True, "type": "array[string]"},
            "required_outcome": {"required": True, "type": "string"},
            "unresolved_decisions": {
                "required": True,
                "type": "array[string] or exact ABSENT",
                "empty_array_allowed": True,
                "semantic_requiredness": "CONDITIONAL",
            },
            "state_evidence": {
                "required": True,
                "type": "object",
                "required_fields": list(ART_DIRECTOR_STATE_FIELDS),
                "additional_fields": False,
                "field_representation": "JSON object or exact ABSENT independently per field",
            },
            "content": {
                "required": True,
                "type": "non-empty string",
                "display_heading_template": False,
                "content_keyword_requirements": [],
            },
            "scene_packages": {"required": True, "const": ABSENT},
        },
        "conditional_content": {
            "production_feasibility": "Only when evidence establishes a real burden or Production decision",
            "unresolved_issue": "Only when a real unresolved owner decision exists",
            "current_visual_state": "Supply when present; exact ABSENT is lawful otherwise",
        },
    }


def art_director_output_schema() -> Dict[str, Any]:
    """Provider-facing non-strict JSON schema projection from the manifest."""

    return {
        "primary_state_or_outcome": f"one exact token from {list(ART_DIRECTOR_PRIMARY_STATES)}",
        "flags": "exact ABSENT",
        "handoffs": "exact ABSENT",
        "canon_assignment_locks": ["copy every received lock exactly"],
        "prohibited_changes": ["copy every received prohibition exactly"],
        "required_outcome": "string, including exact ABSENT when no required outcome exists",
        "unresolved_decisions": "array of non-empty strings (empty allowed) or exact ABSENT",
        "state_evidence": {
            field: "JSON object or exact ABSENT"
            for field in ART_DIRECTOR_STATE_FIELDS
        },
        "content": "non-empty zh-CN minimum-sufficient role deliverable; no fixed headings or required keywords",
        "scene_packages": "exact ABSENT",
    }


def art_director_prompt_contract_instruction() -> str:
    """Prompt instruction derived from the same machine-field manifest."""

    fields = ", ".join(ART_DIRECTOR_TOP_LEVEL_FIELDS)
    states = ", ".join(ART_DIRECTOR_STATE_FIELDS)
    return (
        "ART DIRECTOR MACHINE CONTRACT: Emit exactly these required top-level fields and no others: "
        f"{fields}. State Evidence must contain exactly these required fields: {states}; validate each independently "
        "as a JSON object or exact ABSENT. visual_state may be a JSON object or exact ABSENT. "
        "unresolved_decisions may be a non-empty-string array (including an empty array) or exact ABSENT. "
        "Do not invent an unresolved issue or Production-feasibility content when none is supported. "
        "Normal content is minimum-sufficient and has no mandatory display headings or required keywords."
    )


def art_director_validator_requiredness_manifest() -> Dict[str, Any]:
    """Expose validator requiredness for identity tests and audit reports."""

    return copy.deepcopy(art_director_machine_field_manifest())


def classify_art_director_failure(
    *,
    provider_schema_allows_representation: bool,
    validator_rejected: bool,
    canonical_semantic_violation: bool,
) -> str:
    """Prioritize integration drift over a generic semantic label."""

    if provider_schema_allows_representation and validator_rejected and not canonical_semantic_violation:
        return ART_DIRECTOR_FAILURE_ALIGNMENT
    if canonical_semantic_violation:
        return "ROLE SEMANTIC FAILURE"
    return ART_DIRECTOR_FAILURE_MACHINE


def _is_json_object(value: Any) -> bool:
    if not isinstance(value, Mapping):
        return False
    if any(not isinstance(key, str) for key in value):
        return False
    try:
        json.dumps(value, ensure_ascii=False)
    except (TypeError, ValueError):
        return False
    return True


def _object_or_absent(value: Any) -> bool:
    return value == ABSENT or _is_json_object(value)


def _string_array(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) and bool(item.strip()) for item in value)


def inspect_art_director_contract(output: Any) -> ArtDirectorContractInspection:
    """Inspect structure only; never infer one field from another."""

    if not isinstance(output, Mapping):
        return ArtDirectorContractInspection(False, False, False, "INVALID", "INVALID")
    state = output.get("state_evidence")
    top_exact = set(output) == set(ART_DIRECTOR_TOP_LEVEL_FIELDS)
    state_exact = isinstance(state, Mapping) and set(state) == set(ART_DIRECTOR_STATE_FIELDS)
    visual = state.get("visual_state") if isinstance(state, Mapping) else None
    unresolved = output.get("unresolved_decisions")
    return ArtDirectorContractInspection(
        content_nonempty=isinstance(output.get("content"), str) and bool(output["content"].strip()),
        top_level_fields_exact=top_exact,
        state_fields_exact=state_exact,
        visual_state_representation=("ABSENT" if visual == ABSENT else "OBJECT" if _is_json_object(visual) else "INVALID"),
        unresolved_decisions_representation=(
            "ABSENT" if unresolved == ABSENT else "EMPTY_ARRAY" if unresolved == []
            else "NON_EMPTY_ARRAY" if _string_array(unresolved) else "INVALID"
        ),
    )


# Backward-compatible name retained for Repair06 callers. Its semantics are now
# strictly machine-contract inspection rather than prose-semantic inspection.
inspect_art_director_semantic_fields = inspect_art_director_contract


def validate_art_director_integration_output(output: Mapping[str, Any]) -> Dict[str, Any]:
    """Validate the authoritative machine contract without changing output."""

    if not isinstance(output, Mapping):
        raise ArtDirectorIntegrationContractError("Art Director integration output must be a JSON object")
    if set(output) != set(ART_DIRECTOR_TOP_LEVEL_FIELDS):
        raise ArtDirectorIntegrationContractError("Art Director output fields do not match the exact machine manifest")
    if output["primary_state_or_outcome"] not in ART_DIRECTOR_PRIMARY_STATES:
        raise ArtDirectorIntegrationContractError(
            "Art Director primary state is not an exact canonical token",
            classification=ART_DIRECTOR_FAILURE_TOKEN,
        )
    if output["flags"] != ABSENT or output["handoffs"] != ABSENT:
        raise ArtDirectorIntegrationContractError(
            "Art Director has no canonical flag/handoff transport; both fields must remain exact ABSENT",
            classification=ART_DIRECTOR_FAILURE_AUTHORITY,
        )
    if not _string_array(output["canon_assignment_locks"]):
        raise ArtDirectorIntegrationContractError("canon_assignment_locks must be an array of non-empty strings")
    if not _string_array(output["prohibited_changes"]):
        raise ArtDirectorIntegrationContractError("prohibited_changes must be an array of non-empty strings")
    if not isinstance(output["required_outcome"], str):
        raise ArtDirectorIntegrationContractError("required_outcome must be a string")
    if output["unresolved_decisions"] != ABSENT and not _string_array(output["unresolved_decisions"]):
        raise ArtDirectorIntegrationContractError(
            "unresolved_decisions must be an array of non-empty strings (empty allowed) or exact ABSENT"
        )
    state = output["state_evidence"]
    if not isinstance(state, Mapping) or set(state) != set(ART_DIRECTOR_STATE_FIELDS):
        raise ArtDirectorIntegrationContractError("state_evidence must contain the exact six required machine fields")
    for field in ART_DIRECTOR_STATE_FIELDS:
        if not _object_or_absent(state[field]):
            raise ArtDirectorIntegrationContractError(f"state_evidence.{field} must be a JSON object or exact ABSENT")
    if not isinstance(output["content"], str) or not output["content"].strip():
        raise ArtDirectorIntegrationContractError("Art Director content must be non-empty text")
    if output["scene_packages"] != ABSENT:
        raise ArtDirectorIntegrationContractError(
            "Art Director cannot supply scene_packages",
            classification=ART_DIRECTOR_FAILURE_AUTHORITY,
        )

    inspection = inspect_art_director_contract(output)
    manifest = art_director_machine_field_manifest()
    return {
        "output_policy": manifest["output_policy"],
        "contract_version": manifest["contract_version"],
        "required_display_headings": [],
        "content_nonempty": inspection.content_nonempty,
        "top_level_fields_exact": inspection.top_level_fields_exact,
        "state_fields_exact": inspection.state_fields_exact,
        "visual_state_contract": "OBJECT_OR_EXACT_ABSENT",
        "visual_state_representation": inspection.visual_state_representation,
        "unresolved_decisions_contract": "REQUIRED_FIELD_ARRAY_OR_EXACT_ABSENT_EMPTY_ARRAY_ALLOWED",
        "unresolved_decisions_representation": inspection.unresolved_decisions_representation,
        "conditional_production_feasibility_preserved": True,
        "content_heuristics": [],
        "forbidden_ai_production_tokens": [],
        "required_semantic_fields_present": [],
        "missing_required_semantic_fields": [],
        "prompt_schema_validator_manifest": manifest,
        "semantic_mutation": 0,
        "canonical_token_mutation": 0,
    }
