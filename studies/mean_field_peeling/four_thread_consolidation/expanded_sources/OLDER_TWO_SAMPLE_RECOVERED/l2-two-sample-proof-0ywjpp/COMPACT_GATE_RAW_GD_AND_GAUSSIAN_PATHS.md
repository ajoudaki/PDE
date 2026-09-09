# Smooth saturation: exact raw-GD confinement and Gaussian first-path bounds

Root candidate, 2026-09-06. NOT YET INDEPENDENTLY AUDITED. This is an
actual finite-width estimate and first-path compactness result, not a
global mean-field identification, uniqueness, or nonlazy theorem.
No experiment or external specialized theorem is used. Fixed smooth
saturation is being tested as an activation, not adopted as the final
model. No parameters, velocities, or updates are clipped.

The proof imports ideas, not assertions, from the previously developed
controlled confinement and raw-GD action arguments. All estimates needed
for the conclusions here are supplied below.

## 1. Model and precise conclusions

Fix R>0 and an even smooth function p, positive on (-R,R), zero outside
[-R,R], and nonnegative everywhere. Let phi_1(z)=integral_0^z p(v)dv
and phi_2(z)=arctan(z). These are fixed independently of width, input
angle, and labels. Write B_ell,P_ell,L_ell for finite upper bounds on
|phi_ell|, |phi_ell'|, |phi_ell''|, respectively. In particular
B_1=integral_0^R p>0 and L_1 is a Lipschitz constant for p.

There are two fixed inputs with ||x_a||^2=d and x_1^T x_2/d=rho,
-1<=rho<1, labels y=(1,-1), and C=[[1,rho],[rho,1]]. At width n,
W^(1) is n by d, W^(2) is n by n, and W^(3) is the RESCALED readout.
All initialization entries, across all three blocks, are independent
CENTERED GAUSSIANS, with laws N(0,1/d), N(0,1/n), and N(0,n^-2),
respectively. Define, for sample a,

    z^(1)_a=W^(1)x_a, h^(1)_a=phi_1(z^(1)_a),
    z^(2)_a=W^(2)h^(1)_a, h^(2)_a=phi_2(z^(2)_a),
    f_a=(W^(3))^T h^(2)_a/n, r_a=f_a-y_a, L=sum_a r_a^2,
    delta^(2)_a=W^(3) phi_2'(z^(2)_a),
    q^(1)_a=(W^(2))^T delta^(2)_a,
    delta^(1)_a=p(z^(1)_a) q^(1)_a, c_a=-2r_a.

Products of two vectors in these displays are coordinatewise. Raw GD
has eta=n^-2 and the simultaneous updates

    W^(1)+=W^(1)+(eta/d) sum_a c_a delta^(1)_a x_a^T,
    W^(2)+=W^(2)+(eta/n) sum_a c_a delta^(2)_a(h^(1)_a)^T,
    W^(3)+=W^(3)+eta sum_a c_a h^(2)_a.                 (1)

Raw parameters are linearly interpolated and hidden fields recomputed.
GF replaces each increment in (1) by its derivative after division by
eta. All norms below are ordinary Euclidean/Frobenius/operator norms;
normalizations are explicit.

For every finite T, there is n_T<infinity, independent of the angle
and dimension, such that on

    E_n={||W^(2)(0)||_op<=8, ||W^(3)(0)||_infinity<=1},

for all n>=n_T and all first neurons i, both raw GD and GF are defined
through T and

    sup_(t<=T)|z^(1)_(a,i)(t)|
      <= |z^(1)_(a,i)(0)|+3R+1,  a=1,2.             (2)

GF has the stronger bound with 3R instead of 3R+1 for all finite
widths, all initial parameters, and all finite T. More precisely its
bound is max(R,|z^(1)_(a,i)(0)|)+2|rho|R. The raw-GD bound has only
an additional D_n=O_T(n^-3/2).

Initially doubly saturated first rows remain exactly frozen for BOTH
schemes, at every width and every step size. For n>=n_T on E_n,
an initially nonfrozen pair never enters the doubly saturated set,
even inside a raw interpolation cell, through T. In the scalar cases
rho=0 and rho=-1, an initially active coordinate stays active through
T. These are gate statements, not assertions of nonzero velocity.

For every 0<alpha<1/4, every sample a, and n>=n_T,

    E[1_(E_n) (1/n) sum_i
       exp(alpha sup_(t<=T)|z^(1)_(a,i)(t)|^2)]
      <= exp(2alpha(3R+1)^2)/sqrt(1-4alpha).          (3)

The same assertion for GF holds without 1_(E_n) or the width threshold,
with 3R in the constant. It bounds even sup over all finite times.
For GD, the quantifier is each fixed T followed by sufficiently large
n; this is not an assertion uniform over T for one fixed width.

