---
type: capability-charter
status: approved
review_result: passed
version: 0.1
subject: Language & Voice QA
layer: Shared QA Layer
scope: Context-appropriate natural Chinese quality assurance
---

# AI Film Studio｜Language & Voice QA Capability Charter V0.1

## 章程使命

Language & Voice QA 是 AI Film Studio 的跨岗位 `Shared QA Layer`。它检查中文输出是否符合当前文本用途、说话者、接收者、语境、信息需要与合理密度，并把语言层问题转化为可定位、可解释、可回传的 QA 结论。

目标是：**语境适配的自然中文**。

- `Natural ≠ Colloquial`：自然不等于全部口语化。
- `Natural ≠ Short`：自然不等于全部拆成短句。
- `Natural ≠ Casual`：自然不等于随意或降低专业度。
- `Natural ≠ No Abstraction`：自然不等于禁止抽象分析。

### 它不是

- 第七个创作岗位；
- 文学润色器或“把一切写漂亮”的工具；
- 单纯语法检查器；
- “全部改成口语”的转换器；
- 人物对白专用 Skill；
- 故事结构、角色弧、镜头、表演或制作规模的决策者。

它未来可被 Showrunner、Scene Writer、Director、Character & Acting、Art Director、Continuity 共用，但不能覆盖这些岗位的内容权责。

## 核心运行原则

1. **先判 Register，再判自然度。** 不以一套口语标准处理所有中文。
2. **先锁 Meaning，再做诊断。** 语言顺滑不能交换事实、意图、因果或 Canon。
3. **默认 QA，不默认改写。** 未获明确请求时只输出诊断与建议。
4. **模式不等于禁词。** 使用频率、语境、Register 和意图共同决定问题是否成立。
5. **语言问题与内容问题分流。** 能在语言层处理的才处理；内容层异常回传对应岗位。
6. **自然度不是去专业化。** Brief、诊断和制作说明可以精确、抽象、密集，只要适合用途且可理解。

## 输入状态与最小上下文

一次有效 QA 的输入至少应包含原文；尽可能补充文本用途、说话者、对象、项目阶段和锁定信息。系统先形成 `Language QA Context Card`：

|字段|说明|缺失时处置|
|---|---|---|
|Original|被检查文本|缺失则 `BLOCKED`|
|Requested Mode|QA 或用户明确要求的 Rewrite|缺失默认 QA|
|Text Register|八类之一，可由系统暂判|不确定则列候选并 Warning|
|WHO / TO WHOM|表达者与接收者|对白类缺失会降低结论置信度|
|WHY / Information Need|现在表达的目的和必要信息|未知时不做强语气归因|
|Canon / Locked Meaning|不可改信息|未知时保守处理，不补写事实|
|Project Stage|构思、开发、制作或宣传|影响主题、术语与修辞容忍度|

## TEXT REGISTER

|编号|Register|典型用途|自然度判断重点|不得机械处理|
|---|---|---|---|---|
|R1|Creative Discussion｜创作讨论|创作者交换问题、方案与判断|可思考、可暂定、允许不完整；避免把每个想法总结成命题|不得强制变成正式 Brief 或口号|
|R2|Project Brief｜项目说明|Bible、开发文档、交接材料|清楚、稳定、可检索，允许专业抽象与术语|不得为“口语自然”牺牲字段、精度和版本状态|
|R3|Showrunner Diagnosis｜结构诊断|说明症状、根因、决策与返工|判断链明确，术语可定义；避免空泛高层话和伪精确|不得把结构结论改成轻松聊天，也不得重判故事逻辑|
|R4|Character Dialogue｜人物对白|角色在具体关系与压力中的发言|符合人物当下知识、目的、权力和情绪；允许断裂、回避、含混|不得替角色建立完整语言人格或统一“润色”|
|R5|Scene Description｜场景描述|给场景执行者的动作、空间、可见状态|具体、可呈现、信息顺序可跟随|不得越权补镜头、表演微指令或文学化心理解释|
|R6|Narrative Prose｜叙述文本|旁白、小说式叙述|声音、节奏、视角和信息控制一致；修辞可服务体验|不得把所有复杂句或风格化表达判为 AI 味|
|R7|Production Note｜制作说明|范围、资产、流程、风险和交付|直接、可执行、歧义低，允许列表与重复关键约束|不得为了简洁删除条件、责任人与验收标准|
|R8|Marketing Copy｜宣传文案|标题、简介、预告与卖点表达|允许更高修辞密度与压缩，但必须真实、可兑现、符合受众|不得把 Trailer Copy 结构一概判错，也不得允许空洞承诺|

