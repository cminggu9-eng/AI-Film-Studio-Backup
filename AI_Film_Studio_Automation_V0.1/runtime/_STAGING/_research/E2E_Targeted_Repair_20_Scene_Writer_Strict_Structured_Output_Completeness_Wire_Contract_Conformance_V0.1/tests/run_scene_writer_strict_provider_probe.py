"""One authorized, raw-first, Scene Writer-only strict completeness probe."""

from __future__ import annotations

import copy
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Mapping

from repair20_support import R25, current_wire_audit

import run_minimal_e2e as e2e
from provider_response_persistence import persist_provider_response, persist_validation_error
from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter
from runtime.shared_qa.model_executor import ModelExecutionError, ModelExecutor, ModelRequest, assess_response_truncation
from scene_writer_strict_transport import validate_strict_scene_writer_arguments


PROBE_ID = "SCENE-WRITER-STRICT-PROBE-20-F03"
PROBE_ROOT = Path(__file__).resolve().parents[1] / "reports" / PROBE_ID
ARTIFACTS = PROBE_ROOT / "artifacts"


def immutable_showrunner_input(compiled: Mapping[str, Any]) -> tuple[Dict[str, Any], Dict[str, Any]]:
    """Use only the R25 successful upstream output as read-only input data."""

    source = R25 / "artifacts" / "showrunner_output.json"
    showrunner = json.loads(source.read_text(encoding="utf-8"))
    envelope = e2e.make_envelope(
        e2e.role_spec("showrunner"),
        showrunner,
        "Scene Writer",
        "Frozen successful R25 upstream is probe input only; this is not an R25 retry.",
        source,
        run_id="E2E-RUN-25",
    )
    source = compiled["fixture"]
    fixture_constraints = {
        "scene_count": source["scene_count"],
        "output_language": e2e.OUTPUT_LANGUAGE,
        "characters": source["characters"],
        "relationship": source["relationship_constraints"],
        "prop": source["tracked_entities"][0],
        "knowledge": source["knowledge_events"],
        "visual_state": source["state_dimensions"],
        "prohibited": source["prohibited_outcomes"],
        "decision_locks": source["decision_locks"],
    }
    input_payload = e2e.downstream_input(
        upstream_artifacts={"showrunner": showrunner},
        envelopes={"showrunner": envelope},
        ledger=None,
        role_constraints={
            "mode": "CREATE",
            "scene_count": 3,
            "fixture_constraints": fixture_constraints,
            "strict_structured_transport": {
                "function": "submit_scene_writer_package",
                "response_format_route": "PROHIBITED",
                "no_auto_repair": True,
            },
        },
    )
    return showrunner, input_payload


def write_report(payload: Mapping[str, Any]) -> None:
    e2e.write_json(PROBE_ROOT / "Scene_Writer_Strict_Provider_Completeness_Probe_20.json", payload)
    print(json.dumps(dict(payload), ensure_ascii=False, indent=2))


