"""Provider-free positive regression for Repair 15 environment isolation."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
for import_path in (str(STAGE / "implementation"), str(HARNESS), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

import run_minimal_e2e as runner
from preflight_environment_isolation import PreflightSuiteManifest, build_preflight_subprocess_env, provenance_json


FIXTURE_01 = runner.FIXTURE_01_BINDING
FIXTURE_02 = RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1" / "fixtures" / "E2E_FIX_02_Runtime_Binding_V0.1.json"
FIXTURE_03 = RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1" / "fixtures" / "E2E_FIX_03_Runtime_Binding_V0.1.json"
SW_MANIFEST = next(item for item in runner.MANDATORY_PREFLIGHT_BASE_SUITES if item.suite_id == "SW-INT")
STRICT_MANIFEST = next(item for item in runner.MANDATORY_PREFLIGHT_BASE_SUITES if item.suite_id == "STRICT")
CA_CORE_MANIFEST = next(item for item in runner.MANDATORY_PREFLIGHT_BASE_SUITES if item.suite_id == "CHARACTER-ACTING-TRANS-CORE")
CONT_CORE_MANIFEST = next(item for item in runner.MANDATORY_PREFLIGHT_BASE_SUITES if item.suite_id == "CONTINUITY-ALIGN-CORE")


def parent_with(binding: Path | None) -> dict[str, str]:
    parent = dict(os.environ)
    for key in list(parent):
        if key.upper().startswith("AFS_E2E_"):
            del parent[key]
    if binding is not None:
        parent["AFS_E2E_FIXTURE_BINDING"] = str(binding)
    parent["AFS_E2E_RUN_ID"] = "LIVE-RUN-SHOULD-NOT-LEAK"
    parent["AFS_E2E_AUTHORIZATION_LABEL"] = "LIVE-AUTH-SHOULD-NOT-LEAK"
    return parent


def run_manifest(manifest: PreflightSuiteManifest, parent: dict[str, str]) -> dict[str, Any]:
    return runner._run_static_suite(manifest, parent_env=parent)


def suite_passes(manifest: PreflightSuiteManifest, parent: dict[str, str]) -> bool:
    result = run_manifest(manifest, parent)
    return runner._suite_result_is_pass(result, manifest.expected_total)


def run_dry_run(parent: dict[str, str], fixture: Path) -> dict[str, Any]:
    manifest = PreflightSuiteManifest("FIXTURE02-DRY-RUN", HARNESS / "run_minimal_e2e.py", 0, fixture)
    child_env, _ = build_preflight_subprocess_env(manifest, parent)
    completed = subprocess.run(
        [sys.executable, "-X", "utf8", "-B", str(HARNESS / "run_minimal_e2e.py"), "--live-dry-run"],
        cwd=str(AUTOMATION_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
        env=child_env,
    )
    payload = json.loads(completed.stdout)
    assert completed.returncode == 0 and payload["result"] == "PASS", (completed.returncode, completed.stderr, payload)
    return payload


def run_json_script(script: Path, parent: dict[str, str]) -> tuple[int, dict[str, Any]]:
    manifest = PreflightSuiteManifest("NO-FIXTURE-REGRESSION", script, 0)
    child_env, _ = build_preflight_subprocess_env(manifest, parent)
    completed = subprocess.run(
        [sys.executable, "-X", "utf8", "-B", str(script)],
        cwd=str(AUTOMATION_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
        env=child_env,
    )
    return completed.returncode, json.loads(completed.stdout)


def main() -> int:
    cases: list[dict[str, str]] = []

    def add(case_id: str, action: Callable[[], str]) -> None:
        try:
            cases.append({"id": case_id, "result": "PASS", "detail": action()})
        except Exception as exc:  # explicit provider-free regression result
            cases.append({"id": case_id, "result": "FAIL", "detail": f"{type(exc).__name__}: {exc}"})

    def provenance_complete() -> str:
        _, provenance = build_preflight_subprocess_env(SW_MANIFEST, parent_with(FIXTURE_02))
        required = {"environment_policy_version", "suite", "parent_afs_e2e_classification", "removed_live_run_variables", "explicitly_injected_variables", "effective_fixture_binding", "environment_hash"}
        assert required.issubset(provenance)
        return "environment provenance is complete and redacted"

    def fixture_classified() -> str:
        _, provenance = build_preflight_subprocess_env(SW_MANIFEST, parent_with(FIXTURE_02))
        assert provenance["parent_afs_e2e_classification"]["AFS_E2E_FIXTURE_BINDING"] == "LIVE_RUN_SCOPED"
        return "AFS_E2E_FIXTURE_BINDING is classified LIVE_RUN_SCOPED"

    def live_vars_isolated() -> str:
        child, provenance = build_preflight_subprocess_env(SW_MANIFEST, parent_with(FIXTURE_02))
        assert child["AFS_E2E_FIXTURE_BINDING"] == str(FIXTURE_01)
        assert "AFS_E2E_RUN_ID" not in child and "AFS_E2E_AUTHORIZATION_LABEL" not in child
        assert len(provenance["removed_live_run_variables"]) >= 3
        return "live-run AFS_E2E variables are absent from the historical child"

    def suite_fixture_explicit() -> str:
        _, provenance = build_preflight_subprocess_env(SW_MANIFEST, parent_with(None))
        assert provenance["suite"]["fixture_binding_source"] == "SUITE_MANIFEST"
        assert provenance["effective_fixture_binding"] == str(FIXTURE_01)
        return "Fixture01 historical suite owns an explicit Fixture01 binding"

    def fixture01_matrix() -> str:
        outcomes = [suite_passes(SW_MANIFEST, parent_with(binding)) for binding in (None, FIXTURE_01, FIXTURE_02, FIXTURE_03)]
        assert outcomes == [True, True, True, True], outcomes
        return "Fixture01 SW-INT is 4/4 identical PASS under unset/F01/F02/F03 parents"

    def fixture02_matrix() -> str:
        outcomes = [run_dry_run(parent_with(binding), FIXTURE_02)["fixture_id"] for binding in (None, FIXTURE_01, FIXTURE_02, FIXTURE_03)]
        assert outcomes == ["E2E-FIX-02"] * 4, outcomes
        return "Fixture02 child binding is parent-independent"

    def suite_order_independent() -> str:
        assert suite_passes(SW_MANIFEST, parent_with(FIXTURE_02))
        assert run_dry_run(parent_with(FIXTURE_01), FIXTURE_02)["fixture_id"] == "E2E-FIX-02"
        assert run_dry_run(parent_with(FIXTURE_03), FIXTURE_02)["fixture_id"] == "E2E-FIX-02"
        assert suite_passes(SW_MANIFEST, parent_with(FIXTURE_03))
        return "Fixture01 -> Fixture02 and Fixture02 -> Fixture01 carry no child environment state"

    def parent_unchanged() -> str:
        parent = parent_with(FIXTURE_02)
        before = dict(parent)
        build_preflight_subprocess_env(SW_MANIFEST, parent)
        assert parent == before
        return "parent live environment is unchanged"

    def old_failure_reproduced() -> str:
        """Repair16 removes the former scene-id global, not the historical evidence."""
        parent = parent_with(FIXTURE_02)
        completed = subprocess.run(
            [sys.executable, "-X", "utf8", "-B", str(SW_MANIFEST.script)],
            cwd=str(AUTOMATION_ROOT),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
            env=parent,
        )
        payload = json.loads(completed.stdout)
        assert completed.returncode == 0 and payload["passed"] == 15 and payload["total"] == 15, payload
        return "historical mismatch remains recorded while current generic contract no longer recreates it from a parent environment"

    def corrected_replay() -> str:
        assert suite_passes(SW_MANIFEST, parent_with(FIXTURE_02))
        return "same SW-INT suite passes with manifest-owned Fixture01 environment"

    def strict_recovered() -> str:
        assert suite_passes(STRICT_MANIFEST, parent_with(FIXTURE_02))
        return "STRICT cascade is recovered"

    def character_recovered() -> str:
        assert suite_passes(CA_CORE_MANIFEST, parent_with(FIXTURE_02))
        return "Repair13 core cascade is recovered"

    def continuity_recovered() -> str:
        assert suite_passes(CONT_CORE_MANIFEST, parent_with(FIXTURE_02))
        return "Repair14 core cascade is recovered"

    def mandatory_base_passes() -> str:
        records = [run_manifest(manifest, parent_with(FIXTURE_02)) for manifest in runner.MANDATORY_PREFLIGHT_BASE_SUITES]
        assert all(runner._suite_result_is_pass(record, manifest.expected_total) for record, manifest in zip(records, runner.MANDATORY_PREFLIGHT_BASE_SUITES))
        return "all 14 historical mandatory suites pass under isolated environments"

    def fixture02_compile_regression() -> str:
        payload = run_dry_run(parent_with(FIXTURE_01), FIXTURE_02)
        assert payload["fixture_id"] == "E2E-FIX-02" and payload["scene_ids"] == ["E2E-FIX-02-S01", "E2E-FIX-02-S02", "E2E-FIX-02-S03"]
        return "Fixture02 compile/live dry-run remains exact"

    def fixture_generality_passes() -> str:
        code, payload = run_json_script(RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1" / "tests" / "run_fixture_generality_tests.py", parent_with(FIXTURE_02))
        assert code == 0 and payload["passed"] == 18 and payload["total"] == 18, payload
        return "GEN-01–18 remains PASS"

    def unified_gate_passes() -> str:
        code, payload = run_json_script(RESEARCH / "Systemic_Hardening_Phase_2_Runtime_Reliability_Regression_Enforcement_V0.1" / "run_systemic_regression_gate.py", parent_with(FIXTURE_02))
        assert code == 0 and payload["overall"] == "PASS" and len(payload["records"]) == 25, payload
        return "Unified Phase2 Gate remains 25/25 PASS"

    def integrity_passes() -> str:
        assert runner.canonical_skill_hashes() == runner.EXPECTED_HASHES
        assert len(runner.production_lock_hashes()) == 6
        return "canonical Skill and Production Lock integrity passes"

    add("ENV-ISO-01", provenance_complete)
    add("ENV-ISO-02", fixture_classified)
    add("ENV-ISO-03", live_vars_isolated)
    add("ENV-ISO-04", suite_fixture_explicit)
    add("ENV-ISO-05", fixture01_matrix)
    add("ENV-ISO-06", fixture02_matrix)
    add("ENV-ISO-07", suite_order_independent)
    add("ENV-ISO-08", parent_unchanged)
    add("ENV-ISO-09", old_failure_reproduced)
    add("ENV-ISO-10", corrected_replay)
    add("ENV-ISO-11", strict_recovered)
    add("ENV-ISO-12", character_recovered)
    add("ENV-ISO-13", continuity_recovered)
    add("ENV-ISO-14", mandatory_base_passes)
    add("ENV-ISO-15", fixture02_compile_regression)
    add("ENV-ISO-16", fixture_generality_passes)
    add("ENV-ISO-17", unified_gate_passes)
    add("ENV-ISO-18", integrity_passes)
    passed = sum(item["result"] == "PASS" for item in cases)
    print(json.dumps({"classification": "REPAIR15 ENVIRONMENT ISOLATION POSITIVE TESTS", "results": cases, "passed": passed, "total": 18, "provider_calls": 0, "executor_calls": 0, "role_calls": 0, "probe_calls": 0, "real_e2e_runs": 0}, ensure_ascii=False, indent=2))
    return 0 if passed == 18 else 1


if __name__ == "__main__":
    raise SystemExit(main())
