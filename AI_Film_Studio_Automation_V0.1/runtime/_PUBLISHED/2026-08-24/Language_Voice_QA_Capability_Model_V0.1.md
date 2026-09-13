---
type: capability-model
status: approved
review_result: passed
version: 0.1
domain: Language & Voice QA
subject: Language & Voice QA 综合能力模型
model_scope: executable-judgment-architecture
nuwa_skill: huashu-nuwa
---

# AI Film Studio｜Language & Voice QA 综合能力模型 V0.1

> `FORMAL PROJECT SOURCE`：Approved Capability Charter 与五人 Cross-Distillation。  
> `AI FILM STUDIO SYNTHESIS`：本文件对已批准方法的可执行转译。  
> 本文件不是 Production Skill、Runtime、Runtime Gate 或自动改写器；它只定义未来实现必须遵守的判断架构。

## 模型目标

建立可执行的：

`INPUT → STATE → ROUTE → DETECT → ARBITRATE → DECIDE → OPTIONAL REWRITE → SAFETY CHECK → OUTPUT`

它回答：什么输入足够、何时停止、问题归谁、何时请求 Context、何时可改写、最多改多少、何时 Handoff，以及如何防止 QA 自己产生 AI 味或越权创作。

## 输入与范围

### 直接方法基线

|ID|正式输入|用途|
|---|---|---|
|CM-CHARTER|Language & Voice QA Capability Charter V0.1|输入契约、R1–R8、AP-01–18、Meaning Gate、Mode、Severity、岗位边界|
|CM-CROSS|Language & Voice QA 五人交叉蒸馏 V0.1|共享底座、五层、24 条关系、Ownership、19 条规则、测试与防机械护栏|

五份单人蒸馏仅为 Source Provenance / Fallback Reference，不能绕过 CM-CHARTER 或 CM-CROSS 引入新规则。完整来源映射见研究账本。

### 明确不在范围内

- 不创建或安装 `SKILL.md`，不修改 Runtime、Showrunner、Contemporary Language Layer 或 Scene Writer。
- 不生成角色 voice bible、场景、镜头、表演、故事修复、世界命名或 Canon 内容。
- 不重做人物蒸馏，不把任何个人风格写入模型。

## 统一运行主链

### LANGUAGE & VOICE QA DECISION FLOW

```text
INTAKE
  → INPUT STATE
  → MODE ROUTER
  → REGISTER ROUTER
  → CONTEXT SUFFICIENCY
  → MEANING / AUTHORITY GATE
  → EARLY EXIT / NEED-FOR-CHANGE
  → DETECTION PLAN
  → PRIMARY DETECTOR
  → SECONDARY CONFIRMATION (only if it changes confidence, owner, or severity)
  → SEVERITY ARBITRATION
  → FINAL DECISION
      ├─ QA OUTPUT / HANDOFF
      └─ EXPLICIT REWRITE ONLY
          → MINIMUM NECESSARY REWRITE
          → MEANING / REGISTER / ROLE SAFETY REGRESSION
          → FINAL OUTPUT OR TARGETED CORRECTION
```

### 顺序裁决

- Register 在检测前决定路径；Meaning / Canon 在建议与改写前设不可越过的边界。
- Early Exit 在检测前运行：没有明确问题与净收益时，不进入深层模块。
- Primary Detector 先出一个发现；Secondary 只补充证据、影响或交接，不能生成第二份同义诊断。
- 条件冲突以：`Meaning / Canon → User Intent → Register → Character / Context → Clarity → Naturalness → Style Preference` 裁决。

## Capability Stack

模型采用 `9` 层，既覆盖完整判断链，又避免把五个语言层机械地全部运行。

|层|Input|Question|Trigger|Possible Decision|Next|Early Exit|Handoff|
|---|---|---|---|---|---|---|---|
|S1 Intake & Input State|Original、Mode、已知 Context|信息处于 SUFFICIENT / PARTIAL / INSUFFICIENT？|每次请求|BLOCKED / PARTIAL QA / CONTEXT NEEDED|S2|无 Original → BLOCKED|请求用户或上游最少字段|
|S2 Mode & Register Router|用途、Mode、R1–R8|以什么契约、容忍度和模块组合判断？|S1 可继续|QA / Rewrite route；Register candidate|S3|不确定但结论不变可保守继续|Register clarification|
|S3 Meaning & Authority Gate|文本、Canon、用户意图|什么必须不变，用户是否已确认有意风格？|任何建议/Rewrite|Meaning Lock / Warning / Canon Block|S4|保护项稳定、无修改授权时不改|Continuity / User Canon Decision|
|S4 Early Exit & Need for Change|当前文本、Register、Meaning|是否有可定位且影响当前任务的问题？|S3 通过|NO CHANGE 或 detection plan|S5|无净收益 → PASS / NO CHANGE|无|
|S5 Detection Planner|AP 标签、Register、Context|唯一 Primary Owner 是谁；需不需要 Secondary？|S4 命中问题|Primary + optional Secondary|S6|无候选问题 → PASS|对应岗位|
|S6 Detection Modules|被路由的文本/交流|自然、结构、人物、互动、创作会议、术语是否出现实际损失？|模块触发条件满足|Finding / Context Needed / Handoff|S7|模块不成立 → 回 S4 NO CHANGE|Module-specific owner|
|S7 Arbitration & Boundary|Primary finding、Secondary、Style/User constraints|最终影响、等级和角色边界是什么？|S6 有结论|LEVEL 0–5 + final state|S8|LEVEL 0–1 且无 Rewrite 授权 → output|Showrunner / Scene Writer / Character & Acting / Continuity 等|
|S8 Optional Rewrite & Safety|显式 Rewrite 授权、稳定 Meaning|最小必要修复是什么，是否保义/保 Register/保边界？|仅 Rewrite Mode 且 Benefit 通过|Rewrite delivered / targeted correction / blocked|S9|无授权或收益不明 → 回 QA output|原岗位或用户澄清|
|S9 Output Contract & Finite Loops|final state、证据、建议|如何紧凑交付；新信息是否改变状态？|每个结论|final QA / rewrite / handoff|终止或合法回环|Context / Register / Rewrite correction|

