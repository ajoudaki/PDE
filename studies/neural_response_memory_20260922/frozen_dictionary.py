"""Frozen initialization dictionaries; all training lives in compact_flow.

Derivative coefficient formulas are consolidated from new_dictionary.py,
new_dictionary_p45.py, new_dictionary_p7.py and p7_gaussian_check.py.
No fitted trajectory or task label enters a dictionary constructor.
"""
from functools import lru_cache
from types import SimpleNamespace
from pathlib import Path
import json
import math
import sys
import numpy as np
import torch

# The established polynomial-word compiler is shared, not reimplemented.
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'code'))
from pde.observable_initialization import build_dictionary

OLD_RANKS = {1: (5, 3), 3: (35, 10), 5: (128, 21), 6: (213, 28),
             7: (333, 36), 8: (499, 45), 9: (720, 55)}


def old_raw_features(initial, order):
    """Original Chebyshev/action-word dictionary, including redundant tails."""
    if order not in OLD_RANKS:
        raise ValueError('Old dictionary orders: 1,3,5,6,7,8,9')
    definition = build_dictionary(order)
    lower = initial.w.tanh()
    upper = (initial.M @ lower).tanh()
    reverse = (initial.M.T @ upper).tanh()
    cache = {}
    def word(value):
        if value not in cache:
            op = value.op
            if op == 'one': result = torch.ones_like(initial.c)
            elif op in ('g1', 'g2'): result = initial.w[:, int(op[-1])-1]
            elif op == 'action': result = (initial.M if value.population == 2 else initial.M.T) @ word(value.args[0])
            elif op in ('sin', 'cos', 'tanh'): result = getattr(torch, op)(word(value.args[0]))
            elif op == 'scale': result = float(value.scalar)*word(value.args[0])
            elif op == 'add': result = word(value.args[0])+word(value.args[1])
            elif op == 'multiply': result = word(value.args[0])*word(value.args[1])
            else: raise ValueError('Unsupported initialized word: '+op)
            cache[value] = result
        return cache[value]
    result = []
    for coordinates, exponents, tail in zip((torch.cat((lower, reverse), 1), upper),
            (definition.first_exponents, definition.second_exponents),
            (definition.first_tail, definition.second_tail)):
        terms = [torch.ones_like(coordinates), coordinates]
        for _ in range(1, order): terms.append(2*coordinates*terms[-1]-terms[-2])
        columns = []
        for powers in exponents:
            column = torch.ones_like(initial.c)
            for j, degree in enumerate(powers): column = column*terms[degree][:, j]
            columns.append(column)
        result.append(torch.stack(columns+[word(w) for w in tail], 1))
    return result


@torch.no_grad()
def frozen_bases(w, matrices, c, kind, order=1, ranks=None, seed=7319):
    """Build once in float64, then cast to the declared training precision.

    Default random ranks/draws reproduce scaling_dictionary's p<=9 protocol.
    Explicit ranks allow random baselines at arbitrary depth/input dimension.
    """
    n, depth, dtype = len(w), len(matrices)+1, w.dtype
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError('Positive integer dictionary order required')
    if isinstance(seed, bool) or not isinstance(seed, int) or not 0 <= seed <= 2**64-2-100000:
        raise ValueError('Dictionary seed and appended seeds must fit uint64')
    if kind in ('dictionary_old', 'dictionary_flow'):
        if ranks is not None: raise ValueError('Historical dictionary ranks are fixed by order')
        if depth != 2 or w.shape[1] != 2:
            raise ValueError('Historical dictionaries require depth=2 and input dimension=2')
        initial = SimpleNamespace(w=w.double(), M=matrices[0].double(), c=c.double())
        if kind == 'dictionary_old': raw = old_raw_features(initial, order)
        else:
            if order not in range(1, 8): raise ValueError('Gradient-flow dictionary orders: 1..7')
            builder = d_raw_features if order <= 3 else d45_raw_features if order <= 5 else d7_raw_features
            *raw, _ = builder(initial, order)
        bases = []
        ridge = 1/(1024*(order+1)**2)
        for values in raw:
            gram = values.T @ values/n
            # Preserve the derivative builder's explicit symmetrization.
            if kind == 'dictionary_flow': gram = (gram+gram.T)/2
            chol = torch.linalg.cholesky(gram+ridge*torch.eye(values.shape[1], dtype=values.dtype, device=w.device))
            bases.append(torch.linalg.solve_triangular(chol, values.T, upper=False).T.contiguous())
    elif kind in ('gaussian', 'orthogonal'):
        legacy = ranks is None
        if legacy:
            if depth != 2 or order not in OLD_RANKS:
                raise ValueError('Supply ranks for random baselines outside the historical two-layer orders')
            ranks = OLD_RANKS[order]
        elif isinstance(ranks, int): ranks = [ranks]*depth
        if len(ranks) != depth or any(isinstance(k, bool) or not isinstance(k, int) or k < 1 for k in ranks):
            raise ValueError('Use one positive rank per hidden layer')
        bases = []
        for i, rank in enumerate(ranks):
            if kind == 'orthogonal' and rank > n: raise ValueError('Orthogonal rank cannot exceed width')
            generator = torch.Generator(device=w.device).manual_seed(seed+i)
            raw = torch.randn((n, (128, 21)[i] if legacy else rank), generator=generator, device=w.device, dtype=torch.float64)
            if legacy and rank > raw.shape[1]:
                generator.manual_seed(seed+100000+i)
                extra = torch.randn((n, (592, 34)[i]), generator=generator, device=w.device, dtype=torch.float64)
                raw = torch.cat((raw, extra), 1)
            raw = raw[:, :rank]
            bases.append(raw/raw.square().mean(0).sqrt() if kind == 'gaussian'
                         else math.sqrt(n)*torch.linalg.qr(raw, mode='reduced')[0])
    else: raise ValueError('Unknown frozen dictionary: '+kind)
    return [b.to(dtype).contiguous() for b in bases]

