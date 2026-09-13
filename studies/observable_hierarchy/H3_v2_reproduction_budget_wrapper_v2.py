import argparse,json,os,resource,subprocess,time,sys
from pathlib import Path
import psutil
p=argparse.ArgumentParser();p.add_argument('--name',required=True);p.add_argument('--cpu',type=float,default=0);p.add_argument('--memory',type=int,default=0);p.add_argument('command',nargs=argparse.REMAINDER);a=p.parse_args()
scratch=Path(__file__).resolve().parent
env=dict(os.environ);env.update({k:'1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')});env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=str(Path.cwd()/'code'),H2_TEST_SCRATCH=str(scratch/'closure_test_scratch'),TMPDIR=str(scratch/'temporary'),OMP_DYNAMIC='FALSE',MKL_DYNAMIC='FALSE');env.pop('H2_PROTOTYPE_MODULE',None)
Path(env['TMPDIR']).mkdir(exist_ok=True)
record=dict(name=a.name,command=a.command,cwd=str(Path.cwd()),cpu_budget=a.cpu,memory_limit=a.memory,environment={k:env[k] for k in ('PYTHONPATH','TMPDIR','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','H2_TEST_SCRATCH')})
(scratch/(a.name+'_command.json')).write_text(json.dumps(record,indent=2)+'\n')
def limits():
 if a.memory:resource.setrlimit(resource.RLIMIT_AS,(a.memory,a.memory))
 if a.cpu:resource.setrlimit(resource.RLIMIT_CPU,(int(a.cpu),int(a.cpu)))
started=time.monotonic();seen={};peak=0;stop=None
with (scratch/(a.name+'.log')).open('x') as log:
 child=subprocess.Popen(a.command,env=env,stdout=log,stderr=subprocess.STDOUT,preexec_fn=limits,start_new_session=True)
 while child.poll() is None:
  try:
   proc=psutil.Process(child.pid)
   for item in [proc]+proc.children(recursive=True):
    try:
     u=item.cpu_times();seen[item.pid]=max(seen.get(item.pid,0),u.user+u.system);peak=max(peak,item.memory_info().rss)
    except (psutil.NoSuchProcess,psutil.ZombieProcess):pass
  except (psutil.NoSuchProcess,psutil.ZombieProcess):pass
  if a.cpu and sum(seen.values())>=a.cpu:
   stop='aggregate_cpu_budget';os.killpg(child.pid,9);break
  time.sleep(.05)
 child.wait()
u=resource.getrusage(resource.RUSAGE_CHILDREN);record.update(exit_code=child.returncode,stopped=stop,wall_seconds=time.monotonic()-started,reaped_cpu_seconds=u.ru_utime+u.ru_stime,sampled_tree_cpu_seconds=sum(seen.values()),peak_sampled_rss=peak,peak_os_rss_bytes=u.ru_maxrss*1024)
(scratch/(a.name+'_result.json')).write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record));sys.exit(child.returncode if child.returncode>=0 else 128-child.returncode)
