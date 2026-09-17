#!/usr/bin/env python3
"""Compare the retained final functions with a frozen NTK at matched training MSE."""
import argparse
import json
import os
from pathlib import Path
import signal
import sys
import time

sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '2'
import numpy as np
import mpmath as mp
from RADIAL_NTK import sha, propagate


def stopping_time(kernel, residual, target):
    lam, vectors = np.linalg.eigh(kernel)
    assert lam.min() > 0
    coefficients = vectors.T @ residual
    def loss(t):
        return float(np.mean(coefficients ** 2 * np.exp(-4 * t * lam / residual.size)))
    low, high = 0., 100.
    for _ in range(60):
        if loss(high) <= target:
            break
        high *= 2
    else:
        raise RuntimeError('No matching time within the predeclared bracket budget')
    for _ in range(90):
        middle = (low + high) / 2
        if loss(middle) > target:
            low = middle
        else:
            high = middle
    assert abs(loss(high) - target) < 1e-9
    return high, loss(high)


def high_precision_check(kernel, cross, f0, indices, labels, horizon, prediction, target):
    with mp.workdps(70):
        k = mp.matrix(kernel.tolist())
        residual = mp.matrix((f0[indices] - labels).tolist())
        lam, vectors = mp.eigsy(k)
        coefficients = vectors.T * residual
        rate_time = mp.mpf(2) * horizon / len(labels)
        q = mp.matrix([-mp.expm1(-rate_time * value) / value for value in lam])
        alpha = vectors * mp.matrix([q[i] * coefficients[i] for i in range(len(labels))])
        checked_indices = np.unique(np.r_[np.linspace(0, len(f0) - 1, 64, dtype=int), indices])
        expected = np.array([float(mp.mpf(float(f0[j])) - mp.fdot(cross[j].tolist(), alpha))
                             for j in checked_indices])
        error = float(np.max(np.abs(prediction[checked_indices] - expected)))
        loss = float(mp.fsum((coefficients[i] * mp.exp(-rate_time * lam[i])) ** 2
                            for i in range(len(labels))) / len(labels))
    assert error < 1e-6
    assert abs(loss - target) < 1e-9
    return {'decimal_digits': 70, 'checked_angle_count': len(checked_indices),
            'max_prediction_difference': error, 'loss': loss,
            'loss_difference_from_target': abs(loss - target)}


