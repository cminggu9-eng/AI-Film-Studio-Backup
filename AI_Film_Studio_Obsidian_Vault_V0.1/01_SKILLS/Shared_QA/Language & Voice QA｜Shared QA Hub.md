---
type: navigation-hub
status: approved
version: 0.1
domain: Language & Voice QA
scope: navigation-lifecycle-lineage
---

# Language & Voice QA｜Shared QA Hub

> 本页是 Shared QA 的导航、生命周期与谱系入口，不包含新的能力规则，不创建未来阶段资产，也不改变任何已发布 V0.1 方法语义。

## 当前生命周期

|阶段|状态|
|---|---|
|Capability Charter|`DONE`|
|Candidate Audit|`DONE`|
|Single Distillation x5|`DONE`|
|Cross-Distillation V0.1|`PASS`|
|Capability Model V0.1|`FROZEN`|
|Production Skill V0.1|`FROZEN`|
|Runtime Integration|`FROZEN`|
|Model Executor Binding|`ACTIVE`|
|DeepSeek Provider|`ACTIVE DEVELOPMENT PROVIDER`|
|Contemporary Language Layer V0.1|`FROZEN`|
|Rewrite Gate|`ACTIVE`|
|Validation Pack|`FROZEN`|
|Human Acceptance|`ACCEPT WITH KNOWN LIMITATIONS — HUMAN ACCEPTED`|
|Scene Writer|`PHASE 1 — CAPABILITY DISCOVERY / DISTILLATION PREPARATION`|

Shared QA 是跨角色质量层，不计入 AI Film Studio 原有六大创作角色。

## 正式资产

### Charter 与候选审计

- [[Language & Voice QA｜Capability Charter V0.1]]
- [[Language & Voice QA｜蒸馏对象选择审计 V0.1]]

### 五名单人正式蒸馏

- [[叶圣陶｜Language & Voice QA 能力蒸馏 V0.1]]
- [[汪曾祺｜Language & Voice QA 能力蒸馏 V0.1]]
- [[老舍｜Language & Voice QA 能力蒸馏 V0.1]]
- [[余光中｜Language & Voice QA 能力蒸馏 V0.1]]
- [[刘震云｜Language & Voice QA 能力蒸馏 V0.1]]

### 综合输出

- [[Language & Voice QA｜五人交叉蒸馏 V0.1]]
- [[Language & Voice QA｜综合能力模型 V0.1]]

### Production Skill

- Canonical Production Skill V0.1：`01_SKILLS/Shared_QA/SKILL.md`（`language-voice-qa`；production-grade、validated、published；V0.1 已冻结）

### Acceptance Closure

- Human Acceptance：`ACCEPT WITH KNOWN LIMITATIONS`；KL-01 / KL-02 为非阻断观察项，不在本轮修复。
- 受控收口记录：`AI_Film_Studio_Automation_V0.1/runtime/_STAGING/_research/Shared_QA_Human_Acceptance_Closure_V0.1/Shared_QA_Human_Acceptance_Record_V0.1.md`

## 谱系

```text
Capability Charter + 五名单人正式蒸馏
  → Five-Person Cross-Distillation V0.1
  → Language & Voice QA Capability Model V0.1
  → Language & Voice QA Production Skill V0.1
```

语义约定：`Sources` 表示方法输入；`Output` 表示受控产物；Hub 只提供 Parent / navigation 入口。Obsidian backlinks 提供反向可导航关系；不对五份单人档案建立全连接。

## 导航元数据边界

本 Hub 与所链接正式资产中的 Relations 区块均为 post-publication navigation metadata：它们不改变 V0.1 capability semantics，不覆写 `runtime/_PUBLISHED` 历史快照，也不构成 Scene Writer Production Skill、Runtime 或未来角色的创建。Shared QA V0.1 已受控冻结；除非用户明确授权，不主动改动其已冻结资产或语义。
