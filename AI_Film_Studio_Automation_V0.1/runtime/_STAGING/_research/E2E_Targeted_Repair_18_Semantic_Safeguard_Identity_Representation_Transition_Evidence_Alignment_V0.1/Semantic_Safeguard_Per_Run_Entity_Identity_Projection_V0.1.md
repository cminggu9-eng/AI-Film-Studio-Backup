# Semantic Safeguard Per-Run Entity Identity Projection

Implementation: `integration_contract/semantic_alignment.py`.

Each compiled projection contains only current binding records, a stable `binding_entity_node`, exact namespace tokens, source pointer, binding ID, and projection hash. F01, F02, and F03 produced three distinct projection hashes. Forward and reverse fixture use did not leak representations.

Derivation mode: `BINDING_RECORD_MEMBERSHIP_ONLY`.

