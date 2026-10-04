"""Recompute route metrics from retained arrays without rerunning training."""
import argparse
import json
from pathlib import Path
import numpy as np


def load_runs(folder):
    result=[]
    for p in sorted(folder.glob('run_*.json')):
        row=json.loads(p.read_text());row['file']=str(p)
        row['arrays']=dict(np.load(p.with_suffix('.npz'))) if p.with_suffix('.npz').exists() else {}
        result.append(row)
    return result


def rms(a):return float(np.sqrt(np.mean(np.asarray(a,dtype=np.float64)**2)))


def main():
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True)
    p.add_argument('--prefix',default='input_field')
    p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    det=load_runs(a.root/(a.prefix+'_deterministic'));pilot=load_runs(a.root/(a.prefix+'_stream_pilot'))
    confirm=load_runs(a.root/(a.prefix+'_stream_confirmation'));refine=load_runs(a.root/(a.prefix+'_refinement'))
    summary={'deterministic':[],'stream_pilot':[],'stream_confirmation':[],'refinement':[]}
    for row in det:
        c=row['config'];d=next(r for r in det if r['config']['kind']=='dense'
                             and r['config']['seed']==c['seed'] and r['config']['teacher']==c['teacher'])
        summary['deterministic'].append(dict(config=c,target_rmse=row['target_rmse'],
                    prediction_rmse_to_dense=rms(row['arrays']['prediction']-d['arrays']['prediction']),
                    normalized_rmse_to_dense=rms(row['arrays']['prediction']-d['arrays']['prediction'])/row['teacher_rms'],
                    teacher_rms=row['teacher_rms'],feature_movement=row['feature_movement']))
    for stage,rows in [('stream_pilot',pilot),('stream_confirmation',confirm)]:
        for row in rows:
            c=row['config'];d=next(r for r in rows if r['config']['kind']=='dense' and r['config']['seed']==c['seed'])
            summary[stage].append(dict(config=c,target_rmse=row['target_rmse'],status=row['status'],
                   prediction_rmse_to_dense=rms(row['arrays']['prediction']-d['arrays']['prediction']),
                   feature_movement=row['feature_movement'],internal_weight_movement=row['internal_weight_movement'],
                   same_final_batch_as_dense=row['final_batch_fingerprint']==d['final_batch_fingerprint'],
                   moving_scalar_count=row['moving_scalar_count'],seconds=row['seconds'],
                   peak_cuda_allocated_bytes=row['peak_cuda_allocated_bytes']))
    for row in refine:
        c=row['config'];baseline=next(r for r in confirm if r['config']['kind']==c['kind'] and r['config']['seed']==c['seed'])
        error=rms(row['arrays']['prediction']-baseline['arrays']['prediction'])
        target_change=abs(row['target_rmse']-baseline['target_rmse'])
        prefix=c['prefix_nodes']==512
        summary['refinement'].append(dict(config=c,target_rmse=row['target_rmse'],prediction_change=error,
                        normalized_prediction_change=error/row['teacher_rms'],target_rmse_change=target_change,
                        normalized_target_rmse_change=target_change/row['teacher_rms'],
                        numerical_gate_pass=bool(error/row['teacher_rms']<(.01 if prefix else .05)
                                                 and (prefix or target_change/row['teacher_rms']<.03))))
    for stage in ['stream_pilot','stream_confirmation']:
        rows=summary[stage]
        if not rows:continue
        med={k:float(np.median([r['target_rmse'] for r in rows if r['config']['kind']==k]))
             for k in ['field','dense','readout','frozen_internal','low_rank']}
        field=[r for r in rows if r['config']['kind']=='field']
        summary[stage+'_decision']=dict(median_target_rmse=med,field_over_readout=med['field']/med['readout'],
                    field_over_dense=med['field']/med['dense'],field_over_frozen_internal=med['field']/med['frozen_internal'],
                    field_over_low_rank=med['field']/med['low_rank'],
                    loss_gates_pass=bool(med['field']<=.8*med['readout'] and med['field']<=1.25*med['dense']+.02),
                    minimum_final_hidden_feature_movement=min(r['feature_movement'][-1] for r in field),
                    all_runs_completed=all(r['status']=='complete' for r in rows),
                    all_batches_matched=all(r['same_final_batch_as_dense'] for r in rows))
    summary['quadrature']=[]
    for row in det:
        c=row['config']
        if c['nodes']!=256:continue
        base=next(r for r in det if r['config']==dict(c,nodes=128))
        summary['quadrature'].append(dict(teacher=c['teacher'],prediction_change=rms(row['arrays']['prediction']-base['arrays']['prediction'])))
    completions=[json.loads(p.read_text()) for name in [a.prefix+suffix for suffix in ['_deterministic','_stream_pilot','_stream_confirmation','_refinement']]
                 if (p:=a.root/name/'completion.json').exists()]
    summary['completed_fit_count']=sum(x['attempts'] for x in completions)
    summary['sum_stage_fit_loop_seconds']=sum(x['seconds'] for x in completions)
    (a.out/'summary.json').write_text(json.dumps(summary,indent=2))
    if confirm:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig,axes=plt.subplots(1,2,figsize=(10,3.7),constrained_layout=True)
        for teacher,marker in [('A','o'),('B','s')]:
            vals=[]
            for C in [5,9,17]:
                rr=[r['normalized_rmse_to_dense'] for r in summary['deterministic']
                    if r['config']['teacher']==teacher and r['config']['kind']=='field'
                    and r['config']['C']==C and r['config']['q']==3 and r['config']['nodes']==128]
                vals.append(np.median(rr))
            axes[0].plot([5,9,17],vals,marker=marker,label=f'Teacher {teacher}')
        axes[0].set(xlabel='Input functions C (time order q=3)',ylabel='Prediction RMSE / teacher RMS',yscale='log',
                    title='Deterministic pilots, common T=64',xticks=[5,9,17]);axes[0].legend(frameon=False)
        kinds=['readout','frozen_internal','field','dense','low_rank']
        labels=['Readout\nonly','Frozen\ninternal','Input\nfield','Dense','Rank15\nfactors']
        for seed in [201,202,203,204,205]:
            values=[next(r['target_rmse'] for r in confirm if r['config']['seed']==seed and r['config']['kind']==kind) for kind in kinds]
            axes[1].plot(range(5),values,'o-',alpha=.5,linewidth=.8,markersize=4)
        axes[1].set(xticks=range(5),xticklabels=labels,ylabel='Held-out target RMSE',yscale='log',
                    title='Fresh batches, T=128, five new seeds')
        for ax in axes:ax.grid(alpha=.2)
        fig.savefig(a.out/'input_field_summary.png',dpi=180);fig.savefig(a.out/'input_field_summary.pdf');plt.close(fig)
    print(json.dumps({k:v for k,v in summary.items() if k.endswith('decision') or k in ['completed_fit_count','sum_stage_fit_loop_seconds','quadrature','refinement']},indent=2))


if __name__=='__main__':main()
