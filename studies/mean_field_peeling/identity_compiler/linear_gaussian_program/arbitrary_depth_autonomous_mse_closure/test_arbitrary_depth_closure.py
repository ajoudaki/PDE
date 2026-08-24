"""Algebraic regression tests for the arbitrary-depth operator closure."""

from __future__ import annotations

from fractions import Fraction
from math import factorial

import numpy as np


def forward_backward(a, b, matrices):
    p = [a]
    for matrix in matrices:
        p.append(matrix @ p[-1])

    z = [None] * (len(matrices) + 1)
    z[-1] = b
    for j in range(len(matrices) - 1, -1, -1):
        z[j] = matrices[j].T @ z[j + 1]
    return p, z


def output(a, b, matrices):
    p, _ = forward_backward(a, b, matrices)
    return float(b @ p[-1])


def kernel(p, z):
    value = float(z[0] @ z[0] + p[-1] @ p[-1])
    for j in range(1, len(p)):
        value += float(z[j] @ z[j]) * float(p[j - 1] @ p[j - 1])
    return value


def test_directional_derivative_is_kernel_at_depths_one_through_five():
    rng = np.random.default_rng(20260820)
    eps = 1.0e-6

    for hidden_depth in range(1, 6):
        q = hidden_depth - 1
        dimension = 4
        a = rng.normal(size=dimension)
        b = rng.normal(size=dimension)
        matrices = [rng.normal(size=(dimension, dimension)) / 2 for _ in range(q)]

        p, z = forward_backward(a, b, matrices)
        a_dot = z[0]
        b_dot = p[-1]
        matrix_dots = [np.outer(z[j], p[j - 1]) for j in range(1, q + 1)]

        f_plus = output(
            a + eps * a_dot,
            b + eps * b_dot,
            [m + eps * dm for m, dm in zip(matrices, matrix_dots)],
        )
        f_minus = output(
            a - eps * a_dot,
            b - eps * b_dot,
            [m - eps * dm for m, dm in zip(matrices, matrix_dots)],
        )
        directional_derivative = (f_plus - f_minus) / (2 * eps)

        np.testing.assert_allclose(
            directional_derivative,
            kernel(p, z),
            rtol=2.0e-8,
            atol=2.0e-8,
        )


def all_rooted_paths(q, max_length):
    """Return the colored path bases, grouped by terminal layer."""
    by_layer = [[] for _ in range(q + 1)]
    roots = (("a", 0), ("b", q))
    for color, root in roots:
        frontier = [(color, (root,))]
        by_layer[root].append(frontier[0])
        for _ in range(max_length):
            next_frontier = []
            for color_now, vertices in frontier:
                terminal = vertices[-1]
                for neighbor in (terminal - 1, terminal + 1):
                    if 0 <= neighbor <= q:
                        path = (color_now, vertices + (neighbor,))
                        by_layer[neighbor].append(path)
                        next_frontier.append(path)
            frontier = next_frontier
    return by_layer


def path_edge_operators(q, max_length):
    bases = all_rooted_paths(q, max_length)
    indices = [{path: i for i, path in enumerate(basis)} for basis in bases]
    operators = []

    for layer in range(1, q + 1):
        matrix = np.zeros((len(bases[layer]), len(bases[layer - 1])), dtype=int)
        for column, path in enumerate(bases[layer - 1]):
            color, vertices = path

            appended = (color, vertices + (layer,))
            if len(vertices) - 1 < max_length:
                matrix[indices[layer][appended], column] += 1.0

            if len(vertices) >= 2 and vertices[-2] == layer:
                shortened = (color, vertices[:-1])
                matrix[indices[layer][shortened], column] += 1.0
        operators.append(matrix)
    return bases, indices, operators


def test_rooted_path_source_has_f_zero_and_k_l_plus_one():
    for hidden_depth in range(1, 7):
        q = hidden_depth - 1

        if q == 0:
            # The two colored roots span the same layer but are orthogonal.
            a = np.array([1.0, 0.0])
            b = np.array([0.0, 1.0])
            p, z = forward_backward(a, b, [])
        else:
            bases, indices, matrices = path_edge_operators(q, max_length=q)
            a = np.zeros(len(bases[0]))
            b = np.zeros(len(bases[q]))
            a[indices[0][("a", (0,))]] = 1.0
            b[indices[q][("b", (q,))]] = 1.0
            p, z = forward_backward(a, b, matrices)

        np.testing.assert_allclose(float(b @ p[-1]), 0.0, atol=0.0)
        np.testing.assert_allclose(kernel(p, z), hidden_depth + 1.0, atol=0.0)
        for vector in p + z:
            np.testing.assert_allclose(float(vector @ vector), 1.0, atol=0.0)


