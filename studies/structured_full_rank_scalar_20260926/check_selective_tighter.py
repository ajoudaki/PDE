"""Read-only audit of tighter-threshold scalar/checkpoint continuations.

Compares saved arrays and exact resumed states. No compilation, initialization,
reference evaluation, or ODE integration occurs here.
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
BASE=ROOT/'data/generated/structured_full_rank_scalar_20260926'
NEW=BASE/'selective_tighter_20260927'
GEOMETRY=BASE/'selective_geometry_20260927'
ORDER=BASE/'selective_order_20260927'
TASKS=('pair_orthogonal_cos1','cluster_triple_cos1','triple_wide_mixed')

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())
def rms(values):return float(np.sqrt(np.mean(np.asarray(values)**2)))
def value(checks,name,a,b):checks[name]=bool(np.allclose(a,b,rtol=1e-10,atol=1e-12))
def find_source(task,depth):
    folder=GEOMETRY if depth==1 else ORDER
    suffix='__selective_zero.json' if depth==1 else '__selective_zero_out2.json'
    matches=list(folder.rglob(task+suffix))
    if len(matches)!=1:raise ValueError(f'Expected one source record for {task} depth{depth}')
    return matches[0]

def reference_comparison(task,method,angles,prediction,folder,target):
    tag='gaussian' if method=='gaussian' else 'block_k4_P1_canonical'
    path=folder/'references'/f'{task}__{tag}.json'
    if not path.exists():return {'status':'pending'}
    meta=read(path)
    if not meta.get('data_file'):return {'status':'no_reference_checkpoint','fitted':False}
    checkpoint=path.parent/meta['data_file'];checks={'data_hash':sha(checkpoint)==meta['data_sha256']}
    with np.load(checkpoint,allow_pickle=False) as data:
        separation=np.abs(np.angle(np.exp(1j*(angles[:,None]-data['angles'][None,:]))));indices=np.argmin(separation,axis=1)
        checks['same_exact_64_angles']=len(set(map(int,indices)))==64 and float(np.max(separation[np.arange(64),indices]))<1e-13
        checks['finite_predictions']=bool(np.all(np.isfinite(data['prediction'])) and np.all(np.isfinite(data['train_prediction'])))
        error=rms(prediction-data['prediction'][indices]);coarse=rms((prediction-data['prediction'][indices])[::2]);mse=float(np.mean((data['train_prediction']-data['train_labels'])**2))
        value(checks,'reported_train_mse',mse,meta['train_mse'])
    threshold=float(meta['target_mse']);checks['same_stop_target']=threshold==float(target)
    fitted=meta.get('stop_reason')=='target' and mse<=threshold*(1+1e-7)
    checks['fit_status']=fitted==bool(meta.get('fitted'))
    return {'status':'fitted' if fitted else 'partial','fitted':fitted,'raw_circle_rms':error,'circle64_vs32_rms_change':abs(error-coarse),'quadrature_flag':abs(error-coarse)>.001,'reference_train_mse':mse,'target_mse':threshold,'reference_data_sha256':sha(checkpoint),'reference_metadata_sha256':sha(path),'checks':checks,'passed':all(checks.values())}


def audit_scalar(path,task,depth):
    meta=read(path);source_path=find_source(task,depth);source_meta=read(source_path);source_checkpoint=source_path.parent/source_meta['data_file'];checks={}
    result={'task':task,'output_dependency_depth':depth,'record':str(path),'record_sha256':sha(path),'source_record':str(source_path),'source_record_sha256':sha(source_path),'source_checkpoint':str(source_checkpoint),'source_checkpoint_sha256':sha(source_checkpoint),'stop_reason':meta.get('stop_reason'),'target_mse':meta.get('target_mse')}
    result['source_matches']={name:(STUDY/name).exists() and sha(STUDY/name)==expected for name,expected in meta.get('sources',{}).items()}
    if not meta.get('data_file'):
        return {**result,'status':'no_checkpoint','fitted':False,'passed':not meta.get('fitted',False),'checks':{'not_fitted':not meta.get('fitted',False)}}
    checkpoint=path.parent/meta['data_file'];checks['data_hash']=sha(checkpoint)==meta['data_sha256']
    with np.load(checkpoint,allow_pickle=False) as data,np.load(source_checkpoint,allow_pickle=False) as original:
        checks['finite_all_saved_numeric_arrays']=all(np.all(np.isfinite(data[k])) for k in data.files if np.issubdtype(data[k].dtype,np.number))
        checks['resume_initial_state_bitwise_identical']=np.array_equal(data['initial_state'],original['state'])
        checks['unchanged_query_panel']=np.array_equal(data['all_query_angles'],original['all_query_angles'])
        checks['unchanged_core_indices']=np.array_equal(data['core_ids'],original['core_ids'])
        checks['unchanged_passive_indices']=np.array_equal(data['passive_ids'],original['passive_ids'])
        checks['unchanged_F_indices']=np.array_equal(data['template_Fids'],original['template_Fids'])
        checks['unchanged_labels']=np.array_equal(data['train_labels'],original['train_labels'])
        source_raw_sha=hashlib.sha256(np.ascontiguousarray(original['state'],dtype=np.float64).tobytes()).hexdigest()
        result['independent_resume_raw_float64_sha256']=source_raw_sha
        # Check any recorded raw-state digest inside resume provenance.
        for name,expected in meta.get('resume',{}).items():
            if isinstance(expected,str) and 'state' in name and 'sha256' in name:checks['resume_'+name]=expected==source_raw_sha
        m=len(data['train_labels']);angles=data['angles'];labels=data['train_labels'];state=data['state'];nc=len(data['core_ids']);npas=len(data['passive_ids'])
        ci={int(v):i for i,v in enumerate(data['core_ids'])};pi={int(v):i for i,v in enumerate(data['passive_ids'])};Fids=data['template_Fids']
        core=2*state[-1]*np.clip(state[[ci[int(v)] for v in Fids[:m]]],-1,1)
        passive=2*state[-1]*np.clip(state[nc:-1].reshape(64+m,npas)[:,pi[int(Fids[-1])]],-1,1)
        value(checks,'state_decodes_core',core,data['train_prediction']);value(checks,'state_decodes_passive_panel',passive,data['all_passive_prediction'])
        checks['circle_alias_split']=np.array_equal(data['prediction'],passive[:64]) and np.array_equal(data['passive_train_prediction'],passive[64:])
        value(checks,'circle_grid',angles,2*np.pi*np.arange(64)/64)
        value(checks,'appended_alias_angles',data['all_query_angles'],np.r_[angles,data['train_angles']])
        mse=float(np.mean((core-labels)**2));alias_mse=float(np.mean((passive[64:]-labels)**2));gap=passive[64:]-core
        for name,actual in [('train_mse',mse),('passive_train_mse',alias_mse),('alias_gap_rms',rms(gap)),('alias_gap_max',float(np.max(np.abs(gap))))]:value(checks,name,actual,meta[name])
        threshold=float(meta['target_mse']);fitted=meta.get('stop_reason')=='target' and mse<=threshold*(1+1e-7)
        checks['fit_status']=fitted==bool(meta.get('fitted'))
        source_time=float(source_meta['physical_time'])
        if 'source_physical_time' in meta:value(checks,'source_physical_time',meta['source_physical_time'],source_time)
        if 'elapsed_physical_time' in meta:value(checks,'absolute_time_sum',meta['physical_time'],source_time+meta['elapsed_physical_time'])
        history=data['history'];value(checks,'absolute_history_start',history[0,0],source_time);value(checks,'history_final_mse',history[-1,1],mse)
        if 'history_elapsed' in data.files:value(checks,'history_absolute_offset',history[:,0],data['history_elapsed'][:,0]+source_time)
        comparisons={};baseline_comparisons={}
        for method in ('block','gaussian'):
            compared=reference_comparison(task,method,angles,data['prediction'],NEW,threshold);comparisons[method]=compared
            baseline_comparisons[method]=reference_comparison(task,method,original['angles'],original['prediction'],GEOMETRY,.01)
            recorded=meta.get(method+'_comparison',{})
            if compared.get('raw_circle_rms') is not None and recorded.get('status')=='available':
                value(checks,method+'_reported_raw_rms',compared['raw_circle_rms'],recorded['raw_circle_rms'])
                if 'fitted_pair' in recorded:checks[method+'_fitted_pair']=bool(recorded['fitted_pair'])==bool(fitted and compared['fitted'])
        result.update(status='fitted' if fitted else 'partial',fitted=fitted,core_train_mse=mse,passive_train_mse=alias_mse,alias_rms=rms(gap),alias_max=float(np.max(np.abs(gap))),alias_inconsistency_flag=float(np.max(np.abs(gap)))>.05,scalar_count=len(state),compared_resume_scalar_entries=len(state),source_time=source_time,physical_time=meta.get('physical_time'),elapsed_physical_time=meta.get('elapsed_physical_time'),comparisons=comparisons,previous_mse01_comparisons=baseline_comparisons)
    if 'template_cache' in meta and 'template_cache' in source_meta:
        checks['same_template_pickle_hash']=meta['template_cache'].get('pickle_sha256')==source_meta['template_cache'].get('pickle_sha256')
    resume=meta.get('resume',{})
    for key,expected in resume.items():
        if 'sha256' not in key:continue
        if 'source_checkpoint' in key:checks['provenance_'+key]=expected==sha(source_checkpoint)
        elif 'source_metadata' in key:checks['provenance_'+key]=expected==sha(source_path)
        elif 'compiled_template' in key:checks['provenance_'+key]=expected==source_meta['template_cache']['pickle_sha256']
    comparison_ok=all(c.get('passed',True) for c in result['comparisons'].values()) and all(c.get('passed',True) for c in result['previous_mse01_comparisons'].values())
    result.update(checks=checks,passed=all(checks.values()) and comparison_ok)
    return result



def audit_reference(path):
    meta=read(path);source=Path(meta['source_checkpoint']);source_meta=read(source.with_suffix('.json'));checks={}
    checks['source_checkpoint_hash']=sha(source)==meta['source_checkpoint_sha256']
    checks['source_report_hash']=sha(source.with_suffix('.json'))==meta['source_report_sha256']
    checks['source_manifest_hash']=meta['source_manifest_sha256']==source_meta['source_manifest_sha256']
    checks['new_manifest_hash']=sha(path.parent/'manifest.json')==meta['source_manifest_current_sha256']
    checks['initialization_not_called']=meta['initialization_called'] is False
    checkpoint=path.parent/meta['data_file'];checks['data_hash']=sha(checkpoint)==meta['data_sha256']
    with np.load(source,allow_pickle=False) as old,np.load(checkpoint,allow_pickle=False) as data:
        checks['finite_numeric_arrays']=all(np.all(np.isfinite(data[k])) for k in data.files if np.issubdtype(data[k].dtype,np.number))
        for key,expected in meta['start_state_array_sha256'].items():
            actual=hashlib.sha256(np.ascontiguousarray(old[key]).tobytes()).hexdigest()
            checks['resume_hash_'+key]=actual==expected
            checks['resume_shape_'+key]=list(old[key].shape)==meta['start_state_array_shapes'][key]
        for key,expected in meta['final_state_array_sha256'].items():
            checks['final_array_hash_'+key]=hashlib.sha256(np.ascontiguousarray(data[key]).tobytes()).hexdigest()==expected
        checks['same_labels']=np.array_equal(data['train_labels'],old['train_labels'])
        checks['same_circle_queries']=np.array_equal(data['angles'],old['angles'])
        if 'vector' in data.files:
            checks['same_static_G']=np.array_equal(data['G'],old['G'])
            checks['same_layout']=np.array_equal(data['layout'],old['layout'])
            value(checks,'resumed_clock',old['vector'][-1],meta['continuation_start_L'])
        if 'history' in old.files:checks['history_preserves_prior_prefix']=np.array_equal(data['history'][:len(old['history'])],old['history'])
        mse=float(np.mean((data['train_prediction']-data['train_labels'])**2));value(checks,'train_mse',mse,meta['train_mse'])
        value(checks,'source_time',source_meta['physical_time'],meta['continuation_start_time'])
        value(checks,'absolute_time',meta['physical_time'],meta['continuation_start_time']+meta['continuation_elapsed_time'])
        fitted=meta['stop_reason']=='target' and mse<=float(meta['target_mse'])*(1+1e-7)
        checks['fitted_status']=fitted==bool(meta['fitted'])
    return {'task':meta['task'],'tag':meta['tag'],'target_mse':meta['target_mse'],'fitted':fitted,'recomputed_train_mse':mse,'resume_arrays':list(meta['start_state_array_sha256']),'checks':checks,'passed':all(checks.values())}


def audit():
    rows=[];errors=[];reference_rows=[]
    for task in TASKS:
        for tag in ("gaussian","block_k4_P1_canonical"):
            ref_path=NEW/"references"/f"{task}__{tag}.json"
            if ref_path.exists():
                try:reference_rows.append(audit_reference(ref_path))
                except Exception as exc:errors.append({"reference":str(ref_path),"error":repr(exc)})
    for task in TASKS:
        for depth in (1,2):
            paths=list(NEW.rglob(f'{task}__selective_zero_out{depth}.json'))
            if not paths:continue
            if len(paths)!=1:errors.append({'task':task,'depth':depth,'record_count':len(paths)});continue
            try:rows.append(audit_scalar(paths[0],task,depth))
            except Exception as exc:errors.append({'task':task,'depth':depth,'error':repr(exc)})
    comparisons=[]
    for task in TASKS:
        pair={r['output_dependency_depth']:r for r in rows if r['task']==task}
        if set(pair)!={1,2} or not all(r.get('comparisons',{}).get('block',{}).get('raw_circle_rms') is not None for r in pair.values()):continue
        a,b=pair[1],pair[2];old=a['comparisons']['block']['raw_circle_rms'];new=b['comparisons']['block']['raw_circle_rms'];fraction=(old-new)/old if old else None
        eligible=all(r['fitted'] and r['comparisons']['block']['fitted'] for r in (a,b));same_target=a['target_mse']==b['target_mse']
        previous1=a['previous_mse01_comparisons']['block']['raw_circle_rms'];previous2=b['previous_mse01_comparisons']['block']['raw_circle_rms']
        comparisons.append({'task':task,'target_mse':a['target_mse'],'same_target':same_target,'fitted_primary_pair':eligible and same_target,'q1_raw_block_rms':old,'q2_raw_block_rms':new,'q2_fractional_reduction_vs_q1':fraction,'previous_mse01_q1_block_rms':previous1,'previous_mse01_q2_block_rms':previous2,'previous_mse01_q2_fractional_reduction_vs_q1':(previous1-previous2)/previous1,'classification':'partial_comparison' if not eligible or not same_target else 'q2_improves_at_least_5percent' if fraction>=.05 else 'q2_worsens_at_least_5percent' if fraction<=-.05 else 'change_below_5percent'})
    return {'audited_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(__file__),'scope':'Saved scalar and reference continuations only; exact checkpoint resume and same-target comparisons; no ODE work','scalar_records':len(rows),'reference_records':len(reference_rows),'complete':len(rows)==6 and len(reference_rows)==6,'passed':not errors and all(r['passed'] for r in rows+reference_rows) and all(r['same_target'] for r in comparisons),'errors':errors,'results':rows,'reference_results':reference_rows,'order_comparisons':comparisons}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--watch',action='store_true');parser.add_argument('--deadline',type=float,default=time.time()+720);args=parser.parse_args()
    output=NEW/'checks';output.mkdir(parents=True,exist_ok=True)
    while True:
        result=audit();(output/'independent_tighter_audit.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({k:result[k] for k in ('audited_utc','scalar_records','complete','passed','errors')}),flush=True)
        if not args.watch or result['complete'] or time.time()>=args.deadline:break
        time.sleep(30.)
