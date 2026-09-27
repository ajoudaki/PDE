"""Read-only independent audit of saved selective-geometry campaign results.

No model integration, compilation, pickle loading, or source/result mutation.
Only this audit's JSON products are written in its assigned checks directory.
"""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import time
import numpy as np

STUDY=Path(__file__).resolve().parent
ROOT=STUDY.parent.parent
CAMPAIGN=ROOT/'data/generated/structured_full_rank_scalar_20260926/selective_geometry_20260927'

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def rms(a):return float(np.sqrt(np.mean(np.asarray(a)**2)))
def load(path):return json.loads(Path(path).read_text())
def finite_arrays(data):
    return {k:bool(np.all(np.isfinite(data[k]))) for k in data.files if np.issubdtype(data[k].dtype,np.number)}
def verify_value(checks,key,actual,reported):
    checks[key]=bool(np.allclose(actual,reported,rtol=1e-10,atol=1e-12))
def source_matches(hashes):
    return {name:(digest(STUDY/name)==expected if (STUDY/name).exists() else False) for name,expected in hashes.items()}

def audit_reference(path,task):
    meta=load(path);checks={};result={'task':task['name'],'record_file':str(path),'record_sha256':digest(path),'stop_reason':meta.get('stop_reason'),'recorded_fitted':meta.get('fitted')}
    if not meta.get('data_file'):
        checks['unstarted_is_not_fitted']=not meta.get('fitted',False)
        return {**result,'status':'no_checkpoint','checks':checks,'passed':all(checks.values())}
    data_path=path.parent/meta['data_file'];checks['data_hash']=data_path.exists() and digest(data_path)==meta.get('data_sha256')
    if not data_path.exists():return {**result,'status':'missing_checkpoint','checks':checks,'passed':False}
    with np.load(data_path,allow_pickle=False) as data:
        finite=finite_arrays(data);checks['all_numeric_arrays_finite']=all(finite.values())
        checks['circle_shape']=data['angles'].shape==(256,) and data['prediction'].shape==(256,)
        checks['circle_grid']=np.allclose(data['angles'],2*np.pi*np.arange(256)/256,rtol=0,atol=1e-14)
        checks['labels_match_frozen_task']=np.allclose(data['train_labels'],task['labels'],rtol=0,atol=1e-14)
        checks['train_angles_match_frozen_task']=np.allclose(data['train_angles'],task['angles'],rtol=0,atol=1e-14)
        mse=float(np.mean((data['train_prediction']-data['train_labels'])**2));verify_value(checks,'train_mse',mse,meta['train_mse'])
        fitted=meta.get('stop_reason')=='target' and mse<=.01*(1+1e-7)
        checks['fit_status']=fitted==bool(meta.get('fitted'))
        result.update(recomputed_train_mse=mse,recomputed_fitted=fitted,numeric_array_finiteness=finite)
    manifest=path.parent/('manifest_'+meta['tag']+'.json')
    checks['manifest_hash']=manifest.exists() and digest(manifest)==meta['source_manifest_sha256']
    result.update(status='fitted' if result['recomputed_fitted'] else 'partial',checks=checks,passed=all(checks.values()))
    return result

def compare_reference(path,task,angles,prediction,core,aliases,candidate_fitted,recorded):
    if not path.exists():return {'status':'pending_reference'}
    meta=load(path)
    if not meta.get('data_file'):return {'status':'reference_without_checkpoint','fitted_pair':False}
    checkpoint=path.parent/meta['data_file'];checks={}
    if not checkpoint.exists():return {'status':'missing_reference_checkpoint','fitted_pair':False}
    with np.load(checkpoint,allow_pickle=False) as data:
        # Derive each reference index by angle, independently of recorded indices.
        separation=np.abs(np.angle(np.exp(1j*(angles[:,None]-data['angles'][None,:]))))
        indices=np.argmin(separation,axis=1)
        checks['exact_distinct_circle_angles']=len(set(map(int,indices)))==64 and float(np.max(separation[np.arange(64),indices]))<1e-13
        reference=data['prediction'][indices];difference=prediction-reference
        error=rms(difference);grid_change=abs(error-rms(difference[::2]))
        train_error=rms(core-data['train_prediction']);passive_error=rms(aliases-data['train_prediction'])
        ref_mse=float(np.mean((data['train_prediction']-data['train_labels'])**2))
        ref_fitted=meta.get('stop_reason')=='target' and ref_mse<=.01*(1+1e-7)
        checks['labels_match']=np.allclose(data['train_labels'],task['labels'],rtol=0,atol=1e-14)
    fitted_pair=bool(candidate_fitted and ref_fitted)
    if recorded.get('status')=='available':
        for key,value in [('raw_circle_rms',error),('circle_grid_change_64_vs_32',grid_change),('core_train_prediction_rms',train_error),('passive_train_prediction_rms',passive_error)]:verify_value(checks,key,value,recorded[key])
        checks['recorded_reference_data_hash']=recorded['data_sha256']==digest(checkpoint)
        checks['recorded_reference_metadata_hash']=recorded['metadata_sha256']==digest(path)
        checks['fitted_pair_status']=fitted_pair==bool(recorded['fitted_pair'])
        checks['recorded_reference_indices']=list(map(int,indices))==recorded['reference_circle_indices']
    return {'status':'fitted_pair' if fitted_pair else 'partial_comparison','fitted_pair':fitted_pair,'raw_circle_rms':error,'circle_grid_change_64_vs_32':grid_change,'coarse_grid_flag':grid_change>.001,'core_train_prediction_rms':train_error,'passive_train_prediction_rms':passive_error,'reference_train_mse':ref_mse,'reference_fitted':ref_fitted,'reference_indices':indices.tolist(),'checks':checks,'passed':all(checks.values())}

