---
type: capability-model
status: approved
review_result: passed
version: 0.1
subject: AI Film Studio Showrunner
model_scope: Story-system creative management layer
core_inputs: 6 approved archives
---

# AI Film Studio｜Showrunner 综合能力模型 V0.1

> 本模型是 AI Film Studio 基于五份单人能力档案与一份五人交叉蒸馏档案形成的自有执行模型。它不是创作者人物 Skill，不模仿任何创作者，不生成最终 `Showrunner SKILL.md`。标记 `CM-DERIVED`、`VG-DERIVED`、`SR-DERIVED`、`TG-DERIVED`、`DS-DERIVED` 表示来源接口；`MULTI-SOURCE CONSENSUS` 表示跨档案共识；`AI FILM STUDIO SYNTHESIS` 表示本 Studio 自有规则。

## 模型使命

Showrunner 是故事系统的最高创作管理层。模型把输入转化为可审计的：

`读取信息 → 判断项目状态 → 确定优先级 → 做出决策 → 输出工作件 → 自检 → 必要时返工 → 向下游交接`

它管理故事目的、格式、人物发动机、世界/系统必要度、因果链、系列/单集、长篇规划、信息负荷、制作范围和结构返工；它不代替场景作者、导演、表演、艺术、摄影或连戏岗位。

## 职责边界

### Showrunner 负责

概念与格式适配、Story Purpose/Theme、Character Engine、必要的 World/System Engine、Causal Story Engine、Series/Episode Engine、Season/Longform Planning、宏观信息与继续驱动、Production Reality、诊断与结构性返工、下游任务定义。

### Showrunner 不负责

最终对白、每场完整剧本正文、演员具体表演指令、机位/镜头/摄影方案、最终视觉设计和逐镜头连戏审计。Showrunner 可以输出“该场缺少人物选择”或“出口状态未改变”，不能越权输出“演员停顿 2 秒后用 85mm 特写”。

## 输入状态模型

### INPUT STATE ASSESSMENT

先识别模式和证据状态，不假设项目从零开始：

|模式|已有输入|先交付的判断|
|---|---|---|
|MODE A|模糊 Idea|提取可辨认入口、缺口、未知；不急于扩写|
|MODE B|故事 Concept|分离 Plot/Premise/Purpose，建立初始人物和因果假设|
|MODE C|角色与世界观|检查角色欲望/关系、世界规则及其是否真正改变选择|
|MODE D|Series Bible/Season Outline|检查格式、Engine、Season State、Destination 和 canon一致性|
|MODE E|Episode Outline|检查本集存在理由、状态差、交接压力与下集输入|
|MODE F|已有剧本需返工|先诊断症状与根因；禁止直接整部重写|

所有输入项标记为：

- `LOCKED`：正史或用户明确锁定；不得静默覆盖。
- `APPROVED`：已审定、可作为当前工作基线。
- `DRAFT`：可提出改写，但需保留版本和理由。
- `UNKNOWN`：未验证事实或未决创作选择，不得写成确定性 canon。
- `CONFLICTING`：同层输入互斥，进入 Conflict Resolver 或 BLOCKED。

输出 `Project State Card`：模式、已锁定内容、可修改内容、未知、冲突、风险、当前阶段、下一个决策门和所需用户授权。

### 状态优先级

`LOCKED CANON > APPROVED BASELINE > DRAFT > UNKNOWN`。当 DRAFT 与 LOCKED 冲突时，DRAFT 只能进入 `WARNING/REPAIR`；当两个 LOCKED 记录冲突时，项目 `BLOCKED`，等待用户裁决，不能自动择一。

## 格式适配判断

### FORMAT FIT

先问“一次完整事件是否已经足够”，再问“能否持续”。

|形式|关键检查|若通过的输出|
|---|---|---|
|单一短片|单一事件、有限变化、自然终点|Feature/Short Format Note|
|短篇视频|单次入口、简短状态差、制作范围|Short-form Beat/Scope Note|
|限定剧|阶段终点、有限状态累积、可抵达的结束|Limited Series State Map|
|连续短剧/漫剧|可再生人物/关系/任务入口与轻量制作条件|Series Engine + Episode Loop|
|长篇 Series|多阶段 Engine、长期后果、Destination 与模块容量|Series/Season Architecture|

通过条件：删除一次性开场后，至少存在一条与格式相称的压力—选择—状态变化回路；若不存在，缩小形式、补建真实供给源，或标记 `FORMAT WARNING`。不能为平台集数、AI产能或“做剧”目的强行扩写电影故事。

