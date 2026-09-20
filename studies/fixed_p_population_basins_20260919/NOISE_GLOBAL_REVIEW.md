# Independent review of the accepted-noise global arguments

2026-09-19. Isolated mathematical review. No simulation or author-file edits.

## Verdict and scope

**PASS for the stated claims.** I found no substantive mathematical gap in
the frozen arguments. In particular, the population closure admits the
claimed finite-data interpolation and the uniform hitting estimate on
bounded Hilbert balls. The original strict-decrease algorithm satisfies
the fitting-or-norm-escape dichotomy. Unconditional fitting is proved only
for the explicitly changed fractional-progress algorithm. The auxiliary
counterexample correctly disproves the corresponding abstract guarantee
for the original algorithm; it is not a counterexample in this closure.

This verdict is an independent internal check, not promotion or a proof
of unconditional convergence for the original canonical noisy trajectory.

The complete frozen research inputs read were:

* `NOISE_GLOBAL_PROGRESS.md`, SHA-256
  `70fc60f0554f54041c233d0f50f697e1cfab9a0dd834c8293470540818e11288`;
* `NOISE_OBSTRUCTION.md`, SHA-256
  `da873cefecd99390037fe41e855f8ffcfae54067587ea734338c62b5379c7be5`;
* `ESCAPE_AND_LIMITS.md`, SHA-256
  `544a5fde3b224cfa30539754c5d27123b900c12ed3fe5df98df00d5a8dd20ac2`.

The assigned established excerpts of `docs/global_nonlinear.md` were
read completely: lines 13161–13786 and 15146–15528, covering B/C.1/D.3.
Only their dictionary, carrier and exact-closure facts are needed here.
Their neural-limit identifications are not extended by this review.
The required `solve-math-rigorously` skill was read and applied. No
README, study history, other study, other review or unassigned scientific
input was read. Assertions in the frozen files referring to separate,
unassigned initialization calculations are not independent inputs to
this verdict.

## 1. Exact model, available marks and global flow

The model in the frozen files agrees with the established finite-order
closure, including the actual transpose, the unhalved weighted loss,
and the population L2/Frobenius metric. For orders 1, 2 and 3 the complete
raw feature lists are the polynomial lists specified in B. Their features
are bounded, their normalizing Cholesky factors are invertible, and the
lower list contains 1 while the upper list contains
`X = tanh(xi_1)`.

More explicitly, if `e_0` and `e_X` select these raw features, then
`l = L_1^T e_0` and `e = L_2^T e_X` satisfy
`b_1^T l = 1` and `b_2^T e = X`. The established law gives
`xi_1 ~ N(0,v)` with `v>0`, so X has positive density throughout
`(-1,1)`. The lower marks retain `g_1`, a standard Gaussian, permitting
partitions with any prescribed finite collection of positive masses.
These are facts about the complete canonical mark laws, not replacement
initializations.

The all-Hilbert-space extension in `ESCAPE_AND_LIMITS.md` §1 is valid.
On a bounded state ball, the lower expectation is Lipschitz in w; the
upper preactivations are bounded and Lipschitz in L-infinity; and the
backward fields q are bounded and Lipschitz in L-infinity. Multiplying
q by the L2-Lipschitz lower gate gives a locally Lipschitz row velocity.
The readout and matrix velocities obey the same conclusion. The stated
quadratic remainder for the lower expectation proves its Fréchet
differentiability. Combining it with the finite-dimensional upper
preactivation map and the bounded readout pairing proves that the loss
is C1 with the stated gradient.

Consequently the energy identity holds in this metric. With
`R = sqrt(L(S_0))`, the three displayed speed bounds first control c
linearly, then M quadratically, then w on every finite interval. The
vector field is uniformly bounded and Lipschitz on every bounded ball,
so a solution approaching a finite maximal time is Cauchy and can be
continued. This justifies arbitrary finite flow intervals after accepted
Gaussian perturbations, even when the perturbed fields are only L2.
It does not require, or establish, C2 regularity in the Hilbert topology.

