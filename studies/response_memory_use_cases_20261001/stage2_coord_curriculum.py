"""Frozen support-only curriculum experiment; see STAGE2_COORD_CURRICULUM_PROTOCOL.md."""
import argparse
import json
from pathlib import Path
import shutil
import sys
import time
import numpy as np
import torch
from stage2_coord_experiment import (new_model,interaction,controls,rel,scalar,sha,dump)
from history_probe import interval_coefficients

HERE=Path(__file__).resolve().parent


def groups(data,domain):
    train=data['X_train'][:512]
    if domain=='har':
        ids=np.unique(data['subject_train'][:512]);k=len(ids)//2
        threshold=float((ids[k-1]+ids[k])/2)
        masks={s:np.asarray(data['subject_'+s])<=threshold for s in ('train','val','test')}
    else:
        coordinate=lambda X: (X[:,:-1]/X[:,-1:]).mean(1) if domain=='fashion' else X[:,7]/X[:,-1]
        threshold=float(np.median(coordinate(train)))
        masks={s:coordinate(data['X_'+s])<=threshold for s in ('train','val','test')}
    masks['train']=masks['train'][:512]
    for split,mask in masks.items():
        if split!='val' and (not mask.any() or mask.all()):raise RuntimeError(('empty group',domain,split))
    for mask in (masks['train'],~masks['train']):
        if domain!='housing' and len(np.unique(data['y_train'][:512][mask]))!=2:
            raise RuntimeError(('single-class group',domain))
    meta=dict(threshold=threshold,counts={},labels={})
    for s,mask in masks.items():
        y=data['y_'+s][:len(mask)]
        meta['counts'][s]=[int(mask.sum()),int((~mask).sum())]
        meta['labels'][s]=[float(y[mask].mean()) if mask.any() else None,float(y[~mask].mean()) if (~mask).any() else None]
    return masks,meta


def phase_weights(mask,device):
    a=torch.as_tensor(mask,device=device,dtype=torch.float64);b=1-a
    return a/a.sum(),b/b.sum()