SOURCE_SHA256 = {'p7_gaussian_check.py': 'b418b3fbbbeb1e7cba8e508f712eb05fecfec3eef13e70f666b12e0c1fdef3b7', 'new_dictionary.py': '69e961da6614823f9d8afa8258a097aefef13ce37faf9b2b9184182b7ef9fb87', 'new_dictionary_p45.py': 'a99981904d16700e7a8544d1e0d16b3f2ccc5ebd1803a5d28b9a5450fed033eb', 'new_dictionary_p7.py': 'f4709f9c5287f125f17a637ed4e0c88cbad7125cd84fca3a54ad830afcf52a19'}

def g_mul(a, b):
    out = np.zeros((a.shape[0], a.shape[1] + b.shape[1] - 1))
    for i in range(a.shape[1]):
        for j in range(b.shape[1]):
            out[:, i + j] += a[:, i] * b[:, j]
    return out

def g_ytimes(a, axis):
    out = np.zeros((a.shape[0], a.shape[1] + 1))
    out[:, axis:axis + a.shape[1]] = a
    return out

def g_gaussian_rule(order):
    (z, w) = np.polynomial.hermite.hermgauss(order)
    return (np.sqrt(2) * z, w / np.sqrt(np.pi))

@lru_cache(maxsize=3)
def g_population_contractions(order=256):
    """All scalars needed by the label-leading W(t) coefficient through t8.

    UK[a,b,c,j] = <U_ab,[y1^(3-j)y2^j] K3_c>.
    hT[i,a,j] = <h_i,[y1^(4-j)y2^j] T_a>.
    VV[a,b,j] = [y1^(4-j)y2^j] <V_a,V_b>.
    beta[a,j] = [y1^(3-j)y2^j] beta_a.
    """
    (fixed_z, fixed_w) = np.polynomial.hermite.hermgauss(256)
    v = float(fixed_w @ np.tanh(np.sqrt(2) * fixed_z) ** 2 / np.sqrt(np.pi))
    (z, w) = g_gaussian_rule(order)
    grid = np.array(np.meshgrid(z, z, indexing='ij')).reshape(2, -1).T
    weights = np.outer(w, w).ravel()
    n = len(weights)

    def avg(x):
        return np.einsum('n,n...->...', weights, x)
    h = np.tanh(grid)
    ell = 1 - h * h
    lower_second = -2 * h * ell
    Y = np.sqrt(v) * grid
    H = np.tanh(Y)
    d = 1 - H * H
    e = -2 * H * d
    U = (d[:, :, None] * H[:, None, :]).reshape(n, 4)
    pairs = [(a, b) for a in range(2) for b in range(2)]
    DU = np.zeros((n, 4, 2))
    for (i, (a, b)) in enumerate(pairs):
        DU[:, i, b] += d[:, a] * d[:, b]
        DU[:, i, a] += e[:, a] * H[:, b]
    A = avg(DU)
    C = avg(U[:, :, None] * U[:, None, :])
    mu = h @ A.T
    gates = np.stack([ell[:, a] ** 2 for (a, b) in pairs], 1)
    Lmean = gates * mu
    LL = avg(gates[:, :, None] * gates[:, None, :] * (C[None] + mu[:, :, None] * mu[:, None, :]))
    P = avg(Lmean[:, :, None] * h[:, None, :])
    kappa = float(w @ (1 - np.tanh(z) ** 2) ** 2)
    ximean = Y @ P.T / v
    Fmean = ximean + (v + kappa) * U
    S = H
    R = [g_ytimes(Fmean[:, 2 * a:2 * a + 2], a) / 2 for a in range(2)]
    J = sum((g_ytimes(d[:, b:b + 1] * R[b], b) for b in range(2)))
    K = [d[:, a:a + 1] * J / 3 + e[:, a:a + 1] * g_mul(S, R[a]) for a in range(2)]
    KR = np.zeros((2, 4, n, 4))
    for (i, (c, b)) in enumerate(pairs):
        Ri = [np.zeros((n, 3)), np.zeros((n, 3))]
        Ri[c][:, c + b] = 0.5
        Ji = sum((g_ytimes(d[:, a:a + 1] * Ri[a], a) for a in range(2)))
        for a in range(2):
            KR[a, i] = d[:, a:a + 1] * Ji / 3 + e[:, a:a + 1] * g_mul(S, Ri[a])
    KY = np.zeros((2, 2, n, 4))
    upper_third = (6 * H * H - 2) * d
    for j in range(2):
        Rj = [g_ytimes((v + kappa) * DU[:, 2 * a:2 * a + 2, j], a) / 2 for a in range(2)]
        Jj = sum((g_ytimes(d[:, b:b + 1] * Rj[b] + (e[:, b:b + 1] * R[b] if j == b else 0), b) for b in range(2)))
        Sj = np.zeros_like(S)
        Sj[:, j] = d[:, j]
        for a in range(2):
            KY[a, j] = (d[:, a:a + 1] * Jj + (e[:, a:a + 1] * J if a == j else 0)) / 3
            KY[a, j] += e[:, a:a + 1] * (g_mul(Sj, R[a]) + g_mul(S, Rj[a]))
            if a == j:
                KY[a, j] += upper_third[:, a:a + 1] * g_mul(S, R[a])
    UK = np.empty((2, 2, 2, 4))
    for (i, (a, b)) in enumerate(pairs):
        for c in range(2):
            UK[a, b, c] = avg(U[:, i:i + 1] * K[c])
    beta = np.array([avg(H[:, a:a + 1] * J / 3 + g_mul(S, d[:, a:a + 1] * R[a])) for a in range(2)])
    VV = np.zeros((2, 2, 5))
    hT = np.zeros((2, 2, 5))
    hV = np.zeros((2, 2, 3))
    adjoint_response_error = 0.0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for k in range(2):
                    (ia, ib) = (2 * a + c, 2 * b + k)
                    VV[a, b, a + b + c + k] += avg(gates[:, ia] * gates[:, ib] * (C[ia, ib] + mu[:, ia] * mu[:, ib])) / 4
        for i in range(2):
            for b in range(2):
                hV[i, a, a + b] += avg(h[:, i] * Lmean[:, 2 * a + b]) / 2
            f = h[:, i] * ell[:, a] ** 2
            fY = avg(f[:, None] * h)
            fxi = avg(f[:, None] * Lmean)
            conditional_cov = fxi - fY @ P.T / v
            fmean = Y @ fY / v
            fK = avg(fmean[:, None] * K[a])
            for j in range(4):
                fK += conditional_cov[j] * avg(KR[a, j])
            reverse_fK = np.zeros(4)
            for j in range(2):
                reverse_fK += fY[j] * avg(KY[a, j])
            for j in range(4):
                reverse_fK += fxi[j] * avg(KR[a, j])
            adjoint_response_error = max(adjoint_response_error, float(np.max(np.abs(reverse_fK - fK))))
            hT[i, a, a:a + 4] += fK / 4
            for b in range(2):
                lower = avg(f * h[:, b]) / 8
                for c in range(2):
                    for k in range(2):
                        hT[i, a, a + b + c + k] += lower * C[2 * b + c, 2 * a + k]
            for b in range(2):
                for c in range(2):
                    (i1, i2) = (2 * a + b, 2 * a + c)
                    value = avg(h[:, i] * lower_second[:, a] * ell[:, a] ** 2 * (C[i1, i2] + mu[:, i1] * mu[:, i2])) / 4
                    hT[i, a, 2 * a + b + c] += value
    joint = np.block([[v * np.eye(2), P.T], [P, LL]])
    return dict(order=order, v=v, tau=float(w @ np.tanh(np.sqrt(v) * z) ** 2), kappa=kappa, A=A, C=C, P=P, LL=LL, UK=UK, hT=hT, VV=VV, hV=hV, beta=beta, adjoint_response_error=adjoint_response_error, source_covariance_minimum_eigenvalue=float(np.linalg.eigvalsh(joint).min()))