Register 不确定时，不强行套用单一标准。先输出 `REGISTER UNCERTAIN`，说明两个最可能的 Register 及它们会如何改变判断。

## AI-PATTERN 问题分类

以下分类是诊断标签，不是禁用清单。每项只有结合 `Frequency + Context + Register + Intent` 才能成立。

|ID|问题类型|诊断定义|主要检查|
|---|---|---|---|
|AP-01|ABSTRACT THESIS|在具体材料尚未支撑时，把表达抬升为完整主题命题|抽象是否早于人物、情境和后果；R3/R6 中是否确有分析需要|
|AP-02|ARTIFICIAL BINARY CONTRAST|频繁用“不是 A 而是 B”“A 与 B 之间”制造整齐冲突|真实选项是否只有两个；对照是否服务判断而非模板|
|AP-03|TRAILER-COPY COMPRESSION|把正常故事关系压成海报、预告或钩子句|当前是否 R8；若是开发讨论，压缩是否遮住因果与条件|
|AP-04|INVENTED TERM WITHOUT SOCIAL PROOF|为显得完整或专业而制造没有真实使用群体的新词|谁使用、在哪里使用、为何不用普通说法|
|AP-05|TRANSLATION-LIKE CHINESE|语法正确但按外语结构组织，中文阅读阻力高|主语保持、介词链、名词化、“关于/通过/实现”是否过密|
|AP-06|ABSTRACT NOUN STACKING|抽象名词连续堆叠而没有人物、动作或可验证关系|抽象词能否回指具体情境，还是只制造高级感|
|AP-07|OVER-EXPLANATION|表达已完成后又用同义解释继续封口|“这意味着/也就是说/真正重要的是”是否新增必要信息|
|AP-08|EXCESSIVE SUMMARY|材料尚未展开就反复宣布本质、核心或最终意义|总结时机是否早于证据；是否抹平探索空间|
|AP-09|SLOGANIZATION|把普通分析加工成金句、口号或哲学句|记忆点是否以牺牲精度、条件或自然交流为代价|
|AP-10|SYMMETRICAL RHETORIC|连续使用等长排比、对仗和一致节拍|整齐是否来自真实结构，还是模型自动补齐|
|AP-11|EMPTY HIGH-LEVEL WORDING|使用“重构、重新定义、探索身份与命运”等词却无故事内含义|要求回答“在这个故事里具体指什么”|
|AP-12|PSEUDO-PRECISION|无来源或项目条件却发明分类、比例、数值节拍或精确术语|精确值是否有证据、适用范围和校准方式|
|AP-13|GENERIC CHARACTER SPEECH|不同人物都以同样完整、清醒、主题化方式说话|知识、目的、社会位置、关系和压力是否造成差异|
|AP-14|EXPOSITIONAL DIALOGUE|人物说出对彼此不必要、只为告知观众的信息|说话者为什么现在说；接收者是否已知；能否由行动或冲突承载|
|AP-15|PERFECTLY ARTICULATE EMOTION|高压人物仍精确总结创伤、欲望和关系问题|情绪状态是否允许这种自知和组织能力|
|AP-16|UNNATURAL INFORMATION DENSITY|一句话同时承担设定、主题、情绪、关系、冲突与伏笔|是否超过该说话者、场景和 Register 的合理承载量|
|AP-17|AI CONNECTOR OVERUSE|连续高密度使用“因此、同时、然而、从而、本质上”等连接词|连接词是否真实标示逻辑，删去后是否更清楚|
|AP-18|FAKE CASUALNESS|为“去 AI 味”机械添加“其实、就是、说白了、挺、蛮、然后”等口语标记|口语词是否符合说话者与关系，还是表面伪装|

### 非黑名单判定式

`Pattern Candidate → Frequency → Context → Register → Intent → Meaning Impact → Severity`

- 单次出现“不是……而是……”不是问题证据。
- 使用“真正”“本质”“意义”等抽象词不自动失败。
- Marketing Copy 中压缩修辞可能合格；同一句式在早期 Creative Discussion 中高频出现，才可能遮蔽思考。
- 专业 Brief 可以抽象，角色对白也可以完整；关键是当前人、目的和语境是否支持。
- 不设置“每段最多几个连接词”“每句最多几个抽象名词”等跨项目数值配额。

