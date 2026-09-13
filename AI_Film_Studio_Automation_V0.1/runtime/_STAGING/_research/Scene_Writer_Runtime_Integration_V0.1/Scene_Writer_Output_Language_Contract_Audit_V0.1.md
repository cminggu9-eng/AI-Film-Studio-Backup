---
type: output-language-contract-audit
status: passed-with-semantic-observation-recorded
scope: runtime execution constraint only
---

# Scene Writer Output Language Contract Audit V0.1

## Architecture finding

Before this repair, Scene Writer Runtime had no output-language field, no resolved-language metadata, no language-aware validator, and no fallback policy. The prior English Smoke output was therefore unconstrained; it was not evidence of a Chinese-language failure.

## Contract decision

`output_language` is an Assignment / Runtime execution constraint, not a canonical Skill dramatic rule.

| Input condition | Effective output language | Result |
|---|---|---|
| exact `output_language` is present | its exact value | `EXPLICIT` |
| `output_language` absent; exact `assignment_language` is present | `assignment_language` | `INHERIT_ASSIGNMENT_LANGUAGE` |
| both are absent | none | `CONTRACT_ERROR / OUTPUT_LANGUAGE_UNRESOLVED` |
| either supplied value is unsupported | none | `CONTRACT_ERROR` |

Supported tokens: `zh-CN`, `en-US`. Language inference from free text, Unicode guesswork, user wording, project identity, or system locale is prohibited. The script-based validator is only a post-execution enforcement check; it never chooses an output language.

## Propagation path

`Scene Assignment.output_language → SceneWriterRuntime normalization/resolution → canonical executor invocation input + execution metadata → shared ModelExecutor request → DeepSeek provider → Runtime Output Language Validator → Runtime Result Envelope`.

The executor prompt applies the resolved value to readable creative and user-facing/audit control text. Canonical mode, primary-state, flag, and handoff-owner tokens remain unmodified exact English tokens.

## Semantic and frozen boundaries

No Scene Writer dramatic rule, Objective/Resistance/Turn, Shootability, Entry/Exit, Production Burden, authority boundary, Showrunner, Shared QA, Capability Model, or canonical Skill body was changed. The canonical Skill remains hash-identical and contains no hardcoded Chinese-output behavior.
