---
type: systemic-regression-matrix
status: baseline-consolidated
version: 0.1
---

# AI Film Studio Systemic Regression Matrix V0.1

## Tier policy

| Tier | Scope | When required |
| --- | --- | --- |
| Tier 1 | static and provider-free contract checks | every runtime modification |
| Tier 2 | recorded-response transport, parser, schema, token, truncation, and custody checks | any transport/parser/schema change |
| Tier 3 | real E2E against frozen fixture and call budget | only when cross-role runtime, executor, provider, or state transport materially changes |

## Matrix

| Test | Owner | Layer | Failure prevents | Current status | Tier / frequency |
| --- | --- | --- | --- | --- | --- |
| `PERSIST` | Runtime custody | A persistence/evidence | validation before raw evidence custody | `8/8 PASS` (Repair 01) | T1, every runtime change |
| `STATE` | Runtime state envelope | H state/continuity transport | state/display conflation or unordered state record | baseline observed: ledger append-only `3` entries | T1, every state-envelope change |
| `SEM` | Semantic safeguard | J semantic safeguard | silent semantic rewrite or verifier-as-sole-gate | Golden `PASS`; rewrite `PROHIBITED` | T1, every safeguard change |
| `SW-INT` | Scene Writer contract | B/C/D | invalid six-field package or token drift reaching downstream | `15/15 PASS` | T1, every Scene Writer runtime change |
| `SER` | Scene Writer transport | E serialization | lossy compact normalization / invalid serial form | `12/12 PASS` | T1, every serialization change |
| `TRUNC` | Scene Writer transport | E truncation | truncated response accepted as complete | `4/4 PASS` | T1, every response-budget change |
| `STRICT` | Scene Writer strict adapter | C structured transport | malformed/ordinary-content reply accepted in strict path | `15/15 PASS`; beta path scoped | T1+T2, every strict-adapter change |
| `TOKEN` | Canonical token contract | D token integrity | canonical modes/states/flags/handoffs translated or collapsed | `10/10 PASS` | T1+T2, every token/schema change |
| `OWN` | Showrunner hydration | F transport ownership | adapter/Showrunner creating Scene Writer semantics | `10/10 PASS` | T1+T2, every handoff adapter change |
| `DIR-INT` | Director contract | B/G | wrong structural order or display/parser mismatch | `12/12 PASS` | T1+T2, every Director parser/contract change |
| `AD-INT` | Art Director contract | B/G | minimum-sufficient Art Director record rejected for absent legacy headings | `12/12 PASS` | T1+T2, every Art Director parser/contract change |
| `AD-RERUN04` | Art Director recorded reassessment | G presentation separation | historical record altered or semantically “repaired” during reassessment | `8/8 PASS` | T2, every Art Director parser change |
| `Provider-Free Startup` | Runtime launcher | A/I | local startup invokes provider or writes outside declared evidence root | no independently named suite yet; admission criterion defined below | T1, must be added before Phase 2 runtime expansion |
| `E2E-INT-01`–`18` | Minimal E2E harness | cross-role | end-to-end handoff, state, semantic, provider custody regressions | Golden `18/18 PASS` | T3, only material cross-role/executor/provider/state-transport change |

## Admission and escalation

- A T1/T2 failure blocks Tier 3; no real call is used to diagnose a failing provider-free/recorded regression.
- A `Provider-Free Startup` test must assert zero provider calls, no retry/fallback, no canonical/lock mutation, and one declared evidence root. It is backlog work, not retroactively claimed as passed.
- Tier 3 retains the Golden fixture, seven-call cap, zero recovery budget, raw-before-validate custody, and explicit user authorization. Tier 3 does not start automatically.

