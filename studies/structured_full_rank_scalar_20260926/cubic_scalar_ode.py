"""Scalar residual-response ODE and its finite arbitrary-query decoder.

Initialization may inspect a finite initialized network. The returned model
retains only scalar contraction tensors; its RHS never accesses neuron fields,
weights, quadrature nodes, target trajectories, or a test grid. No training on
import. Conventions match KERNEL_SCALAR_ROUTE_20260930.md.
"""
from __future__ import annotations

from dataclasses import dataclass
import time

import numpy as np
from scipy.integrate import RK45
from scipy.linalg import cho_solve
from scipy.optimize import brentq


def decoder_tensor(S):
    """C[q,a,b,c] combines all cubic query contributions."""
    return (S.transpose(1, 0, 2, 3) + S
            + S.transpose(0, 2, 1, 3) + S.transpose(0, 2, 3, 1))


def _initial_fields(w, W, inputs):
    first = np.tanh(np.asarray(inputs) @ w.T)
    second = np.tanh(first @ W.T)
    return first, second, 1-first*first, 1-second*second


def _initial_responses(w, W, inputs):
    first, second, first_gate, second_gate = _initial_fields(w, W, inputs)
    m, n = second.shape
    gamma = second_gate[:, None, :] * second[None, :, :]
    beta = ((gamma.reshape(m*m, n) @ W).reshape(m, m, n)
            * first_gate[:, None, :])
    return first, second, first_gate, second_gate, gamma, beta


@dataclass
class QueryCoefficients:
    cross_gram: np.ndarray
    cubic: np.ndarray

    @property
    def nbytes(self):
        return self.cross_gram.nbytes + self.cubic.nbytes


@dataclass
class ScalarModel:
    labels: np.ndarray
    initial_gram: np.ndarray
    response_gram: np.ndarray

    def __post_init__(self):
        self.labels = np.asarray(self.labels, dtype=float).copy()
        self.initial_gram = np.asarray(self.initial_gram, dtype=float).copy()
        self.response_gram = np.asarray(self.response_gram, dtype=float).copy()
        self.m = len(self.labels)
        m = self.m
        if self.initial_gram.shape != (m, m) or self.response_gram.shape != (m, m, m, m):
            raise ValueError('Coefficient dimensions do not match labels')
        self.eigenvalues = np.linalg.eigvalsh(self.initial_gram)
        self.condition = float(self.eigenvalues[-1]/self.eigenvalues[0])
        if self.eigenvalues[0] <= 0 or self.condition > 1e12:
            raise ValueError(f'Initial Gram fails conditioning gate: {self.eigenvalues}')
        self.cholesky = np.linalg.cholesky(self.initial_gram)
        self.triangle = np.triu_indices(m, 1)
        self.area_count = len(self.triangle[0])
        self.alpha = 2/m
        self.training_decoder = decoder_tensor(self.response_gram)
        self.slices = (slice(0, m), slice(m, 2*m),
                       slice(2*m, 2*m+self.area_count),
                       slice(2*m+self.area_count, 2*m+self.area_count+m**3))
        self.size = 2*m+self.area_count+m**3

    @property
    def training_size(self):
        return 2*self.m+self.area_count

    @property
    def coefficient_nbytes(self):
        return sum(a.nbytes for a in (self.labels, self.initial_gram,
                   self.response_gram, self.cholesky, self.training_decoder))

    def initial_state(self):
        state = np.zeros(self.size)
        state[self.slices[0]] = -self.labels
        return state

    def unpack(self, state):
        residual, z, area = [state[s] for s in self.slices[:3]]
        J = .5*np.outer(z, z)
        J[self.triangle] += area
        J[self.triangle[::-1]] -= area
        P = state[self.slices[3]].reshape(self.m, self.m, self.m)
        return residual, z, J, P

    def solve_gram(self, rhs):
        return cho_solve((self.cholesky, True), rhs, check_finite=False)

    def kernel(self, z, J):
        m, alpha = self.m, self.alpha
        M = (alpha**2 * (self.response_gram.reshape(m*m, m*m)
                         @ J.ravel()).reshape(m, m).T)
        N = alpha**2*np.einsum('qdab,d,b->qa', self.response_gram, z, z)
        transformed = self.cholesky.T @ (np.eye(m)+self.solve_gram(M))
        completed = transformed.T@transformed+N
        return completed, M, N

    def rhs(self, at, state):
        residual, z, J, _ = self.unpack(state)
        kernel, _, _ = self.kernel(z, J)
        result = np.empty_like(state)
        result[self.slices[0]] = -self.alpha*(kernel@residual)
        result[self.slices[1]] = residual
        result[self.slices[2]] = .5*(residual[self.triangle[0]]*z[self.triangle[1]]
                                    - z[self.triangle[0]]*residual[self.triangle[1]])
        result[self.slices[3]] = (residual[:, None, None]*J[None, :, :]).ravel()
        return result

    def cubic_prediction(self, state, coefficients=None):
        _, z, _, P = self.unpack(state)
        gram, cubic = ((self.initial_gram, self.training_decoder)
                       if coefficients is None else
                       (coefficients.cross_gram, coefficients.cubic))
        return -self.alpha*(gram@z+self.alpha**2*np.einsum('qabc,abc->q', cubic, P))

    def predict(self, state, coefficients):
        residual = state[self.slices[0]]
        discrepancy = self.labels+residual-self.cubic_prediction(state)
        return (self.cubic_prediction(state, coefficients)
                + coefficients.cross_gram@self.solve_gram(discrepancy))


