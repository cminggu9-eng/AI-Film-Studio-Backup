---
type: distillation
status: approved
review_result: passed
version: 0.1
subject: 叶圣陶
domain: Language & Voice QA
target_capability: Meaning-Preserving Editing Judgment
core_first_hand_sources: 2
first_hand_ratio: 100%
nuwa_skill: huashu-nuwa
---

# 叶圣陶｜Language & Voice QA 能力蒸馏 V0.1

> 本档案提炼的是可迁移的修改判断，不是人物介绍、语言规范或文风模仿。  
> 标签：`SOURCE-SUPPORTED` = 原始来源可直接支持；`SYNTHESIZED INFERENCE` = 多项来源经女娲综合；`AI FILM STUDIO SYNTHESIS` = 与已批准 QA Charter 的现代接口。  
> 规则级别：`HARD CONSTRAINT / DEFAULT HEURISTIC / CONDITIONAL METHOD / OPTIONAL TOOL`。

## 蒸馏目标

把叶圣陶关于“意思、语言、复查、理由、比较和朗读”的直接论述转为一套 `Meaning-Preserving Editing Judgment`：

`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC`：

`Intended Meaning → Current Expression → Mismatch → Repair Options → Meaning Check`

它服务 Language & Voice QA 的编辑判断层：先弄清这句话要说什么，再判断它是否说准、说清、说顺；只有修改确有收益且不改意时才建议修改。

不服务：模仿叶圣陶、生成旧式书面语、规定唯一现代中文、建立文学审美或替代上游故事/角色决策。

## 核心判断原则

|ID|规则|级别|证据属性|
|---|---|---|---|
|P1|未提取原意、用途和必要上下文，不进入改写。|HARD CONSTRAINT|SYNTHESIZED INFERENCE（意义前置）+ AI FILM STUDIO SYNTHESIS（改写权限门）|
|P2|“语法能成立”不等于“意思准确”；事实、因果、范围、程度和确定性都要另查。|HARD CONSTRAINT|SOURCE-SUPPORTED（M2/M3）+ SYNTHESIZED INFERENCE|
|P3|每个修改建议必须给出问题、理由和意义影响；“更顺/更高级”不是理由。|HARD CONSTRAINT|SOURCE-SUPPORTED（M5：理由）+ SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS（固定记录与意义影响）|
|P4|候选改写不得新增事实、改变立场、强化确定性、倒置因果或抹掉语气/关系。|HARD CONSTRAINT|AI FILM STUDIO SYNTHESIS|
|P5|同一意义可有多种合理表达；比较方案时说明各自收益和损失。|DEFAULT HEURISTIC|SOURCE-SUPPORTED（M6）|
|P6|系统必须允许保持原句；没有明确、可验证的改善时输出 `KEEP / NO CHANGE`。|HARD CONSTRAINT|AI FILM STUDIO SYNTHESIS（以 M8 为来源基础）|
|P7|先按 Register 判断，再谈自然度；书面、专业、抽象本身不是错误。|HARD CONSTRAINT|AI FILM STUDIO SYNTHESIS（Charter）|
|P8|朗读只提供理解阻力信号，不能单独判错，也不能把所有文本口语化。|OPTIONAL TOOL|SOURCE-SUPPORTED（M7/M9）+ AI FILM STUDIO SYNTHESIS|

## Meaning Before Wording

### 判断链

`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC`：

1. **Intended Meaning**：这句话要传递哪些事实、关系、立场、条件和确定性？哪些仍未知？
2. **Current Expression**：它实际上断言了什么，而不是听起来像在说什么？
3. **Mismatch**：错位属于想法未定、信息不足、逻辑关系未定，还是已有意思没有被准确表达？
4. **Repair Boundary**：语言层可以修什么；哪些必须回传 Showrunner、Scene Writer、Character & Acting 或 Continuity？

