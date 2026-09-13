"""One authorized Director-only State Object Contract Probe 05 after Repair 09K.

The script compiles one per-run contract from frozen validated upstream records,
persists redacted pre-send evidence, invokes the production Director path once,
and never retries, falls back, repairs, or calls another role.
"""
from __future__ import annotations

import copy
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
FIXTURE_BINDING = RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1" / "fixtures" / "E2E_FIX_01_Runtime_Binding_V0.1.json"
SOURCE = HARNESS / "evidence" / "E2E-RUN-12"
os.environ["AFS_E2E_FIXTURE_BINDING"] = str(FIXTURE_BINDING)
if str(HARNESS) not in sys.path:
    sys.path.insert(0, str(HARNESS))

import run_minimal_e2e as e2e
from director_provider_compatibility import build_deepseek_compatible_director_contract, deepseek_compatible_schema
from director_state_object_contract import COMPILER_ID, compile_director_state_object_contract, lint_deepseek_strict_schema, stable_hash
from director_structured_submission import (
    FUNCTION_NAME,
    assert_director_contract_identity,
    director_prompt_contract_manifest,
    director_structured_contract_manifest,
    director_submission_schema,
    director_validator_contract_manifest,
    make_director_payload_validator,
)
from integration_contract.state_ledger import E2EStateLedger
from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter
from runtime.shared_qa.model_executor import ModelRequest


PROBE_ID = "DIRECTOR-STATE-OBJECT-CONTRACT-PROBE-05"
EVIDENCE = ROOT / "evidence" / PROBE_ID
INVOCATION_ID = f"{PROBE_ID}:director:1"
TYPED_ABSENT = {"type": "string", "enum": ["ABSENT"]}
EXACT_ABSENT_FIELDS = ("proposed_state", "knowledge_timing", "visual_state")
DYNAMIC_FIELDS = ("relevant_prior_state", "current_state")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_markdown(path: Path, title: str, sections: Mapping[str, Any]) -> None:
    lines = [f"# {title}", ""]
    for heading, value in sections.items():
        lines.extend((f"## {heading}", ""))
        if isinstance(value, (dict, list)):
            lines.extend(("```json", json.dumps(value, ensure_ascii=False, indent=2), "```", ""))
        else:
            lines.extend((str(value), ""))
    path.write_text("\n".join(lines), encoding="utf-8")


def source_paths() -> dict[str, Path]:
    return {
        "fixture_binding": FIXTURE_BINDING,
        "showrunner_output": SOURCE / "artifacts" / "showrunner_output.json",
        "scene_writer_output": SOURCE / "artifacts" / "scene_writer_output.json",
        "showrunner_envelope": SOURCE / "envelopes" / "01_showrunner_to_scene_writer.json",
        "scene_writer_envelope": SOURCE / "envelopes" / "02_scene_writer_to_director.json",
        "state_ledger": SOURCE / "state_ledger.json",
        "semantic_safeguard": SOURCE / "semantic_safeguard.json",
    }


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def rebuild_ledger(raw_ledger: Mapping[str, Any]) -> E2EStateLedger:
    if raw_ledger.get("append_only") is not True or not isinstance(raw_ledger.get("entries"), list):
        raise RuntimeError("frozen run-local Ledger is not append-only")
    ledger = E2EStateLedger(run_id=PROBE_ID)
    for expected_sequence, record in enumerate(raw_ledger["entries"], start=1):
        if record.get("sequence") != expected_sequence:
            raise RuntimeError("frozen Ledger sequence is not contiguous")
        ledger.append(envelope=record["envelope"], state_snapshot=record["state_snapshot"])
    return ledger


