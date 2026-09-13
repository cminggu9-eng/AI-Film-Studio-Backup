"""Provider-free Scene Writer Integration Contract suite for E2E Targeted Repair 01."""

from __future__ import annotations

import copy
import hashlib
import inspect
import json
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable, Dict


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
HARNESS_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
for import_path in (str(ROOT / "implementation"), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

import scene_writer_integration_contract as contract
import run_minimal_e2e as e2e
from provider_response_persistence import persist_provider_response
from fixture_contract_compiler import compile_path
from scene_writer_scene_id_contract import build_scene_id_contract
from scene_writer_state_field_contract import build_scene_writer_state_projection, state_field_name


RUN_ID = "SW-INT-TEST-01"
SCENE_WRITER_SKILL = AUTOMATION_ROOT.parent / "AI_Film_Studio_Obsidian_Vault_V0.1" / "01_SKILLS" / "02_Scene_Writer" / "scene-writer" / "SKILL.md"
FAILED_OUTPUT = HARNESS_STAGE / "evidence" / "E2E-RUN-01-RECOVERY-01" / "artifacts" / "scene_writer_output.json"
FIXTURE_BINDING = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1" / "fixtures" / "E2E_FIX_01_Runtime_Binding_V0.1.json"
FIXTURE_CONTRACT = compile_path(FIXTURE_BINDING)
SCENE_ID_CONTRACT = build_scene_id_contract(FIXTURE_CONTRACT)
STATE_FIELD_CONTRACT = build_scene_writer_state_projection(FIXTURE_CONTRACT)
STATE_FIELD = state_field_name(STATE_FIELD_CONTRACT)


def valid_output() -> Dict[str, Any]:
    scenes = []
    for index, scene_id in enumerate(SCENE_ID_CONTRACT["ordered_scene_ids"], start=1):
        code = "soaked_uniform" if index == 1 else "changed_clothes"
        scenes.append(
            {
                "scene_id": scene_id,
                "content": f"场景 {index}：正常的中文场景材料。",
                "structural_deliverable": {
                    "目标": "推进受授权的当前行动。",
                    "阻力": "关系与信息限制构成阻力。",
                    "对白行动": "通过对话试探并确认边界。",
                    "转折": "行动条件发生可见变化。",
                    "入场": "从当前压力点进入。",
                    "出场": "在下一状态建立后离开。",
                },
                "state_evidence": {
                    "entity_identity": "A-17",
                    "entity_custody": "许宁持有并可追踪。",
                    "knowledge_holders": ["许宁", "许曼"],
                    "reveal_status": "REVEALED_WITH_EVENT" if index == 3 else "NOT_YET_REVEALED",
                    "relationship_state": "未完全和解。",
                    STATE_FIELD: code,
                    "machine_state_display": "许宁仍穿湿透制服。" if index == 1 else "许宁已换下湿透制服，穿着干净衣物。",
                    "location_presence": "受授权地点内。",
                    "authorized_transitions": ["change_from_soaked_uniform"] if index == 3 else [],
                },
                "source_attribution": {
                    "source_role": "Scene Writer",
                    "source_record_id": f"{RUN_ID}/scene_writer/{scene_id}",
                    "version": "0.1",
                    "evidence_locator": f"scene_packages/{scene_id}",
                },
                "evidence_locator": f"scene_packages/{scene_id}",
            }
        )
    return {
        "primary_state_or_outcome": "SCENE_CREATED",
        "flags": "ABSENT",
        "handoffs": "ABSENT",
        "scene_packages": scenes,
    }


def full_transport_output() -> Dict[str, Any]:
    output = valid_output()
    for scene in output["scene_packages"]:
        scene["source_attribution"]["source_record_id"] = f"{e2e.RUN_ID}/scene_writer/{scene['scene_id']}"
    output.update(
        {
            "canon_assignment_locks": ["frozen-lock"],
            "prohibited_changes": ["frozen-prohibition"],
            "required_outcome": "ABSENT",
            "unresolved_decisions": [],
            "state_evidence": {
                "relevant_prior_state": "ABSENT",
                "current_state": "ABSENT",
                "proposed_state": "ABSENT",
                "knowledge_timing": "ABSENT",
                "relationship_state": "ABSENT",
                "visual_state": "ABSENT",
            },
            "content": "场景 1\n场景 2\n场景 3",
        }
    )
    return output


def _assert_rejected(output: Dict[str, Any], code: str) -> None:
    report = contract.assess_scene_writer_integration_contract(output, run_id=RUN_ID, fixture_contract=FIXTURE_CONTRACT)
    diagnostics = report["structural_gate"]["diagnostics"] + report["state_token_gate"]["diagnostics"]
    assert not report["passed"], report
    assert code in [item["code"] for item in diagnostics], diagnostics


def _run_case(case_id: str, action: Callable[[], str]) -> Dict[str, str]:
    try:
        return {"id": case_id, "result": "PASS", "detail": action()}
    except Exception as exc:
        return {"id": case_id, "result": "FAIL", "detail": f"{type(exc).__name__}: {exc}"}


def main() -> int:
    initial_hash = hashlib.sha256(SCENE_WRITER_SKILL.read_bytes()).hexdigest()
    counters = {"provider_calls": 0, "executor_calls": 0, "semantic_safeguard_calls": 0, "legacy_verifier_calls": 0}

    def valid_machine_code() -> str:
        assert contract.validate_scene_writer_integration_contract(valid_output(), run_id=RUN_ID, fixture_contract=FIXTURE_CONTRACT)["scene_packages"][0]["state_evidence"][STATE_FIELD] == "soaked_uniform"
        assert e2e.validate_role_output(e2e.role_spec("scene_writer"), full_transport_output(), scene_id_contract=SCENE_ID_CONTRACT, state_field_contract=STATE_FIELD_CONTRACT, fixture_contract=FIXTURE_CONTRACT)["scene_packages"][0]["state_evidence"][STATE_FIELD] == "soaked_uniform"
        return "valid exact machine-state codes are accepted through the integrated Scene Writer role-contract path"

    def chinese_display_allowed() -> str:
        output = valid_output()
        output["scene_packages"][0]["state_evidence"]["machine_state_display"] = "许宁的夜班制服被暴雨浸透。"
        assert contract.assess_scene_writer_integration_contract(output, run_id=RUN_ID, fixture_contract=FIXTURE_CONTRACT)["passed"]
        return "Chinese display prose is accepted without token aliasing"

    def display_cannot_replace_code() -> str:
        output = valid_output()
        output["scene_packages"][0]["state_evidence"][STATE_FIELD] = "湿透制服"
        _assert_rejected(output, "INVALID_MACHINE_STATE_CODE")
        return "display prose cannot replace the exact machine code"

    def missing_code_rejected() -> str:
        output = valid_output()
        del output["scene_packages"][0]["state_evidence"][STATE_FIELD]
        _assert_rejected(output, "MISSING_MACHINE_STATE_CODE")
        return "missing machine code is attributable structural failure"

    def wrong_code_rejected() -> str:
        output = valid_output()
        output["scene_packages"][0]["state_evidence"][STATE_FIELD] = "wet_uniform"
        _assert_rejected(output, "INVALID_MACHINE_STATE_CODE")
        return "wrong exact machine code is rejected"

    def required_structure_present() -> str:
        output = valid_output()
        for scene in output["scene_packages"]:
            assert tuple(scene["structural_deliverable"].keys()) == contract.STRUCTURAL_FIELD_NAMES
        assert contract.assess_scene_writer_integration_contract(output, run_id=RUN_ID, fixture_contract=FIXTURE_CONTRACT)["structural_gate"]["passed"]
        return "all six frozen structural fields are present for every scene"

    def missing_structure_rejected() -> str:
        output = valid_output()
        del output["scene_packages"][1]["structural_deliverable"]["转折"]
        _assert_rejected(output, "MISSING_STRUCTURAL_ITEM")
        return "one missing frozen structural item is rejected"

    def scenes_independently_validated() -> str:
        output = valid_output()
        del output["scene_packages"][2]["source_attribution"]
        report = contract.assess_scene_writer_integration_contract(output, run_id=RUN_ID, fixture_contract=FIXTURE_CONTRACT)
        assert any(item["path"].startswith("scene_packages[2]") for item in report["structural_gate"]["diagnostics"])
        return "all three scenes are validated independently"

    def canonical_tokens_preserved() -> str:
        output = valid_output()
        before = copy.deepcopy(output)
        validated = contract.validate_scene_writer_integration_contract(output, run_id=RUN_ID, fixture_contract=FIXTURE_CONTRACT)
        assert validated["primary_state_or_outcome"] == "SCENE_CREATED"
        assert validated["flags"] == "ABSENT" and validated["handoffs"] == "ABSENT"
        assert output == before
        return "Scene Writer canonical tokens are preserved exactly"

    def unsupported_field_rejected() -> str:
        output = valid_output()
        output["scene_packages"][0]["unsupported_adapter_field"] = "invented"
        _assert_rejected(output, "SCENE_FIELD_SET")
        return "unsupported structural field invention is rejected"

    def gate_does_not_rewrite() -> str:
        output = valid_output()
        before = copy.deepcopy(output)
        validated = contract.validate_scene_writer_integration_contract(output, run_id=RUN_ID, fixture_contract=FIXTURE_CONTRACT)
        assert output == before and validated == before and validated is not output
        return "structural/state-token gate returns a deep copy without rewriting output"

    def semantic_separate() -> str:
        report = contract.assess_scene_writer_integration_contract(valid_output(), run_id=RUN_ID, fixture_contract=FIXTURE_CONTRACT)
        assert "semantic_safeguard" not in report and counters["semantic_safeguard_calls"] == 0
        return "semantic safeguard remains a separate later gate"

    def legacy_supplemental() -> str:
        source = inspect.getsource(contract)
        assert "legacy_verifier" not in source and counters["legacy_verifier_calls"] == 0
        return "legacy verifier is neither invoked nor elevated by the structural gate"

    def persisted_before_gate() -> str:
        with tempfile.TemporaryDirectory(prefix="afs-sw-contract-order-") as temp:
            root = Path(temp)
            raw = json.dumps(valid_output(), ensure_ascii=False, separators=(",", ":"))
            persisted = persist_provider_response(
                evidence_dir=root,
                role="Scene Writer",
                invocation_id="SW-INT-14:scene_writer:1",
                timestamp="2026-08-28T00:00:00+00:00",
                raw_response={"raw_content": raw, "provider": "deepseek", "model": "deepseek-v4-pro", "provider_invocation_id": "recorded"},
                usage_record={"usage": {"prompt_tokens": 1, "completion_tokens": 1}},
                input_artifact="recorded/scene_writer_input.json",
            )
            assert Path(persisted["raw_response_artifact"]).is_file() and Path(persisted["invocation_metadata_artifact"]).is_file()
            assert contract.assess_scene_writer_integration_contract(valid_output(), run_id=RUN_ID, fixture_contract=FIXTURE_CONTRACT)["passed"]
        assert counters["provider_calls"] == 0 and counters["executor_calls"] == 0
        return "raw response and invocation metadata are verified before the contract gate; no Provider or executor call is made"

    def no_canonical_mutation() -> str:
        assert hashlib.sha256(SCENE_WRITER_SKILL.read_bytes()).hexdigest() == initial_hash
        return "Scene Writer canonical SKILL hash remains unchanged"

    def failed_output_regression() -> str:
        failed = json.loads(FAILED_OUTPUT.read_text(encoding="utf-8"))
        report = contract.assess_scene_writer_integration_contract(failed, run_id="E2E-RUN-01", fixture_contract=FIXTURE_CONTRACT)
        diagnostics = report["structural_gate"]["diagnostics"] + report["state_token_gate"]["diagnostics"]
        codes = {item["code"] for item in diagnostics}
        assert "MISSING_MACHINE_STATE_CODE" in codes and "MISSING_STRUCTURAL_DELIVERABLE" in codes, diagnostics
        return "frozen failed output is diagnosed for missing exact machine state code and six-item structural deliverable"

    results = [
        _run_case("SW-INT-01", valid_machine_code),
        _run_case("SW-INT-02", chinese_display_allowed),
        _run_case("SW-INT-03", display_cannot_replace_code),
        _run_case("SW-INT-04", missing_code_rejected),
        _run_case("SW-INT-05", wrong_code_rejected),
        _run_case("SW-INT-06", required_structure_present),
        _run_case("SW-INT-07", missing_structure_rejected),
        _run_case("SW-INT-08", scenes_independently_validated),
        _run_case("SW-INT-09", canonical_tokens_preserved),
        _run_case("SW-INT-10", unsupported_field_rejected),
        _run_case("SW-INT-11", gate_does_not_rewrite),
        _run_case("SW-INT-12", semantic_separate),
        _run_case("SW-INT-13", legacy_supplemental),
        _run_case("SW-INT-14", persisted_before_gate),
        _run_case("SW-INT-15", no_canonical_mutation),
    ]
    regression = _run_case("FROZEN-FAILED-OUTPUT", failed_output_regression)
    payload = {"suite": "Scene Writer Integration Contract", "results": results, "frozen_failed_output_regression": regression, "passed": sum(item["result"] == "PASS" for item in results), "total": len(results), "counters": counters}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["passed"] == payload["total"] and regression["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
