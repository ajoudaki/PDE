"""Independent arithmetic spot checks of the frozen paper's coefficient ledgers.

No paper imports; all formulas transcribed from the permitted five files.
Finite checks supplement, and do not replace, the symbolic audit.
"""
from decimal import Decimal, getcontext
getcontext().prec = 80
D = Decimal
failures = []
checks = 0

def check(tag, lhs, rhs, beta, L):
    global checks
    checks += 1
    if lhs > rhs * D('1.00000000000000000001'):
        failures.append((tag, str(beta), L, str(lhs / rhs)))

for beta in map(D, ['10', '16', '100', '10000']):
  for L in [2, 3, 4, 8, 16, 32]:
    b, s, t2 = beta - 1, beta, beta
    exp = D(1).exp()
    H, P, k, tau = {}, {}, {}, {}
    H[1], P[1] = max(1, b + 20*s), D(3)
    for j in range(2, L+1):
        H[j] = max(1, b + 10*s*H[j-1])
        P[j] = H[j-1]+10*s*P[j-1]+1
    k[L] = H[L]
    for j in range(L-1, 0, -1):
        k[j] = 10*s*k[j+1]
    tau = {j: s*k[j] for j in k}
    f = {j: s*P[j] for j in P}
    A = 2*s*P[L]+2*s*s*sum(k[j]*P[j-1] for j in range(2,L+1))
    Ds = t2*sum(P[j]**2 for j in P)
    Hs = A+t2*sum(P[j]**2*k[j] for j in P)
    Es = t2*sum((10*s)**(2*(j-1))*k[j] for j in P)
    Ts = 2*Hs**2+4*A**2*(exp**2-1)
    D0 = (1+b+s)*(1+Ts+Es+s*s*max(k.values())**2)
    D1 = 576*exp**3*(1+b+s)*Ds**3
    CF = s*(8*max(f.values())**2+max(H.values())**2+1)
    Cabs = 8*(D0+1)
    V0 = {1: tau[1]}
    for j in range(2,L+1):
        V0[j] = tau[j]*H[j-1]**2+10*s*V0[j-1]
    G0 = {L: s*H[L]+14*t2*V0[L]+s}
    for j in range(L-1,0,-1):
        G0[j] = 10*s*G0[j+1]+s**3*k[j+1]**2*H[j]+14*t2*V0[j]+s
    WG = 128*(1+max(H.values())+s*max(V0.values())+max(G0.values()))
    eta = min(D(1), 1/(1024*Cabs*WG))
    B = 1024*exp**2*L
    Lambda = (exp+B).ln()+(1/eta).ln()
    Sstar = min(D(1),1/(4*A),(eta/(4000*Ds)).sqrt(),
                (eta/(16*exp*Ds*(2*B).sqrt())).sqrt(),
                (eta/Lambda).sqrt(),(eta**3/(D1*B)).sqrt().sqrt(),
                (1/(8*D0*CF)).sqrt())
    S = 16*beta**(-30*L)
    check('S <= Sstar', S, Sstar, beta,L)
    for j in P:
        check('H_j', H[j],3*beta**(2*j),beta,L)
        check('P_j', P[j],beta**(3*j-2),beta,L)
        check('k_j', k[j],3*beta**(4*L-2*j),beta,L)
        check('tau_j',tau[j],3*beta**(4*L-2*j+1),beta,L)
    for tag,lhs,power in [('A',A,5*L-2),('D',Ds,6*L-2),('Hstar',Hs,8*L-2),
                         ('Estar',Es,6*L-2),('Tstar',Ts,16*L-3),('D0',D0,16*L-2),
                         ('D1',D1,18*L-2),('CF',CF,6*L),('Cabs',Cabs,16*L-1),
                         ('WG',WG,9*L+1),('eta inverse',1/eta,25*L+4)]:
        check(tag,lhs,beta**power,beta,L)
    CG=32*max(D(1),max(H.values()),max(tau.values()))
    Ksrc=16*Cabs*(1+CG)
    check('Ksrc',Ksrc,beta**(21*L),beta,L)
    gs=tau[1]+sum(tau[j]*H[j-1] for j in range(2,L+1))
    rs={j:P[j]*gs for j in P}
    qs={j:f[j]*gs for j in P}
    js={j:20*(10*s)**(j-1) for j in P}
    bs={j:s*js[j] for j in P}
    ee={1:t2*rs[1]*P[1]}
    aa={1:t2*js[1]*P[1]+2*s}
    for j in range(2,L+1):
        ee[j]=t2*rs[j]*P[j]+s*(qs[j-1]+tau[j]*H[j-1]*f[j-1]+10*ee[j-1])
        aa[j]=t2*js[j]*P[j]+s*(bs[j-1]+10*aa[j-1])
    TQ=8*max(f.values())*max(f[j]*Hs+ee[j] for j in P)
    TJ=8*max(f.values())*max(aa.values())
    for d in [1,2,10,100]:
        root=D(d+3).sqrt()
        Us=[4*s*Ksrc]
        Vs=[2*(32*root+2*s*Ksrc*S*S+1)]
        Ufs=[4*s*Ksrc]
        for j in range(2,L+1):
            bracket=s*Ksrc*(H[j-1]**2+f[j-1]**2+S*TQ+S*S*H[j-1]*qs[j-1])
            Us.append(2*(bracket+16*root*qs[j-1]+1))
            Ufs.append(2*(bracket+64*qs[j-1]+1))
            Vs.append(2*(16*root*bs[j-1]+s*Ksrc*S*S*(TJ+H[j-1]*bs[j-1])+1))
        check('U',max(Us),beta**(26*L)*root,beta,L)
        check('V',max(Vs),beta**(2*L)*root,beta,L)
        check('Ufin',max(Ufs),beta**(26*L),beta,L)
    K=H[L]**2+S*S*(tau[1]**2+sum(tau[j]**2*H[j-1]**2 for j in range(2,L+1)))
    check('K',K,beta**(14*L),beta,L)

print('Coefficient inequality checks:', checks)
print('Violations:', len(failures))
for failure in failures[:30]:
    print(failure)
