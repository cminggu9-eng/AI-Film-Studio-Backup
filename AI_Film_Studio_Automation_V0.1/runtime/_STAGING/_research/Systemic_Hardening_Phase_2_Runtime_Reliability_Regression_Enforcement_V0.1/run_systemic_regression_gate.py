"""Unified provider-free / recorded-response gate for Systemic Hardening Phase 2."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


PHASE = Path(__file__).resolve().parent
AUTOMATION_ROOT = next(parent for parent in PHASE.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
sys.path.insert(0, str(HARNESS))

from runtime_reliability_contract import validate_golden_recorded_evidence  # noqa: E402


def suite(name: str, tier: str, script: Path, expected: int, invariant: str, lineage: str) -> dict[str, str | int | Path]:
    return {"suite": name, "tier": tier, "script": script, "expected": expected, "invariant": invariant, "lineage": lineage}


SUITES = (
    suite("STATE", "TIER 1", RESEARCH / "Integration_Contract_Repair_V0.1" / "tests" / "run_state_contract_tests.py", 12, "CONTINUITY DOES NOT REPAIR", "H / J"),
    suite("SEM", "TIER 1", RESEARCH / "Integration_Contract_Repair_V0.1" / "tests" / "run_semantic_safeguard_tests.py", 12, "NO SILENT REPAIR", "J"),
    suite("Provider-Free Startup", "TIER 1", RESEARCH / "Integration_Contract_Repair_V0.1" / "tests" / "run_provider_free_startup_test.py", 0, "NO AUTOMATIC PROVIDER FALLBACK", "A / I"),
    suite("Minimal Harness Startup", "TIER 1", HARNESS / "tests" / "test_minimal_e2e_harness_startup.py", 0, "NO AUTOMATIC PROVIDER FALLBACK", "A / I"),
    suite("PERSIST", "TIER 1", RESEARCH / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1" / "tests" / "run_provider_response_persistence_tests.py", 8, "RAW PROVIDER EVIDENCE PERSISTS BEFORE VALIDATION", "A"),
    suite("SW-INT", "TIER 1", RESEARCH / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1" / "tests" / "run_scene_writer_integration_contract_tests.py", 15, "MACHINE TOKEN != DISPLAY PROSE", "B / D"),
    suite("SER", "TIER 1", RESEARCH / "E2E_Targeted_Repair_02_Scene_Writer_Response_Budget_Serialization_V0.1" / "tests" / "run_scene_writer_serialization_tests.py", 12, "NO SILENT REPAIR", "E"),
    suite("TRUNC", "TIER 1", RESEARCH / "E2E_Targeted_Repair_02_Scene_Writer_Response_Budget_Serialization_V0.1" / "tests" / "run_scene_writer_truncation_detection_tests.py", 4, "RAW PROVIDER EVIDENCE PERSISTS BEFORE VALIDATION", "E"),
    suite("STRICT", "TIER 2", RESEARCH / "E2E_Targeted_Repair_03_Strict_Structured_Transport_V0.1" / "tests" / "run_scene_writer_strict_transport_tests.py", 15, "TRANSPORT OWNS TRANSPORT", "C"),
    suite("TOKEN", "TIER 2", RESEARCH / "E2E_Targeted_Repair_03A_Canonical_Token_Alignment_V0.1" / "tests" / "run_scene_writer_canonical_token_tests.py", 10, "CANONICAL TOKENS MUST REMAIN EXACT", "D"),
    suite("Probe03 Recorded", "TIER 2", RESEARCH / "E2E_Targeted_Repair_03A_Canonical_Token_Alignment_V0.1" / "tests" / "run_scene_writer_probe03_recorded_response_regression.py", 5, "CANONICAL TOKENS MUST REMAIN EXACT", "C / D"),
    suite("SHOWRUNNER-OWN", "TIER 2", RESEARCH / "E2E_Targeted_Repair_04_Showrunner_Transport_Ownership_Separation_V0.1" / "tests" / "run_showrunner_transport_ownership_tests.py", 10, "TRANSPORT MAY REPRESENT ABSENCE BUT MAY NOT INVENT ROLE SEMANTICS", "F"),
    suite("DIR-INT", "TIER 2", RESEARCH / "E2E_Targeted_Repair_05_Director_Output_Contract_Transport_Alignment_V0.1" / "tests" / "run_director_integration_contract_tests.py", 12, "DISPLAY HEADING != MACHINE IDENTITY", "B / G"),
    suite("AD-INT", "TIER 2", RESEARCH / "E2E_Targeted_Repair_06_Art_Director_Output_Contract_Parser_Alignment_V0.1" / "tests" / "run_art_director_integration_contract_tests.py", 12, "DISPLAY HEADING != MACHINE IDENTITY", "B / G"),
    suite("AD-RERUN04", "TIER 2", RESEARCH / "E2E_Targeted_Repair_06_Art_Director_Output_Contract_Parser_Alignment_V0.1" / "tests" / "run_art_director_recorded_reassessment_regression.py", 8, "NO SILENT REPAIR", "G"),
    suite("P0/P1 Reliability", "TIER 1+2", PHASE / "tests" / "run_runtime_reliability_contract_tests.py", 9, "ROLE OWNS SEMANTICS / TRANSPORT OWNS TRANSPORT", "A / C / F / I"),
    suite("STRICT-LIFE", "TIER 1+2", RESEARCH / "E2E_Targeted_Repair_11_Strict_Transport_Lifecycle_Authorization_V0.1" / "tests" / "run_strict_transport_lifecycle_tests.py", 30, "STRICT TRANSPORT REQUIRES AN EXACT AUTHORIZED ROLE/FUNCTION PAIR", "C / I"),
    suite("DIR-STATE-OBJ", "TIER 1+2", RESEARCH / "E2E_Targeted_Repair_09K_Director_State_Object_Contract_Implementation_V0.1" / "tests" / "run_director_state_object_phase2_regression.py", 12, "CONTRACT DRIVES STATE OBJECT PROJECTION", "G / H / J"),
    suite("AD-ALIGN-CORE", "TIER 1+2", RESEARCH / "E2E_Targeted_Repair_12_Art_Director_Output_Contract_Validator_Alignment_V0.1" / "tests" / "run_art_director_alignment_core_tests.py", 17, "PROMPT = PROVIDER CONTRACT = VALIDATOR", "B / G / H"),
    suite("AD-ALIGN-NEG", "TIER 1+2", RESEARCH / "E2E_Targeted_Repair_12_Art_Director_Output_Contract_Validator_Alignment_V0.1" / "tests" / "run_art_director_alignment_negative_tests.py", 12, "ABSENCE OF IRRELEVANT CONTENT IS NOT A FAILURE", "B / G / H"),
    suite("CA-TRANS-CORE", "TIER 1+2", RESEARCH / "E2E_Targeted_Repair_13_Character_Acting_Reserved_Transport_Slot_Alignment_V0.1" / "tests" / "run_character_acting_transport_core_tests.py", 17, "ROLE OWNS SEMANTICS / TRANSPORT OWNS TRANSPORT", "F / I"),
    suite("CA-TRANS-NEG", "TIER 1+2", RESEARCH / "E2E_Targeted_Repair_13_Character_Acting_Reserved_Transport_Slot_Alignment_V0.1" / "tests" / "run_character_acting_transport_negative_tests.py", 12, "RESERVED TRANSPORT MAY REPRESENT ABSENCE BUT MAY NOT INVENT SEMANTICS", "F / I"),
    suite("CONT-ALIGN-CORE", "TIER 1+2", RESEARCH / "E2E_Targeted_Repair_14_Continuity_Machine_Outcome_Parser_Alignment_V0.1" / "tests" / "run_continuity_alignment_core_tests.py", 17, "CANONICAL OUTCOME IS MACHINE IDENTITY", "B / G / H"),
    suite("CONT-ALIGN-NEG", "TIER 1+2", RESEARCH / "E2E_Targeted_Repair_14_Continuity_Machine_Outcome_Parser_Alignment_V0.1" / "tests" / "run_continuity_alignment_negative_tests.py", 12, "MACHINE TOKEN != DISPLAY PROSE", "B / G / H"),
)


def run_suite(item: dict[str, str | int | Path]) -> dict[str, Any]:
    script = Path(item["script"])
    completed = subprocess.run([sys.executable, "-X", "utf8", "-B", str(script)], cwd=str(AUTOMATION_ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        payload = {}
    expected = int(item["expected"])
    reported_total = payload.get("total")
    reported_passed = payload.get("passed")
    result_value = payload.get("result")
    pass_by_count = expected > 0 and reported_total == expected and reported_passed == expected
    pass_by_result = expected == 0 and result_value == "PASS"
    passed = completed.returncode == 0 and (pass_by_count or pass_by_result)
    return {
        "suite": item["suite"], "tier": item["tier"], "invariant": item["invariant"], "failure_lineage": item["lineage"],
        "script": str(script), "expected": expected, "reported_passed": reported_passed, "reported_total": reported_total,
        "result": "PASS" if passed else "FAIL", "returncode": completed.returncode,
        "provider_calls": payload.get("provider_calls", 0), "executor_calls": payload.get("executor_calls", 0), "stdout": completed.stdout, "stderr": completed.stderr,
    }


def main() -> int:
    records = [run_suite(dict(item)) for item in SUITES]
    golden = validate_golden_recorded_evidence(evidence_root=HARNESS / "evidence" / "E2E-RUN-05")
    records.append({"suite": "Golden Recorded Regression", "tier": "TIER 2", "invariant": "ROLE OWNS SEMANTICS / CANONICAL TOKENS MUST REMAIN EXACT", "failure_lineage": "A / C / D / F / G / H / I / J", "script": "recorded E2E-RUN-05 evidence", "expected": 0, "reported_passed": None, "reported_total": None, "result": golden["result"], "returncode": 0 if golden["result"] == "PASS" else 1, "provider_calls": 0, "executor_calls": 0, "golden": golden})
    overall = "PASS" if all(record["result"] == "PASS" for record in records) else "FAIL"
    output = {"classification": "AI FILM STUDIO SYSTEMIC REGRESSION GATE", "overall": overall, "records": records, "provider_calls": 0, "executor_calls": 0, "role_calls": 0, "real_e2e_runs": 0}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
