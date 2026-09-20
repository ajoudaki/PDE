"""Precommitted, finite-quadrature diagnostic; no population theorem claimed."""
from pathlib import Path
import gc
import hashlib
import json
import os
import platform
import sys
import time

import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.special import roots_hermitenorm


STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
OUT = ROOT / 'data/generated/p1_three_input_geometry_20260918/equilateral_01'
ETA = 1 / 4096
TIMES = np.array([0., 1., 2., 5., 10., 20., 40., 80., 120.])
WEIGHTS = np.array([3 / 8, 1 / 8, 1 / 2])
LABELS = np.array([1., 1., -1.])
START = time.monotonic()
DEADLINE = START + 120


class ResourceCap(Exception):
    pass


def coefficients(order):
    z, p = np.polynomial.legendre.leggauss(order)
    z = 10 * z
    p = 10 * p * np.exp(-z * z / 2) / np.sqrt(2 * np.pi)
    p /= p.sum()
    h = np.tanh(z)
    nu = p @ (h * h)
    upper = np.tanh(np.sqrt(nu) * z)
    tau = p @ (upper * upper)
    alpha = 1 - tau
    k = np.tanh(alpha * h[:, None] + np.sqrt(tau) * z[None, :])
    prod = p[:, None] * p[None, :]
    s = np.sum(prod * k * k)
    beta = np.sum(prod * h[:, None] * k)
    gamma = 1 - s
    aa = np.sqrt(nu + ETA)
    bb = np.sqrt(s + ETA - beta * beta / (nu + ETA))
    cc = np.sqrt(tau + ETA)
    dh = alpha * nu / (aa * cc)
    dk = (alpha * beta * ETA / (nu + ETA) + tau * gamma) / (bb * cc)
    return dict(nu=nu, tau=tau, alpha=alpha, s=s, beta=beta,
                gamma=gamma, aa=aa, bb=bb, cc=cc, dh=dh, dk=dk)


def tensor_rule(q, dimension):
    z, p = roots_hermitenorm(q)
    p = p / np.sqrt(2 * np.pi)
    inds = np.indices((q,) * dimension).reshape(dimension, -1).T
    return z[inds], np.prod(p[inds], axis=1)


def one_solve(q, theta, constants, tight=False):
    low, pl = tensor_rule(q, 4)
    up, pu = tensor_rule(q, 2)
    g = low[:, :2].copy()
    h = np.tanh(g)
    k = np.tanh(constants['alpha'] * h + np.sqrt(constants['tau']) * low[:, 2:])
    b1 = np.concatenate((h / constants['aa'],
                         (k - constants['beta'] * h / (constants['nu'] + ETA))
                         / constants['bb']), axis=1)
    b2 = np.tanh(np.sqrt(constants['nu']) * up) / constants['cc']
    angles = theta + 2 * np.pi * np.arange(3) / 3
    directions = np.stack((np.cos(angles), np.sin(angles)), axis=1)
    matrix = np.concatenate((constants['dh'] * np.eye(2),
                             constants['dk'] * np.eye(2)), axis=1)
    nlow, nup = len(pl), len(pu)
    boundary = 2 * nlow
    b1weighted = b1.T * pl
    b2weighted = b2.T * pu
    state0 = np.concatenate((g.ravel(), np.zeros(nup), matrix.ravel()))

    def unpack(state):
        return (state[:boundary].reshape(nlow, 2),
                state[boundary:boundary+nup], state[boundary+nup:].reshape(2, 4))

    def evaluate(state):
        w, c, m = unpack(state)
        lower = np.tanh(w @ directions.T)
        a = b1weighted @ lower
        code = m @ a
        upper = np.tanh(b2 @ code)
        f = (pu * c) @ upper
        residual = f - LABELS
        d = b2weighted @ (c[:, None] * (1 - upper * upper))
        back = b1 @ (m.T @ d)
        pr = WEIGHTS * residual
        wdot = -2 * (((1 - lower * lower) * back * pr) @ directions)
        cdot = -2 * upper @ pr
        mdot = -2 * (d * pr) @ a.T
        return (lower, upper, code, f, residual, wdot, cdot, mdot)

    def rhs(t, state):
        if time.monotonic() >= DEADLINE:
            raise ResourceCap()
        values = evaluate(state)
        return np.concatenate((values[5].ravel(), values[6], values[7].ravel()))

    lower0, upper0 = evaluate(state0)[:2]
    initial_time = time.monotonic()
    result = solve_ivp(rhs, (0, 120), state0, method='DOP853', t_eval=TIMES,
                       rtol=2e-9 if tight else 2e-7,
                       atol=2e-11 if tight else 2e-9)
    tag = f'q{q}_angle{round(theta * 180 / np.pi):02d}' + ('_tight' if tight else '')
    records = []
    for t, state in zip(result.t, result.y.T):
        lower, upper, code, f, r, wd, cd, md = evaluate(state)
        w, c, m = unpack(state)
        gram = upper.T @ (pu[:, None] * upper)
        diss = np.sum(pl[:, None] * wd * wd) + pu @ (cd * cd) + np.sum(md * md)
        records.append(dict(t=float(t), loss=float(WEIGHTS @ (r * r)),
            predictions=f.tolist(), code=code.tolist(),
            readout_norm=float(np.sqrt(pu @ (c * c))),
            matrix_norm=float(np.linalg.norm(m)),
            gram_eigenvalues=np.linalg.eigvalsh(gram).tolist(),
            dissipation=float(diss),
            lower_displacement=float(np.sqrt(np.sum(pl[:, None] * WEIGHTS * (lower-lower0)**2))),
            upper_displacement=float(np.sqrt(np.sum(pu[:, None] * WEIGHTS * (upper-upper0)**2)))))
    report = dict(tag=tag, q=q, angle=theta, tight=tight,
                  status='complete' if result.success and result.t[-1] == 120 else 'failed',
                  message=result.message, evaluations=result.nfev,
                  seconds=time.monotonic()-initial_time, records=records)
    (OUT / f'{tag}.json').write_text(json.dumps(report, indent=2) + '\n')
    np.savez_compressed(OUT / f'{tag}_endpoint.npz', state=result.y[:, -1])
    return report