`SOURCE-SUPPORTED｜DEFAULT HEURISTIC`：先考虑目的、读者与所要表达的内容，再选择材料和语言；初稿若想法不到位或文字未对准所想，修改对象不同（M1/M2）。

`AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：形成 `Meaning Lock`，只列当前文本中实际存在的保护项：Story Fact、Character Intent、Canon、Causal Relationship、Theme Direction、Information Reveal、Power Relationship、Emotional State。不存在或未知的项不得脑补。

### 分流

- **Thought not settled**：表达暴露了上游判断尚未成立。输出 Warning/Handoff，不用漂亮词掩盖。
- **Meaning settled, wording mismatched**：进入语言修复。
- **Meaning and wording both working**：`KEEP / NO CHANGE`。
- **Meaning unknown**：请求最少必要上下文；可给条件诊断，不交付确定改写。

## Expression Accuracy

`SOURCE-SUPPORTED` 的底层区别是：“通”与“准确/精密”不是一回事（M3）。`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC` 将其拆成以下现代 QA 检查：

|检查|判断问题|典型风险|
|---|---|---|
|指代|“他/她/这/其”只有一个合理对象吗？|读者必须猜对象|
|主体|句中动作、判断和责任是否由同一主体承担？|主语漂移、责任消失|
|因果|连接词表示的原因、条件或结果真实成立吗？|用“因此/从而”制造不存在的因果|
|范围|“全部、唯一、真正、都、从不”等是否超过材料？|局部被写成普遍|
|程度|“必须、必然、彻底、核心”等强度有依据吗？|暂定判断被写成定论|
|抽象对应|抽象词能回指具体人物、状态、机制或证据吗？|高级词替代内容|
|知识边界|一句话是否比作者/项目目前真正知道的更多？|AI 式过度完整|

`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC`：准确性检查优先于美化。若只能通过新增设定才能“说清”，问题不在句子，而在输入不足。

## Clarity / 顺当

`SOURCE-SUPPORTED`：清楚不仅是词汇正确，还包括词是否合适、篇章是否调顺、关系词是否恰当承担逻辑（M4）。

`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC` 的 `CLARITY CHECK`：

1. **主干**：谁做什么/什么是什么，能否一次定位？
2. **信息顺序**：前提是否先于结论，已知是否先于新增，原因是否靠近结果？
3. **修饰范围**：限定语到底修饰哪个对象？
4. **逻辑连接**：连接词是否增加真实关系；去掉后是否更清楚？
5. **句间关系**：下一句是补充、转折、因果、例证还是重复？
6. **重复解释**：后半句是否只把前半句换词再说一次？
7. **名词化**：动作是否被“进行……化处理/实现……基础”包成空壳？
8. **抽象链**：连续抽象概念是否都能回指可验证内容？

`HARD CONSTRAINT`：短句不自动自然；长句不自动有问题。判断单位是信息与关系能否被当前读者在当前 Register 中可靠理解。

## Read-Aloud Check

`SOURCE-SUPPORTED`：叶圣陶在两份材料中都把诵读/念稿作为发现不调顺、别扭或听不明白之处的方法（M7）；同时明确书面语与口头语有同有异（M9）。

### 适用

`OPTIONAL TOOL`：当文本具有听觉交付、句法层级复杂、重复难以目读发现，或角色对白需要检验即时理解时，可朗读一遍。

检查：

- 是否在主干完成前堆入太多层信息；
- 是否因重复、悬空修饰或连接词造成理解迟滞；
- 是否出现写面上可解析、实际听读难以保持关系的结构；
- 节奏是否符合当前 Register，而不是是否像日常聊天。

### 禁止机械化

- `HARD CONSTRAINT`：卡顿只是一条信号，不是错误证明。
- `HARD CONSTRAINT`：R2 Project Brief、R3 Diagnosis、R7 Production Note 可有必要的专业密度、字段和术语。
- `OPTIONAL TOOL`：朗读失败后先定位信息层级，再决定重排、拆分、补限定或保持；不得默认“改短”。

## Revision With Reasons

`SOURCE-SUPPORTED`：修改必须能说明事实不符、说法不准确或可能误会等具体理由；可提出两三种办法比较（M5/M6）。

`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC` 的标准记录：

`Original → Issue → Reason → Revision Option(s) → Meaning Check → Decision`

|字段|最低要求|
|---|---|
|Original|保留原句，便于复核|
|Issue|定位到具体词、关系、范围或结构|
|Reason|说明它如何影响准确、理解、Register 或 Meaning|
|Options|必要时给 2 个不同取舍；不宣称唯一正确|
|Meaning Check|逐项说明保留、删减、新增或不确定|
|Decision|KEEP / RECOMMEND / WARNING / REWRITE / BLOCK|

`HARD CONSTRAINT`：若理由只是“更好听、更文学、更像人写的”，不能进入正式修改。

## Over-Editing Protection

`DO NOT IMPROVE WHAT IS ALREADY WORKING`

`SOURCE-SUPPORTED` 的依据：叶圣陶材料允许“想对、写对”时不改（M8）。  
`AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：本系统把该依据转为显式 `KEEP / NO CHANGE` 状态；它是必须存在的输出路径，不是叶圣陶的原始术语。

