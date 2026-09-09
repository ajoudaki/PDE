# A local raw-jet bridge for the actual two-sample controls

Root candidate, 2026-09-06. UNREVIEWED. This is a modular local result,
not the requested global two-label theorem. In particular, failure of
fixed control signs is not failure of the mean-field limit.

Use the fixed activation

  phi(z)=1+0.1 atan(sinh z).

The purpose is to discharge a quantitative local-trajectory bridge for
the static initial cubic law, without assuming a C4 population path in
Lp and without claiming that a Gaussian operator maps all of Lp to Lp.
The latter shortcut is neither used nor needed. Only finitely many
INITIAL Gaussian-query fields need moments beyond order two.

## 1. Explicit modular dependencies and scope

The root has read each mathematical dependency in full. Their roles are
separate; the pending static-law audit must be resolved before promoting
the combined result.

1. SECH_GATE_ACTIVATION_DESIGN.md, SHA256
   c0f67365fbe36af74db9708ce8a32018b30d8164e77c50b068f71299045e4f24:
   bounds 5/6<phi<7/6, |phi'|<=1/10, |phi''|<=1/10, bounded derivatives
   of every fixed order, and initial nondegeneracy. Scoped audit PASS.
   Its fixed-sign characteristic theorem is NOT used here.
2. TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md, SHA256
   9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170:
   the finite Gaussian Euler response construction and estimates on
   feature interval [0,3/2]. Scoped audit PASS for its stated activation.
3. SAME_LABEL_GLOBAL_ASSEMBLY.md, SHA256
   510fd019c204e0e89e0c6bcb99c031a11de974b05323df1c016c72b263f64a44:
   ONLY Sections 1-2 and the symmetry paragraph beginning Section 3.
   Those are both-label local construction/comparison arguments. No
   same-label fitting bound is imported as an opposite-label result.
4. SECH_ACTUAL_CONTROL_SIGN_TEST.md, SHA256
   43c2e8422f3973a883e4dcab86509bfe97b91a5a001c8189b198c69642f53e51:
   finite initial jet identities, joint initial Gaussian-query laws,
   all fixed moments of those fields, and a density lower bound for
   each pair (R^(ell)_a,T^(ell)_a), ell=1,2, near (0,1).
   The revised 744-line text was read by the root. This dependency is
   UNDER its fresh isolated audit. Its unproved remainder
   premise (A) is NOT used. We prove a different sufficient remainder.

Dependencies 2-3 use the elementary finite-program/common-space proof in
L3_GLOBAL_SELF_CONTAINED_PROOF.md, SHA256
bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e,
Sections 2-3 and 5. The common operator spaces may be enlarged to include
the finite initial queries in dependency 4, as justified next.
Initial W^(2)_0 and W^(3)_0
are bounded operators between SEPARATE neuron populations, with their
actual adjoints. All norms below are ordinary population L2 norms or
operator norms; rank-one U tensor V means B maps to U E[VB]. The finite
counterpart is U V^T/n. No normalized-inner-product notation is used.

No external specialized theorem is invoked in this bridge. This document
is not a replacement for importing these dependencies into the eventual
single self-contained final proof.

For the common-space enlargement, smoothly truncate the inputs to every
polynomial-growth operation in the finite static jet program at level M.
The resulting coordinate maps are globally Lipschitz, with constants
growing at most polynomially in M. A degree-d map at a static tuple X
has truncation error at most

  C(E[(1+|X|)^(2d) 1_(|X|>M)])^(1/2)

in L2. The stated static higher moments make this smaller than any
prescribed inverse power of M; empirical moment convergence gives the
same limiting estimate for finite arrays. There are only finitely many
operations, so their polynomial Lipschitz losses are absorbed by choosing
a sufficiently high static moment. Matrix calls cost only their bounded
L2 operator norms. Append any finite collection of cut-Euler or Lipschitz
probe programs and apply the same comparisons. Include all such truncated
programs and finite unions in the countable common-space construction.
The same-matrix comparisons and second-moment passage make their static
approximations Cauchy in L2, with the joint laws in dependency 4. Bounded
initial actions and their transpose pairings pass to those L2 limits.
Thus the jets are realized using the SAME initial operators as the flow;
no untruncated polynomial map is falsely declared globally Lipschitz.

## 2. Why the audited local construction transfers to this activation

