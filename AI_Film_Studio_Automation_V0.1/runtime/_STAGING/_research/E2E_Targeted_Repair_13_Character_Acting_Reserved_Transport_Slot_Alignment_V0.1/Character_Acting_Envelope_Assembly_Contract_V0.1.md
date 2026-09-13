# Character & Acting Envelope Assembly Contract V0.1

Date: 2026-08-31

## Assembly sequence

1. Persist the untouched Provider response, usage, invocation metadata, finish reason, and trace evidence.
2. Parse the non-strict JSON object.
3. Validate the nine-field Character raw role payload.
4. Validate exact canonical outcome and authority boundary.
5. Validate the independent upstream Scene Writer artifact and source identity.
6. Deep-copy the raw role payload.
7. Insert only `scene_packages: ABSENT` as the integration-owned reserved slot.
8. Persist assembly evidence with zero semantic/canonical mutation.
9. Validate the final ten-field role transport.
10. Assemble the normal State & Evidence Envelope and continue only after all gates pass.

The State & Evidence Envelope itself does not duplicate scene packages. Downstream input retains the validated Scene Writer artifact/envelope separately from the Character & Acting artifact/envelope. This preserves both source identities and avoids a model-echo mutation surface.