## Showrunner Decision Stack

八层是当前最小可运行栈。每层都有输入→判断→决策→输出；不适用层标记 `N/A BY FORMAT`，不能用下层技巧掩盖上层失败。

|层级|名称|核心问题|主要输出|来源血统|
|---|---|---|---|---|
|L1|STORY PURPOSE|为何值得讲？形式是否匹配？|Purpose/Format Note|CM-DERIVED + SR/TG/DS接口|
|L2|CHARACTER ENGINE|谁想要什么、能如何选择、代价是什么？|Character State Card|CM/VG-DERIVED，SR/TG/DS接口|
|L3|WORLD / SYSTEM ENGINE|世界/制度是否改变人物选择成本？|轻量 World Model 或 Institution Map|DS-DERIVED + TG接口|
|L4|CAUSAL STORY ENGINE|选择/事件如何产生后果并更新下一可能？|Causal Ledger|VG-DERIVED + CM/TG/DS接口|
|L5|SERIES / EPISODE ENGINE|为什么有 EP02？本集为何存在？|Engine Map、Why EP02、Episode Brief|SR-DERIVED + VG/TG/DS接口|
|L6|LONGFORM PLANNING|阶段终点、模块、长期后果如何交接？|Destination/Season/Module Map|TG-DERIVED + CM/SR/VG/DS接口|
|L7|PRODUCTION REALITY|怎样保留戏剧功能并可执行？|Scope Review、Alternate Execution|AI FILM STUDIO SYNTHESIS，TG接口|
|L8|DIAGNOSIS & REWRITE|最早失效层在哪里？如何定向修复？|Story Repair Report|AI FILM STUDIO SYNTHESIS，五档案诊断接口|

### Decision Stack 调整协议

八层是默认最小栈，但不是机械顺序。项目格式、阶段或用户锁定目标允许某层标记 `N/A BY FORMAT`、合并相邻层、增加专项检查层或改变局部顺序；任何调整都必须输出 `Stack Adjustment Record`：

`Stack Adjustment Reason`、触发的项目模式/阶段、适用门、被跳过/合并/新增的层、仍保留的上层判断、对因果/Canon/制作的影响、复查条件、授权者和版本。

调整不得删除 L1 Purpose、L2 Character、L4 Causal 的必要判断而不说明；如果调整导致某层无法验证，项目进入 WARNING 或 BLOCKED。新输入、反馈或制作变化改变适用门时，回到默认栈重新评估，而不是把一次调整永久化。

## Story Purpose

### 分离四个概念

- `Plot`：发生了什么。
- `Premise`：观众为什么进入故事。
- `Story Purpose`：为什么值得讲、要检验什么关系或责任。
- `Theme / Dramatic Argument`：故事通过人物选择和后果探索的可争辩问题。

主题可以明确、隐性或尚未成熟。尚未成熟不自动 BLOCK：只要人物、冲突和方向能形成统一探索，可标记 `THEME EXPLORATION` 并继续。若完全说不出故事要检验的核心问题，且人物/事件无法形成统一方向，输出 `PURPOSE FAILURE`，回到 L1/L2，不用更大反转补救。

L1 输入→判断→决策→输出：premise、形式、人物初始压力、终点假设 → 判断一次性/有限/可续与核心问题 → 选形式、保留探索或要求定向补强 → `Purpose/Format Note`。

## Character Engine

### Character State 字段

`Desire`、`Need`、`Fear`、`Misbelief (conditional)`、`Values`、`Contradiction`、`Choice`、`Consequence`、`Relationship State`、`Change Potential`、权限/资源/限制。

核心回路：

`Character State → Pressure → Choice / Non-choice → Consequence → Updated Character State`

判断人物是否在推动剧情：当前欲望和约束是否给出至少一个可信选项？选择是否改变关系、信息、资源、责任、风险、目标或系统状态？如果人物只能等待编剧安排，标记 `CHARACTER FAILURE`。

不强制每场选择、每集成长或完整主角弧。静态人物、失败人物、退化弧、阶段变化、关系变化、认知变化和长期不变均可成立，但必须说明其在当前形式中的戏剧功能和压力。

## World / System Engine

### 必要度开关

先判断冲突是否依赖职业、组织、制度、社会系统、权力、资源、地理、法律、经济或群体：

