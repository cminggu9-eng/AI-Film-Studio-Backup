---
type: systemic-hardening-phase-2-selected-scope
status: completed-scope
version: 0.1
---

# AI Film Studio Systemic Hardening Phase 2 Selected Scope V0.1

## Source-of-truth selection

| Backlog ID | Priority | Original failure evidence | Layer | Why now | Exact repair boundary | Closure regression |
| --- | --- | --- | --- | --- | --- | --- |
| SH-P0-01 | P0 | Phase 1 matrix: no independently named Provider-Free Startup gate | A / I | importing/starting runtime must remain zero-call | explicit boundary validator plus named startup and Gate entry | `Provider-Free Startup`, `Minimal Harness Startup`, `REL-01`–`04` |
| SH-P0-02 | P0 | Rerun 01 provider-accounting correction | A / I | manifest/provider/ledger disagreement must be detectable before future reliability claims | lifecycle consistency validator: run ID, call counts, invocation IDs, custody links, handoffs, ledger | `REL-05`–`08`; Golden recorded regression |
| SH-P1-01 | P1 | Rerun 04 evidence-root hygiene failure | I | future runs need one unambiguous root, not a nested alias | canonical run-local absolute root and authorization boundary | `REL-01`–`04`, `REL-07` |
| SH-P1-02 | P1 | Repair 03 Beta strict transport was controlled-path only | C | strict transport must stay Scene Writer adapter-scoped | recorded lifecycle check isolates the one strict Scene Writer call; retry/fallback prohibited | `STRICT 15/15`, `REL-09` |
| SH-P1-03 | P1 | Rerun 01/02 Showrunner ownership failures | F | absence transport cannot create semantic fields | retain and package ownership regression in the unified gate | `SHOWRUNNER-OWN 10/10` |

P2/P3 items were not selected. No role capability, Canonical Skill semantics, Capability Model, Nuwa, creative quality, media, database/RAG, or Human Acceptance work entered this phase.

