import hashlib, json, os, pathlib, resource, subprocess, sys, time
scratch=pathlib.Path(__file__).resolve().parent
edition=scratch.parent/'H3_v2_edition_v2'
env=dict(os.environ)
env.update({k:'1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')})
env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=str(edition/'code'),TMPDIR=str(scratch/'tmp'),H2_TEST_SCRATCH=str(scratch/'h2_tmp'),OMP_DYNAMIC='FALSE',MKL_DYNAMIC='FALSE')
env.pop('H2_PROTOTYPE_MODULE',None)
for p in (scratch/'tmp',scratch/'h2_tmp'):p.mkdir(exist_ok=True)
command=[sys.executable,'-B','-m','unittest','discover','-s','code/tests','-p','test_observable*.py','-v']
record={'command':command,'cwd':str(edition),'cpu_limit_seconds':240,'address_space_limit_bytes':4*1024**3,'environment':{k:env[k] for k in ('PYTHONPATH','TMPDIR','H2_TEST_SCRATCH','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')}}
(scratch/'tests_command.json').write_text(json.dumps(record,indent=2)+'\n')
def limits():
 resource.setrlimit(resource.RLIMIT_CPU,(240,240));resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.monotonic()
with (scratch/'tests.log').open('x') as log:
 p=subprocess.run(command,cwd=edition,env=env,stdout=log,stderr=subprocess.STDOUT,preexec_fn=limits,timeout=300)
r=resource.getrusage(resource.RUSAGE_CHILDREN)
record.update(exit_code=p.returncode,wall_seconds=time.monotonic()-start,cpu_seconds=r.ru_utime+r.ru_stime,peak_rss_bytes=r.ru_maxrss*1024,log_sha256=hashlib.sha256((scratch/'tests.log').read_bytes()).hexdigest())
(scratch/'tests_result.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record));print((scratch/'tests.log').read_text())
