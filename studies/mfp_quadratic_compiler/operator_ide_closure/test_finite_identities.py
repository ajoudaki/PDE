#!/usr/bin/env python3
"""Independent finite-width checks for the quadratic operator-IDE algebra."""

from __future__ import annotations

import numpy as np


def inner(v: np.ndarray, w: np.ndarray) -> float:
    return float(np.mean(v * w))


def fields(a: np.ndarray, u: np.ndarray, g: np.ndarray):
    x = u * u
    z = g @ x
    b = a * z
    r = g.T @ b
    return x, z, b, r


def feature_rhs(a: np.ndarray, u: np.ndarray, g: np.ndarray):
    x, z, b, r = fields(a, u, g)
    return z * z, 4 * u * r, 2 * np.outer(b, x) / len(a)


def prediction_and_kernel(a: np.ndarray, u: np.ndarray, g: np.ndarray):
    x, z, b, r = fields(a, u, g)
    f = inner(a, z * z)
    k = (
        inner(z * z, z * z)
        + 4 * inner(b, b) * inner(x, x)
        + 16 * inner(x, r * r)
    )
    return f, k


def kernel_derivative(a: np.ndarray, u: np.ndarray, g: np.ndarray) -> float:
    """Differentiate K exactly along feature flow."""
    x, z, b, r = fields(a, u, g)
    da, du, dg = feature_rhs(a, u, g)
    dx = 2 * u * du
    dz = dg @ x + g @ dx
    db = da * z + a * dz
    dr = dg.T @ b + g.T @ db
    return float(
        4 * inner(z**3, dz)
        + 8 * inner(b, db) * inner(x, x)
        + 8 * inner(b, b) * inner(x, dx)
        + 16 * inner(dx, r * r)
        + 32 * inner(x * r, dr)
    )


def orthogonal_component(v: np.ndarray, constraints: list[np.ndarray]):
    out = v.astype(float).copy()
    for c in constraints:
        out -= inner(out, c) / inner(c, c) * c
    return out


def test_gradient_and_balances():
    rng = np.random.default_rng(20260821)
    n = 19
    a = rng.normal(size=n)
    u = rng.normal(size=n)
    w = rng.normal(size=(n, n))
    g = w / np.sqrt(n)
    da, du, dg = feature_rhs(a, u, g)
    f, k = prediction_and_kernel(a, u, g)

    eps = 2.0e-7
    f_plus, _ = prediction_and_kernel(a + eps * da, u + eps * du, g + eps * dg)
    f_minus, _ = prediction_and_kernel(a - eps * da, u - eps * du, g - eps * dg)
    assert np.isclose((f_plus - f_minus) / (2 * eps), k, rtol=2e-8, atol=2e-8)

    # W=sqrt(n)G.  These are the row and column balance derivatives.
    dw = np.sqrt(n) * dg
    row_derivative = 2 * np.sum(w * dw, axis=1) - 4 * a * da
    col_derivative = 2 * np.sum(w * dw, axis=0) - u * du
    assert np.max(np.abs(row_derivative)) < 2e-12
    assert np.max(np.abs(col_derivative)) < 2e-12
    assert np.isfinite(f)


def test_hidden_rank_one_direction():
    """Same current node fields and K, but a different next K derivative."""
    rng = np.random.default_rng(20260822)
    n = 17
    a = rng.normal(size=n)
    u = rng.normal(size=n)
    g = rng.normal(size=(n, n)) / np.sqrt(n)
    x, z, big_b, r = fields(a, u, g)
    v = x * r

    # c is orthogonal to x but not to x*r; q is orthogonal to B.
    c = orthogonal_component(v, [x])
    q = orthogonal_component(
        z**3 + 2 * inner(x, x) * a * a * z + 8 * a * (g @ v),
        [big_b],
    )
    assert abs(inner(c, x)) < 2e-12
    assert abs(inner(q, big_b)) < 2e-12
    h = np.outer(q, c) / n

    eps = 1.0e-6
    f0, k0 = prediction_and_kernel(a, u, g)
    fp, kp = prediction_and_kernel(a, u, g + eps * h)
    fm, km = prediction_and_kernel(a, u, g - eps * h)
    assert np.isclose(fp, f0, atol=2e-13)
    assert np.isclose(fm, f0, atol=2e-13)
    assert np.isclose(kp, k0, atol=2e-12)
    assert np.isclose(km, k0, atol=2e-12)

    numerical = (
        kernel_derivative(a, u, g + eps * h)
        - kernel_derivative(a, u, g - eps * h)
    ) / (2 * eps)
    witness = z**3 + 2 * inner(x, x) * a * a * z + 8 * a * (g @ v)
    exact = 64 * inner(c, v) * inner(q, witness)
    assert abs(exact) > 1e-4
    assert np.isclose(numerical, exact, rtol=2e-7, atol=2e-7)


def test_general_one_cell_reduction():
    """Check the normalized one-cell subsystem and vanishing-operator spike."""
    n = 101
    rho = 7.0
    gamma = 1.0 / rho
    a = np.zeros(n)
    u = np.zeros(n)
    g = np.zeros((n, n))
    a[0] = rho
    u[0] = rho
    g[0, 0] = gamma

    da, du, dg = feature_rhs(a, u, g)
    assert np.isclose(da[0], gamma**2 * rho**4)
    assert np.isclose(du[0], 4 * rho**4 * gamma**2)
    assert np.isclose(dg[0, 0], 2 * gamma * rho**5 / n)
    assert np.count_nonzero(da[1:]) == 0
    assert np.count_nonzero(du[1:]) == 0
    assert np.count_nonzero(dg[1:, :]) == 0
    assert np.count_nonzero(dg[:, 1:]) == 0

    # Derivatives of v^2-4a^2 and g^2-v^2/(2n) vanish.
    assert np.isclose(2 * rho * du[0] - 8 * rho * da[0], 0.0)
    assert np.isclose(2 * gamma * dg[0, 0] - rho * du[0] / n, 0.0)

    f, k = prediction_and_kernel(a, u, g)
    assert np.isclose(f, rho**3 / n)
    assert np.isclose(k, 17 * rho**4 / n + 4 * rho**8 / n**2)


if __name__ == "__main__":
    test_gradient_and_balances()
    test_hidden_rank_one_direction()
    test_general_one_cell_reduction()
    print("quadratic finite-width operator identities: PASS")
