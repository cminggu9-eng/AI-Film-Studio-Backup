# Wire validation before decode

Raw provider tool arguments are persisted first, then validated against the DeepSeek projected schema and the cross-field invariant `ABSENT => items == []`. Failure taxonomy: `DIRECTOR PROVIDER-WIRE STRICT CONFORMANCE FAILURE`.
