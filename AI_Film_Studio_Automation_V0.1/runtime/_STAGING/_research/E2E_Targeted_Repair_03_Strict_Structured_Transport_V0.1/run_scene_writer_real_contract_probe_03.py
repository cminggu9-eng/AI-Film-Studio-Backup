"""One authorized strict-function Scene Writer Probe 03; no retries or fallback."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Mapping


ROOT = Path(__file__).resolve().parent
AUTOMATION_ROOT = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
HARNESS_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
REPAIR_01 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1"
REPAIR_02 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_02_Scene_Writer_Response_Budget_Serialization_V0.1"
for import_path in (str(ROOT / "implementation"), str(REPAIR_02 / "implementation"), str(REPAIR_01 / "implementation"), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

import run_minimal_e2e as e2e
from integration_contract.semantic_safeguard import evaluate_semantic_safeguard
from integration_contract.state_ledger import E2EStateLedger
from scene_writer_integration_contract import STRUCTURAL_FIELD_NAMES, assess_scene_writer_integration_contract, frozen_contract_sources
from scene_writer_response_budget import SELECTED_COMPLETION_BUDGET
from scene_writer_strict_transport import FUNCTION_NAME, build_structured_output_contract, schema_contract_coverage, validate_provider_strict_schema, validate_strict_scene_writer_arguments


PROBE_RUN_ID = "SW-CONTRACT-PROBE-03"
EVIDENCE_ROOT = Path(os.environ.get("AFS_SW_CONTRACT_PROBE_03_EVIDENCE_ROOT", str(ROOT / "evidence" / PROBE_RUN_ID)))
FROZEN_RECOVERY_ROOT = HARNESS_STAGE / "evidence" / "E2E-RUN-01-RECOVERY-01"
SHOWRUNNER_OUTPUT = FROZEN_RECOVERY_ROOT / "artifacts" / "showrunner_output.json"
SHOWRUNNER_ENVELOPE = FROZEN_RECOVERY_ROOT / "envelopes" / "01_showrunner_to_scene_writer.json"
STRICT_TEST = ROOT / "tests" / "run_scene_writer_strict_transport_tests.py"
REGRESSION_TEST = ROOT / "tests" / "run_scene_writer_probe02_serialization_regression.py"
PREFLIGHT_TEST = ROOT / "tests" / "run_scene_writer_strict_transport_preflight.py"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_markdown(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def run_offline_suite(script: Path) -> Dict[str, Any]:
    completed = subprocess.run([sys.executable, "-X", "utf8", "-B", str(script)], text=True, capture_output=True, encoding="utf-8", errors="replace", check=False)
    try:
        result: Dict[str, Any] = json.loads(completed.stdout)
    except json.JSONDecodeError:
        result = {"raw_stdout": completed.stdout}
    return {"script": str(script), "returncode": completed.returncode, "result": result, "stderr": completed.stderr}


def scene_writer_input(showrunner_output: Mapping[str, Any], showrunner_envelope: Mapping[str, Any]) -> Dict[str, Any]:
    fixture = e2e.fixture_constraints()
    return e2e.downstream_input(
        upstream_artifacts={"showrunner": showrunner_output},
        envelopes={"showrunner": showrunner_envelope},
        ledger=None,
        role_constraints={
            "mode": "CREATE",
            "scene_count": 3,
            "fixture_constraints": fixture["execution_constraints"],
            "scene_writer_integration_contract": frozen_contract_sources(),
            "response_budget_contract": {
                "classification": "LARGE_STRUCTURED_DELIVERABLE",
                "selected_completion_budget": SELECTED_COMPLETION_BUDGET,
                "compact_serialization": "scene-writer-integration-compact-v0.1",
                "no_retry": True,
                "no_fallback": True,
            },
            "strict_structured_transport": {
                "function": FUNCTION_NAME,
                "response_format_route": "PROHIBITED",
                "no_manual_json_escaping": True,
                "no_auto_repair": True,
            },
            "execution_boundary": "One CREATE-only strict-function contract probe. Do not call Showrunner, downstream roles, or a verifier.",
        },
    )


def acceptance(result: Mapping[str, Any], contract: Mapping[str, Any], safeguard: Mapping[str, Any], call_record: Mapping[str, Any]) -> Dict[str, Dict[str, str]]:
    scenes = result["scene_packages"]
    all_text = "\n".join(scene["content"] for scene in scenes)
    transport = call_record.get("structured_transport") if isinstance(call_record.get("structured_transport"), Mapping) else {}
    statuses = {
        "PROBE-03-01": transport.get("required_tool_call_verified") is True and transport.get("function_name") == FUNCTION_NAME,
        "PROBE-03-02": transport.get("arguments_parsed") is True,
        "PROBE-03-03": transport.get("schema_validated") is True,
        "PROBE-03-04": len(scenes) == 3,
        "PROBE-03-05": all(all(isinstance(scene["structural_deliverable"].get(name), str) and scene["structural_deliverable"][name].strip() for name in STRUCTURAL_FIELD_NAMES) for scene in scenes),
        "PROBE-03-06": contract["state_token_gate"]["passed"],
        "PROBE-03-07": scenes[0]["state_evidence"]["clothing_visual_state_code"] == "soaked_uniform",
        "PROBE-03-08": all(scene["state_evidence"]["key_identity"] == "A-17" for scene in scenes),
        "PROBE-03-09": all(isinstance(scene["state_evidence"]["key_custody"], str) and scene["state_evidence"]["key_custody"].strip() for scene in scenes),
        "PROBE-03-10": not any(finding["code"] == "KNOWLEDGE_TIMING_EARLY" for finding in safeguard["layer_a"]["findings"]),
        "PROBE-03-11": "change_from_soaked_uniform" in scenes[-1]["state_evidence"]["authorized_transitions"],
        "PROBE-03-12": "完全和解" not in all_text and "RECONCILED" not in all_text.upper(),
        "PROBE-03-13": contract["structural_gate"]["passed"],
        "PROBE-03-14": contract["state_token_gate"]["passed"],
        "PROBE-03-15": safeguard["integration_decision"] == "PASS",
        "PROBE-03-16": call_record.get("persistence_verified") is True,
        "PROBE-03-17": call_record.get("transport_auto_repairs") == 0,
    }
    details = {
        "PROBE-03-01": "one required strict function call received",
        "PROBE-03-02": "arguments parsed without tolerant parsing",
        "PROBE-03-03": "arguments pass the strict function schema",
        "PROBE-03-04": "three scenes complete",
        "PROBE-03-05": "six structural fields complete per scene",
        "PROBE-03-06": "machine state codes valid",
        "PROBE-03-07": "soaked_uniform exact",
        "PROBE-03-08": "A-17 retained",
        "PROBE-03-09": "custody retained",
        "PROBE-03-10": "knowledge timing retained",
        "PROBE-03-11": "authorized clothing transition retained",
        "PROBE-03-12": "no unauthorized reconciliation",
        "PROBE-03-13": "Structural Contract Gate PASS",
        "PROBE-03-14": "State Token Gate PASS",
        "PROBE-03-15": "Semantic Safeguard PASS",
        "PROBE-03-16": "raw response and usage persisted before validation",
        "PROBE-03-17": "no transport auto-repair",
    }
    return {key: {"result": "PASS" if value else "FAIL", "detail": details[key]} for key, value in statuses.items()}


def classify_failure(exc: e2e.E2EBlocked) -> Dict[str, str]:
    category = exc.category
    if category in {"PROVIDER STRICT-MODE FAILURE", "TOOL-CALL SERIALIZATION FAILURE", "SCHEMA VALIDATION FAILURE", "ROLE STRUCTURAL FAILURE", "ROLE STATE FAILURE", "SEMANTIC SAFEGUARD FAILURE", "HARNESS FAILURE"}:
        return {"category": category, "owner": exc.owner, "detail": exc.detail}
    detail_upper = exc.detail.upper()
    if "STATE TOKEN" in detail_upper or "_TOKEN" in detail_upper or "REVEAL" in detail_upper:
        category = "ROLE STATE FAILURE"
    elif "STRUCTURAL" in detail_upper or "SCENE_PACKAGE" in detail_upper or "COMPACT SERIALIZATION" in detail_upper:
        category = "ROLE STRUCTURAL FAILURE"
    elif category.startswith("RUNTIME"):
        category = "HARNESS FAILURE"
    else:
        category = "HARNESS FAILURE"
    return {"category": category, "owner": exc.owner, "detail": exc.detail}


def render_report(manifest: Mapping[str, Any], probe_acceptance: Mapping[str, Mapping[str, str]] | None, failure: Mapping[str, str] | None) -> str:
    lines = ["# AI Film Studio Scene Writer Real Contract Probe 03 Report V0.1", "", "| Item | Result |", "| --- | --- |"]
    rows = (("Run ID", manifest["run_id"]), ("Status", manifest["status"]), ("Provider / model", "DeepSeek / deepseek-v4-pro"), ("Transport", f"strict function `{FUNCTION_NAME}`"), ("Beta feature", "YES; isolated adapter path"), ("Provider calls", str(manifest["provider_call_count"])), ("Retries / fallback", "0 / 0"), ("Showrunner calls", "0"), ("Downstream calls", "0"))
    lines.extend(f"| {label} | {value} |" for label, value in rows)
    if probe_acceptance is not None:
        lines.extend(["", "## Probe Acceptance", "", "| Test | Result | Detail |", "| --- | --- | --- |"])
        lines.extend(f"| {test_id} | {item['result']} | {item['detail']} |" for test_id, item in probe_acceptance.items())
    if failure is not None:
        lines.extend(["", "## Safe Stop", "", f"- Category: `{failure['category']}`", f"- Owner: `{failure['owner']}`", f"- Detail: {failure['detail']}"])
    lines.append("")
    return "\n".join(lines)


def run() -> int:
    if EVIDENCE_ROOT.exists():
        raise RuntimeError(f"Refusing to overwrite existing probe evidence: {EVIDENCE_ROOT}")
    EVIDENCE_ROOT.mkdir(parents=True)
    manifest: Dict[str, Any] = {
        "run_id": PROBE_RUN_ID,
        "authorization": "E2E Targeted Repair 03 — Scene Writer Strict Structured Transport V0.1",
        "status": "PREFLIGHT",
        "started_at": utc_now(),
        "provider": "deepseek",
        "model": "deepseek-v4-pro",
        "transport": "strict_function",
        "function_name": FUNCTION_NAME,
        "BETA_PROVIDER_FEATURE_USED": "YES",
        "provider_call_budget": 1,
        "selected_completion_budget": SELECTED_COMPLETION_BUDGET,
        "retry_count": 0,
        "automatic_fallback": 0,
        "showrunner_real_calls": 0,
        "downstream_role_calls": 0,
        "full_e2e_reruns": 0,
        "json_auto_repairs": 0,
        "provider_call_count": 0,
        "frozen_showrunner_artifact": str(SHOWRUNNER_OUTPUT),
        "frozen_showrunner_artifact_sha256": hashlib.sha256(SHOWRUNNER_OUTPUT.read_bytes()).hexdigest() if SHOWRUNNER_OUTPUT.is_file() else None,
    }
    failure: Dict[str, str] | None = None
    probe_acceptance: Dict[str, Dict[str, str]] | None = None
    executor: e2e.CanonicalRoleExecutor | None = None
    try:
        if not SHOWRUNNER_OUTPUT.is_file() or not SHOWRUNNER_ENVELOPE.is_file():
            raise e2e.E2EBlocked("HARNESS FAILURE", "Integration Harness", "Frozen passed Showrunner recovery package is unavailable")
        offline = {
            "strict_01_to_15": run_offline_suite(STRICT_TEST),
            "probe_02_regression": run_offline_suite(REGRESSION_TEST),
            "provider_free_preflight": run_offline_suite(PREFLIGHT_TEST),
        }
        capability = validate_provider_strict_schema()
        static = e2e.static_preflight()
        write_json(EVIDENCE_ROOT / "preflight.json", {"offline": offline, "schema_capability": capability, "schema_coverage": schema_contract_coverage(), "static": static})
        if any(item["returncode"] != 0 for item in offline.values()) or not capability["passed"]:
            raise e2e.E2EBlocked("HARNESS FAILURE", "Scene Writer", "Strict transport preflight did not pass")
        manifest["status"] = "RUNNING"
        showrunner_output = json.loads(SHOWRUNNER_OUTPUT.read_text(encoding="utf-8"))
        showrunner_envelope = json.loads(SHOWRUNNER_ENVELOPE.read_text(encoding="utf-8"))
        executor = e2e.CanonicalRoleExecutor(evidence_dir=EVIDENCE_ROOT, run_id=PROBE_RUN_ID)
        scene_writer = e2e.role_spec("scene_writer")
        result, _, output_path = executor.invoke(
            spec=scene_writer,
            input_payload=scene_writer_input(showrunner_output, showrunner_envelope),
            required_locks=showrunner_output["canon_assignment_locks"],
            prohibited_changes=showrunner_output["prohibited_changes"],
            completion_budget=SELECTED_COMPLETION_BUDGET,
            structured_output=build_structured_output_contract(),
            structured_arguments_validator=validate_strict_scene_writer_arguments,
        )
        contract = assess_scene_writer_integration_contract(result, run_id=PROBE_RUN_ID)
        write_json(EVIDENCE_ROOT / "scene_writer_contract_gate.json", contract)
        scene_envelope = e2e.make_envelope(scene_writer, result, "Director", "Probe-only downstream handoff withheld", output_path, run_id=PROBE_RUN_ID)
        ledger = E2EStateLedger(run_id=f"{PROBE_RUN_ID}-semantic-only")
        for scene in result["scene_packages"]:
            ledger.append(envelope=e2e.scene_envelope(scene, result, output_path, run_id=PROBE_RUN_ID), state_snapshot=e2e.scene_ledger_snapshot(scene))
        safeguard = evaluate_semantic_safeguard(envelope=scene_envelope, ledger=ledger, creative_output=result["content"], assertions=e2e.build_scene_assertions(result["scene_packages"]), legacy_verifier_result=e2e.ABSENT, legacy_verifier_only=False)
        write_json(EVIDENCE_ROOT / "semantic_safeguard.json", safeguard)
        probe_acceptance = acceptance(result, contract, safeguard, executor.call_records[0])
        write_json(EVIDENCE_ROOT / "probe_acceptance.json", probe_acceptance)
        if not all(item["result"] == "PASS" for item in probe_acceptance.values()):
            raise e2e.E2EBlocked("SEMANTIC SAFEGUARD FAILURE", "Scene Writer Contract Probe", "Real probe acceptance is not 17/17 PASS")
        manifest["status"] = "PASS"
    except e2e.E2EBlocked as exc:
        manifest["status"] = "BLOCKED"
        failure = classify_failure(exc)
    except Exception as exc:
        manifest["status"] = "BLOCKED"
        failure = {"category": "HARNESS FAILURE", "owner": "Integration Harness", "detail": f"{type(exc).__name__}: {exc}"}
    finally:
        manifest["completed_at"] = utc_now()
        manifest["provider_call_count"] = len(executor.call_records) if executor is not None else 0
        manifest["provider_calls"] = executor.call_records if executor is not None else []
        write_json(EVIDENCE_ROOT / "execution_manifest.json", manifest)
        if failure is not None:
            write_json(EVIDENCE_ROOT / "failure_attribution.json", failure)
        write_markdown(EVIDENCE_ROOT / "AI_Film_Studio_Scene_Writer_Real_Contract_Probe_03_Report_V0.1.md", render_report(manifest, probe_acceptance, failure))
    passed = sum(item["result"] == "PASS" for item in probe_acceptance.values()) if probe_acceptance is not None else 0
    print(json.dumps({"evidence_root": str(EVIDENCE_ROOT), "status": manifest["status"], "provider_call_count": manifest["provider_call_count"], "probe_acceptance": f"{passed}/17" if probe_acceptance is not None else "NOT_REACHED"}, ensure_ascii=False, indent=2))
    return 0 if manifest["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(run())
