"""Checked extension of the frozen derivative dictionary; P45_PROTOCOL.md.

Symbolic binary homogeneous polynomials are coefficient tables, never labels
from a task. Column j of degree d multiplies y1**(d-j)*y2**j. Every coefficient
is an initialized field. Population contractions use deterministic Gaussian
moments; operator calls use the same initialized matrix and its transpose.
"""
from functools import lru_cache
import numpy as np
import torch

import new_dictionary as previous
from pde.observable_torch_p1 import ClosureEngine


def mul(a, b):
    out = a.new_zeros((a.shape[0], a.shape[1] + b.shape[1] - 1))
    for i in range(a.shape[1]):
        for j in range(b.shape[1]):
            out[:, i+j] += a[:, i] * b[:, j]
    return out


def y_times(a, axis):
    out = a.new_zeros((a.shape[0], a.shape[1]+1))
    out[:, axis:axis+a.shape[1]] = a
    return out


@lru_cache(maxsize=1)
def population_moments():
    records = []
    # v stays exactly the previous builder's 256-node value at both rules.
    v = previous._variance_rules()[1]
    for order in (128, 256):
        z, weights = np.polynomial.hermite.hermgauss(order)
        weights = weights / np.sqrt(np.pi)
        h = np.tanh(np.sqrt(2.)*z)
        H = np.tanh(np.sqrt(2.*v)*z)
        p, d = 1-h*h, 1-H*H
        tau = float(weights @ (H*H))
        d1, d2 = float(weights @ d), float(weights @ (d*d))
        H2d = float(weights @ (H*H*d))
        H2d2 = float(weights @ (H*H*d*d))
        lam_diag = float(weights @ (h*h*p*p)) * (d2-2*H2d)
        lam_off = v * float(weights @ (p*p)) * d1*d1
        lam = [[lam_diag, lam_off], [lam_off, lam_diag]]
        g = [[[H2d2 if a == b == k else tau*d2 if a == b else H2d*d1
               for k in range(2)] for b in range(2)] for a in range(2)]
        records.append(dict(order=order, v=v, tau=tau, mean_d=d1,
                            mean_d2=d2, mean_H2d=H2d, mean_H2d2=H2d2,
                            lam=lam, g=g))
    left, right = records
    discrepancy = max(abs(left[k]-right[k]) for k in
                      ('tau', 'mean_d', 'mean_d2', 'mean_H2d', 'mean_H2d2'))
    discrepancy = max(discrepancy, float(np.max(np.abs(
        np.array(left['lam'])-np.array(right['lam'])))))
    discrepancy = max(discrepancy, float(np.max(np.abs(
        np.array(left['g'])-np.array(right['g'])))))
    if discrepancy > 1e-9:
        raise ValueError('population moment quadrature gate failed')
    return dict(working=right, coarse=left, maximum_discrepancy=discrepancy,
                discrepancy_is_error_bound=False,
                method='one-dimensional Gauss-Hermite 128/256, working 256')


