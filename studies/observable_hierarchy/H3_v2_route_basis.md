# Revised C-H3: polynomial core with an exhaustive initialized tail

Candidate frozen independently on 2026-09-13 before seeing another route. This is a
theoretical route report, not a promoted result or an empirical result. No
trajectory was run and no claim of useful accuracy at a demonstrated order is
made. The proposed finite orders below have *proved distinct retained spans*.

## Scope and conclusion

The scientific inputs read completely were `docs/global_nonlinear.md`
C.4.7.8–C.4.7.9 (lines 11441–12554 at reading), `docs/NOTATION.md`, and
`code/pde/observable_closure.py`. Shared instructions, the rigorous-math and
conjecture-investigation skills, and the latter's research-contract,
adversarial-audit and proof-search references were also read. No other study,
study README, route, history or external scientific source was read. Established
theorems invoked below are the conclusions of these allowed sections; their
upstream source proofs were outside this assignment and were not independently
reaudited here.

The main constructive result is a different dictionary that has a small,
explicit Gaussian core. Its first three degree orders have feature dimensions
`(5,3)`, `(15,6)`, `(35,10)` on the two populations. These are genuine span
enrichments, not just changes to a ridge or duplicate columns. The associated
initial action contractions use Gaussian integrals in dimensions four and two,
including a nonzero forward/reverse response term; forming those contractions
does not require introducing further integration dimensions. An exhaustive
bounded-word tail restores the full observable-space density required by C-H2.

The second result is a fixed-order stability argument for numerical population
and data measures when the feature maps have common finite bounds. Together
with a continuous, full-Gram Gaussian initialization procedure, it supplies a
fully specified *iterated numerical consistency limit*. There is no rate,
error certificate, tolerance-to-order selector, growing-width invocation or
finite-order accuracy claim.

The exact model, loss, block mobilities, physical time and action/adjoint are
C-H1 (H1)–(H3). Fix `Y >= 1`, `T = 1/200`, and `rho = delta/2` as in C-H2.
All predictions are compared uniformly on `[0,T] × S1`. Every observation
tuple is separately fixed before limits and uses its same-population joint
law, with Euclidean W2 and quadratic contractions as in C-H2.

## 1. A small jointly initialized core

Use the following *frozen initialized* observations:

\[
h_i=\sin g_i,\qquad \xi_i=A_0h_i,\qquad
s_i=\sin\xi_i,\qquad p_i=A_0^*s_i,\qquad i=1,2.
\]

Define the positive scalar constants

\[
v=E\sin^2G=(1-e^{-2})/2,
\qquad \alpha=e^{-v/2},
\qquad \tau=(1-e^{-2v})/2,
\quad G\sim N(0,1).
\]

The H6 joint source rule gives the exact realization

\[
\xi_1,\xi_2\stackrel{\rm iid}{\sim}N(0,v),
\qquad p_i=\zeta_i+\alpha\sin g_i,
\qquad \zeta_1,\zeta_2\stackrel{\rm iid}{\sim}N(0,\tau),
\tag{1}
\]

where the reverse Gaussian group is independent of `g`, and the two population
groups are integrated separately. Indeed `E[h_i h_j]=v delta_ij`,
`E[s_i s_j]=tau delta_ij`, and the only nonzero response derivative is
`E[partial_(xi_i) sin xi_i]=alpha`. The independent reverse source in (1) is
retained; discarding it would change the model.

The bounded coordinate vectors are

\[
X_1=(\tanh g_1,\tanh g_2,\tanh p_1,\tanh p_2),
\qquad X_2=(\tanh\xi_1,\tanh\xi_2).
\tag{2}
\]

Their distributions have strictly positive densities on the open cubes of
dimensions four and two. For population 1, the density of `(g,p)` is a strictly
positive Gaussian density in `g` times a strictly positive Gaussian density
in `p-alpha sin g`; applying the coordinatewise tanh diffeomorphism proves
the assertion. The second population is the direct Gaussian case. Thus a
nonzero polynomial in either vector cannot vanish almost surely: continuity
would make it nonzero on an open set of positive density. The elementary fact
that a polynomial vanishing on an open box is zero follows by induction on its
number of variables, using the one-variable finite-root property.

