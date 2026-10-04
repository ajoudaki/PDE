"""GPU1-only bounded completion; retains original failures and candidate costs."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def main():
    if os.environ.get('CUDA_VISIBLE_DEVICES')!='1':
        raise RuntimeError('this completion is authorized on physical GPU1 only')
    study=Path(__file__).resolve().parent
    generated=study.parent.parent/'data/generated/response_memory_fast_mixing_20261002'
    verification=json.loads((generated/'population_cost_split_verification01/verification.json').read_text())
    if not verification['passed']:raise RuntimeError('verification did not pass')
    for source,expected in verification['source_hashes'].items():
        if hashlib.sha256(Path(source).read_bytes()).hexdigest()!=expected:
            raise RuntimeError('source changed after verification: '+source)
    out=generated/'population_cost_gpu1_reference_split01'
    command=[sys.executable,str(study/'fast_training_split_reference.py'),'--out',str(out),
        '--widths','32768','--seeds',*map(str,range(8001,8033)),'--kinds','quarter_circle',
        '--compact','--tf32','--protocol','POPULATION_COST_PROTOCOL.md']
    record={'command':command,'cwd':str(Path.cwd()),'visible_gpu':'1',
        'reference_timeout_seconds':700,'verification':verification,'started_utc':time.strftime('%Y-%m-%d %H:%M:%S UTC',time.gmtime()),
        'worker_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    started=time.monotonic()
    record_path=generated/'population_cost_split_worker01.json'
    record_path.write_text(json.dumps(record,indent=2)+'\n')
    try:
        with (generated/'population_cost_gpu1_reference_split01.log').open('x') as log:
            result=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,timeout=700,check=False)
        record['returncode']=result.returncode
    except subprocess.TimeoutExpired:
        record['returncode']='TIMEOUT'
    finally:
        record['elapsed_seconds']=time.monotonic()-started
        record['ended_utc']=time.strftime('%Y-%m-%d %H:%M:%S UTC',time.gmtime())
        record_path.write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps(record),flush=True)
    if record['returncode']!=0:raise RuntimeError('bounded reference producer failed')


if __name__=='__main__':main()
