# Gaussian-tail-preserving initialization for the uncut operator references

Construction sidecar, 2026-09-06. CONDITIONAL on the precise premises
below. This proves a refined reference initialization and transfers only
the existing reference global-existence/action and canonical LOCAL
consistency conclusions. It proves neither canonical global existence
nor propagation of the new initial tail bounds to positive times.

## 0. Imported premises and the exact scope of this proof

Only the following two mathematical source files were read:

- SOFTPLUS_ENERGY_PRESERVING_OPERATOR_REFERENCES.md, SHA256
  464df3966e4d899f8615179968926edfe2b1e592fade50bbde08ba9fdcdd06f2.
- Its explicitly named interface SOFTPLUS_LOCAL_POPULATION_ASSEMBLY.md,
  SHA256
  398d12f41a60276cbee91323293c2f64b97055eac935f45ee31b8cac6946c97d.

Their unreviewed common-space, local, and reference-flow assertions are
conditional premises here. Their further dependencies are not read or
independently certified. Precisely, the premises used are the following.

**Common-space premise.** Fix rho in [-1,1), epsilon=1/10,
phi(x)=1+epsilon log(1+exp(x)), C=[[1,rho],[rho,1]], and labels
y=(1,sigma), sigma in {-1,1}. There are three probability spaces
(Omega_ell,mu_ell), with separable real Hilbert spaces
H_ell=L2(Omega_ell,mu_ell) admitting countable dense families of bounded
functions. There are prescribed bounded operators

    W0^2 : H_1 -> H_2,       W0^3 : H_2 -> H_3,
    ||W0^ell||op <= 10,

with their genuine Hilbert adjoints. On these SAME spaces write the
canonical initial fields as G^ell_a, ell=1,2,3 and a=1,2. They satisfy

    (G^1_1,G^1_2) is centered Gaussian with covariance C,
    h^ell_a = phi(G^ell_a),
    G^2_a = W0^2 h^1_a,       G^3_a = W0^3 h^2_a,
    Q_ell = ( <h^ell_a,h^ell_b> )_(a,b=1,2).

The pair G^2 has centered Gaussian law with covariance Q_1, and G^3
has centered Gaussian law with covariance Q_2. These are pair-marginal
statements on their respective populations, not assertions that fields
on different populations are independent or that all six fields have
a jointly Gaussian law. At rho=-1, G^1_2=-G^1_1 almost surely.

The sample-exchange symmetry is supplied on the common spaces as
measure-preserving involutions, with induced operators J_ell on H_ell.
Thus J_ell is a unitary involution, preserves bounded functions, and
acts by composition, so J_ell phi(u)=phi(J_ell u). Moreover,

    J_ell G^ell_a = G^ell_(3-a),
    J_ell W0^ell = W0^ell J_(ell-1),       ell=2,3.

These multiplicative/composition properties, not merely an abstract
unitary involution, are part of the imported symmetry premise.

**Reference-flow premise.** The bounded-kernel theorem in Sections 1
and 3 of the energy-preserving reference note applies to any bounded
initial first fields, bounded initial middle kernels, zero initial
readout, and the stated raw metric. It gives a unique global uncut
physical gradient flow. With sample-exchange symmetry, let

    f_a = <W4,H^3_a>,       g = (f_1+sigma f_2)/2,
    k = ||(H^3_1(0)+sigma H^3_2(0))/2||_2^2.

If k>0, the uncut feature-ascent path reaches g=1 at a finite feature
time s_fit<=1/k and has total raw action one. Its before-fit primal
bounds depend on initial first L2/operator norms and the feature-time
budget, not on the initial kernel supremum. Physical time satisfies
dt/ds=1/[4(1-g)] and diverges at s_fit. Its symmetry, energy, and actual
curvature-action conclusions apply. The initial operator bound 10 in
some displayed consequences is replaced by the actual uniform initial
bound; the bounded-kernel continuation proof itself allows arbitrary
finite initial bounds.

