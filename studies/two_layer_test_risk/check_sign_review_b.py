"""Reviewer B: supplied-data verification only; never invokes a quadrature kernel."""
import hashlib, importlib.util, json, math, pathlib, resource, struct, time
from fractions import Fraction as F

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
START = time.process_time()
BASE = pathlib.Path(__file__).resolve().parents[1]
OUT = pathlib.Path(__file__).resolve().parent
PACKET = BASE / 'packet'
PROD = BASE / 'evidence/production'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = json.loads((BASE/'manifest.json').read_text())
coverage = {}
for group, directory in [('packet_sha256','packet'), ('evidence_sha256','evidence')]:
    for name, wanted in manifest[group].items():
        path = BASE/directory/name
        actual = sha(path)
        assert actual == wanted, name
        coverage[str(path.relative_to(BASE))] = actual
coverage['manifest.json'] = sha(BASE/'manifest.json')
(OUT/'verified_input_hashes.json').write_text(json.dumps(coverage,indent=2)+'\n')

spec=importlib.util.spec_from_file_location('frozen_driver',PACKET/'certificate_driver.py')
d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
I=d.I
pi,p,normal,nf=d.constants();pf=[v.midfloat() for v in p]
saved_constants=json.loads((PROD/'constants.json').read_text())
assert saved_constants=={'pi':pi.json(),'p':[v.json() for v in p],
                        'normal':normal.json(),'normal_float_bits':d.bits(nf)}