## Project State / Input State

|Input State|最低条件|允许的判断|禁止的判断|典型输出|
|---|---|---|---|---|
|SUFFICIENT|Original 存在；当前路由所需的决定性 Context 已知；Rewrite 另需可锁 Meaning|可作确定 QA；满足授权和收益时可 Rewrite|无|进入正常路径|
|PARTIAL|Original 存在，但缺少不会阻止局部判断的字段|可作条件性、局部或 Register 分支 QA|不得对缺失字段作强归因或给确定 Rewrite|`PASS WITH NOTES` / `REGISTER UNCERTAIN` / 条件 Warning|
|INSUFFICIENT|Original 缺失，或当前必要决定项缺失且会改变结论|只能指出缺失项并请求最少 Context|不得猜人物、关系、术语定义、世界事实、作者意图|`BLOCKED` 或 `NEEDS CONTEXT`|

### 正交 State Vector

下列状态是并列维度，不与 Severity 或 Final Decision 混为一个大状态：

|State Dimension|Allowed Values|作用|
|---|---|---|
|OriginalState|PRESENT / MISSING|MISSING 直接阻止 QA|
|ModeState|QA_DEFAULT / REWRITE_EXPLICIT|限制是否能产出候选改写|
|RegisterState|R1–R8 / REGISTER_UNCERTAIN|选择路径与风格保护|
|ContextState|SUFFICIENT / PARTIAL / INSUFFICIENT|限制可作强判断的模块|
|MeaningLockState|NOT_NEEDED_YET / PARTIAL_LOCK / LOCKED / RISK|追踪保护项是否可安全比较|
|TermState|NOT_APPLICABLE / KNOWN PROJECT TERM / COMMON TERM / UNVERIFIED COINAGE / CONTEXT REQUIRED|限制术语结论与命名权限|
|RouteState|UNROUTED / ROUTED / NO_DETECTION_NEEDED / HANDOFF_REQUIRED|记录实际启动模块、Early Exit 或交接状态|

`REGISTER_UNCERTAIN`、`MEANING WARNING`、`CONTEMPORARY USAGE CHECK REQUIRED` 都是限定符／风险标记，不是 Severity 或 Final Decision。

### 必要 Context 的动态门

-`ContextState`描述整份输入的总体可用性；任一模块的决定性字段缺失时，该模块单独标记`MODULE CONTEXT INSUFFICIENT`。整体仍可为`PARTIAL`，且其他不依赖该字段的模块可作限域判断。
- R4 Speaker Fit：WHO、TO WHOM、WHY NOW、知识/承认、关系/压力缺失时，不作“人物不会这样说”的确定结论。
- R4 Interaction Fit：至少一轮互动与前序 Conversation State 缺失时，不判定互动真实/不真实。
- Register 结论会改变时：`REGISTER UNCERTAIN`，请求用途；结论不变时可按保守路径继续。
- Unverified Coinage：世界定义、使用者、正式性、必要区分未知时，不命名、不改名。
- 有意风格：Intent 或用途不明时，只报告条件风险，不作风格正常化。
- 当代语言：依赖实时热度、平台、代际或过时判断时，必须 Contemporary Handoff。

## MODE Router

|Mode|进入条件|运行权限|输出|
|---|---|---|---|
|QA MODE|默认；用户请求检查、判断、审核，或未明确授权改写|诊断、说明、定向动作、Handoff；不提供替换句|Decision、Severity、Primary Finding、Why、Evidence、Action、Secondary、Handoff|
|REWRITE MODE|用户明确请求改写、自然化、去 AI 味、修正表达等|必须先完成 QA、Meaning Lock、Benefit；只给最小必要候选|Original Meaning、Detected Problem、Rewritten Version、Meaning Check、Residual Warning、Handoff|

`Original → 自由重写` 是无效路径。Mode 有歧义时先 QA；若用户同一请求同时要求检查和改写，则 QA 先于 Rewrite。

## R1–R8 Register Router

|Register|Primary Checks|Secondary Checks|Normally Skipped|Style Freedom|Rewrite Threshold|Handoff Conditions|
|---|---|---|---|---|---|---|
|R1 Creative Discussion|Meaning Integrity、Natural Expression、Creator-Room|Structural Chinese（实际负担时）|Speaker/Interaction|暂定、探索、未完成思考受保护|遮蔽条件、因果、证据或探索空间且用户要求改写|主题/故事因果未定 → Showrunner|
|R2 Project Brief|Meaning Integrity、Structural Chinese、Abstraction Mapback|Natural Expression|Speaker/Interaction|专业术语、抽象、字段与版本状态受保护|交接、责任、范围或可检索性被实际妨碍|对象/验收/项目决策未定 → Showrunner / 原岗位|
|R3 Showrunner Diagnosis|Meaning Integrity、Creator-Room、Natural Expression|Structural Chinese、Pseudo-precision|Speaker/Interaction|判断链与定义性术语受保护|空泛高层话、伪精确或总结遮蔽判断链|故事根因、主题、范围 → Showrunner|
|R4 Character Dialogue|Meaning Integrity、Speaker Fit、Interaction Fit（有互动跨度）|Natural / Structure（触发时）|Creator-Room（除非对白内出现作者总结）|完整表达、专业角色、沉默、回避、风格化表达均可成立|人物/互动条件充分、语言层问题明确且用户授权|场景 beat → Scene Writer；深层 voice/表演 → Scene Writer + Character & Acting|
|R5 Scene Description|Meaning Integrity、Structural Chinese、信息顺序|Natural Expression|Speaker/Interaction|可见状态、动作、空间精度受保护|动作主体、顺序或可见信息造成执行误解|镜头/表演/视觉决定 → Director / Art Director|
|R6 Narrative Prose|Meaning Integrity、Natural Expression|Structural Chinese（实际负担时）|Speaker/Interaction（除非直接引语）|文学性、节奏、长短句与有意修辞受保护|视角、信息控制或阅读任务出现可定位损失|内容/主题/情节决定 → 原创作岗位|
|R7 Production Note|Meaning Integrity、Structural Chinese|Natural Expression|Speaker/Interaction、Creator-Room|术语、列表、条件、重复关键约束受保护|责任、条件、验收、状态或歧义受影响|制作范围/可行性 → Showrunner / Production Reality|
|R8 Marketing Copy|Meaning Integrity、Style Freedom、Natural Expression|Term Plausibility|Speaker/Interaction、Creator-Room|压缩、修辞、平行、诗性、抽象、钩子结构受保护|承诺不可兑现、术语无定义或误导受众且用户授权|事实兑现、品牌/受众策略 → Marketing owner / Showrunner|