@torch.no_grad()
def raw_features(initial, p):
    if isinstance(p, bool) or not isinstance(p, int) or p not in (4, 5):
        raise ValueError('extension order must be 4 or 5')
    lower, upper, metadata = previous.raw_features(initial, 3)
    metadata.update(p=p, maximum_weight_taylor_power=p+1,
                    dictionary='derivative_collected_increment_extension',
                    inherited_builder='new_dictionary.py',
                    p4_span_equals_p3=True,
                    population_moments=population_moments())
    if p == 5:
        n = len(initial.w)
        h, L = lower[:, :2], lower[:, 2:].reshape(n, 2, 2)
        H = torch.tanh(initial.M @ h)
        lower_gate = 1-h.square()
        lower_second = -2*h*lower_gate
        d = 1-H.square()
        e = -2*H*d
        third = (6*H.square()-2)*d
        U = upper[:, :4].reshape(n, 2, 2)
        Q = (initial.M.T @ U.flatten(1)).reshape(n, 2, 2)
        F = previous._variance_rules()[1]*U + (initial.M @ L.flatten(1)).reshape(n, 2, 2)
        S = H
        R = [y_times(F[:, a, :], a)/2 for a in range(2)]
        q = [y_times(lower_gate[:, a:a+1]*Q[:, a, :], a)/2 for a in range(2)]
        J = sum(y_times(d[:, b:b+1]*R[b], b) for b in range(2))
        K3 = [d[:, a:a+1]*J/3 + e[:, a:a+1]*mul(S, R[a]) for a in range(2)]
        # Check that collection preserves the exact old upper column convention.
        collection_error = max(float((6*K3[a]-upper[:, 4+4*a:8+4*a]).abs().max())
                               for a in range(2))
        moments = population_moments()['working']
        T, E = [], []
        for a in range(2):
            B2adj = initial.w.new_zeros((n, 4))
            for b in range(2):
                gram = initial.w.new_zeros((n, 3))
                gram[:, 0], gram[:, 2] = moments['g'][a][b]
                B2adj += y_times(h[:, b:b+1]*gram, b)/2
            value = (y_times(lower_gate[:, a:a+1].square()*(initial.M.T @ K3[a]), a)/4
                     + y_times(lower_gate[:, a:a+1].square()*B2adj, a)/4
                     + lower_second[:, a:a+1]*mul(q[a], q[a]))
            T.append(value)
        for a in range(2):
            contraction = initial.w.new_zeros((n, 4))
            for b in range(2):
                contraction += moments['lam'][a][b]*y_times(y_times(U[:, b, :], b), b)
            E.append(initial.M @ T[a]
                     + previous._variance_rules()[1]*y_times(K3[a], a)/4
                     + 3*y_times(contraction, a)/8)
        K = sum(y_times(d[:, b:b+1]*E[b]+e[:, b:b+1]*mul(R[b], R[b])/2, b)
                for b in range(2))
        K5 = [d[:, a:a+1]*K/5 + e[:, a:a+1]*mul(J, R[a])/3
              + e[:, a:a+1]*mul(S, E[a])
              + third[:, a:a+1]*mul(S, mul(R[a], R[a]))/2
              for a in range(2)]
        zero_error = max(float(T[0][:, 4].abs().max()), float(T[1][:, 0].abs().max()))
        if zero_error != 0:
            raise ValueError('symbolic polynomial divisibility failed')
        scale = max(1., float(upper.abs().max()))
        if collection_error > 1e-12*scale:
            raise ValueError('inherited coefficient collection mismatch')
        lower = torch.cat((lower, 24*T[0][:, :4], 24*T[1][:, 1:]), dim=1)
        upper = torch.cat((upper, 120*K5[0], 120*K5[1]), dim=1)
        metadata.update(
            lower_column_order=metadata['lower_column_order']+
                [f'24*T{a+1}_y1^{4-j}y2^{j}' for a in range(2) for j in range(a, a+4)],
            upper_column_order=metadata['upper_column_order']+
                [f'120*K5_{a+1}_y1^{5-j}y2^{j}' for a in range(2) for j in range(6)],
            added_lower_raw_scale=24, added_upper_raw_scale=120,
            raw_column_rescaling='inherited columns unchanged; new derivative coefficients times 4! and 5!',
            inherited_collection_absolute_error=collection_error,
            polynomial_divisibility_absolute_error=zero_error,
            scalar_contractions='population Gaussian moments, not empirical task contractions')
    if not bool(torch.isfinite(lower).all() and torch.isfinite(upper).all()):
        raise ValueError('nonfinite higher-order dictionary')
    metadata.update(K1=lower.shape[1], K2=upper.shape[1])
    return lower.contiguous(), upper.contiguous(), metadata


@torch.no_grad()
def build(initial, p, *, block_size=512, forward_mode='auto'):
    lower, upper, metadata = raw_features(initial, p)
    n, eta = len(initial.w), 1/(1024*(p+1)**2)
    b1, diag1 = previous._ridge_basis(lower, eta)
    b2, diag2 = previous._ridge_basis(upper, eta)
    M = b2.T @ (initial.M @ b1)/n
    metadata.update(eta=eta, lower=diag1, upper=diag2, width=n,
                    middle_parameter_count=b1.shape[1]*b2.shape[1],
                    retained_initial_readout=True, retained_dense_background=False,
                    normalization='raw Gram plus eta*I, inverse Cholesky transpose',
                    sign_folded=False, population_rule='finite Gaussian carrier',
                    nominal_population_nodes=n, omitted_inactive_constant_features=False)
    engine = ClosureEngine(b1, initial.w, b2, M, device=initial.w.device,
                           dtype=initial.w.dtype, block_size=block_size,
                           forward_mode=forward_mode, representation=metadata)
    return engine, engine.state(initial.w, initial.c, M), metadata