@lru_cache(maxsize=1)
def d__variance_rules():
    values = []
    for order in (128, 256):
        (nodes, weights) = np.polynomial.hermite.hermgauss(order)
        values.append(float(weights @ np.tanh(np.sqrt(2.0) * nodes) ** 2 / np.sqrt(np.pi)))
    return tuple(values)

def d__quadrature_metadata():
    (coarse, fine) = d__variance_rules()
    return {'v': fine, 'v_128': coarse, 'v_256': fine, 'v_quadrature_absolute_discrepancy': abs(fine - coarse), 'v_quadrature': 'Gauss-Hermite 128/256; 256-node working value', 'v_target': 'E[tanh(G)^2], G standard normal', 'v_discrepancy_is_error_bound': False}

def d__validate_initial(initial, p):
    if isinstance(p, bool) or not isinstance(p, int) or p not in (1, 2, 3):
        raise ValueError('new dictionary level must be 1, 2, or 3')
    if initial.w.ndim != 2 or initial.w.shape[1] != 2:
        raise ValueError('initial.w must have shape (n,2)')
    n = initial.w.shape[0]
    if n < 1 or initial.M.shape != (n, n) or initial.c.shape != (n,):
        raise ValueError('inconsistent equal-width finite initial state')
    if initial.w.dtype not in (torch.float32, torch.float64):
        raise ValueError('initial state must use float32 or float64')
    for value in (initial.w, initial.c, initial.M):
        if value.dtype != initial.w.dtype or value.device != initial.w.device:
            raise ValueError('initial state dtype/device mismatch')
        if not bool(torch.isfinite(value).all()):
            raise ValueError('nonfinite initial state')

def d__initialized_fields(initial, p):
    h = torch.tanh(initial.w)
    H = torch.tanh(initial.M @ h)
    D = 1 - H.square()
    U = D[:, :, None] * H[:, None, :]
    fields = {'h': h, 'H': H, 'U': U}
    if p == 3:
        Q = (initial.M.T @ U.flatten(1)).reshape(-1, 2, 2)
        lower_gate_squared = (1 - h.square()).square()
        L = lower_gate_squared[:, :, None] * Q
        F = d__variance_rules()[1] * U + (initial.M @ L.flatten(1)).reshape(-1, 2, 2)
        fields.update(L=L, F=F)
    return fields

