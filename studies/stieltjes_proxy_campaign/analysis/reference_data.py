"""Strict ingestion and lineage-aware finite-width curve estimators."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np


COMPLETE_STATUSES = {"complete_scientific_point", "complete_validation_only"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


@dataclass(frozen=True)
class ReferencePoint:
    """One immutable finite-width point plus its raw pair-lineage arrays."""

    point_id: str
    group: str
    mode: str
    width: int
    antithetic_pairs: int
    target: float
    family_key: str | None
    family_parameters: tuple[tuple[str, str], ...]
    config: Mapping[str, Any]
    diagnostics: Mapping[str, Any]
    arrays: Mapping[str, np.ndarray]
    evidence_admissible: bool
    arrays_path: Path
    arrays_sha256: str

    @property
    def output_nodes(self) -> np.ndarray:
        return np.asarray(self.arrays["output_nodes"], dtype=np.float64)


@dataclass(frozen=True)
class ReferenceRun:
    summary_path: Path
    config_path: Path
    status: str
    evidence_admissible: bool
    points: tuple[ReferencePoint, ...]
    summary: Mapping[str, Any]
    config: Mapping[str, Any]


def _load_npz(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as archive:
        return {name: np.array(archive[name], copy=True) for name in archive.files}


def _analysis_metadata(point: Mapping[str, Any]) -> tuple[str, str | None, tuple[tuple[str, str], ...]]:
    analysis = point.get("analysis", {})
    if analysis is None:
        analysis = {}
    if not isinstance(analysis, Mapping):
        raise ValueError("point analysis metadata must be an object")
    group = str(
        analysis.get(
            "comparison_group",
            point.get("comparison_group", point["id"]),
        )
    )
    family_key_raw = analysis.get("family_key", point.get("family_key"))
    family_key = None if family_key_raw is None else str(family_key_raw)
    parameters_raw = analysis.get("family_parameters", point.get("family_parameters", {}))
    if not isinstance(parameters_raw, Mapping):
        raise ValueError("family_parameters must be an object")
    parameters = tuple(sorted((str(key), str(value)) for key, value in parameters_raw.items()))
    return group, family_key, parameters


def _validate_raw_arrays(point: Mapping[str, Any], arrays: Mapping[str, np.ndarray]) -> None:
    required_common = {"output_nodes", "raw_trajectory_output", "raw_trajectory_kernel"}
    missing = sorted(required_common - arrays.keys())
    if missing:
        raise ValueError(f"{point['id']} is missing raw arrays {missing}")
    raw_output = np.asarray(arrays["raw_trajectory_output"])
    raw_kernel = np.asarray(arrays["raw_trajectory_kernel"])
    if raw_output.ndim != 2 or raw_kernel.shape != raw_output.shape:
        raise ValueError("raw output and kernel arrays must have the same 2D shape")
    expected_trajectories = 2 * int(point["antithetic_pairs"])
    if raw_output.shape[1] != expected_trajectories:
        raise ValueError(
            f"expected {expected_trajectories} adjacent antithetic trajectories, "
            f"found {raw_output.shape[1]}"
        )
    nodes = np.asarray(arrays["output_nodes"], dtype=np.float64)
    if nodes.ndim != 1 or len(nodes) < 2 or np.any(np.diff(nodes) <= 0.0):
        raise ValueError("output_nodes must be a strictly increasing 1D grid")
    if not np.all(np.isfinite(raw_output)) or not np.all(np.isfinite(raw_kernel)):
        raise ValueError("reference raw arrays contain nonfinite values")
    mode = str(point["mode"])
    if mode == "physical":
        required = {"raw_time", "raw_trajectory_weighted_kernel", "raw_trajectory_loss"}
    elif mode == "output_clock":
        required = {"raw_output_clock", "raw_trajectory_loss"}
    else:
        raise ValueError(f"unknown reference mode {mode!r}")
    missing = sorted(required - arrays.keys())
    if missing:
        raise ValueError(f"{point['id']} is missing mode-specific raw arrays {missing}")


def load_reference_run(
    summary_path: str | Path,
    *,
    config_path: str | Path | None = None,
    verify_hashes: bool = True,
    require_scientific: bool = False,
) -> ReferenceRun:
    """Load one explicitly named run and verify every completed NPZ artifact.

    Validation-only runs can exercise the implementation, but setting
    ``require_scientific=True`` rejects them before any analysis is performed.
    """

    summary_path = Path(summary_path).resolve()
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    admissible = bool(summary.get("scientific_evidence_admissible", False))
    if require_scientific and not admissible:
        raise PermissionError("the supplied run is not admissible scientific evidence")
    if config_path is None:
        reference_root = summary_path.parent.parent.parent
        config_path = reference_root / "configs" / str(summary["config_name"])
    config_path = Path(config_path).resolve()
    config = json.loads(config_path.read_text(encoding="utf-8"))
    config_by_id = {str(point["id"]): point for point in config["points"]}
    if len(config_by_id) != len(config["points"]):
        raise ValueError("configuration point ids are not unique")

    points: list[ReferencePoint] = []
    for record in summary.get("points", []):
        point_id = str(record["id"])
        if record.get("status") not in COMPLETE_STATUSES:
            continue
        try:
            point_config = config_by_id[point_id]
        except KeyError as exc:
            raise ValueError(f"summary point {point_id!r} is absent from configuration") from exc
        array_path = summary_path.parent / str(record["arrays_file"])
        actual_hash = sha256(array_path)
        expected_hash = str(record["arrays_sha256"])
        if verify_hashes and actual_hash != expected_hash:
            raise ValueError(f"NPZ hash mismatch for {point_id}")
        arrays = _load_npz(array_path)
        _validate_raw_arrays(point_config, arrays)
        group, family_key, parameters = _analysis_metadata(point_config)
        points.append(ReferencePoint(
            point_id=point_id,
            group=group,
            mode=str(point_config["mode"]),
            width=int(point_config["width"]),
            antithetic_pairs=int(point_config["antithetic_pairs"]),
            target=float(point_config.get("target", 1.0)),
            family_key=family_key,
            family_parameters=parameters,
            config=point_config,
            diagnostics=record.get("diagnostics", {}),
            arrays=arrays,
            evidence_admissible=admissible,
            arrays_path=array_path,
            arrays_sha256=actual_hash,
        ))
    return ReferenceRun(
        summary_path=summary_path,
        config_path=config_path,
        status=str(summary.get("status", "unknown")),
        evidence_admissible=admissible,
        points=tuple(points),
        summary=summary,
        config=config,
    )


def pair_average(values: np.ndarray) -> np.ndarray:
    """Average adjacent antithetic members without losing the pair axis."""

    values = np.asarray(values, dtype=np.float64)
    if values.ndim != 2 or values.shape[1] % 2:
        raise ValueError("pair averaging requires a 2D array with an even final axis")
    return values.reshape(values.shape[0], values.shape[1] // 2, 2).mean(axis=2)


def _strict_interpolation_grid(x: np.ndarray, tolerance: float) -> tuple[np.ndarray, np.ndarray]:
    increments = np.diff(x)
    if float(np.min(increments)) < -tolerance:
        raise FloatingPointError("resampled ensemble output is nonmonotone")
    keep = np.concatenate(([True], increments > 0.0))
    if np.count_nonzero(keep) < 2:
        raise FloatingPointError("resampled output grid is degenerate")
    return x[keep], keep


def estimate_curve(
    point: ReferencePoint,
    *,
    output_nodes: Sequence[float] | np.ndarray | None = None,
    pair_indices: Sequence[int] | np.ndarray | None = None,
) -> dict[str, np.ndarray]:
    """Estimate a curve after resampling whole antithetic pair lineages.

    In physical mode, mean output is recomputed for the resample and inverted
    before the ratio defining ``K_eff`` is formed.  This is intentionally not
    a resample of the already aggregated pointwise ratio.
    """

    nodes = point.output_nodes if output_nodes is None else np.asarray(output_nodes, dtype=np.float64)
    if nodes.ndim != 1 or np.any(np.diff(nodes) <= 0.0):
        raise ValueError("analysis output nodes must be strictly increasing")
    pairs = point.antithetic_pairs
    if pair_indices is None:
        indices = np.arange(pairs, dtype=np.int64)
    else:
        indices = np.asarray(pair_indices, dtype=np.int64)
        if indices.ndim != 1 or len(indices) != pairs:
            raise ValueError("a lineage bootstrap must draw exactly the original pair count")
        if np.any(indices < 0) or np.any(indices >= pairs):
            raise IndexError("pair bootstrap index is outside the lineage range")

    pair_output = pair_average(point.arrays["raw_trajectory_output"])[:, indices]
    pair_kernel = pair_average(point.arrays["raw_trajectory_kernel"])[:, indices]
    mean_output = pair_output.mean(axis=1)
    mean_kernel = pair_kernel.mean(axis=1)
    tolerance = float(point.config.get("monotonic_tolerance", 1e-10))

    if point.mode == "physical":
        pair_weighted = pair_average(point.arrays["raw_trajectory_weighted_kernel"])[:, indices]
        pair_loss = pair_average(point.arrays["raw_trajectory_loss"])[:, indices]
        x, keep = _strict_interpolation_grid(mean_output, tolerance)
        if nodes[0] < x[0] - tolerance or nodes[-1] > x[-1] + tolerance:
            raise FloatingPointError("resampled physical trajectory does not span the common output grid")
        time = np.asarray(point.arrays["raw_time"], dtype=np.float64)[keep]
        numerator = pair_weighted.mean(axis=1)[keep]
        direct = mean_kernel[keep]
        mean_loss = pair_loss.mean(axis=1)[keep]
        denominator = point.target - nodes
        if np.any(denominator <= 0.0):
            raise FloatingPointError("physical K_eff is undefined at or beyond target")
        return {
            "output": nodes,
            "kernel": np.interp(nodes, x, numerator) / denominator,
            "direct_kernel": np.interp(nodes, x, direct),
            "mean_loss": np.interp(nodes, x, mean_loss),
            "loss_of_mean_output": np.square(denominator),
            "physical_time": np.interp(nodes, x, time),
        }

    coordinate = np.asarray(point.arrays["raw_output_clock"], dtype=np.float64)
    if nodes[0] < coordinate[0] or nodes[-1] > coordinate[-1]:
        raise FloatingPointError("output-clock reference does not span the common grid")
    pair_loss = pair_average(point.arrays["raw_trajectory_loss"])[:, indices]
    mean_loss = pair_loss.mean(axis=1)
    return {
        "output": nodes,
        "kernel": np.interp(nodes, coordinate, mean_kernel),
        "direct_kernel": np.interp(nodes, coordinate, mean_kernel),
        "mean_loss": np.interp(nodes, coordinate, mean_loss),
        "loss_of_mean_output": np.square(point.target - nodes),
    }


def pair_level_node_kernel(point: ReferencePoint) -> np.ndarray:
    """Return a diagnostic pair-level kernel on the stored node-time grid."""

    if point.mode == "output_clock":
        if "node_pair_kernel" in point.arrays:
            return np.asarray(point.arrays["node_pair_kernel"], dtype=np.float64)
        coordinate = np.asarray(point.arrays["raw_output_clock"], dtype=np.float64)
        paired = pair_average(point.arrays["raw_trajectory_kernel"])
        return np.vstack([
            np.interp(point.output_nodes, coordinate, paired[:, j])
            for j in range(paired.shape[1])
        ]).T

    if {"node_pair_output", "node_pair_weighted_kernel"} <= point.arrays.keys():
        pair_output = np.asarray(point.arrays["node_pair_output"], dtype=np.float64)
        pair_weighted = np.asarray(point.arrays["node_pair_weighted_kernel"], dtype=np.float64)
        denominator = point.target - pair_output
        result = np.full_like(pair_weighted, np.nan)
        np.divide(pair_weighted, denominator, out=result, where=denominator > 0.0)
        return result
    raise ValueError("physical point lacks stored pair-level node arrays")
