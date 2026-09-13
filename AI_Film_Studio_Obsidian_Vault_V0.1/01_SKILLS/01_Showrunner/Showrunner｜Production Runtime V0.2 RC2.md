---
type: runtime-qa
status: locked
review_result: passed
version: 0.2-rc2
subject: AI Film Studio Showrunner Production Runtime
production_lock: locked
---

# AI Film Studio Showrunner｜Production Runtime V0.2 RC2

## Scope and freeze

- Showrunner Capability Model: unchanged.
- Canonical `SKILL.md`: unchanged.
- Installed `ai-film-studio-showrunner/SKILL.md`: unchanged.
- Canonical and installed SHA-256: `13180590744CBFDF930A66D3D35414B2667B7D345FF564D25B71361235C0C750`.
- This document records Runtime Layer RC2, not Showrunner Skill V0.2.

## RC2 runtime changes

1. `showrunner_role_router.py` now uses intent priority: Canon conflict → role boundary → diagnosis → production scope → format fit → series development → generic Showrunner.
2. Chinese format/series synonyms now include continuous comic/short drama, series comic/short drama, long-form serial story, multi-episode story, capacity, and sustainable-update queries.
3. Router output carries an executable boundary contract. Director and acting outputs are checked for prohibited micro-direction before delivery.
4. Anti-Mechanical checking is sentence-scoped: universal cadence, episode quota, unqualified numeric structure, fixed Continuing Drive, and approximate cadence are rejected unless the same sentence is explicitly project-specific and conditional.
5. `runtime_pipeline.py` connects Router → Candidate V1 → Gate V1 → optional Candidate V2 → Gate V2 → final delivery status, with a complete auditable record.
6. `runtime/_TEST_SANDBOX/<test-id>/<timestamp>/` isolates test canon, project state, logs, and temporary outputs from the formal Vault.

## Regression results

`python -X utf8 scripts/test_showrunner_compliance_gate.py`

- 18/18 PASS.
- Router intent-priority and synonym matrix: PASS.
- Director boundary reject/allow pair: PASS.
- Acting boundary reject/allow pair: PASS.
- Historical BB-07 plus RC2 cadence/Continuing Drive fixtures: all rejected.
- Project-specific heuristic, quiet ending, and light-genre candidate options: PASS.
- Receipt completeness, one-correction recovery, fail-safe block, sandbox isolation, and hash freeze: PASS.
- FINAL-BB-01 through FINAL-BB-10 deterministic runtime regression: 10/10 PASS.

`scripts/test_showrunner_runtime_e2e.py --case RT-07-1|2|3`

- RT-07-1, RT-07-2, RT-07-3: each records `GATE_RECOVERED` after one correction inside its own sandbox.

## BB-06 artifact audit

`03_PROJECTS/Project-001/林舟｜人物正史.md` was created during the prior FINAL-BB-06 run. Its creation time aligns with that test period, its contents contain only the test canon, and no project narrative or other canon document references it. This RC2 audit note is the sole system-level reference. Classification: `TEST ARTIFACT CONFIRMED`.

RC2 does not delete or archive it. User authorization is required for either action.

## Status

Production Lock was explicitly authorized on 2026-08-22. Runtime V0.2 RC2 is the formal production runtime bound to Showrunner Skill V0.1:

`Orchestrator → Explicit Role Router → ai-film-studio-showrunner → Runtime Compliance Gate → Final Output`

Formal AI Film Studio Showrunner work must not bypass this runtime chain. `FINAL CREATIVE AUTHORITY = USER`.
