"""Scoped CPU NumPy rescore of frozen GELU panels; no analyzer/producer imports.

Retained from the executed activation_circle_audit_interim01/gelu_rescore.py.
Use explicit --metrics and --output paths; output is append-only. Reproduce
with PYTHONDONTWRITEBYTECODE=1 and OMP/OPENBLAS/MKL/NUMEXPR threads=1 using
/home/amir/miniconda3/bin/python. This validates saved panel arithmetic,
metadata and file integrity, not trajectory replay.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import time
import zipfile

import numpy as np

STUDY = Path(__file__).resolve().parent
MILESTONES = [.9, .5, .1, .03, .01, .003, .001]
SCALAR_KEYS = ('rms_8192', 'rms_4096', 'nested_grid_change',
               'closure_refinement_rms', 'dense_refinement_rms',
               'combined_sensitivity', 'closure_time', 'dense_time')


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b''):
            digest.update(chunk)
    return digest.hexdigest()


def array_hash(*arrays):
    digest = hashlib.sha256()
    for array in arrays:
        digest.update(str(array.shape).encode())
        digest.update(str(array.dtype).encode())
        digest.update(array.tobytes(order='C'))
    return digest.hexdigest()


def rms(x):
    return float(np.sqrt(np.mean(np.square(x), dtype=np.float64)))


def main(metrics_path, output_path):
    started = time.monotonic()
    metrics_path, output_path = Path(metrics_path).resolve(), Path(output_path).resolve()
    if output_path.exists():
        raise FileExistsError(output_path)
    analysis_hash = sha(metrics_path)
    analysis = json.loads(metrics_path.read_text())
    cases = {k: v for k, v in json.loads((STUDY / 'activation_circle_cases.json').read_text()).items()
             if v['activation'] == 'gelu'}
    rows = [r for r in analysis['comparisons'] if r['activation'] == 'gelu']
    primary = [r for r in analysis['primary_comparisons'] if r['activation'] == 'gelu']
    ranks = [r for r in analysis['order_comparisons'] if r['activation'] == 'gelu']
    failures = []
    def check(condition, name):
        if not bool(condition):
            failures.append(name)
        return bool(condition)
    check(len(rows) == 42, '42_milestone_rows')
    check(len(primary) == 6, '6_primary_rows')
    check(len(ranks) == 42, '42_order_comparisons')
    expected_rows = {(case, order, milestone) for case in cases for order in (1, 2, 3)
                     for milestone in MILESTONES}
    check({(r['case'], r['P'], r['milestone']) for r in rows} == expected_rows,
          'complete_unique_milestone_grid')
    paths = sorted({r[key] for r in rows for key in
                    ('dense_run', 'closure_run', 'dense_previous', 'closure_previous')})
    check(len(paths) == 16, '16_referenced_runs')
    source_checks = {}
    for filename in ('ACTIVATION_CIRCLE_PROTOCOL.md', 'activation_circle_cases.json'):
        actual = sha(STUDY / filename)
        source_checks[filename] = dict(actual_sha256=actual,
                                      expected_sha256=analysis['source_sha256'][filename])
        check(actual == analysis['source_sha256'][filename], filename + '_sha256')
    source_checks['check_activation_circle.py'] = dict(actual_sha256=sha(STUDY / 'check_activation_circle.py'),
                                                       purpose='read for audit-method context only; never imported')
    cache, integrity = {}, []
    max_mse_metadata_error = 0.
    max_relative_milestone_error = 0.
    for path in paths:
        run = Path(path)
        check('gelu__' in run.name, str(run) + '_scope')
        config = json.loads((run / 'config.json').read_text())
        summary = json.loads((run / 'summary.json').read_text())
        provenance = analysis['provenance'][path]
        run_checks = {}
        def local(condition, name):
            run_checks[name] = check(condition, run.name + ':' + name)
        actual_hashes = {name: sha(run / name) for name in ('config.json', 'summary.json', 'arrays.npz')}
        local(actual_hashes['config.json'] == summary['effective_config_sha256']
              == provenance['config_sha256'], 'config_sha256')
        local(actual_hashes['summary.json'] == provenance['summary_sha256'], 'summary_sha256')
        local(actual_hashes['arrays.npz'] == summary['arrays_sha256']
              == provenance['arrays_sha256'], 'arrays_sha256')
        local(summary['source_sha256'] == provenance['source_sha256'], 'recorded_source_hashes_consistent')
        with zipfile.ZipFile(run / 'arrays.npz') as archive:
            local(archive.testzip() is None, 'archive_crc')
        keys = ('times', 'losses', 'accepted_steps', 'local_error_ratios',
                'observation_times', 'observation_training_mse', 'observation_labels',
                'circle_angles', 'circle_inputs', 'circle_predictions',
                'train_inputs', 'train_labels', 'train_predictions')
        with np.load(run / 'arrays.npz', allow_pickle=False) as archive:
            arrays = {key: archive[key] for key in keys}
        x, y = np.asarray(config['inputs']), np.asarray(config['labels'])
        spec = cases[config['case']]
        theta = np.deg2rad(spec['angles_degrees'])
        expected_x = np.column_stack((np.cos(theta), np.sin(theta)))
        local(config['activation'] == summary['activation'] == 'gelu', 'activation')
        local(config['source_case_definition'] == spec, 'frozen_case_definition')
        local(np.allclose(x, expected_x, atol=2e-15, rtol=0)
              and np.array_equal(y, spec['labels']), 'literal_training_task')
        local(np.array_equal(x, arrays['train_inputs']) and np.array_equal(y, arrays['train_labels']),
              'saved_training_data')
        local(array_hash(x, y) == summary['data_sha256'] == provenance['data_sha256'], 'data_sha256')
        local(array_hash(arrays['circle_inputs']) == summary['query_sha256']
              == provenance['query_sha256'], 'query_sha256')
        expected_angles = np.arange(8192, dtype=np.float64) * (2*np.pi/8192)
        expected_circle = np.column_stack((np.cos(expected_angles), np.sin(expected_angles)))
        local(arrays['circle_angles'].shape == (8192,)
              and np.allclose(arrays['circle_angles'], expected_angles, atol=2e-15, rtol=0),
              '8192_uniform_angles')
        local(arrays['circle_inputs'].shape == (8192, 2)
              and np.allclose(arrays['circle_inputs'], expected_circle, atol=2e-15, rtol=0),
              'unit_circle_grid')
        fixed = dict(width=4096, seed=20260920, query_count=8192, initial_step=.05,
                     max_step=2., max_time=10000., max_steps=30000, max_wall_seconds=300.,
                     target_loss=.001, milestones=MILESTONES, bisection_iterations=32, threads=1)
        local(all(config[key] == value for key, value in fixed.items()), 'frozen_config')
        local(config['rtol'] in (1.25e-5, 3.125e-6)
              and config['atol'] == config['rtol']/100, 'solver_tolerance_pair')
        local(summary['status'] == 'target_loss' and summary['crossed_losses'] == MILESTONES,
              'all_milestones_reached')
        local(summary['dtype'] == 'float64' and summary['deterministic_algorithms']
              and not summary['tf32'], 'float64_deterministic_metadata')
        labels = list(map(str, arrays['observation_labels']))
        local(len(labels) == len(set(labels)), 'unique_observation_labels')
        local(arrays['circle_predictions'].shape == (len(labels), 8192)
              and np.isfinite(arrays['circle_predictions']).all(), 'finite_full_panels')
        local(arrays['train_predictions'].shape == (len(labels), 8)
              and np.isfinite(arrays['train_predictions']).all(), 'finite_training_predictions')
        rescored_mse = np.mean(np.square(arrays['train_predictions'] - y), axis=1)
        observation_summary = {o['label']: o for o in summary['observations']}
        local(set(labels) == set(observation_summary), 'observations_match_summary')
        error = float(np.max(np.abs(rescored_mse - arrays['observation_training_mse'])))
        max_mse_metadata_error = max(max_mse_metadata_error, error)
        local(error <= 2e-12, 'training_mse_metadata')
        observations = {}
        milestone_errors = []
        for i, label in enumerate(labels):
            mse = float(rescored_mse[i])
            t = float(arrays['observation_times'][i])
            local(abs(mse-observation_summary[label]['training_mse']) <= 2e-12,
                  label + '_summary_mse')
            local(t == observation_summary[label]['time'], label + '_summary_time')
            if label.startswith('loss_'):
                target = float(label[5:])
                relative = abs(mse/target - 1)
                milestone_errors.append(relative)
                max_relative_milestone_error = max(max_relative_milestone_error, relative)
                local(relative <= .01, label + '_mse_within_one_percent')
            observations[label] = dict(prediction=arrays['circle_predictions'][i], mse=mse, time=t)
        local(len(arrays['accepted_steps']) == summary['accepted'], 'accepted_count')
        local(np.isfinite(arrays['local_error_ratios']).all()
              and np.all(arrays['local_error_ratios'] <= 1), 'accepted_error_ratios')
        local(np.all(np.diff(arrays['times']) > 0)
              and np.allclose(np.diff(arrays['times']), arrays['accepted_steps'], atol=1e-10, rtol=1e-12),
              'trace_time_increments')
        local(np.isfinite(arrays['losses']).all() and arrays['losses'][-1] == summary['training_mse']
              and arrays['times'][-1] == summary['time'], 'trace_final')
        local(np.all(np.diff(arrays['observation_times']) >= 0)
              and np.all(arrays['observation_times'] <= summary['time'] + 1e-10), 'observation_order')
        cache[path] = dict(config=config, summary=summary, observations=observations,
                           grid=arrays['circle_inputs'])
        integrity.append(dict(run=path, actual_hashes=actual_hashes, checks=run_checks,
                              passed=all(run_checks.values()), mse_metadata_max_abs_error=error,
                              milestone_mse_max_relative_error=max(milestone_errors),
                              maximum_accepted_error_ratio=float(np.max(arrays['local_error_ratios']))))
    check(len({json.dumps(c['summary']['source_sha256'], sort_keys=True) for c in cache.values()}) == 1,
          'producer_hashes_identical_across_16_runs')
    check(len({c['summary']['initialization_hash'] for c in cache.values()}) == 1,
          'recorded_initialization_hash_identical_across_16_runs')
    results, differences = [], {key: 0. for key in SCALAR_KEYS}
    differences['physical_losses'] = 0.
    def rescore(row):
        label = 'loss_' + format(row['milestone'], 'g')
        selections = {'closure_fine': 'closure_run', 'dense_fine': 'dense_run',
                      'closure_previous': 'closure_previous', 'dense_previous': 'dense_previous'}
        o = {name: cache[row[key]]['observations'][label] for name, key in selections.items()}
        c, d, pc, pd = (o[name]['prediction'] for name in selections)
        score = rms(c-d)
        nested = rms((c-d)[::2])
        cs, ds = rms(c-pc), rms(d-pd)
        actual_losses = {name: data['mse'] for name, data in o.items()}
        gates = dict(closure_refinement_available=True, dense_refinement_available=True,
                     closure_absolute=cs <= .005, dense_absolute=ds <= .005,
                     closure_relative=cs <= .1*score, dense_relative=ds <= .1*score,
                     grid=abs(score-nested) <= 1e-5,
                     physical_loss=all(abs(mse-row['milestone']) <= .01*row['milestone']
                                       for mse in actual_losses.values()))
        passed = all(gates.values())
        agreed = score <= .1
        verdict = ('coarse_agreement' if agreed else 'coarse_disagreement') if passed else 'numerically_unresolved'
        return dict(case=row['case'], P=row['P'], milestone=row['milestone'],
                    rms_8192=score, rms_4096=nested, nested_grid_change=abs(score-nested),
                    closure_refinement_rms=cs, dense_refinement_rms=ds, combined_sensitivity=cs+ds,
                    closure_time=o['closure_fine']['time'], dense_time=o['dense_fine']['time'],
                    physical_losses=actual_losses, numerical_gates=gates, numerical_pass=passed,
                    failed_gates=[key for key, value in gates.items() if not value],
                    measured_coarse_agreement=agreed, scientific_verdict=verdict)
    for row in rows + primary:
        identity = f"{row['case']}:P{row['P']}:{row['milestone']}:{row['comparison_type']}"
        answer = rescore(row)
        for key in SCALAR_KEYS:
            error = abs(answer[key] - row[key])
            differences[key] = max(differences[key], error)
            check(error <= 2e-13*max(1, abs(answer[key])), identity+':'+key)
        for key in answer['physical_losses']:
            error = abs(answer['physical_losses'][key]-row['physical_losses'][key])
            differences['physical_losses'] = max(differences['physical_losses'], error)
            check(error <= 2e-12, identity+':physical_losses:'+key)
        for key in ('numerical_gates', 'numerical_pass', 'failed_gates', 'measured_coarse_agreement', 'scientific_verdict'):
            check(answer[key] == row[key], identity+':'+key)
        for key in ('closure', 'dense'):
            fine = cache[row[key+'_run']]['config']
            previous = cache[row[key+'_previous']]['config']
            local_model = 'moment' if key == 'closure' else 'dense'
            check(fine['case'] == previous['case'] == row['case'] and
                  fine['model'] == previous['model'] == local_model, identity+':'+key+'_identity')
            if key == 'closure':
                check(fine['order'] == previous['order'] == row['P'], identity+':order_identity')
            check(fine['rtol'] == row[key+'_rtol'] == 3.125e-6 and
                  previous['rtol'] == row[key+'_previous_rtol'] == 1.25e-5, identity+':tolerances')
        check(all(np.array_equal(cache[row['dense_run']]['grid'], cache[row[key]]['grid'])
                  for key in ('closure_run', 'dense_previous', 'closure_previous')), identity+':identical_grids')
        if row in rows:
            results.append(answer)
    for case in cases:
        check(len({r['dense_run'] for r in rows if r['case'] == case}) == 1,
              case+':common_fine_dense_reference')
    lookup = {(r['case'], r['P'], r['milestone']): r for r in results}
    rank_results = []
    rank_discrepancies = dict(lower_minus_higher_rms=0., summed_observed_sensitivity=0.)
    for rank in ranks:
        lo = lookup[(rank['case'], rank['lower_P'], rank['milestone'])]
        hi = lookup[(rank['case'], rank['higher_P'], rank['milestone'])]
        gap = lo['rms_8192'] - hi['rms_8192']
        margin = lo['combined_sensitivity'] + hi['combined_sensitivity']
        both = lo['numerical_pass'] and hi['numerical_pass']
        resolved = both and abs(gap) > margin
        verdict = ('higher_order_improves' if gap > 0 else 'higher_order_worsens') if resolved else 'unresolved'
        out = dict(case=rank['case'], milestone=rank['milestone'], lower_P=rank['lower_P'],
                   higher_P=rank['higher_P'], lower_minus_higher_rms=gap,
                   summed_observed_sensitivity=margin, both_numerical_gates_pass=both,
                   resolved=resolved, verdict=verdict)
        for key in rank_discrepancies:
            error = abs(out[key]-rank[key])
            rank_discrepancies[key] = max(rank_discrepancies[key], error)
            check(error <= 2e-13, 'ranking:'+str((rank['case'],rank['milestone'],rank['lower_P'],rank['higher_P'],key)))
        for key in ('both_numerical_gates_pass', 'resolved', 'verdict'):
            check(out[key] == rank[key], 'ranking:'+str((rank['case'],rank['milestone'],key)))
        rank_results.append(out)
    check(sha(metrics_path) == analysis_hash, 'metrics_summary_unchanged_during_audit')
    primary_results = [lookup[(r['case'], r['P'], r['milestone'])] for r in primary]
    output = dict(scope='GELU saved-panel scalar audit; no training, GPU, Torch or production imports',
                  not_checked=['physical checkpoint replay', 'checkpoint file integrity',
                               'input config files or campaign manifests',
                               'current producer source file hashes (recorded hashes only)',
                               'fresh initialization draw reproduction'],
                  input_metrics=str(metrics_path), input_metrics_sha256=analysis_hash,
                  auditor_sha256=sha(Path(__file__)), source_checks=source_checks,
                  environment=dict(python=sys.version, numpy=np.__version__, platform=platform.platform(),
                                   threads={k: os.environ.get(k) for k in
                                            ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS')}),
                  counts=dict(runs=len(paths), milestone_rows=len(results), primary_rows=len(primary_results),
                              order_comparisons=len(rank_results)),
                  maximum_discrepancies=differences, maximum_rank_discrepancies=rank_discrepancies,
                  maximum_training_mse_metadata_error=max_mse_metadata_error,
                  maximum_milestone_mse_relative_error=max_relative_milestone_error,
                  all_numerical_gates_pass=all(r['numerical_pass'] for r in results),
                  all_primary_exceed_scientific_rms_0p1=all(r['rms_8192'] > .1 for r in primary_results),
                  primary=primary_results, milestones=results, rankings=rank_results,
                  integrity=integrity, failures=failures, passed=not failures,
                  elapsed_seconds=time.monotonic()-started)
    with output_path.open('x') as handle:
        json.dump(output, handle, indent=2, allow_nan=False)
        handle.write('\n')
    print(json.dumps({key: output[key] for key in
                      ('counts', 'maximum_discrepancies', 'maximum_rank_discrepancies',
                       'maximum_training_mse_metadata_error', 'maximum_milestone_mse_relative_error',
                       'all_numerical_gates_pass', 'all_primary_exceed_scientific_rms_0p1',
                       'failures', 'passed', 'elapsed_seconds')}, indent=2))
    print('OUTPUT', output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--metrics', required=True, type=Path, help='Frozen metrics_summary.json to verify')
    parser.add_argument('--output', required=True, type=Path, help='Fresh audit JSON path; existing output is refused')
    args = parser.parse_args()
    main(args.metrics, args.output)
