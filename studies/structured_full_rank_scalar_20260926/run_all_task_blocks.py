"""One-seed width2048 block8/16/32 comparison across all twelve circle tasks.

Same unrestricted dense model and solver; exactly sixty serial trajectories.
"""
import quick_block_compare as quick  # Sets BLAS threads before NumPy.

import argparse
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time

import numpy as np
import scipy
from circle_tasks import TASKS, task_manifest

METHODS = ('gaussian', 'gaussian_control', 'block8', 'block16', 'block32')
WIDTH, SEED, TARGET = 2048, 1, .01


def analyze(out, rows):
    comparisons = []
    for task in TASKS:
        subset = {r['method']: r for r in rows if r['task'] == task.name}
        if 'gaussian' not in subset:
            continue
        with np.load(out/subset['gaussian']['data_file']) as data:
            reference, angles = data['prediction'], data['angles']
        for method in METHODS:
            if method not in subset:
                continue
            row = subset[method]
            with np.load(out/row['data_file']) as data:
                if not np.array_equal(data['angles'], angles):
                    raise ValueError('Circle grids changed')
                error = data['prediction']-reference
            rms = float(np.sqrt(np.mean(error**2)))
            comparisons.append({'task': task.name, 'method': method,
                'rms_vs_gaussian': rms,
                'quadrature_change': abs(rms-float(np.sqrt(np.mean(error[::2]**2)))),
                'fitted_pair': row['fitted'] and subset['gaussian']['fitted'],
                'train_mse': row['train_mse'], 'reference_train_mse': subset['gaussian']['train_mse'],
                'data_file': row['data_file'], 'source_directory': str(out),
                'data_sha256': row['data_sha256'], 'total_seconds': row['total_seconds']})
    quick.write_json(out/'comparisons.json', comparisons)
    return comparisons


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    out = args.output.resolve()
    source = Path(__file__).resolve().parent
    out.mkdir(parents=True, exist_ok=False)
    snapshot = out/'source_snapshot'
    snapshot.mkdir()
    files = ('run_all_task_blocks.py', 'quick_block_compare.py', 'dense_compare.py',
             'dense_wide_integrator.py', 'circle_tasks.py')
    for name in files:
        shutil.copyfile(source/name, snapshot/name)
    manifest = {'width': WIDTH, 'seed': SEED, 'tasks': [t.name for t in TASKS],
        'training_data': task_manifest(), 'target_mse': TARGET, 'methods': METHODS,
        'block_sizes': [8, 16, 32], 'expected_trajectories': len(TASKS)*len(METHODS),
        'sources': {name: quick.digest(source/name) for name in files},
        'command': sys.argv, 'cwd': str(Path.cwd()), 'workers': 1, 'blas_threads': 1,
        'python': platform.python_version(), 'numpy': np.__version__,
        'scipy': scipy.__version__, 'machine': platform.platform(),
        'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
        'rtol': 1e-5, 'atol': 1e-8, 'deadline_seconds': 50, 'interrupt_seconds': 55,
        'per_run_ceiling_seconds': 60, 'grid': 2048,
        'initialization_streams': {'w': [SEED, 1], 'c': [SEED, 2],
            'gaussian': [SEED, 101], 'gaussian_control': [SEED, 102],
            **{f'block{k}': [SEED, 300+k] for k in (8, 16, 32)}}}
    quick.write_json(out/'manifest.json', manifest)
    started = time.monotonic()
    rows = []
    for task in TASKS:
        for method in METHODS:
            rows.append(quick.run_one((str(out), task.name, method, None,
                                       TARGET, WIDTH, SEED, False)))
            quick.write_json(out/'results.json', rows)
            # Persist available comparisons throughout the run, including partials.
            analyze(out, rows)
        print(json.dumps({'task_complete': task.name, 'completed_runs': len(rows),
            'fitted_runs': sum(r['fitted'] for r in rows),
            'batch_seconds': time.monotonic()-started}), flush=True)
    comparisons = analyze(out, rows)
    quick.write_json(out/'completion.json', {'wall_seconds': time.monotonic()-started,
        'new_trajectories': len(rows), 'all_fitted': all(r['fitted'] for r in rows),
        'fitted_trajectories': sum(r['fitted'] for r in rows),
        'max_new_run_seconds': max(r['total_seconds'] for r in rows),
        'max_quadrature_change': max(r['quadrature_change'] for r in comparisons)})
    lines = ['# All circle tasks: width2048 block-size curves', '',
        'Seed1, first training MSE0.01 crossing, unchanged unrestricted dense flow.',
        'Metric: absolute RMS of fitted function minus same-task Gaussian around2048 circle angles.', '',
        '| Task | Gaussian control | Block8 | Block16 | Block32 |',
        '|---|---:|---:|---:|---:|']
    for task in TASKS:
        subset = {r['method']: r for r in comparisons if r['task'] == task.name}
        values = [f"{subset[m]['rms_vs_gaussian']:.8f}" if subset[m]['fitted_pair']
                  else 'not fitted' for m in METHODS[1:]]
        lines.append('| '+task.name+' | '+' | '.join(values)+' |')
    lines += ['', 'One draw per method, matched outer initialization. '
        'Gaussian control changes only middle initialization. '
        'This checks finite-width predictors, not a population limit or scalar closure.',
        'Nonfitted pairs are retained as partial diagnostics in JSON but excluded from fitted curves.']
    (out/'report.md').write_text('\n'.join(lines)+'\n')
    print((out/'report.md').read_text(), flush=True)


if __name__ == '__main__':
    main()
