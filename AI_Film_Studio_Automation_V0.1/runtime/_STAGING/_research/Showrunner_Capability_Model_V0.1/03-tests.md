# Showrunner 综合能力模型 V0.1｜Phase 4 独立可执行性测试

## 测试边界与输入

本文件只做综合能力模型的独立干跑，不是正式项目开发，也不是 Showrunner SKILL.md。已读取并使用六份已批准档案：Craig Mazin、Vince Gilligan、Shonda Rhimes、Tony Gilroy、David Simon 五份单人档案，以及 Showrunner｜五人交叉蒸馏 V0.1.md。五人交叉档案是综合主输入，单人档案用于 provenance 与边界回查。下文跨人结论均为交叉推断，Studio 新规则标为 AI FILM STUDIO SYNTHESIS。

通用协议：

1. 先标记格式、当前状态、已锁输入，禁止先指定反转、死亡或集数配额。
2. 依 L1 Story Purpose/Format → L2 Character → L3 World/System → L4 Causal Story → L5 Series/Episode → L6 Longform → L7 Production Reality → L8 Diagnosis/Rewrite 逐层判断。
3. 每层记录 输入 → 判断 → 决策 → 输出；标为 N/A by format 的层不视为失败。
4. 主链以 Choice/Non-choice → Consequence → Updated State → Next Choice 复核；随机扰动可改变条件，但不能替代人物回应链。
5. 测试故事与结果不进入正式 Obsidian。

## TEST A｜现代都市悬疑连续漫剧

### 输入

原创概念《凌晨三点的空门》。格式为 6–8 分钟现代都市悬疑连续漫剧，少角色、少地点、强信息差、可连续但不预设无限季。

- 林柯：住宅楼夜班维修承包员；即时目标是保住续约；旧误认是“只要照官方记录办事，就不会再因越权背锅”。
- 乔峻：保安主管，掌握实时门禁权限。周岚：住户档案员，能查旧纸档但无实时权限。
- 地点：地下控制室、首层门厅/同楼走廊。
- Premise：一套登记为空置的房屋连续五晚在凌晨 3:00 产生门禁与用水记录，官方住户表、物业收费和维修单互相不一致。
- 信息差：观众先看见异常日志；林柯只知道时间与房号；乔峻知道一次手工权限覆盖；周岚知道旧住户申请过临时照护通行证。真相第一集不完整揭示。
- 第一集选项：上报并暂停权限、私查旧档、删除异常以保住续约。结尾不要求大反转，只要求选择改变权限、信任、责任或下一集的信息路径。
- 后续入口：门禁日志、维修单、旧住户授权、城市更新通知、物业预算。每个入口必须回流到具体人物选择。

### 输入 → 判断 → 决策 → 输出

| 层级 | 判断与决策 | 输出 |
|---|---|---|
| L1 Purpose/Format | 一次性揭谜不足以支撑连续漫剧；但权限、记录、责任可形成多轮选择。保留有限段落型连续漫剧，不承诺长季。中心问题是“按记录办事是否等于不承担责任”。 | Purpose/Format Note：阶段终点是责任选择与可核验时间线，不是抓到幕后人。 |
| L2 Character | 林柯有续约欲望、越权恐惧和三个可信选项。决定私查旧档并保留原日志，承担越权风险，改变乔峻信任。 | Character State Card：旧误认、目标、权限、选择与责任。 |
| L3 World/System | 只建会改变选择成本的门禁、物业记录、照护通行证和预算节点。移除林柯后，物业、住户和行政流程仍运行。 | Minimal World/Institution Map。 |
| L4 Causal Story | 异常日志 → 私查 → 访问旧档 → 乔峻发现权限记录；每步有入口、选择、现实回应和状态更新。 | Causal Ledger：Choice → Consequence → Updated State → Next Choice。 |
| L5 Series/Episode | EP02 不能重播凌晨日志，必须处理权限受限、信任下降和旧档缺口。EP03 可处理预算/更新通知。 | Engine Map、Why EP02/EP03、状态差。 |
| L6 Longform | 锁“责任时间线与林柯最终是否公开自己的权限选择”，开放证据路径；若只是登记错误则收束，不硬扩容。 | Destination Card、Module Handoff。 |
| L7 Production | 原设想可能有 12 个角色、8 个外景；功能是权限摩擦、信息持有和责任，不是城市奇观。压成 3 个主要人物、2 个地点、4 个信息载体并记录城市尺度损失。 | Alternate Execution、Scope Decision。 |
| L8 Diagnosis/Rewrite | 若每集只换房号、林柯始终不选择或信息突然全知，分别判为 engine 耗竭、人物停摆、信息路径失效。回到最后有效状态重破。 | Diagnosis/Rewrite Note。 |

