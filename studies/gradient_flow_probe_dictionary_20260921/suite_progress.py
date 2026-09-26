"""Provisional saved-endpoint comparisons for requested live progress updates.

This is not the final replay/provenance audit or a numerical validity verdict.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import torch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA = ROOT/'data/generated/gradient_flow_probe_dictionary_20260921'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.cuda.set_device(args.device)
    start = time.monotonic()
    manifest = json.loads((HERE/'SUITE_MANIFEST.json').read_text())
    rows = []
    def prediction(path):
        with np.load(path, allow_pickle=False) as a:
            return torch.tensor(a['endpoint_prediction'],device=args.device,dtype=torch.float64)
    for case in manifest['cases']:
        refs = {level: prediction(manifest['archive_cells'][case+'_full'][level]['arrays_path'])
                for level in ('primary','refined')}
        for p in (1,3,5):
            row = dict(case=case,p=p)
            own = {}
            for level in ('primary','refined'):
                cell = DATA/f'suite_{level}01'/f'{case}_new_p{p}'
                if not (cell/'summary.json').exists():
                    continue
                summary = json.loads((cell/'summary.json').read_text())
                if summary['status'] != 'fitted':
                    row[level+'_status'] = summary['status']
                    continue
                own[level] = prediction(cell/'arrays.npz')
                row[level+'_new_rms'] = float((own[level]-refs[level]).square().mean().sqrt())
                for family in ('ours','gaussian','orthogonal'):
                    old = manifest['archive_cells'][f'{case}_{family}_p{p}']
                    score = float((prediction(old[level]['arrays_path'])-refs[level]).square().mean().sqrt())
                    row[level+'_'+family+'_rms'] = score
                    row[family+'_archive_valid'] = old['valid']
            if len(own)==2:
                row['new_refinement_max'] = float((own['primary']-own['refined']).abs().max())
            if own:
                rows.append(row)
    torch.cuda.synchronize(args.device)
    result = dict(provisional=True,independent_audit_complete=False,rows=rows,
        seconds=time.monotonic()-start,device=args.device,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (args.out/'progress.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    for p in (1,3,5):
        ready=[r for r in rows if r['p']==p and 'refined_new_rms' in r]
        counts={f:sum(r['refined_new_rms']<r['refined_'+f+'_rms'] for r in ready) for f in ('ours','gaussian','orthogonal')}
        print(json.dumps(dict(p=p,refined_ready=len(ready),new_lower_rms_count=counts,
            own_refinement_fail=[r['case'] for r in ready if r['new_refinement_max']>.01],
            details=[{k:v for k,v in r.items() if k in ('case','refined_new_rms','refined_ours_rms','refined_gaussian_rms','refined_orthogonal_rms')} for r in ready])),flush=True)
    print(json.dumps(dict(seconds=result['seconds'])),flush=True)


if __name__=='__main__':
    main()
