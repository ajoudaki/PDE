import base64, hashlib, json, signal, time
from collections import Counter
from pathlib import Path
import numpy as np
start=time.perf_counter()
signal.alarm(59)
root=Path('/home/amir/Codes/PDE')
base=root/'data/generated/alternating_circle_fit_capacity_20260921'
export=base/'radial_view01/final'
out=base/'radial_browser01/data_check.json'
assert not out.exists()
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def npz(p):
 with np.load(p,allow_pickle=False) as z:return {k:z[k].copy() for k in z.files}
def pred(state,fixed,u):
 n=len(state['c']);h=np.tanh(state['W']@u.T)
 if 'A' in state: z=state['A']@h
 else:z=fixed['B2']@(state['M']@(fixed['B1'].T@h/n))
 return state['c']@np.tanh(z)/n
payload=read(export/'payload.json');audit=read(export/'audit.json')
errors=[]
def check(cond,label):
 if not cond:errors.append(label)
check(sha(root/'studies/alternating_circle_fit_capacity_20260921/radial_data.py')==audit['exporterSha256'],'exporter_hash')
check(sha(export/'payload.json')==audit['outputsSha256']['payload.json'],'payload_hash')
analyses={r:read(base/p/'analysis.json') for r,p in [('adam','analysis01'),('gd','gd_analysis01')]}
for p,h in audit['inputAnalysisSha256'].items():check(sha(p)==h,'input_analysis_hash:'+p)
rows={f'{r}:{a["attempt"]}':(r,a,Path(d['run_root'])/a['attempt']) for r,d in analyses.items() for a in d['attempts'] if not a['reproduction']}
ids=[a['id'] for a in payload['records']]
check(len(ids)==69 and len(set(ids))==69 and set(ids)==set(rows),'exact_original_69_scope')
check(Counter(r['round'] for r in payload['records'])=={'adam':30,'gd':39},'round_counts')
auditrows={a['id']:a for a in audit['attempts']}
check(set(auditrows)==set(ids),'audit_record_coverage')
checks=[]
for rec in payload['records']:
 ident=rec['id'];rid,row,path=rows[ident];ar=auditrows[ident]
 record=read(path/'record.json');data=npz(path/'dataset.npz');saved=npz(path/'predictions.npz');state=npz(path/'best.npz')
 fixed=npz(path/'initial.npz') if rec['model'].startswith('closure') else {}
 check(sha(path/'record.json')==row['record_sha256']==ar['recordSha256'],ident+':record_hash')
 for name,key in [('best.npz','bestSha256'),('dataset.npz','datasetSha256'),('predictions.npz','predictionsSha256'),('trace.jsonl','traceSha256')]:
  check(sha(path/name)==ar[key]==record['outputs_sha256'][name],ident+':'+name+'_hash')
 check(row['decision_valid'] and not row['reproduction'],ident+':decision_original')
 check(rec['m']==row['m'] and rec['seed']==row['seed'] and rec['model']==row['model'],ident+':configuration')
 check(rec['gain']==('canonical' if row['initialization']=='canonical' else 'high'),ident+':gain')
 check(rec['etaMax']==(row['eta_max'] if rid=='gd' else None),ident+':step_cap')
 check(rec['trainable']==row['trainable_scalars'] and rec['retained']==row['retained_predictor_scalars'],ident+':scalar_counts')
 samples=np.frombuffer(base64.b64decode(rec['samples64']),dtype='<f8')
 y=(-1.)**np.arange(rec['m']);theta=2*np.pi*np.arange(rec['m'])/rec['m']
 check(samples.shape==(rec['m'],) and np.isfinite(samples).all(),ident+':samples_shape')
 check(np.array_equal(y,data['y']) and np.max(np.abs(theta-data['theta']))<1e-14,ident+':sample_order')
 metrics_mse=float(np.mean((samples-y)**2));metrics_signs=int(np.count_nonzero(samples*y<=0));fitted=metrics_mse<=.001 and metrics_signs==0
 expected_mse=row['reported_mse'] if rid=='adam' else row['best_mse'];expected_signs=row['reported_sign_errors'] if rid=='adam' else row['best_sign_errors']
 check(abs(metrics_mse-expected_mse)<=1e-9 and rec['mse']==expected_mse,ident+':mse')
 check(metrics_signs==rec['signErrors']==expected_signs and fitted==rec['fit']==row['accepted_fit'],ident+':fit_signs')
 best=None;count=0
 for line in (path/'trace.jsonl').read_text().splitlines():
  e=json.loads(line);count+=1;v=e.get('mse')
  if v is not None and np.isfinite(v) and (best is None or v<best['mse']):best=e
 check(best is not None and abs(best['mse']-record['diagnostics']['best']['mse'])<=1e-9,ident+':best_trace_checkpoint')
 check(rec['bestPhase']==best.get('phase') and rec['bestStep']==best.get('accepted_step' if rid=='gd' else 'optimizer_step') and rec['bestEvaluation']==best.get('forward_evaluations' if rid=='gd' else 'evaluation'),ident+':best_phase_step')
 check(ar['traceSelection']['traceEntries']==count,ident+':trace_count')
 phase=rec['bestPhase'];kind=rec['bestStateKind']
 check(('line-search trial' in kind) if phase=='lbfgs' else ('least-squares' in kind) if phase=='readout_polish' else ('accepted simultaneous GD' in kind) if phase=='gd' else True,ident+':best_state_kind')
 result={'id':ident,'mse_discrepancy':abs(metrics_mse-expected_mse),'phase':phase,'sample_source':'float64_checkpoint_replay'}
 if rec['circleAvailable']:
  check(row['raw_replay_valid'] and 'highPrecisionEvidence' not in ar,ident+':circle_authority')
  p=pred(state,fixed,data['u']);sampleerr=float(np.max(np.abs(p-samples)))
  check(sampleerr<=1e-8 and np.max(np.abs(samples-saved['best_train']))<=1e-8,ident+':samples64_checkpoint')
  values=np.frombuffer(base64.b64decode(rec['circle32']),dtype='<f4').astype(float)
  indices=np.frombuffer(base64.b64decode(rec['indices16']),dtype='<u2').astype(int)
  check(len(indices)==len(values)==rec['circleCount'] and 128<=len(indices)<=2048 and indices[0]==0 and indices[-1]<8192 and np.all(np.diff(indices)>0),ident+':curve_indices')
  grid=np.concatenate([pred(state,fixed,data['circle_u'][j:j+512]) for j in range(0,8192,512)])
  griderr=float(np.max(np.abs(grid-saved['best_circle'])))
  check(griderr<=1e-8,ident+':grid_checkpoint')
  selectederror=float(np.max(np.abs(values-grid[indices])))
  check(selectederror<=rec['circleRoundingError']+1e-8,ident+':selected_values')
  displayed=np.interp(np.arange(8192),np.append(indices,8192),np.append(values,values[0]))
  interp=float(np.max(np.abs(displayed-grid)))
  check(abs(interp-rec['circleInterpolationError'])<=2e-8,ident+':interpolation_error')
  check(abs(grid.min()-rec['circleMin'])<=1e-8 and abs(grid.max()-rec['circleMax'])<=1e-8 and abs(np.max(np.abs(grid))-rec['circleMaxAbs'])<=1e-8,ident+':full_grid_extrema')
  check(abs(grid[indices].min()-grid.min())<=1e-8 and abs(grid[indices].max()-grid.max())<=1e-8,ident+':global_extrema_retained')
  disp=ar['display'];check(disp['globalExtremaRetained'] and disp['vertices']==len(indices),ident+':display_metadata')
  check(disp['targetMetBeforeRounding']==(disp['beforeRoundingInterpolationError']<=.002+1e-12),ident+':target_flag')
  result.update(sample_max_error=sampleerr,grid_max_error=griderr,interpolation_error=interp,vertices=len(indices),target_met=disp['targetMetBeforeRounding'])
 else:
  check(rid=='adam' and 'highPrecisionEvidence' in ar and rec['circleCount']==0 and rec['circle32'] is None and rec['indices16'] is None and bool(rec['circleReason']),ident+':markers_only')
  evidence=read(ar['highPrecisionEvidence']);check(sha(ar['highPrecisionEvidence'])==ar['highPrecisionEvidenceSha256'],ident+':HP_evidence_hash')
  expected=np.asarray([float(v) for v in evidence['high_precision']['predictions_decimal']])
  check(evidence['best_sha256']==sha(path/'best.npz') and evidence['dataset_sha256']==sha(path/'dataset.npz'),ident+':HP_checkpoint_data_binding')
  check(np.array_equal(samples,expected),ident+':HP_samples64_exact')
  result.update(sample_source='existing_high_precision_predictions_converted_to_binary64',digits=evidence['high_precision']['digits'],sample_max_error=0.)
 checks.append(result)
