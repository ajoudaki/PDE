"""Actual dense networks for the frozen NET_PLAN; no closure in the trainer."""
import argparse, hashlib, json, os, subprocess, sys, time, shutil, traceback
from pathlib import Path
import numpy as np
import torch

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'code'))
from pde import finite_network as ref

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
    return h.hexdigest()
def write_json(path,obj):
    path=Path(path);tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n');tmp.replace(path)
def source_hashes():
    paths=[HERE/'NET_RUN.py',HERE/'NET_PLAN.md',ROOT/'code/pde/finite_network.py',ROOT/'docs/NOTATION.md']
    return {str(p.relative_to(ROOT)):sha(p) for p in paths}
def setup(device):
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False
    if device.startswith('cuda'):torch.cuda.set_device(torch.device(device))

class Network:
    def __init__(self,arrays,device='cpu',dtype=torch.float64):
        self.W,self.V,self.c=[torch.as_tensor(x,dtype=dtype,device=device).clone() for x in arrays]
        self.n=len(self.c);self.device=device;self.dtype=dtype
    @classmethod
    def initialize(cls,n,seed,device,dtype):
        p=ref.initialize(n,2,2,seed=seed)
        return cls((*p.weights,p.readout),device,dtype)
    def fields(self,u,state=None):
        W,V,c=self.state() if state is None else state
        h1=torch.tanh(W@u);h2=torch.tanh(V@h1);f=c@h2/self.n
        return h1,h2,f
    def state(self):return self.W,self.V,self.c
    def rhs(self,u,y,state=None):
        W,V,c=self.state() if state is None else state
        h1,h2,f=self.fields(u,(W,V,c));q=(f-y)/len(y)
        d2=c[:,None]*(1-h2*h2);d1=(V.T@d2)*(1-h1*h1)
        return -2*(d1*q)@u.T,(-2/self.n)*(d2*q)@h1.T,-2*h2@q
    @torch.no_grad()
    def step(self,u,y,h):
        old=self.state();v=self.rhs(u,y)
        stage=tuple(a+h*b for a,b in zip(old,v));v2=self.rhs(u,y,stage)
        for a,b,d in zip(old,v,v2):a.add_(b,alpha=h/2).add_(d,alpha=h/2)
    @torch.no_grad()
    def predict(self,angles,block=256):
        angles=np.asarray(angles);pieces=[]
        for j in range(0,len(angles),block):
            t=angles[j:j+block];u=torch.as_tensor(np.array([np.cos(t),np.sin(t)]),device=self.device,dtype=self.dtype)
            pieces.append(self.fields(u)[2].cpu().numpy().astype(float))
        return np.concatenate(pieces)
    def arrays(self):return tuple(a.detach().cpu().numpy() for a in self.state())
    def tensor_inputs(self,angles):
        t=np.asarray(angles);return torch.as_tensor(np.array([np.cos(t),np.sin(t)]),device=self.device,dtype=self.dtype)

