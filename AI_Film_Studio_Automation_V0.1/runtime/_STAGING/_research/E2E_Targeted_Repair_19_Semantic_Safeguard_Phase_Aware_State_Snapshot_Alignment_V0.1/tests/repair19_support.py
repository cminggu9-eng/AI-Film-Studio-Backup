"""Provider-free helpers for Repair19 phase-aware state snapshot tests."""

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
REPAIR_18 = RESEARCH / "E2E_Targeted_Repair_18_Semantic_Safeguard_Identity_Representation_Transition_Evidence_Alignment_V0.1"
HARNESS = RESEARCH / "Minimal_E2E_Runtime_Validation_V0.1"
PHASE2 = RESEARCH / "Systemic_Hardening_Phase_2_Runtime_Reliability_Regression_Enforcement_V0.1"
R24 = HARNESS / "evidence" / "E2E-RUN-24"
# SHA-256 of the R24 manifest joined with actual LF bytes.  This mirrors the
# integrity algorithm below; a textual "\\n" separator is deliberately not used.
R24_TREE_BASELINE = "81732b599c679c9b4d90b552a07f308fad47fb63c31920e04f2378826f8c8461"
R24_RAW_BASELINE = "2775b1243389142e662408a0aef551cd616e52c9fbb3eb5a5bb2aa62a10c7e13"

for item in (INTEGRATION / "implementation", REPAIR_07 / "implementation", HARNESS, AUTOMATION_ROOT):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from fixture_contract_compiler import compile_path
from integration_contract.semantic_alignment import build_shared_transition_authority_projection, classify_transition_evidence
from integration_contract.semantic_safeguard import evaluate_semantic_safeguard
from integration_contract.state_ledger import E2EStateLedger
from integration_contract.state_phase import (
    StatePhaseContractError,
    build_state_phase_projection,
    build_phase_scoped_required_state_value,
    resolve_state_phase_snapshot,
)


def binding(number: int) -> Path:
    return REPAIR_07 / "fixtures" / f"E2E_FIX_0{number}_Runtime_Binding_V0.1.json"


os.environ.setdefault("AFS_E2E_FIXTURE_BINDING", str(binding(3)))
import run_minimal_e2e as e2e


def compiled(number: int) -> Dict[str, Any]:
    return compile_path(binding(number))


def scenes_for(contract: Mapping[str, Any], *, transition_scene: int | None) -> list[Dict[str, Any]]:
    fixture = contract["fixture"]
    dimension = fixture["state_dimensions"][0]
    transition = fixture["authorized_transitions"][0]
    from_state, to_state = dimension["allowed_tokens"]
    scenes: list[Dict[str, Any]] = []
    transitioned = False
    for index, scene_id in enumerate(contract["scene_ids"], start=1):
        if transition_scene == index:
            transitioned = True
        value = to_state if transitioned else from_state
        scenes.append(
            {
                "scene_id": scene_id,
                "evidence_locator": f"scene_packages/{scene_id}",
                "state_evidence": {
                    "entity_identity": fixture["tracked_entities"][0]["entity_id"],
                    dimension["dimension"]: value,
                    "authorized_transitions": [transition] if transition_scene == index else [],
                },
            }
        )
    return scenes


def phase_projection(contract: Mapping[str, Any], scenes: list[Mapping[str, Any]]) -> Dict[str, Any]:
    return build_state_phase_projection(
        contract,
        scenes,
        source_artifact="provider-free-phase-fixture",
        source_version="REPAIR19_TEST_V0.1",
        canonical_owner="Scene Writer",
    )


def r24_tree_hash() -> str:
    rows: list[bytes] = []
    for path in sorted((item for item in R24.rglob("*") if item.is_file()), key=lambda item: str(item).lower()):
        rows.append(
            f"{path.relative_to(R24).as_posix()} "
            f"{hashlib.sha256(path.read_bytes()).hexdigest()}".encode("utf-8")
        )
    return hashlib.sha256(b"\n".join(rows)).hexdigest()


def r24_raw_hash() -> str:
    return hashlib.sha256((R24 / "artifacts" / "scene_writer_provider_response.json").read_bytes()).hexdigest()


def r24_output() -> Dict[str, Any]:
    return json.loads((R24 / "artifacts" / "scene_writer_output.json").read_text(encoding="utf-8"))


def r24_envelope() -> Dict[str, Any]:
    return json.loads((R24 / "envelopes" / "02_scene_writer_to_director.json").read_text(encoding="utf-8"))


def r24_phase_replay() -> Dict[str, Any]:
    output = r24_output()
    scenes = output["scene_packages"]
    contract = compiled(3)
    projection = build_state_phase_projection(
        contract,
        scenes,
        source_artifact=str(R24 / "artifacts" / "scene_writer_output.json"),
        source_version="SCENE_WRITER_TRANSPORT_V0.1",
        canonical_owner="Scene Writer",
    )
    assertions = e2e.build_scene_assertions(
        scenes,
        source_artifact=str(R24 / "artifacts" / "scene_writer_output.json"),
        source_version="SCENE_WRITER_TRANSPORT_V0.1",
        canonical_owner="Scene Writer",
    )
    ledger = E2EStateLedger(run_id="E2E-RUN-24-RECORDED-REPLAY-REPAIR19")
    envelope = r24_envelope()
    for scene in scenes:
        ledger.append(envelope=envelope, state_snapshot=copy.deepcopy(scene["state_evidence"]))
    report = evaluate_semantic_safeguard(
        envelope=envelope,
        ledger=ledger,
        creative_output=output["content"],
        assertions=assertions,
    )
    required = next(item for item in assertions if item["id"] == "REQUIRED-STATE")
    transition = next(item for item in assertions if item["id"] == "AUTHORIZED-TRANSITION")
    dimension = contract["fixture"]["state_dimensions"][0]["dimension"]
    first_scene = contract["scene_ids"][0]
    return {
        "projection": projection,
        "entry": resolve_state_phase_snapshot(projection, scene_id=first_scene, state_dimension=dimension, phase="ENTRY"),
        "exit": resolve_state_phase_snapshot(projection, scene_id=first_scene, state_dimension=dimension, phase="EXIT"),
        "required_assertion": required,
        "transition": transition["value"],
        "report": report,
        "ledger": ledger,
        "raw_sha256_before": r24_raw_hash(),
        "raw_sha256_after": r24_raw_hash(),
        "tree_sha256_before": r24_tree_hash(),
        "tree_sha256_after": r24_tree_hash(),
    }


def assertion(value: Any, expected: Any, *, assertion_id: str = "REQUIRED-STATE") -> Dict[str, Any]:
    return {
        "id": assertion_id,
        "rule": "REQUIRED_STATE",
        "value": value,
        "expected": expected,
        "authority_source": "E2E-FIX-03",
        "evidence_locator": "phase-replay#state",
        "authorized_transition": False,
        "semantic_review_required": False,
    }


def evaluate_required(value: Any, expected: Any) -> Dict[str, Any]:
    replay = r24_phase_replay()
    return evaluate_semantic_safeguard(
        envelope=r24_envelope(),
        ledger=replay["ledger"],
        creative_output=r24_output()["content"],
        assertions=[assertion(value, expected)],
    )


def run_json(script: Path) -> tuple[int, Dict[str, Any]]:
    env = dict(os.environ)
    env["AFS_E2E_FIXTURE_BINDING"] = str(binding(3))
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
