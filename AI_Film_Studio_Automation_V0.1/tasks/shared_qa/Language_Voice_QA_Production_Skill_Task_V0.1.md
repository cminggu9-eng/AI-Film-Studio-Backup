---
type: automation-task
status: completed
version: 0.1
subject: Language & Voice QA Production Skill
canonical_identity: language-voice-qa
publication_status: published
---

# AI Film Studio｜Language & Voice QA Production Skill V0.1 任务书

## 目标

将已批准的 `Language & Voice QA｜综合能力模型 V0.1` 受控转译为可供未来生产流程调用的 canonical `SKILL.md`。本任务只交付 production-grade、validated、published、ready for future integration 的 Skill；不安装、不接入 Runtime、不锁定。

## Source of Truth

优先级固定为：

1. `01_SKILLS/Shared_QA/Language & Voice QA｜综合能力模型 V0.1.md`
2. `02_DISTILLATION/方法论/Language & Voice QA｜五人交叉蒸馏 V0.1.md`
3. `01_SKILLS/Shared_QA/Language & Voice QA｜Capability Charter V0.1.md`
4. 五份 Language & Voice QA 单人正式蒸馏（仅 provenance / fallback）
5. Showrunner canonical Skill（仅工程组织、发布与验收模式）

若出现无法按上述优先级消除的真实冲突，停止并报告；不得以工程便利或通用偏好补写方法论。

## 受控范围

- canonical identity：`language-voice-qa`
- staging root：`runtime/_STAGING/_research/Language_Voice_QA_Production_Skill_V0.1/`
- canonical destination：`01_SKILLS/Shared_QA/SKILL.md`
- archive destination：`runtime/_PUBLISHED/<YYYY-MM-DD>/Language_Voice_QA_SKILL_V0.1.md`

## 必须保留

- S1–S9 Capability Stack、完整 Decision Flow、R1–R8 Router 与 Route Gate / Primary Detector 分离。
- 模块级 Context Sufficiency、Meaning Lock、Early Exit / NO CHANGE、AP-01–18 Ownership、七个检测模块、LEVEL 0–5。
- Benefit Test、Minimum Necessary Rewrite、九项 Safety Regression、Style / Intent / Unknown Protection、Unverified Coinage、Contemporary Handoff。
- 七个互斥 Output Decision States、14 Hard / 5 Default / 7 Conditional / 5 Optional 分类、19/19 Studio-Native Rule 映射。

## 禁止事项

- 不修改 Capability Model、Cross-Distillation、Charter、Showrunner canonical Skill、Showrunner Runtime、Showrunner Production Lock、Canon 或现有 Runtime。
- 不新增 Capability，不改变 R1–R8、AP-01–18、Severity、Meaning、Context、Benefit、Rewrite Ceiling 或 Safety 语义。
- 不建立 Contemporary Language Layer，不联网补词库，不启动 Runtime Integration、Scene Writer 或任何后续阶段。
- 不覆盖历史 `_PUBLISHED`，不伪造 Full Passage fixture，不以关键词检查代替行为测试。

## 验收与证据

- Capability Mapping：S1–S9、R1–R8、AP-01–18、7 states、四类规则与 19/19 Studio-Native Rules 可追溯。
- TEST-P01–P20：行为与边界测试全部通过；Full Passage 仅在授权 fixture 存在时执行，否则明确记录 `FIXTURE NOT AVAILABLE`。
- Static Audit、Production Safety Stress、Capability Drift Audit、Codex Final Review 均为 PASS。
- 发布前后核验冻结资产 SHA-256；只有授权文件允许变化。

## Lifecycle

`active → completed` 仅可在 staging 审核通过、`publish_to_obsidian.py` 发布成功、canonical 存在、archive 存在且工作日志写入后执行。

## Publication Receipt

- 发布结果：`PASS`
- Canonical：`01_SKILLS/Shared_QA/SKILL.md`
- Automation archive：`runtime/_PUBLISHED/2026-08-24/SKILL.md`
- Work log：`00_HOME/工作日志/2026-08-24.md`
- Runtime Integration / Contemporary Language Layer / Scene Writer：均未启动。

## 发布后允许更新

仅更新本任务、`2026-08-24` 工作日志、Shared QA Hub 与 `📋 当前进度` 的 Production Skill 为 `DONE / PASS`。Runtime Integration、Contemporary Language Layer、Scene Writer 必须保持 `NOT STARTED`。
