import os, sys, json, time, resource, subprocess, hashlib
from pathlib import Path

ROOT=Path('/home/amir/Codes/PDE')
HERE=Path(__file__).resolve().parent
ED=ROOT/'data/generated/observable_hierarchy/H4_candidate_v1'
env=dict(os.environ)
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    env[key]='1'
env.update(PYTHONPATH=str(ED/'code'),PYTHONDONTWRITEBYTECODE='1',TMPDIR=str(HERE/'tmp'))
(HERE/'tmp').mkdir(exist_ok=True)
for key in ('H4_LAW_TEST_SCRATCH','H4_VALIDATION_TEST_SCRATCH'):
    env.pop(key,None)
suite=[sys.executable,'-B','-m','unittest','discover','-s','code/tests','-p','test_observable*.py','-v']
jobs=[('recipe_unconfigured',suite,dict(env),120,180)]
env.update(H4_LAW_TEST_SCRATCH=str(HERE/'tmp'),H4_VALIDATION_TEST_SCRATCH=str(HERE/'tmp'))
jobs.append(('suite_configured',suite,dict(env),120,180))
jobs.append(('reference_certificate',[sys.executable,'-B',str(ROOT/'data/generated/observable_hierarchy/H4_full_tests_v1/reference_certificate.py')],dict(env),120,180))
if len(sys.argv)>1 and sys.argv[1]=='archive':
    jobs=[('archive_audit',[sys.executable,'-B',str(HERE/'archive_audit.py')],dict(env),180,240)]
records=[]
for name,command,environment,cpu_limit,wall_limit in jobs:
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(cpu_limit,cpu_limit))
        resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    wall=time.monotonic()
    with (HERE/(name+'.log')).open('x') as log:
        try:
            result=subprocess.run(command,cwd=ED,env=environment,stdout=log,stderr=subprocess.STDOUT,timeout=wall_limit,preexec_fn=limits)
            code=result.returncode
        except subprocess.TimeoutExpired:
            code='wall_timeout'
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    record=dict(name=name,command=command,cwd=str(ED),environment={k:environment.get(k) for k in ('PYTHONPATH','PYTHONDONTWRITEBYTECODE','TMPDIR','H4_LAW_TEST_SCRATCH','H4_VALIDATION_TEST_SCRATCH','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')},exit_code=code,cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,wall_seconds=time.monotonic()-wall,peak_child_rss_bytes=after.ru_maxrss*1024,log_sha256=hashlib.sha256((HERE/(name+'.log')).read_bytes()).hexdigest())
    records.append(record)
    print(json.dumps(record),flush=True)
    (HERE/('archive_execution.json' if len(sys.argv)>1 else 'test_execution.json')).write_text(json.dumps(records,indent=2)+'\n')
    if not isinstance(code,int) or code<0:
        break
