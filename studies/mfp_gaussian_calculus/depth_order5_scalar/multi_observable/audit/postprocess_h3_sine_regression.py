"""Deterministically postprocess the frozen H3 raw panel after JSON failure."""

from __future__ import annotations

import hashlib
import json
from math import sqrt
from pathlib import Path

import numpy as np
from scipy.stats import chi2

from studies.mean_field_peeling.generic_first_stieltjes.depth_order5_scalar.multi_observable.independent_route_a.numeric_head import (
    compile_numeric,
    normalized_sine_moment,
)


HERE = Path(__file__).resolve().parent
RAW = HERE / "H3_NORMALIZED_SINE_RAW.npz"
EXPECTED_RAW_SHA256 = "d99931b2976f87f2c40988399555d08ab203893d9e77107a546f62b49b95faef"


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
    if digest(RAW) != EXPECTED_RAW_SHA256:
        raise RuntimeError("raw H3 panel hash changed")
    payload = np.load(RAW, allow_pickle=False)
    widths = payload["widths"].astype(float)
    names = tuple(str(value) for value in payload["names"])
    raw = payload["values"]
    prediction = compile_numeric(3, normalized_sine_moment(96))
    expected = {
        "layer2_gamma04": float(prediction["layers"][2]["Gamma04"]),
        "layer2_q4": float(prediction["layers"][2]["Q4"]),
        "layer3_gamma04": float(prediction["layers"][3]["Gamma04"]),
        "layer3_q4": float(prediction["layers"][3]["Q4"]),
    }
    means = raw.mean(axis=1)
    sems = raw.std(axis=1, ddof=1) / sqrt(raw.shape[1])
    fits = {}
    for index, name in enumerate(names):
        fit = affine_fit(widths, means[:, index], sems[:, index])
        fit["prediction"] = expected[name]
        fit["z"] = (fit["intercept"] - expected[name]) / fit["intercept_se"]
        fits[name] = fit
    result = {
        "decision": "inconclusive",
        "decision_reason": (
            "three widths saturate the required intercept+1/n+1/n^2 "
            "curvature comparison"
        ),
        "activation": "sin(x)/sqrt((1-exp(-2))/2)",
        "hidden_layers": 3,
        "observed_layers": [2, 3],
        "widths": widths.astype(int).tolist(),
        "replicates_per_width": int(raw.shape[1]),
        "seed_formula": "19000000 + 100000*width + replicate",
        "prediction": expected,
        "means": {name: means[:, i].tolist() for i, name in enumerate(names)},
        "standard_errors": {name: sems[:, i].tolist() for i, name in enumerate(names)},
        "fits": fits,
        "nonfinite_count": int((~np.isfinite(raw)).sum()),
        "raw_path": RAW.name,
        "raw_sha256": EXPECTED_RAW_SHA256,
        "runner_serialization_failure": (
            "the preregistered runner completed and wrote raw data, then failed "
            "because numpy.bool_ is not JSON serializable"
        ),
    }
    result_path = HERE / "H3_NORMALIZED_SINE_RESULT.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))

