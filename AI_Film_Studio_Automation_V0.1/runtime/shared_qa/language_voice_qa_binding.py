"""Registered canonical executor binding for Language & Voice QA V0.1."""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, Mapping

from runtime.compliance.compliance_gate import sha256_file
from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter
from runtime.shared_qa.language_voice_qa_executor import CanonicalLanguageVoiceQAExecutor
from runtime.shared_qa.language_voice_qa_runtime import LanguageVoiceQARuntime
from runtime.shared_qa.model_executor import ModelExecutor


class ExecutorBindingError(RuntimeError):
    """A missing or illegal executor binding; Runtime converts this to F3."""


@dataclass(frozen=True)
class CanonicalBinding:
    identity: str
    version: str
    sha256: str
    canonical_path: Path

    @classmethod
    def load(cls) -> "CanonicalBinding":
        contract_path = Path(__file__).with_name("language_voice_qa_contract.json")
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        project_root = contract_path.parents[2]
        config = json.loads((project_root / "studio.config.json").read_text(encoding="utf-8"))
        skill = contract["skill"]
        return cls(
            identity=skill["identity"],
            version=skill["version"],
            sha256=skill["sha256"].upper(),
            canonical_path=(Path(config["vault_path"]) / skill["canonical_relative_path"]).resolve(),
        )


class CanonicalExecutorRegistry:
    """Resolve one exact canonical identity; no staging or fallback paths exist."""

    def __init__(self, binding: CanonicalBinding) -> None:
        self.binding = binding
        self._executor: Callable[[Dict[str, Any]], Dict[str, Any]] | None = None

    def register(self, executor: Any) -> None:
        if self._executor is not None:
            raise ExecutorBindingError("Canonical executor is already registered")
        if not callable(executor) or not hasattr(executor, "canonical_metadata"):
            raise ExecutorBindingError("Executor is not a canonical callable")
        metadata = executor.canonical_metadata()
        if not isinstance(metadata, Mapping):
            raise ExecutorBindingError("Executor canonical metadata is invalid")
        if (
            metadata.get("identity") != self.binding.identity
            or metadata.get("version") != self.binding.version
            or str(metadata.get("sha256", "")).upper() != self.binding.sha256
        ):
            raise ExecutorBindingError("Executor identity or version did not match canonical binding")
        try:
            candidate_path = Path(str(metadata.get("path", ""))).resolve()
        except OSError as exc:
            raise ExecutorBindingError("Executor path could not be resolved") from exc
        if candidate_path != self.binding.canonical_path:
            raise ExecutorBindingError("Executor attempted a non-canonical Skill path")
        if not candidate_path.is_file() or sha256_file(candidate_path).upper() != self.binding.sha256:
            raise ExecutorBindingError("Executor canonical Skill hash did not match")
        self._executor = executor

    def resolve(self, identity: str, version: str, sha256: str) -> Callable[[Dict[str, Any]], Dict[str, Any]]:
        if self._executor is None:
            raise ExecutorBindingError("No registered canonical language-voice-qa executor")
        if identity != self.binding.identity or version != self.binding.version or sha256.upper() != self.binding.sha256:
            raise ExecutorBindingError("Canonical executor identity, version, or hash mismatch")
        return self._executor

    def dispatch(self, invocation: Dict[str, Any]) -> Dict[str, Any]:
        skill = invocation.get("canonical_skill") if isinstance(invocation, Mapping) else None
        if not isinstance(skill, Mapping):
            raise ExecutorBindingError("Runtime dispatch request lacked canonical Skill identity")
        executor = self.resolve(
            str(skill.get("identity", "")),
            str(skill.get("version", "")),
            str(skill.get("sha256", "")),
        )
        return executor(copy.deepcopy(invocation))


@dataclass
class LanguageVoiceQABindingBundle:
    runtime: LanguageVoiceQARuntime
    registry: CanonicalExecutorRegistry
    executor: CanonicalLanguageVoiceQAExecutor
    provider: DeepSeekProviderAdapter


def create_language_voice_qa_binding(*, log_dir: Path | None = None) -> LanguageVoiceQABindingBundle:
    binding = CanonicalBinding.load()
    provider = DeepSeekProviderAdapter()
    executor = CanonicalLanguageVoiceQAExecutor(
        skill_path=binding.canonical_path,
        expected_sha256=binding.sha256,
        model_executor=ModelExecutor(provider),
    )
    registry = CanonicalExecutorRegistry(binding)
    registry.register(executor)
    return LanguageVoiceQABindingBundle(
        runtime=LanguageVoiceQARuntime(registry.dispatch, log_dir=log_dir),
        registry=registry,
        executor=executor,
        provider=provider,
    )

