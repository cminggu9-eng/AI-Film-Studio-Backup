---
type: model-usage-cost-report
status: partial-revalidation-stopped
provider: deepseek
model: deepseek-v4-pro
---

# Model Usage & Cost Report V0.1

- Provider / Model: `deepseek` / `deepseek-v4-pro`
- Thinking mode: `disabled`
- Completed real API calls: 13 (1 connection check, 1 Smoke, 10 primary fixtures, 1 C01 callback)
- Successful calls: 13
- Failed provider calls: 0
- Revalidation-only estimated cost: ¥0.052661 (F01–F08, C01 initial+callback, C02 initial)
- SMOKE-EXEC-01 estimated cost: ¥0.024732
- F08 estimated cost: recorded in `executor_revalidation/F08.json` and Human Review Sheet.
- Cache-hit tokens: recorded per invocation in raw revalidation JSON when returned by the provider.

All values are `ESTIMATED`, calculated from returned token usage and DeepSeek V4 Pro public per-1M-token pricing as of 2026-08-24. They are not billing confirmations. API credentials are not present in this report.

## Token Contract Repair Increment

- Incremental real API calls: 8 (C02 repair initial + callback; AV-01–AV-06).
- Incremental input tokens: 54,677.
- Incremental output tokens: 3,367.
- Incremental estimated cost: ¥0.0486682.
- Cumulative known estimated cost: ¥0.1260612 (excludes the minimal connection-check call whose cost was not recorded in the prior report).
- AV-07 and AV-08 made no provider call; they exercised the existing evidence and Runtime safety boundaries.

## Rewrite Output Consistency Gate Increment

- F08-only real rerun: `deepseek` / `deepseek-v4-pro`.
- Input tokens: 7,968; output tokens: 486; cache-hit tokens: 6,528; latency: 8,532 ms.
- Incremental estimated cost: ¥0.0073992.
- Cumulative known estimated cost: ¥0.1334604.
- C02 Human Review Sheet synchronization made no API call.
