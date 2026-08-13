#!/usr/bin/env python3
"""Run the frozen order-13 normalized-jet median experiment."""

from __future__ import annotations

import hashlib
import json
import math
import os
import platform
import resource
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
STUDY = HERE.parents[1]
PEELING = STUDY / "peeling"
sys.path.insert(0, str(PEELING))
from finite_width_jet_reference import feature_jet  # noqa: E402


PROTOCOL = HERE / "FRESH_ORDER13_MEDIAN_PROTOCOL.md"
CERTIFICATE = STUDY / "theory/certificates_order11.json"
OUT = HERE / "runs/fresh_order13_median_run"
WIDTHS = (128, 256)
COUNT = 512
SEED_BASE = 2026081601
ADDRESS_CAP = 8 * 1024**3


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_median_interval(values: np.ndarray, alpha: float = 0.05) -> dict:
    ordered = np.sort(values)
    n = len(ordered)
    # Largest k (one-based lower order statistic) with two-sided binomial tail
    # no larger than alpha.  Compute exact integer tails over denominator 2**n.
    cumulative = 0
    k = 0
    for j in range(n + 1):
        candidate = cumulative + math.comb(n, j)
        if Fraction(2 * candidate, 2**n) <= Fraction(str(alpha)):
            cumulative = candidate
            k = j + 1
        else:
            break
    if k < 1:
        raise RuntimeError("sample too small for requested median interval")
    lower = float(ordered[k - 1])
    upper = float(ordered[n - k])
    coverage = 1.0 - 2.0 * float(Fraction(cumulative, 2**n))
    return {
        "k_one_based": k,
        "lower": lower,
        "upper": upper,
        "width": upper - lower,
        "coverage": coverage,
    }


def exact_targets() -> tuple[list[float], float]:
    raw = json.loads(CERTIFICATE.read_text())
    a = [Fraction(value) for value in raw["a"]]
    a0 = a[0]
    targets = [float(a[r] / a0 ** (2 * r + 1)) for r in range(1, 6)]

    moments = [Fraction(value) for value in raw["mu"]]
    determinant_slope = moments[1] * moments[3] - moments[2] ** 2
    determinant_constant = (
        -moments[1] * moments[4] ** 2
        + 2 * moments[2] * moments[3] * moments[4]
        - moments[3] ** 3
    )
    mu5_threshold = -determinant_constant / determinant_slope
    a1, a2, a3, a4, a5 = a[1:]
    remainder = (
        -116 * a0**4 * a1 * a5
        - 92 * a0**4 * a2 * a4
        - 42 * a0**4 * a3**2
        + 546 * a0**3 * a1**2 * a4
        + 884 * a0**3 * a1 * a2 * a3
        + 130 * a0**3 * a2**3
        - 1820 * a0**2 * a1**3 * a3
        - 2366 * a0**2 * a1**2 * a2**2
        + 5005 * a0 * a1**4 * a2
        - 2184 * a1**6
    )
    a6_threshold = (
        -mu5_threshold * a0**17 - remainder
    ) / (13 * a0**5)
    return targets, float(a6_threshold / a0**13)


