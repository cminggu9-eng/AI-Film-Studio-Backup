"""Provider-free Repair 11 tests for exact strict transport lifecycle admission."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable, Mapping


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION / "runtime" / "_STAGING" / "_research"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
R13 = HARNESS / "evidence" / "E2E-RUN-13"
sys.path.insert(0, str(HARNESS))

from runtime_reliability_contract import STRICT_TRANSPORT_AUTHORIZATION_REGISTRY, validate_lifecycle_consistency  # noqa: E402
import run_minimal_e2e as e2e  # noqa: E402


def run_json(script: Path) -> tuple[int, Mapping[str, Any]]:
    completed = subprocess.run([sys.executable, "-X", "utf8", "-B", str(script)], cwd=str(AUTOMATION), capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        payload = {}
    return completed.returncode, payload if isinstance(payload, Mapping) else {}


def append(results: list[dict[str, str]], identifier: str, condition: bool, detail: str) -> None:
    results.append({"id": identifier, "result": "PASS" if condition else "FAIL", "detail": detail})


def lifecycle(manifest: Mapping[str, Any], provider: Mapping[str, Any], handoffs: list[Any], ledger: Mapping[str, Any]) -> Mapping[str, Any]:
    return validate_lifecycle_consistency(manifest=manifest, provider_manifest=provider, handoffs=handoffs, ledger=ledger, evidence_root=R13, require_complete_chain=True)


def strict_call(call: dict[str, Any], function_name: str) -> None:
    call["structured_transport"] = {
        "enabled": True,
        "function_name": function_name,
        "beta_provider_feature_used": True,
        "required_tool_call_verified": True,
        "arguments_parsed": True,
        "schema_validated": True,
    }


def main() -> int:
    manifest = json.loads((R13 / "execution_manifest.json").read_text(encoding="utf-8"))
    provider = json.loads((R13 / "provider_manifest.json").read_text(encoding="utf-8"))
    handoffs = json.loads((R13 / "handoff_trace.json").read_text(encoding="utf-8"))
    ledger = json.loads((R13 / "state_ledger.json").read_text(encoding="utf-8"))
    failure = json.loads((R13 / "failure_attribution.json").read_text(encoding="utf-8"))
    corrected = lifecycle(manifest, provider, handoffs, ledger)
    strict = {item["role"]: item for item in corrected["strict_transport_authorizations"]}
    calls = provider["calls"]
    results: list[dict[str, str]] = []

    phase2 = RESEARCH / "Systemic_Hardening_Phase_2_Runtime_Reliability_Regression_Enforcement_V0.1"
    sw_test = RESEARCH / "E2E_Targeted_Repair_03_Strict_Structured_Transport_V0.1" / "tests" / "run_scene_writer_strict_transport_tests.py"
    align_test = RESEARCH / "E2E_Targeted_Repair_09K_Director_State_Object_Contract_Implementation_V0.1" / "tests" / "run_director_state_object_phase2_regression.py"
    provider_free_test = RESEARCH / "Integration_Contract_Repair_V0.1" / "tests" / "run_provider_free_startup_test.py"
    generality_test = RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1" / "tests" / "run_fixture_generality_tests.py"
    sw_exit, sw_payload = run_json(sw_test)
    align_exit, align_payload = run_json(align_test)
    startup_exit, _ = run_json(provider_free_test)
    generality_exit, generality_payload = run_json(generality_test)
    phase2_source = (phase2 / "run_systemic_regression_gate.py").read_text(encoding="utf-8")
    lifecycle_source = (HARNESS / "runtime_reliability_contract.py").read_text(encoding="utf-8")
    probe04 = json.loads((RESEARCH / "Director_Strict_Compatibility_Probe_04_After_Repair_09F_V0.1" / "evidence" / "DIRECTOR-STRICT-COMPATIBILITY-PROBE-04" / "probe_manifest.json").read_text(encoding="utf-8"))

    append(results, "STRICT-LIFE-01", any("isolated to Scene Writer" in str(item.get("blocking_reason")) for item in failure), "old Scene Writer-only provenance is preserved in immutable R13 failure evidence")
    append(results, "STRICT-LIFE-02", "STRICT_TRANSPORT_AUTHORIZATION_REGISTRY" in lifecycle_source and "strict transport role/function pair is not explicitly authorized" in lifecycle_source, "new lifecycle invariant is represented by a closed registry")
    append(results, "STRICT-LIFE-03", STRICT_TRANSPORT_AUTHORIZATION_REGISTRY == {"Scene Writer": "submit_scene_writer_package", "Director": "submit_director_package"}, "registry contains exactly two approved pairs")
    append(results, "STRICT-LIFE-04", strict.get("Scene Writer", {}).get("authorized") is True and strict.get("Scene Writer", {}).get("function_name") == "submit_scene_writer_package", "Scene Writer exact pair is authorized")
    append(results, "STRICT-LIFE-05", strict.get("Director", {}).get("authorized") is True and strict.get("Director", {}).get("function_name") == "submit_director_package", "Director exact pair is authorized")
    append(results, "STRICT-LIFE-06", all(not item["structured_transport"]["enabled"] for item in calls if item["role"] not in STRICT_TRANSPORT_AUTHORIZATION_REGISTRY), "other five roles remain non-strict")
    append(results, "STRICT-LIFE-07", corrected["result"] == "PASS", "immutable E2E-RUN-13 recorded calls satisfy the corrected lifecycle gate")
    append(results, "STRICT-LIFE-08", all(item["strict"] is True for item in strict.values()), "strict:true lifecycle validation is preserved")
    append(results, "STRICT-LIFE-09", all(item["tool_choice_function_name"] == item["function_name"] for item in strict.values()), "exact tool choice remains bound to the declared function")
    append(results, "STRICT-LIFE-10", all(call["structured_transport"].get("beta_provider_feature_used") is True for call in calls if call["structured_transport"]["enabled"]) and "strict_beta_base_url" not in lifecycle_source, "provider strict mechanics remain adapter-scoped")
    append(results, "STRICT-LIFE-11", sw_exit == 0 and sw_payload.get("passed") == 15 and sw_payload.get("total") == 15, "Scene Writer strict schema regression passes")
    append(results, "STRICT-LIFE-12", align_exit == 0 and align_payload.get("passed") == 12 and align_payload.get("total") == 12 and probe04.get("result") == "PASS", "historical Probe 04 remains PASS while the current Director 09K object contract regression passes")
    append(results, "STRICT-LIFE-13", all(call.get("persistence_verified") is True for call in calls), "raw-first lifecycle evidence remains complete")
    append(results, "STRICT-LIFE-14", len(STRICT_TRANSPORT_AUTHORIZATION_REGISTRY) == 2 and all("*" not in key and "*" not in value for key, value in STRICT_TRANSPORT_AUTHORIZATION_REGISTRY.items()), "registry has no wildcard authorization")
    append(results, "STRICT-LIFE-15", startup_exit == 0, "Provider-Free Startup passes")
    append(results, "STRICT-LIFE-16", generality_exit == 0 and generality_payload.get("passed") == 18 and generality_payload.get("total") == 18, "GEN-01 through GEN-18 pass")
    append(results, "STRICT-LIFE-17", 'suite("STRICT-LIFE"' in phase2_source and ", 30," in phase2_source, "Unified Phase 2 gate registers the strict lifecycle suite")
    append(results, "STRICT-LIFE-18", e2e.canonical_skill_hashes() == e2e.EXPECTED_HASHES, "seven canonical Skill hashes remain unchanged")

    def rejects(mutator: Callable[[dict[str, Any]], None]) -> bool:
        candidate = copy.deepcopy(provider)
        mutator(candidate)
        return lifecycle(manifest, candidate, handoffs, ledger)["result"] == "FAIL"

    for identifier, role in (
        ("STRICT-LIFE-NEG-01", "Showrunner"), ("STRICT-LIFE-NEG-02", "Character & Acting"),
        ("STRICT-LIFE-NEG-03", "Art Director"), ("STRICT-LIFE-NEG-04", "Continuity"),
        ("STRICT-LIFE-NEG-05", "Shared QA"),
    ):
        append(results, identifier, rejects(lambda candidate, role=role: strict_call(next(item for item in candidate["calls"] if item["role"] == role), "submit_director_package")), f"{role} strict transport is rejected")
    append(results, "STRICT-LIFE-NEG-06", rejects(lambda candidate: strict_call(next(item for item in candidate["calls"] if item["role"] == "Scene Writer"), "submit_director_package")), "Scene Writer plus Director function is rejected")
    append(results, "STRICT-LIFE-NEG-07", rejects(lambda candidate: strict_call(next(item for item in candidate["calls"] if item["role"] == "Director"), "submit_scene_writer_package")), "Director plus Scene Writer function is rejected")
    append(results, "STRICT-LIFE-NEG-08", rejects(lambda candidate: strict_call(next(item for item in candidate["calls"] if item["role"] == "Director"), "submit_unknown_package")), "authorized role plus unknown function is rejected")
    append(results, "STRICT-LIFE-NEG-09", rejects(lambda candidate: (next(item for item in candidate["calls"] if item["role"] == "Showrunner").__setitem__("role", "Unknown Role"), strict_call(next(item for item in candidate["calls"] if item["role"] == "Unknown Role"), "submit_director_package"))), "unknown role plus authorized function is rejected")
    append(results, "STRICT-LIFE-NEG-10", rejects(lambda candidate: next(item for item in candidate["calls"] if item["role"] == "Director")["structured_transport"].__setitem__("enabled", False)), "strict:false on an authorized strict pair is rejected")
    append(results, "STRICT-LIFE-NEG-11", rejects(lambda candidate: next(item for item in candidate["calls"] if item["role"] == "Director")["structured_transport"].__setitem__("tool_choice_function_name", "submit_scene_writer_package")), "tool choice mismatch is rejected")
    append(results, "STRICT-LIFE-NEG-12", rejects(lambda candidate: next(item for item in candidate["calls"] if item["role"] == "Director")["structured_transport"].__setitem__("beta_provider_feature_used", False)), "provider strict mechanics outside adapter scope are rejected")

    passed = sum(item["result"] == "PASS" for item in results)
    print(json.dumps({"classification": "STRICT TRANSPORT LIFECYCLE AUTHORIZATION", "results": results, "passed": passed, "total": len(results), "provider_calls": 0, "executor_calls": 0, "role_calls": 0, "real_e2e_runs": 0}, ensure_ascii=False, indent=2))
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
