# Growing smooth caps: fresh combined proof audit

2026-10-01. **PASS for the precise conditional all-time theorem and its
fixed-confidence consequence in M_SCALE_RESULT.md, at the input hashes
below.** This is an internal mathematical check, not promotion. It does
not certify an all-initialization all-time second moment, a cap-independent
root-width constant, or convergence to an unclipped population.

## Assignment, scope, and exact verdict

The audited claim concerns the model of SMOOTH_SETUP.md: two hidden tanh
layers, the original Gaussian mixer and its actual transpose, q=1 memories,
the residual-RMS clock, zero initial readout and values, and the two
recursive gates c_M(s)=M tanh(s/M). The labels are fixed, nonzero, and
independent of width and cap. The initial population readout-feature Gram
has a positive gap; queries lie in a fixed bounded set.

There is one positive label threshold, independent of M>=1, for which
constants C,c>0 can be chosen so that, with

\[
T_C(M)=\exp\{\exp[\exp(C(1+M))]\},
\]

\[
\left(\mathbb E\left[\int\sup_{t\ge0}
 |f_{n,M}(t,x)-f_{\infty,M}(t,x)|^2\,d\mu(x)
 \;\middle|\;\mathcal G_n\right]\right)^{1/2}
 \le T_C(M)n^{-1/2},\qquad n\ge T_C(M)^4.
\]

The event G_n is cap independent and has complement probability at most
Ce^{-cn}. The comparison includes the finite-width mean bias and the
fitted endpoint, and its reference is the system's own smooth population.
For the displayed triple-log schedule the resulting bound is
n^{-1/2+o(1)}. I found no unresolved step within this claim and the supplied
dependency scope.

I read the complete six principal inputs and all five supporting notes
listed at the end. In particular, I reconstructed the local cavity,
tagged-response, mean-map tensor, passive-velocity, and feedback arguments;
I did not accept their conclusions from prior review verdicts. No historical
review report, other study, experiment, manuscript edit, or Git operation
was used. The required research, rigorous-proof, and canonical-notation
skills, including the neural-response and adversarial-audit references,
were applied. The foundational finite-Gaussian-program/common-action
construction is used in the form stated and justified in
CLIPPED_POPULATION_ROUTE.md Section 4; this scoped audit did not reopen
its underlying maintained-book theorem.

## 1. Common labels and deterministic damping

The fitting estimate uses only |c_M(s)|<=|s|. In normalized Euclidean norm,
the activity s(t)=integral_0^t rho therefore gives, uniformly in M,

\[
\|w\|_\infty,\|d_a\|_\infty\le Cs,\quad
\|v_a\|_\infty\le Cs^2,\quad \|k_a\|_\infty\le1,
\quad\|\ell_a\|_n\le Cs.
\]

The true prediction derivative uses w sech^2(z), not the clipped d.
Its hidden-motion correction has size Cs^2 rho. A fixed positive
initial Gram margin thus yields rho(t)<=Y exp(-lambda t) and total
activity S_0=Y/lambda, with one M-independent small-label condition.
SMOOTH_ALLINIT_ROUTE.md supplies this calculation without assuming that
the smooth top clip is inactive.

For first differences, M_CAP_SCHEDULE_ROUTE.md correctly distinguishes
the values of the hidden residual coefficients from their Lipschitz
constants. The values are O(S_0^2), or O(S_0^3) for the clock term, and
are absorbed into the Gram damping using common small labels. Only the
coefficient differences cost C(1+M). In particular the residual-difference
term in the state inequality has an M-independent coefficient: its
read-in contribution uses ||ell||_n<=CS_0, not the coordinate bound M.
Consequently integration of the damped residual inequality before state
Gronwall gives a polynomial in M times exp(CM), with no requirement
M S_0<1. This applies both to initialization stability and to the final
controlled-population comparison.

The scalar-freezing histories also meet the domain uniformly in cap.
The lower residual estimate rho_n(t)>=Y exp(-Ct) and the upper fitting
estimate imply s_n(t)<=C bar s(t). This proves
|bar V(t)|<=C bar s(t)^3; Jensen alone would not prove it. The actual
contraction velocities give |dot bar K|+|dot bar V|<=C bar rho. No
derivative of rho or of r/rho is used.

## 2. Local constants, full Gaussian laws, and localization

For F_M(alpha,p)=M tanh(p sech^2(alpha)/M), a derivative with at least one
p differentiation is bounded independently of M>=1 at each fixed order.
A pure alpha derivative is bounded by CM and also by C|p|. On the upper
branch p=w, the latter bound removes M because |w|<=CS_0.

