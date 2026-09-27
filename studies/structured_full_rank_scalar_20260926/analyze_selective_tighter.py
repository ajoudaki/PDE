"""Raw circle errors before and after checkpoint continuation to tighter MSE."""
from __future__ import annotations

import csv
import json
from pathlib import Path

from analyze_selective_order import DATA, TASKS, digest, measure


def main():
    run = DATA/'selective_tighter_20260927'
    previous = DATA/'selective_geometry_20260927'
    order = DATA/'selective_order_20260927'
    rows, evidence = [], []
    for task in TASKS:
        for depth in (1, 2):
            prior_path = ((previous/'scalar'/f'{task}__selective_zero.json') if depth == 1
                else order/'scalar'/f'{task}__selective_zero_out2.json')
            new_path = run/'scalar'/f'{task}__selective_zero_out{depth}.json'
            prior = measure(prior_path, previous/'references')
            new = measure(new_path, run/'references')
            metadata = json.loads(new_path.read_text())
            for suffix in ('gaussian', 'block_k4_P1_canonical'):
                ref = json.loads((run/'references'/f'{task}__{suffix}.json').read_text())
                if ref['target_mse'] != metadata['target_mse']:
                    raise ValueError('Unmatched reference stopping target')
            row = {'task': task, 'J': depth, 'target_mse': metadata['target_mse'],
                'fitted': new['fitted'], 'core_mse': new['train_mse'],
                'passive_train_mse': new['passive_train_mse'],
                'alias_gap_max': new['alias_gap_max'],
                'additional_training_seconds': new['training_seconds'],
                'physical_time': new['physical_time'],
                'total_scalars': new['state_counts']['total_dynamic_scalars']}
            for ref in ('block', 'gaussian'):
                row[f'previous_{ref}_rms'] = prior['circle_errors'][ref]['rms']
                row[f'tighter_{ref}_rms'] = new['circle_errors'][ref]['rms']
                row[f'{ref}_grid_change'] = new['circle_errors'][ref]['grid_change_64_vs_32']
            rows.append(row)
            evidence.append({'task': task, 'J': depth, 'previous': prior, 'tighter': new})
    comparisons = []
    for task in TASKS:
        low, high = [r for r in rows if r['task'] == task]
        pair = {'task': task, 'both_fitted': bool(low['fitted'] and high['fitted'])}
        for ref in ('block', 'gaussian'):
            pair[f'J1_{ref}_rms'] = low[f'tighter_{ref}_rms']
            pair[f'J2_{ref}_rms'] = high[f'tighter_{ref}_rms']
            pair[f'order_increase_reduction_percent_{ref}'] = 100*(1-high[f'tighter_{ref}_rms']/low[f'tighter_{ref}_rms'])
        comparisons.append(pair)
    output = run/'analysis'
    output.mkdir(parents=True, exist_ok=True)
    with (output/'summary.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (output/'summary.json').write_text(json.dumps({'table': rows, 'order_comparison': comparisons,
        'records': evidence, 'analysis_source_sha256': digest(Path(__file__).resolve()),
        'analysis_dependency_sha256': digest(Path(__file__).with_name('analyze_selective_order.py')),
        'partial_comparisons_not_fitted': True}, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'table': rows, 'order_comparison': comparisons}, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
