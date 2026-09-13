# Preflight Subprocess Environment Isolation Contract V0.1

`build_preflight_subprocess_env(suite_manifest, parent_env)` is the sole projection point for offline preflight children.

1. It starts from an explicit safe-global allowlist.
2. It removes all parent `AFS_E2E_*` variables, including unknown names.
3. It applies only the suite manifest's declared fixture binding.
4. It does not mutate `os.environ` or the parent mapping.
5. It returns the child environment plus redacted provenance and a stable environment hash.

The generic isolation implementation contains no E2E fixture identifiers or story literals.