**Local-interface premise.** There is a canonical uncut feature path
theta on [0,S_*], with 0<S_*<=1/196, on the same spaces and initial
operators. The interface supplies canonical three-cut paths theta_R
on this interval, their uniform primal bounds, their state and velocity
convergence to theta and theta', and Gaussian L2 cut defects at most
A exp(-b R^2). Here R>=1 is an integer, and the cut outputs have
absolute value at most 2R.
The asymmetric state-velocity comparison of Section 4 of the reference
note is valid in any fixed bounded primal set: its coefficient is at
most A_box(1+R), and initial-operator perturbations enter through their
actions and adjoints on the old forward/backward inputs. The state
distance compares first fields, HS trained increments, and readout;
it never subtracts the two initial operators in HS norm. This is the
exact local comparison premise used in Section 8 below.

No other mathematical source or global canonical assertion is imported.
The rest of the initialization proof is given explicitly. Its mechanism
is to project the initial operators onto bounded finite-dimensional
spaces, then correct their action on the actual two initial features
to hit bounded truncations of the prescribed Gaussian targets exactly.

## 1. Positivity of the canonical and truncated feature Grams

The activation satisfies

    1 <= phi(x) <= 2+epsilon |x|,
    |phi(x)-phi(y)| <= epsilon |x-y|,
    phi(x)-phi(-x) = epsilon x.

It is strictly increasing. For a two-dimensional Gaussian pair with
positive definite covariance, the feature Gram is positive definite:
if c_1 phi(X_1)+c_2 phi(X_2)=0 almost surely, continuity and the strictly
positive Gaussian density imply that the identity holds at every point
of R^2. Varying x_1 with x_2 fixed gives c_1=0; positivity of phi then
gives c_2=0. Thus the squared L2 norm of every nonzero feature linear
combination is positive.

For -1<rho<1 this proves Q_1>0. At rho=-1, put G=G^1_1. The pair
(phi(G),phi(-G)) is exchangeable. The two eigenvalues of its Gram are

    lambda_+ = (1/2) E{[phi(G)+phi(-G)]^2} >= 2,
    lambda_- = (1/2) E{[phi(G)-phi(-G)]^2}
             = epsilon^2/2 > 0.

Hence Q_1>0 also at this endpoint. The imported Gaussian covariance
recursion now implies that G^2 has full support, so Q_2>0; then G^3
has full support, so Q_3>0. No inverse of C is used at rho=-1.

For each integer N>=1 choose the odd, bounded, 1-Lipschitz truncation

    tau_N(x) = max(-N,min(x,N)).

Only the initial fields use this map; all subsequent dynamics use the
uncut activation and gradients. Smoothness of initial random fields
as functions of their Gaussian coordinates is not a hypothesis of the
bounded-kernel theorem, so this hard truncation is sufficient.

Define the prescribed bounded targets and their actual features by

    z^ell_(N,a) = tau_N(G^ell_a),
    h^ell_(N,a) = phi(z^ell_(N,a)),             ell=1,2,3.

They obey |z^ell_(N,a)|<=min(|G^ell_a|,N),
1<=h^ell_(N,a)<=2+epsilon N, and

    z^ell_(N,a) -> G^ell_a in H_ell,
    h^ell_(N,a) -> h^ell_a in H_ell.                  (1)

The first convergence is dominated convergence, since the truncation
error is bounded by |G^ell_a|; the second uses the Lipschitz bound for
phi. Define

    B_(ell,N) = ( <h^ell_(N,a),h^ell_(N,b)> )_(a,b=1,2).

Every entry converges to its Q_ell entry: subtract the products and
apply Cauchy--Schwarz using (1) and the uniform L2 feature bounds.
Therefore

    B_(ell,N) -> Q_ell,       Q_ell>0.                 (2)

In fact every B_(ell,N) is already positive definite. For a full-support
Gaussian pair, a vanishing feature combination would, on the open
square (-N,N)^2, be the same combination of phi(x_1),phi(x_2);
the preceding varying-coordinate argument applies. For the antiparallel
first pair, oddness gives z^1_(N,2)=-z^1_(N,1), and its Gram eigenvalues
are

    lambda_+(B_(1,N)) >= 2,
    lambda_-(B_(1,N)) = (epsilon^2/2) E tau_N(G)^2 > 0.