The complete prescribed-history vector Jacobian therefore satisfies

\[
\|L(t)\|_{\rm op}\le C\rho(t)(1+M+K_W^2),
\qquad K_W=\|W_0\|_{\rm op}.
\]

The M term is the direct lower preactivation derivative and carries no
matrix factor. The largest matrix path contains W_0^top, one upper gate,
and W_0, whose scalar derivative is M independent. This separation is
what makes the full-Gaussian moment threshold independent of M.

Each higher variation has this same homogeneous Jacobian. Its source is
a finite sum of products of lower variations and graph derivatives.
Thus every finite-order constant used by the cavity proof has the form

\[
C(1+M)^b(1+K_W)^b
 \exp\{CS_0(1+M+K_W^2)\}.
\]

The induction does not place an already large tangent bound into the
homogeneous Gronwall coefficient. The Gaussian operator tail
P(K_W>L)<=2 exp(-nL^2/16), for fixed sufficiently large L, then integrates
each fixed moment once n exceeds a fixed threshold. The coefficient of
K_W^2 remains independent of M, including after the finite Hölder and
moment enlargements in the tagged calculation. Values are bounded by
exp(C(1+M)); their contributions outside a fixed operator cutoff have
the same cap factor times exp(-cn).

The source calculation is also correctly normalized spatially. A pure
cavity tangent coordinate has conditional fixed-moment size n^{-1/2}.
Its quadratic local defect has size n^{-1}; summing squared defects over
O(n) coordinates gives an ordinary Euclidean remainder of size n^{-1/2}.
The tagged calculation estimates the derivative remainder directly,
using the pure tangent products and the already controlled state
remainder. It never invokes a dimension-free normalized-L2 Hessian.

The forced histories are deterministic before removing a Gaussian row or
column. Conditional Gaussian independence is used only for the cavity
environment, not after conditioning on G_n. The operator-cutoff event
is cavity measurable; the removed Gaussian vector is still integrated
over its full law. Replacing bad cavity data by one admissible tuple,
and separately controlling the removed-vector exceptional set, costs
the stated exponential tail. The comparison to the original conditional
means occurs after this unconditioned forced calculation. These are
distinct conditionings and the proof keeps them distinct.

## 3. Reinsertion and the coarse-domain bridge

The finite cavity and expected covariance/response tuples fit a
deterministic container of size B_M<=exp(C(1+M)). Covariance increments
use normalized signal estimates; response densities and their target-row
regularity use the propagator. Averaging the full-Gaussian response
envelope puts the unlocalized expected tuple in the same enlarged
container. The container need not be invariant under the law map.

The older scalar reinsertion absorption is correctly replaced. In the
upper scalar equation the response of h has no current atom, so changes
in z are bounded by the field error plus
C(1+B_M) integral_0^s sup_{v<=u}|delta z(v)| du. In the lower equation
the upper atom D(s)h(s) enters the read-in ODE. It is not an implicit
algebraic equation for h(s). Its comparison therefore also has an
ordinary causal integral inequality. The directly computed tagged
variation has the same homogeneous equations and controlled sources.

These facts yield a double-exponential scalar constant

\[
A_M\le\exp\{\exp(C(1+M))\}
\]

without decreasing activity as M grows. Fixed-order positive tensors on
a coarse domain can, conservatively, be bounded by
exp(C(1+M+B_M)^12). Substitution of B_M gives the displayed size of A_M.
The finite mean-law defect is therefore at most A_M/sqrt(n), including
the cutoff replacement. Neither this step nor the subsequent comparison
assumes that the whole coarse container maps into itself.

## 4. The causal lower estimate, including response contacts

This is the central new stability step. Let e_H(s) and e_D(s) be the
unnormalized running errors in covariance, source-integrated regular
response rows, and the separate upper atom, as defined in
M_UNIFORM_LAW_ROUTE.md equation (18).

On a mesh, fix a lower Gaussian history slot with cell index r. It first
enters a through the read-in update with factor Delta_r. The deterministic
positive tensor recurrence retains this factor after propagating to h
and summing all other derivative slots. Through the third order needed
for response interpolation, this gives A_M Delta_r. If another slot has
the same numerical source index, there is still only one guaranteed
Delta_r. The proof preserves these diagonal contacts; it does not
incorrectly replace them by Delta_r squared.

For covariance interpolation, group the two covariance slots by their
latest cell r and fix one such slot. Summing the other slots gives

\[
 A_M\sum_r\Delta_r
 \sup_{i,j\le r}|\delta\Gamma_{ij}|.
\]

