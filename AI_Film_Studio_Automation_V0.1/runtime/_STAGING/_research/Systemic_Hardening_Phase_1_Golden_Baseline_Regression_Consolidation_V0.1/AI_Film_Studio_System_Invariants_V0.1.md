---
type: system-invariants
status: proposed-hardening-guardrails
version: 0.1
---

# AI Film Studio System Invariants V0.1

These invariants are runtime hardening guardrails derived from the recorded lineage. They do not amend Canonical Skills or Production Locks.

1. `ROLE OWNS SEMANTICS`
2. `TRANSPORT OWNS TRANSPORT`
3. `TRANSPORT MAY REPRESENT ABSENCE BUT MAY NOT INVENT ROLE SEMANTICS`
4. `DISPLAY HEADING != MACHINE IDENTITY`
5. `MACHINE TOKEN != DISPLAY PROSE`
6. `RAW PROVIDER EVIDENCE MUST PERSIST BEFORE VALIDATION`
7. `CANONICAL TOKENS MUST NOT BE TRANSLATED OR COLLAPSED`
8. `SEMANTIC FAILURE != STRUCTURAL FAILURE`
9. `STRUCTURAL FAILURE != TRANSPORT FAILURE`
10. `NO SILENT REPAIR`
11. `NO AUTOMATIC PROVIDER FALLBACK`
12. `CONTINUITY DETECTS / ROUTES BUT DOES NOT REPAIR`
13. `SHARED QA DEFAULTS TO NON-REWRITE`

## Operational interpretation

| Invariant family | Required behavior |
| --- | --- |
| Ownership | Role-originated semantic material is validated, attributed, and handed off; an adapter may only emit expressly-owned transport fields or absence sentinels. |
| Representation | Parse actual required semantic fields and canonical tokens. Never require historical display aliases unless the role contract itself declares them. |
| Custody | Persist raw response, invocation metadata, usage, and persistence verification before parse/validation/truncation decisions. |
| Failure handling | Classify the earliest failing layer; stop with evidence. No JSON repair, heading insertion, semantic mutation, resample, retry, or fallback is implicit. |
| Downstream review | Continuity flags/routes rather than repairs. Shared QA can return `PASS`, `FLAG`, `BLOCK`, or `HANDOFF`, and does not rewrite creative output by default. |

## Enforcement boundary

Any proposed exception must name its owner, representation, evidence, and new regression. An undocumented exception is a failure, not a compatibility mode.

