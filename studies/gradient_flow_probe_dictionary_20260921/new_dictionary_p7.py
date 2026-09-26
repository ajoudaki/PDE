"""Full-time frozen derivative factors through W2(t) powers seven/eight.

See P7_DERIVATION.md. Binary slot j is y1**(degree-j)*y2**j.
All labels are formal coefficient devices. Population contractions are
deterministic Gaussian integrals; the actual initialized matrix supplies
every forward/adjoint query. The exact p5 raw prefix is preserved.
"""
from functools import lru_cache

import numpy as np
import torch

import new_dictionary as base
import new_dictionary_p45 as previous
from p7_gaussian_check import population_contractions
from pde.observable_torch_p1 import ClosureEngine


def mul(a, b):
    rows = max(a.shape[0], b.shape[0])
    if a.shape[0] not in (1, rows) or b.shape[0] not in (1, rows):
        raise ValueError("incompatible polynomial row counts")
    out = a.new_zeros((rows, a.shape[1]+b.shape[1]-1))
    for i in range(a.shape[1]):
        for j in range(b.shape[1]):
            out[:, i+j] += a[:, i]*b[:, j]
    return out


def ytimes(a, axis):
    return previous.y_times(a, axis)


@lru_cache(maxsize=1)
def moment_metadata():
    coarse, fine = population_contractions(192), population_contractions(256)
    keys = ('v', 'tau', 'kappa', 'A', 'C', 'P', 'LL', 'UK', 'hT', 'VV', 'hV', 'beta')
    errors = {key: float(np.max(np.abs(np.asarray(coarse[key])-np.asarray(fine[key]))))
              for key in keys}
    maximum = max(errors.values())
    parity = max(abs(fine['beta'][0, 1]), abs(fine['beta'][0, 3]),
                 abs(fine['beta'][1, 0]), abs(fine['beta'][1, 2]),
                 float(np.max(np.abs(fine['beta'][0]-fine['beta'][1, ::-1]))))
    if maximum > 1e-9 or parity > 2e-13 or fine['adjoint_response_error'] > 2e-13:
        raise ValueError('p7 population moment validation failed')
    return dict(method='two-dimensional Gauss-Hermite after analytic Gaussian innovation integration',
                resolution_orders=[192, 256], working_order=256,
                resolution_discrepancies=errors, maximum_discrepancy=maximum,
                discrepancy_is_error_bound=False, beta_parity_error=parity,
                beta_parity_projection='average the two equal diagonal/off-diagonal entries; set forbidden monomials to exact zero',
                beta_diagonal=float((fine['beta'][0, 0]+fine['beta'][1, 3])/2),
                beta_off_diagonal=float((fine['beta'][0, 2]+fine['beta'][1, 1])/2),
                adjoint_response_error=float(fine['adjoint_response_error']),
                source_covariance_minimum_eigenvalue=float(fine['source_covariance_minimum_eigenvalue']),
                contractions='initial Gaussian population UK,hT,VV,hV,C,beta; never empirical task contractions')


