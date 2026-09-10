#!/usr/bin/env python3
"""Fixed deterministic checks for certificate_kernel.cpp; no chi evaluation."""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import struct
import subprocess
import sys
import time
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def decode(bits):
    return struct.unpack('<d', struct.pack('<Q', bits))[0]


def bits(x):
    return struct.unpack('<Q', struct.pack('<d', float(x)))[0]


def oracle_exp(r):
    """Exact rational enclosure: degree40 alternating series, dyadic180 squaring."""
    r = F(r)
    assert 0 <= r <= 64
    s = r / 256
    term = F(1)
    total = term
    for k in range(1, 41):
        term *= -s/k
        total += term
    lo = total - abs(term*s/41)
    hi = total
    scale = 1 << 180
    lower = lo.numerator*scale // lo.denominator
    upper = -((-hi.numerator*scale)//hi.denominator)
    for _ in range(8):
        lower = lower*lower // scale
        upper = -((-upper*upper)//scale)
    return F(lower, scale), F(upper, scale)


def oracle_tanh(x):
    x = F(x)
    if abs(x) > 16:
        # This is an analytic saturation enclosure, independent of libm.
        lo, hi = (F(1)-F(3,10**14), F(1))
    else:
        elo,ehi=oracle_exp(2*abs(x))
        lo,hi=(1-ehi)/(1+ehi),(1-elo)/(1+elo)
    return (-hi,-lo) if x<0 else (lo,hi)


def invoke(binary, text, real_inputs):
    result=subprocess.run([str(binary)],input=text,text=True,capture_output=True,check=True)
    obj=json.loads(result.stdout)
    assert obj['parsed_input_bits']==[bits(x) for x in real_inputs]
    return obj


def array(obj,key,shape):
    return np.array([decode(x) for x in obj[key+'_bits']]).reshape(shape)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    source=Path(__file__).with_name('certificate_kernel.cpp').resolve()
    binary=(args.output/'certificate_kernel').resolve()
    command=['g++','-O3','-std=c++17','-fno-fast-math','-ffp-contract=off',str(source),'-o',str(binary)]
    start=time.monotonic()
    compile_result=subprocess.run(command,text=True,capture_output=True)
    (args.output/'compile.log').write_text(compile_result.stdout+compile_result.stderr)
    compile_result.check_returncode()
    values=[-100.,-17.,-16.,-8.,-1.,-.125,-1e-9,0.,1e-9,.125,1.,4.,8.,16.,17.,32.,48.,64.,100.]
    primitive=invoke(binary,'primitives\n'+str(len(values))+'\n'+' '.join(map(repr,values))+'\n',values)
    primitive_checks=[]
    for i,x in enumerate(values):
        actual=F(decode(primitive['tanh_bits'][i]));lo,hi=oracle_tanh(x)
        error=max(abs(actual-lo),abs(actual-hi))
        assert error <= F(5,10**12)
        entry=dict(input=x,tanh_absolute_error_bound=float(error))
        if 0<=x<=64:
            actual=F(decode(primitive['exp_negative_bits'][i]));lo,hi=oracle_exp(F(x))
            relative=max(abs(actual-lo),abs(actual-hi))/lo
            assert relative <= F(2,10**12)
            entry['exponential_relative_error_bound']=float(relative)
        primitive_checks.append(entry)
    # Independent direct finite-tensor oracle. This checks contraction/indexing;
    # the rational primitive test above checks elementary-function accuracy.
    normal=1/math.sqrt(2*math.pi)
    h=.5;m=1
    nodes=np.array([-h,0.,h]);weights=h*normal*np.exp(-nodes*nodes/2)
    directions=np.array([[1.,0.],[.75,.5],[.75,-.5],[.5,.75]])
    real=[h,h,normal,*directions.ravel()]
    lower=invoke(binary,'lower\n1 1\n'+' '.join(map(repr,real))+'\n',real)
    points=np.array(list(itertools.product(nodes,repeat=2)))
    mass=np.array([a*b for a,b in itertools.product(weights,repeat=2)])
    z=points@directions.T;H=np.tanh(z);d=1-H*H
    expectedQ=np.einsum('v,vi,vj->ij',mass,H,H)
    expectedL=np.einsum('v,va,vb->ab',mass,d,d)
    expectedT=np.einsum('v,va,vb,vi,vj->abij',mass,d,d,H,H)
    errors={}
    for name,expected in [('Q',expectedQ),('L',expectedL),('T',expectedT)]:
        errors['lower_'+name]=float(np.max(np.abs(array(lower,name,expected.shape)-expected)))
    root=np.array([[.5,0,0,0],[.375,.125,.25,0],[.375,.125,-.25,0],[.25,-.125,.25,.125]])
    p=np.array([.25,-.125,-.0625])
    real=[h,h,h,h,normal,*root.ravel(),*p]
    upper=invoke(binary,'upper\n1 1 1 1\n'+' '.join(map(repr,real))+'\n',real)
    points=np.array(list(itertools.product(nodes,repeat=4)))
    mass=np.array([math.prod(v) for v in itertools.product(weights,repeat=4)])
    Y=points@root.T;H=np.tanh(Y);d=1-H*H;dd=-2*H*d;S=H[:,:3]@p
    expected={
        'dynamic_V':np.einsum('v,v,va->a',mass,S*S*d[:,3],d[:,:3]),
        'dynamic_C':np.einsum('v,va,vb->ab',mass*S*H[:,3],d[:,:3],d[:,:3]),
        'dynamic_dd':np.einsum('v,va->a',mass*d[:,3],d[:,:3]),
        'dynamic_ESdd':np.array([mass@(S*dd[:,3])]),
        'dynamic_Hdd':np.einsum('v,va->a',mass*H[:,3],dd[:,:3]),
        'dynamic_SH':np.array([mass@(S*H[:,3])]),
    }
    points=np.array(list(itertools.product(nodes,repeat=3)))
    mass=np.array([math.prod(v) for v in itertools.product(weights,repeat=3)])
    Y=points@root[:3,:3].T;H=np.tanh(Y);d=1-H*H;dd=-2*H*d;S=H@p
    expected.update(ES2=np.array([mass@(S*S)]),
                    V=np.einsum('v,va,vb->ab',mass*S*S,d,d),
                    ddgram=np.einsum('v,va,vb->ab',mass,d,d),
                    ESdd=np.einsum('v,va->a',mass*S,dd))
    for name,wanted in expected.items():
        errors['upper_'+name]=float(np.max(np.abs(array(upper,name,wanted.shape)-wanted)))
    assert max(errors.values()) < 1e-9
    # The exactly zero conditional variance branch must omit its root.
    root[3,3]=0
    real=[h,h,h,0.,normal,*root.ravel(),*p]
    singular=invoke(binary,'upper\n1 1 1 0\n'+' '.join(map(repr,real))+'\n',real)
    assert singular['total_points']==27
    result=dict(status='pass',scope='primitive and supplied finite-rule identities only; no chi calculation',
                command=sys.argv,compile_command=command,elapsed_seconds=time.monotonic()-start,
                source_sha256=sha(source),test_sha256=sha(__file__),binary_sha256=sha(binary),
                python=sys.version,numpy=np.__version__,platform=platform.platform(),
                compiler=subprocess.check_output(['g++','--version'],text=True).splitlines()[0],
                primitive_checks=primitive_checks,contraction_absolute_errors=errors,
                max_contraction_error=max(errors.values()),singular_branch_total_points=27,
                long_double_mantissa_bits=upper['long_double_mantissa_bits'])
    (args.output/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    for name,obj in [('primitive',primitive),('lower',lower),('upper',upper),('singular',singular)]:
        (args.output/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
