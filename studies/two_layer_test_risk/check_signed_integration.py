#!/usr/bin/env python3
"""Fresh frozen-edition integration checks; never evaluate a coefficient grid.

Each invocation has a 60 CPU-second limit. 'replay' reconstructs saved bits
and rational enclosures, without calling the C++ kernel or a Gaussian rule.
"""
import argparse
import ast
from collections import Counter
import difflib
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import re
import resource
import subprocess
import sys
import time
from unittest.mock import patch

BASE = Path(__file__).resolve().parents[2]
FROZEN = BASE / 'data/generated/two_layer_test_risk/signed_promotion_v1'
EDITION = FROZEN / 'edition'
PACKET = FROZEN / 'packet'
SCRATCH = FROZEN / 'integration'
EXPECTED = 'bef8b4af500bfef3e8a5f4234e239ac68e30c5891841280b0f38be55bfb2ffb3'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def readj(path):
    return json.loads(Path(path).read_text())

def module():
    path = EDITION / 'code/tools/two_layer_risk/certificate.py'
    spec = importlib.util.spec_from_file_location('integration_certificate', path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

def structure():
    manifest = readj(FROZEN / 'manifest.json')
    assert sha(FROZEN / 'manifest.json') == EXPECTED
    counts = {}
    verified = {}
    for group in ('packet', 'edition', 'evidence'):
        expected = manifest[group + '_sha256']
        actual = {str(p.relative_to(FROZEN / group)): sha(p)
                  for p in (FROZEN / group).rglob('*') if p.is_file()}
        assert actual == expected, (group, set(actual) ^ set(expected))
        counts[group] = len(actual)
        verified[group] = actual
    chapter = (EDITION / 'docs/global_nonlinear.md').read_bytes()
    addition = (PACKET / 'candidate.md').read_bytes()
    pos = chapter.index(addition)
    assert chapter[pos:] == addition
    old = chapter[:pos - 1]
    assert chapter[pos - 1:pos] == b'\n'
    assert hashlib.sha256(old).hexdigest() == manifest['copied_base_sha256']['docs/global_nonlinear.md']
    assert len(old.splitlines()) == 3829
    unchanged = []
    for name, expected in manifest['copied_base_sha256'].items():
        if name == 'docs/global_nonlinear.md':
            continue
        alternative = {'docs/README.md': 'docs_README_before.md',
                       'code/README.md': 'code_README_before.md'}.get(name)
        supplied = PACKET / alternative if alternative else EDITION / name
        assert sha(supplied) == expected
        if alternative is None:
            unchanged.append(name)
    packet_for = {'PROMOTION_certificate.py': 'certificate.py',
                  'PROMOTION_check_driver.py': 'check_driver.py',
                  'PROMOTION_check_kernel.py': 'check_kernel.py',
                  'PROMOTION_TOOL_GUIDE.md': 'README.md'}
    for source, dest in manifest['destination_mapping'].items():
        p = PACKET / packet_for.get(source, source)
        assert sha(p) == manifest['source_sha256'][source] == sha(EDITION / dest)
    for doc in ('code', 'docs'):
        assert (PACKET / (doc + '_README_after.md')).read_bytes() == (EDITION / doc / 'README.md').read_bytes()
    assert (PACKET / 'code_README_after.md').read_bytes().startswith((PACKET / 'code_README_before.md').read_bytes())
    dependency = (PACKET / 'dependencies.md').read_text()
    spans = list(re.finditer(r'<!-- Original lines (\d+)--(\d+)\. -->\n\n', dependency))
    original = old.decode().splitlines(keepends=True)
    dependency_ranges = []
    for j, match in enumerate(spans):
        lo, hi = map(int, match.groups())
        actual = dependency[match.end():spans[j+1].start() if j+1 < len(spans) else len(dependency)]
        expected = ''.join(original[lo-1:hi])
        assert actual.strip() == expected.strip(), (lo,hi)
        dependency_ranges.append([lo,hi])
    tags = re.findall(r'\\tag\{(C4\.[^}]+)\}', addition.decode())
    assert len(tags) == len(set(tags))
    assert not re.findall(r'\\tag\{C4\.', old.decode())
    references = set(re.findall(r'\((C4\.[A-Z]?\d+[a-z]?)\)', addition.decode()))
    assert references <= set(tags), references - set(tags)
    # Fresh independent scanner, restricted to the nine proposed destinations.
    changed = ['docs/global_nonlinear.md', 'docs/README.md', 'code/README.md'] + list(manifest['destination_mapping'].values())
    links = []
    for name in changed:
        if not name.endswith('.md'):
            continue
        p = EDITION / name
        text = p.read_text()
        if name == 'docs/global_nonlinear.md':
            text = addition.decode()
        text = re.sub(r'^```[^\n]*\n.*?^```[^\n]*$', '', text, flags=re.M|re.S)
        text = re.sub(r'\\\[.*?\\\]|\\\(.*?\\\)', '', text, flags=re.S)
        text = re.sub(r'`+[^`\n]*`+', '', text)
        for target in re.findall(r'\]\(([^)\n]+)\)', text):
            if target.startswith(('https://','http://','mailto:')):
                continue
            location, _, fragment = target.partition('#')
            dest = (p.parent / location).resolve() if location else p
            assert dest.is_relative_to(EDITION) and dest.is_file(), (name,target)
            if fragment:
                headings = re.findall(r'^#{1,6}\s+(.+)$',dest.read_text(),re.M)
                slugs = {re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in headings}
                assert fragment in slugs or f'id="{fragment}"' in dest.read_text(), (name,target)
            links.append([name,target])
    oldtree = ast.parse((PACKET / 'original_numerical_source.py').read_text())
    newtree = ast.parse((PACKET / 'certificate.py').read_text())
    def funcs(tree):
        return {n.name:n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
    oldf,newf = funcs(oldtree),funcs(newtree)
    identical=[]
    for name in oldf:
        if name == 'run':
            continue
        a,b=oldf[name],newf[name]
        if name == 'grid':
            a.body=a.body[1:];b.body=b.body[1:]
        assert ast.dump(a,include_attributes=False)==ast.dump(b,include_attributes=False), name
        identical.append(name)
    def loop(tree):
        return next(n for n in ast.walk(funcs(tree)['run'])
                    if isinstance(n,ast.For) and ast.unparse(n.target)=='j')
    assert ast.dump(loop(oldtree),include_attributes=False)==ast.dump(loop(newtree),include_attributes=False)
    diff=list(difflib.unified_diff((PACKET/'original_numerical_source.py').read_text().splitlines(),
                                  (PACKET/'certificate.py').read_text().splitlines(),lineterm=''))
    (SCRATCH/'numerical_source.diff').write_text('\n'.join(diff)+'\n')
    (SCRATCH/'verified_hashes.json').write_text(json.dumps(verified,indent=2)+'\n')
    return dict(counts=counts,old_chapter_bytes=len(old),old_chapter_lines=len(original),
                new_chapter_lines=len(addition.splitlines()),unchanged_base=unchanged,
                dependency_ranges=dependency_ranges,destinations=changed,unique_new_tags=len(tags),
                checked_local_links=links,identical_computation_units=identical,
                full_numerical_angle_loop_ast_identical=True)

def replay(run):
    d=module(); root=FROZEN/'evidence'/run
    pi,p,normal,nf=d.constants();pf=[v.midfloat() for v in p]
    constants={'pi':pi.json(),'p':[v.json() for v in p],
               'normal':normal.json(),'normal_float_bits':d.bits(nf)}
    assert constants == readj(root/'constants.json')
    totals={k:d.I(0) for k in ('nodal_sum','raw_nodal_projection','clock_nodal_subtraction')}
    common=None;nodes=0;rows=[];input_count=0;output_scalars=0
    meta=readj(root/'metadata.json')
    assert meta['source_sha256']['certificate_driver.py']==sha(PACKET/'original_numerical_source.py')
    assert meta['source_sha256']['certificate_kernel.cpp']==sha(PACKET/'certificate_kernel.cpp')
    assert meta['result_sha256']==sha(root/'result.json')
    result=readj(root/'result.json')
    assert meta['configuration']['target']==26
    assert meta['configuration']['angles']==256 and meta['configuration']['evaluated_indices']==list(range(64))
    assert meta['compile_command'][1:5]==['-O3','-std=c++17','-fno-fast-math','-ffp-contract=off']
    maxeps=F(0)
    for j in range(64):
        folder=root/f'angle_{j:03d}'
        u=d.directions(pi,j);uf=[[v.midfloat() for v in row] for row in u]
        lowraw=readj(folder/'lower_stdout.json')
        factor,var=d.root_factor(lowraw)
        for mode,matrix in [('lower',uf),('upper',factor)]:
            counts,steps,grid=d.grid(matrix,26)
            real=steps+[nf]+[float(v) for row in matrix for v in row]
            if mode=='upper':real+=pf
            body=mode+'\n'+' '.join(map(str,counts))+'\n'+' '.join(format(v,'.17g') for v in real)+'\n'
            assert body==(folder/(mode+'_input.txt')).read_text(),(run,j,mode,'regenerated input')
            raw=readj(folder/(mode+'_stdout.json')); audit=readj(folder/(mode+'_audit.json'))
            assert raw['mode']==mode
            assert raw['parsed_input_bits']==[d.bits(v) for v in real]
            assert raw['long_double_mantissa_bits']>=64
            assert raw['total_points']==math.prod(2*m+1 for m in counts)
            assert raw['outer_points']==math.prod(2*m+1 for m in (counts[:3] if mode=='upper' else counts))
            assert audit['grid']==grid
            assert audit['input_sha256']==sha(folder/(mode+'_input.txt'))
            assert audit['output_sha256']==sha(folder/(mode+'_stdout.json'))
            assert (folder/(mode+'_stderr.txt')).read_bytes()==b''
            assert all(abs(F(d.unbits(b))-1)<F(1,10**8) for b in raw['grid_mass_bits'])
            input_count+=len(real)
            for key,values in raw.items():
                if key.endswith('_bits') and isinstance(values,list):
                    assert all(math.isfinite(d.unbits(b)) for b in values)
                    output_scalars+=len(values)
        low=d.lower_intervals(lowraw,u,uf,26)
        high=d.upper_intervals(readj(folder/'upper_stdout.json'),low,factor,p,pf,26)
        c=d.contraction(low,high,p)
        common=c['beta'] if common is None else d.I(max(common.lo,c['beta'].lo),min(common.hi,c['beta'].hi))
        teacher=d.trig(6*pi*F(j,256),'cos');weight=F(2 if j==0 else 4,256)
        rawterm=2*weight*teacher*c['J'];clockterm=2*weight*teacher*c['beta']*c['a']
        totals['nodal_sum']+=rawterm-clockterm
        totals['raw_nodal_projection']+=rawterm
        totals['clock_nodal_subtraction']+=clockterm
        row=readj(folder/'enclosure.json')
        assert row==result['rows'][j]
        for key,value in c.items():assert row['moments'][key]==value.json(),(run,j,key)
        assert row['teacher']==teacher.json()
        assert row['alpha']==(2*pi*F(j,256)).json()
        assert row['heuristic_conditional_variance']==var
        assert row['weighted_raw']==rawterm.json() and row['weighted_clock']==clockterm.json()
        assert row['cumulative']==totals['nodal_sum'].json()
        assert row['epsilon_first_covariance']==str(low['epsilon_first_covariance'])
        assert row['epsilon_upper_covariance']==str(high['epsilon_upper_covariance'])
        assert row['epsilon_labels']==str(high['epsilon_labels'])
        maxeps=max(maxeps,high['epsilon_upper_covariance'])
        nodes+=row['upper_points'];rows.append(j)
    for key,value in totals.items():assert result[key]==value.json()
    chi=totals['nodal_sum'].widen(d.ANGLE_ERROR)
    assert result['chi']==chi.json() and result['beta_intersection']==common.json()
    assert result['max_upper_covariance_error']==str(maxeps)
    assert result['total_upper_nodes']==nodes==86101134
    assert F(27,100000)<chi.lo<=chi.hi<F(273,1000000)
    assert F(35309,1000000)<common.lo<=common.hi<F(35311,1000000)
    return dict(run=run,rows=rows,regenerated_real_input_bits=input_count,
                checked_output_bits=output_scalars,total_upper_nodes=nodes,chi=chi.json(),
                beta=common.json(),raw_projection=totals['raw_nodal_projection'].json(),
                clock_subtraction=totals['clock_nodal_subtraction'].json(),
                result_sha256=sha(root/'result.json'),recorded_cpu_seconds=meta['cpu_seconds'],
                no_kernel_execution=True)

def api():
    env=dict(os.environ);d=module();assert dict(os.environ)==env
    api_root=SCRATCH/'api_fixtures';api_root.mkdir()
    cases=[]
    def reject(output,target,kind):
        try:d.certify(output,target)
        except kind:cases.append([repr(output),repr(target),kind.__name__])
        else:raise AssertionError((output,target,kind))
    fresh=api_root/'must_not_exist'
    for target in [True,False,26.,'26',F(26)]:reject(fresh,target,TypeError)
    for target in [0,25,27,31]:reject(fresh,target,ValueError)
    for output in [None,12,b'bytes']:reject(output,26,TypeError)
    for output in ['', 'bad\x00path']:reject(output,26,ValueError)
    existing=api_root/'api_existing';existing.mkdir()
    reject(existing,26,FileExistsError)
    existingfile=api_root/'api_existing_file';existingfile.write_text('untouched')
    reject(existingfile,26,FileExistsError)
    dangling=api_root/'api_dangling';dangling.symlink_to(api_root/'missing_target')
    reject(dangling,26,FileExistsError)
    with patch.object(d.sys,'platform','not-linux'):reject(fresh,26,RuntimeError)
    assert not fresh.exists()
    out=api_root/'api_simulated_success'
    payload={'decision':'INCONCLUSIVE','chi':{'lo':'-1/10','hi':'1/10'},'nested':{'values':[1]}}
    commands=[]
    def fake_worker(command,*,env,check):
        assert check is True
        assert all(env[k]=='1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'))
        assert command==[sys.executable,'-B',str(d.SOURCE),'--output',str(out),'--target','26','--_worker']
        commands.append(command);out.mkdir();(out/'result.json').write_text(json.dumps(payload))
        return subprocess.CompletedProcess(command,0)
    with patch.object(d.subprocess,'run',fake_worker):answer=d.certify(out)
    assert answer==payload
    answer['nested']['values'].append(2)
    assert readj(out/'result.json')==payload and dict(os.environ)==env
    # Exercise the actual public worker's failure retention without compiling,
    # calculating, calling Git, or reading archived arrays.
    fakebin=api_root/'compiler_failure_bin';fakebin.mkdir()
    fakecompiler=fakebin/'g++'
    fakecompiler.write_text('#!/bin/sh\nif [ "$1" = "--version" ]; then\n  echo "integration failure fixture"\n  exit 0\nfi\necho "intentional compile failure" >&2\nexit 9\n')
    fakecompiler.chmod(0o755)
    failure=api_root/'actual_worker_failure'
    with patch.dict(os.environ,{'PATH':str(fakebin)}):
        env2=dict(os.environ)
        reject(failure,26,subprocess.CalledProcessError)
        assert dict(os.environ)==env2
    failed=readj(failure/'metadata.json')
    assert failed['status']=='failed' and not (failure/'result.json').exists()
    assert 'intentional compile failure' in (failure/'compile.log').read_text()
    assert all(v=='1' for v in failed['environment']['thread_environment'].values())
    assert set(failed['source_sha256'])=={'certificate.py','certificate_kernel.cpp'}
    assert dict(os.environ)==env
    return dict(import_preserves_environment=True,rejections=cases,
                successful_worker_mock_commands=commands,return_dictionary_is_independent=True,
                actual_worker_compile_failure_retained=True,
                full_successful_coefficient_run_not_performed=True)

def boundaries():
    d=module(); records=[]
    runenv=os.environ.copy();runenv['PYTHONPATH']=str(EDITION/'code')
    snippets={
        'guide_import': 'from fractions import Fraction\nfrom pathlib import Path\nfrom tools.two_layer_risk.certificate import certify\nassert callable(certify)\nprint("guide imports succeeded; no coefficient call")',
        'optimized_rejection': 'from tools.two_layer_risk.certificate import certify\ntry:\n certify("must_not_be_created")\nexcept RuntimeError as e:\n print(e)\nelse:\n raise AssertionError("optimization was not rejected")',
    }
    commands=[('help',[sys.executable,'-B','code/tools/two_layer_risk/certificate.py','--help'])]
    commands += [(key,[sys.executable]+(['-O'] if key=='optimized_rejection' else [])+['-B','-c',body])
                 for key,body in snippets.items()]
    for name,command in commands:
        proc=subprocess.run(command,cwd=EDITION,env=runenv,text=True,capture_output=True,timeout=20)
        assert proc.returncode==0,(name,proc.stderr)
        records.append(dict(name=name,command=command,returncode=proc.returncode,stdout=proc.stdout,stderr=proc.stderr))
    # Fresh path resolution does not create parents or files.
    fresh=SCRATCH/'missing_parents'/'validated_only'
    assert d._validate_request(fresh,30)==fresh.resolve() and not fresh.parent.exists()
    class StringPath:
        def __fspath__(self):return str(fresh)
    assert d._validate_request(StringPath(),26)==fresh.resolve()
    budgetdir=SCRATCH/'budget_preflight';budgetdir.mkdir()
    try:d.call_kernel(Path('/never_called'),'lower',[[1.,0.],[0.,1.],[1.,0.],[0.,1.]],.3989422804014327,[],26,budgetdir,d.cpu_used()-1000)
    except AssertionError as e:assert 'CPU budget exhausted' in str(e)
    else:raise AssertionError('Exhausted budget was not rejected')
    assert (budgetdir/'lower_input.txt').is_file() and not (budgetdir/'lower_stdout.json').exists()
    binary=SCRATCH/'focused_kernel/certificate_kernel'
    fixtures=['','unknown\n','primitives\n0\n','primitives\n1\nnan\n',
              'lower\n0 1\n0 .5 .3989422804014327\n1 0 0 1 1 0 0 1\n',
              'lower\n1 1\n.5 .5 .2\n1 0 0 1 1 0 0 1\n',
              'lower\n1 1\n.5 .5 .3989422804014327\n3 0 0 1 1 0 0 1\n']
    for body in fixtures:
        proc=subprocess.run([str(binary)],input=body,text=True,capture_output=True,timeout=5)
        assert proc.returncode!=0
        records.append(dict(kernel_input=body,returncode=proc.returncode,stdout=proc.stdout,stderr=proc.stderr))
    return dict(checks=records,fresh_string_pathlike_and_target30_validated_without_computation=True,
                exhausted_run_budget_rejected_before_primitive=True)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['structure','replay','api','boundaries'])
    parser.add_argument('--run',choices=['certificate_20260910_01','certificate_reproduction_20260910_01'])
    args=parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU,(60,61))
    SCRATCH.mkdir(parents=True,exist_ok=True)
    start=time.process_time(); wall=time.monotonic()
    result=structure() if args.mode=='structure' else replay(args.run) if args.mode=='replay' else api() if args.mode=='api' else boundaries()
    result.update(check=args.mode,source_sha256=sha(__file__),manifest_sha256=sha(FROZEN/'manifest.json'),
                  python=sys.version,platform=platform.platform(),cpu_seconds=time.process_time()-start,
                  wall_seconds=time.monotonic()-wall,command=sys.argv)
    name=args.mode+('_'+args.run if args.run else '')
    (SCRATCH/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['checked_local_links','rejections']},indent=2))

if __name__=='__main__':main()
