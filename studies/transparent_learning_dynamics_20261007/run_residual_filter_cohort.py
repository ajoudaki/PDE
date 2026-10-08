"""One frozen numerical-repair cohort, each trajectory in its own process."""
from pathlib import Path
import subprocess
import sys
DRIVER=Path(__file__).with_name('residual_filter_experiment.py')
def call(kind,n,seed,h=.2,method='filtered',replicate=False):
    args=[sys.executable,str(DRIVER),kind,'--n',str(n),'--seed',str(seed),'--h',str(h),'--method',method]
    if replicate:args+=['--replicate']
    subprocess.run(args,check=True)
if __name__=='__main__':
    for method,h in (('filtered',.2),('rk4',.025)):
        for n in (512,1024):
            for seed in (101,202,303):call('dense',n,seed,h,method)
    call('dense',512,101,.0125,'rk4')
    for h in (.4,.1,.05):call('dense',512,101,h)
    for seed in (1701,1702,1703):call('causal',256,seed)
    for h in (.2,.1):call('causal',128,1701,h)
    call('causal',512,1701)
    call('causal',256,1701,.4)
    call('causal',256,1701,replicate=True)