Let `T_j` denote the Chebyshev polynomial, specified by
`T_0=1`, `T_1=x`, `T_(j+1)=2x T_j-T_(j-1)`. The identity
`T_j(cos theta)=cos(j theta)` follows by induction from the cosine addition
identity, and gives `|T_j(x)| <= 1` on `[-1,1]`. For each order `m >= 1`, retain

\[
\mathcal P_{\ell,m}
=\left\{\prod_{i=1}^{d_\ell}T_{a_i}(X_{\ell,i}):
a_i\ge0,\quad \sum_i a_i\le m\right\},
\qquad(d_1,d_2)=(4,2).
\tag{3}
\]

These are bounded admissible initialized words: the recurrence uses rational
affine operations and bounded products, and each coordinate in (2) is an
admissible word. Each raw feature is bounded by one. Distinct products in (3)
are linearly independent: their leading monomials have different exponent
vectors, and polynomial vanishing is excluded by the positive-density argument.
The count is `binomial(m+d_l,d_l)`, by counting nonnegative exponent vectors
with one additional slack coordinate.

For density beyond this fixed core, append every bounded valid C-H2 code
`n <= m`, with its dependencies and population type. Omit only literal syntax
duplicates already present; do not perform a numerical rank test or discard
small modes. The code enumeration is the established exhaustive grammar,
not a hidden function-valued feature. Denote the resulting nested finite list
by `psi_(l,m)`. At `m=1,2,3`, the code prefix contributes only the already
present constants: codes 2 and 3 are unbounded seeds. Consequently the exact
first three retained dimensions and matrix sizes are

| Degree m | Population 1 | Population 2 | Action coefficients |
|---:|---:|---:|---:|
| 1 | 5 | 3 | 15 |
| 2 | 15 | 6 | 90 |
| 3 | 35 | 10 | 350 |

All contain reverse-dependent first-population features. Their strictly
increasing dimensions are exact, independently of the chosen quadrature.
Numerical rank is a separate diagnostic and is not this proof.

## 2. A nonadaptive positive filter and the density proof

Use the explicit rational schedule

\[
\eta_m=\frac{1}{1024(m+1)^2},\quad
G_{\ell,m}=E_\ell[\psi_{\ell,m}\psi_{\ell,m}^{T}],\quad
b_{\ell,m}=(G_{\ell,m}+\eta_m I)^{-1/2}\psi_{\ell,m}.
\tag{4}
\]

The prefactor is a fixed design choice, not an error tolerance. Replacing it
by any fixed positive rational gives the same proof. The schedule is unrelated
to training data, a time mesh, future observables, width or measured error.

Let `U_l a=b_l^T a` on the canonical carrier and `Q_l=U_l U_l*`.
Diagonalizing the finite Gram gives `U_l*U_l <= I`, so both maps are
contractions and `Q_l` is a positive contraction. If `psi_l` has envelope
vector `B_l`, then `|b_l| <= eta_m^(-1/2)|B_l|`; this is a finite common
pointwise bound at each fixed order, not an order-uniform assertion.

The exhaustive appended tail contains every rational initialized bounded word
at some finite order. C-H2's rational-mark argument and C-H1's
Fourier-cylinder argument therefore give density in the entire initialized
observable L2 space. For completeness, if `S_m a=psi_m^T a`, then

\[
\|(I-Q_m)S_m a\|_2
=\|\eta_m S_m(G_m+\eta_m I)^{-1}a\|_2
\le \tfrac12\sqrt{\eta_m}\,|a|.
\tag{5}
\]

This is the scalar inequality
`eta sqrt(lambda)/(lambda+eta) <= sqrt(eta)/2` on every Gram eigenvalue.
An earlier finite-span representation keeps its coefficient norm when
zero-padded. Hence (5), followed by approximation from that dense union and
`||I-Q_m|| <= 1`, proves `Q_m v -> v` for every observable `v`.

