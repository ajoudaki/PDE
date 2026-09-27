"""Run the remaining nine tasks with the unchanged moving-block closure."""
import block_scalar_closure as scalar
import argparse
import json
from pathlib import Path
import platform
import shutil
import sys
import time

import numpy as np
import scipy
from circle_tasks import BY_NAME
from run_block_scalar_closure import COUNTS, SUBSETS, digest, write, rms

TASKS = ('pair_cos1', 'pair_cos3', 'triple_cos3', 'triple_mixed',
         'broad_ridge6', 'sharp_ridge8', 'alternating3', 'alternating9',
         'multiscale12')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('baseline', 'previous', 'output'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    baseline, previous, out = (getattr(args, n).resolve() for n in ('baseline', 'previous', 'output'))
    source = Path(__file__).resolve().parent
    old = json.loads((baseline/'manifest.json').read_text())
    prior = json.loads((previous/'manifest.json').read_text())
    assert (old['width'], old['seed'], old['target_mse']) == (2048, 1, .01)
    assert digest(source/'block_scalar_closure.py') == prior['sources']['block_scalar_closure.py']
    for name in ('dense_compare.py', 'dense_wide_integrator.py', 'circle_tasks.py'):
        assert digest(source/name) == old['sources'][name]
    dense_rows = {(r['task'], r['method']): r for r in json.loads((baseline/'results.json').read_text())}
    dense, hashes, availability = {}, {}, []
    angles = 2*np.pi*np.arange(2048)/2048
    for task in TASKS:
        for method in ('gaussian', 'block16'):
            row = dense_rows[task, method]
            availability.append({k: row[k] for k in ('task', 'method', 'fitted', 'train_mse', 'stop_reason')})
            if not row['fitted']:
                continue
            path = baseline/row['data_file']
            assert digest(path) == row['data_sha256']
            with np.load(path) as data:
                assert np.array_equal(data['angles'], angles)
                dense[task, method] = data['prediction']
            hashes[path.name] = row['data_sha256']
    out.mkdir(parents=True, exist_ok=False)
    snapshot = out/'source_snapshot'
    snapshot.mkdir()
    names = ('block_scalar_closure.py', 'run_remaining_block_scalar.py', 'run_block_scalar_closure.py',
             'circle_tasks.py', 'dense_compare.py', 'dense_wide_integrator.py')
    for name in names:
        shutil.copyfile(source/name, snapshot/name)
    manifest = {**{k: prior[k] for k in ('width_reference', 'reference_blocks', 'k', 'seed',
                'counts', 'subset_streams', 'target_mse', 'initialization', 'subset_rule',
                'rtol', 'atol', 'first_step', 'max_step', 'grid', 'deadline_seconds',
                'interrupt_seconds', 'per_run_ceiling_seconds', 'workers', 'blas_threads')},
        'tasks': TASKS, 'history_order': 8, 'time_cap': 3000., 'planned_runs': 90,
        'baseline': str(baseline), 'baseline_data_hashes': hashes, 'baseline_availability': availability,
        'previous': str(previous), 'previous_results_sha256': digest(previous/'results.json'),
        'previous_refinement_sha256': digest(previous/'refinement.json'),
        'sources': {n: digest(source/n) for n in names}, 'command': sys.argv,
        'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__}
    write(out/'manifest.json', manifest)
    pool = scalar.initial_pool(2048, 16, 1)
    rows, predictions, references = [], {}, {}
    started = time.monotonic()

    def run(task, indices, kind, stream=None):
        tick = time.monotonic()
        print(f'Start {task} q={len(indices)} subset={stream}', flush=True)
        u, labels = BY_NAME[task].data()
        layout, G, initial = scalar.initialize(pool, indices, u, 8)
        vector, status = scalar.integrate(layout, G, initial, u, labels)
        prediction = scalar.predict(layout, G, vector, angles)
        final = scalar.forward(layout, G, vector, u)
        start = scalar.forward(layout, G, initial, u)
        assert abs(float(np.mean((final[0]-labels)**2))-status['train_mse']) < 1e-12
        assert np.all(np.isfinite(prediction))
        tag = f'{task}__P8__q{len(indices)}__{kind}'+(f'__s{stream}' if stream is not None else '')
        path = out/(tag+'.npz')
        history = status.pop('history')
        np.savez(path, vector=vector, initial_vector=initial, G=G, indices=indices,
                 angles=angles, prediction=prediction, train_prediction=final[0],
                 train_labels=labels, train_angles=np.asarray(BY_NAME[task].angles), history=history)
        row = {'tag': tag, 'task': task, 'order': 8, 'q': len(indices), 'k': 16,
            'subset_stream': stream, 'kind': kind, **status,
            'dynamic_scalars': layout.size, 'static_G_scalars': G.size,
            'total_seconds': time.monotonic()-tick,
            'h1_motion_rms': rms(final[2], start[2]), 'h2_motion_rms': rms(final[4], start[4]),
            'data_file': path.name, 'data_sha256': digest(path)}
        for method in ('block16', 'gaussian'):
            row['rms_vs_dense_'+method] = (rms(prediction, dense[task, method])
                if status['fitted'] and (task, method) in dense else None)
        write(path.with_suffix('.json'), row)
        rows.append(row)
        predictions[tag] = prediction
        write(out/'results.json', rows)
        print(json.dumps(row), flush=True)
        return row

    for task in TASKS:
        references[task] = run(task, np.arange(128), 'reference')
        for stream in SUBSETS:
            perm = np.random.default_rng(np.random.SeedSequence([1, stream])).permutation(128)
            for q in COUNTS:
                run(task, perm[:q], 'representative', stream)
    write(out/'selection.json', {'selected_order': 8, 'references': {t:r['tag'] for t,r in references.items()}})
    comparisons = []
    for row in rows:
        ref = references[row['task']]
        fitted = row['fitted'] and ref['fitted']
        error = predictions[row['tag']]-predictions[ref['tag']]
        comparisons.append({**{k: row[k] for k in ('tag', 'task', 'kind', 'order', 'q',
                'subset_stream', 'rms_vs_dense_block16', 'rms_vs_dense_gaussian', 'data_file', 'data_sha256')},
            'fitted_pair': fitted,
            'rms_vs_full_closure': float(np.sqrt(np.mean(error**2))) if fitted else None,
            'quadrature_change': abs(float(np.sqrt(np.mean(error**2)))-float(np.sqrt(np.mean(error[::2]**2))))})
    write(out/'comparisons.json', comparisons)
    summaries = []
    for task in TASKS:
        for q in COUNTS:
            group = [r for r in comparisons if r['task']==task and r['q']==q]
            summary = {'task': task, 'q': q, 'count': len(group),
                       'fitted_pairs': sum(r['fitted_pair'] for r in group)}
            for metric in ('rms_vs_full_closure', 'rms_vs_dense_block16', 'rms_vs_dense_gaussian'):
                values = [r[metric] for r in group if r[metric] is not None]
                summary[metric] = {'mean':float(np.mean(values)), 'min':min(values), 'max':max(values),
                                   'count':len(values)} if values else None
            summaries.append(summary)
    write(out/'summary.json', summaries)
    completion = {'wall_seconds': time.monotonic()-started, 'runs': len(rows),
        'fitted_runs': sum(r['fitted'] for r in rows), 'selected_order':8,
        'max_run_seconds': max(r['total_seconds'] for r in rows),
        'max_loss_rise': max(r['max_loss_rise'] for r in rows),
        'max_quadrature_change': max(r['quadrature_change'] for r in comparisons)}
    write(out/'completion.json', completion)
    print(json.dumps(completion), flush=True)


if __name__ == '__main__':
    main()
