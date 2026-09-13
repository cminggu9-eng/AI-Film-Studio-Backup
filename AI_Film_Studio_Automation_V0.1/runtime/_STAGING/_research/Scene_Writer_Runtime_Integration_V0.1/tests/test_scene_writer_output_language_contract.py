"""Non-network output-language transport and validation tests for Scene Writer."""

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

from runtime.compliance.compliance_gate import sha256_file  # noqa: E402
from runtime.scene_writer.scene_writer_runtime import SceneWriterRuntime  # noqa: E402


EXPECTED_HASH = "93e1be12988f8caa6cdd76acb5e6c1bf6ad3ca0dff5806a2ea93511e66052dfb"


def input_payload(request_id: str, **language_fields: str) -> Dict[str, Any]:
    return {
        "request_id": request_id,
        "requested_mode": "CREATE",
        "scene_id": "OUTPUT-LANGUAGE-CONTRACT",
        "scene_purpose": "non-network output-language contract validation",
        **language_fields,
    }


ZH_OUTPUT = {
    "creative_deliverable": {"kind": "scene", "content": "林妍站在会议桌旁，请陈默留下处理明早的演示。陈默没有立刻答应，只要求先收到全部现有材料。"},
    "control_data": {
        "primary_state": "SCENE_CREATED",
        "flags": ["PRODUCTION_REVIEW_REQUIRED"],
        "handoffs": [],
        "scene_function": "在时间压力下确认明早演示的承担者。",
        "objectives": "林妍需要确认人选；陈默需要先获得工作条件。",
        "resistance": "陈默不接受没有材料的临时责任。",
        "before_state": "会议结束，陈默准备离开。",
        "turn": "陈默从拒绝立即承担转为有条件接下。",
        "state_after": "林妍需要在今晚发送全部现有材料。",
        "entry_rationale": "从会议结束后的私下请求进入。",
        "exit_rationale": "停在条件被确认后的下一步压力上。",
        "diagnosis_summary": "无阻断项。",
    },
}

EN_OUTPUT = {
    "creative_deliverable": {"kind": "scene", "content": "Lin Yan asks Chen Mo to cover tomorrow's presentation. Chen Mo refuses to commit until every existing file is sent tonight."},
    "control_data": {
        "primary_state": "SCENE_CREATED",
        "flags": ["PRODUCTION_REVIEW_REQUIRED"],
        "handoffs": [],
        "scene_function": "Confirm a presenter under immediate time pressure.",
        "objectives": "Lin Yan needs a commitment; Chen Mo needs workable conditions.",
        "resistance": "Chen Mo will not accept an unprepared last-minute responsibility.",
        "before_state": "The meeting is over and Chen Mo is leaving.",
        "turn": "Chen Mo shifts from resistance to conditional acceptance.",
        "state_after": "Lin Yan must send all existing material tonight.",
        "entry_rationale": "Enter at the urgent private request.",
        "exit_rationale": "Exit on the confirmed condition and remaining obligation.",
        "diagnosis_summary": "No blocker.",
    },
}


def runtime_for(output: Dict[str, Any]) -> SceneWriterRuntime:
    return SceneWriterRuntime(synthetic_executor=lambda _: copy.deepcopy(output), test_sandbox=True)


def run_case(case_id: str, function) -> Dict[str, str]:
    try:
        return {"id": case_id, "result": "PASS", "detail": function()}
    except Exception as exc:
        return {"id": case_id, "result": "FAIL", "detail": f"{type(exc).__name__}: {exc}"}


def main() -> int:
    results = []

    def explicit_zh() -> str:
        response = runtime_for(ZH_OUTPUT).execute(input_payload("OL-SW-01", output_language="zh-CN"))
        assert response["runtime_status"] == "SUCCESS" and response["output_language"] == "zh-CN", response
        assert response["output_language_resolution"] == "EXPLICIT", response
        return "explicit zh-CN reaches Runtime validation"
    results.append(run_case("OL-SW-01", explicit_zh))

    def explicit_en() -> str:
        response = runtime_for(EN_OUTPUT).execute(input_payload("OL-SW-02", output_language="en-US"))
        assert response["runtime_status"] == "SUCCESS" and response["output_language"] == "en-US", response
        return "explicit en-US reaches Runtime validation"
    results.append(run_case("OL-SW-02", explicit_en))

    def canonical_tokens_stay_exact() -> str:
        response = runtime_for(ZH_OUTPUT).execute(input_payload("OL-SW-03", output_language="zh-CN"))
        control = response["scene_writer"]["control_data"]
        assert control["primary_state"] == "SCENE_CREATED", control
        assert control["flags"] == ["PRODUCTION_REVIEW_REQUIRED"], control
        translated = copy.deepcopy(ZH_OUTPUT)
        translated["control_data"]["primary_state"] = "场景已创建"
        rejected = runtime_for(translated).execute(input_payload("OL-SW-03-REJECT", output_language="zh-CN"))
        assert rejected["runtime_status"] == "FAIL_SAFE", rejected
        return "canonical state and flag tokens remain exact English tokens"
    results.append(run_case("OL-SW-03", canonical_tokens_stay_exact))

    def inherit_assignment_language() -> str:
        response = runtime_for(ZH_OUTPUT).execute(input_payload("OL-SW-04", assignment_language="zh-CN"))
        assert response["runtime_status"] == "SUCCESS", response
        assert response["output_language"] == "zh-CN" and response["output_language_resolution"] == "INHERIT_ASSIGNMENT_LANGUAGE", response
        return "missing output_language inherits explicit assignment_language without script guessing"
    results.append(run_case("OL-SW-04", inherit_assignment_language))

    def missing_language_rejected() -> str:
        response = runtime_for(EN_OUTPUT).execute(input_payload("OL-SW-05"))
        assert response["runtime_status"] == "CONTRACT_ERROR" and response["runtime_failure_code"] == "OUTPUT_LANGUAGE_UNRESOLVED", response
        return "missing output_language and assignment_language is deterministic contract error"
    results.append(run_case("OL-SW-05", missing_language_rejected))

    def invalid_language_rejected() -> str:
        response = runtime_for(EN_OUTPUT).execute(input_payload("OL-SW-06", output_language="zh"))
        assert response["runtime_status"] == "CONTRACT_ERROR" and response["runtime_failure_code"] == "INVALID_OUTPUT_LANGUAGE", response
        return "invalid language token rejected"
    results.append(run_case("OL-SW-06", invalid_language_rejected))

    def language_mismatch_rejected() -> str:
        response = runtime_for(EN_OUTPUT).execute(input_payload("OL-SW-07", output_language="zh-CN"))
        assert response["runtime_status"] == "FAIL_SAFE" and response["runtime_failure_code"] == "MALFORMED_EXECUTOR_OUTPUT", response
        return "English creative/control text cannot satisfy explicit zh-CN"
    results.append(run_case("OL-SW-07", language_mismatch_rejected))

    def no_skill_hardcode() -> str:
        runtime = SceneWriterRuntime()
        skill_text = runtime.canonical_skill_path.read_text(encoding="utf-8")
        assert sha256_file(runtime.canonical_skill_path).lower() == EXPECTED_HASH
        assert "output_language" not in skill_text and "永远中文" not in skill_text
        return "canonical Skill hash and body remain language-agnostic"
    results.append(run_case("OL-SW-08", no_skill_hardcode))

    payload = {"classification": "NON-NETWORK OUTPUT LANGUAGE CONTRACT TEST", "results": results, "passed": sum(item["result"] == "PASS" for item in results), "total": len(results)}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["passed"] == payload["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
