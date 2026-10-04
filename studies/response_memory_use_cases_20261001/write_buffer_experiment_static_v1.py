"""Preregistered response-memory consolidation route; baseline remains unchanged."""
import os
os.environ.setdefault('OMP_NUM_THREADS','1')
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse, hashlib, json, math, platform, sys, time
from pathlib import Path
import numpy as np
import torch
from baseline_compact_flow import Flow, LowRankFlow
HERE=Path(__file__).resolve().parent
SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
torch.set_num_threads(1)
torch.backends.cuda.matmul.allow_tf32=False
torch.backends.cudnn.allow_tf32=False

def task(m=8,rotation=0):
    a=2*np.pi*(np.arange(m)+.13)/m+rotation
    return np.stack([np.cos(a),np.sin(a)],1),np.sign(np.cos(3*a))

def queries():
    a=2*np.pi*np.arange(513)/513
    return np.stack([np.cos(a),np.sin(a)],1),np.sign(np.cos(3*a))

class BufferFlow(Flow):
    @torch.no_grad()
    def consolidate(self):
        factors=self._factors()
        for W,(left,right) in zip(self.matrices,factors): W.add_(left@right.T)
        for A,B in zip(self.moments[::2],self.moments[1::2]): A.zero_();B.zero_()
        self.s.zero_()
        h,_=self._forward(self.inputs,self._factors())
        for B,current in zip(self.moments[1::2],h[:-1]): B[0].copy_(current)

    @torch.no_grad()
    def defect(self):
        h,delta,r=self._fields()
        rho=r.square().mean().sqrt()
        normsq=self.w.new_zeros(()); bound=self.w.new_zeros(())
        for i,(A,B) in enumerate(zip(self.moments[::2],self.moments[1::2])):
            u=delta[i+1]*r-rho*(self.weights*A).sum(0)/(1+self.s)
            v=h[i]-(self.weights*B).sum(0)/(1+self.s)
            scale=2/(self.n*self.M)
            normsq+=scale**2*((u.T@u)*(v.T@v)).sum()
            bound+=scale*(u.square().sum(0).sqrt()*v.square().sum(0).sqrt()).sum()
        return normsq.clamp_min(0).sqrt(),bound

class DelayedFlow(Flow):
    def __init__(self,*args,max_steps,multiplier=1.,**kw):
        super().__init__(*args,order=None,**kw)
        assert self.depth==2
        self.state=[self.w,self.c]
        self.history_h=self.w.new_empty((max_steps,self.n,self.M))
        self.history_q=torch.empty_like(self.history_h)
        self.pending=0;self.multiplier=multiplier
    @torch.no_grad()
    def rhs(self):
        hidden,q,r,_=self._loss_fields()
        self.current_h=hidden[0];self.current_q=q[1]
        self.loss=r.square().mean()
        return [(-2/self.M)*q[0]@self.inputs,(-2/self.M)*hidden[-1]@r]
    @torch.no_grad()
    def record_stage(self):
        self.history_h[self.pending].copy_(self.current_h)
        self.history_q[self.pending].copy_(self.current_q)
        self.pending+=1
    @torch.no_grad()
    def consolidate(self,dt):
        h=self.history_h[:self.pending].permute(1,0,2).reshape(self.n,-1)
        q=self.history_q[:self.pending].permute(1,0,2).reshape(self.n,-1)
        self.matrices[0].add_(q@h.T,alpha=-2*dt*self.multiplier/(self.M*self.n))
        rank=h.shape[1];self.pending=0
        return rank

@torch.no_grad()
def midpoint(flow,dt,saved):
    for dst,x in zip(saved,flow.state):dst.copy_(x)
    v=flow.rhs()
    for x,x0,dx in zip(flow.state,saved,v):x.copy_(x0+(.5*dt)*dx)
    v=flow.rhs()
    if isinstance(flow,DelayedFlow):flow.record_stage()
    for x,x0,dx in zip(flow.state,saved,v):x.copy_(x0+dt*dx)

