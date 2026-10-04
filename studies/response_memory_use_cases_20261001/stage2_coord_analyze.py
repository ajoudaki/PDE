"""Fixed aggregation and no-training reflection reconstruction from saved coefficients."""
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import torch
from stage2_coord_experiment import new_model,interaction,scores,rel,sha,dump


def main():
    p=argparse.ArgumentParser();p.add_argument('--runs',type=Path,nargs='+',required=True)
    p.add_argument('--data',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--device',default='cpu');a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
    start=time.perf_counter();rows=[];reflection=[];budgets=[];hashes={}
    for folder in a.runs:
        hashes[str(folder/'results.json')]=sha(folder/'results.json')
        if (folder/'completion.json').exists():
            budgets.append(dict(run=folder.name,**json.loads((folder/'completion.json').read_text())))
        for r in json.loads((folder/'results.json').read_text()):
            r['run']=folder.name;rows.append(r)
            if 'edits' not in r:continue
            path=folder/f"{r['domain']}_seed{r['seed']}_endpoint.npz"
            hashes[str(path)]=sha(path)
            z=np.load(path);data=dict(np.load(a.data/(r['domain']+'.npz')))
            f=new_model(data,r['n'],r['seed'],a.device)
            for target,key in zip(f.state,('first','hidden','readout')):
                target.copy_(torch.as_tensor(z[key],device=a.device))
            base=f.matrices[0].clone();exact=torch.as_tensor(z['edit_reverse'],device=a.device)
            exactpred=torch.as_tensor(z['test_pred_reverse'],device=a.device)
            row=dict(domain=r['domain'],seed=r['seed'],n=r['n'],dt=r['dt'],run=folder.name,modes={})
            for q in (4,8,16,32):
                if 'h_q'+str(q) not in z:continue
                hc=torch.as_tensor(z['h_q'+str(q)],device=a.device)
                bc=torch.as_tensor(z['b_q'+str(q)],device=a.device)
                E=(-2)*interaction(hc[1::2],bc[1::2],1.,r['n'],r['m'])
                f.matrices[0].copy_(base+E)
                pred=f.predict(data['X_test'])
                row['modes'][str(q)]=dict(relative_edit_error=rel(E,exact),
                    prediction_rms_error=float((pred-exactpred).square().mean().sqrt()),
                    test_mse=float((pred-torch.as_tensor(data['y_test'],device=a.device)).square().mean()))
            reflection.append(row)
    confirm=[r for r in rows if r['run']=='stage2_coord_confirm01']
    by_domain={}
    for d in sorted({r['domain'] for r in confirm}):
        rr=[r for r in confirm if r['domain']==d]
        relchange=lambda r,k:(r['edits'][k]['test_mse']/r['base']['test_mse']-1)
        damage=[relchange(r,'reverse') for r in rr]
        sign=[np.median([relchange(r,'sign_'+str(j)) for j in range(5)]) for r in rr]
        nonlinear=[abs(r['edits']['reverse']['train_nonlinear_remainder'])/
             max(abs(r['edits']['reverse']['train_mse']-r['base']['train_mse']),1e-30) for r in rr]
        passed=all(v>0 for v in damage) and np.median(damage)>=.1 and np.median(np.array(damage)-sign)>=.05 and np.median(nonlinear)>=.5
        controls={k:float(np.median([relchange(r,k) for r in rr])) for k in
                  ('q1','gradient_descent','gradient_ascent','opposite_reverse','time_shuffle_0','time_shuffle_1','window_0','window_1','window_2')}
        controls['sign_median']=float(np.median(sign))
        controls['spectral_median']=float(np.median([np.median([relchange(r,'spectral_'+str(j)) for j in range(5)]) for r in rr]))
        continuations={k:float(np.median([r['continuations'][k]['test_mse']/r['continuations']['none']['test_mse']-1 for r in rr])) for k in ('q1','reverse','sign_0','gradient_descent')}
        by_domain[d]=dict(reversal_relative_damage=damage,median_reversal_relative_damage=float(np.median(damage)),
             positive_seeds=sum(v>0 for v in damage),median_excess_over_sign=float(np.median(np.array(damage)-sign)),
             median_nonlinear_fraction=float(np.median(nonlinear)),registered_pass=bool(passed),
             control_median_relative_changes=controls,continuation_median_relative_changes=continuations,
             feature_motion=[r['feature_motion'] for r in rr],
             max_invariant_error=max(max(r['invariants'].values()) for r in rr))
    refine=[]
    for r in rows:
        if r['run']!='stage2_coord_refine01':continue
        coarse=next(z for z in confirm if z['domain']==r['domain'] and z['seed']==r['seed'])
        folder=next(f for f in a.runs if f.name==r['run']);cfolder=next(f for f in a.runs if f.name==coarse['run'])
        z=np.load(folder/f"{r['domain']}_seed{r['seed']}_endpoint.npz")
        c=np.load(cfolder/f"{r['domain']}_seed{r['seed']}_endpoint.npz")
        pred_error=float(np.sqrt(np.mean((z['baseline_pred_test']-c['baseline_pred_test'])**2)))
        fine_effect=r['edits']['reverse']['test_mse']-r['base']['test_mse']
        coarse_effect=coarse['edits']['reverse']['test_mse']-coarse['base']['test_mse']
        effect_change=abs(fine_effect-coarse_effect)
        refine.append(dict(domain=r['domain'],prediction_rms_discrepancy=pred_error,
            coarse_effect=coarse_effect,fine_effect=fine_effect,absolute_effect_change=effect_change,
            resolved=bool(pred_error<=.02 and abs(coarse_effect)>2*effect_change)))
    causal=[r for r in rows if 'final' in r]
    summary=dict(confirmation=by_domain,step_refinement=refine,reflection=reflection,causal=causal,
                 solves=sum(r['solves'] for r in budgets),producer_seconds=sum(r['seconds'] for r in budgets),
                 scientific_runs=[{k:v for k,v in r.items() if k!='output_hashes'} for r in budgets],
                 source_hash=sha(__file__),input_hashes=hashes,analysis_seconds=time.perf_counter()-start)
    dump(a.out/'summary.json',summary)
    print(json.dumps({k:v for k,v in summary.items() if k in ('confirmation','step_refinement','solves','producer_seconds','analysis_seconds')},indent=2))


if __name__=='__main__':
    with torch.no_grad():main()
