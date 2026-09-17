"""Plots of loss and hidden Gram evolution for the thirty-degree experiment."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import sys
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MPLCONFIGDIR']='/tmp/pde-arc30-matplotlib'
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from ARC30_20260914_PREPARE import sha, GENERATED

COLORS={1:'#d58c00',3:'#009e73',5:'#cc5078'}


def main(output):
    output=output.resolve()
    if output.parent!=GENERATED.resolve() or not output.name.startswith('ARC30_'):
        raise ValueError('Plot output must be this study\'s ARC30 run')
    result=json.loads((output/'arc30_comparison.json').read_text())
    if result['status']!='complete' or not result['validation_pass']:
        raise ValueError('Complete validated run required')
    destination=output/'figures';destination.mkdir(exist_ok=True)
    with np.load(output/'inputs.npz') as archive:
        inputs={k:archive[k].copy() for k in archive.files}
    times=inputs['times'];products=[];raw_hashes={}
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,
                         'savefig.facecolor':'white'})

    def save(fig,name):
        for extension in ('png','pdf'):
            path=destination/f'{name}.{extension}'
            fig.savefig(path,dpi=180,bbox_inches='tight')
            products.append(dict(path=str(path.relative_to(output)),sha256=sha(path)))
        plt.close(fig)

    def time_axis(ax):
        ax.set_xscale('symlog',linthresh=.5,linscale=.7)
        ax.set_xticks([0,.5,1,5,10,40],['0','.5','1','5','10','40'])
        ax.set_xlim(0,40)
        ax.set_xlabel('Training time t (early times expanded)');ax.grid(alpha=.2)

    def selected(layer,panel,observable,closure):
        return next(r for r in result['seed_mean_comparisons'] if r['width']==8192 and r['layer']==layer and
                    r['panel']==panel and r['observable']==observable and r['closure']==closure)

    losses={}
    for n in (2048,8192):
        losses[n]=np.stack([np.load(output/'network'/f'arcs30_n{n}_s{s}'/'observations.npz')['loss']
                            for s in (11,29,47)])
    fig,axes=plt.subplots(1,3,figsize=(14,4.2),constrained_layout=True)
    ax=axes[0]
    ax.fill_between(times,losses[8192].min(0),losses[8192].max(0),color='#214b80',alpha=.18)
    ax.plot(times,losses[8192].mean(0),color='#214b80',lw=2.2,label='Network 8192: 3-seed mean')
    ax.plot(times,losses[2048].mean(0),color='#848b95',lw=1.2,ls=':',label='Network 2048: 3-seed mean')
    for n in (1,3,5):
        with np.load(output/'closure'/f'arcs30_N{n}'/'observations.npz') as data:
            ax.plot(times,data['loss'],color=COLORS[n],lw=1.8,label=f'Closure N = {n}')
    with np.load(output/'closure'/'arcs30_N5_fine'/'observations.npz') as data:
        ax.plot(times,data['loss'],color='#825ac3',ls='--',lw=1.8,label='N = 5, finest quadrature')
    ax.set_yscale('log');ax.set_ylabel('Training mean squared loss');ax.set_title('Loss evolution')
    time_axis(ax)
    for layer in (1,2):
        ax=axes[layer]
        for n in (1,3,5):
            row=selected(layer,'data','G',f'arcs30_N{n}')
            ax.plot(times,row['rms_curve'],color=COLORS[n],lw=1.8)
        row=selected(layer,'data','G','arcs30_N5_fine')
        ax.plot(times,row['rms_curve'],color='#825ac3',ls='--',lw=1.8)
        ax.set_ylim(bottom=0);ax.set_title(f'Layer {layer}: full Gram error')
        ax.set_ylabel('Gram RMS error\n(16 training inputs)');time_axis(ax)
    handles,labels=axes[0].get_legend_handles_labels()
    fig.legend(handles,labels,loc='outside lower center',ncol=3,frameon=False)
    fig.suptitle('Training arcs widened to ±30° · loss and hidden geometry\nGram errors against the width-8192, three-seed network mean',fontsize=15)
    save(fig,'loss_and_gram_errors')

    fig,axes=plt.subplots(2,4,figsize=(15,7),constrained_layout=True)
    for i,observable in enumerate(('G','DeltaG')):
        for j,(layer,panel) in enumerate(((1,'data'),(2,'data'),(1,'circle'),(2,'circle'))):
            ax=axes[i,j]
            for n in (1,3,5):
                row=selected(layer,panel,observable,f'arcs30_N{n}')
                ax.plot(times,row['rms_curve'],color=COLORS[n],lw=1.8,label=f'N = {n}')
            row=selected(layer,panel,observable,'arcs30_N5_fine')
            ax.plot(times,row['rms_curve'],color='#825ac3',ls='--',lw=1.8,label='N = 5, finest quadrature')
            if i==0:ax.set_title(f"Layer {layer} · {'training' if panel=='data' else 'circle'} inputs")
            if j==0:ax.set_ylabel(('Full Gram G(t)' if i==0 else 'Change G(t) − G(0)')+'\nMatrix RMS discrepancy')
            ax.set_ylim(bottom=0);time_axis(ax)
    h,l=axes[0,0].get_legend_handles_labels();fig.legend(h,l,loc='outside lower center',ncol=4,frameon=False)
    fig.suptitle('Thirty-degree arcs · hidden Gram discrepancies\nWidth-8192 three-seed reference, 206 saved times',fontsize=15)
    save(fig,'gram_and_increment_errors')

    paths=[output/'network'/f'arcs30_n8192_s{s}'/'gram.npy' for s in (11,29,47)]
    networks=[np.load(p,mmap_mode='r') for p in paths]
    indices=[int(np.flatnonzero(times==t)[0]) for t in (0,1,5,40)]
    for p in paths:raw_hashes[str(p.relative_to(output))]=sha(p)
    for suffix,title in (('', 'N = 5'),('_fine','N = 5, finest quadrature')):
        path=output/'closure'/f'arcs30_N5{suffix}'/'gram.npy'
        closure=np.load(path,mmap_mode='r');raw_hashes[str(path.relative_to(output))]=sha(path)
        for layer in (1,2):
            finite=np.stack([sum(np.asarray(g[k,layer-1,16:,16:])/3 for g in networks) for k in indices])
            predicted=np.stack([closure[k,layer-1,16:,16:] for k in indices]);error=predicted-finite
            limit=max(float(np.abs(finite).max()),float(np.abs(predicted).max()))
            error_limit=max(float(np.abs(error).max()),1e-12)
            fig,axes=plt.subplots(3,4,figsize=(12,8.8),constrained_layout=True)
            for row,matrices in enumerate((finite,predicted,error)):
                lim=error_limit if row==2 else limit
                for col,t in enumerate((0,1,5,40)):
                    ax=axes[row,col]
                    im=ax.imshow(matrices[col],origin='lower',extent=(0,360,0,360),vmin=-lim,vmax=lim,
                                 cmap='RdBu_r',interpolation='nearest')
                    ax.set_xticks([0,180,360]);ax.set_yticks([0,180,360])
                    if row==0:ax.set_title(f't = {t}')
                    if col==0:ax.set_ylabel(('Network: 3-seed mean',f'Closure: {title}','Closure − network')[row]+'\nInput angle (degrees)')
                    if row==2:ax.set_xlabel('Input angle (degrees)')
                fig.colorbar(im,ax=axes[row,:],fraction=.018,pad=.015)
            fig.suptitle(f'Layer {layer} Gram evolution · training on ±30° arcs\n128 × 128 circle panel; network width 8192',fontsize=15)
            save(fig,f'layer{layer}_gram_evolution{suffix}')

    fig,ax=plt.subplots(figsize=(6,6),constrained_layout=True)
    theta=np.linspace(0,2*np.pi,400)
    ax.plot(np.cos(theta),np.sin(theta),c='#b9bec8',lw=1)
    with np.load(GENERATED/'GRAM_20260914_v1'/'inputs.npz') as old:
        previous=old['arcs_inputs'];previous_y=old['arcs_labels']
    for label,color in ((1,'#214b80'),(-1,'#c4484b')):
        u=inputs['arcs30_inputs'][inputs['arcs30_labels']==label]
        ax.scatter(u[:,0],u[:,1],c=color,s=65,edgecolors='white',label=f'New ±30° points, label {label:+d}',zorder=4)
        u=previous[previous_y==label]
        ax.scatter(u[:,0],u[:,1],facecolors='none',edgecolors=color,s=45,alpha=.5,
                   label='Earlier ±5° points' if label==1 else None,zorder=3)
    ax.plot([-1,1],[-1,1],'--',c='#6e7580',lw=1,label='Separator u₁ = u₂')
    ax.set(aspect='equal',xlim=(-1.15,1.15),ylim=(-1.15,1.15),xlabel='Normalized input u₁',ylabel='Normalized input u₂',
           title='Same 16 inputs and labels, broader geometry\nActual sampled deviations now reach ±30°')
    ax.legend(loc='lower left',fontsize=8,frameon=False);ax.grid(alpha=.15)
    save(fig,'training_inputs_5_vs_30_degrees')
    manifest=dict(source_sha256=sha(__file__),comparison_sha256=sha(output/'arc30_comparison.json'),
        inputs_sha256=sha(output/'inputs.npz'),old_inputs_sha256=sha(GENERATED/'GRAM_20260914_v1'/'inputs.npz'),
        raw_gram_sha256=raw_hashes,command=sys.argv,numpy_version=np.__version__,matplotlib_version=matplotlib.__version__,
        products=products)
    (destination/'figures.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(dict(status='complete',figure_files=len(products),directory=str(destination))))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    main(parser.parse_args().output)
