"""Reviewer B checks of frozen inputs; never performs Gaussian integration."""
import ast
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
from fractions import Fraction as F

ROOT = Path('/home/amir/Codes/PDE/data/generated/two_layer_test_risk/c5_promotion_20260912_v2')
OUT = ROOT/'reviewer_b'
SRC = ROOT/'edition/code/tools/two_layer_risk/certificate.py'
RUNS = ['certificate_20260910_01', 'certificate_reproduction_20260910_01']

def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p): return json.loads(Path(p).read_text())
def ub(b): return struct.unpack('=d', struct.pack('=Q', b))[0]
def bits(v): return struct.unpack('=Q', struct.pack('=d', v))[0]
def module():
    spec = importlib.util.spec_from_file_location('review_b_subject', SRC)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
def save(name, x):
    (OUT/name).write_text(json.dumps(x, indent=2)+'\n')
    print(json.dumps(x, indent=2))

def audit():
    m = read(ROOT/'manifest.json')
    hashes = {}
    for field, sub in [('packet_sha256','packet'),('edition_sha256','edition'),('evidence_sha256','evidence')]:
        for name, expected in m[field].items():
            path = ROOT/sub/name
            actual = digest(path)
            assert actual == expected, str(path)
            hashes[str(path.relative_to(ROOT))] = actual
    assert digest(ROOT/'scientific_assignment.md') == m['scientific_assignment_sha256']
    hashes['scientific_assignment.md'] = digest(ROOT/'scientific_assignment.md')
    hashes['manifest.json'] = digest(ROOT/'manifest.json')
    save('input_hashes.json', hashes)
    kernel = SRC.with_name('certificate_kernel.cpp').read_bytes()
    edited = b'See the arithmetic proof in global_nonlinear.md, C.5'
    assert kernel.count(edited) == 1
    recovered = kernel.replace(edited, b'See CERTIFICATION_ENGINE.md')
    old_hash = hashlib.sha256(recovered).hexdigest()
    assert old_hash == '9d7bbcd743e465ae0e4caacd0f1e670d78283e1388a2fe48bda6193ef0e66ad9'
    assert kernel.splitlines()[1].startswith(b'//')
    class StripDocs(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            self.generic_visit(node)
            if node.body and isinstance(node.body[0],ast.Expr) and isinstance(node.body[0].value,ast.Constant) and isinstance(node.body[0].value.value,str):
                node.body.pop(0)
            return node
    trees = [StripDocs().visit(ast.parse(p.read_text())) for p in [ROOT/'packet/original_numerical_source.py',SRC]]
    defs = [{n.name:n for n in t.body if isinstance(n,(ast.FunctionDef,ast.ClassDef))} for t in trees]
    same = []
    for name in defs[0]:
        if name == 'run': continue
        assert ast.dump(defs[0][name]) == ast.dump(defs[1][name]), name
        same.append(name)
    segments=[]
    for t in trees:
        run=next(n for n in t.body if isinstance(n,ast.FunctionDef) and n.name=='run')
        block=next(n for n in run.body if isinstance(n,ast.Try)).body
        ix=next(i for i,n in enumerate(block) if isinstance(n,ast.Assign) and isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Name) and n.value.func.id=='constants')
        segments.append(ast.dump(ast.Module(body=block[ix:],type_ignores=[])))
    assert segments[0]==segments[1]
    dep=(ROOT/'packet/dependencies.md').read_text()
    before=(ROOT/'packet/docs_global_nonlinear.md.before').read_text().splitlines()
    import re
    pieces=re.split(r'<!-- Original lines (\d+)--(\d+)\. -->\n\n',dep)
    dependency_locations=[]
    before_text='\n'.join(before)
    for i in range(1,len(pieces),3):
        lo,hi=int(pieces[i]),int(pieces[i+1]); body=pieces[i+2].rstrip()
        # Frozen range comments use stale line numbers. Locate the actual
        # complete text; C's orientation paragraph deliberately excludes C.4.
        matched=body
        if body.startswith('## C.'):
            old=next(s for s in before if s.startswith('The local theorem C.1 permits'))
            new=next(s for s in body.splitlines() if s.startswith('The local theorem permits'))
            matched=body.replace(new,old)
        assert before_text.count(matched)==1,(lo,hi)
        begin=before_text[:before_text.index(matched)].count('\n')+1
        dependency_locations.append({'stated':[lo,hi],'actual':[begin,begin+len(matched.splitlines())-1],'only_C_orientation_paragraph_adjusted':body.startswith('## C.')})
    candidate=(ROOT/'packet/candidate.md').read_text()
    full=(ROOT/'edition/docs/global_nonlinear.md').read_text()
    assert full.count(candidate)==1
    sizes={'lower':{'Q_bits':16,'L_bits':16,'T_bits':256},'upper':{'ES2_bits':1,'V_bits':9,'ddgram_bits':9,'ESdd_bits':3,'dynamic_V_bits':3,'dynamic_C_bits':9,'dynamic_dd_bits':3,'dynamic_ESdd_bits':1,'dynamic_Hdd_bits':3,'dynamic_SH_bits':1}}
    d=module(); pi,p,norm,nf=d.constants()
    evidence_stats=[]
    for name in RUNS:
        run=ROOT/'evidence'/name; meta=read(run/'metadata.json'); result=read(run/'result.json')
        assert meta['status']=='completed' and meta['exit_status']==0
        assert meta['result_sha256']==digest(run/'result.json')
        assert meta['source_sha256']['certificate_driver.py']==digest(ROOT/'packet/original_numerical_source.py')
        assert meta['source_sha256']['certificate_kernel.cpp']==old_hash
        assert meta['compile_command'][:5]==['g++','-O3','-std=c++17','-fno-fast-math','-ffp-contract=off']
        assert meta['configuration']=={'target':26,'angles':256,'evaluated_indices':list(range(64)),'interval_bits':96,'arithmetic_abs_error':'1/1000000000','angle_error':'1/1000000','cpu_limit_seconds':900,'kernel_cpu_limit_seconds':60,'seed':'none'}
        assert (run/'compile.log').read_bytes()==b''
        assert read(run/'constants.json')=={'pi':pi.json(),'p':[v.json() for v in p],'normal':norm.json(),'normal_float_bits':bits(nf)}
        nodes=0; scalars=0; min_mass=1.;max_mass=1.
        for j in range(64):
            folder=run/f'angle_{j:03d}'; row=read(folder/'enclosure.json')
            assert row==result['rows'][j]
            for mode,q in [('lower',2),('upper',4)]:
                inp=(folder/(mode+'_input.txt')).read_text().split(); assert inp[0]==mode
                counts=list(map(int,inp[1:1+q])); real=list(map(float,inp[1+q:])); raw=read(folder/(mode+'_stdout.json')); aud=read(folder/(mode+'_audit.json'))
                assert len(real)==(11 if mode=='lower' else 24)
                assert raw['mode']==mode and raw['parsed_input_bits']==[bits(v) for v in real]
                assert len(raw['grid_mass_bits'])==q and raw['long_double_mantissa_bits']>=64
                assert set(raw)==set(sizes[mode])|{'mode','parsed_input_bits','outer_points','total_points','long_double_mantissa_bits','grid_mass_bits'}
                for key,n in sizes[mode].items():
                    assert len(raw[key])==n
                    assert all(type(b)is int and 0<=b<2**64 and math.isfinite(ub(b)) for b in raw[key]); scalars+=n
                assert (folder/(mode+'_stderr.txt')).read_bytes()==b''
                assert aud['mode']==mode and aud['input_sha256']==digest(folder/(mode+'_input.txt')) and aud['output_sha256']==digest(folder/(mode+'_stdout.json'))
                assert aud['elapsed_seconds']>0
                assert counts[:min(q,3)] and all(1<=v<=200 for v in counts[:min(q,3)])
                factor=[real[q+1+i*q:q+1+(i+1)*q] for i in range(4)]
                assert max(abs(v) for rr in factor for v in rr)<=2
                want_m,want_h,want_ev=d.grid(factor,26)
                assert counts==want_m and real[:q]==want_h and aud['grid']==want_ev
                assert abs(F(real[q])-F(nf))==0
                if mode=='upper':
                    assert all(rr[3]==0 for rr in factor[:3]); assert sum(abs(F(v)) for v in real[-3:])<F(27,50)
                    assert real[-3:]==[v.midfloat() for v in p]
                else:
                    exact=d.directions(pi,j)
                    assert factor==[[v.midfloat() for v in rr] for rr in exact]
                total=math.prod(2*v+1 for v in counts); outer=total if mode=='lower' else math.prod(2*v+1 for v in counts[:3])
                assert total==raw['total_points']==aud['total_points']==row[mode+'_points']
                assert outer==raw['outer_points']
                masses=[ub(b) for b in raw['grid_mass_bits']]
                assert all(abs(F(v)-1)<F(1,10**8) for v in masses)
                min_mass=min(min_mass,*masses);max_mass=max(max_mass,*masses)
                if mode=='upper':nodes+=total
            # Both complete calculations have identical input/primitive bits.
            other=ROOT/'evidence'/RUNS[0]/f'angle_{j:03d}'
            for suffix in ['lower_input.txt','upper_input.txt','lower_stdout.json','upper_stdout.json','enclosure.json']:
                assert (folder/suffix).read_bytes()==(other/suffix).read_bytes()
        assert nodes==86101134==result['total_upper_nodes']
        evidence_stats.append({'run':name,'nodes':nodes,'all_primitive_scalars_read':scalars,'grid_mass_range':[min_mass,max_mass],'source_hashes_checked':True,'metadata':meta})
    save('audit.json',{'status':'PASS','original_kernel_recovered_sha256':old_hash,'matching_numerical_definitions':same,'entire_coefficient_loop_ast_equal':True,'dependency_locations':dependency_locations,'evidence':evidence_stats})

