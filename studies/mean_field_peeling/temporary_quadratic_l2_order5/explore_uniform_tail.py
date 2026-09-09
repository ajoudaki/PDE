#!/usr/bin/env python3
"""Monte Carlo pressure test for the nonlocal quadratic step-doubling tail.

This is exploratory only; it is not used as proof.
"""

import numpy as np


def run(init, steps, h, eps):
    a, w, u = (x.copy() for x in init)
    scale = np.sqrt(1.0 + 3.0 * eps * eps)

    def phi(x):
        return (x + eps * x * x) / scale

    def dphi(x):
        return (1.0 + 2.0 * eps * x) / scale

    n = len(a)
    root_n = np.sqrt(n)
    for _ in range(steps):
        x = phi(u)
        z = w @ x / root_n
        y = phi(z)
        c = a * dphi(z)
        back = w.T @ c / root_n
        # Simultaneous Euler update: all right sides use the old state.
        a_new = a + h * y
        w_new = w + (h / root_n) * np.outer(c, x)
        u_new = u + h * back * dphi(u)
        a, w, u = a_new, w_new, u_new
    x = phi(u)
    z = w @ x / root_n
    return np.mean(a * phi(z))


def main():
    rng = np.random.default_rng(90210)
    widths = [128]
    eps_values = [0.0, 0.01, 0.05, 0.2]
    rho_values = [0.02, 0.05, 0.1]
    horizons = [2, 4, 8, 16, 32]
    trials = 12
    for n in widths:
        for eps in eps_values:
            for rho in rho_values:
                print(f"n={n} eps={eps} rho={rho}")
                for t in horizons:
                    h = rho / t
                    y = eps * eps
                    j = (48 + 3446*y + 54820*y**2 + 387560*y**3
                         + 1380876*y**4 + 2399274*y**5
                         + 1592952*y**6) / (1 + 3*y)**6
                    kappa = 0.5 * t * (2*t - 1) * j
                    values = []
                    for _ in range(trials):
                        init = (
                            rng.standard_normal(n),
                            rng.standard_normal((n, n)),
                            rng.standard_normal(n),
                        )
                        fine = run(init, 2 * t, h, eps)
                        coarse = run(init, t, 2 * h, eps)
                        values.append((fine - coarse - kappa*h**3) * t / rho**5)
                    values = np.asarray(values)
                    print(t, float(np.mean(values)), float(np.std(values)))


if __name__ == "__main__":
    main()
