"""Reproducible scientific plots of the fixed sparse-circle campaign."""
import argparse, hashlib, json, subprocess
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

COLORS={'NTK':'#252525','N1':'#1670b1','N2':'#69a6d0','N3':'#ed8b23','N5':'#8250a3'}
LABELS={'NTK':'Frozen NTK','N1':'N = 1','N2':'N = 2','N3':'N = 3','N5':'N = 5'}
HERE=Path(__file__).resolve().parent

def power(f):
    z=np.fft.rfft(f)/len(f);p=np.abs(z)**2;p[1:-1]*=2
    return p/p.sum()
def bandwidth(f):
    p=power(f);return float(np.sqrt(p@np.arange(len(p))**2))
def save(fig,out,name):
    fig.savefig(out/(name+'.png'),dpi=180,bbox_inches='tight')
    fig.savefig(out/(name+'.pdf'),bbox_inches='tight');plt.close(fig)
def data(analysis,case,N=1):
    p=analysis/f'{case}_N{N}_main.npz'
    if not p.exists():return None
    with np.load(p,allow_pickle=False) as a:return {k:a[k] for k in a.files}
def styles(key):return dict(color=COLORS[key],lw=2.1,ls='--' if key in ('NTK','N2') else '-')
def sorted_angle(f,rotation):
    psi=(np.arange(len(f))*360/len(f)-rotation+180)%360-180;idx=np.argsort(psi)
    return psi[idx],f[idx]