## 2. Interpolation for every compatible finite circle dataset

`NOISE_GLOBAL_PROGRESS.md` §2 is correct without a sample-count bound
or an initial-feature independence assumption.

The prediction is odd in the input at every state. Identical inputs may
therefore be merged by adding their masses. An antipodal sample may
be changed to the chosen representative with its label negated; both
its prediction and label change sign, preserving its squared residual.
Compatibility makes each resulting label well defined. The reduced
directions are distinct modulo sign.

For any two such directions, there are open sets of v giving equal
signs and open sets giving opposite signs. Finitely many witnesses can
avoid every input's orthogonality directions simultaneously. Thus the
resulting sign vectors are nonzero and pairwise distinct modulo sign.
Each forbidden equation

\[
\sum_j\alpha_j\sigma_i(v_j)=0,
\qquad
\sum_j\alpha_j\bigl(\sigma_i(v_j)\pm\sigma_k(v_j)\bigr)=0
\]

is a proper affine condition on the simplex. A linear form vanishing
on the entire simplex vanishes at every vertex and has all coefficients
zero; the sign-vector construction excludes that possibility. The
relative interior therefore contains masses avoiding all the finitely
many conditions. This includes the one-sample case.

For distinct nonzero slopes modulo sign, the functions `tanh(s_i X)`
are linearly independent in the actual upper L2 space. Positive density
and continuity turn an almost-sure relation into an identity on
`(-1,1)`, and real analyticity extends it along the real line. After
absorbing slope signs, write the positive slopes in increasing order.
The limit at positive infinity makes the coefficient sum zero. Subtract
that constant relation and multiply by the exponential associated with
the smallest slope: only its coefficient survives in the limit, with
factor -2. Removing it and iterating proves independence. No assertion
that X itself has unbounded support is used in this analytic argument.

The fields `w_T = T v` are bounded and hence belong to the required
lower L2 space. The choice `M_* = e l^T` gives exactly the scalar
preactivation `X s_i(T)`. At a sufficiently large finite T the finite
collection of nonzero/distinct-modulo-sign conditions persists. The
Gram matrix is then positive definite, and the displayed readout
`c_T = sum_j (K(T)^(-1)y)_j H_j(T)` lies in L2 and interpolates every
reduced target. Restoring merged samples preserves zero loss.

This is an exact represented state of the full population closure.
It is neither an assertion that deterministic canonical flow reaches
that state nor a finite-particle interpolation theorem. In particular,
no canonical parity restriction is imposed on this state: the declared
full-support noise is allowed to perturb all coordinates of H.

## 3. Uniform hitting from bounded Hilbert balls

The distinction between compact controls and noncompact states in §3
is valid and essential. The controls

\[
h(S)=(Tv,\ h_c(c),\ M_*-M)
\]

have one fixed row field, a bounded readout correction in the fixed
finite-dimensional span of the ideal upper features, and a bounded
finite-dimensional matrix component. Their closure is compact even
though the current states and their row fields need not be precompact.
The proof never tries to choose the noncompact controls `-w` or `-c`.

For `m = min_{i,j}|v_j dot u_i|>0` and `||w_tilde||_2 <= R+1`, the
bad set has probability at most `4(R+1)^2/(T^2 m^2)`. On its complement,
every lower argument has its prescribed sign and magnitude at least
`Tm/2`. The pointwise tanh error there is at most `2 exp(-Tm)`; on
the bad set it is at most 2. This gives exactly the stated bound

\[
d_T=2e^{-Tm}+\frac{8(R+1)^2}{T^2m^2}.
\]

The special matrix converts this unweighted lower expectation directly
to `X` times that expectation, since `b_1^T l=1`. A matrix perturbation
of Frobenius norm at most r contributes at most `B_1 B_2 r` in upper
L-infinity. The actual upper feature error is consequently at most
`d_T+B_1 B_2 r`. Pairing it with `c+h_c(c)` and bounding the separate
readout perturbation gives the displayed residual estimate

