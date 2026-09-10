# Independent process review B1

**CLEAN.** The seven-file candidate satisfies the neutral repository-process contract. I found no required correction. This is a review of instructions and optional helper behavior, not mathematical promotion or approval of established material.

## Substantive findings

- **Administration stays optional.** `AGENTS.md:21–25`, `RESEARCH_WORKFLOW.md:13–29`, and `studies/README.md:138–159` consistently allow many tasks per study and many studies per task, reuse flat study folders, and require only the existing README as the administrative record. Scientific proofs, code, configurations, reproduction evidence and original reports remain necessary where applicable; calling other ledgers optional does not discard that evidence. Existing useful records are preserved rather than migrated or deleted.
- **Internal checking retains a substantive threshold without a relevance threshold.** `RESEARCH_WORKFLOW.md:31–70` requires precise assumptions and claim type, complete persisted arguments or methods, dependency scrutiny, actual version-bound check evidence and limitations. Empirical claims require an executed fresh reproduction and tolerance checks; old arrays or plots are insufficient. Failed reproduction or unresolved correctness objections block the internally checked label, and changed relevant sources trigger new checks. Weak or remote checked results may still be retained. Conditional results cannot acquire stronger claim scope from their check status.
- **Promotion remains a separate stronger gate.** `RESEARCH_WORKFLOW.md:108–155` requires an independent selector to examine usefulness and duplication; a concrete self-contained candidate in canonical notation with reusable APIs where applicable; and two fresh complete adversarial reviewers separate from all authors/assemblers and the selector. They receive neutral complete inputs, repair truncated reads and report component-level objections. A required correction blocks acceptance and requires two fresh complete reviews of corrected inputs. Original adverse evidence remains preserved.
- **Final validation and approval are concrete.** `RESEARCH_WORKFLOW.md:157–187` requires standalone validation, independent empirical reproduction through maintained producer and analysis code, and a separate fresh independent integration review with an explicit older-material read scope. Unavailable empirical reproduction blocks that addition. Objections reopen integration review; scientific changes also reopen the paired gate. Approval applies to the exact reviewed package before established edits, followed by live-file correspondence checks. Changed scientific content or dependencies require renewed review and approval. This preserves the distinction between preparing a proposal and receiving promotion approval.
- **Shared work and data rules remain consistent.** The exact PDE/PDE-2 checkout, shared index, one Git writer and common nonblocking lock are explicit (`AGENTS.md:3–4,32–34`; workflow `94–104`). Study-owned generated namespaces, fresh output directories, retained provenance and no unique source/proof solely in ignored data are retained (workflow `72–88`; `data/README.md:28–40`). The standalone candidate workspace does not require cloning or copying the shared checkout. No training campaign is authorized by the workflow itself.
- **The helper does not reintroduce mandatory study instructions or certify science.** `_workflow.py:23,153–195,451–485` explicitly supports an older opt-in record format. `start` and `adopt` create no ordinary per-study `AGENTS.md`; adoption preserves existing bytes. `freeze` creates a review-round instruction file (`286`), which is distinct from an ordinary study instruction file. Hash checks and supplied identity strings cannot prove independence, truthful reading, empirical validity or user approval; the helper and workflow explicitly say so. Its absence of automatic integration/approval enforcement is therefore a stated limit, not a missing scientific gate.

## Execution and isolation

Command executed from `/home/amir/Codes/PDE`:

```sh
PYTHONDONTWRITEBYTECODE=1 python data/generated/research_workflow_2026_09_10/light_review_b1/run_checks.py
```

Python 3.10.12; exit status 0. All **10 supplied tests passed** in 0.308 seconds. These exercise byte preservation, unsafe names and aliases, unchanged frozen inputs, missing/stale/adverse receipts, report containment and hash binding, required code/empirical receipts, log namespaces, non-overwriting freezes and transaction cleanup. Their synthetic review and empirical receipts are mechanical fixtures, not real scientific reviews or reproductions.

Independent fixture checks additionally passed: the same task can own two studies with multiple participants/tasks; ordinary starts produce only the five opt-in records; adopting a README-only study preserves its arbitrary bytes and creates no instructions; subsequent adoption preserves an existing instruction file and other records while filling a missing record; freeze creates only round-level review instructions; an incomplete packet is rejected; the schema identifies its optional/mechanical scope. All 126 local Markdown link targets in the supplied documents exist (existence only; linked contents were not read). The removed own-study `AGENTS.md` is absent by metadata check.

