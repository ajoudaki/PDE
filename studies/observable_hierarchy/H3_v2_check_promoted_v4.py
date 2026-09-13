"""Check exact approved H3 live correspondence, tests, and published example.

Run with --output pointing to a fresh observable_hierarchy generated directory.
Budgets and scope are fixed in H3_v2_promotion_plan_v4.md. No new configurations.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
import time

import psutil

resource.setrlimit(resource.RLIMIT_CPU, (60, 600))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 4*1024**3))
root = Path(__file__).resolve().parents[2]
study = root/'studies/observable_hierarchy'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
output = args.output.resolve()
assert output.is_relative_to(root/'data/generated/observable_hierarchy')
output.mkdir(exist_ok=False)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = json.loads((study/'H3_v2_edition_v3_manifest.json').read_text())
mapping = json.loads((study/'H3_v2_promotion_mapping_v4.json').read_text())

def correspondence():
    checked = {}
    for name, expected in manifest['edition_hashes'].items():
        if name.startswith(('code/', 'docs/')):
            actual = sha(root/name)
            assert actual == expected, name
            checked[name] = actual
    assert len(checked) == 24
    for name, item in mapping['files'].items():
        assert checked[name] == item['proposed_sha256']
    section = (study/'H3_v2_edition_v3_section.md').read_text()
    chapter = (root/'docs/global_nonlinear.md').read_text()
    base = (root/'data/generated/observable_hierarchy/H3_v2_integration_inputs_v3/base_global_nonlinear.md').read_text()
    assert chapter.count(section) == 1
    assert chapter.replace(section+'\n', '', 1) == base
    target = 'global_nonlinear.md#c4710-finite-numerical-autonomous-observable-closure'
    assert ']('+target+')' in (root/'docs/README.md').read_text()
    return checked

entry = correspondence()
(output/'entry_hashes.json').write_text(json.dumps(entry, indent=2)+'\n')
env = dict(os.environ)
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'BLIS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    env[key] = '1'
env.update(PYTHONDONTWRITEBYTECODE='1', PYTHONPATH=str(root/'code'),
           H2_TEST_SCRATCH=str(output/'closure_test_scratch'),
           TMPDIR=str(output/'temporary'), OMP_DYNAMIC='FALSE', MKL_DYNAMIC='FALSE')
env.pop('H2_PROTOTYPE_MODULE', None)
Path(env['TMPDIR']).mkdir()

def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (240, 240))
    resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))

def run(name, command):
    specification = dict(command=command, cwd=str(root), cpu_seconds_limit=240,
                         wall_seconds_limit=280, address_space_bytes=4*1024**3,
                         environment={k:env[k] for k in ('PYTHONPATH', 'TMPDIR',
                             'H2_TEST_SCRATCH', 'OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS')})
    (output/(name+'_command.json')).write_text(json.dumps(specification, indent=2)+'\n')
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    started = time.monotonic()
    seen, stopped = {}, None
    with (output/(name+'.log')).open('x') as log:
        child = subprocess.Popen(command, cwd=root, env=env, stdout=log,
                                 stderr=subprocess.STDOUT, preexec_fn=limits,
                                 start_new_session=True)
        while child.poll() is None:
            try:
                parent = psutil.Process(child.pid)
                descendants = parent.children(recursive=True)
                for process in [parent]+descendants:
                    try:
                        u = process.cpu_times()
                        seen[process.pid] = max(seen.get(process.pid, 0), u.user+u.system)
                    except (psutil.NoSuchProcess, psutil.ZombieProcess):
                        pass
                if sum(seen.values()) >= 240 or time.monotonic()-started >= 280:
                    stopped = 'cpu_or_wall_budget'
                    for process in reversed(descendants+[parent]):
                        try:
                            process.kill()
                        except psutil.NoSuchProcess:
                            pass
                    break
            except psutil.NoSuchProcess:
                pass
            time.sleep(.02)
        child.wait()
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = dict(**specification, exit_code=child.returncode, stopped=stopped,
                  cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                  sampled_tree_cpu_seconds=sum(seen.values()),
                  wall_seconds=time.monotonic()-started,
                  cumulative_children_peak_rss_bytes=after.ru_maxrss*1024,
                  log_sha256=sha(output/(name+'.log')))
    (output/(name+'_result.json')).write_text(json.dumps(result, indent=2)+'\n')
    assert child.returncode == 0 and stopped is None, name
    return result

tests = run('tests', [sys.executable, '-B', '-m', 'unittest', 'discover',
                     '-s', 'code/tests', '-p', 'test_observable*.py', '-v'])
assert re.search(r'Ran 54 tests\b', (output/'tests.log').read_text())
guide_source = study/'H3_v2_reproduction_guide_example_v2.py'
guide = output/'guide_example.py'
guide.write_bytes(guide_source.read_bytes())
example = run('guide', [sys.executable, '-B', str(guide)])
observed = json.loads((output/'guide_example_checks.json').read_text())
assert observed['source'] == str(root/'code/pde/observable_solver.py')
assert observed['status'] == 'operational_pass'
assert all(all(values.values()) for values in observed['checks'].values())
exit_hashes = correspondence()
assert entry == exit_hashes
(output/'exit_hashes.json').write_text(json.dumps(exit_hashes, indent=2)+'\n')
result = dict(status='pass', live_files_matched=len(exit_hashes),
              approved_destinations=len(mapping['files']), tests_passed=54,
              guide_exact_restart=True, guide_source_sha256=sha(guide_source),
              checks={'tests':tests, 'guide':example},
              checker_sha256=sha(Path(__file__)),
              limits='Frozen installation checks; no new resolution or error certificate.')
(output/'result.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'checks'}, indent=2))
