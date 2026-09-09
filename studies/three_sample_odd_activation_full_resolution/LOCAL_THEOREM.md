# An unconditional common short-time theorem for the exact convex mixture

2026-09-08. Candidate derivation pending independent review. This is a
short-time result, not the requested global theorem. It is included to
separate actual constructed solutions from the continuation modules'
unproved tail premises. All old source files remain unchanged.

## 1. Statement and exact scope

In the original three-hidden-layer raw model, take any three deterministic
RMS-unit inputs, all binary labels, the original Gaussian initialization,
and phi(z)=az+e atan(z), a=1-e, 0<e<=1/2. Let S=10^(-40).
There is one canonical strong population GF on [0,S], unique against
bounded-primal strong competitors on the same spaces, with the original
compact-interval finite GF/simultaneous raw-GD limits and observable
scope. The same S works for every such input triple and every e in this
range. No input-Gram inverse, positive input rank, symmetry, overall gain
or horizon-dependent activation is used.

Under the requested pairwise absolute separation, the initial-motion
conclusions also become actual trajectory statements. The activation
regression error stays positive on this interval in every sample/layer.
The theorem does not assert continuation beyond S with the same uniform
source estimates, and does not resolve the user's global request.

## 2. Uniform controlled primal bounds

First allow arbitrary deterministic controls ||c(t)||_1<=6 on [0,S].
Use the exact source regularization

  D_R(z,q)=a q+e (1+z^2)^(-1) tau_R(q),

where tau_R is the original smooth odd incoming-field clip with
|tau_R(q)|<=|q| and |tau_R'|<=1. In particular |D_R|<=|q|,
|partial_q D_R|<=1, |partial_z D_R|<=|q|, and |phi'|<=1.
It is an approximation to the original gradient field, not a loss gradient.

Stop at joint hidden raw displacement one. Initialized first projection
norm is one and adjacent action norms are at most ten, so every current
primal action/projection norm is at most eleven. Put F=2048. Then

  max_i,ell ||h_i^ell||_2 <=11^3<F,
  ||C(t)||_2<=6Ft,
  max_i,ell ||q_i^ell(t)||_2<=121*6Ft<2*10^6 t.

The bound on q also covers every capped backward field. Each hidden block
speed is at most 6*121||C(t)||_2. Summing the three block norms in Euclidean
norm and integrating gives joint hidden displacement

  D_h(t)<=10^7 t^2.                                      (1)

The same inequalities hold on positive Euler meshes: the sum of h_j t_j
is at most t_k^2/2. Thus no continuous first exit or discrete overshoot is
possible. The cap/mesh-independent actual primal bounds through S are

  ||Z_i^ell||_2<=F,  ||q_i^ell||_2<=Q:=2*10^6 S.           (2)

They hold before and independently of any response bootstrap.

## 3. Same-array value and derivative bounds on a coefficient prefix

Use the exact local Gaussian source equations from Part R of the original
source construction, with deterministic controls and all source covariance
arrays frozen in named derivatives:

  Z=xi+A d, q=zeta+B h, h=aZ+e atan(Z), d=D_R(Z,q).

A is strict causal with block infinity-norm density at most alpha;
B is causal with complete row norm at most b. Every current backward
return remains present. Assume temporarily alpha*S*b<=10^(-20).
The strict/causal resolvents (I-a^2 AB)^(-1) and (I-a^2 BA)^(-1)
have complete row norms at most two. For U=(I-a^2AB)^(-1)A,
its strict density is at most 2alpha, and BU has row at most 2alpha*S*b.

At the SAME actual arrays, Gaussian elimination gives

  Z_G=(I-a^2AB)^(-1)xi+aU zeta,
  q_G=(I-a^2BA)^(-1)zeta+aB(I-a^2AB)^(-1)xi,
  q-q_G=ea BU[g(Z)tau_R(q)]+e(I-a^2BA)^(-1)B atan(Z).

The bounded atan remainder and actual L2 bound (2) imply
||q_G||_2<=2Q+4b for every marginal. Gaussian moments and absorption
of the term 2ea alpha*S*b ||q||_p give the safe estimate

  max_i ||q_i(t)||_p <= M sqrt(p), M=20(Q+b), p>=2.        (3)

All quantities on the right concern the actual source arrays; no affine
covariance comparison or independence between a Gaussian part and its
remainder is assumed. The corresponding forward Gaussian elimination
bounds all Z,h moments as well. Only (3) is needed for production below.

Set Qmax_k=max_i |q_(k,i)|. Then ||Qmax_k||_p<=3M sqrt(p).
The exact derivative equation, with G=diag phi'(Z), V=diag partial_q D_R,
and N=diag partial_z D_R, is

  J=I_xi+A[NJ+V(I_zeta+B GJ)].

Here ||G||,||V||<=1 and ||N_k||<=Qmax_k. Finite causal iteration,
retaining every source-column step, gives

  ||partial_xi Z_k||row<=E_k,
  ||partial_(zeta_j) Z_k||<=alpha h_j E_k,
  ||partial_xi d_k||row<=(Qmax_k+b) E_k,
  E_k=exp(alpha*b*S+alpha sum_(r<k) h_r Qmax_r).           (4)

These are complete current-plus-past row bounds for xi derivatives;
the zeta derivative is strict. For example every B term is bounded by
its causal row b times the past derivative maximum, whereas the strict
A supplies the time step in the Volterra sum. No backward strict density
or minimum mesh step is assumed.

