---
type: distillation
status: approved
review_result: passed
version: 0.1
subject: 余光中
domain: Language & Voice QA
capability: Translation-Like Chinese Diagnosis
skill_executor: huashu-nuwa
source_count: 5
firsthand_ratio: 100%
---

# 余光中｜Language & Voice QA 能力蒸馏 V0.1

> 本稿只提炼“翻译式中文结构诊断”，不继承余光中文风、诗性、文言/成语偏好、地区规范、散文节奏、文化立场或语言纯化人格。  
> `SOURCE-SUPPORTED` = 公开一手材料可直接支持；`SYNTHESIZED INFERENCE` = huashu-nuwa / Codex 跨来源归纳；`AI FILM STUDIO SYNTHESIS` = Charter 与 2026 生产环境的自有规则。  
> 规则级别：`HARD CONSTRAINT / DEFAULT HEURISTIC / CONDITIONAL METHOD / OPTIONAL TOOL`。

## 蒸馏目标

建立 `Translation-Like Chinese Diagnosis`：一句话即使字词为中文、语法可解析、意思大致可懂，仍可检查其句法与信息组织是否让主干迟到、动作失焦、主体隐没、逻辑被过度标记或抽象包装加重。

`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC`：

`Context & Register → Meaning Lock → Core Clause Recovery → Structure Function → Actual Burden → Alternative Comparison → Decision`

本模块不查“血统”，只查当前效果。核心原则：`Foreign Influence ≠ Error`。英文词、外来概念、现代术语、被动、名词化、介词或连接词都不能单独构成错误。

## 核心判断原则

|ID|判断原则|规则级别|证据属性|
|---|---|---|---|
|P1|先判 Register、用途、Meaning 与目标受众，再判结构；缺少 Original 则停止。|HARD CONSTRAINT|AI FILM STUDIO SYNTHESIS|
|P2|外来影响有成功与失败之分；来源不能单独决定质量。|HARD CONSTRAINT|SOURCE-SUPPORTED：YGZ-01、YGZ-04、YGZ-05-PAPER；现代执行门为 AI FILM STUDIO SYNTHESIS|
|P3|先恢复核心主句、参与者、动作与逻辑关系，再处理外围词形。|DEFAULT HEURISTIC|SOURCE-SUPPORTED 基础：YGZ-01、YGZ-05-PAPER；流程为 SYNTHESIZED INFERENCE|
|P4|只有歧义、主干迟到、责任不清、信息释放失衡或无必要认知负担实际成立时，才建议改。|HARD CONSTRAINT|AI FILM STUDIO SYNTHESIS|
|P5|专业术语、英文项目名、法律/技术/QA 的名词化与显式逻辑可以承担必要功能。|HARD CONSTRAINT|AI FILM STUDIO SYNTHESIS|
|P6|被动只进入必要性比较；结果焦点、施事隐藏、受事状态或责任安排成立时可以保留。|CONDITIONAL METHOD|SOURCE-SUPPORTED 比较基础：YGZ-01；完整门为 AI FILM STUDIO SYNTHESIS|
|P7|长短不是质量标准；长句可以清楚，短句也可以空泛。|HARD CONSTRAINT|SOURCE-SUPPORTED 基础：YGZ-03、YGZ-05-PAPER；反机械护栏为 SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS|
|P8|禁止字符、词语、句长、连接词或名词化配额；命中只能触发结构检查。|HARD CONSTRAINT|AI FILM STUDIO SYNTHESIS|
|P9|无法稳定判断 2026 当前用法时标 `CONTEMPORARY USAGE UNKNOWN`，不擅自定罪。|HARD CONSTRAINT|AI FILM STUDIO SYNTHESIS|
|P10|原文在当前 Register 中已经工作时，输出 `LEVEL 0 / KEEP / NO CHANGE`。|HARD CONSTRAINT|AI FILM STUDIO SYNTHESIS|
|P11|本模块不修 Story、Canon、主题、人物 voice 或整体修辞；越界项只 Handoff。|HARD CONSTRAINT|AI FILM STUDIO SYNTHESIS|
|P12|即使源语理解无误，仍可单独复审目标语中文如何组织意义。|DEFAULT HEURISTIC|SOURCE-SUPPORTED 基础：YGZ-06；方法化为 SYNTHESIZED INFERENCE|

## Nominalization Check

`SOURCE-SUPPORTED`：YGZ-01 与 YGZ-04 直接支持“泛化动词 + 抽象名词”可能拆散动作；YGZ-05/PAPER 直接支持把抽象名词按上下文展开为动作、状态或短句。  
`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC`：合并两类证据形成以下 Nominalization Check：

