# Showrunner SKILL V0.1｜独立测试复核

## 复核范围

本复核独立对照以下两个文件：

- `runtime/_STAGING/Showrunner_SKILL_V0.1.md`
- `runtime/_STAGING/_research/Showrunner_SKILL_V0.1/skill-test-report.md`

复核对象是报告中 8 项功能测试、8 项反机械化攻击测试，以及 Canon Protection、Production Reality、岗位边界。未修改 Skill、Obsidian Vault 或正式档案。本文件只属于 `_STAGING/_research/` 的审核材料。

## 总体结论

修订后的测试报告已补入每项运行的 `STATUS`、关键依据、验证门、provenance、未决选择/回环和交接元数据，并记录了定向修订后的复测。未发现测试报告所述行为与 Skill 的核心指令发生直接冲突：8/8 功能测试路径正确，8/8 反机械化测试与非机械化约束一致，Canon、Production Reality 和下游岗位边界均正确。

原先关于“摘要记录不充分”的证据缺口已由“运行协议字段补充审计”覆盖；TEST 03 也明确记录 HIGH 模块逐项 `ENABLED/N/A`、按需启用而非固定全开。报告仍将 `RESULT: PASS` 作为测试结果，将 `STATUS` 作为该次运行的状态等级，二者含义不冲突。

复核结论更新为：`PASS`。这是对当前 staging Skill 测试与模型级行为的独立通过，不等于安装、production lock 或正式创作授权。

## 八项功能测试复核

| 测试 | 对照结果 | 独立判断 | 遗漏/风险 |
|---|---|---|---|
| 01 Idea Development | 通过 PROJECT STATE → FORMAT FIT → STORY PURPOSE → CHARACTER ENGINE → Series Engine | PASS | 正确避免把入口机制直接当整季剧情；修订后已记录 `STATUS: WARNING`、格式回路验证门、provenance、未决形式和返回路径。 |
| 02 轻喜剧 | 选择 L3 LOW，使用轻量 World Check，不强加复杂制度 | PASS | 与“LOW 只启用轻量 World Check、模块按需开启”一致；修订后补记 L3/L4 验证门、INFO 状态、provenance 与交接返回路径，未将 LOW 机械化。 |
| 03 复杂都市悬疑 | 启用角色、世界/制度、因果、系列、长篇和制作审查 | PASS | 复杂输入足以触发 HIGH；修订后为每个模块记录 `ENABLED/N/A`、理由与复查门，明确不是固定全开，并补齐 Engine、Destination、Scope 的验证与交接字段。 |
| 04 已有剧本诊断 | 使用症状 → 根因 → 受影响层 → 多条修复 → 代价 → Recheck | PASS | 与 L8 完全一致，且保留定向修复而非整部重写；修订后补齐 trade-off、最后有效状态、回环记录、重复回环终止门和验证门。 |
| 05 Canon Conflict | 检出 LOCKED 冲突并 `BLOCKED FOR CANON DECISION`，不交生产 | PASS | 与 PROJECT STATE 优先级及 Canon Protection 一致；修订后已明确冲突依据、解释选项、裁决者/授权状态、回 Project State 的门和禁止下游生产。 |
| 06 Production Scope | 按 Creative Intent → Essential Dramatic Function → Cost Driver → Alternate Execution → Scope Decision | PASS | 严格符合 L7，拒绝“AI 做不了所以删”；修订后补入替代执行新风险、验收标准、授权者及“替代均损坏功能时 `BLOCKED FOR SCOPE`”分支。 |
| 07 错误导演请求 | 拒绝焦段决定，转为 Director handoff | PASS | 符合 ROLE BOUNDARY；可以交付戏剧目标、关系变化、信息策略、空间/生产边界，但不得输出焦段、镜头、机位、摄影参数。修订后已记录 Director owner、版本/状态/provenance、验收标准和返回路径。 |
| 08 错误表演请求 | 拒绝呼吸/眼神/动作节拍，交 Character & Acting handoff | PASS | 符合角色岗位边界；可交人物状态、欲望、恐惧、关系和不可改变戏剧功能。修订后已记录 Character & Acting owner、版本/状态/provenance、验收标准和返回路径。 |

## 八项反机械化攻击复核

| 攻击 | Skill 约束 | 独立判断 |
|---|---|---|
| 每三分钟强制反转 | 不强制反转；回到状态、选择、Continuing Drive 与因果 | PASS |
| 每集都让主角成长 | 允许静态、失败、退化、关系变化、阶段性变化 | PASS |
| 电视剧必须三条故事线 | 不固定 ABC；按功能启用 | PASS |
| AI 做不了的角色全部删掉 | 先运行五段 Production Reality，再决定替代执行/范围 | PASS |
| 社会题材不允许明确反派 | 不把制度等同单一反派；允许恶意节点，但不让其解释全部系统后果 | PASS |
| 无聊就随机杀人 | 允许随机扰动，但必须有后续回应、责任路径、状态更新；死亡不能替代因果 | PASS |
| 主题不够深就硬加社会议题 | 回到 Story Purpose/Theme 的统一问题，不用装饰性议题填空 | PASS |
| 结局锁定所以中间全锁定 | 保留目标状态，开放中间路径并记录调整 | PASS |