For an integrated response output, the third tensor has an additional
distinguished response slot. That slot may be later than r. This causes
no failure: the fixed-slot estimate already sums every other slot, while
the covariance-error factor depends only on the two covariance slots.
The direct regular-response source term involving F_{M,p} at its source
has no propagation integral, but the required norm integrates that
source. It therefore retains exactly the needed time integral. The
claim would generally fail in a supremum norm of the pointwise response
density; that stronger norm is not used.

Response-input perturbations have the same structure. An atom or row
insertion at drift time r has size bounded by the current atom error
plus the integrated current response-row error, and it carries Delta_r.
Its additional history derivative and causal propagation preserve that
factor. This yields

\[
e_H(\mathcal L D,\mathcal L\widetilde D;s)
 \le A_M\int_0^s e_D(u)\,du.
\]

The upper map retains its current Gaussian dependence and its current
response atom. Its tensor bounds give e_D(UH,U Htilde;s)<=A_M e_H(s),
without an extra time integral. Both estimates also work for random
input errors because deterministic entrywise tensors multiply each
error before expectation or Lp norms are taken. No expected temporal
supremum is substituted for a supremum of entrywise expectations.

The meshes converge through the explicit source equations, using cell
averages in the source variable and target-row L1 regularity. Singular
covariances are permitted: Gaussian covariance interpolation uses no
inverse. Thus the asserted continuum inequalities follow in precisely
the norm used by the approximate-fixed-point defect.

## 5. Common-domain existence and own-population identification

The construction in M_UNIFORM_LAW_ROUTE.md Sections 2--5 supplies a law
fixed point at a common positive activity size. Its lower pure-state
derivatives use C|p| rather than CM. The lower Gaussian history has a
sub-Gaussian supremum envelope from its mean-square Lipschitz increments
and its zero initial value. The resulting finite-order derivative
envelopes are polynomial times an exponential of that Gaussian
supremum, so every fixed required moment is finite uniformly in M.

The order of domain choices is sound: impose S L_d,S B_d<=1, choose the
resulting numerical lower constants L_h,B_h, choose finite upper
constants L_d,B_d, and finally reduce one common S_* to satisfy these
restrictions and contraction. Dependence on lower input response data
enters through the atom and row mass, at most C S B_d, so no bare large
B_d is covertly used in the lower recurrence. The expected entrywise
tensors are deterministic after conditioning on an admissible environment;
the environment-measurable covariance error factors out before their
Gaussian averaging. This closes the common-domain existence argument
without a pathwise M-independent lower gate bound.

The revised M_SCALE_RESULT.md uses the correct identification order.
First take this common-domain law fixed point. It and the finite expected
tuple lie in the coarse container. With delta_n=A_M/sqrt(n), their
differences obey

\[
e_H(s)\le\delta_n+A_M\int_0^s e_D(u)\,du,
\qquad e_D(s)\le\delta_n+A_M e_H(s).
\]

Substitution and integral Gronwall give a constant bounded by
C(1+A_M)^2 exp(A_M^2 S_0) delta_n. No condition A_M S_0<1 occurs.
For each fixed M and each fixed prescribed history, the qualitative
finite-program/common-action construction identifies finite observable
limits with the own forced closure population. The quantitative
comparison identifies those same limits with the law fixed point.
Uniqueness of limits identifies their relevant observables; the
population is not defined as a finite-width mean.

Although the histories frozen at the original conditional means depend
on n, this identification is applied with each history held fixed while
the auxiliary forced width tends to infinity. The quantitative constants
are uniform over the stated admissible history class. The common-action
construction for the union of the two prescribed program families puts
the forced and autonomous flows on the same action spaces for the final
deterministic comparison. It is not a coupling obtained by declaring
independent forward and transpose fields.

## 6. Velocity sources, full mean bias, and the final bound

The lower passive feature velocity q=dot h/rho is an explicitly bounded
smooth observable for every fixed cap, with fixed-order constants within
the preceding envelopes. Its reused forward action W_0 q has the joint
Gaussian covariance with W_0 h, a regular response, and a direct current
response atom. SMOOTH_CAVITY_ROUTE.md equations (34)--(38) retain all
three pieces. They give a source estimate, not a derivative of an
already established approximation bound.

The forced prediction velocity uses w sech^2(z) times this action. The
only unbounded extra variable is the passive Gaussian coordinate, which
appears linearly. Its conditional variance is bounded on the localized
domain. The deterministic derivative tensors multiplied by its first
moment therefore justify interpolation of the full joint covariance;
the covariance blocks are not changed separately outside the positive
semidefinite class. The resulting physical error has a factor rho(t).
The key-contraction velocity is handled by the same q observable.

