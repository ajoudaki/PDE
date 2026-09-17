"""Study-local plot extension for the matched-loss frozen initial tangent kernel."""
from pathlib import Path
import shutil
import subprocess
import hashlib

import matplotlib.pyplot as plt
import numpy as np
from PLOTS import COLORS, STYLE, relative_gram, set_style

SEEDS = (11, 29, 47)
NTK_COLOR = '#C32683'
CURVES = [('actual', COLORS['reference'], '-', 'Actual network'),
          ('N1', COLORS[1], STYLE[1], 'Closure N=1'),
          ('N3', COLORS[3], STYLE[3], 'Closure N=3'),
          ('N5', COLORS[5], STYLE[5], 'Closure N=5'),
          ('NTK', NTK_COLOR, (0, (6, 2)), 'Frozen NTK — matched loss')]


def render(run, out, inputs, arrays, summary):
    set_style()
    directory = out / 'figures'
    directory.mkdir()
    times = inputs['times']
    theta = inputs['dense_theta']
    degrees = np.degrees(theta)
    train_degrees = inputs['train_degrees']
    labels = inputs['labels']
    indices = arrays['training_indices']
    closed_theta = np.r_[theta, theta[0] + 2 * np.pi]
    close = lambda f: np.r_[f, f[0]]
    network_seeds = np.array([arrays[f'network_seed_{s}'] for s in SEEDS])
    ntk_seeds = np.array([arrays[f'NTK_seed_{s}'] for s in SEEDS])
    all_values = np.concatenate([arrays[key] for key, *_ in CURVES] + [network_seeds.ravel(), ntk_seeds.ravel()])
    radius = 2. if np.min(all_values) > -2 else float(np.ceil(np.max(abs(all_values))) + 1)
    outer = radius + max(1., float(all_values.max())) + .3
    summary['radius_offset'] = radius
    stops = [summary['seeds'][str(seed)]['stopping_time'] for seed in SEEDS]
    actual_loss = summary['models']['actual']['training_mse']
    ntk_loss = summary['models']['NTK']['training_mse']

    def save(fig, stem):
        for ext in ('png', 'pdf'):
            fig.savefig(directory / f'{stem}.{ext}', dpi=190, bbox_inches='tight', facecolor='white')
        plt.close(fig)

    def radial(ax, selected):
        ax.set_theta_zero_location('E')
        ax.set_theta_direction(1)
        ax.plot(closed_theta, np.full_like(closed_theta, radius), color='#939DA6', ls=':', lw=1.4)
        ax.fill_between(closed_theta, radius + close(network_seeds.min(axis=0)),
                        radius + close(network_seeds.max(axis=0)), color=COLORS['reference'], alpha=.15)
        for key, color, style, name in CURVES:
            if key not in selected:
                continue
            r = radius + close(arrays[key])
            assert r.min() > 0 and r.max() < outer
            ax.plot(closed_theta, r, color=color, ls=style, lw=2.4 if key in ('actual', 'NTK') else 1.9, label=name)
        ax.scatter(inputs['train_theta'], np.full(16, radius), s=25, marker='o', facecolors='white',
                   edgecolors='#353F48', linewidths=.85, zorder=7, label='Training directions')
        for sign, color, marker in ((1, '#2369A2', '+'), (-1, '#BD3F47', '_')):
            take = labels == sign
            ax.scatter(inputs['train_theta'][take], radius + labels[take], color=color, marker=marker,
                       s=85, linewidths=1.7, zorder=8, label=f'Target {sign:+d}')
        ax.set_ylim(0, outer)
        ax.set_thetagrids(np.arange(0, 360, 45))
        ax.set_rlabel_position(215)
        ax.set_yticks([radius - 1, radius, radius + 1])
        ax.set_yticklabels(['f=−1', 'f=0', 'f=+1'])
        ax.grid(alpha=.7)
        ax.spines['polar'].set_color('#CDD3D8')

    fig, ax = plt.subplots(figsize=(10.4, 8.4), subplot_kw={'projection': 'polar'})
    fig.subplots_adjust(left=.06, right=.77, top=.83, bottom=.19)
    radial(ax, [k for k, *_ in CURVES])
    fig.suptitle('First-quadrant training: output at comparable loss', fontsize=16, y=.975)
    fig.text(.43, .925, f'Radius = {radius:g} + f(θ)', ha='center', fontsize=12)
    ax.legend(loc='upper left', bbox_to_anchor=(1.13, 1.03), frameon=False, fontsize=10)
    fig.text(.50, .115, 'Network and closures at T=100; NTK stopped at the matching training loss.', ha='center', fontsize=10)
    fig.text(.50, .080, f'Mean training MSE: network {actual_loss:.7f}; NTK {ntk_loss:.7f}.', ha='center', fontsize=10)
    fig.text(.50, .045, f'NTK physical stopping times: {min(stops):.4g}–{max(stops):.4g}; mean of the same three seeds.',
             ha='center', fontsize=9, color='#586570')
    if radius != 2:
        fig.text(.50, .015, 'Reference radius enlarged to display all predictions without negative radii.', ha='center', fontsize=9)
    save(fig, 'radial_overlay')

    fig, axes = plt.subplots(2, 2, figsize=(11, 11), subplot_kw={'projection': 'polar'}, constrained_layout=True)
    for ax, key in zip(axes.flat, ('N1', 'N3', 'N5', 'NTK')):
        radial(ax, ('actual', key))
        ax.set_title(f'{key if key != "NTK" else "NTK at matched loss"} and network reference', pad=20)
    fig.suptitle(f'Common radial scale R={radius:g}; black = network at T=100', fontsize=15)
    save(fig, 'radial_individual')

    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.5), constrained_layout=True)
    for ax, end in zip(axes, (360, 90)):
        ax.fill_between(degrees, network_seeds.min(axis=0), network_seeds.max(axis=0),
                        color=COLORS['reference'], alpha=.14)
        for key, color, style, name in CURVES:
            ax.plot(degrees, arrays[key], color=color, ls=style, lw=2.1, label=name)
        ax.scatter(train_degrees, labels, marker='x', color='#232C34', s=32, zorder=8, label='Training targets')
        ax.axhline(0, color='#9DA7AE', lw=.7)
        ax.set(xlim=(0, end), xlabel='Angle θ (degrees)', ylabel='Output f(θ)',
               title='Entire circle' if end == 360 else 'Training quadrant')
        ax.set_xticks(np.arange(0, end + 1, 60 if end == 360 else 15))
        if end == 90:
            vals = np.concatenate([arrays[k][degrees <= 90 + 1e-10] for k, *_ in CURVES] + [labels])
            padding = .1 * np.ptp(vals)
            ax.set_ylim(vals.min() - padding, vals.max() + padding)
        ax.grid(alpha=.7)
    axes[0].legend(loc='best', fontsize=8.5, framealpha=.95)
    fig.suptitle('Matched training loss: network/closures at T=100; NTK trained longer', fontsize=14)
    save(fig, 'output_vs_angle')

    fig, ax = plt.subplots(figsize=(11, 5), constrained_layout=True)
    ax.scatter(train_degrees, labels, s=95, marker='x', color='#17212B', lw=2, label='Training targets', zorder=9)
    for (key, color, _, name), marker in zip(CURVES, ('o', 's', '^', 'D', 'P')):
        ax.scatter(train_degrees, arrays[key][indices], s=34, marker=marker,
                   facecolors='none', edgecolors=color, lw=1.4, label=name, zorder=10)
    ax.set(xlim=(-2, 92), xlabel='Training angle θ (degrees)', ylabel='Prediction',
           title='All sixteen training inputs: comparable endpoint loss')
    ax.grid(alpha=.7)
    ax.legend(ncol=3, frameon=False, loc='upper center', bbox_to_anchor=(.5, -.17), fontsize=9)
    save(fig, 'training_predictions')

    network_loss = np.mean([arrays[f'network_loss_{s}'] for s in SEEDS], axis=0)
    ntk_loss_curve = np.mean([arrays[f'NTK_loss_seed_{s}'] for s in SEEDS], axis=0)
    def draw_loss(ax):
        ax.plot(times, network_loss, color=COLORS['reference'], lw=2.4, label='Network, width8192 mean')
        for order in (1, 3, 5):
            ax.plot(times, arrays[f'N{order}_loss'], color=COLORS[order], ls=STYLE[order], lw=1.9, label=f'Closure N={order}')
        ax.plot(times, ntk_loss_curve, color=NTK_COLOR, ls=(0, (6, 2)), lw=2.1, label='Frozen initial NTK, same time')
        ax.set(xlim=(0, 100), yscale='log', ylabel='Training MSE')
        ax.grid(alpha=.7)

    jobs = {}
    for name in [f'net_n8192_s{s}' for s in SEEDS] + [f'cl_N{n}_base' for n in (1, 3, 5)]:
        with np.load(run / name / 'trajectories.npz') as z:
            jobs[name] = z['grams']
    reference_grams = np.mean([jobs[f'net_n8192_s{s}'] for s in SEEDS], axis=0, dtype=np.float64)
    fig = plt.figure(figsize=(12.8, 11.3), constrained_layout=True)
    grid = fig.add_gridspec(3, 2)
    ax = fig.add_subplot(grid[0, :])
    draw_loss(ax)
    ax.set_title('Training loss on the common physical time interval [0,100]')
    ax.legend(ncol=3, frameon=False, fontsize=9)
    for row, sl, name in ((1, slice(0, 16), 'Training inputs'), (2, slice(16, None), 'Passive circle')):
        ref = reference_grams[:, :, sl, sl]
        frozen = relative_gram(np.broadcast_to(ref[:1], ref.shape), ref)
        for layer in range(2):
            ax = fig.add_subplot(grid[row, layer])
            ax.plot(times, frozen[:, layer], color='#808A93', ls=(0, (3, 2)), lw=2, label='Frozen initial hidden Gram')
            for order in (1, 3, 5):
                error = relative_gram(jobs[f'cl_N{order}_base'][:, :, sl, sl], ref)
                ax.plot(times, error[:, layer], color=COLORS[order], ls=STYLE[order], lw=1.8, label=f'Closure N={order}')
            ax.set(xlim=(0, 100), ylim=(0, None), xlabel='Physical time', ylabel='Relative Gram error',
                   title=f'{name} · hidden layer {layer + 1}')
            ax.grid(alpha=.7)
            if row == 1 and layer == 0:
                ax.legend(frameon=False, fontsize=8.5)
    fig.suptitle('NTK output dynamics and separate frozen-hidden Gram controls', fontsize=15)
    save(fig, 'loss_and_gram_errors')
    del jobs, reference_grams

    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.9), constrained_layout=True)
    draw_loss(axes[0])
    axes[0].set(xlabel='Physical time', title='Same training time')
    axes[0].legend(fontsize=8, frameon=False)
    for j, seed in enumerate(SEEDS):
        axes[1].plot(arrays[f'NTK_long_times_seed_{seed}'][1:], arrays[f'NTK_long_loss_seed_{seed}'][1:],
                     color=NTK_COLOR, alpha=.75, lw=1.6, ls=('-', '--', ':')[j], label=f'NTK seed {seed}')
        state = summary['seeds'][str(seed)]
        axes[1].scatter(state['stopping_time'], state['NTK_training_mse'], color=NTK_COLOR, s=25)
    axes[1].scatter(100, actual_loss, color=COLORS['reference'], marker='*', s=110, zorder=8,
                    label='Network mean at T=100')
    axes[1].axhline(actual_loss, color='#8C959C', ls=':', lw=1)
    axes[1].set(xscale='log', yscale='log', xlabel='Physical time (log scale)', ylabel='Training MSE',
                title='Continue NTK until each seed matches network loss')
    axes[1].grid(alpha=.7)
    axes[1].legend(fontsize=8, frameon=False)
    save(fig, 'ntk_loss_to_match')

    names = ['radial_overlay', 'output_vs_angle', 'loss_and_gram_errors', 'ntk_loss_to_match',
             'gram_heatmaps_layer1', 'gram_heatmaps_layer2', 'radial_individual', 'training_dataset',
             'training_predictions', 'activation_rms_and_movement', 'width_and_seed_uncertainty',
             'quadrature_controls', 'step_and_precision_controls']
    pdfs = []
    retained = {}
    for name in names:
        path = directory / f'{name}.pdf'
        if not path.exists():
            path = run / 'figures' / f'{name}.pdf'
            retained[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
        pdfs.append(path)
    unite = shutil.which('pdfunite')
    if unite is None:
        raise RuntimeError('pdfunite required for the requested combined plot packet')
    subprocess.run([unite, *map(str, pdfs), str(directory / 'all_plots_with_ntk.pdf')], check=True)
    summary['retained_original_pdf_hashes'] = retained
    summary['combined_pdf_page_count'] = len(pdfs)
    summary['new_figures'] = [p.name for p in directory.glob('*.pdf')]