def initialize(w, W, inputs, labels):
    """Form initial scalar contractions; returned object retains no weights."""
    inputs = np.asarray(inputs)
    first, second, _, _, gamma, beta = _initial_responses(w, W, inputs)
    m, n = second.shape
    S = ((beta.reshape(m*m, n)@beta.reshape(m*m, n).T/n).reshape(m, m, m, m)
         * (inputs@inputs.T)[:, None, :, None]
         + (gamma.reshape(m*m, n)@gamma.reshape(m*m, n).T/n).reshape(m, m, m, m)
         * (first@first.T/n)[:, None, :, None])
    return ScalarModel(labels, second@second.T/n, S)


def query_coefficients(w, W, inputs, queries, batch_size=16):
    """One-time response coefficients with exactly one query index.

    The temporary width-sized arrays are discarded before ODE evolution.
    Queries are passive coefficient evaluations, never training examples.
    """
    inputs, queries = np.asarray(inputs), np.asarray(queries)
    first, second, first_gate, second_gate, gamma, beta = _initial_responses(w, W, inputs)
    m, n = second.shape
    count = len(queries)
    cross_gram = np.empty((count, m))
    cubic = np.empty((count, m, m, m))
    dot = inputs@inputs.T
    first_gram = first@first.T/n
    beta_flat, gamma_flat = beta.reshape(m*m, n), gamma.reshape(m*m, n)
    for start in range(0, count, batch_size):
        stop = min(count, start+batch_size)
        points = queries[start:stop]
        p, h, q, d = _initial_fields(w, W, points)
        length = len(points)
        cross_gram[start:stop] = h@second.T/n
        gamma_A = second_gate[None, :, :]*h[:, None, :]
        beta_A = ((gamma_A.reshape(length*m, n)@W).reshape(length, m, n)
                  * first_gate[None, :, :])
        A = ((beta_A.reshape(length*m, n)@beta_flat.T/n).reshape(length, m, m, m)
             * dot[None, :, :, None]
             + (gamma_A.reshape(length*m, n)@gamma_flat.T/n).reshape(length, m, m, m)
             * first_gram[None, :, :, None])
        gamma_B = d[:, None, :]*second[None, :, :]
        beta_B = ((gamma_B.reshape(length*m, n)@W).reshape(length, m, n)
                  * q[:, None, :])
        B = ((beta_B.reshape(length*m, n)@beta_flat.T/n).reshape(length, m, m, m)
             * (points@inputs.T)[:, None, :, None]
             + (gamma_B.reshape(length*m, n)@gamma_flat.T/n).reshape(length, m, m, m)
             * (p@first.T/n)[:, None, :, None])
        cubic[start:stop] = A+B+B.transpose(0, 2, 1, 3)+B.transpose(0, 2, 3, 1)
    return QueryCoefficients(cross_gram, cubic)


