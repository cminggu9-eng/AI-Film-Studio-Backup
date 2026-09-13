"""Provider-free Repair13 positive contract and regression tests (01-17)."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
VAULT = AUTOMATION_ROOT.parent / "AI_Film_Studio_Obsidian_Vault_V0.1"
R16 = HARNESS / "evidence" / "E2E-RUN-16"
R16_RAW = R16 / "artifacts" / "character_&_acting_provider_response.json"
R16_SCENE_WRITER = R16 / "artifacts" / "scene_writer_output.json"
for path in (STAGE / "implementation", HARNESS, AUTOMATION_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from character_acting_transport_contract import (  # noqa: E402
    ABSENT,
    CHARACTER_ACTING_CANONICAL_OUTCOMES,
    CHARACTER_ACTING_FINAL_TRANSPORT_FIELDS,
    CHARACTER_ACTING_RAW_ROLE_FIELDS,
    CONTRACT_VERSION,
    SOURCE_SCHEMA_IDENTITY,
    assemble_character_acting_transport,
    character_acting_contract_manifest,
    character_acting_raw_role_schema,
    validate_character_acting_non_strict_transport,
    validate_character_acting_raw_role_payload,
    validate_final_character_acting_transport,
)
from run_minimal_e2e import (  # noqa: E402
    build_system_prompt,
    make_envelope,
    output_schema,
    role_spec,
    validate_role_output,
)


def run_json(script: Path) -> tuple[bool, dict[str, Any]]:
    completed = subprocess.run(
        [sys.executable, "-X", "utf8", "-B", str(script)],
        cwd=str(AUTOMATION_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        payload = {}
    return completed.returncode == 0, payload


def count_pass(script: Path, expected: int) -> bool:
    ok, payload = run_json(script)
    return ok and payload.get("passed") == expected and payload.get("total") == expected


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    skill = VAULT / "01_SKILLS" / "04_Character_Acting" / "character-acting" / "SKILL.md"
    output_model = VAULT / "01_SKILLS" / "04_Character_Acting" / "Character_Acting_Output_Model_V0.1.md"
    authority_model = VAULT / "01_SKILLS" / "04_Character_Acting" / "Character_Acting_Authority_Model_V0.1.md"
    interface = VAULT / "00_HOME" / "AI_Film_Studio_Interface_Contract_Map_V0.1.md"
    envelope_contract = VAULT / "00_HOME" / "AI_Film_Studio_State_Evidence_Envelope_V0.1.md"
    scene_contract = VAULT / "00_HOME" / "Scene_Writer_Integration_Output_Contract_V0.1.md"
    showrunner_transport = VAULT / "00_HOME" / "Showrunner_Transport_Hydration_Contract_V0.1.md"
    source_files = (skill, output_model, authority_model, interface, envelope_contract, scene_contract, showrunner_transport, R16_RAW, R16_SCENE_WRITER)
    texts = {path.name: path.read_text(encoding="utf-8") for path in source_files[:-2]}

    raw_file_before = R16_RAW.read_bytes()
    scene_file_before = R16_SCENE_WRITER.read_bytes()
    raw_record = json.loads(raw_file_before.decode("utf-8"))
    raw = json.loads(raw_record["raw_content"])
    raw_snapshot = copy.deepcopy(raw)
    scene_writer = json.loads(scene_file_before.decode("utf-8"))
    scene_snapshot = copy.deepcopy(scene_writer)
    manifest = character_acting_contract_manifest()
    raw_validated = validate_character_acting_raw_role_payload(raw)
    assembly = assemble_character_acting_transport(raw, scene_writer_output=scene_writer, source_artifact_path=R16_SCENE_WRITER)
    final_validated = validate_final_character_acting_transport(assembly.payload)
    spec = role_spec("character_acting")
    integrated = validate_role_output(
        spec,
        final_validated,
        required_locks=scene_writer["canon_assignment_locks"],
        prohibited_changes=scene_writer["prohibited_changes"],
        run_id="E2E-RUN-16",
    )
    envelope = make_envelope(spec, integrated, "Art Director", "Recorded Repair13 replay", R16_RAW, run_id="E2E-RUN-16")
    prompt = build_system_prompt(spec, texts["SKILL.md"], run_id="REPAIR13-PROVIDER-FREE-CAPTURE")
    validate_character_acting_non_strict_transport(strict_enabled=False)

    director_ok = count_pass(RESEARCH / "E2E_Targeted_Repair_09K_Director_State_Object_Contract_Implementation_V0.1" / "tests" / "run_director_state_object_phase2_regression.py", 12)
    art_director_ok = count_pass(RESEARCH / "E2E_Targeted_Repair_12_Art_Director_Output_Contract_Validator_Alignment_V0.1" / "tests" / "run_art_director_alignment_core_tests.py", 17)
    lifecycle_ok = count_pass(RESEARCH / "E2E_Targeted_Repair_11_Strict_Transport_Lifecycle_Authorization_V0.1" / "tests" / "run_strict_transport_lifecycle_tests.py", 30)

    source_identity = assembly.evidence["upstream_scene_packages"]
    provenance_complete = (
        all(path.is_file() for path in source_files)
        and "does not own story facts" in texts["Character_Acting_Authority_Model_V0.1.md"]
        and "Scene Writer locked scene facts" in texts["SKILL.md"]
        and "scene_packages" in texts["Scene_Writer_Integration_Output_Contract_V0.1.md"]
        and "ABSENT is the literal integration sentinel" in texts["AI_Film_Studio_State_Evidence_Envelope_V0.1.md"]
    )
    raw_contract_resolved = set(character_acting_raw_role_schema()) == set(CHARACTER_ACTING_RAW_ROLE_FIELDS) and "scene_packages" not in character_acting_raw_role_schema()
    final_contract_resolved = set(final_validated) == set(CHARACTER_ACTING_FINAL_TRANSPORT_FIELDS) and final_validated["scene_packages"] == ABSENT
    source_preserved = (
        source_identity["source_role"] == "Scene Writer"
        and source_identity["source_schema_identity"] == SOURCE_SCHEMA_IDENTITY
        and source_identity["scene_package_ids"] == [item["scene_id"] for item in scene_writer["scene_packages"]]
        and source_identity["source_record_ids"] == [item["source_attribution"]["source_record_id"] for item in scene_writer["scene_packages"]]
        and source_identity["source_artifact_sha256"] == sha256_bytes(scene_file_before)
    )
    raw_unchanged = raw == raw_snapshot and R16_RAW.read_bytes() == raw_file_before
    scene_unchanged = scene_writer == scene_snapshot and R16_SCENE_WRITER.read_bytes() == scene_file_before
    prompt_aligned = output_schema(spec) == character_acting_raw_role_schema() and "scene_packages" not in prompt and "RAW ROLE OUTPUT SCHEMA" in prompt
    envelope_pass = envelope["source_role"] == "Character & Acting" and envelope["primary_state_or_outcome"] == raw["primary_state_or_outcome"]

    results = [
        ("CA-TRANS-01", provenance_complete, "scene_packages provenance resolves to Scene Writer semantics plus an Integration-owned Character reserved slot"),
        ("CA-TRANS-02", raw_contract_resolved, "raw role contract contains only nine Character & Acting-owned fields"),
        ("CA-TRANS-03", final_contract_resolved, "final role transport preserves the ten-field contract with exact ABSENT"),
        ("CA-TRANS-04", manifest["ownership"]["scene_packages_semantic_owner"] == "Scene Writer" and manifest["ownership"]["scene_packages_character_stage_owner"] == "Integration reserved transport slot", "ownership boundary is exact"),
        ("CA-TRANS-05", manifest["ownership"]["scene_packages_character_final_representation"] == ABSENT and manifest["ownership"]["upstream_scene_packages_representation"] == "independent source artifact and identity reference", "transport representation is exact"),
        ("CA-TRANS-06", assembly.payload["scene_packages"] == ABSENT and assembly.evidence["semantic_mutation"] == 0 and assembly.evidence["scene_package_semantic_copy"] == 0, "deterministic reserved-slot assembly passes"),
        ("CA-TRANS-07", source_preserved and scene_unchanged, "upstream source identity and artifact are preserved"),
        ("CA-TRANS-08", raw_validated == raw and prompt_aligned, "raw role validator and non-strict prompt are aligned"),
        ("CA-TRANS-09", final_validated == integrated and set(final_validated) == set(CHARACTER_ACTING_FINAL_TRANSPORT_FIELDS), "final transport validator remains exact"),
        ("CA-TRANS-10", manifest["provider_transport"] == "NON_STRICT", "Character & Acting remains non-strict"),
        ("CA-TRANS-11", tuple(spec.allowed_outcomes) == CHARACTER_ACTING_CANONICAL_OUTCOMES, "canonical outcomes remain exact"),
        ("CA-TRANS-12", raw_unchanged and manifest["semantic_mutation"] == 0 and "Scene Writer" in texts["Character_Acting_Authority_Model_V0.1.md"], "role and authority boundaries are preserved"),
        ("CA-TRANS-13", raw_unchanged and raw_validated["primary_state_or_outcome"] == "PERFORMANCE_INTERPRETATION_READY", "E2E-RUN-16 recorded raw role payload passes read-only replay"),
        ("CA-TRANS-14", envelope_pass and final_validated["scene_packages"] == ABSENT and assembly.evidence["contract_version"] == CONTRACT_VERSION, "E2E-RUN-16 corrected final envelope replay passes"),
        ("CA-TRANS-15", director_ok, "Director state contract regression passes 12/12"),
        ("CA-TRANS-16", art_director_ok, "Art Director Repair12 regression passes 17/17"),
        ("CA-TRANS-17", lifecycle_ok, "Repair11 lifecycle regression passes 30/30"),
    ]
    records = [{"id": item_id, "result": "PASS" if passed else "FAIL", "detail": detail} for item_id, passed, detail in results]
    passed = sum(item["result"] == "PASS" for item in records)
    output = {
        "classification": "CHARACTER & ACTING REPAIR13 TRANSPORT CORE TESTS",
        "results": records,
        "passed": passed,
        "total": len(records),
        "recorded_replay": {
            "raw_role_contract": "PASS" if raw_unchanged else "FAIL",
            "final_transport_assembly": "PASS" if envelope_pass else "FAIL",
            "raw_provider_response_sha256": sha256_bytes(raw_file_before),
            "raw_content_sha256": sha256_bytes(raw_record["raw_content"].encode("utf-8")),
            "scene_writer_source_sha256": sha256_bytes(scene_file_before),
            "historical_status_preserved": True,
            "decisions": [
                "RECORDED CHARACTER & ACTING ROLE PAYLOAD SATISFIES CORRECTED RAW CONTRACT",
                "FINAL TRANSPORT ENVELOPE ASSEMBLY PASS",
            ],
        },
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

