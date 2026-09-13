"""One bounded Scene Writer contract probe for E2E Targeted Repair 02."""

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
for import_path in (str(ROOT / "implementation"), str(REPAIR_01 / "implementation"), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

import run_minimal_e2e as e2e
from integration_contract.semantic_safeguard import evaluate_semantic_safeguard
from integration_contract.state_ledger import E2EStateLedger
from scene_writer_integration_contract import STRUCTURAL_FIELD_NAMES, assess_scene_writer_integration_contract, frozen_contract_sources
from scene_writer_response_budget import SELECTED_COMPLETION_BUDGET, scene_writer_response_budget_preflight


PROBE_RUN_ID = "SW-CONTRACT-PROBE-02"
EVIDENCE_ROOT = Path(os.environ.get("AFS_SW_CONTRACT_PROBE_02_EVIDENCE_ROOT", str(ROOT / "evidence" / PROBE_RUN_ID)))
FROZEN_RECOVERY_ROOT = HARNESS_STAGE / "evidence" / "E2E-RUN-01-RECOVERY-01"
SHOWRUNNER_OUTPUT = FROZEN_RECOVERY_ROOT / "artifacts" / "showrunner_output.json"
SHOWRUNNER_ENVELOPE = FROZEN_RECOVERY_ROOT / "envelopes" / "01_showrunner_to_scene_writer.json"
PERSIST_TEST = REPAIR_01 / "tests" / "run_provider_response_persistence_tests.py"
CONTRACT_TEST = REPAIR_01 / "tests" / "run_scene_writer_integration_contract_tests.py"
SERIALIZATION_TEST = ROOT / "tests" / "run_scene_writer_serialization_tests.py"
TRUNCATION_TEST = ROOT / "tests" / "run_scene_writer_truncation_detection_tests.py"
BUDGET_PREFLIGHT_TEST = ROOT / "tests" / "run_scene_writer_response_budget_preflight.py"


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
            "execution_boundary": "One CREATE-only contract probe. Do not call Showrunner, downstream roles, or a verifier.",
        },
    )


def acceptance(result: Mapping[str, Any], contract: Mapping[str, Any], safeguard: Mapping[str, Any], call_record: Mapping[str, Any]) -> Dict[str, Dict[str, str]]:
    scenes = result["scene_packages"]
    all_text = "\n".join(scene["content"] for scene in scenes)
    truncation = call_record.get("truncation_assessment", {})
    statuses = {
        "PROBE-02-A": call_record.get("provider_success") is True and truncation.get("truncated") is False,
        "PROBE-02-B": truncation.get("json_complete") is True,
        "PROBE-02-C": len(scenes) == 3,
        "PROBE-02-D": all(all(isinstance(scene["structural_deliverable"].get(name), str) and scene["structural_deliverable"][name].strip() for name in STRUCTURAL_FIELD_NAMES) for scene in scenes),
        "PROBE-02-E": contract["state_token_gate"]["passed"],
        "PROBE-02-F": scenes[0]["state_evidence"]["clothing_visual_state_code"] == "soaked_uniform",
        "PROBE-02-G": all(scene["state_evidence"]["key_identity"] == "A-17" for scene in scenes),
        "PROBE-02-H": all(isinstance(scene["state_evidence"]["key_custody"], str) and scene["state_evidence"]["key_custody"].strip() for scene in scenes),
        "PROBE-02-I": not any(finding["code"] == "KNOWLEDGE_TIMING_EARLY" for finding in safeguard["layer_a"]["findings"]),
        "PROBE-02-J": "change_from_soaked_uniform" in scenes[-1]["state_evidence"]["authorized_transitions"],
        "PROBE-02-K": "完全和解" not in all_text and "RECONCILED" not in all_text.upper(),
        "PROBE-02-L": contract["structural_gate"]["passed"],
        "PROBE-02-M": contract["state_token_gate"]["passed"],
        "PROBE-02-N": safeguard["integration_decision"] == "PASS",
    }
    descriptions = {
        "PROBE-02-A": "provider response complete / not truncated",
        "PROBE-02-B": "valid JSON parse",
        "PROBE-02-C": "three scenes complete",
        "PROBE-02-D": "six structural items present",
        "PROBE-02-E": "machine state token valid",
        "PROBE-02-F": "soaked_uniform exact location",
        "PROBE-02-G": "A-17 retained",
        "PROBE-02-H": "custody retained",
        "PROBE-02-I": "knowledge timing retained",
        "PROBE-02-J": "authorized clothing transition retained",
        "PROBE-02-K": "no unauthorized reconciliation",
        "PROBE-02-L": "Structural Contract Gate PASS",
        "PROBE-02-M": "State Token Gate PASS",
        "PROBE-02-N": "Semantic Safeguard PASS",
    }
    return {key: {"result": "PASS" if value else "FAIL", "detail": descriptions[key]} for key, value in statuses.items()}


def cost_size_report(call_record: Mapping[str, Any] | None) -> Dict[str, Any]:
    if not isinstance(call_record, Mapping):
        return {"provider_call_executed": False}
    usage_record = call_record.get("usage")
    usage = usage_record.get("usage") if isinstance(usage_record, Mapping) and isinstance(usage_record.get("usage"), Mapping) else {}
    budget = call_record.get("selected_completion_budget")
    completion = usage.get("completion_tokens")
    return {
        "provider_call_executed": True,
        "input_tokens": usage.get("prompt_tokens"),
        "completion_tokens": completion,
        "total_tokens": usage.get("total_tokens"),
        "selected_completion_budget": budget,
        "actual_utilization_ratio": round(completion / budget, 6) if isinstance(completion, int) and isinstance(budget, int) and budget else None,
        "finish_reason": call_record.get("provider_finish_reason") or (usage_record.get("finish_reason") if isinstance(usage_record, Mapping) else None),
        "response_characters": call_record.get("response_characters"),
        "response_utf8_bytes": call_record.get("response_utf8_bytes"),
        "provider_cost_cny": call_record.get("estimated_cost_cny"),
        "truncation_assessment": call_record.get("truncation_assessment"),
    }