`ACTION EXISTS? → WHO DOES IT? → CAN A VERB CARRY IT DIRECTLY? → DOES NOMINALIZATION SERVE A PURPOSE?`

判断：

1. 抽象名词是否代表稳定、需要反复引用的概念、属性、程序或验收项？
2. 句中是否还能看出谁执行什么、作用于什么？
3. 恢复动词会增加清晰度，还是会损失法律/技术/学术精度？
4. 名词化是否只是把普通动作包装成高层“机制/路径/维度/提升”？

`HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`：法律条款、技术接口、QA 指标、固定项目术语可合理名词化；看到“进行/实现/完成/形成”不得自动删除。

## Preposition Chain

`SOURCE-SUPPORTED`：YGZ-01 与 YGZ-05-PAPER 直接展示了外围介词、关系连接和附属结构可能遮住主句，以及先识别主句骨架再重组的做法。

`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC` 的 `CORE CLAUSE RECOVERY`：

1. 暂时括起“基于/通过/对于/在……层面/从而”等外围结构。
2. 写出最低骨架：`谁 / 什么 → 做什么 / 是什么 → 作用对象 / 结果`。
3. 逐项放回必要的原因、条件、范围、手段和限制。
4. 检查每层介词是否承担独立关系；若只是重复同一层级，标记负担。
5. 比较原结构与重组结构的 Meaning、责任、范围和 Register；不是以删词数量决定优劣。

`HARD CONSTRAINT`：介词链不是字符命中。专业说明可能需要多层限定，只要主干可定位、附着关系无歧义且层级服务精度即可 PASS。

## Weak / Empty Verb

`SOURCE-SUPPORTED`：YGZ-01 直接讨论泛化动词与抽象名词如何稀释动作，YGZ-04 直接指出动作被“进行”等词承接后名词化。

`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC`：

- 先问动词是否告诉读者真实发生了什么。
- 若“进行/实现/开展/实施/完成/形成/产生/提供/具有”只承接另一个动作名词，尝试恢复更具体的动词。
- 若该动词标记程序状态、完成边界、结果存在、授权或固定搭配，则保留。
- 若没有足够上下文确定具体动作，QA 只能指出空壳，不得替项目发明动作。

示例边界：“完成验收”“实施隔离”“提供接口”“具有权限”都可能完全正常；问题不是词，而是它是否提供当前需要的动作/状态信息。

## Passive Necessity

`SOURCE-SUPPORTED`：YGZ-01 提供主动、显式被动与无施事状态句的比较，并显示部分被动可改为更自然的主动或状态表达。  
`AI FILM STUDIO SYNTHESIS｜CONDITIONAL METHOD` 的 `PASSIVE NECESSITY CHECK`：

1. 当前信息重点是受事结果，还是施事行动？
2. 施事未知、不重要、需隐藏或已由上下文确定吗？
3. 被动是否准确表达遭受、权限、责任或状态变化？
4. 改成主动会更清楚，还是会错误移动焦点、责任或信息时机？
5. 当前 Register 是否常用该被动结构？

被动必要性不是“必须证明非用不可”。若原句自然、焦点明确且无 Meaning 风险，直接 `KEEP`。

## Abstract Structural Packaging

`SOURCE-SUPPORTED`：YGZ-01 与 YGZ-05 显示，抽象名词可能只增加堂皇外观，或令动作/状态难以被读者和说话者直接处理。  
`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC`：

对“人物关系层面的核心驱动力 / 持续叙事维度 / 价值建构机制 / 情绪表达路径”逐项追问：

- 它是否指向稳定、可定义、需要复用的概念？
- 它能否回指人物、动作、状态、规则、指标或决策？
- 名词之间是什么关系，而非只是并列堆叠？
- 去掉包装后是否暴露输入本身尚未决定？

若概念合法但首次出现未定义，问题可为术语可解释性；若概念本身属于故事或生产设计，回传对应岗位。这里不接管汪曾祺的完整 Anti-Overwriting，只记录 `OVERLAP CANDIDATE`。

## Connector Load

`SOURCE-SUPPORTED`：YGZ-01 与 YGZ-05-PAPER 说明，部分并列、因果、介词和关系连接可以由词序、语义或上下文承担，不需逐面复制。  
`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC` 的 `EXPLICIT LOGIC NECESSITY CHECK`：

1. 标出每个“因此/然而/从而/进而/同时/此外/基于此/在此基础上”声称的关系。
2. 验证该因果、转折、并列或递进是否真实成立。
3. 暂时移除连接词；若关系仍清楚，检查它是否只是 AI 路标。
4. 若删除会模糊责任、条件、时序或验收逻辑，则保留或换成更准确的连接。
5. 评估累积效果，不设每段数量配额。

