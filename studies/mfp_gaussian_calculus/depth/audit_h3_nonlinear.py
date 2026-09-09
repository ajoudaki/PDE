"""Reproduce the nonlinear H=3 finite-width audit of the depth recursion.

The target is computed by ``gnf_audit_reference``, the independently
contracted one-dimensional-atom recursion.  Samples come from the exact
finite-width moving feature-ascent jet, not from ``gnf_recursion``.
"""

from __future__ import annotations

import argparse
from math import sqrt

import numpy as np

from .finite_width_jet import feature_ascent_jet
from .gnf_audit_reference import evaluate_depth_b1_audit_recurrence
from .model import sample_state


def sine_derivative(order: int, x: np.ndarray) -> np.ndarray:
    return (np.sin(x), np.cos(x), -np.sin(x), -np.cos(x))[order % 4]


def _positive_integer_list(raw: str) -> tuple[int, ...]:
    result = tuple(int(value) for value in raw.split(","))
    if not result or any(value < 1 for value in result):
        raise argparse.ArgumentTypeError("expected comma-separated positive integers")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q0", type=float, default=1.0)
    parser.add_argument("--widths", type=_positive_integer_list, default=(64, 128, 256, 512))
    parser.add_argument("--seeds", type=_positive_integer_list, default=(4000, 3000, 1200, 220))
    parser.add_argument("--quadrature-order", type=int, default=80)
    parser.add_argument("--seed-base", type=int, default=831_000_000)
    args = parser.parse_args()
    if len(args.widths) != len(args.seeds):
        parser.error("--widths and --seeds must have the same number of entries")
    if len(args.widths) < 3:
        parser.error("the intercept audit needs at least three widths")

    target = evaluate_depth_b1_audit_recurrence(
        args.q0,
        3,
        sine_derivative,
        quadrature_order=args.quadrature_order,
    )
    print(
        f"target A={target.ntk:.12g} T={target.straight_line:.12g} "
        f"Hsq={target.hessian_square:.12g} C={target.correction:.12g}"
    )

    gram = np.asarray([[args.q0]])
    channel = np.asarray([1.0])
    rows = []
    for width, seeds in zip(args.widths, args.seeds):
        samples = np.empty(seeds)
        for index in range(seeds):
            state = sample_state(
                width,
                gram,
                hidden_layers=3,
                seed=args.seed_base + width * 10_000 + index,
            )
            samples[index] = feature_ascent_jet(
                state, gram, channel, sine_derivative
            ).derivatives[3]
        mean = float(samples.mean())
        standard_error = float(samples.std(ddof=1) / sqrt(seeds))
        rows.append((width, mean, standard_error))
        z_score = (mean - target.correction) / standard_error
        print(
            f"n={width:4d} seeds={seeds:5d} mean={mean:.12g} "
            f"SE={standard_error:.8g} z_to_target={z_score:.4f}"
        )

    inverse_width = np.asarray([1.0 / row[0] for row in rows])
    means = np.asarray([row[1] for row in rows])
    errors = np.asarray([row[2] for row in rows])
    design = np.column_stack((np.ones_like(inverse_width), inverse_width))
    precision = np.diag(1.0 / errors**2)
    covariance = np.linalg.inv(design.T @ precision @ design)
    coefficients = covariance @ design.T @ precision @ means
    residual = means - design @ coefficients
    chi_square_per_dof = float(
        residual @ precision @ residual / (len(rows) - design.shape[1])
    )
    intercept_error = sqrt(float(covariance[0, 0]))
    intercept_z = (float(coefficients[0]) - target.correction) / intercept_error
    print(
        f"weighted 1/n intercept={coefficients[0]:.12g} "
        f"SE={intercept_error:.8g} slope={coefficients[1]:.9g} "
        f"chi2/dof={chi_square_per_dof:.6g} z_to_target={intercept_z:.4f}"
    )


if __name__ == "__main__":
    main()
