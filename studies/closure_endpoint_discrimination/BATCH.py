"""Budgeted two-GPU/two-CPU dispatcher for one predeclared campaign batch."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import time

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]


def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()


def run(campaign,jobs):
    campaign=Path(campaign).resolve();jobs=Path(jobs).resolve();folder=jobs.parent
    target=folder/'batch.json'
    if target.exists():raise FileExistsError(target)
    manifest=json.loads((campaign/'manifest.json').read_text());spec=json.loads(jobs.read_text())
    for path,expected in manifest['sources_sha256'].items():
        if sha(ROOT/path)!=expected:raise RuntimeError('Frozen source changed: '+path)
    for path,expected in manifest['inputs_sha256'].items():
        if sha(campaign/path)!=expected:raise RuntimeError('Input changed: '+path)
    budget=manifest['budget'];startpath=campaign/'compute_start.json'
    if not startpath.exists():
        with startpath.open('x') as f:json.dump(dict(unix_time=time.time()),f)
    campaign_start=json.loads(startpath.read_text())['unix_time']
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
        PYTHONDONTWRITEBYTECODE='1',CUBLAS_WORKSPACE_CONFIG=':4096:8',MPLBACKEND='Agg')
    queue=list(spec['jobs']);active={};results=[];started=time.monotonic();reason=None
    slots=[('gpu0','cuda:0'),('gpu1','cuda:1'),('cpu0','cpu'),('cpu1','cpu')]
    try:
        while queue or active:
            if time.time()-campaign_start>budget['scientific_seconds']:reason='campaign_time_limit'
            if shutil.disk_usage(campaign).free<budget['minimum_free_bytes']:reason='free_disk_limit'
            size=sum(p.stat().st_size for p in campaign.rglob('*') if p.is_file())
            if size>budget['output_bytes']:reason='output_disk_limit'
            if reason:break
            for slot,device in slots:
                if slot in active:continue
                match=next((i for i,j in enumerate(queue) if j['device']==device or (device.startswith('cuda') and j['device']=='cuda:auto')),None)
                if match is None:continue
                job=queue.pop(match);config=json.loads(Path(job['config_path']).read_text());config['device']=device
                resolved=folder/(job['name']+'.resolved.json')
                with resolved.open('x') as f:json.dump(config,f,indent=2)
                cmd=[manifest['python'],'-B',str(HERE/('NETWORK.py' if job['kind']=='network' else 'CLOSURE.py')),
                     '--config',str(resolved),'--out',job['out']]
                if job.get('resume'):cmd+=['--resume',job['resume']]
                log=open(folder/(job['name']+'.log'),'x')
                process=subprocess.Popen(cmd,cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
                active[slot]=dict(job=job,process=process,log=log,cmd=cmd,start=time.monotonic())
                print(json.dumps(dict(event='start',job=job['name'],device=device)),flush=True)
            for slot,item in list(active.items()):
                proc=item['process'];age=time.monotonic()-item['start'];timeout=age>budget['worker_seconds']
                if timeout and proc.poll() is None:os.killpg(proc.pid,signal.SIGTERM)
                code=proc.poll()
                if code is None:continue
                item['log'].close();job=item['job'];record_path=Path(job['out'])/'record.json'
                producer=json.loads(record_path.read_text()) if record_path.exists() else {}
                result=dict(name=job['name'],out=job['out'],command=item['cmd'],exit_code=code,
                            elapsed_seconds=age,producer_status=producer.get('status'),last_time=producer.get('last_time'),settled=producer.get('settled'))
                results.append(result);del active[slot]
                print(json.dumps(dict(event='finish',**result)),flush=True)
                if code!=0 or producer.get('status')!='complete':reason='worker_failure:'+job['name'];break
            if reason:break
            time.sleep(1)
    finally:
        for item in active.values():
            if item['process'].poll() is None:os.killpg(item['process'].pid,signal.SIGTERM)
        for item in active.values():
            try:code=item['process'].wait(timeout=5)
            except subprocess.TimeoutExpired:os.killpg(item['process'].pid,signal.SIGKILL);code=item['process'].wait()
            item['log'].close();results.append(dict(name=item['job']['name'],out=item['job']['out'],command=item['cmd'],exit_code=code,interrupted=True))
        report=dict(complete=reason is None and len(results)==len(spec['jobs']),reason=reason,
                    results=results,pending=[x['name'] for x in queue],elapsed_seconds=time.monotonic()-started,
                    campaign_elapsed_seconds=time.time()-campaign_start,jobs_file_sha256=sha(jobs))
        with target.open('x') as f:json.dump(report,f,indent=2)
        print(json.dumps(dict(complete=report['complete'],reason=reason,elapsed_seconds=report['elapsed_seconds'])),flush=True)
    if not report['complete']:raise SystemExit(1)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--campaign',required=True);p.add_argument('--jobs',required=True)
    a=p.parse_args();run(a.campaign,a.jobs)
