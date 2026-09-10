# Independent review A1: lightweight research workflow

**Verdict: CLEAN. Required corrections: none within the assigned scope.**

Reviewer: fresh isolated session `/root/light_workflow_review_a1`.
Date: 2026-09-10. This is a repository-process and helper review, not a
mathematical promotion or a review of older scientific results.

## Assignment and isolation

I reviewed the seven selected files against the neutral requirements: one shared
checkout/index; root instructions and one guide with the existing study README as
the only required administrative record; tasks and studies having a many-to-many
relationship; rigorous internal checks and executed empirical reproducibility;
stronger fresh promotion reviews, independent relevance screening, canonical
self-contained theory and reusable code, and approval of the concrete reviewed
addition before established changes; preservation of artifacts; optional helper
schemas; no ordinary per-study instruction-file creation or requirement.

I read only the neutral assignment, its input manifest, and the complete seven
selected files. I did not perform author startup, inspect author conversation or
study history, read old verdicts or another reviewer's report, follow linked old
scientific text, run research experiments, access the network, or mutate Git.
Candidate instruction files were treated as review data. No further agents were
used. Writes were confined to this original report and the assigned scratch area
`data/generated/research_workflow_2026_09_10/light_review_a1/`.

The only additional repository inspection was existence metadata for local
navigation targets and the assigned study's absent `AGENTS.md`. The helper's
unmodified read-only `git rev-parse --verify HEAD` baseline queries were permitted.
No missing review inputs were found.

## Complete reading and input identity

Manifest: `data/generated/research_workflow_2026_09_10/simplification_r1/inputs.json`.
Initial and final SHA-256, byte counts and line counts all matched that manifest.
All **1,277 lines** were read, including implementation, tests, schemas and prompts.

| File | Complete read range | Bytes | Initial = final SHA-256 |
| --- | ---: | ---: | --- |
| `AGENTS.md` | 1–34 | 2088 | `a5e5b3749d9e9ee088c659bc2cf4ddb2d88adf371d98bf34140ded532020a517` |
| `RESEARCH_WORKFLOW.md` | 1–187 | 12553 | `4323e5ada1a4875af2c8121c742c50f07d8ff5b569c3aa71e11ef9a14605b442` |
| `README.md` | 1–62 | 3084 | `1320f6047ac3a6e8c49807b574fcee1b49e02d662da1b151668c916c1ef1037c` |
| `studies/README.md` | 1–159 | 10800 | `ef74a49c38f02fcc1f628906d3d42c5776b5b5ec0af7d6437c309cb9df85d366` |
| `data/README.md` | 1–40 | 2511 | `a4a97a4fffcfb58b2b987d96f1303b71976a1766ca44bf2b5649b64747b347a6` |
| `studies/_workflow.py` | 1–538 | 28468 | `a72eaa0f76edd8fe720ff5cff455e98b8b8f45257e0e71cc6769c2cdda549e20` |
| `studies/research_workflow_2026_09_10/tests/test_workflow.py` | 1–257 | 13254 | `dd568b317ea76fad50078349e47b1c6894ea0cd96f9b7b61c816b6b705a75c47` |

Actual reading commands were `cat` for the manifest and `nl -ba` for each selected
file. The helper was requested in ranges 1–180, 181–360 and 361–538. The combined
tool response was truncated; I repaired the missing middle by explicitly rereading
`nl -ba studies/_workflow.py | sed -n '340,488p'`. The observed complete ranges
1–180, 181–339, 340–488 and 489–538 cover the whole helper. The other six full-file
reads were visible completely. Python `hashlib.sha256` checks preceded substantive
review, ran before and after tests, and were repeated after testing before this
report was written. No selected input changed.

## Findings and component verdicts

- **Workflow and ordinary bookkeeping: CLEAN.** Root instructions lines 21–30,
  guide lines 13–29 and catalogue lines 138–159 agree on flat studies, shared
  contributions and README-based administration. They preserve existing records
  and make structured records/helper checks explicitly optional. Scientific source,
  actual evidence and original review reports remain substantive requirements;
  those are not replaced by administrative templates.
