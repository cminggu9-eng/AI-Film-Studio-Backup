# Showrunner 综合能力模型 V0.1｜规则、条件性张力与 Provenance

> 本文件是 `Showrunner_Capability_Model_V0.1` 的研究工作文件，不是正式 Vault 内容，也不是 `Showrunner SKILL.md`。本轮按 `huashu-nuwa` 的主题 Skill 变体执行：以已批准档案为输入，做跨档案提炼，保留直接来源、跨档案推断与 AI Film Studio 自有规则的边界。

## 1. 输入与方法边界

### 1.1 六份输入档案

| 代号 | 正式档案 | 状态 | 本轮用途 |
|---|---|---|---|
| CM | `02_DISTILLATION/编剧研究/Craig Mazin｜Showrunner能力蒸馏 V0.1.md` | `approved / passed` | 主题论断、人物误认、选择与行动证明；仅保留方法层 |
| VG | `02_DISTILLATION/编剧研究/Vince Gilligan｜Showrunner能力蒸馏 V0.1.md` | `approved / passed` | Choice→Consequence、升级条件、story breaking |
| SR | `02_DISTILLATION/编剧研究/Shonda Rhimes｜Showrunner能力蒸馏 V0.1.md` | `approved / passed` | Series/Season/Continuing Drive、形式容量、room 复盘 |
| TG | `02_DISTILLATION/编剧研究/Tony Gilroy｜Showrunner能力蒸馏 V0.1.md` | `approved / passed` | Destination、Scene/Reality、复杂信息、模块、制作现实 |
| DS | `02_DISTILLATION/编剧研究/David Simon｜Showrunner能力蒸馏 V0.1.md` | `approved / passed` | Research→Drama、Institution/Incentive、分布式因果、系统持续 |
| X | `02_DISTILLATION/方法论/Showrunner｜五人交叉蒸馏 V0.1.md` | `approved / passed` | 交叉档案是本阶段综合主输入；前五份只做来源追踪与边界回查 |

