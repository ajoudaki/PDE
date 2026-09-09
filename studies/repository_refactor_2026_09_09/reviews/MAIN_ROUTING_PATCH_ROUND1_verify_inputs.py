"""Join read-time hashes to final byte hashes; never read unrelated repository files."""
import collections
import hashlib
import json
from pathlib import Path

PRIVATE = Path(__file__).resolve().parent
REPO = Path('/home/amir/Codes/PDE')
observations = collections.defaultdict(set)
for row in map(json.loads, (PRIVATE / 'read_hashes.jsonl').read_text().splitlines()):
    observations[row['path']].add(row['sha256'])
for line in (PRIVATE / 'initial.sha256').read_text().splitlines():
    sha, relative = line.split('  ', 1)
    observations[str(REPO / relative)].add(sha)
observations[str(REPO / 'studies/resnet_dense_long_horizon/run_all.py')].add(
    '709b1b37e4ec56d63b730bbc970300145223a0f328f18c131f4714fec13070d9')
rows = []
for name, before in sorted(observations.items()):
    path = Path(name)
    after = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
    rows.append({'path': name, 'before_sha256': sorted(before), 'after_sha256': after,
                 'unchanged': len(before) == 1 and after in before})
(PRIVATE / 'input-hashes-before-after.json').write_text(json.dumps(rows, indent=2) + '\n')
(PRIVATE / 'inputs.before.sha256').write_text(''.join(
    f"{r['before_sha256'][0]}  {r['path']}\n" for r in rows))
(PRIVATE / 'inputs.after.sha256').write_text(''.join(
    f"{r['after_sha256']}  {r['path']}\n" for r in rows))
counts = collections.Counter(str(Path(row['path']).relative_to(REPO)).split('/')[0] for row in rows)
summary = {'files': len(rows), 'unchanged': sum(row['unchanged'] for row in rows),
           'changed': [row for row in rows if not row['unchanged']], 'top_level_counts': dict(counts)}
(PRIVATE / 'input-hash-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
