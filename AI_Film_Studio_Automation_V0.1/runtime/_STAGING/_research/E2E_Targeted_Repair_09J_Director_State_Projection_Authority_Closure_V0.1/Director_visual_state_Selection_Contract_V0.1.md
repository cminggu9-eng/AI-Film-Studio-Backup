# Director visual_state Selection Contract V0.1

Only a source dimension explicitly classified by approved metadata as visual, spatial, or physical-visual continuity may be projected. Dimension-name matching and content heuristics are forbidden.

Current compiled state-dimension records provide dimension names and enum domains but no explicit classification property. Therefore the field is exactly:

```json
{"type":"string","enum":["ABSENT"]}
```

The underlying machine states remain available in `current_state`; `visual_state=ABSENT` does not delete or reclassify them. Director cannot add Art Director, performance-method, or Canon fields.

Status: **AUTHORITY CLOSED**.

