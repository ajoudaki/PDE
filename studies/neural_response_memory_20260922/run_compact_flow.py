"""One task-independent runner for compact_flow.Flow; no normalization.

Data NPZ keys: inputs (M,d), labels (M,), test_inputs (Q,d), optionally
test_labels (Q,). The same supplied configuration is used for every file.
"""
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


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data',type=Path,nargs='+',required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--device',default='cuda:0')
    p.add_argument('--width',type=int,default=2048)
    p.add_argument('--depth',type=int,default=3)
    p.add_argument('--activation',default='relu')
    p.add_argument('--orders',type=int,nargs='+',default=[0,1,2,3],help='0=dense, positive=P-order closure')
    p.add_argument('--step',type=float,default=.0625)
    p.add_argument('--target-rms',type=float,default=.04)
    p.add_argument('--seconds',type=float,default=60.)
    p.add_argument('--max-steps',type=int,default=60000)
    p.add_argument('--seed',type=int,default=20260920)
    p.add_argument('--hidden-gain',default='1',help='A positive number or unit_moment; initialization only')
    p.add_argument('--readout-std',type=float,default=None)
    a=p.parse_args()
    if len(set(a.orders))!=len(a.orders) or any(v<0 for v in a.orders):p.error('Use distinct nonnegative orders')
    if len({v.stem for v in a.data})!=len(a.data):p.error('Data filenames must have distinct stems')
    gain=a.hidden_gain if a.hidden_gain=='unit_moment' else float(a.hidden_gain)
    torch.set_num_threads(1);torch.backends.cuda.matmul.allow_tf32=False
    if torch.device(a.device).type=='cuda':torch.cuda.set_device(a.device)
    a.out.mkdir(parents=True,exist_ok=False)
    here=Path(__file__).resolve().parent
    sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
    config=dict(width=a.width,depth=a.depth,activation=a.activation,normalization='none',
                seed=a.seed,dtype='float32',step=a.step,target_rms=a.target_rms,
                max_seconds=a.seconds,max_steps=a.max_steps,block=8,hidden_gain=gain,
                readout_std=1/a.width if a.readout_std is None else a.readout_std)
    meta=dict(config=config,orders=a.orders,command=shlex.join([sys.executable,*sys.argv]),
              cwd=os.getcwd(),git_head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
              source_sha256={n:sha(here/n) for n in ['compact_flow.py','run_compact_flow.py']},
              torch=torch.__version__,numpy=np.__version__,device=a.device,
              gpu=torch.cuda.get_device_name(a.device) if torch.device(a.device).type=='cuda' else None)
    (a.out/'config.json').write_text(json.dumps(meta,indent=2)+'\n')
    def rms(value):
        value=float(np.sqrt(np.mean(np.asarray(value,dtype=np.float64)**2)))
        return value if np.isfinite(value) else None
    for source in a.data:
        with np.load(source) as d: data={k:d[k].copy() for k in d.files}
        x,y,query=(data[k] for k in ['inputs','labels','test_inputs'])
        folder=a.out/source.stem;folder.mkdir()
        np.savez(folder/'data.npz',**data)
        dense=None
        for order in sorted(a.orders):
            started=time.perf_counter();name='dense' if order==0 else f'P{order}'
            model=Flow(x,y,width=a.width,depth=a.depth,activation=a.activation,order=order or None,
                       seed=a.seed,device=a.device,normalization='none',hidden_gain=gain,readout_std=a.readout_std)
            fit=model.fit(step=a.step,target_rms=a.target_rms,max_seconds=a.seconds,max_steps=a.max_steps,block=8)
            if not np.isfinite(fit['rms']):fit['rms']=None
            prediction=model.predict(x).cpu().numpy().astype(np.float64)
            curve=np.concatenate([model.predict(query[i:i+512]).cpu().numpy() for i in range(0,len(query),512)]).astype(np.float64)
            if order==0:dense=curve.copy()
            path=folder/(name+'.npz');np.savez(path,prediction=prediction,test_prediction=curve)
            record=dict(model=name,config=config,fit=fit,train_rms=rms(prediction-y),
                        test_rms_vs_dense=rms(curve-dense) if dense is not None else None,
                        test_rms_vs_target=rms(curve-data['test_labels']) if 'test_labels' in data else None,
                        hidden_gains=model.hidden_gains,total_seconds=time.perf_counter()-started,
                        data_source=str(source.resolve()),data_source_sha256=sha(source),
                        data_sha256=sha(folder/'data.npz'),predictions_sha256=sha(path))
            (folder/(name+'.json')).write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
            print(json.dumps(dict(data=source.stem,**{k:record[k] for k in ['model','train_rms','test_rms_vs_dense','total_seconds']},status=fit['status'])),flush=True)
            del model


if __name__=='__main__':main()
