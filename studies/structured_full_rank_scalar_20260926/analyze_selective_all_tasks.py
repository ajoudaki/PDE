"""Read-only synthesis of the representative J2 circle-task screen."""
from __future__ import annotations
import csv
import json
from pathlib import Path
import numpy as np
from true_aggregate_references import digest

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT/'data/generated/structured_full_rank_scalar_20260926'
NEW = ('pair_cos3', 'near_pair_sin9', 'cluster_triple_cos9', 'quartet_mixed',
       'broad_ridge6', 'alternating3')
REUSED = ('pair_orthogonal_cos1', 'cluster_triple_cos1', 'triple_wide_mixed')
NOT_SELECTED = ('pair_cos1', 'triple_cos3', 'triple_mixed', 'quartet_broad',
                'sharp_ridge8', 'alternating5', 'multiscale12', 'alternating9')


def main():
    run = DATA/'all_tasks_j2_20260927'
    rows, evidence = [], []
    for task in (*REUSED, *NEW):
        directory = (DATA/'selective_tighter_20260927/scalar' if task in REUSED
                     else run/'scalar')
        record_path = directory/f'{task}__selective_zero_out2.json'
        if not record_path.exists():
            rows.append(dict(task=task, reused=False, status='pending'))
            continue
        record = json.loads(record_path.read_text())
        row = {'task': task, 'reused': task in REUSED,
            'status': 'fitted' if record['fitted'] else record['stop_reason'],
            'core_mse': record.get('train_mse'),
            'passive_train_mse': record.get('passive_train_mse'),
            'alias_gap_max': record.get('alias_gap_max'),
            'dynamic_scalars': (record.get('state_counts') or {}).get('total_dynamic_scalars'),
            'training_seconds': record.get('training_seconds', 0.),
            'total_seconds': record.get('total_seconds'),
            'scalar_block_rms': None, 'scalar_gaussian_rms': None,
            'block_gaussian_rms': None, 'max_grid_change': None,
            'screen': 'not_fitted'}
        reference_predictions = {}
        for method, suffix in [('block', 'block_k4_P1_canonical'), ('gaussian', 'gaussian')]:
            refpath = run/'references'/f'{task}__{suffix}.npz'
            with np.load(refpath, allow_pickle=False) as ref:
                reference_predictions[method] = ref['prediction'].copy()
                reference_angles = ref['angles'].copy()
        row['block_gaussian_rms'] = float(np.sqrt(np.mean(
            (reference_predictions['block']-reference_predictions['gaussian'])**2)))
        item = {'task': task, 'record_file': str(record_path),
                'record_sha256': digest(record_path)}
        if record.get('data_file'):
            checkpoint = directory/record['data_file']
            if digest(checkpoint) != record['data_sha256']:
                raise ValueError('Scalar checkpoint hash mismatch')
            with np.load(checkpoint, allow_pickle=False) as scalar:
                angles, prediction = scalar['angles'].copy(), scalar['prediction'].copy()
            distance = np.abs(np.angle(np.exp(1j*(angles[:, None]-reference_angles[None, :]))))
            indices = np.argmin(distance, axis=1)
            if np.max(distance[np.arange(len(angles)), indices]) > 1e-13:
                raise ValueError('Circle grid mismatch')
            grid_changes = []
            for method in ('block', 'gaussian'):
                difference = prediction-reference_predictions[method][indices]
                error = float(np.sqrt(np.mean(difference**2)))
                grid_changes.append(abs(error-float(np.sqrt(np.mean(difference[::2]**2)))))
                row[f'scalar_{method}_rms'] = error
            row['max_grid_change'] = max(grid_changes)
            if record['fitted']:
                value = row['scalar_gaussian_rms']
                row['screen'] = 'coarse_accuracy' if value <= .1 else (
                    'high_error' if value > .3 else 'intermediate_error')
            item['data_sha256'] = digest(checkpoint)
        rows.append(row)
        evidence.append(item)
    output = run/'analysis'
    output.mkdir(parents=True, exist_ok=True)
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with (output/'summary.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    result = {'table': rows, 'not_selected': list(NOT_SELECTED), 'evidence': evidence,
        'analysis_source_sha256': digest(Path(__file__)),
        'metric': 'raw predicted-function difference on matched circle angles',
        'new_tasks': list(NEW), 'reused_tasks': list(REUSED)}
    (output/'summary.json').write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(rows, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
