# Continuous conditioning-corrected flow with a quantitative potential

2026-09-19. Lead theoretical candidate, continuation of this study's
optimizer investigation. Not promoted; no experiment or discretization.

## 1. Exact target and what is changed

Use the same finite-data physical Hilbert closure as
ESCAPE_AND_LIMITS.md, Section 1, with phi=tanh and state S=(w,c,M).
The initialization, fixed bounded marks b1,b2, complete joint Gaussian
laws and actual transpose remain canonical. In particular

\[
a_i=E_1[b_1\phi(w\cdot x_i/\sqrt2)],\quad
H_i=\phi(b_2^TMa_i),\quad f_i=E_2[cH_i],\quad
L=\sum_i\mu_i(f_i-y_i)^2.
\tag{1}
\]

The finite inputs lie on sqrt(2) S1; mu_i>0 sum to one, y_i are binary,
and repeated/antipodal observations have compatible labels. Merge them
with sign changes into m representatives. All derivatives below are
in the original fixed population L2/Frobenius metric. Define

\[
(Az)_i=\sqrt{\mu_i}E_2[zH_i],\quad K=AA^*,\quad
e_i=\sqrt{\mu_i}(f_i-y_i),\quad L=|e|^2.
\tag{2}
\]

The starting state has finite physical norm and K0>0. This holds for
canonical p=1,2 and every such finite compatible circle dataset by
INITIAL_EXCLUSION.md and INITIAL_REVIEW.md, Section 6. Those proofs,
not any landscape conjecture, are the only initialization input.

This candidate changes the vector field continuously. It has no
rejected proposals, pauses, hidden-state projection or prescribed
neighborhood of initialization. It adds a current-feature conditioning
penalty and a nonnegative readout descent correction. Bounded random
readout mobilities may be included. The fitting mechanism is the
conditioning correction; the random component is optional.

The correction is small as its strength tends to zero on bounded
regions where the current K stays uniformly positive. It can become
large near singular K. Do not call this a globally uniformly small
additive-noise perturbation or assert unconditional all-horizon
approximation of ordinary GF.

## 2. Current-state potential and explicit dynamics

On the open domain D={S:K(S)>0}, let

\[
R(S)=\operatorname{tr}K(S)^{-1},\qquad
\Phi_\varepsilon(S)=L(S)[1+\varepsilon R(S)],\qquad
\varepsilon>0.
\tag{3}
\]

R depends on w,M alone. It is large when a readout prediction direction
becomes poorly conditioned. For comparison, the minimum-norm readout
correction fitting the current residual has squared norm e^T K^{-1}e,
which is at most L R. This follows by writing the correction as
-A*K^{-1}e, computing its squared norm, and using
lambda_max(K^{-1})<=tr(K^{-1}). This comparison interprets the penalty;
the algorithm is not supplied that fitted correction.

Fix 0<=nu<1. Let P_t act as the identity on w,M and as a selfadjoint
operator P_c(t) on the readout, with

\[
(1-\nu)I\le P_t\le(1+\nu)I.
\tag{4}
\]

Admissible mobility paths below are piecewise constant in physical time,
with finitely many changes on every bounded interval. A concrete random
choice requires only the initial features. Choose an
orthonormal basis q_1,...,q_m of span{H_i(S0)} in L2(lambda2). At
physical times j tau, tau>0 fixed, draw independent signs xi_{j,l}=+/-1
with equal probability and, throughout [j tau,(j+1)tau), put

\[
P_c(t)z=z+\nu\sum_{l=1}^m \xi_{j,l}q_l E_2[q_lz].
\tag{5}
\]

This is a bounded colored multiplicative perturbation of the readout
gradient. All parameters evolve continuously through those times; only
the mobility changes. Taking nu=0 gives the deterministic construction.
Neither (4) nor the proof requires a special distribution of the signs.

For L>0 in D, define

\[
\beta_\varepsilon(S)=
\frac{\varepsilon L
 [-\langle\nabla L,\nabla R\rangle]_+}
 {\|\nabla_c L\|_2^2},
\qquad [a]_+=\max(a,0).
\tag{6}
\]