def build_request(director_input: Mapping[str, Any], strict_contract: Any) -> tuple[ModelRequest, dict[str, Any], str]:
    spec = e2e.role_spec("director")
    skill_path, skill_hash = e2e.canonical_skill(spec)
    request_payload = {
        "run_id": PROBE_ID,
        "role": spec.display_name,
        "canonical_binding": {"identity": spec.identity, "canonical_path": str(skill_path), "sha256": skill_hash},
        "selected_mode": spec.selected_mode,
        "output_language": e2e.OUTPUT_LANGUAGE,
        "input": copy.deepcopy(dict(director_input)),
    }
    request = ModelRequest(
        system_prompt=e2e.build_system_prompt(
            spec,
            skill_path.read_text(encoding="utf-8"),
            run_id=PROBE_ID,
            structured_function_name=strict_contract.function_name,
            structured_parameters_schema=strict_contract.parameters_schema,
        ),
        user_prompt=json.dumps(request_payload, ensure_ascii=False, separators=(",", ":")),
        model=e2e.MODEL,
        thinking_mode=e2e.THINKING_MODE,
        max_tokens=e2e.role_completion_budget(spec.key),
        response_format=None,
        structured_output=strict_contract,
    )
    wire, endpoint = DeepSeekProviderAdapter.build_provider_payload(request)
    return request, wire, endpoint


def preflight() -> dict[str, Any]:
    paths = source_paths()
    if not all(path.is_file() for path in paths.values()):
        raise RuntimeError("required frozen upstream artifact is missing")
    safeguard = load_json(paths["semantic_safeguard"])
    if safeguard.get("integration_decision") != "PASS":
        raise RuntimeError("frozen Scene Writer semantic safeguard is not PASS")
    compiled = e2e.compiled_run_contract()
    showrunner = load_json(paths["showrunner_output"])
    scene_writer = load_json(paths["scene_writer_output"])
    showrunner_envelope = load_json(paths["showrunner_envelope"])
    scene_writer_envelope = load_json(paths["scene_writer_envelope"])
    ledger = rebuild_ledger(load_json(paths["state_ledger"]))
    source_records = e2e.director_state_source_records(scene_writer["scene_packages"], ledger)
    state_contract = compile_director_state_object_contract(
        compiled_run_contract=compiled,
        validated_upstream_state_records=(),
        run_local_state_ledger_records=source_records,
        required_locks=scene_writer["canon_assignment_locks"],
        transition_authority_records=compiled["fixture"]["authorized_transitions"],
    )
    strict_contract = build_deepseek_compatible_director_contract(state_contract)
    neutral_schema = director_submission_schema(state_contract)
    strict_schema = deepseek_compatible_schema(state_contract)
    lint = lint_deepseek_strict_schema(strict_schema)
    prompt_manifest = director_prompt_contract_manifest(strict_schema, state_contract)
    function_manifest = director_structured_contract_manifest(strict_schema, state_contract)
    validator_manifest = director_validator_contract_manifest(state_contract)
    identity = assert_director_contract_identity(prompt_manifest, function_manifest, validator_manifest)
    if len(strict_schema["required"]) != 15 or set(strict_schema["required"]) != set(strict_schema["properties"]):
        raise RuntimeError("Director outer contract is not exact 15 fields")
    strict_state = strict_schema["properties"]["state_evidence"]["properties"]
    if any(strict_state[field] != TYPED_ABSENT for field in EXACT_ABSENT_FIELDS):
        raise RuntimeError("three exact ABSENT fields are not typed enums")
    for field in DYNAMIC_FIELDS:
        node = strict_state[field]
        if node.get("type") != "object" or node.get("additionalProperties") is not False or set(node.get("required", [])) != set(node.get("properties", {})):
            raise RuntimeError(f"dynamic state schema is not closed: {field}")
    director_input = e2e.downstream_input(
        upstream_artifacts={"showrunner": showrunner, "scene_writer": scene_writer},
        envelopes={"showrunner": showrunner_envelope, "scene_writer": scene_writer_envelope},
        ledger=ledger,
        role_constraints={"mode": "PLAN", "no_story_rewrite": True, "probe_id": PROBE_ID},
        director_state_contract=state_contract,
    )
    request, wire, endpoint = build_request(director_input, strict_contract)
    if wire.get("tools", [{}])[0].get("function", {}).get("name") != FUNCTION_NAME:
        raise RuntimeError("final tool function is not submit_director_package")
    if wire.get("tools", [{}])[0].get("function", {}).get("strict") is not True:
        raise RuntimeError("final tool schema is not strict:true")
    if wire.get("tool_choice", {}).get("function", {}).get("name") != FUNCTION_NAME:
        raise RuntimeError("final exact tool choice is missing")
    if "JSON-encoded state object" in request.system_prompt or "MUST be a JSON string" in request.system_prompt:
        raise RuntimeError("legacy string prompt path is reachable")
    hashes = e2e.canonical_skill_hashes()
    if hashes != e2e.EXPECTED_HASHES:
        raise RuntimeError("canonical Skill hash drift blocks Provider send")
    source_manifest = {name: {"path": str(path), "sha256": sha256_file(path), "read_only": True} for name, path in paths.items()}
    return {
        "result": "PASS",
        "probe_id": PROBE_ID,
        "timestamp": utc_now(),
        "invocation_id": INVOCATION_ID,
        "model": request.model,
        "endpoint": f"{endpoint}/chat/completions",
        "token_budget": request.max_tokens,
        "compiled_run_contract_id": compiled["fixture"]["fixture_id"],
        "compiled_run_contract": compiled,
        "state_schema_compiler_version": COMPILER_ID,
        "state_contract": state_contract,
        "five_compiled_field_schemas": copy.deepcopy(state_contract["state_schemas"]),
        "source_trace_manifest": copy.deepcopy(state_contract["source_trace"]),
        "source_records": source_records,
        "source_artifacts": source_manifest,
        "strict_contract": strict_contract,
        "neutral_schema": neutral_schema,
        "strict_schema": strict_schema,
        "request": request,
        "wire_payload": wire,
        "director_input": director_input,
        "ledger": ledger,
        "scene_writer": scene_writer,
        "identity": identity,
        "strict_lint": lint,
        "hash_chain": {
            "repair09j_authority": state_contract["authority"]["authority_bundle_hash"],
            "compiled_run_contract": state_contract["compiled_contract_hash"],
            "state_schema": state_contract["state_schema_hash"],
            "source_trace": state_contract["source_trace_hash"],
            "provider_neutral_contract": stable_hash(neutral_schema),
            "deepseek_projection": stable_hash(strict_schema),
            "final_function_parameters": stable_hash(wire["tools"][0]["function"]["parameters"]),
            "final_wire_payload": stable_hash(wire),
            "system_prompt": hashlib.sha256(request.system_prompt.encode("utf-8")).hexdigest(),
        },
        "canonical_skill_hashes": hashes,
        "legacy_string_path": "UNREACHABLE",
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "retries": 0,
        "fallbacks": 0,
    }