Consequently the feature Grams to be inverted below are nonsingular
for all N, including rho=-1. In particular, for each fixed rho and ell,
there is a positive lower bound on lambda_min(B_(ell,N)) for all N:
use convergence to Q_ell for the tail of the sequence and the minimum
of the finitely many remaining positive eigenvalues. No lower bound
uniform as rho approaches 1 is asserted.

## 2. Bounded, symmetry-preserving finite-dimensional projections

In each H_ell choose a countable family (b_(ell,j)) of bounded functions
whose real linear span is dense. Let E_(ell,N) be the real span of

    1;  b_(ell,j), J_ell b_(ell,j) for 1<=j<=N;
    z^ell_(m,a), h^ell_(m,a) for 1<=m<=N and a=1,2.

These are finite-dimensional spaces consisting of bounded functions.
They are increasing, have dense union, and are invariant under J_ell:
J exchanges each target/feature pair because tau_N is the same scalar
map on both samples and J acts by composition. Let P_(ell,N) denote
the orthogonal projection onto E_(ell,N). Then

    ||P_(ell,N)||op <= 1,
    P_(ell,N) -> I strongly,
    P_(ell,N) J_ell = J_ell P_(ell,N).                (3)

For strong convergence, approximate any fixed L2 vector by a member
of the dense union and use the minimizing property of orthogonal
projection. Commutation holds since the unitary involution preserves
both E_(ell,N) and its orthogonal complement. In addition,

    P_(ell,N) z^ell_(N,a) = z^ell_(N,a),
    P_(ell,N) h^ell_(N,a) = h^ell_(N,a).              (4)

Choose an orthonormal basis in each E_(ell,N). Each basis vector is
bounded, being a finite linear combination of the bounded generators.
Define the projected base operators, for ell=2,3, by

    A_(ell,N) = P_(ell,N) W0^ell P_(ell-1,N).

They have operator norm at most 10. In bounded orthonormal bases
(e_i) of E_(ell,N) and (f_j) of E_(ell-1,N), their kernels are

    a_(ell,N)(x,u)
       = sum_(i,j) <e_i,W0^ell f_j> e_i(x) f_j(u).    (5)

Thus they are finite rank with bounded kernels at every fixed N.
For any fixed v in H_(ell-1),

    ||A_(ell,N)v-W0^ell v||_2
      <= 10 ||P_(ell-1,N)v-v||_2
         + ||(P_(ell,N)-I)W0^ell v||_2 -> 0.

Their adjoints have the reversed projection formula. The identical
estimate with (W0^ell)^* proves strong convergence of the adjoints.
Also A_(ell,N) intertwines J_(ell-1) and J_ell by (3) and the imported
intertwining identity for W0^ell.

## 3. Exact two-feature corrections

Fix ell=2 or 3. All maps in this section are defined using the fields
already prescribed in Section 1, so there is no circular initialization.
Set

    U_(ell,N) : R^2 -> H_(ell-1),
    U_(ell,N)c = sum_a c_a h^(ell-1)_(N,a),
    V_(ell,N) : R^2 -> H_ell,
    V_(ell,N)c = sum_a c_a z^ell_(N,a),
    D_(ell,N) = V_(ell,N)-A_(ell,N)U_(ell,N).

The input Gram is

    U_(ell,N)^* U_(ell,N) = B_(ell-1,N)>0.

Here U^*v is the column vector of the two inner products with the
actual input features. Define the correction and the final initial
operator by

    T_(ell,N) = D_(ell,N) B_(ell-1,N)^(-1) U_(ell,N)^*,
    W0,N^ell = A_(ell,N)+T_(ell,N).                  (6)

Multiplication on the right by U_(ell,N) gives

    T_(ell,N) U_(ell,N) = D_(ell,N),
    W0,N^ell h^(ell-1)_(N,a) = z^ell_(N,a), a=1,2.  (7)

This is an exact identity in H_ell, not an asymptotic moment match.

