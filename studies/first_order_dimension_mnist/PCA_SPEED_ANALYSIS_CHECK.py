"""Compare the root's benchmark-only export with independent audit arithmetic."""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "data/generated/first_order_dimension_mnist"
HERE = BASE / "pca_speed_check"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    independent = json.loads((HERE / 'check.json').read_text())
    source = BASE / 'pca_benchmark_analysis_003/summary.json'
    exported = json.loads(source.read_text())
    benchmark = exported['benchmark']
    checks = []

    def equal(label, actual, expected):
        if isinstance(expected, float):
            good = math.isclose(actual, expected, rel_tol=1e-13, abs_tol=1e-14)
        else:
            good = actual == expected
        checks.append({'field': label, 'passed': good, 'actual': actual, 'expected': expected})

    equal('physical_horizon', benchmark['physical_horizon'], 100)
    equal('row_count', len(benchmark['rows']), 8)
    for row in benchmark['rows']:
        name = f"{row['representation']}_{row['model']}_r{row['repetition']}"
        reference = independent['runs'][name]
        for key in ('gpu', 'dimension', 'integration_seconds', 'training_wall_seconds', 'initialization_seconds'):
            equal(f'rows.{name}.{key}', row[key], reference[key])
        for key in ('peak_allocated', 'moving_state', 'retained_model'):
            equal(f'rows.{name}.{key}_MiB', row[key + '_MiB'], reference[key + '_bytes'] / 2**20)
        equal(f'rows.{name}.summary_sha256', row['summary_sha256'], independent['input_hashes'][name]['summary_sha256'])
    for representation in ('original', 'pca'):
        for model in ('network', 'closure'):
            name = f'{representation}_{model}'
            rows = [independent['runs'][f'{name}_r{rep}'] for rep in (1,2)]
            times = [row['integration_seconds'] for row in rows]
            peaks = [row['peak_allocated_bytes'] / 2**20 for row in rows]
            aggregate = benchmark['aggregate'][representation][model]
            expected = {
                'integration_seconds_range': [min(times), max(times)],
                'mean_integration_seconds': sum(times)/2,
                'peak_allocated_MiB_range': [min(peaks), max(peaks)],
                'relative_timing_range': (max(times)-min(times))/(sum(times)/2),
                'timing_variation_exceeds_15_percent': independent['timing_dispersion'][name]['above_15_percent'],
            }
            for key,value in expected.items():
                equal(f'aggregate.{name}.{key}', aggregate[key], value)
    for row in benchmark['same_gpu_comparisons']:
        gpu = row['gpu']
        for name, comparisons in row['comparisons'].items():
            independent_name = name.replace('_vs_', '_over_')
            reference = independent['same_gpu_ratios'][independent_name]['per_gpu'][gpu]
            equal(f'ratios.{gpu}.{name}.integration_speedup', comparisons['integration_speedup'], 1/reference['integration_seconds'])
            equal(f'ratios.{gpu}.{name}.training_loop_speedup', comparisons['training_loop_speedup'], 1/reference['training_wall_seconds'])
            equal(f'ratios.{gpu}.{name}.peak_memory_reduction_fraction', comparisons['peak_memory_reduction_fraction'], 1-reference['peak_allocated_bytes'])
    equal('PCA_metadata_exact', exported['pca'], json.loads((BASE / 'data_pca98/metadata.json').read_text()))
    equal('analysis_source_sha256', exported['analysis_source_sha256'], sha(ROOT / 'studies/first_order_dimension_mnist/PCA_ANALYZE.py'))
    result = {'passed': all(item['passed'] for item in checks), 'field_count': len(checks),
              'checks': checks, 'root_summary_sha256': sha(source),
              'independent_check_sha256': sha(HERE / 'check.json'), 'source_sha256': sha(Path(__file__)),
              'scope': 'Benchmark rows, ranges, ratio arithmetic, PCA metadata and provenance only; no main-run scientific analysis claims'}
    (HERE / 'root_analysis_check.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'passed': result['passed'], 'field_count': result['field_count'],
                      'failed': [item for item in checks if not item['passed']]}))


if __name__ == '__main__':
    main()
