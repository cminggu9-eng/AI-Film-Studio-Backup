---
type: taskbook
status: completed
version: 0.1
task_id: language-voice-qa-cross-distillation-v0.1
scope: five-person-approved-distillations-only
created: 2026-08-24
completed: 2026-08-24
---

# Language & Voice QA｜五人交叉蒸馏任务书 V0.1

## 目标

以五份已经审批通过的 Language & Voice QA 单人能力蒸馏档案和
`Language & Voice QA｜Capability Charter V0.1` 为唯一正式输入，建立供未来
Capability Model 使用的、Studio-Native 的语言判断架构。

本任务不是人物风格融合，不产出人物人格、文风或模仿指令，也不创建 Capability Model、
Production Skill、Runtime 或任何正式 QA 工具。

## 正式输入

- 叶圣陶、汪曾祺、老舍、余光中、刘震云五份已批准正式蒸馏档案。
- `01_SKILLS/Shared_QA/Language & Voice QA｜Capability Charter V0.1.md`。

## 必须产出

- 五层判断架构与适用边界。
- CONSENSUS / COMPLEMENTARY / OVERLAP / CONDITIONAL TENSION / TRUE CONFLICT 矩阵。
- Charter AP-01 至 AP-18 的 Primary Owner、Secondary Signal、Handoff Target。
- Register Router（R1–R8）、早退/NO CHANGE、收益检验、改写上限、严重度仲裁、
 术语与抽象处理、对话整合路径、当代语言交接及角色边界。
- 12–20 条含 RULE ID、TRIGGER、QUESTION、DECISION、ALLOWED ACTION、
  PROHIBITED ACTION、SOURCE MAP 的 Studio-Native 规则。
- 指定 Cross-Challenge、Big Boss、False Positive、Anti-Mechanical 和 Rewrite Safety 测试记录。

## 流程与发布约束

1. 必须遵循 `AGENTS.md`、`PUBLISH_RULES.md` 与已安装 `huashu-nuwa` Skill。
2. 首轮完整结果仅可写入 `runtime/_STAGING`，并保留来源映射和女娲调用记录。
3. Codex 独立审核必须确认：不融合人物、不把条件方法变成硬规则、不制造冲突、
   不越过 QA 角色边界，并且测试通过。
4. 仅当审核结论为 approved / passed 时，使用
   `scripts/publish_to_obsidian.py` 发布到
   `02_DISTILLATION/方法论/Language & Voice QA｜五人交叉蒸馏 V0.1.md`。
5. 发布后验证正式档案、归档和工作日志；随后立即停止。

## 明确禁止

- 修改五份单人正式蒸馏档案、Capability Charter、任何现有 Skill 或 Showrunner 资产。
- 自动开始 Language & Voice QA Capability Model、QA Skill、Runtime、
  Contemporary Language Layer 或 Scene Writer。
- 将未经审核的内容直接写入 Obsidian 正式区域。
