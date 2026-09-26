"""Provisional saved-endpoint RMS updates; no validity or selection decisions."""
import argparse
import json
import time
from pathlib import Path
import numpy as np
import torch


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--device',required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    torch.set_num_threads(1)
    torch.cuda.set_device(args.device)
    start=time.monotonic()
    data=Path(__file__).resolve().parents[2]/'data/generated/gradient_flow_probe_dictionary_20260921'
    old=json.loads((data/'suite_analysis_final01/metrics.json').read_text())
    lookup={(r['case'],r['method']):r for r in old}
    rows=[]
    with np.load(data/'suite_analysis_final01/endpoint_predictions.npz',allow_pickle=False) as refs:
        for level in ('primary','refined'):
            root=data/f'p7_{level}01'
            for ledger in sorted(root.glob('results_worker*.json')):
                results=json.loads(ledger.read_text())
                for key,record in results.items():
                    if not record.get('declared_executed'):
                        continue
                    case=key.removesuffix('_new_p7')
                    with np.load(root/key/'arrays.npz',allow_pickle=False) as arrays:
                        predicted=torch.tensor(arrays['endpoint_prediction'],device=args.device)
                    reference=torch.tensor(refs[case+'_full_'+level+'_prediction'],device=args.device)
                    rms=float((predicted-reference).square().mean().sqrt())
                    rows.append(dict(case=case,level=level,new72=rms,status=record['status'],
                        baselines={m:lookup[case,m][level+'_rms'] for m in ('new_p5','old_p3','gaussian_p3','orthogonal_p3')}))
    torch.cuda.synchronize()
    args.out.mkdir(parents=True,exist_ok=False)
    result=dict(provisional=True,selection_decisions=False,device=args.device,rows=rows,seconds=time.monotonic()-start)
    (args.out/'progress.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':
    main()
