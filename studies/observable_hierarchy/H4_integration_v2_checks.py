"""Fresh frozen-edition integration checks; no research trajectories."""
from pathlib import Path
import hashlib, json, os, resource, shutil, subprocess, sys, time

ROOT = Path('/home/amir/Codes/PDE')
EDITION = ROOT/'data/generated/observable_hierarchy/H4_candidate_v2b'
SCRATCH = ROOT/'data/generated/observable_hierarchy/H4_integration_v2'
VIEW = SCRATCH/'standalone'
VIEW.mkdir(exist_ok=True)
for name in ('code', 'docs'):
    target = VIEW/name
    if not target.exists(): target.symlink_to(EDITION/name, target_is_directory=True)
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONPATH=str(VIEW/'code'))
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    ENV[key] = '1'
COMMANDS=[]

def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(580,580))
    resource.setrlimit(resource.RLIMIT_AS,(4*2**30,4*2**30))

def run(name, command, cwd=VIEW):
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    start=time.monotonic()
    with (SCRATCH/(name+'.log')).open('x') as log:
        result=subprocess.run(command,cwd=cwd,env=ENV,stdout=log,stderr=subprocess.STDOUT,preexec_fn=limits,timeout=590)
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    entry=dict(name=name,command=command,cwd=str(cwd),exit_code=result.returncode,wall_seconds=time.monotonic()-start,
               cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,maximum_child_rss_bytes=after.ru_maxrss*1024)
    COMMANDS.append(entry)
    (SCRATCH/'commands.json').write_text(json.dumps(COMMANDS,indent=2)+'\n')
    print(json.dumps(entry),flush=True)
    if sum(x['cpu_seconds'] for x in COMMANDS)>600: raise RuntimeError('cumulative CPU allowance exhausted')

guide=(EDITION/'code/README.md').read_text()
new=guide[guide.index('## Observable computation through physical time 40'):]
snippet=new.split('```python\n')[1].split('```')[0]
(SCRATCH/'public_example.py').write_text(snippet)
recipe=new.split('```text\n')[1].split('```')[0].splitlines()
assert recipe[0]=='mkdir -p data/established'
assert 'unittest discover' in recipe[2]
run('literal_test_recipe',['bash','-c','\n'.join(recipe[:3])])
run('public_law_example',[sys.executable,'-B',str(SCRATCH/'public_example.py')])
for name in ('run_observable_validation','validate_observable_horizon','analyze_observable_horizon'):
    run(name+'_help',[sys.executable,'-B','code/scripts/'+name+'.py','--help'])
run('recorded_array_analysis',[sys.executable,'-B','code/scripts/analyze_observable_horizon.py','--plan','code/validation/observable_horizon_plan.json',
    '--runs',str(ROOT/'data/generated/observable_hierarchy/H4_author_runs_v1'),'--output',str(SCRATCH/'analysis')])