def public_preflight(pre: Mapping[str, Any]) -> dict[str, Any]:
    excluded = {"strict_contract", "request", "wire_payload", "director_input", "ledger", "scene_writer"}
    return {key: value for key, value in pre.items() if key not in excluded}


def persist_before_send(pre: Mapping[str, Any]) -> None:
    wire = copy.deepcopy(pre["wire_payload"])
    evidence = {
        "lifecycle_stage": "FINAL_PROVIDER_PAYLOAD_READY_PERSISTED_BEFORE_NETWORK_SEND",
        "probe_id": PROBE_ID,
        "invocation_id": pre["invocation_id"],
        "timestamp": pre["timestamp"],
        "endpoint": pre["endpoint"],
        "model": pre["model"],
        "token_budget": pre["token_budget"],
        "state_schema_compiler_version": pre["state_schema_compiler_version"],
        "compiled_run_contract_id": pre["compiled_run_contract_id"],
        "five_compiled_field_schemas": pre["five_compiled_field_schemas"],
        "source_trace_manifest": pre["source_trace_manifest"],
        "system_prompt": pre["request"].system_prompt,
        "function_parameters": wire["tools"][0]["function"]["parameters"],
        "hash_chain": pre["hash_chain"],
        "redacted_final_wire_payload": wire,
        "redaction": {"api_key": "NOT_PERSISTED", "authorization": "NOT_PERSISTED", "secret_environment_values": "NOT_PERSISTED"},
        "provider_calls_at_persistence": 0,
    }
    write_json(EVIDENCE / "preflight_manifest.json", public_preflight(pre))
    write_json(EVIDENCE / "artifacts" / "director_state_object_pre_send_evidence.json", evidence)


