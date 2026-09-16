"""Bounded standalone integration validation; retain commands and original logs."""
import argparse
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time


def check_added_links(edition):
    """Check new local Markdown file links and their simple GFM heading anchors."""
    checked=[]
    for rel in ('docs/README.md','code/README.md','docs/global_nonlinear.md',
                'docs/observable_p1.md','code/GENERAL_P1.md'):
        path=edition/rel
        baseline=edition/'integration_inputs/baseline'/rel
        text=path.read_text()
        if baseline.exists():
            text='\n'.join(line[2:] for line in difflib.ndiff(baseline.read_text().splitlines(),text.splitlines())
                           if line.startswith('+ '))
        text=re.sub(r'```.*?```','',text,flags=re.S)
        for target in re.findall(r'\]\(([^)\n]+)\)',text):
            if '://' in target or target.startswith('mailto:'):continue
            filename,separator,fragment=target.partition('#')
            destination=(path.parent/filename).resolve() if filename else path
            if not destination.is_relative_to(edition) or not destination.is_file():
                raise ValueError('broken new local link: '+rel+' -> '+target)
            if separator:
                headings=re.findall(r'^#{1,6}\s+(.+?)\s*#*$',destination.read_text(),re.M)
                anchors=[re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in headings]
                if fragment not in anchors:raise ValueError('broken added heading fragment: '+target)
            checked.append(dict(source=rel,target=target))
    return dict(passed=True,scope='new Markdown links and simple heading fragments only',links=checked)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--edition', required=True, type=Path)
    parser.add_argument('--device', required=True)
    parser.add_argument('--python', required=True)
    parser.add_argument('--run', required=True)
    args = parser.parse_args()
    edition = args.edition.resolve()
    out = edition/'data/established'/args.run
    out.mkdir(parents=True,exist_ok=False)
    (out/'added_links.json').write_text(json.dumps(check_added_links(edition),indent=2)+'\n')
    env = dict(os.environ,PYTHONPATH=str(edition/'code'),PYTHONDONTWRITEBYTECODE='1',
               OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
               CUBLAS_WORKSPACE_CONFIG=':4096:8',PDE_TEST_DEVICE=args.device,
               CIRCLE_TEST_DEVICE=args.device,CIRCLE_TEST_SCRATCH=str(out),TMPDIR=str(out))
    commands = []
    def add(name, *tail):
        commands.append((name,[args.python,'-B',*tail]))
    if args.device=='cpu':
        commands.append(('numpy_only_discovery',[sys.executable,'-B','-m','unittest','discover',
                         '-s','code/tests','-p','test_general_p1.py','-v']))
        add('boundary','code/tools/check_library.py')
        for name in ('test_library_boundary','test_observable_initialization','test_observable_solver'):
            add(name,'code/tests/'+name+'.py')
        add('numpy_only_import','-c',"import pde,sys; assert 'torch' not in sys.modules; print('NumPy-only import preserved')")
        blocks = re.findall(r'```python\n(.*?)\n```',(edition/'code/GENERAL_P1.md').read_text(),re.S)
        add('general_guide','-c','\n'.join(blocks))
        guide = (edition/'code/README.md').read_text()
        circle = guide.split('## Optional GPU backend for the finite circle closure',1)
        if len(circle)!=2:
            raise ValueError('missing circle guide section')
        blocks = re.findall(r'```python\n(.*?)\n```',circle[1],re.S)
        if not blocks:
            raise ValueError('missing circle guide example')
        add('circle_guide','-c','\n'.join(blocks))
    for name in ('test_observable_torch_circle','test_general_p1'):
        add(name,'code/tests/'+name+'.py')
    add('circle_example','code/scripts/validate_torch_circle.py','--device',args.device,'--output',str(out/'circle'))
    for repeat in ('a','b'):
        add('general_example_'+repeat,'code/scripts/example_general_p1.py','--device',args.device,'--output',str(out/('general_'+repeat)))
    add('general_replay','code/scripts/analyze_general_p1.py','--run',str(out/'general_a'),
        '--repeat',str(out/'general_b'),'--output',str(out/'general_analysis.json'))
    frozen = json.loads((edition/'FROZEN_SHA256.json').read_text())
    for rel, expected in frozen.items():
        if hashlib.sha256((edition/rel).read_bytes()).hexdigest()!=expected:
            raise ValueError('frozen file changed: '+rel)
    record = dict(status='running',cwd=str(edition),device=args.device,
        limits=dict(total_wall_seconds=600,subprocess_wall_seconds=120,numerical_threads=1,
                    scope='deterministic unit checks and fixed tiny examples; no historical training reproduction',
                    general_example=dict(d=3,m=9,n=16,P=16,steps=10,h=.005),
                    circle_example=dict(d=2,orders=[1,3,5],Q=64,P=32,steps=4,h=.005),
                    cuda='general producer allocator cap 15 percent; circle producer checks 1 GiB; no heavy jobs'),
        environment={k:env[k] for k in ['PYTHONPATH','PYTHONDONTWRITEBYTECODE','OPENBLAS_NUM_THREADS',
                     'OMP_NUM_THREADS','MKL_NUM_THREADS','CUBLAS_WORKSPACE_CONFIG','PDE_TEST_DEVICE',
                     'CIRCLE_TEST_DEVICE','CIRCLE_TEST_SCRATCH','TMPDIR']},
        manifest_sha256=hashlib.sha256((edition/'FROZEN_SHA256.json').read_bytes()).hexdigest(),commands=[])
    report = out/'validation.json'
    report.write_text(json.dumps(record,indent=2)+'\n')
    began=time.monotonic()
    try:
        for name, command in commands:
            remaining=600-(time.monotonic()-began)
            if remaining<=0: raise TimeoutError('validation wall budget exhausted')
            tick=time.monotonic()
            result=subprocess.run(command,cwd=edition,env=env,capture_output=True,text=True,timeout=min(120,remaining))
            (out/(name+'.stdout')).write_text(result.stdout)
            (out/(name+'.stderr')).write_text(result.stderr)
            record['commands'].append(dict(name=name,command=command,exit_status=result.returncode,wall_seconds=time.monotonic()-tick))
            report.write_text(json.dumps(record,indent=2)+'\n')
            print(name+': '+str(result.returncode),flush=True)
            if result.returncode: raise RuntimeError(name+' failed; original logs retained')
        for rel,expected in frozen.items():
            if hashlib.sha256((edition/rel).read_bytes()).hexdigest()!=expected:
                raise ValueError('validation changed frozen source: '+rel)
        record['status']='complete'
    except BaseException as error:
        record.update(status='failed',error=repr(error))
        raise
    finally:
        record['process_window_seconds']=time.monotonic()-began
        record['outputs']={str(p.relative_to(out)):hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in sorted(out.rglob('*')) if p.is_file() and p!=report}
        report.write_text(json.dumps(record,indent=2)+'\n')


if __name__=='__main__':
    main()
