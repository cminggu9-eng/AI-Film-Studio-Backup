"""Provider-free bounded budget preflight."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in ROOT.parents if (parent / "studio.config.json").is_file())
for import_path in (str(ROOT / "implementation"), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

from scene_writer_response_budget import scene_writer_response_budget_preflight


if __name__ == "__main__":
    payload = scene_writer_response_budget_preflight()
    payload["classification"] = "SCENE WRITER RESPONSE BUDGET PREFLIGHT"
    payload["provider_calls"] = 0
    print(json.dumps(payload, ensure_ascii=False, indent=2))