Write d_a=z^ell_(N,a)-A_(ell,N)h^(ell-1)_(N,a) for the columns of D.
They are bounded: the first term is bounded, and the second belongs
to the finite-dimensional space of bounded functions E_(ell,N).
The correction has kernel

    t_(ell,N)(x,u)
      = sum_(a,b=1,2) d_a(x) [B_(ell-1,N)^(-1)]_(a,b)
                                      h^(ell-1)_(N,b)(u). (8)

Each factor is bounded at fixed N, and all four scalar coefficients
are finite. Hence (8) is a bounded finite-rank kernel. Its rank is at
most two. Both d_a and the input features belong to their respective
projection spaces, so actually

    W0,N^ell = P_(ell,N) W0,N^ell P_(ell-1,N).

In particular the total rank is at most dim E_(ell,N), and the full
initial kernel is the bounded sum of (5) and (8). Its genuine adjoint
is the integral operator with the transposed kernel. No bound uniform
in N on kernel supremum, kernel HS norm, or L2-to-L-infinity norm is
needed or asserted.

To estimate the correction, (4) gives the especially useful identity

    d_a = P_(ell,N)[z^ell_(N,a)-W0^ell h^(ell-1)_(N,a)].

Using the exact canonical relation G^ell_a=W0^ell h^(ell-1)_a,

    ||d_a||_2
      <= ||z^ell_(N,a)-G^ell_a||_2
         + 10 epsilon ||z^(ell-1)_(N,a)-G^(ell-1)_a||_2
      -> 0.                                         (9)

Thus no convergence uniform over arbitrary moving L2 inputs is being
assumed; (9) handles these specific moving inputs directly. Let
lambda_N=lambda_min(B_(ell-1,N)). Since

    (B^(-1)U^*)(B^(-1)U^*)^* = B^(-1),

the norm of B^(-1)U^* is lambda_N^(-1/2). Also
||D||op <= (sum_a ||d_a||_2^2)^(1/2). Consequently

    ||T_(ell,N)||op
       <= (sum_a ||d_a||_2^2)^(1/2) / sqrt(lambda_N)
       -> 0.                                        (10)

All Gram inverses exist, and the positive limiting Gram controls their
conditioning for large N. Formula (10), not a bound on the initial
kernel supremum, is what controls the operator perturbation.

## 4. Exact equivariance, uniform bounds, and both strong limits

Let S=[[0,1],[1,0]] be the swap on R^2. Suppressing ell,N, the pair
symmetries and the equivariance of A imply

    J_in U = U S,       J_out V = V S,
    J_out D = D S,      U^* J_in = S U^*.

Unitarity of J_in gives S B S=B for B=U^*U; hence B^(-1) commutes
with S. Substituting into (6),

    J_out T = D S B^(-1) U^*
            = D B^(-1) S U^* = T J_in.

Thus the correction itself is equivariant and

    J_ell W0,N^ell = W0,N^ell J_(ell-1), ell=2,3.     (11)

There is no averaging error in (7). This equivariant Gram formula
establishes symmetry without a separate post-correction symmetrization.

By (10),

    ||W0,N^ell||op <= 10+||T_(ell,N)||op = 10+o(1).   (12)

Every term is finite and the correction norms tend to zero; therefore
both initial operator sequences are uniformly bounded over all N.
For all sufficiently large N both norms are at most 11. When numerical
uniform bounds are used below, discard finitely many initial indices
and retain this tail, relabeling it if desired. Nothing asserts the
literal bound 10 for the corrected operators.

For every fixed v in H_(ell-1) and w in H_ell, (3), (5), and (10) give

    W0,N^ell v -> W0^ell v in H_ell,
    (W0,N^ell)^* w -> (W0^ell)^* w in H_(ell-1).       (13)

Indeed the base operators and their adjoints converge strongly, while
T_(ell,N) and its adjoint converge to zero in operator norm. These are
strong limits for BOTH orientations. They are not operator-norm or HS
convergence statements for W0,N^ell-W0^ell. Only the finite-rank
correction T_(ell,N), not the projected base minus W0^ell, was proved
small in operator norm.

## 5. Initial realizability and exact full forward evaluation

Initialize the first fields by Z^1_(N,a)(0)=z^1_(N,a), the middle
operators by W0,N^2,W0,N^3, and the readout by W4_N(0)=0. All initial
trained increments relative to W0,N^ell are zero.

