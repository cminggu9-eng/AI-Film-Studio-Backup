---
type: distillation
status: approved
review_result: passed
version: 0.1
subject: 刘震云
domain: Language & Voice QA
target_capability: Everyday Social Communication Judgment
core_first_hand_sources: 4
first_hand_ratio: 100%
nuwa_skill: huashu-nuwa
---

# 刘震云｜Language & Voice QA 能力蒸馏 V0.1

> 本稿蒸馏的是社会交流判断机制，不是刘震云文风、幽默、地域语言或作品方法的模仿。  
> `SOURCE-SUPPORTED` = 来源可直接支持的窄主张；`SYNTHESIZED INFERENCE` = 女娲基于多份来源的能力归纳；`AI FILM STUDIO SYNTHESIS` = Charter 与生产系统的运行转译。  
> 规则级别：`HARD CONSTRAINT / DEFAULT HEURISTIC / CONDITIONAL METHOD / OPTIONAL TOOL`。

## 蒸馏目标

建立 `Everyday Social Communication Judgment`：当一句话符合人物身份、语法自然、没有翻译腔时，继续判断整段交流是否像具有各自注意力、利益、关系历史、信息边界和即时目的的人在交往，而不是两个语言模型协作传输信息。

`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC`：

`Context → Participants → Receiver / Relationship → Intended / Spoken / Received / Response → Conversation State → Social Plausibility → Decision`

本模块只负责 `INTERACTION FIT`。它不替代 Meaning、Naturalness、Syntax、Speaker Fit、场景设计、人物表演或故事结构。

## 核心判断原则

|ID|原则|级别|证据属性|
|---|---|---|---|
|P1|判断单位至少是一轮互动及其上下文，而不是孤立漂亮句。|HARD CONSTRAINT|SOURCE-SUPPORTED 基础：LZY-01 前后联结；运行门为 SYNTHESIZED INFERENCE|
|P2|先确认真实 Receiver；名义关系不等于实际信任、风险或披露权限。|HARD CONSTRAINT|SOURCE-SUPPORTED 基础：LZY-02、LZY-04；五段式为 SYNTHESIZED INFERENCE|
|P3|所想、所说、所听与所回可以不同，也可以一致；差异不是质量配额。|HARD CONSTRAINT|SOURCE-SUPPORTED 基础：LZY-01/02；四段式为 AI FILM STUDIO SYNTHESIS|
|P4|礼貌、清楚、合作不自动是 AI；只有它超过人物能力、关系许可、压力状态或即时目的时才构成风险。|HARD CONSTRAINT|SYNTHESIZED INFERENCE + AI FILM STUDIO SYNTHESIS|
|P5|答非所问、沉默、重复、闲话和低效率不自动真实；必须说明其社会/关系功能。|HARD CONSTRAINT|SOURCE-SUPPORTED 基础：LZY-01；反机械门为 AI FILM STUDIO SYNTHESIS|
|P6|人物不必准确理解自己，也不必永远误解自己；自我解释差距是条件方法。|CONDITIONAL METHOD|SYNTHESIZED INFERENCE；完整状态为 AI FILM STUDIO SYNTHESIS|
|P7|具体生活材料需与人物性格、见识和当前作品相融；将其转译为关系/任务检查，并规定物件或小事没有真实性特权。|DEFAULT HEURISTIC|SOURCE-SUPPORTED 基础：LZY-03（细节—人物性格/见识/作品适配）；关系/任务运行门与真实性特权判断为 SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS|
|P8|人物不能共同成为作者的同一话筒；但正常共识、专业协作和程序性确认必须允许。|HARD CONSTRAINT|SOURCE-SUPPORTED 基础：LZY-02/04；AUTHORIAL COLLABORATION 为 AI FILM STUDIO SYNTHESIS|
|P9|原交流已满足人物、关系、目的和 Register 时，必须允许 `LEVEL 0 / KEEP / NO CHANGE`。|HARD CONSTRAINT|AI FILM STUDIO SYNTHESIS|
|P10|不确定社会语境时降低置信度并请求最少信息，不脑补动机、误解、潜台词或心理。|HARD CONSTRAINT|AI FILM STUDIO SYNTHESIS|

## Receiver Matters

