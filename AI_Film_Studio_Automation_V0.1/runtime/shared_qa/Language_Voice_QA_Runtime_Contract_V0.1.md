---
type: runtime-contract
status: approved
review_result: passed
version: 0.1
subject: Language & Voice QA Runtime Integration
canonical_skill: language-voice-qa
canonical_skill_version: 0.1
---

# Language & Voice QA Runtime Contract V0.1

## 调用边界

`LanguageVoiceQARuntime` 接收 runtime envelope 与一个由合法上游提供的 `language-voice-qa` 执行器。Adapter 负责 canonical Skill 完整性、输入封装、输出契约、七状态映射、失败安全、幂等与最小审计；执行器负责 Skill 判断。Adapter 不检测语言问题，不计算 Severity，不决定 Rewrite，也不二次润色。

## Input Contract

Runtime envelope 使用 snake_case；传给执行器时映射为 canonical Skill 的正式字段：

|Runtime field|Canonical Skill field|规则|
|---|---|---|
|`original` / `text` / `passage`|`Original`|唯一强制字段；冲突 alias 为 F1，缺失/空值为 F2|
|`requested_mode`|`Requested Mode`|缺失安全派生为 `QA_DEFAULT`|
|`register`|`Register / usage`|可缺失；缺失保持 Unknown|
|`available_context`|`Available Context`|只传上游提供内容|
|`speaker_character_context`|`Speaker / Character Context`|只在上游提供时传值|
|`project_constraints_canon`|`Project Constraints / Canon`|不从项目猜测或补造|
|`user_creative_intent`|`User Creative Intent`|不从文本推断|
|`protected_terms_entities`|`Protected Terms / Entities`|原样传递，不标准化|

每个 canonical 字段同时记录 `PROVIDED / DERIVED_SAFELY / UNKNOWN`。Unknown 以 `null` 传递，不替换成模型猜测。

## Invocation Gate

允许的 gate 只有：输入结构、合法 Original、允许 Mode、显式 `skip_qa`、内容幂等、future dependency 拒绝与 Skill integrity。不存在“是否值得 QA”的额外审美门槛。

## Executor Contract

执行器接收：

```text
canonical_skill: identity / version / sha256
input: canonical fields
context_provenance: PROVIDED / DERIVED_SAFELY / UNKNOWN
runtime: invocation_id / contract_version
```

执行器输出至少包含：`decision`、`severity`、`route`、`mode`、`context_state`。Runtime 只验证枚举和结构，不验证 Severity 与 Decision 是否“合理”。

## Seven-State Runtime Mapping

|Canonical Skill State|Runtime Action|文本处理|
|---|---|---|
|`PASS / NO CHANGE`|`pass_through`|原文原样成功返回|
|`PASS WITH NOTES`|`return_diagnostic`|原文返回，附 Skill diagnostics|
|`RETURN FOR LANGUAGE REVISION`|`return_diagnostic`|原文返回，不擅自改写|
|`NEEDS CONTEXT`|`request_context`|原文返回，请求 Skill 指定的最少 Context|
|`ROLE HANDOFF / WARNING`|`handoff`|原文与 handoff 原样返回|
|`REWRITE DELIVERED`|`accepted_rewrite`|仅在全部 rewrite transport guards 通过后采用 revised text|
|`BLOCKED`|`safe_stop`|原文保留，停止下游替换|

映射是 `7 / 7` 一对一；transport failure / skipped / dependency metadata 不是第八个 Skill state。

## Rewrite Transport Guards

`REWRITE DELIVERED` 仅在输入为 `REWRITE_EXPLICIT` 且 Skill 输出同时报告以下字段时采用：`revised_text`、`benefit_result: PASS`、非空 `rewrite_scope`、`meaning_lock_status: PASS|LOCKED`、`rewrite_ceiling_status: PASS`、九项 `safety_regression` 全部 PASS。Runtime 不自行执行 Meaning、Benefit 或 Safety 判断，只忠实检查 Skill 已报告的 contract flags。任一缺失/失败均为 F6，保留原文。

## Contemporary Handoff

当 Skill 的唯一主状态为 `ROLE HANDOFF / WARNING` 且报告 `CONTEMPORARY USAGE CHECK REQUIRED`，Runtime 保留主状态，并增加 transport metadata：`HANDOFF_REQUIRED / CONTEMPORARY_LAYER_NOT_AVAILABLE`。不得联网、不得调用或创建未来 Layer。

## Failure Model

F1 Invalid Input；F2 Insufficient Required Data；F3 Skill Invocation Failure；F4 Malformed Skill Output；F5 State Contract Violation；F6 Rewrite Contract Violation；F7 Unauthorized Future Dependency；F8 Integrity Failure。所有失败均 `FAIL_SAFE`，不得采用 revised text。

## Idempotency / Audit / Output Separation

稳定 input + context + Skill V0.1 生成稳定 invocation key；同一 Runtime 实例重复调用返回首个结果，不重复写日志或累积 diagnostics/handoff/rewrite。审计记录不复制 Original 或 revised text，只记录 identifier、Skill identity/version/hash、mode、context availability、decision、severity、route、rewrite/handoff/contract/failure 状态。

返回值明确分为 `internal_runtime_result`、`downstream_payload`、`user_facing_result` 与脱敏 `audit_record`。