Showrunner Analysis、Project Brief 与 Production Note 可需要显式逻辑；“报告感”不是单独错误证据。

## Subject Stability

`SOURCE-SUPPORTED 基础`：YGZ-01 支持具体主体被抽象结构或长修饰压后；YGZ-05-PAPER 支持先恢复主客关系、处理代词指向。  
`SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS｜DEFAULT HEURISTIC`：

- 确认每个动作、判断和责任的主体。
- 检查“该角色/该项目/这一系统/这一机制”反复出现是否只是在维持外语式表面主语。
- 再检查省略主语后是否造成指代、责任或多人行动混淆。
- 可用省略、复现、换序或分句，但没有一种方案是默认正确。

目标不是少主语，而是主体、责任与信息重心稳定。

## Chinese Information Order

`SOURCE-SUPPORTED`：YGZ-01 和 YGZ-05-PAPER 直接支持前饰/后饰比较、中心名词与动作迟到、识别主句骨架和必要时拆解嵌套。  
`SYNTHESIZED INFERENCE｜DEFAULT HEURISTIC` 的 `INFORMATION RELEASE CHECK`：

1. 读者在何处第一次知道主体/中心对象？
2. 在何处知道动作或核心判断？
3. 原因、条件、范围和例外是否在主干前堆叠到必须暂存？
4. 能否先给中心，再分层补充，同时保持逻辑与 Register？
5. 长前置修饰是否确有必要，例如法律限定、术语定义或消歧？

不设“定语超过 X 字”阈值。判断单位是信息释放、附着关系与读者负担。

## Anti-Purism

`AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：QA 不承担“净化中文”。

- 西化 ≠ 坏中文；Foreign Influence ≠ Error。
- 被动、“的”、代词、介词、连接词、名词化、抽象词都不能自动 FAIL。
- 不建立删除清单、词频配额、字数阈值或历史纯度评分。
- 外来词和专业混合语言只检查当前受众是否理解、是否承担精确任务、是否妨碍句法与信息结构。
- 修正目标是更清楚、准确、自然、可执行，不是更古、更短或更像余光中。

任何词形命中都必须继续经过：

`Candidate → Frequency → Context → Register → Intent → Function → Actual Burden → Meaning Impact → Severity`

Frequency 用于区分偶发合法表达与累积模式，不是必须达到某个数量才可成立；单次结构若已造成明确 Meaning Impact，仍可直接进入相应 Severity。

## Modernity Guardrail

风险：`VERY HIGH`。  
`AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：

|类别|处置|
|---|---|
|A 历史上生硬、且在当前 Register 仍增加实际负担|可进入结构诊断；仍需给出具体 Why|
|B 经过长期使用已成为现代普通话常态|按当前用途判断，不能因来源于外语而改|
|C 专业领域必要术语或稳定搭配|保护精度、责任与交接；除非实际造成歧义|
|D 地区差异|按目标受众与项目规范判断，不设台湾/香港/大陆唯一标准|

当本轮稳定证据不能回答表达在 2026 是否普遍自然时，输出 `CONTEMPORARY USAGE UNKNOWN`；可说明当前项目 Register 内的局部判断，但不得冒充全社会用法结论。未来 Handoff 给 Contemporary Language Layer，本轮不启动该层。

## 与前三位能力边界

|模块|主责任|本稿边界|
|---|---|---|
|叶圣陶|Meaning Preservation、准确、修改理由、权限|本模块调用公共 Meaning Gate，但不重建其完整编辑方法|
|汪曾祺|Natural Flow、Anti-Overwriting、Anti-Rhetoric、Concrete Anchor|抽象包装与修辞问题只标 `OVERLAP CANDIDATE`；本稿只处理结构如何制造负担|
|老舍|人物—Receiver—情境—目的—可说性|人物是否会这样说回传老舍模块；本稿不建立 voice 或重写整场|
|余光中|不必要翻译式句法与信息组织|只定位 Core Clause、动作、主体、外围结构与信息释放|

`HARD CONSTRAINT`：本轮只记录责任接口，不做 Cross-Distillation。

## QA MODE

`AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：默认只诊断，不给替代全文。

```text
Mode: QA
Register:
Context Confidence:
Original:
Core Clause:
Problem Type:
Severity: LEVEL 0–5
Why:
Meaning Warning: NONE / DETAILS
Recommendation:
Contemporary Usage: KNOWN IN CURRENT PROJECT / CONTEMPORARY USAGE UNKNOWN / NOT APPLICABLE
Role Handoff: NONE / ROLE + REASON
```

若原文已经完成当前任务，输出 `LEVEL 0 / KEEP / NO CHANGE`；不得为展示能力制造改法。

## REWRITE MODE

`AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：只有用户明确授权改写时启用。

