"""Bounded J2 coverage runner with exact shared setup/runtime acceleration.

Compilation is cached by exact task/configuration and implementation hashes.
Training requires --train; the default only compiles and checks the scalar RHS.
Every run carries 64 circle queries and passive copies of all training inputs.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import hashlib
import json
from pathlib import Path
import pickle
import platform
import signal
import subprocess
import sys
import time

import numpy as np
import scipy

from circle_tasks import directions
from run_true_aggregate_selective import BudgetReached, integrate
from selective_runtime_fast import FastSharedQueryClosure
from selective_initialization_fast import initialize_shared_fast
from true_aggregate_ode import flatten
from true_aggregate_references import digest, initial_block_pool, write_json


SOURCE_NAMES = ('run_selective_all_tasks.py', 'geometry_tasks.py',
    'selective_runtime_fast.py', 'selective_initialization_fast.py',
    'true_aggregate_selective_fast.py', 'true_aggregate_selective.py',
    'true_aggregate_ode.py', 'run_true_aggregate_selective.py',
    'true_aggregate_references.py', 'block_scalar_closure.py',
    'circle_tasks.py', 'dense_wide_integrator.py', 'SELECTIVE_ALL_TASKS_PROTOCOL.md')


def load_template(task, output, source_hashes):
    """Never repeat a completed or failed compilation for the same cache key."""
    from true_aggregate_selective_fast import FastSelectiveClosure
    u, labels = task.data()
    configuration = {'task': task.name, 'u': u.tolist(), 'labels': labels.tolist(),
        'k': 4, 'order': 1, 'mark_bound': 3., 'boundary': 'zero',
        'dependency_depth': 0, 'augment_outputs': True, 'preserve_essential': True,
        'output_depth': 2, 'symbolic_query_angle': .123,
        'compile_seconds': 60., 'max_states': 100000, 'max_terms': 1000000,
        'sources': source_hashes}
    fingerprint = hashlib.sha256(json.dumps(configuration, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()
    cache = output/'cache'
    cache.mkdir(parents=True, exist_ok=True)
    metadata_path = cache/f'{task.name}__{fingerprint}.json'
    template_path = metadata_path.with_suffix('.pkl')
    if metadata_path.exists():
        metadata = json.loads(metadata_path.read_text())
        if metadata['configuration'] != configuration:
            raise ValueError('Cached template configuration mismatch')
        if not metadata['compile']['complete']:
            return None, {**metadata, 'cache_hit': True}
        template_path = Path(metadata['pickle_file'])
        if digest(template_path) != metadata['pickle_sha256']:
            raise ValueError('Cached template digest mismatch')
        with template_path.open('rb') as handle:
            model = pickle.load(handle)
        return model, {**metadata, 'cache_hit': True}
    if template_path.exists():
        raise FileExistsError('Incomplete cache transaction; do not silently recompile')
    # A compatible old one-query template can initialize the full new panel;
    # an old state without the aliases is never reused as a complete state.
    prior = output.parent.parent/'selective_order_20260927/scalar/cache'
    for old_path in sorted(prior.glob(f'{task.name}__*.json')):
        old = json.loads(old_path.read_text())
        old_config = old.get('configuration', {})
        science_keys = ('task', 'u', 'labels', 'k', 'order', 'mark_bound', 'boundary',
                        'dependency_depth', 'augment_outputs', 'preserve_essential',
                        'output_depth', 'symbolic_query_angle')
        runtime_keys = ('true_aggregate_selective_fast.py', 'true_aggregate_selective.py',
                        'true_aggregate_ode.py')
        if (all(old_config.get(key) == configuration[key] for key in science_keys)
                and all(old_config.get('sources', {}).get(key) == source_hashes[key]
                        for key in runtime_keys) and old.get('compile', {}).get('complete')):
            old_pickle = Path(old['pickle_file'])
            if digest(old_pickle) != old['pickle_sha256']:
                raise ValueError('Prior template digest mismatch')
            with old_pickle.open('rb') as handle:
                model = pickle.load(handle)
            metadata = {'configuration': configuration, 'fingerprint': fingerprint,
                'compile': model.report, 'pickle_file': str(old_pickle),
                'pickle_sha256': old['pickle_sha256'], 'prior_cache_metadata': str(old_path),
                'prior_cache_metadata_sha256': digest(old_path), 'compilation_executed': False}
            write_json(metadata_path, metadata)
            return model, {**metadata, 'cache_hit': True}
    model = None
    compile_started = time.monotonic()
    def compile_alarm(signum, frame):
        raise BudgetReached('Constructor-inclusive compilation wall limit')
    previous = signal.signal(signal.SIGALRM, compile_alarm)
    signal.setitimer(signal.ITIMER_REAL, 60.)
    try:
        model = FastSelectiveClosure(u, labels, k=4, order=1,
            queries=np.vstack((u, directions([.123])[0])), mark_bound=3.,
            boundary='zero', dependency_depth=0, augment_outputs=True,
            preserve_essential=True, output_depth=2)
        model.compile(seconds=max(.001, 60.-(time.monotonic()-compile_started)),
                      max_states=100000, max_terms=1000000)
        compile_report = model.report
    except (BudgetReached, MemoryError) as error:
        compile_report = {'complete': False,
            'status': 'constructor_compile_wall_limit' if isinstance(error, BudgetReached) else 'memory_limit',
            'states': len(getattr(model, 'trees', ())) if model is not None else None,
            'processed_states': len(getattr(model, 'rows', ())) if model is not None else None,
            'error': str(error)}
        model = None
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.)
        signal.signal(signal.SIGALRM, previous)
    compile_report['constructor_inclusive_seconds'] = time.monotonic()-compile_started
    compile_report['hard_wall_cap_includes_constructor'] = True
    metadata = {'configuration': configuration, 'fingerprint': fingerprint,
                'compile': compile_report, 'pickle_file': str(template_path),
                'compilation_executed': True}
    if model is not None and model.compiled:
        with template_path.open('xb') as handle:
            pickle.dump(model, handle, protocol=pickle.HIGHEST_PROTOCOL)
        metadata['pickle_sha256'] = digest(template_path)
    write_json(metadata_path, metadata)
    return (model if model is not None and model.compiled else None), {**metadata, 'cache_hit': False}


def resource_estimate(template, count):
    """Conservative float64/int64 allocation accounting before query setup."""
    passive_colors = {i for i, name in enumerate(template.colors)
                      if name[0] in ('x', 'h') and name[1] >= template.m}
    flags = np.asarray([any(col in passive_colors for _, decorations in flatten(tree)[0]
                        for col in decorations) for tree in template.trees], dtype=bool)
    passive = int(np.sum(flags))
    core = len(flags)-passive
    passive_terms = int(np.sum(flags[template.row_index]))
    terms = len(template.values)
    dynamic = core+count*passive+1
    # Four lane-by-passive-term arrays cover cached scatter indices, weights,
    # indexed child values and their product; remaining terms cover raw/q,
    # fields/coefficient matrices, packed metadata and RK45/state storage.
    estimated = 8*(4*count*passive_terms + 4*count*len(flags)
                   + 3*count*len(template.coeff_keys) + 20*dynamic + 10*terms)
    return {'shared_core': core, 'passive_per_query': passive, 'query_count': count,
        'total_dynamic_scalars': dynamic, 'retained_terms': terms,
        'core_terms': terms-passive_terms, 'passive_terms': passive_terms,
        'estimated_peak_workspace_bytes': estimated,
        'estimated_workspace_formula': '8*(4*N*passive_terms+4*N*template_states+3*N*coefficient_keys+20*dynamic_states+10*retained_terms)',
        'max_dynamic_scalars': 2000000, 'max_workspace_bytes': 1073741824,
        'passed': dynamic <= 2000000 and estimated <= 1073741824}


def reference_comparison(path, circle_angles, prediction, train_prediction,
                         alias_prediction, fitted):
    """Raw errors on the exact same 64 angles; aliases never enter circle RMS."""
    if not path.exists() or not path.with_suffix('.json').exists():
        return {'status': 'reference_pending', 'expected_data_file': str(path)}
    metadata = json.loads(path.with_suffix('.json').read_text())
    with np.load(path, allow_pickle=False) as data:
        angles = data['angles']
        distances = np.abs(np.angle(np.exp(1j*(circle_angles[:, None]-angles[None, :]))))
        indices = np.argmin(distances, axis=1)
        if len(np.unique(indices)) != len(circle_angles) or np.max(
                distances[np.arange(len(circle_angles)), indices]) > 1e-13:
            raise ValueError('Reference lacks the exact requested 64-point circle grid')
        reference_circle = data['prediction'][indices]
        reference_train = data['train_prediction']
    if reference_train.shape != train_prediction.shape:
        raise ValueError('Reference training design mismatch')
    difference = prediction-reference_circle
    rms = float(np.sqrt(np.mean(difference*difference)))
    coarse = float(np.sqrt(np.mean(difference[::2]**2)))
    return {'status': 'available', 'raw_circle_rms': rms,
        'circle_grid_change_64_vs_32': abs(rms-coarse),
        'core_train_prediction_rms': float(np.sqrt(np.mean((train_prediction-reference_train)**2))),
        'passive_train_prediction_rms': float(np.sqrt(np.mean((alias_prediction-reference_train)**2))),
        'reference_train_prediction': reference_train.tolist(),
        'fitted_pair': bool(fitted and metadata['fitted']),
        'reference_train_mse': metadata['train_mse'],
        'reference_physical_time': metadata['physical_time'],
        'reference_circle_indices': indices.tolist(),
        'data_file': str(path), 'data_sha256': digest(path),
        'metadata_sha256': digest(path.with_suffix('.json'))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task', required=True)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--references', required=True, type=Path)
    parser.add_argument('--train', action='store_true', help='Run only after protocol authorization')
    parser.add_argument('--campaign-deadline', type=float, help='Absolute Unix wall deadline')
    args = parser.parse_args()
    from circle_tasks import TASKS as circle_tasks
    from geometry_tasks import TASKS as geometry_tasks
    tasks = {task.name: task for task in (*circle_tasks, *geometry_tasks)}
    task = tasks[args.task]
    started = time.monotonic()
    args.output.mkdir(parents=True, exist_ok=True)
    report_path = args.output/f'{task.name}__selective_zero_out2.json'
    data_path = report_path.with_suffix('.npz')
    if args.train and (report_path.exists() or data_path.exists()):
        raise FileExistsError('No duplicate J2 coverage training or overwritten results')
    source = Path(__file__).resolve().parent
    source_hashes = {name: digest(source/name) for name in SOURCE_NAMES}
    u, labels = task.data()
    circle_angles = 2*np.pi*np.arange(64)/64
    all_angles = np.r_[circle_angles, np.asarray(task.angles)]
    report = {'task': task.name, 'train_angles': list(task.angles),
        'train_labels': labels.tolist(), 'method': 'selective_zero_output_depth2',
        'width_initial_pool': 1024, 'k': 4, 'order': 1, 'seed': 1,
        'mark_bound': 3., 'output_dependency_depth': 2, 'dependency_depth': 0,
        'boundary': 'zero', 'preserve_essential': True, 'target_mse': .001,
        'target_rmse': float(np.sqrt(.001)),
        'circle_grid': 64, 'passive_train_aliases': len(labels),
        'passive_query_order': '64 circle angles followed by every training angle',
        'fit_criterion': 'MSE of shared-core training predictions',
        'primary_metric': 'raw circle RMS versus matched block-memory population on exactly 64 matched angles',
        'secondary_metric': 'raw circle RMS versus canonical Gaussian on the same angles',
        'circle_rms_excludes_training_aliases': True,
        'solver': {'method': 'RK45', 'rtol': 1e-5, 'atol': 1e-7,
            'first_step': .01, 'max_step': 1., 'physical_time_cap': 3000.,
            'training_wall_cap': 45.,
            'error_norm': 'maximum scaled RMS over core, each passive block, and clock'},
        'command': sys.argv, 'sources': source_hashes,
        'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=source.parent.parent,
                                            text=True).strip(),
        'environment': {'python': platform.python_version(), 'numpy': np.__version__,
                        'scipy': scipy.__version__, 'platform': platform.platform(),
                        'blas_threads': 1},
        'campaign_deadline_epoch': args.campaign_deadline,
        'runtime_state': 'shared scalar contractions, passive scalar contractions, one clock'}
    template, cache_info = load_template(task, args.output, source_hashes)
    report['template_cache'] = cache_info
    report['compile'] = cache_info['compile']
    if template is None:
        report.update(stop_reason='compile_limit', fitted=False, training_seconds=0.,
                      total_seconds=time.monotonic()-started)
        write_json(report_path if args.train else args.output/f'{task.name}__counts.json', report)
        print(json.dumps(report), flush=True)
        return
    report['resource_estimate'] = resource_estimate(template, len(all_angles))
    if not report['resource_estimate']['passed']:
        report.update(stop_reason='full_query_memory_gate', fitted=False,
                      training_seconds=0., total_seconds=time.monotonic()-started,
                      training_executed=False)
        write_json(report_path if args.train else args.output/f'{task.name}__counts.json', report)
        print(json.dumps(report), flush=True)
        return
    model = FastSharedQueryClosure(template, all_angles)
    report['state_counts'] = {'shared_core': model.ncore, 'passive_per_query': model.npassive,
        'circle_queries': 64, 'training_alias_queries': len(labels),
        'total_dynamic_scalars': model.size, 'single_query_template': len(template.trees)+1}
    report['passive_independence'] = model.check_independence()
    report['vectorization_check'] = model.check_vectorization()
    print(json.dumps({'phase': 'compiled', 'task': task.name,
        'cache_hit': cache_info['cache_hit'], **report['state_counts']}), flush=True)
    if not args.train:
        report['training_executed'] = False
        write_json(args.output/f'{task.name}__counts.json', report)
        return
    used_seconds = sum(json.loads(path.read_text()).get('training_seconds', 0.)
                       for path in args.output.glob('*__selective_zero_out2.json'))
    report['prior_scalar_training_seconds'] = used_seconds
    remaining_wall = (args.campaign_deadline-time.time()
                      if args.campaign_deadline else float('inf'))
    if used_seconds >= 270. or remaining_wall <= 0.:
        report.update(stop_reason='campaign_budget', fitted=False, training_seconds=0.)
        write_json(report_path, report)
        return
    def init_alarm(signum, frame):
        raise BudgetReached('Initial contraction integration wall limit')
    old_handler = signal.signal(signal.SIGALRM, init_alarm)
    signal.setitimer(signal.ITIMER_REAL, min(90., remaining_wall))
    try:
        pool = initial_block_pool(1024, 4, 1, 3.)
        initial, report['initialization'] = initialize_shared_fast(model, pool)
        report['initial_pool_entry_redraws'] = pool['entry_redraws']
        del pool
    except BudgetReached:
        report.update(stop_reason='initialization_wall_limit', fitted=False,
                      training_seconds=0., total_seconds=time.monotonic()-started)
        write_json(report_path, report)
        print(json.dumps(report), flush=True)
        return
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.)
        signal.signal(signal.SIGALRM, old_handler)
    initial_core = model.prediction(initial)
    initial_alias = model.circle_prediction(initial)[64:]
    report['initial_train_mse'] = float(np.mean((initial_core-labels)**2))
    report['initial_alias_max_gap'] = float(np.max(np.abs(initial_alias-initial_core)))
    benchmark = time.monotonic()
    velocity = model.rhs(0., initial)
    report['initial_rhs_seconds'] = time.monotonic()-benchmark
    if not np.all(np.isfinite(velocity)):
        raise ValueError('Initial scalar RHS is not finite')
    if report['initial_rhs_seconds'] > 1.:
        report.update(stop_reason='rhs_cost_gate', fitted=False, training_seconds=0.,
                      total_seconds=time.monotonic()-started)
        write_json(report_path, report)
        return
    print(json.dumps({'phase': 'initialized', 'task': task.name,
        'initial_core_mse': report['initial_train_mse'],
        'initial_alias_max_gap': report['initial_alias_max_gap'],
        'rhs_seconds': report['initial_rhs_seconds']}), flush=True)
    remaining_wall = (args.campaign_deadline-time.time()
                      if args.campaign_deadline else float('inf'))
    fit_seconds = min(45., 270.-used_seconds, remaining_wall)
    if fit_seconds <= .25:
        report.update(stop_reason='campaign_budget', fitted=False, training_seconds=0.,
                      total_seconds=time.monotonic()-started)
        write_json(report_path, report)
        return
    report['solver']['training_wall_cap'] = fit_seconds
    state, history, info = integrate(model, initial, labels, fit_seconds, target=.001)
    report.update(info)
    core_prediction = model.prediction(state)
    passive_prediction = model.circle_prediction(state)
    circle_prediction, alias_prediction = passive_prediction[:64], passive_prediction[64:]
    core_mse = float(np.mean((core_prediction-labels)**2))
    alias_mse = float(np.mean((alias_prediction-labels)**2))
    gap = alias_prediction-core_prediction
    report.update(train_mse=core_mse, core_train_rmse=float(np.sqrt(core_mse)),
        passive_train_mse=alias_mse, passive_train_rmse=float(np.sqrt(alias_mse)),
        alias_gap_rms=float(np.sqrt(np.mean(gap*gap))), alias_gap_max=float(np.max(np.abs(gap))),
        train_prediction=core_prediction.tolist(), passive_train_prediction=alias_prediction.tolist(),
        final_max_abs_q=float(np.max(np.abs(state[:-1]))),
        final_clipped_fraction=float(np.mean(np.abs(state[:-1]) > 1.)),
        endpoint_status='fitted threshold endpoint' if report['fitted'] else 'partial endpoint')
    for method, suffix in [('gaussian', 'gaussian'), ('block', 'block_k4_P1_canonical')]:
        reference_metadata = args.references/f'{task.name}__{suffix}.json'
        if reference_metadata.exists() and json.loads(reference_metadata.read_text())['target_mse'] != .001:
            raise ValueError('Reference target differs from the fixed MSE.001 target')
        report[f'{method}_comparison'] = reference_comparison(
            args.references/f'{task.name}__{suffix}.npz', circle_angles,
            circle_prediction, core_prediction, alias_prediction, report['fitted'])
    gaussian = report['gaussian_comparison']
    report['core_train_prediction_rms_vs_gaussian'] = gaussian.get('core_train_prediction_rms')
    report['passive_train_prediction_rms_vs_gaussian'] = gaussian.get('passive_train_prediction_rms')
    report['core_train_prediction_rms_vs_block'] = report['block_comparison'].get('core_train_prediction_rms')
    report['passive_train_prediction_rms_vs_block'] = report['block_comparison'].get('passive_train_prediction_rms')
    report['history_columns'] = ['physical_time', 'core_train_mse', 'L', 'max_abs_q', 'fraction_outside_unit_box']
    np.savez_compressed(data_path, state=state, initial_state=initial, history=history,
        angles=circle_angles, prediction=circle_prediction, all_query_angles=all_angles,
        all_passive_prediction=passive_prediction, train_prediction=core_prediction,
        passive_train_prediction=alias_prediction, alias_gap=gap,
        train_angles=task.angles, train_labels=labels, core_ids=model.core_ids,
        passive_ids=model.passive_ids, template_Fids=template.Fids)
    report.update(data_file=data_path.name, data_sha256=digest(data_path),
                  total_seconds=time.monotonic()-started, training_executed=True)
    write_json(report_path, report)
    print(json.dumps(report, allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
