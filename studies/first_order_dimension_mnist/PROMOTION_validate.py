"""Capture bounded standalone checks of the general-p1 assembled edition."""
import argparse
import hashlib
import json
import os
import re
import subprocess
import time
from pathlib import Path


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--edition',required=True,type=Path)
    parser.add_argument('--device',required=True)
    parser.add_argument('--python',required=True)
    parser.add_argument('--tests',action='store_true')
    args=parser.parse_args();edition=args.edition.resolve()
    output=edition/'data'/'established'/('validation_'+args.device.replace(':','_'))
    output.mkdir(parents=True,exist_ok=False)
    env=dict(os.environ,PYTHONPATH=str(edition/'code'),PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',
             OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',CUBLAS_WORKSPACE_CONFIG=':4096:8',PDE_TEST_DEVICE=args.device,TMPDIR=str(output))
    commands=[]
    if args.tests:commands.append(('tests',[args.python,'-B','code/tests/test_general_p1.py']))
    for suffix in ('a','b'):
        commands.append(('example_'+suffix,[args.python,'-B','code/scripts/example_general_p1.py','--output',str(output/suffix),'--device',args.device]))
    commands.append(('analysis',[args.python,'-B','code/scripts/analyze_general_p1.py','--run',str(output/'a'),'--repeat',str(output/'b'),'--output',str(output/'analysis.json')]))
    if args.device=='cpu':
        blocks=re.findall(r'```python\n(.*?)\n```',(edition/'code/GENERAL_P1.md').read_text(),re.S)
        commands.append(('guide_examples',[args.python,'-B','-c','\n'.join(blocks)]))
        commands.append(('numpy_only_import',[args.python,'-B','-c',"import pde,sys; assert 'torch' not in sys.modules; print('NumPy-only package import preserved')"]))
    records=[];start=time.monotonic()
    try:
        for name,cmd in commands:
            remaining=580-(time.monotonic()-start)
            if remaining<=0:raise RuntimeError('total wall budget exhausted')
            tick=time.monotonic()
            result=subprocess.run(cmd,cwd=edition,env=env,capture_output=True,text=True,timeout=min(120,remaining))
            (output/(name+'.stdout')).write_text(result.stdout);(output/(name+'.stderr')).write_text(result.stderr)
            records.append(dict(name=name,command=cmd,exit_status=result.returncode,wall_seconds=time.monotonic()-tick))
            print(name+': '+str(result.returncode),flush=True)
            if result.returncode:raise RuntimeError(name+' failed; inspect retained logs')
    finally:
        sources=[p for p in (edition/'code/pde').glob('*.py') if p.name in ('__init__.py','gaussian_moments.py','finite_network.py','observable_p1_initialization.py','observable_torch_p1.py','finite_torch.py','closure_comparison.py')]
        sources += [edition/'code/tests/test_general_p1.py',edition/'code/scripts/example_general_p1.py',edition/'code/scripts/analyze_general_p1.py',edition/'code/GENERAL_P1.md',edition/'docs/observable_p1.md']
        record=dict(device=args.device,cwd=str(edition),environment={k:env[k] for k in ('PYTHONPATH','PYTHONDONTWRITEBYTECODE','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','CUBLAS_WORKSPACE_CONFIG','PDE_TEST_DEVICE','TMPDIR')},
                    commands=records,total_wall_seconds=time.monotonic()-start,
                    source_sha256={str(p.relative_to(edition)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
                    complete=len(records)==len(commands) and all(x['exit_status']==0 for x in records))
        (output/'validation.json').write_text(json.dumps(record,indent=2)+'\n')

if __name__=='__main__':main()
