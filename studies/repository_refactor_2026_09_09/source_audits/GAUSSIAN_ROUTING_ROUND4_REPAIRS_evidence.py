import ast
import copy
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path('/home/amir/Codes/PDE/studies/mfp_gaussian_calculus')
PRIVATE = Path(__file__).parent
OWNED = [
    'depth_order5/independent/compare_symbolic_q0.py',
    'depth_order5/audit/compare_frozen.py',
    'depth_order5/audit/audit_symbolic_q0.py',
    'depth_order5/audit/run_normalized_sine_experiment.py',
    'depth_order5_observables/independent/run_sine_experiment.py',
    'depth_order5_scalar/multi_observable/audit/run_hostile_checks.py',
    'depth_order5/primary/run_lightweight_checks.py',
    'depth_order5/audit/run_checks.py',
]
TESTS = ['test_migration_sibling_consumers.py', 'test_migration_replay_helpers.py']
PROTECTED = [ROOT / 'study_paths.py', ROOT.parent / '_output_paths.py']

def snapshot():
    return {str(path): {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                       'source': path.read_text()}
            for path in [*(ROOT / p for p in OWNED + TESTS), *PROTECTED] if path.exists()}

def dump(nodes):
    return ast.dump(ast.Module(body=nodes, type_ignores=[]), include_attributes=False)

if __name__ == '__main__':
    mode = sys.argv[1]
    current = snapshot()
    (PRIVATE / (mode + '.json')).write_text(json.dumps(current, indent=2) + '\n')
    if mode == 'before':
        assert all(not (ROOT / name).exists() for name in TESTS)
        print('Recorded eight owned source files and two unchanged guards.')
    else:
        before = json.loads((PRIVATE / 'before.json').read_text())
        for path in PROTECTED:
            assert current[str(path)] == before[str(path)], str(path)
        checks = []
        for name in OWNED:
            old = ast.parse(before[str(ROOT / name)]['source'])
            new = ast.parse(current[str(ROOT / name)]['source'])
            old_functions = {n.name: n for n in old.body if isinstance(n, ast.FunctionDef)}
            new_functions = {n.name: n for n in new.body if isinstance(n, ast.FunctionDef)}
            if name in OWNED[:5]:
                original = copy.deepcopy(old_functions['main'].body)
                normalized = copy.deepcopy(new_functions['main'].body)
                normalized = [n for n in normalized if not (
                    isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)
                    and isinstance(n.value.func, ast.Name)
                    and n.value.func.id == 'guard_output_inputs')]
                def assignment(statement, target):
                    return (isinstance(statement, ast.Assign)
                            and len(statement.targets) == 1
                            and isinstance(statement.targets[0], ast.Name)
                            and statement.targets[0].id == target)
                if name == OWNED[0]:
                    timer = next(n for n in normalized if assignment(n, 'started'))
                    normalized.remove(timer)
                    normalized.insert(1, timer)
                elif name == OWNED[1]:
                    assert assignment(normalized[1], 'output')
                    normalized.pop(1)
                    normalized = [n for n in normalized if not assignment(n, 'declared_inputs')]
                elif name == OWNED[3]:
                    prediction = next(n for n in normalized if assignment(n, 'prediction_path'))
                    normalized.remove(prediction)
                    payload = next(n for n in normalized if assignment(n, 'prediction_payload'))
                    # Undo only the named-path extraction added for the preflight.
                    payload.value.args[0].func.value = prediction.value
                elif name == OWNED[4]:
                    prediction = next(n for n in normalized if assignment(n, 'prediction_path'))
                    normalized.remove(prediction)
                    position = next(i for i, n in enumerate(original) if assignment(n, 'prediction_path'))
                    normalized.insert(position, prediction)
                assert dump(original) == dump(normalized), name
                checks.append({'file': name, 'function': 'main', 'check': 'original body preserved except preflight and path/timer placement'})
            if name.endswith('run_hostile_checks.py'):
                start = next(i for i, n in enumerate(old.body) if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name) and n.target.id == 'checks')
                original_work = [n for n in old.body[start:] if not isinstance(n, ast.FunctionDef)]
                assert dump(original_work) == dump(new_functions['main'].body[1:])
                checks.append({'file': name, 'check': 'hostile executable block preserved', 'statements': len(original_work)})
            for function, node in old_functions.items():
                if function == 'main' and name in OWNED[:5]:
                    continue
                other = new_functions[function]
                if dump(node.body) != dump(other.body):
                    assert isinstance(other.body[0], ast.Raise), (name, function)
                    tail = other.body[1:]
                    # Replay mains may move their report import behind refusal.
                    if tail and isinstance(tail[0], ast.ImportFrom):
                        tail = tail[1:]
                    assert dump(node.body) == dump(tail), (name, function)
                    checks.append({'file': name, 'function': function, 'check': 'body preserved behind immediate refusal'})
                else:
                    checks.append({'file': name, 'function': function, 'check': 'body unchanged'})
        (PRIVATE / 'ast-preservation.json').write_text(json.dumps(checks, indent=2) + '\n')
        changes = [{'path': path, 'before_sha256': before.get(path, {}).get('sha256'), 'after_sha256': record['sha256']}
                   for path, record in current.items() if before.get(path) != record]
        assert {c['path'] for c in changes} == {str(ROOT / p) for p in OWNED + TESTS}
        (PRIVATE / 'changed-paths-hashes.json').write_text(json.dumps(changes, indent=2) + '\n')
        print(json.dumps({'changed_files': len(changes), 'preservation_checks': len(checks), 'shared_guards_unchanged': True}))