`SOURCE-SUPPORTED 基础：LZY-01、LZY-02、LZY-04；完整链为 SYNTHESIZED INFERENCE｜HARD CONSTRAINT`

`SPEAKER → RECEIVER → RELATIONSHIP → PURPOSE → SPEECH FORM`

逐层检查：

1. **Speaker**：是谁在表达；当前知道、相信、承认什么。
2. **Receiver**：具体说给谁，而不是泛泛“给观众”。
3. **Relationship**：名义关系、实际信任、权力、债务、风险和历史分别怎样。
4. **Purpose**：想让对方知道、做、停止、误解、原谅，还是只维持接触。
5. **Speech Form**：这些条件是否支持直说、解释、敷衍、暗示、隐瞒、玩笑或不说。

Receiver 改变的可能不只是语气，也包括信息范围、理由是否展开、谁承担风险、是否暴露真实目的。不得把母亲、领导、陌生人或朋友映射成固定说法。

## Communication Is Not Transmission

`SYNTHESIZED INFERENCE + AI FILM STUDIO SYNTHESIS｜DEFAULT HEURISTIC`

`INTENDED MESSAGE → SPOKEN MESSAGE → RECEIVED MESSAGE → RESPONSE`

- **Intended**：说话者试图完成什么；未知时不读心。
- **Spoken**：实际说了什么、遗漏什么、以何种强度说。
- **Received**：对方依据知识、注意力、利益和关系可能听到什么；没有证据时列候选，不宣判。
- **Response**：回应了原句、自己的担心、关系压力，还是另一个紧迫问题。

四层一致可以完全自然；四层不同也不自动精彩。QA 只在差异造成非预期的信息、关系或任务损失时提出问题。

## Misalignment

`SYNTHESIZED INFERENCE｜CONDITIONAL METHOD；分类为 AI FILM STUDIO SYNTHESIS`

可能来源：利益不同、信息不同、注意点不同、关系期待不同、面子、恐惧、身份/权力、不愿承认、同词异解、另一项更紧迫的现实需要。

运行门：

1. 先标出具体错位发生在哪两层；
2. 找出文本或已知设定中的证据；
3. 判断它是人物有意策略、合理误差、当前关系结果，还是作者无意遗漏；
4. 无上下文则 `NEEDS CONTEXT / UNDERDETERMINED`；
5. 只有无意错位破坏当前戏剧任务时，才建议语言返工或岗位 Handoff。

禁止把“答非所问”字符模式直接判坏，也禁止为真实感强造误解。

## Silence as Response

`SOURCE-SUPPORTED 基础：LZY-01、LZY-04；运行规则为 SYNTHESIZED INFERENCE｜CONDITIONAL METHOD`

不回应、转移话题、结束谈话、欲言又止或以行动替代语言，可能表达拒绝、回避、失去说话条件、维持面子、控制谈话或关系断裂。成立需同时满足：

- 当前人物有不说的理由；
- Receiver 能把沉默/动作纳入已知关系与当下问题；
- 该行为改变或维持了交流状态；
- QA 不需要发明人物完整内心才能解释其最低功能。

若动作的具体含义可能有多种，只能报告 `FUNCTION PLAUSIBLE / MEANING UNDERDETERMINED`。不把沉默当高级技巧，不要求每场留白。

## Social Position

`SOURCE-SUPPORTED 基础：LZY-01 的场合/媒介/单位与家庭差异；完整操作为 SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS｜DEFAULT HEURISTIC`

社会位置通过关系策略影响交流：谁能追问、拒绝、命令、拖延、装懂、要求解释或承担说错的后果。检查：

- 正式职位与当前实际权力是否一致；
- 说话者承担什么职业、关系或名誉风险；
- Receiver 能提供、阻止或惩罚什么；
- 公开/私下、即时/延迟、留痕/不留痕如何改变表达。

禁止“员工必委婉、领导必直接、家人必坦白”。社会位置只是约束，不是台词模板。

## Ordinary Motives

`SOURCE-SUPPORTED 基础：LZY-02 的人物大小事排序、LZY-03 的生活底部；现代分类为 SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC`

人物此刻可能只想不丢脸、不添麻烦、早点离开、借到钱、避免争吵、保住工作、证明自己没错、让谈话结束或保持表面和平。QA 要问：是否有一个与现场相连的实际沟通动作。

