"""Private implementation inventory; no repository writes."""
import ast
import hashlib
import json
from pathlib import Path
import sys

BASE = Path('/home/amir/Codes/PDE')
OUT = Path(__file__).parent
STUDIES = ('mfp_gaussian_calculus', 'stieltjes_resolution')

def sha(payload):
    return hashlib.sha256(payload).hexdigest()

def snapshot():
    rows = {}
    functions = {}
    literals = {}
    for group, prefix in (('source', 'studies'), ('historical', 'data/historical/studies')):
        for study in STUDIES:
            for path in sorted((BASE / prefix / study).rglob('*')):
                if not path.is_file():
                    continue
                name = path.relative_to(BASE).as_posix()
                raw = path.read_bytes()
                rows[name] = {'sha256': sha(raw), 'bytes': len(raw), 'group': group}
                if group == 'source' and path.suffix == '.py':
                    tree = ast.parse(raw)
                    functions[name] = {node.name: sha(ast.dump(node, include_attributes=False).encode())
                                       for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
                    literals[name] = sorted(node.value for node in ast.walk(tree)
                                            if isinstance(node, ast.Constant) and isinstance(node.value, str)
                                            and len(node.value) == 64 and all(char in '0123456789abcdef' for char in node.value))
    return {'files': rows, 'functions': functions, 'digest_literals': literals,
            'shared_helper_sha256': sha((BASE / 'studies/_output_paths.py').read_bytes())}

if __name__ == '__main__':
    phase = sys.argv[1]
    assert phase in ('before', 'after')
    data = snapshot()
    target = OUT / f'{phase}.json'
    target.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
    print('inventory', target, sha(target.read_bytes()))
    if phase == 'after':
        old = json.loads((OUT / 'before.json').read_text())
        changed = {path: {'before': old['files'].get(path), 'after': data['files'].get(path)}
                   for path in old['files'].keys() | data['files'].keys()
                   if old['files'].get(path) != data['files'].get(path)}
        altered_functions = {path: [name for name, digest in values.items()
                                   if data['functions'].get(path, {}).get(name) != digest]
                             for path, values in old['functions'].items()}
        altered_functions = {path: names for path, names in altered_functions.items() if names}
        digest_changes = [path for path, values in old['digest_literals'].items()
                          if data['digest_literals'].get(path) != values]
        proof = {'changed_files': changed, 'changed_existing_functions': altered_functions,
                 'changed_existing_digest_literals': digest_changes,
                 'historical_files_unchanged': all(not (row['before'] or row['after'])['group'] == 'historical' for row in changed.values()),
                 'non_python_files_unchanged': all(Path(path).suffix == '.py' for path in changed),
                 'existing_functions_compared': sum(map(len, old['functions'].values())),
                 'shared_helper_before': old['shared_helper_sha256'],
                 'shared_helper_after': data['shared_helper_sha256']}
        (OUT / 'preservation.json').write_text(json.dumps(proof, indent=2, sort_keys=True) + '\n')
        print(json.dumps(proof, indent=2))