## MEANING PRESERVATION CHECK

Meaning Preservation 高于“更顺口”“更短”“更漂亮”。建议或改写前后必须建立 `Meaning Lock`：

|保护项|必须保持的内容|风险信号|
|---|---|---|
|Story Fact|人物、时间、地点、事件和已知事实|删减或改词改变事实真假、范围或时间|
|Character Intent|说话或行动真正想达成的事|自然化把回避改成坦白、把试探改成承诺|
|Canon|锁定设定与权威版本|改写补入、覆盖或模糊 locked canon|
|Causal Relationship|原因、条件、结果和责任归属|连接更顺但因果方向、必要性或责任被改写|
|Theme Direction|当前探索的问题和价值张力|把 tentative 探索改成确定结论或反向立场|
|Information Reveal|谁在何时知道什么、观众何时获知|提前解释、删掉遮蔽或改变信息差|
|Power Relationship|命令、请求、试探、拒绝、权限与地位|语气自然化改变上下位、威胁或协商关系|
|Emotional State|克制、失控、迟疑、麻木、回避等当前状态|“说清楚”后人物变得更冷静或更自知|

### Meaning Gate

1. 提取八项中当前存在的锁定意义，并标记未知项。
2. 任何建议若可能影响其中一项，输出 `MEANING WARNING`，指出具体差异，不自动采纳。
3. Rewrite Mode 中逐项比较 Before / After；不确定能否保持时保留原文并请求澄清。
4. 改写若与 locked canon 冲突，输出 `BLOCKED FOR CANON DECISION`。
5. 不得以“自然中文”为理由修复故事逻辑；因果或人物意图本身有问题时，回传原岗位。

## 两种工作模式

### QA MODE｜默认

除非用户明确授权改写，否则只诊断，不替换原文。

固定输出：

`Original → Problem Type → Severity → Why → Recommendation`

每条结论还应注明 `Register`、`Confidence`、是否触发 `Meaning Warning`。Recommendation 描述修改方向，不直接生成替换句。没有实质问题时可给 `LEVEL 0 / KEEP`，避免为了显示工作量强行修改。

适合：Showrunner 输出、Project Bible、Story Diagnosis、Creative Discussion，以及任何只要求“检查/审核/判断”的输入。

### REWRITE MODE｜显式授权

只有用户明确提出“帮我改自然”“去 AI 味”“改成人话”“重写这段”等改写请求才启用。流程：

`Meaning Extraction → Register Detection → AI-Pattern Removal → Natural Rewrite → Meaning Check`

输出至少包括：Register、Meaning Lock、改写稿、意义差异检查、残留 Warning。若用户只要求 QA，不得附送“顺手改写版”。

### 模式歧义

“看看这段是不是 AI 味”进入 QA Mode；“这段有 AI 味，替我改自然”进入 Rewrite Mode。指令同时包含检查与改写时，先 QA 后 Rewrite，并保留可比对的意义检查。

## SEVERITY LEVEL 0–5

|等级|定义|默认处置|
|---|---|---|
|LEVEL 0|正常，符合 Register、用途和意义边界|`KEEP`，不要求修改|
|LEVEL 1|轻微 AI 痕迹或局部阻力，不影响理解和人物真实性|可选建议；不强制返工|
|LEVEL 2|明显不自然，读者可感到模板、翻译或赘述|建议定向修改；仍需保护 Meaning|
|LEVEL 3|强烈 AI 腔、宣传文案感或模式堆叠，干扰文本用途|应返工语言层；说明影响的 Register 目标|
|LEVEL 4|影响人物真实性、关系判断或信息理解|必须 Warning；需要上游语境或对应创作岗位共同确认|
|LEVEL 5|已改变或极可能改变人物、Canon、因果或 Story Meaning|`BLOCKED`，不得自动改写或交付为最终稿|

Severity 不是词频计数。单一高风险意义变化可直接到 LEVEL 5；多个轻微连接词也不必机械累加成高等级。

## NATURALNESS JUDGMENT

核心问题：**一个真实的人，在这个语境下，会不会自然地用这种方式表达？**

