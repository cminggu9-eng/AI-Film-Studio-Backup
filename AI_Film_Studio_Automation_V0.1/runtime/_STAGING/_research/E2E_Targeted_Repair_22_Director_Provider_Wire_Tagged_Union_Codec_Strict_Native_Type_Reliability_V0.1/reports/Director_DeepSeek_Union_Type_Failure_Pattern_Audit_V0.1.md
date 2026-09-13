# Director DeepSeek union failure audit

R26 and Probe21 supplied `unresolved_decisions` as a JSON string instead of its canonical `ABSENT | array[text]` value. The actual provider-facing schema exposed that union directly. Repair22 changes only that provider representation.
