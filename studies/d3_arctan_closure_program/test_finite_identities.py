import numpy as np


def theta(u):
    return u + u**3 / 3.0


def theta_inverse(r):
    return 2.0 * np.sinh(np.arcsinh(1.5 * r) / 3.0)


def fields(a, r, g1, g2):
    u = theta_inverse(r)
    d1 = 1.0 / (1.0 + u**2)
    x1 = np.arctan(u)
    z2 = g1 @ x1
    d2 = 1.0 / (1.0 + z2**2)
    x2 = np.arctan(z2)
    z3 = g2 @ x2
    d3 = 1.0 / (1.0 + z3**2)
    x3 = np.arctan(z3)
    b3 = a * d3
    r2 = g2.T @ b3
    b2 = d2 * r2
    q1 = g1.T @ b2
    return u, d1, x1, z2, d2, x2, z3, d3, x3, b3, r2, b2, q1


def feature_rhs(a, r, g1, g2):
    vals = fields(a, r, g1, g2)
    _, _, x1, _, _, x2, _, _, x3, b3, _, b2, q1 = vals
    n = a.size
    return x3, q1, np.outer(b2, x1) / n, np.outer(b3, x2) / n


def predictor_and_kernel(a, r, g1, g2):
    vals = fields(a, r, g1, g2)
    _, d1, x1, _, _, x2, _, _, x3, b3, _, b2, q1 = vals
    f = np.mean(a * x3)
    k = (
        np.mean(x3**2)
        + np.mean(b3**2) * np.mean(x2**2)
        + np.mean(b2**2) * np.mean(x1**2)
        + np.mean(d1**2 * q1**2)
    )
    return f, k


def test_transformed_flow_and_kernel_identity():
    rng = np.random.default_rng(20260821)
    for n in (3, 7, 19):
        a = rng.normal(size=n)
        u = rng.normal(size=n)
        r = theta(u)
        g1 = rng.normal(size=(n, n)) / np.sqrt(n)
        g2 = rng.normal(size=(n, n)) / np.sqrt(n)

        da, dr, dg1, dg2 = feature_rhs(a, r, g1, g2)
        d1 = fields(a, r, g1, g2)[1]
        q1 = fields(a, r, g1, g2)[-1]
        np.testing.assert_allclose(dr, (1.0 + u**2) * (d1 * q1), rtol=2e-13, atol=2e-13)

        _, k0 = predictor_and_kernel(a, r, g1, g2)
        for h in (1e-4, 3e-5, 1e-5):
            fp, _ = predictor_and_kernel(
                a + h * da, r + h * dr, g1 + h * dg1, g2 + h * dg2
            )
            fm, _ = predictor_and_kernel(
                a - h * da, r - h * dr, g1 - h * dg1, g2 - h * dg2
            )
            numerical = (fp - fm) / (2.0 * h)
            np.testing.assert_allclose(numerical, k0, rtol=4e-7, atol=3e-8)

        assert k0 >= 0.0


if __name__ == "__main__":
    test_transformed_flow_and_kernel_identity()
    print("depth-3 arctan finite identities: PASS")
