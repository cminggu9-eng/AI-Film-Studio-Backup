"""Fail-safe runtime adapter for the canonical Language & Voice QA Skill V0.1.

SKILL DECIDES. RUNTIME EXECUTES.
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Mapping, Optional

from runtime.compliance.compliance_gate import sha256_file


SkillInvoker = Callable[[Dict[str, Any]], Dict[str, Any]]


def _find_project_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / "studio.config.json").is_file():
            return candidate
    raise RuntimeError("AI Film Studio Automation root not found")


def _read_frontmatter(path: Path) -> Dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    result: Dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return result
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip("'\"")
    return {}


def _stable_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str)


def _json_safe(value: Any) -> bool:
    try:
        json.dumps(value, ensure_ascii=False)
        return True
    except (TypeError, ValueError):
        return False


def _normalize_rewrite_comparison(value: str) -> str:
    """Normalize only line endings and outer whitespace for rewrite-change proof."""
    return value.replace("\r\n", "\n").replace("\r", "\n").strip()


class LanguageVoiceQARuntime:
    """Transport-only adapter around a caller-supplied canonical Skill executor."""

    def __init__(
        self,
        invoker: SkillInvoker,
        *,
        contract_path: Optional[Path] = None,
        skill_path: Optional[Path] = None,
        log_dir: Optional[Path] = None,
        now: Optional[Callable[[], datetime]] = None,
        test_only_allow_noncanonical_skill_path: bool = False,
    ) -> None:
        self.invoker = invoker
        self.contract_path = contract_path or Path(__file__).with_name("language_voice_qa_contract.json")
        self.contract = json.loads(self.contract_path.read_text(encoding="utf-8"))
        self.project_root = _find_project_root(Path(__file__).resolve())
        config = json.loads((self.project_root / "studio.config.json").read_text(encoding="utf-8"))
        self.vault_root = Path(config["vault_path"])
        self.canonical_skill_path = self.vault_root / self.contract["skill"]["canonical_relative_path"]
        self.skill_path = skill_path or self.canonical_skill_path
        self.log_dir = log_dir or self.project_root / "runtime" / "_COMPLIANCE_LOG"
        self.now = now or (lambda: datetime.now(timezone.utc))
        self.test_only_allow_noncanonical_skill_path = test_only_allow_noncanonical_skill_path
        self._cache: Dict[str, Dict[str, Any]] = {}
        self._invocation_ids: Dict[str, str] = {}

    def _integrity(self) -> tuple[bool, Dict[str, Any]]:
        expected = self.contract["skill"]
        details: Dict[str, Any] = {
            "identity": expected["identity"],
            "version": expected["version"],
            "path": str(self.skill_path),
            "expected_sha256": expected["sha256"],
        }
        if not self.test_only_allow_noncanonical_skill_path:
            try:
                if self.skill_path.resolve() != self.canonical_skill_path.resolve():
                    details.update({"passed": False, "reason": "NON_CANONICAL_SKILL_PATH", "actual_sha256": None})
                    return False, details
            except OSError:
                details.update({"passed": False, "reason": "CANONICAL_PATH_RESOLUTION_FAILED", "actual_sha256": None})
                return False, details
        if not self.skill_path.is_file():
            details.update({"passed": False, "reason": "CANONICAL_SKILL_UNAVAILABLE", "actual_sha256": None})
            return False, details
        try:
            metadata = _read_frontmatter(self.skill_path)
            actual_hash = sha256_file(self.skill_path)
        except (OSError, UnicodeError, ValueError) as exc:
            details.update({"passed": False, "reason": "CANONICAL_SKILL_UNREADABLE", "error": type(exc).__name__})
            return False, details
        details.update({"metadata": metadata, "actual_sha256": actual_hash})
        for field in ("name", "version", "status", "review_result"):
            expected_value = expected["identity"] if field == "name" else expected[field]
            if metadata.get(field) != expected_value:
                details.update({"passed": False, "reason": f"SKILL_{field.upper()}_MISMATCH"})
                return False, details
        if actual_hash != expected["sha256"]:
            details.update({"passed": False, "reason": "SKILL_HASH_MISMATCH"})
            return False, details
        missing_refs = [
            relative for relative in expected["critical_references"] if not (self.vault_root / relative).is_file()
        ]
        if missing_refs:
            details.update({"passed": False, "reason": "CRITICAL_REFERENCE_MISSING", "missing": missing_refs})
            return False, details
        decisions = set(self.contract["output"]["decision_mapping"])
        if len(decisions) != 7:
            details.update({"passed": False, "reason": "SEVEN_STATE_MAPPING_INVALID"})
            return False, details
        details.update({"passed": True, "reason": None})
        return True, details

    def _normalize_input(self, envelope: Any) -> tuple[Optional[Dict[str, Any]], Optional[tuple[str, str]]]:
        if not isinstance(envelope, Mapping):
            return None, ("F1", "Runtime envelope must be an object")
        if not _json_safe(envelope):
            return None, ("F1", "Runtime envelope must be JSON-serializable")

        aliases = self.contract["input"]["original_aliases"]
        present = [(name, envelope[name]) for name in aliases if name in envelope]
        if not present:
            return None, ("F2", "Original text is required")
        distinct = {_stable_json(value) for _, value in present}
        if len(distinct) > 1:
            return None, ("F1", "Conflicting Original aliases")
        original = present[0][1]
        if not isinstance(original, str):
            return None, ("F1", "Original text must be a string")
        if not original.strip():
            return None, ("F2", "Original text must not be empty")

        mode_provided = "requested_mode" in envelope
        mode = envelope.get("requested_mode", "QA_DEFAULT")
        if mode not in self.contract["input"]["allowed_modes"]:
            return None, ("F1", "Requested Mode is not allowed")

        register = envelope.get("register")
        if register is not None:
            if not isinstance(register, str):
                return None, ("F1", "Register must be a string or null")
            code = register.strip().split(" ", 1)[0]
            if code not in self.contract["input"]["allowed_register_codes"]:
                return None, ("F1", "Register must use R1-R8 or remain unknown")

        if "skip_qa" in envelope and not isinstance(envelope["skip_qa"], bool):
            return None, ("F1", "skip_qa must be boolean")
        requested_dependencies = envelope.get("requested_dependencies", [])
        if not isinstance(requested_dependencies, list) or not all(isinstance(x, str) for x in requested_dependencies):
            return None, ("F1", "requested_dependencies must be a string list")

        field_map = self.contract["input"]["canonical_fields"]
        canonical_input: Dict[str, Any] = {}
        provenance: Dict[str, str] = {}
        for runtime_name, canonical_name in field_map.items():
            if runtime_name == "original":
                canonical_input[canonical_name] = original
                provenance[canonical_name] = "PROVIDED"
            elif runtime_name == "requested_mode":
                canonical_input[canonical_name] = mode
                provenance[canonical_name] = "PROVIDED" if mode_provided else "DERIVED_SAFELY"
            elif runtime_name in envelope:
                canonical_input[canonical_name] = envelope[runtime_name]
                provenance[canonical_name] = "PROVIDED"
            else:
                canonical_input[canonical_name] = None
                provenance[canonical_name] = "UNKNOWN"

        normalized = {
            "original": original,
            "mode": mode,
            "register": register,
            "canonical_input": canonical_input,
            "context_provenance": provenance,
            "skip_qa": envelope.get("skip_qa", False),
            "requested_dependencies": requested_dependencies,
            "canon_mutation_requested": bool(envelope.get("canon_mutation_requested", False)),
            "showrunner_mutation_requested": bool(envelope.get("showrunner_mutation_requested", False)),
            "invocation_id": envelope.get("invocation_id"),
            "caller": envelope.get("caller", "UNKNOWN"),
        }
        if normalized["invocation_id"] is not None and not isinstance(normalized["invocation_id"], str):
            return None, ("F1", "invocation_id must be a string")
        return normalized, None

    def _invocation_key(self, normalized: Dict[str, Any]) -> str:
        stable = {
            "skill_identity": self.contract["skill"]["identity"],
            "skill_version": self.contract["skill"]["version"],
            "canonical_input": normalized["canonical_input"],
            "skip_qa": normalized["skip_qa"],
            "requested_dependencies": normalized["requested_dependencies"],
            "canon_mutation_requested": normalized["canon_mutation_requested"],
            "showrunner_mutation_requested": normalized["showrunner_mutation_requested"],
        }
        return hashlib.sha256(_stable_json(stable).encode("utf-8")).hexdigest()

    def _write_audit(self, audit: Dict[str, Any]) -> str:
        self.log_dir.mkdir(parents=True, exist_ok=True)
        safe_id = re.sub(r"[^A-Za-z0-9_.-]", "_", audit["invocation_id"])
        target = self.log_dir / f"language-voice-qa-{safe_id}.json"
        target.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
        return str(target)

    def _context_summary(self, normalized: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        if not normalized:
            return {"provided": [], "derived_safely": [], "unknown": []}
        provenance = normalized["context_provenance"]
        return {
            "provided": sorted(key for key, state in provenance.items() if state == "PROVIDED"),
            "derived_safely": sorted(key for key, state in provenance.items() if state == "DERIVED_SAFELY"),
            "unknown": sorted(key for key, state in provenance.items() if state == "UNKNOWN"),
        }

    def _result(
        self,
        *,
        invocation_id: str,
        timestamp: str,
        normalized: Optional[Dict[str, Any]],
        integrity: Dict[str, Any],
        status: str,
        decision: Optional[str],
        severity: Optional[str],
        route: Optional[str],
        action: str,
        final_text: Optional[str],
        rewrite_used: bool,
        handoff: Any,
        contract_passed: bool,
        failure_code: Optional[str] = None,
        failure_message: Optional[str] = None,
        diagnostics: Any = None,
        transport_metadata: Optional[Dict[str, Any]] = None,
        write_log: bool = True,
    ) -> Dict[str, Any]:
        original = normalized["original"] if normalized else None
        audit = {
            "invocation_id": invocation_id,
            "timestamp": timestamp,
            "skill_identity": self.contract["skill"]["identity"],
            "skill_version": self.contract["skill"]["version"],
            "skill_sha256": integrity.get("actual_sha256"),
            "input_mode": normalized["mode"] if normalized else None,
            "context_availability_summary": self._context_summary(normalized),
            "final_decision_state": decision,
            "severity": severity,
            "route": route,
            "rewrite_used": rewrite_used,
            "handoff_occurred": bool(handoff),
            "runtime_contract_passed": contract_passed,
            "failure_code": failure_code,
            "failure_name": self.contract["failure_codes"].get(failure_code) if failure_code else None,
            "integrity_passed": bool(integrity.get("passed")),
        }
        if write_log:
            audit["log_path"] = self._write_audit(audit)
        return {
            "internal_runtime_result": {
                "runtime_status": status,
                "invocation_id": invocation_id,
                "contract_identity": self.contract["contract_identity"],
                "contract_version": self.contract["contract_version"],
                "skill_integrity": integrity,
                "decision": decision,
                "severity": severity,
                "route": route,
                "action": action,
                "rewrite_used": rewrite_used,
                "handoff": handoff,
                "runtime_contract_passed": contract_passed,
                "failure_code": failure_code,
                "failure_message": failure_message,
                "transport_metadata": transport_metadata or {},
            },
            "downstream_payload": {
                "text": final_text if final_text is not None else original,
                "original_preserved": not rewrite_used,
                "decision": decision,
                "severity": severity,
                "route": route,
                "action": action,
                "handoff": handoff,
                "diagnostics": diagnostics,
            },
            "user_facing_result": {
                "status": status,
                "decision": decision,
                "message": failure_message if failure_code else diagnostics,
                "text": final_text if rewrite_used else None,
                "handoff": handoff,
            },
            "audit_record": audit,
        }

    def _failure(
        self,
        code: str,
        message: str,
        *,
        normalized: Optional[Dict[str, Any]],
        integrity: Dict[str, Any],
        invocation_id: Optional[str] = None,
        timestamp: Optional[str] = None,
    ) -> Dict[str, Any]:
        invocation_id = invocation_id or str(uuid.uuid4())
        timestamp = timestamp or self.now().isoformat()
        return self._result(
            invocation_id=invocation_id,
            timestamp=timestamp,
            normalized=normalized,
            integrity=integrity,
            status="FAIL_SAFE",
            decision=None,
            severity=None,
            route=None,
            action="safe_stop",
            final_text=normalized["original"] if normalized else None,
            rewrite_used=False,
            handoff=None,
            contract_passed=False,
            failure_code=code,
            failure_message=message,
        )

    def _validate_output(self, output: Any, normalized: Dict[str, Any]) -> Optional[tuple[str, str]]:
        if not isinstance(output, Mapping):
            return "F4", "Skill output must be an object"
        for field in ("decision", "severity", "route", "mode", "context_state"):
            if field not in output:
                return "F4", f"Skill output missing required field: {field}"
        decision = output["decision"]
        if decision not in self.contract["output"]["decision_mapping"]:
            return "F5", "Skill output contains a non-canonical decision state"
        if output["severity"] not in self.contract["output"]["allowed_severities"]:
            return "F4", "Skill output severity is malformed"
        if not isinstance(output["route"], str) or not output["route"].strip():
            return "F4", "Skill output route is malformed"
        if not isinstance(output["mode"], str) or not output["mode"].strip():
            return "F4", "Skill output mode is malformed"
        if not isinstance(output["context_state"], str) or not output["context_state"].strip():
            return "F4", "Skill output context_state is malformed"
        if output.get("canon_mutation_requested") or output.get("invoke_dependencies"):
            return "F7", "Skill output attempted an unauthorized future dependency or Canon mutation"

        revised = output.get("revised_text")
        if decision != "REWRITE DELIVERED" and revised not in (None, normalized["original"]):
            return "F6", "Non-rewrite decision attempted to replace Original"
        if decision == "REWRITE DELIVERED":
            if normalized["mode"] != "REWRITE_EXPLICIT":
                return "F6", "Rewrite was not explicitly authorized by input mode"
            if not isinstance(revised, str) or not revised.strip():
                return "F6", "Rewrite decision lacks revised_text"
            if _normalize_rewrite_comparison(revised) == _normalize_rewrite_comparison(normalized["original"]):
                return "F6", "Rewrite decision did not produce a real text change"
            if output.get("benefit_result") != "PASS":
                return "F6", "Rewrite decision lacks Benefit PASS"
            rewrite_scope = output.get("rewrite_scope")
            if not rewrite_scope or (isinstance(rewrite_scope, str) and not rewrite_scope.strip()):
                return "F6", "Rewrite decision lacks Rewrite Scope"
            if output.get("meaning_lock_status") not in {"PASS", "LOCKED"}:
                return "F6", "Rewrite decision reports Meaning Lock failure or absence"
            if output.get("rewrite_ceiling_status") != "PASS":
                return "F6", "Rewrite decision lacks Rewrite Ceiling PASS"
            safety = output.get("safety_regression")
            lenses = self.contract["output"]["rewrite_safety_lenses"]
            if not isinstance(safety, Mapping) or set(safety) != set(lenses):
                return "F6", "Rewrite decision has incomplete Safety Regression"
            if any(safety[lens] != "PASS" for lens in lenses):
                return "F6", "Rewrite decision reports Safety Regression failure"
        return None

    def invoke(self, envelope: Any) -> Dict[str, Any]:
        normalized, input_error = self._normalize_input(envelope)
        empty_integrity = {"passed": False, "reason": "NOT_CHECKED"}
        if input_error:
            return self._failure(input_error[0], input_error[1], normalized=normalized, integrity=empty_integrity)
        assert normalized is not None

        key = self._invocation_key(normalized)
        if key in self._cache:
            return copy.deepcopy(self._cache[key])

        invocation_id = normalized["invocation_id"] or str(uuid.uuid4())
        if invocation_id in self._invocation_ids and self._invocation_ids[invocation_id] != key:
            return self._failure(
                "F1",
                "invocation_id was already used for different stable input",
                normalized=normalized,
                integrity=empty_integrity,
                invocation_id=invocation_id,
            )
        timestamp = self.now().isoformat()

        forbidden = set(self.contract["forbidden_runtime_dependencies"])
        if forbidden.intersection(normalized["requested_dependencies"]):
            result = self._failure(
                "F7", "Unauthorized future dependency requested", normalized=normalized,
                integrity=empty_integrity, invocation_id=invocation_id, timestamp=timestamp,
            )
            self._cache[key] = result
            self._invocation_ids[invocation_id] = key
            return copy.deepcopy(result)
        if normalized["canon_mutation_requested"] or normalized["showrunner_mutation_requested"]:
            result = self._failure(
                "F7", "Canon or locked Showrunner mutation requested", normalized=normalized,
                integrity=empty_integrity, invocation_id=invocation_id, timestamp=timestamp,
            )
            self._cache[key] = result
            self._invocation_ids[invocation_id] = key
            return copy.deepcopy(result)

        if normalized["skip_qa"]:
            result = self._result(
                invocation_id=invocation_id, timestamp=timestamp, normalized=normalized,
                integrity={"passed": True, "reason": "SKIPPED_BEFORE_INVOCATION"},
                status="SUCCESS", decision=None, severity=None, route="SKIP_QA",
                action="skip", final_text=normalized["original"], rewrite_used=False,
                handoff=None, contract_passed=True,
                transport_metadata={"invocation_gate": "EXPLICIT_SKIP"},
            )
            self._cache[key] = result
            self._invocation_ids[invocation_id] = key
            return copy.deepcopy(result)

        integrity_ok, integrity = self._integrity()
        if not integrity_ok:
            result = self._failure(
                "F8", integrity["reason"], normalized=normalized, integrity=integrity,
                invocation_id=invocation_id, timestamp=timestamp,
            )
            self._cache[key] = result
            self._invocation_ids[invocation_id] = key
            return copy.deepcopy(result)

        invocation = {
            "canonical_skill": {
                "identity": self.contract["skill"]["identity"],
                "version": self.contract["skill"]["version"],
                "sha256": integrity["actual_sha256"],
            },
            "input": normalized["canonical_input"],
            "context_provenance": normalized["context_provenance"],
            "runtime": {
                "invocation_id": invocation_id,
                "contract_version": self.contract["contract_version"],
                "caller": normalized["caller"],
            },
        }
        try:
            output = self.invoker(copy.deepcopy(invocation))
        except Exception as exc:  # the adapter must preserve Original across executor failures
            result = self._failure(
                "F3", f"Skill executor failed: {type(exc).__name__}", normalized=normalized,
                integrity=integrity, invocation_id=invocation_id, timestamp=timestamp,
            )
            self._cache[key] = result
            self._invocation_ids[invocation_id] = key
            return copy.deepcopy(result)

        output_error = self._validate_output(output, normalized)
        if output_error:
            result = self._failure(
                output_error[0], output_error[1], normalized=normalized, integrity=integrity,
                invocation_id=invocation_id, timestamp=timestamp,
            )
            self._cache[key] = result
            self._invocation_ids[invocation_id] = key
            return copy.deepcopy(result)

        decision = output["decision"]
        action = self.contract["output"]["decision_mapping"][decision]
        rewrite_used = decision == "REWRITE DELIVERED"
        handoff = output.get("role_handoff")
        transport_metadata: Dict[str, Any] = {}
        if output.get("contemporary_state") == "CONTEMPORARY USAGE CHECK REQUIRED":
            transport_metadata.update({
                "handoff_status": "HANDOFF_REQUIRED",
                "dependency_status": "CONTEMPORARY_LAYER_NOT_AVAILABLE",
            })
        final_text = output["revised_text"] if rewrite_used else normalized["original"]
        result = self._result(
            invocation_id=invocation_id,
            timestamp=timestamp,
            normalized=normalized,
            integrity=integrity,
            status="SUCCESS",
            decision=decision,
            severity=output["severity"],
            route=output["route"],
            action=action,
            final_text=final_text,
            rewrite_used=rewrite_used,
            handoff=handoff,
            contract_passed=True,
            diagnostics=output.get("diagnostics"),
            transport_metadata=transport_metadata,
        )
        self._cache[key] = result
        self._invocation_ids[invocation_id] = key
        return copy.deepcopy(result)
