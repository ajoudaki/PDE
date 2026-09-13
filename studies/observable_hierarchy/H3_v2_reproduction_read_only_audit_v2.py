from pathlib import Path
import hashlib,json,itertools
import numpy as np
from pde.observable_solver import load_restart
root=Path.cwd();scratch=Path(__file__).resolve().parent
manifest=json.loads((root/'review/manifest.json').read_text());planpath=root/'code/validation/observable_solver_plan.json';plan=json.loads(planpath.read_text());planhash=hashlib.sha256(planpath.read_bytes()).hexdigest();runs=root/'data/established/independent_v2_runs';summary=json.loads((root/'data/established/independent_v2_analysis/summary.json').read_text());supervisor=json.loads((runs/'supervisor.json').read_text())
assert [r['id'] for r in supervisor['configurations']]==[c['id'] for c in plan['configurations']]
assert {p.name for p in runs.iterdir() if p.is_dir()}=={c['id'] for c in plan['configurations']}
assert supervisor['supervisor_sha256']==manifest['edition_hashes']['code/scripts/run_observable_validation.py']
assert supervisor['worker_sha256']==manifest['edition_hashes']['code/scripts/validate_observable_solver.py']
assert summary['postprocessor_sha256']==manifest['edition_hashes']['code/scripts/analyze_observable_solver.py']
result=dict(status='pass',raw_immutable_checks={},runs=[],comparison_pairs=[])
for p,h in json.loads((scratch/'immutable_raw_evidence_hashes.json').read_text()).items():
 actual=hashlib.sha256((root/p).read_bytes()).hexdigest();assert actual==h;result['raw_immutable_checks'][p]=actual
for config,superrow,row in zip(plan['configurations'],supervisor['configurations'],summary['runs']):
 name=config['id'];folder=runs/name;recordpath=folder/'record.json';record=json.loads(recordpath.read_text());assert record['configuration']==config and record['plan_sha256']==planhash
 assert record['status']==superrow['status']=='operational_pass' and record['restart_exact']
 assert superrow['record_sha256']==hashlib.sha256(recordpath.read_bytes()).hexdigest()
 assert record['producer_sha256']==manifest['edition_hashes']['code/scripts/validate_observable_solver.py']
 assert len(record['source_hashes'])==6
 for filename,h in record['source_hashes'].items():assert h==manifest['edition_hashes']['code/pde/'+filename]
 for filename,h in record['outputs'].items():assert h==hashlib.sha256((folder/filename).read_bytes()).hexdigest()
 assert set(record['thread_environment'].values())=={'1'}
 state,data=load_restart(folder/'final_restart.json');mid,middata=load_restart(folder/'midpoint_restart.json')
 frozen=('b1','g','p1','b2','p2','D')
 assert all(np.array_equal(getattr(state,k),getattr(mid,k)) for k in frozen)
 assert all(np.array_equal(getattr(data,k),getattr(middata,k)) for k in ('inputs','labels','probabilities'))
 keys=('b1','g','w','p1','b2','c','p2','M','D')
 assert set(vars(state))==set(keys)|{'arithmetic','metadata'}
 a={k:np.asarray(getattr(state,k),float) for k in keys};u=np.asarray(data.inputs,float);pw=np.asarray(data.probabilities,float)
 expected={1:(5,3),3:(35,10),5:(128,21)}[config['order']];p=config['population_nodes'];d1,d2=expected;m=len(u);B=min(plan['common']['block_size'],m)
 assert a['b1'].shape==(p,d1) and a['b2'].shape==(p,d2) and a['M'].shape==a['D'].shape==(d2,d1)
 assert m==(2 if config['law']=='atom' else 2*config['nodes_per_arc'])
 assert all(np.isfinite(v).all() for v in a.values())
 initial1=np.tanh(a['g']@u.T);current1=np.tanh(a['w']@u.T);initial2=np.tanh(a['b2']@(a['D']@(a['b1'].T@(a['p1'][:,None]*initial1))));current2=np.tanh(a['b2']@(a['M']@(a['b1'].T@(a['p1'][:,None]*current1))))
 with np.load(folder/'observations.npz',allow_pickle=False) as z:
  errors=dict(first_pairs=float(np.max(np.abs(z['first_pairs']-np.stack((initial1,current1),axis=2)))),second_pairs=float(np.max(np.abs(z['second_pairs']-np.stack((initial2,current2),axis=2)))))
  circle=z['circle'];h1=np.tanh(a['w']@circle.T);h2=np.tanh(a['b2']@(a['M']@(a['b1'].T@(a['p1'][:,None]*h1))));prediction=a['p2']@(a['c'][:,None]*h2)
  errors['prediction']=float(np.max(np.abs(prediction-z['prediction'])))
  assert all(v<1e-12 for v in errors.values())
  for layer,prior,current in ((1,initial1,current1),(2,initial2,current2)):
   rms=float(np.sqrt(a['p'+str(layer)]@((current-prior)**2)@pw));errors['rms'+str(layer)]=abs(rms-record['rms'+str(layer)]);assert errors['rms'+str(layer)]<1e-12
 # Differences are computed in the working arithmetic before float conversion.
 with state.arithmetic.context():
  dynamics=dict(row_max_abs=float(np.max(np.abs(np.asarray(state.w-state.g,float)))),readout_max_abs=float(np.max(np.abs(np.asarray(state.c,float)))),matrix_frobenius=float(np.linalg.norm(np.asarray(state.M-state.D,float))))
 assert all(value>0 and value==record['dynamic_changes'][k] for k,value in dynamics.items())
 phases=('initialization','evolution','restart','observation');overhead={clock:record['total_seconds'][clock]-sum(record[k+'_seconds'][clock] for k in phases) for clock in ('cpu','wall')}
 assert min(overhead.values())>=0
 assert row['state_memory_postprocess']['array_byte_correction']==0
 S=p*(d1+5)+p*(d2+2)+2*d1*d2;V=3*p+d1*d2;fields=B*(3*p+d1+d2+1)
 assert row['state_scalars']==S and row['dynamic_scalars']==V
 result['runs'].append(dict(id=name,source_and_output_hashes_verified=True,complete_state_schema=True,frozen_marks_midpoint_to_final_exact=True,dimensions=[d1,d2],state_scalars=S,dynamic_scalars=V,fields_block_retained_scalar_slots=fields,heun_workspace_scalars_planning_estimate=10*V+6*fields+8*m,workspace_estimate_meaning='Conservative scalar-slot planning allowance from fixed-size stage/velocity and blocked field expressions; excludes caller-held states, scalar-object internals, BLAS/interpreter workspace and Python/container heap; no measured allocator peak claim.',float64_reconstruction_max_errors=errors,dynamic_changes=dynamics,diagnostics_serialization_other_seconds=overhead,evolution_cpu_seconds_per_step=record['evolution_seconds']['cpu']/config['steps']))
# Independently enumerate the declared comparison rule and compare all pairs.
for a,b in itertools.combinations(plan['configurations'],2):
 if a['law']!=b['law']:continue
 changed={k for k in a if k!='id' and a[k]!=b[k]}
 if changed=={'order'} or (changed and (changed<={'digits','backend'} or changed<={'initialization_nodes','population_nodes','nodes_per_arc','steps'})):result['comparison_pairs'].append([a['id'],b['id']])
assert result['comparison_pairs']==[[r['left'],r['right']] for r in summary['comparisons']]
(scratch/'read_only_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(status=result['status'],runs=len(result['runs']),comparison_pairs=len(result['comparison_pairs']),maximum_reconstruction_error=max(v for r in result['runs'] for v in r['float64_reconstruction_max_errors'].values()))))
