"""Bounded Scene Writer response-budget policy for E2E Targeted Repair 02."""

from __future__ import annotations

from typing import Any, Dict

from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter


CONTRACT_VERSION = "0.1"
DELIVERABLE_TYPE = "LARGE_STRUCTURED_DELIVERABLE"
SCENE_COUNT = 3
FAILED_COMPLETION_CAP = 3500
SELECTED_COMPLETION_BUDGET = 5000
LOCAL_POLICY_CEILING = 6000


class ResponseBudgetPreflightError(RuntimeError):
    """A bounded-budget configuration does not satisfy the authorized contract."""


def scene_writer_response_budget_preflight() -> Dict[str, Any]:
    """Return the deterministic, provider-free gate required before a real call."""

    capabilities = DeepSeekProviderAdapter.completion_capabilities()
    provider_ceiling = capabilities.get("provider_documented_max_output_tokens")
    checks = {
        "expected_deliverable_type": DELIVERABLE_TYPE,
        "scenes": SCENE_COUNT,
        "structural_contract_enabled": True,
        "state_contract_enabled": True,
        "selected_completion_budget": SELECTED_COMPLETION_BUDGET,
        "previous_failed_cap": FAILED_COMPLETION_CAP,
        "additional_headroom_tokens": SELECTED_COMPLETION_BUDGET - FAILED_COMPLETION_CAP,
        "additional_headroom_ratio": round((SELECTED_COMPLETION_BUDGET - FAILED_COMPLETION_CAP) / FAILED_COMPLETION_CAP, 6),
        "local_policy_ceiling": LOCAL_POLICY_CEILING,
        "provider_capabilities": capabilities,
        "selected_below_local_policy_ceiling": SELECTED_COMPLETION_BUDGET <= LOCAL_POLICY_CEILING,
        "selected_below_provider_documented_ceiling": isinstance(provider_ceiling, int) and SELECTED_COMPLETION_BUDGET < provider_ceiling,
        "bounded_not_unlimited": SELECTED_COMPLETION_BUDGET > 0,
        "headroom_rationale": (
            "The prior response reached 3500 completion tokens while incomplete. "
            "5000 adds 1500 tokens (42.9%) and is paired with compact serialization; "
            "it remains below the local 6000-token policy ceiling and far below the documented model maximum."
        ),
    }
    checks["passed"] = all(
        (
            checks["selected_below_local_policy_ceiling"],
            checks["selected_below_provider_documented_ceiling"],
            checks["bounded_not_unlimited"],
            checks["selected_completion_budget"] > checks["previous_failed_cap"],
        )
    )
    if not checks["passed"]:
        raise ResponseBudgetPreflightError("SINGLE-CALL SERIALIZATION NOT VIABLE")
    return checks

