"""Provider-free support for Repair18 contract and recorded replay tests."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Mapping


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
RESEARCH = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research"
INTEGRATION = RESEARCH / "Integration_Contract_Repair_V0.1"
REPAIR_07 = RESEARCH / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1"
REPAIR_15 = RESEARCH / "E2E_Targeted_Repair_15_Mandatory_Preflight_Environment_Isolation_V0.1"
REPAIR_16 = RESEARCH / "E2E_Targeted_Repair_16_Scene_Writer_Per_Run_Strict_Scene_ID_Contract_Alignment_V0.1"
REPAIR_17 = RESEARCH / "E2E_Targeted_Repair_17_Scene_Writer_Per_Run_State_Field_Bridge_Generic_Contract_Cleanup_V0.1"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
PHASE2 = RESEARCH / "Systemic_Hardening_Phase_2_Runtime_Reliability_Regression_Enforcement_V0.1"
R22 = HARNESS / "evidence" / "E2E-RUN-22"

for item in (INTEGRATION / "implementation", REPAIR_07 / "implementation", HARNESS, AUTOMATION_ROOT):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from fixture_contract_compiler import compile_binding, compile_path
from integration_contract.semantic_alignment import (
    SemanticAlignmentContractError,
    build_entity_identity_projection,
    build_shared_transition_authority_projection,
    classify_transition_evidence,
    resolve_entity_identity,
    resolved_identity_match,
)
from integration_contract.semantic_safeguard import evaluate_semantic_safeguard
from integration_contract.state_ledger import E2EStateLedger


def binding(number: int) -> Path:
    return REPAIR_07 / "fixtures" / f"E2E_FIX_0{number}_Runtime_Binding_V0.1.json"


os.environ.setdefault("AFS_E2E_FIXTURE_BINDING", str(binding(2)))
import run_minimal_e2e as e2e


def compiled(number: int) -> Dict[str, Any]:
    return compile_path(binding(number))


def scene_matrix(contract: Mapping[str, Any], *, occurs: bool = True, token_scene: int | None = None) -> list[Dict[str, Any]]:
    fixture = contract["fixture"]
    dimension = fixture["state_dimensions"][0]
    from_state, to_state = dimension["allowed_tokens"]
    transition = fixture["authorized_transitions"][0]
    values = [from_state, to_state, to_state] if occurs else [from_state, from_state, from_state]
    scenes: list[Dict[str, Any]] = []
    for index, scene_id in enumerate(contract["scene_ids"], start=1):
        transitions = [transition] if token_scene is None or token_scene == index else []
        scenes.append(
            {
                "scene_id": scene_id,
                "evidence_locator": f"scene_packages/{scene_id}",
                "state_evidence": {
                    "entity_identity": fixture["tracked_entities"][0]["entity_id"],
                    dimension["dimension"]: values[index - 1],
                    "authorized_transitions": transitions,
                },
            }
        )
    return scenes


def identity_pair(contract: Mapping[str, Any], entity_index: int = 0):
    projection = build_entity_identity_projection(contract)
    entity = contract["fixture"]["tracked_entities"][entity_index]
    return (
        projection,
        resolve_entity_identity(projection, namespace="transport.entity_id", token=entity["entity_id"]),
        resolve_entity_identity(projection, namespace="assertion.identity_lock", token=entity["identity_lock"]),
    )


def r22_output() -> Dict[str, Any]:
    return json.loads((R22 / "artifacts" / "scene_writer_output.json").read_text(encoding="utf-8"))


def r22_tree_hash() -> str:
    rows = []
    for path in sorted((item for item in R22.rglob("*") if item.is_file()), key=lambda item: str(item).lower()):
        rows.append(f"{path.relative_to(R22).as_posix()} {hashlib.sha256(path.read_bytes()).hexdigest()}")
    return hashlib.sha256("\n".join(rows).encode("utf-8")).hexdigest()


def r22_replay() -> Dict[str, Any]:
    output = r22_output()
    scenes = output["scene_packages"]
    assertions = e2e.build_scene_assertions(scenes)
    envelope = json.loads((R22 / "envelopes" / "02_scene_writer_to_director.json").read_text(encoding="utf-8"))
    ledger = E2EStateLedger(run_id="E2E-RUN-22-RECORDED-REPLAY-REPAIR18")
    for scene in scenes:
        ledger.append(envelope=envelope, state_snapshot=copy.deepcopy(scene["state_evidence"]))
    report = evaluate_semantic_safeguard(
        envelope=envelope,
        ledger=ledger,
        creative_output=output["content"],
        assertions=assertions,
    )
    transition_assertion = next(item for item in assertions if item["id"] == "AUTHORIZED-TRANSITION")
    return {
        "integration_decision": report["integration_decision"],
        "findings": report["layer_a"]["findings"],
        "prop_assertions": [item for item in assertions if item["id"].startswith("PROP-")],
        "transition": transition_assertion["value"],
        "historical_status": "BLOCKED",
        "historical_status_preserved": True,
        "provider_calls": 0,
        "executor_calls": 0,
        "role_calls": 0,
        "probe_calls": 0,
        "live_e2e_runs": 0,
    }


def run_json(script: Path) -> tuple[int, Dict[str, Any]]:
    env = dict(os.environ)
    env["AFS_E2E_FIXTURE_BINDING"] = str(binding(2))
    for name in ("AFS_E2E_RUN_ID", "AFS_E2E_AUTHORIZATION_LABEL", "AFS_E2E_EVIDENCE_ROOT", "AFS_E2E_RECOVERY_OF"):
        env.pop(name, None)
    completed = subprocess.run(
        [sys.executable, "-X", "utf8", "-B", str(script)],
        cwd=str(AUTOMATION_ROOT),
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        payload = {"stdout": completed.stdout, "stderr": completed.stderr}
    return completed.returncode, payload


def synthetic_two_entity_contract() -> Dict[str, Any]:
    source = json.loads(binding(2).read_text(encoding="utf-8"))
    source["tracked_entities"].append(
        {
            "entity_id": "foreign_entity_token",
            "identity_lock": "foreign_identity_lock",
            "custody_required": True,
            "condition_lock": "foreign_condition",
        }
    )
    return compile_binding(source)
