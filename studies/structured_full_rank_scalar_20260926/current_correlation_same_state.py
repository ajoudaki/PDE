"""One same-state approximation pass; no training or candidate trajectory."""
from __future__ import annotations

import hashlib
import io
import json
import os
from pathlib import Path
import signal
import time

for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import numpy as np

import current_projected_correlation as route_a
import current_gaussian_correlation as route_b

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
BASE = ROOT/'data/generated/structured_full_rank_scalar_20260926'
ROUND = BASE/'current_correlation_20260930'
OUT = ROUND/'same_state'
TASKS = ('near_pair_sin9', 'cluster_triple_cos9', 'cluster_triple_cos1')
_B_LINK = None


def frozen_b_link(variance):
    global _B_LINK
    if _B_LINK is None:
        _B_LINK = route_b.RadialTanhLink(128)
    return _B_LINK.evaluate(variance)[0]


def rms(x):
    return float(np.sqrt(np.mean(np.asarray(x)**2)))


def comparison(approx, exact, directions):
    difference = approx-exact
    denominator = float(np.linalg.norm(exact))
    contractions = {}
    for name, v in directions.items():
        truth = float(v@exact@v)
        estimate = float(v@approx@v)
        contractions[name] = {
            'exact': truth, 'approximation': estimate,
            'signed_error': estimate-truth,
            'signed_relative_error': (estimate-truth)/abs(truth) if truth else None,
        }
    return {'exact': exact.tolist(), 'approximation': approx.tolist(),
            'signed_difference': difference.tolist(),
            'absolute_frobenius_error': float(np.linalg.norm(difference)),
            'relative_frobenius_error': float(np.linalg.norm(difference))/denominator if denominator else None,
            'contractions': contractions}


