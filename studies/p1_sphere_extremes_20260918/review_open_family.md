# Independent review of the unconditional open-family theorem

**Verdict: PASS for the theorem as stated in `protected_family.md`.** The
proof supplies the initialization, finite-clock endpoint, endpoint rank,
finite entrance, and trapping premises needed for its conclusion. I found
no mathematical gap requiring a conditional downgrade. This verdict concerns
the exact population-expectation, fixed-order closure and its stated local
family; it is not a promotion decision or a network-identification result.

Review date: 2026-09-18. No experiment, numerical diagnostic, quadrature
value, author history, other study, or other review was used. The complete
two frozen arguments and `docs/observable_p1.md` were read, together with the
assigned canonical state/equations/existence material in
`docs/global_nonlinear.md` C.4.7.9.3--4 and C.4.7.10.D.3. The rigorous
mathematics skill and the conjecture skill's adversarial audit guidance were
applied.

Reviewed file hashes:

- `protected_family.md`:
  `a7fb86719adaf96c3f3fc60a8e5f02618c4eb60aa32461cd7b1df77cd417178d`.
- `initialization_positivity.md`:
  `a785048dfbf22f3940941dbb92f985729cc393977b882eb5153ddf54dc39367b`.
- `docs/observable_p1.md`:
  `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba`.

## 1. Canonical object, initialization, and nonzero diagonal coefficient

The coefficient formulas in both frozen arguments agree with the permitted
exact p=1 source, including the reused-action response `alpha h`, the
Cholesky subtraction, the term `tau gamma` in the second band of D, and
the positive ridge `eta=1/4096`. Removing the inactive constant coordinates
is justified by the canonical mark-negation invariant class. It does not
restrict the remaining full 3-by-6 matrix evolution.

The positivity certificate is valid. In its notation, set
`R=k-(beta/nu)h`. Independence and Gaussian integration by parts give
`E[ZR]=sqrt(tau) gamma`, and therefore

\[
 s-\beta^2/\nu=E R^2\ge\tau\gamma^2,
 \qquad b^2\ge\tau\gamma^2+\eta.
\]

The integration by parts is legitimate: the differentiated tanh has a
bounded derivative and the Gaussian boundary term vanishes. Since
`0<beta<=alpha nu`, the numerator defining `B_*` is at most
`eta/gamma+tau gamma`; hence `0<B_*<=1/gamma`. Integrating
`sech^2 z>=1-z^2` gives the stated lower bound on `K(h)/h`.
The replacement of `B_*` by its upper bound has the correct direction
because `m-alpha<0`.

The remaining scalar bounds are also justified without numerical input:
`nu<3/7`, `alpha>11/15`, `nu>1/64`, and
`gamma>=alpha-alpha^2 nu`. The lower bound on `nu` follows from the
probability of `1/2<=|G|<=1` and the proved bound on `tanh(1/2)`.
The bracket in the certificate is consequently bounded below by

\[
 2\alpha-1-\alpha^2(\nu+1/3)-1/65
 \ge 7/15-1936/4725-1/65=2552/61425>0.
\]

The monotonicity in `alpha` and `nu` used for this substitution has the
stated sign on the full bounding rectangle. Thus `Psi(h)` has the strict
sign of `h`. Conditioning the other input coordinates gives the stated
formula for `T(r)`; for `r>0` the conditional second factor has the strict
sign of G. Therefore `T(r)>0`, and specifically
`rho_0=sqrt(3)T(1/sqrt(3))>0`. This is a proved coefficient of the exact
initialization, not an assumed trained-state sign condition.

## 2. Scalar-clock protection and actual fitted endpoints

The equal-weight transitive symmetry makes every reference residual equal.
The physical equation is therefore exactly
`theta_dot=2(1-F) grad F`, with the original metric and every matrix entry
retained. Along the ascent clock, the three identities

\[
 F_s=\|\nabla F\|^2\ge\|\bar h\|_2^2,
 \quad C_s=2F,
 \quad F=\langle c,\bar h\rangle
\]

are valid. Canonical `c(0)=0` gives `F(s)=ks+o(s)` and
`C(s)=ks^2+o(s^2)`. For positive s, monotonicity of F and its positive
initial derivative imply `F,C>0`. Cauchy--Schwarz then proves that
`F^2/C` is nondecreasing from k, so `F_s>=k` throughout the clock.
The quotient is used only for positive s; its initial value is a limit.

The clock bounds (5) follow directly from bounded features and unit inputs:
`|c_s|<=1`, `||M_s||_F<=L_1 L_2 s`, and
`||w_s||_infinity<=L_1 L_2 s ||M||_F`. Their integrations have the
correct constants. Local contraction in the affine space
`g+L-infinity` and these bounds rule out finite-clock escape. Thus the
unique level-one crossing `s_*<=1/k` exists as an actual finite-clock
state.

