"""Independent bounded reproduction of the frozen hypergradient candidate.

Pre-execution decision: reproduce seed 101, width 128, float32, T=8,
dt=1/32, 24 Adam(lr=.05) label updates for dense and q1. Compare final
labels and independently recomputed dense test errors to frozen records;
pass tolerance 2e-4 for labels and 2e-5 for MSE (CPU versus CUDA).
Also use float64 finite differences at the actual T=8 horizon, a direct
autograd weight-gradient oracle, q1 clock derivative ablation, independent
materialized moment RHS, checkpoint parity, and dense half-step replay.
Stop computation at 295 CPU seconds. No new seeds or scientific selection.
Outputs are written only to the assigned fresh review namespace.
After successful seed101 reproduction, repeat the identical primary check
at the first confirmation seed201,width512 to verify the reported width
change. This is reproducibility checking, not a new scientific selection.
"""
import argparse, hashlib, importlib.util, json, os, sys, time
from pathlib import Path
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
import torch
from torch.utils.checkpoint import checkpoint

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE))
import hypergradient as hg

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--width',type=int,default=128);ap.add_argument('--seed',type=int,default=101);a=ap.parse_args()
    assert (a.width,a.seed) in [(128,101),(512,201)]
    a.out.mkdir(parents=True,exist_ok=False)
    started=time.process_time();wall=time.monotonic()
    def budget():
        if time.process_time()-started>295:raise TimeoutError('295 CPU seconds exceeded')
    def save(name,obj):
        (a.out/name).write_text(json.dumps(hg.plain(obj),indent=2,allow_nan=False))
    (a.out/'hypergradient_review_cpu_source.py').write_bytes(Path(__file__).read_bytes())
    manifest=json.loads((HERE/'HYPERGRADIENT_FROZEN_MANIFEST.json').read_text())
    checks=[]
    for f in manifest['files']:
        data=(ROOT/f['path']).read_bytes()
        checks.append(dict(path=f['path'],sha256=hashlib.sha256(data).hexdigest(),matches=hashlib.sha256(data).hexdigest()==f['sha256'],bytes_match=len(data)==f['bytes']))
    save('hashes.json',checks)
    assert all(f['matches'] and f['bytes_match'] for f in checks)
    result=dict(start_utc=hg.utc(),python=sys.version,torch=torch.__version__,numpy=np.__version__,device='cpu',threads=torch.get_num_threads(),source=hg.SOURCE,baseline=hg.BASE,width=a.width,seed=a.seed)
    x,y=hg.circle(8,.13,'cpu',torch.float32);v,target=hg.circle(32,.37,'cpu',torch.float32);test,truth=hg.circle(256,.71,'cpu',torch.float32)
    dense=hg.FunctionalFlow(x,a.width,a.seed,'dense')
    with torch.no_grad():
        base=float((dense.predict(dense.solve(y,1/32,8),test)-truth).square().mean())
    result['original_mse']=base;result['designs']=[]
    for kind in ['dense','q1']:
        flow=hg.FunctionalFlow(x,a.width,a.seed,kind)
        labels=y.clone().requires_grad_();opt=torch.optim.Adam([labels],lr=.05);losses=[]
        for it in range(24):
            budget();opt.zero_grad(set_to_none=True)
            loss=(flow.predict(flow.solve(labels,1/32,8),v)-target).square().mean()
            assert torch.isfinite(loss);loss.backward();assert torch.isfinite(labels.grad).all()
            losses.append(float(loss));opt.step()
            with torch.no_grad():labels.clamp_(-3,3)
        with torch.no_grad():
            mse=float((dense.predict(dense.solve(labels,1/32,8),test)-truth).square().mean())
            fine=float((dense.predict(dense.solve(labels,1/64,8),test)-truth).square().mean())
        dirname='hypergradient_pilot101' if a.seed==101 else 'hypergradient_confirm201_205'
        old=json.loads((ROOT/f'data/generated/response_memory_use_cases_20261001/{dirname}/seed{a.seed}_{kind}.json').read_text())
        row=dict(kind=kind,labels=labels,losses=losses,dense_mse=mse,refined_dense_mse=fine,label_max_difference=float((labels.detach()-torch.tensor(old['labels'])).abs().max()),mse_difference=abs(mse-old['dense_test_mse']),refined_mse_difference=abs(fine-old['refined_dense_test_mse']))
        row['pass']=row['label_max_difference']<2e-4 and row['mse_difference']<2e-5
        result['designs'].append(row);save('reproduction.json',result)
        print(json.dumps({k:v for k,v in row.items() if k not in ['labels','losses']}),flush=True)
    # Independent dense RHS oracle, using differentiation of the scalar loss.
    budget();xd,yd=hg.circle(8,.13,'cpu',torch.float64);vd,td=hg.circle(32,.37,'cpu',torch.float64)
    d=hg.FunctionalFlow(xd,32,101,'dense');state=d.solve(yd,1/32,1)
    w,W,c=[z.detach().requires_grad_() for z in state]
    loss=((c@torch.tanh(W@torch.tanh(w@xd.T))/32-yd)**2).mean()
    grads=torch.autograd.grad(loss,(w,W,c));rhs=d.rhs((w,W,c),yd)
    result['dense_rhs_oracle_error']=max(float((r+m*g).abs().max()) for r,g,m in zip(rhs,grads,[32,1,32]))
    # Materialize the closure matrix and construct each mode derivative literally.
    q=hg.FunctionalFlow(xd,32,101,'q4');state=q.solve(yd,1/32,1);w,c,A,B,s=state
    W=q.W0.clone()
    for j in range(4):
        for b in range(8):W=W-2/(32*8*(1+s))*(2*j+1)*torch.outer(A[j,:,b],B[j,:,b])
    h1=torch.tanh(w@xd.T);h2=torch.tanh(W@h1);r=c@h2/32-yd;rho=r.square().mean().sqrt()
    delta2=(1-h2*h2)*c[:,None];delta1=(1-h1*h1)*(W.T@delta2)
    def transport(M,source):
        return torch.stack([source-rho/(1+s)*(j*M[j]+sum(((2*k+1)*M[k] for k in range(j)),torch.zeros_like(M[0]))) for j in range(4)])
    oracle=(-2/8*(delta1*r)@xd,-2/8*h2@r,transport(A,delta2*r),transport(B,rho*h1),rho)
    result['q4_materialized_rhs_error']=max(float((u-v).abs().max()) for u,v in zip(oracle,q.rhs(state,yd)))
    direction=torch.arange(1,9,dtype=torch.float64);direction/=direction.norm();rows=[]
    for kind in ['dense','q1']:
        budget();flow=hg.FunctionalFlow(xd,32,101,kind)
        def objective(lab):return (flow.predict(flow.solve(lab,1/32,8),vd)-td).square().mean()
        label=yd.clone().requires_grad_();g=torch.autograd.grad(objective(label),label)[0];exact=float(g@direction)
        row=dict(kind=kind,directional_autograd=exact)
        for eps in [1e-4,5e-5]:
            fd=float((objective(yd+eps*direction)-objective(yd-eps*direction))/(2*eps))
            row[str(eps)]=dict(fd=fd,relative_error=abs(fd-exact)/abs(exact))
        # Matched block-16 checkpointing at full physical horizon.
        def block(lab,*values):
            for _ in range(16):values=tuple(v+dv/32 for v,dv in zip(values,flow.rhs(values,lab)))
            return values
        label=yd.clone().requires_grad_();state=flow.initial()
        for _ in range(16):state=checkpoint(block,label,*state,use_reentrant=False)
        cp=torch.autograd.grad((flow.predict(state,vd)-td).square().mean(),label)[0]
        row['checkpoint_gradient_max_difference']=float((cp-g).abs().max());rows.append(row)
    result['T8_derivative_checks']=rows
    # Demonstrate that detaching activity dynamics changes the derivative.
    flow=hg.FunctionalFlow(xd,32,101,'q1');label=yd.clone().requires_grad_();state=flow.initial()
    for _ in range(256):
        rhs=flow.rhs(state,label)
        rhs=(*rhs[:-1],rhs[-1].detach())
        state=tuple(v+dv/32 for v,dv in zip(state,rhs))
    gd=torch.autograd.grad((flow.predict(state,vd)-td).square().mean(),label)[0]
    result['clock_detachment_gradient_relative_difference']=float((gd-g).norm()/g.norm())
    result.update(cpu_seconds=time.process_time()-started,wall_seconds=time.monotonic()-wall,end_utc=hg.utc())
    save('reproduction.json',result);print(json.dumps(hg.plain(result),indent=2),flush=True)

if __name__=='__main__':main()
