#!/usr/bin/env python3
"""Matched-loss initial tangent-kernel control for the first-quadrant experiment."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '2'
import numpy as np
import mpmath as mp
import scipy
from scipy.linalg import expm

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'code'))
from pde import finite_network as finite
SEEDS = (11, 29, 47)


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def features(parameters, directions):
    a, b, c = parameters
    z1 = a @ directions.T
    h1 = np.tanh(z1)
    z2 = b @ h1
    h2 = np.tanh(z2)
    delta2 = c[:, None] * finite.TANH.derivative(z2)
    delta1 = (b.T @ delta2) * finite.TANH.derivative(z1)
    return h1, h2, delta1, delta2, c @ h2 / c.size


def kernel_parts(left, right, u, v):
    h, g, d, e, _ = left
    h0, g0, d0, e0, _ = right
    n = h.shape[0]
    return np.stack([(u @ v.T) * (d.T @ d0 / n),
                     (h.T @ h0 / n) * (e.T @ e0 / n), g.T @ g0 / n])


class FrozenFlow:
    def __init__(self, kernel, initial_training, labels, require_positive=True):
        self.kernel, self.labels = kernel, labels
        self.values, self.vectors = np.linalg.eigh(kernel)
        assert np.max(np.abs(kernel - kernel.T)) <= 1e-12
        if require_positive:
            assert self.values.min() > 0
        self.coefficients = self.vectors.T @ (initial_training - labels)

    def loss(self, t):
        t = np.asarray(t)
        return np.mean(self.coefficients ** 2 * np.exp(-4 * t[..., None] * self.values / len(self.labels)), axis=-1)

    def predict(self, cross, initial, t):
        exponent = -2 * t * self.values / len(self.labels)
        factors = np.full_like(self.values, 2 * t / len(self.labels))
        use = self.values != 0
        factors[use] = -np.expm1(exponent[use]) / self.values[use]
        alpha = self.vectors @ (factors * self.coefficients)
        output = initial - cross @ alpha
        training = self.labels + self.vectors @ (np.exp(exponent) * self.coefficients)
        return output, training

    def stop_at_loss(self, target):
        lo, hi = 0., 100.
        for _ in range(60):
            if self.loss(hi) <= target:
                break
            hi *= 2
        else:
            raise RuntimeError('No matching loss within declared time bracket')
        for _ in range(90):
            mid = (lo + hi) / 2
            if self.loss(mid) > target:
                lo = mid
            else:
                hi = mid
        assert abs(float(self.loss(hi)) - target) < 1e-9
        return hi


def arithmetic_checks():
    rng = np.random.default_rng(538)
    p = finite.initialize(17, 2, 2, seed=61)
    p = finite.Parameters(p.weights, rng.normal(size=17))
    pars = (*p.weights, p.readout)
    u = rng.normal(size=(9, 2))
    u /= np.linalg.norm(u, axis=1)[:, None]
    fields = features(pars, u)
    observed = kernel_parts(fields, fields, u, u)
    reference = finite.kernel_blocks(p, np.sqrt(2) * u.T)
    checks = {'kernel_blocks_vs_maintained': float(np.max(abs(observed - reference)))}
    assert checks['kernel_blocks_vs_maintained'] < 2e-12
    k = reference.sum(axis=0)
    y, f0 = rng.normal(size=4), fields[-1]
    for name, train_kernel, cross in (
            ('ordinary', k[:4, :4], k[4:, :4]),
            ('singular', np.diag([0., .1, 0., 1.]), rng.normal(size=(5, 4)))):
        flow = FrozenFlow(train_kernel, f0[:4], y, require_positive=False)
        pred, train = flow.predict(cross, f0[4:], 100.)
        generator = np.zeros((9, 9))
        generator[:4, :4] = -.5 * train_kernel
        generator[4:, :4] = -.5 * cross
        direct = expm(100 * generator) @ np.r_[f0[:4] - y, f0[4:]]
        error = max(float(np.max(abs(pred - direct[4:]))), float(np.max(abs(train - y - direct[:4]))))
        checks[f'{name}_exponential_error'] = error
        assert error < 2e-11
    return checks


def high_precision(kernel, cross, f0, train_indices, labels, horizon, predictions, target):
    with mp.workdps(70):
        lam, v = mp.eigsy(mp.matrix(kernel.tolist()))
        coeff = v.T * mp.matrix((f0[train_indices] - labels).tolist())
        beta = mp.mpf(2) * horizon / len(labels)
        q = [-mp.expm1(-beta * value) / value for value in lam]
        alpha = v * mp.matrix([q[j] * coeff[j] for j in range(len(labels))])
        selection = np.unique(np.r_[train_indices, np.linspace(0, len(f0) - 1, 64, dtype=int)])
        expected = np.array([float(mp.mpf(float(f0[j])) - mp.fdot(cross[j].tolist(), alpha)) for j in selection])
        gap = float(np.max(abs(predictions[selection] - expected)))
        loss = float(mp.fsum((coeff[j] * mp.exp(-beta * lam[j])) ** 2 for j in range(len(labels))) / len(labels))
    assert gap < 1e-6 and abs(loss - target) < 1e-9
    return {'digits': 70, 'angles_checked': len(selection), 'prediction_error': gap,
            'training_loss_error': abs(loss - target)}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--run', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    run, out = args.run.resolve(), args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    os.environ['MPLCONFIGDIR'] = str(out / 'matplotlib_cache')
    start = time.monotonic()
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('300-second execution limit')))
    signal.alarm(300)
    summary = {'status': 'started', 'command': getattr(sys, 'orig_argv', sys.argv),
               'cwd': os.getcwd(), 'input_hashes': {}, 'source_hashes': {}, 'seeds': {}}
    try:
        for p in (HERE / 'NTK_COMPARE.py', HERE / 'NTK_PLOTS.py', HERE / 'NTK_PLAN.md', HERE / 'PLOTS.py',
                  HERE / 'NETWORK.py', ROOT / 'code/pde/finite_network.py', ROOT / 'docs/NOTATION.md'):
            summary['source_hashes'][str(p)] = digest(p)
        with np.load(run / 'inputs.npz') as z:
            data = {k: z[k] for k in z.files}
        summary['input_hashes'][str(run / 'inputs.npz')] = digest(run / 'inputs.npz')
        idx = np.searchsorted(data['dense_theta'], data['train_theta'])
        assert np.array_equal(data['dense_u'][idx], data['train_u'])
        assert np.array_equal(data['labels'], np.repeat([1., -1., 1., -1.], 4))
        arrays = {k: data[k] for k in ('dense_theta', 'dense_uniform_indices', 'train_theta', 'labels', 'times')}
        arrays['training_indices'] = idx
        labels = data['labels']
        inputs = data['train_u'].astype(np.float32).astype(np.float64)
        dense = data['dense_u'].astype(np.float32).astype(np.float64)
        summary['arithmetic_checks'] = arithmetic_checks()
        print('Maintained-kernel and propagation checks passed.', flush=True)
        for seed in SEEDS:
            folder = run / f'net_n8192_s{seed}'
            record = json.loads((folder / 'record.json').read_text())
            assert record['status'] == 'complete' and record['completed_time'] == 100
            assert record['config']['width'] == 8192 and record['config']['seed'] == seed
            assert record['config']['dtype'] == 'float32'
            assert record['source_sha256'] == digest(HERE / 'NETWORK.py')
            assert record['input_sha256'] == digest(run / 'inputs.npz')
            for path in (folder / 'record.json', folder / 'trajectories.npz'):
                summary['input_hashes'][str(path)] = digest(path)
            assert digest(folder / 'trajectories.npz') == record['output_sha256']['trajectories.npz']
            with np.load(folder / 'trajectories.npz') as z:
                target = float(z['loss'][-1])
                saved_initial = z['predictions'][0, :16].copy()
                saved_gram = z['grams'][0, 1, :16, :16].copy()
                arrays[f'network_seed_{seed}'] = z['dense_predictions'].copy()
                arrays[f'network_loss_{seed}'] = z['loss'].copy()
            rng = np.random.default_rng(seed)
            params = []
            combined = hashlib.sha256()
            for name, shape, scale in (('a', (8192, 2), 1.), ('b', (8192, 8192), np.sqrt(8192)), ('c', (8192,), 8192)):
                raw = rng.standard_normal(shape) / scale
                raw_bytes = memoryview(raw).cast('B')
                assert hashlib.sha256(raw_bytes).hexdigest() == record['initial_float64_sha256'][name]
                combined.update(raw_bytes)
                params.append(raw.astype(np.float32).astype(np.float64))
                del raw_bytes, raw
            assert combined.hexdigest() == record['initial_float64_sha256']['combined_a_b_c']
            train_fields = features(params, inputs)
            blocks = kernel_parts(train_fields, train_fields, inputs, inputs)
            gram_error = float(np.max(abs(blocks[2] - saved_gram)))
            initial_error = float(np.max(abs(train_fields[-1] - saved_initial)))
            assert gram_error < 3e-6 and initial_error < 3e-9
            cross, f0 = [], []
            for first in range(0, len(dense), 256):
                u = dense[first:first + 256]
                field = features(params, u)
                cross.append(kernel_parts(field, train_fields, u, inputs).sum(axis=0))
                f0.append(field[-1])
            cross, f0 = np.concatenate(cross), np.concatenate(f0)
            flow = FrozenFlow(blocks.sum(axis=0), train_fields[-1], labels)
            stop = flow.stop_at_loss(target)
            prediction, train_prediction = flow.predict(cross, f0, stop)
            at100, _ = flow.predict(cross, f0, 100.)
            loss = float(np.mean((prediction[idx] - labels) ** 2))
            identity_error = float(np.max(abs(prediction[idx] - train_prediction)))
            assert abs(loss - target) < 1e-9 and identity_error < 1e-7
            hp = high_precision(blocks.sum(axis=0), cross, f0, idx, labels, stop, prediction, target)
            logtimes = np.r_[0., np.geomspace(.01, stop, 400)]
            arrays.update({f'NTK_seed_{seed}': prediction, f'NTK_t100_seed_{seed}': at100,
                           f'kernel_blocks_seed_{seed}': blocks, f'cross_kernel_seed_{seed}': cross,
                           f'f0_seed_{seed}': f0, f'NTK_loss_seed_{seed}': flow.loss(data['times']),
                           f'NTK_long_times_seed_{seed}': logtimes, f'NTK_long_loss_seed_{seed}': flow.loss(logtimes)})
            summary['seeds'][str(seed)] = {
                'initial_parameter_hashes_match': True, 'initial_prediction_error': initial_error,
                'initial_G2_error': gram_error, 'minimum_kernel_eigenvalue': float(flow.values.min()),
                'stopping_time': stop, 'actual_training_mse': target, 'NTK_training_mse': loss,
                'NTK_T100_mse': float(flow.loss(100.)), 'training_identity_error': identity_error,
                'high_precision': hp}
            print(f'Seed {seed}: matched MSE {loss:.7f}, NTK time {stop:.7g}.', flush=True)
            del params, field, train_fields
            assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024 < 3 * 1024 ** 3
        arrays['actual'] = np.mean([arrays[f'network_seed_{s}'] for s in SEEDS], axis=0, dtype=np.float64)
        arrays['NTK'] = np.mean([arrays[f'NTK_seed_{s}'] for s in SEEDS], axis=0)
        arrays['NTK_t100'] = np.mean([arrays[f'NTK_t100_seed_{s}'] for s in SEEDS], axis=0)
        for order in (1, 3, 5):
            folder = run / f'cl_N{order}_base'
            record = json.loads((folder / 'record.json').read_text())
            assert record['status'] == 'complete' and record['final_time'] == 100.
            for path in (folder / 'record.json', folder / 'trajectories.npz'):
                summary['input_hashes'][str(path)] = digest(path)
            assert digest(folder / 'trajectories.npz') == record['output_sha256']['trajectories.npz']
            with np.load(folder / 'trajectories.npz') as z:
                arrays[f'N{order}'] = z['dense_predictions'].copy()
                arrays[f'N{order}_loss'] = z['loss'].copy()
        uniform = data['dense_uniform_indices']
        summary['models'] = {}
        for key in ('actual', 'N1', 'N3', 'N5', 'NTK'):
            delta = (arrays[key] - arrays['actual'])[uniform]
            if key == 'actual':
                loss = np.mean([summary['seeds'][str(s)]['actual_training_mse'] for s in SEEDS])
            elif key == 'NTK':
                loss = np.mean([summary['seeds'][str(s)]['NTK_training_mse'] for s in SEEDS])
            else:
                loss = arrays[key + '_loss'][-1]
            summary['models'][key] = {'training_mse': float(loss),
                'mean_curve_training_mse': float(np.mean((arrays[key][idx] - labels) ** 2)),
                'uniform_circle_rmse': float(np.sqrt(np.mean(delta ** 2))),
                'uniform_circle_max_error': float(np.max(abs(delta))),
                'output_range': [float(arrays[key].min()), float(arrays[key].max())]}
        with np.load(run / 'cl_N5_base/trajectories.npz') as z:
            assert np.array_equal(arrays['N5'], z['dense_predictions'])
        np.savez_compressed(out / 'ntk_predictions.npz', **arrays)
        from NTK_PLOTS import render
        render(run, out, data, arrays, summary)
        summary.update({'status': 'complete', 'exit_status': 0,
                        'versions': {'python': sys.version, 'numpy': np.__version__, 'scipy': scipy.__version__, 'mpmath': mp.__version__},
                        'device': 'CPU', 'blas_threads': 2, 'reference': 'width8192 mean of seeds11/29/47',
                        'comparison': 'NTK stopped separately per seed at corresponding network T100 loss; network and closures stay at T100.',
                        'gram_scope': 'Output NTK defines no nonlinear hidden Gram trajectory; existing frozen-hidden baselines retained.'})
        products = [p for p in out.rglob('*') if p.is_file() and 'matplotlib_cache' not in p.parts]
        assert sum(p.stat().st_size for p in products) < 100 * 1024 ** 2
        summary['products'] = {str(p.relative_to(out)): digest(p) for p in products}
    except BaseException as error:
        summary.update({'status': 'failed', 'exit_status': 1, 'exception': repr(error)})
        raise
    finally:
        signal.alarm(0)
        summary['wall_seconds'] = time.monotonic() - start
        summary['peak_rss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
        (out / 'ntk_comparison.json').write_text(json.dumps(summary, indent=2, allow_nan=False) + '\n')
    print(json.dumps({k: summary[k] for k in ('status', 'models', 'wall_seconds', 'radius_offset')}, indent=2))


if __name__ == '__main__':
    main()