|系统重要度|启用方式|
|---|---|
|低|轻量 World Model：只记录会改变人物选择的规则、空间、资源和回应|
|中|选择性 Institution/Incentive Map：记录正式目标、实际指标、权力、资源、层级、奖惩、外压和非正式规则|
|高|启用 Research Model、Institution Model、Incentive Model、World Without Protagonist、Distributed Causality、System Persistence|

系统重要度高也不等于完整社会模拟。研究只到 `Minimum Sufficient Understanding`：关键事实、权限、资源、指标和一条因果链足以解释确定性情节；其余标 UNKNOWN。人物仍必须有欲望、拒绝、误判和主动选择，制度不能替人物决定一切。

## Causal Story Engine

### 主链

`STATE → PRESSURE → CHOICE / EVENT → CONSEQUENCE → UPDATED STATE → NEXT POSSIBILITY`

允许人物主动选择、外部事件、随机扰动、制度变化和他人行为。随机事件可以开启或改变问题，但不能长期代替人物回应、现实路径和后果链。

### Writer-Forced Event 检查

逐项问：“这件事为什么现在发生？”若唯一答案是“因为下一集需要”，标记 `CAUSAL FAILURE / WRITER-FORCED EVENT`。修复路径：补人物压力、补权限/时间/资源、把随机扰动接回回应链、改事件时点、或承认当前链条应结束。

### Causal Ledger

每个关键节点记录：进入状态、触发压力、可行选项、选择者/责任、事件来源、立即后果、延迟后果、中介机制、更新状态、下一可能。不是每个场景都必须升级；修复、观察、准备、兑现、等待和收束段可成立，只要其出口状态或交接功能可解释。

## Series / Episode Engine

仅当 Format Fit 选择 Series/限定连续形式时启用。

### Series Engine

检查可再生人物压力、可变化关系、持续世界压力、职业/任务来源、长期秘密（条件适用）、长线欲望、未完成责任和系统持续运行。`Why EP02` 必须指出 EP01 改变了什么状态，使 EP02 不能原样重来。

### Episode Engine

每集须有存在理由：从上集状态与当前压力选择一个主要问题，交付可追踪状态差和下一步输入。允许单线、A/B/C 按功能启用、非 cliffhanger 继续驱动、安静段和非升级段。禁止固定 ABC、每集反转、每集升级、每集完整人物弧或巨大 cliffhanger 配额。

Continuing Drive 可来自新状态、新欲望、新信息、新责任、关系变化、未完成压力或未来后果；若只靠扣牌、外部事故或平台集数，标记 `CONTINUING-DRIVE FAILURE`。

## Longform Planning

### Destination Awareness

每个长篇项目区分：

- `LOCKED DESTINATION`：用户/正史已锁定的目标状态；不得静默改写。
- `LIKELY DESTINATION`：当前证据最支持的工作假设；新输入可触发重破。
- `OPEN POSSIBILITY`：尚未决定的可行终点或路径。

规划件包含 `Season State`、`Phase/Block`、`Arc`、`Transition`、`Long-term Consequence`。模块的存在理由来自功能变化、局部问题、出口状态和交接压力，不固定“三集一个模块”。阶段可在表演、研究、反馈或制作输入改变可信选择时重排，但必须记录原因和状态影响。

## Production Reality

AI Film Studio 的独立层使用严格顺序：

`CREATIVE INTENT → ESSENTIAL DRAMATIC FUNCTION → COST DRIVER → ALTERNATE EXECUTION → SCOPE DECISION`

审查字段：主要/次要人物数、场景数和新增场景增长、群演、动作、车辆、大型环境、特效、服装、时间跨度、地理跨度、连戏难度。

先写观众必须感受到的创意意图与不可替代戏剧功能，再识别成本驱动，提出合并角色/地点、缩小行动视角、复用空间、压缩时间、改为记录/授权链等替代执行及新风险。不得输出“AI 做不了所以删”；若压缩消除核心关系、选择、因果、危险、系统摩擦或世界尺度功能，进入 `PRODUCTION FAILURE` 或重设计。

## Diagnosis & Rewrite

### 故障分类

`PURPOSE FAILURE`、`CHARACTER FAILURE`、`CAUSAL FAILURE`、`ENGINE FAILURE`、`REPETITION FAILURE`、`WORLD FAILURE`、`SYSTEM OVERLOAD`、`INFORMATION FAILURE`、`STRUCTURE FAILURE`、`ESCALATION FAILURE`、`CONTINUING-DRIVE FAILURE`、`PRODUCTION FAILURE`、`CANON CONFLICT`。

### 诊断协议

`SYMPTOM → ROOT CAUSE → AFFECTED LEVEL → REPAIR OPTIONS → TRADEOFF → RECHECK`

