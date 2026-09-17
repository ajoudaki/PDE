"""Execute the fixed sparse-circle cases with two bounded GPU workers."""
import argparse, hashlib, json, os
from pathlib import Path
import shutil, subprocess, sys, time
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
GENERATED=ROOT/'data/generated/closure_circle_spectral_mechanism'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def write(path,value):
    path=Path(path)
    if path.exists():raise FileExistsError(path)
    temporary=path.with_name(path.name+'.tmp')
    with temporary.open('x') as f:json.dump(value,f,indent=2,allow_nan=False)
    temporary.rename(path)
def circle(n):
    a=2*np.pi*np.arange(n)/n
    return np.column_stack((np.cos(a),np.sin(a)))

def cases():
    out=[]
    def add(name,kind,delta,rotation,amplitude,angles,labels,orders,wave):
        out.append(dict(name=name,kind=kind,delta=delta,rotation=rotation,amplitude=amplitude,
                    angles_degrees=list(np.asarray(angles,dtype=float)),labels=list(np.asarray(labels,dtype=float)),
                    orders=orders,wave=wave))
    for delta in (15,30,60,90,150):
        add(f'pair_d{delta}_r45','pair',delta,45,1,45+np.array([-delta/2,delta/2]),[-1,1],[1,2,3,5],'pairs')
    for delta in (30,90):
        add(f'pair_d{delta}_r0','pair',delta,0,1,[-delta/2,delta/2],[-1,1],[1,2,3,5],'pairs')
        add(f'pair_d{delta}_r45_a02','pair',delta,45,.2,45+np.array([-delta/2,delta/2]),[-.2,.2],[1,3,5],'multi')
    for delta in (20,40,60):
        add(f'triple_d{delta}','triple',delta,45,1,45+np.array([-delta,0,delta]),[1,-1,1],[1,3,5],'multi')
    for delta in (15,30,45):
        add(f'quad_d{delta}','quad',delta,45,1,45+delta*np.array([-1.5,-.5,.5,1.5]),[-1,1,-1,1],[1,3,5],'multi')
    return out

def configurations():
    out=[]
    for case in cases():
        for order in case['orders']:
            for control in ('main','fine','half'):
                enabled=control=='main' or case['name'] in ('pair_d30_r45','triple_d40','quad_d30') or (case['name']=='pair_d90_r45' and order!=2 and control=='fine')
                if not enabled:continue
                out.append(dict(case,order=order,control=control,Q=8192 if control=='fine' else 4096,
                            P=4096 if control=='fine' else 2048,h=.01 if control=='half' else .02,
                            t_min=100,t_max=600,obs_dt=10,id=f"{case['name']}_N{order}_{control}"))
    assert len(out)==75
    return out

def prepare(output):
    output=Path(output).resolve();assert output.is_relative_to(GENERATED)
    output.mkdir()
    sources=[HERE/f for f in ('PLAN.md','RUN.py','ENGINE.py','ENGINE_CHECK.py','NTK.py','NTK_CHECK.py')]
    sources += [ROOT/'code/pde'/f for f in ('observable_solver.py','observable_initialization.py','observable_words.py','observable_arithmetic.py','observable_fixed.py')]
    write(output/'manifest.json',dict(created=time.time(),command=[sys.executable,*sys.argv],cwd=str(ROOT),
          head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
          sources={str(p):sha(p) for p in sources},configurations=configurations(),
          budget=dict(scientific_seconds=1200,worker_seconds=120,output_bytes=600*2**20,minimum_free_bytes=int(1.5*2**30))))
    print(output,flush=True)

def limits(output,started,budget):
    if time.time()-started>budget['scientific_seconds']:return 'scientific_wall_limit'
    if shutil.disk_usage(output).free<budget['minimum_free_bytes']:return 'free_disk_limit'
    if sum(p.stat().st_size for p in GENERATED.rglob('*') if p.is_file())>budget['output_bytes']:return 'study_output_limit'
    return None