def d__collected_upper(H, F):
    (D, E) = (1 - H.square(), -2 * H * (1 - H.square()))

    def A(a, b, c):
        return D[:, a] * D[:, b] * F[:, b, c]

    def B(a, b, c):
        return H[:, c] * E[:, a] * F[:, a, b]
    return torch.stack((A(0, 0, 0) + 3 * B(0, 0, 0), A(0, 0, 1) + 3 * (B(0, 0, 1) + B(0, 1, 0)), A(0, 1, 0) + 3 * B(0, 1, 1), A(0, 1, 1), A(1, 0, 0), A(1, 0, 1) + 3 * B(1, 0, 0), A(1, 1, 0) + 3 * (B(1, 0, 1) + B(1, 1, 0)), A(1, 1, 1) + 3 * B(1, 1, 1)), dim=1)

@torch.no_grad()
def d_raw_features(initial, p):
    """Return (lower table, upper table, JSON-safe metadata), without ridge.

    Column order is lower h1,h2,[L11,L12,L21,L22], and upper
    U11,U12,U21,U22,[C1,...,C8]. Both first levels have identical tables.
    C1...C4 multiply y1^4,y1^3*y2,y1^2*y2^2,y1*y2^3 in the h1
    coefficient; C5...C8 multiply y1^3*y2,...,y2^4 in h2. The actual
    feedback coefficient has an additional common factor 1/6.
    """
    d__validate_initial(initial, p)
    fields = d__initialized_fields(initial, p)
    (lower, upper) = (fields['h'], fields['U'].flatten(1))
    if p == 3:
        lower = torch.cat((lower, fields['L'].flatten(1)), dim=1)
        upper = torch.cat((upper, d__collected_upper(fields['H'], fields['F'])), dim=1)
    if not bool(torch.isfinite(lower).all() and torch.isfinite(upper).all()):
        raise ValueError('nonfinite derivative dictionary')
    metadata = {'dictionary': 'derivative_collected_increment', 'p': p, 'maximum_weight_taylor_power': p + 1, 'normalized_probes': [[1.0, 0.0], [0.0, 1.0]], 'physical_probe_scale': float(np.sqrt(2.0)), 'K1': lower.shape[1], 'K2': upper.shape[1], 'lower_column_order': ['h1', 'h2'] + (['L11', 'L12', 'L21', 'L22'] if p == 3 else []), 'upper_column_order': ['U11', 'U12', 'U21', 'U22'] + ([f'C{i}' for i in range(1, 9)] if p == 3 else []), 'F_coefficient': 'v*U + W0*L', 'raw_column_rescaling': 'none', 'finite_jet_matching_claim': False, **d__quadrature_metadata()}
    return (lower.contiguous(), upper.contiguous(), metadata)

def d__ridge_basis(raw, eta):
    (n, k) = raw.shape
    gram = raw.T @ raw / n
    gram = (gram + gram.T) / 2
    identity = torch.eye(k, dtype=raw.dtype, device=raw.device)
    regularized = gram + eta * identity
    chol = torch.linalg.cholesky(regularized)
    basis = torch.linalg.solve_triangular(chol, raw.T, upper=False).T.contiguous()
    effective_gram = basis.T @ basis / n
    effective_gram = (effective_gram + effective_gram.T) / 2
    raw_eigs = torch.linalg.eigvalsh(gram)
    effective_eigs = torch.linalg.eigvalsh(effective_gram)
    eps = torch.finfo(raw.dtype).eps
    raw_threshold = max(n, k) * eps * max(float(raw_eigs[-1]), 0.0)
    effective_threshold = max(n, k) * eps * max(float(effective_eigs[-1]), 0.0)
    chol_inverse = torch.linalg.solve_triangular(chol, identity, upper=False)
    ridge_identity = effective_gram + eta * (chol_inverse @ chol_inverse.T)
    raw_norm = float(torch.linalg.norm(raw))
    triangular_error = float(torch.linalg.norm(basis @ chol.T - raw))
    triangular_residual = triangular_error / raw_norm if raw_norm else triangular_error
    diagnostics = {'raw_eigenvalues': raw_eigs.cpu().tolist(), 'effective_eigenvalues': effective_eigs.cpu().tolist(), 'raw_numerical_rank': int((raw_eigs > raw_threshold).sum()), 'effective_numerical_rank': int((effective_eigs > effective_threshold).sum()), 'raw_rank_threshold': raw_threshold, 'effective_rank_threshold': effective_threshold, 'rank_threshold_rule': 'max(n,K)*dtype_epsilon*largest_Gram_eigenvalue', 'filter_directions_above_half': int((effective_eigs > 0.5).sum()), 'effective_degrees_of_freedom': float(effective_eigs.sum()), 'ridge_condition': float((raw_eigs[-1] + eta) / (raw_eigs[0] + eta)), 'cholesky_relative_residual': float(torch.linalg.norm(chol @ chol.T - regularized) / torch.linalg.norm(regularized)), 'triangular_relative_residual': triangular_residual, 'ridge_identity_residual_frobenius': float(torch.linalg.norm(ridge_identity - identity)), 'ridge_condition_limit': 10000000000.0, 'triangular_relative_residual_limit': 1e-08}
    json.dumps(diagnostics, allow_nan=False)
    if not 1.0 <= diagnostics['ridge_condition'] <= 10000000000.0:
        raise ValueError('derivative dictionary ridge condition exceeds 1e10')
    if triangular_residual > 1e-08:
        raise ValueError('derivative dictionary triangular residual exceeds 1e-8')
    return (basis, diagnostics)

