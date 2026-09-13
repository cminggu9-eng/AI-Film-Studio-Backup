"""Offline STATE-01 through STATE-12 evidence-contract tests."""

from __future__ import annotations

import ast
import copy
import json
import sys
from pathlib import Path
from typing import Any, Callable, Dict


STAGE = Path(__file__).resolve().parents[1]
IMPLEMENTATION = STAGE / "implementation"
if str(IMPLEMENTATION) not in sys.path:
    sys.path.insert(0, str(IMPLEMENTATION))

from integration_contract.state_evidence import ABSENT, validate_state_evidence_envelope
from integration_contract.state_ledger import E2EStateLedger


def base_envelope() -> Dict[str, Any]:
    return {
        "source_role": "Scene Writer",
        "source_record_id": "E2E-FIX-01-SCENE-01",
        "version": "1.0",
        "timestamp": "2026-08-26T00:00:00Z",
        "intended_recipient": "Continuity",
        "handoff_reason": "State comparison",
        "canon_assignment_locks": ["PROP:A-17", "KNOWLEDGE:mother-storage", "RELATIONSHIP:no-auto-reconciliation"],
        "prohibited_changes": ["Do not change A-17", "Do not infer reconciliation"],
        "canonical_mode": "CREATE",
        "primary_state_or_outcome": "SCENE_CREATED",
        "flags": ["DIRECTOR_HANDOFF_ELIGIBLE"],
        "handoffs": [],
        "required_outcome": "State evidence is available for comparison.",
        "unresolved_decisions": [],
        "relevant_prior_state": {"key_custody": "许宁"},
        "current_state": {"key_custody": "许曼", "clothing": "wet_uniform"},
        "proposed_state": {"clothing": "dry_clothes"},
        "knowledge_timing": {"mother_storage": {"authorized_at": "scene-02", "holder": "许曼"}},
        "relationship_state": {"relation": "estranged", "change": "not-resolved"},
        "visual_state": {"clothing": "wet_uniform"},
        "authority_source": "Showrunner assignment E2E-FIX-01",
        "evidence_locator": "E2E-FIX-01#sole-original-input",
    }


def run_case(case_id: str, assertion: Callable[[], str]) -> Dict[str, str]:
    try:
        return {"id": case_id, "result": "PASS", "detail": assertion()}
    except Exception as exc:
        return {"id": case_id, "result": "FAIL", "detail": f"{type(exc).__name__}: {exc}"}


def main() -> int:
    reports = []
    original = base_envelope()
    reports.append(run_case("STATE-01", lambda: "source/version preserved" if validate_state_evidence_envelope(original)["source_record_id"] == original["source_record_id"] and validate_state_evidence_envelope(original)["version"] == original["version"] else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("STATE-02", lambda: "locks preserved" if validate_state_evidence_envelope(original)["canon_assignment_locks"] == original["canon_assignment_locks"] else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("STATE-03", lambda: "canonical tokens unchanged" if validate_state_evidence_envelope(original)["canonical_mode"] == "CREATE" and validate_state_evidence_envelope(original)["primary_state_or_outcome"] == "SCENE_CREATED" else (_ for _ in ()).throw(AssertionError())))

    def absent_remains_absent() -> str:
        candidate = copy.deepcopy(original)
        candidate["relationship_state"] = ABSENT
        copied = validate_state_evidence_envelope(candidate)
        assert copied["relationship_state"] == ABSENT
        return "ABSENT preserved without synthesis"
    reports.append(run_case("STATE-04", absent_remains_absent))

    reports.append(run_case("STATE-05", lambda: "knowledge timing attributable" if validate_state_evidence_envelope(original)["knowledge_timing"]["mother_storage"]["authorized_at"] == "scene-02" else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("STATE-06", lambda: "prior/current/proposed distinguishable" if [validate_state_evidence_envelope(original)[key] for key in ("relevant_prior_state", "current_state", "proposed_state")] == [{"key_custody": "许宁"}, {"key_custody": "许曼", "clothing": "wet_uniform"}, {"clothing": "dry_clothes"}] else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("STATE-07", lambda: "visual state attributable" if validate_state_evidence_envelope(original)["visual_state"]["clothing"] == "wet_uniform" else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("STATE-08", lambda: "relationship state attributable" if validate_state_evidence_envelope(original)["relationship_state"]["relation"] == "estranged" else (_ for _ in ()).throw(AssertionError())))
    reports.append(run_case("STATE-09", lambda: "authority owner preserved" if validate_state_evidence_envelope(original)["authority_source"] == "Showrunner assignment E2E-FIX-01" else (_ for _ in ()).throw(AssertionError())))

    def continuity_comparison_without_inference() -> str:
        ledger = E2EStateLedger(run_id="STATE-10")
        prior = ledger.append(envelope=original, state_snapshot={"key_identity": "A-17", "custody": "许宁"})
        current_envelope = copy.deepcopy(original)
        current_envelope["source_record_id"] = "E2E-FIX-01-SCENE-02"
        current = ledger.append(envelope=current_envelope, state_snapshot={"key_identity": "A-17", "custody": "许曼"})
        packet = ledger.comparison_input(dimension="custody", prior_entry_id=prior.entry_id, current_entry_id=current.entry_id)
        assert packet["comparison_ready"] is True and packet["role_decision"] == "NOT_MADE"
        return "comparison evidence supplied without a Continuity decision"
    reports.append(run_case("STATE-10", continuity_comparison_without_inference))

    def no_silent_repair() -> str:
        candidate = copy.deepcopy(original)
        candidate["current_state"] = ABSENT
        copied = validate_state_evidence_envelope(candidate)
        assert copied["current_state"] == ABSENT
        return "missing current state was not repaired"
    reports.append(run_case("STATE-11", no_silent_repair))

    def no_database_dependency() -> str:
        source = (IMPLEMENTATION / "integration_contract" / "state_ledger.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        imported = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.extend(alias.name.lower() for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.append(node.module.lower())
        forbidden_imports = ("sqlite3", "requests", "urllib", "sqlalchemy", "chromadb", "faiss")
        assert not any(name.startswith(forbidden) for name in imported for forbidden in forbidden_imports), imported
        return "run-local in-memory ledger has no database dependency"
    reports.append(run_case("STATE-12", no_database_dependency))

    payload = {"classification": "OFFLINE STATE CONTRACT TEST", "results": reports, "passed": sum(item["result"] == "PASS" for item in reports), "total": len(reports)}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["passed"] == payload["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
