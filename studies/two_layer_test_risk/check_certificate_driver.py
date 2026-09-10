#!/usr/bin/env python3
"""Exact synthetic and constant checks for certificate_driver; no chi run."""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time


def load(path):
    spec=importlib.util.spec_from_file_location('checked_certificate_driver',path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.mkdir(parents=True,exist_ok=False)
    started=time.monotonic()
    path=Path(__file__).with_name('certificate_driver.py').resolve()
    drv=load(path);I=drv.I
    pi,p,normal,nf=drv.constants()
    def atan(q):
        val=sum(F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(100))
        return val,val+F(1,201*q**201)
    a,b=atan(5);c,d=atan(239)
    assert pi.lo <= 16*a-4*d <= 16*b-4*c <= pi.hi
    normal_identity=normal*normal*2*pi
    assert normal_identity.lo<=1<=normal_identity.hi
    trig_checks=[]
    for x in [F(-5),F(-1),F(-1,8),F(0),F(1,8),F(1),F(5)]:
        for name,offset in [('cos',0),('sin',1)]:
            value=sum(F((-1)**k,math.factorial(2*k+offset))*x**(2*k+offset)
                      for k in range(61))
            error=abs(x)**122/F(math.factorial(122))
            box=drv.trig(I(x),name)
            assert box.lo<=value-error<=value+error<=box.hi
            assert box.hi-box.lo < F(1,10**20), 'Trigonometric enclosure is unusably wide'
            trig_checks.append({'x':str(x),'kind':name,'width':str(box.hi-box.lo)})
    for x in [F(0),F(1,7),F(2),F(5),F(10**9)]:
        box=drv.sqrt_interval(I(x))
        assert box.lo**2<=x<=box.hi**2
    grid_checks=[]
    matrices=[[[0.0,0.0],[0.0,0.0]],[[2.0,.001],[-2.,-.001]],
              [[.5,0.,0.,0.],[.375,.125,.25,0.],[.375,.125,-.25,0.],[.25,-.125,.25,.125]]]
    for mat in matrices:
        for target in [26,30]:
            count,steps,evidence=drv.grid(mat,target)
            for j,ev in enumerate(evidence):
                if ev.get('omitted_zero_column'):continue
                h=F(steps[j]);aa=F(ev['a']);cc=max(abs(F(row[j])) for row in mat)
                assert aa*cc<pi.lo/4
                assert 2*pi.lo*aa/h-aa*aa/2>=target
                assert 2*pi.lo*pi.lo/(h*h)>=target
                assert 8<=count[j]*h<=9
            grid_checks.append({'target':target,'counts':count,'steps':list(map(str,steps))})
    # Two independent exact finite probability tables. The test checks the
    # response/contraction algebra, not a Gaussian identification theorem.
    h=[[F(v,10) for v in row] for row in [[2,3,-1,4],[-3,2,4,-2],[1,-4,2,3],[4,-2,-3,-1]]]
    H=[[F(v,10) for v in row] for row in [[3,-2,1,4],[-2,4,3,-1],[1,3,-4,2],[4,1,-2,-3],[-3,-1,2,1]]]
    e=[[1-v*v for v in row] for row in h]
    dd=[[1-v*v for v in row] for row in H]
    ddd=[[-2*v*(1-v*v) for v in row] for row in H]
    p=[F(1,30),F(-1,60),F(-1,90)]
    S=[sum(p[a]*row[a] for a in range(3)) for row in H]
    def lowavg(f):return sum(f(k) for k in range(4))/4
    def upavg(f):return sum(f(k) for k in range(5))/5
    Q=[[lowavg(lambda k:h[k][a]*h[k][b]) for b in range(4)] for a in range(4)]
    # Keep a correlated positive-semidefinite source Gram in this algebra test.
    directions=[[F(1),F(0)],[F(3,5),F(4,5)],[F(3,5),F(-4,5)],[F(0),F(1)]]
    G=[[sum(x*y for x,y in zip(a,b)) for b in directions] for a in directions]
    low={'Q':[I(Q[a][b]) for a in range(4) for b in range(4)],
         'L':[I(lowavg(lambda k:e[k][a]*e[k][b])) for a in range(4) for b in range(4)],
         'T':[I(lowavg(lambda k:e[k][a]*e[k][b]*h[k][i]*h[k][j]))
              for a in range(4) for b in range(4) for i in range(4) for j in range(4)],
         'G':[[I(v) for v in row] for row in G]}
    V=[[upavg(lambda k:S[k]**2*dd[k][a]*dd[k][b]) for b in range(4)] for a in range(4)]
    Edd=[[upavg(lambda k:dd[k][a]*dd[k][b]) for b in range(4)] for a in range(4)]
    ESdd=[upavg(lambda k:S[k]*ddd[k][a]) for a in range(4)]
    high={'ES2':[I(upavg(lambda k:S[k]**2))],
          'V':[I(V[a][b]) for a in range(3) for b in range(3)],
          'ddgram':[I(Edd[a][b]) for a in range(3) for b in range(3)],
          'ESdd':[I(ESdd[a]) for a in range(3)],
          'dynamic_V':[I(V[3][b]) for b in range(3)],
          'dynamic_C':[I(upavg(lambda k:H[k][3]*S[k]*dd[k][a]*dd[k][b]))
                       for a in range(3) for b in range(3)],
          'dynamic_dd':[I(Edd[3][a]) for a in range(3)],
          'dynamic_ESdd':[I(ESdd[3])],
          'dynamic_Hdd':[I(upavg(lambda k:H[k][3]*ddd[k][a])) for a in range(3)],
          'dynamic_SH':[I(upavg(lambda k:S[k]*H[k][3]))]}
    computed=drv.contraction(low,high,[I(v) for v in p])
    # Direct response means at each lower node, rather than the T contraction.
    p4=p+[F(0)]
    MU=[[sum(h[k][j]*(p4[j]*Edd[j][a]+(ESdd[a] if j==a else 0)) for j in range(4))
         for a in range(4)] for k in range(4)]
    D=[[lowavg(lambda k:e[k][a]*e[k][b]*(V[a][b]+MU[k][a]*MU[k][b]))
        for b in range(4)] for a in range(4)]
    A=sum(p[a]*p[b]*(G[a][b]*D[a][b]+Q[a][b]*V[a][b]) for a in range(3) for b in range(3))
    Fx=sum(p[b]*(Q[3][b]*V[3][b]+G[3][b]*D[3][b]) for b in range(3))
    Bx=F(0)
    for a in range(3):
        Hdd=upavg(lambda k:H[k][3]*ddd[k][a])
        MF=[h[k][3]*Edd[3][a]+h[k][a]*Hdd for k in range(4)]
        for b in range(3):
            cross=upavg(lambda k:H[k][3]*S[k]*dd[k][a]*dd[k][b])
            response=lowavg(lambda k:e[k][a]*e[k][b]*(cross+MF[k]*MU[k][b]))
            Bx+=p[a]*p[b]*(Q[a][b]*cross+G[a][b]*response)
    B0=upavg(lambda k:S[k]**2)
    exact={'A':A,'B0':B0,'beta':8*A/(3*B0),'a':2*upavg(lambda k:S[k]*H[k][3]),
           'J':4*Fx+F(4,3)*Bx,'F':Fx,'B':Bx}
    for key,value in exact.items():
        assert computed[key].lo<=value<=computed[key].hi,(key,str(value),computed[key].json())
    # The teacher's squared Fourier character has discrete mean one half.
    # All arguments stay within trig's declared [-5,5] input interval.
    weighted=I(0)
    for j in range(64):
        teacher=drv.trig(6*pi*F(j,256),'cos')
        weighted+=(F(2 if j==0 else 4,256))*teacher*teacher
    assert weighted.lo<=F(1,2)<=weighted.hi
    assert weighted.hi-weighted.lo < F(1,10**20), 'Symmetry-weight check is unusably wide'
    result={'status':'PASS','scope':'exact constants, grids and synthetic contractions; no coefficient evaluation',
            'driver_sha256':sha(path),'test_sha256':sha(__file__),
            'elapsed_seconds':time.monotonic()-started,'pi_interval':pi.json(),
            'trig_checks':trig_checks,'grid_checks':grid_checks,
            'synthetic_contraction_exact':{k:str(v) for k,v in exact.items()},
            'synthetic_contraction_enclosures':{k:v.json() for k,v in computed.items()},
            'symmetry_weight_cos3_squared':weighted.json()}
    (args.output/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('trig_checks','synthetic_contraction_enclosures')},indent=2))


if __name__=='__main__':main()