def extract_tool_arguments(raw: Mapping[str, Any]) -> tuple[str | None, Mapping[str, Any] | None]:
    calls = raw.get("tool_calls")
    if not isinstance(calls, list) or len(calls) != 1 or not isinstance(calls[0], Mapping):
        return None, None
    function = calls[0].get("function")
    if not isinstance(function, Mapping):
        return None, None
    name = function.get("name")
    arguments = function.get("arguments")
    if not isinstance(arguments, str):
        return name if isinstance(name, str) else None, None
    try:
        parsed = json.loads(arguments)
    except json.JSONDecodeError:
        return name if isinstance(name, str) else None, None
    return name if isinstance(name, str) else None, parsed if isinstance(parsed, Mapping) else None


def validate_success(pre: Mapping[str, Any], executor: Any, result: Mapping[str, Any], output_path: Path) -> dict[str, Any]:
    if len(executor.call_records) != 1:
        raise RuntimeError("Provider call count is not exactly one")
    call_record = executor.call_records[0]
    raw = executor.model_executor.response_for(INVOCATION_ID)
    if not isinstance(raw, Mapping):
        raise RuntimeError("raw-first response record is unavailable")
    function_name, arguments = extract_tool_arguments(raw)
    if function_name != FUNCTION_NAME:
        raise RuntimeError("PROVIDER / STRUCTURED TRANSPORT FAILURE: wrong function name")
    if not isinstance(arguments, Mapping):
        raise RuntimeError("PROVIDER / STRUCTURED TRANSPORT FAILURE: arguments are not exact JSON object")
    exact_fields = set(arguments) == set(pre["strict_schema"]["required"]) and len(arguments) == 15
    if not exact_fields:
        raise RuntimeError("ROLE STRUCTURAL FAILURE: outer field set is not exact 15")
    state = arguments.get("state_evidence")
    if not isinstance(state, Mapping):
        raise RuntimeError("STATE REPRESENTATION FAILURE: state_evidence is not an object")
    dynamic_objects = all(isinstance(state.get(field), Mapping) for field in DYNAMIC_FIELDS)
    exact_absent = all(state.get(field) == "ABSENT" for field in EXACT_ABSENT_FIELDS)
    source_values = all(state.get(field) == pre["state_contract"]["expected_state_values"][field] for field in (*DYNAMIC_FIELDS, *EXACT_ABSENT_FIELDS))
    if not dynamic_objects or not exact_absent or not source_values:
        raise RuntimeError("STATE REPRESENTATION FAILURE: five-field contract or source values diverged")
    trace_valid = stable_hash(pre["source_trace_manifest"]) == pre["state_contract"]["source_trace_hash"]
    if not trace_valid:
        raise RuntimeError("SOURCE TRACE FAILURE: source trace hash diverged")
    envelope = e2e.make_envelope(e2e.role_spec("director"), result, "Character & Acting", "Direction constraints", output_path, run_id=PROBE_ID)
    carriage = all(isinstance(envelope[field], Mapping) for field in DYNAMIC_FIELDS) and all(envelope[field] == "ABSENT" for field in EXACT_ABSENT_FIELDS)
    if not carriage:
        raise RuntimeError("DOWNSTREAM TRANSPORT FAILURE: object/ABSENT carriage diverged")
    envelope_path = EVIDENCE / "envelopes" / "director_to_character_acting.json"
    write_json(envelope_path, envelope)
    trace_headers = raw.get("trace_headers")
    observability = {
        "http_status": raw.get("http_status"),
        "provider_request_id": raw.get("provider_invocation_id"),
        "approved_trace_headers": trace_headers,
        "usage": raw.get("usage"),
        "finish_reason": raw.get("finish_reason"),
        "invocation_id": raw.get("invocation_id"),
        "raw_response_artifact": call_record.get("raw_response_artifact"),
        "invocation_metadata_artifact": call_record.get("invocation_metadata_artifact"),
        "persistence_verified": call_record.get("persistence_verified"),
        "raw_persisted_before_validation": bool(call_record.get("raw_response_artifact")) and call_record.get("persistence_verified") is True,
    }
    if raw.get("http_status") != 200 or not isinstance(trace_headers, Mapping) or not observability["raw_persisted_before_validation"]:
        raise RuntimeError("OBSERVABILITY FAILURE: raw-first HTTP/trace evidence is incomplete")
    reports = {
        "exact_field_validation": {"result": "PASS", "exact_function": True, "exactly_15_fields": True, "required_fields_present": True, "additional_fields": [], "outer_coercion": 0},
        "state_validation": {"result": "PASS", "dynamic_objects": {field: True for field in DYNAMIC_FIELDS}, "exact_absent": {field: True for field in EXACT_ABSENT_FIELDS}, "source_owned_values_exact": source_values, "source_trace_valid": trace_valid, "legacy_string_path": "UNREACHABLE", "auto_repair": 0},
        "downstream_carriage": {"result": "PASS", "envelope_artifact": str(envelope_path), "dynamic_objects_preserved": True, "exact_absent_preserved": True, "stringify_count": 0},
        "observability": {"result": "PASS", **observability},
    }
    for name, payload in reports.items():
        write_json(EVIDENCE / "artifacts" / f"director_{name}.json", payload)
    return {**reports, "call_record": call_record, "arguments": dict(arguments), "envelope": envelope}


