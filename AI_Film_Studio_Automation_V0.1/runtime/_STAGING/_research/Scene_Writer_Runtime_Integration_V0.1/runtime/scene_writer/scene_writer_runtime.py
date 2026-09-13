"""Staging-only transport and contract adapter for canonical ``scene-writer``.

This module deliberately contains no provider client, model executor, semantic
scene generator, or fallback. It receives an already-registered, provider-
neutral canonical dispatch callable; binds one published Skill by exact
identity, version, path, and SHA-256; validates transport contracts; and
returns a technical runtime envelope separate from Scene Writer semantic states.
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Callable, Dict, Mapping, Optional

from runtime.compliance.compliance_gate import sha256_file
from runtime.scene_writer.execution_projection import state_projection_matrix
from runtime.scene_writer.semantic_assignment_integrity import build_assignment_constraint_ledger, validate_semantic_integrity_result


StructuredExecutor = Callable[[Dict[str, Any]], Dict[str, Any]]


class SceneWriterRuntime:
    """Minimal registered adapter with an intentionally unbound real executor."""

    def __init__(
        self,
        *,
        contract_path: Optional[Path] = None,
        executor: Optional[StructuredExecutor] = None,
        semantic_verifier: Optional[StructuredExecutor] = None,
        synthetic_executor: Optional[StructuredExecutor] = None,
        test_sandbox: bool = False,
        execution_classification: str = "PRODUCTION",
    ) -> None:
        self.contract_path = contract_path or Path(__file__).with_name("scene_writer_runtime_contract.json")
        self.contract = json.loads(self.contract_path.read_text(encoding="utf-8"))
        self.project_root = self._find_project_root(Path(__file__).resolve())
        config = json.loads((self.project_root / "studio.config.json").read_text(encoding="utf-8-sig"))
        self.vault_root = Path(config["vault_path"])
        self.canonical_skill_path = (self.vault_root / self.contract["skill"]["canonical_relative_path"]).resolve()
        if executor is not None and synthetic_executor is not None:
            raise ValueError("Real and synthetic executors cannot be registered together")
        if synthetic_executor is not None and not test_sandbox:
            raise ValueError("Synthetic executor is permitted only in TEST SANDBOX")
        if executor is not None and not callable(executor):
            raise ValueError("Registered executor must be callable")
        if semantic_verifier is not None and not callable(semantic_verifier):
            raise ValueError("Semantic verifier must be callable")
        if synthetic_executor is not None and semantic_verifier is not None and not test_sandbox:
            raise ValueError("Synthetic semantic verifier is permitted only in TEST SANDBOX")
        if not isinstance(execution_classification, str) or not execution_classification.strip():
            raise ValueError("execution_classification must be a non-empty string")
        self._synthetic_executor = synthetic_executor
        self._executor = executor
        self._semantic_verifier = semantic_verifier
        self._test_sandbox = test_sandbox
        self._execution_classification = execution_classification
        self._cache: Dict[str, Dict[str, Any]] = {}
        self._request_keys: Dict[str, str] = {}

    @staticmethod
    def _find_project_root(start: Path) -> Path:
        for candidate in (start, *start.parents):
            if (candidate / "studio.config.json").is_file():
                return candidate
        raise RuntimeError("AI Film Studio Automation root not found")

    @staticmethod
    def _stable_json(value: Any) -> str:
        return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str)

    @staticmethod
    def _json_safe(value: Any) -> bool:
        try:
            json.dumps(value, ensure_ascii=False)
            return True
        except (TypeError, ValueError):
            return False

    @staticmethod
    def _frontmatter_identity(path: Path) -> Dict[str, str]:
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0].strip() != "---":
            return {}
        result: Dict[str, str] = {}
        in_metadata = False
        for line in lines[1:]:
            if line.strip() == "---":
                return result
            if line.startswith("metadata:"):
                in_metadata = True
                continue
            if in_metadata and line and not line.startswith((" ", "\t")):
                in_metadata = False
            if ":" not in line or line.lstrip().startswith("#"):
                continue
            key, value = line.split(":", 1)
            normalized_key = key.strip()
            if in_metadata and normalized_key == "display_version":
                result["display_version"] = value.strip().strip("'\"")
            elif not in_metadata and normalized_key == "name":
                result["name"] = value.strip().strip("'\"")
        return {}

    def canonical_binding(self) -> Dict[str, Any]:
        skill = self.contract["skill"]
        details: Dict[str, Any] = {
            "identity": skill["identity"],
            "version": skill["version"],
            "canonical_path": str(self.canonical_skill_path),
            "expected_sha256": skill["sha256"],
            "adapter_status": "REGISTERED",
            "real_executor": "BOUND" if self._executor is not None else "UNBOUND",
            "semantic_integrity_verifier": "BOUND" if self._semantic_verifier is not None else "UNBOUND",
            "synthetic_executor": "ISOLATED_TEST_ONLY" if self._synthetic_executor else "NOT_PRESENT",
        }
        if not self.canonical_skill_path.is_file():
            return {**details, "passed": False, "reason": "CANONICAL_SKILL_UNAVAILABLE", "actual_sha256": None}
        try:
            identity = self._frontmatter_identity(self.canonical_skill_path)
            actual_hash = sha256_file(self.canonical_skill_path).lower()
        except (OSError, UnicodeError, ValueError) as exc:
            return {**details, "passed": False, "reason": "CANONICAL_SKILL_UNREADABLE", "error": type(exc).__name__}
        details.update({"actual_sha256": actual_hash, "metadata": identity})
        if identity.get("name") != skill["identity"]:
            return {**details, "passed": False, "reason": "CANONICAL_IDENTITY_MISMATCH"}
        if identity.get("display_version") != skill["version"]:
            return {**details, "passed": False, "reason": "CANONICAL_VERSION_MISMATCH"}
        if actual_hash != skill["sha256"]:
            return {**details, "passed": False, "reason": "CANONICAL_HASH_MISMATCH"}
        return {**details, "passed": True, "reason": None}

    def registry_status(self) -> Dict[str, str]:
        return {
            "adapter": "REGISTERED",
            "canonical_skill": "RESOLVABLE" if self.canonical_binding().get("passed") else "FAIL_SAFE",
            "real_semantic_executor": "BOUND" if self._executor is not None else "UNBOUND",
            "semantic_integrity_verifier": "BOUND" if self._semantic_verifier is not None else "UNBOUND",
            "synthetic_executor": "ISOLATED_TEST_ONLY" if self._synthetic_executor else "NOT_PRESENT",
        }

    def _runtime_result(
        self,
        *,
        runtime_status: str,
        request_id: Optional[str],
        binding: Dict[str, Any],
        failure_code: Optional[str] = None,
        failure_message: Optional[str] = None,
        scene_writer: Optional[Dict[str, Any]] = None,
        idempotency: str = "NEW",
        output_language: Optional[str] = None,
        output_language_resolution: Optional[str] = None,
        assignment_fact_validation: Optional[Dict[str, Any]] = None,
        semantic_integrity_validation: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return {
            "runtime_status": runtime_status,
            "runtime_failure_code": failure_code,
            "runtime_failure_message": failure_message,
            "request_id": request_id,
            "canonical_binding": binding,
            "idempotency": idempotency,
            "scene_writer": scene_writer,
            "output_language": output_language,
            "output_language_resolution": output_language_resolution,
            "assignment_fact_validation": assignment_fact_validation,
            "semantic_integrity_validation": semantic_integrity_validation,
        }

    def _contract_error(self, request_id: Optional[str], code: str, message: str) -> Dict[str, Any]:
        return self._runtime_result(
            runtime_status="CONTRACT_ERROR", request_id=request_id, binding=self.canonical_binding(),
            failure_code=code, failure_message=message,
        )

    def _fail_safe(self, request_id: Optional[str], binding: Dict[str, Any], code: str, message: str) -> Dict[str, Any]:
        return self._runtime_result(
            runtime_status="FAIL_SAFE", request_id=request_id, binding=binding,
            failure_code=code, failure_message=message,
        )

    def _normalize_input(self, envelope: Any) -> tuple[Optional[Dict[str, Any]], Optional[tuple[str, str]], Optional[str]]:
        if not isinstance(envelope, Mapping):
            return None, ("INVALID_ENVELOPE", "Runtime input must be a JSON object"), None
        if not self._json_safe(envelope):
            return None, ("NON_JSON_INPUT", "Runtime input must be JSON-serializable"), None
        required = self.contract["input"]["required_fields"]
        missing = [field for field in required if field not in envelope]
        if missing:
            return None, ("MISSING_TRANSPORT_FIELD", "Missing transport field: " + ", ".join(missing)), None
        request_id = envelope.get("request_id")
        if not isinstance(request_id, str) or not request_id.strip():
            return None, ("INVALID_REQUEST_ID", "request_id must be a non-empty string"), None
        mode = envelope.get("requested_mode")
        if mode not in self.contract["input"]["allowed_modes"]:
            return None, ("ILLEGAL_MODE", "requested_mode must be one exact canonical token"), None
        allowed = {"request_id", "requested_mode", *self.contract["input"]["transport_fields"]}
        unknown = sorted(set(envelope) - allowed)
        if unknown:
            return None, ("UNKNOWN_TRANSPORT_FIELD", "Unsupported transport field: " + ", ".join(unknown)), None
        normalized = {key: copy.deepcopy(envelope.get(key)) for key in allowed if key in envelope}
        for field in self.contract["input"]["transport_fields"]:
            normalized.setdefault(field, None)
        policy = self.contract["input"]["output_language_policy"]
        allowed_languages = set(policy["allowed_values"])
        explicit_language = normalized["output_language"]
        assignment_language = normalized["assignment_language"]
        if explicit_language is not None:
            if not isinstance(explicit_language, str) or explicit_language not in allowed_languages:
                return None, ("INVALID_OUTPUT_LANGUAGE", "output_language must be one exact supported language token"), None
            normalized["output_language"] = explicit_language
            return normalized, None, "EXPLICIT"
        if assignment_language is not None:
            if not isinstance(assignment_language, str) or assignment_language not in allowed_languages:
                return None, ("INVALID_ASSIGNMENT_LANGUAGE", "assignment_language must be one exact supported language token"), None
            normalized["output_language"] = assignment_language
            return normalized, None, "INHERIT_ASSIGNMENT_LANGUAGE"
        return None, ("OUTPUT_LANGUAGE_UNRESOLVED", "output_language is absent and no explicit assignment_language can be inherited"), None

    def _request_key(self, normalized: Dict[str, Any]) -> str:
        payload = {key: value for key, value in normalized.items() if key != "request_id"}
        return hashlib.sha256(self._stable_json(payload).encode("utf-8")).hexdigest()

    def _validate_handoff(self, packet: Any) -> Optional[str]:
        if not isinstance(packet, Mapping):
            return "Handoff must be an object"
        required = set(self.contract["output"]["handoff_fields"])
        if set(packet) != required:
            return "Handoff must contain exactly the canonical packet fields"
        if not isinstance(packet["target_owner"], str) or not packet["target_owner"].strip():
            return "Handoff target_owner must be a non-empty string"
        for field in ("reason", "scene_function", "decision_needed", "scene_writer_did_not_decide"):
            if not isinstance(packet[field], str) or not packet[field].strip():
                return f"Handoff {field} must be a non-empty string"
        if not isinstance(packet["relevant_locks"], list):
            return "Handoff relevant_locks must be a list"
        return None

    @staticmethod
    def _language_error(text: Any, language: str, location: str) -> Optional[str]:
        if not isinstance(text, str) or not text.strip():
            return f"{location} must be a non-empty text value for output language validation"
        han = len(re.findall(r"[\u3400-\u4dbf\u4e00-\u9fff]", text))
        latin = len(re.findall(r"[A-Za-z]", text))
        if language == "zh-CN":
            if han == 0 or han * 4 < latin:
                return f"{location} does not satisfy zh-CN output-language validation"
        elif language == "en-US":
            if latin < 3 or han > max(4, latin // 20):
                return f"{location} does not satisfy en-US output-language validation"
        else:
            return "Runtime received an unsupported resolved output language"
        return None

    def _validate_output_language(self, creative: Any, control: Mapping[str, Any], language: str) -> Optional[str]:
        if creative is not None:
            error = self._language_error(creative["content"], language, "creative_deliverable.content")
            if error:
                return error
        for field in (
            "scene_function", "objectives", "resistance", "before_state", "state_after", "turn",
            "entry_rationale", "exit_rationale", "production_burden", "unresolved_issue",
            "diagnosis_summary", "upstream_decision_needed", "out_of_scope_boundary",
        ):
            if control.get(field) is not None:
                error = self._language_error(control[field], language, f"control_data.{field}")
                if error:
                    return error
        missing_context = control.get("material_missing_context")
        if isinstance(missing_context, Mapping):
            for field in ("missing", "why_material"):
                error = self._language_error(missing_context.get(field), language, f"control_data.material_missing_context.{field}")
                if error:
                    return error
        for index, packet in enumerate(control.get("handoffs", [])):
            for field in ("reason", "scene_function", "decision_needed", "scene_writer_did_not_decide"):
                error = self._language_error(packet[field], language, f"control_data.handoffs[{index}].{field}")
                if error:
                    return error
            for lock_index, lock in enumerate(packet["relevant_locks"]):
                error = self._language_error(lock, language, f"control_data.handoffs[{index}].relevant_locks[{lock_index}]")
                if error:
                    return error
        return None

    @staticmethod
    def _text_values(value: Any) -> list[str]:
        if isinstance(value, str):
            return [value]
        if isinstance(value, Mapping):
            collected: list[str] = []
            for nested in value.values():
                collected.extend(SceneWriterRuntime._text_values(nested))
            return collected
        if isinstance(value, list):
            collected = []
            for nested in value:
                collected.extend(SceneWriterRuntime._text_values(nested))
            return collected
        return []

    def _assignment_fact_profile(self, normalized: Mapping[str, Any]) -> Dict[str, Any]:
        source_fields = (
            "canon_locks", "showrunner_locks", "participants", "character_context", "required_event",
            "required_information", "required_outcome", "prior_scene_state", "desired_post_state",
            "production_constraints", "scene_purpose", "repair_target",
        )
        source_text = "\n".join(
            text for field in source_fields for text in self._text_values(normalized.get(field))
        )
        source_lower = source_text.lower()
        profile = ["LOCKED_FACT_PRESERVATION", "UNSPECIFIED_FACT_PROHIBITION", "CHARACTER_KNOWLEDGE_SCOPE"]
        explicit_unknown_reason = bool(
            re.search(r"\breason\b.{0,48}\bunknown\b|\bunknown\b.{0,48}\breason\b|原因.{0,12}(未知|不明)|未知.{0,12}原因", source_text, re.IGNORECASE)
        )
        if explicit_unknown_reason:
            profile.append("EXPLICIT_UNKNOWN_REASON")
        coarse_tonight = bool(re.search(r"\btonight\b|今晚", source_lower, re.IGNORECASE))
        if coarse_tonight:
            profile.append("COARSE_TIME_TONIGHT")
        return {"source_text": source_text, "profile": profile}

    @staticmethod
    def _unsupported_pattern_found(output_text: str, source_text: str, pattern: str) -> bool:
        return bool(re.search(pattern, output_text, re.IGNORECASE)) and not bool(re.search(pattern, source_text, re.IGNORECASE))

    def _validate_assignment_facts(self, creative: Any, control: Mapping[str, Any], normalized: Mapping[str, Any]) -> Dict[str, Any]:
        profile_data = self._assignment_fact_profile(normalized)
        source_text = profile_data["source_text"]
        output_text = "\n".join(self._text_values(creative) + self._text_values(control))
        violations: list[Dict[str, str]] = []

        if "EXPLICIT_UNKNOWN_REASON" in profile_data["profile"]:
            unknown_reason_patterns = (
                r"临时有(?:事|状况|情况)", r"突发情况", r"家里有事", r"身体原因", r"个人原因", r"紧急情况",
                r"\btemporary (?:issue|problem|emergency)\b", r"\bfamily issue\b", r"\bpersonal issue\b",
                r"\bhealth (?:reason|issue)\b", r"\bemergency\b",
            )
            if any(self._unsupported_pattern_found(output_text, source_text, pattern) for pattern in unknown_reason_patterns):
                violations.append({"code": "EXPLICIT_UNKNOWN_REASON_CONCRETIZED", "message": "An explicitly unknown absence reason was narrowed into an unsupported category"})

        if "COARSE_TIME_TONIGHT" in profile_data["profile"]:
            deadline_patterns = (
                r"今晚\s*(?:(?:\d{1,2}|[一二三四五六七八九十]{1,3})\s*点(?:前|后)?|午夜)", r"(?:一|两|三|半|\d+)\s*(?:小时|分钟)(?:内|后)",
                r"\b(?:by|before)\s+(?:midnight|\d{1,2}(?::\d{2})?\s*(?:am|pm)?)\b",
                r"\bwithin\s+\d+\s+(?:hours?|minutes?)\b",
            )
            if any(self._unsupported_pattern_found(output_text, source_text, pattern) for pattern in deadline_patterns):
                violations.append({"code": "COARSE_TIME_CONCRETIZED", "message": "A coarse Assignment time was converted into an unsupported precise deadline or duration"})

        capability_patterns = (
            r"比谁都(?:懂|擅长|合适)", r"最(?:懂|擅长|合适)", r"\bbetter than\b", r"\bmost capable\b", r"\bonly one who can\b",
        )
        if any(self._unsupported_pattern_found(output_text, source_text, pattern) for pattern in capability_patterns):
            violations.append({"code": "UNSUPPORTED_CAPABILITY_RANKING", "message": "An unsupported capability comparison or ranking was added"})

        relationship_patterns = (
            r"我们以前(?:一起|就)", r"一直以来", r"认识这么多年", r"当年", r"\bwe used to\b", r"\byears ago\b", r"\bsince college\b",
        )
        if any(self._unsupported_pattern_found(output_text, source_text, pattern) for pattern in relationship_patterns):
            violations.append({"code": "UNSUPPORTED_RELATIONSHIP_HISTORY", "message": "An unsupported relationship-history fact was added"})

        knowledge_source_patterns = (
            r"从.{0,18}(?:那里|处)(?:知道|听说)", r"(?:有人|同事|领导|人事).{0,12}(?:告诉|说)",
            r"\bheard from\b", r"\btold by\b", r"\blearned from\b",
        )
        if any(self._unsupported_pattern_found(output_text, source_text, pattern) for pattern in knowledge_source_patterns):
            violations.append({"code": "UNSUPPORTED_CHARACTER_KNOWLEDGE_SOURCE", "message": "A character knowledge source absent from the Assignment was added"})

        return {"status": "FAIL" if violations else "PASS", "guard_profile": profile_data["profile"], "violations": violations}

    def _validate_output(self, output: Any, normalized: Dict[str, Any]) -> Optional[str]:
        if not isinstance(output, Mapping):
            return "Executor output must be an object"
        if set(output) != {"creative_deliverable", "control_data"}:
            return "Executor output must contain only creative_deliverable and control_data"
        creative = output["creative_deliverable"]
        control = output["control_data"]
        if creative is not None:
            if not isinstance(creative, Mapping) or set(creative) != {"kind", "content"}:
                return "Creative deliverable must be null or an exact kind/content object"
            if creative["kind"] not in self.contract["output"]["creative_kinds"]:
                return "Creative deliverable kind is invalid"
            if not isinstance(creative["content"], str) or not creative["content"].strip():
                return "Creative deliverable content must be a non-empty string"
        if not isinstance(control, Mapping):
            return "control_data must be an object"
        allowed_control = set(self.contract["output"]["control_fields"])
        if "primary_state" not in control or "flags" not in control or "handoffs" not in control:
            return "control_data requires primary_state, flags, and handoffs"
        unknown_control = set(control) - allowed_control
        if unknown_control:
            return "control_data has unsupported fields"
        state = control["primary_state"]
        if not isinstance(state, str) or state not in self.contract["output"]["primary_states"]:
            return "primary_state must be one exact canonical token"
        flags = control["flags"]
        if not isinstance(flags, list) or not all(isinstance(flag, str) for flag in flags):
            return "flags must be a string list"
        if len(flags) != len(set(flags)) or any(flag not in self.contract["output"]["flags"] for flag in flags):
            return "flags must be unique exact canonical tokens"
        handoffs = control["handoffs"]
        if not isinstance(handoffs, list):
            return "handoffs must be a list"
        for packet in handoffs:
            error = self._validate_handoff(packet)
            if error:
                return error
        projection = state_projection_matrix()[state]
        if normalized["requested_mode"] not in projection["valid_modes"]:
            return f"{state} is not valid for {normalized['requested_mode']} transport"
        for field in projection["forbidden_non_null_control_fields"]:
            if control.get(field) is not None:
                return f"{state} forbids non-null control_data.{field}"
        if state == "SCENE_CREATED" and (creative is None or creative["kind"] != "scene"):
            return "SCENE_CREATED requires a scene creative deliverable"
        if state == "SCENE_REVISED" and (creative is None or creative["kind"] != "revision"):
            return "SCENE_REVISED requires a revision creative deliverable"
        if state == "NO_MATERIAL_CHANGE":
            if creative is not None or control.get("material_rewrite_claimed") is not False:
                return "NO_MATERIAL_CHANGE forbids a creative rewrite and requires material_rewrite_claimed=false"
            if normalized["requested_mode"] == "DIAGNOSE":
                summary = control.get("diagnosis_summary")
                if not isinstance(summary, str) or not summary.strip():
                    return "DIAGNOSE NO_MATERIAL_CHANGE requires a non-empty diagnosis_summary"
        if state == "NEEDS_CONTEXT":
            if creative is not None:
                return "NEEDS_CONTEXT forbids a creative deliverable"
            missing = control.get("material_missing_context")
            if not isinstance(missing, Mapping) or set(missing) != {"missing", "why_material", "target_owner"}:
                return "NEEDS_CONTEXT requires exact material_missing_context summary"
            if not all(isinstance(missing[field], str) and missing[field].strip() for field in missing):
                return "material_missing_context fields must be non-empty strings"
        if state == "UPSTREAM_DECISION_REQUIRED":
            if creative is not None:
                return "UPSTREAM_DECISION_REQUIRED forbids a creative deliverable"
            if not isinstance(control.get("upstream_decision_needed"), str) or not control["upstream_decision_needed"].strip():
                return "UPSTREAM_DECISION_REQUIRED requires upstream_decision_needed"
            if "UPSTREAM_HANDOFF_REQUIRED" not in flags:
                return "UPSTREAM_DECISION_REQUIRED requires UPSTREAM_HANDOFF_REQUIRED"
            if not handoffs:
                return "UPSTREAM_DECISION_REQUIRED requires at least one lawful handoff packet"
        if state == "REQUEST_OUT_OF_SCOPE":
            if creative is not None:
                return "REQUEST_OUT_OF_SCOPE forbids a creative deliverable"
            if not isinstance(control.get("out_of_scope_boundary"), str) or not control["out_of_scope_boundary"].strip():
                return "REQUEST_OUT_OF_SCOPE requires out_of_scope_boundary"
        language_error = self._validate_output_language(creative, control, normalized["output_language"])
        if language_error:
            return language_error
        return None

    def execute(self, envelope: Any) -> Dict[str, Any]:
        normalized, input_error, output_language_resolution = self._normalize_input(envelope)
        request_id = envelope.get("request_id") if isinstance(envelope, Mapping) else None
        if input_error:
            return self._contract_error(request_id, input_error[0], input_error[1])
        assert normalized is not None
        key = self._request_key(normalized)
        previous_key = self._request_keys.get(normalized["request_id"])
        if previous_key is not None:
            if previous_key != key:
                return self._contract_error(normalized["request_id"], "DUPLICATE_REQUEST_ID_CONFLICT", "request_id was reused with different input")
            cached = copy.deepcopy(self._cache[previous_key])
            cached["idempotency"] = "DUPLICATE_REPLAY"
            return cached
        binding = self.canonical_binding()
        if not binding["passed"]:
            result = self._fail_safe(normalized["request_id"], binding, "CANONICAL_BINDING_FAILURE", binding["reason"])
        elif self._synthetic_executor is None and self._executor is None:
            result = self._fail_safe(normalized["request_id"], binding, "EXECUTOR_UNBOUND", "No real semantic executor is registered")
        elif self._executor is not None and self._semantic_verifier is None:
            result = self._fail_safe(normalized["request_id"], binding, "SEMANTIC_VERIFIER_UNBOUND", "No semantic assignment integrity verifier is registered")
        else:
            executor = self._synthetic_executor or self._executor
            assert executor is not None
            ledger = build_assignment_constraint_ledger(normalized)
            invocation = {
                "canonical_skill": {
                    "identity": binding["identity"], "version": binding["version"], "sha256": binding["actual_sha256"],
                    "path": binding["canonical_path"],
                },
                "input": copy.deepcopy(normalized),
                "runtime": {
                    "contract_identity": self.contract["contract_identity"],
                    "contract_version": self.contract["contract_version"],
                    "classification": "SYNTHETIC / NON-CANON / NON-SEMANTIC" if self._test_sandbox else self._execution_classification,
                    "invocation_id": f"scene-writer:{normalized['request_id']}",
                    "caller": normalized.get("scene_id") or "scene-writer-runtime",
                    "output_language": normalized["output_language"],
                    "output_language_resolution": output_language_resolution,
                    "assignment_constraint_ledger": copy.deepcopy(ledger),
                },
            }
            try:
                output = executor(copy.deepcopy(invocation))
            except Exception as exc:
                result = self._fail_safe(normalized["request_id"], binding, "EXECUTOR_FAILURE", type(exc).__name__)
            else:
                output_error = self._validate_output(output, normalized)
                if output_error:
                    result = self._fail_safe(normalized["request_id"], binding, "MALFORMED_EXECUTOR_OUTPUT", output_error)
                else:
                    fact_validation = self._validate_assignment_facts(output["creative_deliverable"], output["control_data"], normalized)
                    if fact_validation["status"] != "PASS":
                        result = self._fail_safe(
                            normalized["request_id"], binding, "ASSIGNMENT_FACT_LOCK_VIOLATION",
                            "; ".join(item["code"] for item in fact_validation["violations"]),
                        )
                        result["output_language"] = normalized["output_language"]
                        result["output_language_resolution"] = output_language_resolution
                        result["assignment_fact_validation"] = fact_validation
                    else:
                        if self._semantic_verifier is None:
                            integrity_validation: Dict[str, Any] = {
                                "integrity_result": "NOT_RUN_TEST_SANDBOX",
                                "violations": [],
                                "classification": "SYNTHETIC / NON-CANON / NON-SEMANTIC",
                            }
                            verifier_failed = False
                        else:
                            verification_invocation = {
                                "assignment_constraint_ledger": copy.deepcopy(ledger),
                                "generated_creative_deliverable": copy.deepcopy(output["creative_deliverable"]),
                                "relevant_control_data": copy.deepcopy(output["control_data"]),
                                "runtime": {
                                    "invocation_id": f"scene-writer-integrity:{normalized['request_id']}",
                                    "scene_writer_invocation_id": f"scene-writer:{normalized['request_id']}",
                                    "classification": invocation["runtime"]["classification"],
                                },
                            }
                            try:
                                integrity_validation = self._semantic_verifier(copy.deepcopy(verification_invocation))
                                integrity_validation = validate_semantic_integrity_result(integrity_validation)
                                verifier_failed = False
                            except Exception as exc:
                                result = self._fail_safe(normalized["request_id"], binding, "SEMANTIC_VERIFIER_FAILURE", type(exc).__name__)
                                result["output_language"] = normalized["output_language"]
                                result["output_language_resolution"] = output_language_resolution
                                result["assignment_fact_validation"] = fact_validation
                                integrity_validation = None
                                verifier_failed = True
                        if verifier_failed:
                            pass
                        elif not isinstance(integrity_validation, Mapping) or integrity_validation.get("integrity_result") not in {"PASS", "FAIL", "NOT_RUN_TEST_SANDBOX"} or not isinstance(integrity_validation.get("violations"), list):
                            result = self._fail_safe(normalized["request_id"], binding, "SEMANTIC_VERIFIER_FAILURE", "Verifier returned an invalid runtime result")
                            result["output_language"] = normalized["output_language"]
                            result["output_language_resolution"] = output_language_resolution
                            result["assignment_fact_validation"] = fact_validation
                            result["semantic_integrity_validation"] = copy.deepcopy(dict(integrity_validation)) if isinstance(integrity_validation, Mapping) else None
                        elif integrity_validation["integrity_result"] == "FAIL":
                            result = self._fail_safe(normalized["request_id"], binding, "SEMANTIC_INTEGRITY_VIOLATION", "Semantic Assignment Integrity Verification returned FAIL")
                            result["output_language"] = normalized["output_language"]
                            result["output_language_resolution"] = output_language_resolution
                            result["assignment_fact_validation"] = fact_validation
                            result["semantic_integrity_validation"] = copy.deepcopy(dict(integrity_validation))
                        else:
                            result = self._runtime_result(
                                runtime_status="SUCCESS", request_id=normalized["request_id"], binding=binding,
                                scene_writer=copy.deepcopy(output), output_language=normalized["output_language"],
                                output_language_resolution=output_language_resolution,
                                assignment_fact_validation=fact_validation,
                                semantic_integrity_validation=copy.deepcopy(dict(integrity_validation)),
                            )
        self._request_keys[normalized["request_id"]] = key
        self._cache[key] = copy.deepcopy(result)
        return copy.deepcopy(result)
