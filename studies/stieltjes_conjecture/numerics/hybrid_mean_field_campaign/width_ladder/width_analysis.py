#!/usr/bin/env python3
"""Frozen estimators and paired-width inference for the width ladder.

The key invariant is that every resampled K_eff estimate re-inverts the
resampled mean output curve.  Cross-fit control slopes are likewise re-estimated
inside every bootstrap replicate.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np

from nested_rng import exact_initial_component_means, exact_initial_total_mean


class AnalysisInvalid(RuntimeError):
    pass


POSITIVE_NODES = np.array([0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99])
INFERENTIAL_MASK = POSITIVE_NODES <= 0.9
WIDTHS = np.array([2048.0, 4096.0, 8192.0])


@dataclass(frozen=True)
class Estimate:
    raw_mean: np.ndarray
    raw_se: np.ndarray
    controlled_mean: np.ndarray
    raw_lineage: np.ndarray
    controlled_lineage: np.ndarray
    betas: np.ndarray


def _validate_dataset(data: dict[str, np.ndarray]) -> None:
    required = {
        "raw_time",
        "raw_output",
        "raw_kernel",
        "raw_weighted_kernel",
        "lineage_ids",
        "initial_components",
        "initial_total",
        "initial_state_sha256",
    }
    missing = required - set(data)
    if missing:
        raise AnalysisInvalid(f"dataset misses arrays {sorted(missing)}")
    ids = np.asarray(data["lineage_ids"], dtype=np.int64)
    if ids.ndim != 1 or len(np.unique(ids)) != len(ids):
        raise AnalysisInvalid("lineage ids are not a distinct vector")
    trajectory_count = data["raw_output"].shape[1]
    if trajectory_count != 2 * len(ids):
        raise AnalysisInvalid("raw trajectories do not match lineage count")
    shape = data["raw_output"].shape
    for key in ("raw_kernel", "raw_weighted_kernel"):
        if data[key].shape != shape:
            raise AnalysisInvalid(f"{key} shape differs from raw output")
    if data["initial_components"].shape != (len(ids), 3):
        raise AnalysisInvalid("initial component-control shape is wrong")
    if data["initial_total"].shape != (len(ids),):
        raise AnalysisInvalid("initial total-control shape is wrong")
    if data["initial_state_sha256"].shape != (len(ids),):
        raise AnalysisInvalid("initial-state digest shape is wrong")
    numeric_required = required - {"lineage_ids", "initial_state_sha256"}
    if not all(np.all(np.isfinite(data[key])) for key in numeric_required):
        raise AnalysisInvalid("nonfinite raw dataset")


def load_npz(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as archive:
        data = {key: archive[key] for key in archive.files}
    _validate_dataset(data)
    return data


def merge_shards(shards: Iterable[dict[str, np.ndarray]]) -> dict[str, np.ndarray]:
    pieces = list(shards)
    if not pieces:
        raise AnalysisInvalid("no shards supplied")
    for piece in pieces:
        _validate_dataset(piece)
    time = pieces[0]["raw_time"]
    for piece in pieces[1:]:
        if not np.array_equal(piece["raw_time"], time):
            raise AnalysisInvalid("shard time grids differ")
    ids = np.concatenate([piece["lineage_ids"] for piece in pieces])
    if len(np.unique(ids)) != len(ids):
        raise AnalysisInvalid("shards contain overlapping lineages")
    order = np.argsort(ids)
    if not np.array_equal(ids[order], np.arange(ids.min(), ids.max() + 1)):
        raise AnalysisInvalid("shards do not form a contiguous lineage set")

    # First concatenate pairs in shard order, then reorder whole adjacent pairs.
    pair_columns = np.concatenate(
        [
            np.arange(2 * len(piece["lineage_ids"]), dtype=np.int64).reshape(-1, 2)
            + 2 * sum(len(previous["lineage_ids"]) for previous in pieces[:index])
            for index, piece in enumerate(pieces)
        ],
        axis=0,
    )
    trajectory_order = pair_columns[order].reshape(-1)
    merged: dict[str, np.ndarray] = {
        "raw_time": time.copy(),
        "lineage_ids": ids[order],
        "initial_components": np.concatenate(
            [piece["initial_components"] for piece in pieces], axis=0
        )[order],
        "initial_total": np.concatenate(
            [piece["initial_total"] for piece in pieces], axis=0
        )[order],
        "initial_state_sha256": np.concatenate(
            [piece["initial_state_sha256"] for piece in pieces], axis=0
        )[order],
    }
    for key in ("raw_output", "raw_kernel", "raw_weighted_kernel", "raw_loss", "raw_q1", "raw_q2"):
        if all(key in piece for piece in pieces):
            combined = np.concatenate([piece[key] for piece in pieces], axis=1)
            merged[key] = combined[:, trajectory_order]
    if "output_nodes" in pieces[0]:
        merged["output_nodes"] = pieces[0]["output_nodes"].copy()
    _validate_dataset(merged)
    return merged


def _pair_columns(indices: np.ndarray) -> np.ndarray:
    indices = np.asarray(indices, dtype=np.int64)
    return np.stack((2 * indices, 2 * indices + 1), axis=1)


def _strict_interp_x(x: np.ndarray, *, tolerance: float = 1e-10) -> tuple[np.ndarray, np.ndarray]:
    increments = np.diff(x)
    if float(np.min(increments)) < -tolerance:
        raise AnalysisInvalid("curve is nonmonotone beyond tolerance")
    keep = np.concatenate(([True], increments > 0.0))
    if np.count_nonzero(keep) < 2:
        raise AnalysisInvalid("curve has fewer than two distinct abscissas")
    return x[keep], keep


def lineage_outcomes(
    data: dict[str, np.ndarray],
    nodes: np.ndarray,
    *,
    estimand: str,
    indices: np.ndarray | None = None,
) -> np.ndarray:
    """Return one row per selected lineage and one column per output node."""

    _validate_dataset(data)
    nodes = np.asarray(nodes, dtype=np.float64)
    if np.any(nodes <= 0.0) or np.any(nodes >= 1.0):
        raise ValueError("positive curve nodes must lie strictly between zero and one")
    count = len(data["lineage_ids"])
    selected = np.arange(count, dtype=np.int64) if indices is None else np.asarray(indices, dtype=np.int64)
    if selected.ndim != 1 or selected.size < 2 or np.any(selected < 0) or np.any(selected >= count):
        raise ValueError("invalid lineage resample")
    columns = _pair_columns(selected)
    flat_columns = columns.reshape(-1)
    time = data["raw_time"]
    output = data["raw_output"][:, flat_columns]
    kernel = data["raw_kernel"][:, flat_columns]

    if estimand == "effective":
        mean_output = output.mean(axis=1)
        x, keep = _strict_interp_x(mean_output)
        if nodes[0] < x[0] or nodes[-1] > x[-1]:
            raise AnalysisInvalid("resampled mean curve does not hit every node")
        node_time = np.interp(nodes, x, time[keep])
        weighted = data["raw_weighted_kernel"][:, flat_columns]
        values = np.empty((len(selected), len(nodes)), dtype=np.float64)
        for row in range(len(selected)):
            branch0 = np.interp(node_time, time, weighted[:, 2 * row])
            branch1 = np.interp(node_time, time, weighted[:, 2 * row + 1])
            values[row] = 0.5 * (branch0 + branch1) / (1.0 - nodes)
        return values

    if estimand == "progress":
        values = np.empty((len(selected), len(nodes)), dtype=np.float64)
        for row in range(len(selected)):
            branch_values = []
            for branch in (0, 1):
                column = 2 * row + branch
                f = output[:, column]
                f0 = float(f[0])
                if f0 >= 1.0:
                    raise AnalysisInvalid("path starts at or above target")
                progress = (f - f0) / (1.0 - f0)
                x, keep = _strict_interp_x(progress)
                if nodes[0] < x[0] or nodes[-1] > x[-1]:
                    raise AnalysisInvalid("path does not hit every progress node")
                branch_values.append(np.interp(nodes, x, kernel[keep, column]))
            values[row] = 0.5 * (branch_values[0] + branch_values[1])
        return values
    raise ValueError(f"unknown estimand {estimand!r}")


def _crossfit_adjust(
    outcomes: np.ndarray,
    controls: np.ndarray,
    fold_labels: np.ndarray,
    *,
    ridge_factor: float,
) -> tuple[np.ndarray, np.ndarray]:
    outcomes = np.asarray(outcomes, dtype=np.float64)
    controls = np.asarray(controls, dtype=np.float64)
    folds = np.asarray(fold_labels, dtype=np.int64)
    if controls.ndim == 1:
        controls = controls[:, None]
    if outcomes.ndim != 2 or controls.shape[0] != outcomes.shape[0]:
        raise ValueError("cross-fit shapes are inconsistent")
    unique_folds = np.unique(folds)
    if not np.array_equal(unique_folds, np.arange(4)):
        raise AnalysisInvalid("cross-fit requires all four folds")
    adjusted = np.empty_like(outcomes)
    betas = np.empty((4, outcomes.shape[1], controls.shape[1]), dtype=np.float64)
    tiny = np.finfo(np.float64).tiny

    for fold in range(4):
        test = folds == fold
        train = ~test
        if np.count_nonzero(test) < 1 or np.count_nonzero(train) <= controls.shape[1]:
            raise AnalysisInvalid("cross-fit fold is underdetermined")
        X = controls[train]
        Y = outcomes[train]
        Xc = X - X.mean(axis=0, keepdims=True)
        Yc = Y - Y.mean(axis=0, keepdims=True)
        gram = Xc.T @ Xc
        ridge_scale = float(np.trace(gram)) / max(1, controls.shape[1])
        ridge = max(tiny, ridge_factor * ridge_scale)
        matrix = gram + ridge * np.eye(controls.shape[1])
        try:
            beta = np.linalg.solve(matrix, Xc.T @ Yc).T
        except np.linalg.LinAlgError as exc:
            raise AnalysisInvalid("cross-fit control regression is singular") from exc
        betas[fold] = beta
        adjusted[test] = outcomes[test] - controls[test] @ beta.T
    return adjusted, betas


def estimate(
    data: dict[str, np.ndarray],
    width: int,
    nodes: np.ndarray,
    *,
    estimand: str,
    control: str = "scalar",
    indices: np.ndarray | None = None,
    fold_labels: np.ndarray | None = None,
    precomputed_full_outcomes: np.ndarray | None = None,
) -> Estimate:
    count = len(data["lineage_ids"])
    selected = np.arange(count, dtype=np.int64) if indices is None else np.asarray(indices, dtype=np.int64)
    if precomputed_full_outcomes is None:
        outcomes = lineage_outcomes(data, nodes, estimand=estimand, indices=selected)
    else:
        full = np.asarray(precomputed_full_outcomes, dtype=np.float64)
        if full.shape != (count, len(nodes)):
            raise ValueError("precomputed outcome cache has the wrong shape")
        outcomes = full[selected]
    if fold_labels is None:
        folds = np.asarray(data["lineage_ids"], dtype=np.int64)[selected] % 4
    else:
        folds = np.asarray(fold_labels, dtype=np.int64)
    if control == "scalar":
        controls = data["initial_total"][selected] - exact_initial_total_mean(width)
        ridge_factor = 1e-12
    elif control == "components":
        controls = data["initial_components"][selected] - exact_initial_component_means(width)[None, :]
        ridge_factor = 1e-10
    elif control == "none":
        controlled = outcomes.copy()
        betas = np.zeros((4, outcomes.shape[1], 0), dtype=np.float64)
        return Estimate(
            raw_mean=outcomes.mean(axis=0),
            raw_se=outcomes.std(axis=0, ddof=1) / math.sqrt(len(outcomes)),
            controlled_mean=controlled.mean(axis=0),
            raw_lineage=outcomes,
            controlled_lineage=controlled,
            betas=betas,
        )
    else:
        raise ValueError(f"unknown control mode {control!r}")
    controlled, betas = _crossfit_adjust(
        outcomes, controls, folds, ridge_factor=ridge_factor
    )
    return Estimate(
        raw_mean=outcomes.mean(axis=0),
        raw_se=outcomes.std(axis=0, ddof=1) / math.sqrt(len(outcomes)),
        controlled_mean=controlled.mean(axis=0),
        raw_lineage=outcomes,
        controlled_lineage=controlled,
        betas=betas,
    )


def initialization_calibration(data: dict[str, np.ndarray], width: int) -> dict[str, Any]:
    components = data["initial_components"]
    total = data["initial_total"]
    targets = np.concatenate(
        (exact_initial_component_means(width), [exact_initial_total_mean(width)])
    )
    samples = np.column_stack((components, total))
    means = samples.mean(axis=0)
    se = samples.std(axis=0, ddof=1) / math.sqrt(len(samples))
    defects = means - targets
    within = np.abs(defects) <= 4.0 * se
    return {
        "labels": ["kernel_a", "kernel_W", "kernel_u", "kernel_total"],
        "exact": targets.tolist(),
        "raw_mean": means.tolist(),
        "raw_lineage_se": se.tolist(),
        "defect": defects.tolist(),
        "within_four_se": within.tolist(),
        "pass": bool(np.all(within)),
    }


def jackknife_clock_bias(
    datasets: dict[int, dict[str, np.ndarray]],
    *,
    nodes: np.ndarray = POSITIVE_NODES,
) -> dict[str, Any]:
    """Delete-one-lineage bias diagnostic for nonlinear K_eff inversion."""

    raw_bias_rows = []
    controlled_bias_rows = []
    raw_corrected_rows = []
    controlled_corrected_rows = []
    details: dict[str, Any] = {}
    for width in (2048, 4096, 8192):
        data = datasets[width]
        count = len(data["lineage_ids"])
        full = estimate(
            data, width, nodes, estimand="effective", control="scalar"
        )
        loo_raw = []
        loo_controlled = []
        for deleted in range(count):
            indices = np.delete(np.arange(count, dtype=np.int64), deleted)
            current = estimate(
                data,
                width,
                nodes,
                estimand="effective",
                control="scalar",
                indices=indices,
            )
            loo_raw.append(current.raw_mean)
            loo_controlled.append(current.controlled_mean)
        loo_raw_array = np.stack(loo_raw)
        loo_controlled_array = np.stack(loo_controlled)
        raw_bias = (count - 1) * (loo_raw_array.mean(axis=0) - full.raw_mean)
        controlled_bias = (count - 1) * (
            loo_controlled_array.mean(axis=0) - full.controlled_mean
        )
        raw_corrected = full.raw_mean - raw_bias
        controlled_corrected = full.controlled_mean - controlled_bias
        raw_bias_rows.append(raw_bias)
        controlled_bias_rows.append(controlled_bias)
        raw_corrected_rows.append(raw_corrected)
        controlled_corrected_rows.append(controlled_corrected)
        details[str(width)] = {
            "raw_bias_estimate": raw_bias.tolist(),
            "controlled_bias_estimate": controlled_bias.tolist(),
            "raw_bias_corrected_sensitivity": raw_corrected.tolist(),
            "controlled_bias_corrected_sensitivity": controlled_corrected.tolist(),
        }

    raw_corrected_by_width = np.stack(raw_corrected_rows)
    controlled_corrected_by_width = np.stack(controlled_corrected_rows)
    model_sensitivity: dict[str, Any] = {"raw": {}, "controlled": {}}
    for model in ("top_width", "inv_n", "inv_sqrt_n"):
        model_sensitivity["raw"][model] = fit_intercept(
            raw_corrected_by_width, WIDTHS, model
        ).tolist()
        model_sensitivity["controlled"][model] = fit_intercept(
            controlled_corrected_by_width, WIDTHS, model
        ).tolist()
    return {
        "method": "delete_one_lineage_jackknife_bias=(R-1)*(mean(T_minus_i)-T_full)",
        "primary_estimate_is_not_bias_subtracted": True,
        "by_width": details,
        "raw_bias_by_width": np.stack(raw_bias_rows).tolist(),
        "controlled_bias_by_width": np.stack(controlled_bias_rows).tolist(),
        "bias_corrected_model_sensitivity": model_sensitivity,
    }


def stratified_bootstrap_indices(
    lineage_ids: np.ndarray, resamples: int, seed: int
) -> tuple[np.ndarray, np.ndarray]:
    ids = np.asarray(lineage_ids, dtype=np.int64)
    if len(ids) != 16:
        raise AnalysisInvalid("frozen bootstrap requires exactly 16 lineages")
    folds = ids % 4
    members = [np.flatnonzero(folds == fold) for fold in range(4)]
    if any(len(group) != 4 for group in members):
        raise AnalysisInvalid("each frozen bootstrap fold must contain four lineages")
    rng = np.random.default_rng(seed)
    draws = np.empty((resamples, 16), dtype=np.int64)
    labels = np.tile(np.repeat(np.arange(4, dtype=np.int64), 4), (resamples, 1))
    for replicate in range(resamples):
        draws[replicate] = np.concatenate(
            [rng.choice(group, size=4, replace=True) for group in members]
        )
    return draws, labels


def fit_intercept(values: np.ndarray, widths: np.ndarray, model: str) -> np.ndarray:
    values = np.asarray(values, dtype=np.float64)
    widths = np.asarray(widths, dtype=np.float64)
    if values.shape[0] != len(widths):
        raise ValueError("width axis mismatch")
    if model == "top_width":
        return values[-1].copy()
    if model == "inv_n":
        x = 1.0 / widths
    elif model == "inv_sqrt_n":
        x = 1.0 / np.sqrt(widths)
    elif model == "inv_n_quadratic":
        design = np.column_stack((np.ones(len(widths)), 1.0 / widths, 1.0 / widths**2))
        return (np.linalg.pinv(design) @ values)[0]
    else:
        raise ValueError(f"unknown width model {model!r}")
    design = np.column_stack((np.ones(len(widths)), x))
    return (np.linalg.pinv(design) @ values)[0]


def simultaneous_log_band(
    point: np.ndarray,
    replicates: np.ndarray,
    *,
    confidence: float = 0.99,
) -> tuple[np.ndarray, np.ndarray, float]:
    if np.any(point <= 0.0) or np.any(replicates <= 0.0):
        raise AnalysisInvalid("log bands require positive estimates")
    center = np.log(point)
    deviations = np.log(replicates) - center[None, :]
    scale = deviations.std(axis=0, ddof=1)
    if np.any(scale <= 0.0) or not np.all(np.isfinite(scale)):
        raise AnalysisInvalid("degenerate bootstrap scale")
    statistic = np.max(np.abs(deviations / scale[None, :]), axis=1)
    critical = float(np.quantile(statistic, confidence, method="higher"))
    return np.exp(center - critical * scale), np.exp(center + critical * scale), critical


def analyze_width_models(
    point_by_width: np.ndarray,
    bootstrap_by_width: np.ndarray,
) -> dict[str, Any]:
    """Fit all frozen models for one estimand/control.

    Shapes are ``(3,nodes)`` and ``(replicates,3,nodes)``.
    """

    mandatory = ("top_width", "inv_n", "inv_sqrt_n")
    result: dict[str, Any] = {"models": {}}
    union_lower = None
    union_upper = None
    for model in mandatory:
        point = fit_intercept(point_by_width, WIDTHS, model)
        boot = np.stack(
            [fit_intercept(sample, WIDTHS, model) for sample in bootstrap_by_width],
            axis=0,
        )
        lower, upper, critical = simultaneous_log_band(point, boot)
        result["models"][model] = {
            "point": point.tolist(),
            "lower_99_simultaneous": lower.tolist(),
            "upper_99_simultaneous": upper.tolist(),
            "critical_max_log_statistic": critical,
        }
        union_lower = lower if union_lower is None else np.minimum(union_lower, lower)
        union_upper = upper if union_upper is None else np.maximum(union_upper, upper)

    result["mandatory_union"] = {
        "lower": union_lower.tolist(),
        "upper": union_upper.tolist(),
        "full_width": (union_upper - union_lower).tolist(),
    }

    for model in ("inv_n", "inv_sqrt_n"):
        point = fit_intercept(point_by_width[1:], WIDTHS[1:], model)
        boot = np.stack(
            [fit_intercept(sample[1:], WIDTHS[1:], model) for sample in bootstrap_by_width],
            axis=0,
        )
        lower, upper, critical = simultaneous_log_band(point, boot)
        result["models"][f"{model}_leave_2048"] = {
            "point": point.tolist(),
            "lower_99_simultaneous": lower.tolist(),
            "upper_99_simultaneous": upper.tolist(),
            "critical_max_log_statistic": critical,
            "sensitivity_only": True,
        }
    return result


def bootstrap_campaign(
    datasets: dict[int, dict[str, np.ndarray]],
    *,
    nodes: np.ndarray = POSITIVE_NODES,
    resamples: int = 20_000,
    seed: int = 202608190731,
) -> dict[str, Any]:
    expected = (2048, 4096, 8192)
    if tuple(sorted(datasets)) != expected:
        raise AnalysisInvalid("scientific ladder must contain exactly 2048,4096,8192")
    reference_ids = datasets[2048]["lineage_ids"]
    if not np.array_equal(reference_ids, np.arange(16)):
        raise AnalysisInvalid("scientific lineages must be exactly 0 through 15")
    for width in expected[1:]:
        if not np.array_equal(datasets[width]["lineage_ids"], reference_ids):
            raise AnalysisInvalid("lineage ids differ across widths")
    draws, bootstrap_folds = stratified_bootstrap_indices(reference_ids, resamples, seed)
    estimands = ("effective", "progress")
    progress_cache = {
        width: lineage_outcomes(
            datasets[width], nodes, estimand="progress"
        )
        for width in expected
    }
    point: dict[str, np.ndarray] = {}
    raw_point: dict[str, np.ndarray] = {}
    raw_se: dict[str, np.ndarray] = {}
    component_point: dict[str, np.ndarray] = {}
    for estimand in estimands:
        controlled_rows = []
        raw_rows = []
        se_rows = []
        component_rows = []
        for width in expected:
            current = estimate(
                datasets[width],
                width,
                nodes,
                estimand=estimand,
                control="scalar",
                precomputed_full_outcomes=(
                    progress_cache[width] if estimand == "progress" else None
                ),
            )
            component = estimate(
                datasets[width],
                width,
                nodes,
                estimand=estimand,
                control="components",
                precomputed_full_outcomes=(
                    progress_cache[width] if estimand == "progress" else None
                ),
            )
            controlled_rows.append(current.controlled_mean)
            raw_rows.append(current.raw_mean)
            se_rows.append(current.raw_se)
            component_rows.append(component.controlled_mean)
        point[estimand] = np.stack(controlled_rows)
        raw_point[estimand] = np.stack(raw_rows)
        raw_se[estimand] = np.stack(se_rows)
        component_point[estimand] = np.stack(component_rows)

    bootstrap = {
        estimand: np.empty((resamples, 3, len(nodes)), dtype=np.float64)
        for estimand in estimands
    }
    raw_bootstrap = {
        estimand: np.empty((resamples, 3, len(nodes)), dtype=np.float64)
        for estimand in estimands
    }
    valid = 0
    failures: dict[str, int] = {}
    for replicate in range(resamples):
        try:
            indices = draws[replicate]
            folds = bootstrap_folds[replicate]
            for e_index, estimand in enumerate(estimands):
                del e_index
                for w_index, width in enumerate(expected):
                    current = estimate(
                        datasets[width],
                        width,
                        nodes,
                        estimand=estimand,
                        control="scalar",
                        indices=indices,
                        fold_labels=folds,
                        precomputed_full_outcomes=(
                            progress_cache[width]
                            if estimand == "progress"
                            else None
                        ),
                    )
                    bootstrap[estimand][valid, w_index] = current.controlled_mean
                    raw_bootstrap[estimand][valid, w_index] = current.raw_mean
            valid += 1
        except (AnalysisInvalid, np.linalg.LinAlgError, FloatingPointError) as exc:
            key = f"{type(exc).__name__}: {exc}"
            failures[key] = failures.get(key, 0) + 1
    valid_fraction = valid / resamples
    if valid_fraction < 0.995:
        raise AnalysisInvalid(
            f"only {valid_fraction:.6f} bootstrap replicates are valid"
        )
    for estimand in estimands:
        bootstrap[estimand] = bootstrap[estimand][:valid]
        raw_bootstrap[estimand] = raw_bootstrap[estimand][:valid]

    width_results = {
        estimand: analyze_width_models(point[estimand], bootstrap[estimand])
        for estimand in estimands
    }
    raw_width_results = {
        estimand: analyze_width_models(raw_point[estimand], raw_bootstrap[estimand])
        for estimand in estimands
    }

    # Estimator disagreement is evaluated on like-for-like controlled samples.
    disagreement_point = np.abs(np.log(point["effective"]) - np.log(point["progress"]))
    disagreement_boot = np.abs(
        np.log(bootstrap["effective"]) - np.log(bootstrap["progress"])
    )
    contraction_2048_4096 = disagreement_boot[:, 1] - disagreement_boot[:, 0]
    contraction_4096_8192 = disagreement_boot[:, 2] - disagreement_boot[:, 1]
    lower_q = 0.005
    upper_q = 0.995
    contraction = {
        "D_by_width": disagreement_point.tolist(),
        "point_monotone_through_y_0_9": bool(
            np.all(np.diff(disagreement_point[:, INFERENTIAL_MASK], axis=0) <= 0.0)
        ),
        "D4096_minus_D2048_ci99": np.quantile(
            contraction_2048_4096, [lower_q, upper_q], axis=0, method="higher"
        ).tolist(),
        "D8192_minus_D4096_ci99": np.quantile(
            contraction_4096_8192, [lower_q, upper_q], axis=0, method="higher"
        ).tolist(),
    }

    return {
        "nodes": nodes.tolist(),
        "resamples_requested": resamples,
        "resamples_valid": valid,
        "valid_fraction": valid_fraction,
        "bootstrap_seed": seed,
        "bootstrap_failures": failures,
        "controlled_point_by_width": {key: value.tolist() for key, value in point.items()},
        "raw_point_by_width": {key: value.tolist() for key, value in raw_point.items()},
        "raw_lineage_se_by_width": {key: value.tolist() for key, value in raw_se.items()},
        "component_control_sensitivity_point_by_width": {
            key: value.tolist() for key, value in component_point.items()
        },
        "width_models": width_results,
        "raw_width_models": raw_width_results,
        "estimator_disagreement": contraction,
        # Kept in memory by the CLI only when requested; not JSON serialized.
        "_bootstrap_arrays": bootstrap,
        "_raw_bootstrap_arrays": raw_bootstrap,
    }


def authorization_diagnostics(result: dict[str, Any], step_result: dict[str, Any]) -> dict[str, Any]:
    """Evaluate the exact frozen eligibility gates; never launch a holdout."""

    nodes = np.asarray(result["nodes"], dtype=np.float64)
    i09 = int(np.flatnonzero(np.isclose(nodes, 0.9))[0])
    point = np.asarray(result["controlled_point_by_width"]["effective"])
    boot = result["_bootstrap_arrays"]["effective"]
    differences = {
        "K4096_minus_K2048": boot[:, 1] - boot[:, 0],
        "K8192_minus_K4096": boot[:, 2] - boot[:, 1],
    }
    adjacent: dict[str, Any] = {}
    resolved = True
    for name, samples in differences.items():
        interval = np.quantile(samples[:, i09], [0.005, 0.995], method="higher")
        point_difference = (
            point[1, i09] - point[0, i09]
            if name.startswith("K4096")
            else point[2, i09] - point[1, i09]
        )
        same_signed_exclusion = bool(
            (point_difference > 0.0 and interval[0] > 0.0)
            or (point_difference < 0.0 and interval[1] < 0.0)
        )
        adjacent[name] = {
            "point": float(point_difference),
            "ci99": interval.tolist(),
            "resolved_same_sign": same_signed_exclusion,
        }
        resolved = resolved and same_signed_exclusion
    contraction = bool(
        abs(adjacent["K8192_minus_K4096"]["point"])
        < abs(adjacent["K4096_minus_K2048"]["point"])
    )

    primary_union = result["width_models"]["effective"]["mandatory_union"]
    secondary_union = result["width_models"]["progress"]["mandatory_union"]
    p_low = float(primary_union["lower"][i09])
    p_high = float(primary_union["upper"][i09])
    s_low = float(secondary_union["lower"][i09])
    s_high = float(secondary_union["upper"][i09])
    union_overlap = max(p_low, s_low) <= min(p_high, s_high)
    union_width = p_high - p_low
    resolution = union_width <= 0.8209726639786652

    leave_checks: dict[str, Any] = {}
    leave_pass = True
    for model in ("inv_n", "inv_sqrt_n"):
        full = result["width_models"]["effective"]["models"][model]
        leave = result["width_models"]["effective"]["models"][f"{model}_leave_2048"]
        value = float(leave["point"][i09])
        full_value = float(full["point"][i09])
        inside = float(full["lower_99_simultaneous"][i09]) <= value <= float(
            full["upper_99_simultaneous"][i09]
        )
        movement = abs(value - full_value)
        current_pass = inside and movement <= 0.5 * union_width
        leave_checks[model] = {
            "full_intercept": full_value,
            "leave_2048_intercept": value,
            "inside_full_99_band": inside,
            "absolute_movement": movement,
            "half_union_width": 0.5 * union_width,
            "pass": current_pass,
        }
        leave_pass = leave_pass and current_pass

    disagreement = result["estimator_disagreement"]
    disagreement_ci = float(disagreement["D8192_minus_D4096_ci99"][1][i09])
    disagreement_pass = bool(
        disagreement["point_monotone_through_y_0_9"] and disagreement_ci < 0.0
    )

    jackknife = result["jackknife_clock_inversion_bias"]
    threshold = 0.25 * union_width
    raw_bias_at_09 = np.asarray(jackknife["raw_bias_by_width"])[:, i09]
    controlled_bias_at_09 = np.asarray(jackknife["controlled_bias_by_width"])[:, i09]
    jackknife_model_movements: dict[str, Any] = {"raw": {}, "controlled": {}}
    jackknife_pass = bool(
        np.max(np.abs(raw_bias_at_09)) <= threshold
        and np.max(np.abs(controlled_bias_at_09)) <= threshold
    )
    for control_name, model_source in (
        ("raw", result["raw_width_models"]["effective"]),
        ("controlled", result["width_models"]["effective"]),
    ):
        for model in ("top_width", "inv_n", "inv_sqrt_n"):
            primary_value = float(model_source["models"][model]["point"][i09])
            corrected_value = float(
                jackknife["bias_corrected_model_sensitivity"][control_name][model][i09]
            )
            movement = abs(corrected_value - primary_value)
            current_pass = movement <= threshold
            jackknife_model_movements[control_name][model] = {
                "primary": primary_value,
                "bias_corrected_sensitivity": corrected_value,
                "absolute_movement": movement,
                "threshold": threshold,
                "pass": current_pass,
            }
            jackknife_pass = jackknife_pass and current_pass

    calibration_pass = all(
        record["pass"] for record in result["initialization_calibration"].values()
    )
    gates = {
        "initialization_calibration": calibration_pass,
        "paired_adjacent_corrections_resolved": resolved,
        "adjacent_correction_magnitude_contracts": contraction,
        "estimand_unions_overlap_at_y_0_9": union_overlap,
        "primary_union_width_at_y_0_9": union_width,
        "exact_resolution_threshold": 0.8209726639786652,
        "primary_union_meets_resolution": resolution,
        "leave_2048_sensitivities": leave_checks,
        "leave_2048_pass": leave_pass,
        "estimator_disagreement_upper_ci_at_y_0_9": disagreement_ci,
        "estimator_disagreement_contracts": disagreement_pass,
        "step_halving": bool(step_result["pass"]),
        "jackknife_clock_bias_threshold": threshold,
        "jackknife_clock_bias_model_movements": jackknife_model_movements,
        "jackknife_clock_bias_nonmaterial": jackknife_pass,
    }
    eligible = bool(
        calibration_pass
        and resolved
        and contraction
        and union_overlap
        and resolution
        and leave_pass
        and disagreement_pass
        and step_result["pass"]
        and jackknife_pass
    )
    return {
        "status": (
            "eligible_for_separate_authorization"
            if eligible
            else "closed_inconclusive_at_width_8192"
        ),
        "does_not_authorize_execution": True,
        "adjacent_corrections": adjacent,
        "gates": gates,
    }


def step_halving_gate(
    coarse: dict[str, np.ndarray],
    fine: dict[str, np.ndarray],
    union_width_by_estimand: dict[str, np.ndarray],
    *,
    nodes: np.ndarray = POSITIVE_NODES,
) -> dict[str, Any]:
    if not np.array_equal(coarse["lineage_ids"], fine["lineage_ids"]):
        raise AnalysisInvalid("step-halving lineage ids differ")
    if not np.array_equal(coarse["lineage_ids"], np.array([0, 1])):
        raise AnalysisInvalid("frozen step-halving lineages must be 0 and 1")
    if not np.array_equal(
        coarse["initial_state_sha256"], fine["initial_state_sha256"]
    ):
        raise AnalysisInvalid("step-halving initial-state digests differ")
    np.testing.assert_allclose(
        coarse["raw_output"][0], fine["raw_output"][0], rtol=8e-15, atol=8e-15
    )
    np.testing.assert_allclose(
        coarse["raw_kernel"][0], fine["raw_kernel"][0], rtol=8e-15, atol=8e-15
    )

    output: dict[str, Any] = {}
    index_09 = int(np.flatnonzero(np.isclose(nodes, 0.9))[0])
    passed = True
    for estimand in ("effective", "progress"):
        coarse_values = lineage_outcomes(coarse, nodes, estimand=estimand).mean(axis=0)
        fine_values = lineage_outcomes(fine, nodes, estimand=estimand).mean(axis=0)
        absolute = np.abs(coarse_values - fine_values)
        relative = absolute / np.maximum(np.abs(fine_values), np.finfo(float).tiny)
        fixed = bool(
            np.all(relative[nodes <= 0.95] <= 0.002)
            and np.all(relative[np.isclose(nodes, 0.99)] <= 0.005)
        )
        realized = bool(
            absolute[index_09]
            <= 0.25 * float(union_width_by_estimand[estimand][index_09])
        )
        output[estimand] = {
            "coarse": coarse_values.tolist(),
            "fine": fine_values.tolist(),
            "absolute_change": absolute.tolist(),
            "relative_change": relative.tolist(),
            "fixed_relative_gate": fixed,
            "quarter_realized_union_gate_at_y_0_9": realized,
        }
        passed = passed and fixed and realized
    output["pass"] = passed
    return output


def _json_ready(result: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in result.items() if not key.startswith("_")}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n2048", type=Path, required=True)
    parser.add_argument("--n4096", type=Path, required=True)
    parser.add_argument("--n8192-shard0", type=Path, required=True)
    parser.add_argument("--n8192-shard1", type=Path, required=True)
    parser.add_argument("--n4096-halfstep", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--resamples", type=int, default=20_000)
    args = parser.parse_args()

    datasets = {
        2048: load_npz(args.n2048),
        4096: load_npz(args.n4096),
        8192: merge_shards(
            [load_npz(args.n8192_shard0), load_npz(args.n8192_shard1)]
        ),
    }
    result = bootstrap_campaign(datasets, resamples=args.resamples)
    calibrations = {
        str(width): initialization_calibration(data, width)
        for width, data in datasets.items()
    }
    union_widths = {
        estimand: np.asarray(
            result["width_models"][estimand]["mandatory_union"]["full_width"],
            dtype=np.float64,
        )
        for estimand in ("effective", "progress")
    }
    coarse_subset = {
        key: (
            value[:, :4]
            if key.startswith("raw_") and value.ndim == 2
            else value[:2]
            if key in {"lineage_ids", "initial_components", "initial_total", "initial_state_sha256"}
            else value
        )
        for key, value in datasets[4096].items()
    }
    fine = load_npz(args.n4096_halfstep)
    result["initialization_calibration"] = calibrations
    result["jackknife_clock_inversion_bias"] = jackknife_clock_bias(datasets)
    result["step_halving"] = step_halving_gate(
        coarse_subset, fine, union_widths
    )
    result["width_16384_eligibility"] = authorization_diagnostics(
        result, result["step_halving"]
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(_json_ready(result), indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