- **Scientific gates: CLEAN as process specifications.** Guide lines 31–70 retain
  precise scopes and claim types, complete arguments and dependencies, meaningful
  tests, actual check evidence, executed empirical reproduction, unresolved-gap
  treatment, and rechecking after source changes. Lines 72–88 retain authorized
  budgets, fresh outputs, provenance, reproducible commands and durable inputs.
  Part 2 retains independent selection, complete canonical candidates, two fresh
  complete isolated adversarial reviews, correction-triggered fresh reviews,
  standalone validation with producer/analysis reproduction, a separate fresh
  integration review, package-specific user approval, and final correspondence.
  An internal check or optional helper result cannot bypass those gates.
- **Shared checkout and preservation: CLEAN.** Root lines 3–4 prohibit parallel
  checkouts and resetting others' work. Guide lines 94–104 specify assigned writes,
  a common nonblocking Git writer lock, current index/version checks and explicit
  paths. These are coordination rules; the candidate does not claim OS enforcement.
- **Optional helper: CLEAN for this simplification.** `RECORDS`, `templates`,
  `start` and `study_record` omit ordinary per-study `AGENTS.md`. Adoption adds
  missing opt-in records and preserves existing bytes. `freeze` still creates a
  round-local isolated-review instruction file; that is explicit packet support,
  not an ordinary study instruction requirement. The schema and printed check
  notice explicitly limit the helper to mechanical consistency. Historical
  lifecycle labels are not promoted into scientific acceptance or user approval.
- **Deterministic checks and navigation: CLEAN.** The supplied suite and the
  independent attacks below passed. All 126 local Markdown link occurrences in
  the five selected guides point to existing targets. This was an existence check,
  not a content audit of those targets. The maintenance study's ordinary
  `AGENTS.md` is absent, including absence of a dangling symlink.

## Executed checks and independent attacks

Working directory: `/home/amir/Codes/PDE`. Python: **3.10.12**.
Exact test command:

```sh
python -B data/generated/research_workflow_2026_09_10/light_review_a1/review_checks.py
```

Exit status **0**. The supplied ten tests passed in **0.392 seconds**. They covered
fresh creation and standalone execution; adoption preservation; unsafe names,
roots and namespaces; symlink/hardlink refusal; non-overwriting freeze and changed
current/frozen sources; each selection/reviewer field gate and report hash binding;
report containment and duplicate reports; extra inputs; code/empirical validation
receipts, namespaces and changed logs; code-component declaration; empty candidates;
and failed-freeze cleanup. Their empirical fixtures are explicitly synthetic
arithmetic subprocesses, not empirical scientific reproductions.

The test module was imported unchanged. Its `SOURCE` remained the exact selected
`studies/_workflow.py`; only module `REPO` was redirected to the assigned scratch
area so fixtures stayed within review ownership. Bytecode writes were disabled.
No Git-command stub or process-execution stub was used. The supplied suite's
`write_new` failure injection remained in place.

Additional independent checks, using a separate synthetic fixture:

1. Created a new opt-in study, adopted a README-only study containing arbitrary
   binary evidence, and checked both records. Neither operation created a study
   `AGENTS.md`; adoption preserved the existing README and binary bytes.
2. Added an existing binary-valued `AGENTS.md`, removed one optional record and
   adopted again with a different proposed owner/question. Every existing file,
   including metadata and the instruction file, stayed byte-identical; only the
   missing optional record was restored.
3. Added a second contributor and two task entries: record checks accepted them.
   Checked every allowed lifecycle value, including `promoted`: each check printed
   the complete mechanical-only disclaimer. This tests reporting, not acceptance.
4. Attacked relative paths with traversal, absolute paths, doubled separators,
   backslashes, NUL and DEL. All seven cases were rejected.
5. Injected failure on the third `write_new` call separately during `start` and
   `adopt`. Both exited 1. New-study rollback removed newly created artifacts;
   adoption rollback exactly preserved the preexisting binary README. This was
   the only additional implementation stub and it was restored immediately.
6. Froze a packet and verified its round-local isolation instructions while the
   study had no local instruction file. A packet check without selection evidence
   exited 1 with the actual missing `selection.json` path.
7. Checked local navigation targets without reading their content; all 126 existed.
   Checked the assigned maintenance study's absent local instruction file.
8. Rehashed every selected input: all seven matched their initial identities.

Full harness, actual command output and before/after identities are retained in
the assigned scratch directory. SHA-256:

