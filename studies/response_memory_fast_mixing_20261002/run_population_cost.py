"""Run the frozen accuracy-cost campaign with one worker per allocated GPU."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--lane',type=int,choices=[0,1],required=True)
    p.add_argument('--generated',type=Path,required=True)
    p.add_argument('--repair-completion',action='store_true')
    a=p.parse_args()
    producer=Path(__file__).with_name('fast_training.py').resolve()
    lane=a.lane
    batches=[(f'population_cost_gpu{lane}_a',
              'gaussian' if lane==0 else 'quarter_circle',range(7601,7609),[512,2048,8192,16384]),
             (f'population_cost_gpu{lane}_b',
              'quarter_circle' if lane==0 else 'gaussian',range(7609,7617),[512,2048,8192,16384]),
             (f'population_cost_gpu{lane}_reference','quarter_circle',
              range(8001+16*lane,8017+16*lane),[32768])]
    if a.repair_completion:
        batches=[(name+'_repair01',kind,seeds,widths) for name,kind,seeds,widths in batches
                 if not (lane==1 and name.endswith('_a'))]
    begun=time.monotonic()
    records=[]
    for name,kind,seeds,widths in batches:
        command=[sys.executable,str(producer),'--out',str(a.generated/name),
                 '--widths',*map(str,widths),'--seeds',*map(str,seeds),'--kinds',kind,
                 '--compact','--tf32','--protocol','POPULATION_COST_PROTOCOL.md']
        remaining=600-(time.monotonic()-begun)
        if remaining<=0:
            raise RuntimeError('ten GPU-process minute worker budget exhausted')
        with (a.generated/f'{name}.log').open('w') as log:
            result=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,
                                  timeout=remaining,check=False)
        records.append(dict(command=command,returncode=result.returncode,
                            elapsed_seconds=time.monotonic()-begun))
        record=dict(lane=lane,visible_gpu=os.environ.get('CUDA_VISIBLE_DEVICES'),
                    producer_sha256=hashlib.sha256(producer.read_bytes()).hexdigest(),
                    records=records,elapsed_seconds=time.monotonic()-begun)
        (a.generated/(f'population_cost_lane{lane}'+('_repair01.json' if a.repair_completion else '.json'))).write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps(dict(batch=name,returncode=result.returncode,
                              elapsed_seconds=time.monotonic()-begun)),flush=True)
        if result.returncode:
            raise RuntimeError(f'producer failed; retained log {name}.log')


if __name__=='__main__':
    main()
