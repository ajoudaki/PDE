"""Regenerate the bounded gate's table and comparison figure from raw arrays."""
import csv
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'data/generated/response_memory_plasticity_intervention_20261002/seed0_run2'
results = json.loads((OUT / 'results.json').read_text())
rows = [r for r in results['rows'] if r['phase'] == 'probe']
with (OUT / 'comparison.csv').open('w') as stream:
    writer = csv.writer(stream)
    writer.writerow(['arm', 'speed', 'probe1_auc', 'probe2_auc', 'probe1_accuracy', 'function_jump'])
    for r in rows:
        writer.writerow([r['arm'], r['speed'], r['probe1']['auc'], r['probe2']['auc'],
                         r['probe1']['accuracy'], r['function_jump']])
candidate = next(r for r in rows if r['arm'] == 'aligned')
untouched = next(r for r in rows if r['arm'] == 'untouched' and r['speed'] == 1)
best = min((r for r in rows if r['arm'] not in ['aligned', 'orthogonal', 'balanced']),
           key=lambda r: r['probe1']['auc'])
summary = {
    'decision': 'stop_this_witness_no_consequential_gain',
    'candidate_improvement_over_untouched_percent':
        100 * (1 - candidate['probe1']['auc'] / untouched['probe1']['auc']),
    'best_rival': [best['arm'], best['speed']],
    'candidate_worse_than_best_rival_percent':
        100 * (candidate['probe1']['auc'] / best['probe1']['auc'] - 1),
    'orthogonal_factor_max_trajectory_difference': max(
        float(np.max(np.abs(np.load(OUT / f'factor_speed1_probe{k}.npy') -
                            np.load(OUT / f'factor_orthogonal_speed1_probe{k}.npy'))))
        for k in (1, 2)),
    'max_initial_function_jump': max(r['function_jump'] for r in rows),
    'elapsed_seconds': results['elapsed_seconds'],
    'metadata': results['metadata'],
}
(OUT / 'decision.json').write_text(json.dumps(summary, indent=2))

fig, ax = plt.subplots(1, 2, figsize=(10, 3.6), constrained_layout=True)
choices = [('aligned_speed1', 'Aligned histories, speed 1'),
           ('untouched_speed1', 'Unchanged histories, speed 1'),
           ('untouched_speed4', 'Unchanged histories, speed 4'),
           ('factor_aligned_speed4', 'Aligned ordinary factors, speed 4'),
           ('dense_speed4', 'Dense gradient flow, speed 4')]
for stem, label in choices:
    values = np.load(OUT / (stem + '_probe1.npy'))
    ax[0].plot(values[:, 0], values[:, 2], label=label)
    ax[1].plot(values[:, 0], values[:, 1], label=label)
ax[0].set(xlabel='Training time after concept shift', ylabel='Held-out MSE',
          title='No consequential held-out improvement')
ax[1].set(xlabel='Training time after concept shift', ylabel='Training MSE',
          title='Unchanged learner already adapts quickly', xlim=(0, 16), yscale='log')
ax[0].legend(fontsize=7)
for axis in ax:
    axis.grid(alpha=.2)
fig.savefig(OUT / 'adaptation_comparison.png', dpi=180)
fig.savefig(OUT / 'adaptation_comparison.pdf')
print(json.dumps(summary, indent=2))
