import hashlib
import json
from pathlib import Path
import subprocess

private = Path(__file__).parent
inventory = json.loads((private / 'frozen_inventory.json').read_text())
paths = [row['path'] for row in inventory]
raw = subprocess.check_output(['git', 'ls-tree', '-r', 'e93ce49', '--', *paths],
                              cwd='/home/amir/Codes/PDE', text=True)
committed = {line.split('\t', 1)[1]: line.split('\t', 1)[0].split()[2]
             for line in raw.splitlines()}
rows = []
for relative in paths:
    data = (private / 'snapshot' / relative).read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    rows.append({'path':relative, 'snapshot_git_blob':blob, 'commit_git_blob':committed.get(relative),
                 'matches':blob == committed.get(relative)})
result = {'commit':'e93ce49', 'included_ancestor':'5b9ef6e', 'files':len(rows), 'all_match':all(x['matches'] for x in rows),
          'mismatches':[x for x in rows if not x['matches']], 'records':rows}
(private / 'commit-verification.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k:v for k,v in result.items() if k != 'records'}, indent=2))