Consequently the empirical laws of the joint first initial pair,
two preactivation paths, and two activation paths are compactly
contained in every fixed finite Wasserstein order on continuous-path
space. Here the product space is R^2 x C([0,T];R^2) x
C([0,T];R^2), with the Euclidean initial norm and uniform path norms;
W_s uses, for example, the sum of these three norms as its metric.
Explicitly, for every T, epsilon>0, and finite s>=1 there is a
deterministic W_s-compact set of laws containing these empirical laws
with probability at least 1-epsilon-o(1), for GF and GD. No limit is
identified and no velocity topology is asserted by this conclusion.

## 2. Width-uniform finite-horizon controls for the actual schemes

We give the raw-GD descent proof so that small increments are a
conclusion, not an assumption. More generally assume initial bounds
||W^(2)(0)||_op<=a and ||W^(3)(0)||_infinity<=b. Put

    R_0=sqrt(2)(B_2 b+1), R_*=R_0+1, H=T+1,
    K=2sqrt(2)R_*, M=b+B_2 K H,
    A=a+H K P_2 M B_1, Q=A P_2 M.

Take eta<=1. Stop at a candidate first node with sqrt(L)>R_*.
Every preceding update has sum_a|c_a|<=K. Summing readout and rank
increments gives ||W^(3)||_infinity<=M and ||W^(2)||_op<=A up to
and INCLUDING the candidate exit node through ceil(T/eta). Convexity
gives the same bounds along each raw segment. Thus recomputed fields
satisfy

    ||delta^(2)_a||/sqrt(n)<=P_2 M,
    ||q^(1)_a||/sqrt(n)<=Q.                           (4)

The fixed raw tangent metric is

    d||V^(1)||_F^2/n+||V^(2)||_F^2+||V^(3)||^2/n.

The increment divided by eta is minus the gradient of L in this
metric. For a unit tangent V put alpha_1=sqrt(d/n)||V^(1)||_F,
alpha_2=||V^(2)||_F, alpha_3=||V^(3)||/sqrt(n), all at most one.
Writing J=B_1+A P_1 and F_*=B_2+M P_2 J, differentiation gives

    ||D_V z^(1)_a||/sqrt(n)<=alpha_1,
    ||D_V z^(2)_a||/sqrt(n)<=B_1 alpha_2+A P_1 alpha_1,
    |D_V f_a|<=F_*.

