"""Check edition identifiers/references and preserve the frozen book paragraphs."""
import argparse
import collections
import json
from pathlib import Path
import re
import subprocess
import sys
import tarfile


def check(root):
    root = Path(root).resolve()
    errors, targets, refs, links = [], collections.defaultdict(list), [], []
    if re.search(r'(?m)^header-includes:', (root/'docs/_quarto.yml').read_text()):
        errors.append('Raw TeX header includes must be scoped to PDF/LaTeX formats')
    for path in sorted((root/'docs').glob('*.qmd')):
        text = path.read_text()
        if re.search(r'^\s*:+\s*\{[^}\n]*#proof-[^}\n]*\.proof', text, re.M):
            errors.append(f'{path.name}: proof IDs must be preceding anchor spans, not identifiers on proof divisions')
        for match in re.finditer(r'\{[^}\n]*#([\w:-]+)[^}\n]*\}', text):
            targets[match[1]].append(path.name)
        for match in re.finditer(r'(?<!\w)@((?:sec|eq|thm|lem|prp|cor|def|rem|fig|tbl|ch)-[\w-]+)', text):
            refs.append((match[1], path.name))
        for match in re.finditer(r'\]\(([^\s)#]*\.qmd)?#([\w:-]+)\)', text):
            links.append((match[2], match[1], path.name))
    for target, paths in targets.items():
        if len(paths) != 1:
            errors.append(f'duplicate ID {target}: {paths}')
    for target, path in refs:
        if target not in targets:
            errors.append(f'missing target {target} in {path}')
    for target, destination, path in links:
        if target not in targets:
            errors.append(f'missing linked target {target} in {path}')
        elif destination and Path(destination).name not in targets[target]:
            errors.append(f'linked target {target} is not in {destination} from {path}')
    result = subprocess.run([sys.executable, str(root/'code/tools/check_library.py')],
                            cwd=root, capture_output=True, text=True)
    if result.returncode:
        errors.append(result.stderr.strip())
    study = Path(__file__).resolve().parent
    for fragment in study.glob('promotion_*.qmd'):
        if re.search(r'@sec-[\w-]+', fragment.read_text()):
            errors.append(f'{fragment.name}: use named links for unnumbered sections')
    allowed = {'docs/index.qmd', 'docs/_quarto.yml', 'code/README.md', 'code/tools/check_library.py'}
    additions = {'docs/09-trainability.qmd', 'docs/10-correlated-pairs.qmd',
                 'docs/12-three-sample-learning.qmd', 'docs/13-predictor-selection.qmd'}
    with tarfile.open(study/'promotion_base.tar.gz') as archive:
        for member in archive.getmembers():
            if member.name in allowed or not member.name.startswith(('docs/', 'code/')):
                continue
            old = archive.extractfile(member).read()
            new = (root/member.name).read_bytes()
            if member.name.startswith('docs/'):
                expected = re.sub(rb'\A# (9|10|11|12|13|14)\. ', lambda m: f'# {int(m[1])+1}. '.encode(), old)
                if member.name in additions:
                    number = Path(member.name).name[:2]
                    fragment = (study/f'promotion_{number}.qmd').read_bytes().rstrip()+b'\n\n'
                    new = new.replace(fragment, b'', 1)
                    preserved = new.rstrip() == expected.rstrip()
                else:
                    preserved = new == expected
            elif member.name == 'code/tools/two_layer_risk/README.md':
                preserved = new == old.replace(b'the scoped comparison in Chapter 14', b'the scoped test-risk comparison')
            else:
                preserved = new == old
            if not preserved:
                errors.append(f'changed previous content: {member.name}')
    report = dict(errors=errors, identifiers=len(targets), native_reference_uses=len(refs),
                  named_fragment_links=len(links),
                  library_check=result.stdout.strip(), preservation='byte comparison with frozen base')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('edition', type=Path)
    args = parser.parse_args()
    report = check(args.edition)
    print(json.dumps(report, indent=2))
    raise SystemExit(bool(report['errors']))
