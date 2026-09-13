# Transition Application to Snapshot

Repair19 preserves the Repair18 four-field transition invariant:

```text
AUTHORIZED != OCCURRED != OBSERVED != HANDED_OFF
```

The state phase projection delegates transition classification to the shared transition authority. It advances only on an actual occurrence; it never repairs or rewrites recorded Scene Writer evidence.

R24 S01 remains exactly:

```json
{"AUTHORIZED": true, "OCCURRED": true, "OBSERVED": true, "HANDED_OFF": false}
```

That valid occurrence produces the recorded EXIT state without altering the ENTRY source.