Define `D_m=U_2* A0 U_1` by joint initialized contractions. Exactly as in
C-H2, `||D_m|| <= 2` and the proof action
`B_m=Q_2 A0 Q_1` converges strongly together with its adjoint. Strong
convergence is uniform on compact L2 sets by a finite net and the common
operator bound. The same contraction argument approximates compact curves of
Hilbert–Schmidt increments. These are precisely the three error-production
terms in H2.10. The direct H2.11–H2.16 comparison then applies without any
change to its constants or nonlinear tail mechanism. It proves the full
C-H2 limiting predictions and separately fixed observation tuples for this
new dictionary and ridge schedule. A different coding order is not being
mistaken for a new population dynamics theorem.

Operationally, evolve *exactly* H2.3–H2.6 with these `b_l,D_m`: save two
current joint populations `(b,g,w)` and `(b,c)`, and the finite `M,D_m`.
Recompute nonlinear fields on the whole circle; use `M^T` for the reverse
action. There is no extra hidden operator, trajectory coefficient or frozen
training kernel. The existing well-posedness, energy, own-state restart and
observation rules apply since their required feature bounds and contraction
properties have just been verified.

## 3. Exact low-order contractions without extra Gaussian dimensions

At degrees one through three, let `F(g,zeta)` be a raw population-1 feature
and `H(xi)` a raw population-2 feature. Define

\[
\beta_i=E_1[F\sin g_i],\qquad
\gamma_i=E_1[\partial_{\zeta_i}F].
\]

In the *same initialized program*, a new forward call gives

\[
A_0 F=\xi_F+\sum_{i=1}^2\gamma_i\sin\xi_i,
\qquad E[\xi_F\xi_i]=\beta_i.
\]

There may be further Gaussian innovation in `xi_F`; it is not set to zero.
Because the existing forward covariance is `v I`, the centered Gaussian
`xi_F-sum_i(beta_i/v)xi_i` is independent of `(xi_1,xi_2)` and has mean
zero, also in the zero-innovation case. Thus its contribution to this
particular contraction is zero and

\[
E_2[H A_0F]
=\sum_{i=1}^2\frac{\beta_i}{v}E_2[H\xi_i]
 +\sum_{i=1}^2\gamma_i E_2[H\sin\xi_i].
\tag{6}
\]

The first term is the covariance contribution and the second is the full
reverse-to-forward response. Both are needed. The same expression is
`E_1[(A0*H)F]` by the actual adjoint; no independently sampled reverse map
is used. The derivative in `gamma_i` is with respect to the formal named
reverse source, holding covariance and earlier response coefficients fixed.

All population-1 expectations in (6), and its raw feature Gram, use only
the four independent Gaussians `(g1,g2,zeta1,zeta2)`. All population-2
expectations use only the two Gaussians `(xi1,xi2)`. The normalization (4)
is applied afterward to the raw contraction matrix. Thus adding polynomial
features at the first three orders increases finite matrix work but not the
underlying Gaussian integration dimension. This is an exact conditional
integration identity, not a covariance supplied in place of the Gaussian
neural law.

When the exhaustive tail reaches extra action words, (6) alone is insufficient.
Use the complete finite source program described next. There is no claim that
the full dense hierarchy retains the four/two integration dimensions.

## 4. A continuous finite Gaussian initialization algorithm

The prototype's incremental QR/Schur extension is not by itself a proved
continuous numerical initializer at singular source Grams. A route that relies
on it unchanged has a gap. The following finite-law procedure avoids a rank
decision and is an alternative mathematical numerical specification.

Keep the formal named source coordinates, their two covariance matrices and
the already fixed response coefficients. At each new oriented action call:

1. Evaluate, on its input population, all the old operands for that orientation
   and the new operand. Form the *entire* uncentered Gram of this finite list
   using a common positive Gaussian quadrature. Compute the new response
   expectations using derivatives with respect to the formal named sources.
2. Store those response coefficients and replace that source group's covariance
   by this full Gram. Realize its named sources using the positive-semidefinite
   principal square root of the Gram applied to a vector of independent standard
   Gaussians of length equal to the number of named sources. Retain zero
   directions; do not threshold eigenvalues or remove named derivatives.
3. Continue in the fixed causal order. After the entire contraction union has
   been constructed, evaluate both complete joint initial laws and raw Grams
   and contractions, then use (4).

