"""Functional canonical Flow adapter and precommitted eight-label calibration probe."""
import argparse, datetime, hashlib, json, math, os, platform, sys, time
from pathlib import Path
os.environ.setdefault('OMP_NUM_THREADS','1')
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np
import torch
from baseline_compact_flow import Flow
HERE=Path(__file__).resolve().parent
SOURCE=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
BASE=hashlib.sha256((HERE/'baseline_compact_flow.py').read_bytes()).hexdigest()
torch.set_num_threads(1)
torch.backends.cuda.matmul.allow_tf32=False
torch.backends.cudnn.allow_tf32=False

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def plain(v):
    if isinstance(v,torch.Tensor):return v.detach().cpu().tolist()
    if isinstance(v,dict):return {k:plain(w) for k,w in v.items()}
    if isinstance(v,(list,tuple)):return [plain(w) for w in v]
    return v

def write(path,value):path.write_text(json.dumps(plain(value),indent=2,allow_nan=False))
def circle(count,shift,device,dtype):
    theta=(torch.arange(count,device=device,dtype=dtype)+shift)*(2*math.pi/count)
    return torch.stack((theta.cos(),theta.sin()),1),torch.sin(3*theta)+.4*torch.cos(theta)

class FunctionalFlow:
    """State coordinates and operations exactly map to source Flow at depth2/tanh."""
    def __init__(self,x,width,seed,kind='dense'):
        self.x=x;self.n=width;self.m=len(x);self.kind=kind
        self.q=int(kind[1:]) if kind.startswith('q') else None
        rng=np.random.default_rng(seed)
        self.w0=x.new_tensor(rng.standard_normal((width,x.shape[1])))
        self.W0=x.new_tensor(rng.standard_normal((width,width))/math.sqrt(width))
        self.c0=x.new_zeros(width)
        if self.q:
            self.deg=torch.arange(self.q,device=x.device,dtype=x.dtype)[:,None,None]
            self.weights=2*self.deg+1
    def initial(self):
        if self.q:
            h=torch.tanh(self.w0@self.x.T)
            # Prefix B0=h, higher modes0; built functionally to preserve input dependence.
            B=torch.cat((h[None],h.new_zeros((self.q-1,self.n,self.m))))
            return (self.w0,self.c0,torch.zeros_like(B),B,self.x.new_zeros(()))
        return (self.w0,self.W0,self.c0)
    @staticmethod
    def cols(v):return v.permute(1,0,2).reshape(v.shape[1],-1)
    def factors(self,state):
        if not self.q:return None
        _,_,A,B,s=state
        return (-2/(self.m*self.n))*self.cols(self.weights*A),self.cols(B/(1+s))
    def apply(self,h,state,transpose=False,factors=None):
        W=self.W0 if self.q else state[1]
        z=(W.T if transpose else W)@h
        if self.q:
            left,right=self.factors(state) if factors is None else factors
            if transpose:left,right=right,left
            z=z+left@(right.T@h)
        return z
    def fields(self,state,x=None):
        x=self.x if x is None else x
        w=state[0];c=state[1] if self.q else state[2]
        h1=torch.tanh(w@x.T)
        h2=torch.tanh(self.apply(h1,state))
        return h1,h2,c@h2/self.n
    def predict(self,state,x):return self.fields(state,x)[2]
    def rhs(self,state,y):
        h1,h2,f=self.fields(state)
        r=f-y;c=state[1] if self.q else state[2]
        delta2=(1-h2.square())*c[:,None]
        delta1=(1-h1.square())*self.apply(delta2,state,True)
        dw=(-2/self.m)*(delta1*r)@self.x
        dc=(-2/self.m)*(h2@r)
        if not self.q:
            return dw,(-2/(self.m*self.n))*(delta2*r)@h1.T,dc
        _,_,A,B,s=state;rho=r.square().mean().sqrt()
        def transport(moment,source):
            if self.q==1:return source[None]
            weighted=self.weights*moment
            lower=torch.cat((torch.zeros_like(weighted[:1]),weighted[:-1].cumsum(0)))
            return source[None]-(rho/(1+s))*(self.deg*moment+lower)
        return dw,dc,transport(A,delta2*r),transport(B,rho*h1),rho
    def solve(self,y,dt,T):
        steps=round(T/dt)
        if abs(steps*dt-T)>1e-10:raise ValueError('noninteger step count')
        state=self.initial()
        for _ in range(steps):state=tuple(v+dt*dv for v,dv in zip(state,self.rhs(state,y)))
        return state
    def frozen_map(self,query,dt,T):
        # Exact discrete readout-only Euler solution; initial zero readout.
        h=torch.tanh(self.W0@torch.tanh(self.w0@self.x.T))
        hq=torch.tanh(self.W0@torch.tanh(self.w0@query.T))
        K=h.T@h/self.n
        lam,V=torch.linalg.eigh(K)
        # Stable polynomial divided difference at eigenvalue0, no discarded modes.
        a=2*dt*lam/self.m
        factor=torch.where(lam.abs()>1e-10,-torch.expm1(round(T/dt)*torch.log1p(-a))/lam,
                           torch.full_like(lam,2*T/self.m))
        return (hq.T@h/self.n)@(V*factor)@V.T