check(sum(r['circleAvailable'] for r in payload['records'])==65 and sum(not r['circleAvailable'] for r in payload['records'])==4,'curve_marker_counts')
for rid,analysis in analyses.items():
 for group in analysis['groups']:
  members=[r for r in payload['records'] if r['round']==rid and r['model']==group['model'] and r['m']==group['m'] and r['gain']==('canonical' if group['initialization']=='canonical' else 'high') and r['etaMax']==(group['eta_max'] if rid=='gd' else None)]
  check(len(members)==group['attempts'] and sum(r['fit'] for r in members)==group['fits'],'group_counts:'+str((rid,group['model'],group['m'],group['initialization'],group.get('eta_max'))))
report={'passed':not errors,'failures':errors,'scope':'Independent display-data fidelity only; no training or repeated optimization audit. All69 sample arrays/metrics/phase bindings and all65 circle subsets replayed.','record_count':len(checks),'original_counts':dict(Counter(r['round'] for r in payload['records'])),'circle_count':65,'high_precision_markers_only_count':4,'source_sha256':{'radial_data.py':sha(root/'studies/alternating_circle_fit_capacity_20260921/radial_data.py'),'payload.json':sha(export/'payload.json'),'audit.json':sha(export/'audit.json')},'maximum_sample_discrepancy':max(r['sample_max_error'] for r in checks),'maximum_circle_replay_discrepancy':max(r.get('grid_max_error',0) for r in checks),'maximum_sampled_grid_interpolation_error':max(r.get('interpolation_error',0) for r in checks),'curves_exceeding_nominal_0_002_target':sum(r.get('target_met') is False for r in checks),'elapsed_seconds':time.perf_counter()-start,'cpu_budget_seconds':60,'training_performed':False,'limitations':['Thirty curves reach the2048-vertex limit before the nominal0.002 interpolation target; use each actual error.','Interpolation errors concern8192 stored grid nodes, not continuous angles or canvas pixel geometry.','Four previously precision-adjudicated Adam cases show only their existing checked training markers; no unchecked curve is exported.'],'records':checks}
out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('records','scope','limitations','source_sha256')},indent=2))
signal.alarm(0)
raise SystemExit(0 if report['passed'] else 1)
