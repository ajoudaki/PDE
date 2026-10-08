"""Bounded two-hidden-layer causal-mechanism experiments; no theorem claims.

Canonical mean-square flow, normalized directions, exactly zero readout.
Outputs are generated evidence; all source edits use apply_patch.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import resource
import time
from pathlib import Path

import numpy as np
from numpy.polynomial.hermite import hermgauss


V = np.array([[1., 0., 2 / np.sqrt(5)], [0., 1., 1 / np.sqrt(5)]])


def initialize(n, seed):
    rng = np.random.default_rng(seed)
    return (rng.normal(size=(n, 2)), rng.normal(size=(n, n)) / np.sqrt(n),
            np.zeros(n))


def fields(state, frozen=None):
    a, wmat, w = state
    z1 = a @ V
    if frozen is None:
        h1 = np.tanh(z1)
        g1 = 1 - h1 * h1
    else:
        z10, h10, g1, z20, h20, g2 = frozen
        h1 = h10 + g1 * (z1 - z10)
    z2 = wmat @ h1
    if frozen is None:
        h2 = np.tanh(z2)
        g2 = 1 - h2 * h2
    else:
        h2 = h20 + g2 * (z2 - z20)
    d2 = w[:, None] * g2
    b1 = wmat.T @ d2
    d1 = g1 * b1
    return dict(z1=z1, h1=h1, g1=g1, z2=z2, h2=h2, g2=g2,
                d2=d2, b1=b1, d1=d1, f=w @ h2 / len(w))


def rhs(state, labels, mode="full", frozen=None):
    p = fields(state, frozen)
    c = labels - p['f'][:2]
    da = (p['d1'][:, :2] * c) @ V[:, :2].T
    dwmat = ((p['d2'][:, :2] * c) @ p['h1'][:, :2].T) / len(state[2])
    dw = p['h2'][:, :2] @ c
    if mode == 'frozen_middle':
        dwmat.fill(0)
    if mode == 'frozen_features':
        da.fill(0)
        dwmat.fill(0)
    return da, dwmat, dw


def add(state, velocity, scale):
    return tuple(x + scale * dx for x, dx in zip(state, velocity))


def step(state, labels, dt, method, mode, frozen):
    k1 = rhs(state, labels, mode, frozen)
    if method == 'euler':
        return add(state, k1, dt)
    k2 = rhs(add(state, k1, dt / 2), labels, mode, frozen)
    k3 = rhs(add(state, k2, dt / 2), labels, mode, frozen)
    k4 = rhs(add(state, k3, dt), labels, mode, frozen)
    return tuple(x + dt / 6 * (v1 + 2*v2 + 2*v3 + v4)
                 for x, v1, v2, v3, v4 in zip(state, k1, k2, k3, k4))


def observe(state, initial, labels, mode, frozen):
    p = fields(state, frozen)
    p0 = fields(initial)
    n = len(state[2])
    c1, c2 = (p['h1'].T @ p['h1'] / n, p['h2'].T @ p['h2'] / n)
    d1, d2 = (p['d1'].T @ p['d1'] / n, p['d2'].T @ p['d2'] / n)
    kb = np.array([c2, c1 * d2, (V.T @ V) * d1])
    if mode == 'frozen_middle':
        kb[1] = 0
    if mode == 'frozen_features':
        kb[1:] = 0
    c = labels - p['f'][:2]
    binit = initial[1].T @ p['d2']
    blearned = p['b1'] - binit
    zinit = initial[1] @ p['h1']
    zlearned = p['z2'] - zinit
    # Gate quartiles fixed at initialization: compare paired movement, not
    # an adaptively selected set of neurons.
    gate_bins = []
    cuts = np.quantile(p0['g1'][:, 0], [0, .25, .5, .75, 1])
    for b in range(4):
        mask = ((p0['g1'][:, 0] >= cuts[b]) &
                (p0['g1'][:, 0] <= cuts[b+1] if b == 3 else
                 p0['g1'][:, 0] < cuts[b+1]))
        gate_bins.append(np.mean((p['h1'][mask, 0] - p0['h1'][mask, 0])**2))
    return dict(f=p['f'], c1=c1, c2=c2, kernel_blocks=kb,
                loss=np.mean(c*c),
                loss_derivative=-float(c @ kb[:, :2, :2].sum(0) @ c),
                motion1=np.mean((p['h1']-p0['h1'])**2, axis=0),
                motion2=np.mean((p['h2']-p0['h2'])**2, axis=0),
                backward_init_rms=np.sqrt(np.mean(binit*binit, axis=0)),
                backward_learned_rms=np.sqrt(np.mean(blearned*blearned, axis=0)),
                forward_learned_rms=np.sqrt(np.mean(zlearned*zlearned, axis=0)),
                gate_motion=np.array(gate_bins),
                gate_change=np.mean((p['g1']-p0['g1'])**2, axis=0))


def simulate(n=512, seed=101, amplitude=.15, sign=-1, horizon=24., dt=.1,
             method='rk4', mode='full', observe_every=1):
    initial = initialize(n, seed)
    state = tuple(x.copy() for x in initial)
    labels = amplitude * np.array([1., float(sign)])
    frozen = None
    if mode == 'affine_gates':
        p0 = fields(initial)
        frozen = tuple(p0[k] for k in ('z1', 'h1', 'g1', 'z2', 'h2', 'g2'))
    count = int(round(horizon / dt))
    assert abs(count * dt - horizon) < 1e-10
    records, times = [], []
    for k in range(count + 1):
        if k % observe_every == 0 or k == count:
            records.append(observe(state, initial, labels, mode, frozen))
            times.append(k * dt)
        if k < count:
            state = step(state, labels, dt, method, mode, frozen)
            if not all(np.isfinite(x).all() for x in state):
                raise FloatingPointError(f'nonfinite state at step {k}')
    arrays = {key: np.array([r[key] for r in records]) for key in records[0]}
    arrays['time'] = np.array(times)
    return arrays


def quadrature_constants(order=100):
    x, weights = hermgauss(order)
    x, weights = np.sqrt(2)*x, weights / np.sqrt(np.pi)
    h, g = np.tanh(x), 1-np.tanh(x)**2
    sigma2, qx = weights @ (h*h), weights @ (g*g)
    z = np.sqrt(sigma2) * x
    hh, gg = np.tanh(z), 1-np.tanh(z)**2
    nu, alpha, beta = weights @ (hh*hh), weights @ gg, weights @ (gg*gg)
    b1 = sigma2 * qx * alpha**2
    b2middle = sigma2 * nu * beta
    b2 = (sigma2+qx)*nu*beta + sigma2*qx*alpha**4
    return dict(sigma2=float(sigma2), qx=float(qx), nu=float(nu),
                alpha=float(alpha), beta=float(beta), b1=float(b1),
                b2=float(b2), b2middle=float(b2middle))


def unit_checks():
    # Independent maintained finite-network API; zero the finite readout
    # explicitly (its default initializer is not zero-readout).
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'code'))
    from pde import Parameters, flow_velocity, kernel, TANH
    state = initialize(13, 91)
    state = (state[0], state[1], np.linspace(-.2, .2, 13))
    y = np.array([.15, -.15])
    official = flow_velocity(Parameters(state[:2], state[2]),
                             np.sqrt(2)*V[:, :2], y, activation=TANH)
    own = rhs(state, y)
    errors = [np.max(np.abs(a-b)) for a,b in
              zip(own, (*official.weights, official.readout))]
    obs = observe(state, initialize(13, 91), y, 'full', None)
    errors.append(np.max(np.abs(obs['kernel_blocks'].sum(0) -
                  kernel(Parameters(state[:2], state[2]), np.sqrt(2)*V,
                         activation=TANH))))
    assert max(errors) < 1e-12, errors
    # Exact Euler memory reconstruction: independently accumulate learned
    # rank-one writes and evaluate both orientations at each later state.
    state = initialize(17, 92)
    initial = tuple(x.copy() for x in state)
    history = []
    memory_error = 0.
    dt = .03
    for _ in range(12):
        p = fields(state)
        c = y-p['f'][:2]
        forward = initial[1] @ p['h1']
        backward = initial[1].T @ p['d2']
        for ch, dh, hh in history:
            forward += dt * (dh*ch) @ (hh.T @ p['h1'] / 17)
            backward += dt * hh @ (ch[:,None] * (dh.T @ p['d2'] / 17))
        memory_error = max(memory_error, np.max(abs(forward-p['z2'])),
                           np.max(abs(backward-p['b1'])))
        history.append((c.copy(),p['d2'][:,:2].copy(),p['h1'][:,:2].copy()))
        state = step(state,y,dt,'euler','full',None)
    assert memory_error < 1e-12, memory_error
    return {'canonical_rhs_kernel_max_error':float(max(errors)),
            'two_sided_memory_max_error':float(memory_error),
            'quadrature_100':quadrature_constants(100),
            'quadrature_160':quadrature_constants(160)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    parser.add_argument('--width', type=int, default=512)
    parser.add_argument('--seed', type=int, default=101)
    parser.add_argument('--amplitude', type=float, default=.15)
    parser.add_argument('--sign', type=int, default=-1, choices=(-1,1))
    parser.add_argument('--horizon', type=float, default=24.)
    parser.add_argument('--dt', type=float, default=.1)
    parser.add_argument('--method', choices=('rk4','euler'), default='rk4')
    parser.add_argument('--mode', choices=('full','frozen_middle','frozen_features','affine_gates'), default='full')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        print(json.dumps(unit_checks(), indent=2))
        return
    if args.output is None:
        parser.error('--output is required except for --self-test')
    args.output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    arrays = simulate(args.width,args.seed,args.amplitude,args.sign,args.horizon,
                      args.dt,args.method,args.mode)
    record = vars(args).copy()
    record['output'] = str(args.output)
    record.update(wall_seconds=time.perf_counter()-started,
                  peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  numpy=np.__version__, quadrature=quadrature_constants())
    np.savez_compressed(args.output/'trajectory.npz', **arrays)
    (args.output/'record.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(dict(run=str(args.output), seconds=record['wall_seconds'],
                         final_loss=float(arrays['loss'][-1]),
                         final_f=arrays['f'][-1].tolist(),
                         delta_c1=float(arrays['c1'][-1,0,1]-arrays['c1'][0,0,1]),
                         delta_c2=float(arrays['c2'][-1,0,1]-arrays['c2'][0,0,1]))))


if __name__ == '__main__':
    main()