def schedule_weights(name,N,wa,wb):
    if name=='joint':return ((wa+wb)/2)[None].expand(N,-1)
    i=torch.arange(N,device=wa.device)
    if name=='AB':usea=i<N//2
    elif name=='BA':usea=i>=N//2
    elif name=='alternating':usea=(i//(N//8))%2==0
    else:raise ValueError(name)
    return torch.where(usea[:,None],wa[None],wb[None])


def weighted_fields(f,lam):
    h=(f.w@f.inputs.T).tanh();h2=(f.matrices[0]@h).tanh()
    r=f.c@h2/f.n-f.labels;weighted_r=f.M*lam*r
    b=f.c[:,None]*(1-h2.square())*weighted_r
    v1=(-2/f.M)*((f.matrices[0].T@b)*(1-h.square()))@f.inputs
    v2=(-2/(f.M*f.n))*b@h.T
    vc=(-2/f.M)*h2@weighted_r
    return h,b,(v1,v2,vc)


@torch.no_grad()
def measure(f,data,masks):
    metrics={};preds={}
    for s in ('train','val','test'):
        x=f.inputs if s=='train' else data['X_'+s]
        y=f.labels if s=='train' else torch.as_tensor(data['y_'+s],device=f.device,dtype=f.dtype)
        pred=f.predict(x);preds[s]=pred
        squared=(pred-y).square();mask=torch.as_tensor(masks[s],device=f.device)
        metrics[s+'_mse']=scalar(squared.mean())
        metrics[s+'_A_mse']=scalar(squared[mask].mean()) if bool(mask.any()) else None
        metrics[s+'_B_mse']=scalar(squared[~mask].mean()) if bool((~mask).any()) else None
        if set(np.unique(data['y_'+s][:len(y)])).issubset({-1.,1.}):
            metrics[s+'_accuracy']=scalar(((pred>=0)==(y>=0)).double().mean())
    metrics['train_balanced_mse']=(metrics['train_A_mse']+metrics['train_B_mse'])/2
    return metrics,preds


@torch.no_grad()
def run(data,domain,n,seed,device,T,dt,schedule):
    masks,meta=groups(data,domain);f=new_model(data,n,seed,device)
    wa,wb=phase_weights(masks['train'],device);N=round(T/dt)
    weights=schedule_weights(schedule,N,wa,wb)
    expected=N*(wa+wb)/2
    exposure=rel(weights.sum(0),expected)
    if exposure>1e-12:raise RuntimeError(('exposure',exposure))
    hs=f.w.new_empty((N,n,f.M));bs=torch.empty_like(hs)
    initial=f.matrices[0].clone();h0=(f.w@f.inputs.T).tanh()
    curves=[dict(t=0.,**measure(f,data,masks)[0])]
    for i in range(N):
        h,b,v=weighted_fields(f,weights[i]);hs[i].copy_(h);bs[i].copy_(b)
        for p,g in zip(f.state,v):p.add_(g,alpha=dt)
        if (i+1)%(N//8)==0:curves.append(dict(t=(i+1)*dt,**measure(f,data,masks)[0]))
    if not all(bool(torch.isfinite(p).all()) for p in f.state):raise RuntimeError('Nonfinite')
    exact=f.matrices[0]-initial;parity=rel(interaction(hs,bs,dt,n,f.M),exact)
    if parity>1e-9:raise RuntimeError(('observer',parity))
    base,preds=measure(f,data,masks)
    h1=(f.w@f.inputs.T).tanh();z=f.w@f.inputs.T
    idx=torch.arange(N,device=device);swap=(idx+N//2)%N
    within=torch.cat((idx[:N//2].flip(0),idx[N//2:].flip(0)))
    edits={'none':torch.zeros_like(exact),
       'swap':interaction(hs,bs[swap],dt,n,f.M)-exact,
       'within':interaction(hs,bs[within],dt,n,f.M)-exact,
       'q1_global':(-2*dt*N/(n*f.M))*(bs.mean(0)@hs.mean(0).T)-exact}
    invariants=dict(exposure=exposure,observer=parity,
       simultaneous_swap=rel(interaction(hs[swap],bs[swap],dt,n,f.M),exact),
       swap_backward_mean=rel(bs[swap].mean(0),bs.mean(0)))
    compression={};coeffs={};K=N//2
    dh=hs[:K]-hs[K:];db=bs[:K]-bs[K:]
    henergy=dt*dh.square().sum((0,1));benergy=dt*db.square().sum((0,1))
    for q in (1,4,8,16):
        C=torch.as_tensor(interval_coefficients(np.full(K,dt),q),device=device,dtype=f.dtype)
        hc=(C@dh.flatten(1)).reshape(q,n,f.M);bc=(C@db.flatten(1)).reshape(q,n,f.M)
        eq=-interaction(hc,bc,1.,n,f.M);edits['swap_q'+str(q)]=eq
        ht=(henergy-hc.square().sum((0,1))).clamp_min(0);bt=(benergy-bc.square().sum((0,1))).clamp_min(0)
        bound=scalar((2/(n*f.M))*(ht*bt).sqrt().sum());err=scalar((eq-edits['swap']).norm())
        if err>bound+1e-9:raise RuntimeError(('swap tail',q,err,bound))
        compression[str(q)]=dict(relative_edit_error=rel(eq,edits['swap']),absolute_error=err,bound=bound)
        if q==8:coeffs=dict(phase_difference_h_q8=hc.cpu().numpy(),phase_difference_b_q8=bc.cpu().numpy())
    edits['swap_centered']=edits['swap']-edits['swap_q1']
    for kind in ('swap','within'):
        for j in range(5):
            sign,iso,gates=controls(edits[kind],130000+seed*20+j+(100 if kind=='within' else 0))
            edits[kind+'_sign_'+str(j)]=sign
            if j==0:edits[kind+'_spectral']=iso
            invariants.update({kind+str(j)+'_'+key:val for key,val in gates.items()})
    for tag,lam in (('joint',(wa+wb)/2),('last',weights[-1])):
        descent=weighted_fields(f,lam)[2][1]
        descent=descent*(edits['swap'].norm()/descent.norm().clamp_min(1e-30))
        edits['gradient_'+tag+'_descent']=descent;edits['gradient_'+tag+'_ascent']=-descent
    if max(invariants.values())>1e-9:raise RuntimeError(('invariants',invariants))
    grad=-weighted_fields(f,(wa+wb)/2)[2][1]
    matrices=f.matrices[0].clone();rows={}
    arrays={k:p.cpu().numpy() for k,p in zip(('first','hidden','readout'),f.state)}
    arrays.update(coeffs)
    arrays.update({k+'_baseline':v.cpu().numpy() for k,v in preds.items()})
    del hs,bs,dh,db,weights
    for name,E in edits.items():
        f.matrices[0].copy_(matrices+E)
        row,pp=measure(f,data,masks)
        for s in ('train','val','test'):row[s+'_prediction_rms']=scalar((pp[s]-preds[s]).square().mean().sqrt())
        row.update(edit_norm=scalar(E.norm()),balanced_linear_change=scalar((grad*E).sum()))
        row['balanced_nonlinear_remainder']=row['train_balanced_mse']-base['train_balanced_mse']-row['balanced_linear_change']
        rows[name]=row
        if name in ('none','swap','within','swap_q1','swap_q8','swap_centered'):
            arrays['edit_'+name]=E.cpu().numpy();arrays['test_pred_'+name]=pp['test'].cpu().numpy()
    return dict(domain=domain,n=n,m=f.M,seed=seed,T=T,dt=dt,schedule=schedule,grouping=meta,
       curves=curves,base=base,edits=rows,compression=compression,invariants=invariants,
       feature_motion=scalar((h1-h0).norm()/h0.norm()),nonlinearity=scalar((z-h1).norm()/z.norm())),arrays


def main():
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--seeds',type=int,nargs='+',required=True)
    p.add_argument('--schedules',nargs='+',default=['joint','AB','BA','alternating'])
    p.add_argument('--dt',type=float,default=1/16);p.add_argument('--width',type=int,default=256)
    p.add_argument('--device',default='cuda:1');p.add_argument('--max-seconds',type=float,default=3600)
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
    sources=['stage2_coord_curriculum.py','stage2_coord_experiment.py','baseline_compact_flow.py','history_probe.py',
             'STAGE2_COORD_CURRICULUM_PROTOCOL.md','STAGE2_COORD_THEORY.md']
    for name in sources:shutil.copy2(HERE/name,a.out/name)
    dump(a.out/'manifest.json',dict(command=sys.argv,source_hashes={s:sha(HERE/s) for s in sources},
         input_hashes={d:sha(a.data/(d+'.npz')) for d in ('fashion','housing','har')},dtype='float64',tf32=False,
         torch=torch.__version__,numpy=np.__version__,device=a.device,threads=torch.get_num_threads(),
         started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())))
    rows=[];start=time.perf_counter();solves=0
    try:
        for domain in ('fashion','housing','har'):
            data=dict(np.load(a.data/(domain+'.npz')))
            for seed in a.seeds:
                for schedule in a.schedules:
                    if time.perf_counter()-start>a.max_seconds:raise RuntimeError('Wall-time cap')
                    begin=time.perf_counter();r,arrays=run(data,domain,a.width,seed,a.device,64.,a.dt,schedule)
                    r['seconds']=time.perf_counter()-begin;name=f'{domain}_seed{seed}_{schedule}'
                    dump(a.out/(name+'.json'),r);np.savez_compressed(a.out/(name+'.npz'),**arrays)
                    rows.append(r);solves+=1;dump(a.out/'results.json',rows)
                    print(json.dumps(dict(case=name,seconds=r['seconds'],base_test=r['base']['test_mse'],
                       swap_test=r['edits']['swap']['test_mse'],within_test=r['edits']['within']['test_mse'],
                       q1_test=r['edits']['swap_q1']['test_mse'],solves=solves)),flush=True)
        dump(a.out/'completion.json',dict(exit_status=0,solves=solves,seconds=time.perf_counter()-start,
            output_hashes={p.name:sha(p) for p in a.out.glob('*.npz')}))
    except Exception as exc:
        dump(a.out/'failure.json',dict(error=repr(exc),solves=solves,seconds=time.perf_counter()-start));raise


if __name__=='__main__':main()
