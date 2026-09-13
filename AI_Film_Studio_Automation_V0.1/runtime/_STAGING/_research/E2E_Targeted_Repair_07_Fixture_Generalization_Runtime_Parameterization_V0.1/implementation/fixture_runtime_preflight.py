"""Generic, provider-free entrypoint for a fixture-parameterized E2E run.

This is the only Repair 07 runtime entrypoint.  It admits a run only after a
binding has been deterministically compiled; orchestration consumers receive
the compiled contract rather than fixture-specific globals.
"""
from __future__ import annotations

from pathlib import Path

from fixture_contract_compiler import compile_path


def prepare_run(binding_path: Path) -> dict:
    """Return the fully bound generic runtime contract without executing roles."""
    compiled = compile_path(binding_path)
    return {
        "fixture_id": compiled["fixture"]["fixture_id"],
        "strict_schema": compiled["strict_schema"],
        "semantic_safeguard_config": compiled["semantic_safeguard_config"],
        "ledger_tracking": compiled["ledger_tracking"],
        "acceptance_evidence_map": compiled["acceptance_evidence_map"],
        "reveal_event_contract": compiled["reveal_event_contract"],
    }
