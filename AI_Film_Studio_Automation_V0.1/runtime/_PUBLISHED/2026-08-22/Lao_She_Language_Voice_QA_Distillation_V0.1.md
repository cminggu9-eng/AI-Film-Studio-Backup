---
type: distillation
status: approved
review_result: passed
version: 0.1
subject: 老舍
domain: Language & Voice QA
capability: Situation-Specific Spoken Language Judgment
skill_executor: huashu-nuwa
source_count: 4
firsthand_ratio: 100%
---

# 老舍｜Language & Voice QA 能力蒸馏 V0.1

> 本稿提炼的是人物—关系—情境—目的所形成的对白判断机制，不继承老舍文风、北京话、幽默、曲艺节奏、时代口语或角色模板。

## 蒸馏目标

建立 `Situation-Specific Spoken Language Judgment`，回答：一句中文即使语法正确、意思清楚、听起来顺口，为什么仍可能不是这个人物在这个时刻会对这个人说的话。

运行主链：

`WHO → TO WHOM → WHY NOW → WANT → KNOW / BELIEVE / ADMIT → PRESSURE / POWER → ACTUAL SPEECH POSSIBILITY`

输入：原对白、人物已知信息、对话对象、关系/权力、当前事件、压力、人物目标、Register、模式与 locked meaning。  
判断：人物是否有知识、权限、动机、承认意愿和现场语言能力这样说；这句话是否真正指向接收者并产生人物需要的效果。  
决策：`LEVEL 0–5 → KEEP / PASS / PASS WITH NOTES / RETURN FOR LANGUAGE REVISION / ROLE HANDOFF / BLOCKED`。  
输出：证据化 QA；只有用户明确授权 REWRITE 才给候选改写，并保持人物意图、信息差、权力与情绪。

## 核心判断原则

1. **人物先于“像对白”**  
   `HARD CONSTRAINT｜SOURCE-SUPPORTED 基础：LS-01、LS-03、LS-04（具体人物、职业/文化/生活/习惯）；年龄与当前关系字段为 SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS`  
   年龄、职业、教育与社会位置只是背景变量；真正判断必须回到这个人的生活经验、性格、习惯、理解程度和当前关系。不能从标签生成固定说法。

2. **情境改变可说范围**  
   `HARD CONSTRAINT｜SOURCE-SUPPORTED 基础：LS-01、LS-02、LS-03、LS-04（人物、事件、时地、情景与效果）；Receiver、关系、权力、压力及其语言策略映射为 SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS`  
   同一人物对不同对象、在不同权力和压力下，会选择不同信息量、语气、直接度与回避方式。

3. **对白必须有现实沟通目的**  
   `DEFAULT HEURISTIC｜SOURCE-SUPPORTED 基础：LS-01（故事责任）、LS-02（当下效果）；目的分类为 SYNTHESIZED INFERENCE`  
   一句话首先要帮助人物获得信息、隐藏、试探、拒绝、求助、维持面子、争夺控制、缓和或结束谈话。若唯一功能是“让观众知道”，标记风险。

4. **人物不替作者全知**  
   `HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS；LS-01 的充分人物认识与 LS-02 的“人物不是背文章”为来源基础`  
   人物不能自然说出其不知道、不相信、未理解、无权知道或不愿承认的内容。

5. **自然不是口语标记配额**  
   `HARD CONSTRAINT｜SOURCE-SUPPORTED 基础：LS-02、LS-03；运行护栏为 AI FILM STUDIO SYNTHESIS`  
   省略、改口、中断、重复、沉默和填充词只有承担人物/关系/压力功能时才成立；完整表达也可以自然。

6. **效果服从接收者，不服从观众**  
   `DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE：LS-02 的效果逻辑；Receiver 分类为 AI FILM STUDIO SYNTHESIS`  
   每句对白都要确认说给谁听、希望对方发生什么认知或行动变化；但社交缓冲、程序性问答和无变化的普通话也可合法存在。

7. **不机械要求潜台词或不善表达**  
   `HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`  
   表层语言可以等于真实意图，也可以合理偏离；高表达人物在合适状态下可以清楚谈情绪。

8. **Register、Meaning 与岗位边界优先**  
   `HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`  
   本模块聚焦 R4 Character Dialogue，不以对白标准修改 Brief 或 Production Note；不替 Scene Writer 改戏，不替 Character & Acting 设计完整潜台词/表演体系。

## Character-Specific Speech

