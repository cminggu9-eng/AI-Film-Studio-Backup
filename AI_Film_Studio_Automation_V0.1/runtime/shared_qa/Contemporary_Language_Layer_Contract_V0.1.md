---
type: runtime-contract
status: approved
review_result: passed
version: 0.1
subject: Contemporary Language Layer
---

# Contemporary Language Layer V0.1｜Runtime Contract

## Boundary

`LAYER PROVIDES EVIDENCE. QA MAKES DECISION.` The Layer has no final QA state, Severity, Rewrite authority, replacement text, character judgment, Canon authority, trend score or role-routing authority.

## Fixed sequence

```text
language-voice-qa
  → ROLE HANDOFF / WARNING + CONTEMPORARY USAGE CHECK REQUIRED
  → Contemporary Handoff Coordinator
  → Contemporary Evidence Runtime
  → Contemporary Evidence Return (Available Context)
  → language-voice-qa
  → Final QA Decision
```

The coordinator only accepts that exact pre-existing Handoff combination. It calls QA again but never interprets or replaces the second QA result.

## Request and response

Required request fields: `phrase`, `question`, `production_run_id`; optional bounded fields: `question_type`, `scope`, `minimal_context`, `protected_context`, `as_of`. `requested_action` must be `EVIDENCE_ONLY`.

Evidence Return always provides: query; evidence status; current-usage status; structured usage observations; temporal status; separate regional/platform scope; register observation; semantic-drift status; source summary and quality tier; explicit confidence; ambiguity; non-decisional QA handling hint; timestamp; and evidence window. It returns neither external source text nor a rewrite candidate.

## Evidence statuses and confidence

`EVIDENCE_AVAILABLE`, `EVIDENCE_CONFLICT`, `NO_RELIABLE_EVIDENCE_FOUND`, and `INSUFFICIENT_CURRENT_EVIDENCE` are evidence-transport statuses, not canonical QA states. Confidence is `High`, `Medium`, `Low`, or `Insufficient` and is computed from source tier, count, independence, freshness, natural-use support, scope and conflict.

## Recheck, caching and safety

There is no persistent V0.1 cache. Every response records the evidence window. In one coordinator instance, a claim may receive one full cycle per production run; only `NEW_CONTEXT`, `USER_REVERIFY`, or `EVIDENCE_WINDOW_CHANGED` may justify another.

The adapter accepts external material as data only. It rejects prohibited personal-data fields and non-evidence actions, omits raw snippets from the QA return, and never stores external pages, user profiles or private information.
