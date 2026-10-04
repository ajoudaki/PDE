"""Stronger feature-learning surrogate and irregular-support stress."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np
import torch
from hypergradient import FunctionalFlow,circle,write,utc

HERE=Path(__file__).resolve().parent


class FrozenMiddle(FunctionalFlow):
    def rhs(self,state,y):
        first,hidden,last=super().rhs(state,y)
        return first,torch.zeros_like(hidden),last


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True)
    p.add_argument('--panel',choices=['regular','irregular'],required=True)
    p.add_argument('--device',required=True);p.add_argument('--seeds',type=int,nargs='+',required=True)
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
    names=['hypergradient_controls.py','hypergradient.py','baseline_compact_flow.py',
           'HYPERGRADIENT_CONTROL_PROTOCOL.md']
    manifest={'command':sys.argv,'python':sys.executable,'torch':torch.__version__,
              'numpy':np.__version__,'device':a.device,'gpu':torch.cuda.get_device_name(a.device),
              'started_utc':utc(),'source_hashes':{s:hashlib.sha256((HERE/s).read_bytes()).hexdigest() for s in names},
              'horizon':8,'step':1/32,'width':512,'outer_steps':24,'label_bounds':[-3,3]}
    for name in names:(a.out/name).write_bytes((HERE/name).read_bytes())
    write(a.out/'manifest.json',manifest)
    x,y=circle(8,.13,a.device,torch.float32)
    if a.panel=='irregular':
        jitter=np.random.default_rng(12345).uniform(-1,1,8)
        angle=torch.as_tensor(2*np.pi*(np.arange(8)+.13+.32*jitter)/8,device=a.device,dtype=x.dtype)
        x=torch.stack((angle.cos(),angle.sin()),1)
        y=torch.sin(3*angle)+.4*torch.cos(angle)
    outer,target=circle(32,.37,a.device,x.dtype);query,truth=circle(256,.71,a.device,x.dtype)
    rows=[];begin=time.perf_counter();solves=0
    for seed in a.seeds:
        dense=FunctionalFlow(x,512,seed,'dense')
        with torch.no_grad():
            original=dense.predict(dense.solve(y,1/32,8),query);solves+=1
            original_mse=float((original-truth).square().mean())
        for kind in (['frozen_middle'] if a.panel=='regular' else ['dense','q1','frozen_middle']):
            model=FrozenMiddle(x,512,seed,'dense') if kind=='frozen_middle' else FunctionalFlow(x,512,seed,kind)
            labels=y.clone().requires_grad_();opt=torch.optim.Adam([labels],lr=.05)
            history=[];start=time.perf_counter()
            for _ in range(24):
                opt.zero_grad(set_to_none=True)
                loss=(model.predict(model.solve(labels,1/32,8),outer)-target).square().mean();solves+=1
                if not torch.isfinite(loss):raise RuntimeError('Nonfinite outer loss')
                loss.backward();history.append(float(loss));opt.step()
                with torch.no_grad():labels.clamp_(-3,3)
            with torch.no_grad():
                dense_pred=dense.predict(dense.solve(labels,1/32,8),query);solves+=1
                own=model.predict(model.solve(labels,1/32,8),query);solves+=1
                mse=float((dense_pred-truth).square().mean())
            torch.cuda.synchronize(a.device)
            row={'seed':seed,'kind':kind,'panel':a.panel,'seconds':time.perf_counter()-start,
                 'original_dense_mse':original_mse,'dense_test_mse':mse,
                 'surrogate_test_mse':float((own-truth).square().mean()),
                 'labels':labels.detach(),'inputs':x,'original_labels':y,'loss_history':history}
            write(a.out/f'seed{seed}_{kind}.json',row);rows.append(row)
            print(json.dumps({k:v for k,v in row.items() if k not in ['labels','inputs','original_labels','loss_history']}),flush=True)
    write(a.out/'results.json',rows)
    write(a.out/'completion.json',{'exit_status':0,'inner_solves':solves,'seconds':time.perf_counter()-begin,'ended_utc':utc()})


if __name__=='__main__':main()
