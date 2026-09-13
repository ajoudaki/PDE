import hashlib, json, os, resource, subprocess, sys, time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(120,120))
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
sys.dont_write_bytecode=True
scratch=Path(__file__).resolve().parent
old=scratch.parent/'H3_v2_edition_v2'; new=scratch.parent/'H3_v2_edition_v3'
os.environ['PYTHONDONTWRITEBYTECODE']='1';os.environ['PYTHONPATH']=str(new/'code')
sys.path.insert(0,str(new/'code'))
import numpy as np
from pde.observable_solver import load_restart, state_bytes
start=time.process_time();runroot=old/'data/established/independent_v2_runs'
plan=json.loads((old/'code/validation/observable_solver_plan.json').read_text())
rows=[]
for c in plan['configurations']:
    folder=runroot/c['id'];record=json.loads((folder/'record.json').read_text())
    assert record['configuration']==c
    for f,h in record['outputs'].items():assert hashlib.sha256((folder/f).read_bytes()).hexdigest()==h
    current,data=load_restart(folder/'final_restart.json');mid,middata=load_restart(folder/'midpoint_restart.json')
    for k in ('b1','g','p1','b2','p2','D'):assert np.array_equal(getattr(current,k),getattr(mid,k))
    for k in ('inputs','labels','probabilities'):assert np.array_equal(getattr(data,k),getattr(middata,k))
    keys=('b1','g','w','p1','b2','c','p2','M','D')
    assert set(vars(current))==set(keys)|{'arithmetic','metadata'}
    a={k:np.asarray(getattr(current,k),float) for k in keys}
    assert all(np.isfinite(v).all() for v in a.values())
    u=np.asarray(data.inputs,float);weights=np.asarray(data.probabilities,float)
    h0=np.tanh(a['g']@u.T);h=np.tanh(a['w']@u.T)
    z0=np.tanh(a['b2']@(a['D']@(a['b1'].T@(a['p1'][:,None]*h0))))
    z=np.tanh(a['b2']@(a['M']@(a['b1'].T@(a['p1'][:,None]*h))))
    with np.load(folder/'observations.npz',allow_pickle=False) as archive:
        assert all(np.isfinite(archive[k]).all() for k in archive.files)
        errors={'first_pairs':float(np.max(np.abs(archive['first_pairs']-np.stack([h0,h],axis=2)))),
                'second_pairs':float(np.max(np.abs(archive['second_pairs']-np.stack([z0,z],axis=2))))}
        panelh=np.tanh(a['w']@archive['circle'].T)
        pred=a['p2']@(a['c'][:,None]*np.tanh(a['b2']@(a['M']@(a['b1'].T@(a['p1'][:,None]*panelh)))))
        errors['prediction']=float(np.max(np.abs(pred-archive['prediction'])))
        shapes={k:list(archive[k].shape) for k in archive.files}
    for layer,prior,value in ((1,h0,h),(2,z0,z)):
        rms=float(np.sqrt(a['p'+str(layer)]@((value-prior)**2)@weights))
        errors['rms'+str(layer)]=abs(rms-record['rms'+str(layer)])
    assert max(errors.values())<1e-12
    assert state_bytes(current)==record['state_bytes_final']
    rows.append(dict(id=c['id'],shapes=shapes,maximum_errors=errors,
                     frozen_marks_equal=True,state_bytes=state_bytes(current),
                     total_state_scalars=sum(v.size for v in a.values())))
command=[sys.executable,'-B',str(new/'code/scripts/analyze_observable_solver.py'),
         '--plan',str(old/'code/validation/observable_solver_plan.json'),
         '--runs',str(runroot),'--output',str(scratch/'reanalysis'),'--recount-state']
with (scratch/'reanalysis.log').open('x') as log:
    child=subprocess.run(command,cwd=scratch,stdout=log,stderr=subprocess.STDOUT,env=os.environ)
assert child.returncode==0
fresh=json.loads((scratch/'reanalysis/summary.json').read_text())
prior=json.loads((old/'data/established/independent_v2_analysis/summary.json').read_text())
volatile=['postprocessing_cpu_seconds']
for key in volatile:fresh.pop(key);prior.pop(key)
assert fresh==prior
assert (scratch/'reanalysis/summary.md').read_bytes()==(old/'data/established/independent_v2_analysis/summary.md').read_bytes()
usage=resource.getrusage(resource.RUSAGE_CHILDREN)
result=dict(rows=rows,command=command,analysis_exit_code=child.returncode,
            complete_summary_equal_except=volatile,markdown_summary_byte_identical=True,
            cpu_seconds=time.process_time()-start+usage.ru_utime+usage.ru_stime,
            peak_rss_bytes=max(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,usage.ru_maxrss)*1024)
(scratch/'evidence_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