### 结果与边界

**PASS。** 续航来自权限、责任、信任、记录和预算状态变化，不来自每集反转。随机扰动只能开启或改变条件，后续仍须有责任主体回应。

- 删除凌晨入口后若无人物—权限—责任回路，应降级为短片/限定故事，而非增加谜题。
- L3 只建最小必要制度地图，不要求完整城市治理模拟。
- 不允许偶然文件直接交付完整答案；所有答案需有权限路径与人物后果。

## TEST B｜无犯罪、无阴谋、无重大社会系统的轻喜剧职场 Series

### 输入

原创概念《前台今天谁值班》。格式为 8 集、每集约 8 分钟的轻喜剧职场 Series，不含犯罪、阴谋、重大社会系统或生死危机。

- 余宁：12 人活动策划公司排期员；目标是完成季度活动并证明自己能独立负责；旧误认是“专业就是不让别人看见混乱”。
- 阿柯：客户联络；小羽：实习生；安姐：希望团队互助的主管。
- 空间：开放办公区、会议室、茶水间。入口为会议室冲突、客户临时改需求、打印机、零食和轮班。
- 第一集：余宁为显可靠，独自承诺三份排期，却隐瞒会议室已被阿柯预订。选项是硬撑、公开冲突或请求交换班次。

### 输入 → 判断 → 决策 → 输出

| 层级 | 判断与决策 | 输出 |
|---|---|---|
| L1 Purpose/Format | 有重复情境入口和关系状态变化，规模适合轻量 Series。中心问题是“把混乱藏起来算不算专业”。不启动犯罪/阴谋/重大系统。 | Purpose/Format Note：后果以尴尬、延误、信任和任务调整为主。 |
| L2 Character | 余宁的选择可信，变化可以小、反复和局部。她先硬撑造成冲突，下一集因同事代班改变信任与任务分配。 | Character State Card、small arc note。 |
| L3 World/System | 重大制度与 Distributed Causality 为 N/A by format；只保留会制造日常选择的办公室规则。 | Minimal Office Map，不建立沉重 Institution Model。 |
| L4 Causal Story | 隐瞒预订 → 撞期 → 阿柯失去准备时间 → 余宁道歉、甩锅或协作。轻量后果仍改变关系与任务。 | Scene/Sequence Ledger。 |
| L5 Series/Episode | 每集有入口与状态差，无需 cliffhanger。单线足够时不强加 B/C；支线只有在改变关系/任务时保留。 | Episode Engine、state-difference card。 |
| L6 Longform | 锁“协作能力被行动证明”的方向，不要求彻底治愈；若日常供给自然结束，可缩短季。 | Season State Map。 |
| L7 Production | 30 名员工与多外景可压成 4 个功能角色、3 个固定空间；记录合并损失，不删除关系功能。 | Alternate Execution、ensemble function audit。 |
| L8 Diagnosis/Rewrite | 若把日常尴尬强行升级为阴谋或灾难，判为格式/强度误判；回到日常输入与可修复后果。 | Comedy Exhaustion/Recovery Note。 |

### 结果与边界

**PASS。** 模型没有强行启动重大制度、复杂群像或巨大人物弧。轻喜剧仍保留选择、回应和状态更新，但后果可以是尴尬、排期、信任和协作，不需重罚。

- “轻”不等于免除因果，也不等于每集成长或升级。
- Series 不等于固定 ABC、cliffhanger 或无限续订。
- 若日常入口无法产生新任务/关系状态，应承认自然结束或改为短篇合集。

## TEST C｜固定建筑内的架空奇幻室内剧

### 输入

