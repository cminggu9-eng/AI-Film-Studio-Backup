"""RW-C01–RW-C10: deterministic rewrite-change contract tests."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.shared_qa.language_voice_qa_runtime import LanguageVoiceQARuntime

LENSES = ["Meaning", "Fact", "Character", "Relationship", "Certainty", "Timeline", "Canon", "Register", "Role Boundary"]
ORIGINAL = "第一行\n第二行"


def rewrite_output(**overrides):
    value = {
        "decision": "REWRITE DELIVERED", "severity": "LEVEL 3", "route": "Structural Chinese", "mode": "REWRITE MODE", "context_state": "SUFFICIENT",
        "revised_text": "第一行\n修订后的第二行", "benefit_result": "PASS", "rewrite_scope": "第二行", "meaning_lock_status": "PASS",
        "rewrite_ceiling_status": "PASS", "safety_regression": {lens: "PASS" for lens in LENSES}, "contemporary_state": None,
    }
    value.update(overrides)
    return value


def execute(output):
    return LanguageVoiceQARuntime(lambda _invocation: copy.deepcopy(output)).invoke({"original": ORIGINAL, "requested_mode": "REWRITE_EXPLICIT"})


def main() -> int:
    checks = []
    def check(name, callback):
        try:
            callback()
            checks.append((name, "PASS"))
        except Exception as exc:
            checks.append((name, f"FAIL: {type(exc).__name__}: {exc}"))
    check("RW-C01 changed rewrite passes", lambda: assert_success(execute(rewrite_output())))
    check("RW-C02 identical rewrite rejected", lambda: assert_f6(execute(rewrite_output(revised_text=ORIGINAL))))
    check("RW-C03 missing rewrite rejected", lambda: assert_f6(execute(rewrite_output(revised_text=None))))
    check("RW-C04 Benefit FAIL rejected", lambda: assert_f6(execute(rewrite_output(benefit_result="FAIL"))))
    check("RW-C05 Safety failure rejected", lambda: assert_f6(execute(rewrite_output(safety_regression={lens: ("FAIL" if lens == "Meaning" else "PASS") for lens in LENSES}))))
    check("RW-C06 NO CHANGE retains original", lambda: assert_success(execute({"decision":"PASS / NO CHANGE","severity":"LEVEL 0","route":"Early Exit","mode":"QA MODE","context_state":"SUFFICIENT","revised_text":None,"contemporary_state":None})))
    check("RW-C07 notes without rewrite pass", lambda: assert_success(execute({"decision":"PASS WITH NOTES","severity":"LEVEL 1","route":"Natural Expression","mode":"QA MODE","context_state":"SUFFICIENT","revised_text":None,"contemporary_state":None})))
    check("RW-C08 line endings only rejected", lambda: assert_f6(execute(rewrite_output(revised_text="第一行\r\n第二行"))))
    check("RW-C09 outer whitespace only rejected", lambda: assert_f6(execute(rewrite_output(revised_text="  第一行\n第二行\n"))))
    def no_semantic_decision_mutation():
        result = execute(rewrite_output())
        assert result["internal_runtime_result"]["decision"] == "REWRITE DELIVERED"
    check("RW-C10 gate preserves valid QA decision", no_semantic_decision_mutation)
    for name, status in checks:
        print(f"{name}: {status}")
    return 0 if all(status == "PASS" for _, status in checks) else 1


def assert_success(result):
    assert result["internal_runtime_result"]["runtime_status"] == "SUCCESS", result["internal_runtime_result"]


def assert_f6(result):
    assert result["internal_runtime_result"]["failure_code"] == "F6", result["internal_runtime_result"]


if __name__ == "__main__":
    raise SystemExit(main())

