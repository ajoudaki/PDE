# Constructed corrections: what their flow inequalities actually prove

2026-09-16. Current account of the user-requested potential-design stage.
An explicit matrix correction and a separate cubic/quartic flow correction
have been constructed. The broader all-rho initialized exponential theorem
has NOT been proved. These are internal research results, not promotion.

The governing contract is correction_contract.md. The canonical fixed p=1
d=3 closure, complete initialization correlations, fixed dictionary,
unhalved physical square loss, evolving w,c,M and actual M^T are retained.
The original d=2 circle problem remains distinct. No experiments ran.

## 1. A simple corrected formula

For signed inputs v_i=y_i u_i with y=(+1,+1,-1), define the normalized
signed prediction vector p_i=f(v_i)/sqrt(3), target n=1/sqrt(3), error
xi=p-n, and L=|xi|^2. Let q=E2[c^2]. The frozen initialized upper Gram is

    (Gamma0)_ij=E2[H_i(0) H_j(0)]/3.

The proposed matrix correction is

    mu0=(n^T Gamma0^(-1)n)^(-1),
    Phi_mat=L+mu0(1+q) xi^T(Gamma0+p p^T)^(-1)xi.          (1)

Gamma0 and mu0 depend only on prescribed inputs and exact initialization.
The other quantities come from the complete present state. No reference
endpoint, future trajectory, response jet or new evolving variable occurs.

The full proof in correction_matrix.md establishes L<=Phi_mat and
Phi_mat(0)=2. Unlike the inverse-current-Gram template, (1) is well defined
when the current full tangent Gram loses rank. The separate proof
correction_initial_rank.md establishes Gamma0>0 for any three unit signed
inputs with no equal or opposite pair, not only near the rho family.
That is a statement about the formula's domain, not its all-time sign.

The geometric meaning of mu0 is exact: its reciprocal is the minimum
squared readout norm needed to interpolate the labels using initialized
upper features. This is a fixed, justified geometric target, not an
assumption that hidden features stay frozen during training.

At symmetric rho data, p=Fn and Gamma0 has mean eigenvalue C0. Then
mu0=C0 and (1) reduces EXACTLY to the original scalar potential

    L[1+C0(1+q)/(C0+F^2)].

Thus (1) extends the old formula rather than introducing an unrelated
observable which happens to decrease in a different model.

## 2. The missing terms and the actual decay defect

Choose an orthonormal frame E for n-perpendicular. Decompose

    p=Fn+E zeta, e=1-F,
    Gamma0=[[C0,beta0^T],[beta0,D0]], d=C0+F^2,
    h=beta0+F zeta,
    B=D0+zeta zeta^T-h h^T/d.

Here zeta records the two disagreement directions. The exact completed
square in the new correction is

    xi^T(Gamma0+p p^T)^(-1)xi
       =e^2/d+(zeta+e h/d)^T B^(-1)(zeta+e h/d).           (2)

The added structure therefore mixes disagreement with mean error and
with both initialized coupling beta0 and current coupling F zeta.
It is not a separate requirement that every same-class distance decrease.
Because B is a Schur complement of Gamma0+p p^T, it is positive on the
entire declared data domain, including current tangent rank-loss states.

The normalization also accounts for the initialized mixed directions:

    mu0=C0-beta0^T D0^(-1)beta0.                           (3)

Near symmetry beta0 is first order in the input perturbation; its
contribution in (3) is second order. This is a concrete correction term
revealed by the data geometry.

Let K be the full probability-normalized tangent Gram of the three
predictions, including row, matrix and readout blocks. The exact equations
are p'=-2K xi, q'=-4xi^T p. Put R=(Gamma0+p p^T)^(-1). Then

    Phi_mat'=-4xi^T K xi
       -4mu0[(1+q)(1-p^T R xi) xi^T R K xi
                              +(xi^T p) xi^T R xi].        (4)

All terms caused by the moving metric are included in (4). No K' term
occurs because this chosen metric uses the current predictions and a
frozen initialized matrix, not the inverse of K.

At initialization, the proposed decay defect at rate 4mu0 is

    Phi_mat'(0)+4mu0 Phi_mat(0)
       =-4(C0-mu0)=-4beta0^T D0^(-1)beta0<=0.              (5)

Using C0 instead of mu0 as the prefactor and rate gives the wrong sign
when beta0!=0. This comparison changes the rate as well as the prefactor.
At the fixed old rate 4C0, even (1) has defect +4(C0-mu0) at time zero.
The normalization is therefore not a proof that a faster fixed rate has
been restored; merely lowering a trial rate can also repair an initial
defect. Its substantive role is the explicit interpolation geometry,
common initialized value, and exact extension (2). No necessity or
global sufficiency is inferred from the initial calculation.

The first and second coefficients of the ENTIRE trained flow defect are
given in correction_matrix.md, equations (14)--(21), including the trained
responses of w,c,M, the input-sphere curvature and Gamma0's dependence
on all three inputs. The surviving second-order term involves the first
variation of E^T K n. It has not acquired a favorable sign merely through
(3); this is where the global proof remains incomplete.

