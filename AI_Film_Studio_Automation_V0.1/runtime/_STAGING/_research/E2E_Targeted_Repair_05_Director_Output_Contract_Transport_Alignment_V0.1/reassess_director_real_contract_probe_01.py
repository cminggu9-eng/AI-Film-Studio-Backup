"""Provider-free post-execution acceptance review for the one-shot Director probe."""

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
RERUN03_SCENE_OUTPUT = HARNESS_STAGE / "evidence" / "E2E-RUN-03" / "artifacts" / "scene_writer_output.json"
EVIDENCE_ROOT = STAGE / "evidence" / "DIRECTOR-CONTRACT-PROBE-01"
for import_path in (str(IMPLEMENTATION), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

from director_integration_contract import (  # noqa: E402
    DIRECTOR_CANONICAL_OUTPUT_HEADINGS,
    DIRECTOR_PRIMARY_STATES,
    inspect_director_semantic_fields,
)
from run_minimal_e2e import ABSENT, e2e_int_12_tokens_preserved, make_envelope, role_spec, write_json  # noqa: E402


def _section_nonempty(content: str, heading: str) -> bool:
    positions = [(token, content.index(token)) for token in DIRECTOR_CANONICAL_OUTPUT_HEADINGS]
    positions.sort(key=lambda item: item[1])
    index = next(position for position, item in enumerate(positions) if item[0] == heading)
    start = positions[index][1] + len(heading)
    end = positions[index + 1][1] if index + 1 < len(positions) else len(content)
    return bool(content[start:end].strip())


def main() -> int:
    artifacts = EVIDENCE_ROOT / "artifacts"
    initial = json.loads((EVIDENCE_ROOT / "director_real_contract_probe_01.json").read_text(encoding="utf-8"))
    result = json.loads((artifacts / "director_output.json").read_text(encoding="utf-8"))
    raw = json.loads((artifacts / "director_provider_response.json").read_text(encoding="utf-8"))
    invocation = json.loads((artifacts / "director_invocation.json").read_text(encoding="utf-8"))
    persistence = json.loads((artifacts / "director_persistence_verification.json").read_text(encoding="utf-8"))
    frozen_scene = json.loads(RERUN03_SCENE_OUTPUT.read_text(encoding="utf-8"))
    content = result["content"]
    director = role_spec("director")
    envelope = make_envelope(director, result, "Character & Acting", "Post-execution acceptance review", artifacts / "director_output.json", run_id="DIRECTOR-CONTRACT-PROBE-01")
    inspection = inspect_director_semantic_fields(content)
    exact_scene_texts = [scene["content"] for scene in frozen_scene["scene_packages"]]
    acting_method_takeover_signals = ("演员必须", "演员应当", "采用斯坦尼", "使用情绪记忆", "微表情训练", "表演体系")
    checks = [
        ("DIR-PROBE-01", bool(content.strip()), "response complete"),
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
        ("DIR-PROBE-12", result["scene_packages"] == ABSENT and not any(scene_text in content for scene_text in exact_scene_texts), "no upstream Scene package rewrite"),
        ("DIR-PROBE-13", result["canon_assignment_locks"] == frozen_scene["canon_assignment_locks"] and result["prohibited_changes"] == frozen_scene["prohibited_changes"], "Canon locks and prohibitions unchanged"),
        ("DIR-PROBE-14", not any(signal in content for signal in acting_method_takeover_signals), "no acting-method takeover; Character & Acting is lawfully named only as a future handoff owner"),
        ("DIR-PROBE-15", inspection.semantic_fields_present and inspection.canonical_order and e2e_int_12_tokens_preserved(role_results={"director": result}, envelopes={"director": envelope}), "State & Evidence handoff PASS"),
        ("DIR-PROBE-16", raw.get("lifecycle_stage") == "RAW_RESPONSE_PERSISTED" and bool(raw.get("raw_content")) and invocation.get("lifecycle_stage") == "USAGE_AND_INVOCATION_METADATA_PERSISTED" and bool(invocation.get("usage")) and persistence.get("verified") is True, "raw response and usage persisted before local validation"),
    ]
    results = [{"id": item_id, "result": "PASS" if passed else "FAIL", "detail": detail} for item_id, passed, detail in checks]
    passed = sum(item["result"] == "PASS" for item in results)
    review = {
        "run_id": "DIRECTOR-CONTRACT-PROBE-01",
        "classification": "DIRECTOR-ONLY REAL CONTRACT PROBE POST-EXECUTION ACCEPTANCE REVIEW",
        "status": "PASS" if passed == len(results) else "FAIL",
        "results": results,
        "passed": passed,
        "total": len(results),
        "original_probe_report": str(EVIDENCE_ROOT / "director_real_contract_probe_01.json"),
        "original_probe_report_preserved": True,
        "correction": {
            "type": "POST_EXECUTION_ASSERTION_CORRECTION",
            "provider_calls_added": 0,
            "original_raw_response_sha256": raw["raw_content_sha256"],
            "DIR-PROBE-14": "A future Character & Acting handoff is not Director acting-method takeover.",
            "DIR-PROBE-16": "Usage belongs to the separately persisted invocation-metadata artifact, not the raw-response artifact.",
        },
        "integrity": {
            "provider_calls": 0,
            "executor_calls": 0,
            "retries": 0,
            "fallbacks": 0,
            "showrunner_calls": 0,
            "scene_writer_calls": 0,
            "downstream_calls": 0,
            "semantic_mutation": 0,
            "auto_repairs": 0,
        },
        "frozen_scene_writer_artifact_sha256": hashlib.sha256(RERUN03_SCENE_OUTPUT.read_bytes()).hexdigest(),
    }
    write_json(EVIDENCE_ROOT / "director_real_contract_probe_01_post_execution_acceptance_review.json", review)
    print(json.dumps(review, ensure_ascii=False, indent=2))
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
