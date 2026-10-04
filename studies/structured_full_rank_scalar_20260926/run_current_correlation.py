"""Frozen current-correlation screen; reuses dense endpoints, never trains dense."""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import hashlib
import importlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time
import numpy as np
import scipy
import dense_compare as dense
from small_scalar_integrator import integrate

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA = ROOT/'data/generated/structured_full_rank_scalar_20260926'
OLD = DATA/'cubic_scalar_20260930'
FOCUS = ('near_pair_sin9', 'cluster_triple_cos9', 'cluster_triple_cos1')
MODULES = {'projected': 'current_projected_correlation',
           'gaussian': 'current_gaussian_correlation'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def clean(value):
    if isinstance(value, dict):
        return {str(k): clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(v) for v in value]
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, Path):
        return str(value)
    return value


def write_json(path, value):
    path.write_text(json.dumps(clean(value), indent=2, allow_nan=False)+'\n')


def arrays_of(model):
    if hasattr(model, 'coefficient_dict'):
        return model.coefficient_dict()
    return {k: v for k, v in vars(model).items() if isinstance(v, np.ndarray)}


def run(args):
    out = DATA/'current_correlation_20260930'/args.output
    out.mkdir(parents=True, exist_ok=False)
    sources = out/'sources'
    sources.mkdir()
    names = ['run_current_correlation.py', 'dense_compare.py',
             'small_scalar_integrator.py', 'cubic_scalar_ode.py',
             'CURRENT_CORRELATION_PROTOCOL_20260930.md']
    for method in args.methods:
        names += [MODULES[method]+'.py',
                  'CURRENT_CORRELATION_ROUTE_'+('A' if method == 'projected' else 'B')+'_20260930.md']
    for name in names:
        shutil.copy2(HERE/name, sources/name)
    manifest = dict(command=sys.argv, cwd=str(Path.cwd()),
        git_head=subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
        settings=vars(args), python=platform.python_version(), numpy=np.__version__,
        scipy=scipy.__version__, platform=platform.platform(),
        threads={k: os.environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
        sources={name: sha(sources/name) for name in names})
    write_json(out/'manifest.json', manifest)
    start = time.monotonic()
    results = []
    for task in args.tasks:
        with np.load(OLD/(task+'.npz')) as archive:
            saved = {k: archive[k] for k in archive.files}
        old_info = json.loads((OLD/(task+'.json')).read_text())
        selected = np.array(old_info['representatives'])
        train_angles = saved['train_angles']
        angles = np.r_[saved['angles'], train_angles]
        points = np.column_stack([np.cos(angles), np.sin(angles)])
        train_inputs = points[256:][selected]
        labels = saved['model_labels']
        for method in args.methods:
            name = task+'__'+method
            module = importlib.import_module(MODULES[method])
            before = time.monotonic()
            input_coefficient_path = None
            if args.coefficients_from:
                if args.training_only:
                    raise ValueError('training-only validation requires its own query-free constructor')
                input_coefficient_path = (DATA/'current_correlation_20260930'/
                    args.coefficients_from/(name+'__coefficients.npz'))
                with np.load(input_coefficient_path) as archive:
                    model = module.from_coefficients(dict(archive))
            else:
                initial = dense.initialize(1024, 1, 'gaussian')
                model = module.initialize_with_queries(initial.w, initial.W,
                    train_inputs, labels, points if not args.training_only else np.empty((0, 2)))
                del initial
            init_seconds = time.monotonic()-before
            if init_seconds > 30:
                raise TimeoutError('constructor exceeded frozen 30-second cap')
            coef = arrays_of(model)
            np.savez_compressed(out/(name+'__coefficients.npz'), **coef)
            row = dict(task=task, method=method, constructor_seconds=init_seconds,
                constructor_metadata=getattr(model, 'metadata', {}),
                training_states=model.training_size, total_states=model.size,
                input_sha256={str(OLD/(task+'.npz')): sha(OLD/(task+'.npz')),
                              str(OLD/(task+'.json')): sha(OLD/(task+'.json'))},
                coefficient_scalars=sum(v.size for v in coef.values()),
                coefficient_bytes=sum(v.nbytes for v in coef.values()),
                model_array_bytes=sum(v.nbytes for v in vars(model).values()
                                      if isinstance(v, np.ndarray)),
                coefficient_shapes={k: list(v.shape) for k, v in coef.items()},
                coefficient_sha256=sha(out/(name+'__coefficients.npz')))
            if input_coefficient_path:
                row['input_sha256'][str(input_coefficient_path)] = sha(input_coefficient_path)
            # Queries must not contribute to the mathematical training RHS.
            state0 = model.initial_state()
            changed = state0.copy()
            if model.size > model.training_size:
                changed[model.training_size:] *= 0.37
            row['query_independence_max_abs'] = float(np.max(np.abs(
                model.rhs(0, state0)[:model.training_size]-
                model.rhs(0, changed)[:model.training_size])))
            if args.preflight:
                state, history = state0, np.empty((0, 2))
                info = dict(stop_reason='constructor_only', fitted=False,
                    train_mse=float(np.mean(model.residual(state0)**2)),
                    training_seconds=0., integration_performed=False)
            else:
                state, info, history = integrate(model.rhs, state0, model.residual,
                    list(model.blocks.values()) if isinstance(model.blocks, dict) else model.blocks,
                    rtol=args.rtol, atol=args.atol, wall_seconds=20.)
            row.update(info)
            row['max_abs_state'] = float(np.max(np.abs(state)))
            row['diagnostics'] = model.diagnostics(state)
            before = time.monotonic()
            pred = model.predict(state)
            row['decode_seconds'] = time.monotonic()-before
            if not args.training_only and not args.preflight:
                difference = pred[:256]-saved['dense']
                row.update(circle_rms=float(np.sqrt(np.mean(difference**2))),
                    nested_rms_change=float(abs(np.sqrt(np.mean(difference**2))-
                                               np.sqrt(np.mean(difference[::2]**2)))),
                    alias_max_abs=float(np.max(np.abs(pred[256+selected] -
                        (labels+model.residual(state))))),
                    original_circle_rms=old_info['scalar_dense_rms'])
            changed = state.copy()
            if model.size > model.training_size:
                changed[model.training_size:] *= 0.37
            row['endpoint_query_independence_max_abs'] = float(np.max(np.abs(
                model.rhs(0, state)[:model.training_size]-
                model.rhs(0, changed)[:model.training_size])))
            np.savez_compressed(out/(name+'.npz'), state=state, history=history,
                prediction=pred, dense=saved['dense'], angles=angles,
                labels=labels, selected=selected)
            row['data_sha256'] = sha(out/(name+'.npz'))
            write_json(out/(name+'.json'), row)
            results.append(row)
            visible = ('task', 'method', 'stop_reason', 'fitted', 'train_mse',
                       'circle_rms', 'training_states', 'total_states',
                       'training_seconds', 'alias_max_abs', 'nested_rms_change',
                       'max_abs_state')
            print(json.dumps(clean({k: row[k] for k in visible if k in row}),
                             allow_nan=False), flush=True)
    write_json(out/'summary.json', dict(results=results,
        wall_seconds=time.monotonic()-start, exit_status=0))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--methods', nargs='+', choices=tuple(MODULES), required=True)
    parser.add_argument('--tasks', nargs='+', default=list(FOCUS))
    parser.add_argument('--output', required=True)
    parser.add_argument('--rtol', type=float, default=1e-8)
    parser.add_argument('--atol', type=float, default=1e-10)
    parser.add_argument('--training-only', action='store_true')
    parser.add_argument('--coefficients-from')
    parser.add_argument('--preflight', action='store_true')
    run(parser.parse_args())
