"""Preserve complete archival output, then keep a compact durable source map.

Run after H3_v2_review_provenance_check_v3.py. Original full-result bytes are
written unchanged under a fresh generated name before replacing the study map.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import resource

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
root = Path(__file__).resolve().parents[2]
study = root / 'studies/observable_hierarchy'
mapping = study / 'H3_v2_review_sources_complete_v3.json'
raw_bytes = mapping.read_bytes()
complete = json.loads(raw_bytes)
assert 'checks' in complete['verification'], 'Expected full verifier output.'
scratch = root / 'data/generated/observable_hierarchy/H3_v2_review_provenance_v3'
scratch.mkdir(exist_ok=True)
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
raw_result = scratch / f'verification_{stamp}.json'
with raw_result.open('xb') as stream:
    stream.write(raw_bytes)
assert raw_result.read_bytes() == raw_bytes
compact = {key: value for key, value in complete.items() if key != 'verification'}
compact['verification'] = {
    key: value for key, value in complete['verification'].items()
    if key not in ('checks', 'original_artifact_inventory')
}
compact['verification']['original_artifact_count'] = len(complete['verification']['original_artifact_inventory'])
compact['raw_result'] = dict(path=str(raw_result.relative_to(root)),
                             sha256=hashlib.sha256(raw_bytes).hexdigest(),
                             bytes=len(raw_bytes), byte_identical_to_original_full_result=True)
compact['archival_sources'] = []
for name in ('H3_v2_review_provenance_check_v3.py', 'H3_v2_review_provenance_compact_v3.py'):
    path = study / name
    compact['archival_sources'].append(dict(path=str(path.relative_to(root)),
                                            sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
mapping.write_text(json.dumps(compact, indent=2) + '\n')
print(json.dumps(dict(map_path=str(mapping.relative_to(root)),
                      map_sha256=hashlib.sha256(mapping.read_bytes()).hexdigest(),
                      map_bytes=mapping.stat().st_size, raw_result=compact['raw_result']), indent=2))
