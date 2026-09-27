"""Bounded Gaussian-block/HD initialization comparison; unrestricted dense GF.

Run only through main. Every trajectory gets one BLAS thread, a 50-second
solver deadline, and a 55-second training interrupt with an accepted-state
checkpoint. All comparisons are absolute circle function RMS differences.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import platform
import shutil
import signal
import subprocess
import sys
import time

import numpy as np
import scipy

import dense_compare as dense
from dense_wide_integrator import integrate
from circle_tasks import BY_NAME, directions


METHODS = ('gaussian', 'gaussian_control', 'hd', 'block8', 'block32', 'block128')
TASK_NAMES = ('cluster_triple_cos9', 'alternating5')
N = 1024
TARGET = 0.01
GRID = 2048


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, allow_nan=False) + '\n')


def initialize(n, seed, method):
    if not method.startswith('block'):
        return dense.initialize(n, seed, method)
    k = int(method.removeprefix('block'))
    if k < 1 or n % k:
        raise ValueError('Block size must be a positive divisor of width')
    w = dense._rng(seed, 1).standard_normal((n, 2))
    c = dense._rng(seed, 2).standard_normal(n) / n
    rng = dense._rng(seed, 300 + k)
    W = np.zeros((n, n), dtype=np.float64)
    for start in range(0, n, k):
        W[start:start+k, start:start+k] = rng.standard_normal((k, k)) / np.sqrt(k)
    return dense.State(w, W, c)


class TrainingBudget(Exception):
    pass


def run_one(job):
    out, task_name, method, resume, target, width, seed, finish_partials = job
    out = Path(out)
    started = time.monotonic()
    task = BY_NAME[task_name]
    u, y = task.data()
    source_hash = None
    start_time = 0.
    previous_seconds = 0.
    if resume:
        old_path = Path(resume) / f'{task_name}__{method}.npz'
        old_row = json.loads(old_path.with_suffix('.json').read_text())
        source_hash = digest(old_path)
        if source_hash != old_row['data_sha256'] or (not old_row['fitted'] and not finish_partials):
            raise ValueError('Continuation requires an intact fitted checkpoint')
        if finish_partials:
            previous_seconds = old_row.get('cumulative_total_seconds', old_row['total_seconds'])
        with np.load(old_path) as old:
            state = dense.State(old['w'], old['W'], old['c'])
            if not np.array_equal(old['train_labels'], y):
                raise ValueError('Continuation labels changed')
        start_time = old_row['physical_time']
    else:
        state = initialize(width, seed, method)
    if state.width != width:
        raise ValueError('Checkpoint width does not match requested width')
    initial_fields = dense._forward(state, u)
    initial_row_norm = float(np.sum(state.W * state.W) / width)
    accepted = [0., state, float(np.mean((initial_fields.output-y)**2))]
    history = []
    max_rise = 0.
    last_log = started

    def callback(t, current, mse):
        nonlocal max_rise, last_log
        if history:
            max_rise = max(max_rise, mse-history[-1][1])
        accepted[:] = [t, current, mse]
        history.append((start_time+t, mse))
        now = time.monotonic()
        if now-last_log >= 10:
            print(json.dumps({'progress': task_name, 'method': method,
                              'mse': mse, 'seconds': now-started}), flush=True)
            last_log = now

    def stop_training(signum, frame):
        raise TrainingBudget()

    training_limit = min(50., max(0., 58.-previous_seconds))
    interrupt_limit = min(55., max(.1, 59.-previous_seconds))
    old_handler = signal.signal(signal.SIGALRM, stop_training)
    signal.setitimer(signal.ITIMER_REAL, max(.1, interrupt_limit-(time.monotonic()-started)))
    result = None
    try:
        result = integrate(state, u, y, time_cap=3000., rtol=1e-5, atol=1e-8,
                           target_train_mse=target, max_step=10.,
                           deadline=time.time()+max(0., training_limit-(time.monotonic()-started)),
                           callback=callback)
        state, physical_time, mse = result.state, result.time, result.train_mse
        reason = result.stop_reason
    except TrainingBudget:
        physical_time, state, mse = accepted
        reason = 'training_wall_limit'
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.)
        signal.signal(signal.SIGALRM, old_handler)
    training_seconds = time.monotonic()-started
    angles = 2*np.pi*np.arange(GRID)/GRID
    points = directions(angles)
    prediction = np.concatenate([dense._forward(state, points[j:j+256]).output
                                 for j in range(0, GRID, 256)])
    train_fields = dense._forward(state, u)
    recomputed_mse = float(np.mean((train_fields.output-y)**2))
    path = out / f'{task_name}__{method}.npz'
    np.savez(path, angles=angles, prediction=prediction, train_angles=task.angles,
             train_labels=y, train_prediction=train_fields.output,
             history=np.asarray(history), w=state.w, W=state.W, c=state.c)
    row = {'task': task_name, 'method': method, 'width': width, 'seed': seed,
           'block_size': int(method[5:]) if method.startswith('block') else None,
           'train_mse': recomputed_mse, 'stop_reason': reason,
           'target_mse': target,
           'fitted': reason == 'target' and recomputed_mse <= target*(1+1e-7),
           'physical_time': start_time+physical_time,
           'continuation_start_time': start_time,
           'continuation_start_mse': float(np.mean((initial_fields.output-y)**2)),
           'source_checkpoint_sha256': source_hash,
           'training_seconds': training_seconds,
           'total_seconds': time.monotonic()-started,
           'previous_seconds': previous_seconds,
           'cumulative_total_seconds': previous_seconds+time.monotonic()-started,
           'max_loss_rise': max(max_rise, result.max_loss_rise if result else 0.),
           'nsteps': result.nsteps if result else len(history)-1,
           'nfev': result.nfev if result else None,
           'start_mean_squared_singular_value': initial_row_norm,
           'h1_motion_rms': float(np.sqrt(np.mean((train_fields.h1-initial_fields.h1)**2))),
           'h2_motion_rms': float(np.sqrt(np.mean((train_fields.h2-initial_fields.h2)**2))),
           'solver': result.settings if result else None,
           'data_file': path.name, 'data_sha256': digest(path)}
    write_json(out / f'{task_name}__{method}.json', row)
    print(json.dumps(row), flush=True)
    return row


def analyze(out, rows, target=TARGET, resume=None, tasks=TASK_NAMES, width=N, seed=0):
    comparisons = []
    for task in tasks:
        subset = {r['method']: r for r in rows if r['task'] == task}
        data = {method: np.load(out / row['data_file']) for method, row in subset.items()}
        reference = data['gaussian']['prediction']
        hd = data['hd']['prediction']
        for method in METHODS:
            row = subset[method]
            pred = data[method]['prediction']
            error = float(np.sqrt(np.mean((pred-reference)**2)))
            coarse = float(np.sqrt(np.mean((pred[::2]-reference[::2])**2)))
            comparisons.append({'task': task, 'method': method,
                'rms_vs_gaussian': error,
                'rms_vs_hd': float(np.sqrt(np.mean((pred-hd)**2))),
                'quadrature_change': abs(error-coarse),
                'fitted_pair': row['fitted'] and subset['gaussian']['fitted'],
                'training_seconds': row['training_seconds'],
                'total_seconds': row['total_seconds'], 'train_mse': row['train_mse']})
        for item in data.values():
            item.close()
    write_json(out / 'comparisons.json', comparisons)
    lines = [f'# Quick width-{width} Gaussian-block comparison', '',
             f'Unrestricted dense canonical training; seed{seed} matched outer weights; '
             f'first MSE{target:g} crossing. Absolute circle RMS against the fitted '
             'Gaussian reference, with 2048 test angles. One draw per method.', '',
             '| Task | Initialization | RMS vs Gaussian | Training seconds | MSE |',
             '|---|---|---:|---:|---:|']
    for row in comparisons:
        lines.append(f"| {row['task']} | {row['method']} | {row['rms_vs_gaussian']:.8f} | "
                     f"{row['training_seconds']:.2f} | {row['train_mse']:.8f} |")
    lines += ['', 'This tests initialization replacement, not scalar compression. '
              'One seed and width do not establish an order rate or population limit. '
              f'MSE{target:g} endpoints are not zero-loss limits. '
              'No solver refinement campaign was performed.']
    if resume:
        lines += ['', f'Continued saved states from `{resume}`; no reinitialization.']
    if not all(r['fitted'] for r in rows):
        lines += ['', '**PARTIAL: some runs did not reach the common target. '
                  'Their discrepancies are diagnostics, not fitted-model comparisons.**']
    (out / 'report.md').write_text('\n'.join(lines)+'\n')
    return comparisons


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--resume', help='Previous fitted checkpoint directory')
    parser.add_argument('--target', type=float, default=TARGET)
    parser.add_argument('--width', type=int, default=N)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--tasks', nargs='+', choices=tuple(BY_NAME), default=TASK_NAMES)
    parser.add_argument('--workers', type=int, default=3)
    parser.add_argument('--finish-partials', action='store_true',
                        help='Use remaining cumulative 60-second budget of saved trajectories')
    args = parser.parse_args()
    if not 0 < args.target < 1:
        parser.error('--target must lie between zero and one')
    if args.width < 128 or args.width & (args.width-1):
        parser.error('--width must be a power of two >=128')
    if args.seed < 0 or not 1 <= args.workers <= 3:
        parser.error('Require seed>=0 and 1<=workers<=3')
    resume = str(Path(args.resume).resolve()) if args.resume else None
    if args.finish_partials and not resume:
        parser.error('--finish-partials requires --resume')
    if resume:
        old_manifest = json.loads((Path(resume)/'manifest.json').read_text())
        if old_manifest['width'] != args.width or old_manifest['seed'] != args.seed:
            raise ValueError('Continuation width/seed must match previous run')
        source = Path(__file__).resolve().parent
        for name in ('dense_compare.py', 'dense_wide_integrator.py', 'circle_tasks.py'):
            if digest(source/name) != old_manifest['sources'][name]:
                raise ValueError(f'Canonical source changed: {name}')
    out = Path(args.output).resolve()
    out.mkdir(parents=True, exist_ok=False)
    source = Path(__file__).resolve().parent
    snapshot = out / 'source_snapshot'
    snapshot.mkdir()
    files = ('quick_block_compare.py', 'dense_compare.py',
             'dense_wide_integrator.py', 'circle_tasks.py')
    for name in files:
        shutil.copyfile(source/name, snapshot/name)
    started = time.monotonic()
    config = {'width': args.width, 'seed': args.seed, 'methods': METHODS, 'tasks': args.tasks,
              'block_streams': {method: 300+int(method[5:]) for method in METHODS
                                if method.startswith('block')},
              'target_mse': args.target, 'resume': resume,
              'finish_partials': args.finish_partials,
              'resume_manifest_sha256': digest(Path(resume)/'manifest.json') if resume else None,
              'grid': GRID, 'workers': args.workers,
              'training_deadline_seconds': 50, 'training_interrupt_seconds': 55,
              'rtol': 1e-5, 'atol': 1e-8, 'command': sys.argv,
              'cwd': str(Path.cwd()), 'python': platform.python_version(),
              'numpy': np.__version__, 'scipy': scipy.__version__,
              'blas_threads': 1, 'machine': platform.platform(),
              'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
              'sources': {name: digest(source/name) for name in files},
              'training_data': {name: {'angles': BY_NAME[name].angles,
                                     'labels': BY_NAME[name].target(BY_NAME[name].angles).tolist()}
                                for name in args.tasks}}
    write_json(out / 'manifest.json', config)
    jobs = [(str(out), task, method, resume, args.target, args.width, args.seed, args.finish_partials)
            for task in args.tasks for method in METHODS]
    rows = []
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(run_one, job) for job in jobs]
        for future in as_completed(futures):
            rows.append(future.result())
            write_json(out / 'results.json', rows)
    comparisons = analyze(out, rows, args.target, resume, args.tasks, args.width, args.seed)
    write_json(out / 'completion.json', {'wall_seconds': time.monotonic()-started,
        'all_fitted': all(r['fitted'] for r in rows), 'runs': len(rows),
        'max_run_seconds': max(r['total_seconds'] for r in rows),
        'max_cumulative_run_seconds': max(r['cumulative_total_seconds'] for r in rows),
        'max_quadrature_change': max(r['quadrature_change'] for r in comparisons)})
    print((out/'report.md').read_text(), flush=True)


if __name__ == '__main__':
    main()
