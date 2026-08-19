"""Bounded finite-width audit of the emitted L=2, B=1 normal form.

This script compares exact finite-width automatic Taylor propagation with the
candidate width-limit GNF.  It is evidence for the implementation/derivation,
not a replacement for the finite-width-to-limit proof.
"""

from __future__ import annotations

import argparse
import json
from math import sqrt

import numpy as np

from .finite_width_jet import feature_jet
from .l2_b1_correction import first_correction_normal_form
from .normal_form import (
    PolynomialActivation,
    evaluate_polynomial,
    evaluate_quadrature,
)


def polynomial_oracle(coefficients):
    coefficients = tuple(float(value) for value in coefficients)

    def derivative(order, x):
        values = list(coefficients)
        for _ in range(order):
            values = [k * values[k] for k in range(1, len(values))]
        out = np.zeros_like(x, dtype=np.float64)
        for coefficient in reversed(values):
            out = out * x + coefficient
        return out

    return derivative


def activation(name):
    polynomials = {
        "constant": [2.0],
        "linear": [0.0, 1.0],
        "affine": [1.0, 1.0],
        "quadratic": [0.0, 0.0, 1.0],
        "cubic": [0.0, 0.0, 0.0, 1.0],
    }
    if name in polynomials:
        coefficients = polynomials[name]
        return polynomial_oracle(coefficients), PolynomialActivation(coefficients)

    if name == "sin":
        def derivative(order, x):
            return (np.sin(x), np.cos(x), -np.sin(x), -np.cos(x))[order % 4]

        return derivative, None

    if name == "tanh":
        def derivative(order, x):
            t = np.tanh(x)
            return (
                t,
                1.0 - t * t,
                -2.0 * t * (1.0 - t * t),
                -2.0 * (1.0 - t * t) * (1.0 - 3.0 * t * t),
            )[order]

        return derivative, None

    raise ValueError(name)


def parse_ints(text):
    values = tuple(int(value) for value in text.split(","))
    if not values or any(value < 1 for value in values):
        raise argparse.ArgumentTypeError("expected comma-separated positive integers")
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--activation",
        choices=("constant", "linear", "affine", "quadratic", "cubic", "sin", "tanh"),
        required=True,
    )
    parser.add_argument("--widths", type=parse_ints, default=(16, 32, 64))
    parser.add_argument("--seeds", type=parse_ints, default=(4096, 2048, 1024))
    parser.add_argument("--seed-offset", type=int, default=0)
    parser.add_argument("--q0", type=float, default=1.0)
    parser.add_argument("--quadrature-order", type=int, default=160)
    args = parser.parse_args()
    if len(args.widths) != len(args.seeds):
        parser.error("--widths and --seeds must have the same number of entries")

    oracle, polynomial = activation(args.activation)
    state = first_correction_normal_form()
    if polynomial is not None:
        q0_exact = int(args.q0) if float(args.q0).is_integer() else args.q0
        target_a = float(evaluate_polynomial(state.ntk, polynomial, {"q_0": q0_exact}))
        target_c = float(
            evaluate_polynomial(state.correction, polynomial, {"q_0": q0_exact})
        )
        target_kind = "exact polynomial Wick contraction"
    else:
        target_a = evaluate_quadrature(
            state.ntk, oracle, {"q_0": args.q0}, order=args.quadrature_order
        )
        target_c = evaluate_quadrature(
            state.correction,
            oracle,
            {"q_0": args.q0},
            order=args.quadrature_order,
        )
        target_kind = f"Gauss-Hermite order {args.quadrature_order}"

    rows = []
    seed_cursor = args.seed_offset
    for width, seed_count in zip(args.widths, args.seeds):
        samples = np.asarray(
            [
                feature_jet(width, args.q0, oracle, seed_cursor + seed).derivatives[[1, 3]]
                for seed in range(seed_count)
            ]
        )
        seed_cursor += seed_count
        mean = samples.mean(axis=0)
        stderr = samples.std(axis=0, ddof=1) / sqrt(seed_count)
        rows.append(
            {
                "width": width,
                "seed_count": seed_count,
                "seed_end_exclusive": seed_cursor,
                "mean_F1": float(mean[0]),
                "stderr_F1": float(stderr[0]),
                "z_F1_vs_limit": float((mean[0] - target_a) / stderr[0])
                if stderr[0] > 0
                else None,
                "mean_F3": float(mean[1]),
                "stderr_F3": float(stderr[1]),
                "z_F3_vs_limit": float((mean[1] - target_c) / stderr[1])
                if stderr[1] > 0
                else None,
            }
        )

    print(
        json.dumps(
            {
                "activation": args.activation,
                "q0": args.q0,
                "target_kind": target_kind,
                "target_A": target_a,
                "target_C": target_c,
                "rows": rows,
                "interpretation": (
                    "Finite-width Monte Carlo is an implementation audit only; "
                    "z-scores against the width limit include finite-width bias."
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
