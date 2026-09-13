"""Provider-free Repair13 negative transport and ownership tests."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Callable


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
R16 = HARNESS / "evidence" / "E2E-RUN-16"
R16_RAW = R16 / "artifacts" / "character_&_acting_provider_response.json"
R16_SCENE_WRITER = R16 / "artifacts" / "scene_writer_output.json"
for path in (STAGE / "implementation", HARNESS, AUTOMATION_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from character_acting_transport_contract import (  # noqa: E402
    ABSENT,
    FAILURE_AUTHORITY,
    FAILURE_SLOT,
    CharacterActingTransportContractError,
    assemble_character_acting_transport,
    validate_character_acting_assembly_evidence,
    validate_character_acting_non_strict_transport,
    validate_character_acting_raw_role_payload,
    validate_final_character_acting_transport,
)


def rejected(action: Callable[[], Any], classification: str | None = None) -> bool:
    try:
        action()
    except CharacterActingTransportContractError as exc:
        return classification is None or exc.classification == classification
    return False


def main() -> int:
    record = json.loads(R16_RAW.read_text(encoding="utf-8"))
    raw = json.loads(record["raw_content"])
    scene_writer = json.loads(R16_SCENE_WRITER.read_text(encoding="utf-8"))
    assembly = assemble_character_acting_transport(raw, scene_writer_output=scene_writer, source_artifact_path=R16_SCENE_WRITER)

    invented = copy.deepcopy(raw)
    invented["scene_packages"] = copy.deepcopy(scene_writer["scene_packages"])
    prose_reconstruction = copy.deepcopy(raw)
    prose_reconstruction["content"] += " scene_packages are fully described here."
    mutated_source = copy.deepcopy(scene_writer)
    mutated_source["scene_packages"][0]["content"] += " unauthorized mutation"
    lost_identity = assembly.evidence_record()
    del lost_identity["upstream_scene_packages"]["source_record_ids"]
    bad_outcome = copy.deepcopy(raw)
    bad_outcome["primary_state_or_outcome"] = "PERFORMANCE_READY"
    missing_semantic = copy.deepcopy(raw)
    del missing_semantic["required_outcome"]
    missing_semantic["content"] += " required_outcome can be guessed from this prose."
    owns_absent = copy.deepcopy(raw)
    owns_absent["scene_packages"] = ABSENT

    classification_probe = False
    try:
        assemble_character_acting_transport(raw, scene_writer_output={}, source_artifact_path=R16_SCENE_WRITER)
    except CharacterActingTransportContractError as exc:
        classification_probe = exc.classification == FAILURE_SLOT and "ROLE SEMANTIC" not in exc.classification

    raw_stage_passes_without_final_slot = validate_character_acting_raw_role_payload(raw) == raw
    results = [
        ("CA-TRANS-NEG-01", rejected(lambda: validate_character_acting_raw_role_payload(invented), FAILURE_AUTHORITY), "Character & Acting cannot be forced to invent scene_packages"),
        ("CA-TRANS-NEG-02", rejected(lambda: assemble_character_acting_transport(prose_reconstruction, scene_writer_output={}, source_artifact_path=R16_SCENE_WRITER), FAILURE_SLOT), "model prose cannot reconstruct missing upstream scene_packages"),
        ("CA-TRANS-NEG-03", rejected(lambda: assemble_character_acting_transport(raw, scene_writer_output=mutated_source, source_artifact_path=R16_SCENE_WRITER), FAILURE_SLOT), "modified upstream packages are rejected"),
        ("CA-TRANS-NEG-04", rejected(lambda: assemble_character_acting_transport(raw, scene_writer_output={}, source_artifact_path=R16_SCENE_WRITER), FAILURE_SLOT), "missing required upstream source cannot become ABSENT"),
        ("CA-TRANS-NEG-05", raw_stage_passes_without_final_slot, "raw role validator does not apply the final-envelope-only slot"),
        ("CA-TRANS-NEG-06", rejected(lambda: validate_final_character_acting_transport(raw), FAILURE_SLOT), "final transport requirement cannot be deleted"),
        ("CA-TRANS-NEG-07", rejected(lambda: validate_character_acting_assembly_evidence(lost_identity), FAILURE_SLOT), "source identity loss is rejected"),
        ("CA-TRANS-NEG-08", rejected(lambda: validate_character_acting_raw_role_payload(bad_outcome)), "canonical Character outcome mutation is rejected"),
        ("CA-TRANS-NEG-09", rejected(lambda: validate_character_acting_non_strict_transport(strict_enabled=True), FAILURE_AUTHORITY), "unauthorized Character & Acting strict transport is rejected"),
        ("CA-TRANS-NEG-10", classification_probe, "integration transport failure is not classified role semantic"),
        ("CA-TRANS-NEG-11", rejected(lambda: assemble_character_acting_transport(missing_semantic, scene_writer_output=scene_writer, source_artifact_path=R16_SCENE_WRITER)), "silent semantic hydration from prose is rejected"),
        ("CA-TRANS-NEG-12", rejected(lambda: validate_character_acting_raw_role_payload(owns_absent), FAILURE_AUTHORITY), "scene_packages ownership cannot transfer to Character & Acting"),
    ]
    records = [{"id": item_id, "result": "PASS" if passed else "FAIL", "detail": detail} for item_id, passed, detail in results]
    passed = sum(item["result"] == "PASS" for item in records)
    output = {
        "classification": "CHARACTER & ACTING REPAIR13 TRANSPORT NEGATIVE TESTS",
        "results": records,
        "passed": passed,
        "total": len(records),
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "real_e2e_runs": 0,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if passed == len(records) else 1


if __name__ == "__main__":
    raise SystemExit(main())

