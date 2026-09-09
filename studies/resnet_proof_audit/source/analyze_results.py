#!/usr/bin/env python3
"""Deterministic, fail-closed analysis driver for the PDE obligation study.

This module reads scientific archives; it never imports or runs a scientific
vector field.  Every admitted ``.npz`` is already byte-sealed by
``run_study.py`` (or the structural runner), bound to the preregistered
protocol and frozen source tree, and finite.  Missing scientific jobs produce
an explicit ``UNRESOLVED`` gate.  Malformed, duplicate, partial, or unknown
archives abort analysis.

The statistical unit is always a complete Gaussian root (or a complete
quadrature scramble).  The confidence level, bootstrap count, seed,
normalizations, thresholds, and allocations are read verbatim from the
frozen protocol.  There is no command-line threshold override.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import sys
import tempfile
from typing import Any, Callable, Iterable, Mapping, Sequence

import numpy as np
import scipy


HERE = Path(__file__).resolve().parent
AUDIT_ROOT = HERE.parent
WORKSPACE_ROOT = AUDIT_ROOT.parent
PROTOCOL_PATH = AUDIT_ROOT / "protocol" / "preregistered_protocol.json"
FROZEN_INPUTS_PATH = AUDIT_ROOT / "results" / "seals" / "FROZEN_INPUTS.json"
RESULTS_ROOT = AUDIT_ROOT / "results"
PROCESSED_ROOT = RESULTS_ROOT / "processed"

if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from analyze_study import (  # noqa: E402
    _familywise_band_from_explicit_draws,
    AlignmentGrid,
    ArchiveValidationError,
    GateStatus,
    GateVerdict,
    GeneratorResidualSeries,
    InnovationSamples,
    ObservableCurve,
    ObservableEnsemble,
    aggregate_error_ledger,
    align_curve,
    analyze_generator_residuals,
    analyze_homogenization,
    derive_homogenization_outer_seed,
    hash_array,
    homogenization_summary_names,
    load_sealed_stage_archive,
    validate_homogenization_archive_schema,
    whole_root_familywise_bootstrap,
)


Array = np.ndarray


class AnalysisError(RuntimeError):
    """Raised when the evidence inventory cannot be analyzed safely."""


@dataclass(frozen=True)
class LoadedEvidence:
    path: Path
    stage: str
    archive: Any
    file_sha256: str


@dataclass(frozen=True)
class ScalarBand:
    point: Mapping[str, float]
    lower: Mapping[str, float]
    upper: Mapping[str, float]
    critical_lower: float
    critical_upper: float
    pilot_replicates: int
    critical_replicates: int
    critical_order_index: int
    critical_order_assurance: float
    mc_failure_probability: float


@dataclass(frozen=True)
class AnalysisContext:
    audit_root: Path
    workspace_root: Path
    protocol_path: Path
    frozen_inputs_path: Path
    results_root: Path
    processed_root: Path
    protocol: Mapping[str, Any]
    frozen_inputs: Mapping[str, Any]
    protocol_sha256: str
    frozen_inputs_sha256: str
    frozen_hashes: frozenset[str]
    evidence: tuple[LoadedEvidence, ...]


_CANONICAL_STAGES = {
    "numerics": "numerics",
    "scaling": "scaling",
    "homogenization": "homogenization",
    "attack": "attack",
    "generator": "generator",
    "gain": "amplification",
    "tail_pde": "tail_pde",
    "tail_dense": "tail_dense",
}
_BASE_SOURCE_LABELS = {
    "canonical_pde": (
        "activation_linearity_smoking_gun/source/src/"
        "dense_pde/operator_galerkin.py"
    ),
    "canonical_dense": (
        "activation_linearity_smoking_gun/source/src/"
        "dense_reference/core.py"
    ),
    "canonical_activations": (
        "activation_linearity_smoking_gun/source/src/activations.py"
    ),
    "cross_p": "source/cross_p.py",
    "dense_gates": "source/dense_gates.py",
    "runner": "source/run_study.py",
}
_STRUCTURAL_SOURCE_LABELS = {
    "structural_runner": "source/structural_runner.py",
    "pde_tangent": "source/pde_tangent.py",
}
_RUN_STUDY_STAGES = {"numerics", "scaling", "homogenization", "attack"}
_STRUCTURAL_STAGES = {"generator", "gain", "tail_pde", "tail_dense"}


def _jsonable(value: Any) -> Any:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, (GateStatus,)):
        return value.value
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(item) for item in value]
    if hasattr(value, "to_dict"):
        return _jsonable(value.to_dict())
    return value


def _canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        _jsonable(value),
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
        ensure_ascii=True,
    ).encode("utf-8")


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _resolve_frozen_path(
    audit_root: Path, workspace_root: Path, label: str
) -> Path:
    local = audit_root / label
    if local.is_file():
        return local
    external = workspace_root / label
    if external.is_file():
        return external
    raise AnalysisError(f"frozen source is missing: {label}")


def _load_json(path: Path) -> Mapping[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise AnalysisError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, Mapping):
        raise AnalysisError(f"JSON root must be an object: {path}")
    return value


def _live_environment() -> dict[str, str]:
    return {
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
    }


def _expected_source_hashes(
    raw_stage: str,
    frozen_by_label: Mapping[str, str],
) -> dict[str, str]:
    if raw_stage in _RUN_STUDY_STAGES:
        labels = dict(_BASE_SOURCE_LABELS)
    elif raw_stage in _STRUCTURAL_STAGES:
        labels = {**_BASE_SOURCE_LABELS, **_STRUCTURAL_SOURCE_LABELS}
    else:
        raise AnalysisError(
            f"unrecognized scientific stage {raw_stage!r}"
        )
    missing = [
        label for label in labels.values() if label not in frozen_by_label
    ]
    if missing:
        raise AnalysisError(
            "frozen inventory lacks a required runtime source: "
            + ", ".join(missing)
        )
    return {
        key: frozen_by_label[label] for key, label in labels.items()
    }


def discover_evidence(
    *,
    audit_root: Path = AUDIT_ROOT,
    verify_current_frozen_sources: bool = True,
) -> AnalysisContext:
    """Discover and validate every scientific archive below ``results``."""

    audit_root = Path(audit_root).resolve()
    workspace_root = audit_root.parent
    protocol_path = audit_root / "protocol" / "preregistered_protocol.json"
    frozen_path = audit_root / "results" / "seals" / "FROZEN_INPUTS.json"
    results_root = audit_root / "results"
    processed_root = results_root / "processed"
    if not protocol_path.is_file():
        raise AnalysisError(f"missing protocol: {protocol_path}")
    if not frozen_path.is_file():
        raise AnalysisError(f"missing frozen-input seal: {frozen_path}")

    protocol = _load_json(protocol_path)
    frozen = _load_json(frozen_path)
    protocol_hash = _sha256_file(protocol_path)
    freeze_hash = _sha256_file(frozen_path)
    if frozen.get("schema_version") != 1:
        raise AnalysisError("unsupported frozen-input schema")
    if frozen.get("protocol_sha256") != protocol_hash:
        raise AnalysisError("current protocol does not match frozen protocol hash")
    files = frozen.get("files")
    if not isinstance(files, list) or not files:
        raise AnalysisError("frozen-input manifest has no file inventory")
    frozen_hashes: set[str] = set()
    frozen_by_label: dict[str, str] = {}
    for item in files:
        if not isinstance(item, Mapping):
            raise AnalysisError("malformed frozen-input file entry")
        label = item.get("path")
        expected = item.get("sha256")
        if not isinstance(label, str) or not isinstance(expected, str):
            raise AnalysisError("malformed frozen-input file path/hash")
        if label in frozen_by_label:
            raise AnalysisError(
                f"duplicate frozen-input file label: {label}"
            )
        frozen_by_label[label] = expected
        frozen_hashes.add(expected)
        if verify_current_frozen_sources:
            path = _resolve_frozen_path(audit_root, workspace_root, label)
            if _sha256_file(path) != expected:
                raise AnalysisError(f"frozen source hash mismatch: {label}")
    frozen_environment = frozen.get("environment")
    if (
        not isinstance(frozen_environment, Mapping)
        or set(frozen_environment)
        != {"python", "platform", "numpy", "scipy"}
        or not all(
            isinstance(value, str)
            for value in frozen_environment.values()
        )
    ):
        raise AnalysisError("frozen-input environment is malformed")
    frozen_environment = dict(frozen_environment)
    if verify_current_frozen_sources and frozen_environment != _live_environment():
        raise AnalysisError(
            "live analysis environment differs from the frozen environment"
        )

    partials = sorted(results_root.rglob("*.partial")) if results_root.exists() else []
    if partials:
        labels = ", ".join(str(path.relative_to(audit_root)) for path in partials)
        raise AnalysisError(f"partial scientific/processed files present: {labels}")

    loaded: list[LoadedEvidence] = []
    identities: dict[tuple[str, str], Path] = {}
    for path in sorted(results_root.rglob("*.npz")) if results_root.exists() else []:
        try:
            archive = load_sealed_stage_archive(
                path,
                required_config_keys=(),
                required_arrays=(),
                expected_protocol_sha256=protocol_hash,
            )
        except ArchiveValidationError as exc:
            raise AnalysisError(f"invalid sealed archive {path}: {exc}") from exc
        raw_stage = str(archive.metadata["stage"])
        if raw_stage not in _CANONICAL_STAGES:
            raise AnalysisError(
                f"unrecognized scientific stage {raw_stage!r}: {path}"
            )
        stage = _CANONICAL_STAGES[raw_stage]
        if archive.metadata.get("frozen_inputs_sha256") != freeze_hash:
            raise AnalysisError(f"archive has wrong frozen-input binding: {path}")
        expected_sources = _expected_source_hashes(
            raw_stage, frozen_by_label
        )
        source_hashes = archive.metadata.get("source_hashes")
        if not isinstance(source_hashes, Mapping) or dict(
            source_hashes
        ) != expected_sources:
            raise AnalysisError(
                f"archive source map is not exactly the frozen stage map: "
                f"{path}"
            )
        if archive.metadata.get("environment") != frozen_environment:
            raise AnalysisError(
                f"archive environment differs from the freeze: {path}"
            )
        for key, expected in {
            "python_version": frozen_environment["python"],
            "platform": frozen_environment["platform"],
            "numpy_version": frozen_environment["numpy"],
            "scipy_version": frozen_environment["scipy"],
        }.items():
            if archive.metadata.get(key) != expected:
                raise AnalysisError(
                    f"archive {key} differs from the freeze: {path}"
                )
        identity = (stage, str(archive.metadata["config_sha256"]))
        if identity in identities:
            raise AnalysisError(
                "duplicate scientific configuration: "
                f"{identities[identity]} and {path}"
            )
        identities[identity] = path
        loaded.append(
            LoadedEvidence(
                path=path,
                stage=stage,
                archive=archive,
                file_sha256=_sha256_file(path),
            )
        )
    return AnalysisContext(
        audit_root=audit_root,
        workspace_root=workspace_root,
        protocol_path=protocol_path,
        frozen_inputs_path=frozen_path,
        results_root=results_root,
        processed_root=processed_root,
        protocol=protocol,
        frozen_inputs=frozen,
        protocol_sha256=protocol_hash,
        frozen_inputs_sha256=freeze_hash,
        frozen_hashes=frozenset(frozen_hashes),
        evidence=tuple(loaded),
    )


def _stage_evidence(
    context: AnalysisContext, stage: str
) -> tuple[LoadedEvidence, ...]:
    return tuple(item for item in context.evidence if item.stage == stage)


def _gate(
    status: GateStatus,
    *reasons: str,
    metrics: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    return GateVerdict(
        status,
        tuple(sorted(set(reasons))),
        dict(metrics or {}),
    ).to_dict()


def _unresolved_missing(stage: str) -> Mapping[str, Any]:
    return {
        "gate": _gate(
            GateStatus.UNRESOLVED,
            f"{stage.upper()}_EVIDENCE_MISSING",
        ),
        "metrics": {},
        "missing": ["all preregistered jobs"],
    }


def _as_float(value: Any, name: str) -> float:
    result = float(value)
    if not np.isfinite(result):
        raise AnalysisError(f"nonfinite configuration value: {name}")
    return result


def _canonical_model_config(
    protocol: Mapping[str, Any],
) -> dict[str, Any]:
    model = protocol["scope"]["canonical_model"]
    return {
        "X": np.asarray(model["X"], dtype=float).tolist(),
        "y": np.asarray(model["y"], dtype=float).tolist(),
        "activation": str(model["activation"]),
        "sigma_w": float(model["sigma_w"]),
        "A": float(model["A"]),
        "gamma": float(model["gamma"]),
    }


def _require_exact_config(
    item: LoadedEvidence,
    expected: Mapping[str, Any],
    *,
    label: str,
) -> None:
    actual = item.archive.config
    if _canonical_json_bytes(actual) != _canonical_json_bytes(expected):
        raise AnalysisError(
            f"{label} config is not exactly preregistered: {item.path}"
        )


def _derive_stage_seed(
    protocol: Mapping[str, Any],
    stage_code: int,
    *coordinates: int,
) -> int:
    entropy = [
        int(protocol["error_ledger"]["bootstrap_seed"]),
        int(stage_code),
        *(int(value) for value in coordinates),
    ]
    return int(
        np.random.SeedSequence(entropy).generate_state(
            1, dtype=np.uint64
        )[0]
    )


def _scaling_memory_estimate(
    *,
    n_grid: Sequence[int],
    L_grid: Sequence[int],
    input_dimension: int,
    sample_count: int,
    horizon: float,
    sample_dt: float,
) -> int:
    n_max = max(map(int, n_grid))
    L_max = max(map(int, L_grid))
    float_bytes = np.dtype(np.float64).itemsize
    parameter_elements = (
        L_max * n_max * n_max
        + n_max * int(input_dimension)
        + n_max
    )
    master_bytes = parameter_elements * float_bytes
    parameter_bytes = parameter_elements * float_bytes
    field_elements = (
        2 * (L_max + 1) * n_max * int(sample_count)
        + 3 * L_max * n_max * int(sample_count)
    )
    field_workspace_bytes = 8 * field_elements * float_bytes
    time_count = int(np.ceil(float(horizon) / float(sample_dt))) + 1
    jobs = len(tuple(n_grid)) * len(tuple(L_grid))
    observable_elements = jobs * time_count * (
        int(sample_count)
        + (L_max + 1) * int(sample_count) ** 2
        + 1
    )
    observable_bytes = 2 * observable_elements * float_bytes
    return int(
        master_bytes
        + 10 * parameter_bytes
        + field_workspace_bytes
        + observable_bytes
        + 1024**3
    )


def _expected_scaling_config(
    protocol: Mapping[str, Any],
    *,
    tier: str,
    root_index: int,
) -> dict[str, Any]:
    stage = protocol["stage_1_ordered_target"]
    declared = stage[f"{tier}_grid"]
    n_grid = [int(value) for value in declared["n"]]
    L_grid = [int(value) for value in declared["L"]]
    horizon = float(stage["active_horizon"])
    sample_dt = float(protocol["norms"]["time_sampling"])
    model = _canonical_model_config(protocol)
    return {
        "tier": tier,
        "n_grid": n_grid,
        "L_grid": L_grid,
        "root_index": int(root_index),
        "root_seed": _derive_stage_seed(
            protocol,
            101,
            0 if tier == "screen" else 1,
            int(root_index),
        ),
        "T": horizon,
        "dt": float(stage["dt"]),
        "sample_dt": sample_dt,
        "common_depth_nodes": max(L_grid) + 1,
        "memory_preflight_estimated_peak_bytes": _scaling_memory_estimate(
            n_grid=n_grid,
            L_grid=L_grid,
            input_dimension=len(model["X"]),
            sample_count=len(model["y"]),
            horizon=horizon,
            sample_dt=sample_dt,
        ),
        "canonical_model": model,
    }


def _expected_attack_config(
    protocol: Mapping[str, Any],
    *,
    n: int,
    depth: int,
    root_index: int,
) -> dict[str, Any]:
    stage = protocol["stage_3_same_state_attack"]
    basis_ladder = [int(value) for value in stage["basis_ladder"]]
    restart_horizons = [
        float(value) for value in stage["restart_horizons"]
    ]
    layers = [
        max(0, depth // 4 - 1),
        max(0, depth // 2 - 1),
        max(0, 3 * depth // 4 - 1),
    ]
    return {
        "n": int(n),
        "L": int(depth),
        "root_index": int(root_index),
        "root_seed": _derive_stage_seed(
            protocol, 303, int(root_index)
        ),
        "master_width": max(int(value) for value in stage["widths"]),
        "master_depth": max(int(value) for value in stage["depths"]),
        "checkpoint": float(stage["checkpoint"]),
        "layers": layers,
        "basis_ladder": basis_ladder,
        "primary_basis_size": int(stage["primary_basis_size"]),
        "amplitudes": [float(value) for value in stage["amplitudes"]],
        "restart_horizons": restart_horizons,
        "maximum_restart_horizon": max(restart_horizons),
        "constraint_tolerance_relative": float(
            stage["constraint_tolerance_relative"]
        ),
        "dt": float(protocol["stage_1_ordered_target"]["dt"]),
        "canonical_model": _canonical_model_config(protocol),
    }


def _resolution_coordinates(
    resolution: Mapping[str, Any],
    *,
    axis: str,
    seed: int,
) -> dict[str, Any]:
    primary = resolution["primary"]
    if axis == "primary":
        if int(seed) not in tuple(
            int(value) for value in primary["scramble_seeds"]
        ):
            raise AnalysisError("structural primary seed is undeclared")
        candidate = primary
    else:
        matches = [
            item
            for item in resolution[
                "one_axis_refinements_at_seed_20260723"
            ]
            if str(item["axis"]) == axis and int(item["seed"]) == int(seed)
        ]
        if len(matches) != 1:
            raise AnalysisError(
                "structural refinement axis/seed is undeclared"
            )
        candidate = matches[0]
    return {
        "base_order": int(candidate["base_order"]),
        "N": int(candidate["N"]),
        "R": int(candidate["R"]),
        "dt": float(candidate["dt"]),
        "seed": int(seed),
    }


def _expected_resolution_config(
    protocol: Mapping[str, Any],
    resolution: Mapping[str, Any],
    *,
    axis: str,
    seed: int,
    family: str,
) -> dict[str, Any]:
    coordinates = _resolution_coordinates(
        resolution, axis=axis, seed=seed
    )
    latent_dimension = len(
        protocol["scope"]["canonical_model"]["X"]
    ) + 1
    return {
        **coordinates,
        "M": int(coordinates["base_order"]) ** latent_dimension,
        "resolution_axis": axis,
        "resolution_is_primary": axis == "primary",
        "resolution_family": family,
    }


def _tail_boundaries(
    protocol: Mapping[str, Any],
) -> tuple[tuple[float, float], ...]:
    ends = tuple(
        float(value)
        for value in protocol["stage_6_all_time_tail"][
            "horizon_ladder"
        ]
    )
    return tuple(zip((0.0,) + ends[:-1], ends))


def _expected_tail_pde_config(
    protocol: Mapping[str, Any],
    *,
    seed: int,
    block_start: float,
    block_end: float,
    restart_seal_sha256: str | None,
) -> dict[str, Any]:
    ladder = protocol["stage_0_integrity_and_numerics"]["nested_ladder"]
    return {
        "N": int(ladder["primary_N"]),
        "R": int(ladder["primary_R"]),
        "dt": float(ladder["primary_dt"]),
        "base_order": int(ladder["primary_base_order"]),
        "M": int(ladder["primary_M"]),
        "P": 5,
        "seed": int(seed),
        "block_start": float(block_start),
        "block_end": float(block_end),
        "sample_dt": float(protocol["norms"]["time_sampling"]),
        "finite_horizon_only": True,
        "restart_seal_sha256": restart_seal_sha256,
        "canonical_model": _canonical_model_config(protocol),
    }


def _expected_tail_dense_config(
    protocol: Mapping[str, Any],
    *,
    root_index: int,
) -> dict[str, Any]:
    stage = protocol["stage_6_all_time_tail"]["dense_diagnostic"]
    return {
        "n": int(stage["n"]),
        "L": int(stage["L"]),
        "root_index": int(root_index),
        "root_seed": _derive_stage_seed(
            protocol, 607, int(root_index)
        ),
        "T": float(stage["maximum_horizon"]),
        "dt": float(protocol["stage_1_ordered_target"]["dt"]),
        "sample_dt": float(protocol["norms"]["time_sampling"]),
        "finite_horizon_only": True,
        "canonical_model": _canonical_model_config(protocol),
    }


def _validate_tail_pde_archive(
    protocol: Mapping[str, Any],
    item: LoadedEvidence,
    *,
    seed: int,
    block_start: float,
    block_end: float,
    restart_seal_sha256: str | None,
) -> None:
    _require_exact_config(
        item,
        _expected_tail_pde_config(
            protocol,
            seed=seed,
            block_start=block_start,
            block_end=block_end,
            restart_seal_sha256=restart_seal_sha256,
        ),
        label="PDE-tail",
    )
    arrays = item.archive.arrays
    if "endpoint_time" not in arrays:
        raise AnalysisError(
            f"PDE-tail endpoint time is missing: {item.path}"
        )
    endpoint_time = np.asarray(arrays["endpoint_time"])
    if (
        endpoint_time.shape != ()
        or endpoint_time.dtype != np.dtype(np.float64)
        or endpoint_time.item() != block_end
    ):
        raise AnalysisError(
            f"PDE-tail endpoint time mismatch: {item.path}"
        )
    times = np.asarray(arrays.get("times"))
    if (
        times.ndim != 1
        or times.dtype != np.dtype(np.float64)
        or times.size == 0
        or times[0] != block_start
        or times[-1] != block_end
    ):
        raise AnalysisError(
            f"PDE-tail sampled endpoints mismatch: {item.path}"
        )


def _metric_distance(
    f_left: Array,
    g_left: Array,
    f_right: Array,
    g_right: Array,
    *,
    s_f: float,
    s_g: float,
) -> float:
    f_left = np.asarray(f_left, dtype=float)
    g_left = np.asarray(g_left, dtype=float)
    f_right = np.asarray(f_right, dtype=float)
    g_right = np.asarray(g_right, dtype=float)
    if f_left.shape != f_right.shape or g_left.shape != g_right.shape:
        raise AnalysisError("aligned observable shapes differ")
    output = float(np.max(np.linalg.norm(f_left - f_right, axis=-1))) / s_f
    gram = float(
        np.max(np.linalg.norm(g_left - g_right, axis=(-2, -1)))
    ) / s_g
    return max(output, gram)


def _curve_to_grid(
    curve: ObservableCurve,
    *,
    times: Array,
    depths: Array,
) -> ObservableCurve:
    return align_curve(curve, AlignmentGrid(times, depths))


def _curve_from_numerics(item: LoadedEvidence) -> ObservableCurve:
    arrays = item.archive.arrays
    required = ("times", "f", "grams")
    missing = [key for key in required if key not in arrays]
    if missing:
        raise AnalysisError(f"numerics archive missing arrays {missing}: {item.path}")
    gram = np.asarray(arrays["grams"], dtype=float)
    if gram.ndim != 4:
        raise AnalysisError(f"numerics grams have wrong rank: {item.path}")
    return ObservableCurve(
        np.asarray(arrays["times"], dtype=float),
        np.linspace(0.0, 1.0, gram.shape[1]),
        np.asarray(arrays["f"], dtype=float),
        gram,
    )


def _scalarize_band(band: Any) -> ScalarBand:
    def scalars(table: Mapping[str, Array]) -> dict[str, float]:
        result: dict[str, float] = {}
        for key, value in table.items():
            array = np.asarray(value, dtype=float)
            if array.shape != ():
                raise AnalysisError(f"expected scalar bootstrap statistic: {key}")
            result[key] = float(array)
        return result

    return ScalarBand(
        point=scalars(band.point),
        lower=scalars(band.lower),
        upper=scalars(band.upper),
        critical_lower=float(band.critical_lower),
        critical_upper=float(band.critical_upper),
        pilot_replicates=int(band.pilot_replicates),
        critical_replicates=int(band.critical_replicates),
        critical_order_index=int(band.critical_order_index),
        critical_order_assurance=float(band.critical_order_assurance),
        mc_failure_probability=float(band.mc_failure_probability),
    )


def _bootstrap_calibration_metadata(band: Any) -> Mapping[str, Any]:
    return {
        "pilot_replicates": int(band.pilot_replicates),
        "calibration_replicates": int(band.critical_replicates),
        "critical_order_index_zero_based": int(
            band.critical_order_index
        ),
        "critical_order_assurance": float(
            band.critical_order_assurance
        ),
        "mc_failure_probability": float(band.mc_failure_probability),
        "two_sided_statistic": "absolute_max_standardized_deviation",
    }


def _grouped_familywise_bootstrap(
    *,
    root_counts: Mapping[str, int],
    statistic: Callable[[Mapping[str, Array]], Mapping[str, float]],
    replicates: int,
    pilot_replicates: int,
    seed: int,
    confidence: float,
    mc_failure_probability: float,
) -> ScalarBand:
    """One max-standardized family over independently resampled root groups.

    This is used only when the frozen protocol declares different root counts
    inside one stochastic family (the P5 standard and nested quadrature
    ladders).  Every draw resamples complete roots within each group and the
    maximum is then taken over the union of all declared statistics.
    """

    if not root_counts or any(count < 2 for count in root_counts.values()):
        raise AnalysisError("each bootstrap group needs at least two roots")
    all_indices = {
        name: np.arange(count, dtype=int) for name, count in root_counts.items()
    }
    point = {key: float(value) for key, value in statistic(all_indices).items()}
    if not point or any(not np.isfinite(value) for value in point.values()):
        raise AnalysisError("grouped bootstrap point statistic is invalid")
    pilot_seed, calibration_seed = np.random.SeedSequence(seed).spawn(2)

    def draw_stream(
        rng: np.random.Generator, count: int
    ) -> Iterable[Mapping[str, float]]:
        for _draw in range(count):
            indices = {
                name: rng.integers(0, root_count, size=root_count)
                for name, root_count in root_counts.items()
            }
            current = {
                key: float(value)
                for key, value in statistic(indices).items()
            }
            if set(current) != set(point):
                raise AnalysisError("bootstrap statistic inventory changed")
            if any(not np.isfinite(value) for value in current.values()):
                raise AnalysisError("nonfinite grouped bootstrap statistic")
            yield current

    return _scalarize_band(
        _familywise_band_from_explicit_draws(
            point=point,
            pilot_draws=draw_stream(
                np.random.default_rng(pilot_seed), pilot_replicates
            ),
            pilot_replicates=pilot_replicates,
            draws=draw_stream(
                np.random.default_rng(calibration_seed), replicates
            ),
            replicates=replicates,
            confidence=confidence,
            mc_failure_probability=mc_failure_probability,
            seed=seed,
        )
    )


def _analysis_constants(
    context: AnalysisContext,
    *,
    sequential_look: bool = False,
    look_count: int | None = None,
) -> tuple[int, int, int, float, float]:
    ledger = context.protocol["error_ledger"]
    replicates = int(ledger["bootstrap_replicates"])
    pilot_replicates = int(ledger["bootstrap_pilot_replicates"])
    seed = int(ledger["bootstrap_seed"])
    mc_failure_probability = float(
        ledger["bootstrap_mc_failure_probability_per_call"]
    )
    if look_count is None:
        look_count = 2 if sequential_look else 1
    if look_count not in (1, 2, 3):
        raise AnalysisError("unsupported frozen look count")
    confidence_key = {
        1: "stage_family_confidence",
        2: "two_look_family_confidence",
        3: "three_look_family_confidence",
    }[look_count]
    confidence = float(ledger[confidence_key])
    if replicates != 20000 or pilot_replicates != 5000:
        raise AnalysisError(
            "protocol bootstrap pilot/calibration counts differ from freeze"
        )
    expected = {
        1: 0.993,
        2: 0.9965,
        3: 0.9976666666666667,
    }[look_count]
    if not np.isclose(confidence, expected):
        raise AnalysisError(
            f"{confidence_key} differs from the frozen seven-family allocation"
        )
    if not np.isclose(mc_failure_probability, 0.001 / 13.0):
        raise AnalysisError("bootstrap MC failure allocation differs from freeze")
    return (
        replicates,
        pilot_replicates,
        seed,
        confidence,
        mc_failure_probability,
    )


def _sparse_refinement_upper_bound(
    *,
    one_seed_axis_upper: float,
    primary_scramble_radius_upper: float,
    primary_sampling_upper: float,
) -> float:
    """Conservative bound for a refinement evaluated at only one scramble."""

    values = (
        float(one_seed_axis_upper),
        float(primary_scramble_radius_upper),
        float(primary_sampling_upper),
    )
    if any(not np.isfinite(value) or value < 0.0 for value in values):
        raise ValueError("sparse-refinement bounds must be finite/nonnegative")
    return values[0] + 2.0 * values[1] + values[2]


def _stage0_numerical_radius(
    *,
    primary_mean_shift_upper: float,
    primary_to_joint_upper: float,
    cofinal_remainder_upper: float | None,
) -> tuple[float, float | None]:
    """Return diagnostic and certified PDE numerical radii.

    The first primary-to-joint correction is observable, but it is not a
    bound on the uncomputed remainder beyond the joint corner.  Without a
    separately certified remainder, only the diagnostic radius is returned.
    """

    values = (
        float(primary_mean_shift_upper),
        float(primary_to_joint_upper),
    )
    if any(not np.isfinite(value) or value < 0.0 for value in values):
        raise ValueError("Stage-0 numerical radii must be finite/nonnegative")
    diagnostic = float(sum(values))
    if cofinal_remainder_upper is None:
        return diagnostic, None
    remainder = float(cofinal_remainder_upper)
    if not np.isfinite(remainder) or remainder < 0.0:
        raise ValueError("cofinal numerical remainder must be nonnegative")
    return diagnostic, diagnostic + remainder


def _empirical_axis_sum_upper_bound(
    by_axis: Mapping[str, float],
) -> float:
    """Sum one-axis sensitivities without claiming an interaction bound.

    A maximum over one-axis corrections is not a cofinal numerical-error
    bound.  Summing the nonnegative corrections is a conservative empirical
    sensitivity envelope, but it still cannot certify interactions that were
    never evaluated at a joint refinement corner.
    """

    if not by_axis:
        raise ValueError("at least one axis bound is required")
    values = tuple(float(value) for value in by_axis.values())
    if any(not np.isfinite(value) or value < 0.0 for value in values):
        raise ValueError("axis bounds must be finite/nonnegative")
    return float(sum(values))


def _has_cofinal_joint_corner_certificate(
    resolution: Mapping[str, Any],
) -> bool:
    """Whether the exact required structural inventory declares a joint job."""

    candidates = resolution.get(
        "one_axis_refinements_at_seed_20260723", ()
    )
    joint_count = sum(
        isinstance(candidate, Mapping)
        and str(candidate.get("axis")) == "joint"
        for candidate in candidates
    )
    return (
        resolution.get("cofinal_joint_corner_certificate") is True
        and joint_count == 1
    )


def _combine_structural_nuisance_upper_bound(
    by_axis: Mapping[str, float],
) -> tuple[float, str]:
    """Use a direct joint correction when present, otherwise an axis sum."""

    if "joint" in by_axis:
        value = float(by_axis["joint"])
        if not np.isfinite(value) or value < 0.0:
            raise ValueError("joint-corner bound must be finite/nonnegative")
        return value, "direct_primary_to_joint_corner"
    return (
        _empirical_axis_sum_upper_bound(by_axis),
        "conservative_empirical_axis_sum",
    )


def analyze_stage0_numerics(
    context: AnalysisContext,
) -> tuple[Mapping[str, Any], list[Mapping[str, Any]]]:
    items = _stage_evidence(context, "numerics")
    if not items:
        return _unresolved_missing("numerics"), []
    protocol = context.protocol
    stage = protocol["stage_0_integrity_and_numerics"]
    s_f = float(protocol["norms"]["S_f"])
    s_g = float(protocol["norms"]["S_G"])
    allocation = float(
        protocol["error_ledger"]["preallocated_components"]["PDE_numerics"]
    )
    (
        replicates,
        pilot_replicates,
        seed,
        confidence,
        mc_failure_probability,
    ) = _analysis_constants(
        context, look_count=3
    )
    common_times = np.arange(
        0.0,
        float(stage["active_horizon"]) + 1e-12,
        float(protocol["norms"]["time_sampling"]),
    )
    common_times[-1] = float(stage["active_horizon"])
    common_depths = np.linspace(0.0, 1.0, 17)

    records: dict[
        tuple[int, int, int, int, float, int], ObservableCurve
    ] = {}
    for item in items:
        config = item.archive.metadata["config"]
        try:
            key = (
                int(config["P"]),
                int(config["base_order"]),
                int(config["N"]),
                int(config["R"]),
                _as_float(config["dt"], "dt"),
                int(config["seed"]),
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise AnalysisError(
                f"malformed numerics configuration: {item.path}"
            ) from exc
        if key in records:
            raise AnalysisError(f"duplicate numerics configuration: {key}")
        records[key] = _curve_to_grid(
            _curve_from_numerics(item),
            times=common_times,
            depths=common_depths,
        )

    execution = stage.get("execution_inventory")
    if not isinstance(execution, Mapping):
        raise AnalysisError("Stage 0 has no exact execution inventory")
    active_levels = tuple(int(value) for value in execution["active_levels"])
    phase_a_configs = execution["phase_A_primary_configs_per_level"]
    phase_b_configs = execution[
        "phase_B_conditional_upward_configs_per_level"
    ]
    downward_configs = execution[
        "seed0_downward_diagnostic_configs_per_level"
    ]
    p70_configs = execution["conditional_P70_configs"]

    def coordinate(config: Mapping[str, Any]) -> tuple[int, int, int, float, int]:
        return (
            int(config["base_order"]),
            int(config["N"]),
            int(config["R"]),
            float(config["dt"]),
            int(config["seed"]),
        )

    phase_b_axis = {
        (
            int(template["base_order"]),
            int(template["N"]),
            int(template["R"]),
            float(template["dt"]),
        ): str(template["axis"])
        for template in execution["phase_B_upward_templates"]
    }
    downward_axis = {
        coordinate(template): str(template["axis"])
        for template in execution["seed0_downward_diagnostic_templates"]
    }
    p70_resolution = stage["P70_conditional_extension"][
        "numerical_resolution"
    ]
    p70_primary = p70_resolution["primary"]
    p70_axis = {
        coordinate(candidate): str(candidate["axis"])
        for candidate in p70_resolution[
            "one_axis_refinements_at_seed_20260723"
        ]
    }
    admitted: dict[tuple[int, str, int], ObservableCurve] = {}
    for key, curve in records.items():
        P, base_order, N, R, dt, seed_value = key
        config_tuple = (base_order, N, R, dt, seed_value)
        item = next(
            evidence
            for evidence in items
            if int(evidence.archive.config["P"]) == P
            and coordinate(evidence.archive.config) == config_tuple
        )
        config = item.archive.config
        if P in active_levels:
            if config_tuple in {coordinate(value) for value in phase_a_configs}:
                phase, axis = "phase_A_primary", "primary"
            elif config_tuple in {coordinate(value) for value in phase_b_configs}:
                phase = "phase_B_conditional"
                axis = phase_b_axis[(base_order, N, R, dt)]
            elif config_tuple in {coordinate(value) for value in downward_configs}:
                phase = "downward_diagnostic"
                axis = downward_axis[config_tuple]
            else:
                raise AnalysisError(
                    f"undeclared active numerics configuration: {item.path}"
                )
        elif P == 70:
            if config_tuple not in {coordinate(value) for value in p70_configs}:
                raise AnalysisError(
                    f"undeclared P70 numerics configuration: {item.path}"
                )
            phase = "conditional_P70"
            primary_key = (
                int(p70_primary["base_order"]),
                int(p70_primary["N"]),
                int(p70_primary["R"]),
                float(p70_primary["dt"]),
                seed_value,
            )
            axis = (
                "primary"
                if config_tuple == primary_key
                else p70_axis[config_tuple]
            )
        else:
            raise AnalysisError(f"undeclared numerics level P={P}")
        latent_dimension = len(
            protocol["scope"]["canonical_model"]["X"]
        ) + 1
        _require_exact_config(
            item,
            {
                "P": P,
                "N": N,
                "R": R,
                "dt": dt,
                "seed": seed_value,
                "T": float(stage["active_horizon"]),
                "master_levels": [5, 15, 35, 70],
                "base_order": base_order,
                "M": base_order**latent_dimension,
                "conditional_p70_authorized": P == 70,
                "phase_b_authorized": (
                    phase == "phase_B_conditional"
                ),
                "execution_phase": phase,
                "numerical_axis": axis,
                "canonical_model": _canonical_model_config(protocol),
            },
            label="numerics",
        )
        if (
            str(config.get("execution_phase")) != phase
            or str(config.get("numerical_axis")) != axis
        ):
            raise AnalysisError(
                f"numerics phase/axis metadata mismatch: {item.path}"
            )
        admitted_key = (P, axis, seed_value)
        if admitted_key in admitted:
            raise AnalysisError(
                f"duplicate numerics phase/axis configuration: {admitted_key}"
            )
        admitted[admitted_key] = curve

    phase_a_seeds = tuple(int(value["seed"]) for value in phase_a_configs)
    expected_a = {
        (P, "primary", seed_value)
        for P in active_levels
        for seed_value in phase_a_seeds
    }
    missing_a = sorted(expected_a - set(admitted))
    if missing_a:
        return (
            {
                "gate": _gate(
                    GateStatus.UNRESOLVED,
                    "NUMERICS_PHASE_A_INCOMPLETE",
                ),
                "metrics": {},
                "missing": [str(value) for value in missing_a],
            },
            [],
        )

    primary_roots = {
        P: (
            np.stack(
                [admitted[(P, "primary", value)].f for value in phase_a_seeds]
            ),
            np.stack(
                [
                    admitted[(P, "primary", value)].gram
                    for value in phase_a_seeds
                ]
            ),
        )
        for P in active_levels
    }
    primary_centers = {
        P: (
            np.mean(primary_roots[P][0], axis=0),
            np.mean(primary_roots[P][1], axis=0),
        )
        for P in active_levels
    }

    def phase_a_statistic(indices: Array) -> Mapping[str, float]:
        means = {
            P: (
                np.mean(primary_roots[P][0][indices], axis=0),
                np.mean(primary_roots[P][1][indices], axis=0),
            )
            for P in active_levels
        }
        result: dict[str, float] = {}
        for P in active_levels:
            dispersion = _loo_curve_dispersion(
                primary_roots[P][0],
                primary_roots[P][1],
                indices,
                s_f=s_f,
                s_g=s_g,
            )
            result[f"dispersion/P{P}"] = dispersion["rms"]
            result[f"descriptive_mean_se/P{P}"] = dispersion["mean_se"]
            result[f"mean_shift/P{P}"] = _resampled_mean_curve_shift(
                primary_roots[P][0],
                primary_roots[P][1],
                indices,
                full_center=primary_centers[P],
                s_f=s_f,
                s_g=s_g,
            )
        for low, high in zip(active_levels[:-1], active_levels[1:]):
            result[f"adjacent/P{low}_P{high}"] = (
                _curve_distance_from_arrays(
                    means[low], means[high], s_f=s_f, s_g=s_g
                )
            )
        return result

    phase_a_band = _scalarize_band(
        whole_root_familywise_bootstrap(
            root_count=len(phase_a_seeds),
            statistic=phase_a_statistic,
            replicates=replicates,
            pilot_replicates=pilot_replicates,
            seed=seed,
            confidence=confidence,
            mc_failure_probability=mc_failure_probability,
        )
    )
    adjacent_lowers = {
        f"P{low}_P{high}": max(
            0.0, phase_a_band.lower[f"adjacent/P{low}_P{high}"]
        )
        for low, high in zip(active_levels[:-1], active_levels[1:])
    }
    adjacent_uppers = {
        f"P{low}_P{high}": max(
            0.0, phase_a_band.upper[f"adjacent/P{low}_P{high}"]
        )
        for low, high in zip(active_levels[:-1], active_levels[1:])
    }
    minimum_adjacent_lower = min(adjacent_lowers.values())
    minimum_adjacent_upper = min(adjacent_uppers.values())
    dispersion_upper = {
        P: max(0.0, phase_a_band.upper[f"dispersion/P{P}"])
        for P in active_levels
    }
    dispersion_lower = {
        P: max(0.0, phase_a_band.lower[f"dispersion/P{P}"])
        for P in active_levels
    }
    mean_shift_upper = {
        P: max(0.0, phase_a_band.upper[f"mean_shift/P{P}"])
        for P in active_levels
    }
    phase_a_unlocked = (
        minimum_adjacent_lower > 0.0
        and all(value < allocation for value in dispersion_upper.values())
        and all(
            value < 0.2 * minimum_adjacent_lower
            for value in dispersion_upper.values()
        )
    )
    phase_a_fail = (
        any(value > allocation for value in dispersion_lower.values())
        or (
            minimum_adjacent_upper > 0.0
            and any(
                value >= 0.2 * minimum_adjacent_upper
                for value in dispersion_lower.values()
            )
        )
    )
    phase_b_present = any(
        key[0] in active_levels
        and key[1] in set(phase_b_axis.values())
        for key in admitted
    )
    phase_a_metrics = {
        "confidence": confidence,
        "critical_lower": phase_a_band.critical_lower,
        "critical_upper": phase_a_band.critical_upper,
        "bootstrap_calibration": _bootstrap_calibration_metadata(
            phase_a_band
        ),
        "inference_scope": {
            "root_count": len(phase_a_seeds),
            "finite_sample_coverage_claimed": False,
            "ledger_admissible": False,
            "semantics": "four-scramble diagnostic bootstrap",
        },
        "dispersion_lower": dispersion_lower,
        "dispersion_upper": dispersion_upper,
        "primary_mean_shift_upper": mean_shift_upper,
        "adjacent_lower": adjacent_lowers,
        "adjacent_upper": adjacent_uppers,
        "unlocked": phase_a_unlocked,
    }
    if not phase_a_unlocked:
        reasons = [
            (
                "NUMERICS_PHASE_A_DISPERSION_CLEAR_FAILURE"
                if phase_a_fail
                else "NUMERICS_PHASE_A_UNLOCK_UNRESOLVED"
            )
        ]
        if phase_b_present:
            reasons.append(
                "NUMERICS_PHASE_B_PRESENT_WITHOUT_PHASE_A_UNLOCK"
            )
        return (
            {
                "gate": _gate(
                    GateStatus.FAIL if phase_a_fail else GateStatus.UNRESOLVED,
                    *reasons,
                    metrics={"allocation": allocation},
                ),
                "phase_A_gate": _gate(
                    GateStatus.FAIL if phase_a_fail else GateStatus.UNRESOLVED,
                    *reasons,
                ),
                "metrics": {"phase_A": phase_a_metrics},
                "missing": [],
                "conditional_stop": True,
            },
            [],
        )

    axes = tuple(str(value["axis"]) for value in execution["phase_B_upward_templates"])
    expected_b = {
        (P, axis, seed_value)
        for P in active_levels
        for axis in axes
        for seed_value in phase_a_seeds
    }
    missing_b = sorted(expected_b - set(admitted))
    if missing_b:
        return (
            {
                "gate": _gate(
                    GateStatus.UNRESOLVED,
                    "NUMERICS_PHASE_B_TRIGGERED_INCOMPLETE",
                ),
                "phase_A_gate": _gate(
                    GateStatus.PASS, "NUMERICS_PHASE_A_UNLOCK_PASSES"
                ),
                "metrics": {"phase_A": phase_a_metrics},
                "missing": [str(value) for value in missing_b],
            },
            [],
        )

    paired_corrections = {
        (P, axis): np.asarray(
            [
                _curve_distance_from_arrays(
                    (
                        admitted[(P, "primary", seed_value)].f,
                        admitted[(P, "primary", seed_value)].gram,
                    ),
                    (
                        admitted[(P, axis, seed_value)].f,
                        admitted[(P, axis, seed_value)].gram,
                    ),
                    s_f=s_f,
                    s_g=s_g,
                )
                for seed_value in phase_a_seeds
            ]
        )
        for P in active_levels
        for axis in axes
    }

    def phase_b_statistic(indices: Array) -> Mapping[str, float]:
        return {
            f"paired_cauchy/P{P}/{axis}": float(
                np.mean(paired_corrections[(P, axis)][indices])
            )
            for P in active_levels
            for axis in axes
        }

    phase_b_band = _scalarize_band(
        whole_root_familywise_bootstrap(
            root_count=len(phase_a_seeds),
            statistic=phase_b_statistic,
            replicates=replicates,
            pilot_replicates=pilot_replicates,
            seed=seed + 1,
            confidence=confidence,
            mc_failure_probability=mc_failure_probability,
        )
    )
    rows: list[Mapping[str, Any]] = []
    per_p_upper: dict[int, float] = {}
    comparisons: dict[str, Any] = {}
    failures: list[str] = []
    unresolved: list[str] = []
    for P in active_levels:
        comparisons[f"P{P}"] = {}
        for axis in axes:
            key = f"paired_cauchy/P{P}/{axis}"
            lower = max(0.0, phase_b_band.lower[key])
            upper = max(0.0, phase_b_band.upper[key])
            comparisons[f"P{P}"][axis] = {
                "point": phase_b_band.point[key],
                "lower": lower,
                "upper": upper,
            }
            rows.append(
                {
                    "stage": "numerics",
                    "metric": f"P{P}/{axis}",
                    "point": phase_b_band.point[key],
                    "lower": lower,
                    "upper": upper,
                    "semantics": (
                        "paired same-scramble Phase-B correction distribution"
                    ),
                }
            )
        per_p_upper[P] = max(
            comparisons[f"P{P}"][axis]["upper"] for axis in axes
        )
        lower_max = max(
            comparisons[f"P{P}"][axis]["lower"] for axis in axes
        )
        if lower_max > allocation:
            failures.append("NUMERICS_PHASE_B_ALLOCATION_CLEAR_FAILURE")
        elif per_p_upper[P] > allocation:
            unresolved.append("NUMERICS_PHASE_B_ALLOCATION_UNRESOLVED")
        if minimum_adjacent_lower <= 0.0:
            unresolved.append(
                "NUMERICS_ADJACENT_P_DISCREPANCY_LCB_UNRESOLVED"
            )
        elif per_p_upper[P] >= 0.2 * minimum_adjacent_lower:
            unresolved.append(
                "NUMERICS_PHASE_B_NOT_SEPARATED_FROM_P_CHANGE"
            )

    downward_rows = []
    for P in active_levels:
        for axis in ("M_down", "R_down"):
            item = admitted.get((P, axis, phase_a_seeds[0]))
            if item is None:
                continue
            base = admitted[(P, "primary", phase_a_seeds[0])]
            value = _curve_distance_from_arrays(
                (base.f, base.gram),
                (item.f, item.gram),
                s_f=s_f,
                s_g=s_g,
            )
            downward_rows.append(
                {
                    "stage": "numerics",
                    "metric": f"P{P}/{axis}",
                    "point": value,
                    "lower": "",
                    "upper": "",
                    "semantics": "seed-zero downward diagnostic only",
                }
            )
    rows.extend(downward_rows)

    numerical_radius_pairs = {
        P: _stage0_numerical_radius(
            primary_mean_shift_upper=mean_shift_upper[P],
            primary_to_joint_upper=comparisons[f"P{P}"]["joint"]["upper"],
            cofinal_remainder_upper=None,
        )
        for P in active_levels
    }
    diagnostic_numerical_radius_by_p = {
        P: values[0] for P, values in numerical_radius_pairs.items()
    }
    certified_numerical_radius_by_p = {
        P: values[1] for P, values in numerical_radius_pairs.items()
    }
    for P, diagnostic_radius in diagnostic_numerical_radius_by_p.items():
        rows.append(
            {
                "stage": "numerics",
                "metric": f"P{P}/diagnostic_numerical_radius",
                "point": diagnostic_radius,
                "lower": 0.0,
                "upper": diagnostic_radius,
                "semantics": (
                    "primary-scramble mean-shift radius plus direct "
                    "primary-to-joint correction; diagnostic only because "
                    "no second cofinal remainder is available"
                ),
            }
        )

    if failures:
        status, reasons = GateStatus.FAIL, failures
    else:
        status, reasons = GateStatus.UNRESOLVED, [
            *unresolved,
            "NUMERICS_COFINAL_REMAINDER_CERTIFICATE_MISSING",
            "NUMERICS_FOUR_SCRAMBLE_BOOTSTRAP_DIAGNOSTIC_ONLY",
        ]

    p70_present = {key for key in admitted if key[0] == 70}
    p70_result: Mapping[str, Any] = {
        "status": "NOT_RUN",
        "alpha": "reserved and unused",
    }
    if p70_present:
        p70_seeds = tuple(
            int(value) for value in p70_primary["scramble_seeds"]
        )
        p70_axes = tuple(
            str(value["axis"])
            for value in p70_resolution[
                "one_axis_refinements_at_seed_20260723"
            ]
        )
        expected_p70 = {
            (70, "primary", seed_value) for seed_value in p70_seeds
        } | {
            (70, axis, p70_seeds[0]) for axis in p70_axes
        }
        missing_p70 = sorted(expected_p70 - p70_present)
        if missing_p70:
            status = GateStatus.UNRESOLVED
            reasons = [*reasons, "NUMERICS_P70_FAMILY_INCOMPLETE"]
            p70_result = {
                "status": "UNRESOLVED",
                "missing": [str(value) for value in missing_p70],
            }
        else:
            p70_roots = (
                np.stack(
                    [admitted[(70, "primary", value)].f for value in p70_seeds]
                ),
                np.stack(
                    [
                        admitted[(70, "primary", value)].gram
                        for value in p70_seeds
                    ]
                ),
            )
            p70_center = (
                np.mean(p70_roots[0], axis=0),
                np.mean(p70_roots[1], axis=0),
            )

            def p70_statistic(indices: Array) -> Mapping[str, float]:
                current_center = (
                    np.mean(p70_roots[0][indices], axis=0),
                    np.mean(p70_roots[1][indices], axis=0),
                )
                dispersion = _loo_curve_dispersion(
                    p70_roots[0],
                    p70_roots[1],
                    indices,
                    s_f=s_f,
                    s_g=s_g,
                )
                result = {
                    "dispersion": dispersion["rms"],
                    "descriptive_mean_se": dispersion["mean_se"],
                    "mean_shift": _curve_distance_from_arrays(
                        current_center,
                        p70_center,
                        s_f=s_f,
                        s_g=s_g,
                    ),
                }
                base = admitted[(70, "primary", p70_seeds[0])]
                for axis in p70_axes:
                    refined = admitted[(70, axis, p70_seeds[0])]
                    result[f"cauchy/{axis}"] = _curve_distance_from_arrays(
                        (base.f, base.gram),
                        (refined.f, refined.gram),
                        s_f=s_f,
                        s_g=s_g,
                    )
                return result

            p70_band = _scalarize_band(
                whole_root_familywise_bootstrap(
                    root_count=len(p70_seeds),
                    statistic=p70_statistic,
                    replicates=replicates,
                    pilot_replicates=pilot_replicates,
                    seed=seed + 2,
                    confidence=confidence,
                    mc_failure_probability=mc_failure_probability,
                )
            )
            p70_dispersion = max(0.0, p70_band.upper["dispersion"])
            p70_sampling = max(0.0, p70_band.upper["mean_shift"])
            p70_axis_bounds = {
                axis: _sparse_refinement_upper_bound(
                    one_seed_axis_upper=max(
                        0.0, p70_band.upper[f"cauchy/{axis}"]
                    ),
                    primary_scramble_radius_upper=p70_dispersion,
                    primary_sampling_upper=p70_sampling,
                )
                for axis in p70_axes
            }
            p70_upper, p70_combination_rule = (
                _combine_structural_nuisance_upper_bound(
                    p70_axis_bounds
                )
            )
            p70_joint_certified = (
                _has_cofinal_joint_corner_certificate(p70_resolution)
            )
            p70_result = {
                "status": (
                    "PASS"
                    if (
                        p70_upper <= allocation
                        and p70_joint_certified
                    )
                    else "UNRESOLVED"
                ),
                "combined_upper": p70_upper,
                "by_axis": p70_axis_bounds,
                "combination_rule": p70_combination_rule,
                "cofinal_joint_corner_certificate": (
                    p70_joint_certified
                ),
                "cross_P_comparison_performed": False,
                "bootstrap_calibration": _bootstrap_calibration_metadata(
                    p70_band
                ),
                "inference_scope": {
                    "root_count": len(p70_seeds),
                    "finite_sample_coverage_claimed": False,
                    "semantics": "four-scramble diagnostic bootstrap",
                },
            }
            if not p70_joint_certified:
                status = GateStatus.UNRESOLVED
                reasons = [
                    *reasons,
                    "NUMERICS_P70_NO_COFINAL_JOINT_CORNER",
                ]
            elif p70_upper > allocation:
                status = GateStatus.UNRESOLVED
                reasons = [
                    *reasons,
                    "NUMERICS_P70_RESOLUTION_UNRESOLVED",
                ]

    return (
        {
            "gate": _gate(status, *reasons, metrics={"allocation": allocation}),
            "phase_A_gate": _gate(
                GateStatus.PASS, "NUMERICS_PHASE_A_UNLOCK_PASSES"
            ),
            "metrics": {
                "phase_A": phase_a_metrics,
                "phase_B": {
                    "confidence": confidence,
                    "critical_lower": phase_b_band.critical_lower,
                    "critical_upper": phase_b_band.critical_upper,
                    "bootstrap_calibration": (
                        _bootstrap_calibration_metadata(phase_b_band)
                    ),
                    "comparisons": comparisons,
                    "combined_upper_by_P": per_p_upper,
                    "diagnostic_numerical_radius_by_P": (
                        diagnostic_numerical_radius_by_p
                    ),
                    "certified_numerical_radius_by_P": (
                        certified_numerical_radius_by_p
                    ),
                    "certified_remainder_available": False,
                },
                "conditional_P70": p70_result,
                "inference_scope": {
                    "root_count": len(phase_a_seeds),
                    "finite_sample_coverage_claimed": False,
                    "semantics": "four-scramble diagnostic bootstrap",
                },
            },
            "missing": [],
            "component_upper_bound": None,
            "diagnostic_component_upper_bound": max(
                diagnostic_numerical_radius_by_p.values()
            ),
            "diagnostic_component_upper_bound_by_P": (
                diagnostic_numerical_radius_by_p
            ),
        },
        rows,
    )


def _curve_distance_from_arrays(
    left: tuple[Array, Array],
    right: tuple[Array, Array],
    *,
    s_f: float,
    s_g: float,
) -> float:
    return _metric_distance(
        left[0], left[1], right[0], right[1], s_f=s_f, s_g=s_g
    )


def _resampled_mean_curve_shift(
    f_roots: Array,
    gram_roots: Array,
    indices: Array,
    *,
    full_center: tuple[Array, Array] | None = None,
    s_f: float,
    s_g: float,
) -> float:
    """Distance from a resampled mean curve to the full-root center."""

    f_values = np.asarray(f_roots, dtype=float)
    gram_values = np.asarray(gram_roots, dtype=float)
    selected = np.asarray(indices, dtype=int)
    if (
        f_values.shape[0] != gram_values.shape[0]
        or selected.ndim != 1
        or selected.size == 0
    ):
        raise AnalysisError("invalid root arrays for mean-shift bootstrap")
    center = (
        (
            np.mean(f_values, axis=0),
            np.mean(gram_values, axis=0),
        )
        if full_center is None
        else full_center
    )
    resampled = (
        np.mean(f_values[selected], axis=0),
        np.mean(gram_values[selected], axis=0),
    )
    return _curve_distance_from_arrays(
        resampled, center, s_f=s_f, s_g=s_g
    )


def _log_slope(x: Sequence[float], y: Sequence[float]) -> float:
    xx = np.log(np.asarray(x, dtype=float))
    yy = np.log(np.maximum(np.asarray(y, dtype=float), 1e-300))
    return float(np.polyfit(xx, yy, 1)[0])


def _geometric_tail_bound(
    *,
    correction_upper: float,
    ratio_upper: float,
) -> float | None:
    """Radius of a geometric remainder ball around the finest curve."""

    if (
        not np.isfinite(correction_upper)
        or not np.isfinite(ratio_upper)
        or correction_upper < 0.0
        or ratio_upper < 0.0
        or ratio_upper >= 1.0
    ):
        return None
    return float(correction_upper * ratio_upper / (1.0 - ratio_upper))


def _propagated_depth_bounds(
    *,
    center_points: Sequence[float],
    center_lowers: Sequence[float],
    center_uppers: Sequence[float],
    width_tail_radii: Sequence[float | None],
) -> tuple[
    tuple[Mapping[str, float] | None, ...],
    tuple[Mapping[str, float] | None, ...],
]:
    """Propagate width-limit balls into adjacent depth corrections.

    If ``C_i`` is the observed finest-width correction between depths i and
    i+1 and the two finest-width centers lie in balls of radii ``r_i`` and
    ``r_{i+1}`` around their width limits, then the true width-limit
    correction lies in

    ``[max(0, C_i^lower-r_i-r_{i+1}), C_i^upper+r_i+r_{i+1}]``.

    Successive correction-ratio bounds use interval division.  A zero lower
    denominator leaves the ratio unresolved instead of silently using the
    raw center ratio.
    """

    points = tuple(float(value) for value in center_points)
    lowers = tuple(float(value) for value in center_lowers)
    uppers = tuple(float(value) for value in center_uppers)
    radii = tuple(width_tail_radii)
    if not (len(points) == len(lowers) == len(uppers)):
        raise ValueError("depth correction point/band lengths disagree")
    if len(radii) != len(points) + 1:
        raise ValueError("one width-tail radius is required at every depth")
    corrections: list[Mapping[str, float] | None] = []
    for index, point in enumerate(points):
        left_radius = radii[index]
        right_radius = radii[index + 1]
        if left_radius is None or right_radius is None:
            corrections.append(None)
            continue
        radius_sum = float(left_radius) + float(right_radius)
        corrections.append(
            {
                "point": point,
                "lower": max(0.0, lowers[index] - radius_sum),
                "upper": max(0.0, uppers[index] + radius_sum),
                "width_radius_sum": radius_sum,
            }
        )
    ratios: list[Mapping[str, float] | None] = []
    for left, right in zip(corrections[:-1], corrections[1:]):
        if left is None or right is None or left["lower"] <= 0.0:
            ratios.append(None)
            continue
        ratios.append(
            {
                "point": right["point"] / max(left["point"], 1e-300),
                "lower": right["lower"] / max(left["upper"], 1e-300),
                "upper": right["upper"] / left["lower"],
            }
        )
    return tuple(corrections), tuple(ratios)


def _loo_curve_dispersion(
    f_roots: Array,
    gram_roots: Array,
    indices: Array,
    *,
    s_f: float,
    s_g: float,
) -> Mapping[str, float]:
    """LOO root distances and RMS/SE summaries for a resampled ensemble."""

    selected_f = np.asarray(f_roots, dtype=float)[indices]
    selected_g = np.asarray(gram_roots, dtype=float)[indices]
    count = selected_f.shape[0]
    if count < 2:
        raise ValueError("LOO dispersion requires at least two roots")
    sum_f = np.sum(selected_f, axis=0)
    sum_g = np.sum(selected_g, axis=0)
    distances = np.empty(count, dtype=float)
    for index in range(count):
        loo_center = (
            (sum_f - selected_f[index]) / (count - 1),
            (sum_g - selected_g[index]) / (count - 1),
        )
        distances[index] = _curve_distance_from_arrays(
            (selected_f[index], selected_g[index]),
            loo_center,
            s_f=s_f,
            s_g=s_g,
        )
    rms = float(np.sqrt(np.mean(distances * distances)))
    return {
        "rms": rms,
        "mean_se": rms / np.sqrt(count),
        "empirical_max": float(np.max(distances)),
        "empirical_q95": float(
            np.quantile(distances, 0.95, method="higher")
        ),
    }


def _scaling_root_archive(
    item: LoadedEvidence,
) -> tuple[int, tuple[int, ...], tuple[int, ...], dict[tuple[int, int], tuple[Array, Array]]]:
    config = item.archive.metadata["config"]
    arrays = item.archive.arrays
    required = (
        "times",
        "job_n",
        "job_L",
        "f",
        "gram_common_depth",
        "common_depth_s",
    )
    missing = [key for key in required if key not in arrays]
    if missing:
        raise AnalysisError(f"scaling archive missing {missing}: {item.path}")
    try:
        root = int(config["root_index"])
        widths = tuple(int(value) for value in config["n_grid"])
        depths = tuple(int(value) for value in config["L_grid"])
    except (KeyError, TypeError, ValueError) as exc:
        raise AnalysisError(f"malformed scaling config: {item.path}") from exc
    job_n = np.asarray(arrays["job_n"], dtype=int)
    job_L = np.asarray(arrays["job_L"], dtype=int)
    keys = tuple(zip(job_n.tolist(), job_L.tolist()))
    expected = {(n, depth) for n in widths for depth in depths}
    if len(keys) != len(set(keys)) or set(keys) != expected:
        raise AnalysisError(f"scaling archive grid does not match config: {item.path}")
    f = np.asarray(arrays["f"], dtype=float)
    gram = np.asarray(arrays["gram_common_depth"], dtype=float)
    if f.shape[0] != len(keys) or gram.shape[0] != len(keys):
        raise AnalysisError(f"scaling job axis mismatch: {item.path}")
    table = {key: (f[index], gram[index]) for index, key in enumerate(keys)}
    return root, widths, depths, table


def _stage1_sequential_action(
    *,
    screen_status: GateStatus,
    positive_present: bool,
    positive_complete: bool,
) -> str:
    if screen_status == GateStatus.FAIL:
        return (
            "STOP_FAILED_SCREEN_WITH_EXTRANEOUS_POSITIVE"
            if positive_present
            else "STOP_FAILED_SCREEN"
        )
    if not positive_complete:
        return "WAIT_FOR_TRIGGERED_POSITIVE"
    return "ANALYZE_POSITIVE"


def _combine_stage1_sequential_results(
    *,
    screen_result: Mapping[str, Any],
    positive_result: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Retain both Stage-1 look records while exposing the final look."""

    return {
        **positive_result,
        "screen_gate": screen_result["gate"],
        "sequential_looks": {
            "screen": screen_result,
            "positive": positive_result,
        },
        "sequential_alpha_spending": (
            "equal Stage-1 half-alpha screen and positive looks"
        ),
    }