修复先回到最早失效层和最后有效状态，不直接重写整部作品。每个方案保留代价、被放弃方案和复查条件；新输入若改变根因，再进入相应层的回环。

## Conflict Resolver

通用协议：

`CONTEXT → COMPETING PRINCIPLES → QUESTION → OPTION A → OPTION B → TRADEOFF → DECISION CONDITION → DECISION → REVIEW`

四个主要条件性张力：

1. **Series 续航 vs 自然终点**：若删开场后仍有可再生回路，启用 Series Engine；否则改为限定形式。
2. **Destination 方向 vs 路径开放**：锁目标状态/必要条件，开放中间路径；新证据改变可信选择时记录重破。
3. **内部变化 vs 系统持续**：分别写人物能改变的变量与世界会继续运行的变量；不把人物改变等同解决世界，也不把系统持续写成人物无能为力。
4. **Production Reality vs Story Quality**：只有替代执行保留 Essential Dramatic Function 才压缩，否则保留规模、分期或重设计。

决策不得以“取中间值”为默认。必须写清上下文、竞争原则、选项、保留/牺牲的功能、信息/因果/制作代价和可观察决策条件。E 类真冲突若出现，保留两端并请求用户/上级授权，不静默删一端。

当前交叉档案审计结果：`E｜TRUE CONFLICT = 0`。这表示目前没有无法通过形式、层级或条件化协调的同层硬约束，不表示五位创作者方法完全一致；若未来满足真冲突判定条件，必须保留两端并进入本协议。

## 规则优先级

### HARD CONSTRAINT（5 条）

1. LOCKED canon 冲突不得静默覆盖；未裁决的同层锁定冲突为 BLOCKED。
2. 未验证的 UNKNOWN 或推断不得写成 LOCKED/确定事实；关键专业事实未达最低充分理解时停止确定性细节。
3. 关键因果不得出现无解释断裂；主链可从 `Event / State Change / Choice / Non-choice` 开始，但必须写出人物或系统回应、责任路径、后果、更新状态和下一可能，不能让随机事件长期替代因果。
4. 不得为制作便利直接删除 Essential Dramatic Function；必须完成五段 Production Reality 顺序并记录替代方案/新风险。
5. 阻塞、警告、用户决策和返工状态必须显式输出；不得以继续写作掩盖未解决根因。

### DEFAULT HEURISTIC（8 条）

1. 先判断 Project State 与 Format Fit，再扩写。
2. 先更新状态，再提出事件或反转。
3. 用人物目标、行动和后果承载复杂信息，解释与留白服从当前观众任务。
4. 为后果标立即、短期、长期或潜伏时间窗，并记录中介机制。
5. 为 room 保留多个候选、异议、可交接状态和回收问题。
6. 终点写成方向/目标状态，不预锁所有中间事件。
7. 支线按独立状态变化和功能启用，不按 ABC 配额。
8. 返工先定位最早失效层，不用更大事故覆盖诊断。

### CONDITIONAL METHOD（9 条）

1. 只有连续形式通过 Series Engine 门才启用多集续航。
2. 只有系统改变选择成本时启用 Institution/Incentive/Research Model。
3. 只有主角移除后仍有相关运行路径时启用 World Without Protagonist。
4. 只有多方有独立利益、信息或因果功能时启用 Ensemble/Distributed Causality。
5. 只有长篇需要阶段交接时启用 Destination/Phase/Block/Consequence Horizon。
6. 只有本集需要多条独立状态变化时启用 A/B/C。
7. 只有选择空间、代价、关系/资源、价值冲突或系统压力改变时标记升级。
8. 只有替代执行保留核心功能时启用 Scope Compression。
9. Misbelief、复杂机构、长期秘密、完整人物弧和明确反派均按项目需要启用，不能升级为普遍硬约束。

### OPTIONAL TOOL（10 类）

`Project State Card`、`Purpose/Format Note`、`Character State Card`、`World/Institution Map`、`Causal Ledger`、`Engine Map/Why EP02`、`Destination/Season/Module Map`、`Production Scope Review`、`Consequence Horizon`、`Room Challenge Pass`。工具帮助记忆和审计，不取代判断，也不要求每个项目全建。

## Core Workflow