def test_depth_one_feature_closed_form():
    # A(s)=cosh(s)a+sinh(s)b and B(s)=sinh(s)a+cosh(s)b.
    for feature_time in (0.0, 0.2, 0.7):
        f = np.sinh(2.0 * feature_time)
        k = 2.0 * np.cosh(2.0 * feature_time)
        np.testing.assert_allclose(f, np.sinh(2.0 * feature_time))
        np.testing.assert_allclose(k, 2.0 * np.cosh(2.0 * feature_time))


def fraction_zeros(shape):
    result = np.empty(shape, dtype=object)
    result.fill(Fraction(0))
    return result


def convolve_matvec(matrix_coefficients, vector_coefficients, order):
    result = fraction_zeros(matrix_coefficients[0].shape[:1])
    for r in range(order + 1):
        result += matrix_coefficients[r] @ vector_coefficients[order - r]
    return result


def path_feature_derivatives(hidden_depth, max_order):
    """Exact ordinary-Taylor recurrence for the truncated path ODE."""
    q = hidden_depth - 1

    if q == 0:
        dimensions = [2]
        operators = []
        a_root = 0
        b_root = 1
    else:
        max_length = (max_order + 1) * q
        bases, indices, operators = path_edge_operators(q, max_length)
        dimensions = [len(basis) for basis in bases]
        a_root = indices[0][("a", (0,))]
        b_root = indices[q][("b", (q,))]

    endpoint_a = [fraction_zeros((dimensions[0],)) for _ in range(max_order + 1)]
    endpoint_b = [fraction_zeros((dimensions[q],)) for _ in range(max_order + 1)]
    endpoint_a[0][a_root] = Fraction(1)
    endpoint_b[0][b_root] = Fraction(1)

    effective = []
    for edge, operator in enumerate(operators):
        coefficients = [fraction_zeros(operator.shape) for _ in range(max_order + 1)]
        coefficients[0] = operator.astype(object)
        effective.append(coefficients)

    forward = [
        [fraction_zeros((dimension,)) for _ in range(max_order + 1)]
        for dimension in dimensions
    ]
    backward = [
        [fraction_zeros((dimension,)) for _ in range(max_order + 1)]
        for dimension in dimensions
    ]

    for order in range(max_order):
        forward[0][order] = endpoint_a[order]
        for edge in range(q):
            forward[edge + 1][order] = convolve_matvec(
                effective[edge], forward[edge], order
            )

        backward[q][order] = endpoint_b[order]
        for edge in range(q - 1, -1, -1):
            transposed = [coefficient.T for coefficient in effective[edge]]
            backward[edge][order] = convolve_matvec(
                transposed, backward[edge + 1], order
            )

        endpoint_a[order + 1] = backward[0][order] / (order + 1)
        endpoint_b[order + 1] = forward[q][order] / (order + 1)

        for edge in range(q):
            coefficient = fraction_zeros(effective[edge][0].shape)
            for r in range(order + 1):
                coefficient += np.outer(
                    backward[edge + 1][r], forward[edge][order - r]
                )
            effective[edge][order + 1] = coefficient / (order + 1)

    # The final state coefficient has now been computed; propagate it once.
    forward[0][max_order] = endpoint_a[max_order]
    for edge in range(q):
        forward[edge + 1][max_order] = convolve_matvec(
            effective[edge], forward[edge], max_order
        )

    output_coefficients = []
    for order in range(max_order + 1):
        coefficient = Fraction(0)
        for r in range(order + 1):
            coefficient += endpoint_b[r] @ forward[q][order - r]
        output_coefficients.append(coefficient)

    return tuple(
        factorial(order) * coefficient
        for order, coefficient in enumerate(output_coefficients)
    )


def test_path_ode_reproduces_known_feature_jets_through_order_five():
    expected = {
        1: (0, 2, 0, 8, 0, 32),
        2: (0, 3, 0, 48, 0, 1464),
        3: (0, 4, 0, 160, 0, 13888),
    }
    for hidden_depth, derivatives in expected.items():
        assert path_feature_derivatives(hidden_depth, 5) == derivatives