class B:
    """Independent outward rational arithmetic, using a finer 128-bit grid."""
    scale=2**128
    def __init__(self,a=0,b=None):
        if isinstance(a,B):self.a,self.b=a.a,a.b;return
        if hasattr(a,'lo'):a,b=a.lo,a.hi
        a,b=F(a),F(a if b is None else b)
        self.a=F((a.numerator*self.scale)//a.denominator,self.scale)
        self.b=F(-((-b.numerator*self.scale)//b.denominator),self.scale)
        assert self.a<=self.b
    def __add__(self,x):
        x=B(x);return B(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return B(-self.b,-self.a)
    def __sub__(self,x):return self+-B(x)
    def __rsub__(self,x):return B(x)+-self
    def __mul__(self,x):
        x=B(x);v=[u*w for u in (self.a,self.b) for w in (x.a,x.b)]
        return B(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=B(x);assert x.a*x.b>0
        return self*B(1/x.b,1/x.a)
    def radius(self):return max(abs(self.a),abs(self.b))
    def saved(self):return {'lo':str(self.a),'hi':str(self.b),'lo_display':float(self.a),'hi_display':float(self.b)}

def make_intervals(raw,key,strip,real,price,eps,label=0):
    radius=F(1,10**9)+F(5,10**11)*strip+F(6,10**15)*real+price*eps+label
    return [B(F(d.unbits(bit))-radius,F(d.unbits(bit))+radius) for bit in raw[key+'_bits']]

def independent(lowraw,upraw,u,uf,root):
    pp=list(map(B,p));P=F(27,50)
    G=[[sum((B(x)*B(y) for x,y in zip(ua,ub)),B()) for ub in u] for ua in u]
    gh=[[sum(F(x)*F(y) for x,y in zip(ua,ub)) for ub in uf] for ua in uf]
    eg=max((G[a][b]-gh[a][b]).radius() for a in range(4) for b in range(4))
    q=make_intervals(lowraw,'Q',1,1,2,eg)
    l=make_intervals(lowraw,'L',4,1,3,eg)
    t=make_intervals(lowraw,'T',4,1,9,eg)
    qh=[[sum(F(x)*F(y) for x,y in zip(ra,rb)) for rb in root] for ra in root]
    eq=max((q[4*a+b]-qh[a][b]).radius() for a in range(4) for b in range(4))
    ep=sum((pp[a]-F(pf[a])).radius() for a in range(3))
    specs={'ES2':(P*P,P*P,2*P*P,2*P*ep),'V':(4*P*P,P*P,9*P*P,2*P*ep),
           'ddgram':(4,1,3,0),'ESdd':(4*P,P,5*P,ep),
           'dynamic_V':(4*P*P,P*P,9*P*P,2*P*ep),'dynamic_C':(4*P,P,9*P,ep),
           'dynamic_dd':(4,1,3,0),'dynamic_ESdd':(4*P,P,5*P,ep),
           'dynamic_Hdd':(4,1,5,0),'dynamic_SH':(P,P,2*P,ep)}
    h={key:make_intervals(upraw,key,aa,bb,cc,eq,ee) for key,(aa,bb,cc,ee) in specs.items()}
    means=[]
    for a in range(3):
        means.append([pp[j]*h['ddgram'][3*j+a]+(h['ESdd'][a] if j==a else B()) for j in range(3)]+[B()])
    means.append([pp[j]*h['dynamic_dd'][j] for j in range(3)]+[h['dynamic_ESdd'][0]])
    def lam(a,b,cross,mf,mg):
        return l[4*a+b]*cross+sum((t[(4*a+b)*16+4*i+j]*mf[i]*mg[j] for i in range(4) for j in range(4)),B())
    aa=B()
    for a in range(3):
        for b in range(3):
            v=h['V'][3*a+b]
            aa+=pp[a]*pp[b]*(G[a][b]*lam(a,b,v,means[a],means[b])+q[4*a+b]*v)
    fx=sum((pp[b]*(q[12+b]*h['dynamic_V'][b]+G[3][b]*lam(3,b,h['dynamic_V'][b],means[3],means[b])) for b in range(3)),B())
    bx=B()
    for a in range(3):
        mf=[h['dynamic_Hdd'][a] if i==a else B() for i in range(3)]+[h['dynamic_dd'][a]]
        for b in range(3):
            cross=h['dynamic_C'][3*a+b]
            bx+=pp[a]*pp[b]*(q[4*a+b]*cross+G[a][b]*lam(a,b,cross,mf,means[b]))
    b0=h['ES2'][0];assert b0.a>0
    beta=8*aa/(3*b0);assert beta.radius()<F(1,10)
    return {'A':aa,'B0':b0,'beta':beta,'a':2*h['dynamic_SH'][0],'F':fx,'B':bx,'J':4*fx+B(F(4,3))*bx}

result=json.loads((PROD/'result.json').read_text())
meta=json.loads((PROD/'metadata.json').read_text())
assert meta['result_sha256']==sha(PROD/'result.json')
for key,value in meta['source_sha256'].items():
    if key in manifest['original_source_sha256']:assert value==manifest['original_source_sha256'][key]
assert meta['configuration']['target']==26 and meta['configuration']['evaluated_indices']==list(range(64))
assert '-fno-fast-math' in meta['compile_command'] and '-ffp-contract=off' in meta['compile_command']
total=I();rawtotal=I();clocktotal=I();common=None;indtotal=B();indrows=[]
primitive_count=0;upper_nodes=0;lower_nodes=0;min_b0=None;max_eq=F(0);not_nested=[]
for j in range(64):
    folder=PROD/f'angle_{j:03d}'
    u=d.directions(pi,j);uf=[[v.midfloat() for v in row] for row in u]
    lows=json.loads((folder/'lower_stdout.json').read_text())
    root,var=d.root_factor(lows)
    highs=json.loads((folder/'upper_stdout.json').read_text())
    for mode,raw,matrix in [('lower',lows,uf),('upper',highs,root)]:
        count,steps,grid=d.grid(matrix,26)
        real=steps+[nf]+[float(v) for row in matrix for v in row]+(pf if mode=='upper' else [])
        body=mode+'\n'+' '.join(map(str,count))+'\n'+' '.join(format(v,'.17g') for v in real)+'\n'
        assert body==(folder/(mode+'_input.txt')).read_text()
        assert raw['mode']==mode and raw['parsed_input_bits']==list(map(d.bits,real))
        assert raw['long_double_mantissa_bits']>=64
        assert raw['total_points']==math.prod(2*m+1 for m in count)
        assert raw['outer_points']==math.prod(2*m+1 for m in (count if mode=='lower' else count[:3]))
        for x in raw['grid_mass_bits']:assert abs(F(d.unbits(x))-1)<F(1,10**8)
        for key,values in raw.items():
            if key.endswith('_bits') and isinstance(values,list) and key not in ('parsed_input_bits','grid_mass_bits'):
                primitive_count+=len(values)
                assert all(math.isfinite(d.unbits(v)) for v in values)
        audit=json.loads((folder/(mode+'_audit.json')).read_text())
        assert audit['grid']==grid and audit['input_sha256']==sha(folder/(mode+'_input.txt'))
        assert audit['output_sha256']==sha(folder/(mode+'_stdout.json'))
        assert audit['total_points']==raw['total_points'] and audit['mode']==mode
        assert (folder/(mode+'_stderr.txt')).read_text()==''
    low=d.lower_intervals(lows,u,uf,26)
    high=d.upper_intervals(highs,low,root,p,pf,26)
    c=d.contraction(low,high,p)
    cc=independent(lows,highs,u,uf,root)
    for key,value in cc.items():
        assert max(c[key].lo,value.a)<=min(value.b,c[key].hi),(j,key)
        if not c[key].lo<=value.a<=value.b<=c[key].hi:
            not_nested.append({'angle':j,'component':key,'independent':value.saved(),'producer':c[key].json()})
    if common is None:common=c['beta']
    else:common=I(max(common.lo,c['beta'].lo),min(common.hi,c['beta'].hi))
    teacher=d.trig(6*pi*F(j,256),'cos');weight=F(2 if j==0 else 4,256)
    rawterm=2*weight*teacher*c['J'];clockterm=2*weight*teacher*c['beta']*c['a']
    total+=rawterm-clockterm;rawtotal+=rawterm;clocktotal+=clockterm
    indtotal+=B(2*weight)*B(teacher)*(cc['J']-cc['beta']*cc['a'])
    row={'index':j,'alpha':(2*pi*F(j,256)).json(),'teacher':teacher.json(),
         'moments':{k:v.json() for k,v in c.items()},'epsilon_first_covariance':str(low['epsilon_first_covariance']),
         'epsilon_upper_covariance':str(high['epsilon_upper_covariance']),'epsilon_labels':str(high['epsilon_labels']),
         'heuristic_conditional_variance':var,'weighted_raw':rawterm.json(),'weighted_clock':clockterm.json(),
         'cumulative':total.json(),'lower_points':lows['total_points'],'upper_points':highs['total_points']}
    assert row==json.loads((folder/'enclosure.json').read_text())==result['rows'][j]
    upper_nodes+=highs['total_points'];lower_nodes+=lows['total_points']
    max_eq=max(max_eq,high['epsilon_upper_covariance'])
    min_b0=c['B0'].lo if min_b0 is None else min(min_b0,c['B0'].lo)
    indrows.append({'index':j,'components':{k:v.saved() for k,v in cc.items()}})
    if j%16==15:print('verified supplied angle sets',j+1,flush=True)
chi=total.widen(F(1,10**6));indchi=indtotal+B(-F(1,10**6),F(1,10**6))
for key,value in [('chi',chi),('nodal_sum',total),('raw_nodal_projection',rawtotal),('clock_nodal_subtraction',clocktotal),('beta_intersection',common)]:
    assert value.json()==result[key]
assert str(max_eq)==result['max_upper_covariance_error'] and upper_nodes==result['total_upper_nodes']
assert F(27,100000)<chi.lo<chi.hi<F(273,1000000)
assert F(35309,1000000)<common.lo<common.hi<F(35311,1000000)
assert F(27,100000)<indchi.a<indchi.b<F(273,1000000)
summary={'status':'verified all frozen values and independent contraction',
         'manifest_sha256':coverage['manifest.json'],'source_sha256':sha(pathlib.Path(__file__)),
         'hashed_packet_files':18,'hashed_evidence_files':588,'angle_sets':64,'primitive_scalars':primitive_count,
         'upper_nodes_in_saved_data':upper_nodes,'lower_nodes_in_saved_data':lower_nodes,
         'new_gaussian_integrations':0,'minimum_B0_lower':str(min_b0),'max_upper_covariance_error':str(max_eq),
         'chi':chi.json(),'beta_intersection':common.json(),'raw_nodal_projection':rawtotal.json(),
         'clock_nodal_subtraction':clocktotal.json(),'independent_chi':indchi.saved(),
         'independent_components_overlap_recorded_intervals':True,
         'non_nested_component_count_due_to_grouping':len(not_nested),'cpu_seconds':time.process_time()-START}
(OUT/'reassembly_result.json').write_text(json.dumps(summary,indent=2)+'\n')
(OUT/'independent_components.json').write_text(json.dumps(indrows,indent=2)+'\n')
(OUT/'independent_non_nested_intervals.json').write_text(json.dumps(not_nested,indent=2)+'\n')
print(json.dumps(summary,indent=2))
