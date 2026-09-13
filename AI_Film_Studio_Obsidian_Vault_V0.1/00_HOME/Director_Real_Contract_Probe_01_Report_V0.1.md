---
type: director-real-contract-probe-report
status: complete-awaiting-user-review
version: 0.1
date: 2026-08-28
---

# Director Real Contract Probe 01 Report V0.1

## Eligibility and execution

The probe was eligible because provenance was complete, DIR-INT was `12/12 PASS`, and static evidence could not prove a live Provider would honor the exact canonical heading order. It used only the frozen successful Rerun 03 Showrunner package, Scene Writer package, State & Evidence envelopes, and ledger.

| Boundary | Result |
| --- | --- |
| Provider calls | `1 / 1` Director-only call |
| Invocation | `DIRECTOR-CONTRACT-PROBE-01:director:1` |
| Model | `deepseek-v4-pro` |
| Retries / fallbacks | `0 / 0` |
| Showrunner / Scene Writer / downstream calls | `0 / 0 / 0` |
| Full E2E reruns | `0` |
| Raw response SHA-256 | `8408fd7bff7f6901c0c6ebdb57ad944a6f82e4c5fa492b6d44b599caa83b4f97` |
| Usage | 10,621 prompt + 1,999 completion = 12,620 tokens; estimated CNY `0.043857` |

## Acceptance

The initial generated record is preserved at `.../director_real_contract_probe_01.json`. Its post-execution observer used an overly broad acting-method keyword and read usage from the wrong persistence artifact, producing an initial `14/16` result. No Provider call was repeated.

The provider-free post-execution acceptance review reads the same persisted raw response and invocation metadata, corrects only those two observer assertions, and passes **16 / 16**. A lawful future `Character & Acting` handoff is not a Director acting-method takeover; usage is correctly read from `director_invocation.json`.

Evidence root:

`runtime/_STAGING/_research/E2E_Targeted_Repair_05_Director_Output_Contract_Transport_Alignment_V0.1/evidence/DIRECTOR-CONTRACT-PROBE-01`

The Probe output has all eight headings in canonical order, exact `PLAN` and `DIRECTION_PLAN_PRODUCED`, unchanged locks/prohibitions, `ABSENT` scene packages, a valid State & Evidence handoff, and persisted raw/usage evidence before validation. No creative output was auto-repaired.
