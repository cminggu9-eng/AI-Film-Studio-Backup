"""Run Repair21 mandatory provider-free gates without writing historical evidence."""

from __future__ import annotations

import json
import os
import subprocess
import sys

from repair21_support import AUTOMATION_ROOT, PHASE2, REPAIR_07
import run_minimal_e2e as e2e


def run_json(script):
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
    return completed.returncode, payload


def main() -> int:
    for key in tuple(os.environ):
        if key.upper().startswith("AFS_E2E_"):
            os.environ.pop(key)
    preflight = e2e.rerun_preflight()
    generic_code, generic = run_json(REPAIR_07 / "tests" / "run_fixture_generality_tests.py")
    phase2_code, phase2 = run_json(PHASE2 / "run_systemic_regression_gate.py")
    output = {
        "classification": "REPAIR21 OFFLINE GATE RUN",
        "mandatory_preflight": {
            "passed": preflight.get("passed") is True,
            "suite_count": len(preflight.get("required_suites", {})),
            "required_suites": preflight.get("required_suites", {}),
        },
        "genericity": {"returncode": generic_code, "passed": generic.get("passed"), "total": generic.get("total")},
        "unified_phase2": {"returncode": phase2_code, "overall": phase2.get("overall"), "record_count": len(phase2.get("records", []))},
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "live_e2e_runs": 0,
    }
    passed = (
        output["mandatory_preflight"]["passed"]
        and output["mandatory_preflight"]["suite_count"] == 15
        and generic_code == 0
        and generic.get("passed") == 18
        and generic.get("total") == 18
        and phase2_code == 0
        and phase2.get("overall") == "PASS"
        and len(phase2.get("records", [])) == 25
    )
    output["overall"] = "PASS" if passed else "FAIL"
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
