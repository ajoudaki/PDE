"""Independent NumPy audit of final saved-panel arithmetic; never evolve a model.

Use --metrics METRICS_SUMMARY --output FRESH_JSON. This checks scalar scores,
gates, selected resolutions, availability, and order comparisons against saved
arrays. Physical-state replay and campaign accounting remain separate checks.
No producer or analyzer is imported.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import zipfile

import numpy as np

STUDY = Path(__file__).resolve().parent
LOSSES = (.9, .5, .1, .03, .01, .003, .001)
TIMES = (10., 100., 1000.)
MODELS = ('dense', 'P1', 'P2', 'P3')
EXTRA = 7.8125e-7


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def rms(x):
    return float(np.sqrt(np.mean(np.asarray(x)**2)))


def main(metrics_path, output):
    started = time.monotonic()
    metrics_path, output = Path(metrics_path).resolve(), Path(output).resolve()
    if output.exists():
        raise FileExistsError(output)
    digest = sha(metrics_path)
    data = json.loads(metrics_path.read_text())
    cases = json.loads((STUDY/'activation_circle_cases.json').read_text())
    failures, checks, cache, integrity, differences = [], 0, {}, [], {}

    def check(value, name):
        nonlocal checks
        checks += 1
        if not value:
            failures.append(name)

    def scalar(actual, reported, name):
        if actual is None or reported is None:
            check(actual is reported, name)
            return
        error = abs(actual-reported)
        differences[name.split(':')[-1]] = max(error, differences.get(name.split(':')[-1], 0.))
        check(np.isfinite(error) and error <= 2e-12*max(1.,abs(actual)), name)

    for name, expected in data['source_sha256'].items():
        check(sha(STUDY/name) == expected, 'analysis_source:'+name)
    # Every valid scientific run is loaded, including resolutions not selected.
    for path, provenance in data['provenance'].items():
        p = Path(path)
        config, summary = (json.loads((p/name).read_text()) for name in ('config.json','summary.json'))
        actual = {name:sha(p/name) for name in ('config.json','summary.json','arrays.npz')}
        local = []
        for name, key in (('config.json','config_sha256'),('summary.json','summary_sha256'),('arrays.npz','arrays_sha256')):
            passed = actual[name] == provenance[key]
            local.append(passed); check(passed,path+':'+key)
        with zipfile.ZipFile(p/'arrays.npz') as z:
            passed = z.testzip() is None
            local.append(passed); check(passed,path+':crc')
        keys = ('observation_labels','observation_times','observation_training_mse',
                'circle_predictions','train_predictions','train_inputs','train_labels','circle_inputs')
        with np.load(p/'arrays.npz',allow_pickle=False) as z:
            arrays = {key:z[key] for key in keys}
        labels = list(map(str,arrays['observation_labels']))
        mse = np.mean((arrays['train_predictions']-arrays['train_labels'])**2,axis=1)
        records = {row['label']:row for row in summary['observations']}
        check(len(set(labels)) == len(labels) and set(labels) == set(records),path+':labels')
        check(np.isfinite(arrays['circle_predictions']).all(),path+':finite_panels')
        check(arrays['circle_predictions'].shape == (len(labels),8192),path+':panel_shape')
        check(np.array_equal(arrays['train_inputs'],config['inputs']) and
              np.array_equal(arrays['train_labels'],config['labels']),path+':saved_training_data')
        check(config['source_case_definition'] == cases[config['case']],path+':literal_case')
        check(config['activation'] == summary['activation'] == cases[config['case']]['activation'],path+':activation')
        scalar(float(np.max(abs(mse-arrays['observation_training_mse']))),0.,path+':training_mse_metadata')
        obs = {}
        for i,label in enumerate(labels):
            scalar(float(mse[i]),records[label]['training_mse'],path+':observation_mse')
            check(float(arrays['observation_times'][i]) == records[label]['time'],path+':observation_time')
            obs[label] = dict(pred=arrays['circle_predictions'][i],mse=float(mse[i]),
                              time=float(arrays['observation_times'][i]),requested_time=records[label]['requested_time'])
        cache[path] = dict(config=config,summary=summary,obs=obs,grid=arrays['circle_inputs'])
        integrity.append(dict(path=path,hashes=actual,hash_crc_passed=all(local)))

    groups = {}
    for path, run in cache.items():
        c = run['config']; model = 'dense' if c['model']=='dense' else 'P'+str(c['order'])
        groups.setdefault((c['case'],model),[]).append(path)
    selected = {}
    for (case,model), paths in groups.items():
        paths.sort(key=lambda p:cache[p]['config']['rtol'])
        check(len({cache[p]['config']['rtol'] for p in paths}) == len(paths),case+':'+model+':unique_tolerances')
        pair = [paths[0],paths[1] if len(paths)>1 else None]
        selected[(case,model)] = pair
        check(data['selected'][case][model] == dict(finest=pair[0],previous=pair[1]),case+':'+model+':selected')
    unusable = {(r.get('case'),r.get('model')) for r in data['attempts']
                if r.get('rtol') == EXTRA and not r.get('valid_scientific_run')}

    def evaluate(case, order, value, kind):
        label = ('loss_' if kind=='loss' else 'time_')+format(value,'.12g')
        cp,dp = selected.get((case,'P'+str(order))),selected.get((case,'dense'))
        if not cp or not dp or any(label not in cache[pair[0]]['obs'] for pair in (cp,dp)):
            return None
        paths = dict(closure_fine=cp[0],dense_fine=dp[0],closure_previous=cp[1],dense_previous=dp[1])
        obs = {key:cache[path]['obs'].get(label) if path else None for key,path in paths.items()}
        c,d = obs['closure_fine'],obs['dense_fine']
        delta = c['pred']-d['pred']; error,nested = rms(delta),rms(delta[::2])
        cs = rms(c['pred']-obs['closure_previous']['pred']) if obs['closure_previous'] else None
        ds = rms(d['pred']-obs['dense_previous']['pred']) if obs['dense_previous'] else None
        gates = dict(closure_refinement_available=cs is not None,dense_refinement_available=ds is not None,
                     closure_absolute=cs is not None and cs<=.005,dense_absolute=ds is not None and ds<=.005,
                     closure_relative=cs is not None and cs<=.1*error,dense_relative=ds is not None and ds<=.1*error,
                     grid=abs(error-nested)<=1e-5)
        if kind=='loss':
            gates['physical_loss'] = all(o is not None and abs(o['mse']/value-1)<=.01 for o in obs.values())
        else:
            gates['physical_time'] = all(o is not None and o['time']==value and o['requested_time']==value for o in obs.values())
        for prefix,model in (('closure','P'+str(order)),('dense','dense')):
            if (case,model) in unusable:
                gates[prefix+'_additional_resolution_unavailable'] = False
        passed = all(gates.values())
        verdict = ('coarse_agreement' if error<=.1 else 'coarse_disagreement') if passed else 'numerically_inconclusive'
        if kind=='time' and passed:
            verdict = 'matched_time_diagnostic'
        return dict(rms_8192=error,rms_4096=nested,nested_grid_change=abs(error-nested),
                    closure_refinement_rms=cs,dense_refinement_rms=ds,
                    combined_sensitivity=cs+ds if cs is not None and ds is not None else None,
                    closure_time=c['time'],dense_time=d['time'],
                    physical_losses={key:o['mse'] if o else None for key,o in obs.items()},
                    numerical_gates=gates,numerical_pass=passed,failed_gates=[k for k,v in gates.items() if not v],
                    measured_coarse_agreement=error<=.1,scientific_verdict=verdict)

    results = {}
    counts = {}
    tables = (('comparisons','loss'),('primary_comparisons','loss'),('fallback_comparisons','loss'),('matched_time_comparisons','time'))
    for table,kind in tables:
        counts[table] = len(data[table])
        seen = set()
        for row in data[table]:
            value = row['milestone'] if kind=='loss' else row['requested_time']
            identity = (row['case'],row['P'],value)
            check(identity not in seen,table+':duplicate:'+str(identity));seen.add(identity)
            answer = evaluate(row['case'],row['P'],value,kind)
            if answer is None:
                check(table=='primary_comparisons' and row.get('available') is False and
                      row['scientific_verdict']=='primary_unavailable',table+':unavailable:'+str(identity))
                continue
            check(row.get('available') is True,table+':available:'+str(identity))
            cp,dp = selected[(row['case'],'P'+str(row['P']))],selected[(row['case'],'dense')]
            for key,path in zip(('closure_run','closure_previous','dense_run','dense_previous'),(*cp,*dp)):
                check(row[key]==path,table+':'+str(identity)+':'+key)
            for name,actual in answer.items():
                if name=='physical_losses':
                    for k,v in actual.items(): scalar(v,row[name][k],table+':'+str(identity)+':'+k)
                elif name=='failed_gates': check(set(actual)==set(row[name]),table+':'+str(identity)+':'+name)
                elif isinstance(actual,(dict,bool,str)):
                    check(actual==row[name],table+':'+str(identity)+':'+name)
                else: scalar(actual,row[name],table+':'+str(identity)+':'+name)
            if table=='comparisons': results[identity]=answer
        expected = {(case,order,value) for case in cases for order in (1,2,3)
                    for value in ((.001,) if table=='primary_comparisons' else TIMES if kind=='time' else LOSSES)
                    if table=='primary_comparisons' or evaluate(case,order,value,kind) is not None}
        if table!='fallback_comparisons': check(seen==expected,table+':complete_row_inventory')

    expected_ranks = set()
    for case,order,value in results:
        for low,high in ((1,2),(1,3),(2,3)):
            if (case,low,value) in results and (case,high,value) in results:
                expected_ranks.add((case,value,low,high))
    seen = set()
    for row in data['order_comparisons']:
        identity = (row['case'],row['milestone'],row['lower_P'],row['higher_P'])
        check(identity not in seen,'rank_duplicate');seen.add(identity)
        low,high = (results[(row['case'],order,row['milestone'])] for order in (row['lower_P'],row['higher_P']))
        gap = low['rms_8192']-high['rms_8192']
        margin = low['combined_sensitivity']+high['combined_sensitivity'] if all(r['combined_sensitivity'] is not None for r in (low,high)) else None
        both = low['numerical_pass'] and high['numerical_pass']
        resolved = both and margin is not None and abs(gap)>margin
        verdict = ('higher_order_improves' if gap>0 else 'higher_order_worsens') if resolved else 'unresolved'
        scalar(gap,row['lower_minus_higher_rms'],'rank:gap')
        scalar(margin,row['summed_observed_sensitivity'],'rank:margin')
        check((both,resolved,verdict)==(row['both_numerical_gates_pass'],row['resolved'],row['verdict']),'rank:'+str(identity))
    check(seen==expected_ranks,'rank_complete_inventory')
    counts.update(valid_runs=len(cache),order_comparisons=len(seen),checks=checks)
    check(sha(metrics_path)==digest,'metrics_unchanged')
    result = dict(passed=not failures,failures=failures,counts=counts,maximum_discrepancies=differences,
                  input_metrics=str(metrics_path),input_metrics_sha256=digest,auditor_sha256=sha(__file__),
                  command=sys.argv,python=sys.version,numpy=np.__version__,integrity=integrity,
                  scope='Independent CPU saved-panel rescore; no trajectory or physical-state replay',
                  elapsed_seconds=time.monotonic()-started)
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('x') as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps({k:result[k] for k in ('passed','failures','counts','maximum_discrepancies','elapsed_seconds')},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--metrics',required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    main(args.metrics,args.output)