def metadata(args):
    return dict(start_utc=utc(),source_sha256=SOURCE,baseline_sha256=BASE,argv=sys.argv,
                python=sys.version,torch=torch.__version__,numpy=np.__version__,platform=platform.platform(),
                gpu=torch.cuda.get_device_name(args.device) if 'cuda' in args.device else None,config=vars(args))

def checks(args,out):
    result=metadata(args);rows=[]
    x,y=circle(8,.13,args.device,torch.float64);v,_=circle(32,.37,args.device,torch.float64)
    for kind in ['dense','q1','q2','q4','q8']:
        a=FunctionalFlow(x,32,101,kind);state=a.initial()
        b=Flow(x,y,width=32,depth=2,activation='tanh',order=a.q,seed=101,device=args.device,dtype=torch.float64,hidden_gain=1.,readout_std=1.)
        b.c.zero_()
        row=dict(kind=kind)
        for step in range(32):
            state=tuple(s+dv/64 for s,dv in zip(state,a.rhs(state,y)));b.step(1/64)
            if step in [0,31]:
                row[f'state_error_{step+1}']=max(float((s-t).abs().max()) for s,t in zip(state,b.state))
                row[f'prediction_error_{step+1}']=float((a.predict(state,v)-b.predict(v)).abs().max())
        rows.append(row)
    result['parity']=rows;fd=[]
    for kind in ['dense','q1','q4']:
        a=FunctionalFlow(x,32,101,kind);label=y.clone().requires_grad_();target=circle(32,.37,args.device,torch.float64)[1]
        def loss(lab):return (a.predict(a.solve(lab,1/32,1),v)-target).square().mean()
        grad=torch.autograd.grad(loss(label),label)[0];direction=torch.arange(1,9,device=x.device,dtype=x.dtype);direction/=direction.norm()
        exact=float(grad@direction)
        row=dict(kind=kind,autograd=exact)
        for eps in [1e-4,5e-5]:
            approx=float((loss(y+eps*direction)-loss(y-eps*direction))/(2*eps))
            row[str(eps)]=dict(finite_difference=approx,relative_error=abs(approx-exact)/max(abs(exact),1e-12))
        fd.append(row)
    # Input-direction check specifically includes initial B0(x), while fixed query stays fixed.
    xx=x.clone().requires_grad_();direction=torch.arange(1,1+x.numel(),device=x.device,dtype=x.dtype).reshape_as(x);direction=direction/direction.norm()
    def input_loss(z):
        a=FunctionalFlow(z,32,101,'q4');return (a.predict(a.solve(y,1/32,1),v)-target).square().mean()
    exact=float((torch.autograd.grad(input_loss(xx),xx)[0]*direction).sum());eps=1e-4
    approx=float((input_loss(x+eps*direction)-input_loss(x-eps*direction))/(2*eps))
    result['input_prefix_fd']=dict(autograd=exact,finite_difference=approx,relative_error=abs(exact-approx)/max(abs(exact),1e-12))
    result['label_fd']=fd;result['end_utc']=utc()
    result['pass']=all(row[k]<1e-10 for row in rows for k in row if k!='kind') and all(row[str(e)]['relative_error']<1e-4 for row in fd for e in [1e-4,5e-5]) and result['input_prefix_fd']['relative_error']<1e-4
    write(out/'checks.json',result);print(json.dumps(result),flush=True)

