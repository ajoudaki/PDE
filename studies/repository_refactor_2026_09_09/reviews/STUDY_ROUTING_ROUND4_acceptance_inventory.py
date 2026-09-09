from pathlib import Path
import ast
import hashlib
import json
import sys

ROOT = Path('/home/amir/Codes/PDE')
PRIVATE = Path(__file__).resolve().parent
STUDIES = ['resnet_generalization', 'resnet_proof_audit', 'resnet_activation_controls', 'stieltjes_finite_width', 'stieltjes_direct_loewner', 'stieltjes_hybrid_campaign', 'stieltjes_proxy_campaign']
EXPLICIT = {'test_raw_output_preflight.py', 'test_acceptance_boundaries.py', 'test_analysis_boundaries.py', 'test_reference_migration_boundaries.py', 'test_shared_output_paths.py', 'test_trapezoid_compat.py'}

def permitted(path):
    return path.name in EXPLICIT or path.name.startswith(('test_migration_', 'test_output_', 'test_writer_'))

def inventory():
    result = {'.gitignore': ROOT / '.gitignore', 'studies/_output_paths.py': ROOT / 'studies/_output_paths.py'}
    for study in STUDIES:
        for path in (ROOT / 'studies' / study).rglob('*'):
            if not path.is_file() or '__pycache__' in path.parts:
                continue
            if path.name.startswith('test_') and not permitted(path):
                continue
            if path.suffix in {'.py', '.sh'} or path.name.startswith(('README', 'REPRODUCTION')):
                result[str(path.relative_to(ROOT))] = path
    return dict(sorted(result.items()))

phase = sys.argv[1]
files = inventory()
records = {name: {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'bytes': path.stat().st_size} for name, path in files.items()}
(PRIVATE / f'{phase}.json').write_text(json.dumps(records, indent=2) + '\n')
(PRIVATE / f'{phase}.sha256').write_text(''.join(f'{value["sha256"]}  {name}\n' for name, value in records.items()))
if phase == 'before':
    tests = [name for name, path in files.items() if permitted(path)]
    (PRIVATE / 'permitted-tests.json').write_text(json.dumps(tests, indent=2) + '\n')
    for name in tests:
        tree = ast.parse((ROOT / name).read_text())
        print(name, len((ROOT / name).read_text().splitlines()), 'lines;', sum(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith('test_') for node in ast.walk(tree)), 'test functions')
    print('SNAPSHOT', len(records), 'files;', len(tests), 'test modules;', hashlib.sha256((PRIVATE / 'before.sha256').read_bytes()).hexdigest())
else:
    before = json.loads((PRIVATE / 'before.json').read_text())
    changed = [name for name in sorted(before.keys() | records.keys()) if before.get(name) != records.get(name)]
    print('CHANGED', json.dumps(changed))
    print('SNAPSHOT', len(records), 'files;', hashlib.sha256((PRIVATE / f'{phase}.sha256').read_bytes()).hexdigest())
