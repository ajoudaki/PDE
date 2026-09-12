"""Deterministic source-correspondence and proposed-document checks."""
from pathlib import Path
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / 'studies/observable_hierarchy'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--edition', type=Path)
    args = parser.parse_args()
    protected = json.loads((STUDY / 'H2_source_hashes.json').read_text())
    # This validates the unmodified live sources before user-approved promotion.
    for name, value in protected.items():
        if sha(ROOT / name) != value:
            raise AssertionError('Source changed: ' + name)
    packet = (STUDY / 'dependencies_v1.md').read_text()
    checked = []
    for part in packet.split('\n---\n'):
        if not part.lstrip().startswith('Source:'):
            continue
        header, body = part.strip().split('\n\n', 1)
        source = header.split('`')[1]
        assert body.strip() in (ROOT / source).read_text(), source
        checked.append(header)
    old = (STUDY / 'candidate_v3.md').read_text().rstrip()
    assert old in (ROOT / 'docs/global_nonlinear.md').read_text()
    proposal = (STUDY / 'H2_proposed_section_v3.md').read_text()
    labels = set(re.findall(r'\(H2\.(\d+)\)', proposal))
    assert labels == {str(i) for i in range(20)}, labels
    assert not re.search(r'[A-Za-z_]\(H2\.', proposal), 'Equation renaming touched a function call'
    assert 'studies/' not in proposal and 'dependencies_v1.md' not in proposal
    assert '||D_N||op<=2' in proposal
    if args.edition:
        edition = args.edition.resolve()
        book = (edition / 'docs/global_nonlinear.md').read_text()
        assert old in book, 'Frozen C-H1 body changed in proposed edition'
        assert proposal.rstrip() in book
        anchor = '#### C.4.8. Sampling fluctuations of the trained prediction'
        restored = book.replace(proposal.rstrip()+'\n\n', '', 1)
        assert restored == (ROOT / 'docs/global_nonlinear.md').read_text(), 'Unrelated book change'
        assert book.index(proposal.rstrip()) < book.index(anchor)
        for part in packet.split('\n---\n'):
            if not part.lstrip().startswith('Source:'):
                continue
            header, body = part.strip().split('\n\n', 1)
            assert body.strip() in (edition / header.split('`')[1]).read_text()
        assert (edition / 'code/pde/observable_closure.py').read_bytes() == (STUDY / 'H2_prototype_v3.py').read_bytes()
    print(json.dumps({'status': 'PASS', 'dependency_excerpts': len(checked),
                      'frozen_C_H1_preserved': True, 'equation_labels': sorted(labels,key=int),
                      'edition': str(args.edition) if args.edition else None}, indent=2))


if __name__ == '__main__':
    main()
