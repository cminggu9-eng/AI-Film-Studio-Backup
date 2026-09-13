"""Non-network Assignment Fact / Character Knowledge Lock tests for Scene Writer."""

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

from runtime.scene_writer.scene_writer_runtime import SceneWriterRuntime  # noqa: E402


def payload(request_id: str, **overrides: Any) -> Dict[str, Any]:
    base = {
        "request_id": request_id,
        "requested_mode": "CREATE",
        "output_language": "zh-CN",
        "scene_id": "FACT-KNOWLEDGE-CONTRACT",
        "scene_purpose": "以中性方式完成明确请求，不增加未经授权项目事实。",
        "canon_locks": ["原定演示人明早不能到场；具体原因未知，不得补写。"],
        "showrunner_locks": ["陈默最终同意先接下演示，但林妍今晚发送全部现有材料。"],
        "participants": [
            {"name": "林妍", "knowledge": "知道原定演示人不能到场；不知道具体原因。"},
            {"name": "陈默", "knowledge": "未获得原定演示人缺席原因的来源或细节。"},
        ],
        "required_event": "林妍提出请陈默接手明早演示。",
        "required_information": "原定演示人明早不能到场；原因未知，不得补写。",
        "required_outcome": "陈默有条件同意，林妍今晚发送全部现有材料。",
        "prior_scene_state": "会议结束，林妍与陈默留在会议室。",
        "desired_post_state": "陈默有条件接下演示，林妍今晚发送材料。",
    }
    base.update(overrides)
    return base


NEUTRAL_OUTPUT = {
    "creative_deliverable": {"kind": "scene", "content": "林妍把文件夹放在桌上，请陈默接手明早演示。陈默没有立刻答应，只要求今晚收到全部现有材料。林妍点头，开始整理文件。"},
    "control_data": {
        "primary_state": "SCENE_CREATED", "flags": [], "handoffs": [],
        "scene_function": "确认明早演示的承担者。",
        "objectives": "林妍寻求确认；陈默寻求明确条件。",
        "resistance": "陈默不接受没有材料的临时责任。",
        "before_state": "会议结束，两人留在会议室。",
        "turn": "陈默从保留转为有条件同意。",
        "state_after": "林妍今晚发送材料，陈默接下演示。",
        "entry_rationale": "从请求发生处进入。",
        "exit_rationale": "在条件确认后结束。",
    },
}


def runtime_for(output: Dict[str, Any]) -> SceneWriterRuntime:
    return SceneWriterRuntime(synthetic_executor=lambda _: copy.deepcopy(output), test_sandbox=True)


def expect_fact_rejection(case_id: str, output: Dict[str, Any], expected_code: str) -> str:
    result = runtime_for(output).execute(payload(case_id))
    assert result["runtime_status"] == "FAIL_SAFE", result
    assert result["runtime_failure_code"] == "ASSIGNMENT_FACT_LOCK_VIOLATION", result
    codes = {item["code"] for item in result["assignment_fact_validation"]["violations"]}
    assert expected_code in codes, result
    return expected_code


def run_case(case_id: str, function) -> Dict[str, str]:
    try:
        return {"id": case_id, "result": "PASS", "detail": function()}
    except Exception as exc:
        return {"id": case_id, "result": "FAIL", "detail": f"{type(exc).__name__}: {exc}"}


def with_scene(text: str) -> Dict[str, Any]:
    output = copy.deepcopy(NEUTRAL_OUTPUT)
    output["creative_deliverable"]["content"] = text
    return output


def main() -> int:
    results = []
    results.append(run_case("FK-SW-01", lambda: expect_fact_rejection("FK-SW-01", with_scene("林妍说：他临时有状况，所以明早来不了。"), "EXPLICIT_UNKNOWN_REASON_CONCRETIZED")))
    results.append(run_case("FK-SW-02", lambda: expect_fact_rejection("FK-SW-02", with_scene("林妍说：我从人事那里知道他明早来不了。"), "UNSUPPORTED_CHARACTER_KNOWLEDGE_SOURCE")))
    results.append(run_case("FK-SW-03", lambda: expect_fact_rejection("FK-SW-03", with_scene("陈默说：今晚十二点前必须把材料发给我。"), "COARSE_TIME_CONCRETIZED")))
    results.append(run_case("FK-SW-04", lambda: expect_fact_rejection("FK-SW-04", with_scene("林妍说：陈默最懂这些材料，所以只能由你接手。"), "UNSUPPORTED_CAPABILITY_RANKING")))
    results.append(run_case("FK-SW-05", lambda: expect_fact_rejection("FK-SW-05", with_scene("陈默说：我们以前一起做过项目，你知道我不喜欢临时接手。"), "UNSUPPORTED_RELATIONSHIP_HISTORY")))

    def neutral_action() -> str:
        result = runtime_for(NEUTRAL_OUTPUT).execute(payload("FK-SW-06"))
        assert result["runtime_status"] == "SUCCESS", result
        return "neutral immediate action remains lawful"
    results.append(run_case("FK-SW-06", neutral_action))

    def dialogue_strategy() -> str:
        result = runtime_for(with_scene("林妍没有绕开问题：‘明早的演示需要有人接手。’陈默看着文件夹：‘材料今晚都发给我，我再接。’")).execute(payload("FK-SW-07"))
        assert result["runtime_status"] == "SUCCESS", result
        return "request and conditional negotiation remain lawful dialogue construction"
    results.append(run_case("FK-SW-07", dialogue_strategy))

    def uncertainty_stays_uncertainty() -> str:
        result = runtime_for(with_scene("陈默问起缺席原因，林妍说：‘我不知道，也不想替他猜。’随后她把文件夹推过去。 ")).execute(payload("FK-SW-08"))
        assert result["runtime_status"] == "SUCCESS", result
        return "a stated uncertainty is not upgraded into knowledge"
    results.append(run_case("FK-SW-08", uncertainty_stays_uncertainty))

    results.append(run_case("FK-SW-09", lambda: expect_fact_rejection("FK-SW-09", with_scene("林妍说：我知道他临时有事，所以才来找你。"), "EXPLICIT_UNKNOWN_REASON_CONCRETIZED")))

    def no_context_hunger() -> str:
        result = runtime_for(NEUTRAL_OUTPUT).execute(payload("FK-SW-10"))
        assert result["runtime_status"] == "SUCCESS", result
        validation = result["assignment_fact_validation"]
        assert "EXPLICIT_UNKNOWN_REASON" in validation["guard_profile"] and "COARSE_TIME_TONIGHT" in validation["guard_profile"], validation
        return "complete assignment stays executable under fact protection"
    results.append(run_case("FK-SW-10", no_context_hunger))

    report = {"classification": "NON-NETWORK ASSIGNMENT FACT / CHARACTER KNOWLEDGE CONTRACT TEST", "results": results, "passed": sum(item["result"] == "PASS" for item in results), "total": len(results)}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] == report["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