# Independent endpoint arithmetic at a finer 128-bit grid, and the generic
# four-slot Lambda identity. No subject interval or contraction implementation
# is used in this reconstruction.
UNIT=1<<128
class Box:
    def __init__(self,a=0,b=None):
        if isinstance(a,Box):self.a,self.b=a.a,a.b;return
        a,b=F(a),F(a if b is None else b)
        self.a=F((a*UNIT).__floor__(),UNIT);self.b=F((b*UNIT).__ceil__(),UNIT)
        assert self.a<=self.b
    def __add__(s,t):
        t=Box(t);return Box(s.a+t.a,s.b+t.b)
    __radd__=__add__
    def __neg__(s):return Box(-s.b,-s.a)
    def __sub__(s,t):return s+-Box(t)
    def __rsub__(s,t):return Box(t)+-s
    def __mul__(s,t):
        t=Box(t);x=[s.a*t.a,s.a*t.b,s.b*t.a,s.b*t.b];return Box(min(x),max(x))
    __rmul__=__mul__
    def __truediv__(s,t):
        t=Box(t);assert t.a*t.b>0;return s*Box(1/t.b,1/t.a)
    def widen(s,r):return Box(s.a-r,s.b+r)
    def abs(s):return max(abs(s.a),abs(s.b))
    def json(s):return {'lo':str(s.a),'hi':str(s.b),'display':[float(s.a),float(s.b)]}