def analyze_stage1_scaling(
    context: AnalysisContext,
    *,
    _tier_override: str | None = None,
) -> tuple[Mapping[str, Any], list[Mapping[str, Any]]]:
    items = _stage_evidence(context, "scaling")
    if not items:
        return _unresolved_missing("ordered_scaling"), []
    protocol = context.protocol
    stage = protocol["stage_1_ordered_target"]
    s_f = float(protocol["norms"]["S_f"])
    s_g = float(protocol["norms"]["S_G"])
    allocations = protocol["error_ledger"]["preallocated_components"]
    width_allocation = float(allocations["width_tail_conditional"])
    depth_allocation = float(allocations["depth_tail_conditional"])
    (
        replicates,
        pilot_replicates,
        seed,
        confidence,
        mc_failure_probability,
    ) = _analysis_constants(
        context, sequential_look=True
    )

    by_tier: dict[str, dict[int, dict[tuple[int, int], tuple[Array, Array]]]] = {
        "screen": {},
        "positive": {},
    }
    grids: dict[str, tuple[tuple[int, ...], tuple[int, ...]]] = {}
    for item in items:
        config = item.archive.metadata["config"]
        tier = str(config.get("tier", ""))
        if tier not in by_tier:
            raise AnalysisError(f"unknown scaling tier in {item.path}: {tier!r}")
        try:
            exact_root = int(config["root_index"])
        except (KeyError, TypeError, ValueError) as exc:
            raise AnalysisError(
                f"malformed scaling root index: {item.path}"
            ) from exc
        _require_exact_config(
            item,
            _expected_scaling_config(
                protocol,
                tier=tier,
                root_index=exact_root,
            ),
            label="scaling",
        )
        root, widths, depths, table = _scaling_root_archive(item)
        declared = stage[f"{tier}_grid"]
        if widths != tuple(declared["n"]) or depths != tuple(declared["L"]):
            raise AnalysisError(
                f"scaling archive uses a partial/noncanonical {tier} grid: {item.path}"
            )
        if tier in grids and grids[tier] != (widths, depths):
            raise AnalysisError(f"{tier} scaling grids disagree")
        grids[tier] = (widths, depths)
        expected_roots = int(stage[f"{tier}_grid"]["coupled_roots"])
        if not 0 <= root < expected_roots:
            raise AnalysisError(
                f"scaling root index is outside the {tier} inventory: {root}"
            )
        if root in by_tier[tier]:
            raise AnalysisError(f"duplicate scaling root {tier}/{root}")
        by_tier[tier][root] = table

    positive_expected = int(stage["positive_grid"]["coupled_roots"])
    screen_expected = int(stage["screen_grid"]["coupled_roots"])
    screen_complete = set(by_tier["screen"]) == set(range(screen_expected))
    positive_complete = set(by_tier["positive"]) == set(
        range(positive_expected)
    )
    if _tier_override is None:
        if not screen_complete:
            absent = sorted(
                set(range(screen_expected)) - set(by_tier["screen"])
            )
            return (
                {
                    "gate": _gate(
                        GateStatus.UNRESOLVED,
                        "ORDERED_SCALING_SCREEN_INCOMPLETE",
                    ),
                    "metrics": {},
                    "missing": [f"screen_root_indices={absent}"],
                },
                [],
            )
        screen_result, screen_rows = analyze_stage1_scaling(
            context, _tier_override="screen"
        )
        screen_status = GateStatus(screen_result["gate"]["status"])
        sequential_action = _stage1_sequential_action(
            screen_status=screen_status,
            positive_present=bool(by_tier["positive"]),
            positive_complete=positive_complete,
        )
        if sequential_action.startswith("STOP_FAILED_SCREEN"):
            if by_tier["positive"]:
                reasons = list(screen_result["gate"]["reason_codes"])
                reasons.append(
                    "ORDERED_POSITIVE_TIER_AFTER_FAILED_SCREEN_PROTOCOL_VIOLATION"
                )
                screen_result = {
                    **screen_result,
                    "gate": _gate(
                        GateStatus.FAIL,
                        *sorted(set(reasons)),
                        metrics={
                            **screen_result["gate"].get("metrics", {}),
                            "positive_archives_ignored": len(
                                by_tier["positive"]
                            ),
                        },
                    ),
                }
            return screen_result, screen_rows
        if sequential_action == "WAIT_FOR_TRIGGERED_POSITIVE":
            absent = sorted(
                set(range(positive_expected)) - set(by_tier["positive"])
            )
            return (
                {
                    **screen_result,
                    "gate": _gate(
                        GateStatus.UNRESOLVED,
                        *sorted(
                            set(
                                screen_result["gate"]["reason_codes"]
                                + [
                                    "ORDERED_POSITIVE_TIER_TRIGGERED_INCOMPLETE"
                                ]
                            )
                        ),
                        metrics=screen_result["gate"].get("metrics", {}),
                    ),
                    "missing": [f"positive_root_indices={absent}"],
                },
                screen_rows,
            )
        positive_result, positive_rows = analyze_stage1_scaling(
            context, _tier_override="positive"
        )
        return (
            _combine_stage1_sequential_results(
                screen_result=screen_result,
                positive_result=positive_result,
            ),
            screen_rows + positive_rows,
        )
    if _tier_override not in ("screen", "positive"):
        raise AnalysisError("invalid internal scaling tier override")
    tier = _tier_override
    expected_count = (
        screen_expected if tier == "screen" else positive_expected
    )
    if set(by_tier[tier]) != set(range(expected_count)):
        missing = []
        absent = sorted(set(range(expected_count)) - set(by_tier[tier]))
        missing.append(f"{tier}_root_indices={absent}")
        return (
            {
                "gate": _gate(
                    GateStatus.UNRESOLVED,
                    "ORDERED_SCALING_ROOT_INVENTORY_INCOMPLETE",
                ),
                "metrics": {},
                "missing": missing,
            },
            [],
        )
    roots = by_tier[tier]
    widths, depths = grids[tier]
    root_ids = tuple(sorted(roots))
    root_count = len(root_ids)
    stacked = {
        key: (
            np.stack([roots[root][key][0] for root in root_ids]),
            np.stack([roots[root][key][1] for root in root_ids]),
        )
        for key in roots[root_ids[0]]
    }
    full_centers = {
        key: (
            np.mean(value[0], axis=0),
            np.mean(value[1], axis=0),
        )
        for key, value in stacked.items()
    }
    finest_width = widths[-1]

    def statistic(indices: Array) -> Mapping[str, float]:
        means = {
            key: (
                np.mean(value[0][indices], axis=0),
                np.mean(value[1][indices], axis=0),
            )
            for key, value in stacked.items()
        }
        result: dict[str, float] = {}
        for depth in depths:
            dispersions: list[float] = []
            corrections: list[float] = []
            for width in widths:
                dispersion = _loo_curve_dispersion(
                    stacked[(width, depth)][0],
                    stacked[(width, depth)][1],
                    indices,
                    s_f=s_f,
                    s_g=s_g,
                )
                result[f"dispersion_rms/L{depth}/n{width}"] = dispersion[
                    "rms"
                ]
                result[f"descriptive_mean_se/L{depth}/n{width}"] = dispersion[
                    "mean_se"
                ]
                result[f"mean_shift/L{depth}/n{width}"] = (
                    _resampled_mean_curve_shift(
                        stacked[(width, depth)][0],
                        stacked[(width, depth)][1],
                        indices,
                        full_center=full_centers[(width, depth)],
                        s_f=s_f,
                        s_g=s_g,
                    )
                )
                result[f"descriptive_max/L{depth}/n{width}"] = dispersion[
                    "empirical_max"
                ]
                result[f"descriptive_q95/L{depth}/n{width}"] = dispersion[
                    "empirical_q95"
                ]
                dispersions.append(max(dispersion["rms"], 1e-300))
            result[f"dispersion_rms_slope/L{depth}"] = _log_slope(
                widths, dispersions
            )
            for index in range(len(widths) - 1):
                corrections.append(
                    _curve_distance_from_arrays(
                        means[(widths[index], depth)],
                        means[(widths[index + 1], depth)],
                        s_f=s_f,
                        s_g=s_g,
                    )
                )
                result[f"width_correction/L{depth}/{index}"] = corrections[-1]
            for index in range(len(corrections) - 1):
                ratio = corrections[index + 1] / max(corrections[index], 1e-300)
                result[f"width_ratio/L{depth}/{index}"] = min(ratio, 1e6)
        depth_corrections: list[float] = []
        for index in range(len(depths) - 1):
            depth_corrections.append(
                _curve_distance_from_arrays(
                    means[(finest_width, depths[index])],
                    means[(finest_width, depths[index + 1])],
                    s_f=s_f,
                    s_g=s_g,
                )
            )
            result[f"depth_correction/{index}"] = depth_corrections[-1]
        for index in range(len(depth_corrections) - 1):
            ratio = depth_corrections[index + 1] / max(
                depth_corrections[index], 1e-300
            )
            result[f"depth_ratio/{index}"] = min(ratio, 1e6)
        return result

    band = _scalarize_band(
        whole_root_familywise_bootstrap(
            root_count=root_count,
            statistic=statistic,
            replicates=replicates,
            pilot_replicates=pilot_replicates,
            seed=seed + 101,
            confidence=confidence,
            mc_failure_probability=mc_failure_probability,
        )
    )
    failures: list[str] = []
    unresolved: list[str] = []
    if len(widths) < 4:
        unresolved.append("ORDERED_INSUFFICIENT_WIDTH_LEVELS")
    if len(depths) < 4:
        unresolved.append("ORDERED_INSUFFICIENT_DEPTH_LEVELS")
    width_tails: dict[str, float | None] = {}
    rows: list[Mapping[str, Any]] = []
    for depth in depths:
        slope_key = f"dispersion_rms_slope/L{depth}"
        if band.lower[slope_key] >= -0.25:
            failures.append("ORDERED_RMS_DISPERSION_NONCONTRACTING")
        elif band.upper[slope_key] >= -0.25:
            unresolved.append("ORDERED_RMS_DISPERSION_SLOPE_UNRESOLVED")
        ratio_keys = [
            f"width_ratio/L{depth}/{index}"
            for index in range(max(0, len(widths) - 2))
        ]
        for key in ratio_keys:
            if band.lower[key] >= 1.0:
                failures.append("ORDERED_WIDTH_RATIO_NONCONTRACTING")
            elif band.upper[key] >= 1.0:
                unresolved.append("ORDERED_WIDTH_RATIO_UNRESOLVED")
        if ratio_keys:
            correction_key = f"width_correction/L{depth}/{len(widths) - 2}"
            tail = _geometric_tail_bound(
                correction_upper=max(0.0, band.upper[correction_key]),
                ratio_upper=max(0.0, band.upper[ratio_keys[-1]]),
            )
        else:
            tail = None
        width_tails[f"L{depth}"] = tail
        if tail is None:
            unresolved.append("ORDERED_WIDTH_TAIL_UNBOUNDED")
        elif tail > width_allocation:
            failures.append("ORDERED_WIDTH_TAIL_ALLOCATION_EXCEEDED")
        rows.append(
            {
                "stage": "ordered_scaling",
                "metric": f"width_tail_ball/L{depth}",
                "point": tail if tail is not None else "",
                "lower": "",
                "upper": tail if tail is not None else "",
                "semantics": "conditional norm-ball radius around finest-width curve",
            }
        )
    center_points = [
        band.point[f"depth_correction/{index}"]
        for index in range(max(0, len(depths) - 1))
    ]
    center_lowers = [
        max(0.0, band.lower[f"depth_correction/{index}"])
        for index in range(max(0, len(depths) - 1))
    ]
    center_uppers = [
        max(0.0, band.upper[f"depth_correction/{index}"])
        for index in range(max(0, len(depths) - 1))
    ]
    propagated_corrections, propagated_ratios = _propagated_depth_bounds(
        center_points=center_points,
        center_lowers=center_lowers,
        center_uppers=center_uppers,
        width_tail_radii=[width_tails[f"L{depth}"] for depth in depths],
    )
    for index, correction in enumerate(propagated_corrections):
        rows.append(
            {
                "stage": "ordered_scaling",
                "metric": f"depth_correction_width_propagated/{index}",
                "point": correction["point"] if correction is not None else "",
                "lower": correction["lower"] if correction is not None else "",
                "upper": correction["upper"] if correction is not None else "",
                "semantics": (
                    "adjacent-depth correction interval after adding both "
                    "width-limit norm-ball radii"
                ),
            }
        )
    for ratio in propagated_ratios:
        if ratio is None:
            unresolved.append("ORDERED_DEPTH_RATIO_DENOMINATOR_UNRESOLVED")
        elif ratio["lower"] >= 1.0:
            failures.append("ORDERED_DEPTH_RATIO_NONCONTRACTING")
        elif ratio["upper"] >= 1.0:
            unresolved.append("ORDERED_DEPTH_RATIO_UNRESOLVED")
    if (
        propagated_corrections
        and propagated_corrections[-1] is not None
        and propagated_ratios
        and propagated_ratios[-1] is not None
    ):
        depth_tail = _geometric_tail_bound(
            correction_upper=propagated_corrections[-1]["upper"],
            ratio_upper=propagated_ratios[-1]["upper"],
        )
    else:
        depth_tail = None
    if depth_tail is None:
        unresolved.append("ORDERED_DEPTH_TAIL_UNBOUNDED")
    elif depth_tail > depth_allocation:
        failures.append("ORDERED_DEPTH_TAIL_ALLOCATION_EXCEEDED")
    sampling_bound = max(
        max(0.0, band.upper[f"mean_shift/L{depth}/n{width}"])
        for width in widths
        for depth in depths
    )
    rows.append(
        {
            "stage": "ordered_scaling",
            "metric": "dense_sampling_bound",
            "point": sampling_bound,
            "lower": 0.0,
            "upper": sampling_bound,
            "semantics": (
                "simultaneous direct bootstrap displacement of each "
                "resampled mean curve from its full-root center"
            ),
        }
    )
    if tier != "positive" and not failures:
        unresolved.append("ORDERED_POSITIVE_GRID_REQUIRED")
    if failures:
        status = GateStatus.FAIL
        reasons = failures
    elif unresolved:
        status = GateStatus.UNRESOLVED
        reasons = unresolved
    else:
        status = GateStatus.PASS
        reasons = ["ORDERED_SCALING_AND_NORM_BALL_TAILS_PASS"]
    return (
        {
            "gate": _gate(
                status,
                *reasons,
                metrics={
                    "tail_semantics": "norm balls centered on finest curves",
                    "tier": tier,
                },
            ),
            "metrics": {
                "tier": tier,
                "widths": widths,
                "depths": depths,
                "confidence": confidence,
                "bootstrap_replicates": replicates,
                "critical_lower": band.critical_lower,
                "critical_upper": band.critical_upper,
                "bootstrap_calibration": _bootstrap_calibration_metadata(
                    band
                ),
                "inference_scope": {
                    "root_count": root_count,
                    "finite_sample_coverage_claimed": False,
                    "semantics": "assumption-dependent whole-root bootstrap",
                },
                "dispersion_semantics": (
                    "leave-one-out root distances; RMS is gated and "
                    "RMS/sqrt(root_count) is descriptive only; the direct "
                    "resampled-mean displacement bounds the ensemble mean; "
                    "sample maximum/q95 are descriptive only"
                ),
                "width_tail_norm_balls": width_tails,
                "depth_corrections_width_propagated": propagated_corrections,
                "depth_ratios_width_propagated": propagated_ratios,
                "depth_tail_norm_ball": depth_tail,
                "dense_sampling_upper_bound": sampling_bound,
                "finest_curve_center": {
                    "width": finest_width,
                    "depth": depths[-1],
                },
            },
            "missing": [],
            "component_bounds": {
                "dense_sampling": sampling_bound,
                "width_tail_conditional": (
                    max(value for value in width_tails.values() if value is not None)
                    if width_tails and all(value is not None for value in width_tails.values())
                    else None
                ),
                "depth_tail_conditional": depth_tail,
            },
        },
        rows,
    )