小动机没有道德或真实性优先权。高自省、公共理想、专业职责或宏观议题在人物确有能力和目的时同样成立。

## Everyday Detail Anchoring

`SOURCE-SUPPORTED 基础：LZY-03 只直接支持细节需与人物性格、见识和当前作品相融；关系压力、现代事项示例、真实性特权与完整运行门为 SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS｜DEFAULT HEURISTIC`

钱、时间、钥匙、订单、吃饭、交通、微信、工作和谁没回来等具体事项可以承载关系，但只有在它们与人物性格、见识、关系压力和当前任务相融时才有效。

检查：

- 具体事项是否真的改变交流，还是装饰“烟火气”；
- 它是否让抽象关系问题可定位，而非替代必要表达；
- 人物是否会在此刻注意这件小事；
- 删除它后关系信息是否损失。

不设置生活物件、饭菜、钱或时间的出现配额。

## Self-Interpretation Gap

`SOURCE-SUPPORTED 基础：LZY-01 的嘴—心距离、LZY-02 的人物认知独立；完整模型为 SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS｜CONDITIONAL METHOD`

`ACTUAL STATE ≠ SELF-EXPLANATION` 可以成立。人物可能把嫉妒说成“不可靠”、把害怕说成“麻烦”、把羞耻说成“原则”。运行时必须分开：

1. Story / Canon 已知的实际状态；
2. 人物当前能意识到什么；
3. 人物愿向这个 Receiver 承认什么；
4. 人物实际说出的解释。

QA 不能把上帝视角的“真实心理”直接写进台词。高自省人物、治疗/复盘语境或已完成认识变化时，准确自我解释可以 PASS。

## Conversation Memory

`SOURCE-SUPPORTED 基础：LZY-01 的前后联结；状态模型为 AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`

检查单位必须保留 `CONVERSATION STATE`：

- 已经说过与确认过什么；
- 哪个问题被拒绝、误解或回避；
- 当前情绪和关系状态；
- 谁掌握主动、谁欠回应；
- 哪个问题尚未解决；
- 新一句如何更新或故意不更新这些状态。

QA 只报告状态断裂、无因复位或遗忘风险；不替 Scene Writer 设计下一 beat、动作和整段重写。

## Social Plausibility

`SYNTHESIZED INFERENCE + AI FILM STUDIO SYNTHESIS｜DEFAULT HEURISTIC`

最终检查：这是否像社会中的人正在交流，而非共享同一作者脑内信息的模型节点？

- 各方是否有自己的注意力与重要性排序；
- 是否存在具体 Receiver 与关系历史；
- 回应是否精确到超出知识、能力、压力或承认意愿；
- 每个人是否都过度合作、都懂主题、都帮助总结；
- 低效、闲话或沉默是否有功能，而不是随机噪声；
- 普通明确交流是否被错误复杂化。

Social Plausibility 不是“越乱越真”。真实的人也会高效、清楚、善于沟通。

## 与老舍边界

- **老舍｜SPEAKER FIT**：这个人物在这个时刻是否知道、能说、愿说、会这样说。
- **刘震云｜INTERACTION FIT**：这些参与者是否依据各自 Receiver、关系、目的、接收结果与已有状态真实地互动。
- **重叠处置**：WHO/TO WHOM 可同时出现，但刘模块不重建人物完整语言人格，也不接管职业词、知识权限和单句可说性的全部判断。
- **Handoff**：根因是单个人物 voice/知识时交老舍接口或 Character & Acting；根因是多方回应、接收和状态链时留在本模块。

这是职责切分，不是当前五人 Cross-Distillation。

## 与前三位能力边界

- **叶圣陶**：Meaning、Accuracy、修改理由、改前改后保义。
- **汪曾祺**：Naturalness、整体流动、Anti-Overwriting / Anti-Rhetoric。
- **余光中**：Translation-like Syntax、名词化、介词、主干与信息顺序。
- **刘震云**：Receiver、接收差异、互动状态和社会交流可信度。

公共的 Register、Meaning Lock、Mode、Severity、NO CHANGE 与 Handoff 来自 Charter，不归因于任何作者。本稿只记录未来接口，不融合四人方法。

## Contemporary Language 边界

`AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`

本模块可问：人物是否接触该表达、是否会对这个 Receiver 使用、当前场景是否容纳、它是亲近/引用/表演/讽刺还是假生活化。