def own_sqrt(x):
    x=Box(x)
    return Box(F(math.isqrt((x.a*UNIT*UNIT).__floor__()),UNIT),F(1+math.isqrt((x.b*UNIT*UNIT).__floor__()),UNIT))
def own_constants():
    def arct(q):
        s=sum(F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(100))
        return Box(s,s+F(1,201*q**201))
    pi=16*arct(5)-4*arct(239)
    p=[Box(F(1,3)),(Box(1)-own_sqrt(5))/12,(Box(1)-own_sqrt(5))/12]
    return pi,p
def sincos(x,sine=False):
    # Degree 89/88 Taylor via recurrence; higher precision than the producer.
    x=Box(x);assert x.abs()<=5
    term=x if sine else Box(1);out=term
    for k in range(1,45):
        term=term*(-x*x)/((2*k+(1 if sine else 0))*(2*k-1+(1 if sine else 0)))
        out+=term
    return out.widen(F(5**90,math.factorial(90)))
def dot(x,y):return sum((a*b for a,b in zip(x,y)),Box())

def reconstruct():
    pi,p=own_constants();P=F(27,50);allruns=[]
    for runname in RUNS:
        run=ROOT/'evidence'/runname; rawsum=Box(); clocksum=Box(); nodal=Box(); beta_common=None; rows=[]
        for j in range(64):
            f=run/f'angle_{j:03d}';lo=read(f/'lower_stdout.json');up=read(f/'upper_stdout.json')
            li=(f/'lower_input.txt').read_text().split();ui=(f/'upper_input.txt').read_text().split()
            lower_real=list(map(float,li[3:]));upper_real=list(map(float,ui[5:]))
            uf=[[F(v) for v in lower_real[3+2*i:5+2*i]] for i in range(4)]
            factor=[[F(v) for v in upper_real[5+4*i:9+4*i]] for i in range(4)]
            ang=[Box(0),pi/5,-pi/5,pi*F(j,128)]
            u=[[sincos(a),sincos(a,True)] for a in ang]
            G=[[dot(a,b) for b in u] for a in u]
            eg=max((G[a][b]-sum(v*w for v,w in zip(uf[a],uf[b]))).abs() for a in range(4) for b in range(4))
            def enclose(raw,key,strip,real,price,eps,labels=0):
                radius=F(1,10**9)+F(5,10**11)*strip+F(6,10**15)*real+price*eps+labels
                return [Box(F(ub(v))).widen(radius) for v in raw[key+'_bits']]
            q=enclose(lo,'Q',1,1,2,eg);ell=enclose(lo,'L',4,1,3,eg);tt=enclose(lo,'T',4,1,9,eg)
            eq=max((q[4*a+b]-sum(v*w for v,w in zip(factor[a],factor[b]))).abs() for a in range(4) for b in range(4))
            ep=sum((p[a]-F(upper_real[-3+a])).abs() for a in range(3))
            spec={'ES2':(P*P,P*P,2*P*P,2*P*ep),'V':(4*P*P,P*P,9*P*P,2*P*ep),'dynamic_V':(4*P*P,P*P,9*P*P,2*P*ep),'ddgram':(4,1,3,0),'dynamic_dd':(4,1,3,0),'ESdd':(4*P,P,5*P,ep),'dynamic_ESdd':(4*P,P,5*P,ep),'dynamic_C':(4*P,P,9*P,ep),'dynamic_Hdd':(4,1,5,0),'dynamic_SH':(P,P,2*P,ep)}
            h={key:enclose(up,key,*v[:3],eq,v[3]) for key,v in spec.items()}
            def Q(a,b):return q[4*a+b]
            def L(a,b):return ell[4*a+b]
            def T(a,b,i,k):return tt[64*a+16*b+4*i+k]
            def V(a,b):return h['dynamic_V'][b] if a==3 else h['V'][3*a+b]
            def dd(a,b):return h['dynamic_dd'][b] if a==3 else h['ddgram'][3*a+b]
            def sd(a):return h['dynamic_ESdd'][0] if a==3 else h['ESdd'][a]
            deriv=[[p[i]*dd(a,i) for i in range(3)]+[Box()] for a in range(4)]
            for a in range(4):deriv[a][a]+=sd(a)
            def Lambda(a,b,cross,v,w):
                return L(a,b)*cross+sum((T(a,b,i,k)*v[i]*w[k] for i in range(4) for k in range(4)),Box())
            def C(a,cross,derivative):
                return sum((p[b]*(Q(a,b)*cross[b]+G[a][b]*Lambda(a,b,cross[b],derivative,deriv[b])) for b in range(3)),Box())
            A=sum((p[a]*C(a,[V(a,b) for b in range(3)],deriv[a]) for a in range(3)),Box())
            B0=h['ES2'][0];assert B0.a>0
            beta=8*A/(3*B0);assert beta.abs()<F(1,10)
            forward=C(3,[V(3,b) for b in range(3)],deriv[3]);back=Box()
            for a in range(3):
                v=[Box() for _ in range(4)];v[3]=h['dynamic_dd'][a];v[a]+=h['dynamic_Hdd'][a]
                back+=p[a]*C(a,[h['dynamic_C'][3*a+b] for b in range(3)],v)
            J=4*forward+F(4,3)*back; ax=2*h['dynamic_SH'][0]
            teacher=sincos(pi*F(3*j,128));weight=F(2 if j==0 else 4,256)
            raw=2*weight*teacher*J;clock=2*weight*teacher*beta*ax
            rawsum+=raw;clocksum+=clock;nodal+=raw-clock
            beta_common=beta if beta_common is None else Box(max(beta_common.a,beta.a),min(beta_common.b,beta.b))
            rows.append({'index':j,'epsilon_G':str(eg),'epsilon_Q':str(eq),'epsilon_p':str(ep),'beta':beta.json(),'J':J.json(),'a':ax.json()})
        chi=nodal.widen(F(1,10**6))
        assert F(27,100000)<chi.a<=chi.b<F(273,1000000)
        assert F(35309,1000000)<beta_common.a<=beta_common.b<F(35311,1000000)
        saved=read(run/'result.json')
        assert max(F(saved['chi']['lo']),chi.a)<=min(F(saved['chi']['hi']),chi.b)
        allruns.append({'run':runname,'chi':chi.json(),'beta':beta_common.json(),'raw':rawsum.json(),'clock':clocksum.json(),'nodal':nodal.json(),'rows':rows})
    (OUT/'independent_reconstruction.json').write_text(json.dumps({'status':'PASS','method':'Independent 128-bit outward endpoint arithmetic; longer input series; generic four-slot Lambda; supplied bits only','runs':allruns},indent=2)+'\n')
    print(json.dumps([{k:v for k,v in r.items() if k!='rows'} for r in allruns],indent=2))

