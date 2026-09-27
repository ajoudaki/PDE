"""Width1024 seed1 block curve for overlay with the saved width2048 curve.

Exactly seven serial dense trajectories: Gaussian, its control, and five blocks.
"""
import quick_block_compare as quick  # Set BLAS threads before importing NumPy.

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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    baseline, out = args.baseline.resolve(), args.output.resolve()
    source = Path(__file__).resolve().parent
    old = json.loads((baseline/'manifest.json').read_text())
    if (old['width'], old['seed'], old['target_mse']) != (2048, 1, .001):
        raise ValueError('Expected width2048 seed1 MSE0.001 overlay baseline')
    for name in ('quick_block_compare.py', 'dense_compare.py',
                 'dense_wide_integrator.py', 'circle_tasks.py'):
        if quick.digest(source/name) != old['sources'][name]:
            raise ValueError(f'Source changed: {name}')
    out.mkdir(parents=True, exist_ok=False)
    snapshot = out/'source_snapshot'
    snapshot.mkdir()
    files = ('run_block_overlay.py', 'quick_block_compare.py', 'dense_compare.py',
             'dense_wide_integrator.py', 'circle_tasks.py')
    for name in files:
        shutil.copyfile(source/name, snapshot/name)
    methods = ('gaussian', 'gaussian_control', 'block8', 'block16',
               'block32', 'block64', 'block128')
    task = 'cluster_triple_cos9'
    manifest = {'width': 1024, 'seed': 1, 'task': task, 'target_mse': .001,
        'methods': methods, 'block_sizes': [8, 16, 32, 64, 128],
        'baseline': str(baseline),
        'baseline_manifest_sha256': quick.digest(baseline/'manifest.json'),
        'sources': {name: quick.digest(source/name) for name in files},
        'command': sys.argv, 'cwd': str(Path.cwd()), 'workers': 1, 'blas_threads': 1,
        'python': platform.python_version(), 'numpy': np.__version__,
        'scipy': scipy.__version__, 'machine': platform.platform(),
        'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
        'rtol': 1e-5, 'atol': 1e-8, 'deadline_seconds': 50, 'interrupt_seconds': 55,
        'per_run_ceiling_seconds': 60, 'grid': 2048,
        'initialization_streams': {'w': [1, 1], 'c': [1, 2],
            'gaussian': [1, 101], 'gaussian_control': [1, 102],
            **{f'block{k}': [1, 300+k] for k in (8, 16, 32, 64, 128)}}}
    quick.write_json(out/'manifest.json', manifest)
    started = time.monotonic()
    rows = []
    for method in methods:
        rows.append(quick.run_one((str(out), task, method, None, .001, 1024, 1, False)))
        quick.write_json(out/'results.json', rows)
    with np.load(out/rows[0]['data_file']) as data:
        reference, angles = data['prediction'], data['angles']
    comparisons = []
    for row in rows:
        with np.load(out/row['data_file']) as data:
            if not np.array_equal(data['angles'], angles):
                raise ValueError('Circle grids changed')
            error = data['prediction']-reference
        rms = float(np.sqrt(np.mean(error**2)))
        comparisons.append({'task': task, 'method': row['method'],
            'rms_vs_gaussian': rms,
            'quadrature_change': abs(rms-float(np.sqrt(np.mean(error[::2]**2)))),
            'fitted_pair': row['fitted'] and rows[0]['fitted'],
            'train_mse': row['train_mse'], 'new_run': True,
            'data_file': row['data_file'], 'source_directory': str(out),
            'data_sha256': row['data_sha256'], 'total_seconds': row['total_seconds']})
    quick.write_json(out/'comparisons.json', comparisons)
    quick.write_json(out/'completion.json', {'wall_seconds': time.monotonic()-started,
        'new_trajectories': len(rows), 'all_fitted': all(r['fitted'] for r in rows),
        'max_new_run_seconds': max(r['total_seconds'] for r in rows),
        'max_quadrature_change': max(r['quadrature_change'] for r in comparisons)})
    lines = ['# Clustered cosine-9: width1024 overlay', '',
        'Seed1, MSE0.001. All seven width1024 endpoints are new; width2048 is reused.', '',
        '| Initialization | Absolute circle RMS vs Gaussian | Fitted pair? |',
        '|---|---:|---|']
    for row in comparisons:
        lines.append(f"| {row['method']} | {row['rms_vs_gaussian']:.8f} | {row['fitted_pair']} |")
    lines += ['', 'One draw per method and width; same seed and initialization rules. '
        'Same seed does not make different-width matrices identical or fully nested. '
        'This is a finite-width comparison, not a population-limit claim.']
    if not all(r['fitted_pair'] for r in comparisons):
        lines += ['', 'PARTIAL: unfitted pairs must be excluded from matched-loss curves.']
    (out/'report.md').write_text('\n'.join(lines)+'\n')
    print((out/'report.md').read_text(), flush=True)


if __name__ == '__main__':
    main()
