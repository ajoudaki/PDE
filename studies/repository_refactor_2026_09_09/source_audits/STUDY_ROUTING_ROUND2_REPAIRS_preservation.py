"""Compare to captured pre-edit bytes, never Git history or scientific outputs."""
import ast
import hashlib
import json
from pathlib import Path

from snapshot import ROOT, OUT, capture

def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()

def normalized(value):
    if isinstance(value, list):
        value = ast.Module(body=value, type_ignores=[])
    return ast.dump(value, include_attributes=False)

def functions(text):
    return {node.name: node for node in ast.parse(text).body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}

before = json.loads((OUT/'baseline.json').read_text())
before_hashes = json.loads((OUT/'hashes.before.json').read_text())
after_hashes, after = capture()
changed = {path: dict(before=before_hashes.get(path), after=value)
           for path, value in after_hashes.items() if value != before_hashes.get(path)}
unchanged_defs, changed_defs, added_defs = {}, {}, {}
for path, old in before.items():
    if not path.endswith('.py'):
        continue
    prior, current = functions(old), functions(after[path])
    unchanged_defs[path] = {name: digest(normalized(node)) for name, node in prior.items()
                            if name in current and normalized(node) == normalized(current[name])}
    changed_defs[path] = [name for name in prior if name not in unchanged_defs[path]]
    added_defs[path] = sorted(set(current)-set(prior))

checks = {}
def check(label, left, right):
    if not isinstance(left, str):
        left, right = normalized(left), normalized(right)
    record = dict(before_sha256=digest(left), after_sha256=digest(right), equal=left == right)
    checks[label] = record
    assert record['equal'], label

def function_pair(relative, name):
    path = 'studies/'+relative
    return functions(before[path])[name], functions(after[path])[name]

def prefix_before_assignment(body, name):
    return body[:next(i for i, n in enumerate(body) if isinstance(n, ast.Assign)
                     and any(isinstance(t, ast.Name) and t.id == name for t in n.targets))]

for filename in ('run_pde.py', 'run_exact_reference.py'):
    old, new = function_pair('resnet_generalization/'+filename, 'run')
    check(filename+': complete pre-publication calculation/configuration prefix',
          prefix_before_assignment(old.body, 'output_dir'), prefix_before_assignment(new.body, 'output_dir'))
    calls = lambda node: [n for n in ast.walk(node) if isinstance(n, ast.Call)
                           and ast.unparse(n.func) == 'np.savez_compressed']
    check(filename+': complete NPZ payload call', calls(old), calls(new))

for name in ('plot_curves', 'plot_aggregate', 'plot_transitions'):
    old, new = function_pair('stieltjes_hybrid_campaign/breadth_panel/successive_n4096/analyze.py', name)
    check('hybrid '+name+': complete pre-publication plotting body',
          prefix_before_assignment(old.body, 'temporary'), prefix_before_assignment(new.body, 'path'))

stage = 'stieltjes_hybrid_campaign/width_ladder/euler_fp32/run_stage_v_point.py'
for name in ('configure_ieee_fp32', 'validate_lock', 'validate_unlock', 'parse_device',
             'validate_predecessor', 'environment'):
    check('Stage V '+name+': entire definition', *function_pair(stage, name))
old, new = function_pair(stage, 'main')
calls = lambda node: [n for n in ast.walk(node) if isinstance(n, ast.Call)
                       and ast.unparse(n.func) in ('run_point', 'np.savez_compressed')]
check('Stage V: complete run_point and arrays payload calls', calls(old), calls(new))
base = lambda node: next(n.value for n in node.body if isinstance(n, ast.Assign)
                         and any(isinstance(t, ast.Name) and t.id == 'base' for t in n.targets))
check('Stage V: complete manifest base payload', base(old), base(new))
handlers = lambda node: [n for n in ast.walk(node) if isinstance(n, ast.ExceptHandler)]
check('Stage V: entire scientific failure handler', handlers(old), handlers(new))
old, new = function_pair(stage, 'finalize_timeout')
status = lambda node: next(n for n in node.body if isinstance(n, ast.If)
                           and ast.unparse(n.test) == "manifest.get('status') == 'running'")
check('Stage V: unchanged timeout status/telemetry payload', status(old), status(new))
old, new = function_pair(stage, 'reserve_attempt')
new.body = [n for n in new.body if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)
            and ast.unparse(n.value.func) in ('checked_point_dir', 'PATHS.require_output'))]
check('Stage V: historical/current one-attempt logic after removing only added path guards', old, new)

for relative in ('resnet_generalization/analyze_generalization.py',
                 'stieltjes_hybrid_campaign/breadth_panel/successive_n4096/analyze.py',
                 'stieltjes_hybrid_campaign/breadth_panel/successive_n8192/compare_with_n4096.py'):
    name = 'run_analysis' if relative.startswith('resnet') else 'main'
    check(relative+': entire '+name, *function_pair(relative, name))

json_unchanged = {p: value for p, value in before_hashes.items() if p.endswith('.json')}
assert all(after_hashes[p] == value for p, value in json_unchanged.items())
for path, old in before.items():
    if path.endswith('.py'):
        strings = lambda text: sorted(n.value for n in ast.walk(ast.parse(text)) if isinstance(n, ast.Constant)
                                      and isinstance(n.value, str) and len(n.value) == 64
                                      and all(c in '0123456789abcdef' for c in n.value))
        assert strings(old) == strings(after[path]), 'changed hash literal: '+path
for path in after:
    if path.endswith('.py'):
        ast.parse(after[path], filename=path)
result = dict(changed_paths=changed, compared_json_files=json_unchanged,
              unchanged_top_level_definitions=unchanged_defs,
              changed_top_level_definitions={p: names for p, names in changed_defs.items() if names},
              added_top_level_definitions={p: names for p, names in added_defs.items() if names},
              focused_preservation_checks=checks,
              all_existing_64_hex_python_literals_unchanged=True,
              limits='AST identity is not a scientific correctness or numerical reproducibility test.')
(OUT/'hashes.final.json').write_text(json.dumps(after_hashes, indent=2, sort_keys=True)+'\n')
(OUT/'preservation.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
print(json.dumps(dict(changed_paths=len(changed), final_inputs=len(after_hashes),
                      json_unchanged=len(json_unchanged),
                      unchanged_top_level_definitions=sum(map(len, unchanged_defs.values())),
                      focused_checks=len(checks), changed_definitions=result['changed_top_level_definitions']), indent=2))