def classify_failure(exc: Exception, provider_called: bool) -> str:
    text = str(exc)
    if not provider_called:
        if "source" in text.casefold() or "ledger" in text.casefold():
            return "STATE SOURCE AUTHORITY FAILURE"
        if "trace" in text.casefold():
            return "SOURCE TRACE FAILURE"
        if "schema" in text.casefold() or "contract" in text.casefold():
            return "STATE SCHEMA COMPILATION FAILURE"
        return "STRICT SCHEMA FAILURE"
    if isinstance(exc, e2e.E2EBlocked):
        category = exc.category
        if "PROVIDER" in category:
            return "PROVIDER FAILURE"
        if "SCHEMA" in category or "STRUCTURED" in category:
            return "STRICT SCHEMA FAILURE"
        if "STATE" in category:
            return "STATE REPRESENTATION FAILURE"
        if "HANDOFF" in category:
            return "DOWNSTREAM TRANSPORT FAILURE"
        if "ROLE" in category:
            return "ROLE STRUCTURAL FAILURE"
    for candidate in (
        "PROVIDER / STRUCTURED TRANSPORT FAILURE", "ROLE STRUCTURAL FAILURE", "STATE REPRESENTATION FAILURE",
        "SOURCE TRACE FAILURE", "DOWNSTREAM TRANSPORT FAILURE", "OBSERVABILITY FAILURE",
    ):
        if candidate in text:
            return "STRICT SCHEMA FAILURE" if candidate.startswith("PROVIDER / STRUCTURED") else candidate.split(":", 1)[0]
    return "LOCAL VALIDATOR FAILURE"


