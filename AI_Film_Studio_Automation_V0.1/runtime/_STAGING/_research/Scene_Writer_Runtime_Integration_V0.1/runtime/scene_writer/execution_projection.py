"""Runtime-only state-aware output projection for canonical Scene Writer execution.

The projection does not interpret or amend the frozen canonical Skill.  It
only describes how an already-lawful canonical decision is represented in the
strict Runtime output transport.
"""

from __future__ import annotations

import copy
from typing import Any, Dict


_STATE_PROJECTIONS: Dict[str, Dict[str, Any]] = {
    "SCENE_CREATED": {
        "valid_modes": ["CREATE"],
        "creative_deliverable": {"required": {"kind": "scene", "content": "non-empty scene"}},
        "required_control_fields": ["primary_state", "flags", "handoffs"],
        "optional_control_fields": [
            "scene_function", "objectives", "resistance", "before_state", "turn", "state_after",
            "entry_rationale", "exit_rationale", "diagnosis_summary", "rule_hits", "audit_metadata",
            "production_burden", "unresolved_issue",
        ],
        "forbidden_non_null_control_fields": [
            "material_rewrite_claimed", "material_missing_context", "upstream_decision_needed", "out_of_scope_boundary",
        ],
    },
    "SCENE_REVISED": {
        "valid_modes": ["REVISE"],
        "creative_deliverable": {"required": {"kind": "revision", "content": "non-empty local revision"}},
        "required_control_fields": ["primary_state", "flags", "handoffs"],
        "optional_control_fields": [
            "scene_function", "objectives", "resistance", "before_state", "turn", "state_after",
            "entry_rationale", "exit_rationale", "diagnosis_summary", "rule_hits", "audit_metadata",
            "production_burden", "unresolved_issue",
        ],
        "forbidden_non_null_control_fields": [
            "material_rewrite_claimed", "material_missing_context", "upstream_decision_needed", "out_of_scope_boundary",
        ],
    },
    "NO_MATERIAL_CHANGE": {
        "valid_modes": ["REVISE", "DIAGNOSE"],
        "creative_deliverable": "required null",
        "required_control_fields": ["primary_state", "flags", "handoffs", "material_rewrite_claimed=false"],
        "optional_control_fields": ["diagnosis_summary", "rule_hits", "audit_metadata", "unresolved_issue"],
        "forbidden_non_null_control_fields": [
            "material_missing_context", "upstream_decision_needed", "out_of_scope_boundary",
        ],
        "mode_specific_requirement": {
            "DIAGNOSE": "diagnosis_summary is required and must diagnose without a replacement scene or revision",
        },
    },
    "NEEDS_CONTEXT": {
        "valid_modes": ["CREATE", "REVISE", "DIAGNOSE"],
        "creative_deliverable": "required null",
        "required_control_fields": [
            "primary_state", "flags", "handoffs",
            "material_missing_context={missing,why_material,target_owner}",
        ],
        "optional_control_fields": ["unresolved_issue", "audit_metadata"],
        "forbidden_non_null_control_fields": [
            "material_rewrite_claimed", "upstream_decision_needed", "out_of_scope_boundary",
        ],
    },
    "UPSTREAM_DECISION_REQUIRED": {
        "valid_modes": ["CREATE", "REVISE", "DIAGNOSE"],
        "creative_deliverable": "required null",
        "required_control_fields": [
            "primary_state", "flags including UPSTREAM_HANDOFF_REQUIRED", "handoffs with at least one lawful packet",
            "upstream_decision_needed",
        ],
        "optional_control_fields": ["unresolved_issue", "audit_metadata"],
        "forbidden_non_null_control_fields": [
            "material_rewrite_claimed", "material_missing_context", "out_of_scope_boundary",
        ],
    },
    "REQUEST_OUT_OF_SCOPE": {
        "valid_modes": ["CREATE", "REVISE", "DIAGNOSE"],
        "creative_deliverable": "required null",
        "required_control_fields": ["primary_state", "flags", "handoffs", "out_of_scope_boundary"],
        "optional_control_fields": ["unresolved_issue", "audit_metadata"],
        "forbidden_non_null_control_fields": [
            "material_rewrite_claimed", "material_missing_context", "upstream_decision_needed",
        ],
    },
}


def state_projection_matrix() -> Dict[str, Dict[str, Any]]:
    """Return a defensive copy of all six canonical Runtime projections."""
    return copy.deepcopy(_STATE_PROJECTIONS)


def execution_projection_for_mode(requested_mode: str) -> Dict[str, Any]:
    """Return only the legal transport shapes for one exact Runtime mode."""
    if requested_mode not in {"CREATE", "REVISE", "DIAGNOSE"}:
        raise ValueError("requested_mode must be an exact Runtime mode token")
    states = {
        state: details
        for state, details in _STATE_PROJECTIONS.items()
        if requested_mode in details["valid_modes"]
    }
    return {
        "projection_identity": "SCENE_WRITER_RUNTIME_MODE_STATE_PROJECTION_V0.1",
        "requested_mode": requested_mode,
        "permitted_primary_states": list(states),
        "states": copy.deepcopy(states),
        "serialization_rules": [
            "Return exactly creative_deliverable and control_data at the top level.",
            "Select one lawful primary state; a mode never forces a creative scene or revision.",
            "Omit fields that are not required or applicable; never use an empty string as a placeholder.",
            "Canonical mode, primary-state, flag, and handoff-owner tokens remain exact English tokens.",
        ],
    }

