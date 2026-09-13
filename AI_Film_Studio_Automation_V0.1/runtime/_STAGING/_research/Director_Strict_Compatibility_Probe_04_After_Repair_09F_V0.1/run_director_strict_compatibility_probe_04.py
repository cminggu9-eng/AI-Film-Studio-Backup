"""One authorized Director-only strict compatibility Probe 04 after Repair 09F.

This probe invokes the existing production CanonicalRoleExecutor exactly once.
It never retries, rewrites a request/payload, or calls an additional role.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parent
AUTOMATION = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION / "runtime" / "_STAGING" / "_research"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
for directory in (
    HARNESS,
    RESEARCH / "E2E_Targeted_Repair_09D_Director_Strict_Provider_Observability_Conformance_V0.1" / "implementation",
):
    sys.path.insert(0, str(directory))
os.environ["AFS_E2E_FIXTURE_BINDING"] = str(
    RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1"
    / "fixtures" / "E2E_FIX_01_Runtime_Binding_V0.1.json"
)

import run_minimal_e2e as e2e
from deepseek_strict_linter import lint
from director_provider_compatibility import (
    PROJECTION_ID,
    build_deepseek_compatible_director_contract,
    deepseek_compatible_schema,
)
from director_structured_submission import (
    FUNCTION_NAME,
    JSON_OBJECT_STRING_STATE_FIELDS,
    deterministic_display_projection,
    director_structured_contract_manifest,
    director_submission_schema,
)
from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter
from runtime.shared_qa.model_executor import ModelRequest


RUN_ID = "DIRECTOR-STRICT-COMPATIBILITY-PROBE-04"
EVIDENCE = ROOT / "evidence" / RUN_ID
SOURCE = HARNESS / "evidence" / "E2E-RUN-12"
EXPECTED_POINTERS = (
    "/properties/flags", "/properties/handoffs", "/properties/unresolved_decisions/anyOf/0",
    "/properties/state_evidence/properties/relevant_prior_state/anyOf/0",
    "/properties/state_evidence/properties/current_state/anyOf/0",
    "/properties/state_evidence/properties/proposed_state/anyOf/0",
    "/properties/state_evidence/properties/knowledge_timing/anyOf/0",
    "/properties/state_evidence/properties/relationship_state/anyOf/0",
    "/properties/state_evidence/properties/visual_state/anyOf/0",
)


def stable_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def write_markdown(path: Path, title: str, values: Mapping[str, Any]) -> None:
    lines = [f"# {title}", ""]
    for key, value in values.items():
        rendered = json.dumps(value, ensure_ascii=False, indent=2) if isinstance(value, (dict, list)) else str(value)
        lines.extend((f"## {key}", "", rendered, ""))
    path.write_text("\n".join(lines), encoding="utf-8")


def node_at(schema: Mapping[str, Any], pointer: str) -> Any:
    value: Any = schema
    for part in pointer.strip("/").split("/"):
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def source_artifacts() -> dict[str, Path]:
    return {
        "director_input": SOURCE / "artifacts" / "director_input.json",
        "scene_writer_output": SOURCE / "artifacts" / "scene_writer_output.json",
        "showrunner_output": SOURCE / "artifacts" / "showrunner_output.json",
    }


def build_exact_request(director_input: Mapping[str, Any], contract: Any) -> tuple[ModelRequest, dict[str, Any], str]:
    spec = e2e.role_spec("director")
    skill_path, skill_hash = e2e.canonical_skill(spec)
    request_payload = {
        "run_id": RUN_ID,
        "role": spec.display_name,
        "canonical_binding": {"identity": spec.identity, "canonical_path": str(skill_path), "sha256": skill_hash},
        "selected_mode": spec.selected_mode,
        "output_language": e2e.OUTPUT_LANGUAGE,
        "input": director_input,
    }
    request = ModelRequest(
        system_prompt=e2e.build_system_prompt(
            spec, skill_path.read_text(encoding="utf-8"), run_id=RUN_ID,
            structured_function_name=contract.function_name,
            structured_parameters_schema=contract.parameters_schema,
        ),
        user_prompt=json.dumps(request_payload, ensure_ascii=False, separators=(",", ":")),
        model=e2e.MODEL,
        thinking_mode=e2e.THINKING_MODE,
        max_tokens=e2e.role_completion_budget(spec.key),
        response_format=None,
        structured_output=contract,
    )
    payload, endpoint = DeepSeekProviderAdapter.build_provider_payload(request)
    return request, payload, endpoint


def preflight() -> dict[str, Any]:
    contract = build_deepseek_compatible_director_contract()
    neutral_manifest = director_structured_contract_manifest()
    function_manifest = director_structured_contract_manifest(contract.parameters_schema)
    validator_manifest = director_structured_contract_manifest()
    if not (neutral_manifest["allowed_fields"] == function_manifest["allowed_fields"] == validator_manifest["allowed_fields"]):
        raise RuntimeError("prompt/function/validator allowed-field manifest drift")
    if not (neutral_manifest["required_fields"] == function_manifest["required_fields"] == validator_manifest["required_fields"]):
        raise RuntimeError("prompt/function/validator required-field manifest drift")
    if len(function_manifest["allowed_fields"]) != 15:
        raise RuntimeError("Director strict contract must contain exactly 15 fields")
    schema = deepseek_compatible_schema()
    typed_absence = {"type": "string", "enum": ["ABSENT"]}
    if lint(schema):
        raise RuntimeError("DeepSeek strict linter failed")
    if not all(node_at(schema, pointer) == typed_absence for pointer in EXPECTED_POINTERS):
        raise RuntimeError("all nine typed ABSENT nodes must be preserved")
    hashes = {spec.key: e2e.canonical_skill(spec)[1] for spec in e2e.ROLE_SPECS}
    if hashes != e2e.EXPECTED_HASHES:
        raise RuntimeError("canonical Skill hash drift blocks Provider send")
    sources = source_artifacts()
    if not all(path.is_file() for path in sources.values()):
        raise RuntimeError("frozen upstream artifacts are unavailable")
    director_record = json.loads(sources["director_input"].read_text(encoding="utf-8"))
    director_input = director_record.get("input")
    if not isinstance(director_input, Mapping):
        raise RuntimeError("frozen Director input shape is invalid")
    request, wire_payload, endpoint = build_exact_request(director_input, contract)
    legacy_schema_reference_count = request.system_prompt.count("REQUIRED TRANSPORT SCHEMA:")
    if legacy_schema_reference_count != 0:
        raise RuntimeError("legacy generic transport schema reference blocks Provider send")
    if wire_payload.get("tool_choice", {}).get("function", {}).get("name") != FUNCTION_NAME:
        raise RuntimeError("exact Director function binding is missing")
    return {
        "result": "PASS",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "run_id": RUN_ID,
        "fixture_binding": os.environ["AFS_E2E_FIXTURE_BINDING"],
        "compiled_run_contract": e2e.compiled_run_contract(),
        "source_artifacts": {name: {"path": str(path), "sha256": sha256_file(path)} for name, path in sources.items()},
        "director_structured_contract_version": "Director Full Structured Submission V0.1",
        "compatibility_projection_version": PROJECTION_ID,
        "prompt_contract_version": "Repair 09F deterministic structured prompt V0.1",
        "validator_version": "Repair 09F exact Director payload validator V0.1",
        "function_name": FUNCTION_NAME,
        "strict": True,
        "endpoint": f"{endpoint}/chat/completions",
        "model": request.model,
        "token_budget": request.max_tokens,
        "invocation_id": f"{RUN_ID}:director:1",
        "prompt_allowed_field_manifest": function_manifest["allowed_fields"],
        "function_schema_property_manifest": function_manifest["allowed_fields"],
        "validator_expected_field_manifest": validator_manifest["allowed_fields"],
        "required_field_manifest": function_manifest["required_fields"],
        "manifest_hashes": {
            "provider_neutral_contract": stable_hash(director_submission_schema()),
            "prompt_projection": stable_hash(request.system_prompt),
            "compatibility_projection": stable_hash(contract.parameters_schema),
            "final_parameters": stable_hash(wire_payload["tools"][0]["function"]["parameters"]),
            "final_wire_payload": stable_hash(wire_payload),
            "prompt_allowed_fields": stable_hash(function_manifest["allowed_fields"]),
            "function_fields": stable_hash(function_manifest["allowed_fields"]),
            "validator_fields": stable_hash(validator_manifest["allowed_fields"]),
        },
        "legacy_generic_transport_schema_reference_count": legacy_schema_reference_count,
        "nine_typed_enum_pointers": list(EXPECTED_POINTERS),
        "canonical_skill_hashes": hashes,
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "retries": 0,
        "fallbacks": 0,
        "request": request,
        "wire_payload": wire_payload,
        "director_input": dict(director_input),
    }


def public_preflight(value: Mapping[str, Any]) -> dict[str, Any]:
    return {key: item for key, item in value.items() if key not in {"request", "wire_payload", "director_input"}}


def persist_before_send(value: Mapping[str, Any]) -> None:
    request = value["request"]
    wire_payload = value["wire_payload"]
    write_json(EVIDENCE / "preflight_manifest.json", public_preflight(value))
    write_json(EVIDENCE / "artifacts" / "director_pre_send_contract_evidence.json", {
        "lifecycle_stage": "PERSISTED_BEFORE_NETWORK_SEND",
        "run_id": RUN_ID,
        "invocation_id": value["invocation_id"],
        "endpoint": value["endpoint"],
        "model": value["model"],
        "token_budget": value["token_budget"],
        "system_prompt": request.system_prompt,
        "function_parameters": wire_payload["tools"][0]["function"]["parameters"],
        "prompt_field_manifest": value["prompt_allowed_field_manifest"],
        "validator_field_manifest": value["validator_expected_field_manifest"],
        "manifest_hashes": value["manifest_hashes"],
        "final_wire_payload": wire_payload,
        "redaction": {"api_key": "NOT_PERSISTED", "authorization_header": "NOT_PERSISTED", "secret_environment_values": "NOT_PERSISTED"},
        "fixture_and_upstream_references": value["source_artifacts"],
    })


def extracted_arguments(raw_response: Mapping[str, Any]) -> Mapping[str, Any] | None:
    calls = raw_response.get("tool_calls")
    if not isinstance(calls, list) or len(calls) != 1:
        return None
    function = calls[0].get("function") if isinstance(calls[0], Mapping) else None
    arguments = function.get("arguments") if isinstance(function, Mapping) else None
    if not isinstance(arguments, str):
        return None
    try:
        parsed = json.loads(arguments)
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, Mapping) else None


def write_success_reports(pre: Mapping[str, Any], executor: Any, result: Mapping[str, Any], output_path: Path) -> dict[str, Any]:
    record = executor.call_records[0]
    raw = executor.model_executor.response_for(pre["invocation_id"])
    if not isinstance(raw, Mapping):
        raise RuntimeError("raw response receipt unavailable after success")
    arguments = extracted_arguments(raw)
    exact_fields = isinstance(arguments, Mapping) and set(arguments) == set(pre["required_field_manifest"])
    json_object_string_status = {}
    if isinstance(arguments, Mapping) and isinstance(arguments.get("state_evidence"), Mapping):
        for field in JSON_OBJECT_STRING_STATE_FIELDS:
            value = arguments["state_evidence"].get(field)
            try:
                json_object_string_status[field] = value == "ABSENT" or (isinstance(value, str) and isinstance(json.loads(value), Mapping))
            except (TypeError, ValueError):
                json_object_string_status[field] = False
    else:
        json_object_string_status = {field: False for field in JSON_OBJECT_STRING_STATE_FIELDS}
    observability = {
        "http_status": raw.get("http_status"),
        "trace_headers": raw.get("trace_headers"),
        "provider_request_id": raw.get("provider_invocation_id"),
        "usage": raw.get("usage"),
        "finish_reason": raw.get("finish_reason"),
        "raw_response_artifact": record.get("raw_response_artifact"),
        "invocation_metadata_artifact": record.get("invocation_metadata_artifact"),
        "persistence_verification_artifact": record.get("persistence_verification_artifact"),
        "complete": isinstance(raw.get("http_status"), int) and isinstance(raw.get("trace_headers"), Mapping)
        and all(name in raw["trace_headers"] for name in DeepSeekProviderAdapter.trace_header_names),
    }
    if not observability["complete"]:
        raise RuntimeError("success-path observability is incomplete")
    if not (exact_fields and all(json_object_string_status.values())):
        raise RuntimeError("exact strict payload validation evidence is incomplete")
    display_matches = isinstance(arguments, Mapping) and result.get("content") == deterministic_display_projection(arguments)
    if not display_matches:
        raise RuntimeError("display projection is not deterministic from validated machine fields")
    envelope = e2e.make_envelope(e2e.role_spec("director"), result, "Character & Acting", "Direction constraints", output_path, run_id=RUN_ID)
    envelope_path = EVIDENCE / "envelopes" / "director_to_character_acting.json"
    write_json(envelope_path, envelope)
    reports = {
        "field_validation": {
            "result": "PASS", "function_name": FUNCTION_NAME, "exactly_15_fields": exact_fields,
            "additional_fields": [], "required_fields_present": exact_fields,
            "json_object_string_fields": json_object_string_status,
            "canonical_mode": arguments.get("selected_mode") if isinstance(arguments, Mapping) else None,
            "canonical_primary_state": arguments.get("primary_state_or_outcome") if isinstance(arguments, Mapping) else None,
            "executor_structured_transport": record.get("structured_transport"),
            "auto_repair": 0,
        },
        "observability": observability,
        "envelope": {
            "result": "PASS", "envelope_artifact": str(envelope_path), "deterministic_display_projection": display_matches,
            "display_projection_source": "validated Director machine fields", "carry_forward_locks": result.get("canon_assignment_locks"),
            "carry_forward_prohibited_changes": result.get("prohibited_changes"),
        },
    }
    write_json(EVIDENCE / "artifacts" / "director_exact_field_validation.json", reports["field_validation"])
    write_json(EVIDENCE / "artifacts" / "director_success_observability.json", reports["observability"])
    write_json(EVIDENCE / "artifacts" / "director_envelope_validation.json", reports["envelope"])
    return reports


def final_documents(pre: Mapping[str, Any], outcome: Mapping[str, Any], success: bool) -> None:
    docs = {
        "Director_Strict_Compatibility_Probe_04_Execution_Manifest_V0.1.md": ("Director Strict Compatibility Probe 04 Execution Manifest V0.1", public_preflight(pre)),
        "Director_Strict_Compatibility_Probe_04_Final_Wire_Evidence_V0.1.md": ("Director Strict Compatibility Probe 04 Final Wire Evidence V0.1", {
            "before_send_artifact": str(EVIDENCE / "artifacts" / "director_pre_send_contract_evidence.json"),
            "production_path_wire_artifact": outcome.get("call_record", {}).get("final_wire_payload_artifact"),
            "wire_payload_hash": pre["manifest_hashes"]["final_wire_payload"], "secrets": "NOT PERSISTED",
        }),
        "Director_Strict_Compatibility_Probe_04_Provider_Response_V0.1.md": ("Director Strict Compatibility Probe 04 Provider Response V0.1", {
            "result": outcome["result"], "call_record": outcome.get("call_record"), "raw_response_artifact": outcome.get("call_record", {}).get("raw_response_artifact"),
        }),
        "Director_Strict_Compatibility_Probe_04_Exact_Field_Validation_V0.1.md": ("Director Strict Compatibility Probe 04 Exact Field Validation V0.1", outcome.get("field_validation", {"result": "NOT REACHED"})),
        "Director_Strict_Compatibility_Probe_04_Observability_Report_V0.1.md": ("Director Strict Compatibility Probe 04 Observability Report V0.1", outcome.get("observability", {"result": "NOT REACHED"})),
        "Director_Strict_Compatibility_Probe_04_Envelope_Validation_V0.1.md": ("Director Strict Compatibility Probe 04 Envelope Validation V0.1", outcome.get("envelope", {"result": "NOT REACHED"})),
        "AI_Film_Studio_Director_Strict_Compatibility_Probe_04_Task_Record_V0.1.md": ("AI Film Studio Director Strict Compatibility Probe 04 Task Record V0.1", {
            "authorization": "ONE Director-only real strict compatibility probe after Repair 09F", "result": outcome["result"],
            "provider_calls": outcome["provider_calls"], "retries": 0, "fallbacks": 0, "other_role_calls": 0, "real_e2e_runs": 0,
        }),
        "AI_Film_Studio_Director_Strict_Compatibility_Probe_04_Work_Log_V0.1.md": ("AI Film Studio Director Strict Compatibility Probe 04 Work Log V0.1", {
            "steps": ["preflight and before-send evidence", "one production Director invocation", "raw-first persistence", "strict local validation", "deterministic envelope and display validation"],
            "result": outcome["result"], "no_repair_during_probe": True,
        }),
        "Director_Strict_Compatibility_Probe_04_Final_Review_V0.1.md": ("Director Strict Compatibility Probe 04 Final Review V0.1", {
            "result": outcome["result"],
            "recommendation": "DIRECTOR STRICT PROVIDER COMPATIBILITY CONFIRMED — READY TO RESTART R01" if success else outcome.get("recommendation", "DIRECTOR TARGETED REPAIR REQUIRED"),
            "automatic_next_run": "NOT EXECUTED; AWAITING USER REVIEW", "classification": outcome.get("classification"),
        }),
    }
    if not success:
        docs["Director_Strict_Compatibility_Probe_04_Failure_Attribution_V0.1.md"] = ("Director Strict Compatibility Probe 04 Failure Attribution V0.1", {
            "classification": outcome.get("classification"), "exception_type": outcome.get("exception_type"), "exception": outcome.get("exception"),
            "safe_stop": True, "retry": 0, "fallback": 0, "repair_during_probe": 0,
        })
    for filename, (title, values) in docs.items():
        write_markdown(ROOT / filename, title, values)


def main() -> int:
    if EVIDENCE.exists():
        raise RuntimeError(f"immutable Probe 04 evidence root already exists: {EVIDENCE}")
    try:
        pre = preflight()
    except Exception as exc:
        EVIDENCE.mkdir(parents=True)
        failed_pre = {"result": "FAIL", "run_id": RUN_ID, "classification": "PRE-SEND CONTRACT / INTEGRITY FAILURE", "exception_type": type(exc).__name__, "exception": str(exc), "provider_calls": 0, "retries": 0, "fallbacks": 0}
        write_json(EVIDENCE / "probe_manifest.json", failed_pre)
        final_documents(failed_pre, failed_pre, False)
        print(json.dumps(failed_pre, ensure_ascii=False, indent=2))
        return 1
    EVIDENCE.mkdir(parents=True)
    persist_before_send(pre)
    scene_writer = json.loads(source_artifacts()["scene_writer_output"].read_text(encoding="utf-8"))
    contract = build_deepseek_compatible_director_contract()
    executor = e2e.CanonicalRoleExecutor(evidence_dir=EVIDENCE, run_id=RUN_ID)
    try:
        result, input_path, output_path = executor.invoke(
            spec=e2e.role_spec("director"), input_payload=pre["director_input"],
            required_locks=scene_writer["canon_assignment_locks"], prohibited_changes=scene_writer["prohibited_changes"],
            structured_output=contract,
            structured_arguments_validator=e2e.make_director_payload_validator(
                selected_mode="PLAN", required_locks=scene_writer["canon_assignment_locks"], prohibited_changes=scene_writer["prohibited_changes"],
            ),
        )
        reports = write_success_reports(pre, executor, result, output_path)
        outcome = {"result": "PASS", "run_id": RUN_ID, "classification": "DIRECTOR STRICT PROVIDER COMPATIBILITY CONFIRMED", "provider_calls": 1, "retries": 0, "fallbacks": 0, "other_role_calls": 0, "real_e2e_runs": 0, "call_record": executor.call_records[0], "input_artifact": str(input_path), "output_artifact": str(output_path), **reports}
        write_json(EVIDENCE / "probe_manifest.json", outcome)
        final_documents(pre, outcome, True)
        print(json.dumps(outcome, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        record = executor.call_records[0] if executor.call_records else {}
        category = exc.category if isinstance(exc, e2e.E2EBlocked) else "OBSERVABILITY FAILURE" if "observability" in str(exc) else "LOCAL VALIDATOR FAILURE"
        recommendation = "DIRECTOR PROVIDER OBSERVABILITY REPAIR REQUIRED" if category == "OBSERVABILITY FAILURE" else "DIRECTOR TARGETED REPAIR REQUIRED"
        outcome = {"result": "FAIL", "run_id": RUN_ID, "classification": category, "recommendation": recommendation, "provider_calls": 1, "retries": 0, "fallbacks": 0, "other_role_calls": 0, "real_e2e_runs": 0, "exception_type": type(exc).__name__, "exception": str(exc), "call_record": record}
        write_json(EVIDENCE / "probe_manifest.json", outcome)
        final_documents(pre, outcome, False)
        print(json.dumps(outcome, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
