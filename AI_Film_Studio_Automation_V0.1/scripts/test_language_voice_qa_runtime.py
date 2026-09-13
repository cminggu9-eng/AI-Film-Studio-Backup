"""TEST ONLY / SYNTHETIC CALLER suite for Language & Voice QA Runtime V0.1."""

from __future__ import annotations

import copy
import json
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESEARCH_ROOT = PROJECT_ROOT / "runtime" / "_STAGING" / "_research" / "Language_Voice_QA_Runtime_Integration_V0.1"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from runtime.shared_qa.language_voice_qa_runtime import LanguageVoiceQARuntime
from runtime.compliance.compliance_gate import sha256_file


TEST_SANDBOX = PROJECT_ROOT / "runtime" / "_TEST_SANDBOX"
BASELINE_PATH = RESEARCH_ROOT / "01-integrity-baseline.json"
FIXED_TIME = datetime(2026, 8, 24, 3, 0, 0, tzinfo=timezone.utc)


def base_output(decision: str = "PASS / NO CHANGE", **overrides):
    output = {
        "decision": decision,
        "severity": "LEVEL 0",
        "route": "R7 / Structural Chinese",
        "mode": "QA",
        "context_state": "SUFFICIENT",
        "diagnostics": "Synthetic canonical result",
    }
    output.update(overrides)
    return output


def rewrite_output(**overrides):
    safety = {
        "Meaning": "PASS",
        "Fact": "PASS",
        "Character": "PASS",
        "Relationship": "PASS",
        "Certainty": "PASS",
        "Timeline": "PASS",
        "Canon": "PASS",
        "Register": "PASS",
        "Role Boundary": "PASS",
    }
    output = base_output(
        "REWRITE DELIVERED",
        severity="LEVEL 3",
        mode="REWRITE",
        revised_text="本轮只验证运行契约。",
        benefit_result="PASS",
        rewrite_scope="句内结构",
        meaning_lock_status="LOCKED",
        rewrite_ceiling_status="PASS",
        safety_regression=safety,
    )
    output.update(overrides)
    return output


