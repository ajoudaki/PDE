"""Independent saved-state reconstruction. Never imports the producer engine."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
import numpy as np
import torch

ROOT=Path(__file__).resolve().parents[2]
GEN=ROOT/'data/generated/neural_response_memory_20260922'
OUT=GEN/'factor_audit01'

def digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(8*1024*1024),b''):
            h.update(block)
    return h.hexdigest()

def array_hash(x):
    return hashlib.sha256(np.ascontiguousarray(x).tobytes()).hexdigest()

def rms(x):
    return float(np.sqrt(np.mean(np.square(x))))

def arrays_path(path):
    return (ROOT/path).with_name('arrays.npz')

def load_panel(path):
    with np.load(path,allow_pickle=False) as z:
        return {k:z[k] for k in ('endpoint_angles','endpoint_inputs','endpoint_prediction')}

def compare_analysis(result, analysis_path):
    """Compare the analyzer with independently replayed and scored arrays."""
    analysis=json.loads(analysis_path.read_text())
    discrepancies=[]
    rows={(r['case'],r['P'],r['seed'],r['level']):r for r in result['rows']}
    pairs={(r['case'],r['P'],r['seed']):r for r in result['pairs']}
    clos={(r['case'],r['P']):r for r in result['closure_comparisons']}
    def same(label,a,b):
        if a is None or b is None:
            okay=a is None and b is None
        elif isinstance(a,bool) or isinstance(b,bool):
            okay=a==b
        else:
            okay=bool(np.isclose(a,b,rtol=2e-11,atol=2e-13))
        if not okay:discrepancies.append({'label':label,'independent':a,'analyzer':b})
    for published in analysis['factor_all_levels']:
        key=(published['case'],published['P'],published['factor_seed'],published['level'])
        raw=rows.get(key)
        if raw is None:
            discrepancies.append({'label':str(key),'issue':'analyzer row missing from replay'})
            continue
        same(str(key)+' physical MSE',raw['loss'],published['physical_training_mse'])
        if raw['status']=='fitted':
            same(str(key)+' circle RMS',raw['circle_rms'],published['circle_rms'])
            same(str(key)+' nested difference',raw['nested_difference'],published['nested_grid_rms_difference'])
            same(str(key)+' archival RMS',raw['archival_circle_rms'],published['archival_target_circle_rms'])
        else:
            same(str(key)+' unavailable endpoint',None,published['circle_rms'])
            same(str(key)+' terminal diagnostic',raw['circle_rms'],published['terminal_function_metrics']['circle_rms'])
    for published in analysis['closure_selected']:
        key=(published['case'],published['P']);raw=clos[key]
        for own,other in [('circle_rms','circle_rms'),('nested_difference','nested_grid_rms_difference'),
                          ('refinement_rms','endpoint_refinement_rms'),('refinement_max','endpoint_refinement_max')]:
            same(str(key)+' closure '+own,raw[own],published[other])
    for case,published in analysis['dense_references'].items():
        same(case+' dense refinement RMS',result['dense_refinement'][case]['rms'],published['endpoint_refinement_rms'])
        same(case+' dense refinement max',result['dense_refinement'][case]['max'],published['endpoint_refinement_max'])
    for published in analysis['factor_selected']:
        key=(published['case'],published['P'],published['factor_seed']);raw=pairs[key]
        same(str(key)+' selected level',raw['selected_level'],published['level'])
        same(str(key)+' validity',raw['valid'],published['valid'])
        if 'factor_refinement_rms_latest' in raw:
            same(str(key)+' refinement RMS',raw['factor_refinement_rms_latest'],published['endpoint_refinement_rms'])
            same(str(key)+' refinement max',raw['factor_refinement_max_latest'],published['endpoint_refinement_max'])
    for published in analysis['paired_comparisons']:
        for factor,comparison in zip(published['factors'],published['comparisons']):
            key=(published['case'],published['P'],factor['factor_seed']);raw=pairs.get(key)
            if raw is None:continue
            same(str(key)+' direction resolved',raw['resolved_latest'],comparison['directional_difference_resolved'])
            if factor['circle_rms'] is not None and 'gap' in raw:
                same(str(key)+' score gap',raw['gap'],comparison['factor_minus_closure_rms'])
                same(str(key)+' ratio',raw['factor_to_closure_ratio'],comparison['factor_to_closure_rms_ratio'])
                same(str(key)+' sensitivity',raw['combined_sensitivity_latest'],comparison['numerical_sensitivity_max'])
                substantial=bool(raw['resolved_latest'] and (raw['factor_to_closure_ratio']>=2 or raw['factor_to_closure_ratio']<=.5))
                same(str(key)+' substantial',substantial,comparison['substantial_difference'])
    expected={(case,P,seed,level) for case in result['dense_refinement'] for P in (1,3,7)
              for seed in (20260924,20260925) for level in (0,1)}
    missing=sorted(expected-set(rows))
    reported_missing=sorted((r['case'],r['P'],r['factor_seed'],r['level']) for r in analysis['missing_primary_trajectories'])
    if missing!=reported_missing:discrepancies.append({'label':'missing primary trajectories','independent':missing,'analyzer':reported_missing})
    same('recorded trajectory count',len(rows),analysis['integration_budget']['recorded_trajectories'])
    same('integration seconds',sum(r['integration_seconds'] for r in rows.values()),analysis['integration_budget']['integration_seconds'])
    return {'status':'PASS' if not discrepancies else 'DISCREPANCIES',
            'analysis_sha256':digest(analysis_path),'discrepancies':discrepancies,
            'missing_primary_trajectories':missing}

@torch.no_grad()
def reconstruct(w,c,A,B,W0,U,device):
    cast=lambda a:torch.as_tensor(a,dtype=torch.float64,device=device)
    w,c,A,B=map(cast,(w,c,A,B))
    output=[]
    # Row-oriented forward pass is independent of engine.apply_hidden/predict.
    for start in range(0,len(U),384):
        first=torch.tanh(cast(U[start:start+384])@w.T)
        second=torch.tanh(first@W0.T+(first@B.T)@A.T)
        output.append((second@c/len(c)).cpu().numpy())
    return np.concatenate(output)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--device',required=True)
    parser.add_argument('--limit',type=int,default=None,help='Smoke check only this many completed cells')
    parser.add_argument('--compare-analysis',action='store_true',help='Require current analyzer outputs to match independent checks')
    args=parser.parse_args()
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32=False
    started=time.monotonic()
    frozen=json.loads((GEN/'analysis01/metrics.json').read_text())
    target_panels={};dense_change={};source_hashes={};closure={}
    for case,old in frozen['dense_references'].items():
        fresh=frozen['fresh_dense_references'].get(case)
        selected=arrays_path(fresh['selected_source']) if fresh else ROOT/old['selected_archive']
        previous=arrays_path(fresh['previous_source']) if fresh else ROOT/old['coarser_archive']
        p,q=load_panel(selected),load_panel(previous)
        assert np.array_equal(p['endpoint_angles'],q['endpoint_angles'])
        assert p['endpoint_angles'].shape==(8192,)
        assert np.allclose(p['endpoint_angles'],np.arange(8192)*(2*np.pi/8192),rtol=0,atol=2e-14)
        assert np.allclose(p['endpoint_inputs'],np.column_stack((np.cos(p['endpoint_angles']),np.sin(p['endpoint_angles']))),rtol=0,atol=2e-14)
        target_panels[case]=p
        dense_change[case]={'rms':rms(p['endpoint_prediction']-q['endpoint_prediction']),
                            'max':float(np.max(np.abs(p['endpoint_prediction']-q['endpoint_prediction'])))}
        for path in (selected,previous): source_hashes[str(path.relative_to(ROOT))]=digest(path)
    for row in frozen['selected']:
        path=arrays_path(row['source']);previous=arrays_path(row['previous_level_source'])
        p,q=load_panel(path),load_panel(previous);ref=target_panels[row['case']]
        assert np.array_equal(p['endpoint_angles'],ref['endpoint_angles'])
        assert array_hash(p['endpoint_prediction'])==row['endpoint_prediction_sha256']
        delta=p['endpoint_prediction']-ref['endpoint_prediction']
        closure[(row['case'],row['P'])]={'circle_rms':rms(delta),'nested_difference':abs(rms(delta)-rms(delta[::2])),
          'refinement_rms':rms(p['endpoint_prediction']-q['endpoint_prediction']),
          'refinement_max':float(np.max(np.abs(p['endpoint_prediction']-q['endpoint_prediction'])))}
        for pth in (path,previous): source_hashes[str(pth.relative_to(ROOT))]=digest(pth)
    n=2048;rng=np.random.default_rng(20260920)
    w0=rng.standard_normal((n,2));W0=rng.standard_normal((n,n))/np.sqrt(n);c0=rng.standard_normal(n)/n
    W0_device=torch.as_tensor(W0,device=args.device,dtype=torch.float64)
    rows=[];predictions={};groups={};issues=[];archive_checks={}
    cache_root=OUT/'cells';cache_root.mkdir(exist_ok=True)
    current_source_hashes={name:digest(ROOT/'studies/neural_response_memory_20260922'/name)
                          for name in ('factor_control_engine.py','run_factor_control.py','test_factor_control.py','FACTOR_CONTROL_PROTOCOL.md')}
    replay_script_sha=digest(__file__)
    summaries=sorted((GEN/'factor_control01').glob('*_factor_P*_seed*_level*/summary.json'))
    if args.limit is not None:summaries=summaries[:args.limit]
    for summary_path in summaries:
        path=summary_path.with_name('arrays.npz');config_path=summary_path.with_name('config.json')
        summary=json.loads(summary_path.read_text());config=json.loads(config_path.read_text())
        ident=(config['case'],config['P'],config['factor_seed'],config['level'])
        archival_path=ROOT/config['reference']
        if config['reference'] not in archive_checks:
            with np.load(archival_path,allow_pickle=False) as archived:
                archive_checks[config['reference']]={
                    'sha256':digest(archival_path),
                    'initial_w_equal':bool(np.array_equal(archived['w'][0],w0)),
                    'initial_c_equal':bool(np.array_equal(archived['c'][0],c0)),
                    'initial_W0_equal':bool(np.array_equal(archived['M'][0],W0)),
                    'inputs_hash':array_hash(archived['training_inputs']),
                    'labels_hash':array_hash(archived['labels']),
                    'endpoint_hash':array_hash(archived['endpoint_prediction'])}
            source_hashes[config['reference']]=archive_checks[config['reference']]['sha256']
        fingerprint={'archive_sha256':digest(path),'config_sha256':digest(config_path),
                     'summary_sha256':digest(summary_path),'current_source_sha256':current_source_hashes,
                     'replay_script_sha256':replay_script_sha,
                     'target_prediction_sha256':array_hash(target_panels[ident[0]]['endpoint_prediction']),
                     'archival_reference_sha256':archive_checks[config['reference']]['sha256']}
        cache_path=cache_root/(summary_path.parent.name+'.json')
        pred_path=cache_root/(summary_path.parent.name+'.npy')
        cached=json.loads(cache_path.read_text()) if cache_path.exists() and pred_path.exists() else None
        if cached and cached['fingerprint']==fingerprint:
            row=cached['row'];predictions[ident]=np.load(pred_path,allow_pickle=False)
            if not row['own_endpoint_gates']:issues.append({'cell':ident,'issue':'independent endpoint gate failure'})
            for check in ('source_hash_agreement','array_hash_agreement','archival_hash_agreement','archival_input_agreement','archival_prediction_agreement'):
                if not row[check]:issues.append({'cell':ident,'issue':check+' failed'})
            rows.append(row);groups.setdefault(ident[:3],[]).append(row)
            source_hashes[str(path.relative_to(ROOT))]=fingerprint['archive_sha256']
            source_hashes[str(config_path.relative_to(ROOT))]=fingerprint['config_sha256']
            source_hashes[str(summary_path.relative_to(ROOT))]=fingerprint['summary_sha256']
            print(json.dumps({'cell':ident,'cached_after_hash_validation':True}),flush=True)
            continue
        with np.load(path,allow_pickle=False) as z:
            w,c,A,B,U,y=[z[k] for k in ('w','c','A','B','training_inputs','labels')]
            panel=z['endpoint_inputs'];stored=z['endpoint_prediction'];angles=z['endpoint_angles']
            predictions[ident]=reconstruct(w,c,A,B,W0_device,panel,args.device)
            train=reconstruct(w,c,A,B,W0_device,U,args.device)
            pred=predictions[ident];ref=target_panels[ident[0]]
            rank=config['rank'];initB=np.random.default_rng(ident[2]).standard_normal((rank,n))/np.sqrt(rank)
            expected={'w':w0,'c':c0,'W0':W0,'A':np.zeros((n,rank)),'B':initB}
            init_hashes={key:array_hash(value)==config['initial_array_sha256'][key] for key,value in expected.items()}
            finite=all(np.all(np.isfinite(a)) for a in (w,c,A,B))
            loss=float(np.mean((train-y)**2));delta=pred-ref['endpoint_prediction']
            row={'case':ident[0],'P':ident[1],'seed':ident[2],'level':ident[3],
                 'source':str(path.relative_to(ROOT)),'state_finite':bool(finite),'initial_hashes':init_hashes,
                 'status':summary['status'],'rank':rank,
                 'prediction_reconstruction_max':float(np.max(np.abs(pred-stored))),
                 'training_prediction_reconstruction_max':float(np.max(np.abs(train-z['training_prediction']))),
                 'loss':loss,'loss_difference_from_summary':abs(loss-summary['endpoint_loss_recomputed']),
                 'circle_rms':rms(delta),'nested_difference':abs(rms(delta)-rms(delta[::2])),
                 'archival_circle_rms':rms(pred-z['reference_endpoint_prediction']),
                 'exact_common_grid':bool(np.array_equal(angles,ref['endpoint_angles']) and np.array_equal(panel,ref['endpoint_inputs'])),
                 'trace_last_loss':float(z['losses'][-1]),'trace_previous_loss':float(z['losses'][-2]) if len(z['losses'])>1 else None,
                 'trace_loss_increases':int(np.count_nonzero(np.diff(z['losses'])>1e-10)),
                 'accepted_error_max':float(np.max(z['local_error_ratios'])) if len(z['local_error_ratios']) else None,
                 'accepted_step_max':float(np.max(z['accepted_steps'])) if len(z['accepted_steps']) else None,
                 'accepted_steps':len(z['accepted_steps']),
                 'source_hash_agreement':all(digest(ROOT/'studies/neural_response_memory_20260922'/name)==value
                      for name,value in config['source_sha256'].items() if name in ('factor_control_engine.py','run_factor_control.py','test_factor_control.py','FACTOR_CONTROL_PROTOCOL.md')),
                 'array_hash_agreement':digest(path)==summary['arrays_sha256'],
                 'archival_hash_agreement':config['reference_sha256']==archive_checks[config['reference']]['sha256'],
                 'archival_input_agreement':array_hash(U)==archive_checks[config['reference']]['inputs_hash']
                      and array_hash(y)==archive_checks[config['reference']]['labels_hash'],
                 'archival_prediction_agreement':array_hash(z['reference_endpoint_prediction'])==archive_checks[config['reference']]['endpoint_hash'],
                 'integration_seconds':summary['integration_seconds']}
            row['own_endpoint_gates']=bool(finite and all(init_hashes.values()) and summary['status']=='fitted'
                 and abs(loss/.001-1)<=.01 and row['nested_difference']<=1e-5 and row['exact_common_grid']
                 and row['prediction_reconstruction_max']<1e-10 and row['trace_previous_loss'] is not None
                 and row['trace_previous_loss']>.001 and row['trace_last_loss']<=.001
                 and row['accepted_error_max'] is not None and row['accepted_error_max']<=1)
            if not row['own_endpoint_gates']:issues.append({'cell':ident,'issue':'independent endpoint gate failure'})
            for check in ('source_hash_agreement','array_hash_agreement','archival_hash_agreement','archival_input_agreement','archival_prediction_agreement'):
                if not row[check]:issues.append({'cell':ident,'issue':check+' failed'})
        np.save(pred_path,predictions[ident],allow_pickle=False)
        cache_path.write_text(json.dumps({'fingerprint':fingerprint,'row':row},indent=2)+'\n')
        rows.append(row);groups.setdefault(ident[:3],[]).append(row)
        source_hashes[str(path.relative_to(ROOT))]=digest(path)
        source_hashes[str(config_path.relative_to(ROOT))]=digest(config_path)
        source_hashes[str(summary_path.relative_to(ROOT))]=digest(summary_path)
        print(json.dumps({'cell':ident,'reconstruction_max':row['prediction_reconstruction_max'],'loss':loss}),flush=True)
    pairs=[]
    for key,levels in sorted(groups.items()):
        levels.sort(key=lambda x:x['level']);selected=levels[-1]
        if len(levels)<2:
            pairs.append({'case':key[0],'P':key[1],'seed':key[2],'selected_level':selected['level'],
                          'factor_rms':selected['circle_rms'],'valid':False,
                          'resolved_latest':False,'issue':'missing refinement'})
            continue
        differences=[predictions[(*key,b['level'])]-predictions[(*key,a['level'])] for a,b in zip(levels,levels[1:])]
        sensitivities=[rms(d) for d in differences];last_max=float(np.max(np.abs(differences[-1])))
        close=closure[key[:2]];dense=dense_change[key[0]]
        latest_scale=max(sensitivities[-1],close['refinement_rms'],dense['rms'])
        all_factor_scale=max(*sensitivities,close['refinement_rms'],dense['rms'])
        gap=selected['circle_rms']-close['circle_rms'];ratio=selected['circle_rms']/close['circle_rms']
        valid=bool(selected['own_endpoint_gates'] and levels[-2]['own_endpoint_gates']
                   and {0,1}.issubset({x['level'] for x in levels}) and last_max<=.01)
        pair={'case':key[0],'P':key[1],'seed':key[2],'selected_level':selected['level'],
              'factor_rms':selected['circle_rms'],'closure_rms':close['circle_rms'],'factor_to_closure_ratio':ratio,
              'factor_refinement_rms_latest':sensitivities[-1],'factor_refinement_rms_all':sensitivities,
              'factor_refinement_max_latest':last_max,'combined_sensitivity_latest':latest_scale,
              'combined_sensitivity_all_factor_changes':all_factor_scale,'gap':gap,
              'valid':valid,'resolved_latest':bool(valid and abs(gap)>3*latest_scale),
              'resolved_all_factor_changes':bool(valid and abs(gap)>3*all_factor_scale)}
        pairs.append(pair)
    protocol_checks=[];cap_overheads=[]
    for summary_path in summaries:
        config=json.loads(summary_path.with_name('config.json').read_text());summary=json.loads(summary_path.read_text())
        samples=4 if config['case']=='equal_mixed_odd' else 8
        expected_config={'width':2048,'input_dimension':2,'network_seed':20260920,'dtype':'float64',
            'rank':config['P']*samples,'sample_count':samples,'original_sample_count':8,
            'rtol':6.25e-5/4**config['level'],'atol':6.25e-7/4**config['level'],
            'threshold':.001,'initial_step':.05,'max_step':2.,'min_step':1e-7,
            'max_time':10000.,'max_steps':30000,'crossing_bisections':32,
            'mobilities':{'w':2048,'c':2048,'A':1,'B':1}}
        bad=[key for key,value in expected_config.items() if config[key]!=value]
        if not 0<config['run_seconds']<=240:bad.append('run_seconds')
        if bad:protocol_checks.append({'cell':summary_path.parent.name,'incorrect_config_fields':bad})
        if summary['integration_seconds']>config['run_seconds']:
            cap_overheads.append({'cell':summary_path.parent.name,'status':summary['status'],
                 'nominal_cap_seconds':config['run_seconds'],'integration_seconds':summary['integration_seconds'],
                 'excess_seconds':summary['integration_seconds']-config['run_seconds']})
    budget={'recorded_trajectories':len(rows),'primary_trajectories':sum(r['level']<2 for r in rows),
            'level2_trajectories':sum(r['level']==2 for r in rows),
            'integration_seconds':sum(r['integration_seconds'] for r in rows)}
    budget['within_cumulative_caps']=bool(budget['recorded_trajectories']<=75 and budget['primary_trajectories']<=60
            and budget['level2_trajectories']<=15 and budget['integration_seconds']<=3600)
    result={'scope':'All saved direct-factor endpoints independently replayed; moment endpoints independently scored only.',
            'device':args.device,'elapsed_seconds':time.monotonic()-started,'run_count':len(rows),
            'rows':rows,'pairs':pairs,'dense_refinement':dense_change,
            'closure_comparisons':[{'case':key[0],'P':key[1],**value} for key,value in closure.items()],
            'source_sha256':source_hashes,'archival_initialization_checks':archive_checks,'issues':issues,
            'protocol_configuration_failures':protocol_checks,'budget':budget,'wall_cap_check_overheads':cap_overheads,
            'audit_source_sha256':digest(__file__)}
    if args.compare_analysis:result['analysis_comparison']=compare_analysis(result,GEN/'factor_analysis01/metrics.json')
    (OUT/'endpoint_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'complete':True,'runs':len(rows),'elapsed_seconds':result['elapsed_seconds'],'issues':issues}),flush=True)

if __name__=='__main__':main()
