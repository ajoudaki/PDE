"""Small float64 layout experiment for the measured skinny-product bottleneck."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
import numpy as np
import torch
from activation_moment_engine import ActivationMomentEngine


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--config',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    args.out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1);torch.cuda.set_device(0);torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32=False
    cfg=json.loads(args.config.read_text())
    engine=ActivationMomentEngine(2,cfg['width'],cfg['order'],cfg['inputs'],cfg['labels'],
        activation=cfg['activation'],seed=cfg['seed'],device='cuda:0',dtype=torch.float64)
    x=engine.initial.B2[0].clone();results=[]
    with torch.no_grad():
        for transposed in (False,True):
            w=engine.W20.T if transposed else engine.W20
            wc=w.contiguous();wf=w.T.contiguous().T
            columns=[x[:,j].contiguous() for j in range(x.shape[1])]
            pads={m:torch.zeros((len(x),m),dtype=x.dtype,device=x.device) for m in (16,32,64)}
            for pad in pads.values():pad[:,:x.shape[1]].copy_(x)
            splits={s:(w.reshape(w.shape[0],s,-1).permute(1,0,2),
                       x.reshape(s,-1,x.shape[1])) for s in (4,8,16)}
            baseline=w@x
            variants={
                'original':lambda:w@x,
                'reverse_product':lambda:(x.T@w.T).T,
                'contiguous_matrix':lambda:wc@x,
                'column_major_matrix':lambda:wf@x,
                'column_major_input':lambda:w@x.T.contiguous().T,
                'eight_matvecs':lambda:torch.stack([torch.mv(w,c) for c in columns],dim=1),
                'batched_matvecs':lambda:torch.bmm(w.expand(x.shape[1],-1,-1),
                    x.T.unsqueeze(-1)).squeeze(-1).T,
                **{f'split_k_{s}':(lambda a=a,b=b:torch.bmm(a,b).sum(dim=0))
                   for s,(a,b) in splits.items()},
                **{f'pad_{m}':(lambda pad=pad:(w@pad)[:,:x.shape[1]]) for m,pad in pads.items()},
            }
            for name,call in variants.items():
                value=call();error=float((value-baseline).abs().max().cpu())
                for _ in range(5):call()
                timings=[]
                for _ in range(3):
                    torch.cuda.synchronize();start=time.perf_counter()
                    for _ in range(30):call()
                    torch.cuda.synchronize();timings.append((time.perf_counter()-start)/30)
                results.append(dict(transposed=transposed,variant=name,seconds=float(np.median(timings)),
                    max_abs_error=error,bitwise_equal=bool(torch.equal(value,baseline)),replicates=timings))
    out=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        config=str(args.config.resolve()),dtype='float64',device='cuda:0',results=results,
        caveat='Fixed-input microbenchmark; precomputed alternative layouts/padding exclude their per-step input-copy cost. Full-step testing is required.')
    (args.out/'benchmark.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(results,indent=2))


if __name__=='__main__':main()
