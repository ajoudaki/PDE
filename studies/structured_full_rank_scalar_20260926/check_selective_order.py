"""Independent saved-result audit of output dependency depth J=1 versus J=2.

Loads saved templates for set/row checks; never compiles or integrates an ODE.
Reads only this study's authorized order and geometry comparison namespaces.
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
from true_aggregate_ode import degree

STUDY=Path(__file__).resolve().parent
ROOT=STUDY.parent.parent
BASE=ROOT/'data/generated/structured_full_rank_scalar_20260926'
OLD=BASE/'selective_geometry_20260927'
NEW=BASE/'selective_order_20260927'
TASKS=('pair_orthogonal_cos1','cluster_triple_cos1','triple_wide_mixed')

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())
def rms(values):return float(np.sqrt(np.mean(np.asarray(values)**2)))
def resolve(path):
    path=Path(path);return path if path.is_absolute() else ROOT/path

def check_value(checks,name,a,b):checks[name]=bool(np.allclose(a,b,rtol=1e-10,atol=1e-12))
def records(folder,task):return list(folder.rglob(task+'__selective_zero.json'))+list(folder.rglob(task+'__selective_zero_depth2.json'))+list(folder.rglob(task+'__selective_zero_out2.json'))

def metric_record(path):
    meta=read(path);checks={};result={'record':str(path),'record_sha256':sha(path),'stop_reason':meta.get('stop_reason'),'recorded_fitted':bool(meta.get('fitted'))}
    result['source_matches']={name:(STUDY/name).exists() and sha(STUDY/name)==value for name,value in meta.get('sources',{}).items()}
    if not meta.get('data_file'):
        return {**result,'status':'no_checkpoint','fitted':False,'checks':{'not_fitted':not meta.get('fitted',False)},'passed':not meta.get('fitted',False)}
    data_path=path.parent/meta['data_file'];checks['data_sha256']=sha(data_path)==meta['data_sha256']
    with np.load(data_path,allow_pickle=False) as data:
        checks['finite_saved_numeric_arrays']=all(np.all(np.isfinite(data[k])) for k in data.files if np.issubdtype(data[k].dtype,np.number))
        labels=np.asarray(data['train_labels']);m=len(labels);angles=data['angles'];core=data['train_prediction'];alias=data['passive_train_prediction']
        checks['circle64_shape']=angles.shape==(64,) and data['prediction'].shape==(64,)
        check_value(checks,'circle64_angles',angles,2*np.pi*np.arange(64)/64)
        check_value(checks,'query_panel_angles',data['all_query_angles'],np.r_[angles,data['train_angles']])
        checks['circle_alias_split']=np.array_equal(data['all_passive_prediction'][:64],data['prediction']) and np.array_equal(data['all_passive_prediction'][64:],alias)
        check_value(checks,'metadata_labels',labels,meta['train_labels'])
        state=data['state'];nc=len(data['core_ids']);npas=len(data['passive_ids']);Fids=data['template_Fids']
        ci={int(v):i for i,v in enumerate(data['core_ids'])};pi={int(v):i for i,v in enumerate(data['passive_ids'])}
        train_ids=[ci[int(v)] for v in Fids[:m]];output_id=pi[int(Fids[-1])]
        check_value(checks,'core_decoded_from_state',2*state[-1]*np.clip(state[train_ids],-1,1),core)
        check_value(checks,'passive_decoded_from_state',2*state[-1]*np.clip(state[nc:-1].reshape(64+m,npas)[:,output_id],-1,1),data['all_passive_prediction'])
        core_mse=float(np.mean((core-labels)**2));alias_mse=float(np.mean((alias-labels)**2));gap=alias-core
        for name,value in [('train_mse',core_mse),('passive_train_mse',alias_mse),('alias_gap_rms',rms(gap)),('alias_gap_max',float(np.max(np.abs(gap))))]:check_value(checks,name,value,meta[name])
        fitted=meta.get('stop_reason')=='target' and core_mse<=.01*(1+1e-7)
        checks['fit_status']=fitted==bool(meta.get('fitted'))
        checks['partial_classification']=meta['endpoint_status']==('fitted threshold endpoint' if fitted else 'partial endpoint')
        comparisons={}
        for method,tag in [('block','block_k4_P1_canonical'),('gaussian','gaussian')]:
            ref_path=OLD/'references'/f"{meta['task']}__{tag}.json";ref_meta=read(ref_path);ref_data_path=ref_path.parent/ref_meta['data_file']
            checks[method+'_data_hash']=sha(ref_data_path)==ref_meta['data_sha256']
            with np.load(ref_data_path,allow_pickle=False) as ref:
                distances=np.abs(np.angle(np.exp(1j*(angles[:,None]-ref['angles'][None,:]))));idx=np.argmin(distances,axis=1)
                checks[method+'_exact_matched_angles']=len(set(map(int,idx)))==64 and float(np.max(distances[np.arange(64),idx]))<1e-13
                difference=data['prediction']-ref['prediction'][idx];error=rms(difference);grid_change=abs(error-rms(difference[::2]))
                ref_mse=float(np.mean((ref['train_prediction']-ref['train_labels'])**2));ref_fitted=ref_meta['stop_reason']=='target' and ref_mse<=.01*(1+1e-7)
                check_value(checks,method+'_labels',labels,ref['train_labels'])
            recorded=meta.get(method+'_comparison',{})
            if recorded.get('status')=='available':
                check_value(checks,method+'_reported_circle_rms',error,recorded['raw_circle_rms'])
                check_value(checks,method+'_reported_grid_change',grid_change,recorded['circle_grid_change_64_vs_32'])
                checks[method+'_recorded_reference_hash']=recorded['data_sha256']==sha(ref_data_path)
            comparisons[method]={'raw_circle_rms':error,'circle64_vs32_rms_change':grid_change,'quadrature_flag':grid_change>.001,'reference_fitted':ref_fitted,'fitted_pair':bool(fitted and ref_fitted),'reference_data_sha256':sha(ref_data_path)}
        result.update(status='fitted' if fitted else 'partial',fitted=fitted,core_train_mse=core_mse,passive_train_mse=alias_mse,alias_rms=rms(gap),alias_max=float(np.max(np.abs(gap))),alias_inconsistency_flag=float(np.max(np.abs(gap)))>.05,dynamic_scalars=len(state),shared_core_scalars=nc,passive_scalars_per_query=npas,clock_scalars=1,training_seconds=meta.get('training_seconds'),initialization_seconds=meta.get('initialization',{}).get('seconds'),comparisons=comparisons)
    result.update(checks=checks,passed=all(checks.values()))
    return result


def load_template(meta):
    cache=meta['template_cache'];path=resolve(cache['pickle_file'])
    if sha(path)!=cache['pickle_sha256']:raise ValueError('Template pickle digest mismatch')
    config=cache['configuration'];fingerprint=hashlib.sha256(json.dumps(config,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    if fingerprint!=cache['fingerprint']:raise ValueError('Template configuration fingerprint mismatch')
    with path.open('rb') as stream:template=pickle.load(stream)
    return template,path,cache['pickle_sha256']


def structural_check(meta1,meta2):
    a,pa,ha=load_template(meta1);b,pb,hb=load_template(meta2)
    first=set(a.trees);second=set(b.trees);checks={'nested_selected_tree_sets':first<=second,'strictly_larger_selected_set':len(second)>len(first),'depths_are_1_and_2':a.output_depth==1 and b.output_depth==2,'same_u':np.array_equal(a.u,b.u),'same_labels':np.array_equal(a.labels,b.labels),'same_k_memory_boundary':a.k==b.k==4 and a.order==b.order==1 and a.boundary==b.boundary=='zero','same_fixed_dependency_depth':a.dependency_depth==b.dependency_depth==0,'same_essential_roots':set(a.essential_trees)==set(b.essential_trees)}
    # Old exact F rows supply first-generation output child trees. We check
    # those saved rows' children in J2 against full public derivative formulas.
    output_children=set()
    for idx in a.Fids:
        output_children.update(a.trees[child] for coefficient,key,child in a.rows[int(idx)])
    protected=set(b.essential_trees)|output_children
    missing_rows=[];coefficient_mismatches=[]
    for tree in protected:
        index=b.tree_ids.get(tree)
        if index is None:missing_rows.append({'degree':degree(tree),'reason':'row absent'});continue
        full={(key,child):coefficient for coefficient,key,child in b.derivative(tree)}
        stored={(key,b.trees[child]):coefficient for coefficient,key,child in b.rows[index]}
        if set(full)!=set(stored):missing_rows.append({'degree':degree(tree),'missing_terms':len(set(full)-set(stored))})
        elif full!=stored:coefficient_mismatches.append(index)
    checks['all_first_output_children_and_essential_rows_exact']=not missing_rows and not coefficient_mismatches
    # A bounded countercheck: stop at first D-field constituent whose dynamics
    # still meets the boundary. This is not a full omitted-term enumeration.
    witness=None
    Dtrees=sorted({child for terms in b.Dterms.values() for coefficient,key,child in terms})
    for tree in Dtrees:
        omitted=[child for coefficient,key,child in b.derivative(tree) if child not in b.tree_ids]
        if omitted:
            witness={'constituent_degree':degree(tree),'constituent_row_index':b.tree_ids[tree],'missing_derivative_terms':len(omitted),'first_missing_child_degree':degree(omitted[0])};break
    return {'checks':checks,'passed':all(checks.values()),'q1_template':str(pa),'q1_template_sha256':ha,'q2_template':str(pb),'q2_template_sha256':hb,'q1_contractions':len(a.trees),'q2_contractions':len(b.trees),'new_contractions':len(second-first),'q1_maximum_local_degree':max(map(degree,a.trees)),'q2_maximum_local_degree':max(map(degree,b.trees)),'q1_retained_terms':len(a.values),'q2_retained_terms':len(b.values),'checked_output_child_rows':len(output_children),'checked_total_protected_rows':len(protected),'missing_protected_rows':missing_rows,'coefficient_mismatches':coefficient_mismatches,'remaining_D_feedback_derivative_boundary_witness':witness,'interpretation':'Nested states and protected explicit output-child derivatives; no monotone error or full output-curvature/convergence guarantee. All runtime variables are current scalar contractions and one clock.'}


def audit():
    rows=[];errors=[]
    for task in TASKS:
        old=records(OLD,task);new=records(NEW,task)
        if not new:continue
        if len(old)!=1 or len(new)!=1:
            errors.append({'task':task,'old_record_count':len(old),'new_record_count':len(new)});continue
        try:
            q1=metric_record(old[0]);q2=metric_record(new[0]);row={'task':task,'q1':q1,'q2':q2}
            if q1.get('comparisons') and q2.get('comparisons'):
                structure=structural_check(read(old[0]),read(new[0]));row['structure']=structure
                old_error=q1['comparisons']['block']['raw_circle_rms'];new_error=q2['comparisons']['block']['raw_circle_rms'];change=(old_error-new_error)/old_error if old_error else None
                eligible=q1['comparisons']['block']['fitted_pair'] and q2['comparisons']['block']['fitted_pair']
                classification=('improvement_at_least_5percent' if change>=.05 else 'increase_at_least_5percent' if change<=-.05 else 'less_than_5percent_change') if eligible and change is not None else 'partial_comparison'
                row.update(primary_fractional_error_reduction=change,fitted_primary_comparison=eligible,primary_classification=classification,passed=q1['passed'] and q2['passed'] and structure['passed'])
            else:row.update(primary_classification='no_complete_checkpoint_comparison',passed=q1['passed'] and q2['passed'])
            rows.append(row)
        except Exception as exc:errors.append({'task':task,'error':repr(exc)})
    return {'audited_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(__file__),'scope':'Saved J1/J2 templates and artifacts only; no compilation, training, or ODE evaluation','expected_tasks':list(TASKS),'recorded_tasks':len(rows),'complete':len(rows)==3,'passed':not errors and all(row['passed'] for row in rows),'errors':errors,'results':rows}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--watch',action='store_true');parser.add_argument('--deadline',type=float,default=time.time()+720);args=parser.parse_args()
    output=NEW/'checks';output.mkdir(parents=True,exist_ok=True)
    while True:
        result=audit();(output/'independent_order_audit.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({key:result[key] for key in ('audited_utc','recorded_tasks','complete','passed','errors')}),flush=True)
        if not args.watch or result['complete'] or time.time()>=args.deadline:break
        time.sleep(30.)
