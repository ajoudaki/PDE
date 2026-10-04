"""Replay only frozen candidate artifacts; never integrates or trains a model."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'

import numpy as np

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
DATA = ROOT/'data/generated/structured_full_rank_scalar_20260926'
BASE = DATA/'current_correlation_20260930'
FOCUS = ('near_pair_sin9', 'cluster_triple_cos9', 'cluster_triple_cos1')
FREEZE = {
    'current_projected_correlation.py': 'cd7ead9070a2ecce2f9728143666f79381a146fb7ec968656c89673a1a22d2e1',
    'CURRENT_CORRELATION_ROUTE_A_20260930.md': 'a6ae2b5b876c13f116c0e4eef8142cb86a1d8ae9a4e766b4c8f4be75c7c6fc21',
    'current_gaussian_correlation.py': '7b37942a3b0a6eaae2d0e52ec4cd0e42e6d82fe08c0cdf17bff69f7965362b90',
    'CURRENT_CORRELATION_ROUTE_B_20260930.md': '4d696ab574d3dea3ed42a80403105d3bd8afa0347a1b0a6c5aff50675498f205',
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_npz(path):
    with np.load(path) as file:
        return {key: file[key] for key in file.files}


def maxabs(x):
    return float(np.max(np.abs(x))) if np.size(x) else 0.


def load_model_source(path):
    name = 'audit_frozen_'+path.stem+'_'+sha(path)[:12]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def audit_row(campaign, row):
    task, method = row['task'], row['method']
    if task not in FOCUS:
        raise ValueError('Audit scope does not permit dataset expansion')
    module_name = {'projected': 'current_projected_correlation.py',
                   'gaussian': 'current_gaussian_correlation.py'}[method]
    source = campaign/'sources'/module_name
    if module_name not in FREEZE or sha(source) != FREEZE[module_name]:
        raise ValueError('Candidate source is absent from the authorized freeze')
    module = load_model_source(source)
    stem = task+'__'+method
    data_path = campaign/(stem+'.npz')
    coefficient_path = campaign/(stem+'__coefficients.npz')
    payload = load_npz(data_path)
    coefficients = load_npz(coefficient_path)
    model = module.from_coefficients(coefficients)
    state, history = payload['state'], payload['history']
    residual = model.residual(state)
    pred = model.predict(state)
    labels = payload['labels']
    f = labels+residual
    alpha = 2/len(labels)
    velocity = model.rhs(0., state)
    energy = model.readout_energy if method == 'projected' else lambda at: model.moments(at)[0]
    q = energy(state)
    epsilon = 1e-6/max(1., maxabs(velocity))
    plus, minus = state+epsilon*velocity, state-epsilon*velocity
    residual_dot_fd = (model.residual(plus)-model.residual(minus))/(2*epsilon)
    energy_dot_fd = (energy(plus)-energy(minus))/(2*epsilon)
    checks = {
        'data_hash_matches': sha(data_path) == row['data_sha256'],
        'coefficient_hash_matches': sha(coefficient_path) == row['coefficient_sha256'],
        'prediction_replay_max_abs': maxabs(pred-payload['prediction']),
        'training_mse_replay_abs_error': abs(float(np.mean(residual**2))-row['train_mse']),
        'energy_derivative_abs_error': abs(float(energy_dot_fd)+2*alpha*float(residual@f)),
        'readout_energy': float(q),
        'max_tanh_energy_excess': float(np.max(pred**2-q)) if pred.size else None,
        'finite_state_and_prediction': bool(np.all(np.isfinite(state)) and np.all(np.isfinite(pred))),
        'training_size_matches': model.training_size == row['training_states'],
        'total_size_matches': model.size == row['total_states'],
        'coefficient_bytes_match': sum(v.nbytes for v in coefficients.values()) == row['coefficient_bytes'],
        'numeric_coefficient_scalars': sum(v.size for v in coefficients.values() if v.dtype.kind in 'biufc'),
        'numeric_coefficient_bytes': sum(v.nbytes for v in coefficients.values() if v.dtype.kind in 'biufc'),
        'metadata_array_bytes': sum(v.nbytes for v in coefficients.values() if v.dtype.kind not in 'biufc'),
        'dynamic_state_bytes': state.nbytes,
        'nested_scalar_link_bytes': (model.link.nodes.nbytes+model.link.weights.nbytes) if method == 'gaussian' else 0,
    }
    canonical_path = DATA/'all_tasks_j2_20260927/references'/(task+'__gaussian.npz')
    canonical = load_npz(canonical_path)
    checks['canonical_dense_copy_max_abs'] = maxabs(payload['dense']-canonical['prediction'])
    hashes = {str(path.relative_to(ROOT)): sha(path)
              for path in (data_path, coefficient_path, canonical_path)}
    checks['recorded_input_hashes_match'] = all(sha(Path(path)) == digest for path, digest in row['input_sha256'].items())
    upstream_coefficients = [Path(p) for p in row['input_sha256'] if p.endswith('__coefficients.npz')]
    if upstream_coefficients:
        upstream = load_npz(upstream_coefficients[0])
        checks['upstream_coefficients_all_arrays_exact'] = all(np.array_equal(value, upstream[key]) for key, value in coefficients.items())
        checks['upstream_numeric_coefficients_exact'] = all(np.array_equal(value, upstream[key]) for key, value in coefficients.items() if value.dtype.kind in 'biufc')
    selected = payload['selected']
    checks['alias_max_abs'] = maxabs(pred[256+selected]-f) if len(pred) else None
    if history.size:
        checks['history_last_mse_abs_error'] = abs(float(history[-1, 1])-float(np.mean(residual**2)))
        checks['history_max_loss_increase'] = max(0., float(np.max(np.diff(history[:, 1])))) if len(history)>1 else 0.
        checks['fitted_mse_error'] = abs(float(np.mean(residual**2))-.001) if row['fitted'] else None
    if 'circle_rms' in row:
        diff = pred[:256]-canonical['prediction']
        circle = float(np.sqrt(np.mean(diff**2)))
        nested = abs(circle-float(np.sqrt(np.mean(diff[::2]**2))))
        checks.update(circle_rms=circle, circle_metric_abs_error=abs(circle-row['circle_rms']),
                      nested_rms_change=nested, nested_metric_abs_error=abs(nested-row['nested_rms_change']))
    if method == 'projected':
        r, K, _, passive = model.unpack(state)
        _, _, _, _, _, G, N = model._fields(r, K, q)
        tangent = K+N
        checks['loss_derivative_abs_error'] = abs(float(2/len(r)*r@residual_dot_fd)+4/len(r)**2*float(r@tangent@r))
        augmented = np.block([[K, f[:, None]], [f[None, :], np.array([[q]])]])
        mins = [float(np.linalg.eigvalsh(augmented)[0])]
        for p in passive:
            cross = np.r_[p[:model.m], p[model.m]]
            aug = np.block([[augmented, cross[:, None]], [cross[None, :], np.array([[p[model.m+1]]])]])
            mins.append(float(np.linalg.eigvalsh(aug)[0]))
        changed = state.copy()
        changed[model.training_size:] *= .37
        checks['query_independence_training_rhs_max_abs'] = maxabs(model.rhs(0., changed)[:model.training_size]-velocity[:model.training_size])
        checks['min_augmented_eigenvalue'] = min(mins)
        checks['min_tangent_eigenvalue'] = float(np.linalg.eigvalsh(tangent)[0])
        checks['max_query_cauchy_schwarz_excess'] = float(np.max(pred**2-q*passive[:, model.m+1])) if len(pred) else None
        checks['max_physical_gate_excess'] = float(np.max(np.diag(G)-q))
        equilibrium = state.copy()
        equilibrium[:model.m] = 0.
        checks['zero_residual_rhs_max_abs'] = maxabs(model.rhs(0., equilibrium))
    else:
        q, u, V = model.moments(state)
        uq, vq, Vq = model.query_moments(state)
        tangent = model.tangent_kernel(state)
        covariance = np.block([[np.array([[q]]), u[None, :]], [u[:, None], V]])
        mins = [float(np.linalg.eigvalsh(covariance)[0])]
        for j in range(model.nquery):
            cross = np.r_[uq[j], Vq[j]]
            aug = np.block([[covariance, cross[:, None]], [cross[None, :], np.array([[vq[j]]])]])
            mins.append(float(np.linalg.eigvalsh(aug)[0]))
        empty_coefficients = dict(coefficients)
        empty_coefficients['query_A'] = np.empty((0, model.m))
        empty_coefficients['query_V0'] = np.empty((0, model.m))
        empty_coefficients['query_var0'] = np.empty(0)
        empty = module.from_coefficients(empty_coefficients)
        checks['query_independence_training_rhs_max_abs'] = maxabs(empty.rhs(0., state)-velocity)
        checks['query_independence_bitwise'] = bool(np.array_equal(empty.rhs(0., state), velocity))
        checks['query_free_state_and_blocks_equal'] = bool(np.array_equal(empty.initial_state(), model.initial_state()) and empty.blocks == model.blocks)
        checks['loss_derivative_abs_error'] = abs(float(2/len(residual)*residual@residual_dot_fd)+4/len(residual)**2*float(residual@tangent@residual))
        checks['min_augmented_eigenvalue'] = min(mins)
        checks['min_tangent_eigenvalue'] = float(np.linalg.eigvalsh(tangent)[0])
        checks['max_query_covariance_cauchy_schwarz_excess'] = float(np.max(uq*uq-q*vq)) if len(pred) else None
        checks['exact_energy_derivative_abs_error'] = abs(model.moment_derivatives(state)[0]+2*alpha*float(residual@f))
        exact_s, exact_t = model.link.evaluate(np.r_[np.diag(V), vq])
        fine_s, fine_t = module.RadialTanhLink(256).evaluate(np.r_[np.diag(V), vq])
        checks['quadrature_refinement_s_maxabs'] = maxabs(exact_s-fine_s)
        checks['quadrature_refinement_t_maxabs'] = maxabs(exact_t-fine_t)
        checks['max_variance'] = float(max(np.max(np.diag(V)), np.max(vq)))
        model.labels = f.copy()
        checks['zero_residual_rhs_max_abs'] = maxabs(model.rhs(0., state))
    return {'task': task, 'method': method, 'fitted': row['fitted'],
            'stop_reason': row['stop_reason'], 'checks': checks,
            'hashes': hashes, 'epsilon': epsilon}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign')
    parser.add_argument('--summarize', action='store_true')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    if args.summarize:
        if args.campaign is not None or '/' in args.output:
            raise ValueError('Summary takes only an output basename')
        summarize(args.output)
        return
    if args.campaign is None:
        raise ValueError('An explicit frozen campaign is required')
    if '/' in args.campaign or '/' in args.output:
        raise ValueError('Use one explicit campaign and output basename')
    campaign = BASE/args.campaign
    destination = BASE/'audit'/args.output
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise FileExistsError(destination)
    started = time.monotonic()
    manifest = json.loads((campaign/'manifest.json').read_text())
    summary = json.loads((campaign/'summary.json').read_text())
    source_checks = {}
    for name, recorded in manifest['sources'].items():
        actual = sha(campaign/'sources'/name)
        source_checks[name] = {'actual_sha256': actual, 'manifest_matches': actual == recorded,
                              'authorized_freeze_matches': actual == FREEZE[name] if name in FREEZE else None}
    if not all(item['manifest_matches'] for item in source_checks.values()):
        raise ValueError('Source snapshot manifest mismatch')
    result = {'campaign': args.campaign, 'scope': 'saved-state replay and instantaneous identities; no integration',
              'source_checks': source_checks,
              'manifest_sha256': sha(campaign/'manifest.json'),
              'summary_sha256': sha(campaign/'summary.json'),
              'audit_source_sha256': sha(Path(__file__)),
              'records': [audit_row(campaign, row) for row in summary['results']]}
    result['wall_seconds'] = time.monotonic()-started
    destination.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'campaign': args.campaign, 'wall_seconds': result['wall_seconds'],
                      'records': [{'task': row['task'], 'method': row['method'],
                                   'checks': {key: value for key, value in row['checks'].items()
                                              if key in ('circle_rms', 'prediction_replay_max_abs',
                                                         'energy_derivative_abs_error', 'loss_derivative_abs_error',
                                                         'min_augmented_eigenvalue', 'alias_max_abs',
                                                         'upstream_numeric_coefficients_exact',
                                                         'query_independence_bitwise')}}
                                  for row in result['records']]}, indent=2, allow_nan=False))


def summarize(output_name):
    destination = BASE/'audit'/output_name
    if destination.exists():
        raise FileExistsError(destination)
    campaigns = ('focus_projected', 'focus_gaussian', 'refinement_projected', 'refinement_gaussian')
    saved_rows, audited, manifests = [], [], {}
    for name in campaigns:
        saved = json.loads((BASE/name/'summary.json').read_text())
        audit = json.loads((BASE/'audit'/(name+'.json')).read_text())
        manifests[name] = json.loads((BASE/name/'manifest.json').read_text())
        saved_rows.extend(saved['results'])
        audited.extend(audit['records'])
    refinements = {}
    for method in ('projected', 'gaussian'):
        stem = 'near_pair_sin9__'+method
        primary = load_npz(BASE/('focus_'+method)/(stem+'.npz'))
        fine = load_npz(BASE/('refinement_'+method)/(stem+'.npz'))
        diff = primary['prediction'][:256]-fine['prediction'][:256]
        pcoef = load_npz(BASE/('focus_'+method)/(stem+'__coefficients.npz'))
        fcoef = load_npz(BASE/('refinement_'+method)/(stem+'__coefficients.npz'))
        refinements[method] = {
            'circle_prediction_rms_change': float(np.sqrt(np.mean(diff*diff))),
            'circle_prediction_max_abs_change': maxabs(diff),
            'all_coefficient_arrays_exact': all(np.array_equal(value, fcoef[key]) for key, value in pcoef.items()),
        }
    required_true = ('data_hash_matches', 'coefficient_hash_matches', 'finite_state_and_prediction',
                     'training_size_matches', 'total_size_matches', 'coefficient_bytes_match',
                     'recorded_input_hashes_match', 'upstream_numeric_coefficients_exact')
    checks = {
        'all_required_boolean_checks_pass': all(all(row['checks'][key] for key in required_true) for row in audited),
        'prediction_replay_max_abs': max(row['checks']['prediction_replay_max_abs'] for row in audited),
        'canonical_dense_copy_max_abs': max(row['checks']['canonical_dense_copy_max_abs'] for row in audited),
        'circle_metric_replay_max_abs': max(row['checks']['circle_metric_abs_error'] for row in audited),
        'training_mse_replay_max_abs': max(row['checks']['training_mse_replay_abs_error'] for row in audited),
        'fitted_mse_error_max': max(row['checks']['fitted_mse_error'] for row in audited),
        'alias_max_abs': max(row['checks']['alias_max_abs'] for row in audited),
        'min_augmented_eigenvalue': min(row['checks']['min_augmented_eigenvalue'] for row in audited),
        'min_tangent_eigenvalue': min(row['checks']['min_tangent_eigenvalue'] for row in audited),
        'history_max_loss_increase': max(row['checks']['history_max_loss_increase'] for row in audited),
        'nested_panel_max_change': max(row['checks']['nested_rms_change'] for row in audited),
        'max_tanh_energy_excess': max(row['checks']['max_tanh_energy_excess'] for row in audited),
        'zero_residual_rhs_max_abs': max(row['checks']['zero_residual_rhs_max_abs'] for row in audited),
        'query_independence_rhs_max_abs': max(row['checks']['query_independence_training_rhs_max_abs'] for row in audited),
        'loss_derivative_fd_max_abs_error': max(row['checks']['loss_derivative_abs_error'] for row in audited),
    }
    frozen_sources = {name: manifest['sources'] for name, manifest in manifests.items()}
    result = {
        'status': 'saved-result replay and declared invariant gates pass; both accuracy witnesses fail',
        'fits_audited': len(saved_rows),
        'primary_fits': sum(len(json.loads((BASE/name/'summary.json').read_text())['results']) for name in campaigns[:2]),
        'refinement_fits': 2,
        'sum_recorded_training_seconds': sum(row['training_seconds'] for row in saved_rows),
        'max_recorded_training_seconds': max(row['training_seconds'] for row in saved_rows),
        'all_fitted': all(row['fitted'] for row in saved_rows),
        'all_recorded_stops_target': all(row['stop_reason'] == 'target' for row in saved_rows),
        'checks': checks, 'near_pair_refinements': refinements,
        'manifest_source_hashes': frozen_sources,
        'settings': {name: manifest['settings'] for name, manifest in manifests.items()},
        'audit_source_sha256': sha(Path(__file__)),
        'input_audit_hashes': {name+'.json': sha(BASE/'audit'/(name+'.json')) for name in campaigns},
        'limitations': ['No cluster tolerance replication; accuracy branch not triggered.',
                        'A query-free fit not performed; its RHS independence is exact but adaptive steps can depend on query errors.',
                        'Endpoint comparisons use each method own MSE crossing.',
                        'One optional energy central difference loses absolute accuracy on B hard cluster; exact energy identity error is 7.78e-16.'],
    }
    destination.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key: result[key] for key in ('status', 'fits_audited', 'sum_recorded_training_seconds', 'checks', 'near_pair_refinements')}, indent=2))


if __name__ == '__main__':
    main()
