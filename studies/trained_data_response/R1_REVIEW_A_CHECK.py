"""Independent exact algebra/boundary checks. No sampled or trained networks."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def add(a, b):
    z = dict(a)
    for k, v in b.items():
        z[k] = z.get(k, F(0)) + v
    return {k: v for k, v in z.items() if v}


def mul(a, b):
    z = {}
    for i, x in a.items():
        for j, y in b.items():
            z[i + j] = z.get(i + j, F(0)) + x * y
    return {k: v for k, v in z.items() if v}


def mm(a, b):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def tr(a):
    return [list(x) for x in zip(*a)]


def scale(a, s):
    return [[s*x for x in row] for row in a]


def madd(a, b):
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


cosh = {1: F(1, 2), -1: F(1, 2)}
sinh = {1: F(1, 2), -1: F(-1, 2)}
cosh2 = mul(cosh, cosh)
assert cosh2 == {2: F(1, 4), 0: F(1, 2), -2: F(1, 4)}
dc = {k: k*v for k, v in cosh2.items() if k*v}
assert mul(dc, cosh) == mul({k: 2*v for k, v in sinh.items()}, cosh2)

# Embed this block in ell^2. D e_j=2^(-j)e_j on all coordinates is
# injective and positive, but its lower operator bound is zero. S has
# support in the first four coordinates, so these exact identities are
# also identities on the infinite-dimensional embedded construction.
v = [[F(1)], [F(-2)], [F(3, 2)], [F(1, 3)]]
a = [[F(1), F(2)]]
S = mm(v, a)
D = [[F(1, 2**(i+1)) if i == j else F(0)
      for j in range(4)] for i in range(4)]
E = mm(tr(S), D)
K = mm(E, S)
kappa = mm(mm(tr(v), D), v)[0][0]
Kplus = scale(mm(tr(a), a), 1/(25*kappa))
assert mm(mm(K, Kplus), K) == K
assert mm(mm(Kplus, K), Kplus) == Kplus
assert mm(K, Kplus) == tr(mm(K, Kplus))
assert mm(Kplus, K) == tr(mm(Kplus, K))
P = madd(eye(4), scale(mm(mm(S, Kplus), E), -1))
assert mm(P, P) == P
assert mm(E, P) == [[F(0)]*4 for _ in range(2)]
assert mm(P, S) == [[F(0)]*2 for _ in range(4)]
assert mm(D, P) == tr(mm(D, P))
SE = mm(S, E)
assert mm(SE, SE) == scale(SE, 5*kappa)
# Therefore exp(-2t SE)=I+(exp(-10*kappa*t)-1)*SE/(5*kappa),
# proving the submitted singular formula in this boundary instance.
assert mm(mm(S, Kplus), E) == scale(SE, 1/(5*kappa))
kernel = [[F(-2)], [F(1)]]
assert mm(S, kernel) == [[F(0)] for _ in range(4)]
assert mm(K, kernel) == [[F(0)] for _ in range(2)]

# Without the metric relation, ES=0 does permit secular nilpotent growth.
badS = [[F(1)], [F(0)]]
badE = [[F(0), F(1)]]
badSE = mm(badS, badE)
assert mm(badE, badS) == [[F(0)]]
assert badSE != [[F(0)]*2 for _ in range(2)]
assert mm(badSE, badSE) == [[F(0)]*2 for _ in range(2)]

# Sum of the displayed D0 majorants in S24 is <=81 D0^4 for D0>=1.
# Powers of D0 are compared only upwards; the forcing bound is <=36 D0^3.
assert (5+30)+(5+24+3)+(5+9) == 81
assert (2+12)+(2+12)+8 == 36
assert F(1, 4) == F(1, 3)/2+F(2, 3)/8
assert 2*F(1, 2) == 1

result = {
    'checks': 'PASS',
    'clock_primitive_and_weight_derivative': 'exact Laurent polynomial identities',
    'singular_gram_pseudoinverse_projection': 'exact rational identities',
    'injective_noncoercive_metric_boundary': 'ell^2 diagonal extension, D_jj=2^-j',
    'endpoint_rank_one_kappa': str(kappa),
    'kernel_compatibility_boundary': 'nilpotent obstruction without metric relation',
    'cavity_constant_majorants': '81 D0^4 and 36 D0^3, dominated by 100 D0^4',
    'interpolation_and_loss_normalization': 'exact rational identities',
    'scope': 'deterministic algebra; no training, numerical integration, or sweeps',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_name('independent_results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
