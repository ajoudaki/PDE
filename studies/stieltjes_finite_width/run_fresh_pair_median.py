#!/usr/bin/env python3
"""Fresh-seed, initialization-only pair-median calibration experiment."""

from __future__ import annotations

# These must be set before importing NumPy.  The process also installs an
# address-space rlimit in main(), independently of the shell environment.
import os

for _name in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "NUMEXPR_NUM_THREADS",
    "BLIS_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
):
    os.environ[_name] = "6"

import hashlib
import json
import math
import platform
import resource
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from jet_control_variate import taylor_jet  # noqa: E402


WIDTHS = (128, 256)
PAIR_COUNT = 224
BATCH_PAIRS = 8
PAIR_SEED_BASE = 91723651
BOOTSTRAP_SEED_BASE = 410927
BOOTSTRAPS = 10_000
THREAD_CAP = 6
ADDRESS_SPACE_CAP = 8 * 1024**3
G0 = 111.0
G2 = 842592.0
EXACT_Q_NUMERATOR = -38443196932
EXACT_Q_DENOMINATOR = 5616860517
EXACT_Q = EXACT_Q_NUMERATOR / EXACT_Q_DENOMINATOR
OUTPUT = HERE / "runs/fresh_pair_median_run"
PROTOCOL = HERE / "FRESH_PAIR_MEDIAN_PROTOCOL.md"


@dataclass
class State:
    a: np.ndarray
    W: np.ndarray
    u: np.ndarray


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def install_memory_limit() -> None:
    old_soft, old_hard = resource.getrlimit(resource.RLIMIT_AS)
    hard = ADDRESS_SPACE_CAP if old_hard == resource.RLIM_INFINITY else min(
        old_hard, ADDRESS_SPACE_CAP
    )
    soft = min(hard, ADDRESS_SPACE_CAP)
    resource.setrlimit(resource.RLIMIT_AS, (soft, hard))


def generate_batch(width: int, first: int, count: int) -> State:
    """Generate independent pairs under the frozen seed rule."""
    a0 = np.empty((count, width), dtype=np.float64)
    u0 = np.empty_like(a0)
    W0 = np.empty((count, width, width), dtype=np.float64)
    for local, pair_index in enumerate(range(first, first + count)):
        rng = np.random.default_rng(
            np.random.SeedSequence([PAIR_SEED_BASE, width, pair_index])
        )
        a0[local] = rng.standard_normal(width)
        u0[local] = rng.standard_normal(width)
        W0[local] = rng.standard_normal((width, width))
    a = np.stack((a0, -a0), axis=1).reshape(2 * count, width)
    u = np.repeat(u0[:, None, :], 2, axis=1).reshape(2 * count, width)
    W = np.repeat(W0[:, None, :, :], 2, axis=1).reshape(
        2 * count, width, width
    )
    return State(a=a, W=W, u=u)


def pair_statistics(width: int) -> tuple[np.ndarray, np.ndarray]:
    """Return the pair-averaged f5 jet and transformed held-out statistic."""
    f5 = np.empty(PAIR_COUNT, dtype=np.float64)
    for first in range(0, PAIR_COUNT, BATCH_PAIRS):
        count = min(BATCH_PAIRS, PAIR_COUNT - first)
        state = generate_batch(width, first, count)
        jet = taylor_jet(state, order=5)
        paired = jet.reshape(count, 2, 6).mean(axis=1)
        f5[first : first + count] = paired[:, 5]
        print(
            f"width={width} completed={first + count}/{PAIR_COUNT}",
            flush=True,
        )
    base = 2.0 * G2**2 / (3.0 * G0**5)
    q = 5.0 * f5 / G0**4 - base
    return f5, q