def _homogenization_prefix(depth: int, checkpoint: float) -> str:
    return f"D{depth}_t{int(round(1000.0 * checkpoint)):04d}"


def _expected_stage2_config(
    protocol: Mapping[str, Any],
    outer_root_index: int,
) -> Mapping[str, Any]:
    """Return the exact Stage-2 configuration emitted by the frozen runner."""

    stage = protocol["stage_2_homogenization"]
    model = protocol["scope"]["canonical_model"]
    return {
        "widths": [int(value) for value in stage["widths"]],
        "width": int(stage["width"]),
        "depths": [int(value) for value in stage["depths"]],
        "outer_root_index": int(outer_root_index),
        "outer_seed": derive_homogenization_outer_seed(
            int(protocol["error_ledger"]["bootstrap_seed"]),
            int(outer_root_index),
        ),
        "replicas": int(stage["independent_W_replicas_per_outer_root"]),
        "checkpoints": [float(value) for value in stage["checkpoints"]],
        "candidate_levels": [
            int(value) for value in stage["candidate_levels"]
        ],
        "dt": float(protocol["stage_1_ordered_target"]["dt"]),
        "canonical_model": {
            "X": np.asarray(model["X"], dtype=float).tolist(),
            "y": np.asarray(model["y"], dtype=float).tolist(),
            "activation": str(model["activation"]),
            "sigma_w": float(model["sigma_w"]),
            "A": float(model["A"]),
            "gamma": float(model["gamma"]),
        },
    }


def _validate_stage2_archive(
    protocol: Mapping[str, Any],
    item: LoadedEvidence,
) -> int:
    """Fail closed on Stage-2 root, config, inventory, shape, and RNG drift."""

    try:
        config = item.archive.metadata["config"]
        raw_root = config["outer_root_index"]
    except (KeyError, TypeError) as exc:
        raise AnalysisError(
            f"malformed homogenization config: {item.path}"
        ) from exc
    if isinstance(raw_root, bool) or not isinstance(raw_root, int):
        raise AnalysisError(
            f"homogenization outer-root index must be an integer: {item.path}"
        )
    root = int(raw_root)
    expected_roots = int(
        protocol["stage_2_homogenization"]["outer_B_a_roots"]
    )
    if not 0 <= root < expected_roots:
        raise AnalysisError(
            f"unexpected homogenization outer-root index {root}: {item.path}"
        )
    expected_config = _expected_stage2_config(protocol, root)
    if _canonical_json_bytes(config) != _canonical_json_bytes(expected_config):
        raise AnalysisError(
            f"homogenization config is not exactly preregistered: {item.path}"
        )

    model = expected_config["canonical_model"]
    X = np.asarray(model["X"], dtype=float)
    y = np.asarray(model["y"], dtype=float)
    try:
        validate_homogenization_archive_schema(
            item.archive.arrays,
            widths=expected_config["widths"],
            depths=expected_config["depths"],
            checkpoints=expected_config["checkpoints"],
            candidate_levels=expected_config["candidate_levels"],
            replicas=int(expected_config["replicas"]),
            input_dimension=X.shape[0],
            sample_count=y.size,
            outer_seed=int(expected_config["outer_seed"]),
        )
    except (ArchiveValidationError, TypeError, ValueError) as exc:
        raise AnalysisError(
            f"invalid homogenization archive schema: {item.path}: {exc}"
        ) from exc
    return root


def _finalize_stage2_gate(
    model_free_gate: GateVerdict,
) -> Mapping[str, Any]:
    """Apply the frozen boundary: no actual predictor means no Stage-2 pass."""

    if model_free_gate.status == GateStatus.FAIL:
        return model_free_gate.to_dict()
    return _gate(
        GateStatus.UNRESOLVED,
        "HOMOGENIZATION_ACTUAL_CONDITIONAL_ONSAGER_PREDICTOR_MISSING",
        *(
            model_free_gate.reason_codes
            if model_free_gate.status == GateStatus.UNRESOLVED
            else ()
        ),
        metrics={
            "model_free_status": model_free_gate.status.value,
            "finite_P_residual_semantics": "diagnostic_only",
        },
    )