def worker(output,assignment,device):
    import torch, ENGINE
    torch.set_num_threads(1);torch.set_num_interop_threads(1)
    torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
    output=Path(output);manifest=json.loads((output/'manifest.json').read_text())
    for p,h in manifest['sources'].items():assert sha(p)==h,(p,'changed_source')
    start=json.loads((output/'clock.json').read_text())['start'];budget=manifest['budget']
    jobs=json.loads(Path(assignment).read_text());cache={};panel=circle(720);dense=circle(1440);kp=circle(128)
    environment=dict(python=sys.version,numpy=np.__version__,torch=torch.__version__,device=device,
                     gpu=torch.cuda.get_device_name(device),threads=torch.get_num_threads())
    for config in jobs:
        reason=limits(output,start,budget)
        if reason:print(json.dumps(dict(event='worker_stop',reason=reason)),flush=True);return
        directory=output/config['id'];directory.mkdir();began=time.time()
        write(directory/'config.json',config)
        write(directory/'started.json',dict(unix_time=began,pid=os.getpid(),device=device))
        try:
            key=config['order'],config['Q'],config['P']
            if key not in cache:cache[key]=ENGINE.initialize(*key,device=device)
            e=cache[key].clone();initial=cache[key]
            angles=np.deg2rad(config['angles_degrees']);u=np.column_stack((np.cos(angles),np.sin(angles)))
            y=np.array(config['labels']);p=np.ones(len(y))/len(y);data=e.prepare_data(u,y,p)
            frozen_train=initial.tangent_blocks(u)[1]
            frozen_cross=np.concatenate([initial.tangent_blocks(block,u)[1] for block in np.array_split(dense,6)])
            k0=initial.tangent_blocks(kp)
            times=[];preds=[];train=[];losses=[];settled=False;stop='horizon_cap'
            total=int(round(config['t_max']/config['h']));interval=int(round(config['obs_dt']/config['h']))
            e._validate_state()
            for step in range(total+1):
                if step%interval==0:
                    now=round(step*config['h'],8);f=e.predict(panel);ft=e.predict(u);loss=float(p@((ft-y)**2))
                    times.append(now);preds.append(f);train.append(ft);losses.append(loss)
                    if len(losses)>1 and loss-losses[-2]>1e-6*max(1,config['amplitude']**2):raise ValueError('loss_increase')
                    if now>=config['t_min'] and len(preds)>=5:
                        scale=max(config['amplitude'],float(np.max(np.abs(f))))
                        drifts=[float(np.max(np.abs(preds[-1]-preds[-3]))),float(np.max(np.abs(preds[-3]-preds[-5])))]
                        settled=loss<=1e-6*config['amplitude']**2 and max(drifts)<=.002*scale
                        if settled:stop='mild_settling';break
                    reason=limits(output,start,budget)
                    if reason or time.time()-began>budget['worker_seconds']:
                        stop=reason or 'trajectory_wall_limit';break
                if step<total:e.step_data(data,config['h'])
            e._validate_state();final=e.predict(dense);diag=e.diagnostics(dense,u,p)
            kfinal=e.tangent_blocks(kp)
            payload=dict(times=np.array(times),predictions=np.array(preds),train_predictions=np.array(train),loss=np.array(losses),
                    dense_predictions=final,train_inputs=u,labels=y,weights=p,angles=angles,
                    frozen_kernel_train=frozen_train,frozen_kernel_cross=frozen_cross,
                    kernel_circle_initial=k0,kernel_circle_final=kfinal,
                    singular_values_initial=np.linalg.svd(initial.M.cpu().numpy(),compute_uv=False),
                    singular_values_final=np.linalg.svd(e.M.cpu().numpy(),compute_uv=False),**diag)
            e.save_npz(directory/'state.npz',metadata=dict(config=config,source_sha256=sha(HERE/'ENGINE.py')),data=data)
            restored=ENGINE.load_npz(directory/'state.npz',device=device)
            replay=float(np.max(np.abs(restored.predict(dense)-final)))
            assert replay<=1e-12
            assert all(np.all(np.isfinite(v)) for v in payload.values())
            odd=float(np.max(np.abs(final[:720]+final[720:])))
            gram_min=min(float(np.linalg.eigvalsh(diag[f'hidden{layer}_gram_current']).min()) for layer in (1,2))
            assert odd<1e-10 and gram_min>=-1e-8
            with (directory/'observations.npz').open('xb') as f:np.savez_compressed(f,**payload)
            complete=stop in ('horizon_cap','mild_settling')
            record=dict(status='complete' if complete else 'interrupted',stop_reason=stop,settled=settled,last_time=times[-1],
                        final_loss=losses[-1],config=config,environment=environment,elapsed=time.time()-began,
                        checks=dict(replay_max=replay,oddness_max=odd,gram_min_eigenvalue=gram_min),
                        source_sha256=sha(HERE/'ENGINE.py'),manifest_sha256=sha(output/'manifest.json'),
                        outputs={f:sha(directory/f) for f in ('state.npz','observations.npz','config.json')})
            write(directory/'record.json',record)
            print(json.dumps(dict(event='finish',id=config['id'],time=times[-1],loss=losses[-1],settled=settled,stop=stop,seconds=record['elapsed'])),flush=True)
            if not complete:return
        except Exception as error:
            write(directory/'failure.json',dict(error=repr(error),elapsed=time.time()-began,config=config))
            raise

