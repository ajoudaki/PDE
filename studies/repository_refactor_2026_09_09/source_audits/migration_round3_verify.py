"""Bounded selected checks, one process per suite, with private temporary files."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path('/home/amir/Codes/PDE')
PRIVATE = Path(__file__).resolve().parent
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
           OMP_NUM_THREADS='1', MKL_NUM_THREADS='1', NUMEXPR_NUM_THREADS='1',
           VECLIB_MAXIMUM_THREADS='1', BLIS_NUM_THREADS='1', TMPDIR=str(PRIVATE))
records = []

def run(name, command, count, kind, pythonpath=''):
    start = time.monotonic()
    env = dict(ENV, PYTHONPATH=pythonpath)
    try:
        result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True, timeout=45)
        record = dict(name=name, kind=kind, command=command, pythonpath=pythonpath,
                      returncode=result.returncode, stdout=result.stdout, stderr=result.stderr,
                      expected_checks=count, seconds=time.monotonic()-start)
        match = re.search(r'Ran (\d+) tests?', result.stderr)
        record['observed_checks'] = int(match.group(1)) if match else count
    except subprocess.TimeoutExpired as exc:
        record = dict(name=name, kind=kind, command=command, returncode=124, expected_checks=count, error=str(exc))
    records.append(record)
    (PRIVATE/'verification.json').write_text(json.dumps(records, indent=2)+'\n')
    print(name, record['returncode'], flush=True)

for module, count in [
    ('studies.resnet_generalization.tests.test_migration_paths', 7),
    ('studies.mfp_cubic_compiler.two_input_plus_gaussian_program.test_migration_paths', 2),
    ('studies.stieltjes_finite_width.test_migration_paths', 5),
    ('studies.mfp_gaussian_calculus.test_migration_paths', 9),
    ('studies.stieltjes_hybrid_campaign.breadth_panel.test_migration_paths', 9)]:
    run(module, [sys.executable, '-B', '-m', 'unittest', module, '-v'], count, 'new regression')

prefix = 'studies/stieltjes_hybrid_campaign/breadth_panel/'
legacy = [prefix+'fp64_successor/'+f for f in ('watchdog_launcher.py', 'gpu_preflight.py',
          'run_local_qualification.py', 'adjudicate_local_qualification.py')]
legacy += [prefix+f'successive_n{n}/run_block.py' for n in (4096, 8192)]
legacy += ['studies/mfp_gaussian_calculus/depth_order5/primary/freeze_primary.py',
           'studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/postprocess_h3_curvature_extension.py']
for path in legacy:
    run(path, [sys.executable, '-B', str(PRIVATE/'guard_entrypoint.py'), path], 1, 'guarded CLI')

# The previously inspected nine bounded commands, never general repository discovery.
prior = json.loads(Path('/tmp/flat-study-path-repair-OE9KpPVL/baseline-results.json').read_text())
for item in prior:
    command = item['command']
    if item['name'] == 'operator_core':
        # Main owns this directory and may add unrelated test modules.
        command = [sys.executable, '-B', '-m', 'unittest', 'test_dense_reference', 'test_operator_galerkin', '-v']
        pythonpath = item['pythonpath']+':'+str(ROOT/'studies/resnet_operator_core/tests')
    else:
        pythonpath = item['pythonpath']
    run(item['name'], command, item['expected_checks'], 'bounded baseline', pythonpath)

failed = [r['name'] for r in records if r['returncode'] != 0]
print('FAILED', failed)
for kind in ('new regression', 'guarded CLI', 'bounded baseline'):
    print(kind, sum(r.get('observed_checks', 0) for r in records if r['kind'] == kind and r['returncode'] == 0))
raise SystemExit(bool(failed))
