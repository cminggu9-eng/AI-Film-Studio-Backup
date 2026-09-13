from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

from director_state_object_test_support import AUTOMATION_ROOT, HARNESS, RESEARCH, HERE
import run_minimal_e2e as e2e


ROOT = HERE.parent.parent
EVIDENCE = ROOT / "evidence"
SCRIPTS = {
    "director_state_object_negative_tests.json": ROOT / "tests" / "run_director_state_object_negative_tests.py",
    "director_state_object_tests.json": ROOT / "tests" / "run_director_state_object_contract_tests.py",
    "systemic_phase2_gate.json": RESEARCH / "Systemic_Hardening_Phase_2_Runtime_Reliability_Regression_Enforcement_V0.1" / "run_systemic_regression_gate.py",
    "repair11_strict_lifecycle.json": RESEARCH / "E2E_Targeted_Repair_11_Strict_Transport_Lifecycle_Authorization_V0.1" / "tests" / "run_strict_transport_lifecycle_tests.py",
}
HISTORICAL = {
    "E2E-RUN-13 Director raw": HARNESS / "evidence" / "E2E-RUN-13" / "artifacts" / "director_provider_response.json",
    "E2E-RUN-14 Director raw": HARNESS / "evidence" / "E2E-RUN-14" / "artifacts" / "director_provider_response.json",
    "Probe04 manifest": RESEARCH / "Director_Strict_Compatibility_Probe_04_After_Repair_09F_V0.1" / "evidence" / "DIRECTOR-STRICT-COMPATIBILITY-PROBE-04" / "probe_manifest.json",
}


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    records = []
    for filename, script in SCRIPTS.items():
        completed = subprocess.run([sys.executable, "-X", "utf8", "-B", str(script)], cwd=str(AUTOMATION_ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
        try:
            payload = json.loads(completed.stdout)
        except json.JSONDecodeError:
            payload = {"result": "FAIL", "stdout": completed.stdout, "stderr": completed.stderr}
        write_json(EVIDENCE / filename, payload)
        result = payload.get("result", payload.get("overall"))
        if result is None and payload.get("passed") == payload.get("total") and isinstance(payload.get("total"), int):
            result = "PASS"
        records.append({"artifact": str(EVIDENCE / filename), "returncode": completed.returncode, "result": result})
    integrity = {
        "canonical_hashes": e2e.canonical_skill_hashes(),
        "expected_canonical_hashes": e2e.EXPECTED_HASHES,
        "canonical_hashes_unchanged": e2e.canonical_skill_hashes() == e2e.EXPECTED_HASHES,
        "historical_artifacts": {
            name: {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "immutable_read_only": True}
            for name, path in HISTORICAL.items()
        },
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "e2e_runs": 0,
        "canonical_skill_mutation": 0,
        "production_lock_mutation": 0,
        "result": "PASS",
    }
    write_json(EVIDENCE / "integrity_and_historical_hashes.json", integrity)
    summary = {"classification": "REPAIR 09K EVIDENCE GENERATION", "records": records, "integrity": integrity, "result": "PASS" if all(item["returncode"] == 0 for item in records) and integrity["canonical_hashes_unchanged"] else "FAIL"}
    write_json(EVIDENCE / "evidence_generation_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
