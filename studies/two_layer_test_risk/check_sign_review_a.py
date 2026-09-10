"""Independent exact interval reassembly; loads all frozen evidence, no integration."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, isqrt, prod
import hashlib, json, resource, struct, time

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
started = time.process_time()
BASE = Path(__file__).resolve().parents[1]
SCALE = 2**112

class B:
    def __init__(self, lo=0, hi=None):
        if isinstance(lo, B):
            self.lo,self.hi=lo.lo,lo.hi
            return
        lo,hi=F(lo),F(lo if hi is None else hi)
        self.lo=F(lo.numerator*SCALE//lo.denominator,SCALE)
        self.hi=F(-((-hi.numerator*SCALE)//hi.denominator),SCALE)
    def __add__(self, x):
        x=B(x);return B(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self):return B(-self.hi,-self.lo)
    def __sub__(self,x):return self+-B(x)
    def __rsub__(self,x):return B(x)+-self
    def __mul__(self,x):
        if isinstance(x,B):v=[a*b for a in [self.lo,self.hi] for b in [x.lo,x.hi]]
        else:v=[self.lo*F(x),self.hi*F(x)]
        return B(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,x):
        if not isinstance(x,B):return self*(1/F(x))
        assert x.lo*x.hi>0
        return self*B(1/x.hi,1/x.lo)
    def absmax(self):return max(abs(self.lo),abs(self.hi))
    def widen(self,r):return B(self.lo-r,self.hi+r)
    def record(self):return {'lo':str(self.lo),'hi':str(self.hi)}

def decode(b):
    v=struct.unpack('=d',struct.pack('=Q',b))[0]
    return F(v)
def bits(v):return struct.unpack('=Q',struct.pack('=d',v))[0]
def enclosing(old,new):
    assert F(old['lo'])<=new.lo<=new.hi<=F(old['hi']), (old,new.record())
def overlap(old,new):
    # Different algebraic groupings have different dependency overestimates.
    assert max(F(old['lo']),new.lo)<=min(F(old['hi']),new.hi), (old,new.record())
def atan(q):
    v=sum(F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(100))
    return B(v,v+F(1,201*q**201))
PI=16*atan(5)-4*atan(239)
def sqrt_box(x):
    x=B(x)
    lo=isqrt(x.lo.numerator*SCALE*SCALE//x.lo.denominator)
    hi=isqrt(x.hi.numerator*SCALE*SCALE//x.hi.denominator)+1
    return B(F(lo,SCALE),F(hi,SCALE))
P=F(27,50)
LABELS=[B(F(1,3)),(1-sqrt_box(5))/12,(1-sqrt_box(5))/12]
NORMAL=B(1)/sqrt_box(2*PI)
def trig(x,sine=False):
    term=x if sine else B(1)
    value=term
    for k in range(1,48):
        term=-(term*x*x)/((2*k+int(sine)-1)*(2*k+int(sine)))
        value=value+term
    return value.widen(F(5**96,factorial(96)))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),B(0))

# Load every declared frozen evidence byte and parse every JSON, not only final flags.
manifest=json.loads((BASE/'manifest.json').read_text())
loaded={}
for name,want in manifest['evidence_sha256'].items():
    raw=(BASE/'evidence'/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==want
    loaded[name]=json.loads(raw) if name.endswith('.json') else raw.decode()
prodroot=BASE/'evidence/production'
saved=loaded['production/result.json']
constants=loaded['production/constants.json']
enclosing(constants['pi'],PI)
for old,new in zip(constants['p'],LABELS):enclosing(old,new)
enclosing(constants['normal'],NORMAL)
assert (NORMAL-decode(constants['normal_float_bits'])).absmax()<F(1,10**15)

rawsum,clocksum,total=B(0),B(0),B(0)
betas=[];eps1=[];eps2=[];min_B0=None;grids=[];counts=[];radii={}
def primitive_boxes(obj,key,strip,real,price,eps,labels=0):
    r=F(1,10**9)+F(5,10**11)*strip+F(6,10**15)*real+price*eps+labels
    radii.setdefault(key,[]).append(r)
    return [B(decode(v)).widen(r) for v in obj[key+'_bits']]
def check_input(j,mode):
    stem=f'production/angle_{j:03d}/{mode}'
    tokens=loaded[stem+'_input.txt'].split();assert tokens.pop(0)==mode
    d=2 if mode=='lower' else 4
    m=list(map(int,tokens[:d]));v=list(map(float,tokens[d:]));vf=list(map(F,v))
    obj=loaded[stem+'_stdout.json'];audit=loaded[stem+'_audit.json']
    assert obj['parsed_input_bits']==list(map(bits,v))
    assert obj['mode']==mode and obj['long_double_mantissa_bits']>=64
    assert obj['total_points']==prod(2*k+1 for k in m)==audit['total_points']
    assert audit['input_sha256']==manifest['evidence_sha256'][stem+'_input.txt']
    assert audit['output_sha256']==manifest['evidence_sha256'][stem+'_stdout.json']
    assert loaded[stem+'_stderr.txt']==''
    matrix=[vf[d+1+d*a:d+1+d*(a+1)] for a in range(4)]
    for col in range(d):
        h=vf[col];c=max(abs(row[col]) for row in matrix)
        if m[col]==0:
            assert mode=='upper' and col==3 and c==0 and h==0
            continue
        a=min(F(7),F(3,4)/c) if c else F(7)
        assert 0<h<=1 and 1<=m[col]<=200 and 8<=m[col]*h<=9
        assert a*c<=F(3,4)<PI.lo/4
        assert 6*a/h-a*a/2>=26 and h*h<=F(18,26)
        assert abs(decode(obj['grid_mass_bits'][col])-1)<F(1,10**8)
        grids.append({'mode':mode,'count':m[col],'c':str(c),'h':str(h)})
    assert max(abs(v) for row in matrix for v in row)<=2
    assert (NORMAL-vf[d]).absmax()<F(1,10**15)
    for key,arr in obj.items():
        if key.endswith('_bits') and isinstance(arr,list):
            for v in arr:decode(v)
    return obj,matrix,vf[-3:] if mode=='upper' else None

for j in range(64):
    low,uhat,_=check_input(j,'lower')
    high,root,phat=check_input(j,'upper')
    assert all(root[a][3]==0 for a in range(3))
    assert sum(map(abs,phat))<P and sum(p.absmax() for p in LABELS)<P
    angles=[B(0),PI/5,-PI/5,2*PI*F(j,256)]
    u=[[trig(a),trig(a,True)] for a in angles]
    G=[[dot(a,b) for b in u] for a in u]
    e1=max((G[a][b]-sum(uhat[a][k]*uhat[b][k] for k in range(2))).absmax() for a in range(4) for b in range(4))
    q=primitive_boxes(low,'Q',1,1,2,e1)
    l=primitive_boxes(low,'L',4,1,3,e1)
    t=primitive_boxes(low,'T',4,1,9,e1)
    assert len(q)==len(l)==16 and len(t)==256
    e2=max((q[4*a+b]-sum(root[a][k]*root[b][k] for k in range(4))).absmax() for a in range(4) for b in range(4))
    ep=sum((p-v).absmax() for p,v in zip(LABELS,phat))
    specs={'ES2':(P*P,P*P,2*P*P,2*P*ep),'V':(4*P*P,P*P,9*P*P,2*P*ep),'ddgram':(4,1,3,0),'ESdd':(4*P,P,5*P,ep),'dynamic_V':(4*P*P,P*P,9*P*P,2*P*ep),'dynamic_C':(4*P,P,9*P,ep),'dynamic_dd':(4,1,3,0),'dynamic_ESdd':(4*P,P,5*P,ep),'dynamic_Hdd':(4,1,5,0),'dynamic_SH':(P,P,2*P,ep)}
    U={k:primitive_boxes(high,k,s,r,h,e2,pe) for k,(s,r,h,pe) in specs.items()}
    sizes={'ES2':1,'V':9,'ddgram':9,'ESdd':3,'dynamic_V':3,'dynamic_C':9,'dynamic_dd':3,'dynamic_ESdd':1,'dynamic_Hdd':3,'dynamic_SH':1}
    assert all(len(U[k])==n for k,n in sizes.items())
    response=[]
    for a in range(4):
        row=[LABELS[i]*(U['ddgram'][3*i+a] if a<3 else U['dynamic_dd'][i]) for i in range(3)]+[B(0)]
        row[a]+=U['ESdd'][a] if a<3 else U['dynamic_ESdd'][0]
        response.append(row)
    def lam(a,b,cross,left,right):
        return l[4*a+b]*cross+sum((t[(4*a+b)*16+4*i+k]*left[i]*right[k] for i in range(4) for k in range(4)),B(0))
    def channel(a,b,cross,left):
        return q[4*a+b]*cross+G[a][b]*lam(a,b,cross,left,response[b])
    A=sum((LABELS[a]*LABELS[b]*channel(a,b,U['V'][3*a+b],response[a]) for a in range(3) for b in range(3)),B(0))
    B0=U['ES2'][0];assert B0.lo>0
    beta=8*A/(3*B0);assert beta.absmax()<=F(1,10)
    front=sum((LABELS[b]*channel(3,b,U['dynamic_V'][b],response[3]) for b in range(3)),B(0))
    back=B(0)
    for a in range(3):
        left=[B(0) for _ in range(4)]
        left[3]=U['dynamic_dd'][a];left[a]=U['dynamic_Hdd'][a]
        back+=sum((LABELS[a]*LABELS[b]*channel(a,b,U['dynamic_C'][3*a+b],left) for b in range(3)),B(0))
    J=4*front+F(4,3)*back;velocity=2*U['dynamic_SH'][0]
    moments={'A':A,'B0':B0,'beta':beta,'a':velocity,'J':J,'F':front,'B':back}
    row=loaded[f'production/angle_{j:03d}/enclosure.json']
    assert row==saved['rows'][j]
    for k,v in moments.items():overlap(row['moments'][k],v)
    teacher=trig(6*PI*F(j,256));enclosing(row['teacher'],teacher)
    weight=F(2 if j==0 else 4,256)
    raw=2*weight*teacher*J;clock=2*weight*teacher*beta*velocity
    rawsum+=raw;clocksum+=clock;total+=raw-clock
    for k,v in [('weighted_raw',raw),('weighted_clock',clock),('cumulative',total)]:overlap(row[k],v)
    min_B0=B0.lo if min_B0 is None else min(min_B0,B0.lo)
    betas.append(beta);eps1.append(e1);eps2.append(e2);counts.append(row['upper_points'])

for k,v in [('raw_nodal_projection',rawsum),('clock_nodal_subtraction',clocksum),('nodal_sum',total),('chi',total.widen(F(1,10**6)))]:overlap(saved[k],v)
chi=saved['chi'];beta=saved['beta_intersection']
assert F(27,100000)<F(chi['lo'])<=F(chi['hi'])<F(273,1000000)
assert F(35309,1000000)<F(beta['lo'])<=F(beta['hi'])<F(35311,1000000)
alternative=total.widen(F(1,10**6))
assert F(27,100000)<alternative.lo<=alternative.hi<F(273,1000000)
assert F(35309,1000000)<max(b.lo for b in betas)<=min(b.hi for b in betas)<F(35311,1000000)
assert sum(counts)==saved['total_upper_nodes']

# Primitive exp/arithmetic and rule constants: all comparisons exact rational.
unit=F(1,2**53);gamma25=25*unit/(1-25*unit)
delta0=F(16,9)*gamma25+F(4,3)*F(1,4)**13/F(factorial(13))
assert delta0<46*unit
assert (1+46*unit)**256*(1+unit)**255-1<F(2,10**12)
exp_lower={x:sum(F(x)**k/factorial(k) for k in range(81)) for x in [26,30,32]}
for x,v in [(26,195000000000),(30,10000000000000),(32,78900000000000)]:assert exp_lower[x]>v
for target,bnd in [(26,F(5,10**11)),(30,F(1,10**12))]:
    den=exp_lower[target]-1;mass=1+2/den
    strip=sum((2/den)*mass**j for j in range(4))
    tails=sum(F(1,10)/exp_lower[32]*mass**j for j in range(4))
    assert strip<bnd
    assert tails<F(6,10**15)
    if target==30:assert strip+tails<bnd
assert 4*(F(401**3,2**64)/(1-F(401**3,2**64)))<F(15,10**12)

# Every invariant raw record of the fresh execution agrees, including exact bits.
fresh=BASE.parent/'certificate_reproduction_20260910_01'
same=[]
for name in manifest['evidence_sha256']:
    if name.startswith('production/') and (name.endswith('_input.txt') or name.endswith('_stdout.json') or name.endswith('/enclosure.json') or name in ['production/result.json','production/constants.json']):
        rel=name.removeprefix('production/')
        assert (fresh/rel).read_bytes()==(BASE/'evidence'/name).read_bytes()
        same.append(rel)
result={'status':'PASS','all_frozen_evidence_loaded':len(loaded),'angles_independently_reassembled':64,'independent_interval_bits':112,'fresh_invariant_files_byte_identical':len(same),'min_B0_lower':str(min_B0),'max_first_covariance_error':str(max(eps1)),'max_upper_covariance_error':str(max(eps2)),'independent_chi':total.widen(F(1,10**6)).record(),'independent_raw':rawsum.record(),'independent_clock':clocksum.record(),'primitive_max_radii':{k:str(max(v)) for k,v in radii.items()},'exact_sign_checks':True,'exact_elementary_and_rule_bounds':True,'cpu_seconds':time.process_time()-started}
(BASE/'reviewer_a/independent_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
