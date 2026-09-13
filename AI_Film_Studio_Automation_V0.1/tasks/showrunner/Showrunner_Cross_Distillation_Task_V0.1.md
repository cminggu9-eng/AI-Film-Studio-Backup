# AI Film Studio V0.1 — Showrunner 五人交叉蒸馏任务书

## 任务定位

本任务只对五份已批准的单人能力档案进行 `huashu-nuwa` 交叉抽象，不重新蒸馏任何创作者，不生成最终 `Showrunner SKILL.md`，不开始场景写作、导演或长篇项目。

Codex 负责证据边界、调度、独立审核与发布控制；女娲 `huashu-nuwa` 负责交叉方法论抽象；Obsidian Vault 是正式档案；用户是最终决策者。未经审核的结果只能进入 `runtime/_STAGING/`。

## 唯一核心输入

只允许使用以下五份已通过审核的正式档案作为核心输入：

1. `02_DISTILLATION/编剧研究/Craig Mazin｜Showrunner能力蒸馏 V0.1.md`
2. `02_DISTILLATION/编剧研究/Vince Gilligan｜Showrunner能力蒸馏 V0.1.md`
3. `02_DISTILLATION/编剧研究/Shonda Rhimes｜Showrunner能力蒸馏 V0.1.md`
4. `02_DISTILLATION/编剧研究/Tony Gilroy｜Showrunner能力蒸馏 V0.1.md`
5. `02_DISTILLATION/编剧研究/David Simon｜Showrunner能力蒸馏 V0.1.md`

研究账本、证据审计与既有干跑只能用于回查出处和边界，不能替换五份核心输入，也不能抹除各自的 `SOURCE-SUPPORTED`、`SYNTHESIZED INFERENCE` 与 `AI FILM STUDIO SYNTHESIS` 标签。

## 能力矩阵要求

建立至少 29 行矩阵，至少覆盖：Story Premise、Theme、Character Desire、Misbelief/Internal Change、Choice、Consequence、Story Breaking、Causal Chain、Series Engine、Episode Engine、Season Engine、Relationship Engine、Continuing Drive、Destination Awareness、Scene/Phase State、Reality Check、Complex Information、Modular Longform、Institution Model、Incentive System、Ensemble、Distributed Causality、System Persistence、Long-Term Consequence、Production Reality、Scope Compression、Research→Drama、Exhaustion Diagnosis、Rewrite/Recovery。

每行必须有：能力、Craig/Vince/Shonda/Tony/David 各自贡献、重叠、互补或冲突、推荐归属、层级。不得只复制五篇文章；必须去重并保留来源。

## 关系分类与交叉检查

- A `CONSENSUS`：多份档案在同一判断门槛上相容。
- B `COMPLEMENTARY`：不同层级或不同输入输出，组合后增值。
- C `OVERLAP`：功能相近，须指定主责和接口。
- D `CONDITIONAL TENSION`：条件不同才适用，保留触发条件。
- E `TRUE CONFLICT`：不能强行合并，保留两端与决策条件。

必须显式检查 Craig×Vince、Vince×Shonda、Shonda×Tony、Tony×David、Craig×David，以及 Production Reality×Story Quality。生产取舍顺序固定为：`Creative Intent → Essential Dramatic Function → Production Cost Driver → Alternative Execution → Scope Decision`，不能因为 AI 做不到就删除戏剧功能。

## 综合规则边界

所有规则必须标为：`HARD CONSTRAINT`、`DEFAULT HEURISTIC`、`CONDITIONAL METHOD` 或 `OPTIONAL TOOL`。明确拒绝以下机械化误读：每场必须选择、每集必须升级或 cliffhanger、每季必须解决、所有故事必须复杂制度／群像、结局必须预先完全确定、现实主义必须绝对、低成本必须优先。真冲突使用 `CONTEXT → QUESTION → OPTION A/B → TRADEOFF → DECISION CONDITION`，不得删除任何一方。

## 原创综合干跑

使用与五人既有干跑不同的故事：普通社区物业经理发现五年间许多老住户突然搬离，表面理由分别是家庭、医疗、退休或卖房；她逐步发现城市更新、房地产融资、照护机构、家庭债务和房价互相作用。必须测试故事目的、人物发动机、无主角世界发动机、因果链、系列／单集发动机、终点意识、信息管理、群像功能、制作压缩、非大 cliffhanger 的继续驱动、系统持续、以及“垃圾桶随机发现完整阴谋文件”的重写。另对六条反机械化压力测试给出结果。

## 交付与发布

首轮只能写入：`runtime/_STAGING/Showrunner_Cross_Distillation_V0.1.md`。必须包含：

`## 输入档案`、`## 能力矩阵`、`## 共识规则`、`## 互补能力`、`## 重复能力与去重结果`、`## 条件性张力`、`## 真冲突`、`## 冲突决策机制`、`## Showrunner 决策层级`、`## 规则优先级`、`## AI Film Studio 自有综合规则`、`## 综合工作流程`、`## 诊断问题`、`## 失败模式`、`## 修正方法`、`## 综合干跑`、`## 反机械化测试`、`## 证据与来源映射`、`## Codex 审核结论`。

Codex 必须独立审核：矩阵规模与出处、去重质量、关系分类、真冲突保留、层级、规则优先级、原创干跑、反机械化与不同故事类型适用边界。审核不通过不得发布；通过后才改为 `status: approved`、`review_result: passed`，并使用 `scripts/publish_to_obsidian.py` 发布至 `02_DISTILLATION/方法论/Showrunner｜五人交叉蒸馏 V0.1.md`。发布成功后核验 Vault 正式文件、`_PUBLISHED` 归档和工作日志。

完成后立即停止，不创建 Showrunner Skill，不锁定综合模型，不开始下一生产阶段。
