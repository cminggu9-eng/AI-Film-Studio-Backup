"""Runtime-owned bounded completion budgets; no canonical role semantics live here."""
from __future__ import annotations
from typing import Any, Dict

POLICY_ID = "ROLE_RESPONSE_BUDGET_POLICY_V0.1"
POLICY_VERSION = "V0.1"
SHOWRUNNER_MAX_COMPLETION_TOKENS = 4500
_BUDGETS = {"showrunner": SHOWRUNNER_MAX_COMPLETION_TOKENS, "scene_writer": 5000, "director": 3500, "character_acting": 3500, "art_director": 3500, "continuity": 3500, "shared_qa": 3500}

def role_completion_budget(role_key: str) -> int:
    try: return _BUDGETS[role_key]
    except KeyError as exc: raise ValueError(f"No bounded completion-budget policy for role: {role_key}") from exc

def budget_policy_record(role_key: str) -> Dict[str, Any]:
    budget = role_completion_budget(role_key)
    return {"policy_id": POLICY_ID, "policy_version": POLICY_VERSION, "role_key": role_key, "selected_max_tokens": budget, "bounded": True, "upper_bound_rationale": "role-specific fixed execution cap; no dynamic continuation or retry"}
