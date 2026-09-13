"""Synthetic, non-semantic contract tests for Scene Writer Runtime V0.1."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Dict


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
for path in (str(STAGE), str(AUTOMATION_ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)

from runtime.scene_writer.scene_writer_runtime import SceneWriterRuntime  # noqa: E402


FIXTURES = json.loads((STAGE / "fixtures" / "scene_writer_runtime_synthetic_fixtures.json").read_text(encoding="utf-8"))["fixtures"]


def base_input(request_id: str, fixture_id: str, mode: str | None = None) -> Dict[str, Any]:
    fixture = FIXTURES[fixture_id]
    return {
        "request_id": request_id,
        "requested_mode": mode or fixture["mode"],
        "assignment_language": "en-US",
        "project_id": "SYNTHETIC-PROJECT",
        "episode_id": "SYNTHETIC-EPISODE",
        "scene_id": fixture_id,
        "scene_purpose": "synthetic contract transport only",
        "canon_locks": [],
        "showrunner_locks": [],
        "participants": [],
        "character_context": {},
        "required_event": None,
        "required_information": None,
        "required_outcome": None,
        "prior_scene_state": None,
        "desired_post_state": None,
        "production_constraints": None,
        "requested_form": None,
        "downstream_requests": [],
        "qa_requests": []
    }


class FixtureExecutor:
    def __init__(self, outputs: Dict[str, Any] | None = None) -> None:
        self.outputs = outputs or {name: item["output"] for name, item in FIXTURES.items()}
        self.calls = 0

    def __call__(self, invocation: Dict[str, Any]) -> Dict[str, Any]:
        self.calls += 1
        return copy.deepcopy(self.outputs[invocation["input"]["scene_id"]])


def synthetic_runtime(executor: FixtureExecutor | None = None) -> tuple[SceneWriterRuntime, FixtureExecutor]:
    fixture_executor = executor or FixtureExecutor()
    return SceneWriterRuntime(synthetic_executor=fixture_executor, test_sandbox=True), fixture_executor


def expect_success(runtime: SceneWriterRuntime, fixture_id: str, request_id: str) -> Dict[str, Any]:
    result = runtime.execute(base_input(request_id, fixture_id))
    assert result["runtime_status"] == "SUCCESS", result
    return result


def malformed_output(output: Dict[str, Any], fixture_id: str = "RT-SW-CREATE-01") -> Dict[str, Any]:
    executor = FixtureExecutor({fixture_id: output})
    runtime, _ = synthetic_runtime(executor)
    result = runtime.execute(base_input("MAL-" + fixture_id, fixture_id))
    assert result["runtime_status"] == "FAIL_SAFE", result
    assert result["runtime_failure_code"] == "MALFORMED_EXECUTOR_OUTPUT", result
    return result


def run_case(case_id: str, func) -> Dict[str, Any]:
    try:
        detail = func()
        return {"id": case_id, "result": "PASS", "detail": detail or ""}
    except AssertionError as exc:
        return {"id": case_id, "result": "FAIL", "detail": str(exc)}


def main() -> int:
    results = []

    results.append(run_case("RT-SW-01", lambda: (lambda b: "canonical identity" if b["identity"] == "scene-writer" else (_ for _ in ()).throw(AssertionError(b)))(SceneWriterRuntime().canonical_binding())))
    results.append(run_case("RT-SW-02", lambda: (lambda b: "canonical version" if b["version"] == "V0.1" else (_ for _ in ()).throw(AssertionError(b)))(SceneWriterRuntime().canonical_binding())))

    def hash_lock():
        runtime = SceneWriterRuntime()
        runtime.contract["skill"]["sha256"] = "0" * 64
        result = runtime.execute(base_input("HASH-LOCK", "RT-SW-CREATE-01"))
        assert result["runtime_status"] == "FAIL_SAFE" and result["runtime_failure_code"] == "CANONICAL_BINDING_FAILURE", result
        return "hash mismatch fails safe"
    results.append(run_case("RT-SW-03", hash_lock))

    results.append(run_case("RT-SW-04", lambda: (lambda r: "CREATE transport" if r["scene_writer"]["control_data"]["primary_state"] == "SCENE_CREATED" else (_ for _ in ()).throw(AssertionError(r)))(expect_success(*synthetic_runtime()[0:1], "RT-SW-CREATE-01", "CREATE-01"))))

    def fixture_state(case_id: str, fixture_id: str, expected: str) -> Dict[str, Any]:
        runtime, _ = synthetic_runtime()
        result = expect_success(runtime, fixture_id, case_id)
        assert result["scene_writer"]["control_data"]["primary_state"] == expected, result
        return {"state": expected}

    results.append(run_case("RT-SW-05", lambda: fixture_state("REVISE-01", "RT-SW-REVISE-01", "SCENE_REVISED")))
    results.append(run_case("RT-SW-06", lambda: fixture_state("DIAG-01", "RT-SW-DIAG-01", "NO_MATERIAL_CHANGE")))
    results.append(run_case("RT-SW-07", lambda: fixture_state("NMC-01", "RT-SW-NMC-01", "NO_MATERIAL_CHANGE")))
    results.append(run_case("RT-SW-08", lambda: fixture_state("NC-01", "RT-SW-NC-01", "NEEDS_CONTEXT")))
    results.append(run_case("RT-SW-09", lambda: fixture_state("UP-01", "RT-SW-UP-01", "UPSTREAM_DECISION_REQUIRED")))
    results.append(run_case("RT-SW-10", lambda: fixture_state("OOS-01", "RT-SW-OOS-01", "REQUEST_OUT_OF_SCOPE")))

    def multiple_flags():
        result = fixture_state("MULTI-01", "RT-SW-MULTI-01", "SCENE_CREATED")
        runtime, _ = synthetic_runtime()
        rerun = expect_success(runtime, "RT-SW-MULTI-01", "MULTI-02")
        assert set(rerun["scene_writer"]["control_data"]["flags"]) == {"SHARED_QA_HANDOFF_ELIGIBLE", "DIRECTOR_HANDOFF_ELIGIBLE"}, rerun
        return result
    results.append(run_case("RT-SW-11", multiple_flags))
    results.append(run_case("RT-SW-12", lambda: fixture_state("PROD-01", "RT-SW-PRODUCTION-01", "SCENE_CREATED")))
    results.append(run_case("RT-SW-13", lambda: fixture_state("QA-01", "RT-SW-SHARED-QA-01", "SCENE_CREATED")))
    results.append(run_case("RT-SW-14", lambda: fixture_state("DIR-01", "RT-SW-DIRECTOR-01", "SCENE_CREATED")))
    results.append(run_case("RT-SW-15", lambda: fixture_state("ACT-01", "RT-SW-ACTING-01", "SCENE_CREATED")))
    results.append(run_case("RT-SW-16", lambda: fixture_state("DEF-01", "RT-SW-DEFERRED-01", "SCENE_CREATED")))

    def illegal_mode():
        runtime = SceneWriterRuntime()
        payload = base_input("BAD-MODE", "RT-SW-CREATE-01")
        payload["requested_mode"] = "CREATE_SCENE"
        result = runtime.execute(payload)
        assert result["runtime_status"] == "CONTRACT_ERROR" and result["runtime_failure_code"] == "ILLEGAL_MODE", result
        return "strict mode rejection"
    results.append(run_case("RT-SW-17", illegal_mode))

    def malformed_primary_matrix():
        cases = {
            "RT-MAL-01": {"creative_deliverable": None, "control_data": {"flags": [], "handoffs": []}},
            "RT-MAL-02": {"creative_deliverable": None, "control_data": {"primary_state": ["SCENE_CREATED", "SCENE_REVISED"], "flags": [], "handoffs": []}},
            "RT-MAL-03": {"creative_deliverable": None, "control_data": {"primary_state": "SCENE_CREATED — done", "flags": [], "handoffs": []}}
        }
        for case_id, output in cases.items():
            result = malformed_output(output, fixture_id="RT-SW-CREATE-01")
            assert result["runtime_failure_code"] == "MALFORMED_EXECUTOR_OUTPUT", (case_id, result)
        return "RT-MAL-01..03 rejected"
    results.append(run_case("RT-SW-18", malformed_primary_matrix))

    def unknown_flag():
        output = copy.deepcopy(FIXTURES["RT-SW-CREATE-01"]["output"])
        output["control_data"]["flags"] = ["UNLISTED_FLAG"]
        malformed_output(output)
        return "RT-MAL-04 rejected"
    results.append(run_case("RT-SW-19", unknown_flag))

    def display_suffix():
        output = copy.deepcopy(FIXTURES["RT-SW-CREATE-01"]["output"])
        output["control_data"]["primary_state"] = "SCENE_CREATED (done)"
        malformed_output(output)
        return "RT-MAL-05 rejected"
    results.append(run_case("RT-SW-20", display_suffix))

    def executor_unbound():
        runtime = SceneWriterRuntime()
        result = runtime.execute(base_input("UNBOUND-01", "RT-SW-CREATE-01"))
        assert result["runtime_status"] == "FAIL_SAFE" and result["runtime_failure_code"] == "EXECUTOR_UNBOUND", result
        return "unbound executor fail-safe"
    results.append(run_case("RT-SW-21", executor_unbound))

    def no_mock_fallback():
        runtime = SceneWriterRuntime()
        result = runtime.execute(base_input("NO-MOCK-01", "RT-SW-CREATE-01"))
        assert result["scene_writer"] is None and result["runtime_failure_code"] == "EXECUTOR_UNBOUND", result
        return "no fallback semantic output"
    results.append(run_case("RT-SW-22", no_mock_fallback))

    def duplicate_safety():
        runtime, executor = synthetic_runtime()
        first = runtime.execute(base_input("DUP-01", "RT-SW-CREATE-01"))
        second = runtime.execute(base_input("DUP-01", "RT-SW-CREATE-01"))
        conflict = base_input("DUP-01", "RT-SW-CREATE-01")
        conflict["scene_purpose"] = "different payload"
        third = runtime.execute(conflict)
        assert first["runtime_status"] == "SUCCESS" and second["idempotency"] == "DUPLICATE_REPLAY" and executor.calls == 1, (first, second, executor.calls)
        assert third["runtime_status"] == "CONTRACT_ERROR" and third["runtime_failure_code"] == "DUPLICATE_REQUEST_ID_CONFLICT", third
        return "replay without second executor call"
    results.append(run_case("RT-SW-23", duplicate_safety))

    def creative_control_separation():
        runtime, _ = synthetic_runtime()
        result = expect_success(runtime, "RT-SW-CREATE-01", "SEP-01")
        scene = result["scene_writer"]
        assert set(scene) == {"creative_deliverable", "control_data"} and "chain_of_thought" not in scene, scene
        return "separate creative/control channels"
    results.append(run_case("RT-SW-24", creative_control_separation))

    def no_chain_of_thought():
        output = copy.deepcopy(FIXTURES["RT-SW-CREATE-01"]["output"])
        output["chain_of_thought"] = "private reasoning"
        malformed_output(output)
        return "private reasoning field rejected"
    results.append(run_case("RT-SW-25", no_chain_of_thought))

    def revised_consistency():
        output = copy.deepcopy(FIXTURES["RT-SW-REVISE-01"]["output"])
        output["creative_deliverable"] = None
        malformed_output(output, fixture_id="RT-SW-REVISE-01")
        return "RT-MAL-06 rejected"
    results.append(run_case("RT-SW-26", revised_consistency))

    def nmc_consistency():
        output = copy.deepcopy(FIXTURES["RT-SW-NMC-01"]["output"])
        output["creative_deliverable"] = {"kind": "revision", "content": "synthetic contradiction"}
        output["control_data"]["material_rewrite_claimed"] = True
        malformed_output(output, fixture_id="RT-SW-NMC-01")
        return "RT-MAL-07 rejected"
    results.append(run_case("RT-SW-27", nmc_consistency))

    def handoff_schema():
        output = copy.deepcopy(FIXTURES["RT-SW-UP-01"]["output"])
        output["control_data"]["handoffs"] = [{"target_owner": "Showrunner"}]
        malformed_output(output, fixture_id="RT-SW-UP-01")
        return "RT-MAL-08 rejected"
    results.append(run_case("RT-SW-28", handoff_schema))

    def frozen_integrity():
        binding = SceneWriterRuntime().canonical_binding()
        assert binding["passed"] and binding["actual_sha256"] == "93e1be12988f8caa6cdd76acb5e6c1bf6ad3ca0dff5806a2ea93511e66052dfb", binding
        return "canonical Skill remains frozen"
    results.append(run_case("RT-SW-29", frozen_integrity))

    def synthetic_isolation():
        production = SceneWriterRuntime().registry_status()
        test, _ = synthetic_runtime()
        sandbox = test.registry_status()
        assert production["real_semantic_executor"] == "UNBOUND" and production["synthetic_executor"] == "NOT_PRESENT", production
        assert sandbox["real_semantic_executor"] == "UNBOUND" and sandbox["synthetic_executor"] == "ISOLATED_TEST_ONLY", sandbox
        return "synthetic executor never becomes a production executor"
    results.append(run_case("RT-SW-30", synthetic_isolation))

    payload = {"classification": "SYNTHETIC / NON-CANON / NON-SEMANTIC", "results": results, "passed": sum(item["result"] == "PASS" for item in results), "total": len(results)}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["passed"] == payload["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
