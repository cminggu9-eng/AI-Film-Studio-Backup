---
type: director-strict-compatibility-probe-03-final-wire-evidence
status: persisted-before-send
version: 0.1
---

# Director Strict Compatibility Probe 03 — Final Wire Evidence V0.1

Before sending, the real adapter persisted the exact redacted payload at `evidence/DIRECTOR-STRICT-COMPATIBILITY-PROBE-03/artifacts/director_final_wire_payload.json`.

| Hash stage | SHA-256 |
| --- | --- |
| Provider-neutral Director contract | `3adbf243cc99866251c09091f35c62820322c1b85072c3b5c34f2bce8ac5f8f8` |
| Compatibility projection | `06b1bd545b87c70452072f8c3aae3d1e417b87b041f8046b50ed538ca512a1a0` |
| Final function parameters | `06b1bd545b87c70452072f8c3aae3d1e417b87b041f8046b50ed538ca512a1a0` |
| Final wire payload | `1b2057d294306802a52e8d8e695a8add0b2bbeedc711c059131c3267a3764c51` |

Projection hash equals final parameters hash. All nine fixed absence nodes are typed `string` enums; no bare enum-only node is present. The request used the DeepSeek beta strict endpoint, model `deepseek-v4-pro`, `max_tokens: 3500`, `strict: true`, and forced `tool_choice` for `submit_director_package`.