The denominator is positive, since
||nabla_c L||^2=4 e^T K e>0. As R has no readout dependence and P_t is
the identity in its hidden blocks,
<nabla L,P_t nabla R>=<nabla L,nabla R>; no random term was dropped
from (6). At zero loss define beta=0 and stop at the fitted state.

The proposed continuous physical-time dynamics is

\[
\dot S=-P_t\nabla\Phi_\varepsilon(S)
       -\beta_\varepsilon(S)(0,\nabla_c L(S),0).
\tag{7}
\]

Equivalently, its blocks are

\[
\begin{split}
\dot w&=-(1+\varepsilon R)\nabla_w L-\varepsilon L\nabla_w R,\\
\dot M&=-(1+\varepsilon R)\nabla_M L-\varepsilon L\nabla_M R,\\
\dot c&=-(1+\varepsilon R)P_c(t)\nabla_c L
        -\beta_\varepsilon\nabla_c L.
\end{split}
\tag{8}
\]

All quantities are current-state functions or fixed initialization/data
information. The matrix differential
dR=-tr(K^{-2} dK) defines its derivatives explicitly. It can be
evaluated by the same finite Gram integrations and chain rule as the
original loss; no future path or unknown endpoint is used.

The beta term compensates only for a possible increase of L caused by
the hidden conditioning correction. Its purpose is to retain actual
loss monotonicity as well as potential decay.

## 3. Exact global inequalities inside D

Write k=lambda_min(K)>0. Since R>=1/k,

\[
k(1+\varepsilon R)\ge\varepsilon.
\tag{9}
\]

Also nabla_c Phi=(1+epsilon R)nabla_c L, whence

\[
\begin{split}
\|\nabla\Phi_\varepsilon\|^2
&\ge4(1+\varepsilon R)^2 e^TK e\\
&\ge4k(1+\varepsilon R)\Phi_\varepsilon
\ge4\varepsilon\Phi_\varepsilon.
\end{split}
\tag{10}
\]

This is an algebraic inequality for the explicitly constructed
potential on the entire positive-Gram domain. No uniform positive
lower bound on K along the trajectory is assumed.

Set q=<nabla L,nabla R>. Differentiation of the actual loss along (7)
and substitution of (6) give exactly, at positive loss,

\[
\begin{split}
\dot L
&=-(1+\varepsilon R)\langle\nabla L,P_t\nabla L\rangle
  -\varepsilon Lq-\varepsilon L[-q]_+\\
&=-(1+\varepsilon R)\langle\nabla L,P_t\nabla L\rangle
  -\varepsilon L[q]_+\\
&\le-4(1-\nu)k(1+\varepsilon R)L\\
&\le-4(1-\nu)\varepsilon L.
\end{split}
\tag{11}
\]

The readout descent correction also dissipates Phi, because its
readout gradient is a positive multiple of nabla_c L:

\[
\begin{split}
\dot\Phi_\varepsilon
&=-\langle\nabla\Phi_\varepsilon,
           P_t\nabla\Phi_\varepsilon\rangle
  -\beta_\varepsilon(1+\varepsilon R)\|\nabla_c L\|^2\\
&\le-(1-\nu)\|\nabla\Phi_\varepsilon\|^2\\
&\le-4(1-\nu)\varepsilon\Phi_\varepsilon.
\end{split}
\tag{12}
\]

Thus both L and Phi decrease for every mobility realization.
These are physical-time pathwise inequalities, not expectation-only
or accepted-stage statements.

## 4. Regularity, existence, possible singular endpoints, finite length

The whole-H loss is C1 with locally Lipschitz gradient, as proved in
ESCAPE_AND_LIMITS.md. The same property holds for K entries: a_i(w)
is C1 with Lipschitz derivative into its finite-dimensional target;
bounded phi'' controls the L2 Taylor remainder and differences of the
first derivative. Bounded b2 makes the remaining H_i maps smooth
finite-dimensional compositions. On every bounded state ball with
K>=k0 I, finite matrix inversion and its derivatives are bounded and
Lipschitz. Consequently R and Phi have locally Lipschitz gradients
there. This uses C1,1 regularity, not an invalid global C2 assertion
for L2 Nemytskii operators.

