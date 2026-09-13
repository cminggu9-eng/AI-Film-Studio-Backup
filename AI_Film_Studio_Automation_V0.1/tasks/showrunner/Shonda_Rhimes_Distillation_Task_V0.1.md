# Shonda Rhimes｜Showrunner 能力蒸馏任务书 V0.1

## 任务性质

AI Film Studio V0.1 的第三份 Showrunner 单人能力方法论蒸馏。沿用已经验证的受控管线；本任务只沉淀连续剧的可复用判断与协作方法，不建立新的 Showrunner Skill，也不改变既有管线架构。

## 目标

从可验证的、以 Shonda Rhimes 本人公开陈述为核心的材料中，提取 **Series Engine（连续剧发动机）**：回答一部剧为何能在第一集之后，持续、自然地生成值得观看的故事。

本轮必须覆盖：

1. 项目是否适合电视、电影、短剧或其他叙事形式的判断；
2. premise 与可再生 Series Engine 的区别；
3. 持续欲望、变化中的关系、可再生冲突，以及职业／组织／环境来源、长期秘密与责任、未决状态如何供给故事；
4. pilot 如何建立世界、人物、关系、核心冲突、发动机和“为何需要第二集”；
5. Episode Engine：本集为何存在，以及本集结束后的状态如何自然导出下一集；
6. A／B／C 线的用途、切换效果、节奏／主题／关系价值，以及何时不应机械套用；
7. Episode Turn 如何形成真实状态变化，而不是拖延同一问题；
8. Continuing Drive 如何以新问题、欲望、信息、关系、责任、未完成压力或状态变化继续推进，而非强制大 cliffhanger；
9. Season Engine 如何让多集构成阶段推进；
10. Relationship Engine 如何持续产生选择与变化；
11. 如何识别耗竭、重复冲突、人为拖延、假悬念和不合理选择；
12. 如何在不牺牲人物与因果的前提下，建立商业上的“继续观看”动机。

## 不要提取

- *Grey's Anatomy*、*Scandal*、*Bridgerton* 或其他作品的具体剧情；
- 医疗、政治、浪漫题材模板，以及出轨、死亡、秘密等表层刺激物；
- 角色类型、签名式对白、快节奏表达、视觉风格或“模仿 Shonda Rhimes”的写作人格；
- “好电视剧等于无限大反转”的机械结论。

## 证据要求

优先使用 Shonda Rhimes 本人的公开课程／合法公开材料、长访谈、showrunning 或 writers' room 讨论、关于 pilot、角色、系列及故事机制的公开陈述。课程目录或宣传页只能证明课程存在或其公开描述；不得把未公开课件内容伪写成其观点。

二手资料只能用于定位、背景或交叉核验，不能单独支撑核心方法。每个重要结论必须标为：

- **SOURCE-SUPPORTED**：可追溯到列出的来源；或
- **SYNTHESIZED INFERENCE**：基于多个来源的归纳，不能伪装成原话或单一事实。

## 方法分类要求

所有方法必须标为以下之一：

1. **硬约束**：缺失即无法确认故事仍由人物、关系或可验证的状态变化驱动；
2. **默认启发式**：通常有效，项目条件可推翻；
3. **条件适用方法**：明确前提下才使用；
4. **可选工具**：用于检查、协作或可视化，不代替判断。

不得把任意方法写成“每场／每集必须有 A/B/C、cliffhanger、巨大反转、人物弧、固定页数事件、持续升级或无限问题”的公式。

## 执行流程

1. 读取本任务书、`AGENTS.md`、`PUBLISH_RULES.md`、`studio.config.json` 与已安装的 `huashu-nuwa`。
2. 仅在 `runtime/_STAGING/_research/Shonda_Rhimes_V0.1/` 准备来源—主张对应的证据工作区。
3. 按女娲 Skill 进行单人能力蒸馏；首稿只能写入：
   `runtime/_STAGING/Shonda_Rhimes_Showrunner_Distillation_V0.1.md`。
4. Codex 独立审核 Series Engine、premise 区分、pilot／episode／season／relationship engines、多线非机械性、非廉价 Continuing Drive、耗竭诊断、输入→判断→决策→输出、失败与修正，并确认只与 Craig／Vince 互补、不融合。
5. 使用下列原创概念进行可执行性干跑，且不把它发展为正式项目：
   “一家小型私家侦探机构处理城市失踪人口档案。三位核心成员分别接手不同失踪案，同时每人都隐瞒一件与事务所创立有关的旧案秘密。”
   检验发动机、EP02/03/04、pilot 功能、三种单集来源、长期线与单集线、ABC 是否必要、非大 cliffhanger 的继续驱动力、耗竭阈值，以及故事本身与当前结构的问题区别。
6. 发现证据不足、强制 ABC／cliffhanger／大反转、人物为续订做不合理选择或因果失真时，只做定向补证据、返工和复审；未通过不得发布。
7. 审核通过后将 frontmatter 设为 `approved/passed`，且只能通过下列脚本发布：

```powershell
python scripts/publish_to_obsidian.py `
  --source "runtime/_STAGING/Shonda_Rhimes_Showrunner_Distillation_V0.1.md" `
  --dest "02_DISTILLATION/编剧研究/Shonda Rhimes｜Showrunner能力蒸馏 V0.1.md" `
  --title "Shonda Rhimes Showrunner 能力蒸馏 V0.1"
```

## 完成标准

- 实际遵循 `huashu-nuwa`；
- 核心方法具备可核验、以第一手为主的证据；
- 形成可复用的 Series Engine，而不是题材或作品套路；
- 明确 premise 与 engine、pilot／episode／season／relationship engines 的关系；
- 所有结论带有 SOURCE-SUPPORTED 或 SYNTHESIZED INFERENCE 边界，且具四类方法分类；
- 原创干跑、Codex 独立审核和必要返工均通过；
- 发布脚本成功，Vault 档案、`_PUBLISHED` 归档与工作日志真实存在；
- 完成后立即停止，不自动开始 Tony Gilroy、David Simon、交叉蒸馏、能力模型或 Showrunner SKILL.md。
