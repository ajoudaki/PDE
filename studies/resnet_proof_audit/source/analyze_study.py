"""Deterministic analysis primitives for the PDE proof-obligation study.

This module deliberately contains no scientific simulator, plotting code, or
report writer.  It consumes already sealed arrays (or synthetic arrays in unit
tests), computes the preregistered diagnostics, and emits machine-readable
results.

The central statistical rule is *whole-root coupling*: a bootstrap draw is one
vector of Gaussian-root indices, reused for every width, depth, replica,
observable, and proof gate supplied to the statistic.  This preserves the
couplings that make the scaling corrections informative.

Geometric width, depth, and time tails are explicitly labelled conditional.
They are numerical extrapolations under continuation of the observed
contraction envelope, never unconditional limits.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import hashlib
import json
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence

import numpy as np
from scipy.stats import binom


Array = np.ndarray
Statistic = Callable[[Array], Mapping[str, Array | float]]
DEFAULT_STAGE_FAMILY_CONFIDENCE = 1.0 - 0.049 / 7.0


class ArchiveValidationError(ValueError):
    """Raised when a purported sealed stage archive fails closed."""


class GateStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"


@dataclass(frozen=True)
class GateVerdict:
    status: GateStatus
    reason_codes: tuple[str, ...]
    metrics: Mapping[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status.value,
            "reason_codes": list(self.reason_codes),
            "metrics": _jsonable(self.metrics),
        }


def _jsonable(value: Any) -> Any:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(item) for item in value]
    return value


def _canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        _jsonable(value),
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _valid_sha256(value: Any) -> bool:
    if not isinstance(value, str) or len(value) != 64:
        return False
    try:
        int(value, 16)
    except ValueError:
        return False
    return True


def hash_array(array: Array) -> str:
    """Hash an array including dtype and shape, with object arrays forbidden."""

    value = np.asarray(array)
    if value.dtype.hasobject:
        raise ArchiveValidationError("object arrays are forbidden in archives")
    header = _canonical_json_bytes(
        {"dtype": value.dtype.str, "shape": list(value.shape)}
    )
    payload = np.ascontiguousarray(value).tobytes(order="C")
    return _sha256_bytes(header + b"\0" + payload)


def derive_homogenization_outer_seed(
    bootstrap_seed: int,
    outer_root_index: int,
) -> int:
    """Derive the frozen Stage-2 outer-root seed without scientific code."""

    entropy = [
        int(bootstrap_seed),
        202,
        int(outer_root_index),
    ]
    return int(
        np.random.SeedSequence(entropy).generate_state(
            1, dtype=np.uint64
        )[0]
    )


def homogenization_summary_names(
    candidate_levels: Sequence[int],
) -> tuple[str, ...]:
    """Return the exact compact Stage-2 layer-summary families."""

    levels = tuple(int(value) for value in candidate_levels)
    if not levels or any(value < 1 for value in levels):
        raise ArchiveValidationError(
            "homogenization candidate levels must be positive"
        )
    if tuple(sorted(set(levels))) != levels:
        raise ArchiveValidationError(
            "homogenization candidate levels must be strictly increasing"
        )
    return (
        "forward_action",
        "transpose_action",
        *tuple(
            name
            for level in levels
            for name in (
                f"forward_reconstruction_residual_P{level}",
                f"transpose_projection_residual_P{level}",
            )
        ),
    )


def homogenization_expected_array_shapes(
    *,
    widths: Sequence[int],
    depths: Sequence[int],
    checkpoints: Sequence[float],
    candidate_levels: Sequence[int],
    replicas: int,
    input_dimension: int,
    sample_count: int,
) -> Mapping[str, tuple[int, ...]]:
    """Build the exact compact Stage-2 archive inventory."""

    width_values = tuple(int(value) for value in widths)
    depth_values = tuple(int(value) for value in depths)
    time_values = tuple(float(value) for value in checkpoints)
    replica_count = int(replicas)
    input_count = int(input_dimension)
    samples = int(sample_count)
    if (
        not width_values
        or not depth_values
        or not time_values
        or replica_count < 2
        or input_count < 1
        or samples < 1
    ):
        raise ArchiveValidationError(
            "homogenization archive dimensions are invalid"
        )
    shapes: dict[str, tuple[int, ...]] = {
        "shared_B_standard": (max(width_values), input_count),
        "shared_a_standard": (max(width_values),),
        "W_replica_seeds": (replica_count,),
        "checkpoints": (len(time_values),),
        "widths": (len(width_values),),
        "depths": (len(depth_values),),
    }
    summary_names = homogenization_summary_names(candidate_levels)
    for width in width_values:
        for depth in depth_values:
            for checkpoint in time_values:
                prefix = (
                    f"W{width}_D{depth}_"
                    f"t{int(round(1000.0 * checkpoint)):04d}"
                )
                field_shape = (replica_count, width, samples)
                shapes[f"{prefix}_terminal_H"] = field_shape
                shapes[f"{prefix}_input_P"] = field_shape
                for name in summary_names:
                    base = f"{prefix}_{name}"
                    shapes[f"{base}_depth_average"] = field_shape
                    shapes[f"{base}_layer_covariance"] = (depth, depth)
                    shapes[f"{base}_integrated_covariance"] = ()
                    shapes[f"{base}_bias_squared_by_layer"] = (depth,)
                    shapes[f"{base}_depth_average_bias_squared"] = ()
    return shapes


def validate_homogenization_archive_schema(
    arrays: Mapping[str, Array],
    *,
    widths: Sequence[int],
    depths: Sequence[int],
    checkpoints: Sequence[float],
    candidate_levels: Sequence[int],
    replicas: int,
    input_dimension: int,
    sample_count: int,
    outer_seed: int,
) -> None:
    """Fail closed on any Stage-2 schema, shape, or master-RNG drift."""

    expected_shapes = homogenization_expected_array_shapes(
        widths=widths,
        depths=depths,
        checkpoints=checkpoints,
        candidate_levels=candidate_levels,
        replicas=replicas,
        input_dimension=input_dimension,
        sample_count=sample_count,
    )
    actual_keys = set(arrays)
    expected_keys = set(expected_shapes)
    if actual_keys != expected_keys:
        raise ArchiveValidationError(
            "homogenization array inventory mismatch: "
            f"missing={sorted(expected_keys - actual_keys)}, "
            f"extra={sorted(actual_keys - expected_keys)}"
        )
    for key, expected_shape in expected_shapes.items():
        value = np.asarray(arrays[key])
        if value.shape != expected_shape:
            raise ArchiveValidationError(
                f"homogenization array shape mismatch for {key}: "
                f"{value.shape} != {expected_shape}"
            )
        expected_dtype = (
            np.dtype(np.uint64)
            if key == "W_replica_seeds"
            else (
                np.dtype(np.int64)
                if key in ("widths", "depths")
                else np.dtype(np.float64)
            )
        )
        if value.dtype != expected_dtype:
            raise ArchiveValidationError(
                f"homogenization array dtype mismatch for {key}: "
                f"{value.dtype} != {expected_dtype}"
            )
        if value.dtype.kind in "fc" and not np.all(np.isfinite(value)):
            raise ArchiveValidationError(
                f"homogenization array {key} contains nonfinite values"
            )
        if key.endswith("_layer_covariance") and not np.array_equal(
            value, value.T
        ):
            raise ArchiveValidationError(
                f"homogenization covariance is not exactly symmetric: {key}"
            )

    width_values = np.asarray(tuple(int(value) for value in widths))
    depth_values = np.asarray(tuple(int(value) for value in depths))
    time_values = np.asarray(tuple(float(value) for value in checkpoints))
    if not np.array_equal(np.asarray(arrays["widths"]), width_values):
        raise ArchiveValidationError("homogenization width array mismatch")
    if not np.array_equal(np.asarray(arrays["depths"]), depth_values):
        raise ArchiveValidationError("homogenization depth array mismatch")
    if not np.array_equal(np.asarray(arrays["checkpoints"]), time_values):
        raise ArchiveValidationError(
            "homogenization checkpoint array mismatch"
        )

    seeds = np.asarray(arrays["W_replica_seeds"])
    if not np.issubdtype(seeds.dtype, np.integer):
        raise ArchiveValidationError(
            "homogenization W-replica seeds must be integers"
        )
    if np.unique(seeds).size != int(replicas):
        raise ArchiveValidationError(
            "homogenization W-replica seeds must be unique"
        )
    rng = np.random.default_rng(int(outer_seed))
    expected_B = rng.normal(
        size=(max(width_values), int(input_dimension))
    )
    expected_a = rng.normal(size=max(width_values))
    expected_seeds = rng.integers(
        0,
        np.iinfo(np.uint64).max,
        size=int(replicas),
        dtype=np.uint64,
    )
    if not np.array_equal(
        np.asarray(arrays["shared_B_standard"]), expected_B
    ):
        raise ArchiveValidationError(
            "homogenization B master does not match its outer seed"
        )
    if not np.array_equal(
        np.asarray(arrays["shared_a_standard"]), expected_a
    ):
        raise ArchiveValidationError(
            "homogenization a master does not match its outer seed"
        )
    if not np.array_equal(seeds.astype(np.uint64), expected_seeds):
        raise ArchiveValidationError(
            "homogenization W-replica seeds do not match the outer seed"
        )


@dataclass(frozen=True)
class StageArchive:
    metadata: Mapping[str, Any]
    arrays: Mapping[str, Array]

    @property
    def stage(self) -> str:
        return str(self.metadata["stage"])

    @property
    def config(self) -> Mapping[str, Any]:
        return self.metadata["config"]


_ARCHIVE_REQUIRED_METADATA = (
    "schema_version",
    "stage",
    "sealed",
    "protocol_sha256",
    "config",
    "config_sha256",
    "source_hashes",
    "array_hashes",
    "seal_sha256",
)


def build_sealed_archive(
    *,
    stage: str,
    config: Mapping[str, Any],
    arrays: Mapping[str, Array],
    protocol_sha256: str,
    source_hashes: Mapping[str, str],
    schema_version: int = 1,
) -> StageArchive:
    """Build an in-memory archive using the schema accepted by the loader.

    This helper is useful for runner code and synthetic tests.  It performs no
    I/O and does not weaken validation: loading the returned mapping recomputes
    every hash.
    """

    if not stage:
        raise ArchiveValidationError("stage must be nonempty")
    if not isinstance(config, Mapping) or not config:
        raise ArchiveValidationError("config must be a nonempty mapping")
    normalized = {str(key): np.asarray(value) for key, value in arrays.items()}
    if not normalized:
        raise ArchiveValidationError("arrays must be nonempty")
    metadata: dict[str, Any] = {
        "schema_version": int(schema_version),
        "stage": str(stage),
        "sealed": True,
        "protocol_sha256": protocol_sha256,
        "config": dict(config),
        "config_sha256": _sha256_bytes(_canonical_json_bytes(config)),
        "source_hashes": dict(source_hashes),
        "array_hashes": {
            key: hash_array(value) for key, value in normalized.items()
        },
    }
    metadata["seal_sha256"] = _sha256_bytes(_canonical_json_bytes(metadata))
    archive = StageArchive(metadata=metadata, arrays=normalized)
    return validate_sealed_stage_archive(
        archive,
        required_config_keys=(),
        required_arrays=tuple(normalized),
    )


def _nested_config_value(config: Mapping[str, Any], dotted_key: str) -> Any:
    value: Any = config
    for part in dotted_key.split("."):
        if not isinstance(value, Mapping) or part not in value:
            raise ArchiveValidationError(
                f"missing required config key: {dotted_key}"
            )
        value = value[part]
    return value


def _read_archive_source(
    source: StageArchive | Mapping[str, Any] | str | Path,
) -> StageArchive:
    if isinstance(source, StageArchive):
        return source
    if isinstance(source, (str, Path)):
        path = Path(source)
        if path.suffix != ".npz":
            raise ArchiveValidationError("sealed archive path must be .npz")
        try:
            with np.load(path, allow_pickle=False) as handle:
                if "metadata_json" not in handle.files:
                    raise ArchiveValidationError(
                        "archive is missing metadata_json"
                    )
                raw = np.asarray(handle["metadata_json"])
                if raw.shape != ():
                    raise ArchiveValidationError(
                        "metadata_json must be a scalar string"
                    )
                text = raw.item()
                if isinstance(text, bytes):
                    text = text.decode("utf-8")
                if not isinstance(text, str):
                    raise ArchiveValidationError(
                        "metadata_json must decode to text"
                    )
                metadata = json.loads(text)
                arrays = {
                    key: np.asarray(handle[key])
                    for key in handle.files
                    if key != "metadata_json"
                }
        except ArchiveValidationError:
            raise
        except Exception as exc:  # pragma: no cover - exact backend varies
            raise ArchiveValidationError(
                f"could not read sealed archive: {exc}"
            ) from exc
        return StageArchive(metadata=metadata, arrays=arrays)
    if not isinstance(source, Mapping):
        raise ArchiveValidationError("unsupported archive source")
    missing = {"metadata", "arrays"} - set(source)
    if missing:
        raise ArchiveValidationError(
            f"archive mapping missing keys: {sorted(missing)}"
        )
    metadata = source["metadata"]
    arrays = source["arrays"]
    if not isinstance(metadata, Mapping) or not isinstance(arrays, Mapping):
        raise ArchiveValidationError(
            "archive metadata and arrays must be mappings"
        )
    return StageArchive(
        metadata=dict(metadata),
        arrays={str(key): np.asarray(value) for key, value in arrays.items()},
    )


def validate_sealed_stage_archive(
    source: StageArchive | Mapping[str, Any] | str | Path,
    *,
    required_config_keys: Sequence[str],
    required_arrays: Sequence[str],
    expected_stage: str | None = None,
    expected_protocol_sha256: str | None = None,
    expected_source_hashes: Mapping[str, str] | None = None,
) -> StageArchive:
    """Load and cryptographically validate a sealed stage archive.

    The caller must explicitly declare the config and array keys needed for
    its analysis.  Missing provenance, unhashed arrays, extra unbound arrays,
    malformed hashes, and config/hash mismatches all fail closed.
    """

    archive = _read_archive_source(source)
    metadata = dict(archive.metadata)
    missing = set(_ARCHIVE_REQUIRED_METADATA) - set(metadata)
    if missing:
        raise ArchiveValidationError(
            f"missing provenance keys: {sorted(missing)}"
        )
    if metadata["schema_version"] != 1:
        raise ArchiveValidationError("unsupported archive schema_version")
    if metadata["sealed"] is not True:
        raise ArchiveValidationError("archive is not sealed")
    if not isinstance(metadata["stage"], str) or not metadata["stage"]:
        raise ArchiveValidationError("stage provenance is malformed")
    if expected_stage is not None and metadata["stage"] != expected_stage:
        raise ArchiveValidationError(
            f"stage mismatch: {metadata['stage']} != {expected_stage}"
        )
    if not _valid_sha256(metadata["protocol_sha256"]):
        raise ArchiveValidationError("protocol_sha256 is malformed")
    if (
        expected_protocol_sha256 is not None
        and metadata["protocol_sha256"] != expected_protocol_sha256
    ):
        raise ArchiveValidationError("protocol hash mismatch")

    config = metadata["config"]
    if not isinstance(config, Mapping) or not config:
        raise ArchiveValidationError("config provenance must be nonempty")
    for key in required_config_keys:
        _nested_config_value(config, key)
    config_hash = _sha256_bytes(_canonical_json_bytes(config))
    if config_hash != metadata["config_sha256"]:
        raise ArchiveValidationError("config hash mismatch")

    source_hashes = metadata["source_hashes"]
    if not isinstance(source_hashes, Mapping) or not source_hashes:
        raise ArchiveValidationError("source_hashes must be nonempty")
    if any(
        not isinstance(key, str) or not _valid_sha256(value)
        for key, value in source_hashes.items()
    ):
        raise ArchiveValidationError("source_hashes are malformed")
    if expected_source_hashes is not None:
        for key, value in expected_source_hashes.items():
            if source_hashes.get(key) != value:
                raise ArchiveValidationError(
                    f"source hash mismatch for {key}"
                )

    array_hashes = metadata["array_hashes"]
    if not isinstance(array_hashes, Mapping) or not array_hashes:
        raise ArchiveValidationError("array_hashes must be nonempty")
    array_keys = set(archive.arrays)
    hashed_keys = set(array_hashes)
    if array_keys != hashed_keys:
        raise ArchiveValidationError(
            "array inventory is not exactly hash-bound"
        )
    for key in required_arrays:
        if key not in archive.arrays:
            raise ArchiveValidationError(
                f"missing required array: {key}"
            )
    for key, expected in array_hashes.items():
        if not _valid_sha256(expected):
            raise ArchiveValidationError(
                f"malformed array hash for {key}"
            )
        if hash_array(archive.arrays[key]) != expected:
            raise ArchiveValidationError(f"array hash mismatch for {key}")

    if not _valid_sha256(metadata["seal_sha256"]):
        raise ArchiveValidationError("seal_sha256 is malformed")
    without_seal = dict(metadata)
    seal = without_seal.pop("seal_sha256")
    if _sha256_bytes(_canonical_json_bytes(without_seal)) != seal:
        raise ArchiveValidationError("stage seal mismatch")
    return StageArchive(metadata=metadata, arrays=archive.arrays)


def load_sealed_stage_archive(
    source: StageArchive | Mapping[str, Any] | str | Path,
    *,
    required_config_keys: Sequence[str],
    required_arrays: Sequence[str],
    expected_stage: str | None = None,
    expected_protocol_sha256: str | None = None,
    expected_source_hashes: Mapping[str, str] | None = None,
) -> StageArchive:
    return validate_sealed_stage_archive(
        source,
        required_config_keys=required_config_keys,
        required_arrays=required_arrays,
        expected_stage=expected_stage,
        expected_protocol_sha256=expected_protocol_sha256,
        expected_source_hashes=expected_source_hashes,
    )


def finalize_runner_stage_archive(
    source: StageArchive | Mapping[str, Any] | str | Path,
    *,
    frozen_inputs_sha256: str,
    required_config_keys: Sequence[str],
    required_arrays: Sequence[str],
    expected_stage: str | None = None,
    expected_protocol_sha256: str | None = None,
    expected_source_hashes: Mapping[str, str] | None = None,
) -> StageArchive:
    """Convert one atomic ``run_study`` result into the sealed schema.

    ``run_study.atomic_save_npz`` guarantees atomic publication and binds its
    scientific configuration, but intentionally does not hash the array
    inventory.  Analysis must therefore call this explicit finalizer before a
    runner archive is admissible.  The finalizer validates the runner
    provenance, binds every array byte, and includes the frozen-input manifest
    hash in the resulting stage seal.  A raw runner archive is *not* accepted
    by :func:`load_sealed_stage_archive`.
    """

    if not _valid_sha256(frozen_inputs_sha256):
        raise ArchiveValidationError("frozen_inputs_sha256 is malformed")
    runner = _read_archive_source(source)
    metadata = dict(runner.metadata)
    required_metadata = {
        "archive_schema",
        "stage",
        "protocol_sha256",
        "source_sha256",
        "config",
        "config_sha256",
    }
    missing = required_metadata - set(metadata)
    if missing:
        raise ArchiveValidationError(
            f"runner archive missing provenance keys: {sorted(missing)}"
        )
    if metadata["archive_schema"] != 1:
        raise ArchiveValidationError("unsupported runner archive_schema")
    stage = metadata["stage"]
    if not isinstance(stage, str) or not stage:
        raise ArchiveValidationError("runner stage provenance is malformed")
    if expected_stage is not None and stage != expected_stage:
        raise ArchiveValidationError(
            f"runner stage mismatch: {stage} != {expected_stage}"
        )
    protocol_hash = metadata["protocol_sha256"]
    if not _valid_sha256(protocol_hash):
        raise ArchiveValidationError(
            "runner protocol_sha256 is malformed"
        )
    if (
        expected_protocol_sha256 is not None
        and protocol_hash != expected_protocol_sha256
    ):
        raise ArchiveValidationError("runner protocol hash mismatch")
    config = metadata["config"]
    if not isinstance(config, Mapping) or not config:
        raise ArchiveValidationError(
            "runner config provenance must be nonempty"
        )
    for key in required_config_keys:
        _nested_config_value(config, key)
    if (
        _sha256_bytes(_canonical_json_bytes(config))
        != metadata["config_sha256"]
    ):
        raise ArchiveValidationError("runner config hash mismatch")
    source_hashes = metadata["source_sha256"]
    if not isinstance(source_hashes, Mapping) or not source_hashes:
        raise ArchiveValidationError(
            "runner source_sha256 must be a nonempty mapping"
        )
    if any(
        not isinstance(key, str) or not _valid_sha256(value)
        for key, value in source_hashes.items()
    ):
        raise ArchiveValidationError(
            "runner source_sha256 entries are malformed"
        )
    if expected_source_hashes is not None:
        for key, value in expected_source_hashes.items():
            if source_hashes.get(key) != value:
                raise ArchiveValidationError(
                    f"runner source hash mismatch for {key}"
                )
    embedded_freeze = metadata.get("frozen_inputs_sha256")
    if (
        embedded_freeze is not None
        and embedded_freeze != frozen_inputs_sha256
    ):
        raise ArchiveValidationError(
            "runner frozen-input manifest hash mismatch"
        )
    for key in required_arrays:
        if key not in runner.arrays:
            raise ArchiveValidationError(
                f"runner archive missing required array: {key}"
            )
    for key, value in runner.arrays.items():
        if value.dtype.hasobject:
            raise ArchiveValidationError(
                f"runner archive contains object array: {key}"
            )
        if value.dtype.kind in "fc" and not np.all(np.isfinite(value)):
            raise ArchiveValidationError(
                f"runner archive contains nonfinite array: {key}"
            )

    sealed_metadata: dict[str, Any] = {
        "schema_version": 1,
        "stage": stage,
        "sealed": True,
        "protocol_sha256": protocol_hash,
        "config": dict(config),
        "config_sha256": metadata["config_sha256"],
        "source_hashes": dict(source_hashes),
        "array_hashes": {
            key: hash_array(value) for key, value in runner.arrays.items()
        },
        "frozen_inputs_sha256": frozen_inputs_sha256,
        "runner_metadata": metadata,
        "runner_metadata_sha256": _sha256_bytes(
            _canonical_json_bytes(metadata)
        ),
    }
    sealed_metadata["seal_sha256"] = _sha256_bytes(
        _canonical_json_bytes(sealed_metadata)
    )
    sealed = StageArchive(
        metadata=sealed_metadata,
        arrays=runner.arrays,
    )
    return validate_sealed_stage_archive(
        sealed,
        required_config_keys=required_config_keys,
        required_arrays=required_arrays,
        expected_stage=expected_stage,
        expected_protocol_sha256=expected_protocol_sha256,
        expected_source_hashes=expected_source_hashes,
    )


def _strict_grid(values: Iterable[float], name: str) -> Array:
    result = np.asarray(tuple(values), dtype=float)
    if result.ndim != 1 or result.size == 0:
        raise ValueError(f"{name} must be a nonempty one-dimensional grid")
    if not np.all(np.isfinite(result)) or np.any(np.diff(result) <= 0.0):
        raise ValueError(f"{name} must be finite and strictly increasing")
    return result


@dataclass(frozen=True)
class AlignmentGrid:
    times: Array
    depths: Array

    def __post_init__(self) -> None:
        object.__setattr__(self, "times", _strict_grid(self.times, "times"))
        object.__setattr__(
            self, "depths", _strict_grid(self.depths, "depths")
        )


@dataclass(frozen=True)
class ObservableCurve:
    times: Array
    depths: Array
    f: Array
    gram: Array

    def __post_init__(self) -> None:
        times = _strict_grid(self.times, "curve times")
        depths = _strict_grid(self.depths, "curve depths")
        f = np.asarray(self.f, dtype=float)
        gram = np.asarray(self.gram, dtype=float)
        if f.ndim != 2 or f.shape[0] != times.size:
            raise ValueError("f must have shape (time, sample)")
        if (
            gram.ndim != 4
            or gram.shape[0] != times.size
            or gram.shape[1] != depths.size
            or gram.shape[2:] != (f.shape[1], f.shape[1])
        ):
            raise ValueError(
                "gram must have shape (time, depth, sample, sample)"
            )
        if not np.all(np.isfinite(f)) or not np.all(np.isfinite(gram)):
            raise ValueError("curve arrays must be finite")
        object.__setattr__(self, "times", times)
        object.__setattr__(self, "depths", depths)
        object.__setattr__(self, "f", f)
        object.__setattr__(self, "gram", gram)


@dataclass(frozen=True)
class ObservableEnsemble:
    root_ids: Array
    times: Array
    depths: Array
    f: Array
    gram: Array

    def __post_init__(self) -> None:
        roots = np.asarray(self.root_ids)
        times = _strict_grid(self.times, "ensemble times")
        depths = _strict_grid(self.depths, "ensemble depths")
        f = np.asarray(self.f, dtype=float)
        gram = np.asarray(self.gram, dtype=float)
        if roots.ndim != 1 or roots.size == 0:
            raise ValueError("root_ids must be nonempty and one-dimensional")
        if np.unique(roots).size != roots.size:
            raise ValueError("root_ids must be unique")
        if f.ndim != 3 or f.shape[:2] != (roots.size, times.size):
            raise ValueError("ensemble f must have shape (root,time,sample)")
        if (
            gram.ndim != 5
            or gram.shape[:3] != (roots.size, times.size, depths.size)
            or gram.shape[3:] != (f.shape[2], f.shape[2])
        ):
            raise ValueError(
                "ensemble gram must have shape "
                "(root,time,depth,sample,sample)"
            )
        if not np.all(np.isfinite(f)) or not np.all(np.isfinite(gram)):
            raise ValueError("ensemble arrays must be finite")
        object.__setattr__(self, "root_ids", roots)
        object.__setattr__(self, "times", times)
        object.__setattr__(self, "depths", depths)
        object.__setattr__(self, "f", f)
        object.__setattr__(self, "gram", gram)

    @property
    def roots(self) -> int:
        return int(self.root_ids.size)


def _interp_first_axis(old: Array, values: Array, new: Array) -> Array:
    if new[0] < old[0] - 1e-12 or new[-1] > old[-1] + 1e-12:
        raise ValueError("alignment grid would extrapolate")
    flat = np.asarray(values, dtype=float).reshape(old.size, -1)
    result = np.empty((new.size, flat.shape[1]), dtype=float)
    for column in range(flat.shape[1]):
        result[:, column] = np.interp(new, old, flat[:, column])
    return result.reshape((new.size,) + values.shape[1:])


def align_curve(curve: ObservableCurve, grid: AlignmentGrid) -> ObservableCurve:
    f = _interp_first_axis(curve.times, curve.f, grid.times)
    gram_time = _interp_first_axis(curve.times, curve.gram, grid.times)
    swapped = np.swapaxes(gram_time, 0, 1)
    gram_depth = _interp_first_axis(curve.depths, swapped, grid.depths)
    gram = np.swapaxes(gram_depth, 0, 1)
    return ObservableCurve(grid.times, grid.depths, f, gram)


def align_ensemble(
    ensemble: ObservableEnsemble, grid: AlignmentGrid
) -> ObservableEnsemble:
    f = np.stack(
        [
            _interp_first_axis(ensemble.times, member, grid.times)
            for member in ensemble.f
        ]
    )
    grams: list[Array] = []
    for member in ensemble.gram:
        gram_time = _interp_first_axis(ensemble.times, member, grid.times)
        gram_depth = _interp_first_axis(
            ensemble.depths, np.swapaxes(gram_time, 0, 1), grid.depths
        )
        grams.append(np.swapaxes(gram_depth, 0, 1))
    return ObservableEnsemble(
        ensemble.root_ids,
        grid.times,
        grid.depths,
        f,
        np.stack(grams),
    )


def ensemble_mean(
    ensemble: ObservableEnsemble, indices: Array | None = None
) -> ObservableCurve:
    if indices is None:
        indices = np.arange(ensemble.roots)
    indices = np.asarray(indices, dtype=int)
    return ObservableCurve(
        ensemble.times,
        ensemble.depths,
        np.mean(ensemble.f[indices], axis=0),
        np.mean(ensemble.gram[indices], axis=0),
    )


@dataclass(frozen=True)
class FullCurveDistance:
    combined: float
    output: float
    gram: float
    output_scale: float
    gram_scale: float
    mode: str


def _curve_array_distance(
    left_f: Array,
    left_gram: Array,
    right_f: Array,
    right_gram: Array,
    *,
    s_f: float,
    s_g: float,
) -> FullCurveDistance:
    if s_f <= 0.0 or s_g <= 0.0:
        raise ValueError("observable scales must be positive")
    output = float(
        np.max(np.linalg.norm(left_f - right_f, axis=-1)) / s_f
    )
    gram = float(
        np.max(
            np.linalg.norm(left_gram - right_gram, axis=(-2, -1))
        )
        / s_g
    )
    return FullCurveDistance(
        combined=max(output, gram),
        output=output,
        gram=gram,
        output_scale=float(s_f),
        gram_scale=float(s_g),
        mode="absolute",
    )


def full_curve_distance(
    left: ObservableCurve,
    right: ObservableCurve,
    *,
    grid: AlignmentGrid,
    s_f: float,
    s_g: float,
    mode: str = "absolute",
    motion_floor: float = 0.05,
) -> FullCurveDistance:
    """Fixed full-curve distance after declared time/depth alignment."""

    left_aligned = align_curve(left, grid)
    right_aligned = align_curve(right, grid)
    if left_aligned.f.shape != right_aligned.f.shape:
        raise ValueError("curves have different sample dimensions")
    if mode == "absolute":
        return _curve_array_distance(
            left_aligned.f,
            left_aligned.gram,
            right_aligned.f,
            right_aligned.gram,
            s_f=s_f,
            s_g=s_g,
        )
    if mode != "motion":
        raise ValueError("mode must be 'absolute' or 'motion'")
    if motion_floor <= 0.0:
        raise ValueError("motion_floor must be positive")
    lf = left_aligned.f - left_aligned.f[:1]
    rf = right_aligned.f - right_aligned.f[:1]
    lg = left_aligned.gram - left_aligned.gram[:1]
    rg = right_aligned.gram - right_aligned.gram[:1]
    f_scale = max(
        float(np.max(np.linalg.norm(lf, axis=-1))),
        float(np.max(np.linalg.norm(rf, axis=-1))),
        motion_floor,
    )
    g_scale = max(
        float(np.max(np.linalg.norm(lg, axis=(-2, -1)))),
        float(np.max(np.linalg.norm(rg, axis=(-2, -1)))),
        motion_floor,
    )
    result = _curve_array_distance(
        lf, lg, rf, rg, s_f=f_scale, s_g=g_scale
    )
    return FullCurveDistance(
        combined=result.combined,
        output=result.output,
        gram=result.gram,
        output_scale=f_scale,
        gram_scale=g_scale,
        mode="motion",
    )


@dataclass(frozen=True)
class FamilywiseBootstrapBand:
    point: Mapping[str, Array]
    lower: Mapping[str, Array]
    upper: Mapping[str, Array]
    critical_lower: float
    critical_upper: float
    replicates: Mapping[str, Array]
    confidence: float
    seed: int
    pilot_replicates: int
    critical_replicates: int
    critical_order_index: int
    critical_order_assurance: float
    mc_failure_probability: float


def _normalize_statistic(
    result: Mapping[str, Array | float],
) -> dict[str, Array]:
    normalized: dict[str, Array] = {}
    for key, value in result.items():
        array = np.asarray(value, dtype=float)
        if not np.all(np.isfinite(array)):
            raise ValueError(f"statistic {key} is nonfinite")
        normalized[str(key)] = array
    if not normalized:
        raise ValueError("statistic must return at least one value")
    return normalized


def _mc_upper_quantile_index(
    *,
    replicates: int,
    probability: float,
    failure_probability: float,
) -> tuple[int, float]:
    """Return a binomially guarded zero-based empirical-quantile index.

    If ``c_probability`` is the target quantile of an i.i.d. calibration
    distribution, the selected order statistic is at least
    ``c_probability`` with probability at least
    ``1 - failure_probability`` over the finite calibration draw.  This
    explicitly budgets Monte-Carlo error instead of treating an empirical
    quantile as exact.
    """

    if replicates < 1:
        raise ValueError("calibration replicate count must be positive")
    if not 0.5 < probability < 1.0:
        raise ValueError("quantile probability must lie in (0.5,1)")
    if not 0.0 < failure_probability < 1.0:
        raise ValueError("MC failure probability must lie in (0,1)")
    successes = int(
        binom.ppf(1.0 - failure_probability, replicates, probability)
    )
    index = successes
    if index >= replicates:
        raise ValueError(
            "finite calibration sample cannot attain the declared "
            "quantile assurance"
        )
    assurance = float(binom.cdf(index, replicates, probability))
    if assurance + 64.0 * np.finfo(float).eps < 1.0 - failure_probability:
        raise ValueError("binomial quantile assurance calculation failed")
    return index, assurance


def _conservative_quantile(values: Array, probability: float) -> float:
    """Higher empirical quantile for descriptive, non-calibration summaries."""

    return float(np.quantile(values, probability, method="higher"))


def _collect_bootstrap_draws(
    *,
    point: Mapping[str, Array],
    draws: Iterable[Mapping[str, Array | float]],
    expected_count: int,
) -> dict[str, Array]:
    if expected_count < 2:
        raise ValueError("at least two bootstrap draws are required")
    shapes = {key: value.shape for key, value in point.items()}
    storage = {
        key: np.empty((expected_count,) + shape, dtype=float)
        for key, shape in shapes.items()
    }
    count = 0
    for raw in draws:
        if count >= expected_count:
            raise ValueError("bootstrap draw stream is longer than declared")
        current = _normalize_statistic(raw)
        if set(current) != set(point):
            raise ValueError("bootstrap statistic keys changed across draws")
        for key, value in current.items():
            if value.shape != shapes[key]:
                raise ValueError(
                    f"bootstrap statistic shape changed for {key}"
                )
            storage[key][count] = value
        count += 1
    if count != expected_count:
        raise ValueError(
            f"bootstrap draw stream has {count} draws, expected "
            f"{expected_count}"
        )
    return storage


def _familywise_band_from_independent_draws(
    *,
    point: Mapping[str, Array | float],
    pilot_draws: Iterable[Mapping[str, Array | float]],
    pilot_replicates: int,
    calibration_draws: Iterable[Mapping[str, Array | float]],
    critical_replicates: int,
    confidence: float,
    mc_failure_probability: float,
    seed: int,
) -> FamilywiseBootstrapBand:
    """Build one two-sided absolute-max band from independent draw batches."""

    normalized_point = _normalize_statistic(point)
    pilot_storage = _collect_bootstrap_draws(
        point=normalized_point,
        draws=pilot_draws,
        expected_count=pilot_replicates,
    )
    scales: dict[str, Array] = {}
    for key, values in pilot_storage.items():
        scale = np.std(values, axis=0, ddof=1)
        numerical_floor = (
            64.0
            * np.finfo(float).eps
            * np.maximum(1.0, np.abs(normalized_point[key]))
        )
        scales[key] = np.maximum(scale, numerical_floor)

    storage = _collect_bootstrap_draws(
        point=normalized_point,
        draws=calibration_draws,
        expected_count=critical_replicates,
    )
    absolute_max = np.full(critical_replicates, -np.inf, dtype=float)
    for key, values in storage.items():
        standardized = np.abs(
            (values - normalized_point[key]) / scales[key]
        )
        flat = standardized.reshape(critical_replicates, -1)
        absolute_max = np.maximum(absolute_max, np.max(flat, axis=1))
    order_index, assurance = _mc_upper_quantile_index(
        replicates=critical_replicates,
        probability=confidence,
        failure_probability=mc_failure_probability,
    )
    critical = max(
        0.0,
        float(np.partition(absolute_max, order_index)[order_index]),
    )
    return FamilywiseBootstrapBand(
        point=normalized_point,
        lower={
            key: value - critical * scales[key]
            for key, value in normalized_point.items()
        },
        upper={
            key: value + critical * scales[key]
            for key, value in normalized_point.items()
        },
        critical_lower=critical,
        critical_upper=critical,
        replicates=storage,
        confidence=confidence,
        seed=seed,
        pilot_replicates=pilot_replicates,
        critical_replicates=critical_replicates,
        critical_order_index=order_index,
        critical_order_assurance=assurance,
        mc_failure_probability=mc_failure_probability,
    )


def whole_root_familywise_bootstrap(
    *,
    root_count: int,
    statistic: Statistic,
    replicates: int,
    pilot_replicates: int,
    seed: int,
    confidence: float,
    mc_failure_probability: float,
) -> FamilywiseBootstrapBand:
    """One simultaneous max-standardized band from coupled whole-root draws.

    The statistic may contain heterogeneous quantities (for example,
    dimensionless contraction ratios, log--log slopes, and normalized curve
    errors).  Taking a maximum of their *raw* bootstrap deviations would be
    unit dependent and would let the numerically largest quantity determine
    every interval.  We therefore estimate a bootstrap scale separately for
    each scalar component, take the maximum standardized deviation over the
    complete supplied family, and then transform the common critical value
    back to each component's native units.

    This controls the family supplied to this call.  Independent scientific
    stages use a preregistered Bonferroni allocation because their Gaussian
    roots, quadrature scrambles, and attack roots are not one exchangeable
    bootstrap population.
    """

    if root_count < 2:
        raise ValueError("at least two roots are required")
    if replicates < 2 or pilot_replicates < 2:
        raise ValueError("pilot and calibration replicates must be at least two")
    if not 0.5 < confidence < 1.0:
        raise ValueError("confidence must lie in (0.5,1)")
    all_indices = np.arange(root_count, dtype=int)
    point = _normalize_statistic(statistic(all_indices))
    pilot_seed, calibration_seed = np.random.SeedSequence(seed).spawn(2)
    pilot_rng = np.random.default_rng(pilot_seed)
    calibration_rng = np.random.default_rng(calibration_seed)

    def draw_stream(
        rng: np.random.Generator, count: int
    ) -> Iterable[Mapping[str, Array | float]]:
        for _draw in range(count):
            indices = rng.integers(0, root_count, size=root_count)
            yield statistic(indices)

    return _familywise_band_from_independent_draws(
        point=point,
        pilot_draws=draw_stream(pilot_rng, pilot_replicates),
        pilot_replicates=pilot_replicates,
        calibration_draws=draw_stream(calibration_rng, replicates),
        critical_replicates=replicates,
        confidence=confidence,
        mc_failure_probability=mc_failure_probability,
        seed=seed,
    )


def _familywise_band_from_explicit_draws(
    *,
    point: Mapping[str, Array | float],
    pilot_draws: Iterable[Mapping[str, Array | float]],
    pilot_replicates: int,
    draws: Iterable[Mapping[str, Array | float]],
    replicates: int,
    confidence: float,
    mc_failure_probability: float,
    seed: int,
) -> FamilywiseBootstrapBand:
    """Build the standard band from independent pilot/calibration streams."""

    return _familywise_band_from_independent_draws(
        point=point,
        pilot_draws=pilot_draws,
        pilot_replicates=pilot_replicates,
        calibration_draws=draws,
        critical_replicates=replicates,
        confidence=confidence,
        mc_failure_probability=mc_failure_probability,
        seed=seed,
    )


def _distance_same_grid(
    left: ObservableCurve,
    right: ObservableCurve,
    *,
    s_f: float,
    s_g: float,
) -> float:
    return _curve_array_distance(
        left.f,
        left.gram,
        right.f,
        right.gram,
        s_f=s_f,
        s_g=s_g,
    ).combined


def _mean_curve_from_arrays(
    ensemble: ObservableEnsemble, indices: Array
) -> ObservableCurve:
    return ensemble_mean(ensemble, indices)


def _root_concentration_radius(
    ensemble: ObservableEnsemble,
    indices: Array,
    *,
    s_f: float,
    s_g: float,
    quantile: float,
) -> float:
    mean = ensemble_mean(ensemble, indices)
    distances = []
    for root in indices:
        member = ObservableCurve(
            ensemble.times,
            ensemble.depths,
            ensemble.f[root],
            ensemble.gram[root],
        )
        distances.append(
            _distance_same_grid(member, mean, s_f=s_f, s_g=s_g)
        )
    return _conservative_quantile(np.asarray(distances), quantile)


def _log_slope(x: Sequence[float], y: Sequence[float]) -> float:
    x_array = np.asarray(x, dtype=float)
    y_array = np.asarray(y, dtype=float)
    if x_array.size < 2 or np.any(x_array <= 0.0):
        raise ValueError("log slope requires at least two positive x values")
    if np.any(y_array <= 0.0):
        raise ValueError("log slope requires positive y values")
    return float(np.polyfit(np.log(x_array), np.log(y_array), 1)[0])


def _add_scaled_curve(
    base: ObservableCurve, correction: ObservableCurve, scale: float
) -> ObservableCurve:
    return ObservableCurve(
        base.times,
        base.depths,
        base.f + scale * correction.f,
        base.gram + scale * correction.gram,
    )


def _curve_difference(
    later: ObservableCurve, earlier: ObservableCurve
) -> ObservableCurve:
    return ObservableCurve(
        later.times,
        later.depths,
        later.f - earlier.f,
        later.gram - earlier.gram,
    )


def _geometric_extrapolation(
    curves: Sequence[ObservableCurve],
    *,
    s_f: float,
    s_g: float,
    ratio_cap: float = 0.999,
) -> tuple[ObservableCurve, list[float], list[float], float | None]:
    """Return the finest curve plus a conditional geometric *radius*.

    Norm-ratio contraction does not establish that successive vector
    corrections point in a common direction.  Consequently we never add a
    scalar multiple of the last correction to manufacture an extrapolated
    curve.  The finest resolved curve remains the center, while
    ``correction_last * r / (1-r)`` is carried only as a conditional norm-ball
    radius.
    """

    corrections = [
        _distance_same_grid(curves[index + 1], curves[index], s_f=s_f, s_g=s_g)
        for index in range(len(curves) - 1)
    ]
    ratios = [
        corrections[index + 1] / corrections[index]
        if corrections[index] > 0.0
        else np.inf
        for index in range(len(corrections) - 1)
    ]
    if not ratios or not np.isfinite(ratios[-1]) or ratios[-1] >= 1.0:
        return curves[-1], corrections, ratios, None
    ratio = min(max(ratios[-1], 0.0), ratio_cap)
    tail = corrections[-1] * ratio / (1.0 - ratio)
    return curves[-1], corrections, ratios, tail


def _depth_corrections_with_width_balls(
    curves: Sequence[ObservableCurve],
    width_tail_radii: Sequence[float | None],
    *,
    s_f: float,
    s_g: float,
) -> tuple[list[float], list[float], float | None]:
    """Propagate conditional width-tail balls into depth corrections."""

    if len(curves) != len(width_tail_radii):
        raise ValueError("depth curves and width-tail radii disagree")
    corrections: list[float] = []
    for index in range(len(curves) - 1):
        left = width_tail_radii[index]
        right = width_tail_radii[index + 1]
        if left is None or right is None:
            corrections.append(1e6)
        else:
            corrections.append(
                _distance_same_grid(
                    curves[index + 1],
                    curves[index],
                    s_f=s_f,
                    s_g=s_g,
                )
                + float(left)
                + float(right)
            )
    ratios = [
        corrections[index + 1] / corrections[index]
        if corrections[index] > 0.0
        else np.inf
        for index in range(len(corrections) - 1)
    ]
    if not ratios or not np.isfinite(ratios[-1]) or ratios[-1] >= 1.0:
        return corrections, ratios, None
    ratio = min(max(ratios[-1], 0.0), 0.999)
    return (
        corrections,
        ratios,
        corrections[-1] * ratio / (1.0 - ratio),
    )


@dataclass(frozen=True)
class OrderedScalingSummary:
    widths: tuple[int, ...]
    depths: tuple[int, ...]
    concentration_radii: Mapping[int, Mapping[int, float]]
    concentration_slopes: Mapping[int, float]
    width_corrections: Mapping[int, tuple[float, ...]]
    width_ratios: Mapping[int, tuple[float, ...]]
    width_tail_conditional: Mapping[int, float | None]
    width_extrapolated: Mapping[int, ObservableCurve]
    depth_corrections: tuple[float, ...]
    depth_ratios: tuple[float, ...]
    depth_tail_conditional: float | None
    familywise_band: FamilywiseBootstrapBand
    gate: GateVerdict


def analyze_ordered_scaling(
    ensembles: Mapping[tuple[int, int], ObservableEnsemble],
    *,
    grid: AlignmentGrid,
    s_f: float,
    s_g: float,
    bootstrap_replicates: int,
    bootstrap_pilot_replicates: int,
    bootstrap_mc_failure_probability: float,
    bootstrap_seed: int,
    confidence: float = DEFAULT_STAGE_FAMILY_CONFIDENCE,
    concentration_quantile: float = 0.95,
    slope_upper_threshold: float = -0.25,
) -> OrderedScalingSummary:
    """Analyze width first at each L, then depth after width extrapolation."""

    if not ensembles:
        raise ValueError("scaling ensembles are empty")
    widths = tuple(sorted({int(key[0]) for key in ensembles}))
    depths = tuple(sorted({int(key[1]) for key in ensembles}))
    expected = {(n, depth) for n in widths for depth in depths}
    if set(ensembles) != expected:
        raise ValueError("scaling grid must be rectangular")
    aligned = {
        key: align_ensemble(value, grid) for key, value in ensembles.items()
    }
    first = aligned[(widths[0], depths[0])]
    for key, ensemble in aligned.items():
        if not np.array_equal(ensemble.root_ids, first.root_ids):
            raise ValueError(
                f"root IDs are not whole-root coupled at {key}"
            )
        if ensemble.f.shape[-1] != first.f.shape[-1]:
            raise ValueError("sample dimensions differ across scaling grid")

    def compute(indices: Array) -> Mapping[str, float]:
        means = {
            key: _mean_curve_from_arrays(value, indices)
            for key, value in aligned.items()
        }
        result: dict[str, float] = {}
        width_extrapolated: dict[int, ObservableCurve] = {}
        for depth in depths:
            radii = [
                _root_concentration_radius(
                    aligned[(width, depth)],
                    indices,
                    s_f=s_f,
                    s_g=s_g,
                    quantile=concentration_quantile,
                )
                for width in widths
            ]
            for width, radius in zip(widths, radii):
                result[f"concentration/L{depth}/n{width}"] = radius
            result[f"concentration_slope/L{depth}"] = _log_slope(
                widths, radii
            )
            curves = [means[(width, depth)] for width in widths]
            extrapolated, corrections, ratios, tail = (
                _geometric_extrapolation(
                    curves, s_f=s_f, s_g=s_g
                )
            )
            width_extrapolated[depth] = extrapolated
            for index, correction in enumerate(corrections):
                result[f"width_correction/L{depth}/{index}"] = correction
            for index, ratio in enumerate(ratios):
                # A finite capped value keeps bootstrap families auditable;
                # the uncapped point ratio still determines the gate.
                result[f"width_ratio/L{depth}/{index}"] = min(
                    ratio, 1e6
                )
            result[f"width_tail_conditional/L{depth}"] = (
                tail if tail is not None else 1e6
            )
        depth_curves = [width_extrapolated[depth] for depth in depths]
        width_tail_radii = [
            (
                result[f"width_tail_conditional/L{depth}"]
                if result[f"width_tail_conditional/L{depth}"] < 1e5
                else None
            )
            for depth in depths
        ]
        corrections, ratios, tail = _depth_corrections_with_width_balls(
            depth_curves,
            width_tail_radii,
            s_f=s_f,
            s_g=s_g,
        )
        for index, correction in enumerate(corrections):
            result[f"depth_correction/{index}"] = correction
        for index, ratio in enumerate(ratios):
            result[f"depth_ratio/{index}"] = min(ratio, 1e6)
        result["depth_tail_conditional"] = (
            tail if tail is not None else 1e6
        )
        return result

    band = whole_root_familywise_bootstrap(
        root_count=first.roots,
        statistic=compute,
        replicates=bootstrap_replicates,
        pilot_replicates=bootstrap_pilot_replicates,
        seed=bootstrap_seed,
        confidence=confidence,
        mc_failure_probability=bootstrap_mc_failure_probability,
    )
    all_indices = np.arange(first.roots)
    means = {
        key: ensemble_mean(value, all_indices)
        for key, value in aligned.items()
    }
    concentration: dict[int, dict[int, float]] = {}
    slopes: dict[int, float] = {}
    width_corrections: dict[int, tuple[float, ...]] = {}
    width_ratios: dict[int, tuple[float, ...]] = {}
    width_tails: dict[int, float | None] = {}
    extrapolated: dict[int, ObservableCurve] = {}
    for depth in depths:
        concentration[depth] = {
            width: float(
                band.point[f"concentration/L{depth}/n{width}"]
            )
            for width in widths
        }
        slopes[depth] = float(
            band.point[f"concentration_slope/L{depth}"]
        )
        curves = [means[(width, depth)] for width in widths]
        curve, corrections, ratios, tail = _geometric_extrapolation(
            curves, s_f=s_f, s_g=s_g
        )
        extrapolated[depth] = curve
        width_corrections[depth] = tuple(corrections)
        width_ratios[depth] = tuple(ratios)
        width_tails[depth] = tail
    (
        depth_corrections_list,
        depth_ratios_list,
        depth_tail,
    ) = _depth_corrections_with_width_balls(
        [extrapolated[depth] for depth in depths],
        [width_tails[depth] for depth in depths],
        s_f=s_f,
        s_g=s_g,
    )

    failures: list[str] = []
    unresolved: list[str] = []
    if len(widths) < 4:
        unresolved.append("ORDERED_INSUFFICIENT_WIDTH_LEVELS")
    if len(depths) < 4:
        unresolved.append("ORDERED_INSUFFICIENT_DEPTH_LEVELS")
    for depth in depths:
        name = f"concentration_slope/L{depth}"
        lower = float(band.lower[name])
        upper = float(band.upper[name])
        if lower >= slope_upper_threshold:
            failures.append("ORDERED_CONCENTRATION_NONCONTRACTING")
        elif upper >= slope_upper_threshold:
            unresolved.append("ORDERED_CONCENTRATION_SLOPE_UNRESOLVED")
        for index, ratio in enumerate(width_ratios[depth]):
            key = f"width_ratio/L{depth}/{index}"
            lower_ratio = float(band.lower[key])
            upper_ratio = float(band.upper[key])
            if lower_ratio >= 1.0:
                failures.append("ORDERED_WIDTH_RATIO_NONCONTRACTING")
            elif upper_ratio >= 1.0:
                unresolved.append("ORDERED_WIDTH_RATIO_UNRESOLVED")
    for index, ratio in enumerate(depth_ratios_list):
        key = f"depth_ratio/{index}"
        lower_ratio = float(band.lower[key])
        upper_ratio = float(band.upper[key])
        if lower_ratio >= 1.0:
            failures.append("ORDERED_DEPTH_RATIO_NONCONTRACTING")
        elif upper_ratio >= 1.0:
            unresolved.append("ORDERED_DEPTH_RATIO_UNRESOLVED")
    if failures:
        gate = GateVerdict(
            GateStatus.FAIL,
            tuple(sorted(set(failures))),
            {"conditional_geometric_tails": True},
        )
    elif unresolved:
        gate = GateVerdict(
            GateStatus.UNRESOLVED,
            tuple(sorted(set(unresolved))),
            {"conditional_geometric_tails": True},
        )
    else:
        gate = GateVerdict(
            GateStatus.PASS,
            ("ORDERED_SCALING_CONTRACTS_CONDITIONAL_TAIL",),
            {"conditional_geometric_tails": True},
        )
    return OrderedScalingSummary(
        widths=widths,
        depths=depths,
        concentration_radii=concentration,
        concentration_slopes=slopes,
        width_corrections=width_corrections,
        width_ratios=width_ratios,
        width_tail_conditional=width_tails,
        width_extrapolated=extrapolated,
        depth_corrections=tuple(depth_corrections_list),
        depth_ratios=tuple(depth_ratios_list),
        depth_tail_conditional=depth_tail,
        familywise_band=band,
        gate=gate,
    )


@dataclass(frozen=True)
class NumericalCauchySummary:
    discrepancies: Mapping[str, FullCurveDistance]
    upper_bounds: Mapping[str, float]
    gate: GateVerdict


def analyze_numerical_cauchy(
    curves: Mapping[str, ObservableCurve],
    comparisons: Sequence[tuple[str, str, str]],
    *,
    grid: AlignmentGrid,
    s_f: float,
    s_g: float,
    allocation: float,
    upper_bounds: Mapping[str, float] | None,
    discrepancy_lcb: float | None = None,
    nuisance_fraction: float = 0.2,
    mode: str = "absolute",
) -> NumericalCauchySummary:
    discrepancies: dict[str, FullCurveDistance] = {}
    for label, left, right in comparisons:
        if label in discrepancies:
            raise ValueError(f"duplicate Cauchy label: {label}")
        if left not in curves or right not in curves:
            raise ValueError(f"missing Cauchy curve for {label}")
        discrepancies[label] = full_curve_distance(
            curves[left],
            curves[right],
            grid=grid,
            s_f=s_f,
            s_g=s_g,
            mode=mode,
        )
    if upper_bounds is None:
        gate = GateVerdict(
            GateStatus.UNRESOLVED,
            ("CAUCHY_UNCERTAINTY_MISSING",),
            {"point_discrepancies": {k: v.combined for k, v in discrepancies.items()}},
        )
        return NumericalCauchySummary(discrepancies, {}, gate)
    missing = set(discrepancies) - set(upper_bounds)
    if missing:
        gate = GateVerdict(
            GateStatus.UNRESOLVED,
            ("CAUCHY_UPPER_BOUND_MISSING",),
            {"missing": sorted(missing)},
        )
        return NumericalCauchySummary(discrepancies, dict(upper_bounds), gate)
    failures: list[str] = []
    for label in discrepancies:
        upper = float(upper_bounds[label])
        if not np.isfinite(upper) or upper < 0.0:
            failures.append("CAUCHY_UPPER_BOUND_INVALID")
        elif upper > allocation:
            failures.append("CAUCHY_ALLOCATION_EXCEEDED")
        if (
            discrepancy_lcb is not None
            and upper >= nuisance_fraction * discrepancy_lcb
        ):
            failures.append("CAUCHY_NUISANCE_NOT_SEPARATED")
    gate = GateVerdict(
        GateStatus.FAIL if failures else GateStatus.PASS,
        tuple(sorted(set(failures)))
        if failures
        else ("CAUCHY_ALL_BOUNDS_WITHIN_ALLOCATION",),
        {"allocation": allocation, "discrepancy_lcb": discrepancy_lcb},
    )
    return NumericalCauchySummary(discrepancies, dict(upper_bounds), gate)


@dataclass(frozen=True)
class InnovationSamples:
    values: Array
    layered: bool

    def __post_init__(self) -> None:
        value = np.asarray(self.values, dtype=float)
        if value.ndim < 3:
            raise ValueError(
                "innovation values need outer-root, replica, and feature axes"
            )
        if value.shape[0] < 2 or value.shape[1] < 2:
            raise ValueError("at least two outer roots and replicas are required")
        if not np.all(np.isfinite(value)):
            raise ValueError("innovation samples must be finite")
        object.__setattr__(self, "values", value)


@dataclass(frozen=True)
class HomogenizationDepthSummary:
    variance: float
    rms: float
    cross_replica_bias_squared: float
    cross_replica_bias_norm: float
    covariance: Array
    integrated_covariance: float


@dataclass(frozen=True)
class HomogenizationFieldSummary:
    by_depth: Mapping[int, HomogenizationDepthSummary]
    variance_slope: float
    integrated_covariance_slope: float
    bias_squared_at_max_depth: float
    bias_squared_upper_at_max_depth: float
    bias_norm_at_max_depth: float
    bias_norm_upper_at_max_depth: float


@dataclass(frozen=True)
class HomogenizationSummary:
    fields: Mapping[str, HomogenizationFieldSummary]
    familywise_band: FamilywiseBootstrapBand
    gate: GateVerdict


def _homogenization_root_statistics(
    samples: InnovationSamples, depth: int
) -> tuple[Array, Array, Array]:
    values = samples.values
    outer, replicas = values.shape[:2]
    if samples.layered:
        if values.ndim < 4 or values.shape[2] != depth:
            raise ValueError(
                f"layered innovation at depth {depth} has wrong layer axis"
            )
        flattened = values.reshape(outer, replicas, depth, -1)
        averaged = np.mean(flattened, axis=2)
        centered = flattened - np.mean(flattened, axis=1, keepdims=True)
        covariance = np.einsum(
            "orld,orkd->olk",
            centered,
            centered,
            optimize=True,
        )
        covariance /= (replicas - 1) * flattened.shape[-1]
    else:
        flattened = values.reshape(outer, replicas, -1)
        averaged = flattened
        centered = flattened - np.mean(flattened, axis=1, keepdims=True)
        variance = np.sum(centered * centered, axis=(1, 2))
        variance /= (replicas - 1) * flattened.shape[-1]
        covariance = variance[:, None, None]

    if replicas % 2:
        raise ValueError(
            "the frozen split-pair bias estimator requires an even "
            "replica count"
        )
    feature_count = averaged.shape[-1]
    half = replicas // 2
    first_mean = np.mean(averaged[:, :half], axis=1)
    second_mean = np.mean(averaged[:, half:], axis=1)
    # The two fixed halves contain independent W replicas.  Their signed
    # cross product is an unbiased squared-mean estimator and remains valid
    # under separate within-half bootstrap resampling.
    bias_squared = np.sum(first_mean * second_mean, axis=1) / feature_count
    integrated = np.sum(covariance, axis=(1, 2)) / (
        covariance.shape[1] ** 2
    )
    return integrated, bias_squared, covariance


def _summarize_homogenization_samples(
    samples: InnovationSamples, depth: int, outer_indices: Array
) -> HomogenizationDepthSummary:
    integrated, bias_squared, covariance = _homogenization_root_statistics(
        samples, depth
    )
    variance = float(np.mean(integrated[outer_indices]))
    bias_sq = float(np.mean(bias_squared[outer_indices]))
    covariance_mean = np.mean(covariance[outer_indices], axis=0)
    return HomogenizationDepthSummary(
        variance=variance,
        rms=float(np.sqrt(max(variance, 0.0))),
        cross_replica_bias_squared=bias_sq,
        cross_replica_bias_norm=float(np.sqrt(max(bias_sq, 0.0))),
        covariance=covariance_mean,
        integrated_covariance=float(
            np.sum(covariance_mean) / covariance_mean.shape[0] ** 2
        ),
    )


def analyze_homogenization(
    fields: Mapping[str, Mapping[int, InnovationSamples]],
    *,
    model_free_fields: Sequence[str],
    candidate_fields: Sequence[str],
    candidate_bias_allocation: float,
    bootstrap_replicates: int,
    bootstrap_pilot_replicates: int,
    bootstrap_mc_failure_probability: float,
    bootstrap_seed: int,
    confidence: float = DEFAULT_STAGE_FAMILY_CONFIDENCE,
    expected_slope: float = -1.0,
    slope_upper_threshold: float = -0.5,
    conditional_mean_tested: bool = False,
    width_ladders: Mapping[str, Mapping[int, str]] | None = None,
) -> HomogenizationSummary:
    if not fields:
        raise ValueError("homogenization fields are empty")
    names = tuple(fields)
    depth_sets = {tuple(sorted(table)) for table in fields.values()}
    if len(depth_sets) != 1:
        raise ValueError("all homogenization fields need the same depths")
    depths = next(iter(depth_sets))
    if len(depths) < 2:
        raise ValueError("at least two depths are required")
    first = fields[names[0]][depths[0]]
    outer_roots = first.values.shape[0]
    replicas = first.values.shape[1]
    for name, table in fields.items():
        for depth, sample in table.items():
            if sample.values.shape[:2] != (outer_roots, replicas):
                raise ValueError(
                    f"outer-root/replica shape mismatch for {name}/{depth}"
                )
    nonlayered_inner_products: dict[tuple[str, int], Array] = {}
    for name, table in fields.items():
        for depth, sample in table.items():
            if sample.layered:
                continue
            flat = sample.values.reshape(outer_roots, replicas, -1)
            nonlayered_inner_products[(name, depth)] = (
                np.einsum("ori,osi->ors", flat, flat, optimize=True)
                / flat.shape[-1]
            )

    def resampled_nonlayered_summary(
        *,
        name: str,
        depth: int,
        outer_indices: Array,
        replica_indices: Array,
    ) -> HomogenizationDepthSummary:
        inner = nonlayered_inner_products[(name, depth)]
        variances = np.empty(outer_indices.size, dtype=float)
        bias_squared = np.empty_like(variances)
        half = replicas // 2
        for row, root in enumerate(outer_indices):
            chosen = replica_indices[row]
            matrix = inner[root][np.ix_(chosen, chosen)]
            variances[row] = (
                np.trace(matrix) - np.sum(matrix) / replicas
            ) / (replicas - 1)
            bias_squared[row] = float(
                np.sum(matrix[:half, half:]) / (half * half)
            )
        variance = float(np.mean(variances))
        bias_sq = float(np.mean(bias_squared))
        covariance = np.asarray([[variance]])
        return HomogenizationDepthSummary(
            variance=variance,
            rms=float(np.sqrt(max(variance, 0.0))),
            cross_replica_bias_squared=bias_sq,
            cross_replica_bias_norm=float(
                np.sqrt(max(bias_sq, 0.0))
            ),
            covariance=covariance,
            integrated_covariance=variance,
        )

    def compute(
        indices: Array,
        replica_indices: Array | None = None,
    ) -> Mapping[str, float]:
        result: dict[str, float] = {}
        computed: dict[
            tuple[str, int], HomogenizationDepthSummary
        ] = {}
        for name, table in fields.items():
            variances: list[float] = []
            integrated_values: list[float] = []
            for depth in depths:
                sample = table[depth]
                if replica_indices is not None:
                    if not sample.layered:
                        summary = resampled_nonlayered_summary(
                            name=name,
                            depth=depth,
                            outer_indices=indices,
                            replica_indices=replica_indices,
                        )
                        current_sample = None
                        current_indices = None
                    else:
                        selected = np.stack(
                            [
                                sample.values[root, replica_indices[row]]
                                for row, root in enumerate(indices)
                            ]
                        )
                        current_sample = InnovationSamples(
                            selected, layered=True
                        )
                        current_indices = np.arange(indices.size)
                else:
                    current_sample = sample
                    current_indices = indices
                if current_sample is not None:
                    summary = _summarize_homogenization_samples(
                        current_sample, depth, current_indices
                    )
                computed[(name, depth)] = summary
                result[f"{name}/variance/L{depth}"] = summary.variance
                result[f"{name}/integrated_covariance/L{depth}"] = (
                    summary.integrated_covariance
                )
                # Keep the off-diagonal U-statistic signed throughout the
                # bootstrap.  Applying sqrt(max(U, 0)) to each draw creates a
                # nonregular point mass at zero and can erase real
                # between-root uncertainty when every observed U is negative.
                result[f"{name}/bias_squared/L{depth}"] = (
                    summary.cross_replica_bias_squared
                )
                variances.append(max(summary.variance, 1e-300))
                integrated_values.append(
                    max(summary.integrated_covariance, 1e-300)
                )
            result[f"{name}/variance_slope"] = _log_slope(
                depths, variances
            )
            result[f"{name}/integrated_covariance_slope"] = _log_slope(
                depths, integrated_values
            )
        for group, ladder in (width_ladders or {}).items():
            widths = tuple(sorted(int(width) for width in ladder))
            if len(widths) < 3:
                raise ValueError(
                    "homogenization width diagnostics require three widths"
                )
            names_by_width = {
                int(width): str(name) for width, name in ladder.items()
            }
            for name in names_by_width.values():
                if name not in fields:
                    raise ValueError(
                        f"width diagnostic references unknown field {name}"
                    )
            for metric in (
                "variance",
                "integrated_covariance",
                "bias_squared",
            ):
                values = []
                for width in widths:
                    summary = computed[
                        (names_by_width[width], depths[-1])
                    ]
                    value = {
                        "variance": summary.variance,
                        "integrated_covariance": (
                            summary.integrated_covariance
                        ),
                        "bias_squared": (
                            summary.cross_replica_bias_squared
                        ),
                    }[metric]
                    result[f"width/{group}/{metric}/n{width}"] = value
                    values.append(value)
                corrections = [
                    abs(values[index + 1] - values[index])
                    for index in range(len(values) - 1)
                ]
                for index, value in enumerate(corrections):
                    result[
                        f"width/{group}/{metric}/correction{index}"
                    ] = value
                result[f"width/{group}/{metric}/ratio"] = min(
                    corrections[-1] / max(corrections[-2], 1e-300),
                    1e6,
                )
        return result

    all_indices = np.arange(outer_roots, dtype=int)
    point = compute(all_indices)
    half = replicas // 2
    pilot_seed, calibration_seed = np.random.SeedSequence(
        bootstrap_seed
    ).spawn(2)

    def draw_stream(
        rng: np.random.Generator, count: int
    ) -> Iterable[Mapping[str, float]]:
        for _draw in range(count):
            outer_indices = rng.integers(
                0, outer_roots, size=outer_roots
            )
            first = rng.integers(
                0, half, size=(outer_roots, half)
            )
            second = rng.integers(
                half, replicas, size=(outer_roots, half)
            )
            replica_indices = np.concatenate((first, second), axis=1)
            yield compute(outer_indices, replica_indices)

    band = _familywise_band_from_explicit_draws(
        point=point,
        pilot_draws=draw_stream(
            np.random.default_rng(pilot_seed),
            bootstrap_pilot_replicates,
        ),
        pilot_replicates=bootstrap_pilot_replicates,
        draws=draw_stream(
            np.random.default_rng(calibration_seed),
            bootstrap_replicates,
        ),
        replicates=bootstrap_replicates,
        confidence=confidence,
        mc_failure_probability=bootstrap_mc_failure_probability,
        seed=bootstrap_seed,
    )
    indices = np.arange(outer_roots)
    summaries: dict[str, HomogenizationFieldSummary] = {}
    for name, table in fields.items():
        by_depth = {
            depth: _summarize_homogenization_samples(
                table[depth], depth, indices
            )
            for depth in depths
        }
        bias_squared_key = f"{name}/bias_squared/L{depths[-1]}"
        bias_squared_upper = float(band.upper[bias_squared_key])
        summaries[name] = HomogenizationFieldSummary(
            by_depth=by_depth,
            variance_slope=float(band.point[f"{name}/variance_slope"]),
            integrated_covariance_slope=float(
                band.point[f"{name}/integrated_covariance_slope"]
            ),
            bias_squared_at_max_depth=float(
                band.point[bias_squared_key]
            ),
            bias_squared_upper_at_max_depth=bias_squared_upper,
            bias_norm_at_max_depth=by_depth[
                depths[-1]
            ].cross_replica_bias_norm,
            bias_norm_upper_at_max_depth=float(
                np.sqrt(max(bias_squared_upper, 0.0))
            ),
        )

    failures: list[str] = []
    unresolved: list[str] = []
    for name in model_free_fields:
        if name not in summaries:
            unresolved.append("HOMOGENIZATION_MODEL_FREE_FIELD_MISSING")
            continue
        key = f"{name}/variance_slope"
        lower = float(band.lower[key])
        upper = float(band.upper[key])
        if lower >= slope_upper_threshold:
            failures.append("HOMOGENIZATION_VARIANCE_NONDECAY")
        elif upper >= slope_upper_threshold:
            unresolved.append("HOMOGENIZATION_VARIANCE_SLOPE_UNRESOLVED")
    for name in candidate_fields:
        if name not in summaries:
            unresolved.append("HOMOGENIZATION_CANDIDATE_FIELD_MISSING")
            continue
        slope_key = f"{name}/integrated_covariance_slope"
        lower = float(band.lower[slope_key])
        upper = float(band.upper[slope_key])
        if lower >= slope_upper_threshold:
            failures.append("HOMOGENIZATION_COVARIANCE_NONDECAY")
        elif upper >= slope_upper_threshold:
            unresolved.append("HOMOGENIZATION_COVARIANCE_SLOPE_UNRESOLVED")
        bias_key = f"{name}/bias_squared/L{depths[-1]}"
        # Only the simultaneous signed-U upper bound is mapped through the
        # square root for the norm gate.
        bias_upper = float(np.sqrt(max(float(band.upper[bias_key]), 0.0)))
        if bias_upper > candidate_bias_allocation:
            failures.append("HOMOGENIZATION_CANDIDATE_BIAS_EXCEEDS_ALLOCATION")
    for group in (width_ladders or {}):
        for metric in (
            "variance",
            "integrated_covariance",
            "bias_squared",
        ):
            key = f"width/{group}/{metric}/ratio"
            if float(band.lower[key]) >= 1.0:
                unresolved.append(
                    "HOMOGENIZATION_WIDTH_RESOLUTION_NONCONTRACTING"
                )
            elif float(band.upper[key]) >= 1.0:
                unresolved.append(
                    "HOMOGENIZATION_WIDTH_CONTRACTION_UNRESOLVED"
                )
    if not conditional_mean_tested:
        unresolved.append("HOMOGENIZATION_CONDITIONAL_MEAN_NOT_TESTED")
    if failures:
        gate = GateVerdict(
            GateStatus.FAIL, tuple(sorted(set(failures)))
        )
    elif unresolved:
        gate = GateVerdict(
            GateStatus.UNRESOLVED, tuple(sorted(set(unresolved)))
        )
    else:
        gate = GateVerdict(
            GateStatus.PASS,
            ("HOMOGENIZATION_VARIANCE_BIAS_COVARIANCE_PASS",),
        )
    return HomogenizationSummary(summaries, band, gate)


@dataclass(frozen=True)
class GeneratorResidualSeries:
    times: Array
    back: Array
    outgoing: Array
    observable: Array
    shadow: Array

    def __post_init__(self) -> None:
        times = _strict_grid(self.times, "generator times")
        arrays = {}
        for name in ("back", "outgoing", "observable"):
            value = np.asarray(getattr(self, name), dtype=float)
            if value.ndim == 1:
                value = value[None, :]
            if value.ndim != 2 or value.shape[1] != times.size:
                raise ValueError(
                    f"{name} must have shape (root,time) or (time,)"
                )
            if np.any(value < 0.0) or not np.all(np.isfinite(value)):
                raise ValueError(f"{name} residual must be finite/nonnegative")
            arrays[name] = value
        shadow = np.asarray(self.shadow, dtype=float)
        if shadow.ndim == 1:
            shadow = shadow[:, None]
        if shadow.ndim != 2 or shadow.shape[0] != arrays["back"].shape[0]:
            raise ValueError("shadow must have shape (root,horizon)")
        if np.any(shadow < 0.0) or not np.all(np.isfinite(shadow)):
            raise ValueError("shadow errors must be finite/nonnegative")
        if any(
            value.shape[0] != arrays["back"].shape[0]
            for value in arrays.values()
        ):
            raise ValueError("generator root counts differ")
        object.__setattr__(self, "times", times)
        object.__setattr__(self, "back", arrays["back"])
        object.__setattr__(self, "outgoing", arrays["outgoing"])
        object.__setattr__(self, "observable", arrays["observable"])
        object.__setattr__(self, "shadow", shadow)


@dataclass(frozen=True)
class GeneratorPairSummary:
    back_integral: float
    outgoing_integral: float
    observable_integral: float
    shadow_max: float


@dataclass(frozen=True)
class GeneratorResidualSummary:
    pairs: Mapping[tuple[int, int], GeneratorPairSummary]
    contraction_ratios: Mapping[str, tuple[float, ...]]
    familywise_band: FamilywiseBootstrapBand
    gate: GateVerdict


def analyze_generator_residuals(
    series: Mapping[tuple[int, int], GeneratorResidualSeries],
    *,
    numerical_upper_bounds: Mapping[tuple[tuple[int, int], str], float],
    numerics_allocation: float,
    bootstrap_replicates: int,
    bootstrap_pilot_replicates: int,
    bootstrap_mc_failure_probability: float,
    bootstrap_seed: int,
    confidence: float = DEFAULT_STAGE_FAMILY_CONFIDENCE,
    require_p70_extension: bool = True,
) -> GeneratorResidualSummary:
    if len(series) < 2:
        raise ValueError("at least two generator pairs are required")
    ordered_pairs = tuple(sorted(series))
    levels = tuple(
        sorted({level for pair in ordered_pairs for level in pair})
    )
    contraction_pairs = tuple(
        (levels[index], levels[index + 1])
        for index in range(len(levels) - 1)
        if (levels[index], levels[index + 1]) in series
    )
    if len(contraction_pairs) < 2:
        raise ValueError(
            "generator series need at least two consecutive level pairs"
        )
    root_count = series[ordered_pairs[0]].back.shape[0]
    for pair, value in series.items():
        if value.back.shape[0] != root_count:
            raise ValueError(f"generator root count differs for {pair}")

    def compute(indices: Array) -> Mapping[str, float]:
        result: dict[str, float] = {}
        for pair in ordered_pairs:
            record = series[pair]
            prefix = f"P{pair[0]}_P{pair[1]}"
            for metric in ("back", "outgoing", "observable"):
                mean_path = np.mean(getattr(record, metric)[indices], axis=0)
                integral = float(np.trapezoid(mean_path, record.times))
                key = f"{metric}_integral/{prefix}"
                result[key] = integral
            shadow = float(np.max(np.mean(record.shadow[indices], axis=0)))
            result[f"shadow_max/{prefix}"] = shadow
        for metric in (
            "back_integral",
            "outgoing_integral",
            "observable_integral",
            "shadow_max",
        ):
            metric_values = []
            for pair in contraction_pairs:
                prefix = f"P{pair[0]}_P{pair[1]}"
                metric_values.append(result[f"{metric}/{prefix}"])
            for index in range(len(metric_values) - 1):
                denominator = metric_values[index]
                ratio = (
                    metric_values[index + 1] / denominator
                    if denominator > 0.0
                    else np.inf
                )
                result[f"ratio/{metric}/{index}"] = min(ratio, 1e6)
        return result

    band = whole_root_familywise_bootstrap(
        root_count=root_count,
        statistic=compute,
        replicates=bootstrap_replicates,
        pilot_replicates=bootstrap_pilot_replicates,
        seed=bootstrap_seed,
        confidence=confidence,
        mc_failure_probability=bootstrap_mc_failure_probability,
    )
    pair_summaries: dict[tuple[int, int], GeneratorPairSummary] = {}
    for pair in ordered_pairs:
        prefix = f"P{pair[0]}_P{pair[1]}"
        pair_summaries[pair] = GeneratorPairSummary(
            back_integral=float(band.point[f"back_integral/{prefix}"]),
            outgoing_integral=float(
                band.point[f"outgoing_integral/{prefix}"]
            ),
            observable_integral=float(
                band.point[f"observable_integral/{prefix}"]
            ),
            shadow_max=float(band.point[f"shadow_max/{prefix}"]),
        )
    contraction: dict[str, tuple[float, ...]] = {}
    for metric in (
        "back_integral",
        "outgoing_integral",
        "observable_integral",
        "shadow_max",
    ):
        contraction[metric] = tuple(
            float(band.point[f"ratio/{metric}/{index}"])
            for index in range(len(contraction_pairs) - 1)
        )

    failures: list[str] = []
    unresolved: list[str] = []
    gated_metrics = (
        "back_integral",
        "outgoing_integral",
        "observable_integral",
        "shadow_max",
    )
    for metric in gated_metrics:
        for index in range(len(contraction_pairs) - 1):
            key = f"ratio/{metric}/{index}"
            if float(band.lower[key]) >= 1.0:
                failures.append("GENERATOR_RESIDUAL_NONCONTRACTING")
            elif float(band.upper[key]) >= 1.0:
                unresolved.append("GENERATOR_CONTRACTION_UNRESOLVED")
    for pair in ordered_pairs:
        for metric in ("back", "outgoing", "observable", "shadow"):
            key = (pair, metric)
            if key not in numerical_upper_bounds:
                unresolved.append("GENERATOR_NUMERICAL_BOUND_MISSING")
            elif numerical_upper_bounds[key] > numerics_allocation:
                unresolved.append("GENERATOR_NUMERICALLY_UNRESOLVED")
    if require_p70_extension and contraction_pairs[-1][1] < 70:
        unresolved.append("GENERATOR_P70_EXTENSION_REQUIRED")
    if failures:
        gate = GateVerdict(
            GateStatus.FAIL, tuple(sorted(set(failures)))
        )
    elif unresolved:
        gate = GateVerdict(
            GateStatus.UNRESOLVED, tuple(sorted(set(unresolved)))
        )
    else:
        gate = GateVerdict(
            GateStatus.PASS,
            ("GENERATOR_RESIDUALS_CONTRACT_THROUGH_P70",),
        )
    return GeneratorResidualSummary(
        pair_summaries, contraction, band, gate
    )


@dataclass(frozen=True)
class AttackCell:
    gaps: Array
    max_constraint_defect: float = 0.0

    def __post_init__(self) -> None:
        gaps = np.asarray(self.gaps, dtype=float)
        if gaps.ndim != 1 or gaps.size < 2:
            raise ValueError("attack gaps need at least two roots")
        if np.any(gaps < 0.0) or not np.all(np.isfinite(gaps)):
            raise ValueError("attack gaps must be finite/nonnegative")
        if (
            not np.isfinite(self.max_constraint_defect)
            or self.max_constraint_defect < 0.0
        ):
            raise ValueError("constraint defect must be finite/nonnegative")
        object.__setattr__(self, "gaps", gaps)


@dataclass(frozen=True)
class AttackScalingSummary:
    mean_gaps: Mapping[tuple[int, int, float], float]
    width_slopes: Mapping[tuple[int, float], float]
    depth_slopes: Mapping[tuple[int, float], float]
    amplitude_slopes: Mapping[tuple[int, int], float]
    familywise_band: FamilywiseBootstrapBand
    gate: GateVerdict


def analyze_attack_scaling(
    cells: Mapping[tuple[int, int, float], AttackCell],
    *,
    attack_kind: str,
    allocation: float,
    constraint_tolerance: float,
    bootstrap_replicates: int,
    bootstrap_pilot_replicates: int,
    bootstrap_mc_failure_probability: float,
    bootstrap_seed: int,
    confidence: float = DEFAULT_STAGE_FAMILY_CONFIDENCE,
) -> AttackScalingSummary:
    if attack_kind not in {"independent", "coherent"}:
        raise ValueError("attack_kind must be independent or coherent")
    if not cells:
        raise ValueError("attack cells are empty")
    widths = tuple(sorted({key[0] for key in cells}))
    depths = tuple(sorted({key[1] for key in cells}))
    amplitudes = tuple(sorted({float(key[2]) for key in cells}))
    expected = {
        (width, depth, amplitude)
        for width in widths
        for depth in depths
        for amplitude in amplitudes
    }
    if set(cells) != expected:
        raise ValueError("attack grid must be rectangular")
    root_count = next(iter(cells.values())).gaps.size
    if any(cell.gaps.size != root_count for cell in cells.values()):
        raise ValueError("attack cells must share whole-root count")

    def compute(indices: Array) -> Mapping[str, float]:
        means = {
            key: float(np.mean(cell.gaps[indices]))
            for key, cell in cells.items()
        }
        result: dict[str, float] = {}
        for (width, depth, amplitude), value in means.items():
            result[f"gap/n{width}/L{depth}/a{amplitude:g}"] = value
        for depth in depths:
            for amplitude in amplitudes:
                values = [
                    max(means[(width, depth, amplitude)], 1e-300)
                    for width in widths
                ]
                result[f"width_slope/L{depth}/a{amplitude:g}"] = _log_slope(
                    widths, values
                )
        for width in widths:
            for amplitude in amplitudes:
                values = [
                    max(means[(width, depth, amplitude)], 1e-300)
                    for depth in depths
                ]
                result[f"depth_slope/n{width}/a{amplitude:g}"] = _log_slope(
                    depths, values
                )
        for width in widths:
            for depth in depths:
                values = [
                    max(means[(width, depth, amplitude)], 1e-300)
                    for amplitude in amplitudes
                ]
                result[f"amplitude_slope/n{width}/L{depth}"] = _log_slope(
                    amplitudes, values
                )
        return result

    band = whole_root_familywise_bootstrap(
        root_count=root_count,
        statistic=compute,
        replicates=bootstrap_replicates,
        pilot_replicates=bootstrap_pilot_replicates,
        seed=bootstrap_seed,
        confidence=confidence,
        mc_failure_probability=bootstrap_mc_failure_probability,
    )
    mean_gaps = {
        key: float(
            band.point[
                f"gap/n{key[0]}/L{key[1]}/a{float(key[2]):g}"
            ]
        )
        for key in cells
    }
    width_slopes = {
        (depth, amplitude): float(
            band.point[f"width_slope/L{depth}/a{amplitude:g}"]
        )
        for depth in depths
        for amplitude in amplitudes
    }
    depth_slopes = {
        (width, amplitude): float(
            band.point[f"depth_slope/n{width}/a{amplitude:g}"]
        )
        for width in widths
        for amplitude in amplitudes
    }
    amplitude_slopes = {
        (width, depth): float(
            band.point[f"amplitude_slope/n{width}/L{depth}"]
        )
        for width in widths
        for depth in depths
    }
    if attack_kind == "coherent":
        gate = GateVerdict(
            GateStatus.UNRESOLVED,
            ("ATTACK_COHERENT_DIAGNOSTIC_ONLY",),
        )
        return AttackScalingSummary(
            mean_gaps,
            width_slopes,
            depth_slopes,
            amplitude_slopes,
            band,
            gate,
        )
    failures: list[str] = []
    unresolved: list[str] = []
    if any(
        cell.max_constraint_defect > constraint_tolerance
        for cell in cells.values()
    ):
        failures.append("ATTACK_PRESENT_STATE_CONSTRAINT_FAILED")
    for width, depth, amplitude in cells:
        key = f"gap/n{width}/L{depth}/a{amplitude:g}"
        if float(band.lower[key]) > allocation:
            failures.append("ATTACK_GAP_EXCEEDS_ALLOCATION")
        elif float(band.upper[key]) > allocation:
            unresolved.append("ATTACK_GAP_BOUND_UNRESOLVED")
    for depth in depths:
        for amplitude in amplitudes:
            key = f"width_slope/L{depth}/a{amplitude:g}"
            if float(band.lower[key]) >= 0.0:
                failures.append("ATTACK_WIDTH_TREND_NONCONTRACTING")
            elif float(band.upper[key]) >= 0.0:
                unresolved.append("ATTACK_WIDTH_TREND_UNRESOLVED")
    for width in widths:
        for amplitude in amplitudes:
            key = f"depth_slope/n{width}/a{amplitude:g}"
            if float(band.lower[key]) >= 0.0:
                failures.append("ATTACK_DEPTH_TREND_NONCONTRACTING")
            elif float(band.upper[key]) >= 0.0:
                unresolved.append("ATTACK_DEPTH_TREND_UNRESOLVED")
    if failures:
        gate = GateVerdict(
            GateStatus.FAIL, tuple(sorted(set(failures)))
        )
    elif unresolved:
        gate = GateVerdict(
            GateStatus.UNRESOLVED, tuple(sorted(set(unresolved)))
        )
    else:
        gate = GateVerdict(
            GateStatus.PASS,
            ("ATTACK_INDEPENDENT_GAPS_CONTRACT_AND_STAY_SMALL",),
        )
    return AttackScalingSummary(
        mean_gaps,
        width_slopes,
        depth_slopes,
        amplitude_slopes,
        band,
        gate,
    )


@dataclass(frozen=True)
class ErrorLedgerSummary:
    bounds: Mapping[str, float]
    allocations: Mapping[str, float]
    total_bound: float
    target_total: float
    margins: Mapping[str, float]
    conditional_components: tuple[str, ...]
    gate: GateVerdict


def aggregate_error_ledger(
    bounds: Mapping[str, float],
    *,
    allocations: Mapping[str, float],
    target_total: float,
    conditional_validity: Mapping[str, bool] | None = None,
    nuisance_discrepancy_lcb: float | None = None,
    nuisance_components: Sequence[str] = (),
    nuisance_fraction: float = 0.2,
) -> ErrorLedgerSummary:
    missing = set(allocations) - set(bounds)
    if missing:
        return ErrorLedgerSummary(
            bounds=dict(bounds),
            allocations=dict(allocations),
            total_bound=float("nan"),
            target_total=target_total,
            margins={},
            conditional_components=tuple(),
            gate=GateVerdict(
                GateStatus.UNRESOLVED,
                ("LEDGER_COMPONENT_MISSING",),
                {"missing": sorted(missing)},
            ),
        )
    normalized = {key: float(bounds[key]) for key in allocations}
    if any(not np.isfinite(value) or value < 0.0 for value in normalized.values()):
        return ErrorLedgerSummary(
            normalized,
            dict(allocations),
            float("nan"),
            target_total,
            {},
            tuple(),
            GateVerdict(
                GateStatus.FAIL, ("LEDGER_COMPONENT_INVALID",)
            ),
        )
    margins = {
        key: float(allocations[key]) - normalized[key] for key in allocations
    }
    total = float(sum(normalized.values()))
    failures: list[str] = []
    unresolved: list[str] = []
    if any(margin < 0.0 for margin in margins.values()):
        failures.append("LEDGER_ALLOCATION_EXCEEDED")
    if total > target_total:
        failures.append("LEDGER_TOTAL_EXCEEDED")
    if nuisance_components:
        if nuisance_discrepancy_lcb is None:
            unresolved.append("LEDGER_NUISANCE_LCB_MISSING")
        else:
            for name in nuisance_components:
                if (
                    name in normalized
                    and normalized[name]
                    >= nuisance_fraction * nuisance_discrepancy_lcb
                ):
                    failures.append("LEDGER_NUISANCE_NOT_SEPARATED")
    conditional_validity = dict(conditional_validity or {})
    conditional_components = tuple(sorted(conditional_validity))
    if any(not valid for valid in conditional_validity.values()):
        unresolved.append("LEDGER_CONDITIONAL_TAIL_UNJUSTIFIED")
    if failures:
        gate = GateVerdict(
            GateStatus.FAIL, tuple(sorted(set(failures)))
        )
    elif unresolved:
        gate = GateVerdict(
            GateStatus.UNRESOLVED, tuple(sorted(set(unresolved)))
        )
    else:
        gate = GateVerdict(
            GateStatus.PASS,
            ("LEDGER_ALL_COMPONENTS_WITHIN_ALLOCATION",),
        )
    return ErrorLedgerSummary(
        normalized,
        dict(allocations),
        total,
        target_total,
        margins,
        conditional_components,
        gate,
    )


__all__ = [
    "AlignmentGrid",
    "ArchiveValidationError",
    "AttackCell",
    "AttackScalingSummary",
    "ErrorLedgerSummary",
    "FamilywiseBootstrapBand",
    "FullCurveDistance",
    "GateStatus",
    "GateVerdict",
    "GeneratorPairSummary",
    "GeneratorResidualSeries",
    "GeneratorResidualSummary",
    "HomogenizationDepthSummary",
    "HomogenizationFieldSummary",
    "HomogenizationSummary",
    "InnovationSamples",
    "NumericalCauchySummary",
    "ObservableCurve",
    "ObservableEnsemble",
    "OrderedScalingSummary",
    "StageArchive",
    "aggregate_error_ledger",
    "align_curve",
    "align_ensemble",
    "analyze_attack_scaling",
    "analyze_generator_residuals",
    "analyze_homogenization",
    "analyze_numerical_cauchy",
    "analyze_ordered_scaling",
    "build_sealed_archive",
    "derive_homogenization_outer_seed",
    "ensemble_mean",
    "finalize_runner_stage_archive",
    "full_curve_distance",
    "hash_array",
    "homogenization_expected_array_shapes",
    "homogenization_summary_names",
    "load_sealed_stage_archive",
    "validate_homogenization_archive_schema",
    "validate_sealed_stage_archive",
    "whole_root_familywise_bootstrap",
]
