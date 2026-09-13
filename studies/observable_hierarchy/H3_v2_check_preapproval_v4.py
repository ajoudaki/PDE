"""Verify the reviewed proposal against its still-unmodified established bases.

Static preapproval check only: 60 CPU seconds, 1 GiB, no solver execution.
Run from any directory with --output set to a fresh study-owned generated path.
This checker deliberately expects the pre-promotion book/code hashes.
"""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import time

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
start = time.process_time()
root = Path(__file__).resolve().parents[2]
study = root/'studies/observable_hierarchy'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
output = args.output.resolve()
assert output.is_relative_to(root/'data/generated/observable_hierarchy')
assert not output.exists()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
checks = []

def check(path, expected):
    actual = sha(path)
    assert actual == expected, str(path)
    checks.append(dict(path=str(path.relative_to(root)), sha256=actual))

for version in ('v2', 'v3'):
    edition = root/f'data/generated/observable_hierarchy/H3_v2_edition_{version}'
    manifest = json.loads((edition/'review/manifest.json').read_text())
    assert (edition/'review/manifest.json').read_bytes() == (study/f'H3_v2_edition_{version}_manifest.json').read_bytes()
    for name, expected in manifest['edition_hashes'].items():
        check(edition/name, expected)

edition = root/'data/generated/observable_hierarchy/H3_v2_edition_v3'
manifest = json.loads((edition/'review/manifest.json').read_text())
for name, expected in manifest['source_hashes'].items():
    check(root/name, expected)
check(study/'H3_v2_assemble.py', manifest['assembler_sha256'])
evidence = json.loads((study/'H3_v2_evidence_v3.json').read_text())
for name, item in evidence['files'].items():
    check(root/name, item['sha256'])
    assert (root/name).stat().st_size == item['bytes']
integration = root/'data/generated/observable_hierarchy/H3_v2_integration_v4'
entry = json.loads((integration/'entry_hashes.json').read_text())
end = json.loads((integration/'exit_hashes.json').read_text())
for name, item in end['files'].items():
    assert item['sha256'] == entry['files'][name]['expected'] == entry['files'][name]['sha256']
    check(root/name, item['sha256'])
for name, expected in {
    'H3_v2_scientific_a_v3.md': 'b71ffc512de13794f32b3c9b5f8474a4b95472e237592a327de524ff44c89309',
    'H3_v2_scientific_b_v3.md': '7b54689374a160bc91139c063c03d79ad35995653ce96ffb1a85d80b2b4c3dc9',
    'H3_v2_integration_v4.md': '1269a5e66a407876c4c48dfaf6d44b949114377ecaeb7a8fe8c33dbbdf2e037d',
    'H3_contract.md': 'e2378953321766e6b327b341a77bfe9a07f4f564c7b1cef6e3b8b8a126048f5e',
}.items():
    check(study/name, expected)
mapping = json.loads((study/'H3_v2_promotion_mapping_v4.json').read_text())
check(edition/'review/manifest.json', mapping['edition_manifest_sha256'])
for name, item in mapping['files'].items():
    check(root/item['candidate_path'], item['proposed_sha256'])
    if item['base_sha256'] is None:
        assert not (root/name).exists(), name
    else:
        check(root/name, item['base_sha256'])
patch = study/'H3_v2_proposed_changes_v4.patch'
check(patch, mapping['patch_sha256'])
subprocess.run(['git', 'apply', '--check', str(patch)], cwd=root, check=True)
output.mkdir()
result = dict(status='pass', hash_comparisons=len(checks), checks=checks,
              proposed_destinations=len(mapping['files']), patch_applies_without_changes=True,
              cpu_seconds=time.process_time()-start,
              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,
              checker_sha256=sha(Path(__file__)),
              limitation='integrity and application check, not a substitute for reviews or user approval')
(output/'result.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'checks'}, indent=2))
