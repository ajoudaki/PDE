"""Replot recorded validation outputs after matching training MSE only."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import time

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from VALIDATION_ANALYSIS import error_metrics

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'data/generated/first_order_dimension_mnist'
SEEDS = (1729, 2718, 3141)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_run(model, seed):
    path = BASE / f'main4096/{model}_{seed}'
    with np.load(path / 'observations.npz', allow_pickle=False) as data:
        run = {k: data[k].copy() for k in (
            'times', 'train_predictions', 'train_y', 'val_predictions', 'val_y')}
    run['summary'] = json.loads((path / 'summary.json').read_text())
    assert run['summary']['configuration']['width'] == 4096
    assert run['times'][-1] == 600
    assert np.all(np.diff(run['times']) > 0)
    run['mse'] = np.mean((run['train_predictions'].astype(np.float64)
                          - run['train_y'].astype(np.float64))**2, axis=1)
    assert np.all(np.isfinite(run['mse']))
    return run


def metrics(pred, reference, labels):
    return {
        **error_metrics(pred, reference),
        'within_class': {
            str(digit): error_metrics(pred[labels == label], reference[labels == label])
            for digit, label in ((3, 1), (5, -1))},
    }


def nearest(run, target):
    assert run['mse'].min() <= target <= run['mse'].max()
    return int(np.argmin(np.abs(run['mse'] - target)))


def analyze(output):
    started = time.perf_counter()
    dest = BASE / output
    dest.mkdir(parents=True, exist_ok=False)
    runs = {m: [read_run(m, s) for s in SEEDS] for m in ('network', 'closure')}
    dataset_path = BASE / 'data_3_5/dataset.npz'
    with np.load(dataset_path, allow_pickle=False) as data:
        labels = data['val_y'].copy()
        train_y = data['train_y'].copy()
        ids = data['val_ids'].copy()
    dataset_sha = digest(dataset_path)
    assert len(ids) == 1000 and len(np.unique(ids)) == 1000
    for group in runs.values():
        for run in group:
            assert np.array_equal(run['val_y'], labels)
            assert np.array_equal(run['train_y'], train_y)
            assert run['summary']['data']['metadata']['dataset_sha256'] == dataset_sha

    network = np.array([r['val_predictions'][-1] for r in runs['network']], dtype=np.float64)
    reference = network.mean(axis=0)
    net_losses = [float(r['mse'][-1]) for r in runs['network']]
    target = float(np.mean(net_losses))
    indices = [nearest(r, target) for r in runs['closure']]
    matched = np.array([r['val_predictions'][i] for r, i in zip(runs['closure'], indices)], dtype=np.float64)
    same_time = np.array([r['val_predictions'][-1] for r in runs['closure']], dtype=np.float64)
    rows = []
    pairs = []
    for j, (seed, run, index) in enumerate(zip(SEEDS, runs['closure'], indices)):
        old = metrics(same_time[j], reference, labels)
        new = metrics(matched[j], reference, labels)
        above = int(np.flatnonzero(run['mse'] >= target)[-1])
        below = int(np.flatnonzero(run['mse'] <= target)[0])
        assert below - above in (0, 1), 'Nonmonotone crossing needs explicit handling'
        bracket = [{'time': float(run['times'][k]), 'training_mse': float(run['mse'][k]),
                    'validation_metrics': metrics(run['val_predictions'][k], reference, labels)}
                   for k in sorted({above, below})]
        rows.append({
            'seed': seed, 'selected_index': index,
            'selected_time': float(run['times'][index]),
            'matched_training_mse': float(run['mse'][index]),
            'relative_loss_mismatch': float(run['mse'][index] / target - 1),
            'final_training_mse': float(run['mse'][-1]),
            'same_time': old, 'matched_loss': new,
            'rms_reduction_fraction': 1 - new['rms'] / old['rms'],
            'bracket_sensitivity': bracket,
        })
        for k, net_seed in enumerate(SEEDS):
            pair_index = nearest(run, net_losses[k])
            pairs.append({
                'closure_seed': seed, 'network_seed': net_seed,
                'network_final_training_mse': net_losses[k],
                'common_target_matched': metrics(matched[j], network[k], labels),
                'same_time': metrics(same_time[j], network[k], labels),
                'individual_target_time': float(run['times'][pair_index]),
                'individual_target_training_mse': float(run['mse'][pair_index]),
                'individual_target_matched': metrics(run['val_predictions'][pair_index], network[k], labels),
            })
    old_mean = float(np.mean([r['same_time']['rms'] for r in rows]))
    new_mean = float(np.mean([r['matched_loss']['rms'] for r in rows]))
    report = {
        'method': 'Nearest saved training MSE; no interpolation, calibration or validation-based time selection',
        'reference': 'Mean final T600 validation output of three actual networks',
        'target_definition': 'Arithmetic mean of individual networks final training MSE; not ensemble-predictor MSE',
        'width': 4096, 'closure_order': 1, 'network_time': 600,
        'seeds': SEEDS, 'validation_count': len(ids), 'training_count': len(train_y),
        'network_final_training_mse': net_losses, 'target_training_mse': target,
        'rows': rows, 'all_individual_pairs': pairs,
        'mean_individual_rms_same_time': old_mean,
        'mean_individual_rms_matched_loss': new_mean,
        'mean_rms_reduction_fraction': 1 - new_mean / old_mean,
        'network_pairwise_rms': [error_metrics(network[i], network[j])['rms']
                                 for i, j in itertools.combinations(range(3), 2)],
        'matched_ensemble_metrics': metrics(matched.mean(axis=0), reference, labels),
        'same_time_ensemble_metrics': metrics(same_time.mean(axis=0), reference, labels),
        'provenance': {
            'dataset_sha256': dataset_sha,
            'sources': {p.name: digest(p) for p in (Path(__file__), HERE / 'VALIDATION_ANALYSIS.py', HERE / 'MATCHED_LOSS_PLAN.md')},
            'input_sha256': {f'{m}_{s}/{name}': digest(BASE / f'main4096/{m}_{s}/{name}')
                             for m in runs for s in SEEDS for name in ('observations.npz', 'summary.json')},
        },
        'limits': 'Postprocessing existing audited trajectories; no new training reproduction. Matching one scalar loss does not establish equality of learned functions.',
    }

    np.savez_compressed(dest / 'sample_predictions.npz', labels=labels, official_train_ids=ids,
                        network_final=network, network_mean=reference,
                        closure_final=same_time, closure_matched=matched,
                        matched_times=np.array([r['selected_time'] for r in rows]))
    columns = np.column_stack([ids, labels, network.T, reference, same_time.T, matched.T])
    header = ['official_train_id', 'label'] + [f'network_{s}_T600' for s in SEEDS] + ['network_mean_T600']
    header += [f'closure_{s}_T600' for s in SEEDS]
    header += [f'closure_{r["seed"]}_T{r["selected_time"]:g}' for r in rows]
    np.savetxt(dest / 'validation_samples.csv', columns, delimiter=',', header=','.join(header), comments='')

    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
    colors = np.where(labels > 0, '#ce654a', '#3377a1')
    limit = 1.08 * max(np.max(abs(reference)), np.max(abs(matched)), np.max(abs(same_time)))
    fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharex=True, sharey=True, layout='constrained')
    times_text = ', '.join(f'{r["selected_time"]:g}' for r in rows)
    for ax, values, title, rms in zip(axes, (same_time, matched),
            ('Equal time: both at T = 600', f'Matched training loss: closure T = {times_text}'),
            (old_mean, new_mean)):
        for pred in values:
            ax.scatter(reference, pred, s=10, c=colors, alpha=.25, linewidths=0, rasterized=True)
        ax.plot([-limit, limit], [-limit, limit], '--', c='#333333', lw=1)
        ax.set(xlim=(-limit, limit), ylim=(-limit, limit), aspect='equal',
               xlabel='Actual network mean output at T = 600',
               title=f'{title}\nMean individual validation RMS = {rms:.5f}')
        ax.grid(alpha=.12)
    axes[0].set_ylabel('p = 1 closure output')
    axes[1].legend(handles=[Line2D([], [], marker='o', ls='', color=c, label=f'Digit {d}')
                           for c, d in (('#ce654a', 3), ('#3377a1', 5))], loc='lower right')
    fig.suptitle(f'MNIST 3 versus 5 · n = P = 4,096 · 1,000 validation images\n'
                 f'All three closure seeds · target training MSE = {target:.6f}', fontsize=14)
    fig.savefig(dest / 'matched_loss_scatter.png', dpi=180)
    fig.savefig(dest / 'matched_loss_scatter.pdf')
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), sharex=True, sharey=True, layout='constrained')
    err_limit = 1.06 * max(np.max(abs(same_time - reference)), np.max(abs(matched - reference)))
    for ax, values, title in zip(axes, (same_time, matched), ('Equal time', 'Matched training loss')):
        for pred in values:
            ax.scatter(reference, pred - reference, s=10, c=colors, alpha=.25, linewidths=0)
        ax.axhline(0, c='#333333', lw=1)
        ax.set(title=title, xlabel='Actual network mean output at T = 600', ylim=(-err_limit, err_limit))
        ax.grid(alpha=.12)
    axes[0].set_ylabel('Closure minus network')
    fig.suptitle('Validation prediction differences · identical axes · no calibration')
    fig.savefig(dest / 'matched_loss_residuals.png', dpi=180)
    plt.close(fig)
    report['analysis_wall_seconds'] = time.perf_counter() - started
    (dest / 'summary.json').write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')
    print(json.dumps({'target': target, 'times': [r['selected_time'] for r in rows],
                      'matched_losses': [r['matched_training_mse'] for r in rows],
                      'same_time_mean_rms': old_mean, 'matched_mean_rms': new_mean,
                      'reduction_fraction': report['mean_rms_reduction_fraction']}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='matched_loss4096_001')
    analyze(parser.parse_args().output)