核心纪律：X 档案中的交叉结论、A–E 分类、L1–L8 层级、冲突协议、13 条 Studio 规则，均不得回写成 CM/VG/SR/TG/DS 的单人观点。若某规则来自 X，只标 `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；若是本 Studio 为管线增加的门、字段或优先级，标 `AI FILM STUDIO SYNTHESIS`。

### 1.2 证据标签

- `SOURCE-SUPPORTED`：单人档案可由其最终核心证据直接支持的窄主张。
- `SYNTHESIZED INFERENCE｜PERSON`：单人档案内部跨来源归纳，仍属于该档案的能力边界。
- `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`：至少两份已批准档案之间的交叉抽象；不是任何单人的原话、固定术语或普遍法则。
- `AI FILM STUDIO SYNTHESIS`：为本 Studio 的输入、判断、决策、输出、审核或生产安全而建立的规则；不归因给任何创作者。

## 2. 规则优先级（四分类）

四类不是“重要性排行榜”，而是运行时的约束强度。越靠前越少、越具体；条件不满足时，条件方法与工具不得越权覆盖硬约束。下列规则均为本阶段候选规则，待主模型与原创测试复核。

### 2.1 HARD CONSTRAINT｜少量硬约束（5 条）

硬约束只保留可跨形式或在明确适用边界内不可跳过的安全/因果门；不把每场成长、每集反转、现实主义、群像或低成本写成硬约束。

| ID | 规则 | 适用边界 | Provenance / 依据 | 违反时输出 |
|---|---|---|---|---|
| HC-01 | 关键主链必须能解释 `选择/不作为 → 后果 → 更新状态 → 下一选择/原因`。若箭头无法由人物、关系、资源、信息、权限或系统状态解释，标记链断裂。 | 关键剧情链；纯定位、观察、修复、兑现、收束段可不产生新选择，但须有功能与后续影响说明。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；CM M4/M6、VG 选择—后果链、DS 分布式因果、TG 场景出口 | `BLOCKED｜Causal Chain Broken`，返回最后有效状态，不用更大反转遮盖。 |
| HC-02 | 关键行为不得以“编剧想让它发生”替代可解释的欲望、信息、权限/资源、时间/空间与现实回应；随机扰动可作为起点或条件，但其后主要推进必须由人物回应和后果承载。 | 有因果承载作用的行为/场景；不是纪录片式禁绝巧合，也不要求每个动作都完整研究。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；CM 真实选项、VG 意外责任链、TG Reality Gate、DS Incentive Chain | `BLOCKED｜Reality/Agency Path Missing`，补权限路径、组织回应或人物选项。 |
| HC-03 | 长篇或制度性项目中，会改变选择成本的状态不得无解释重置；若状态清除、撤销、遗忘、替换、修复或重建，必须给出中介过程。 | 只在长篇/制度性/跨阶段项目启用；轻类型、单场景不因格式不需要而阻塞。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；DS System State/Institutional Memory、VG 持续后果、SR 状态差、TG 模块交接 | `BLOCKED｜State Persistence Missing`，更新 System/Relationship/Consequence State。 |
| HC-04 | 证据层级、跨档案推断与 Studio 自有规则必须保留 provenance；不得把 X 的综合规则改写为某位创作者的原生观点，更不得以作品表层、人格或题材替代方法证据。 | 所有模型规则、模板字段、诊断结论、审稿报告与发布档案。 | `AI FILM STUDIO SYNTHESIS`；五份单人档案及 X 的证据边界共同支持 | `BLOCKED｜Attribution/Boundary Failure`，回写标签和来源映射。 |
| HC-05 | 高成本创意不得只因成本、AI 能力或制作困难被删除；必须先经过 `Creative Intent → Essential Dramatic Function → Production Cost Driver → Alternative Execution → Scope Decision`。 | 出现明显制作成本、角色/地点/群演/动作/特效或跨度压力时启用；无高成本压力不制造流程负担。 | `AI FILM STUDIO SYNTHESIS`；源头接口来自 TG Production Reality，但该顺序与字段是 X/Studio 新规则，不归因 TG | `BLOCKED｜Unjustified Deletion`，补功能分析、替代执行与新风险。 |

硬约束总数：5。HC-03、HC-05 有明确适用边界；不能把它们升级成所有项目的绝对要求。

### 2.2 DEFAULT HEURISTIC｜默认启发式（7 条）

默认启发式是通常先尝试的低风险工作方向，可被格式、题材、用户已锁状态或新证据改写；它们不是每场/每集配额。

| ID | 规则 | 默认动作 | Provenance |
|---|---|---|---|
| DH-01 | `State before Event`：先更新人物、关系、信息、资源、责任、权限和系统状态，再问下一步会自然发生什么。 | 在 room/Showrunner 审查中先填写状态差，再提出事件候选；不先指定“需要反转”。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；CM、VG、SR、TG、DS 的状态接口去重 |
| DH-02 | 让结构从 premise、欲望、论断、压力、选择和后果生成，不从页码、固定 beat 或完成品模板倒灌。 | 先做 Purpose/Character/Causal 检查，再使用节拍或模块作为审计载体。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；CM M1/M2/M4、VG story-breaking、SR premise/engine |
| DH-03 | 用目标、行动、权限与后果承载复杂信息，再决定哪些解释或留白值得保留。 | 给信息标持有者、获取路径、当前任务和兑现回报；删除不改变选择的百科负荷。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；TG Complexity Pass、DS Research→Drama |
| DH-04 | 把后果按立即、短期、长期、潜伏分层；责任必须可追，但不要求下一场立即报应。 | 每个重大决定标注时间窗与中介机制，避免结果被重置或机械即时化。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；VG 责任链、DS Consequence Horizon |
| DH-05 | room 先暴露候选、异议与证据，再形成能被知情作者接手的输出。 | beat/模块写行动者、目的、前因、选择/功能、后果/完成状态和下步条件；不规定卡片形状、人数或天数。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；VG、SR、TG、DS 的 room 资料 |
| DH-06 | 升级是条件判断，不是强度配额。只有代价、退路、关系/资源、价值冲突或系统压力显著改变时才标“升级”。 | 允许兑现、观察、准备、修复、消化、等待、横向发展、阶段收束；记录它们的戏剧功能。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；VG、SR、TG、DS |
| DH-07 | 诊断先于强化：先定位最早失效层，再选择修正；不以死亡、反转、更多地点、更多人物或更大规模掩盖根因。 | 输出 `ROOT CAUSE → AFFECTED LEVEL → REPAIR OPTIONS → TRADEOFF → RECHECK`。 | `AI FILM STUDIO SYNTHESIS`；X 的审核/返工接口，不归因单人 |

### 2.3 CONDITIONAL METHOD｜条件适用方法（7 条）

条件方法必须先通过 `适用门`；不满足时输出 `N/A BY FORMAT` 或建议换形式，不视为能力缺失。

| ID | 方法 | 适用门 | 不适用时 | Provenance |
|---|---|---|---|---|
| CM-01 | Series/Continuing Engine：从欲望、关系、职责、资源、信息或压力状态产生可解释的下一集输入。 | 删除一次性开场后，仍有可再生的选择—状态回路；项目确实需要多集/连续格式。 | 缩小为短片、电影、限定剧或重建 engine；不为集数扩容。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；SR 主责、VG/DS/TG 辅助 |
| CM-02 | Season/Endpoint：锁目标状态、阶段目的与必要因果条件，保持中间路径可变。 | 需要季弧/长篇方向，且存在可验证终点或阶段状态；外部输入仍可能改变可信路径。 | 不强行预锁完整事件表；改为较短形式或以当前阶段目的工作。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；TG/CM 与 VG/SR 的条件接口 |
| CM-03 | Institution/Ensemble/World-without-Protagonist：建立最小制度、激励、多方与系统持续图。 | 机构/多方会改变人物选择、信息、权限、资源或长期后果，并且多人物有独立功能。 | 亲密主观、轻喜剧或单地点项目只建必要接口；不做完整社会模拟。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；DS 主责，TG/SR/VG 辅助 |
| CM-04 | Scene/Reality/Complexity Gate：用 Entry State→Event/Choice→Exit State 和信息路径检查现实回应。 | 场景或行为承担因果、权限、信息或组织回应；有现实依赖。 | 仅展示性/风格性段落可标注功能，不强行增加大变化；不把现实变成纪录片禁令。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；TG 主责、VG/CM/DS 接口 |
| CM-05 | Modular Longform：按局部问题、状态出口、遗留压力和交接物拆 block/chapter/phase。 | 长篇、多人协作或制作需要模块交接，且每个模块有真实局部功能。 | 不使用固定“三集一块”或同构模块；保持更自然的段落尺度。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；TG 主责，SR/DS 辅助 |
| CM-06 | Scope Compression：压缩角色、地点、移动、时间跨度或群演的外壳，保留不可替代的关系、因果、危险、系统摩擦与世界尺度功能。 | 已完成 HC-05 的创意功能和替代执行评估，压缩后核心功能仍可验证。 | 回退方案、分期或改变项目范围；不以低成本自动优先。 | `AI FILM STUDIO SYNTHESIS`；TG 提供窄方法输入，X/Studio 命名与顺序 |
| CM-07 | Research-to-Drama：把研究事实转成压力、位置、选项、选择与后果。 | 陌生职业/制度/历史机制会改变故事核心因果，且研究可改变人物目标、权限、风险或选择。 | 资料留在研究账本、标未知或删除；不让角色朗读百科。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；DS 主责、TG 信息载体 |

### 2.4 OPTIONAL TOOL｜可选工具（10 项）

工具是外接记忆与审计载体，不是价值本身；除非某项目进入对应条件门，否则不要求全套建立。

| ID | 工具 | 主要用途 | Provenance |
|---|---|---|---|
| OT-01 | `Purpose / Format Note` | 区分一次性 premise、有限故事与可续 engine，记录主题论断和自然终点。 | `AI FILM STUDIO SYNTHESIS`，由 X 层级化 |
| OT-02 | `Character State Card` | 记录欲望、误认/恐惧、关系位置、资源、可选项与拒绝成本。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；CM/VG |
| OT-03 | `State Ledger` | 逐场/逐集/逐阶段记录变化状态，避免无痕重置。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；CM/VG/SR/TG/DS 去重 |
| OT-04 | `Causal Ledger` | 记录 Choice→Consequence→Updated State→Next Cause 与责任节点。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；VG/CM/DS |
| OT-05 | `Engine Map` | 映射重复情境入口、供给源、触发人物、可选项、后果与耗竭风险。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；SR/VG |
| OT-06 | `Destination Card` | 记录目标状态、必要因果条件、可变路径与新证据触发的改道。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；TG/CM |
| OT-07 | `Reality / Institution Map` | 分别记录场景权限/空间/时间/回应与机构目标/指标/层级/奖惩。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；TG/DS；不得合并为“写实主义表” |
| OT-08 | `Consequence Horizon` | 标示立即、短期、长期、潜伏后果及中介机制。 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION`；DS/VG |
| OT-09 | `Ensemble Function Audit` | 审计人物独立系统位置、信息、权力、关系或因果功能；合并前记录损失。 | `AI FILM STUDIO SYNTHESIS`；DS/SR 提供能力输入 |
| OT-10 | `Alternate Execution / Room Challenge Pass` | 记录高成本替代方案、新风险，或由 room 反驳“囤牌/凑线/拖集数”。 | `AI FILM STUDIO SYNTHESIS`；TG/CM/VG/SR/DS 输入，工具不归因单人 |

