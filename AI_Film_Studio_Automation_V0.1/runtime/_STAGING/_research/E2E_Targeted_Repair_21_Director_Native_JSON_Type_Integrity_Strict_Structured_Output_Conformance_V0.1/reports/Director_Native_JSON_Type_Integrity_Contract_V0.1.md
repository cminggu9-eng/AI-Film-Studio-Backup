# Director Native JSON Type Integrity Contract V0.1

Repair21 adds one generic provider-facing instruction generated from the final function schema:

> Use native JSON types exactly as declared by the function schema. Never serialize an array or object into a JSON string.

The reminder is generated from the final parameters and covers the schema-declared container and `ABSENT` domains. It contains no F01/F02/F03 identifier, C-09 reference, battery term, or story decision. It does not normalize, parse, wrap, or collapse any response value.

Production validator behavior is unchanged: a stringified array/object remains an error.

