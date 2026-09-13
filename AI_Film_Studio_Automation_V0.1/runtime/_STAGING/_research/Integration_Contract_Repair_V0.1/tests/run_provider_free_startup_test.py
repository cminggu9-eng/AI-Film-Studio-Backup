"""Fresh-process static-startup proof with provider and executor traps."""

from __future__ import annotations

import importlib
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict


STAGE = Path(__file__).resolve().parents[1]
IMPLEMENTATION = STAGE / "implementation"
AUTOMATION_ROOT = next(parent for parent in STAGE.parents if (parent / "studio.config.json").is_file())
SCENE_STAGE = AUTOMATION_ROOT / "runtime" / "_STAGING" / "_research" / "Scene_Writer_Runtime_Integration_V0.1"
for path in (str(IMPLEMENTATION), str(SCENE_STAGE), str(AUTOMATION_ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)


def import_file(module_name: str, path: Path) -> None:
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)


def main() -> int:
    from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter
    from runtime.shared_qa.model_executor import ModelExecutor

    counters: Dict[str, int] = {
        "provider_initializations": 0,
        "provider_completions": 0,
        "executor_initializations": 0,
        "executor_calls": 0,
    }
    original_provider_init = DeepSeekProviderAdapter.__init__
    original_provider_complete = DeepSeekProviderAdapter.complete
    original_executor_init = ModelExecutor.__init__
    original_executor_execute = ModelExecutor.execute

    def provider_init_trap(self, *args: Any, **kwargs: Any) -> None:
        counters["provider_initializations"] += 1
        raise AssertionError("Provider initialization is forbidden during startup proof")

    def provider_complete_trap(self, *args: Any, **kwargs: Any) -> Any:
        counters["provider_completions"] += 1
        raise AssertionError("Provider completion is forbidden during startup proof")

    def executor_init_trap(self, *args: Any, **kwargs: Any) -> None:
        counters["executor_initializations"] += 1
        raise AssertionError("Executor construction is forbidden during startup proof")

    def executor_execute_trap(self, *args: Any, **kwargs: Any) -> Any:
        counters["executor_calls"] += 1
        raise AssertionError("Executor call is forbidden during startup proof")

    DeepSeekProviderAdapter.__init__ = provider_init_trap
    DeepSeekProviderAdapter.complete = provider_complete_trap
    ModelExecutor.__init__ = executor_init_trap
    ModelExecutor.execute = executor_execute_trap
    try:
        importlib.import_module("integration_contract")
        startup = importlib.import_module("integration_contract.provider_free_startup")
        discovery = startup.startup_discovery()
        import_file("integration_legacy_smoke_import", SCENE_STAGE / "tests" / "run_smoke_sw_exec_01.py")
        import_file("integration_legacy_synthetic_import", SCENE_STAGE / "tests" / "run_synthetic_e2e.py")
    finally:
        DeepSeekProviderAdapter.__init__ = original_provider_init
        DeepSeekProviderAdapter.complete = original_provider_complete
        ModelExecutor.__init__ = original_executor_init
        ModelExecutor.execute = original_executor_execute

    assert discovery["role"]["identity"] == "scene-writer", discovery
    assert discovery["adapter"]["adapter"] == "SceneWriterRuntime", discovery
    assert discovery["state_envelope"]["absent_token"] == "ABSENT", discovery
    assert discovery["fixture"]["fixture_id"] == "E2E-FIX-01", discovery
    assert all(value == 0 for value in counters.values()), counters
    payload = {
        "classification": "PROVIDER-FREE IMPORT / DISCOVERY / STATIC STARTUP",
        "checks": [
            "clean import",
            "harness import",
            "configuration load",
            "role discovery",
            "adapter discovery",
            "state-envelope load",
            "fixture load",
            "legacy smoke runner import",
            "legacy synthetic runner import",
        ],
        "provider_calls": 0,
        "executor_calls": 0,
        "counters": counters,
        "result": "PASS",
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
