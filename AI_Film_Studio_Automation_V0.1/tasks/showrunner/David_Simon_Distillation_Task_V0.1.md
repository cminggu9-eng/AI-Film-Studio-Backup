# David Simon｜Showrunner 能力蒸馏任务书 V0.1

## 任务性质

AI Film Studio V0.1 的第五份 Showrunner 单人能力方法论蒸馏。本轮目标是 **WORLD-SYSTEM ENGINE**：提取如何研究、建模和管理一个即使主角不存在，也能自行运行、施加压力并产生剧情的世界系统。

本轮不进行五人交叉蒸馏、不建立综合 Showrunner 模型或正式 Showrunner Skill，不发展原创测试概念为正式项目。

## 核心目标

提取并验证以下能力模块：

1. **Research Before Drama**：建立 `Minimum Sufficient Understanding`，判断哪些现实机制必须先研究、研究到何时足够开始创作，避免常识臆测与无限研究。
2. **Institution Model**：拆解机构的正式目标、实际目标、权力来源、资源、奖惩、指标、层级、内部利益、外部压力、制度限制、非正式规则和自我保护机制，形成可选择性使用的 `Institution Map`。
3. **Incentive-Based Behavior**：将 `Character Desire + Institutional Incentive + Constraint → Behavior` 作为分析接口；系统改变选择成本与后果，不把人物简化为制度木偶。
4. **World Without Protagonist Test**：移除主人公后，机构、人物、权力、资源和事件是否仍继续运行；不把完整社会模拟机械施加于轻类型故事。
5. **Multi-Sided Conflict**：分析多方利益、合作与冲突、临时联盟、不同事件含义和不完整信息；不把“人物越多”当成质量。
6. **Ensemble Function Test**：每个重要人物必须提供新视角、利益位置、因果入口、权力关系、信息区域或关系功能；重复功能优先考虑合并，但不得粗暴压成主角／反派二元。
7. **Distributed Causality**：用规则、利益、惯性、错误决策、局部行为和意外后果解释事件；同时保留明确恶意行为者的适用空间。
8. **Institutional Memory & Persistence**：维护跨阶段的 `System State`，让决策、丑闻、失败、处罚、人事、资源和权力变化持续影响后续，不因主角一场戏而重置世界。
9. **Long-Term Consequence**：区分立即、短期、长期和潜伏后果（若证据支持），避免“每个行为下一场马上报应”。
10. **Research → Drama Conversion**：事实 → 压力 → 利益冲突 → 人物位置 → 选择 → 后果；禁止用百科对白展示研究。

## 禁止提取

- *The Wire*、Baltimore、警察、毒品、新闻行业或任何具体作品／城市／机构的剧情、角色、政治立场与世界模板；
- 悲观主义、犬儒主义、慢节奏、社会写实气质、对白风格或“像 David Simon 一样写”的人格；
- “没有英雄和反派”“群像越大越高级”“系统故事不能有明确反派”等绝对化结论。

## 与既有单人蒸馏的边界

Tony Gilroy 的 Scene／阶段状态、现实因果、模块化与制作检查只作为潜在 **OVERLAP CANDIDATE** 记录；本轮不融合、不重写 Tony 成果。David Simon 本轮集中于 Research Model、Institution Model、Incentive System、World Without Protagonist、Ensemble Function、Distributed Causality、System Persistence 与长期制度后果。

## 证据规则

- 优先使用 David Simon 本人的著作、长篇访谈、讲座、writers' room／创作过程讨论及直接公开陈述；二手材料只能辅助核验，不得单独承载核心主张。
- 每个重要结论标记为：`SOURCE-SUPPORTED`、`SYNTHESIZED INFERENCE` 或 `AI FILM STUDIO SYNTHESIS`。
- 每个方法同时标注：硬约束、默认启发式、条件适用方法或可选工具。
- 明确区分本人直接说出、跨来源归纳和 Studio 自有规则；不得虚构引语、课程、访谈或来源。

## 执行流程

