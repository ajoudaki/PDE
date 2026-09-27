"""Fill block16 and block64 using an existing n2048 seed1 comparison.

Exactly two serial training trajectories; all other fitted states are reused.
"""
import quick_block_compare as quick  # Sets single-thread BLAS before NumPy.

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
    old_manifest = json.loads((baseline/'manifest.json').read_text())
    if (old_manifest['width'], old_manifest['seed'], old_manifest['target_mse']) != (2048, 1, .001):
        raise ValueError('Expected the completed n2048 seed1 MSE0.001 baseline')
    for name in ('dense_compare.py', 'dense_wide_integrator.py', 'circle_tasks.py'):
        if quick.digest(source/name) != old_manifest['sources'][name]:
            raise ValueError(f'Canonical source changed: {name}')
    task = 'cluster_triple_cos9'
    old_rows = {r['method']: r for r in json.loads((baseline/'results.json').read_text())}
    for row in old_rows.values():
        if not row['fitted'] or quick.digest(baseline/row['data_file']) != row['data_sha256']:
            raise ValueError('Expected intact fitted baseline states')
    out.mkdir(parents=True, exist_ok=False)
    snapshot = out/'source_snapshot'
    snapshot.mkdir()
    files = ('fill_block_sizes.py', 'quick_block_compare.py', 'dense_compare.py',
             'dense_wide_integrator.py', 'circle_tasks.py')
    for name in files:
        shutil.copyfile(source/name, snapshot/name)
    manifest = {'width': 2048, 'seed': 1, 'task': task, 'target_mse': .001,
        'new_methods': ['block16', 'block64'], 'block_sizes': [8,16,32,64,128],
        'baseline': str(baseline), 'baseline_manifest_sha256': quick.digest(baseline/'manifest.json'),
        'old_data_hashes': {k: v['data_sha256'] for k,v in old_rows.items()},
        'sources': {name: quick.digest(source/name) for name in files},
        'command': sys.argv, 'cwd': str(Path.cwd()), 'workers': 1, 'blas_threads': 1,
        'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__,
        'head': subprocess.check_output(['git','rev-parse','HEAD'], text=True).strip(),
        'rtol': 1e-5, 'atol': 1e-8, 'deadline_seconds': 50, 'interrupt_seconds': 55,
        'grid': 2048, 'initialization_streams': {'block16': [1,316], 'block64': [1,364]}}
    quick.write_json(out/'manifest.json', manifest)
    started = time.monotonic()
    rows = []
    for method in manifest['new_methods']:
        rows.append(quick.run_one((str(out), task, method, None, .001, 2048, 1, False)))
        quick.write_json(out/'results.json', rows)
    new_rows = {r['method']: r for r in rows}
    with np.load(baseline/old_rows['gaussian']['data_file']) as data:
        reference, angles = data['prediction'], data['angles']
    methods = ('gaussian_control','hd','block8','block16','block32','block64','block128')
    comparisons = []
    for method in methods:
        fresh = method in new_rows
        row = new_rows[method] if fresh else old_rows[method]
        directory = out if fresh else baseline
        with np.load(directory/row['data_file']) as data:
            if not np.array_equal(data['angles'], angles):
                raise ValueError('Circle grids changed')
            error = data['prediction']-reference
        rms = float(np.sqrt(np.mean(error**2)))
        comparisons.append({'method': method, 'rms_vs_gaussian': rms,
            'quadrature_change': abs(rms-float(np.sqrt(np.mean(error[::2]**2)))),
            'fitted_pair': row['fitted'] and old_rows['gaussian']['fitted'],
            'train_mse': row['train_mse'], 'new_run': fresh,
            'data_file': row['data_file'], 'source_directory': str(directory),
            'data_sha256': row['data_sha256'], 'total_seconds': row['total_seconds']})
    quick.write_json(out/'comparisons.json', comparisons)
    quick.write_json(out/'completion.json', {'wall_seconds': time.monotonic()-started,
        'new_trajectories': len(rows), 'all_fitted': all(r['fitted_pair'] for r in comparisons),
        'max_new_run_seconds': max(r['total_seconds'] for r in rows),
        'max_quadrature_change': max(r['quadrature_change'] for r in comparisons)})
    lines = ['# Clustered cosine-9: intermediate block sizes', '',
             'Width2048, seed1, MSE0.001. Only block16 and block64 are new runs.', '',
             '| Initialization | Absolute circle RMS vs Gaussian | New training? |',
             '|---|---:|---|']
    for row in comparisons:
        lines.append(f"| {row['method']} | {row['rms_vs_gaussian']:.8f} | {row['new_run']} |")
    if not all(r['fitted_pair'] for r in comparisons):
        lines += ['', 'PARTIAL: comparisons involving an unfitted endpoint are not matched-loss results.']
    lines += ['', 'One realization per block size. Distinct block-size streams remain; '
              'this checks the saved-seed curve, not seed independence or a population order law.']
    (out/'report.md').write_text('\n'.join(lines)+'\n')
    print((out/'report.md').read_text(), flush=True)


if __name__ == '__main__':
    main()