def main() -> int:
    if PROBE_ROOT.exists():
        write_report({
            "classification": "SCENE WRITER STRICT PROVIDER COMPLETENESS PROBE",
            "probe_id": PROBE_ID,
            "overall": "BLOCKED",
            "detail": "probe evidence path already exists; a second provider probe is forbidden",
            "provider_calls": 0,
            "retry_count": 0,
        })
        return 1

    audit = current_wire_audit()
    compiled, strict = audit["compiled"], audit["strict"]
    schema, scene_ids, state = audit["schema"], audit["scene_ids"], audit["state"]
    showrunner, input_payload = immutable_showrunner_input(compiled)
    skill_path, skill_hash = e2e.canonical_skill(e2e.role_spec("scene_writer"))
    request_payload = {
        "run_id": PROBE_ID,
        "role": "Scene Writer",
        "canonical_binding": {
            "identity": e2e.role_spec("scene_writer").identity,
            "canonical_path": str(skill_path),
            "sha256": skill_hash,
        },
        "selected_mode": e2e.role_spec("scene_writer").selected_mode,
        "output_language": e2e.OUTPUT_LANGUAGE,
        "input": input_payload,
    }
    request = ModelRequest(
        system_prompt=audit["prompt"],
        user_prompt=json.dumps(request_payload, ensure_ascii=False, separators=(",", ":")),
        model=e2e.MODEL,
        thinking_mode=e2e.THINKING_MODE,
        max_tokens=5000,
        response_format=None,
        structured_output=strict,
    )
    wire_payload, endpoint = DeepSeekProviderAdapter.build_provider_payload(request)
    function = wire_payload["tools"][0]["function"]
    schema_identity = e2e.scene_writer_schema_identity_manifest(
        compiled_schema=schema,
        final_strict_schema=strict.parameters_schema,
        adapter_projected_schema=function["parameters"],
        wire_schema=function["parameters"],
        local_validator_schema=strict.parameters_schema,
        function_name=strict.function_name,
        wire_function_name=function["name"],
        wire_strict=function["strict"],
        wire_tool_choice=wire_payload["tool_choice"],
    )
    mechanics = schema_identity["wire_strict_mechanics"]
    equivalence = schema_identity["schema_byte_equivalence"]
    if not (mechanics["function_name_exact"] and mechanics["strict_true"] and mechanics["tool_choice_exact"] and equivalence["all_five_equal"]):
        write_report({
            "classification": "SCENE WRITER STRICT PROVIDER COMPLETENESS PROBE",
            "probe_id": PROBE_ID,
            "overall": "BLOCKED",
            "detail": "compiled-to-wire strict mechanics are not authorized for provider send",
            "schema_identity": schema_identity,
            "provider_calls": 0,
            "retry_count": 0,
        })
        return 1

    e2e.write_json(ARTIFACTS / "scene_writer_probe_input.json", request_payload)
    e2e.write_json(ARTIFACTS / "scene_writer_schema_identity_manifest.json", schema_identity)
    e2e.write_json(ARTIFACTS / "scene_writer_final_wire_payload.json", {
        "lifecycle_stage": "FINAL_WIRE_PAYLOAD_PERSISTED_BEFORE_SEND",
        "probe_id": PROBE_ID,
        "endpoint": f"{endpoint}/chat/completions",
        "payload": wire_payload,
        "wire_payload_sha256": e2e.sha256_text(e2e.stable_json(wire_payload)),
        "final_parameters_sha256": e2e.sha256_text(e2e.stable_json(function["parameters"])),
        "schema_identity_manifest_artifact": str((ARTIFACTS / "scene_writer_schema_identity_manifest.json").resolve()),
    })

    invocation_id = f"{PROBE_ID}:scene_writer:1"
    provider = DeepSeekProviderAdapter()
    executor = ModelExecutor(provider)
    started = e2e.utc_now()
    raw_response: Mapping[str, Any] | None = None
    usage: Mapping[str, Any] | None = None
    persistence: Mapping[str, Any] | None = None
    report: Dict[str, Any] = {
        "classification": "SCENE WRITER STRICT PROVIDER COMPLETENESS PROBE",
        "probe_id": PROBE_ID,
        "fixture_id": compiled["fixture"]["fixture_id"],
        "upstream_input_source": str((R25 / "artifacts" / "showrunner_output.json").resolve()),
        "upstream_input_mode": "IMMUTABLE_READ_ONLY_NOT_A_R25_RETRY",
        "strict_function_name": strict.function_name,
        "strict_true": function["strict"],
        "tool_choice": copy.deepcopy(wire_payload["tool_choice"]),
        "max_tokens": request.max_tokens,
        "schema_identity": schema_identity,
        "retry_count": 0,
        "provider_calls": 1,
        "executor_calls": 1,
        "role_calls": 1,
        "live_e2e_runs": 0,
        "r03_restarted": False,
    }
    try:
        receipt = executor.execute_with_receipt(
            request,
            invocation_id=invocation_id,
            fixture_id=compiled["fixture"]["fixture_id"],
        )
        raw_response = executor.response_for(invocation_id)
        usage = executor.usage_for(invocation_id)
        if not isinstance(raw_response, Mapping) or not isinstance(usage, Mapping):
            raise ModelExecutionError("raw provider response is unavailable before local validation")
        persistence = persist_provider_response(
            evidence_dir=PROBE_ROOT,
            role="Scene Writer",
            invocation_id=invocation_id,
            timestamp=started,
            raw_response=raw_response,
            usage_record=usage,
            input_artifact=str((ARTIFACTS / "scene_writer_probe_input.json").resolve()),
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
        e2e.write_json(ARTIFACTS / "scene_writer_truncation_detection.json", truncation)
        arguments = executor.extract_required_tool_arguments(receipt, function_name=strict.function_name)
        validated = validate_strict_scene_writer_arguments(
            arguments,
            parameters_schema=schema,
            scene_id_contract=scene_ids,
            state_field_contract=state,
        )
        required = schema["properties"]["scenes"]["items"]["required"]
        per_scene_complete = [
            {
                "scene_id": scene.get("id"),
                "all_required_present": all(field in scene for field in required),
                "structural_required_present": all(
                    field in scene["structural"]
                    for field in schema["properties"]["scenes"]["items"]["properties"]["structural"]["required"]
                ),
                "state_required_present": all(
                    field in scene["state"]
                    for field in schema["properties"]["scenes"]["items"]["properties"]["state"]["required"]
                ),
            }
            for scene in validated["scenes"]
        ]
        local_schema_pass = (
            [scene["id"] for scene in validated["scenes"]] == scene_ids["ordered_scene_ids"]
            and all(item["all_required_present"] and item["structural_required_present"] and item["state_required_present"] for item in per_scene_complete)
        )
        report.update({
            "raw_first_persistence": persistence,
            "truncation": truncation,
            "provider_finish_reason": raw_response.get("finish_reason"),
            "local_schema_pass": local_schema_pass,
            "repair16_exact_scene_ids_pass": [scene["id"] for scene in validated["scenes"]] == scene_ids["ordered_scene_ids"],
            "repair17_state_field_pass": all(state["transport_field_name"] in scene["state"] for scene in validated["scenes"]),
            "per_scene_completeness": per_scene_complete,
            "overall": "PASS" if local_schema_pass and not truncation["truncated"] else "FAIL",
        })
    except Exception as exc:
        raw_response = executor.response_for(invocation_id)
        usage = executor.usage_for(invocation_id)
        if isinstance(raw_response, Mapping) and isinstance(usage, Mapping):
            persistence = persist_provider_response(
                evidence_dir=PROBE_ROOT,
                role="Scene Writer",
                invocation_id=invocation_id,
                timestamp=started,
                raw_response=raw_response,
                usage_record=usage,
                input_artifact=str((ARTIFACTS / "scene_writer_probe_input.json").resolve()),
            )
            persist_validation_error(
                evidence_dir=PROBE_ROOT,
                role="Scene Writer",
                invocation_id=invocation_id,
                validation_stage="Strict Structured Completeness Probe",
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
