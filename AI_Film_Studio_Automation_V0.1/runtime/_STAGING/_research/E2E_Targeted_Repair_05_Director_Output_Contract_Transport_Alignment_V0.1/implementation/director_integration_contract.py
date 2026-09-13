"""Canonical Director semantic-field contract for integration validation.

Machine field IDs are stable integration identifiers. Their display headings
are the exact canonical Director output tokens; this module never normalizes,
renames, or repairs a heading in Provider output.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Mapping


ABSENT = "ABSENT"

DIRECTOR_CANONICAL_MODES = ("PLAN", "REVISE", "DIAGNOSE")
DIRECTOR_PRIMARY_STATES = (
    "DIRECTION_PLAN_PRODUCED",
    "DIRECTION_PLAN_REVISED",
    "NO_MATERIAL_DIRECTION_CHANGE",
    "NEEDS_CONTEXT",
    "UPSTREAM_DECISION_REQUIRED",
    "OUT_OF_SCOPE_HANDOFF",
)

# Source: Director canonical SKILL.md, Output section, exact heading order.
DIRECTOR_SEMANTIC_FIELDS = (
    ("directorial_intent", "DIRECTORIAL INTENT"),
    ("staging_blocking", "STAGING / BLOCKING"),
    ("audience_information", "AUDIENCE INFORMATION"),
    ("spatial_geography", "SPATIAL GEOGRAPHY"),
    ("camera_coverage_intent", "CAMERA / COVERAGE INTENT"),
    ("rhythm_transition_intent", "RHYTHM / TRANSITION INTENT"),
    ("production_burden", "PRODUCTION BURDEN"),
    ("handoffs_unresolved_issues", "HANDOFFS / UNRESOLVED ISSUES"),
)
DIRECTOR_CANONICAL_OUTPUT_HEADINGS = tuple(heading for _, heading in DIRECTOR_SEMANTIC_FIELDS)


class DirectorIntegrationContractError(ValueError):
    """Director output is structurally non-conformant; no repair is performed."""


@dataclass(frozen=True)
class DirectorSemanticInspection:
    """Presence and canonical-order evidence without transforming Provider text."""

    field_positions: Dict[str, int]
    missing_field_ids: tuple[str, ...]
    canonical_order: bool

    @property
    def semantic_fields_present(self) -> bool:
        return not self.missing_field_ids


def inspect_director_semantic_fields(content: Any) -> DirectorSemanticInspection:
    """Locate only exact canonical heading lines and report their order.

    This is not a tolerant parser. Case, whitespace, slash form, and heading
    order are all retained as emitted. A different display form is simply not
    an instance of the canonical heading token.
    """

    if not isinstance(content, str) or not content.strip():
        raise DirectorIntegrationContractError("Director content must be non-empty text")
    heading_positions: Dict[str, int] = {}
    for line_number, line in enumerate(content.splitlines()):
        if line in DIRECTOR_CANONICAL_OUTPUT_HEADINGS and line not in heading_positions:
            heading_positions[line] = line_number
    field_positions = {
        field_id: heading_positions[heading]
        for field_id, heading in DIRECTOR_SEMANTIC_FIELDS
        if heading in heading_positions
    }
    missing = tuple(field_id for field_id, heading in DIRECTOR_SEMANTIC_FIELDS if heading not in heading_positions)
    ordered_positions = [field_positions[field_id] for field_id, _ in DIRECTOR_SEMANTIC_FIELDS if field_id in field_positions]
    return DirectorSemanticInspection(
        field_positions=field_positions,
        missing_field_ids=missing,
        canonical_order=not missing and ordered_positions == sorted(ordered_positions),
    )


def validate_director_integration_output(output: Mapping[str, Any]) -> Dict[str, Any]:
    """Validate the Director contract without altering semantic content."""

    if not isinstance(output, Mapping):
        raise DirectorIntegrationContractError("Director integration output must be an object")
    primary_state = output.get("primary_state_or_outcome")
    if primary_state not in DIRECTOR_PRIMARY_STATES:
        raise DirectorIntegrationContractError("Director primary state is not an exact canonical token")
    if output.get("flags") != ABSENT or output.get("handoffs") != ABSENT:
        raise DirectorIntegrationContractError("Director has no defined canonical flag/handoff tokens; transport values must remain ABSENT")
    inspection = inspect_director_semantic_fields(output.get("content"))
    if inspection.missing_field_ids:
        raise DirectorIntegrationContractError(
            "Director required semantic field headings missing: " + ", ".join(inspection.missing_field_ids)
        )
    if not inspection.canonical_order:
        raise DirectorIntegrationContractError("Director canonical output headings are present but not in canonical order")
    return {
        "machine_field_ids": [field_id for field_id, _ in DIRECTOR_SEMANTIC_FIELDS],
        "display_headings": list(DIRECTOR_CANONICAL_OUTPUT_HEADINGS),
        "field_positions": dict(inspection.field_positions),
        "semantic_mutation": 0,
        "canonical_token_mutation": 0,
    }