At *exact* integration this is H6. Adding a source preserves the old marginal
law: the old-old block of the full operand Gram equals its previously stored
Gram, because all old operands depend only on already named coordinates and
later source extensions preserve their marginals. Induction on the action calls
proves that the old expressions and response coefficients retain their H6 law.
The principal-root realization may change a coupling to auxiliary independent
Gaussians, but never that named joint law. The new covariance and response are
exactly H6's. This argument includes duplicated and zero-variance operands.

At finite quadrature the old-old block can change slightly. It is not claimed
to be an exact extension at that resolution. It is a consistent approximation:
fix the finite program first, and let the common Gaussian quadrature converge
in W2 to each needed standard Gaussian law. Inductively all previous
covariances and coefficients converge. The principal square root is continuous
even at a singular positive-semidefinite matrix: roots of a converging bounded
matrix sequence are bounded; every convergent subsequence limit is positive
semidefinite and squares to the limiting matrix; diagonalizing that matrix
proves uniqueness of its positive-semidefinite square root. Hence all roots
converge. Coupling them by the same finite standard Gaussian vector gives L2
convergence of the named sources.

The allowed finite words have uniform linear-growth envelopes and bounded
named-source derivatives when their finitely many coefficients range in a
compact neighborhood of their limits. Bounded operands and their Gram
integrands converge by bounded convergence; response expectations converge
by their bounded derivative envelopes. For final contractions, an L2 action
output times a bounded feature converges in L1 by subtraction and
Cauchy–Schwarz. Source laws are finite Gaussian laws, so the linear-growth
envelopes also give uniform square-tail control. These facts justify the
induction under the Gaussian quadrature and prove W2 convergence of the final
joint laws. The strictly positive fixed `eta_m` makes normalization continuous
and supplies a uniform finite feature envelope for all sufficiently resolved
initializations.

A completely finite positive Gaussian quadrature sequence is obtained by
one-dimensional Gaussian quantile midpoints `(j-1/2)/k`, each of weight `1/k`,
and their tensor product in every separately fixed dimension. Their quantile
step functions converge in L2 to the Gaussian quantile function. On a central
probability interval this is uniform continuity; on either tail monotonicity
bounds a midpoint's squared value by twice the integral over the outer half
of its cell, so the L2 tails vanish. Tensor products and the product coupling
give the finite-dimensional W2 conclusion. Quantiles and all elementary
integrals/algebra can be approximated with increasing arithmetic precision;
arithmetic precision is removed first below.

The source principal root can be approximated without any zero-eigenvalue
decision, for example by uniform polynomial approximations to `sqrt(x)` on
a bounded spectral interval, followed by precision refinement. The source
Gram is formed from a positive weighted list, not repaired by an empirical
eigenvalue cutoff. The ridge inverse square root is approximated on its
strictly positive spectral interval. Only convergence of these routines is
needed; there is no error certificate or useful complexity claim.

The derivative coordinates must remain *named-source* coordinates. Taking AD
with respect to the auxiliary independent Gaussians after multiplying by a
square root would generally compute a different derivative and invalidate H6.

## 5. Fixed-order dependence on population and data measures

Here the feature dimension is fixed. Consider two H2.4–H2.6 systems, with
initial mark laws `lambda_1=Law(b,g)`, `lambda_2=Law(b)` and their tilded
counterparts, initialization matrices `D, D_tilde`, and data laws `mu,mu_tilde`.
Assume a common finite pointwise feature bound `|b_l| <= L_l`, finite common
`||g||_2` and matrix bounds, labels bounded by `Y`, `w(0)=g`, and `c(0)=0`.
The feature Grams need not be contractions for this numerical comparison.

Each system is still an exact gradient flow in its own population L2 metrics
and the Euclidean `M` metric. The scalar differentiation used in H2.7 uses
only these same pairings; it does not require normalized feature Grams. Thus
the loss stays at most `Y^2`, and `integral |r| dmu <= Y`. It follows that