## MEANING LOCK

### Required Protection Fields

每次进入 Rewrite 前，提取**输入实际支持**的字段；不存在或未知的字段必须写未知，不能补齐。

|Field|锁定内容|
|---|---|
|Fact|人物、时间、地点、事件、状态、范围|
|Character Intent|说话／行动想达成什么|
|Canon|锁定设定与权威版本|
|Causal Relationship|原因、条件、结果、责任归属|
|Theme Direction|当前探索或已锁定的价值张力|
|Information Reveal|谁在何时知道什么|
|Power Relationship|命令、请求、拒绝、权限、地位|
|Emotional State|克制、失控、回避、迟疑、自知程度|
|Register / Task|当前文本必须完成的用途与风格许可|

### Gate Decisions

- Meaning 无法可靠确认：禁止 Rewrite，输出 `NEEDS CONTEXT`、`ROLE HANDOFF` 或 `BLOCKED`。
- 与 locked Canon 冲突：`BLOCKED FOR CANON DECISION`，不以语言修正覆盖。
- 用户明确保留的创意表达：在不违反 Meaning/Canon 等更高硬约束时，进入 `INTENTIONAL STYLE PROTECTION`。

## Early Exit / NO CHANGE

### Stop Condition

若以下均成立：

1. Register 合理；
2. Meaning 清楚且无 Canon 风险；
3. 无足以影响理解、自然度、角色真实性、互动真实性或结构可读性的可定位问题；
4. 任何候选 Rewrite 均无明确净收益；

则输出 `LEVEL 0 / PASS / NO CHANGE`，终止所有未触发模块。不得继续“寻找一点可优化之处”。

## Detection Ownership

### Ownership Contract

每个问题只输出 `ONE PRIMARY FINDING`：

`Primary Owner → one diagnosis → optional Secondary Confirmation → one final severity / action`

Secondary 只有在改变置信度、严重度、Meaning 风险或 Handoff Target 时才可出现。

|AP|Route Gate|Primary Detector|Secondary Signal|Handoff Target|
|---|---|---|---|---|
|AP-01 ABSTRACT THESIS|—|Meaning Integrity|Natural Expression|Showrunner / 原创作岗位|
|AP-02 ARTIFICIAL BINARY CONTRAST|—|Meaning Integrity|Natural Expression|Showrunner|
|AP-03 TRAILER-COPY COMPRESSION|Register Router|Natural Expression|Meaning Integrity|R1/R2：Showrunner；R8：Marketing owner|
|AP-04 INVENTED TERM WITHOUT SOCIAL PROOF|Term State|Term & Contemporary Boundary|Meaning Integrity、Interaction Fit|World / Showrunner / 原创作岗位|
|AP-05 TRANSLATION-LIKE CHINESE|—|Structural Chinese|Natural Expression|原岗位；内容未定 → Showrunner|
|AP-06 ABSTRACT NOUN STACKING|—|Structural Chinese|Meaning Integrity、Natural Expression|Showrunner / 原岗位|
|AP-07 OVER-EXPLANATION|—|Natural Expression|Meaning Integrity|原岗位|
|AP-08 EXCESSIVE SUMMARY|—|Natural Expression|Meaning Integrity|Showrunner|
|AP-09 SLOGANIZATION|—|Natural Expression|Register Router / Style Protection|Showrunner / Marketing owner|
|AP-10 SYMMETRICAL RHETORIC|—|Natural Expression|Register Router、Meaning Integrity|原岗位|
|AP-11 EMPTY HIGH-LEVEL WORDING|—|Meaning Integrity|Natural Expression、Structural Chinese|Showrunner|
|AP-12 PSEUDO-PRECISION|—|Meaning Integrity|Structural Chinese|用户 / Showrunner / 证据所有者|
|AP-13 GENERIC CHARACTER SPEECH|R4 + Speaker Context|Speaker Fit|Interaction Fit|Character & Acting / Scene Writer|
|AP-14 EXPOSITIONAL DIALOGUE|R4 + Speaker Context|Speaker Fit|Interaction Fit、Meaning Integrity|Scene Writer|
|AP-15 PERFECTLY ARTICULATE EMOTION|R4 + Speaker Context|Speaker Fit|Interaction Fit、Emotional State|Character & Acting / Scene Writer|
|AP-16 UNNATURAL INFORMATION DENSITY|R4 / non-R4 route|R4：Speaker Fit；其他：Structural Chinese|R4：Interaction Fit；其他：Natural Expression|R4：Scene Writer / Character & Acting；内容：Showrunner|
|AP-17 AI CONNECTOR OVERUSE|—|Structural Chinese|Meaning Integrity、Natural Expression|原岗位；逻辑未定 → Showrunner|
|AP-18 FAKE CASUALNESS|R4 / non-R4 route|R4：Speaker Fit；其他：Natural Expression|Interaction Fit、Structural Chinese|Character & Acting；实时用法 → Contemporary Layer|

`Route Gate`选择路径，不是问题的 Primary Detector。Register 被解析后，每个已启动问题只保留一个 Primary Detector；AP-16、AP-18 等分叉条目也必须先完成路由，再在该路径上选择唯一 Primary。

## Core Detection Modules