def d45_mul(a, b):
    out = a.new_zeros((a.shape[0], a.shape[1] + b.shape[1] - 1))
    for i in range(a.shape[1]):
        for j in range(b.shape[1]):
            out[:, i + j] += a[:, i] * b[:, j]
    return out

def d45_y_times(a, axis):
    out = a.new_zeros((a.shape[0], a.shape[1] + 1))
    out[:, axis:axis + a.shape[1]] = a
    return out

@lru_cache(maxsize=1)
def d45_population_moments():
    records = []
    v = d__variance_rules()[1]
    for order in (128, 256):
        (z, weights) = np.polynomial.hermite.hermgauss(order)
        weights = weights / np.sqrt(np.pi)
        h = np.tanh(np.sqrt(2.0) * z)
        H = np.tanh(np.sqrt(2.0 * v) * z)
        (p, d) = (1 - h * h, 1 - H * H)
        tau = float(weights @ (H * H))
        (d1, d2) = (float(weights @ d), float(weights @ (d * d)))
        H2d = float(weights @ (H * H * d))
        H2d2 = float(weights @ (H * H * d * d))
        lam_diag = float(weights @ (h * h * p * p)) * (d2 - 2 * H2d)
        lam_off = v * float(weights @ (p * p)) * d1 * d1
        lam = [[lam_diag, lam_off], [lam_off, lam_diag]]
        g = [[[H2d2 if a == b == k else tau * d2 if a == b else H2d * d1 for k in range(2)] for b in range(2)] for a in range(2)]
        records.append(dict(order=order, v=v, tau=tau, mean_d=d1, mean_d2=d2, mean_H2d=H2d, mean_H2d2=H2d2, lam=lam, g=g))
    (left, right) = records
    discrepancy = max((abs(left[k] - right[k]) for k in ('tau', 'mean_d', 'mean_d2', 'mean_H2d', 'mean_H2d2')))
    discrepancy = max(discrepancy, float(np.max(np.abs(np.array(left['lam']) - np.array(right['lam'])))))
    discrepancy = max(discrepancy, float(np.max(np.abs(np.array(left['g']) - np.array(right['g'])))))
    if discrepancy > 1e-09:
        raise ValueError('population moment quadrature gate failed')
    return dict(working=right, coarse=left, maximum_discrepancy=discrepancy, discrepancy_is_error_bound=False, method='one-dimensional Gauss-Hermite 128/256, working 256')

@torch.no_grad()
def d45_raw_features(initial, p):
    if isinstance(p, bool) or not isinstance(p, int) or p not in (4, 5):
        raise ValueError('extension order must be 4 or 5')
    (lower, upper, metadata) = d_raw_features(initial, 3)
    metadata.update(p=p, maximum_weight_taylor_power=p + 1, dictionary='derivative_collected_increment_extension', inherited_builder='new_dictionary.py', p4_span_equals_p3=True, population_moments=d45_population_moments())
    if p == 5:
        n = len(initial.w)
        (h, L) = (lower[:, :2], lower[:, 2:].reshape(n, 2, 2))
        H = torch.tanh(initial.M @ h)
        lower_gate = 1 - h.square()
        lower_second = -2 * h * lower_gate
        d = 1 - H.square()
        e = -2 * H * d
        third = (6 * H.square() - 2) * d
        U = upper[:, :4].reshape(n, 2, 2)
        Q = (initial.M.T @ U.flatten(1)).reshape(n, 2, 2)
        F = d__variance_rules()[1] * U + (initial.M @ L.flatten(1)).reshape(n, 2, 2)
        S = H
        R = [d45_y_times(F[:, a, :], a) / 2 for a in range(2)]
        q = [d45_y_times(lower_gate[:, a:a + 1] * Q[:, a, :], a) / 2 for a in range(2)]
        J = sum((d45_y_times(d[:, b:b + 1] * R[b], b) for b in range(2)))
        K3 = [d[:, a:a + 1] * J / 3 + e[:, a:a + 1] * d45_mul(S, R[a]) for a in range(2)]
        collection_error = max((float((6 * K3[a] - upper[:, 4 + 4 * a:8 + 4 * a]).abs().max()) for a in range(2)))
        moments = d45_population_moments()['working']
        (T, E) = ([], [])
        for a in range(2):
            B2adj = initial.w.new_zeros((n, 4))
            for b in range(2):
                gram = initial.w.new_zeros((n, 3))
                (gram[:, 0], gram[:, 2]) = moments['g'][a][b]
                B2adj += d45_y_times(h[:, b:b + 1] * gram, b) / 2
            value = d45_y_times(lower_gate[:, a:a + 1].square() * (initial.M.T @ K3[a]), a) / 4 + d45_y_times(lower_gate[:, a:a + 1].square() * B2adj, a) / 4 + lower_second[:, a:a + 1] * d45_mul(q[a], q[a])
            T.append(value)
        for a in range(2):
            contraction = initial.w.new_zeros((n, 4))
            for b in range(2):
                contraction += moments['lam'][a][b] * d45_y_times(d45_y_times(U[:, b, :], b), b)
            E.append(initial.M @ T[a] + d__variance_rules()[1] * d45_y_times(K3[a], a) / 4 + 3 * d45_y_times(contraction, a) / 8)
        K = sum((d45_y_times(d[:, b:b + 1] * E[b] + e[:, b:b + 1] * d45_mul(R[b], R[b]) / 2, b) for b in range(2)))
        K5 = [d[:, a:a + 1] * K / 5 + e[:, a:a + 1] * d45_mul(J, R[a]) / 3 + e[:, a:a + 1] * d45_mul(S, E[a]) + third[:, a:a + 1] * d45_mul(S, d45_mul(R[a], R[a])) / 2 for a in range(2)]
        zero_error = max(float(T[0][:, 4].abs().max()), float(T[1][:, 0].abs().max()))
        if zero_error != 0:
            raise ValueError('symbolic polynomial divisibility failed')
        scale = max(1.0, float(upper.abs().max()))
        if collection_error > 1e-12 * scale:
            raise ValueError('inherited coefficient collection mismatch')
        lower = torch.cat((lower, 24 * T[0][:, :4], 24 * T[1][:, 1:]), dim=1)
        upper = torch.cat((upper, 120 * K5[0], 120 * K5[1]), dim=1)
        metadata.update(lower_column_order=metadata['lower_column_order'] + [f'24*T{a + 1}_y1^{4 - j}y2^{j}' for a in range(2) for j in range(a, a + 4)], upper_column_order=metadata['upper_column_order'] + [f'120*K5_{a + 1}_y1^{5 - j}y2^{j}' for a in range(2) for j in range(6)], added_lower_raw_scale=24, added_upper_raw_scale=120, raw_column_rescaling='inherited columns unchanged; new derivative coefficients times 4! and 5!', inherited_collection_absolute_error=collection_error, polynomial_divisibility_absolute_error=zero_error, scalar_contractions='population Gaussian moments, not empirical task contractions')
    if not bool(torch.isfinite(lower).all() and torch.isfinite(upper).all()):
        raise ValueError('nonfinite higher-order dictionary')
    metadata.update(K1=lower.shape[1], K2=upper.shape[1])
    return (lower.contiguous(), upper.contiguous(), metadata)