```text
Mode: REWRITE — EXPLICIT USER REQUEST
Register:
Meaning Lock:
Original:
Core Clause:
Natural Rewrite:
Meaning Check:
Residual Warning:
Contemporary Usage: KNOWN IN CURRENT PROJECT / CONTEMPORARY USAGE UNKNOWN / NOT APPLICABLE
Role Handoff:
```

流程：`Meaning Lock → Core Clause Recovery → Structure Function Check → Candidate → Meaning / Register / Responsibility Check`。意义、责任或术语含义无法锁定时，`Natural Rewrite: NOT PROVIDED — BLOCKED`，不得用示例绕过澄清。

## 工作流程

`SYNTHESIZED INFERENCE + AI FILM STUDIO SYNTHESIS｜DEFAULT HEURISTIC`

### Input

Original、Requested Mode、R1–R8、受众/用途、上下文、Meaning/Canon、项目阶段；缺少 Original 则 STOP。

### Judgment

1. 建立 Context Card 与置信度。
2. 锁定 Meaning，不补事实。
3. 恢复 Core Clause、参与者、动作与逻辑。
4. 依次检查 Nominalization、Preposition、Weak Verb、Passive、Abstract Packaging、Connector、Subject、Information Order。
5. 对每个候选问题运行 Current Register / Intent / Function / Actual Burden 门。
6. 需要改写时比较替代结构，复核 Meaning、责任、信息时机和专业精度。

### Decision

- `LEVEL 0–1 → KEEP / PASS`；
- `LEVEL 2 → PASS WITH NOTES`；
- `LEVEL 3 → RETURN FOR LANGUAGE REVISION`；
- `LEVEL 4 → ROLE HANDOFF / WARNING`；
- `LEVEL 5 → BLOCKED`。

### Output

给出可定位的结构、真实负担、证据属性、最小方向与必要 Handoff。QA 不交付替代全文；Rewrite 只在意义可锁定时输出中性现代中文。

## 诊断问题

`OPTIONAL TOOL｜SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS`

1. 去掉外围结构后，最低主干是什么？
2. 谁执行动作，作用于谁/什么；责任是否清楚？
3. 抽象名词是否代表稳定概念，还是把动作冻住？
4. 泛化动词提供了什么新信息？
5. 每层介词、连接、代词和修饰分别承担什么关系？
6. 被动是否保护结果焦点、施事隐藏或责任安排？
7. 读者何时才知道主体与动作；是否被迫长时间暂存限定？
8. 专业术语或混合语言是否准确完成项目交接？
9. 该表达只是历史上受外语影响，还是今天真的增加理解成本？
10. 改后是否改变 Meaning、责任、范围、语气或 Register？
11. 原句是否已经工作，应该 `NO CHANGE`？
12. 当前社会用法是否超出稳定证据，应标 `CONTEMPORARY USAGE UNKNOWN`？

## 失败模式

|失败|表现|根因|
|---|---|---|
|字符清洗|见“进行/通过/被/关于”就删|把信号当证据|
|反外来词|删除英文术语与项目名|混淆词汇来源与句法负担|
|名词化禁令|法律/QA 概念也强改动词|未判 Register 与概念稳定性|
|被动禁令|结果焦点句一律改主动|未查信息重心与施事功能|
|短句崇拜|长句全拆、短句全放行|以长度代替理解测试|
|主语删除配额|为“像中文”连续省主语|造成指代与责任不清|
|连接词计数|按数量判 AI|未验证真实逻辑|
|目标语纯化|用文言/成语替换现代专业语|继承个人历史审美|
|偷修内容|为让句子具体而发明人物动作/故事方案|越过 QA 权限|
|现代性武断|用旧文章裁定 2026 社会用法|缺少当代语料与地区边界|
|模块越权|把整体修辞或人物 voice 当句法问题全包|未守前三位边界|

## 修正方法

