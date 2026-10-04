"""One bounded saved-endpoint pass; never trains or fits a model."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import time

for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'

import numpy as np
from scipy.integrate import simpson

import cubic_scalar_ode as scalar
import dense_compare as dense

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'data/generated/structured_full_rank_scalar_20260926'
OUT = BASE / 'cubic_feedback_repair_20260930/diagnostic'
TASKS = ('near_pair_sin9', 'cluster_triple_cos9', 'cluster_triple_cos1',
         'pair_cos3', 'triple_wide_mixed')


def rms(a):
    return float(np.sqrt(np.mean(np.asarray(a)**2)))


def comparison(a, b):
    return {'absolute_frobenius': float(np.linalg.norm(a-b)),
            'relative_frobenius': float(np.linalg.norm(a-b)/np.linalg.norm(b))}


def matrix(a):
    result = {'frobenius': float(np.linalg.norm(a)), 'matrix': a.tolist()}
    if a.shape[0] == a.shape[1]:
        result['eigenvalues_symmetric_part'] = np.linalg.eigvalsh((a+a.T)/2).tolist()
        result['diagonal'] = np.diag(a).tolist()
    return result


def dense_fields(state, points):
    h1 = np.tanh(points @ state.w.T)
    z2 = h1 @ state.W.T
    h2 = np.tanh(z2)
    d2 = dense._sech_squared(z2)*state.c
    d1 = dense._sech_squared(points @ state.w.T)*(d2 @ state.W)
    return h1, h2, d1, d2


def kernel_blocks(left, right, dots, n):
    h1, h2, d1, d2 = left
    p1, p2, e1, e2 = right
    return (h2 @ p2.T/n, (d1 @ e1.T/n)*dots,
            (d2 @ e2.T/n)*(h1 @ p1.T/n))


def second_feature_response(points, initial, inputs, first, gamma, beta):
    """L[q,a,b,j] = D h2(q)[initial response direction (a,b)]."""
    h1 = np.tanh(points @ initial.w.T)
    h2 = np.tanh(h1 @ initial.W.T)
    raw = ((1-h1*h1)[:, None, None, :]*beta[None, :, :, :]
           * (points @ inputs.T)[:, :, None, None])
    response = (raw.reshape(-1, initial.width) @ initial.W.T).reshape(raw.shape)
    response += gamma[None, :, :, :]*(h1 @ first.T/initial.width)[:, :, None, None]
    response *= (1-h2*h2)[:, None, None, :]
    return h1, h2, response


def diagnose(task, initial, deadline):
    if time.monotonic() >= deadline:
        raise TimeoutError('15-second endpoint-evaluation budget exhausted')
    scalar_path = BASE / 'cubic_scalar_20260930' / (task+'.npz')
    dense_path = BASE / 'all_tasks_j2_20260927/references' / (task+'__gaussian.npz')
    saved = dict(np.load(scalar_path))
    ref = dict(np.load(dense_path))
    state = dense.State(ref['w'], ref['W'], ref['c'])
    inputs = np.column_stack((np.cos(saved['train_angles']), np.sin(saved['train_angles'])))
    points = np.column_stack((np.cos(saved['angles']), np.sin(saved['angles'])))
    n, m = state.width, len(inputs)
    model = scalar.ScalarModel(saved['model_labels'], saved['initial_gram'], saved['response_gram'])
    r, z, J, P = model.unpack(saved['state'])
    K0 = model.initial_gram
    K, M, N = model.kernel(z, J)
    Q = M.T @ model.solve_gram(M)
    Kcub = K0+M+M.T+N
    coeff = scalar.QueryCoefficients(saved['query_gram'], saved['query_cubic'])
    pred = model.predict(saved['state'], coeff)
    raw = model.cubic_prediction(saved['state'], coeff)
    frozen_along_z = -model.alpha*(coeff.cross_gram @ z)
    alias = pred-raw
    cross_cubic = (coeff.cross_gram + model.alpha**2
                   *np.einsum('qabc,bc->qa', coeff.cubic, J))
    cross_completion = coeff.cross_gram @ model.solve_gram(Q)
    cross_eff = cross_cubic+cross_completion
    train = dense_fields(state, inputs)
    Bc, Bw, BW = kernel_blocks(train, train, inputs@inputs.T, n)
    Kdense = Bc+Bw+BW
    first, second, _, _, gamma, beta = scalar._initial_responses(initial.w, initial.W, inputs)
    _, _, L = second_feature_response(inputs, initial, inputs, first, gamma, beta)
    hcorr = model.alpha**2*np.einsum('ab,qabn->qn', J, L)
    c1 = -model.alpha*(z @ second)
    c3 = -model.alpha**3*np.einsum('qab,qabn->n', P, L)
    Mdirect = second @ hcorr.T/n
    reconstructed_raw_train = (second @ (c1+c3)+hcorr @ c1)/n
    projection_h = (np.eye(m)+M.T @ model.solve_gram(np.eye(m))) @ second

    prediction, dense_cross, dense_parts = [], [], [[], [], []]
    all_h0, all_hcorr, all_dense_h, reconstructed_raw = [], [], [], []
    for start in range(0, len(points), 16):
        if time.monotonic() >= deadline:
            raise TimeoutError('15-second endpoint-evaluation budget exhausted')
        query = points[start:start+16]
        fields = dense_fields(state, query)
        blocks = kernel_blocks(fields, train, query@inputs.T, n)
        prediction.append(fields[1] @ state.c/n)
        dense_cross.append(sum(blocks))
        for out, block in zip(dense_parts, blocks):
            out.append(block)
        _, h0, query_L = second_feature_response(query, initial, inputs, first, gamma, beta)
        delta_h = model.alpha**2*np.einsum('ab,qabn->qn', J, query_L)
        all_h0.append(h0)
        all_hcorr.append(delta_h)
        all_dense_h.append(fields[1])
        reconstructed_raw.append((h0 @ (c1+c3)+delta_h @ c1)/n)
    prediction, dense_cross = np.concatenate(prediction), np.concatenate(dense_cross)
    dense_parts = [np.concatenate(x) for x in dense_parts]
    h0, delta_h, hdense = [np.concatenate(x) for x in (all_h0, all_hcorr, all_dense_h)]
    hist = saved['history']
    times, losses = hist[:, 0], hist[:, 1]
    dt = np.diff(times)
    loss_integral_trap = float(np.trapz(losses, times))
    loss_integral_simpson = float(simpson(losses, x=times))
    # Accepted losses are monotone; the enclosure assumes monotonicity of
    # the continuous scalar flow, which follows from the PSD kernel.
    integral_lower, integral_upper = float(dt@losses[1:]), float(dt@losses[:-1])
    q_from_integral = lambda value: float(-2*model.alpha*(model.labels@z)-4*value)
    q_dense = float(np.mean(state.c**2))
    q_proxy = q_from_integral(loss_integral_trap)
    replay = {
        'dense_circle_max_abs': float(np.max(np.abs(prediction-ref['prediction']))),
        'dense_train_max_abs': float(np.max(np.abs(train[1]@state.c/n-ref['train_prediction']))),
        'scalar_circle_max_abs': float(np.max(np.abs(pred[:len(points)]-saved['scalar']))),
        'cubic_training_kernel_identity': float(np.max(np.abs(cross_cubic[len(points):]-Kcub))),
        'second_feature_cross_gram_identity': float(np.max(np.abs(Mdirect-M))),
        'explicit_cubic_readout_train_identity': float(np.max(np.abs(reconstructed_raw_train-raw[len(points):]))),
        'explicit_cubic_readout_circle_identity': float(np.max(np.abs(np.concatenate(reconstructed_raw)-raw[:len(points)]))),
    }
    # The explicit readout reconstruction also uses numerical shuffle
    # identities among integrated P and z,J, hence has the saved ODE error.
    assert max(value for key, value in replay.items()
               if not key.startswith('explicit_cubic')) < 1e-10, replay
    assert max(value for key, value in replay.items()
               if key.startswith('explicit_cubic')) < 1e-8, replay
    assert np.all(np.isfinite(dense_cross)) and np.all(np.isfinite(cross_eff))
    assert np.all(np.diff(losses) <= 1e-12)
    assert np.max(np.abs(prediction)) <= np.sqrt(q_dense)+1e-12
    # Eigenbasis of K0 makes the hard, weak-initial-kernel direction explicit.
    ev, vec = np.linalg.eigh(K0)
    direction = vec[:, 0]
    result = {
        'task': task, 'inputs': inputs.tolist(), 'labels': model.labels.tolist(),
        'scalar_time': float(times[-1]), 'dense_time': float(ref['history'][-1, 0]),
        'checks': replay,
        'training': {name: matrix(a) for name, a in {
            'K0': K0, 'M_plus_transpose': M+M.T, 'N': N, 'Q_completion': Q,
            'scalar_completed': K, 'scalar_cubic': Kcub,
            'dense_readout': Bc, 'dense_first_layer': Bw,
            'dense_middle_layer': BW, 'dense_full': Kdense,
            'scalar_feature_gram_projected': K0+M+M.T+Q,
            'scalar_feature_gram_full_second_order': (second+hcorr)@(second+hcorr).T/n,
        }.items()},
        'kernel_errors': {
            'completed_vs_dense': comparison(K, Kdense),
            'cubic_vs_dense': comparison(Kcub, Kdense),
            'projected_feature_vs_dense': comparison(K0+M+M.T+Q, Bc),
            'linear_feature_vs_dense': comparison(K0+M+M.T, Bc),
            'response_N_vs_dense_lower': comparison(N, Bw+BW),
            'circle_completed_vs_dense': comparison(cross_eff[:len(points)], dense_cross),
            'circle_cubic_vs_dense': comparison(cross_cubic[:len(points)], dense_cross),
            'circle_completion_frobenius': float(np.linalg.norm(cross_completion[:len(points)])),
            'circle_dense_frobenius': float(np.linalg.norm(dense_cross)),
            'initial_inverse_M_spectral': float(np.linalg.norm(model.solve_gram(M), 2)),
        },
        'weak_initial_direction': {
            'initial_eigenvalue': float(ev[0]), 'direction': direction.tolist(),
            **{name: float(direction@a@direction) for name, a in {
                'dense_readout': Bc, 'dense_lower': Bw+BW, 'dense_full': Kdense,
                'M_plus_transpose': M+M.T, 'N': N, 'Q': Q,
                'scalar_completed': K}.items()},
        },
        'readout': {
            'dense_q_exact': q_dense, 'dense_sqrt_q': float(np.sqrt(q_dense)),
            'scalar_compatible_q_trapezoid': q_proxy,
            'scalar_compatible_q_simpson': q_from_integral(loss_integral_simpson),
            'scalar_compatible_q_monotone_enclosure': [q_from_integral(integral_upper), q_from_integral(integral_lower)],
            'scalar_q1': float(np.mean(c1*c1)),
            'scalar_q_order4': float(np.mean(c1*c1+2*c1*c3)),
            'scalar_q_c1_plus_c3': float(np.mean((c1+c3)**2)),
            'cubic_c3_rms': rms(c3), 'linear_c1_rms': rms(c1),
            'dense_vs_c1_c3_rms': rms(state.c-c1-c3),
            'dense_vs_c1_rms': rms(state.c-c1),
            'q0_dense': float(np.mean(initial.c**2)),
            'loss_integral_trapezoid': loss_integral_trap,
            'loss_integral_simpson': loss_integral_simpson,
        },
        'features': {
            'dense_circle_h2_rms': rms(hdense), 'initial_circle_h2_rms': rms(h0),
            'dense_h2_motion_rms': rms(hdense-h0),
            'second_order_h2_motion_rms': rms(delta_h),
            'second_order_h2_error_rms': rms(h0+delta_h-hdense),
            'second_order_h2_abs_max': float(np.max(np.abs(h0+delta_h))),
            'second_order_h2_outside_tanh_fraction': float(np.mean(np.abs(h0+delta_h)>1)),
            'projected_train_h2_rms': rms(projection_h),
            'dense_train_h2_rms': rms(train[1]),
        },
        'decoder': {
            'scalar_dense_circle_rms': rms(pred[:len(points)]-prediction),
            'cubic_dense_circle_rms': rms(raw[:len(points)]-prediction),
            'alias_circle_rms': rms(alias[:len(points)]),
            'alias_train_rms': rms(alias[len(points):]),
            'raw_cubic_circle_rms': rms(raw[:len(points)]),
            'linear_circle_rms': rms(frozen_along_z[:len(points)]),
            'cubic_increment_circle_rms': rms(raw[:len(points)]-frozen_along_z[:len(points)]),
            'scalar_circle_abs_max': float(np.max(np.abs(pred[:len(points)]))),
            'dense_circle_abs_max': float(np.max(np.abs(prediction))),
            'scalar_training_mse': float(np.mean(r*r)),
            'dense_training_mse': float(np.mean((train[1]@state.c/n-model.labels)**2)),
        },
        'source_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in (scalar_path, dense_path)},
    }
    return result


def main():
    started = time.monotonic()
    # Reserve one second for initial metadata reads performed before this script.
    deadline = started+13
    OUT.mkdir(parents=True, exist_ok=True)
    destination = OUT/'diagnostic.json'
    if destination.exists():
        raise FileExistsError(destination)
    initial = dense.initialize(1024, 1, 'gaussian')
    rows = []
    status = 'complete'
    for task in TASKS:
        try:
            rows.append(diagnose(task, initial, deadline))
        except TimeoutError as exc:
            status = str(exc)
            break
    output = {'status': status, 'wall_seconds': time.monotonic()-started,
              'budget_seconds': 15, 'mode': 'saved endpoint diagnostics only',
              'tasks': rows, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    destination.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({'status': status, 'wall_seconds': output['wall_seconds'],
                      'tasks': [{
                          'task': row['task'], 'kernel': row['kernel_errors'],
                          'readout': row['readout'], 'features': row['features'],
                          'decoder': row['decoder']
                      } for row in rows]}, indent=2))


if __name__ == '__main__':
    main()