def replay():
    d=module();pi,p,norm,nf=d.constants();rows=[]
    for name in RUNS:
        run=ROOT/'evidence'/name; total=d.I();rt=d.I();ct=d.I();common=None
        for j in range(64):
            f=run/f'angle_{j:03d}';saved=read(f/'enclosure.json');lr=read(f/'lower_stdout.json');ur=read(f/'upper_stdout.json')
            u=d.directions(pi,j);uf=[[v.midfloat() for v in row] for row in u]
            low=d.lower_intervals(lr,u,uf,26);factor,var=d.root_factor(lr)
            real=list(map(float,(f/'upper_input.txt').read_text().split()[5:]));assert factor==[real[5+4*k:9+4*k] for k in range(4)]
            high=d.upper_intervals(ur,low,factor,p,[v.midfloat() for v in p],26); c=d.contraction(low,high,p)
            assert {k:v.json() for k,v in c.items()}==saved['moments']
            assert str(low['epsilon_first_covariance'])==saved['epsilon_first_covariance']
            assert str(high['epsilon_upper_covariance'])==saved['epsilon_upper_covariance']
            assert str(high['epsilon_labels'])==saved['epsilon_labels']
            assert var==saved['heuristic_conditional_variance']
            teacher=d.trig(6*pi*F(j,256),'cos');weight=F(2 if j==0 else 4,256)
            raw=2*weight*teacher*c['J'];clock=2*weight*teacher*c['beta']*c['a'];total+=raw-clock;rt+=raw;ct+=clock
            assert raw.json()==saved['weighted_raw'] and clock.json()==saved['weighted_clock'] and total.json()==saved['cumulative']
            common=c['beta'] if common is None else d.I(max(common.lo,c['beta'].lo),min(common.hi,c['beta'].hi))
        result=read(run/'result.json'); reconstructed={'chi':total.widen(d.ANGLE_ERROR),'nodal_sum':total,'raw_nodal_projection':rt,'clock_nodal_subtraction':ct,'beta_intersection':common}
        assert all(value.json()==result[key] for key,value in reconstructed.items())
        rows.append({'run':name,'all_64_rows_exactly_equal':True,**{k:v.json() for k,v in reconstructed.items()}})
    save('exact_replay.json',{'status':'PASS','runs':rows})