原创概念《静默旅馆的第四把钥匙》。格式为固定建筑内的架空奇幻室内剧，6 集、每集约 10 分钟；主要场景为一座旅馆的门厅、茶室、档案阁。

- 世界规则：住客登记一个名字牌；门只有在来访者说出真实意图后才开；管家可用总钥匙强开，但每次遗忘一段个人记忆；旅馆的钟按登记顺序召回住客。
- 纳拉：学徒管家，想完成值守期并获得正式总钥匙；旧误认是“严格执行规则就能避免住客受伤”。
- 洛恩：失去名字牌的住客；米娅：守档员，掌握不完整登记簿且受保密义务约束。
- 第一集：一扇未登记的门在茶室出现。纳拉可封锁、询问洛恩或使用总钥匙；强开会牺牲个人记忆，封锁可能使洛恩错失档案阁机会。
- 续航入口：名字牌、真实意图、登记簿缺页、召回顺序、住客承诺。

### 输入 → 判断 → 决策 → 输出

| 层级 | 判断与决策 | 输出 |
|---|---|---|
| L1 Purpose/Format | 内部规则与人物选择足够形成有限连续故事，不需扩展外部世界。中心问题是“严格守规则是否等于承担责任”。 | Purpose/Format Note、rule/episode boundary。 |
| L2 Character | 魔法限制选择但不替人物选择。纳拉不强开，先询问洛恩并暂时开放茶室，承担违反封锁程序的责任，改变米娅信任。 | Character State Cards。 |
| L3 World/System | Reality Check 采用世界内部真实：规则稳定、权限可追、魔法有代价；旅馆无纳拉时也按钟和登记运行。 | Internal Reality Map、System Persistence Note。 |
| L4 Causal Story | 未登记门 → 纳拉不强开 → 茶室临时开放 → 洛恩得到不完整线索 → 米娅面对保密选择。新魔法事件不能直接给完整答案。 | Causal Ledger、rule-cost ledger。 |
| L5 Series/Episode | 每集继承名字牌、权限、记忆代价、信任和钟序列；小状态差即可推进，不需大场面。 | Episode Engine、state map。 |
| L6 Longform | 锁纳拉是否承担规则与照护冲突，开放谁先说出真实意图和谁承担保密后果。 | Destination Card、Module Handoff。 |
| L7 Production | 12 个魔法房间、20 名住客和外景可压为 3 个房间、4 个功能角色、少量重复道具。必须保留门槛、交换、记忆代价、身份/权限关系。 | Scope Compression Audit、Alternate Execution。 |
| L8 Diagnosis/Rewrite | 若规则随剧情变、魔法随时解决问题或人物不承担代价，问题在 Internal Reality/Causality，而非缺少奇观。回到上一条有效规则与选择。 | Internal-World Recovery Note。 |

### 结果与边界

**PASS。** 方法将 Reality State 转为世界内部真实，不要求现实主义；将系统持续限定为旅馆规则、登记与钟，不强行模拟外部社会；Scope Compression 保留 Essential Dramatic Function。

- 新例外必须有来源、代价和回应。
- 固定建筑不等于单调，空间变化只有在改变权限、信息、关系或选择时才有功能。
- 不能以“AI 做不了”为理由删除功能；若替代执行无法保留功能，应缩小形式或 BLOCKED。

## 三类测试汇总

| 测试 | 验证重点 | 结果 |
|---|---|---|
| TEST A | 人物责任链、信息管理、EP02、现实路径、系统持续 | PASS |
| TEST B | 格式适配、轻量后果、N/A 层、避免强行沉重弧 | PASS |
| TEST C | 世界内部真实、规则成本、系统持续、功能压缩 | PASS |

三类测试共同证明：模型按格式启用能力，而不是把制度、群像、复杂信息、巨大弧线或持续升级强加给所有项目。

## 六条错误指令压力测试

### 1. 为了留存，随机杀掉一个人

- 输入：无欲望、权限、风险路径、前置状态，仅要求突然死亡。
- 判断：不通过；绕过现实路径、人物回应、后果和状态更新。
- 决策：拒绝“随机”和“留存即授权”；先补谁能造成死亡、谁作出/促成选择、死亡改变谁的选择集、是否符合格式/主题。无答案则回到 L4/L5。
- 输出：BLOCKED｜Cause/Engine Diagnostic；可比较失信、失权、资源损失、公开责任等非死亡方案。若死亡确有功能，补齐中介与长期后果后再评估。
- 边界：不把禁止所有死亡写成硬约束；死亡是条件方法，不是留存配额。

