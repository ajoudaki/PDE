# Second-order geometry at a collapsed fitting state

2026-09-16. Root analytical candidate; no experiment or promotion. Inputs:
the exact canonical equations and initialization in docs/observable_p1.md,
docs/global_nonlinear.md C.4.7.9 and C.4.7.10, and this study's complete
three_coordinate_candidate.md, perturbation_modes.md,
perturbation_metric_template.md and resolution_endpoint.md. This is a
current-state geometric theorem, not a proof that the state below is reached
from initialization, nor a global decay theorem for its perturbations.

## 1. Setting and why the second order matters

Absorb the fixed labels into v_i=y_i u_i, so all three targets are one.
Use the exact p=1 fields

    a_i=E1[b1 tanh(w.v_i)], z_i=b2^T M a_i, H_i=tanh z_i,
    d_i=E2[b2 c tanh'(z_i)], Q_i=b1^T M^T d_i,
    f_i=E2[c H_i].

Here tanh' means sech^2; derivative superscripts below are ordinary
derivatives of tanh. All gradient norms use the fixed physical metric.
Consider a current state with bounded w-g and c, finite M, and

    z_i=z,  d_i=0,  f_i=1  for all i.                         (1)

These are exactly the upper-collapse/zero-reverse conditions at a possible
singular fitting endpoint of the symmetric family. The theorem is stated
conditionally on the current state (1); its reachability remains separate.
Then every prediction gradient is the same nonzero physical vector

    g_*=grad f_i=(0,H,0),  H=tanh z,  ||g_*||^2=E2 H^2>0.        (2)

The order of the blocks is (w,c,M). Nonzero H follows from E2[cH]=1.
Thus the normalized tangent Gram has rank one, and its null space is the
two-dimensional space of zero-sum output coefficients.

For each input choose arbitrary eta_i perpendicular to v_i and perturb on
the sphere by

    v_i(tau)=(v_i+tau eta_i)/sqrt(1+tau^2 |eta_i|^2).

Consequently v_i'(0)=eta_i and v_i''(0)=-|eta_i|^2 v_i. The three eta_i
are independent; no common scalar angular change is imposed.

## 2. Full state/input quadratic response

First take a linear state path X(tau)=X+tau h with h=(h_w,h_c,h_M), where
h_w and h_c are bounded. Polynomial Gaussian envelopes for these directions
are equally admissible provided all displayed products have finite moments.
The bounded case suffices for every assertion here and avoids any claim of
a C2 Nemytskii map on unrestricted L2. For each i define the first lower
and upper preactivation variations

    l_i=h_w.v_i+w.eta_i,
    A_i=E1[b1 tanh'(w.v_i) l_i],
    Z_i=b2^T(h_M a_i+M A_i).                                (3)

The first predictor derivative is

    f_i'(0)=E2[h_c H]+d_i^T(h_M a_i+M A_i)=<g_*,h>.           (4)

In particular every fixed-state input derivative vanishes at (1).
Choose h in the neutral space <g_*,h>=0. Directly differentiating twice gives

    f_i''(0)=B_i(h,eta),
    B_i(h,eta)=2 E2[h_c tanh'(z) Z_i]
                     +E2[c tanh''(z) Z_i^2].               (5)

Here is the full calculation showing which terms vanish and why. The second
lower preactivation variation is

    l_i^{[2]}=2h_w.eta_i-|eta_i|^2(w.v_i),
    a_i^{[2]}=E1[b1{tanh''(w.v_i)l_i^2
                               +tanh'(w.v_i)l_i^{[2]}}],
    z_i^{[2]}=b2^T(2h_M A_i+M a_i^{[2]}).

The second predictor derivative before simplification is

    2E2[h_c tanh'(z)Z_i]
      +E2[c tanh''(z)Z_i^2]+E2[c tanh'(z)z_i^{[2]}].

Its last term equals d_i^T(2h_M A_i+M a_i^{[2]}) and vanishes by (1).
Thus the sphere-curvature and lower second-derivative terms have been
included; their coefficients vanish at this particular singular state.
They must be retained away from it. Formula (5) still includes both hidden
layers through the actual M and the first-layer moment A_i.

All differentiations and second-order remainders follow from bounded tanh
derivatives, bounded dictionary columns, bounded c and h_c, and Gaussian
moments for w=g+(bounded). The lower Taylor remainder is bounded after
integration by a constant times |tau|^3 E1(1+|g|)^3 on bounded direction
sets. Upper preactivation variations are finite coefficient vectors, so
the upper remainders have the same order. This proves the expansions in
ordinary population L2 and for their scalar expectations.

More generally use X(tau)=X+tau h+(tau^2/2)k, with bounded directions k.
The extra contribution to f_i''(0) is <g_*,k>, common to all three inputs:

    f_i(tau)-1=(tau^2/2)[B_i(h,eta)+<g_*,k>]+O(tau^3).        (6)

## 3. Quartic residual energy and its transverse part

From the unhalved mean loss, (6) gives the exact leading term

    L(X(tau);v(tau))
      =(tau^4/12) sum_i [B_i(h,eta)+<g_*,k>]^2+O(tau^5).      (7)

Since H is bounded and nonzero, a bounded readout component of k can realize
any prescribed scalar <g_*,k>. Minimizing only over that second-order common
correction therefore gives the coefficient

    (1/12) sum_i (B_i-bar B)^2,  bar B=(B_1+B_2+B_3)/3.     (8)

This minimization is a local geometric calculation, not an assertion that
gradient flow chooses this correction or reaches the state (1). The true
uncontrolled quadratic residual is the disagreement between the three B_i.
The ordinary data Hessian of loss is zero in these neutral directions,
despite a possibly nonzero quartic loss term. A second-order predictor
calculation, rather than a second-order loss calculation alone, is needed
to see that effect.

The original mixed potential Phi=L W has the same leading form multiplied
by its finite positive current value W. The initialization constant C0 is
positive at any nondegenerate symmetric seed and stays positive in a small
input neighborhood. Hence W(X(tau),v(tau))=W(X,v)+O(tau), even when its
actual data dependence is retained. In particular,

    Phi(X(tau);v(tau))
      =(W(X,v) tau^4/12) sum_i [B_i+<g_*,k>]^2+O(tau^5).     (9)

There is no claim that the quartic coefficient is globally convex or has a
uniform gradient inequality. Formula (9) does not turn a vanishing Hessian
into absence of an error.

## 4. The tangent metric opens at second order

Let Gamma_i denote the first variation of the full physical prediction
gradient along the same state/input path, evaluated at tau=0. Its blocks
are explicitly

    D_i=E2[b2{h_c tanh'(z)+c tanh''(z)Z_i}],
    Gamma_i^c=tanh'(z)Z_i,
    Gamma_i^M=D_i a_i^T,
    Gamma_i^w=tanh'(w.v_i)(b1^T M^T D_i)v_i.                (10)

Terms containing d_i or Q_i vanish by (1); all other first derivatives of
the full gradient are present. In particular the last line retains the
actual backward query and is not a readout-only metric.

Let K_ij(tau)=<grad f_i(tau),grad f_j(tau)>/3. For every real zeta with
sum_i zeta_i=0, the sum of its zeroth-order gradients vanishes. Thus

    zeta^T K(tau) zeta
       =(tau^2/3)||sum_i zeta_i Gamma_i||^2+o(tau^2),
    (zeta^T K zeta)'(0)=0,
    (zeta^T K zeta)''(0)
       =(2/3)||sum_i zeta_i Gamma_i||^2.                   (11)

The raw null-space Hessian in (11) is nonnegative. This does not suffice
for positive definiteness of the whole perturbed K: the output directions
may acquire a first-order component along the old common direction.
The exact Schur complement removes that component as follows.

Let n=(1,1,1)/sqrt(3), and choose a 3-by-2 matrix E with orthonormal columns
in n-perp. Define a physical-space linear map A:R2->H by

    A zeta=(1/sqrt(3)) sum_i (E zeta)_i Gamma_i.

Writing K in the basis (n,E), its parallel entry, off-diagonal block and
transverse block obey

    k(tau)=||g_*||^2+O(tau),
    b(tau)=tau A^*g_*+o(tau),
    H_perp(tau)=tau^2 A^*A+o(tau^2).

Consequently its Schur complement is

    H_perp-b b^T/k
      =tau^2 A^*(I-P_{g_*})A+o(tau^2),
    P_{g_*} h=g_* <g_*,h>/||g_*||^2.                                (12)

Formula (12) is the relevant second-order test: both weak prediction
directions open quadratically precisely when A^*(I-P_{g_*})A is positive
definite. If it is singular, higher orders may still open them; no
impossibility conclusion follows. If it is positive definite, continuity
and the Schur formula give a positive full Gram for every sufficiently
small nonzero tau, with its two small eigenvalues of order tau^2.

This calculation explains why checking an input Hessian or a hidden Gram
alone can miss the issue. The correction uses derivative differences
between inputs, projects away the already learned common prediction, and
includes lower, middle and readout contributions. Its coefficients are
computable from the current state, chosen tangent directions and h.

## 5. Precise use and limit of the result

At the possible singular endpoint, the first-order fixed-state input response
vanishes. The quadratic predictor response and quadratic Schur coefficient
describe the next possible orders of residual production and metric opening;
either coefficient may vanish for a chosen direction. Their comparison is
therefore a natural next nonlinear problem. A generic Taylor expansion with
a nonzero first-order residual would give the wrong scale here.

Equations (5),(8),(12) supply explicit coefficients for that problem. To
deduce fitting of the actual perturbed initialized trajectory still requires
a stability or capture inequality relating the resulting quadratic residual
to the available quadratic sensitivity, and control of its subsequent
evolution. A local positive Schur coefficient by itself is not that inequality.
No unknown endpoint, response history, or free correction variable is added
to the original potential or the autonomous closure. The variations h,k
are proof variables for the local geometry, not extra state coordinates.
