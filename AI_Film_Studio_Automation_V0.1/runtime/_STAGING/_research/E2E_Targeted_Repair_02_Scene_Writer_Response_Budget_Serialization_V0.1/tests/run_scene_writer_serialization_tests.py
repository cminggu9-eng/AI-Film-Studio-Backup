"""Provider-free SER-01 through SER-12 for the compact Scene Writer transport."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Dict


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
HARNESS_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
REPAIR_01 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1"
REPAIR_07 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1"
for import_path in (str(ROOT / "implementation"), str(REPAIR_01 / "implementation"), str(REPAIR_07 / "implementation"), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

import run_minimal_e2e as e2e
from scene_writer_compact_serialization import COMPACT_FORMAT
from scene_writer_integration_contract import STRUCTURAL_FIELD_NAMES
from scene_writer_scene_id_contract import build_scene_id_contract
from scene_writer_state_field_contract import build_scene_writer_state_projection, state_field_name
from fixture_contract_compiler import compile_path

FIXTURE_CONTRACT = compile_path(REPAIR_07 / "fixtures" / "E2E_FIX_01_Runtime_Binding_V0.1.json")
SCENE_ID_CONTRACT = build_scene_id_contract(FIXTURE_CONTRACT)
STATE_FIELD_CONTRACT = build_scene_writer_state_projection(FIXTURE_CONTRACT)
STATE_FIELD = state_field_name(STATE_FIELD_CONTRACT)


def compact_payload() -> Dict[str, Any]:
    return {
        "format": COMPACT_FORMAT,
        "control": {
            "outcome": "SCENE_CREATED",
            "flags": "ABSENT",
            "handoffs": "ABSENT",
            "required_outcome": "ABSENT",
            "unresolved_decisions": "ABSENT",
        },
        "state": {
            "prior": {"A-17": "许宁携带", "clothing": "soaked_uniform"},
            "current": {"storage_room": "未开启", "custody": "两人共同确认"},
            "proposed": {"next": "天亮后共同开启，内容未知"},
            "knowledge_timing": {"storage_room_contents": "UNKNOWN"},
            "relationship": {"status": "疏离但暂时合作，未和解"},
            "visual": {"transition": "change_from_soaked_uniform"},
        },
        "scenes": [
            {
                "id": "E2E-FIX-01-S01",
                "content": "许宁穿着湿透制服进入门厅，把刻有 A-17 的钥匙放到许曼面前。许曼承认母亲要求两人共同开启储物间，却只让他先换衣、等天亮。",
                "structural": {"目标": "交付钥匙并确认用途", "阻力": "许曼不解释储物间内容", "对白行动": "许曼以换衣和等待阻断追问", "转折": "共同开启规则被确认", "入场": "许宁湿透携钥入门", "出场": "钥匙留在两人之间"},
                "state": {"entity_id": "A-17", "custody": "许宁交出钥匙，许曼与他共同保管", "holders": ["许宁", "许曼"], "reveal": "REVEALED_WITH_EVENT", "relationship": "久未联系，仍疏离", STATE_FIELD: "soaked_uniform", "state_display": "许宁的夜班制服湿透", "location": "许曼住所门厅", "transitions": []},
            },
            {
                "id": "E2E-FIX-01-S02",
                "content": "许宁换下湿制服，在门厅边等雨势减弱。许曼只谈母亲留下的规则，拒绝回答储物间里有什么；两人暂时同意等到天亮。",
                "structural": {"目标": "在等待中取得共同步骤", "阻力": "旧日疏离和内容未知", "对白行动": "两人以规则代替解释", "转折": "许宁接受等待条件", "入场": "许宁已换下湿制服", "出场": "两人仍未说开旧事"},
                "state": {"entity_id": "A-17", "custody": "钥匙由两人共同看守", "holders": ["许宁", "许曼"], "reveal": "NOT_YET_REVEALED", "relationship": "疏离但形成临时合作", STATE_FIELD: "changed_clothes", "state_display": "许宁已换下湿制服", "location": "许曼住所门厅", "transitions": ["change_from_soaked_uniform"]},
            },
            {
                "id": "E2E-FIX-01-S03",
                "content": "天色发白，许宁和许曼带着 A-17 走到储物间门前。许曼再次说明必须共同开启，许宁点头；门尚未打开，两人的关系也没有被宣布和解。",
                "structural": {"目标": "抵达开启前的共同决定", "阻力": "内容仍未知且关系未解", "对白行动": "许曼重申共同开启规则", "转折": "许宁接受共同开启", "入场": "两人带钥匙走到门前", "出场": "门未开启，悬念保留"},
                "state": {"entity_id": "A-17", "custody": "两人共同携带钥匙到门前", "holders": ["许宁", "许曼"], "reveal": "NOT_YET_REVEALED", "relationship": "未和解，仅共同完成下一步", STATE_FIELD: "changed_clothes", "state_display": "许宁已换下湿制服", "location": "储物间门前", "transitions": ["change_from_soaked_uniform"]},
            },
        ],
    }


def semantic_projection(compact: Dict[str, Any], normalized: Dict[str, Any]) -> bool:
    for compact_scene, expanded_scene in zip(compact["scenes"], normalized["scene_packages"]):
        if compact_scene["content"] != expanded_scene["content"]:
            return False
        if compact_scene["structural"] != expanded_scene["structural_deliverable"]:
            return False
        state = compact_scene["state"]
        expanded = expanded_scene["state_evidence"]
        if state["entity_id"] != expanded["entity_identity"] or state["custody"] != expanded["entity_custody"]:
            return False
        if state["holders"] != expanded["knowledge_holders"] or state["reveal"] != expanded["reveal_status"]:
            return False
        if state["relationship"] != expanded["relationship_state"] or state[STATE_FIELD] != expanded[STATE_FIELD]:
            return False
        if state["state_display"] != expanded["machine_state_display"] or state["location"] != expanded["location_presence"]:
            return False
        if state["transitions"] != expanded["authorized_transitions"]:
            return False
    return True


def run() -> int:
    frozen_showrunner = HARNESS_STAGE / "evidence" / "E2E-RUN-01-RECOVERY-01" / "artifacts" / "showrunner_output.json"
    frozen = json.loads(frozen_showrunner.read_text(encoding="utf-8"))
    locks = frozen["canon_assignment_locks"]
    prohibitions = frozen["prohibited_changes"]
    compact = compact_payload()
    serialized = json.dumps(compact, ensure_ascii=False, separators=(",", ":"))
    round_trip = json.loads(serialized)
    validated = e2e.validate_role_output(e2e.role_spec("scene_writer"), round_trip, locks, prohibitions, run_id="SER-TEST-01", scene_id_contract=SCENE_ID_CONTRACT, state_field_contract=STATE_FIELD_CONTRACT, fixture_contract=FIXTURE_CONTRACT)
    full_size = len(json.dumps(validated, ensure_ascii=False, separators=(",", ":")))
    compact_size = len(serialized)
    results = [
        {"id": "SER-01", "result": "PASS" if len(validated["scene_packages"]) == 3 else "FAIL", "detail": "three-scene payload serializes fully"},
        {"id": "SER-02", "result": "PASS" if all(set(item["structural_deliverable"]) == set(STRUCTURAL_FIELD_NAMES) for item in validated["scene_packages"]) else "FAIL", "detail": "six structural fields retained per scene"},
        {"id": "SER-03", "result": "PASS" if validated["scene_packages"][0]["state_evidence"][STATE_FIELD] == "soaked_uniform" else "FAIL", "detail": "machine tokens retained"},
        {"id": "SER-04", "result": "PASS" if all(item["state_evidence"]["machine_state_display"] for item in validated["scene_packages"]) else "FAIL", "detail": "display prose retained"},
        {"id": "SER-05", "result": "PASS" if all(item["source_attribution"]["version"] == "0.1" for item in validated["scene_packages"]) else "FAIL", "detail": "source/version retained"},
        {"id": "SER-06", "result": "PASS" if all(item["evidence_locator"] == item["source_attribution"]["evidence_locator"] for item in validated["scene_packages"]) else "FAIL", "detail": "evidence locator retained"},
        {"id": "SER-07", "result": "PASS" if validated["canon_assignment_locks"] == locks and validated["prohibited_changes"] == prohibitions else "FAIL", "detail": "Canon locks retained exactly"},
        {"id": "SER-08", "result": "PASS" if validated["state_evidence"]["knowledge_timing"] == compact["state"]["knowledge_timing"] else "FAIL", "detail": "knowledge timing retained"},
        {"id": "SER-09", "result": "PASS" if "change_from_soaked_uniform" in validated["scene_packages"][-1]["state_evidence"]["authorized_transitions"] else "FAIL", "detail": "authorized clothing transition retained"},
        {"id": "SER-10", "result": "PASS" if compact_size < full_size else "FAIL", "detail": f"compact transport {compact_size} chars vs normalized {full_size} chars"},
        {"id": "SER-11", "result": "PASS" if json.loads(json.dumps(validated, ensure_ascii=False)) == validated else "FAIL", "detail": "valid JSON round-trip"},
        {"id": "SER-12", "result": "PASS" if semantic_projection(compact, validated) else "FAIL", "detail": "no semantic mutation during normalization"},
    ]
    payload = {"classification": "OFFLINE SCENE WRITER SERIALIZATION TEST", "results": results, "passed": sum(item["result"] == "PASS" for item in results), "total": len(results), "provider_calls": 0, "real_role_executions": 0}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["passed"] == payload["total"] else 1


if __name__ == "__main__":
    raise SystemExit(run())
