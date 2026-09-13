# AI Film Studio V0.1 — Showrunner 综合能力模型任务书

## 任务定位

本阶段把六份已批准档案转译为 AI Film Studio 自有的 `SHOWRUNNER CAPABILITY MODEL V0.1`。不重新研究五位创作者，不重新进行人物蒸馏，不生成最终 `Showrunner SKILL.md`，不开始 Scene Writer、Director 或正式剧本开发。

Codex 负责调度、状态审计、审核、发布控制；必要时以 `huashu-nuwa` 做定向交叉抽象；Obsidian Vault 是正式档案；用户是最终决策者。首轮只写入 `runtime/_STAGING/`。

## 核心输入

必须读取并保留 provenance：

1. `02_DISTILLATION/编剧研究/Craig Mazin｜Showrunner能力蒸馏 V0.1.md`
2. `02_DISTILLATION/编剧研究/Vince Gilligan｜Showrunner能力蒸馏 V0.1.md`
3. `02_DISTILLATION/编剧研究/Shonda Rhimes｜Showrunner能力蒸馏 V0.1.md`
4. `02_DISTILLATION/编剧研究/Tony Gilroy｜Showrunner能力蒸馏 V0.1.md`
5. `02_DISTILLATION/编剧研究/David Simon｜Showrunner能力蒸馏 V0.1.md`
6. `02_DISTILLATION/方法论/Showrunner｜五人交叉蒸馏 V0.1.md`

交叉蒸馏档案是主要综合输入；前五份档案用于来源追踪与边界回查。不得把交叉模型的新规则误归因给单个创作者。

## 模型职责边界

Showrunner 是故事系统的最高创作管理层，负责概念、格式、Story Purpose、人物/世界/因果/系列/长篇、信息管理、制作规模、诊断、返工和下游任务定义。不得越权输出最终对白、表演指令、机位、镜头、摄影、视觉设计或最终连戏审计。

## 必须建立的能力

- `INPUT STATE ASSESSMENT`：MODE A 模糊 Idea、B Concept、C 角色/世界、D Series Bible/Season Outline、E Episode Outline、F 剧本返工；标记 LOCKED/APPROVED/DRAFT/UNKNOWN/CONFLICTING。
- Format Fit：短片、短视频、限定剧、连续短剧/漫剧、长篇 Series；不为“做剧”扩写电影故事。
- 八层候选 Decision Stack：Story Purpose、Character Engine、World/System、Causal Story、Series/Episode、Longform、Production Reality、Diagnosis & Rewrite；允许调整但须说明理由。
- `CONFLICT RESOLVER`：`CONTEXT → COMPETING PRINCIPLES → QUESTION → OPTION A/B → TRADEOFF → DECISION CONDITION`。
- 规则四类：HARD CONSTRAINT、DEFAULT HEURISTIC、CONDITIONAL METHOD、OPTIONAL TOOL；硬约束必须少而明确。
- 主流程与回环、STOP/WARNING/BLOCKED 条件、至少十种输出类型、五类下游 Handoff。
- Provenance：五位创作者派生、多源共识、AI Film Studio 自有综合规则。

## 压力测试

必须使用全新原创项目：

- TEST A：6–8 分钟现代都市悬疑连续漫剧，少角色/少地点/强信息差/连续剧情。
- TEST B：无犯罪、无阴谋、无重大社会系统的轻喜剧职场 Series，验证不会强行启动沉重系统与巨大人物弧。
- TEST C：固定建筑内的架空奇幻室内剧，验证“世界内部真实”与 Scope Compression。

另测试六条错误指令：随机杀人、轻喜剧无需因果、系统题材主角选择不重要、AI 做不了就删配角、每三分钟反转、锁定角色与新剧情冲突时直接改角色。

## 输出与发布

首轮只写：`runtime/_STAGING/Showrunner_Capability_Model_V0.1.md`，至少包含任务书指定的 24 个章节（模型使命、职责边界、输入状态模型、格式适配判断、Decision Stack、八层能力、Conflict Resolver、规则优先级、Core Workflow、回环、Stop/Block、输出类型、Downstream Handoff、Provenance、三类测试、错误指令、已知边界、Codex 审核结论）。

审核通过后 frontmatter 必须为：

```yaml
type: capability-model
status: approved
review_result: passed
version: 0.1
subject: AI Film Studio Showrunner
```

使用 `scripts/publish_to_obsidian.py` 发布至：`01_SKILLS/01_Showrunner/Showrunner｜综合能力模型 V0.1.md`。发布失败不得绕过脚本。完成后立即停止；不生成、安装或锁定 `Showrunner SKILL.md`。
