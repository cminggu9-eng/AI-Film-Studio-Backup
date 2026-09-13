"""Provider-free negative regression for Repair 15 environment isolation."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Callable


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
SW_MANIFEST = next(item for item in runner.MANDATORY_PREFLIGHT_BASE_SUITES if item.suite_id == "SW-INT")


def parent_with(binding: Path | None) -> dict[str, str]:
    parent = dict(os.environ)
    for key in list(parent):
        if key.upper().startswith("AFS_E2E_"):
            del parent[key]
    if binding is not None:
        parent["AFS_E2E_FIXTURE_BINDING"] = str(binding)
    return parent


def main() -> int:
    results: list[dict[str, str]] = []

    def reject(case_id: str, action: Callable[[], str]) -> None:
        try:
            results.append({"id": case_id, "result": "PASS", "detail": action()})
        except Exception as exc:
            results.append({"id": case_id, "result": "FAIL", "detail": f"{type(exc).__name__}: {exc}"})

    def f02_to_f01_rejected() -> str:
        child, _ = build_preflight_subprocess_env(SW_MANIFEST, parent_with(FIXTURE_02))
        assert child["AFS_E2E_FIXTURE_BINDING"] != str(FIXTURE_02)
        return "Fixture02 parent binding cannot leak into Fixture01 suite"

    def f01_to_f02_rejected() -> str:
        fixture02_suite = PreflightSuiteManifest("F02", HARNESS / "run_minimal_e2e.py", 0, FIXTURE_02)
        child, _ = build_preflight_subprocess_env(fixture02_suite, parent_with(FIXTURE_01))
        assert child["AFS_E2E_FIXTURE_BINDING"] != str(FIXTURE_01)
        return "Fixture01 parent binding cannot leak into Fixture02 suite"

    def parent_inference_rejected() -> str:
        no_fixture_suite = PreflightSuiteManifest("NO-FIXTURE", HARNESS / "tests" / "test_minimal_e2e_harness_startup.py", 0)
        child, _ = build_preflight_subprocess_env(no_fixture_suite, parent_with(FIXTURE_02))
        assert "AFS_E2E_FIXTURE_BINDING" not in child
        return "suite fixture cannot be inferred from parent environment"

    def unknown_removed() -> str:
        parent = parent_with(FIXTURE_02)
        parent["AFS_E2E_UNDECLARED"] = "must-not-leak"
        child, provenance = build_preflight_subprocess_env(SW_MANIFEST, parent)
        assert "AFS_E2E_UNDECLARED" not in child
        assert provenance["parent_afs_e2e_classification"]["AFS_E2E_UNDECLARED"] == "UNKNOWN_AFS_E2E"
        return "unknown AFS_E2E variable is removed rather than inherited"

    def no_carryover() -> str:
        first, _ = build_preflight_subprocess_env(SW_MANIFEST, parent_with(FIXTURE_01))
        fixture02_suite = PreflightSuiteManifest("F02", HARNESS / "run_minimal_e2e.py", 0, FIXTURE_02)
        second, _ = build_preflight_subprocess_env(fixture02_suite, parent_with(FIXTURE_01))
        assert first["AFS_E2E_FIXTURE_BINDING"] == str(FIXTURE_01)
        assert second["AFS_E2E_FIXTURE_BINDING"] == str(FIXTURE_02)
        return "previous child fixture cannot carry into next suite"

    def no_global_mutation() -> str:
        before = dict(os.environ)
        build_preflight_subprocess_env(SW_MANIFEST, parent_with(FIXTURE_02))
        assert dict(os.environ) == before
        return "builder does not mutate os.environ"

    def historical_ids_not_rewritten() -> str:
        assert SW_MANIFEST.fixture_binding == FIXTURE_01
        return "Fixture01 historical expected IDs remain suite-owned"

    def no_fixture_hardcode() -> str:
        source = (STAGE / "implementation" / "preflight_environment_isolation.py").read_text(encoding="utf-8")
        assert all(token not in source for token in ("E2E-FIX-01", "E2E-FIX-02", "E2E-FIX-03"))
        return "generic isolation code contains no fixture business hardcode"

    def secret_not_emitted() -> str:
        parent = parent_with(FIXTURE_02)
        parent["DEEPSEEK_API_KEY"] = "secret-value-must-not-appear"
        parent["AFS_E2E_UNKNOWN_SECRET"] = "unknown-secret-must-not-appear"
        child, provenance = build_preflight_subprocess_env(SW_MANIFEST, parent)
        rendered = provenance_json(provenance)
        assert "DEEPSEEK_API_KEY" not in child and "secret-value-must-not-appear" not in rendered and "unknown-secret-must-not-appear" not in rendered
        return "provider secrets are absent from child environment evidence"

    def failure_not_skipped() -> str:
        missing = PreflightSuiteManifest("MISSING", STAGE / "tests" / "missing_suite.py", 1)
        record = runner._run_static_suite(missing, parent_env=parent_with(FIXTURE_02))
        assert runner._suite_result_is_pass(record, missing.expected_total) is False
        return "failed suite is represented as failure and cannot be skipped"

    def cascade_not_role_semantic() -> str:
        corrected = HARNESS / "evidence" / "E2E-RUN-19" / "R02_Corrected_Failure_Attribution_Analysis_V0.1.md"
        text = corrected.read_text(encoding="utf-8")
        assert "PRE-FLIGHT ENVIRONMENT ISOLATION / RUNTIME HARNESS FAILURE" in text and "Not a role semantic failure" in text
        return "same-root cascade remains preflight harness attribution"

    def parent_change_determinism_rejected() -> str:
        first, _ = build_preflight_subprocess_env(SW_MANIFEST, parent_with(FIXTURE_01))
        second, _ = build_preflight_subprocess_env(SW_MANIFEST, parent_with(FIXTURE_02))
        assert first["AFS_E2E_FIXTURE_BINDING"] == second["AFS_E2E_FIXTURE_BINDING"] == str(FIXTURE_01)
        return "parent fixture cannot alter deterministic suite binding"

    reject("ENV-ISO-NEG-01", f02_to_f01_rejected)
    reject("ENV-ISO-NEG-02", f01_to_f02_rejected)
    reject("ENV-ISO-NEG-03", parent_inference_rejected)
    reject("ENV-ISO-NEG-04", unknown_removed)
    reject("ENV-ISO-NEG-05", no_carryover)
    reject("ENV-ISO-NEG-06", no_global_mutation)
    reject("ENV-ISO-NEG-07", historical_ids_not_rewritten)
    reject("ENV-ISO-NEG-08", no_fixture_hardcode)
    reject("ENV-ISO-NEG-09", secret_not_emitted)
    reject("ENV-ISO-NEG-10", failure_not_skipped)
    reject("ENV-ISO-NEG-11", cascade_not_role_semantic)
    reject("ENV-ISO-NEG-12", parent_change_determinism_rejected)
    passed = sum(item["result"] == "PASS" for item in results)
    print(json.dumps({"classification": "REPAIR15 ENVIRONMENT ISOLATION NEGATIVE TESTS", "results": results, "passed": passed, "total": 12, "provider_calls": 0, "executor_calls": 0, "role_calls": 0, "probe_calls": 0, "real_e2e_runs": 0}, ensure_ascii=False, indent=2))
    return 0 if passed == 12 else 1


if __name__ == "__main__":
    raise SystemExit(main())

