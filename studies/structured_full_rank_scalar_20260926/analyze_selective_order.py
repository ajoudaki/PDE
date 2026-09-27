"""Compare saved scalarization orders on the three preselected tasks.

Read-only with respect to runs and controls; no compilation or ODE execution.
RMS values are recomputed from the raw 64 circle predictions.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import numpy as np


TASKS = ('pair_orthogonal_cos1', 'cluster_triple_cos1', 'triple_wide_mixed')
ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT/'data/generated/structured_full_rank_scalar_20260926'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def measure(record_path, references):
    record = json.loads(record_path.read_text())
    result = {'record': str(record_path), 'record_sha256': digest(record_path),
        'fitted': record['fitted'], 'stop_reason': record['stop_reason'],
        'train_mse': record.get('train_mse'),
        'training_seconds': record.get('training_seconds'),
        'total_seconds': record.get('total_seconds'),
        'initialization_seconds': record.get('initialization', {}).get('seconds'),
        'physical_time': record.get('physical_time'),
        'alias_gap_max': record.get('alias_gap_max'),
        'passive_train_mse': record.get('passive_train_mse'),
        'max_clipped_fraction_accepted': record.get('max_clipped_fraction_accepted'),
        'state_counts': record.get('state_counts'), 'circle_errors': {}}
    if 'data_file' not in record:
        return result
    checkpoint = record_path.parent/record['data_file']
    if digest(checkpoint) != record['data_sha256']:
        raise ValueError(f'Checkpoint hash mismatch: {checkpoint}')
    with np.load(checkpoint, allow_pickle=False) as data:
        prediction = data['prediction'].copy()
        angles = data['angles'].copy()
    for name, suffix in [('block', 'block_k4_P1_canonical'), ('gaussian', 'gaussian')]:
        refpath = references/f'{record["task"]}__{suffix}.npz'
        with np.load(refpath, allow_pickle=False) as reference:
            distance = np.abs(np.angle(np.exp(1j*(angles[:, None]-reference['angles'][None, :]))))
            indices = np.argmin(distance, axis=1)
            if np.max(distance[np.arange(len(angles)), indices]) > 1e-13:
                raise ValueError('Circle grids are not matched')
            difference = prediction-reference['prediction'][indices]
        rms = float(np.sqrt(np.mean(difference**2)))
        coarse = float(np.sqrt(np.mean(difference[::2]**2)))
        result['circle_errors'][name] = {'rms': rms,
            'grid_change_64_vs_32': abs(rms-coarse), 'reference_sha256': digest(refpath)}
        if not np.isclose(rms, record[f'{name}_comparison']['raw_circle_rms'],
                          rtol=1e-12, atol=1e-14):
            raise ValueError('Recorded error mismatch')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=Path, default=DATA/'selective_order_20260927')
    parser.add_argument('--baseline', type=Path, default=DATA/'selective_geometry_20260927')
    args = parser.parse_args()
    evidence, rows = [], []
    for task in TASKS:
        old = measure(args.baseline/'scalar'/f'{task}__selective_zero.json',
                      args.baseline/'references')
        new = measure(args.run/'scalar'/f'{task}__selective_zero_out2.json',
                      args.baseline/'references')
        evidence.append({'task': task, 'J1': old, 'J2': new})
        row = {'task': task, 'J2_fitted': new['fitted'], 'J2_stop': new['stop_reason']}
        for depth, result in [(1, old), (2, new)]:
            row[f'J{depth}_core_mse'] = result['train_mse']
            row[f'J{depth}_train_seconds'] = result['training_seconds']
            row[f'J{depth}_alias_max'] = result['alias_gap_max']
            counts = result['state_counts'] or {}
            core = counts.get('shared_core')
            row[f'J{depth}_core_and_clock'] = core+1 if core is not None else None
            row[f'J{depth}_total_scalars'] = counts.get('total_dynamic_scalars')
            for reference in ('block', 'gaussian'):
                row[f'J{depth}_{reference}_rms'] = result['circle_errors'].get(reference, {}).get('rms')
        for reference in ('block', 'gaussian'):
            previous, current = row[f'J1_{reference}_rms'], row[f'J2_{reference}_rms']
            row[f'{reference}_reduction_percent'] = 100*(1-current/previous) if current is not None else None
        evidence[-1]['comparison_is_fitted_to_fitted'] = bool(old['fitted'] and new['fitted'])
        rows.append(row)
    output = args.run/'analysis'
    output.mkdir(parents=True, exist_ok=True)
    with (output/'summary.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (output/'summary.json').write_text(json.dumps({'records': evidence, 'table': rows,
        'analysis_source_sha256': digest(Path(__file__).resolve()),
        'metric': 'raw scalar minus reference circle RMS; each endpoint at its own first core MSE0.01, or explicitly partial'},
        indent=2, allow_nan=False)+'\n')
    print(json.dumps(rows, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