def write_documents(pre: Mapping[str, Any], outcome: Mapping[str, Any]) -> None:
    success = outcome.get("result") == "PASS"
    docs: dict[str, tuple[str, Mapping[str, Any]]] = {
        "Director_State_Object_Probe05_Execution_Manifest_V0.1.md": ("Director State Object Probe05 Execution Manifest V0.1", {"Probe": PROBE_ID, "Result": outcome.get("result"), "Execution": public_preflight(pre), "Call integrity": {"provider_calls": outcome.get("provider_calls"), "retries": 0, "fallbacks": 0, "other_role_calls": 0, "e2e_runs": 0}}),
        "Director_State_Object_Probe05_Compiled_Schema_V0.1.md": ("Director State Object Probe05 Compiled Schema V0.1", {"Compiler": pre.get("state_schema_compiler_version"), "Fixture": pre.get("compiled_run_contract_id"), "Five schemas": pre.get("five_compiled_field_schemas"), "Hash chain": pre.get("hash_chain")}),
        "Director_State_Object_Probe05_Source_Trace_V0.1.md": ("Director State Object Probe05 Source Trace V0.1", {"Result": "PASS" if pre.get("source_trace_manifest") else "NOT REACHED", "Source artifacts": pre.get("source_artifacts"), "Source trace": pre.get("source_trace_manifest")}),
        "Director_State_Object_Probe05_Final_Wire_Evidence_V0.1.md": ("Director State Object Probe05 Final Wire Evidence V0.1", {"Before-send artifact": str(EVIDENCE / "artifacts" / "director_state_object_pre_send_evidence.json"), "Production wire artifact": outcome.get("call_record", {}).get("final_wire_payload_artifact"), "Hash chain": pre.get("hash_chain"), "Secrets": "NOT PERSISTED"}),
        "Director_State_Object_Probe05_Provider_Response_V0.1.md": ("Director State Object Probe05 Provider Response V0.1", {"Result": outcome.get("result"), "Classification": outcome.get("classification"), "Call record": outcome.get("call_record", {}), "Raw response": outcome.get("call_record", {}).get("raw_response_artifact")}),
        "Director_State_Object_Probe05_Exact_Field_Validation_V0.1.md": ("Director State Object Probe05 Exact Field Validation V0.1", outcome.get("exact_field_validation", {"result": "NOT REACHED"})),
        "Director_State_Object_Probe05_State_Validation_V0.1.md": ("Director State Object Probe05 State Validation V0.1", outcome.get("state_validation", {"result": "NOT REACHED"})),
        "Director_State_Object_Probe05_Downstream_Carriage_V0.1.md": ("Director State Object Probe05 Downstream Carriage V0.1", outcome.get("downstream_carriage", {"result": "NOT REACHED"})),
        "Director_State_Object_Probe05_Observability_Report_V0.1.md": ("Director State Object Probe05 Observability Report V0.1", outcome.get("observability", {"result": "NOT REACHED"})),
        "Director_State_Object_Probe05_Final_Review_V0.1.md": ("Director State Object Probe05 Final Review V0.1", {"Result": outcome.get("result"), "Classification": outcome.get("classification"), "Recommendation": "DIRECTOR STATE OBJECT CONTRACT COMPATIBILITY CONFIRMED — READY TO RESTART R01" if success else outcome.get("recommendation"), "Automatic next run": "NOT EXECUTED; AWAITING USER REVIEW"}),
        "AI_Film_Studio_Director_State_Object_Probe05_Task_Record_V0.1.md": ("AI Film Studio Director State Object Probe05 Task Record V0.1", {"Authorization": "ONE Director-only real State Object Contract Probe05 after Repair09K", "Result": outcome.get("result"), "Provider calls": outcome.get("provider_calls"), "Other role calls": 0, "Retries": 0, "Fallbacks": 0, "Runtime repair": 0, "Provider contract repair": 0}),
        "AI_Film_Studio_Director_State_Object_Probe05_Work_Log_V0.1.md": ("AI Film Studio Director State Object Probe05 Work Log V0.1", {"Steps": ["09K provider-free prechecks", "frozen R12 upstream validation", "09K per-run schema compile", "pre-send evidence persistence", "one production Director invocation", "raw-first persistence", "local state/source-trace validation", "downstream Envelope carriage"], "Result": outcome.get("result"), "No repair during probe": True}),
    }
    if not success:
        docs["Director_State_Object_Probe05_Failure_Attribution_V0.1.md"] = ("Director State Object Probe05 Failure Attribution V0.1", {"Classification": outcome.get("classification"), "Exception type": outcome.get("exception_type"), "Exception": outcome.get("exception"), "Safe stop": True, "Retry": 0, "Fallback": 0, "Repair during probe": 0})
    for filename, (title, sections) in docs.items():
        write_markdown(ROOT / filename, title, sections)


