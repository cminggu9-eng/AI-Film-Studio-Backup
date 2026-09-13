# TR-SW-01–20 Test Report V0.1

## Latest status

| Group | Result |
|---|---:|
| TR-SW-01–16 | 16 / 16 PASS |
| TR-SW-17 Known Bad Replay | FAIL |
| TR-SW-18 Clean Replay | FAIL |
| TR-SW-19–20 | 2 / 2 PASS |
| Latest total | 18 / 20 PASS |

The required gate is `20 / 20 PASS`; it was not reached.

## Attempt evidence

- `Scene_Writer_Targeted_Repair_TR_SW_Results_V0.1.json`: 16 / 20; F03 remained a verifier false negative; four clean replays passed.
- `...Attempt_2_V0.1.json`: 19 / 20; static cases repaired, F03 still a verifier false negative; four clean replays passed.
- `...Attempt_3_V0.1.json`: 18 / 20; claim-audit F03 still passed; first clean replay returned invalid provider JSON.
- `...Attempt_4_V0.1.json`: 18 / 20; audit evidence shows F03's unsupported clause was omitted from the audit; first clean replay returned invalid provider JSON.
- `...Attempt_5_V0.1.json`: 18 / 20; exhaustive candidate coverage caused non-JSON provider responses in both replay groups.

TR-SW-19 confirms the implementation contains no regex/synonym semantic classifier. TR-SW-20 confirms canonical SHA-256 is unchanged.
