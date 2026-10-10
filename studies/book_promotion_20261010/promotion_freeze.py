"""Retain an exact, verdict-free review packet and explicit reading scopes."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import tarfile

STUDY = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('edition', type=Path)
    parser.add_argument('--version', type=int, required=True)
    args = parser.parse_args()
    edition = args.edition.resolve()
    archive_path = STUDY/f'promotion_packet_v{args.version}.tar.gz'
    if archive_path.exists():
        raise ValueError('Frozen packets must not be overwritten')
    contents, roles = {}, {}
    for row in json.loads((edition/'edition_sources.json').read_text()):
        p = edition/row['path']
        data = p.read_bytes()
        if hashlib.sha256(data).hexdigest() != row['sha256']:
            raise ValueError(f'Edition changed: {p}')
        contents['edition/'+row['path']] = data
    for name in ('AGENTS.md', 'RESEARCH_WORKFLOW.md'):
        contents['edition/'+name] = (edition/name).read_bytes()
        roles['edition/'+name] = 'complete instructions'
    for name in ('promotion_compression.qmd', 'promotion_09.qmd', 'promotion_10.qmd', 'promotion_12.qmd', 'promotion_13.qmd'):
        path = 'additions/'+name
        contents[path] = (STUDY/name).read_bytes()
        roles[path] = 'complete proposed mathematical addition'
    with tarfile.open(STUDY/'promotion_book_dependencies.tar.gz') as source:
        for member in source.getmembers():
            contents[member.name] = source.extractfile(member).read()
            roles[member.name] = 'complete established mathematical dependency passage'
    with tarfile.open(STUDY/'promotion_code.tar.gz') as source:
        for member in source.getmembers():
            roles['edition/'+member.name] = 'complete proposed code/test/guide (README supplied in full)'
    dependencies = ('__init__ finite_network finite_torch gaussian_moments observable_arithmetic '
                    'observable_compiler observable_fixed observable_initialization observable_p1_initialization '
                    'observable_solver observable_torch_p1 observable_words closure_comparison').split()
    for name in dependencies:
        roles[f'edition/code/pde/{name}.py'] = 'complete established code dependency'
    for name in ('docs/index.qmd', 'docs/notation.qmd', 'docs/_quarto.yml', 'code/GENERAL_P1.md'):
        roles['edition/'+name] = 'complete notation/navigation/API guide'
    contents['assignment.md'] = (STUDY/'promotion_review_assignment.md').read_bytes()
    roles['assignment.md'] = 'complete neutral assignment'
    rows = [dict(path=p, sha256=hashlib.sha256(b).hexdigest(), bytes=len(b),
                 read_scope=roles.get(p, 'frozen standalone build input; no fresh whole-book or unrelated-code audit'))
            for p,b in sorted(contents.items())]
    metadata = dict(version=args.version, authors_and_assemblers=[
        'Amir Joudaki (compact source byline)', '/root', '/root/assemble_compression_core',
        '/root/assemble_dictionary_core', '/root/assemble_older_theory', '/root/assemble_data_core',
        '/root/assemble_visual_core', '/root/radial_bundle_adapter', '/root/draft_compression_chapter',
        '/root/draft_older_chapters', '/root/draft_code_package'],
        provenance_note='Historical sources remain identified by the originating manifests; historical agent identities are not completely enumerated. Reviewers must be newly created contexts with no participation or inherited material.',
        selector='/root/promotion_screen', files=rows,
        preservation='Existing chapter bodies unchanged apart from inserted sections, title ordinals and navigation; additions are separately provided for full review without rereading whole destination chapters.',
        scientific_scope='All proposed additions and full listed dependencies. Standard numerical/browser packages are external software dependencies; all custom code is in scope.')
    contents['inputs.json'] = (json.dumps(metadata, indent=2)+'\n').encode()
    with tarfile.open(archive_path, 'w:gz') as archive:
        for path,data in sorted(contents.items()):
            member = tarfile.TarInfo(path); member.size=len(data); member.mode=0o644
            archive.addfile(member, io.BytesIO(data))
    receipt = dict(packet=archive_path.name, sha256=hashlib.sha256(archive_path.read_bytes()).hexdigest(), **metadata)
    (STUDY/f'promotion_review_inputs_v{args.version}.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(archive_path)


if __name__ == '__main__':
    main()