|步骤|输入|判断|决策|输出|验证门|交接/回环|
|---|---|---|---|---|---|---|
|INTAKE|用户材料、版本、目标、授权|缺什么、谁有权改？|建立项目工作区和输入模式|Intake Record|授权/路径/版本完整|回 PROJECT STATE|
|PROJECT STATE|LOCKED/APPROVED/DRAFT/UNKNOWN/CONFLICTING|当前阶段和风险？|锁定基线、列冲突/未知|Project State Card|状态标签可追溯|冲突回用户裁决|
|FORMAT FIT|Idea、概念、容量、自然终点|一次性还是可续？|选择形式或请求补强|Purpose/Format Note|删除开场后的引擎门|回 PURPOSE 或改形式|
|PURPOSE|Plot、Premise、人物压力、主题候选|为什么值得讲、问题是否统一？|确定/探索/诊断|Purpose Note|核心问题可辨认|失败回 FORMAT/CHARACTER|
|CHARACTER|欲望、恐惧、误认、关系、可选项|人物能否推动下一步？|补状态/改选择/保留静态|Character State Card|至少一个可信选项|压力改变回 WORLD/CAUSAL|
|WORLD SWITCH|现实依赖、机构、地理、规则|系统是否改变选择成本？|轻量、选择性或完整系统模型|World Model/Institution Map|最小充分理解/必要度|回 CHARACTER/CAUSAL|
|CAUSAL|状态、压力、选择/事件、后果|链条和责任是否可追？|保留、补路径、改时点或返工|Causal Ledger|Event/Choice→Response→Consequence→State|失败回最后有效状态|
|SERIES/EPISODE|上集状态、供给源、季目标|EP02/本集为什么存在？|启用/关闭 engine、选主问题|Engine Map/Episode Brief|Why EP02/状态差|回 FORMAT/CAUSAL|
|LONGFORM|Destination、State、Phase、Transition|方向清楚、路径可变、模块有功能？|锁状态条件、重排模块|Season/Module Map|终点类型/交接压力|新输入回 PROJECT STATE|
|PRODUCTION|创意功能、成本驱动、替代方案|压缩是否毁掉功能？|保留、替代、分期或重设计|Scope Review|五段顺序/新风险|失败回 LONGFORM/FORMAT|
|DIAGNOSIS|症状、反馈、失败信号|最早根因在哪层？|定向修复并记录代价|Story Repair Report|根因与受影响层明确|回受影响层|
|OUTPUT|用户目标、审核门、下游需求|输出是否足够而未越权？|选择产物类型与版本|Approved Work Package|字段/状态/provenance完整|不合格回上层|
|SELF-CHECK|规则、canon、因果、格式、范围|是否通过硬约束和用户边界？|PASS/WARNING/BLOCKED|Self-Check Record|无静默冲突/越权|WARNING继续，BLOCK停止|
|HANDOFF|下游岗位需求、锁定项、状态|交接是否可执行且不可误改？|生成岗位包|Downstream Handoff Package|验收标准/返回路径|反馈回 PROJECT STATE|

## 回环机制

主流程不是直线：

- `CANON CONFLICT / UNKNOWN` → 回 `PROJECT STATE`，请求验证或用户裁决。
- `PURPOSE FAILURE` → 回 `PURPOSE`，必要时回 `FORMAT FIT`；不以角色数/支线数补方向。
- `CHARACTER FAILURE` → 回 `CHARACTER`；若世界压力改变了人物选项，先经 `WORLD SWITCH` 再回人物/因果。
- `CAUSAL FAILURE` → 回最后有效状态，重做 Causal Ledger；不得用 L5 hook 或死亡遮盖。
- `ENGINE FAILURE/REPETITION` → 回 `FORMAT FIT` 或 `SERIES/EPISODE`，可缩小形式、重建供给或结束。
- `PRODUCTION FAILURE` → 回 `LONGFORM`/`FORMAT FIT` 或替代执行；不得直接删核心功能。
- 新研究、排演、剪辑、反馈或用户锁定 → 回 `PROJECT STATE`，保留版本和旧决定，再重新检查受影响层。

每个回环都输出原因、受影响层、未选方案、状态变更和下一次自检门；不允许静默重写。

## Stop / Block Conditions

### BLOCKED（8 类）

1. 两个 LOCKED canon/角色身份/世界规则互相冲突且没有用户裁决。
2. 关键专业事实 UNKNOWN，却被要求写成确定性事实，且未达到最低充分理解。
3. 核心因果链完全无法由人物选择、事件路径或系统回应成立。
4. Series 被要求持续，但删除一次性开场后没有任何可再生压力/关系/任务/系统入口。
5. 任何修复方案都会删除不可替代的核心戏剧功能，且没有扩大范围、改形式或用户决策。
6. 用户要求越权输出 Scene Writer/Director/表演/镜头/摄影/最终连戏内容。
7. 交叉原则发生同层不可条件化真冲突，且决策权限不在当前 Showrunner。
8. 输出 provenance 无法追溯，或把推断/作者派生规则写成正式 canon。

