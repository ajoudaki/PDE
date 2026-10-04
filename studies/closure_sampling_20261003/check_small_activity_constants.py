"""Bounded deterministic verification; no neural training or random sampling.

The source cap comes from the frozen, inspected evaluator in the source
proof. Runtime constants are recomputed below from the new inequalities.
The depth-two cap certificate uses exact rational arithmetic and explicit
rational brackets for e, not rounded floating-point comparisons.
"""

from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import math


def source_evaluator():
    path = Path(__file__).with_name("ACTIVATION_CONSTANTS_REFINEMENT_ROUTE.md")
    raw = path.read_bytes()
    assert sha256(raw).hexdigest() == (
        "407f0b1079c7f65dd09960bc45c78a4f266c30054585c9aa9df8b7ab61859660"
    )
    code = raw.decode().split("```python\n", 1)[1].split("```", 1)[0]
    namespace = {"__name__": "frozen_source_evaluator"}
    exec(compile(code, str(path), "exec"), namespace)
    return namespace["evaluate"]


def runtime(L, source):
    h = g = 2.0
    tube = 3.75
    beta = [g * (g * tube) ** (L - j) for j in range(1, L + 1)]
    beta_max = max(beta)
    tuple_norm = lambda a: math.sqrt(a[0] ** 2 + h**2 * sum(x*x for x in a[1:]))
    U = tuple_norm(beta)
    F = g
    for _ in range(1, L):
        F = g * (h + tube * F)
    Ddelta, W = 3 * beta_max + 3, 64.0
    J0 = h * math.sqrt(L) * (7 * beta_max + 3)
    V0 = 14 * F * U
    Ph, Pd, Dr = 17.0, 18 * beta_max + 11, 136.0
    crt = min(1.0, 1 / math.sqrt(224 * F * U), 1 / (6 * J0))
    c = min(source["csrc"], source["cangle"], source["ctime"], crt)
    A0 = 10 + 8*c*c*(Ddelta*Ph + h*Pd)
    Cf = F*(1 + A0)
    Ar, Br = 3*W*Cf, 3*Dr
    Dgram = Ph + L*(Pd*h*h*c + 9*beta_max**2*Ph*c*c)
    X, Y, Z = [0.0]*L, [0.0]*L, [0.0]*L
    Z[-1] = g*Cf
    for j in range(L-2, -1, -1):
        X[j] = g*tube*X[j+1] + g*Ddelta
        Y[j] = g*tube*Y[j+1] + g*A0
        Z[j] = g*tube*Z[j+1] + g*Cf
    Ea = U*Ar + tuple_norm(X) + Ddelta*Cf*math.sqrt(L-1)
    Eq = 16*source["Ksrc"]*tuple_norm(Z)
    gc, Tp = 2+24*J0*c, 6*V0
    A = 4*max(6*Cf+gc*c*Ea, gc*U) + 6*Cf*W + 8*Tp*c
    Bexp = 4*gc*Eq
    Fsrc = (24*Cf + 4*gc*c*Ea + 6*Cf*W
            + 4*gc*(tuple_norm(Y)+c*U*Br) + 48*Dgram)
    O = max(h, W*Cf*c*(3*h+1))
    Rout = (3*h+1)*(W*Cf+Dr)
    Wtail = 2*h+6*h*h+(50*V0+6*J0**2)*c*c
    Ttail = h*Wtail+7*V0*c*c
    general = (Rout + O*(math.sqrt(math.e)*Fsrc+math.sqrt(2)*Bexp*c)
               * math.exp(A*c+Bexp**2*c**4) + 8*Ttail*math.exp(-8))
    decreasing = Bexp*c*c + Bexp*c/(Fsrc+Bexp*c) <= 1
    sharp = (Rout + O*(Fsrc+Bexp*c)*math.exp(A*c+Bexp*c*c)
             + 8*Ttail*math.exp(-8)) if decreasing else None
    return dict(L=L, c=c, A=A, Bexp=Bexp, Fsrc=Fsrc, O=O,
                Rout=Rout, Ttail=Ttail, general=general,
                decreasing=decreasing, sharp=sharp)