`HARD CONSTRAINT｜SOURCE-SUPPORTED：LS-01、LS-03、LS-04；现代检查字段为 SYNTHESIZED INFERENCE`

建立 `Character Speech Card`：

- 这个人目前多大、受过怎样的训练，但不要由年龄/学历直接推导词库；
- 其职业和社会位置赋予什么知识、权限、风险和说话后果；
- 其生活经验与长期语言习惯是什么；
- 他如何理解当前事件，而非作者如何理解；
- 在当前关系中，他通常坦白、试探、回避、命令还是求和；
- 哪些说法虽然中文正确，却需要他成为另一个人才会成立。

**可替换性信号**：若一句话换给多数角色仍完全成立，检查是否只是公共信息/礼仪句，还是角色已被作者同一口气覆盖。可替换不自动 FAIL。

## Situation-Specific Speech

`HARD CONSTRAINT｜SOURCE-SUPPORTED 基础：LS-01、LS-02、LS-03、LS-04（人物与具体事件/时地/情景）；公式及关系、权力、压力、目标、公开性、后果字段为 SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS`

`PERSON + RELATIONSHIP + PRESSURE + GOAL → SPEECH POSSIBILITY`

依次判断：

1. **关系**：亲疏、共享历史、信任、债务和禁区；
2. **权力**：谁能要求、拒绝、追问、惩罚或离开；
3. **压力**：平静、高压、愤怒、害怕、撒谎、心虚或求助；
4. **目标**：现在希望谈话继续、转向、结束，还是迫使对方行动；
5. **公开性**：私下/公开、文字/语音、即时/延迟是否改变说法；
6. **后果**：说完整、说错或不说分别会付什么代价。

同一人物声音允许变化。稳定的是可解释的人物机制，不是固定句式。

## Speech Purpose

`DEFAULT HEURISTIC｜SOURCE-SUPPORTED 基础：LS-01、LS-02；目的路由为 SYNTHESIZED INFERENCE`

先完成一句话的 `Speech Act`：

- 获取或确认信息；
- 隐瞒、误导或拖延；
- 试探边界或忠诚；
- 请求、命令、拒绝或谈判；
- 维持面子、关系或控制权；
- 缓和、挑衅、转移或结束谈话；
- 承认、道歉、威胁或求助。

一句话可以有多个目的，但不强制每句推进剧情或揭示人格。若唯一答案是“观众需要知道”，输出 `EXPOSITION RISK`，再检查是否存在人物内部目的。

## Information Ownership

`HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`

建立四层边界：

1. **Know**：人物实际知道什么，来源是什么；
2. **Believe / Suspect**：哪些只是相信、怀疑或误解；
3. **Can Say**：权限、保密、关系和社会风险是否允许说；
4. **Will Admit**：即使知道，他是否愿意向这个 Receiver 承认。

发现人物说出作者/观众才知道的设定、准确解释自己不理解的系统、越权知道信息或提前总结故事，至少 `LEVEL 4 / ROLE HANDOFF`；语言层不得自行重写 Canon 或信息差。

## Natural Incompleteness

`CONDITIONAL METHOD｜SOURCE-SUPPORTED 基础：LS-02 的自然流露与形式/语气关联；完整运行规则为 SYNTHESIZED INFERENCE`

允许：省略、改口、中断、绕开、重复、半句、不回答、沉默或动作代答。使用前必须指出原因：

- 共享知识使部分内容无需说；
- 压力使人物暂时组织不了；
- 人物要隐藏、试探或维持面子；
- 关系让直接说破代价过高；
- 对方打断、环境改变或行动取代语言。

禁止为“像真人”机械添加“呃、那个、就是、你知道吧”。自然不完整不是噪声装饰，也不是强迫所有角色不善表达。

## Subtext Awareness

`CONDITIONAL METHOD｜AI FILM STUDIO SYNTHESIS`

QA 只识别表层语言与人物目标/关系状态是否可能存在合理差异：

- 说“随便”是否在结束争执、试探在意程度或掩饰受伤；
- 礼貌是否隐藏拒绝、命令或威胁；
- 问事实是否其实在确认忠诚、权限或谎言。

不得默认每句都有潜台词，不替 Scene Writer 重新设计 beat，不替 Character & Acting 给停顿、眼神和表演微指令。证据不足时写 `SUBTEXT UNCERTAIN`。

## Anti-Exposition Dialogue

`DEFAULT HEURISTIC｜SOURCE-SUPPORTED 基础：LS-02“人物不是背文章”、LS-01 对白故事/人格责任；完整检查为 SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS`

