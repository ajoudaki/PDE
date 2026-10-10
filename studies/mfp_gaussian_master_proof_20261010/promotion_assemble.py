"""Build a selective standalone docs/code edition; never modify maintained inputs."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
GENERATED = ROOT / 'data/generated' / STUDY.name
EXCLUDED = {'.git', '.quarto', '__pycache__', '.pytest_cache', 'node_modules',
            '_book', '_site'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory():
    paths = []
    for dirname in ('docs', 'code'):
        for path in sorted((ROOT / dirname).rglob('*')):
            rel = path.relative_to(ROOT)
            if any(part.startswith('.') or part in EXCLUDED for part in rel.parts):
                continue
            if path.is_symlink():
                raise ValueError(f'Symlink is not a frozen source: {rel}')
            if path.is_file() and path.suffix not in ('.pyc', '.pyo'):
                paths.append(path)
    paths.extend(ROOT / name for name in ('Makefile', 'requirements.txt'))
    return {str(path.relative_to(ROOT)): digest(path) for path in paths}


def replace_exact(path, patches):
    text = path.read_text()
    for patch in patches:
        old, new = patch['old'], patch['new']
        count = patch.get('count', 1)
        if text.count(old) != count:
            raise ValueError(f'Expected {count} patch target(s) in {path}: {old[:100]!r}')
        text = text.replace(old, new, count)
    path.write_text(text)


def assemble(run, baseline_only=False):
    if not run or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789_-' for c in run):
        raise ValueError('Use a simple lowercase run name')
    target = GENERATED / run
    target.mkdir(parents=True, exist_ok=False)
    edition = target / 'edition'
    baseline = inventory()
    for name, expected in baseline.items():
        dest = edition / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, dest)
        assert digest(dest) == expected, name
    assert inventory() == baseline, 'Concurrent source changes: retry a new run'
    (target / 'baseline_manifest.json').write_text(json.dumps(baseline, indent=2)+'\n')
    mapping = {}
    if not baseline_only:
        mapping = json.loads((STUDY / 'promotion_code_mapping.json').read_text())
        for source, dest in mapping.items():
            assert Path(source).name == source and dest.startswith('code/'), (source, dest)
            resolved = (edition / dest).resolve()
            assert resolved.is_relative_to(edition.resolve()), dest
            resolved.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(STUDY / source, resolved)
        replace_exact(edition / 'code/README.md', json.loads(
            (STUDY / 'promotion_code_readme_patches.json').read_text()))
        chapter = edition / 'docs/02-gaussian-reuse.qmd'
        replace_exact(chapter, json.loads((STUDY / 'promotion_book_patches.json').read_text()))
        anchor = '## 7. Reusable finite calculus and forest factorization {#sec-docs-gaussian-calculus-l1824}'
        replace_exact(chapter, [{'old': anchor, 'new':
            (STUDY / 'promotion_theory.qmd').read_text().rstrip()+'\n\n'+anchor}])
        bib = edition / 'docs/references.bib'
        bib.write_text(bib.read_text().rstrip()+'\n\n'+(STUDY / 'promotion_bibliography.bib').read_text())
        quarto_patches = STUDY / 'promotion_quarto_patches.json'
        if quarto_patches.exists():
            replace_exact(edition / 'docs/_quarto.yml', json.loads(quarto_patches.read_text()))
    final = {str(p.relative_to(edition)): digest(p) for p in sorted(edition.rglob('*')) if p.is_file()}
    changed = {name: value for name, value in final.items() if baseline.get(name) != value}
    (target / 'candidate_manifest.json').write_text(json.dumps(final, indent=2)+'\n')
    (target / 'changed_manifest.json').write_text(json.dumps(changed, indent=2)+'\n')
    (target / 'candidate_mapping.json').write_text(json.dumps(mapping, indent=2)+'\n')
    print(json.dumps({'edition':str(edition), 'source_files':len(final), 'changed_files':len(changed)}, indent=2))
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run')
    parser.add_argument('--baseline-only', action='store_true')
    args = parser.parse_args()
    assemble(args.run, args.baseline_only)
