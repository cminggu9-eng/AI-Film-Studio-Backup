# Art Director unresolved_decisions Contract Alignment V0.1

Date: 2026-08-31  
Result: ALIGNED

## Authoritative machine contract

- Field presence: required.
- Type: array of non-empty strings or exact `ABSENT`.
- Lawful empty representation: `[]`.
- Lawful absence representation: exact `ABSENT`.
- Semantic purpose: carry actual unresolved owner decisions without inventing them.
- Downstream behavior: preserve the supplied representation; no automatic decision or content synthesis.
- Production feasibility: conditional, not universally mandatory.

## Validation outcomes

| Input | Result |
|---|---:|
| `[]` | PASS |
| `ABSENT` | PASS |
| non-empty array of strings | PASS |
| wrong type | FAIL-CLOSED |
| missing top-level field | FAIL-CLOSED |
| invalid field plus production-rich prose | FAIL-CLOSED |

The validator no longer requires a non-empty unresolved issue and no longer searches production-related keywords as substitute structural evidence.

