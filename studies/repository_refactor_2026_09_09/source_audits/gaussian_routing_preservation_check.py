"""Verify only the permitted interface AST/text edits against private baseline."""
import ast
import copy
import hashlib
import json
from pathlib import Path

PRIVATE = Path('/tmp/pde-gaussian-routing-final.bJLzzv91')
ROOT = Path('/home/amir/Codes/PDE')
baseline = json.loads((PRIVATE/'implementation_before.json').read_text())
checks = []
for source in baseline['sources']:
    path = ROOT/source['path']
    original = source['text']
    assert hashlib.sha256(original.encode()).hexdigest() == source['sha256']
    current = path.read_text()
    old = ast.parse(original)
    new = ast.parse(current)
    expected_text = original
    if path.name == 'full_l2_paired_transition.py':
        expected_text = expected_text.replace('PATHS = StudyPaths(__file__)', 'STUDY_PATHS = StudyPaths(__file__)', 1)
        expected_text = expected_text.replace('args = PATHS.parse()', 'args = STUDY_PATHS.parse()', 1)
        for node in ast.walk(new):
            if isinstance(node, ast.Name) and node.id == 'STUDY_PATHS':
                node.id = 'PATHS'
        kind = 'routing object only; mathematical PATHS tuple unchanged'
    elif path.name == 'depth_assembler.py':
        old_function = next(n for n in old.body if isinstance(n, ast.FunctionDef) and n.name == '_read_accepted')
        new_function = next(n for n in new.body if isinstance(n, ast.FunctionDef) and n.name == '_read_accepted')
        expected_text = expected_text.replace(
            'def _read_accepted(depth: int) -> dict[str, SPoly]:\n    root = Path(__file__).resolve().parents[2]',
            'def _read_accepted(depth: int) -> dict[str, SPoly]:\n'
            '    """Read the explicitly frozen comparison maps from retained historical data."""\n'
            '    root = Path(__file__).resolve().parents[4] / "data/historical/studies/mfp_gaussian_calculus"', 1)
        assert isinstance(new_function.body[0], ast.Expr)
        new_function.body = [copy.deepcopy(old_function.body[0]), *new_function.body[2:]]
        kind = 'historical path and loader docstring only; parsing/comparison unchanged'
    else:
        reason_node = next(n for n in new.body if isinstance(n, ast.Assign) and
                           any(isinstance(t, ast.Name) and t.id == 'ARCHIVE_ONLY_REASON' for t in n.targets))
        reason = ast.literal_eval(reason_node.value)
        block = ('ARCHIVE_ONLY_REASON = ' + json.dumps(reason) + '\n'
                 'if __name__ == "__main__":\n    raise RuntimeError(ARCHIVE_ONLY_REASON)\n\n')
        if path.name == 'run_checks.py':
            expected_text = expected_text.replace('from .audit_hostile', block+'from .audit_hostile', 1)
            entry = 'run'
        else:
            marker = 'from __future__ import annotations\n\n'
            expected_text = expected_text.replace(marker, marker+block, 1)
            entry = 'run' if path.name == 'audit_hostile.py' else 'build' if path.name == 'build_full_report.py' else 'emit'
        signature = next(line for line in original.splitlines() if line.startswith('def '+entry+'('))
        expected_text = expected_text.replace(signature+'\n', signature+'\n    raise RuntimeError(ARCHIVE_ONLY_REASON)\n', 1)
        def reason_raise(node):
            return isinstance(node, ast.Raise) and any(isinstance(n, ast.Name) and n.id == 'ARCHIVE_ONLY_REASON'
                                                      for n in ast.walk(node))
        new.body = [n for n in new.body if n is not reason_node and not
                    (isinstance(n, ast.If) and len(n.body) == 1 and reason_raise(n.body[0]))]
        function = next(n for n in new.body if isinstance(n, ast.FunctionDef) and n.name == entry)
        assert reason_raise(function.body[0])
        function.body = function.body[1:]
        kind = 'early CLI refusal and first-step callable refusal only; original bodies retained'
    ast_preserved = ast.dump(new, include_attributes=False) == ast.dump(old, include_attributes=False)
    exact_text_preserved = current == expected_text
    assert ast_preserved and exact_text_preserved, (source['path'], ast_preserved, exact_text_preserved,
                                                   repr(current[:250]), repr(expected_text[:250]))
    checks.append({'path': source['path'], 'change': kind,
                   'sha256_before': source['sha256'], 'sha256_after': hashlib.sha256(current.encode()).hexdigest(),
                   'only_permitted_text_edits': exact_text_preserved, 'normalized_ast_identical': ast_preserved})

print(json.dumps({'passed': True, 'files': checks}, indent=2))
