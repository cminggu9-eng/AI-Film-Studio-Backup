# Showrunner Capability Model V0.1 — Architecture Research

> 研究用途：为 `AI Film Studio SHOWRUNNER CAPABILITY MODEL V0.1` 提供架构草案。本文不是最终 `Showrunner SKILL.md`，不写入正式 Vault，也不重新蒸馏五位创作者。
>
> 归因边界：下文的能力接口来自六份已批准正式档案；输入模式、状态标签、八层决策堆栈、停止门、数据类型和下游交接协议，是 `AI FILM STUDIO SYNTHESIS`，不是任何单一创作者的原生术语或固定流程。

## 研究输入与方法边界

本次架构只使用以下六份已批准正式档案：

| 代号 | 输入档案 | 状态 | 本次架构可借用的能力接口 |
|---|---|---|---|
| CM | `02_DISTILLATION/编剧研究/Craig Mazin｜Showrunner能力蒸馏 V0.1.md` | approved / passed | central dramatic argument、人物旧逻辑、选择与行动证明、有限季总论断/单集论断、反模板返工 |
| VG | `02_DISTILLATION/编剧研究/Vince Gilligan｜Showrunner能力蒸馏 V0.1.md` | approved / passed | Character Consequence Engine、Choice→Consequence→Next Cause、story breaking、责任链、条件性升级 |
| SR | `02_DISTILLATION/编剧研究/Shonda Rhimes｜Showrunner能力蒸馏 V0.1.md` | approved / passed | Premise/Series Engine、EP02 门、状态续航、关系/职责供给、Continuing Drive、room 诊断 |
| TG | `02_DISTILLATION/编剧研究/Tony Gilroy｜Showrunner能力蒸馏 V0.1.md` | approved / passed | Destination Awareness、Entry→Event→Exit、Reality Check、复杂信息、模块交接、Production Reality、Scope Compression |
| DS | `02_DISTILLATION/编剧研究/David Simon｜Showrunner能力蒸馏 V0.1.md` | approved / passed | Research→Drama、Institution/Incentive、World Without Protagonist、Ensemble Function、Distributed Causality、System Persistence |
| X5 | `02_DISTILLATION/方法论/Showrunner｜五人交叉蒸馏 V0.1.md` | approved / passed | 已去重的五人能力矩阵、A–E 关系、规则优先级、冲突机制、L1–L8 作为候选综合层级 |

### 女娲流程的适用方式

本轮按 `huashu-nuwa` 的主题/交叉抽象变体使用：先读取批准输入，区分来源支持、跨来源推断和 Studio 自有协议，再把可复用判断接口组合为可审计系统。这里不启动人物重新研究，不生成 Skill，不把五人档案中的工具名称误称为 Showrunner 的固定算法。

标签约定：

- `SOURCE-DERIVED`：可回查至单人正式档案中的窄范围能力接口。
- `CROSS-DERIVED`：五人交叉档案已经完成去重后保留下来的组合判断。
- `AI FILM STUDIO SYNTHESIS`：本模型为输入管理、层级、状态、门和交接设计的自有协议。

## 一、INPUT STATE ASSESSMENT

### 1.1 目的

Showrunner 不把任何输入直接当成“可写剧本”。第一步是确认：当前用户交付的是什么、哪些字段已经获得授权、哪些只是提案、哪些互相冲突，以及该输入适合调用哪一层能力。输入状态评估的输出是可追踪的事实和缺口清单，不是替用户偷偷补齐的创作决定。

### 1.2 六种输入模式