def evaluate(args,out):
    result=metadata(args);started=time.monotonic();dtype=torch.float32
    x,y=circle(8,.13,args.device,dtype);outer,target=circle(32,.37,args.device,dtype);test,test_y=circle(256,.71,args.device,dtype)
    for seed in args.seeds:
        seed_start=time.monotonic();models={k:FunctionalFlow(x,args.width,seed,k) for k in args.kinds if k!='frozen'}
        dense=FunctionalFlow(x,args.width,seed,'dense');frozen=FunctionalFlow(x,args.width,seed,'frozen')
        frozen_outer=frozen.frozen_map(outer,args.dt,args.horizon).detach();frozen_test=frozen.frozen_map(test,args.dt,args.horizon).detach()
        with torch.no_grad():
            original=dense.solve(y,args.dt,args.horizon);p0=dense.predict(original,test);h0=dense.fields(dense.initial())[0:2];hf=dense.fields(original)[0:2]
            E0=float((p0-test_y).square().mean());sep=float((p0-frozen_test@y).square().mean().sqrt())
            movement=[float((a-b).square().mean().sqrt()) for a,b in zip(h0,hf)]
        summary=dict(seed=seed,width=args.width,horizon=args.horizon,dt=args.dt,original_dense_test_mse=E0,
                     original_frozen_test_mse=float((frozen_test@y-test_y).square().mean()),dense_frozen_prediction_rms=sep,feature_movement=movement,designs=[])
        dense_gradient=None
        for kind in args.kinds:
            torch.cuda.empty_cache();torch.cuda.reset_peak_memory_stats(args.device)
            run_start=time.monotonic();record=dict(start_utc=utc(),kind=kind,seed=seed,width=args.width,horizon=args.horizon,dt=args.dt,steps=round(args.horizon/args.dt),outer_steps=args.outer_steps,source_sha256=SOURCE,baseline_sha256=BASE)
            labels=y.clone().requires_grad_();optimizer=torch.optim.Adam([labels],lr=.05);losses=[];status='ok'
            try:
                for it in range(args.outer_steps):
                    optimizer.zero_grad(set_to_none=True)
                    pred=frozen_outer@labels if kind=='frozen' else models[kind].predict(models[kind].solve(labels,args.dt,args.horizon),outer)
                    loss=(pred-target).square().mean()
                    if not torch.isfinite(loss):raise FloatingPointError('nonfinite outer loss')
                    loss.backward()
                    if not torch.isfinite(labels.grad).all():raise FloatingPointError('nonfinite hypergradient')
                    if it==0:
                        g=labels.grad.detach().clone();record['initial_gradient']=g;record['initial_outer_mse']=float(loss)
                        if kind=='dense':dense_gradient=g
                        if dense_gradient is not None:
                            record['gradient_cosine']=float(torch.nn.functional.cosine_similarity(g,dense_gradient,dim=0))
                            record['gradient_relative_error']=float((g-dense_gradient).norm()/dense_gradient.norm())
                    losses.append(float(loss));optimizer.step()
                    with torch.no_grad():labels.clamp_(-3,3)
                    del pred,loss
                labels=labels.detach()
                with torch.no_grad():
                    trained=dense.solve(labels,args.dt,args.horizon);p=dense.predict(trained,test)
                    E=float((p-test_y).square().mean())
                    own=frozen_test@labels if kind=='frozen' else models[kind].predict(models[kind].solve(labels,args.dt,args.horizon),test)
                record.update(labels=labels,outer_loss_history=losses,dense_test_mse=E,dense_error_ratio=E/E0,
                              surrogate_test_mse=float((own-test_y).square().mean()),surrogate_dense_prediction_rms=float((own-p).square().mean().sqrt()))
                if args.refine:
                    with torch.no_grad():
                        pr=dense.predict(dense.solve(labels,args.dt/2,args.horizon),test)
                        p0r=dense.predict(dense.solve(y,args.dt/2,args.horizon),test)
                    record.update(refined_dense_test_mse=float((pr-test_y).square().mean()),refined_original_dense_test_mse=float((p0r-test_y).square().mean()),dense_refinement_prediction_rms=float((pr-p).square().mean().sqrt()))
            except (FloatingPointError,RuntimeError) as e:
                status='failed';record['error']=repr(e);record['outer_loss_history']=losses
            torch.cuda.synchronize(args.device)
            record.update(status=status,end_utc=utc(),seconds=time.monotonic()-run_start,peak_allocated_bytes=torch.cuda.max_memory_allocated(args.device),peak_reserved_bytes=torch.cuda.max_memory_reserved(args.device))
            q=int(kind[1:]) if kind.startswith('q') else 0
            record['moving_coordinates']=3*args.width+2*8*args.width*q+1 if q else (args.width if kind=='frozen' else args.width**2+3*args.width)
            record['fixed_weight_coordinates']=args.width**2 if q else (args.width**2+2*args.width if kind=='frozen' else 0)
            write(out/f'seed{seed}_{kind}.json',record);summary['designs'].append(plain(record))
            print(json.dumps({k:plain(record[k]) for k in ['kind','seed','status','seconds','peak_allocated_bytes','dense_test_mse','dense_error_ratio','gradient_cosine'] if k in record}),flush=True)
        summary['seconds']=time.monotonic()-seed_start;write(out/f'seed{seed}_summary.json',summary)
    result.update(end_utc=utc(),seconds=time.monotonic()-started);write(out/'run.json',result)

