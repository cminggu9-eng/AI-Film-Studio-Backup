# Scene Writer Canonical Token Test Report V0.1

## Result

`TOKEN-01 through TOKEN-10: 10 / 10 PASS`

| Test | Result | Coverage |
| --- | --- | --- |
| TOKEN-01 | PASS | all six exact Primary Decision States |
| TOKEN-02 | PASS | `NEEDS_DECISION` absent |
| TOKEN-03 | PASS | `UPSTREAM_DECISION_REQUIRED` preserved |
| TOKEN-04 | PASS | `REQUEST_OUT_OF_SCOPE` preserved |
| TOKEN-05 | PASS | all seven flags/handoffs accounted |
| TOKEN-06 | PASS | unknown flag rejected |
| TOKEN-07 | PASS | `ABSENT` remains transport-only |
| TOKEN-08 | PASS | recorded CREATE / `SCENE_CREATED` Probe03 path valid |
| TOKEN-09 | PASS | E2E-INT-12 exact source-mode / state / flags / handoffs preservation |
| TOKEN-10 | PASS | canonical Skill hash unchanged |

## Required regressions

| Suite | Result |
| --- | --- |
| Strict structured transport | 15 / 15 PASS |
| Scene Writer Integration Contract | 15 / 15 PASS |
| Probe03 recorded-response regression | 5 / 5 PASS |

All are static or read-only recorded-response checks. Provider Calls: 0. Executor Calls: 0. Probe03 reruns: 0. JSON Auto-Repairs: 0.
