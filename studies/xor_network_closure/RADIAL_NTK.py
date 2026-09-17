#!/usr/bin/env python3
"""Add the matched initial-NTK prediction to the saved radial endpoint figure."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import signal
import sys
import time

sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '2'
import numpy as np
import scipy
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code'))
from pde import finite_network as reference


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def array_sha(array):
    return hashlib.sha256(memoryview(np.ascontiguousarray(array)).cast('B')).hexdigest()


def fields(parameters, directions):
    w1, w2, c = parameters
    z1 = w1 @ directions.T
    h1 = np.tanh(z1)
    z2 = w2 @ h1
    h2 = np.tanh(z2)
    d2 = c[:, None] * reference.TANH.derivative(z2)
    d1 = (w2.T @ d2) * reference.TANH.derivative(z1)
    return h1, h2, d1, d2, c @ h2 / c.size


def cross_blocks(left, right, left_inputs, right_inputs):
    h1, h2, d1, d2, _ = left
    g1, g2, e1, e2, _ = right
    n = h1.shape[0]
    return np.stack(((d1.T @ e1 / n) * (left_inputs @ right_inputs.T),
                     (h1.T @ g1 / n) * (d2.T @ e2 / n),
                     h2.T @ g2 / n))


def propagate(kernel, cross, f0_train, f0_test, labels, horizon):
    eigenvalues, vectors = np.linalg.eigh(kernel)
    assert np.min(eigenvalues) >= -1e-11
    assert np.max(np.abs(kernel - kernel.T)) <= 1e-11
    rate_time = 2 * horizon / len(labels)
    q = np.full_like(eigenvalues, rate_time)
    nonzero = eigenvalues != 0
    q[nonzero] = -np.expm1(-rate_time * eigenvalues[nonzero]) / eigenvalues[nonzero]
    coefficients = vectors.T @ (f0_train - labels)
    prediction = f0_test - cross @ (vectors @ (q * coefficients))
    training = labels + vectors @ (np.exp(-rate_time * eigenvalues) * coefficients)
    return prediction, training, eigenvalues


def check():
    rng = np.random.default_rng(107)
    params = reference.initialize(13, 2, 2, seed=5)
    # Order-one readout exercises every block, which is essential for this check.
    params = reference.Parameters(params.weights, rng.normal(size=13))
    inputs = rng.normal(size=(9, 2))
    inputs /= np.linalg.norm(inputs, axis=1)[:, None]
    parameters = (*params.weights, params.readout)
    observed = cross_blocks(fields(parameters, inputs[:5]),
                            fields(parameters, inputs[5:]), inputs[:5], inputs[5:])
    expected = reference.kernel_blocks(params, np.sqrt(2) * inputs.T)[:, :5, 5:]
    errors = {'kernel_blocks_vs_maintained': float(np.max(np.abs(observed - expected)))}
    assert errors['kernel_blocks_vs_maintained'] <= 2e-12
    # Independently solve the coupled train/test residual system by a matrix exponential.
    all_kernel = reference.kernel(params, np.sqrt(2) * inputs.T)
    initial = reference.forward(params, np.sqrt(2) * inputs.T).output
    labels = rng.normal(size=4)
    for label, k, cross in (
            ('full', all_kernel[:4, :4], all_kernel[4:, :4]),
            ('singular', np.diag([0., .1, 0., .8]), rng.normal(size=(5, 4)))):
        pred, train, _ = propagate(k, cross, initial[:4], initial[4:], labels, 100.)
        generator = np.zeros((9, 9))
        generator[:4, :4] = -2 * k / 4
        generator[4:, :4] = -2 * cross / 4
        direct = expm(100 * generator) @ np.r_[initial[:4] - labels, initial[4:]]
        errors[f'{label}_exponential'] = float(np.max(np.abs(pred - direct[4:])))
        errors[f'{label}_training'] = float(np.max(np.abs(train - labels - direct[:4])))
        assert errors[f'{label}_exponential'] <= 2e-11
        assert errors[f'{label}_training'] <= 2e-11
    return errors


def plot(output, arrays):
    os.environ['MPLCONFIGDIR'] = str(output / 'matplotlib_cache')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans', 'savefig.dpi': 200})
    fig, ax = plt.subplots(figsize=(10.4, 11.5), subplot_kw={'projection': 'polar'})
    fig.subplots_adjust(top=.805, bottom=.15, left=.09, right=.91)
    ax.set_theta_zero_location('E')
    ax.set_theta_direction(1)
    ax.set_ylim(0, 3.42)
    ax.set_xticks(np.arange(12) * np.pi / 6)
    ax.set_xticklabels([f'{d}°' for d in range(0, 360, 30)])
    ax.tick_params(axis='x', pad=9)
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels([r'$f=-1$', r'$f=0$', r'$f=+1$'])
    ax.set_rlabel_position(315)
    ax.grid(color='#B8BDC5', alpha=.42, linewidth=.7)
    ax.spines['polar'].set_visible(False)
    circle = np.linspace(0, 2 * np.pi, 721)
    ax.plot(circle, np.full(721, 2.), color='#8A929E', lw=1.7, ls=(0, (3, 3)), zorder=2)
    positive, negative = '#C84848', '#3269B8'
    for angle, y in zip(arrays['training_angles'], arrays['labels']):
        ax.plot([angle, angle], [2, 2 + y], color=positive if y > 0 else negative,
                alpha=.4, lw=.9, ls=':', zorder=3)
    styles = [('actual', '#171C26', '-', 2.5, 'Actual network'),
              ('N1', '#E08A25', (0, (5, 2)), 2.1, r'$N=1$ closure'),
              ('N3', '#7862B3', (0, (5, 2, 1, 2)), 2., r'$N=3$ closure'),
              ('N5', '#008A83', (0, (1, 1.4)), 2.5, r'$N=5$ closure'),
              ('NTK', '#C72B85', (0, (7, 2)), 2.5, 'Frozen initial NTK')]
    theta = np.r_[arrays['angles'], arrays['angles'][0] + 2 * np.pi]
    handles = []
    for key, color, style, width, label in styles:
        radii = 2 + np.r_[arrays[key], arrays[key][0]]
        assert 0 < radii.min() and radii.max() < 3.42
        line, = ax.plot(theta, radii, color=color, lw=width, ls=style, label=label, zorder=5)
        handles.append(line)
    for y, color in ((1, positive), (-1, negative)):
        select = arrays['labels'] == y
        angles = arrays['training_angles'][select]
        ax.scatter(angles, np.full(select.sum(), 2.), s=45, c=color,
                   edgecolors='white', linewidths=.75, zorder=8)
        ax.scatter(angles, np.full(select.sum(), 2 + y), s=51, marker='D',
                   facecolors='white', edgecolors=color, linewidths=1.35, zorder=9)
    fig.suptitle('Final output around the circle', fontsize=20, fontweight='semibold', y=.98)
    fig.text(.5, .942, r'$t=100\qquad \rho(\theta)=2+f(\theta)$', ha='center', fontsize=14)
    fig.legend(handles=handles[:4], loc='upper center', bbox_to_anchor=(.5, .915),
               ncol=4, frameon=False, handlelength=2.6, fontsize=11)
    fig.legend(handles=handles[4:], loc='upper center', bbox_to_anchor=(.5, .879),
               frameon=False, handlelength=3.2, fontsize=12)
    legend_inputs = [
        Line2D([], [], marker='o', color='none', markerfacecolor=positive,
               markeredgecolor='white', markersize=7, label='+1 training input'),
        Line2D([], [], marker='o', color='none', markerfacecolor=negative,
               markeredgecolor='white', markersize=7, label='−1 training input'),
        Line2D([], [], marker='D', color='none', markerfacecolor='white',
               markeredgecolor='#526071', markersize=7, label='Desired output at that input')]
    fig.legend(handles=legend_inputs, loc='lower center', bbox_to_anchor=(.5, .078),
               ncol=3, frameon=False, fontsize=11)
    fig.text(.5, .062, 'Dots mark inputs; diamonds mark targets. Positive outputs extend outward.',
             ha='center', fontsize=10.5, color='#39404B')
    fig.text(.5, .039, 'Network and NTK: width 8192, mean of the same three seeds.',
             ha='center', fontsize=10.5, color='#596271')
    fig.text(.5, .017, 'NTK frozen at initialization; same training time and learning-rate scaling.',
             ha='center', fontsize=10.5, color='#596271')
    for ext in ('png', 'pdf', 'svg'):
        fig.savefig(output / f'final_radial_output_ntk.{ext}', bbox_inches='tight', facecolor='white')
    plt.close(fig)
    return matplotlib.__version__


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--base', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('300-second budget')))
    signal.alarm(300)
    record = {'status': 'started', 'command': getattr(sys, 'orig_argv', sys.argv),
              'cwd': os.getcwd(), 'input_hashes': {}, 'source_hashes': {},
              'scope': 'Existing radial plot plus initial full mobility-weighted NTK, no network training.'}
    record_path = output / 'radial_ntk.json'
    try:
        for path in (Path(__file__), Path(__file__).with_name('RADIAL_NTK_PLAN.md'),
                     ROOT / 'code/pde/finite_network.py', ROOT / 'docs/NOTATION.md'):
            record['source_hashes'][str(path)] = sha(path)
        base = args.base.resolve()
        run = args.run.resolve()
        prior = json.loads((base / 'radial_output.json').read_text())
        assert sha(base / 'radial_predictions.npz') == prior['products']['radial_predictions.npz']
        for path in (base / 'radial_output.json', base / 'radial_predictions.npz', run / 'inputs.npz'):
            record['input_hashes'][str(path)] = sha(path)
        with np.load(base / 'radial_predictions.npz') as z:
            arrays = {key: z[key] for key in z.files}
        with np.load(run / 'inputs.npz') as z:
            inputs, labels = z['inputs'], z['labels']
        assert np.array_equal(inputs, arrays['directions'][arrays['training_indices']])
        assert np.array_equal(labels, arrays['labels'])
        directions = arrays['directions'].astype(np.float32).astype(np.float64)
        inputs = inputs.astype(np.float32).astype(np.float64)
        record['checks'] = check()
        record['seeds'] = {}
        print('Kernel and exact propagation checks passed.', flush=True)
        for seed in (11, 29, 47):
            folder = run / 'network' / f'n8192_s{seed}'
            source_record = json.loads((folder / 'record.json').read_text())
            assert source_record['status'] == 'complete'
            assert source_record['config'] == {'dtype': 'float32', 'name': f'n8192_s{seed}',
                                               'seed': seed, 'step': .01, 'width': 8192}
            for filename in ('record.json', 'observations.npz', 'gram.npy'):
                path = folder / filename
                record['input_hashes'][str(path)] = sha(path)
                if filename != 'record.json':
                    assert sha(path) == source_record['output_hashes'][filename]['sha256']
            with np.load(folder / 'observations.npz') as z:
                initial_saved = z['predictions'][0, :16]
                actual_loss = float(z['loss'][-1])
            saved_gram = np.load(folder / 'gram.npy', mmap_mode='r')[0, 1, :16, :16]
            rng = np.random.default_rng(seed)
            n = 8192
            parameters = []
            for key, shape, divisor in (('W1', (n, 2), 1.), ('W2', (n, n), np.sqrt(n)),
                                        ('c', (n,), n)):
                initial = rng.standard_normal(shape) / divisor
                assert array_sha(initial) == source_record['initial_float64_arrays'][key]['sha256']
                working = initial.astype(np.float32)
                assert array_sha(working) == source_record['initial_working_arrays'][key]['sha256']
                parameters.append(working.astype(np.float64))
                del initial, working
            training = fields(parameters, inputs)
            blocks = cross_blocks(training, training, inputs, inputs)
            kernel = blocks.sum(axis=0)
            f0 = training[-1]
            initial_error = float(np.max(np.abs(f0 - initial_saved)))
            gram_error = float(np.max(np.abs(blocks[2] - saved_gram)))
            assert initial_error <= 3e-9 and gram_error <= 3e-6
            values, readout_values = [], []
            cross_values, initial_values = [], []
            for offset in range(0, len(directions), 256):
                batch = directions[offset:offset + 256]
                evaluated = fields(parameters, batch)
                cross = cross_blocks(evaluated, training, batch, inputs)
                pred, endpoint, eigenvalues = propagate(kernel, cross.sum(axis=0), f0,
                                                        evaluated[-1], labels, 100.)
                readout, _, _ = propagate(blocks[2], cross[2], f0, evaluated[-1], labels, 100.)
                values.append(pred)
                readout_values.append(readout)
                cross_values.append(cross)
                initial_values.append(evaluated[-1])
                del evaluated, cross
            values, readout_values = np.concatenate(values), np.concatenate(readout_values)
            train_values = values[arrays['training_indices']]
            endpoint_error = float(np.max(np.abs(train_values - endpoint)))
            assert endpoint_error <= 2e-11
            assert np.isfinite(values).all()
            arrays[f'NTK_seed_{seed}'] = values
            arrays[f'frozen_readout_seed_{seed}'] = readout_values
            arrays[f'kernel_blocks_seed_{seed}'] = blocks
            arrays[f'cross_blocks_seed_{seed}'] = np.concatenate(cross_values, axis=1)
            arrays[f'f0_seed_{seed}'] = np.concatenate(initial_values)
            record['seeds'][str(seed)] = {
                'initial_parameter_hashes_match': True, 'initial_prediction_error': initial_error,
                'initial_gram_error': gram_error, 'training_endpoint_identity_error': endpoint_error,
                'kernel_min_eigenvalue': float(eigenvalues.min()),
                'kernel_hidden_block_abs_max': float(np.max(np.abs(blocks[:2].sum(axis=0)))),
                'NTK_training_mse': float(np.mean((train_values - labels) ** 2)),
                'actual_training_mse': actual_loss,
                'NTK_vs_readout_max_difference': float(np.max(np.abs(values - readout_values)))}
            del parameters, training, blocks, kernel
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
            assert rss <= 3 * 1024 ** 3
            print(f'Seed {seed}: NTK MSE={record["seeds"][str(seed)]["NTK_training_mse"]:.6f}; '
                  f'actual MSE={actual_loss:.6f}.', flush=True)
            record_path.write_text(json.dumps(record, indent=2) + '\n')
        arrays['NTK'] = np.mean([arrays[f'NTK_seed_{s}'] for s in (11, 29, 47)], axis=0)
        arrays['frozen_readout'] = np.mean([arrays[f'frozen_readout_seed_{s}'] for s in (11, 29, 47)], axis=0)
        with np.load(base / 'radial_predictions.npz') as z:
            assert all(np.array_equal(arrays[key], z[key]) for key in z.files)
        np.savez(output / 'radial_predictions.npz', **arrays)
        matplotlib_version = plot(output, arrays)
        seed_records = list(record['seeds'].values())
        record.update({
            'status': 'complete', 'exit_status': 0, 'physical_time': 100, 'radius_offset': 2,
            'prior_arrays_unchanged': True,
            'NTK_mean_seed_training_mse': float(np.mean([r['NTK_training_mse'] for r in seed_records])),
            'actual_mean_seed_training_mse': float(np.mean([r['actual_training_mse'] for r in seed_records])),
            'NTK_mean_curve_training_mse': float(np.mean((arrays['NTK'][arrays['training_indices']] - labels) ** 2)),
            'actual_mean_curve_training_mse': float(np.mean((arrays['actual'][arrays['training_indices']] - labels) ** 2)),
            'NTK_mean_curve_max_difference_from_actual': float(np.max(np.abs(arrays['NTK'] - arrays['actual']))),
            'NTK_mean_curve_max_difference_from_readout': float(np.max(np.abs(arrays['NTK'] - arrays['frozen_readout']))),
            'environment': {'python': sys.version, 'numpy': np.__version__, 'scipy': scipy.__version__,
                            'matplotlib': matplotlib_version, 'platform': platform.platform(),
                            'device': 'CPU', 'blas_threads': 2, 'evaluation_precision': 'float64',
                            'parameters_and_inputs': 'original float32 values promoted to float64'},
            'products': {path.name: sha(path) for path in output.iterdir()
                         if path.is_file() and path != record_path}})
    except BaseException as error:
        record.update({'status': 'failed', 'exit_status': 1, 'exception': repr(error)})
        raise
    finally:
        signal.alarm(0)
        record['wall_seconds'] = time.monotonic() - started
        record['peak_rss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
        record_path.write_text(json.dumps(record, indent=2, allow_nan=False) + '\n')
    print(json.dumps({key: record[key] for key in ('status', 'wall_seconds', 'NTK_mean_seed_training_mse',
                                                 'actual_mean_seed_training_mse',
                                                 'NTK_mean_curve_max_difference_from_actual',
                                                 'NTK_mean_curve_max_difference_from_readout')}, indent=2))


if __name__ == '__main__':
    main()
