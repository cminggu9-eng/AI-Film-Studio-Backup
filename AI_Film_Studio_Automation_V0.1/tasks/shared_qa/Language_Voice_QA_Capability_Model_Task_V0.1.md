---
type: taskbook
status: completed
version: 0.1
task_id: language-voice-qa-capability-model-v0.1
scope: executable-judgment-architecture-only
created: 2026-08-24
completed: 2026-08-24
---

# Language & Voice QA｜Capability Model 任务书 V0.1

## 授权目标

把已经通过的 Capability Charter 与五人 Cross-Distillation 转译成可执行的
`INPUT → STATE → ROUTE → DETECT → ARBITRATE → DECIDE → OPTIONAL REWRITE → SAFETY CHECK → OUTPUT`
判断架构，作为未来 Production Skill 的唯一方法基线。

## 正式基线

- `01_SKILLS/Shared_QA/Language & Voice QA｜Capability Charter V0.1.md`
- `02_DISTILLATION/方法论/Language & Voice QA｜五人交叉蒸馏 V0.1.md`
- 五份已批准单人蒸馏仅作 Source Provenance / Fallback Reference；不重新蒸馏。

## 必须建立

- Input State、Mode Router、R1–R8 Router、Meaning Lock、Early Exit；
- Detection Ownership、五个核心 Detection Modules、Creator-Room、Term State、Contemporary Handoff；
- Benefit Test、Minimum Necessary Rewrite、九项 Rewrite Safety、Severity 0–5、Output Decision States；
- Capability Stack、有限 Context / Register / Rewrite loops；
- Hard Constraints、Default Heuristics、Conditional Methods、Optional Tools；
- 全部 19 条 Studio-Native Rules 的 model mapping；
- TEST A–L、Static Audit、Wrong-Instruction Stress Test 与 Codex 独立审核。

## 发布及停止约束

1. 依照 `AGENTS.md`、`PUBLISH_RULES.md` 与 `huashu-nuwa` 工作流执行；首稿只能写入 `_STAGING`。
2. 仅审核通过后，使用 `scripts/publish_to_obsidian.py` 发布到
   `01_SKILLS/Shared_QA/Language & Voice QA｜综合能力模型 V0.1.md`。
3. 不得创建 `SKILL.md`、安装 Skill、修改 Runtime、Showrunner、Contemporary Layer、
   Scene Writer、五人 Cross-Distillation、单人蒸馏或项目 Canon。
4. 发布成功后立即停止，等待用户另行授权 Production Skill。