def rational_depth_two_certificate():
    elo, ehi = Q(2718, 1000), Q(2719, 1000)
    partial_e = sum((Q(1, math.factorial(k)) for k in range(9)), Q(0))
    # Terms after 1/8! have ratio at most 1/10 after the first 1/9!.
    assert elo < partial_e < partial_e + Q(10, 9*math.factorial(9)) < ehi
    slope = Q(16, 15)
    P, K = [Q(2), Q(158, 15)], [Q(128, 15), Q(2)]
    AH, H2, DH = Q(57032, 225), Q(64712, 225), Q(4)
    E = K[0] + (4*slope)**2*K[1]
    D0_hi = 2*H2**2 + 4*AH**2*(ehi**2-1) + E + slope**2*max(K)**2
    assert D0_hi < 1810000
    V = [slope*K[0]]
    V.append(slope*K[1]+4*slope*V[0])
    G2 = slope+2*V[1]
    G1 = 4*slope*G2+slope**3*K[1]**2+14*V[0]+slope
    assert 128*max(1, G1, G2) < 1810000
    eta_lo = Q(1, 1810000)
    budget_hi, D1_hi = 128*ehi**2, 576*ehi**3*DH**3
    assert ehi+budget_hi < 950 < elo**7
    assert 1810000 < elo**15  # Thus Lambda < 7+15=22.
    c, S = Q(28, 10**8), 16*Q(28, 10**8)
    assert S < 1 and 4*AH*S < 1
    assert 4000*DH*S*S < eta_lo
    assert (16*ehi*DH*S*S)**2*(2*budget_hi) < eta_lo**2
    assert 22*S*S < eta_lo
    assert D1_hi*budget_hi*S**4 < eta_lo**2
    assert 2*slope*K[0]*S*S < 1
    assert (8*c)**2*20 < 1  # The real fitting C_* is below 20.

    f = [slope*x for x in P]
    tc = [slope*x for x in K]
    grad = sum(tc)
    rr, qq = [p*grad for p in P], [x*grad for x in f]
    ee = [rr[0]*P[0]]
    ee.append(rr[1]*P[1]+slope*(qq[0]+tc[1]*f[0]+4*ee[0]))
    jq = [Q(6), 6*4*slope]
    bq = [slope*x for x in jq]
    aj = [jq[0]*P[0]+2*slope]
    aj.append(jq[1]*P[1]+slope*(bq[0]+4*aj[0]))
    TQ = 8*max(f)*max(f[j]*H2+ee[j] for j in range(2))
    TJ = 8*max(f)*max(aj)
    Ksrc = Q(65536, 225)
    AU = max(4*slope*Ksrc,
             2*(slope*Ksrc*(1+f[0]**2+TQ+qq[0])+1))
    BU = 2*qq[0]
    assert S*S*slope*Ksrc*max(2, TJ+bq[0]) < 1
    assert 1024*c*c*(AU+BU) < Q(1, 2)
    assert 224*19*16*c*c < 1 and 6*306*c < 1

    # Conservative runtime upper bounds for every cap c <= 3e-7.
    cap = Q(3, 10**7)
    Cf, U, J0, V0 = Q(210), Q(16), Q(306), Q(4256)
    Ea = U*192*Cf+96+48*Cf
    assert Ea < 656000
    assert 3570**2+4*420**2 < 3668**2
    Eq = 16*292*3668
    assert Eq < 17670000
    gc = 2+24*J0*cap
    assert gc < Q(2003, 1000)
    Dgram = 17+2*(281*4*cap+9*225*17*cap*cap)
    assert Dgram < Q(17001, 1000)
    A = 4*max(6*Cf+gc*cap*Ea, gc*U)+6*Cf*64+8*6*V0*cap
    Bexp = 4*gc*Eq
    Fsrc = (24*Cf+4*gc*cap*Ea+6*Cf*64
            +4*gc*(Q(20002,1000)+cap*U*408)+48*Dgram)
    assert A < 85700 and Bexp < 142000000 and Fsrc < 86700
    assert 64*Cf*cap*7 < 2
    Ttail = 56+(107*V0+12*93312)*cap*cap
    assert Ttail < Q(56000001, 10**6)
    assert 142000000*cap**2+142000000*cap/5016 < 1
    assert 85700*cap+142000000*cap**2 < Q(26, 1000)
    assert 1/(1-Q(26,1000)) < Q(1027,1000)  # exp(x) <= 1/(1-x).
    final = (95032+2*(86700+142000000*cap)*Q(1027,1000)
             +8*Q(56000001,10**6)/elo**8)
    assert final < 280000
    return c, final


if __name__ == "__main__":
    evaluate_source = source_evaluator()
    for depth in (2, 3, 5):
        print(runtime(depth, evaluate_source(depth)))
    cap, error_upper = rational_depth_two_certificate()
    print("Rational certificate: label cap", str(cap),
          "error upper bound <", math.ceil(error_upper))
