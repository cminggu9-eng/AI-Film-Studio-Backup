# AI Film Studio V0.1 — Language & Voice QA 蒸馏对象选择审计任务书

## 任务定位

本任务依据已批准的 `Language & Voice QA｜Capability Charter V0.1.md`，审核 7 位候选是否适合在未来接受正式能力方法论蒸馏，并从中推荐 4–5 位互补对象。它是候选证据与组合适配审计，不是人物蒸馏。

## 冻结边界

- 禁止调用 `huashu-nuwa` 执行人物蒸馏。
- 禁止创建人物 Distillation、Cross-Distillation、Capability Model、Language & Voice QA Skill 或 Runtime 实现。
- 禁止修改 Showrunner canonical、installed Skill、Capability Model、Runtime 或 production hash。
- Scene Writer 保持 `NOT STARTED`。
- 研究材料只进入 `runtime/_STAGING/_research/Language_Voice_QA_Candidate_Audit_V0.1/`。

## 输入

### 能力章程

`AI_Film_Studio_Obsidian_Vault_V0.1/01_SKILLS/Shared_QA/Language & Voice QA｜Capability Charter V0.1.md`

必须以六个能力槽为选择目标：

- A Natural Modern Chinese
- B Spoken Dialogue
- C Restraint
- D Editing & Syntax
- E Everyday Observation
- F Anti-Rhetoric

候选适配还需服务章程中的 18 类 AI-pattern、Meaning Preservation、Register、Term Plausibility、Theme Language 与 Character Dialogue 边界。

### 候选池

Primary：汪曾祺、老舍、叶圣陶、余光中、刘震云。

Alternates：余华、吕叔湘。

Primary 不是预设通过名单；Alternates 必须按同一标准独立审核。

## 证据规则

每位候选建立 Candidate Evidence Ledger，字段至少包括：

`Candidate / Source / URL / Source Type / First-hand or Secondary / Date / Capability Slot / Relevant Claim / Accessibility / Reliability / Notes`

证据优先级：本人文章、随笔或创作谈 → 本人演讲 → 本人长访谈 → 本人课程或讲稿 → 权威机构转载的本人原文。二手评论只用于导航或交叉核验，不能独立承载候选通过结论。

候选必须回答：可验证一手资料数量、资料类型、主要方法覆盖、来源稳定性、是否足够支撑正式蒸馏。无法访问全文、身份不明、转述无原话或来源链断裂的材料不得计入核心一手数量。

## 审核维度

### Capability Coverage

不能只写 High / Medium / Low；每个评分都必须说明直接证据、可提取方法和限制。最终组合必须覆盖 A–F，且每槽至少一位主责任人。

### 重叠分析

必须检查：

1. 汪曾祺 × 叶圣陶：艺术语言 vs 编辑检查；
2. 老舍 × 刘震云：人物情境语言 vs 现代生活语言；
3. 叶圣陶 × 余光中：意思/修改/通顺 vs 翻译腔/汉语结构；
4. 余光中 × 吕叔湘：规范批评 vs 系统语言诊断；
5. 老舍 × 余华：Dialogue QA 的直接性、证据密度与互补。

### Style Imitation Risk

每位候选标记 LOW / MEDIUM / HIGH，并给出切断方案。不得把候选转成文风、地域口语、幽默、简洁或修辞风格模仿器。

### Modernity Risk

早期候选的方法只提取可迁移判断机制；时代词汇、地域习惯、历史规范不得直接升级为 2026 年现代普通话硬规则。

### Readiness

只有同时满足以下条件才可列入最终推荐：

1. 核心一手证据充分且可核验；
2. 能提取 Input → Judgment → Decision → Output 或等价可执行判断；
3. 对至少一个能力槽提供明确主责任价值；
4. 与组合内其他人不只重复；
5. 风格模仿与现代性风险有可执行护栏。

## 正式输出

### 研究目录

`AI_Film_Studio_Automation_V0.1/runtime/_STAGING/_research/Language_Voice_QA_Candidate_Audit_V0.1/`

研究目录应包含 canonical evidence ledger、coverage matrix、risk/overlap analysis 和 selection rationale。

### Obsidian 审计档案

`AI_Film_Studio_Obsidian_Vault_V0.1/01_SKILLS/Shared_QA/Language & Voice QA｜蒸馏对象选择审计 V0.1.md`

建议 frontmatter：

```yaml
type: candidate-suitability-audit
status: approved
review_result: passed
version: 0.1
subject: Language & Voice QA Distillation Candidates
```

只有证据、覆盖、风险和最终组合全部通过时才能批准。若任一能力槽无主责任人或核心证据不足，保持 draft/pending 并报告 BLOCKED。

## 最终审核门

Codex 必须确认：

1. 7 位候选均按相同证据标准审核；
2. 每位候选的核心一手数量可复算；
3. 所有核心主张可回到本人公开材料；
4. Coverage Matrix 含理由，不只含等级；
5. 五组指定重叠均有结论；
6. 7 位候选均有 Style Imitation Risk；
7. 早期候选均有 Modernity Risk 与迁移护栏；
8. 最终推荐为 4–5 人且覆盖 A–F；
9. 每位最终候选有 Primary/Secondary Capability、必要性、非重复性、Evidence Readiness 与 Risk；
10. Alternate 有明确启用条件；
11. 本轮未产生任何正式人物蒸馏或后续模型/Skill；
12. Showrunner 与 Scene Writer 冻结状态保持。

## 停止条件

审计通过并写入指定档案后立即停止。下一阶段只能在用户明确授权“锁定蒸馏对象并开始第一位人物蒸馏”后启动。

