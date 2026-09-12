"""Independent bounded deterministic checks; reads only the frozen packet."""
from contextlib import redirect_stdout
from fractions import Fraction as F
from hashlib import sha256
from io import StringIO
from pathlib import Path
import json
import math
import platform

ROOT = Path('/home/amir/Codes/PDE')
STUDY = ROOT / 'studies/nonlinear_selection_generalization'
OUT = ROOT / 'data/generated/nonlinear_selection_generalization/assessment_20260912/math'

def digest(data):
    return sha256(data).hexdigest()

manifest_data = (STUDY / 'scientific_manifest_v2.json').read_bytes()
manifest = json.loads(manifest_data)
hashes = {}
for name, expected in manifest['files'].items():
    data = (STUDY / name).read_bytes()
    hashes[name] = digest(data)
    assert hashes[name] == expected['sha256'], name
    assert len(data) == expected['bytes'], name
    assert len(data.splitlines()) == expected['lines'], name
hashes['scientific_manifest_v2.json'] = digest(manifest_data)

frozen = (STUDY / 'frozen_global_nonlinear_v2.md').read_text()
start = frozen.index('###### 5. Reproducible rational Gaussian certificate')
end = frozen.index('##### C.4.5.2.', start)
program = frozen[start:end].split('```python\n', 1)[1].split('```', 1)[0]
printed = StringIO()
with redirect_stdout(printed):
    exec(compile(program, 'frozen:C.4.5.1.5', 'exec'), {})

# psi=h(cos(alpha)+sin(alpha)). The six Fourier coefficients at
# cos1,sin1,cos3,sin3,cos5,sin5 are as follows. Orthogonality gives the norm.
coefficients = [F(1,2), F(1,2), -F(1,4), F(1,4), -F(1,4), -F(1,4)]
assert sum(c*c for c in coefficients)/2 == F(3,8)
assert 2*F(1,4)+F(1,4)*F(1,4) == F(9,16)

# Label margin: (1-t^2)^2-(1-3t^2+2t^3)=t^2(1-t)^2.
lhs_coeff = [F(0), F(0), F(1), F(-2), F(1)]
rhs_coeff = [F(0), F(0), F(1), F(-2), F(1)]
assert lhs_coeff == rhs_coeff

# Exact coefficients after the two square-completion estimates in NGL7.
rate = F(7,13)
norm_sq = F(11,3)
movement = F(1,19)
e_coeff = rate/4-movement
tail_coeff = -(rate/4+norm_sq/2)
assert -4*e_coeff == -rate+4*movement
assert -4*tail_coeff == rate+2*norm_sq
assert (rate+2*norm_sq)/(rate/2) == 2*(1+2*norm_sq/rate)

inverse_checks = []
for radius, kt in [(0.5,0.1),(0.01,2.0),(1e-6,5.0)]:
    eta = math.e*math.exp(-(math.sqrt(math.log(math.e/radius))+kt/2)**2)
    recovered = math.e*math.exp(-(math.sqrt(math.log(math.e/eta))-kt/2)**2)
    error = abs(recovered-radius)/radius
    assert error < 2e-14
    assert math.sqrt(math.log(math.e/eta)) > 1+kt/2
    inverse_checks.append({'radius':radius,'KT':kt,'relative_error':error})

candidate = (STUDY / 'candidate_addition_v2.md').read_text()
assert candidate.count(r'\[') == candidate.count(r'\]')
assert candidate.count(r'\(') == candidate.count(r'\)')
assert 'studies/' not in candidate and 'data/generated' not in candidate

result = {
    'result':'PASS: bounded deterministic checks',
    'python':platform.python_version(),
    'input_hashes':hashes,
    'check_source_sha256':digest(Path(__file__).read_bytes()),
    'reference_program_sha256':digest(program.encode()),
    'reference_stdout':printed.getvalue(),
    'psi_norm_squared':'3/8',
    'robust_budget_fraction':'9/16',
    'inverse_checks':inverse_checks,
    'limits':'No training, no eigenvalue evaluation, no width-rate verification, '
             'and no automated certification of the analytic arguments.'
}
(OUT / 'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