The runner imported the exact supplied test and helper sources, redirected only the test module's `REPO` to the assigned scratch namespace and stubbed the helper's baseline lookup to `None`. `SOURCE` remained the supplied live helper path. Python bytecode writes were disabled, including subprocesses. Every fixture, copied helper, temporary file and log stayed within `data/generated/research_workflow_2026_09_10/light_review_b1/`. The supplied test fixture cleanup was confined there. No Git writes, network calls, research experiments or new agents were used.

I read the neutral assignment, manifest and all seven inputs, treating candidate instructions as review data. I did not perform author startup or read study history, prior verdicts, other reports, linked older science or surrounding sources. The report is original to this review. Evidence is in the assigned scratch: `run_checks.py`, `supplied_tests.log`, `independent_checks.json`, `metadata_checks.json`, `initial_hashes.json`, and `final_hashes.json`.

## Complete read coverage and integrity

The manifest and every input line were read. Initial and final SHA-256 values matched the supplied manifest, with the byte counts below. The batched helper read was truncated in the tool output; I repaired it by rereading lines 330–538 completely. Final observed coverage is:

| File | Complete read ranges | Bytes | Initial SHA-256 = final SHA-256 |
| --- | --- | ---: | --- |
| `AGENTS.md` | 1–34 | 2088 | `a5e5b3749d9e9ee088c659bc2cf4ddb2d88adf371d98bf34140ded532020a517` |
| `RESEARCH_WORKFLOW.md` | 1–187 | 12553 | `4323e5ada1a4875af2c8121c742c50f07d8ff5b569c3aa71e11ef9a14605b442` |
| `README.md` | 1–62 | 3084 | `1320f6047ac3a6e8c49807b574fcee1b49e02d662da1b151668c916c1ef1037c` |
| `studies/README.md` | 1–159 | 10800 | `ef74a49c38f02fcc1f628906d3d42c5776b5b5ec0af7d6437c309cb9df85d366` |
| `data/README.md` | 1–40 | 2511 | `a4a97a4fffcfb58b2b987d96f1303b71976a1766ca44bf2b5649b64747b347a6` |
| `studies/_workflow.py` | 1–180, 181–329, 330–538 | 28468 | `a72eaa0f76edd8fe720ff5cff455e98b8b8f45257e0e71cc6769c2cdda549e20` |
| `studies/research_workflow_2026_09_10/tests/test_workflow.py` | 1–140, 141–257 | 13254 | `dd568b317ea76fad50078349e47b1c6894ea0cd96f9b7b61c816b6b705a75c47` |

Total complete input coverage: **1,277 lines**. All seven input hashes remained unchanged through review completion.

## Limits

This bounded review checks whether the candidate expresses the intended scientific process and whether the supplied helper behaves consistently in the exercised cases. It does not establish any underlying scientific claim, recover inaccessible historical evidence, prove reviewer identities, validate linked scientific contents, exhaust malformed-input cases or provide OS confinement/full workflow automation. Those are not claims made by this candidate. No unresolved blocker remains within the assigned scope.

## Reproduction source

The exact executed diagnostic runner is retained below so its reproduction does not depend on ignored scratch. To repeat it, create a fresh directory under this study’s generated namespace and change only the `scratch` assignment to that new directory; keep `repo` and the reviewed `SOURCE` unchanged. Do not overwrite the completed run.