\[
\|c(t)\|_\infty\le2Yt,\quad
|a(u)|\le L_1,\quad |d(u)|\le2L_2Yt,
\quad \|M(t)\|\le\|D\|+2L_1L_2Y^2t^2.
\tag{7}
\]

Indeed `||M'|| <= 2 integral |r| |d| |a| <= 4 L1 L2 Y^2 t`.
Also `|q(u,b)| <= L1 ||M|| |d|`, so

\[
\|w'(t)\|_\infty
\le4L_1L_2Y^2t\,\|M(t)\|.
\tag{8}
\]

This is a bound on the increment velocity; the frozen `g` remains unbounded.
Equations (7)–(8) give uniform sup bounds for increments and readouts and L2
bounds for rows on `[0,T]`. Local existence and continuation follow by the
same bounded-characteristic contraction argument as C-H2. Constants here may
depend on the fixed feature order and envelopes.

Take any couplings `pi_1,pi_2` of the initial joint mark laws and transport
both endpoints along their own characteristics. Let

\[
e(t)=\|w-\widetilde w\|_{L^2(\pi_1)}
 +\|c-\widetilde c\|_{L^2(\pi_2)}
 +\|M-\widetilde M\|_F,
\quad \epsilon_b=\sum_\ell\|b_\ell-\widetilde b_\ell\|_{L^2(\pi_\ell)}.
\]

For identical input `u`, explicit subtractions give

\[
|a-\widetilde a|
\le \|b_1-\widetilde b_1\|_2
 +L_1\|w-\widetilde w\|_2,
\]

and, splitting `b^T M a` into changes of its three factors,

\[
\|z_2-\widetilde z_2\|_2
 +|f-\widetilde f|+|d-\widetilde d|
 +\|q-\widetilde q\|_2
\le C(e+\epsilon_b).
\tag{9}
\]

To justify the `d` estimate, split changes of `b`, then `c`, then the gate;
use the common readout bound and `Lip(1-tanh^2) <= 2`. The other terms use
`Lip(tanh) <= 1` and (7). In the row drift the changed lower gate multiplies
the *bounded* reference `q`, bounded pointwise by (7), so it costs at most
`2 ||q||_infty ||w-w_tilde||_2`. This is where bounded features remove the
unrestricted-L2 product obstruction. Matrix rank products and readout drifts
are bounded by the same direct two-factor subtractions. For a common data law,
therefore, the drift difference is at most `C(e+epsilon_b)` in the sum norm.

For the data-law change, its integrands are Lipschitz into this same sum norm
on `Z` with the normalized-input-plus-label distance. To check the potentially
unbounded row term,

\[
\|\tanh(w\cdot u)-\tanh(w\cdot v)\|_2
\le\|w\|_2|u-v|,
\]

and the lower-gate difference has at most twice this bound. The `a,z2,d,q,f`
input differences then follow as above from bounded `b,c,M`; the explicit
factor `u` contributes `|u-v|`. Label dependence is affine through `r=f-y`.
The common row L2 bound from (8) makes the resulting Lipschitz constant finite.
Integrating the difference under a coupling of the two data laws proves a
drift difference at most `C W1(mu,mu_tilde)`.

Thus almost everywhere

\[
e'(t)\le C\bigl(e(t)+\epsilon_b+W_1(\mu,\widetilde\mu)\bigr).
\]

Multiply by `exp(-Ct)` and integrate to obtain

\[
\sup_{t\le T} e(t)
\le e^{CT}\{e(0)+CT[\epsilon_b+W_1(\mu,\widetilde\mu)]\}.
\tag{10}
\]

An arbitrarily near-optimal initial W2 coupling bounds `epsilon_b`, the initial
row error and the frozen `g` discrepancy by the initial joint-law distances;
`e(0)` also includes `||D-D_tilde||`. Equation (10), with the unchanged static
coordinates included, controls the full saved joint population laws in W2.
Equation (9) controls prediction uniformly over the whole circle. Induction
through each separately fixed observation graph gives its joint W2 and
quadratic-contraction convergence: bounded gates preserve L2 convergence,
finite action kernels are bounded, and the frozen seeds use the same marks.
The growing-graph or growing-order version of (10) is not asserted.

