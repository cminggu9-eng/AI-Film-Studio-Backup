"""Bounded bridge between a canonical QA Handoff and evidence-only retrieval."""

from __future__ import annotations

import copy
import hashlib
import json
from typing import Any, Callable, Dict, Mapping

from runtime.shared_qa.contemporary_language_runtime import ContemporaryLanguageRuntime


QAExecutor = Callable[[Dict[str, Any]], Dict[str, Any]]


class ContemporaryHandoffCoordinator:
    """Run at most one evidence cycle per unresolved claim in a production run.

    The coordinator has no language judgment: it only recognizes the existing
    canonical Handoff, supplies an evidence envelope as Available Context, and
    calls the supplied QA executor again.  It never creates a final QA state.
    """

    _HANDOFF_DECISION = "ROLE HANDOFF / WARNING"
    _HANDOFF_STATE = "CONTEMPORARY USAGE CHECK REQUIRED"

    def __init__(self, qa_executor: QAExecutor, evidence_runtime: ContemporaryLanguageRuntime) -> None:
        self.qa_executor = qa_executor
        self.evidence_runtime = evidence_runtime
        self._completed_cycles: set[str] = set()

    @staticmethod
    def _is_contemporary_handoff(result: Any) -> bool:
        return isinstance(result, Mapping) and (
            result.get("decision") == ContemporaryHandoffCoordinator._HANDOFF_DECISION
            and result.get("contemporary_state") == ContemporaryHandoffCoordinator._HANDOFF_STATE
        )

    @staticmethod
    def _claim_key(request: Mapping[str, Any]) -> str:
        stable = {
            "phrase": request.get("phrase"),
            "question": request.get("question"),
            "scope": request.get("scope"),
            "question_type": request.get("question_type", "USAGE"),
        }
        return hashlib.sha256(
            json.dumps(stable, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
        ).hexdigest()

    def run(self, envelope: Any) -> Dict[str, Any]:
        if not isinstance(envelope, Mapping):
            return {"coordinator_status": "FAIL_SAFE", "failure_code": "CL-C1", "failure_message": "Envelope must be an object"}
        qa_input = envelope.get("qa_input")
        evidence_request = envelope.get("contemporary_request")
        if not isinstance(qa_input, Mapping) or not isinstance(evidence_request, Mapping):
            return {"coordinator_status": "FAIL_SAFE", "failure_code": "CL-C1", "failure_message": "qa_input and contemporary_request are required objects"}
        if qa_input.get("canon_mutation_requested") or qa_input.get("showrunner_mutation_requested"):
            return {"coordinator_status": "FAIL_SAFE", "failure_code": "CL-C2", "failure_message": "Coordinator cannot process Canon or Showrunner mutation requests"}

        try:
            initial = self.qa_executor(copy.deepcopy(dict(qa_input)))
        except Exception as exc:
            return {"coordinator_status": "FAIL_SAFE", "failure_code": "CL-C3", "failure_message": f"Initial QA call failed: {type(exc).__name__}"}
        if not self._is_contemporary_handoff(initial):
            return {
                "coordinator_status": "NO_CONTEMPORARY_HANDOFF",
                "initial_qa_result": copy.deepcopy(initial),
                "evidence_result": None,
                "final_qa_result": None,
            }

        production_run_id = evidence_request.get("production_run_id")
        if not isinstance(production_run_id, str) or not production_run_id.strip():
            return {"coordinator_status": "FAIL_SAFE", "failure_code": "CL-C1", "failure_message": "production_run_id is required"}
        key = f"{production_run_id.strip()}:{self._claim_key(evidence_request)}"
        recheck_reason = envelope.get("recheck_reason")
        exceptions = set(self.evidence_runtime.contract["allowed_recheck_reasons"])
        if key in self._completed_cycles and recheck_reason not in exceptions:
            return {
                "coordinator_status": "LIMIT_REACHED",
                "initial_qa_result": copy.deepcopy(initial),
                "evidence_result": None,
                "final_qa_result": None,
                "limit": "One full evidence cycle per unresolved claim per production run",
            }

        evidence_result = self.evidence_runtime.resolve(copy.deepcopy(dict(evidence_request)))
        self._completed_cycles.add(key)
        callback_input = copy.deepcopy(dict(qa_input))
        prior_context = callback_input.get("available_context")
        if isinstance(prior_context, Mapping):
            merged_context: Dict[str, Any] = copy.deepcopy(dict(prior_context))
        else:
            merged_context = {"upstream_available_context": prior_context} if prior_context is not None else {}
        merged_context["Contemporary Evidence Return"] = copy.deepcopy(evidence_result["evidence_return"])
        callback_input["available_context"] = merged_context
        callback_input["contemporary_evidence_return"] = copy.deepcopy(evidence_result["evidence_return"])
        try:
            final = self.qa_executor(callback_input)
        except Exception as exc:
            return {
                "coordinator_status": "FAIL_SAFE",
                "failure_code": "CL-C4",
                "failure_message": f"QA callback failed: {type(exc).__name__}",
                "initial_qa_result": copy.deepcopy(initial),
                "evidence_result": evidence_result,
                "final_qa_result": None,
            }
        return {
            "coordinator_status": "EVIDENCE_RETURNED_TO_QA",
            "initial_qa_result": copy.deepcopy(initial),
            "evidence_result": evidence_result,
            "final_qa_result": copy.deepcopy(final),
            "cycle_key": key,
        }