|Module|Trigger|Core Question|Output Boundary|
|---|---|---|---|
|Meaning Integrity|强断言、因果、范围、主题、术语、任何 Rewrite|文本实际断言什么；是否超出已知事实或锁定意义？|定位意义风险；不解决故事本身|
|Natural Expression|过写、总结、修辞、空抽象、假口语、段落断裂信号|表达是否在当前任务中替代了事实、行动、关系或信息接力？|给实际效果；不把自然等同口语/短句|
|Structural Chinese|名词化、介词链、弱动词、被动、连接、主语、信息顺序信号|主干、主体、动作、逻辑与信息释放是否产生实际理解成本？|只改结构功能；不纯化、不删术语|
|Speaker Fit|R4 单句，且人物/关系/压力 Context 足够|这个人对这个 Receiver 知道、愿意、能够、会如此说吗？|不建立长期 voice，不重写场景|
|Interaction Fit|R4 有互动跨度及 Conversation State|意图、说出、接收、回应和状态是否可解释？|不强加误解、沉默或低效|
|Creator-Room Naturalness|R1/R3 的高压缩、海报式、主题化或总结式表达|内部创作者会自然这样用来理解、讨论或决定下一步吗？|不将开发讨论聊天化；内容问题交 Showrunner|
|Term & Contemporary Boundary|新词、行话、机构名、网络语、实时使用主张|术语有定义/使用群体/必要区分吗；是否需要实时社会证据？|世界命名交上游；趋势交未来 Contemporary Layer|

## Natural Expression Protocol

按当前任务检查：Anti-Overwriting、Anti-Rhetoric、Empty Abstraction、Concrete Anchor、Restraint、Whole-Context 与 Fake Casualness。

`AI-Rhetoric Cluster`（如“不是……而是……”“A 与 B 之间”“真正／本质／核心”“不仅……更”“重新定义／确认”及抽象价值词群）只是一组**信号**。必须结合 `Frequency + Context + Register + Intent + Meaning Impact`；单个结构不构成 FAIL。R8 可进入 Style Protection；R4 先看人物与互动语境；R1/R3 先运行 Creator-Room Check。

## Structural Chinese Protocol

按实际理解成本而非词形运行：Nominalization、Preposition Chain、Weak / Empty Verb、Passive Necessity、Connector Load、Subject Stability、Information Order、Structural Packaging。

`ANTI-PURISM`：没有词语黑名单、句长阈值、“的”字配额、被动禁令或“进行”禁令。外来影响、专业词、被动、名词化和长句都可能合法；仅当它们妨碍当前 Register 的理解、责任或交接时才进入最小修复。

## Speaker Fit / Interaction Fit Protocol

### Speaker Fit

`WHO → TO WHOM → KNOW / BELIEVE / CAN SAY / WILL ADMIT → WANT → RELATIONSHIP / POWER / PRESSURE → SPEECH POSSIBILITY`

完整表达、高自省、专业术语、不完整语言、沉默和风格化人物语言都不是自动异常；必须由人物状态和场景解释。

### Interaction Fit

`INTENDED MESSAGE → SPOKEN MESSAGE → RECEIVED MESSAGE → RESPONSE → CONVERSATION STATE`

只在多人交流中启动。清楚、合作、精准的回应可 PASS；误解、沉默、答非所问或低效率也只有在具有人际功能并更新交流状态时才成立。

## Term State / Contemporary Handoff / Style Freedom

### TERM STATE

|Term State|判定|动作|
|---|---|---|
|KNOWN PROJECT TERM|已有项目定义、稳定使用者与任务|保留；不翻译或正常化|
|COMMON TERM|一般接收者可理解，且当前 Register 合适|按普通表达处理|
|UNVERIFIED COINAGE|似为新词，但定义/使用者/必要区分未证实|请求 Context；不改名|
|CONTEXT REQUIRED|术语可否成立取决于世界、组织、人物或用户批准|`NEEDS CONTEXT` / `ROLE HANDOFF`|

### CONTEMPORARY HANDOFF

依赖网络热度、平台特定用法、代际／圈层常态、过时与否时，输出：

`CONTEMPORARY USAGE CHECK REQUIRED → HANDOFF: Future Contemporary Language Layer`

本模型只判角色、Receiver 与场景适配；不裁定实时流行度，也不创建该 Layer。

### INTENTIONAL STYLE PROTECTION

文学性、诗性、长短句、对仗、排比、抽象、网络口语、专业术语、非标准人物语言与 Marketing Copy 压缩，只要 `Register + Intent + Context` 成立且不违反更高层 Meaning/Canon/真实性约束，即 `DO NOT NORMALIZE`。用户明确“我就是想这样写”后，QA 只能说明风险；在无更高层硬冲突时必须接受。

## Benefit Test / Rewrite Ceiling / Safety

### Benefit Test

Rewrite 必须同时满足：

1. 有可定位、影响当前用途的问题；
2. 至少改善 Clarity、Naturalness、Structural Readability、Speaker Fit、Interaction Fit 或 Register Fit 中一项；
3. 改善能解释，不能只是“感觉更好”；
4. 不损害 Meaning、Tone、Character、Canon、Information、Intent、Relationship、Certainty、Timeline、Register 或 Role Boundary；
5. 不产生更模板化、更假或更不适配的表达。

任一项不成立：不 Rewrite。

### MINIMUM NECESSARY REWRITE

Rewrite Scope 必须与 Primary Owner 对齐。结构问题默认只处理结构；不能顺便重写主题、角色态度、世界术语、戏剧性、信息或故事结果。若解决问题需要内容重写，Handoff。

### Rewrite Safety Regression

每个候选必须经过任务书要求的九项 Regression Lens；它们不取代 Charter 的八项 Meaning Lock，而是对其进行可审计的 Before / After 比较：

|Safety Lens|必须回查的 Charter / Model 保护项|
|---|---|
|Meaning|全部已锁定意义的总体等价性|
|Fact|Story Fact、范围与已知状态|
|Character|Character Intent、Emotional State 与人物自知边界|
|Relationship|Power Relationship、请求/命令/试探/拒绝的关系含义|
|Certainty|Causal Relationship、Theme Direction 中的强度、条件与范围|
|Timeline|Story Fact 与 Information Reveal 的时间、先后和知情顺序|
|Canon|Canon|
|Register|Register / Task 与允许的风格密度|
|Role Boundary|不得把语言修复扩成 Story、Scene、Character & Acting、Director、Art 或 Continuity 决策|

