"""Bounded initialized neuron-sampling diagnostic; see GPU_SAMPLING_PROTOCOL.md.

Uses maintained NetworkEngine initialization and equations. The batched hot
path below is verified against its public RHS and Heun step. Small networks
store K=B diag(mu)^-1, an exact weighted-coordinate change, not a new flow.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import shutil
import sys
import time

for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ.setdefault(key, '1')
import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code'))
from pde.finite_torch import NetworkEngine
from pde.observable_torch_p1 import TensorState
from pde.closure_comparison import prediction_metrics


@dataclass
class Batch:
    A: torch.Tensor
    M: torch.Tensor
    w: torch.Tensor

    def arrays(self):
        return self.A, self.M, self.w

    def clone(self):
        return Batch(*(x.clone() for x in self.arrays()))


def settings():
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.set_float32_matmul_precision('highest')


def fields(s, U, masses=None):
    h = torch.tanh(s.A @ U.T)
    if masses is None:
        g = torch.tanh(s.M @ h)
        f = (s.w[:, :, None] * g).mean(dim=1)
    else:
        mu, nu = masses
        g = torch.tanh(s.M @ (mu[:, :, None] * h))
        f = ((nu*s.w)[:, :, None] * g).sum(dim=1)
    return h, g, f


def rhs(s, U, labels, masses=None):
    h, g, f = fields(s, U, masses)
    c = labels - f  # 2/m=1 for the two equally weighted training samples.
    delta = s.w[:, :, None] * (1-g.square())
    if masses is None:
        backward = s.M.transpose(1, 2) @ delta
        dM = (delta*c[:, None, :]) @ h.transpose(1, 2) / s.A.shape[1]
    else:
        mu, nu = masses
        backward = s.M.transpose(1, 2) @ (nu[:, :, None]*delta)
        dM = (delta*c[:, None, :]) @ h.transpose(1, 2)
    dA = (backward * (1-h.square()) * c[:, None, :]) @ U
    dw = (g*c[:, None, :]).sum(dim=2)
    return Batch(dA, dM, dw)


def heun(s, U, labels, dt, masses=None):
    k = rhs(s, U, labels, masses)
    stage = Batch(*(a+dt*b for a, b in zip(s.arrays(), k.arrays())))
    ell = rhs(stage, U, labels, masses)
    return Batch(*(a+(dt/2)*(b+c) for a, b, c in
                   zip(s.arrays(), k.arrays(), ell.arrays())))


def max_difference(a, b):
    return max(float((x-y).detach().abs().max()) for x,y in zip(a.arrays(), b.arrays()))


def validate_core(device):
    dtype = torch.float64
    engine = NetworkEngine(2, 7, 811, device=device, dtype=dtype)
    state = engine.initial_state()
    state.c.copy_(torch.linspace(-.3, .2, 7, device=device, dtype=dtype))
    U = torch.tensor([[1., 0.], [.6, .8]], device=device, dtype=dtype)
    y = torch.tensor([.2, -.1], device=device, dtype=dtype)
    data = engine.prepare_data(U, y)
    s = Batch(state.w[None], state.M[None], state.c[None])
    public = engine.rhs(state, data)
    expected = Batch(public.w[None], public.M[None], public.c[None])
    errors = {'rhs_public': max_difference(rhs(s,U,y),expected)}
    public_next = engine.heun_step(state, data, .02)
    expected_next = Batch(public_next.w[None],public_next.M[None],public_next.c[None])
    errors['heun_public'] = max_difference(heun(s,U,y,.02), expected_next)
    mass = torch.full((1,7),1/7,device=device,dtype=dtype)
    weighted = Batch(s.A.clone(),s.M*7,s.w.clone())
    wrhs = rhs(weighted,U,y,(mass,mass))
    converted = Batch(wrhs.A,wrhs.M/7,wrhs.w)
    errors['uniform_weighted_rhs'] = max_difference(converted,expected)
    wn = heun(weighted,U,y,.02,(mass,mass))
    errors['uniform_weighted_heun'] = max_difference(Batch(wn.A,wn.M/7,wn.w),expected_next)

    # Nonuniform rectangular gradient identity, independent autograd oracle.
    gen = torch.Generator(device=device).manual_seed(839)
    A = torch.randn((1,4,2),generator=gen,device=device,dtype=dtype).requires_grad_()
    K = (.2*torch.randn((1,3,4),generator=gen,device=device,dtype=dtype)).requires_grad_()
    w = (.2*torch.randn((1,3),generator=gen,device=device,dtype=dtype)).requires_grad_()
    mu = torch.tensor([[.1,.2,.3,.4]],device=device,dtype=dtype)
    nu = torch.tensor([[.2,.3,.5]],device=device,dtype=dtype)
    z = Batch(A,K,w)
    f = fields(z,U,(mu,nu))[2]
    loss = (f-y).square().mean()
    gradients = torch.autograd.grad(loss,(A,K,w))
    oracle = Batch(-gradients[0]/mu[:,:,None],
                   -gradients[1]/(nu[:,:,None]*mu[:,None,:]),
                   -gradients[2]/nu)
    actual = rhs(z,U,y,(mu,nu))
    errors['weighted_autograd'] = max_difference(actual,oracle)
    a = Batch(*(v.detach() for v in z.arrays()))
    with torch.no_grad():
        uninterrupted = a.clone()
        for _ in range(6): uninterrupted = heun(uninterrupted,U,y,.01,(mu,nu))
        first = a.clone()
        for _ in range(3): first = heun(first,U,y,.01,(mu,nu))
        # Array-only save/load round trip; no initialization or full-state input.
        recovered = Batch(*(torch.from_numpy(v.cpu().numpy().copy()).to(device) for v in first.arrays()))
        for _ in range(3): recovered = heun(recovered,U,y,.01,(mu,nu))
    errors['restart'] = max_difference(uninterrupted,recovered)
    assert max(errors.values()) < 2e-12, errors
    return errors


def state_schedule(n):
    result=[]
    for anchor in (128,256,512):
        for p in (1,2):
            budget=anchor*(math.log(n)/math.log(512))**p
            width=int(math.floor((-5+math.sqrt(1+4*budget))/2))
            while width*width+5*width+6 > budget+1e-10: width-=1
            result.append({'anchor':anchor,'p':p,'budget':budget,'width':width,
                           'moving':width*width+3*width,'fixed':2*width+6,
                           'total':width*width+5*width+6})
    return result


def make_dense(n,seed,device,dtype):
    engines=[NetworkEngine(2,n,s,device='cpu',dtype=torch.float64) for s in (seed,seed+10000)]
    A=np.stack([e.initial.w.numpy() for e in engines])
    M=np.stack([e.initial.M.numpy() for e in engines])
    state=Batch(torch.tensor(A,device=device,dtype=dtype),
                torch.tensor(M,device=device,dtype=dtype),
                torch.zeros((2,n),device=device,dtype=dtype))
    return state,A[0].copy(),M[0].copy()


def pack_samplers(samplers,device,dtype):
    count=len(samplers); size=max(len(s['mu']) for s in samplers)
    A=np.zeros((count,size,2)); K=np.zeros((count,size,size)); w=np.zeros((count,size))
    mu=np.zeros((count,size)); nu=np.zeros((count,size))
    for j,s in enumerate(samplers):
        n1,n2=len(s['mu']),len(s['nu'])
        A[j,:n1]=s['A']; K[j,:n2,:n1]=s['B']/s['mu'][None,:]
        w[j,:n2]=s['w']; mu[j,:n1]=s['mu']; nu[j,:n2]=s['nu']
    tensor=lambda x:torch.tensor(x,device=device,dtype=dtype)
    return Batch(tensor(A),tensor(K),tensor(w)),(tensor(mu),tensor(nu))


def feature_motion(h,g,h0,g0,masses=None):
    if masses is None:
        first=(h-h0).square().mean(dim=(1,2)).sqrt()
        second=(g-g0).square().mean(dim=(1,2)).sqrt()
    else:
        first=((h-h0).square()*masses[0][:,:,None]).sum(dim=1).mean(dim=1).sqrt()
        second=((g-g0).square()*masses[1][:,:,None]).sum(dim=1).mean(dim=1).sqrt()
    return torch.stack((first,second),dim=1)


def comparison_metrics(predictions, n):
    errors=predictions-predictions[:,0:1,:]
    result=[]
    for j in range(predictions.shape[1]):
        e=errors[:,j,:]
        endpoint=prediction_metrics(predictions[-1,j],predictions[-1,0],
            ids=np.arange(e.shape[1]),reference_ids=np.arange(e.shape[1]))['overall']
        result.append({'sup_panel_time':float(np.abs(e).max()),
            'rms_of_time_sup':float(np.sqrt(np.mean(np.max(np.abs(e),axis=0)**2))),
            'endpoint':endpoint,
            'scaled_sup':float(math.sqrt(n)*np.abs(e).max())})
    baseline=result[1]['sup_panel_time']
    for record in result:
        record['ratio_to_dense_copy']=record['sup_panel_time']/baseline if baseline>0 else None
    return result


@torch.no_grad()
def run_case(n,seed,angle,sign,args,out,deadline):
    from neuron_sampling_setup import prepare_witness,build_sampler
    begin=time.perf_counter(); device=args.device
    case_id=f'n{n}_s{seed}_a{angle:g}_sign{sign:+d}'
    case_out=out/case_id; case_out.mkdir()
    dtype=getattr(torch,args.dtype)
    U_np=np.array([[1.,0.],[math.cos(math.radians(angle)),math.sin(math.radians(angle))]])
    labels_np=np.array([.2,.1*sign])
    U=torch.tensor(U_np,device=device,dtype=dtype)
    labels=torch.tensor(labels_np,device=device,dtype=dtype)
    dense,A0,W0=make_dense(n,seed,device,dtype)
    schedule=state_schedule(n); widths=sorted({r['width'] for r in schedule})
    witness=prepare_witness(A0,W0,U_np,labels_np,probe_count=16)
    samplers=[build_sampler(A0,W0,U_np,labels_np,k,probe_count=16,witness=witness) for k in widths]
    small,masses=pack_samplers(samplers,device,dtype)
    setup_seconds=time.perf_counter()-begin
    model_names=['dense_reference','dense_independent']+[f'sampled_N{k}' for k in widths]+['frozen_dense_hidden']
    for row in schedule: row['model_index']=2+widths.index(row['width'])
    for s in samplers: assert np.all(s['mu']>0) and np.all(s['nu']>0)
    phi=2*np.pi*(np.arange(args.panel)+args.panel_offset)/args.panel
    panel_np=np.stack((np.cos(phi),np.sin(phi)),axis=1)
    panel=torch.tensor(panel_np,device=device,dtype=dtype)
    hd0,gd0,_=fields(dense,U)
    hs0,gs0,_=fields(small,U,masses)
    gquery0=fields(dense,panel)[1][0]
    gram=(gd0[0].T @ gd0[0]/n).cpu().numpy()
    cross=(gd0[0].T @ gquery0/n).cpu().numpy()
    evals,evecs=np.linalg.eigh(gram)
    times=[]; predictions=[]; residuals=[]; motions=[]; training_predictions=[]
    def observe(t):
        if time.perf_counter()>deadline: raise TimeoutError('worker hard budget exceeded')
        if torch.cuda.max_memory_allocated(device)>8*2**30: raise MemoryError('8 GiB GPU budget exceeded')
        for state in (dense,small):
            if not all(bool(torch.isfinite(v).all()) for v in state.arrays()): raise FloatingPointError('nonfinite state')
        hd,gd,fd=fields(dense,U)
        hs,gs,fs=fields(small,U,masses)
        pd=fields(dense,panel)[2].cpu().numpy()
        ps=fields(small,panel,masses)[2].cpu().numpy()
        coeff=evecs @ ((-np.expm1(-evals*t)/evals)*(evecs.T@labels_np))
        frozen=coeff@cross
        training_frozen=coeff@gram
        predictions.append(np.concatenate((pd,ps,frozen[None]),axis=0))
        fit=np.concatenate((fd.cpu().numpy(),fs.cpu().numpy(),training_frozen[None]),axis=0)
        training_predictions.append(fit)
        residuals.append(np.sqrt(np.mean((fit-labels_np)**2,axis=1)))
        motion=torch.cat((feature_motion(hd,gd,hd0,gd0),feature_motion(hs,gs,hs0,gs0,masses)),dim=0)
        motions.append(np.concatenate((motion.cpu().numpy(),np.zeros((1,2))),axis=0))
        times.append(t)
    observe(0.)
    stride=round(args.observe_every/args.dt)
    assert abs(stride*args.dt-args.observe_every)<1e-10 and stride>=1
    first_steps=round(args.horizon/args.dt); max_steps=round(args.max_horizon/args.dt)
    end_step=first_steps
    start_evolution=time.perf_counter()
    try:
        for step in range(1,max_steps+1):
            dense=heun(dense,U,labels,args.dt)
            small=heun(small,U,labels,args.dt,masses)
            if step%stride==0: observe(round(step*args.dt,10))
            if step==first_steps:
                if np.max(residuals[-1][:-1]) <=1e-6: break
                end_step=max_steps
            if step>=end_step: break
    except BaseException:
        np.savez_compressed(case_out/'partial_observations.npz',times=np.asarray(times),panel=panel_np,
            predictions=np.asarray(predictions),training_predictions=np.asarray(training_predictions),
            residual_rms=np.asarray(residuals),feature_motion=np.asarray(motions),labels=labels_np,U=U_np)
        raise
    torch.cuda.synchronize(device)
    evolution_seconds=time.perf_counter()-start_evolution
    if times[-1]!=round(step*args.dt,10): observe(round(step*args.dt,10))
    times=np.array(times); predictions=np.array(predictions); residuals=np.array(residuals); motions=np.array(motions)
    lag=max(0,len(times)-1-round(10/args.observe_every))
    tail=np.max(np.abs(predictions[-1]-predictions[lag]),axis=1)
    settled=(residuals[-1]<=1e-6)&(tail<=1e-5)
    metrics=comparison_metrics(predictions,n)
    # Own compressed final state, sufficient to restart without reference arrays.
    states={}
    for j,k in enumerate(widths):
        states[f'A_{k}']=small.A[j,:k].cpu().numpy()
        states[f'K_{k}']=small.M[j,:k,:k].cpu().numpy()
        states[f'w_{k}']=small.w[j,:k].cpu().numpy()
        states[f'mu_{k}']=masses[0][j,:k].cpu().numpy()
        states[f'nu_{k}']=masses[1][j,:k].cpu().numpy()
    np.savez_compressed(case_out/'reduced_restart.npz',U=U_np,labels=labels_np,**states)
    np.savez_compressed(case_out/'observations.npz',times=times,panel=panel_np,predictions=predictions,
                        training_predictions=np.asarray(training_predictions),
                        residual_rms=residuals,feature_motion=motions,labels=labels_np,U=U_np)
    record={'n':n,'seed':seed,'copy_seed':seed+10000,'angle':angle,'sign':sign,'labels':labels_np.tolist(),
        'dt':args.dt,'dtype':args.dtype,'model_names':model_names,'widths':widths,'schedule':schedule,
        'initial_gram_eigenvalues':evals.tolist(),'metrics':metrics,'last_residual_rms':residuals[-1].tolist(),
        'last_ten_time_change':tail.tolist(),'settled':settled.tolist(),'last_time':float(times[-1]),
        'feature_motion_final':motions[-1].tolist(),'setup_seconds':setup_seconds,
        'evolution_seconds':evolution_seconds,'total_seconds':time.perf_counter()-begin,
        'sampler_diagnostics':[s['diagnostics'] for s in samplers]}
    for filename in ('observations.npz','reduced_restart.npz'):
        record[filename+'_sha256']=hashlib.sha256((case_out/filename).read_bytes()).hexdigest()
    (case_out/'record.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'case':case_id,'seconds':round(record['total_seconds'],2),
       'T':record['last_time'],'dense_error':metrics[1]['sup_panel_time'],
       'sample_errors':[r['sup_panel_time'] for r in metrics[2:-1]],
       'settled':settled.tolist()}),flush=True)
    return record


def provenance(out,args):
    paths=[Path(__file__),Path(__file__).with_name('neuron_sampling_setup.py'),
           Path(__file__).with_name('GPU_SAMPLING_PROTOCOL.md'),
           ROOT/'code/pde/finite_torch.py',ROOT/'code/pde/finite_network.py',
           ROOT/'code/pde/observable_torch_p1.py',ROOT/'code/pde/closure_comparison.py']
    source_dir=out/'sources';source_dir.mkdir()
    hashes={}
    for path in paths:
        if path.exists():
            hashes[str(path.relative_to(ROOT))]=hashlib.sha256(path.read_bytes()).hexdigest()
            shutil.copy2(path,source_dir/path.name)
    meta={'args':vars(args),'argv':sys.argv,'cwd':os.getcwd(),'python':sys.version,'executable':sys.executable,
          'platform':platform.platform(),'numpy':np.__version__,'torch':torch.__version__,
          'cuda':torch.version.cuda,'gpu':torch.cuda.get_device_name(args.device),
          'source_hashes':hashes,'threads':torch.get_num_threads(),'tf32':torch.backends.cuda.matmul.allow_tf32}
    (out/'provenance.json').write_text(json.dumps(meta,indent=2)+'\n')


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--mode',choices=('validate','pilot','run','refine'),default='run')
    p.add_argument('--device',default='cuda:0');p.add_argument('--output',required=True)
    p.add_argument('--angle',type=float,default=90.)
    p.add_argument('--dtype',choices=('float32','float64'),default='float64')
    p.add_argument('--dt',type=float,default=.2);p.add_argument('--panel',type=int,default=257)
    p.add_argument('--panel-offset',type=float,default=.5)
    p.add_argument('--observe-every',type=float,default=1.)
    p.add_argument('--horizon',type=float,default=120.);p.add_argument('--max-horizon',type=float,default=240.)
    p.add_argument('--budget-seconds',type=float,default=1200.)
    args=p.parse_args();settings()
    out=Path(args.output).resolve();out.mkdir(parents=True,exist_ok=False)
    provenance(out,args)
    started=time.perf_counter();deadline=started+args.budget_seconds
    status={'completed':[],'failures':[]}
    try:
        checks=validate_core(args.device)
        (out/'core_validation.json').write_text(json.dumps(checks,indent=2)+'\n')
        print(json.dumps({'core_validation':checks}),flush=True)
        if args.mode=='validate': return
        if args.mode=='pilot': cases=[(512,6291,60.,-1)]
        elif args.mode=='refine': cases=[(2048,7301,60.,-1)]
        else: cases=[(n,s,args.angle,sign) for n in (512,1024,2048) for s in (7301,7302,7303) for sign in (1,-1)]
        for n,seed,angle,sign in cases:
            try:
                record=run_case(n,seed,angle,sign,args,out,deadline)
                status['completed'].append({k:record[k] for k in ('n','seed','angle','sign','total_seconds')})
            except Exception as exc:
                status['failures'].append({'n':n,'seed':seed,'angle':angle,'sign':sign,'error':repr(exc)})
                (out/'status.json').write_text(json.dumps(status,indent=2)+'\n')
                raise
            (out/'status.json').write_text(json.dumps(status,indent=2)+'\n')
    finally:
        status['wall_seconds']=time.perf_counter()-started
        status['peak_gpu_allocated']=torch.cuda.max_memory_allocated(args.device)
        (out/'status.json').write_text(json.dumps(status,indent=2)+'\n')


if __name__=='__main__':
    main()