| 模式 | 典型输入 | 必查字段 | 默认可进入层级 | 缺失时的动作 |
|---|---|---|---|---|
| **MODE A — 模糊 Idea** | 一句话点子、意象、问题、人物种子 | 想让观众关注什么、自然终点的初步假设、是否已有形式偏好 | L1，必要时 L2 诊断 | 不扩写剧情；输出 `Intake State Assessment` 与澄清/候选方向。没有必要信息时 `WARNING` |
| **MODE B — Concept** | premise、人物入口、世界入口、主题问题 | Story Purpose、premise/engine 区分、形式与体量、主要欲望、终点假设 | L1–L2；按题材进入 L3 | 若只有开场事件而无后续供给，不能直接判为 Series；输出 `Format Fit Note` |
| **MODE C — Character/World** | 角色卡、关系图、世界/制度设定、研究摘要 | 欲望/误认/约束/权限、现实依赖、系统目标与回应、缺失知识 | L2–L3 | 只建立与当前故事有关的最小世界接口；不把设定百科自动转成戏剧 |
| **MODE D — Series Bible/Season Outline** | series engine、季目标、集列表、模块、角色关系、世界规则 | EP02 可发生性、季起止状态、引擎供给、模块交接、系统持久状态 | L1–L6 | 逐层验证；不因已有集列表而跳过因果和容量检查 |
| **MODE E — Episode Outline** | 单集 premise、beats、A/B/C、前后集状态、信息分配 | 本集存在理由、Entry/Exit State、选择—后果、交接压力、线的独立功能 | L2、L4、L5、必要时 L6 | 若上集状态不明，先补状态账本；不以大反转补接口 |
| **MODE F — Script Rework** | 剧本、反馈、粗剪问题、制作限制、冲突意见 | 当前版本、反馈事实、最后有效状态、最早失效层、锁定内容、返工权限 | L8 入口，回跳 L1–L7 | 先诊断后改写；锁定正史或用户授权范围冲突时 `BLOCKED` |

### 1.3 每次评估的状态字段

建议将输入评估写成以下记录；字段是 `AI FILM STUDIO SYNTHESIS`，用于避免把未知写成事实：

```yaml
input_id: <唯一标识>
mode: A|B|C|D|E|F
source_artifacts: [<文件或用户输入>]
purpose_claim: <当前能直接支持的故事目的；未知则 UNKNOWN>
format_claim: <用户提出或待判断的形式>
current_state: <人物/关系/信息/资源/责任/系统中已知状态>
authority_status: LOCKED|APPROVED|DRAFT|UNKNOWN|CONFLICTING
provenance: USER|CANON|APPROVED_ARCHIVE|INFERENCE|STUDIO_SYNTHESIS
required_unknowns: [<会改变因果、形式或制作选择的未知>]
conflicts: [<互相冲突的输入及其来源>]
next_gate: <下一层或 STOP/WARNING/BLOCKED>
```

### 1.4 五种状态标签的含义

| 标签 | 允许的动作 | 不允许的动作 |
|---|---|---|
| `LOCKED` | 读取、引用、检查后果；提出冲突报告 | 未经用户授权静默改写、重命名或覆盖 |
| `APPROVED` | 作为当前工作基线；可在返工包中提出替代方案 | 将其重新当成未审核素材或移除 provenance |
| `DRAFT` | 进行判断、补缺、重破和候选比较 | 把候选自动升级为正史/锁定决定 |
| `UNKNOWN` | 标注缺口，按需要研究、询问或降级范围 | 以常识、套路或模型臆测填入确定性事实 |
| `CONFLICTING` | 进入 Conflict Resolver；保留两端、条件与未选项 | 以平均、删除一端或静默选择伪造共识 |

状态规则：若 `LOCKED` 与任何新输入冲突，默认为 `BLOCKED`，由用户决定；若两个 `DRAFT` 冲突，可进入决策机制；若冲突只影响可选工具或非当前格式层，可标为 `WARNING`，但必须记录。

### 1.5 输入门

1. 输入来源、授权状态和 provenance 可追踪；否则停止扩写并补记录。
2. 至少能写出当前 Story Purpose 或明确标为 UNKNOWN；若连问题对象都不明，保持 MODE A。
3. 用户指定形式与故事自然终点不匹配时，不强行扩容，输出 `Format Fit Note` 并建议缩小、改形式或补建引擎。
4. L4 关键因果工作前，主要人物至少有欲望/约束/可选项；制度/专业细节在现实依赖高时需通过最低充分理解门。
5. 任何输入不应绕过锁定内容保护、用户决策权或下游范围边界。

## 二、FORMAT FIT

Format Fit 不是“把故事做成剧”的确认，而是判断故事的自然容量、状态变化颗粒度、引擎供给和制作范围是否相配。它由 `CROSS-DERIVED` 的 Premise/Engine、Continuing Drive、Destination、模块与制作接口综合而来。