def boundary():
    before=dict(os.environ);d=module();assert dict(os.environ)==before
    cases=[]
    for target in [True,26.,'26',F(26),0,25,31,None]:
        out=OUT/'must_not_exist'
        try:d.certify(out,target)
        except (TypeError,ValueError) as ex:cases.append([repr(target),type(ex).__name__])
        else:raise AssertionError(target)
        assert not out.exists()
    for output in ['',b'bytes',None,12,'x\x00y',OUT]:
        try:d.certify(output)
        except (TypeError,ValueError,FileExistsError) as ex:cases.append([repr(output),type(ex).__name__])
        else:raise AssertionError(output)
    link=OUT/'dangling';link.symlink_to(OUT/'absent')
    try:d.certify(link)
    except FileExistsError:cases.append(['dangling_symlink','FileExistsError'])
    else:raise AssertionError('accepted symlink')
    assert d._validate_request(OUT/'future'/'output',30)==OUT/'future'/'output'
    assert not (OUT/'future').exists()
    help_result=subprocess.run([sys.executable,'-B',str(SRC),'--help'],text=True,capture_output=True,check=True)
    (OUT/'cli_help.txt').write_text(help_result.stdout)
    optimized=subprocess.run([sys.executable,'-B','-O',str(SRC),'--output',str(OUT/'optimized_no_output')],text=True,capture_output=True)
    assert optimized.returncode!=0 and 'without -O or -OO' in optimized.stderr
    assert not (OUT/'optimized_no_output').exists()
    (OUT/'optimized_rejection.txt').write_text(optimized.stderr)
    # Exercise actual worker failure without any integration: with g++ absent
    # the compiler-version query fails, then retained metadata records failure.
    failed=OUT/'missing_compiler';old=os.environ.get('PATH');os.environ['PATH']=str(OUT/'no_binaries')
    try:
        try:d.certify(failed)
        except subprocess.CalledProcessError:pass
        else:raise AssertionError('missing compiler accepted')
    finally:
        if old is None:os.environ.pop('PATH',None)
        else:os.environ['PATH']=old
    assert read(failed/'metadata.json')['status']=='failed'
    assert not (failed/'result.json').exists()
    assert dict(os.environ)==before
    # Fixed malformed supplied inputs are kernel checks, not integrations.
    binary=OUT/'kernel_check/certificate_kernel'
    bad=['','unknown\n','primitives\n0\n','primitives\n1\nnan\n','lower\n0 0\n0 0 .399\n'+'0 '*8+'\n']
    for body in bad:
        proc=subprocess.run([str(binary)],input=body,text=True,capture_output=True)
        assert proc.returncode!=0 and proc.stderr
    save('boundary.json',{'status':'PASS','rejected_requests':cases,'import_environment_unchanged':True,'help_no_computation':True,'optimized_python_rejected':True,'missing_compiler_failure_retained':True,'malformed_kernel_cases':len(bad)})