def checks(device,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);setup(device);begun=time.time();errors={}
    rng=np.random.default_rng(117)
    for n in [5,11]:
        arrays=(rng.normal(size=(n,2)),rng.normal(size=(n,n))/np.sqrt(n),rng.normal(size=n))
        a=np.array([.1,.8,2.2]);u=np.array([np.cos(a),np.sin(a)]);y=np.array([1.,-.7,.2]);p=ref.Parameters(arrays[:2],arrays[2])
        net=Network(arrays,device);ut=net.tensor_inputs(a);yt=torch.as_tensor(y,dtype=net.dtype,device=device)
        f=net.fields(ut);rf=ref.forward(p,np.sqrt(2)*u)
        errors[f'{n}_forward']=float(max(np.max(abs(f[0].cpu().numpy()-rf.hidden[0])),np.max(abs(f[1].cpu().numpy()-rf.hidden[1])),np.max(abs(f[2].cpu().numpy()-rf.output))))
        rv=ref.flow_velocity(p,np.sqrt(2)*u,y);v=net.rhs(ut,yt)
        errors[f'{n}_rhs']=float(max(np.max(abs(x.cpu().numpy()-z)) for x,z in zip(v,(*rv.weights,rv.readout))))
        ag=[x.clone().requires_grad_() for x in net.state()];pred=ag[2]@torch.tanh(ag[1]@torch.tanh(ag[0]@ut))/n
        grads=torch.autograd.grad(torch.mean((pred-yt)**2),ag)
        errors[f'{n}_autograd']=float(max((a+b*m).abs().max().item() for a,b,m in zip(v,grads,[n,1,n])))
        h=.013;stage=ref.Parameters(tuple(x+h*z for x,z in zip(p.weights,rv.weights)),p.readout+h*rv.readout)
        r2=ref.flow_velocity(stage,np.sqrt(2)*u,y)
        exact=tuple(x+h*(v1+v2)/2 for x,v1,v2 in zip((*p.weights,p.readout),(*rv.weights,rv.readout),(*r2.weights,r2.readout)))
        net.step(ut,yt,h);errors[f'{n}_heun']=float(max(np.max(abs(x-z)) for x,z in zip(net.arrays(),exact)))
        fn=out/f'roundtrip_{n}.npz';np.savez(fn,W=net.arrays()[0],V=net.arrays()[1],c=net.arrays()[2])
        with np.load(fn,allow_pickle=False) as z:copy=Network((z['W'],z['V'],z['c']),device)
        errors[f'{n}_replay']=float(np.max(abs(copy.predict(a)-net.predict(a))))
        before=net.arrays();net.step(ut,yt,h);copy.step(ut,yt,h)
        errors[f'{n}_restart']=float(max(np.max(abs(a-b)) for a,b in zip(net.arrays(),copy.arrays())))
    result=dict(errors=errors,passed=max(errors.values())<1e-10,source_hashes=source_hashes(),torch=torch.__version__,numpy=np.__version__,device=device,elapsed=time.time()-begun)
    write_json(out/'checks.json',result);print(json.dumps(result),flush=True)
    if not result['passed']:raise RuntimeError('worker correctness failure')

def config(delta,n,seed,variant='main'):
    h=.01 if variant=='half' else .02;dtype='float64' if variant=='precision' else 'float32'
    return dict(id=f'pair_d{delta}_n{n}_s{seed}_{variant}',kind='pair',delta=delta,rotation=45,amplitude=1.,width=n,seed=seed,h=h,dtype=dtype,variant=variant,
                angles_degrees=[45-delta/2,45+delta/2],labels=[-1.,1.],retain_state=delta==30 and (n<=4096 or seed==1729))
