#!/usr/bin/env python3
"""Add N3 to the radial endpoint plot, retaining the original dense evaluations."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

sys.dont_write_bytecode=True
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'code'))
from pde import observable_solver as solver


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(4*1024*1024),b''):h.update(block)
    return h.hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run',type=Path,required=True);p.add_argument('--base',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    run=args.run.resolve();base=args.base.resolve();output=args.output.resolve()
    output.mkdir(parents=True,exist_ok=False)
    os.environ['MPLCONFIGDIR']=str(output/'matplotlib_cache')
    prior=json.loads((base/'radial_output.json').read_text())
    assert prior['physical_time']==100 and prior['display_radius_offset']==2
    assert sha(base/'radial_predictions.npz')==prior['products']['radial_predictions.npz']
    with np.load(base/'radial_predictions.npz') as z:arrays={k:z[k] for k in z.files}
    theta=arrays['angles'];directions=arrays['directions'];train_theta=arrays['training_angles'];labels=arrays['labels']
    with np.load(run/'inputs.npz') as z:inputs=z['inputs'];panel=z['panel']
    folder=run/'closure/N3_base';r=json.loads((folder/'record.json').read_text())
    assert r['status']=='success' and r['endpoint_time']==100
    assert r['config']['order']==3 and r['config']['initialization_nodes']==2048 and r['config']['population_nodes']==1024
    input_hashes={str(base/'radial_output.json'):sha(base/'radial_output.json'),
                  str(base/'radial_predictions.npz'):sha(base/'radial_predictions.npz'),
                  str(run/'inputs.npz'):sha(run/'inputs.npz'),str(folder/'record.json'):sha(folder/'record.json')}
    for file in ('observations.npz','checkpoint.json'):
        digest=sha(folder/file);assert digest==r['output_hashes'][file]
        input_hashes[str(folder/file)]=digest
    for file,digest in r['source_hashes'].items():assert sha(ROOT/file)==digest
    state,data=solver.load_restart(folder/'checkpoint.json')
    assert np.array_equal(data.inputs,inputs) and np.array_equal(data.labels,labels)
    with np.load(folder/'observations.npz') as z:
        assert z['times'][-1]==100
        stored=z['predictions'][-1].copy()
    original=solver.predict(state,panel,block_size=16)
    n3=solver.predict(state,directions,block_size=16)
    original_gap=float(np.max(np.abs(original-stored)))
    train_gap=float(np.max(np.abs(n3[arrays['training_indices']]-stored[:16])))
    assert original_gap<=2e-10 and train_gap<=2e-10
    arrays['N3']=n3
    for name in ('actual','N1','N3','N5'):
        assert np.isfinite(arrays[name]).all() and np.min(2+arrays[name])>0
    np.savez(output/'radial_predictions.npz',**arrays)

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans','savefig.dpi':220})
    fig,ax=plt.subplots(figsize=(10.4,11),subplot_kw={'projection':'polar'})
    fig.subplots_adjust(top=.83,bottom=.16,left=.09,right=.91)
    ax.set_theta_zero_location('E');ax.set_theta_direction(1)
    ax.set_ylim(0,3.42);ax.set_xticks(np.arange(12)*np.pi/6)
    ax.set_xticklabels([f'{d}°' for d in range(0,360,30)]);ax.tick_params(axis='x',pad=9)
    ax.set_yticks([1,2,3]);ax.set_yticklabels([r'$f=-1$',r'$f=0$',r'$f=+1$'])
    ax.set_rlabel_position(315);ax.grid(color='#B8BDC5',alpha=.42,linewidth=.7)
    ax.spines['polar'].set_visible(False)
    circle=np.linspace(0,2*np.pi,721)
    ax.plot(circle,np.full(721,2.),color='#8A929E',lw=1.7,ls=(0,(3,3)),zorder=2)
    positive='#C84848';negative='#3269B8'
    for angle,y in zip(train_theta,labels):
        ax.plot([angle,angle],[2,2+y],color=positive if y>0 else negative,alpha=.4,lw=.9,ls=':',zorder=3)
    styles=[('actual','#171C26','-',2.5,'Actual network'),
            ('N1','#E08A25',(0,(5,2)),2.1,r'$N=1$ closure'),
            ('N3','#7862B3',(0,(5,2,1,2)),2.0,r'$N=3$ closure'),
            ('N5','#008A83',(0,(1,1.4)),2.5,r'$N=5$ closure')]
    closed_theta=np.r_[theta,theta[0]+2*np.pi];handles=[]
    for name,color,ls,lw,label in styles:
        line,=ax.plot(closed_theta,2+np.r_[arrays[name],arrays[name][0]],color=color,lw=lw,ls=ls,label=label,zorder=5)
        handles.append(line)
    for y,color in ((1,positive),(-1,negative)):
        select=labels==y
        ax.scatter(train_theta[select],np.full(select.sum(),2.),s=45,c=color,edgecolors='white',linewidths=.75,zorder=8)
        ax.scatter(train_theta[select],np.full(select.sum(),2+y),s=51,marker='D',facecolors='white',edgecolors=color,linewidths=1.35,zorder=9)
    fig.suptitle('Final output around the circle',fontsize=20,fontweight='semibold',y=.98)
    fig.text(.5,.94,r'$t=100\qquad \rho(\theta)=2+f(\theta)$',ha='center',fontsize=14)
    fig.legend(handles=handles,loc='upper center',bbox_to_anchor=(.5,.912),ncol=4,frameon=False,handlelength=2.6,fontsize=11)
    legend_inputs=[Line2D([],[],marker='o',color='none',markerfacecolor=positive,markeredgecolor='white',markersize=7,label='+1 training input'),
                   Line2D([],[],marker='o',color='none',markerfacecolor=negative,markeredgecolor='white',markersize=7,label='−1 training input'),
                   Line2D([],[],marker='D',color='none',markerfacecolor='white',markeredgecolor='#526071',markersize=7,label='Desired output at that input')]
    fig.legend(handles=legend_inputs,loc='lower center',bbox_to_anchor=(.5,.086),ncol=3,frameon=False,fontsize=11)
    fig.text(.5,.066,'Dots locate inputs on the reference circle; diamonds mark their target radii.',ha='center',fontsize=11,color='#39404B')
    fig.text(.5,.044,'Positive outputs extend outward; negative outputs move inward.',ha='center',fontsize=11,color='#39404B')
    fig.text(.5,.021,'Network: width 8192, mean of three seeds. Closures use the same quadrature resolution.',ha='center',fontsize=10,color='#596271')
    products={}
    for ext in ('png','pdf','svg'):
        path=output/f'final_radial_output.{ext}';fig.savefig(path,bbox_inches='tight',facecolor='white');products[path.name]=sha(path)
    plt.close(fig);products['radial_predictions.npz']=sha(output/'radial_predictions.npz')
    result={'status':'complete','source_sha256':sha(__file__),'source_hashes':r['source_hashes'],
            'input_hashes':input_hashes,'products':products,'physical_time':100,'display_radius_offset':2,
            'dense_angle_count':len(theta),'new_N3_original_panel_max_error':original_gap,'new_N3_training_max_error':train_gap,
            'prior_curves_unchanged':True,'reference':'width8192 mean seeds11,29,47',
            'closures':['N1_base','N3_base','N5_base'],'quadrature':'Q2048/P1024, all three orders',
            'coordinate_map':'(rho*cos(theta), rho*sin(theta)), rho=2+f(theta)',
            'minimum_radius':{k:float(np.min(2+arrays[k])) for k in ('actual','N1','N3','N5')},
            'dense_circle_maximum_prediction_error':{k:float(np.max(np.abs(arrays[k]-arrays['actual']))) for k in ('N1','N3','N5')},
            'command':getattr(sys,'orig_argv',sys.argv),'numpy_version':np.__version__,'matplotlib_version':matplotlib.__version__,
            'scope':'User requested adding N3; prior endpoint evaluations reused, N3 forward evaluated only, no training.'}
    with (output/'radial_output.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:result[k] for k in ('status','dense_angle_count','new_N3_original_panel_max_error','new_N3_training_max_error','minimum_radius','dense_circle_maximum_prediction_error')},indent=2))


if __name__=='__main__':main()