def theory():
    u=F(1,2**53)
    gamma=lambda n,v:F(n)*v/(1-F(n)*v)
    delta=F(16,9)*gamma(25,u)+F(4,3)*F(1,4)**13/math.factorial(13)
    assert delta<46*u
    assert (1+46*u)**256*(1+u)**255-1<F(2,10**12)
    assert 4*gamma(401**3,F(1,2**64))<F(15,10**12)
    assert F(200001,10**15)+F(15,10**12)+F(1,10**13)<F(22,10**11)
    exponential_lower={26:195000000000,30:10000000000000,32:78900000000000}
    for k,bound in exponential_lower.items():
        assert sum(F(k**j,math.factorial(j)) for j in range(81))>bound
    # Separate upper bounds for strip and tail coefficients, including masses.
    del26=F(2,exponential_lower[26]-1)
    masses=sum((1+del26)**j for j in range(4))
    assert F(2,exponential_lower[26]-1)*masses<F(5,10**11)
    assert F(1,10*exponential_lower[32])*masses<F(6,10**15)
    del30=F(2,exponential_lower[30]-1)
    assert (F(2,exponential_lower[30]-1)+F(1,10*exponential_lower[32]))*sum((1+del30)**j for j in range(4))<F(1,10**12)
    # Independent exponential-generating-series composition, without the
    # producer's Stirling/Bell recurrences, reconstructs the angular bound.
    n=8
    def mul(a,b):return [sum(a[j]*b[k-j] for j in range(k+1)) for k in range(n+1)]
    def powers(a):
        out=[[F(1)]+[F(0)]*n]
        for j in range(1,n+1):out.append(mul(out[-1],a))
        return out
    m=[F(1),F(1),F(1),F(2)]+[F(math.factorial(j))*F(4,3)**j for j in range(4,11)]
    normal=[F(1)];ceilnorm=[F(1)]
    for j in range(1,n+1):
        if j%2: normal.append(F(4,5)*2**((j-1)//2)*math.factorial((j-1)//2))
        else: normal.append(F(math.prod(range(1,j,2))))
        moment=math.prod(range(1,2*j,2));a=math.isqrt(moment);ceilnorm.append(F(a+(a*a<moment)))
    ex=powers([F(0)]+[F(1,math.factorial(j)) for j in range(1,n+1)])
    # [z^k](exp(z)-1)^j/j! = S(k,j)/k!.
    sigma=[F(0)]+[sum(m[j]*ceilnorm[j]*ex[j][k]/math.factorial(j) for j in range(1,k+1)) for k in range(1,n+1)]
    sy=powers(sigma)
    lower=[];upper=[]
    for r in range(3):
        lower.append([m[r]]+[sum(m[r+j]*normal[j]*ex[j][k]/math.factorial(j) for j in range(1,k+1)) for k in range(1,n+1)])
        upper.append([m[r]]+[sum(m[r+j]*normal[j]*sy[j][k]/math.factorial(j) for j in range(1,k+1)) for k in range(1,n+1)])
    g=[F(1,math.factorial(j)) for j in range(n+1)]
    t=[F(3**j,math.factorial(j)) for j in range(n+1)]
    v0=mul(lower[0],upper[1]);v1=mul(g,mul(lower[1],upper[1]));v2=mul(g,mul(lower[2],upper[2]))
    prof=[2*(F(27,50)**3*(F(20,3)*v0[k]+12*v1[k]+4*v2[k]+F(16,3)*upper[0][k])+F(27,250)*upper[0][k]) for k in range(n+1)]
    D=mul(t,prof)[8]*math.factorial(8);error=F(16,7)*D/F(256**8)
    assert D==F(41272525446939874982,31640625)
    assert error==F(20636262723469937491,127677049435953561600000000)<F(1,10**6)
    # phi'''' at both possible positive critical points, with exact interval
    # sqrt(105), suffices by symmetry and zero endpoint values.
    critical=[]
    for sign in [-1,1]:
        z=(Box(15)+sign*own_sqrt(105))/30;x=own_sqrt(z)
        value=x*(16-40*z+24*z*z)
        assert value.abs()<5
        critical.append(value.json())
    save('theory.json',{'status':'PASS','initial_exp_relative_error_bound':str(delta),'angular_derivative':str(D),'angular_error':str(error),'tanh_fourth_derivative_critical_values':critical,'rational_exponential_strip_tail_and_roundoff_checks':True})

if __name__=='__main__':
    resource.setrlimit(resource.RLIMIT_CPU,(60,61))
    OUT.mkdir(exist_ok=True)
    start=time.process_time();mode=sys.argv[1]
    {'audit':audit,'reconstruct':reconstruct,'replay':replay,'boundary':boundary,'theory':theory}[mode]()
    print('self_cpu_seconds',time.process_time()-start)
