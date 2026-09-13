"""One bounded real Scene Writer contract probe for E2E Targeted Repair 01.

This runner never invokes Showrunner or any downstream role. It consumes the
frozen Showrunner package from E2E-RUN-01-RECOVERY-01 and permits exactly one
Scene Writer Provider request after all offline gates pass.
"""

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
for import_path in (str(ROOT / "implementation"), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

import run_minimal_e2e as e2e
from integration_contract.semantic_safeguard import evaluate_semantic_safeguard
from integration_contract.state_ledger import E2EStateLedger
from scene_writer_integration_contract import STRUCTURAL_FIELD_NAMES, assess_scene_writer_integration_contract, frozen_contract_sources


PROBE_RUN_ID = "SW-CONTRACT-PROBE-01"
EVIDENCE_ROOT = Path(os.environ.get("AFS_SW_CONTRACT_PROBE_EVIDENCE_ROOT", str(ROOT / "evidence" / PROBE_RUN_ID)))
FROZEN_RECOVERY_ROOT = HARNESS_STAGE / "evidence" / "E2E-RUN-01-RECOVERY-01"
SHOWRUNNER_OUTPUT = FROZEN_RECOVERY_ROOT / "artifacts" / "showrunner_output.json"
SHOWRUNNER_ENVELOPE = FROZEN_RECOVERY_ROOT / "envelopes" / "01_showrunner_to_scene_writer.json"
PERSIST_TEST = ROOT / "tests" / "run_provider_response_persistence_tests.py"
CONTRACT_TEST = ROOT / "tests" / "run_scene_writer_integration_contract_tests.py"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_markdown(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def run_offline_suite(script: Path) -> Dict[str, Any]:
    result = subprocess.run([sys.executable, "-X", "utf8", str(script)], text=True, capture_output=True, encoding="utf-8", errors="replace", check=False)
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        payload = {"raw_stdout": result.stdout}
    return {"script": str(script), "returncode": result.returncode, "result": payload, "stderr": result.stderr}


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
            "source_attribution_contract": {
                "source_role": "Scene Writer",
                "source_record_id_pattern": f"{PROBE_RUN_ID}/scene_writer/<scene_id>",
                "version": "0.1",
                "evidence_locator_pattern": "scene_packages/<scene_id>",
            },
            "execution_boundary": "One CREATE-only contract probe. Do not call Showrunner, downstream roles, or a verifier.",
        },
    )


def acceptance(result: Mapping[str, Any], contract_report: Mapping[str, Any], safeguard: Mapping[str, Any]) -> Dict[str, Dict[str, str]]:
    scenes = result["scene_packages"]
    all_text = "\n".join(scene["content"] for scene in scenes)
    statuses = {
        "PROBE-01": len(scenes) == 3,
        "PROBE-02": bool(contract_report["state_token_gate"]["passed"]),
        "PROBE-03": all(all(isinstance(scene["structural_deliverable"].get(name), str) and scene["structural_deliverable"][name].strip() for name in STRUCTURAL_FIELD_NAMES) for scene in scenes),
        "PROBE-04": all(scene["state_evidence"]["key_identity"] == "A-17" for scene in scenes),
        "PROBE-05": all(isinstance(scene["state_evidence"]["key_custody"], str) and scene["state_evidence"]["key_custody"].strip() for scene in scenes),
        "PROBE-06": any(scene["state_evidence"]["reveal_status"] == "REVEALED_WITH_EVENT" for scene in scenes),
        "PROBE-07": not any(finding["code"] in {"KNOWLEDGE_TIMING_EARLY", "UNSUPPORTED_NEW_FACT"} for finding in safeguard["layer_a"]["findings"]),
        "PROBE-08": scenes[0]["state_evidence"]["clothing_visual_state_code"] == "soaked_uniform",
        "PROBE-09": "change_from_soaked_uniform" in scenes[-1]["state_evidence"]["authorized_transitions"],
        "PROBE-10": "完全和解" not in all_text and "RECONCILED" not in all_text.upper(),
        "PROBE-11": bool(contract_report["passed"]),
        "PROBE-12": safeguard["integration_decision"] == "PASS",
    }
    descriptions = {
        "PROBE-01": "exactly 3 scenes",
        "PROBE-02": "machine state exact tokens valid",
        "PROBE-03": "six frozen structural fields per scene",
        "PROBE-04": "A-17 retained",
        "PROBE-05": "custody retained",
        "PROBE-06": "knowledge timing event retained",
        "PROBE-07": "no premature storage-room knowledge finding",
        "PROBE-08": "soaked_uniform exact code present",
        "PROBE-09": "authorized clothing transition retained",
        "PROBE-10": "no unauthorized full reconciliation",
        "PROBE-11": "Structural Contract Gate PASS",
        "PROBE-12": "Integration Semantic Safeguard PASS",
    }
    return {key: {"result": "PASS" if value else "FAIL", "detail": descriptions[key]} for key, value in statuses.items()}


