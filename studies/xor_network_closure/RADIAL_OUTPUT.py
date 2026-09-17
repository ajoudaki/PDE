#!/usr/bin/env python3
"""Forward-only endpoint evaluation and radial output figure; no training."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time

sys.dont_write_bytecode=True
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
STUDY=Path(__file__).resolve().parent


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(4*1024*1024),b''):h.update(block)
    return h.hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--device',default='cuda:0')
    args=parser.parse_args();run=args.run.resolve();output=args.output.resolve()
    output.mkdir(parents=True,exist_ok=False)
    os.environ['MPLCONFIGDIR']=str(output/'matplotlib_cache')
    started=time.time();inputs_hash=sha(run/'inputs.npz')
    with np.load(run/'inputs.npz',allow_pickle=False) as z:
        inputs=z['inputs'];panel=z['panel'];labels=z['labels']
    theta_train=np.mod(np.arctan2(inputs[:,1],inputs[:,0]),2*np.pi)
    theta=np.unique(np.concatenate((np.arange(1440)*2*np.pi/1440,theta_train)))
    directions=np.column_stack((np.cos(theta),np.sin(theta)))
    train_indices=np.searchsorted(theta,theta_train)
    assert np.array_equal(theta[train_indices],theta_train)
    directions[train_indices]=inputs
    source_hashes={str(Path(__file__).relative_to(ROOT)):sha(__file__)}
    input_hashes={'inputs.npz':inputs_hash}
    evaluations={};archived={};dense={}

    def retained(family,name):
        folder=run/family/name
        record=json.loads((folder/'record.json').read_text())
        assert record['status'] in ('complete','success')
        assert record['config']['name']==name
        for file,digest in record['source_hashes'].items():
            assert sha(ROOT/file)==digest,file
            source_hashes[str((ROOT/file).relative_to(ROOT))]=digest
        for file in ('record.json','observations.npz','checkpoint.pt' if family=='network' else 'checkpoint.json'):
            actual=sha(folder/file);input_hashes[str((folder/file).relative_to(run))]=actual
            if file!='record.json':
                expected=record['output_hashes'][file]
                assert actual==(expected['sha256'] if isinstance(expected,dict) else expected)
        with np.load(folder/'observations.npz',allow_pickle=False) as z:
            assert z['times'][-1]==100 and z['predictions'].shape==(201,144)
            stored=z['predictions'][-1].copy()
        return folder,record,stored

    import NETWORK as network
    import torch
    device=network.configure(args.device)
    for seed in (11,29,47):
        name=f'n8192_s{seed}';folder,record,stored=retained('network',name)
        checkpoint=torch.load(folder/'checkpoint.pt',map_location='cpu',weights_only=True)
        assert checkpoint['time']==100 and checkpoint['config']==record['config']
        state=tuple(checkpoint[k].to(device) for k in ('W1','W2','c'))
        dtype=state[0].dtype
        with torch.inference_mode():
            original=network.fields(state,torch.tensor(panel.T.copy(),dtype=dtype,device=device))[-1].double().cpu().numpy()
            values=[]
            for start in range(0,len(directions),256):
                u=torch.tensor(directions[start:start+256].T.copy(),dtype=dtype,device=device)
                values.append(network.fields(state,u)[-1].double().cpu().numpy())
            values=np.concatenate(values)
        original_gap=float(np.max(np.abs(original-stored)))
        training_gap=float(np.max(np.abs(values[train_indices]-stored[:16])))
        assert original_gap<=3e-6 and training_gap<=3e-6
        assert np.isfinite(values).all()
        evaluations[name]={'original_panel_max_error':original_gap,'dense_training_max_error':training_gap}
        archived[name]=stored;dense[name]=values
        del state,checkpoint
    software=network.environment(device)
    if device.type=='cuda':torch.cuda.synchronize(device)

    sys.path.insert(0,str(ROOT/'code'))
    from pde import observable_solver as solver
    for name in ('N1_base','N5_base'):
        folder,record,stored=retained('closure',name)
        state,data=solver.load_restart(folder/'checkpoint.json')
        assert np.array_equal(data.inputs,inputs) and np.array_equal(data.labels,labels)
        original=solver.predict(state,panel,block_size=16)
        values=solver.predict(state,directions,block_size=16)
        original_gap=float(np.max(np.abs(original-stored)))
        training_gap=float(np.max(np.abs(values[train_indices]-stored[:16])))
        assert original_gap<=2e-10 and training_gap<=2e-10
        assert np.isfinite(values).all()
        evaluations[name]={'original_panel_max_error':original_gap,'dense_training_max_error':training_gap}
        archived[name]=stored;dense[name]=values
    actual=np.mean([dense[f'n8192_s{s}'] for s in (11,29,47)],axis=0)
    saved_mean=np.mean([archived[f'n8192_s{s}'] for s in (11,29,47)],axis=0)
    assert hashlib.sha256(np.ascontiguousarray(saved_mean).tobytes()).hexdigest()=='ae737b8e2b277d7f8c5a99eb3cf5a407875726ecb1a71f9fc99ea97234c117ca'
    radius=2.
    curves={'actual':actual,'N1':dense['N1_base'],'N5':dense['N5_base']}
    assert all(np.min(radius+f)>0 for f in curves.values())
    arrays={'angles':theta,'directions':directions,'training_angles':theta_train,
            'training_indices':train_indices,'labels':labels,**curves}
    arrays.update({f'seed_{s}':dense[f'n8192_s{s}'] for s in (11,29,47)})
    np.savez(output/'radial_predictions.npz',**arrays)

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans','savefig.dpi':220})
    fig,ax=plt.subplots(figsize=(10.2,10.8),subplot_kw={'projection':'polar'})
    fig.subplots_adjust(top=.83,bottom=.15,left=.09,right=.91)
    ax.set_theta_zero_location('E');ax.set_theta_direction(1)
    ax.set_ylim(0,3.42);ax.set_xticks(np.arange(12)*np.pi/6)
    ax.set_xticklabels([f'{d}°' for d in range(0,360,30)])
    ax.tick_params(axis='x',pad=9)
    ax.set_yticks([1,2,3]);ax.set_yticklabels([r'$f=-1$',r'$f=0$',r'$f=+1$'])
    ax.set_rlabel_position(315)
    ax.grid(color='#B8BDC5',alpha=.42,linewidth=.7)
    ax.spines['polar'].set_visible(False)
    closed_theta=np.r_[theta,theta[0]+2*np.pi]
    reference_angles=np.linspace(0,2*np.pi,721)
    ax.plot(reference_angles,np.full(721,radius),color='#8A929E',lw=1.7,ls=(0,(3,3)),zorder=2)
    positive='#C84848';negative='#3269B8'
    for angle,y in zip(theta_train,labels):
        color=positive if y>0 else negative
        ax.plot([angle,angle],[radius,radius+y],color=color,alpha=.40,lw=.9,ls=':',zorder=3)
    styles=[('actual','#171C26','-',2.5,'Actual network'),
            ('N1','#E08A25',(0,(5,2)),2.1,r'$N=1$ closure'),
            ('N5','#008A83',(0,(3,1.5,1,1.5)),2.2,r'$N=5$ closure')]
    handles=[]
    for name,color,ls,lw,label in styles:
        values=radius+np.r_[curves[name],curves[name][0]]
        line,=ax.plot(closed_theta,values,color=color,lw=lw,ls=ls,label=label,zorder=5)
        handles.append(line)
    for y,color in ((1,positive),(-1,negative)):
        select=labels==y
        ax.scatter(theta_train[select],np.full(select.sum(),radius),s=45,c=color,
                   edgecolors='white',linewidths=.75,zorder=8)
        ax.scatter(theta_train[select],np.full(select.sum(),radius+y),s=51,marker='D',
                   facecolors='white',edgecolors=color,linewidths=1.35,zorder=9)
    fig.suptitle('Final output around the circle',fontsize=20,fontweight='semibold',y=.98)
    fig.text(.5,.938,r'$t=100\qquad \rho(\theta)=2+f(\theta)$',ha='center',fontsize=14)
    fig.legend(handles=handles,loc='upper center',bbox_to_anchor=(.5,.91),ncol=3,frameon=False,handlelength=3.2)
    legend_inputs=[Line2D([],[],marker='o',color='none',markerfacecolor=positive,markeredgecolor='white',markersize=7,label='+1 training input'),
                   Line2D([],[],marker='o',color='none',markerfacecolor=negative,markeredgecolor='white',markersize=7,label='−1 training input'),
                   Line2D([],[],marker='D',color='none',markerfacecolor='white',markeredgecolor='#526071',markersize=7,label='Desired output at that input')]
    fig.legend(handles=legend_inputs,loc='lower center',bbox_to_anchor=(.5,.075),ncol=3,frameon=False,fontsize=11)
    fig.text(.5,.05,'Dots locate inputs on the reference circle; diamonds mark their target radii.',ha='center',fontsize=11,color='#39404B')
    fig.text(.5,.027,'Positive outputs extend outward; negative outputs move inward.',ha='center',fontsize=11,color='#39404B')
    products={}
    for suffix in ('png','pdf','svg'):
        file=output/f'final_radial_output.{suffix}'
        fig.savefig(file,bbox_inches='tight',facecolor='white');products[file.name]=sha(file)
    plt.close(fig)
    products['radial_predictions.npz']=sha(output/'radial_predictions.npz')
    result={'status':'complete','scope':'Forward-only endpoint evaluation and plotting; no retraining or time rescaling.',
            'command':getattr(sys,'orig_argv',sys.argv),'cwd':os.getcwd(),'source_hashes':source_hashes,
            'input_hashes':input_hashes,'evaluations':evaluations,'products':products,
            'physical_time':100,'display_radius_offset':radius,'dense_angle_count':len(theta),
            'reference':'width8192 mean of seeds11,29,47','closures':'N1_base and N5_base, both Q2048/P1024, h=.01',
            'coordinate_map':'(rho cos(theta), rho sin(theta)), rho=2+f(theta)',
            'curve_ranges':{k:[float(v.min()),float(v.max())] for k,v in curves.items()},
            'minimum_radius':{k:float(np.min(radius+v)) for k,v in curves.items()},
            'saved_circle_maximum_prediction_error':{k:float(np.max(np.abs(archived[k+'_base'][16:]-saved_mean[16:]))) for k in ('N1','N5')},
            'dense_circle_maximum_prediction_error':{k:float(np.max(np.abs(curves[k]-actual))) for k in ('N1','N5')},
            'matplotlib':matplotlib.__version__,'software':software,'wall_seconds':time.time()-started}
    with (output/'radial_output.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:result[k] for k in ('status','physical_time','dense_angle_count','evaluations','minimum_radius','dense_circle_maximum_prediction_error','wall_seconds')},indent=2))


if __name__=='__main__':main()
