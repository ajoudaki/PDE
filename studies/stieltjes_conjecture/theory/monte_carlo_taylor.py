#!/usr/bin/env python3
"""Vectorized finite-width Taylor arithmetic for exploratory sign estimates.

This is not a proof certificate.  It is used only to decide which exact
Hankel calculation is most likely to be decisive.
"""

import argparse
import math
import numpy as np


def batch_coefficients(rng, samples, n, order=13):
    u = [rng.standard_normal((samples, n))]
    c = [rng.standard_normal((samples, n))]
    b = [rng.standard_normal((samples, n, n)) / math.sqrt(n)]
    q = []
    v = []

    def extend_qv(k):
        qk = sum(u[j] * u[k - j] for j in range(k + 1))
        q.append(qk)
        vk = sum(np.einsum("spj,sj->sp", b[j], q[k - j])
                 for j in range(k + 1))
        v.append(vk)

    extend_qv(0)
    for k in range(order):
        d = [sum(c[j] * v[t - j] for j in range(t + 1))
             for t in range(k + 1)]

        c_rhs = sum(v[j] * v[k - j] for j in range(k + 1))
        b_rhs = sum(np.einsum("sp,si->spi", d[j], q[k - j])
                    for j in range(k + 1)) * (2.0 / n)

        r = [sum(np.einsum("spi,sp->si", b[j], d[t - j])
                 for j in range(t + 1)) for t in range(k + 1)]
        u_rhs = sum(u[j] * r[k - j] for j in range(k + 1)) * 4.0

        scale = 1.0 / (k + 1)
        u.append(u_rhs * scale)
        b.append(b_rhs * scale)
        c.append(c_rhs * scale)
        extend_qv(k + 1)

    f = []
    for k in range(order + 1):
        v2 = sum(v[j] * v[k - j] for j in range(k + 1))
        # Need the full convolution c * (v*v), not only c[0].
        val = np.zeros(samples)
        for a in range(k + 1):
            vv = sum(v[j] * v[k - a - j]
                     for j in range(k - a + 1))
            val += np.mean(c[a] * vv, axis=1)
        f.append(val)
    return f


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--width", type=int, default=16)
    p.add_argument("--samples", type=int, default=1000)
    p.add_argument("--batch", type=int, default=20)
    p.add_argument("--seed", type=int, default=1234)
    args = p.parse_args()
    rng = np.random.default_rng(args.seed)
    vals = {k: [] for k in range(1, 14, 2)}
    left = args.samples
    while left:
        size = min(left, args.batch)
        f = batch_coefficients(rng, size, args.width)
        for k in vals:
            vals[k].append(f[k])
        left -= size
    for k, chunks in vals.items():
        x = np.concatenate(chunks)
        mean = x.mean()
        se = x.std(ddof=1) / math.sqrt(len(x))
        print(k, f"coef={mean:.12e}", f"se={se:.4e}",
              f"derivative={mean*math.factorial(k):.12e}")


if __name__ == "__main__":
    main()