Here are the exact activation uses in the local dependencies, so the
transfer is not based on an unspecified analogy. Set a=7/6, e=1/10 and
c=1/5. The new activation satisfies |phi|<=a, |phi'|<=e and |phi''|<=c.
It is smooth with bounded derivatives. The raw bottom root is N(0,C),
where C has diagonal one and off-diagonal rho in [-1,1). No inverse
coordinate change, special arctangent identity, or lower gate bound
occurs in the raw two-sample short response proof.

Its Section 1 only uses these smooth bounded coordinate maps, the two
cuts, zero readout, and the independent Gaussian initial matrices.
Section 2 is a causal construction/induction order independent of phi.
Section 3 bounds the raw first sensitivities using e,c,a. Sections 4-5
use the same three bounds for the middle and top sensitivities and
readout |W^(4)|<=as. Section 6 uses the resulting Gaussian variance and
response-shift bounds. All its numerical inequalities therefore hold
unchanged, for both labels and all C in the stated range. In particular
the actual cut query envelope is

  sup_(R>=1,s<=3/2,a,ell=1,2)
             E exp(|q^(ell)_(R,a)(s)|^2/16)<=2.             (1)

Here q^(2)_R is the top reverse query, and q^(1)_R is the reverse query
after clipping the middle query. Both bottom and middle updates use
the same cap R. The derivative of each cut is at most one.

Sections 1-2 of the assembly use bounded phi, phi', phi'', the raw C
matrix, bounded initial operators and adjoints, the zero-readout bound,
and (1). Their Picard/comparison arguments consequently apply unchanged.
They construct the actual uncut feature flow theta on [0,3/2], uniquely
restartable on reached subintervals, and its cut references theta_R.
In the sum of the two raw first-field L2 distances, the two operator
distances and the readout L2 distance, denoted d, they give

  sup_(s<=3/2) d(theta(s),theta_R(s))
       <= C exp(C R-R^2/256).                              (2)

Changing the finite constants or the negative quadratic coefficient is
harmless; (2) records one form of the bound. For both reverse queries
and the middle deltas, the analogous error is bounded by a polynomial
in R times the right side of (2), hence also decays faster than every
inverse power of R. This follows by the top Lipschitz comparison, the
middle three-term cut comparison and one more adjoint action. No tail
assumption on an uncut competitor is needed.

For any two bounded-primal states with bounded reference readout, the
same-cap field satisfies

  ||V_R(A)-V_R(B)|| <= C(1+R)d(A,B).                       (3)

The constant is uniform for the bounded sets used below. The middle
gate-difference term costs R once; the bottom gate-difference term also
costs R once, but the propagated query difference is multiplied only
by bounded phi'. Thus the bound is linear, not quadratic, in R.

For y=(1,sigma), sample exchange combined with multiplication of the
readout by sigma is an isometry of the initial law and cut equations.
This is a readout sign reversal only in the opposite-label case.
The backward fields transform as q_a maps to sigma q_(3-a); the odd
cuts preserve this relation. Deterministic finite-program empirical
limits give f_2=y_1y_2 f_1; cut removal preserves this symmetry. This
argument is independent of activation parity. Hence, for y=(1,sigma),
g=(f_1+sigma f_2)/2 starts at zero and the local physical clock obeys
ds/dt=4(1-g). It is strictly increasing on a sufficiently short interval.
No claim that this clock reaches all physical times is made here.

## 3. The initial jets used in the approximation

Write Z^(ell)_a,H^(ell)_a for the initialized population fields. The
symbols with bracket [j] below denote formal j-th derivatives at feature
time zero, not values of a positive-time field. Put y=(1,sigma), sigma=±1.
The globally sign-reversed label pair is obtained by reversing W^(4)
and both backward queries. Let

  V=(1/2)sum_a y_a H^(3)_a,
  delta^(3)_[1],a=V phi'(Z^(3)_a),
  R^(2)_a=(W^(3)_0)^*delta^(3)_[1],a,
  delta^(2)_[1],a=phi'(Z^(2)_a)R^(2)_a,
  R^(1)_a=(W^(2)_0)^*delta^(2)_[1],a,
  delta^(1)_[1],a=phi'(Z^(1)_a)R^(1)_a.

Define the second hidden/raw derivatives recursively by

  Z^(1)_[2],b=(1/2)sum_a C_ba y_a delta^(1)_[1],a,
  H^(1)_[2],a=phi'(Z^(1)_a)Z^(1)_[2],a,
  W^(ell)_[2]=(1/2)sum_a y_a
                    delta^(ell)_[1],a tensor H^(ell-1)_a,
  Z^(ell)_[2],a=W^(ell)_[2]H^(ell-1)_a
                         +W^(ell)_0 H^(ell-1)_[2],a,
  H^(ell)_[2],a=phi'(Z^(ell)_a)Z^(ell)_[2],a, ell=2,3,
  V_2=(1/2)sum_a y_a H^(3)_[2],a.