def exact_median_interval(values: np.ndarray, alpha: float = 0.05) -> dict:
    """Exact distribution-free two-sided interval for a continuous median."""
    ordered = np.sort(values)
    n = len(ordered)
    denominator = 2**n
    cumulative = 0
    k = 0
    # k is one-based in the mathematical interval.  Select the largest k
    # for which the two-sided noncoverage probability is at most alpha.
    for candidate in range(1, n // 2 + 1):
        cumulative += math.comb(n, candidate - 1)
        noncoverage = 2.0 * cumulative / denominator
        if noncoverage <= alpha:
            k = candidate
        else:
            break
    if k == 0:
        raise RuntimeError("sample too small for requested median interval")
    lower = float(ordered[k - 1])
    upper = float(ordered[n - k])
    coverage = 1.0 - 2.0 * cumulative_without_last(n, k - 1) / denominator
    return {
        "alpha": alpha,
        "k_one_based": k,
        "lower_order_statistic": k,
        "upper_order_statistic": n - k + 1,
        "lower": lower,
        "upper": upper,
        "width": upper - lower,
        "exact_coverage": coverage,
    }


def cumulative_without_last(n: int, maximum: int) -> int:
    return sum(math.comb(n, j) for j in range(maximum + 1))


def bootstrap_interval(values: np.ndarray, width: int) -> dict:
    rng = np.random.default_rng(
        np.random.SeedSequence([BOOTSTRAP_SEED_BASE, width])
    )
    medians = np.empty(BOOTSTRAPS, dtype=np.float64)
    chunk = 500
    for first in range(0, BOOTSTRAPS, chunk):
        count = min(chunk, BOOTSTRAPS - first)
        indices = rng.integers(0, len(values), size=(count, len(values)))
        medians[first : first + count] = np.median(values[indices], axis=1)
    return {
        "replicates": BOOTSTRAPS,
        "lower": float(np.quantile(medians, 0.025)),
        "upper": float(np.quantile(medians, 0.975)),
        "median": float(np.median(medians)),
        "standard_deviation": float(np.std(medians, ddof=1)),
    }


def summarize(values: np.ndarray, width: int) -> dict:
    exact_ci = exact_median_interval(values)
    estimate = float(np.median(values))
    return {
        "width": width,
        "pair_count": len(values),
        "estimate": estimate,
        "estimate_minus_exact": estimate - EXACT_Q,
        "negative_estimate": estimate < 0.0,
        "exact_in_primary_interval": exact_ci["lower"] <= EXACT_Q <= exact_ci["upper"],
        "primary_exact_interval": exact_ci,
        "secondary_bootstrap_interval": bootstrap_interval(values, width),
        "sample_quantiles": {
            str(q): float(np.quantile(values, q))
            for q in (0.0, 0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99, 1.0)
        },
    }


def classify(summaries: dict[str, dict]) -> tuple[str, dict]:
    s128 = summaries["128"]
    s256 = summaries["256"]
    ci256 = s256["primary_exact_interval"]
    checks = {
        "n256_interval_contains_exact": s256["exact_in_primary_interval"],
        "n256_interval_width_at_most_10": ci256["width"] <= 10.0,
        "n128_interval_contains_exact": s128["exact_in_primary_interval"],
        "both_estimates_negative": s128["estimate"] < 0.0 and s256["estimate"] < 0.0,
        "both_estimates_within_5_of_exact": (
            abs(s128["estimate"] - EXACT_Q) <= 5.0
            and abs(s256["estimate"] - EXACT_Q) <= 5.0
        ),
        "cross_width_difference_at_most_5": abs(
            s128["estimate"] - s256["estimate"]
        ) <= 5.0,
    }
    if all(checks.values()):
        return "pass", checks
    if checks["n256_interval_contains_exact"] and not checks[
        "n256_interval_width_at_most_10"
    ]:
        return "underpowered_inconclusive", checks
    return "calibration_failure", checks


def main() -> None:
    install_memory_limit()
    OUTPUT.mkdir(exist_ok=False)
    script = Path(__file__).resolve()
    results: dict[str, object] = {
        "status": "running",
        "frozen_design": {
            "widths": list(WIDTHS),
            "pair_count_each": PAIR_COUNT,
            "batch_pairs": BATCH_PAIRS,
            "pair_seed_rule": [PAIR_SEED_BASE, "width", "zero_based_pair_index"],
            "bootstrap_seed_rule": [BOOTSTRAP_SEED_BASE, "width"],
            "bootstraps": BOOTSTRAPS,
            "thread_cap": THREAD_CAP,
            "address_space_cap_bytes": ADDRESS_SPACE_CAP,
        },
        "exact_target": {
            "numerator": EXACT_Q_NUMERATOR,
            "denominator": EXACT_Q_DENOMINATOR,
            "decimal": EXACT_Q,
        },
        "provenance": {
            "protocol_sha256": sha256(PROTOCOL),
            "script_sha256": sha256(script),
            "python": sys.version,
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "widths": {},
    }
    for width in WIDTHS:
        f5, q = pair_statistics(width)
        np.savez_compressed(OUTPUT / f"pair_values_width_{width}.npz", f5=f5, q=q)
        results["widths"][str(width)] = summarize(q, width)
    classification, checks = classify(results["widths"])
    results["status"] = classification
    results["gate_checks"] = checks
    # Linux reports ru_maxrss in KiB.
    results["peak_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    (OUTPUT / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({"status": classification, "checks": checks}, indent=2))
    print("No positive-time trajectories were simulated.")


if __name__ == "__main__":
    main()
