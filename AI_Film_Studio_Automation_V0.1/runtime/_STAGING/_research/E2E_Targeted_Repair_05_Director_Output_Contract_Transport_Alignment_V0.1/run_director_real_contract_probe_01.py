"""One authorized, Director-only real contract probe for Repair 05.

It uses frozen successful Rerun03 upstream artifacts.  It intentionally makes
no Showrunner, Scene Writer, downstream-role, retry, or fallback call.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Mapping


STAGE = Path(__file__).resolve().parent
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
IMPLEMENTATION = STAGE / "implementation"
HARNESS_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
RERUN03_ROOT = HARNESS_STAGE / "evidence" / "E2E-RUN-03"
RERUN03_DIRECTOR_INPUT = RERUN03_ROOT / "artifacts" / "director_input.json"
RERUN03_SCENE_OUTPUT = RERUN03_ROOT / "artifacts" / "scene_writer_output.json"
EVIDENCE_ROOT = STAGE / "evidence" / "DIRECTOR-CONTRACT-PROBE-01"
RUN_ID = "DIRECTOR-CONTRACT-PROBE-01"
for import_path in (str(IMPLEMENTATION), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

from director_integration_contract import (  # noqa: E402
    DIRECTOR_CANONICAL_OUTPUT_HEADINGS,
    DIRECTOR_PRIMARY_STATES,
    inspect_director_semantic_fields,
)
from run_minimal_e2e import (  # noqa: E402
    ABSENT,
    CanonicalRoleExecutor,
    E2EBlocked,
    e2e_int_12_tokens_preserved,
    make_envelope,
    role_spec,
    write_json,
)


def _section_nonempty(content: str, heading: str) -> bool:
    positions = [(token, content.index(token)) for token in DIRECTOR_CANONICAL_OUTPUT_HEADINGS]
    positions.sort(key=lambda item: item[1])
    current = next(index for index, item in enumerate(positions) if item[0] == heading)
    start = positions[current][1] + len(heading)
    end = positions[current + 1][1] if current + 1 < len(positions) else len(content)
    return bool(content[start:end].strip())


def _write_manifest(payload: Mapping[str, Any]) -> None:
    write_json(EVIDENCE_ROOT / "probe_manifest.json", payload)


def main() -> int:
    if EVIDENCE_ROOT.exists():
        raise RuntimeError(f"Refusing to overwrite a one-shot probe evidence root: {EVIDENCE_ROOT}")
    frozen_input = json.loads(RERUN03_DIRECTOR_INPUT.read_text(encoding="utf-8"))
    input_payload = frozen_input["input"]
    scene_writer = input_payload["upstream_artifacts"]["scene_writer"]
    scene_output_sha256 = hashlib.sha256(RERUN03_SCENE_OUTPUT.read_bytes()).hexdigest()
    director = role_spec("director")
    _write_manifest({
        "run_id": RUN_ID,
        "classification": "DIRECTOR-ONLY REAL CONTRACT PROBE",
        "status": "STARTED",
        "authorization": "E2E Targeted Repair 05 optional one Director probe",
        "frozen_input": str(RERUN03_DIRECTOR_INPUT),
        "frozen_scene_writer_artifact": str(RERUN03_SCENE_OUTPUT),
        "frozen_scene_writer_artifact_sha256": scene_output_sha256,
        "provider_call_budget": 1,
        "provider_calls": 0,
        "showrunner_calls": 0,
        "scene_writer_calls": 0,
        "downstream_calls": 0,
        "retries": 0,
        "fallbacks": 0,
        "full_e2e_reruns": 0,
        "auto_repairs": 0,
    })
    executor = CanonicalRoleExecutor(evidence_dir=EVIDENCE_ROOT, run_id=RUN_ID)
    try:
        result, input_path, output_path = executor.invoke(
            spec=director,
            input_payload=input_payload,
            required_locks=scene_writer["canon_assignment_locks"],
            prohibited_changes=scene_writer["prohibited_changes"],
            completion_budget=3500,
        )
    except E2EBlocked as exc:
        _write_manifest({
            "run_id": RUN_ID,
            "classification": "DIRECTOR-ONLY REAL CONTRACT PROBE",
            "status": "BLOCKED",
            "failure_category": exc.category,
            "failure_detail": exc.detail,
            "provider_call_budget": 1,
            "provider_calls": len(executor.call_records),
            "calls": executor.call_records,
            "showrunner_calls": 0,
            "scene_writer_calls": 0,
            "downstream_calls": 0,
            "retries": 0,
            "fallbacks": 0,
            "full_e2e_reruns": 0,
            "auto_repairs": 0,
        })
        print(json.dumps({"status": "BLOCKED", "category": exc.category, "detail": exc.detail, "provider_calls": len(executor.call_records)}, ensure_ascii=False, indent=2))
        return 1

    content = result["content"]
    inspection = inspect_director_semantic_fields(content)
    envelope = make_envelope(
        director,
        result,
        "Character & Acting",
        "Director-only contract-probe handoff",
        output_path,
        run_id=RUN_ID,
    )
    raw_path = EVIDENCE_ROOT / "artifacts" / "director_provider_response.json"
    invocation_path = EVIDENCE_ROOT / "artifacts" / "director_invocation.json"
    persistence_path = EVIDENCE_ROOT / "artifacts" / "director_persistence_verification.json"
    raw_persisted = json.loads(raw_path.read_text(encoding="utf-8")) if raw_path.is_file() else {}
    invocation_persisted = json.loads(invocation_path.read_text(encoding="utf-8")) if invocation_path.is_file() else {}
    scene_texts = [scene["content"] for scene in scene_writer["scene_packages"]]
    acting_takeover_signals = ("演员必须", "演员应当", "采用斯坦尼", "使用情绪记忆", "微表情训练", "表演体系")
    checks = [
        ("DIR-PROBE-01", isinstance(content, str) and bool(content.strip()), "response complete"),
        ("DIR-PROBE-02", isinstance(result, Mapping) and result["scene_packages"] == ABSENT, "JSON transport parse PASS; no Scene Writer package emitted"),
        ("DIR-PROBE-03", envelope["canonical_mode"] == "PLAN", "canonical Mode exact"),
        ("DIR-PROBE-04", result["primary_state_or_outcome"] in DIRECTOR_PRIMARY_STATES, "canonical Primary State exact"),
        ("DIR-PROBE-05", _section_nonempty(content, "DIRECTORIAL INTENT"), "Directorial Intent present"),
        ("DIR-PROBE-06", _section_nonempty(content, "STAGING / BLOCKING"), "Staging / Blocking present"),
        ("DIR-PROBE-07", _section_nonempty(content, "SPATIAL GEOGRAPHY"), "Spatial Geography present"),
        ("DIR-PROBE-08", _section_nonempty(content, "AUDIENCE INFORMATION"), "Audience Information present"),
        ("DIR-PROBE-09", _section_nonempty(content, "CAMERA / COVERAGE INTENT"), "Camera / Coverage Intent present"),
        ("DIR-PROBE-10", _section_nonempty(content, "RHYTHM / TRANSITION INTENT"), "Rhythm / Transition Intent present"),
        ("DIR-PROBE-11", _section_nonempty(content, "PRODUCTION BURDEN") and _section_nonempty(content, "HANDOFFS / UNRESOLVED ISSUES"), "production burden and unresolved constraints represented"),
        ("DIR-PROBE-12", result["scene_packages"] == ABSENT and not any(scene_text in content for scene_text in scene_texts), "no upstream Scene package rewrite"),
        ("DIR-PROBE-13", result["canon_assignment_locks"] == scene_writer["canon_assignment_locks"] and result["prohibited_changes"] == scene_writer["prohibited_changes"], "Canon locks and prohibitions unchanged"),
        ("DIR-PROBE-14", not any(signal in content for signal in acting_takeover_signals), "no acting-method takeover signal"),
        ("DIR-PROBE-15", inspection.semantic_fields_present and inspection.canonical_order and e2e_int_12_tokens_preserved(role_results={"director": result}, envelopes={"director": envelope}), "State & Evidence handoff PASS"),
        ("DIR-PROBE-16", raw_path.is_file() and invocation_path.is_file() and persistence_path.is_file() and raw_persisted.get("lifecycle_stage") == "RAW_RESPONSE_PERSISTED" and bool(raw_persisted.get("raw_content")) and invocation_persisted.get("lifecycle_stage") == "USAGE_AND_INVOCATION_METADATA_PERSISTED" and bool(invocation_persisted.get("usage")), "raw response and usage persisted before local validation"),
    ]
    results = [{"id": item_id, "result": "PASS" if passed else "FAIL", "detail": detail} for item_id, passed, detail in checks]
    passed = sum(item["result"] == "PASS" for item in results)
    envelope_path = EVIDENCE_ROOT / "envelopes" / "01_director_to_character_acting.json"
    write_json(envelope_path, envelope)
    report = {
        "run_id": RUN_ID,
        "classification": "DIRECTOR-ONLY REAL CONTRACT PROBE",
        "status": "PASS" if passed == len(results) else "FAIL",
        "results": results,
        "passed": passed,
        "total": len(results),
        "input_artifact": str(input_path),
        "output_artifact": str(output_path),
        "envelope_artifact": str(envelope_path),
        "frozen_scene_writer_artifact": str(RERUN03_SCENE_OUTPUT),
        "frozen_scene_writer_artifact_sha256": scene_output_sha256,
        "provider_call_budget": 1,
        "provider_calls": len(executor.call_records),
        "calls": executor.call_records,
        "showrunner_calls": 0,
        "scene_writer_calls": 0,
        "downstream_calls": 0,
        "retries": 0,
        "fallbacks": 0,
        "full_e2e_reruns": 0,
        "semantic_mutation": 0,
        "auto_repairs": 0,
    }
    _write_manifest(report)
    write_json(EVIDENCE_ROOT / "director_real_contract_probe_01.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
