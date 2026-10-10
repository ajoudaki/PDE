#!/usr/bin/env python3
"""Plot the sphere-3 accuracy/state trade-off from the saved point checks.

Usage:
    python paper/figures/plot_sphere3_tradeoff.py \
        --data data/generated/cubic_log_comparison_20261008/sphere3_reference_seeds \
        --out paper/figures
"""
import argparse
import json
import re
from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402

INK, MUTED = '#1f1f1e', '#6b6b68'
METHODS = [  # key prefix, label, colour, marker
    ('legendre', 'Legendre', '#2a78d6', 'o'),
    ('logarithmic', 'Taylor', '#eb6834', 's'),
    ('harmonic', 'Harmonic', '#1baf7a', 'D'),
]
FILES = {'max_time_rms': 'max_time_point_check_median_thinned_clean_paired.json',
         'endpoint_rms': 'point_check_median_thinned_clean_paired.json'}
YLABEL = {'max_time_rms': 'Test RMS to dense (worst time)',
          'endpoint_rms': 'Test RMS to dense (end of training)'}


def series(points, prefix, metric):
    keys = [k for k in points if re.fullmatch(prefix + r'(_n?\d+)?', k)]
    xy = sorted((points[k]['moving'], points[k][metric]) for k in keys)
    return [x for x, _ in xy], [y for _, y in xy]


def plot(data, metric, out):
    check = json.loads((data / FILES[metric]).read_text())
    points, dense = check['displayed_points'], check['displayed_dense_seed_summaries']
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 8, 'pdf.fonttype': 42,
                         'axes.edgecolor': MUTED, 'axes.linewidth': .6,
                         'xtick.color': MUTED, 'ytick.color': MUTED,
                         'xtick.labelcolor': INK, 'ytick.labelcolor': INK,
                         'xtick.major.width': .6, 'ytick.major.width': .6,
                         'xtick.minor.visible': False, 'ytick.minor.visible': False})
    fig, ax = plt.subplots(figsize=(4.6, 3.0))
    ax.set(xscale='log', yscale='log', xlim=(1.5e4, 9e7))
    ax.spines[['top', 'right']].set_visible(False)

    # Benchmark: two independently initialized width-4096 dense runs.
    pair = check['dense_pair_rms']
    ax.axhline(pair, color=MUTED, linewidth=.8, linestyle=(0, (1, 2)), zorder=1)
    ax.text(2.2e7, pair, 'dense\nvs. dense', color=MUTED, ha='left', va='center',
            linespacing=1.1, bbox=dict(facecolor='white', edgecolor='none', pad=1))

    # Smaller dense networks trained directly: median and min-max over three seeds.
    rows = sorted(dense.values(), key=lambda v: v['width'])
    x = [v['width'] ** 2 + 4 * v['width'] for v in rows]  # trained parameters, d = 3
    ax.fill_between(x, [v['minimum'] for v in rows], [v['maximum'] for v in rows],
                    color='#e3e3df', linewidth=0, zorder=2)
    ax.plot(x, [v['median'] for v in rows], color='#55554f', linewidth=1.3, zorder=3)
    ax.text(x[2], rows[2]['maximum'] * 1.2, 'smaller dense', color=INK, ha='center', va='bottom')

    for prefix, label, colour, marker in METHODS:
        mx, my = series(points, prefix, metric)
        ax.plot(mx, my, color=colour, marker=marker, markersize=3.8, linewidth=1.5,
                markeredgewidth=0, zorder=5)
        ax.text(mx[-1] * 1.3, my[-1], label, color=INK, va='center')

    ax.set_xlabel('Trained parameters', color=INK)
    ax.set_ylabel(YLABEL[metric], color=INK)
    lows = [min(series(points, p, metric)[1]) for p, *_ in METHODS]
    ax.set_ylim(min(lows) / 2, max(v['maximum'] for v in rows) * 2.5)
    fig.tight_layout(pad=.3)
    stem = out / f'sphere3_tradeoff_{metric.replace("_rms", "")}'
    fig.savefig(stem.with_suffix('.pdf'))
    fig.savefig(stem.with_suffix('.png'), dpi=300)
    plt.close(fig)
    print(stem.with_suffix('.pdf'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    for metric in FILES:
        plot(args.data, metric, args.out)
