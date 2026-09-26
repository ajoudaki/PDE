"""Recompute matched circle metrics and produce the one-case figure."""
import os
for key in ('OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS'):
    os.environ.setdefault(key, '1')
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT/'data/generated/adaptive_response_compression_20260922'
DERIVATIVE = ROOT/'data/generated/gradient_flow_probe_dictionary_20260921'
DENSE = ROOT/'data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_refined01/two_outliers_alternating_full/arrays.npz'
P3 = DERIVATIVE/'suite_refined01/two_outliers_alternating_new_p3/arrays.npz'
P7 = DERIVATIVE/'p7_refined01/two_outliers_alternating_new_p7/arrays.npz'


def sha(path):
    with Path(path).open('rb') as handle:
        return hashlib.file_digest(handle,'sha256').hexdigest() if hasattr(hashlib,'file_digest') else hashlib.sha256(handle.read()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    args.out.mkdir(parents=True,exist_ok=False)
    paths={'dense':DENSE,'frozen_p3':P3,'frozen_p7':P7,
           **{name:BASE/name/'arrays.npz' for name in
              ('trainable_p3_primary01','trainable_p3_refined01','frozen_p3_replay01')}}
    data={name:np.load(path,allow_pickle=False) for name,path in paths.items()}
    target=data['dense']['endpoint_prediction']
    rows=[]
    for name,a in data.items():
        assert np.array_equal(a['endpoint_inputs'],data['dense']['endpoint_inputs'])
        difference=a['endpoint_prediction']-target
        rows.append(dict(method=name,rms=float(np.sqrt(np.mean(difference**2))),
            maximum=float(np.max(np.abs(difference))),
            grid_rms_change=abs(float(np.sqrt(np.mean(difference**2))-np.sqrt(np.mean(difference[::2]**2)))),
            fit_time=float(a['times'][-1]),training_mse=float(a['losses'][-1]),
            first_detected_crossing=bool(np.all(a['losses'][:-1]>.001) and a['losses'][-1]<=.001),
            arrays_path=str(paths[name]),arrays_sha256=sha(paths[name])))
    coarse=data['trainable_p3_primary01']['endpoint_prediction']
    fine=data['trainable_p3_refined01']['endpoint_prediction']
    frozen=data['frozen_p3_replay01']
    refinement=float(np.max(np.abs(coarse-fine)))
    replay=float(np.max(np.abs(frozen['endpoint_prediction']-data['frozen_p3']['endpoint_prediction'])))
    replay_time=abs(float(frozen['times'][-1]-data['frozen_p3']['times'][-1]))
    lookup={row['method']:row for row in rows}
    selected=lookup['trainable_p3_refined01']['rms']
    gates=dict(base_refinement_max=refinement,base_refinement_pass=refinement<=.01,
        frozen_replay_max=replay,frozen_replay_time_error=replay_time,
        frozen_replay_pass=replay<=.001 and replay_time<=.001,
        nested_grid_pass=all(row['grid_rms_change']<=.001 for row in rows),
        all_fit=all(row['first_detected_crossing'] for row in rows))
    comparisons={}
    for baseline in ('frozen_p3','frozen_p7'):
        value=lookup[baseline]['rms']
        margins=[lookup[level]['rms']-value for level in ('trainable_p3_primary01','trainable_p3_refined01')]
        comparisons[baseline]=dict(absolute_change=selected-value,relative_change=selected/value-1,
            direction_both_levels=('improves' if max(margins)<=-.01 else 'worsens' if min(margins)>=.01 else 'inconclusive'))
    seconds=sum(json.loads((paths[name].parent/'summary.json').read_text())['worker_seconds'] for name in
                ('trainable_p3_primary01','trainable_p3_refined01','frozen_p3_replay01'))
    result=dict(rows=rows,gates=gates,comparisons=comparisons,worker_seconds=seconds,
        selected='trainable_p3_refined01',extra_eligible=refinement>.01,
        source_sha256=sha(__file__),metric='8192-angle RMS to common finer dense fitted function; own MSE .001 endpoints')
    (args.out/'metrics.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(1,2,figsize=(11.5,4.2),constrained_layout=True)
    styles=[('dense','Dense reference','#555555'),('frozen_p3','Frozen p3 · 18 vectors','#db9245'),
            ('frozen_p7','Frozen p7 · 72 vectors','#4374b8'),
            ('trainable_p3_refined01','Trainable p3 · 18 vectors','#bf3f70')]
    for name,label,color in styles:
        a=data[name]
        axes[0].plot(a['times'],a['losses'],label=label,color=color,lw=1.8)
        axes[1].plot(a['endpoint_angles']*180/np.pi,a['endpoint_prediction'],label=label,color=color,lw=1.7)
    angles=np.arctan2(data['dense']['training_inputs'][:,1],data['dense']['training_inputs'][:,0])%(2*np.pi)
    axes[1].scatter(angles*180/np.pi,data['dense']['labels'],color='black',s=22,zorder=5,label='Training labels')
    axes[0].set(xlabel='Gradient-flow time',ylabel='Training MSE',yscale='log',xscale='symlog')
    axes[0].set_xlim(0,1.04*max(float(data[name]['times'][-1]) for name,_,_ in styles))
    axes[0].axhline(.001,color='#888888',ls=':',lw=1)
    axes[1].set(xlabel='Angle (degrees)',ylabel='Predicted function',xlim=(0,360))
    axes[1].legend(frameon=False,fontsize=8)
    for ax in axes: ax.grid(alpha=.15)
    fig.suptitle('Alternating labels + two outliers · n=2048 · unfreezing derivative p3')
    fig.savefig(args.out/'comparison.png',dpi=170)
    fig.savefig(args.out/'comparison.svg')
    plt.close(fig)
    print(json.dumps(dict(gates=gates,comparisons=comparisons,worker_seconds=seconds),indent=2))


if __name__=='__main__':
    main()
