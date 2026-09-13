"""Showrunner-only separation of semantic payload and E2E transport slots.

This adapter has one lawful deterministic action: at the Showrunner-to-Scene
Writer boundary it can represent the absent, Scene-Writer-owned package slot
as the integration sentinel ``ABSENT``. It cannot supply a Showrunner fact,
derive a semantic value, translate a token, or overwrite an existing package.
"""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from typing import Any, Dict, Mapping


ABSENT = "ABSENT"

# These fields are emitted by the Showrunner role and must be present before
# integration is allowed to add any transport field.
SHOWRUNNER_ROLE_OWNED_FIELDS = frozenset(
    {
        "primary_state_or_outcome",
        "flags",
        "handoffs",
        "canon_assignment_locks",
        "prohibited_changes",
        "required_outcome",
        "unresolved_decisions",
        "state_evidence",
        "content",
    }
)

# This field is part of the generic E2E result schema, but its semantic content
# can only be owned by Scene Writer. It is not a Showrunner semantic field.
SHOWRUNNER_TRANSPORT_OWNED_FIELDS = frozenset({"scene_packages"})

SHOWRUNNER_STATUS_TOKENS = frozenset({"INFO", "WARNING", "BLOCKED", "PASS"})
STATE_EVIDENCE_FIELDS = frozenset(
    {
        "relevant_prior_state",
        "current_state",
        "proposed_state",
        "knowledge_timing",
        "relationship_state",
        "visual_state",
    }
)


class ShowrunnerRolePayloadError(ValueError):
    """A required Showrunner-owned semantic payload field is absent or invalid."""


class ShowrunnerTransportHydrationError(ValueError):
    """The adapter cannot lawfully represent the transport slot as absent."""


@dataclass(frozen=True)
class ShowrunnerTransportHydration:
    """Hydrated result plus explicit field-origin evidence."""

    payload: Dict[str, Any]
    inserted_transport_fields: tuple[str, ...]
    transport_field_origins: Dict[str, str]

    def evidence_record(self) -> Dict[str, Any]:
        return {
            "adapter": "Showrunner Transport Ownership Separation V0.1",
            "inserted_transport_fields": list(self.inserted_transport_fields),
            "transport_field_origins": copy.deepcopy(self.transport_field_origins),
            "semantic_mutation": 0,
            "canonical_token_mutation": 0,
        }


def _is_json_safe(value: Any) -> bool:
    try:
        json.dumps(value, ensure_ascii=False)
    except (TypeError, ValueError):
        return False
    return True


def _require_nonempty_text_list(value: Any, field: str) -> None:
    if not isinstance(value, list) or not value or any(not isinstance(item, str) or not item.strip() for item in value):
        raise ShowrunnerRolePayloadError(f"Showrunner role-owned {field} must be a non-empty string list")


def _validate_state_evidence(value: Any) -> None:
    if not isinstance(value, Mapping) or set(value) != STATE_EVIDENCE_FIELDS:
        raise ShowrunnerRolePayloadError("Showrunner role-owned state_evidence must contain the exact six supplied dimensions")
    if any(item is None for item in value.values()):
        raise ShowrunnerRolePayloadError("Showrunner role-owned state_evidence must not use null")
    if not _is_json_safe(value):
        raise ShowrunnerRolePayloadError("Showrunner role-owned state_evidence must be JSON-safe")


def validate_showrunner_role_owned_payload(payload: Mapping[str, Any]) -> Dict[str, Any]:
    """Validate role-owned fields before transport hydration.

    ``scene_packages`` may be absent or present because it is a transport-owned
    slot. Every other field is exact and role-owned; missing values stay
    failures and cannot be inferred from the Showrunner prose.
    """

    if not isinstance(payload, Mapping):
        raise ShowrunnerRolePayloadError("Showrunner provider response must be an object")
    actual = set(payload)
    missing = SHOWRUNNER_ROLE_OWNED_FIELDS - actual
    unknown = actual - SHOWRUNNER_ROLE_OWNED_FIELDS - SHOWRUNNER_TRANSPORT_OWNED_FIELDS
    if missing or unknown:
        details: list[str] = []
        if missing:
            details.append("missing role-owned: " + ", ".join(sorted(missing)))
        if unknown:
            details.append("unknown: " + ", ".join(sorted(unknown)))
        raise ShowrunnerRolePayloadError("Showrunner role-owned payload fields are not exact; " + "; ".join(details))
    if payload["primary_state_or_outcome"] not in SHOWRUNNER_STATUS_TOKENS:
        raise ShowrunnerRolePayloadError("Showrunner primary state must be an exact canonical STATUS token")
    if payload["flags"] != ABSENT or payload["handoffs"] != ABSENT:
        raise ShowrunnerRolePayloadError("Showrunner has no canonical flags or handoffs; both role-owned values must be ABSENT")
    _require_nonempty_text_list(payload["canon_assignment_locks"], "canon_assignment_locks")
    _require_nonempty_text_list(payload["prohibited_changes"], "prohibited_changes")
    if payload["unresolved_decisions"] != ABSENT and not isinstance(payload["unresolved_decisions"], list):
        raise ShowrunnerRolePayloadError("Showrunner role-owned unresolved_decisions must be a list or ABSENT")
    if not isinstance(payload["content"], str) or not payload["content"].strip():
        raise ShowrunnerRolePayloadError("Showrunner role-owned content must be non-empty")
    _validate_state_evidence(payload["state_evidence"])
    if not _is_json_safe(payload):
        raise ShowrunnerRolePayloadError("Showrunner role-owned payload must be JSON-safe")
    return copy.deepcopy(dict(payload))


def hydrate_showrunner_transport(
    role_payload: Mapping[str, Any],
    *,
    downstream_scene_writer_artifact_exists: bool,
) -> ShowrunnerTransportHydration:
    """Add only the lawful absent Scene Writer package transport slot.

    The four conditions for a transport absence sentinel are enforced here:
    the field is transport-owned, Showrunner cannot own its semantic content,
    no downstream artifact exists, and the absence is determined by the
    boundary state rather than by creative inference.
    """

    result = validate_showrunner_role_owned_payload(role_payload)
    if "scene_packages" in result:
        return ShowrunnerTransportHydration(
            payload=result,
            inserted_transport_fields=(),
            transport_field_origins={"scene_packages": "PROVIDER_SUPPLIED_TRANSPORT_SLOT_PRESERVED"},
        )
    if downstream_scene_writer_artifact_exists:
        raise ShowrunnerTransportHydrationError(
            "Cannot hydrate scene_packages as ABSENT after a downstream Scene Writer artifact exists"
        )
    result["scene_packages"] = ABSENT
    return ShowrunnerTransportHydration(
        payload=result,
        inserted_transport_fields=("scene_packages",),
        transport_field_origins={"scene_packages": "INTEGRATION_TRANSPORT_ABSENCE_SENTINEL"},
    )