This lemma permits numerical feature laws that are small perturbations of the
canonical initialized law. Insisting only on W2 convergence without a common
pointwise feature bound would not justify its crucial `q` bound. The ridge
and bounded raw words provide that hypothesis at every fixed order.

## 6. A fixed represented law family and all numerical axes

One concrete family is the following two labeled arcs. For finite rational
parameters `theta_1,theta_2,sigma_1,sigma_2`, with `sigma_i >= 0`, set

\[
u_1(s)=(\cos(\theta_1+\sigma_1s),\sin(\theta_1+\sigma_1s)),
\]
\[
u_2(s)=(\cos(\pi/2+\theta_2+\sigma_2s),
          \sin(\pi/2+\theta_2+\sigma_2s)),
\quad -1\le s\le1,
\]

and let `mu` be half the pushforward of uniform `s` to `(sqrt(2)u_1(s),+1)`
and half its pushforward to `(sqrt(2)u_2(s),-1)`. Retain all these represented
laws satisfying

\[
|\theta_1|+|\theta_2|+\sigma_1+\sigma_2\le\rho.
\tag{11}
\]

Transport each arc to its reference input. Since chord distance is bounded
by angular distance, `W1(mu,nu*) <= rho/2 < rho`. This single family is fixed
before all approximation orders. It includes nonorthogonal two-atom laws
(`sigma_i=0`, unequal small angle shifts), and nonatomic laws (`sigma_i>0`).
It inherits the canonical positive hidden-motion/nonaffinity time from C-H1
part 8. The bound uses the established positive `rho`; the allowed inputs do
not supply a numerical lower bound for that radius. Consequently this report
does not certify a particular decimal perturbation as belonging to the family.
That is a limitation of numeric membership certification, not a shrinking
family or an assumption on the unknown trajectory.

For a supplied represented member, use midpoint quadrature in `s` on each
arc, retaining the correct label and mass. Its data W1 convergence follows
by coupling each interval to its midpoint and continuity of the arc map.
The atomic cases are already exact. No input mesh is used to replace the
whole-circle observation map; every reported circle value is recomputed from
the current state. Uniformity follows from (9)–(10).

Distinguish six axes in a finite output `O_hat_(m,k,n,r,J,p)`:

- `m`: dictionary degree plus exhaustive code prefix, and the fixed ridge (4).
- `k`: Gaussian quadrature for the finite initializer's coefficients, feature
  Grams and contractions. For each `m,k`, its computed finite coefficients
  define bounded feature maps of a standard Gaussian variable and hence exact
  auxiliary mark laws `lambda_(l,m,k)`. These auxiliary laws are the objects
  approximated on the next axis; they do not require exact population integrals
  in the final implementation.
- `n`: a separate positive Gaussian quadrature of those complete joint mark
  maps, yielding finite current population tables initialized with `w=g,c=0`.
  Each same-population mark tuple is evaluated on one common Gaussian node.
- `r`: the arc/data integration mesh just described.
- `J`: simultaneous explicit Euler updates of all current `w,c,M` with step
  `T/J`, linear interpolation of these state coordinates, and recomputation
  of observations from that interpolated state.
- `p`: increasing arithmetic precision for all finite operations, including
  initialization, roots, quadrature nodes, gates and time updates.

Every finite member consists of two finite weighted population tables and a
finite action matrix. Population sizes depend on quadrature resolution, not
neural width. Store its marks, weights, current rows/readouts, `M,D`, dictionary
and represented data parameters for restart. No original dense network matrix,
elapsed trajectory or target observation is retained.

The acceptable consistency statement is the following iterated limit, with
rightmost limits taken first:

\[
\lim_{m\to\infty}\lim_{k\to\infty}\lim_{n\to\infty}
\lim_{r\to\infty}\lim_{J\to\infty}\lim_{p\to\infty}
d_T\bigl(\widehat O_{m,k,n,r,J,p},O_{\rm canonical}\bigr)=0.
\tag{12}
\]

Here `d_T` can be the prediction supremum norm or the supremum-in-time W2
distance of any separately fixed admitted joint tuple; quadratic contractions
converge as well. The statement is for each fixed represented law and tuple,
not uniformly over an unbounded collection of programs or a simultaneous
diagonal of all numerical axes.