If alpha*S*M<=10^(-20), weighted Jensen gives E E_k^2<2.
Here is a direct numerical justification. From the displayed p-moments,
||Qmax||_k<=6M k for every integer k>=1. The exponential series and
k!>=(k/exp(1))^k yield

  E exp(u Qmax)<=1/(1-6 exp(1) M u)

when the denominator is positive. Apply this with u=2alpha*S, and use
weighted Jensen for the time sum. Multiplication by exp(2alpha*b*S)
still leaves a value below two under the stated inequalities.
Consequently E E_k<=2 and, using ACTUAL raw L2 bounds after controlling
the exponential,

  E[(Qmax_k+b)E_k]<=2(3Q+b).                            (5)

## 4. Actual chronological coefficient closure

All source coefficients are exactly their expected named derivatives
plus the learned two-time moment term. With ||c||_1<=6 and (2), a local
forward population produces next-layer strict density at most

  alpha_next <= 2alpha+6F^2,                            (6)

and a local reverse population produces the next lower causal row at most

  b_next <= 2(3Q+b)+6S Q^2.                             (7)

The Gaussian source groups and their covariances are precisely those of
the actual capped program. The estimates include all sample blocks,
current derivative returns and learned contractions.

Use these explicit outer bounds:

  alpha_1=6, alpha_2=10^9, alpha_3=10^11,
  b_4=6S, b_3=10^12 S, b_2=10^18 S.                    (8)

A_l is the local forward response at layer l and B_(l+1) its reverse
partner; thus the three local pairs use
(alpha_1,b_2), (alpha_2,b_3), (alpha_3,b_4).
The bottom A_1 density and top B_4 readout integrator obey their bounds
exactly. Since S=10^(-40), even the coarse envelopes alpha<=10^11 and
b<=10^18 S give

  alpha*S*b <=10^29 S^2=10^(-51),
  alpha*S*20(Q+b) <= 3*10^30 S^2 <10^(-49).              (9)

Hence (3)--(7) apply with strict slack. The two forward productions are

  2alpha_1+6F^2<10^9,
  2alpha_2+6F^2<10^11.

The top reverse production, with b=b_4, is less than 10^12 S;
the middle reverse production, with b=b_3, is less than 10^18 S.
The learned term 6S Q^2=24*10^12 S^3 is smaller than S.

Chronological construction first builds each current forward row in
increasing layer order, then each current reverse row in decreasing
layer order. Current forward rows depend on older reverse histories;
current reverse rows use the already built higher row. Equations
(6)--(9) therefore strictly improve every newly produced outer bound.
Induction establishes the ACTUAL cap/mesh-uniform source bounds on the
whole controlled interval. There is no assumed long-time coefficient
bound left in this short-time assertion.

## 5. Original physical GF and removal of approximation

For physical GF take c_i=-r_i. On the controlled interval the estimates
above give |f_i|<=||C||||h_i^3||<=6F^2 S, so
||r||_1<=3+18F^2 S<6. A first exit of the control bound is impossible.
The capped physical paths thus exist throughout [0,S], with strict
primal slack and the cap-independent source Gaussian tails just proved.
Fixed-cap local Lipschitz continuation is the one in Part F of the
original construction and does not assume a capped energy identity.

The original asymmetric cap comparison now has its actual hypotheses:
common bounded primal paths and uniform incoming Gaussian tails through
this fixed interval. The error C_S exp(C_S R-c_S R^2) tends to zero.
Its direction version makes the cap limit a strong C1 path, and the
scalar predictor differential identifies the true raw gradient.
The reference-only comparison proves uniqueness versus nonsymmetric
bounded-primal strong competitors and restart within the interval.

At fixed cap/coarse mesh the original finite Gaussian-program theorem
applies. Width is taken first; deterministic raw Euler comparison then
removes the coarse mesh, and reference-tail comparison removes the cap.
The finite readout is retained in these comparisons and tends to zero
only after the fixed-program limit. Simultaneous raw GD has exactly its
original step n^-2 and the original node derivative convention.
The action/adjunction, true-kernel and ordered observational truncation
arguments from the original source and velocity bridge use the same
bounded fields on [0,S], so all original compact-interval observable
conclusions hold there. No fitting clock, growing-transcript Gaussian
claim or cross-width operator-norm convergence is used.

For nonaffinity, initialized preactivation marginal variances lie in
[1/16,1]: |phi'|>=a>=1/2 and Gaussian first-chaos projection preserve
a factor a^2 at each layer. The explicit Gaussian atan regression
margin eta_* from equation (9) of the old quantitative proof applies
throughout this variance range. Telescoping against initialization gives
||z_i^ell(t)-z_i^ell(0)||_2<=3*11^2 D_h(t), which by (1) is much smaller
than sqrt(eta_*)/2 on [0,S]. The square root of optimal atan regression
error is 1-Lipschitz in L2 coupling. Thus the activation regression error
is at least e^2 eta_*/4>0 after cap removal. The previously derived
three-input initial-motion Gaussian calculations now apply to an actual
strong solution whenever the pairwise separation holds.

## 6. Exact remaining boundary

This constructs the original flow on a common nonzero interval for every
admissible triple with an order-one convex mixture such as e=1/2. It is
not a global witness. At a later reached state the readout is nonzero and
the initialized Gaussian source history is adapted; the small reverse
rows b_l=O(S) used in (8) cannot simply be reset to zero. A restart lemma
with actual history-dependent source bounds, and a proof that its step
sizes do not accumulate at a finite time, remain necessary for global
continuation. The Osgood and nonperturbative value modules identify ways
to attack that continuation step but do not establish it.