On L>0, beta is locally Lipschitz by its positive denominator.
Near a fixed zero-loss state in D, nabla L is linear in e with
state-dependent locally Lipschitz coefficients, while ||nabla_c L||^2
is a uniformly positive quadratic form in e. Therefore beta has
the form

  epsilon |e|^2 [-linear_in_e]_+ / quadratic_in_e.

For e!=0 this is homogeneous of degree one in e with a uniformly
Lipschitz angular factor on the unit sphere. Extending it by zero at
e=0 is locally Lipschitz: if two residuals have comparable norms,
use the angular Lipschitz bound; if not, its O(|e|) bound and the
reverse triangle inequality suffice. State-dependence of the
coefficients is locally Lipschitz. The correction beta nabla_c L
is therefore locally Lipschitz as well. Thus (7) has a unique
local solution in D on each interval of constant P_t, and the
piecewise process is uniquely determined before it leaves D.

We prove it cannot lose existence at positive loss or infinite norm.
Let D_t=-dot Phi>=0, a=1-nu, b=1+nu. Equations (10)--(12) give

\[
\|P_t\nabla\Phi\|
\le \frac{b}{a}\frac{D_t}{2\sqrt{\varepsilon\Phi}}.
\tag{13}
\]

Indeed D_t>=a||nabla Phi||^2 and
||nabla Phi||>=2sqrt(epsilon Phi). Furthermore,

\[
(1+\varepsilon R)\|\nabla_c L\|
\ge2\sqrt{\varepsilon\Phi}
\]

by the same readout estimate. The second dissipative term in (12)
therefore implies

\[
\beta\|\nabla_c L\|
\le \frac{D_t}{2\sqrt{\varepsilon\Phi}}.
\tag{14}
\]

Combining (13)--(14) and integrating yields the finite-travel bound

\[
\int_0^T\|\dot S\|\,dt
\le
\frac{b/a+1}{\sqrt\varepsilon}
\bigl(\sqrt{\Phi(S_0)}-\sqrt{\Phi(S_T)}\bigr)
\le\frac{b/a+1}{\sqrt\varepsilon}\sqrt{\Phi(S_0)}.
\tag{15}
\]

The same bound applies on any subinterval, with its endpoint values.
It supplies a strong Hilbert limit at every finite maximal endpoint:
monotonicity gives a limit of Phi, and the subinterval version of
(15) makes the state Cauchy. Finite-time norm blowup is impossible.

If the limiting Gram is positive, local existence continues the
solution. If its smallest eigenvalue is zero, R diverges, while
Phi=L(1+epsilon R)<=Phi(S0); continuity of L forces L=0 at the
limiting state. Define such a finite singular fitted endpoint to
be absorbing. No positive-loss singular boundary can be reached.
Set Phi=0 at an absorbing zero-loss singular endpoint; its potential
can then have a downward jump while the state and actual loss are
continuous. The positive-Gram formula need not have a continuous
extension there. This convention is explicit and is not used to
conceal a positive-loss termination.

This proves global existence and uniqueness for the stated process,
with the explicit absorbing convention if D is exited. If the
trajectory stays in D forever, (15) still gives finite total travel
and a strong endpoint as t tends to infinity. In both cases (11)
and continuity give zero loss at that endpoint.

## 5. Main theorem and the precise weak-perturbation limit

For every epsilon>0, every 0<=nu<1 and every admissible mobility
realization, from the declared initial state,

\[
L(t)\le L(0)e^{-4(1-\nu)\varepsilon t},\qquad
\Phi_\varepsilon(t)\le
\Phi_\varepsilon(0)e^{-4(1-\nu)\varepsilon t}.
\tag{16}
\]

The full state converges strongly to a finite fitted state. The rate
is in the physical clock of (7), which runs continuously; no separate
proposal-cost Delta or paused training phase exists.

