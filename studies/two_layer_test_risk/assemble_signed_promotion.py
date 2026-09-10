"""Freeze the signed canonical edition and complete review inputs.

Only selected documentation/tool files are copied, never the checkout or
index. All output must be a fresh study-owned generated directory.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    study = Path(__file__).resolve().parent
    root = study.parents[1]
    output = args.output.resolve()
    if not output.is_relative_to(root/'data/generated/two_layer_test_risk'):
        raise ValueError('Output must be in the study generated namespace')
    expected = {
        'docs/global_nonlinear.md':'8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101',
        'docs/README.md':'4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453',
        'docs/NOTATION.md':'199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b',
        'code/README.md':'00f5070d35a3e9fb9d0e9886f0f6d9f680a8d34bb32307807d1f88afc807a774',
    }
    for path, digest in expected.items():
        if sha(root/path) != digest:
            raise ValueError(f'Changed maintained dependency: {path}')
    mapping = {
        'PROMOTION_certificate.py':'code/tools/two_layer_risk/certificate.py',
        'certificate_kernel.cpp':'code/tools/two_layer_risk/certificate_kernel.cpp',
        'angle_error_bound.py':'code/tools/two_layer_risk/angle_error_bound.py',
        'PROMOTION_check_driver.py':'code/tools/two_layer_risk/check_driver.py',
        'PROMOTION_check_kernel.py':'code/tools/two_layer_risk/check_kernel.py',
        'PROMOTION_TOOL_GUIDE.md':'code/tools/two_layer_risk/README.md',
    }
    for name in (*mapping, 'PROMOTION_SIGN_C4_V2.md', 'PROMOTION_SIGN_DOCS_README.md',
                 'PROMOTION_CODE_README_APPENDIX.md', 'SIGNED_PROMOTION_ASSIGNMENT.md',
                 'SIGNED_INTEGRATION_ASSIGNMENT.md'):
        if not (study/name).is_file():
            raise ValueError(f'Missing complete candidate input: {name}')
    output.mkdir(parents=True, exist_ok=False)
    packet, edition = output/'packet', output/'edition'
    packet.mkdir()
    edition.mkdir()
    copied = sorted((root/'docs').glob('*.md')) + [root/'code/README.md', root/'code/tools/check_library.py']
    for source in copied:
        target = edition/source.relative_to(root)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    base = (root/'docs/global_nonlinear.md').read_text()
    candidate = (study/'PROMOTION_SIGN_C4_V2.md').read_text()
    (edition/'docs/global_nonlinear.md').write_text(base+'\n'+candidate.rstrip()+'\n')
    shutil.copyfile(study/'PROMOTION_SIGN_DOCS_README.md', edition/'docs/README.md')
    (edition/'code/README.md').write_text((root/'code/README.md').read_text()
                                       +'\n'+(study/'PROMOTION_CODE_README_APPENDIX.md').read_text())
    for source, destination in mapping.items():
        target = edition/destination
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(study/source, target)
    packet_map = {
        'candidate.md':study/'PROMOTION_SIGN_C4_V2.md',
        'docs_README_before.md':root/'docs/README.md',
        'docs_README_after.md':edition/'docs/README.md',
        'code_README_before.md':root/'code/README.md',
        'code_README_after.md':edition/'code/README.md',
        'NOTATION.md':root/'docs/NOTATION.md',
        'assignment.md':study/'SIGNED_PROMOTION_ASSIGNMENT.md',
        'integration_assignment.md':study/'SIGNED_INTEGRATION_ASSIGNMENT.md',
        'original_numerical_source.py':study/'certificate_driver.py',
    }
    for destination, source in packet_map.items():
        shutil.copyfile(source, packet/destination)
    for source, destination in mapping.items():
        shutil.copyfile(edition/destination, packet/Path(destination).name)
    lines = base.splitlines(keepends=True)
    deps = ['# Complete operative dependencies\n\n',
            'Unchanged full proof units of global_nonlinear.md. Legacy III.F\n'
            'denotes the contained Section 3 conditioning/response proof.\n'
            'C.4 retains its own activation and normalization hypotheses.\n\n']
    for first, last in ((181,500),(1835,1893),(2449,3829)):
        deps += [f'\n<!-- Original lines {first}--{last}. -->\n\n', ''.join(lines[first-1:last])]
    (packet/'dependencies.md').write_text(''.join(deps))
    evidence = output/'evidence'
    evidence.mkdir()
    runs = ['certificate_20260910_01', 'certificate_reproduction_20260910_01']
    for run in runs:
        source = root/'data/generated/two_layer_test_risk'/run
        if not (source/'result.json').is_file():
            raise ValueError(f'Missing executed coefficient evidence: {run}')
        for item in sorted(source.rglob('*')):
            if item.is_file() and item.name != 'certificate_kernel':
                target = evidence/run/item.relative_to(source)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(item,target)
    check = subprocess.run([sys.executable,'-B','code/tools/check_library.py'], cwd=edition,
                           text=True,capture_output=True)
    validation = {'command':[sys.executable,'-B','code/tools/check_library.py'],
                  'returncode':check.returncode,'stdout':check.stdout,'stderr':check.stderr}
    (output/'validation.json').write_text(json.dumps(validation,indent=2)+'\n')
    originals = {str(path.relative_to(root)):sha(path) for path in copied}
    source_names = set(mapping) | {'PROMOTION_SIGN_C4_V2.md','PROMOTION_SIGN_DOCS_README.md',
                                  'PROMOTION_CODE_README_APPENDIX.md','SIGNED_PROMOTION_ASSIGNMENT.md',
                                  'SIGNED_INTEGRATION_ASSIGNMENT.md','certificate_driver.py',
                                  'build_signed_candidate.py','canonicalize_signed_candidate.py'}
    manifest = {
        'authors_assemblers':['root','cubic_derivation','matching_remainder','quadrature_check',
                             'sign_structure','certified_error','certification_engine','sign_code_assembly',
                             'signed_notation_assembly'],
        'selector':'sign_relevance', 'scientific_base_sha256':expected,
        'source_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),
        'source_sha256':{name:sha(study/name) for name in sorted(source_names)},
        'assembler_sha256':sha(Path(__file__).resolve()), 'copied_base_sha256':originals,
        'destination_mapping':mapping,
        'packet_sha256':{str(p.relative_to(packet)):sha(p) for p in sorted(packet.rglob('*')) if p.is_file()},
        'edition_sha256':{str(p.relative_to(edition)):sha(p) for p in sorted(edition.rglob('*')) if p.is_file()},
        'evidence_sha256':{str(p.relative_to(evidence)):sha(p) for p in sorted(evidence.rglob('*')) if p.is_file()},
        'empirical_training_claims':False,
        'computer_assisted_proof':True,
        'additional_coefficient_runs_authorized':False,
    }
    (output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'output':str(output),'manifest_sha256':sha(output/'manifest.json'),
                      'packet_files':len(manifest['packet_sha256']),
                      'edition_files':len(manifest['edition_sha256']),
                      'evidence_files':len(manifest['evidence_sha256']),
                      'structural_check_returncode':check.returncode},indent=2))
    if check.returncode:
        raise SystemExit(check.returncode)


if __name__ == '__main__':
    main()
