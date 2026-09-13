---
type: controlled-publish-test-report
role: character-and-acting
status: passed
version: 0.1
---

# Character & Acting Controlled Publish Test Report V0.1

| Test | Result |
| --- | --- |
| PUB-CA-01 approved staging exists | PASS |
| PUB-CA-02 approved staging SHA exact | PASS |
| PUB-CA-03 canonical identity correct | PASS |
| PUB-CA-04 quick_validate PASS | PASS — `Skill is valid!` |
| PUB-CA-05 Vault canonical created correctly | PASS |
| PUB-CA-06 staging / Vault hash equal | PASS |
| PUB-CA-07 archive hash equal | PASS |
| PUB-CA-08 ZIP-entry hash equal | PASS |
| PUB-CA-09 minimal canonical package | PASS — only `character-acting/SKILL.md` |
| PUB-CA-10 no secret leakage | PASS |
| PUB-CA-11 CA-C `21 / 21` preserved | PASS |
| PUB-CA-12 CA-D `18 / 18` preserved | PASS |
| PUB-CA-13 Rules `10 / 10` preserved | PASS |
| PUB-CA-14 Modes `3 / 3` exact | PASS |
| PUB-CA-15 Capability Outcomes `6 / 6` exact | PASS |
| PUB-CA-16 Handoff architecture preserved | PASS |
| PUB-CA-17 CA-C10 gap preserved | PASS |
| PUB-CA-18 CA-C19 no-evidence boundary preserved | PASS |
| PUB-CA-19 CA-C21 deferred preserved | PASS |
| PUB-CA-20 no Nuwa call | PASS — `0` |
| PUB-CA-21 no Runtime asset | PASS |
| PUB-CA-22 no Executor binding | PASS |
| PUB-CA-23 no Provider call | PASS — `0` |
| PUB-CA-24 not marked Production Ready | PASS — `NO` |
| PUB-CA-25 Semantic Mutation = 0 | PASS |

`25 / 25 PASS`. Four-way SHA-256: `CD96A794D37371B855552C23A2670EBD78A9F2E2D3218152CE568C3B4356B09F`.