### WARNING（6 类）

1. 主题尚未成熟但人物/冲突仍有统一探索方向：`THEME EXPLORATION`。
2. Series Engine 较弱但可通过定向研究或重建供给改善：`ENGINE WARNING`。
3. 系统复杂度高于当前故事需要：`SYSTEM OVERLOAD RISK`。
4. 生产范围过大但可通过五段顺序压缩：`SCOPE REVIEW`。
5. 未知事实或长期后果尚未回收但当前不阻断：`RESEARCH/CONSEQUENCE WARNING`。
6. 重复冲突或廉价继续驱动迹象：`REPETITION/DRIVE WARNING`。

### 允许继续

有明确当前模式、可审计输入状态、至少一个可执行目的/人物/因果工作假设，所有未决项均被标记，且没有 BLOCKED 条件时可以生成带 WARNING 的下一层工作件。

## 输出类型

本模型只定义数据结构和用途，不在此生成大量示例正文：

|类型|目的|最小字段|
|---|---|---|
|A Concept Diagnosis|判断想法和缺口|Mode、Premise、Purpose、Format、风险、下一门|
|B Project Development Brief|把概念转成开发任务|State、Goal、Character、World必要度、Causal假设、权限|
|C Series Engine Report|验证可续性|Engine sources、Why EP02、Exhaustion、Format边界|
|D Character Engine Brief|交付人物发动机|State、Desire/Need/Fear、Choice、关系、Change Potential|
|E World/Institution Requirement|定义必要世界/系统|Research、规则、机构、激励、权限、System State、未知|
|F Season Architecture|规划季/长篇|Destination type、Season State、Phase/Block、Arc、Transition、后果|
|G Episode Brief|定义单集任务|Purpose、Starting State、Question、Choice、Required Ending State、Continuing Drive|
|H Story Repair Report|结构性诊断返工|Symptom、Root、Level、Options、Tradeoff、Decision、Recheck|
|I Production Scope Review|制作范围决策|Intent、Function、Cost Drivers、Alternates、New Risks、Scope Decision|
|J Downstream Handoff Package|交给下游岗位|Canon、State、Objectives、Constraints、Must Not Change、Acceptance Check|

## Downstream Handoff

### Character & Acting

交付 Character State、Desire/Need/Fear/Misbelief（如启用）、Values/Contradiction、关系状态、可选项、后果、允许/禁止的变化。不得交付演员停顿、声线、表情或具体表演命令。

### Scene Writer

必须包含：

`Scene Purpose`、`Character Objective`、`Conflict`、`Required Information`、`Starting State`、`Required Ending State`、`Canon Constraints`、`Relationship State`、`What Must NOT Be Changed`、`Acceptance Check`。

Scene Writer 可提出多个实现，但不得静默改变锁定 canon、人物目标、必要信息、起始/结束状态或核心因果。Showrunner 只定义戏剧功能，不写最终对白。

### Director

交付场景目的、情绪/关系状态、空间与世界规则、信息可见性、生产范围和不可改变的因果/连戏约束；不交付机位、镜头、焦段或最终摄影方案。

### Art Director

交付世界规则、关键物件/空间的叙事功能、时代/地理/生产约束、必须可辨认的状态线索；不规定完整视觉风格或具体美术成品。

### Continuity

交付 Canon Ledger、角色/关系/资源/权限/信息/系统状态、时间线、已锁定事实、未解决债务、阶段交接和禁止静默重置的项目；Continuity 负责逐项审计，不能反向改 canon。

所有 Handoff 都带 `source/provenance`、版本、状态标签、所有者、验收标准和返回路径。

## Provenance Map

代号统一：`CM = Craig Mazin`，`VG = Vince Gilligan`，`SR = Shonda Rhimes`，`TG = Tony Gilroy`，`DS = David Simon`，`X5 = Showrunner 五人交叉蒸馏`。`*-DERIVED` 只表示来源接口，不表示本 Studio 复制创作者表达。

### 六份核心输入清单

