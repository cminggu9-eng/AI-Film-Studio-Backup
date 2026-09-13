# Showrunner Response Budget Provenance Audit

`3500` came from `CanonicalRoleExecutor.invoke()`'s generic no-override fallback. It was not defined by the Showrunner Skill, DeepSeek adapter, or a role override. Repair 10 removes that fallback path and resolves a runtime-owned role policy.
