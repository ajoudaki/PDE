"""Audit only the new p7 extension, retaining the fixed common references.

The saved-state reader and direct forward arithmetic come from the previously
checked suite analyzer. This explicit adapter adds p7 dimensions, dependency
requirements and moment checks; it imports no model producer or builder.
"""
import sys
from pathlib import Path
import suite_analyze as suite

READ = suite.base.read_json
WRITE = suite.base.write_json
OLD_METRICS = suite.DATA/'suite_analysis_final01/metrics.json'
ORIGINAL_AUDIT = suite.audit
ORIGINAL_SOURCE_AUDIT = suite.source_audit


def source_audit(config, spec, current, require, recoveries=None):
    checks = ORIGINAL_SOURCE_AUDIT(config, spec, current, require, recoveries)
    if current:
        names = ('new_dictionary_p7.py', 'p7_gaussian_check.py', 'p7_run.py',
                 'P7_PROTOCOL.md', 'P7_DICTIONARY_SPEC.md', 'P7_DERIVATION.md',
                 'P7_GAUSSIAN_CONTRACTIONS.md')
        hashes = config.get('source_hashes', {})
        for name in names:
            path = suite.STUDY/name
            key = str(path.relative_to(suite.ROOT))
            checks[key] = key in hashes and suite.base.digest(path) == hashes[key]
            require(checks[key], 'missing or changed p7 dependency: '+key)
    return checks


def audit(*args, **kwargs):
    record, bundle = ORIGINAL_AUDIT(*args, **kwargs)
    method = kwargs.get('method', args[3] if len(args) > 3 else None)
    if method == 'new_p7' and 'dictionary_metadata_path' in record:
        metadata = READ(record['dictionary_metadata_path'])
        moments = metadata['p7_population_moments']
        if moments['maximum_discrepancy'] > 1e-9:
            record['reasons'].append('p7 population moment resolution gate failed')
        if metadata['maximum_weight_taylor_power'] != 8:
            record['reasons'].append('p7 Taylor-order mismatch')
        if record['reasons']:
            record['valid'] = False
            record['replay_valid'] = False
    return record, bundle


def compare_rows(rows):
    historical = {(r['case'], r['method']): r for r in READ(OLD_METRICS)}
    comparisons = []
    for left in rows:
        for target in ('old_p3','gaussian_p3','orthogonal_p3','new_p5'):
            right = historical[left['case'], target]
            winners = []
            item = dict(case=left['case'], p=7, new_p=7, against=right['family'],
                        baseline_p=right['p'], baseline_method=target,
                        new_vectors=72, baseline_vectors=right['vectors'],
                        comparison_policy='closest archived vector count 45 among 8,45,149; new38 separately',
                        valid=left['valid'] and right['valid'])
            for level in suite.LEVELS:
                a, b = left.get(level+'_rms'), right.get(level+'_rms')
                winner = 'unavailable' if a is None or b is None else 'new_p7' if a < b else target if b < a else 'tie'
                item[level+'_winner'] = winner
                item[level+'_baseline_over_new_rms'] = b/a if a is not None and b is not None and a > 0 else None
                winners.append(winner)
            item['ordering_agrees'] = winners[0] == winners[1] and winners[0] != 'unavailable'
            item['verdict'] = winners[0] if item['valid'] and item['ordering_agrees'] else 'inconclusive'
            comparisons.append(item)
    return comparisons


def main():
    suite.COUNTS['new'][7] = (26,46)
    suite.METHODS = ('new_p7',)
    suite.ORDERS = (7,)
    suite.source_audit = source_audit
    suite.audit = audit
    suite.compare_rows = compare_rows
    suite.main()
    out = Path(sys.argv[sys.argv.index('--out')+1]).resolve()
    provenance = READ(out/'provenance.json')
    provenance['executed_analysis_sources'][str(Path(__file__))] = suite.base.digest(__file__)
    provenance['historical_metrics'] = dict(path=str(OLD_METRICS), sha256=suite.base.digest(OLD_METRICS))
    provenance['comparison_policy'] = 'new72 vs archived45 (closest available); new72 vs new38 separately'
    provenance['numerical_limits']['max_extra_new_total'] = 11
    WRITE(out/'provenance.json', provenance)


if __name__ == '__main__':
    main()
