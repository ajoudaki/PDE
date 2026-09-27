"""Weighted moving-characteristic reference for the scalar k=1, H=1 closure.

This is a reference quadrature, not an Eulerian histogram.  The independent
initial variables are half-normal g and full Gaussian w_x,w_y.  The even-order
Gaussian tensor rule has order**3/2 atoms; no source neuron width is involved.
The readout c and memory A start at zero, b=tanh(w @ u.T), and L=1.

All contractions use the current fields and fixed probability weights.  The
normalized memory b=B/L gives z=g*h-(2/m)*A E[b*h], so no extra L belongs in
the middle interaction.  No experiment runs at import time.
"""

import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'

from dataclasses import dataclass
from numbers import Integral
import time

import numpy as np
from scipy.optimize import brentq

from dense_compare import _inputs, _labels
from dense_wide_integrator import _BlockRK45


@dataclass(frozen=True)
class _Layout:
    n: int
    m: int

    @property
    def slices(self):
        edges = np.cumsum((0, 2*self.n, self.n, self.n*self.m,
                           self.n*self.m, 1))
        return tuple(slice(int(a), int(b)) for a, b in zip(edges[:-1], edges[1:]))

    @property
    def size(self):
        return self.n*(3+2*self.m)+1

    def unpack(self, vector):
        w, c, A, b, L = (vector[sl] for sl in self.slices)
        return w.reshape(self.n, 2), c, A.reshape(self.n, self.m), \
            b.reshape(self.n, self.m), float(L[0])

    def pack(self, state):
        return np.concatenate((np.asarray(state['w']).ravel(), state['c'],
                               np.asarray(state['A']).ravel(),
                               np.asarray(state['b']).ravel(),
                               np.asarray(state['L']).reshape(1)))