def pilot_gate(args,out):
    x,y=circle(8,.13,args.device,torch.float64);test,target=circle(32,.37,args.device,torch.float64)
    result=metadata(args);rows=[]
    for kind in args.kinds:
        a=FunctionalFlow(x,args.width,args.seeds[0],kind);preds=[];grads=[]
        for dt in [args.dt,args.dt/2]:
            label=y.clone().requires_grad_();state=a.solve(label,dt,args.horizon);p=a.predict(state,test)
            grads.append(torch.autograd.grad((p-target).square().mean(),label)[0]);preds.append(p.detach())
        rows.append(dict(kind=kind,prediction_rms=float((preds[0]-preds[1]).square().mean().sqrt()),gradient_cosine=float(torch.nn.functional.cosine_similarity(grads[0],grads[1],dim=0)),gradient_relative_error=float((grads[0]-grads[1]).norm()/grads[1].norm())))
    result.update(rows=rows,end_utc=utc());write(out/'gate.json',result);print(json.dumps(result),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=['check','gate','run'],required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--device',default='cuda:0');p.add_argument('--width',type=int,default=128);p.add_argument('--dt',type=float,default=1/32);p.add_argument('--horizon',type=float,default=8.);p.add_argument('--seeds',type=int,nargs='+',default=[101]);p.add_argument('--kinds',nargs='+',default=['dense','q1','q2','q4','q8','frozen']);p.add_argument('--outer-steps',type=int,default=24);p.add_argument('--refine',action='store_true');args=p.parse_args();args.out.mkdir(parents=True,exist_ok=False);args.out=str(args.out);out=Path(args.out);(out/'hypergradient_source.py').write_bytes(Path(__file__).read_bytes())
    {'check':checks,'gate':pilot_gate,'run':evaluate}[args.mode](args,out)
