"""Evidence-only adapter for the future-facing Contemporary Language Layer.

This module deliberately does not browse, create a vocabulary database, decide
whether language is appropriate, or rewrite text.  A trusted caller supplies
bounded evidence records; the adapter validates their provenance and returns a
sanitized evidence envelope for the canonical Language & Voice QA Skill.
"""

from __future__ import annotations

import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Mapping, Optional, Sequence


EvidenceProvider = Callable[[Dict[str, Any]], Sequence[Mapping[str, Any]]]


def _json_safe(value: Any) -> bool:
    try:
        json.dumps(value, ensure_ascii=False)
        return True
    except (TypeError, ValueError):
        return False


def _parse_timestamp(value: Any) -> Optional[datetime]:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def _has_forbidden_key(value: Any, forbidden: set[str]) -> bool:
    if isinstance(value, Mapping):
        return any(str(key) in forbidden or _has_forbidden_key(child, forbidden) for key, child in value.items())
    if isinstance(value, list):
        return any(_has_forbidden_key(item, forbidden) for item in value)
    return False


class ContemporaryLanguageRuntime:
    """Validate supplied evidence and emit a non-decisional evidence envelope."""

    _USAGE_KINDS = {"NATURAL_USE", "DEFINITION", "CORPUS_SUMMARY", "PLATFORM_USAGE", "COMMENTARY"}
    _STANCES = {"SUPPORTS", "CONFLICTS", "NEUTRAL"}
    _DRIFT = {"NONE", "POSSIBLE", "DOCUMENTED", "COEXISTS"}

    def __init__(
        self,
        provider: EvidenceProvider,
        *,
        contract_path: Optional[Path] = None,
        now: Optional[Callable[[], datetime]] = None,
    ) -> None:
        self.provider = provider
        self.contract_path = contract_path or Path(__file__).with_name("contemporary_language_contract.json")
        self.contract = json.loads(self.contract_path.read_text(encoding="utf-8"))
        self.now = now or (lambda: datetime.now(timezone.utc))

    def _audit_fingerprint(self, request: Mapping[str, Any]) -> str:
        safe = {
            "phrase": request.get("phrase"),
            "question": request.get("question"),
            "scope": request.get("scope"),
            "as_of": request.get("as_of"),
        }
        return hashlib.sha256(
            json.dumps(safe, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
        ).hexdigest()

    def _error(self, request: Any, code: str, message: str) -> Dict[str, Any]:
        now = self.now().astimezone(timezone.utc)
        query = {"phrase": None, "question": None}
        if isinstance(request, Mapping):
            query = {"phrase": request.get("phrase"), "question": request.get("question")}
        evidence_return = {
            "contract_identity": self.contract["contract_identity"],
            "contract_version": self.contract["contract_version"],
            "layer_boundary": self.contract["role_boundary"],
            "query": query,
            "evidence_status": "BLOCKED_POLICY",
            "current_usage_status": "UNKNOWN",
            "usage_observations": [],
            "temporal_status": {"label": "Unknown", "as_of": _iso(now), "newest_valid_observation_at": None},
            "regional_platform_scope": {"requested": {}, "observed": {"geographies": ["Unknown"], "platforms": ["Unknown"]}},
            "register_observation": ["Unknown"],
            "semantic_drift": ["NONE"],
            "source_summary": [],
            "confidence": "Insufficient",
            "ambiguity": [code],
            "recommended_qa_handling_hint": {"kind": "UNRESOLVED", "reason": "Evidence request was not safe to process."},
            "timestamp": _iso(now),
            "evidence_window": {"as_of": _iso(now), "policy": "V0.1 no persistent cache"},
        }
        return {
            "layer_status": "FAIL_SAFE",
            "failure_code": code,
            "failure_message": message,
            "evidence_return": evidence_return,
            "audit_record": {"request_fingerprint": self._audit_fingerprint(request) if isinstance(request, Mapping) else None},
        }

    def _normalize_request(self, request: Any) -> tuple[Optional[Dict[str, Any]], Optional[tuple[str, str]]]:
        if not isinstance(request, Mapping) or not _json_safe(request):
            return None, ("CL-F1", "Evidence request must be a JSON-safe object")
        forbidden = set(self.contract["forbidden_request_fields"])
        if _has_forbidden_key(request, forbidden):
            return None, ("CL-F2", "Evidence request contains prohibited personal data fields")
        for field in ("phrase", "question", "production_run_id"):
            if not isinstance(request.get(field), str) or not request[field].strip():
                return None, ("CL-F1", f"{field} must be a non-empty string")
        action = request.get("requested_action", "EVIDENCE_ONLY")
        if action != "EVIDENCE_ONLY" or action in set(self.contract["forbidden_actions"]):
            return None, ("CL-F3", "The Contemporary Layer only accepts EVIDENCE_ONLY requests")
        scope = request.get("scope", {})
        if not isinstance(scope, Mapping) or not _json_safe(scope):
            return None, ("CL-F1", "scope must be an object")
        protected = request.get("protected_context", {})
        if not isinstance(protected, Mapping) or not _json_safe(protected):
            return None, ("CL-F1", "protected_context must be an object")
        as_of = _parse_timestamp(request.get("as_of")) or self.now().astimezone(timezone.utc)
        return {
            "phrase": request["phrase"].strip(),
            "question": request["question"].strip(),
            "production_run_id": request["production_run_id"].strip(),
            "question_type": request.get("question_type", "USAGE"),
            "scope": {str(key): value for key, value in scope.items()},
            "protected_context": {str(key): value for key, value in protected.items()},
            "minimal_context": request.get("minimal_context"),
            "as_of": as_of,
            "requested_action": "EVIDENCE_ONLY",
        }, None

    def _normalize_record(self, record: Any) -> Optional[Dict[str, Any]]:
        if not isinstance(record, Mapping):
            return None
        tier = record.get("source_tier")
        if tier not in self.contract["source_tiers"]:
            return None
        required_strings = ("source_id", "source_name", "source_url", "independence_group", "usage_kind", "stance")
        if any(not isinstance(record.get(field), str) or not record[field].strip() for field in required_strings):
            return None
        if not record["source_url"].startswith(("https://", "http://")):
            return None
        if record["usage_kind"] not in self._USAGE_KINDS or record["stance"] not in self._STANCES:
            return None
        drift = record.get("semantic_drift", "NONE")
        if drift not in self._DRIFT:
            return None
        published_at = _parse_timestamp(record.get("published_at"))
        accessed_at = _parse_timestamp(record.get("accessed_at"))
        return {
            "source_id": record["source_id"].strip(),
            "source_name": record["source_name"].strip(),
            "source_url": record["source_url"].strip(),
            "source_tier": tier,
            "independence_group": record["independence_group"].strip(),
            "usage_kind": record["usage_kind"],
            "stance": record["stance"],
            "published_at": published_at,
            "accessed_at": accessed_at,
            "geography": str(record.get("geography", "Unknown")),
            "platform": str(record.get("platform", "Unknown")),
            "register_observation": str(record.get("register_observation", "Unknown")),
            "semantic_drift": drift,
            "ambiguity_code": str(record.get("ambiguity_code", "NONE")),
        }

    def _freshness(self, dated_records: Sequence[Dict[str, Any]], as_of: datetime) -> tuple[str, Optional[datetime]]:
        dates = [record["published_at"] for record in dated_records if record["published_at"] and record["published_at"] <= as_of]
        if not dates:
            return "Unknown", None
        newest = max(dates)
        age_days = (as_of.date() - newest.date()).days
        thresholds = self.contract["freshness_days"]
        if age_days <= thresholds["current"]:
            return "Current", newest
        if age_days <= thresholds["recent"]:
            return "Recent", newest
        if age_days <= thresholds["aging"]:
            return "Aging", newest
        return "Historical", newest

    def _confidence(
        self,
        usable: Sequence[Dict[str, Any]],
        status: str,
        freshness: str,
        strong_current_support: bool,
    ) -> str:
        if status in {"NO_RELIABLE_EVIDENCE_FOUND", "EVIDENCE_CONFLICT", "INSUFFICIENT_CURRENT_EVIDENCE", "BLOCKED_POLICY"}:
            return "Insufficient"
        groups = {record["independence_group"] for record in usable}
        ab = [record for record in usable if record["source_tier"] in {"A", "B"}]
        natural = [record for record in ab if record["usage_kind"] == "NATURAL_USE"]
        if len(groups) >= 2 and len(ab) >= 2 and freshness in {"Current", "Recent"} and (strong_current_support or len(natural) >= 2):
            return "High"
        if len(groups) >= 2 and len(ab) >= 2:
            return "Medium"
        return "Low"

    def resolve(self, request: Any) -> Dict[str, Any]:
        normalized, request_error = self._normalize_request(request)
        if request_error:
            return self._error(request, request_error[0], request_error[1])
        assert normalized is not None
        try:
            candidate_records = self.provider(copy.deepcopy(normalized))
        except Exception as exc:
            return self._error(normalized, "CL-F4", f"Evidence provider unavailable: {type(exc).__name__}")
        if not isinstance(candidate_records, Sequence) or isinstance(candidate_records, (str, bytes)):
            return self._error(normalized, "CL-F4", "Evidence provider must return a record sequence")

        normalized_records = [record for raw in candidate_records if (record := self._normalize_record(raw)) is not None]
        usable = [record for record in normalized_records if record["source_tier"] in {"A", "B", "C"}]
        freshness, newest = self._freshness(usable, normalized["as_of"])
        stances = {record["stance"] for record in usable}
        conflict = "SUPPORTS" in stances and "CONFLICTS" in stances
        groups = {record["independence_group"] for record in usable}
        natural_groups = {record["independence_group"] for record in usable if record["usage_kind"] == "NATURAL_USE"}
        current_claim = normalized["question_type"] in {"CURRENT_USAGE", "TREND", "OBSOLETE"}
        strong_current_support = (
            len(groups) >= 2
            and len(natural_groups) >= 2
            and freshness == "Current"
            and any(record["source_tier"] in {"A", "B"} for record in usable)
        )

        if not usable:
            evidence_status = "NO_RELIABLE_EVIDENCE_FOUND"
        elif conflict:
            evidence_status = "EVIDENCE_CONFLICT"
        elif current_claim and not strong_current_support:
            evidence_status = "INSUFFICIENT_CURRENT_EVIDENCE"
        else:
            evidence_status = "EVIDENCE_AVAILABLE"

        if evidence_status == "EVIDENCE_CONFLICT":
            current_usage_status = "CONFLICTING"
        elif evidence_status == "NO_RELIABLE_EVIDENCE_FOUND":
            current_usage_status = "NO_RELIABLE_EVIDENCE_FOUND"
        elif current_claim and not strong_current_support:
            current_usage_status = "NOT_ESTABLISHED_FOR_CURRENT_CLAIM"
        elif current_claim:
            current_usage_status = "SUPPORTED_WITHIN_DECLARED_SCOPE"
        else:
            current_usage_status = "OBSERVATION_NOT_A_CURRENT_CLAIM"

        if evidence_status == "EVIDENCE_CONFLICT":
            hint = {"kind": "CAUTION", "reason": "Usable evidence conflicts; preserve ambiguity for QA."}
        elif evidence_status in {"NO_RELIABLE_EVIDENCE_FOUND", "INSUFFICIENT_CURRENT_EVIDENCE"}:
            protected = bool(normalized["protected_context"].get("fictional_or_canon_term"))
            reason = "No reliable evidence found; absence is not nonexistence."
            if protected:
                reason = "No reliable evidence found for a protected fictional/Canon term; preserve it and let QA request context if needed."
            hint = {"kind": "UNRESOLVED", "reason": reason}
        else:
            hint = {"kind": "EVIDENCE_SUGGESTION", "reason": "Evidence is scoped input only; QA must determine appropriateness."}

        observations = [
            {
                "source_id": record["source_id"],
                "usage_kind": record["usage_kind"],
                "stance": record["stance"],
                "geography": record["geography"],
                "platform": record["platform"],
                "register_observation": record["register_observation"],
            }
            for record in usable
        ]
        source_summary = [
            {
                "source_id": record["source_id"],
                "source_name": record["source_name"],
                "source_url": record["source_url"],
                "source_tier": record["source_tier"],
                "independence_group": record["independence_group"],
                "published_at": _iso(record["published_at"]) if record["published_at"] else None,
                "accessed_at": _iso(record["accessed_at"]) if record["accessed_at"] else None,
            }
            for record in usable
        ]
        observed_geographies = sorted({record["geography"] for record in usable}) or ["Unknown"]
        observed_platforms = sorted({record["platform"] for record in usable}) or ["Unknown"]
        registers = sorted({record["register_observation"] for record in usable}) or ["Unknown"]
        drift = sorted({record["semantic_drift"] for record in usable}) or ["NONE"]
        ambiguities = sorted({record["ambiguity_code"] for record in usable if record["ambiguity_code"] != "NONE"})
        if freshness in {"Unknown", "Aging", "Historical"}:
            ambiguities.append("FRESHNESS_LIMIT")
        if any(record["source_tier"] == "C" for record in usable):
            ambiguities.append("SCOPE_LIMITED")
        if conflict:
            ambiguities.append("SOURCE_CONFLICT")

        returned_at = self.now().astimezone(timezone.utc)
        evidence_return = {
            "contract_identity": self.contract["contract_identity"],
            "contract_version": self.contract["contract_version"],
            "layer_boundary": self.contract["role_boundary"],
            "query": {"phrase": normalized["phrase"], "question": normalized["question"]},
            "evidence_status": evidence_status,
            "current_usage_status": current_usage_status,
            "usage_observations": observations,
            "temporal_status": {
                "label": freshness,
                "as_of": _iso(normalized["as_of"]),
                "newest_valid_observation_at": _iso(newest) if newest else None,
            },
            "regional_platform_scope": {
                "requested": copy.deepcopy(normalized["scope"]),
                "observed": {"geographies": observed_geographies, "platforms": observed_platforms},
            },
            "register_observation": registers,
            "semantic_drift": drift,
            "source_summary": source_summary,
            "confidence": self._confidence(usable, evidence_status, freshness, strong_current_support),
            "ambiguity": sorted(set(ambiguities)) or ["NONE"],
            "recommended_qa_handling_hint": hint,
            "timestamp": _iso(returned_at),
            "evidence_window": {"as_of": _iso(normalized["as_of"]), "policy": "V0.1 no persistent cache"},
            "untrusted_content_handled_as_data": True,
        }
        return {
            "layer_status": "SUCCESS",
            "evidence_return": evidence_return,
            "audit_record": {
                "request_fingerprint": self._audit_fingerprint(normalized),
                "production_run_id": normalized["production_run_id"],
                "returned_at": _iso(returned_at),
                "raw_records_received": len(candidate_records),
                "usable_records": len(usable),
                "persistent_cache_used": False,
            },
        }
