# Canonical and provider-wire representations

Canonical remains the exact 15-field Director contract. `unresolved_decisions` remains `ABSENT | array[text]`. The DeepSeek-only wire projection is `{status: ABSENT|PRESENT, items: array[text]}`; it distinguishes `ABSENT` from `[]` losslessly.
