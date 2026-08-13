import argparse
import json
import time

import numpy as np


def feature_jet(width: int, order: int, gamma: float, seed: int):
    """Taylor coefficients of the finite-width feature-ascent output.

    u_i is the first preactivation, B_ji the second-layer weight,
    c_j = n W^3_j, and v_j = gamma * sum_i B_ji u_i^2.
    Arrays store ordinary power-series coefficients, not derivatives.
    """
    rng = np.random.default_rng(seed)
    n = width

    u = np.zeros((order + 1, n), dtype=np.float64)
    c = np.zeros((order + 1, n), dtype=np.float64)
    B = np.zeros((order + 1, n, n), dtype=np.float64)
    p = np.zeros_like(u)  # u^2
    v = np.zeros_like(c)
    q = np.zeros_like(c)  # v^2
    d = np.zeros_like(c)  # c*v
    e = np.zeros_like(u)  # B^T*(c*v), with series convolution
    f = np.zeros(order + 1, dtype=np.float64)

    u[0] = rng.standard_normal(n)
    B[0] = rng.standard_normal((n, n)) / np.sqrt(n)
    c[0] = rng.standard_normal(n)

    for k in range(order + 1):
        pk = np.zeros(n)
        for a in range(k + 1):
            pk += u[a] * u[k - a]
        p[k] = pk

        vk = np.zeros(n)
        for a in range(k + 1):
            vk += B[a] @ p[k - a]
        v[k] = gamma * vk

        qk = np.zeros(n)
        dk = np.zeros(n)
        for a in range(k + 1):
            qk += v[a] * v[k - a]
            dk += c[a] * v[k - a]
        q[k] = qk
        d[k] = dk

        ek = np.zeros(n)
        for a in range(k + 1):
            ek += B[a].T @ d[k - a]
        e[k] = ek

        fk = 0.0
        for a in range(k + 1):
            fk += np.dot(c[a], q[k - a])
        f[k] = gamma * fk / n

        if k == order:
            break

        c[k + 1] = gamma * q[k] / (k + 1)

        brhs = np.zeros((n, n))
        for a in range(k + 1):
            brhs += d[a, :, None] * p[k - a, None, :]
        B[k + 1] = (2.0 * gamma * gamma / n) * brhs / (k + 1)

        urhs = np.zeros(n)
        for a in range(k + 1):
            urhs += u[a] * e[k - a]
        u[k + 1] = 4.0 * gamma * gamma * urhs / (k + 1)

    return f


def mul(a, b, order):
    out = np.zeros(order + 1)
    for i in range(min(len(a), order + 1)):
        jmax = min(len(b) - 1, order - i)
        if jmax >= 0:
            out[i:i + jmax + 1] += a[i] * b[:jmax + 1]
    return out


def compose(a, b, order):
    """a(b(y)), truncated; b[0] must vanish."""
    out = np.zeros(order + 1)
    power = np.zeros(order + 1)
    power[0] = 1.0
    for k in range(min(len(a), order + 1)):
        out += a[k] * power
        power = mul(power, b, order)
    return out


def inverse_series(f, order):
    """Inverse of f(s)-f(0), through y**order."""
    if f[1] == 0:
        raise ValueError("zero linear coefficient")
    inv = np.zeros(order + 1)
    inv[1] = 1.0 / f[1]
    base = np.zeros(order + 1)
    base[:min(len(f), order + 1)] = f[:min(len(f), order + 1)]
    base[0] = 0.0
    for k in range(2, order + 1):
        trial = inv.copy()
        trial[k] = 0.0
        other = compose(base, trial, k)[k]
        inv[k] = -other / f[1]
    return inv


def output_kernel_jet(f, order):
    """Coefficients of F'(F^{-1}(F(0)+y)) via 1/(inverse)' ."""
    inv = inverse_series(f, order + 1)
    deriv = np.array([(k + 1) * inv[k + 1] for k in range(order + 1)])
    rec = np.zeros(order + 1)
    rec[0] = 1.0 / deriv[0]
    for k in range(1, order + 1):
        rec[k] = -sum(deriv[j] * rec[k - j] for j in range(1, k + 1)) / deriv[0]
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--width", type=int, required=True)
    ap.add_argument("--order", type=int, default=13)
    ap.add_argument("--gamma", type=float, default=1.0)
    ap.add_argument("--seeds", type=int, default=4)
    ap.add_argument("--seed-offset", type=int, default=0)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    rows = []
    krows = []
    start = time.time()
    for s in range(args.seed_offset, args.seed_offset + args.seeds):
        t0 = time.time()
        coef = feature_jet(args.width, args.order, args.gamma, s)
        paired_coef = coef.copy()
        paired_coef[0::2] = 0.0
        kcoef = output_kernel_jet(paired_coef, args.order - 1)
        rows.append(coef)
        krows.append(kcoef)
        if not args.quiet:
            print(json.dumps({
                "width": args.width,
                "seed": s,
                "seconds": time.time() - t0,
                "coefficients": coef.tolist(),
                "kernel_coefficients": kcoef.tolist(),
            }), flush=True)
    arr = np.array(rows)
    karr = np.array(krows)
    print(json.dumps({
        "summary": True,
        "width": args.width,
        "seeds": args.seeds,
        "seconds": time.time() - start,
        "mean": arr.mean(axis=0).tolist(),
        "stderr": (arr.std(axis=0, ddof=1) / np.sqrt(len(arr))).tolist() if len(arr) > 1 else None,
        "kernel_mean": karr.mean(axis=0).tolist(),
        "kernel_stderr": (karr.std(axis=0, ddof=1) / np.sqrt(len(karr))).tolist() if len(karr) > 1 else None,
    }))


if __name__ == "__main__":
    main()