| 形式 | 适配信号 | 关键检查 | 常见错误 |
|---|---|---|---|
| **短片** | 一个中心论断/关系或有限压力，终点集中且不需反复供给 | 单一目的、最小人物集合、一次或少数状态转移 | 为证明复杂世界而扩写制度和群像 |
| **短视频** | 低解释负荷、单一可见目的、短反馈回路 | 首要观看入口、即时可读的目标/阻力、结束后的状态差 | 依赖长篇背景、隐藏大量信息或复杂交接 |
| **限定剧** | 有明确阶段终点，足够多的选择/后果支撑有限集数 | 季级目标状态、EP02 门、模块交接、长期后果的必要时间窗 | 把有限故事拖成无限 engine，或锁死所有路径 |
| **连续短剧/漫剧** | 可重复情境入口 + 会变化的人物/关系/资源状态 | 每集/段落的状态差、低成本可复用接口、继续观看理由 | 固定 ABC、每段反转、用囤秘密代替变化 |
| **长篇 Series** | 多轮供给源、人物/制度/关系/系统状态可持续变化 | World/Institution 是否必要、System Persistence、Consequence Horizon、模块与制作现实 | 以人数/地点制造复杂度；无终点方向地膨胀 |

`Format Fit Note` 至少回答：

1. 初始 premise 为什么值得观看？
2. 去掉一次性开场后，什么会让人物再次选择？
3. 当前形式需要的状态变化和自然终点是什么？
4. 哪些 L3/L5/L6 能力对该形式是 `N/A by format`？
5. 若不适配，最小改动是缩小形式、补建真实供给源，还是重新定义目的？

适配结论使用 `FIT`、`FIT WITH CONDITIONS`、`NOT FIT—REDIRECT` 三值；`NOT FIT` 不是项目失败，而是防止用错误形式消耗故事。短片或轻喜剧不因没有完整制度图而失败；长篇制度故事也不因没有主角独自解决世界而失败。

## 三、八层 DECISION STACK

这是 AI Film Studio 的审计顺序，不是五位创作者的原生分类。初始开发从 L1 向下；审核与返工从最早失效层回跳。任何下层输出都不能掩盖上层未通过。

| 层级 | 能力 | 输入 | 判断问题 | 决策/输出 | 适用条件 |
|---|---|---|---|---|---|
| **L1** | Story Purpose | premise、主题问题、自然终点、观众承诺、预计形式 | 这是要证明/探索什么？形式容量承载得了吗？ | `Purpose/Format Note`、目的与形式决定 | 全部项目；未知时保持诊断，不进入大规模扩写 |
| **L2** | Character Engine | 欲望、误认/恐惧、关系位置、约束、可行选项、拒绝成本 | 人物此刻为什么能这样选？选择改变什么？ | `Character State Card`、人物引擎与选择集 | 全部有角色行动的故事；无人物中心的实验需明确替代驱动 |
| **L3** | World/System | 现实依赖、机构/环境、激励、权限、资源、研究、系统回应 | 哪些世界条件会改变选择成本？主角离场后必要边界是否继续？ | 最小 `World/Institution Map`、`Reality Check` | 仅在系统、专业现实或环境确实改变因果时启用；轻类型可 `N/A` |
| **L4** | Causal Story | 事件、选择/不作为、权限路径、回应、后果、更新状态 | 是否为 `Choice → Consequence → Updated State → Next Cause`？ | `Causal Ledger`、`Reality State Card` | 所有有因果推进的项目；随机可作起点，不能跳过回应链 |
| **L5** | Series/Episode | 上集状态、引擎供给、EP02、单集问题、季目标、A/B/C 候选 | 为什么是下一集/这一集？是否改变状态而非囤牌？ | `Engine Map`、`Episode State Map`、主线/支线决定 | 连续形式才必需；短片/单段项目标 `N/A by format` |
| **L6** | Longform Planning | 目标状态、阶段问题、模块、交接压力、可变路径、时间窗 | 方向是否清楚而中间路径可重破？模块是否有出口与遗留债务？ | `Destination Card`、`Season/Module Map`、handoff | 限定剧/长篇/阶段性项目；短内容可 `N/A` |
| **L7** | Production Reality | 创意意图、必要戏剧功能、成本驱动、角色/地点/群演/动作、替代执行、新风险 | 能否保留功能后重设计，而不是因成本/AI能力直接删除？ | `Production Reality Check`、`Alternate Execution`、`Scope Decision` | 有明确生产约束时启用；不能反向决定故事目的 |
| **L8** | Diagnosis & Rewrite | 草稿、反馈、状态账本、冲突、制作输入、已通过层 | 最早哪一层失效？最后有效状态在哪里？ | `Diagnostic Report`、`Rewrite Packet`、复审门 | 所有项目可用；不是更大反转或加规模的补丁层 |