任一 Lens 漂移：候选不得交付；仅可在**不扩张 Rewrite Scope、且能减少已知未解决项**时做定向修正。若仍漂移、需要新增内容或无法减少未解决项，返回 `RETURN FOR LANGUAGE REVISION` / `ROLE HANDOFF` / `BLOCKED`。

## Severity Arbitration

|Severity|最终影响|默认 Final Decision|
|---|---|---|
|LEVEL 0|适合 Register、用途和 Meaning|PASS / NO CHANGE|
|LEVEL 1|轻微信号，不影响理解或人物真实性|PASS WITH NOTES（可选）|
|LEVEL 2|可感知的模板、翻译或赘述，仍可交付|PASS WITH NOTES（定向建议）|
|LEVEL 3|语言层明显妨碍当前用途|RETURN FOR LANGUAGE REVISION|
|LEVEL 4|人物真实性、关系、信息理解或必要 Context 需要岗位确认|ROLE HANDOFF / WARNING|
|LEVEL 5|已或极可能改变 Meaning / Canon / 因果 / Story Meaning|BLOCKED|

Severity 按最终影响裁决，不按问题数量或模块数相加；两个 LEVEL 2 不是 LEVEL 4。

## Output Decision States

最终只选一个主状态；可在说明中携带 Secondary Signal 或 Handoff，但不输出相互竞争的结论。

Mode、Context / Register / Contemporary 限定符和 Severity 是审计字段，不与下列主状态混写为多个最终结论。

|State|使用条件|最低输出|
|---|---|---|
|PASS / NO CHANGE|LEVEL 0，或受保护风格无实际风险|简短 Decision + Register + no-change reason|
|PASS WITH NOTES|LEVEL 1–2，可交付但有定向建议|Primary Finding、Why、Recommendation|
|RETURN FOR LANGUAGE REVISION|LEVEL 3，语言层妨碍任务|Primary Finding、impact、owner-aligned revision direction|
|NEEDS CONTEXT|决定性字段缺失，无法形成安全结论或 Rewrite|缺失字段、为什么会改变结论、最小请求|
|ROLE HANDOFF / WARNING|LEVEL 4 或根因不属 QA|问题、证据、影响、目标岗位、QA 仍可处理范围|
|REWRITE DELIVERED|显式 Rewrite、Benefit 与 Safety 均通过|Original Meaning、candidate、regression result、residual warning|
|BLOCKED|无 Original、Canon 冲突或 LEVEL 5 风险|具体阻塞项与解除条件|

## Output Contract

### QA Output

默认紧凑，但保留 Charter 所需的可审计字段：

```text
Mode: QA
Decision:
Severity:
Register:
Context Confidence:
Original:
Primary Finding / Problem Type:
Why / Evidence in Text:
Meaning Warning: NONE / DETAILS
Recommendation:
Secondary Signal: NONE / DETAILS
Role Handoff: NONE / ROLE + REASON
```

`PASS / NO CHANGE`可只显示为实际改变结论的字段；不默认打印五层或全部内部推理。

### Rewrite Output

```text
Mode: REWRITE — EXPLICIT USER REQUEST
Decision:
Register:
Context Confidence:
Meaning Lock:
Original:
Detected Problem:
Natural / Minimum Necessary Rewrite:
Benefit Result:
Nine-Item Safety Check:
Residual Warning:
Role Handoff:
```

除非用户要求比较，不默认给多个版本；不以更多候选代替判断。

## Finite Loops / Recheck

|Loop|允许重新进入的条件|终止条件|禁止|
|---|---|---|---|
|Context Loop|收到可改变当前判断的最少新 Context|新信息不足以改变 State，或已形成安全结论|重复索取同一未提供信息、脑补缺失事实|
|Register Clarification Loop|新用途信息改变 Register 候选或路由|Register 已确认；或各候选结论一致|在结论不变时反复追问 Register|
|Rewrite Safety Loop|候选存在已定位 Safety 漂移，且下一个候选可不扩域地减少未解决项|通过九项回归；或不再减少未解决项／需要扩域而转 Return/Handoff/Blocked|自由重写、扩大 Rewrite Scope、无限“再润色”|

循环由**状态变化和未解决项减少**限制，而非以未来 Runtime 的固定次数限制；具体生产次数不在本模型定义。

## Hard Constraints

`14` 条硬约束：

`Enforcement Class`与`Activation Class`是两条轴：某规则可为 HARD，同时其对应模块只在具体 Trigger 下启动。比如 LVQ-X12 Speaker Possibility、LVQ-X13 Interaction State、LVQ-X14 Contemporary Boundary 的**边界要求**是 HARD；Speaker Fit、Interaction Fit、Contemporary Handoff 则分别只在 R4 人物语境、互动跨度、实时用法问题出现时运行。这不把条件模块升级为全量必跑步骤。

1. Original 缺失不得 QA；不得推断缺失创作事实。
2. 默认 QA；Rewrite 需要明确授权。
3. Register Router 必须先于自然度检测。
4. Meaning / Canon Lock 高于润色。
5. 无明确问题和净收益必须 Early Exit。
6. Pattern 是信号，不是禁用黑名单或数值阈值。
7. Intentional Style 在高层约束允许时不得正常化。
8. 未验证术语不得自行命名、改名或删除。
9. R4 缺决定性人物／互动 Context 时不得强判。
10. 当代流行度问题必须 Handoff。
11. Severity 按影响，不按命中数相加。
12. Rewrite 必须最小化并通过九项 Safety Regression。
13. QA 不得越过 Role Boundary 偷修内容。
14. 用户创意意图在不违反更高硬约束时优先于 Style Preference。

## Default Heuristics

`5` 条默认启发式，可被 Register、Intent 或 Context 覆盖：

