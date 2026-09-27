"""One fixed-grid histogram per distinct task; no per-task tuning or reruns."""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import ctypes as ct
import json
from pathlib import Path
import shutil
import subprocess
import time
import numpy as np
from scipy.special import ndtr
from run_histogram_candidate import pointer, PTR, rms, digest, write
from circle_tasks import BY_NAME
from histogram_multi_reference import run_reference, predict, weighted_rhs

TASKS = ('pair_cos1', 'pair_cos3', 'near_pair_sin9', 'triple_cos3',
         'triple_mixed', 'cluster_triple_cos9')
ANGLES = np.arange(1024)*2*np.pi/1024


def grid(m):
    return (5, 9, 9, 9)+(5 if m == 2 else 3,)*(2*m)


def bounds(m):
    return np.array([5., 4., 4., 4.]+[3.]*m+[1.]*m)


def axes_for(shape, upper):
    return [np.linspace(0 if j == 0 else -v, v, n)
            for j, (n, v) in enumerate(zip(shape, upper))]


def initialize(shape, upper, u):
    axes = axes_for(shape, upper)
    laws = []
    for j in range(3):
        axis = axes[j]
        edges = np.r_[0 if j == 0 else -np.inf, (axis[:-1]+axis[1:])/2, np.inf]
        laws.append(np.diff(2*ndtr(edges)-1 if j == 0 else ndtr(edges)))
    m = len(u)
    p = np.zeros(shape)
    for ix, wx in enumerate(axes[1]):
        for iy, wy in enumerate(axes[2]):
            h = np.tanh(u@np.array([wx, wy]))
            positions = (h+1)/2*(np.array(shape[4+m:])-1)
            lo = np.minimum(np.floor(positions).astype(int), np.array(shape[4+m:])-2)
            frac = positions-lo
            for bits in range(1 << m):
                idx = tuple(lo[j]+((bits >> j) & 1) for j in range(m))
                weight = float(np.prod([frac[j] if (bits >> j) & 1 else 1-frac[j] for j in range(m)]))
                index = (slice(None), ix, iy, shape[3]//2)+tuple(n//2 for n in shape[4:4+m])+idx
                p[index] += laws[0]*laws[1][ix]*laws[2][iy]*weight
    assert abs(float(p.sum())-1) < 1e-13
    return p.ravel()


class Histogram:
    def __init__(self, library, shape, upper, u, threads=8):
        self.lib = ct.CDLL(str(library)); self.shape = tuple(shape)
        self.m = len(u); self.upper = np.asarray(upper, dtype=np.float64)
        self.axes = axes_for(shape, upper)
        lib = self.lib
        lib.hist_multi_create.argtypes = [ct.c_int, ct.POINTER(ct.c_int), PTR, PTR, ct.c_int]
        lib.hist_multi_create.restype = ct.c_void_p
        lib.hist_multi_free.argtypes = [ct.c_void_p]
        lib.hist_multi_rhs.argtypes = [ct.c_void_p, PTR, ct.c_double, PTR, PTR, PTR]
        lib.hist_multi_integrate.argtypes = [ct.c_void_p, PTR, PTR, PTR, ct.c_double,
                                           ct.c_double, ct.c_double, ct.c_double, PTR]
        lib.hist_multi_predict.argtypes = [ct.c_void_p, PTR, ct.c_double, PTR, ct.c_int, PTR]
        dims = np.array(shape, dtype=np.int32)
        self.handle = lib.hist_multi_create(self.m, dims.ctypes.data_as(ct.POINTER(ct.c_int)),
                                            pointer(self.upper), pointer(np.ascontiguousarray(u)), threads)
        if not self.handle:
            raise RuntimeError('Histogram allocation failed')

    def close(self):
        if self.handle:
            self.lib.hist_multi_free(self.handle); self.handle = None

    def rhs(self, p, L, labels):
        dp = np.empty_like(p); stats = np.empty(16)
        self.lib.hist_multi_rhs(self.handle, pointer(p), L, pointer(labels), pointer(dp), pointer(stats))
        return dp, stats

    def integrate(self, p, labels):
        L = np.array([1.]); stats = np.empty(12)
        self.lib.hist_multi_integrate(self.handle, pointer(p), pointer(L), pointer(labels),
                                     .01, .7, 50., 100., pointer(stats))
        return float(L[0]), stats

    def predict(self, p, L, angles=ANGLES):
        angles = np.ascontiguousarray(angles, dtype=np.float64); result = np.empty_like(angles)
        self.lib.hist_multi_predict(self.handle, pointer(p), L, pointer(angles), len(angles), pointer(result))
        return result


def check(library, out):
    checks = []
    for task in ('pair_cos3', 'triple_mixed'):
        u, labels = BY_NAME[task].data(); m = len(labels)
        shape = (3, 5, 5, 5)+(5,)*m+(3,)*m
        model = Histogram(library, shape, bounds(m), u, 2)
        indices = [(1, 1, 3, 3)+(1,)*m+(0,)*m,
                   (1, 3, 1, 1)+(3,)*m+(2,)*m]
        weights = np.array([.4, .6]); p = np.zeros(int(np.prod(shape)))
        nodes = np.array([[axis[j] for axis, j in zip(model.axes, index)] for index in indices])
        for index, weight in zip(indices, weights):
            p[np.ravel_multi_index(index, shape)] = weight
        state = {'g': nodes[:, 0], 'weights': weights, 'w': nodes[:, 1:3],
                 'c': nodes[:, 3], 'A': nodes[:, 4:4+m], 'b': nodes[:, 4+m:], 'L': np.array(1.7)}
        velocity = weighted_rhs(state, u, labels)
        expected = np.r_[0., weights@velocity['w'], weights@velocity['c'],
                         weights@velocity['A'], weights@velocity['b']]
        dp, stats = model.rhs(p, 1.7, labels)
        observed = []
        for j, axis in enumerate(model.axes):
            marginal = dp.reshape(shape).sum(axis=tuple(v for v in range(len(shape)) if v != j))
            observed.append(marginal@axis)
        error = float(np.max(np.abs(np.array(observed)-expected)))
        angles = ANGLES[::64]
        query_error = float(np.max(np.abs(model.predict(p, 1.7, angles)-predict(state, angles))))
        assert error < 1e-10, error
        assert query_error < 1e-10, query_error
        assert abs(float(dp.sum())) < 1e-10
        assert (p+.5/stats[2]*dp).min() >= -1e-14
        model.close()
        checks.append({'task': task, 'velocity_max_error': error,
                       'query_max_error': query_error, 'mass_positive_conservative': True})
    write(out/'checks.json', checks)
    print(json.dumps({'checks': checks}), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    out = parser.parse_args().output.resolve(); out.mkdir(parents=True, exist_ok=False)
    source = Path(__file__).resolve().parent
    names = ('run_histogram_breadth.py', 'histogram_multi_input.cpp', 'histogram_multi_reference.py',
             'run_histogram_candidate.py', 'circle_tasks.py', 'block_scalar_closure.py',
             'dense_compare.py', 'dense_wide_integrator.py')
    snapshot = out/'source_snapshot'; snapshot.mkdir()
    for name in names:
        shutil.copyfile(source/name, snapshot/name)
    library = out/'histogram_multi_input.so'
    command = ['g++', '-O3', '-std=c++17', '-fopenmp', '-shared', '-fPIC',
               str(source/'histogram_multi_input.cpp'), '-o', str(library)]
    subprocess.run(command, check=True, capture_output=True)
    write(out/'manifest.json', {'tasks': TASKS, 'k': 1, 'memory_order': 1, 'target_mse': .01,
          'shape_m2': grid(2), 'shape_m3': grid(3), 'bounds_m2': bounds(2).tolist(),
          'bounds_m3': bounds(3).tolist(), 'reference_orders': [16, 24], 'test_points': len(ANGLES),
          'training_seconds_ceiling': 50, 'time_cap': 100, 'cfl': .7, 'threads': 8,
          'sources': {name: digest(source/name) for name in names},
          'library_sha256': digest(library), 'compile_command': command})
    check(library, out)
    rows = []
    for task in TASKS:
        u, labels = BY_NAME[task].data(); m = len(labels)
        references = []
        for order in (16, 24):
            tick = time.monotonic()
            print(f'Start {task} population reference GH{order}', flush=True)
            state, info = run_reference(u, labels, order=order, target=.01, deadline=50., timecap=100.)
            prediction = predict(state, ANGLES)
            path = out/f'{task}__reference{order}.npz'
            np.savez(path, **state, prediction=prediction, angles=ANGLES, u=u, labels=labels)
            record = {'task': task, 'method': f'reference{order}', **info,
                      'total_seconds': time.monotonic()-tick, 'data_file': path.name,
                      'data_sha256': digest(path)}
            write(path.with_suffix('.json'), record)
            references.append((record, prediction))
            print(json.dumps({k:v for k,v in record.items() if k != 'history'}), flush=True)
        tick = time.monotonic()
        shape = grid(m); model = Histogram(library, shape, bounds(m), u)
        p = initialize(shape, bounds(m), u)
        print(f'Start {task} histogram: {len(p)} fixed masses', flush=True)
        L, stats = model.integrate(p, labels)
        prediction = model.predict(p, L)
        train_prediction = model.predict(p, L, np.array(BY_NAME[task].angles))
        model.close()
        path = out/f'{task}__histogram.npz'
        np.savez(path, p=p, L=L, shape=shape, bounds=bounds(m), u=u, labels=labels,
                 prediction=prediction, train_prediction=train_prediction, angles=ANGLES, stats=stats)
        refinfo, refpred = references[-1]
        both_fitted = int(stats[0]) == 0 and refinfo['fitted']
        error = rms(prediction, refpred)
        refgap = rms(references[0][1], refpred)
        mse = float(np.mean((train_prediction-labels)**2))
        assert abs(mse-float(stats[2])) < 1e-9
        record = {'task': task, 'method': 'histogram', 'm': m, 'dynamic_scalars': len(p)+1,
                  'fitted': int(stats[0]) == 0, 'stop_reason': int(stats[0]),
                  'physical_time': float(stats[1]), 'train_mse': mse,
                  'training_seconds': float(stats[4]), 'total_seconds': time.monotonic()-tick,
                  'mass': float(stats[5]), 'minimum_mass': float(stats[6]),
                  'maximum_taper_zone_mass': float(stats[7]), 'maximum_loss_rise': float(stats[8]),
                  'rms_vs_reference24': error, 'reference16_vs24_rms': refgap,
                  'circle_grid_difference': abs(error-rms(prediction[::2], refpred[::2])),
                  'fitted_pair': both_fitted, 'reference_train_mse': refinfo['train_mse'],
                  'data_file': path.name, 'data_sha256': digest(path)}
        record['screen_gates_passed'] = bool(both_fitted and references[0][0]['fitted']
              and error <= .01 and refgap <= .005 and record['circle_grid_difference'] <= .0001
              and abs(record['mass']-1) <= 1e-10 and record['minimum_mass'] >= -1e-14
              and record['maximum_taper_zone_mass'] <= .001)
        write(path.with_suffix('.json'), record)
        rows.extend([r[0] for r in references]+[record]); write(out/'results.json', rows)
        print(json.dumps({'TASK_RESULT': record}), flush=True)
    write(out/'decision.json', {'completed_tasks': len(TASKS), 'trajectories': len(rows),
          'next_action': 'stop; no further runs in this breadth screen',
          'scope': 'fixed-grid k1 H1 histogram vs numerical population reference'})


if __name__ == '__main__':
    main()