### 3.1 堆栈的运行原则

- **向下展开**：只有上一层的问题已达到当前门槛，才建立下一层的工件。
- **条件跳过**：`N/A by format` 必须说明理由；跳过不是把未验证问题当通过。
- **向上回跳**：L4 发现 premise 无法支撑因果时回 L1；L5 发现无续航时回 L1/L2；L7 发现压缩抹掉功能时回 L1–L4；L8 只回到最早失效层。
- **层级证据**：每个判断记录 `SOURCE-DERIVED`、`CROSS-DERIVED` 或 `AI FILM STUDIO SYNTHESIS`，并保留输入状态。

## 四、CONFLICT RESOLVER

冲突处理不是把两端平均，而是把条件显式化：

```text
CONTEXT
  → COMPETING PRINCIPLES
  → QUESTION
  → OPTION A / OPTION B（必要时 OPTION C = 改形式或暂停）
  → TRADEOFF
  → DECISION CONDITION
  → DECISION
  → OUTPUT
  → REVIEW
```

最小记录字段：

| 字段 | 要记录的内容 |
|---|---|
| `CONTEXT` | 项目形式、当前层级、阶段、已锁状态、制作边界、事实缺口 |
| `COMPETING PRINCIPLES` | 例如“续航供给”与“自然终点”、“方向”与“路径开放” |
| `QUESTION` | 一个可观察、可决策的问题，不写抽象口号 |
| `OPTION A/B` | 两条能实际执行的路径及保留的创意功能 |
| `TRADEOFF` | 主题、人物、因果、信息、形式、生产和长期维护代价 |
| `DECISION CONDITION` | 删除开场后是否仍有回路、压缩是否丢失不可替代功能等可验证门槛 |
| `DECISION` | 当前选项、责任人/授权人、未选项为何保留 |
| `OUTPUT` | 要创建或更新的模型数据类型 |
| `REVIEW` | 哪些新证据/反馈会触发重审、何时复查 |

## 五、CORE WORKFLOW 与回环

### 5.1 主流程

```text
INTAKE
  → INPUT STATE ASSESSMENT
  → PURPOSE / FORMAT FIT
  → CHARACTER ENGINE
  → (CONDITIONAL) WORLD / SYSTEM
  → CAUSAL STORY
  → (CONDITIONAL) SERIES / EPISODE
  → (CONDITIONAL) LONGFORM
  → PRODUCTION REALITY
  → DIAGNOSIS / REVIEW
  → HANDOFF 或 REWRITE LOOP
```

每一阶段都必须具备：

`INPUT → ASSESSMENT → DECISION → OUTPUT → VALIDATION → HANDOFF`

### 5.2 核心状态回路

主链的最小可执行形式是：

```text
当前人物/关系/信息/资源/责任/系统状态
  → 可行选择与不作为
  → 现实回应与后果
  → 更新状态与下一步约束
  → 下一问题/选择
```

场景级可写为 `Entry State → Event/Choice → Exit State`；人物级为 `Choice → Consequence → Next Cause`；制度性长篇才继续接 `Distributed Causality → System State → Consequence Horizon`。不是每个场景都必须成长、升级或产生大转折；观察、准备、修复、等待、兑现与收束只要改变可追踪接口或完成必要功能即可。

### 5.3 返工回环

1. 收集草稿、研究、表演/剪辑反馈和制作事实，不直接照抄反馈方案。
2. 找出最早失效层：目的/格式、人物选择、现实路径、因果状态、续航、长篇方向、生产功能，或仅是表达执行。
3. 回到该层最后有效的状态账本；保留已通过层和不可静默修改的锁定内容。
4. 通过 Conflict Resolver 比较修正方案，写出代价与未选方案。
5. 生成 `Rewrite Packet`，重新验证受影响的下层和下游交接。

## 六、STOP / WARNING / BLOCKED 条件

### `STOP`：正常停机，不等于失败