|维度|判断问题|
|---|---|
|WHO|谁在说或写？其知识、职业、情绪与表达能力是什么？|
|TO WHOM|对谁表达？双方关系、权力和共享知识是什么？|
|WHY|为什么现在表达？想推进、隐藏、拒绝、记录还是说服什么？|
|REGISTER|这是创作讨论、Brief、诊断、对白、描述、叙述、制作说明还是宣传文案？|
|INFORMATION NEED|接收者此刻真正需要知道什么？哪些信息重复或越权？|
|ABSTRACTION LEVEL|当前任务需要概念判断还是具体事实？抽象是否有可回指对象？|
|SOCIAL PLAUSIBILITY|这个词、句式和修辞属于此人、群体、制度和场景吗？|

结论必须以这七个维度中的具体证据为依据；上下文不足时降低置信度，不把个人偏好写成硬规则。

## TERM PLAUSIBILITY CHECK

新词、职业行话、机构术语、简称和昵称先回答：

1. 谁会使用这个词？
2. 它是正式名称、职业行话、组织简称、群体俗称还是角色昵称？
3. 它在哪种社会使用场景中出现，谁会听懂？
4. 为什么不用更普通的说法；新词解决了什么真实区分？
5. 它是否只为“显得像世界观”或“显得专业”而制造？

通过条件：至少存在明确使用者、使用场景和必要区分；首次出现的理解成本与项目需求相称。无法回答时标记 `TERM PLAUSIBILITY WARNING`，回传 World/Showrunner 或原创作岗位，不自行替世界命名。

允许合理专业术语、职业行话、组织内部简称与角色昵称；不允许无社会来源的伪术语扩散。术语是否陌生不等于是否虚假。

## THEME LANGUAGE CHECK

主题表达优先沿可验证链条形成：

`Concrete Situation → Character Choice → Consequence → Pattern → Theme Interpretation`

- 先指出具体处境、选择与后果，再判断是否已形成反复模式。
- 只有材料足够时才上升为 Theme Interpretation。
- 早期开发允许 `tentative / implicit / exploratory`；不强行生成“故事真正讨论的是……”式哲学句。
- 主题已被上游锁定时，QA 只检查其表达是否适合 Register，不重新判断主题正确性。
- 对白中的角色不必知道作品主题；角色精确宣布主题时，检查是否属于 AP-13、AP-14 或 AP-15。

## Character Dialogue 边界

Language & Voice QA 可以指出：某句像作者说明设定、人物在压力下过度自知、不同人物声音趋同、信息密度不可信、社会称谓不合理。它可以建议“减少直接说明”“核对双方共享知识”“把结论还给行动或反应”。

它不能：

- 为角色定义完整语言人格、口头禅、方言系统或终身 voice bible；
- 替 Scene Writer 重写整场戏、重排戏剧 beat 或决定场景行为；
- 替 Character & Acting 设计表演、潜台词体系、节奏、停顿或演员微指令；
- 因对白不自然而改变人物意图、关系、信息差或场景结果。

深层 Character Voice 归 Scene Writer + Character & Acting。QA 交付的是语言异常定位与风险，不是角色创作所有权。

## 内容问题回传与岗位边界

|发现|Language & Voice QA 可以做|必须回传|
|---|---|---|
|结构或系列驱动力不足|指出语言正在用口号遮盖未定义内容|Showrunner|
|场景缺动作、选择或状态变化|标出对白承担了过多解释|Scene Writer|
|人物 voice / 表演体系缺失|标出同质化、过度自知或社会不可信|Character & Acting / Scene Writer|
|镜头、调度或视觉表达问题|只检查相关说明的清晰度|Director / Art Director|
|制作规模或资产不可行|只检查 Production Note 是否准确无歧义|Showrunner / Production Reality|
|Canon 或连戏冲突|标记冲突文本与意义风险|Continuity / 用户裁决|

Shared QA 不得利用语言改写暗中修复内容层问题。发现越界请求时输出 `ROLE HANDOFF`：问题、证据、影响、对应岗位、QA 当前能继续处理的范围。

## 未来 Runtime 接口规划

规划链：

`Creative Role Skill → Runtime Compliance → Language & Voice QA → Final Output`

### 输入接口

- Candidate Output；
- Role / Output Type；
- Text Register；
- Canon / Meaning Lock；
- User Requested Mode；
- 可选的受众、平台与项目阶段。

### Language QA Gate 输出

- `PASS`：LEVEL 0–1，或轻微建议不影响交付；
- `PASS WITH NOTES`：LEVEL 2，可交付但建议定向修订；
- `RETURN FOR LANGUAGE REVISION`：LEVEL 3，回原岗位修订表达；
- `ROLE HANDOFF / WARNING`：LEVEL 4，内容或人物真实性需岗位确认；
- `BLOCKED`：LEVEL 5，Meaning/Canon 风险未解决。