def initial_rule(u, order=16):
    """Return initial weighted state; order=16 gives 2048, 24 gives 6912 atoms."""
    u = _inputs(u)
    if (isinstance(order, (bool, np.bool_)) or not isinstance(order, Integral)
            or order < 2 or order % 2):
        raise ValueError('order must be an even integer >= 2')
    nodes, one_weights = np.polynomial.hermite.hermgauss(int(order))
    nodes = np.sqrt(2.)*nodes
    one_weights = one_weights/np.sqrt(np.pi)
    g, wx, wy = np.meshgrid(nodes[order//2:], nodes, nodes, indexing='ij')
    wg, wwx, wwy = np.meshgrid(2*one_weights[order//2:], one_weights,
                              one_weights, indexing='ij')
    weights = np.ascontiguousarray((wg*wwx*wwy).ravel())
    # Remove only floating summation drift; preserve the Gaussian rule itself.
    weights /= weights.sum()
    w = np.ascontiguousarray(np.column_stack((wx.ravel(), wy.ravel())))
    n = len(weights)
    return {'g': np.ascontiguousarray(g.ravel()), 'weights': weights,
            'w': w, 'c': np.zeros(n), 'A': np.zeros((n, len(u))),
            'b': np.tanh(w@u.T), 'L': np.asarray(1.)}


def _forward(layout, g, weights, vector, u):
    w, c, A, b, _ = layout.unpack(vector)
    h = np.tanh(w@u.T)
    S = b.T@(weights[:, None]*h)
    z = g[:, None]*h-(2./layout.m)*(A@S)
    H = np.tanh(z)
    prediction = (weights*c)@H
    return prediction, h, H


def _rhs(layout, g, weights, vector, u, labels):
    _, c, A, b, L = layout.unpack(vector)
    prediction, h, H = _forward(layout, g, weights, vector, u)
    r = prediction-labels
    rho = float(np.sqrt(np.mean(r*r)))
    delta = c[:, None]*(1.-H*H)
    T = A.T@(weights[:, None]*delta)
    back = g[:, None]*delta-(2./layout.m)*(b@T)
    derivative = np.empty_like(vector)
    dw, dc, dA, db, _ = layout.unpack(derivative)
    dw[:] = -(2./layout.m)*((r*(1.-h*h)*back)@u)
    dc[:] = -(2./layout.m)*(H@r)
    dA[:] = delta*r
    db[:] = (rho/L)*(h-b)
    derivative[-1] = rho
    return derivative


def weighted_rhs(state, u, labels):
    """Canonical pointwise velocity as a dict; fixed g and weights are omitted."""
    u = _inputs(u)
    labels = _labels(labels, len(u))
    layout = _Layout(len(state['weights']), len(u))
    derivative = _rhs(layout, state['g'], state['weights'], layout.pack(state),
                      u, labels)
    w, c, A, b, L = layout.unpack(derivative)
    return {'w': w, 'c': c, 'A': A, 'b': b, 'L': np.asarray(L)}


def predict(savedstate, angles, batch=128):
    """Evaluate the same trained law at unseen circle angles in bounded batches."""
    angles = np.asarray(angles, dtype=float)
    if angles.ndim != 1 or not np.all(np.isfinite(angles)):
        raise ValueError('angles must be a finite one-dimensional array')
    if (isinstance(batch, (bool, np.bool_)) or not isinstance(batch, Integral)
            or batch < 1):
        raise ValueError('batch must be a positive integer')
    layout = _Layout(len(savedstate['weights']), savedstate['A'].shape[1])
    vector = layout.pack(savedstate)
    result = np.empty(len(angles))
    for j in range(0, len(angles), int(batch)):
        selected = angles[j:j+batch]
        u = np.column_stack((np.cos(selected), np.sin(selected)))
        result[j:j+batch] = _forward(layout, savedstate['g'],
                                     savedstate['weights'], vector, u)[0]
    return result


class _DeadlineReached(Exception):
    pass


def run_reference(u, labels, order=16, target=.01, deadline=50., timecap=100.):
    """Integrate until the refined target crossing, deadline, or physical cap.

    deadline is a relative wall-clock budget in seconds.  The returned state
    is always the last finite accepted checkpoint (or the refined target
    state), even when a deadline interrupts an RK stage.  info contains only
    JSON-compatible values.  Solver tolerances are rtol=1e-7, atol=1e-9,
    max_step=.25 with a maximum-of-state-blocks scaled RMS error norm.
    """
    started = time.monotonic()
    u = _inputs(u)
    labels = _labels(labels, len(u))
    for name, value in (('target', target), ('deadline', deadline),
                        ('timecap', timecap)):
        if not np.isfinite(value) or value < 0:
            raise ValueError(f'{name} must be finite and nonnegative')
    target, deadline, timecap = float(target), float(deadline), float(timecap)
    state = initial_rule(u, order)
    g, weights = state['g'], state['weights']
    layout = _Layout(len(weights), len(u))
    values = layout.pack(state)

    def mse_at(vector):
        residual = _forward(layout, g, weights, vector, u)[0]-labels
        return float(np.mean(residual*residual))

    def function(at, vector):
        if time.monotonic()-started >= deadline:
            raise _DeadlineReached()
        return _rhs(layout, g, weights, vector, u, labels)

    t, mse, steps, max_rise = 0., mse_at(values), 0, 0.
    history = [[t, mse, float(values[-1])]]
    solver = None
    bracket = None
    reason = 'time_cap'
    if mse <= target:
        reason, bracket = 'target', [0., 0.]
    elif time.monotonic()-started >= deadline:
        reason = 'deadline'
    elif timecap > 0:
        try:
            solver = _BlockRK45(function, 0., values, timecap, rtol=1e-7,
                                atol=1e-9, first_step=min(.005, timecap),
                                max_step=.25, block_slices=layout.slices)
            while solver.status == 'running':
                old_t, old_mse = t, mse
                solver.step()
                if solver.status == 'failed':
                    reason = 'solver_failed'
                    break
                trial_mse = mse_at(solver.y)
                if not np.isfinite(trial_mse) or not np.all(np.isfinite(solver.y)):
                    reason = 'nonfinite'
                    break
                max_rise = max(max_rise, trial_mse-old_mse)
                if trial_mse <= target:
                    bracket = [old_t, float(solver.t)]
                    interpolation = solver.dense_output()
                    tolerance = max(1e-12, 8*np.finfo(float).eps*max(1., solver.t))
                    root = brentq(lambda at: mse_at(interpolation(at))-target,
                                  *bracket, xtol=tolerance,
                                  rtol=8*np.finfo(float).eps)
                    candidate = interpolation(root)
                    candidate_mse = mse_at(candidate)
                    for _ in range(4):
                        if candidate_mse <= target:
                            break
                        root = min(solver.t,
                                   root+max(tolerance, 1e-9*(solver.t-old_t)))
                        candidate = interpolation(root)
                        candidate_mse = mse_at(candidate)
                    if (not np.isfinite(candidate_mse) or candidate_mse > target
                            or abs(candidate_mse-target) > max(1e-12, 1e-6*target)):
                        reason = 'event_refinement_failed'
                        break
                    values, t, mse = candidate.copy(), float(root), candidate_mse
                    reason = 'target'
                else:
                    values, t, mse = solver.y.copy(), float(solver.t), trial_mse
                steps += 1
                history.append([t, mse, float(values[-1])])
                if reason == 'target':
                    break
        except _DeadlineReached:
            reason = 'deadline'

    w, c, A, b, L = layout.unpack(values)
    state.update(w=w.copy(), c=c.copy(), A=A.copy(), b=b.copy(), L=np.asarray(L))
    info = {'kind': 'weighted_characteristic_reference', 'gaussian_seed_order': int(order),
            'characteristics': layout.n, 'dynamic_scalars': layout.size,
            'stop_reason': reason, 'fitted': reason == 'target' and mse <= target,
            'train_mse': mse, 'physical_time': t, 'target_mse': target,
            'target_bracket': bracket, 'nsteps': steps,
            'nfev': int(solver.nfev) if solver is not None else 0,
            'max_loss_rise': max_rise, 'history': history,
            'training_seconds': time.monotonic()-started,
            'rtol': 1e-7, 'atol': 1e-9, 'max_step': .25,
            'first_step': min(.005, timecap), 'time_cap': timecap,
            'deadline_seconds': deadline,
            'error_norm': 'maximum of per-block scaled RMS'}
    return state, info
