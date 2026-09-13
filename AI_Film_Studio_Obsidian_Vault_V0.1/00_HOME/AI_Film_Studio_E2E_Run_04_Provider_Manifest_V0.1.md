---
type: e2e-run-04-provider-manifest
status: blocked-awaiting-user-review
version: 0.1
date: 2026-08-28
---

# AI Film Studio E2E Run 04 Provider Manifest V0.1

| Role | Invocation | Contract result | Prompt / completion / total tokens | Estimated CNY |
| --- | --- | --- | --- | --- |
| Showrunner | `E2E-RUN-04:showrunner:1` | PASS | 4,916 / 1,894 / 6,810 | 0.0253504 |
| Scene Writer | `E2E-RUN-04:scene_writer:1` | PASS | 7,984 / 1,316 / 9,300 | 0.0204240 |
| Director | `E2E-RUN-04:director:1` | PASS | 10,268 / 1,440 / 11,708 | 0.0394440 |
| Character & Acting | `E2E-RUN-04:character_acting:1` | PASS | 9,647 / 1,279 / 10,926 | 0.0366150 |
| Art Director | `E2E-RUN-04:art_director:1` | Parser gate BLOCKED after persistence | 15,381 / 1,609 / 16,990 | 0.0557970 |

Total: 5 calls; 48,196 prompt tokens; 7,538 completion tokens; 55,734 total tokens; estimated CNY `0.1776304`.

Each call has raw response, usage/invocation metadata, finish reason, transport metadata, and persistence verification recorded before local validation. All completed with `finish_reason: stop` except Scene Writer’s expected forced-function `tool_calls`; no response was truncated.
