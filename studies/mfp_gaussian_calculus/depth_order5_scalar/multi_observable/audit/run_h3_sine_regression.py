"""Execute the frozen hostile H=3 normalized-sine panel.

The audit contract has only three widths, so its requested affine-versus-
quadratic curvature gate is saturated and the confirmatory decision is forced
to ``inconclusive``.  The numerical panel is still run exactly as frozen and
its z-scores are retained as non-confirmatory evidence.
"""

from __future__ import annotations

import hashlib
import json
from math import exp, sqrt
from pathlib import Path

import numpy as np
from scipy.stats import chi2

from studies.mean_field_peeling.generic_first_stieltjes.depth.model import sample_state
from studies.mean_field_peeling.generic_first_stieltjes.depth_order5_scalar.multi_observable.independent_route_a.finite_width_hidden import (
    feature_ascent_hidden_jet,
)
from studies.mean_field_peeling.generic_first_stieltjes.depth_order5_scalar.multi_observable.independent_route_a.numeric_head import (
    compile_numeric,
    normalized_sine_moment,
)


HERE = Path(__file__).resolve().parent
WIDTHS = (64, 128, 256)
REPLICATES = 1024
SEED_FORMULA = "19000000 + 100000*width + replicate"


def oracle(order, value):
    normalization = sqrt((1.0 - exp(-2.0)) / 2.0)
    return np.sin(value + order * np.pi / 2.0) / normalization


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def affine_fit(widths, means, sems):
    design = np.column_stack((np.ones_like(widths), 1.0 / widths))
    weight = 1.0 / sems**2
    normal = design.T @ (weight[:, None] * design)
    covariance = np.linalg.inv(normal)
    coefficient = covariance @ (design.T @ (weight * means))
    residual = (means - design @ coefficient) / sems
    chi_square = float(residual @ residual)
    return {
        "intercept": float(coefficient[0]),
        "slope": float(coefficient[1]),
        "intercept_se": float(sqrt(covariance[0, 0])),
        "chi_square": chi_square,
        "degrees_of_freedom": 1,
        "goodness_p": float(chi2.sf(chi_square, 1)),
    }


def run():
    prediction = compile_numeric(3, normalized_sine_moment(96))
    names = ("layer2_gamma04", "layer2_q4", "layer3_gamma04", "layer3_q4")
    expected = {
        "layer2_gamma04": float(prediction["layers"][2]["Gamma04"]),
        "layer2_q4": float(prediction["layers"][2]["Q4"]),
        "layer3_gamma04": float(prediction["layers"][3]["Gamma04"]),
        "layer3_q4": float(prediction["layers"][3]["Q4"]),
    }
    raw = np.zeros((len(WIDTHS), REPLICATES, len(names)), dtype=np.float64)
    maximum_identity_residual = 0.0
    for width_index, width in enumerate(WIDTHS):
        for replicate in range(REPLICATES):
            seed = 19_000_000 + 100_000 * width + replicate
            state = sample_state(width, np.asarray([[1.0]]), 3, seed)
            jet = feature_ascent_hidden_jet(
                state,
                np.asarray([[1.0]]),
                np.asarray([1.0]),
                oracle,
                order=4,
            )
            for layer in (1, 2):
                rhs = (
                    2.0 * jet.gamma[layer][0, 4]
                    + 8.0 * jet.gamma[layer][1, 3]
                    + 6.0 * jet.gamma[layer][2, 2]
                )
                q4 = jet.q_derivatives[layer, 4]
                maximum_identity_residual = max(
                    maximum_identity_residual,
                    abs(q4 - rhs) / max(1.0, abs(q4), abs(rhs)),
                )
            raw[width_index, replicate] = (
                jet.gamma[1][0, 4],
                jet.q_derivatives[1, 4],
                jet.gamma[2][0, 4],
                jet.q_derivatives[2, 4],
            )

    raw_path = HERE / "H3_NORMALIZED_SINE_RAW.npz"
    np.savez_compressed(
        raw_path,
        widths=np.asarray(WIDTHS),
        names=np.asarray(names),
        values=raw,
    )
    means = raw.mean(axis=1)
    sems = raw.std(axis=1, ddof=1) / sqrt(REPLICATES)
    fits = {}
    for index, name in enumerate(names):
        fit = affine_fit(np.asarray(WIDTHS, dtype=float), means[:, index], sems[:, index])
        fit["prediction"] = expected[name]
        fit["z"] = (fit["intercept"] - expected[name]) / fit["intercept_se"]
        fits[name] = fit

    result = {
        "decision": "inconclusive",
        "decision_reason": (
            "the frozen three-width design cannot evaluate its required 1/n^2 "
            "curvature gate: the three-parameter quadratic fit is saturated"
        ),
        "activation": "sin(x)/sqrt((1-exp(-2))/2)",
        "hidden_layers": 3,
        "observed_layers": [2, 3],
        "widths": list(WIDTHS),
        "replicates_per_width": REPLICATES,
        "seed_formula": SEED_FORMULA,
        "prediction": expected,
        "means": {name: means[:, i].tolist() for i, name in enumerate(names)},
        "standard_errors": {name: sems[:, i].tolist() for i, name in enumerate(names)},
        "fits": fits,
        "maximum_finite_width_identity_relative_residual": maximum_identity_residual,
        "identity_tolerance": 1e-9,
        "identity_gate_pass": maximum_identity_residual <= 1e-9,
        "nonfinite_count": int((~np.isfinite(raw)).sum()),
        "raw_path": raw_path.name,
        "raw_sha256": digest(raw_path),
    }
    result_path = HERE / "H3_NORMALIZED_SINE_RESULT.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))