def run(campaign,analysis,out):
    campaign=Path(campaign).resolve();analysis=Path(analysis).resolve();out=Path(out).resolve();out.mkdir()
    plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','axes.grid':True,'grid.alpha':.18})
    pages=[]
    fig,axs=plt.subplots(2,2,figsize=(13,9),constrained_layout=True)
    for N in (1,2,3,5):
        a=data(analysis,'pair_d15_r45',N)
        if a is None:continue
        x,y=sorted_angle(a['learned_final'],45)
        for ax in axs[0]:ax.plot(x,y,label=LABELS[f'N{N}'],**styles(f'N{N}'))
    a=data(analysis,'pair_d15_r45',1)
    if a is not None:
        x,y=sorted_angle(a['ntk_endpoint'],45)
        for ax in axs[0]:ax.plot(x,y,label=LABELS['NTK'],**styles('NTK'));ax.scatter([-7.5,7.5],[-1,1],s=45,c='black',zorder=8)
    axs[0,0].set(title='Opposite labels only 15° apart',xlabel='Angle from the pair midpoint (degrees)',ylabel='Raw output');axs[0,0].legend(ncol=2,fontsize=9)
    axs[0,1].set(title='The same curves near the training points',xlabel='Angle from midpoint (degrees)',ylabel='Raw output',xlim=(-45,45),ylim=(-1.8,1.8))
    for key in ('NTK','N1','N2','N3','N5'):
        angles=[];ks=[];amplitudes=[]
        for d in (15,30,60,90,150):
            a=data(analysis,f'pair_d{d}_r45',1 if key=='NTK' else int(key[1:]))
            if a is None:continue
            f=a['ntk_endpoint' if key=='NTK' else 'learned_final'];angles.append(d);ks.append(bandwidth(f));amplitudes.append(abs(f).max())
        axs[1,0].plot(angles,ks,marker='o',ms=4,label=LABELS[key],**styles(key))
        axs[1,1].plot(angles,amplitudes,marker='o',ms=4,label=LABELS[key],**styles(key))
    axs[1,0].set(title='Effective angular frequency',xlabel='Separation of opposite labels (degrees)',ylabel=r'$k_{\rm rms}=\|f\prime\|_2/\|f\|_2$')
    axs[1,1].set(title='Overshoot away from the training points',xlabel='Separation of opposite labels (degrees)',ylabel='Maximum |output| / label amplitude')
    axs[1,1].axhline(1,color='gray',lw=.8)
    fig.suptitle('Angular spacing, frequency, and overshoot',fontsize=18)
    save(fig,out,'frequency_geometry');pages.append('frequency_geometry')

    fig,axs=plt.subplots(1,2,subplot_kw={'projection':'polar'},figsize=(13,6.8),constrained_layout=True)
    for ax,case,title in zip(axs,('pair_d30_r45','quad_d30'),('Two opposite-label points, 30° apart','Four alternating labels, 30° spacing')):
        arrays={f'N{N}':data(analysis,case,N) for N in (1,3,5)};arrays={k:v for k,v in arrays.items() if v is not None}
        if not arrays:ax.set_visible(False);continue
        a=next(iter(arrays.values()));curves={k:v['learned_final'] for k,v in arrays.items()};curves['NTK']=a['ntk_endpoint']
        R=1+max(float(abs(f).max()) for f in curves.values());theta=np.linspace(0,2*np.pi,len(next(iter(curves.values())))+1)
        for key,f in curves.items():ax.plot(theta,R+np.r_[f,f[0]],label=LABELS[key],**styles(key))
        ax.plot(theta,np.full_like(theta,R),color='gray',lw=1,ls=':',label='Reference circle')
        cfg=json.loads((campaign/f'{case}_N1_main/config.json').read_text());t=np.deg2rad(cfg['angles_degrees']);y=np.array(cfg['labels'])
        ax.scatter(t,np.full_like(t,R),facecolors='white',edgecolors='black',s=38,zorder=8)
        ax.scatter(t,R+y,c='black',s=34,zorder=8)
        ax.set_title(title+f'\nRadius = {R:.2f} + output',pad=22)
        ax.grid(alpha=.22)
    axs[0].legend(loc='lower center',bbox_to_anchor=(.5,-.18),ncol=3,fontsize=9)
    fig.suptitle('Fitted circle curves: closures and the frozen NTK\nHollow dots: inputs on the reference circle; filled dots: training labels',fontsize=14)
    save(fig,out,'radial_comparison');pages.append('radial_comparison')

    multi=[('triple_d20','3 points: 20° spacing'),('triple_d40','3 points: 40° spacing'),('triple_d60','3 points: 60° spacing'),('quad_d15','4 points: 15° spacing'),('quad_d30','4 points: 30° spacing'),('quad_d45','4 points: 45° spacing')]
    if any(data(analysis,c) is not None for c,_ in multi):
        fig,axs=plt.subplots(2,3,figsize=(14,7.5),constrained_layout=True)
        for ax,(case,title) in zip(axs.flat,multi):
            for key in ('NTK','N1','N3','N5'):
                a=data(analysis,case,1 if key=='NTK' else int(key[1:]))
                if a is None:continue
                f=a['ntk_endpoint' if key=='NTK' else 'learned_final'];f=f/np.sqrt(np.mean(f*f));x,y=sorted_angle(f,45)
                ax.plot(x,y,label=LABELS[key],**styles(key))
            ax.set(title=title,xlabel='Angle from midpoint (degrees)',ylabel='Output / circle RMS')
        axs[0,0].legend(fontsize=8,ncol=2)
        fig.suptitle('Three and four points: comparing normalized shapes\nEach curve is divided by its own RMS; this panel deliberately removes amplitude',fontsize=15)
    save(fig,out,'multi_point_shapes');pages.append('multi_point_shapes')

    fig,axs=plt.subplots(1,3,figsize=(14,4.7),constrained_layout=True)
    for ax,delta in zip(axs,(15,60,150)):
        notes=[]
        for N in (1,5):
            a=data(analysis,f'pair_d{delta}_r45',N)
            f=a['learned_final'];g=a['template_normalized_tanh_sine']
            x,y=sorted_angle(f,45);_,z=sorted_angle(g,45)
            ax.plot(x,y,label=f'N = {N}, learned',**styles(f'N{N}'))
            ax.plot(x,z,color=COLORS[f'N{N}'],lw=1.4,ls='--',label=f'N = {N}, tanh–sine fit')
            err=np.linalg.norm(f-g)/np.linalg.norm(f)
            notes.append(f'N = {N}: {100*err:.2f}% reconstruction error')
        ax.scatter([-delta/2,delta/2],[-1,1],s=28,c='black',zorder=8)
        ax.set(title=f'Opposite labels {delta}° apart',xlabel='Angle from midpoint (degrees)',ylabel='Raw output')
        ax.text(.02,.97,'\n'.join(notes),transform=ax.transAxes,va='top',fontsize=8)
    axs[1].legend(loc='lower right',fontsize=8)
    fig.suptitle('A one-parameter description of the learned two-point curve\nFitted to the output after training; a reconstruction, not an endpoint theorem',fontsize=14)
    save(fig,out,'simple_curve_reconstruction');pages.append('simple_curve_reconstruction')

    fig,axs=plt.subplots(2,3,figsize=(12.5,7),constrained_layout=True)
    matrices=[];mode=np.arange(-9,10,2)
    for N in (1,3,5):
        raw=campaign/f'pair_d30_r45_N{N}_main/observations.npz'
        if not raw.exists():continue
        with np.load(raw,allow_pickle=False) as a:
            for state in ('initial','final'):
                K=a[f'kernel_circle_{state}'].sum(0);F=np.fft.ifft(np.fft.fft(K,axis=0),axis=1)/len(K);F/=np.linalg.norm(F)
                block=abs(F[np.ix_(mode%len(K),mode%len(K))])
                matrices.append((N,state,np.log10(np.maximum(block,1e-5))))
    for N,state,M in matrices:
        ax=axs[0 if state=='initial' else 1,(1,3,5).index(N)]
        im=ax.imshow(M,vmin=-5,vmax=0,cmap='magma',origin='lower',extent=(-10,10,-10,10));ax.grid(False)
        ax.set(title=f'N = {N}, {state}',xlabel='Source Fourier mode',ylabel='Output Fourier mode',xticks=[-9,-5,-1,1,5,9],yticks=[-9,-5,-1,1,5,9])
    if matrices:fig.colorbar(im,ax=axs.ravel().tolist(),label='log10 normalized Fourier-kernel magnitude',shrink=.8)
    fig.suptitle('Training changes how angular modes interact\nTwo-point case at 30°; each full kernel normalized to unit Frobenius norm',fontsize=15)
    save(fig,out,'learned_kernel_modes');pages.append('learned_kernel_modes')

    # Record precise input and producer hashes; panels retain raw arrays elsewhere.
    manifest=dict(campaign=str(campaign),analysis=str(analysis),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        analysis_summary_sha256=hashlib.sha256((analysis/'summary.json').read_bytes()).hexdigest(),pages=pages,
        description='Finite mild-settling outputs where recorded; capped runs remain finite-time diagnostics. No new training.')
    with (out/'plot_record.json').open('x') as f:json.dump(manifest,f,indent=2)
    subprocess.run(['pdfunite',*[str(out/(name+'.pdf')) for name in pages],str(out/'spectral_mechanism_report.pdf')],check=True)
    return manifest

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--campaign',required=True);p.add_argument('--analysis',required=True);p.add_argument('--output',required=True);a=p.parse_args();run(a.campaign,a.analysis,a.output)