def analyze_stage2_homogenization(
    context: AnalysisContext,
) -> tuple[Mapping[str, Any], list[Mapping[str, Any]]]:
    items = _stage_evidence(context, "homogenization")
    if not items:
        return _unresolved_missing("homogenization"), []
    protocol = context.protocol
    stage = protocol["stage_2_homogenization"]
    expected_roots = int(stage["outer_B_a_roots"])
    roots: dict[int, LoadedEvidence] = {}
    for item in items:
        root = _validate_stage2_archive(protocol, item)
        if root in roots:
            raise AnalysisError(f"duplicate homogenization outer root: {root}")
        roots[root] = item
    absent = sorted(set(range(expected_roots)) - set(roots))
    if absent:
        return (
            {
                "gate": _gate(
                    GateStatus.UNRESOLVED,
                    "HOMOGENIZATION_OUTER_ROOTS_INCOMPLETE",
                ),
                "metrics": {},
                "missing": [f"outer_root_indices={absent}"],
            },
            [],
        )
    widths = tuple(int(value) for value in stage["widths"])
    depths = tuple(int(value) for value in stage["depths"])
    checkpoints = tuple(float(value) for value in stage["checkpoints"])
    replicas = int(stage["independent_W_replicas_per_outer_root"])

    fields: dict[str, dict[int, InnovationSamples]] = {}
    model_free_names: list[str] = []
    diagnostic_names: list[str] = []
    width_ladders: dict[str, dict[int, str]] = {}
    summary_names = homogenization_summary_names(stage["candidate_levels"])
    covariance_diagnostics: dict[str, Any] = {}

    def prefix(width: int, depth: int, checkpoint: float) -> str:
        return (
            f"W{width}_D{depth}_"
            f"t{int(round(1000.0 * checkpoint)):04d}"
        )

    def fixed_half_bias_squared(values: Array) -> float:
        flat = np.asarray(values, dtype=float).reshape(replicas, -1)
        half = replicas // 2
        return float(
            np.mean(
                np.mean(flat[:half], axis=0)
                * np.mean(flat[half:], axis=0)
            )
        )

    def replica_variance(values: Array) -> float:
        flat = np.asarray(values, dtype=float).reshape(replicas, -1)
        return float(
            np.sum(
                (flat - np.mean(flat, axis=0, keepdims=True)) ** 2
            )
            / ((replicas - 1) * flat.shape[1])
        )

    for checkpoint in checkpoints:
        checkpoint_tag = f"t{checkpoint:g}"
        for width in widths:
            definitions = {
                f"terminal_hidden/n{width}/{checkpoint_tag}": "terminal_H",
                f"input_adjoint/n{width}/{checkpoint_tag}": "input_P",
                f"forward_depth_average/n{width}/{checkpoint_tag}": (
                    "forward_action_depth_average"
                ),
                f"transpose_depth_average/n{width}/{checkpoint_tag}": (
                    "transpose_action_depth_average"
                ),
            }
            for name, suffix in definitions.items():
                table: dict[int, InnovationSamples] = {}
                for depth in depths:
                    key = f"{prefix(width, depth, checkpoint)}_{suffix}"
                    values = []
                    for root in range(expected_roots):
                        arrays = roots[root].archive.arrays
                        if key not in arrays:
                            raise AnalysisError(
                                f"homogenization archive missing {key}: "
                                f"{roots[root].path}"
                            )
                        current = np.asarray(arrays[key], dtype=float)
                        if current.shape[0] != replicas:
                            raise AnalysisError(
                                f"homogenization replica mismatch: {key}"
                            )
                        values.append(current)
                    table[depth] = InnovationSamples(
                        np.stack(values), layered=False
                    )
                fields[name] = table
                model_free_names.append(name)
                group = name.replace(f"/n{width}", "")
                width_ladders.setdefault(group, {})[width] = name

            for summary_name in summary_names:
                name = f"{summary_name}/n{width}/{checkpoint_tag}"
                table = {}
                for depth in depths:
                    base = f"{prefix(width, depth, checkpoint)}_{summary_name}"
                    average_key = f"{base}_depth_average"
                    covariance_key = f"{base}_layer_covariance"
                    integrated_key = f"{base}_integrated_covariance"
                    bias_layer_key = f"{base}_bias_squared_by_layer"
                    bias_average_key = f"{base}_depth_average_bias_squared"
                    values = []
                    covariance_values = []
                    bias_layer_values = []
                    for root in range(expected_roots):
                        arrays = roots[root].archive.arrays
                        required = (
                            average_key,
                            covariance_key,
                            integrated_key,
                            bias_layer_key,
                            bias_average_key,
                        )
                        absent_keys = [
                            key for key in required if key not in arrays
                        ]
                        if absent_keys:
                            raise AnalysisError(
                                f"homogenization archive missing {absent_keys}: "
                                f"{roots[root].path}"
                            )
                        average = np.asarray(
                            arrays[average_key], dtype=float
                        )
                        covariance = np.asarray(
                            arrays[covariance_key], dtype=float
                        )
                        bias_layer = np.asarray(
                            arrays[bias_layer_key], dtype=float
                        )
                        if (
                            average.shape[0] != replicas
                            or covariance.shape != (depth, depth)
                            or bias_layer.shape != (depth,)
                        ):
                            raise AnalysisError(
                                f"homogenization compact summary shape "
                                f"mismatch: {base}"
                            )
                        stored_integrated = float(
                            np.asarray(arrays[integrated_key])
                        )
                        stored_bias = float(
                            np.asarray(arrays[bias_average_key])
                        )
                        covariance_integrated = float(
                            np.sum(covariance) / depth**2
                        )
                        recomputed_variance = replica_variance(average)
                        recomputed_bias = fixed_half_bias_squared(average)
                        if not (
                            np.isclose(
                                stored_integrated,
                                covariance_integrated,
                                rtol=2e-10,
                                atol=2e-12,
                            )
                            and np.isclose(
                                stored_integrated,
                                recomputed_variance,
                                rtol=2e-10,
                                atol=2e-12,
                            )
                            and np.isclose(
                                stored_bias,
                                recomputed_bias,
                                rtol=2e-10,
                                atol=2e-12,
                            )
                        ):
                            raise AnalysisError(
                                f"homogenization stored/recomputed compact "
                                f"summary mismatch: {base}"
                            )
                        values.append(average)
                        covariance_values.append(covariance)
                        bias_layer_values.append(bias_layer)
                    table[depth] = InnovationSamples(
                        np.stack(values), layered=False
                    )
                    covariance_diagnostics[
                        f"{name}/L{depth}"
                    ] = {
                        "mean_full_covariance_integral": float(
                            np.mean(
                                [
                                    np.sum(value) / depth**2
                                    for value in covariance_values
                                ]
                            )
                        ),
                        "mean_max_abs_layer_bias_squared": float(
                            np.mean(
                                [
                                    np.max(np.abs(value))
                                    for value in bias_layer_values
                                ]
                            )
                        ),
                        "uncertainty_scope": (
                            "point diagnostic only; no covariance-shape "
                            "bootstrap"
                        ),
                    }
                fields[name] = table
                group = name.replace(f"/n{width}", "")
                width_ladders.setdefault(group, {})[width] = name
                if (
                    "reconstruction_residual" in summary_name
                    or "projection_residual" in summary_name
                ):
                    diagnostic_names.append(name)
                elif summary_name in (
                    "forward_action",
                    "transpose_action",
                ):
                    # These duplicate the named depth-average model-free
                    # fields byte-for-byte; keep them as audited summaries,
                    # not a second gate entry.
                    pass

    (
        replicates_count,
        pilot_replicates,
        seed,
        confidence,
        mc_failure_probability,
    ) = _analysis_constants(context)
    summary = analyze_homogenization(
        fields,
        model_free_fields=tuple(model_free_names),
        # Neither the finite-P nonlinear reconstruction nor row-projection
        # residual is the conjectured conditional/Onsager mean, so these
        # fields remain familywise diagnostics.
        candidate_fields=(),
        candidate_bias_allocation=float(
            protocol["error_ledger"]["preallocated_components"][
                "amplified_closure"
            ]
        ),
        bootstrap_replicates=replicates_count,
        bootstrap_pilot_replicates=pilot_replicates,
        bootstrap_mc_failure_probability=mc_failure_probability,
        bootstrap_seed=seed + 202,
        confidence=confidence,
        conditional_mean_tested=True,
        width_ladders=width_ladders,
    )
    model_free_gate = summary.gate
    projection_failures: list[str] = []
    projection_unresolved: list[str] = []
    projection_allocation = float(
        protocol["error_ledger"]["preallocated_components"][
            "amplified_closure"
        ]
    )
    max_depth = depths[-1]
    for name in diagnostic_names:
        if "_P15/" not in name:
            continue
        slope_key = f"{name}/integrated_covariance_slope"
        slope_lower = float(summary.familywise_band.lower[slope_key])
        slope_upper = float(summary.familywise_band.upper[slope_key])
        if slope_lower >= -0.5:
            projection_failures.append(
                "HOMOGENIZATION_P15_DIAGNOSTIC_COVARIANCE_NONDECAY"
            )
        elif slope_upper >= -0.5:
            projection_unresolved.append(
                "HOMOGENIZATION_P15_DIAGNOSTIC_SLOPE_UNRESOLVED"
            )
        bias_key = f"{name}/bias_squared/L{max_depth}"
        bias_lower = float(summary.familywise_band.lower[bias_key])
        bias_upper = float(summary.familywise_band.upper[bias_key])
        if bias_lower > projection_allocation**2:
            projection_failures.append(
                "HOMOGENIZATION_P15_DIAGNOSTIC_BIAS_WARNING"
            )
        elif bias_upper > projection_allocation**2:
            projection_unresolved.append(
                "HOMOGENIZATION_P15_DIAGNOSTIC_BIAS_UNRESOLVED"
            )
    if projection_failures:
        projection_gate = _gate(
            GateStatus.FAIL, *sorted(set(projection_failures))
        )
    elif projection_unresolved:
        projection_gate = _gate(
            GateStatus.UNRESOLVED, *sorted(set(projection_unresolved))
        )
    else:
        projection_gate = _gate(
            GateStatus.PASS,
            "HOMOGENIZATION_P15_FINITE_P_DIAGNOSTIC_PASSES",
        )
    gate = _finalize_stage2_gate(model_free_gate)
    rows: list[Mapping[str, Any]] = []
    field_metrics: dict[str, Any] = {}
    for name, field in summary.fields.items():
        variance_slope_key = f"{name}/variance_slope"
        covariance_slope_key = f"{name}/integrated_covariance_slope"
        bias_squared_key = f"{name}/bias_squared/L{max_depth}"
        field_metrics[name] = {
            "variance_slope": field.variance_slope,
            "integrated_covariance_slope": field.integrated_covariance_slope,
            "bias_squared_at_max_depth": field.bias_squared_at_max_depth,
            "bias_squared_upper_at_max_depth": (
                field.bias_squared_upper_at_max_depth
            ),
            "bias_norm_at_max_depth": field.bias_norm_at_max_depth,
            "bias_norm_upper_at_max_depth": (
                field.bias_norm_upper_at_max_depth
            ),
        }
        for metric, value in (
            ("variance_slope", field.variance_slope),
            ("integrated_covariance_slope", field.integrated_covariance_slope),
            ("bias_squared_at_max_depth", field.bias_squared_at_max_depth),
            (
                "bias_squared_upper_at_max_depth",
                field.bias_squared_upper_at_max_depth,
            ),
            ("bias_norm_at_max_depth", field.bias_norm_at_max_depth),
            (
                "bias_norm_upper_at_max_depth",
                field.bias_norm_upper_at_max_depth,
            ),
        ):
            if metric == "variance_slope":
                lower = float(
                    summary.familywise_band.lower[variance_slope_key]
                )
                upper = float(
                    summary.familywise_band.upper[variance_slope_key]
                )
            elif metric == "integrated_covariance_slope":
                lower = float(
                    summary.familywise_band.lower[covariance_slope_key]
                )
                upper = float(
                    summary.familywise_band.upper[covariance_slope_key]
                )
            elif metric == "bias_squared_at_max_depth":
                lower = float(
                    summary.familywise_band.lower[bias_squared_key]
                )
                upper = float(
                    summary.familywise_band.upper[bias_squared_key]
                )
            elif metric == "bias_squared_upper_at_max_depth":
                lower = ""
                upper = field.bias_squared_upper_at_max_depth
            elif metric == "bias_norm_upper_at_max_depth":
                lower = ""
                upper = field.bias_norm_upper_at_max_depth
            else:
                lower = ""
                upper = ""
            rows.append(
                {
                    "stage": "homogenization",
                    "metric": f"{name}/{metric}",
                    "point": value,
                    "lower": lower,
                    "upper": upper,
                    "semantics": (
                        "finite-P residual diagnostic only"
                        if name in diagnostic_names
                        else "model-free depth statistic"
                    ),
                }
            )
    width_metrics: dict[str, Any] = {}
    for group in width_ladders:
        width_metrics[group] = {}
        for metric in (
            "variance",
            "integrated_covariance",
            "bias_squared",
        ):
            key = f"width/{group}/{metric}/ratio"
            width_metrics[group][metric] = {
                "ratio_point": float(summary.familywise_band.point[key]),
                "ratio_lower": float(summary.familywise_band.lower[key]),
                "ratio_upper": float(summary.familywise_band.upper[key]),
            }
            rows.append(
                {
                    "stage": "homogenization",
                    "metric": key,
                    "point": float(summary.familywise_band.point[key]),
                    "lower": float(summary.familywise_band.lower[key]),
                    "upper": float(summary.familywise_band.upper[key]),
                    "semantics": (
                        "paired n128-to256 vs n256-to512 scalar "
                        "correction ratio at L=128"
                    ),
                }
            )
    return (
        {
            "gate": gate,
            "model_free_gate": model_free_gate.to_dict(),
            "finite_P_diagnostic_gate": projection_gate,
            "metrics": {
                "confidence": confidence,
                "bootstrap_replicates": replicates_count,
                "bootstrap_calibration": _bootstrap_calibration_metadata(
                    summary.familywise_band
                ),
                "inference_scope": {
                    "outer_root_count": expected_roots,
                    "finite_sample_coverage_claimed": False,
                    "ledger_admissible": False,
                    "semantics": "four-outer-root diagnostic bootstrap",
                },
                "fields": field_metrics,
                "finite_P_diagnostics": diagnostic_names,
                "coupled_width_diagnostics": width_metrics,
                "full_covariance_diagnostics": covariance_diagnostics,
                "actual_conditional_mean_available": False,
                "hierarchical_bootstrap": {
                    "outer_roots_resampled": True,
                    "W_replicas_resampled_within_selected_outer_root": True,
                    "bias_split": [[0, 1, 2, 3], [4, 5, 6, 7]],
                },
            },
            "missing": ["actual trained conditional/Onsager predictor archive"],
        },
        rows,
    )


def _restart_gap(
    arrays: Mapping[str, Array],
    kind: str,
    *,
    amplitude_index: int,
    horizon: float,
    s_f: float,
    s_g: float,
) -> float:
    f_key = f"{kind}_restart_f_difference"
    g_key = f"{kind}_restart_gram_difference"
    if f_key not in arrays or g_key not in arrays:
        raise AnalysisError(f"attack archive lacks {kind} restart differences")
    if "restart_times" not in arrays:
        raise AnalysisError("attack archive lacks restart_times")
    times = np.asarray(arrays["restart_times"], dtype=float)
    f_all = np.asarray(arrays[f_key], dtype=float)
    gram_all = np.asarray(arrays[g_key], dtype=float)
    if (
        f_all.ndim != 3
        or gram_all.ndim != 5
        or f_all.shape[0] <= amplitude_index
        or gram_all.shape[0] <= amplitude_index
        or f_all.shape[1] != times.size
        or gram_all.shape[1] != times.size
    ):
        raise AnalysisError(f"attack {kind} restart shapes are malformed")
    mask = times <= horizon + 1e-13
    if not np.any(mask) or not np.isclose(times[mask][-1], horizon):
        raise AnalysisError(f"attack restart path has no horizon {horizon}")
    f = f_all[amplitude_index, mask]
    gram = gram_all[amplitude_index, mask]
    return max(
        float(np.max(np.linalg.norm(f, axis=-1))) / s_f,
        float(np.max(np.linalg.norm(gram, axis=(-2, -1)))) / s_g,
    )


def _attack_constraint_defect(
    item: LoadedEvidence,
    *,
    amplitudes: Sequence[float],
    basis_ladder: Sequence[int],
) -> float:
    detail = item.archive.metadata.get("scientific_detail", {})
    maximum = 0.0
    if not isinstance(detail, Mapping):
        raise AnalysisError(f"attack scientific detail is missing: {item.path}")
    multilayer = detail.get("multilayer", {})
    if not isinstance(multilayer, Mapping):
        raise AnalysisError(f"attack multilayer defects are missing: {item.path}")
    expected_defects = {
        "Z",
        "T",
        "H",
        "P",
        "f",
        "gram",
        "theta",
        *(f"P{level}_retained_row_coefficients" for level in basis_ladder),
    }
    expected_amplitudes = {
        f"alpha_{float(amplitude):g}" for amplitude in amplitudes
    }
    for kind in ("independent", "coherent"):
        kind_detail = multilayer.get(kind)
        if not isinstance(kind_detail, Mapping):
            raise AnalysisError(
                f"attack {kind} multilayer defects are missing: {item.path}"
            )
        by_amplitude = kind_detail.get(
            "relative_present_state_defects_by_amplitude"
        )
        if not isinstance(by_amplitude, Mapping) or set(
            by_amplitude
        ) != expected_amplitudes:
            raise AnalysisError(
                f"attack {kind} amplitude-defect inventory mismatch: "
                f"{item.path}"
            )
        for label in expected_amplitudes:
            defects = by_amplitude[label]
            if not isinstance(defects, Mapping) or not expected_defects.issubset(
                defects
            ):
                raise AnalysisError(
                    f"attack {kind}/{label} defect inventory is partial: "
                    f"{item.path}"
                )
            values = [float(defects[name]) for name in expected_defects]
            if not all(np.isfinite(values)):
                raise AnalysisError(f"attack constraint defect is nonfinite")
            maximum = max(maximum, max(values))
    direction_defects = detail.get("direction_constraint_defects", {})
    if not isinstance(direction_defects, Mapping):
        raise AnalysisError(f"attack direction defects are missing: {item.path}")
    depth = int(item.archive.config["L"])
    expected_direction_names = {
        f"{kind}_layer_{layer}"
        for kind in ("independent", "coherent")
        for layer in range(depth)
    }
    if set(direction_defects) != expected_direction_names:
        raise AnalysisError(
            f"attack direction/layer defect inventory mismatch: {item.path}"
        )
    expected_direction_defects = {
        "deltaW_P35_fro",
        "deltaW_H_fro",
        "deltaW_T_beta_fro",
        "unit_frobenius_error",
    }
    for label in expected_direction_names:
        defects = direction_defects[label]
        if not isinstance(defects, Mapping) or not expected_direction_defects.issubset(
            defects
        ):
            raise AnalysisError(
                f"attack direction defect inventory is partial: {item.path}"
            )
        values = [
            float(defects[name]) for name in expected_direction_defects
        ]
        if not all(np.isfinite(values)):
            raise AnalysisError("attack direction constraint is nonfinite")
        maximum = max(maximum, max(values))
    return maximum


def _attack_sequential_decision(
    *,
    screen_candidates: Sequence[tuple[float, float]],
    persistent_candidates: Sequence[tuple[float, float]],
    screen_constraints_pass: bool,
    confirmation_constraints_pass: bool,
    confirmation_complete: bool,
    confirmation_present: bool,
) -> tuple[GateStatus, list[str], bool]:
    """Apply the frozen one-sided screen/confirmation decision tree."""

    if not screen_constraints_pass:
        reasons = ["ATTACK_SCREEN_PRESENT_STATE_CONSTRAINT_UNRESOLVED"]
        if confirmation_present:
            reasons.append("ATTACK_CONFIRMATION_PRESENT_WITHOUT_VALID_TRIGGER")
        return GateStatus.UNRESOLVED, reasons, False
    if not screen_candidates:
        reasons = [
            "ATTACK_NULL_SCREEN_NO_OFF_MANIFOLD_COUNTEREXAMPLE",
            "ATTACK_NO_COUNTEREXAMPLE_IS_NOT_SUFFICIENCY_EVIDENCE",
        ]
        if confirmation_present:
            reasons.append("ATTACK_CONFIRMATION_PRESENT_WITHOUT_VALID_TRIGGER")
        return GateStatus.UNRESOLVED, reasons, False
    if not confirmation_complete:
        return (
            GateStatus.UNRESOLVED,
            ["ATTACK_SCREEN_TRIGGERED_CONFIRMATION_INCOMPLETE"],
            True,
        )
    if not confirmation_constraints_pass:
        return (
            GateStatus.UNRESOLVED,
            ["ATTACK_CONFIRMATION_PRESENT_STATE_CONSTRAINT_UNRESOLVED"],
            True,
        )
    if persistent_candidates:
        return (
            GateStatus.FAIL,
            ["ATTACK_P35_COHERENT_GAP_CONFIRMED_WIDTH_DEPTH_PERSISTENT"],
            True,
        )
    return (
        GateStatus.UNRESOLVED,
        [
            "ATTACK_SCREEN_SIGNAL_NOT_CONFIRMED_ACROSS_WIDTH_DEPTH",
            "ATTACK_NO_COUNTEREXAMPLE_IS_NOT_SUFFICIENCY_EVIDENCE",
        ],
        True,
    )


