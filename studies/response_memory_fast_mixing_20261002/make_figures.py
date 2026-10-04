"""Reproduce the fast-environment summary from saved, versioned runs."""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from analyze_training import summarize


def main():
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    a.out.mkdir(parents=True,exist_ok=False)
    pilot=summarize(a.data/'training02');confirm=summarize(a.data/'confirmation01')
    merged=pilot|confirm
    scale=json.loads((a.data/'scaling01'/'summary.json').read_text())
    timing={k:np.array([r['training_seconds'] for r in scale['rows'] if r['kind']==k])
            for k in ('gaussian','quarter_circle')}
    memory={k:np.array([r['peak_allocated_bytes'] for r in scale['rows'] if r['kind']==k])
            for k in ('gaussian','quarter_circle')}
    checks={}
    for k in timing:
        tag=f'{k}_n16384_s7511_dt0.02.npz'
        original=np.load(a.data/'scaling01'/tag)['predictions']
        repeat=np.load(a.data/'scaling_reproduction01'/tag)['predictions']
        ieee=np.load(a.data/'scaling_ieee01'/tag)['predictions']
        checks[k]=dict(reproduction_max_rms=float(np.sqrt(np.mean((repeat-original)**2,axis=1)).max()),
                       tf32_max_rms=float(np.sqrt(np.mean((ieee-original)**2,axis=1)).max()))
    speed=float(np.median(timing['gaussian'])/np.median(timing['quarter_circle']))
    mem=float(np.median(memory['gaussian'])/np.median(memory['quarter_circle']))
    report=dict(ensemble=merged,speed_ratio=speed,peak_memory_ratio=mem,
                numerical_checks=checks,
                provenance={str(p):hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in (Path(__file__),Path(__file__).with_name('analyze_training.py'))})
    (a.out/'results.json').write_text(json.dumps(report,indent=2)+'\n')
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,
                         'axes.labelsize':10,'figure.dpi':150})
    fig,axes=plt.subplots(2,2,figsize=(10,7.1),layout='constrained')
    colors={'flat':'#b46a35','quarter_circle':'#24776c','gaussian_diagonal':'#7c68a6'}
    labels={'flat':'Flat spectrum','quarter_circle':'Gaussian spectrum','gaussian_diagonal':'Gaussian diagonal'}
    widths=np.array([512,2048,8192])
    for k,c in colors.items():
        axes[0,0].plot(widths,[merged[str(n)]['distances'][k][0] for n in widths],'-o',color=c,label=labels[k])
        axes[0,1].plot(widths,[merged[str(n)]['distances'][k][2] for n in widths],'-o',color=c,label=labels[k])
    for ax in axes[0]:
        ax.set_xscale('log',base=2);ax.set_yscale('log');ax.set_xticks(widths,[str(n) for n in widths])
        ax.set_xlabel('Hidden width');ax.grid(alpha=.18)
    axes[0,0].set_ylabel('Prediction discrepancy, RMS')
    axes[0,0].set_title('A. Distance to Gaussian ensemble learning')
    axes[0,0].legend(frameon=False,fontsize=8)
    axes[0,1].set_ylabel('Second-layer Gram discrepancy, RMS')
    axes[0,1].set_title('B. Distance in evolving feature geometry')
    xx=np.arange(2);keys=['gaussian','quarter_circle'];names=['Dense Gaussian\nmixer','Fast Gaussian-spectrum\nmixer']
    axes[1,0].bar(xx,[np.median(timing[k]) for k in keys],color=['#536477','#24776c'],width=.6)
    axes[1,0].set_xticks(xx,names);axes[1,0].set_ylabel('Training + scheduled evaluation (s)')
    axes[1,0].set_title(f'C. Width16,384: {speed:.2f}× faster')
    axes[1,1].bar(xx,[np.median(memory[k])/2**20 for k in keys],color=['#536477','#24776c'],width=.6)
    axes[1,1].set_xticks(xx,names);axes[1,1].set_ylabel('Peak allocated CUDA memory (MiB)')
    axes[1,1].set_title(f'D. Width16,384: {mem:.2f}× less peak memory')
    fig.suptitle('A fast fixed environment for the order-one response-memory learner',fontsize=13)
    fig.savefig(a.out/'fast_environment.png',bbox_inches='tight')
    fig.savefig(a.out/'fast_environment.pdf',bbox_inches='tight')
    plt.close(fig)
    print(json.dumps({k:report[k] for k in ('speed_ratio','peak_memory_ratio','numerical_checks')},indent=2))


if __name__=='__main__':main()