本模块不得判断“包的、绷不住、班味、已老实求放过”等在 2026 是否流行、过时或平台占比。需要该结论时输出：

`HANDOFF: Contemporary Language Layer — CURRENT USAGE / PLATFORM EVIDENCE REQUIRED`

LZY-03 是 2025 现代锚，不是实时语料库。

## QA MODE

`AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`

默认只诊断，不给替代台词：

```text
Mode: QA
Register:
Context Confidence:
Original / Interaction Span:
Speaker / Receiver / Relationship / Purpose:
Intended / Spoken / Received / Response:
Conversation State:
Problem Type:
Severity: LEVEL 0–5
Why:
Meaning Warning: NONE / DETAILS
Recommendation:
Role Handoff: NONE / ROLE + REASON
```

无实质问题必须允许 `LEVEL 0 / KEEP / NO CHANGE`。上下文不足时用 `NEEDS CONTEXT / UNDERDETERMINED`，不得用“可能”包装成事实。

## REWRITE MODE

`AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`

仅在用户明确要求改写，且 Meaning、人物、Receiver、关系、目的和 Conversation State 足够时启用：

`Meaning Lock → Interaction Context → Social Function → Minimal Candidate → Meaning / Power / Reveal / State Check`

固定输出：

```text
Mode: REWRITE — EXPLICIT USER REQUEST
Register:
Meaning Lock:
Interaction Context:
Original:
Natural Rewrite:
Meaning Check:
Residual Warning:
Role Handoff:
```

不得把回避改坦白、把怀疑改知识、把请求改命令、把未回应问题抹掉或把人物改成更高自省。资料不足时 `Natural Rewrite: NOT PROVIDED — NEEDS CONTEXT`。

## 工作流程

`SYNTHESIZED INFERENCE + AI FILM STUDIO SYNTHESIS｜DEFAULT HEURISTIC`

### Input

- Original / interaction span；
- WHO / RECEIVER / relationship；
- situation / medium / publicness；
- current purpose、knowledge、risk；
- preceding conversation state；
- Register、Requested Mode、Meaning / Canon。

### Judgment

1. 建 Context Card；未知项明确为空。
2. 先锁 Meaning、Information Reveal 与 Power，阻止读心和偷修。
3. 跑 Receiver Matters，确认表达对象与实际关系。
4. 跑 Intended / Spoken / Received / Response，定位差异而不预设差异。
5. 更新 Conversation State；查回应是否接住、回避或遗忘前文。
6. 条件性调用 Misalignment、Silence、Social Position、Ordinary Motive、Detail、Self-Interpretation。
7. 运行 Social Plausibility 与反机械检查。

### Decision

- `LEVEL 0 → KEEP / NO CHANGE`
- `LEVEL 1 → PASS / OPTIONAL NOTE`
- `LEVEL 2 → PASS WITH NOTES / TARGETED LANGUAGE DIRECTION`
- `LEVEL 3 → RETURN FOR LANGUAGE REVISION`
- `LEVEL 4 → ROLE HANDOFF / WARNING`
- `LEVEL 5 → BLOCKED`

### Output

给出互动问题发生在哪一层、证据、影响、最小方向和岗位边界。QA 不写整场；Rewrite 只给保义、保关系、保状态的局部候选。

## 诊断问题

`SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS｜OPTIONAL TOOL`

1. 这句话具体说给谁，为什么对这个人说？
2. 名义关系与实际信任、权力和风险是否一致？
3. 说话者想完成什么，实际说出了多少？
4. Receiver 有何知识、利益和注意点，可能接收到什么？
5. 回应是在答原问题、保护自己，还是处理另一个紧迫问题？
6. 错位有文本证据，还是 QA 在脑补？
7. 沉默/动作是否最低限度更新了交流状态？
8. 人物是否精确理解自己到超出其状态；也可能确实有这种能力吗？
9. 小事/物件是否承载关系，还是只装生活化？
10. 后一句是否记得前面已拒绝、回避和未回答的内容？
11. 所有人是否都在帮作者总结同一主题？
12. 当前交流即使低效，是否仍合理完成维持关系、避险或程序任务？
13. 原交流是否已经自然，应该 `NO CHANGE`？

## 失败模式