| Evidence file | SHA-256 |
| --- | --- |
| `review_checks.py` | `7243b9481b0838e65b9af69867eb652d57226917e0e574583df729e297aa6129` |
| `checks.log` | `2d381e98df5db801c8861ec58f814544c09d62f0a0b5952c1a27aebb5f82c2d5` |
| `hash_checks.json` | `b329768476215e47244bf6c58f5106daca2a9fa251bf67b6ce9b7dee61e7a65a` |

## Limits and unresolved objections

There are no unresolved correctness objections within this bounded review.
No claim is made about old proofs, actual empirical results, old study record
contents, historical preservation across all repository files, or whether other
tasks obey these instructions. The helper cannot establish truthful reviewer
identities, honest complete reading, scientific validity, or real approval; the
candidate explicitly assigns those judgments to the workflow and coordinator.
Concurrency races and hostile OS-level confinement were not tested and are not
requested guarantees. The opt-in helper's retained structured schemas are not a
failure of the required lightweight ordinary process.

This original report is complete for the seven unchanged inputs identified above.

## Complete diagnostic source

The complete original diagnostic source is retained here so reproducing this
review does not depend on ignored scratch. Save it to the recorded harness path
and use an empty assigned scratch fixture area when rerunning; its synthetic
fixtures deliberately use non-overwriting directory creation. The selected source
and supplied test files must retain the identities listed above.

