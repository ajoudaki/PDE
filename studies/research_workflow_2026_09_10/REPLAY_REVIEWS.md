# Replaying the deterministic review diagnostics

These commands replay bounded maintenance diagnostics, not the reviewers' human
judgment or any scientific experiment. A fresh replay does not replace the saved
original runs. From the repository root, choose a new unused run name below.
The selected seven-file packet is sufficient: no historical arrays or book proofs
are needed. Python 3.10.12 and its standard library were used originally.

The A scripts resolve their packet root from their own scratch-file location;
the B script uses its working directory. Restore those original layouts rather
than editing the preserved scripts or executing them beside their source copies.

```python
from pathlib import Path
import hashlib, json, os, subprocess, sys

root = Path.cwd()
study = root / 'studies/research_workflow_2026_09_10'
work = root / 'data/generated/research_workflow_2026_09_10/replay_r1_001'
work.mkdir(parents=True, exist_ok=False)
manifest = json.loads((study / 'reviews/r1/INPUTS.json').read_text())
for item in manifest:
    source = study / 'reviews/r1/inputs' / item['path']
    content = source.read_bytes()
    assert hashlib.sha256(content).hexdigest() == item['sha256']
    target = work / item['path']
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)
    target.chmod(0o444)

env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1',
           GIT_CEILING_DIRECTORIES=str(work), GIT_CONFIG_NOSYSTEM='1',
           GIT_CONFIG_GLOBAL='/dev/null')
commands = [[sys.executable, '-B',
             'studies/research_workflow_2026_09_10/tests/test_workflow.py', '-v']]
for label, folder, names in [
    ('A1', 'a1_checks', ['adversarial_checks.py', 'transaction_checks.py']),
    ('B1', 'reviewer_b1', ['adversarial_checks.py']),
]:
    area = work / 'data/generated/research_workflow_2026_09_10' / folder
    area.mkdir(parents=True, exist_ok=False)
    for name in names:
        target = area / name
        target.write_bytes((study / 'reviews' / ('evidence_' + label) / name).read_bytes())
        commands.append([sys.executable, '-B', str(target)])
for index, command in enumerate(commands):
    result = subprocess.run(command, cwd=work, env=env,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (work / ('command_%d.log' % index)).write_bytes(result.stdout)
    assert result.returncode == 0, (command, result.returncode)
```

All fixtures and generated logs remain inside the new study-owned workspace.
Original scripts and input hashes are recorded in `reviews/EVIDENCE.json` and
`reviews/r1/INPUTS.json`. Preserve the new invocation/environment, exit statuses
and output hashes if using a replay as further evidence; do not relabel an older
review as having examined later source changes.