def prepare(out):
    out=Path(out).resolve();out.mkdir(parents=True,exist_ok=False)
    configs=[config(d,n,s) for d in [30,15,90] for n in [1024,4096] for s in [1729,2718,3141]]
    configs += [config(30,4096,1729,'half'),config(30,1024,1729,'precision')]
    manifest=dict(configs=configs,conditional_wide=[config(30,8192,s) for s in [1729,2718,3141]],source_hashes=source_hashes(),cwd=str(ROOT),command=sys.argv,
                  environment={k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','CUBLAS_WORKSPACE_CONFIG']})
    write_json(out/'manifest.json',manifest);return manifest

def limits(out):
    used=sum(p.stat().st_size for p in out.rglob('*') if p.is_file())
    if used>650*2**20:raise RuntimeError('650MiB campaign output cap')
    if shutil.disk_usage(out).free<1.5*2**30:raise RuntimeError('minimum free disk reached')
    clock=json.loads((out/'clock.json').read_text())['start']
    if time.time()-clock>1200:raise RuntimeError('1200-second campaign limit')

@torch.no_grad()
def run_job(out,cfg,device):
    out=Path(out).resolve();directory=out/cfg['id'];directory.mkdir();begun=time.time();write_json(directory/'started.json',dict(wall_start=begun,pid=os.getpid(),config=cfg))
    write_json(directory/'config.json',cfg);manifest=json.loads((out/'manifest.json').read_text())
    if source_hashes()!=manifest['source_hashes']:raise RuntimeError('producer changed after freeze')
    dtype=getattr(torch,cfg['dtype']);n=cfg['width'];net=Network.initialize(n,cfg['seed'],device,dtype)
    initial_hash=hashlib.sha256()
    for a in net.arrays():initial_hash.update(a.tobytes())
    theta=2*np.pi*np.arange(1440)/1440;stop_theta=2*np.pi*np.arange(512)/512;motion_theta=2*np.pi*np.arange(128)/128
    ta=np.deg2rad(cfg['angles_degrees']);u=net.tensor_inputs(ta);y=torch.as_tensor(cfg['labels'],device=device,dtype=dtype);um=net.tensor_inputs(motion_theta)
    h10,h20,_=net.fields(u);h10=h10.clone();h20=h20.clone();hm10,hm20,_=net.fields(um);hm10=hm10.clone();hm20=hm20.clone()
    times=[];losses=[];predictions=[];train_predictions=[];settled=False;common=None;stop_reason='time_cap';max_increase=0.
    h=cfg['h'];steps_per_obs=int(round(10/h));job_cap=240 if n>=8192 else 120
    # All updates remain simultaneous raw-weight Heun; no change in model.
    for obs in range(31):
        t=obs*10.;p=net.predict(stop_theta);ft=net.fields(u)[2].cpu().numpy().astype(float);loss=float(np.mean((ft-np.array(cfg['labels']))**2))
        if not np.all(np.isfinite(p)) or not np.isfinite(loss):raise RuntimeError('nonfinite output')
        if losses:max_increase=max(max_increase,loss-losses[-1])
        if max_increase>1e-6:raise RuntimeError('loss increased beyond allowance')
        times.append(t);losses.append(loss);predictions.append(p);train_predictions.append(ft)
        if t==100:common=net.predict(theta)
        if t>=100 and loss<=1e-6:
            scale=.002*max(1,float(np.max(abs(p))))
            if np.max(abs(p-predictions[-3]))<=scale and np.max(abs(predictions[-3]-predictions[-5]))<=scale:
                settled=True;stop_reason='mild_settling';break
        if t>=300:break
        limits(out)
        if time.time()-begun>job_cap:raise RuntimeError('per-job wall limit')
        for j in range(steps_per_obs):net.step(u,y,h)
    dense=net.predict(theta);h1,h2,_=net.fields(u);hm1,hm2,_=net.fields(um)
    odd=float(np.max(abs(dense[:720]+dense[720:])));tol=2e-5 if dtype==torch.float32 else 1e-10
    if odd>tol:raise RuntimeError('antipodal oddness failed')
    outputs={};replay=None
    if cfg['retain_state']:
        W,V,c=net.arrays();np.savez_compressed(directory/'state.npz',W=W,V=V,c=c)
        with np.load(directory/'state.npz',allow_pickle=False) as z:copy=Network((z['W'],z['V'],z['c']),device,dtype)
        replay=float(np.max(abs(copy.predict(theta)-dense)));del copy
        if replay>tol:raise RuntimeError('disk replay failed')
        outputs['state.npz']=sha(directory/'state.npz')
    np.savez_compressed(directory/'observations.npz',theta=theta,dense_predictions=dense,common_T100=common if common is not None else np.full(1440,np.nan),times=times,loss=losses,predictions=predictions,train_predictions=train_predictions,
        gram1_initial=(h10.T@h10/n).cpu().numpy(),gram2_initial=(h20.T@h20/n).cpu().numpy(),gram1_final=(h1.T@h1/n).cpu().numpy(),gram2_final=(h2.T@h2/n).cpu().numpy(),
        motion1_circle=float(torch.mean((hm1-hm10)**2).sqrt()),motion2_circle=float(torch.mean((hm2-hm20)**2).sqrt()))
    for name in ['observations.npz','config.json']:outputs[name]=sha(directory/name)
    limits(out)
    if time.time()-begun>job_cap:raise RuntimeError('per-job wall limit including diagnostics')
    record=dict(status='complete',config=cfg,settled=settled,final_time=times[-1],final_loss=losses[-1],stop_reason=stop_reason,
        checks=dict(oddness=odd,max_loss_increase=max_increase,disk_replay=replay),source_hashes=manifest['source_hashes'],initial_weight_sha256=initial_hash.hexdigest(),outputs=outputs,
        elapsed=time.time()-begun,environment=dict(torch=torch.__version__,numpy=np.__version__,device=device,gpu=torch.cuda.get_device_name(torch.device(device)),tf32=False,dtype=cfg['dtype']))
    write_json(directory/'record.json',record);print(json.dumps(dict(id=cfg['id'],seconds=record['elapsed'],T=times[-1],loss=losses[-1],settled=settled)),flush=True)

def worker(out,assignment,device):
    setup(device)
    for cfg in json.loads(Path(assignment).read_text()):
        try:run_job(Path(out),cfg,device)
        except Exception as e:
            directory=Path(out)/cfg['id'];directory.mkdir(exist_ok=True)
            write_json(directory/'failure.json',dict(error=repr(e),traceback=traceback.format_exc(),config=cfg));raise

def wave(out,which):
    out=Path(out).resolve();manifest=json.loads((out/'manifest.json').read_text());configs=manifest['configs'] if which=='main' else manifest['conditional_wide']
    if not (out/'clock.json').exists():write_json(out/'clock.json',dict(start=time.time()))
    begun=time.time();processes=[];logs=[];reason=None
    for gpu in [0,1]:
        assignment=out/f'{which}_assignment{gpu}.json';write_json(assignment,configs[gpu::2]);log=(out/f'{which}_worker{gpu}.log').open('x');logs.append(log)
        processes.append(subprocess.Popen([sys.executable,'-B',str(Path(__file__).resolve()),'--worker',str(assignment),'--output',str(out),'--device',f'cuda:{gpu}'],stdout=log,stderr=subprocess.STDOUT,cwd=ROOT,env=os.environ.copy()))
    try:
        while any(p.poll() is None for p in processes):
            limits(out)
            if any(p.poll() not in [None,0] for p in processes):raise RuntimeError('worker failure')
            for cfg in configs:
                d=out/cfg['id'];started=d/'started.json'
                if started.exists() and not (d/'record.json').exists():
                    cap=240 if cfg['width']>=8192 else 120
                    if time.time()-json.loads(started.read_text())['wall_start']>cap:raise RuntimeError(f'wall cap for {cfg["id"]}')
            time.sleep(.5)
    except Exception as e:
        reason=repr(e)
        for p in processes:
            if p.poll() is None:p.terminate()
    finally:
        codes=[p.wait() for p in processes]
        for log in logs:log.close()
    result=dict(wave=which,exit_codes=codes,elapsed=time.time()-begun,stop_reason=reason,completed=[c['id'] for c in configs if (out/c['id']/'record.json').exists()],missing=[c['id'] for c in configs if not (out/c['id']/'record.json').exists()])
    write_json(out/f'{which}_batch.json',result);print(json.dumps(result),flush=True)
    if reason or any(codes):raise RuntimeError('campaign wave incomplete')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--device',default='cpu');p.add_argument('--check',action='store_true');p.add_argument('--prepare',action='store_true');p.add_argument('--wave',choices=['main','wide']);p.add_argument('--worker');a=p.parse_args()
    if a.check:checks(a.device,a.output)
    elif a.prepare:prepare(a.output)
    elif a.worker:worker(a.output,a.worker,a.device)
    elif a.wave:wave(a.output,a.wave)
