"""Provider-free import proof for the Minimal E2E execution harness."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict


STAGE = Path(__file__).resolve().parents[1]
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
REPAIR_IMPLEMENTATION = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Integration_Contract_Repair_V0.1" / "implementation"
SCENE_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Scene_Writer_Runtime_Integration_V0.1"
for import_path in (str(STAGE), str(REPAIR_IMPLEMENTATION), str(SCENE_STAGE), str(AUTOMATION_ROOT)):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)


def main() -> int:
    from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter
    from runtime.shared_qa.model_executor import ModelExecutor

    counters: Dict[str, int] = {"provider_initializations": 0, "provider_calls": 0, "executor_initializations": 0, "executor_calls": 0}
    saved = (DeepSeekProviderAdapter.__init__, DeepSeekProviderAdapter.complete, ModelExecutor.__init__, ModelExecutor.execute)

    def provider_init(self, *args: Any, **kwargs: Any) -> None:
        counters["provider_initializations"] += 1
        raise AssertionError("Provider initialization on harness import is forbidden")

    def provider_call(self, *args: Any, **kwargs: Any) -> Any:
        counters["provider_calls"] += 1
        raise AssertionError("Provider call on harness import is forbidden")

    def executor_init(self, *args: Any, **kwargs: Any) -> None:
        counters["executor_initializations"] += 1
        raise AssertionError("Executor initialization on harness import is forbidden")

    def executor_call(self, *args: Any, **kwargs: Any) -> Any:
        counters["executor_calls"] += 1
        raise AssertionError("Executor call on harness import is forbidden")

    DeepSeekProviderAdapter.__init__ = provider_init
    DeepSeekProviderAdapter.complete = provider_call
    ModelExecutor.__init__ = executor_init
    ModelExecutor.execute = executor_call
    try:
        spec = importlib.util.spec_from_file_location("minimal_e2e_harness_startup", STAGE / "run_minimal_e2e.py")
        if spec is None or spec.loader is None:
            raise RuntimeError("Harness module cannot be loaded")
        module = importlib.util.module_from_spec(spec)
        sys.modules["minimal_e2e_harness_startup"] = module
        spec.loader.exec_module(module)
        assert module.RUN_ID == "E2E-RUN-01"
        assert len(module.ROLE_SPECS) == 7
    finally:
        DeepSeekProviderAdapter.__init__, DeepSeekProviderAdapter.complete, ModelExecutor.__init__, ModelExecutor.execute = saved

    assert all(value == 0 for value in counters.values()), counters
    print(json.dumps({"result": "PASS", "classification": "MINIMAL E2E HARNESS IMPORT", "counters": counters, "provider_calls": 0, "executor_calls": 0}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
