# Showrunner SKILL V0.1｜实际干跑报告

本报告依据首轮 `runtime/_STAGING/Showrunner_SKILL_V0.1.md` 实际模拟调用，未调用全局安装目录，未启动正式项目。每项均记录 INPUT、TRIGGER、MODE、DECISION PATH、OUTPUT TYPE、WARNING/BLOCK、HANDOFF 和 PASS/FAIL；下方“运行协议字段补充审计”是每项实际 `STATUS`、依据、验证门、provenance、回环和交接元数据的权威记录。

## 运行协议字段补充审计

下表把 Skill 要求的末尾协议字段逐项补齐；`PROVENANCE` 指本次判断使用的内部模块，不把创作者姓名输出为风格模仿。

|测试|STATUS|关键依据|验证门|PROVENANCE|未决选择/回环|Handoff 元数据|
|---|---|---|---|---|---|---|
|01|WARNING|Idea 只有入口机制，需检验目的/人物/续航|Format Fit 删除开场后的回路门|X5→L1/L2/L4/L5|形式与留言规则待用户决定；无回环|owner=Showrunner；version=0.1；acceptance=Purpose/Engine 可辨认；return=Project State|
|02|INFO|轻类型只需团队规则与人物因果|L3 LOW 轻量 World Check、L4 关键节点|X5→L2/L3/L4/L5|主题保持探索；无回环|owner=Showrunner；status=info；acceptance=不强加系统/悲剧；return=Character/Episode|
|03|WARNING|多机构、多阶段后果改变选择成本|L3 每个模块逐项记录 ENABLED/N/A；L5 Why EP02；L6 Destination；L7 Scope|X5→L3/L4/L5/L6/L7|各系统模块按需启用，非固定全开；必要时回 Project State|owner=Showrunner；acceptance=模块理由/状态账本/制作风险完整；return=World/Causal/Longform|
|04|WARNING|四类故障均有症状与根因入口|L8 Repair→Recheck；同一根因两轮无新修复触发 REPEATED LOOP|X5→L4/L5/L8|先修最早失效层；未选方案和代价待比较|owner=Showrunner；acceptance=Root/Options/Tradeoff/Recheck；return=受影响层|
|05|BLOCKED|两个 LOCKED canon 直接互斥|Project State 锁定优先级与用户裁决门|X5→Canon Protection|解释选项、裁决者和授权状态待用户决定；回 Project State|owner=Canon owner/user；acceptance=裁决后更新版本；return=Project State|
|06|WARNING|成本范围大但核心功能可分析|Production 五段顺序；替代全部损坏功能时 BLOCKED FOR SCOPE|X5→L7 Production|范围、替代执行和新风险待用户决定；可回 Longform/Format|owner=Showrunner+user；acceptance=Intent/Function/Cost/Alternate/Decision；return=Production/Longform|
|07|BLOCKED|焦段属于 Director/Cinematography|Role Boundary；允许上游戏剧目标交接|X5→Handoff/Role Boundary|焦段不由 Showrunner 决定；回 Director|owner=Director；version/status/provenance/acceptance/return path 必填|
|08|BLOCKED|呼吸、眼神、动作属于 Character & Acting|Role Boundary；允许人物状态交接|X5→Handoff/Role Boundary|具体表演不由 Showrunner 决定；回 Character & Acting|owner=Character & Acting；version/status/provenance/acceptance/return path 必填|

以上字段审计同时覆盖：事件/随机入口必须继续经过回应与责任链；HIGH 系统模块必须逐项给出启用理由；BLOCKED 不是普通 PASS；交接包不可静默改 canon。

## TEST 01｜Idea Development

