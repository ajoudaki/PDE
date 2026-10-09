#!/usr/bin/env python3
"""Plot test RMS to the dense run over training time, sphere-3, width 4096.

Usage:
    python paper/figures/plot_sphere3_time.py \
        --data data/generated/cubic_log_comparison_20261008 --out paper/figures
"""
import argparse
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402

INK, MUTED = '#1f1f1e', '#6b6b68'
TRAIN = 8  # first columns are training inputs; the remaining 30 are test inputs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()

    def load(run, key):
        with np.load(args.data / run / 'trajectories.npz') as z:
            times = z['times_' + key] if 'times_' + key in z.files else None
            return z[key][:, TRAIN:].astype(float), times

    def rms(a, b):
        return np.sqrt(((a - b) ** 2).mean(axis=1))

    ref, t = load('paired_run/sphere3_seed601', 'dense')  # coupled reference, seed 601
    ref602, _ = load('sphere3_reference_seeds', 'dense_reference602')
    ref603, _ = load('sphere3_reference_seeds', 'dense_reference603')
    pairs = [rms(load('paired_run/sphere3_seed601', 'iid')[0], ref), rms(ref602, ref603)]
    smalls = [rms(load('sphere3_dense_n509', f'dense_n509_seed{s}')[0], r)
              for s, r in ((10601, ref), (10602, ref602), (10603, ref603))]
    geomean = lambda curves: np.exp(np.mean(np.log(np.maximum(curves, 1e-300)), axis=0))
    small = geomean(smalls)  # smooth; a pointwise median would jump between seeds
    methods = [('Legendre', '#2a78d6', 'sphere3_other_points', 'legendre'),
               ('Logarithmic', '#eb6834', 'sphere3_new_4_trials64', 'budget_4'),
               ('Harmonic', '#1baf7a', 'sphere3_other_points', 'harmonic')]
    keep = t > 0  # every model equals the dense run at t = 0 (zero readout)
    t = t[keep]

    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 8, 'pdf.fonttype': 42,
                         'axes.edgecolor': MUTED, 'axes.linewidth': .6,
                         'xtick.color': MUTED, 'ytick.color': MUTED,
                         'xtick.labelcolor': INK, 'ytick.labelcolor': INK,
                         'xtick.major.width': .6, 'ytick.major.width': .6,
                         'xtick.minor.visible': False, 'ytick.minor.visible': False})
    fig, ax = plt.subplots(figsize=(4.6, 3.0))
    ax.set(yscale='log', xlim=(0, 40))
    ax.spines[['top', 'right']].set_visible(False)
    ax.set_xticks([0, 8, 16, 24, 32])
    ax.spines['bottom'].set_bounds(0, 32)

    def label(y, text, colour=INK):
        ax.text(32.8, y, text, color=colour, va='center')

    # Smaller dense: geometric mean over 3 seeds. Dense vs. dense: geometric mean of 2 pairs.
    ax.plot(t, small[keep], color='#55554f', linewidth=1.2, zorder=2)
    pair = geomean(pairs)[keep]
    ax.plot(t, pair, color=MUTED, linewidth=1, linestyle=(0, (1, 2)), zorder=2)
    i = np.searchsorted(t, 12)
    ax.text(t[i], pair[i] * 1.1, 'dense vs. dense', color=MUTED, ha='left', va='bottom')
    label(small[-1] * 1.25, 'smaller dense')
    floor = np.inf
    for name, colour, run, key in methods:
        curve = rms(load(run, key)[0], ref)[keep]
        ax.plot(t, curve, color=colour, linewidth=1.6, zorder=4)
        label(curve[-1], name)
        floor = min(floor, curve.min())

    ax.set_ylim(floor / 2, small.max() * 2)
    ax.set_xlabel('Training time $t$', color=INK)
    ax.set_ylabel('Test RMS to dense', color=INK)
    fig.tight_layout(pad=.3)
    args.out.mkdir(parents=True, exist_ok=True)
    stem = args.out / 'sphere3_time'
    fig.savefig(stem.with_suffix('.pdf'))
    fig.savefig(stem.with_suffix('.png'), dpi=300)
    print(stem.with_suffix('.pdf'))


if __name__ == '__main__':
    main()
