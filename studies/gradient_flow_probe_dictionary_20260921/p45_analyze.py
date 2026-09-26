"""Extend the saved-state audit to p4/p5 without changing historical sources."""
import argparse
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
import torch
import comparison_analyze as base

base.COUNTS['new'].update({4:(6,12), 5:(14,24)})
DATA = base.DATA


@torch.no_grad()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--primary', type=Path, default=DATA/'p45_primary01')
    parser.add_argument('--refined', type=Path, default=DATA/'p45_refined01')
    parser.add_argument('--extra', type=Path, action='append', default=[])
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--device', default='cuda:0')
    args = parser.parse_args()
    roots = [base.owned(p) for p in (args.primary,args.refined,*args.extra)]
    out = base.owned(args.out)
    if out.exists() or out in roots:
        raise ValueError('fresh output required')
    if not torch.cuda.is_available():
        raise RuntimeError('CUDA float64 required')
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.cuda.set_device(args.device)
    start = time.monotonic()
    out.mkdir(parents=True)
    rows, validation, gates, predictions = [], {}, [], {}
    for case in base.CASES:
        fulls = [base.audit(path,case,'full',args.device) for path in base.cell_paths(case,'full',roots)]
        full_change = base.discrepancy(fulls[0][1],fulls[1][1])
        full_valid = all(f[0]['valid'] for f in fulls) and full_change is not None and full_change <= .01
        validation[case+'_full'] = dict(valid=full_valid, refinement_max=full_change,
                                        attempts=[x[0] for x in fulls])
        for i, (record,bundle) in enumerate(fulls):
            if bundle is not None:
                predictions[f'{case}_full_{i}'] = bundle['prediction'].cpu().numpy()
                predictions[case+'_angles'] = bundle['angles']
        for p in (3,4,5):
            method, key = f'new_p{p}', f'{case}_new_p{p}'
            paths = ([DATA/f'comparison_{level}01'/key for level in ('primary','refined')]
                     if p == 3 else [roots[0]/key,roots[1]/key]+
                     [root/key for root in roots[2:] if (root/key).exists()])
            attempts = [base.audit(path,case,method,args.device,
                        fulls[min(i,1)][1]['initial'] if fulls[min(i,1)][1] else None)
                        for i,path in enumerate(paths)]
            reasons, branch = [], []
            if len(attempts)>3:
                reasons.append('more than one extra attempt')
            if len(attempts)==3:
                change0 = base.discrepancy(attempts[0][1],attempts[1][1])
                eligible = all(a[0]['valid'] for a in attempts[:2]) and change0 is not None and change0>.01
                branch.append(dict(eligible=eligible, preceding_refinement_max=change0))
                if not eligible:
                    reasons.append('extra lacked the preregistered numerical trigger')
            selected = attempts[-2:]
            change = base.discrepancy(selected[0][1],selected[1][1])
            if change is None or change>.01:
                reasons.append('endpoint refinement maximum exceeds .01 or is unavailable')
            for i,a in enumerate(selected):
                reasons.extend(f'level{i}: '+r for r in a[0]['reasons'])
            for k in ('rtol','atol'):
                a,b = (item[0].get(k) for item in selected)
                if a is None or b is None or not math.isclose(a,4*b,rel_tol=1e-12):
                    reasons.append('tolerances not fourfold tighter: '+k)
            valid = not reasons and full_valid
            validation[key] = dict(valid=valid, reasons=reasons, refinement_max=change,
                attempts=[a[0] for a in attempts], branch_checks=branch,
                selected_paths=[a[0]['path'] for a in selected])
            if p in (4,5):
                eligible = len(attempts)==2 and all(a[0]['valid'] for a in attempts) and change is not None and change>.01
                gates.append(dict(cell=key, eligible=eligible, refinement_max=change,
                                  next_level=2 if eligible else None))
            k1,k2 = base.COUNTS['new'][p]
            row = dict(case=case,p=p,method=method,K1=k1,K2=k2,vectors=k1+k2,
                       middle_parameters=k1*k2,valid=valid,reasons=reasons,
                       refinement_max=change,full_refinement_max=full_change)
            for i,(record,bundle) in enumerate(selected):
                level = ('primary','refined')[i]
                row.update({level+'_'+k:record.get(k) for k in ('path','rtol','atol','time','loss','status')})
                row[level+'_full_path'] = fulls[i][0]['path']
                if bundle is not None and fulls[i][1] is not None:
                    scores = base.metrics(bundle['prediction'],fulls[i][1]['prediction'])
                    grid = base.metrics(bundle['prediction'][::2],fulls[i][1]['prediction'][::2])
                    row.update({level+'_'+k:v for k,v in scores.items()})
                    row.update({level+'_'+k+'_grid4096':v for k,v in grid.items()})
                    predictions[key+f'_{i}'] = bundle['prediction'].cpu().numpy()
                    if not base.aligned(bundle,fulls[i][1]):
                        row['valid'] = False
                        row['reasons'].append('prediction/reference grid mismatch')
            rows.append(row)
        del fulls, attempts, selected
        torch.cuda.empty_cache()
    comparisons = []
    for case in base.CASES:
        baseline = next(row for row in rows if row['case']==case and row['p']==3)
        for p in (4,5):
            current = next(row for row in rows if row['case']==case and row['p']==p)
            wins = [current.get(level+'_rms',math.inf)<baseline.get(level+'_rms',-math.inf)
                    for level in ('primary','refined')]
            comparisons.append(dict(case=case,p=p,against_p=3,
                valid=current['valid'] and baseline['valid'], ordering_agrees=wins[0]==wins[1],
                primary_lower_rms=wins[0],refined_lower_rms=wins[1],
                refined_rms_ratio=current.get('refined_rms',math.inf)/baseline['refined_rms']))
    base.write_json(out/'metrics.json',rows)
    base.write_json(out/'validation.json',validation)
    base.write_json(out/'comparisons.json',comparisons)
    base.write_json(out/'gates.json',dict(cells=gates,eligible_cells=[g['cell'] for g in gates if g['eligible']]))
    np.savez(out/'endpoint_predictions.npz',**predictions)
    torch.cuda.synchronize(args.device)
    seconds = time.monotonic()-start
    base.write_json(out/'provenance.json',dict(seconds=seconds,command=sys.argv,device=args.device,
        gpu=torch.cuda.get_device_name(args.device),torch=str(torch.__version__),numpy=np.__version__,
        sources={str(Path(__file__)):base.digest(__file__),str(Path(base.__file__)):base.digest(base.__file__)},
        input_hashes=base.HASHES,selection='latest two new attempts; frozen p3 and full levels',
        output_hashes={str(path):base.digest(path) for path in out.iterdir() if path.is_file()}))
    print(json.dumps(dict(out=str(out),seconds=seconds,valid_rows=sum(r['valid'] for r in rows),
                         eligible=[g['cell'] for g in gates if g['eligible']])),flush=True)


if __name__=='__main__':
    main()