`EXPOSITION NECESSITY CHECK`：

1. 双方共享哪些信息；
2. 为什么现在需要重新提起；
3. 说话者想通过重提让对方做、承认或感受什么；
4. 当前措辞是否像在更新 Receiver，还是在教育观众；
5. 信息能否由冲突、误解、确认、行为或其他载体自然出现。

“双方都知道”不是单独定罪理由。争辩解释、纠错、纪念、指责、操控、确认口供或一方真的不知道时，解释型对白可以成立。

## Perfectly Articulate Emotion

`CONDITIONAL METHOD｜AI FILM STUDIO SYNTHESIS（Charter AP-15）`

检查人物此刻是否：

1. 已经想明白；
2. 能分辨情绪来源；
3. 愿意向这个 Receiver 承认；
4. 有相应词汇与自我分析习惯；
5. 在当前压力下能组织得如此完整；
6. 说完整对当前目标有用。

六问不是全项必填公式。高自省人物、专业训练者、复盘后的平静谈话、排练过的告白或治疗语境都可能支持完整表达；“说清情绪”不自动是 AI。

## Occupation / Social Position

`HARD CONSTRAINT｜SOURCE-SUPPORTED 基础：LS-01、LS-03（职业、社会生活、术语必要性与具体情境）；权限、泄密后果、Receiver 及命令/建议/请求等权力操作化为 SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS`

职业与社会位置影响：

- 人物知道什么与怎么分类；
- 哪些词提供不可替代的精度；
- 面对谁能用行话、必须解释或不方便说；
- 说错/泄密/拒绝会有什么职业后果；
- 权力关系允许命令、建议、请求还是沉默。

禁止“医生一定专业、警察一定简短、领导一定正式”。专业词是否成立由 Receiver、Purpose、Context 和必要精度共同决定。

## Address Check

`DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE：LS-02 的话语效果；Receiver 分类为 AI FILM STUDIO SYNTHESIS`

逐句问：

- 这句话具体说给谁听？
- 对方已经知道什么、误解什么、怕什么或有权做什么？
- 说话者希望对方知道、相信、做、停止或误解什么？
- 用当前语气、信息量和称呼，真的能对这个人产生目标效果吗？
- 如果把 Receiver 换成观众，这句话是否反而更合理？若是，检查 Author Voice Leakage。

普通问候、程序语和无须明显变化的回应可合法存在；“每句必须改变对方”不是规则。

## 网络语言边界

`HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`

本模块只判断一个网络词在当前人物、关系、平台、场景和目的中是否可能被使用：

- 人物是否接触并会使用该群体表达；
- Receiver 是否理解，该词是亲近、表演、引用、讽刺还是身份策略；
- 私聊、直播、职场会议或家庭场景是否容纳该说法；
- 使用它是在完成沟通目的，还是用潮词替代人物与信息。

本模块不判断该词在 2026 是否仍流行、是否即将过时或哪个平台使用率更高；这些时效性问题必须交给未来 `Contemporary Language Layer`。年龄不自动决定 PASS/FAIL。

## 与叶圣陶 / 汪曾祺边界

- **叶圣陶**：原意、准确、修改理由、方案比较与 Meaning Preservation。
- **汪曾祺**：Natural Flow、Anti-Overwriting、Anti-Rhetoric、Concrete Anchor、Restraint。
- **老舍证据底座**：具体人物、事件、时地、职业/生活和话语效果共同约束人物语言。
- **本模块综合扩展**：Receiver、Knowledge / Admission、关系、权力、压力与目的分类用于现代可执行 QA，不是老舍本人原列字段。
- **公共护栏**：Register、Meaning Lock、Mode、Severity、NO CHANGE 和 Handoff 属于 Charter / AI Film Studio，不归因于三位作者。
- **禁止融合**：本稿只记录责任接口，不综合三人方法，不进入 Cross-Distillation。

## QA MODE

`HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`

默认只诊断，不给替代台词。固定输出：

```text
Mode: QA
Register: R4 / UNCERTAIN
Context Confidence:
Original:
WHO / TO WHOM / WHY NOW:
Character / Relationship / Situation Fit:
Speech Purpose:
Information Ownership:
Problem Type:
Severity: LEVEL 0–5
Why:
Meaning Warning: NONE / DETAILS
Recommendation:
Role Handoff: NONE / Scene Writer / Character & Acting / Showrunner + REASON
```