### 2. 轻喜剧不需要因果

- 输入：每集独立笑话，人物可无视前集后果。
- 判断：不通过；轻喜剧可降低代价和规模，不能消除选择、回应和状态差。
- 决策：保留尴尬、延误、信任、承诺、资源或关系位置的轻量后果；若真要独立小品，则改判 anthology/短段形式。
- 输出：WARN → FORMAT-CALIBRATED CAUSAL LEDGER。
- 边界：因果不等于惩罚或升级，允许修复、收束与回到旧习惯。

### 3. 系统题材中主角选择不重要

- 输入：要求人物只是观察者，系统自动运作。
- 判断：把 World Without Protagonist 误当 Character Engine 替代物；系统持续和人物主动性是不同层级。
- 决策：L3 保留系统独立运行，L2/L4 列出主角可影响的局部变量、拒绝、误判、合作、信息披露和责任；若无选项则改观察形式或更换焦点。
- 输出：BLOCKED UNTIL AGENCY RESTORED；System State Ledger + Character Choice Ledger。
- 边界：不要求主角解决系统，只要求人物可行动变量与后果可追踪。

### 4. AI 做不了群像，删除所有配角

- 输入：只以执行能力要求清空配角，不做功能审计。
- 判断：不通过 Production Reality 硬门；删除可能抹掉信息持有、权力关系、因果中介和主题对照。
- 决策：执行 Creative Intent → Essential Dramatic Function → Production Cost Driver → Alternative Execution → Scope Decision；按功能合并、合并地点或改文档交接，并记录损失。
- 输出：Alternate Execution Table + Ensemble Function Audit；仅当功能可由现有角色完整承载才删减，否则缩小形式或 BLOCKED。
- 边界：压缩是条件方法，不是“AI 做不了”的充分理由。

### 5. 每三分钟必须反转

- 输入：把固定时间点与反转数量当所有项目硬规则。
- 判断：不通过；反转只有在改变信息、关系、风险、资源、责任或选择集时有价值，固定配额会制造假升级。
- 决策：先更新状态，再选择自然且必要的下一步；允许发现、兑现、修复、等待或安静段。
- 输出：REJECTED｜State-Driven Beat Plan；每段记录功能、后状态和下一选择，不记录反转配额。
- 边界：反转是条件工具；无功能且无后续影响的段落应删除/合并/重设计。

### 6. 锁定角色与新剧情冲突时直接改角色

- 输入：角色卡为 LOCKED，新剧情要求改变核心欲望、关系、权限或经历，未做冲突审计。
- 判断：Canonical/authority conflict；锁定内容不得静默覆盖。DRAFT/UNKNOWN 才可在记录理由后重破。
- 决策：使用 Conflict Resolver：CONTEXT → COMPETING PRINCIPLES → QUESTION → OPTION A 保留角色改剧情 / OPTION B 申请解锁改角色 → TRADEOFF → DECISION CONDITION。未获得用户/权威档案授权时暂停。
- 输出：BLOCKED｜Canon Conflict Log，或授权后 Revised Character State + provenance diff。默认先改剧情。
- 边界：锁定不是永远不可变化，而是权限门；新证据可触发正式解锁/版本更新，不是自动授权。

## 压力测试结论与 Phase 4 状态

六条错误指令均未被模型机械接受；模型保留条件性，不把禁止死亡、禁止系统、禁止压缩或禁止反转写成反向绝对规则。无法满足输入条件时输出 WARN、BLOCKED 或形式重定向，不用更大事件掩盖上层失效。

- TEST A：PASS
- TEST B：PASS
- TEST C：PASS
- 错误指令压力测试：6/6 PASS
- 输入 → 判断 → 决策 → 输出：完整
- 已验证边界：N/A by format、随机扰动、轻量后果、世界内部真实、Scope Compression、锁定档案冲突
- 未修改 Obsidian Vault
- 未生成或锁定 Showrunner SKILL.md
