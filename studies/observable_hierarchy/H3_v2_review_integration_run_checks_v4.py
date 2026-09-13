import json, os, resource, subprocess, sys, time
from pathlib import Path

scratch = Path(__file__).resolve().parent
edition = scratch.parent / 'H3_v2_edition_v3'
env = os.environ.copy()
env.update({key: '1' for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS',
    'MKL_NUM_THREADS', 'BLIS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')})
env.update(PYTHONDONTWRITEBYTECODE='1', PYTHONPATH=str(edition / 'code'),
           H2_TEST_SCRATCH=str(scratch / 'closure_test_scratch'), TMPDIR=str(scratch / 'temporary'))
env.pop('H2_PROTOTYPE_MODULE', None)
Path(env['TMPDIR']).mkdir(exist_ok=True)
command = [sys.executable, '-B', '-m', 'unittest', 'discover', '-s',
           str(edition / 'code/tests'), '-p', 'test_observable*.py', '-v']
def limits():
    resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (300, 300))
start = time.monotonic()
with (scratch / 'tests.log').open('x') as log:
    result = subprocess.run(command, cwd=scratch, env=env, stdout=log,
                            stderr=subprocess.STDOUT, preexec_fn=limits)
usage = resource.getrusage(resource.RUSAGE_CHILDREN)
record = dict(command=command, cwd=str(scratch), environment={key: env[key] for key in
              ('PYTHONPATH','PYTHONDONTWRITEBYTECODE','H2_TEST_SCRATCH','TMPDIR',
               'OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS',
               'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')},
              cpu_seconds=usage.ru_utime + usage.ru_stime,
              wall_seconds=time.monotonic() - start, peak_rss_bytes=usage.ru_maxrss * 1024,
              exit_code=result.returncode, cpu_limit=300, address_space_limit=4*1024**3)
(scratch / 'tests_result.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record))
sys.exit(result.returncode)
