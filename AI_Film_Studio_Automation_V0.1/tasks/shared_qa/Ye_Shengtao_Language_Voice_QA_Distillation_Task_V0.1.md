---
type: distillation-task
status: completed
version: 0.1
subject: 叶圣陶
domain: Language & Voice QA
target_capability: Meaning-Preserving Editing Judgment
---

# 叶圣陶｜Language & Voice QA 能力蒸馏任务 V0.1

## 任务边界

本轮只蒸馏叶圣陶可迁移到 AI Film Studio 的 `Meaning-Preserving Editing Judgment`。不得模仿个人文风，不得继承历史词汇、时代语法规范、文学审美、教科书式表达或“所有文本都应浅白/简短/朗朗上口”的偏好。

本轮不得启动汪曾祺、老舍、余光中、刘震云、Cross-Distillation、Capability Model、QA Skill、Runtime 或 Scene Writer。

## 角色与发布规则

- Codex：证据准备、调度、独立审核、测试与发布控制。
- `huashu-nuwa`：能力方法论的正式蒸馏执行器。
- 首轮结果只写入 `runtime/_STAGING/Ye_Shengtao_Language_Voice_QA_Distillation_V0.1.md`。
- 未通过审核不得设为 `approved / passed`，不得进入 Vault。
- 通过后只能由 `scripts/publish_to_obsidian.py` 发布。

## 核心问题

当一句话语法看似成立，却不自然、不清楚或不准确时，形成以下可执行链：

`Intended Meaning → Current Expression → Mismatch → Repair Options → Meaning Check`

必须回答：原意是什么、问题在哪里、为什么是问题、有哪些合理方案、修改后是否真的更好且未改意。

## 必须形成的能力模块

1. `Meaning Before Wording`：词句问题与思想/逻辑未理清分流。
2. `Expression Accuracy`：区分语法正确与意义准确，检查指代、主体、因果、范围、程度、抽象对应和越证据断言。
3. `Clarity / 顺当`：检查主干、信息顺序、修饰范围、逻辑连接、句间关系、重复、名词化和抽象链；不得把短句等同自然。
4. `Read-Aloud Check`：只作语体敏感的辅助检查，不以卡顿自动判错，不将专业 Brief 强制口语化。
5. `Revision With Reasons`：`Original → Issue → Reason → Revision Option → Meaning Check`；允许多案与 `NO CHANGE`。
6. `Over-Editing Protection`：没有明确收益时保持原句。
7. `Register Awareness`：适配 Charter 的 R1–R8，不建立唯一“标准中文”。

## 证据协议

必须重新打开候选审计中的两份一手材料，不得只转述审计摘要：

- YST-01：中国作家网《怎样写作》选文。
- YST-02：叶圣陶研究会保存的 1978 写作报告及 1979 修改附记。

可以补充高质量一手材料；二手来源不得单独支撑核心规则。建立 canonical Evidence Ledger，逐条记录来源、原文位置/段落锚、直接支持范围、禁止外推范围和正文主张映射。

所有主要方法必须标注：

- `SOURCE-SUPPORTED`
- `SYNTHESIZED INFERENCE`
- `AI FILM STUDIO SYNTHESIS`

并归入：

- `HARD CONSTRAINT`
- `DEFAULT HEURISTIC`
- `CONDITIONAL METHOD`
- `OPTIONAL TOOL`

## 女娲执行约束

完整读取并实际使用 `C:\Users\布朗熊\.codex\skills\nuwa-skill\SKILL.md`。采用其主题/能力方法论变体：证据优先、来源分级、三重验证、推断边界、失败模式与独立验证。由于本任务禁止人物模仿，不生成身份卡、角色扮演、表达 DNA、个人语气或人物 Perspective Skill。

应保存调用回执：Skill 名、路径、SHA-256、读取状态、执行时间、采用阶段与受任务边界约束而省略的阶段。

## Staging 必备章节

- `## 蒸馏目标`
- `## 核心判断原则`
- `## Meaning Before Wording`
- `## Expression Accuracy`
- `## Clarity / 顺当`
- `## Read-Aloud Check`
- `## Revision With Reasons`
- `## Over-Editing Protection`
- `## Register Awareness`
- `## QA Mode 应用`
- `## Rewrite Mode 应用`
- `## 工作流程`
- `## 诊断问题`
- `## 失败模式`
- `## 修正方法`
- `## 禁止继承`
- `## 可 Skill 化规则`
- `## 证据与来源`
- `## Codex 审核结论`

## 原创干跑

### TEST A｜主题总结 QA

输入：“这个故事真正讨论的不是游戏，而是在算法不断定义人的价值时，一个普通人如何重新确认自己的存在。”

只做 QA：检查 Meaning、抽象密度、确定性、清楚度、Register 与过度总结，然后决定 `KEEP / CHANGE / WARNING`。

### TEST B｜人工二元

输入：“他必须在服从规则与保护一个具体的人之间做出选择。”

检查是否为人工二元对仗；还原可能因果；给出两个自然度不同的候选，并逐项验证原意。输入不足时必须标明假设，不能把推测写成事实。

### TEST C｜名词化与空泛

输入：“项目现在需要对世界观、人物关系以及系统机制进行进一步的完整化处理，从而使后续剧情开发获得更加稳定的基础。”

检查名词化、空泛表达、连接词、抽象层级和意义保护；不得把删除字数本身当作完成。

### TEST D｜NO CHANGE

输入：“第二天没人记得她了，只有他记得。”

合格结果应允许 `NO CHANGE`，不得为炫技改得更文学、更完整或更高级。

### TEST E｜Project Brief

输入：“第一季重点验证世界规则、核心人物关系和 Series Engine 是否成立，暂不进入完整场景剧本。”

必须按 R2 判断，不能因书面化、专业术语或抽象度误判为 AI 腔。

### TEST F｜伪术语

输入：`任务事故现场`

检查谁会使用、在哪种社会/项目场景使用、它指向什么具体区别、为什么普通说法不够。不得因陌生自动删除，也不得因“像专业词”无证放行；上下文不足时应给 `TERM PLAUSIBILITY WARNING` 并请求最少必要信息。

### Rewrite Mode｜Showrunner 创作讨论

输入：“寻找那个已经被全城遗忘、却仍存在于男主记忆中的人。”

先提取 Meaning，再给 Natural Discussion Version；逐项检查人物事实、信息保留、新增设定和风格模仿风险。

## Codex 审核门

1. Meaning Preservation 成立。
2. 区分语法正确与表达准确。
3. 修改都有理由与意义复核。
4. 支持 `NO CHANGE`。
5. 防止过度编辑。
6. R1–R8 Register 可适配。
7. Read-Aloud 未机械化。
8. 未引入历史语言规范。
9. 未模仿叶圣陶文风。
10. 能处理指定 AI 腔案例。
11. 形成 `Input → Judgment → Decision → Output`。
12. 能作为后续 Cross-Distillation 的独立能力。

任一门失败：定位问题，定向补证据或返工，重跑受影响测试，再审核。最多两轮；仍失败则保持 staging 并报告 `BLOCKED`。

## 发布条件与目标

审核 PASS 后才可设置：

```yaml
type: distillation
status: approved
review_result: passed
version: 0.1
subject: 叶圣陶
domain: Language & Voice QA
```

发布目标：

`02_DISTILLATION/语言与表达研究/叶圣陶｜Language & Voice QA 能力蒸馏 V0.1.md`

发布后必须确认：正式文件存在、staging 已进入 `_PUBLISHED/<YYYY-MM-DD>/`、工作日志已写入、无未解决阻塞项。随后立即停止。
