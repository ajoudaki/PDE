from __future__ import annotations

from dataclasses import replace

import numpy as np

from analysis.bootstrap import bootstrap_point
from analysis.pilot_runner import (
    _difference_interval,
    interval_overlap,
    paired_step_halving,
    projection_trend,
)
from analysis.tests.test_analysis import synthetic_physical_point


def _configured_point(point_id: str, width: int, *, step: float, pairs: int):
    point = synthetic_physical_point(width=width, pairs=pairs)
    return replace(
        point,
        point_id=point_id,
        config={
            **point.config,
            "seed_base": 1234,
            "step": step,
            "max_time": 1.0,
            "integrator": "rk4",
            "microcanonical_readout": False,
        },
        diagnostics={
            **point.diagnostics,
            "max_projection_relative_norm": 0.1 if width == 256 else 0.06,
        },
    )


def test_paired_step_gate_uses_exact_subset_and_initial_lineages() -> None:
    coarse = _configured_point("coarse", 512, step=2e-4, pairs=12)
    extended = dict(coarse.arrays)
    extended_output = 1.25 * extended["raw_trajectory_output"]
    extended["raw_trajectory_output"] = extended_output
    extended["raw_trajectory_weighted_kernel"] = (
        (1.0 - extended_output) * extended["raw_trajectory_kernel"]
    )
    extended["raw_trajectory_loss"] = np.square(1.0 - extended_output)
    extended["output_nodes"] = np.array([0.0, 0.2, 0.4, 0.99])
    coarse = replace(coarse, arrays=extended)
    arrays = {}
    for key, value in coarse.arrays.items():
        if key.startswith("raw_trajectory_"):
            arrays[key] = value[:, :8]
        elif key.startswith("node_pair_"):
            arrays[key] = value[:, :4]
        elif key.startswith("node_raw_"):
            arrays[key] = value[:, :8]
        else:
            arrays[key] = value
    fine = replace(
        coarse,
        point_id="fine",
        antithetic_pairs=4,
        arrays=arrays,
        config={
            **coarse.config,
            "step": 1e-4,
            "analysis": {
                "paired_coarse_point_id": "coarse",
                "paired_lineage_indices": [0, 1, 2, 3],
            },
        },
    )
    # The fine fixture is the exact first-four-lineage restriction of coarse.
    result = paired_step_halving(
        {"coarse": coarse, "fine": fine},
        {
            "coarse_point_id": "coarse",
            "fine_point_id": "fine",
            "coarse_lineage_indices": [0, 1, 2, 3],
            "maximum_relative_change_through_y_0_95": 1e-12,
            "maximum_relative_change_at_y_0_99": 1e-12,
        },
    )
    assert result["passed"]
    assert result["initial_output_and_kernel_bitwise_equal"]


def test_projection_and_interval_gates_are_fail_closed() -> None:
    low = _configured_point("low", 256, step=2e-4, pairs=8)
    high = _configured_point("high", 512, step=2e-4, pairs=8)
    projection = projection_trend(
        {"low": low, "high": high},
        {
            "point_256": "low",
            "point_512": "high",
            "statistic": "max_projection_relative_norm",
            "maximum_scaled_rate_ratio": 2.0,
        },
    )
    assert projection["passed"]

    left = bootstrap_point(low, replicates=40, seed=10, confidence=0.9)
    right = bootstrap_point(high, replicates=40, seed=11, confidence=0.9)
    assert interval_overlap(left, right)["passed"]
    shifted_band = replace(
        right.band,
        estimate=right.band.estimate * 10.0,
        lower=right.band.lower * 10.0,
        upper=right.band.upper * 10.0,
    )
    assert not interval_overlap(left, replace(right, band=shifted_band))["passed"]


def test_two_width_percentile_trend_uses_declared_attempt_count() -> None:
    low = _configured_point("low", 256, step=2e-4, pairs=8)
    high = _configured_point("high", 512, step=2e-4, pairs=8)

    def metric(point, indices=None):
        values = np.arange(point.antithetic_pairs, dtype=float)
        if indices is not None:
            values = values[indices]
        return float(np.mean(values) / point.width)

    result = _difference_interval(
        low,
        high,
        metric=metric,
        seed=99,
        resamples=80,
        minimum_valid_fraction=0.95,
        lower_quantile=0.005,
        upper_quantile=0.995,
    )
    assert result["attempted_resamples"] == 80
    assert result["valid_resamples"] == 80
    assert result["equal_tail_interval"][0] <= result["equal_tail_interval"][1]
