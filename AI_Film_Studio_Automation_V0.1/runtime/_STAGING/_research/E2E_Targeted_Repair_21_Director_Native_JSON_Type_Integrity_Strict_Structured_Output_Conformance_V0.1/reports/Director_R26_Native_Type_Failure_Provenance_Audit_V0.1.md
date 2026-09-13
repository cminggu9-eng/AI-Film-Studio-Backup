# Director R26 Native-Type Failure Provenance Audit V0.1

## Result

`E2E-RUN-26` remains `BLOCKED`. Its earliest Director blocker is a native JSON type violation, not a semantic judgment or truncation failure.

| Provenance step | Authoritative evidence | Result |
| --- | --- | --- |
| Compiled contract | Per-run F03 Director contract | `unresolved_decisions` is required and is `ABSENT` or native `array<string>` |
| DeepSeek projection | Lossless strict projection | Same union preserved |
| R26 final wire | `E2E-RUN-26/artifacts/director_final_wire_payload.json` | `strict:true`, exact forced `submit_director_package`, same union |
| R26 raw arguments | `director_provider_response.json`, raw SHA `bfefb3b84284c665ca8ee8f2d5a73afe9ded177374be72f2556bd2eb69acc900` | `unresolved_decisions` is a JSON string containing an array |
| Local validator | `director_validation_error.json` | Fail-closed: `must be ABSENT or text list` |

The R26 raw field can be inspected diagnostically as syntactically valid JSON, but that inspection is never passed to production validation and cannot repair the recorded run.

## Attribution

The wire schema correctly expresses the native union. The raw Provider tool arguments violate it before any local conversion boundary. Attribution is therefore `PROVIDER STRICT NATIVE-TYPE CONFORMANCE FAILURE`.