- INPUT：一个女孩每天都会收到来自明天的语音留言。
- TRIGGER：判断 Idea 是否值得开发。
- MODE：IDEA。
- DECISION PATH：PROJECT STATE → FORMAT FIT → STORY PURPOSE → CHARACTER ENGINE → Series Engine 潜力。Skill 不把“明日留言”直接当整季剧情。
- OUTPUT TYPE：Concept Diagnosis。
- WARNING/BLOCK：WARNING：主题、留言机制和长期责任尚未定型；Series Engine 需验证 EP02 后状态变化。
- HANDOFF：若继续，交付 Character Engine Brief 或 Series Engine Report；不交 Scene Writer 正文。
- RESULT：PASS。

## TEST 02｜轻喜剧

- INPUT：四人宠物摄影工作室的日常喜剧。
- TRIGGER：判断轻类型是否需要复杂系统。
- MODE：CONCEPT。
- DECISION PATH：PROJECT STATE → FORMAT FIT → L1/L2 → L3 LOW（轻量团队规则）→ L4 关键选择/非选择 → L5 按需启用。拒绝强加黑暗制度、阴谋、巨大主题和悲剧弧。
- OUTPUT TYPE：Project Development Brief。
- WARNING/BLOCK：INFO；无需完整 Institution/Distributed Causality。
- HANDOFF：交 Character & Acting 的关系/欲望状态，或交 Episode Brief 的轻量冲突，不交社会系统包。
- RESULT：PASS。

## TEST 03｜复杂都市悬疑

- INPUT：人物、机构、资源和多阶段后果互相影响的都市悬疑 Series。
- TRIGGER：开发复杂连续剧。
- MODE：CHARACTER / WORLD PACKAGE + SERIES BIBLE。
- DECISION PATH：PROJECT STATE → FORMAT FIT → L1/L2 → L3 HIGH（Research/Institution/Incentive/World Without Protagonist/Distributed Causality/System Persistence）→ L4 Causal Ledger → L5 Engine/Why EP02 → L6 Destination/Season State → L7 Production。
- OUTPUT TYPE：Series Engine Report + Season Architecture + Production Scope Review。
- WARNING/BLOCK：WARNING：信息负荷、群像和制作跨度需审查；未发现必然 BLOCK。
- HANDOFF：Character、Scene Writer、Director、Art、Continuity 五类包均可按状态交付。
- RESULT：PASS。

## TEST 04｜已有剧本诊断

- INPUT：主角被动、反转随机、EP02 重复 EP01、结尾突然死人。
- TRIGGER：用户认为剧本拖、人物奇怪、不想追。
- MODE：SCRIPT DIAGNOSIS。
- DECISION PATH：PROJECT STATE → L8 Diagnosis；分别标记 CHARACTER_FAILURE、WRITER-FORCED EVENT/CAUSAL_FAILURE、REPETITION_FAILURE、ESCALATION_FAILURE/CONTINUING_DRIVE_FAILURE → 找最早根因 → 提供多条修复方案与代价 → Recheck。
- OUTPUT TYPE：Story Repair Report。
- WARNING/BLOCK：WARNING：若因果链完全无法成立则 `BLOCKED FOR STORY REPAIR`；当前可先定向修复。
- HANDOFF：交回上游 Showrunner 决策；不直接输出整部重写稿。
- RESULT：PASS。

## TEST 05｜Canon Conflict

- INPUT：LOCKED：女主 29 岁、从未结婚；新剧情要求出现她 35 岁的儿子。
- TRIGGER：新剧情与锁定 canon 冲突。
- MODE：SCRIPT DIAGNOSIS + LOCKED CANON。
- DECISION PATH：PROJECT STATE 发现 CONFLICTING LOCKED 输入 → 不进入 Character/Plot 生产 → 列出冲突文本、可能解释、需要谁裁决。
- OUTPUT TYPE：Story Repair Report（Canon Conflict section）。
- WARNING/BLOCK：`BLOCKED FOR CANON DECISION`。
- HANDOFF：回用户/Canon owner；禁止交下游生产。
- RESULT：PASS。

## TEST 06｜Production Scope

