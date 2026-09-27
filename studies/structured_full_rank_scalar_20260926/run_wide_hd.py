"""Width2048 dense HD/Gaussian comparison. Never runs on import."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib,json,platform,shutil,subprocess,time,traceback
from pathlib import Path
import numpy as np
import scipy
import dense_compare as dense
from circle_tasks import BY_NAME,TASKS,directions,task_manifest
from dense_wide_integrator import integrate

HERE=Path(__file__).resolve().parent
METHODS=('gaussian','gaussian_control','hd')

def digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

def predict(state,angles):
    u=directions(angles)
    return np.concatenate([dense._forward(state,u[j:j+256]).output for j in range(0,len(u),256)])

def run_one(job):
    started=time.monotonic();out=Path(job['output'])
    key=f"{job['task']}__n{job['width']}__s{job['seed']:02d}__{job['method']}"
    status={'key':key,**job}
    try:
        if time.time()>job['deadline']:raise TimeoutError('campaign deadline before start')
        task=BY_NAME[job['task']];u,y=task.data()
        state=dense.initialize(job['width'],job['seed'],job['method'])
        t=0.;history=[];segments=[];result=None
        for horizon in (3000.,10000.):
            result=integrate(state,u,y,time_cap=horizon-t,rtol=job['rtol'],atol=job['atol'],
                target_train_mse=job['target'],deadline=job['deadline'],max_step=10.)
            shifted={k:np.asarray(v).copy() for k,v in result.history.items()}
            shifted['time']+=t
            history.extend(zip(shifted['time'].tolist(),shifted['train_mse'].tolist()))
            segment={'start_time':t,'end_time':t+result.time,'nfev':result.nfev,
              'nsteps':result.nsteps,'nreject':result.nreject,'stop_reason':result.stop_reason,
              'max_loss_rise':result.max_loss_rise,'settings':result.settings}
            segments.append(segment)
            bracket=result.first_target_bracket
            if bracket is not None:bracket=[t+float(b) for b in bracket]
            t+=result.time;state=result.state
            if result.stop_reason!='time_cap':break
        f=dense._forward(state,u).output
        mse=float(np.mean((f-y)**2))
        valid_stop=result.stop_reason in ('target','time_cap')
        fitted=bool(valid_stop and mse<=job['target']*(1+1e-7))
        angles=2*np.pi*np.arange(job['grid'])/job['grid']
        circle=predict(state,angles)
        arrays={'angles':angles,'prediction':circle,'train_angles':np.asarray(task.angles),
          'train_labels':y,'train_prediction':f,'history':np.asarray(history),
          'final_w':state.w,'final_W':state.W,'final_c':state.c}
        filename=out/(key+'.npz');np.savez(filename,**arrays)
        status.update(status='ok' if valid_stop else 'unresolved',fitted=fitted,time=t,train_mse=mse,first_target_bracket=bracket,
          segments=segments,nfev=sum(s['nfev'] for s in segments),
          max_loss_rise=max(s['max_loss_rise'] for s in segments),
          stop_reason=result.stop_reason,data_file=filename.name,data_sha256=digest(filename),
          wall_seconds=time.monotonic()-started)
    except Exception as exc:
        status.update(status='failed',error=repr(exc),traceback=traceback.format_exc(),
                      wall_seconds=time.monotonic()-started)
    (out/(key+'.json')).write_text(json.dumps(status,indent=2,allow_nan=False)+'\n')
    return {k:status.get(k) for k in ('key','status','fitted','time','train_mse','wall_seconds','error')}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',required=True);p.add_argument('--width',type=int,default=2048)
    p.add_argument('--tasks',nargs='+',default=[t.name for t in TASKS],choices=list(BY_NAME))
    p.add_argument('--methods',nargs='+',default=list(METHODS),choices=METHODS)
    p.add_argument('--seeds',nargs='+',type=int,default=list(range(12)))
    p.add_argument('--rtol',type=float,default=1e-5);p.add_argument('--atol',type=float,default=1e-8)
    p.add_argument('--target',type=float,default=1e-4);p.add_argument('--grid',type=int,default=4096)
    p.add_argument('--workers',type=int,default=8);p.add_argument('--wall-minutes',type=float,default=110.)
    args=p.parse_args();out=Path(args.output).resolve();out.mkdir(parents=True,exist_ok=False)
    files=['dense_compare.py','dense_wide_integrator.py','circle_tasks.py','run_wide_hd.py','WIDE_HD_PROTOCOL.md']
    snap=out/'source_snapshot';snap.mkdir()
    sources={}
    for name in files:
        shutil.copyfile(HERE/name,snap/name);sources[name]=digest(HERE/name)
    config=vars(args)|{'output':str(out),'started':time.time(),'deadline':time.time()+args.wall_minutes*60,
      'command':__import__('sys').argv,'task_definitions':task_manifest(),'sources':sources,
      'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,
      'cpu_count':os.cpu_count(),'blas_threads':1,'git_head':subprocess.check_output(
          ['git','rev-parse','HEAD'],text=True).strip()}
    (out/'manifest.json').write_text(json.dumps(config,indent=2)+'\n')
    jobs=[{'task':task,'seed':seed,'method':method,'width':args.width,'rtol':args.rtol,
      'atol':args.atol,'target':args.target,'grid':args.grid,'output':str(out),
      'deadline':config['deadline']} for seed in args.seeds for task in args.tasks for method in args.methods]
    print(json.dumps({'jobs':len(jobs),'output':str(out)}),flush=True)
    started=time.monotonic();done=0
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        fs=[pool.submit(run_one,j) for j in jobs]
        for f in as_completed(fs):
            r=f.result();done+=1
            with (out/'progress.jsonl').open('a') as stream:stream.write(json.dumps(r)+'\n')
            if done%3==0 or r['status']!='ok':
                print(json.dumps({'completed':done,'total':len(jobs),'elapsed':time.monotonic()-started,'last':r}),flush=True)
    (out/'completion.json').write_text(json.dumps({'completed':done,'total':len(jobs),'wall_seconds':time.monotonic()-started})+'\n')
    (out/'artifact_hashes.json').write_text(json.dumps({p.name:digest(p) for p in out.iterdir() if p.is_file()},indent=2)+'\n')

if __name__=='__main__':main()
