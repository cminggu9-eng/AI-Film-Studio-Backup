"""Provider-free STRICT-01 through STRICT-15 for Scene Writer transport."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, Mapping


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
HARNESS_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Minimal_E2E_Runtime_Validation_V0.1"
REPAIR_01 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_01_Scene_Writer_Integration_Contract_V0.1"
REPAIR_02 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_02_Scene_Writer_Response_Budget_Serialization_V0.1"
REPAIR_07 = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1"
REPAIR_08C = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "E2E_Targeted_Repair_08C_Scene_Writer_Strict_Schema_Composition_V0.1"
for import_path in (str(ROOT / "implementation"), str(REPAIR_02 / "implementation"), str(REPAIR_01 / "implementation"), str(REPAIR_07 / "implementation"), str(REPAIR_08C / "implementation"), str(HARNESS_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

import run_minimal_e2e as e2e
from provider_response_persistence import persist_provider_response
from runtime.shared_qa.model_executor import ModelExecutor, ModelRequest, ModelResponse
from scene_writer_compact_serialization import COMPACT_FORMAT
from scene_writer_integration_contract import STRUCTURAL_FIELD_NAMES, assess_scene_writer_integration_contract
from scene_writer_scene_id_contract import build_scene_id_contract
from scene_writer_state_field_contract import build_scene_writer_state_projection, state_field_name
from scene_writer_schema_composer import compose as compose_scene_writer_schema
from fixture_contract_compiler import compile_path
from scene_writer_strict_transport import (
    FUNCTION_NAME,
    build_structured_output_contract,
    validate_required_tool_call_shape,
    validate_provider_strict_schema,
    validate_strict_scene_writer_arguments,
)


EXPECTED_HASHES = copy.deepcopy(e2e.EXPECTED_HASHES)
FIXTURE_BINDING = REPAIR_07 / "fixtures" / "E2E_FIX_01_Runtime_Binding_V0.1.json"
FIXTURE_CONTRACT = compile_path(FIXTURE_BINDING)
SCENE_ID_CONTRACT = build_scene_id_contract(FIXTURE_CONTRACT)
STATE_FIELD_CONTRACT = build_scene_writer_state_projection(FIXTURE_CONTRACT)
STATE_FIELD = state_field_name(STATE_FIELD_CONTRACT)
PARAMETERS_SCHEMA = compose_scene_writer_schema(FIXTURE_CONTRACT, scene_id_contract=SCENE_ID_CONTRACT, state_field_contract=STATE_FIELD_CONTRACT)


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
            "prior": {"relationship_state": "久未联系，关系疏离", "knowledge_state": "储物间内容未知", "visual_state": "暴雨夜，湿透制服"},
            "current": {"relationship_state": "被迫共处", "knowledge_state": "共同开启规则已知，内容未知", "visual_state": "钥匙已出示"},
            "proposed": {"relationship_state": "临时合作但未和解", "knowledge_state": "天亮后共同开启", "visual_state": "换下湿制服"},
            "knowledge_timing": {"reveal_of_shared_use": "场景1由许曼告知", "reveal_of_room_content": "三场结束时仍未知"},
            "relationship": {"initial": "生疏试探", "after_scene_1": "被迫共处", "after_scene_3": "未和解的临时合作"},
            "visual": {"scene_1": "湿透制服", "scene_2": "换衣等待", "scene_3": "门前准备开启"},
        },
        "scenes": [
            {
                "id": "E2E-FIX-01-S01",
                "content": "场景 1\n许宁湿透进门，递出刻有 A-17 的钥匙。\n许曼说：\"必须两个人一起开。\"",
                "structural": {"目标": "交付钥匙", "阻力": "内容未知", "对白行动": "许曼说明规则", "转折": "共同开启被确认", "入场": "许宁湿透携钥入门", "出场": "钥匙留在两人之间"},
                "state": {"entity_id": "A-17", "custody": "许宁交出，许曼共同看守", "holders": ["许宁", "许曼"], "reveal": "REVEALED_WITH_EVENT", "relationship": "生疏试探", STATE_FIELD: "soaked_uniform", "state_display": "许宁夜班制服湿透", "location": "许曼住所门厅", "transitions": []},
            },
            {
                "id": "E2E-FIX-01-S02",
                "content": "场景 2\n许宁换下湿制服，在客厅等待天亮。许曼拒绝说明储物间内容。",
                "structural": {"目标": "确认等待步骤", "阻力": "内容未知与旧日疏离", "对白行动": "以规则代替解释", "转折": "许宁接受等待", "入场": "许宁已换下湿制服", "出场": "两人仍未说开旧事"},
                "state": {"entity_id": "A-17", "custody": "钥匙由两人共同看守", "holders": ["许宁", "许曼"], "reveal": "NOT_YET_REVEALED", "relationship": "疏离但暂时合作", STATE_FIELD: "changed_clothes", "state_display": "许宁已换下湿制服", "location": "许曼住所门厅", "transitions": ["change_from_soaked_uniform"]},
            },
            {
                "id": "E2E-FIX-01-S03",
                "content": "场景 3\n天亮前，两人带着 A-17 到储物间门前。门尚未打开，关系也没有完全和解。",
                "structural": {"目标": "抵达共同决定", "阻力": "内容未知且关系未解", "对白行动": "重申共同开启", "转折": "许宁接受共同开启", "入场": "两人带钥匙到门前", "出场": "门未开启，悬念保留"},
                "state": {"entity_id": "A-17", "custody": "两人共同携带钥匙", "holders": ["许宁", "许曼"], "reveal": "NOT_YET_REVEALED", "relationship": "未和解，仅共同完成下一步", STATE_FIELD: "changed_clothes", "state_display": "许宁穿着换下湿制服后的衣物", "location": "储物间门前", "transitions": ["change_from_soaked_uniform"]},
            },
        ],
    }


def frozen_locks() -> tuple[list[str], list[str]]:
    path = HARNESS_STAGE / "evidence" / "E2E-RUN-01-RECOVERY-01" / "artifacts" / "showrunner_output.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    return value["canon_assignment_locks"], value["prohibited_changes"]


def semantic_projection(compact: Mapping[str, Any], normalized: Mapping[str, Any]) -> bool:
    for source, expanded in zip(compact["scenes"], normalized["scene_packages"]):
        state = expanded["state_evidence"]
        if source["content"] != expanded["content"] or source["structural"] != expanded["structural_deliverable"]:
            return False
        if source["state"]["entity_id"] != state["entity_identity"] or source["state"]["custody"] != state["entity_custody"]:
            return False
        if source["state"]["holders"] != state["knowledge_holders"] or source["state"]["reveal"] != state["reveal_status"]:
            return False
        if source["state"]["relationship"] != state["relationship_state"] or source["state"][STATE_FIELD] != state[STATE_FIELD]:
            return False
        if source["state"]["state_display"] != state["machine_state_display"] or source["state"]["location"] != state["location_presence"]:
            return False
        if source["state"]["transitions"] != state["authorized_transitions"]:
            return False
    return True


def function_response(payload: Mapping[str, Any], *, prose: str = "", tool_name: str = FUNCTION_NAME) -> ModelResponse:
    arguments = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    wire = json.dumps({"id": "synthetic-strict-01", "model": "deepseek-v4-pro", "choices": [{"message": {"content": prose or None, "tool_calls": [{"id": "call-1", "type": "function", "function": {"name": tool_name, "arguments": arguments}}]}, "finish_reason": "tool_calls"}], "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}}, ensure_ascii=False, separators=(",", ":"))
    return ModelResponse(content=prose, provider="deepseek", model="deepseek-v4-pro", provider_invocation_id="synthetic-strict-01", usage={"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}, latency_ms=1, thinking_mode="disabled", finish_reason="tool_calls", tool_calls=({"id": "call-1", "type": "function", "function": {"name": tool_name, "arguments": arguments}},), raw_provider_response=wire)


class SyntheticStrictProvider:
    provider = "deepseek"
    model = "deepseek-v4-pro"
    thinking_mode = "disabled"

    def __init__(self, response: ModelResponse) -> None:
        self.response = response
        self.request_count = 0
        self.request = None

    def complete(self, request: Any) -> ModelResponse:
        self.request_count += 1
        self.request = request
        return self.response

    @staticmethod
    def estimate_cost_cny(_: Mapping[str, Any]) -> float:
        return 0.0


def test_persistence_before_validation() -> bool:
    raw_wire = json.dumps({"id": "synthetic-strict-evidence", "choices": []}, ensure_ascii=False, separators=(",", ":"))
    with tempfile.TemporaryDirectory() as directory:
        evidence = Path(directory)
        persisted = persist_provider_response(
            evidence_dir=evidence,
            role="Scene Writer",
            invocation_id="STRICT-PERSIST-01",
            timestamp="STATIC",
            raw_response={
                "raw_content": raw_wire,
                "raw_provider_response": raw_wire,
                "assistant_content": "ordinary assistant prose",
                "tool_calls": [],
                "provider": "synthetic",
                "model": "synthetic",
                "provider_invocation_id": "synthetic-strict-evidence",
                "finish_reason": "stop",
                "requested_max_tokens": 0,
                "structured_output": {"function_name": FUNCTION_NAME, "transport": "forced_function"},
            },
            usage_record={"request_success": True},
            input_artifact="STATIC",
        )
        raw_path = Path(persisted["raw_response_artifact"])
        value = json.loads(raw_path.read_text(encoding="utf-8")) if raw_path.is_file() else {}
        return value.get("lifecycle_stage") == "RAW_RESPONSE_PERSISTED" and value.get("raw_provider_response") == raw_wire


def test_required_function_name() -> bool:
    try:
        validate_required_tool_call_shape(
            assistant_content="",
            tool_calls=[{"id": "call-1", "type": "function", "function": {"name": "wrong_function", "arguments": "{}"}}],
        )
    except Exception:
        return True
    return False


def test_ordinary_prose_rejected() -> bool:
    try:
        validate_required_tool_call_shape(
            assistant_content="ordinary assistant prose",
            tool_calls=[{"id": "call-1", "type": "function", "function": {"name": FUNCTION_NAME, "arguments": "{}"}}],
        )
    except Exception:
        return True
    return False


def run() -> int:
    payload = compact_payload()
    locks, prohibitions = frozen_locks()
    contract = build_structured_output_contract(PARAMETERS_SCHEMA)
    serialized = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    parsed = json.loads(serialized)
    valid = validate_strict_scene_writer_arguments(parsed, parameters_schema=PARAMETERS_SCHEMA, scene_id_contract=SCENE_ID_CONTRACT, state_field_contract=STATE_FIELD_CONTRACT)
    hydrated = e2e.validate_role_output(e2e.role_spec("scene_writer"), valid, locks, prohibitions, run_id="STRICT-TEST-01", scene_id_contract=SCENE_ID_CONTRACT, state_field_contract=STATE_FIELD_CONTRACT, fixture_contract=FIXTURE_CONTRACT)
    scene_contract = assess_scene_writer_integration_contract(hydrated, run_id="STRICT-TEST-01", fixture_contract=FIXTURE_CONTRACT)

    bad_scene_count = copy.deepcopy(payload)
    bad_scene_count["scenes"].pop()
    bad_structural = copy.deepcopy(payload)
    del bad_structural["scenes"][0]["structural"]["入场"]
    bad_machine = copy.deepcopy(payload)
    bad_machine["scenes"][0]["state"][STATE_FIELD] = "wet"
    bad_extra = copy.deepcopy(payload)
    bad_extra["scenes"][0]["unexpected"] = "blocked"
    multiline = copy.deepcopy(payload)
    multiline["scenes"][1]["structural"]["入场"] = "许宁换完衣服进入客厅，\n坐定"
    quoted = copy.deepcopy(payload)
    quoted["scenes"][0]["content"] = "许曼说：\"A-17 不能一个人开。\""
    control = copy.deepcopy(payload)
    control["scenes"][0]["content"] = "许宁\u0001递出钥匙"

    def rejected(value: Mapping[str, Any]) -> bool:
        try:
            validate_strict_scene_writer_arguments(value, parameters_schema=PARAMETERS_SCHEMA, scene_id_contract=SCENE_ID_CONTRACT, state_field_contract=STATE_FIELD_CONTRACT)
        except Exception:
            return True
        return False

    current_hashes = {spec.key: e2e.canonical_skill(spec)[1] for spec in e2e.ROLE_SPECS}
    results = [
        {"id": "STRICT-01", "result": "PASS" if contract.function_name == FUNCTION_NAME and test_required_function_name() else "FAIL", "detail": "required function name is enforced"},
        {"id": "STRICT-02", "result": "PASS" if test_ordinary_prose_rejected() else "FAIL", "detail": "ordinary assistant prose cannot replace the required function call"},
        {"id": "STRICT-03", "result": "PASS" if rejected(bad_scene_count) else "FAIL", "detail": "exactly three scenes is locally enforced where provider strict mode lacks array bounds"},
        {"id": "STRICT-04", "result": "PASS" if rejected(bad_structural) else "FAIL", "detail": "all six structural fields are required"},
        {"id": "STRICT-05", "result": "PASS" if rejected(bad_machine) else "FAIL", "detail": "machine enum is required"},
        {"id": "STRICT-06", "result": "PASS" if hydrated["scene_packages"][0]["state_evidence"]["machine_state_display"] == payload["scenes"][0]["state"]["state_display"] else "FAIL", "detail": "display prose is retained"},
        {"id": "STRICT-07", "result": "PASS" if json.loads(json.dumps(multiline, ensure_ascii=False))["scenes"][1]["structural"]["入场"] == multiline["scenes"][1]["structural"]["入场"] and validate_strict_scene_writer_arguments(multiline, parameters_schema=PARAMETERS_SCHEMA, scene_id_contract=SCENE_ID_CONTRACT, state_field_contract=STATE_FIELD_CONTRACT) else "FAIL", "detail": "Chinese multiline content round-trips as JSON function arguments"},
        {"id": "STRICT-08", "result": "PASS" if json.loads(json.dumps(quoted, ensure_ascii=False))["scenes"][0]["content"] == quoted["scenes"][0]["content"] and validate_strict_scene_writer_arguments(quoted, parameters_schema=PARAMETERS_SCHEMA, scene_id_contract=SCENE_ID_CONTRACT, state_field_contract=STATE_FIELD_CONTRACT) else "FAIL", "detail": "quotes round-trip as JSON function arguments"},
        {"id": "STRICT-09", "result": "PASS" if "\\u0001" in json.dumps(control, ensure_ascii=False) and json.loads(json.dumps(control, ensure_ascii=False))["scenes"][0]["content"] == control["scenes"][0]["content"] and validate_strict_scene_writer_arguments(control, parameters_schema=PARAMETERS_SCHEMA, scene_id_contract=SCENE_ID_CONTRACT, state_field_contract=STATE_FIELD_CONTRACT) else "FAIL", "detail": "control characters serialize legally"},
        {"id": "STRICT-10", "result": "PASS" if rejected(bad_extra) else "FAIL", "detail": "unknown fields are rejected by additionalProperties=false"},
        {"id": "STRICT-11", "result": "PASS" if scene_contract["passed"] else "FAIL", "detail": "hydrated output passes Scene Writer integration gates"},
        {"id": "STRICT-12", "result": "PASS" if len(hydrated["scene_packages"]) == 3 and hydrated["state_evidence"]["knowledge_timing"] == payload["state"]["knowledge_timing"] else "FAIL", "detail": "hydrated output passes the accepted compact serialization path"},
        {"id": "STRICT-13", "result": "PASS" if test_persistence_before_validation() else "FAIL", "detail": "raw provider evidence persists before transport validation"},
        {"id": "STRICT-14", "result": "PASS" if semantic_projection(payload, hydrated) else "FAIL", "detail": "hydration causes no semantic mutation"},
        {"id": "STRICT-15", "result": "PASS" if current_hashes == EXPECTED_HASHES else "FAIL", "detail": "all seven canonical Skill hashes remain unchanged"},
    ]
    payload_out = {"classification": "OFFLINE STRICT STRUCTURED TRANSPORT TEST", "schema_validation": validate_provider_strict_schema(SCENE_ID_CONTRACT, STATE_FIELD_CONTRACT), "results": results, "passed": sum(item["result"] == "PASS" for item in results), "total": len(results), "provider_calls": 0, "retries": 0, "fallbacks": 0, "json_auto_repairs": 0, "canonical_hashes": current_hashes}
    print(json.dumps(payload_out, ensure_ascii=False, indent=2))
    return 0 if payload_out["passed"] == payload_out["total"] else 1


if __name__ == "__main__":
    raise SystemExit(run())
