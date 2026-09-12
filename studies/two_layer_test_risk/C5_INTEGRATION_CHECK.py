"""Independent integration checks of the frozen C.5 v2 edition; no quadrature run."""
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
import re
import resource
import subprocess
import sys
import time
from unittest.mock import patch

ROOT = Path('/home/amir/Codes/PDE/data/generated/two_layer_test_risk/c5_promotion_20260912_v2')
ED = ROOT/'edition'
SCRATCH = ROOT/'integration'
TOOL = ED/'code/tools/two_layer_risk'

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path): return json.loads(path.read_text())
def load(name, path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module
def write(name, obj): (SCRATCH/name).write_text(json.dumps(obj,indent=2)+'\n')

def structure():
    manifest=read(ROOT/'manifest.json')
    expected='bff8f94655977a14491d3777463513069a1895bf2eaea7f924e6e58802b31941'
    assert sha(ROOT/'manifest.json')==expected
    hashes={'manifest.json':expected}
    for key,folder in [('packet_sha256','packet'),('edition_sha256','edition'),('evidence_sha256','evidence')]:
        for rel,digest in manifest[key].items():
            path=ROOT/folder/rel
            assert path.is_file() and not path.is_symlink()
            assert sha(path)==digest,(folder,rel)
            hashes[f'{folder}/{rel}']=digest
    assert len(manifest['destinations'])==9
    assert all(sha(ED/rel)==h for rel,h in manifest['destinations'].items())
    before=(ROOT/'packet/docs_global_nonlinear.md.before').read_bytes()
    candidate=(ROOT/'packet/candidate.md').read_bytes()
    chapter=(ED/'docs/global_nonlinear.md').read_bytes()
    assert chapter==before+b'\n'+candidate
    code_before=(ROOT/'packet/code_README.md.before').read_bytes()
    assert (ED/'code/README.md').read_bytes().startswith(code_before)
    original=(ROOT/'packet/original_candidate.md').read_text()
    oldtitle=original.splitlines()[0]
    new=candidate.decode()
    inverse=new.replace(new.splitlines()[0],oldtitle,1).replace('C5.','C4.').replace('C.5 certificate:','C.4 certificate:')
    assert inverse==original
    deps=(ROOT/'packet/dependencies.md').read_text()
    proof_spans=[];dependency_context_diffs=[]
    for block in re.split(r'<!-- Original lines \d+--\d+\. -->\n\n',deps)[1:]:
        body=block.rstrip()
        idx=chapter.decode().find(body)
        if idx<0 and body.startswith('## C. A local fixed-depth theorem and strict Gaussian activity'):
            begin=chapter.decode().index(body.splitlines()[0])
            end=chapter.decode().index('### C.4. Training-law stability',begin)
            current=chapter.decode()[begin:end].rstrip()
            oldlines=body.splitlines();newlines=current.splitlines()
            assert oldlines[:2]==newlines[:2] and oldlines[3:]==newlines[3:]
            assert oldlines[2].replace('The local theorem permits','The local theorem C.1 permits').replace('strict-activity corollary requires','strict-activity corollary C.3 requires')+' Section C.4 instead fixes two hidden tanh layers and Gaussian initialization, extends the learning law to every bounded-label law on the normalized input circle, and proves quantitative stability and a simultaneous sampling/width/GD-step limit. Its activity conclusion applies to a specified open family of laws.'==newlines[2]
            dependency_context_diffs.append({'old':oldlines[2],'current':newlines[2]})
            body=current;idx=begin
        assert idx>=0,body[:100]
        assert chapter.decode().count(body)==1
        start=chapter.decode()[:idx].count('\n')+1
        proof_spans.append([start,start+body.count('\n')])
    assert (ROOT/'packet/NOTATION.md').read_bytes()==(ED/'docs/NOTATION.md').read_bytes()
    oldguide=(ROOT/'packet/docs_README.md.before').read_text()
    guide=(ED/'docs/README.md').read_text()
    def section(s,h,end): return s.split(h,1)[1].split(end,1)[0]
    assert section(oldguide,'## Strategic roadmap: insight before breadth','## Chapters and their exact roles')==section(guide,'## Strategic roadmap: insight before breadth','## Chapters and their exact roles')
    tags=re.findall(r'\\tag\{([^}]+)\}',new)
    assert len(tags)==len(set(tags))==60
    fullcounts=Counter(re.findall(r'\\tag\{([^}]+)\}',chapter.decode()))
    assert all(fullcounts[t]==1 for t in tags)
    refs=set(re.findall(r'C5\.(?:\d+[a-z]?|[EAD]\d+)',new))
    assert refs==set(tags),(refs-set(tags),set(tags)-refs)
    assert not re.search(r'C4\.',new)
    kernel=(TOOL/'certificate_kernel.cpp').read_text()
    old_kernel=kernel.replace('See the arithmetic proof in global_nonlinear.md, C.5','See CERTIFICATION_ENGINE.md')
    original_kernel_hash=hashlib.sha256(old_kernel.encode()).hexdigest()
    for name in ('certificate_20260910_01','certificate_reproduction_20260910_01'):
        meta=read(ROOT/'evidence'/name/'metadata.json')
        assert original_kernel_hash==meta['source_sha256']['certificate_kernel.cpp']
        assert sha(ROOT/'packet/original_numerical_source.py')==meta['source_sha256']['certificate_driver.py']
    oldtree=ast.parse((ROOT/'packet/original_numerical_source.py').read_text())
    newtree=ast.parse((TOOL/'certificate.py').read_text())
    def named(tree):
        out={}
        for n in tree.body:
            if isinstance(n,(ast.FunctionDef,ast.ClassDef)):
                if n.body and isinstance(n.body[0],ast.Expr) and isinstance(n.body[0].value,ast.Constant) and isinstance(n.body[0].value.value,str): n.body=n.body[1:]
                out[n.name]=n
        return out
    oldnodes,newnodes=named(oldtree),named(newtree)
    unchanged=[]
    for name in oldnodes.keys()-{'run'}:
        assert ast.dump(oldnodes[name])==ast.dump(newnodes[name]),name
        unchanged.append(name)
    def loop(tree):
        for node in ast.walk(tree):
            if isinstance(node,ast.For) and isinstance(node.target,ast.Name) and node.target.id=='j' and ast.dump(node.iter)==ast.dump(ast.parse('range(64)',mode='eval').body):return node
    assert ast.dump(loop(oldnodes['run']))==ast.dump(loop(newnodes['run']))
    boundary=load('library_boundary',ED/'code/tools/check_library.py')
    assert boundary.main(ED)==0
    # All local fragments in changed documents, plus candidate links, are resolved.
    def anchors(path):
        result=[];seen=Counter()
        for heading in re.findall(r'^#{1,6}\s+(.+)$',path.read_text(),re.M):
            slug=re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-')
            count=seen[slug];seen[slug]+=1
            result.append(slug+(f'-{count}' if count else ''))
        return set(result)
    links=[]
    for path in [ED/'docs/README.md',ED/'code/README.md',TOOL/'README.md']:
        for target in re.findall(r'\]\(([^)\n]+)\)',boundary.prose_only(path.read_text())):
            if target.startswith(('http:','https:','mailto:')): continue
            file,_,fragment=target.partition('#');dest=(path.parent/file).resolve() if file else path
            assert dest.exists(),(path,target)
            assert not fragment or fragment in anchors(dest),(path,target)
            links.append([str(path.relative_to(ED)),target])
    for target in re.findall(r'\]\(([^)\n]+)\)',boundary.prose_only(new)):
        dest=(ED/'docs'/target).resolve();assert dest.is_file()
        links.append(['docs/global_nonlinear.md C.5',target])
    diff=''.join(difflib.unified_diff(oldguide.splitlines(True),guide.splitlines(True),fromfile='before',tofile='after'))
    (SCRATCH/'docs_guide.diff').write_text(diff)
    srcdiff=''.join(difflib.unified_diff((ROOT/'packet/original_numerical_source.py').read_text().splitlines(True),(TOOL/'certificate.py').read_text().splitlines(True),fromfile='original executed driver',tofile='candidate driver'))
    (SCRATCH/'driver_source.diff').write_text(srcdiff)
    write('input_hashes.json',hashes)
    return {'status':'PASS','verified_input_files':len(hashes),'destinations':manifest['destinations'],
            'old_chapter_bytes':len(before),'old_chapter_lines':before.count(b'\n'),
            'candidate_lines':candidate.count(b'\n'),'candidate_start_line':before.count(b'\n')+2,
            'code_guide_preserved_lines':code_before.count(b'\n'),'operative_proof_spans':proof_spans,'dependency_context_differences':dependency_context_diffs,
            'unique_C5_tags':len(tags),'same_numerical_functions':sorted(unchanged),
            'same_64_node_body_AST':True,'original_kernel_hash':original_kernel_hash,'resolved_links':links}

def replay(runname):
    drv=load('replayed_driver',TOOL/'certificate.py');I=drv.I
    run=ROOT/'evidence'/runname
    meta=read(run/'metadata.json');stored=read(run/'result.json')
    assert meta['status']=='completed' and meta['exit_status']==0
    assert meta['configuration']['target']==26
    assert meta['configuration']['evaluated_indices']==list(range(64))
    assert meta['configuration']['angles']==256 and meta['configuration']['interval_bits']==96
    assert meta['configuration']['arithmetic_abs_error']==str(drv.ARITHMETIC)
    assert meta['configuration']['angle_error']==str(drv.ANGLE_ERROR)
    assert meta['compile_command'][1:5]==['-O3','-std=c++17','-fno-fast-math','-ffp-contract=off']
    assert meta['result_sha256']==sha(run/'result.json')
    assert not (run/'compile.log').read_bytes()
    pi,p,normal,nf=drv.constants();pf=[v.midfloat() for v in p]
    assert read(run/'constants.json')=={'pi':pi.json(),'p':[v.json() for v in p],'normal':normal.json(),'normal_float_bits':drv.bits(nf)}
    total=I(0);raw_total=I(0);clock_total=I(0);common=None;rows=[];nodecount=0;maxeps=F(0)
    for j in range(64):
        folder=run/f'angle_{j:03d}'
        u=drv.directions(pi,j);uf=[[v.midfloat() for v in row] for row in u]
        raws={};matrices={}
        for mode,dim,offset in [('lower',2,3),('upper',4,5)]:
            tokens=(folder/f'{mode}_input.txt').read_text().split()
            assert tokens[0]==mode
            counts=list(map(int,tokens[1:1+dim]));real=list(map(float,tokens[1+dim:]))
            assert len(real)==(11 if dim==2 else 24)
            matrix=[real[offset+i*dim:offset+(i+1)*dim] for i in range(4)]
            if mode=='lower':assert matrix==uf
            else:assert real[-3:]==pf and all(row[3]==0 for row in matrix[:3])
            assert real[dim]==nf and all(abs(F(v))<=2 for row in matrix for v in row)
            cg,hg,eg=drv.grid(matrix,26);assert counts==cg and real[:dim]==hg
            raw=read(folder/f'{mode}_stdout.json');audit=read(folder/f'{mode}_audit.json')
            assert raw['mode']==mode
            assert raw['parsed_input_bits']==[drv.bits(v) for v in real]
            assert raw['long_double_mantissa_bits']>=64
            assert raw['total_points']==math.prod(2*m+1 for m in counts)
            assert raw['outer_points']==(raw['total_points'] if mode=='lower' else math.prod(2*m+1 for m in counts[:3]))
            assert len(raw['grid_mass_bits'])==dim
            assert all(abs(F(drv.unbits(b))-1)<F(1,10**8) for b in raw['grid_mass_bits'])
            assert audit['mode']==mode and audit['grid']==eg
            assert audit['input_sha256']==sha(folder/f'{mode}_input.txt')
            assert audit['output_sha256']==sha(folder/f'{mode}_stdout.json')
            assert audit['total_points']==raw['total_points']
            assert not (folder/f'{mode}_stderr.txt').read_bytes()
            shapes=({'Q':16,'L':16,'T':256} if mode=='lower' else {'ES2':1,'V':9,'ddgram':9,'ESdd':3,'dynamic_V':3,'dynamic_C':9,'dynamic_dd':3,'dynamic_ESdd':1,'dynamic_Hdd':3,'dynamic_SH':1})
            for key,n in shapes.items():assert len(raw[key+'_bits'])==n and all(math.isfinite(drv.unbits(b)) for b in raw[key+'_bits'])
            raws[mode]=raw;matrices[mode]=matrix
        low=drv.lower_intervals(raws['lower'],u,uf,26)
        high=drv.upper_intervals(raws['upper'],low,matrices['upper'],p,pf,26)
        c=drv.contraction(low,high,p)
        common=c['beta'] if common is None else I(max(common.lo,c['beta'].lo),min(common.hi,c['beta'].hi))
        teacher=drv.trig(6*pi*F(j,256),'cos');weight=F(2 if j==0 else 4,256)
        rawterm=2*weight*teacher*c['J'];clockterm=2*weight*teacher*c['beta']*c['a']
        raw_total+=rawterm;clock_total+=clockterm;total+=rawterm-clockterm
        row=read(folder/'enclosure.json')
        assert row==stored['rows'][j]
        wanted={'index':j,'alpha':(2*pi*F(j,256)).json(),'teacher':teacher.json(),
                'moments':{k:v.json() for k,v in c.items()},
                'epsilon_first_covariance':str(low['epsilon_first_covariance']),
                'epsilon_upper_covariance':str(high['epsilon_upper_covariance']),
                'epsilon_labels':str(high['epsilon_labels']),
                'weighted_raw':rawterm.json(),'weighted_clock':clockterm.json(),
                'cumulative':total.json(),'lower_points':raws['lower']['total_points'],
                'upper_points':raws['upper']['total_points']}
        assert all(row[k]==v for k,v in wanted.items()),j
        # Root selection is non-evidentiary, but its recorded diagnostic is checked too.
        factor,var=drv.root_factor(raws['lower'])
        assert factor==matrices['upper'] and var==row['heuristic_conditional_variance']
        nodecount+=row['upper_points'];maxeps=max(maxeps,high['epsilon_upper_covariance']);rows.append(j)
    chi=total.widen(drv.ANGLE_ERROR)
    wanted={'chi':chi.json(),'nodal_sum':total.json(),'raw_nodal_projection':raw_total.json(),
            'clock_nodal_subtraction':clock_total.json(),'beta_intersection':common.json(),
            'angle_error':str(drv.ANGLE_ERROR),'max_upper_covariance_error':str(maxeps),
            'total_upper_nodes':nodecount,'decision':'POSITIVE' if chi.lo>0 else 'NEGATIVE' if chi.hi<0 else 'INCONCLUSIVE'}
    assert all(stored[k]==v for k,v in wanted.items())
    assert F(27,100000)<chi.lo<=chi.hi<F(273,1000000)
    assert F(35309,1000000)<common.lo<=common.hi<F(35311,1000000)
    assert nodecount==86101134
    return {'status':'PASS','scope':'Exact supplied-bit reconstruction; no Gaussian finite sums executed',
            'run':runname,'angles':rows,'records':580,'aggregate':wanted,
            'original_command':meta['command'],'original_cpu_seconds':meta['cpu_seconds']}

def boundary():
    before=dict(os.environ)
    drv=load('api_boundary_driver',TOOL/'certificate.py')
    assert dict(os.environ)==before
    cases=[]
    for target in [True,False,26.,'26',None,F(26)]:
        try: drv.certify(SCRATCH/'must_not_be_created',target)
        except TypeError: cases.append(['target_type',repr(target)])
        else: raise AssertionError(target)
    for target in [0,25,27,31]:
        try: drv.certify(SCRATCH/'must_not_be_created',target)
        except ValueError: cases.append(['target_value',target])
        else: raise AssertionError(target)
    for path,kind in [('',ValueError),('a\x00b',ValueError),(b'path',TypeError),(None,TypeError),(SCRATCH,FileExistsError)]:
        try: drv.certify(path)
        except kind: cases.append(['output',repr(path)])
        else: raise AssertionError(path)
    dangling=SCRATCH/'dangling_link';dangling.symlink_to(SCRATCH/'nonexistent_link_target')
    try:
        try:drv.certify(dangling)
        except FileExistsError:cases.append(['dangling_output_symlink','rejected'])
        else:raise AssertionError('symlink')
    finally:dangling.unlink()
    assert not (SCRATCH/'must_not_be_created').exists()
    opt=subprocess.run([sys.executable,'-B','-O',str(TOOL/'certificate.py'),'--output',str(SCRATCH/'optimized_must_not_exist')],capture_output=True,text=True)
    assert opt.returncode!=0 and 'without -O or -OO' in opt.stderr
    assert not (SCRATCH/'optimized_must_not_exist').exists()
    helpresult=subprocess.run([sys.executable,'-B',str(TOOL/'certificate.py'),'--help'],capture_output=True,text=True)
    assert helpresult.returncode==0 and '--target {26,30}' in helpresult.stdout and '--_worker' not in helpresult.stdout
    (SCRATCH/'guide_help.stdout').write_text(helpresult.stdout)
    (SCRATCH/'optimized_rejection.stderr').write_text(opt.stderr)
    # Test the public launch/return boundary using an explicit inert worker mock.
    output=SCRATCH/'mock_api_output'
    payload={'decision':'MOCK','nested':{'items':[1,2]}}
    launches=[]
    def fake_run(command,env,check):
        launches.append({'command':command,'threads':{k:env[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')}})
        assert all(v=='1' for v in launches[-1]['threads'].values()) and check
        assert command[:3]==[sys.executable,'-B',str(TOOL/'certificate.py')]
        assert command[-1]=='--_worker'
        output.mkdir();(output/'result.json').write_text(json.dumps(payload))
    with patch.object(drv.subprocess,'run',fake_run): result=drv.certify(output,30)
    assert dict(os.environ)==before and result==payload
    result['nested']['items'].append(3)
    assert read(output/'result.json')==payload
    assert 'pde' not in sys.modules
    # Run the documented namespace import without calling its full-run example.
    env=dict(os.environ,PYTHONPATH=str(ED/'code'))
    imported=subprocess.run([sys.executable,'-B','-c','from tools.two_layer_risk.certificate import certify; assert callable(certify); print("guide import PASS")'],cwd=ED,env=env,capture_output=True,text=True)
    assert imported.returncode==0,imported.stderr
    return {'status':'PASS','invalid_request_cases':cases,'optimized_rejection':True,'help_no_computation':True,'namespace_import':imported.stdout.strip(),'mocked_worker_launch':launches,'environment_unchanged':True,'return_json_ownership':True}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('check',choices=['structure','replay','boundary']);parser.add_argument('--run');args=parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU,(60,61))
    SCRATCH.mkdir(exist_ok=True)
    start=time.monotonic()
    result={'structure':structure,'boundary':boundary,'replay':lambda:replay(args.run)}[args.check]()
    result['elapsed_seconds']=time.monotonic()-start
    result['checker_sha256']=sha(Path(__file__))
    name=args.check+('_'+args.run if args.run else '')+'.json'
    write(name,result)
    print(json.dumps(result,indent=2))
