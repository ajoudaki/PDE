"""Continue complete saved Gaussian and block-memory reference states.

No initialization is called. Original checkpoints are read-only. The target
must be supplied explicitly; --inspect-only verifies inputs without training.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import signal
import sys
import time

import numpy as np

import geometry_tasks
import true_aggregate_references as refs
import dense_wide_integrator as wide
import block_scalar_closure as block


TASKS = ('pair_orthogonal_cos1', 'cluster_triple_cos1', 'triple_wide_mixed')
TAGS = ('gaussian', 'block_k4_P1_canonical')
SOURCE_NAMES = ('continue_selective_references.py', 'true_aggregate_references.py',
                'dense_wide_integrator.py', 'block_scalar_closure.py',
                'run_geometry_references.py', 'geometry_tasks.py')


def array_hash(value):
    return hashlib.sha256(np.ascontiguousarray(value).tobytes()).hexdigest()


def state_arrays(model):
    if isinstance(model, refs.GaussianCheckpoint):
        return {'w': model.state.w, 'W': model.state.W, 'c': model.state.c}
    return {'G': model.G, 'vector': model.vector,
        'layout': np.asarray([model.layout.q, model.layout.k, model.layout.m,
                              model.layout.order, model.layout.d])}


def load_source(root, task_name, tag):
    path = root/f'{task_name}__{tag}.npz'
    metadata = json.loads(path.with_suffix('.json').read_text())
    checkpoint_hash = refs.digest(path)
    if checkpoint_hash != metadata['data_sha256'] or not metadata['fitted']:
        raise ValueError('Continuation requires an intact fitted checkpoint')
    if metadata['width'] != 1024 or metadata['seed'] != 1:
        raise ValueError('Unexpected initialization width or seed')
    task = geometry_tasks.BY_NAME[task_name]
    model = refs.load_checkpoint(path)
    with np.load(path, allow_pickle=False) as saved:
        if not (np.array_equal(saved['train_angles'], np.asarray(task.angles))
                and np.array_equal(saved['train_labels'], task.target(task.angles))):
            raise ValueError('Saved training task differs from frozen definition')
        history = saved['history'].copy()
    arrays = state_arrays(model)
    if not all(np.all(np.isfinite(value)) for value in arrays.values()):
        raise ValueError('Nonfinite source state')
    if tag != 'gaussian' and (model.layout.n != 1024 or model.layout.k != 4
                              or model.layout.order != 1):
        raise ValueError('Unexpected block dimensions')
    prediction = model.predict(task.angles)
    mse = float(np.mean((prediction-task.target(task.angles))**2))
    if abs(mse-metadata['train_mse']) > 1e-13:
        raise ValueError('Saved state does not reproduce source training MSE')
    source_manifest = root/f'manifest_{tag}.json'
    if refs.digest(source_manifest) != metadata['source_manifest_sha256']:
        raise ValueError('Source manifest hash mismatch')
    info = {'task': task_name, 'tag': tag,
        'source_checkpoint': str(path.resolve()), 'source_checkpoint_sha256': checkpoint_hash,
        'source_report_sha256': refs.digest(path.with_suffix('.json')),
        'source_manifest_sha256': refs.digest(source_manifest),
        'continuation_start_time': metadata['physical_time'],
        'continuation_start_mse': mse,
        'start_state_array_sha256': {name: array_hash(value) for name, value in arrays.items()},
        'start_state_array_shapes': {name: list(value.shape) for name, value in arrays.items()},
        'continuation_start_L': None if tag == 'gaussian' else float(model.vector[-1]),
        'initialization_called': False}
    return model, metadata, history, info


class TrainingBudget(Exception):
    pass


def continue_gaussian(model, task, target, seconds, physical_start):
    u, labels = task.data()
    accepted = [0., model.state, float(np.mean((model.predict(task.angles)-labels)**2))]
    history, count = [], [0]
    original_rhs = wide.flat_rhs

    def rhs(*values):
        count[0] += 1
        return original_rhs(*values)

    def callback(at, state, mse):
        accepted[:] = [at, state, mse]
        history.append((at, mse))

    def alarm(signum, frame):
        raise TrainingBudget()

    old_handler = signal.signal(signal.SIGALRM, alarm)
    wide.flat_rhs = rhs
    started = time.monotonic()
    signal.setitimer(signal.ITIMER_REAL, seconds)
    result = None
    try:
        result = wide.integrate(model.state, u, labels, time_cap=max(0., 3000.-physical_start),
            rtol=1e-5, atol=1e-8, target_train_mse=target, max_step=10.,
            deadline=time.time()+max(.1, seconds-1.), callback=callback)
        elapsed_time, state, mse = result.time, result.state, result.train_mse
        reason = result.stop_reason
    except TrainingBudget:
        elapsed_time, state, mse = accepted
        reason = 'training_wall_limit'
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.)
        signal.signal(signal.SIGALRM, old_handler)
        wide.flat_rhs = original_rhs
    info = {'continuation_elapsed_time': elapsed_time, 'train_mse': mse,
        'stop_reason': reason, 'nfev': count[0],
        'nsteps': result.nsteps if result else max(0, len(history)-1),
        'max_loss_rise': result.max_loss_rise if result else
            max([0.]+[b[1]-a[1] for a,b in zip(history, history[1:])]),
        'continuation_target_bracket': result.first_target_bracket if result else None,
        'training_seconds': time.monotonic()-started,
        'solver': result.settings if result else None}
    return refs.GaussianCheckpoint(state), np.asarray(history), info


def continue_block(model, task, target, seconds, physical_start):
    u, labels = task.data()
    vector, info = block.integrate(model.layout, model.G, model.vector, u, labels,
        target=target, rtol=1e-5, atol=1e-8, deadline_seconds=seconds-1.,
        interrupt_seconds=seconds, time_cap=max(0., 3000.-physical_start))
    history = info.pop('history')
    info['continuation_elapsed_time'] = info.pop('physical_time')
    info['continuation_target_bracket'] = info.pop('target_bracket')
    info['final_L'] = float(vector[-1])
    return refs.BlockMemoryCheckpoint(model.layout, model.G, vector), history, info


def run_one(root, output, task_name, tag, target, seconds, manifest_hash):
    started = time.monotonic()
    model, old, old_history, provenance = load_source(root, task_name, tag)
    task = geometry_tasks.BY_NAME[task_name]
    physical_start = provenance['continuation_start_time']
    evolve = continue_gaussian if tag == 'gaussian' else continue_block
    model, history, info = evolve(model, task, target, seconds, physical_start)
    elapsed_time = info['continuation_elapsed_time']
    history[:, 0] += physical_start
    combined_history = np.vstack((old_history, history[1:]))
    angles = 2*np.pi*np.arange(256)/256
    prediction = model.predict(angles)
    train_prediction = model.predict(task.angles)
    labels = task.target(task.angles)
    mse = float(np.mean((train_prediction-labels)**2))
    fitted = info['stop_reason'] == 'target' and mse <= target*(1+1e-7)
    arrays = state_arrays(model)
    path = output/f'{task_name}__{tag}.npz'
    np.savez(path, kind='gaussian' if tag == 'gaussian' else 'block_memory',
        angles=angles, prediction=prediction, train_angles=np.asarray(task.angles),
        train_prediction=train_prediction, train_labels=labels,
        history=combined_history, continuation_history=history, **arrays)
    bracket = info.get('continuation_target_bracket')
    row = {**provenance, **info, 'method': old['method'], 'width': 1024, 'seed': 1,
        'k': None if tag == 'gaussian' else 4, 'order': None if tag == 'gaussian' else 1,
        'target_mse': target, 'grid': 256, 'train_mse': mse, 'fitted': fitted,
        'physical_time': physical_start+elapsed_time,
        'target_bracket': [physical_start+t for t in bracket] if bracket is not None else None,
        'endpoint_status': 'fitted tighter threshold endpoint' if fitted else 'partial continuation endpoint',
        'source_manifest_current_sha256': manifest_hash,
        'data_file': path.name, 'data_sha256': refs.digest(path),
        'final_state_array_sha256': {name: array_hash(value) for name, value in arrays.items()},
        'total_seconds': time.monotonic()-started}
    if refs.digest(provenance['source_checkpoint']) != provenance['source_checkpoint_sha256']:
        raise ValueError('Source checkpoint was modified during continuation')
    refs.write_json(path.with_suffix('.json'), row)
    print(json.dumps(row, allow_nan=False), flush=True)
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=Path('data/generated/structured_full_rank_scalar_20260926/selective_geometry_20260927/references'))
    parser.add_argument('--output', type=Path, default=Path('data/generated/structured_full_rank_scalar_20260926/selective_tighter_20260927/references'))
    parser.add_argument('--target', type=float)
    parser.add_argument('--fit-seconds', type=float, default=44.)
    parser.add_argument('--inspect-only', action='store_true')
    args = parser.parse_args()
    if not 1 < args.fit_seconds <= 45:
        parser.error('Fit cap must be between 1 and 45 seconds')
    if not args.inspect_only and not (args.target is not None and 0 < args.target < .01):
        parser.error('Supply an explicit target MSE between zero and .01')
    args.output.mkdir(parents=True, exist_ok=True)
    jobs = [(task, tag) for tag in TAGS for task in TASKS]
    preflight = [load_source(args.source, task, tag)[3] for task, tag in jobs]
    if args.inspect_only:
        refs.write_json(args.output/'preflight.json', preflight)
        print(json.dumps(preflight, indent=2), flush=True)
        return
    reserved = [args.output/'manifest.json']
    reserved += [args.output/f'{task}__{tag}{suffix}' for task, tag in jobs
                 for suffix in ('.npz', '.json')]
    if any(path.exists() for path in reserved):
        raise FileExistsError('Continuation results already exist; no reruns')
    source = Path(__file__).resolve().parent
    manifest = {'started_utc': datetime.now(timezone.utc).isoformat(),
        'task_names': TASKS, 'tags': TAGS, 'target_mse': args.target,
        'fit_seconds': args.fit_seconds, 'width': 1024, 'seed': 1, 'k': 4, 'order': 1,
        'grid': 256, 'source_directory': str(args.source.resolve()),
        'sources': {name: refs.digest(source/name) for name in SOURCE_NAMES},
        'preflight': preflight, 'command': sys.argv, 'blas_threads': 1,
        'continuation_policy': 'load complete saved state; no initialization; original physical clock and field',
        'state_array_hash_format': 'SHA256 of C-contiguous NumPy array bytes; dtype and shape from checkpoint'}
    manifest_path = args.output/'manifest.json'
    refs.write_json(manifest_path, manifest)
    started = time.monotonic()
    rows = []
    for task, tag in jobs:
        rows.append(run_one(args.source, args.output, task, tag, args.target,
                            args.fit_seconds, refs.digest(manifest_path)))
        refs.write_json(args.output/'results.json', rows)
    refs.write_json(args.output/'completion.json', {
        'runs': len(rows), 'all_fitted': all(row['fitted'] for row in rows),
        'training_seconds': sum(row['training_seconds'] for row in rows),
        'wall_seconds': time.monotonic()-started, 'target_mse': args.target,
        'reinitializations': 0, 'reruns': 0})


if __name__ == '__main__':
    main()