def d7_mul(a, b):
    rows = max(a.shape[0], b.shape[0])
    if a.shape[0] not in (1, rows) or b.shape[0] not in (1, rows):
        raise ValueError('incompatible polynomial row counts')
    out = a.new_zeros((rows, a.shape[1] + b.shape[1] - 1))
    for i in range(a.shape[1]):
        for j in range(b.shape[1]):
            out[:, i + j] += a[:, i] * b[:, j]
    return out

def d7_ytimes(a, axis):
    return d45_y_times(a, axis)

@lru_cache(maxsize=1)
def d7_moment_metadata():
    (coarse, fine) = (g_population_contractions(192), g_population_contractions(256))
    keys = ('v', 'tau', 'kappa', 'A', 'C', 'P', 'LL', 'UK', 'hT', 'VV', 'hV', 'beta')
    errors = {key: float(np.max(np.abs(np.asarray(coarse[key]) - np.asarray(fine[key])))) for key in keys}
    maximum = max(errors.values())
    parity = max(abs(fine['beta'][0, 1]), abs(fine['beta'][0, 3]), abs(fine['beta'][1, 0]), abs(fine['beta'][1, 2]), float(np.max(np.abs(fine['beta'][0] - fine['beta'][1, ::-1]))))
    if maximum > 1e-09 or parity > 2e-13 or fine['adjoint_response_error'] > 2e-13:
        raise ValueError('p7 population moment validation failed')
    return dict(method='two-dimensional Gauss-Hermite after analytic Gaussian innovation integration', resolution_orders=[192, 256], working_order=256, resolution_discrepancies=errors, maximum_discrepancy=maximum, discrepancy_is_error_bound=False, beta_parity_error=parity, beta_parity_projection='average the two equal diagonal/off-diagonal entries; set forbidden monomials to exact zero', beta_diagonal=float((fine['beta'][0, 0] + fine['beta'][1, 3]) / 2), beta_off_diagonal=float((fine['beta'][0, 2] + fine['beta'][1, 1]) / 2), adjoint_response_error=float(fine['adjoint_response_error']), source_covariance_minimum_eigenvalue=float(fine['source_covariance_minimum_eigenvalue']), contractions='initial Gaussian population UK,hT,VV,hV,C,beta; never empirical task contractions')