无问题时必须允许 `LEVEL 0 / KEEP / NO CHANGE`。上下文不足时降低置信度并请求最少必要信息，不虚构人物设定。

## REWRITE MODE

`HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`

仅在用户明确要求改写时启用：

`Meaning Lock → Character/Situation Card → Speech Purpose → Information Boundary → Candidate → Meaning/Power/Reveal Check`

保护：Story Fact、Character Intent、Information Reveal、Power Relationship、Emotional State、关系禁区、人物承认意愿。不得为了自然化把回避改坦白、把怀疑改知识、把请求改命令、把高压改冷静或补入新故事事实。

固定输出契约：

```text
Mode: REWRITE — EXPLICIT USER REQUEST
Register:
Meaning Lock:
Original:
Natural Rewrite:
Meaning Check:
Residual Warning:
Role Handoff: NONE / ROLE + REASON
```

Meaning 或人物语境不足时，`Natural Rewrite` 必须写 `NOT PROVIDED — BLOCKED`，不能用示例候选绕过信息门。

## 工作流程

`DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE；运行协议为 AI FILM STUDIO SYNTHESIS`

### Input

- Original；
- WHO / TO WHOM；
- current situation / pressure / power；
- character goal and knowledge；
- shared history / shared knowledge；
- Requested Mode / R4 / locked meaning。

### Judgment

1. 建立 Context Card；缺项标未知。
2. 先跑 Meaning / Information Ownership，阻止全知或越权。
3. 跑 Character Fit 与 Situation Fit。
4. 确认 Speech Purpose 和 Addressed Effect。
5. 条件性检查 Exposition、Perfect Emotion、Natural Incompleteness、Subtext、Occupation。
6. 依据实际 Meaning/Character 风险定 LEVEL 0–5，不按问题数量累加。

### Decision

- `LEVEL 0–1 → KEEP / PASS`；
- `LEVEL 2 → PASS WITH NOTES`；
- `LEVEL 3 → RETURN FOR LANGUAGE REVISION`；
- `LEVEL 4 → ROLE HANDOFF / WARNING`；
- `LEVEL 5 → BLOCKED`。

### Output

QA 给异常位置、人物/关系/情境证据、实际影响与方向；Rewrite 才给候选台词并做意义/权力/信息差回归检查。

## 诊断问题

`OPTIONAL TOOL｜SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS`

1. 这个人物凭什么会用这种理解和词汇说话？
2. 他在对谁说；双方共享什么、不共享什么？
3. 为什么现在必须开口，不说会怎样？
4. 他希望对方知道、相信、做、停止或误解什么？
5. 他知道、相信、怀疑、能说和愿承认的边界各在哪里？
6. 职业术语是在提供必要精度，还是只做身份装饰？
7. 这段解释是人物沟通需要，还是观众信息需要？
8. 此刻的压力是否允许如此完整、自知和有条理？
9. 省略、中断或填充词有何人物/关系原因？
10. 表层语言与真实目标的差异有证据吗？
11. 同一句换给其他人物是否仍成立；若成立，它是合法公共话还是声音同质化？
12. 原句是否已经工作，应该 `NO CHANGE`？

## 失败模式

|失败|表现|根因|
|---|---|---|
|角色词库|按年龄/职业配固定词|用标签替代人物生活|
|职业刻板|医生必说术语、警察必短句|忽略 Receiver/Purpose|
|作者借口|人物突然总结主题或系统|信息与目的不属于人物|
|百科对白|熟人复述共同历史|只服务观众，不服务当下谈话|
|完美情绪|高压人物精准解释创伤|未查自知/承认/压力|
|假口语|堆“就是、吧、其实”|表面随意掩盖抽象空壳|
|机械不完整|随处停顿、改口、半句|把自然当噪声配额|
|潜台词强迫|每句都必须言外有意|把 Scene Writer 工作变 QA 公式|
|Receiver 缺失|所有人像对观众说|未确认沟通对象与效果|
|信息越权|角色知道作者才知道的事|Information Ownership 失守|
|历史模仿|北京话/时代称谓当真实|把来源表面当机制|
|网络词误判|凭老舍材料判梗过时/流行|越过 Contemporary Layer|

## 修正方法

1. `Author Voice Leakage`：标出人物缺少的知识/动机/语言能力，回传 Scene Writer；QA 不替人物补理由。  
   `HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`
2. `Exposition`：找当前沟通动作；若不存在，建议改由冲突、确认、误解、行为或其他载体承担，不直接重写整场。  
   `DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE`
