"""Append audited p7 results to the frozen suite, with explicit numerical replacements."""
import argparse
import json
from pathlib import Path
import numpy as np
import suite_merge as previous
import p7_analyze


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--analysis', type=Path, nargs='+', required=True)
    parser.add_argument('--replacement', type=Path, nargs='*', default=[])
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    base = p7_analyze.suite.DATA/'suite_analysis_final01'
    manifest_path = p7_analyze.suite.STUDY/'SUITE_MANIFEST.json'
    manifest = previous.read(manifest_path)
    cases = list(manifest['cases'])
    manifest_hash = previous.sha(manifest_path)
    base_provenance = previous.read(base/'provenance.json')
    assert base_provenance['manifest_sha256'] == manifest_hash
    base_hashes = {}
    for name in ('metrics.json','validation.json','comparisons.json','gates.json','endpoint_predictions.npz','completion.json'):
        path = base/name
        actual = previous.sha(path)
        assert base_provenance['output_hashes'][str(path)] == actual
        base_hashes[str(path)] = actual
    out = p7_analyze.suite.base.owned(args.out)
    assert not out.exists()
    selected = {}
    replacements = []
    for directory in args.analysis:
        chunk = previous.chunk(directory, manifest_hash)
        for case in chunk['completion']['completed_cases']:
            assert case in cases and case not in selected
            selected[case] = chunk
    assert set(selected) == set(cases)
    for directory in args.replacement:
        chunk = previous.chunk(directory, manifest_hash)
        for case in chunk['completion']['completed_cases']:
            old = selected[case]
            key = case+'_new_p7'
            assert any(g['cell']==key and g['eligible'] for g in old['gates']['cells'])
            a,b = old['validation'][key], chunk['validation'][key]
            assert len(a['attempts']) == 2 and len(b['attempts']) == 3
            assert [r['path'] for r in a['attempts']] == [r['path'] for r in b['attempts'][:2]]
            assert b['branch_checks'][-1]['eligible']
            assert old['validation'][case+'_full']['selected_paths'] == chunk['validation'][case+'_full']['selected_paths']
            selected[case] = chunk
            replacements.append(dict(case=case, preceding=old['path'], selected=chunk['path'],
                                     rule='latest two attempts after one gated /4 refinement, regardless of result'))
    rows = previous.read(base/'metrics.json')
    validation = previous.read(base/'validation.json')
    comparisons = previous.read(base/'comparisons.json')
    gates = previous.read(base/'gates.json')
    with np.load(base/'endpoint_predictions.npz', allow_pickle=False) as arrays:
        predictions = {key:arrays[key] for key in arrays.files}
    sources = {}
    for case in cases:
        chunk = selected[case]
        new = [row for row in chunk['metrics'] if row['case']==case]
        assert len(new)==1 and new[0]['method']=='new_p7'
        old_row = next(row for row in rows if row['case']==case)
        assert all(new[0][level+'_full_path']==old_row[level+'_full_path'] for level in ('primary','refined'))
        old_full = validation[case+'_full']
        fresh_full = chunk['validation'][case+'_full']
        assert old_full['selected_paths'] == fresh_full['selected_paths']
        assert [r['arrays_sha256'] for r in old_full['attempts'][-2:]] == [r['arrays_sha256'] for r in fresh_full['attempts'][-2:]]
        rows.extend(new)
        validation[case+'_new_p7'] = chunk['validation'][case+'_new_p7']
        comparisons.extend(p7_analyze.compare_rows(new))
        gates['cells'].extend(g for g in chunk['gates']['cells'] if g['cell']==case+'_new_p7')
        with np.load(Path(chunk['path'])/'endpoint_predictions.npz', allow_pickle=False) as arrays:
            for level in ('primary','refined'):
                key = case+'_new_p7_'+level+'_prediction'
                predictions[key] = arrays[key]
        sources[case] = dict(path=chunk['path'], file_hashes=chunk['file_hashes'])
    assert len(rows)==143 and len(validation)==154 and len(comparisons)==143
    gates['eligible_cells'] = [g['cell'] for g in gates['cells'] if g['eligible']]
    gates['p7_replacements'] = replacements
    out.mkdir(parents=True)
    for name,value in (('metrics',rows),('validation',validation),('comparisons',comparisons),('gates',gates)):
        previous.write(out/(name+'.json'),value)
    np.savez(out/'endpoint_predictions.npz',**predictions)
    previous.analysis.csv_write(out/'metrics.csv',rows)
    previous.analysis.csv_write(out/'comparisons.csv',comparisons)
    previous.write(out/'completion.json',dict(status='complete',cpu_merge_only=True,completed_cases=cases,
        rows=len(rows),valid_rows=sum(row['valid'] for row in rows),p7_valid_rows=sum(row['valid'] for row in rows if row['method']=='new_p7')))
    previous.write(out/'provenance.json',dict(base_path=str(base),base_metrics_sha256=previous.sha(base/'metrics.json'),
        base_artifact_hashes=base_hashes,base_provenance_sha256=previous.sha(base/'provenance.json'),
        manifest_sha256=manifest_hash,merger_sha256=previous.sha(__file__),p7_comparison_source_sha256=previous.sha(p7_analyze.__file__),
        selected_p7_sources=sources,replacements=replacements,
        output_hashes={str(p):previous.sha(p) for p in sorted(out.iterdir()) if p.is_file()}))
    print(json.dumps(previous.read(out/'completion.json')))


if __name__ == '__main__':
    main()
