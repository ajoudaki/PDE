"""Independent static integration checks; no trajectories or input edits."""
from pathlib import Path
import difflib
import hashlib
import json
import os
import platform
import re
import subprocess
import sys

ROOT = Path('/home/amir/Codes/PDE')
STUDY = ROOT / 'studies/observable_hierarchy'
SCRATCH = ROOT / 'data/generated/observable_hierarchy/H2_integration_v2'
EDITION = SCRATCH / 'edition'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest = json.loads((STUDY / 'H2_integration_inputs_v2.json').read_text())
checked = {}
for name, record in manifest['inputs'].items():
    actual = sha(ROOT / name)
    assert actual == record['sha256'], name
    checked[name] = dict(sha256=actual, lines=len((ROOT / name).read_bytes().splitlines()))
(SCRATCH / 'verified_inputs.json').write_text(json.dumps(checked, indent=2) + '\n')

assembly = json.loads((EDITION / 'ASSEMBLY.json').read_text())
for name, expected in assembly['outputs'].items():
    assert sha(EDITION / name) == expected, name

unchanged = []
for name in assembly['inputs']['copy_sources']:
    if name not in ('docs/global_nonlinear.md', 'docs/README.md', 'code/README.md'):
        assert (EDITION / name).read_bytes() == (ROOT / name).read_bytes(), name
        unchanged.append(name)

old_book = (ROOT / 'docs/global_nonlinear.md').read_bytes()
book = (EDITION / 'docs/global_nonlinear.md').read_bytes()
section = (STUDY / 'H2_proposed_section_v1.md').read_bytes().rstrip() + b'\n\n'
anchor = b'#### C.4.8. Sampling fluctuations of the trained prediction'
assert old_book.count(anchor) == 1
assert book == old_book.replace(anchor, section + anchor)
assert book.count(section) == 1
old_h1 = (STUDY / 'candidate_v3.md').read_bytes().rstrip()
assert old_book.count(old_h1) == book.count(old_h1) == 1

guides = (STUDY / 'H2_guides_v1.md').read_text()
guide_sources = []
for part in guides.split('\n---\n'):
    if part.lstrip().startswith('Source:'):
        header, body = part.strip().split('\n\n', 1)
        source = header.split('`')[1]
        assert body.rstrip() == (ROOT / source).read_text().rstrip(), source
        guide_sources.append(source)

old_code_guide = (ROOT / 'code/README.md').read_bytes()
new_code_guide = (EDITION / 'code/README.md').read_bytes()
assert new_code_guide.startswith(old_code_guide)
assert new_code_guide == (STUDY / 'H2_code_README_v2.md').read_bytes()
assert (EDITION / 'docs/README.md').read_bytes() == (STUDY / 'H2_docs_README_v1.md').read_bytes()
assert (EDITION / 'code/pde/observable_closure.py').read_bytes() == (STUDY / 'H2_prototype.py').read_bytes()

original_test = (STUDY / 'H2_test_prototype.py').read_text()
expected_test = original_test.replace(
    'os.environ.get("H2_PROTOTYPE_MODULE", "H2_prototype")',
    'os.environ.get("H2_PROTOTYPE_MODULE", "pde.observable_closure")',
).replace(
    'Set H2_PROTOTYPE_MODULE=pde.observable_closure after a reviewed relocation.\n'
    'The default imports the study-owned prototype beside this file.',
    'The default imports pde.observable_closure from the installed package.\n'
    'H2_PROTOTYPE_MODULE may override that import for isolated checks.',
)
assert (EDITION / 'code/tests/test_observable_closure.py').read_text() == expected_test

diff = ''.join(difflib.unified_diff(
    (ROOT / 'docs/README.md').read_text().splitlines(True),
    (EDITION / 'docs/README.md').read_text().splitlines(True),
    fromfile='source/docs/README.md', tofile='edition/docs/README.md'))
(SCRATCH / 'book_guide.diff').write_text(diff)

new_guides = new_code_guide[len(old_code_guide):].decode()
links = []
for target in re.findall(r'\]\(([^)]+)\)', new_guides):
    filename, fragment = target.split('#', 1)
    path = (EDITION / 'code' / filename).resolve()
    assert path.is_file()
    headings = re.findall(r'^#+\s+(.+)$', path.read_text(), flags=re.M)
    slugs = [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings]
    assert slugs.count(fragment) == 1, target
    links.append(target)

env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
           OMP_NUM_THREADS='1', PYTHONPATH=str(EDITION / 'code'),
           H2_TEST_SCRATCH=str(SCRATCH / 'static_scratch'))
env.pop('H2_PROTOTYPE_MODULE', None)
import_program = '''from pathlib import Path
import pde, pde.observable_closure, pde.finite_network, pde.gaussian_moments
import numpy
for module in (pde,pde.observable_closure,pde.finite_network,pde.gaussian_moments):
    print(module.__name__,Path(module.__file__).resolve())
print("numpy",numpy.__version__)
'''
commands = [
    [sys.executable, '-B', str(STUDY / 'H2_check_documents.py'), '--edition', str(EDITION)],
    [sys.executable, '-B', '-c', import_program],
]
records = []
for index, command in enumerate(commands):
    result = subprocess.run(command, cwd=EDITION, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log = SCRATCH / f'independent_check_{index}.log'
    log.write_text(result.stdout)
    assert result.returncode == 0, result.stdout
    records.append(dict(command=command, cwd=str(EDITION), exit=result.returncode,
                        output=str(log), sha256=sha(log)))

summary = dict(status='PASS', source_hashes=checked,
               manifest_sha256=sha(STUDY / 'H2_integration_inputs_v2.json'),
               python=sys.version, platform=platform.platform(),
               environment={k: env[k] for k in ['PYTHONDONTWRITEBYTECODE',
                 'OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'PYTHONPATH', 'H2_TEST_SCRATCH']},
               unchanged_copied_files=unchanged, complete_frozen_guides=guide_sources,
               chapter_bytes_exact=True, complete_C_H1_bytes_exact=True,
               code_guide_append_only=True, module_direct_copy=True,
               test_only_import_and_docstring=True, new_links=links,
               book_guide_hunks=diff.count('@@') // 2, commands=records,
               edition_outputs=assembly['outputs'])
(SCRATCH / 'integration_checks.json').write_text(json.dumps(summary, indent=2)+'\n')
print(json.dumps({k: summary[k] for k in ['status','chapter_bytes_exact',
    'complete_C_H1_bytes_exact','code_guide_append_only','module_direct_copy',
    'test_only_import_and_docstring','new_links','book_guide_hunks']}, indent=2))
