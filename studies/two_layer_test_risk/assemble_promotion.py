"""Freeze the proof-only candidate and its complete relevant dependencies.

Copies selected library source files into a fresh study-owned review/edition
directory. It never edits the live library or copies the checkout/Git index.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    study = root/'studies/two_layer_test_risk'
    output = args.output.resolve()
    allowed = root/'data/generated/two_layer_test_risk'
    if not output.is_relative_to(allowed.resolve()):
        raise ValueError('review output must stay in the study generated namespace')
    expected = {
        'docs/global_nonlinear.md': '8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101',
        'docs/README.md': '4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453',
        'docs/NOTATION.md': '199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b',
    }
    for name, value in expected.items():
        if digest(root/name) != value:
            raise ValueError(f'changed scientific dependency: {name}')
    candidate = (study/'PROMOTION_C4.md').read_text()
    assert candidate.startswith('### C.4.')
    guide_before = (root/'docs/README.md').read_text()
    extra = (' A fixed two-hidden-layer tanh design also admits a controlled cubic '
             'test-risk expansion at equal training loss; the coefficient\'s sign and nonvanishing remain open.')
    lines = guide_before.splitlines(keepends=True)
    matches = [i for i,line in enumerate(lines) if line.startswith('| [Global nonlinear learning]')]
    assert len(matches) == 1
    index = matches[0]
    assert lines[index].endswith(' |\n')
    lines[index] = lines[index][:-3] + extra + ' |\n'
    guide_after = ''.join(lines)
    output.mkdir(parents=True, exist_ok=False)
    packet = output/'packet'
    edition = output/'edition'
    packet.mkdir()
    (edition/'docs').mkdir(parents=True)
    (edition/'code/tools').mkdir(parents=True)
    # These sources resolve the book's local links in a standalone edition.
    copied = list((root/'docs').glob('*.md'))+[root/'code/README.md',root/'code/tools/check_library.py']
    for source in copied:
        target = edition/source.relative_to(root)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source,target)
    base_global = (root/'docs/global_nonlinear.md').read_text()
    (edition/'docs/global_nonlinear.md').write_text(base_global+'\n'+candidate.rstrip()+'\n')
    (edition/'docs/README.md').write_text(guide_after)
    (packet/'candidate.md').write_text(candidate)
    (packet/'docs_README_before.md').write_text(guide_before)
    (packet/'docs_README_after.md').write_text(guide_after)
    shutil.copyfile(root/'docs/NOTATION.md',packet/'NOTATION.md')
    dep_lines = base_global.splitlines(keepends=True)
    pieces = ['# Complete operative dependencies for the proposed C.4\n\n',
              'The following are unchanged full proof units from global_nonlinear.md.\n'
              'Section III.F in legacy cross-references denotes the contained Section 3\n'
              'finite-program conditioning/response argument reproduced here.\n'
              'Earlier section-specific activation constants do not replace C.1 or C.4\n'
              'hypotheses. No historical verdict is a premise.\n\n']
    for first,last in ((181,500),(1835,1893),(2449,3829)):
        pieces += [f'\n<!-- Exact source lines {first}--{last}; original section numbering. -->\n\n',
                   ''.join(dep_lines[first-1:last])]
    (packet/'dependencies.md').write_text(''.join(pieces))
    shutil.copyfile(study/'PROMOTION_REVIEW_ASSIGNMENT.md',packet/'assignment.md')
    manifest = {
        'author_assemblers': ['root','cubic_derivation','matching_remainder','quadrature_check'],
        'selector': 'relevance_selector',
        'scientific_base_hashes': expected,
        'source_head': subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),
        'candidate_source_sha256': digest(study/'PROMOTION_C4.md'),
        'assembler_sha256': digest(Path(__file__).resolve()),
        'copied_sources_sha256': {str(p.relative_to(root)):digest(p) for p in copied},
        'packet_sha256': {str(p.relative_to(packet)):digest(p) for p in sorted(packet.iterdir())},
        'edition_sha256': {str(p.relative_to(edition)):digest(p) for p in sorted(edition.rglob('*')) if p.is_file()},
        'destinations': ['docs/global_nonlinear.md: append C.4','docs/README.md: extend one table row'],
        'empirical_claims': False, 'code_changes': False,
    }
    (output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    checked = subprocess.run([sys.executable,'-B','code/tools/check_library.py'],cwd=edition,
                             capture_output=True,text=True)
    validation = {
        'command':[sys.executable,'-B','code/tools/check_library.py'],
        'cwd':str(edition), 'exit_status':checked.returncode,
        'stdout':checked.stdout,'stderr':checked.stderr,
        'scope':'standalone proof-only edition links/boundary; no code or empirical addition',
        'no_study_dependency_in_candidate': 'studies/' not in candidate,
        'old_global_prefix_preserved': (edition/'docs/global_nonlinear.md').read_text().startswith(base_global),
        'guide_changed_lines':sum(a!=b for a,b in zip(guide_before.splitlines(),guide_after.splitlines())),
    }
    (output/'validation.json').write_text(json.dumps(validation,indent=2)+'\n')
    print(json.dumps({'output':str(output),'manifest':manifest,'validation':validation},indent=2))
    if checked.returncode or not validation['no_study_dependency_in_candidate']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
