"""Scientific figures from the completed hidden-activation Gram replay."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['MPLCONFIGDIR'] = '/tmp/pde-gram-matplotlib'
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

STUDY = Path(__file__).resolve().parent
GENERATED = STUDY.parents[1] / 'data/generated/wide_network_closure_comparison'
COLORS = {1: '#d58c00', 3: '#009e73', 5: '#cc5078'}


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    base = args.output.resolve()
    if base.parent != GENERATED.resolve() or not base.name.startswith('GRAM_'):
        raise ValueError('Figures belong in this study\'s fresh GRAM_* run only')
    comparison = json.loads((base / 'gram_comparison.json').read_text())
    if comparison['status'] != 'complete' or not comparison['validation_pass']:
        raise ValueError('Complete validated Gram arrays are required')
    destination = base / 'figures'
    destination.mkdir(exist_ok=True)
    with np.load(base / 'inputs.npz') as archive:
        inputs = {k: archive[k].copy() for k in archive.files}
    times = inputs['times']
    plt.rcParams.update({'font.size': 10, 'axes.spines.top': False,
                         'axes.spines.right': False, 'savefig.facecolor': 'white',
                         'axes.titleweight': 'medium'})
    products = []

    def save(fig, name):
        for extension in ('png', 'pdf'):
            path = destination / (name + '.' + extension)
            fig.savefig(path, dpi=180, bbox_inches='tight')
            products.append(dict(path=str(path.relative_to(base)), sha256=digest(path)))
        plt.close(fig)

    columns = [(1, 'data'), (2, 'data'), (1, 'circle'), (2, 'circle')]
    for observable in ('G', 'DeltaG'):
        fig, axes = plt.subplots(2, 4, figsize=(15, 7), constrained_layout=True)
        for row, case in enumerate(('axis', 'arcs')):
            for col, (layer, panel) in enumerate(columns):
                ax = axes[row, col]
                selected = [r for r in comparison['seed_mean_comparisons']
                            if r['case'] == case and r['width'] == 8192 and
                            r['layer'] == layer and r['panel'] == panel and
                            r['observable'] == observable and r['closure_kind'] == 'primary']
                for r in sorted(selected, key=lambda r: r['order']):
                    ax.plot(times, r['rms_curve'], color=COLORS[r['order']],
                            label=f"N = {r['order']}", linewidth=1.9)
                if observable == 'DeltaG':
                    baseline = next(r for r in comparison['frozen_initial_baselines']
                                    if r['case'] == case and r.get('width') == 8192 and
                                    r['family'] == 'network_seed_mean' and r['layer'] == layer and r['panel'] == panel)
                    ax.plot(times, baseline['rms_curve'], color='#6e7580', linestyle='--',
                            linewidth=1.2, label='Frozen initial Gram')
                ax.set_xscale('symlog', linthresh=.5, linscale=.7)
                ax.set_xticks([0, .5, 1, 5, 10, 40], ['0', '.5', '1', '5', '10', '40'])
                ax.set_ylim(bottom=0)
                ax.grid(alpha=.2)
                if row == 0:
                    ax.set_title(f"Layer {layer} · {'training inputs' if panel == 'data' else '128 circle inputs'}")
                if col == 0:
                    ax.set_ylabel(f"{'2 axis inputs' if case == 'axis' else '16 arc inputs'}\nMatrix RMS discrepancy")
                if row == 1:
                    ax.set_xlabel('Training time t (early times expanded)')
        handles, labels = axes[0, 0].get_legend_handles_labels()
        fig.legend(handles, labels, loc='outside lower center', ncol=len(labels), frameon=False)
        quantity = 'Full hidden Gram G(t)' if observable == 'G' else 'Change in hidden Gram G(t) − G(0)'
        fig.suptitle(quantity + '\nClosure discrepancy from the width-8192, three-seed mean', fontsize=15)
        save(fig, 'gram_errors' if observable == 'G' else 'gram_increment_errors')

    # Complete matrix heatmaps at the four declared inspection times, for each layer.
    gram_hashes = {}
    for case in ('axis', 'arcs'):
        network = []
        for seed in (11, 29, 47):
            path = base / 'network' / f'{case}_n8192_s{seed}' / 'gram.npy'
            network.append(np.load(path, mmap_mode='r'))
            gram_hashes[str(path.relative_to(base))] = digest(path)
        closure_path = base / 'closure' / f'{case}_N5' / 'gram.npy'
        closure = np.load(closure_path, mmap_mode='r')
        gram_hashes[str(closure_path.relative_to(base))] = digest(closure_path)
        m = len(inputs[case + '_labels'])
        indices = [int(np.flatnonzero(times == t)[0]) for t in (0, 1, 5, 40)]
        for layer in (1, 2):
            finite = np.stack([sum(np.asarray(g[i, layer-1, m:, m:]) / 3 for g in network) for i in indices])
            predicted = np.stack([closure[i, layer-1, m:, m:] for i in indices])
            error = predicted - finite
            limit = max(float(np.max(np.abs(finite))), float(np.max(np.abs(predicted))))
            error_limit = max(float(np.max(np.abs(error))), 1e-12)
            fig, axes = plt.subplots(3, 4, figsize=(12, 8.8), constrained_layout=True)
            for row, matrices in enumerate((finite, predicted, error)):
                vmax = error_limit if row == 2 else limit
                for col, instant in enumerate((0, 1, 5, 40)):
                    ax = axes[row, col]
                    im = ax.imshow(matrices[col], origin='lower', extent=(0, 360, 0, 360),
                                   vmin=-vmax, vmax=vmax, cmap='RdBu_r', interpolation='nearest')
                    ax.set_xticks([0, 180, 360])
                    ax.set_yticks([0, 180, 360])
                    if row == 0:
                        ax.set_title(f't = {instant}')
                    if col == 0:
                        ax.set_ylabel(('Network: 3-seed mean', 'Closure: N = 5', 'Closure − network')[row] + '\nInput angle (degrees)')
                    if row == 2:
                        ax.set_xlabel('Input angle (degrees)')
                fig.colorbar(im, ax=axes[row, :], fraction=.018, pad=.015)
            fig.suptitle(f"Layer {layer} hidden Gram · {'16 arc' if case == 'arcs' else '2 axis'} training inputs\n128 × 128 circle panel; network width 8192", fontsize=15)
            save(fig, f'{case}_layer{layer}_gram_evolution')

    fig, ax = plt.subplots(figsize=(5.5, 5.5), constrained_layout=True)
    theta = np.linspace(0, 2*np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), color='#b9bec8', linewidth=1)
    xy, labels = inputs['arcs_inputs'], inputs['arcs_labels']
    for value, color in ((1, '#214b80'), (-1, '#c4484b')):
        points = xy[labels == value]
        ax.scatter(points[:, 0], points[:, 1], c=color, edgecolors='white', s=55,
                   label=f'{len(points)} inputs, target {value:+d}', zorder=3)
    ax.plot([-1, 1], [-1, 1], '--', color='#6e7580', linewidth=1, label='Separator: u₁ = u₂')
    ax.set(xlim=(-1.15, 1.15), ylim=(-1.15, 1.15), xlabel='Normalized input u₁', ylabel='Normalized input u₂',
           title='The 16-input training task\nTwo simple, linearly separable clusters', aspect='equal')
    ax.legend(loc='lower right', fontsize=9, frameon=False)
    ax.grid(alpha=.15)
    save(fig, 'arcs16_training_labels')

    manifest = dict(source_sha256=digest(__file__), comparison_sha256=digest(base/'gram_comparison.json'),
                    inputs_sha256=digest(base/'inputs.npz'), raw_gram_sha256=gram_hashes,
                    command=sys.argv, numpy_version=np.__version__, matplotlib_version=matplotlib.__version__,
                    products=products)
    (destination / 'gram_figures.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'figure_count': len(products), 'directory': str(destination)}))


if __name__ == '__main__':
    main()