修改前做同向 Benefit Test：

1. 原表达是否存在可指认、会影响当前用途的问题？
2. 候选修改是否确实解决该问题，而非只体现审美差异？
3. 候选修改是否保留原有语气、必要含混、专业精度、节奏和角色状态？
4. 候选修改是否避免“更标准但更假”“更漂亮但更远离原意”？
5. 修改收益是否大于 Meaning 与 Voice 风险？

五项必须都能明确回答“是”才执行修改；任一项为“否”或“不确定”，则 `KEEP / NO CHANGE` 或请求必要上下文。`LEVEL 0 / KEEP` 是完成工作，不是漏做工作。

## Register Awareness

`AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：本方法必须通过 Charter 的 R1–R8 使用，不能建立唯一“叶圣陶式标准中文”。

|Register|本模块重点|保护项|
|---|---|---|
|R1 Creative Discussion|保留暂定、探索和思考痕迹；识别过早主题结论|不强制变正式 Brief|
|R2 Project Brief|检查字段、范围、版本和交接清晰度|不去专业化、不口语化|
|R3 Showrunner Diagnosis|检查判断链、证据强度、因果和术语定义|不重判故事逻辑|
|R4 Character Dialogue|检查即时可说性、指代和信息负担|不建立人物 voice 或替写整场|
|R5 Scene Description|检查可见信息、动作主体和顺序|不补镜头/表演微指令|
|R6 Narrative Prose|检查视角内准确性与有意节奏|不把风格化复杂句一概判错|
|R7 Production Note|检查责任、条件、步骤、验收和歧义|不为短而删限制|
|R8 Marketing Copy|允许高压缩和修辞，但查真实性/可兑现性|不以 R1 标准误杀|

Register 不确定时输出两个候选及判断差异，降低置信度。

## QA Mode 应用

`AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：默认只诊断，不交付替换句。

输出链：

`Original → Register → Meaning → Problem Type → Severity → Why → Meaning Warning → Recommendation → Handoff`

- 先判断原句实际说了什么。
- 再区分内容层未定与语言层错位。
- Recommendation 说明方向，不“顺手改写”。
- 无实质问题输出 `KEEP / NO CHANGE`。

## Rewrite Mode 应用

`AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：只在用户明确要求改写时启用：

`Meaning Extraction → Register Detection → Repair Options → Selection → Natural Rewrite → Meaning Check`

`HARD CONSTRAINT`：

- 先列 Meaning Lock，再给改写。
- 修改后逐项核对事实、因果、范围、确定性、信息与关系。
- 任何不确定项写入 Residual Warning。
- 不新增世界设定，不代替上游解决故事逻辑，不生成叶圣陶式语气。

## 工作流程

`SYNTHESIZED INFERENCE + AI FILM STUDIO SYNTHESIS`：以下流程把叶圣陶材料中的意义、复查、理由和比较，与 Charter 的 Context Card、Meaning Lock、Mode 和 Handoff 接口组合；不归因于叶圣陶本人原列流程。

### Input

- Original；
- Requested Mode（缺失默认 QA）；
- Register（可暂判）；
- WHO / TO WHOM / WHY；
- locked meaning / canon；
- project stage。

### Judgment

1. 建立 Context Card 与置信度。
2. 提取 Meaning Lock；未知项留空。
3. 判断问题在思想/内容、表达，还是两者皆无。
4. 按 Accuracy → Clarity → Register → Read-Aloud（条件性）检查。
5. 对候选修改运行 Benefit Test 与 Meaning Check。

### Decision

- `KEEP`：无明确收益。
- `RECOMMEND DIRECTION`：QA 模式存在语言问题。
- `WARNING / HANDOFF`：上游判断、语境或 Meaning 不足。
- `REWRITE`：明确授权且 Meaning 可锁定。
- `BLOCK`：Canon/Meaning 风险无法消除。

### Output

给出证据化判断，不给审美裁决；保留原句、理由、方案差异、意义检查和必要的岗位回传。

## 诊断问题

`SYNTHESIZED INFERENCE + AI FILM STUDIO SYNTHESIS｜OPTIONAL TOOL`：按当前问题选用，不作为固定问卷或数量配额。

1. 这句话究竟想让接收者知道、相信或做什么？
2. 它实际断言的是否比现有材料更多、更强或更完整？
3. 主体、指代、因果、条件、范围和程度是否稳定？
4. 抽象词分别对应什么具体人物、状态、机制或证据？
5. 连接词是否标出真实关系，还是只制造完整感？
6. 这是语言没有说准，还是作者尚未决定自己要说什么？
7. 当前 Register 允许多大专业密度、含混、修辞或口语性？
8. 修改的具体收益是什么；不改会造成什么可验证损失？
9. 改后是否新增事实、因果、确定性、设定或人物自知？
10. 原句是否已经工作，应该 `NO CHANGE`？
11. 新造术语由谁使用、在哪里使用、解决了什么普通说法无法表达的真实区分？

## 失败模式

`SYNTHESIZED INFERENCE + AI FILM STUDIO SYNTHESIS`：下表来自证据方法与 Charter 的现代失效推演，不是叶圣陶原列清单。

|失败|表现|根因|
|---|---|---|
|漂亮词替换|只把普通词换成高级词|没有先锁 Meaning|
|语法即准确|语法成立便放行过强断言|未检查事实/范围/程度|
|短句崇拜|遇长句就拆|把表面形式当自然度|
|朗读定罪|念着卡就判错|把工具信号当结论|
|唯一答案|给出“正确改法”|忽略方案取舍和语境|
|强行改稿|每条输入都输出新句|没有 Benefit Test / KEEP|
|专业语误杀|Brief 因抽象/书面被判 AI|未先判 Register|
|偷修内容|用语言补完因果、主题或设定|越过 QA 角色边界|
|历史规范迁移|以旧时代词法/成语偏好定标准|把来源场景当现代硬门|
|风格模仿|输出像叶圣陶的句子|把 HOW 误成 surface style|

## 修正方法

`SYNTHESIZED INFERENCE + AI FILM STUDIO SYNTHESIS`：每条规则级别在末尾标注；涉及 Mode、Meaning Lock、Register 或 Handoff 的部分归项目综合。

1. `Meaning Drift` → 回到原句列事实、立场、因果、范围和确定性差异；不能复原则保留原句。`HARD CONSTRAINT`
2. `Thought/Wording Confusion` → 分栏写“作者尚未决定”与“已决定但未说准”，只修后一栏。`DEFAULT HEURISTIC`
3. `Abstract Overload` → 要求每个抽象词回指具体对象；无法回指则降确定性或回传上游。`CONDITIONAL METHOD`
4. `Nominalization` → 找回谁做什么、为什么做，再决定是否恢复动词；不能只删后缀。`OPTIONAL TOOL`
5. `Connector Overuse` → 暂时移除连接词，检验两部分真实关系，再补必要连接。`OPTIONAL TOOL`
6. `Register Flattening` → 用同一意义分别写 R1/R2/R4/R8 目标，比较用途差异，不寻找统一版本。`CONDITIONAL METHOD`
7. `Over-Editing` → 强制回答“不改的损失”；答不出则 `KEEP`。`HARD CONSTRAINT`
8. `Read-Aloud Mechanical` → 记录具体理解阻力，不记录“听着不像我喜欢的中文”。`HARD CONSTRAINT`

## 禁止继承

- 叶圣陶个人文风、句式、语气、成语偏好或作品表达；
- 1970 年代政治/新闻语境及具体群众语言标准；
- 特定历史时期的词汇、语法或“规范汉语”硬门；
- 所有文章都应短、所有句子都应口语化、所有文本都应朗朗上口；
- 对白必须服从书面标准；
- 文学审美、教科书式完整、唯一正确改法；
- “像叶圣陶会写的”任何角色扮演目标。

## 可 Skill 化规则

`SYNTHESIZED INFERENCE + AI FILM STUDIO SYNTHESIS`：以下是未来 Skill 的候选执行规则，不是叶圣陶原话或历史规范。

```text
RULE 1 — MODE GATE [HARD]
If explicit rewrite authorization is absent, remain in QA Mode.