Constants may depend on geometry through initial Phi, conditioning
forces, and the physical speed, even though the displayed rate in
this chosen clock is 4(1-nu)epsilon. In particular (8) multiplies
ordinary GF by 1+epsilon R and adds a conditioning force; a bad
Gram can make these changes large. This is a genuine optimizer
change, not a free geometry-independent rate for weak fixed noise.

Let S^0(t) be the unmodified exact gradient flow. Fix a finite T
such that its Gram is positive throughout [0,T]. Its continuous
path is compact, so lambda_min K has a positive minimum there,
and its norm is bounded. In a fixed neighborhood of this path,
the vector field (7) differs from -nabla L uniformly by at most
C_T(epsilon+nu), for 0<epsilon<=1 and 0<=nu<=1/2.

To see the only potentially nontrivial term, use

\[
\beta\le
\frac{\varepsilon\|\nabla L\|\|\nabla R\|}{4k_0}
\tag{17}
\]

on K>=k0 I, obtained from ||nabla_c L||^2>=4k0 L.
The state-bounded coefficients make beta nabla_c L uniformly O(epsilon).
The other differences are epsilon R nabla L, epsilon L nabla R,
and a mobility difference bounded by nu. All constants concern
this neighborhood, not a future-trained endpoint.

Use the ordinary GF Lipschitz constant C on that neighborhood.
Before any exit from it, integrating the difference equation gives

\[
\sup_{t\le T}\|S^{\varepsilon,\nu}(t)-S^0(t)\|
\le C_T'(\varepsilon+\nu).
\tag{18}
\]

For completeness, the elementary inequality
d(t)<=a t+C int_0^t d(s)ds implies
d(t)<=a (exp(Ct)-1)/C, with the Ct=0 case interpreted by continuity;
it follows by multiplying the integral inequality's scalar
majorant equation by exp(-Ct). Choose epsilon+nu small enough that
this bound is below the neighborhood radius; a first-exit argument
then makes the comparison valid on all [0,T]. The bound holds for
every mobility realization, so it is stronger than convergence in
probability on these horizons.

Equation (18) has an ESSENTIAL hypothesis. This study has not proved
that ordinary canonical GF keeps its readout Gram positive at every
finite time for arbitrary data. If its Gram reaches a singularity,
the proof does not give approximation beyond that time.
Pointwise convergence of vector fields away from the singular set
must not be upgraded to a global uniformly small perturbation claim.

As epsilon,nu tend to zero the original physical GF is recovered on
the stated regular horizons. The guaranteed long-time rate tends
to zero. No interchange of the small-correction and infinite-time
limits is made.

## 6. What survives and what does not

Proved by this candidate, subject to internal checking:

- Unconditional global fitting and exponential physical-time decay
  for the explicitly defined continuous corrected optimizer, at
  canonical p=1,2 on every finite compatible binary circle dataset.
- Monotone actual loss, monotone larger state potential, finite
  strong endpoint, and no imposed bound around initial hidden fields.
- Bounded colored random readout mobility can be included without
  weakening the pathwise proof beyond the factor 1-nu.
- Uniform finite-horizon closeness to original GF on every horizon
  where that original trajectory's Gram remains positive.

Not proved:

- The same conclusion for plain additive Brownian or minibatch noise.
- A globally uniformly small perturbation of the vector field.
- Approximation of ordinary GF past an unproved Gram singularity.
- Numerical complexity, a finite-width theorem, or practical
  efficiency of repeated Gram inversion and its derivative.

The mechanism is explicit conditioning regularization, not spontaneous
noise escape from every saddle. The regularization is essential to
this proof even when optional noise is present.

Scientific dependencies: ESCAPE_AND_LIMITS.md Section 1;
INITIAL_EXCLUSION.md and the supplied INITIAL_REVIEW.md Section 6;
the exact model definitions already derived from the canonical book.
All new differential inequalities, endpoint handling and comparison
arguments are supplied above. This file is a candidate until checked.