1. 读取本任务书、`AGENTS.md`、`PUBLISH_RULES.md`、`studio.config.json` 与完整 `C:\Users\布朗熊\.codex\skills\nuwa-skill\SKILL.md`。
2. 在 `runtime/_STAGING/_research/David_Simon_V0.1/` 建立来源、主张映射、冲突和证据边界；按女娲 Skill 的多源研究流程执行，所有中间材料留在 `_STAGING`。
3. 完成证据检查点后，正式执行 `huashu-nuwa` 单人能力蒸馏。第一轮只能写入：
   `runtime/_STAGING/David_Simon_Showrunner_Distillation_V0.1.md`
4. 首稿必须包含以下章节：
   `## 蒸馏目标`、`## 核心判断原则`、`## 工作流程`、`## 诊断问题`、`## 失败模式`、`## 修正方法`、`## 禁止继承`、`## 可 Skill 化规则`、`## 证据与来源`、`## Codex 审核结论`。
5. Codex 独立检查 Research Model、Institution Model、激励行为、多方冲突、群像功能、分布式因果、System State、长期后果、Research → Drama、三层标签、四类方法分类、输入 → 判断 → 决策 → 输出及与 Tony 的未融合边界。
6. 使用下方原创沿海码头概念干跑；只测试方法，不发展正式项目。发现机械规则、政治／风格误蒸馏、证据不足或因果断裂时，定向补证据／返工并重新干跑。
7. 只有 Codex 复审 PASS 后，才将 frontmatter 改为 `status: approved`、`review_result: passed`，并调用 `publish_to_obsidian.py`。

## 原创可执行性干跑

测试概念：一座人口约 40 万的沿海城市计划关闭一座运营多年的老客运码头，将土地交给新的商业开发项目；涉及市交通部门、码头运营公司、开发商、周边商户、居民、船员和地方媒体；一名年轻地方记者只是众多人物之一。

必须记录以下八项结果：

1. **World Without Protagonist**：移除记者后，一个月内机构工作、人物目标、权力流动、资源争夺和事件发展仍继续。
2. **Institution Map**：为市交通部门写正式目标、实际压力、奖惩、资源、层级、外部压力和自我保护机制，并证明其能产生故事压力。
3. **Multi-Sided Conflict**：至少分析交通部门、运营公司、开发商、商户／居民的目标、恐惧、控制范围和盲区，不生成简单好人／坏人阵营。
4. **Character + Incentive**：设计一个并非本质恶意的中层公务员，让制度奖励促成一个对居民不利但职位上合理的决定，同时保留拒绝压力的自由选择。
5. **Distributed Causality**：由多个合理局部决定共同产生负面后果，再反向测试明确恶意角色仍可存在。
6. **Research → Drama**：从码头运营、交通预算或土地开发机制中选一项，转换为人物目标、现实障碍、选择和后果，不用百科对白。
7. **Ensemble Function**：对初版 15 个重要人物逐一判断独立系统位置、信息／因果／关系功能；合并重复功能，但不压成主角／反派二元。
8. **Long-Term Consequence**：让第一阶段的小行政决定在后续阶段产生可追溯的大后果，不能以“后来想起来了”补因果。

## 机械化禁区

- 不要求所有故事都建立复杂制度模拟；轻类型可采用最小必要系统模型；
- 不把研究深度等同于领域专家资格，不允许无限研究阻塞创作；
- 不把人物简化成激励函数或制度木偶；
- 不把多方冲突、人群数量、系统复杂度或长期跨度当成质量配额；
- 不要求每个行为下一场立即反馈；
- 不把分布式因果变成“不能有反派”；
- 不把研究转成百科对白；不以政治立场、慢节奏、犬儒气质或社会写实风格代替方法论；
- 不提前融合 Tony Gilroy 或前四位成果；只记录 `OVERLAP CANDIDATE`。

## 发布命令

```powershell
python scripts/publish_to_obsidian.py `
  --source "runtime/_STAGING/David_Simon_Showrunner_Distillation_V0.1.md" `
  --dest "02_DISTILLATION/编剧研究/David Simon｜Showrunner能力蒸馏 V0.1.md" `
  --title "David Simon Showrunner 能力蒸馏 V0.1"
```

## 完成与停止条件

- 正式 Obsidian 文件、`runtime/_PUBLISHED` 归档和工作日志真实存在；无发布错误或未解决阻塞。
- 完成后立即停止；禁止自动开始五人交叉蒸馏、综合能力模型、Showrunner SKILL.md、Scene Writer、Director 或正式剧本。
