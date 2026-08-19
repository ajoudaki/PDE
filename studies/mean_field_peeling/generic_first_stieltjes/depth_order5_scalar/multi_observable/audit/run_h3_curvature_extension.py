"""Run the pre-results width-512 extension of the hostile H=3 sine panel."""

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
OLD_RAW = HERE / "H3_NORMALIZED_SINE_RAW.npz"
OLD_SHA256 = "d99931b2976f87f2c40988399555d08ab203893d9e77107a546f62b49b95faef"
WIDTHS = (64, 128, 256, 512)
REPLICATES = 1024
NAMES = ("layer2_gamma04", "layer2_q4", "layer3_gamma04", "layer3_q4")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def oracle(order, value):
    normalization = sqrt((1.0 - exp(-2.0)) / 2.0)
    return np.sin(value + order * np.pi / 2.0) / normalization


def fit(widths, means, sems, quadratic: bool):
    columns = [np.ones_like(widths), 1.0 / widths]
    if quadratic:
        columns.append(1.0 / widths**2)
    design = np.column_stack(columns)
    weight = 1.0 / sems**2
    normal = design.T @ (weight[:, None] * design)
    covariance = np.linalg.inv(normal)
    coefficient = covariance @ (design.T @ (weight * means))
    residual = (means - design @ coefficient) / sems
    degrees = len(widths) - len(columns)
    chi_square = float(residual @ residual)
    return {
        "coefficients": coefficient.tolist(),
        "coefficient_se": np.sqrt(np.diag(covariance)).tolist(),
        "intercept": float(coefficient[0]),
        "intercept_se": float(sqrt(covariance[0, 0])),
        "chi_square": chi_square,
        "degrees_of_freedom": degrees,
        "goodness_p": float(chi2.sf(chi_square, degrees)) if degrees else None,
    }


def one_network(width: int, replicate: int):
    seed = (
        19_000_000 + 100_000 * width + replicate
        if width < 512
        else 23_000_000 + replicate
    )
    state = sample_state(width, np.asarray([[1.0]]), 3, seed)
    jet = feature_ascent_hidden_jet(
        state, np.asarray([[1.0]]), np.asarray([1.0]), oracle, order=4
    )
    maximum_residual = 0.0
    for layer in (1, 2):
        rhs = (
            2.0 * jet.gamma[layer][0, 4]
            + 8.0 * jet.gamma[layer][1, 3]
            + 6.0 * jet.gamma[layer][2, 2]
        )
        q4 = jet.q_derivatives[layer, 4]
        maximum_residual = max(
            maximum_residual,
            abs(q4 - rhs) / max(1.0, abs(q4), abs(rhs)),
        )
    values = np.asarray(
        (
            jet.gamma[1][0, 4], jet.q_derivatives[1, 4],
            jet.gamma[2][0, 4], jet.q_derivatives[2, 4],
        ),
        dtype=np.float64,
    )
    return values, maximum_residual


