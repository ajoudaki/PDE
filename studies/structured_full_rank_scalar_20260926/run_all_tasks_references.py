"""Reuse, continue, or freshly fit the exact matching all-task references.

Inventory is read-only. Training requires --run and an explicit cumulative
budget; existing checkpoints are never overwritten or resumed unnecessarily.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
from contextlib import redirect_stdout
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace

import numpy as np
import circle_tasks
import geometry_tasks
import true_aggregate_references as refs
import continue_selective_references as continuation


STUDY = Path(__file__).resolve().parent
DATA = STUDY.parents[1]/'data/generated/structured_full_rank_scalar_20260926'
ALL_TASKS = dict(circle_tasks.BY_NAME)
ALL_TASKS.update(geometry_tasks.BY_NAME)
TAGS = ('gaussian', 'block_k4_P1_canonical')
TARGET = .001


def inventory(output):
    choices = {(name, tag): [] for name in ALL_TASKS for tag in TAGS}
    for path in DATA.rglob('*.json'):
        if output in path.parents or path.stat().st_size > 2_000_000:
            continue
        try:
            row = json.loads(path.read_text())
        except (ValueError, OSError):
            continue
        if not isinstance(row, dict) or row.get('task') not in ALL_TASKS:
            continue
        if row.get('width') != 1024 or row.get('seed') != 1:
            continue
        tag = ('gaussian' if row.get('method') == 'gaussian' else
               'block_k4_P1_canonical' if row.get('tag') == 'block_k4_P1_canonical' else None)
        if tag is None or not row.get('fitted') or not row.get('data_file'):
            continue
        target = row.get('target_mse')
        if target is None or target < TARGET or row['train_mse'] < TARGET*(1-1e-6):
            continue
        data_path = path.parent/row['data_file']
        if not data_path.exists():
            continue
        choices[row['task'], tag].append((target, len(str(data_path)), str(data_path), path))
    selected = []
    for task in ALL_TASKS:
        for tag in TAGS:
            options = sorted(choices[task, tag])
            if not options:
                selected.append({'task': task, 'tag': tag, 'action': 'fresh',
                                 'source_checkpoint': None})
                continue
            _, _, data_path, report_path = options[0]
            row = json.loads(report_path.read_text())
            entry = {'task': task, 'tag': tag,
                'action': 'reuse' if row['target_mse'] == TARGET else 'continue',
                'source_checkpoint': data_path, 'source_report': str(report_path),
                'source_target_mse': row['target_mse'], 'source_train_mse': row['train_mse'],
                'source_physical_time': row['physical_time']}
            _, _, _, checked = load_existing(entry)
            entry.update(checked)
            selected.append(entry)
    return selected


def load_existing(entry):
    path = Path(entry['source_checkpoint'])
    old = json.loads(path.with_suffix('.json').read_text())
    source_hash = refs.digest(path)
    if source_hash != old['data_sha256']:
        raise ValueError(f'Checkpoint hash mismatch: {path}')
    task = ALL_TASKS[entry['task']]
    with np.load(path, allow_pickle=False) as saved:
        if not (np.array_equal(saved['train_angles'], np.asarray(task.angles))
                and np.array_equal(saved['train_labels'], task.target(task.angles))):
            raise ValueError('Reference task mismatch')
        if entry['tag'] == 'gaussian':
            model = refs.GaussianCheckpoint(refs.dense.State(saved['w'], saved['W'], saved['c']))
            if model.state.width != 1024:
                raise ValueError('Reference width mismatch')
        else:
            q, k, m, order, d = map(int, saved['layout'])
            if (q*k, k, m, order, d) != (1024, 4, len(task.angles), 1, 2):
                raise ValueError('Block reference layout mismatch')
            model = refs.BlockMemoryCheckpoint(refs.block.Layout(q, k, m, order, d),
                                               saved['G'], saved['vector'])
        history = saved['history'].copy()
    arrays = continuation.state_arrays(model)
    if not all(np.all(np.isfinite(value)) for value in arrays.values()):
        raise ValueError('Nonfinite checkpoint')
    mse = float(np.mean((model.predict(task.angles)-task.target(task.angles))**2))
    if abs(mse-old['train_mse']) > 1e-12:
        raise ValueError('Checkpoint MSE mismatch')
    provenance = {'task': entry['task'], 'tag': entry['tag'],
        'source_checkpoint': str(path.resolve()), 'source_checkpoint_sha256': source_hash,
        'source_report_sha256': refs.digest(path.with_suffix('.json')),
        'continuation_start_time': old['physical_time'], 'continuation_start_mse': mse,
        'start_state_array_sha256': {key: continuation.array_hash(value) for key, value in arrays.items()},
        'start_state_array_shapes': {key: list(value.shape) for key, value in arrays.items()},
        'continuation_start_L': None if entry['tag'] == 'gaussian' else float(model.vector[-1]),
        'initialization_called': False}
    return model, old, history, provenance


def reuse(entry, output, manifest_hash):
    started = time.monotonic()
    model, old, history, provenance = load_existing(entry)
    task = ALL_TASKS[entry['task']]
    angles = 2*np.pi*np.arange(256)/256
    prediction = model.predict(angles)
    train_prediction = model.predict(task.angles)
    path = output/f"{entry['task']}__{entry['tag']}.npz"
    np.savez(path, kind='gaussian' if entry['tag'] == 'gaussian' else 'block_memory',
        angles=angles, prediction=prediction, train_angles=np.asarray(task.angles),
        train_labels=task.target(task.angles), train_prediction=train_prediction,
        history=history, **continuation.state_arrays(model))
    return {**provenance, 'method': old['method'], 'width': 1024, 'seed': 1,
        'target_mse': TARGET, 'grid': 256, 'train_mse': old['train_mse'],
        'fitted': True, 'physical_time': old['physical_time'],
        'continuation_elapsed_time': 0., 'stop_reason': 'reused_target_checkpoint',
        'training_seconds': 0., 'nfev': 0, 'nsteps': 0,
        'source_manifest_current_sha256': manifest_hash,
        'data_file': path.name, 'data_sha256': refs.digest(path),
        'total_seconds': time.monotonic()-started}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DATA/'all_tasks_j2_20260927/references')
    parser.add_argument('--run', action='store_true')
    parser.add_argument('--tasks', nargs='+', choices=tuple(ALL_TASKS),
                        help='Explicit task subset; omitted tasks are recorded but never run')
    parser.add_argument('--fit-seconds', type=float, default=44.)
    parser.add_argument('--training-budget', type=float)
    parser.add_argument('--campaign-deadline-unix', type=float)
    args = parser.parse_args()
    if not 1 < args.fit_seconds <= 45:
        parser.error('Invalid per-fit budget')
    if args.run and (args.training_budget is None or args.training_budget <= 0):
        parser.error('Running requires an explicit positive training budget')
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    full_inventory = inventory(output)
    refs.write_json(output/'inventory.json', full_inventory)
    selected_tasks = tuple(dict.fromkeys(args.tasks)) if args.tasks else tuple(ALL_TASKS)
    plan = [row for name in selected_tasks for row in full_inventory if row['task'] == name]
    refs.write_json(output/'selected_inventory.json', plan)
    selection = {'selected_tasks': selected_tasks,
        'not_selected_tasks': [name for name in ALL_TASKS if name not in selected_tasks],
        'not_selected_reason': 'user requested representative configurations without similar extra cases',
        'training_for_unselected_tasks': False}
    refs.write_json(output/'selection.json', selection)
    counts = {action: sum(row['action'] == action for row in plan)
              for action in ('reuse', 'continue', 'fresh')}
    print(json.dumps({'phase': 'inventory', 'counts': counts, 'tasks': len(selected_tasks),
                      'not_selected_tasks': selection['not_selected_tasks']}), flush=True)
    if not args.run:
        return
    if (output/'manifest.json').exists():
        raise FileExistsError('Campaign already launched; no reruns')
    for row in plan:
        for suffix in ('.npz', '.json'):
            if (output/f"{row['task']}__{row['tag']}{suffix}").exists():
                raise FileExistsError('Reference output already exists')
    refs.BY_NAME.update(ALL_TASKS)
    continuation.geometry_tasks.BY_NAME.update(ALL_TASKS)
    started = time.time()
    source_names = ('run_all_tasks_references.py', 'continue_selective_references.py',
        'true_aggregate_references.py', 'dense_compare.py', 'dense_wide_integrator.py',
        'block_scalar_closure.py', 'circle_tasks.py', 'geometry_tasks.py')
    manifest = {'started_utc': datetime.fromtimestamp(started, timezone.utc).isoformat(),
        'started_unix': started, 'target_mse': TARGET, 'grid': 256, 'width': 1024,
        'seed': 1, 'k': 4, 'order': 1, 'fit_seconds': args.fit_seconds,
        'training_budget': args.training_budget, 'campaign_deadline_unix': args.campaign_deadline_unix,
        'inventory_sha256': refs.digest(output/'inventory.json'), 'counts': counts,
        'selected_inventory_sha256': refs.digest(output/'selected_inventory.json'),
        'selection': selection,
        'tasks': {name: {'angles': task.angles, 'labels': task.target(task.angles).tolist()}
                  for name, task in ALL_TASKS.items() if name in selected_tasks},
        'sources': {name: refs.digest(STUDY/name) for name in source_names},
        'command': sys.argv, 'blas_threads': 1}
    refs.write_json(output/'manifest.json', manifest)
    manifest_hash = refs.digest(output/'manifest.json')
    rows = []
    # Gaussian references first, then matched blocks, while preserving task order.
    for tag in TAGS:
        for entry in (row for row in plan if row['tag'] == tag):
            remaining = args.training_budget-sum(row['training_seconds'] for row in rows)
            if args.campaign_deadline_unix is not None:
                remaining = min(remaining, args.campaign_deadline_unix-time.time()-1.)
            cap = min(args.fit_seconds, remaining-.05)
            if entry['action'] == 'reuse':
                row = reuse(entry, output, manifest_hash)
            elif cap <= 1.:
                row = {'task': entry['task'], 'tag': tag, 'fitted': False,
                    'stop_reason': 'campaign_budget', 'training_seconds': 0., 'data_file': None}
            elif entry['action'] == 'continue':
                previous_loader = continuation.load_source
                continuation.load_source = lambda root, task, method: load_existing(entry)
                try:
                    with redirect_stdout(io.StringIO()):
                        row = continuation.run_one(Path(entry['source_checkpoint']).parent,
                            output, entry['task'], tag, TARGET, cap, manifest_hash)
                finally:
                    continuation.load_source = previous_loader
            else:
                options = SimpleNamespace(kind='gaussian' if tag == 'gaussian' else 'block_memory',
                    tag=tag, output=output, width=1024, seed=1, target=TARGET, grid=256,
                    fit_seconds=cap, k=4, order=1, readout='canonical')
                with redirect_stdout(io.StringIO()):
                    row = refs.run_one(entry['task'], options, manifest_hash)
                row['initialization_called'] = True
            row['reference_action'] = entry['action']
            refs.write_json(output/f"{entry['task']}__{tag}.json", row)
            rows.append(row)
            refs.write_json(output/'results.json', rows)
            print(json.dumps({key: row.get(key) for key in ('task', 'tag', 'reference_action',
                'fitted', 'train_mse', 'stop_reason', 'training_seconds', 'physical_time', 'data_file')}), flush=True)
    refs.write_json(output/'completion.json', {'runs': len(rows), 'counts': counts,
        'all_fitted': all(row['fitted'] for row in rows),
        'training_seconds': sum(row['training_seconds'] for row in rows),
        'wall_seconds': time.time()-started, 'reruns': 0})


if __name__ == '__main__':
    main()
