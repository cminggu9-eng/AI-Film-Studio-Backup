# Director State ABSENT Semantics V0.1

For each of the five fields, lawful absence is represented only by the exact string sentinel `ABSENT`, consistent with the 09B state branch and the role-neutral State Evidence contract. `null` is invalid. `{}` is a JSON object and must never be silently equated with `ABSENT`.

The authority gap concerns the properties of a present object; it does not make absence ambiguous. A future exact schema must retain this outer union: `ABSENT` or one fully valid approved object.