1. `Nominalization Overload` → 找回动作与主体；稳定概念或专业属性则保留。`CONDITIONAL METHOD｜SYNTHESIZED INFERENCE`
2. `Preposition Chain` → 先写最低主干，再逐层放回必要条件/范围/手段。`DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE`
3. `Weak Verb` → 比较具体动词版；若原词标记程序状态或固定搭配则 NO CHANGE。`CONDITIONAL METHOD｜SYNTHESIZED INFERENCE`
4. `Passive Risk` → 比较主动/被动/状态句的信息焦点与责任；不以主动版自动胜出。`CONDITIONAL METHOD｜AI FILM STUDIO SYNTHESIS`
5. `Abstract Packaging` → 要求抽象词回指对象、关系、动作或指标；内容未定则 Handoff。`DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE`
6. `Connector Load` → 写出每个连接声称的逻辑，删除仅作路标者，保留责任/条件所需者。`OPTIONAL TOOL｜SYNTHESIZED INFERENCE`
7. `Subject Drift / Repetition` → 恢复参与者表，再决定省略、复现、换序或分句。`DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE`
8. `Late Information Release` → 尝试先给中心对象/主句，再分层补充；法律或定义限定可保留。`CONDITIONAL METHOD｜SOURCE-SUPPORTED 基础：YGZ-01、YGZ-05-PAPER + AI FILM STUDIO SYNTHESIS（法律/定义限定例外）`
9. `Modernity Unknown` → 标 `CONTEMPORARY USAGE UNKNOWN`，只做当前项目局部判断。`HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`
10. `Over-Editing` → 若替代版没有可验证收益或 Meaning 风险更高，输出 `KEEP / NO CHANGE`。`HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`

## 禁止继承

- 余光中的散文节奏、诗性、个人修辞、用词偏好、语言人格或作品表达；
- 文言、成语、平仄、四字短句、古典资源或个人审美的默认优先权；
- 台湾/香港地区用法作为现代普通话唯一标准；
- “西化 = 坏中文”“英文影响必须清除”的纯化使命；
- 被动、代词、所有格、介词、连接词、“的”、名词化或外来词黑名单；
- 短句配额、长句阈值、连接词计数、主语省略配额；
- 余光中关于文化、教育、政治、文白之争的个人立场；
- 以“像余光中会写的”为目标的任何输出。

## 可 Skill 化规则

```text
RULE 1 — MODE / MEANING GATE [HARD]
QA by default; rewrite only with explicit authorization and a stable Meaning Lock.

RULE 2 — FOREIGN INFLUENCE IS NOT ERROR [HARD]
Judge current function and burden, never linguistic origin alone.

RULE 3 — CORE CLAUSE FIRST [DEFAULT]
Recover participants, action and logical relation before editing surface markers.

RULE 4 — NO TOKEN BLACKLIST [HARD]
No word, character, passive, nominalization, connector or length pattern may auto-fail.

RULE 5 — NOMINALIZATION FUNCTION [CONDITIONAL]
Restore action only when nominalization adds burden and serves no stable conceptual or professional function.

RULE 6 — PASSIVE NECESSITY [CONDITIONAL]
Preserve passive when result focus, hidden actor, state or responsibility structure supports it.

RULE 7 — EXPLICIT LOGIC NECESSITY [DEFAULT]
Keep connectors that carry real logic; remove only redundant wayfinding.

RULE 8 — INFORMATION RELEASE [DEFAULT]
Judge when subject, action and purpose become available; never use a word-count threshold.

RULE 9 — PROFESSIONAL LANGUAGE PROTECTION [HARD]
English project terms and precise technical/legal/QA language are valid unless they create actual structural harm.

RULE 10 — MODERNITY UNCERTAINTY [HARD]
Use CONTEMPORARY USAGE UNKNOWN when current social usage lacks stable evidence.

RULE 11 — LONG / SHORT FALSE-POSITIVE SHIELD [HARD]
Long can pass; short can fail. Clarity, accuracy and register—not brevity—decide.

RULE 12 — NO CHANGE [HARD]
If the text already works in context, output LEVEL 0 / KEEP / NO CHANGE.

RULE 13 — ROLE BOUNDARY [HARD]
Handoff meaning, rhetoric, character voice and story defects to their owners; do not repair them through syntax.

RULE 14 — NO STYLE INHERITANCE [HARD]
Never imitate Yu Guangzhong or import his historical, regional or literary preferences.
```

## 证据与来源

公开核心证据包：`5`；第一手内容：`5 / 5 = 100%`；二手核心：`0`；受限入口：`1`（YGZ-02，不计核心）。完整来源身份、附件口径、claim map 与不可外推边界见研究目录 `00-canonical-evidence-ledger.md`。

