"""CLI wrapper for the Showrunner Runtime Compliance Gate."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.compliance.compliance_gate import gate_with_correction, load_rules, write_compliance_log


def main() -> int:
    parser = argparse.ArgumentParser(description="Run deterministic Showrunner compliance checks.")
    parser.add_argument("--candidate-file", type=Path, required=True)
    parser.add_argument("--candidate-v2-file", type=Path)
    parser.add_argument("--rules", type=Path)
    parser.add_argument("--log", type=Path)
    args = parser.parse_args()
    rules = load_rules(args.rules)
    candidate_v1 = json.loads(args.candidate_file.read_text(encoding="utf-8"))
    candidate_v2 = None
    if args.candidate_v2_file:
        candidate_v2 = json.loads(args.candidate_v2_file.read_text(encoding="utf-8"))
    result = gate_with_correction(candidate_v1, candidate_v2, rules)
    log_path = write_compliance_log(result, args.log)
    result["log_path"] = str(log_path)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] in {"PASS", "GATE_RECOVERED"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