\[
|f_i-y_i|\le C_R(d_T+B_1B_2r)+r.
\]

Choose T first and r second, uniformly in the bounded state ball.
The probability weights summing to one then give loss below the target.
A finite cover of the compact control closure supplies finitely many
open proposal balls, each of positive mass by full support. Their
minimum mass is strictly positive. This proves (6) with no compactness
assumption on the population states and no Cameron–Martin assumption
on individual control centers.

The result uses the fixed full-support proposal law. It supplies no
lower bound uniform in R, target loss, noise scale or data geometry.
The stated extension to other full-support additive laws is valid;
conditioning proposals to a fixed norm ball removes the needed support
and is not covered.

## 4. Original strict-decrease acceptance

The conditional-probability proof in §4 is valid. At every proposal
time whose state has norm at most R and loss at least a, the event of
landing below `a/2` has conditional probability at least `q(R,a/2)`.
It is accepted, and later flow preserves the lower loss. Conditioning
successively at the visit times bounds avoidance through N visits by
`(1-q)^N`. Thus infinitely many bounded visits on `L_infinity >= a`
have probability zero. Taking the stated countable union gives

\[
\mathbb P\{L_\infty>0,\ \liminf_k\|S_k\|_H<\infty\}=0.
\]

Its reformulation as fitting or `||S_k||_H -> infinity` is exact: a
nonnegative norm sequence with no infinitely recurring finite ball
tends to infinity. It is stronger than merely excluding precompact
positive-loss trajectories. The alternatives need not be disjoint.

The tightness corollary also checks out. If
`P(L_infinity >= a)=s>0`, uniform tightness on a deterministic infinite
subsequence gives a radius R at which the bounded/high-loss event has
probability at least `s/2` at every selected time. The probability of
a crossing from at least a to below `a/2` is then at least `qs/2` at
each selected time. These crossing events are pairwise disjoint because
loss is nonincreasing, contradicting countable additivity.

As usual, proposal states and optional flow durations are understood
to be measurable and nonanticipating, and the claims concern an
infinite sequence of proposal opportunities. These conventions are
already implicit in the independent fresh-draw algorithm. No argument
here establishes bounded recurrence, tightness or exclusion of positive
loss norm escape from canonical initialization.

## 5. Fractional-progress acceptance

The theorem in §5 is correct for states in H with its declared fixed
full-support Gaussian law. At a positive-loss stage, after any stated
finite flow interval, the held state T and stage threshold are fixed
conditional on the stage history. Continuity and the zero-loss witness
give an open set of increments with loss below `theta ell`, hence
a positive conditional success probability p. Independent repeated
proposals from that unchanged T yield precisely the geometric waiting
tail and conditional mean in (14).

Induction and a countable intersection give almost-sure completion of
every finite stage unless zero was reached earlier. Every completion
multiplies loss by at most theta, proving (13). For each fixed positive
accuracy only finitely many stages are needed; their almost-surely
finite proposal counts and finite flow durations sum to a finite total.
Rejected candidates do not change the accepted-state loss.

Holding T fixed and rejecting smaller-than-required improvements are
both used in this proof. Allowing such improvements, or continuing
flow during unsuccessful trials, invalidates the fixed geometric
waiting-time argument without additional estimates. Geometric decay
per completed stage does not provide a deterministic rate in proposals
or physical time, or a bound on unconditional expected waiting time.
The proof uses unbounded full support and gives no corresponding
guarantee for norm-bounded small perturbations. Gaussianity itself is
not otherwise essential. The stated generalization to a continuous
loss of infimum zero is valid using an approximate minimizer.

## 6. Explicit obstruction for the original rule

All derivative, landscape and flow claims for

\[
r(x)=1+(x-1)e^{-x},\qquad L(x)=r(x)^2
\]

