"""Static preservation check: original statements/constants remain unchanged."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path('/home/amir/Codes/PDE')
OUT = Path(__file__).parent
before = json.loads((OUT / 'before.json').read_text())
after = json.loads((OUT / 'after.json').read_text())

def dump(node):
    return ast.dump(node, include_attributes=False)

def subsequence(original, current):
    remaining = iter(current)
    return all(any(item == candidate for candidate in remaining) for item in original)

records = []
functions = 0
for original_path in sorted((OUT / 'originals/studies').rglob('*.py')):
    path = ROOT / original_path.relative_to(OUT / 'originals')
    original = ast.parse(original_path.read_text())
    current = ast.parse(path.read_text())
    by_name = {node.name: node for node in current.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
    current_nodes = [dump(node) for node in current.body]
    for node in original.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions += 1
            new = by_name[node.name]
            assert subsequence([dump(item) for item in node.body], [dump(item) for item in new.body]), (path, node.name)
            old_body, new_body = node.body, new.body
            node.body, new.body = [], []
            assert dump(node) == dump(new), (path, node.name, 'signature changed')
            node.body, new.body = old_body, new_body
            if dump(node) != dump(new):
                records.append({'path': str(path), 'function': node.name, 'original_statements_retained_in_order': True,
                                'added_top_level_statements': len(new.body) - len(node.body)})
        elif isinstance(node, ast.ImportFrom) and dump(node) not in current_nodes:
            matches = [item for item in current.body if isinstance(item, ast.ImportFrom) and item.module == node.module and item.level == node.level]
            assert any(set(map(dump, node.names)) <= set(map(dump, item.names)) for item in matches), (path, 'import changed')
        else:
            assert dump(node) in current_nodes, (path, 'pre-existing module statement changed')

historical_before = {path: value for path, value in before.items() if '/data/historical/studies/' in path}
historical_after = {path: value for path, value in after.items() if '/data/historical/studies/' in path}
assert historical_before == historical_after
non_python = {path: value for path, value in before.items() if not path.endswith('.py')}
assert all(after.get(path) == value for path, value in non_python.items())
for phase, entries in (('before', historical_before), ('after', historical_after)):
    (OUT / f'retained-{phase}.sha256').write_text(''.join(f'{value}  {path}\n' for path, value in sorted(entries.items())))
retained_manifest = hashlib.sha256((OUT / 'retained-before.sha256').read_bytes()).hexdigest()
summary = {
    'original_function_bodies_checked': functions,
    'changed_functions_only_add_guard_statements': records,
    'pre_existing_module_statements_and_constants_preserved': True,
    'retained_files_byte_identical': len(historical_before),
    'retained_manifest_sha256_before_and_after': retained_manifest,
    'pre_existing_non_python_files_byte_identical': len(non_python),
    'no_scientific_execution_in_this_check': True,
}
(OUT / 'preservation.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
