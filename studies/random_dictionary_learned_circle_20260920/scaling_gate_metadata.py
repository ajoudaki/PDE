"""CPU-only protocol metadata checks; no model import, arrays, or training."""
import argparse
import hashlib
import json
import math
from pathlib import Path

DIMENSIONS = {1: (5, 3), 3: (35, 10), 5: (128, 21), 6: (213, 28),
              7: (333, 36), 8: (499, 45), 9: (720, 55)}
METHODS = ('ours', 'gaussian', 'orthogonal')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, action='append', required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    hashes, workers, dictionaries, problems = {}, [], [], []

    def read(path):
        blob = path.read_bytes()
        hashes[str(path.resolve())] = hashlib.sha256(blob).hexdigest()
        return json.loads(blob)

    for root in args.root:
        for path in sorted(root.glob('config_*.json')):
            config = read(path)
            suffix = path.stem.removeprefix('config_')
            selected = config['selected_cells']
            expected = [f'{case}_{model}' for i, case in enumerate(config['cases'])
                        if i % config['workers'] == config['worker']
                        for model in (['full'] if config['include_full'] else []) +
                        [f'{method}_p{order}' for order in config['orders_executed'] for method in METHODS]]
            if config['stage'] != 'extra' and selected != expected:
                problems.append(f'{path}: selected cells differ from declared cases/orders/worker')
            if config['stage'] == 'extra' and not set(selected).issubset(expected):
                problems.append(f'{path}: extra cell outside declared cases/orders/worker')
            if len(selected) != len(set(selected)):
                problems.append(f'{path}: duplicate selected cells')
            if not set(config['orders_executed']).issubset(config['orders']):
                problems.append(f'{path}: executed orders outside planned orders')
            if not 0 < config['worker_limit_seconds'] <= 600:
                problems.append(f'{path}: invalid worker cap')
            if config['stage'] in ('A', 'B'):
                if config['group'] != 'discovery' or config['width'] != 2048 or (
                        config['network_seed'], config['dictionary_seed']) != (20260920, 7319):
                    problems.append(f'{path}: discovery identity changed')
                required = [6, 7] if config['stage'] == 'A' else [8, 9]
                if config['orders_executed'] != required:
                    problems.append(f'{path}: unexpected stage orders')
                if config['include_full'] != (config['stage'] == 'A'):
                    problems.append(f'{path}: unexpected full-reference execution')
            results_path = root / f'results_{suffix}.json'
            completion_path = root / f'completion_{suffix}.json'
            results = read(results_path) if results_path.exists() else {}
            completion = read(completion_path) if completion_path.exists() else None
            if not set(results).issubset(selected):
                problems.append(f'{path}: undeclared results')
            if completion:
                if set(results) != set(selected) or completion['planned_cells'] != selected:
                    problems.append(f'{path}: completed selected/result/planned mismatch')
                if completion['total'] != len(results):
                    problems.append(f'{path}: total count mismatch')
                if completion['fitted'] != sum(x['status'] == 'fitted' for x in results.values()):
                    problems.append(f'{path}: fitted count mismatch')
                if completion['exit_status'] != 0:
                    problems.append(f'{path}: worker failed')
            for key, result in results.items():
                summary_path = root / key / 'summary.json'
                if not summary_path.exists() or read(summary_path) != result:
                    problems.append(f'{path}: summary/result mismatch for {key}')
            workers.append({'config': str(path.resolve()), 'stage': config['stage'],
                            'group': config['group'], 'selected': selected,
                            'planned_orders': config['orders'], 'executed_orders': config['orders_executed'],
                            'reserved_seconds': config['worker_limit_seconds'],
                            'completion': completion, 'statuses': {key: value['status'] for key, value in results.items()}})
        for path in sorted(root.glob('dictionary_*.json')):
            record = read(path)
            failures = []
            if not record['all_finite'] or tuple(record['nominal_dimensions']) != DIMENSIONS[record['order']]:
                failures.append('nonfinite dictionary or incorrect dimensions')
            if record['random_legacy_dimensions'] != [128, 21] or record['random_appended_dimensions'] != [592, 34] or record['random_appended_seed_offset'] != 100000:
                failures.append('changed random-block construction')
            if record['method'] == 'ours' and record['ridge'] != 1 / (1024 * (record['order'] + 1) ** 2):
                failures.append('changed ridge')
            populations = []
            for i, population in enumerate(record['populations']):
                condition = population['ridge_condition']
                triangular = population['triangular_solve_residual']
                orthogonal = max(abs(x - 1) for x in population['normalized_gram_eigenvalues']) if record['method'] == 'orthogonal' else None
                if not all(population['finite_checks'].values()) or not all(math.isfinite(x) for x in population['normalized_gram_eigenvalues']):
                    failures.append(f'population {i+1}: nonfinite condition')
                if record['method'] == 'ours' and (condition is None or not math.isfinite(condition) or not 1 <= condition <= 1e10):
                    failures.append(f'population {i+1}: regularized Gram condition failed')
                if record['method'] == 'ours' and (triangular is None or not math.isfinite(triangular) or triangular > 1e-8):
                    failures.append(f'population {i+1}: triangular residual failed')
                if orthogonal is not None and orthogonal > 1e-8:
                    failures.append(f'population {i+1}: orthogonal residual failed')
                populations.append({'nominal': population['nominal_count'], 'rank': population['numerical_rank'],
                                    'ridge_condition': condition, 'triangular_residual': triangular,
                                    'orthogonal_eigenvalue_residual': orthogonal})
            problems.extend(f'{path}: {failure}' for failure in failures)
            dictionaries.append({'path': str(path.resolve()), 'order': record['order'], 'method': record['method'],
                                 'width': record['width'], 'populations': populations, 'pass': not failures})
    completed = [worker for worker in workers if worker['completion'] is not None]
    total_seconds = sum(worker['completion']['seconds'] for worker in completed)
    output = {'scope': 'Saved producer metadata, not independent raw arithmetic or ODE certification',
              'workers': workers, 'dictionaries': dictionaries, 'problems': problems,
              'completed_worker_seconds': total_seconds, 'remaining_6000_seconds': 6000-total_seconds,
              'completed_selected_count': sum(len(worker['selected']) for worker in completed),
              'input_hashes': hashes}
    args.out.write_text(json.dumps(output, indent=2, allow_nan=False) + '\n')
    print(json.dumps({key: output[key] for key in ('problems', 'completed_worker_seconds', 'remaining_6000_seconds', 'completed_selected_count')}))

if __name__ == '__main__':
    main()
