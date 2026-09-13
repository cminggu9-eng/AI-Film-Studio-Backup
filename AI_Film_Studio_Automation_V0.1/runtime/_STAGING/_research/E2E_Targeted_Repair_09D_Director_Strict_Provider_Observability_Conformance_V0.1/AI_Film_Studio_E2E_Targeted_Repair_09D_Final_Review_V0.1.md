---
type: e2e-targeted-repair-09d-final-review
status: awaiting-user-review
recommendation: director-strict-provider-targeted-compatibility-repair-required
version: 0.1
---

# AI Film Studio E2E Targeted Repair 09D Final Review V0.1

## Outcome

**DIRECTOR STRICT PROVIDER TARGETED COMPATIBILITY REPAIR REQUIRED**

Repair 09D closes the historical observability gap: its one authorized Director-only probe persisted final redacted wire evidence before sending and raw/parsed Provider error evidence before classification. The real DeepSeek error pinpoints a schema-structure defect; no further request was sent.

## Exact next repair boundary

1. Update the DeepSeek-only `const`/fixed-string projection to output `type: string` with `enum`.
2. Add a recursive linter rule that rejects every schema node without `type`, `anyOf`, or `$ref`, and report the live Provider requirement explicitly.
3. Update equivalence assertions for typed fixed strings; rerun the 16 offline checks, Repair 09B validator chain, and Unified Phase 2 gate.
4. Only after a new explicit authorization, send one fresh Director-only probe with the existing observability capture.

## Explicitly not done

No R01/R02/R03 run, no retry, no fallback, no free-form mode, no `strict: false`, no canonical-Skill mutation, no semantic field removal, and no production-lock mutation.

## Final stop

AI FILM STUDIO E2E TARGETED REPAIR 09D COMPLETE — AWAITING USER REVIEW.

