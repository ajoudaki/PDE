"""Predeclared stronger frozen control and fair full/checkpoint memory diagnostics."""
import argparse, gc, hashlib, json, math, sys, time
from pathlib import Path
import numpy as np
import torch
from scipy.optimize import lsq_linear
from torch.utils.checkpoint import checkpoint
from hypergradient import FunctionalFlow,circle,utc,write,SOURCE,BASE

def meta(a):return dict(start_utc=utc(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),adapter_sha256=SOURCE,baseline_sha256=BASE,config={k:str(v) if isinstance(v,Path) else v for k,v in vars(a).items()},torch=torch.__version__,numpy=np.__version__,gpu=torch.cuda.get_device_name(0),python=sys.version)
def convex(a,out):
    result=meta(a);rows=[]
    for seed in a.seeds:
        start=time.monotonic();x,y=circle(8,.13,'cuda:0',torch.float64);outer,target=circle(32,.37,'cuda:0',torch.float64);test,test_y=circle(256,.71,'cuda:0',torch.float64)
        flow=FunctionalFlow(x,a.width,seed,'dense');A=flow.frozen_map(outer,1/32,8).cpu().numpy();fit=lsq_linear(A,target.cpu().numpy(),bounds=(-3,3),tol=1e-12,lsmr_tol=1e-12,max_iter=1000)
        labels=x.new_tensor(fit.x)
        with torch.no_grad():
            frozen=flow.frozen_map(test,1/32,8)@labels
            dense=flow.predict(flow.solve(labels,1/32,8),test)
            fine=flow.predict(flow.solve(labels,1/64,8),test)
        row=dict(seed=seed,width=a.width,labels=labels,lsq_success=fit.success,lsq_status=fit.status,optimality=fit.optimality,lsq_iterations=fit.nit,frozen_outer_mse=float(np.mean((A@fit.x-target.cpu().numpy())**2)),frozen_test_mse=float((frozen-test_y).square().mean()),dense_test_mse=float((dense-test_y).square().mean()),refined_dense_test_mse=float((fine-test_y).square().mean()),seconds=time.monotonic()-start)
        rows.append(row);print(json.dumps({k:v for k,v in row.items() if k!='labels'}),flush=True)
    result.update(rows=rows,end_utc=utc());write(out/'convex.json',result)
def memory(a,out):
    result=meta(a);rows=[];reference={}
    # Warm library allocation/checkpoint dispatch before every measured comparison.
    warm=torch.ones((32,32),device='cuda:0',requires_grad=True)
    for _ in range(2):
        temp=checkpoint(lambda z: z@z,warm,use_reentrant=False)
        warm_grad=torch.autograd.grad(temp.square().mean(),warm)[0]
    del temp,warm_grad,warm
    torch.cuda.synchronize()
    for n in [128,512]:
      for kind in ['dense',a.kind]:
       for strategy in ['full','checkpoint16']:
        gc.collect();torch.cuda.empty_cache();x,y=circle(8,.13,'cuda:0',torch.float32);query,target=circle(32,.37,'cuda:0',torch.float32);flow=FunctionalFlow(x,n,201,kind);label=y.clone().requires_grad_()
        torch.cuda.synchronize();base=torch.cuda.memory_allocated();torch.cuda.reset_peak_memory_stats();start=time.monotonic()
        if strategy=='full':state=flow.solve(label,1/32,8)
        else:
            def block(lab,*values):
                for _ in range(16):values=tuple(v+dv/32 for v,dv in zip(values,flow.rhs(values,lab)))
                return values
            state=flow.initial()
            for _ in range(16):state=checkpoint(block,label,*state,use_reentrant=False)
        p=flow.predict(state,query);loss=(p-target).square().mean();grad=torch.autograd.grad(loss,label)[0]
        torch.cuda.synchronize();elapsed=time.monotonic()-start;peak=torch.cuda.max_memory_allocated();g=grad.cpu().numpy();key=(n,kind)
        if strategy=='full':reference[key]=g
        rows.append(dict(width=n,kind=kind,strategy=strategy,seconds=elapsed,setup_allocated_bytes=base,peak_allocated_bytes=peak,incremental_peak_bytes=peak-base,gradient=grad.detach(),gradient_max_difference=float(np.max(np.abs(reference[key]-g))),moving_coordinates=n*n+3*n if kind=='dense' else 3*n+16*n*int(kind[1:])+1,fixed_source_coordinates=0 if kind=='dense' else n*n))
        print(json.dumps({k:v for k,v in rows[-1].items() if k!='gradient'}),flush=True)
        del x,y,query,target,flow,label,state,p,loss,grad
    result.update(rows=rows,end_utc=utc());write(out/'memory.json',result)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=['convex','memory'],required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--width',type=int,default=128);p.add_argument('--seeds',type=int,nargs='+',default=[101,102,103]);p.add_argument('--kind',default='q1');a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False);(a.out/'hypergradient_audit_source.py').write_bytes(Path(__file__).read_bytes());{'convex':convex,'memory':memory}[a.mode](a,a.out)
