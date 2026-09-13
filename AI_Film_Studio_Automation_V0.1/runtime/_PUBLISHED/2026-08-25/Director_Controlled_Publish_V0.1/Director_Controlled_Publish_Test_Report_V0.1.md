---
type: controlled-publish-test-report
status: passed-awaiting-user-review
version: 0.1
subject: Director Controlled Publish
provider_calls: 0
---

# Director Controlled Publish Test Report V0.1

## Results

| Test | Result | Evidence |
| --- | --- | --- |
| PUB-DIR-01 | PASS | Approved staging `director/SKILL.md` exists. |
| PUB-DIR-02 | PASS | Canonical top-level identity is `name: director`. |
| PUB-DIR-03 | PASS | Canonical package validator returns `Skill is valid!`. |
| PUB-DIR-04 | PASS | Vault canonical package, manifest, and production lock exist. |
| PUB-DIR-05 | PASS | Approved staging and Vault canonical SHA-256 equal the frozen baseline. |
| PUB-DIR-06 | PASS | Controlled archive SHA-256 equals the frozen baseline. |
| PUB-DIR-07 | PASS | Zip entry `director/SKILL.md` SHA-256 equals baseline; zip contains only package and Manifest. |
| PUB-DIR-08 | PASS | Vault canonical `director/` contains only `SKILL.md`. |
| PUB-DIR-09 | PASS | Canonical, archive, and Manifest secret scan is clean. |
| PUB-DIR-10 | PASS | DR-C14 remains `NO EVIDENCE / NOT DISTILLABLE`. |
| PUB-DIR-11 | PASS | DR-C20 remains `DEFERRED`. |
| PUB-DIR-12 | PASS | No Director Runtime assets were created. |
| PUB-DIR-13 | PASS | No executor binding or global/user-level Skill installation was created. |
| PUB-DIR-14 | PASS | No Provider, DeepSeek, or OpenAI invocation occurred. |
| PUB-DIR-15 | PASS | Director is explicitly not Production Ready; project roadmap marks Character & Acting as `NEXT` only. |

## Hash Equality

```text
APPROVED_STAGING_SHA256 = 807D5B398A247A69C3F54FB58F256E8E87AE3B245540071A8B3F6832B49A7781
VAULT_CANONICAL_SHA256 = 807D5B398A247A69C3F54FB58F256E8E87AE3B245540071A8B3F6832B49A7781
CONTROLLED_ARCHIVE_SHA256 = 807D5B398A247A69C3F54FB58F256E8E87AE3B245540071A8B3F6832B49A7781
ZIP_ENTRY_SHA256 = 807D5B398A247A69C3F54FB58F256E8E87AE3B245540071A8B3F6832B49A7781
```

**Publish Verification: `15 / 15 PASS`.**

## Integrity

- Semantic Mutation: `0`.
- Unauthorized Mutation: `0`.
- Runtime, Executor, Provider, Smoke, real scene direction, Full Semantic Validation, Human Acceptance, and next-role execution: `0`.