Scalar freezing compares the actual and forced physical velocities
directly, including dot K, and gives integrable errors. The forced-law
comparison supplies the population counterparts. These verify all of
SMOOTH_FEEDBACK_COMPLETION.md equations (5)--(7), with the larger cap
constant. Reconstructing the true moments introduces the explicitly
controlled current K,V discrepancies. Differentiating their exact
reconstruction identity uses the supplied dot K error; it does not
differentiate a value-error estimate.

The final damped state/residual comparison then multiplies the source
by only a polynomial in M times exp(CM), as in Section 1 above. The
centered conditional fluctuation estimate has this smaller factor as
well: the Gaussian-root Lipschitz estimate for the actual velocity is
integrable in physical time, so Lipschitz extension, Gaussian Poincare,
and Minkowski give the supremum inside conditional L2. Adding the
deterministic mean bias proves the claimed full conditional RMS bound.

Every factor is dominated by T_C(M) after enlarging C. Gaussian moment
integrability and P(G_n)>=1/2 require only a fixed minimum width; any
additional requirement that the statistical defect be below a fixed
margin is also covered by n>=T_C(M)^4. No M-dependent label restriction
is hidden in this width condition. Query constants depend only on the
fixed radius and its inner products with training inputs, so integrating
against the bounded-support probability law preserves the estimate.
The conditional Markov bound plus P(G_n^c)<=Ce^{-cn} gives the stated
unconditional fixed-confidence formulation.

## 7. Schedule and claim boundary

Let N_*=exp(exp(exp(1))) and u_n=log log log(n+N_*). For M(n)=sqrt(u_n),

\[
\frac{\log T_C(M(n))}{\log(n+N_*)}
 =\exp\{\exp(C(1+\sqrt{u_n}))-\exp(u_n)\}\longrightarrow0.
\]

Indeed C(1+sqrt(u))-u tends to minus infinity. Hence T_C(M(n))=n^{o(1)},
its fourth power is eventually below n, and the asserted
n^{-1/2+o(1)} rate follows for one fixed nonzero label vector. This
asymptotic deduction checks both the error constant and the width
threshold.

This audit does not establish an estimate uniform over all cap values
inside one expectation. It does not estimate the actual all-time
trajectory on the exceptional initialization event. It does not compare
f_infinity,M(n) with one unclipped target. It does not assert a logarithmic
or faster cap schedule. These are separate, stronger statements.

## Frozen inputs

The check applies to the following versions. M_SCALE_RESULT.md was
updated during the audit to make the population-identification order
explicit; this table records the updated version. No stronger route
developed in parallel is an input to this verdict.

| File | SHA-256 |
|---|---|
| M_SCALE_RESULT.md | 4c00f454061f91ead2ac5d301eb2061bf1177723bd489ef6c13a5d680041e0b9 |
| M_UNIFORM_CAVITY_ROUTE.md | 674edcc8b8c19e107bb4d203d36d70681f82678db50592a4b822adab5e045f71 |
| M_UNIFORM_LAW_ROUTE.md | a140dbb446d502c704939c2799a1a297f55ca9260f931fbc0e347891398a5c0f |
| M_CAP_SCHEDULE_ROUTE.md | 88ecd7b169fa52f532e826b210369d7363f606b4b5a7225b043a46823a82c3dc |
| SMOOTH_SETUP.md | a9a2166984c946a5cceebd6f01c168b052e1b74da2b52a2df92c111aa830eee6 |
| SMOOTH_RESULT.md | 525ee04832a67240ef751c27ce054b545a4d9c6859a180a372e32abb78e6d110 |
| SMOOTH_CAVITY_ROUTE.md | 9e22c3f455a6c0447a654a9af6154c0a6c38247bacf2f5aaf40a408895982315 |
| SMOOTH_MEAN_MAP_ROUTE.md | 9ca3c42741683d9ba37c5dac9a2df6018e606326756b671b89023fbeaba3b95e |
| SMOOTH_FEEDBACK_COMPLETION.md | eb3454d7c13c94ce4a89da8491bca0ff65e207c4d4275a2122ae588cd381d7e2 |
| CLIPPED_POPULATION_ROUTE.md | 63bdd715efc7d05875acd4b591d8d2751f38a4f15246f78b7ebfab44c36b5082 |
| SMOOTH_ALLINIT_ROUTE.md | db8b43883fb81c4e1afc3cb9961620bfda5b5ed0933f55ec57e422085b16ee8a |
