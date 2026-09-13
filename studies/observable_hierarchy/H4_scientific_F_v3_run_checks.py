"""Review F: bounded deterministic supplied tests, no research runs."""
from pathlib import Path
import os,resource,subprocess,sys,json,time
ROOT=Path('/home/amir/Codes/PDE'); ED=ROOT/'data/generated/observable_hierarchy/H4_candidate_v3'; OUT=ROOT/'data/generated/observable_hierarchy/H4_scientific_F_v3'
resource.setrlimit(resource.RLIMIT_AS,(4*2**30,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(300,)*2)
env=dict(os.environ,PYTHONPATH=str(ED/'code'),PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',H4_LAW_TEST_SCRATCH=str(OUT),H4_VALIDATION_TEST_SCRATCH=str(OUT),TMPDIR=str(OUT))
cmd=[sys.executable,'-B','-m','unittest','discover','-s',str(ED/'code/tests'),'-p','test_observable*.py','-v']
before=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.monotonic()
with (OUT/'supplied_tests.log').open('x') as f:
 r=subprocess.run(cmd,env=env,cwd=ED,stdout=f,stderr=subprocess.STDOUT,timeout=180)
after=resource.getrusage(resource.RUSAGE_CHILDREN)
record=dict(command=cmd,environment={k:env[k] for k in ['PYTHONPATH','PYTHONDONTWRITEBYTECODE','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','TMPDIR']},returncode=r.returncode,cpu_seconds=(after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime),wall_seconds=time.monotonic()-start,peak_rss_bytes=after.ru_maxrss*1024)
(OUT/'supplied_tests_record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
