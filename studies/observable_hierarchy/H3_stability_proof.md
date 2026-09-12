# Explicit short-horizon stability preflight

Status: candidate contained proof and exact scalar implementation; not a C-H3
solver, effective closure-order theorem, or numerical demonstration.
Author: coordinator `/root`. Dependency: complete C.4.7.3 source proof, especially
(N9)–(N19), in dependencies_v1.md; canonical target and actual finite-GF
identification are C.4.7.1–5. The proof preserves those model conventions.

## A source cap at T=1/200

Set Y=1, T=1/200, C=101/10000, R=10101/10000, B=1/32 and

    D=B+2 R C^2 T,
    A_B=4 R exp(6 R D T+8 R^2 T^2 C^2),
    d=2 R T+2 C,
    Psi=d exp(d T(A_B+2 R)).

The exact rational program H3_stability.py proves exp(2T)<R,
exp(2T)-1<C and Psi<B. Its exponential enclosure is the finite Taylor sum
through n and a geometric upper remainder: after the first omitted term all
term ratios are at most x/(n+2)<1. Every displayed check is an integer/rational
inequality. Decimal displays do not enter the proof.

For any finite law with |y|<=1 and any positive Euler mesh of total length <=T,
(N9) bounds the readout supremum by C and all residuals by R. Suppose all
previous beta rows obey B. The complete causal lower pulse estimates (N10)–(N14)
give the density A_B, and the upper derivative recursion (N15)–(N16) bounds the
current beta row by Psi<B. There is no current unknown row on the right: its
lower w and alpha depend on previous steps only, and its upper recursion has
strictly earlier memory plus its single distinguished current slot. The initial
row is zero. Induction therefore gives beta<=B for every node, without any
law-cardinality, mass, mesh-count or Gram-rank dependence. This is precisely the
short-time case of the sufficient inequality (N19), not its false continuation
to T=40.

Consequently every recomputed passive query has the same-carrier decomposition
Q=G+J, where G is centered Gaussian of variance <=C^2 and |J|<=D. The two need
not be independent. Affine interpolation is covered by adding a shorter final
step, as in the dependency. On every H2-admitted law, its already identified
canonical solution is the limit of such finite-law Euler paths. Source
cross-covariances (N3), their Gaussian isometry, and strong convergence of upper
backward fields pass G in L2. The remainders J pass in L2 and retain |J|<=D by
an almost-sure subsequence. This proves the same marginal decomposition for
every time and input of that canonical solution. It does not claim a Gaussian
bound for a time/input supremum, nor for arbitrary approximate action fields.

If r>=D, scalar domination and Markov's inequality give

    ||Q 1_{|Q|>r}||_2 <= 4(C+D) exp(-(r-D)^2/(8 C^2)).

Indeed write |G|<=C|Z| in distribution, bound |Q| by C|Z|+D, and use
1_{|Z|>a}<=exp((Z^2-a^2)/4). The elementary Gaussian integrals
E exp(Z^2/4)=sqrt(2) and E Z^2 exp(Z^2/4)=2sqrt(2), obtained by completing the
square, bound the square of the left side by
2 exp(-a^2/4)(2sqrt(2)C^2+sqrt(2)D^2). Its square root is below the stated
constant. Smaller variance satisfies the same domination. The bound is uniform
in marginal time and input, so averaging the individual tails over the law
does not change it. At r=1/5 the exact program proves this bound <10^-15.

This proof resolves an explicit small-time tail/stability constant. It does not
numerically specify the previously existential H2 neighborhood radius.

## Explicit one-reference error propagation

Compare two common-carrier states with the SAME base A0, HS increments, action
norms <=a, readout L2 norms <=c, reference readout supremum <=c, and labels <=1.
Let x,k,z be row L2, middle HS and readout L2 differences, and let R=1+c.
Use |tanh|,|tanh'|<=1, Lip(tanh)<=1, Lip(tanh')<=2. The elementary subtractions
give, uniformly in u,

    dz2 <= a x+k,
    df <= z+c(a x+k),
    dd2 <= z+2c(a x+k),
    dQ <= a dd2+c k.

At a cutoff s>=0, subtract the lower gate by splitting the reference Q:

    dd1 <= dQ+2s x+2 tau_s(Qref).

The three velocity differences are then bounded respectively by

    2ac df+2R dd1,
    2c df+2R(dd2+c x),
    2df+2R dz2.

These estimates use the actual transpose and rank HS norm; every product has
a bounded multiplier or a two-factor scalar contraction. Collecting x,k,z
gives coefficients

    Lx=2a²c²+4Rc a²+2c²a+2Rc(2a+1)+2(c+R)a+4Rs,
    Lk=2ac²+2Rc(2a+1)+2c²+4Rc+2(c+R),
    Lz=2ac+2Ra+2c+2R+2.

Thus for e=x+k+z, sum velocity difference <=L(s)e+4R tau_s(Qref),
where L=max(Lx,Lk,Lz). The canonical path satisfies the needed bounds with
a=201/100,c=1/50: energy gives ||c||infty<=2T and
||K||HS<=2T², while ||A0||<=2. An approximate path must SEPARATELY certify
its own stated bounds and its use of the same base A0.

If an absolutely continuous represented path has full canonical RHS defect
at most b, then its error to this canonical path satisfies a.e.

    e' <= L(s)e+b+4R tau_s(Qref).

Norms of absolutely continuous Hilbert curves justify the upper derivative,
also at zero. Multiplying by exp(-Lt) and integrating proves

    e(t) <= exp(Lt)e(0)+(exp(Lt)-1)(b+4R tau_s)/L.

At s=1/5 the exact scalar code proves L<8.3 and, conditionally on b<=10^-5
and e(0)=0, e(T)<5.2*10^-8. This is a propagation calculation, not a claim
that any proposed numerical path has that small defect. For predictions the
same-base bound is df<=z+c(a x+k); hidden upper error is <=a x+k. Those
factors must be applied to the separate requested observation tolerances.
Changed-base H2 action error is not an HS state error and must be separately
bounded or removed by an explicit same-base lift before using this calculation.

## Remaining obligations

An effective certified closure still needs a finite numerical representation
with rigorously computable full defects, Gaussian/population/input integrals,
time and arithmetic bounds, and a proved terminating refinement rule. No
residual supplied by an assumed oracle is an implementation of those tasks.
No numerical trajectory or resolved learning signal is asserted by this note.
