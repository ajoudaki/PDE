#!/usr/bin/env python3
"""Cross-check frozen arithmetic and artifacts after the fixed experiment."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
STUDY=Path(__file__).resolve().parent
BASE=ROOT/'data/generated/xor_network_closure/run_001'
CACHE={}


def sha(path):
    path=Path(path).resolve()
    if path not in CACHE:
        h=hashlib.sha256()
        with path.open('rb') as f:
            for chunk in iter(lambda:f.read(4*1024*1024),b''):h.update(chunk)
        CACHE[path]=h.hexdigest()
    return CACHE[path]


def read(name):return json.loads((BASE/name).read_text())


def main():
    a=read('analysis.json'); b=read('independent_check.json');m=read('manifest.json')
    assert a['verdict']['all_16_runs_valid'] and not a['issues'] and b['status']=='passed'
    assert read('manifest_frozen.json')==m
    assert sha(BASE/'inputs.npz')==m['inputs_sha256']==a['provenance']['inputs_sha256']
    for path,digest in m['source_hashes'].items():assert sha(ROOT/path)==digest,path
    assert sha(STUDY/'EXPERIMENT_PLAN.md')==m['plan_sha256']
    for path,digest in read('analysis_frozen.json')['source_hashes'].items():assert sha(ROOT/path)==digest
    assert sha(STUDY/'ANALYSIS.py')==a['provenance']['analysis_source_sha256']
    assert sha(STUDY/'CHECK.py')==b['source_sha256']==read('raw_check_frozen.json')['sha256']
    for path,digest in b['inputs_and_outputs_sha256'].items():assert sha(BASE/path)==digest,path
    input_hash=sha(BASE/'inputs.npz');manifest_hash=sha(BASE/'manifest.json')
    for family in ('network','closure'):
        for c in m[family+'_runs']:
            folder=BASE/family/c['name'];r=json.loads((folder/'record.json').read_text())
            assert r['config']==c and r['status'] in ('success','complete')
            if family=='closure':
                assert r['inputs_sha256']==input_hash and r['manifest_sha256']==manifest_hash
                assert r['observation_count']==201 and r['last_observed_time']==100
            else:
                assert r['input_hashes'][str(BASE/'inputs.npz')]==input_hash
                assert r['input_hashes'][str(BASE/'manifest.json')]==manifest_hash
                assert r['counts']['observations']==201 and r['last_time']==100
            assert r.get('steps_completed',r.get('counts',{}).get('steps'))==round(100/c['step'])
            for path,digest in r['source_hashes'].items():assert sha(ROOT/path)==digest,path
            main_report=a['runs'][family+'/'+c['name']]
            assert main_report['valid']
            for path,digest in main_report['hashes'].items():assert sha(folder/path)==digest
    differences=[]
    def compare(x,y):
        x,y=np.asarray(x),np.asarray(y)
        assert x.shape==y.shape
        errors=np.abs(x-y).ravel();differences.extend(errors.tolist())
        assert np.isfinite(errors).all() and np.max(errors,initial=0)<5e-12
    for width,values in b['network_mean_loss'].items():compare(values,a['width_means'][width]['loss'])
    for name,values in b['closure_loss'].items():compare(values,a['runs']['closure/'+name]['curves']['loss'])
    for r in b['gram_errors']:
        v=a['comparisons'][f"closure/{r['closure']}:width{r['width']}"]['comparison']['panels'][r['panel']][r['observable']][f"layer{r['layer']}"]
        compare(r['curve'],v['curve']);compare(r['maximum'],v['maximum']['value']);compare(r['terminal'],v['curve'][-1])
    for r in b['frozen_gram']:
        v=a['width_means'][str(r['width'])]['frozen_gram_baseline']['panels'][r['panel']]['G'][f"layer{r['layer']}"]
        compare(r['curve'],v['curve']);compare(r['maximum'],v['maximum']['value']);compare(r['terminal'],v['curve'][-1])
    for name,values in b['frozen_readout_loss'].items():
        if name.endswith('_mean'):v=a['width_means'][name.split('_')[0][1:]]['frozen_readout_mean_loss']
        else:v=a['runs']['network/'+name]['frozen_readout']['loss']
        compare(values,v)
    for r in b['controls']:
        v=next(v for v in a['controls'].values() if [s.split('/')[1] for s in v['members']]==[r['left'],r['right']])
        compare(r['maxima']['loss'],v['maxima']['loss'])
        for p in ('training','circle'):
            for q in ('G','DeltaG'):
                for l in (1,2):compare(r['maxima'][f'{p}_{q}{l}'],v['maxima'][f'{p}.{q}.layer{l}'])
        assert r['passed']==v['pass']
    plots=read('plots_manifest.json')
    assert plots['plot_source_sha256']==sha(STUDY/'PLOTS.py')
    assert plots['analysis_sha256']==sha(BASE/'analysis.json')
    assert plots['inputs_sha256']==input_hash
    for path,digest in plots['outputs'].items():assert sha(BASE/path)==digest
    supervisor=read('supervisor.json')
    assert supervisor['status']=='complete' and len(supervisor['workers'])==16
    assert all(r['exit_code']==0 and r['wall_seconds']<600 for r in supervisor['workers'])
    assert supervisor['scientific_wall_seconds']<1200
    assert read('progress.json')['active']==[]
    total_bytes=sum(p.stat().st_size for p in BASE.parent.rglob('*') if p.is_file())
    free=shutil.disk_usage(BASE).free
    assert total_bytes<8*1024**3 and free>3*1024**3
    assert all(p.is_file() for p in STUDY.iterdir()),'Study must remain flat'
    link_count=0
    for name in ('README.md','REPORT.md'):
        for target in re.findall(r'\]\(([^)]+)\)',(STUDY/name).read_text()):
            if '://' not in target:
                path=(STUDY/target.split('#')[0]).resolve()
                assert path.exists() or path==BASE/'final_verification.json',str(path)
                link_count+=1
    result={'status':'passed','source_sha256':sha(__file__),'command':getattr(sys,'orig_argv',sys.argv),
            'runs_validated':16,'statistics_compared':len(differences),'maximum_arithmetic_difference':max(differences),
            'frozen_readout_independent_method':'matrix exponential versus eigendecomposition',
            'all_output_and_checkpoint_hashes_validated':True,'frozen_producer_count':len(m['source_hashes']),
            'plan_sha256':m['plan_sha256'],'inputs_sha256':input_hash,'analysis_sha256':sha(BASE/'analysis.json'),
            'independent_check_sha256':sha(BASE/'independent_check.json'),'plot_files':len(plots['outputs']),
            'report_sha256':sha(STUDY/'REPORT.md'),'readme_sha256':sha(STUDY/'README.md'),
            'local_links_checked':link_count,'study_is_flat':True,'science_seconds':supervisor['scientific_wall_seconds'],
            'generated_bytes':total_bytes,'disk_free_bytes':free,'all_numerical_controls_pass':False,
            'unresolved_axes':a['verdict']['unresolved_axes'],'interpretation':'Internal artifact and arithmetic checks; closure quadrature unresolved.'}
    with (BASE/'final_verification.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