## 3. 四个正式 Conditional Tensions → CONFLICT RESOLVER

### 3.1 CT-01｜Series Engine 的续航 vs 自然终点

来源矩阵：`X` 的 D 类 `Season Engine`/`Continuing Drive`；SR 主责，VG/DS 提供后果与状态供给，TG 提供阶段方向，CM 提供有限季的总论断/单集问题。此处的交叉规则不能写成“Shonda 认为电视必须持续”或“Vince 认为每集必须后果升级”。

**CONTEXT**：项目已出现 pilot/第一单元；团队在“为了连续格式增加供给”与“承认故事自然终点”之间做形式/季弧决策。当前必须记录格式、预计体量、删除开场后的引擎、已改变状态、目标终点与制作承诺。

**COMPETING PRINCIPLES**：

- 原则 A：若续航来自人物、关系、职责、资源、信息或压力变化，Series Engine 可支持多集；下一集应从上一集改变后的状态出发（SR/VG 交叉推断）。
- 原则 B：若一次性触发事件删除后没有可再生的选择回路，扩容会造成拖延、假 cliffhanger 和人物失智；应选择有限形式或重建引擎（SR/CM/TG 交叉推断）。

**QUESTION**：当前构想是否真的需要连续形式，以及在 pilot 之后谁在什么约束下仍会被迫做可解释的新选择？

