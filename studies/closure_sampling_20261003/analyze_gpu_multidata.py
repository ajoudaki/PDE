"""Recompute multi-dataset GPU errors and conservative protocol decisions.

Reads arrays only: no sampler, torch, dense evolution, or scientific training.
Run with --inputs ROOT... --output FRESH_DIR. Optional --expected-config files
make missing cases visible even when a worker did not start. Baseline decisions
always require both prescribed seeds at all three widths.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
from pathlib import Path
import sys

import numpy as np


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def metrics(predictions):
    error = predictions - predictions[:, :1, :]
    return dict(rms_time_sup=np.sqrt(np.mean(np.max(np.abs(error), axis=0)**2, axis=1)),
                max_time_rms=np.sqrt(np.mean(error**2, axis=2)).max(axis=0),
                endpoint_rms=np.sqrt(np.mean(error[-1]**2, axis=1)),
                sup_panel_time=np.max(np.abs(error), axis=(0, 2)))


def metric_oracle():
    prediction = np.zeros((2, 2, 2))
    prediction[0, 1, 0] = prediction[1, 1, 1] = 1.
    result = metrics(prediction)
    assert result['rms_time_sup'][1] == 1.
    assert np.isclose(result['max_time_rms'][1], 1/np.sqrt(2))
    assert np.isclose(result['endpoint_rms'][1], 1/np.sqrt(2))
    return {key: float(value[1]) for key, value in result.items()}


def write_csv(path, rows):
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with Path(path).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows({key: json.dumps(value, separators=(',', ':'))
                         if isinstance(value, (dict, list, tuple)) else value
                         for key, value in row.items()} for row in rows)


def case_key(record):
    return (record['dataset_id'], int(record['n']), int(record['seed']))


def total_state(width, d, m):
    return width**2+(d+3)*width+m*(d+1)


def load_case(folder):
    folder = Path(folder)
    record = read_json(folder/'record.json')
    for filename in ('observations.npz', 'reduced_restart.npz'):
        if record.get(filename+'_sha256') != digest(folder/filename):
            raise ValueError('Missing or mismatched archive hash: '+str(folder/filename))
    with np.load(folder/'observations.npz', allow_pickle=False) as archive:
        data = {key: archive[key] for key in archive.files}
    for key in ('times', 'panel', 'predictions', 'training_predictions',
                'labels', 'U', 'residual_rms', 'feature_motion'):
        if key not in data or not np.isfinite(data[key]).all():
            raise ValueError('Missing/nonfinite '+key+' at '+str(folder))
    t, p, U = data['times'], data['predictions'], data['U']
    if t.ndim != 1 or t[0] != 0 or np.any(np.diff(t) <= 0):
        raise ValueError('Invalid observation time axis')
    if p.shape != (len(t), len(record['model_names']), len(data['panel'])):
        raise ValueError('Prediction axis mismatch')
    if U.ndim != 2 or data['panel'].shape[1] != U.shape[1]:
        raise ValueError('Input/query dimension mismatch')
    if data['training_predictions'].shape != (len(t), len(record['model_names']), len(U)):
        raise ValueError('Training prediction axis mismatch')
    residual = np.sqrt(np.mean((data['training_predictions']-data['labels'])**2, axis=2))
    np.testing.assert_allclose(residual, data['residual_rms'], atol=1e-12, rtol=1e-10)
    for directions in (U, data['panel']):
        np.testing.assert_allclose(np.linalg.norm(directions, axis=1), 1., atol=1e-10, rtol=0)
    value = metrics(p)
    stored_keys = {'rms_time_sup': 'rms_of_time_sup', 'max_time_rms': 'sup_of_time_rms',
                   'endpoint_rms': 'endpoint_rms', 'sup_panel_time': 'sup_panel_time'}
    for key, stored in stored_keys.items():
        np.testing.assert_allclose(value[key], [item[stored] for item in record['metrics']],
                                   atol=1e-14, rtol=1e-12)
    return record, data


def core_gate(root):
    path = root/'core_validation.json'
    if not path.exists():
        return False, {'missing': str(path)}
    check = read_json(path)
    dynamics = check.get('dynamics', check)
    required = ('rhs_public', 'heun_public', 'uniform_weighted_rhs',
                'uniform_weighted_heun', 'weighted_autograd', 'restart')
    if all(key in dynamics for key in required):
        valid = all(np.isfinite(dynamics[key]) and abs(dynamics[key]) < 2e-12 for key in required)
    else:
        required_dimensions = ('d2_m2', 'd3_m4', 'd5_m8')
        required_fields = ('rhs_public', 'heun_public', 'uniform_weighted_rhs', 'weighted_autograd')
        valid = all(name in dynamics and all(key in dynamics[name] and
            np.isfinite(dynamics[name][key]) and abs(dynamics[name][key]) < 2e-12
            for key in required_fields) for name in required_dimensions)
    valid = valid and all(check.get('metrics', {}).get(key) is True for key in
                          ('noncommuting_metric_oracle', 'root_scaling', 'zero_baseline'))
    return bool(valid), check


def source_diagnostics(diag):
    result = {}
    for layer in (1, 2):
        info = diag[f'basis{layer}']
        result[f'priority_rank{layer}'] = int(info['priority_rank'])
        result[f'retained_rank{layer}'] = int(info['retained_rank'])
        result[f'residual_source_modes{layer}'] = int(info['retained_rank']-info['priority_rank'])
        result[f'priority_exhausts_rank{layer}'] = info['priority_rank'] >= info['requested_rank']
        result[f'discarded_priority{layer}'] = int(info['discarded_priority_directions'])
        result[f'discarded_source_modes{layer}'] = int(info['discarded_resolved_directions'])
        result[f'priority_singular_values{layer}'] = info['priority_singular_values']
        result[f'cubature_gram{layer}'] = float(diag[f'cubature{layer}']['gram_operator_error'])
        for name, error in info['source_residuals'].items():
            result[f'source{layer}_{name}'] = float(error['relative_frobenius'])
    for name in ('forward_initial', 'reverse_initial_jet', 'forward_second_jet',
                 'feature_initial', 'own_first_feature_second_jet', 'own_second_feature_second_jet'):
        result[name] = float(diag[name]['mean_weighted_rms'])
    for name in ('dense_initial_gram_gap', 'compressed_initial_gram_gap', 'training_gram_frobenius_error'):
        result[name] = float(diag[name])
    result['initial_dense_gram_eigenvalues'] = np.linalg.eigvalsh(diag['dense_initial_training_gram']).tolist()
    result['initial_reduced_gram_eigenvalues'] = np.linalg.eigvalsh(diag['compressed_initial_training_gram']).tolist()
    return result


def extract(roots, expected_configs):
    rows, controls, cases, failures, provenance, configs = [], [], [], [], [], []
    seen = set()
    datasets = {}
    for path in expected_configs:
        cfg = read_json(path)
        configs.append(cfg)
        datasets.update(cfg['datasets'])
    for root in map(Path, roots):
        config = read_json(root/'config.resolved.json')
        configs.append(config)
        for name, value in config['datasets'].items():
            if name in datasets:
                # Refinement query panels may change; training data may not.
                for key in ('U', 'labels'):
                    if datasets[name][key] != value[key]:
                        raise ValueError('Dataset changed between input roots: '+name)
            datasets[name] = value
        stage = config['stage']
        core_ok, core = core_gate(root)
        status = read_json(root/'status.json') if (root/'status.json').exists() else {}
        for failure in status.get('failures', []):
            failures.append(dict(root=str(root), stage=stage, **failure))
        provenance.append(dict(root=str(root), stage=stage, core_pass=core_ok,
            core_checks=core, status=status,
            hashes={name: digest(root/name) for name in ('config.resolved.json', 'provenance.json',
                'core_validation.json', 'status.json') if (root/name).exists()}))
        for failure_path in sorted(root.glob('*/setup_failures.json')):
            case_config = read_json(failure_path.parent/'case_config.json')['case']
            for failure in read_json(failure_path):
                failures.append(dict(root=str(root), stage=stage, **case_config,
                                     kind='construction', **failure))
        for record_path in sorted(root.glob('*/record.json')):
            record, data = load_case(record_path.parent)
            dataset = datasets[record['dataset_id']]
            d, m = data['U'].shape[1], len(data['U'])
            value = metrics(data['predictions'])
            initial_times = data['times'] <= 120+1e-9
            common = metrics(data['predictions'][initial_times])
            common_complete = bool(np.isclose(data['times'][initial_times][-1], 120., atol=1e-8))
            tail_times = data['times'] >= data['times'][-1]-10-1e-9
            tail = np.max(np.abs(data['predictions'][tail_times]-data['predictions'][-1]), axis=(0, 2))
            residual = data['residual_rms'][-1]
            settled = (residual <= 1e-6) & (tail <= 1e-5) & (data['times'][-1] >= 10)
            base = dict(stage=stage, dataset_id=record['dataset_id'],
                group=dataset.get('metadata', {}).get('group', record['dataset_id']), d=d, m=m,
                n=int(record['n']), seed=int(record['seed']), case_path=str(record_path.parent),
                last_time=float(data['times'][-1]), dt=float(record['dt']))
            root_n = math.sqrt(record['n'])
            for j, name in enumerate(record['model_names']):
                if j not in (0, 1) and name != 'frozen_dense_hidden':
                    continue
                controls.append(dict(base, model=name,
                    **{key: float(v[j]) for key, v in value.items()},
                    scaled_rms=root_n*float(value['rms_time_sup'][j]),
                    common120_scaled_rms=root_n*float(common['rms_time_sup'][j]),
                    fit_rms=float(residual[j]), tail_change=float(tail[j]), settled=bool(settled[j]),
                    feature1=float(data['feature_motion'][-1, j, 0]),
                    feature2=float(data['feature_motion'][-1, j, 1])))
            for pos, spec in enumerate(record['schedule']):
                j = int(spec.get('model_index', pos+2))
                N, rank = int(spec['width']), int(spec['rank'])
                factor = float(spec.get('coefficient_multiplier', spec.get('multiplier', 1)))
                count = total_state(N, d, m)
                if count != spec['total']:
                    raise ValueError('Incorrect retained state count at '+str(record_path))
                budget = float(spec.get('budget', factor*2550*(math.log(record['n'])/math.log(512))**4))
                if count > budget+1e-8 or total_state(N+1, d, m) <= budget-1e-8:
                    raise ValueError('Selected width not maximal in declared budget')
                identity = (stage, case_key(record), factor, rank)
                if identity in seen:
                    raise ValueError('Duplicate comparison: '+str(identity))
                seen.add(identity)
                diag = record['sampler_diagnostics'][pos]
                final_ok = all(diag[layer]['fits'][-1]['success'] for layer in ('cubature1', 'cubature2'))
                discarded = sum(diag[layer]['discarded_directions'] for layer in ('frame1', 'frame2'))
                construction_ok = bool(final_ok and discarded == 0)
                trajectory_ok = bool(core_ok and construction_ok)
                endpoint_ok = bool(trajectory_ok and np.all(settled[[0, 1, j]]))
                primary, dense = float(value['rms_time_sup'][j]), float(value['rms_time_sup'][1])
                rows.append(dict(base, model=record['model_names'][j], factor=factor, rank=rank, N=N,
                    P=count, moving=N*N+(d+1)*N, fixed=2*N+m*(d+1), budget=budget,
                    **{key: float(v[j]) for key, v in value.items()}, scaled_rms=root_n*primary,
                    scaled_endpoint_rms=root_n*float(value['endpoint_rms'][j]),
                    common120_rms=float(common['rms_time_sup'][j]),
                    common120_scaled_rms=root_n*float(common['rms_time_sup'][j]),
                    common120_complete=common_complete, dense_rms=dense, dense_scaled_rms=root_n*dense,
                    ratio_to_dense_copy=primary/dense if dense else None,
                    fit_rms=float(residual[j]), tail_change=float(tail[j]), settled=bool(settled[j]),
                    dense_reference_settled=bool(settled[0]), dense_copy_settled=bool(settled[1]),
                    dense_reference_fit=float(residual[0]), dense_copy_fit=float(residual[1]),
                    core_pass=core_ok, construction_pass=construction_ok, final_optimizer_pass=bool(final_ok),
                    frame_discarded_directions=int(discarded), trajectory_valid=trajectory_ok,
                    settled_valid=endpoint_ok, ceiling_pass=root_n*primary <= .15,
                    intermediate_optimizer_warnings=sum(not fit['success'] for layer in ('cubature1', 'cubature2')
                                                       for fit in diag[layer]['fits'][:-1]),
                    feature1=float(data['feature_motion'][-1, j, 0]),
                    feature2=float(data['feature_motion'][-1, j, 1]), **source_diagnostics(diag)))
            cases.append(dict(base, model_names=record['model_names'], settled=settled.tolist(),
                core_pass=core_ok, record_sha256=digest(record_path),
                observations_sha256=record['observations.npz_sha256'],
                initial_gram_eigenvalues=record.get('initial_gram_eigenvalues')))
    return rows, controls, cases, failures, provenance, configs, datasets


def ratio(a, b):
    if b == 0:
        return 1. if a == 0 else None
    return float(a/b)


def dataset_decisions(rows, failures, configs, datasets):
    identities = {(r['stage'], r['dataset_id'], r['factor'], r['rank']) for r in rows}
    expected = {}
    for cfg in configs:
        for case in cfg['cases']:
            for spec in cfg['samplers']:
                factor = float(spec.get('coefficient_multiplier', spec.get('multiplier', 1)))
                key = (cfg['stage'], case['dataset_id'], factor, int(spec['rank']))
                identities.add(key)
                expected.setdefault(key, set()).add((case['n'], case['seed']))
    decisions = []
    for key in sorted(identities):
        stage, name, factor, rank = key
        selected = [r for r in rows if (r['stage'], r['dataset_id'], r['factor'], r['rank']) == key]
        desired = expected.get(key, set())
        if stage == 'baseline':
            desired = {(n, s) for n in (512, 1024, 2048) for s in (9411, 9412)}
        actual = {(r['n'], r['seed']) for r in selected}
        complete = bool(desired and actual == desired and len(selected) == len(desired))
        failures_for_task = [f for f in failures if f.get('stage') == stage and f.get('dataset_id') == name
            and ('sampler' not in f or (float(f['sampler'].get('coefficient_multiplier', 1)),
                                       int(f['sampler']['rank'])) == (factor, rank))]
        invalid = any(not r['construction_pass'] for r in selected)
        construction_failure = any(f.get('kind') == 'construction' or
                                   'setup' in str(f.get('error', '')).lower() or
                                   'cubature' in str(f.get('error', '')).lower() or
                                   'positive' in str(f.get('error', '')).lower() or
                                   'rank' in str(f.get('error', '')).lower() for f in failures_for_task)
        low = [r for r in selected if r['n'] == 512]
        high = [r for r in selected if r['n'] == 2048]
        comparable = bool(low and high and {r['seed'] for r in low} == {r['seed'] for r in high})
        growth = ratio(np.median([r['scaled_rms'] for r in high]),
                       np.median([r['scaled_rms'] for r in low])) if comparable else None
        common_growth = ratio(np.median([r['common120_scaled_rms'] for r in high]),
                              np.median([r['common120_scaled_rms'] for r in low])) if comparable else None
        ceiling_ok = bool(selected and all(r['ceiling_pass'] for r in selected))
        settled_ok = bool(selected and all(r['settled_valid'] for r in selected))
        growth_required = stage in ('baseline', 'confirmation')
        growth_ok = bool(growth is not None and growth <= 1.5) if growth_required else True
        performance = bool(complete and ceiling_ok and settled_ok and growth_ok)
        trigger = bool(stage == 'baseline' and (invalid or construction_failure or
            any(not r['ceiling_pass'] for r in selected) or (growth is not None and growth > 1.5)))
        status = ('incomplete' if not complete else 'construction_invalid' if invalid else
                  'finite_time_error_exceeds_ceiling' if not ceiling_ok else
                  'settlement_unresolved' if not settled_ok else 'growth_criterion_failed' if not growth_ok else
                  'performance_pass_numerics_pending')
        decisions.append(dict(stage=stage, dataset_id=name,
            group=datasets[name].get('metadata', {}).get('group', name), factor=factor, rank=rank,
            count=len(selected), expected_count=len(desired), complete=complete,
            missing_cases=[list(v) for v in sorted(desired-actual)],
            maximum_scaled_rms=max((r['scaled_rms'] for r in selected), default=None),
            median_scaled_rms=float(np.median([r['scaled_rms'] for r in selected])) if selected else None,
            all_constructions_valid=bool(selected and not invalid), construction_failure=construction_failure,
            all_trajectories_valid=bool(selected and all(r['trajectory_valid'] for r in selected)),
            all_settled=settled_ok, ceiling_pass=ceiling_ok, growth_pass=growth_ok,
            median_width_growth=growth, common120_median_width_growth=common_growth,
            performance_pass=performance, increase_trigger=trigger, status=status,
            maximum_residual=max((r['fit_rms'] for r in selected), default=None),
            maximum_dense_residual=max((max(r['dense_reference_fit'], r['dense_copy_fit']) for r in selected), default=None),
            initial_second_layer_priority_exhausted_count=sum(r['priority_exhausts_rank2'] for r in selected),
            observed_horizons=sorted({r['last_time'] for r in selected})))
    return decisions


def group_recommendations(rows, decisions):
    result = []
    for group in sorted({r['group'] for r in decisions if r['stage'] == 'baseline'}):
        baseline = [r for r in decisions if r['stage'] == 'baseline' and r['group'] == group]
        triggered = [r for r in baseline if r['increase_trigger']]
        choice = sorted(triggered, key=lambda r: (not(r['construction_failure'] or not r['all_constructions_valid']),
            -(r['maximum_scaled_rms'] if r['maximum_scaled_rms'] is not None else -1), r['dataset_id']))
        worst = choice[0]['dataset_id'] if choice else None
        diagnostic_all = [r for r in decisions if r['stage'] in ('diagnostic', 'diagnostics') and r['group'] == group]
        diagnostic = [r for r in diagnostic_all if r['performance_pass']]
        winner = min(diagnostic, key=lambda r: (r['factor'], r['maximum_scaled_rms'], r['rank'])) if diagnostic else None
        finite = [r for r in diagnostic_all if r['complete'] and r['all_trajectories_valid'] and r['ceiling_pass']]
        finite_best = min(finite, key=lambda r: (r['factor'], r['maximum_scaled_rms'], r['rank'])) if finite else None
        confirmed = [] if winner is None else [r['dataset_id'] for r in decisions if r['stage'] == 'confirmation'
            and r['group'] == group and (r['factor'], r['rank']) == (winner['factor'], winner['rank'])
            and r['performance_pass']]
        result.append(dict(group=group, triggered_datasets=[r['dataset_id'] for r in triggered],
            diagnostic_dataset=worst, diagnostic_case=None if worst is None else
                dict(dataset_id=worst, n=2048, seed=9411),
            selected_candidate=None if winner is None else
                dict(factor=winner['factor'], rank=winner['rank'], dataset_id=winner['dataset_id']),
            finite_time_ceiling_candidate_not_selected=None if finite_best is None else
                dict(factor=finite_best['factor'], rank=finite_best['rank'], dataset_id=finite_best['dataset_id'],
                     all_settled=finite_best['all_settled']),
            confirmed_datasets=confirmed,
            confirmation_required=[] if winner is None else
                [dict(dataset_id=r['dataset_id'], n=n, seed=9412) for r in triggered for n in (512, 2048)],
            recommendation='retain_baseline' if all(r['performance_pass'] for r in baseline) else
                'diagnose_prespecified_increase' if triggered and not diagnostic_all else
                'candidate_confirmed_numerics_pending' if winner and set(confirmed) >= {r['dataset_id'] for r in triggered} else
                'confirm_selected_candidate' if winner else
                'diagnostics_have_no_protocol_winner' if diagnostic_all else 'incomplete_or_settlement_unresolved'))
    return result


def refinement(coarse, fine):
    rc, c = load_case(coarse)
    rf, f = load_case(fine)
    if case_key(rc) != case_key(rf):
        raise ValueError('Refinement case identity mismatch')
    np.testing.assert_array_equal(c['U'], f['U'])
    np.testing.assert_array_equal(c['labels'], f['labels'])
    end = min(c['times'][-1], f['times'][-1])
    use = c['times'] <= end+1e-9
    times = c['times'][use]
    indices = np.searchsorted(f['times'], times)
    np.testing.assert_allclose(f['times'][indices], times, atol=1e-9, rtol=0)
    distance = np.max(np.abs(c['panel'][:, None]-f['panel'][None]), axis=2)
    columns = np.argmin(distance, axis=1)
    if np.max(distance[np.arange(len(columns)), columns]) > 1e-12:
        raise ValueError('Refinement panel does not contain all coarse queries')
    covers_coarse = bool(f['times'][-1] >= c['times'][-1]-1e-9)
    proper = bool(covers_coarse and np.isclose(rf['dt']*2, rc['dt']) and len(f['panel']) >= 2*len(c['panel']) and
                  np.max(np.diff(f['times'])) <= .5*np.max(np.diff(c['times']))+1e-9)
    names = [name for name in rc['model_names'] if name in rf['model_names']]
    ci = [rc['model_names'].index(name) for name in names]
    fi = [rf['model_names'].index(name) for name in names]
    cp = c['predictions'][use][:, ci]
    fp = f['predictions'][indices][:, fi]
    shared = fp[:, :, columns]
    all_fine_times = f['times'] <= end+1e-9
    full_fine = f['predictions'][all_fine_times][:, fi]
    cm = metrics(cp)
    fm, pm = metrics(full_fine[:, :, columns]), metrics(full_fine)
    same_point_gap = np.max(np.abs(cp-shared), axis=(0, 2))
    change = np.abs(cm['rms_time_sup']-fm['rms_time_sup'])
    rows = []
    for j, name in enumerate(names):
        threshold = max(1e-4, .05*float(cm['rms_time_sup'][j]))
        rows.append(dict(model=name, threshold=threshold,
            same_point_prediction_change=float(same_point_gap[j]), common_query_primary_change=float(change[j]),
            extra_panel_primary_change=float(abs(pm['rms_time_sup'][j]-fm['rms_time_sup'][j])),
            passed=bool(proper and same_point_gap[j] <= threshold and change[j] <= threshold)))
    reduced = [r for r in rows if r['model'] not in ('dense_reference', 'dense_independent', 'frozen_dense_hidden')]
    return dict(case=list(case_key(rc)), d=int(c['U'].shape[1]), coarse=str(coarse), fine=str(fine),
        common_horizon=float(end), original_coarse_horizon=float(c['times'][-1]),
        original_fine_horizon=float(f['times'][-1]), covers_coarse_horizon=covers_coarse,
        proper_refinement=proper, models=rows,
        passed=bool(reduced and all(r['passed'] for r in rows)))


def required_refinements(rows):
    result = []
    for kind in ('circle', 'sphere'):
        selected = [r for r in rows if r['stage'] not in ('refinement', 'refine', 'resolution')
                    and (r['d'] == 2) == (kind == 'circle')]
        if selected:
            worst = max(selected, key=lambda r: r['rms_time_sup'])
            result.append(dict(domain=kind, dataset_id=worst['dataset_id'], n=worst['n'], seed=worst['seed'],
                factor=worst['factor'], rank=worst['rank'], model=worst['model'],
                case_path=worst['case_path'], last_time=worst['last_time'], rms_time_sup=worst['rms_time_sup']))
    return result


def cell_summary(rows):
    result = []
    for key in sorted({(r['stage'], r['dataset_id'], r['factor'], r['rank'], r['n']) for r in rows}):
        selected = [r for r in rows if (r['stage'], r['dataset_id'], r['factor'], r['rank'], r['n']) == key]
        item = dict(zip(('stage', 'dataset_id', 'factor', 'rank', 'n'), key))
        item.update(count=len(selected), N=selected[0]['N'], P=selected[0]['P'],
                    all_settled=all(r['settled_valid'] for r in selected))
        for metric in ('scaled_rms', 'rms_time_sup', 'scaled_endpoint_rms', 'common120_scaled_rms',
                       'dense_scaled_rms', 'fit_rms', 'last_time'):
            item[metric+'_median'] = float(np.median([r[metric] for r in selected]))
            item[metric+'_max'] = max(r[metric] for r in selected)
        item['ratio_of_medians'] = ratio(np.median([r['rms_time_sup'] for r in selected]),
                                        np.median([r['dense_rms'] for r in selected]))
        result.append(item)
    return result


def plot(rows, controls, out):
    rows = [r for r in rows if r['stage'] not in ('refinement', 'refine', 'resolution')]
    if not rows:
        return
    os.environ.setdefault('MPLCONFIGDIR', str((out/'matplotlib_cache').resolve()))
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    names = sorted({r['dataset_id'] for r in rows if r['stage'] == 'baseline'})
    if not names:
        return
    fig, axes = plt.subplots(math.ceil(len(names)/3), 3, figsize=(13, 3*math.ceil(len(names)/3)),
                             squeeze=False, layout='constrained')
    for ax, name in zip(axes.flat, names):
        selected = [r for r in rows if r['dataset_id'] == name]
        for factor, rank in sorted({(r['factor'], r['rank']) for r in selected}):
            arm = [r for r in selected if (r['factor'], r['rank']) == (factor, rank)]
            for seed in sorted({r['seed'] for r in arm}):
                points = sorted([r for r in arm if r['seed'] == seed], key=lambda r: r['n'])
                ax.plot([r['n'] for r in points], [r['scaled_rms'] for r in points],
                    marker='o', linewidth=1, alpha=.75, label=f'{factor:g}× rank{rank}, s{seed}')
                bad = [r for r in points if not r['settled_valid']]
                ax.scatter([r['n'] for r in bad], [r['scaled_rms'] for r in bad],
                           marker='x', s=65, color='red', zorder=5)
        baseline = [r for r in controls if r['stage'] == 'baseline' and
                    r['dataset_id'] == name and r['model'] == 'dense_independent']
        widths = sorted({r['n'] for r in baseline})
        ax.plot(widths, [np.median([r['scaled_rms'] for r in baseline if r['n'] == n]) for n in widths],
                '--', color='0.4', label='dense-copy median')
        ax.axhline(.15, color='black', linestyle=':', linewidth=1)
        ax.set_title(name.replace('_', ' '), fontsize=10)
        ax.set_xscale('log', base=2); ax.set_yscale('log'); ax.grid(alpha=.2)
        ax.set_xlabel('Dense width n'); ax.set_ylabel('sqrt(n) × RMS of time max')
        ax.legend(fontsize=6)
    for ax in list(axes.flat)[len(names):]:
        ax.set_visible(False)
    fig.suptitle('Dataset continuation: every seed; red crosses mark invalid or unsettled models')
    fig.savefig(out/'multidata_scaled_rms.png', dpi=180)
    fig.savefig(out/'multidata_scaled_rms.pdf')
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs', nargs='+')
    parser.add_argument('--expected-config', nargs='*', default=[])
    parser.add_argument('--output')
    parser.add_argument('--refinement-pair', nargs=2, action='append', default=[])
    parser.add_argument('--no-plots', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    oracle = metric_oracle()
    if args.self_test:
        assert total_state(48, 2, 2) == 2550
        assert total_state(47, 5, 8) == 2633
        print(json.dumps(dict(metric_oracle=oracle, passed=True))); return
    if not args.inputs or not args.output:
        parser.error('--inputs and --output are required')
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    rows, controls, cases, failures, provenance, configs, datasets = extract(args.inputs, args.expected_config)
    decisions = dataset_decisions(rows, failures, configs, datasets)
    groups = group_recommendations(rows, decisions)
    refinements = [refinement(*pair) for pair in args.refinement_pair]
    required = required_refinements(rows)
    coverage = {kind: False for kind in ('circle', 'sphere')}
    for need in required:
        coverage[need['domain']] = any(check['passed'] and
            Path(check['coarse']).resolve() == Path(need['case_path']).resolve() and
            any(item['model'] == need['model'] and item['passed'] for item in check['models'])
            for check in refinements)
    if all(coverage.values()):
        for decision in decisions:
            if decision['performance_pass']:
                decision['status'] = 'performance_pass_checked'
    summary = dict(case_records=len(cases), comparison_count=len(rows),
        baseline_complete_cases=len({case_key(r) for r in cases if r['stage'] == 'baseline'}),
        baseline_expected_cases=72, dataset_decisions=decisions, group_recommendations=groups,
        failures=failures, refinement_checks=refinements, refinement_coverage=coverage,
        required_refinement_cases=required,
        numerical_checks_complete=all(coverage.values()), primary_ceiling=.15,
        metric_oracle=oracle, cluster_seeds=[9411, 9412],
        inference='Descriptive finite-grid evidence; no high-probability or asymptotic claim.',
        inputs=provenance)
    for name, data in (('all_comparisons.csv', rows), ('controls.csv', controls), ('cases.csv', cases),
                       ('cell_summary.csv', cell_summary(rows)), ('dataset_decisions.csv', decisions)):
        write_csv(out/name, data)
    (out/'summary.json').write_text(json.dumps(summary, indent=2, allow_nan=False)+'\n')
    (out/'analysis_provenance.json').write_text(json.dumps(dict(argv=sys.argv,
        python=sys.version, numpy=np.__version__, analysis_sha256=digest(__file__),
        protocol_sha256=digest(Path(__file__).with_name('GPU_MULTIDATA_PROTOCOL.md')),
        input_record_hashes={r['case_path']: r['record_sha256'] for r in cases}), indent=2)+'\n')
    (out/'analysis_source.py').write_bytes(Path(__file__).read_bytes())
    if not args.no_plots:
        plot(rows, controls, out)
    print(json.dumps({key: summary[key] for key in ('case_records', 'comparison_count',
        'baseline_complete_cases', 'group_recommendations', 'refinement_coverage')}, indent=2))


if __name__ == '__main__':
    main()
