"""Bounded checks of the approved live integration; no research campaign."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'data/generated/closure_endpoint_discrimination/promotion_20260916/live_integration'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--device', required=True)
    args = parser.parse_args()
    out = OUT/args.device.replace(':','_')
    out.mkdir(exist_ok=False)
    env = dict(os.environ, PYTHONPATH=str(ROOT/'code'), PYTHONDONTWRITEBYTECODE='1',
               OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1',
               CUBLAS_WORKSPACE_CONFIG=':4096:8', PDE_TEST_DEVICE=args.device,
               CIRCLE_TEST_DEVICE=args.device, CIRCLE_TEST_SCRATCH=str(out), TMPDIR=str(out))
    py = '/home/amir/miniconda3/bin/python'
    commands = []
    if args.device == 'cpu':
        commands += [('numpy_discovery', ['/usr/bin/python3','-B','-m','unittest','discover',
                      '-s','code/tests','-p','test_general_p1.py','-v']),
                     ('library_boundary',[py,'-B','code/tests/test_library_boundary.py']),
                     ('library_check',[py,'-B','code/tools/check_library.py']),
                     ('numpy_import',['/usr/bin/python3','-B','-c',
                      "import pde,sys; assert 'torch' not in sys.modules; print(pde.__file__)"])]
    for name in ['test_general_p1','test_observable_torch_circle']:
        commands.append((name,[py,'-B','code/tests/'+name+'.py']))
    report = dict(status='running',cwd=str(ROOT),device=args.device,
                  limits=dict(total_wall_seconds=600,subprocess_seconds=120,threads=1,
                              scope='affected deterministic integration tests only'),
                  environment={k:env[k] for k in ['PYTHONPATH','PYTHONDONTWRITEBYTECODE',
                    'OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
                    'CUBLAS_WORKSPACE_CONFIG','PDE_TEST_DEVICE','CIRCLE_TEST_DEVICE',
                    'CIRCLE_TEST_SCRATCH','TMPDIR']},commands=[])
    record = out/'validation.json'
    record.write_text(json.dumps(report,indent=2)+'\n')
    began=time.monotonic()
    try:
        for name, command in commands:
            remaining=600-(time.monotonic()-began)
            if remaining <= 0: raise TimeoutError('total check budget')
            tick=time.monotonic()
            result=subprocess.run(command,cwd=ROOT,env=env,capture_output=True,text=True,
                                  timeout=min(120,remaining))
            (out/(name+'.stdout')).write_text(result.stdout)
            (out/(name+'.stderr')).write_text(result.stderr)
            report['commands'].append(dict(name=name,command=command,exit_status=result.returncode,
                                            wall_seconds=time.monotonic()-tick))
            record.write_text(json.dumps(report,indent=2)+'\n')
            print(name+': '+str(result.returncode),flush=True)
            if result.returncode: raise RuntimeError(name+' failed; logs retained')
        report['status']='complete'
    except BaseException as error:
        report.update(status='failed',error=repr(error))
        raise
    finally:
        report['wall_seconds']=time.monotonic()-began
        report['outputs']={str(p.relative_to(out)):hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in sorted(out.iterdir()) if p.is_file() and p!=record}
        record.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    main()
