import ast
import hashlib
import json
from pathlib import Path

ROOT = Path('/home/amir/Codes/PDE')
OUT = Path('/tmp/pde-study-routing-worker.C590sh2m')
STUDIES = ('resnet_generalization', 'resnet_proof_audit', 'resnet_activation_controls',
           'stieltjes_finite_width', 'stieltjes_direct_loewner',
           'stieltjes_hybrid_campaign', 'stieltjes_proxy_campaign')

def capture():
    hashes, sources = {}, {}
    selected = [ROOT/'studies/_output_paths.py']
    for name in STUDIES:
        tree = ROOT/'studies'/name
        selected.extend(tree.rglob('*.py'))
        selected.extend(tree.rglob('*.json'))
        selected.extend(tree.rglob('README.md'))
    selected.append(ROOT/'studies/resnet_generalization/REPRODUCTION.md')
    for path in sorted(set(selected)):
        raw = path.read_bytes()
        relative = str(path.relative_to(ROOT))
        hashes[relative] = hashlib.sha256(raw).hexdigest()
        # Retain current code/document baselines privately to compare complete
        # calculation bodies without relying on mutable Git history.
        if path.suffix == '.py' or path.name in ('README.md', 'REPRODUCTION.md'):
            sources[relative] = raw.decode()
    return hashes, sources

if __name__ == '__main__':
    hashes, sources = capture()
    assert not (OUT/'baseline.json').exists()
    (OUT/'hashes.before.json').write_text(json.dumps(hashes, indent=2, sort_keys=True)+'\n')
    (OUT/'baseline.json').write_text(json.dumps(sources, sort_keys=True)+'\n')
    print(f'Captured {len(hashes)} file hashes and {len(sources)} private code/document baselines')