def run():
    if digest(OLD_RAW) != OLD_SHA256:
        raise RuntimeError("the frozen three-width raw panel changed")
    old = np.load(OLD_RAW, allow_pickle=False)
    if tuple(old["widths"].tolist()) != WIDTHS[:3] or tuple(old["names"].tolist()) != NAMES:
        raise RuntimeError("unexpected old-panel schema")
    old_values = old["values"]
    combined = np.empty((len(WIDTHS), REPLICATES, len(NAMES)), dtype=np.float64)
    combined[:3] = old_values
    maximum_identity_residual = 0.0
    maximum_old_reproduction_error = 0.0
    for width_index, width in enumerate(WIDTHS):
        for replicate in range(REPLICATES):
            values, residual = one_network(width, replicate)
            maximum_identity_residual = max(maximum_identity_residual, residual)
            if width < 512:
                reference = old_values[width_index, replicate]
                maximum_old_reproduction_error = max(
                    maximum_old_reproduction_error,
                    float(np.max(np.abs(values - reference) / np.maximum(1.0, np.maximum(np.abs(values), np.abs(reference))))),
                )
            else:
                combined[width_index, replicate] = values

    raw_path = HERE / "H3_NORMALIZED_SINE_CURVATURE_EXTENSION_RAW.npz"
    np.savez_compressed(
        raw_path,
        widths=np.asarray(WIDTHS),
        names=np.asarray(NAMES),
        values=combined,
    )
    means = combined.mean(axis=1)
    sems = combined.std(axis=1, ddof=1) / sqrt(REPLICATES)
    prediction = compile_numeric(3, normalized_sine_moment(96))
    targets = {
        "layer2_gamma04": float(prediction["layers"][2]["Gamma04"]),
        "layer2_q4": float(prediction["layers"][2]["Q4"]),
        "layer3_gamma04": float(prediction["layers"][3]["Gamma04"]),
        "layer3_q4": float(prediction["layers"][3]["Q4"]),
    }
    fits = {}
    for index, name in enumerate(NAMES):
        affine = fit(np.asarray(WIDTHS, dtype=float), means[:, index], sems[:, index], False)
        quadratic = fit(np.asarray(WIDTHS, dtype=float), means[:, index], sems[:, index], True)
        affine["prediction"] = targets[name]
        affine["z"] = (affine["intercept"] - targets[name]) / affine["intercept_se"]
        curvature_z = quadratic["coefficients"][2] / quadratic["coefficient_se"][2]
        intercept_shift = quadratic["intercept"] - affine["intercept"]
        shift_threshold = 2.0 * max(affine["intercept_se"], quadratic["intercept_se"])
        resolved_material_curvature = abs(curvature_z) > 2.0 and abs(intercept_shift) > shift_threshold
        fits[name] = {
            "affine": affine,
            "quadratic": quadratic,
            "curvature_z": curvature_z,
            "intercept_shift": intercept_shift,
            "intercept_shift_threshold": shift_threshold,
            "resolved_material_curvature": bool(resolved_material_curvature),
            "se_gate": bool(affine["intercept_se"] <= 0.10 * max(1.0, abs(targets[name]))),
        }

    nonfinite = int((~np.isfinite(combined)).sum())
    z_values = [abs(value["affine"]["z"]) for value in fits.values()]
    replication_required = any(3.0 < value <= 6.0 for value in z_values)
    validity = {
        "identity": maximum_identity_residual <= 1e-9,
        "old_reproduction": maximum_old_reproduction_error <= 1e-12,
        "finite": nonfinite == 0,
        "standard_errors": all(value["se_gate"] for value in fits.values()),
        "curvature": not any(value["resolved_material_curvature"] for value in fits.values()),
    }
    if not all(validity.values()):
        decision = "inconclusive"
        reason = "one or more preregistered validity/curvature gates failed"
    elif replication_required:
        decision = "replication_required"
        reason = "at least one primary affine z lies in (3,6]"
    elif all(value <= 4.0 for value in z_values):
        decision = "pass"
        reason = "all validity, curvature, standard-error, and z gates passed"
    else:
        decision = "inconclusive"
        reason = "a primary affine z exceeds 4"

    result = {
        "decision": decision,
        "decision_reason": reason,
        "contract": "H3_CURVATURE_EXTENSION_CONTRACT.md",
        "activation": "sin(x)/sqrt((1-exp(-2))/2)",
        "hidden_layers": 3,
        "observed_layers": [2, 3],
        "widths": list(WIDTHS),
        "replicates_per_width": REPLICATES,
        "new_width_seed_formula": "23000000 + replicate",
        "prediction": targets,
        "means": {name: means[:, i].tolist() for i, name in enumerate(NAMES)},
        "standard_errors": {name: sems[:, i].tolist() for i, name in enumerate(NAMES)},
        "fits": fits,
        "validity_gates": validity,
        "maximum_finite_width_identity_relative_residual": maximum_identity_residual,
        "maximum_old_reproduction_scaled_error": maximum_old_reproduction_error,
        "nonfinite_count": nonfinite,
        "replication_required": replication_required,
        "raw_path": raw_path.name,
        "raw_sha256": digest(raw_path),
        "old_raw_sha256": OLD_SHA256,
    }
    result_path = HERE / "H3_NORMALIZED_SINE_CURVATURE_EXTENSION_RESULT.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