For -1<rho<1 every first-field pair is realizable on the two-input
span. More explicitly, if e_1,e_2 are the unit input vectors with
Gram C, the vector sum_a [C^(-1)z^1_N]_a e_a has inner products z^1_N
with the two inputs and squared norm (z^1_N)^T C^(-1)z^1_N. Since C
is fixed and invertible, (1) implies convergence in the first raw norm

    ||z^1_N-G^1||first^2
      = E[(z^1_N-G^1)^T C^(-1)(z^1_N-G^1)] -> 0.

Also ||z^1_N||first^2 <= 2||C^(-1)||op, so these norms are uniformly
bounded for fixed rho. At rho=-1, oddness gives the realizable pair
(tau_N(G),-tau_N(G)); the first raw norm is ||tau_N(G)||_2<=1 and
convergence is scalar L2 convergence. In every case each first marginal
has L2 norm at most one, and the first fields are bounded at fixed N.
For any admissible first-field increment v, its representing input
vector has inner products v_a with unit vectors e_a, so
||v_a||_2<=||v||first by Cauchy--Schwarz. At rho=-1 this is equality
in the scalar representation. This marginal control is used in the
local-interval estimate below.

Evaluating the actual network from these parameters gives, successively,

    H^1_(N,a)(0) = phi(z^1_(N,a)) = h^1_(N,a),
    Z^2_(N,a)(0) = W0,N^2 H^1_(N,a)(0) = z^2_(N,a),
    H^2_(N,a)(0) = phi(z^2_(N,a)) = h^2_(N,a),
    Z^3_(N,a)(0) = W0,N^3 H^2_(N,a)(0) = z^3_(N,a),
    H^3_(N,a)(0) = phi(z^3_(N,a)) = h^3_(N,a).       (14)

The two middle equalities are exactly (7). Thus all six prescribed
hidden targets are the actual initial preactivations. In particular,
the W3 correction uses phi(z^2_N), the actual W2 output after activation,
not a surrogate feature pair. At time zero the readout, predictions,
all backward delta fields, and both reverse queries are zero; residuals
are -y and g_N(0)=0. These are the full forward/backward initial
identities. On each population one can choose versions realizing them
simultaneously almost surely for all N and both samples, since only
countably many L2 identities are involved.

## 6. Uniform Gaussian exponential-square envelopes for all six fields

Let v_(ell,a)=E|G^ell_a|^2. The Gaussian covariance recursion and the
growth bound on phi give bounds independent of rho and a:

    sqrt(v_(1,a)) = 1,
    sqrt(v_(2,a)) = ||phi(G^1_a)||_2 <= 2+epsilon = 2.1,
    sqrt(v_(3,a)) = ||phi(G^2_a)||_2 <= 2+0.1(2.1) = 2.21.

Thus every variance is at most 2.21^2=4.8841<5. A centered scalar
Gaussian X of variance v has, for 2 eta v<1,

    E exp(eta X^2) = (1-2 eta v)^(-1/2).

This follows by combining exp(eta x^2) with its Gaussian density and
integrating the resulting Gaussian; for v=0 the expectation is one.
Take eta=1/20. Then all six canonical fields obey

    E_ell exp(eta |G^ell_a|^2) <= sqrt(2).

By (14) and pointwise truncation domination, the stronger common-space
envelope bound holds:

    E_ell exp( (1/20) sup_(N>=1)|Z^ell_(N,a)(0)|^2 )
       <= E_ell exp( (1/20)|G^ell_a|^2 ) <= sqrt(2),
                                      ell=1,2,3; a=1,2. (15)

Hence the six requested exponential-square moments are uniform in N;
the displayed constants are also independent of rho. This conclusion
concerns the actual recomputed preactivations by exact identity (14).
Boundedness of an operator on L2 alone would not imply (15).

For clarity about separate populations, (15) is six marginal-envelope
statements. If a simultaneous scalar envelope is desired, place the
three populations on their product space, or on any coupling with the
same marginals. Holder's inequality with six exponents equal to six
gives

    E exp( (1/120) sum_(ell=1)^3 sum_(a=1)^2
                         sup_N |Z^ell_(N,a)(0)|^2 ) <= sqrt(2). (16)