def analyze_stage3_attack(
    context: AnalysisContext,
) -> tuple[Mapping[str, Any], list[Mapping[str, Any]]]:
    items = _stage_evidence(context, "attack")
    if not items:
        return _unresolved_missing("same_state_attack"), []
    protocol = context.protocol
    stage = protocol["stage_3_same_state_attack"]
    widths = tuple(int(value) for value in stage["widths"])
    depths = tuple(int(value) for value in stage["depths"])
    amplitudes = tuple(float(value) for value in stage["amplitudes"])
    horizons = tuple(float(value) for value in stage["restart_horizons"])
    root_count = int(stage["heldout_roots"])
    tolerance = float(stage["constraint_tolerance_relative"])
    allocation = float(
        protocol["error_ledger"]["preallocated_components"]["amplified_closure"]
    )
    sequential = stage.get("sequential_design")
    if not isinstance(sequential, Mapping):
        raise AnalysisError("Stage 3 lacks its frozen sequential design")
    screen_config = sequential.get("screen_cell")
    confirmation_config = sequential.get("confirmation_cells")
    if not isinstance(screen_config, Mapping) or not isinstance(
        confirmation_config, list
    ):
        raise AnalysisError("Stage 3 sequential cell inventory is malformed")
    screen_cell = (int(screen_config["n"]), int(screen_config["L"]))
    confirmation_cells = tuple(
        (int(value["n"]), int(value["L"]))
        for value in confirmation_config
    )
    threshold = float(sequential["trigger_threshold"])
    if not np.isclose(threshold, allocation):
        raise AnalysisError(
            "Stage 3 screen threshold differs from amplified-closure allocation"
        )
    if int(sequential["screen_roots"]) != root_count:
        raise AnalysisError("Stage 3 screen root count is inconsistent")
    s_f = float(protocol["norms"]["S_f"])
    s_g = float(protocol["norms"]["S_G"])
    cells: dict[tuple[int, int], dict[int, LoadedEvidence]] = {}
    for item in items:
        config = item.archive.metadata["config"]
        try:
            key = (int(config["n"]), int(config["L"]))
            root = int(config["root_index"])
        except (KeyError, TypeError, ValueError) as exc:
            raise AnalysisError(f"malformed attack config: {item.path}") from exc
        _require_exact_config(
            item,
            _expected_attack_config(
                protocol,
                n=key[0],
                depth=key[1],
                root_index=root,
            ),
            label="attack",
        )
        table = cells.setdefault(key, {})
        if root in table:
            raise AnalysisError(f"duplicate attack root for {key}: {root}")
        table[root] = item
    expected_cells = {(width, depth) for width in widths for depth in depths}
    if expected_cells != {screen_cell, *confirmation_cells}:
        raise AnalysisError(
            "Stage 3 sequential cells do not equal the declared width/depth grid"
        )
    extra = set(cells) - expected_cells
    if extra:
        raise AnalysisError(f"attack archives contain undeclared cells: {sorted(extra)}")
    screen_missing = sorted(
        set(range(root_count)) - set(cells.get(screen_cell, {}))
    )
    if screen_missing:
        return (
            {
                "gate": _gate(
                    GateStatus.UNRESOLVED,
                    "ATTACK_SCREEN_INCOMPLETE",
                    metrics={"missing_root_count": len(screen_missing)},
                ),
                "metrics": {},
                "missing": [f"{screen_cell}:roots={screen_missing}"],
            },
            [],
        )

    expected_master = (max(widths), max(depths))
    confirmation_missing = {
        cell: sorted(set(range(root_count)) - set(cells.get(cell, {})))
        for cell in confirmation_cells
    }
    confirmation_complete = all(
        not missing for missing in confirmation_missing.values()
    )
    confirmation_present = any(
        cells.get(cell) for cell in confirmation_cells
    )
    analysis_cells = (
        (screen_cell,) + confirmation_cells
        if confirmation_complete
        else (screen_cell,)
    )
    for root in range(root_count):
        root_items = [cells[cell][root] for cell in analysis_cells]
        seeds = {
            int(item.archive.metadata["config"].get("root_seed", -1))
            for item in root_items
        }
        master_shapes = {
            (
                int(item.archive.metadata["config"].get("master_width", -1)),
                int(item.archive.metadata["config"].get("master_depth", -1)),
            )
            for item in root_items
        }
        if len(seeds) != 1 or master_shapes != {expected_master}:
            raise AnalysisError(
                "attack root is not jointly coupled across width/depth cells: "
                f"root={root}, seeds={sorted(seeds)}, "
                f"master_shapes={sorted(master_shapes)}"
            )
        master_hashes = []
        for item in root_items:
            detail = item.archive.metadata.get("scientific_detail", {})
            hashes = (
                detail.get("coupled_root_sha256")
                if isinstance(detail, Mapping)
                else None
            )
            if not isinstance(hashes, Mapping):
                raise AnalysisError(
                    f"attack archive lacks coupled-root hashes: {item.path}"
                )
            master_hashes.append(_canonical_json_bytes(hashes))
        if len(set(master_hashes)) != 1:
            raise AnalysisError(
                "attack root master hashes disagree across cells: "
                f"root={root}"
            )

    gaps: dict[tuple[str, int, int, float, float], Array] = {}
    constraint_by_cell: dict[tuple[int, int], float] = {}
    for cell, root_items in cells.items():
        cell_maximum = 0.0
        for root, item in root_items.items():
            item = cells[cell][root]
            arrays = item.archive.arrays
            if not np.array_equal(
                np.asarray(arrays.get("amplitudes"), dtype=float),
                np.asarray(amplitudes),
            ) or not np.array_equal(
                np.asarray(arrays.get("restart_horizons"), dtype=float),
                np.asarray(horizons),
            ):
                raise AnalysisError(f"attack bundle grid mismatch: {item.path}")
            if int(np.asarray(arrays.get("primary_basis_size"))) != 35:
                raise AnalysisError(f"attack is not P35-primary: {item.path}")
            if not np.array_equal(
                np.asarray(arrays.get("basis_ladder"), dtype=int),
                np.asarray((5, 15, 35)),
            ):
                raise AnalysisError(f"attack basis ladder mismatch: {item.path}")
            cell_maximum = max(
                cell_maximum,
                _attack_constraint_defect(
                    item,
                    amplitudes=amplitudes,
                    basis_ladder=(5, 15, 35),
                ),
            )
        constraint_by_cell[cell] = cell_maximum
    for cell in analysis_cells:
        for kind in ("independent", "coherent"):
            for amplitude_index, amplitude in enumerate(amplitudes):
                for horizon in horizons:
                    values = [
                        _restart_gap(
                            cells[cell][root].archive.arrays,
                            kind,
                            amplitude_index=amplitude_index,
                            horizon=horizon,
                            s_f=s_f,
                            s_g=s_g,
                        )
                        for root in range(root_count)
                    ]
                    gaps[(kind, *cell, amplitude, horizon)] = np.asarray(values)

    def make_statistic(
        included_cells: Sequence[tuple[int, int]],
        *,
        include_slopes: bool,
    ) -> Callable[[Array], Mapping[str, float]]:
        included = tuple(included_cells)

        def statistic(indices: Array) -> Mapping[str, float]:
            means = {
                key: float(np.mean(value[indices]))
                for key, value in gaps.items()
                if (key[1], key[2]) in included
            }
            result: dict[str, float] = {}
            for (
                kind,
                width,
                depth,
                amplitude,
                horizon,
            ), value in means.items():
                result[
                    f"gap/{kind}/n{width}/L{depth}/"
                    f"a{amplitude:g}/T{horizon:g}"
                ] = value
            if include_slopes:
                for kind in ("independent", "coherent"):
                    for horizon in horizons:
                        for depth in depths:
                            for amplitude in amplitudes:
                                values = [
                                    means[
                                        (
                                            kind,
                                            width,
                                            depth,
                                            amplitude,
                                            horizon,
                                        )
                                    ]
                                    for width in widths
                                ]
                                result[
                                    f"width_slope/{kind}/L{depth}/"
                                    f"a{amplitude:g}/T{horizon:g}"
                                ] = _log_slope(widths, values)
                        for width in widths:
                            for amplitude in amplitudes:
                                values = [
                                    means[
                                        (
                                            kind,
                                            width,
                                            depth,
                                            amplitude,
                                            horizon,
                                        )
                                    ]
                                    for depth in depths
                                ]
                                result[
                                    f"depth_slope/{kind}/n{width}/"
                                    f"a{amplitude:g}/T{horizon:g}"
                                ] = _log_slope(depths, values)
            return result

        return statistic

    (
        replicates,
        pilot_replicates,
        seed,
        confidence,
        mc_failure_probability,
    ) = _analysis_constants(
        context, sequential_look=True
    )
    screen_band = _scalarize_band(
        whole_root_familywise_bootstrap(
            root_count=root_count,
            statistic=make_statistic(
                (screen_cell,), include_slopes=False
            ),
            replicates=replicates,
            pilot_replicates=pilot_replicates,
            seed=seed + 303,
            confidence=confidence,
            mc_failure_probability=mc_failure_probability,
        )
    )
    confirmation_band = (
        _scalarize_band(
            whole_root_familywise_bootstrap(
                root_count=root_count,
                statistic=make_statistic(
                    analysis_cells, include_slopes=True
                ),
                replicates=replicates,
                pilot_replicates=pilot_replicates,
                seed=seed + 304,
                confidence=confidence,
                mc_failure_probability=mc_failure_probability,
            )
        )
        if confirmation_complete
        else None
    )
    rows: list[Mapping[str, Any]] = []
    screen_candidates: list[tuple[float, float]] = []
    persistent_coherent: list[tuple[float, float]] = []
    for kind in ("independent", "coherent"):
        for width, depth in analysis_cells:
            current_band = (
                screen_band
                if (width, depth) == screen_cell
                else confirmation_band
            )
            if current_band is None:  # pragma: no cover
                raise AnalysisError("confirmation band is unexpectedly absent")
            for amplitude in amplitudes:
                for horizon in horizons:
                    key = (
                        f"gap/{kind}/n{width}/L{depth}/"
                        f"a{amplitude:g}/T{horizon:g}"
                    )
                    rows.append(
                        {
                            "stage": "same_state_attack",
                            "metric": key,
                            "point": current_band.point[key],
                            "lower": max(0.0, current_band.lower[key]),
                            "upper": max(0.0, current_band.upper[key]),
                            "semantics": (
                                f"{kind} P35-invisible off-manifold restart gap"
                            ),
                        }
                    )
        if kind == "coherent":
            for amplitude in amplitudes:
                for horizon in horizons:
                    screen_key = (
                        f"gap/coherent/n{screen_cell[0]}/L{screen_cell[1]}/"
                        f"a{amplitude:g}/T{horizon:g}"
                    )
                    if screen_band.lower[screen_key] > threshold:
                        screen_candidates.append((amplitude, horizon))
                    if (
                        confirmation_complete
                        and (amplitude, horizon) in screen_candidates
                        and confirmation_band is not None
                        and all(
                            confirmation_band.lower[
                            f"gap/coherent/n{width}/L{depth}/"
                            f"a{amplitude:g}/T{horizon:g}"
                        ]
                        > threshold
                            for width, depth in confirmation_cells
                        )
                    ):
                        persistent_coherent.append((amplitude, horizon))
    screen_constraints_pass = constraint_by_cell[screen_cell] <= tolerance
    confirmation_constraints_pass = confirmation_complete and all(
        constraint_by_cell[cell] <= tolerance for cell in confirmation_cells
    )
    status, reasons, triggered = _attack_sequential_decision(
        screen_candidates=screen_candidates,
        persistent_candidates=persistent_coherent,
        screen_constraints_pass=screen_constraints_pass,
        confirmation_constraints_pass=confirmation_constraints_pass,
        confirmation_complete=confirmation_complete,
        confirmation_present=confirmation_present,
    )
    missing = []
    if triggered and not confirmation_complete:
        missing = [
            f"{cell}:roots={absent}"
            for cell, absent in confirmation_missing.items()
            if absent
        ]
    return (
        {
            "gate": _gate(
                status,
                *reasons,
                metrics={
                    "primary_attack": "coherent_P35",
                    "off_manifold_reachability_caveat": True,
                    "sequential_screen_cell": screen_cell,
                    "confirmation_triggered": triggered,
                },
            ),
            "independent_diagnostic_gate": _gate(
                GateStatus.UNRESOLVED,
                "ATTACK_INDEPENDENT_CORROBORATING_DIAGNOSTIC_ONLY",
            ),
            "metrics": {
                "confidence": confidence,
                "bootstrap_replicates": replicates,
                "screen_critical_lower": screen_band.critical_lower,
                "screen_critical_upper": screen_band.critical_upper,
                "screen_bootstrap_calibration": (
                    _bootstrap_calibration_metadata(screen_band)
                ),
                "confirmation_critical_lower": (
                    confirmation_band.critical_lower
                    if confirmation_band is not None
                    else None
                ),
                "confirmation_critical_upper": (
                    confirmation_band.critical_upper
                    if confirmation_band is not None
                    else None
                ),
                "confirmation_bootstrap_calibration": (
                    _bootstrap_calibration_metadata(confirmation_band)
                    if confirmation_band is not None
                    else None
                ),
                "inference_scope": {
                    "root_count": root_count,
                    "finite_sample_coverage_claimed": False,
                    "semantics": "assumption-dependent eight-root bootstrap",
                },
                "alpha_spending": "equal Stage-3 half-alpha per frozen look",
                "max_present_state_constraint_defect_by_cell": {
                    f"n{cell[0]}_L{cell[1]}": value
                    for cell, value in sorted(constraint_by_cell.items())
                },
                "allocation": allocation,
                "screen_threshold": threshold,
                "screen_candidates": screen_candidates,
                "persistent_coherent_cells": persistent_coherent,
                "screen_complete": True,
                "confirmation_complete": confirmation_complete,
                "confirmation_present": confirmation_present,
                "analyzed_cells": analysis_cells,
                "basis_ladder": (5, 15, 35),
                "primary_basis_size": 35,
            },
            "missing": missing,
            "ledger_semantics": "attack gaps are not an additive error component",
        },
        rows,
    )


def _pair_tag(pair: tuple[int, int]) -> str:
    return f"P{pair[0]}_Q{pair[1]}"


def _decode_ascii_names(value: Array) -> tuple[str, ...]:
    result = []
    for item in np.asarray(value).reshape(-1):
        if isinstance(item, bytes):
            result.append(item.decode("ascii"))
        else:
            result.append(str(item))
    return tuple(result)


def _decode_ascii_scalar(value: Array, name: str) -> str:
    array = np.asarray(value)
    if array.shape != ():
        raise AnalysisError(f"{name} must be a scalar")
    item = array.item()
    return item.decode("ascii") if isinstance(item, bytes) else str(item)


def _generator_total_residual_path(
    value: Array,
    *,
    checkpoint_count: int,
    name: str,
) -> Array:
    """Validate a four-component generator residual and return its total."""

    array = np.asarray(value, dtype=float)
    if array.shape != (checkpoint_count, 4):
        raise AnalysisError(f"generator {name} shape mismatch")
    if not np.all(np.isfinite(array)):
        raise AnalysisError(f"generator {name} contains nonfinite values")
    return array[:, 3]


def _structural_resolution_key(
    *,
    protocol: Mapping[str, Any],
    stage_key: str,
    item: LoadedEvidence,
    resolution: Mapping[str, Any] | None = None,
) -> tuple[str, int]:
    """Validate one Stage-4/5 structural resolution configuration."""

    config = item.archive.config
    if resolution is None:
        resolution = protocol[stage_key]["numerical_resolution"]
    primary = resolution["primary"]
    coordinates = ("base_order", "N", "R", "dt")
    try:
        requested = {
            "base_order": int(config["base_order"]),
            "N": int(config["N"]),
            "R": int(config["R"]),
            "dt": float(config["dt"]),
            "seed": int(config["seed"]),
        }
        axis = str(config["resolution_axis"])
        is_primary = bool(config["resolution_is_primary"])
        declared_M = int(config["M"])
    except (KeyError, TypeError, ValueError) as exc:
        raise AnalysisError(
            f"malformed structural resolution config: {item.path}"
        ) from exc
    if axis == "primary":
        valid = (
            requested["seed"] in tuple(map(int, primary["scramble_seeds"]))
            and requested["base_order"] == int(primary["base_order"])
            and requested["N"] == int(primary["N"])
            and requested["R"] == int(primary["R"])
            and requested["dt"] == float(primary["dt"])
        )
        expected_primary = True
    else:
        candidates = [
            candidate
            for candidate in resolution[
                "one_axis_refinements_at_seed_20260723"
            ]
            if str(candidate["axis"]) == axis
        ]
        valid = len(candidates) == 1 and (
            requested["base_order"] == int(candidates[0]["base_order"])
            and requested["N"] == int(candidates[0]["N"])
            and requested["R"] == int(candidates[0]["R"])
            and requested["dt"] == float(candidates[0]["dt"])
            and requested["seed"] == int(candidates[0]["seed"])
        )
        expected_primary = False
    if not valid or is_primary != expected_primary:
        raise AnalysisError(
            f"undeclared structural resolution configuration: {item.path}"
        )
    latent_dimension = (
        len(protocol["scope"]["canonical_model"]["X"]) + 1
    )
    expected_M = requested["base_order"] ** latent_dimension
    if declared_M != expected_M:
        raise AnalysisError(f"structural M/base-order mismatch: {item.path}")
    arrays = item.archive.arrays
    required_array_values: Mapping[str, tuple[Any, np.dtype[Any]]] = {
        "numerical_resolution_base_order": (
            requested["base_order"],
            np.dtype(np.int64),
        ),
        "numerical_resolution_M": (expected_M, np.dtype(np.int64)),
        "numerical_resolution_N": (
            requested["N"],
            np.dtype(np.int64),
        ),
        "numerical_resolution_R": (
            requested["R"],
            np.dtype(np.int64),
        ),
        "numerical_resolution_dt": (
            requested["dt"],
            np.dtype(np.float64),
        ),
        "numerical_resolution_seed": (
            requested["seed"],
            np.dtype(np.int64),
        ),
        "numerical_resolution_is_primary": (
            int(expected_primary),
            np.dtype(np.uint8),
        ),
    }
    if "numerical_resolution_axis_ascii" not in arrays:
        raise AnalysisError(f"structural axis array is missing: {item.path}")
    if (
        _decode_ascii_scalar(
            arrays["numerical_resolution_axis_ascii"],
            "numerical_resolution_axis_ascii",
        )
        != axis
    ):
        raise AnalysisError(f"structural axis metadata mismatch: {item.path}")
    for name, (expected, expected_dtype) in required_array_values.items():
        if name not in arrays:
            raise AnalysisError(f"structural resolution array {name} missing")
        value = np.asarray(arrays[name])
        if (
            value.shape != ()
            or value.dtype != expected_dtype
            or value.item() != expected
        ):
            raise AnalysisError(
                f"structural resolution array {name} mismatch: {item.path}"
            )
    return axis, requested["seed"]


def _structural_expected_keys(
    protocol: Mapping[str, Any],
    stage_key: str,
    *,
    resolution: Mapping[str, Any] | None = None,
) -> set[tuple[str, int]]:
    if resolution is None:
        resolution = protocol[stage_key]["numerical_resolution"]
    primary = resolution["primary"]
    expected = {
        ("primary", int(seed))
        for seed in primary["scramble_seeds"]
    }
    expected.update(
        (str(candidate["axis"]), int(candidate["seed"]))
        for candidate in resolution[
            "one_axis_refinements_at_seed_20260723"
        ]
    )
    return expected


def _generator_shared_arrays_identical(
    low_item: LoadedEvidence, extended_item: LoadedEvidence
) -> None:
    """Verify that a conditional P70 rerun did not change any P<=35 byte."""

    ignored = {
        "levels",
        "pairs",
        "numerical_resolution_family_ascii",
    }
    shared = (set(low_item.archive.arrays) & set(extended_item.archive.arrays)) - ignored
    for key in shared:
        if hash_array(low_item.archive.arrays[key]) != hash_array(
            extended_item.archive.arrays[key]
        ):
            raise AnalysisError(
                "P70 extension changed a frozen P<=35 generator array: "
                f"{key}, seeds "
                f"{low_item.archive.config.get('seed')} and "
                f"{extended_item.archive.config.get('seed')}"
            )


def analyze_stage4_generator(
    context: AnalysisContext,
    *,
    _selected_level: int | None = None,
) -> tuple[Mapping[str, Any], list[Mapping[str, Any]]]:
    items = _stage_evidence(context, "generator")
    if not items:
        return _unresolved_missing("generator"), []
    if _selected_level is None:
        base_result, base_rows = analyze_stage4_generator(
            context, _selected_level=35
        )
        p70_present = any(
            int(item.archive.config.get("max_level", -1)) == 70
            for item in items
        )
        trigger = (
            "GENERATOR_P70_EXTENSION_REQUIRED"
            in base_result["gate"]["reason_codes"]
        )
        if not p70_present:
            return base_result, base_rows
        if not trigger:
            status = GateStatus(base_result["gate"]["status"])
            reason = "GENERATOR_P70_PRESENT_WITHOUT_BASE_TRIGGER"
            return (
                {
                    **base_result,
                    "gate": _gate(
                        status,
                        *base_result["gate"]["reason_codes"],
                        reason,
                        metrics=base_result["gate"].get("metrics", {}),
                    ),
                    "conditional_P70_evidence_ignored": True,
                },
                base_rows,
            )
        active_by_key = {
            (
                str(item.archive.config.get("resolution_axis")),
                int(item.archive.config.get("seed", -1)),
            ): item
            for item in items
            if int(item.archive.config.get("max_level", -1)) == 35
        }
        p70_by_key = {
            (
                str(item.archive.config.get("resolution_axis")),
                int(item.archive.config.get("seed", -1)),
            ): item
            for item in items
            if int(item.archive.config.get("max_level", -1)) == 70
        }
        for key in sorted(set(active_by_key) & set(p70_by_key)):
            _generator_shared_arrays_identical(
                active_by_key[key], p70_by_key[key]
            )
        extension_result, extension_rows = analyze_stage4_generator(
            context, _selected_level=70
        )
        return (
            {
                **extension_result,
                "base_trigger_gate": base_result["gate"],
                "base_trigger_metrics": base_result.get("metrics", {}),
                "sequential_alpha_spending": (
                    "equal Stage-4 half-alpha base and conditional-P70 looks"
                ),
            },
            base_rows + extension_rows,
        )
    if _selected_level not in (35, 70):
        raise AnalysisError("invalid internal generator level selection")
    protocol = context.protocol
    stage = protocol["stage_4_generator_consistency"]
    checkpoints = np.asarray(stage["checkpoints"], dtype=float)
    base_pairs = tuple(tuple(map(int, pair)) for pair in stage["pairs"])
    primary_resolution = stage["numerical_resolution"]
    p70_resolution = protocol["stage_0_integrity_and_numerics"][
        "P70_conditional_extension"
    ].get("numerical_resolution")
    records: dict[tuple[int, str, int], LoadedEvidence] = {}
    for item in items:
        config = item.archive.config
        try:
            max_level = int(config["max_level"])
        except (KeyError, TypeError, ValueError) as exc:
            raise AnalysisError(f"malformed generator config: {item.path}") from exc
        if max_level not in (35, 70):
            raise AnalysisError(f"undeclared generator configuration: {item.path}")
        if max_level != _selected_level:
            continue
        if max_level == 70 and not isinstance(p70_resolution, Mapping):
            raise AnalysisError(
                "P70 generator archive exists without a declared P70 "
                f"resolution family: {item.path}"
            )
        resolution = (
            p70_resolution if max_level == 70 else primary_resolution
        )
        axis, seed_value = _structural_resolution_key(
            protocol=protocol,
            stage_key="stage_4_generator_consistency",
            item=item,
            resolution=resolution,
        )
        family_key = "numerical_resolution_family_ascii"
        expected_family = (
            "conditional_P70_nested"
            if max_level == 70
            else "stage_4_generator_consistency_active"
        )
        expected_levels = [5, 15, 35]
        expected_pairs = [
            [int(value) for value in pair]
            for pair in stage["pairs"]
        ]
        if max_level == 70:
            expected_levels.append(70)
            expected_pairs.append([35, 70])
        _require_exact_config(
            item,
            {
                **_expected_resolution_config(
                    protocol,
                    resolution,
                    axis=axis,
                    seed=seed_value,
                    family=expected_family,
                ),
                "levels": expected_levels,
                "pairs": expected_pairs,
                "max_level": max_level,
                "conditional_p70_authorized": max_level == 70,
                "checkpoints": [
                    float(value) for value in stage["checkpoints"]
                ],
                "shadow_horizons": [
                    float(value) for value in stage["shadow_horizons"]
                ],
                "canonical_model": _canonical_model_config(protocol),
            },
            label="generator",
        )
        if family_key not in item.archive.arrays or _decode_ascii_scalar(
            item.archive.arrays[family_key], family_key
        ) != expected_family:
            raise AnalysisError(
                f"generator resolution-family metadata mismatch: {item.path}"
            )
        key = (max_level, axis, seed_value)
        if key in records:
            raise AnalysisError(f"duplicate generator configuration: {key}")
        arrays = item.archive.arrays
        if "checkpoints" not in arrays or not np.array_equal(
            np.asarray(arrays["checkpoints"], dtype=float), checkpoints
        ):
            raise AnalysisError(f"generator checkpoint grid mismatch: {item.path}")
        records[key] = item

    selected_level = _selected_level
    selected_resolution = (
        p70_resolution if selected_level == 70 else primary_resolution
    )
    if not isinstance(selected_resolution, Mapping):
        return (
            {
                "gate": _gate(
                    GateStatus.UNRESOLVED,
                    "GENERATOR_P70_RESOLUTION_FAMILY_MISSING",
                ),
                "metrics": {},
                "missing": ["conditional P70 numerical-resolution protocol"],
            },
            [],
        )
    expected_selected = {
        (selected_level, axis, seed_value)
        for axis, seed_value in _structural_expected_keys(
            protocol,
            "stage_4_generator_consistency",
            resolution=selected_resolution,
        )
    }
    missing_selected = sorted(expected_selected - set(records))
    if missing_selected:
        return (
            {
                "gate": _gate(
                    GateStatus.UNRESOLVED,
                    (
                        "GENERATOR_P70_EXTENSION_INCOMPLETE"
                        if selected_level == 70
                        else "GENERATOR_STRUCTURAL_RESOLUTION_INCOMPLETE"
                    ),
                ),
                "metrics": {},
                "missing": [str(value) for value in missing_selected],
            },
            [],
        )
    extension_complete = selected_level == 70
    seeds = tuple(
        int(value)
        for value in selected_resolution["primary"]["scramble_seeds"]
    )
    seed0 = seeds[0]
    refinement_axes = tuple(
        str(value["axis"])
        for value in selected_resolution[
            "one_axis_refinements_at_seed_20260723"
        ]
    )
    selected = {
        (axis, seed_value): records[(selected_level, axis, seed_value)]
        for axis, seed_value in _structural_expected_keys(
            protocol,
            "stage_4_generator_consistency",
            resolution=selected_resolution,
        )
    }
    joint_corner_certified = _has_cofinal_joint_corner_certificate(
        selected_resolution
    )
    pairs = base_pairs + (((35, 70),) if extension_complete else ())
    shadow_horizons = tuple(float(value) for value in stage["shadow_horizons"])
    shadow_sup_depth_available = True

    def paths_from_item(
        item: LoadedEvidence,
    ) -> dict[tuple[tuple[int, int], str], Array]:
        nonlocal shadow_sup_depth_available
        result: dict[tuple[tuple[int, int], str], Array] = {}
        arrays = item.archive.arrays
        for pair in pairs:
            tag = _pair_tag(pair)
            required = {
                "lift_consistency": f"{tag}_lift_consistency",
                "back": f"{tag}_R_back",
                "outgoing": f"{tag}_R_out_lift",
                "full_high_outgoing": f"{tag}_R_out_high_state",
                "observable": f"{tag}_back_full_observable_primary",
            }
            absent = [value for value in required.values() if value not in arrays]
            if absent:
                raise AnalysisError(
                    f"generator archive missing {absent}: {item.path}"
                )
            back_array = np.asarray(arrays[required["back"]], dtype=float)
            lift_array = np.asarray(
                arrays[required["lift_consistency"]], dtype=float
            )
            observable_array = np.asarray(
                arrays[required["observable"]], dtype=float
            )
            outgoing_array = np.asarray(
                arrays[required["outgoing"]], dtype=float
            )
            full_high_array = np.asarray(
                arrays[required["full_high_outgoing"]], dtype=float
            )
            back_total = _generator_total_residual_path(
                back_array,
                checkpoint_count=checkpoints.size,
                name=f"{tag} back",
            )
            lift_low_total = _generator_total_residual_path(
                lift_array,
                checkpoint_count=checkpoints.size,
                name=f"{tag} lift-low",
            )
            if observable_array.shape != (checkpoints.size, 3):
                raise AnalysisError(
                    f"generator observable shape mismatch: {tag}"
                )
            for value, name in (
                (outgoing_array, "outgoing"),
                (full_high_array, "full_high_outgoing"),
            ):
                if value.shape != (checkpoints.size,):
                    raise AnalysisError(
                        f"generator {name} shape mismatch: {tag}"
                    )
            result[(pair, "back")] = back_total
            result[(pair, "lift_low")] = lift_low_total
            result[(pair, "outgoing")] = outgoing_array
            result[(pair, "full_high_outgoing")] = full_high_array
            result[(pair, "observable")] = observable_array[:, 2]
            for horizon in shadow_horizons:
                horizon_tag = f"h{int(round(1000.0 * horizon)):04d}"
                legacy_key = (
                    f"{tag}_shadow_{horizon_tag}_"
                    "increment_observable_normalized"
                )
                sup_depth_key = (
                    f"{tag}_shadow_{horizon_tag}_"
                    "increment_observable_normalized_sup_depth"
                )
                key = (
                    sup_depth_key
                    if sup_depth_key in arrays
                    else legacy_key
                )
                if sup_depth_key not in arrays:
                    shadow_sup_depth_available = False
                if key not in arrays:
                    raise AnalysisError(
                        f"generator archive missing shadow {key}: {item.path}"
                    )
                value = np.asarray(arrays[key], dtype=float)
                if value.shape[0] != checkpoints.size:
                    raise AnalysisError(f"shadow checkpoint shape mismatch: {key}")
                result[(pair, f"shadow_T{horizon:g}")] = value
        return result

    all_paths = {
        key: paths_from_item(item) for key, item in selected.items()
    }
    scalar_metrics = (
        "back",
        "lift_low",
        "outgoing",
        "full_high_outgoing",
        "observable",
        "shadow",
    )

    def scalar_value(
        paths: Mapping[tuple[tuple[int, int], str], Array],
        pair: tuple[int, int],
        metric: str,
    ) -> float:
        if metric == "shadow":
            return max(
                float(
                    np.max(paths[(pair, f"shadow_T{horizon:g}")])
                )
                for horizon in shadow_horizons
            )
        return float(np.trapezoid(paths[(pair, metric)], checkpoints))

    def path_cauchy(
        left: Mapping[tuple[tuple[int, int], str], Array],
        right: Mapping[tuple[tuple[int, int], str], Array],
        pair: tuple[int, int],
        metric: str,
    ) -> float:
        if metric == "shadow":
            return max(
                float(
                    np.max(
                        np.abs(
                            left[(pair, f"shadow_T{horizon:g}")]
                            - right[(pair, f"shadow_T{horizon:g}")]
                        )
                    )
                )
                for horizon in shadow_horizons
            )
        return float(
            np.trapezoid(
                np.abs(left[(pair, metric)] - right[(pair, metric)]),
                checkpoints,
            )
        )

    primary_values = {
        (pair, metric): np.asarray(
            [
                scalar_value(
                    all_paths[("primary", seed_value)], pair, metric
                )
                for seed_value in seeds
            ]
        )
        for pair in pairs
        for metric in scalar_metrics
    }
    cauchy_values = {
        (pair, metric, axis): path_cauchy(
            all_paths[("primary", seed0)],
            all_paths[(axis, seed0)],
            pair,
            metric,
        )
        for pair in pairs
        for metric in scalar_metrics
        for axis in refinement_axes
    }

    representative = selected[("primary", seed0)].archive.arrays
    required_basis = (
        "basis_component_names_ascii",
        "basis_hermite_diagnostics",
        "basis_random_diagnostics",
        "basis_pod_diagnostics",
    )
    missing_basis = [key for key in required_basis if key not in representative]
    if missing_basis:
        raise AnalysisError(f"generator basis arrays missing: {missing_basis}")
    basis_names = _decode_ascii_names(
        representative["basis_component_names_ascii"]
    )
    basis: dict[str, Array] = {}
    for kind, key in (
        ("hermite", "basis_hermite_diagnostics"),
        ("pod", "basis_pod_diagnostics"),
    ):
        values = [
            np.asarray(
                selected[("primary", seed_value)].archive.arrays[key],
                dtype=float,
            )
            for seed_value in seeds
        ]
        basis[kind] = np.stack(values)
    random_values = [
        np.asarray(
            selected[("primary", seed_value)].archive.arrays[
                "basis_random_diagnostics"
            ],
            dtype=float,
        )
        for seed_value in seeds
    ]
    basis["random"] = np.stack(random_values)
    if basis["hermite"].shape[-1] != len(basis_names):
        raise AnalysisError("basis component-name count mismatch")

    consecutive = [(5, 15), (15, 35)]
    if extension_complete:
        consecutive.append((35, 70))

    def statistic(indices: Array) -> Mapping[str, float]:
        result: dict[str, float] = {}
        for pair in pairs:
            tag = _pair_tag(pair)
            for metric in scalar_metrics:
                values = primary_values[(pair, metric)]
                mean = float(np.mean(values[indices]))
                label = (
                    "shadow_max"
                    if metric == "shadow"
                    else f"{metric}_integral"
                )
                result[f"{label}/{tag}"] = mean
                result[f"scramble_radius/{label}/{tag}"] = float(
                    np.quantile(
                        np.abs(values[indices] - mean),
                        0.95,
                        method="higher",
                    )
                )
                result[f"sampling/{label}/{tag}"] = abs(
                    mean - float(np.mean(values))
                )
                for axis in refinement_axes:
                    result[f"cauchy/{label}/{tag}/{axis}"] = (
                        cauchy_values[(pair, metric, axis)]
                    )
        for metric in (
            "back_integral",
            "lift_low_integral",
            "outgoing_integral",
            "observable_integral",
            "shadow_max",
        ):
            values = [result[f"{metric}/{_pair_tag(pair)}"] for pair in consecutive]
            for index in range(len(values) - 1):
                result[f"ratio/{metric}/{index}"] = min(
                    values[index + 1] / max(values[index], 1e-300),
                    1e6,
                )
        for kind in ("hermite", "pod"):
            mean = np.mean(basis[kind][indices], axis=0)
            for component, name in enumerate(basis_names):
                result[f"basis/{kind}/{name}"] = float(
                    np.max(mean[..., component])
                )
        random_mean = np.mean(basis["random"][indices], axis=0)
        for random_index in range(random_mean.shape[0]):
            for component, name in enumerate(basis_names):
                result[f"basis/random{random_index}/{name}"] = float(
                    np.max(random_mean[random_index, ..., component])
                )
        return result

    (
        replicates,
        pilot_replicates,
        seed,
        confidence,
        mc_failure_probability,
    ) = _analysis_constants(
        context, sequential_look=True
    )
    band = _scalarize_band(
        whole_root_familywise_bootstrap(
            root_count=len(seeds),
            statistic=statistic,
            replicates=replicates,
            pilot_replicates=pilot_replicates,
            seed=seed + 404,
            confidence=confidence,
            mc_failure_probability=mc_failure_probability,
        )
    )
    failures: list[str] = []
    unresolved: list[str] = []
    gated_metrics = (
        "back_integral",
        "lift_low_integral",
        "outgoing_integral",
        "observable_integral",
        "shadow_max",
    )
    if not shadow_sup_depth_available:
        unresolved.append("GENERATOR_SHADOW_SUP_DEPTH_GRAM_MISSING")
    numerics_allocation = float(
        protocol["error_ledger"]["preallocated_components"]["PDE_numerics"]
    )
    numerical_bounds: dict[str, Any] = {}
    residual_intervals: dict[tuple[str, tuple[int, int]], tuple[float, float]] = {}
    for metric in (
        *gated_metrics,
        "full_high_outgoing_integral",
    ):
        for pair in pairs:
            tag = _pair_tag(pair)
            residual_key = f"{metric}/{tag}"
            scramble_upper = max(
                0.0, band.upper[f"scramble_radius/{metric}/{tag}"]
            )
            sampling_upper = max(
                0.0, band.upper[f"sampling/{metric}/{tag}"]
            )
            by_axis = {}
            for axis in refinement_axes:
                cauchy_key = f"cauchy/{metric}/{tag}/{axis}"
                by_axis[axis] = _sparse_refinement_upper_bound(
                    one_seed_axis_upper=max(0.0, band.upper[cauchy_key]),
                    primary_scramble_radius_upper=scramble_upper,
                    primary_sampling_upper=sampling_upper,
                )
            numerical_upper, combination_rule = (
                _combine_structural_nuisance_upper_bound(by_axis)
            )
            numerical_bounds[f"{metric}/{tag}"] = {
                "by_axis": by_axis,
                "combined_upper": numerical_upper,
                "combination_rule": combination_rule,
                "cofinal_interaction_bound": joint_corner_certified,
            }
            lower = max(0.0, band.lower[residual_key] - numerical_upper)
            upper = max(0.0, band.upper[residual_key]) + numerical_upper
            residual_intervals[(metric, pair)] = (lower, upper)
            if metric in gated_metrics:
                if (
                    metric in ("observable_integral", "shadow_max")
                    and numerical_upper > numerics_allocation
                ):
                    unresolved.append(
                        "GENERATOR_STRUCTURAL_NUMERICS_EXCEED_ALLOCATION"
                    )
                if lower <= 0.0 or numerical_upper >= 0.2 * lower:
                    unresolved.append(
                        "GENERATOR_STRUCTURAL_NUMERICS_NOT_SEPARATED"
                    )
    if not joint_corner_certified:
        unresolved.append(
            "GENERATOR_STRUCTURAL_NUMERICS_NO_COFINAL_JOINT_CORNER"
        )
    propagated_ratios: dict[str, Any] = {}
    for metric in gated_metrics:
        for index in range(len(consecutive) - 1):
            previous = consecutive[index]
            following = consecutive[index + 1]
            previous_lower, previous_upper = residual_intervals[
                (metric, previous)
            ]
            following_lower, following_upper = residual_intervals[
                (metric, following)
            ]
            label = f"{metric}/{_pair_tag(previous)}_to_{_pair_tag(following)}"
            if previous_lower <= 0.0:
                propagated_ratios[label] = None
                unresolved.append("GENERATOR_CONTRACTION_DENOMINATOR_UNRESOLVED")
                continue
            ratio_lower = following_lower / max(previous_upper, 1e-300)
            ratio_upper = following_upper / previous_lower
            propagated_ratios[label] = {
                "lower": ratio_lower,
                "upper": ratio_upper,
            }
            if ratio_lower >= 1.0:
                failures.append("GENERATOR_RESIDUAL_NONCONTRACTING")
            elif ratio_upper >= 1.0:
                unresolved.append("GENERATOR_CONTRACTION_UNRESOLVED")
    if not extension_complete and not failures:
        if not unresolved and all(
            propagated_ratios.get(
                f"{metric}/{_pair_tag(consecutive[0])}_to_"
                f"{_pair_tag(consecutive[1])}"
            )
            is not None
            and propagated_ratios[
                f"{metric}/{_pair_tag(consecutive[0])}_to_"
                f"{_pair_tag(consecutive[1])}"
            ]["upper"]
            < 1.0
            for metric in gated_metrics
        ):
            unresolved.append("GENERATOR_P70_EXTENSION_REQUIRED")
        else:
            unresolved.append("GENERATOR_P70_TRIGGER_UNRESOLVED")
    if extension_complete and len(consecutive) >= 3:
        # Whether running P70 was authorized by the measured amplified
        # residual is checked by Stage 5; absent Stage 5 remains unresolved.
        unresolved.append("GENERATOR_P70_TRIGGER_REQUIRES_STAGE5")
    axis_only_diagnostic_status: GateStatus
    axis_only_diagnostic_reasons: list[str]
    if failures:
        axis_only_diagnostic_status = GateStatus.FAIL
        axis_only_diagnostic_reasons = failures
    elif unresolved:
        axis_only_diagnostic_status = GateStatus.UNRESOLVED
        axis_only_diagnostic_reasons = unresolved
    else:
        axis_only_diagnostic_status = GateStatus.PASS
        axis_only_diagnostic_reasons = [
            "GENERATOR_RESIDUALS_RESOLVED_AND_CONTRACT_THROUGH_P70"
        ]
    if not joint_corner_certified:
        status = GateStatus.UNRESOLVED
        reasons = [
            "GENERATOR_STRUCTURAL_NUMERICS_NO_COFINAL_JOINT_CORNER",
            "GENERATOR_AXIS_SUM_IS_EMPIRICAL_NOT_INTERACTION_CERTIFICATE",
        ]
        if axis_only_diagnostic_status == GateStatus.FAIL:
            reasons.append(
                "GENERATOR_AXIS_ONLY_DIAGNOSTIC_INDICATES_NONCONTRACTION"
            )
    elif failures:
        status = GateStatus.FAIL
        reasons = failures
    elif unresolved:
        status = GateStatus.UNRESOLVED
        reasons = unresolved
    else:
        status = GateStatus.PASS
        reasons = ["GENERATOR_RESIDUALS_RESOLVED_AND_CONTRACT_THROUGH_P70"]
    rows: list[Mapping[str, Any]] = []
    pair_metrics: dict[str, Any] = {}
    for pair in pairs:
        tag = _pair_tag(pair)
        pair_metrics[tag] = {}
        for metric in (
            "back_integral",
            "lift_low_integral",
            "outgoing_integral",
            "full_high_outgoing_integral",
            "observable_integral",
            "shadow_max",
        ):
            key = f"{metric}/{tag}"
            pair_metrics[tag][metric] = {
                "point": band.point[key],
                "lower": max(0.0, band.lower[key]),
                "upper": max(0.0, band.upper[key]),
            }
            rows.append(
                {
                    "stage": "generator_consistency",
                    "metric": key,
                    "point": band.point[key],
                    "lower": max(0.0, band.lower[key]),
                    "upper": max(0.0, band.upper[key]),
                    "semantics": "integrated generator/shadow defect",
                }
            )
    return (
        {
            "gate": _gate(
                status,
                *reasons,
                metrics={
                    "outgoing_reported_not_double_counted": True,
                    "P70_extension_complete": extension_complete,
                    "axis_only_diagnostic_status": (
                        axis_only_diagnostic_status.value
                    ),
                    "axis_only_diagnostic_reason_codes": (
                        axis_only_diagnostic_reasons
                    ),
                },
            ),
            "trigger_state": (
                "P70_EVALUATED_PENDING_STAGE5"
                if extension_complete
                else (
                    "TRIGGER_READY"
                    if reasons == ["GENERATOR_P70_EXTENSION_REQUIRED"]
                    else "NOT_READY"
                )
            ),
            "metrics": {
                "confidence": confidence,
                "bootstrap_replicates": replicates,
                "critical_lower": band.critical_lower,
                "critical_upper": band.critical_upper,
                "bootstrap_calibration": _bootstrap_calibration_metadata(
                    band
                ),
                "inference_scope": {
                    "root_count": len(seeds),
                    "finite_sample_coverage_claimed": False,
                    "ledger_admissible": False,
                    "semantics": "four-scramble diagnostic bootstrap",
                },
                "pairs": pair_metrics,
                "consecutive_pairs": consecutive,
                "basis_component_names": basis_names,
                "basis_semantics": "POD trained on pilot times and evaluated held-out",
                "numerical_residual_bound_available": (
                    joint_corner_certified
                ),
                "empirical_axis_sum_available": True,
                "numerical_combination_rule": (
                    "direct_primary_to_joint_corner"
                    if joint_corner_certified
                    else "conservative_empirical_axis_sum"
                ),
                "cofinal_joint_corner_certificate": (
                    joint_corner_certified
                ),
                "selected_resolution_family": (
                    "conditional_P70" if extension_complete else "active_P35"
                ),
                "numerical_bounds": numerical_bounds,
                "numerically_propagated_contraction_ratios": (
                    propagated_ratios
                ),
            },
            "missing": [],
        },
        rows,
    )