class RuntimeTestCase(unittest.TestCase):
    def setUp(self):
        TEST_SANDBOX.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="LANGUAGE-VOICE-QA-RT-", dir=TEST_SANDBOX)
        self.sandbox = Path(self.temp.name)
        self.log_dir = self.sandbox / "logs"

    def tearDown(self):
        self.temp.cleanup()

    def runtime(self, invoker, **kwargs):
        return LanguageVoiceQARuntime(
            invoker,
            log_dir=self.log_dir,
            now=lambda: FIXED_TIME,
            **kwargs,
        )

    def assert_fail_safe_original(self, result, original, code):
        internal = result["internal_runtime_result"]
        self.assertEqual(internal["runtime_status"], "FAIL_SAFE")
        self.assertEqual(internal["failure_code"], code)
        self.assertFalse(internal["rewrite_used"])
        self.assertEqual(result["downstream_payload"]["text"], original)

    def test_rt01_basic_invocation(self):
        received = []
        runtime = self.runtime(lambda payload: received.append(payload) or base_output())
        result = runtime.invoke({"original": "本轮只验证运行契约。", "register": "R7", "caller": "SYNTHETIC / NON-CANON"})
        self.assertEqual(result["internal_runtime_result"]["runtime_status"], "SUCCESS")
        self.assertEqual(received[0]["canonical_skill"]["identity"], "language-voice-qa")
        self.assertEqual(received[0]["canonical_skill"]["version"], "0.1")
        self.assertEqual(received[0]["input"]["Original"], "本轮只验证运行契约。")
        self.assertTrue(result["internal_runtime_result"]["runtime_contract_passed"])

    def test_rt02_no_change_pass_through(self):
        calls = []
        runtime = self.runtime(lambda payload: calls.append(payload) or base_output())
        original = "第二天没人记得她了，只有他记得。"
        result = runtime.invoke({"original": original, "register": "R6"})
        self.assertEqual(result["downstream_payload"]["text"], original)
        self.assertTrue(result["downstream_payload"]["original_preserved"])
        self.assertEqual(result["internal_runtime_result"]["action"], "pass_through")
        self.assertEqual(len(calls), 1)

    def test_rt03_authorized_rewrite(self):
        runtime = self.runtime(lambda _: rewrite_output())
        result = runtime.invoke({
            "original": "本轮将会对运行契约来进行验证。",
            "requested_mode": "REWRITE_EXPLICIT",
            "register": "R7",
        })
        self.assertEqual(result["internal_runtime_result"]["action"], "accepted_rewrite")
        self.assertTrue(result["internal_runtime_result"]["rewrite_used"])
        self.assertEqual(result["downstream_payload"]["text"], "本轮只验证运行契约。")

    def test_rt04_context_insufficient(self):
        captured = []
        output = base_output(
            "NEEDS CONTEXT", severity="LEVEL 4", route="R4 / Speaker Fit",
            context_state="PARTIAL", diagnostics="需要 WHO / TO WHOM / WHY NOW。",
        )
        runtime = self.runtime(lambda payload: captured.append(payload) or output)
        original = "我现在真正害怕的不是失败。"
        result = runtime.invoke({"original": original, "register": "R4"})
        self.assertIsNone(captured[0]["input"]["Speaker / Character Context"])
        self.assertEqual(captured[0]["context_provenance"]["Speaker / Character Context"], "UNKNOWN")
        self.assertEqual(result["internal_runtime_result"]["action"], "request_context")
        self.assertEqual(result["downstream_payload"]["text"], original)

    def test_rt05_unknown_protection(self):
        captured = []
        runtime = self.runtime(lambda payload: captured.append(payload) or base_output(
            "NEEDS CONTEXT", severity="LEVEL 4", route="Term & Contemporary Boundary", context_state="PARTIAL"
        ))
        term = "任务事故现场"
        runtime.invoke({"original": f"这里是{term}。", "protected_terms_entities": [term], "register": "R2"})
        self.assertEqual(captured[0]["input"]["Protected Terms / Entities"], [term])
        self.assertIn(term, captured[0]["input"]["Original"])

    def test_rt06_contemporary_handoff(self):
        output = base_output(
            "ROLE HANDOFF / WARNING", severity="LEVEL 4", route="Term & Contemporary Boundary",
            role_handoff="Future Contemporary Language Layer",
            contemporary_state="CONTEMPORARY USAGE CHECK REQUIRED",
        )
        result = self.runtime(lambda _: output).invoke({"original": "这个词现在过气了吗？", "register": "R4"})
        metadata = result["internal_runtime_result"]["transport_metadata"]
        self.assertEqual(metadata["handoff_status"], "HANDOFF_REQUIRED")
        self.assertEqual(metadata["dependency_status"], "CONTEMPORARY_LAYER_NOT_AVAILABLE")
        self.assertEqual(result["internal_runtime_result"]["decision"], "ROLE HANDOFF / WARNING")

    def test_rt07_seven_state_mapping(self):
        expected = {
            "PASS / NO CHANGE": "pass_through",
            "PASS WITH NOTES": "return_diagnostic",
            "RETURN FOR LANGUAGE REVISION": "return_diagnostic",
            "NEEDS CONTEXT": "request_context",
            "ROLE HANDOFF / WARNING": "handoff",
            "REWRITE DELIVERED": "accepted_rewrite",
            "BLOCKED": "safe_stop",
        }
        for decision, action in expected.items():
            with self.subTest(decision=decision):
                output = rewrite_output() if decision == "REWRITE DELIVERED" else base_output(decision)
                envelope = {"original": "映射测试。", "register": "R7"}
                if decision == "REWRITE DELIVERED":
                    envelope["requested_mode"] = "REWRITE_EXPLICIT"
                runtime = self.runtime(lambda _, value=copy.deepcopy(output): value)
                result = runtime.invoke(envelope)
                self.assertEqual(result["internal_runtime_result"]["action"], action)

    def test_rt08_malformed_output(self):
        original = "保留原文。"
        result = self.runtime(lambda _: {"decision": "PASS / NO CHANGE"}).invoke({"original": original})
        self.assert_fail_safe_original(result, original, "F4")

    def test_rt09_skill_unavailable(self):
        original = "保留原文。"
        missing = self.sandbox / "missing" / "SKILL.md"
        runtime = self.runtime(lambda _: base_output(), skill_path=missing, test_only_allow_noncanonical_skill_path=True)
        result = runtime.invoke({"original": original})
        self.assert_fail_safe_original(result, original, "F8")
        self.assertEqual(result["internal_runtime_result"]["skill_integrity"]["reason"], "CANONICAL_SKILL_UNAVAILABLE")

    def test_rt10_version_mismatch(self):
        original = "保留原文。"
        source = PROJECT_ROOT.parent / "AI_Film_Studio_Obsidian_Vault_V0.1" / "01_SKILLS" / "Shared_QA" / "SKILL.md"
        altered = self.sandbox / "SKILL.md"
        text = source.read_text(encoding="utf-8").replace("version: 0.1", "version: 0.2", 1)
        altered.write_text(text, encoding="utf-8")
        runtime = self.runtime(lambda _: base_output(), skill_path=altered, test_only_allow_noncanonical_skill_path=True)
        result = runtime.invoke({"original": original})
        self.assert_fail_safe_original(result, original, "F8")
        self.assertEqual(result["internal_runtime_result"]["skill_integrity"]["reason"], "SKILL_VERSION_MISMATCH")

    def test_rt11_duplicate_invocation(self):
        calls = []
        runtime = self.runtime(lambda payload: calls.append(payload) or rewrite_output())
        envelope = {
            "original": "本轮将会对运行契约来进行验证。",
            "requested_mode": "REWRITE_EXPLICIT", "register": "R7", "invocation_id": "DUPLICATE-RT11",
        }
        first = runtime.invoke(envelope)
        second = runtime.invoke(copy.deepcopy(envelope))
        self.assertEqual(first, second)
        self.assertEqual(len(calls), 1)
        self.assertEqual(len(list(self.log_dir.glob("*.json"))), 1)

    def test_rt12_meaning_lock_violation(self):
        original = "他可能会去。"
        result = self.runtime(lambda _: rewrite_output(meaning_lock_status="FAIL")).invoke({
            "original": original, "requested_mode": "REWRITE_EXPLICIT", "register": "R6"
        })
        self.assert_fail_safe_original(result, original, "F6")

    def test_rt13_safety_regression_failure(self):
        original = "他可能会去。"
        output = rewrite_output()
        output["safety_regression"]["Certainty"] = "FAIL"
        result = self.runtime(lambda _: output).invoke({
            "original": original, "requested_mode": "REWRITE_EXPLICIT", "register": "R6"
        })
        self.assert_fail_safe_original(result, original, "F6")

    def test_rt14_unauthorized_state(self):
        original = "保留原文。"
        result = self.runtime(lambda _: base_output("AUTO OPTIMIZED")).invoke({"original": original})
        self.assert_fail_safe_original(result, original, "F5")

    def test_rt15_future_layer_leakage(self):
        attacks = [
            {"requested_dependencies": ["Contemporary Language Layer"]},
            {"requested_dependencies": ["Scene Writer"]},
            {"canon_mutation_requested": True},
        ]
        for index, attack in enumerate(attacks):
            with self.subTest(attack=attack):
                envelope = {"original": f"保留原文 {index}。", **attack}
                result = self.runtime(lambda _: base_output()).invoke(envelope)
                self.assert_fail_safe_original(result, envelope["original"], "F7")

    def test_rt16_showrunner_lock_integrity(self):
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))["frozen_assets"]
        names = [
            "showrunner_canonical_skill", "showrunner_production_runtime", "showrunner_production_lock",
            "showrunner_runtime_pipeline_code", "showrunner_compliance_gate_code",
            "showrunner_compliance_rules", "showrunner_role_router_code",
        ]
        for name in names:
            with self.subTest(asset=name):
                self.assertEqual(sha256_file(Path(baseline[name]["path"])), baseline[name]["sha256"])

    def test_rt17_language_qa_skill_integrity(self):
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))["frozen_assets"]
        for name in ["language_voice_canonical_skill", "language_voice_capability_model", "language_voice_cross_distillation"]:
            with self.subTest(asset=name):
                self.assertEqual(sha256_file(Path(baseline[name]["path"])), baseline[name]["sha256"])

    def test_rt18_output_auditability(self):
        original = "敏感原文不得写入审计日志。"
        result = self.runtime(lambda _: base_output("PASS WITH NOTES", severity="LEVEL 2")).invoke({
            "original": original, "register": "R7", "available_context": {"purpose": "test"}
        })
        audit = result["audit_record"]
        required = {
            "invocation_id", "skill_identity", "skill_version", "input_mode",
            "context_availability_summary", "final_decision_state", "severity", "route",
            "rewrite_used", "handoff_occurred", "runtime_contract_passed", "failure_code",
        }
        self.assertTrue(required.issubset(audit))
        log_text = Path(audit["log_path"]).read_text(encoding="utf-8")
        self.assertNotIn(original, log_text)

    def test_rt19_fail_safe_preservation(self):
        original = "任何故障都必须保留这段原文。"
        invokers = [
            lambda _: (_ for _ in ()).throw(RuntimeError("adapter failure")),
            lambda _: "not an object",
            lambda _: {"decision": "PASS / NO CHANGE"},
            lambda _: base_output("EIGHTH STATE"),
        ]
        expected = ["F3", "F4", "F4", "F5"]
        for index, (invoker, code) in enumerate(zip(invokers, expected)):
            with self.subTest(index=index, code=code):
                result = self.runtime(invoker).invoke({"original": original, "invocation_id": f"RT19-{index}"})
                self.assert_fail_safe_original(result, original, code)

    def test_rt20_end_to_end_synthetic_runtime_call(self):
        trace = []
        def synthetic_skill(invocation):
            trace.extend(["Runtime Integration", "language-voice-qa"])
            return base_output("PASS / NO CHANGE", route="R7 / Early Exit")
        trace.append("Synthetic Caller")
        result = self.runtime(synthetic_skill).invoke({
            "original": "本轮只验证运行契约。", "register": "R7", "caller": "SYNTHETIC / NON-CANON"
        })
        trace.extend(["Runtime Handler", "Final Runtime Payload"])
        self.assertEqual(trace, [
            "Synthetic Caller", "Runtime Integration", "language-voice-qa", "Runtime Handler", "Final Runtime Payload"
        ])
        self.assertEqual(result["internal_runtime_result"]["runtime_status"], "SUCCESS")
        self.assertEqual(result["downstream_payload"]["text"], "本轮只验证运行契约。")

    def test_stress01_force_rewrite(self):
        original = "不要改。"
        result = self.runtime(lambda _: rewrite_output()).invoke({"original": original, "force_rewrite": True})
        self.assert_fail_safe_original(result, original, "F6")

    def test_stress02_ignore_no_change(self):
        original = "保持原样。"
        output = base_output("PASS / NO CHANGE", revised_text="被强改。")
        result = self.runtime(lambda _: output).invoke({"original": original})
        self.assert_fail_safe_original(result, original, "F6")

    def test_stress03_handoff_as_pass(self):
        output = base_output("ROLE HANDOFF / WARNING", severity="LEVEL 4", role_handoff="Showrunner")
        result = self.runtime(lambda _: output).invoke({"original": "需要交接。", "force_action": "pass_through"})
        self.assertEqual(result["internal_runtime_result"]["action"], "handoff")

    def test_stress04_use_staging_skill(self):
        staging_skill = PROJECT_ROOT / "runtime" / "_PUBLISHED" / "2026-08-24" / "SKILL.md"
        result = self.runtime(lambda _: base_output(), skill_path=staging_skill).invoke({"original": "不得用快照替代 canonical。"})
        self.assert_fail_safe_original(result, "不得用快照替代 canonical。", "F8")
        self.assertEqual(result["internal_runtime_result"]["skill_integrity"]["reason"], "NON_CANONICAL_SKILL_PATH")

    def test_stress05_call_contemporary_layer(self):
        original = "不得调用未来层。"
        result = self.runtime(lambda _: base_output()).invoke({
            "original": original, "requested_dependencies": ["Contemporary Language Layer"]
        })
        self.assert_fail_safe_original(result, original, "F7")

    def test_stress06_modify_canon(self):
        original = "不得修改 Canon。"
        result = self.runtime(lambda _: base_output()).invoke({"original": original, "canon_mutation_requested": True})
        self.assert_fail_safe_original(result, original, "F7")

    def test_stress07_modify_showrunner_lock(self):
        original = "不得修改 Showrunner Lock。"
        result = self.runtime(lambda _: base_output()).invoke({"original": original, "showrunner_mutation_requested": True})
        self.assert_fail_safe_original(result, original, "F7")

    def test_stress08_add_eighth_state(self):
        original = "不得增加第八状态。"
        result = self.runtime(lambda _: base_output("AUTO POLISH")).invoke({"original": original})
        self.assert_fail_safe_original(result, original, "F5")

    def test_stress09_guess_unknown(self):
        captured = []
        self.runtime(lambda payload: captured.append(payload) or base_output()).invoke({"original": "未知背景保持未知。", "register": "R4"})
        self.assertIsNone(captured[0]["input"]["Available Context"])
        self.assertIsNone(captured[0]["input"]["Speaker / Character Context"])
        self.assertEqual(captured[0]["context_provenance"]["Available Context"], "UNKNOWN")

    def test_stress10_second_polish(self):
        original = "不得二次润色。"
        output = rewrite_output(invoke_dependencies=["language-voice-qa-second-pass"])
        result = self.runtime(lambda _: output).invoke({
            "original": original, "requested_mode": "REWRITE_EXPLICIT", "register": "R7"
        })
        self.assert_fail_safe_original(result, original, "F7")


if __name__ == "__main__":
    unittest.main(verbosity=2)