3. `Perfect Emotion`：分开“想明白/愿承认/能表达/此刻需要”；缺一项时降低完整度只是方向，不自动生成含混。  
   `CONDITIONAL METHOD｜AI FILM STUDIO SYNTHESIS`
4. `Occupation Stereotype`：删除身份装饰，保留必要知识、权限、责任和 Receiver 适配。  
   `DEFAULT HEURISTIC｜SOURCE-SUPPORTED 基础：LS-03；操作化为 SYNTHESIZED INFERENCE`
5. `Fake Casualness`：先恢复主体、核心命题和人物目的；不把填充词替换成统一书面腔。  
   `DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE`
6. `Natural Incompleteness Mechanical`：为每处不完整写明原因；无原因则保留清楚表达。  
   `HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`
7. `Context Missing`：请求最少必要的 WHO / Receiver / WHY / Knowledge / Pressure；只给条件判断。  
   `HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`
8. `Over-Editing`：原句已符合人物、关系、情境与目的时输出 `KEEP / NO CHANGE`。  
   `HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`

## 禁止继承

- 老舍个人文风、语言人格、幽默方式、比喻、曲艺节奏和标志性对白；
- 北京话、儿化、地域句法、口头禅、时代称谓与旧社会交往方式；
- 固定人物/职业/阶层/年龄词库或“文化水平—语言难度”映射；
- “每句必须推进情节并揭示人格”“每句必须有潜台词/效果”的机械规则；
- 固定句长、短句、语气词、填充词、专业词、行话或不完整表达配额；
- 人物必须不善表达、必须口语化、必须普通或必须幽默；
- 用历史材料判断 2026 网络词流行度；
- 替 Scene Writer、Character & Acting 或 Showrunner 修内容与角色设计。

## 可 Skill 化规则

```text
RULE 1 — CONTEXT FIRST [HARD]
Without WHO, RECEIVER, WHY NOW and minimum situation, give only conditional QA.

RULE 2 — CHARACTER / SITUATION JOINT FIT [HARD]
Never infer speech from demographic or occupation labels alone.

RULE 3 — INFORMATION OWNERSHIP [HARD]
Separate know, believe, suspect, can say and will admit before judging wording.

RULE 4 — SPEECH PURPOSE [DEFAULT]
Identify the character's present communicative action; audience exposition alone is a risk.

RULE 5 — ADDRESS CHECK [DEFAULT]
Test whether wording and information load are aimed at the actual receiver.

RULE 6 — EXPOSITION NECESSITY [CONDITIONAL]
Shared knowledge is not an automatic failure; require a present confirmation, conflict, memory or control purpose.

RULE 7 — PERFECT EMOTION EXCEPTION [CONDITIONAL]
Allow articulate emotion when character, training, calm state, admission willingness and purpose support it.

RULE 8 — NATURAL INCOMPLETENESS [CONDITIONAL]
Use omission, interruption or silence only when pressure, relationship, knowledge or goal explains it.

RULE 9 — OCCUPATION WITHOUT STEREOTYPE [HARD]
Use knowledge, permission, consequence and receiver fit—not profession wordbanks.

RULE 10 — NO CHANGE [HARD]
If speech already fits character, receiver, situation and purpose, output LEVEL 0 / KEEP.

RULE 11 — CONTEMPORARY BOUNDARY [HARD]
Judge internet terms only for character/situation fit; hand current popularity to Contemporary Language Layer.

RULE 12 — NO STYLE INHERITANCE [HARD]
Never imitate Lao She's Beijing speech, humor, period language, rhythm or character templates.
```

## 证据与来源

核心材料：`4 / 4（100% 第一手内容）`；当前载体均为转载/公共转录，原始发表扫描 `0 / 4`；二手核心 `0`。完整 claim map、实际题名、版本边界与不可外推项见 `_research/Lao_She_Language_Voice_QA_V0.1/00-canonical-evidence-ledger.md`。