def render_report(manifest: Mapping[str, Any], probe_acceptance: Mapping[str, Mapping[str, str]] | None, failure: Mapping[str, str] | None) -> str:
    lines = ["# AI Film Studio Scene Writer Real Contract Probe 02 Report V0.1", "", "| Item | Result |", "| --- | --- |"]
    rows = (("Run ID", manifest["run_id"]), ("Status", manifest["status"]), ("Provider / model", "DeepSeek / deepseek-v4-pro"), ("Selected completion budget", str(manifest["selected_completion_budget"])), ("Provider calls", str(manifest["provider_call_count"])), ("Retries / fallback", "0 / 0"), ("Showrunner calls", "0"), ("Downstream calls", "0"))
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
    budget_preflight = scene_writer_response_budget_preflight()
    manifest: Dict[str, Any] = {
        "run_id": PROBE_RUN_ID,
        "authorization": "E2E Targeted Repair 02 — Scene Writer Response Budget & Serialization V0.1",
        "status": "PREFLIGHT",
        "started_at": utc_now(),
        "provider": "deepseek",
        "model": "deepseek-v4-pro",
        "provider_call_budget": 1,
        "selected_completion_budget": SELECTED_COMPLETION_BUDGET,
        "response_budget_preflight": budget_preflight,
        "retry_count": 0,
        "automatic_fallback": 0,
        "showrunner_real_calls": 0,
        "downstream_role_calls": 0,
        "provider_call_count": 0,
        "frozen_showrunner_artifact": str(SHOWRUNNER_OUTPUT),
        "frozen_showrunner_artifact_sha256": hashlib.sha256(SHOWRUNNER_OUTPUT.read_bytes()).hexdigest() if SHOWRUNNER_OUTPUT.is_file() else None,
    }
    failure: Dict[str, str] | None = None
    probe_acceptance: Dict[str, Dict[str, str]] | None = None
    executor: e2e.CanonicalRoleExecutor | None = None
    try:
        if not SHOWRUNNER_OUTPUT.is_file() or not SHOWRUNNER_ENVELOPE.is_file():
            raise e2e.E2EBlocked("RUNTIME / HARNESS FAILURE", "Integration Harness", "Frozen passed Showrunner package is unavailable")
        offline = {
            "persistence": run_offline_suite(PERSIST_TEST),
            "scene_writer_contract": run_offline_suite(CONTRACT_TEST),
            "serialization": run_offline_suite(SERIALIZATION_TEST),
            "truncation_detection": run_offline_suite(TRUNCATION_TEST),
            "budget_preflight": run_offline_suite(BUDGET_PREFLIGHT_TEST),
        }
        static = e2e.static_preflight()
        write_json(EVIDENCE_ROOT / "preflight.json", {"offline": offline, "static": static, "response_budget_preflight": budget_preflight})
        if not budget_preflight["passed"] or any(item["returncode"] != 0 for item in offline.values()):
            raise e2e.E2EBlocked("EXECUTOR / RESPONSE-BUDGET FAILURE", "Scene Writer", "Budget or required offline gates did not pass")
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
            raise e2e.E2EBlocked("SEMANTIC SAFEGUARD FAILURE", "Scene Writer Contract Probe", "Real probe acceptance is not 14/14 PASS")
        manifest["status"] = "PASS"
    except e2e.E2EBlocked as exc:
        manifest["status"] = "BLOCKED"
        failure = {"category": exc.category, "owner": exc.owner, "detail": exc.detail}
    except Exception as exc:
        manifest["status"] = "BLOCKED"
        failure = {"category": "RUNTIME / HARNESS FAILURE", "owner": "Integration Harness", "detail": f"{type(exc).__name__}: {exc}"}
    finally:
        manifest["completed_at"] = utc_now()
        manifest["provider_call_count"] = len(executor.call_records) if executor is not None else 0
        manifest["provider_calls"] = executor.call_records if executor is not None else []
        write_json(EVIDENCE_ROOT / "execution_manifest.json", manifest)
        write_json(EVIDENCE_ROOT / "probe_cost_size.json", cost_size_report(executor.call_records[0] if executor is not None and executor.call_records else None))
        if failure is not None:
            write_json(EVIDENCE_ROOT / "failure_attribution.json", failure)
        write_markdown(EVIDENCE_ROOT / "AI_Film_Studio_Scene_Writer_Real_Contract_Probe_02_Report_V0.1.md", render_report(manifest, probe_acceptance, failure))
    passed = sum(item["result"] == "PASS" for item in probe_acceptance.values()) if probe_acceptance is not None else 0
    print(json.dumps({"evidence_root": str(EVIDENCE_ROOT), "status": manifest["status"], "provider_call_count": manifest["provider_call_count"], "probe_acceptance": f"{passed}/14" if probe_acceptance is not None else "NOT_REACHED"}, ensure_ascii=False, indent=2))
    return 0 if manifest["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(run())

