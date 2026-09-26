"""Bounded saved-state audit for the fixed width-2048 derivative-dictionary suite.

Only numeric I/O, independent forward arithmetic, and metrics are inherited from
comparison_analyze. No trajectory producer or dictionary builder is imported.
Each case uses its manifest's same pair of dense endpoints for every method.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import signal
import sys
import time
import zipfile
import numpy as np
import torch
import comparison_analyze as base

ROOT, STUDY, DATA, ARCHIVE = base.ROOT, base.STUDY, base.DATA, base.ARCHIVE
WIDTH, THRESHOLD, REPLAY, GATE = 2048, 1e-3, 1e-10, .01
ORDERS = (1, 3, 5)
FAMILIES = ('new', 'old', 'gaussian', 'orthogonal')
COUNTS = {'new': {1: (2, 4), 3: (6, 12), 5: (14, 24)}}
COUNTS.update({family: {1: (5, 3), 3: (35, 10), 5: (128, 21)} for family in FAMILIES[1:]})
METHODS = tuple(f'{family}_p{p}' for family in FAMILIES for p in ORDERS)
LEVELS = ('primary', 'refined')
ARCHIVED_WRAPPER = 'studies/random_dictionary_learned_circle_20260920/scaling_benchmark.py'
ARCHIVED_WRAPPER_HASH = 'fce49cb577e89e1bed1a043277fd786af52b37ddac5b55a2ccfd861f9f637a9a'
RECOVERED_WRAPPER = DATA/'suite_inventory01/sourceproofs/acfbedf7_scaling_benchmark.py'
RECOVERY_RECORD = DATA/'suite_inventory01/sourceproofs/reconciliation.json'
READ_ROOTS = (ROOT/'code', STUDY, ROOT/'studies/random_dictionary_learned_circle_20260920', DATA, ARCHIVE)


class BudgetExpired(Exception):
    pass


def checked_path(value):
    path = Path(value)
    path = (ROOT/path).resolve() if not path.is_absolute() else path.resolve()
    if not any(path.is_relative_to(root) for root in READ_ROOTS):
        raise ValueError('input outside authorized scope: '+str(path))
    return path


def normalize_manifest(manifest):
    """The frozen manifest explicitly selects archive paths; no score selection."""
    cases = manifest.get('cases', manifest.get('width2048_original_cases'))
    if cases is None or not any(k in manifest for k in ('cells', 'archive_cells')):
        raise ValueError('manifest must contain cases and explicitly selected cells')
    cells = manifest.get('cells', manifest.get('archive_cells'))
    return cases, {key.replace('_ours_p', '_old_p'): value for key, value in cells.items()}


def locate_config(directory, case, method):
    """New producers may place an exact local config pointer beside each cell."""
    pointer = directory/'producer.json'
    if pointer.exists():
        return checked_path(base.read_json(pointer)['config_path'])
    matches = []
    for path in sorted(directory.parent.glob('config*.json')):
        config = base.read_json(path)
        declared = config.get('selected_cases', config.get('cases', {}))
        if case not in declared:
            continue
        if config.get('case') not in (None, case):
            continue
        if method not in config.get('methods', METHODS):
            continue
        assigned = config.get('assigned_cases', config.get('worker_cases'))
        if assigned is not None and case not in assigned:
            continue
        matches.append(path)
    if len(matches) != 1:
        raise ValueError(f'ambiguous or missing producer configuration for {directory}: {matches}')
    return matches[0]


def spec_path(spec):
    return checked_path(spec.get('path', spec.get('directory')))


def source_audit(config, spec, current, require, recoveries=None):
    """Validate executed dependencies, excluding unrelated archived plot/doc drift."""
    hashes = config.get('source_hashes', {})
    critical = spec.get('executed_producer_dependency_hashes', spec.get('executed_sources', config.get('executed_sources')))
    if isinstance(critical, dict):
        critical = list(critical)
    if critical is None:
        if current:
            critical = list(hashes)
        else:
            critical = [name for name in hashes if name.startswith('code/') or Path(name).name in (
                'benchmark.py', 'diverse_benchmark.py', 'diverse_dictionary.py', 'diverse_cases.py')]
            producer = Path(config.get('command', [''])[0]).name
            critical += [name for name in hashes if Path(name).name == producer]
    must = ['code/pde/finite_torch.py', 'code/pde/observable_torch_p1.py',
            'studies/random_dictionary_learned_circle_20260920/diverse_benchmark.py']
    if current:
        must += ['studies/gradient_flow_probe_dictionary_20260921/new_dictionary.py',
                 'studies/gradient_flow_probe_dictionary_20260921/new_dictionary_p45.py',
                 'studies/gradient_flow_probe_dictionary_20260921/suite_run.py',
                 'studies/gradient_flow_probe_dictionary_20260921/SUITE_PROTOCOL.md',
                 'studies/gradient_flow_probe_dictionary_20260921/SUITE_MANIFEST.json']
    require(all(name in hashes and name in critical for name in must), 'missing executed producer source hashes')
    checks = {}
    for name in sorted(set(critical)):
        require(name in hashes, 'missing source hash: '+name)
        if name not in hashes:
            continue
        source = checked_path(name)
        expected = spec.get('executed_producer_dependency_hashes', {}).get(name, hashes[name])
        require(expected == hashes[name], 'manifest/config source mismatch: '+name)
        checks[name] = base.digest(source) == hashes[name]
        if (not checks[name] and not current and name == ARCHIVED_WRAPPER
                and hashes[name] == ARCHIVED_WRAPPER_HASH and config.get('group') == 'discovery'
                and config.get('stage') == 'A'):
            reconciliation = base.read_json(RECOVERY_RECORD)
            listed = any(spec.get('config_path') == entry['config_path'] and spec.get('config_sha256') == entry['config_sha256']
                         for entry in reconciliation['matching_archived_endpoint_configs'])
            recovered_hash = base.digest(RECOVERED_WRAPPER)
            checks[name] = (listed and recovered_hash == hashes[name]
                            and reconciliation['expected_sha256'] == hashes[name]
                            and reconciliation['frozen_source_path'] == str(RECOVERED_WRAPPER))
            if recoveries is not None:
                recoveries.append(dict(original_path=str(source), current_sha256=base.digest(source),
                    expected_sha256=hashes[name], recovered_path=str(RECOVERED_WRAPPER),
                    recovered_sha256=recovered_hash, reconciliation_path=str(RECOVERY_RECORD),
                    reconciliation_sha256=base.digest(RECOVERY_RECORD), current_matches_recorded=False, recovered_matches_recorded=checks[name]))
        require(checks[name], 'executed producer source hash mismatch: '+name)
    return checks


@torch.no_grad()
def audit(spec, case, geometry, method, device, origin=None, manifest_path=None):
    directory = spec_path(spec)
    record = dict(path=str(directory), valid=False, fitted=False, replay_valid=False,
                  reasons=[], checks={}, status='missing')
    reasons, checks = record['reasons'], record['checks']
    bundle = None

    def require(condition, message):
        if not bool(condition):
            reasons.append(message)

    def difference(name, actual, expected, tolerance=REPLAY):
        a, b = base.tensor(actual, device), base.tensor(expected, device)
        if a.shape != b.shape:
            checks[name] = None
            reasons.append(name+': shape mismatch')
            return
        error = base.finite_number((a-b).abs().max()) if a.numel() else 0.
        checks[name] = error
        require(error is not None and error <= tolerance, name+' exceeds tolerance')

    try:
        summary = base.read_json(directory/'summary.json')
        config_path = checked_path(spec['config_path']) if spec.get('config_path') else locate_config(directory, case, method)
        config = base.read_json(config_path)
        if spec.get('config_sha256'):
            require(base.digest(config_path) == spec['config_sha256'], 'manifest/config hash mismatch')
        current = directory.is_relative_to(DATA)
        record.update(config_path=str(config_path), summary=summary, status=summary.get('status'),
                      rtol=config.get('rtol'), atol=config.get('atol'))
        for key, expected in (('width', WIDTH), ('network_seed', 20260920), ('threshold', THRESHOLD), ('dtype', 'float64')):
            require(config.get(key) == expected, 'configuration mismatch: '+key)
        declared = config.get('cases', {}).get(case)
        require(declared is not None, 'case absent from producer geometry')
        if declared is not None:
            require(all(declared.get(key) == geometry[key] for key in ('angles_degrees', 'labels')), 'configuration geometry mismatch')
        for name in ('rtol', 'atol'):
            value = config.get(name)
            require(isinstance(value, (float, int)) and value > 0, 'invalid '+name)
            require(summary.get(name) == value, 'summary/config '+name+' mismatch')
            if name in spec:
                require(value == spec[name], 'manifest/config '+name+' mismatch')
        record['producer_source_recoveries'] = []
        record['producer_source_checks'] = source_audit(config, spec, current, require, record['producer_source_recoveries'])
        if current:
            declared_manifest = checked_path(config['manifest_path'])
            require(manifest_path is not None and declared_manifest == manifest_path, 'producer manifest path mismatch')
            require(base.digest(declared_manifest) == config['manifest_sha256'], 'producer manifest hash mismatch')
            key = case+'_'+method
            require(key in config.get('execution_schedule', []), 'cell absent from declared execution schedule')
            results_path = directory.parent/f"results_worker{config['worker']}.json"
            results = base.read_json(results_path)
            execution = results.get(key, {})
            require(execution.get('declared_executed') is True, 'cell lacks declared execution result')
            for name, value in summary.items():
                require(execution.get(name) == value, 'execution/summary mismatch: '+name)
            initial_archive = checked_path(config['initial_archive'])
            require(initial_archive.is_relative_to(ARCHIVE), 'initialization is not in authorized archive')
            require(base.digest(initial_archive) == config['initial_archive_sha256'], 'initial archive hash mismatch')
            level = config.get('level')
            require(level in (0, 1, 2), 'invalid new tolerance level')
            if level in (0, 1, 2):
                require(config['rtol'] == 6.25e-5/4**level and config['atol'] == 6.25e-7/4**level, 'new tolerance differs from frozen protocol')
        if method.startswith('new'):
            metadata_path = checked_path(spec['dictionary_metadata_path']) if spec.get('dictionary_metadata_path') else (directory/'dictionary.json' if (directory/'dictionary.json').exists() else directory.parent/(directory.name+'_dictionary.json'))
            metadata = base.read_json(metadata_path)
            require(metadata.get('v_quadrature_absolute_discrepancy', math.inf) <= 1e-9, 'variance quadrature gate failed')
            record['dictionary_metadata_path'] = str(metadata_path)
            p = int(method.split('_p')[1])
            k1, k2 = COUNTS['new'][p]
            require((metadata['K1'], metadata['K2']) == (k1, k2), 'dictionary metadata dimensions mismatch')
            require(metadata['eta'] == 1/(1024*(p+1)**2), 'dictionary ridge changed')
            require(metadata.get('retained_initial_readout') is True and metadata.get('retained_dense_background') is False, 'dictionary initialization policy mismatch')
            for population in (metadata['lower'], metadata['upper']):
                condition, residual = population['ridge_condition'], population['triangular_relative_residual']
                require(math.isfinite(condition) and 1 <= condition <= 1e10, 'ridge condition gate failed')
                require(math.isfinite(residual) and 0 <= residual <= 1e-8, 'triangular residual gate failed')
            if p == 5:
                require(metadata['population_moments']['maximum_discrepancy'] <= 1e-9, 'population moment gate failed')
        record['arrays_sha256'] = base.digest(directory/'arrays.npz')
        with base.Arrays(directory/'arrays.npz') as saved:
            snapshots = saved['snapshot_times']
            require(snapshots.ndim == 1 and len(snapshots) >= 1, 'invalid snapshot times')
            require(saved.shape('w') == (len(snapshots), WIDTH, 2), 'saved readin shape mismatch')
            require(saved.shape('c') == (len(snapshots), WIDTH), 'saved readout shape mismatch')
            if method == 'full':
                middle_shape = (WIDTH, WIDTH)
                require('b1' not in saved and 'b2' not in saved, 'full reference contains bases')
                bases = {}
            else:
                family, order = method.split('_p')
                k1, k2 = COUNTS[family][int(order)]
                middle_shape = (k2, k1)
                require(saved.shape('b1') == (WIDTH, k1) and saved.shape('b2') == (WIDTH, k2), 'actual dictionary shape mismatch')
                record.update(K1=saved.shape('b1')[1], K2=saved.shape('b2')[1],
                              dictionary_array_sha256={key:hashlib.sha256(saved[key].tobytes()).hexdigest() for key in ('b1','b2','D')})
                bases = {key: base.tensor(saved[key], device) for key in ('b1', 'b2')}
                for key in ('p1', 'p2'):
                    difference('uniform_'+key, saved[key], torch.full((WIDTH,), 1/WIDTH, device=device, dtype=torch.float64))
                require(all(saved[key].dtype == np.float64 for key in ('b1', 'b2', 'D', 'g')), 'dictionary storage is not float64')
            require(saved.shape('M') == (len(snapshots), *middle_shape), 'saved middle shape mismatch')
            require(saved.shape('circle_predictions') == (len(snapshots), 2048), 'saved circle shape mismatch')
            for prefix, count in (('circle', 2048), ('endpoint', 8192)):
                angles = torch.arange(count, device=device, dtype=torch.float64)*(2*math.pi/count)
                difference(prefix+'_angles', saved[prefix+'_angles'], angles)
                difference(prefix+'_inputs', saved[prefix+'_inputs'], torch.stack((angles.cos(), angles.sin()), 1))
            angles = base.tensor(geometry['angles_degrees'], device)*(math.pi/180)
            difference('training_inputs', saved['training_inputs'], torch.stack((angles.cos(), angles.sin()), 1))
            difference('training_labels', saved['labels'], geometry['labels'])
            endpoint = base.tensor(saved['endpoint_prediction'], device)
            require(endpoint.shape == (8192,) and torch.isfinite(endpoint).all(), 'invalid endpoint output')
            times, losses = (base.tensor(saved[k], device) for k in ('times', 'losses'))
            require(times.ndim == 1 and times.shape == losses.shape and len(times) > 0, 'invalid loss/time shape')
            require(torch.isfinite(times).all() and torch.isfinite(losses).all(), 'nonfinite loss/time trace')
            require(times[0] == 0 and (times[1:] > times[:-1]).all(), 'time trace not strictly increasing from zero')
            require((losses[1:] <= losses[:-1]*(1+1e-8)+1e-12).all(), 'accepted loss increases')
            difference('summary_time', times[-1], summary['time'])
            difference('summary_initial_loss', losses[0], summary['initial_loss'])
            difference('summary_final_loss', losses[-1], summary['loss'])
            difference('initial_snapshot_time', snapshots[0], 0.)
            difference('final_snapshot_time', snapshots[-1], times[-1])
            require(np.isfinite(snapshots).all() and np.all(np.diff(snapshots) > 0), 'snapshot ordering invalid')
            accepted, errors = (base.tensor(saved[k], device) for k in ('accepted_steps', 'local_error_ratios'))
            difference('accepted_step_times', accepted, times.diff())
            require(len(accepted) == summary['steps'] <= 30000 and errors.shape == accepted.shape, 'step count mismatch')
            require(torch.isfinite(errors).all() and (errors >= 0).all() and (errors <= 1).all(), 'invalid local errors')
            require((accepted > 0).all() and (accepted <= 2+REPLAY).all(), 'steps outside bounds')
            initial_copy = None
            for index, label in ((0, 'initial'), (-1, 'final')):
                state = {}
                for key in ('w', 'c', 'M'):
                    raw = saved.snapshot(key, index)
                    require(raw.dtype == np.float64, label+' '+key+' not float64')
                    state[key] = base.tensor(raw, device)
                state.update(bases)
                require(all(torch.isfinite(x).all() for x in state.values()), label+' state nonfinite')
                difference(label+'_circle_replay', base.predict(state, saved['circle_inputs'], device), saved.snapshot('circle_predictions', index))
                loss = (base.predict(state, saved['training_inputs'], device)-base.tensor(saved['labels'], device)).square().mean()
                difference(label+'_loss_replay', loss, losses[0 if index == 0 else -1])
                if index == 0:
                    if method == 'full':
                        initial_copy = {key: state[key].clone() for key in ('w', 'c', 'M')}
                    if origin is not None:
                        for key in ('w', 'c') + (('M',) if method == 'full' else ()):
                            difference('common_initial_'+key, state[key], origin[key])
                    if method != 'full':
                        difference('initial_middle_D', state['M'], saved['D'])
                        difference('initial_readin_g', state['w'], saved['g'])
                        require(origin is not None, 'common dense initialization unavailable')
                        if origin is not None:
                            difference('projected_initial_middle', state['M'], state['b2'].T@(origin['M']@state['b1'])/WIDTH)
                    if current and origin is not None:
                        expected_hashes = config.get('initial_array_sha256', {})
                        for key in ('w', 'c', 'M'):
                            actual = hashlib.sha256(origin[key].cpu().numpy().tobytes()).hexdigest()
                            require(expected_hashes.get(key) == actual, 'initial array provenance mismatch: '+key)
                else:
                    difference('endpoint_replay', base.predict(state, saved['endpoint_inputs'], device), endpoint)
                    record['recomputed_loss'] = base.finite_number(loss)
                del state
            record.update(loss=summary['loss'], time=summary['time'],
                          first_crossing=bool((losses[:-1] > THRESHOLD).all()),
                          fitted=summary.get('status') == 'fitted' and float(losses[-1]) <= THRESHOLD*(1+1e-8))
            record['replay_valid'] = not reasons
            require(record['fitted'], 'not fitted at declared threshold')
            require(record['first_crossing'], 'not first detected threshold crossing')
            bundle = dict(prediction=endpoint, angles=saved['endpoint_angles'], inputs=saved['endpoint_inputs'],
                          training_inputs=saved['training_inputs'], labels=saved['labels'], initial=initial_copy,
                          dictionary_arrays={key:base.tensor(saved[key], device) for key in ('b1','b2','D')} if current else None)
        record['valid'] = not reasons
    except (OSError, ValueError, KeyError, TypeError, IndexError, RuntimeError, zipfile.BadZipFile) as exc:
        reasons.append(f'audit failure: {type(exc).__name__}: {exc}')
    return record, bundle


def paired(attempts, archived=None, is_new=False):
    reasons, branches = [], []
    if len(attempts) < 2:
        return dict(valid=False, reasons=['fewer than two levels'], refinement_max=None)
    if is_new and len(attempts) > 3:
        reasons.append('more than one extra attempted')
    for i in range(2, len(attempts)):
        prior = attempts[i-2:i]
        delta = base.discrepancy(prior[0][1], prior[1][1])
        eligible = all(item[0]['valid'] for item in prior) and delta is not None and delta > GATE
        branches.append(dict(eligible=eligible, preceding_refinement_max=delta, extra_path=attempts[i][0]['path']))
        if is_new and not eligible:
            reasons.append('extra lacked frozen refinement trigger')
    if is_new:
        for left, right in zip(attempts, attempts[1:]):
            a, b = left[1], right[1]
            if a is None or b is None or a.get('dictionary_arrays') is None or b.get('dictionary_arrays') is None:
                reasons.append('cross-level frozen dictionary unavailable')
            elif any(float((a['dictionary_arrays'][key]-b['dictionary_arrays'][key]).abs().max()) > REPLAY for key in ('b1','b2','D')):
                reasons.append('frozen dictionary differs across numerical levels beyond replay tolerance')
    selected = attempts[-2:]
    change = base.discrepancy(selected[0][1], selected[1][1])
    reasons.extend(f'{LEVELS[i]}: '+reason for i, item in enumerate(selected) for reason in item[0]['reasons'])
    if change is None or change > GATE:
        reasons.append('endpoint refinement sampled maximum exceeds .01 or is unavailable')
    for i in range(1, len(attempts)):
        for name in ('rtol', 'atol'):
            a, b = attempts[i-1][0].get(name), attempts[i][0].get(name)
            if a is None or b is None or b >= a or (is_new and not math.isclose(a, 4*b, rel_tol=1e-12)):
                reasons.append('invalid successive tolerances: '+name)
    # Preserve archive-invalid cells even if a weaker fresh audit would pass.
    if archived is not None and archived.get('valid') is False:
        reasons.extend('archived invalid: '+r for r in (archived.get('reasons') or ['selected numerical gate failed']))
    return dict(valid=not reasons, reasons=reasons, refinement_max=change,
                attempts=[a[0] for a in attempts], branch_checks=branches,
                selected_paths=[a[0]['path'] for a in selected])


def compare_rows(rows):
    lookup = {(r['case'], r['method']): r for r in rows}
    comparisons = []
    for case in dict.fromkeys(r['case'] for r in rows):
        for p in ORDERS:
            left = lookup[case, f'new_p{p}']
            for family in FAMILIES[1:]:
                baseline_p = min(ORDERS, key=lambda q: abs(sum(COUNTS[family][q])-left['vectors']))
                right = lookup[case, f'{family}_p{baseline_p}']
                winners = []
                item = dict(case=case, p=p, new_p=p, against=family, baseline_p=baseline_p,
                            new_vectors=left['vectors'], baseline_vectors=right['vectors'],
                            comparison_policy='closest available archived total-vector count among p1,p3,p5; no unrun p2',
                            valid=left['valid'] and right['valid'])
                for level in LEVELS:
                    a, b = left.get(level+'_rms'), right.get(level+'_rms')
                    winner = 'unavailable' if a is None or b is None else 'new' if a < b else family if b < a else 'tie'
                    item[level+'_winner'] = winner
                    item[level+'_baseline_over_new_rms'] = b/a if a is not None and b is not None and a > 0 else None
                    winners.append(winner)
                item['ordering_agrees'] = winners[0] == winners[1] and winners[0] != 'unavailable'
                item['verdict'] = winners[0] if item['valid'] and item['ordering_agrees'] else 'inconclusive'
                comparisons.append(item)
    return comparisons


def csv_write(path, rows):
    if not rows:
        return
    names = list(dict.fromkeys(k for row in rows for k in row))
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=names)
        writer.writeheader()
        writer.writerows({key: json.dumps(value) if isinstance(value, (dict, list)) else value for key, value in row.items()} for row in rows)


@torch.no_grad()
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--primary', type=Path, required=True)
    parser.add_argument('--refined', type=Path, required=True)
    parser.add_argument('--extra', type=Path, action='append', default=[])
    parser.add_argument('--cases', nargs='+')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--device', required=True)
    parser.add_argument('--budget', type=float, default=100)
    args = parser.parse_args()
    if not 0 < args.budget <= 100:
        parser.error('budget must be in (0,100] seconds')
    manifest_path = checked_path(args.manifest)
    manifest = base.read_json(manifest_path)
    cases, archive_cells = normalize_manifest(manifest)
    selected_cases = args.cases or list(cases)
    if len(set(selected_cases)) != len(selected_cases) or any(case not in cases for case in selected_cases):
        raise ValueError('invalid selected case list')
    roots = [base.owned(path) for path in (args.primary, args.refined, *args.extra)]
    extras_declared = [case+'_'+method for root in roots[2:] for case in cases for method in METHODS[:3] if (root/(case+'_'+method)).exists()]
    if len(extras_declared) > 33:
        raise ValueError('more than thirty-three extra new cells are present')
    out = base.owned(args.out)
    if out.exists() or len(set(roots)) != len(roots) or out in roots:
        raise ValueError('fresh output and distinct input roots required')
    out.mkdir(parents=True)
    if not torch.cuda.is_available() or torch.device(args.device).type != 'cuda':
        raise RuntimeError('CUDA required for scientific replay and metrics')
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.cuda.set_device(args.device)
    rows, validation, predictions, gates, completed = [], {}, {}, [], []
    started = time.monotonic()
    current_case = None
    outcome = 'complete'
    def timeout(signum, frame):
        raise BudgetExpired('100-second bounded analysis timer reached')
    prior_handler = signal.signal(signal.SIGALRM, timeout)
    # Reserve three seconds for saving final progress/provenance.
    signal.setitimer(signal.ITIMER_REAL, max(.1, args.budget-3))
    def save():
        base.write_json(out/'metrics.json', rows)
        base.write_json(out/'validation.json', validation)
        base.write_json(out/'comparisons.json', compare_rows(rows))
        base.write_json(out/'gates.json', dict(cells=gates, eligible_cells=[g['cell'] for g in gates if g['eligible']]))
        np.savez(out/'endpoint_predictions.npz', **predictions)
        csv_write(out/'metrics.csv', rows)
    try:
        for case in selected_cases:
            current_case = case
            audited = {}
            full_entry = archive_cells[case+'_full']
            full_specs = [full_entry[level] for level in LEVELS]
            full_attempts = [audit(full_specs[0], case, cases[case], 'full', args.device)]
            origin = full_attempts[0][1]['initial'] if full_attempts[0][1] else None
            full_attempts.append(audit(full_specs[1], case, cases[case], 'full', args.device, origin))
            full_check = paired(full_attempts, full_entry)
            validation[case+'_full'] = full_check
            audited['full'] = full_attempts
            for method in METHODS:
                key = case+'_'+method
                if method.startswith('new'):
                    paths = [root/key for root in roots[:2]]+[root/key for root in roots[2:] if (root/key).exists()]
                    specs = [dict(path=str(path)) for path in paths]
                    archive_entry = None
                else:
                    archive_entry = archive_cells[key]
                    specs = [archive_entry[level] for level in LEVELS]
                attempts = [audit(spec, case, cases[case], method, args.device, origin, manifest_path) for spec in specs]
                check = paired(attempts, archive_entry, method.startswith('new'))
                validation[key] = check
                audited[method] = attempts[-2:]
                if method.startswith('new'):
                    change = check['refinement_max']
                    eligible = len(attempts) == 2 and all(a[0]['valid'] for a in attempts) and change is not None and change > GATE
                    gates.append(dict(cell=key, eligible=eligible, refinement_max=change, next_level=2 if eligible else None,
                                      extras_attempted=max(0, len(attempts)-2)))
                base.write_json(out/'validation_partial.json', validation)
            case_rows = []
            for method in METHODS:
                key = case+'_'+method
                family, order = method.split('_p')
                p = int(order)
                k1, k2 = COUNTS[family][p]
                check = validation[key]
                row = dict(case=case, method=method, family=family, p=p, K1=k1, K2=k2, vectors=k1+k2,
                           middle_parameters=k1*k2, valid=check['valid'] and full_check['valid'],
                           reasons=check['reasons']+['full: '+r for r in full_check['reasons']],
                           refinement_max=check['refinement_max'], full_refinement_max=full_check['refinement_max'])
                for i, level in enumerate(LEVELS):
                    record, bundle = audited[method][i]
                    full_record, reference = full_attempts[i]
                    row.update({level+'_'+name: record.get(name) for name in ('path','rtol','atol','loss','time','status')})
                    row[level+'_full_path'] = full_record['path']
                    row[level+'_eligible'] = record['valid'] and full_record['valid']
                    for metric in ('rms','l1','mse','max_abs'):
                        for suffix in ('', '_grid4096', '_grid_change'):
                            row[level+'_'+metric+suffix] = None
                    if base.aligned(bundle, reference):
                        score = base.metrics(bundle['prediction'], reference['prediction'])
                        nested = base.metrics(bundle['prediction'][::2], reference['prediction'][::2])
                        for metric, value in score.items():
                            row[level+'_'+metric] = value
                            row[level+'_'+metric+'_grid4096'] = nested[metric]
                            row[level+'_'+metric+'_grid_change'] = abs(value-nested[metric]) if value is not None and nested[metric] is not None else None
                            if value is None:
                                row['valid'] = False
                                row['reasons'].append('nonfinite metric: '+level+' '+metric)
                    else:
                        row['valid'] = False
                        row['reasons'].append('reference/grid alignment failed: '+level)
                case_rows.append(row)
            for method, attempts in audited.items():
                for level, (_, bundle) in zip(LEVELS, attempts):
                    if bundle is not None:
                        predictions[case+'_'+method+'_'+level+'_prediction'] = bundle['prediction'].cpu().numpy()
                        predictions[case+'_angles'] = bundle['angles']
            rows.extend(case_rows)
            completed.append(case)
            save()
            print(json.dumps(dict(case=case, valid_rows=sum(r['valid'] for r in case_rows), seconds=time.monotonic()-started)), flush=True)
            del audited, full_attempts, origin, attempts, bundle
            torch.cuda.empty_cache()
    except BudgetExpired:
        outcome = 'budget_cap'
    except Exception:
        outcome = 'analysis_failure'
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, prior_handler)
        save()
        torch.cuda.synchronize(args.device)
        seconds = time.monotonic()-started
        base.write_json(out/'completion.json', dict(status=outcome, seconds=seconds, budget_seconds=args.budget,
            declared_cases=selected_cases, completed_cases=completed, incomplete_cases=[c for c in selected_cases if c not in completed],
            interrupted_case=current_case if outcome != 'complete' else None))
        base.write_json(out/'provenance.json', dict(command=sys.argv, device=args.device, gpu=torch.cuda.get_device_name(args.device),
            dtype='float64', width=WIDTH, torch=str(torch.__version__), numpy=np.__version__, cases=cases,
            manifest_path=str(manifest_path), manifest_sha256=base.digest(manifest_path), counts=COUNTS,
            executed_analysis_sources={str(Path(__file__)):base.digest(__file__), str(Path(base.__file__)):base.digest(base.__file__)},
            input_hashes=base.HASHES.copy(),
            comparison_policy='new6 vs archived8; new18 vs archived8; new38 vs archived45, closest available vector counts',
            selection='explicit archive manifest; latest two attempted new levels, including invalid attempts; no random-control selection',
            references='one common manifest-selected pair per case, shared across every compared method',
            numerical_limits=dict(replay=REPLAY, refinement=GATE, max_extra_per_new_cell=1, max_extra_new_total=33),
            metric='8192-angle RMS/L1/MSE/sampled maximum vs common dense reference; nested4096 diagnostics',
            output_hashes={str(path):base.digest(path) for path in sorted(out.iterdir()) if path.is_file()}))
        print(json.dumps(dict(out=str(out), status=outcome, completed_cases=completed, seconds=seconds)), flush=True)


if __name__ == '__main__':
    main()