|失败|表现|根因|
|---|---|---|
|透明传输|每个人都准确收到并解释原意|把人当共享状态模型|
|AI 共情|争吵中立刻准确命名对方需求|未查人物能力、关系与压力|
|机械错位|每段都答非所问|把症状当风格|
|沉默崇拜|用停顿/动作装高级|没有社会理由和状态更新|
|低效崇拜|越重复、含混越真实|把信息损耗当真人证明|
|小动机崇拜|大理想/自省一律判假|忽略人物能力和任务|
|生活物件配额|每场硬塞吃饭、钱、钥匙|把具体性变装饰|
|读心 QA|给错位/沉默编完整心理|输入不足却伪确定|
|状态失忆|每句单独自然，后文忘记回避/拒绝|未保留 Conversation State|
|作者合唱团|人物轮流完成统一主题论证|人物注意力与认知独立性消失|
|假生活化|网络词/填充词堆叠|用表面口语替代关系判断|
|正常交流误杀|问时间、回答可以也被强加潜台词|把复杂性做成硬门|

## 修正方法

1. `AI Cooperation` → 分开人物各自注意点、利益和压力；只建议恢复差异，不发明冲突。`DEFAULT HEURISTIC`
2. `Unproven Misalignment` → 标出未知动机，请求最少上下文；不自动改回直接回答。`HARD CONSTRAINT`
3. `Mechanical Silence` → 要求说明不说的理由、Receiver 可读信号和状态变化；否则保留明确表达。`CONDITIONAL METHOD`
4. `Social Position Stereotype` → 用具体权力、风险和组织环境替换身份标签。`DEFAULT HEURISTIC`
5. `Abstract Relationship Talk` → 查找已存在的具体事件锚；不新增生活道具。`CONDITIONAL METHOD`
6. `Over-Self-Diagnosis` → 分开 Canon 实态、人物认识和愿意承认；QA 不替写心理。`CONDITIONAL METHOD`
7. `State Amnesia` → 建一行状态表：未答问题 / 情绪 / 主动权 / 承诺；逐轮更新。`OPTIONAL TOOL`
8. `Over-Editing` → 若互动已适合人物、关系、目的与 Register，输出 `KEEP / NO CHANGE`。`HARD CONSTRAINT`

## 禁止继承

- 刘震云个人文风、幽默、荒诞、反讽、句法节奏、短句、句号/分号偏好；
- 河南/延津地域语言、方言、家常话、时代口语或作品人格；
- 具体作品、人物、情节、媒介冲突、标志性对白或比喻；
- 每场误解、答非所问、沉默、欲言又止、谎言、废话或生活小事配额；
- “真实 = 低效/不清楚/不自知”“亲人不知心、陌生人更知心”等反常模板；
- 来源中的任何数字比例或每日句数；
- 用 2025 访谈替代 2026 网络流行度证据；
- 替 Scene Writer 改整场、替 Character & Acting 设计完整 voice、替 Showrunner 修故事逻辑。

## 可 Skill 化规则

```text
RULE 1 — INTERACTION UNIT [HARD]
Judge an exchange with its preceding state, not isolated polished lines.

RULE 2 — RECEIVER REQUIRED [HARD]
Identify the actual receiver, relationship, risk and purpose before a firm social-plausibility judgment.

RULE 3 — NON-TRANSPARENT COMMUNICATION [DEFAULT]
Compare intended, spoken, received and response layers; permit both alignment and divergence.

RULE 4 — NO MISALIGNMENT QUOTA [HARD]
Never add misunderstanding, evasion or conflict merely to look human.

RULE 5 — SILENCE FUNCTION [CONDITIONAL]
Accept silence or action as response only when context supports a social function and state update.

RULE 6 — SOCIAL POSITION, NOT STEREOTYPE [DEFAULT]
Use actual power, risk, dependence and publicness; never map roles to fixed lines.

RULE 7 — ORDINARY MOTIVE WITHOUT SMALLNESS BIAS [DEFAULT]
Seek the immediate communicative action, while allowing ideals and self-awareness when supported.

RULE 8 — DETAIL FIT [DEFAULT]
Use existing concrete anchors only when they fit character, knowledge, relationship and task; no object quota.

RULE 9 — SELF-INTERPRETATION GAP [CONDITIONAL]
Separate actual state, self-knowledge, admission and speech; never inject omniscient psychology.

RULE 10 — CONVERSATION STATE [HARD]
Track answered, avoided and unresolved issues plus emotion and control across turns.

RULE 11 — NO CHANGE [HARD]
Clear, cooperative and ordinary communication may pass; do not force complexity.

RULE 12 — CONTEMPORARY HANDOFF [HARD]
Judge character/context fit only; hand current slang popularity to Contemporary Language Layer.

RULE 13 — ROLE BOUNDARY [HARD]
Keep Speaker Fit, Meaning, prose naturalness, syntax, scene design and acting with their owners.

RULE 14 — NO STYLE INHERITANCE [HARD]
Never imitate Liu Zhenyun or reproduce his regional, comic or work-specific surface features.
```