**OPTION A**：保留/开发 Series Engine；配对可重复情境入口与可变化人物/关系/责任/资源状态，写出 Why EP02、阶段终点和耗竭信号。

**OPTION B**：缩小格式（短片/电影/限定剧）或重建 engine；保留已成立的主题与人物压力，不为填满集数囤积秘密、扩大事故或延后结算。

**TRADEOFF**：A 保留多集的关系复利、复杂系统和观众持续承诺，但增加状态账本、模块交接和耗竭诊断成本；B 减少拖延与制作负担，但可能放弃多阶段关系、长期后果或系统层素材。

**DECISION CONDITION**：通过 `删掉一次性开场事件 → 列出至少一个人物/关系/职责/系统压力回路 → 写出下一步状态变化` 测试；若不存在可再生回路，B 为默认决策。若存在回路但只靠外来事件/扣牌延长，先修 Engine Map，不直接扩集。

**DECISION / OUTPUT**：生成 `Purpose/Format Note`、`Engine Map`、`Why EP02` 或 `Format Change Note`；保留未选方案和触发重审条件。

**REVIEW**：当表演、新研究、用户锁定形式或制作约束改变“可续性/自然终点”时，回到该 resolver；不以“已经订了集数”覆盖诊断。

### 3.2 CT-02｜Destination Awareness 的方向 vs 路径开放

