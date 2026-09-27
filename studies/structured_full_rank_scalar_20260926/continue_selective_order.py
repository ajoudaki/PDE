"""Resume frozen J=1/J=2 scalar checkpoints to an explicit tighter MSE.

No initialization or compilation runs. The same autonomous scalar ODE resumes
from the exact saved vector; elapsed solver time is offset in reported history.
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
import subprocess
import sys
import time

import numpy as np
import scipy

from run_true_aggregate_selective import SharedQueryClosure, integrate
from run_selective_geometry import reference_comparison
from true_aggregate_references import digest, write_json


TASKS = ('pair_orthogonal_cos1', 'cluster_triple_cos1', 'triple_wide_mixed')
SOURCE_NAMES = ('continue_selective_order.py', 'run_selective_geometry.py',
    'run_true_aggregate_selective.py', 'true_aggregate_selective_fast.py',
    'true_aggregate_selective.py', 'true_aggregate_ode.py',
    'true_aggregate_references.py', 'dense_wide_integrator.py',
    'SELECTIVE_TIGHTER_PROTOCOL.md')


def state_digest(state):
    return hashlib.sha256(np.ascontiguousarray(state).tobytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task', choices=TASKS, required=True)
    parser.add_argument('--output-depth', type=int, choices=(1, 2), required=True)
    parser.add_argument('--target-mse', type=float, required=True)
    parser.add_argument('--source-directory', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--references', type=Path, required=True)
    parser.add_argument('--campaign-deadline', type=float)
    parser.add_argument('--train', action='store_true')
    args = parser.parse_args()
    if not 0. < args.target_mse < .01:
        parser.error('Continuation requires a positive target MSE below .01')
    started = time.monotonic()
    args.output.mkdir(parents=True, exist_ok=True)
    tag = f'{args.task}__selective_zero_out{args.output_depth}'
    report_path, data_path = args.output/f'{tag}.json', args.output/f'{tag}.npz'
    if args.train and (report_path.exists() or data_path.exists()):
        raise FileExistsError('No repeated continuation or overwritten result')
    source_tag = (f'{args.task}__selective_zero' if args.output_depth == 1
                  else f'{args.task}__selective_zero_out2')
    source_path = args.source_directory/f'{source_tag}.json'
    old = json.loads(source_path.read_text())
    if not old['fitted'] or old['output_dependency_depth'] != args.output_depth:
        raise ValueError('Expected a fitted checkpoint at the requested output depth')
    source_data_path = args.source_directory/old['data_file']
    if digest(source_data_path) != old['data_sha256']:
        raise ValueError('Source checkpoint digest mismatch')
    source = Path(__file__).resolve().parent
    for name, expected in old['sources'].items():
        if digest(source/name) != expected:
            raise ValueError(f'Frozen source differs from checkpoint: {name}')
    template_path = Path(old['template_cache']['pickle_file'])
    if digest(template_path) != old['template_cache']['pickle_sha256']:
        raise ValueError('Source compiled-template digest mismatch')
    with template_path.open('rb') as handle:
        template = pickle.load(handle)
    with np.load(source_data_path, allow_pickle=False) as data:
        saved = data['state']
        if saved.dtype != np.dtype('float64') or saved.ndim != 1:
            raise ValueError('Expected the original float64 scalar state')
        initial = saved.copy()
        if not np.array_equal(saved, initial) or state_digest(saved) != state_digest(initial):
            raise ValueError('Resume state is not an exact copy')
        angles, all_angles = data['angles'].copy(), data['all_query_angles'].copy()
        train_angles, labels = data['train_angles'].copy(), data['train_labels'].copy()
        old_core_ids, old_passive_ids = data['core_ids'].copy(), data['passive_ids'].copy()
        old_Fids = data['template_Fids'].copy()
        old_train_prediction = data['train_prediction'].copy()
        old_passive_prediction = data['all_passive_prediction'].copy()
    if len(angles) != 64 or not np.array_equal(all_angles, np.r_[angles, train_angles]):
        raise ValueError('Source does not contain exactly 64 probes and all training aliases')
    if not np.array_equal(template.labels, labels):
        raise ValueError('Cached template labels differ from the source checkpoint')
    model = SharedQueryClosure(template, all_angles)
    if (initial.shape != (model.size,) or not np.array_equal(model.core_ids, old_core_ids)
            or not np.array_equal(model.passive_ids, old_passive_ids)
            or not np.array_equal(template.Fids, old_Fids)):
        raise ValueError('Source checkpoint and cached template layouts differ')
    decoded = model.prediction(initial)
    passive_decoded = model.circle_prediction(initial)
    decode_error = max(float(np.max(np.abs(decoded-old_train_prediction))),
                       float(np.max(np.abs(passive_decoded-old_passive_prediction))))
    if decode_error != 0.:
        raise ValueError(f'Source checkpoint prediction decoder changed: {decode_error}')
    report = {'task': args.task, 'method': 'continued_selective_zero',
        'output_dependency_depth': args.output_depth, 'dependency_depth': 0,
        'preserve_essential': True, 'boundary': 'zero', 'k': 4, 'order': 1,
        'width_initial_pool': 1024, 'seed': 1, 'mark_bound': 3.,
        'target_mse': args.target_mse, 'target_rmse': float(np.sqrt(args.target_mse)),
        'source_physical_time': old['physical_time'],
        'physical_time_convention': 'source checkpoint time plus autonomous elapsed integration time',
        'circle_grid': 64, 'passive_train_aliases': len(labels),
        'primary_metric': 'raw circle RMS versus matched block at the new MSE threshold',
        'secondary_metric': 'raw circle RMS versus canonical Gaussian at the new MSE threshold',
        'compile_executed': False, 'initialization_executed': False,
        'resume': {'source_metadata_file': str(source_path),
            'source_metadata_sha256': digest(source_path),
            'source_checkpoint_file': str(source_data_path),
            'source_checkpoint_sha256': digest(source_data_path),
            'source_state_sha256': state_digest(initial),
            'initial_state_sha256': state_digest(initial),
            'state_copy_exact': True, 'source_target_mse': old['target_mse'],
            'source_train_mse': old['train_mse'], 'source_sources_verified': True,
            'compiled_template_file': str(template_path),
            'compiled_template_sha256': digest(template_path),
            'initial_prediction_decoder_error': decode_error},
        'state_counts': {'shared_core': model.ncore, 'passive_per_query': model.npassive,
            'circle_queries': 64, 'training_alias_queries': len(labels),
            'total_dynamic_scalars': model.size, 'single_query_template': len(template.trees)+1},
        'sources': {name: digest(source/name) for name in SOURCE_NAMES},
        'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'],
                        cwd=source.parent.parent, text=True).strip(),
        'environment': {'python': platform.python_version(), 'numpy': np.__version__,
                        'scipy': scipy.__version__, 'blas_threads': 1},
        'command': sys.argv, 'campaign_deadline_epoch': args.campaign_deadline,
        'solver': {'method': 'RK45', 'rtol': 1e-5, 'atol': 1e-7,
            'first_step': .01, 'max_step': 1., 'elapsed_physical_time_cap': 3000.,
            'training_wall_cap': 45.,
            'error_norm': 'maximum scaled RMS over core, each passive block, and clock'}}
    report['passive_independence'] = model.check_independence()
    report['vectorization_check'] = model.check_vectorization()
    report['initial_train_mse'] = float(np.mean((decoded-labels)**2))
    print(json.dumps({'phase': 'resume_verified', 'task': args.task,
        'output_depth': args.output_depth, 'scalars': model.size,
        'source_physical_time': old['physical_time'],
        'initial_train_mse': report['initial_train_mse'],
        'target_mse': args.target_mse}), flush=True)
    if not args.train:
        write_json(args.output/f'{tag}__preflight.json', report)
        return
    used_seconds = sum(json.loads(path.read_text()).get('training_seconds', 0.)
        for path in args.output.glob('*__selective_zero_out*.json')
        if not path.stem.endswith('__preflight'))
    remaining_wall = args.campaign_deadline-time.time() if args.campaign_deadline else float('inf')
    fit_seconds = min(45., 270.-used_seconds, remaining_wall)
    report['prior_continuation_training_seconds'] = used_seconds
    report['solver']['training_wall_cap'] = max(0., fit_seconds)
    if fit_seconds <= .25:
        report.update(stop_reason='campaign_budget', fitted=False, training_seconds=0.)
        write_json(report_path, report)
        return
    state, history_elapsed, info = integrate(model, initial, labels, fit_seconds,
                                             target=args.target_mse)
    report.update(info)
    report['elapsed_physical_time'] = info['physical_time']
    report['physical_time'] = old['physical_time']+info['physical_time']
    report['target_bracket_elapsed'] = info['target_bracket']
    report['target_bracket'] = ([old['physical_time']+x for x in info['target_bracket']]
                                if info['target_bracket'] else None)
    history = history_elapsed.copy()
    history[:, 0] += old['physical_time']
    core_prediction, passive_prediction = model.prediction(state), model.circle_prediction(state)
    circle_prediction, alias_prediction = passive_prediction[:64], passive_prediction[64:]
    gap = alias_prediction-core_prediction
    core_mse = float(np.mean((core_prediction-labels)**2))
    passive_mse = float(np.mean((alias_prediction-labels)**2))
    report.update(train_mse=core_mse, core_train_rmse=float(np.sqrt(core_mse)),
        passive_train_mse=passive_mse, passive_train_rmse=float(np.sqrt(passive_mse)),
        alias_gap_rms=float(np.sqrt(np.mean(gap*gap))), alias_gap_max=float(np.max(np.abs(gap))),
        train_prediction=core_prediction.tolist(), passive_train_prediction=alias_prediction.tolist(),
        final_max_abs_q=float(np.max(np.abs(state[:-1]))),
        final_clipped_fraction=float(np.mean(np.abs(state[:-1]) > 1.)),
        endpoint_status='fitted tighter-threshold endpoint' if report['fitted'] else 'partial continuation')
    for method, suffix in [('block', 'block_k4_P1_canonical'), ('gaussian', 'gaussian')]:
        path = args.references/f'{args.task}__{suffix}.npz'
        if path.exists() and path.with_suffix('.json').exists():
            reference_info = json.loads(path.with_suffix('.json').read_text())
            if reference_info['target_mse'] != args.target_mse:
                raise ValueError('Reference stop threshold does not match this continuation')
        report[f'{method}_comparison'] = reference_comparison(path, angles,
            circle_prediction, core_prediction, alias_prediction, report['fitted'])
    for method in ('block', 'gaussian'):
        report[f'core_train_prediction_rms_vs_{method}'] = report[f'{method}_comparison'].get('core_train_prediction_rms')
        report[f'passive_train_prediction_rms_vs_{method}'] = report[f'{method}_comparison'].get('passive_train_prediction_rms')
    report['history_columns'] = ['absolute_physical_time', 'core_train_mse', 'L',
                                'max_abs_q', 'fraction_outside_unit_box']
    np.savez_compressed(data_path, state=state, initial_state=initial,
        history=history, history_elapsed=history_elapsed, angles=angles,
        prediction=circle_prediction, all_query_angles=all_angles,
        all_passive_prediction=passive_prediction, train_prediction=core_prediction,
        passive_train_prediction=alias_prediction, alias_gap=gap,
        train_angles=train_angles, train_labels=labels, core_ids=model.core_ids,
        passive_ids=model.passive_ids, template_Fids=template.Fids)
    report.update(data_file=data_path.name, data_sha256=digest(data_path),
                  final_state_sha256=state_digest(state), total_seconds=time.monotonic()-started)
    write_json(report_path, report)
    print(json.dumps(report, allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
