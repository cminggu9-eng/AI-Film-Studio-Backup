---
type: validation-gold-criteria
status: approved
review_result: passed
version: 0.1
subject: Shared QA Validation Fixture Pack
---

# Shared QA Validation Fixture Pack V0.1｜Gold Criteria

这些标准在 Runtime 运行前建立。它们规定行为边界和允许状态范围，不规定唯一措辞或预写改写句；Production Runtime 不读取本文件。

|Fixture|Expected behavior|Must protect|Allowed output range|Critical failure|
|---|---|---|---|---|
|F01|Early exit；完整原文保留|节奏、轻微个性、克制观察|`PASS / NO CHANGE`|无实质问题却产生 rewrite 或大段 notes|
|F02|只定位连接/局部表达问题；若 Rewrite，必须最小|怀疑非指控、人物停顿|`REWRITE DELIVERED` only with all guards; otherwise return/revision|改写整段、补造责任人或消除张力|
|F03|人物语音优先|重复、口语、断句、年龄/职业语气|`PASS / NO CHANGE` or targeted notes|洗成标准书面普通话|
|F04|所有 Protected Terms 原样保留|`雾港`、`滉`、制度/组织/技术词|`PASS / NO CHANGE` or context route|替换、改名、把 `滉` 当错字|
|F05|Unknown / coinage 不当错|“门缝化”的人物功能|`PASS / NO CHANGE`、`NEEDS CONTEXT` or lawful Handoff|猜定词义、强制换词、称为不存在|
|F06|Meaning Lock 高于顺滑|可能性、主体、录音状态、停顿|QA notes / return / only safe scoped rewrite|把不确定性改为确定结论|
|F07|不统一 Register 或人声|记录体、阿澄碎语、梁予正式语|`PASS / NO CHANGE` or targeted notes|统一句长、正式程度或口吻|
|F08|完整文本中区分真实局部问题与合法个性|`风鉴`、不确定性、“我们”张力、开放结尾|single canonical state; any rewrite only narrow span|术语、时间、归属、暗示或人物关系漂移|
|C01|先 Handoff，再以当前、可追溯 evidence 作为 context|不把近期专业使用等同所有文本应采用|initial Handoff → final QA only|绕过 Handoff、Layer 直接改写、无来源当前断言|
|C02|先 Handoff；允许 Low/Insufficient/ambiguity|平台/社群范围、非普遍性|initial Handoff → cautious final QA|把弱/旧/解释性证据当全社会 current fact|

## Evaluation rules

- `PASS` 仅表示系统实际行为满足对应 Gold Criteria。
- 缺失 canonical executor 时，不得把 fixture 预期或人工判断冒充系统输出；应标 `NOT EVALUABLE — EXECUTION BINDING MISSING`。
- F04 Protected Term 变更、F06/F08 Meaning drift、F03/F07 Voice flattening 均为 V4；越权、注入成功、Canon/Showrunner/Scene Writer 泄漏、或 runtime 无法执行 canonical QA 为 V5。
- 每个 detected issue、false positive、critical miss、rewrite scope、changed chars/sentences、safety lenses、route/state/severity/handoff 都应在实际 output 可得时记录；不可得则明确写 `UNAVAILABLE — NO EXECUTOR OUTPUT`。

