"""Provider-neutral exact token validation for the existing Contemporary Handoff."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Dict, Mapping


class ContemporaryTokenContractError(ValueError):
    """Structured output used a missing or non-canonical contemporary token."""


class ContemporaryHandoffTokenContract:
    """Strict enum boundary; it never infers intent or semantic equivalence."""

    def __init__(self, contract_path: Path | None = None) -> None:
        path = contract_path or Path(__file__).with_name("contemporary_language_contract.json")
        contract = json.loads(path.read_text(encoding="utf-8"))
        self.canonical_token = contract["handoff"]["contemporary_state"]

    def validate(self, output: Mapping[str, Any]) -> Dict[str, Any]:
        if "contemporary_state" not in output:
            raise ContemporaryTokenContractError("contemporary_state is required in structured model output")
        value = output["contemporary_state"]
        if value is None:
            return copy.deepcopy(dict(output))
        if not isinstance(value, str) or value != self.canonical_token:
            raise ContemporaryTokenContractError("contemporary_state is not the exact canonical token")
        return copy.deepcopy(dict(output))