check directly. The only stationary points are the zero minimum at 0
and the strict maximum at 2; on `(2,infinity)` loss decreases to 1 and
gradient flow increases x. The vector field is bounded on that branch.
On the other branches the flow stays in the bounded interval between
its initial point and the relevant stationary boundary, so it is
globally defined there as well.

The positive-probability argument in `NOISE_OBSTRUCTION.md` is valid,
not merely a deterministic escape-path argument. With
`R_k=x_0+sum_{j<=k} xi_j^+`, independence gives

\[
\mathbb P(\xi_{k+1}\le2-R_k)
\le e^{-\lambda(x_0-2)+\lambda^2\tau^2/2}
       \bigl(\mathbb E e^{-\lambda\xi_1^+}\bigr)^k.
\]

Here `0<q=E exp(-lambda xi_1^+)<1`. A union bound therefore gives the
claimed positive lower bound on avoiding all branch-crossing proposals
once x_0 satisfies (6). On this event all positive proposals are accepted,
all negative proposals are rejected, and every finite nonnegative flow
interval can only increase the comparison margin. Independent positive
increments above a fixed threshold occur infinitely often, so R_k and
the actual states tend to infinity. Loss consequently tends to 1.

From an arbitrary `x_0>2`, one sufficiently large positive first proposal
has positive probability and reaches a region with a uniform positive
lower bound for the subsequent escape event. This proves the claimed
extension to every starting point on that branch. For conditioned
bounded proposals and `x_0>2+epsilon`, the branch is invariant for every
realization and the same positive-increment argument gives escape
almost surely.

The Hilbert-space embedding is also valid. Full support gives positive
variance in any nonzero scalar direction; acceptance depends only on
that scalar coordinate, irrespective of correlations with orthogonal
coordinates. Under norm conditioning, a small ball around a positive
multiple of that direction gives the required positive-increment
probability. The example disproves the abstract convergence implication
despite having no positive-loss local minima. Nothing in it realizes
that scalar loss inside the canonical population closure.

## 7. Remaining supporting claims and limits

The other supporting arguments in `ESCAPE_AND_LIMITS.md` are consistent:
the square-loss example `(1+s^3)^2` has an open one-sided basin tending
to the nonminimum at zero; the transverse second variation has the
stated factor `4 alpha B`; `(w,0,0)` is an exact per-sample stationary
state; and the displayed choice of k and middle direction gives negative
curvature when its stated vector v is nonzero. Positive definiteness of
the upper feature Gram at orders 1–3 follows from polynomial independence
on the open support and invertible normalization.

The stationary identity follows by pairing the readout stationarity
equation with c: `sum mu_i r_i f_i=0`, whence
`L=sum mu_i y_i^2-sum mu_i f_i^2`. The strict-initial-descent formula
and its exclusion of stationary loss-one limits follow with the
unhalved-loss factor 4. They do not exclude lower positive plateaus.

The countable-cover argument for simultaneous exclusion of nonglobal
accumulation states under full-support accepted noise is sound. Each
selected neighborhood offers a fixed positive probability of a fixed
loss drop at each visit; infinitely many visits would force infinitely
many such drops, contradicting nonnegative loss. A countable subcover
exists because H is separable. The conditioned local-noise version
correctly excludes only non-local-minima without a separate landscape
assumption. Neither statement supplies recurrence. The cautions about
uncountable unions of null basins, deterministic canonical initialization,
and lack of infinite-dimensional Lebesgue probability are appropriate.

No amendment is needed for the mathematical conclusions as scoped.
The unresolved obligation for the original rule remains exactly the
one stated in the frozen progress note: exclude positive-loss norm
escape in this closure, or control effective descent probabilities
along such escape trajectories. The modified acceptance theorem does
not discharge that obligation for the original algorithm, ordinary
gradient flow, minibatch SGD, or norm-bounded infinitesimal noise.
