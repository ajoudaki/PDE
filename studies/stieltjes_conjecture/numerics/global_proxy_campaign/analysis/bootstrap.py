"""Pair-lineage bootstrap and finite-width diagnostic summaries."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

import numpy as np

from .reference_data import ReferencePoint, estimate_curve, pair_level_node_kernel


MAX_BOOTSTRAPS = 20_000


@dataclass(frozen=True)
class BootstrapBand:
    """A studentized simultaneous confidence band on the log-kernel scale."""

    estimate: np.ndarray
    lower: np.ndarray
    upper: np.ndarray
    pointwise_log_standard_error: np.ndarray
    simultaneous_critical_value: float
    confidence: float
    valid_replicates: int
    attempted_replicates: int
    scale: str = "log"

    def record(self) -> dict[str, Any]:
        return {
            "estimate": self.estimate.tolist(),
            "lower": self.lower.tolist(),
            "upper": self.upper.tolist(),
            "pointwise_log_standard_error": self.pointwise_log_standard_error.tolist(),
            "simultaneous_critical_value": self.simultaneous_critical_value,
            "confidence": self.confidence,
            "valid_replicates": self.valid_replicates,
            "attempted_replicates": self.attempted_replicates,
            "scale": self.scale,
        }


@dataclass(frozen=True)
class PointBootstrap:
    point_id: str
    width: int
    output: np.ndarray
    band: BootstrapBand
    samples: np.ndarray
    diagnostics: Mapping[str, Any]

    def compact_record(self) -> dict[str, Any]:
        return {
            "point_id": self.point_id,
            "width": self.width,
            "output": self.output.tolist(),
            "band": self.band.record(),
            "diagnostics": dict(self.diagnostics),
        }


def simultaneous_log_band(
    estimate: Sequence[float] | np.ndarray,
    samples: np.ndarray,
    *,
    confidence: float,
) -> BootstrapBand:
    """Construct a max-|t| band using bootstrap log deviations.

    The bootstrap samples are centered on the original estimate.  Zero-noise
    coordinates contribute zero to the maximum when every resample agrees,
    and make the band fail closed if a nonzero deviation occurs with zero
    estimated scale.
    """

    estimate = np.asarray(estimate, dtype=np.float64)
    samples = np.asarray(samples, dtype=np.float64)
    if estimate.ndim != 1 or samples.ndim != 2 or samples.shape[1] != len(estimate):
        raise ValueError("estimate must be 1D and bootstrap samples B-by-grid")
    if not 0.5 < confidence < 1.0:
        raise ValueError("confidence must lie strictly between 0.5 and 1")
    if np.any(estimate <= 0.0) or np.any(samples <= 0.0):
        raise FloatingPointError("log-scale bootstrap requires positive kernels")
    log_estimate = np.log(estimate)
    log_samples = np.log(samples)
    standard_error = np.std(log_samples, axis=0, ddof=1)
    deviations = np.abs(log_samples - log_estimate[None, :])
    standardized = np.zeros_like(deviations)
    positive_scale = standard_error > 0.0
    standardized[:, positive_scale] = (
        deviations[:, positive_scale] / standard_error[positive_scale]
    )
    if np.any(~positive_scale):
        nonzero = deviations[:, ~positive_scale] > 8.0 * np.finfo(float).eps
        standardized[:, ~positive_scale] = np.where(nonzero, np.inf, 0.0)
    scores = np.max(standardized, axis=1)
    critical = float(np.quantile(scores, confidence, method="higher"))
    if not np.isfinite(critical):
        raise FloatingPointError("simultaneous bootstrap critical value is nonfinite")
    radius = critical * standard_error
    return BootstrapBand(
        estimate=estimate,
        lower=np.exp(log_estimate - radius),
        upper=np.exp(log_estimate + radius),
        pointwise_log_standard_error=standard_error,
        simultaneous_critical_value=critical,
        confidence=float(confidence),
        valid_replicates=int(samples.shape[0]),
        attempted_replicates=int(samples.shape[0]),
    )


def point_diagnostics(point: ReferencePoint, central: Mapping[str, np.ndarray]) -> dict[str, Any]:
    """Compute prespecified self-averaging, Jensen, and leakage diagnostics."""

    pair_kernel = pair_level_node_kernel(point)
    finite = np.isfinite(pair_kernel)
    finite_counts = finite.sum(axis=1)
    pair_mean = np.nanmean(pair_kernel, axis=1)
    pair_sd = np.nanstd(pair_kernel, axis=1, ddof=1)
    cv = np.divide(
        pair_sd,
        np.abs(pair_mean),
        out=np.full_like(pair_sd, np.inf),
        where=np.abs(pair_mean) > 0.0,
    )
    relative_se = np.divide(
        cv,
        np.sqrt(finite_counts),
        out=np.full_like(cv, np.inf),
        where=finite_counts > 0,
    )
    jensen_gap = np.asarray(central["mean_loss"]) - np.asarray(
        central["loss_of_mean_output"]
    )
    jensen_relative = np.divide(
        jensen_gap,
        np.asarray(central["mean_loss"]),
        out=np.zeros_like(jensen_gap),
        where=np.asarray(central["mean_loss"]) > 0.0,
    )
    leakage_keys = (
        "node_pair_transverse_leakage",
        "node_raw_transverse_leakage",
        "mean_transverse_leakage",
    )
    leakage_key = next((key for key in leakage_keys if key in point.arrays), None)
    if leakage_key is None:
        leakage: dict[str, Any] = {"applicable": False}
    else:
        values = np.asarray(point.arrays[leakage_key], dtype=np.float64)
        leakage = {
            "applicable": True,
            "source_key": leakage_key,
            "maximum_absolute": float(np.max(np.abs(values))),
            "rms": float(np.sqrt(np.mean(np.square(values)))),
        }
    return {
        "antithetic_pair_count": point.antithetic_pairs,
        "minimum_finite_pair_count_at_node": int(np.min(finite_counts)),
        "maximum_pair_kernel_cv": float(np.max(cv)),
        "maximum_relative_standard_error": float(np.max(relative_se)),
        "maximum_absolute_jensen_gap": float(np.max(np.abs(jensen_gap))),
        "maximum_relative_jensen_gap": float(np.max(np.abs(jensen_relative))),
        "maximum_output_variance_at_nodes": float(
            point.diagnostics.get("maximum_output_variance_at_nodes", np.nan)
        ),
        "leakage": leakage,
    }


def bootstrap_point(
    point: ReferencePoint,
    *,
    output_nodes: Sequence[float] | np.ndarray | None = None,
    replicates: int = 2_000,
    seed: int = 0,
    confidence: float = 0.95,
    minimum_valid_fraction: float = 0.95,
) -> PointBootstrap:
    """Bootstrap a finite-width kernel by resampling adjacent pair lineages."""

    if not 20 <= replicates <= MAX_BOOTSTRAPS:
        raise ValueError(f"replicates must lie in [20,{MAX_BOOTSTRAPS}]")
    if not 0.5 < minimum_valid_fraction <= 1.0:
        raise ValueError("minimum_valid_fraction must lie in (0.5,1]")
    nodes = point.output_nodes if output_nodes is None else np.asarray(output_nodes, dtype=np.float64)
    central = estimate_curve(point, output_nodes=nodes)
    estimate = np.asarray(central["kernel"], dtype=np.float64)
    if np.any(estimate <= 0.0) or not np.all(np.isfinite(estimate)):
        raise FloatingPointError("central reference kernel is not positive and finite")

    rng = np.random.default_rng(int(seed))
    samples: list[np.ndarray] = []
    invalid = 0
    for _ in range(int(replicates)):
        indices = rng.integers(0, point.antithetic_pairs, size=point.antithetic_pairs)
        try:
            curve = estimate_curve(point, output_nodes=nodes, pair_indices=indices)
            kernel = np.asarray(curve["kernel"], dtype=np.float64)
            if np.any(kernel <= 0.0) or not np.all(np.isfinite(kernel)):
                raise FloatingPointError("nonpositive bootstrap kernel")
            samples.append(kernel)
        except FloatingPointError:
            invalid += 1
    valid_fraction = len(samples) / replicates
    if valid_fraction < minimum_valid_fraction:
        raise FloatingPointError(
            f"only {len(samples)}/{replicates} bootstrap trajectories span the common grid"
        )
    sample_array = np.asarray(samples, dtype=np.float64)
    band = simultaneous_log_band(estimate, sample_array, confidence=confidence)
    band = BootstrapBand(
        estimate=band.estimate,
        lower=band.lower,
        upper=band.upper,
        pointwise_log_standard_error=band.pointwise_log_standard_error,
        simultaneous_critical_value=band.simultaneous_critical_value,
        confidence=band.confidence,
        valid_replicates=len(samples),
        attempted_replicates=replicates,
    )
    diagnostics = point_diagnostics(point, central)
    diagnostics.update({
        "bootstrap_seed": int(seed),
        "bootstrap_invalid_replicates": invalid,
        "bootstrap_valid_fraction": valid_fraction,
        "maximum_simultaneous_log_band_width": float(
            np.max(np.log(band.upper / band.lower))
        ),
    })
    return PointBootstrap(
        point_id=point.point_id,
        width=point.width,
        output=np.asarray(nodes, dtype=np.float64),
        band=band,
        samples=sample_array,
        diagnostics=diagnostics,
    )
