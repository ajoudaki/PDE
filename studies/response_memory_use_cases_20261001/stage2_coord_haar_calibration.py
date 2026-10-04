"""Review-requested offline Haar calibration. No training or frozen-file mutation."""
import argparse
import json
from pathlib import Path
import shutil
import sys
import time
import numpy as np
import torch
from stage2_coord_experiment import new_model,scores,scalar,rel,sha,dump
from stage2_coord_curriculum import groups,measure

HERE=Path(__file__).resolve().parent


def positive_qr(A):
    Q,R=torch.linalg.qr(A)
    diagonal=torch.diag(R)
    if bool((diagonal==0).any()):raise RuntimeError('Zero QR diagonal')
    signs=diagonal.sign()
    return Q*signs[None,:],signs[:,None]*R,Q


def tiny_checks(device):
    g=torch.Generator(device=device).manual_seed(720251)
    rand=lambda *shape:torch.randn(shape,generator=g,device=device,dtype=torch.float64)
    Y=rand(7,9);perm=torch.tensor([2,6,1,3,0,5,4],device=device);yp=Y[perm]
    A=rand(8,8);Q,R,_=positive_qr(A);O=positive_qr(rand(8,8))[0]
    transformed=positive_qr(O@A)[0]
    errors=dict(coordinate_gram=rel(yp.T@yp,Y.T@Y),time_gram_conjugacy=rel(yp@yp.T,(Y@Y.T)[perm][:,perm]),
         positive_qr_equivariance=rel(transformed,O@Q),qr_reconstruction=rel(Q@R,A),
         qr_orthogonality=rel(Q.T@Q,torch.eye(8,device=device,dtype=torch.float64)))
    for value in (-2.,3.):
        aa=torch.tensor([[value]],device=device,dtype=torch.float64)
        qq,rr,_=positive_qr(aa)
        if scalar(qq[0,0])!=np.sign(value) or scalar(rr[0,0])!=abs(value):raise AssertionError('Scalar QR')
    if max(errors.values())>1e-9:raise AssertionError(errors)
    return errors


def directions(E,seed):
    s=torch.linalg.svdvals(E);n=E.shape[0]
    g=torch.Generator(device=E.device).manual_seed(seed)
    torch.randint(0,2,(n,),generator=g,device=E.device,dtype=torch.int64) # Original stream alignment.
    A=torch.randn(E.shape,generator=g,device=E.device,dtype=E.dtype)
    B=torch.randn(E.shape,generator=g,device=E.device,dtype=E.dtype)
    L,RL,oldL=positive_qr(A);R,RR,oldR=positive_qr(B)
    new=(L*s)@R.T;old=(oldL*s)@oldR.T;eye=torch.eye(n,device=E.device,dtype=E.dtype)
    gates=dict(left_orthogonality=rel(L.T@L,eye),right_orthogonality=rel(R.T@R,eye),
         left_qr_reconstruction=rel(L@RL,A),right_qr_reconstruction=rel(R@RR,B),
         singular_spectrum=rel(torch.linalg.svdvals(new),s),norm=abs(scalar(new.norm()/E.norm())-1),
         left_gram_formula=rel(new@new.T,(L*s.square())@L.T),
         right_gram_formula=rel(new.T@new,(R*s.square())@R.T))
    if min(scalar(torch.diag(RL).min()),scalar(torch.diag(RR).min()))<=0:raise AssertionError('QR positivity')
    if max(gates.values())>1e-9:raise AssertionError(gates)
    return old,new,gates