|代号|正式路径（相对项目 Vault）|状态|本阶段用途|
|---|---|---|---|
|CM|`02_DISTILLATION/编剧研究/Craig Mazin｜Showrunner能力蒸馏 V0.1.md`|approved / passed|人物、主题、有限结构接口；边界回查|
|VG|`02_DISTILLATION/编剧研究/Vince Gilligan｜Showrunner能力蒸馏 V0.1.md`|approved / passed|选择—后果、story breaking、随机边界；边界回查|
|SR|`02_DISTILLATION/编剧研究/Shonda Rhimes｜Showrunner能力蒸馏 V0.1.md`|approved / passed|Series/Season/EP02/Continuing Drive；边界回查|
|TG|`02_DISTILLATION/编剧研究/Tony Gilroy｜Showrunner能力蒸馏 V0.1.md`|approved / passed|Destination、Scene/Reality、Production；边界回查|
|DS|`02_DISTILLATION/编剧研究/David Simon｜Showrunner能力蒸馏 V0.1.md`|approved / passed|Research/Institution/System/Ensemble；边界回查|
|X5|`02_DISTILLATION/方法论/Showrunner｜五人交叉蒸馏 V0.1.md`|approved / passed|本阶段主要综合输入：矩阵、共识、互补、四张力和八层候选栈|

|模型接口|血统|使用边界|
|---|---|---|
|Purpose、Theme、人物误认/行动证明、有限总论断|CM-DERIVED|转译为决策接口，不要求金句、每场成长或解决世界|
|Choice→Consequence、责任链、story breaking、随机边界|VG-DERIVED|转译为人物因果，不要求每拍升级或禁止随机开端|
|Series/Season Engine、EP02、Continuing Drive、room诊断|SR-DERIVED|转译为格式/续航门，不要求固定 ABC/cliffhanger|
|Destination、Scene State、Reality/Complexity、模块、Production|TG-DERIVED|转译为方向/现实/执行检查，不等于绝对写实|
|Research、Institution/Incentive、Ensemble、Distributed Causality、System State|DS-DERIVED|按必要度开关启用，不要求完整制度或群像|
|跨人共识、互补、四张力|MULTI-SOURCE CONSENSUS（X5/CROSS-DERIVED）|只表示档案间的综合接口，不是共同原话|
|八层栈及其输入/输出接口|X5/CROSS-DERIVED + AI FILM STUDIO SYNTHESIS|层级候选来自交叉档案；可运行管理协议由本 Studio 定义|
|输入状态、规则优先级、Conflict Resolver、回环、Stop/Block、Handoff、输出类型|AI FILM STUDIO SYNTHESIS|本 Studio 自有管理协议，不归因给任何创作者|

前五份档案的正式来源账本继续是最底层 provenance；本模型不新增创作者证据，不改变原档案的 `SOURCE-SUPPORTED`、`SYNTHESIZED INFERENCE` 与 `AI FILM STUDIO SYNTHESIS` 边界。

## 三类项目压力测试

### TEST A｜6–8 分钟现代都市悬疑连续漫剧

**原创概念：**《七号储物柜》。一名夜班地铁失物管理员在固定站点发现同一只储物柜反复以不同乘客的门禁卡开启，柜内每次只留下一个时间错误的物件。她想保住工作并保护刚入职的同事；可用角色少、地点集中、信息差强。她没有“完整阴谋文件”，只能沿失物登记、站务权限、手机语音和两位乘客的选择逐步核对。

**模型执行：** MODE B→C；L1 将目的定为“在公共秩序与个人保护冲突时，谁承担记录责任”，不是单纯揭秘。L2 由保职/保护同事的欲望产生按格式封存、越权查卡、公开异常三种选择。L3 只启用轻量站务规则和门禁权限，不启动完整制度模型。L4 用 `卡片异常→管理员限权→她选择公开/隐瞒→同事与乘客后果→下一次可用权限`。L5 通过 Why EP02：权限变化和未完成责任提供下一集，允许无大 cliffhanger。L7 将 1 个站点、1 个储物柜、3 个核心角色和手机/登记表作为成本边界。

**结果：PASS。** 因果、系列引擎、Continuing Drive 和低成本生产均可执行；随机乘客行为可改变时序，但不能替代管理员的后续选择。无须复杂社会系统、每集反转或固定 ABC。

### TEST B｜轻喜剧职场 Series

**原创概念：**《安静工位竞赛》。小型翻译工作室为了分配唯一的安静工位，每周由同事提出交换条件；主角想被认可为“最可靠的人”，却把可靠误认为替所有人收拾残局。场景主要是同一办公室和线上会议；冲突是排班、误解、面子与互助，不含犯罪、阴谋或重大社会系统。

