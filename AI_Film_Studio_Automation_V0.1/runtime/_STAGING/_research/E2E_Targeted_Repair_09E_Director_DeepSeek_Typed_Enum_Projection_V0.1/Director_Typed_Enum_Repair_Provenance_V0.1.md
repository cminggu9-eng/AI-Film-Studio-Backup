---
type: director-typed-enum-repair-provenance
status: complete
version: 0.1
---

# Director Typed-Enum Repair Provenance V0.1

## Source evidence (read-only)

Repair 09D Probe 03 persisted the exact final wire schema and raw DeepSeek error evidence before classification. The Provider message was:

```text
Invalid tool parameters schema : one of `type`, `anyOf`, `$ref` field is required
```

The historical artifacts remain immutable:

- `../E2E_Targeted_Repair_09C_Director_Strict_Provider_Compatibility_V0.1/evidence/DIRECTOR-COMPATIBILITY-PROBE-03/artifacts/director_provider_http_error.json`
- `../E2E_Targeted_Repair_09C_Director_Strict_Provider_Compatibility_V0.1/evidence/DIRECTOR-COMPATIBILITY-PROBE-03/artifacts/director_final_wire_payload.json`

## Exact repair subject

All nine affected nodes formerly had only `{"enum":["ABSENT"]}`. Repair 09E projects each one as `{"type":"string","enum":["ABSENT"]}`.

The accepted value set remains exactly `{ABSENT}`. Requiredness, canonical tokens, machine fields, semantic owner, and lawful absence meaning are unchanged. Semantic impact: **NONE**.