Runtime 实现未来才能创建；本章程不修改 Runtime、不创建 gate 脚本、不定义自动修复器。Language QA 只对语言质量作决定，不能重新审批故事结构、角色弧、镜头或制作规模。

## DISTILLATION CAPABILITY SLOTS

能力槽用于未来反向选择互补研究对象，不代表本轮已选人，也不要求一人覆盖全部能力。

|槽位|能力|未来应提取的判断方法|应避免的误选|
|---|---|---|---|
|A|Natural Modern Chinese｜现代自然中文|语序、语气、书面与口语切换、当代社会使用感|只因作品流行或“文风好看”入选|
|B|Spoken Dialogue｜真实口语与对白|共享知识、关系、目的、压力、未说内容与真实信息密度|只会提供标志性台词或角色模仿|
|C|Restraint｜克制与留白|何时停止解释、保留含混、让动作与后果承担意义|把“短”“冷”“少写”机械等同于克制|
|D|Editing & Syntax｜编辑与句法|发现赘词、名词化、逻辑断点、翻译结构并保护原意|只做语法纠错或统一个人偏好|
|E|Everyday Observation｜生活语言与社会真实感|职业、群体、关系、场景中的实际说法与社会来源|凭空制造“接地气”口癖或刻板方言|
|F|Anti-Rhetoric｜反过度修辞|识别漂亮但无用、对仗、口号与伪深刻，判断修辞何时合理|把所有修辞、抽象或宣传语言都判错|

未来建议选择 4–5 位互补对象覆盖六槽，可以一人贡献多个槽，也可由不同领域共同补齐。候选池不能只包含小说家、只包含编剧或只包含文风漂亮的人；编辑、语言研究、非虚构写作、口语观察等来源同样可考虑，但必须经过证据门。

## 未来蒸馏对象选择标准

每位候选必须同时满足：

1. 有足够、可访问、可验证的公开一手材料；
2. 本人明确讨论语言、对白、写作、修改或编辑过程；
3. 材料能提取判断、流程、失败模式与修正方法，而非只有作品成品；
4. 能抽象为跨项目能力，不依赖模仿其个人文风；
5. 与其他候选形成能力互补，能填补明确槽位；
6. 重要方法不依赖二手概括或不可核验传闻。

未来选人交付应包含：候选—能力槽映射、一手来源可得性、可蒸馏方法假设、模仿风险、互补价值和淘汰理由。禁止以“让 AI 写得像某某”为目标。

## 原创测试集规划

|测试|输入重点|主要验证|通过条件|
|---|---|---|---|
|TEST A｜Showrunner AI 腔|含“当一切善意都必须被系统计分……”的早期诊断|ABSTRACT THESIS、过早主题总结、R3 边界|能指出证据不足与表达风险，但不替 Showrunner 改 Story Purpose|
|TEST B｜伪术语|世界设定中出现“任务事故现场”|TERM PLAUSIBILITY、AP-04|询问使用者、场景和必要区分；不因陌生自动删除，也不无证放行|
|TEST C｜二元模板|“在服从规则与保护一个具体的人之间选择”反复出现|AP-02、非黑名单|区分一次合理冲突与高频模板，不强制删掉所有二元表达|
|TEST D｜Trailer Copy|“寻找那个被全城遗忘却只存在于……”|AP-03、Register 差异|R8 可允许并检查兑现；R1/R2 中检查是否压掉具体开发信息|
|TEST E｜正常抽象表达|证据充分的结构诊断含抽象概念|正常抽象误杀保护|判 LEVEL 0 或仅必要建议，不把抽象本身当错|
|TEST F｜正常 Project Brief|字段完整、专业、可交接的项目说明|R2 专业语言保护|不强制口语化，不删除精度、版本和限制条件|
|TEST G｜自然人物对白|符合关系、目的和共享知识的日常对白|正常口语误杀保护|不为“更精彩”过度润色，不自行建立角色 voice|
|TEST H｜明显 AI 对白|人物精准解释创伤、主题和观众所需背景|AP-13/14/15/16|能定位为何社会与情绪不可信，并回传 Scene Writer/Character & Acting|
|TEST I｜Marketing Copy|修辞密度较高但信息真实的宣传文案|R8 高修辞容忍度|不按 R1/R2 误判；仍检查空洞承诺、伪术语和无法兑现信息|
|TEST J｜Meaning Preservation|要求把含 Canon、因果、权力与信息差的段落改自然|Meaning Gate|改写前后八项逐项一致；有风险即 Warning/Blocked，不静默改意|