For another unit tangent U, the second preactivation differential is

    V^(2)[p(z^(1)_a)U^(1)x_a]
    +U^(2)[p(z^(1)_a)V^(1)x_a]
    +W^(2)[p'(z^(1)_a)(U^(1)x_a)(V^(1)x_a)].

Its RMS norm is at most 2P_1+A L_1 sqrt(n). The product inequality
used here is ||uv||/sqrt(n)<=sqrt(n)(||u||/sqrt(n))(||v||/sqrt(n)).
The two readout cross terms, top curvature term, and last displayed
term in D_U D_V f_a are therefore bounded in total by

    F_**(n)=2P_2 J+M L_2 J^2+M P_2(2P_1+A L_1 sqrt(n)).

For the top curvature term the readout bound is coordinatewise M,
and (1/n)sum_i |(D_U z^(2)_a)_i(D_V z^(2)_a)_i<=J^2.
This checks all mixed derivatives without an unproved Hessian premise.
The old update has raw norm at most K F_*; its segment residual norm
is at most R_*+sqrt(2)eta K F_*^2, hence at most R_*+1 for large n.
Since D^2 L=2sum_a(Df_a tensor Df_a+r_a D^2f_a), its raw operator
norm on the segment is at most

    H_*(n)=4F_*^2+2sqrt(2)(R_*+1)F_**(n)=O_T(1+sqrt(n)).

The one-dimensional integral Taylor formula along the raw segment
gives, once eta H_*(n)<=1,

    L_(k+1)<=L_k-(eta/2)||grad_raw L_k||_raw^2.

This contradicts the candidate first exit, since L_0<=R_0^2. With
eta=n^-2 the condition holds for all sufficiently large n. Hence
the bounds K,M,A,Q are valid for the actual uncut GD through T.

For GF, differentiation gives exactly -Ldot=||grad_raw L||_raw^2.
The same residual, readout, and rank bounds follow by integration.
In finite dimension the smooth vector field has a unique local flow
(Picard iteration on a bounded parameter ball is a contraction on a
sufficiently short interval). Bounds (4) imply a bounded first-parameter
velocity on each fixed finite horizon, and all other parameter blocks
are bounded there as well. The local construction therefore continues
past every finite endpoint. This proves global finite-width GF, not a
population continuation theorem.

At each GD node define the two-vector u_i=(c_1 q^(1)_(1,i),
c_2 q^(1)_(2,i)). Equations (4) imply |u_i|<=K Q sqrt(n), since
each |q^(1)_(a,i)|<=Q sqrt(n) and sum_a|c_a|<=K. The first-pair
update is exactly

    z_i^+=z_i+eta C diag(p(z_(1,i)),p(z_(2,i)))u_i.     (5)

As ||C||_op<=2, every pair increment has length at most

    D_n=2P_1 K Q eta sqrt(n)=2P_1 K Q n^-3/2.          (6)

The pair velocity on a raw cell has norm |Delta z_i|/eta; averaging
the squared norms, rather than using the maximum-coordinate bound,
also gives (1/n)sum_i |dot z_i|^2<=4P_1^2 K^2 Q^2. The same
bound holds at each time for GF. It will be used only for path
tightness, not for uniform integrability of squared velocities.

## 3. The discrete barrier and exact excursion invariant

Let F={(z_1,z_2): |z_1|>=R, |z_2|>=R}. Its complement consists
of pairs with at least one active gate. For fixed u define
b_u(z)=C diag(p(z_1),p(z_2))u. For z_* in F, b_u(z_*)=0 and

    |b_u(z)-b_u(z_*)|<=2L_1 |u| |z-z_*|.

The closed set F has a nearest point to each z. Therefore

    |b_u(z)|<=2L_1 |u| dist(z,F).                     (7)

Distance to a closed set is 1-Lipschitz. For any 0<=theta<=1,

    dist(z+theta eta b_u(z),F)
       >=(1-2eta L_1|u|)dist(z,F).                  (8)

Enlarge n_T so that 2eta L_1 KQ sqrt(n)<1 and D_n<=1. If an
old node is outside F, (8) keeps its entire next raw segment outside
F. Induction proves non-entry through T. If a node is in F, the
whole first-parameter row has zero derivative/update and the pair is
constant thereafter, regardless of all other neurons' updates.
In particular initially frozen rows are exactly preserved for any eta.

Fix a nonfrozen row and examine a maximal consecutive block of nodes
on which z_1>R. At every node in this block, |z_2|<R by non-entry.
Since p(z_1)=0, (5) gives the exact invariant

    Delta(z_1-rho z_2)=0                            (9)

for every step whose old node belongs to the block. If the block
begins at time zero, its later values satisfy z_1<=z_1(0)+2|rho|R.
Otherwise its first value is at most R+D_n, because the preceding
node had z_1<=R and the increment was at most D_n. Equation (9)
then bounds every value in the block by R+D_n+2|rho|R. This argument
does not sum blocks; it uses only the block containing the node being
estimated. Negative excursions obey the same estimate for -z_1,
and exchanging samples gives

    |z_(a,i)(k eta)|
       <=max(R,|z_(a,i)(0)|)+2|rho|R+D_n.           (10)

Initially frozen pairs satisfy (10) trivially, even if both initial
coordinates are very large. Inside a raw cell the preactivation is
the affine interpolation of its endpoints, so the same absolute-value
bound holds. For rho=0, use (8)'s scalar version for distance to the
complement of (-R,R). For rho=-1 physical inputs have z_2=-z_1 at
all raw states, and the scalar update is eta p(z_1)(u_1-u_2).
Here |u_1-u_2|<=sqrt(2)KQ sqrt(n), covered by the width condition
above. These scalar barriers prove individual gate persistence in
the two stated cases.

For GF the same facts require no step restriction. At any frozen
point z_*, |zdot|<=2L_1|u(t)||z-z_*|. The integral Gronwall
inequality proves constant motion if started there, and, reversing
time on a finite interval, excludes finite-time entry from outside.
The control is integrable for each finite neuron because of the
finite-horizon bounds already proved. On an open excursion z_1>R,
the derivative of z_1-rho z_2 vanishes and |z_2|<R. At a positive
starting time z_1=R; an excursion starting at zero uses its initial
value. The same argument as above now gives (10) with D_n=0. It
also covers infinitely many excursions, since none are summed.

## 4. Gaussian tails, compact containment, and preserved frozen mass

A 1/4-net of the unit sphere in R^n has at most 9^n points: choose
a maximal separated family and compare the volumes of disjoint
radius-1/8 balls to a radius-9/8 ball. Approximating each of the two
unit vectors in a bilinear form gives ||W^(2)(0)||_op at most twice
the maximum on the two nets. Each such form is N(0,1/n), hence

    Pr(E_n^c)<=b_n:=2exp[-(8-2log9)n]+2n exp(-n^2/2). (11)

The second term is the union bound for the actual readout, whose
coordinates have variance n^-2. No initial first-row event is imposed.
For each sample, G_(a,i)=z^(1)_(a,i)(0) is standard Gaussian; the
pair has covariance C and pairs are independent across i. For
B=3R+1, (2) and (|G|+B)^2<=2G^2+2B^2 give

    1_(E_n) exp(alpha sup_t |z^(1)_(a,i)(t)|^2)
        <=exp(2alpha B^2)exp(2alpha G_(a,i)^2).

The Gaussian integral E exp(2alpha G^2)=(1-4alpha)^-1/2 proves
(3) by averaging, without any independence claim about evolved rows.
Markov's inequality consequently gives, uniformly for n>=n_T,

    Pr((1/n)sum_i exp(alpha sup_t|z^(1)_(a,i)(t)|^2)>M_0)
       <=b_n+exp(2alpha B^2)/(M_0 sqrt(1-4alpha)).     (12)

This supplies all finite empirical path-moment bounds and their tail
uniform integrability in probability, not unconditional GD expectation
bounds on E_n^c. For example, for any finite
s and alpha>0, there is a finite constant C_(s,alpha) with

    x^s 1_(x>r)<=C_(s,alpha) exp(alpha x^2)
                              exp(-alpha r^2/2).

One may apply (12) and this bound to each sample and then sum.
For the joint pair, use |(z_1,z_2)|<=|z_1|+|z_2|; the separate
exponential-square bounds imply the required joint norm tails after
decreasing alpha. Activation paths are bounded and phi_1 is Lipschitz.

For completeness, compact containment follows as follows. On E_n the
empirical average of integral_0^T |dot z_i|^2 is at most the constant
4T P_1^2K^2Q^2 from Section 2. Initial-pair norms and path suprema
have an empirical exponential-square bound with arbitrarily high
probability by (12) and the initialization Gaussian integral. Fix
a large bound on this empirical exponential moment. The resulting
deterministic class of laws retains BOTH this moment cutoff and the
displayed average derivative-energy cutoff; define derivative energy
to be infinity outside absolutely continuous paths with square-
integrable derivative. In this class, Markov's inequality makes the mass with large initial
norm or large path derivative energy arbitrarily small. Paths with
both bounds have a uniform square-root time modulus by
|z(t)-z(s)|<=sqrt(|t-s|)(integral |dot z|^2)^(1/2);
their closures are compact in the uniform topology (finite grids,
bounded values, and this modulus give total boundedness and closure).
Thus the laws are tight. Their exponential path-norm bound gives
uniform integrability of every fixed finite power of that norm.
Tightness and this integrability imply relative W_s compactness:
truncate to a common compact set, use a finite small-diameter partition
there to couple convergent cell masses, and bound the transport cost
outside by first splitting at path norm L: its s-moment there is at
most the s-moment above L plus L^s times the mass outside the compact
set. Choose L using moment tails and then the compact set using
tightness. Taking the W_s
closure gives the claimed compact set. Including the initial pair is
a continuous evaluation map, and adding activation paths is a fixed
Lipschitz map, so the same argument proves their joint assertion.
Choose the empirical exponential-moment bound sufficiently large in
(12), then let n grow; this is the stated probability quantifier.

The initial frozen groups also remain present in every scheme. Put
N_s=# {i: both |G_(a,i)|>=R with equal signs} and N_o similarly
with opposite signs. Their unchanged feature contributions imply,
at every continued time, for the ordinary empirical first Gram,

    ((h^(1)_a)^T h^(1)_b/n)_(a,b)
       >= (B_1^2/n) [[N_s+N_o,N_s-N_o],
                      [N_s-N_o,N_s+N_o]]
       >= (2B_1^2/n)min(N_s,N_o) I.                (13)

The inequalities are positive-semidefinite order. For |rho|<1 the
Gaussian pair density is strictly positive, so the two probabilities
m_s,m_o are positive. Variance of each empirical count and Chebyshev
give probability at least

    1-(4/n)[(1-m_s)/m_s+(1-m_o)/m_o]

that (13)'s lower coefficient is at least B_1^2 min(m_s,m_o)>0.
At rho=-1 only the antisymmetric direction is present; no full-rank
lower bound is claimed there. No inverse of a singular Gram is used.

These conclusions improve first-layer tail control for this activation
candidate under actual raw GD, not just under GF or abstract controls.
They do NOT bound q^(1)'s multiplication operator, second-layer
preactivation tails, learned response kernels, or the unweighted
first kernel. They do NOT give strong velocity compactness, identify
any subsequential law with an autonomous population flow, prove
uniqueness or restartability, or establish persistent nonlazy dynamics.
Gate persistence alone does not imply a gate is moving. In particular
none of (2)--(13) is presented as the requested global MF/GF theorem.
