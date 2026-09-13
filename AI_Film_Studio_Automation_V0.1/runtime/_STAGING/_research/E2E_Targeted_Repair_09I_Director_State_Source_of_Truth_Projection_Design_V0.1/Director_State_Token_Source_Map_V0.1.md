# Director State Token Source Map V0.1

| Token category | Approved source | Projection status |
|---|---|---|
| absence | State Evidence `ABSENT` | closed at outer field |
| state-dimension values | compiled `state_dimensions[].allowed_tokens` | dynamic and exact, but no five-field mapping |
| transition identifiers | compiled `authorized_transitions` / shared transition projection | dynamic and exact, but no proposed-delta mapping |
| knowledge event values | binding `knowledge_events` | source carried but inner schema/property mapping open |
| Director Mode / Primary State | Canonical Director contract | outer payload only |

No Fixture01 literal is copied into a generic schema. Fixture01–03 compilation confirms that the state dimension and transition domains change with the binding.

