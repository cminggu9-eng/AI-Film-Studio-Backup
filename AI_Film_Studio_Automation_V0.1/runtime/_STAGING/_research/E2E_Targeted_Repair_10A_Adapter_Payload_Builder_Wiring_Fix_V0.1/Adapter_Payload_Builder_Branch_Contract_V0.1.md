# Adapter Payload Builder Branch Contract

`ModelRequest.structured_output` is the explicit branch input. `None` is the lawful non-structured branch and yields `response_format=json_object`; a valid contract is the structured branch and yields strict tool/function transport plus forced tool_choice. Invalid mixed or absent branch states fail closed.