The physical scalar clock approaches this crossing without reaching it at
finite time, by local uniqueness at its equilibrium. Its loss satisfies
`L_dot=-4F_s L<=-4kL`. Continuity at finite clock time supplies convergence
of the complete state to `theta(s_*)` in the asserted increment-supremum
and matrix norms. No endpoint or future feature-Gram lower bound is assumed.

## 3. Cyclic geometry and nonzero lower backward fields

The cyclic Gram eigenvalues are exactly
`3 cos^2(theta), (3/2)sin^2(theta), (3/2)sin^2(theta)`.
Consequently the displayed triples are independent for sufficiently small
positive opening. Coordinate permutation is an actual symmetry of the
joint canonical marks and the two constant bands of D. It preserves the
full vector field, including its transpose action.

The Section 2 analytic activity argument is sound: Gaussian correlation
has the displayed Hermite power series on `|r|<1`; `T(1)>0` excludes the
zero function. The averaged upper activation cannot be the zero function
when z is nonzero, by either its linear term or the cubic product identity.
The upper mark law has positive density on a box containing zero.
Alternatively, the stronger positivity certificate immediately supplies
activity at the collapsed diagonal. Continuity then gives
`k_theta>=k_collapsed/2>0` for all sufficiently small openings.

At the collapsed reference, permutation symmetry gives
`Ma=rho v` and `d=delta v`. The positive initial `rho_0` and
`c_s=tanh(rho B)` imply that c has the strict sign of B at every positive
clock time as long as rho remains positive. The differentiated lower
contraction is

\[
 a_s=S M^T d,\qquad
 S=E[b_1b_1^T\operatorname{sech}^4(w\cdot v)]\succeq0.
\]

It follows that
`rho_s=delta (||a||^2+v^T M S M^T v)>=0`.
The first-zero argument is valid, so rho remains positive and delta is
strictly positive at the fitted endpoint. Moreover `M^T v` cannot vanish
there because `v^T Ma=rho>0`.

The lower feature covariance is positive definite. Within each coordinate
pair, independent nondegenerate reverse noise makes the conditional
variance of k given h strictly positive, and `Var(h)>0`; different pairs
are independent and centered. The invertible normalization preserves
positive definiteness. Thus
`q_*=delta b_1^T M^T v` has strictly positive L2 norm.

On a common finite clock interval, the polynomial bounds and the Hilbert
regularity checked below give continuous dependence on opening. The common
lower bound on `F_s` and uniform convergence of F imply convergence of its
level-one hitting times and hence of the actual fitted states. Continuity
of `q_j` in state and input therefore transfers its nonzero L2 norm to
all three endpoint fields for every sufficiently small positive opening.
This is precisely the needed endpoint persistence. At canonical time zero
all q fields vanish because c is zero; no all-time positive lower bound on
their individual norms is asserted or needed.

## 4. Full prediction derivative rank and Hilbert regularity

For independent inputs, a relation among the lower gradient rows reads

\[
 \sum_{j=0}^2\xi_j q_j\operatorname{sech}^2(w\cdot u_j)u_j=0
 \quad\text{almost surely}.
\]

Applying the inverse input matrix pointwise forces each scalar coefficient
to vanish. The lower gates are strictly positive almost surely because w
is finite almost surely, and each endpoint `q_j` is nonzero in L2.
Therefore every `xi_j` is zero. The complete derivative has full row rank.
This proof does not require a well-conditioned readout-feature Gram or
a uniform positive lower gate. The gradients also lie in the canonical
mark-parity subspace, so the use of the ambient Hilbert metric does not
create a rank unavailable to the actual canonical dynamics.

The proposed Hilbert regularity is valid despite unbounded Gaussian g.
The finite vector `a(w,u)=E[b_1 tanh(w dot u)]` has derivative
`Da[v]=E[b_1 sech^2(w dot u)(v dot u)]`. Its Taylor remainder is bounded
by a constant times `||v||_2^2`, and subtracting derivatives gives the
stated operator-norm Lipschitz bound by Cauchy--Schwarz. This uses a
finite expectation-valued map, rather than falsely asserting smoothness
of an unrestricted nonlinear substitution operator from L2 to L2.

Since upper preactivations depend on the finite contraction a and finite M,
their changes have pointwise bounds controlled by the Hilbert state
difference. The prediction gradient blocks are exactly

\[
 \nabla_w f=q\operatorname{sech}^2(w\cdot u)u,
 \qquad\nabla_c f=h_2,
 \qquad\nabla_M f=d a^T.
\]

