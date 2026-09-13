# Cross Fixture Isolation Test Report V0.1

`PASS`.

- Fixture 02 compiled output contains none of Fixture 01 prop/state values or Fixture 03 prop value.
- Fixture 03 compiled output contains none of Fixture 01 prop/state values or Fixture 02 prop/state values.
- Compiler source contains none of the scanned fixture semantic literals.
- Bindings are read independently and copied before compilation.

