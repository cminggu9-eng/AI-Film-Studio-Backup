---
type: evidence-design
status: approved
review_result: passed
version: 0.1
subject: Contemporary Language Layer
---

# Contemporary Language Layer V0.1｜Evidence Design

## 最小安全实现

`ContemporaryLanguageRuntime` 接收 caller 注入的 `EvidenceProvider`，而不是自行抓取页面或维护词表。Provider 必须给出可审计的 source id、URL、Tier、独立性组、发表/访问时间、使用种类、立场、地域、平台、Register 观察与语义漂移标签。Layer 只回传结构化摘要，丢弃原始摘录，因此网页中的注入文本不会成为 QA 的上下文指令。

## Evidence Request

`phrase`、`question`、`production_run_id` 为必填；`scope`、`minimal_context`、`protected_context`、`question_type` 与 `as_of` 为最小可选项。整个项目资料、用户画像、帐号、联系人、私人消息与行为历史均拒绝。请求动作只能是 `EVIDENCE_ONLY`。

## Evidence Return

返回 `evidence_status` 与 `current_usage_status`，以及：query、usage observations、temporal status、regional/platform scope、register observation、semantic drift、source summary/tier、confidence、ambiguity、QA handling hint、timestamp/evidence window。它没有 `decision`、`severity`、`revised_text`、替换建议或角色裁决字段。

## Evidence lifecycle

- V0.1 不持久化 cache，也不保存网页或用户资料。
- 每份结果带 `as_of` 和 freshness policy，供 future host 选择何时重取。
- Coordinator 在同一 production run 中按 claim fingerprint 限制一次完整 cycle；新 Context、用户明确复核或 evidence window 变化才能例外重查。
- `NO_RELIABLE_EVIDENCE_FOUND` 是未知状态，不是“不存在”或“应修改”。

## Handoff mapping

只在 `ROLE HANDOFF / WARNING + CONTEMPORARY USAGE CHECK REQUIRED` 的精确组合后进入。Coordinator 把 Evidence Return 放入 `Available Context` 后调用 QA；第二次 QA 的结果不被本层解释、重写或覆盖。