def audit_scalar(path,task):
    meta=load(path);checks={};result={'task':task['name'],'record_file':str(path),'record_sha256':digest(path),'stop_reason':meta.get('stop_reason'),'recorded_fitted':meta.get('fitted')}
    result['current_source_hash_matches']=source_matches(meta.get('sources',{}))
    if not meta.get('data_file'):
        checks['unstarted_is_not_fitted']=not meta.get('fitted',False)
        return {**result,'status':'no_checkpoint','checks':checks,'passed':all(checks.values())}
    checkpoint=path.parent/meta['data_file'];checks['data_hash']=checkpoint.exists() and digest(checkpoint)==meta.get('data_sha256')
    if not checkpoint.exists():return {**result,'status':'missing_checkpoint','checks':checks,'passed':False}
    with np.load(checkpoint,allow_pickle=False) as data:
        finite=finite_arrays(data);checks['all_numeric_arrays_finite']=all(finite.values());m=len(task['angles'])
        expected_angles=2*np.pi*np.arange(64)/64
        checks['circle_shape']=data['angles'].shape==(64,) and data['prediction'].shape==(64,)
        checks['circle_grid']=np.allclose(data['angles'],expected_angles,rtol=0,atol=1e-14)
        checks['full_query_shape']=data['all_query_angles'].shape==(64+m,) and data['all_passive_prediction'].shape==(64+m,)
        checks['query_split_angles']=np.allclose(data['all_query_angles'],np.r_[expected_angles,task['angles']],rtol=0,atol=1e-14)
        checks['query_split_circle_predictions']=np.array_equal(data['prediction'],data['all_passive_prediction'][:64])
        checks['query_split_alias_predictions']=np.array_equal(data['passive_train_prediction'],data['all_passive_prediction'][64:])
        checks['labels_match_frozen_task']=np.allclose(data['train_labels'],task['labels'],rtol=0,atol=1e-14)
        checks['train_angles_match_frozen_task']=np.allclose(data['train_angles'],task['angles'],rtol=0,atol=1e-14)
        core=data['train_prediction'];aliases=data['passive_train_prediction'];gap=aliases-core
        core_mse=float(np.mean((core-data['train_labels'])**2));alias_mse=float(np.mean((aliases-data['train_labels'])**2));alias_rms=rms(gap);alias_max=float(np.max(np.abs(gap)))
        for key,value in [('train_mse',core_mse),('passive_train_mse',alias_mse),('alias_gap_rms',alias_rms),('alias_gap_max',alias_max)]:verify_value(checks,key,value,meta[key])
        verify_value(checks,'recorded_core_prediction',core,meta['train_prediction']);verify_value(checks,'recorded_alias_prediction',aliases,meta['passive_train_prediction'])
        verify_value(checks,'saved_alias_gap',gap,data['alias_gap'])
        fitted=meta.get('stop_reason')=='target' and core_mse<=.01*(1+1e-7)
        checks['fit_status']=fitted==bool(meta.get('fitted'))
        checks['endpoint_classification']=meta['endpoint_status']==('fitted threshold endpoint' if fitted else 'partial endpoint')
        # Independently decode predictions from saved scalar state and index maps.
        state=data['state'];core_ids=data['core_ids'];passive_ids=data['passive_ids'];Fids=data['template_Fids'];nc=len(core_ids);npas=len(passive_ids)
        core_lookup={int(value):i for i,value in enumerate(core_ids)};passive_lookup={int(value):i for i,value in enumerate(passive_ids)}
        train_ids=np.array([core_lookup[int(v)] for v in Fids[:m]]);output_id=passive_lookup[int(Fids[-1])]
        checks['state_size']=len(state)==nc+(64+m)*npas+1
        checks['partition_indices']=len(set(map(int,core_ids))&set(map(int,passive_ids)))==0 and set(map(int,np.r_[core_ids,passive_ids]))==set(range(nc+npas))
        recomputed_core=2*state[-1]*np.clip(state[train_ids],-1,1)
        recomputed_all=2*state[-1]*np.clip(state[nc:-1].reshape(64+m,npas)[:,output_id],-1,1)
        verify_value(checks,'core_predictions_from_state',recomputed_core,core);verify_value(checks,'all_passive_predictions_from_state',recomputed_all,data['all_passive_prediction'])
        initial=data['initial_state'];initial_core=2*initial[-1]*np.clip(initial[train_ids],-1,1);initial_alias=2*initial[-1]*np.clip(initial[nc:-1].reshape(64+m,npas)[64:,output_id],-1,1)
        verify_value(checks,'initial_core_mse',float(np.mean((initial_core-data['train_labels'])**2)),meta['initial_train_mse'])
        verify_value(checks,'initial_alias_max_gap',float(np.max(np.abs(initial_alias-initial_core))),meta['initial_alias_max_gap'])
        history=data['history'];verify_value(checks,'history_last_mse',history[-1,1],core_mse)
        checks['history_time_monotone']=bool(np.all(np.diff(history[:,0])>=0))
        checks['clock_positive']=bool(state[-1]>=1.-1e-12)
        verify_value(checks,'max_q',float(np.max(np.abs(state[:-1]))),meta['final_max_abs_q'])
        result.update(recomputed_core_train_mse=core_mse,recomputed_passive_train_mse=alias_mse,recomputed_alias_rms=alias_rms,recomputed_alias_max=alias_max,alias_inconsistency_flag=alias_max>.05,recomputed_fitted=fitted,numeric_array_finiteness=finite)
        comparisons={}
        for kind,tag in [('gaussian','gaussian'),('block','block_k4_P1_canonical')]:
            comparisons[kind]=compare_reference(CAMPAIGN/'references'/f"{task['name']}__{tag}.json",task,data['angles'],data['prediction'],core,aliases,fitted,meta.get(kind+'_comparison',{}))
        result['comparisons']=comparisons
    cache=meta.get('template_cache',{});config=cache.get('configuration',{})
    fingerprint=hashlib.sha256(json.dumps(config,sort_keys=True,separators=(',',':')).encode()).hexdigest();checks['template_configuration_fingerprint']=fingerprint==cache.get('fingerprint')
    pickle_path=Path(cache.get('pickle_file',''))
    if not pickle_path.is_absolute():pickle_path=ROOT/pickle_path
    checks['template_pickle_hash']=pickle_path.exists() and digest(pickle_path)==cache.get('pickle_sha256')
    comparison_pass=all(value.get('passed',True) for value in result['comparisons'].values())
    gaussian=result['comparisons']['gaussian']
    if gaussian.get('fitted_pair'):
        err=gaussian['raw_circle_rms'];screen='coarse_accuracy' if err<=.1 else 'strong_discrepancy' if err>.3 else 'intermediate'
    else:screen='partial_or_pending_not_eligible'
    result.update(status='fitted' if fitted else 'partial',gaussian_descriptive_screen=screen,checks=checks,passed=all(checks.values()) and comparison_pass)
    return result

