# AI Film Studio E2E Run 01 Provider Manifest V0.1

## Bounded recovery calls

| # | Role | Invocation ID | Timestamp UTC | Result | Tokens | Estimated cost |
| --- | --- | --- | --- | --- | --- |
| 1 | Showrunner | `E2E-RUN-01:showrunner:1` | 2026-08-26T09:36:04.841198+00:00 | Provider / role contract PASS | 4,947 in / 1,335 out / 6,282 total | CNY 0.022851 |
| 2 | Scene Writer | `E2E-RUN-01:scene_writer:1` | 2026-08-26T09:36:33.295422+00:00 | Provider / structural role contract PASS; semantic gate BLOCK | 5,709 in / 2,393 out / 8,102 total | CNY 0.031485 |

| Accounting field | Result |
| --- | --- |
| Recovery provider calls | 2 |
| Recovery known tokens | 10,656 input / 3,728 output / 14,384 total |
| Recovery estimated total cost | CNY 0.054336 |
| Initial technical attempt | 1 real Showrunner request; token and cost telemetry unavailable because the former runner failed before persistence |
| Total actual Provider calls for the authorization | 3 |
| Retries | 0 |
| Automatic fallback | 0 |

Structured per-call evidence is retained in `provider_manifest.json`. The initial-attempt accounting correction is retained separately and is not represented as invented token or cost data.
