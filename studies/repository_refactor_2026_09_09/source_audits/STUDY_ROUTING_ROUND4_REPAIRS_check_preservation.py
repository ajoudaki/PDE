"""Exact-byte and complete-callable comparison against this patch's snapshots."""
import ast
import difflib
import hashlib
import json
from pathlib import Path

PRIVATE = Path(__file__).resolve().parent
ROOT = Path('/home/amir/Codes/PDE')
SOURCE_PATHS = (
    'studies/resnet_generalization/analyze_generalization.py',
    'studies/resnet_activation_controls/analyze_activation.py',
    'studies/resnet_activation_controls/run_experiment.py',
)
TEST_PATHS = (
    'studies/resnet_generalization/tests/test_writer_boundaries.py',
    'studies/resnet_activation_controls/tests/test_migration_boundaries.py',
)
REPORT = Path('/tmp/seven-study-acceptance.XDKtlKsM/ACCEPTANCE.md')
REPORT_SHA = '18c45145e79aab813f7838e04edc753943e08e04dc4c2f16e986b4a7331945fd'


def sha(value):
    return hashlib.sha256(value).hexdigest()


def replace_exact(text, old, new, count=1):
    assert text.count(old) == count, (old, text.count(old), count)
    return text.replace(old, new)


def normalized_source(relative, current):
    """Undo ONLY the explicitly authorized additions/reordering, then compare all bytes."""
    if relative.endswith(('analyze_generalization.py', 'analyze_activation.py')):
        nodes = {node.name: node for node in ast.parse(current).body if isinstance(node, ast.FunctionDef)}
        lines = current.splitlines(keepends=True)
        helper = nodes['_preflight_analysis_outputs']
        following = nodes['run_analysis']
        current = ''.join(lines[:helper.lineno-1] + lines[following.lineno-1:])
        if relative.endswith('analyze_generalization.py'):
            current = replace_exact(current, '    _preflight_analysis_outputs(args)\n', '', 2)
            current = replace_exact(current,
                '    for destination in (\n'
                '        Path(args.results_dir), Path(args.output_dir),\n'
                '        Path(args.figures_dir), Path(args.report),\n'
                '    ):\n',
                '    for destination in (results, output, figures_dir, report_path):\n')
        else:
            current = replace_exact(current, '    _preflight_analysis_outputs(args)\n', '')
            current = replace_exact(current, '    _preflight_analysis_outputs(args, (pde_seal, dense_seal))\n', '', 2)
    else:
        partial = ('    partial = path.with_suffix(path.suffix + ".partial")\n'
                   '    if partial.exists():\n'
                   '        raise IntegrityError(f"stale partial record blocks write: {partial}")\n')
        final = ('    if path.exists():\n'
                 '        if path.read_text() != encoded:\n'
                 '            raise IntegrityError(f"refusing to overwrite changed record: {path}")\n'
                 '        return\n')
        current = replace_exact(current, partial + final, final + partial)
    return current


def callables(text):
    output = {}

    def visit(node, scope=()):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            scope = (*scope, node.name)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            first = min([node.lineno, *(d.lineno for d in node.decorator_list)])
            source = ''.join(text.splitlines(keepends=True)[first-1:node.end_lineno])
            output['.'.join(scope)] = {
                'source_sha256': sha(source.encode()),
                'ast_sha256': sha(ast.dump(node, include_attributes=False).encode()),
                'source': source,
            }
        for child in ast.iter_child_nodes(node):
            visit(child, scope)

    visit(ast.parse(text))
    return output


before_inventory = json.loads((PRIVATE/'before.json').read_text())
current_inventory = {relative: {'sha256': sha((ROOT/relative).read_bytes()),
                                'bytes': (ROOT/relative).stat().st_size}
                     for relative in before_inventory}
changed = {p for p in before_inventory if before_inventory[p] != current_inventory[p]}
assert changed == set(SOURCE_PATHS + TEST_PATHS), changed
assert sha(REPORT.read_bytes()) == REPORT_SHA
records = []
diffs = []
for relative in SOURCE_PATHS + TEST_PATHS:
    original_bytes = (PRIVATE/'originals'/relative).read_bytes()
    current_bytes = (ROOT/relative).read_bytes()
    assert sha(original_bytes) == before_inventory[relative]['sha256']
    original, current = original_bytes.decode(), current_bytes.decode()
    old_calls, new_calls = callables(original), callables(current)
    assert old_calls.keys() <= new_calls.keys()
    changed_calls = [name for name in old_calls if old_calls[name]['source_sha256'] != new_calls[name]['source_sha256']]
    added_calls = sorted(new_calls.keys() - old_calls.keys())
    if relative in SOURCE_PATHS:
        restored = normalized_source(relative, current)
        assert restored.encode() == original_bytes, relative
        expected_changed = ['_write_once'] if relative.endswith('run_experiment.py') else ['run_analysis']
        assert changed_calls == expected_changed, (relative, changed_calls)
        assert added_calls == ([] if relative.endswith('run_experiment.py') else ['_preflight_analysis_outputs'])
    else:
        assert changed_calls == [], (relative, changed_calls)
    row = {
        'path': relative, 'before_sha256': sha(original_bytes), 'after_sha256': sha(current_bytes),
        'original_callable_count': len(old_calls), 'changed_original_callables': changed_calls,
        'added_callables': added_calls,
        'full_module_bytes_equal_after_exact_boundary_only_reversal': relative in SOURCE_PATHS,
        'callables': {name: {'before': {k: v for k, v in old_calls[name].items() if k != 'source'},
                             'after': {k: v for k, v in new_calls[name].items() if k != 'source'}}
                      for name in old_calls},
    }
    records.append(row)
    diffs.extend(difflib.unified_diff(original.splitlines(keepends=True), current.splitlines(keepends=True),
                                    fromfile='originals/'+relative, tofile=relative))
    print(json.dumps({k: v for k, v in row.items() if k != 'callables'}))

assert sum(len(callables((ROOT/p).read_text())) - len(callables((PRIVATE/'originals'/p).read_text()))
           for p in TEST_PATHS) > 16  # Tests plus their inert routing fixture helpers.
summary = {
    'status': 'PASS', 'inventory_files': len(before_inventory), 'changed_paths': sorted(changed),
    'unchanged_inventory_files': len(before_inventory)-len(changed),
    'prior_report': str(REPORT), 'prior_report_before_sha256': REPORT_SHA,
    'prior_report_after_sha256': sha(REPORT.read_bytes()), 'files': records,
}
(PRIVATE/'preservation.json').write_text(json.dumps(summary, indent=2)+'\n')
(PRIVATE/'patch.diff').write_text(''.join(diffs))
print('PRESERVATION PASS: exact complete-source restoration, all original test callables unchanged, report unchanged')