def _graph(initial, lower, upper, *, through_p7):
    """Ordinary homogeneous coefficient fields; exposed for scoped checks."""
    metadata = moment_metadata()
    moments = population_contractions(256)
    to_tensor = lambda a: torch.as_tensor(a, dtype=initial.w.dtype, device=initial.w.device)
    n = len(initial.w)
    h = lower[:, :2]
    ell = 1-h.square()
    m = -2*h*ell
    lower_third = (6*h.square()-2)*ell
    H = torch.tanh(initial.M @ h)
    d = 1-H.square()
    e = -2*H*d
    f = (6*H.square()-2)*d
    fourth = 8*H*d*(2-3*H.square())
    U = upper[:, :4].reshape(n, 2, 2)
    L = lower[:, 2:6].reshape(n, 2, 2)
    F = base._variance_rules()[1]*U+(initial.M @ L.flatten(1)).reshape(n, 2, 2)
    Q = (initial.M.T @ U.flatten(1)).reshape(n, 2, 2)
    S = H
    sd = [S*d[:, a:a+1] for a in range(2)]
    q = [ytimes(ell[:, a:a+1]*Q[:, a, :], a)/2 for a in range(2)]
    V = [ytimes(L[:, a, :], a)/2 for a in range(2)]
    R = [ytimes(F[:, a, :], a)/2 for a in range(2)]
    J = sum(ytimes(d[:, a:a+1]*R[a], a) for a in range(2))
    K3 = [upper[:, 4+4*a:8+4*a]/6 for a in range(2)]
    T = [initial.w.new_zeros((n, 5)) for _ in range(2)]
    T[0][:, :4], T[1][:, 1:] = lower[:, 6:10]/24, lower[:, 10:14]/24
    K5 = [upper[:, 12+6*a:18+6*a]/120 for a in range(2)]
    beta = [initial.w.new_zeros((1, 4)) for _ in range(2)]
    beta[0][0, 0] = beta[1][0, 3] = metadata['beta_diagonal']
    beta[0][0, 2] = beta[1][0, 1] = metadata['beta_off_diagonal']
    B = sum(mul(H[:, a:a+1], beta[a]) for a in range(2))
    Z, Zplus = [], []
    for a in range(2):
        bz = sum(mul(F[:, a, b:b+1], beta[b]) for b in range(2))
        sy = F[:, a, :]
        Z.append(-ytimes(bz, a)/20-mul(sy, beta[a])/5)
        Zplus.append(ytimes(bz, a)/10+3*mul(sy, beta[a])/8)
    common_M = sum(ytimes(d[:, b:b+1]*Z[b], b)
                   -mul(d[:, b:b+1]*R[b], beta[b]) for b in range(2))
    common_P = sum(ytimes(d[:, b:b+1]*(Zplus[b]-Z[b]), b)
                   +11*mul(d[:, b:b+1]*R[b], beta[b])/4 for b in range(2))
    M = [d[:, a:a+1]*common_M/6-e[:, a:a+1]*mul(B, R[a])/4
         +e[:, a:a+1]*mul(S, Z[a]) for a in range(2)]
    P = [d[:, a:a+1]*common_P/7+3*e[:, a:a+1]*mul(B, R[a])/5
         +e[:, a:a+1]*mul(S, Zplus[a]-Z[a]/2) for a in range(2)]
    graph = dict(h=h, H=H, U=U, L=L, F=F, q=q, V=V, R=R, J=J,
                 K3=K3, T=T, K5=K5, beta=beta, B=B, Z=Z, Zplus=Zplus, M=M, P=P)
    if not through_p7:
        return graph
    C, UK = to_tensor(moments['C']), to_tensor(moments['UK'])
    hT, VV, hV = (to_tensor(moments[key]) for key in ('hT', 'VV', 'hV'))
    def pair_sd_sd(a, b):
        out = initial.w.new_zeros((1, 3))
        for c in range(2):
            for k in range(2):
                out[0, c+k] += C[2*a+c, 2*b+k]
        return out
    def pair_sd_K3(a, b):
        return sum(ytimes(UK[a, c, b][None, :], c) for c in range(2))
    B2adj_sd = [sum(ytimes(mul(h[:, b:b+1], pair_sd_sd(b, a)), b)/2
                    for b in range(2)) for a in range(2)]
    J3 = [ytimes(initial.M.T @ K3[a]+B2adj_sd[a], a) for a in range(2)]
    P4 = [ell[:, a:a+1]*J3[a]/4
          +m[:, a:a+1]*mul(q[a], ytimes(initial.M.T @ sd[a], a))/4
          for a in range(2)]
    # Check preactivation composition against the inherited activation field.
    T_recomputed = [ell[:, a:a+1]*P4[a]+m[:, a:a+1]*mul(q[a], q[a])/2
                    for a in range(2)]
    composition_error = max(float((T_recomputed[a]-T[a]).abs().max()) for a in range(2))
    E = []
    for a in range(2):
        B2V = sum(ytimes(mul(sd[b], hV[b, a][None, :]), b)/2 for b in range(2))
        Fh = sum(ytimes((moments['v']*K3[b] if a == b else torch.zeros_like(K3[b]))
                         +mul(sd[b], hV[a, b][None, :]), b)/4 for b in range(2))
        E.append(initial.M @ T[a]+B2V+Fh)
    N = sum(ytimes(d[:, b:b+1]*E[b]+e[:, b:b+1]*mul(R[b], R[b])/2, b)
            for b in range(2))
    T6 = []
    for a in range(2):
        B2adj_K3 = sum(ytimes(ytimes(mul(h[:, b:b+1], pair_sd_K3(b, a)), a), b)/2
                       for b in range(2))
        Fadj_sd = sum(ytimes(ytimes(mul(h[:, b:b+1], pair_sd_K3(a, b))
                                  +mul(V[b], pair_sd_sd(b, a)), a), b)
                      for b in range(2))
        value = (ell[:, a:a+1].square()*(ytimes(initial.M.T @ K5[a], a)
                                        +B2adj_K3+Fadj_sd/4)/6
                 +ell[:, a:a+1]*m[:, a:a+1]*mul(q[a], J3[a])/6
                 +4*m[:, a:a+1]*mul(q[a], P4[a])/3
                 +lower_third[:, a:a+1]*mul(q[a], mul(q[a], q[a]))/3)
        T6.append(value)
    E6 = []
    for a in range(2):
        B2T = sum(ytimes(mul(sd[b], hT[b, a][None, :]), b)/2 for b in range(2))
        FV = sum(ytimes(mul(K3[b], hV[b, a][None, :])+mul(sd[b], VV[b, a][None, :]), b)/4
                 for b in range(2))
        Gh = sum(ytimes((moments['v']*K5[b] if a == b else torch.zeros_like(K5[b]))
                        +mul(K3[b], hV[a, b][None, :])+mul(sd[b], hT[a, b][None, :]), b)/6
                 for b in range(2))
        E6.append(initial.M @ T6[a]+B2T+FV+Gh)
    O = sum(ytimes(d[:, a:a+1]*E6[a]+e[:, a:a+1]*mul(R[a], E[a])
                  +f[:, a:a+1]*mul(R[a], mul(R[a], R[a]))/6, a) for a in range(2))
    K7 = [d[:, a:a+1]*O/7+e[:, a:a+1]*mul(N, R[a])/5
          +mul(J, e[:, a:a+1]*E[a]+f[:, a:a+1]*mul(R[a], R[a])/2)/3
          +mul(S, e[:, a:a+1]*E6[a]+f[:, a:a+1]*mul(R[a], E[a])
               +fourth[:, a:a+1]*mul(R[a], mul(R[a], R[a]))/6)
          for a in range(2)]
    zero_error = max(float(T6[0][:, 6].abs().max()), float(T6[1][:, 0].abs().max()))
    if zero_error != 0:
        raise ValueError('p7 symbolic y_a divisibility failed')
    scale = max(1., max(float(x.abs().max()) for x in T))
    if composition_error > 1e-9*scale:
        raise ValueError('p7 inherited lower composition mismatch')
    graph.update(P4=P4, E=E, N=N, T6=T6, E6=E6, O=O, K7=K7,
                 composition_absolute_error=composition_error, divisibility_absolute_error=zero_error)
    return graph


