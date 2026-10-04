"""Small-state feedback experiment, with frozen methods and explicit costs."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys
import time
import numpy as np
import scipy
import dense_compare as dense
from circle_tasks import directions
from cubic_bilinear_repair import BilinearModel
from cubic_bounded_gram_repair import BoundedGramModel,GramQueryCoefficients
from cubic_overlap_gate_repair import OverlapModel
from cubic_minimal_mode_repair import bounded_gram_coefficients
from small_scalar_integrator import integrate

HERE=Path(__file__).resolve().parent
DATA=HERE.parents[1]/'data/generated/structured_full_rank_scalar_20260926'
OLD=DATA/'cubic_scalar_20260930'
GEO=DATA/'cubic_feedback_repair_20260930/geometric_decoder'


def hashfile(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--methods',nargs='+',default=['bilinear','bounded','ungated'])
    parser.add_argument('--tasks',nargs='+',default=['near_pair_sin9','cluster_triple_cos9','cluster_triple_cos1'])
    parser.add_argument('--output',default='round2')
    parser.add_argument('--rtol',type=float,default=1e-8)
    parser.add_argument('--atol',type=float,default=1e-10)
    args=parser.parse_args()
    out=DATA/'cubic_feedback_repair_20260930'/args.output
    out.mkdir(parents=True,exist_ok=False)
    started=time.monotonic()
    initial=dense.initialize(1024,1,'gaussian')
    allresults=[]
    manifest=dict(command=sys.argv,python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
        settings=vars(args),source_sha256={p:hashfile(HERE/p) for p in
          ('run_cubic_feedback_repair.py','cubic_bilinear_repair.py','cubic_bounded_gram_repair.py',
           'cubic_overlap_gate_repair.py','cubic_minimal_mode_repair.py','small_scalar_integrator.py','CUBIC_REPAIR_ROUND2_20260930.md',
           'CUBIC_REPAIR_ROUND3_20260930.md','dense_compare.py')})
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    for name in args.tasks:
        with np.load(OLD/f'{name}.npz') as d:
            y,K0,S=d['model_labels'],d['initial_gram'],d['response_gram']
            kx=d['query_gram']
            angles=np.r_[d['angles'],d['train_angles']]
            ref=d['dense']
            original=d['scalar']
        oldinfo=json.loads((OLD/f'{name}.json').read_text())
        selected=np.asarray(oldinfo['representatives'])
        with np.load(GEO/f'{name}.npz') as d:
            A,B=d['query_A'],d['query_B']
        initial_h=dense._forward(initial,directions(angles)).h2
        diag=np.mean(initial_h*initial_h,axis=0)
        extended=None
        coefficient_seconds=None
        if any(method.startswith('mode') for method in args.methods):
            coefficient_started=time.monotonic()
            extended=bounded_gram_coefficients(initial.w,initial.W,directions(angles[256:])[selected],y,directions(angles))
            coefficient_seconds=time.monotonic()-coefficient_started
            np.savez_compressed(out/f'{name}__extended_coefficients.npz',
                                **{k:v for k,v in extended.items() if k!='mode_metadata'})
            if coefficient_seconds>30:
                raise TimeoutError('Mode coefficient construction exceeds30s budget')
        for method in args.methods:
            if method=='bilinear':
                model=BilinearModel(y,K0,S)
                predict=lambda state:model.predict(state,kx,A,B)
            elif method in ('bounded','ungated'):
                model=BoundedGramModel(y,K0,S,GramQueryCoefficients(kx,diag,B),gated=method=='bounded')
                predict=model.predict
            elif method in ('overlap','overlap_ungated'):
                model=OverlapModel(y,K0,S,kx,diag,B,gated=method=='overlap')
                predict=model.predict
            elif method in ('mode','mode_ungated'):
                model=OverlapModel(y,extended['G'],extended['S'],extended['kx'],extended['querydiag'],extended['query_B'],
                                   gated=method=='mode')
                predict=model.predict
            else:
                raise ValueError(f'Unknown frozen method: {method}')
            state,info,history=integrate(model.rhs,model.initial_state(),model.residual,model.blocks,
                                       rtol=args.rtol,atol=args.atol)
            row=dict(task=name,method=method,**info,training_states=model.training_size,total_states=model.size,
                     old_circle_rms=oldinfo['scalar_dense_rms'],
                     input_sha256={str(p.relative_to(DATA)):hashfile(p) for p in (OLD/f'{name}.npz',GEO/f'{name}.npz')})
            if method.startswith('mode'):
                row.update(mode_metadata=extended['mode_metadata'],coefficient_seconds=coefficient_seconds,
                           coefficient_sha256=hashfile(out/f'{name}__extended_coefficients.npz'))
            try:
                pred=predict(state)
                difference=pred[:256]-ref
                row.update(circle_rms=float(np.sqrt(np.mean(difference**2))),
                    nested_rms_change=float(abs(np.sqrt(np.mean(difference**2))-np.sqrt(np.mean(difference[::2]**2)))),
                    alias_max_abs=float(np.max(np.abs(pred[256+selected]-(y+model.residual(state))))),
                    max_circle_output=float(np.max(np.abs(pred[:256]))))
                if method=='bilinear':
                    v,Theta,T=model.unpack(state)
                    direct=(kx+np.einsum('xibc,bc->xi',B,Theta))@v
                    row['direct_bilinear_circle_rms']=float(np.sqrt(np.mean((direct[:256]-ref)**2)))
                    row['readout_energy']=float(v@K0@v)
                else:
                    row['geometry']=model.diagnostics(state)
                np.savez_compressed(out/f'{name}__{method}.npz',state=state,history=history,
                                    prediction=pred,dense=ref,old=original,angles=angles)
            except (np.linalg.LinAlgError,FloatingPointError) as error:
                row['decoding_error']=str(error)
                np.savez_compressed(out/f'{name}__{method}.npz',state=state,history=history)
            row['data_sha256']=hashfile(out/f'{name}__{method}.npz')
            (out/f'{name}__{method}.json').write_text(json.dumps(row,indent=2,allow_nan=False)+'\n')
            allresults.append(row)
            print(json.dumps({k:row.get(k) for k in ('task','method','fitted','stop_reason','circle_rms','train_mse',
                'training_states','total_states','training_seconds','alias_max_abs','direct_bilinear_circle_rms','geometry')}),flush=True)
    (out/'summary.json').write_text(json.dumps(dict(results=allresults,seconds=time.monotonic()-started),indent=2,allow_nan=False)+'\n')


if __name__=='__main__':
    main()