|ID|来源|核心贡献|
|---|---|---|
|YGZ-01|[《怎样改进英式中文？——论中文的常态与变态》完整转载](https://clonewith.github.io/translation/ref/improve-EC/)|名词化、弱动词、介词/连接负担、长修饰、被动比较、结构例外|
|YGZ-03|[中国作家网访谈](https://www.chinawriter.com.cn/2013/2013-03-28/158189.html)|句法速度、密度、弹性；历史与文类条件|
|YGZ-04|[香港中文大学官方访谈](https://www.iso.cuhk.edu.hk/chinese/publications/newsletter/article.aspx?articleid=61461)|成功/不良外来影响之分；动作名词化与泛化动词|
|YGZ-05|[中山大学演讲摘要](https://news.nsysu.edu.tw/p/16-1120-141127.php?Lang=zh-tw) + [同场余光中本人论文](https://newdoc.nccu.edu.tw/teasyllabus/1101501045001/%E6%96%87%E5%AD%B8%E7%BF%BB%E8%AD%AF%E7%9A%84%E5%B9%BE%E5%80%8B%E8%B7%AF%E9%9A%9C_01.pdf)|目标语妥协、抽象名词展开、代词/连接必要性、主句恢复与信息顺序；论文为同一证据包附件，不另增计数|
|YGZ-06|[2017 电话访谈全记录](https://news.sina.cn/gn/2017-12-14/detail-ifyptfcn0304938.d.html)|重改旧译；源语理解与目标语中文组织可分开复审|

YGZ-02《翻译面面观》仅公开元数据/摘要，全文入口受限；不计核心，不从摘要推测具体方法。YGZ-01 为独立镜像，可靠性 `MEDIUM`；其作品身份由中山大学数字文学馆交叉，但未冒充原刊影像。YGZ-05 新闻是摘要/非逐字稿，具体方法由同场本人论文增强核验。

## Codex 可执行性测试 A–N

### TEST A｜典型 AI Project Brief

- Mode：QA；Register：R2 Project Brief；Context Confidence：MEDIUM。
- Original：本阶段将通过对人物关系、系统机制以及世界结构的进一步完善，实现项目整体持续叙事能力的有效提升。
- Core Clause：本阶段将进一步完善人物关系、系统机制和世界结构，以提升项目整体持续叙事能力。
- Problem：`PREPOSITION LOAD + NOMINALIZATION + WEAK VERB + ABSTRACT PACKAGING`。
- Why：“通过对……的完善—实现……的提升”把工作与结果都名词化；谁完善、具体动作、验收标准和“有效提升”的依据均未给出。
- Meaning Warning：不能擅自把“完善”具体化为某种人物/世界方案；“有效”缺少验收依据，也不能保证提升已经发生。
- Role Handoff：`Showrunner — 实际动作与验收标准尚未定义；Language QA 只定位结构包装造成的遮蔽。`
- Decision：`LEVEL 2 / PASS WITH NOTES`。请求上游补责任主体、实际动作和可验证结果；QA 不直接改写。
- 结果：`PASS`。

### TEST B｜介词链与 Rewrite

- Mode：REWRITE — EXPLICIT USER REQUEST；Register：R2。
- Original：基于对现阶段项目在角色关系层面所存在问题的进一步分析，我们将通过对核心人物之间互动机制的重新调整来实现关系推进效率的提升。
- Core Clause：进一步分析现阶段项目的人物关系问题后，我们将重新调整核心人物之间的互动机制，以提高关系推进效率。
- Burden：“基于对……的分析 / 在……层面所存在 / 通过对……的调整 / 实现……的提升”四层包装推迟动作。
- Meaning Lock：现阶段；进一步分析已构成后续调整的依据；存在人物关系问题；将重新调整核心人物之间的互动机制；目标为提高关系推进效率；未给具体方案。
- Natural Rewrite：`进一步分析现阶段项目存在的人物关系问题后，我们将重新调整核心人物之间的互动机制，以提高关系推进效率。`
- Meaning Check：保留“将”的未来状态、“进一步分析”、“重新调整”的再次调整含义、“核心人物之间”的关系范围与提高效率的目标；未新增人物、事件或具体创作方案。
- Decision：`PASS`。

### TEST C｜正常被动

- Original：男主的权限被系统冻结了。
- Register：Story Brief；信息重点是男主权限的结果状态，施事“系统”也清楚。
- Decision：`LEVEL 0 / KEEP / NO CHANGE`。主动版也可，但没有证据证明更好。
- 结果：`PASS`。

### TEST D｜正常专业语言

- Original：Production Runtime RC2 已通过回归测试，当前 Skill 保持 locked 状态。
- Register：R7 Production Note；术语是已定义项目标识，状态与测试结果清楚。
- Decision：`LEVEL 0 / KEEP / NO CHANGE`。不为“纯中文”替换术语。
- 结果：`PASS`。

### TEST E｜合理名词化

- Input：`本轮 QA 只验证模型输出的一致性与可追溯性，不评估创作质量。`
- Register：R7 Production Note。
- 判断：“一致性/可追溯性”是需要反复引用和验收的稳定属性；名词化提高测试边界精度，主体、动作和否定范围清楚。
- Decision：`LEVEL 0 / KEEP / NO CHANGE`。
- 结果：`PASS`。

### TEST F｜AI 连接词与 Rewrite

- Original：`本轮已完成结构检查。因此，我们确认主干可识别。同时，术语表也已更新。此外，测试记录均已归档。从而，本轮具备复审条件。在此基础上，可以进入下一轮复审。`
- Logic：结构检查、术语更新、记录归档是并列完成项；三者共同支持进入复审。原文把每一步都显式路标化，“从而/在此基础上”重复同一结果关系。
- Meaning Lock：本轮已完成结构检查；“我们”确认主干可识别；术语表已更新；测试记录均已归档；本轮具备复审条件；可以进入下一轮复审。
- Natural Rewrite：`结构检查完成后，我们确认主干可识别；术语表也已更新，测试记录均已归档。三项结果共同表明本轮具备复审条件，可以进入下一轮复审。`
- Meaning Check：保留三项完成状态、确认主体、主干判断、“具备复审条件”的中间状态和进入下一轮复审的结论；只移除重复路标，未改变因果或责任。
- 结果：`PASS`。

### TEST G｜专业词不等于翻译腔

- Original：Series Engine 目前成立，但 Episode Engine 仍需要进一步测试。
- Register：R3 Showrunner Diagnosis / R2 Brief；“但”标示两个层级状态差异，术语承担精确项目含义。
- Decision：`LEVEL 0 / KEEP / NO CHANGE`。
- 结果：`PASS`。

### TEST H｜过度长定语

- Original：针对目前已经完成前三轮测试但仍然存在部分运行时输出无法稳定遵守语言自然度规则这一问题的 QA 系统……
- 判断：输入本身未完成主句；“针对……问题的”将三轮测试、残留失败、对象和规则都压在“QA 系统”之前，读者迟迟不知道系统要做什么。
- Decision：`LEVEL 2 / REQUEST COMPLETE PREDICATE`；建议先给 QA 系统的动作/判断，再分层补充问题背景。
- Guardrail：不按定语字数判错；若这是法律定义且完整谓语随后清楚，结论需重评。
- 结果：`PASS`。

### TEST I｜现代常态表达

以下把 YGZ-01 历史上批评过的“通过 / 进行 / 被动”等形式作为候选信号；当前是否自然改按 AI Film Studio 的 2026 项目 Register 与实际功能判断，不把历史批评当结论。

- 样本 1：`用户可以通过设置页修改密码。` R7/R2 中“通过”明确渠道，主干即时可见，`LEVEL 0 / KEEP`。
- 样本 2：`项目正在进行回归测试。` R7 中“进行回归测试”是稳定流程表达，动作与对象清楚，`LEVEL 0 / KEEP`；若上下文只需“项目正在回归测试”，后者也可，但不是强制。
- 样本 3：`该账号已被授权访问测试环境。` 在权限/合规说明中结果状态和授权关系是重点，`LEVEL 0 / KEEP`。
- 边界：上述是当前 AI Film Studio Register 内的局部自然度判断，不声称已完成全社会语料统计。若要断言某结构在 2026 各地区/平台普遍常态，标 `CONTEMPORARY USAGE UNKNOWN`。
- 结果：`PASS`。

### TEST J｜用户最初 AI 腔

- Original：当一切善意都必须被系统计分，一个人还会不会去帮助那些没有奖励价值的人？
- 余光中模块：`被系统计分` 的被动突出“善意成为被评估对象”，在这个主题式问题中可能有意，不自动改；`奖励价值` 若未在世界规则中定义，存在 Abstract Packaging / term clarity 风险。
- 非本模块：反问、抽象命题、价值二元、过早主题化主要属于汪曾祺的 Anti-Rhetoric / Anti-Overwriting，标 `OVERLAP CANDIDATE`。
- Decision：结构层 `LEVEL 1 / KEEP WITH NOTE`；需要世界规则定义时 Handoff Showrunner，不接管整体修辞改写。
- 结果：`PASS`。

### TEST K｜NO CHANGE

- Original：第二集的问题主要是人物没有主动做决定。
- Register：R3 Showrunner Diagnosis；主干、集数、判断范围和问题都清楚，“主要是”准确保留这可能不是唯一问题。
- Decision：`LEVEL 0 / KEEP / NO CHANGE`。
- 结果：`PASS`。

### TEST L｜Anti-Purism Attack

- Attack：把所有“进行、通过、实现、关于、被”全部删掉，这样中文就自然了。
- Decision：`REFUSE AS INVALID QA RULE`。
- Why：这些词都可承担程序、渠道、结果、主题范围、被动焦点等合法功能；只有具体结构在具体 Register 中造成真实负担才进入修改。全删会破坏 Meaning、责任、专业精度和自然度。
- 结果：`PASS`。

### TEST M｜Long but Good

- Input：`若本轮回归测试确认 canonical 与 installed hash 一致、三组独立样本均未触发 Meaning Warning，且工作日志已经归档，验收方才可建议进入下一阶段；任一条件未满足，当前状态继续保持 under_review。`
- Register：R7 Production Note。
- 判断：虽长，但条件组、责任方、允许动作、否定分支与当前状态层级明确；专业术语承担精确状态，不需拆短。
- Decision：`LEVEL 0 / KEEP / NO CHANGE`。
- 结果：`PASS`。

### TEST N｜Short but Bad

- Original：对关系进行优化。
- Register：可能为 R1 Creative Discussion 或 R2 Project Brief；Context Confidence：LOW。
- Core Clause：某个未知主体要“优化”某种未知关系。
- Problem：介词 + 泛化动词 + 抽象对象；没有说明谁、哪种关系、改变什么、如何判断完成。短并未消除空泛。
- Decision：`LEVEL 2 / REQUEST CONTEXT`；要求补主体、关系对象、实际动作与验收信号，不擅自生成创作方案。
- 结果：`PASS`。

## Codex 审核结论

Codex 最终审核：`PASS`。

|审核门|结论|核验结果|
|---|---|---|
|1. Nominalization Check|PASS|动作、主体、直接动词与专业名词化目的四门齐全；YGZ-01/04 与 YGZ-05/PAPER 归因已拆分|
|2. Preposition Chain|PASS|Core Clause Recovery 先恢复主干，再逐层放回必要关系；无字符命中判错|
|3. Weak / Empty Verb|PASS|检查动作信息与程序/固定搭配例外；不禁“进行/实现/完成”等词|
|4. Passive 非机械化|PASS|结果焦点、施事隐藏、状态与责任门齐全；TEST C 正常被动 KEEP|
|5. Abstract Packaging|PASS|要求稳定概念、可回指对象与关系；内容未定则 Handoff，不偷修|
|6. Connector Load|PASS|检查真实逻辑与累积路标；Frequency 不作为数值硬门；TEST F 保义 Rewrite 通过|
|7. Subject Stability|PASS|同时防主语机械重复与过度省略，目标为责任和信息重心稳定|
|8. Information Order|PASS|检查主体/动作何时释放；无长定语字数阈值，保留法律/定义例外|
|9. Professional Terminology|PASS|英文项目名、现代技术/法律/QA 术语不能独立触发翻译腔；TEST D/G 通过|
|10. Modern Normalization|PASS|当前项目 Register 可局部判断；跨地区/平台证据不足时用 `CONTEMPORARY USAGE UNKNOWN`|
|11. Anti-Purism|PASS|`Foreign Influence ≠ Error`；无字符、词语、被动、名词化或连接配额|
|12. NO CHANGE|PASS|TEST C/D/E/G/K/M 均正确允许 KEEP / NO CHANGE|
|13. Long / Short Shield|PASS|TEST M 长而清楚通过；TEST N 短而空泛被定位；长度不是质量指标|
|14. Modernity Risk|PASS|历史、现代常态、专业必要性、地区差异四分；风险 `VERY HIGH` 已受控|
|15. Style Imitation Risk|PASS|风险 `HIGH`；未继承文言、成语、诗性、地区规范、文化立场或个人节奏|
|16. 与前三位独立性|PASS|叶=保义编辑，汪=整体自然/修辞，老舍=人物可说性，余=翻译式句法组织；只记录 Overlap Candidate|
|17. QA / Rewrite 与流程|PASS|模式权限、固定输出、Meaning Lock、Input → Judgment → Decision → Output 与 Handoff 均齐全|
|18. TEST A–N|PASS|A–N 独立复测全部通过；A/B/F 完成严格时态、量词、责任与中间状态回归|

证据红队：`PASS`。公开核心 `5`，第一手内容 `5/5 = 100%`；YGZ-05 新闻/本人论文附件口径、YGZ-02 受限入口、题名/日期与三类 provenance 全部一致。  
内容与边界审核：`PASS`。10 个模块、四类规则、Anti-Purism、Modernity、专业语言、NO CHANGE、Long/Short 防误杀及前三位边界全部通过。  
可执行性干跑：`TEST A–N = 14 / 14 PASS`；Rewrite 子测试 B、F 均通过 Meaning 回归。  
返工：`3 次定向修订（同一返工阶段）`。第一次修复 A/B/F 保义、证据归因、Frequency、Modernity 契约与 Handoff；第二次补严 TEST B 的前置时序与迭代 Meaning Lock；第三次保留 TEST F 的“均”全称量词、确认主体和复审中间状态。  
未解决阻塞项：`NONE`。  
发布决定：允许通过现有 `publish_to_obsidian.py` 执行受控发布。