来源矩阵：`X` 的 D 类 `Destination Awareness`；TG/CM 提供阶段目标、终点条件和行动证明，VG/SR 提供人物状态对路径的重破与季级重发明。目标状态、因果条件与中间事件必须分层；不能将此张力伪写为 TG “预先锁死”，也不能伪写为 VG/SR “拒绝规划”。

**CONTEXT**：项目进入季弧、长篇或模块拆解，需要足够方向让 room 筛选材料，同时可能出现更符合人物/现实的新路径。

**COMPETING PRINCIPLES**：

- 原则 A：先写可验证的阶段终点、必须成立的因果条件和终局行动；没有方向时模块会膨胀、事件无法筛选（TG/CM 交叉推断）。
- 原则 B：只锁目标状态与必要条件，不锁死所有中间事件；若新证据、表演或人物选择改变可信路径，必须允许重破（VG/SR/TG 共同边界）。

**QUESTION**：当前锁定的是“要抵达的状态/证明条件”，还是已经把所有过程节点写成不可修改的事件表？

**OPTION A**：锁目标状态、不可违背因果条件与终局证明门；允许中间路径 A/B/C，通过每个模块是否更接近目标状态来筛选。

**OPTION B**：暂不锁完整终点路径；当外部输入、用户决策或人物逻辑尚未稳定时，先做局部状态/现实检查，必要时调整格式或暂停扩写。

**TRADEOFF**：A 给予 room 方向、制作前置与结局证据，但若过度具体会把人物扭成终点工具；B 保留发现与真实性，但若没有阶段目的会累积无方向模块、研究和未决债务。

**DECISION CONDITION**：必须能写出“目标状态 + 至少一项必要因果条件 + 终局行动证明”；同时必须列出至少一条可变中间路径和何种新输入可合法改道。缺目标/条件则暂停长篇扩写；目标存在但路径被锁死则重破，而不是放弃方向。

**DECISION / OUTPUT**：生成 `Destination Card`、`Module Map`、`Path Alternatives` 和“允许改道条件”；未选路径保留在决策记录中。

**REVIEW**：若新的研究、排练、平台格式或用户锁定状态改变可行路径，检查终点条件是否仍有效，再选择保留目标、改目标或改形式。

### 3.3 CT-03｜Production Reality vs Story Quality / Creative Intent

来源矩阵：`X` 的 D 类 `Production Reality`；TG 的 Production Reality Check 是窄范围能力输入；`Creative Intent → Essential Dramatic Function → Production Cost Driver → Alternative Execution → Scope Decision` 是 `AI FILM STUDIO SYNTHESIS`，不能归因给 TG 或任何单人。

**CONTEXT**：项目遇到角色数、地点数、群演、车辆、动作、特效、跨度、调度或预算压力；团队倾向“太贵/AI 做不到，直接删掉”。

**COMPETING PRINCIPLES**：

- 原则 A：先保护创意意图与必要戏剧功能（主题、关系、人物选择、因果、危险、制度摩擦、世界尺度感），再重设计执行（X/Studio 规则）。
- 原则 B：生产现实会改变可行的空间、时间、角色配置和执行方式；不识别成本驱动会造成不可交付、返工或信息混乱（TG 窄范围 + Studio 规则）。

**QUESTION**：当前昂贵元素本身是不可替代的戏剧功能，还是仅一种可以替换的执行外壳？

**OPTION A**：保留原执行，只有在成本驱动已可承受、连戏/协作/交付风险可接受时通过。

