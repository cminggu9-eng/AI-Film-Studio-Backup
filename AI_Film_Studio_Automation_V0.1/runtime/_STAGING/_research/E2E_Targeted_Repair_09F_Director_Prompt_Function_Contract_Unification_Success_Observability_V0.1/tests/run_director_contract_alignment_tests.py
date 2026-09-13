"""Provider-free Repair 09F prompt/function/validator alignment tests."""
from __future__ import annotations

import copy
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any, Mapping


HERE = Path(__file__).resolve().parent
RUNTIME = next(parent for parent in HERE.parents if parent.name == "runtime")
RESEARCH = RUNTIME / "_STAGING" / "_research"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
for directory in (
    RUNTIME.parent,
    HARNESS,
    RESEARCH / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1" / "implementation",
    RESEARCH / "E2E_Targeted_Repair_05_Director_Output_Contract_Transport_Alignment_V0.1" / "implementation",
    RESEARCH / "E2E_Targeted_Repair_09B_Director_Full_Structured_Submission_Payload_V0.1" / "implementation",
    RESEARCH / "E2E_Targeted_Repair_09C_Director_Strict_Provider_Compatibility_V0.1" / "implementation",
):
    sys.path.insert(0, str(directory))

import run_minimal_e2e as e2e
from director_provider_compatibility import build_deepseek_compatible_director_contract, deepseek_compatible_schema
from director_structured_submission import JSON_OBJECT_STRING_STATE_FIELDS, SEMANTIC_FIELD_IDS, STATE_DIMENSIONS, director_structured_contract_manifest, make_director_payload_validator
from provider_response_persistence import persist_provider_response
from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter
from runtime.shared_qa.model_executor import ModelExecutor, ModelRequest, ModelResponse


def stable_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def valid_payload() -> dict[str, Any]:
    payload = {field: f"content for {field}" for field in SEMANTIC_FIELD_IDS}
    payload.update({
        "selected_mode": "PLAN", "primary_state_or_outcome": "DIRECTION_PLAN_PRODUCED", "flags": "ABSENT", "handoffs": "ABSENT",
        "required_outcome": "ABSENT", "unresolved_decisions": "ABSENT",
        "state_evidence": {field: json.dumps({"field": field}, ensure_ascii=False, separators=(",", ":")) for field in JSON_OBJECT_STRING_STATE_FIELDS},
    })
    payload["state_evidence"]["relationship_state"] = "疏远、互有猜疑，未和解"
    return payload


def reject(validator: Any, payload: Mapping[str, Any]) -> bool:
    try:
        validator(payload)
    except Exception:
        return True
    return False


def prompt_fields(prompt: str) -> list[str]:
    match = re.search(r"Emit exactly these 15 required fields and no others: (\[[^\]]+\])", prompt)
    if match is None:
        raise ValueError("derived Director prompt field manifest unavailable")
    return json.loads(match.group(1))


class MockSuccessProvider:
    provider = "deepseek"
    model = "deepseek-v4-pro"
    thinking_mode = "disabled"

    def __init__(self, response: ModelResponse) -> None:
        self.response = response

    def complete(self, _: ModelRequest) -> ModelResponse:
        return self.response


def persist_mock_success(response: ModelResponse) -> dict[str, Any]:
    request = ModelRequest(system_prompt="mock", user_prompt="mock", model="deepseek-v4-pro", thinking_mode="disabled", max_tokens=3500, response_format=None, structured_output=build_deepseek_compatible_director_contract())
    executor = ModelExecutor(MockSuccessProvider(response))
    receipt = executor.execute_with_receipt(request, invocation_id="DIR-ALIGN-MOCK-01", fixture_id="E2E-FIX-01")
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        persisted = persist_provider_response(evidence_dir=root, role="Director", invocation_id="DIR-ALIGN-MOCK-01", timestamp="STATIC", raw_response=executor.response_for("DIR-ALIGN-MOCK-01"), usage_record=executor.usage_for("DIR-ALIGN-MOCK-01"), input_artifact="STATIC")
        raw = json.loads(Path(persisted["raw_response_artifact"]).read_text(encoding="utf-8"))
        metadata = json.loads(Path(persisted["invocation_metadata_artifact"]).read_text(encoding="utf-8"))
    return {"receipt": receipt, "raw": raw, "metadata": metadata}


def expect(identifier: str, condition: bool, results: list[dict[str, str]], detail: str) -> None:
    results.append({"id": identifier, "result": "PASS" if condition else "FAIL", "detail": detail})


