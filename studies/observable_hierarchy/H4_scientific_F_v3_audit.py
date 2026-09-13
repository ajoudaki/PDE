"""Independent F review: frozen integrity, all archive values, direct algebra.
No initialization or research trajectories. Numerical CPU hard cap 250 seconds.
"""
from pathlib import Path
from fractions import Fraction
from decimal import Decimal
import os,sys,json,hashlib,resource,time,runpy,contextlib,io,re
ROOT=Path('/home/amir/Codes/PDE'); ED=ROOT/'data/generated/observable_hierarchy/H4_candidate_v3'; OUT=ROOT/'data/generated/observable_hierarchy/H4_scientific_F_v3';ST=ROOT/'studies/observable_hierarchy'
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1');sys.dont_write_bytecode=True
resource.setrlimit(resource.RLIMIT_AS,(4*2**30,)*2);resource.setrlimit(resource.RLIMIT_CPU,(250,)*2)
sys.path.insert(0,str(ED/'code'))
import numpy as np
from pde import observable_solver as so
from pde.observable_arithmetic import Arithmetic
from pde.observable_fixed import Fixed
from pde.observable_laws import OrthogonalArcLaw,DyadicRadius,RationalRadius,supported_law,_working_fraction,_fraction_from_record
from scripts import analyze_observable_horizon as an,validate_observable_horizon as worker
start=time.process_time();report={'checks':[]};records=[]
def H(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(ok,label):
 if not ok:raise AssertionError(label)
 report['checks'].append(label)
manifest=ST/'H4_review_manifest_v3.json';check(H(manifest)=='06132871ed70c3c13651a3fbb1f8e76d13582301237acb811f50756bdb223d02','frozen manifest digest')
m=json.loads(manifest.read_text());inventory=[]
for f in m['files']:
 p=ROOT/f['path'];payload=p.read_bytes();check(hashlib.sha256(payload).hexdigest()==f['sha256'] and len(payload)==f['bytes'],'file '+f['path']);inventory.append(dict(**f,lines=payload.count(b'\n') if p.suffix in ('.py','.md') else None))
(OUT/'inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
em=json.loads((ED/'edition_manifest.json').read_text())
for f in em['files']:check(H(ED/f['destination'])==f['destination_sha256'],'edition destination '+f['destination'])
section=(ST/'H4_proposed_section_v2.md').read_bytes();assembled=(ED/'docs/global_nonlinear.md').read_bytes();insert=b'\n\n'+section.rstrip();check(assembled.count(insert)==1,'one exact insertion');old=assembled.replace(insert,b'',1)
check(hashlib.sha256(old).hexdigest()=='77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932','every preexisting chapter byte preserved')
dep=json.loads((ST/'H4_dependency_manifest.json').read_text());packet=(ST/'H4_dependencies.md').read_bytes()
for unit in dep['units']:
 payload=old if unit['source']=='docs/global_nonlinear.md' else (ED/unit['source']).read_bytes()
 check(hashlib.sha256(payload).hexdigest()==unit['source_sha256'],'dependency whole provenance '+unit['scope'])
 excerpt=b''.join(payload.splitlines(keepends=True)[unit['first_line']-1:unit['last_line']]);check(hashlib.sha256(excerpt).hexdigest()==unit['excerpt_sha256'],'complete excerpt '+unit['scope']);check(excerpt in packet,'packet exact inclusion '+unit['scope'])
check(H(ED/'code/README.md')==H(ST/'H4_code_readme_v3.md'),'complete code guide duplicate');check(H(ED/'docs/README.md')==H(ST/'H4_docs_readme.md'),'complete docs guide duplicate')
cert=ROOT/'data/generated/observable_hierarchy/H4_full_tests_v1/reference_certificate.py'
stream=io.StringIO()
with contextlib.redirect_stdout(stream):cv=runpy.run_path(str(cert))
report['rational_certificate']=stream.getvalue().strip();check(cv['qlo']>Fraction(39,100) and cv['rlo']>Fraction(3,5),'rational certificate strict bounds')
planpath=ED/'code/validation/observable_horizon_plan.json';plan=json.loads(planpath.read_text());runs=ROOT/'data/generated/observable_hierarchy/H4_author_runs_v1'
summary=json.loads((ROOT/'data/generated/observable_hierarchy/H4_author_analysis_v1/summary.json').read_text());fresh=an.analyze(planpath,runs)
for k,v in fresh.items():check(v==summary[k],'recomputed analyzer field '+k)
check(an.markdown(summary)==(ROOT/'data/generated/observable_hierarchy/H4_author_analysis_v1/summary.md').read_text(),'markdown reproduced exactly')
report['aggregate']=fresh['aggregate'];report['comparisons']=fresh['comparisons'];report['archive_statistics']={'observations':0,'npz_members':0,'working_observation_scalars':0,'checkpoint_scalars':0,'exact_float_views':0,'max_direct_checkpoint_observation_error':0,'max_independent_loss_rms_error':0}
ast=report['archive_statistics']
def decode(record,digits,backend):
 vals=record['values'];check(len(vals)==int(np.prod(record['shape'],dtype=int)),'encoded shape count')
 if digits is None:arr=np.array([float.fromhex(x) for x in vals])
 elif backend=='rational':arr=np.array([float(Fraction(int(x,16),10**digits)) for x in vals])
 else:arr=np.array([float(Decimal(x)) for x in vals])
 check(np.isfinite(arr).all(),'all decoded entries finite');return arr.reshape(record['shape'])
def direct(state,data,circle):
 b1,g,w,p1,b2,c,p2,M,D=[np.asarray(getattr(state,k),float) for k in worker.STATE_KEYS]
 u,y,dp=[np.asarray(getattr(data,k),float) for k in worker.DATA_KEYS]
 def fields(inputs,current):
  first=np.tanh((w if current else g)@inputs.T)
  # Direct explicit population sums, with an independently written middle action.
  coef=np.einsum('pj,p,pa->ja',b1,p1,first)
  second=np.tanh(np.einsum('qi,ij,ja->qa',b2,M if current else D,coef))
  return first,second,np.einsum('q,q,qa->a',p2,c,second)
 h1,h2,f=fields(u,True);i1,i2,_=fields(u,False)
 return dict(first_pairs=np.stack([i1,h1],axis=-1),second_pairs=np.stack([i2,h2],axis=-1),prediction=fields(circle,True)[2],training_prediction=f,loss=dp@((f-y)**2),rms1=np.sqrt(np.einsum('p,a,pa->',p1,dp,(h1-i1)**2)),rms2=np.sqrt(np.einsum('q,a,qa->',p2,dp,(h2-i2)**2)))
for cfg in plan['configurations']:
 folder=runs/cfg['id'];rec=json.loads((folder/'record.json').read_text());rrow={'id':cfg['id']}
 check(rec['configuration']==cfg and rec['plan_sha256']==H(planpath),'run provenance '+cfg['id']);check(rec['status']=='operational_pass','operation '+cfg['id'])
 for k,h in rec['source_hashes'].items():check(H(ED/'code/pde'/k)==h,'producer module '+cfg['id']+'/'+k)
 check(H(ED/'code/scripts/validate_observable_horizon.py')==rec['producer_sha256'],'producer hash '+cfg['id']);check(set(rec['thread_environment'].values())=={'1'},'worker thread record '+cfg['id'])
 check(all(rec['restart_comparison'].values()) and rec['restart_prediction_exact'],'all declared restart comparisons '+cfg['id'])
 for name,h in rec['outputs'].items():check(H(folder/name)==h,'author artifact digest '+cfg['id']+'/'+name)
 # A complete read and recursive field walk occurs even for descriptive fields.
 def walk(x):
  if isinstance(x,dict):return sum(walk(k)+walk(v) for k,v in x.items())
  if isinstance(x,list):return sum(map(walk,x))
  if isinstance(x,float):check(np.isfinite(x),'record finite scalar')
  return 1
 rrow['record_leaf_count']=walk(rec)
 for item in rec['observations']:
  exact=json.loads((folder/item['exact_json']).read_text());check(exact['format']==worker.OBSERVATION_FORMAT and Fraction(exact['time'])==Fraction(item['time']),'observation header')
  ast['observations']+=1
  with np.load(folder/item['npz'],allow_pickle=False) as archive:
   check(set(archive.files)==set(exact['arrays']),'all NPZ member names')
   data={}
   for key,value in exact['arrays'].items():
    arr=decode(value,exact['digits'],exact['backend']);got=archive[key];check(arr.shape==got.shape and arr.tobytes()==got.tobytes(),'exact scalar float view '+cfg['id']+'/'+item['time']+'/'+key);data[key]=got.copy();ast['npz_members']+=1;ast['working_observation_scalars']+=arr.size;ast['exact_float_views']+=1
  loss=float(np.sum(data['input_weights']*(data['training_prediction']-data['labels'])**2))
  errors=[abs(loss-float(data['loss']))]
  for l in (1,2):
   n='first' if l==1 else 'second';pair=data[n+'_pairs'];rms=float(np.sqrt(np.einsum('p,a,pa->',data[n+'_weights'],data['input_weights'],(pair[:,:,1]-pair[:,:,0])**2)))
   errors.append(abs(rms-float(data['rms'+str(l)])))
  ast['max_independent_loss_rms_error']=max(ast['max_independent_loss_rms_error'],*errors);check(max(errors)<2e-11,'independent all-pair algebra')
  if item['time']=='0':check(np.array_equal(data['first_pairs'][:,:,0],data['first_pairs'][:,:,1]) and np.array_equal(data['second_pairs'][:,:,0],data['second_pairs'][:,:,1]),'initial pairs exact')
  check((folder/item['exact_json']).stat().st_size==item['exact_bytes'] and (folder/item['npz']).stat().st_size==item['npz_bytes'],'observation bytecounts')
 for filename,obsindex,sizekey in [('midpoint_restart.json',4,'checkpoint_bytes'),('final_restart.json',5,'final_checkpoint_bytes')]:
  saved=json.loads((folder/filename).read_text());check((folder/filename).stat().st_size==rec[sizekey],'checkpoint bytecount')
  for group in ('state','data'):
   for value in saved[group].values():ast['checkpoint_scalars']+=decode(value,saved['digits'],saved['backend']).size
  state,law=so.load_restart(folder/filename);check(worker.frozen_signature(state,law)==rec['frozen_signature_initial'],'decoded checkpoint frozen signature '+cfg['id']+'/'+filename)
  check(state.metadata==rec['initialization_metadata'] and law.metadata==rec['law_metadata'],'all checkpoint metadata')
  check(sum(getattr(state,k).size for k in worker.STATE_KEYS)==rec['workspace_final']['state_scalars'],'state scalar counts')
  check(so.state_bytes(state)['arrays']==rec['state_bytes_final']['arrays'],'state bytecount')
  rule,limits=worker.build_law(plan,cfg);regenerated=rule.quadrature(cfg['nodes_per_arc'],state.arithmetic,limits=limits)
  for key in worker.DATA_KEYS:check(worker.encode_array(getattr(regenerated,key),state.arithmetic)==saved['data'][key],'exact regenerated law array '+key)
  check(regenerated.metadata==law.metadata,'regenerated complete law metadata')
  with np.load(folder/rec['observations'][obsindex]['npz'],allow_pickle=False) as a:
   ds=direct(state,law,a['circle'])
   errors=[float(np.max(np.abs(np.asarray(v)-a[k]))) for k,v in ds.items()];ast['max_direct_checkpoint_observation_error']=max(ast['max_direct_checkpoint_observation_error'],*errors);check(max(errors)<1e-11,'direct checkpoint recomputation '+cfg['id']+'/'+filename)
  if filename=='final_restart.json':
   rrow.update(loss=rec['loss_final'],rms1=rec['rms1'],rms2=rec['rms2'],cpu=rec['total_seconds']['cpu'],rss=rec['peak_rss_bytes'],collapse=law.metadata['collapsed_to_reference'],scope=law.metadata['scientific_scope'],state_scalars=sum(getattr(state,k).size for k in worker.STATE_KEYS),record_fields=list(rec))
 log=json.loads((runs/(cfg['id']+'.log')).read_text());check(log['status']==rec['status'] and log['total_seconds']==rec['total_seconds'],'complete worker log')
 records.append(rrow)
supervisor=json.loads((runs/'supervisor.json').read_text());check(supervisor['worker_sha256']==H(ED/'code/scripts/validate_observable_horizon.py') and supervisor['supervisor_sha256']==H(ED/'code/scripts/run_observable_validation.py'),'supervisor source provenance')
check(len(supervisor['configurations'])==14 and supervisor['status']=='operational_pass','supervisor complete14')
for row in supervisor['configurations']:
 check(row['exit_code']==0 and row['stopped'] is None and row['status']=='operational_pass','supervisor every configuration');check(row['record_sha256']==H(runs/row['id']/'record.json'),'supervisor record binding')
report['runs']=records;report['supervisor_cpu']=supervisor['total_cpu_seconds'];report['cpu_seconds']=time.process_time()-start;report['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024;report['status']='PASS'
(OUT/'audit_results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ('checks','runs','comparisons')},indent=2))