@torch.no_grad()
def checks():
    result={}
    x,y=task(5);query,_=queries()
    for q in [1,3]:
        f=BufferFlow(x,y,width=17,depth=2,activation='tanh',order=q,seed=101,device='cpu',dtype=torch.float64,hidden_gain=1.,readout_std=1.)
        f.c.zero_();saved=[z.clone() for z in f.state]
        for _ in range(50):midpoint(f,.01,saved)
        factors=f._factors();W=f.matrices[0]+factors[0][0]@factors[0][1].T
        probe=torch.randn((17,6),dtype=torch.float64)
        err_forward=float((f._apply(0,probe,factors)-W@probe).abs().max())
        err_transpose=float((f._apply(0,probe,factors,True)-W.T@probe).abs().max())
        vel=f.rhs(); A,B=f.moments;dA,dB=vel[2:4];tau=1+f.s;rho=vel[-1]
        cols=f._columns
        dW=(-2/(f.n*f.M))*(cols(f.weights*dA)@cols(B).T/tau+cols(f.weights*A)@cols(dB).T/tau-cols(f.weights*A)@cols(B).T*rho/tau**2)
        h,d,r=f._fields();u=d[1]*r-rho*(f.weights*A).sum(0)/tau;v=h[0]-(f.weights*B).sum(0)/tau
        E=(2/(f.n*f.M))*u@v.T
        dense=(-2/(f.n*f.M))*(d[1]*r)@h[0].T
        err_defect=float((dW-dense-E).norm()/(dW.norm()+1e-30))
        en,bound=f.defect();err_norm=abs(float(en-E.norm()))
        old=[z.clone() for z in f.state];values=[];eps=1e-6
        for sign in [-1,1]:
            for z,z0,dz in zip(f.state,old,vel):z.copy_(z0+sign*eps*dz)
            le,ri=f._factors()[0];values.append(f.matrices[0]+le@ri.T)
        for z,z0 in zip(f.state,old):z.copy_(z0)
        err_fd=float(((values[1]-values[0])/(2*eps)-dW).norm()/(dW.norm()+1e-30))
        before=f.predict(query).clone();f.consolidate();err_flush=float((f.predict(query)-before).abs().max())
        result[q]=dict(forward=err_forward,transpose=err_transpose,analytic_defect_relative=err_defect,defect_norm_absolute=err_norm,defect_norm=float(en),defect_bound=float(bound),finite_difference_relative=err_fd,flush_continuity=err_flush)
        assert max(err_forward,err_transpose,err_defect,err_norm,err_flush)<1e-10,result
        assert err_fd<1e-6 and float(en)<=float(bound)*(1+1e-12),result
    return result

