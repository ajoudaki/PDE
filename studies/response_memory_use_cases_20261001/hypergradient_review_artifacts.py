"""Audit every frozen data artifact and independently reproduce the convex control.

Before execution: validate all saved design summaries, label exports, pass gates,
and memory arithmetic; recompute seed101's fixed-label-box frozen optimum on CPU.
Compare objective and dense transfer to 1e-9. The nullspace permits nonunique
labels, so compare predictions and antisymmetric label parts rather than the
unidentified symmetric part. This is a reproduction check, not new model choice.
"""
import argparse,csv,hashlib,json,math,os,sys,time
from pathlib import Path
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
import torch
from scipy.optimize import lsq_linear
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];sys.path.insert(0,str(HERE))
import hypergradient as hg

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 (a.out/'hypergradient_review_artifacts_source.py').write_bytes(Path(__file__).read_bytes())
 start=time.process_time();manifest=json.loads((HERE/'HYPERGRADIENT_FROZEN_MANIFEST.json').read_text())
 objs={f['path']:json.loads((ROOT/f['path']).read_text()) for f in manifest['files'] if f['path'].endswith('.json')}
 sums={v['seed']:v for k,v in objs.items() if Path(k).name.startswith('seed') and k.endswith('_summary.json')}
 ds={(v['seed'],v['kind']):v for k,v in objs.items() if Path(k).name.startswith('seed') and not k.endswith('_summary.json')}
 for seed,s in sums.items():
  for d in s['designs']:assert d==ds[seed,d['kind']]
 for d in ds.values():
  assert d['status']=='ok' and len(d['outer_loss_history'])==24 and d['outer_steps']==24 and d['steps']==256
  assert len(d['labels'])==8 and max(map(abs,d['labels']))<=3 and np.isfinite(d['outer_loss_history']).all()
  assert d['source_sha256']==hg.SOURCE and d['baseline_sha256']==hg.BASE
 convex={r['seed']:r for k,v in objs.items() if k.endswith('/convex.json') for r in v['rows']}
 data=ROOT/'data/generated/response_memory_use_cases_20261001'
 exports=list(csv.DictReader((data/'hypergradient_summary/optimized_labels.csv').open()))
 for r in exports:
  d=convex[int(r['seed'])] if r['method']=='frozen_convex' else ds[int(r['seed']),r['method']]
  assert [float(r[f'y{i}']) for i in range(8)]==d['labels']
 summary=objs[str(data.relative_to(ROOT)/'hypergradient_summary/summary.json')]
 table_rows=list(csv.DictReader((data/'hypergradient_summary/results.csv').open()))
 gates=[]
 for seed,s in sums.items():
  orig=s['original_dense_test_mse'];d=ds[seed,'dense'];q=ds[seed,'q1'];f=ds[seed,'frozen']
  def metrics(base,dense,q1,frozen):return dict(error_ratio=q1/base,retained=(base-q1)/(base-dense),frozen_ratio=q1/frozen)
  coarse=metrics(orig,d['dense_test_mse'],q['dense_test_mse'],f['dense_test_mse'])
  fine=metrics(q['refined_original_dense_test_mse'],d['refined_dense_test_mse'],q['refined_dense_test_mse'],f['refined_dense_test_mse'])
  for mm in [coarse,fine]:assert mm['error_ratio']<=.8 and mm['retained']>=.8 and mm['frozen_ratio']<=.9
  assert min(s['feature_movement'])>=.05 and s['dense_frozen_prediction_rms']>=.05
  saved=next(r for r in summary['rows'] if r['seed']==seed)
  assert saved['benefit_retained']==coarse['retained']
  csvrow=next(r for r in table_rows if int(r['seed'])==seed)
  assert float(csvrow['benefit_retained'])==coarse['retained'] and csvrow['pass']=='True'
  gates.append(dict(seed=seed,coarse=coarse,refined=fine))
 memories={}
 for k,v in objs.items():
  if k.endswith('/memory.json'):
   for r in v['rows']:
    assert r['peak_allocated_bytes']-r['setup_allocated_bytes']==r['incremental_peak_bytes']
    n=r['width'];assert r['moving_coordinates']==(n*n+3*n if r['kind']=='dense' else 19*n+1)
    assert r['gradient_max_difference']==0
   memories[k]=[dict(width=r['width'],kind=r['kind'],strategy=r['strategy'],peak_mib=r['peak_allocated_bytes']/2**20,seconds=r['seconds']) for r in v['rows']]
 # Fresh float64 convex control and conditioning on the four identifiable modes.
 x,y=hg.circle(8,.13,'cpu',torch.float64);v,target=hg.circle(32,.37,'cpu',torch.float64);test,truth=hg.circle(256,.71,'cpu',torch.float64)
 flow=hg.FunctionalFlow(x,128,101,'dense');A=flow.frozen_map(v,1/32,8).numpy()
 fit=lsq_linear(A,target.numpy(),bounds=(-3,3),tol=1e-12,lsmr_tol=1e-12,max_iter=1000)
 lab=x.new_tensor(fit.x);old=convex[101];oldlab=x.new_tensor(old['labels'])
 with torch.no_grad():
  mse=float((flow.predict(flow.solve(lab,1/32,8),test)-truth).square().mean())
  fine=float((flow.predict(flow.solve(lab,1/64,8),test)-truth).square().mean())
 svals=np.linalg.svd(A,compute_uv=False)
 control=dict(success=fit.success,optimality=fit.optimality,frozen_outer_mse=float(np.mean((A@fit.x-target.numpy())**2)),dense_transfer_mse=mse,refined_dense_transfer_mse=fine,antisymmetric_label_difference=float(((lab[:4]-lab[4:])-(oldlab[:4]-oldlab[4:])).abs().max()),condition_four_modes=float(svals[0]/svals[3]),singular_values=svals.tolist())
 control['objective_difference']=abs(control['frozen_outer_mse']-old['frozen_outer_mse']);control['dense_transfer_difference']=abs(mse-old['dense_test_mse'])
 assert control['objective_difference']<1e-9 and control['dense_transfer_difference']<1e-9
 # Independent direct readout Euler versus spectral polynomial, at this width.
 h=torch.tanh(flow.W0@torch.tanh(flow.w0@x.T));hq=torch.tanh(flow.W0@torch.tanh(flow.w0@v.T));c=flow.c0.clone()
 for _ in range(256):c=c-2/(8*32)*h@(c@h/128-y)
 spec=float((c@hq/128-flow.frozen_map(v,1/32,8)@y).abs().max())
 conf=[g['coarse']['retained'] for g in gates if 200<=g['seed']<300]
 result=dict(starting_manifest_files=len(manifest['files']),json_objects_read=len(objs),designs=len(ds),label_export_rows=len(exports),gates=gates,confirmation_median_retained=float(np.median(conf)),memory_audits=memories,convex_reproduction=control,frozen_direct_spectral_max_error=spec,cpu_seconds=time.process_time()-start)
 hg.write(a.out/'artifact_audit.json',result);print(json.dumps(hg.plain(result),indent=2))

if __name__=='__main__':main()
