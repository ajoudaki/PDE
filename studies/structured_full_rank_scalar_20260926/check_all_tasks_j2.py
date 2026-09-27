"""Independent audit of the six selected J2 attempts and carried-forward cases.

No initialization, compilation, training, or numerical RHS evaluation. Cached
symbolic metadata is loaded only to verify state counts and declared gates.
"""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import pickle
import time
import numpy as np
from true_aggregate_ode import flatten

STUDY=Path(__file__).resolve().parent;ROOT=STUDY.parent.parent
BASE=ROOT/'data/generated/structured_full_rank_scalar_20260926'
NEW=BASE/'all_tasks_j2_20260927'
SELECTED=('pair_cos3','near_pair_sin9','cluster_triple_cos9','quartet_mixed','broad_ridge6','alternating3')
CARRIED=('pair_orthogonal_cos1','cluster_triple_cos1','triple_wide_mixed')
NOT_SELECTED=('pair_cos1','triple_cos3','triple_mixed','sharp_ridge8','alternating5','alternating9','multiscale12','quartet_broad')

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())
def rms(v):return float(np.sqrt(np.mean(np.asarray(v)**2)))
def equal(checks,key,a,b):checks[key]=bool(np.allclose(a,b,rtol=1e-10,atol=1e-12))
def resolve(path):
    p=Path(path);return p if p.is_absolute() else ROOT/p


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
        difference=prediction-data['prediction'][indices];error=rms(difference);coarse=rms(difference[::2]);mse=float(np.mean((data['train_prediction']-data['train_labels'])**2))
        equal(checks,'reported_train_mse',mse,meta['train_mse'])
    threshold=float(meta['target_mse']);checks['same_stop_target']=threshold==float(target)
    fitted=meta.get('stop_reason') in ('target','reused_target_checkpoint') and mse<=threshold*(1+1e-7)
    checks['fit_status']=fitted==bool(meta.get('fitted'))
    return {'status':'fitted' if fitted else 'partial','fitted':fitted,'raw_circle_rms':error,'circle64_vs32_rms_change':abs(error-coarse),'quadrature_flag':abs(error-coarse)>.001,'reference_train_mse':mse,'target_mse':threshold,'reference_data_sha256':sha(checkpoint),'reference_metadata_sha256':sha(path),'checks':checks,'passed':all(checks.values())}


def inspect_reference(path):
    meta=read(path);data_path=path.parent/meta['data_file'];checks={'checkpoint_hash':sha(data_path)==meta['data_sha256'],'target_mse':meta['target_mse']==.001}
    with np.load(data_path,allow_pickle=False) as data:
        checks['finite_numeric_arrays']=all(np.all(np.isfinite(data[k])) for k in data.files if np.issubdtype(data[k].dtype,np.number))
        checks['circle_shape']=data['angles'].shape==(256,) and data['prediction'].shape==(256,)
        equal(checks,'circle_grid',data['angles'],2*np.pi*np.arange(256)/256)
        mse=float(np.mean((data['train_prediction']-data['train_labels'])**2));equal(checks,'train_mse',mse,meta['train_mse'])
        fitted=meta.get('stop_reason') in ('target','reused_target_checkpoint') and mse<=.001*(1+1e-7);checks['fitted_status']=fitted==bool(meta.get('fitted'))
        if meta.get('source_checkpoint'):
            source=Path(meta['source_checkpoint']);checks['source_checkpoint_hash']=sha(source)==meta['source_checkpoint_sha256']
            with np.load(source,allow_pickle=False) as old:
                for key,expected in meta.get('start_state_array_sha256',{}).items():checks['start_array_hash_'+key]=hashlib.sha256(np.ascontiguousarray(old[key]).tobytes()).hexdigest()==expected
                if meta.get('reference_action')=='reuse':
                    keys=('w','W','c') if 'W' in data.files else ('G','vector','layout')
                    checks['reused_state_arrays_equal']=all(np.array_equal(data[k],old[k]) for k in keys)
        for key,expected in meta.get('final_state_array_sha256',{}).items():checks['final_array_hash_'+key]=hashlib.sha256(np.ascontiguousarray(data[key]).tobytes()).hexdigest()==expected
    return {'task':meta['task'],'tag':meta.get('tag'),'reference_action':meta.get('reference_action'),'fitted':fitted,'recomputed_train_mse':mse,'checks':checks,'passed':all(checks.values())}


