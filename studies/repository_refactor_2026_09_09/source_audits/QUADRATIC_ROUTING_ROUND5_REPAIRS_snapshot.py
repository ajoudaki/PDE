"""Private stdlib integrity/AST snapshot; historical payloads are hashed only."""
import ast
import hashlib
import json
from pathlib import Path

repo = Path('/home/amir/Codes/PDE')
study = repo / 'studies/mfp_quadratic_compiler'
historical = repo / 'data/historical/studies/mfp_quadratic_compiler'
files = sorted(p for p in study.rglob('*') if p.is_file())
files.append(repo / 'studies/repository_refactor_2026_09_09/test_quadratic_routing.py')
manifest = historical / 'campaign4/results_order9.json'
files.append(manifest)
for record in json.loads(manifest.read_text())['sector_manifest']:
    label = record['path']
    for prefix in ('studies/mfp_quadratic_compiler/', 'studies/mean_field_peeling/quadratic_compiler/'):
        if label.startswith(prefix):
            path = historical / label[len(prefix):]
            break
    else:
        raise AssertionError(label)
    assert path.resolve().is_relative_to(historical)
    files.append(path)
for label in ('provenance_stage_a.json', 'provenance_stage_b.json',
              'provenance_stage_c_projection.json',
              'frozen/stage_a_connected_order3.json', 'frozen/stage_a_reference_order3.json',
              'frozen/stage_b_connected_order5.json'):
    files.append(historical / 'campaign5_b3' / label)
hashes = {str(p): {'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'bytes': p.stat().st_size}
          for p in sorted(set(files))}
functions = {}
for path in study.rglob('*.py'):
    tree = ast.parse(path.read_text())
    functions[str(path)] = {node.name: hashlib.sha256(ast.dump(node, include_attributes=False).encode()).hexdigest()
                          for node in tree.body if isinstance(node, (ast.FunctionDef, ast.ClassDef))}
print(json.dumps({'hashes': hashes, 'python_functions': functions}, indent=2, sort_keys=True))
