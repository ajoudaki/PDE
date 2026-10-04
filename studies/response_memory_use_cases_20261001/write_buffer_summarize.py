"""Aggregate only the preregistered route outputs and create a static figure."""
import argparse,json
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--root',default='data/generated/response_memory_use_cases_20261001');a=p.parse_args();root=Path(a.root);analysis_dir=root/'write_buffer_analysis';analysis_dir.mkdir(exist_ok=True);report={}

def load(stage):
    values={}
    folder=root/stage
    if not folder.exists():return values
    for run in sorted(folder.iterdir()):
        if not (run/'summary.json').exists():continue
        s=json.loads((run/'summary.json').read_text());z=np.load(run/'predictions.npz')
        values[run.name]=(s,{k:z[k].copy() for k in z.files})
    return values

for stage in ['write_buffer_repeated_pilot','write_buffer_repeated_confirm','write_buffer_repeated_refine','write_buffer_repeated_width']:
    values=load(stage);rows=[]
    for name,(s,z) in values.items():
        ds,d=values['dense_s'+str(s['seed'])];error=np.sqrt(np.mean((z['predictions']-d['predictions'])**2,axis=1));t=z['times'];primary=(t>0)&(t%16==0);ends=(t>0)&(t%32==0);mids=t%32==16
        train=np.array([v['train_rms'] for v in s['snapshots']]);acc=np.array([v['accuracy'] for v in s['snapshots']])
        row=dict(name=name,method=s['method'],seed=s['seed'],mean_error=float(error[primary].mean()),midpoint_error=float(error[mids].mean()),endpoint_error=float(error[ends].mean()),max_observed_error=float(error.max()),final_error=float(error[-1]),mean_block_end_train_rms=float(train[ends].mean()),max_block_end_train_rms=float(train[ends].max()),final_train_rms=float(train[-1]),final_accuracy=float(acc[-1]),seconds=s['seconds'],materialization_seconds=s['materialization_seconds'],materialization_flops=s['materialization_flops'],diagnostic_seconds=s['diagnostic_seconds'],dense_write_events=s['dense_write_events'],optimizer_dense_writes=s['optimizer_dense_writes'],moving_state_scalars=s['moving_state_scalars'],fixed_dense_scalars=s['fixed_dense_scalars'],delayed_history_allocated_scalars=s['delayed_history_allocated_scalars'],delayed_max_used_scalars=s['delayed_max_used_scalars'],peak_allocated_cuda_bytes=s['peak_allocated_cuda_bytes'])
        rows.append(row)
    report[stage]=rows
coarse=load('write_buffer_repeated_confirm');fine=load('write_buffer_repeated_refine');refinement=[]
for name,(s,z) in fine.items():
    sc,zc=coarse[name]
    assert np.array_equal(z['times'],zc['times'])
    rms=np.sqrt(np.mean((z['predictions']-zc['predictions'])**2,axis=1))
    refinement.append(dict(name=name,mean_coarse_fine_grid_rms=float(rms.mean()),maximum_coarse_fine_grid_rms=float(rms.max()),final_coarse_fine_grid_rms=float(rms[-1])))
report['refinement']=refinement
all_summaries=[]
for stage in ['write_buffer_pilot','write_buffer_repeated_pilot','write_buffer_repeated_confirm','write_buffer_repeated_refine','write_buffer_repeated_width']:
    all_summaries.extend([s for s,z in load(stage).values()])
report['budget']=dict(complete_scientific_fits=len(all_summaries),train_wall_seconds=sum(s['seconds'] for s in all_summaries),statuses={status:sum(s['status']==status for s in all_summaries) for status in set(s['status'] for s in all_summaries)},cpu_smoke_fits=2)
(analysis_dir/'aggregate.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
if coarse:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axes=plt.subplots(1,2,figsize=(10,3.6),constrained_layout=True)
    names=['fixed3_32','delay_selected','factor_selected'];labels=['Response memory q=3','Delayed updates (0.25 gain)','Trained rank-24 factors'];colors=['#166b9d','#c64f3d','#7d559c']
    for name,label,color in zip(names,labels,colors):
        errors=[];rms=[]
        for seed in range(201,206):
            s,z=coarse[f'{name}_s{seed}'];_,d=coarse[f'dense_s{seed}'];times=z['times'];errors.append(np.sqrt(np.mean((z['predictions']-d['predictions'])**2,axis=1)));rms.append([v['train_rms'] for v in s['snapshots']])
        errors=np.array(errors);rms=np.array(rms);keep=times>0
        axes[0].semilogy(times[keep],errors.mean(0)[keep],label=label,color=color)
        axes[0].fill_between(times[keep],errors.min(0)[keep],errors.max(0)[keep],alpha=.14,color=color)
        end=(times>0)&(times%32==0)
        axes[1].semilogy(times[end],rms.mean(0)[end],label=label,color=color,marker='o',ms=3)
    for ax in axes:
        for t in range(32,256,32):ax.axvline(t,color='#888888',lw=.4,alpha=.4)
        ax.set_xlabel('Physical training time');ax.grid(alpha=.15)
    axes[0].set_ylabel('RMS prediction difference from dense');axes[1].set_ylabel('Training RMS at block end');axes[0].legend(fontsize=8)
    fig.suptitle('Repeated adaptation: eight supports, eight matrix consolidations; five fresh seeds',fontsize=10)
    fig.savefig(analysis_dir/'repeated_confirmation.png',dpi=180);fig.savefig(analysis_dir/'repeated_confirmation.pdf')