def audit():
    registration=load(CAMPAIGN/'references/registration_manifest.json');rows=[];reference_rows=[];errors=[]
    for task in registration['tasks']:
        for tag in ('gaussian','block_k4_P1_canonical'):
            path=CAMPAIGN/'references'/f"{task['name']}__{tag}.json"
            if path.exists():
                try:reference_rows.append(audit_reference(path,task))
                except Exception as exc:errors.append({'file':str(path),'error':repr(exc)})
        matches=list(CAMPAIGN.rglob(f"{task['name']}__selective_zero.json"))
        for path in matches:
            try:rows.append(audit_scalar(path,task))
            except Exception as exc:errors.append({'file':str(path),'error':repr(exc)})
    return {'audited_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':digest(__file__),'scope':'new selective_geometry_20260927 campaign only; saved arrays, no training','reference_registration_sha256':digest(CAMPAIGN/'references/registration_manifest.json'),'reference_current_source_hash_matches':source_matches(registration['source_hashes']),'expected_tasks':len(registration['tasks']),'scalar_records':len(rows),'reference_records':len(reference_rows),'scalar_all_tasks_recorded':len(rows)==len(registration['tasks']),'passed':not errors and all(r['passed'] for r in rows+reference_rows),'errors':errors,'scalars':rows,'references':reference_rows}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--watch',action='store_true');args=parser.parse_args()
    checks=CAMPAIGN/'checks';checks.mkdir(parents=True,exist_ok=True)
    deadline=load(CAMPAIGN/'references/registration_manifest.json')['started_unix']+720
    while True:
        result=audit();(checks/'independent_result_audit.json').write_text(json.dumps(result,indent=2)+'\n')
        summary={k:result[k] for k in ('audited_utc','scalar_records','reference_records','scalar_all_tasks_recorded','passed','errors')}
        print(json.dumps(summary),flush=True)
        if not args.watch or result['scalar_all_tasks_recorded'] or time.time()>=deadline:break
        time.sleep(30.)