@torch.no_grad()
def raw_features(initial, p):
    if isinstance(p, bool) or not isinstance(p, int) or p not in (6, 7):
        raise ValueError('full-time extension order must be 6 or 7')
    lower, upper, metadata = previous.raw_features(initial, 5)
    graph = _graph(initial, lower, upper, through_p7=(p == 7))
    m_columns = torch.stack((graph['M'][0][:, 1], graph['M'][0][:, 2],
                             graph['M'][1][:, 3], graph['M'][1][:, 4]), dim=1)
    upper = torch.cat((upper, 720*m_columns), dim=1)
    upper_names = metadata['upper_column_order']+[
        '720*M1_y1^4y2', '720*M1_y1^3y2^2', '720*M2_y1^2y2^3', '720*M2_y1y2^4']
    lower_names = metadata['lower_column_order']
    if p == 7:
        tau = population_contractions(256)['tau']
        p_columns = torch.stack((graph['P'][0][:, 1], graph['P'][1][:, 4]), dim=1)
        lower = torch.cat((lower, 720*graph['T6'][0][:, :6], 720*graph['T6'][1][:, 1:]), dim=1)
        upper = torch.cat((upper, 5040*tau*p_columns, 5040*graph['K7'][0], 5040*graph['K7'][1]), dim=1)
        lower_names = lower_names+[
            f'720*T6_{a+1}_y1^{6-j}y2^{j}' for a in range(2) for j in range(a, a+6)]
        upper_names += ['5040*tau*P1_y1^4y2', '5040*tau*P2_y1y2^4']+[
            f'5040*K7_{a+1}_y1^{7-j}y2^{j}' for a in range(2) for j in range(8)]
    if not bool(torch.isfinite(lower).all() and torch.isfinite(upper).all()):
        raise ValueError('nonfinite p7 derivative dictionary')
    metadata.update(dictionary='derivative_collected_full_time_increment_extension',
                    inherited_builder='new_dictionary_p45.py', p=p,
                    maximum_weight_taylor_power=p+1, K1=lower.shape[1], K2=upper.shape[1],
                    lower_column_order=lower_names, upper_column_order=upper_names,
                    p6_span_equals_p5_claim=False, minimal_population_dimension_claim=False,
                    full_lower_label_degrees_retained=True, p7_population_moments=moment_metadata(),
                    raw_column_rescaling='p5 prefix unchanged; M time6 times6!; T6 time6 times6!; tauP and K7 time7 times7!',
                    added_M_raw_scale=720, added_T6_raw_scale=720 if p == 7 else None,
                    added_P_raw_scale='5040*tau' if p == 7 else None,
                    added_K7_raw_scale=5040 if p == 7 else None,
                    new_dense_adjoint_query_count=12 if p == 7 else 0,
                    new_dense_forward_query_count=12 if p == 7 else 0,
                    inherited_p5_raw_prefix_exact=True,
                    scalar_contractions='Gaussian population moments, never empirical task contractions')
    if p == 7:
        metadata.update(lower_composition_absolute_error=graph['composition_absolute_error'],
                        polynomial_divisibility_absolute_error=graph['divisibility_absolute_error'])
    return lower.contiguous(), upper.contiguous(), metadata


@torch.no_grad()
def build(initial, p, *, block_size=512, forward_mode='auto'):
    lower, upper, metadata = raw_features(initial, p)
    n, eta = len(initial.w), 1/(1024*(p+1)**2)
    b1, diag1 = base._ridge_basis(lower, eta)
    b2, diag2 = base._ridge_basis(upper, eta)
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