def main() -> int:
    if EVIDENCE.exists():
        raise RuntimeError(f"immutable Probe05 evidence root already exists: {EVIDENCE}")
    try:
        pre = preflight()
    except Exception as exc:
        EVIDENCE.mkdir(parents=True, exist_ok=False)
        outcome = {"result": "FAIL", "classification": classify_failure(exc, False), "recommendation": "DIRECTOR STATE AUTHORITY REPAIR REQUIRED", "provider_calls": 0, "retries": 0, "fallbacks": 0, "exception_type": type(exc).__name__, "exception": str(exc), "safe_stop": True}
        write_json(EVIDENCE / "probe_manifest.json", outcome)
        write_documents({"result": "FAIL", "probe_id": PROBE_ID}, outcome)
        print(json.dumps(outcome, ensure_ascii=False, indent=2))
        return 1
    EVIDENCE.mkdir(parents=True, exist_ok=False)
    persist_before_send(pre)
    executor = e2e.CanonicalRoleExecutor(evidence_dir=EVIDENCE, run_id=PROBE_ID)
    try:
        result, input_path, output_path = executor.invoke(
            spec=e2e.role_spec("director"),
            input_payload=pre["director_input"],
            required_locks=pre["scene_writer"]["canon_assignment_locks"],
            prohibited_changes=pre["scene_writer"]["prohibited_changes"],
            structured_output=pre["strict_contract"],
            structured_arguments_validator=make_director_payload_validator(
                selected_mode="PLAN",
                required_locks=pre["scene_writer"]["canon_assignment_locks"],
                prohibited_changes=pre["scene_writer"]["prohibited_changes"],
                state_contract=pre["state_contract"],
            ),
            director_state_contract=pre["state_contract"],
        )
        reports = validate_success(pre, executor, result, output_path)
        outcome = {
            "result": "PASS",
            "probe_id": PROBE_ID,
            "classification": "DIRECTOR STATE OBJECT CONTRACT COMPATIBILITY CONFIRMED",
            "provider_calls": 1,
            "executor_calls": 1,
            "other_role_calls": 0,
            "e2e_runs": 0,
            "retries": 0,
            "fallbacks": 0,
            "input_artifact": str(input_path),
            "output_artifact": str(output_path),
            **{key: value for key, value in reports.items() if key not in {"arguments", "envelope"}},
        }
        write_json(EVIDENCE / "probe_manifest.json", outcome)
        write_documents(pre, outcome)
        print(json.dumps(outcome, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        provider_called = bool(executor.call_records) or executor.model_executor.response_for(INVOCATION_ID) is not None
        call_record = executor.call_records[0] if executor.call_records else {}
        classification = classify_failure(exc, provider_called)
        outcome = {
            "result": "FAIL",
            "probe_id": PROBE_ID,
            "classification": classification,
            "recommendation": "DIRECTOR STATE AUTHORITY REPAIR REQUIRED" if classification in {"STATE SOURCE AUTHORITY FAILURE", "SOURCE TRACE FAILURE"} else "DIRECTOR STATE OBJECT TARGETED REPAIR REQUIRED",
            "provider_calls": 1 if provider_called else 0,
            "executor_calls": 1 if provider_called else 0,
            "other_role_calls": 0,
            "e2e_runs": 0,
            "retries": 0,
            "fallbacks": 0,
            "exception_type": type(exc).__name__,
            "exception": str(exc),
            "call_record": call_record,
            "safe_stop": True,
        }
        write_json(EVIDENCE / "probe_manifest.json", outcome)
        write_documents(pre, outcome)
        print(json.dumps(outcome, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