## 证据与来源

核心证据 `4`；第一手内容 `4/4 = 100%`；二手核心 `0`。唯一 ID、载体限制、Claim Map 与不可外推边界见 `_research/Liu_Zhenyun_Language_Voice_QA_V0.1/00-canonical-evidence-ledger.md`。

|ID|来源|核心贡献|
|---|---|---|
|LZY-01|[中国作家网｜刘震云：写作向彼岸靠近](https://www.chinawriter.com.cn/n1/2022/1118/c405057-32569482.html)|前后联结；场合/媒介/关系改变说话；嘴与心；欲言又止；日常话语功能|
|LZY-02|[中国作家网｜刘震云对话北大师生](https://www.chinawriter.com.cn/2015/2015-06-15/245638.html)|人物认知独立；言外内容；知心话接收者；名义关系与实际亲密差异。媒体整理记录，非已验证逐字稿|
|LZY-03|[中国作家网｜刘震云谈新作](https://image.chinawriter.com.cn/n1/2025/1219/c405057-40627614.html)|生活底部与概念边界；细节—人物性格/见识适配；反机械因果；个人短句/分号只作 Style 风险|
|LZY-04|[中国作家网｜2017 BIBF 刘震云与马东对谈](https://www.chinawriter.com.cn/n1/2017/0829/c405057-29500156.html)|直接支持人物想说但无人听、作者自述倾听人物、表面不说与内在活动；“人物不作作者话筒”为与 LZY-02 交叉后的综合推断；授权刊发、略有删节的公开实录|

## Codex 可执行性测试 A–O

### TEST A｜AI 高质量沟通

- Register：R4；Context Confidence：MEDIUM。
- 问题：B 的回应同时准确命名原因、对方感受和未被重视的需要；在“正在争吵”条件下存在 `AI COOPERATION / RESPONSE PRECISION` 风险。
- Interaction Fit：刘模块只判断该回应精度是否超过两人的关系历史、当前争吵压力与 B 的互动目的。
- Speaker Fit Handoff：B 是否受过沟通训练、一贯防御或具备这种个人表达能力，由老舍接口 / Character & Acting 确认。
- 边界：输入没有 B 的沟通训练、既往相处方式或是否在复盘；不能断言任何真人都不会这样说。
- Decision：`LEVEL 2 / PASS WITH NOTES + REQUEST CHARACTER CONTEXT`。若 B 一贯防御且高压，此句应返工；若 B 受过训练、已多次讨论或在主动修复，可 PASS。QA 不给替代台词。
- 结果：`PASS`。

### TEST B｜现实错位

- Original：A 问昨晚没回来，B 问冰箱有没有菜。
- 可能是回避、没听清、另一紧急需要、准备解释的前置，也可能是作者漏接。
- Decision：`NEEDS CONTEXT / UNDERDETERMINED`。不得自动判坏，不补写原因。
- 结果：`PASS`。

### TEST C｜沉默与钥匙

- 沉默 + 推钥匙至少构成可观察回应，并更新物件控制/谈话状态。
- “承认、离开、交还权限、绝交”等具体意义均未由输入证明。
- Decision：`FUNCTION PLAUSIBLE / MEANING UNDERDETERMINED / PASS WITH CONTEXT WARNING`。
- 结果：`PASS`。

### TEST D｜生活小事承载关系

- A 抽象“信任缺失”：若人物在咨询、复盘或惯于抽象表达，可成立；争吵现场可能过度总结。
- B “第三次晚回来”：提供可验证事件锚，适合质问，但可能回避真正目的或不适合正式关系总结。
- Decision：`NO UNIVERSAL WINNER`；按人物、Register、目的选择。
- 结果：`PASS`。

### TEST E｜Self-Interpretation Gap

- Story Fact 已知人物嫉妒；人物只说对方不可靠，可以是自我解释不足、拒绝承认或其真实判断的一部分。
- QA 不把“我嫉妒”写入对白；需看人物是否知道/愿认。
- Decision：`PASS / CONDITIONAL GAP`。
- 结果：`PASS`。

### TEST F｜正常明确沟通

- “明天下午三点开会，你能来吗？”“可以。”
- 目的、接收、回应和状态均清楚，无需潜台词或错位。
- Decision：`LEVEL 0 / KEEP / NO CHANGE`。
- 结果：`PASS`。

### TEST G｜所有人都懂主题

- 三人依次用同一抽象层完成系统认可—身份—价值机制论证。
- Problem：`AUTHORIAL COLLABORATION + SHARED COGNITION WITHOUT EVIDENCE`。
- Decision：`LEVEL 4 / ROLE HANDOFF TO SCENE WRITER`；核查各自注意点和争议，不由 QA 写整场。
- 结果：`PASS`。

### TEST H｜社会位置

- “你错了”与“这个数据是不是还得再看一下”均非自动真实版本。
- 取决于员工性格、错误风险、领导容错、会议公开性、证据确定度和组织文化。
- Decision：`NEEDS CONTEXT / NO UNIVERSAL WINNER`。
- 结果：`PASS`。

### TEST I｜网络用语

- “今天班味有点重”只检查年轻角色是否接触、Receiver 是否理解、场景和目的是否容纳。
- 流行度：`CONTEMPORARY USAGE UNKNOWN`。
- Handoff：`Contemporary Language Layer`。
- 结果：`PASS`。

### TEST J｜Conversation Memory

原创六轮：

1. A：“报名表交了吗？”
2. B：“打印机坏了。”
3. A：“我问的是你交没交。”
4. B：“我下午去公司。”
5. A：“所以你还没交，对吗？”
6. B：“没有。三点前交。”

状态：任务给定第 2 轮是“回避”，但台词本身只能证明它未直接回答，提交状态仍为 `UNKNOWN`；若不采用任务给定事实，回避动机也应标 `UNDERDETERMINED`。第 3 轮重问；第 4 轮仍未确认是否提交，只新增“下午去公司”，这与提交的关系仍 `UNDERDETERMINED`；第 5 轮准确重开未答问题；第 6 轮明确“未交”并新增“三点前提交”的承诺。整段记得前文，不因第 2/4 轮非直接回应自动失败，也不从表层台词脑补因果。

Decision：`PASS`。

### TEST K｜普通人的小动机

- “不想重复失去信任的创伤”需要较高自省、抽象能力和此刻承认意愿。
- “怕你知道了又要吵”是更局部的避冲突动机，但不是自动优选。
- Decision：按人物能力、关系和当前目的；`NO SMALLNESS BIAS`。
- 结果：`PASS`。

### TEST L｜接收者改变说法

同一事实面对母亲、一般同事、银行工作人员、亲近朋友时，可能改变披露原因、请求类型、正式度、证明材料和羞耻风险。QA 先问各方关系与目的；不生成四套固定句式。

Decision：`PASS`。

### TEST M｜真实但低效

原创：A：“你去医院了吗？”B：“早上人太多。”A：“所以没去？”B：“我在门口坐了会儿。”A：“药呢？”B：“还剩两片。”

它低效且多次不直接回答，但可能显示回避、疲惫或尚未完成就医；输入不足时不能断言心理，也不能只为效率改成完整报告。Decision：`NEEDS CONTEXT / DO NOT OPTIMIZE AUTOMATICALLY`。

结果：`PASS`。

### TEST N｜AI 假生活化

- 47 岁严肃法务主管在正式内部会议说高密网络口语。
- Problem：人物/组织/Register/信息任务共同失配；并非单个网络词自动失败。
- Decision：`LEVEL 3 / RETURN FOR LANGUAGE REVISION`；流行度仍 Handoff。
- 结果：`PASS`。

### TEST O｜NO CHANGE

- “你吃了吗？”“还没。”在合理朋友日常语境中完成普通问答。
- Decision：`LEVEL 0 / KEEP / NO CHANGE`。不强加戏剧价值。
- 结果：`PASS`。

## Rewrite 回归测试

### REWRITE R1｜信息充分

- Mode：`REWRITE — EXPLICIT USER REQUEST`；R4。
- Context：三年伴侣争吵；B 是防御型工程师，知道近期工作忙且有具体失约，声称理解 A 的感受，认为工作忙可能使 A 感到被忽视，同时想否认“不在乎”并要求只讨论具体失约；不具治疗式表达习惯。
- Meaning Lock：声称理解 A 的感受；工作忙可能造成被忽视感，必须保留“可能”的不确定性；否认不在乎；只讨论具体失约；保持争吵压力，不新增事件。
- Original：“我理解你的感受。可能是因为我最近工作太忙，让你觉得自己没有被重视。”
- Natural Rewrite：“我知道我最近工作太忙，可能让你觉得自己没被重视。可这不等于我不在乎你。你说的是哪次失约，我们就说哪次。”
- Meaning Check：保留对 A 感受的理解声明、工作忙与被忽视感之间的暂定因果及“可能”强度；依据已给 Context 保留否认和只讨论具体失约的范围；未扩展为任意“没做好”的事情，也未新增事件、承诺或心理诊断。权力关系、信息披露和当前争吵状态未改变。
- Residual Warning：若 B 实际想道歉或没有防御倾向，此版不适用。
- 结果：`PASS`。

### REWRITE R2｜信息不足

- 用户要求把 TEST B 改得“更像真人”，但未说明 B 的目的、是否听见、关系或紧迫事项。
- Natural Rewrite：`NOT PROVIDED — NEEDS CONTEXT`。
- 请求：B 是否听见、是否回避、双方关系、冰箱问题为何现在紧迫。
- 结果：`PASS`。没有用示例候选绕过输入门。

## 综合测试｜服从规则与保住一个人

- **R1 Creative Discussion**：这是供创作者讨论的抽象冲突句；刘模块只问它是否对具体协作者完成讨论任务。二元是否成立、主题是否过早由 Showrunner/汪曾祺/叶圣陶接口判断。
- **R4 Character Dialogue**：需检查人物是否会对当前 Receiver 如此完整地概括“规则/保住/选择”，以及双方是否已共享制度与对象。若只是作者借人物总结，标 `INTERACTION FIT RISK`；高自省、正式谈判或已充分讨论时可成立。
- 边界：不接管 Syntax、Anti-Rhetoric、Meaning 或完整 Speaker Fit。
- 结果：`PASS`。

## Codex 审核结论

Codex 最终审核：`PASS`。

- huashu-nuwa：已实际调用；收据、完整来源笔记、唯一 Evidence Ledger 与女娲过程记录均在研究目录。
- 证据红队：`PASS`。核心一手内容 `4/4 = 100%`；LZY-02/04 的媒体记录性质、LZY-03 的 2025 日期、直接支持/综合推断/项目合成及 Style/Modernity 边界全部通过。
- 内容与岗位边界：`PASS`。十个能力模块、四类规则、Input → Judgment → Decision → Output、QA/Rewrite、Meaning/Severity/Handoff、老舍 SPEAKER FIT 与刘震云 INTERACTION FIT 的职责切分全部通过。
- 可执行性干跑：`TEST A–O = 15/15 PASS`；Rewrite R1/R2 与综合 Register 边界测试全部通过；正常明确沟通与日常问答均能 `NO CHANGE`。
- 返工：`2 轮定向返工`。第一轮修正 TEST J 的动机脑补、Rewrite R1 的共情/暂定因果/范围漂移，并统一 TEST G Handoff 等级与 TEST A 职责分流；第二轮收紧 LZY-03/LZY-04 provenance 标签并统一四份核心计数。
- Style Imitation Risk：`HIGH / CONTROLLED`。未继承短句、分号、地域语言、幽默、荒诞、作品人物或情节。
- Modernity Risk：`LOW-MEDIUM / CONTROLLED`。2025 材料只作较新锚点；2026 网络流行度明确 Handoff。
- 未解决阻塞：`NONE`。
- 发布决定：允许通过现有 `publish_to_obsidian.py` 执行受控发布。
