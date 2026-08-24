"""Regression tests for the unfrozen-readout depth-three closure."""

from __future__ import annotations

from math import factorial
from itertools import product

import numpy as np


def apply_fock_symbol(state, symbol):
    """Apply one circular-generator symbol to a sparse Fock vector."""
    create_color, annihilate_color = {
        "b": (0, 1),
        "b*": (1, 0),
        "r": (2, 3),
        "r*": (3, 2),
    }[symbol]
    result = {}
    for word, coefficient in state.items():
        created = (create_color,) + word
        result[created] = result.get(created, 0.0) + coefficient
        if word and word[0] == annihilate_color:
            shortened = word[1:]
            result[shortened] = result.get(shortened, 0.0) + coefficient
    return result


def apply_fock_word(root, symbols):
    state = {root: 1.0}
    for symbol in reversed(symbols):
        state = apply_fock_symbol(state, symbol)
    return state


def test_colored_fock_source_has_two_independent_tracial_root_sectors():
    alphabet = ("b", "b*", "r", "r*")
    vacuum = ()
    x_tail = (4,)
    a_tail = (5,)
    for length in range(6):
        for symbols in product(alphabet, repeat=length):
            vacuum_moment = apply_fock_word(vacuum, symbols).get(vacuum, 0.0)
            x_state = apply_fock_word(x_tail, symbols)
            a_state = apply_fock_word(a_tail, symbols)
            assert x_state.get(x_tail, 0.0) == vacuum_moment
            assert a_state.get(a_tail, 0.0) == vacuum_moment
            assert x_state.get(a_tail, 0.0) == 0.0
            assert a_state.get(x_tail, 0.0) == 0.0


def feature_rhs(a, r, b, x):
    z = b @ x
    p = r.T @ a
    return r @ z, np.outer(a, z), np.outer(p, x), b.T @ p


def feature_kernel(a, r, b, x):
    a_dot, r_dot, b_dot, x_dot = feature_rhs(a, r, b, x)
    return (
        a_dot @ a_dot
        + np.sum(r_dot * r_dot)
        + np.sum(b_dot * b_dot)
        + x_dot @ x_dot
    )


def cyclic_matrix(a, r, b, x):
    n = len(a)
    c = np.zeros((1 + 3 * n, 1 + 3 * n))
    slices = (slice(0, 1), slice(1, 1 + n), slice(1 + n, 1 + 2 * n), slice(1 + 2 * n, 1 + 3 * n))
    c[slices[0], slices[3]] = a.reshape(1, n)
    c[slices[1], slices[0]] = x.reshape(n, 1)
    c[slices[2], slices[1]] = b
    c[slices[3], slices[2]] = r
    return c


def test_exact_cyclic_lift_trace_readouts_and_moment_map():
    rng = np.random.default_rng(20260820)
    n = 5
    a = rng.normal(size=n)
    x = rng.normal(size=n)
    r = rng.normal(size=(n, n))
    b = rng.normal(size=(n, n))

    a_dot, r_dot, b_dot, x_dot = feature_rhs(a, r, b, x)
    c = cyclic_matrix(a, r, b, x)
    c_dot = cyclic_matrix(a_dot, r_dot, b_dot, x_dot)

    np.testing.assert_allclose(c_dot, np.linalg.matrix_power(c.T, 3))
    f = float(a @ r @ b @ x)
    np.testing.assert_allclose(np.trace(np.linalg.matrix_power(c, 4)) / 4, f)
    np.testing.assert_allclose(
        np.trace(np.linalg.matrix_power(c, 3) @ np.linalg.matrix_power(c.T, 3)),
        feature_kernel(a, r, b, x),
    )

    moment_map_dot = (
        c_dot.T @ c
        + c.T @ c_dot
        - c_dot @ c.T
        - c @ c_dot.T
    )
    np.testing.assert_allclose(moment_map_dot, 0.0, atol=1.0e-10)


def test_exact_central_reduction():
    rng = np.random.default_rng(1701)
    n = 6
    a = rng.normal(size=n)
    x = rng.normal(size=n)
    r = rng.normal(size=(n, n))
    b = rng.normal(size=(n, n))

    a_dot, r_dot, b_dot, x_dot = feature_rhs(a, r, b, x)
    z = b @ x
    p = r.T @ a
    z_dot = b_dot @ x + b @ x_dot
    p_dot = r_dot.T @ a + r.T @ a_dot
    left = b @ b.T + (x @ x) * np.eye(n)
    right = r.T @ r + (a @ a) * np.eye(n)

    np.testing.assert_allclose(z_dot, left @ p)
    np.testing.assert_allclose(p_dot, right @ z)
    np.testing.assert_allclose(
        p @ left @ p + z @ right @ z,
        feature_kernel(a, r, b, x),
    )

    left_dot = b_dot @ b.T + b @ b_dot.T + 2 * (x @ x_dot) * np.eye(n)
    right_dot = r_dot.T @ r + r.T @ r_dot + 2 * (a @ a_dot) * np.eye(n)
    common = np.outer(z, p) + np.outer(p, z) + 2 * (z @ p) * np.eye(n)
    np.testing.assert_allclose(left_dot, common)
    np.testing.assert_allclose(right_dot, common)


