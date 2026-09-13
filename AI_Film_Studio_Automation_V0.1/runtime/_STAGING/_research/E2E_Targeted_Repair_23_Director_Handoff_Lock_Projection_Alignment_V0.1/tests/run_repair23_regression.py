"""Repair23 provider-free regression, integrity, and historical immutability gate."""
from __future__ import annotations

import copy
import json
import os
import subprocess
import sys
from pathlib import Path

from repair23_support import *
from repair22_support import PROBE21, R26_ARTIFACTS, outer_arguments, projection_audit, wire_fixture
from director_provider_compatibility import DirectorProviderWireError

PHASE2 = RESEARCH / "Systemic_Hardening_Phase_2_Runtime_Reliability_Regression_Enforcement_V0.1"
REPAIR07 = RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1"


def run_json(script: Path):
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
        payload = {"stdout_tail": completed.stdout[-2000:], "stderr_tail": completed.stderr[-2000:]}
    return completed.returncode, payload


def rejected(payload, contract) -> bool:
    try:
        validate_director_provider_wire_arguments(payload, contract)
    except DirectorProviderWireError:
        return True
    return False


def codec_regression(contract) -> Dict[str, Any]:
    audit = projection_audit(contract)
    present = wire_fixture(contract)
    absent = wire_fixture(contract, "ABSENT", [])
    empty = wire_fixture(contract, "PRESENT", [])
    decoded_present = decode_director_provider_wire_arguments(validate_director_provider_wire_arguments(present, contract), contract)
    decoded_absent = decode_director_provider_wire_arguments(validate_director_provider_wire_arguments(absent, contract), contract)
    decoded_empty = decode_director_provider_wire_arguments(validate_director_provider_wire_arguments(empty, contract), contract)
    r26 = outer_arguments(R26_ARTIFACTS / "director_provider_response.json")
    probe21 = outer_arguments(PROBE21)
    assertions = {
        "canonical_outer_field_count_15": len(audit["canonical"]["required"]) == 15,
        "only_unresolved_decisions_tagged": audit["manifest"]["tagged_union_fields"] == ["unresolved_decisions"],
        "present_native_array_roundtrip": decoded_present["unresolved_decisions"] == ["unresolved-decision"],
        "absent_roundtrip": decoded_absent["unresolved_decisions"] == "ABSENT",
        "empty_array_not_absent": decoded_empty["unresolved_decisions"] == [] and decoded_empty["unresolved_decisions"] != decoded_absent["unresolved_decisions"],
        "r26_legacy_string_rejected": rejected(r26, contract),
        "probe21_legacy_string_rejected": rejected(probe21, contract),
    }
    return {"overall": "PASS" if all(assertions.values()) else "FAIL", "passed": sum(assertions.values()), "total": len(assertions), "assertions": assertions}


def main() -> int:
    for key in tuple(os.environ):
        if key.upper().startswith("AFS_E2E_"):
            os.environ.pop(key)
    historical_before = historical_e2e_digests()
    probe22_before = tree_digest(PROBE22)
    r26_manifest = read_json(R26 / "execution_manifest.json")

    preflight = e2e.rerun_preflight()
    generic_code, generic = run_json(REPAIR07 / "tests" / "run_fixture_generality_tests.py")
    phase2_code, phase2 = run_json(PHASE2 / "run_systemic_regression_gate.py")
    _, contract = state_contract()
    codec = codec_regression(contract)

    historical_after = historical_e2e_digests()
    probe22_after = tree_digest(PROBE22)
    canonical_now = e2e.canonical_skill_hashes()
    locks_now = e2e.production_lock_hashes()
    result = {
        "classification": "REPAIR23 PROVIDER-FREE REGRESSION",
        "mandatory_preflight": {"overall": "PASS" if preflight.get("passed") is True and len(preflight.get("required_suites", {})) == 15 else "FAIL", "passed": len(preflight.get("required_suites", {})), "total": 15},
        "genericity": {"overall": "PASS" if generic_code == 0 and generic.get("passed") == 18 and generic.get("total") == 18 else "FAIL", "passed": generic.get("passed"), "total": generic.get("total")},
        "unified_phase2": {"overall": "PASS" if phase2_code == 0 and phase2.get("overall") == "PASS" and len(phase2.get("records", [])) == 25 else "FAIL", "records": len(phase2.get("records", []))},
        "repair22_tagged_codec": codec,
        "canonical_skills": {"overall": "PASS" if canonical_now == r26_manifest["final_canonical_skill_hashes"] and len(canonical_now) == 7 else "FAIL", "unchanged": canonical_now == r26_manifest["final_canonical_skill_hashes"], "count": len(canonical_now)},
        "production_locks": {"overall": "PASS" if locks_now == r26_manifest["production_lock_hashes_after"] and len(locks_now) == 6 else "FAIL", "unchanged": locks_now == r26_manifest["production_lock_hashes_after"], "count": len(locks_now)},
        "historical_e2e_06_26": {"overall": "PASS" if historical_before == historical_after and len(historical_after) == 21 else "FAIL", "unchanged": historical_before == historical_after, "count": len(historical_after)},
        "probe22_evidence": {"overall": "PASS" if probe22_before == probe22_after else "FAIL", "unchanged": probe22_before == probe22_after, "tree_sha256": probe22_after},
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "live_e2e_calls": 0,
    }
    gates = (result["mandatory_preflight"], result["genericity"], result["unified_phase2"], result["repair22_tagged_codec"], result["canonical_skills"], result["production_locks"], result["historical_e2e_06_26"], result["probe22_evidence"])
    result["overall"] = "PASS" if all(item["overall"] == "PASS" for item in gates) else "FAIL"
    e2e.write_json(REPORTS / "Repair23_Regression_Result.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["overall"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