@torch.no_grad()
def run(args):
    out=Path(args.out);out.mkdir(parents=True,exist_ok=False)
    x,y=task();query,target=queries();steps=round(args.horizon/args.dt)
    common=dict(width=args.width,depth=2,activation='tanh',seed=args.seed,device=args.device,dtype=getattr(torch,args.dtype),hidden_gain=1.,readout_std=1.,normalization='none')
    cfg=vars(args).copy();cfg.update(source_sha256=SHA,baseline_sha256=hashlib.sha256((HERE/'baseline_compact_flow.py').read_bytes()).hexdigest(),torch=torch.__version__,python=sys.version,platform=platform.platform(),task='circle_sign_cos3_m8_phase0.13',gpu=torch.cuda.get_device_name(args.device) if args.device.startswith('cuda') else 'cpu')
    (out/'config.json').write_text(json.dumps(cfg,indent=2))
    if args.method=='dense':f=Flow(x,y,order=None,**common)
    elif args.method=='factor':f=LowRankFlow(x,y,rank=args.order*8,factor_seed=args.factor_seed,**common)
    elif args.method=='delayed':f=DelayedFlow(x,y,max_steps=steps,multiplier=args.multiplier,**common)
    else:f=BufferFlow(x,y,order=args.order,**common)
    f.c.zero_(); saved=[v.clone() for v in f.state]
    initial_h=f._forward(f.inputs,f._factors())[0]
    initial_h=[v.clone() for v in initial_h]
    def sync():
        if f.device.type=='cuda':torch.cuda.synchronize(f.device)
    schedule=[]
    if args.schedule:schedule=json.loads(Path(args.schedule).read_text())['flush_steps']
    next_flush=set(schedule)
    snapshots=[];prediction=[];flush_steps=[];defects=[];status='complete';material_flops=0;diagnostic_seconds=0.;material_seconds=0.;max_pending=0
    defect_acc=0.;max_defect_acc=0.;last_diag=0;force_times={8,16,32,64,128,256,args.horizon}
    sample_steps={round(t/args.dt) for t in force_times if t<=args.horizon}
    sample_steps.add(0)
    def observe(k):
        p=f.predict(query);train=f.predict(f.inputs);rms=float((train-f.labels).square().mean().sqrt())
        h=f._forward(f.inputs,f._factors())[0]
        snapshots.append(dict(step=k,time=k*args.dt,train_rms=rms,accuracy=float(((p>=0)==torch.as_tensor(target>=0,device=f.device)).float().mean()),feature_rms=[float((a-b).square().mean().sqrt()) for a,b in zip(h,initial_h)]))
        prediction.append(p.cpu().numpy())
        return rms
    if f.device.type=='cuda':torch.cuda.reset_peak_memory_stats(f.device)
    observe(0);sync();start=time.perf_counter()
    for k in range(1,steps+1):
        midpoint(f,args.dt,saved)
        if isinstance(f,DelayedFlow):max_pending=max(max_pending,f.pending)
        flush=False
        if args.method=='fixed':flush=(k%round(args.interval/args.dt)==0)
        if args.method=='defect' and (k%args.diagnostic_every==0 or k==steps):
            sync();t0=time.perf_counter();en,bound=f.defect();en,bound=float(en),float(bound);sync();diagnostic_seconds+=time.perf_counter()-t0
            defect_acc+=(k-last_diag)*args.dt*bound;last_diag=k;max_defect_acc=max(max_defect_acc,defect_acc)
            defects.append(dict(step=k,time=k*args.dt,norm=en,bound=bound,accumulated_bound=defect_acc))
            flush=defect_acc>=args.threshold*math.sqrt(args.width)
        if args.method=='delayed':flush=k in next_flush or (not args.schedule and k%round(args.interval/args.dt)==0)
        # Save predictions before/after a scheduled support switch separately.
        if args.support_switch and k==round(128/args.dt):flush=args.method in ('fixed','defect','closure','delayed')
        if flush:
            sync();t0=time.perf_counter()
            rank=f.consolidate(args.dt) if isinstance(f,DelayedFlow) else args.order*f.M
            if not isinstance(f,DelayedFlow):f.consolidate()
            sync();material_seconds+=time.perf_counter()-t0;material_flops+=2*f.n*f.n*rank;flush_steps.append(k);defect_acc=0.;last_diag=k
        if k in sample_steps or k%max(1,round(8/args.dt))==0:
            rms=observe(k)
            if not math.isfinite(rms) or rms>20:status='diverged';break
        if args.support_switch and k==round(128/args.dt):
            xx,yy=task(rotation=np.pi/16);f.inputs.copy_(torch.as_tensor(xx,device=f.device,dtype=f.dtype));f.labels.copy_(torch.as_tensor(yy,device=f.device,dtype=f.dtype))
            if isinstance(f,BufferFlow):
                h=f._forward(f.inputs,f._factors())[0]
                for B,current in zip(f.moments[1::2],h[:-1]):B[0].copy_(current)
        if time.perf_counter()-start>args.max_seconds:status='wall_limit';break
    sync();elapsed=time.perf_counter()-start
    if snapshots[-1]['step']!=k:observe(k)
    if isinstance(f,BufferFlow):
        sync();t0=time.perf_counter();en,bound=f.defect();en,bound=float(en),float(bound);sync();diagnostic_seconds+=time.perf_counter()-t0
        final_defect=dict(norm=en,bound=bound)
    else:final_defect=None
    summary=dict(status=status,method=args.method,order=args.order,width=args.width,seed=args.seed,dt=args.dt,physical_time=k*args.dt,steps=k,seconds=elapsed,dense_write_events=2*k if args.method=='dense' else len(flush_steps),optimizer_dense_writes=k if args.method=='dense' else len(flush_steps),flush_steps=flush_steps,flush_times=[s*args.dt for s in flush_steps],materialization_flops=material_flops,materialization_seconds=material_seconds,diagnostic_seconds=diagnostic_seconds,diagnostic_count=len(defects),max_integrated_defect_bound=max_defect_acc,final_defect=final_defect,moving_state_scalars=sum(v.numel() for v in f.state),fixed_dense_scalars=0 if args.method=='dense' else sum(v.numel() for v in f.matrices),delayed_history_allocated_scalars=f.history_h.numel()*2 if isinstance(f,DelayedFlow) else 0,delayed_max_used_scalars=2*max_pending*f.n*f.M,peak_allocated_cuda_bytes=torch.cuda.max_memory_allocated(f.device) if f.device.type=='cuda' else None,snapshots=snapshots)
    np.savez_compressed(out/'predictions.npz',predictions=np.stack(prediction),times=np.array([v['time'] for v in snapshots]),query=query,target=target)
    (out/'defects.json').write_text(json.dumps(defects,indent=2));(out/'summary.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps(dict(out=str(out),status=status,seconds=elapsed,last=snapshots[-1],writes=summary['dense_write_events'])),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--out',required=True);p.add_argument('--method',choices=['dense','closure','fixed','defect','delayed','factor'],default='dense');p.add_argument('--order',type=int,default=1);p.add_argument('--seed',type=int,default=101);p.add_argument('--factor-seed',type=int,default=20260924);p.add_argument('--width',type=int,default=256);p.add_argument('--dt',type=float,default=1/16);p.add_argument('--horizon',type=float,default=256);p.add_argument('--interval',type=float,default=32);p.add_argument('--threshold',type=float,default=.002);p.add_argument('--diagnostic-every',type=int,default=8);p.add_argument('--multiplier',type=float,default=1.);p.add_argument('--schedule');p.add_argument('--device',default='cuda:1');p.add_argument('--dtype',default='float32');p.add_argument('--max-seconds',type=float,default=180);p.add_argument('--support-switch',action='store_true');a=p.parse_args()
    if a.check:
        result=checks();Path(a.out).write_text(json.dumps(result,indent=2));print(json.dumps(result))
    else:run(a)
