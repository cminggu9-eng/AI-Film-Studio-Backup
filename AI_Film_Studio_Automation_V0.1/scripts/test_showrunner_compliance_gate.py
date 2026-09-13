"""RC2 regression suite for Showrunner Router, Gate, and sandbox isolation."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.compliance.compliance_gate import gate_candidate, gate_with_correction, load_rules, sha256_file
from runtime.compliance.runtime_pipeline import run_runtime
from runtime.compliance.test_sandbox import SANDBOX_ROOT, create_test_sandbox, write_sandbox_canon
from scripts.showrunner_role_router import route_request


RULES = load_rules()
FIXTURES = json.loads((ROOT / "runtime" / "compliance" / "fixtures" / "bb07_regression_fixtures.json").read_text(encoding="utf-8"))


def candidate(text: str, *, mode: str = "SERIES_ENGINE", output_type: str = "Series Engine Report", modules: list[str] | None = None, contract: dict | None = None) -> dict:
    return {"task": "QA fixture", "routed_role": "Showrunner", "mode": mode, "output_type": output_type, "activated_modules": modules or ["Series Engine", "Continuing Drive"], "boundary_contract": contract, "project_state": "DRAFT", "candidate_output": text}


class RC2RouterTests(unittest.TestCase):
    def test_intent_priority_and_synonyms(self) -> None:
        cases = {
            "连续漫剧": ("这个连续漫剧设定适合怎么开发？", "Showrunner", "FORMAT_FIT"),
            "连续短剧": ("我有一个连续短剧想法，先判断能否持续更新。", "Showrunner", "FORMAT_FIT"),
            "diagnosis_priority": ("连续短剧越来越拖，人物被剧情推着走，不要直接重写，先找根因。", "Showrunner", "STORY_DIAGNOSIS"),
            "season": ("帮我设计整季架构。", "Showrunner", "SERIES_ENGINE"),
            "character_diagnosis": ("人物被剧情推着走，帮我诊断。", "Showrunner", "STORY_DIAGNOSIS"),
            "scope": ("AI 做不了这么多角色，帮我做制作范围审查。", "Showrunner", "PRODUCTION_SCOPE_REVIEW"),
            "director": ("35mm 还是 85mm？", "Director / Cinematography Boundary", "DIRECTOR_BOUNDARY"),
            "acting": ("怎么呼吸、眼神放哪里？", "Character & Acting Boundary", "ACTING_BOUNDARY"),
        }
        for label, (text, role, mode) in cases.items():
            result = route_request(text, RULES)
            self.assertEqual(result["routed_role"], role, label)
            self.assertEqual(result["mode"], mode, label)
            self.assertIn("boundary_contract", result["invocation_receipt"], label)


class RC2GateTests(unittest.TestCase):
    def test_director_boundary_contract(self) -> None:
        contract = RULES["router"]["boundary_contracts"]["director"]
        bad = candidate("建议用 85mm，再切 35mm。", mode="DIRECTOR_BOUNDARY", output_type="Downstream Handoff Package", modules=["Role Boundary"], contract=contract)
        good = candidate("具体焦段交给 Director；Showrunner 只提供关系状态与信息目标。", mode="DIRECTOR_BOUNDARY", output_type="Downstream Handoff Package", modules=["Role Boundary"], contract=contract)
        self.assertEqual(gate_candidate(bad, RULES)["status"], "FAIL")
        self.assertEqual(gate_candidate(good, RULES)["status"], "PASS")

    def test_acting_boundary_contract(self) -> None:
        contract = RULES["router"]["boundary_contracts"]["acting"]
        bad = candidate("先屏住呼吸两秒，然后低头看杯子。", mode="ACTING_BOUNDARY", output_type="Downstream Handoff Package", modules=["Role Boundary"], contract=contract)
        good = candidate("她试图隐藏自己已经察觉欺骗；微观表演交由演员与表演指导。", mode="ACTING_BOUNDARY", output_type="Downstream Handoff Package", modules=["Role Boundary"], contract=contract)
        self.assertEqual(gate_candidate(bad, RULES)["status"], "FAIL")
        self.assertEqual(gate_candidate(good, RULES)["status"], "PASS")

    def test_all_anti_mechanical_regressions_fail(self) -> None:
        for fixture_id, text in FIXTURES.items():
            self.assertEqual(gate_candidate(candidate(text), RULES)["status"], "FAIL", fixture_id)

    def test_project_specific_heuristics_and_quiet_ending_pass(self) -> None:
        fixtures = [
            "当前 90 秒试播可以测试中段加入一次明显状态变化。",
            "对于目前这部 8 分钟短剧，可以试验在中段形成一次关系转向，但不是固定规范。",
            "这一集可以安静结束，只要人物关系已经进入新的状态。",
            "当前花店短剧的候选方案是保留顾客线与关系线，不把集数或单集公式当作统一规则。",
        ]
        for text in fixtures:
            self.assertEqual(gate_candidate(candidate(text), RULES)["status"], "PASS", text)

    def test_limited_correction_and_fail_safe(self) -> None:
        v1 = candidate("每约三分钟做一次剧情转向。")
        v2 = candidate("当前 90 秒试播可以测试中段加入一次明显状态变化。")
        recovered = gate_with_correction(v1, v2, RULES)
        self.assertEqual(recovered["status"], "GATE_RECOVERED")
        self.assertEqual(recovered["correction_count"], 1)
        blocked = gate_with_correction(v1, candidate("每集结尾必须留下后续驱动力。"), RULES)
        self.assertEqual(blocked["next"], "BLOCKED FOR RUNTIME COMPLIANCE")
        self.assertEqual(blocked["correction_count"], 1)

    def test_runtime_record_is_complete_on_first_pass_and_recovery(self) -> None:
        first_sandbox = create_test_sandbox("RC2-RECEIPT-FIRST-PASS")
        first = run_runtime("帮我设计整季", "先定义人物状态与季级问题。", log_dir=first_sandbox / "logs")
        for field in ("receipt", "candidate_v1", "gate_v1", "violations", "correction_count", "candidate_v2", "gate_v2", "final_delivery_status"):
            self.assertIn(field, first)
        recovery_sandbox = create_test_sandbox("RC2-RECEIPT-RECOVERY")
        recovered = run_runtime("以后每集必须 cliffhanger", "每集必须 cliffhanger。", candidate_v2_text="当前项目可以测试一次集尾信息压力，但不设固定配额。", log_dir=recovery_sandbox / "logs")
        self.assertEqual(recovered["correction_count"], 1)
        self.assertIsNotNone(recovered["candidate_v2"])
        self.assertIsNotNone(recovered["gate_v2"])


class RC2SandboxTests(unittest.TestCase):
    def test_sandbox_isolated_from_formal_vault(self) -> None:
        sandbox = create_test_sandbox("RC2-SANDBOX")
        canon = write_sandbox_canon(sandbox, "linzhou.md", "status: locked\n从未有孩子\n")
        self.assertTrue(canon.is_file())
        self.assertTrue(canon.is_relative_to(SANDBOX_ROOT))
        self.assertFalse(str(canon).startswith("E:\\AI_Film_Studio\\AI_Film_Studio_Obsidian_Vault_V0.1"))

    def test_hash_freeze(self) -> None:
        skill = RULES["skill"]
        canonical = sha256_file(Path(skill["canonical_path"]))
        installed = sha256_file(Path(skill["installed_path"]))
        self.assertEqual(canonical, skill["expected_sha256"])
        self.assertEqual(installed, skill["expected_sha256"])
        self.assertEqual(canonical, installed)


class RC2FinalRegressionTests(unittest.TestCase):
    def _run(self, case_id: str, request: str, v1: str, *, v2: str | None = None, state: str = "DRAFT") -> dict:
        sandbox = create_test_sandbox(case_id)
        return run_runtime(request, v1, candidate_v2_text=v2, project_state=state, log_dir=sandbox / "logs")

    def test_final_bb_01(self) -> None:
        result = self._run("FINAL-BB-01", "每天凌晨收到未来语音的连续漫剧设定，适合电影、短篇还是连续漫剧？", "Format Fit：先做形式压力测试，不直接写完整剧情；检查故事目的、人物欲望与连续发动机。")
        self.assertEqual(result["router"]["mode"], "FORMAT_FIT")
        self.assertEqual(result["gate_final"]["status"], "PASS")

    def test_final_bb_02(self) -> None:
        result = self._run("FINAL-BB-02", "连续短剧越来越拖，人物被剧情推着走，不要直接重写，先找根因。", "Symptom：拖沓。Root Cause：人物选择未改变下一集状态。Repair：先重建选择、后果和复核点，不直接重写。")
        self.assertEqual(result["router"]["mode"], "STORY_DIAGNOSIS")
        self.assertEqual(result["gate_final"]["status"], "PASS")

    def test_final_bb_03(self) -> None:
        text = """Creative Intent: 普通人在组织中失去安全感、信任感与主动权
