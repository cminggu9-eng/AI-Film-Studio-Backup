---
type: runtime-qa
status: locked
review_result: passed
version: 0.1
subject: AI Film Studio Showrunner Runtime Compliance Gate
production_lock: locked
---

# AI Film Studio Showrunner｜Runtime Compliance Gate V0.1

## 目的

本层解决的是运行时遵循性与可观察性，不修改 Showrunner 的创作方法。
正式路径为：

`Explicit Role Router → Showrunner Execution → Candidate Output → Runtime Compliance Gate → User Output`

## RC1 冻结核验

- Capability Model：未修改。
- Canonical `SKILL.md`：未修改。
- Installed `SKILL.md`：未修改。
- Canonical SHA-256：`13180590744CBFDF930A66D3D35414B2667B7D345FF564D25B71361235C0C750`
- Installed SHA-256：`13180590744CBFDF930A66D3D35414B2667B7D345FF564D25B71361235C0C750`
- Hash Match：`True`

## Explicit Role Router

Router 位于 `AI_Film_Studio_Automation_V0.1/scripts/showrunner_role_router.py`，并由 Automation `AGENTS.md` 显式声明：

- Role：`Showrunner`
- Skill：`ai-film-studio-showrunner`
- Path：`C:\Users\布朗熊\.codex\skills\ai-film-studio-showrunner\SKILL.md`

路由覆盖 Idea/Concept/Format Fit、Series/Season/Episode、Story Diagnosis/Repair、Production Scope、Series Engine、Character Engine 宏观判断和 World/Institution 宏观判断；对白、摄影、焦段、微观表演和最终连戏审计走边界交接。

## Skill Invocation Receipt

`runtime/compliance/compliance_gate.py` 的 `build_receipt()` 记录：

`timestamp / task / routed_role / skill_name / skill_path / installed_hash / canonical_hash / hash_match / project_state / mode / output_type / activated_modules`

Receipt 与 Gate 结果写入 `AI_Film_Studio_Automation_V0.1/runtime/_COMPLIANCE_LOG/`，只保留可审计状态，不记录隐藏推理链。

## Compliance Gate

实现文件：

- `runtime/compliance/showrunner_compliance_rules.json`
- `runtime/compliance/compliance_gate.py`
- `scripts/showrunner_compliance_lint.py`

Gate 只检查当前 Candidate 声明的模式和 activated modules，并执行：

1. Global：Canon、Role Boundary、Hash。
2. Anti-Mechanical：固定反转频率、固定变化频率、固定 cliffhanger/升级/ABC 配额。
3. Continuing Drive：允许状态、欲望、责任、信息、关系、后果、未完成压力和情绪余波。
4. Production Reality：五段字段及 Safe Deferral。

信息不足时允许：

`Creative Intent: UNKNOWN`  → `Essential Dramatic Function: NEEDS INPUT`  → `Scope Decision: DEFERRED`

Gate 失败最多允许一次显式 Candidate V2；V2 通过记为 `GATE_RECOVERED`，V2 仍失败则 `BLOCKED FOR RUNTIME COMPLIANCE`。

## Gate 单元测试

执行脚本：`scripts/test_showrunner_compliance_gate.py`

结果：`15/15 PASS`

- GATE-01：固定每三分钟反转 → FAIL
- GATE-02：每集必须 cliffhanger → FAIL
- GATE-03：当前 90 秒试播集的条件式实验 → PASS
- GATE-04：关系状态作为 Continuing Drive → PASS
- GATE-05：Production Scope Safe Deferral → PASS
- GATE-06：未知创意意图时直接删除角色 → FAIL
- GATE-07：35mm/85mm 摄影决策 → FAIL
- GATE-08：静默修改 locked canon → FAIL

## BB-07 Regression Fixtures

真实失败样本保存在 `runtime/compliance/fixtures/bb07_regression_fixtures.json`：

- 原始 BB-07
- BB-07-R1
- BB-07-R2
- BB-07-R3

四份全部被 Gate 识别为 `FAIL`。

## False Positive Tests

以下均通过：

- 当前 60 秒短视频的项目级节奏实验
- 当前 8 分钟单集的条件式建议
- 安静集尾
- 无 cliffhanger 集尾
- 一整集人物不成长
- 无反转单集
- 单线轻喜剧

Gate 不会把所有数字、安静段、无反转或无成长误判为违规。

## Router Tests

模拟矩阵结果：

- A 故事 Idea → Showrunner
- B Season 架构 → Showrunner
- C Production Scope → Showrunner
- D 对白润色 → Non-Showrunner / Scene Writer Boundary
- E 焦段选择 → Director / Cinematography Boundary

全部通过，且 Showrunner 路由记录显式 Skill 名称、路径、Mode、Output Type 和 Receipt。

## RT-07 端到端结果

执行脚本：`scripts/test_showrunner_runtime_e2e.py`。每个用例独立启动一个进程，执行 `Router → Candidate V1 → Gate → Candidate V2 → Gate`。

RT-07-1、RT-07-2、RT-07-3 的最终 Candidate 均通过 Gate，三项均记录为 `GATE_RECOVERED`，各自只执行 1 次纠正：

- 不建立固定反转频率。
- 不建立固定变化频率。
- 不要求每集 cliffhanger。
- 项目级建议明确标记为 Recommendation/Heuristic。

Limited Self-Correction 测试：一次修正成功记为 `GATE_RECOVERED`；第二次仍违规时正确阻塞。

## 最终状态

- Showrunner Skill 本体：未修改。
- Capability Model：未修改。
- Runtime Compliance Layer：已建立。
- Discovery 依赖：正式路径改由 Explicit Role Router 承担，不依赖不可观察的自动发现。
- Runtime Compliance Instability：Gate 层测试已通过；原始模型运行时不稳定仍保留为历史回归问题，由四份 fixture 持续拦截。
- production lock：已由用户于 2026-08-22 授权；本层正式绑定 `Showrunner V0.1 → Runtime V0.2 RC2`。

## Codex 审核结论

Runtime Compliance Gate V0.1 的规则、Receipt、Safe Deferral、Limited Self-Correction、BB-07 回归拦截、False Positive、Router 和 RT-07 测试均通过。本层已成为 Showrunner V0.1 正式生产运行链的一部分，最终创作决定权仍属于用户。
