"""Explicit inspected migration cases, excluding fit/seal/report payload cases."""
import importlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path('/home/amir/Codes/PDE')
OUT = Path(__file__).parent
TMP = OUT / 'test-tmp'
TMP.mkdir(exist_ok=True)
sys.path.insert(0, str(ROOT))
groups = {
    'focused': [
        'studies.causal_flow_peeling_calculus.test_migration_input_aliases',
        'studies.d3_arctan_closure_program.test_migration_input_aliases',
        'studies.mfp_gaussian_calculus.test_migration_input_aliases',
        'studies.stieltjes_resolution.canonical_hidden_high_order.test_migration_input_aliases',
        'studies.mfp_program_history.report.test_migration_paths',
    ],
    'existing': [
        'studies.mfp_gaussian_calculus.test_migration_retired_interfaces.RetiredInterfaceTests',
        'studies.mfp_gaussian_calculus.test_migration_retired_interfaces.FrozenComparisonInputTests.test_historical_paths_and_both_retained_map_schemas',
        'studies.mfp_gaussian_calculus.test_migration_retired_interfaces.FrozenComparisonInputTests.test_missing_or_malformed_retained_inputs_do_not_fall_back',
        'studies.stieltjes_resolution.canonical_hidden_high_order.test_migration_paths',
    ],
}
test_class = importlib.import_module('studies.mfp_gaussian_calculus.test_migration_paths').GaussianPathTests
excluded = {'test_selected_sine_fixture_to_separate_fresh_result', 'test_freeze_refuses_existing_seal_without_any_writes'}
groups['existing'] += [test_class.__module__ + '.GaussianPathTests.' + name
                       for name in unittest.defaultTestLoader.getTestCaseNames(test_class) if name not in excluded]
results = []
for group, names in groups.items():
    command = [sys.executable, '-B', '-m', 'unittest', '-v', *names]
    result = subprocess.run(command, cwd=ROOT, env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', TMPDIR=str(TMP)),
                            text=True, capture_output=True, timeout=60)
    log = OUT / f'tests-{group}.log'
    log.write_text(result.stdout + result.stderr)
    results.append({'group': group, 'command': command, 'exit_code': result.returncode, 'log': str(log)})
    print(result.stdout + result.stderr, flush=True)
(OUT / 'test-results.json').write_text(json.dumps(results, indent=2) + '\n')
(OUT / 'dependencies.json').write_text(json.dumps({name: importlib.util.find_spec(name) is not None
                                                for name in ('numpy', 'scipy', 'sympy', 'mpmath', 'torch', 'pytest')}, indent=2) + '\n')
sys.exit(any(result['exit_code'] != 0 for result in results))