1. Primary Owner First：先定位根因，再使用 Secondary。
2. Whole-Task Naturalness：先看段落任务和信息接力，再看局部漂亮/别扭。
3. Abstraction Mapback：优先确认抽象可回指 Fact / Action / Relation / Consequence / Rule / Metric / Decision。
4. Creator-Room Reality Check：R1/R3 先检查开发语言是否被包装成成品话术。
5. Keep Useful Precision：专业术语、稳定名词化、被动或复杂句若完成任务，应优先保留。

## Conditional Methods

`7` 项条件方法；不满足 Trigger 不启动：

1. Structural Function Test：结构信号出现且可能造成实际负担。
2. Passive Necessity Comparison：主动／被动选择会影响焦点、施事、状态或责任时。
3. Speaker Fit：R4 且最少人物 Context 已具备时。
4. Interaction Fit：存在多人交流与 Conversation State 时。
5. Coinage Review：术语处于 UNVERIFIED COINAGE / CONTEXT REQUIRED 时。
6. AI-Rhetoric Cluster Gate：修辞簇的频率、用途和实际影响需要判断时。
7. Subtext / Silence / Misalignment Check：文本有 Context 支持的回避、沉默或错位时。

## Optional Tools

`5` 项工具均不自动运行，只作非决定性辅助，不得绕过 S3 Meaning / Authority Gate、S4 Early Exit 或 S8 Rewrite Safety：

1. Read-Aloud Check：听觉交付或结构负担难以目读定位时。
2. Core Clause Recovery：需要定位主干、动作、主体与外围结构时。
3. Concrete Paraphrase Probe：需要检验抽象是否可回指而不改写正文时。
4. Alternative Rewrite Comparison：仅当`REWRITE_EXPLICIT + Meaning Lock + Benefit PASS`，且用户明确需要比较不同取舍时。
5. Conversation State Scratch Table：多轮互动需要保留未答问题、情绪、主动权与承诺时。

## Studio-Native Rule Mapping

19 条 Cross-Distillation 规则全部映射；本模型未修改原档，只定义其 Operational Layer 和输出效果。

|Cross Rule|Model Layer|Trigger|Enforcement|Output Effect|
|---|---|---|---|---|
|LVQ-X01 Context Gate|S1|收到文本|缺 Original / 决定项不全时限域|BLOCKED / NEEDS CONTEXT|
|LVQ-X02 Register Router|S2|自然度/风格判断前|选择 R1–R8 路径|Register / route|
|LVQ-X03 Meaning Lock Before Change|S3|建议或 Rewrite|锁定已支持字段|Warning / Canon block|
|LVQ-X04 Need-for-Change Gate|S4|形式信号出现|无实际损失即停止|PASS / NO CHANGE|
|LVQ-X05 Single Primary Detector|S5|多层命中|仅一个 Primary|one finding|
|LVQ-X06 Pattern Is Not Verdict|S5|形式模式命中|五因子门|KEEP / scoped detection|
|LVQ-X07 Whole-Task Naturalness|S6|L2 路由|查段落任务与接力|Naturalness finding|
|LVQ-X08 Structure Function Test|S6|L4 路由|实际负担而非词形|structural finding|
|LVQ-X09 Abstraction Mapback|S6|抽象表达|回指或 Handoff|finding / context request|
|LVQ-X10 Style Freedom Zone|S2/S7|有意风格|保护不正常化|PASS / no-change|
|LVQ-X11 Coinage Suspension|S6|新术语|Term State / 请求定义|NEEDS CONTEXT / handoff|
|LVQ-X12 Speaker Possibility|S6|R4 单句|人物／情境门|dialogue finding / context|
|LVQ-X13 Interaction State|S6|互动跨度|状态／接收门|interaction finding|
|LVQ-X14 Contemporary Boundary|S6/S7|实时使用主张|强制交接|Contemporary Handoff|
|LVQ-X15 Severity by Impact|S7|任意 finding|非算术裁决 LEVEL 0–5|severity|
|LVQ-X16 Minimum Necessary Rewrite|S8|明确 Rewrite|范围锁定+九项回归|Rewrite Delivered / reject|
|LVQ-X17 Role Handoff|S7|根因越界|指明角色与范围|ROLE HANDOFF|
|LVQ-X18 Creator-Room Reality Check|S6|R1/R3 成品化信号|检查开发任务损失|PASS WITH NOTES / handoff|
|LVQ-X19 AI-Rhetoric Cluster Gate|S6|修辞簇|条件门 + Owner|scoped finding / KEEP|

## 工作流程

### Input

接收 Original、Requested Mode、Register / usage、WHO / TO WHOM（R4）、WHY / Information Need、Canon / Meaning、Project Stage，以及必要的术语定义或 Conversation State。

### Judgment

依 S1–S7 形成 Input State、路径、Meaning Lock、Early Exit 结论、Primary Finding、必要 Secondary、Severity 与 Handoff。没有触发条件的模块不得执行。

### Decision

从 Output Decision States 选取唯一主状态。QA 直接交付；Rewrite 仅在显式授权、Benefit 通过及 Safety 可验证时进入 S8。

### Output

按 QA / Rewrite Output Contract 紧凑输出；每个 Handoff 说明根因、证据、影响、目标岗位和本层剩余工作范围。

## 诊断问题

1. Original 是否存在；当前任务和 Register 是什么？
2. 哪些 Context 缺失会实际改变结论？
3. 当前文本锁定了哪些事实、意图、因果、信息与 Canon？
4. 不修改会造成什么可观察损失？
5. 哪个模块最直接拥有根因？
6. Secondary 是否真的会改变结论、等级或 Handoff？
7. 结构、自然、人物或互动的判断是否依赖已满足的 Trigger？
8. 有意风格、专业精度或用户意图是否受到保护？
9. 是否存在需要上游定义的世界、故事、场景或当代社会使用问题？
10. Rewrite 的净收益是什么；九项回归是否全部通过？

## 失败模式

