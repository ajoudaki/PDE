"""Build a byte-preserving standalone capsule of the frozen H3 component.

This is a study reproduction capsule, not an installed canonical addition or
an assertion that the full C-H3 milestone has passed its promotion gates.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil


def build(destination):
    source = Path(__file__).resolve().parent
    repo = source.parents[1]
    manifest = json.loads((source/'H3_review_manifest_v2.json').read_text())
    verified = []
    for item in manifest['inputs']:
        path = repo/item['path']
        if hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            raise ValueError('changed frozen input: '+item['path'])
        verified.append((item, path))
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    for item, path in verified:
        target = destination/item['capsule_name']
        if target.exists():
            raise ValueError('duplicate capsule name: '+item['capsule_name'])
        shutil.copyfile(path, target)
    shutil.copyfile(source/'H3_review_manifest_v2.json', destination/'manifest.json')
    (destination/'RUN.md').write_text('''# Standalone bounded-reference capsule

Run in this directory with Python 3.10 or later; only the standard library is
needed. Use a fresh output name on each invocation. These commands execute
the bounded reference component, not an arbitrary-accuracy nonlinear solver.

```
python -B H3_shorttime_test.py
python -B H3_circle_kernel_test.py
python -B H3_reference_solver.py --output run
python -B H3_stability.py --output stability
```

The midpoint checkpoint in run/ is a complete restart state for the reference
coefficient evolution. Its certificate remains relative to time zero. The
kernel.json record serializes initialization-only kernel coefficients. The actual
models, error bounds, supported observations and limitations are in the
included complete candidate texts. No study path is needed to execute these
copied modules or tests.
''')
    return destination


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(build(args.output))