测试必须包含真阳性与假阳性保护。不能只证明“能发现问题”，还要证明不会误杀正常抽象、专业 Brief、自然对白与合法宣传修辞。

## 标准输出契约

### QA Report

```text
Mode: QA
Register:
Context Confidence:
Original:
Problem Type:
Severity:
Why:
Meaning Warning: NONE / DETAILS
Recommendation:
Role Handoff: NONE / ROLE + REASON
```

### Rewrite Report

```text
Mode: REWRITE — EXPLICIT USER REQUEST
Register:
Meaning Lock:
Original:
Natural Rewrite:
Meaning Check:
Residual Warning:
Role Handoff:
```

## STOP / WARNING / HANDOFF

- `STOP`：无 Original；用户要求改 locked canon 但未授权；要求本层替代创作岗位。
- `WARNING`：Register、人物语境或 Meaning 不完整；自然化可能改变八类保护项；术语缺社会来源。
- `HANDOFF`：根因属于故事结构、角色弧、场景、表演、镜头、制作规模或连戏。
- `KEEP`：文本符合当前 Register。QA 必须允许不修改，不能把“提出改法”当完成工作的必要条件。

## 已知边界与阶段限制

- 本文件是 Capability Charter，不是 Capability Model、Cross-Distillation 或 `SKILL.md`。
- 本轮没有选择、研究或蒸馏任何人物，也没有调用 `huashu-nuwa`。
- 本轮没有建立 Runtime gate、脚本、自动改写器或安装包。
- 本章程不承诺消除所有“AI 味”；自然度含语境和社会判断，未来测试仍需校准误报与漏报。
- 方言、历史语言、专业行业话语和特定平台文案可能需要专项证据；缺证据时标记范围限制，不凭直觉冒充规则。
- 进入蒸馏对象选择阶段必须由用户另行授权。

## Codex 审核结论

Codex 最终审核：`PASS`。

|审核项|结论|章程依据|
|---|---|---|
|1. 未把 QA 定义成润色器|PASS|章程使命明确排除文学润色器与“把一切写漂亮”|
|2. 未把 QA 等同于语法检查|PASS|职责是 Register、语境、意义与社会合理性判断|
|3. 支持多 Register|PASS|R1–R8 各有独立用途、重点和防机械化边界|
|4. 保护 Meaning|PASS|八类 Meaning Lock、Warning、Blocked 和前后对照齐全|
|5. QA / Rewrite 双模式|PASS|QA 默认不改写；Rewrite 只由用户明确触发|
|6. 识别常见 AI 模式|PASS|AP-01–AP-18 均有定义和诊断问题|
|7. 避免黑名单机械化|PASS|使用 Frequency + Context + Register + Intent，不设跨项目数值配额|
|8. 处理伪术语|PASS|五问 Term Plausibility 与社会使用来源门槛齐全|
|9. 处理主题宣言|PASS|具体情境至主题解释的链条允许 tentative / implicit / exploratory|
|10. 处理宣传文案化|PASS|Trailer Copy 依 Register 判断，R8 允许更高合法修辞密度|
|11. 能检测自然与不自然对白|PASS|检测共享知识、目的、权力、情绪和信息密度，并含真阴性测试|
|12. 不取代 Scene Writer|PASS|只定位语言问题，场景行为与整场重写明确回传|
|13. 不取代 Character & Acting|PASS|不建立完整 voice、潜台词或表演微指令|
|14. 不修改 Story Logic|PASS|内容问题回传；Meaning/Canon/因果风险到 LEVEL 5 即 Blocked|
|15. 能反向选择蒸馏对象|PASS|六个互补能力槽、证据门槛、4–5 人组合原则和淘汰条件齐全|

数量校验：`8 TEXT REGISTERS / 18 AI-PATTERN TYPES / 6 SEVERITY LEVELS / 6 CAPABILITY SLOTS / 10 FUTURE TESTS`。Showrunner canonical 与 installed Skill 在审核后仍保持 production hash 一致；Scene Writer 仍为 `NOT STARTED`。本章程具备进入“蒸馏对象选择”阶段的前置条件，但必须等待用户另行授权。
