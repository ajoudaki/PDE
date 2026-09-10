#!/usr/bin/env python3
"""Freeze the full signed-study review inputs without author verdicts."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

STUDY=Path(__file__).resolve().parent
ROOT=STUDY.parents[1]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();out=args.output.resolve()
    assert out.is_relative_to(ROOT/'data/generated/two_layer_test_risk')
    out.mkdir(parents=True,exist_ok=False);packet=out/'packet';packet.mkdir()
    source_files=['SIGN_THEOREM.md','PROMOTION_C4.md','CUBIC_DERIVATION.md',
                  'MATCHING_AND_REMAINDER.md','RESULT.md','CERTIFIED_ERROR.md',
                  'CERTIFICATION_ENGINE.md','ANGULAR_CERTIFICATE.md',
                  'DRIVER_CERTIFICATION.md','certificate_driver.py','certificate_kernel.cpp',
                  'angle_error_bound.py','check_certificate_kernel.py','check_certificate_driver.py']
    stops={'SIGN_THEOREM.md':'## Reproduction and supersession',
           'CUBIC_DERIVATION.md':'## Status, attacks, and exact remaining obligation',
           'MATCHING_AND_REMAINDER.md':'## 9. Source coverage, checks, and limitations',
           'CERTIFIED_ERROR.md':'## Scope and provenance',
           'CERTIFICATION_ENGINE.md':'## Executed deterministic verification',
           'DRIVER_CERTIFICATION.md':'## Reproduction and ownership'}
    edits={};original={}
    for name in source_files:
        src=STUDY/name;original[name]=sha(src);body=src.read_text();changes=[]
        if name in stops:
            assert stops[name] in body
            body=body.split(stops[name])[0];changes.append('administrative ending omitted at '+stops[name])
        if name=='SIGN_THEOREM.md':
            body=body[:body.index('\n\n')]+ '\n\n'+body[body.index('## Fixed model and comparison'):]
            changes.append('candidate-check-status preface omitted')
        if name=='RESULT.md':
            body=body[body.index('## Hidden movement and activation nonaffinity'):body.index('## Evidence, effect size and terminal obligation')]
            changes.append('only complete hidden-movement/nonaffinity proof is a dependency')
        if name=='DRIVER_CERTIFICATION.md':
            a=body.index('An exact rational scalar is multiplied')
            b=body.index('\n\nPi is enclosed',a)
            body=body[:a]+('Exact rational scalar multiplication applies the scalar to endpoints\n'
                          'before outward rounding; the driver tests trigonometric enclosure widths.\n')+body[b:]
            body=body.replace('KERNEL_REVIEW and the deterministic\nkernel test provide independent verification, separately from that proof.\n','')
            changes.append('preflight-review history/reference removed; exact scalar semantics retained')
        (packet/name).write_text(body)
        edits[name]=changes
    assignment=STUDY/'SIGN_REVIEW_ASSIGNMENT.md'
    shutil.copyfile(assignment,packet/'assignment.md')
    old=ROOT/'data/generated/two_layer_test_risk/promotion_v1/packet/dependencies.md'
    assert sha(old)=='8378046bc80abc06077b34182141d282cf0ba6ac6d7fde6c84e2c6bab5b19db7'
    shutil.copyfile(old,packet/'dependencies.md')
    for name in ('NOTATION.md','README.md'):
        shutil.copyfile(ROOT/'docs'/name,packet/('docs_'+name))
    # Only generated evidence is copied, never the checkout or Git metadata.
    run=ROOT/'data/generated/two_layer_test_risk/certificate_20260910_01'
    evidence=out/'evidence';evidence.mkdir()
    for p in run.rglob('*'):
        if p.is_file() and p.name!='certificate_kernel':
            target=evidence/'production'/p.relative_to(run)
            target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
    for name in ('kernel_check_20260910_01','driver_check_20260910_03','angle_bound_20260910_01'):
        source=ROOT/'data/generated/two_layer_test_risk'/name
        for p in source.iterdir():
            if p.is_file() and p.suffix in ('.json','.log'):
                target=evidence/name/p.name;target.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(p,target)
    manifest={'authors_assemblers':['root','cubic_derivation','matching_remainder','quadrature_check',
                                   'sign_structure','certified_error','certification_engine'],
              'original_source_sha256':original,'packet_adjustments':edits,
              'assignment_source_sha256':sha(assignment),'assembler_sha256':sha(__file__),
              'source_head':'df1117948764a984e7fd2d28949a3c87bc284f84',
              'scientific_book_sources':{name:sha(ROOT/name) for name in
                  ('docs/global_nonlinear.md','docs/finite_dynamics.md','docs/gaussian_calculus.md',
                   'docs/NOTATION.md','docs/README.md')},
              'packet_sha256':{str(p.relative_to(packet)):sha(p) for p in sorted(packet.rglob('*')) if p.is_file()},
              'evidence_sha256':{str(p.relative_to(evidence)):sha(p) for p in sorted(evidence.rglob('*')) if p.is_file()}}
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'packet_files':len(manifest['packet_sha256']),
                      'evidence_files':len(manifest['evidence_sha256']),
                      'manifest_sha256':sha(out/'manifest.json')},indent=2))


if __name__=='__main__':main()
