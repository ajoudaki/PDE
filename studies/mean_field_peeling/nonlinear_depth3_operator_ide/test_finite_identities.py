"""Finite-width regression tests for the frozen mixed-metric equations."""

import numpy as np

from audit_activation_tails import activation, derived, rhs


def predictor_and_kernel(state, name):
    *_, f, k = derived(state, name)
    return f, k


def test_feature_direction_and_raw_kernel():
    rng = np.random.default_rng(20260822)
    names = (
        "arctan",
        "asinh",
        "tanh",
        "sine",
        "residual_sine",
        "shifted_arctan",
        "shifted_tanh",
        "shifted_sine",
        "shifted_gudermannian",
        "composed_power_1p5",
    )
    for name in names:
        for n in (3, 7, 19):
            state = (
                rng.normal(size=n),
                rng.normal(size=n),
                rng.normal(size=(n, n)) / np.sqrt(n),
                rng.normal(size=(n, n)) / np.sqrt(n),
            )
            tangent = rhs(state, name)
            _, exact = predictor_and_kernel(state, name)
            assert exact >= 0.0
            for h in (1e-4, 3e-5, 1e-5):
                plus = tuple(x + h * dx for x, dx in zip(state, tangent))
                minus = tuple(x - h * dx for x, dx in zip(state, tangent))
                f_plus, _ = predictor_and_kernel(plus, name)
                f_minus, _ = predictor_and_kernel(minus, name)
                numerical = (f_plus - f_minus) / (2.0 * h)
                np.testing.assert_allclose(
                    numerical, exact, rtol=7e-7, atol=5e-8
                )


def test_shifted_gudermannian_lift():
    """Check the three activated-coordinate equations in the candidate."""

    rng = np.random.default_rng(20260823)
    eps = 0.2
    for n in (3, 11):
        state = (
            rng.normal(size=n),
            rng.normal(size=n),
            rng.normal(size=(n, n)) / np.sqrt(n),
            rng.normal(size=(n, n)) / np.sqrt(n),
        )
        a, u, g1, g2 = state
        tangent = rhs(state, "shifted_gudermannian")
        x1, x2, _, b3, r2, b2, q1, _, _, _ = derived(
            state, "shifted_gudermannian"
        )
        z2 = g1 @ x1
        z3 = g2 @ x2
        theta1 = np.arcsin(np.tanh(u))
        theta2 = np.arcsin(np.tanh(z2))
        theta3 = np.arcsin(np.tanh(z3))
        d1 = np.cos(theta1)
        d2 = np.cos(theta2)
        d3 = np.cos(theta3)
        a1 = np.mean(x1 * x1)
        a2 = np.mean(x2 * x2)
        exact = (
            eps * d1 * d1 * q1,
            eps * a1 * d2 * d2 * r2
            + eps * eps * d2 * (g1 @ (d1 * d1 * q1)),
            eps * a2 * d3 * d3 * a
            + eps * d3 * (
                g2
                @ (
                eps * a1 * d2 * d2 * r2
                + eps * eps * d2 * (g1 @ (d1 * d1 * q1))
                )
            ),
        )
        for h in (1e-5, 3e-6):
            plus = tuple(x + h * dx for x, dx in zip(state, tangent))
            minus = tuple(x - h * dx for x, dx in zip(state, tangent))

            def phases(s):
                _, uu, gg1, gg2 = s
                xx1, _ = activation("shifted_gudermannian", uu)
                zz2 = gg1 @ xx1
                xx2, _ = activation("shifted_gudermannian", zz2)
                zz3 = gg2 @ xx2
                return tuple(
                    np.arcsin(np.tanh(z)) for z in (uu, zz2, zz3)
                )

            numerical = tuple(
                (p - m) / (2.0 * h)
                for p, m in zip(phases(plus), phases(minus))
            )
            for got, want in zip(numerical, exact):
                np.testing.assert_allclose(got, want, rtol=2e-7, atol=2e-8)


def test_composed_near_critical_lift():
    """Check the exact natural-coordinate transport equations (2.7)."""

    rng = np.random.default_rng(20260824)
    for n in (3, 11, 23):
        state = (
            rng.normal(size=n),
            rng.normal(size=n),
            rng.normal(size=(n, n)) / np.sqrt(n),
            rng.normal(size=(n, n)) / np.sqrt(n),
        )
        a, u, g1, g2 = state
        da, du, dg1, dg2 = rhs(state, "composed_power_1p5")
        x1, x2, _, b3, r2, b2, q1, _, _, _ = derived(
            state, "composed_power_1p5"
        )
        _, d1 = activation("composed_power_1p5", u)
        z2 = g1 @ x1
        _, d2 = activation("composed_power_1p5", z2)
        z3 = g2 @ x2
        _, d3 = activation("composed_power_1p5", z3)
        a1 = np.mean(x1 * x1)
        a2 = np.mean(x2 * x2)

        v1 = q1
        v2 = a1 * r2 + (g1 @ (d1 * d1 * q1)) / d2
        v3 = a2 * a + (g2 @ (d2 * d2 * v2)) / d3

        x1_dot = d1 * du
        z2_dot = dg1 @ x1 + g1 @ x1_dot
        x2_dot = d2 * z2_dot
        z3_dot = dg2 @ x2 + g2 @ x2_dot
        np.testing.assert_allclose(du / d1, v1, rtol=2e-12, atol=2e-12)
        np.testing.assert_allclose(z2_dot / d2, v2, rtol=2e-12, atol=2e-12)
        np.testing.assert_allclose(z3_dot / d3, v3, rtol=2e-12, atol=2e-12)


if __name__ == "__main__":
    test_feature_direction_and_raw_kernel()
    test_shifted_gudermannian_lift()
    test_composed_near_critical_lift()
    print("nonlinear depth-3 finite identities: PASS")
