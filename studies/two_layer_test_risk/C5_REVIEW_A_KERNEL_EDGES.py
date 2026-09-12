#!/usr/bin/env python3
"""Bounded primitive/invalid-input checks; no Gaussian coefficient integration."""
from fractions import Fraction as F
import importlib.util
import hashlib
import json
import math
from pathlib import Path
import resource
import struct
import subprocess
import time

root=Path('/home/amir/Codes/PDE/data/generated/two_layer_test_risk/c5_promotion_20260912_v2')
scratch=root/'reviewer_a'
resource.setrlimit(resource.RLIMIT_CPU,(60,61))
binary=scratch/'focused_kernel/certificate_kernel'
spec=importlib.util.spec_from_file_location('A_edge_oracle',root/'edition/code/tools/two_layer_risk/check_kernel.py')
oracle=importlib.util.module_from_spec(spec);spec.loader.exec_module(oracle)
start=time.process_time()
cases=[('', 'missing mode'),('other\n','unknown mode'),('primitives\n0\n','primitive count'),
       ('primitives\n10001\n','primitive count'),('primitives\n1\nNaN\n','invalid real'),
       ('lower\n201 1\n.5 .5 .3989422804014327 1 0 1 0 1 0 1 0\n','grid out'),
       ('lower\n0 1\n0 .5 .3989422804014327 1 0 1 0 1 0 1 0\n','lower roots'),
       ('lower\n1 1\n.5 .5 .3 1 0 1 0 1 0 1 0\n','normal constant')]
rootmap=[[.5,0,0,0],[.375,.125,.25,0],[.375,.125,-.25,0],[.25,-.125,.25,.125]]
def upper(m,steps,mat,p):
    return 'upper\n'+' '.join(map(str,m))+'\n'+' '.join(map(str,steps+[.3989422804014327]+sum(mat,[])+p))+'\n'
cases.append((upper([1,1,1,0],[.5,.5,.5,0],rootmap,[.25,-.125,-.0625]),'nonzero passive root'))
bad=[r[:] for r in rootmap];bad[0][3]=.125
cases.append((upper([1,1,1,1],[.5]*4,bad,[.25,-.125,-.0625]),'training coordinates'))
cases.append((upper([1,1,1,1],[.5]*4,rootmap,[1.,1.,1.]),'label norm'))
invalid=[]
for text,expected in cases:
    p=subprocess.run([str(binary)],input=text,text=True,capture_output=True,timeout=10)
    assert p.returncode!=0 and expected in p.stderr,(p.returncode,p.stderr,expected)
    invalid.append({'input':text,'exit':p.returncode,'stderr':p.stderr})
tiny=math.ldexp(1.,-1074)
values=[tiny,-tiny,math.ldexp(1.,-1022),-math.ldexp(1.,-1022),math.nextafter(16.,0.),16.,math.nextafter(16.,math.inf),64.,math.nextafter(64.,0.)]
request='primitives\n'+str(len(values))+'\n'+' '.join(map(repr,values))+'\n'
p=subprocess.run([str(binary)],input=request,text=True,capture_output=True,check=True,timeout=10)
data=json.loads(p.stdout);assert data['parsed_input_bits']==[oracle.bits(v) for v in values]
errors=[]
for i,x in enumerate(values):
    y=F(oracle.decode(data['tanh_bits'][i]));lo,hi=oracle.oracle_tanh(x)
    e=max(abs(y-lo),abs(y-hi));assert e<=F(5,10**12)
    row={'value':repr(x),'tanh_absolute_error_enclosure':str(e)}
    if 0<=x<=64:
        y=F(oracle.decode(data['exp_negative_bits'][i]));lo,hi=oracle.oracle_exp(x)
        e=max(abs(y-lo),abs(y-hi))/lo;assert e<=F(2,10**12)
        row['exponential_relative_error_enclosure']=str(e)
    errors.append(row)
result={'status':'PASS','invalid_contracts':invalid,'primitive_edges':errors,'cpu_seconds':time.process_time()-start,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'binary_sha256':hashlib.sha256(binary.read_bytes()).hexdigest()}
(scratch/'kernel_edges.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','invalid_cases':len(invalid),'primitive_edges':len(errors),'cpu_seconds':result['cpu_seconds'],'source_sha256':result['source_sha256']}))
