"""Post-run figures and independent scalar reduction; no training or tuning."""
import json
import pathlib
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

path = pathlib.Path(sys.argv[1])
analysis = json.loads((path/'analysis.json').read_text())
policies = ('P2', 'P32', 'NP', 'SAFE')
colors = dict(q3='#087e8b', svd47='#9b59b6', NTK='#d95f02', average='#777777')
fig, axes = plt.subplots(2, 2, figsize=(10, 6.4), sharex=True, sharey=True)
for ax, policy in zip(axes.ravel(), policies):
    truth = np.load(path/f'dense_{policy}_fine.npz')
    t, dense = truth['time'], truth['predictions']
    for method in colors:
        filename = (f'NTK_{policy}' if method == 'NTK' else
                    'dense_SAFE_fine' if method == 'average' and policy == 'SAFE' else
                    'dense_AVG_fine' if method == 'average' else f'{method}_{policy}_fine')
        pred = np.load(path/f'{filename}.npz')['predictions']
        error = np.sqrt(np.mean((pred-dense)**2, axis=1))
        ax.semilogy(t[1:], np.maximum(error[1:], 1e-12), color=colors[method], label=method)
    ax.set_title(policy)
    ax.grid(alpha=.2)
    ax.set_ylim(1e-9, 1)
    ax.set_ylabel('Passive prediction RMS error')
    ax.set_xlabel('Training time')
axes[0, 0].legend(ncol=2, fontsize=9)
fig.suptitle('Fresh digit adaptation: memory and online truncated SVD', fontsize=12)
fig.tight_layout()
fig.savefig(path/'trajectory_errors.png', dpi=180)
plt.close(fig)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
metrics = analysis['metrics']['dense']
labels = list(policies)
cs = [metrics[p]['C'] for p in policies]
js = [metrics[p]['J'] for p in policies]
axes[0].bar(labels, cs, color=['#c55a40' if c > .25 else '#087e8b' for c in cs])
axes[0].axhline(.25, color='black', linestyle='--', label='Frozen retention threshold')
axes[0].set_ylabel('Maximum old-function RMS drift')
axes[0].legend(fontsize=8)
axes[1].bar(labels, js, color='#557d9b')
axes[1].set_ylabel('Time-average new validation RMSE')
for ax in axes:
    ax.grid(axis='y', alpha=.2)
fig.suptitle('Dense outcomes of the frozen policy menu')
fig.tight_layout()
fig.savefig(path/'menu_decision.png', dpi=180)
plt.close(fig)

# Recompute the principal reductions directly, without importing training code.
y = np.load(path/'query_labels.npy')
independent = {}
for policy in policies:
    z = np.load(path/f'dense_{policy}_fine.npz')
    t, pred = z['time'], z['predictions']
    c = float(np.linalg.norm(pred[:, :128]-pred[0, :128], axis=1).max()/np.sqrt(128))
    loss = np.linalg.norm(pred[:, 128:]-y[128:], axis=1)/np.sqrt(128)
    j = float(np.sum((loss[1:]+loss[:-1])*(t[1:]-t[:-1]))/48)
    assert abs(c-metrics[policy]['C']) < 1e-12
    assert abs(j-metrics[policy]['J']) < 1e-12
    independent[policy] = dict(C=c, J=j)
(path/'independent_reduction.json').write_text(json.dumps(independent, indent=2))
print(json.dumps(independent, indent=2))
