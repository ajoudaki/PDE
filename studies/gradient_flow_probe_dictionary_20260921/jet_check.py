"""Deterministic algebra check, not a training or width-limit experiment.

Compare hand-derived dot-W2 coefficients with a separate truncated-series
implementation of the full finite canonical gradient field. Exactly zero
readout is intentional for this finite algebra oracle.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np


def mul(a, b):
    return np.stack([sum(a[j] * b[k-j] for j in range(k+1))
                     for k in range(len(a))])


def mm(a, b):
    return np.stack([sum(a[j] @ b[k-j] for j in range(k+1))
                     for k in range(len(a))])


def tanh_series(a):
    # y'=x'(1-y*y), independent of the manually differentiated formulas.
    y = np.zeros_like(a)
    y[0] = np.tanh(a[0])
    for k in range(len(a)-1):
        acc = np.zeros_like(a[0])
        for j in range(k+1):
            ell = k-j
            gate = -sum(y[q] * y[ell-q] for q in range(ell+1))
            if ell == 0:
                gate = gate + 1
            acc += (j+1) * a[j+1] * gate
        y[k+1] = acc/(k+1)
    return y


def vector_field(w, a, c, x, labels, weights):
    z1 = w @ (x.T/math.sqrt(2))
    h1 = tanh_series(z1)
    z2 = mm(a, h1)
    h2 = tanh_series(z2)
    f = mul(c[:, :, None], h2).mean(axis=1)
    residual = f.copy()
    residual[0] -= labels
    gate1, gate2 = -mul(h1, h1), -mul(h2, h2)
    gate1[0] += 1
    gate2[0] += 1
    delta2 = mul(c[:, :, None], gate2)
    delta1 = mul(gate1, mm(a.transpose(0, 2, 1), delta2))
    weighted_residual = residual * weights
    dw = -2 * mul(weighted_residual[:, None, :], delta1) @ (x/math.sqrt(2))
    da = -2 * mm(mul(weighted_residual[:, None, :], delta2),
                  h1.transpose(0, 2, 1))/w.shape[1]
    dc = -2 * mul(weighted_residual[:, None, :], h2).sum(axis=2)
    return dw, da, dc


def manual(w, a, x, labels, weights):
    n = len(w)
    h = np.tanh(w @ x.T/math.sqrt(2))
    z2 = a @ h
    upper = np.tanh(z2)
    p, d = 1-h*h, 1-upper*upper
    second = -2*upper*d
    u = 2*upper @ (weights*labels)
    f1 = u @ upper/n
    v = -upper @ (weights*f1)
    f2 = v @ upper/n
    b = ((u[:, None]*d)*(weights*labels)) @ h.T/n
    gram = x @ x.T/2
    reverse = a.T @ (u[:, None]*d)
    eta = p * ((p*reverse*(weights*labels)) @ gram.T)
    xi = b @ h + a @ eta
    c3 = (2/3)*((d*xi) @ (weights*labels)-upper @ (weights*f2))
    d1 = 2*b
    d2 = 2*((v[:, None]*labels-u[:, None]*f1)*d*weights) @ h.T/n
    upper3 = ((c3[:, None]*labels-v[:, None]*f1-u[:, None]*f2)*d
              +u[:, None]*labels*second*xi)
    d3 = 2*((upper3*weights) @ h.T
             +(u[:, None]*labels*d*weights) @ eta.T)/n
    return [np.zeros_like(a), d1, d2, d3]


def check_case(seed, x, labels, weights):
    rng = np.random.default_rng(seed)
    n, order = 7, 4
    w = np.zeros((order+1, n, 2))
    a = np.zeros((order+1, n, n))
    c = np.zeros((order+1, n))
    w[0] = rng.normal(size=(n, 2))
    a[0] = rng.normal(size=(n, n))/math.sqrt(n)
    expected = manual(w[0], a[0], x, labels, weights)
    for k in range(order):
        dw, da, dc = vector_field(w, a, c, x, labels, weights)
        w[k+1], a[k+1], c[k+1] = dw[k]/(k+1), da[k]/(k+1), dc[k]/(k+1)
    observed = vector_field(w, a, c, x, labels, weights)[1]
    errors = [float(np.max(np.abs(expected[k]-observed[k]))) for k in range(4)]
    assert max(errors) < 2e-13, errors
    return dict(seed=seed, width=n, inputs=x.tolist(), labels=labels.tolist(),
                weights=weights.tolist(), maximum_absolute_errors=errors,
                tolerance=2e-13, status="PASS")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    results = [
        check_case(1207, np.eye(2), np.array([0.7, -1.1]), np.array([0.5, 0.5])),
        check_case(1211, np.array([[1., 0.], [0.6, 0.8], [-0.2, 1.1]]),
                   np.array([0.4, -0.9, 0.8]), np.array([0.2, 0.3, 0.5])),
        check_case(1213, np.array([[1., 0.], [1., 0.], [0., 1.]]),
                   np.array([0.4, -0.9, 0.8]), np.array([0.2, 0.3, 0.5])),
        check_case(1217, np.eye(2), np.zeros(2), np.array([0.5, 0.5])),
    ]
    payload = dict(purpose="Finite deterministic Taylor-algebra verification only",
                   python=sys.version, numpy=np.__version__,
                   source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   cases=results)
    with output.open("x") as stream:
        json.dump(payload, stream, indent=2)
        stream.write("\n")
    print(json.dumps(payload))


if __name__ == "__main__":
    main()