def main():
    started = time.monotonic()
    deadline = started+9.
    OUT.mkdir(parents=True, exist_ok=False)
    (OUT/'sources').mkdir()
    output = {'status': 'running', 'budget_seconds': 10,
              'scope': 'same saved dense states; no candidate fits or integration',
              'input_sha256': {}, 'source_sha256': {}, 'tasks': [],
              'environment': {'numpy': np.__version__,
                              **{key: os.environ[key] for key in
                                 ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')}}}

    def guard():
        if time.monotonic() >= deadline:
            raise TimeoutError('Nine-second numerical deadline')

    def snapshot(path):
        guard()
        raw = path.read_bytes()
        rel = path.relative_to(ROOT)
        output['input_sha256'][str(rel)] = hashlib.sha256(raw).hexdigest()
        destination = OUT/'input_snapshot'/rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(raw)
        return raw

    def archive(path):
        raw = snapshot(path)
        with np.load(io.BytesIO(raw), allow_pickle=False) as data:
            return {key: data[key] for key in data.files}

    def alarm(_signum, _frame):
        raise TimeoutError('9.5-second numerical safety alarm')

    signal.signal(signal.SIGALRM, alarm)
    signal.setitimer(signal.ITIMER_REAL, 9.5)
    try:
        source_names = (
            'CURRENT_CORRELATION_PROTOCOL_20260930.md',
            'CURRENT_CORRELATION_SAME_STATE_20260930.md',
            'current_correlation_same_state.py',
            'CURRENT_CORRELATION_ROUTE_A_20260930.md',
            'current_projected_correlation.py',
            'CURRENT_CORRELATION_ROUTE_B_20260930.md',
            'current_gaussian_correlation.py',
            'CURRENT_CORRELATION_DIAGNOSTIC_20260930.md',
            'current_correlation_diagnostic.py',
        )
        for name in source_names:
            raw = (STUDY/name).read_bytes()
            output['source_sha256'][name] = hashlib.sha256(raw).hexdigest()
            (OUT/'sources'/name).write_bytes(raw)
        diag_json = json.loads(snapshot(ROUND/'diagnostic/diagnostic.json'))
        prior = {row['task']: row for row in diag_json['tasks']}
        manifest = json.loads(snapshot(ROUND/'preflight_projected/manifest.json'))
        if manifest['sources']['current_projected_correlation.py'] != output['source_sha256']['current_projected_correlation.py']:
            raise ValueError('A source differs from constructor-only frozen source')
        if output['source_sha256']['current_gaussian_correlation.py'] != '7b37942a3b0a6eaae2d0e52ec4cd0e42e6d82fe08c0cdf17bff69f7965362b90':
            raise ValueError('B source differs from announced final freeze')
        for task in TASKS:
            guard()
            old = prior[task]
            if not all(old['validity_gates'].values()):
                raise ValueError('Assigned diagnostic had a failed validity gate')
            coeff = archive(ROUND/'preflight_projected'/f'{task}__projected__coefficients.npz')
            cubic = archive(BASE/'cubic_scalar_20260930'/f'{task}.npz')
            dense_path = BASE/'all_tasks_j2_20260927/references'/f'{task}__gaussian.npz'
            dense = archive(dense_path)
            dense_meta = json.loads(snapshot(dense_path.with_suffix('.json')))
            dense_hash = output['input_sha256'][str(dense_path.relative_to(ROOT))]
            if dense_meta.get('data_sha256') != dense_hash:
                raise ValueError('Saved dense metadata hash mismatch')
            for name in ('train_angles', 'angles'):
                if not np.array_equal(cubic[name], dense[name]):
                    raise ValueError('Assigned angle arrays disagree')
            if not np.array_equal(cubic['labels'], dense['train_labels']):
                raise ValueError('Assigned labels disagree')
            angles = np.r_[dense['train_angles'], dense['angles']]
            inputs = np.column_stack((np.cos(angles), np.sin(angles)))
            w, W, c = dense['w'], dense['W'], dense['c']
            if any(a.dtype != np.float64 for a in (w, W, c)) or len(c) != 1024:
                raise ValueError('Expected exact float64 width-1024 saved dense state')
            n, m = len(c), len(dense['train_labels'])
            h1 = np.tanh(w@inputs.T)
            z = W@h1
            h2 = np.tanh(z)
            exact_f = c@h2/n
            f = exact_f[:m]
            K = h2[:, :m].T@h2[:, :m]/n
            q = float(c@c/n)
            d = 1-h2[:, :m]**2
            exact_D = (c[:, None]*d).T@(c[:, None]*d)/n
            saved_K = np.asarray(old['matrices']['K_second_feature']['matrix'])
            saved_D = np.asarray(old['matrices']['D_exact']['matrix'])
            exact_lower = (np.asarray(old['matrices']['tangent_first']['matrix'])
                           +np.asarray(old['matrices']['tangent_middle']['matrix']))
            model = route_a.from_coefficients(coeff)
            state = model.initial_state()
            state[:m] = f-model.labels
            state[model.gram_slice] = K[model.triangle]
            state[model.q_index] = q
            _, _, _, _, _, GA, NA = model._fields(f-model.labels, K, q)
            lam = 2/(1-np.diag(coeff['initial_gram']))
            slack = 1-np.diag(K)
            direct_G = slack[:, None]*slack[None, :]*(q
                -(lam*f*f)[:, None]-(lam*f*f)[None, :]
                +(lam*f)[:, None]*(lam*f)[None, :]*K)
            b = c@z/n
            variance = np.mean(z*z, axis=0)
            gaussian_f = b*frozen_b_link(variance)
            difference = gaussian_f-exact_f
            if not all(np.all(np.isfinite(a)) for a in (K, exact_D, GA, NA, gaussian_f, difference)):
                raise ValueError('Nonfinite conditional-map output')
            checks = {
                'dense_train_replay': float(np.max(abs(f-dense['train_prediction']))),
                'dense_circle_replay': float(np.max(abs(exact_f[m:]-dense['prediction']))),
                'diagnostic_K_replay': float(np.max(abs(K-saved_K))),
                'diagnostic_f_replay': float(np.max(abs(f-(np.asarray(old['residual'])+np.asarray(old['labels']))))),
                'diagnostic_q_replay': abs(q-old['q']),
                'diagnostic_D_replay': float(np.max(abs(exact_D-saved_D))),
                'initial_gram_replay': float(np.max(abs(coeff['initial_gram']-cubic['initial_gram']))),
                'A_formula_replay': float(np.max(abs(GA-direct_G))),
            }
            gates = {key: value < (1e-12 if key in ('initial_gram_replay', 'A_formula_replay') else 1e-10)
                     for key, value in checks.items()}
            directions = {name: np.asarray(old['contractions'][name]['direction'])
                          for name in ('residual_unit', 'weak_initial_unit')}
            row = {'task': task, 'checks': checks, 'validity_gates': gates,
                   'A_gate': comparison(GA, saved_D, directions),
                   'A_lower': comparison(NA, exact_lower, directions),
                   'B_training_rms': rms(difference[:m]),
                   'B_circle_rms': rms(difference[m:]),
                   'B_circle_max_abs': float(np.max(abs(difference[m:]))),
                   'B_circle_mean_signed': float(np.mean(difference[m:])),
                   'B_circle_128_rms': rms(difference[m::2]),
                   'B_train_signed_error': difference[:m].tolist(),
                   'B_variance_range': [float(np.min(variance)), float(np.max(variance))],
                   'B_exact_readout_preactivation_moment': b.tolist(),
                   'B_exact_preactivation_second_moment': variance.tolist(),
                   'B_exact_output': exact_f.tolist(),
                   'B_gaussian_output': gaussian_f.tolist(),
                   'B_signed_error': difference.tolist()}
            np.savez(OUT/f'{task}__same_state.npz', K=K, f=f, q=q,
                     beta=coeff['beta'], K0=coeff['initial_gram'],
                     A_gate=GA, exact_gate=saved_D, A_lower=NA, exact_lower=exact_lower,
                     B_b=b, B_variance=variance, B_output=gaussian_f,
                     exact_output=exact_f, B_signed_error=difference, angles=angles)
            output['tasks'].append(row)
            if not all(gates.values()):
                raise ValueError('Same-state validity gate failed')
        guard()
        output['status'] = 'complete'
    except Exception as exc:
        output['status'] = 'failed'
        output['error'] = repr(exc)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        output['wall_seconds'] = time.monotonic()-started
        (OUT/'same_state.json').write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'status': output['status'], 'wall_seconds': output['wall_seconds'],
                      'tasks': [{key: row[key] for key in ('task', 'B_training_rms', 'B_circle_rms')}
                                |{'A_gate_relative_error': row['A_gate']['relative_frobenius_error'],
                                  'A_lower_relative_error': row['A_lower']['relative_frobenius_error']}
                                for row in output['tasks']],
                      **({'error': output['error']} if 'error' in output else {})}, indent=2))
    if output['status'] != 'complete':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