No Gaussian joint law or independence assertion is used in this step.
The coupling serves only to express the envelopes together; the
operators still act between the original separate L2 spaces.

Although phi has an unbounded positive tail, its selected inputs at
each fixed N are bounded, as required in (8). Uniform feature L2 bounds
and even exponential-square envelopes also follow from

    |h^ell_(N,a)|^2 <= 8+2 epsilon^2 |G^ell_a|^2.

For example any fixed beta>0 with 2 beta epsilon^2<=1/20 gives
E exp(beta sup_N |h^ell_(N,a)|^2)<=exp(8 beta)sqrt(2).
No part of the kernel proof treats phi itself as a globally bounded
function.

## 7. Applicability of the existing uncut reference theorem and action bounds

Here are the equations and metric to which the imported theorem is
applied, to fix its meaning for the refined references. At every time,

    H^ell_a=phi(Z^ell_a), Z^2_a=W^2 H^1_a, Z^3_a=W^3 H^2_a,
    delta^3_a=W4 phi'(Z^3_a), q^2_a=(W^3)^*delta^3_a,
    delta^2_a=phi'(Z^2_a)q^2_a, q^1_a=(W^2)^*delta^2_a,
    delta^1_a=phi'(Z^1_a)q^1_a.

The uncut physical equations are

    dot Z^1_b = -2 sum_a C_ba r_a delta^1_a,
    dot W^ell = -2 sum_a r_a delta^ell_a tensor H^(ell-1)_a,
                                                         ell=2,3,
    dot W4 = -2 sum_a r_a H^3_a,
    f_a=<W4,H^3_a>,       r_a=f_a-y_a.

Here (u tensor v)w=u<v,w>. Feature ascent replaces -2r_a by y_a/2.
The raw norm squares are the first-field metric specified in Section 5,
the two HS increment norms, and the L2 readout norm, added together.

Sections 3 and 5 give bounded initial kernels and bounded first fields,
including realizability at rho=-1, with zero readout. Section 4 gives
the required symmetry and uniform initial operator bounds. Thus the
conditional bounded-kernel theorem constructs, for each N, a global
uncut physical reference and its before-fit feature path. The
parameters obey symmetry under

    Z^1_a -> J_1 Z^1_(3-a),
    W^ell -> J_ell W^ell J_(ell-1),
    W4 -> sigma J_3 W4.

The initial state is fixed by this transformation. The reference
uniqueness and symmetry premise yields f_(N,a)=y_a g_N and equal
sample feature second moments at all constructed times.

The initial top speed is computed from the ACTUAL fields in (14):

    k_N = (1/4) y^T B_(3,N)y -> k_0=(1/4)y^T Q_3 y>0. (17)

It is positive for every N by Section 1. Discarding finitely many
additional indices if needed gives simultaneously

    ||W0,N^ell||op<=11,       k_N>=k_0/2,
    s_N<=S_max:=2/k_0.

The imported theorem therefore gives the same full reference action
conclusions, with the corrected operator constant:

    g_N'=||theta_N'||raw^2,
    integral_0^s_N ||theta_N'(s)||raw^2 ds=1,
    ||theta_N(s)-theta_N(0)||raw <= sqrt(s g_N(s))
                                      <=sqrt(S_max),
    ||W^ell_N(s)||op <= M:=11+sqrt(S_max).            (18)

The norm in the displacement formula uses the HS change from W0,N^ell,
not an HS difference from W0^ell. The first/readout L2 and all
forward/backward L2 bounds are uniform over the retained references
on their entire before-fit feature intervals. Physical time covers
[0,infinity). In physical time, L_N=sum_a r_(N,a)^2 starts at 2 and
obeys dot L_N=-||dot theta_N||raw^2 and displacement at most sqrt(2t).