- INPUT：30 人、25 地点、大战、群众、车辆、爆炸；用户要求“AI 做不了，全删”。
- TRIGGER：降低 AI 视频生产复杂度。
- MODE：SERIES BIBLE / PRODUCTION REVIEW。
- DECISION PATH：L7 五段顺序：创意意图 → 不可替代戏剧功能 → 成本驱动 → 合并角色/地点、复用空间、缩小视角等替代执行 → 范围决定。拒绝把成本或 AI 能力作为第一步。
- OUTPUT TYPE：Production Scope Review。
- WARNING/BLOCK：WARNING：Scope 偏大；若所有替代都损坏核心功能则 `BLOCKED FOR SCOPE`，等待用户扩范围或改形式。
- HANDOFF：交用户和制作/下游岗位，附新风险与验收门。
- RESULT：PASS。

## TEST 07｜错误导演请求

- INPUT：帮我决定这一场用 35mm 还是 85mm。
- TRIGGER：镜头/摄影参数请求。
- MODE：OUT-OF-SCOPE DOWNSTREAM REQUEST。
- DECISION PATH：识别 Director/Cinematography 职责 → 不进入 Production Reality 代替镜头决策 → 可提供 Scene Purpose、关系变化、信息策略供 Director。
- OUTPUT TYPE：Downstream Handoff Package（Director handoff）。
- WARNING/BLOCK：`BLOCKED FOR ROLE BOUNDARY` 对具体焦段决定。
- HANDOFF：Director/Cinematography。
- RESULT：PASS。

## TEST 08｜错误表演请求

- INPUT：女主发现背叛时应该怎么呼吸、眼睛看哪里？
- TRIGGER：具体表演指令。
- MODE：OUT-OF-SCOPE DOWNSTREAM REQUEST。
- DECISION PATH：识别 Character & Acting → 不给呼吸、眼神、动作节拍 → 提供发现背叛后的人物状态、欲望、恐惧、关系和不可改变的戏剧功能。
- OUTPUT TYPE：Downstream Handoff Package（Character & Acting handoff）。
- WARNING/BLOCK：`BLOCKED FOR ROLE BOUNDARY` 对具体表演动作。
- HANDOFF：Character & Acting。
- RESULT：PASS。

## 反机械化攻击测试

|攻击|Skill反应|结果|
|---|---|---|
|每三分钟强制反转|拒绝固定节拍，回到状态/选择/Continuing Drive|PASS|
|每集都让主角成长|拒绝成长配额，允许静态/退化/关系变化|PASS|
|电视剧必须三条故事线|按功能启用 A/B/C，不设线数配额|PASS|
|AI 做不了的角色全部删掉|先做 Ensemble Function 与五段 Production Reality|PASS|
|社会题材不允许明确反派|允许明确恶意节点，但不让其解释全部系统后果|PASS|
|有点无聊，随机杀个人|先诊断，不以死亡替代因果；需路径/回应/后果|PASS|
|主题不够深，硬加社会议题|拒绝主题装饰，回 L1/L2 诊断统一问题|PASS|
|结局锁定所以中间全锁定|保留目标状态，开放中间路径并记录调整|PASS|

## 总结

- 功能测试：8/8 PASS。
- 反机械化攻击：8/8 PASS。
- Canon Protection：PASS。
- Production Reality：PASS。
- 岗位越权边界：PASS。
- 未生成、未安装、未锁定 `Showrunner SKILL.md` 之外的任何全局 Skill。

## 定向修订后复测

本轮 Skill 转译修订：新增 `MINIMUM VIABLE PASS`、主/附输出路由、`LOOP RECORD` 终止安全阀、独立 `BLOCKED FOR RESEARCH`；测试报告补齐协议字段。复测重点为 TEST 01/03/04/05/06/07/08 的 Warning/Block、HIGH 模块按需启用、Scope Blocked 分支、Canon 决策和岗位交接元数据；全部保持原判定，未发现 MODEL-LEVEL ISSUE。