def d7__graph(initial, lower, upper, *, through_p7):
    """Ordinary homogeneous coefficient fields; exposed for scoped checks."""
    metadata = d7_moment_metadata()
    moments = g_population_contractions(256)
    to_tensor = lambda a: torch.as_tensor(a, dtype=initial.w.dtype, device=initial.w.device)
    n = len(initial.w)
    h = lower[:, :2]
    ell = 1 - h.square()
    m = -2 * h * ell
    lower_third = (6 * h.square() - 2) * ell
    H = torch.tanh(initial.M @ h)
    d = 1 - H.square()
    e = -2 * H * d
    f = (6 * H.square() - 2) * d
    fourth = 8 * H * d * (2 - 3 * H.square())
    U = upper[:, :4].reshape(n, 2, 2)
    L = lower[:, 2:6].reshape(n, 2, 2)
    F = d__variance_rules()[1] * U + (initial.M @ L.flatten(1)).reshape(n, 2, 2)
    Q = (initial.M.T @ U.flatten(1)).reshape(n, 2, 2)
    S = H
    sd = [S * d[:, a:a + 1] for a in range(2)]
    q = [d7_ytimes(ell[:, a:a + 1] * Q[:, a, :], a) / 2 for a in range(2)]
    V = [d7_ytimes(L[:, a, :], a) / 2 for a in range(2)]
    R = [d7_ytimes(F[:, a, :], a) / 2 for a in range(2)]
    J = sum((d7_ytimes(d[:, a:a + 1] * R[a], a) for a in range(2)))
    K3 = [upper[:, 4 + 4 * a:8 + 4 * a] / 6 for a in range(2)]
    T = [initial.w.new_zeros((n, 5)) for _ in range(2)]
    (T[0][:, :4], T[1][:, 1:]) = (lower[:, 6:10] / 24, lower[:, 10:14] / 24)
    K5 = [upper[:, 12 + 6 * a:18 + 6 * a] / 120 for a in range(2)]
    beta = [initial.w.new_zeros((1, 4)) for _ in range(2)]
    beta[0][0, 0] = beta[1][0, 3] = metadata['beta_diagonal']
    beta[0][0, 2] = beta[1][0, 1] = metadata['beta_off_diagonal']
    B = sum((d7_mul(H[:, a:a + 1], beta[a]) for a in range(2)))
    (Z, Zplus) = ([], [])
    for a in range(2):
        bz = sum((d7_mul(F[:, a, b:b + 1], beta[b]) for b in range(2)))
        sy = F[:, a, :]
        Z.append(-d7_ytimes(bz, a) / 20 - d7_mul(sy, beta[a]) / 5)
        Zplus.append(d7_ytimes(bz, a) / 10 + 3 * d7_mul(sy, beta[a]) / 8)
    common_M = sum((d7_ytimes(d[:, b:b + 1] * Z[b], b) - d7_mul(d[:, b:b + 1] * R[b], beta[b]) for b in range(2)))
    common_P = sum((d7_ytimes(d[:, b:b + 1] * (Zplus[b] - Z[b]), b) + 11 * d7_mul(d[:, b:b + 1] * R[b], beta[b]) / 4 for b in range(2)))
    M = [d[:, a:a + 1] * common_M / 6 - e[:, a:a + 1] * d7_mul(B, R[a]) / 4 + e[:, a:a + 1] * d7_mul(S, Z[a]) for a in range(2)]
    P = [d[:, a:a + 1] * common_P / 7 + 3 * e[:, a:a + 1] * d7_mul(B, R[a]) / 5 + e[:, a:a + 1] * d7_mul(S, Zplus[a] - Z[a] / 2) for a in range(2)]
    graph = dict(h=h, H=H, U=U, L=L, F=F, q=q, V=V, R=R, J=J, K3=K3, T=T, K5=K5, beta=beta, B=B, Z=Z, Zplus=Zplus, M=M, P=P)
    if not through_p7:
        return graph
    (C, UK) = (to_tensor(moments['C']), to_tensor(moments['UK']))
    (hT, VV, hV) = (to_tensor(moments[key]) for key in ('hT', 'VV', 'hV'))

    def pair_sd_sd(a, b):
        out = initial.w.new_zeros((1, 3))
        for c in range(2):
            for k in range(2):
                out[0, c + k] += C[2 * a + c, 2 * b + k]
        return out

    def pair_sd_K3(a, b):
        return sum((d7_ytimes(UK[a, c, b][None, :], c) for c in range(2)))
    B2adj_sd = [sum((d7_ytimes(d7_mul(h[:, b:b + 1], pair_sd_sd(b, a)), b) / 2 for b in range(2))) for a in range(2)]
    J3 = [d7_ytimes(initial.M.T @ K3[a] + B2adj_sd[a], a) for a in range(2)]
    P4 = [ell[:, a:a + 1] * J3[a] / 4 + m[:, a:a + 1] * d7_mul(q[a], d7_ytimes(initial.M.T @ sd[a], a)) / 4 for a in range(2)]
    T_recomputed = [ell[:, a:a + 1] * P4[a] + m[:, a:a + 1] * d7_mul(q[a], q[a]) / 2 for a in range(2)]
    composition_error = max((float((T_recomputed[a] - T[a]).abs().max()) for a in range(2)))
    E = []
    for a in range(2):
        B2V = sum((d7_ytimes(d7_mul(sd[b], hV[b, a][None, :]), b) / 2 for b in range(2)))
        Fh = sum((d7_ytimes((moments['v'] * K3[b] if a == b else torch.zeros_like(K3[b])) + d7_mul(sd[b], hV[a, b][None, :]), b) / 4 for b in range(2)))
        E.append(initial.M @ T[a] + B2V + Fh)
    N = sum((d7_ytimes(d[:, b:b + 1] * E[b] + e[:, b:b + 1] * d7_mul(R[b], R[b]) / 2, b) for b in range(2)))
    T6 = []
    for a in range(2):
        B2adj_K3 = sum((d7_ytimes(d7_ytimes(d7_mul(h[:, b:b + 1], pair_sd_K3(b, a)), a), b) / 2 for b in range(2)))
        Fadj_sd = sum((d7_ytimes(d7_ytimes(d7_mul(h[:, b:b + 1], pair_sd_K3(a, b)) + d7_mul(V[b], pair_sd_sd(b, a)), a), b) for b in range(2)))
        value = ell[:, a:a + 1].square() * (d7_ytimes(initial.M.T @ K5[a], a) + B2adj_K3 + Fadj_sd / 4) / 6 + ell[:, a:a + 1] * m[:, a:a + 1] * d7_mul(q[a], J3[a]) / 6 + 4 * m[:, a:a + 1] * d7_mul(q[a], P4[a]) / 3 + lower_third[:, a:a + 1] * d7_mul(q[a], d7_mul(q[a], q[a])) / 3
        T6.append(value)
    E6 = []
    for a in range(2):
        B2T = sum((d7_ytimes(d7_mul(sd[b], hT[b, a][None, :]), b) / 2 for b in range(2)))
        FV = sum((d7_ytimes(d7_mul(K3[b], hV[b, a][None, :]) + d7_mul(sd[b], VV[b, a][None, :]), b) / 4 for b in range(2)))
        Gh = sum((d7_ytimes((moments['v'] * K5[b] if a == b else torch.zeros_like(K5[b])) + d7_mul(K3[b], hV[a, b][None, :]) + d7_mul(sd[b], hT[a, b][None, :]), b) / 6 for b in range(2)))
        E6.append(initial.M @ T6[a] + B2T + FV + Gh)
    O = sum((d7_ytimes(d[:, a:a + 1] * E6[a] + e[:, a:a + 1] * d7_mul(R[a], E[a]) + f[:, a:a + 1] * d7_mul(R[a], d7_mul(R[a], R[a])) / 6, a) for a in range(2)))
    K7 = [d[:, a:a + 1] * O / 7 + e[:, a:a + 1] * d7_mul(N, R[a]) / 5 + d7_mul(J, e[:, a:a + 1] * E[a] + f[:, a:a + 1] * d7_mul(R[a], R[a]) / 2) / 3 + d7_mul(S, e[:, a:a + 1] * E6[a] + f[:, a:a + 1] * d7_mul(R[a], E[a]) + fourth[:, a:a + 1] * d7_mul(R[a], d7_mul(R[a], R[a])) / 6) for a in range(2)]
    zero_error = max(float(T6[0][:, 6].abs().max()), float(T6[1][:, 0].abs().max()))
    if zero_error != 0:
        raise ValueError('p7 symbolic y_a divisibility failed')
    scale = max(1.0, max((float(x.abs().max()) for x in T)))
    if composition_error > 1e-09 * scale:
        raise ValueError('p7 inherited lower composition mismatch')
    graph.update(P4=P4, E=E, N=N, T6=T6, E6=E6, O=O, K7=K7, composition_absolute_error=composition_error, divisibility_absolute_error=zero_error)
    return graph

