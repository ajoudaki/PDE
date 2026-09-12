"""Assemble a standalone proposed edition without editing maintained files.

The output must be a new directory in this study's generated namespace. Source
hashes are checked against a frozen manifest before any copying. No Git metadata,
studies, history or retained outputs are copied into the assembled edition.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / 'studies' / 'observable_hierarchy'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    out = args.output.resolve()
    allowed = (ROOT / 'data/generated/observable_hierarchy').resolve()
    if allowed not in out.parents or out.exists():
        raise SystemExit('Use a new directory under data/generated/observable_hierarchy')
    manifest = json.loads((STUDY / 'H2_edition_inputs_v1.json').read_text())
    for relative, expected in manifest['sources'].items():
        if digest(ROOT / relative) != expected:
            raise SystemExit('Frozen input changed: ' + relative)
    out.mkdir(parents=True)
    for relative in manifest['copy_sources']:
        destination = out / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, destination)
    book = (ROOT / 'docs/global_nonlinear.md').read_text()
    anchor = '#### C.4.8. Sampling fluctuations of the trained prediction'
    if book.count(anchor) != 1 or '##### C.4.7.9.' in book:
        raise SystemExit('Unexpected chapter insertion point')
    section = (STUDY / 'H2_proposed_section_v1.md').read_text().rstrip() + '\n\n'
    book = book.replace(anchor, section + anchor)
    (out / 'docs/global_nonlinear.md').write_text(book)
    shutil.copyfile(STUDY / 'H2_docs_README_v1.md', out / 'docs/README.md')
    shutil.copyfile(STUDY / 'H2_code_README_v1.md', out / 'code/README.md')
    shutil.copyfile(STUDY / 'H2_prototype.py', out / 'code/pde/observable_closure.py')
    test = (STUDY / 'H2_test_prototype.py').read_text()
    # The review packet contains this exact mechanical import adaptation.
    old_import = 'os.environ.get("H2_PROTOTYPE_MODULE", "H2_prototype")'
    if test.count(old_import) != 1:
        raise SystemExit('Unexpected prototype-test import')
    test = test.replace(old_import, 'os.environ.get("H2_PROTOTYPE_MODULE", "pde.observable_closure")')
    test = test.replace(
        'Set H2_PROTOTYPE_MODULE=pde.observable_closure after a reviewed relocation.\n'
        'The default imports the study-owned prototype beside this file.',
        'The default imports pde.observable_closure from the installed package.\n'
        'H2_PROTOTYPE_MODULE may override that import for isolated checks.')
    (out / 'code/tests').mkdir(exist_ok=True)
    (out / 'code/tests/test_observable_closure.py').write_text(test)
    outputs = {str(p.relative_to(out)): digest(p) for p in sorted(out.rglob('*')) if p.is_file()}
    (out / 'ASSEMBLY.json').write_text(json.dumps({'inputs': manifest, 'outputs': outputs}, indent=2) + '\n')
    print(json.dumps({'output': str(out), 'files': len(outputs)}, indent=2))


if __name__ == '__main__':
    main()