The recursion is in increasing layer order after the initial backwards
queries have been made. Define the cubic backward derivatives by

  delta^(3)_[3],a=V_2 phi'(Z^(3)_a)
                      +3V phi''(Z^(3)_a)Z^(3)_[2],a,
  T^(2)_a=(W^(3)_0)^*delta^(3)_[3],a
                         +3(W^(3)_[2])^*delta^(3)_[1],a,
  delta^(2)_[3],a=phi'(Z^(2)_a)T^(2)_a
                   +3phi''(Z^(2)_a)Z^(2)_[2],a R^(2)_a,
  T^(1)_a=(W^(2)_0)^*delta^(2)_[3],a
                         +3(W^(2)_[2])^*delta^(2)_[1],a,
  delta^(1)_[3],a=phi'(Z^(1)_a)T^(1)_a
                   +3phi''(Z^(1)_a)Z^(1)_[2],a R^(1)_a.

Finally set

  Z^(1)_[4],b=(1/2)sum_a C_ba y_a delta^(1)_[3],a,
  W^(ell)_[4]=(1/2)sum_a y_a [
       delta^(ell)_[3],a tensor H^(ell-1)_a
              +3delta^(ell)_[1],a tensor H^(ell-1)_[2],a], ell=2,3. (4)

These are exactly the zero-readout finite product-rule identities from
the static-law dependency: all trained-matrix terms are retained. Every
scalar field in (4) and the preceding display belongs to Lp for every
finite p. All matrix increments displayed are finite sums of rank-one
operators with finite Hilbert--Schmidt norms. This is a claim about the
specified INITIAL query list, not a boundedness assertion for arbitrary
inputs to either Gaussian operator.

In particular, for each ell=1,2 and sample a, the pair (R^(ell)_a,T^(ell)_a)
has a density bounded below on every sufficiently small fixed box near
(0,1), as proved in dependency 4 (currently under audit).

## 4. A small-jet multiplication estimate

We record the elementary estimate that avoids any unproved Lp operator
bound. Suppose A_u is uniformly bounded pointwise and

  sup_(0<=u<=t)||A_u||_2<=C t^4,
  J_u=uR+(u^3/6)T,

where R,T have all finite moments. For each finite p>=2,
sup_(u<=t)||J_u||_p<=C_p t. Split at |J_u|=sqrt(t). On the first set,
||A_u J_u||_2<=sqrt(t)||A_u||_2. On the second set use the pointwise
bound on A_u and

  ||J_u 1_(|J_u|>sqrt(t))||_2
       <= ||J_u||_p^(p/2) t^((2-p)/4)
       <= C_p t^((p+2)/4).

Taking p>=16 therefore proves

  sup_(u<=t)||A_u J_u||_2<=C t^(9/2).                    (5)

Larger p makes the second term arbitrarily small in powers of t.
The same bound holds if J_u is replaced by a cut of J_u whose magnitude
does not exceed |J_u|. Also, for any Rcap>=1 and any desired exponent N,

  sup_(u<=t)||tau_Rcap(J_u)-J_u||_2<=C_N t^N.             (6)

Indeed the difference is bounded by 2|J_u| on |J_u|>Rcap, and the same
moment estimate applies with threshold Rcap>=1 and sufficiently large p.
All constants concern the finitely many initial jet fields. No evolved
query is assumed to have those Lp bounds in (5)-(6).
Every constant below is independent of u, sufficiently small terminal
feature time t, and the comparison cap. Constants may depend on the
fixed input correlation and label mode.

## 5. A raw approximate path with bounded readout

Fix a sufficiently small terminal feature time t in (0,1]. Here t is a
local feature-time parameter, NOT physical time. For 0<=u<=t define

  Z^(1)_(P,b)(u)=Z^(1)_b+(u^2/2)Z^(1)_[2],b
                                  +(u^4/24)Z^(1)_[4],b,
  W^(ell)_P(u)=W^(ell)_0+(u^2/2)W^(ell)_[2]
                                  +(u^4/24)W^(ell)_[4], ell=2,3,
  bar W^(4)_P(u)=uV+(u^3/6)V_2,
  W^(4)_P(u)=tau_sqrt(t)(bar W^(4)_P(u)).                (7)

