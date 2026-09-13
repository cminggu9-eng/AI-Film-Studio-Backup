# R25 missing-field diagnostic

Diagnostic-only local validation enumerates four omissions:

| Scene | Missing field |
|---|---|
| S02 | structural |
| S02 | state |
| S03 | structural |
| S03 | state |

The official runtime replay intentionally exposes only the safe first failure: S02 missing structural. No diagnostic output changes the frozen raw arguments or advances R25 past its historical stop.