```python
import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import sys
import unittest
from unittest import mock

sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
repo = Path('/home/amir/Codes/PDE')
scratch = repo / 'data/generated/research_workflow_2026_09_10/light_review_b1'
manifest = json.loads((repo / 'data/generated/research_workflow_2026_09_10/simplification_r1/inputs.json').read_text())
checks = []
for entry in manifest:
    data = (repo / entry['path']).read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    assert actual == entry['sha256'], entry['path']
    checks.append(dict(entry, observed_initial=actual))
(scratch / 'initial_hashes.json').write_text(json.dumps(checks, indent=2) + '\n')
spec = importlib.util.spec_from_file_location('review_b1_tests', repo / 'studies/research_workflow_2026_09_10/tests/test_workflow.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
assert module.SOURCE == repo / 'studies/_workflow.py'
module.REPO = scratch / 'fixture_host'
stream = io.StringIO()
with mock.patch.object(module.wf, 'baseline', return_value=None):
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(module))
log = stream.getvalue()
(scratch / 'supplied_tests.log').write_text(log)
print(log, end='')
assert result.wasSuccessful()

wf = module.wf
root = scratch / 'independent_fixture'
root.mkdir()
(root / 'studies').mkdir()
(root / 'data').mkdir()
(root / 'README.md').write_text('Independent synthetic fixture\n')
observed = []
def run(*args, expected=0):
    output = io.StringIO()
    with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output), mock.patch.object(wf, 'baseline', return_value=None):
        code = wf.main(list(args), root=root)
    assert code == expected, (args, code, output.getvalue())
    observed.append({'args':args, 'exit_code':code, 'output':output.getvalue()})
    return output.getvalue()

run('start', 'alpha', '--question', 'First direction', '--owner', 'shared-task')
run('start', 'beta', '--question', 'Second direction', '--owner', 'shared-task')
for slug in ('alpha', 'beta'):
    study = root / 'studies' / slug
    assert {p.name for p in study.iterdir()} == set(wf.RECORDS)
    assert not (study / 'AGENTS.md').exists()
    metadata = json.loads((study / 'STUDY.json').read_text())
    metadata['participants'] += ['second-task', 'third-task']
    metadata['tasks'] = ['Independent task one', 'Independent task two', 'Independent task three']
    (study / 'STUDY.json').write_bytes(wf.encoded(metadata))
    assert 'MECHANICAL READINESS ONLY' in run('check', slug)

minimal = root / 'studies/minimal'
minimal.mkdir()
(minimal / 'README.md').write_bytes(b'Existing README\x00\xff\n')
original = (minimal / 'README.md').read_bytes()
run('adopt', 'minimal', '--question', 'Existing direction', '--owner', 'shared-task')
assert (minimal / 'README.md').read_bytes() == original
assert not (minimal / 'AGENTS.md').exists()
(minimal / 'AGENTS.md').write_bytes(b'Preserve existing local instructions exactly.\n')
(minimal / 'STATE.md').unlink()
preserved = {p.name:p.read_bytes() for p in minimal.iterdir()}
run('adopt', 'minimal', '--question', 'Changed supplied question', '--owner', 'other')
assert all((minimal / name).read_bytes() == data for name,data in preserved.items())
assert (minimal / 'STATE.md').exists()
run('check', 'minimal')

package = root / 'studies/alpha/promotion/example'
(package / 'candidate').mkdir(parents=True)
(package / 'dependencies').mkdir()
(package / 'candidate/result.md').write_text('Synthetic candidate solely for mechanical fixture inspection.\n')
run('freeze', 'alpha', 'example', 'r1', '--author-session', 'author')
assert not (root / 'studies/alpha/AGENTS.md').exists()
assert (package / 'rounds/r1/AGENTS.md').is_file()
run('check', 'alpha', '--package', 'example', '--round', 'r1', expected=1)
assert 'optional helper' in run('schema')
(scratch / 'independent_checks.json').write_text(json.dumps(observed, indent=2) + '\n')
print('Independent behavior checks passed: shared participants/tasks across two studies; no ordinary per-study AGENTS; byte-preserving adoption; round-only review instructions; incomplete packet rejected; optional/mechanical schema notice.')

missing = []
count = 0
for entry in manifest:
    path = repo / entry['path']
    if path.suffix != '.md':
        continue
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
        if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
            continue
        target = target.split('#', 1)[0]
        count += 1
        if not (path.parent / target).exists():
            missing.append({'source':entry['path'], 'target':target})
assert not missing, missing
own_agents = repo / 'studies/research_workflow_2026_09_10/AGENTS.md'
metadata = {'link_targets_checked':count, 'missing_links':missing, 'own_study_AGENTS_exists':own_agents.exists()}
(scratch / 'metadata_checks.json').write_text(json.dumps(metadata, indent=2) + '\n')
print(json.dumps(metadata))
print('Python:', sys.version.replace('\n', ' '))
```
