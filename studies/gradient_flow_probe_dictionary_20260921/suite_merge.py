"""Merge disjoint case audits, replacing only preauthorized refinement cases.

No raw-state or trajectory computation occurs. Exact saved metrics are retained;
nearest-available-size pairwise comparisons are derived from those metrics.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np
import suite_analyze as analysis


def sha(path):
    result = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(8*1024*1024), b''):
            result.update(block)
    return result.hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')


def chunk(path, manifest_hash):
    path=analysis.owned(path) if hasattr(analysis,'owned') else analysis.base.owned(path)
    data={name:read(path/(name+'.json')) for name in ('metrics','validation','gates','completion','provenance')}
    if data['completion']['status'] != 'complete':
        raise ValueError('only complete case chunks can be merged: '+str(path))
    if data['provenance']['manifest_sha256'] != manifest_hash:
        raise ValueError('chunk manifest mismatch: '+str(path))
    hashes={str(path/(name+'.json')):sha(path/(name+'.json')) for name in ('metrics','validation','gates','completion','provenance')}
    prediction_path=path/'endpoint_predictions.npz'
    hashes[str(prediction_path)]=sha(prediction_path)
    declared=data['provenance']['output_hashes']
    for artifact,digest in hashes.items():
        if artifact in declared and declared[artifact] != digest:
            raise ValueError('chunk artifact changed: '+artifact)
    data.update(path=str(path),file_hashes=hashes)
    return data


def case_keys(case):
    return [case+'_'+method for method in ('full',*analysis.METHODS)]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--analysis',nargs='+',type=Path,required=True)
    parser.add_argument('--replacement',nargs='+',type=Path,default=[])
    parser.add_argument('--manifest',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    started=time.monotonic()
    manifest=read(args.manifest)
    manifest_hash=sha(args.manifest)
    cases=list(manifest['cases'])
    out=analysis.base.owned(args.out)
    if out.exists():
        raise FileExistsError(out)
    base_chunks=[chunk(path,manifest_hash) for path in args.analysis]
    replacements=[chunk(path,manifest_hash) for path in args.replacement]
    selected={}
    originals={}
    for item in base_chunks:
        completed=item['completion']['completed_cases']
        if set(completed) != {r['case'] for r in item['metrics']}:
            raise ValueError('incomplete metrics case coverage')
        for case in completed:
            if case in selected or case not in cases:
                raise ValueError('duplicate/unknown base case: '+case)
            selected[case]=item
            originals[case]=item
    if set(selected) != set(cases):
        raise ValueError('base chunks must cover all manifest cases exactly once')
    replacement_log=[]
    already_replaced=set()
    for item in replacements:
        for case in item['completion']['completed_cases']:
            if case not in selected or case in already_replaced:
                raise ValueError('unknown or duplicate replacement case: '+case)
            original=originals[case]
            allowed={gate['cell'] for gate in original['gates']['cells'] if gate['eligible'] and gate['cell'].startswith(case+'_')}
            if not allowed:
                raise ValueError('case has no predeclared numerical-refinement trigger: '+case)
            changed=[]
            for key in case_keys(case):
                old=original['validation'][key]
                new=item['validation'][key]
                old_paths=[a['path'] for a in old['attempts']]
                new_paths=[a['path'] for a in new['attempts']]
                if new_paths != old_paths:
                    if key not in allowed or new_paths[:-1] != old_paths or len(new_paths) != len(old_paths)+1:
                        raise ValueError('replacement contains an unauthorized changed cell: '+key)
                    if not new['branch_checks'] or new['branch_checks'][-1]['eligible'] is not True:
                        raise ValueError('replacement refinement branch was not validated: '+key)
                    changed.append(key)
            if set(changed) != allowed:
                raise ValueError('replacement must retain all and only the preauthorized extra attempts: '+case)
            selected[case]=item
            already_replaced.add(case)
            replacement_log.append(dict(case=case,old_analysis=original['path'],replacement_analysis=item['path'],
                changed_cells=changed,rule='latest pair after the single preauthorized numerical refinement, regardless of score or validity'))
    rows=[]
    validation={}
    predictions={}
    gates=[]
    case_provenance={}
    for case in cases:
        item=selected[case]
        case_rows=[r for r in item['metrics'] if r['case']==case]
        if {r['method'] for r in case_rows} != set(analysis.METHODS) or len(case_rows) != 12:
            raise ValueError('case must retain every method/order: '+case)
        rows.extend(case_rows)
        for key in case_keys(case):
            validation[key]=item['validation'][key]
        gates.extend(g for g in item['gates']['cells'] if g['cell'].startswith(case+'_'))
        with np.load(Path(item['path'])/'endpoint_predictions.npz',allow_pickle=False) as arrays:
            keys=[key for key in arrays.files if key.startswith(case+'_')]
            if len(keys) != 27:
                raise ValueError('case endpoint prediction coverage differs from 13 methods × 2 levels + angles: '+case)
            predictions.update({key:arrays[key] for key in keys})
        case_provenance[case]=dict(selected_analysis=item['path'],source_file_hashes=item['file_hashes'],
            original_analysis=originals[case]['path'],numerical_replacement=case in already_replaced)
    comparisons=analysis.compare_rows(rows)
    if len(rows) != 132 or len(validation) != 143 or len(comparisons) != 99:
        raise ValueError('unexpected suite coverage')
    out.mkdir(parents=True)
    write(out/'metrics.json',rows)
    write(out/'validation.json',validation)
    write(out/'comparisons.json',comparisons)
    write(out/'gates.json',dict(cells=gates,eligible_cells=[g['cell'] for g in gates if g['eligible']],replacements=replacement_log))
    np.savez(out/'endpoint_predictions.npz',**predictions)
    analysis.csv_write(out/'metrics.csv',rows)
    analysis.csv_write(out/'comparisons.csv',comparisons)
    write(out/'case_sources.json',case_provenance)
    write(out/'completion.json',dict(status='complete',seconds=time.monotonic()-started,cpu_merge_only=True,
        declared_cases=cases,completed_cases=cases,incomplete_cases=[],rows=len(rows),valid_rows=sum(r['valid'] for r in rows),
        cells=len(validation),comparisons=len(comparisons)))
    write(out/'provenance.json',dict(command=sys.argv,cpu_merge_only=True,
        manifest_path=str(args.manifest.resolve()),manifest_sha256=manifest_hash,
        merger_sha256=sha(__file__),comparison_source_sha256=sha(analysis.__file__),
        case_sources=case_provenance,replacements=replacement_log,
        comparison_policy='closest AVAILABLE archived total-vector count: new6/old8,new18/old8,new38/old45; each control separate',
        superseded='Original same-p comparisons in suite_analysis01a/comparisons.json are superseded; their unmodified metrics remain inputs.',
        output_hashes={str(path):sha(path) for path in sorted(out.iterdir()) if path.is_file()}))
    print(json.dumps(dict(out=str(out),rows=len(rows),valid_rows=sum(r['valid'] for r in rows),
        comparisons=len(comparisons),replaced_cases=sorted(already_replaced),seconds=time.monotonic()-started)),flush=True)


if __name__=='__main__':
    main()