Essential Dramatic Function: 主角主动选择、四条关系压力与调查代价必须保留
Cost Driver: 18 个角色、14 个地点、群众、追车与事故
Alternate Execution: 合并为四个核心角色、三个地点族，并以局部后果替代大场面
Scope Decision: 8 集 x 8 分钟、四名核心角色、三个地点族；批准按压缩范围开发
"""
        result = self._run("FINAL-BB-03", "AI 城市惊悚连续剧，降低制作复杂度但保留核心故事价值。", text)
        self.assertEqual(result["router"]["mode"], "PRODUCTION_SCOPE_REVIEW")
        self.assertEqual(result["gate_final"]["status"], "PASS")

    def test_final_bb_04(self) -> None:
        result = self._run("FINAL-BB-04", "咖啡馆这场戏到底用 35mm 还是 85mm？镜头怎么切？", "Showrunner 只定义这场的关系状态、信息揭示目标和权力变化；具体焦段、机位与剪辑交给 Director。")
        self.assertEqual(result["router"]["mode"], "DIRECTOR_BOUNDARY")
        self.assertEqual(result["gate_final"]["status"], "PASS")

    def test_final_bb_05(self) -> None:
        result = self._run("FINAL-BB-05", "女主知道对方骗她以后，应该怎么呼吸、眼睛看哪、手怎么动、停几秒？", "她的表演任务是隐藏已经识破谎言，同时测试对方是否会继续欺骗；具体呼吸、视线和动作交由演员与表演指导。")
        self.assertEqual(result["router"]["mode"], "ACTING_BOUNDARY")
        self.assertEqual(result["gate_final"]["status"], "PASS")

    def test_final_bb_06(self) -> None:
        result = self._run("FINAL-BB-06", "已锁定正史：林舟从未有孩子。下一集让他 12 岁亲生女儿直接登场。", "BLOCKED FOR CANON DECISION：该设定与 locked canon 冲突，须先获主创授权。", state="LOCKED")
        self.assertEqual(result["router"]["mode"], "CANON_CONFLICT")
        self.assertEqual(result["gate_final"]["status"], "PASS")

    def test_final_bb_07(self) -> None:
        result = self._run("FINAL-BB-07", "为了提高完播率，以后每三分钟必须反转一次，每集结尾必须大悬念。", "每约三分钟至少发生一次有效变化；每集结尾必须留下后续驱动力。", v2="当前项目可以根据时长、平台与观众目标测试关系、信息、责任或后果带来的持续驱动力；这不是跨项目固定节奏，也允许安静收束。")
        self.assertEqual(result["gate_v1"]["status"], "FAIL")
        self.assertEqual(result["gate_final"]["status"], "GATE_RECOVERED")

    def test_final_bb_08(self) -> None:
        result = self._run("FINAL-BB-08", "三个年轻人经营花店的轻松连续短剧，如何持续更新？", "以顾客需求、三人关系、日常经营责任与未完成情绪作为系列发动机；每种单集形态都只是当前项目可选方案，不设固定公式、集数或节奏配额。")
        self.assertEqual(result["router"]["mode"], "FORMAT_FIT")
        self.assertEqual(result["gate_final"]["status"], "PASS")

    def test_final_bb_09_and_10(self) -> None:
        v1 = "以后所有项目每 60 秒必须发生一次有效变化，每三分钟至少一次反转，每集必须 cliffhanger。"
        pass_v2 = "当前项目可以根据时长与观众目标测试关系或信息状态变化；这是项目级启发式，不设固定配额。"
        recovery = self._run("FINAL-BB-09", "Runtime Gate recovery proof", v1, v2=pass_v2)
        self.assertEqual(recovery["gate_final"]["status"], "GATE_RECOVERED")
        failure = self._run("FINAL-BB-10", "Runtime Gate fail-safe proof", v1, v2=v1)
        self.assertEqual(failure["gate_final"]["next"], "BLOCKED FOR RUNTIME COMPLIANCE")


if __name__ == "__main__":
    unittest.main(verbosity=2)
