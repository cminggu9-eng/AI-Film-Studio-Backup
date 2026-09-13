"""TOKEN-TEST-01–10 for provider-neutral strict Contemporary Handoff tokens."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.shared_qa.contemporary_handoff_coordinator import ContemporaryHandoffCoordinator
from runtime.shared_qa.contemporary_handoff_token_contract import ContemporaryHandoffTokenContract, ContemporaryTokenContractError
from runtime.shared_qa.contemporary_language_runtime import ContemporaryLanguageRuntime


def main() -> int:
    contract = ContemporaryHandoffTokenContract()
    token = contract.canonical_token
    checks = []
    def expect_pass(name, value):
        try:
            contract.validate(value)
            checks.append((name, "PASS"))
        except Exception as exc:
            checks.append((name, f"FAIL: {type(exc).__name__}"))
    def expect_reject(name, value):
        try:
            contract.validate(value)
            checks.append((name, "FAIL: accepted"))
        except ContemporaryTokenContractError:
            checks.append((name, "PASS"))
    expect_pass("TOKEN-TEST-01 exact canonical token", {"contemporary_state": token})
    expect_reject("TOKEN-TEST-02 whitespace safety strict reject", {"contemporary_state": f" {token} "})
    expect_reject("TOKEN-TEST-03 case handling strict reject", {"contemporary_state": token.lower()})
    checks.append(("TOKEN-TEST-04 registered alias", "N/A — no aliases registered"))
    expect_reject("TOKEN-TEST-05 unknown semantic phrase", {"contemporary_state": "probably needs current-language review"})
    expect_reject("TOKEN-TEST-06 invalid new state", {"contemporary_state": "NEW_CONTEMPORARY_STATE"})
    expect_reject("TOKEN-TEST-07 missing state", {})
    expect_pass("TOKEN-TEST-08 non-handoff null state", {"contemporary_state": None})
    token_source = ROOT / "runtime" / "shared_qa" / "contemporary_handoff_token_contract.py"
    checks.append(("TOKEN-TEST-09 provider independence", "PASS" if "deepseek" not in token_source.read_text(encoding="utf-8").lower() else "FAIL"))
    original = {"decision": "ROLE HANDOFF / WARNING", "severity": "LEVEL 4", "contemporary_state": token}
    checks.append(("TOKEN-TEST-10 no semantic drift", "PASS" if contract.validate(original) == original else "FAIL"))
    for name, status in checks:
        print(f"{name}: {status}")
    return 0 if all(status in {"PASS", "N/A — no aliases registered"} for _, status in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
