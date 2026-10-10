"""Assemble a standalone proposed edition; never edit the maintained library."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
CHAPTER = '07-observable-closure.qmd'
MARKER = '<!-- moved verbatim from gaussian-calculus.qmd:1795-1877;'
POINTER = (
    '\nThe sharp literal-array cost of the frozen-top neural tangent hierarchy '
    'is established in [its storage theorem]'
    '(07-observable-closure.qmd#thm-nth-storage-matching). That short-time, deep-linear '
    'benchmark has a separately stated data regime; it is not a same-family '
    'separation theorem for the constructions of this chapter.\n'
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('candidate', type=Path)
    parser.add_argument('workspace', type=Path)
    args = parser.parse_args()
    candidate = args.candidate.resolve()
    workspace = args.workspace.resolve()
    if not candidate.is_relative_to(STUDY):
        raise ValueError('Candidate must belong to this study')
    if not workspace.is_relative_to(ROOT/'data/generated'/STUDY.name):
        raise ValueError('Workspace must belong to this study generated namespace')
    if re.search(r'^:+\s*\{[^\n}]*#proof-[^\n}]*\.proof',
                 candidate.read_text(), re.M):
        raise ValueError('Use a standalone []{#proof-...} anchor before ::: {.proof}')
    workspace.mkdir(parents=True, exist_ok=False)
    originals = []
    for name in ('docs', 'code'):
        shutil.copytree(ROOT/name, workspace/name,
                        ignore=shutil.ignore_patterns('.quarto', '__pycache__', '*.pyc'))
        for path in sorted((workspace/name).rglob('*')):
            if path.is_file():
                originals.append({'path': str(path.relative_to(workspace)),
                                  'sha256': digest(path)})
    chapter = workspace/'docs'/CHAPTER
    text = chapter.read_text()
    if text.count(MARKER) != 1:
        raise ValueError('Expected unique Chapter 7 insertion point')
    block = candidate.read_text().strip() + '\n\n'
    chapter.write_text(text.replace(MARKER, block + MARKER, 1))
    compression = workspace/'docs/08b-trajectory-compression.qmd'
    text = compression.read_text()
    marker = '\n## Setup and the headline theorem'
    if text.count(marker) != 1:
        raise ValueError('Expected unique compression setup')
    compression.write_text(text.replace(marker, POINTER + marker, 1))
    bib = workspace/'docs/references.bib'
    new_bib = (STUDY/'PROMOTION_REFERENCES.bib').read_text()
    if 'huang2020nth' in bib.read_text():
        raise ValueError('Citation key already exists; reconcile before assembly')
    bib.write_text(bib.read_text().rstrip() + '\n\n' + new_bib)
    (workspace/'candidate.qmd').write_bytes(candidate.read_bytes())
    (workspace/'notation.qmd').write_bytes((ROOT/'docs/notation.qmd').read_bytes())
    (workspace/'references.bib').write_bytes((STUDY/'PROMOTION_REFERENCES.bib').read_bytes())
    # The entire edition remains self-contained inside workspace: its existing
    # output-dir and source-packaging hook use this local docs/code pair.
    manifest = {
        'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'candidate': {'path': str(candidate.relative_to(ROOT)), 'sha256': digest(candidate)},
        'authors_assemblers': ['originating study authors (README ownership)',
                               '/root', '/root/nth_compact_assembly'],
        'selector': '/root/nth_selector_current',
        'original_library': originals,
        'changed': [{'path': str(p.relative_to(workspace)), 'sha256': digest(p)}
                    for p in (chapter, compression, bib)],
        'scientific_inputs': [{'path': p.name, 'sha256': digest(p)}
                              for p in (workspace/'candidate.qmd', workspace/'notation.qmd',
                                        workspace/'references.bib')],
    }
    (workspace/'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    ids = re.findall(r'\{#([\w-]+)', block)
    refs = re.findall(r'(?<![\w])@((?:sec|eq|thm|lem|prp|cor|def|rem|proof)-[\w-]+)', block)
    all_text = '\n'.join(p.read_text() for p in (workspace/'docs').glob('*.qmd'))
    all_ids = re.findall(r'\{#([\w-]+)', all_text)
    errors = [f'duplicate new identifier: {i}' for i in ids if all_ids.count(i) != 1]
    errors += [f'unresolved new reference: {r}' for r in refs if r not in all_ids]
    if errors:
        raise ValueError('\n'.join(errors))
    print(json.dumps({'workspace': str(workspace), 'candidate_lines': len(block.splitlines()),
                      'new_ids': len(ids), 'new_refs': len(refs), 'identifier_check': 'PASS'}))


if __name__ == '__main__':
    main()
