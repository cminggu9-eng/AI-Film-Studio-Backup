---
type: systemic-failure-lineage
status: evidence-bounded
version: 0.1
---

# AI Film Studio Systemic Failure Lineage V0.1

## Classification rule

This register preserves each original blocking label and adds a corrected classification only where a later repair supplied direct evidence. A reclassification never asserts that a role's creative semantics were repaired when the repair was transport, parser, or ownership-only.

| Category | Meaning | Evidence position in this Phase |
| --- | --- | --- |
| A | persistence/evidence | Repair 01 and Golden raw-before-validate custody |
| B | role output contract | Scene Writer, Director, and Art Director output boundaries |
| C | structured transport | Repair 03 strict function transport |
| D | canonical token integrity | Repair 03A token alignment |
| E | response budget/serialization | Repair 01/02 probe sequence |
| F | transport ownership | Rerun 01/02 and Repair 04 |
| G | parser/presentation separation | Rerun 03/04 and Repair 05/06 |
| H | state/continuity transport | Golden append-only ledger and envelopes |
| I | metadata/evidence-root hygiene | Rerun 04 custody issue / Rerun 05 root policy |
| J | semantic safeguard | Golden deterministic evidence gate and no-rewrite boundary |

| Failure ID | First observed | Role / layer | Symptom | Original → corrected classification | Corrective evidence / regression | Status |
| --- | --- | --- | --- | --- | --- | --- |
| FL-01 | Rerun 01 | Showrunner → Scene Writer handoff | Showrunner supplied `scene_packages`, although that field is Scene Writer-owned | `HANDOFF CONTRACT FAILURE` → `F TRANSPORT OWNERSHIP` | Repair 04 ownership tests `10/10`; transport separates role semantics from the lawful absence sentinel | Controlled in Golden path |
| FL-02 | Rerun 02 | Showrunner → Scene Writer transport | valid role content lacked integration `scene_packages` slot | `EXECUTOR FAILURE` → `F TRANSPORT OWNERSHIP` | Repair 04 ownership tests `10/10`; adapter may add only `scene_packages: ABSENT` | Controlled in Golden path |
| FL-03 | Rerun 03 | Director parser / presentation | required role-output heading rejected because historical parser expected a different structural sequence | `ROLE SEMANTIC FAILURE` → `MIXED STRUCTURAL + TRANSPORT FAILURE` | Repair 05 `DIR-INT 12/12`; recorded Director probe `16/16` | Controlled in Golden path |
| FL-04 | Rerun 04 | Art Director parser / presentation | minimum-sufficient Chinese records rejected for missing historical English aliases | `ROLE SEMANTIC FAILURE` → `G TRANSPORT / PARSER CONTRACT FAILURE` | Repair 06 Art Director contract `12/12`; recorded reassessment `8/8`; no heading insertion | Controlled in Golden path |
| FL-05 | Repair 01 / 02 probes | Scene Writer response transport | first probe truncated before parse; second was complete but strict JSON had an unescaped control character | evidence progression → `E RESPONSE BUDGET / SERIALIZATION`, then `C STRICT STRUCTURED TRANSPORT` | Repair 01 PERSIST `8/8`; Repair 02 SER `12/12`, TRUNC `4/4`; Repair 03 STRICT `15/15`, Probe03 `17/17` | Controlled only on strict adapter path |
| FL-06 | Repair 03A audit | Scene Writer canonical token transport | non-canonical `NEEDS_DECISION` / noncanonical flags-handoffs could collapse role meaning | token-contract defect → `D CANONICAL TOKEN INTEGRITY` | Repair 03A TOKEN `10/10`, STRICT `15/15`, SW-INT `15/15`, recorded regression `5/5` | Controlled in Golden path |
| FL-07 | Rerun 04 custody review | Evidence-root lifecycle | prior evidence layout permitted nonstandard staging nesting | evidence-hygiene defect → `I METADATA / EVIDENCE-ROOT HYGIENE` | Rerun 05 `SINGLE_CANONICAL_PATH_NO_STAGE_RENESTING`, persisted authorization/manifest before calls | Controlled in Golden path; keep static guard |

## Repair lineage

| Repair | Narrow contribution | Boundary retained |
| --- | --- | --- |
| Repair 01 | raw persistence before parse; state/display split; six-field Scene Writer delivery | probe revealed response truncation; no rerun |
| Repair 02 | bounded response budget, compact lossless normalization, truncation detection | strict JSON defect remained; no auto-repair |
| Repair 03 | strict function transport and recorded wire custody | beta provider feature is controlled-path only |
| Repair 03A | canonical primary state / flags / handoffs alignment | `ABSENT` remains transport absence, not a semantic token |
| Repair 04 | Showrunner transport ownership separation | adapter cannot invent semantic content |
| Repair 05 | Director structural contract alignment | canonical structural order, no creative repair |
| Repair 06 | Art Director minimum-sufficient parser alignment | display headings not required for machine identity |

The lineage deliberately excludes deferred evidence gaps from “fixed” status. Those remain backlog items until separately authorized and evidenced.
