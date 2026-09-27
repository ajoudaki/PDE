"""Bounded representative-block experiment; separate q, P and Gaussian errors."""
import block_scalar_closure as scalar
import argparse
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time

import numpy as np
import scipy
from circle_tasks import BY_NAME

TASKS=('near_pair_sin9','cluster_triple_cos9','alternating5')
COUNTS=(8,32,64)
SUBSETS=(1001,1002,1003)


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def write(path,obj):Path(path).write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')
def rms(a,b):return float(np.sqrt(np.mean((a-b)**2)))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    baseline,out=args.baseline.resolve(),args.output.resolve()
    source=Path(__file__).resolve().parent
    old=json.loads((baseline/'manifest.json').read_text())
    if (old['width'],old['seed'],old['target_mse'])!=(2048,1,.01):
        raise ValueError('Expected the width2048 seed1 loss0.01 dense baseline')
    for name in ('dense_compare.py','dense_wide_integrator.py','circle_tasks.py'):
        if digest(source/name)!=old['sources'][name]:raise ValueError(f'Changed source {name}')
    dense_rows={(r['task'],r['method']):r for r in json.loads((baseline/'results.json').read_text())}
    dense_predictions={};baseline_hashes={}
    angles=2*np.pi*np.arange(2048)/2048
    for task in TASKS:
        for method in ('gaussian','block16'):
            r=dense_rows[task,method];path=baseline/r['data_file']
            if not r['fitted'] or digest(path)!=r['data_sha256']:raise ValueError('Invalid baseline')
            with np.load(path) as data:
                if not np.array_equal(data['angles'],angles):raise ValueError('Circle grid changed')
                dense_predictions[task,method]=data['prediction']
            baseline_hashes[path.name]=r['data_sha256']
    out.mkdir(parents=True,exist_ok=False)
    snapshot=out/'source_snapshot';snapshot.mkdir()
    names=('block_scalar_closure.py','run_block_scalar_closure.py','check_block_scalar_closure.py',
           'dense_compare.py','dense_wide_integrator.py','circle_tasks.py')
    for name in names:shutil.copyfile(source/name,snapshot/name)
    manifest={'width_reference':2048,'reference_blocks':128,'k':16,'seed':1,
        'tasks':TASKS,'counts':COUNTS,'subset_streams':SUBSETS,'target_mse':.01,
        'history_orders':[8,16],'history_selection_rms':.003,
        'fine_check_task':'cluster_triple_cos9','fine_rtol':1e-6,'fine_atol':1e-9,
        'numerical_refinement_rms_limit':2e-4,
        'initialization':'Subsets of the exact seed1 width2048 block16 initial state, including c_i~N(0,1/2048^2)',
        'subset_rule':'Nested prefixes of RNG SeedSequence([1,stream]).permutation(128)',
        'rtol':1e-5,'atol':1e-8,'first_step':.01,'max_step':10.,'grid':2048,
        'deadline_seconds':50,'interrupt_seconds':55,'per_run_ceiling_seconds':60,
        'workers':1,'blas_threads':1,'baseline':str(baseline),'baseline_data_hashes':baseline_hashes,
        'sources':{name:digest(source/name) for name in names},'command':sys.argv,'cwd':str(Path.cwd()),
        'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,
        'machine':platform.platform(),'head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()}
    write(out/'manifest.json',manifest)
    pool=scalar.initial_pool(2048,16,1)
    started=time.monotonic(); rows=[]; predictions={}
    def run(task,order,indices,kind,stream=None,rtol=1e-5,atol=1e-8):
        run_started=time.monotonic()
        u,y=BY_NAME[task].data()
        layout,G,initial=scalar.initialize(pool,indices,u,order)
        state,status=scalar.integrate(layout,G,initial,u,y,rtol=rtol,atol=atol)
        prediction=scalar.predict(layout,G,state,angles)
        final=scalar.forward(layout,G,state,u)
        initial_fields=scalar.forward(layout,G,initial,u)
        recomputed=float(np.mean((final[0]-y)**2))
        if abs(recomputed-status['train_mse'])>1e-12:raise ValueError('Stop MSE mismatch')
        tag=f'{task}__P{order}__q{len(indices)}__{kind}'+(f'__s{stream}' if stream is not None else '')
        path=out/(tag+'.npz')
        history=status.pop('history')
        np.savez(path,vector=state,initial_vector=initial,G=G,indices=indices,
                 angles=angles,prediction=prediction,train_prediction=final[0],train_labels=y,
                 train_angles=np.asarray(BY_NAME[task].angles),history=history)
        row={'tag':tag,'task':task,'order':order,'q':len(indices),'k':16,'subset_stream':stream,
             'kind':kind,**status,'dynamic_scalars':layout.size,'static_G_scalars':G.size,
             'total_seconds':time.monotonic()-run_started,
             'rms_vs_dense_block16':rms(prediction,dense_predictions[task,'block16']),
             'rms_vs_dense_gaussian':rms(prediction,dense_predictions[task,'gaussian']),
             'h1_motion_rms':rms(final[2],initial_fields[2]),'h2_motion_rms':rms(final[4],initial_fields[4]),
             'data_file':path.name,'data_sha256':digest(path)}
        if not np.all(np.isfinite(prediction)):raise ValueError('Nonfinite prediction')
        write(path.with_suffix('.json'),row)
        rows.append(row);predictions[tag]=prediction
        write(out/'results.json',rows)
        print(json.dumps(row),flush=True)
        return row
    references={}
    for task in TASKS:references[task]=run(task,8,np.arange(128),'reference')
    order=8
    if any(not r['fitted'] or r['rms_vs_dense_block16']>.003 for r in references.values()):
        order=16
        for task in TASKS:references[task]=run(task,16,np.arange(128),'reference')
    selection={'selected_order':order,'references':{t:r['tag'] for t,r in references.items()},
               'all_reference_history_errors_below_003':all(r['fitted'] and r['rms_vs_dense_block16']<=.003
                                                         for r in references.values())}
    write(out/'selection.json',selection)
    print(json.dumps(selection),flush=True)
    # Fixed numerical check, separate from the representative/accuracy campaign.
    fine=run('cluster_triple_cos9',order,np.arange(128),'fine',rtol=1e-6,atol=1e-9)
    coarse=references['cluster_triple_cos9']
    refinement={'task':'cluster_triple_cos9','order':order,
        'both_fitted':fine['fitted'] and coarse['fitted'],
        'rms_difference':rms(predictions[fine['tag']],predictions[coarse['tag']]),
        'limit':2e-4}
    refinement['passed']=refinement['both_fitted'] and refinement['rms_difference']<=refinement['limit']
    write(out/'refinement.json',refinement)
    for task in TASKS:
        for stream in SUBSETS:
            permutation=np.random.default_rng(np.random.SeedSequence([1,stream])).permutation(128)
            for q in COUNTS:run(task,order,permutation[:q],'representative',stream)
    comparisons=[]
    for row in rows:
        ref=references[row['task']]
        error=predictions[row['tag']]-predictions[ref['tag']]
        comparisons.append({'tag':row['tag'],'task':row['task'],'kind':row['kind'],
            'order':row['order'],'q':row['q'],'subset_stream':row['subset_stream'],
            'fitted_pair':row['fitted'] and ref['fitted'],
            'rms_vs_full_closure':rms(predictions[row['tag']],predictions[ref['tag']]),
            'rms_vs_dense_block16':row['rms_vs_dense_block16'],
            'rms_vs_dense_gaussian':row['rms_vs_dense_gaussian'],
            'quadrature_change':abs(float(np.sqrt(np.mean(error**2)))-float(np.sqrt(np.mean(error[::2]**2)))),
            'data_file':row['data_file'],'data_sha256':row['data_sha256']})
    write(out/'comparisons.json',comparisons)
    summaries=[]
    for task in TASKS:
        for q in COUNTS:
            group=[r for r in comparisons if r['task']==task and r['q']==q and r['kind']=='representative']
            valid=[r for r in group if r['fitted_pair']]
            summary={'task':task,'q':q,'count':len(group),'fitted_pairs':len(valid)}
            for metric in ('rms_vs_full_closure','rms_vs_dense_block16','rms_vs_dense_gaussian'):
                values=[r[metric] for r in valid]
                summary[metric]={'mean':float(np.mean(values)),'min':min(values),'max':max(values)} if values else None
            summaries.append(summary)
    write(out/'summary.json',summaries)
    completion={'wall_seconds':time.monotonic()-started,'runs':len(rows),
        'representative_runs':sum(r['kind']=='representative' for r in rows),
        'all_fitted':all(r['fitted'] for r in rows),'selected_order':order,
        'max_run_seconds':max(r['total_seconds'] for r in rows),
        'max_loss_rise':max(r['max_loss_rise'] for r in rows),
        'max_quadrature_change':max(r['quadrature_change'] for r in comparisons),
        'refinement_passed':refinement['passed']}
    write(out/'completion.json',completion)
    lines=['# Moving-block scalar closure: first circle comparison','',
        f'Block16, history order{order}, full reference128 blocks (width2048), training MSE0.01.',
        'Three nested subset draws per representative count. Primary metric is absolute circle RMS versus the full memory closure.',
        '', '| Task | q | RMS vs full closure: mean [min,max] | RMS vs dense Gaussian: mean | Fitted pairs |',
        '|---|---:|---:|---:|---:|']
    for r in summaries:
        a=r['rms_vs_full_closure'];b=r['rms_vs_dense_gaussian']
        if a:lines.append(f"| {r['task']} | {r['q']} | {a['mean']:.6f} [{a['min']:.6f}, {a['max']:.6f}] | {b['mean']:.6f} | {r['fitted_pairs']}/3 |")
        else:lines.append(f"| {r['task']} | {r['q']} | no fitted pair | unavailable | 0/3 |")
    lines+=['','| Task | Full closure vs dense block16 (history error) | Dense block16 vs dense Gaussian (initialization change) |',
            '|---|---:|---:|']
    for task,r in references.items():
        lines.append(f"| {task} | {r['rms_vs_dense_block16']:.6f} | {rms(dense_predictions[task,'block16'],dense_predictions[task,'gaussian']):.6f} |")
    lines+=['',f'Whole-run completion: `{json.dumps(completion)}`',
        f'Clustered-task solver refinement: `{json.dumps(refinement)}`',
        'The finite reference is the actual width2048 population closure, not an asserted infinite-width solution. '
        'All endpoints use their own first MSE0.01 crossing, not a common physical time. '
        'No scalar order-rate or global-in-time theorem is inferred from three subset draws.',
        'Raw Gaussian blocks are reused exactly, no spectral clipping or resampling. '
        'All learned features/history factors evolve; only representative count is reduced.']
    (out/'report.md').write_text('\n'.join(lines)+'\n')
    print((out/'report.md').read_text(),flush=True)


if __name__=='__main__':main()
