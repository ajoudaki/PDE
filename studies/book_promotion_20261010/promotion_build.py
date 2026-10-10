"""Assemble the proposed edition from retained source snapshots, never live edits."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import tarfile


STUDY = Path(__file__).resolve().parent


def extract(archive, destination):
    with tarfile.open(archive) as source:
        for member in source.getmembers():
            name = Path(member.name)
            if name.is_absolute() or '..' in name.parts or not member.isfile():
                raise ValueError(f'Unexpected archive member: {member.name}')
            target = destination/name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.extractfile(member).read())


def assemble(destination):
    destination.mkdir(parents=True, exist_ok=False)
    extract(STUDY/'promotion_base.tar.gz', destination)
    extract(STUDY/'promotion_code.tar.gz', destination)
    docs = destination/'docs'
    additions = {'09': '09-trainability.qmd', '10': '10-correlated-pairs.qmd',
                 '12': '12-three-sample-learning.qmd', '13': '13-predictor-selection.qmd'}
    for number, name in additions.items():
        p = docs/name
        text = p.read_text()
        added = (STUDY/f'promotion_{number}.qmd').read_text().rstrip()+'\n\n'
        if number == '13':
            position = text.index('<!-- moved verbatim')
        elif number == '12':
            position = text.index('## Scope of the completed families')
        else:
            position = len(text)
            text = text.rstrip()+'\n\n'
            position = len(text)
        p.write_text(text[:position]+added+text[position:])
    (docs/'08b-trajectory-compression.qmd').write_bytes((STUDY/'promotion_compression.qmd').read_bytes())
    for p in docs.glob('*.qmd'):
        text = p.read_text()
        if p.name == '08b-trajectory-compression.qmd':
            text = text.replace('# Complete-trajectory', '# 9. Complete-trajectory', 1)
        else:
            text = re.sub(r'\A# (9|10|11|12|13|14)\. ', lambda m: f'# {int(m[1])+1}. ', text)
        p.write_text(text)
    for relative in ('code/README.md', 'code/tools/two_layer_risk/README.md'):
        p = destination/relative
        p.write_text(p.read_text().replace('the scoped comparison in Chapter 14', 'the scoped test-risk comparison'))
    config = docs/'_quarto.yml'
    text = config.read_text().replace('        - 08-autonomous-computation.qmd\n',
        '        - 08-autonomous-computation.qmd\n        - 08b-trajectory-compression.qmd\n')
    text = text.replace('  type: book\n',
                        '  type: book\n  post-render:\n    - python package_code_links.py\n', 1)
    (docs/'package_code_links.py').write_bytes((STUDY/'promotion_package_code_links.py').read_bytes())
    (docs/'print_code_links.lua').write_bytes((STUDY/'promotion_print_code_links.lua').read_bytes())
    text = text.replace('      - pdf_breakable_tables.lua\n',
                        '      - pdf_breakable_tables.lua\n      - print_code_links.lua\n')
    # Raw TeX header includes must never be inserted into HTML's body.
    headers = re.search(r'(?m)^header-includes:\n(?:[ \t].*\n)+', text)
    if headers:
        block = ''.join('    '+line for line in headers[0].splitlines(keepends=True))
        text = text[:headers.start()]+text[headers.end():]
        for format_name in ('pdf', 'latex'):
            marker = f'  {format_name}:\n'
            if text.count(marker) != 1:
                raise ValueError(f'Expected one {format_name} format configuration')
            text = text.replace(marker, marker+block)
    config.write_text(text)
    index = docs/'index.qmd'
    text = index.read_text()
    boundary = '\n### III. Nonlinear learning and inductive bias'
    entry = ('\n9. [Complete-trajectory compression](08b-trajectory-compression.qmd#ch-trajectory-compression)\n')
    text = text.replace(boundary, entry+boundary)
    # Preserve all existing scientific text; update the hand-written reading list.
    for old in range(14, 8, -1):
        text = text.replace(f'\n{old}. [', f'\n{old+1}. [') if old != 9 else text
    text = text.replace('\n9. [Trainability', '\n10. [Trainability')
    index.write_text(text)
    paths = sorted(p for folder in ('docs', 'code') for p in (destination/folder).rglob('*') if p.is_file())
    manifest = [dict(path=str(p.relative_to(destination)),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in paths]
    (destination/'edition_sources.json').write_text(json.dumps(manifest, indent=2)+'\n')
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    print(f'{len(assemble(args.out))} files assembled at {args.out}')
