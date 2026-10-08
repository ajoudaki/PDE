"""Exact predeclared multisample run list; one child process per trajectory."""
import argparse
import subprocess
import sys
from pathlib import Path

DRIVER=Path(__file__).with_name('multisample_experiment.py')


def call(kind,m,n,seed,h=.4,method='euler',mode='full'):
    subprocess.run([sys.executable,str(DRIVER),kind,'--m',str(m),'--n',str(n),
                    '--seed',str(seed),'--h',str(h),'--method',method,'--mode',mode],check=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('cohort',choices=('dense','causal_main','causal_refine','causal_controls'))
    args=parser.parse_args()
    if args.cohort=='dense':
        for m in (4,8,16):
            for n in (512,1024):
                for seed in (101,202,303):call('dense',m,n,seed)
            for h in (.1,.05):call('dense',m,512,101,h,method='rk4')
        for mode in ('frozen_middle','affine_gates'):
            for seed in (101,202):call('dense',8,512,seed,mode=mode)
            call('dense',8,512,101,h=.2,mode=mode)
    elif args.cohort=='causal_main':
        for m in (4,8,16):
            for seed in (1701,1702,1703):call('causal',m,512,seed)
    elif args.cohort=='causal_refine':
        for m in (4,8,16):
            call('causal',m,1024,1701)
            for h in (.4,.2):call('causal',m,256,1701,h=h)
    else:
        for mode in ('no_reciprocal','no_middle'):
            for seed in (1701,1702):call('causal',8,512,seed,mode=mode)
