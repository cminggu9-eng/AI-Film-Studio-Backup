# AI Film Studio E2E Run 01 Execution Manifest V0.1

| Item | Result |
| --- | --- |
| Run ID | E2E-RUN-01 |
| Recovery evidence root | E2E-RUN-01-RECOVERY-01 |
| Status | BLOCKED — terminal for this authorization |
| Fixture | E2E-FIX-01; source SHA-256 `72e62b3443b1e7d4d244c8c710344ba5d5a7f3e71d28e808057d5f0e8cb3b41a` |
| Provider / model | DeepSeek / deepseek-v4-pro |
| Primary-role calls in recovery | 2 of 7 |
| Total actual Provider calls across the authorization | 3 (initial technical attempt 1 + bounded recovery 2) |
| Retries | 0 |
| Automatic Provider fallback | 0 |
| Recovery attempts used | 1 of 1 |
| Semantic reruns after BLOCK | 0 |

The recovery ran only because the initial Showrunner response was not recorded before a technical post-response role-contract persistence failure. Its corrected accounting is retained in the sibling `E2E-RUN-01/Initial_Attempt_Provider_Accounting_Correction_V0.1.md` record.