def inspect_cache_and_resources(meta,checks):
    cache=meta['template_cache'];conf=cache['configuration']
    fingerprint=hashlib.sha256(json.dumps(conf,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    checks['cache_fingerprint']=fingerprint==cache['fingerprint']
    compile_report=meta['compile'];checks['constructor_wall_guard']=compile_report.get('hard_wall_cap_includes_constructor') is True or cache.get('compilation_executed') is False
    if not compile_report['complete']:return None
    path=resolve(cache['pickle_file']);checks['template_pickle_hash']=sha(path)==cache['pickle_sha256']
    with path.open('rb') as stream:template=pickle.load(stream)
    checks['fixed_scientific_configuration']=template.output_depth==2 and template.order==1 and template.k==4 and template.boundary=='zero' and template.dependency_depth==0 and template.preserve_essential
    colors={i for i,name in enumerate(template.colors) if name[0] in ('x','h') and name[1]>=template.m}
    flags=np.array([any(color in colors for _,decs in flatten(tree)[0] for color in decs) for tree in template.trees])
    n=len(template.trees);pas=int(np.sum(flags));core=n-pas;N=64+template.m;terms=len(template.values);pterms=int(np.sum(flags[template.row_index]));dynamic=core+N*pas+1
    workspace=8*(4*N*pterms+4*N*n+3*N*len(template.coeff_keys)+20*dynamic+10*terms)
    recomputed={'template_contractions':n,'retained_terms':terms,'shared_core':core,'passive_per_query':pas,'query_count':N,'total_dynamic_scalars':dynamic,'estimated_peak_workspace_bytes':workspace,'estimated_peak_workspace_MiB':workspace/2**20,'passed':dynamic<=2000000 and workspace<=2**30}
    estimates=meta.get('resource_estimate',{})
    for key in ('retained_terms','shared_core','passive_per_query','query_count','total_dynamic_scalars','estimated_peak_workspace_bytes','passed'):
        checks['resource_'+key]=recomputed[key]==estimates.get(key)
    checks['template_size_caps']=n<=100000 and terms<=1000000
    return recomputed


def inspect_scalar(path):
    meta=read(path);checks={'target_mse':meta.get('target_mse')==.001,'selected_task':meta['task'] in SELECTED}
    if meta.get('stop_reason')=='process_failure' and not meta.get('template_cache'):
        log_path=path.parent/(meta['task']+'__run.log');log=log_path.read_text()
        checks.update(not_fitted=meta.get('fitted') is False,no_training=meta.get('training_seconds')==0.,nonzero_process_returncode=meta.get('process_returncode') not in (None,0),no_endpoint_checkpoint=not path.with_suffix('.npz').exists(),preserved_failure_log=bool(log))
        reporting_failure="object has no attribute 'essential_trees'" in log and "self.report={'status':reason" in log
        return {'task':meta['task'],'record_sha256':sha(path),'stop_reason':meta['stop_reason'],'status':'compile_reporting_failure' if reporting_failure else 'execution_failure','fitted':False,'training_seconds':0.,'log_file':str(log_path),'log_sha256':sha(log_path),'compile_limit_reporting_bug':reporting_failure,'interpretation':'No valid template or training endpoint. Source inspection shows CompileLimit was caught during selection, then missing essential_trees broke failure reporting; the triggering limit and partial counts were not saved.' if reporting_failure else 'No valid endpoint; execution failed before a detailed record was saved.','checks':checks,'passed':all(checks.values())}
    drift=[name for name,expected in meta.get('sources',{}).items() if not (STUDY/name).exists() or sha(STUDY/name)!=expected];checks['source_hashes_match']=not drift
    resources=inspect_cache_and_resources(meta,checks)
    result={'task':meta['task'],'record_sha256':sha(path),'stop_reason':meta.get('stop_reason'),'resources':resources,'source_drift':drift}
    if not meta.get('data_file'):
        reason=meta.get('stop_reason');checks['not_fitted_without_checkpoint']=not meta.get('fitted',False)
        checks['no_training_for_gate']=meta.get('training_seconds',0.)==0.
        if reason=='full_query_memory_gate':checks['gate_has_exceeded_resource_bound']=resources is not None and not resources['passed']
        elif reason=='compile_limit':checks['compilation_incomplete']=not meta['compile']['complete']
        category='resource_limited' if reason in ('compile_limit','full_query_memory_gate','initialization_wall_limit','rhs_cost_gate') else 'not_started_budget_or_execution_status'
        return {**result,'status':category,'fitted':False,'checks':checks,'passed':all(checks.values())}
    data_path=path.parent/meta['data_file'];checks['checkpoint_hash']=sha(data_path)==meta['data_sha256'];checks['resources_pass_before_training']=resources is not None and resources['passed']
    checks['saved_passive_independence']=meta['passive_independence']['random_nonzero_state_core_rhs_difference']==0.
    checks['saved_vectorization_check']=meta['vectorization_check']['scaled_error']<1e-12
    checks['initial_pool_discarded']=meta['initialization']['runtime_initial_pool_retained'] is False
    checks['empirical_initialization_unchanged']=meta['initialization']['mathematical_initialization_changed'] is False
    catalog=next(row for row in read(NEW/'coverage.json')['tasks'] if row['name']==meta['task'])
    equal(checks,'task_catalog_angles',meta['train_angles'],catalog['angles']);equal(checks,'task_catalog_labels',meta['train_labels'],catalog['labels'])
    equal(checks,'cache_geometry',meta['template_cache']['configuration']['u'],np.c_[np.cos(catalog['angles']),np.sin(catalog['angles'])]);equal(checks,'cache_labels',meta['template_cache']['configuration']['labels'],catalog['labels'])
    with np.load(data_path,allow_pickle=False) as data:
        checks['finite_numeric_arrays']=all(np.all(np.isfinite(data[k])) for k in data.files if np.issubdtype(data[k].dtype,np.number))
        state=data['state'];initial=data['initial_state'];labels=data['train_labels'];m=len(labels);angles=data['angles'];nc=len(data['core_ids']);npas=len(data['passive_ids'])
        ci={int(v):i for i,v in enumerate(data['core_ids'])};pi={int(v):i for i,v in enumerate(data['passive_ids'])};Fids=data['template_Fids'];train_ids=[ci[int(v)] for v in Fids[:m]];output_id=pi[int(Fids[-1])]
        core=2*state[-1]*np.clip(state[train_ids],-1,1);passive=2*state[-1]*np.clip(state[nc:-1].reshape(64+m,npas)[:,output_id],-1,1)
        equal(checks,'decoded_core',core,data['train_prediction']);equal(checks,'decoded_passive_panel',passive,data['all_passive_prediction'])
        checks['circle_alias_split']=np.array_equal(passive[:64],data['prediction']) and np.array_equal(passive[64:],data['passive_train_prediction'])
        equal(checks,'circle_grid',angles,2*np.pi*np.arange(64)/64);equal(checks,'query_panel',data['all_query_angles'],np.r_[angles,data['train_angles']]);equal(checks,'reported_labels',labels,meta['train_labels'])
        mse=float(np.mean((core-labels)**2));alias_mse=float(np.mean((passive[64:]-labels)**2));gap=passive[64:]-core
        for key,actual in [('train_mse',mse),('passive_train_mse',alias_mse),('alias_gap_rms',rms(gap)),('alias_gap_max',float(np.max(np.abs(gap))))]:equal(checks,key,actual,meta[key])
        fitted=meta.get('stop_reason')=='target' and mse<=.001*(1+1e-7);checks['fit_status']=fitted==bool(meta.get('fitted'));checks['endpoint_classification']=meta['endpoint_status']==('fitted threshold endpoint' if fitted else 'partial endpoint')
        checks['full_dynamic_count']=len(state)==resources['total_dynamic_scalars'];equal(checks,'history_final_mse',data['history'][-1,1],mse)
        initial_core=2*initial[-1]*np.clip(initial[train_ids],-1,1);initial_passive=2*initial[-1]*np.clip(initial[nc:-1].reshape(64+m,npas)[:,output_id],-1,1)
        equal(checks,'initial_core_loss',float(np.mean((initial_core-labels)**2)),meta['initial_train_mse']);equal(checks,'initial_alias_gap',float(np.max(np.abs(initial_passive[64:]-initial_core))),meta['initial_alias_max_gap'])
        comparisons={}
        for method in ('block','gaussian'):
            compared=reference_comparison(meta['task'],method,angles,data['prediction'],NEW,.001);compared['fitted_pair']=bool(fitted and compared.get('fitted'));comparisons[method]=compared
            recorded=meta.get(method+'_comparison',{})
            if recorded.get('status')=='available':
                equal(checks,method+'_raw_rms',compared['raw_circle_rms'],recorded['raw_circle_rms']);equal(checks,method+'_grid_diagnostic',compared['circle64_vs32_rms_change'],recorded['circle_grid_change_64_vs_32']);checks[method+'_fitted_pair']=compared['fitted_pair']==recorded['fitted_pair']
        if comparisons['gaussian']['fitted_pair']:
            error=comparisons['gaussian']['raw_circle_rms'];screen='coarse_accuracy' if error<=.1 else 'high_error' if error>.3 else 'intermediate'
        else:screen='partial_not_eligible'
        result.update(status='fitted' if fitted else 'partial',fitted=fitted,core_train_mse=mse,passive_train_mse=alias_mse,alias_rms=rms(gap),alias_max=float(np.max(np.abs(gap))),alias_inconsistency_flag=float(np.max(np.abs(gap)))>.05,comparisons=comparisons,gaussian_screen=screen,training_seconds=meta['training_seconds'])
    result.update(checks=checks,passed=all(checks.values()) and all(c.get('passed',True) for c in result['comparisons'].values()))
    return result


def inspect_carried(task,previous_audit):
    evidence=next(row for row in previous_audit['results'] if row['task']==task and row['output_dependency_depth']==2)
    path=resolve(evidence['record']);meta=read(path);checkpoint=path.parent/meta['data_file']
    checks={'prior_independent_audit_passed':bool(evidence['passed']),'metadata_unchanged':sha(path)==evidence['record_sha256'],'checkpoint_hash':sha(checkpoint)==meta['data_sha256'],'target_mse':meta['target_mse']==.001}
    with np.load(checkpoint,allow_pickle=False) as data:
        state=data['state'];m=len(data['train_labels']);nc=len(data['core_ids']);npas=len(data['passive_ids'])
        ci={int(v):i for i,v in enumerate(data['core_ids'])};pi={int(v):i for i,v in enumerate(data['passive_ids'])}
        core=2*state[-1]*np.clip(state[[ci[int(v)] for v in data['template_Fids'][:m]]],-1,1)
        passive=2*state[-1]*np.clip(state[nc:-1].reshape(64+m,npas)[:,pi[int(data['template_Fids'][-1])]],-1,1)
        equal(checks,'decoded_core',core,data['train_prediction']);equal(checks,'decoded_passive',passive,data['all_passive_prediction'])
        mse=float(np.mean((core-data['train_labels'])**2));equal(checks,'core_mse',mse,meta['train_mse'])
        checks['fitted']=bool(meta['fitted'] and meta['stop_reason']=='target' and mse<=.001*(1+1e-7))
        checks['finite_state']=bool(np.all(np.isfinite(state)))
        comparisons={method:reference_comparison(task,method,data['angles'],data['prediction'],NEW,.001) for method in ('block','gaussian')}
    return {'task':task,'status':'carried_forward_fitted','record':str(path),'record_sha256':sha(path),'checkpoint_sha256':sha(checkpoint),'core_train_mse':mse,'comparisons':comparisons,'checks':checks,'passed':all(checks.values()) and all(c['passed'] for c in comparisons.values())}


def reference_pair_grid(task):
    paths=[NEW/'references'/f'{task}__{tag}.npz' for tag in ('gaussian','block_k4_P1_canonical')]
    if not all(path.exists() for path in paths):return {'task':task,'status':'pending'}
    with np.load(paths[0],allow_pickle=False) as gaussian,np.load(paths[1],allow_pickle=False) as block:
        grid_equal=np.array_equal(gaussian['angles'],block['angles']);difference=block['prediction']-gaussian['prediction']
        fine=rms(difference);panel=rms(difference[::4]);coarse=rms(difference[::8])
    return {'task':task,'same_256_angles':grid_equal,'block_gaussian_rms_256':fine,'block_gaussian_rms_64':panel,'block_gaussian_rms_32':coarse,'change_64_vs_256':abs(panel-fine),'change_64_vs_32':abs(panel-coarse),'reference_quadrature_flag_64_vs_256':abs(panel-fine)>.001,'interpretation':'Control-grid diagnostic only; scalar values were evaluated on 64 angles.'}


def audit():
    rows=[];refs=[];errors=[];unexpected=[]
    for task in SELECTED:
        path=NEW/'scalar'/f'{task}__selective_zero_out2.json'
        if path.exists():
            try:rows.append(inspect_scalar(path))
            except Exception as exc:errors.append({'scalar':task,'error':repr(exc)})
    for task in SELECTED+CARRIED:
        for tag in ('gaussian','block_k4_P1_canonical'):
            path=NEW/'references'/f'{task}__{tag}.json'
            if path.exists():
                try:refs.append(inspect_reference(path))
                except Exception as exc:errors.append({'reference':str(path),'error':repr(exc)})
    for task in NOT_SELECTED:
        unexpected.extend(str(p) for p in (NEW/'scalar').glob(task+'__*'))
        unexpected.extend(str(p) for p in (NEW/'references').glob(task+'__gaussian.*'))
        unexpected.extend(str(p) for p in (NEW/'references').glob(task+'__block_k4_P1_canonical.*'))
    helpers={}
    for name in ('initializer_equivalence','runtime_equivalence'):
        path=NEW/'checks'/f'{name}.json'
        if path.exists():
            record=read(path);items=record.get('reports',record.get('results',[]));ok=True
            for item in items:
                if name=='initializer_equivalence':ok &= item['bitwise_equal'] and item['max_absolute_error']==0.
                else:ok &= all(check['bitwise_equal'] and check['max_absolute_error']==0. for check in item['checks_initial_final_active_clipping'])
            helpers[name]={'artifact_sha256':sha(path),'bitwise_checks_pass':bool(ok),'tasks':[r['task'] for r in items]}
    previous_path=BASE/'selective_tighter_20260927/checks/independent_tighter_audit.json';previous=read(previous_path);carried=[]
    for task in CARRIED:
        try:carried.append(inspect_carried(task,previous))
        except Exception as exc:errors.append({'carried_forward':task,'error':repr(exc)})
    grids=[reference_pair_grid(task) for task in SELECTED+CARRIED]
    return {'audited_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(__file__),'scope':'Six newly selected J2 attempts, three prior completed cases carried forward, eight explicitly not selected; no new computation of model trajectories','selected_new_tasks':list(SELECTED),'carried_forward_tasks':list(CARRIED),'not_selected_tasks':list(NOT_SELECTED),'new_scalar_records':len(rows),'reference_records':len(refs),'complete':len(rows)==6 and len(refs)==18 and len(carried)==3,'passed':not errors and not unexpected and all(r['passed'] for r in rows+refs+carried) and len(helpers)==2 and all(r['bitwise_checks_pass'] for r in helpers.values()),'errors':errors,'unexpected_unselected_outputs':unexpected,'exact_shortcut_checks':helpers,'new_scalars':rows,'references':refs,'carried_forward_records':carried,'carried_forward_audit_sha256':sha(previous_path),'reference_grid_diagnostics':grids}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--watch',action='store_true');parser.add_argument('--deadline',type=float,default=time.time()+720);args=parser.parse_args()
    output=NEW/'checks';output.mkdir(parents=True,exist_ok=True)
    while True:
        result=audit();(output/'independent_selected_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('audited_utc','new_scalar_records','reference_records','complete','passed','errors')}),flush=True)
        if not args.watch or result['complete'] or time.time()>=args.deadline:break
        time.sleep(30.)
