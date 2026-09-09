"""Prespecified width-limit fits and sensitivity diagnostics."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Literal, Sequence

import numpy as np

from .bootstrap import BootstrapBand, PointBootstrap, simultaneous_log_band


WidthModel = Literal[
    "inv_n_all",
    "inv_sqrt_n_all",
    "inv_n_leave_smallest",
    "inv_n_top3",
    "top_width_direct",
]


@dataclass(frozen=True)
class WidthEstimate:
    model: WidthModel
    widths_used: tuple[int, ...]
    output: np.ndarray
    band: BootstrapBand
    samples: np.ndarray
    maximum_relative_fit_residual: float

    def compact_record(self) -> dict[str, Any]:
        return {
            "model": self.model,
            "widths_used": list(self.widths_used),
            "output": self.output.tolist(),
            "band": self.band.record(),
            "maximum_relative_fit_residual": self.maximum_relative_fit_residual,
        }


@dataclass(frozen=True)
class UnionWidthReference:
    """Conservative union of all prespecified width-sensitivity bands."""

    primary_model: WidthModel
    component_models: tuple[WidthModel, ...]
    output: np.ndarray
    band: BootstrapBand

    def compact_record(self) -> dict[str, Any]:
        return {
            "primary_model": self.primary_model,
            "component_models": list(self.component_models),
            "output": self.output.tolist(),
            "band": self.band.record(),
        }


def _validate_points(points: Sequence[PointBootstrap]) -> tuple[PointBootstrap, ...]:
    points = tuple(sorted(points, key=lambda point: point.width))
    if len(points) < 2:
        raise ValueError("width extrapolation requires at least two widths")
    widths = [point.width for point in points]
    if len(set(widths)) != len(widths):
        raise ValueError("widths must be unique within an extrapolation group")
    first = points[0].output
    for point in points[1:]:
        if not np.array_equal(first, point.output):
            raise ValueError("all width points must use the identical output grid")
        if point.band.confidence != points[0].band.confidence:
            raise ValueError("all width bootstraps must use the same confidence")
    return points


def _fit_intercept(values: np.ndarray, x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Fit values[width,grid] = intercept[grid] + slope[grid] * x."""

    design = np.column_stack((np.ones(len(x)), x))
    coefficients = np.linalg.pinv(design) @ values
    fitted = design @ coefficients
    return coefficients[0], fitted


def _select(points: tuple[PointBootstrap, ...], model: WidthModel) -> tuple[PointBootstrap, ...]:
    if model == "inv_n_leave_smallest":
        return points[1:]
    if model == "inv_n_top3":
        if len(points) < 3:
            raise ValueError("inv_n_top3 requires at least three widths")
        return points[-3:]
    if model == "top_width_direct":
        return points[-1:]
    return points


def extrapolate_widths(
    points: Sequence[PointBootstrap],
    *,
    model: WidthModel,
) -> WidthEstimate:
    """Construct one frozen width-limit sensitivity estimate.

    Bootstrap draws are independent across widths but retain the complete
    antithetic pair lineage within each point.  The number of usable draws is
    the minimum available across widths; no resampling is fabricated to pad a
    smaller point.
    """

    all_points = _validate_points(points)
    chosen = _select(all_points, model)
    widths = np.asarray([point.width for point in chosen], dtype=np.float64)
    central_values = np.vstack([point.band.estimate for point in chosen])
    bootstrap_count = min(point.samples.shape[0] for point in chosen)
    confidence = chosen[0].band.confidence

    if model == "top_width_direct":
        central = central_values[-1]
        samples = chosen[-1].samples[:bootstrap_count]
        residual = 0.0
    else:
        if len(chosen) == 1:
            # With only two pilot widths, leave-smallest-out degenerates to the
            # top-width-only sensitivity.  The explicit top-width band is also
            # present in the eventual union, so this cannot narrow the result.
            central = central_values[0]
            samples = chosen[0].samples[:bootstrap_count]
            residual = 0.0
            band = simultaneous_log_band(central, samples, confidence=confidence)
            return WidthEstimate(
                model=model,
                widths_used=(int(widths[0]),),
                output=np.array(chosen[0].output, copy=True),
                band=band,
                samples=samples,
                maximum_relative_fit_residual=residual,
            )
        if model in {"inv_n_all", "inv_n_leave_smallest", "inv_n_top3"}:
            x = np.reciprocal(widths)
        elif model == "inv_sqrt_n_all":
            x = np.reciprocal(np.sqrt(widths))
        else:  # pragma: no cover - protected by the Literal and branches above
            raise ValueError(f"unknown width model {model!r}")
        central, fitted = _fit_intercept(central_values, x)
        residual = float(np.max(
            np.abs(fitted - central_values)
            / np.maximum(np.abs(central_values), np.finfo(float).tiny)
        ))
        sample_cube = np.stack(
            [point.samples[:bootstrap_count] for point in chosen], axis=1
        )  # bootstrap,width,grid
        design = np.column_stack((np.ones(len(x)), x))
        intercept_weights = np.linalg.pinv(design)[0]
        samples = np.einsum("w,bwg->bg", intercept_weights, sample_cube)

    valid = np.all(np.isfinite(samples) & (samples > 0.0), axis=1)
    samples = samples[valid]
    if len(samples) < max(20, int(0.95 * bootstrap_count)):
        raise FloatingPointError("too many width-extrapolated bootstrap curves are nonpositive")
    if np.any(central <= 0.0) or not np.all(np.isfinite(central)):
        raise FloatingPointError("width-extrapolated central kernel is nonpositive")
    band = simultaneous_log_band(central, samples, confidence=confidence)
    return WidthEstimate(
        model=model,
        widths_used=tuple(int(width) for width in widths),
        output=np.array(chosen[0].output, copy=True),
        band=band,
        samples=samples,
        maximum_relative_fit_residual=residual,
    )