- 当前用户授权的模型/诊断/交接已完成；下游任务（Scene Writer、Director、剧本开发或 Skill 锁定）未获明确授权。
- 项目达到自然终点或当前格式容量，继续扩写只会换皮、囤秘密或拖延。
- 所有适用层通过，剩余层明确 `N/A by format`，可交付当前 Handoff。
- 返工已达到用户要求的版本范围，继续改动会越权修改正史或生产决定。

`STOP` 后保存状态、输出和未决事项；不得自动开始下一位创作者、下游 Skill 或正式剧本。

### `WARNING`：可继续，但必须标记

- 可选工具未建立，但当前判断仍可由基本状态/因果记录复核。
- 非关键字段 `UNKNOWN`，不会改变当前层决定；设置补证或复查点。
- L3/L5/L6 对当前短内容或轻类型为 `N/A by format`。
- 路径存在多个可行方案，尚未需要用户最终裁决；保留条件和未选项。
- 随机扰动、戏剧压缩、明确恶意或延迟后果被启用，但已记录现实路径、人物回应和新风险。

### `BLOCKED`：不得继续扩写或发布

- `LOCKED` 正史与新输入发生未授权冲突。
- 必需的故事目的/形式、关键人物选择接口、现实依赖或核心因果链未知/互相矛盾，且不能安全降级范围。
- 主链无法形成选择/不作为→后果→更新状态→下一选择；或只靠随机事故、囤秘密、反转、死亡或编剧强行推动。
- 计划做连续剧/长篇但删掉一次性开场后没有可再生引擎，且用户未同意改形式或补建引擎。
- 研究依赖高但没有最低充分理解；把未知专业机制写成确定性事实。
- 生产压缩删除 Essential Dramatic Function，或只以“AI 做不到/成本太高”为删除理由而没有替代执行。
- 关键人物/支线/系统功能被删除但未记录不可逆的因果、权力、关系或信息损失。
- provenance 丢失、综合规则被误归因给单人档案，或发布前 frontmatter/审核状态不合规。
- 请求越过 Showrunner 边界输出最终对白、表演、机位、摄影、视觉设计或修改用户最终决策。

## 七、输出数据类型

以下数据类型是模型的接口，不是要求每个项目全部生成。每个工件应带 `project_id`、`mode`、`authority_status`、`provenance`、`source_refs`、`open_questions`、`review_state`。

| 类型 | 作用 | 最小字段 |
|---|---|---|
| `Intake State Assessment` | 识别输入模式与状态 | mode、artifact、authority、unknowns、conflicts、next gate |
| `Purpose/Format Note` | 判断故事目的与形式容量 | premise、central question、natural endpoint、format、fit、reason |
| `Character State Card` | 记录人物当前状态与选择接口 | desire、misbelief/fear、relationship position、constraints、options、refusal cost |
| `Engine Map` | 记录可再生供给源 | trigger、person/role、pressure、choice、state change、exhaustion risk |
| `World/Institution Map` | 记录最小必要世界/制度回应 | formal goal、actual incentive、authority、resources、rules、response、persistence |
| `Reality State Card` | 验证场景或行为入口/出口 | knowledge、desire、permission、time、space、risk、event/choice、exit state |
| `Causal Ledger` | 追踪主链因果 | state、choice/non-choice、response、consequence、beneficiary/cost bearer、next cause |
| `State Ledger` | 跨场景/集/阶段保存变化 | character、relationship、information、resource、responsibility、system state、unresolved pressure |
| `Episode State Map` | 判断单集为何存在 | prior state、episode question、line functions、choice、new state、handoff |
| `Season/Module Map` | 保存阶段方向与开放路径 | destination state、necessary conditions、module purpose、exit、debt、alternate path |
| `Destination Card` | 防止长篇无方向或路径锁死 | target state、causal conditions、open paths、review triggers |
| `Information Map` | 管理复杂信息和观众任务 | holder、access path、current goal、delay reason、payoff、risk of confusion |
| `Ensemble Function Audit` | 评估人物/位置是否不可替代 | system position、information、variable changed、relationship/ethics function、merge loss |
| `Production Reality Check` | 找到成本驱动与戏剧功能 | creative intent、essential function、cost driver、must preserve、can redesign、new risks |
| `Alternate Execution / Scope Decision` | 记录压缩后的执行方案 | original function、compressed shell、preserved relation/causality、tradeoff、approval |
| `Diagnostic Report` | 定位最早失效层 | symptom、root layer、evidence、severity、not-a-fix、recommended gate |
| `Rewrite Packet` | 供 room 定向返工 | last valid state、problem、options、tradeoffs、chosen condition、affected outputs、retest |

