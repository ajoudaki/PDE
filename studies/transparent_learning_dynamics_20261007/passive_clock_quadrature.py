#!/usr/bin/env python3
"""Initialization-only passive cubic-clock coefficients; no dense data input."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import resource
import sys
import time

# Set before importing NumPy/SciPy. This program deliberately has one thread.
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
              "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_name] = "1"
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))

import numpy as np
import scipy
from scipy.special import roots_hermitenorm


def gaussian_rule(order: int) -> tuple[np.ndarray, np.ndarray]:
    nodes, weights = roots_hermitenorm(order)
    weights = weights / math.sqrt(2.0 * math.pi)
    if abs(float(weights.sum()) - 1.0) > 1e-12:
        raise RuntimeError("Gaussian quadrature weights fail normalization.")
    return nodes, weights


def gate_fields(z: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    h = np.tanh(z)
    g = 1.0 - h * h
    second = -2.0 * h * g
    return h, g, second


def lower_moments(nodes: np.ndarray, weights: np.ndarray, rotated: bool):
    xx, yy = np.meshgrid(nodes, nodes, indexing="ij")
    xy = np.column_stack((xx.ravel(), yy.ravel()))
    if rotated:
        angle = math.pi / 7.0
        rotation = np.array([[math.cos(angle), -math.sin(angle)],
                             [math.sin(angle), math.cos(angle)]])
        xy = xy @ rotation.T
    x = np.column_stack((xy, (2.0 * xy[:, 0] + xy[:, 1]) / math.sqrt(5.0)))
    ww = np.outer(weights, weights).ravel()
    h, g, _ = gate_fields(x)
    gram_raw = h.T @ (ww[:, None] * h)
    gg = np.einsum("na,nj->naj", g, g[:, :2]).reshape(-1, 6)
    hh = np.einsum("nc,nd->ncd", h, h).reshape(-1, 9)
    gate_pair = (ww @ gg).reshape(3, 2)
    gate_feature = (gg.T @ (ww[:, None] * hh)).reshape(3, 2, 3, 3)
    return gram_raw, gate_pair, gate_feature


def upper_moments(nodes: np.ndarray, weights: np.ndarray,
                  covariance: np.ndarray, rotated: bool, deadline: float):
    factor = np.linalg.cholesky(covariance)
    if rotated:
        rotation, _ = np.linalg.qr(np.array([[1., 2., -1.],
                                            [2., -1., 2.],
                                            [1., 1., 1.]]))
        factor = factor @ rotation
    xx, yy = np.meshgrid(nodes, nodes, indexing="ij")
    yz = np.column_stack((xx.ravel(), yy.ravel()))
    pair_weights = np.outer(weights, weights).ravel()
    primitive = np.empty((len(pair_weights), 3), dtype=float)
    primitive[:, 1:] = yz
    features = np.zeros((3, 3))
    gates = np.zeros((3, 3))
    curvature_feature = np.zeros((3, 3))
    gaussian_covariance = np.zeros((3, 3))
    # E[g_a T_b g_j T_c], j,c restricted to training samples.
    fourth = np.zeros((3, 3, 2, 2))
    for node, weight in zip(nodes, weights):
        if time.monotonic() >= deadline:
            raise TimeoutError("Soft wall limit reached during quadrature.")
        primitive[:, 0] = node
        z = primitive @ factor.T
        h, g, second = gate_fields(z)
        ww = weight * pair_weights
        features += h.T @ (ww[:, None] * h)
        gates += g.T @ (ww[:, None] * g)
        curvature_feature += second.T @ (ww[:, None] * h)
        gaussian_covariance += z.T @ (ww[:, None] * z)
        gg = np.einsum("na,nj->naj", g, g[:, :2]).reshape(-1, 6)
        hh = np.einsum("nb,nc->nbc", h, h[:, :2]).reshape(-1, 6)
        fourth += (gg.T @ (ww[:, None] * hh)).reshape(3, 2, 3, 2).transpose(0, 2, 1, 3)
    return features, gates, curvature_feature, fourth, gaussian_covariance


def evaluate(order: int, rotated: bool, deadline: float) -> dict:
    nodes, weights = gaussian_rule(order)
    hx, gx, _ = gate_fields(nodes)
    sigma2 = float(weights @ (hx * hx))
    qx = float(weights @ (gx * gx))
    tau_x = float(weights @ (hx * hx * gx * gx))
    hz, gz, _ = gate_fields(math.sqrt(sigma2) * nodes)
    alpha = float(weights @ gz)
    beta = float(weights @ (gz * gz))
    nu = float(weights @ (hz * hz))
    tau = float(weights @ (hz * hz * gz * gz))
    r0 = 3.0 * beta - 2.0 * alpha
    b1 = sigma2 * qx * alpha**2
    b2 = (sigma2 + qx) * nu * beta + sigma2 * qx * alpha**4
    kappa = (2.0 / 3.0) * (
        (sigma2 + qx) * (tau + nu * beta)
        + r0**2 * tau_x + alpha**4 * qx * sigma2
    )
    lower_raw, lower_gg, lower_gg_hh = lower_moments(nodes, weights, rotated)
    covariance = lower_raw.copy()
    np.fill_diagonal(covariance, sigma2)
    covariance[0, 1] = covariance[1, 0] = 0.0
    eigenvalues = np.linalg.eigvalsh(covariance)
    if float(eigenvalues.min()) <= 1e-8:
        raise RuntimeError("Initial upper covariance is unexpectedly near singular.")
    top, top_gg, top_second_h, fourth, realized_covariance = upper_moments(
        nodes, weights, covariance, rotated, deadline
    )
    response_psi = np.zeros((3, 3, 3))
    for aa in range(3):
        for bb in range(3):
            response_psi[aa, bb, aa] += top_second_h[aa, bb]
            response_psi[aa, bb, bb] += top_gg[aa, bb]
    input_gram = np.array([[1., 0., 2. / math.sqrt(5.)],
                           [0., 1., 1. / math.sqrt(5.)],
                           [2. / math.sqrt(5.), 1. / math.sqrt(5.), 1.]])
    directions = {}
    identity_errors = []
    for sign in (-1, 1):
        labels = np.array([1.0, float(sign)])
        response_d = np.zeros((2, 3))
        response_d[:, :2] = np.array([[r0, sign * alpha**2],
                                      [alpha**2, sign * r0]])
        psi_d = np.einsum("abjc,c->abj", fourth, labels)
        middle = np.zeros((3, 3))
        lower_gaussian = np.zeros((3, 3))
        lower_reaction = np.zeros((3, 3))
        for aa in range(3):
            for bb in range(3):
                for jj in range(2):
                    middle[aa, bb] += (
                        labels[jj] * covariance[aa, jj] * psi_d[aa, bb, jj]
                    )
                    lower_gaussian[aa, bb] += (
                        labels[jj] * input_gram[aa, jj] * lower_gg[aa, jj]
                        * psi_d[aa, bb, jj]
                    )
                    lower_reaction[aa, bb] += (
                        labels[jj] * input_gram[aa, jj]
                        * np.einsum("c,d,cd->", response_d[jj],
                                    response_psi[aa, bb], lower_gg_hh[aa, jj])
                    )
        matrix = middle + lower_gaussian + lower_reaction
        cubic = 0.5 * matrix[:, :2] @ labels + (1.0 / 6.0) * labels @ matrix[:2, :]
        slope = float(top[2, :2] @ labels)
        component_cubic = {}
        for name, component in (("learned_middle", middle),
                                ("lower_gaussian_return", lower_gaussian),
                                ("lower_reaction_alignment", lower_reaction)):
            component_cubic[name] = float(
                0.5 * component[2, :2] @ labels
                + (1.0 / 6.0) * labels @ component[:2, 2]
            )
        identity_errors.extend([
            abs(float(cubic[0]) - kappa),
            abs(float(cubic[1]) - sign * kappa),
            abs(float(matrix[0, 1]) - sign * b2),
            abs(float(matrix[1, 0]) - sign * b2),
        ])
        directions[str(sign)] = {
            "k_linear": slope,
            "kappa_passive": float(cubic[2]),
            "kappa_passive_components": component_cubic,
            "training_cubic_from_matrix": cubic[:2].tolist(),
            "M": matrix.tolist(),
            "M_learned_middle": middle.tolist(),
            "M_lower_gaussian": lower_gaussian.tolist(),
            "M_lower_reaction": lower_reaction.tolist(),
        }
    return {
        "order": order, "rotated_coordinates": rotated,
        "constants": {"sigma2": sigma2, "q_X": qx, "alpha": alpha,
                      "beta": beta, "nu": nu, "kappa_training": kappa,
                      "b1": b1, "b2": b2},
        "passive_initial_similarities": top[2, :2].tolist(),
        "upper_initial_covariance": covariance.tolist(),
        "directions": directions,
        "checks": {
            "covariance_min_eigenvalue": float(eigenvalues.min()),
            "gaussian_covariance_error": float(np.max(np.abs(realized_covariance - covariance))),
            "lower_diagonal_error": float(np.max(np.abs(np.diag(lower_raw) - sigma2))),
            "lower_training_cross_error": abs(float(lower_raw[0, 1])),
            "training_identity_max_error": max(identity_errors),
        },
    }


def target_vector(result: dict) -> np.ndarray:
    return np.array([
        result["directions"][str(sign)][key]
        for sign in (-1, 1)
        for key in ("k_linear", "kappa_passive")
    ])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(f"Refusing to overwrite existing output directory: {args.output}")
    args.output.mkdir(parents=True)
    started = time.monotonic()
    deadline = started + 55.0
    threshold = 1e-7
    results = []
    status = "inconclusive"
    refinement = rotation = math.inf
    caught = None
    try:
        for order in (24, 40, 64, 96):
            result = evaluate(order, False, deadline)
            results.append(result)
            print(json.dumps({"stage": "unrotated", "order": order,
                              "targets": target_vector(result).tolist()}), flush=True)
        rotated = evaluate(96, True, deadline)
        results.append(rotated)
        refinement = float(np.max(np.abs(target_vector(results[3]) - target_vector(results[2]))))
        rotation = float(np.max(np.abs(target_vector(results[3]) - target_vector(rotated))))
        if max(refinement, rotation) > threshold and time.monotonic() - started < 35.0:
            fine = evaluate(128, False, deadline)
            results.append(fine)
            fine_rotated = evaluate(128, True, deadline)
            results.append(fine_rotated)
            refinement = float(np.max(np.abs(target_vector(fine) - target_vector(results[3]))))
            rotation = float(np.max(np.abs(target_vector(fine) - target_vector(fine_rotated))))
            frozen = fine
        else:
            frozen = results[3]
        numerical_checks = max(
            frozen["checks"]["training_identity_max_error"],
            frozen["checks"]["gaussian_covariance_error"],
            results[-1]["checks"]["training_identity_max_error"],
            results[-1]["checks"]["gaussian_covariance_error"],
        )
        if max(refinement, rotation) <= threshold and numerical_checks <= threshold:
            status = "pass_refinement_not_rigorous_error_bound"
    except (TimeoutError, MemoryError) as error:
        caught = repr(error)
        unrotated = [item for item in results if not item["rotated_coordinates"]]
        frozen = unrotated[-1] if unrotated else None
    elapsed = time.monotonic() - started
    script_path = Path(__file__).resolve()
    formula_path = script_path.with_name("ANALYTICAL_LEARNING_PROFILES.md")
    report = {
        "status": status,
        "configuration": {
            "input_training": [[1, 0], [0, 1]],
            "input_passive": [2 / math.sqrt(5), 1 / math.sqrt(5)],
            "label_directions": [[1, -1], [1, 1]],
            "base_orders": [24, 40, 64, 96],
            "fallback_order": 128, "absolute_refinement_gate": threshold,
            "soft_wall_seconds": 55, "cpu_limit_seconds": 60,
            "address_space_limit_mb": 512, "single_thread": True,
            "coefficient_provenance": "initialization Gaussian expectations only",
        },
        "refinement_error": refinement, "rotation_error": rotation,
        "frozen_order": None if frozen is None else frozen["order"],
        "frozen_coefficients": None if frozen is None else {
            sign: {key: values[key] for key in ("k_linear", "kappa_passive")}
            for sign, values in frozen["directions"].items()
        },
        "elapsed_seconds": elapsed,
        "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
        "error": caught,
        "source_sha256": hashlib.sha256(script_path.read_bytes()).hexdigest(),
        "formula_sha256": hashlib.sha256(formula_path.read_bytes()).hexdigest(),
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": scipy.__version__, "platform": platform.platform()},
        "results": results,
    }
    output_file = args.output / "coefficients.json"
    output_file.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    print(json.dumps({key: report[key] for key in (
        "status", "frozen_order", "frozen_coefficients", "refinement_error",
        "rotation_error", "elapsed_seconds", "peak_rss_mb")}), flush=True)
    return 0 if status.startswith("pass") else 2


if __name__ == "__main__":
    sys.exit(main())
