---
type: deferred-hardening-register
status: active-deferred
version: 0.1
revisit_trigger: AI FILM STUDIO INTEGRATION VALIDATION / HARDENING
---

# Scene Writer Deferred Hardening Register V0.1

This register preserves defects and uncertainty without assigning responsibility to roles that have not yet been built. “Potential Related Future Role” denotes possible interaction only.

| Issue ID | Category | Evidence | Severity | Current Ownership | Potential Related Future Role | Why Deferred | Revisit Trigger |
|---|---|---|---|---|---|---|---|
| SW-DH-01 | Unsupported Micro-Fact Injection | Full validation F03 / F10 / F14; related Smoke human reviews; verifier returned PASS for the three validated cases | High | Scene Writer Runtime semantic enforcement; Executor / Provider adherence are contributing factors | Scene Writer, Continuity, Runtime, Executor, Provider, Orchestration | Requires cross-role production evidence before broadening semantic policy; no repair is authorized in this phase | AI FILM STUDIO INTEGRATION VALIDATION / HARDENING |
| SW-DH-02 | Character Knowledge Timing | Full validation F09 information-timing failure; assignment fact / knowledge lock human review | High | Scene Writer Runtime constraint projection and Executor adherence | Scene Writer, Continuity, Runtime, Executor, Provider, Orchestration | Needs future integration evidence to separate scene-local knowledge enforcement from continuity-owned history | AI FILM STUDIO INTEGRATION VALIDATION / HARDENING |
| SW-DH-03 | Non-`CREATE` State Reliability | Full validation structured-output failures F06, F11, F12, F13-A, F13-B; no approved real semantic coverage for all non-`CREATE` states | High | Scene Writer Runtime / Executor prompt construction | Scene Writer, Runtime, Executor, Provider, Orchestration | No targeted rerun or further repair is authorized; future chain tests must establish state-specific evidence | AI FILM STUDIO INTEGRATION VALIDATION / HARDENING |
| SW-DH-04 | Semantic Verifier Reliability | Full validation verifier matrix: false-negative evidence; Targeted Repair final review: F03 remains missed and exhaustive coverage produced non-JSON provider response; `TR-SW 18 / 20` | Critical | Scene Writer Runtime semantic verifier architecture; Provider response reliability is contributing | Scene Writer, Runtime, Executor, Provider, Orchestration | The verifier cannot be promoted as the sole semantic gate. Architecture decision is deliberately deferred to systemic hardening | AI FILM STUDIO INTEGRATION VALIDATION / HARDENING |
| SW-DH-05 | Test-Harness Import Side Effect | Targeted Repair task / cost record: importing the legacy Smoke runner triggered an unplanned provider generation; result was FAIL_SAFE and historical evidence was not overwritten | High | Scene Writer Integration Test Harness | Runtime, Executor, Provider, Orchestration | **TECHNICAL DEBT / MUST FIX BEFORE FUTURE REAL INTEGRATION TESTING.** This checkpoint only records it; it does not repair code | AI FILM STUDIO INTEGRATION VALIDATION / HARDENING |

## Guardrails while deferred

- No row is a production-readiness waiver.
- No future role is assigned blame or authority by this register.
- Existing Staging and Vault evidence remains the source of record.
