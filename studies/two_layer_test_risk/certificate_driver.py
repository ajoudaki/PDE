#!/usr/bin/env python3
"""Rigorous enclosure of the fixed matched-loss cubic coefficient.

The C++ kernel only supplies approximate primitive sums. This driver charges
proved arithmetic, analytic cubature, covariance and input errors, propagates
outward rational intervals, and finally adds a proved angular error.
No training, random samples, teacher search or resolution trend is used.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import resource
import struct
import subprocess
import sys
import time
import traceback

for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import numpy as np

BITS = 96
SCALE = 1 << BITS
P = F(27,50)
ARITHMETIC = F(1,10**9)
ANGLE_ERROR = F(1,10**6)
STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]


def floor_dyadic(x):
    x = F(x)
    return F((x.numerator*SCALE)//x.denominator, SCALE)


def ceil_dyadic(x):
    return -floor_dyadic(-F(x))


class I:
    """Rational interval, rounded outward to a fixed dyadic grid."""
    __slots__ = ('lo','hi')
    def __init__(self, lo=0, hi=None):
        if isinstance(lo, I):
            assert hi is None
            self.lo, self.hi = lo.lo, lo.hi
        else:
            self.lo = floor_dyadic(F(lo))
            self.hi = ceil_dyadic(F(lo if hi is None else hi))
        assert self.lo <= self.hi
    def __add__(self, other):
        b=I(other); return I(self.lo+b.lo, self.hi+b.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self, other): return self+-I(other)
    def __rsub__(self, other): return I(other)+-self
    def __mul__(self, other):
        if isinstance(other,I):
            v=[self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        else:
            # Preserve an exact scalar such as 1/79! until after multiplication.
            # Quantizing it first gives a valid but useless amplified interval.
            c=F(other)
            v=[self.lo*c,self.hi*c]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self, other):
        if not isinstance(other,I):
            c=F(other);assert c!=0
            return self*(1/c)
        b=I(other)
        assert b.lo*b.hi>0, 'Interval division crosses zero'
        return self*I(1/b.hi,1/b.lo)
    def __rtruediv__(self, other): return I(other)/self
    def __pow__(self, n):
        assert isinstance(n,int) and n>=0
        out=I(1)
        for _ in range(n): out=out*self
        return out
    def absmax(self): return max(abs(self.lo),abs(self.hi))
    def midfloat(self): return float((self.lo+self.hi)/2)
    def widen(self, r):
        assert r>=0
        return I(self.lo-r,self.hi+r)
    def json(self):
        return {'lo':str(self.lo),'hi':str(self.hi),
                'lo_display':float(self.lo),'hi_display':float(self.hi)}


def sqrt_interval(x):
    x=I(x); assert x.lo>=0
    a=math.isqrt((x.lo.numerator*SCALE*SCALE)//x.lo.denominator)
    b=math.isqrt((x.hi.numerator*SCALE*SCALE)//x.hi.denominator)+1
    return I(F(a,SCALE),F(b,SCALE))


def constants():
    def atan_recip(q):
        v=sum(F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(64))
        error=F(1,129*q**129)
        return I(v,v+error)  # 64 terms, final sign negative.
    pi=16*atan_recip(5)-4*atan_recip(239)
    assert pi.lo>F(25,8) and pi.hi<F(22,7)
    sqrt5=sqrt_interval(5)
    labels=[I(F(1,3)),(1-sqrt5)/12,(1-sqrt5)/12]
    assert sum(v.absmax() for v in labels)<P
    normal=1/sqrt_interval(2*pi)
    normal_float=normal.midfloat()
    assert (normal-I(F(normal_float))).absmax()<F(1,10**15)
    return pi,labels,normal,normal_float


def trig(x, kind):
    x=I(x); assert x.absmax()<=5
    result=I(0)
    for k in range(40):
        power=2*k+(kind=='sin')
        result+=F((-1)**k,math.factorial(power))*x**power
    result=result.widen(F(5**80,math.factorial(80)))
    assert result.hi-result.lo<F(1,10**20), 'Trigonometric preflight precision failed'
    return result


def directions(pi, index):
    angles=[I(0),pi/5,-pi/5,2*pi*F(index,256)]
    return [[trig(a,'cos'),trig(a,'sin')] for a in angles]


def exact_dot(a,b): return sum((I(x)*I(y) for x,y in zip(a,b)),I(0))


def grid(matrix, target):
    """Rational variant of CERTIFIED_ERROR E5; no transcendental choices."""
    dim=len(matrix[0]); counts=[]; steps=[]; evidence=[]
    for j in range(dim):
        c=max(abs(F(row[j])) for row in matrix)
        if dim==4 and j==3 and c==0:
            counts.append(0);steps.append(0.0)
            evidence.append({'omitted_zero_column':True});continue
        a=min(F(7),F(3,4)/c) if c else F(7)
        hstar=6*a/(target+a*a/2)
        h=F((hstar.numerator*1024)//hstar.denominator,1024)
        m=(8*h.denominator+h.numerator-1)//h.numerator
        assert 0<h<=1 and 1<=m<=200 and 8<=m*h<=9
        assert a*c<=F(3,4) and 6*a/h-a*a/2>=target
        assert h*h<=F(18,target)  # Gaussian mass bound, since pi>3.
        counts.append(m);steps.append(float(h))
        assert F(float(h))==h
        evidence.append({'c':str(c),'a':str(a),'h':str(h),'m':m,
                         'exponent_lower':str(6*a/h-a*a/2)})
    return counts,steps,evidence


def bits(x): return struct.unpack('=Q',struct.pack('=d',x))[0]
def unbits(x): return struct.unpack('=d',struct.pack('=Q',x))[0]
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def cpu_used():
    a=resource.getrusage(resource.RUSAGE_SELF)
    b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime


def call_kernel(executable, mode, matrix, normal, p, target, folder, start_cpu):
    counts,steps,evidence=grid(matrix,target)
    real=steps+[normal]+[float(v) for row in matrix for v in row]
    if mode=='upper':real+=p
    body=mode+'\n'+' '.join(map(str,counts))+'\n'+' '.join(format(v,'.17g') for v in real)+'\n'
    (folder/(mode+'_input.txt')).write_text(body)
    remaining=math.floor(900-(cpu_used()-start_cpu))-2
    assert remaining>0, 'Run CPU budget exhausted before next primitive'
    child_limit=min(60,remaining)
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(child_limit,child_limit+1))
    begin=time.monotonic()
    proc=subprocess.run([str(executable)],input=body,text=True,capture_output=True,
                        check=False,timeout=120,preexec_fn=limits)
    (folder/(mode+'_stdout.json')).write_text(proc.stdout)
    (folder/(mode+'_stderr.txt')).write_text(proc.stderr)
    assert proc.returncode==0, (mode,proc.returncode,proc.stderr)
    result=json.loads(proc.stdout)
    assert result['parsed_input_bits']==[bits(v) for v in real]
    assert result['long_double_mantissa_bits']>=64
    assert result['total_points']==math.prod(2*m+1 for m in counts)
    for b in result['grid_mass_bits']:
        assert abs(F(unbits(b))-1)<F(1,10**8), 'Unexpected Gaussian weight mass'
    audit={'mode':mode,'grid':evidence,'elapsed_seconds':time.monotonic()-begin,
           'total_points':result['total_points'],'input_sha256':sha(folder/(mode+'_input.txt')),
           'output_sha256':sha(folder/(mode+'_stdout.json'))}
    (folder/(mode+'_audit.json')).write_text(json.dumps(audit,indent=2)+'\n')
    assert cpu_used()-start_cpu<900, 'Run CPU budget exhausted'
    return result,audit


def cubature_error(strip,real,target):
    return (F(5,10**11)*strip+F(6,10**15)*real if target==26
            else F(1,10**12)*strip)


def enclose(result,key,strip,real,price,epsilon,cerror,target):
    radius=ARITHMETIC+cubature_error(strip,real,target)+price*epsilon+cerror
    return [I(F(unbits(b))).widen(radius) for b in result[key+'_bits']]


def lower_intervals(raw,u_exact,u_float,target):
    G=[[exact_dot(a,b) for b in u_exact] for a in u_exact]
    Ghat=[[sum(F(a)*F(b) for a,b in zip(ua,ub)) for ub in u_float] for ua in u_float]
    eps=max((G[a][b]-Ghat[a][b]).absmax() for a in range(4) for b in range(4))
    q=enclose(raw,'Q',1,1,2,eps,0,target)
    l=enclose(raw,'L',4,1,3,eps,0,target)
    t=enclose(raw,'T',4,1,9,eps,0,target)
    return {'Q':q,'L':l,'T':t,'G':G,'epsilon_first_covariance':eps}


def root_factor(raw):
    q=np.array([unbits(v) for v in raw['Q_bits']]).reshape(4,4)
    q0=q[0,0];q1=(q[0,1]+q[0,2])/2;qd=(q[1,1]+q[2,2])/2;qc=q[1,2]
    b=q1/math.sqrt(q0);c=math.sqrt((qd+qc)/2-b*b);d=math.sqrt((qd-qc)/2)
    L3=np.array([[math.sqrt(q0),0,0],[b,c,d],[b,c,-d]])
    coeff=np.linalg.solve(L3,q[:3,3])
    variance=float(q[3,3]-coeff@coeff)
    L=np.zeros((4,4));L[:3,:3]=L3;L[3,:3]=coeff
    L[3,3]=math.sqrt(max(0,variance))
    assert np.isfinite(L).all() and np.abs(L).max()<=2
    return L.tolist(),variance


def upper_intervals(raw,lower,L,p_exact,p_float,target):
    qhat=[[sum(F(a)*F(b) for a,b in zip(ra,rb)) for rb in L] for ra in L]
    eps=max((lower['Q'][4*a+b]-qhat[a][b]).absmax() for a in range(4) for b in range(4))
    ep=sum((p_exact[a]-F(p_float[a])).absmax() for a in range(3))
    assert sum(abs(F(v)) for v in p_float)<P
    specs={'ES2':(P*P,P*P,2*P*P,2*P*ep),
           'V':(4*P*P,P*P,9*P*P,2*P*ep),
           'ddgram':(4,1,3,0), 'ESdd':(4*P,P,5*P,ep),
           'dynamic_V':(4*P*P,P*P,9*P*P,2*P*ep),
           'dynamic_C':(4*P,P,9*P,ep),
           'dynamic_dd':(4,1,3,0),
           'dynamic_ESdd':(4*P,P,5*P,ep),
           'dynamic_Hdd':(4,1,5,0),
           'dynamic_SH':(P,P,2*P,ep)}
    out={key:enclose(raw,key,*spec[:3],eps,spec[3],target) for key,spec in specs.items()}
    out['epsilon_upper_covariance']=eps
    out['epsilon_labels']=ep
    return out


def contraction(lower,upper,p):
    q,l,t,G=(lower[k] for k in ('Q','L','T','G'))
    def Q(a,b):return q[4*a+b]
    def L(a,b):return l[4*a+b]
    def T(a,b,i,j):return t[(4*a+b)*16+4*i+j]
    dd,V,ESdd=(upper[k] for k in ('ddgram','V','ESdd'))
    M=[[p[j]*dd[j*3+b]+(ESdd[b] if j==b else I(0)) for j in range(3)] for b in range(3)]
    A=I(0)
    for a in range(3):
        for b in range(3):
            response=sum((T(a,b,i,j)*M[a][i]*M[b][j]
                          for i in range(3) for j in range(3)),I(0))
            D=L(a,b)*V[a*3+b]+response
            A+=p[a]*p[b]*(G[a][b]*D+Q(a,b)*V[a*3+b])
    B0=upper['ES2'][0]
    assert B0.lo>0, 'No positive frozen initial loss-slope denominator'
    beta=8*A/(3*B0)
    assert beta.absmax()<=F(1,10), 'Angular beta hypothesis not verified'
    x=3
    mx=[p[i]*upper['dynamic_dd'][i] for i in range(3)]
    fx=I(0)
    for b in range(3):
        v=upper['dynamic_V'][b]
        response=sum((T(x,b,i,j)*mx[i]*M[b][j]
                      for i in range(3) for j in range(3)),I(0))
        response+=sum((T(x,b,x,j)*upper['dynamic_ESdd'][0]*M[b][j]
                       for j in range(3)),I(0))
        fx+=p[b]*(Q(x,b)*v+G[x][b]*(L(x,b)*v+response))
    bx=I(0)
    for a in range(3):
        for b in range(3):
            C=upper['dynamic_C'][a*3+b]
            response=sum((M[b][j]*(T(a,b,x,j)*upper['dynamic_dd'][a]
                                 +T(a,b,a,j)*upper['dynamic_Hdd'][a])
                          for j in range(3)),I(0))
            bx+=p[a]*p[b]*(Q(a,b)*C+G[a][b]*(L(a,b)*C+response))
    return {'A':A,'B0':B0,'beta':beta,'a':2*upper['dynamic_SH'][0],
            'J':4*fx+F(4,3)*bx,'F':fx,'B':bx}


def run(args):
    out=args.output.resolve()
    namespace=ROOT/'data/generated/two_layer_test_risk'
    assert out.is_relative_to(namespace.resolve())
    out.mkdir(parents=True,exist_ok=False)
    source_names=['certificate_driver.py','certificate_kernel.cpp','CERTIFICATION_ENGINE.md',
                  'CERTIFIED_ERROR.md','ANGULAR_CERTIFICATE.md','angle_error_bound.py',
                  'CUBIC_DERIVATION.md','MATCHING_AND_REMAINDER.md','README.md']
    sources={name:sha(STUDY/name) for name in source_names}
    compiler=['g++','-O3','-std=c++17','-fno-fast-math','-ffp-contract=off',
              str(STUDY/'certificate_kernel.cpp'),'-o',str(out/'certificate_kernel')]
    meta={'status':'running','command':sys.argv,'cwd':str(Path.cwd()),
          'source_sha256':sources,'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
          'environment':{'python':sys.version,'numpy':np.__version__,'platform':platform.platform(),
                         'compiler':subprocess.check_output(['g++','--version'],text=True).splitlines()[0]},
          'compile_command':compiler,'configuration':{'target':args.target,'angles':256,
                   'evaluated_indices':list(range(64)),'interval_bits':BITS,
                   'arithmetic_abs_error':str(ARITHMETIC),'angle_error':str(ANGLE_ERROR),
                   'cpu_limit_seconds':900,'kernel_cpu_limit_seconds':60,'seed':'none'}}
    (out/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
    begin=time.monotonic();start_cpu=cpu_used()
    try:
        build=subprocess.run(compiler,text=True,capture_output=True,check=False)
        (out/'compile.log').write_text(build.stdout+build.stderr)
        assert build.returncode==0
        meta['binary_sha256']=sha(out/'certificate_kernel')
        pi,p,normal,nf=constants();pf=[v.midfloat() for v in p]
        (out/'constants.json').write_text(json.dumps({'pi':pi.json(),'p':[v.json() for v in p],
                           'normal':normal.json(),'normal_float_bits':bits(nf)},indent=2)+'\n')
        total=I(0);raw_total=I(0);clock_total=I(0);rows=[];common_beta=None
        for j in range(64):
            folder=out/f'angle_{j:03d}';folder.mkdir()
            u=directions(pi,j);uf=[[v.midfloat() for v in row] for row in u]
            low_raw,low_audit=call_kernel(out/'certificate_kernel','lower',uf,nf,pf,args.target,folder,start_cpu)
            low=lower_intervals(low_raw,u,uf,args.target)
            factor,var=root_factor(low_raw)
            upper_raw,upper_audit=call_kernel(out/'certificate_kernel','upper',factor,nf,pf,args.target,folder,start_cpu)
            high=upper_intervals(upper_raw,low,factor,p,pf,args.target)
            c=contraction(low,high,p)
            if common_beta is None:common_beta=c['beta']
            else:
                assert max(common_beta.lo,c['beta'].lo)<=min(common_beta.hi,c['beta'].hi)
                common_beta=I(max(common_beta.lo,c['beta'].lo),min(common_beta.hi,c['beta'].hi))
            # Each independently valid beta interval contains the same exact beta.
            teacher=trig(6*pi*F(j,256),'cos')
            weight=F(2 if j==0 else 4,256)
            raw_term=2*weight*teacher*c['J']
            clock_term=2*weight*teacher*c['beta']*c['a']
            raw_total+=raw_term;clock_total+=clock_term;total+=raw_term-clock_term
            row={'index':j,'alpha':(2*pi*F(j,256)).json(), 'teacher':teacher.json(),
                 'moments':{k:v.json() for k,v in c.items()},
                 'epsilon_first_covariance':str(low['epsilon_first_covariance']),
                 'epsilon_upper_covariance':str(high['epsilon_upper_covariance']),
                 'epsilon_labels':str(high['epsilon_labels']),
                 'heuristic_conditional_variance':var,
                 'weighted_raw':raw_term.json(),'weighted_clock':clock_term.json(),
                 'cumulative':total.json(),'lower_points':low_audit['total_points'],
                 'upper_points':upper_audit['total_points']}
            (folder/'enclosure.json').write_text(json.dumps(row,indent=2)+'\n');rows.append(row)
            if j%8==0 or j==63:
                print(json.dumps({'angles_completed':j+1,'total':64,'cpu_seconds':cpu_used()-start_cpu}),flush=True)
        chi=total.widen(ANGLE_ERROR)
        decision='POSITIVE' if chi.lo>0 else 'NEGATIVE' if chi.hi<0 else 'INCONCLUSIVE'
        result={'decision':decision,'chi':chi.json(),'nodal_sum':total.json(),
                'raw_nodal_projection':raw_total.json(),'clock_nodal_subtraction':clock_total.json(),
                'beta_intersection':common_beta.json(),'angle_error':str(ANGLE_ERROR),
                'max_upper_covariance_error':str(max(F(r['epsilon_upper_covariance']) for r in rows)),
                'total_upper_nodes':sum(r['upper_points'] for r in rows),
                'rows':rows,'claim':'Exact coefficient enclosure conditional on the audited source/error proofs and arithmetic contract'}
        (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
        meta.update(status='completed',exit_status=0,result_sha256=sha(out/'result.json'),decision=decision)
        print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2),flush=True)
    except BaseException:
        meta.update(status='failed',exit_status=1,error=traceback.format_exc())
        raise
    finally:
        meta.update(cpu_seconds=cpu_used()-start_cpu,elapsed_seconds=time.monotonic()-begin,
                    peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        (out/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--target',type=int,choices=(26,30),default=26)
    run(parser.parse_args())
