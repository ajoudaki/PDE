#!/usr/bin/env python3
"""Fresh-seed test of the frozen adjacent-ratio calibration."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import resource
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
STUDY = HERE.parents[1]
MFP_COMPILER = STUDY.parent / "mean_field_peeling" / "quadratic_compiler"
sys.path.insert(0, str(MFP_COMPILER))
from finite_width_jet_reference import feature_jet  # noqa: E402


PROTOCOL = HERE / "FRESH_CALIBRATED_RATIO_PROTOCOL.md"
CERTIFICATE = STUDY / "theory/certificates_order11.json"
OUT = HERE / "runs/fresh_calibrated_ratio_run"
WIDTHS = (128, 256)
COUNT = 512
BOOTSTRAPS = 20_000
SEED_BASE = 2026081701
BOOTSTRAP_BASE = 2026081702
ADDRESS_CAP = 8 * 1024**3


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_values() -> tuple[np.ndarray, float]:
    raw = json.loads(CERTIFICATE.read_text())
    a = [Fraction(value) for value in raw["a"]]
    a0 = a[0]
    c = np.array([1.0] + [
        float(a[r] / a0 ** (2 * r + 1)) for r in range(1, 6)
    ])

    moments = [Fraction(value) for value in raw["mu"]]
    slope = moments[1] * moments[3] - moments[2] ** 2
    constant = (
        -moments[1] * moments[4] ** 2
        + 2 * moments[2] * moments[3] * moments[4]
        - moments[3] ** 3
    )
    mu5_threshold = -constant / slope
    a1, a2, a3, a4, a5 = a[1:]
    remainder = (
        -116 * a0**4 * a1 * a5 - 92 * a0**4 * a2 * a4
        - 42 * a0**4 * a3**2 + 546 * a0**3 * a1**2 * a4
        + 884 * a0**3 * a1 * a2 * a3 + 130 * a0**3 * a2**3
        - 1820 * a0**2 * a1**3 * a3 - 2366 * a0**2 * a1**2 * a2**2
        + 5005 * a0 * a1**4 * a2 - 2184 * a1**6
    )
    a6_threshold = (-mu5_threshold * a0**17 - remainder) / (13 * a0**5)
    return c, float(a6_threshold / a0**13)


def adjacent_ratios(width: int) -> tuple[np.ndarray, np.ndarray]:
    ratios = np.empty((COUNT, 6), dtype=np.float64)
    linear = np.empty(COUNT, dtype=np.float64)
    for index in range(COUNT):
        seed = np.random.SeedSequence([SEED_BASE, width, index]).generate_state(
            1, dtype=np.uint64
        )[0]
        jet = feature_jet(width, 13, 1.0, int(seed))
        a0n = jet[1]
        if not np.isfinite(a0n) or a0n <= 0:
            raise RuntimeError(f"invalid a0 at width={width}, index={index}")
        linear[index] = a0n
        c = np.ones(7, dtype=np.float64)
        for r in range(1, 7):
            c[r] = jet[2 * r + 1] / a0n ** (2 * r + 1)
        ratios[index] = c[1:] / c[:-1]
        if not np.all(np.isfinite(ratios[index])) or np.any(ratios[index] <= 0):
            raise RuntimeError(f"invalid ratio at width={width}, index={index}")
        if (index + 1) % 64 == 0:
            print(f"width={width} completed={index + 1}/{COUNT}", flush=True)
    return ratios, linear


def estimates(ratios: np.ndarray, exact: np.ndarray) -> np.ndarray:
    medians = np.median(ratios, axis=0)
    out = np.empty(5, dtype=np.float64)  # c2,...,c6
    for r in range(2, 7):
        out[r - 2] = (
            exact[r - 1] * (exact[r - 1] / exact[r - 2])
            * (medians[r - 1] / medians[r - 2])
        )
    return out


def bootstrap(ratios: np.ndarray, exact: np.ndarray, width: int) -> np.ndarray:
    rng = np.random.default_rng(np.random.SeedSequence([BOOTSTRAP_BASE, width]))
    out = np.empty((BOOTSTRAPS, 5), dtype=np.float64)
    for b in range(BOOTSTRAPS):
        indices = rng.integers(0, len(ratios), len(ratios))
        out[b] = estimates(ratios[indices], exact)
    return out


def main() -> None:
    resource.setrlimit(resource.RLIMIT_AS, (ADDRESS_CAP, ADDRESS_CAP))
    OUT.mkdir(parents=True, exist_ok=True)
    exact, threshold = exact_values()
    result: dict = {
        "design": {
            "widths": WIDTHS, "count_each": COUNT, "bootstraps": BOOTSTRAPS,
            "seed_rule": [SEED_BASE, "width", "zero_based_index"],
            "bootstrap_seed_rule": [BOOTSTRAP_BASE, "width"],
            "address_cap": ADDRESS_CAP,
            "thread_environment": {key: os.environ.get(key) for key in (
                "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
        },
        "provenance": {
            "protocol_sha256": sha256(PROTOCOL),
            "script_sha256": sha256(Path(__file__)),
            "finite_width_recurrence_sha256": sha256(
                PEELING / "finite_width_jet_reference.py"),
            "certificate_sha256": sha256(CERTIFICATE),
            "python": platform.python_version(), "numpy": np.__version__,
        },
        "exact_c0_through_c5": exact.tolist(),
        "c6_hankel_threshold": threshold,
        "widths": {},
    }

    points = {}
    intervals = {}
    for width in WIDTHS:
        ratios, linear = adjacent_ratios(width)
        point = estimates(ratios, exact)
        boots = bootstrap(ratios, exact, width)
        interval = np.quantile(boots, [0.025, 0.975], axis=0).T
        points[width] = point
        intervals[width] = interval
        np.savez_compressed(OUT / f"ratios_width_{width}.npz",
                            ratios=ratios, linear=linear)
        np.savez_compressed(OUT / f"bootstrap_width_{width}.npz", estimates=boots)
        result["widths"][str(width)] = {
            "linear_median": float(np.median(linear)),
            "ratio_medians": np.median(ratios, axis=0).tolist(),
            "estimates_c2_through_c6": point.tolist(),
            "intervals_c2_through_c6": interval.tolist(),
        }

    contain = all(
        intervals[width][r - 2, 0] <= exact[r] <= intervals[width][r - 2, 1]
        for width in WIDTHS for r in range(2, 6)
    )
    relative = all(
        abs(points[width][r - 2] / exact[r] - 1.0) <= 0.05
        for width in WIDTHS for r in range(3, 6)
    )
    cross = abs(points[128][4] - points[256][4]) / (
        0.5 * (points[128][4] + points[256][4])
    ) <= 0.10
    checks = {
        "c2_through_c5_intervals_contain_exact_both_widths": contain,
        "c3_through_c5_point_relative_error_at_most_5pct": relative,
        "c6_cross_width_relative_difference_at_most_10pct": bool(cross),
    }
    calibrated = all(checks.values())
    upper_below = all(intervals[width][4, 1] < threshold for width in WIDTHS)
    lower_above = all(intervals[width][4, 0] > threshold for width in WIDTHS)
    if not calibrated:
        status = "uncalibrated_inconclusive"
    elif upper_below:
        status = "empirical_positive_side_signal"
    elif lower_above:
        status = "empirical_negative_side_signal"
    else:
        status = "order13_inconclusive"
    result["calibration_checks"] = checks
    result["status"] = status
    result["peak_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    encoded = json.dumps(result, indent=2) + "\n"
    (OUT / "results.json").write_text(encoded)
    (OUT / "run_command.txt").write_text(
        "OPENBLAS_NUM_THREADS=4 OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 "
        "python studies/stieltjes_conjecture/numerics/finite_width/"
        "run_fresh_calibrated_ratio.py\n")
    print(encoded)


if __name__ == "__main__":
    main()
