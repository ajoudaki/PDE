# Escape, basins, and the scope of a landscape result

2026-09-19. Internally derived results; not promoted.

## 1. Exact population system and topology

Scientific inputs: established global_nonlinear.md C.4.7.10.B, C.1, D.3.
Fix one canonical order p=1,2,3 and its complete initialized joint mark
laws. The bounded columns b1,b2 and their normalization remain fixed.
The following arguments in fact use only bounded marks. Write
phi=tanh, and let the finite training law have masses mu_i>0 summing to
one, inputs x_i in sqrt(2) S1 and labels y_i. All equations use physical
time and the unhalved square loss. Define

\[
\begin{split}
a_i&=E_1[b_1\phi(w\cdot x_i/\sqrt2)],&
z_i&=b_2^TMa_i,&H_i&=\phi(z_i),\\
f_i&=E_2[cH_i],&r_i&=f_i-y_i,&
d_i&=E_2[b_2c\phi'(z_i)],\\
q_i&=b_1^TM^Td_i,&
L&=\sum_i\mu_i r_i^2.
\end{split}
\]

The exact state space used here is the separable real Hilbert space

\[
\mathcal H=L^2(\lambda_1;\mathbb R^2)\oplus
 L^2(\lambda_2)\oplus\mathbb R^{d_2\times d_1},
\]

with its population L2 and Frobenius metric. The fixed Gaussian mark
spaces are standard probability spaces, so these L2 spaces are separable.
States are fields on the fixed carrier; no additional randomness of the
carrier or reinitialization of its marks is implicit. Its exact flow is

\[
\begin{split}
\dot w&=-2\sum_i\mu_i r_i\phi'(w\cdot x_i/\sqrt2)q_i x_i/\sqrt2,\\
\dot c&=-2\sum_i\mu_i r_iH_i,\\
\dot M&=-2\sum_i\mu_i r_i d_i a_i^T.
\end{split} \tag{1}
\]

The transpose is the actual transpose. Canonical initialization is
(g,0,D), where D and the full joint laws are exactly those in the source.

For completeness (1) is locally Lipschitz on this whole Hilbert space,
not just on bounded-field charts. Put B_l=ess sup |b_l|. On a bounded
Hilbert ball, a_i is bounded and Lipschitz in w, and z_i is bounded and
Lipschitz into L-infinity. Thus H_i and phi'(z_i) are bounded and
Lipschitz into L-infinity. Cauchy--Schwarz shows that f_i,d_i are locally
Lipschitz in all states; q_i is locally Lipschitz into L-infinity.
Finally phi'(w dot x_i/sqrt2) is Lipschitz into L2, and multiplying it
by the bounded q_i proves the assertion for the first equation. The
other equations follow from their finite products.

The loss is C1 with locally Lipschitz gradient -F, where F is (1).
For example the Taylor remainder for a_i is at most
C E|delta w|^2 because phi'' is bounded; its derivative is the displayed
expectation of b1 phi' times delta w dot x_i/sqrt2. The remaining maps
are finite-dimensional smooth maps and bounded linear pairings.
Consequently every solution satisfies

\[
\dot L=-\|\dot w\|_2^2-\|\dot c\|_2^2-\|\dot M\|_F^2. \tag{2}
\]

This also gives all-finite-time continuation from every state in H.
Let R=sqrt(L(0)). Since sum mu_i |r_i|<=R,

\[
\begin{split}
\|\dot c\|_2&\le2R,\\
\|\dot M\|_F&\le2R B_1B_2\|c\|_2,\\
\|\dot w\|_2&\le2R B_1B_2\|M\|_F\|c\|_2.
\end{split}
\]

Successive integration bounds c,M,w on every finite interval. The
vector field is bounded and Lipschitz on the resulting bounded balls,
so a finite endpoint is Cauchy and the local solution continues.
This extension is a direct consequence of the finite fixed dictionary;
it is not a claim about the full unclosed neural limit.

One must not strengthen this regularity silently to C2 loss on H.
For example h -> phi'(w+h) need not be Frechet differentiable L2->L2:
fixed-amplitude perturbations on sets of shrinking positive measure
need not have a Taylor remainder that is little-o of their L2 norm.
Directional second variations below are justified along bounded
directions. A population stable-manifold assertion needs its own proof.

## 2. What nearby descent alone proves, and what it does not

Let S_* be an equilibrium and ell=L(S_*). Every trajectory converging
to S_* has L(S(0))>=ell. More generally a trajectory whose loss has
already dropped below ell cannot approach any set on which the loss
equals ell. This follows from (2) and continuity of L.

If every neighborhood of S_* contains a point of loss below ell, S_*
cannot attract an entire neighborhood. However its basin can still
have nonempty interior. An exact analytic, nonnegative square-loss
counterexample is

\[
V(s)=(1+s^3)^2,\qquad
\dot s=-6s^2(1+s^3).
\tag{3}
\]

For every s(0)>0 the solution remains positive, decreases, and tends to
zero: any positive limiting value would give a speed bounded away
from zero. It cannot hit zero at finite time by local uniqueness.
Hence V tends to 1 from above for an open half-line of initial states,
although all sufficiently small negative s have V(s)<1.
Adding sum_j t_j^2 gives an open positive-volume basin in every finite
dimension. This is an abstract gradient-flow counterexample, NOT a
realization in the canonical closure.

Likewise, a statement that each equilibrium separately has a null
basin does not prove that the union of all bad basins is null.
An uncountable union of null sets need not be null.

There is no infinite-dimensional Lebesgue probability measure on H.
A measure claim must specify a random-state law or a finite-dimensional
conditional distribution. The canonical population initial state is
the deterministic triple (g,0,D). Its Gaussian marks do not constitute
a random draw of that triple from a distribution on H. Nullity under
an unrelated state-perturbation law cannot exclude this particular point.

## 3. An exact transverse-curvature test

Write theta=(w,M), and fix a stationary state with bounded c; use
bounded field perturbations below. Let

\[
\mathcal V=\operatorname{span}\{H_1,\ldots,H_n\}\subset L^2(\lambda_2).
\]

Choose k perpendicular to V, and a hidden direction v=(v_w,v_M).
Define

\[
\begin{split}
\delta a_i&=E_1[b_1\phi'(w\cdot x_i/\sqrt2)
                          (v_w\cdot x_i/\sqrt2)],\\
\delta H_i&=\phi'(z_i)b_2^T(v_Ma_i+M\delta a_i),\\
B(k,v)&=\sum_i\mu_i r_i E_2[k\,\delta H_i].
\end{split} \tag{4}
\]

Along the two-block line (theta+t v,c+t alpha k), the exact second
variation is

\[
\frac{d^2}{dt^2}L\big|_{t=0}=A(v)+4\alpha B(k,v), \tag{5}
\]

where A(v) is the second variation with c fixed. Indeed the first
output variation is E[c delta H_i]+alpha E[kH_i]; its second term
vanishes. The second output variation is
E[c delta^2 H_i]+2alpha E[k delta H_i]. Differentiating r_i^2 gives
(5). All derivatives are dominated on these bounded directions.

If B(k,v) is nonzero, choosing alpha with the appropriate sign and
large enough finite magnitude proves a negative second variation.
If the projection of sum_i mu_i r_i delta H_i onto V-perp is nonzero,
it supplies such a bounded k: delta H_i and H_i are bounded, and the
orthogonal projection subtracts only a finite linear combination.
This test uses the interaction of both hidden layers and the readout.
It identifies a genuine quadratic instability certificate; by itself
it does not prove a global basin measure theorem.

## 4. Exact equilibria at which minibatch noise is identically zero

For every w, the state (w,0,0) is stationary. Its predictor is zero
and its loss is sum_i mu_i y_i^2 (one for binary labels). More strongly,
each individual sample gradient is zero: a_i can be nonzero but
H_i=d_i=q_i=0. Thus every minibatch, of any size and with any sampling
law, leaves this state exactly fixed.

Many of these states nevertheless have negative curvature. Put

\[
v=\sum_i\mu_i y_i a_i.
\]

If v is nonzero, (4) at (w,0,0) with a middle direction A gives

\[
B(k,(0,A))=-E_2[b_2k]^T A v. \tag{6}
\]

For canonical orders 1,2,3, G=E_2[b_2b_2^T] is positive definite.
Indeed the raw polynomials are independent on an open cube of
positive density and the normalization is invertible. Choose any
e!=0, k=b_2^T e, and A=(Ge)v^T. Then (6) equals
-|Ge|^2 |v|^2<0. Equation (5) proves negative curvature.

This is an actual closure example where strict saddle geometry and
vanishing minibatch noise coexist. It disproves the assertion that
sampling automatically supplies an escape kick at every bad state.
It does not prove convergence to these states from a noisy or
canonical initial trajectory.

If the initial readout feature sum
R_0=sum_i mu_i y_i H_i(g,D) is nonzero, then

\[
\dot L(0)=-4\|R_0\|_2^2<0. \tag{7}
\]

All states with loss one are then excluded as limiting states of the
canonical trajectory. A separate direct initialization calculation in
this study checks when R_0 is nonzero; (7) alone is only the exact
criterion. Excluding the level one does not exclude lower positive
plateaus.

There is also an exact constraint on every stationary state. Taking
the inner product of dot c=0 with c gives sum_i mu_i r_i f_i=0.
Consequently

\[
L(S_*)=\sum_i\mu_i y_i^2-\sum_i\mu_i f_i(S_*)^2. \tag{7a}
\]

For binary labels, a stationary state has loss one if and only if its
predictor is zero at every data point. Therefore strict initial descent
excludes the entire zero-predictor stationary set, not just the explicit
collapsed examples. Every possible remaining positive-loss stationary
limit must already make a nonzero prediction and have loss strictly
between zero and one.

## 5. Persistent small perturbations turn nearby descent into escape

The result in this section is for an EXPLICITLY MODIFIED algorithm,
not ordinary gradient flow or SGD. Fix any sigma>0. Let Z_k be iid
centered Gaussian random elements of H with a covariance diagonal
in some orthonormal basis, with strictly positive summable eigenvalues.
Use proposals sigma Z_k. Accept a proposal only if it decreases the
actual full loss. Between successive proposals one may run any fixed
nonnegative duration of the exact flow (1). Let S_k denote the state
immediately before proposal k. The entire sequence has nonincreasing
loss. The Gaussian is one declared source of fresh noise and is
independent of the state and all past draws.

Every open H-ball of perturbations has positive probability. To prove
this, approximate its center by its first m basis coordinates. The
finite Gaussian projection has an everywhere positive density.
Choose m so large that the mean squared Gaussian tail is small
compared with the ball radius squared; Markov's inequality gives
positive probability of a sufficiently small tail. Independence
multiplies these two positive probabilities. Scaling by any fixed
sigma>0 preserves this property. This does not assert a lower bound
uniform in sigma, state, or witness distance.

**Local escape.** Suppose S_* has a point T, as near as desired, with
L(T)<L(S_*). By continuity there are open balls U about S_* and W
about T-S_* and a number delta>0 such that

\[
L(S+h)\le L(S)-\delta\qquad(S\in U,\ h\in W).
\tag{8}
\]

One can also shrink U and W so that accepted points in (8) have loss
strictly below inf_{S in U} L(S), and hence leave U. If
q=P(sigma Z_k in W)>0, the conditional probability of staying in U
through N further attempts, starting in U, is at most (1-q)^N.
Other accepted moves or the intervening flow may cause earlier exit.
Once the loss is below L(S_*), monotonicity prevents convergence back
to S_*. Arbitrarily small fixed sigma is sufficient; the waiting-time
bound 1/q can be arbitrarily large.

**Simultaneous exclusion of all non-minimal accumulation states.**
No prescribed endpoint or countable-equilibrium assumption is needed.
For every state that has a strictly lower-loss point, construction
(8) supplies an open U. In particular it supplies one for every
non-local-minimum. A countable subcover can be chosen from any such
family: a separable metric space has a countable basis, and each
covered point lies in a basis ball contained in a member of the
cover; choose one cover member per basis ball.

Fix one selected U and its delta,q. It cannot be visited infinitely
often almost surely. Indeed at each successive visit the fresh noise
has conditional probability at least q of decreasing loss by delta.
For any block of N visits the probability of no such success is at
most (1-q)^N, by repeated conditioning, including at the visit stopping
times. Therefore on infinitely many visits there are infinitely many
successes almost surely. This contradicts L>=0 and monotonicity,
which permit at most floor(L(S_0)/delta) successes. A countable union
of the resulting probability-zero exceptions still has probability zero.
If an accumulation point belonged to one of these open U, that U
would be visited infinitely often. Hence almost surely every
accumulation point of S_k is a local minimum (in fact, because this
Gaussian permits large jumps too, a global minimum).

For the more specifically local version, replace the Gaussian by its
conditioning on ||sigma Z||<epsilon, for an arbitrary fixed epsilon>0.
Its support is the closed epsilon-ball and it gives positive
probability to every open ball inside. At a non-local-minimum choose
T with ||T-S_*||<epsilon/2. The same proof excludes every non-local-
minimum accumulation point. It makes no global-minimum claim unless
the landscape separately has no bad local minima.

Consequences requiring distinct hypotheses:

* Unconditionally for this modified algorithm, the probability of
  point convergence to ANY non-local-minimum is zero.
* If every positive-loss state is not a local minimum, then no
  positive-loss accumulation state exists almost surely.
* If, in addition, the proposal-time trajectory is precompact, then
  L(S_k)->0 almost surely: it has an accumulation point, whose loss
  is the limit of the monotone losses and must be zero.

The second premise is the mathematical landscape property proposed
in the user's question. It is used here as an explicitly stated
abstract hypothesis, not imported from another study. The third
premise has not been proved for the canonical closure. Neither
finite-time energy bounds nor boundedness in H implies precompactness.
Thus no unconditional claim of fitting by the perturbed algorithm
is made.

If noise amplitudes decrease to zero, the witness probabilities may
be summable. The argument then fails. A sufficient replacement is a
divergent sum of the conditional witness probabilities along visits;
“infinitesimal noise” without a persistence condition is insufficient.
Ordinary additive stochastic steps can increase loss, so they do not
satisfy this accept-only proof. Minibatch noise need not have the
support used in (8), as Section 4 demonstrates exactly.

## 6. Current logical outcome

Nearby descent rules out neighborhood attraction but not positive
basin volume. The closure supplies explicit coupled negative-curvature
tests and an exact obstruction to universal SGD escape. Persistent,
loss-tested small noise gives a simultaneous almost-sure exclusion
of convergence to all non-local-minima. These are different results.

For the original deterministic canonical closure, universal nullity
of bad basins, existence of an ambient open bad basin, and convergence
to zero loss remain unresolved here. The further local cone analysis
and initialization calculations are recorded in this study's separate
files and must be read with their precise scopes.
