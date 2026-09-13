---
type: shootability-decision-model
status: passed-awaiting-human-review
version: 0.1
role: Scene Writer
provenance: AI-FILM-STUDIO-SYNTHESIS
---

# Scene Writer Unshootable Language Taxonomy V0.1

> This is a **shootability decision model**, not a keyword blacklist. Words such as “realises”, “feels”, “knows”, or “remembers” are not errors by themselves.

## Shootability Test

For any potentially interior, summary, or abstract statement, decide in order:

1. **Field:** Is it scene action, dialogue, authorised narration/voice-over, concise form-permitted framing, or an internal planning note?
2. **Meaning lock:** What fact, uncertainty, relationship stance, causal strength, or required outcome cannot change?
3. **Existing carrier:** Is the information already supported by action, choice, hesitation, reaction, object/sound, spatial behaviour, dialogue, silence, avoidance, changed behaviour, clue, or authorised form?
4. **Need for conversion:** Would an audience otherwise receive only author explanation in scene action?
5. **Minimum conversion:** What smallest carrier preserves the current scene function without over-explaining or prescribing acting/camera?
6. **Authority:** Does the conversion require changing Canon, a Showrunner lock, a production fact, final direction, final acting, or language/voice QA? If yes, hand off.

## Contextual Pattern Table

|Pattern|Weak when|Lawful when|Possible carriers if conversion is needed|Meaning / anti-mechanical protection|
|---|---|---|---|---|
|Pure internal summary|Scene action requires direct mental access and gives no encounterable carrier.|Authorised interior device, concise permitted framing, or planning note.|Stimulus + choice, changed plan, interruption, line, refusal, object/action, altered response.|Do not turn uncertain awareness into a specific accusation; no word ban.|
|Emotion label|A named feeling substitutes for present pressure/action/relation.|Authorised device or direct dialogue that itself performs action.|Hesitation, avoidance, competing action, silence, active line, changed relation, relevant object/action.|Do not flatten complexity into a generic gesture or intensity label.|
|Relationship summary|Outcome is announced without an enacted change in access/trust/power/obligation.|Planning/narration/authorised concise transition field.|Request/refusal, information sharing/withholding, commitment, changed address/access, dialogue action.|No forced confrontation; relation can move through cooperation, silence, protection or choice.|
|Backstory explanation|History is dumped without current relevance, replacing present action.|Authorised narration or direct dialogue/clue with current dramatic action.|Relevant clue, active question/answer, trigger, concrete consequence, contextual detail.|Do not force every fact into a prop/flashback or invent Canon causality.|
|Abstract intent summary|A decision is asserted in scene action without a current commitment/consequence.|Assignment lock, authorised device, or declaration that changes relation.|Refusal, revoked access, changed plan, condition, commitment, direct line, choice under pressure.|Do not “improve” an approved lie into confession or alter outcome.|
|Weak causal summary|Causal link/conclusion is inaccessible and the audience cannot assess why it changed.|Authorised narration or concise authorised transition.|Discovery, changed response, revised choice, consequence, clue, dialogue action.|No reveal required; do not over-explain or invent evidence.|

## Stop Conditions

- Preserve authorised narration, dialogue action, and concise allowed screen description rather than mechanically converting them.
- Preserve uncertainty and relation stance; a carrier may be smaller than a “full explanation.”
- Stop before final camera, lens, movement, coverage, staging, edit rhythm, micro-expression, intensity, or voice-QA intervention.
- If no lawful carrier can preserve a locked meaning, return `NEEDS_CONTEXT` or `UPSTREAM_DECISION_REQUIRED`, not a substitute story fact.

