"""Bounded, separately identified references for the aggregate-only screen.

No training runs on import. Gaussian references train the unrestricted dense
canonical model. Block-memory references retain every block of a finite-width
sample and are controls, not aggregate candidates or exact population limits.
The checkpoint classes evaluate arbitrary passive circle queries after fitting.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import platform
import signal
import sys
import time

import numpy as np
import scipy

import block_scalar_closure as block
from circle_tasks import BY_NAME, directions
import dense_compare as dense
import dense_wide_integrator as wide


TASK_NAMES = ('pair_cos1', 'triple_mixed', 'cluster_triple_cos9')
SOURCE_NAMES = ('true_aggregate_references.py', 'circle_tasks.py',
                'dense_compare.py', 'dense_wide_integrator.py',
                'block_scalar_closure.py')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')


@dataclass
class GaussianCheckpoint:
    state: dense.State

    def predict(self, angles, batch=128):
        points = directions(np.asarray(angles, dtype=float))
        return np.concatenate([dense._forward(self.state, points[j:j+batch]).output
                               for j in range(0, len(points), batch)])


@dataclass
class BlockMemoryCheckpoint:
    layout: block.Layout
    G: np.ndarray
    vector: np.ndarray

    def predict(self, angles, batch=128):
        return block.predict(self.layout, self.G, self.vector, angles, batch=batch)


def load_checkpoint(path):
    """Return a checkpoint with predict(angles); never starts training."""
    with np.load(path, allow_pickle=False) as saved:
        kind = str(saved['kind'])
        if kind == 'gaussian':
            return GaussianCheckpoint(dense.State(saved['w'], saved['W'], saved['c']))
        if kind == 'block_memory':
            q, k, m, order, d = (int(value) for value in saved['layout'])
            return BlockMemoryCheckpoint(block.Layout(q, k, m, order, d),
                                         saved['G'], saved['vector'])
    raise ValueError(f'Unknown checkpoint kind: {kind}')


class _TrainingBudget(Exception):
    pass


def initial_block_pool(width=1024, k=4, seed=1, mark_bound=3.):
    """Matched initial information; replace only G entries outside the bound.

    The returned w/c/G arrays are initialization inputs only for the aggregate
    candidate. Its runtime must discard these finite-width arrays after forming
    its initial moments. w is never clipped. No redraw changes any in-bound G
    entry, and the original stream is unchanged when all entries obey the bound.
    """
    pool = block.initial_pool(width, k, seed)
    bad = np.abs(pool['G']) > mark_bound
    redrawn = 0
    if np.any(bad):
        rng = np.random.default_rng(np.random.SeedSequence([seed, 300+k]))
        rng.standard_normal(pool['G'].shape)
        while np.any(bad):
            count = int(np.count_nonzero(bad))
            pool['G'][bad] = rng.standard_normal(count)/np.sqrt(k)
            redrawn += count
            bad = np.abs(pool['G']) > mark_bound
    pool['entry_redraws'] = redrawn
    pool['mark_bound'] = mark_bound
    return pool


def gaussian_fit(task, args):
    """Keep the last accepted state even if the hard interrupt is needed."""
    u, labels = task.data()
    initial = dense.initialize(args.width, args.seed, 'gaussian')
    initial_mse = float(np.mean((dense._forward(initial, u).output-labels)**2))
    accepted = [0., initial, initial_mse]
    history = []
    count = [0]
    original_rhs = wide.flat_rhs

    def counted_rhs(*values):
        count[0] += 1
        return original_rhs(*values)

    def callback(at, state, mse):
        accepted[:] = [at, state, mse]
        history.append((at, mse))

    def alarm(signum, frame):
        raise _TrainingBudget()

    old_handler = signal.signal(signal.SIGALRM, alarm)
    started = time.monotonic()
    wide.flat_rhs = counted_rhs
    signal.setitimer(signal.ITIMER_REAL, args.fit_seconds)
    result = None
    try:
        result = wide.integrate(initial, u, labels, time_cap=3000.,
            rtol=1e-5, atol=1e-8, target_train_mse=args.target,
            max_step=10., deadline=time.time()+max(.1, args.fit_seconds-1.),
            callback=callback)
        physical_time, state, mse = result.time, result.state, result.train_mse
        reason = result.stop_reason
    except _TrainingBudget:
        physical_time, state, mse = accepted
        reason = 'training_wall_limit'
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.)
        signal.signal(signal.SIGALRM, old_handler)
        wide.flat_rhs = original_rhs
    training_seconds = time.monotonic()-started
    info = {'physical_time': physical_time, 'train_mse': mse,
            'stop_reason': reason, 'nfev': count[0],
            'nsteps': result.nsteps if result else max(0, len(history)-1),
            'max_loss_rise': result.max_loss_rise if result else
                max([0.]+[b[1]-a[1] for a,b in zip(history, history[1:])]),
            'target_bracket': result.first_target_bracket if result else None,
            'training_seconds': training_seconds, 'initial_mse': initial_mse,
            'initial_readout': 'independent N(0,1/n^2), canonical finite width',
            'solver': result.settings if result else None}
    model = GaussianCheckpoint(state)
    arrays = {'w': state.w, 'W': state.W, 'c': state.c,
              'history': np.asarray(history)}
    return model, info, arrays


def block_fit(task, args):
    u, labels = task.data()
    pool = initial_block_pool(args.width, args.k, args.seed)
    if args.readout == 'zero':
        pool['c'][:] = 0.
    layout, G, initial = block.initialize(pool, np.arange(args.width//args.k),
                                         u, args.order)
    initial_mse = float(np.mean((block.forward(layout, G, initial, u)[0]-labels)**2))
    vector, info = block.integrate(layout, G, initial, u, labels,
        target=args.target, rtol=1e-5, atol=1e-8,
        deadline_seconds=max(.1, args.fit_seconds-1.),
        interrupt_seconds=args.fit_seconds, time_cap=3000.)
    history = info.pop('history')
    info.update(initial_mse=initial_mse,
        initial_readout='zero, population initialization' if args.readout == 'zero'
            else 'independent N(0,1/n^2), canonical finite width',
        initialization_modifications=['c set to zero'] if args.readout == 'zero' else [],
        G_entry_bound=pool['mark_bound'], G_entry_redraws=pool['entry_redraws'],
        G_max_absolute_entry=float(np.max(np.abs(G))),
        G_max_spectral_norm=float(np.max(np.linalg.norm(G, ord=2, axis=(1, 2)))),
        G_max_row_absolute_sum=float(np.max(np.sum(np.abs(G), axis=2))),
        G_max_column_absolute_sum=float(np.max(np.sum(np.abs(G), axis=1))),
        initial_w_max_absolute_entry=float(np.max(np.abs(pool['w']))),
        finite_sample_reference=True)
    model = BlockMemoryCheckpoint(layout, G, vector)
    arrays = {'G': G, 'vector': vector,
              'layout': np.asarray([layout.q, layout.k, layout.m, layout.order, layout.d]),
              'history': history}
    return model, info, arrays


def run_one(task_name, args, manifest_hash):
    started = time.monotonic()
    task = BY_NAME[task_name]
    model, info, arrays = (gaussian_fit if args.kind == 'gaussian' else block_fit)(task, args)
    angles = 2*np.pi*np.arange(args.grid)/args.grid
    prediction = model.predict(angles)
    train_prediction = model.predict(task.angles)
    labels = task.target(task.angles)
    mse = float(np.mean((train_prediction-labels)**2))
    fitted = info['stop_reason'] == 'target' and mse <= args.target*(1+1e-7)
    path = args.output/f'{task_name}__{args.tag}.npz'
    np.savez(path, kind=args.kind, angles=angles, prediction=prediction,
             train_angles=np.asarray(task.angles), train_labels=labels,
             train_prediction=train_prediction, **arrays)
    row = {'task': task_name, 'method': args.kind, 'tag': args.tag,
           'width': args.width, 'seed': args.seed, 'target_mse': args.target,
           'grid': args.grid, 'k': args.k if args.kind == 'block_memory' else None,
           'order': args.order if args.kind == 'block_memory' else None,
           **info, 'train_mse': mse, 'fitted': fitted,
           'endpoint_status': 'fitted threshold endpoint' if fitted else 'partial endpoint',
           'data_file': path.name, 'data_sha256': digest(path),
           'source_manifest_sha256': manifest_hash,
           'total_seconds': time.monotonic()-started}
    if args.kind == 'block_memory':
        gaussian_path = args.output/f'{task_name}__gaussian.npz'
        if gaussian_path.exists():
            reference_row = json.loads(gaussian_path.with_suffix('.json').read_text())
            with np.load(gaussian_path, allow_pickle=False) as reference:
                if not (np.array_equal(reference['angles'], angles)
                        and np.array_equal(reference['train_labels'], labels)
                        and reference_row['width'] == args.width
                        and reference_row['seed'] == args.seed
                        and reference_row['target_mse'] == args.target):
                    raise ValueError('Gaussian and block comparison configuration mismatch')
                difference = prediction-reference['prediction']
                rms = float(np.sqrt(np.mean(difference**2)))
                coarse = float(np.sqrt(np.mean(difference[::2]**2)))
            row.update(rms_vs_gaussian=rms, circle_grid_change=abs(rms-coarse),
                       fitted_pair=fitted and reference_row['fitted'],
                       gaussian_data_sha256=digest(gaussian_path))
    write_json(path.with_suffix('.json'), row)
    print(json.dumps(row, allow_nan=False), flush=True)
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--kind', choices=('gaussian', 'block_memory'), required=True)
    parser.add_argument('--tasks', nargs='+', choices=TASK_NAMES, default=TASK_NAMES)
    parser.add_argument('--width', type=int, default=1024)
    parser.add_argument('--seed', type=int, default=1)
    parser.add_argument('--target', type=float, default=.01)
    parser.add_argument('--grid', type=int, default=256)
    parser.add_argument('--fit-seconds', type=float, default=44.)
    parser.add_argument('--k', type=int, default=4)
    parser.add_argument('--order', type=int, default=1)
    parser.add_argument('--readout', choices=('zero', 'canonical'), default='canonical')
    args = parser.parse_args()
    if not (0 < args.fit_seconds <= 45 and 0 < args.target < 1
            and args.width > 0 and args.seed >= 0 and args.grid >= 2
            and args.k > 0 and args.width % args.k == 0 and args.order > 0):
        parser.error('Invalid dimensions, target, seed, or fit budget')
    args.output = args.output.resolve()
    args.tag = 'gaussian' if args.kind == 'gaussian' else f'block_k{args.k}_P{args.order}_{args.readout}'
    args.output.mkdir(parents=True, exist_ok=True)
    manifest_path = args.output/f'manifest_{args.tag}.json'
    reserved = [manifest_path]
    reserved += [args.output/f'{task}__{args.tag}{suffix}' for task in args.tasks
                 for suffix in ('.npz', '.json')]
    if any(path.exists() for path in reserved):
        raise FileExistsError('Reference output already exists; reruns are disabled')
    source = Path(__file__).resolve().parent
    manifest = {'kind': args.kind, 'tag': args.tag, 'tasks': args.tasks,
        'width': args.width, 'seed': args.seed, 'target_mse': args.target,
        'grid': args.grid, 'k': args.k if args.kind == 'block_memory' else None,
        'order': args.order if args.kind == 'block_memory' else None,
        'block_readout': args.readout if args.kind == 'block_memory' else None,
        'fit_seconds': args.fit_seconds, 'solver_deadline_seconds': args.fit_seconds-1,
        'rtol': 1e-5, 'atol': 1e-8, 'blas_threads': 1,
        'primary_metric': 'sqrt(mean((f_candidate-f_gaussian)^2)) on circle; no amplitude normalization',
        'reference_scope': 'one finite-width realization, separately stopped first MSE crossing',
        'mark_cutoff': 'G entries with absolute value >3 redrawn from same initialization stream; w untouched'
            if args.kind == 'block_memory' else 'none',
        'command': sys.argv, 'cwd': str(Path.cwd()),
        'python': platform.python_version(), 'numpy': np.__version__,
        'scipy': scipy.__version__, 'machine': platform.platform(),
        'sources': {name: digest(source/name) for name in SOURCE_NAMES},
        'training_data': {name: {'angles': BY_NAME[name].angles,
            'labels': BY_NAME[name].target(BY_NAME[name].angles).tolist()}
            for name in args.tasks}}
    write_json(manifest_path, manifest)
    manifest_hash = digest(manifest_path)
    started = time.monotonic()
    rows = []
    for task_name in args.tasks:
        rows.append(run_one(task_name, args, manifest_hash))
        write_json(args.output/f'results_{args.tag}.json', rows)
    write_json(args.output/f'completion_{args.tag}.json', {
        'wall_seconds': time.monotonic()-started, 'runs': len(rows),
        'all_fitted': all(row['fitted'] for row in rows),
        'max_training_seconds': max(row['training_seconds'] for row in rows),
        'reruns': 0})


if __name__ == '__main__':
    main()
