"""Exact canonical binding for Scene Writer using the shared executor infrastructure."""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Dict, Mapping

from runtime.compliance.compliance_gate import sha256_file
from runtime.shared_qa.model_executor import ModelExecutor
from runtime.scene_writer.scene_writer_executor import CanonicalSceneWriterExecutor
from runtime.scene_writer.scene_writer_runtime import SceneWriterRuntime
from runtime.scene_writer.semantic_assignment_integrity import SemanticAssignmentIntegrityVerifier

if TYPE_CHECKING:
    from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter


class SceneWriterExecutorBindingError(RuntimeError):
    """An exact canonical binding failure; caller must fail safe."""


@dataclass(frozen=True)
class SceneWriterCanonicalBinding:
    identity: str
    version: str
    sha256: str
    canonical_path: Path

    @classmethod
    def load(cls) -> "SceneWriterCanonicalBinding":
        contract_path = Path(__file__).with_name("scene_writer_runtime_contract.json")
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        project_root = next(parent for parent in contract_path.parents if (parent / "studio.config.json").is_file())
        config = json.loads((project_root / "studio.config.json").read_text(encoding="utf-8-sig"))
        skill = contract["skill"]
        return cls(
            identity=skill["identity"],
            version=skill["version"],
            sha256=skill["sha256"].lower(),
            canonical_path=(Path(config["vault_path"]) / skill["canonical_relative_path"]).resolve(),
        )


class SceneWriterExecutorRegistry:
    """One exact canonical dispatch target; never accepts Staging or aliases."""

    def __init__(self, binding: SceneWriterCanonicalBinding) -> None:
        self.binding = binding
        self._executor: Callable[[Dict[str, Any]], Dict[str, Any]] | None = None

    def register(self, executor: Any) -> None:
        if self._executor is not None:
            raise SceneWriterExecutorBindingError("Scene Writer executor is already registered")
        if not callable(executor) or not hasattr(executor, "canonical_metadata"):
            raise SceneWriterExecutorBindingError("Executor is not a canonical callable")
        metadata = executor.canonical_metadata()
        if not isinstance(metadata, Mapping):
            raise SceneWriterExecutorBindingError("Executor canonical metadata is invalid")
        if (
            metadata.get("identity") != self.binding.identity
            or metadata.get("version") != self.binding.version
            or str(metadata.get("sha256", "")).lower() != self.binding.sha256
        ):
            raise SceneWriterExecutorBindingError("Executor identity, version, or hash did not match canonical binding")
        try:
            candidate_path = Path(str(metadata.get("path", ""))).resolve()
        except OSError as exc:
            raise SceneWriterExecutorBindingError("Executor path could not be resolved") from exc
        if candidate_path != self.binding.canonical_path:
            raise SceneWriterExecutorBindingError("Executor attempted a non-canonical Skill path")
        if not candidate_path.is_file() or sha256_file(candidate_path).lower() != self.binding.sha256:
            raise SceneWriterExecutorBindingError("Executor canonical Skill hash did not match")
        self._executor = executor

    def resolve(self, identity: str, version: str, sha256: str) -> Callable[[Dict[str, Any]], Dict[str, Any]]:
        if self._executor is None:
            raise SceneWriterExecutorBindingError("No registered canonical Scene Writer executor")
        if identity != self.binding.identity or version != self.binding.version or sha256.lower() != self.binding.sha256:
            raise SceneWriterExecutorBindingError("Canonical executor identity, version, or hash mismatch")
        return self._executor

    def dispatch(self, invocation: Dict[str, Any]) -> Dict[str, Any]:
        skill = invocation.get("canonical_skill") if isinstance(invocation, Mapping) else None
        if not isinstance(skill, Mapping):
            raise SceneWriterExecutorBindingError("Runtime dispatch request lacked canonical Skill identity")
        executor = self.resolve(
            str(skill.get("identity", "")),
            str(skill.get("version", "")),
            str(skill.get("sha256", "")),
        )
        return executor(copy.deepcopy(invocation))


@dataclass
class SceneWriterBindingBundle:
    runtime: SceneWriterRuntime
    registry: SceneWriterExecutorRegistry
    executor: CanonicalSceneWriterExecutor
    semantic_verifier: SemanticAssignmentIntegrityVerifier
    model_executor: ModelExecutor
    provider: "DeepSeekProviderAdapter"


def create_scene_writer_binding(*, execution_classification: str = "PRODUCTION") -> SceneWriterBindingBundle:
    """Create a real canonical binding at the explicit execution boundary.

    Importing or discovering this module never constructs a provider or
    ModelExecutor. Calling this factory is the only supported transition from
    static discovery into an execution-capable binding; the factory still does
    not itself make a provider completion call.
    """
    from runtime.shared_qa.deepseek_provider_adapter import DeepSeekProviderAdapter

    binding = SceneWriterCanonicalBinding.load()
    provider = DeepSeekProviderAdapter()
    model_executor = ModelExecutor(provider)
    executor = CanonicalSceneWriterExecutor(
        skill_path=binding.canonical_path,
        expected_sha256=binding.sha256,
        model_executor=model_executor,
        model=provider.model,
        thinking_mode=provider.thinking_mode,
    )
    registry = SceneWriterExecutorRegistry(binding)
    registry.register(executor)
    semantic_verifier = SemanticAssignmentIntegrityVerifier(
        model_executor=model_executor,
        model=provider.model,
        thinking_mode=provider.thinking_mode,
    )
    return SceneWriterBindingBundle(
        runtime=SceneWriterRuntime(
            executor=registry.dispatch,
            semantic_verifier=semantic_verifier,
            execution_classification=execution_classification,
        ),
        registry=registry,
        executor=executor,
        semantic_verifier=semantic_verifier,
        model_executor=model_executor,
        provider=provider,
    )
