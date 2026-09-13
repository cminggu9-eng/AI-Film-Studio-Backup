"""Deterministic, auditable compliance gate for Showrunner runtime output.

The gate only inspects declared candidate data.  It never invents creative
content or writes into the formal Obsidian Vault.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Optional


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RULES_PATH = Path(__file__).with_name("showrunner_compliance_rules.json")
DEFAULT_LOG_DIR = ROOT / "runtime" / "_COMPLIANCE_LOG"


def load_rules(path: Optional[Path] = None) -> Dict[str, Any]:
    with Path(path or DEFAULT_RULES_PATH).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _text(candidate: Dict[str, Any]) -> str:
    return str(candidate.get("candidate_output", ""))


def _active(candidate: Dict[str, Any], names: Iterable[str]) -> bool:
    haystack = " ".join((str(candidate.get("mode", "")), str(candidate.get("output_type", "")), " ".join(map(str, candidate.get("activated_modules", []))), _text(candidate))).lower()
    return any(name.lower() in haystack for name in names)


def _sentences(text: str) -> list[str]:
    return [part.strip() for part in re.split(r"[。！？\n]+", text) if part.strip()]


def _has_handoff_context(text: str, start: int, markers: Iterable[str]) -> bool:
    window = text[max(0, start - 32): min(len(text), start + 48)]
    return any(marker.lower() in window.lower() for marker in markers)


def _scan_patterns(text: str, patterns: Iterable[str], *, code: str, handoff_markers: Iterable[str] = ()) -> list[Dict[str, Any]]:
    hits: list[Dict[str, Any]] = []
    for pattern in patterns:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            if _has_handoff_context(text, match.start(), handoff_markers):
                continue
            hits.append({"code": code, "offending_text": match.group(0)})
    return hits


def _is_project_specific(sentence: str, anti: Dict[str, Any]) -> bool:
    has_scope = any(marker.lower() in sentence.lower() for marker in anti["conditional_markers"])
    has_option = any(marker.lower() in sentence.lower() for marker in anti["recommendation_markers"])
    broad = any(marker.lower() in sentence.lower() for marker in anti["broad_scope_markers"])
    return has_scope and has_option and not broad


def _boundary_violations(candidate: Dict[str, Any], rules: Dict[str, Any]) -> list[Dict[str, Any]]:
    contract = candidate.get("boundary_contract") or {}
    boundary_role = contract.get("boundary_role", "")
    if not boundary_role:
        return []
    gate = rules["gate"]["boundary"]
    text = _text(candidate)
    if boundary_role == "Director / Cinematography":
        return _scan_patterns(text, gate["director_patterns"], code="DIRECTOR_BOUNDARY_VIOLATION", handoff_markers=gate["handoff_markers"])
    if boundary_role == "Character & Acting":
        return _scan_patterns(text, gate["acting_patterns"], code="ACTING_BOUNDARY_VIOLATION", handoff_markers=gate["handoff_markers"])
    return []


def _anti_mechanical_violations(candidate: Dict[str, Any], rules: Dict[str, Any]) -> list[Dict[str, Any]]:
    if not _active(candidate, ["pacing", "retention", "episode rhythm", "cliffhanger", "reversal", "escalation", "series engine", "continuing drive"]):
        return []
    anti = rules["gate"]["anti_mechanical"]
    violations: list[Dict[str, Any]] = []
    for sentence in _sentences(_text(candidate)):
        lower = sentence.lower()
        if any(marker.lower() in lower for marker in anti["negation_markers"]):
            continue
        event = any(marker.lower() in lower for marker in anti["event_markers"])
        obligation = any(marker.lower() in lower for marker in anti["obligation_markers"])
        broad = any(marker.lower() in lower for marker in anti["broad_scope_markers"])
        interval = any(re.search(pattern, sentence, flags=re.IGNORECASE) for pattern in anti["fixed_interval_regexes"])
        episode = any(re.search(pattern, sentence, flags=re.IGNORECASE) for pattern in anti["episode_unit_regexes"])
        numeric_structure = any(re.search(pattern, sentence, flags=re.IGNORECASE) for pattern in anti["numeric_structure_regexes"])
        if not (event and (interval or episode or broad or numeric_structure)):
            continue
        if _is_project_specific(sentence, anti):
            continue
        # A universal time cadence is mechanical even when phrased softly as
        # "每约三分钟做一次"; project-specific qualification is the escape hatch.
        if interval:
            code = "FIXED_PACING_OR_REVERSAL"
        elif episode and obligation:
            code = "FIXED_EPISODE_QUOTA"
        elif numeric_structure:
            code = "UNQUALIFIED_NUMERIC_STRUCTURE"
        elif broad and obligation:
            code = "CROSS_PROJECT_HARD_CONSTRAINT"
        else:
            continue
        violations.append({
            "code": code,
            "offending_text": sentence,
            "expected_behavior": "Use an explicitly project-specific, conditional heuristic instead of a cross-project pacing or episode quota.",
        })
    return violations


def _production_violations(candidate: Dict[str, Any], rules: Dict[str, Any]) -> list[Dict[str, Any]]:
    if not _active(candidate, ["production reality", "production scope", "production_scope_review"]):
        return []
    text = _text(candidate)
    production = rules["gate"]["production"]
    missing = [label for label in production["required_labels"] if label.lower() not in text.lower()]
    if missing:
        return [{"code": "PRODUCTION_SCOPE_FIELDS_MISSING", "offending_text": ", ".join(missing), "expected_behavior": "Expose all five Production Reality fields, including DEFERRED when input is insufficient."}]
    ci = re.search(r"Creative Intent\s*[:：]\s*([^\n]+)", text, flags=re.IGNORECASE)
    edf = re.search(r"Essential Dramatic Function\s*[:：]\s*([^\n]+)", text, flags=re.IGNORECASE)
    scope = re.search(r"Scope Decision\s*[:：]\s*([^\n]+)", text, flags=re.IGNORECASE)
    unknown = {item.upper() for item in production["unknown_statuses"]}
    deferred = {item.upper() for item in production["deferred_statuses"]}
    ci_value = ci.group(1).strip().upper() if ci else ""
    edf_value = edf.group(1).strip().upper() if edf else ""
    scope_value = scope.group(1).strip().upper() if scope else ""
    violations: list[Dict[str, Any]] = []
    if (ci_value in unknown or edf_value in unknown) and scope_value not in deferred:
        violations.append({"code": "PREMATURE_SCOPE_DECISION", "offending_text": scope.group(0) if scope else "Scope Decision missing", "expected_behavior": "Use Scope Decision: DEFERRED/NEEDS INPUT until Creative Intent and Essential Dramatic Function are known."})
    if ci_value in unknown or edf_value in unknown or "直接" in text:
        for pattern in production["deletion_regexes"]:
            match = re.search(pattern, text, flags=re.IGNORECASE)
            if match:
                violations.append({"code": "UNJUSTIFIED_SCOPE_DELETION", "offending_text": match.group(0), "expected_behavior": "Assess dramatic function and alternate execution before deleting scope."})
                break
    return violations


def _global_violations(candidate: Dict[str, Any], rules: Dict[str, Any]) -> list[Dict[str, Any]]:
    text = _text(candidate)
    violations: list[Dict[str, Any]] = []
    for pattern in rules["gate"]["global"]["canon_conflict_regexes"]:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match and "BLOCKED" not in text.upper():
            violations.append({"code": "CANON_CONFLICT", "offending_text": match.group(0), "expected_behavior": "Stop and request canon authority; do not silently change locked canon."})
    return violations


def build_receipt(candidate: Dict[str, Any], rules: Dict[str, Any]) -> Dict[str, Any]:
    skill = rules["skill"]
    installed = Path(skill["installed_path"])
    canonical = Path(skill["canonical_path"])
    installed_hash = sha256_file(installed) if installed.is_file() else None
    canonical_hash = sha256_file(canonical) if canonical.is_file() else None
    skill_name_match = False
    if installed.is_file():
        try:
            skill_name_match = f"skill_name: {skill['name']}" in installed.read_text(encoding="utf-8")[:4096]
        except (OSError, UnicodeError):
            pass
    return {
        "timestamp": _now(), "task": candidate.get("task", ""), "routed_role": candidate.get("routed_role", "Showrunner"),
        "skill_name": candidate.get("skill_name") or (skill["name"] if candidate.get("routed_role") == "Showrunner" else None),
        "skill_path": candidate.get("skill_path") or (str(installed) if candidate.get("routed_role") == "Showrunner" else None),
        "installed_hash": installed_hash, "canonical_hash": canonical_hash,
        "hash_match": bool(installed_hash and canonical_hash and installed_hash == canonical_hash), "skill_name_match": skill_name_match,
        "project_state": candidate.get("project_state", "UNKNOWN"), "mode": candidate.get("mode", "UNKNOWN"),
        "output_type": candidate.get("output_type", "UNKNOWN"), "activated_modules": candidate.get("activated_modules", []),
        "boundary_contract": candidate.get("boundary_contract"),
    }


def gate_candidate(candidate: Dict[str, Any], rules: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    rules = rules or load_rules()
    violations = _global_violations(candidate, rules) + _boundary_violations(candidate, rules) + _anti_mechanical_violations(candidate, rules) + _production_violations(candidate, rules)
    receipt = build_receipt(candidate, rules)
    if candidate.get("routed_role") == "Showrunner" and not receipt["hash_match"]:
        violations.append({"code": "SKILL_HASH_MISMATCH", "offending_text": f"canonical={receipt['canonical_hash']} installed={receipt['installed_hash']}", "expected_behavior": "Block execution when installed Skill differs from canonical."})
    if candidate.get("routed_role") == "Showrunner" and not receipt["skill_name_match"]:
        violations.append({"code": "SKILL_NAME_MISMATCH", "offending_text": str(receipt["skill_path"]), "expected_behavior": "Verify the installed file declares the expected Skill name."})
    status = "FAIL" if violations else "PASS"
    return {"status": status, "candidate_version": candidate.get("candidate_version", "V1"), "correction_count": 0, "violations": violations, "receipt": receipt, "active_rules": ["GLOBAL", "BOUNDARY_CONTRACT", "ANTI_MECHANICAL", "PRODUCTION_REALITY"], "next": "COMPLIANCE VIOLATION REPORT" if violations else "USER_OUTPUT", "final_delivery_status": "BLOCKED_PENDING" if violations else "READY"}


def gate_with_correction(candidate_v1: Dict[str, Any], candidate_v2: Optional[Dict[str, Any]] = None, rules: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    rules = rules or load_rules()
    first = gate_candidate(candidate_v1, rules)
    if first["status"] == "PASS":
        return first
    if candidate_v2 is None:
        first["next"] = "BLOCKED FOR RUNTIME COMPLIANCE"
        first["final_delivery_status"] = "BLOCKED"
        return first
    second = gate_candidate(candidate_v2, rules)
    second["correction_count"] = 1
    second["first_candidate_violations"] = first["violations"]
    if second["status"] == "PASS":
        second["status"] = "GATE_RECOVERED"
        second["next"] = "USER_OUTPUT"
        second["final_delivery_status"] = "READY_AFTER_ONE_CORRECTION"
    else:
        second["next"] = "BLOCKED FOR RUNTIME COMPLIANCE"
        second["final_delivery_status"] = "BLOCKED"
    return second


def build_runtime_record(candidate_v1: Dict[str, Any], gate_v1: Dict[str, Any], candidate_v2: Optional[Dict[str, Any]] = None, gate_v2: Optional[Dict[str, Any]] = None, final_delivery_status: Optional[str] = None) -> Dict[str, Any]:
    final_gate = gate_v2 or gate_v1
    return {
        "receipt": final_gate["receipt"], "candidate_v1": candidate_v1, "gate_v1": gate_v1,
        "violations": gate_v1["violations"], "correction_count": 1 if candidate_v2 is not None else final_gate.get("correction_count", 0),
        "candidate_v2": candidate_v2, "gate_v2": gate_v2,
        "final_delivery_status": final_delivery_status or final_gate["final_delivery_status"],
    }


def write_compliance_log(result: Dict[str, Any], log_path: Optional[Path] = None) -> Path:
    target_dir = Path(log_path or DEFAULT_LOG_DIR)
    if target_dir.suffix.lower() == ".json":
        target_dir.parent.mkdir(parents=True, exist_ok=True)
        target = target_dir
    else:
        target_dir.mkdir(parents=True, exist_ok=True)
        target = target_dir / f"compliance-{datetime.now().strftime('%Y%m%d-%H%M%S-%f')}.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return target