def _conditional_geometric_amplification(
    *,
    A15_point: float,
    A15_lower: float,
    A15_upper: float,
    A35_point: float,
    A35_lower: float,
    A35_upper: float,
    conditional_numerical_resolution_certified: bool,
    formal_statistical_coverage: bool = False,
) -> Mapping[str, Any]:
    """Form the scoped P35-to-infinity candidate from two closure steps."""

    values = tuple(
        float(value)
        for value in (
            A15_point,
            A15_lower,
            A15_upper,
            A35_point,
            A35_lower,
            A35_upper,
        )
    )
    if any(not np.isfinite(value) or value < 0.0 for value in values):
        raise ValueError("amplification bounds must be finite/nonnegative")
    if values[1] > values[0] or values[0] > values[2]:
        raise ValueError("A15 point must lie inside its interval")
    if values[4] > values[3] or values[3] > values[5]:
        raise ValueError("A35 point must lie inside its interval")
    ratio_point = (
        float(A35_point / A15_point) if A15_point > 0.0 else None
    )
    ratio_lower = (
        float(A35_lower / A15_upper) if A15_upper > 0.0 else None
    )
    ratio_upper = (
        float(A35_upper / A15_lower) if A15_lower > 0.0 else None
    )
    candidate_point = (
        float(A35_point / (1.0 - ratio_point))
        if ratio_point is not None and ratio_point < 1.0
        else None
    )
    candidate_upper = (
        float(A35_upper / (1.0 - ratio_upper))
        if ratio_upper is not None and ratio_upper < 1.0
        else None
    )
    ledger_bound = (
        candidate_upper
        if (
            candidate_upper is not None
            and conditional_numerical_resolution_certified
            and formal_statistical_coverage
        )
        else None
    )
    return {
        "A15_point": float(A15_point),
        "A15_lower": float(A15_lower),
        "A15_upper": float(A15_upper),
        "A35_point": float(A35_point),
        "A35_lower": float(A35_lower),
        "A35_upper": float(A35_upper),
        "ratio_point": ratio_point,
        "ratio_lower": ratio_lower,
        "ratio_upper": ratio_upper,
        "ratio_upper_below_one": (
            ratio_upper is not None and ratio_upper < 1.0
        ),
        "candidate_P35_to_infinity_point": candidate_point,
        "candidate_P35_to_infinity_upper": candidate_upper,
        "conditional_numerical_resolution_certified": bool(
            conditional_numerical_resolution_certified
        ),
        "formal_statistical_coverage": bool(formal_statistical_coverage),
        "ledger_component_upper_bound": ledger_bound,
    }


def analyze_stage5_gain(
    context: AnalysisContext,
    *,
    _conditional_p70: bool = False,
) -> tuple[Mapping[str, Any], list[Mapping[str, Any]]]:
    all_items = _stage_evidence(context, "amplification")
    def is_conditional(item: LoadedEvidence) -> bool:
        return (
            int(item.archive.config.get("low_level", -1)) == 35
            and int(item.archive.config.get("high_level", -1)) == 70
        )

    # The two Stage-5 looks are analyzed separately.  Central reconciliation
    # authorizes the second look only from frozen active-only Stage-4/5 gates.
    items = tuple(
        item
        for item in all_items
        if is_conditional(item) == _conditional_p70
    )
    if not items:
        return _unresolved_missing(
            (
                "conditional P35-from-P70 amplification"
                if _conditional_p70
                else "amplification"
            )
        ), []
    protocol = context.protocol
    stage = protocol["stage_5_amplification"]
    if _conditional_p70:
        declaration = stage.get("conditional_P70_extension")
        if not isinstance(declaration, Mapping):
            raise AnalysisError(
                "conditional P70 gain evidence has no frozen declaration"
            )
        if declaration.get("residual_pair") != [35, 70]:
            raise AnalysisError(
                "conditional P70 gain residual pair is not [35,70]"
            )
        resolution = protocol["stage_0_integrity_and_numerics"][
            "P70_conditional_extension"
        ]["numerical_resolution"]
        low_levels = (35,)
        expected_high_level = 70
        expected_resolution_family = "conditional_P70_gain"
    else:
        resolution = stage["numerical_resolution"]
        low_levels = tuple(int(value) for value in stage["low_levels"])
        expected_high_level = 35
        expected_resolution_family = "stage_5_amplification_active"
    joint_corner_certified = _has_cofinal_joint_corner_certificate(
        resolution
    )
    seeds = tuple(
        int(value) for value in resolution["primary"]["scramble_seeds"]
    )
    seed0 = seeds[0]
    refinement_axes = tuple(
        str(value["axis"])
        for value in resolution[
            "one_axis_refinements_at_seed_20260723"
        ]
    )
    grids = ("primary", "refined")
    records: dict[tuple[int, str, str, int], LoadedEvidence] = {}
    for item in items:
        config = item.archive.config
        try:
            low_level = int(config["low_level"])
            grid = str(config["time_grid_name"])
        except (KeyError, TypeError, ValueError) as exc:
            raise AnalysisError(f"malformed gain configuration: {item.path}") from exc
        try:
            high_level = int(config["high_level"])
        except (KeyError, TypeError, ValueError) as exc:
            raise AnalysisError(
                f"malformed gain high level: {item.path}"
            ) from exc
        if (
            low_level not in low_levels
            or high_level != expected_high_level
            or grid not in grids
        ):
            raise AnalysisError(f"undeclared gain configuration: {item.path}")
        axis, seed_value = _structural_resolution_key(
            protocol=protocol,
            stage_key="stage_5_amplification",
            item=item,
            resolution=resolution,
        )
        family_key = "numerical_resolution_family_ascii"
        arrays = item.archive.arrays
        if (
            family_key not in arrays
            or _decode_ascii_scalar(arrays[family_key], family_key)
            != expected_resolution_family
        ):
            raise AnalysisError(
                f"gain resolution-family metadata mismatch: {item.path}"
            )
        expected_authorized = bool(_conditional_p70)
        closure_step_scope = (
            str(
                stage["conditional_P70_extension"].get(
                    "interpretation",
                    (
                        "next measured closure step only; not a "
                        "P-to-infinity claim"
                    ),
                )
            )
            if _conditional_p70
            else "active finite residual-dictionary closure measurement"
        )
        declared_grid = [
            float(value) for value in stage["time_grids"][grid]
        ]
        _require_exact_config(
            item,
            {
                **_expected_resolution_config(
                    protocol,
                    resolution,
                    axis=axis,
                    seed=seed_value,
                    family=expected_resolution_family,
                ),
                "low_level": low_level,
                "high_level": high_level,
                "conditional_p70_authorized": expected_authorized,
                "closure_step_scope": closure_step_scope,
                "horizon": float(stage["horizon"]),
                "time_grid_name": grid,
                "source_times": declared_grid,
                "observation_times": declared_grid,
                "residual_snapshot_times": declared_grid,
                "nonlinear_amplitudes": [
                    float(value)
                    for value in stage[
                        "symmetric_nonlinear_amplitude_magnitudes"
                    ]
                ],
                "observable_blocks": ["f", "grams"],
                "canonical_model": _canonical_model_config(protocol),
            },
            label="gain",
        )
        if (
            bool(config.get("conditional_p70_authorized", False))
            != expected_authorized
        ):
            raise AnalysisError(
                f"gain conditional authorization metadata mismatch: {item.path}"
            )
        if "residual_pair_levels" not in arrays or not np.array_equal(
            np.asarray(arrays["residual_pair_levels"], dtype=np.int64),
            np.asarray([low_level, high_level], dtype=np.int64),
        ):
            raise AnalysisError(
                f"gain residual-pair array mismatch: {item.path}"
            )
        if "conditional_p70_authorized" not in arrays or bool(
            np.asarray(arrays["conditional_p70_authorized"]).item()
        ) != expected_authorized:
            raise AnalysisError(
                f"gain authorization array mismatch: {item.path}"
            )
        key = (low_level, grid, axis, seed_value)
        if key in records:
            raise AnalysisError(f"duplicate gain configuration: {key}")
        declared_times = np.asarray(declared_grid, dtype=float)
        if not np.array_equal(
            np.asarray(config["source_times"], dtype=float), declared_times
        ):
            raise AnalysisError(f"gain source grid mismatch: {item.path}")
        records[key] = item
    expected = {
        (low_level, grid, axis, seed_value)
        for low_level in low_levels
        for grid in grids
        for axis, seed_value in _structural_expected_keys(
            protocol,
            "stage_5_amplification",
            resolution=resolution,
        )
    }
    missing = sorted(expected - set(records))
    if missing:
        return (
            {
                "gate": _gate(
                    GateStatus.UNRESOLVED,
                    (
                        "AMPLIFICATION_P70_CONDITIONAL_FAMILY_INCOMPLETE"
                        if _conditional_p70
                        else "AMPLIFICATION_TIME_GRID_OR_SCRAMBLE_MISSING"
                    ),
                ),
                "metrics": {},
                "missing": [str(value) for value in missing],
            },
            [],
        )

    def gain_values(item: LoadedEvidence) -> dict[str, float]:
        arrays = item.archive.arrays
        required = (
            "primary_residual_subspace_gain",
            "residual_state_norm_L1_time_integral",
            "amplified_residual_bound_discrete",
            "residual_snapshot_times",
            "residual_basis_reconstruction_error",
            "residual_basis_relative_reconstruction_error",
            "nonlinear_plus_absolute_error",
            "nonlinear_minus_absolute_error",
            "nonlinear_symmetry_defect",
        )
        absent = [key for key in required if key not in arrays]
        if absent:
            raise AnalysisError(f"gain archive missing {absent}: {item.path}")
        gain = float(np.asarray(arrays[required[0]]))
        residual_integral = float(np.asarray(arrays[required[1]]))
        times = np.asarray(arrays[required[3]], dtype=float)
        reconstruction_path = np.asarray(arrays[required[4]], dtype=float)
        relative_path = np.asarray(arrays[required[5]], dtype=float)
        if reconstruction_path.shape != times.shape:
            raise AnalysisError("gain reconstruction path/time mismatch")
        reconstruction = gain * float(
            np.trapezoid(reconstruction_path, times)
        )
        one_sided_error = max(
            float(np.max(arrays[required[6]])),
            float(np.max(arrays[required[7]])),
            float(np.max(arrays[required[8]])),
        )
        return {
            "gain": gain,
            "residual_integral": residual_integral,
            "linear_amplified": float(np.asarray(arrays[required[2]])),
            "reconstruction": reconstruction,
            "nonlinear_remainder": one_sided_error * residual_integral,
            "relative_reconstruction": float(np.max(relative_path)),
        }

    values_by_record = {
        key: gain_values(item) for key, item in records.items()
    }
    value_names = tuple(
        next(iter(values_by_record.values()))
    )
    primary_values: dict[tuple[int, str, str], Array] = {}
    for low_level in low_levels:
        for grid in grids:
            for name in value_names:
                primary_values[(low_level, grid, name)] = np.asarray(
                    [
                        values_by_record[
                            (low_level, grid, "primary", seed_value)
                        ][name]
                        for seed_value in seeds
                    ]
                )

    def closure_value(
        low_level: int,
        axis: str,
        seed_value: int,
    ) -> float:
        primary = values_by_record[
            (low_level, "primary", axis, seed_value)
        ]
        refined = values_by_record[
            (low_level, "refined", axis, seed_value)
        ]
        return (
            refined["linear_amplified"]
            + refined["reconstruction"]
            + refined["nonlinear_remainder"]
            + abs(
                refined["linear_amplified"]
                - primary["linear_amplified"]
            )
        )

    closure_primary = {
        low_level: np.asarray(
            [
                closure_value(low_level, "primary", seed_value)
                for seed_value in seeds
            ]
        )
        for low_level in low_levels
    }
    cauchy_values: dict[tuple[int, str, str, str], float] = {}
    for low_level in low_levels:
        for grid in grids:
            for name in value_names:
                base = values_by_record[
                    (low_level, grid, "primary", seed0)
                ][name]
                for axis in refinement_axes:
                    refined = values_by_record[
                        (low_level, grid, axis, seed0)
                    ][name]
                    cauchy_values[(low_level, grid, name, axis)] = abs(
                        refined - base
                    )
        base_closure = closure_value(low_level, "primary", seed0)
        for axis in refinement_axes:
            cauchy_values[
                (low_level, "combined", "amplified_closure_total", axis)
            ] = abs(
                closure_value(low_level, axis, seed0) - base_closure
            )

    def statistic(indices: Array) -> Mapping[str, float]:
        result: dict[str, float] = {}
        for low_level in low_levels:
            prefix = f"P{low_level}"
            for grid in grids:
                for name in value_names:
                    values = primary_values[(low_level, grid, name)]
                    mean = float(np.mean(values[indices]))
                    result[f"{prefix}/{grid}/{name}"] = mean
                    result[f"scramble/{prefix}/{grid}/{name}"] = float(
                        np.quantile(
                            np.abs(values[indices] - mean),
                            0.95,
                            method="higher",
                        )
                    )
                    result[f"sampling/{prefix}/{grid}/{name}"] = abs(
                        mean - float(np.mean(values))
                    )
                    for axis in refinement_axes:
                        result[
                            f"cauchy/{prefix}/{grid}/{name}/{axis}"
                        ] = cauchy_values[
                            (low_level, grid, name, axis)
                        ]
            source_time_error = float(
                np.mean(
                    np.abs(
                        primary_values[
                            (low_level, "refined", "linear_amplified")
                        ][indices]
                        - primary_values[
                            (low_level, "primary", "linear_amplified")
                        ][indices]
                    )
                )
            )
            result[f"{prefix}/source_time_discretization"] = source_time_error
            closure = closure_primary[low_level]
            closure_mean = float(np.mean(closure[indices]))
            result[f"{prefix}/amplified_closure_total"] = closure_mean
            result[f"scramble/{prefix}/amplified_closure_total"] = float(
                np.quantile(
                    np.abs(closure[indices] - closure_mean),
                    0.95,
                    method="higher",
                )
            )
            result[f"sampling/{prefix}/amplified_closure_total"] = abs(
                closure_mean - float(np.mean(closure))
            )
            for axis in refinement_axes:
                result[
                    f"cauchy/{prefix}/amplified_closure_total/{axis}"
                ] = cauchy_values[
                    (
                        low_level,
                        "combined",
                        "amplified_closure_total",
                        axis,
                    )
                ]
        return result

    (
        replicates,
        pilot_replicates,
        seed,
        confidence,
        mc_failure_probability,
    ) = _analysis_constants(
        context, sequential_look=True
    )
    band = _scalarize_band(
        whole_root_familywise_bootstrap(
            root_count=len(seeds),
            statistic=statistic,
            replicates=replicates,
            pilot_replicates=pilot_replicates,
            seed=seed + (506 if _conditional_p70 else 505),
            confidence=confidence,
            mc_failure_probability=mc_failure_probability,
        )
    )
    allocation = float(
        protocol["error_ledger"]["preallocated_components"]["amplified_closure"]
    )
    numerics_allocation = float(
        protocol["error_ledger"]["preallocated_components"]["PDE_numerics"]
    )
    numerical_bounds: dict[str, Any] = {}
    total_numerical_upper: dict[int, float] = {}
    for low_level in low_levels:
        prefix = f"P{low_level}"
        scramble_upper = max(
            0.0,
            band.upper[f"scramble/{prefix}/amplified_closure_total"],
        )
        sampling_upper = max(
            0.0,
            band.upper[f"sampling/{prefix}/amplified_closure_total"],
        )
        by_axis = {
            axis: _sparse_refinement_upper_bound(
                one_seed_axis_upper=max(
                    0.0,
                    band.upper[
                        f"cauchy/{prefix}/amplified_closure_total/{axis}"
                    ],
                ),
                primary_scramble_radius_upper=scramble_upper,
                primary_sampling_upper=sampling_upper,
            )
            for axis in refinement_axes
        }
        (
            total_numerical_upper[low_level],
            combination_rule,
        ) = (
            _combine_structural_nuisance_upper_bound(by_axis)
        )
        numerical_bounds[prefix] = {
            "by_axis": by_axis,
            "combined_upper": total_numerical_upper[low_level],
            "combination_rule": combination_rule,
            "cofinal_interaction_bound": joint_corner_certified,
        }
    total_lowers = {
        low_level: max(
            0.0,
            band.lower[f"P{low_level}/amplified_closure_total"]
            - total_numerical_upper[low_level],
        )
        for low_level in low_levels
    }
    total_uppers = {
        low_level: (
            max(0.0, band.upper[f"P{low_level}/amplified_closure_total"])
            + total_numerical_upper[low_level]
        )
        for low_level in low_levels
    }
    per_level_resolved = {
        level: (
            total_uppers[level] <= allocation
            and total_numerical_upper[level] <= numerics_allocation
            and total_lowers[level] > 0.0
            and total_numerical_upper[level] < 0.2 * total_lowers[level]
            and joint_corner_certified
        )
        for level in low_levels
    }
    if any(value > allocation for value in total_lowers.values()):
        status = GateStatus.FAIL
        reasons = ["AMPLIFIED_CLOSURE_EXCEEDS_ALLOCATION"]
    elif any(
        total_numerical_upper[level] > numerics_allocation
        or total_lowers[level] <= 0.0
        or total_numerical_upper[level] >= 0.2 * total_lowers[level]
        for level in low_levels
    ):
        status = GateStatus.UNRESOLVED
        reasons = ["AMPLIFICATION_STRUCTURAL_NUMERICS_UNRESOLVED"]
    elif any(value > allocation for value in total_uppers.values()):
        status = GateStatus.UNRESOLVED
        reasons = ["AMPLIFIED_CLOSURE_BOUND_UNRESOLVED"]
    else:
        status = GateStatus.PASS
        reasons = ["AMPLIFIED_RESIDUAL_SUBSPACE_BOUND_PASSES"]
    axis_only_diagnostic_status = status
    axis_only_diagnostic_reasons = list(reasons)
    if not joint_corner_certified:
        status = GateStatus.UNRESOLVED
        reasons = [
            "AMPLIFICATION_STRUCTURAL_NUMERICS_NO_COFINAL_JOINT_CORNER",
            "AMPLIFICATION_AXIS_SUM_IS_EMPIRICAL_NOT_INTERACTION_CERTIFICATE",
        ]
        if axis_only_diagnostic_status == GateStatus.FAIL:
            reasons.append(
                "AMPLIFICATION_AXIS_ONLY_DIAGNOSTIC_EXCEEDS_ALLOCATION"
            )
    if status != GateStatus.FAIL:
        status = GateStatus.UNRESOLVED
        reasons = [
            *reasons,
            "AMPLIFICATION_NONLINEAR_IMPULSE_DIAGNOSTIC_ONLY",
            (
                "AMPLIFICATION_CERTIFICATE_SCOPED_TO_FINITE_P70_DICTIONARY"
                if _conditional_p70
                else "AMPLIFICATION_CERTIFICATE_SCOPED_TO_FINITE_P35_DICTIONARY"
            ),
            (
                "AMPLIFICATION_P70_NUMERICS_UNRESOLVED_NO_LEDGER_BOUND"
                if _conditional_p70
                else "AMPLIFIED_CLOSURE_LEDGER_REQUIRES_P35_FROM_P70"
            ),
        ]
    reasons = [
        *reasons,
        "AMPLIFICATION_FOUR_SCRAMBLE_BOOTSTRAP_DIAGNOSTIC_ONLY",
    ]
    rows: list[Mapping[str, Any]] = []
    for low_level in low_levels:
        for suffix in (
            "primary/gain",
            "refined/gain",
            "refined/residual_integral",
            "refined/linear_amplified",
            "refined/reconstruction",
            "refined/nonlinear_remainder",
            "source_time_discretization",
            "amplified_closure_total",
        ):
            key = f"P{low_level}/{suffix}"
            rows.append(
                {
                    "stage": (
                        "amplification_conditional_P70"
                        if _conditional_p70
                        else "amplification"
                    ),
                    "metric": key,
                    "point": band.point[key],
                    "lower": max(0.0, band.lower[key]),
                    "upper": max(0.0, band.upper[key]),
                    "semantics": (
                        "finite residual-subspace gain/error term; no full-state gain"
                    ),
                }
            )
    return (
        {
            "gate": _gate(
                status,
                *reasons,
                metrics={
                    "allocation": allocation,
                    "full_state_gain_computed": False,
                    "nonlinear_impulse_certificate": False,
                    "maximum_dictionary_level": expected_high_level,
                    "conditional_P70_look": _conditional_p70,
                    "non_double_counting": "outgoing residual excluded",
                    "axis_only_diagnostic_status": (
                        axis_only_diagnostic_status.value
                    ),
                    "axis_only_diagnostic_reason_codes": (
                        axis_only_diagnostic_reasons
                    ),
                },
            ),
            "metrics": {
                "confidence": confidence,
                "bootstrap_replicates": replicates,
                "critical_lower": band.critical_lower,
                "critical_upper": band.critical_upper,
                "bootstrap_calibration": _bootstrap_calibration_metadata(
                    band
                ),
                "point": band.point,
                "lower": {key: max(0.0, value) for key, value in band.lower.items()},
                "upper": {key: max(0.0, value) for key, value in band.upper.items()},
                "numerical_bounds": numerical_bounds,
                "numerical_combination_rule": (
                    "direct_primary_to_joint_corner"
                    if joint_corner_certified
                    else "conservative_empirical_axis_sum"
                ),
                "cofinal_joint_corner_certificate": (
                    joint_corner_certified
                ),
                "total_with_numerics_lower": total_lowers,
                "total_with_numerics_upper": total_uppers,
                "inference_scope": {
                    "root_count": len(seeds),
                    "finite_sample_coverage_claimed": False,
                    "ledger_admissible": False,
                    "semantics": "four-scramble diagnostic bootstrap",
                },
            },
            "missing": [],
            # Active P5/P15 are trend/trigger measurements.  Conditional P35
            # still needs a certified geometric ratio before it can enter the
            # P35-to-infinity ledger.
            "component_upper_bound": None,
            "active_trigger_upper_bounds": total_uppers,
            "P70_trigger_P15_upper_bound": (
                None if _conditional_p70 else total_uppers.get(15)
            ),
            "P70_trigger_state": (
                "AMPLIFIED_P15_READY"
                if (
                    not _conditional_p70
                    and per_level_resolved.get(15, False)
                )
                else "NOT_READY"
            ),
            "conditional_P70_family_complete": _conditional_p70,
            "conditional_numerical_resolution_certified": (
                bool(per_level_resolved.get(35, False))
                if _conditional_p70
                else False
            ),
            "A35_point": (
                band.point.get("P35/amplified_closure_total")
                if _conditional_p70
                else None
            ),
            "A35_lower": (
                total_lowers.get(35) if _conditional_p70 else None
            ),
            "A35_upper": (
                total_uppers.get(35) if _conditional_p70 else None
            ),
        },
        rows,
    )