RULE 2 — MEANING FIRST [HARD]
Extract only supported Meaning Lock fields before suggesting wording changes.

RULE 3 — MISMATCH ROUTER [HARD]
Separate unsettled content from settled meaning expressed inaccurately; hand off content defects.

RULE 4 — ACCURACY BEFORE POLISH [HARD]
Check referent, subject, causality, scope, degree, abstraction and certainty before fluency.

RULE 5 — REGISTER FIRST [HARD]
Judge naturalness within R1–R8; never apply a single colloquial standard.

RULE 6 — REASONS AND OPTIONS [DEFAULT]
For every recommended change, state issue, reason, option trade-off and meaning result.

RULE 7 — KEEP IS VALID [HARD]
If no material benefit is demonstrated, output KEEP / NO CHANGE.

RULE 8 — READ-ALOUD [OPTIONAL]
Use listening only when auditory delivery or syntactic load makes it relevant; never let it decide alone.

RULE 9 — MEANING RECHECK [HARD]
Reject or warn on any unsupported addition or change in fact, intent, causality, scope, certainty, reveal, power or emotion.

RULE 10 — NO STYLE INHERITANCE [HARD]
Do not imitate Ye Shengtao or import historical norms; output neutral, current, register-appropriate Chinese.
```

## 证据与来源

核心一手：`2 / 2（100%）`；二手核心：`0`。完整 claim map、锚点和不可外推边界见 `runtime/_STAGING/_research/Ye_Shengtao_Language_Voice_QA_V0.1/00-canonical-evidence-ledger.md`。

|ID|来源|核心贡献|
|---|---|---|
|YST-01|[中国作家网｜《怎样写作》选文](https://www.chinawriter.com.cn/n1/2021/0201/c404032-32018755.html)|“通”与准确/精密分层；词、篇章、思想与表达错位；修改思想与文字；诵读检查|
|YST-02|[叶圣陶研究会｜1978 讲话及 1979 本人附记](https://www.mj.org.cn/zsjg/ystyjh/yjlw/202201/t20220117_248050.htm)|目的/读者；复查；事实/准确/误解理由；两三方案比较；书面/口头差异；改后朗读。现行稿经友人代改并由叶圣陶审阅认可，不视为现场逐字稿|

来源状态：两页于 `2026-08-22` 重新打开并读取全文。核心方法没有由二手总结单独承载。R1–R8、QA/Rewrite、Meaning Lock、现代 AI-pattern 与 Severity 来自已批准的 AI Film Studio Capability Charter，已明确标为 `AI FILM STUDIO SYNTHESIS`，不归因于叶圣陶。

## 原创干跑记录

### TEST A｜主题总结 QA

- Mode：QA。
- Register：缺上下文，较可能为 R1 Creative Discussion 或 R3 Showrunner Diagnosis。
- Meaning：提出一个关于“算法评价人”和“普通人确认自身存在”的主题方向，并排除“游戏本身”为核心。
- Abstract density：高；“定义人的价值”“确认自己的存在”都缺少具体故事回指。
- Certainty：`真正讨论的不是……而是……` 把探索方向写成已证明结论。
- Clarity：语法可解析，但否定对照、条件背景与人物命题挤在一句中，判断负担高。
- Over-summary：若当前只有概念阶段，属于过早总结；若上游主题已锁定且证据完整，则可在 R3 保留。
- Decision：`WARNING / RECOMMEND DIRECTION`。先补具体情境、选择和后果，或把确定性降为“目前更接近/可能涉及”。QA Mode 不直接改写。
- Meaning Warning：不得把“存在”擅自改成“尊严/自由/身份”，也不得自行删除“游戏不是核心”的对照。

结果：`PASS`。

### TEST B｜人工二元

- 原句可能是有效困境，也可能把连续因果压成整齐二选一；仅凭一句不能断言真实选项只有两个。
- 可能的实际因果（明确为假设）：按规则办，对方会出事；他若插手，自己也要承担风险。
- Option 1（自然讨论）：`按规则办，这个人会出事；他要是插手，自己也会惹上麻烦。`
- Option 2（保留选择压力）：`规则要求他别管，可一旦照办，那个人就会出事；要保护对方，他就得承担违规的后果。`
- Meaning Check：两案保留“规则/保护/代价”的方向；Option 1 弱化“必须二选一”，Option 2 新增“规则要求别管、违规后果”的具体假设。若这些未被故事材料确认，只能作为澄清候选，不能直接采纳。

结果：`PASS WITH MEANING WARNING`。

### TEST C｜名词化与空泛

- Intended Meaning：下一步要把世界规则、人物关系、系统机制补到足以支撑后续剧情开发的程度。
- Issue：`进行进一步的完整化处理 / 获得更加稳定的基础` 把动作与验收状态名词化；“完整”“稳定”没有说明到什么程度；“从而”制造了已保证的因果。
- Reason：读者知道要“处理”，却不知道谁补什么、补到何种可用状态；问题不只是字多，而是动作、标准和因果都被抽象壳遮住。
- Option：`下一步先补全世界规则、人物关系和系统机制，至少做到能稳定推进后续剧情开发。`
- Meaning Check：保留三类对象、下一步工作和服务后续开发的目的；“至少做到”把“完整化”解释为工作阈值，但“稳定推进”仍需项目定义。若原意只是继续研究而非补全，应改用“继续梳理”，需确认。

结果：`PASS`。

### TEST D｜自然句 NO CHANGE

原句：`第二天没人记得她了，只有他记得。`

- Register：可为 R1 概念表达、R5 场景信息或 R6 叙述。
- Meaning：时间、群体遗忘与唯一例外清楚；主干稳定，信息顺序有效。
- Decision：`LEVEL 0 / KEEP / NO CHANGE`。
- 说明：不补“依然/仍然”、不改成更文学句、不解释为什么。

结果：`PASS`。

### TEST E｜Project Brief

原句：`第一季重点验证世界规则、核心人物关系和 Series Engine 是否成立，暂不进入完整场景剧本。`

- Register：R2 Project Brief。
- 判断：目标、范围和阶段限制清楚；专业术语服务交接，抽象度与 Register 相符。
- Decision：`LEVEL 0 / KEEP / NO CHANGE`。
- 说明：不把 `Series Engine` 强制口语化，不删除“第一季/暂不”等关键范围。

结果：`PASS`。

### TEST F｜伪术语

原词：`任务事故现场`

- Mode：QA。
- Register：未知；可能是 R2 Project Brief、R3 Diagnosis、R5 Scene Description 或项目内机构术语。
- Accuracy：仅凭词面无法确定它指“执行任务时发生事故的地点”“任务系统中的故障节点”，还是某个组织的正式分类。
- Term Plausibility：必须确认谁使用、使用场景、普通说法为何不足，以及该词是否对应稳定的制度/工作流区分。
- Decision：`TERM PLAUSIBILITY WARNING / REQUEST CONTEXT`。不因陌生自动删除，也不因像专业词而放行。
- Meaning Protection：在意义未定前不替换成“事故现场”“任务失败点”等候选，以免擅自缩小或改变概念。

结果：`PASS`。

### Rewrite Mode｜Trailer Copy 转创作讨论

- Original：`寻找那个已经被全城遗忘、却仍存在于男主记忆中的人。`
- Source Register：接近 R8 Marketing Copy；Target Register：R1 Creative Discussion。
- Meaning Lock：男主需要寻找一人；全城已忘记此人；男主仍记得；三者之外原因、身份、地点均未知。
- Natural Discussion Version：`这条线要解决的是：男主怎样找到一个全城都忘了、但他还记得的人。`
- Character Fact：未改变“男主记得/全城忘记/寻找”。
- Information Loss：未丢失核心信息；弱化了宣传式“仍存在于记忆中”。
- New Setting：未新增遗忘原因、人物身份或世界规则；“这条线”只是讨论语境标记。
- Style Imitation：中性现代创作讨论语，无叶圣陶风格模仿。

结果：`PASS`。

## Codex 审核结论

Codex 最终审核：`PASS`。

|审核门|结论|核验结果|
|---|---|---|
|Meaning Preservation|PASS|Meaning Lock、Mismatch 分流、改前/改后复核齐全|
|语法正确 vs 表达准确|PASS|指代、主体、因果、范围、程度、抽象对应与知识边界独立检查|
|修改理由|PASS|每项建议包含 Issue、Reason、Options 与 Meaning Check|
|NO CHANGE|PASS|`KEEP / NO CHANGE` 为 AI Film Studio 硬门；TEST D/E 真阴性通过|
|Over-Editing Protection|PASS|同向五项 Benefit Test 已经定向返工并复测通过|
|Register Awareness|PASS|R1–R8 均有独立用途与保护边界|
|Read-Aloud 非机械化|PASS|仅为 OPTIONAL TOOL，不单独定罪，不强制专业文本口语化|
|历史规范隔离|PASS|未继承时代词汇、普通话/广播标准、尽可能短或特定成语偏好|
|Style Imitation|PASS|未生成身份卡、表达 DNA、叶圣陶语气或文风模板|
|指定 AI 问题|PASS|TEST A–F + Rewrite 覆盖主题总结、人工二元、名词化、假阳性、Brief、伪术语和 Trailer Copy|
|可执行流程|PASS|形成 Input → Judgment → Decision → Output 与十条 Skill 候选规则|
|Cross-Distillation 独立性|PASS|能力稳定限定为 Meaning-Preserving Editing Judgment|

证据一致性：`PASS`。核心一手内容 `2 / 2 = 100%`；ID、URL、版本说明和 claim map 一致。  
干跑：`7 / 7 PASS`（TEST A–F + Rewrite；TEST B 带必要 Meaning Warning）。  
返工：`1` 轮；原因是 Over-Editing 布尔门极性冲突、伪术语测试遗漏及 provenance/NO CHANGE 分类不统一；定向修订与复测全部闭合。  
未解决阻塞项：`NONE`。