def union_width_estimates(
    estimates: Sequence[WidthEstimate],
    *,
    primary_model: WidthModel = "inv_n_all",
) -> UnionWidthReference:
    """Take the nodewise union required by the frozen campaign protocol."""

    estimates = tuple(estimates)
    if not estimates:
        raise ValueError("at least one width estimate is required")
    by_model = {estimate.model: estimate for estimate in estimates}
    if len(by_model) != len(estimates):
        raise ValueError("width-union component models must be unique")
    try:
        primary = by_model[primary_model]
    except KeyError as exc:
        raise ValueError("primary model is absent from the sensitivity union") from exc
    for estimate in estimates[1:]:
        if not np.array_equal(primary.output, estimate.output):
            raise ValueError("width-union components use different output grids")
        if estimate.band.confidence != primary.band.confidence:
            raise ValueError("width-union components use different confidence levels")
    lower = np.min(np.vstack([estimate.band.lower for estimate in estimates]), axis=0)
    upper = np.max(np.vstack([estimate.band.upper for estimate in estimates]), axis=0)
    # The primary central estimator is retained for error summaries, while the
    # lower/upper curves are the full sensitivity union.  Samples are not
    # invented for this non-probabilistic outer envelope.
    band = BootstrapBand(
        estimate=np.array(primary.band.estimate, copy=True),
        lower=lower,
        upper=upper,
        pointwise_log_standard_error=np.array(
            primary.band.pointwise_log_standard_error, copy=True
        ),
        simultaneous_critical_value=primary.band.simultaneous_critical_value,
        confidence=primary.band.confidence,
        valid_replicates=primary.band.valid_replicates,
        attempted_replicates=primary.band.attempted_replicates,
        scale="log_bootstrap_plus_width_sensitivity_union",
    )
    return UnionWidthReference(
        primary_model=primary_model,
        component_models=tuple(estimate.model for estimate in estimates),
        output=np.array(primary.output, copy=True),
        band=band,
    )


def width_sensitivity_summary(estimates: Iterable[WidthEstimate]) -> dict[str, Any]:
    estimates = tuple(estimates)
    if len(estimates) < 2:
        raise ValueError("width sensitivity needs at least two estimators")
    grid = estimates[0].output
    for estimate in estimates[1:]:
        if not np.array_equal(grid, estimate.output):
            raise ValueError("width sensitivity estimators use different grids")
    maximum_log_disagreement = 0.0
    no_common_band_nodes = 0
    for i, left in enumerate(estimates):
        for right in estimates[i + 1 :]:
            maximum_log_disagreement = max(
                maximum_log_disagreement,
                float(np.max(np.abs(np.log(left.band.estimate / right.band.estimate)))),
            )
            overlap = np.maximum(left.band.lower, right.band.lower) <= np.minimum(
                left.band.upper, right.band.upper
            )
            no_common_band_nodes += int(np.count_nonzero(~overlap))
    return {
        "models": [estimate.model for estimate in estimates],
        "maximum_pairwise_log_disagreement": maximum_log_disagreement,
        "pair_node_comparisons_with_disjoint_bands": no_common_band_nodes,
    }


def self_averaging_width_summary(points: Sequence[PointBootstrap]) -> dict[str, Any]:
    """Fit the diagnostic decay of pair variance and estimator SE with width."""

    points = tuple(sorted(points, key=lambda point: point.width))
    if len(points) < 2:
        return {"available": False, "reason": "fewer than two widths"}
    widths = np.asarray([point.width for point in points], dtype=np.float64)
    relative_se = np.asarray([
        float(point.diagnostics["maximum_relative_standard_error"]) for point in points
    ])
    if np.any(~np.isfinite(relative_se)) or np.any(relative_se <= 0.0):
        return {"available": False, "reason": "nonpositive or nonfinite relative SE"}
    slope, intercept = np.polyfit(np.log(widths), np.log(relative_se), 1)
    return {
        "available": True,
        "widths": widths.astype(int).tolist(),
        "maximum_relative_standard_errors": relative_se.tolist(),
        "log_log_slope": float(slope),
        "log_log_intercept": float(intercept),
    }