def _post_active_tail_accounting(
    block_uppers: Sequence[float],
    *,
    post_active_indices: Sequence[int],
    q_upper: float,
) -> Mapping[str, float]:
    """Account for measured post-active motion plus the future remainder."""

    values = tuple(float(value) for value in block_uppers)
    indices = tuple(int(index) for index in post_active_indices)
    if not indices:
        raise ValueError("no post-active blocks were supplied")
    if any(index < 0 or index >= len(values) for index in indices):
        raise ValueError("post-active block index is out of range")
    if any(not np.isfinite(value) or value < 0.0 for value in values):
        raise ValueError("tail block bounds must be finite/nonnegative")
    q = float(q_upper)
    if not np.isfinite(q) or q < 0.0 or q >= 1.0:
        raise ValueError("tail contraction ratio must lie in [0,1)")
    measured = float(sum(values[index] for index in indices))
    last_upper = values[indices[-1]]
    future = float(q * last_upper / (1.0 - q))
    return {
        "measured_post_active_upper_sum": measured,
        "future_beyond_maximum_horizon_upper": future,
        "total_post_active_upper": measured + future,
    }


def analyze_stage6_tail(
    context: AnalysisContext,
) -> tuple[Mapping[str, Any], list[Mapping[str, Any]]]:
    pde_items = _stage_evidence(context, "tail_pde")
    dense_items = _stage_evidence(context, "tail_dense")
    if not pde_items and not dense_items:
        return _unresolved_missing("all_time_tail"), []
    protocol = context.protocol
    stage = protocol["stage_6_all_time_tail"]
    seeds = tuple(
        int(value)
        for value in protocol["stage_0_integrity_and_numerics"][
            "nested_ladder"
        ]["scramble_seeds"]
    )
    dense_roots = int(stage["dense_diagnostic"]["roots"])
    boundaries = _tail_boundaries(protocol)
    boundary_by_end = {end: start for start, end in boundaries}
    pde: dict[tuple[int, float], LoadedEvidence] = {}
    for item in pde_items:
        config = item.archive.metadata["config"]
        try:
            key = (int(config["seed"]), float(config["block_end"]))
        except (KeyError, TypeError, ValueError) as exc:
            raise AnalysisError(f"malformed PDE-tail config: {item.path}") from exc
        if key[0] not in seeds or key[1] not in boundary_by_end:
            raise AnalysisError(
                f"undeclared PDE-tail seed/block endpoint: {item.path}"
            )
        if key in pde:
            raise AnalysisError(f"duplicate PDE-tail block: {key}")
        pde[key] = item
    dense: dict[int, LoadedEvidence] = {}
    for item in dense_items:
        config = item.archive.metadata["config"]
        try:
            root = int(config["root_index"])
        except (KeyError, TypeError, ValueError) as exc:
            raise AnalysisError(f"malformed dense-tail config: {item.path}") from exc
        if not 0 <= root < dense_roots:
            raise AnalysisError(
                f"undeclared dense-tail root index: {item.path}"
            )
        _require_exact_config(
            item,
            _expected_tail_dense_config(
                protocol, root_index=root
            ),
            label="dense-tail",
        )
        if root in dense:
            raise AnalysisError(f"duplicate dense-tail root: {root}")
        dense[root] = item
    missing: list[str] = []
    for seed_value in seeds:
        previous_seal: str | None = None
        for start, end in boundaries:
            item = pde.get((seed_value, end))
            if item is None:
                missing.append(f"tail_pde/seed{seed_value}/end{end:g}")
                continue
            _validate_tail_pde_archive(
                protocol,
                item,
                seed=seed_value,
                block_start=start,
                block_end=end,
                restart_seal_sha256=previous_seal,
            )
            previous_seal = str(item.archive.metadata["seal_sha256"])
    absent_dense = sorted(set(range(dense_roots)) - set(dense))
    if absent_dense:
        missing.append(f"tail_dense/root_indices={absent_dense}")
    if missing:
        return (
            {
                "gate": _gate(
                    GateStatus.UNRESOLVED,
                    "TAIL_PREREGISTERED_INVENTORY_INCOMPLETE",
                ),
                "metrics": {},
                "missing": missing,
            },
            [],
        )

    pde_arc = np.empty((len(seeds), len(boundaries)))
    pde_variation = np.empty_like(pde_arc)
    for seed_index, seed_value in enumerate(seeds):
        for block_index, (_start, end) in enumerate(boundaries):
            arrays = pde[(seed_value, end)].archive.arrays
            for key in (
                "block_arclength",
                "block_normalized_observable_total_variation",
            ):
                if key not in arrays or np.asarray(arrays[key]).shape != ():
                    raise AnalysisError(f"PDE-tail scalar missing: {key}")
            pde_arc[seed_index, block_index] = float(arrays["block_arclength"])
            pde_variation[seed_index, block_index] = float(
                arrays["block_normalized_observable_total_variation"]
            )
    dense_arc = []
    dense_variation = []
    dense_theta = []
    dense_expected_blocks = tuple(
        pair for pair in boundaries if pair[1] <= stage["dense_diagnostic"]["maximum_horizon"]
    )
    for root in range(dense_roots):
        arrays = dense[root].archive.arrays
        for key in (
            "block_starts",
            "block_ends",
            "block_arclength",
            "block_normalized_observable_total_variation",
            "block_theta_min",
        ):
            if key not in arrays:
                raise AnalysisError(f"dense-tail archive missing {key}")
        if not np.array_equal(
            np.asarray(arrays["block_starts"], dtype=float),
            np.asarray([pair[0] for pair in dense_expected_blocks]),
        ) or not np.array_equal(
            np.asarray(arrays["block_ends"], dtype=float),
            np.asarray([pair[1] for pair in dense_expected_blocks]),
        ):
            raise AnalysisError("dense-tail block grid mismatch")
        dense_arc.append(np.asarray(arrays["block_arclength"], dtype=float))
        dense_variation.append(
            np.asarray(
                arrays["block_normalized_observable_total_variation"],
                dtype=float,
            )
        )
        dense_theta.append(np.asarray(arrays["block_theta_min"], dtype=float))
    dense_arc_array = np.stack(dense_arc)
    dense_variation_array = np.stack(dense_variation)
    dense_theta_array = np.stack(dense_theta)

    def statistic(indices_by_group: Mapping[str, Array]) -> Mapping[str, float]:
        result: dict[str, float] = {}
        pde_indices = indices_by_group["pde"]
        dense_indices = indices_by_group["dense"]
        pde_arc_mean = np.mean(pde_arc[pde_indices], axis=0)
        pde_variation_mean = np.mean(pde_variation[pde_indices], axis=0)
        dense_arc_mean = np.mean(dense_arc_array[dense_indices], axis=0)
        dense_variation_mean = np.mean(
            dense_variation_array[dense_indices], axis=0
        )
        dense_theta_mean = np.mean(dense_theta_array[dense_indices], axis=0)
        for index, (_start, end) in enumerate(boundaries):
            result[f"pde/arclength/end{end:g}"] = float(pde_arc_mean[index])
            result[f"pde/observable_total_variation/end{end:g}"] = float(
                pde_variation_mean[index]
            )
        for index, (_start, end) in enumerate(dense_expected_blocks):
            result[f"dense/arclength/end{end:g}"] = float(dense_arc_mean[index])
            result[f"dense/observable_total_variation/end{end:g}"] = float(
                dense_variation_mean[index]
            )
            result[f"dense/theta_min/end{end:g}"] = float(
                dense_theta_mean[index]
            )
        for system, arc_values, variation_values in (
            ("pde", pde_arc_mean, pde_variation_mean),
            ("dense", dense_arc_mean, dense_variation_mean),
        ):
            for index in range(len(arc_values) - 1):
                result[f"{system}/arclength_ratio/{index}"] = min(
                    arc_values[index + 1] / max(arc_values[index], 1e-300),
                    1e6,
                )
                result[
                    f"{system}/observable_total_variation_ratio/{index}"
                ] = min(
                    variation_values[index + 1]
                    / max(variation_values[index], 1e-300),
                    1e6,
                )
        return result

    (
        replicates,
        pilot_replicates,
        seed,
        confidence,
        mc_failure_probability,
    ) = _analysis_constants(context)
    band = _grouped_familywise_bootstrap(
        root_counts={"pde": len(seeds), "dense": dense_roots},
        statistic=statistic,
        replicates=replicates,
        pilot_replicates=pilot_replicates,
        seed=seed + 606,
        confidence=confidence,
        mc_failure_probability=mc_failure_probability,
    )
    failures: list[str] = []
    unresolved: list[str] = []
    active_horizon = float(
        protocol["stage_0_integrity_and_numerics"]["active_horizon"]
    )
    tail_accounting: dict[str, Mapping[str, float | None]] = {}
    for system, block_grid in (
        ("pde", boundaries),
        ("dense", dense_expected_blocks),
    ):
        count = len(block_grid)
        block_uppers = [
            max(
                0.0,
                band.upper[
                    f"{system}/observable_total_variation/end{end:g}"
                ],
            )
            for _start, end in block_grid
        ]
        post_active_indices = [
            index
            for index, (start, _end) in enumerate(block_grid)
            if start >= active_horizon
        ]
        measured_post_active = float(
            sum(block_uppers[index] for index in post_active_indices)
        )
        ratio_keys = [
            f"{system}/observable_total_variation_ratio/{index}"
            for index in range(count - 1)
        ]
        last_three = ratio_keys[-3:]
        if len(last_three) < 3:
            unresolved.append("TAIL_TOO_FEW_CONSECUTIVE_BLOCKS")
            tail_accounting[system] = {
                "measured_post_active_upper_sum": measured_post_active,
                "future_beyond_maximum_horizon_upper": None,
                "total_post_active_upper": None,
                "q_upper": None,
            }
            continue
        q_upper = max(band.upper[key] for key in last_three)
        if q_upper >= 1.0:
            if all(band.lower[key] >= 1.0 for key in last_three):
                failures.append("TAIL_OBSERVABLE_DRIFT_NONCONTRACTING")
            else:
                unresolved.append("TAIL_GEOMETRIC_ENVELOPE_UNRESOLVED")
            tail_accounting[system] = {
                "measured_post_active_upper_sum": measured_post_active,
                "future_beyond_maximum_horizon_upper": None,
                "total_post_active_upper": None,
                "q_upper": q_upper,
            }
            continue
        accounting = dict(
            _post_active_tail_accounting(
                block_uppers,
                post_active_indices=post_active_indices,
                q_upper=q_upper,
            )
        )
        accounting["q_upper"] = q_upper
        tail_accounting[system] = accounting
    allocation = float(
        protocol["error_ledger"]["preallocated_components"][
            "training_time_tail_conditional"
        ]
    )
    pde_total = tail_accounting.get("pde", {}).get(
        "total_post_active_upper"
    )
    pde_measured = tail_accounting.get("pde", {}).get(
        "measured_post_active_upper_sum"
    )
    if (
        (pde_total is not None and pde_total > allocation)
        or (pde_measured is not None and pde_measured > allocation)
    ):
        failures.append("TAIL_OBSERVABLE_BOUND_EXCEEDS_ALLOCATION")
    # A shrinking state arclength cannot be converted to an observable bound
    # without the separately measured late-time gain.
    unresolved.append("TAIL_LATE_TIME_PERTURBATION_GAIN_MISSING")
    unresolved.append("TAIL_ARCLENGTH_NOT_CONVERTED_TO_OBSERVABLE_BOUND")
    unresolved.append("TAIL_FLATNESS_IS_NOT_A_STABILITY_CERTIFICATE")
    unresolved.append("TAIL_FLAT_FLOOR_REFINEMENTS_MISSING")
    if failures:
        status = GateStatus.FAIL
        reasons = failures
    else:
        status = GateStatus.UNRESOLVED
        reasons = unresolved
    rows: list[Mapping[str, Any]] = []
    for system, block_grid in (
        ("pde", boundaries),
        ("dense", dense_expected_blocks),
    ):
        for _start, end in block_grid:
            for metric in ("arclength", "observable_total_variation"):
                key = f"{system}/{metric}/end{end:g}"
                rows.append(
                    {
                        "stage": "all_time_tail",
                        "metric": key,
                        "point": band.point[key],
                        "lower": max(0.0, band.lower[key]),
                        "upper": max(0.0, band.upper[key]),
                        "semantics": (
                            "state arclength; not compared directly to 0.005"
                            if metric == "arclength"
                            else "conservative sampled normalized block total variation"
                        ),
                    }
                )
    return (
        {
            "gate": _gate(
                status,
                *reasons,
                metrics={
                    "finite_horizon_only": True,
                    "arclength_separate_from_observable_allocation": True,
                },
            ),
            "metrics": {
                "confidence": confidence,
                "bootstrap_replicates": replicates,
                "critical_lower": band.critical_lower,
                "critical_upper": band.critical_upper,
                "bootstrap_calibration": _bootstrap_calibration_metadata(
                    band
                ),
                "inference_scope": {
                    "pde_root_count": len(seeds),
                    "dense_root_count": dense_roots,
                    "finite_sample_coverage_claimed": False,
                    "ledger_admissible": False,
                    "semantics": "four-root grouped diagnostic bootstrap",
                },
                "conditional_observable_tail_accounting": tail_accounting,
                "conditional_observable_tail_bounds": {
                    system: values.get("total_post_active_upper")
                    for system, values in tail_accounting.items()
                },
                "active_horizon": active_horizon,
                "allocation": allocation,
                "PDE_maximum_horizon": boundaries[-1][1],
                "dense_maximum_horizon": dense_expected_blocks[-1][1],
            },
            "missing": ["late-time residual-subspace restart gain"],
            "component_bound": (
                pde_total
                if status == GateStatus.PASS
                else None
            ),
            "diagnostic_component_bound": pde_total,
        },
        rows,
    )


def _motion_distance(
    left: tuple[Array, Array],
    right: tuple[Array, Array],
    *,
    floor: float = 0.05,
) -> tuple[float, float, float]:
    left_f = left[0] - left[0][0]
    right_f = right[0] - right[0][0]
    left_g = left[1] - left[1][0]
    right_g = right[1] - right[1][0]
    f_scale = max(
        floor,
        float(np.max(np.linalg.norm(left_f, axis=-1))),
        float(np.max(np.linalg.norm(right_f, axis=-1))),
    )
    g_scale = max(
        floor,
        float(np.max(np.linalg.norm(left_g, axis=(-2, -1)))),
        float(np.max(np.linalg.norm(right_g, axis=(-2, -1)))),
    )
    return (
        _metric_distance(
            left_f,
            left_g,
            right_f,
            right_g,
            s_f=f_scale,
            s_g=g_scale,
        ),
        f_scale,
        g_scale,
    )


def _finite_identification_gate(
    *,
    tier: str,
    lower: float | None,
    upper: float | None,
    margin: float = 0.05,
) -> Mapping[str, Any]:
    if tier != "positive":
        return _gate(
            GateStatus.UNRESOLVED,
            "TRIANGLE_POSITIVE_ORDERED_GRID_MISSING",
        )
    if lower is None or upper is None:
        return _gate(
            GateStatus.UNRESOLVED,
            "IDENTIFICATION_P35_BOUND_MISSING",
        )
    if float(lower) >= margin:
        return _gate(
            GateStatus.FAIL,
            "IDENTIFICATION_P35_DENSE_GAP_EXCEEDS_FIVE_PERCENT",
            metrics={"P35_lower": lower, "P35_upper": upper},
        )
    if float(upper) >= margin:
        return _gate(
            GateStatus.UNRESOLVED,
            "IDENTIFICATION_P35_FIVE_PERCENT_EQUIVALENCE_UNRESOLVED",
            metrics={"P35_lower": lower, "P35_upper": upper},
        )
    return _gate(
        GateStatus.PASS,
        "IDENTIFICATION_P35_FINITE_HORIZON_WITHIN_FIVE_PERCENT",
        metrics={"P35_upper": upper},
    )


def analyze_triangle_validation(
    context: AnalysisContext,
    stage0: Mapping[str, Any],
    stage1: Mapping[str, Any],
) -> tuple[Mapping[str, Any], list[Mapping[str, Any]]]:
    """Gate finite-horizon PDE identification against the ordered dense center."""

    numerics = _stage_evidence(context, "numerics")
    scaling = _stage_evidence(context, "scaling")
    if not numerics or not scaling:
        return (
            {
                "gate": _gate(
                    GateStatus.UNRESOLVED,
                    "TRIANGLE_VALIDATION_INPUT_MISSING",
                ),
                "comparisons": {},
                "ledger_semantics": "identification_gate_not_additive",
            },
            [],
        )
    protocol = context.protocol
    s_f = float(protocol["norms"]["S_f"])
    s_g = float(protocol["norms"]["S_G"])
    horizon = float(protocol["stage_0_integrity_and_numerics"]["active_horizon"])
    times = np.arange(
        0.0,
        horizon + 1e-12,
        float(protocol["norms"]["time_sampling"]),
    )
    times[-1] = horizon
    depths = np.linspace(0.0, 1.0, 17)
    seeds = tuple(
        int(value)
        for value in protocol["stage_0_integrity_and_numerics"][
            "nested_ladder"
        ]["scramble_seeds"]
    )
    levels = tuple(
        int(value)
        for value in protocol["stage_0_integrity_and_numerics"][
            "nested_ladder"
        ]["active_levels_before_conditional_extension"]
    )
    primary_ladder = protocol["stage_0_integrity_and_numerics"][
        "nested_ladder"
    ]
    pde: dict[tuple[int, int], ObservableCurve] = {}
    for item in numerics:
        config = item.archive.config
        if (
            int(config["base_order"])
            == int(primary_ladder["primary_base_order"])
            and int(config["N"]) == int(primary_ladder["primary_N"])
            and int(config["R"]) == int(primary_ladder["primary_R"])
            and float(config["dt"])
            == float(primary_ladder["primary_dt"])
        ):
            key = (int(config["P"]), int(config["seed"]))
            if key in pde:
                raise AnalysisError(f"duplicate primary PDE curve: {key}")
            pde[key] = _curve_to_grid(
                _curve_from_numerics(item), times=times, depths=depths
            )
    required_pde = {(P, seed) for P in levels for seed in seeds}
    if not required_pde.issubset(pde):
        return (
            {
                "gate": _gate(
                    GateStatus.UNRESOLVED,
                    "TRIANGLE_PRIMARY_PDE_CURVES_INCOMPLETE",
                ),
                "comparisons": {},
                "ledger_semantics": "identification_gate_not_additive",
            },
            [],
        )

    tier_items: dict[str, dict[int, dict[tuple[int, int], tuple[Array, Array]]]] = {
        "screen": {},
        "positive": {},
    }
    tier_grids: dict[str, tuple[tuple[int, ...], tuple[int, ...]]] = {}
    for item in scaling:
        tier = str(item.archive.config.get("tier"))
        root, widths, physical_depths, table = _scaling_root_archive(item)
        if tier not in tier_items:
            raise AnalysisError(f"unknown scaling tier: {tier}")
        tier_items[tier][root] = table
        tier_grids[tier] = (widths, physical_depths)
    positive_count = int(
        protocol["stage_1_ordered_target"]["positive_grid"]["coupled_roots"]
    )
    screen_count = int(
        protocol["stage_1_ordered_target"]["screen_grid"]["coupled_roots"]
    )
    if set(tier_items["positive"]) == set(range(positive_count)):
        tier = "positive"
        root_table = tier_items[tier]
    elif set(tier_items["screen"]) == set(range(screen_count)):
        tier = "screen"
        root_table = tier_items[tier]
    else:
        return (
            {
                "gate": _gate(
                    GateStatus.UNRESOLVED,
                    "TRIANGLE_DENSE_CENTER_INCOMPLETE",
                ),
                "comparisons": {},
                "ledger_semantics": "identification_gate_not_additive",
            },
            [],
        )
    widths, physical_depths = tier_grids[tier]
    finest_key = (widths[-1], physical_depths[-1])
    dense_center = (
        np.mean(
            np.stack(
                [root_table[root][finest_key][0] for root in sorted(root_table)]
            ),
            axis=0,
        ),
        np.mean(
            np.stack(
                [root_table[root][finest_key][1] for root in sorted(root_table)]
            ),
            axis=0,
        ),
    )
    target_depths = np.linspace(0.0, 1.0, dense_center[1].shape[1])
    pde = {
        key: _curve_to_grid(curve, times=times, depths=target_depths)
        for key, curve in pde.items()
    }
    numerics_bound = stage0.get("component_upper_bound")
    diagnostic_numerics_by_p = stage0.get(
        "diagnostic_component_upper_bound_by_P", {}
    )
    component_bounds = stage1.get("component_bounds", {})
    ingredients = {
        "PDE_numerics": numerics_bound,
        "dense_sampling": component_bounds.get("dense_sampling"),
        "width_tail_conditional": component_bounds.get("width_tail_conditional"),
        "depth_tail_conditional": component_bounds.get("depth_tail_conditional"),
    }
    valid_bounds = all(
        value is not None and np.isfinite(float(value)) and float(value) >= 0.0
        for value in ingredients.values()
    )
    radius = (
        float(sum(float(value) for value in ingredients.values()))
        if valid_bounds
        else None
    )
    common_diagnostic_ingredients = {
        "dense_sampling": component_bounds.get("dense_sampling"),
        "width_tail_conditional": component_bounds.get("width_tail_conditional"),
        "depth_tail_conditional": component_bounds.get("depth_tail_conditional"),
    }
    common_diagnostic_valid = all(
        value is not None and np.isfinite(float(value)) and float(value) >= 0.0
        for value in common_diagnostic_ingredients.values()
    )
    diagnostic_radius_by_p: dict[int, float | None] = {}
    for P in levels:
        diagnostic_numerics = diagnostic_numerics_by_p.get(
            P, diagnostic_numerics_by_p.get(str(P))
        )
        diagnostic_radius_by_p[P] = (
            float(diagnostic_numerics)
            + sum(
                float(value)
                for value in common_diagnostic_ingredients.values()
            )
            if (
                common_diagnostic_valid
                and diagnostic_numerics is not None
                and np.isfinite(float(diagnostic_numerics))
                and float(diagnostic_numerics) >= 0.0
            )
            else None
        )
    comparisons: dict[str, Any] = {}
    rows: list[Mapping[str, Any]] = []
    for P in levels:
        pde_center = (
            np.mean(np.stack([pde[(P, seed)].f for seed in seeds]), axis=0),
            np.mean(np.stack([pde[(P, seed)].gram for seed in seeds]), axis=0),
        )
        absolute = _curve_distance_from_arrays(
            pde_center, dense_center, s_f=s_f, s_g=s_g
        )
        motion, motion_f_scale, motion_g_scale = _motion_distance(
            pde_center, dense_center
        )
        motion_radius = (
            radius
            * max(
                s_f / motion_f_scale,
                s_g / motion_g_scale,
            )
            if radius is not None
            else None
        )
        diagnostic_radius = diagnostic_radius_by_p[P]
        diagnostic_motion_radius = (
            diagnostic_radius
            * max(
                s_f / motion_f_scale,
                s_g / motion_g_scale,
            )
            if diagnostic_radius is not None
            else None
        )
        comparisons[f"P{P}"] = {
            "absolute": {
                "point": absolute,
                "lower_triangle_bound": (
                    max(0.0, absolute - radius) if radius is not None else None
                ),
                "upper_triangle_bound": (
                    absolute + radius if radius is not None else None
                ),
                "diagnostic_lower_triangle_bound": (
                    max(0.0, absolute - diagnostic_radius)
                    if diagnostic_radius is not None
                    else None
                ),
                "diagnostic_upper_triangle_bound": (
                    absolute + diagnostic_radius
                    if diagnostic_radius is not None
                    else None
                ),
            },
            "initialization_subtracted_motion": {
                "point": motion,
                "lower_triangle_bound": (
                    max(0.0, motion - motion_radius)
                    if motion_radius is not None
                    else None
                ),
                "upper_triangle_bound": (
                    motion + motion_radius
                    if motion_radius is not None
                    else None
                ),
                "output_scale": motion_f_scale,
                "gram_scale": motion_g_scale,
                "converted_triangle_radius": motion_radius,
                "diagnostic_lower_triangle_bound": (
                    max(0.0, motion - diagnostic_motion_radius)
                    if diagnostic_motion_radius is not None
                    else None
                ),
                "diagnostic_upper_triangle_bound": (
                    motion + diagnostic_motion_radius
                    if diagnostic_motion_radius is not None
                    else None
                ),
                "diagnostic_converted_triangle_radius": (
                    diagnostic_motion_radius
                ),
            },
        }
        for mode, point in (("absolute", absolute), ("motion", motion)):
            rows.append(
                {
                    "stage": "triangle_validation",
                    "metric": f"P{P}/{mode}",
                    "point": point,
                    "lower": (
                        max(
                            0.0,
                            point
                            - (
                                radius
                                if mode == "absolute"
                                else motion_radius
                            ),
                        )
                        if radius is not None
                        else ""
                    ),
                    "upper": (
                        point
                        + (
                            radius
                            if mode == "absolute"
                            else motion_radius
                        )
                        if radius is not None
                        else ""
                    ),
                    "semantics": (
                        "PDE mean vs finest dense mean; identification gate; "
                        "triangle bound adds numerical/sampling/tail balls"
                    ),
                }
            )
            diagnostic_mode_radius = (
                diagnostic_radius
                if mode == "absolute"
                else diagnostic_motion_radius
            )
            rows.append(
                {
                    "stage": "triangle_validation",
                    "metric": f"P{P}/{mode}/diagnostic",
                    "point": point,
                    "lower": (
                        max(0.0, point - diagnostic_mode_radius)
                        if diagnostic_mode_radius is not None
                        else ""
                    ),
                    "upper": (
                        point + diagnostic_mode_radius
                        if diagnostic_mode_radius is not None
                        else ""
                    ),
                    "semantics": (
                        "diagnostic triangle only; includes direct "
                        "primary-to-joint correction but no certified "
                        "cofinal PDE remainder"
                    ),
                }
            )
    if radius is None:
        gate = _gate(
            GateStatus.UNRESOLVED,
            "TRIANGLE_CERTIFIED_PDE_NUMERICS_REMAINDER_MISSING",
        )
    else:
        p35 = comparisons.get("P35", {}).get("absolute", {})
        gate = _finite_identification_gate(
            tier=tier,
            lower=p35.get("lower_triangle_bound"),
            upper=p35.get("upper_triangle_bound"),
        )
    return (
        {
            "gate": gate,
            "dense_center": {
                "tier": tier,
                "n": widths[-1],
                "L": physical_depths[-1],
            },
            "triangle_radius": radius,
            "triangle_ingredients": ingredients,
            "diagnostic_triangle_radius_by_P": diagnostic_radius_by_p,
            "diagnostic_triangle_ingredients": {
                "PDE_numerics_by_P": diagnostic_numerics_by_p,
                **common_diagnostic_ingredients,
            },
            "comparisons": comparisons,
            "ledger_semantics": (
                "finite-horizon identification gate; central gap is not "
                "double-added to the mechanistic error ledger; diagnostic "
                "triangle bounds are not certified without a cofinal PDE "
                "numerical remainder"
            ),
        },
        rows,
    )


