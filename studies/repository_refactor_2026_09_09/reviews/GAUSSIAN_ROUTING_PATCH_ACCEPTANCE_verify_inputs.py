import ast
import hashlib
import json
from pathlib import Path

private = Path(__file__).parent
live = Path('/home/amir/Codes/PDE')
snapshot = private / 'snapshot'
inventory = json.loads((private / 'frozen_inventory.json').read_text())
initial = dict(line.split('  ', 1)[::-1] for line in (private / 'initial-sha256.txt').read_text().splitlines())
records = []
coverage = []
for row in inventory:
    rel = row['path']
    current = (live / rel).read_bytes()
    frozen = (snapshot / rel).read_bytes()
    after = hashlib.sha256(current).hexdigest()
    frozen_after = hashlib.sha256(frozen).hexdigest()
    records.append(dict(row, after_sha256=after, snapshot_after_sha256=frozen_after,
                        initial_target_sha256=initial.get(rel),
                        unchanged=(after == frozen_after == row['before_sha256']
                                   and (rel not in initial or initial[rel] == after))))
    if rel in initial and rel.endswith('.py'):
        tree = ast.parse(frozen)
        coverage.append({'path':rel, 'lines':len(frozen.splitlines()),
                         'full_source_read':True,
                         'functions':[{'name':n.name, 'start':n.lineno,'end':n.end_lineno}
                                      for n in ast.walk(tree) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))],
                         'imports':[ast.unparse(n) for n in ast.walk(tree) if isinstance(n,(ast.Import,ast.ImportFrom))]})
(private / 'input-before-after.json').write_text(json.dumps(records, indent=2) + '\n')
(private / 'full-read-coverage.json').write_text(json.dumps(coverage, indent=2) + '\n')
canonical_before = ''.join(row['before_sha256'] + '  ' + row['path'] + '\n' for row in records).encode()
canonical_after = ''.join(row['after_sha256'] + '  ' + row['path'] + '\n' for row in records).encode()
summary = {'files':len(records), 'all_unchanged':all(row['unchanged'] for row in records),
           'changed':[row['path'] for row in records if not row['unchanged']],
           'aggregate_before_sha256':hashlib.sha256(canonical_before).hexdigest(),
           'aggregate_after_sha256':hashlib.sha256(canonical_after).hexdigest(),
           'full_read_files':len(coverage),'full_read_lines':sum(row['lines'] for row in coverage)}
(private / 'hash-verification.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