def wave(output,name):
    output=Path(output).resolve();m=json.loads((output/'manifest.json').read_text())
    if not (output/'clock.json').exists():write(output/'clock.json',dict(start=time.time()))
    jobs=[c for c in m['configurations'] if c['wave']==name]
    buckets=[[],[]];cost=[0.,0.]
    for config in sorted(jobs,key=lambda c:(c['control']!='main',c['name'],c['order'])):
        i=int(np.argmin(cost));buckets[i].append(config)
        cost[i]+={1:1,2:1.2,3:1.5,5:3}[config['order']]*(config['P']/2048)*(.02/config['h'])
    processes=[];handles=[];begin=time.time()
    for i,bucket in enumerate(buckets):
        assignment=output/f'{name}_worker{i}.json';write(assignment,bucket)
        log=(output/f'{name}_worker{i}.log').open('x');handles.append(log)
        command=[sys.executable,'-B',str(HERE/'RUN.py'),'--worker',str(assignment),'--output',str(output),'--device',f'cuda:{i}']
        processes.append(subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,cwd=ROOT))
    reason=None;started=json.loads((output/'clock.json').read_text())['start']
    try:
        while any(p.poll() is None for p in processes):
            reason=limits(output,started,m['budget'])
            if any(p.poll() not in (None,0) for p in processes):reason='worker_failure'
            for config in jobs:
                d=output/config['id']
                if (d/'started.json').exists() and not (d/'record.json').exists() and not (d/'failure.json').exists():
                    if time.time()-json.loads((d/'started.json').read_text())['unix_time']>m['budget']['worker_seconds']:
                        reason='trajectory_wall_limit:'+config['id']
            if reason:break
            time.sleep(.25)
    finally:
        if reason:
            for p in processes:
                if p.poll() is None:p.terminate()
        for p in processes:
            try:p.wait(timeout=5)
            except subprocess.TimeoutExpired:p.kill();p.wait()
    codes=[p.returncode for p in processes]
    for h in handles:h.close()
    records={};missing=[]
    for c in jobs:
        r=output/c['id']/'record.json'
        if r.exists():records[c['id']]=json.loads(r.read_text())['status']
        else:missing.append(c['id'])
    write(output/f'{name}_batch.json',dict(exit_codes=codes,records=records,missing=missing,elapsed=time.time()-begin,stop_reason=reason,
                   complete=not missing and all(v=='complete' for v in records.values()) and not any(codes) and reason is None))
    print(json.dumps(dict(wave=name,exit_codes=codes,records=len(records),missing=len(missing))),flush=True)

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--output',required=True);a.add_argument('--prepare',action='store_true');a.add_argument('--wave',choices=['pairs','multi']);a.add_argument('--worker');a.add_argument('--device',default='cuda:0');args=a.parse_args()
    if args.prepare:prepare(args.output)
    elif args.worker:worker(args.output,args.worker,args.device)
    else:wave(args.output,args.wave)