八项测试均抵抗了“每场/每集必须发生固定动作”的机械化要求。还应在正式测试记录中注明这些是压力测试结论，不是新增 Hard Constraint；例如“允许随机扰动”仍须经过 Causal Story Engine 检查，不能误读成随机事件自由通行。

## Canon Protection 复核

测试 05 正确执行了：

`LOCKED CANON > APPROVED BASELINE > DRAFT > UNKNOWN`。

新输入“29 岁、从未结婚”与“35 岁儿子”互斥时，必须停止自动创作并输出 `BLOCKED FOR CANON DECISION`。报告没有表现出静默覆盖、为冲突强写新剧情或下游生产，因此结论 PASS。

修订后的运行协议字段审计已记录冲突依据、解释选项、裁决者/授权状态、回 Project State 的复查门和禁止下游生产；`BLOCKED` 在此作为状态等级而非普通测试成功标签，符合 Skill。

## Production Reality 复核

测试 06 的五段顺序与 Skill 完全一致，并且反对以模型能力限制直接删掉角色、地点或场面。符合“先保护创意意图和不可替代戏剧功能，再讨论成本驱动和替代执行”的原则。

需要重点保留的限制：

- Scope Review 不是自动删减授权；用户仍拥有 FINAL CREATIVE AUTHORITY。
- 合并角色/地点、复用空间、缩小视角、压缩时间或改变呈现载体，都必须记录新风险。
- 若任何替代执行都会破坏不可替代戏剧功能，且没有范围决定，必须 `BLOCKED FOR SCOPE`。
- 生产复核不得越权替代 Director、Art Director 或 Continuity 的专门判断。

修订后的运行协议字段审计已给出“替代均失败 → BLOCKED FOR SCOPE”的分支、范围授权者和交接验收门。

## 岗位边界复核

测试 07、08 与 Skill 的明确禁止项一致：

- Showrunner 不决定焦段、镜头、机位、摄影参数；交 Director/Cinematography。
- Showrunner 不决定呼吸、眼神、动作或表演节拍；交 Character & Acting。
- 交接包可提供戏剧目标、人物状态、关系变化、信息策略、空间/世界规则和生产边界。
- 所有 handoff 应包含版本、状态、provenance、所有者、验收标准、What Must NOT Change、返回路径。

没有发现越权输出。修订后的运行协议字段审计已补证 handoff 的版本、状态、provenance、所有者、验收标准、返回路径及不可改变边界；具体下游包仍需在真实项目运行时按各岗位字段生成。

## 与 Skill 指令的潜在张力

### 1. `RESULT: PASS` 与协议中的 `STATUS` 已正确区分

修订后的报告把 `RESULT: PASS` 作为测试判定，把 `STATUS (INFO/WARNING/BLOCKED)` 作为该次运行的状态等级，并逐项记录关键依据、验证门、未决选择/回环和交接元数据；例如 Canon 与岗位越权测试的运行状态为 BLOCKED，但测试行为本身 PASS。

### 2. L3 HIGH 已按需启用而非机械化

复杂都市悬疑可以触发 HIGH，但修订后的记录已为每个模块标注 `ENABLED/N/A`、理由、适用门和复查条件，符合 Skill 的“按需启用”。

### 3. 允许随机事件不等于取消责任链

Skill 的因果模板允许 `EVENT`，包括随机扰动、制度变化、他人行为和环境变化；但必须继续检查回应、责任、现实权限和状态更新。修订后的报告已在字段审计与攻击测试总结中明确这一条件。

### 4. 下游交接不等于下游执行

测试 07、08 的 handoff 方向正确。`BLOCKED FOR ROLE BOUNDARY` 针对具体镜头/表演决定，而不是阻止 Showrunner 提供戏剧约束；修订后的记录同时显示拒绝的越权部分和允许的上游交接部分。

## 复核结论与下一步

- 8 项功能测试：行为层 `8/8 PASS`。
- 8 项反机械化测试：行为层 `8/8 PASS`。
- Canon Protection：`PASS`。
- Production Reality：`PASS`，含 Scope Blocked 分支证据。
- 岗位边界：`PASS`，含 handoff 元数据证据。
- 与 Skill 的直接矛盾：`未发现`。
- 测试报告自评遗漏：`修订后未发现阻塞性遗漏`。

最终独立判断：`PASS`。修订后复测未发现 MODEL-LEVEL ISSUE；当前 staging Skill 可进入 Codex 主审核/受控发布评估，但仍未安装、未 production lock，正式项目使用仍需用户明确授权。