def make_plots(output, arrays, summary):
    os.environ['MPLCONFIGDIR'] = str(output / 'matplotlib_cache')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans', 'savefig.dpi': 200})
    keys = ('actual', 'N1', 'N3', 'N5', 'NTK_matched')
    maximum = max(float(np.max(np.abs(arrays[key]))) for key in keys)
    radius = 2 if maximum < 2 else int(np.ceil(maximum)) + 1
    summary['radius_offset'] = radius
    styles = [('actual', '#171C26', '-', 2.5, 'Actual network'),
              ('N1', '#E08A25', (0, (5, 2)), 2.1, r'$N=1$ closure'),
              ('N3', '#7862B3', (0, (5, 2, 1, 2)), 2., r'$N=3$ closure'),
              ('N5', '#008A83', (0, (1, 1.4)), 2.5, r'$N=5$ closure'),
              ('NTK_matched', '#C72B85', (0, (7, 2)), 2.5, 'Frozen NTK — matched training loss')]
    fig, ax = plt.subplots(figsize=(10.4, 11.5), subplot_kw={'projection': 'polar'})
    fig.subplots_adjust(top=.805, bottom=.17, left=.09, right=.91)
    ax.set_theta_zero_location('E')
    ax.set_theta_direction(1)
    ax.set_ylim(0, max(3.42, radius + maximum + .25))
    ax.set_xticks(np.arange(12) * np.pi / 6)
    ax.set_xticklabels([f'{d}°' for d in range(0, 360, 30)])
    ax.tick_params(axis='x', pad=9)
    ticks = [-1, 0, 1] if maximum <= 1.5 else list(range(-int(np.ceil(maximum)) + 1,
                                                          int(np.ceil(maximum))))
    if 0 not in ticks:
        ticks.append(0)
        ticks.sort()
    ax.set_yticks([radius + value for value in ticks])
    ax.set_yticklabels([f'$f={value:+d}$' if value else '$f=0$' for value in ticks])
    ax.set_rlabel_position(315)
    ax.grid(color='#B8BDC5', alpha=.42, linewidth=.7)
    ax.spines['polar'].set_visible(False)
    circle = np.linspace(0, 2 * np.pi, 721)
    ax.plot(circle, np.full(721, radius), color='#8A929E', lw=1.7, ls=(0, (3, 3)), zorder=2)
    positive, negative = '#C84848', '#3269B8'
    for angle, y in zip(arrays['training_angles'], arrays['labels']):
        ax.plot([angle, angle], [radius, radius + y], color=positive if y > 0 else negative,
                alpha=.4, lw=.9, ls=':', zorder=3)
    theta = np.r_[arrays['angles'], arrays['angles'][0] + 2 * np.pi]
    handles = []
    for key, color, style, width, label in styles:
        radii = radius + np.r_[arrays[key], arrays[key][0]]
        assert 0 < radii.min() and radii.max() < ax.get_ylim()[1]
        line, = ax.plot(theta, radii, color=color, lw=width, ls=style, label=label, zorder=5)
        handles.append(line)
    for y, color in ((1, positive), (-1, negative)):
        select = arrays['labels'] == y
        angles = arrays['training_angles'][select]
        ax.scatter(angles, np.full(select.sum(), radius), s=45, c=color,
                   edgecolors='white', linewidths=.75, zorder=8)
        ax.scatter(angles, np.full(select.sum(), radius + y), s=51, marker='D',
                   facecolors='white', edgecolors=color, linewidths=1.35, zorder=9)
    fig.suptitle('Output around the circle at comparable training loss', fontsize=17.5,
                 fontweight='semibold', y=.98)
    fig.text(.5, .942, rf'$\rho(\theta)={radius}+f(\theta)$', ha='center', fontsize=14)
    fig.legend(handles=handles[:4], loc='upper center', bbox_to_anchor=(.5, .915),
               ncol=4, frameon=False, handlelength=2.6, fontsize=11)
    fig.legend(handles=handles[4:], loc='upper center', bbox_to_anchor=(.5, .879),
               frameon=False, handlelength=3.2, fontsize=12)
    inputs_legend = [
        Line2D([], [], marker='o', color='none', markerfacecolor=positive,
               markeredgecolor='white', markersize=7, label='+1 training input'),
        Line2D([], [], marker='o', color='none', markerfacecolor=negative,
               markeredgecolor='white', markersize=7, label='−1 training input'),
        Line2D([], [], marker='D', color='none', markerfacecolor='white',
               markeredgecolor='#526071', markersize=7, label='Desired output at that input')]
    fig.legend(handles=inputs_legend, loc='lower center', bbox_to_anchor=(.5, .096),
               ncol=3, frameon=False, fontsize=11)
    times = [record['stopping_time'] for record in summary['seeds'].values()]
    fig.text(.5, .079, 'Network and closures: t = 100. NTK stopped when each seed matches network loss.',
             ha='center', fontsize=10.5, color='#39404B')
    fig.text(.5, .055, f'Mean training MSE: network {summary["actual_mean_seed_mse"]:.6f}; '
             f'NTK {summary["NTK_mean_seed_mse"]:.6f}.', ha='center', fontsize=10.5, color='#39404B')
    fig.text(.5, .031, f'NTK stopping times: {min(times)/1e6:.2f}–{max(times)/1e6:.2f} million. '
             'Width 8192; same three seeds.', ha='center', fontsize=10.5, color='#596271')
    if radius != 2:
        fig.text(.5, .009, f'Common reference radius increased to {radius} to keep all plotted radii positive.',
                 ha='center', fontsize=10.5, color='#596271')
    for ext in ('png', 'pdf', 'svg'):
        fig.savefig(output / f'final_radial_output_matched_ntk.{ext}', bbox_inches='tight', facecolor='white')
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 5.3))
    for key, color, style, width, label in styles:
        ax.plot(np.degrees(theta), np.r_[arrays[key], arrays[key][0]], color=color,
                ls=style, lw=width, label=label)
    for y, color in ((1, positive), (-1, negative)):
        select = arrays['labels'] == y
        ax.scatter(np.degrees(arrays['training_angles'][select]), arrays['labels'][select],
                   marker='D', s=40, facecolors='white', edgecolors=color, zorder=8)
    ax.set(xlim=(0, 360), xlabel='Input angle (degrees)', ylabel='Output f(θ)',
           title='Comparable training loss; network and closures at t = 100')
    ax.set_xticks(np.arange(0, 361, 30))
    ax.grid(alpha=.2)
    ax.axhline(0, color='gray', ls=':', lw=1)
    ax.legend(loc='upper center', bbox_to_anchor=(.5, -.17), ncol=3, frameon=False, fontsize=10)
    fig.subplots_adjust(bottom=.27)
    for ext in ('png', 'pdf'):
        fig.savefig(output / f'output_vs_angle_matched_ntk.{ext}', bbox_inches='tight', facecolor='white')
    plt.close(fig)
    return matplotlib.__version__


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('120-second budget')))
    signal.alarm(120)
    record = {'status': 'started', 'command': getattr(sys, 'orig_argv', sys.argv), 'cwd': os.getcwd()}
    try:
        base = args.base.resolve()
        prior_path = base / 'radial_ntk.json'
        prior = json.loads(prior_path.read_text())
        assert prior['status'] == 'complete'
        data_path = base / 'radial_predictions.npz'
        assert sha(data_path) == prior['products']['radial_predictions.npz']
        record['input_hashes'] = {str(path): sha(path) for path in (prior_path, data_path)}
        record['source_hashes'] = {str(path): sha(path) for path in (
            Path(__file__), Path(__file__).with_name('MATCHED_NTK_PLAN.md'),
            Path(__file__).with_name('RADIAL_NTK.py'))}
        for path, digest in prior['source_hashes'].items():
            assert sha(path) == digest
        with np.load(data_path) as z:
            arrays = {key: z[key] for key in z.files}
        indices, labels = arrays['training_indices'], arrays['labels']
        record['seeds'] = {}
        for seed in (11, 29, 47):
            kernel = arrays[f'kernel_blocks_seed_{seed}'].sum(axis=0)
            cross = arrays[f'cross_blocks_seed_{seed}'].sum(axis=0)
            f0 = arrays[f'f0_seed_{seed}']
            target = prior['seeds'][str(seed)]['actual_training_mse']
            horizon, spectral_loss = stopping_time(kernel, f0[indices] - labels, target)
            prediction, train, _ = propagate(kernel, cross, f0[indices], f0, labels, horizon)
            reconstructed_loss = float(np.mean((prediction[indices] - labels) ** 2))
            error = float(np.max(np.abs(prediction[indices] - train)))
            assert error < 1e-7 and abs(reconstructed_loss - target) < 1e-9
            hp = high_precision_check(kernel, cross, f0, indices, labels, horizon, prediction, target)
            arrays[f'NTK_matched_seed_{seed}'] = prediction
            record['seeds'][str(seed)] = {
                'target_actual_mse': target, 'stopping_time': horizon, 'spectral_mse': spectral_loss,
                'NTK_training_mse': reconstructed_loss, 'training_prediction_identity_error': error,
                'high_precision_check': hp}
        arrays['NTK_matched'] = np.mean([arrays[f'NTK_matched_seed_{seed}'] for seed in (11, 29, 47)], axis=0)
        with np.load(data_path) as z:
            assert all(np.array_equal(arrays[key], z[key]) for key in z.files)
        keys = ('actual', 'N1', 'N3', 'N5', 'NTK_matched')
        record.update({
            'prior_arrays_unchanged': True,
            'actual_mean_seed_mse': float(np.mean([s['target_actual_mse'] for s in record['seeds'].values()])),
            'NTK_mean_seed_mse': float(np.mean([s['NTK_training_mse'] for s in record['seeds'].values()])),
            'plotted_curve_training_mse': {k: float(np.mean((arrays[k][indices] - labels) ** 2)) for k in keys},
            'circle_max_difference_from_actual': {k: float(np.max(np.abs(arrays[k] - arrays['actual']))) for k in keys},
            'circle_output_range': {k: [float(arrays[k].min()), float(arrays[k].max())] for k in keys},
            'comparison': 'Network/closures at t=100; each frozen NTK seed stopped at its network seed training loss.'})
        np.savez(output / 'radial_predictions.npz', **arrays)
        version = make_plots(output, arrays, record)
        files = [p for p in output.iterdir() if p.is_file()]
        assert sum(p.stat().st_size for p in files) < 100 * 1024 ** 2
        record.update({'status': 'complete', 'exit_status': 0,
                       'products': {p.name: sha(p) for p in files},
                       'versions': {'python': sys.version, 'numpy': np.__version__,
                                    'mpmath': mp.__version__, 'matplotlib': version},
                       'device': 'CPU', 'blas_threads': 2})
    except BaseException as error:
        record.update({'status': 'failed', 'exit_status': 1, 'exception': repr(error)})
        raise
    finally:
        signal.alarm(0)
        record['wall_seconds'] = time.monotonic() - started
        (output / 'matched_ntk.json').write_text(json.dumps(record, indent=2, allow_nan=False) + '\n')
    print(json.dumps({k: record[k] for k in ('status', 'seeds', 'plotted_curve_training_mse',
                                          'circle_max_difference_from_actual', 'circle_output_range',
                                          'radius_offset', 'wall_seconds')}, indent=2))


if __name__ == '__main__':
    main()