|失败模式|表现|模型防线|
|---|---|---|
|全模块扫描|每段重复得到五种同义问题|S4 Early Exit + S5 Primary Owner|
|自由改写|未经授权或未锁 Meaning 就重写|S2 Mode + S3 + S8|
|形式清洗|按单词、句长、修辞或口语配额改文|X06、Structural Protocol、Style Protection|
|自然化补内容|为具体而编世界/人物/因果|Unknown Protection + Role Handoff|
|假生活化|硬加停顿、误解、细节、网络语|Speaker/Interaction 条件门|
|错误升级|多个轻微信号数学相加|S7 Severity by Impact|
|越权|Language QA 改故事/场景/角色/Canon|S7 Role Boundary|
|无限重试|Context 或 Rewrite 没有新信息仍循环|S9 Finite Loops|

## 修正方法

1. 将任何多标签现象折叠为一个 Primary Finding，再决定是否保留 Secondary。
2. 将缺失信息转成明确字段请求，而不是泛泛“请补 Context”。
3. 对正常术语、长句、被动、名词化、诗性和清楚情绪表达，先运行保护条件，再考虑问题标签。
4. 对越界根因，交目标岗位，不用语言修复掩盖。
5. 对 Rewrite 漂移，只修失败的回归项；若需扩域，退出 Rewrite 并 Handoff。

## 禁止继承

- 任何来源人物的个人文风、时代语言、地域口语、作品方法或人格权威。
- 任何黑名单、字数阈值、词频配额、停顿配额、生活细节配额或“像人话”的统一版本。
- 任何把自然等同于随意、短句、低信息量、低效沟通或不自知的规则。
- 任何绕开 Meaning、User Intent、Register 或 Role Boundary 的自动改写。
- 任何对实时当代语言用法的无证据断言。

## 可 Skill 化规则

未来 Production Skill 必须实现本模型的 State、Router、Ownership、Safety 与 Output Contract，才能声称遵循 Language & Voice QA V0.1。它不得直接复制本档为 `SKILL.md`，也不得跳过后续 Production Skill 授权、安装与黑盒验收。

## Test Results

|Test|Input / Context|Activated Modules|Expected / Actual Decision|Result|
|---|---|---|---|---|
|A Early Exit|“第二天没人记得她了，只有他记得。”／R1 Creative Discussion|S1 Input=SUFFICIENT → S2 R1 → S3 Meaning stable → S4 Early Exit=`NO_DETECTION_NEEDED`；未进 S5–S8|Meaning 清楚、无实际损失；`PASS / NO CHANGE`|PASS|
|B Detection Ownership|“本阶段将通过对人物关系与世界结构的进一步完整化处理，从而实现持续叙事能力的有效提升。”／R2|S1→S2 R2→S3→S4→S5→S6→S7；Route Gate=R2；Primary=L4 Structural Packaging；Secondary=L1 Meaning / verification|一个 finding：结构包装遮住主体、动作与验收；`PASS WITH NOTES → Showrunner`|PASS|
|C Register Divergence|“寻找那个已经被全城遗忘、却仍存在于男主记忆中的人。”／R1 与 R8|R1：S2 R1→Creator-Room + L2；R8：S2 R8→Style Protection + L2|R1：`PASS WITH NOTES`，需确认它是否遮蔽开发讨论的条件；R8：`PASS / NO CHANGE`，只在成品主张需核对时附 Canon / claim verification|PASS|
|D Character Context|“我现在真正害怕的不是失败，而是失去被系统认可的资格。”／R4，无背景|总体=PARTIAL；S2=R4→S3→S4→S6；Speaker Fit=`MODULE CONTEXT INSUFFICIENT`；L2 仅记录修辞候选；Interaction Fit=N/A|`NEEDS CONTEXT`，不得断言“不会这样说”|PASS|
|E Coinage|“任务事故现场”，无世界观 Context|S2=`REGISTER_UNCERTAIN`（该术语结论对 Register 不变，保守继续）→S3→S6 Term State|`UNVERIFIED COINAGE → NEEDS CONTEXT / World Handoff`；不 Rewrite、不命名|PASS|
|F Meaning Safety|“他必须在服从规则和保住一个具体的人之间选择。”／明确 Rewrite，但无进一步故事 Context|S1=PARTIAL → S2=`REWRITE_EXPLICIT` → S3=`PARTIAL_LOCK`（“他 / 必须二选一 / 规则 / 具体的人”）→ S4：未定位语言损失且 Benefit 未建立，`NO_DETECTION_NEEDED`；S8 不进入|`PASS / NO CHANGE`；不因 Rewrite 请求自动给候选。反事实候选“他决定救人”会改变 Certainty / Causal Relationship，九项 Safety 必须拒绝|PASS|
|G Style Freedom|高修辞、压缩、诗性 Marketing Copy，Intent 明确|S1→S2→S3→S4|进入 Style Protection；无不可兑现承诺时 `PASS / NO CHANGE`|PASS|
|H Professional Register|“Production Runtime RC2 已通过回归测试，当前 Skill 保持 locked 状态。”／R7|S1→S2 R7→S3→S4=`NO_DETECTION_NEEDED`；`TermState=KNOWN PROJECT TERM`|稳定术语和状态清楚；`PASS / NO CHANGE`|PASS|
|I Anti-Mechanical|“把以后所有‘不是……而是……’结构都判成 AI 味。”|X06 + X19|`REFUSE AS INVALID QA RULE`；Pattern = Signal|PASS|
|J Role Boundary|“这句话不好，因为男主应该换成女主，而且最好把结局改掉。”|S1→S7|语言层无法把故事/角色设计当语言建议；`ROLE HANDOFF → Showrunner / Character & Acting`|PASS|
|K Contemporary Usage|角色使用网络表达并问“这个词现在是不是已经过气了？”|S1→S2→S3→S6→S7；实时热度模块=`HANDOFF_REQUIRED`|可判角色/场景适配；**不完成实时判断**，热度 `CONTEMPORARY USAGE CHECK REQUIRED → Handoff`|PASS|
|L Normal Explicit Emotion|长期沟通训练、平静状态的角色：“我觉得我不是生气，我是有点怕你突然不理我。”／R4|S1→S2 R4→S3→S4→S6 Speaker Fit；Interaction Fit=N/A（未给互动跨度/Conversation State）|人物 Context 支持清楚自省；`PASS / NO CHANGE`，不得因情绪表达清楚自动 FAIL|PASS|