@torch.no_grad()
def main():
    p=argparse.ArgumentParser();p.add_argument('--generated',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--device',default='cuda:1');a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
    freeze=HERE/'STAGE2_COORD_FROZEN_MANIFEST.json';frozen=json.loads(freeze.read_text())
    before={name:sha(HERE/name) for name in frozen['source_hashes']}
    if before!=frozen['source_hashes']:raise RuntimeError('Frozen sources differ before calibration')
    start=time.perf_counter();oracles=tiny_checks(a.device)
    sources=['stage2_coord_haar_calibration.py','STAGE2_COORD_REVIEW_CORRECTION.md']
    for name in sources:shutil.copy2(HERE/name,a.out/name)
    inputs={str(freeze):sha(freeze)};rows=[];n_directions=0
    manifest=dict(command=sys.argv,source_hashes={s:sha(HERE/s) for s in sources},frozen_manifest_sha256=sha(freeze),
         torch=torch.__version__,numpy=np.__version__,device=a.device,dtype='float64',tf32=False,threads=torch.get_num_threads(),
         seed_rule='Exact original control seeds and Gaussian draws; QR signs alone corrected.',oracles=oracles)
    dump(a.out/'manifest.json',manifest)
    try:
        for run in ('stage2_coord_confirm01','stage2_coord_curriculum01'):
            folder=a.generated/run;datafolder=a.generated/'stage2_data01'
            results=json.loads((folder/'results.json').read_text());inputs[str(folder/'results.json')]=sha(folder/'results.json')
            for r in results:
                if time.perf_counter()-start>300:raise RuntimeError('Five-minute cap')
                domain=r['domain'];seed=r['seed'];schedule=r.get('schedule','endpoint')
                npz=folder/f'{domain}_seed{seed}_{schedule}.npz';inputs[str(npz)]=sha(npz)
                z=np.load(npz);datafile=datafolder/(domain+'.npz');inputs[str(datafile)]=sha(datafile)
                data=dict(np.load(datafile));f=new_model(data,r['n'],seed,a.device)
                for param,key in zip(f.state,('first','hidden','readout')):param.copy_(torch.as_tensor(z[key],device=a.device))
                baseW=f.matrices[0].clone();base=r['base']
                curriculum=run=='stage2_coord_curriculum01';masks=groups(data,domain)[0] if curriculum else None
                editnames=('swap','within') if curriculum else ('reverse',)
                preds={};case=[]
                for kind in editnames:
                    E=torch.as_tensor(z['edit_'+kind],device=a.device)
                    for j in range(1 if curriculum else 5):
                        control_seed=130000+seed*20+(100 if kind=='within' else 0) if curriculum else 91000+seed*10+j
                        old,new,gates=directions(E,control_seed)
                        oldkey=kind+'_spectral' if curriculum else 'spectral_'+str(j)
                        measured={};oldscore_error=0.
                        for tag,edit in (('old_qr',old),('haar',new)):
                            f.matrices[0].copy_(baseW+edit)
                            metrics,pred=(measure(f,data,masks) if curriculum else scores(f,data))
                            if tag=='old_qr':
                                oldscore_error=max(abs(metrics[k]-r['edits'][oldkey][k]) for k in ('train_mse','val_mse','test_mse'))
                                if oldscore_error>1e-10:raise AssertionError(('old replay',run,domain,seed,kind,j,oldscore_error))
                            metrics['test_relative_change']=metrics['test_mse']/base['test_mse']-1
                            measured[tag]=metrics
                            pp=pred['test'].cpu().numpy() if isinstance(pred['test'],torch.Tensor) else pred['test']
                            preds[f'{kind}_{j}_{tag}']=pp
                        row=dict(run=run,domain=domain,seed=seed,schedule=schedule,edit=kind,draw=j,control_seed=control_seed,
                            invariants=gates,old_score_replay_error=oldscore_error,metrics=measured)
                        rows.append(row);case.append(row);n_directions+=1
                name=f'{run}_{domain}_seed{seed}_{schedule}'
                dump(a.out/(name+'.json'),case);np.savez_compressed(a.out/(name+'.npz'),**preds)
        after={name:sha(HERE/name) for name in frozen['source_hashes']}
        if after!=before:raise RuntimeError('Frozen source changed during calibration')
        summary={}
        for run in ('stage2_coord_confirm01','stage2_coord_curriculum01'):
            for d in ('fashion','housing','har'):
                rr=[r for r in rows if r['run']==run and r['domain']==d]
                for schedule in sorted({r['schedule'] for r in rr}):
                    for edit in sorted({r['edit'] for r in rr}):
                        ss=[r for r in rr if r['schedule']==schedule and r['edit']==edit]
                        # First take the median over orientations within each endpoint, then the median over seeds.
                        perseed={}
                        for seed in sorted({r['seed'] for r in ss}):
                            tt=[r for r in ss if r['seed']==seed]
                            perseed[str(seed)]={tag:float(np.median([r['metrics'][tag]['test_relative_change'] for r in tt])) for tag in ('old_qr','haar')}
                        summary[f'{run}/{d}/{schedule}/{edit}']=dict(per_seed=perseed,
                            old_median=float(np.median([v['old_qr'] for v in perseed.values()])),
                            haar_median=float(np.median([v['haar'] for v in perseed.values()])))
        dump(a.out/'results.json',rows)
        dump(a.out/'summary.json',dict(comparisons=summary,directions=n_directions,endpoint_count=60,
              max_invariant_error=max(max(r['invariants'].values()) for r in rows),
              max_old_replay_score_error=max(r['old_score_replay_error'] for r in rows),oracles=oracles,
              frozen_sources_unchanged=True,primary_gates_unchanged=True,input_hashes=inputs))
        dump(a.out/'completion.json',dict(exit_status=0,seconds=time.perf_counter()-start,new_training_fits=0,
            corrected_directions=n_directions,output_hashes={p.name:sha(p) for p in a.out.glob('*.npz')}))
        print(json.dumps(dict(directions=n_directions,seconds=time.perf_counter()-start,summary=summary),indent=2))
    except Exception as exc:
        dump(a.out/'failure.json',dict(error=repr(exc),seconds=time.perf_counter()-start,directions=n_directions));raise


if __name__=='__main__':main()
