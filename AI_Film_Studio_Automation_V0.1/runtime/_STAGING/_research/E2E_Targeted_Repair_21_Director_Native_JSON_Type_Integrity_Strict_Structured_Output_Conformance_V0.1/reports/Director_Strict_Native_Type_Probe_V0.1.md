# Director Strict Native Type Probe V0.1

Probe ID: `DIRECTOR-NATIVE-TYPE-PROBE-21-F03`  
Result: **FAIL — no second probe permitted**

The probe used the read-only R26 successful upstream Director input package. Its source-input SHA-256 is `4548f22f0b67c43f2a035632ed127152e968999589e5a95c19e4143235ce5f8a`.

| Evidence | Result |
| --- | --- |
| Provider calls | 1 / 1 maximum |
| Final wire | exact `submit_director_package`, `strict:true`, forced exact tool choice |
| Provider response | HTTP 200, `tool_calls`, 2242 / 3500 tokens, not truncated |
| Raw-first persistence | PASS; raw content SHA-256 `cbb9ee767888364462b4a9ed2d504e8463faeb25b10d054e24ffab1bc0fc07a7` |
| Raw `unresolved_decisions` | JSON string containing an array, not a native array |
| Local strict validation | FAIL: `must be ABSENT or text list` |
| Retry / fallback / R03 restart | 0 / 0 / false |

The provider-facing generic type reminder did not change raw native-type conformance. Historical R26 remains `BLOCKED`.

