"""Register frozen geometry tasks in memory and run bounded references.

Existing task/solver modules are untouched. Both methods share an eight-minute
cumulative training budget and the twelve-minute campaign wall deadline.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'

from datetime import datetime, timezone
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

import geometry_tasks
import true_aggregate_references as refs


def main():
    output = Path('data/generated/structured_full_rank_scalar_20260926/selective_geometry_20260927/references').resolve()
    output.mkdir(parents=True, exist_ok=True)
    registration_path = output/'registration_manifest.json'
    if registration_path.exists():
        raise FileExistsError('No reference campaign reruns')
    refs.BY_NAME.update(geometry_tasks.BY_NAME)
    refs.TASK_NAMES = geometry_tasks.TASK_NAMES
    refs.SOURCE_NAMES += ('geometry_tasks.py', 'run_geometry_references.py')
    began = time.time()
    started_utc = datetime.fromtimestamp(began, timezone.utc).isoformat()
    source = Path(__file__).resolve().parent
    registration = {'started_utc': started_utc, 'started_unix': began,
        'tasks': geometry_tasks.manifest(), 'width': 1024, 'seed': 1,
        'target_mse': .01, 'grid': 256, 'k': 4, 'order': 1,
        'per_run_training_cap_seconds': 44.,
        'cumulative_training_cap_seconds': 480.,
        'campaign_wall_cap_seconds': 720.,
        'task_registration': 'process-local BY_NAME and TASK_NAMES; existing modules unchanged',
        'source_hashes': {name: refs.digest(source/name) for name in refs.SOURCE_NAMES},
        'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
        'python': platform.python_version(), 'blas_threads': 1,
        'command': sys.argv.copy()}
    refs.write_json(registration_path, registration)
    print(json.dumps({'phase': 'reference_campaign_start', 'started_utc': started_utc,
                      'started_unix': began}), flush=True)
    original_run = refs.run_one
    completed = []

    def bounded_run(task, args, manifest_hash):
        used = sum(row['training_seconds'] for row in completed)
        remaining_training = 480.-used
        remaining_wall = began+720.-time.time()
        cap = min(44., remaining_training-.05, remaining_wall-1.)
        if cap < .25:
            row = {'task': task, 'method': args.kind, 'tag': args.tag,
                'fitted': False, 'endpoint_status': 'not started; campaign budget',
                'stop_reason': 'campaign_budget', 'training_seconds': 0.,
                'total_seconds': 0., 'data_file': None,
                'source_manifest_sha256': manifest_hash}
            refs.write_json(output/f'{task}__{args.tag}.json', row)
            print(json.dumps(row), flush=True)
        else:
            args.fit_seconds = cap
            row = original_run(task, args, manifest_hash)
        completed.append(row)
        refs.write_json(output/'campaign_progress.json', {
            'started_utc': started_utc, 'runs_recorded': len(completed),
            'training_seconds': sum(r['training_seconds'] for r in completed),
            'wall_seconds': time.time()-began, 'rows': completed})
        return row

    refs.run_one = bounded_run
    for kind in ('gaussian', 'block_memory'):
        sys.argv = [str(Path(__file__).resolve()), '--kind', kind,
                    '--output', str(output), '--width', '1024', '--seed', '1',
                    '--target', '.01', '--grid', '256', '--fit-seconds', '44',
                    '--k', '4', '--order', '1', '--readout', 'canonical',
                    '--tasks', *geometry_tasks.TASK_NAMES]
        refs.main()
    refs.write_json(output/'campaign_completion.json', {
        'started_utc': started_utc, 'runs': len(completed),
        'all_fitted': all(row['fitted'] for row in completed),
        'training_seconds': sum(row['training_seconds'] for row in completed),
        'wall_seconds': time.time()-began, 'reruns': 0})


if __name__ == '__main__':
    main()
