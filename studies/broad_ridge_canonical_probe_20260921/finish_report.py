"""Add prescribed terminal-time reporting and independent replay provenance."""
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STUDY = Path(__file__).resolve().parent
BASE = ROOT/'data/generated/broad_ridge_canonical_probe_20260921'
os.environ.setdefault('MPLCONFIGDIR', str(BASE/'mpl'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    data = np.load(BASE/'data01/data.npz')
    analysis = json.loads((BASE/'analysis01/analysis.json').read_text())
    replay_path = BASE/'check_replay01/checks.json'
    replay = json.loads(replay_path.read_text())
    rows = []
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.3), constrained_layout=True)
    names = ('closure1024', 'width244', 'width492', 'width1024')
    labels = ('Closure · 1024', 'Dense · 244', 'Dense · 492', 'Full dense · 1024')
    for name, label, color in zip(names, labels, ('#009988','#ee7733','#4477aa','#777777')):
        directory = BASE/'run01'/f'{name}_fine'
        result = json.loads((directory/'result.json').read_text())
        final = np.load(directory/'final.npz')
        checkpoints = np.load(directory/'checkpoints.npz')
        terminal = float(final['time'])
        n = 1024 if name == 'closure1024' else int(name[5:])
        W = final['state'][:n*64].reshape(n,64)
        initial = np.load(directory/'source.npz')['W0']
        row = {'model': name, 'time': terminal, 'status': result['status'],
               'median_W_norm_ratio': float(np.median(np.linalg.norm(W,axis=1)) /
                                           np.median(np.linalg.norm(initial,axis=1)))}
        for split in ('train', 'passive'):
            target = data['y_'+split]
            row[split+'_nrmse'] = float(np.linalg.norm(final[split+'_prediction']-target)/np.linalg.norm(target))
        rows.append(row)
        accepted = np.atleast_2d(np.loadtxt(directory/'accepted.csv', delimiter=',', skiprows=1))
        train_scale = float(np.mean(data['y_train']**2))
        axes[0].plot(accepted[:,0], np.sqrt(np.maximum(0,accepted[:,1])/train_scale),
                     label=label, color=color)
        axes[0].scatter([terminal], [row['train_nrmse']], color=color, s=25)
        passive_rmse = np.sqrt(np.mean((checkpoints['passive_prediction']-data['y_passive'])**2, axis=1) /
                               np.mean(data['y_passive']**2))
        times = list(checkpoints['times'])
        values = list(passive_rmse)
        if not times or times[-1] != terminal:
            times.append(terminal); values.append(row['passive_nrmse'])
        axes[1].plot(times, values, '.-', label=label, color=color)
        axes[1].scatter([terminal], [row['passive_nrmse']], color=color, s=25)
    for ax, title in zip(axes, ('Training examples', 'Unseen examples')):
        ax.axhline(1, color='black', linewidth=.8, linestyle=':')
        if analysis['common_time'] is not None:
            ax.axvline(analysis['common_time'], color='black', linewidth=.8, alpha=.4)
        ax.set(xscale='symlog', yscale='log', xlabel='Physical gradient-flow time',
               ylabel='RMS error / target RMS', title=title)
        ax.grid(True, alpha=.2)
    axes[0].legend(fontsize=8)
    fig.suptitle('Broad smooth ridges · tighter-tolerance runs · dots mark compute cutoffs')
    fig.savefig(BASE/'analysis01/loss_with_endpoints.png', dpi=170)
    fig.savefig(BASE/'analysis01/loss_with_endpoints.pdf')
    plt.close(fig)
    evidence = {'final_fine_runs': rows, 'common_comparison_time': analysis['common_time'],
                'replay_run_count': len(replay['runs']),
                'replay_sha256': hashlib.sha256(replay_path.read_bytes()).hexdigest(),
                'max_replay_prediction_difference': max(r['saved_prediction_max_abs'] for r in replay['runs']),
                'max_replay_final_rhs_difference': max(r['final_rhs_max_abs'] for r in replay['runs'])}
    # Descriptive supplement: the reference is slower than the three matched
    # predictors. Keep the original all-four primary decision unchanged.
    matched_times = None
    for name in names[:3]:
        for level in ('primary', 'fine'):
            archive = np.load(BASE/'run01'/f'{name}_{level}'/'checkpoints.npz')
            times = set(archive['times'])
            matched_times = times if matched_times is None else matched_times.intersection(times)
    matched_t = float(max(matched_times))
    matched_rows = []
    for name in names[:3]:
        archive = np.load(BASE/'run01'/f'{name}_fine'/'checkpoints.npz')
        i = list(archive['times']).index(matched_t)
        row = {'model': name, 'time': matched_t}
        for split in ('train', 'passive'):
            target = data['y_'+split]
            row[split+'_nrmse'] = float(np.linalg.norm(archive[split+'_prediction'][i]-target)/np.linalg.norm(target))
        matched_rows.append(row)
    evidence['descriptive_matched_models_common_time'] = matched_t
    evidence['descriptive_matched_models'] = matched_rows
    out = BASE/'analysis01/terminal_summary.json'
    if out.exists():
        raise FileExistsError(out)
    out.write_text(json.dumps(evidence, indent=2)+'\n')
    report = STUDY/'RESULTS.md'
    extra = ['', '## Actual tighter-tolerance endpoints', '',
             '**These endpoints have different physical times and are not a matched-time ranking.**',
             'Every cutoff is recorded explicitly. Small training error demonstrates fitting of this sample, not learning of the population target.', '',
             '| Model | Last physical time | Training normalized RMS | Unseen normalized RMS | Median W norm ratio | Status |',
             '|---|---:|---:|---:|---:|---|']
    for row in rows:
        extra.append(f"| {row['model']} | {row['time']:.6g} | {row['train_nrmse']:.6g} | {row['passive_nrmse']:.6g} | {row['median_W_norm_ratio']:.4g} | {row['status']} |")
    extra += ['', '![Full saved loss curves](../../data/generated/broad_ridge_canonical_probe_20260921/analysis01/loss_with_endpoints.png)', '',
              'Training curves use every accepted-step loss. Passive curves connect saved evaluations; neither line extends beyond its observed cutoff.',
              '', f"Independent replay covered {len(replay['runs'])} runs; maximum saved-prediction error was {evidence['max_replay_prediction_difference']:.3g} and terminal-RHS error {evidence['max_replay_final_rhs_difference']:.3g}.",
              f"Replay SHA-256: `{evidence['replay_sha256']}`.", '']
    extra += ['## Descriptive supplement for the matched predictors', '',
              f'The three matched predictors have resolved checkpoints through time {matched_t:g}.',
              'The full-width reference stopped before that checkpoint at the fine tolerance, so this supplement does not replace the precommitted all-four comparison.', '',
              '| Model | Training normalized RMS | Unseen normalized RMS |',
              '|---|---:|---:|']
    for row in matched_rows:
        extra.append(f"| {row['model']} | {row['train_nrmse']:.6g} | {row['passive_nrmse']:.6g} |")
    extra.append('')
    report.write_text(report.read_text()+'\n'.join(extra))
    print(json.dumps(evidence,indent=2))


if __name__ == '__main__':
    main()