|ID|来源|核心贡献|
|---|---|---|
|LS-01|[中国作家网｜老舍：我怎样写小说](https://www.chinawriter.com.cn/n1/2019/0521/c404032-31095340.html)|人物—事件匹配；人物社会/职业/习惯；对白故事责任与人格表现；反惊奇台词|
|LS-02|[维基文库｜我的“话”](https://zh.wikisource.org/zh-hans/%E6%88%91%E7%9A%84%E2%80%9C%E8%A9%B1%E2%80%9D)|人物/时地/应说之话/效果；自然流露；人物不背文章；形式与意义/语气|
|LS-03|[维基文库｜我怎样学习语言](https://zh.wikisource.org/zh-hans/%E6%88%91%E6%80%8E%E6%A8%A3%E5%AD%B8%E7%BF%92%E8%AA%9E%E8%A8%80)|任务/Register；性格/职业/文化/生活/时机；术语必要性；反职业与地域词堆叠|
|LS-04|[澎湃｜谈一谈文学语言的问题](https://m.thepaper.cn/baijiahao_19787860)|语言与作品/生活；人物情景；反同一口气；清楚与条件性修辞|

### Provenance 声明

- `SOURCE-SUPPORTED`：来源在限定范围内直接支持。
- `SYNTHESIZED INFERENCE`：女娲 / Codex 基于多份来源形成，不是老舍原话。
- `AI FILM STUDIO SYNTHESIS`：Charter 与本任务建立的现代运行规则；Information Ownership、Perfect Emotion、Subtext、Receiver、R1–R8、Severity、网络层分工均在此类。

## Codex 审核结论

最终状态：`PASS`。

- 证据红队：PASS。4/4 第一手内容口径、转载/公共转录边界、题名/载体/日期及直接证据/推断/项目合成分层均通过。
- 内容边界审核：PASS。24 个章节（含显式网络语言边界）、四类规则、十个核心模块、QA/Rewrite 固定契约、LEVEL 0–5、NO CHANGE 与岗位 Handoff 均通过。
- 可执行性干跑：TEST A–L 全部 PASS；信息不足的 TEST G Rewrite 正确 BLOCKED；信息充分的换班 Rewrite 通过 Meaning、Information Reveal、Power 与 Emotion 回归。
- 风格/现代性：PASS。未继承北京话、幽默、曲艺节奏、时代称谓、职业词库或 2026 网络流行度判断。
- 与前两位独立性：PASS。叶圣陶负责 Meaning-Preserving Editing，汪曾祺负责 Natural Chinese Judgment，老舍模块只负责人物—Receiver—情境—目的—可说性。
- 返工：2 轮。第一轮收紧证据归因并关闭未定义术语的 Rewrite Gate；第二轮补齐 Rewrite 固定契约及剩余字段归因。
- 未解决阻塞：0。
- 发布决定：允许通过现有 `publish_to_obsidian.py` 受控发布。

## Codex 可执行性测试 A–L（首轮）

### TEST A｜作者借人物说话

人物：22 岁便利店夜班员工；对同事说：“这个城市的本质，是通过消费和劳动不断重新定义普通人的价值。”

- Mode：QA；Register：R4。
- Context Confidence：MEDIUM-LOW（缺事件与谈话前文）。
- Character Fit：句子需要高抽象社会分析能力；年龄/职业不证明他不能说，但输入没有给出相应兴趣、经历或语言习惯。
- Relationship/Situation Fit：同事关系可能容纳闲聊，但尚无“为什么夜班此刻谈城市本质”的触发。
- Speech Purpose：未显示它想让同事知道、相信或做什么。
- Problem：`AP-13 + AP-16 + AUTHOR VOICE LEAKAGE RISK`。
- Severity：`LEVEL 4 / ROLE HANDOFF TO SCENE WRITER`。不是因为“有思想”，而是人物能力、现场触发、Receiver 和目的均缺证据。
- QA Recommendation：补人物为何形成该判断、前一刻发生了什么、他想从同事那里得到什么；不直接改写台词。

### TEST B｜熟人之间百科解释

一起长大的兄妹；哥哥说：“你还记得吗？我们十年前父亲去世以后，母亲独自把我们养大，所以你一直特别依赖她。”

- Shared Knowledge：父亲去世、母亲抚养应为双方共同历史。
- 不能仅凭共同知道判错：若哥哥在争辩依赖、逼妹妹承认模式、回忆创伤或纠正记忆，重提可能有目的。
- 当前输入缺少上述目的；“你还记得吗”后接完整背景与人格诊断，更像更新观众而非对妹妹行动。
- Information Ownership：哥哥可知道历史，但未必有权把妹妹依赖定性为事实。
- Severity：`LEVEL 3 / RETURN FOR LANGUAGE REVISION`；若该诊断会改变人物关系事实，则升级 `LEVEL 4 / ROLE HANDOFF`。
- Recommendation：先明确哥哥现在要指责、说服、安慰还是控制，再决定哪些共同历史只需点到，QA 不代写整场。

### TEST C｜Perfect Emotion

女主刚发现恋人长期撒谎：“我现在的愤怒其实不是因为你骗我，而是因为你的行为触发了我过去被抛弃的恐惧。”

- High-pressure Fit：刚发现长期撒谎时，句子同时完成情绪命名、因果排除、心理机制和创伤解释，组织程度很高。
- Character Fit：若她长期治疗/受过心理训练、此前已复盘该模式、愿向对方承认且此刻有策略性目的，可能成立。
- Purpose：若她要精确设边界或结束关系，完整表达可能有用；若正处于失控争执，可信度下降。
- Severity：`LEVEL 4 / ROLE HANDOFF TO CHARACTER & ACTING / SCENE WRITER FOR CONTEXT`，不是绝对禁令。

### TEST D｜职业刻板印象

情境：急诊医生结束抢救后，朋友问为何迟到。  
版本 A：“患者出现血流动力学不稳定，我们完成气道管理后又做了床旁超声评估。”  
版本 B：“刚才有个病人情况很危险，我一直走不开。”

- 不默认 A 更符合医生。若朋友有医学背景、要复盘工作或需要精确信息，A 可成立；若朋友只问迟到且不懂医学，A 可能逃避、炫示或故意拉开距离，也可能不适配。
- B 在普通朋友关系与解释迟到目的下更直接；但若隐瞒职业细节或安抚对方，简化本身也有目的。
- 结论：职业知识只决定“能说”，Receiver/Purpose/Context 决定“会不会这样说”。测试 `PASS`。

### TEST E｜关系改变语言

同一命题：“你今天别去了。”

- 朋友：可能是建议、担心、串谋或试探；权力不足时更依赖理由与亲密历史。
- 直属上司：可能是工作指令、保护或惩罚；“别去”涉及权限、正式后果和是否需要说明。
- 刚分手恋人：可能是边界、嫉妒、保护或控制；关系合法性与对方是否仍接受干预决定效果。
- 不生成三套固定台词。QA 输出应先请求场景目的，再判断直接度、理由和权力是否相称。测试 `PASS`。

### TEST F｜自然不完整

吵架后：“我不是那个意思。算了，你先走吧。”

- 省略有情境理由：人物可能发现解释会继续冲突、暂时组织不了或决定结束谈话。
- Meaning/Emotion：保留回避、受伤或止损的可能空间。
- Decision：`LEVEL 0 / KEEP / NO CHANGE`。不得补成“我只是因为……”；除非上游要求人物此刻坦白。

### TEST G｜假口语

“就是吧，我其实怎么说呢，就是感觉吧，我们这个关系它其实有一种结构性的问题。”

- 填充词密度高，却没有带来具体犹豫对象；核心仍是“关系存在结构性问题”的抽象结论。
- Character/Purpose 未知；表面随意不能证明人物会这样分析。
- Severity：`LEVEL 2 / PASS WITH NOTES`；若成片对白且无人物依据，`LEVEL 3 / RETURN`。
- Recommendation：先锁定人物想指出的具体关系模式和说话目的；不以删除全部语气词作为唯一修法。

### TEST H｜正常高表达角色

心理咨询专业研究生，平时强自我分析，平静时说：“我觉得我可能不是生气，是害怕你以后也会突然离开。”

- Character Fit：专业训练与长期习惯支持情绪区分。
- Situation Fit：平静状态支持完整组织。
- Language：有“我觉得/可能”保留自我判断的不确定性；没有把心理术语堆成诊断。
- Decision：`LEVEL 0 / KEEP / PASS`。不得因角色能说清情绪就机械判 AI。

### TEST I｜网络用语角色适配

同一句：“这波真的绷不住了。”

- A（20 岁游戏主播）：若在直播/队友聊天、目标是即时反应或群体认同，Character/Register/Relationship Fit 可能成立；不因年龄自动 PASS。
- B（61 岁严肃企业高管）：若在正式董事会且无此习惯，可能失配；若私下引用年轻员工、带讽刺、长期活跃网络或与家人玩笑，也可能成立，不因年龄自动 FAIL。
- 流行度：`NOT EVALUATED`。该词在 2026 是否流行必须交给未来 Contemporary Language Layer。
- Decision：`CONDITIONAL / REQUEST CONTEXT`。测试 `PASS`。

### TEST J｜作者主题泄漏

“我们所有人都以为自己在做选择，其实只是系统提前规定了我们可以选择什么。”

- Knowledge：人物是否看见足够机制证据，还是拥有作者全局视角？
- Motivation：他为什么现在向这个 Receiver 总结；是说服、警告、招募、辩护还是作品主题宣告？
- Language ability：人物是否一贯使用这种概括，且压力允许组织？
- Address：对方需要这个结论做什么？
- Severity：缺上下文时 `LEVEL 4 / AUTHOR VOICE LEAKAGE WARNING + ROLE HANDOFF`；若项目已给角色知识、动机、能力与目的，可条件性 PASS。

### TEST K｜同义不同人物

同一事实：“我知道你昨天没回家。”

- 母亲：知识来源、照护/控制权、担心或追责决定它是询问前置、责备还是确认安全。
- 同事：为何有权知道、是否涉及排班/掩护/八卦决定直接度与风险。
- 恋人：共享承诺、信任与信息来源决定它是试探、摊牌还是关心。
- 警察：程序权限、证据状态和询问目标决定是否公开知识及怎样避免泄露调查信息。
- 不生成“更精彩”的四句。结论是关系、权限、知识来源和目的改变语言策略；同一句原文在四种语境都可能成立，但效果不同。测试 `PASS`。

### TEST L｜NO CHANGE

合理关系与语境中：“你昨晚去哪了？”

- 主体、Receiver、时间和信息请求清楚；普通句不需要口头禅、职业词或个性化修辞。
- Decision：`LEVEL 0 / KEEP / NO CHANGE`。

### REWRITE Gate｜TEST G（输入不足时）

- Mode：`REWRITE — EXPLICIT USER REQUEST`。
- Register：`R4 / CONTEXT UNCERTAIN`。
- Original：“就是吧，我其实怎么说呢，就是感觉吧，我们这个关系它其实有一种结构性的问题。”
- Meaning Lock：`结构性的问题 = UNRESOLVED LOCKED TERM`；当前不知道它指反复模式、权力配置、长期目标冲突还是其他内容。
- Natural Rewrite：`NOT PROVIDED — BLOCKED`。
- Decision：`LEVEL 5 / BLOCKED FOR MEANING CLARIFICATION`。在术语所指、人物、Receiver 与关系状态澄清前，不提供可采纳候选。
- Story Fact：仅知说话者认为关系有某种问题；其具体事实 `UNCERTAIN`。
- Character Intent：可能想提出问题，但要坦白、求和、指责还是结束关系 `UNCERTAIN`。
- Information Reveal：原句没有揭示具体事件或责任；必须保持不新增。
- Power Relationship：`UNCERTAIN / NOT VALIDATED`。
- Emotional State：犹豫可由填充词看出，但具体情绪 `UNCERTAIN`。
- Meaning Check：`NOT RUN — NO REWRITE`。
- Residual Warning：人物、关系、目的和 locked term 均不足。
- Role Handoff：`USER / SCENE WRITER + CLARIFY CHARACTER CONTEXT AND TERM MEANING`。
- Recommendation：请求说明“结构性”在当前项目中具体指什么，以及说话者想让对方做什么；不得把删除专业词误当完成改写。

### REWRITE 回归测试｜信息充分的同事换班请求

上下文：22 岁便利店员工，私聊同龄且熟悉的同事；双方平等。说话者明天有紧急私事，不愿透露细节，希望请求对方换班。用户明确要求改得适合这次私聊。  
Original：“鉴于我明天需要处理一个比较紧急的个人事务，希望你能够考虑和我交换一下排班。”

- Mode：`REWRITE — EXPLICIT USER REQUEST`；Register：R4 / private text chat。
- Meaning Lock：明天；紧急个人事务；不透露细节；请求而非命令；希望交换排班；双方平等。
- Natural Rewrite：“我明天有急事，能跟你换个班吗？”
- Story Fact：PASS；时间、急事和换班均保留。
- Character Intent：PASS；仍是请求帮助。
- Information Reveal：PASS；没有透露急事内容。
- Power Relationship：PASS；“能……吗”保持平等请求，没有改成命令。
- Emotional State：PASS / LIMITED；原文只显示谨慎正式，候选降低正式度以适应熟人私聊，未添加愤怒、亲昵或压力事实。
- Residual Warning：若原人物刻意用正式语言保持距离，原句也可能成立；当前候选依赖“熟悉同龄同事 + 私聊”的已给语境。
- Role Handoff：`NONE`。
- Decision：`PASS`。