## 八、DOWNSTREAM HANDOFF（五类）

Showrunner 的交接是故事系统和判断接口交接，不是替下游写最终表现层。每类 handoff 都要包含 provenance、状态、授权、未决事项和验收门。

| 交接类型 | 接收方 | 必交付内容 | 明确不交付 |
|---|---|---|---|
| **H1 Concept/Format Handoff** | 项目开发/用户决策 | Purpose/Format Note、premise/engine 区分、自然终点、形式结论、未决选择 | 不把未批准概念写成正史，不扩写成剧本 |
| **H2 Character–World Handoff** | Story Breaking / 编剧 room | Character State Cards、最小 World/Institution Map、关系与权限、现实依赖、研究缺口 | 不替人物决定台词，不把制度图变成完整百科 |
| **H3 Causal–Series Handoff** | Season/Episode Outline 或 Scene Writer | Causal Ledger、Engine/State Map、Destination/Module Handoff、信息交接、continuing drive 条件 | 不规定每场反转/成长/升级，不输出镜头、机位或视觉设计 |
| **H4 Production Reality Handoff** | 制作规划/导演协作接口 | Creative Intent、Essential Dramatic Function、Cost Driver、Alternate Execution、New Risks、Scope Decision | 不以成本直接改主题/人物，不越权下最终表演、摄影或美术命令 |
| **H5 Diagnosis/Recovery Handoff** | Room 重破、审稿、用户最终决策 | Diagnostic Report、最后有效状态、Conflict Resolver 记录、Rewrite Packet、复测结果、锁定项冲突 | 不静默覆盖 locked canon，不把反馈方案当事实或最终决定 |

交接验收：接收方应能回答“当前状态是什么、下一问题是什么、谁能做什么、哪些条件不能改变、什么反馈会触发回环”。无法回答时退回 L8，而不是用强刺激掩盖缺口。

## 九、架构级边界与待验证事项

- 八层层级、六种输入模式、状态枚举、数据类型和五类 Handoff 是 Studio 自有架构，需要在后续原创压力测试中验证，不归因给五位创作者。
- `L3 World/System`、`L5 Series/Episode`、`L6 Longform` 不是所有形式的必选层；不适用必须标记并说明，而不是当作失败。
- `LOCKED` 的正式 Vault 内容优先于未授权新输入；当前研究文件只能读取正式档案，不改变其状态。
- 本架构没有生成最终 `Showrunner SKILL.md`，没有输出场景对白、表演指令、机位、摄影、视觉设计，也没有启动 Scene Writer、Director 或正式剧本开发。
- 下一步复核重点：用任务书的三个原创项目和六条错误指令测试每个模式、格式门、L1–L8 回环、Stop/Warning/Blocked 和 Handoff 是否能在轻类型与系统型故事之间切换。

## Provenance 回查索引

| 架构接口 | 主要档案 | 辅助档案 | 归因边界 |
|---|---|---|---|
| Story Purpose / Theme / Character Change | CM | SR、VG、DS | 主题/人物接口来自 CM；综合层级和状态协议为 CROSS/Studio |
| Choice / Consequence / Causal Chain | VG | CM、TG、DS | VG 提供人物后果链；场景/制度层连接为 CROSS |
| Series / Episode / Continuing Drive | SR | VG、TG | SR 提供格式续航；不是固定集数、ABC 或 cliffhanger 公式 |
| Destination / Scene State / Reality / Production | TG | SR、DS | TG 提供现实接口与替代执行方向；Scope 字段和门为 Studio |
| Research / Institution / Ensemble / Persistence | DS | TG、VG | DS 提供系统层能力；不强迫完整社会模拟或“无反派” |
| 八层、Input State、Conflict Resolver、Stop/Block、输出/交接 | X5 | CM、VG、SR、TG、DS | 由五人交叉结果再经 AI Film Studio 架构化，不能归因单人 |

**研究结论：** 六份已批准档案足以支持一个分层、条件启用、可回环的 Showrunner 架构候选。它的核心不是“每层都做满”，而是用输入状态和形式适配决定启用哪些层，用因果/状态账本保证判断可追踪，用冲突与 Stop/Block 门保护用户决策和创意功能，再以五类 Handoff 把系统交给下游。