For completeness, the exact opposite-label action estimates being
retained from the reference theorem can be stated as follows. Put
U^ell=(H^ell_1+H^ell_2)/2, V^ell=(H^ell_1-H^ell_2)/2,
kappa_ell=||V^ell||_2^2, and use +/- for half-sums/differences of other
sample fields. For sigma=-1, the theorem gives, on each reference,

    integral_0^s_N [||delta^2_-||_2^2+||delta^3_-||_2^2
          +kappa_1||delta^2_+||_2^2+kappa_2||delta^3_+||_2^2] ds <= 1.

Define q^3_a=W4 and M^ell_a=phi''(Z^ell_a)q^ell_a for ell=2,3.
With the same M from (18), the retained curvature bounds are

    integral_0^s_N ||M^2_-||_2^2 ds <= 2(1+epsilon^2 M^2),
    integral_0^s_N kappa_2||M^2_+||_2^2 ds <= 4 epsilon^2 M^2,
    integral_0^s_N [||M^3_-||_2^2+kappa_2||M^3_+||_2^2] ds <= 1.

These are applications to the refined bounded references of the
existing action theorem, with its hypotheses now checked. They are
not new bounds on canonical global paths or on arbitrary products
of curvature fields with correlated sensitivities.

## 8. Local consistency on the existing canonical interval

First check a numerical detail that cannot be hidden in the change
from the original operator bound 10 to the corrected bound 11. All
sufficiently large N feature paths reach the full interval [0,S_*]
before fitting. On an existing before-fit portion with s<=S_*<=1/196,
the reference action inequality gives displacement at most sqrt(s)
<=1/14<0.1. Since each first marginal initially has L2 norm at most
one, this implies

    max_a ||Z^1_(N,a)(s)||_2 < 1.1,
    ||W^2_N(s)||op, ||W^3_N(s)||op < 11.1,
    max_a ||H^1_(N,a)(s)||_2 <= 2.11,
    max_a ||H^2_(N,a)(s)||_2 <= 4.3421,
    max_a ||H^3_(N,a)(s)||_2 <= 6.819731 < 7.

The readout equation then gives ||W4_N(s)||_2<=7s, so
|g_N(s)|<=49s<=1/4. If s_N<=S_*, continuity at the constructed fit
time would imply 1=g_N(s_N)<=1/4, a contradiction. Hence s_N>S_*
and the refined paths share the canonical interval with a uniform
primal bound. This avoids silently reusing a box whose initial
operator hypothesis was exactly 10.

Write

    W^ell_N(s)=W0,N^ell+K^ell_N(s),
    W^ell_R(s)=W0^ell+K^ell_R(s),

where theta_R is the old canonical cut path from the local-interface
premise. Define d(theta_N,theta_R) as the sum of the first-field
distance, the two HS distances between K_N and K_R, and the readout
L2 distance. Initially this is

    a_N=||z^1_N-G^1||first -> 0.

At a fixed R the four old input pairs
H^1_R, H^2_R, delta^2_R, delta^3_R are continuous L2 curves on
[0,S_*]. Their images are compact. Uniform boundedness and the two
strong convergences (13) imply

    e_(N,R) := max_a sup_(s<=S_*) [
      ||(W0,N^2-W0^2)H^1_(R,a)(s)||_2
      +||(W0,N^3-W0^3)H^2_(R,a)(s)||_2
      +||((W0,N^2)^*-(W0^2)^*)delta^2_(R,a)(s)||_2
      +||((W0,N^3)^*-(W0^3)^*)delta^3_(R,a)(s)||_2 ] -> 0. (19)

To justify the compact-input assertion, for a compact set choose a
finite delta-net, use strong convergence at its finitely many points,
and bound the error between an input and its net point by the uniform
operator bound times delta. Let N tend to infinity and then delta to
zero. This argument does not apply to arbitrary bounded sets in L2.

For example the exact forward split is

    W^2_N H^1_N-W^2_R H^1_R
      = W^2_N(H^1_N-H^1_R)
        +(K^2_N-K^2_R)H^1_R+(W0,N^2-W0^2)H^1_R.

The adjoint split is the same expression in the reverse direction
with the old delta input. In the following comparison, let c_R denote
the canonical interface's smooth cap, whose output ceiling is 2R;
it is distinct from the hard INITIAL truncation tau_N in Section 1.
At each backward multiplication, use the old-cut identity

    phi'(z_N)v_N-phi'(z_R)c_R(v_R)
      = phi'(z_N)[v_N-v_R]
        +phi'(z_N)[v_R-c_R(v_R)]
        +c_R(v_R)[phi'(z_N)-phi'(z_R)].