Every bridge in (12) has a distinct justification:

1. At fixed finite `m,k,n,r,J`, the algorithm has finitely many continuous real
   operations. Principal source roots are continuous at zero, ridge roots
   stay strictly positive, and there is no thresholded rank branch. Increasing
   arithmetic precision converges to that finite exact-real output.
2. At fixed population tables and data mesh, the smooth finite ODE has the
   bounds (7)–(8). On a neighborhood of its compact exact path its velocity is
   bounded and Lipschitz. The exact integral identity gives a local Euler
   defect at most `C h^2`; the error recurrence is
   `e_(j+1) <= (1+Lh)e_j+C h^2`. Summing the geometric series yields a bound
   tending to zero as `h=T/J -> 0`. A first-exit argument keeps the numerical
   path in that neighborhood for sufficiently large `J`. This proves uniform
   convergence without an adaptive step selector.
3. Data W1 convergence and (10) remove `r`.
4. Complete joint-mark W2 convergence under positive Gaussian quadrature,
   the fixed feature bounds, and (10) remove `n`.
5. Section 4 gives joint initial-law and matrix convergence as `k -> infinity`,
   with a common feature bound supplied by fixed positive `eta_m`. Equation
   (10) removes `k`. Early-order contractions may use the exact reduction (6).
6. Section 2 and the established C-H2 comparison remove `m`, identifying the
   limit with canonical nonlinear H2 dynamics on the unchanged interval and
   family. C-H2's same-carrier observation argument supplies the final tuples
   and second moments.

All approximations are operationally finite before any limit. Intermediate
exact population objects only identify the successive limits. Equation (12)
does not justify exchanging two limits, selecting a tolerance, retaining
float64 for arbitrarily high order, or claiming accuracy at `m=1,2,3`.

## 7. Audit, obstructions and recommendation

The strongest surviving practical obstruction is Gaussian dimension and
conditioning after the exhaustive tail begins to request new action words.
This route removes unnecessary contraction-source dimensions from the first
three orders and avoids the original code prefix's lack of early span
enrichment. It does not prove an economical dense-order sequence. The explicit
ridge gives bounded features at a fixed order but no useful order-uniform
conditioning, accuracy, cost or finite-precision guarantee.

The raw H6 initialization is not a free isonormal embedding: (1) keeps the
surviving reverse Gaussian source, and (6) keeps its feedback into a subsequent
forward action. Omitting either is a witness-fatal model change. The full-Gram
procedure is a distinct consistent numerical initializer, and would require
implementation and deterministic verification before an executed-method claim.
The current prototype does not already implement it or the alternative basis.

The numerical measure argument requires bounded *feature maps*, while allowing
Gaussian frozen rows and their current row values to remain unbounded in L2.
This distinction is essential. A proof relying on arbitrary W2 mark laws with
unbounded `b`, or on pointwise continuity alone for the raw row terms, is incomplete.

No trajectories, monotone error trends or visible learning at the three proposed
orders were established. The nonlinear target and fixed positive horizon follow
from the established family and the limiting theorem, and do not constitute
an empirical finite-order success. No resource certificate or tolerance-to-order
construction is supplied or needed for (12).

Recommended status: **candidate theoretical construction with a complete
fixed-order measure comparison and an explicit iterated-limit route**. It is
suitable for the supervisor's comparison and scrutiny; implementation,
independent checking, full dependency audit and any promotion remain separate.

## Read-time provenance

The read-time shared HEAD was `c45e04d4efd0ff52e1c2f32b633fb9e8682157bd`.
Only metadata was inspected outside the assigned inputs. Existing concurrent
changes were preserved; this route edited only this assigned report.

| Input | SHA-256 at reading |
|---|---|
| `docs/global_nonlinear.md` | `947eb52f10a8ebcd4970fa2acb1d26cba25dc5d73e8839893d5d2f4e3f688161` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `code/pde/observable_closure.py` | `f8dc5d16e5de1737444c44aae737ee1c9b4d664188d72f59acd0bb92f457c137` |
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