class _Deadline(Exception):
    pass


class _ScalarRK45(RK45):
    def __init__(self, *args, block_slices, **kwargs):
        self.block_slices = [sl for sl in block_slices if sl.stop > sl.start]
        super().__init__(*args, **kwargs)

    def _estimate_error_norm(self, stages, step, scale):
        scaled = self._estimate_error(stages, step)/scale
        return max(float(np.linalg.norm(scaled[sl])/np.sqrt(len(scaled[sl])))
                   for sl in self.block_slices)


def integrate(model, *, target=0.001, rtol=1e-8, atol=1e-10,
              time_cap=3000., deadline_seconds=10., max_step=10.):
    """Return last accepted scalar state, including honest partial outcomes."""
    started = time.monotonic()
    state = model.initial_state()
    mse = float(np.mean(model.labels**2))
    at, steps, evaluations = 0., 0, 0
    history = [(at, mse)]
    reason = 'initial_target' if mse <= target else 'time_cap'
    maximum_rise = 0.
    bracket = None

    def function(t, values):
        nonlocal evaluations
        if time.monotonic()-started >= deadline_seconds:
            raise _Deadline()
        evaluations += 1
        return model.rhs(t, values)

    if mse > target:
        try:
            solver = _ScalarRK45(function, 0., state, time_cap, rtol=rtol,
                atol=atol, max_step=max_step, first_step=min(.01, time_cap),
                block_slices=model.slices)
            while solver.status == 'running':
                previous_time, previous_mse = at, mse
                solver.step()
                if solver.status == 'failed':
                    reason = 'solver_failed'
                    break
                candidate = solver.y
                next_mse = float(np.mean(candidate[:model.m]**2))
                if not np.isfinite(next_mse) or not np.all(np.isfinite(candidate)):
                    reason = 'nonfinite'
                    break
                maximum_rise = max(maximum_rise, next_mse-previous_mse)
                at, state, mse = float(solver.t), candidate.copy(), next_mse
                steps += 1
                if mse <= target:
                    bracket = (previous_time, at)
                    interpolant = solver.dense_output()
                    at = brentq(lambda t: np.mean(interpolant(t)[:model.m]**2)-target,
                                previous_time, at, xtol=1e-12,
                                rtol=8*np.finfo(float).eps)
                    state = interpolant(at)
                    mse = float(np.mean(state[:model.m]**2))
                    reason = 'target'
                    history.append((at, mse))
                    break
                history.append((at, mse))
        except _Deadline:
            reason = 'wall_limit'
    return state, dict(train_mse=mse, physical_time=at, stop_reason=reason,
        fitted=mse <= target*(1+1e-7), steps=steps, nfev=evaluations,
        training_seconds=time.monotonic()-started, max_loss_rise=maximum_rise,
        target_bracket=bracket, history=np.asarray(history),
        solver=dict(method='RK45', rtol=rtol, atol=atol,
            error_norm='max scaled RMS over residual,integral,area,third-integral',
            time_cap=time_cap, max_step=max_step, target_mse=target))


def frozen_kernel(model, coefficients, *, target=0.001, time_cap=3000.):
    """Exact constant-initial-kernel control, with its own MSE crossing."""
    values, vectors = np.linalg.eigh(model.initial_gram)
    projected_labels = vectors.T@model.labels

    def residual(t):
        return -vectors@(np.exp(-model.alpha*values*t)*projected_labels)

    def loss(t):
        return float(np.mean(residual(t)**2))

    if loss(0.) <= target:
        at = 0.
    elif loss(time_cap) > target:
        at = time_cap
    else:
        at = brentq(lambda t: loss(t)-target, 0., time_cap, xtol=1e-12)
    r = residual(at)
    prediction = coefficients.cross_gram@model.solve_gram(model.labels+r)
    return prediction, dict(train_mse=loss(at), physical_time=at,
                            fitted=loss(at) <= target*(1+1e-7))
