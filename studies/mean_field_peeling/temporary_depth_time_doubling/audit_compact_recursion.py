"""Exact/rational audits for the compact depth and time recursions.

This file is only a falsification aid.  The mathematical proof does not use
its output.
"""

from fractions import Fraction as Q


def depth_invariants(L, d, u, v, m, r, s, j, e, ell):
    theta = [Q(1)]
    for _ in range(L):
        theta.append(1 + d * theta[-1])

    V = [Q(0)] * (L + 1)
    M = [Q(0)] * (L + 1)
    J = [Q(0)] * (L + 1)
    b = [None] + [d ** (L - a) for a in range(1, L + 1)]
    pi = [None] + [d * b[a] for a in range(1, L + 1)]

    for a in range(1, L + 1):
        th = theta[a - 1]
        V[a] = d * V[a - 1] + th**2 * b[a] * u
        M[a] = (
            v * V[a - 1]
            + th**2 * b[a] * m
            + (d + v) * M[a - 1]
        )
        J[a] = (
            3 * th * V[a - 1] * r
            + 3 * th**3 * b[a] * j
            + 3 * th * M[a - 1] * (r + s)
            + d * (J[a - 1] + 3 * M[a - 1])
        )

    beta = [Q(0)] * (L + 2)
    gamma = [Q(0)] * (L + 2)
    gamma[L + 1] = 1
    for a in range(L, 0, -1):
        th = theta[a - 1]
        beta[a] = (
            b[a] * V[a - 1] * s
            + 3 * th**2 * b[a] ** 2 * e
            + d * beta[a + 1]
            + gamma[a + 1] ** 2 * ell
            + 2 * th * gamma[a + 1] * b[a] * m
        )
        gamma[a] = (
            pi[a]
            + th * b[a] * (r + s)
            + gamma[a + 1] * (v + d)
        )

    straight = J[L] + 3 * M[L]
    hessian = V[L] + beta[1]
    for a in range(2, L + 1):
        hessian += beta[a] + pi[a] * V[a - 1]
    return straight, hessian


def prior_depth_two(d, u, v, m, r, s, j, e, ell):
    c = 1 + d
    beta = v + c * r
    delta = d + c * s
    k = d + beta + delta
    straight = (
        3 * c**2 * m
        + 3 * c**3 * j
        + 3 * d * u * beta
        + 3 * d * k * m
        + 3 * d**2 * j
    )
    hessian = (
        c**2 * u
        + c * ell
        + 2 * c**2 * m
        + 3 * c**3 * e
        + c * u * d * s
        + 2 * u * d**2
        + 3 * d**2 * e
        + k**2 * ell
        + 2 * d * k * m
    )
    return straight, hessian


def audit():
    samples = [
        tuple(Q(k, 7) for k in range(1, 10)),
        (Q(2), Q(3), Q(-1, 3), Q(2, 5), Q(-4, 7), Q(5, 9), Q(1, 4), Q(3, 8), Q(7, 6)),
    ]
    for args in samples:
        assert depth_invariants(2, *args) == prior_depth_two(*args)

    # Identity activation: d=u=ell=1 and all other moments vanish.
    for L in range(1, 21):
        straight, hessian = depth_invariants(
            L, Q(1), Q(1), Q(0), Q(0), Q(0), Q(0), Q(0), Q(0), Q(1)
        )
        assert straight == 0
        assert hessian == Q(L * (L + 1) ** 2 * (L + 2), 6)

    # Universal time polynomials and their doubling defect.
    for t in range(1, 50):
        A = lambda n: Q(n * (4 * n * n - 3 * n + 1), 2)
        H = lambda n: 2 * n * (n - 1) * (2 * n - 1)
        assert 8 * A(t) - A(2 * t) == -3 * t * (2 * t - 1)
        assert 8 * H(t) - H(2 * t) == -12 * t * (2 * t - 1)


if __name__ == "__main__":
    audit()
    print("compact depth/time recursion audit: PASS")

