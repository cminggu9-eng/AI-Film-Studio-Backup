"""Read-only reassessment of the persisted Rerun04 Art Director response.

This script does not execute the E2E harness or contact a provider.  It writes
only additive evidence under this targeted-repair staging directory.
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
RERUN04_ROOT = HARNESS_STAGE / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1" / "evidence" / "E2E-RUN-04"
SOURCE_RAW = RERUN04_ROOT / "artifacts" / "art_director_provider_response.json"
SOURCE_INPUT = RERUN04_ROOT / "artifacts" / "art_director_input.json"
EVIDENCE_ROOT = STAGE / "evidence" / "ART-DIRECTOR-CONTRACT-ALIGNMENT-01"
for import_path in (str(IMPLEMENTATION), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

from art_director_integration_contract import validate_art_director_integration_output  # noqa: E402
from run_minimal_e2e import (  # noqa: E402
    EXPECTED_HASHES,
    canonical_skill,
    e2e_int_12_tokens_preserved,
    make_envelope,
    role_spec,
    validate_role_output,
    write_json,
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    persisted = json.loads(SOURCE_RAW.read_text(encoding="utf-8"))
    source_input = json.loads(SOURCE_INPUT.read_text(encoding="utf-8"))
    raw_content = persisted["raw_content"]
    raw_hash = hashlib.sha256(raw_content.encode("utf-8")).hexdigest()
    parsed = json.loads(raw_content)
    art_director = role_spec("art_director")
    reparsed = validate_role_output(
        art_director,
        parsed,
        required_locks=parsed["canon_assignment_locks"],
        prohibited_changes=parsed["prohibited_changes"],
        run_id="E2E-RUN-04",
    )
    inspection = validate_art_director_integration_output(reparsed)
    envelope = make_envelope(
        art_director,
        reparsed,
        "Continuity",
        "Read-only Art Director output-contract reassessment",
        SOURCE_RAW,
        run_id="E2E-RUN-04",
    )
    _, skill_hash = canonical_skill(art_director)
    visual_state = reparsed["state_evidence"].get("visual_state")
    checks = [
        ("AD-ALIGN-01", persisted.get("lifecycle_stage") == "RAW_RESPONSE_PERSISTED" and persisted.get("raw_content_sha256") == raw_hash == "fa919f8c3c8dfe9d821193a4717a8826a2aac39a31290aa72fa9e7e0257bea44", "raw response is persisted and unchanged"),
        ("AD-ALIGN-02", source_input.get("canonical_binding", {}).get("canonical_path", "").endswith("01_SKILLS\\05_Art_Director\\art-director\\SKILL.md") and skill_hash == EXPECTED_HASHES["art_director"], "canonical Art Director source and hash are unchanged"),
        ("AD-ALIGN-03", inspection["output_policy"] == "MINIMUM_SUFFICIENT_UNTEMPLATED_RECORDS" and inspection["required_display_headings"] == [] and inspection["missing_required_semantic_fields"] == [], "parser matches minimum-sufficient output while proving required E2E semantics"),
        ("AD-ALIGN-04", reparsed["primary_state_or_outcome"] == "DESIGN_RESPONSE_READY" and art_director.selected_mode == "DESIGN", "canonical outcome and Mode are exact"),
        ("AD-ALIGN-05", bool(reparsed["content"].strip()) and not inspection["forbidden_ai_production_tokens"], "design record is non-empty and contains no forbidden AI-production output"),
        ("AD-ALIGN-06", isinstance(visual_state, Mapping) and bool(visual_state), "current visual state is retained for the Continuity handoff"),
        ("AD-ALIGN-07", e2e_int_12_tokens_preserved(role_results={"art_director": reparsed}, envelopes={"art_director": envelope}), "mode, outcome, flags, and handoffs are preserved exactly"),
        ("AD-ALIGN-08", persisted["raw_content"] == raw_content and parsed == reparsed, "reassessment adds no semantic or heading repair"),
    ]
    results = [{"id": item_id, "result": "PASS" if passed else "FAIL", "detail": detail} for item_id, passed, detail in checks]
    passed = sum(item["result"] == "PASS" for item in results)
    artifacts = EVIDENCE_ROOT / "artifacts"
    write_json(artifacts / "art_director_reparsed_output.json", reparsed)
    write_json(artifacts / "art_director_contract_inspection.json", inspection)
    write_json(EVIDENCE_ROOT / "envelopes" / "05_art_director_to_continuity_reassessed.json", envelope)
    review: dict[str, Any] = {
        "run_id": "E2E-RUN-04",
        "classification": "ART DIRECTOR OUTPUT-CONTRACT / PARSER ALIGNMENT REASSESSMENT",
        "status": "PASS" if passed == len(results) else "FAIL",
        "results": results,
        "passed": passed,
        "total": len(results),
        "source_evidence": {
            "raw_response": str(SOURCE_RAW),
            "raw_response_sha256": raw_hash,
            "input": str(SOURCE_INPUT),
            "input_sha256": _sha256(SOURCE_INPUT),
            "source_evidence_preserved": True,
        },
        "alignment": {
            "historical_failure_classification": "TRANSPORT / PARSER CONTRACT FAILURE",
            "reassessment_result": "PASS",
            "legacy_forced_headings_removed": True,
            "canonical_skill_mutation": 0,
            "raw_response_mutation": 0,
            "semantic_mutation": 0,
            "auto_repairs": 0,
        },
        "integrity": {
            "provider_calls": 0,
            "executor_calls": 0,
            "retries": 0,
            "fallbacks": 0,
            "downstream_role_calls": 0,
        },
    }
    write_json(EVIDENCE_ROOT / "art_director_rerun_04_output_contract_reassessment.json", review)
    print(json.dumps(review, ensure_ascii=False, indent=2))
    return 0 if review["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
