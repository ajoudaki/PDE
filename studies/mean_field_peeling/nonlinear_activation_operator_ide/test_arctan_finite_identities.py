import numpy as np


def theta(u):
    return u + u**3 / 3.0


def theta_inverse(r):
    # sinh(3 asinh(r)/3) is the real inverse of u + u^3/3.
    return 2.0 * np.sinh(np.arcsinh(1.5 * r) / 3.0)


def fields(a, r, g):
    u = theta_inverse(r)
    x = np.arctan(u)
    c = 1.0 / (1.0 + u**2)
    z = g @ x
    y = np.arctan(z)
    d = 1.0 / (1.0 + z**2)
    b = a * d
    q = g.T @ b
    return u, x, c, z, y, d, b, q


def feature_rhs(a, r, g):
    _, x, _, _, y, _, b, q = fields(a, r, g)
    n = a.size
    return y, q, np.outer(b, x) / n


def predictor_and_kernel(a, r, g):
    _, x, c, _, y, _, b, q = fields(a, r, g)
    f = np.mean(a * y)
    k = (
        np.mean(y**2)
        + np.mean(b**2) * np.mean(x**2)
        + np.mean(c**2 * q**2)
    )
    return f, k


def test_theta_inverse():
    r = np.linspace(-50.0, 50.0, 1001)
    u = theta_inverse(r)
    np.testing.assert_allclose(theta(u), r, rtol=2e-13, atol=2e-13)


def test_transformed_feature_flow_and_kernel_identity():
    rng = np.random.default_rng(20260821)
    for n in (3, 7, 19):
        a = rng.normal(size=n)
        u = rng.normal(size=n)
        r = theta(u)
        g = rng.normal(size=(n, n)) / np.sqrt(n)

        da, dr, dg = feature_rhs(a, r, g)
        _, _, c, _, _, _, _, q = fields(a, r, g)

        # In the original coordinate, u' = phi'(u) G^*B.
        du = c * q
        directional_r = (1.0 + u**2) * du
        np.testing.assert_allclose(dr, directional_r, rtol=2e-13, atol=2e-13)

        f0, k0 = predictor_and_kernel(a, r, g)
        for h in (1e-4, 3e-5, 1e-5):
            fp, _ = predictor_and_kernel(a + h * da, r + h * dr, g + h * dg)
            fm, _ = predictor_and_kernel(a - h * da, r - h * dr, g - h * dg)
            numerical = (fp - fm) / (2.0 * h)
            np.testing.assert_allclose(numerical, k0, rtol=2e-7, atol=2e-8)

        assert np.isfinite(f0)
        assert k0 >= 0.0


if __name__ == "__main__":
    test_theta_inverse()
    test_transformed_feature_flow_and_kernel_identity()
    print("arctan finite identities: PASS")