**OPTION B**：保留 Essential Dramatic Function，重设计执行：合并角色/地点、缩小视角、复用空间、压缩时间跨度、改为文件/权限链/受控背景或分期呈现，并记录新风险。

**TRADEOFF**：A 最大程度保持规模、节奏和原始形式，但可能超出生产能力并损害后续交付；B 提高可拍性与稳定性，但若压缩错误会抹掉不可替代的关系、权力、因果、危险或世界感。

**DECISION CONDITION**：没有同时填写 `Creative Intent / Essential Dramatic Function / Cost Driver / Alternate Execution / New Risks` 不得删除。只有至少一项替代执行保留功能，且新风险可接受或有缓解方案时，B 才通过；否则回到重设计、改范围或暂缓，不做静默删减。

**DECISION / OUTPUT**：生成 `Production Reality Note`、`Alternate Execution`、`Scope Decision`、`Risk Register`；保留被拒绝方案及其功能损失。

**REVIEW**：脚本、排练、粗剪、技术限制或用户创意意图更新后复查；发现压缩让因果/人物/世界功能消失，退回方案而不是继续加大反转补偿。

### 3.4 CT-04｜Scope Compression vs 功能完整性

来源矩阵：`X` 的 D 类 `Scope Compression`；TG 提供限制驱动替代解法与模块/制作边界，DS 提供系统位置/多方功能损失审计，SR 提供关系/continuing drive，CM/VG 提供人物选择和后果。Scope Compression 的名称、顺序和审计字段属于 Studio，不是 TG 的固定公式。

**CONTEXT**：初稿拥有过多角色、地点、机构、移动或时间跨度，压缩会带来角色合并、空间复用、时间压缩或视角收束；项目仍需保留核心戏剧。

**COMPETING PRINCIPLES**：

- 原则 A：按功能压缩外壳，保留不可替代的主题论断、人物选择/后果、关系位置、权力差、系统摩擦、调查压力、危险升级和世界尺度功能（Studio/X）。
- 原则 B：多方、群像、复杂制度和长时间跨度只有在提供独立利益、信息、资源、关系或因果功能时才有必要；重复位置可合并，但合并损失必须显式记录（DS/SR/TG 交叉推断）。

**QUESTION**：需要保留的是这个角色/地点/场面本身，还是它承担的不可替代戏剧功能？压缩后谁还能承载该功能，后果链是否仍可追踪？

**OPTION A**：保留原规模；仅在每个角色/地点/机构确有独立功能且制作风险可承担时采用。

**OPTION B**：按功能合并/复用/收束：列出被压缩元素、保留功能、转移承载者、合并损失和新风险；若功能无法转移，恢复必要元素或改变项目范围。

**TRADEOFF**：A 保留多方错位、世界尺度和信息纹理，但可能稀释主链、提高制作与观众负荷；B 提高可追踪性与交付性，但若只按“人数/地点少”优化，会删除因果节点、权力差或系统回应，导致故事失真。

**DECISION CONDITION**：执行 `Ensemble Function Audit + Causal Ledger + Production Note`；每个被合并元素必须回答“谁接替其系统/信息/关系/因果功能、哪项差异被损失、损失是否可接受”。若核心功能无法转移，禁止压缩；若功能可转移且新风险受控，B 通过。

**DECISION / OUTPUT**：生成 `Compression Map`、`Function Loss Register`、`Alternate Execution` 和 `New Risk`；保留原规模候选以便新输入触发恢复。

**REVIEW**：若后续测试显示压缩后的信息密度、空间重复、因果责任或系统持续性不足，恢复被合并位置、拆分模块或改写执行，不用随机死亡清理角色。

## 4. 非正式 Resolver 的条件审计（不新增 D 类计数）

交叉档案还记录三组重要条件边界；它们已被上面四个 resolver 和硬/默认规则覆盖，不在本研究文件中重复计为第五、第六张力：