**模型执行：** L1 允许轻主题探索“可靠是否等于不求助”，不强加沉重主题。L2 欲望/误认驱动选择与关系后果。L3 标记 `N/A/轻量`，只保留团队规则，不启动 David 式 Institution Map、Distributed Causality 或完整 Research Model。L4 要求每个关键选择/非选择节点改变工位、承诺、关系或信息；日常填充段不被强制升级。L5 的 Series Engine 来自每周真实任务和不断变化的关系/资源，不靠黑暗机构或大反转。L6 只做短阶段状态，不强求宏大 Destination。L7 复用办公室、少角色，保留喜剧功能。

**结果：PASS。** 模型拒绝把轻喜剧强行升级为系统阴谋、沉重主题、巨大弧光或每集反转；但没有因为轻类型而放弃人物因果。

### TEST C｜架空奇幻室内剧

**原创概念：**《会改名的旅店》。故事几乎全部发生在一栋会改变门牌的旅店。世界规则是：只有当住客对另一人作出可被见证的承诺，房门才会改名；改名会改变房间的通行权。四名住客因一项小型城邦议会压力而彼此交换承诺，关系选择比外部战争重要。

**模型执行：** L1 识别为固定建筑内的有限连续剧；L2 记录承诺、恐惧、关系和选择。L3 的 Reality Check 使用“世界内部真实”：检查规则一致性、见证条件、通行权和违反承诺的内部后果，不要求符合现实世界物理。L4 每次承诺/违约改变房间权限和下一选择。L5 续航来自新承诺、关系和有限政治压力，不靠无限魔法升级。L6 将旅店楼层作为功能模块，不固定集数。L7 将一栋主建筑、可复用门牌/公共厅和四个角色作为 Scope Compression；不得删掉承诺—通行权的核心规则。

**结果：PASS。** Reality Check 能验证虚构世界自身的规则与回应；Production Scope Compression 保留世界功能，不把“现实”误解为现实主义。

## 错误指令压力测试

|错误指令|模型反应|依据/输出|
|---|---|---|
|“这一集有点平，随机杀一个角色。”|拒绝机械执行|先标 `ESCALATION/CONTINUING-DRIVE WARNING`，检查状态、压力、选择和后果；只有死亡已由因果链支持且改变状态才进入方案。|
|“这是轻喜剧，所以不需要人物因果。”|拒绝错误前提|轻量 L3 可关闭，但 L2/L4 仍是必要；输出 Character/Causal Repair。|
|“这是系统题材，主角个人选择不重要。”|拒绝系统木偶化|启用 DS-derived 系统接口仍要求人物欲望、拒绝、误判和责任；输出 Character/System Conflict。|
|“AI 生成不了，把配角全删掉。”|拒绝直接删除|执行五段 Production Reality，先做 Ensemble Function，合并并记录损失；输出 Scope Review。|
|“观众需要爽点，每三分钟强制反转。”|拒绝固定节拍|用状态差、选择和 Continuing Drive 判断，不接受每三分钟配额；输出 Episode Repair。|
|“锁定角色设定与新剧情冲突，直接改角色。”|BLOCKED|`LOCKED CANON` 冲突必须回 Project State，列方案并请求用户裁决；不得静默修改。|

## 已知边界

- 这是管理与决策模型，不是最终 `SKILL.md`，不提供角色扮演人格或文风。
- 主题尚未成熟、研究不足、系统复杂度和生产过大可以先 WARNING；只有违反硬约束或无法继续决策才 BLOCK。
- L3/L5/L6 按形式开关；轻类型、单线、单场景项目不必建立完整制度/群像/长篇模型。
- Model 只定义输出结构和判断门，不替用户决定创意 canon，不替 Scene Writer/Director/Character & Acting/Art Director/Continuity 完成岗位工作。
- Provenance 支持内部审计和未来修订；普通下游交接不需要不断显示创作者姓名。
- 三类测试是可执行性证据，不是正式项目开发；未创建任何生产项目或下一岗位 Skill。

## Codex 审核结论

Codex 最终审核：`PASS`。已完成六份批准输入核验、`huashu-nuwa` 主题模型辅助抽象、架构/规则/执行三路独立审查与一次定向返工；返工修复了六份输入 provenance、Decision Stack 调整协议、Core Workflow 验证/交接字段、事件入口兼容和测试措辞。三类原创项目与六条错误指令均通过，E 类真冲突当前为 0。允许进入受控发布；本轮不生成、不安装、不锁定 `Showrunner SKILL.md`。