def main() -> int:
    results: list[dict[str, str]] = []
    strict = build_deepseek_compatible_director_contract()
    neutral_manifest = director_structured_contract_manifest()
    function_manifest = director_structured_contract_manifest(strict.parameters_schema)
    validator_manifest = director_structured_contract_manifest()
    skill_path, _ = e2e.canonical_skill(e2e.role_spec("director"))
    prompt = e2e.build_system_prompt(e2e.role_spec("director"), skill_path.read_text(encoding="utf-8"), run_id="DIR-ALIGN-CAPTURE", structured_function_name=strict.function_name, structured_parameters_schema=strict.parameters_schema)
    prompt_manifest = {**function_manifest, "allowed_fields": prompt_fields(prompt), "required_fields": prompt_fields(prompt)}
    request = ModelRequest(system_prompt=prompt, user_prompt="{}", model="deepseek-v4-pro", thinking_mode="disabled", max_tokens=3500, response_format=None, structured_output=strict)
    final_payload, endpoint = DeepSeekProviderAdapter.build_provider_payload(request)
    validator = make_director_payload_validator(selected_mode="PLAN", required_locks=["lock-a"], prohibited_changes=["prohibition-a"])
    good = valid_payload()

    expect("DIR-ALIGN-01", "Director payload did not match exact required field set" in (RESEARCH / "E2E_Targeted_Repair_09E_Director_DeepSeek_Typed_Enum_Projection_V0.1" / "evidence" / "DIRECTOR-STRICT-COMPATIBILITY-PROBE-03" / "probe_manifest.json").read_text(encoding="utf-8"), results, "Probe 03 drift evidence read")
    expect("DIR-ALIGN-02", neutral_manifest["allowed_fields"] == function_manifest["allowed_fields"], results, "single machine source")
    expect("DIR-ALIGN-03", "REQUIRED TRANSPORT SCHEMA:" not in prompt, results, "legacy generic schema removed")
    expect("DIR-ALIGN-04", "DIRECTOR STRUCTURED FUNCTION CONTRACT (DERIVED FROM FINAL FUNCTION PARAMETERS)" in prompt, results, "prompt derived from final parameters")
    expect("DIR-ALIGN-05", len(prompt_manifest["allowed_fields"]) == 15, results, "exact prompt field count")
    expect("DIR-ALIGN-06", function_manifest["allowed_fields"] == list(strict.parameters_schema["properties"]), results, "function manifest exact")
    expect("DIR-ALIGN-07", validator_manifest["allowed_fields"] == neutral_manifest["allowed_fields"], results, "validator manifest exact")
    expect("DIR-ALIGN-08", stable_hash(prompt_manifest["allowed_fields"]) == stable_hash(function_manifest["allowed_fields"]) == stable_hash(validator_manifest["allowed_fields"]) and stable_hash(prompt_manifest["required_fields"]) == stable_hash(function_manifest["required_fields"]) == stable_hash(validator_manifest["required_fields"]), results, "three manifests identical")
    expect("DIR-ALIGN-09", tuple(function_manifest["json_object_string_fields"]) == JSON_OBJECT_STRING_STATE_FIELDS, results, "five object-string fields exact")
    expect("DIR-ALIGN-10", all(f"For {', '.join(JSON_OBJECT_STRING_STATE_FIELDS)}" in prompt and "MUST be a JSON string" in prompt for _ in (0,)), results, "serialization instructions")
    expect("DIR-ALIGN-11", validator(good)["canon_assignment_locks"] == ["lock-a"], results, "valid exact payload passes")
    expect("DIR-ALIGN-12", reject(validator, {**good, "scene_packages": "ABSENT"}), results, "additional fields fail closed")
    object_state = copy.deepcopy(good); object_state["state_evidence"][JSON_OBJECT_STRING_STATE_FIELDS[0]] = {"bad": "object"}
    expect("DIR-ALIGN-13", reject(validator, object_state), results, "object state representation fails")
    expect("DIR-ALIGN-14", final_payload["messages"][0]["content"] == prompt and endpoint.endswith("/beta"), results, "final live request capture")
    expect("DIR-ALIGN-15", set(deepseek_compatible_schema()["required"]) == set(function_manifest["required_fields"]), results, "function schema semantic fields unchanged")
    typed = deepseek_compatible_schema()["properties"]["flags"]
    expect("DIR-ALIGN-16", typed == {"type": "string", "enum": ["ABSENT"]}, results, "09E typed enum preserved")
    trace = {name: "ABSENT" for name in DeepSeekProviderAdapter.trace_header_names}; trace["x-ds-trace-id"] = "trace-01"
    response = ModelResponse(content="", provider="deepseek", model="deepseek-v4-pro", provider_invocation_id="mock-request-01", usage={"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}, latency_ms=1, thinking_mode="disabled", finish_reason="tool_calls", tool_calls=({"type": "function", "function": {"name": strict.function_name, "arguments": json.dumps(good, ensure_ascii=False)}},), raw_provider_response=json.dumps({"id": "mock-request-01", "choices": []}), http_status=200, trace_headers=trace)
    observed = persist_mock_success(response)
    expect("DIR-ALIGN-17", observed["raw"]["http_status"] == 200 and observed["metadata"]["http_status"] == 200 and observed["raw"]["trace_headers"] == trace and observed["metadata"]["trace_headers"] == trace, results, "success observability persists before validation")
    expect("DIR-ALIGN-18", "submit_director_package" == strict.function_name and final_payload["tool_choice"]["function"]["name"] == strict.function_name, results, "offline live-path contract ready")

    legacy_prompt = prompt + "REQUIRED TRANSPORT SCHEMA: {}"
    bad_prompt_manifest = dict(prompt_manifest); bad_prompt_manifest["allowed_fields"] = prompt_manifest["allowed_fields"][:-1]
    bad_validator_manifest = dict(validator_manifest); bad_validator_manifest["allowed_fields"] = validator_manifest["allowed_fields"][:-1]
    missing = copy.deepcopy(good); missing.pop("production_burden")
    token = copy.deepcopy(good); token["primary_state_or_outcome"] = "NOT_CANONICAL"
    malformed_state = copy.deepcopy(good); malformed_state["state_evidence"][JSON_OBJECT_STRING_STATE_FIELDS[1]] = "not-json"
    no_status = persist_mock_success(ModelResponse(content="", provider="deepseek", model="deepseek-v4-pro", provider_invocation_id="mock-request-02", usage={}, latency_ms=1, thinking_mode="disabled", raw_provider_response="{}", http_status=None, trace_headers=trace))
    no_trace = persist_mock_success(ModelResponse(content="", provider="deepseek", model="deepseek-v4-pro", provider_invocation_id="mock-request-03", usage={}, latency_ms=1, thinking_mode="disabled", raw_provider_response="{}", http_status=200, trace_headers=None))
    negatives = {
        "DIR-ALIGN-NEG-01": "REQUIRED TRANSPORT SCHEMA:" in legacy_prompt,
        "DIR-ALIGN-NEG-02": stable_hash(bad_prompt_manifest["allowed_fields"]) != stable_hash(function_manifest["allowed_fields"]),
        "DIR-ALIGN-NEG-03": stable_hash(bad_validator_manifest["allowed_fields"]) != stable_hash(function_manifest["allowed_fields"]),
        "DIR-ALIGN-NEG-04": reject(validator, {**good, "unexpected": "x"}),
        "DIR-ALIGN-NEG-05": reject(validator, {**good, "scene_packages": "ABSENT"}),
        "DIR-ALIGN-NEG-06": reject(validator, {**good, "canon_assignment_locks": []}),
        "DIR-ALIGN-NEG-07": reject(validator, {**good, "prohibited_changes": []}),
        "DIR-ALIGN-NEG-08": reject(validator, object_state),
        "DIR-ALIGN-NEG-09": reject(validator, malformed_state),
        "DIR-ALIGN-NEG-10": reject(validator, token),
        "DIR-ALIGN-NEG-11": no_status["raw"]["http_status"] is None,
        "DIR-ALIGN-NEG-12": no_trace["raw"]["trace_headers"] is None,
    }
    for identifier, passed in negatives.items():
        expect(identifier, passed, results, "negative mutation detected")
    passed = sum(item["result"] == "PASS" for item in results)
    print(json.dumps({"result": "PASS" if passed == len(results) else "FAIL", "passed": passed, "total": len(results), "provider_calls": 0, "executor_calls": 0, "role_calls": 0, "prompt_field_manifest_hash": stable_hash(prompt_manifest["allowed_fields"]), "function_field_manifest_hash": stable_hash(function_manifest["allowed_fields"]), "validator_field_manifest_hash": stable_hash(validator_manifest["allowed_fields"]), "required_field_manifest_hash": stable_hash(function_manifest["required_fields"]), "results": results}, ensure_ascii=False, indent=2))
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
