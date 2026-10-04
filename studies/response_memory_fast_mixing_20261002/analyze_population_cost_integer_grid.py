"""Post-result significance challenge: remove the sparse ensemble-size grid.

This reuses the original expected squared-error estimator; it does not generate
or claim fresh ensemble measurements. In particular K>16 is extrapolated from
16 independent candidate trajectories. Frozen primary analysis is unchanged.
"""
import hashlib
import json
import math
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
SOURCE = BASE / 'data/generated/response_memory_fast_mixing_20261002/population_cost_split_analysis01/population_cost.json'
OUT = BASE / 'data/generated/response_memory_fast_mixing_20261002/population_cost_integer_grid01'


def main():
    report = json.loads(SOURCE.read_text())
    tolerance = 0.0025
    rows = []
    for condition in report['conditions']:
        sample_count = len(condition['seeds'])
        assert sample_count == 16
        diagnostics = condition['diagnostics']
        eligible = []
        for size in range(1, 257):
            errors = {
                name: value['squared_mean_reference_distance']
                + (1 / size - 1 / sample_count) * value['sample_variance']
                for name, value in diagnostics.items()
            }
            if all(error <= tolerance**2 for error in errors.values()):
                eligible.append((size, errors))
        if not eligible:
            rows.append(dict(kind=condition['kind'], width=condition['width'], eligible=False))
            continue
        size, errors = eligible[0]
        # An independent algebraic check of the minimal integer at this width.
        required = []
        for value in diagnostics.values():
            variance = value['sample_variance']
            intercept = value['squared_mean_reference_distance'] - variance / sample_count
            required.append(max(1, math.ceil(variance / (tolerance**2 - intercept))))
        assert max(required) == size
        rows.append(dict(kind=condition['kind'], width=condition['width'], eligible=True,
                         K=size, cost_seconds=size * condition['median_trajectory_seconds'],
                         estimated_squared_errors=errors,
                         display_rms={name: math.sqrt(max(0, error)) for name, error in errors.items()},
                         beyond_observed_sample_count=size > sample_count))
    winners = {kind: min((row for row in rows if row['kind'] == kind and row['eligible']),
                         key=lambda row: row['cost_seconds'])
               for kind in ('gaussian', 'quarter_circle')}
    ratio = winners['quarter_circle']['cost_seconds'] / winners['gaussian']['cost_seconds']
    result = dict(status='POST_RESULT_ANALYTICAL_CHALLENGE', tolerance=tolerance,
                  ensemble_sizes='all integers 1 through 256', conditions=rows,
                  winners=winners, fast_over_gaussian_cost=ratio,
                  gaussian_over_fast_cost=1 / ratio,
                  source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                  producer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  qualification='Expected squared-error estimates from 16 runs per condition; '
                  'no fresh K-run ensembles, no new bootstrap, no infinite-width certificate. '
                  'The frozen powers-of-two grid result is unchanged.')
    OUT.mkdir(parents=True, exist_ok=False)
    (OUT / 'integer_grid.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(winners=winners, ratio=ratio, speedup=1 / ratio), indent=2))


if __name__ == '__main__':
    main()