1. **内在变化 vs 外部系统推进**：CM 的人物行动证明与 DS 的系统持续可以分层；人物不必解决世界问题，系统持续也不等于人物没有主动性。由 HC-01、HC-03、OT-02、OT-04 审计。
2. **即时回报 vs 延迟后果**：VG 要求责任可追，DS 允许长期/潜伏后果；由 DH-04、HC-03、OT-08 审计。不是要求每场立即报应。
3. **复杂性 vs 可追踪**：TG/DS 允许复杂信息和多方位置，但须按观众当前任务分层；由 DH-03、CM-03、CM-04、OT-07 审计。复杂度不是信息量配额。

如未来同一项目、同一阶段、同一输入下两条硬约束确实互相否定，不能通过格式、层级或条件共存，才升级为 `E｜TRUE CONFLICT`；当前六份档案没有这种不可条件化的硬冲突，不能把“暂无 E”伪写成“五人完全一致”。

## 5. 通用 CONFLICT RESOLVER

未来任何方法张力都必须依次落盘；“取一个中间值”不是默认决策。

```text
CONTEXT
→ 写格式、阶段、当前输入、已锁状态、制作边界、用户授权

→ COMPETING PRINCIPLES
→ 写原则 A / 原则 B 的来源标签、适用条件、不可删价值

→ QUESTION
→ 只问一个可决策问题，不把多个根因混成一题

→ OPTION A / OPTION B
→ 给不同且可执行的路径；必要时加 OPTION C：改变形式、暂停扩写或回到上层

→ TRADEOFF
→ 写人物、主题、关系、因果、信息、系统、观众与制作代价；保留未选项

→ DECISION CONDITION
→ 使用可观察门槛（删开场后的引擎、终点条件、功能保留、权限路径、状态继承）

→ DECISION
→ 按 L1→L8 层级与四分类优先级选择；若条件不满足，输出 N/A/WARNING/BLOCKED

→ OUTPUT
→ 生成 Purpose/Format、State、Engine、Destination、Module、Alternate Execution 等工件

→ REVIEW
→ 新证据、表演、反馈、锁定正史或制作变化改变条件时，重新打开 resolver
```

Resolver 决策顺序：先检查 HC 是否满足；再使用适用的 Conditional Method；默认 Heuristic 仅作为起点；Optional Tool 只提供记忆/审计，不可单独决定创作价值。

## 6. Provenance Map

### 6.1 来源档案 → 能力域

| 来源 | 可直接借用的窄能力域 | 不能回写为该单人的内容 |
|---|---|---|
| CM | central dramatic argument、misbelief/旧逻辑、人物目标/选择、行动证明变化、有限季总论断/单集问题、反机械结构审稿 | Series Engine、Institution Map、Production 顺序、X 的 L1–L8 或 13 条 Studio 规则 |
| VG | Character Consequence Engine、责任链、升级条件、随机扰动的后续回应、可交接 story-breaking beat | 每集必须升级、随机绝对禁止、固定卡片/房间配置、Series Engine 全部规则 |
| SR | premise/engine 区分、EP02 状态差、Continuing Drive、Series/Season Engine、关系/职责供给、形式容量与耗竭 | 固定 cliffhanger、ABC 配额、无限连载、每集大反转或快节奏人格 |
| TG | Destination、Scene Entry/Exit、Reality/权限/空间/信息路径、复杂度分层、模块化、制作现实与替代解法的窄输入 | Studio 的 Scope Compression 命名/顺序、纪录片式写实、固定 block、成本优先 |
| DS | Research→Drama、Institution/Incentive、World Without Protagonist、Multi-Sided/Ensemble、Distributed Causality、System State、长期后果 | 完整社会模拟、无反派、政治立场、悲观/慢节奏、所有故事必需系统引擎 |
| X | 五人交叉矩阵、A–E 分类、共识/互补/去重、L1–L8、Conflict Resolver、13 条 Studio 规则、综合干跑 | 不得拆回任何单人，除非重新进行来源追踪并明确新增推断层 |

