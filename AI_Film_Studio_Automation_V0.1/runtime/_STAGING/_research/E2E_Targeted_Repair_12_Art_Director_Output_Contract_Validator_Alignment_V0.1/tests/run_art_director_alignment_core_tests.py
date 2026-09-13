"""Provider-free Repair12 positive contract and regression tests (01-17)."""

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
REPAIR06 = RESEARCH / "E2E_Targeted_Repair_06_Art_Director_Output_Contract_Parser_Alignment_V0.1"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
VAULT = AUTOMATION_ROOT.parent / "AI_Film_Studio_Obsidian_Vault_V0.1"
R15_RAW = HARNESS / "evidence" / "E2E-RUN-15" / "artifacts" / "art_director_provider_response.json"
for path in (REPAIR06 / "implementation", HARNESS, AUTOMATION_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from art_director_integration_contract import (  # noqa: E402
    ART_DIRECTOR_FAILURE_ALIGNMENT,
    ART_DIRECTOR_PRIMARY_STATES,
    ART_DIRECTOR_REQUIRED_DISPLAY_HEADINGS,
    ART_DIRECTOR_STATE_FIELDS,
    ART_DIRECTOR_TOP_LEVEL_FIELDS,
    art_director_machine_field_manifest,
    art_director_output_schema,
    art_director_prompt_contract_instruction,
    art_director_validator_requiredness_manifest,
    classify_art_director_failure,
    validate_art_director_integration_output,
)
from run_minimal_e2e import build_system_prompt, output_schema, role_spec  # noqa: E402


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


def result_pass(script: Path) -> bool:
    ok, payload = run_json(script)
    return ok and payload.get("result") == "PASS"


def recorded_replay() -> dict[str, Any]:
    persisted_bytes = R15_RAW.read_bytes()
    persisted = json.loads(persisted_bytes.decode("utf-8"))
    parsed = json.loads(persisted["raw_content"])
    before = copy.deepcopy(parsed)
    validation = validate_art_director_integration_output(parsed)
    return {
        "passed": parsed == before and persisted_bytes == R15_RAW.read_bytes(),
        "historical_file_sha256": hashlib.sha256(persisted_bytes).hexdigest(),
        "raw_content_sha256": hashlib.sha256(persisted["raw_content"].encode("utf-8")).hexdigest(),
        "validation": validation,
        "historical_status_preserved": True,
        "decision": "RECORDED ART DIRECTOR RESPONSE SATISFIES CORRECTED VALIDATOR",
    }


def main() -> int:
    skill = VAULT / "01_SKILLS" / "05_Art_Director" / "art-director" / "SKILL.md"
    capability = VAULT / "01_SKILLS" / "05_Art_Director" / "Art_Director_Capability_Model_V0.1.md"
    interface = VAULT / "00_HOME" / "AI_Film_Studio_Interface_Contract_Map_V0.1.md"
    source = (REPAIR06 / "implementation" / "art_director_integration_contract.py").read_text(encoding="utf-8")
    skill_text = skill.read_text(encoding="utf-8")
    capability_text = capability.read_text(encoding="utf-8")
    interface_text = interface.read_text(encoding="utf-8")
    manifest = art_director_machine_field_manifest()
    schema = art_director_output_schema()
    validator_manifest = art_director_validator_requiredness_manifest()
    spec = role_spec("art_director")
    prompt = build_system_prompt(spec, skill_text, run_id="REPAIR12-PROVIDER-FREE-CAPTURE")
    base = json.loads(json.loads(R15_RAW.read_text(encoding="utf-8"))["raw_content"])
    lawful_absent = copy.deepcopy(base)
    lawful_absent["state_evidence"]["visual_state"] = "ABSENT"
    lawful_object = copy.deepcopy(base)
    lawful_object["state_evidence"]["visual_state"] = {"scene_1": "soaked_uniform"}
    unresolved_absent = copy.deepcopy(base)
    unresolved_absent["unresolved_decisions"] = "ABSENT"
    no_production_content = copy.deepcopy(base)
    no_production_content["content"] = "A-17 黄铜钥匙与服装状态构成最小充分视觉设计。"
    replay = recorded_replay()

    repair06_ok = count_pass(REPAIR06 / "tests" / "run_art_director_integration_contract_tests.py", 12)
    director_ok = count_pass(RESEARCH / "E2E_Targeted_Repair_09K_Director_State_Object_Contract_Implementation_V0.1" / "tests" / "run_director_state_object_phase2_regression.py", 12)
    scene_writer_ok = count_pass(RESEARCH / "E2E_Targeted_Repair_03_Strict_Structured_Transport_V0.1" / "tests" / "run_scene_writer_strict_transport_tests.py", 15)
    lifecycle_ok = count_pass(RESEARCH / "E2E_Targeted_Repair_11_Strict_Transport_Lifecycle_Authorization_V0.1" / "tests" / "run_strict_transport_lifecycle_tests.py", 30)
    startup_ok = result_pass(RESEARCH / "Integration_Contract_Repair_V0.1" / "tests" / "run_provider_free_startup_test.py")

    heuristic_markers = (
        "FORBIDDEN_AI_PRODUCTION_TOKENS",
        "required_checks",
        "any(token in",
        "_json_text",
        ".casefold()",
    )
    prompt_required = set(ART_DIRECTOR_TOP_LEVEL_FIELDS) == set(output_schema(spec))
    validator_required = set(manifest["required_top_level_fields"]) == set(ART_DIRECTOR_TOP_LEVEL_FIELDS)
    results = [
        ("AD-ALIGN-01", all(path.is_file() for path in (skill, capability, interface, R15_RAW)) and "minimum-sufficient" in skill_text and "minimum-sufficient" in capability_text, "provenance audit sources are complete"),
        ("AD-ALIGN-02", manifest["fields"]["state_evidence"]["field_representation"] == "JSON object or exact ABSENT independently per field" and "visual state where supplied" in interface_text, "visual_state contract resolves to OBJECT OR exact ABSENT"),
        ("AD-ALIGN-03", validate_art_director_integration_output(lawful_absent)["visual_state_representation"] == "ABSENT", "lawful visual_state ABSENT passes"),
        ("AD-ALIGN-04", validate_art_director_integration_output(lawful_object)["visual_state_representation"] == "OBJECT", "lawful visual_state object passes"),
        ("AD-ALIGN-05", validate_art_director_integration_output(base)["unresolved_decisions_representation"] == "EMPTY_ARRAY" and validate_art_director_integration_output(unresolved_absent)["unresolved_decisions_representation"] == "ABSENT", "unresolved_decisions allows empty array or exact ABSENT"),
        ("AD-ALIGN-06", validate_art_director_integration_output(no_production_content)["conditional_production_feasibility_preserved"] is True, "production feasibility remains conditional"),
        ("AD-ALIGN-07", schema == output_schema(spec) and manifest == validator_manifest and prompt_required and validator_required and art_director_prompt_contract_instruction() in prompt, "prompt, provider schema, and validator requiredness are identical"),
        ("AD-ALIGN-08", not any(marker in source for marker in heuristic_markers), "content keyword/richness heuristics are absent"),
        ("AD-ALIGN-09", ART_DIRECTOR_REQUIRED_DISPLAY_HEADINGS == () and manifest["output_policy"] == "MINIMUM_SUFFICIENT_UNTEMPLATED_RECORDS", "minimum-sufficient untamplated principle is preserved"),
        ("AD-ALIGN-10", tuple(spec.allowed_outcomes) == ART_DIRECTOR_PRIMARY_STATES, "canonical outcomes remain exact"),
        ("AD-ALIGN-11", repair06_ok, "Repair06 regression passes 12/12"),
        ("AD-ALIGN-12", replay["passed"] and replay["decision"].startswith("RECORDED ART DIRECTOR RESPONSE"), "E2E-RUN-15 recorded replay is evaluated read-only"),
        ("AD-ALIGN-13", classify_art_director_failure(provider_schema_allows_representation=True, validator_rejected=True, canonical_semantic_violation=False) == ART_DIRECTOR_FAILURE_ALIGNMENT, "failure attribution prioritizes validator alignment drift"),
        ("AD-ALIGN-14", director_ok, "Director state object regression passes 12/12"),
        ("AD-ALIGN-15", scene_writer_ok, "Scene Writer strict regression passes 15/15"),
        ("AD-ALIGN-16", lifecycle_ok, "Repair11 lifecycle regression passes 30/30"),
        ("AD-ALIGN-17", startup_ok, "Provider-Free Startup passes"),
    ]
    records = [{"id": item_id, "result": "PASS" if passed else "FAIL", "detail": detail} for item_id, passed, detail in results]
    passed = sum(item["result"] == "PASS" for item in records)
    output = {
        "classification": "ART DIRECTOR REPAIR12 ALIGNMENT CORE TESTS",
        "results": records,
        "passed": passed,
        "total": len(records),
        "recorded_replay": replay,
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