```python
"""Independent deterministic review checks; no source edits or Git writes."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import sys
import unittest

sys.dont_write_bytecode = True
SOURCE_ROOT = Path('/home/amir/Codes/PDE')
SCRATCH = SOURCE_ROOT / 'data/generated/research_workflow_2026_09_10/light_review_a1'
MANIFEST = SOURCE_ROOT / 'data/generated/research_workflow_2026_09_10/simplification_r1/inputs.json'


def inspect_hashes():
    rows = []
    for expected in json.loads(MANIFEST.read_text()):
        content = (SOURCE_ROOT / expected['path']).read_bytes()
        actual = {'path': expected['path'], 'sha256': hashlib.sha256(content).hexdigest(),
                  'bytes': len(content), 'lines': content.count(b'\n') + int(bool(content) and not content.endswith(b'\n'))}
        assert actual == expected, (actual, expected)
        rows.append(actual)
    return rows


def import_file(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run():
    initial = inspect_hashes()
    supplied = import_file('light_a1_supplied_tests', SOURCE_ROOT / 'studies/research_workflow_2026_09_10/tests/test_workflow.py')
    assert supplied.SOURCE == SOURCE_ROOT / 'studies/_workflow.py'
    supplied.REPO = SCRATCH / 'supplied_fixtures'
    print('Supplied tests: SOURCE unchanged; REPO redirected to', supplied.REPO)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(supplied.WorkflowTests)
    result = unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)
    assert result.wasSuccessful()
    wf = supplied.wf
    root = SCRATCH / 'independent_fixture'
    root.mkdir()
    (root / 'studies').mkdir()
    (root / 'data').mkdir()
    (root / 'README.md').write_text('Synthetic review repository.\n')

    def cli(*args, success=True):
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            status = wf.main(list(args), root=root)
        print('CLI', repr(args), 'exit', status, repr(output.getvalue()))
        assert status == (0 if success else 1)
        return output.getvalue()

    plain = root / 'studies/plain'
    plain.mkdir()
    (plain / 'README.md').write_text('Existing useful README; arbitrary bytes follow.\n')
    (plain / 'notes.bin').write_bytes(b'\x00\xff\xfeunchanged')
    existing = {p.name: p.read_bytes() for p in plain.iterdir()}
    print('README-only study exists without administrative extras:', sorted(existing))
    cli('start', 'fresh', '--question', 'Synthetic preservation check?', '--owner', 'shared-task')
    fresh = root / 'studies/fresh'
    assert {p.name for p in fresh.iterdir()} == set(wf.RECORDS)
    assert not (fresh / 'AGENTS.md').exists()
    cli('adopt', 'plain', '--question', 'Synthetic preservation check?', '--owner', 'shared-task')
    assert not (plain / 'AGENTS.md').exists()
    for name, content in existing.items():
        assert (plain / name).read_bytes() == content
    cli('check', 'plain')
    (plain / 'AGENTS.md').write_bytes(b'Existing instruction bytes\x00\xff\n')
    (plain / 'STATE.md').unlink()
    before = {p.name: p.read_bytes() for p in plain.iterdir()}
    cli('adopt', 'plain', '--question', 'Different question', '--owner', 'other-task')
    for name, content in before.items():
        assert (plain / name).read_bytes() == content
    assert (plain / 'STATE.md').is_file()
    cli('check', 'plain')
    print('PASS independent start/adopt: no study AGENTS creation; existing bytes preserved')

    metadata_path = plain / 'STUDY.json'
    metadata = json.loads(metadata_path.read_text())
    metadata['participants'].append('other-task')
    metadata['tasks'] = ['First assigned direction', 'Second assigned direction']
    metadata_path.write_bytes(wf.encoded(metadata))
    cli('check', 'plain')
    for phase in sorted(wf.LIFECYCLES):
        metadata['lifecycle'] = phase
        metadata_path.write_bytes(wf.encoded(metadata))
        assert 'MECHANICAL READINESS ONLY' in cli('check', 'plain')
    print('PASS independent administrative-status test: multiple tasks and historical lifecycle labels do not remove disclaimer')

    cases = ('../escape', 'a/../b', '/absolute', 'a//b', 'a\\b', 'a\x00b', 'a\x7fb')
    for value in cases:
        try:
            wf.relative(value)
        except wf.WorkflowError:
            pass
        else:
            raise AssertionError(('accepted unsafe path', value))
    print('PASS independent unsafe path cases:', repr(cases))

    for operation in ('start', 'adopt'):
        rollback = root / 'studies' / ('rollback-' + operation)
        if operation == 'adopt':
            rollback.mkdir()
            (rollback / 'README.md').write_bytes(b'preserve existing\x00\xff')
        saved = {p.name: p.read_bytes() for p in rollback.iterdir()} if rollback.exists() else None
        real_write = wf.write_new
        count = [0]

        def failing_write(path, content):
            count[0] += 1
            if count[0] == 3:
                raise OSError('independent injected third-write failure')
            return real_write(path, content)

        wf.write_new = failing_write
        try:
            cli(operation, 'rollback-' + operation, '--question', 'q', '--owner', 'o', success=False)
        finally:
            wf.write_new = real_write
        if saved is None:
            assert not rollback.exists()
        else:
            assert {p.name: p.read_bytes() for p in rollback.iterdir()} == saved
    print('PASS independent partial-write rollback preserves preexisting artifacts')

    package = fresh / 'promotion/review'
    (package / 'candidate').mkdir(parents=True)
    (package / 'dependencies').mkdir()
    (package / 'candidate/result.md').write_text('Synthetic identity: x = x.\n')
    cli('freeze', 'fresh', 'review', 'r1', '--author-session', 'author-a')
    round_path = package / 'rounds/r1'
    assert (round_path / 'AGENTS.md').is_file()
    assert not (fresh / 'AGENTS.md').exists()
    prompt = (round_path / 'REVIEW_PROMPT.md').read_text()
    assert 'inert review evidence' in prompt
    missing = cli('check', 'fresh', '--package', 'review', '--round', 'r1', success=False)
    assert 'selection.json' in missing
    print('PASS round-only isolated-review instructions; packet without selection evidence rejected')

    links = []
    for filename in ('AGENTS.md', 'RESEARCH_WORKFLOW.md', 'README.md', 'studies/README.md', 'data/README.md'):
        path = SOURCE_ROOT / filename
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            if '://' in target or target.startswith('#'):
                continue
            target_path = path.parent / target.split('#')[0]
            assert target_path.exists(), (filename, target)
            links.append((filename, target))
    absent = SOURCE_ROOT / 'studies/research_workflow_2026_09_10/AGENTS.md'
    assert not absent.exists() and not absent.is_symlink()
    print('PASS metadata-only navigation checks:', len(links), 'local link targets exist')
    print('PASS metadata-only absence check:', absent)
    final = inspect_hashes()
    assert initial == final
    (SCRATCH / 'hash_checks.json').write_text(json.dumps({'initial': initial, 'final': final}, indent=2) + '\n')
    print('PASS all seven frozen input hashes unchanged at test end')
    print('No external workload, network, or Git mutation; helper baseline queries unmodified.')


if __name__ == '__main__':
    stream = io.StringIO()
    code = 0
    try:
        with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
            run()
    except Exception:
        import traceback
        traceback.print_exc(file=stream)
        code = 1
    (SCRATCH / 'checks.log').write_text(stream.getvalue())
    print(stream.getvalue(), end='')
    raise SystemExit(code)
```
