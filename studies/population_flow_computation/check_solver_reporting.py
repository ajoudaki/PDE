"""Exercise corrected reporting and checkpoint guards, with zero solver steps."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np

STUDY = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--checkpoint', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
HERE = args.output.resolve()
assert HERE.is_relative_to((STUDY.parents[1]/'data/generated/population_flow_computation').resolve())
HERE.mkdir(parents=True, exist_ok=False)
spec = importlib.util.spec_from_file_location('directional_solver', STUDY/'directional_solver.py')
solver_module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = solver_module
spec.loader.exec_module(solver_module)
spec = importlib.util.spec_from_file_location('audit_run_validation', STUDY/'run_validation.py')
driver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(driver)
result = {'training_trajectories':0}
checkpoint = args.checkpoint
with np.load(checkpoint, allow_pickle=False) as archive:
    arrays = {name:archive[name].copy() for name in archive.files}
metadata = json.loads(str(arrays['metadata']))
for mutation in ('missing','extra'):
    modified = json.loads(json.dumps(metadata))
    if mutation == 'missing':
        del modified['rng_state']['minus_probe']
    else:
        modified['rng_state']['extra'] = modified['rng_state']['minus_probe']
    arrays['metadata'] = np.asarray(json.dumps(modified,sort_keys=True))
    target = HERE/('malformed_'+mutation+'.npz')
    np.savez(target,**arrays)
    try:
        solver_module.DirectionalSolver.load(target)
    except ValueError as error:
        assert str(error) == 'checkpoint must contain every random stream exactly once'
        result[mutation+'_rng_rejected'] = str(error)
    else:
        raise AssertionError('malformed RNG set accepted')
restored = solver_module.DirectionalSolver.load(checkpoint)
assert restored.rng_state() == metadata['rng_state']
result['intact_rng_states_preserved'] = True
result['streaming_hash_matches'] = driver.digest(checkpoint) == hashlib.sha256(checkpoint.read_bytes()).hexdigest()
assert result['streaming_hash_matches']
previous_argv = sys.argv
previous_clock = driver.time.perf_counter
ticks = iter((0.,541.))
skip_dir = HERE/'driver_skip_check'
try:
    sys.argv = ['run_validation.py','--output',str(skip_dir)]
    driver.time.perf_counter = lambda: next(ticks)
    status = driver.main()
finally:
    sys.argv = previous_argv
    driver.time.perf_counter = previous_clock
outcomes = json.loads((skip_dir/'outcomes.json').read_text())
assert status == 1
assert outcomes == [{'name':'short_reference','status':'not_run_wall_budget'}]
result['wall_budget_skip_persisted'] = True
result['source_hashes'] = {name:hashlib.sha256((STUDY/name).read_bytes()).hexdigest()
                            for name in ('directional_solver.py','run_validation.py')}
(HERE/'reporting_fix_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
