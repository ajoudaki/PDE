#!/usr/bin/env python3
"""Fresh review A: exact saved-bit reconstruction and boundary checks only.

No Gaussian integration, model search or training is performed here.
Every invocation has a 60-second CPU cap. Inputs are the assigned frozen packet.
"""
import argparse
import ast
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import resource
import struct
import subprocess
import sys
import time
from unittest.mock import patch

ROOT = Path('/home/amir/Codes/PDE/data/generated/two_layer_test_risk/c5_promotion_20260912_v2')
SCRATCH = ROOT/'reviewer_a'
TOOL = ROOT/'edition/code/tools/two_layer_risk'
SCALE = 2**96

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads(p.read_text())
def load(p, name):
    spec=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m
def bit(v): return struct.unpack('=Q',struct.pack('=d',v))[0]
def val(b):
    assert type(b) is int and 0<=b<2**64
    x=struct.unpack('=d',struct.pack('=Q',b))[0]
    assert math.isfinite(x)
    return Q(x)

# Independent endpoint arithmetic. Every operation widens to the same grid;
# no candidate interval operator or contraction is called in independent_C.
def down(x): return Q((x.numerator*SCALE)//x.denominator,SCALE)
def up(x): return -down(-x)
def box(x,y=None):
    if isinstance(x,tuple): return x
    x=Q(x);y=x if y is None else Q(y)
    assert x<=y
    return down(x),up(y)
def plus(x,y):
    x,y=box(x),box(y);return box(x[0]+y[0],x[1]+y[1])
def negative(x): x=box(x);return -x[1],-x[0]
def minus(x,y): return plus(x,negative(y))
def times(x,y):
    x,y=box(x),box(y)
    v=[a*b for a in x for b in y];return box(min(v),max(v))
def scale(x,q):
    x=box(x);q=Q(q);return box(min(x[0]*q,x[1]*q),max(x[0]*q,x[1]*q))
def divide(x,y):
    y=box(y);assert y[0]*y[1]>0
    return times(x,box(1/y[1],1/y[0]))
def summation(xs):
    r=box(0)
    for x in xs:r=plus(r,x)
    return r
def widen(x,e): x=box(x);return box(x[0]-e,x[1]+e)
def endpoints(i):return i.lo,i.hi
def from_json(d):return Q(d['lo']),Q(d['hi'])
def report_box(i):return {'lo':str(i[0]),'hi':str(i[1]),'display':[float(v) for v in i]}
def intersect(a,b):
    a,b=box(a),box(b);assert max(a[0],b[0])<=min(a[1],b[1]);return box(max(a[0],b[0]),min(a[1],b[1]))

def independent_C(lower, upper, labels):
    """C5.28 directly, with four formal derivative slots throughout."""
    p=[endpoints(v) for v in labels]+[box(0)]
    q,l,t=([endpoints(v) for v in lower[k]] for k in ('Q','L','T'))
    G=[[endpoints(v) for v in row] for row in lower['G']]
    u={k:[endpoints(v) for v in v] for k,v in upper.items() if isinstance(v,list)}
    def T(a,b,i,j):return t[((a*4+b)*4+i)*4+j]
    # mu_U[a,i] is the mean derivative in formal slot i.
    MU=[]
    for a in range(4):
        row=[]
        for i in range(4):
            gate = u['ddgram'][i*3+a] if a<3 and i<3 else u['dynamic_dd'][i] if a==3 and i<3 else box(0)
            z=times(p[i],gate)
            if i==a:z=plus(z,u['ESdd'][a] if a<3 else u['dynamic_ESdd'][0])
            row.append(z)
        MU.append(row)
    def lambda_value(a,b,cross,DF,DH):
        meanprod=summation(times(times(T(a,b,i,j),DF[i]),DH[j]) for i in range(4) for j in range(4))
        return plus(times(l[a*4+b],cross),meanprod)
    def C(a,crosses,derivative):
        return summation(times(p[b],plus(times(q[a*4+b],crosses[b]),times(G[a][b],lambda_value(a,b,crosses[b],derivative,MU[b])))) for b in range(3))
    train=[C(a,u['V'][3*a:3*a+3],MU[a]) for a in range(3)]
    A=summation(times(p[a],train[a]) for a in range(3))
    F=C(3,u['dynamic_V'],MU[3])
    Bterms=[]
    for a in range(3):
        DF=[box(0)]*4
        DF[3]=u['dynamic_dd'][a]
        DF[a]=u['dynamic_Hdd'][a]
        Bterms.append(times(p[a],C(a,u['dynamic_C'][3*a:3*a+3],DF)))
    B=summation(Bterms)
    return {'A':A,'B0':u['ES2'][0],'beta':divide(scale(A,8),scale(u['ES2'][0],3)),
            'a':scale(u['dynamic_SH'][0],2),'J':plus(scale(F,4),scale(B,Q(4,3))),'F':F,'B':B}

def inventory():
    man=read(ROOT/'manifest.json')
    assert digest(ROOT/'manifest.json')=='bff8f94655977a14491d3777463513069a1895bf2eaea7f924e6e58802b31941'
    records={}
    for section,prefix in [('packet_sha256','packet'),('edition_sha256','edition'),('evidence_sha256','evidence')]:
        for rel,want in man[section].items():
            p=ROOT/prefix/rel;got=digest(p);assert got==want,(p,got,want)
            records[str(p.relative_to(ROOT))]=got
    records['scientific_assignment.md']=digest(ROOT/'scientific_assignment.md')
    assert records['scientific_assignment.md']==man['scientific_assignment_sha256']
    records['manifest.json']=digest(ROOT/'manifest.json')
    a=ast.parse((ROOT/'packet/original_numerical_source.py').read_text())
    b=ast.parse((TOOL/'certificate.py').read_text())
    def defs(tree):return {n.name:n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
    def strip_doc(n):
        if n.body and isinstance(n.body[0],ast.Expr) and isinstance(n.body[0].value,ast.Constant) and isinstance(n.body[0].value.value,str): n.body=n.body[1:]
        return ast.dump(n,include_attributes=False)
    a,b=defs(a),defs(b)
    equal=[k for k in a if strip_doc(a[k])==strip_doc(b[k])]
    assert set(a)-set(equal)=={'run'}
    # The entire numerical try body is also unchanged; only provenance/wrapper
    # setup and metadata lifecycle differ in run.
    oldtry=next(n for n in a['run'].body if isinstance(n,ast.Try))
    newtry=next(n for n in b['run'].body if isinstance(n,ast.Try))
    assert ast.dump(ast.Module(body=oldtry.body,type_ignores=[]))==ast.dump(ast.Module(body=newtry.body[1:],type_ignores=[]))
    source=(TOOL/'certificate_kernel.cpp').read_text()
    old=source.replace('// No network training and no libm exp/tanh calls. See the arithmetic proof in global_nonlinear.md, C.5.','// No network training and no libm exp/tanh calls. See CERTIFICATION_ENGINE.md.')
    assert hashlib.sha256(old.encode()).hexdigest()==man['source_sha256']['certificate_kernel.cpp']
    assert (ROOT/'edition/docs/global_nonlinear.md').read_text()==(ROOT/'packet/docs_global_nonlinear.md.before').read_text().rstrip()+'\n\n'+(ROOT/'packet/candidate.md').read_text()
    # Independently verify the elementary rational inequalities in the proof.
    for n,bound in [(26,195000000000),(30,10000000000000),(32,78900000000000)]:
        assert sum(Q(n**j,math.factorial(j)) for j in range(81))>bound
    u=Q(1,2**53);g=25*u/(1-25*u)
    assert Q(16,9)*g+Q(4,3)*Q(1,4)**13/math.factorial(13)<46*u
    assert (1+46*u)**256*(1+u)**255-1<Q(2,10**12)
    ul=Q(1,2**64);n=401**3
    assert 4*n*ul/(1-n*ul)<Q(15,10**12)
    return {'hashes':records,'matched_hashes':len(records),'common_numerical_definitions_identical':equal,
            'entire_calculation_try_body_identical':True,'original_kernel_comment_reconstruction_sha256':hashlib.sha256(old.encode()).hexdigest(),
            'elementary_rational_inequalities':'PASS'}

def reconstruction(which):
    d=load(TOOL/'certificate.py','fresh_A_driver')
    pi,p,normal,nf=d.constants();pf=[v.midfloat() for v in p]
    run=ROOT/'evidence'/which
    meta=read(run/'metadata.json');saved=read(run/'result.json')
    assert meta['status']=='completed' and meta['exit_status']==0
    assert meta['result_sha256']==digest(run/'result.json')
    assert meta['source_sha256']['certificate_driver.py']==digest(ROOT/'packet/original_numerical_source.py')
    assert read(run/'constants.json')=={'pi':pi.json(),'p':[v.json() for v in p],'normal':normal.json(),'normal_float_bits':bit(nf)}
    assert (run/'compile.log').read_text()==''
    total=d.I(0);rawsum=d.I(0);clocks=d.I(0);beta=None
    own=box(0);ownraw=box(0);ownclock=box(0);ownbeta=None
    total_nodes=0;counts=[];maxeps=Q(0);checked_scalars=0;rows=[]
    shapes={'lower':{'Q':16,'L':16,'T':256},'upper':{'ES2':1,'V':9,'ddgram':9,'ESdd':3,'dynamic_V':3,'dynamic_C':9,'dynamic_dd':3,'dynamic_ESdd':1,'dynamic_Hdd':3,'dynamic_SH':1}}
    for j in range(64):
        node=run/f'angle_{j:03d}';exact=d.directions(pi,j);uf=[[x.midfloat() for x in row] for row in exact]
        outputs={};inputs={}
        for mode,dim in [('lower',2),('upper',4)]:
            raw=(node/(mode+'_input.txt')).read_text().split();assert raw.pop(0)==mode
            m=list(map(int,raw[:dim]));real=list(map(float,raw[dim:]));assert len(real)==(11 if mode=='lower' else 24)
            matrix=[real[dim+1+a*dim:dim+1+(a+1)*dim] for a in range(4)]
            obj=read(node/(mode+'_stdout.json'));audit=read(node/(mode+'_audit.json'))
            assert obj['mode']==mode and obj['parsed_input_bits']==list(map(bit,real))
            assert obj['long_double_mantissa_bits']>=64
            assert obj['total_points']==math.prod(2*v+1 for v in m)
            outer=math.prod(2*v+1 for v in (m if mode=='lower' else m[:3]))
            assert obj['outer_points']==outer
            assert set(obj)=={'mode','parsed_input_bits','outer_points','total_points','long_double_mantissa_bits','grid_mass_bits'}|{k+'_bits' for k in shapes[mode]}
            assert len(obj['grid_mass_bits'])==dim
            for b in obj['grid_mass_bits']:assert abs(val(b)-1)<Q(1,10**8)
            for k,n in shapes[mode].items():
                assert len(obj[k+'_bits'])==n
                for b in obj[k+'_bits']:val(b);checked_scalars+=1
            assert (node/(mode+'_stderr.txt')).read_text()==''
            assert audit['mode']==mode and audit['total_points']==obj['total_points']
            assert audit['input_sha256']==digest(node/(mode+'_input.txt')) and audit['output_sha256']==digest(node/(mode+'_stdout.json'))
            mm,hh,ev=d.grid(matrix,26)
            assert m==mm and real[:dim]==hh and audit['grid']==ev
            # Independently check every exact grid inequality, not only flags.
            for axis in range(dim):
                c=max(abs(Q(row[axis])) for row in matrix)
                h=Q(real[axis])
                if m[axis]==0:assert axis==3 and c==0 and h==0;continue
                aa=min(Q(7),Q(3,4)/c) if c else Q(7)
                assert 0<h<=1 and 1<=m[axis]<=200 and 8<=m[axis]*h<=9
                assert aa*c<=Q(3,4) and 6*aa/h-aa*aa/2>=26 and h*h<=Q(18,26)
            assert real[dim]==nf and max(abs(v) for row in matrix for v in row)<=2
            if mode=='lower':assert matrix==uf
            else:assert all(matrix[a][3]==0 for a in range(3)) and real[-3:]==pf
            outputs[mode]=obj;inputs[mode]=matrix
        low=d.lower_intervals(outputs['lower'],exact,inputs['lower'],26)
        # Recompute root proposal from supplied primitives, not another integral.
        proposed,variance=d.root_factor(outputs['lower'])
        assert proposed==inputs['upper']
        high=d.upper_intervals(outputs['upper'],low,inputs['upper'],p,pf,26)
        c=d.contraction(low,high,p);ind=independent_C(low,high,p)
        enclosed=read(node/'enclosure.json')
        assert enclosed==saved['rows'][j]
        assert enclosed['index']==j and enclosed['heuristic_conditional_variance']==variance
        for k,v in c.items():
            assert v.json()==enclosed['moments'][k]
            intersect(endpoints(v),ind[k])
        assert str(low['epsilon_first_covariance'])==enclosed['epsilon_first_covariance']
        assert str(high['epsilon_upper_covariance'])==enclosed['epsilon_upper_covariance']
        assert str(high['epsilon_labels'])==enclosed['epsilon_labels']
        beta=c['beta'] if beta is None else d.I(max(beta.lo,c['beta'].lo),min(beta.hi,c['beta'].hi))
        ownbeta=ind['beta'] if ownbeta is None else intersect(ownbeta,ind['beta'])
        teacher=d.trig(6*pi*Q(j,256),'cos');w=Q(2 if j==0 else 4,256)
        raw=2*w*teacher*c['J'];clk=2*w*teacher*c['beta']*c['a']
        rawsum+=raw;clocks+=clk;total+=raw-clk
        assert teacher.json()==enclosed['teacher'] and (2*pi*Q(j,256)).json()==enclosed['alpha']
        assert raw.json()==enclosed['weighted_raw'] and clk.json()==enclosed['weighted_clock'] and total.json()==enclosed['cumulative']
        iraw=times(scale(endpoints(teacher),2*w),ind['J'])
        iclk=times(times(scale(endpoints(teacher),2*w),ind['beta']),ind['a'])
        ownraw=plus(ownraw,iraw);ownclock=plus(ownclock,iclk);own=plus(own,minus(iraw,iclk))
        total_nodes+=outputs['upper']['total_points'];maxeps=max(maxeps,high['epsilon_upper_covariance'])
        assert enclosed['lower_points']==outputs['lower']['total_points'] and enclosed['upper_points']==outputs['upper']['total_points']
        rows.append({'index':j,'independent':{k:report_box(v) for k,v in ind.items()}})
        counts.append([outputs['lower']['total_points'],outputs['upper']['total_points']])
    for k,v in {'chi':total.widen(Q(1,10**6)),'nodal_sum':total,'raw_nodal_projection':rawsum,'clock_nodal_subtraction':clocks,'beta_intersection':beta}.items():assert v.json()==saved[k]
    assert total_nodes==saved['total_upper_nodes']==86101134 and str(maxeps)==saved['max_upper_covariance_error']
    ownchi=widen(own,Q(1,10**6));assert Q(27,100000)<ownchi[0]<=ownchi[1]<Q(273,1000000)
    assert Q(35309,1000000)<ownbeta[0]<=ownbeta[1]<Q(35311,1000000)
    return {'run':which,'all_saved_rows_exactly_reconstructed':64,'all_scalar_primitive_outputs_checked':checked_scalars,
            'upper_nodes_preexisting_only':total_nodes,'input_output_contracts':'PASS','own_four_slot_contraction':'PASS',
            'own_chi':report_box(ownchi),'own_beta':report_box(ownbeta),'own_raw':report_box(ownraw),'own_clock':report_box(ownclock),
            'evaluated_chapter_chi':saved['chi'],'node_counts':counts,'independent_rows':rows}

def boundary():
    before=dict(os.environ);base=set(SCRATCH.iterdir());d=load(TOOL/'certificate.py','fresh_A_boundary')
    assert dict(os.environ)==before and set(SCRATCH.iterdir())==base
    checked=[];out=SCRATCH/'must_not_be_created'
    for target,exc in [(True,TypeError),(26.0,TypeError),('26',TypeError),(25,ValueError),(31,ValueError)]:
        try:d.certify(out,target)
        except exc:checked.append(repr(target))
        else:raise AssertionError(target)
        assert not out.exists()
    for value,exc in [('',ValueError),('bad\x00path',ValueError),(b'bytes',TypeError),(12,TypeError),(SCRATCH,FileExistsError)]:
        try:d.certify(value)
        except exc:checked.append(repr(value))
        else:raise AssertionError(value)
    link=SCRATCH/'broken_output_symlink';link.symlink_to(SCRATCH/'missing_target')
    try:
        try:d.certify(link)
        except FileExistsError:checked.append('broken symlink rejected')
        else:raise AssertionError('symlink')
    finally:link.unlink()
    # Exercise public success/mutation semantics without launching a calculation.
    seen=[];mockout=SCRATCH/'mock_worker_output'
    def fake_run(command,**kw):
        seen.append((command,kw))
        mockout.mkdir();(mockout/'result.json').write_text('{"decision":"INCONCLUSIVE","chi":{"lo":"-1","hi":"1"}}')
    with patch.object(d.subprocess,'run',fake_run):ret=d.certify(mockout)
    assert seen[0][0]==[sys.executable,'-B',str(TOOL/'certificate.py'),'--output',str(mockout),'--target','26','--_worker']
    assert all(seen[0][1]['env'][k]=='1' for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'])
    assert os.environ==before
    ret['chi']['lo']='changed';assert read(mockout/'result.json')['chi']['lo']=='-1'
    failout=SCRATCH/'mock_failure_must_not_exist'
    with patch.object(d.subprocess,'run',side_effect=subprocess.CalledProcessError(7,['fake'])):
        try:d.certify(failout)
        except subprocess.CalledProcessError as e:assert e.returncode==7
        else:raise AssertionError('failure not propagated')
    assert not failout.exists()
    help_run=subprocess.run([sys.executable,'-B',str(TOOL/'certificate.py'),'--help'],text=True,capture_output=True)
    assert help_run.returncode==0 and '--target {26,30}' in help_run.stdout
    optimized=subprocess.run([sys.executable,'-O','-B',str(TOOL/'certificate.py'),'--output',str(out)],text=True,capture_output=True)
    assert optimized.returncode!=0 and 'without -O or -OO' in optimized.stderr and not out.exists()
    return {'import_environment_unchanged':True,'invalid_cases':checked,'mock_worker_contract':'PASS',
            'mock_inconclusive_return_and_ownership':'PASS','mock_failure_propagates':'PASS','help':help_run.stdout,
            'optimized_exit':optimized.returncode,'optimized_error':optimized.stderr}

def main():
    resource.setrlimit(resource.RLIMIT_CPU,(60,61))
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['inventory','original','reproduction','boundary']);a=parser.parse_args()
    start=time.process_time()
    if a.mode=='inventory':result=inventory()
    elif a.mode=='boundary':result=boundary()
    else:result=reconstruction('certificate_20260910_01' if a.mode=='original' else 'certificate_reproduction_20260910_01')
    result.update(status='PASS',cpu_seconds=time.process_time()-start,source_sha256=digest(Path(__file__)))
    path=SCRATCH/(a.mode+'.json');path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['hashes','independent_rows','node_counts']},indent=2))

if __name__=='__main__':main()
