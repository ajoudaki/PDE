"""Bounded GPU pilots, RHS-capture equivalence, and opposite-GPU repeats."""
import argparse
import json
from pathlib import Path
import time

import numpy as np
import torch

from closure_transfer_euler import (CachedEulerEngine,EulerStage,euler_update,
                                    task_data,run,sha256,write_json)


@torch.no_grad()
def main():
    p=argparse.ArgumentParser();p.add_argument('--out',required=True)
    p.add_argument('--cases-json',required=True);a=p.parse_args()
    out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1);torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False
    charged=0.;equivalence=[];repeats=[]
    fixtures=[('gelu','two_outliers_alternating',1,.015625),
              ('selu','quadrant_alternating',3,.00048828125)]
    for i,(activation,task,order,h) in enumerate(fixtures):
        device=f'cuda:{i}'
        torch.cuda.set_device(device)
        inputs,labels,_=task_data(a.cases_json,activation,task)
        engine=CachedEulerEngine(2,2048,order,inputs,labels,activation=activation,device=device)
        states=[engine.initial_state(),engine.initial_state()]
        stages=[EulerStage(engine,s,b) for s,b in zip(states,['eager','graphs'])]
        costs=[]
        start=time.monotonic()
        for stage,state in zip(stages,states):
            begin=time.monotonic()
            for _ in range(100):
                velocity,loss,valid=stage.evaluate();assert valid
                euler_update(state,velocity,h)
            torch.cuda.synchronize(device)
            costs.append(time.monotonic()-begin)
        charged+=time.monotonic()-start
        errs={name:float(torch.max(torch.abs(getattr(states[0],name)-getattr(states[1],name))))
              for name in states[0].names()}
        assert max(errs.values())<1e-10,errs
        equivalence.append(dict(activation=activation,task=task,P=order,updates_per_backend=100,
                                block_max_differences=errs,eager_seconds=costs[0],graphs_seconds=costs[1]))
        del states,stages,engine
        paths=[]
        for gpu,tag in [(i,'pilot'),(1-i,'opposite_gpu')]:
            path=out/f'{activation}__{task}__P{order}__{tag}'
            args=argparse.Namespace(activation=activation,task=task,P=order,step=h,
                device=f'cuda:{gpu}',out=str(path),max_seconds=30.,max_time=260.,
                max_steps=400,target_mse=1e-8,backend='graphs',cases_json=a.cases_json)
            summary=run(args);charged+=summary['integration_seconds'];paths.append(path)
            assert summary['steps']==400 and summary['state_finite'] and summary['predictions_finite']
            assert summary['initialization_sha256']=='0cccd42603ccc7e57cdae90019acd3e19faeb891433c54b0462ce2983e345ac6'
        with np.load(paths[0]/'state.npz') as x,np.load(paths[1]/'state.npz') as y:
            errors={name:float(np.max(np.abs(x[name]-y[name]))) for name in ('w','c','A2','B2','A3','B3','s')}
        with np.load(paths[0]/'predictions.npz') as x,np.load(paths[1]/'predictions.npz') as y:
            rms=float(np.sqrt(np.mean((x['circle_predictions']-y['circle_predictions'])**2)))
        assert max(errors.values())<1e-10 and rms<1e-12
        repeats.append(dict(activation=activation,task=task,P=order,block_max_differences=errors,
                            circle_rms_difference=rms,paths=[str(p) for p in paths]))
        write_json(out/'partial.json',dict(integration_seconds=charged,equivalence=equivalence,repeats=repeats))
    write_json(out/'receipt.json',dict(passed=True,integration_seconds=charged,equivalence=equivalence,
        repeats=repeats,source_sha256=sha256(__file__),runner_sha256=sha256(Path(__file__).with_name('closure_transfer_euler.py'))))
    print(json.dumps(dict(passed=True,integration_seconds=charged,equivalence=equivalence)),flush=True)


if __name__=='__main__':main()