Here `||q||_infinity<=L_1 ||M|| L_2 ||c||_2`.
This bound and the finite contractions justify local Lipschitz bounds on
all three blocks without multiplying two unrestricted L2 fields.
Input perturbations use
`||(u-u_tilde) dot w||_2<=|u-u_tilde| ||w||_2`.
Thus finite input and positive-weight perturbations give jointly locally
Lipschitz J, A, and the vector field on the relevant Hilbert balls.
Gaussian g is in L2, which is sufficient. Local integral contraction and
Gronwall continuous dependence consequently apply, including to the
ascent clock used above.

## 5. Independent data perturbations: entrance, trapping, and bounds

Positive weights make `A_*=sqrt(diag(mu)) J_*` full row rank. Since its
codomain is finite dimensional, `A_* A_*^T` has a positive least
eigenvalue. The proved joint continuity supplies a state ball and a data
neighborhood with `AA^T>=kappa I` and `||A||<=B`. The neighborhood may
be chosen within positive probability weights and independently varied
unit inputs; it need not preserve cyclic symmetry.

The reference trajectory's proved fitted-state convergence allows the
choice of a finite T satisfying both distance and residual requirements
in (15). Finite-horizon continuous dependence supplies those requirements
for every perturbed canonical trajectory after shrinking the neighborhood.
The initial state is the same exact data-independent canonical state.

While inside the ball, the exact gradient identities give
`L_dot<=-4 kappa L` and `||theta_dot||_X<=2B sqrt(L)`.
Their integrated length bound is exactly
`(B/kappa)sqrt(L(T))<delta/4`, whereas exit would require at least
`delta/2` movement. This proves trapping. Bounded vector fields on these
balls permit continuation; integrable path length supplies an actual
Cauchy endpoint with zero loss.

The stronger bounds are also justified. The finite prefix has the
fixed-order feature-envelope existence bounds. On the tail, bounded M
and L2 readout give supremum bounds on q and on the readout velocity;
the input residual average is bounded by `sqrt(L)`. Thus each of
`||w_dot||_infinity`, `||c_dot||_infinity`, and `||M_dot||_F`
is at most a constant times `sqrt(L)`. Integrability yields bounded
increments and endpoints in the stronger stated norms. In particular,
the claim bounds `w-g` in supremum norm and w in L2; it does not claim
that the Gaussian-initialized w itself is in L-infinity.

## 6. Differential exponential decay from time zero

The prefix argument closes the stronger all-time claim. On the symmetric
reference, `r_ref(t)=1-F_ref(t)>0` at every finite t and
`||grad F_ref||>=sqrt(k_ref)`. Therefore on `[0,T]`

\[
 \|A_{\rm ref}^T e_{\rm ref}\|
 =r_{\rm ref}\|\nabla F_{\rm ref}\|
 \ge r_{\rm ref}(T)\sqrt{k_{\rm ref}}=2m>0.
\]

Uniform finite-horizon continuity preserves the lower bound m on a
sufficiently small common data neighborhood. The canonical readout and
unit absolute labels give `L(0)=1`; exact energy monotonicity gives
`L<=1`. Consequently on the prefix
`L_dot<=-4m^2<=-4m^2 L`. Combined with the trapped tail, this proves
`L_dot<=-lambda L` at every nonnegative time, where
`lambda=min(4m^2,4kappa)>0` is uniform on the chosen neighborhood.
There is no omitted entrance prefactor. The current loss is indeed the
claimed state potential throughout the trajectory.

## 7. Scope and final obligation check

Every required bridge is supplied: exact initialized activity; finite-clock
existence; a bounded fitted reference; nonzero endpoint backward fields;
full endpoint prediction rank; Hilbert regularity; finite entrance under
independent input and mass perturbations; invariant trapping; strong state
bounds; and the all-time differential loss estimate.

The theorem is open relative to `(S^2)^3` and the positive probability
simplex, with labels fixed. Bias-free oddness makes flipping the third
input and label an exact identity of the full loss functional at every
state, so the signed-label version and its open neighborhoods follow.
It has reference label masses 2/3 and 1/3, not balanced labels. No arbitrary
rotation invariance is used. The symmetric decay constant is bounded away
from zero as the opening shrinks, while full three-output rank degenerates
at collapse; the text correctly allows the independent-perturbation radius
and decay constant to shrink. Finite quadrature, finite neural networks,
all sphere datasets, other label assignments, and a uniform transverse
rate are outside the assertion.

The surviving limitation is the stated locality of the family, not a
missing premise in its proof. No hypothetical future conditioning or
oracle endpoint is needed.
