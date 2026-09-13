"""Bounded serial executor for the predeclared independent scientific checks."""
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

ROOT=Path('/home/amir/Codes/PDE')
OUT=ROOT/'data/generated/observable_hierarchy/H4_scientific_E_v3'
EDITION=ROOT/'data/generated/observable_hierarchy/H4_candidate_v3'
OUT.mkdir(parents=True,exist_ok=False)
(OUT/'tmp').mkdir()
environment=dict(os.environ,PYTHONPATH=str(EDITION/'code'),PYTHONDONTWRITEBYTECODE='1',
                 TMPDIR=str(OUT/'tmp'),H4_LAW_TEST_SCRATCH=str(OUT/'tmp'),H4_VALIDATION_TEST_SCRATCH=str(OUT/'tmp'))
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    environment[key]='1'
commands=[
    [sys.executable,'-B','-m','unittest','discover','-s','code/tests','-p','test_observable*.py','-v'],
    [sys.executable,'-B',str(ROOT/'data/generated/observable_hierarchy/H4_full_tests_v1/reference_certificate.py')],
    [sys.executable,'-B',str(ROOT/'studies/observable_hierarchy/H4_scientific_E_v3_check.py')],
]
result=dict(predeclared_sha256=hashlib.sha256((ROOT/'studies/observable_hierarchy/H4_scientific_E_v3_predeclared.md').read_bytes()).hexdigest(),
            budget=dict(cpu_seconds=600,address_space_bytes=4*2**30,numerical_threads=1),commands=[],status='running')
baseline=resource.getrusage(resource.RUSAGE_CHILDREN)
start=time.process_time()
for i,command in enumerate(commands):
    prior=resource.getrusage(resource.RUSAGE_CHILDREN)
    consumed=prior.ru_utime+prior.ru_stime-baseline.ru_utime-baseline.ru_stime+time.process_time()-start
    cap=min(180,int(600-consumed))
    if cap<1:
        result['status']='budget_exhausted';break
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(cap,cap))
        resource.setrlimit(resource.RLIMIT_AS,(4*2**30,4*2**30))
    wall=time.monotonic()
    with (OUT/f'check_{i}.log').open('x') as stream:
        try:
            process=subprocess.run(command,cwd=EDITION,env=environment,stdout=stream,stderr=subprocess.STDOUT,
                                   preexec_fn=limits,timeout=240)
            status='complete'; code=process.returncode
        except subprocess.TimeoutExpired:
            status='timeout';code=None
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    result['commands'].append(dict(command=command,cwd=str(EDITION),status=status,exit_code=code,
        cpu_seconds=after.ru_utime+after.ru_stime-prior.ru_utime-prior.ru_stime,wall_seconds=time.monotonic()-wall,
        log=f'check_{i}.log'))
    (OUT/'run.json').write_text(json.dumps(result,indent=2)+'\n')
    if code!=0:
        result['status']='failure';break
else:
    result['status']='pass'
final=resource.getrusage(resource.RUSAGE_CHILDREN)
result['child_cpu_seconds']=final.ru_utime+final.ru_stime-baseline.ru_utime-baseline.ru_stime
result['parent_cpu_seconds']=time.process_time()-start
result['peak_child_rss_bytes']=final.ru_maxrss*1024
result['environment']={k:environment[k] for k in ('PYTHONPATH','PYTHONDONTWRITEBYTECODE','TMPDIR','H4_LAW_TEST_SCRATCH','H4_VALIDATION_TEST_SCRATCH','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')}
(OUT/'run.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
