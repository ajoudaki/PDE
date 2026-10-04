"""Plot existing single-seed evidence; no training or additional experiment."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

root = Path(__file__).resolve().parents[2]
data = root / 'data/generated/response_memory_order_selection_20261002'
target = data / 'extended_seed_101_target'
summary = json.loads((target / 'summary.json').read_text())
variance = summary['vy']
histories = {
    order: json.loads((target / f'wide_{order}_continuation_metrics.json').read_text())
    for order in ('ab', 'ba')
}
times = np.array([row['physical_time'] for row in histories['ab']])
assert np.array_equal(times, [row['physical_time'] for row in histories['ba']])
risks = {order: np.array([row['ood'] for row in rows]) / variance
         for order, rows in histories.items()}
fig, axes = plt.subplots(1, 2, figsize=(9, 3.3), constrained_layout=True)
for order, label, color in [('ab', 'Majority then minority', '#2077b4'),
                             ('ba', 'Minority then majority', '#ce6c24')]:
    axes[0].plot(times, risks[order], label=label, color=color, linewidth=1.8)
axes[0].axhline(1, color='0.55', linestyle=':', linewidth=1, label='Zero predictor')
axes[0].set(xlabel='Physical training time', ylabel='Shifted-test MSE / E[y²]',
            title='Identical mixed training follows both orders')
axes[0].legend(frameon=False, fontsize=8)
gap = risks['ba'] - risks['ab']
axes[1].plot(times, gap, color='#5b3c88', linewidth=1.8)
axes[1].axhline(0, color='0.55', linewidth=.8)
axes[1].axhline(.05, color='0.55', linestyle=':', linewidth=1, label='Effect-size threshold')
axes[1].set(xlabel='Physical training time', ylabel='Signed MSE difference / E[y²]',
            title=f'Order effect: {100*gap[0]:.1f}% → {100*gap[-1]:.2f}%')
axes[1].legend(frameon=False, fontsize=8)
for ax in axes:
    ax.spines[['top', 'right']].set_visible(False)
fig.suptitle('One exploratory seed: a large early effect does not persist', fontsize=12)
output = data / 'order_contrast_figure01'
output.mkdir(exist_ok=False)
fig.savefig(output / 'order_contrast.png', dpi=180)
fig.savefig(output / 'order_contrast.pdf')
print(output / 'order_contrast.png')
