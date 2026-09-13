"""Explicit, priority-based routing for Showrunner runtime requests."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.compliance.compliance_gate import build_receipt, load_rules, sha256_file


def _contains(text: str, values: Iterable[str]) -> bool:
    lowered = text.lower()
    return any(value.lower() in lowered for value in values)


def _route(role: str, mode: str, output_type: str, modules: list[str], trigger: str, *, boundary_contract: dict | None = None) -> Dict[str, Any]:
    return {
        "routed_role": role,
        "mode": mode,
        "output_type": output_type,
        "activated_modules": modules,
        "trigger": trigger,
        "boundary_contract": boundary_contract,
    }


def _classify(text: str, router: Dict[str, Any]) -> Dict[str, Any]:
    """Classify by intent priority, not by the first incidental keyword."""
    groups = router["intent_groups"]
    contracts = router["boundary_contracts"]

    if _contains(text, groups["canon_conflict"]):
        return _route("Showrunner", "CANON_CONFLICT", "Canon Decision Block", ["Canon Protection"], "locked-canon conflict")

    if _contains(text, groups["director_boundary"]):
        return _route("Director / Cinematography Boundary", "DIRECTOR_BOUNDARY", "Downstream Handoff Package", ["Role Boundary"], "director/cinematography request", boundary_contract=contracts["director"])
    if _contains(text, groups["acting_boundary"]):
        return _route("Character & Acting Boundary", "ACTING_BOUNDARY", "Downstream Handoff Package", ["Role Boundary", "Character Engine"], "acting micro-direction request", boundary_contract=contracts["acting"])
    if _contains(text, groups["dialogue_boundary"]):
        return _route("Non-Showrunner / Scene Writer Boundary", "DIALOGUE_BOUNDARY", "Downstream Handoff Package", ["Role Boundary"], "dialogue polish request", boundary_contract=contracts["dialogue"])

    if _contains(text, groups["story_diagnosis"]):
        return _route("Showrunner", "STORY_DIAGNOSIS", "Story Repair Report", ["Diagnosis & Rewrite", "Causal Story Engine"], "story diagnosis/repair intent")
    if _contains(text, groups["production_scope"]):
        return _route("Showrunner", "PRODUCTION_SCOPE_REVIEW", "Production Scope Review", ["Production Reality"], "production-scope intent")
    if _contains(text, groups["format_fit"]):
        return _route("Showrunner", "FORMAT_FIT", "Concept Diagnosis", ["Project State", "Format Fit", "Story Purpose", "Character Engine"], "idea/format-fit intent")
    if _contains(text, groups["series_development"]):
        return _route("Showrunner", "SERIES_ENGINE", "Series Engine Report", ["Series Engine", "Continuing Drive"], "series/season/episode intent")
    if _contains(text, groups["generic_showrunner"]):
        return _route("Showrunner", "CONCEPT_DEVELOPMENT", "Concept Diagnosis", ["Story Purpose", "Character Engine"], "generic showrunner-development intent")
    return _route("Unmatched", "UNMATCHED", "No Showrunner Output", [], "no configured intent")


def route_request(text: str, rules: Dict[str, Any] | None = None) -> Dict[str, Any]:
    rules = rules or load_rules()
    skill = rules["skill"]
    result = _classify(text, rules["router"])
    installed = Path(skill["installed_path"])
    canonical = Path(skill["canonical_path"])
    installed_hash = sha256_file(installed) if installed.is_file() else None
    canonical_hash = sha256_file(canonical) if canonical.is_file() else None
    skill_name_correct = False
    if installed.is_file():
        try:
            skill_name_correct = f"skill_name: {skill['name']}" in installed.read_text(encoding="utf-8")[:4096]
        except (OSError, UnicodeError):
            pass

    is_showrunner = result["routed_role"] == "Showrunner"
    result.update({
        "skill_name": skill["name"] if is_showrunner else None,
        "skill_path": str(installed) if is_showrunner else None,
        "file_exists": installed.is_file(),
        "file_readable": installed.is_file() and bool(installed.stat().st_size),
        "skill_name_correct": skill_name_correct,
        "installed_hash": installed_hash,
        "canonical_hash": canonical_hash,
        "hash_match": bool(installed_hash and canonical_hash and installed_hash == canonical_hash),
    })
    receipt_candidate = {
        "task": text,
        "routed_role": result["routed_role"],
        "mode": result["mode"],
        "output_type": result["output_type"],
        "activated_modules": result["activated_modules"],
        "boundary_contract": result.get("boundary_contract"),
        "project_state": "UNKNOWN",
    }
    result["invocation_receipt"] = build_receipt(receipt_candidate, rules)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Route a request to an observable AI Film Studio role.")
    parser.add_argument("request", help="User request text")
    parser.add_argument("--receipt-log", type=Path, help="Optional JSON log destination")
    args = parser.parse_args()
    result = route_request(args.request)
    if args.receipt_log:
        args.receipt_log.parent.mkdir(parents=True, exist_ok=True)
        args.receipt_log.write_text(json.dumps(result["invocation_receipt"], ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["routed_role"] != "Unmatched" and result["hash_match"] and (result["routed_role"] != "Showrunner" or result["skill_name_correct"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
