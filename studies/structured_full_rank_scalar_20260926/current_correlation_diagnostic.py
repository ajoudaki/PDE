"""One precommitted saved-state diagnostic. No training, fitting or adaptation."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import signal
import time

for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import numpy as np

import circle_tasks
import dense_compare as dense

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
BASE = ROOT / 'data/generated/structured_full_rank_scalar_20260926'
REFERENCES = BASE / 'all_tasks_j2_20260927/references'
OUT = BASE / 'current_correlation_20260930/diagnostic'
TASKS = ('near_pair_sin9', 'cluster_triple_cos9', 'cluster_triple_cos1')
SOURCE_NAMES = (
    'CUBIC_DENSE_DIAGNOSTIC_20260930.md',
    'cubic_dense_diagnostic_20260930.py', 'dense_compare.py', 'circle_tasks.py',
    'CUBIC_REFERENCE_INVENTORY_20260930.md',
    'CURRENT_CORRELATION_DIAGNOSTIC_20260930.md',
    'current_correlation_diagnostic.py',
)


def rms(a):
    return float(np.sqrt(np.mean(np.asarray(a)**2)))


def ratio(a, b):
    return float(a / b) if b != 0 else None


def comparison(approx, exact):
    return {
        'absolute_frobenius_error': float(np.linalg.norm(approx-exact)),
        'relative_frobenius_error': ratio(np.linalg.norm(approx-exact), np.linalg.norm(exact)),
        'diagonal_absolute_error': np.abs(np.diag(approx-exact)).tolist(),
        'diagonal_relative_error': [ratio(abs(a-b), abs(b))
                                    for a, b in zip(np.diag(approx), np.diag(exact))],
    }


def matrix(a):
    if not np.all(np.isfinite(a)):
        raise ValueError('Nonfinite matrix')
    return {
        'matrix': a.tolist(), 'diagonal': np.diag(a).tolist(),
        'frobenius': float(np.linalg.norm(a)),
        'eigenvalues': np.linalg.eigvalsh((a+a.T)/2).tolist(),
    }


def check_deadline(deadline):
    if time.monotonic() >= deadline:
        raise TimeoutError('25-second numerical-work deadline reached')


def current_D(state, inputs):
    fields = dense._forward(state, inputs)
    weighted = dense._sech_squared(fields.z2) * state.c[:, None]
    return weighted.T @ weighted / state.width


def diagnose(task, initial, deadline):
    check_deadline(deadline)
    path = REFERENCES / (task+'__gaussian.npz')
    metadata_path = path.with_suffix('.json')
    raw = path.read_bytes()
    input_hash = hashlib.sha256(raw).hexdigest()
    metadata_raw = metadata_path.read_bytes()
    metadata = json.loads(metadata_raw)
    with np.load(path) as archive:
        saved = {key: archive[key] for key in archive.files}
    state = dense.State(saved['w'], saved['W'], saved['c'])
    inputs = circle_tasks.directions(saved['train_angles'])
    labels = saved['train_labels']
    if task in circle_tasks.BY_NAME:
        expected_inputs, expected_labels = circle_tasks.BY_NAME[task].data()
    else:
        # This fixed control is explicitly named by the assigned inventory.
        expected_inputs, _ = circle_tasks.BY_NAME['cluster_triple_cos9'].data()
        expected_labels = np.cos(saved['train_angles'])
    n, m = state.width, len(labels)
    if n != 1024 or any(a.dtype != np.float64 for a in (state.w, state.W, state.c)):
        raise ValueError('Expected float64 width-1024 saved state')
    fields = dense.forward(state, inputs)
    passive = dense.forward(state, circle_tasks.directions(saved['angles'])).output
    residual = fields.output-labels
    velocity = dense.rhs(state, inputs, labels)
    alpha = 2/m
    h1, h2 = fields.h1, fields.h2
    e = dense._sech_squared(fields.z1)
    d = dense._sech_squared(fields.z2)
    q = float(np.mean(state.c**2))
    K = h2.T @ h2/n
    H = h1.T @ h1/n
    G = d.T @ d/n
    mu = np.mean(d, axis=0)
    v2 = state.c[:, None]*d
    v1 = e*(state.W.T @ v2)
    D = v2.T @ v2/n
    naive = q*np.outer(mu, mu)
    independent = q*G
    first = (v1.T @ v1/n)*(inputs @ inputs.T)
    middle = D*H
    middle_naive = naive*H
    middle_independent = independent*H
    full = K+first+middle
    initial_fields = dense.forward(initial, inputs)
    K0 = initial_fields.h2.T @ initial_fields.h2/n
    eigenvalues, eigenvectors = np.linalg.eigh(K0)

    # Exact current derivative, split by which parameter block changes D.
    zdot_middle = velocity.W @ h1
    zdot_first = state.W @ (e*(velocity.w @ inputs.T))
    ddot_middle = -2*h2*d*zdot_middle
    ddot_first = -2*h2*d*zdot_first
    ddot = ddot_middle+ddot_first
    Ddot_readout = d.T @ ((2*state.c*velocity.c)[:, None]*d)/n

    def gate_derivative(dotgate):
        half = d.T @ (state.c[:, None]**2*dotgate)/n
        return half+half.T

    Ddot_middle = gate_derivative(ddot_middle)
    Ddot_first = gate_derivative(ddot_first)
    Ddot = Ddot_readout+Ddot_middle+Ddot_first
    qdot = float(2*np.mean(state.c*velocity.c))
    Gdot_half = d.T @ ddot/n
    Gdot = Gdot_half+Gdot_half.T
    mudot = np.mean(ddot, axis=0)
    independent_dot = qdot*G+q*Gdot
    naive_dot = qdot*np.outer(mu, mu)+q*(np.outer(mudot, mu)+np.outer(mu, mudot))
    output_dot = (velocity.c @ h2+state.c @ (d*(zdot_middle+zdot_first)))/n
    predicted_output_dot = -alpha*(full @ residual)
    epsilon = 1e-5/max(1, rms(velocity.w),
                       float(np.linalg.norm(velocity.W)/np.sqrt(n)), rms(velocity.c))
    check_deadline(deadline)
    plus = dense._add(state, velocity, epsilon)
    minus = dense._add(state, velocity, -epsilon)
    finite_difference = (current_D(plus, inputs)-current_D(minus, inputs))/(2*epsilon)

    matrices = {
        'initial_feature_gram': K0, 'K_second_feature': K, 'H_first_feature': H,
        'gate_joint_G': G, 'gate_covariance': G-np.outer(mu, mu),
        'D_exact': D, 'D_naive': naive, 'D_independent_readout': independent,
        'readout_gate_covariance': D-independent,
        'tangent_readout': K, 'tangent_first': first, 'tangent_middle': middle,
        'tangent_middle_naive': middle_naive,
        'tangent_middle_independent_readout': middle_independent,
        'tangent_full': full,
        'Ddot_exact': Ddot, 'Ddot_readout': Ddot_readout,
        'Ddot_middle_gate': Ddot_middle, 'Ddot_first_gate': Ddot_first,
        'Ddot_finite_difference': finite_difference,
        'Ddot_naive_with_exact_marginal_derivatives': naive_dot,
        'Ddot_independent_with_exact_marginal_derivatives': independent_dot,
    }
    directions = {'residual_unit': residual/np.linalg.norm(residual),
                  'residual_raw': residual, 'weak_initial_unit': eigenvectors[:, 0]}
    contractions = {}
    for name, direction in directions.items():
        vals = {key: float(direction @ value @ direction)
                for key, value in matrices.items()}
        for suffix, approx in (('naive', naive), ('independent_readout', independent)):
            error = float(direction @ (approx-D) @ direction)
            vals['D_'+suffix+'_signed_relative_error'] = ratio(error, abs(vals['D_exact']))
            vals['D_'+suffix+'_relative_error'] = ratio(abs(error), abs(vals['D_exact']))
            merr = float(direction @ ((approx-D)*H) @ direction)
            vals['middle_'+suffix+'_relative_error'] = ratio(abs(merr), abs(vals['tangent_middle']))
        vals['first_fraction_of_lower'] = ratio(vals['tangent_first'], vals['tangent_first']+vals['tangent_middle'])
        vals['first_fraction_of_full'] = ratio(vals['tangent_first'], vals['tangent_full'])
        contractions[name] = {'direction': direction.tolist(), **vals}

    mse = float(np.mean(residual**2))
    checks = {
        'npz_matches_metadata_hash': input_hash == metadata.get('data_sha256'),
        'task_inputs_match': bool(np.array_equal(inputs, expected_inputs)),
        'task_labels_match': bool(np.array_equal(labels, expected_labels)),
        'fixed_circle_grid_match': bool(np.array_equal(saved['angles'], 2*np.pi*np.arange(256)/256)),
        'train_prediction_max_abs': float(np.max(np.abs(fields.output-saved['train_prediction']))),
        'circle_prediction_max_abs': float(np.max(np.abs(passive-saved['prediction']))),
        'training_mse_abs_error': abs(mse-float(saved['history'][-1, 1])),
        'mean_gate_identity_max_abs': float(np.max(np.abs(mu-(1-np.diag(K))))),
        'full_tangent_rhs_relative_error': ratio(np.linalg.norm(output_dot-predicted_output_dot), np.linalg.norm(output_dot)),
        'Ddot_fd_relative_error': comparison(finite_difference, Ddot)['relative_frobenius_error'],
        'qdot_energy_identity_abs_error': abs(qdot+2*alpha*float(residual @ fields.output)),
    }
    gates = {
        'saved_replay': all(checks[k] for k in ('npz_matches_metadata_hash', 'task_inputs_match', 'task_labels_match', 'fixed_circle_grid_match'))
                        and checks['train_prediction_max_abs'] < 1e-10
                        and checks['circle_prediction_max_abs'] < 1e-10
                        and checks['training_mse_abs_error'] < 1e-12,
        'gate_identity': checks['mean_gate_identity_max_abs'] < 1e-12,
        'tangent_identity': checks['full_tangent_rhs_relative_error'] < 1e-10,
        'Ddot_derivative': checks['Ddot_fd_relative_error'] < 1e-6,
    }
    return {
        'task': task, 'width': n, 'time': float(saved['history'][-1, 0]),
        'training_mse': mse, 'labels': labels.tolist(), 'inputs': inputs.tolist(),
        'residual': residual.tolist(), 'q': q, 'qdot': qdot,
        'c2_coefficient_of_variation': float(np.std(state.c**2)/q),
        'c2_effective_fraction': float(q*q/np.mean(state.c**4)),
        'mean_gate': mu.tolist(), 'weak_initial_eigenvalue': float(eigenvalues[0]),
        'diagonal_first_fraction_of_lower': (np.diag(first)/np.diag(first+middle)).tolist(),
        'checks': checks, 'validity_gates': gates,
        'matrices': {key: matrix(value) for key, value in matrices.items()},
        'contractions': contractions,
        'errors': {
            'D_naive': comparison(naive, D),
            'D_independent_readout': comparison(independent, D),
            'middle_naive': comparison(middle_naive, middle),
            'middle_independent_readout': comparison(middle_independent, middle),
            'Ddot_naive_exact_marginals': comparison(naive_dot, Ddot),
            'Ddot_independent_exact_marginals': comparison(independent_dot, Ddot),
        },
        'derivative_epsilon': epsilon,
        'input_hashes': {
            str(path.relative_to(ROOT)): input_hash,
            str(metadata_path.relative_to(ROOT)): hashlib.sha256(metadata_raw).hexdigest(),
        },
    }


def main():
    started = time.monotonic()
    deadline = started+25
    OUT.mkdir(parents=True, exist_ok=False)
    snapshots = OUT/'source_snapshot'
    snapshots.mkdir()
    source_hashes = {}
    for name in SOURCE_NAMES:
        raw = (STUDY/name).read_bytes()
        (snapshots/name).write_bytes(raw)
        source_hashes[name] = hashlib.sha256(raw).hexdigest()
    output = {
        'status': 'running', 'budget_seconds': 30,
        'command': 'PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python studies/structured_full_rank_scalar_20260926/current_correlation_diagnostic.py',
        'source_sha256': source_hashes, 'tasks': [],
        'environment': {'numpy_version': np.__version__,
                        **{key: os.environ[key] for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')}},
    }

    def alarm(_signum, _frame):
        raise TimeoutError('28-second safety alarm')

    signal.signal(signal.SIGALRM, alarm)
    signal.alarm(28)
    try:
        initial = dense.initialize(1024, 1, 'gaussian')
        for task in TASKS:
            output['tasks'].append(diagnose(task, initial, deadline))
        output['status'] = 'complete'
    except Exception as exc:
        output['status'] = 'failed'
        output['error'] = repr(exc)
    finally:
        signal.alarm(0)
        output['wall_seconds'] = time.monotonic()-started
        (OUT/'diagnostic.json').write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
    print(json.dumps({
        'status': output['status'], 'wall_seconds': output['wall_seconds'],
        'tasks': [{key: row[key] for key in ('task', 'q', 'checks', 'validity_gates', 'errors')}
                  for row in output['tasks']],
        **({'error': output['error']} if 'error' in output else {}),
    }, indent=2))
    if output['status'] != 'complete':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