The last cut is ONLY part of an approximate comparison path, not the
network or its limiting activation/dynamics. The smooth odd function
tau_K is the identity on [-K,K], has derivative in [0,1], and has
|tau_K(x)|<=min(|x|,2K). The raw readout of P has bound 2sqrt(t).
All primal and operator norms of P are bounded uniformly for t<=1.
At rho=-1 its first-field pair stays in the correct one-field subspace,
because both derivative arrays in (4) lie in the image of C.

The readout cut and its derivative have negligible error to every fixed
power of t in every fixed Lp. To check this, |V|<=a, and for small t,
at<=sqrt(t)/2. A changed value or derivative at any u<=t therefore
requires |V_2|>=3t^(-5/2). The errors are bounded respectively by
2t|V|+(t^3/3)|V_2| and 2|V|+t^2|V_2|. Markov's inequality with higher
moments of V_2 proves the assertion, uniformly over u<=t. The path is
C1 into the raw Banach state space; its readout derivative is the
ordinary chain rule with the fixed threshold sqrt(t).

Recompute all hidden fields from this RAW path. Bounded derivatives of
phi, the initial jet moments, and the bounded operator norms give

  sup_(u<=t)||Z^(ell)_(P,a)(u)
              -Z^(ell)_a-(u^2/2)Z^(ell)_[2],a||_2<=C t^4,
  sup_(u<=t)||H^(ell)_(P,a)(u)
              -H^(ell)_a-(u^2/2)H^(ell)_[2],a||_2<=C t^4. (8)

For ell=1 the first identity is (7), and the second follows from the
pointwise Taylor remainder C|increment|^2 and the L4 jet bounds.
For ell=2 multiply this feature expansion by W^(2)_P. Its coefficient
of u^2 is exactly Z^(2)_[2]/2; the remaining operator/vector products
are O(t^4) in L2. Apply the bounded Lipschitz phi and Taylor-expand only
at the known field Z^(2)+(u^2/2)Z^(2)_[2]. This yields the second
identity at ell=2 using only the static L4 norm of Z^(2)_[2]. Repeat
the identical two operations at ell=3. No Gaussian operator is asked
to map an Lp remainder to Lp.

## 6. Query and velocity defects of this path

Let q^(ell)_(P,R,a) be the recomputed cap-R queries, with the middle cut
included before the first reverse action. For all R>=1, uniformly in
u<=t, we claim

  ||q^(ell)_(P,R,a)(u)-uR^(ell)_a-(u^3/6)T^(ell)_a||_2
                                      <=C t^(9/2), ell=1,2. (9)

For ell=2, replace the recomputed top preactivation by
Z^(3)+(u^2/2)Z^(3)_[2]. The L2 error in its gate is O(t^4) by (8),
and multiplication by W^(4)_P costs at most 2sqrt(t), giving O(t^(9/2)).
Replace this readout by its uncut polynomial, at negligible error.
Taylor-expand the remaining scalar gate about Z^(3). Its product
with uV+(u^3/6)V_2 is

  u delta^(3)_[1]+(u^3/6)delta^(3)_[3]+O_L2(t^5).

All products in this Taylor remainder use only static jet moments.
Multiplying by (W^(3)_P)^* yields the claimed cubic query, with its
3(W^(3)_[2])^*delta^(3)_[1] term. Other rank products are O(t^5).

For the middle delta insert the cubic query J_u from (9). The query
error costs only bounded phi' and the Lipschitz constant one of tau_R.
Removing the cut on J_u has negligible error by (6). The changed gate
between the recomputed preactivation and its quadratic approximation
is pointwise bounded and O(t^4) in L2 by (8). Its product with J_u
is therefore O(t^(9/2)) by (5), NOT by an Lp operator estimate.
The remaining scalar Taylor expansion is

  u delta^(2)_[1]+(u^3/6)delta^(2)_[3]+O_L2(t^5).

The adjoint W^(2)_P gives (9) at ell=1, retaining its trained-matrix
term in exactly the same way. Apply (5)-(6) once more to this first
query and the raw first gate to get the bottom velocity expansion.

The rank-one velocity products also have the correct cubic expansions:
the third derivative of delta tensor H at zero is
delta_[3] tensor H+3delta_[1] tensor H_[2], precisely (4). Their
remaining defects are O(t^(9/2)) in operator norm. Here the rank-one
norm is bounded by the product of two L2 norms; no pointwise bound on
a jet field is needed. The raw first-field defect is O(t^(9/2)).
The readout velocity defect is O(t^4), because (8) gives

  (1/2)sum_a y_a H^(3)_(P,a)
                       =V+(u^2/2)V_2+O_L2(t^4),