def differences(first, second):
    if len(first['records']) != len(TIMES) or len(second['records']) != len(TIMES):
        return dict(valid=False)
    pred = max(np.max(np.abs(np.array(a['predictions']) - b['predictions']))
               for a, b in zip(first['records'], second['records']))
    code = max(np.max(np.abs(np.array(a['code']) - b['code']))
               for a, b in zip(first['records'], second['records']))
    return dict(valid=True, max_prediction_difference=float(pred), max_code_difference=float(code))


def main():
    OUT.mkdir(parents=True, exist_ok=False)
    (OUT / 'source.py').write_bytes(Path(__file__).read_bytes())
    (OUT / 'plan.md').write_bytes((STUDY / 'diagnostic_plan.md').read_bytes())
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in [Path(__file__), STUDY/'diagnostic_plan.md',
                        ROOT/'docs/observable_p1.md', ROOT/'docs/global_nonlinear.md']}
    c128, const = coefficients(128), coefficients(256)
    difference = max(abs(c128[k] - const[k]) for k in const)
    metadata = dict(python=sys.version, numpy=np.__version__, scipy=scipy.__version__,
        platform=platform.platform(), processor=platform.processor(), dtype='float64',
        command='OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python studies/p1_three_input_geometry_20260918/diagnostic.py',
        cwd=str(ROOT), head='019e3630237e33f58b9636c0aa67a039bebf0182',
        threads={k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']},
        source_hashes=hashes, coefficients=const, coefficient_refinement=difference,
        status='running', solves=[])
    (OUT / 'metadata.json').write_text(json.dumps(metadata, indent=2)+'\n')
    if difference > 1e-9:
        metadata['status'] = 'coefficient_gate_failed'
    else:
        try:
            for q in [8, 12, 16]:
                for theta in [0, np.pi/12, np.pi/6]:
                    report = one_solve(q, theta, const)
                    metadata['solves'].append(report)
                    (OUT / 'metadata.json').write_text(json.dumps(metadata, indent=2)+'\n')
                    print(report['tag'], report['status'], report['records'][-1]['loss'], flush=True)
                    gc.collect()
            metadata['solves'].append(one_solve(12, np.pi/12, const, tight=True))
            metadata['status'] = 'complete'
        except ResourceCap:
            metadata['status'] = 'resource_cap'
    metadata['seconds'] = time.monotonic() - START
    (OUT / 'metadata.json').write_text(json.dumps(metadata, indent=2)+'\n')
    lookup = {r['tag']:r for r in metadata['solves']}
    comparisons = {}
    for angle in [0, 15, 30]:
        a, b = f'q12_angle{angle:02d}', f'q16_angle{angle:02d}'
        if a in lookup and b in lookup:
            diff = differences(lookup[a], lookup[b])
            diff['resolved_fitting'] = bool(diff['valid'] and
                diff['max_prediction_difference'] <= 2e-4 and
                diff['max_code_difference'] <= 2e-3 and
                max(lookup[a]['records'][-1]['loss'], lookup[b]['records'][-1]['loss']) <= 1e-6)
            comparisons[str(angle)] = diff
    if 'q12_angle15_tight' in lookup:
        comparisons['time_refinement'] = differences(lookup['q12_angle15'], lookup['q12_angle15_tight'])
    increases = [max(np.diff([s['loss'] for s in r['records']]), default=0) for r in lookup.values()]
    summary = dict(status=metadata['status'], seconds=metadata['seconds'],
        coefficient_difference=difference, max_sampled_loss_increase=float(max(increases, default=0)),
        comparisons=comparisons)
    (OUT / 'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == '__main__':
    main()