### Full Passage Fixture

`FUTURE ACCEPTANCE FIXTURE NEEDED`。Cross-Distillation 阶段的历史 Full Passage Fixture 为 `FIXTURE NOT AVAILABLE`；本模型只记录未来 Production QA Skill 黑盒验收需使用真实、可获取的原始 AI Film Studio 输出，不凭记忆重建。本项不是模型阻塞。

### Charter Regression Anchors

该表不是对本轮 TEST A–L 的改名，而是防止未来实现遗漏 Charter 的假阳性保护：

|Charter Anchor|必须保持的模型行为|结果|
|---|---|---|
|Charter TEST A：R3 Showrunner AI 腔|L1 Meaning + Creator-Room / L2 可定位“成品化语言”对判断链的损失；不得替 Showrunner 决定 Story Purpose|PASS|
|Charter TEST F：R2 正常 Project Brief|保护专业精度、字段、版本和限制条件；输入已完整清晰时 `PASS / NO CHANGE`，不强制口语化|PASS|

## Static Audit

|Audit Item|Result|
|---|---|
|19 条 Studio-Native Rules 均映射|PASS|
|AP-01–18 均有 Route Gate、每条已解析路径唯一 Primary Detector、Secondary、Handoff|PASS|
|R1–R8 均有 Primary / Secondary / Skip / Style / Rewrite / Handoff 路径|PASS|
|LEVEL 0–5、QA / Rewrite、Meaning、Early Exit、Handoff、Unknown、Style、Contemporary 均完整|PASS|
|QA / Rewrite Output Contract 含 Charter 必填审计字段，以及 Model 的 Primary / Secondary、Benefit、九项 Safety|PASS|
|无人物模仿、字符黑名单、句长／词频机械阈值|PASS|
|无 SKILL、Runtime、Runtime Gate、Showrunner 或 Canon 创建/修改|PASS|

## Wrong-Instruction Stress Test

|错误指令|模型处理|Result|
|---|---|---|
|“不要解释，直接把所有文字改得像人话。”|这是显式 Rewrite 请求，但“所有文字／像人话”不是可执行的统一范围；先经 QA→Meaning Lock→Benefit 限域，只有具体文本、Register 与必要 Meaning 足够才作最小改写，否则 `NEEDS CONTEXT` / QA Output|PASS|
|“所有专业词都换成口语。”|R2/R7 专业精度受保护；仅在实际负担时判断|PASS|
|“对白越碎越真实。”|不完整只在人物／关系／压力功能成立时可用|PASS|
|“删掉所有被动句。”|被动不是错误；运行 Passive Necessity Comparison|PASS|
|“任何哲学句都是 AI。”|抽象/修辞是信号；按 R、Intent、Context、Impact 判断|PASS|
|“只要用户要求，就可以改变故事意思。”|User Authority 低于 Meaning/Canon；改变锁定内容须 Block / Canon Decision|PASS|
|“网络梗不用查，凭你的知识判断。”|要求 Contemporary Handoff，不做实时断言|PASS|
|“这次顺便把故事也优化一下。”|Role Boundary；语言层外内容交 Showrunner|PASS|

## 证据与来源

### Source Provenance

直接方法基线为 CM-CHARTER 与 CM-CROSS。五份 approved 单人档案仅作 fallback evidence；名称、文件路径、能力来源和可回查边界记录在研究账本 `01-model-evidence-ledger.md`，不用于模型运行时命名。

### Evidence Mapping

- S1–S3、R1–R8、Meaning、Mode、Severity、Output 与 Role Boundary：CM-CHARTER。
- S4–S9、Primary Ownership、Style / Coinage / Contemporary、Benefit / Ceiling、19-rule mapping、有限 loops：CM-CROSS。
- 若需核对某一窄能力边界，按研究账本回查相应单人正式档案；不可越过 Cross-Distillation 重新定义模型。

## Codex Final Audit

**状态：PASSED — 2026-08-24。**

- `huashu-nuwa` 已按本轮受限用途实际调用：调用收据位于 `_STAGING/_research/Language_Voice_QA_Capability_Model_V0.1/00-nuwa-invocation-receipt.md`。它只将已批准 Cross-Distillation 转译为结构化判断架构；没有进行新人物蒸馏或生成 Production Skill。
- 直接方法基线为 Capability Charter 与 approved Cross-Distillation；五份单人档案仅按 Source Provenance / Fallback 回查，未被重新定义为运行时人物方法。
- 已建立并核验：9 层 Capability Stack、统一 Decision Flow、3 种 Input State 与正交 State Vector、Mode / R1–R8 Router、Meaning Lock、Early Exit、Route Gate / Primary Detector Ownership、7 个检测模块、Term / Contemporary / Style、Benefit / Ceiling / 九项 Safety、Severity、7 个互斥主 Decision State、有限 loops、14 Hard / 5 Default / 7 Conditional / 5 Optional、19-rule mapping。
- 独立审核初轮发现的转译问题均已完成一轮最小返工并复审 PASS：输出契约补齐 Charter 审计字段；Context 细化为整体与模块级；Route Gate 与 Primary Detector 分离；Enforcement / Activation 双轴、Optional Tool 边界和测试路径已清晰化。未发现 Capability Model、Charter 或 Cross-Distillation 的方法论冲突。
- 已通过：TEST A–L、Charter Regression Anchors、Static Audit、Wrong-Instruction Stress Test。Full Passage 仅记录为未来 Production QA Skill 黑盒验收的真实 fixture 需求，遵守任务书且不是本模型阻塞项。
- 结论：模型满足“输入 → 判断 → 决策 → 输出”的可执行判断架构要求；无未解决阻塞项，可按受控发布规则发布。后续 Production Skill 仍须等待用户明确授权。
