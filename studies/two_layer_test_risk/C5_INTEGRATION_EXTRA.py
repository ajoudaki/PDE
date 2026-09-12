"""Additional frozen-kernel rejection and 27-node supplied-rule checks."""
from pathlib import Path
import itertools
import json
import math
import resource
import struct
import subprocess
import time
import numpy as np

resource.setrlimit(resource.RLIMIT_CPU, (60, 61))
r=Path('/home/amir/Codes/PDE/data/generated/two_layer_test_risk/c5_promotion_20260912_v2/integration')
b=r/'kernel_check/certificate_kernel'
start=time.monotonic();cases=[]
bad=['','unknown\n','primitives\n0\n','primitives\n1\nnan\n',
     'lower\n0 1\n0 .5 .3989422804014327 1 0 .75 .5 .75 -.5 .5 .75\n',
     'upper\n1 1 1 0\n.5 .5 .5 0 .3989422804014327 .5 0 0 0 .375 .125 .25 0 .375 .125 -.25 0 .25 -.125 .25 .125 .25 -.125 -.0625\n']
for text in bad:
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(60,61))
    p=subprocess.run([str(b)],input=text,text=True,capture_output=True,timeout=5,preexec_fn=limits)
    assert p.returncode==1 and p.stderr.strip()
    cases.append({'input':text,'returncode':p.returncode,'stderr':p.stderr.strip()})
raw=json.loads((r/'kernel_check/singular.json').read_text())
h=.5;nodes=np.array([-h,0,h]);normal=1/math.sqrt(2*math.pi)
weights=h*normal*np.exp(-nodes*nodes/2)
points=np.array(list(itertools.product(nodes,repeat=3)))
mass=np.array([math.prod(x) for x in itertools.product(weights,repeat=3)])
root=np.array([[.5,0,0],[.375,.125,.25],[.375,.125,-.25],[.25,-.125,.25]])
H=np.tanh(points@root.T);d=1-H*H;dd=-2*H*d
S=H[:,:3]@np.array([.25,-.125,-.0625])
expected={
    'dynamic_V':np.einsum('v,v,va->a',mass,S*S*d[:,3],d[:,:3]),
    'dynamic_C':np.einsum('v,va,vb->ab',mass*S*H[:,3],d[:,:3],d[:,:3]),
    'dynamic_dd':np.einsum('v,va->a',mass*d[:,3],d[:,:3]),
    'dynamic_ESdd':np.array([mass@(S*dd[:,3])]),
    'dynamic_Hdd':np.einsum('v,va->a',mass*H[:,3],dd[:,:3]),
    'dynamic_SH':np.array([mass@(S*H[:,3])])}
errors={}
for key,v in expected.items():
    got=np.array([struct.unpack('=d',struct.pack('=Q',bit))[0]
                  for bit in raw[key+'_bits']]).reshape(v.shape)
    errors[key]=float(np.max(np.abs(got-v)))
assert max(errors.values())<1e-9
result={'status':'PASS','invalid_kernel_cases':cases,
        'zero_passive_root_direct_rule_errors':errors,
        'scope':'27-node supplied rule and rejection checks; no Gaussian coefficient integration',
        'elapsed_seconds':time.monotonic()-start}
(r/'extra_kernel_boundaries.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
