"""Assemble independently prepared promotion additions, without live edits.

This is integration-stage coordination, not a cross-study research dependency.
Only frozen proposals and their established baseline enter the edition.
"""
import argparse
import ast
import difflib
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[2]
OWNER = ROOT / 'data/generated/closure_endpoint_discrimination/promotion_20260916'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    out = parser.parse_args().output.resolve()
    if not out.is_relative_to(OWNER.resolve()):
        raise ValueError('assembled output must be in the originating generated namespace')
    circle_source = ROOT / 'studies/closure_endpoint_discrimination'
    circle_packet = json.loads((circle_source/'PROMOTION_CIRCLE_PACKET.json').read_text())
    circle = ROOT / circle_packet['edition']
    if digest(circle/'FROZEN_SHA256.json') != circle_packet['manifest_sha256']:
        raise ValueError('circle manifest changed')
    circle_hashes = json.loads((circle/'FROZEN_SHA256.json').read_text())
    for rel, expected in circle_hashes.items():
        if digest(circle/rel) != expected:
            raise ValueError(f'circle frozen input changed: {rel}')
    a_source = ROOT/'studies/first_order_dimension_mnist'
    a_manifest = json.loads((a_source/'PROMOTION_MANIFEST.json').read_text())
    a = Path(a_manifest['frozen_root'])
    for rel, expected in a_manifest['files'].items():
        if digest(a/rel) != expected:
            raise ValueError(f'general-p1 frozen input changed: {rel}')
    c_source = ROOT/'studies/closure_circle_spectral_mechanism'
    c_manifest = json.loads((c_source/'PROMOTION_MANIFEST_20260916.json').read_text())
    for rel, expected in c_manifest['frozen_inputs'].items():
        if digest(c_source/rel) != expected:
            raise ValueError(f'explanatory frozen input changed: {rel}')
    # Check all recorded established dependencies, including shared instructions.
    circle_targets = {v for v in circle_packet['source_mapping'].values() if v.startswith('code/')}
    circle_targets.add('code/README.md')
    for rel, expected in circle_hashes.items():
        if rel not in circle_targets and digest(ROOT/rel) != expected:
            raise ValueError(f'concurrent established change needs reassessment: {rel}')
    for rel, frozen in [('docs/README.md','dependencies/original_docs_README.md'),
                        ('code/README.md','dependencies/original_code_README.md')]:
        if (ROOT/rel).read_bytes() != (a/frozen).read_bytes():
            raise ValueError(f'concurrent guide change: {rel}')
    if digest(ROOT/'docs/global_nonlinear.md') != a_manifest['original_global_nonlinear_sha256']:
        raise ValueError('concurrent chapter change')
    out.mkdir(parents=True, exist_ok=False)
    baseline = {}
    for directory in ('docs','code'):
        shutil.copytree(ROOT/directory,out/directory,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        baseline.update({str(p.relative_to(out)):digest(p) for p in (out/directory).rglob('*') if p.is_file()})
    for name in ('AGENTS.md','RESEARCH_WORKFLOW.md'):
        shutil.copyfile(ROOT/name,out/name)
    mapping = []
    for source, destination in circle_packet['source_mapping'].items():
        if not destination.startswith('code/'):
            continue
        shutil.copyfile(circle/destination,out/destination)
        mapping.append(dict(origin='closure_endpoint_discrimination',source=str((circle/destination).relative_to(ROOT)),
                            destination=destination,sha256=digest(out/destination)))
    for source, destination in a_manifest['mapping'].items():
        if (out/destination).exists():
            raise ValueError(f'proposed addition already exists: {destination}')
        (out/destination).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(a/destination,out/destination)
        mapping.append(dict(origin='first_order_dimension_mnist',source=str((a/destination).relative_to(ROOT)),
                            destination=destination,sha256=digest(out/destination)))
    # Integration-only optional-dependency discovery adapter. Scientific test
    # bodies remain exactly those in the immutable paired-review packet.
    test_path = 'code/tests/test_general_p1.py'
    adapter = a_source/'PROMOTION_test_general_p1_optional.py'
    def test_bodies(text):
        return {node.name:ast.get_source_segment(text,node)
                for node in ast.walk(ast.parse(text))
                if isinstance(node,ast.FunctionDef) and node.name.startswith('test_')}
    if test_bodies(adapter.read_text()) != test_bodies((a/test_path).read_text()):
        raise ValueError('integration adapter changed scientific test bodies')
    shutil.copyfile(adapter,out/test_path)
    for row in mapping:
        if row['destination']==test_path:
            row.update(source=str(adapter.relative_to(ROOT)),sha256=digest(adapter),
                       operation='optional Torch discovery adapter; all 16 test bodies unchanged',
                       scientific_base_sha256=digest(a/test_path))
    # Preserve the exact independently frozen guide additions; no paraphrase.
    for rel, original in [('docs/README.md','dependencies/original_docs_README.md'),
                          ('code/README.md','dependencies/original_code_README.md')]:
        base = (a/original).read_bytes()
        proposed = (a/rel).read_bytes()
        if not proposed.startswith(base):
            raise ValueError('general-p1 guide edit is not a simple append')
        value = (circle/rel).read_bytes() if rel=='code/README.md' else base
        (out/rel).write_bytes(value+proposed[len(base):])
    base = (ROOT/'docs/global_nonlinear.md').read_text()
    if base != (c_source/'PROMOTION_BASE_CHAPTER_20260916.md').read_text():
        raise ValueError('explanatory chapter baseline differs')
    anchor = c_manifest['insertion_after']
    insertion = (c_source/'PROMOTION_INSERTION_20260916.md').read_text().strip()
    if base.count(anchor)!=1:
        raise ValueError('insertion anchor is not unique')
    chapter = base.replace(anchor,anchor+'\n\n'+insertion,1)
    if chapter.replace(anchor+'\n\n'+insertion,anchor,1)!=base:
        raise ValueError('chapter preservation failed')
    (out/'docs/global_nonlinear.md').write_text(chapter)
    for rel in ['code/README.md','docs/README.md','docs/global_nonlinear.md']:
        mapping.append(dict(destination=rel,sha256=digest(out/rel),operation='exact frozen append or insertion'))
    all_hashes = {str(p.relative_to(out)):digest(p) for directory in ('docs','code')
                  for p in sorted((out/directory).rglob('*')) if p.is_file()}
    all_hashes.update({name:digest(out/name) for name in ('AGENTS.md','RESEARCH_WORKFLOW.md')})
    changed = {row['destination'] for row in mapping}
    for rel, expected in baseline.items():
        if rel not in changed and all_hashes[rel]!=expected:
            raise ValueError(f'unrelated established file was altered: {rel}')
    record = dict(status='assembled_for_validation; scientific and integration gates remain independent',
                  mapping=mapping, baseline_sha256=baseline, preserved_unchanged_files=sum(rel not in changed for rel in baseline),
                  source_manifests={str(p.relative_to(ROOT)):digest(p) for p in
                    [circle/'FROZEN_SHA256.json',a_source/'PROMOTION_MANIFEST.json',c_source/'PROMOTION_MANIFEST_20260916.json']})
    (out/'ASSEMBLY.json').write_text(json.dumps(record,indent=2)+'\n')
    (out/'FROZEN_SHA256.json').write_text(json.dumps(all_hashes,indent=2)+'\n')
    baseline_files={}
    for rel in changed & baseline.keys():
        destination=out/'integration_inputs/baseline'/rel
        destination.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(ROOT/rel,destination)
        if digest(destination)!=baseline[rel]:raise ValueError('baseline changed during assembly: '+rel)
        baseline_files[str(destination.relative_to(out))]=baseline[rel]
    (out/'integration_inputs/BASELINE_SHA256.json').write_text(json.dumps(dict(sorted(baseline_files.items())),indent=2)+'\n')
    patch=[]
    for rel in sorted(changed):
        original=out/'integration_inputs/baseline'/rel
        before=original.read_text().splitlines(keepends=True) if original.exists() else []
        patch.extend(difflib.unified_diff(before,(out/rel).read_text().splitlines(keepends=True),
                     fromfile='a/'+rel if original.exists() else '/dev/null',tofile='b/'+rel))
    (out/'PROMOTION.diff').write_text(''.join(patch))
    print(json.dumps(dict(edition=str(out),manifest_sha256=digest(out/'FROZEN_SHA256.json'),
                         changed_files=len(changed),preserved_files=record['preserved_unchanged_files']),indent=2))


if __name__=='__main__':
    main()
