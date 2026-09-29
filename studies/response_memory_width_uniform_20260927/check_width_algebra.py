"""Deterministic checks of the width analysis; no training or random search."""

import argparse
import json
import math
from pathlib import Path

import numpy as np


def dense_rhs(first, middle, readout, label):
    n = len(readout)
    h = np.tanh(first)
    g = np.tanh(middle @ h)
    residual = readout @ g / n - label
    delta2 = readout * (1 - g * g)
    delta1 = (1 - h * h) * (middle.T @ delta2)
    return (
        -2 * residual * delta1,
        -2 * residual * np.outer(delta2, h) / n,
        -2 * residual * g,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)

    u = a = c = 1.0
    y = 2.0
    h = math.tanh(u)
    s = 1 - h * h
    g = math.tanh(a * h)
    v = 1 - g * g
    r = c * g - y
    rho = abs(r)
    scalar_rhs = np.array([-2 * r * a * c * v * s,
                           -2 * r * c * v * h, -2 * r * g])
    errors = {}
    for n in [1, 2, 7, 32]:
        rhs = dense_rhs(np.full(n, u), np.full((n, n), a / n),
                        np.full(n, c), y)
        discrepancy = max(np.max(np.abs(rhs[0] - scalar_rhs[0])),
                          np.max(np.abs(n * rhs[1] - scalar_rhs[1])),
                          np.max(np.abs(rhs[2] - scalar_rhs[2])))
        assert discrepancy < 1e-12
        errors[n] = float(discrepancy)

    endpoint_derivatives = {}
    for order in [1, 2, 3, 7, 16]:
        weights = 2 * np.arange(order) + 1
        matrix = np.diag(np.arange(order)).astype(float)
        for k in range(order):
            matrix[k, :k] = weights[:k]
        moments = np.zeros(order)
        moments[0] = h
        moment_dot = rho * (h - matrix @ moments)
        hstar_dot = weights @ moment_dot - rho * (weights @ moments)
        assert abs(hstar_dot) < 1e-12
        endpoint_derivatives[order] = float(hstar_dot)

    hdot = s * scalar_rhs[0]
    middle_error_t2 = r * c * v * hdot
    readout_jacobian = -2 * (2 * c * g - y) * h * v
    readout_error_t3 = readout_jacobian * middle_error_t2 / 3
    assert middle_error_t2 < 0 and readout_error_t3 < 0

    # Independently evaluate the matrix field for the concentration example.
    field_errors = {}
    for n in [1, 2, 7, 32]:
        first = np.zeros(n)
        first[0] = -1
        middle = np.zeros((n, n))
        middle[:, 0] = 1 / math.sqrt(n)
        actual = dense_rhs(first, middle, np.ones(n), 1)[0][0] / math.sqrt(n)
        hn = math.tanh(-1)
        gn = math.tanh(hn / math.sqrt(n))
        expected = -2 * (gn - 1) * (1 - gn * gn) * (1 - hn * hn)
        assert abs(actual - expected) < 1e-12
        field_errors[n] = abs(actual - expected)

    def normalized_first_velocity(n, value):
        hn = math.tanh(value)
        gn = math.tanh(hn / math.sqrt(n))
        return -2 * (gn - 1) * (1 - gn * gn) * (1 - hn * hn)

    eta = 0.1
    concentration = []
    for n in [16, 256, 4096, 65536]:
        state_distance = eta / math.sqrt(n)
        velocity_distance = abs(normalized_first_velocity(n, -1 + eta)
                                - normalized_first_velocity(n, -1))
        concentration.append({"n": n, "state_distance": state_distance,
                              "velocity_distance": velocity_distance,
                              "ratio": velocity_distance / state_distance})
    limit = 2 * abs((1 - math.tanh(-1 + eta) ** 2)
                    - (1 - math.tanh(-1) ** 2))
    assert limit > 0
    assert concentration[-1]["ratio"] > concentration[0]["ratio"]

    result = {
        "scope": "deterministic algebra only; no trajectory integration",
        "numpy_version": np.__version__,
        "dense_replication_rhs_errors": errors,
        "initial_forward_projection_endpoint_derivatives": endpoint_derivatives,
        "middle_error_t2_coefficient": middle_error_t2,
        "readout_error_t3_coefficient": readout_error_t3,
        "concentrated_field_formula_errors": field_errors,
        "concentrated_field_limit": limit,
        "concentration_scaling": concentration,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