There is useful global information in the new normalization. For any
fixed z with n.z!=0, Cauchy--Schwarz gives

    mu0 <= (z^T Gamma0 z)/(n.z)^2.                         (6)

As signed data approach (v,v,-v), choose z=(1,0,1). Its initialized feature
combination tends to zero, while n.z!=0, so mu0 tends to zero. This is the
contradictory original-input limit with labels (+,+,-). The old C0 need
not tend to zero there. Thus (3) captures an actual label-sensitive
geometric degeneracy missed by the mean norm. It still does not prove
that 4mu0 is a valid all-time rate. Equation (6) is an author-checked
corollary of the matrix definition and initialization continuity.

## 3. What is proved for the matrix potential throughout training

For every admitted symmetric rho seed, (1) inherits the exact all-time
symmetric inequality. If its unit-label fitted endpoint has K_*>0, then
there is an open neighborhood of freely perturbed sphere inputs on which

    Phi_mat'<=-lambda Phi_mat, L<=Phi_mat<=2 exp(-lambda t)

for every physical time. The potential is defined from time zero and has
no endpoint-dependent coefficients. The proof permits earlier tangent
rank-loss events. It uses a finite initial comparison and a trapped tail
near the regular fitted state, with the required matrix anticommutator
verified by its commutation at the symmetric center and continuity.

This theorem does NOT enlarge the previously proved set of regular
unit-label rho endpoints. In particular no new interval separated from
rho=1 has been certified. Formula (1) is more general and stays regular
at a possible singular endpoint, but this does not manufacture physical
damping there. This limitation is substantive, not a missing cosmetic
calculation.

## 4. A separate correction that cancels geometric flow defects

correction_normal_form.md constructs additional current-state terms on
K>0. Let j_i=grad f(v_i)/sqrt(3), let z be a formal error variable, and set

    p2(X,z)=z^T K^(-1)z,
    A_K p=2(Kz).grad_z p,
    Bp=-2 sum_i z_i D_{j_i}p, with z held fixed,
    p3=A_K^(-1)Bp2, p4=A_K^(-1)Bp3.                       (7)

These inverse operations are finite linear systems on cubic and quartic
polynomials, with 10 and 15 coefficients. They use present gradients and
their directional derivatives, not future integrals. The exact chain rule
along the actual flow is d p(X,xi)/dt=(B-A_K)p(X,xi). Hence

    d[p2+p3+p4](X,xi)/dt=-4L+(Bp4)(X,xi).                 (8)

The old cost p2 had a cubic moving-geometry defect. p3 cancels it; p4
cancels the resulting quartic defect. The remaining term is quintic in
the current error. This is an actual correction of a flow inequality,
not merely differentiation of the old potential.

For uniformly bounded coefficients and mu I<=K<=Lambda I, sufficiently
small current loss guarantees that

    Phi_corr=L+kappa[p2+p3+p4](X,xi)

dominates L and decays exponentially, with explicit thresholds and rate.
A current-state ball and the condition sqrt(L/mu)<its radius then prove
that the inequality holds forever and the full state fits. No future
metric premise is assumed. The complete derivation and local certificate
are in the report and its isolated review.

The coercive region already gives exponential LOSS decay without the
correction. Thus the new achievement is the explicit cancellation and
geometric organization, not a larger convergence basin. The construction
is an expansion in current residual. Near a regular fitted reference it
also controls arbitrary small input perturbations, but it is NOT an
all-path input expansion about a nonfitted seed. Its coefficients can
diverge as K becomes singular. Those limits must remain explicit.

## 5. Why the remaining obstacle needs reached-state information

The independent correction_flow.md and correction_design.md explore
corrections that remain regular at tangent rank loss. A Gram augmented
by derivatives of prediction gradients is indeed positive through every
symmetric rank-loss event; adding loss-gradient energy is also a valid
current-state expression. Neither supplies the missing physical damping.

There is now an explicit conditional obstruction at any symmetric fitting
state where all upper preactivations coincide and d_i=0. A bounded neutral
state path can have L of order tau^4 while ||grad L|| is of order tau^3.
Every smooth uniformly positive residual-quadratic potential on a full
neighborhood then has |Phi'|/Phi tending to zero along that path. A regular
matrix correction cannot therefore give a uniform positive exponential
inequality on that ENTIRE neighborhood. This is not an initialized-flow
counterexample and does not establish that such a seed is reached.

The two routes also independently prove a more favorable fact about actual
input responses, conditional on a singular symmetric seed existing: the
first two trained STATE responses are bounded and converge; the first
prediction response tends to zero, while the second tends to an explicit
centered quadratic vector. Its nonvanishing for actual canonical responses
is not established. The resulting possible loss first appears at fourth
order in the input perturbation. Consequently a second-order loss jet can
decay while still missing the decisive nonlinear source. Uniform control
of the actual perturbed trajectory does not follow from those response
limits.

The sharper remaining task is to exploit a property of the INITIALIZED
reached states that either excludes this simultaneous collapse or controls
the quadratic predictor source and its subsequent nonlinear motion.
The present work constructs real corrections and exact cancellation
mechanisms, but does not claim that this final dynamical estimate is solved.
