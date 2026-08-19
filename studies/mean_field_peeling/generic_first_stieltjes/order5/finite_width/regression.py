"""Preregistered normalized-sine finite-width regression harness.

The harness refuses to sample the large-width panel until the two exact tiny-
width routes agree seedwise.  It does not contain or infer a theoretical
prediction; callers must supply the flattened C prediction explicitly.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import numpy as np

from .feature_flow import draw_state, feature_flow_jet
from .oracles import sine_oracle
from .raw_ad import raw_coordinate_jet


@dataclass(frozen=True)
class WidthSummary:
    width: int
    seeds: int
    mean: float
    standard_error: float


def certify_seedwise_routes() -> float:
    """Return the worst scaled error after the mandatory exact pre-gate."""

    worst = 0.0
    for width in (1, 2):
        for seed in (104729, 130363, 155921):
            state = draw_state(width, seed)
            moving = feature_flow_jet(state, 1.0, sine_oracle).derivatives
            raw = raw_coordinate_jet(state, 1.0, sine_oracle)
            scale = np.maximum(1.0, np.maximum(np.abs(moving), np.abs(raw.derivatives)))
            error = float(np.max(np.abs(moving - raw.derivatives) / scale))
            family_error = abs(moving[5] - raw.six_families.value) / max(
                1.0, abs(moving[5]), abs(raw.six_families.value)
            )
            worst = max(worst, error, family_error)
    if worst > 5.0e-10:
        raise RuntimeError(f"exact seedwise pre-gate failed: scaled error {worst:.3e}")
    return worst


def _summarize_width(width: int, seeds: int, seed_offset: int) -> WidthSummary:
    values = np.empty(seeds, dtype=np.float64)
    for local_seed in range(seeds):
        state = draw_state(width, seed_offset + local_seed)
        values[local_seed] = feature_flow_jet(state, 1.0, sine_oracle).derivatives[5]
    standard_error = float(values.std(ddof=1) / np.sqrt(seeds))
    return WidthSummary(width, seeds, float(values.mean()), standard_error)


def run_preregistered_regression(
    prediction: float,
    *,
    widths: tuple[int, ...] = (32, 64, 128, 256, 512),
    seeds_per_width: int = 256,
    seed_offset: int = 900001,
) -> dict:
    """Weighted affine extrapolation in 1/n under the frozen decision rule."""

    if max(widths) > 512:
        raise ValueError("preregistered width cap is 512")
    if seeds_per_width * len(widths) > 10000:
        raise ValueError("preregistered network cap is 10,000")
    exact_error = certify_seedwise_routes()
    summaries = []
    cursor = seed_offset
    for width in widths:
        summaries.append(_summarize_width(width, seeds_per_width, cursor))
        cursor += seeds_per_width

    design = np.asarray([[1.0, 1.0 / row.width] for row in summaries])
    response = np.asarray([row.mean for row in summaries])
    variances = np.asarray([row.standard_error**2 for row in summaries])
    if np.any(variances <= 0.0) or not np.all(np.isfinite(variances)):
        raise RuntimeError("invalid standard errors; regression is inconclusive")
    precision = np.diag(1.0 / variances)
    covariance = np.linalg.inv(design.T @ precision @ design)
    coefficients = covariance @ design.T @ precision @ response
    intercept = float(coefficients[0])
    intercept_se = float(np.sqrt(covariance[0, 0]))
    z_score = abs(intercept - prediction) / intercept_se
    residual = response - design @ coefficients
    chi_square = float(residual @ precision @ residual)
    degrees_of_freedom = len(summaries) - 2
    diagnostics_valid = degrees_of_freedom >= 1 and chi_square / degrees_of_freedom <= 3.0
    if not diagnostics_valid or 3.0 < z_score <= 5.0:
        decision = "inconclusive"
    elif z_score <= 3.0:
        decision = "pass"
    else:
        decision = "fail_pending_replication"
    return {
        "activation": "sin(x)/sqrt((1-exp(-2))/2)",
        "target": "C=lim E[D_n^5 f_n]",
        "prediction": float(prediction),
        "exact_route_worst_scaled_error": exact_error,
        "summaries": [asdict(row) for row in summaries],
        "intercept": intercept,
        "intercept_standard_error": intercept_se,
        "z_score": z_score,
        "chi_square": chi_square,
        "degrees_of_freedom": degrees_of_freedom,
        "diagnostics_valid": diagnostics_valid,
        "decision": decision,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prediction", type=float, required=True)
    parser.add_argument("--seeds-per-width", type=int, default=256)
    parser.add_argument("--widths", type=int, nargs="+", default=[32, 64, 128, 256, 512])
    parser.add_argument("--seed-offset", type=int, default=900001)
    args = parser.parse_args()
    result = run_preregistered_regression(
        args.prediction,
        widths=tuple(args.widths),
        seeds_per_width=args.seeds_per_width,
        seed_offset=args.seed_offset,
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