@torch.no_grad()
def d7_raw_features(initial, p):
    if isinstance(p, bool) or not isinstance(p, int) or p not in (6, 7):
        raise ValueError('full-time extension order must be 6 or 7')
    (lower, upper, metadata) = d45_raw_features(initial, 5)
    graph = d7__graph(initial, lower, upper, through_p7=p == 7)
    m_columns = torch.stack((graph['M'][0][:, 1], graph['M'][0][:, 2], graph['M'][1][:, 3], graph['M'][1][:, 4]), dim=1)
    upper = torch.cat((upper, 720 * m_columns), dim=1)
    upper_names = metadata['upper_column_order'] + ['720*M1_y1^4y2', '720*M1_y1^3y2^2', '720*M2_y1^2y2^3', '720*M2_y1y2^4']
    lower_names = metadata['lower_column_order']
    if p == 7:
        tau = g_population_contractions(256)['tau']
        p_columns = torch.stack((graph['P'][0][:, 1], graph['P'][1][:, 4]), dim=1)
        lower = torch.cat((lower, 720 * graph['T6'][0][:, :6], 720 * graph['T6'][1][:, 1:]), dim=1)
        upper = torch.cat((upper, 5040 * tau * p_columns, 5040 * graph['K7'][0], 5040 * graph['K7'][1]), dim=1)
        lower_names = lower_names + [f'720*T6_{a + 1}_y1^{6 - j}y2^{j}' for a in range(2) for j in range(a, a + 6)]
        upper_names += ['5040*tau*P1_y1^4y2', '5040*tau*P2_y1y2^4'] + [f'5040*K7_{a + 1}_y1^{7 - j}y2^{j}' for a in range(2) for j in range(8)]
    if not bool(torch.isfinite(lower).all() and torch.isfinite(upper).all()):
        raise ValueError('nonfinite p7 derivative dictionary')
    metadata.update(dictionary='derivative_collected_full_time_increment_extension', inherited_builder='new_dictionary_p45.py', p=p, maximum_weight_taylor_power=p + 1, K1=lower.shape[1], K2=upper.shape[1], lower_column_order=lower_names, upper_column_order=upper_names, p6_span_equals_p5_claim=False, minimal_population_dimension_claim=False, full_lower_label_degrees_retained=True, p7_population_moments=d7_moment_metadata(), raw_column_rescaling='p5 prefix unchanged; M time6 times6!; T6 time6 times6!; tauP and K7 time7 times7!', added_M_raw_scale=720, added_T6_raw_scale=720 if p == 7 else None, added_P_raw_scale='5040*tau' if p == 7 else None, added_K7_raw_scale=5040 if p == 7 else None, new_dense_adjoint_query_count=12 if p == 7 else 0, new_dense_forward_query_count=12 if p == 7 else 0, inherited_p5_raw_prefix_exact=True, scalar_contractions='Gaussian population moments, never empirical task contractions')
    if p == 7:
        metadata.update(lower_composition_absolute_error=graph['composition_absolute_error'], polynomial_divisibility_absolute_error=graph['divisibility_absolute_error'])
    return (lower.contiguous(), upper.contiguous(), metadata)
