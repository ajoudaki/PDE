"""Review-owned serial bounded deterministic check launcher."""
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

ROOT = Path('/home/amir/Codes/PDE')
OUT = ROOT/'data/generated/observable_hierarchy/H4_scientific_A_v1'
EDITION = ROOT/'data/generated/observable_hierarchy/H4_candidate_v1'
ledger = OUT/'checks.json'
entries = json.loads(ledger.read_text()) if ledger.exists() else []
charged = sum(e['cpu_seconds'] for e in entries)
remaining = max(0, math.floor(590-charged))
if remaining < 1:
    raise RuntimeError('Review CPU budget exhausted')
scratch = OUT/'scratch'
scratch.mkdir(exist_ok=True)
env = dict(os.environ)
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    env[key] = '1'
env.update(PYTHONPATH=str(EDITION/'code'), PYTHONDONTWRITEBYTECODE='1',
           TMPDIR=str(scratch), H4_LAW_TEST_SCRATCH=str(scratch),
           H4_VALIDATION_TEST_SCRATCH=str(scratch), OMP_DYNAMIC='FALSE', MKL_DYNAMIC='FALSE')
def limits():
    resource.setrlimit(resource.RLIMIT_AS, (4*2**30,)*2)
    resource.setrlimit(resource.RLIMIT_CPU, (remaining,)*2)
name, command = sys.argv[1], sys.argv[2:]
start = time.monotonic()
before = resource.getrusage(resource.RUSAGE_CHILDREN)
with (OUT/(name+'.log')).open('x') as log:
    try:
        result = subprocess.run(command, cwd=EDITION, env=env, stdout=log,
                                stderr=subprocess.STDOUT, timeout=remaining+30, preexec_fn=limits)
        status, code = 'complete', result.returncode
    except subprocess.TimeoutExpired:
        status, code = 'wall_limit', None
after = resource.getrusage(resource.RUSAGE_CHILDREN)
entry = dict(name=name, command=command, cwd=str(EDITION), status=status, exit_code=code,
             cpu_seconds=(after.ru_utime+after.ru_stime)-(before.ru_utime+before.ru_stime),
             wall_seconds=time.monotonic()-start, peak_child_rss_bytes=after.ru_maxrss*1024,
             address_space_limit_bytes=4*2**30, cpu_limit_seconds=remaining,
             environment={k:env[k] for k in ('PYTHONPATH','PYTHONDONTWRITEBYTECODE','TMPDIR','H4_LAW_TEST_SCRATCH','H4_VALIDATION_TEST_SCRATCH','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')},
             log_sha256=hashlib.sha256((OUT/(name+'.log')).read_bytes()).hexdigest())
entries.append(entry)
ledger.write_text(json.dumps(entries, indent=2)+'\n')
print(json.dumps(entry))
sys.exit(code if code is not None else 1)
