# Director Strict Mechanics Wire Evidence V0.1

Both R26 and the fresh Probe21 persisted final wire payload before send.

| Check | R26 | Probe21 |
| --- | --- | --- |
| Function name | `submit_director_package` | `submit_director_package` |
| `strict` | `true` | `true` |
| `tool_choice` | exact forced Director function | exact forced Director function |
| HTTP response | 200 | 200 |
| Finish reason | `tool_calls` | `tool_calls` |
| Truncation | not truncated | not truncated (2242 / 3500 tokens) |

The strict mechanics and raw-first persistence are confirmed by actual wire and response artifacts, not runtime configuration alone.

