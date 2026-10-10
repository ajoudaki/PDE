"""Exercise the proposed standalone API and guide without study imports."""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
import sys
import time

study = Path(__file__).resolve().parent
run = study.parents[1]/'data/generated'/study.name/sys.argv[1]
edition = run/'edition'
logs = run/'code_validation'
logs.mkdir(exist_ok=False)
env = dict(os.environ, PYTHONPATH=str(edition/'code'), PYTHONDONTWRITEBYTECODE='1',
           OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
commands = [
    ('imports', [sys.executable,'-B','-c',
      "import pathlib,pde,pde.mfp_compiler,pde.mfp_expr,pde.mfp_finite; "
      "assert pathlib.Path(pde.__file__).resolve().is_relative_to(pathlib.Path.cwd()/'code'); "
      "print(pde.__file__)"]),
    ('boundary', [sys.executable,'-B','code/tools/check_library.py']),
    ('tests', [sys.executable,'-B','-m','unittest','discover','-s','code/tests','-p','test_mfp_*.py','-v']),
    ('calculus', [sys.executable,'-B','code/scripts/example_mfp_calculus.py']),
    ('calculus_json', [sys.executable,'-B','code/scripts/example_mfp_calculus.py','--json']),
    ('mlp', [sys.executable,'-B','code/scripts/example_mfp_mlp_derivative.py']),
    ('mlp_cubic', [sys.executable,'-B','code/scripts/example_mfp_mlp_derivative.py','--activation','cubic','--json']),
    ('kernel_identity', [sys.executable,'-B','code/scripts/example_mfp_kernel_jets.py','--activation','identity']),
    ('kernel_all', [sys.executable,'-B','code/scripts/example_mfp_kernel_jets.py',
                    '--activation','all','--output-dir','data/established/mfp_kernel_jets_01']),
]
guide = (edition/'code/MFP_CALCULUS.md').read_text()
for i, block in enumerate(re.findall(r'^```python\n(.*?)^```', guide, re.M|re.S),1):
    commands.append((f'guide_{i}',[sys.executable,'-B','-c',block]))
results = []
for name, command in commands:
    start = time.monotonic()
    with (logs/f'{name}.log').open('w') as output:
        result = subprocess.run(command,cwd=edition,env=env,stdout=output,
                                stderr=subprocess.STDOUT,timeout=180)
    results.append({'name':name,'command':command,'exit_code':result.returncode,
                    'elapsed_seconds':time.monotonic()-start})
    print(name, result.returncode, flush=True)
    if result.returncode:
        print((logs/f'{name}.log').read_text()[-7000:],flush=True)
        break
out = edition/'data/established/mfp_kernel_jets_01'
if out.exists():
    metadata = json.loads((out/'manifest.json').read_text())
    for name, expected in metadata['output_sha256'].items():
        assert hashlib.sha256((out/name).read_bytes()).hexdigest() == expected
    for name in ('symbolic','identity','quadratic'):
        json.loads((out/f'{name}.json').read_text())
report = {'cwd':str(edition),'commands':results,
          'environment':{key:env[key] for key in ('PYTHONPATH','PYTHONDONTWRITEBYTECODE',
                            'OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')}}
(logs/'manifest.json').write_text(json.dumps(report,indent=2)+'\n')
raise SystemExit(any(r['exit_code'] for r in results))
