"""Read-only negative gates; never execute any scientific or seal writer."""
import ast
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

from run_tests import ROOT, OUT, guard

sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT))
os.chdir(OUT)
sys.addaudithook(guard)
results = {}

def refuses(label, function, expected):
    try:
        function()
    except RuntimeError as exc:
        assert expected in str(exc), str(exc)
        results[label] = str(exc)
    else:
        raise AssertionError('gate unexpectedly passed: '+label)

from studies.resnet_generalization import verify_study
refuses('generalization_source', lambda: verify_study.verify_source(False), 'frozen source mismatch')
for filename, expected in (('seal_dense_postfreeze_amendment.py', 'frozen run_grid.py hash mismatch'),
                           ('analyze_postfreeze_amendment.py', 'frozen analyzer hash mismatch')):
    path = ROOT/'studies/resnet_generalization/protocol'/filename
    spec = importlib.util.spec_from_file_location('bounded_gate_'+path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Their first immutable source hash checks refuse; no sealer/analyzer is imported.
    refuses(filename, module.main, expected)

here = ROOT/'studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32'
source = here/'run_stage_v_point.py'
names = {'sha256', 'load_json', 'validate_lock', 'validate_unlock'}
nodes = [n for n in ast.parse(source.read_text()).body if isinstance(n, ast.FunctionDef) and n.name in names]
future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
env = dict(hashlib=hashlib, json=json, HERE=here, CONFIG=here/'configs/FROZEN_STAGE_V.json',
           LOCK=here/'FROZEN_STAGE_V_MANIFEST.json', UNLOCK=here/'STAGE_V_UNLOCK.json',
           RUN_ROOT=ROOT/'data/generated/stieltjes_hybrid_campaign/width_ladder/euler_fp32/runs/stage_v')
exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(source), 'exec'), env)
refuses('stage_v_source_lock', env['validate_lock'], 'locked source mismatch')
# Isolated unlock-validator call tests the generated-root binding, not a launch.
refuses('stage_v_generated_root_unlock', lambda: env['validate_unlock'](env['sha256'](env['LOCK'])),
        'unlock does not bind the fresh generated run root')
(OUT/'gates.json').write_text(json.dumps(results, indent=2, sort_keys=True)+'\n')
print(json.dumps(results, indent=2))