and the derivative of the cut in (7) changes this polynomial derivative
only negligibly. Consequently, in the state norm from Section 2,

  sup_(u<=t)||P'(u)-V_R(P(u))||<=C t^4, all R>=1.        (10)

The same proof with Hilbert--Schmidt norms controls both matrix
increments if that stronger state norm is desired.

## 7. Compare, then remove the comparison cap

Choose R=t^(-1/4). The cut flow and P start at exactly the same state.
Equations (3),(10) and the integral Gronwall estimate give

  sup_(u<=t)d(theta_R(u),P(u))
       <=C t^5 exp(C(1+R)t)<=C' t^5.                    (11)

The primal bounds needed for (3) are fixed uniformly here, since both
the cut path and P have the bounds described above. Equation (2) is
smaller than every power of t at this R: the negative term is
-t^(-1/2)/256, whereas the positive term is C t^(-1/4).
The same holds for the two query cut-removal errors.

Top query comparison between theta_R and P costs C times (11).
Middle-delta and first-query comparison cost at most C(1+R) times
(11), which is O(t^(19/4)) and hence smaller than O(t^(9/2)).
Combine with (9) and the cut-removal error to obtain, for ell=1,2,

  sup_(0<=u<=t)
  ||q^(ell)_a(u)-uR^(ell)_a-(u^3/6)T^(ell)_a||_2
                                            <=C t^(9/2). (12)

This is an estimate for the ACTUAL uncut population feature flow.
It is not obtained by interchanging width and time derivatives, and
does not assert that the full flow is C4 into Lp. It is exactly the
quantitative estimate needed below.

## 8. Actual sign changes, if the static-law dependency passes

Fix ell,a. By the density lower bound on any fixed compact box for
(R,T)=(R^(ell)_a,T^(ell)_a),
the event

  E_t={-t^2/10<=R<=-t^2/12, 1<=T<=9/8}

has probability at least c_0 t^2 for every sufficiently small t.
The cubic polynomial J(u)=uR+u^3T/6 satisfies on E_t

  J(t)>=t^3/15,
  J(t/2)<=-t^3/24+3t^3/128=-7t^3/384.

By (12), the probability that either endpoint error exceeds t^3/200
is at most C t^3, using the squared L2 error t^9 divided by t^6.
This is o(t^2). Subtract it from P(E_t). For sufficiently small t,

  P{q^(ell)_a(t/2)<0<q^(ell)_a(t)}>= (c_0/2)t^2.         (13)

This conclusion concerns deterministic feature times. Define the local
physical inverse clock by

  vartheta(s)=integral_0^s dv/[4(1-g(v))].

Since g is continuous and g(0)=0, restrict the interval so |g|<=1/2.
Then vartheta is strictly increasing and s/6<=vartheta(s)<=s/2.
The physical endpoints are vartheta(t/2) and vartheta(t), not necessarily
physical times in a one-to-two ratio. The query values and event
probability are unchanged. The residual/label multipliers have fixed
nonzero signs on this interval, so including them in the controls does
not remove the sign reversals.

The endpoint claim also rules out a fixed sign almost everywhere in
time, without assuming a continuous scalar representative for q^(1).
Both constructed queries are continuous into L2: the fields/actions
are continuous, the readout is bounded pointwise, and bounded converging
gates preserve a strongly convergent L2 product by truncation of a fixed
factor. Suppose a measurable sign b(omega) made b q(u,omega)>=0 for
almost every (u,omega). The function u maps to ||(bq(u))_-||_2 is
continuous and zero for almost every u, hence zero at every deterministic
u. The resulting two nonnegative signed endpoint variables cannot have
opposite signs on a positive-probability set. If signs are initially
only described as existing separately for each path, choose them
measurably from the sign of the time integral of q, with sign +1 on
zero paths; Fubini and L2 integrability justify this choice. Thus (13)
is not an artifact of choosing exceptional values at two times.

Thus, once the explicitly pending static-law audit is clean, (13)
discharges the proposed fixed-sign discriminator for the actual local
canonical population flow, for both query layers, both label modes
and all rho in [-1,1). At the antiparallel endpoint this concerns the
named query components, not a claim that two first coordinates become
independent. Constants need not be uniform in rho.

The conclusion does not preclude an activation-specific estimate for
sign-changing trained controls. It identifies a real restriction that
cannot simply be assumed away. The global opposite-label continuation,
the complete two-label one-document theorem, and its several independent
whole-document audits are still open.
