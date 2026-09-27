"""Summarize the fixed geometry campaign from saved predictions only."""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
from pathlib import Path
import numpy as np
from geometry_tasks import TASKS


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', required=True, type=Path)
    parser.add_argument('--plot', action='store_true', help='Requires matplotlib')
    args = parser.parse_args()
    out = args.run/'analysis'
    out.mkdir(exist_ok=True, parents=True)
    rows, plots, inputs = [], [], {}
    for task in TASKS:
        report_path = args.run/'scalar'/f'{task.name}__selective_zero.json'
        if not report_path.exists():
            rows.append({'task': task.name, 'samples': len(task.angles),
                         'status': 'no completed run record'})
            plots.append(None)
            continue
        r = json.loads(report_path.read_text())
        inputs[str(report_path)] = sha(report_path)
        row = {'task': task.name, 'samples': len(task.angles),
               'status': r.get('stop_reason'), 'core_fitted': r.get('fitted', False),
               'training_seconds': r.get('training_seconds', 0.),
               'compile_seconds': r.get('compile', {}).get('seconds'),
               'initialization_seconds': r.get('initialization', {}).get('seconds'),
               'total_seconds': r.get('total_seconds')}
        if not r.get('data_file'):
            rows.append(row)
            plots.append(None)
            continue
        path = report_path.parent/r['data_file']
        if sha(path) != r['data_sha256']:
            raise ValueError(f'Checkpoint hash mismatch: {path}')
        inputs[str(path)] = sha(path)
        with np.load(path, allow_pickle=False) as z:
            arrays = {name: z[name].copy() for name in ('angles', 'prediction',
                'train_prediction', 'passive_train_prediction', 'train_labels',
                'train_angles', 'history')}
        labels = arrays['train_labels']
        if not np.allclose(labels, task.target(task.angles), rtol=0, atol=1e-14):
            raise ValueError('Task labels differ from frozen configuration')
        core, passive = arrays['train_prediction'], arrays['passive_train_prediction']
        row.update(core_train_rmse=float(np.sqrt(np.mean((core-labels)**2))),
            passive_train_rmse=float(np.sqrt(np.mean((passive-labels)**2))),
            alias_gap_rms=float(np.sqrt(np.mean((core-passive)**2))),
            alias_gap_max=float(np.max(np.abs(core-passive))),
            physical_time=r['physical_time'],
            training_core_scalars=r['state_counts']['shared_core']+1,
            total_dynamic_scalars=r['state_counts']['total_dynamic_scalars'])
        references = {}
        for name, tag in [('gaussian', 'gaussian'), ('block', 'block_k4_P1_canonical')]:
            reference_path = args.run/'references'/f'{task.name}__{tag}.npz'
            metadata_path = reference_path.with_suffix('.json')
            meta = json.loads(metadata_path.read_text())
            if sha(reference_path) != meta['data_sha256']:
                raise ValueError(f'Reference hash mismatch: {reference_path}')
            inputs[str(reference_path)] = sha(reference_path)
            inputs[str(metadata_path)] = sha(metadata_path)
            with np.load(reference_path, allow_pickle=False) as ref:
                reference = {key: ref[key].copy() for key in ('angles', 'prediction', 'train_prediction')}
            step = len(reference['angles'])//len(arrays['angles'])
            if not np.allclose(reference['angles'][::step], arrays['angles'], rtol=0, atol=1e-14):
                raise ValueError('Circle grids differ')
            difference = arrays['prediction']-reference['prediction'][::step]
            error = float(np.sqrt(np.mean(difference**2)))
            row[f'circle_rms_vs_{name}'] = error
            row[f'circle_grid_change_vs_{name}'] = abs(error-float(np.sqrt(np.mean(difference[::2]**2))))
            row[f'{name}_fitted'] = meta['fitted']
            row[f'core_prediction_rms_vs_{name}'] = float(np.sqrt(np.mean((core-reference['train_prediction'])**2)))
            row[f'passive_prediction_rms_vs_{name}'] = float(np.sqrt(np.mean((passive-reference['train_prediction'])**2)))
            references[name] = reference
        row['block_circle_rms_vs_gaussian_256'] = float(np.sqrt(np.mean(
            (references['block']['prediction']-references['gaussian']['prediction'])**2)))
        row['fitted_comparison'] = bool(row['core_fitted'] and row['gaussian_fitted'])
        if not row['fitted_comparison']:
            row['screen'] = 'partial comparison'
        elif row['circle_rms_vs_gaussian'] <= .1:
            row['screen'] = 'coarse accuracy screen passed'
        elif row['circle_rms_vs_gaussian'] > .3:
            row['screen'] = 'large discrepancy despite fitted core'
        else:
            row['screen'] = 'intermediate discrepancy'
        row['decoder_consistency_flag'] = row['alias_gap_max'] > .05
        row['quadrature_flag'] = row['circle_grid_change_vs_gaussian'] > .001
        rows.append(row)
        plots.append((arrays, references, row))
    (out/'summary.json').write_text(json.dumps(rows, indent=2, allow_nan=False)+'\n')
    columns = list(dict.fromkeys(key for row in rows for key in row))
    with (out/'summary.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, columns)
        writer.writeheader()
        writer.writerows(rows)

    (out/'provenance.json').write_text(json.dumps({'command': __import__('sys').argv,
        'analysis_source_sha256': sha(__file__), 'inputs': inputs,
        'metrics': 'Raw prediction RMS, no signal normalization; core training fit distinguished from passive decoder'},
        indent=2)+'\n')
    if not args.plot:
        print(json.dumps(rows, indent=2))
        return

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(2, 4, figsize=(15, 7), constrained_layout=True)
    for ax, task, item in zip(axes.flat, TASKS, plots):
        if item is None:
            ax.set_title(task.name.replace('_', ' '), fontsize=10)
            ax.text(.5, .5, 'No completed trajectory', ha='center', transform=ax.transAxes)
            continue
        arrays, refs, row = item
        for key, style, color, label in [('gaussian', '-', '#222222', 'Dense Gaussian'),
                                        ('block', '--', '#9a9a9a', 'Block population')]:
            ax.plot(refs[key]['angles']/np.pi, refs[key]['prediction'], style,
                    color=color, lw=1.3, label=label)
        ax.plot(arrays['angles']/np.pi, arrays['prediction'], color='#1665ad',
                lw=1.4, label='Scalar passive outputs')
        ax.scatter(np.mod(arrays['train_angles'], 2*np.pi)/np.pi,
                   arrays['train_labels'], color='#b94a25', s=22, zorder=5,
                   label='Training labels')
        status = '' if row['core_fitted'] else ' / unfinished'
        ax.set_title(f"{task.name.replace('_', ' ')}{status}\n"
                     f"circle RMS {row['circle_rms_vs_gaussian']:.3f}", fontsize=9)
        ax.set_xlim(0, 2)
        ax.set_xticks([0, 1, 2], ['0', 'π', '2π'])
        ax.grid(alpha=.15)
    handles, labels = axes.flat[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(.5, -.035),
               ncol=4, frameon=False)
    fig.suptitle('Fixed selective scalar closure across eight input configurations\n'
                 'n=1024 references; target core training MSE 0.01; raw circle-function differences', fontsize=12)
    fig.savefig(out/'circle_functions.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(json.dumps(rows, indent=2))


if __name__ == '__main__':
    main()
