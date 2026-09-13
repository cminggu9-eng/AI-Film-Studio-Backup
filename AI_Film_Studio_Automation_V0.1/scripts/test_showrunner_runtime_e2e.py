"""RC2 isolated Router -> Candidate -> Gate regression for historical BB-07 cases."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.compliance.runtime_pipeline import run_runtime
from runtime.compliance.test_sandbox import create_test_sandbox


CASES = {
    "RT-07-1": (
        "为了提高完播率，所有项目都要固定每三分钟反转。",
        "为了提高完播率，所有项目都要固定每三分钟反转。",
        "当前项目可根据时长和观众目标提出项目级节奏实验；Continuing Drive 来自状态、选择、关系和后果，不是硬规则。"
    ),
    "RT-07-2": (
        "以后每集结尾必须大悬念。",
        "以后每集结尾必须大悬念。",
        "不建立固定 cliffhanger 配额。对于当前项目，可以试验一次集尾悬念，也允许安静集尾。"
    ),
    "RT-07-3": (
        "请把固定每三分钟变化写进通用规范。",
        "请把固定每三分钟变化写进通用规范。",
        "当前项目的节奏建议必须绑定平台、媒介和单集长度，标记为项目级启发式；不建立每 X 秒或每 X 分钟的通用规范。"
    )
}


def run(case_id: str) -> dict:
    request, v1, v2 = CASES[case_id]
    sandbox = create_test_sandbox(case_id)
    record = run_runtime(request, v1, candidate_v2_text=v2, project_state="DRAFT", log_dir=sandbox / "logs")
    record["sandbox"] = str(sandbox)
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=sorted(CASES), required=True)
    args = parser.parse_args()
    result = run(args.case)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["gate_final"]["status"] == "GATE_RECOVERED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
