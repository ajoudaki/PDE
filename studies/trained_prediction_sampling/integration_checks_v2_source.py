"""Independent integration checks; fixed algebraic fixture, no training."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib
import json
import math
import re
import platform

ROOT = Path('/home/amir/Codes/PDE')
HERE = Path(__file__).resolve().parent
EDITION = ROOT / 'data/generated/trained_prediction_sampling/integration_v2_edition'
FROZEN = ROOT / 'data/generated/trained_prediction_sampling/standalone_v2'
STUDY = ROOT / 'studies/trained_prediction_sampling'
proposal = (STUDY / 'proposal_C4_8_v2.md').read_bytes()
edits = json.loads((STUDY / 'promotion_edits_v2.json').read_bytes())
checks = {}

# Raw bytes, independent of the assembly helper's read_text/write_text path.
for relative in ('docs/global_nonlinear.md', 'docs/README.md', 'docs/NOTATION.md'):
    original = (ROOT / relative).read_bytes()
    modified = (EDITION / relative).read_bytes()
    assert modified == (FROZEN / relative).read_bytes()
    restored = modified
    if relative == 'docs/global_nonlinear.md':
        suffix = b'\n\n' + proposal
        assert restored.endswith(suffix)
        assert b''.join(restored.splitlines(keepends=True)[11439:12991]) == proposal
        restored = restored[:-len(suffix)]
    for edit in reversed(edits['replacements']):
        if edit['path'] == relative:
            old, new = edit['old'].encode(), edit['new'].encode()
            assert restored.count(new) == 1
            restored = restored.replace(new, old, 1)
    assert restored == original
    checks[relative] = {'raw_byte_inverse': True, 'matches_frozen_edition': True,
                        'sha256': hashlib.sha256(modified).hexdigest()}

text = proposal.decode()
tags = re.findall(r'\\tag\{([^}]+)\}', text)
expected = {f'C.4.8.{kind}{i}' for kind, count in [('P',20),('S',43),('R',25)] for i in range(1,count+1)}
assert set(tags) == expected and len(tags) == 88
for tag in tags:
    # Collision check byte-scans the old body, without retrieving its scientific text.
    assert (ROOT/'docs/global_nonlinear.md').read_bytes().count(('\\tag{'+tag+'}').encode()) == 0
mentions = set(re.findall(r'C\.4\.8\.[PSR]\d+', text))
assert mentions <= expected
headings = [line for line in text.splitlines() if line.startswith('#')]
assert headings[0] == '#### C.4.8. Sampling fluctuations of the trained prediction'
assert all(4 <= len(h)-len(h.lstrip('#')) <= 6 for h in headings)
for number in range(1,5):
    assert sum(h.startswith(f'##### C.4.8.{number}. ') for h in headings) == 1
slug = re.sub(r'[^\w\- ]','',headings[0].split(' ',1)[1].lower()).replace(' ','-')
assert slug == 'c48-sampling-fluctuations-of-the-trained-prediction'
assert (EDITION/'docs/README.md').read_text().count('global_nonlinear.md#'+slug) == 1
checks['new_structure'] = {'tags':len(tags),'unique_referenced_labels':len(mentions),'anchor':slug,
                            'heading_levels':[4,5,6], 'old_label_collisions':0}

# Exact independent expansion of the cutoff product identity R14.
c = list(map(Q, [2,5,-3,7]))  # 00, 10, 01, 11
f = list(map(Q, [-4,6,9,-2]))
mixed = lambda a:a[3]-a[1]-a[2]+a[0]
left = mixed([a*b for a,b in zip(c,f)])
right = c[3]*mixed(f)+(c[3]-c[1])*(f[1]-f[0])+(c[3]-c[2])*(f[2]-f[0])+mixed(c)*f[0]
assert left == right
checks['cutoff_product_identity'] = str(left)

# One fixed finite network, with nonzero readout and incompatible repeated inputs.
# Check each physical flow component against a finite-difference loss derivative.
n = 3
w = [[.2,-.7],[-.4,.1],[.8,.3]]
A = [[.3,-.5,.2],[.1,.4,-.6],[-.2,.7,.5]]
c = [.6,-.8,.4]
data = [(Q(1,5),(1.,0.),.7),(Q(1,2),(.6,.8),-.4),(Q(3,10),(1.,0.),-.2)]
theta = [x for row in w for x in row]+[x for row in A for x in row]+c
def evaluate(v, flow=False):
    W = [v[2*i:2*i+2] for i in range(n)]
    B = [v[6+3*i:9+3*i] for i in range(n)]
    C = v[15:18]
    velocity = [0.]*18
    loss = 0.
    for mass,u,y in data:
        mass = float(mass)
        h = [math.tanh(sum(a*b for a,b in zip(row,u))) for row in W]
        z = [sum(a*b for a,b in zip(row,h)) for row in B]
        b = [math.tanh(x) for x in z]
        residual = sum(a*d for a,d in zip(C,b))/n-y
        delta = [C[i]*(1-b[i]*b[i]) for i in range(n)]
        reverse = [sum(B[j][i]*delta[j] for j in range(n)) for i in range(n)]
        loss += mass*residual*residual
        for i in range(n):
            for j in range(2):
                velocity[2*i+j] += -2*mass*residual*(1-h[i]*h[i])*reverse[i]*u[j]
            for j in range(n):
                velocity[6+3*i+j] += -2*mass*residual*delta[i]*h[j]/n
            velocity[15+i] += -2*mass*residual*b[i]
        ranknorm = math.sqrt(sum((delta[i]*h[j]/n)**2 for i in range(n) for j in range(n)))
        normproduct = math.sqrt(sum(x*x for x in delta)/n)*math.sqrt(sum(x*x for x in h)/n)
        assert abs(ranknorm-normproduct)<1e-14
    return (loss,velocity) if flow else loss

loss,velocity=evaluate(theta,True)
step=1e-6
errors=[]
gradient=[]
for i in range(18):
    plus,minus=theta.copy(),theta.copy()
    plus[i]+=step
    minus[i]-=step
    derivative=(evaluate(plus)-evaluate(minus))/(2*step)
    gradient.append(derivative)
    mobility=n if i<6 or i>=15 else 1
    errors.append(abs(velocity[i]+mobility*derivative))
assert max(errors)<2e-8
metric_speed=sum(v*v/(n if i<6 or i>=15 else 1) for i,v in enumerate(velocity))
energy_error=abs(sum(a*b for a,b in zip(gradient,velocity))+metric_speed)
assert energy_error<2e-8
checks['finite_normalization']={'n':n,'observations':3,'parameters_checked':18,
    'nonzero_actual_readout':True,'repeated_input_with_distinct_labels':True,
    'maximum_gradient_error':max(errors),'energy_identity_error':energy_error,
    'rank_normalization_error_tolerance':1e-14,'finite_difference_step':step,
    'purpose':'Verify n, 1/n and unhalved-loss factors at one state; no trajectory or statistical evidence.'}

before=json.loads((HERE/'hashes_before.json').read_text())
after={name:{'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),
             'lines':len((ROOT/name).read_bytes().splitlines())} for name in before}
assert before==after
(HERE/'hashes_after.json').write_text(json.dumps(after,indent=2)+'\n')
checks['frozen_inputs_unchanged']=True
report={'status':'PASS','python':platform.python_version(),'checks':checks,
        'scope':'New addition and exact edits; old bytes are not a whole-book scientific audit.'}
(HERE/'independent_report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
