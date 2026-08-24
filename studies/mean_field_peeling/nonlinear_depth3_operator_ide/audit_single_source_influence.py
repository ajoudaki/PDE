"""Single-row/column influence audit for the frozen depth-three flow.

This is a discriminating experiment, not a proof.  A single immutable
Ginibre row or column is resampled while every other source is coupled.  The
reported quantities are sqrt(n) times normalized field differences, the
scale predicted by a stable row/column-cavity theorem.
"""

from __future__ import annotations

import argparse
import json

import numpy as np

from audit_activation_tails import derived, rk4


FIELD_NAMES = ("x1", "x2", "x3", "b3", "r2", "b2", "q1", "p1")


def normalized_l2(x):
    return float(np.mean(np.asarray(x) ** 2) ** 0.5)


def perturb_matrix(state, layer, axis, index, rng):
    perturbed = tuple(x.copy() for x in state)
    matrix_position = 2 if layer == 1 else 3
    matrix = perturbed[matrix_position]
    n = matrix.shape[0]
    if axis == "row":
        matrix[index, :] = rng.normal(size=n) / np.sqrt(n)
    elif axis == "column":
        matrix[:, index] = rng.normal(size=n) / np.sqrt(n)
    else:
        raise ValueError(axis)
    return perturbed


def compare(base, perturbed, activation):
    d0 = derived(base, activation)
    d1 = derived(perturbed, activation)
    n = base[0].size
    scale = np.sqrt(n)
    fields = {
        name: scale * normalized_l2(y - x)
        for name, x, y in zip(FIELD_NAMES, d0[:8], d1[:8])
    }
    fields["f"] = scale * abs(float(d1[8] - d0[8]))
    fields["K"] = scale * abs(float(d1[9] - d0[9]))
    return fields


def run_one(activation, n, seed, horizon, step, layer, axis):
    rng = np.random.default_rng(seed)
    base = (
        rng.normal(size=n),
        rng.normal(size=n),
        rng.normal(size=(n, n)) / np.sqrt(n),
        rng.normal(size=(n, n)) / np.sqrt(n),
    )
    index = int(rng.integers(n))
    perturbed = perturb_matrix(base, layer, axis, index, rng)
    steps = int(round(horizon / step))
    initial = compare(base, perturbed, activation)
    maxima = dict(initial)
    for _ in range(steps):
        base = rk4(base, step, activation)
        perturbed = rk4(perturbed, step, activation)
        current = compare(base, perturbed, activation)
        maxima = {key: max(maxima[key], value) for key, value in current.items()}
    return {
        "activation": activation,
        "n": n,
        "seed": seed,
        "layer": layer,
        "axis": axis,
        "index": index,
        "initial_scaled_difference": initial,
        "final_scaled_difference": compare(base, perturbed, activation),
        "max_scaled_difference": maxima,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--activations",
        nargs="+",
        default=["shifted_arctan", "hyperbolic_exp"],
    )
    parser.add_argument("--widths", type=int, nargs="+", default=[64, 128, 256])
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--seed", type=int, default=20260822)
    parser.add_argument("--horizon", type=float, default=0.5)
    parser.add_argument("--step", type=float, default=0.01)
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()

    results = []
    for activation in args.activations:
        for n in args.widths:
            for trial in range(args.trials):
                for layer in (1, 2):
                    for axis in ("row", "column"):
                        results.append(
                            run_one(
                                activation,
                                n,
                                args.seed + 100_003 * trial + 1009 * n,
                                args.horizon,
                                args.step,
                                layer,
                                axis,
                            )
                        )
    if args.summary:
        summary = []
        keys = sorted(
            {
                (item["activation"], item["n"], item["layer"], item["axis"])
                for item in results
            }
        )
        for activation, n, layer, axis in keys:
            group = [
                item["max_scaled_difference"]
                for item in results
                if (
                    item["activation"],
                    item["n"],
                    item["layer"],
                    item["axis"],
                )
                == (activation, n, layer, axis)
            ]
            summary.append(
                {
                    "activation": activation,
                    "n": n,
                    "layer": layer,
                    "axis": axis,
                    "mean_max_scaled_difference": {
                        field: float(np.mean([item[field] for item in group]))
                        for field in ("x2", "x3", "r2", "q1", "f", "K")
                    },
                }
            )
        print(json.dumps(summary, indent=2))
    else:
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