def main() -> None:
    resource.setrlimit(resource.RLIMIT_AS, (ADDRESS_CAP, ADDRESS_CAP))
    OUT.mkdir(parents=True, exist_ok=True)
    targets, threshold = exact_targets()
    results: dict = {
        "design": {
            "widths": WIDTHS,
            "count_each": COUNT,
            "seed_rule": [SEED_BASE, "width", "zero_based_index"],
            "address_cap": ADDRESS_CAP,
            "thread_environment": {
                key: os.environ.get(key)
                for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")
            },
        },
        "provenance": {
            "protocol_sha256": sha256(PROTOCOL),
            "script_sha256": sha256(Path(__file__)),
            "finite_width_recurrence_sha256": sha256(
                PEELING / "finite_width_jet_reference.py"
            ),
            "certificate_sha256": sha256(CERTIFICATE),
            "python": platform.python_version(),
            "numpy": np.__version__,
        },
        "exact_c1_through_c5": targets,
        "c6_hankel_threshold": threshold,
        "widths": {},
    }

    raw_by_width = {}
    for width in WIDTHS:
        values = np.empty((COUNT, 6), dtype=np.float64)
        linear = np.empty(COUNT, dtype=np.float64)
        for index in range(COUNT):
            seed = np.random.SeedSequence([SEED_BASE, width, index]).generate_state(
                1, dtype=np.uint64
            )[0]
            jet = feature_jet(width, 13, 1.0, int(seed))
            a0n = jet[1]
            if not np.isfinite(a0n) or a0n <= 0:
                raise RuntimeError(f"invalid linear coefficient at width={width}, index={index}")
            linear[index] = a0n
            for r in range(1, 7):
                values[index, r - 1] = jet[2 * r + 1] / a0n ** (2 * r + 1)
            if not np.all(np.isfinite(values[index])):
                raise RuntimeError(f"nonfinite jet at width={width}, index={index}")
            if (index + 1) % 64 == 0:
                print(f"width={width} completed={index + 1}/{COUNT}", flush=True)
        raw_by_width[width] = values
        np.savez_compressed(OUT / f"normalized_jets_width_{width}.npz",
                            normalized=values, linear=linear)
        summaries = []
        for r in range(1, 7):
            column = values[:, r - 1]
            summaries.append({
                "r": r,
                "median": float(np.median(column)),
                "interval": exact_median_interval(column),
                "quantiles": {
                    str(q): float(np.quantile(column, q))
                    for q in (0.0, 0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99, 1.0)
                },
            })
        results["widths"][str(width)] = {
            "linear_median": float(np.median(linear)),
            "coefficients": summaries,
        }

    def interval_contains(summary: dict, target: float) -> bool:
        return summary["interval"]["lower"] <= target <= summary["interval"]["upper"]

    c128 = results["widths"]["128"]["coefficients"]
    c256 = results["widths"]["256"]["coefficients"]
    checks = {
        "n256_c1_through_c5_contain_exact": all(
            interval_contains(c256[r], targets[r]) for r in range(5)
        ),
        "n128_c4_c5_contain_exact": all(
            interval_contains(c128[r], targets[r]) for r in (3, 4)
        ),
        "lower_median_signs_correct": all(
            np.sign(c128[r]["median"]) == np.sign(targets[r])
            and np.sign(c256[r]["median"]) == np.sign(targets[r])
            for r in range(5)
        ),
        "c5_cross_width_relative_difference_at_most_20pct": (
            abs(c128[4]["median"] - c256[4]["median"])
            / abs(c256[4]["median"]) <= 0.20
        ),
    }
    calibrated = all(checks.values())
    upper_below = all(
        results["widths"][str(width)]["coefficients"][5]["interval"]["upper"]
        < threshold for width in WIDTHS
    )
    lower_above = all(
        results["widths"][str(width)]["coefficients"][5]["interval"]["lower"]
        > threshold for width in WIDTHS
    )
    if not calibrated:
        status = "uncalibrated_inconclusive"
    elif upper_below:
        status = "empirical_positive_side_signal"
    elif lower_above:
        status = "empirical_negative_side_signal"
    else:
        status = "order13_inconclusive"
    results["calibration_checks"] = checks
    results["status"] = status
    results["peak_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    encoded = json.dumps(results, indent=2) + "\n"
    (OUT / "results.json").write_text(encoded)
    (OUT / "run_command.txt").write_text(
        "OPENBLAS_NUM_THREADS=4 OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 "
        "python studies/stieltjes_conjecture/numerics/finite_width/"
        "run_fresh_order13_median.py\n"
    )
    print(encoded)


if __name__ == "__main__":
    main()