def test_separate_gram_spectra_do_not_determine_feature_kernel():
    angle = 0.61
    cosine, sine = np.cos(angle), np.sin(angle)
    a = np.array([1.0, 0.0, 0.0])
    x = a.copy()
    r = np.diag([1.0, 2.0, 3.0])
    b12 = np.array(
        [[cosine, -sine, 0.0], [sine, cosine, 0.0], [0.0, 0.0, 1.0]]
    )
    b13 = np.array(
        [[cosine, 0.0, -sine], [0.0, 1.0, 0.0], [sine, 0.0, cosine]]
    )

    np.testing.assert_allclose(b12.T @ b12, b13.T @ b13, atol=1.0e-15)
    np.testing.assert_allclose(a @ r @ b12 @ x, a @ r @ b13 @ x)
    np.testing.assert_allclose(
        feature_kernel(a, r, b12, x), 3 + cosine**2 + 4 * sine**2
    )
    np.testing.assert_allclose(
        feature_kernel(a, r, b13, x), 3 + cosine**2 + 9 * sine**2
    )
    assert feature_kernel(a, r, b12, x) != feature_kernel(a, r, b13, x)


def zeros(shape):
    return np.zeros(shape, dtype=float)


def rooted_edge_operators(max_length):
    """Two-edge free-Wick path source, only for the independent jet check."""
    by_layer = [[] for _ in range(3)]
    for color, root in (("in", 0), ("out", 2)):
        frontier = [(color, (root,))]
        by_layer[root].append(frontier[0])
        for _ in range(max_length):
            new_frontier = []
            for color_now, vertices in frontier:
                terminal = vertices[-1]
                for neighbor in (terminal - 1, terminal + 1):
                    if 0 <= neighbor <= 2:
                        path = (color_now, vertices + (neighbor,))
                        by_layer[neighbor].append(path)
                        new_frontier.append(path)
            frontier = new_frontier

    indices = [{path: i for i, path in enumerate(layer)} for layer in by_layer]
    operators = []
    for edge in (1, 2):
        matrix = zeros((len(by_layer[edge]), len(by_layer[edge - 1])))
        for column, path in enumerate(by_layer[edge - 1]):
            color, vertices = path
            if len(vertices) - 1 < max_length:
                matrix[indices[edge][(color, vertices + (edge,))], column] += 1
            if len(vertices) >= 2 and vertices[-2] == edge:
                matrix[indices[edge][(color, vertices[:-1])], column] += 1
        operators.append(matrix)
    return by_layer, indices, operators


def central_source_jet(max_order):
    by_layer, indices, (b0, r0) = rooted_edge_operators(2 * (max_order + 1))
    alpha = zeros((len(by_layer[0]),))
    beta = zeros((len(by_layer[2]),))
    alpha[indices[0][("in", (0,))]] = 1
    beta[indices[2][("out", (2,))]] = 1

    z = [zeros((len(by_layer[1]),)) for _ in range(max_order + 1)]
    p = [zeros((len(by_layer[1]),)) for _ in range(max_order + 1)]
    h = [0.0 for _ in range(max_order + 1)]
    s = [zeros((len(by_layer[1]), len(by_layer[1]))) for _ in range(max_order + 1)]
    z[0] = b0 @ alpha
    p[0] = r0.T @ beta

    identity = zeros((len(by_layer[1]), len(by_layer[1])))
    for i in range(len(identity)):
        identity[i, i] = 1
    left0 = b0 @ b0.T + identity
    right0 = r0.T @ r0 + identity

    for order in range(max_order):
        z_next = zeros(z[0].shape)
        p_next = zeros(p[0].shape)
        for split in range(order + 1):
            if split == 0:
                left_coefficient = left0
                right_coefficient = right0
            else:
                left_coefficient = s[split] + h[split] * identity
                right_coefficient = left_coefficient
            z_next += left_coefficient @ p[order - split]
            p_next += right_coefficient @ z[order - split]
        z[order + 1] = z_next / (order + 1)
        p[order + 1] = p_next / (order + 1)

        scalar = 0.0
        operator = zeros(s[0].shape)
        for split in range(order + 1):
            scalar += z[split] @ p[order - split]
            operator += np.outer(z[split], p[order - split])
            operator += np.outer(p[split], z[order - split])
        h[order + 1] = 2 * scalar / (order + 1)
        s[order + 1] = operator / (order + 1)

    coefficients = []
    for order in range(max_order + 1):
        coefficient = 0.0
        for split in range(order + 1):
            coefficient += z[split] @ p[order - split]
        coefficients.append(coefficient)
    return tuple(factorial(k) * value for k, value in enumerate(coefficients))


def test_free_wishart_central_closure_reproduces_independent_depth_three_jet():
    np.testing.assert_allclose(
        central_source_jet(5),
        (0, 4, 0, 160, 0, 13888),
        rtol=0,
        atol=1.0e-9,
    )
