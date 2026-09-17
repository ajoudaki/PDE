#!/usr/bin/env python3
"""Bounded four-lane launcher for the fixed XOR plan; no scientific adaptation."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import queue
import signal
import subprocess
import sys
import threading
import time

from PREPARE import ROOT, STUDY, sha, write


def main(output):
    manifest=json.loads((output/'manifest.json').read_text())
    assert manifest['status']=='frozen' and manifest['scientific_start_epoch']
    for path,digest in manifest['source_hashes'].items():
        assert sha(ROOT/path)==digest,path
    assert sha(output/'inputs.npz')==manifest['inputs_sha256']
    deadline=manifest['scientific_start_epoch']+1200
    jobs={family:queue.Queue() for family in ('network','closure')}
    for config in sorted(manifest['network_runs'], key=lambda c:(-c['width'],c['step'])):
        jobs['network'].put(config)
    for config in sorted(manifest['closure_runs'],key=lambda c:(-c['order'],-c['population_nodes'],c['step'])):
        jobs['closure'].put(config)
    lock=threading.Lock(); active={}; results=[]; stop=threading.Event()

    def halt(*_):
        stop.set()
        with lock:
            for process in active.values():
                if process.poll() is None: process.terminate()
    signal.signal(signal.SIGTERM,halt)
    signal.signal(signal.SIGINT,halt)

    def lane(family,index):
        while not stop.is_set() and time.time()<deadline:
            try: config=jobs[family].get_nowait()
            except queue.Empty: return
            name=config['name']; start=time.time()
            command=[sys.executable,'-B',str(STUDY/('NETWORK.py' if family=='network' else 'CLOSURE.py')),
                     '--output',str(output),'--run-id',name]
            env=os.environ.copy()
            env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
                       PYTHONDONTWRITEBYTECODE='1',MPLCONFIGDIR=str(output/'matplotlib_cache'))
            if family=='network': env['CUDA_VISIBLE_DEVICES']=str(index)
            logfile=output/f'{family}_{name}.log'
            with logfile.open('x') as log:
                process=subprocess.Popen(command,cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT)
                with lock: active[(family,index)]=process
                reason=None
                while process.poll() is None:
                    if stop.is_set() or time.time()>=min(deadline,start+600):
                        reason='global or worker deadline/interruption'; process.terminate()
                        try: process.wait(timeout=5)
                        except subprocess.TimeoutExpired: process.kill();process.wait()
                        break
                    time.sleep(0.5)
                record={'family':family,'name':name,'exit_code':process.returncode,'wall_seconds':time.time()-start,
                        'command':command,'lane':index,'reason':reason,'log_sha256':sha(logfile)}
                with lock:
                    active.pop((family,index),None); results.append(record)
                    progress={'completed_workers':len(results),'active':[list(k) for k in active],
                              'elapsed_seconds':time.time()-manifest['scientific_start_epoch'],'last':record}
                    (output/'progress.json').write_text(json.dumps(progress,indent=2)+'\n')
                print(json.dumps({'finished':name,'family':family,'exit':process.returncode,
                                  'completed':len(results),'seconds':round(record['wall_seconds'],2)}),flush=True)
                jobs[family].task_done()
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures=[pool.submit(lane,family,index) for family in ('network','closure') for index in range(2)]
        try:
            for future in futures: future.result()
        finally: halt()
    summary={'status':'complete' if len(results)==16 and all(r['exit_code']==0 for r in results) else 'incomplete',
             'workers':results,'scientific_wall_seconds':time.time()-manifest['scientific_start_epoch'],
             'source_sha256':sha(__file__),'manifest_sha256':sha(output/'manifest.json'),
             'command':sys.argv,'cwd':str(ROOT),'pending':{f:jobs[f].qsize() for f in jobs}}
    write(output/'supervisor.json',summary)
    (output/'progress.json').write_text(json.dumps({'status':summary['status'],'active':[],
                                                 'completed_workers':len(results),'scientific_wall_seconds':summary['scientific_wall_seconds']},indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='workers'}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True)
    main(p.parse_args().output.resolve())
