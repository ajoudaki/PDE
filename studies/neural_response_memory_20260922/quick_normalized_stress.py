"""Fixed-budget high-frequency/partial-support depth and LayerNorm comparison."""
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


def data(task, m=64, q=8192):
    rng=np.random.default_rng(20260926)
    if task.startswith('circle'):
        span=np.pi/2 if task.endswith('patch') else 2*np.pi
        angle=(np.arange(m)+.5)*span/m
        test_angle=(np.arange(q)+.5)*2*np.pi/q
        points=lambda a:np.column_stack([np.cos(a),np.sin(a)])
        x,test=points(angle),points(test_angle)
        y,truth=np.sqrt(2)*np.sin(24*angle),np.sqrt(2)*np.sin(24*test_angle)
        region=test_angle<np.pi/2
    else:
        u,v=rng.random((2,m))
        z=.5+.5*u if task.endswith('patch') else 2*u-1
        angle=2*np.pi*v
        make=lambda z,a:np.column_stack([np.sqrt(1-z*z)*np.cos(a),np.sqrt(1-z*z)*np.sin(a),z])
        x=make(z,angle)
        i=np.arange(q); test=make(1-2*(i+.5)/q,i*np.pi*(3-np.sqrt(5)))
        target=lambda a:np.sin(6*np.pi*a[:,0])*np.sin(6*np.pi*a[:,1])
        truth=target(test); scale=np.sqrt(np.mean(truth**2))
        truth,y=truth/scale,target(x)/scale
        region=test[:,2]>=.5
    return x,y,test,truth,region


def plan(task):
    jobs=[(d,'after','gelu',p) for d in [10,15,20] for p in [None,1,2,3]]
    jobs += [(20,'before','gelu',p) for p in [None,1,2,3]]
    if task.endswith('patch'):
        jobs += [(20,'after',a,p) for a in ['relu','selu'] for p in [None,1,2,3]]
        jobs += [(20,'none','gelu',None)]
    return jobs


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--task',choices=['circle_full','circle_patch','sphere_full','sphere_patch'],required=True)
    p.add_argument('--device',required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1);torch.backends.cuda.matmul.allow_tf32=False;torch.cuda.set_device(a.device)
    x,y,test,truth,region=data(a.task)
    np.savez(a.out/'data.npz',inputs=x,labels=y,test_inputs=test,test_labels=truth,region=region)
    here=Path(__file__).resolve().parent
    record=dict(task=a.task,width=2048,samples=len(y),queries=len(truth),step=1/128,
                target_rms=.01,fit_seconds=10.,max_steps=20000,block=8,eps=1e-5,
                network_seed=20260920,data_seed=20260926,dtype='float32',
                command=shlex.join([sys.executable,*sys.argv]),cwd=os.getcwd(),
                git_head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
                torch=torch.__version__,numpy=np.__version__,gpu=torch.cuda.get_device_name(a.device),
                source_sha256={n:hashlib.sha256((here/n).read_bytes()).hexdigest()
                               for n in ['compact_flow.py','quick_normalized_stress.py']},
                data_sha256=hashlib.sha256((a.out/'data.npz').read_bytes()).hexdigest(),
                status='running',rows=[])
    save=lambda:(a.out/'results.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    def rms(v):
        v=float(np.sqrt(np.mean(np.asarray(v,dtype=np.float64)**2)))
        return v if np.isfinite(v) else None
    save();started=time.perf_counter()
    for depth,norm,act,order in plan(a.task):
        begin=time.perf_counter()
        model=Flow(x,y,width=2048,depth=depth,activation=act,order=order,
                   normalization=norm,device=a.device)
        initial=[h.clone() for h in model._forward(model.inputs,model._factors())[0]]
        result=model.fit(step=1/128,target_rms=.01,max_seconds=10,max_steps=20000,block=8)
        if not np.isfinite(result['rms']):result['rms']=None
        pred=model.predict(x).cpu().numpy().astype(np.float64)
        curve=np.concatenate([model.predict(test[i:i+512]).cpu().numpy() for i in range(0,len(test),512)]).astype(np.float64)
        final=model._forward(model.inputs,model._factors())[0]
        motion=[rms((v-u).cpu().numpy()) for u,v in zip(initial,final)]
        if order is None:dense=curve.copy();dense_train=rms(pred-y)
        name='dense' if order is None else f'P{order}'
        row=dict(depth=depth,normalization=norm,activation=act,model=name,**result,
                 train_rms=rms(pred-y),dense_train_rms=dense_train,
                 test_rms_vs_dense=rms(curve-dense),region_rms_vs_dense=rms((curve-dense)[region]),
                 outside_rms_vs_dense=rms((curve-dense)[~region]),
                 test_rms_vs_target=rms(curve-truth),region_rms_vs_target=rms((curve-truth)[region]),
                 outside_rms_vs_target=rms((curve-truth)[~region]),feature_change_rms=motion,
                 total_seconds=time.perf_counter()-begin)
        np.savez(a.out/f'd{depth}_{norm}_{act}_{name}.npz',prediction=pred,test_prediction=curve)
        record['rows'].append(row);save();print(json.dumps(row),flush=True)
        del model,initial,final
    record.update(status='complete',total_seconds=time.perf_counter()-started);save()
    print(json.dumps(dict(task=a.task,total_seconds=record['total_seconds'])),flush=True)


if __name__=='__main__':main()