### 6.2 综合规则 → 证据来源与归因层

| 综合规则/工件 | 支撑输入 | 最终归因标签 | 归因禁令 |
|---|---|---|---|
| HC-01 / `Choice→Consequence→Updated State→Next Choice` | CM、VG、TG、DS，X 去重 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION` | 不称为 Vince 的单一公式，也不要求每场都有选择 |
| HC-02 / Reality + Agency Path | CM、VG、TG、DS，X 分层 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION` | 不写成 Tony 的写实主义禁令、David 的制度决定论或“禁止随机事件” |
| HC-03 / System Persistence | VG、SR、DS、TG，X 长篇边界 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION` | 不要求所有轻类型完整模拟系统，不要求每个后果立即回报 |
| HC-04 / Attribution Gate | 五份档案证据边界，X provenance | `AI FILM STUDIO SYNTHESIS` | 不能把 X 的综合结论伪造为五人共识原话 |
| HC-05 / Production Order | TG 制作现实窄输入，X/Studio | `AI FILM STUDIO SYNTHESIS` | 不说 Gilroy 提出固定五段算法；不因 AI/成本直接删除 |
| `Series Engine` | SR 主责，VG/DS/TG/CM 提供状态、后果、方向边界 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION` | 不把连续性变成固定 cliffhanger/ABC/无限续订 |
| `Destination + Path Open` | TG/CM 方向，VG/SR 改道边界 | `SYNTHESIZED INFERENCE｜CROSS-DISTILLATION` | 不把任何一端写成单人绝对主义 |
| `Scope Compression` | TG 限制驱动替代；DS/SR/CM/VG 提供功能审计输入；X 命名 | `AI FILM STUDIO SYNTHESIS` | 不归因给 TG 的原生术语/算法，不把低成本当第一优先级 |
| `L1–L8 Decision Stack` | 五人档案接口 + X | `AI FILM STUDIO SYNTHESIS` | 不是五人的原生层级；允许按形式标 N/A |
| `Conflict Resolver` | X 交叉协议 + Studio 审核 | `AI FILM STUDIO SYNTHESIS` | 不用“中间值”抹平未选方案、条件和代价 |

### 6.3 运行时归因模板

任何进入综合模型的规则必须按以下格式写入：

```text
[RULE-ID] 规则文本
分类：HARD CONSTRAINT / DEFAULT HEURISTIC / CONDITIONAL METHOD / OPTIONAL TOOL
证据层：SOURCE-SUPPORTED / SYNTHESIZED INFERENCE｜PERSON / SYNTHESIZED INFERENCE｜CROSS-DISTILLATION / AI FILM STUDIO SYNTHESIS
输入档案：CM / VG / SR / TG / DS / X（可多选）
适用门：格式、阶段、题材或制作条件
输出工件：Purpose / State / Causal / Engine / Module / Alternate Execution / Diagnosis
不可归因：明确列出不能写成哪位创作者的原生观点
复查条件：什么新证据、反馈、用户锁定或制作变化会重开规则
```

## 7. 研究完成检查

- [x] 四类规则已分层，HARD CONSTRAINT 仅 5 条且均有边界。
- [x] 正式四个 D 类张力已逐项写成 `CONTEXT → COMPETING PRINCIPLES → QUESTION → OPTION A/B → TRADEOFF → DECISION CONDITION`，并附 `DECISION/OUTPUT/REVIEW`。
- [x] 内在变化/系统持续、即时/延迟、复杂/可追踪被保留为条件审计，不被误计为额外 D 类矩阵行。
- [x] X 的综合规则、层级、冲突器、生产顺序与 Scope Compression 明确标为交叉推断或 Studio 自有，不回写给单人。
- [x] 当前结论保留 `E｜TRUE CONFLICT = 0` 的边界：没有不可条件化的硬约束冲突，但不宣称五人完全一致。
- [x] 未创建 `Showrunner SKILL.md`，未修改 Obsidian Vault。