def render_report(manifest: Mapping[str, Any], probe_acceptance: Mapping[str, Mapping[str, str]] | None, failure: Mapping[str, str] | None) -> str:
    rows = [
        ("Run ID", manifest["run_id"]),
        ("Status", manifest["status"]),
        ("Provider / model", "DeepSeek / deepseek-v4-pro"),
        ("Provider calls", str(manifest["provider_call_count"])),
        ("Retries / fallback", "0 / 0"),
        ("Showrunner calls", "0"),
        ("Downstream role calls", "0"),
    ]
    lines = ["# AI Film Studio Scene Writer Real Contract Probe Report V0.1", "", "| Item | Result |", "| --- | --- |"]
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
        "authorization": "E2E Targeted Repair 01 — Scene Writer Integration Contract V0.1",
        "status": "PREFLIGHT",
        "started_at": utc_now(),
        "provider": "deepseek",
        "model": "deepseek-v4-pro",
        "provider_call_budget": 1,
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
        offline = {"persistence": run_offline_suite(PERSIST_TEST), "scene_writer_contract": run_offline_suite(CONTRACT_TEST)}
        preflight = e2e.static_preflight()
        write_json(EVIDENCE_ROOT / "preflight.json", {"offline": offline, "existing_preflight": preflight})
        if any(item["returncode"] != 0 for item in offline.values()):
            raise e2e.E2EBlocked("RUNTIME / HARNESS FAILURE", "Integration Harness", "Required offline contract gates did not pass")
        manifest["status"] = "RUNNING"
        showrunner_output = json.loads(SHOWRUNNER_OUTPUT.read_text(encoding="utf-8"))
        showrunner_envelope = json.loads(SHOWRUNNER_ENVELOPE.read_text(encoding="utf-8"))
        executor = e2e.CanonicalRoleExecutor(evidence_dir=EVIDENCE_ROOT, run_id=PROBE_RUN_ID)
        scene_writer = e2e.role_spec("scene_writer")
        result, input_path, output_path = executor.invoke(
            spec=scene_writer,
            input_payload=scene_writer_input(showrunner_output, showrunner_envelope),
            required_locks=showrunner_output["canon_assignment_locks"],
            prohibited_changes=showrunner_output["prohibited_changes"],
        )
        contract_report = assess_scene_writer_integration_contract(result, run_id=PROBE_RUN_ID)
        write_json(EVIDENCE_ROOT / "scene_writer_contract_gate.json", contract_report)
        scene_envelope = e2e.make_envelope(
            scene_writer,
            result,
            "Director",
            "Probe-only downstream handoff withheld",
            output_path,
            run_id=PROBE_RUN_ID,
        )
        provisional_ledger = E2EStateLedger(run_id=f"{PROBE_RUN_ID}-semantic-only")
        for scene in result["scene_packages"]:
            provisional_ledger.append(
                envelope=e2e.scene_envelope(scene, result, output_path, run_id=PROBE_RUN_ID),
                state_snapshot=e2e.scene_ledger_snapshot(scene),
            )
        safeguard = evaluate_semantic_safeguard(
            envelope=scene_envelope,
            ledger=provisional_ledger,
            creative_output=result["content"],
            assertions=e2e.build_scene_assertions(result["scene_packages"]),
            legacy_verifier_result=e2e.ABSENT,
            legacy_verifier_only=False,
        )
        write_json(EVIDENCE_ROOT / "semantic_safeguard.json", safeguard)
        probe_acceptance = acceptance(result, contract_report, safeguard)
        write_json(EVIDENCE_ROOT / "probe_acceptance.json", probe_acceptance)
        if not all(item["result"] == "PASS" for item in probe_acceptance.values()):
            raise e2e.E2EBlocked("SEMANTIC SAFEGUARD FAILURE", "Scene Writer Contract Probe", "Real probe acceptance is not 12/12 PASS")
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
        if failure is not None:
            write_json(EVIDENCE_ROOT / "failure_attribution.json", failure)
        write_markdown(EVIDENCE_ROOT / "AI_Film_Studio_Scene_Writer_Real_Contract_Probe_Report_V0.1.md", render_report(manifest, probe_acceptance, failure))
    summary = {"evidence_root": str(EVIDENCE_ROOT), "status": manifest["status"], "provider_call_count": manifest["provider_call_count"], "probe_acceptance": "NOT_REACHED" if probe_acceptance is None else f"{sum(item['result'] == 'PASS' for item in probe_acceptance.values())}/12"}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if manifest["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(run())
