# AI Film Studio E2E Run 01 Initial Attempt Provider Accounting Correction V0.1

## Scope

This record corrects call accounting only. It does not alter the fixture, canonical Skills, runtime output, semantic result, or the initial safe-stop decision.

## Confirmed fact

The initial E2E-RUN-01 made one real DeepSeek `deepseek-v4-pro` request for Showrunner. The provider returned JSON successfully. The runner then raised `Only Scene Writer may supply scene_packages` during local post-response role-contract validation before its original persistence path appended the provider call record.

## Corrected accounting

| Item | Result |
| --- | --- |
| Actual provider calls | 1 |
| Provider success | true |
| Role-contract success | false |
| Retry count | 0 |
| Automatic fallback | 0 |
| Failure class | POST_RESPONSE_ROLE_CONTRACT_FAILURE |
| Exact call timestamp | UNAVAILABLE — original runner failed before persistence |
| Token usage / cost | UNAVAILABLE — not fabricated |

The retained input artifact is `artifacts/showrunner_input.json`. No raw response artifact is claimed because the original runner did not save it before failure.

## Recovery classification

This was a technical post-response persistence/validation defect, not a semantic evaluation failure. Under the authorized recovery budget, one bounded technical recovery may proceed. It must not use fallback, retry, fixture mutation, or repeated semantic sampling.
