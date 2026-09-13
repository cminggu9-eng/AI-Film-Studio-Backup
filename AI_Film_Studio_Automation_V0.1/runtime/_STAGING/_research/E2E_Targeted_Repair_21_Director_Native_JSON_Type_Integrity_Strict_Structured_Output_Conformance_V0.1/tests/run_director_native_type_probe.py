"""One authorized, raw-first Director-only native JSON type probe."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Dict, Mapping

from repair21_support import R26_ARTIFACTS, current_wire_audit, read_json, validator_for
import run_minimal_e2e as e2e
from director_provider_compatibility import build_deepseek_compatible_director_contract
from provider_response_persistence import persist_provider_response, persist_validation_error
from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter
from runtime.shared_qa.model_executor import ModelExecutionError, ModelExecutor, ModelRequest, assess_response_truncation


PROBE_ID = "DIRECTOR-NATIVE-TYPE-PROBE-21-F03"
PROBE_ROOT = Path(__file__).resolve().parents[1] / "reports" / PROBE_ID
ARTIFACTS = PROBE_ROOT / "artifacts"
SOURCE_INPUT = R26_ARTIFACTS / "director_input.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_report(payload: Mapping[str, Any]) -> None:
    e2e.write_json(PROBE_ROOT / "Director_Native_JSON_Type_Probe_21.json", dict(payload))
    print(json.dumps(dict(payload), ensure_ascii=False, indent=2))


def allowed_container_form(value: Any) -> bool:
    return value == "ABSENT" or (isinstance(value, list) and all(isinstance(item, str) and item.strip() for item in value))


def native_object_or_absent(value: Any) -> bool:
    return value == "ABSENT" or isinstance(value, Mapping)


def main() -> int:
    if PROBE_ROOT.exists():
        write_report({
            "classification": "DIRECTOR STRICT NATIVE JSON TYPE PROBE",
            "probe_id": PROBE_ID,
            "overall": "BLOCKED",
            "detail": "probe evidence path already exists; a second provider probe is forbidden",
            "provider_calls": 0,
            "retry_count": 0,
            "r03_restarted": False,
        })
        return 1

    audit = current_wire_audit()
    strict = build_deepseek_compatible_director_contract(audit["state_contract"])
    source_payload = read_json(SOURCE_INPUT)
    skill_path, skill_hash = e2e.canonical_skill(e2e.role_spec("director"))
    source_binding = source_payload.get("canonical_binding")
    if not isinstance(source_binding, Mapping) or source_binding.get("sha256") != skill_hash or source_payload.get("role") != "Director":
        write_report({
            "classification": "DIRECTOR STRICT NATIVE JSON TYPE PROBE",
            "probe_id": PROBE_ID,
            "overall": "BLOCKED",
            "detail": "R26 source package identity does not match the current Director canonical binding",
            "provider_calls": 0,
            "retry_count": 0,
            "r03_restarted": False,
        })
        return 1

    request_payload = copy.deepcopy(source_payload)
    request_payload["run_id"] = PROBE_ID
    request_payload["canonical_binding"] = {
        "identity": e2e.role_spec("director").identity,
        "canonical_path": str(skill_path),
        "sha256": skill_hash,
    }
    prompt = e2e.build_system_prompt(
        e2e.role_spec("director"),
        skill_path.read_text(encoding="utf-8"),
        run_id=PROBE_ID,
        structured_function_name=strict.function_name,
        structured_parameters_schema=strict.parameters_schema,
    )
    request = ModelRequest(
        system_prompt=prompt,
        user_prompt=json.dumps(request_payload, ensure_ascii=False, separators=(",", ":")),
        model=e2e.MODEL,
        thinking_mode=e2e.THINKING_MODE,
        max_tokens=e2e.role_completion_budget("director"),
        response_format=None,
        structured_output=strict,
    )
    wire_payload, endpoint = DeepSeekProviderAdapter.build_provider_payload(request)
    function = wire_payload["tools"][0]["function"]
    mechanics_pass = (
        function["name"] == "submit_director_package"
        and function.get("strict") is True
        and wire_payload.get("tool_choice") == {"type": "function", "function": {"name": "submit_director_package"}}
        and function["parameters"] == audit["projected"]
    )
    if not mechanics_pass:
        write_report({
            "classification": "DIRECTOR STRICT NATIVE JSON TYPE PROBE",
            "probe_id": PROBE_ID,
            "overall": "BLOCKED",
            "detail": "compiled-to-wire strict mechanics are not authorized for provider send",
            "provider_calls": 0,
            "retry_count": 0,
            "r03_restarted": False,
        })
        return 1

    e2e.write_json(ARTIFACTS / "director_probe_input.json", {
        "probe_id": PROBE_ID,
        "source_input": str(SOURCE_INPUT.resolve()),
        "source_input_sha256": sha256(SOURCE_INPUT),
        "source_run_id": source_payload["run_id"],
        "source_mode": "IMMUTABLE_READ_ONLY_UPSTREAM_PACKAGE_NOT_A_R26_RETRY",
        "request_payload": request_payload,
    })
    e2e.write_json(ARTIFACTS / "director_final_wire_payload.json", {
        "lifecycle_stage": "FINAL_WIRE_PAYLOAD_PERSISTED_BEFORE_SEND",
        "probe_id": PROBE_ID,
        "endpoint": f"{endpoint}/chat/completions",
        "payload": wire_payload,
        "wire_payload_sha256": e2e.sha256_text(e2e.stable_json(wire_payload)),
        "final_parameters_sha256": e2e.sha256_text(e2e.stable_json(function["parameters"])),
        "source_input_sha256": sha256(SOURCE_INPUT),
    })

    invocation_id = f"{PROBE_ID}:director:1"
    executor = ModelExecutor(DeepSeekProviderAdapter())
    started = e2e.utc_now()
    report: Dict[str, Any] = {
        "classification": "DIRECTOR STRICT NATIVE JSON TYPE PROBE",
        "probe_id": PROBE_ID,
        "fixture_id": audit["compiled"]["fixture"]["fixture_id"],
        "upstream_input_source": str(SOURCE_INPUT.resolve()),
        "upstream_input_sha256": sha256(SOURCE_INPUT),
        "upstream_input_mode": "IMMUTABLE_READ_ONLY_NOT_A_R26_RETRY",
        "strict_function_name": strict.function_name,
        "strict_true": function["strict"],
        "tool_choice": copy.deepcopy(wire_payload["tool_choice"]),
        "max_tokens": request.max_tokens,
        "retry_count": 0,
        "provider_calls": 1,
        "executor_calls": 1,
        "role_calls": 1,
        "live_e2e_runs": 0,
        "r03_restarted": False,
        "historical_r26_status": "BLOCKED",
    }
    try:
        receipt = executor.execute_with_receipt(request, invocation_id=invocation_id, fixture_id=audit["compiled"]["fixture"]["fixture_id"])
        raw_response = executor.response_for(invocation_id)
        usage = executor.usage_for(invocation_id)
        if not isinstance(raw_response, Mapping) or not isinstance(usage, Mapping):
            raise ModelExecutionError("raw provider response is unavailable before local validation")
        persistence = persist_provider_response(
            evidence_dir=PROBE_ROOT,
            role="Director",
            invocation_id=invocation_id,
            timestamp=started,
            raw_response=raw_response,
            usage_record=usage,
            input_artifact=str((ARTIFACTS / "director_probe_input.json").resolve()),
        )
        raw_usage = raw_response.get("usage") if isinstance(raw_response.get("usage"), Mapping) else {}
        completion_tokens = raw_usage.get("completion_tokens")
        truncation = assess_response_truncation(
            raw_content=str(raw_response.get("raw_content", "")),
            finish_reason=raw_response.get("finish_reason") if isinstance(raw_response.get("finish_reason"), str) else None,
            completion_tokens=completion_tokens if isinstance(completion_tokens, int) else None,
            requested_max_tokens=request.max_tokens,
        )
        truncation["persistence_verification_artifact"] = persistence["persistence_verification_artifact"]
        e2e.write_json(ARTIFACTS / "director_truncation_detection.json", truncation)
        arguments = executor.extract_required_tool_arguments(receipt, function_name=strict.function_name)
        validated = validator_for(audit["state_contract"])(arguments)
        state = arguments["state_evidence"]
        native_type_pass = (
            allowed_container_form(arguments["unresolved_decisions"])
            and native_object_or_absent(state["relevant_prior_state"])
            and native_object_or_absent(state["current_state"])
            and state["proposed_state"] == "ABSENT"
            and state["knowledge_timing"] == "ABSENT"
            and state["visual_state"] == "ABSENT"
        )
        complete = set(arguments) == set(strict.parameters_schema["required"])
        report.update({
            "raw_first_persistence": persistence,
            "provider_finish_reason": raw_response.get("finish_reason"),
            "truncation": truncation,
            "raw_argument_types": {
                "unresolved_decisions": type(arguments["unresolved_decisions"]).__name__,
                "relevant_prior_state": type(state["relevant_prior_state"]).__name__,
                "current_state": type(state["current_state"]).__name__,
            },
            "function_name_exact": raw_response.get("tool_calls", [{}])[0].get("function", {}).get("name") == strict.function_name,
            "fifteen_field_contract_complete": complete,
            "native_type_pass": native_type_pass,
            "local_strict_validation_pass": isinstance(validated, Mapping),
            "source_trace_pass": state["relevant_prior_state"] == audit["state_contract"]["expected_state_values"]["relevant_prior_state"] and state["current_state"] == audit["state_contract"]["expected_state_values"]["current_state"],
            "overall": "PASS" if complete and native_type_pass and not truncation["truncated"] else "FAIL",
        })
    except Exception as exc:
        raw_response = executor.response_for(invocation_id)
        usage = executor.usage_for(invocation_id)
        persistence = None
        if isinstance(raw_response, Mapping) and isinstance(usage, Mapping):
            persistence = persist_provider_response(
                evidence_dir=PROBE_ROOT,
                role="Director",
                invocation_id=invocation_id,
                timestamp=started,
                raw_response=raw_response,
                usage_record=usage,
                input_artifact=str((ARTIFACTS / "director_probe_input.json").resolve()),
            )
            persist_validation_error(
                evidence_dir=PROBE_ROOT,
                role="Director",
                invocation_id=invocation_id,
                validation_stage="Strict Native JSON Type Probe",
                category="SCHEMA VALIDATION FAILURE",
                detail=f"{type(exc).__name__}: {exc}",
            )
        report.update({
            "overall": "FAIL",
            "failure": f"{type(exc).__name__}: {exc}",
            "raw_first_persistence": persistence,
            "retry_performed": False,
        })
    write_report(report)
    return 0 if report.get("overall") == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
