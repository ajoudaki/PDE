"""Fit-first comparison on unchanged stress tasks with one fixed architecture."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import time
os.environ.setdefault('OMP_NUM_THREADS','1')
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np
import torch
from compact_flow import Flow
from quick_normalized_stress import data


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--task',required=True,choices=['circle_full','circle_patch','sphere_full','sphere_patch'])
    p.add_argument('--activation',default='gelu',choices=['gelu','relu','selu'])
    p.add_argument('--normalization',default='after',choices=['before','after','none'])
    p.add_argument('--models',nargs='+',default=['dense','P1','P2','P3'],choices=['dense','P1','P2','P3'])
    p.add_argument('--device',required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--step',type=float,default=1/128)
    p.add_argument('--fit-seconds',type=float,default=30.)
    p.add_argument('--decay',action='store_true',help='Use three fixed learning rates, reducing at RMS 0.8 and 0.2.')
    p.add_argument('--readout-std',type=float,default=None,
                   help='Initial standard deviation of c in c@h/n; default is 1/n.')
    a=p.parse_args()
    if a.readout_std is not None and (not np.isfinite(a.readout_std) or a.readout_std<=0):
        p.error('--readout-std must be positive and finite')
    torch.set_num_threads(1);torch.backends.cuda.matmul.allow_tf32=False;torch.cuda.set_device(a.device)
    x,y,test,truth,region=data(a.task)
    here=Path(__file__).resolve().parent
    hashes={n:hashlib.sha256((here/n).read_bytes()).hexdigest()
            for n in ['compact_flow.py','quick_normalized_stress.py','fit_stress_tasks.py']}
    def rms(v):
        z=float(np.sqrt(np.mean(np.asarray(v,dtype=np.float64)**2)))
        return z if np.isfinite(z) else None
    for name in a.models:
        folder=a.out/a.task/name;folder.mkdir(parents=True,exist_ok=False)
        started=time.perf_counter()
        model=Flow(x,y,width=2048,depth=10,activation=a.activation,order=None if name=='dense' else int(name[1:]),
                   normalization=a.normalization,seed=20260920,device=a.device)
        if a.readout_std is not None:model.c.mul_(a.readout_std*model.n)
        if a.decay:
            phases=[]
            for factor,target in [(1.,.8),(.25,.2),(.0625,.04)]:
                phases.append(model.fit(step=a.step*factor,target_rms=target,
                                        max_seconds=a.fit_seconds/3,max_steps=20000,block=8))
            fit={**phases[-1],'phases':phases,
                 **{k:sum(r[k] for r in phases) for k in ['steps','seconds','physical_time','capture_seconds','loop_seconds']}}
        else:
            fit=model.fit(step=a.step,target_rms=.04,max_seconds=a.fit_seconds,max_steps=60000,block=8)
        if not np.isfinite(fit['rms']):fit['rms']=None
        pred=model.predict(x).cpu().numpy().astype(np.float64)
        curve=np.concatenate([model.predict(test[i:i+512]).cpu().numpy()
                              for i in range(0,len(test),512)]).astype(np.float64)
        np.savez(folder/'arrays.npz',inputs=x,labels=y,prediction=pred,test_inputs=test,
                 test_labels=truth,test_prediction=curve,region=region)
        record=dict(task=a.task,model=name,width=2048,depth=10,activation=a.activation,normalization=a.normalization,
                    readout_std=1/model.n if a.readout_std is None else a.readout_std,
                    step_schedule='rms_decay_0.8_0.2' if a.decay else 'constant',
                    step=a.step,target_rms=.04,fit_seconds=a.fit_seconds,seed=20260920,**{
                        'fit':fit,'train_rms':rms(pred-y),'test_rms_vs_target':rms(curve-truth),
                        'region_rms_vs_target':rms((curve-truth)[region]),
                        'outside_rms_vs_target':rms((curve-truth)[~region])},
                    total_seconds=time.perf_counter()-started,source_sha256=hashes,
                    arrays_sha256=hashlib.sha256((folder/'arrays.npz').read_bytes()).hexdigest(),
                    command=shlex.join([sys.executable,*sys.argv]),cwd=os.getcwd(),
                    git_head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
                    torch=torch.__version__,numpy=np.__version__,gpu=torch.cuda.get_device_name(a.device))
        (folder/'result.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
        print(json.dumps({k:record[k] for k in ['task','model','train_rms','test_rms_vs_target','total_seconds','fit']}),flush=True)
        del model


if __name__=='__main__':main()
