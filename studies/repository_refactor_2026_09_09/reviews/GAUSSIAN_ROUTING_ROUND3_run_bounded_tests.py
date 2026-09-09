"""Only explicitly inspected migration cases; no discovery or science suite."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path('/home/amir/Codes/PDE')
OUT = Path(__file__).parent
TMP = OUT / 'test-tmp'
TMP.mkdir(exist_ok=True)
HISTORY = ROOT / 'data/historical/studies'
inputs = [
    HISTORY / 'mfp_cubic_compiler/two_input_plus_gaussian_program/results_symbolic_order5.json',
    HISTORY / 'mfp_cubic_compiler/two_input_plus_gaussian_program/results_order3.json',
    HISTORY / 'mfp_cubic_compiler/depth2_gaussian_program/results_order9.json',
    HISTORY / 'stieltjes_resolution/canonical_hidden_high_order/PRODUCTION_HIDDEN_RESULT.json',
    HISTORY / 'stieltjes_resolution/canonical_hidden_high_order/INDEPENDENT_HIDDEN_RESULT.json',
]

def hashes():
    return {str(p): hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None for p in inputs}

before = hashes()
(OUT / 'historical-before.json').write_text(json.dumps(before, indent=2) + '\n')
names = [
    'studies.mfp_gaussian_calculus.test_migration_paths',
    'studies.mfp_gaussian_calculus.test_migration_retired_interfaces.RetiredInterfaceTests',
    'studies.mfp_gaussian_calculus.test_migration_retired_interfaces.FrozenComparisonInputTests.test_historical_paths_and_both_retained_map_schemas',
    'studies.mfp_gaussian_calculus.test_migration_retired_interfaces.FrozenComparisonInputTests.test_missing_or_malformed_retained_inputs_do_not_fall_back',
    'studies.mfp_linear_growth_uniform_counterexample.test_migration_paths',
    'studies.mfp_cubic_compiler.two_input_plus_gaussian_program.test_migration_paths.CubicInputPathsTests.test_three_retained_input_hashes_are_exact',
    'studies.stieltjes_resolution.canonical_hidden_high_order.test_migration_paths',
]
environment = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', TMPDIR=str(TMP))
records = []
for index, name in enumerate(names):
    command = [sys.executable, '-B', '-m', 'unittest', '-v', name]
    result = subprocess.run(command, cwd=ROOT, env=environment, text=True,
                            capture_output=True, timeout=45)
    log = OUT / f'bounded-test-{index+1}.log'
    log.write_text(result.stdout + result.stderr)
    records.append({'name': name, 'command': command, 'exit_code': result.returncode, 'log': str(log)})
    print(name, result.returncode, flush=True)
    print(result.stderr[-700:], flush=True)
after = hashes()
(OUT / 'historical-after.json').write_text(json.dumps(after, indent=2) + '\n')
(OUT / 'bounded-tests.json').write_text(json.dumps(records, indent=2) + '\n')
(OUT / 'dependencies.json').write_text(json.dumps({
    n: importlib.util.find_spec(n) is not None
    for n in ('numpy', 'sympy', 'mpmath', 'scipy', 'torch', 'pytest')
}, indent=2) + '\n')
assert before == after, 'historical inputs changed'
