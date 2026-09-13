---
type: director-structured-prompt-capture
status: intercepted-before-network
version: 0.1
---

# Director Structured Prompt Capture V0.1

The final live-path request was built through `build_system_prompt()` and `DeepSeekProviderAdapter.build_provider_payload()` without a network send.

- Function: `submit_director_package`
- Strict: `true`
- Tool choice: forced Director function
- Endpoint class: DeepSeek beta strict route
- Prompt field manifest: exact 15 fields
- Legacy generic schema marker `REQUIRED TRANSPORT SCHEMA:`: `0`
- Typed enum projection: retained
- JSON-object-string instruction: present for all five named state fields
- Provider / executor / role calls: `0 / 0 / 0`

The canonical Skill remains appended as read-only semantic authority, but the prompt's active structured transport instruction is the deterministic contract derived from final function parameters.

