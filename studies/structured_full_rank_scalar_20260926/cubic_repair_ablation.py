"""Causal completion ablation with one diagnostic readout-energy scalar."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from cubic_scalar_ode import ScalarModel,QueryCoefficients,integrate

HERE=Path(__file__).resolve().parent
DATA=HERE.parents[1]/'data/generated/structured_full_rank_scalar_20260926'
SOURCE=DATA/'cubic_scalar_20260930'
OUT=DATA/'cubic_feedback_repair_20260930/ablation'
TASKS=('near_pair_sin9','cluster_triple_cos9','cluster_triple_cos1')


class EnergyAblation(ScalarModel):
    def __init__(self,*args,completion=True):
        super().__init__(*args)
        self.completion=completion
        self.energy_index=self.size
        self.slices=(*self.slices,slice(self.size,self.size+1))
        self.size+=1
        self.minimum_kernel_eigenvalue=np.inf

    def kernel(self,z,J):
        K,M,N=super().kernel(z,J)
        if not self.completion:
            K=self.initial_gram+M+M.T+N
        self.minimum_kernel_eigenvalue=min(self.minimum_kernel_eigenvalue,float(np.linalg.eigvalsh(K)[0]))
        return K,M,N

    def rhs(self,t,state):
        result=super().rhs(t,state)
        r=state[:self.m]
        result[self.energy_index]=-2*self.alpha*np.dot(r,self.labels+r)
        return result


def main():
    OUT.mkdir(parents=True,exist_ok=False)
    started=time.monotonic()
    results=[]
    for name in TASKS:
        with np.load(SOURCE/f'{name}.npz') as d:
            model_args=(d['model_labels'],d['initial_gram'],d['response_gram'])
            coeff=QueryCoefficients(d['query_gram'],d['query_cubic'])
            ref=d['dense'].copy()
        for completion in (True,False):
            model=EnergyAblation(*model_args,completion=completion)
            state,info=integrate(model)
            history=info.pop('history')
            pred=model.predict(state,coeff)
            cub=model.cubic_prediction(state,coeff)
            energy=float(state[model.energy_index])
            row=dict(task=name,method='completed' if completion else 'cubic',**info,
                circle_rms=float(np.sqrt(np.mean((pred[:256]-ref)**2))),
                diagnostic_readout_energy=energy,
                max_circle_squared_bound_excess=float(np.max(pred[:256]**2)-energy),
                alias_correction_rms=float(np.sqrt(np.mean((pred[:256]-cub[:256])**2))),
                minimum_kernel_eigenvalue=model.minimum_kernel_eigenvalue,
                training_states=model.training_size+1,total_states=model.size)
            tag=f"{name}__{row['method']}"
            np.savez_compressed(OUT/f'{tag}.npz',state=state,history=history,prediction=pred,cubic=cub,dense=ref)
            (OUT/f'{tag}.json').write_text(json.dumps(row,indent=2,allow_nan=False)+'\n')
            results.append(row)
            print(json.dumps({k:row[k] for k in ('task','method','fitted','circle_rms','diagnostic_readout_energy','max_circle_squared_bound_excess','alias_correction_rms','minimum_kernel_eigenvalue')}),flush=True)
    manifest=dict(results=results,total_seconds=time.monotonic()-started,
        source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
            (Path(__file__),HERE/'cubic_scalar_ode.py',HERE/'CUBIC_REPAIR_PROTOCOL_20260930.md')})
    (OUT/'summary.json').write_text(json.dumps(manifest,indent=2,allow_nan=False)+'\n')


if __name__=='__main__':
    main()
