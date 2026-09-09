"""Execute the frozen normalized-sine finite-width regression contract."""

from __future__ import annotations

import hashlib
import json
from math import exp, sqrt
from pathlib import Path

import numpy as np
from scipy.stats import chi2

from studies._output_paths import StudyPaths

PATHS = StudyPaths(__file__)

from ....depth.model import sample_state
from .finite_width_hidden import feature_ascent_hidden_jet
from .numeric_head import compile_numeric, normalized_sine_moment


HERE = Path(__file__).resolve().parent
WIDTHS = (32, 64, 128, 256)
REPLICATES = 2000


def oracle(order: int, value: np.ndarray) -> np.ndarray:
    normalization = sqrt((1.0 - exp(-2.0)) / 2.0)
    return np.sin(value + order * np.pi / 2.0) / normalization


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def weighted_affine(widths: np.ndarray, means: np.ndarray, sems: np.ndarray):
    design = np.column_stack((np.ones_like(widths), 1.0 / widths))
    weight = 1.0 / sems**2
    normal = design.T @ (weight[:, None] * design)
    covariance = np.linalg.inv(normal)
    coefficient = covariance @ (design.T @ (weight * means))
    residual = (means - design @ coefficient) / sems
    chi_square = float(residual @ residual)
    degrees = int(widths.size - 2)
    return {
        "intercept": float(coefficient[0]),
        "slope": float(coefficient[1]),
        "intercept_se": float(sqrt(covariance[0, 0])),
        "chi_square": chi_square,
        "degrees_of_freedom": degrees,
        "goodness_p": float(chi2.sf(chi_square, degrees)),
    }


def run(*, output_dir=None) -> dict[str, object]:
    output_dir = PATHS.require_output(output_dir or PATHS.input_dir())
    prediction = compile_numeric(2, normalized_sine_moment(96))
    expected = {
        "layer1_q2": float(prediction["layers"][1]["Q2"]),
        "layer1_q4": float(prediction["layers"][1]["Q4"]),
        "layer1_gamma04": float(prediction["layers"][1]["Gamma04"]),
        "layer2_q2": float(prediction["layers"][2]["Q2"]),
        "layer2_q4": float(prediction["layers"][2]["Q4"]),
        "layer2_gamma04": float(prediction["layers"][2]["Gamma04"]),
    }
    raw = np.zeros((len(WIDTHS), REPLICATES, len(expected)), dtype=np.float64)
    names = tuple(expected)
    for width_index, width in enumerate(WIDTHS):
        for replicate in range(REPLICATES):
            seed = 17_000_000 + 100_000 * width + replicate
            state = sample_state(width, np.asarray([[1.0]]), 2, seed)
            jet = feature_ascent_hidden_jet(
                state,
                np.asarray([[1.0]]),
                np.asarray([1.0]),
                oracle,
                order=4,
            )
            values = {
                "layer1_q2": jet.q_derivatives[0, 2],
                "layer1_q4": jet.q_derivatives[0, 4],
                "layer1_gamma04": jet.gamma[0][0, 4],
                "layer2_q2": jet.q_derivatives[1, 2],
                "layer2_q4": jet.q_derivatives[1, 4],
                "layer2_gamma04": jet.gamma[1][0, 4],
            }
            raw[width_index, replicate] = [values[name] for name in names]

    output_dir.mkdir(parents=True, exist_ok=True)
    raw_path = output_dir / "NORMALIZED_SINE_GAMMA04_RAW.npz"
    np.savez_compressed(raw_path, widths=np.asarray(WIDTHS), names=names, values=raw)
    means = raw.mean(axis=1)
    sems = raw.std(axis=1, ddof=1) / sqrt(REPLICATES)
    fits = {}
    for index, name in enumerate(names):
        fit = weighted_affine(np.asarray(WIDTHS, dtype=float), means[:, index], sems[:, index])
        fit["prediction"] = expected[name]
        fit["z"] = (fit["intercept"] - expected[name]) / fit["intercept_se"]
        fits[name] = fit
    primary = fits["layer2_q4"]
    if abs(primary["z"]) <= 3 and primary["goodness_p"] >= 0.01:
        decision = "pass"
    elif abs(primary["z"]) >= 5 and primary["goodness_p"] >= 0.01:
        decision = "fail"
    else:
        decision = "inconclusive"
    result = {
        "contract": "NONPOLYNOMIAL_EXPERIMENT_CONTRACT.md",
        "activation": "sin(x)/sqrt((1-exp(-2))/2)",
        "hidden_layers": 2,
        "widths": list(WIDTHS),
        "replicates_per_width": REPLICATES,
        "prediction": expected,
        "means": {name: means[:, i].tolist() for i, name in enumerate(names)},
        "standard_errors": {name: sems[:, i].tolist() for i, name in enumerate(names)},
        "fits": fits,
        "primary": "layer2_q4",
        "decision": decision,
        "nonfinite_count": int((~np.isfinite(raw)).sum()),
        "raw_path": raw_path.name,
        "raw_sha256": digest(raw_path),
        "source_sha256": {
            name: digest(HERE / name)
            for name in (
                "gamma04_contraction.py",
                "finite_width_hidden.py",
                "numeric_head.py",
                "run_sine_regression.py",
                "FROZEN_GAMMA04_RECURRENCE.json",
            )
        },
        "command": (
            "python -m studies.mfp_gaussian_calculus."
            "depth_order5_scalar.multi_observable.independent_route_a."
            "run_sine_regression"
        ),
    }
    path = output_dir / "NORMALIZED_SINE_GAMMA04_RESULT.json"
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


if __name__ == "__main__":
    args = PATHS.parse()
    print(json.dumps(run(output_dir=args.output_dir), indent=2, sort_keys=True))
