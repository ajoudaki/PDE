"""Deterministic algebra checks; no optimizer trajectory or training experiment.

Run with --output pointing to a fresh study-generated directory.
Floating point checks supplement, and do not replace, the mathematical proofs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.linalg import expm


def gate(z):
    return 1 / np.cosh(z) ** 2


def curvature(z):
    return -2 * np.tanh(z) * gate(z)


def primitive(z):
    return z / 2 + np.sinh(2 * z) / 4


def shifted(w, shift):
    target = primitive(w) + shift
    z = w.copy()
    for _ in range(12):
        z -= (primitive(z) - target) * gate(z)
    assert np.max(np.abs(primitive(z) - target)) < 1e-12
    return z


def query(w, A, c, u):
    h = np.tanh(w @ u)
    z = A @ h
    H = np.tanh(z)
    delta = c * gate(z)
    Q = A.T @ delta
    return h, z, H, delta, Q, c @ H / len(c)


def raw_field(w, A, c, law):
    n = len(c)
    W, B, d = np.zeros_like(w), np.zeros_like(A), np.zeros_like(c)
    for p, u, y in law:
        h, z, H, delta, Q, f = query(w, A, c, u)
        r = f - y
        W -= 2 * p * r * (gate(w @ u) * Q)[:, None] * u
        B -= 2 * p * r * np.outer(delta, h) / n
        d -= 2 * p * r * H
    return W, B, d


def flatten(v):
    return np.concatenate([x.ravel() for x in v])


def norm(v):
    return np.linalg.norm(flatten(v))


def clock_field(w, A, c, law):
    W, B, d = raw_field(w, A, c, law)
    return W / gate(w), B, d


def tangent(w, A, c, v, ref, sigma):
    n = len(c)
    xi, B, d = v
    dw = gate(w) * xi
    dx, dB, dd = np.zeros_like(xi), np.zeros_like(B), np.zeros_like(d)
    for p, u, y in ref:
        a = int(np.argmax(u))
        h, z, H, delta, Q, f = query(w, A, c, u)
        dh = gate(w[:, a]) ** 2 * xi[:, a]
        dz = B @ h + A @ dh
        dH = gate(z) * dz
        ddelta = d * gate(z) + c * curvature(z) * dz
        dQ = B.T @ delta + A.T @ ddelta
        df = (d @ H + c @ dH) / n
        r = f - y
        dx[:, a] -= 2 * p * (df * Q + r * dQ)
        dB -= 2 * p * (df * np.outer(delta, h)
                      + r * np.outer(ddelta, h)
                      + r * np.outer(delta, dh)) / n
        dd -= 2 * p * (df * H + r * dH)
    source = clock_field(w, A, c, sigma)
    return tuple(a + b for a, b in zip((dx, dB, dd), source))


def metric_flat(v):
    w, B, d = v
    n = len(d)
    return np.concatenate([w.ravel() / np.sqrt(n), B.ravel(), d / np.sqrt(n)])


def run():
    # These are fixed test matrices, not sampled or trained networks.
    w = np.array([[.2, -.4], [1.1, .3], [-.8, .6]])
    A = np.array([[.2, -.1, .4], [.3, .7, -.2], [-.5, .1, .6]])
    c = np.array([.25, -.4, .15])  # nonzero stored readout is essential
    xi = np.array([[.3, -.1], [-.2, .5], [.4, .2]])
    B = np.array([[.1, -.2, .3], [.4, .2, -.1], [-.2, .1, .2]])
    d = np.array([.2, -.3, .4])
    v = xi, B, d
    e1, e2 = np.eye(2)
    ref = [(0.5, e1, 1.), (0.5, e2, -1.)]
    nu = [(.17, np.array([.6, .8]), .7),
          (.23, e1, -.3), (.60, np.array([-.8, .6]), -1.2)]
    sigma = nu + [(-p, u, y) for p, u, y in ref]
    exact = tangent(w, A, c, v, ref, sigma)
    errors = []
    for hstep in (.002, .001, .0005, .00025):
        plus_law = ref + [(hstep * p, u, y) for p, u, y in sigma]
        minus_law = ref + [(-hstep * p, u, y) for p, u, y in sigma]
        plus = clock_field(shifted(w, hstep * xi), A + hstep * B,
                           c + hstep * d, plus_law)
        minus = clock_field(shifted(w, -hstep * xi), A - hstep * B,
                            c - hstep * d, minus_law)
        fd = tuple((a - b) / (2 * hstep) for a, b in zip(plus, minus))
        errors.append(norm(tuple(a - b for a, b in zip(fd, exact))))
    assert all(a / b > 3.8 for a, b in zip(errors, errors[1:]))
    assert errors[-1] < 1e-7

    # Independent raw-loss directional derivative checks mobilities and n factors.
    raw_v = gate(w) * xi, B, d
    raw_grad = tuple(-q for q in raw_field(w, A, c, ref))
    def loss(W, M, C):
        return sum(p * (query(W, M, C, u)[-1] - y) ** 2 for p, u, y in ref)
    hstep = 1e-5
    fd_loss = (loss(w + hstep * raw_v[0], A + hstep * B, c + hstep * d)
               - loss(w - hstep * raw_v[0], A - hstep * B, c - hstep * d)) / (2*hstep)
    metric_pair = metric_flat(raw_grad) @ metric_flat(raw_v)
    assert abs(fd_loss - metric_pair) < 1e-9

    # S* D S agrees with the complete weighted raw training Gram.
    scol, gcol = [], []
    for p, u, y in ref:
        h, z, H, delta, Q, f = query(w, A, c, u)
        a = int(np.argmax(u))
        X = np.zeros_like(w)
        X[:, a] = Q
        s = X, np.outer(delta, h) / len(c), H
        g = gate(w) * X, s[1], s[2]
        scol.append(np.sqrt(p) * metric_flat(s))
        gcol.append(np.sqrt(p) * metric_flat(g))
    S = np.column_stack(scol)
    G = np.column_stack(gcol)
    D = np.diag(np.concatenate([gate(w).ravel() ** 2,
                               np.ones(A.size + c.size)]))
    K = S.T @ D @ S
    assert np.linalg.norm(K - G.T @ G) < 1e-14

    # Exactly singular rank-one Gram, nonnormal S E, strictly positive metric.
    S = np.array([[1., 2.], [-.5, -1.], [.75, 1.5], [.2, .4]])
    D = np.diag([.001, .3, .7, 1.])
    E = S.T @ D
    K = E @ S
    Kplus = np.linalg.pinv(K, rcond=1e-13)
    singular_errors = []
    for t in (0., .1, 1., 10., 100.):
        direct = expm(-2*t*S@E)
        formula = np.eye(4) + S @ Kplus @ (expm(-2*t*K)-np.eye(2)) @ E
        singular_errors.append(float(np.linalg.norm(direct-formula)))
        assert np.linalg.norm(direct-formula) < 2e-12
    z = np.array([-2., 1.])
    assert np.linalg.norm(K@z) < 1e-14 and np.linalg.norm(S@z) < 1e-14

    # Why kernel compatibility cannot be omitted in a general factorization.
    badS, badE = np.array([[1.], [0.]]), np.array([[0., 1.]])
    assert np.linalg.norm(badE@badS) == 0
    assert np.linalg.norm(expm(-20*badS@badE)) > 19

    return dict(tangent_central_difference_errors=errors,
                loss_metric_error=float(abs(fd_loss-metric_pair)),
                singular_semigroup_errors=singular_errors,
                checks="PASS", scope="deterministic algebra; no training; no proof of limiting estimates")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    target = Path(args.output)
    target.mkdir(parents=True, exist_ok=False)
    report = run()
    report.update(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (target/'results.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
