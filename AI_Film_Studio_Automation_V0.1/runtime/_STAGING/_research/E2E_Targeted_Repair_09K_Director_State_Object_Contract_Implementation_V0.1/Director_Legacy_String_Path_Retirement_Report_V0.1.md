# Director Legacy String Path Retirement Report V0.1

Live-path status: **UNREACHABLE**.

The 09C projection no longer replaces dynamic object branches with string schemas. The prompt no longer asks for JSON-object strings. The validator no longer decodes strings. A JSON string supplied for either dynamic field fails locally (`DIR-OBJ-NEG-12`).

The historical alias `JSON_OBJECT_STRING_STATE_FIELDS` remains marked deprecated solely so old source/evidence can still be inspected; no live builder, prompt, projection, validator, runner, capture, or Phase2 09K suite uses it. Historical Probe04 remains an immutable PASS fact, while its old representation does not govern future runs.
