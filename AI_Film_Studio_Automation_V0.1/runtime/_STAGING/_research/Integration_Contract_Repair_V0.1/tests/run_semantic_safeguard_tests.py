"""Offline SEM-01 through SEM-12 safeguard fixtures; no role chain or provider."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Callable, Dict


STAGE = Path(__file__).resolve().parents[1]
IMPLEMENTATION = STAGE / "implementation"
if str(IMPLEMENTATION) not in sys.path:
    sys.path.insert(0, str(IMPLEMENTATION))

from integration_contract.state_evidence import ABSENT
from integration_contract.state_ledger import E2EStateLedger
from integration_contract.semantic_safeguard import evaluate_semantic_safeguard


def envelope() -> Dict[str, Any]:
    return {
        "source_role": "Scene Writer",
        "source_record_id": "E2E-FIX-01-SCENE-02",
        "version": "1.0",
        "timestamp": "2026-08-26T00:00:00Z",
        "intended_recipient": "Continuity",
        "handoff_reason": "Semantic safeguard fixture",
        "canon_assignment_locks": ["PROP:A-17", "KNOWLEDGE:mother-storage", "STATE:wet-uniform", "RELATIONSHIP:no-auto-reconciliation"],
        "prohibited_changes": ["Do not change A-17", "Do not reveal mother/storage information early", "Do not call the relationship reconciled"],
        "canonical_mode": "CREATE",
        "primary_state_or_outcome": "SCENE_CREATED",
        "flags": [],
        "handoffs": [],
        "required_outcome": "A-17 and state evidence remain traceable.",
        "unresolved_decisions": [],
        "relevant_prior_state": {"key_identity": "A-17", "custody": "许宁", "clothing": "wet_uniform"},
        "current_state": {"key_identity": "A-17", "custody": "许曼", "clothing": "wet_uniform"},
        "proposed_state": {"clothing": "dry_clothes"},
        "knowledge_timing": {"mother_storage": {"authorized_at": 2, "holder": "许曼"}},
        "relationship_state": {"relation": "estranged"},
        "visual_state": {"clothing": "wet_uniform"},
        "authority_source": "E2E-FIX-01 sole original input",
        "evidence_locator": "AI_Film_Studio_E2E_Fixture_01_V0.1.md#non-negotiable-fixture-facts",
    }


def ledger() -> E2EStateLedger:
    result = E2EStateLedger(run_id="SEM-FIX")
    result.append(envelope=envelope(), state_snapshot={"key_identity": "A-17", "custody": "许宁", "clothing": "wet_uniform"})
    return result


def assertion(case_id: str, rule: str, value: Any, expected: Any, *, authority: str = "E2E-FIX-01", locator: str = "fixture#evidence", authorized: bool = False, review: bool = False) -> Dict[str, Any]:
    return {
        "id": case_id,
        "rule": rule,
        "value": value,
        "expected": expected,
        "authority_source": authority,
        "evidence_locator": locator,
        "authorized_transition": authorized,
        "semantic_review_required": review,
    }


def evaluate(case_id: str, assertions: list[Dict[str, Any]], *, legacy_only: bool = False, creative: Any = "Synthetic fixture text only.") -> Dict[str, Any]:
    return evaluate_semantic_safeguard(
        envelope=envelope(),
        ledger=ledger(),
        creative_output=creative,
        assertions=assertions,
        legacy_verifier_result="PASS",
        legacy_verifier_only=legacy_only,
    )


def run_case(case_id: str, function: Callable[[], str]) -> Dict[str, str]:
    try:
        return {"id": case_id, "result": "PASS", "detail": function()}
    except Exception as exc:
        return {"id": case_id, "result": "FAIL", "detail": f"{type(exc).__name__}: {exc}"}


def main() -> int:
    reports = []
    reports.append(run_case("SEM-01", lambda: "A-17 change blocked" if evaluate("SEM-01", [assertion("SEM-01", "PROP_EQUALS", "A-18", "A-17")])["integration_decision"] == "BLOCK" else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("SEM-02", lambda: "custody trace accepted" if evaluate("SEM-02", [assertion("SEM-02", "CUSTODY_TRACKED", "许曼", "许曼")])["integration_decision"] == "PASS" else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("SEM-03", lambda: "early knowledge blocked" if evaluate("SEM-03", [assertion("SEM-03", "KNOWLEDGE_NOT_BEFORE", {"observed_at": 1}, {"authorized_at": 2})])["integration_decision"] == "BLOCK" else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("SEM-04", lambda: "unsupported micro-fact blocked" if evaluate("SEM-04", [assertion("SEM-04", "UNSUPPORTED_NEW_FACT", "mother left a warning letter", ABSENT, authority=ABSENT, review=True)])["integration_decision"] == "BLOCK" else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("SEM-05", lambda: "wet uniform preserved" if evaluate("SEM-05", [assertion("SEM-05", "REQUIRED_STATE", "wet_uniform", "wet_uniform")])["integration_decision"] == "PASS" else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("SEM-06", lambda: "authorized clothing transition accepted" if evaluate("SEM-06", [assertion("SEM-06", "AUTHORIZED_TRANSITION", {"from": "wet_uniform", "to": "dry_clothes"}, {"from": "wet_uniform", "to": "dry_clothes"}, authorized=True)])["integration_decision"] == "PASS" else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("SEM-07", lambda: "automatic reconciliation blocked" if evaluate("SEM-07", [assertion("SEM-07", "RELATIONSHIP_NOT_AUTOMATIC", "RECONCILED", "estranged", authorized=False, review=True)])["integration_decision"] == "BLOCK" else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("SEM-08", lambda: "unknown state flags without contradiction" if evaluate("SEM-08", [assertion("SEM-08", "UNKNOWN_STATE", ABSENT, ABSENT)])["integration_decision"] == "FLAG" else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("SEM-09", lambda: "authorized change not misclassified" if evaluate("SEM-09", [assertion("SEM-09", "AUTHORIZED_TRANSITION", {"from": "许宁", "to": "许曼"}, {"from": "许宁", "to": "许曼"}, authorized=True)])["integration_decision"] == "PASS" else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("SEM-10", lambda: "issue keeps evidence locator" if evaluate("SEM-10", [assertion("SEM-10", "PROP_EQUALS", "A-18", "A-17", locator="fixture#key-marking")])["layer_a"]["findings"][0]["evidence_locator"] == "fixture#key-marking" else (_ for _ in ()).throw(AssertionError())))

    def no_rewrite() -> str:
        creative = {"scene": "Synthetic scene material.", "control": {"primary_state": "SCENE_CREATED"}}
        before = copy.deepcopy(creative)
        report = evaluate("SEM-11", [assertion("SEM-11", "PROP_EQUALS", "A-17", "A-17")], creative=creative)
        assert creative == before
        assert "creative_output" not in report and report["creative_output_rewrite"] == "PROHIBITED"
        return "gate returns a report without rewriting scene material"
    reports.append(run_case("SEM-11", no_rewrite))
    reports.append(run_case("SEM-12", lambda: "legacy verifier alone blocked" if evaluate("SEM-12", [assertion("SEM-12", "PROP_EQUALS", "A-17", "A-17")], legacy_only=True)["integration_decision"] == "BLOCK" else (_ for _ in ()).throw(AssertionError())))

    payload = {"classification": "OFFLINE SEMANTIC SAFEGUARD TEST", "results": reports, "passed": sum(item["result"] == "PASS" for item in reports), "total": len(reports), "provider_calls": 0, "real_role_executions": 0}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["passed"] == payload["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
