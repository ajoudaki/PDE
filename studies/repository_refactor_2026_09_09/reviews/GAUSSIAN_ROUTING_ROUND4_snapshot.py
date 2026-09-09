import hashlib
import json
from pathlib import Path
import sys

ROOT = Path('/home/amir/Codes/PDE')
TREES = 'causal_flow_peeling_calculus d3_arctan_closure_program mfp_gaussian_calculus mfp_cubic_compiler mfp_identity_compiler mfp_linear_growth_uniform_counterexample mfp_sine_compiler mfp_quadratic_l2_order5 stieltjes_resolution mfp_program_history'.split()
PRIVATE = Path(__file__).parent

def snapshot():
    paths = [ROOT / '.gitignore', ROOT / 'studies/_output_paths.py']
    for tree in TREES:
        for path in (ROOT / 'studies' / tree).rglob('*'):
            # Only current source, tests and README. Never follow links or read retained reports/data.
            if path.is_symlink() or not path.is_file():
                continue
            if any(part in ('__pycache__', '.git', 'generated', 'historical', 'results', 'artifacts', 'build', 'archive') for part in path.relative_to(ROOT / 'studies' / tree).parts[:-1]):
                continue
            if path.suffix in ('.py', '.sh', '.js', '.ts', '.cpp', '.h', '.hpp') or path.name.startswith('README') or path.name == 'Makefile':
                paths.append(path)
    return {str(p.relative_to(ROOT)): {'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'bytes': p.stat().st_size} for p in sorted(paths)}

if __name__ == '__main__':
    current = snapshot()
    destination = PRIVATE / (sys.argv[1] + '.json')
    destination.write_text(json.dumps(current, indent=2) + '\n')
    print(f'{len(current)} permitted files hashed: {destination}')
    if sys.argv[1] == 'after':
        before = json.loads((PRIVATE / 'before.json').read_text())
        changed = [p for p in sorted(before.keys() | current.keys()) if before.get(p) != current.get(p)]
        print('Changed files:', changed)
        assert not changed
