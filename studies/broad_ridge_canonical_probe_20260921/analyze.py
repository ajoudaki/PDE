"""Recompute the fixed pilot comparison from saved arrays."""
from pathlib import Path
import csv
import hashlib
import json
import os

os.environ.setdefault('MPLCONFIGDIR', str(Path(__file__).resolve().parents[2] /
    'data/generated/broad_ridge_canonical_probe_20260921/mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
STUDY = Path(__file__).resolve().parent
BASE = ROOT/'data/generated/broad_ridge_canonical_probe_20260921'
MODELS = ('closure1024', 'width244', 'width492', 'width1024')
LABELS = {'closure1024': 'Closure · 1024', 'width244': 'Dense · 244',
          'width492': 'Dense · 492', 'width1024': 'Full dense · 1024'}


def main():
    out = BASE/'analysis01'
    out.mkdir(exist_ok=False)
    manifest = json.loads((BASE/'run01/run_record.json').read_text())
    data = np.load(BASE/'data01/data.npz')
    labels = {p: data[f'y_{p}'] for p in ('train', 'passive')}
    scale = {p: float(np.sqrt(np.mean(y*y))) for p, y in labels.items()}
    runs, gates, rows, issues = {}, {}, [], []
    for filename, expected in manifest['frozen_sources'].items():
        if hashlib.sha256((ROOT/filename).read_bytes()).hexdigest() != expected:
            issues.append('Source changed: '+filename)
    for item in manifest['attempts']:
        directory = ROOT/item['directory']
        key = (item['model'], item['level'])
        if not (directory/'checkpoints.npz').exists():
            issues.append('Missing checkpoints: '+str(key))
            continue
        archive = np.load(directory/'checkpoints.npz')
        record = json.loads((directory/'result.json').read_text())
        run = dict(archive)
        run['record'] = record
        run['directory'] = directory
        run['rmse'] = {p: np.sqrt(np.mean((run[p+'_prediction']-labels[p])**2,
                                         axis=1)) for p in labels}
        runs[key] = run
    common = None
    for model in MODELS:
        if any((model, level) not in runs for level in ('primary', 'fine')):
            common = set()
            break
        a, b = (runs[(model, level)] for level in ('primary', 'fine'))
        both = sorted(set(a['times']).intersection(b['times']))
        common = set(both) if common is None else common.intersection(both)
        n = 1024 if model == 'closure1024' else int(model[5:])
        sizes = (n*64, 129*65 if model == 'closure1024' else n*n, n)
        cuts = np.cumsum((0,)+sizes)
        checkpoints = []
        for t in both:
            i, j = list(a['times']).index(t), list(b['times']).index(t)
            pred = max(float(np.max(np.abs(a[p+'_prediction'][i]-b[p+'_prediction'][j])))
                       for p in labels)
            rmse = max(abs(float(a['rmse'][p][i]-b['rmse'][p][j])) for p in labels)
            block = []
            for lo, hi in zip(cuts[:-1], cuts[1:]):
                x, y = a['states'][i, lo:hi], b['states'][j, lo:hi]
                err = float(np.sqrt(np.mean((x-y)**2)))
                bound = float(1e-3*(1+np.sqrt(np.mean(y*y))))
                block.append({'error': err, 'bound': bound, 'pass': err <= bound})
            checkpoints.append({'time': float(t), 'max_prediction_difference': pred,
                                'max_rmse_difference': rmse, 'blocks': block,
                                'pass': pred <= 1e-3 and rmse <= 1e-4 and
                                        all(v['pass'] for v in block)})
        accepted_path = b['directory']/'accepted.csv'
        with accepted_path.open() as handle:
            accepted = list(csv.DictReader(handle))
        losses = np.array([float(r['loss']) for r in accepted])
        max_increase = float(max(0., np.max(np.diff(losses)))) if len(losses)>1 else 0.
        monotone = max_increase <= 1e-6*max(1., float(losses[0]))
        gates[model] = {'checkpoints': checkpoints, 'maximum_loss_increase': max_increase,
                        'monotonicity_pass': monotone,
                        'pass': monotone and all(v['pass'] for v in checkpoints)}
    positive = sorted(t for t in (common or set()) if t > 0)
    tstar = float(positive[-1]) if positive else None
    for model in MODELS:
        if tstar is None or (model, 'fine') not in runs:
            continue
        run = runs[(model, 'fine')]
        i = list(run['times']).index(tstar)
        n = 1024 if model == 'closure1024' else int(model[5:])
        W = run['states'][i, :n*64].reshape(n, 64)
        W0 = run['states'][0, :n*64].reshape(n, 64)
        norms, initial = np.linalg.norm(W, axis=1), np.linalg.norm(W0, axis=1)
        rows.append({'model': model, 'time': tstar,
                     'train_rmse': float(run['rmse']['train'][i]),
                     'passive_rmse': float(run['rmse']['passive'][i]),
                     'train_nrmse': float(run['rmse']['train'][i]/scale['train']),
                     'passive_nrmse': float(run['rmse']['passive'][i]/scale['passive']),
                     'median_first_weight_norm': float(np.median(norms)),
                     'max_first_weight_norm': float(np.max(norms)),
                     'median_norm_ratio': float(np.median(norms)/np.median(initial)),
                     'first_weight_rms_motion': float(np.sqrt(np.mean((W-W0)**2))),
                     'numerically_resolved': gates[model]['pass']})
    signals = {}
    bymodel = {r['model']: r for r in rows}
    for name in ('width244', 'width492'):
        if 'closure1024' not in bymodel or name not in bymodel:
            continue
        c, d = bymodel['closure1024'], bymodel[name]
        train_ratio = c['train_nrmse']/d['train_nrmse']
        test_ratio = c['passive_nrmse']/d['passive_nrmse']
        signals[name] = {'training_error_ratio': train_ratio,
                         'passive_error_ratio': test_ratio,
                         'encouraging_signal': bool(c['numerically_resolved'] and
                             d['numerically_resolved'] and not issues and
                             c['train_nrmse'] <= .1 and train_ratio <= .5 and test_ratio <= .5)}
    result = {'common_time': tstar, 'horizon_censored': tstar != 5000,
              'target_panel_rms': scale, 'rows': rows, 'refinement': gates,
              'signals': signals, 'issues': issues,
              'attempts': [{k: v for k, v in a.items() if k != 'result'} |
                           {'result': a.get('result')} for a in manifest['attempts']],
              'manifest_sha256': hashlib.sha256((BASE/'run01/run_record.json').read_bytes()).hexdigest()}
    (out/'analysis.json').write_text(json.dumps(result, indent=2)+'\n')
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.3), constrained_layout=True)
    colors = ('#009988', '#ee7733', '#4477aa', '#777777')
    for ax, panel in zip(axes, ('train', 'passive')):
        for name, color in zip(MODELS, colors):
            if (name, 'fine') in runs:
                run = runs[(name, 'fine')]
                ax.plot(run['times'], run['rmse'][panel]/scale[panel], marker='.',
                        color=color, label=LABELS[name])
        ax.axhline(1, color='black', linewidth=.8, linestyle=':', label='Zero predictor')
        ax.set(xscale='symlog', yscale='log', xlabel='Physical gradient-flow time',
               ylabel='RMS error / target RMS',
               title='Training examples' if panel == 'train' else 'Unseen examples')
        ax.grid(True, alpha=.2)
        if tstar is not None:
            ax.axvline(tstar, color='black', linewidth=.8, alpha=.4)
    axes[0].legend(fontsize=8)
    fig.suptitle('768 broad tanh ridges in 64 dimensions · canonical flow · one initialization')
    fig.savefig(out/'loss.png', dpi=170)
    fig.savefig(out/'loss.pdf')
    plt.close(fig)
    lines = ['# Broad-ridge canonical-flow pilot', '',
             f'Common comparison time: **{tstar}**. Horizon censored: **{tstar != 5000}**.',
             '', 'One fixed target and one initialization; the two tolerances are numerical reproduction, not seed replication.', '',
             '| Model | Training normalized RMS | Unseen normalized RMS | Median W norm ratio | Numerical gates |',
             '|---|---:|---:|---:|---|']
    for row in rows:
        lines.append(f"| {LABELS[row['model']]} | {row['train_nrmse']:.6g} | {row['passive_nrmse']:.6g} | {row['median_norm_ratio']:.4g} | {row['numerically_resolved']} |")
    lines += ['', 'Error one is the zero predictor baseline. Passive data do not enter updates.',
              '', 'Comparison decisions: `'+json.dumps(signals)+'`.', '',
              '![Loss](../../data/generated/broad_ridge_canonical_probe_20260921/analysis01/loss.png)', '',
              'This bounded-time pilot does not prove a width lower bound or an all-time fitting failure.',
              'All individual terminal times, status flags, numerical comparisons and raw metrics are retained in analysis.json.', '',
              f"Worker process seconds: {manifest['worker_process_wall_seconds']:.3f} / 960.",
              '', f"Manifest SHA-256: `{result['manifest_sha256']}`.", '']
    (STUDY/'RESULTS.md').write_text('\n'.join(lines))
    print(json.dumps({k: result[k] for k in ('common_time', 'horizon_censored', 'rows', 'signals', 'issues')}, indent=2))


if __name__ == '__main__':
    main()
