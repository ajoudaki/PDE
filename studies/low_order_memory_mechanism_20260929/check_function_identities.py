"""Deterministic algebra checks; no trajectories, optimization, or experiments."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform

import numpy as np


def fields(weights, readout, x):
    z, h = [], []
    for ell, w in enumerate(weights):
        z.append(w @ (x / np.sqrt(x.size) if ell == 0 else h[-1]))
        h.append(np.tanh(z[-1]))
    delta = [None] * len(weights)
    delta[-1] = readout * (1 - h[-1] ** 2)
    for ell in range(len(weights) - 2, -1, -1):
        delta[ell] = (1 - h[ell] ** 2) * (weights[ell + 1].T @ delta[ell + 1])
    return h, delta


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    rng = np.random.default_rng(290920262)
    checks = {}
    n, m, d, depth = 5, 3, 2, 3
    xtrain, xtest = rng.normal(size=(m, d)), rng.normal(size=d)
    wfirst = rng.normal(size=(n, d))
    base = rng.normal(size=(depth - 1, n, n)) / np.sqrt(n)
    readout = rng.normal(size=n)
    r = rng.normal(size=m)
    rho, tau = np.linalg.norm(r) / np.sqrt(m), 2.3

    for q in (1, 2, 3, 5):
        modes = 2 * np.arange(q) + 1
        b = rng.normal(size=(depth - 1, m, q, n)) / 3
        c = rng.normal(size=b.shape) / 4
        weights = [wfirst]
        for ell in range(depth - 1):
            pairing = np.einsum('k,aki,akj->ij', modes, c[ell], b[ell])
            weights.append(base[ell] - 2 * pairing / (m * n * tau))
        hf, df = zip(*(fields(weights, readout, x) for x in xtrain))
        hx, dx = fields(weights, readout, xtest)
        wdot = [-2 / m * sum(r[a] * np.outer(df[a][0], xtrain[a] / np.sqrt(d))
                            for a in range(m))]
        u_dot = -2 / m * sum(r[a] * hf[a][-1] for a in range(m))
        hhat, bhat = [], []
        for ell in range(depth - 1):
            db, dc = np.zeros_like(b[ell]), np.zeros_like(c[ell])
            for a in range(m):
                for k in range(q):
                    db[a, k] = rho * hf[a][ell] - rho / tau * (
                        k * b[ell, a, k] + np.einsum('k,ki->i', modes[:k], b[ell, a, :k]))
                    dc[a, k] = r[a] * df[a][ell + 1] - rho / tau * (
                        k * c[ell, a, k] + np.einsum('k,ki->i', modes[:k], c[ell, a, :k]))
            pair = np.einsum('k,aki,akj->ij', modes, c[ell], b[ell])
            dpair = (np.einsum('k,aki,akj->ij', modes, dc, b[ell])
                     + np.einsum('k,aki,akj->ij', modes, c[ell], db))
            wdot.append(-2 * dpair / (m * n * tau) + 2 * rho * pair / (m * n * tau**2))
            hhat.append(np.einsum('k,aki->ai', modes, b[ell]) / tau)
            bhat.append(np.einsum('k,aki->ai', modes, c[ell]) / tau)
        actual = u_dot @ hx[-1] / n + dx[0] @ wdot[0] @ xtest / (n * np.sqrt(d))
        actual += sum(dx[ell] @ wdot[ell] @ hx[ell - 1] / n for ell in range(1, depth))
        kernel, transport = np.zeros(m), 0.0
        for a in range(m):
            kernel[a] = hx[-1] @ hf[a][-1] / n
            kernel[a] += (xtest @ xtrain[a] / d) * (dx[0] @ df[a][0] / n)
            for ell in range(1, depth):
                kernel[a] += (dx[ell] @ df[a][ell] / n) * (hx[ell - 1] @ hhat[ell - 1][a] / n)
                transport += -2 / (m * n**2) * (dx[ell] @ bhat[ell - 1][a]) * (
                    (hf[a][ell - 1] - hhat[ell - 1][a]) @ hx[ell - 1])
        predicted = -2 / m * kernel @ r + rho * transport
        checks[f'q{q}_whole_function_velocity'] = float(abs(actual - predicted))

        hmatrix = np.stack([a[-1] for a in hf], axis=1)
        gram = hmatrix.T @ hmatrix / n
        pinv = np.linalg.pinv(gram)
        predictions = hmatrix.T @ readout / n
        perpendicular = readout - hmatrix @ pinv @ predictions
        decomposition = (hmatrix.T @ hx[-1] / n) @ pinv @ predictions + perpendicular @ hx[-1] / n
        checks[f'q{q}_terminal_decomposition'] = float(abs(decomposition - readout @ hx[-1] / n))
        checks[f'q{q}_training_invisibility'] = float(np.max(np.abs(hmatrix.T @ perpendicular / n)))
        checks[f'q{q}_readout_norm_split'] = float(abs(
            readout @ readout / n - predictions @ pinv @ predictions - perpendicular @ perpendicular / n))

    for depth in (2, 3, 5):
        weights = [rng.normal(size=(n, d))] + [rng.normal(size=(n, n)) / np.sqrt(n) for _ in range(depth - 1)]
        x = xtrain[0]
        h, _ = fields(weights, np.zeros(n), x)
        _, delta = fields(weights, h[-1], x)
        gradients = [np.outer(delta[0], x / np.sqrt(d)) / n]
        gradients += [np.outer(delta[ell], h[ell - 1]) / n for ell in range(1, depth)]
        directions = [n * gradients[0]] + gradients[1:]
        variation = None
        for ell in range(depth):
            dz = directions[ell] @ (x / np.sqrt(d) if ell == 0 else h[ell - 1])
            if ell:
                dz += weights[ell] @ variation
            variation = (1 - h[ell]**2) * dz
        squared_gradient = n * np.sum(gradients[0]**2) + sum(np.sum(g**2) for g in gradients[1:])
        checks[f'depth{depth}_cubic_positive_identity'] = float(abs(h[-1] @ variation / n - squared_gradient))
        alpha = h[-1] @ h[-1] / n
        beta = 2 * squared_gradient / 3
        ctrain = (variation @ h[-1] / 6 + h[-1] @ variation / 2) / n
        checks[f'depth{depth}_calibrated_cubic_zero_on_train'] = float(abs(ctrain / alpha**3 - alpha * beta / alpha**4))
        assert squared_gradient > 0

    # Algebraic elimination behind the local one-function response law.
    amat = 3 * np.eye(m) + rng.normal(size=(m, m)) / 10
    vtrain, row, residual_integral = (rng.normal(size=m) for _ in range(3))
    vtest, clock_increment = 0.7, 0.2
    eta = -amat @ residual_integral + vtrain * clock_increment
    deformation = vtest - row @ np.linalg.solve(amat, vtrain)
    observed = -row @ residual_integral + vtest * clock_increment
    predicted = row @ np.linalg.solve(amat, eta) + deformation * clock_increment
    checks['local_response_elimination'] = float(abs(observed - predicted))
    checks['local_deformation_zero_on_train'] = float(np.max(np.abs(
        vtrain - amat @ np.linalg.solve(amat, vtrain))))
    aa, cc, ax, cx = 2.4, 0.3, 0.8, -0.2
    checks['one_sided_response_difference'] = float(abs(
        (ax + cx) / (aa + cc) - (ax - cx) / (aa - cc)
        - 2 * (aa * cx - ax * cc) / (aa**2 - cc**2)))

    # Static sign check for the explicitly derived reachable scalar witness.
    pscalar, mixing = 0.7, 1.2
    hscalar = np.tanh(pscalar)
    ascalar = np.tanh(mixing * hscalar)
    gate = 1 - ascalar**2
    htest = np.tanh(2 * pscalar)
    atest = np.tanh(mixing * htest)
    gatetest = 1 - atest**2
    bracket = gatetest * htest - atest / ascalar * gate * hscalar
    via_sinh = atest * (2 * htest / np.sinh(2 * mixing * htest)
                         - 2 * hscalar / np.sinh(2 * mixing * hscalar))
    checks['reachable_clock_drift_sign_identity'] = float(abs(bracket - via_sinh))
    assert bracket < 0
    for q in (1, 2, 3, 5):
        checks[f'q{q}_endpoint_weight_sum'] = float(abs(sum(2 * k + 1 for k in range(q)) - q**2))

    for name, value in checks.items():
        if not np.isfinite(value) or value >= 1e-9:
            raise AssertionError((name, value))
    root = Path(__file__).resolve().parent
    sources = ['MODEL.md', 'ACTIVITY_AND_FUNCTION.md', 'FINAL_FUNCTION_ROUTE.md', 'DIRECT_LEARNING_ROUTE.md',
               'INTRINSIC_GEOMETRY_ROUTE.md', Path(__file__).name]
    result = dict(scope='Static deterministic algebra only; no neural trajectories or empirical claims',
                  python=platform.python_version(), numpy=np.__version__, seed=290920262,
                  tolerance=1e-9, checks=checks, maximum_absolute_error=max(checks.values()),
                  passed=True, source_sha256={p: hashlib.sha256((root / p).read_bytes()).hexdigest() for p in sources})
    (args.output / 'checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'checks': len(checks), 'passed': True, 'max_error': max(checks.values())}))


if __name__ == '__main__':
    main()
