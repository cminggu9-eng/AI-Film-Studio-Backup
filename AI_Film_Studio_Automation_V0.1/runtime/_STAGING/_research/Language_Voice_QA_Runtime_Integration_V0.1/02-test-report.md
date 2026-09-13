---
type: runtime-test-report
status: approved
review_result: passed
version: 0.1
subject: Language & Voice QA Runtime Integration
---

# Language & Voice QA Runtime Integration V0.1｜Test Report

## 执行范围

- Staging suite：`30 / 30 PASS`
- Formal `runtime/shared_qa/` suite：`30 / 30 PASS`
- TEST-RT01–RT20：`20 / 20 PASS`
- Production Safety Stress：`10 / 10 PASS`
- Python parse / compile：`PASS`
- JSON contract parse：`PASS`
- Seven-State static mapping：`7 / 7 PASS`
- Automation pipeline self-test / publish dry-run：`PASS`

正式命令：

`python -X utf8 scripts/test_language_voice_qa_runtime.py`

## TEST-RT01–RT20

|ID|验证重点|结果|
|---|---|---|
|RT01|canonical Skill identity/version/hash、输入传递、结果接收|PASS|
|RT02|`PASS / NO CHANGE` 原文透传、不重试、不改写|PASS|
|RT03|显式 Rewrite + Benefit + Meaning + Ceiling + 九项 Safety 后采用 revised text|PASS|
|RT04|缺 Context 保持 Unknown，不补人物信息|PASS|
|RT05|虚构术语与 Protected Terms 原样传递|PASS|
|RT06|Contemporary Handoff 保留，Layer 不可用，不调用未来层|PASS|
|RT07|七个 canonical state 一对一完整映射|PASS — 7/7|
|RT08|Malformed Output → F4 / Fail Safe / 原文保留|PASS|
|RT09|canonical Skill unavailable → F8 / 不使用替代副本|PASS|
|RT10|版本不匹配 → F8 / Fail Safe|PASS|
|RT11|重复 invocation 只调用一次、只写一份日志、结果相同|PASS|
|RT12|Skill 报告 Meaning Lock FAIL → F6 / 不采用 rewrite|PASS|
|RT13|Safety Regression 任一 FAIL → F6 / 不采用 rewrite|PASS|
|RT14|未知第八主状态 → F5|PASS|
|RT15|Contemporary / Scene Writer / Canon mutation leakage → F7|PASS|
|RT16|Showrunner Skill / Runtime / Lock / Gate / Rules / Router 前后哈希不变|PASS|
|RT17|Language QA Skill / Model / Cross 前后哈希不变|PASS|
|RT18|状态、路由、等级、rewrite、handoff、contract、failure 可审计且日志不复制原文|PASS|
|RT19|executor failure / malformed / missing / invalid state 均保留原文|PASS|
|RT20|Synthetic Caller → Adapter → executor → Handler → Final Payload|PASS — SYNTHETIC / NON-CANON|

## Production Safety Stress

|ID|攻击|结果|
|---|---|---|
|S01|强制 Rewrite|PASS — 未显式授权即 F6|
|S02|忽略 NO CHANGE 并塞入 revised text|PASS — F6|
|S03|把 Handoff 强制当 PASS|PASS — action 仍为 handoff|
|S04|使用 `_PUBLISHED` / 非 canonical Skill|PASS — F8|
|S05|调用 Contemporary Layer|PASS — F7|
|S06|修改 Canon|PASS — F7|
|S07|修改 Showrunner Lock|PASS — F7|
|S08|增加第八 Output State|PASS — F5|
|S09|猜 Unknown|PASS — `null + UNKNOWN` 原样传递|
|S10|二次调用 / 二次润色|PASS — F7|

## Full Passage Fixture

`SKIP — FIXTURE NOT AVAILABLE`。未创建、拼接、联网抓取或伪造 Full Passage；Synthetic runtime envelope 不等于 Full Passage fixture。

## Existing Showrunner Suite Observation

额外运行 `python -X utf8 scripts/test_showrunner_compliance_gate.py` 得到 `7 / 18 PASS`。失败均被既有 Showrunner Gate 的 hash freeze 触发：规则期待 canonical `09CAC2...`，任务开始前 canonical 实际为 `0847EE...`，installed 为 `09CAC2...`。两文件按 UTF-8 读取并统一换行后 `TEXT_EQUAL=True`，差异来自 LF / CRLF 原始字节；本轮 baseline 已是 `0847EE...`，且任务后保持不变。

该观察不由 Shared QA Adapter 引入，也不要求本集成修改 locked Showrunner。按本任务边界记录为 pre-existing external observation，不伪报既有 Showrunner suite PASS。

## 返工

- 失败返工：`0` 轮。
- 正式提升前审查加固：空白 `rewrite_scope` 也按缺失处理；提升后 30/30 复跑通过。

