"""Plot saved circle predictions; no fitting or scientific parameter selection."""
from pathlib import Path
import argparse
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    values=np.load(a.out/'circle_predictions.npz')
    metrics=json.loads((a.out/'validation.json').read_text())
    fig,axs=plt.subplots(2,2,figsize=(12,6.8),sharex=True,
                        gridspec_kw={'height_ratios':[2,1]},layout='constrained')
    theta=values['degrees']
    for col,width in enumerate([16,32]):
        dense=values[f'n{width}_dense']; fit=values[f'n{width}_decoded']
        parent=values[f'n{width}_parent']
        ax=axs[0,col]
        ax.plot(theta,dense,color='#202938',lw=2.4,label='Dense fitted network')
        ax.plot(theta,fit,color='#147d92',lw=2,ls='--',label='Decoded scalar model, 12 modes')
        ax.scatter([10,125],[1,-1],color='#b54f17',marker='x',s=70,zorder=5,label='Two training labels')
        metric=metrics['circle'][str(width)]
        ax.set_title(f"Width {width} · circle RMS error {metric['decoded_dense_rms']:.4f}")
        ax.set_ylim(-1.2,1.2); ax.grid(alpha=.15)
        ax=axs[1,col]
        ax.axhline(0,color='#666666',lw=.8)
        ax.plot(theta,fit-dense,color='#147d92',lw=1.8,label='Scalar decoder − dense')
        ax.plot(theta,parent-dense,color='#9b7aa0',lw=1.1,alpha=.8,label='Population P1 − dense')
        ax.set_ylim(-.11,.11);ax.set_xlim(0,360)
        ax.set_xticks(np.arange(0,361,60));ax.set_xlabel('Input angle (degrees)');ax.grid(alpha=.15)
    axs[0,0].set_ylabel('Fitted output');axs[1,0].set_ylabel('Output discrepancy')
    axs[0,0].legend(frameon=False,fontsize=8,loc='lower left')
    axs[1,0].legend(frameon=False,fontsize=8,loc='lower left')
    fig.suptitle('Whole-circle prediction from a scalar ODE and a terminal weight decoder',fontsize=14)
    fig.savefig(a.out/'circle_comparison.png',dpi=180)
    fig.savefig(a.out/'circle_comparison.pdf')


if __name__=='__main__':main()
