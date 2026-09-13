# Suite Fixture Ownership Contract V0.1

- Fixture-specific historical suites own their declared Fixture01 test binding.
- The live runner owns its current live binding, such as Fixture02, but it is never inherited by historical/offline children.
- Fixture-less suites explicitly declare `NO_FIXTURE_BINDING_REQUIRED`.
- A Fixture02 test child must declare Fixture02 in its own manifest; it cannot infer it from parent environment.

This preserves Fixture01 historical test meaning while preserving Fixture02 live compilation context.