The first multiplier is bounded by epsilon and the last old input by
2R. Forward differences contain no such cut factor. Applying these
splits from the top layer down, bounded trained operator norms and
bounded field L2 norms give the imported comparison with a coefficient
linear in R. In this notation it reads

    ||theta_N'(s)-theta_R'(s)||state
      <= C(1+R)[d(theta_N(s),theta_R(s))+e_(N,R)]
                       + C exp(-b R^2),              (20)

where C,b>0 are independent of N and R on the common primal box.
The derivative norm compares first/readout derivatives and HS
increment derivatives. No new reference tail estimate is used in
(20); all cut defects are those of the old canonical cut path.

Integration and the scalar Gronwall inequality give

    sup_(s<=S_*) d(theta_N(s),theta_R(s))
      <= exp(C(1+R)S_*)
          [a_N+C(1+R)S_* e_(N,R)+C S_* exp(-b R^2)].

First let N tend to infinity with R fixed, using (19), and then let
R tend to infinity. Since -b R^2+C(1+R)S_* tends to minus infinity
and theta_R converges to the canonical theta, this proves

    sup_(s<=S_*) d(theta_N(s),theta(s)) -> 0.          (21)

The same order of limits in (20), together with the interface's
velocity convergence, gives uniform local velocity convergence.
The displayed forward/backward splits also give local L2 convergence
of all actual fields. Thus the refinement preserves the existing
canonical local consistency statement for states, velocities, and
fields, with the initial operators compared strongly in both
orientations and only their trained increments compared in HS norm.

## 9. Scope and gap checks specific to this refinement

- The first preactivation covariance at rho=-1 is singular. It is
  never inverted: realizability uses the scalar raw first metric,
  whereas the correction inverts the positive definite FEATURE Gram.
- The inputs in (6) are the actual phi(z^1_N),phi(z^2_N). Exact
  matching at W2 precedes evaluation at W3, so all six initial fields,
  not merely their moments, satisfy the required forward equations.
- Gaussian pair laws and covariance recursion are explicit imported
  premises about the prescribed initialization. They do not follow
  from an arbitrary bounded operator, and no replacement independent
  Gaussian coordinates were introduced.
- The projection bases, input features, and residual output columns
  are bounded at fixed N. This proves bounded kernels even though phi
  has an unbounded positive tail on R. Uniform kernel supremum bounds
  and uniform smoothing constants are not a consequence.
- Gram conditioning and the large-N threshold may depend on rho.
  The six Gaussian-envelope constants in (15) do not. No assertion
  uniform at the excluded coincident-input endpoint rho=1 is needed.
- Equivariance uses a measure-preserving composition symmetry J,
  and is proved for the correction itself. An arbitrary unitary J
  would not by itself commute with the nonlinear activation.
- The initial operator norms are 10+o(1), with a uniform bound 11
  on a retained tail. The local-interval check explicitly allows 11.
  Norm convergence of the full operators and HS convergence to the
  canonical initial operators remain unclaimed.
- The new exponential-square bounds concern INITIAL fields only.
  The existing global bounded-reference theorem supplies finite-N
  continuation, and its energy supplies uniform L2/action estimates;
  neither implies uniform Gaussian envelopes for their future fields.
- Strong initial-operator convergence is used locally only on compact
  families of old canonical inputs. Energy bounds do not establish
  compactness of all later reference inputs. Passing these global
  reference paths to a global canonical path remains an open step
  outside this construction.

Conditional on Section 0, the refined references therefore have exact
Gaussian-truncated initial forward fields, uniform exponential-square
envelopes for all six preactivations, bounded first fields and finite-
rank bounded initial kernels, exact sample symmetry, uniformly bounded
initial operators with strong convergence of both operators and their
adjoints, and the already established reference existence/action and
canonical local consistency properties. Nothing here supplies actual
lower forcing or proves the full canonical theorem.