def _archive_inventory(context: AnalysisContext) -> list[Mapping[str, Any]]:
    return [
        {
            "path": str(item.path.relative_to(context.audit_root)),
            "stage": item.stage,
            "config_sha256": item.archive.metadata["config_sha256"],
            "stage_seal_sha256": item.archive.metadata["seal_sha256"],
            "file_sha256": item.file_sha256,
            "array_count": len(item.archive.arrays),
            "array_hash_inventory_sha256": _sha256_bytes(
                _canonical_json_bytes(item.archive.metadata["array_hashes"])
            ),
        }
        for item in context.evidence
    ]


def _overall_gate(stages: Mapping[str, Mapping[str, Any]]) -> Mapping[str, Any]:
    statuses = [
        GateStatus(value["gate"]["status"])
        for value in stages.values()
    ]
    if GateStatus.FAIL in statuses:
        return _gate(
            GateStatus.FAIL,
            "ONE_OR_MORE_PROOF_OBLIGATIONS_FAILED",
        )
    if GateStatus.UNRESOLVED in statuses:
        return _gate(
            GateStatus.UNRESOLVED,
            "ONE_OR_MORE_PROOF_OBLIGATIONS_UNRESOLVED",
        )
    return _gate(
        GateStatus.PASS,
        "ALL_MEASURED_PROOF_OBLIGATIONS_PASS",
    )


def _p70_state_machine(
    *,
    p70_present: bool,
    base_trigger_ready: bool,
    p15_amplification_ready: bool,
) -> str:
    if not p70_present:
        return (
            "READY_NOT_RUN"
            if base_trigger_ready and p15_amplification_ready
            else "NOT_AUTHORIZED"
        )
    if base_trigger_ready and p15_amplification_ready:
        return "AUTHORIZED_EVALUATE"
    return "DENIED_PROTOCOL_VIOLATION"


def _combine_overall_with_ledger(
    stages: Mapping[str, Mapping[str, Any]],
    ledger_gate: Mapping[str, Any],
) -> Mapping[str, Any]:
    stage_gate = _overall_gate(stages)
    statuses = {
        GateStatus(stage_gate["status"]),
        GateStatus(ledger_gate["status"]),
    }
    if GateStatus.FAIL in statuses:
        return _gate(
            GateStatus.FAIL,
            "PROOF_OBLIGATION_OR_ERROR_LEDGER_FAILED",
        )
    if GateStatus.UNRESOLVED in statuses:
        return _gate(
            GateStatus.UNRESOLVED,
            "PROOF_OBLIGATION_OR_ERROR_LEDGER_UNRESOLVED",
        )
    return _gate(
        GateStatus.PASS,
        "ALL_PROOF_OBLIGATIONS_AND_ERROR_LEDGER_PASS",
    )


def _csv_bytes(rows: Sequence[Mapping[str, Any]], fields: Sequence[str]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(
        buffer,
        fieldnames=list(fields),
        extrasaction="ignore",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow({field: _jsonable(row.get(field, "")) for field in fields})
    return buffer.getvalue().encode("utf-8")


def _atomic_write(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_name(path.name + ".partial")
    if partial.exists():
        raise AnalysisError(f"stale processed partial blocks write: {partial}")
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".partial",
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        directory_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        if temporary.exists():
            temporary.unlink()


def analyze_all(
    context: AnalysisContext,
) -> tuple[Mapping[str, Any], Mapping[str, bytes]]:
    """Analyze every available stage and build deterministic output bytes."""

    stage_results: dict[str, Mapping[str, Any]] = {}
    metric_rows: list[Mapping[str, Any]] = []
    analyzers = (
        ("stage_0_numerics", analyze_stage0_numerics),
        ("stage_1_ordered_target", analyze_stage1_scaling),
        ("stage_2_homogenization", analyze_stage2_homogenization),
        ("stage_3_same_state_attack", analyze_stage3_attack),
        ("stage_4_generator_consistency", analyze_stage4_generator),
        ("stage_5_amplification", analyze_stage5_gain),
        ("stage_6_all_time_tail", analyze_stage6_tail),
    )
    for label, analyzer in analyzers:
        result, rows = analyzer(context)
        stage_results[label] = result
        metric_rows.extend(rows)

    stage4 = stage_results["stage_4_generator_consistency"]
    stage5 = stage_results["stage_5_amplification"]
    p70_generator_present = any(
        item.stage == "generator"
        and int(item.archive.config.get("max_level", -1)) == 70
        for item in context.evidence
    )
    p70_numerics_present = any(
        item.stage == "numerics"
        and int(item.archive.config.get("P", -1)) == 70
        for item in context.evidence
    )
    p70_gain_present = any(
        item.stage == "amplification"
        and int(item.archive.config.get("low_level", -1)) == 35
        and int(item.archive.config.get("high_level", -1)) == 70
        for item in context.evidence
    )
    p70_any_present = (
        p70_generator_present
        or p70_numerics_present
        or p70_gain_present
    )
    p70_gain_declared = isinstance(
        context.protocol.get("stage_5_amplification", {}).get(
            "conditional_P70_extension"
        ),
        Mapping,
    )
    base_trigger_gate = stage4.get("base_trigger_gate")
    base_trigger_ready = (
        stage4.get("trigger_state") == "TRIGGER_READY"
        or (
            isinstance(base_trigger_gate, Mapping)
            and "GENERATOR_P70_EXTENSION_REQUIRED"
            in base_trigger_gate.get("reason_codes", ())
        )
    )
    gain_trigger_ready = (
        stage5.get("P70_trigger_state") == "AMPLIFIED_P15_READY"
    )
    p70_state = _p70_state_machine(
        p70_present=p70_any_present,
        base_trigger_ready=base_trigger_ready,
        p15_amplification_ready=gain_trigger_ready,
    )
    if p70_numerics_present and p70_state == "DENIED_PROTOCOL_VIOLATION":
        stage0 = stage_results["stage_0_numerics"]
        stage_results["stage_0_numerics"] = {
            **stage0,
            "gate": _gate(
                GateStatus.FAIL,
                *stage0["gate"]["reason_codes"],
                "NUMERICS_P70_WITHOUT_FROZEN_BASE_AND_GAIN_AUTHORIZATION",
                metrics=stage0["gate"].get("metrics", {}),
            ),
            "P70_authorization": {
                "base_trigger_ready": base_trigger_ready,
                "P15_amplification_ready": gain_trigger_ready,
                "authorized": False,
                "state": p70_state,
            },
        }
    p70_gain_complete = False
    p70_gain_numerically_certified = False
    p70_amplification_envelope: Mapping[str, Any] | None = None
    if p70_gain_present and not p70_gain_declared:
        stage5 = stage_results["stage_5_amplification"]
        stage_results["stage_5_amplification"] = {
            **stage5,
            "gate": _gate(
                GateStatus.FAIL,
                *stage5["gate"]["reason_codes"],
                "AMPLIFICATION_P70_WITHOUT_FROZEN_PROTOCOL_DECLARATION",
                metrics=stage5["gate"].get("metrics", {}),
            ),
        }
    elif p70_gain_present and p70_state == "DENIED_PROTOCOL_VIOLATION":
        stage5 = stage_results["stage_5_amplification"]
        stage_results["stage_5_amplification"] = {
            **stage5,
            "gate": _gate(
                GateStatus.FAIL,
                *stage5["gate"]["reason_codes"],
                "AMPLIFICATION_P70_WITHOUT_FROZEN_BASE_AND_GAIN_AUTHORIZATION",
                metrics=stage5["gate"].get("metrics", {}),
            ),
            "P70_authorization": {
                "base_trigger_ready": base_trigger_ready,
                "P15_amplification_ready": gain_trigger_ready,
                "authorized": False,
                "state": p70_state,
            },
        }
    elif p70_gain_present:
        active_stage5 = stage_results["stage_5_amplification"]
        conditional_stage5, conditional_rows = analyze_stage5_gain(
            context, _conditional_p70=True
        )
        metric_rows.extend(conditional_rows)
        p70_gain_complete = bool(
            conditional_stage5.get(
                "conditional_P70_family_complete", False
            )
        )
        p70_gain_numerically_certified = bool(
            conditional_stage5.get(
                "conditional_numerical_resolution_certified", False
            )
        )
        if p70_gain_complete:
            active_metrics = active_stage5["metrics"]
            p70_amplification_envelope = (
                _conditional_geometric_amplification(
                    A15_point=float(
                        active_metrics["point"][
                            "P15/amplified_closure_total"
                        ]
                    ),
                    A15_lower=float(
                        active_metrics["total_with_numerics_lower"][15]
                    ),
                    A15_upper=float(
                        active_metrics["total_with_numerics_upper"][15]
                    ),
                    A35_point=float(conditional_stage5["A35_point"]),
                    A35_lower=float(conditional_stage5["A35_lower"]),
                    A35_upper=float(conditional_stage5["A35_upper"]),
                    conditional_numerical_resolution_certified=(
                        p70_gain_numerically_certified
                    ),
                )
            )
            metric_rows.extend(
                [
                    {
                        "stage": "amplification_conditional_P70",
                        "metric": "A35_with_numerics",
                        "point": p70_amplification_envelope["A35_point"],
                        "lower": p70_amplification_envelope["A35_lower"],
                        "upper": p70_amplification_envelope["A35_upper"],
                        "semantics": (
                            "P35-from-P70 finite-dictionary amplified "
                            "closure quantity"
                        ),
                    },
                    {
                        "stage": "amplification_conditional_P70",
                        "metric": "A35_over_active_A15_ratio",
                        "point": p70_amplification_envelope["ratio_point"],
                        "lower": p70_amplification_envelope["ratio_lower"],
                        "upper": p70_amplification_envelope["ratio_upper"],
                        "semantics": (
                            "conditional contraction ratio; an upper bound "
                            "below one is required for a geometric candidate"
                        ),
                    },
                ]
            )
            if (
                p70_amplification_envelope[
                    "candidate_P35_to_infinity_upper"
                ]
                is not None
            ):
                metric_rows.append(
                    {
                        "stage": "amplification_conditional_P70",
                        "metric": "candidate_P35_to_infinity",
                        "point": p70_amplification_envelope[
                            "candidate_P35_to_infinity_point"
                        ],
                        "lower": "",
                        "upper": p70_amplification_envelope[
                            "candidate_P35_to_infinity_upper"
                        ],
                        "semantics": (
                            "geometric candidate only; ledger-admissible "
                            "only with certified conditional numerics"
                        ),
                    }
                )
        active_reasons = [
            reason
            for reason in active_stage5["gate"]["reason_codes"]
            if (
                not p70_gain_complete
                or reason
                != "AMPLIFIED_CLOSURE_LEDGER_REQUIRES_P35_FROM_P70"
            )
        ]
        conditional_reasons = list(
            conditional_stage5["gate"]["reason_codes"]
        )
        combined_reasons = list(
            dict.fromkeys([*active_reasons, *conditional_reasons])
        )
        active_status = GateStatus(active_stage5["gate"]["status"])
        conditional_status = GateStatus(
            conditional_stage5["gate"]["status"]
        )
        combined_status = (
            GateStatus.FAIL
            if GateStatus.FAIL in (active_status, conditional_status)
            else GateStatus.UNRESOLVED
        )
        component_bound = (
            p70_amplification_envelope[
                "ledger_component_upper_bound"
            ]
            if p70_amplification_envelope is not None
            else None
        )
        stage_results["stage_5_amplification"] = {
            **active_stage5,
            "gate": _gate(
                combined_status,
                *combined_reasons,
                metrics={
                    **active_stage5["gate"].get("metrics", {}),
                    "conditional_P70_family_complete": p70_gain_complete,
                    "conditional_P70_numerically_certified": (
                        p70_gain_numerically_certified
                    ),
                },
            ),
            "conditional_P70": conditional_stage5,
            "conditional_P70_family_complete": p70_gain_complete,
            "conditional_P70_metrics": p70_amplification_envelope,
            "component_upper_bound": component_bound,
            "P70_authorization": {
                "base_trigger_ready": True,
                "P15_amplification_ready": True,
                "authorized": True,
                "state": p70_state,
            },
        }
    if p70_generator_present:
        if p70_state == "DENIED_PROTOCOL_VIOLATION":
            stage4 = {
                **stage4,
                "gate": _gate(
                    GateStatus.FAIL,
                    *stage4["gate"]["reason_codes"],
                    "GENERATOR_P70_WITHOUT_FROZEN_BASE_AND_GAIN_AUTHORIZATION",
                ),
                "P70_authorization": {
                    "base_trigger_ready": base_trigger_ready,
                    "P15_amplification_ready": gain_trigger_ready,
                    "authorized": False,
                    "state": p70_state,
                },
            }
        else:
            remaining = [
                reason
                for reason in stage4["gate"]["reason_codes"]
                if reason
                not in {
                    "GENERATOR_P70_TRIGGER_REQUIRES_STAGE5",
                    (
                        "GENERATOR_P35_TO_P70_"
                        "AMPLIFICATION_CERTIFICATE_MISSING"
                    ),
                }
            ]
            if p70_gain_complete:
                remaining.append(
                    (
                        "GENERATOR_P35_TO_P70_AMPLIFICATION_ANALYZED_"
                        + (
                            "AND_NUMERICALLY_CERTIFIED"
                            if p70_gain_numerically_certified
                            else "BUT_NUMERICALLY_UNRESOLVED"
                        )
                    )
                )
            else:
                remaining.append(
                    "GENERATOR_P35_TO_P70_AMPLIFICATION_CERTIFICATE_MISSING"
                )
            current_status = GateStatus(stage4["gate"]["status"])
            reconciled_gate = _gate(
                (
                    GateStatus.FAIL
                    if current_status == GateStatus.FAIL
                    else GateStatus.UNRESOLVED
                ),
                *remaining,
                metrics=stage4["gate"].get("metrics", {}),
            )
            stage4 = {
                **stage4,
                "gate": reconciled_gate,
                "trigger_state": "P70_AUTHORIZED_AND_EVALUATED",
                "P70_authorization": {
                    "base_trigger_ready": True,
                    "P15_amplification_ready": True,
                    "authorized": True,
                    "state": p70_state,
                },
                "P35_to_P70_amplification_complete": p70_gain_complete,
                "P35_to_P70_amplification_numerically_certified": (
                    p70_gain_numerically_certified
                ),
            }
        stage_results["stage_4_generator_consistency"] = stage4

    triangle_validation, triangle_rows = analyze_triangle_validation(
        context,
        stage_results["stage_0_numerics"],
        stage_results["stage_1_ordered_target"],
    )
    metric_rows.extend(triangle_rows)

    allocations = {
        str(key): float(value)
        for key, value in context.protocol["error_ledger"][
            "preallocated_components"
        ].items()
    }
    bounds: dict[str, float] = {}
    stage0_bound = stage_results["stage_0_numerics"].get(
        "component_upper_bound"
    )
    if stage0_bound is not None:
        bounds["PDE_numerics"] = float(stage0_bound)
    stage1_bounds = stage_results["stage_1_ordered_target"].get(
        "component_bounds", {}
    )
    for key in (
        "dense_sampling",
        "width_tail_conditional",
        "depth_tail_conditional",
    ):
        value = stage1_bounds.get(key)
        if value is not None:
            bounds[key] = float(value)
    stage5_bound = stage_results["stage_5_amplification"].get(
        "component_upper_bound"
    )
    if stage5_bound is not None:
        bounds["amplified_closure"] = float(stage5_bound)
    stage6_bound = stage_results["stage_6_all_time_tail"].get(
        "component_bound"
    )
    if stage6_bound is not None:
        bounds["training_time_tail_conditional"] = float(stage6_bound)
    ledger = aggregate_error_ledger(
        bounds,
        allocations=allocations,
        target_total=float(
            context.protocol["error_ledger"]["target_total_fraction"]
        ),
        conditional_validity={
            "width_tail_conditional": (
                stage1_bounds.get("width_tail_conditional") is not None
            ),
            "depth_tail_conditional": (
                stage1_bounds.get("depth_tail_conditional") is not None
            ),
            "training_time_tail_conditional": (
                stage_results["stage_6_all_time_tail"]["gate"]["status"]
                == GateStatus.PASS.value
            ),
        },
    )
    ledger_summary = {
        "gate": ledger.gate.to_dict(),
        "bounds": ledger.bounds,
        "allocations": ledger.allocations,
        "total_bound": (
            ledger.total_bound
            if np.isfinite(ledger.total_bound)
            else None
        ),
        "target_total": ledger.target_total,
        "margins": ledger.margins,
        "conditional_components": ledger.conditional_components,
        "excluded": [
            "same-state attack gaps",
            "outgoing residual when back residual represents the same projection error",
            "P15 amplification used only for the P70 trigger",
        ],
    }

    inventory = _archive_inventory(context)
    overall_stages = {
        **stage_results,
        "finite_horizon_identification": triangle_validation,
    }
    gates_rows = [
        {
            "stage": stage,
            "status": result["gate"]["status"],
            "reason_codes": "|".join(result["gate"]["reason_codes"]),
        }
        for stage, result in overall_stages.items()
    ]
    inventory_bytes = _csv_bytes(
        inventory,
        (
            "path",
            "stage",
            "config_sha256",
            "stage_seal_sha256",
            "file_sha256",
            "array_count",
            "array_hash_inventory_sha256",
        ),
    )
    gates_bytes = _csv_bytes(
        gates_rows, ("stage", "status", "reason_codes")
    )
    metrics_bytes = _csv_bytes(
        metric_rows,
        ("stage", "metric", "point", "lower", "upper", "semantics"),
    )
    csv_payloads = {
        "gates.csv": gates_bytes,
        "metrics.csv": metrics_bytes,
        "archive_inventory.csv": inventory_bytes,
    }
    summary: dict[str, Any] = {
        "schema_version": 1,
        "analysis_identity": {
            "protocol_sha256": context.protocol_sha256,
            "frozen_inputs_sha256": context.frozen_inputs_sha256,
            "analyzer_source_sha256": _sha256_file(Path(__file__).resolve()),
            "bootstrap_replicates": int(
                context.protocol["error_ledger"]["bootstrap_replicates"]
            ),
            "bootstrap_pilot_replicates": int(
                context.protocol["error_ledger"][
                    "bootstrap_pilot_replicates"
                ]
            ),
            "bootstrap_mc_failure_probability_per_call": float(
                context.protocol["error_ledger"][
                    "bootstrap_mc_failure_probability_per_call"
                ]
            ),
            "data_alpha_total": float(
                context.protocol["error_ledger"]["data_alpha_total"]
            ),
            "bootstrap_mc_failure_total": float(
                context.protocol["error_ledger"][
                    "bootstrap_mc_failure_total"
                ]
            ),
            "finite_sample_coverage_claimed": False,
            "bootstrap_seed": int(
                context.protocol["error_ledger"]["bootstrap_seed"]
            ),
            "stage_family_confidence": float(
                context.protocol["error_ledger"]["stage_family_confidence"]
            ),
            "two_look_family_confidence": float(
                context.protocol["error_ledger"][
                    "two_look_family_confidence"
                ]
            ),
            "three_look_family_confidence": float(
                context.protocol["error_ledger"][
                    "three_look_family_confidence"
                ]
            ),
            "independent_stochastic_families": int(
                context.protocol["error_ledger"][
                    "independent_stochastic_families"
                ]
            ),
            "threshold_source": "frozen preregistered protocol only",
            "scientific_trajectory_execution": False,
        },
        "archive_count": len(inventory),
        "archive_inventory": inventory,
        "stage_results": stage_results,
        "finite_horizon_identification": triangle_validation,
        "triangle_validation": triangle_validation,
        "error_ledger": ledger_summary,
        "overall_gate": _combine_overall_with_ledger(
            overall_stages, ledger_summary["gate"]
        ),
        "processed_payload_sha256": {
            name: _sha256_bytes(payload) for name, payload in csv_payloads.items()
        },
        "interpretive_limits": [
            "The 0.95 multiplicity target is conditional on the stated "
            "nonparametric-bootstrap approximation; no exact finite-sample "
            "coverage is claimed. Four-root/scramble families are "
            "diagnostic and cannot supply certified ledger components.",
            "Stage-0 reports a direct primary-mean-shift plus "
            "primary-to-joint diagnostic radius, but no certified PDE "
            "numerical component because no second cofinal remainder was "
            "computed.",
            "Conditional geometric tails are norm balls around the finest "
            "observed curves, not synthetic directional extrapolations.",
            "Finite-P homogenization reconstruction/projection residuals are "
            "diagnostics and do not certify the actual conditional/Onsager "
            "mean.",
            "Active P<=35 Stage-4/5 structural numerics use the executed "
            "direct primary-to-joint correction as their cofinal nuisance "
            "bound; their four one-axis corrections are diagnostics. The "
            "conditional P70 family has no joint corner, so its axis-sum is "
            "only an empirical sensitivity envelope and its numerical gate "
            "remains UNRESOLVED.",
            "Invisible-attack gaps are falsification diagnostics and are not "
            "added to the approximation-error ledger.",
            "A missing stage or incomplete preregistered job inventory is "
            "UNRESOLVED, never PASS.",
        ],
    }
    payloads = dict(csv_payloads)
    payloads["summary.json"] = _canonical_json_bytes(summary) + b"\n"
    return summary, payloads


def write_processed(
    context: AnalysisContext,
    payloads: Mapping[str, bytes],
) -> Mapping[str, str]:
    hashes: dict[str, str] = {}
    for name in ("gates.csv", "metrics.csv", "archive_inventory.csv", "summary.json"):
        if name not in payloads:
            raise AnalysisError(f"missing processed payload: {name}")
        path = context.processed_root / name
        _atomic_write(path, payloads[name])
        hashes[name] = _sha256_file(path)
    return hashes


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analyze sealed PDE proof-obligation archives."
    )
    parser.add_argument(
        "--audit-root",
        type=Path,
        default=AUDIT_ROOT,
    )
    parser.add_argument(
        "--no-write",
        action="store_true",
        help="validate and analyze without writing processed outputs",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    context = discover_evidence(audit_root=args.audit_root)
    summary, payloads = analyze_all(context)
    output_hashes: Mapping[str, str] = {}
    if not args.no_write:
        output_hashes = write_processed(context, payloads)
    print(
        json.dumps(
            {
                "status": "analyzed",
                "overall_gate": summary["overall_gate"],
                "archive_count": summary["archive_count"],
                "processed_sha256": output_hashes,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
