# Consolidated results: basins, saturation, and accepted noise

2026-09-19. Consolidation of the current study, without new proof claims,
experiments, or promotion. The earlier proof files and original review
reports remain the authorities. "Proved" here means checked within this
study, not incorporated into established material.

## Common scope

These results concern the exact canonical population closure on the
normalized input circle, with complete frozen joint marks, dictionary
normalization, actual transpose, physical population L2/Frobenius metric,
and unhalved probability-weighted square loss. State notation is
S=(w,c,M) on the fixed mark carriers; its norm is the physical Hilbert norm.

Unless a narrower scope is stated, the order is p=1,2,3 and the data are
any finite collection of circle inputs with positive weights summing to
one and binary labels. Compatibility means that repeated inputs have
equal labels and antipodal inputs have opposite labels. No linear
independence, class balance, minimum separation, or sample-count bound is
required for the universal-data results below.

This document consolidates this study's basin/noise investigation. It
does not import earlier studies' unpromoted landscape or potential proofs.

## 1. Every compatible finite dataset has an attained zero-loss state

For each dataset and each p=1,2,3, there exists a finite-norm population
state with L=0. Thus compatibility is sufficient, as well as necessary,
for exact fitting in this full state space.

The construction uses lower fields taking finitely many directions,
the constant lower dictionary coordinate, and one upper Gaussian-derived
coordinate. The resulting scalar tanh features are linearly independent;
a finite Gram solve constructs the readout. This is a state-existence
theorem, not a trajectory theorem or a changed canonical initialization.

Proof: [NOISE_GLOBAL_PROGRESS.md](NOISE_GLOBAL_PROGRESS.md), Section 2.
Check: [NOISE_GLOBAL_REVIEW.md](NOISE_GLOBAL_REVIEW.md).

## 2. Canonical deterministic training always starts learning

For p=1 and p=2, every compatible finite circle dataset has

\[
L(0)=1,\qquad L'(0)<0,\qquad L(t)<1\quad(t>0).
\]

After any fixed positive time, monotonicity preserves a strict gap below
one. In particular, the canonical trajectory cannot approach zero
training predictions or any loss-one stationary state, even along a
subsequence.

This retains all initialization correlations and each order's prescribed
ridge. It proves neither a geometry-uniform initial rate nor zero limiting
loss. The corresponding universal initial-descent statement at p=3 is
not claimed here.

Proof: [INITIAL_EXCLUSION.md](INITIAL_EXCLUSION.md).
Check and separately verified p=1 extension:
[INITIAL_REVIEW.md](INITIAL_REVIEW.md).

## 3. Specific bad equilibria have rigorously thin deterministic basins

For the explicit collapsed families and the more general stationary
states with vanishing individual backward fields q_i and a negative
second variation, the local set of trajectories staying nearby lies in
a Lipschitz graph missing at least one unstable direction.

Consequently it has measure zero under conditional densities along
those finite-dimensional unstable directions. The global sets of states
strongly converging to the specified equilibria or families are meagre
in the physical Hilbert topology.

A genuine three-input construction, with distinct non-antipodal inputs,
equal weights and labels (+,-,+), has stationary predictions (0,0,1),
loss 2/3, and the required negative curvature. It lies inside the
canonical parity subsystem.

These are not universal bad-basin-nullity claims. Meagre is a topological
notion, not Gaussian measure zero; canonical reachability of the example
is unproved.

Proofs: [CLOSURE_ROUTE.md](CLOSURE_ROUTE.md),
[PARTIALLY_FITTED_SADDLE.md](PARTIALLY_FITTED_SADDLE.md).
Check: [ESCAPE_REVIEW.md](ESCAPE_REVIEW.md).

## 4. Saturation at infinity is an actual obstruction to uniform progress

For an explicit compatible, balanced three-input law, there are exact
closure states S_R with

\[
L(S_R)=\frac34+\frac1R,\qquad
\|\nabla L(S_R)\|_{\mathcal H}\longrightarrow0,\qquad
\|w_R\|_2=R\longrightarrow\infty,
\]

while c_R and M_R stay bounded. Expected accepted improvement from any
fixed additive proposal law tends to zero. The maximum improvement over
any fixed-radius perturbation ball also tends to zero.

Thus finite-state saddle analysis alone cannot settle all asymptotic
behavior, and loss bounds do not control the population norm. The
mechanism is first-layer saturation and collision of training features.
This is a sequence of states, not a realized deterministic or stochastic
trajectory, and does not prove a positive-loss plateau from canonical
initialization.

Proof: [NOISE_CLOSURE_ROUTE.md](NOISE_CLOSURE_ROUTE.md), Sections 2--3.
Check: [NOISE_SATURATION_REVIEW.md](NOISE_SATURATION_REVIEW.md).

## 5. Original accepted full-support noise: fitting or norm escape

Draw independent increments from a fixed full-support Hilbert-valued
Gaussian and accept every strict decrease of full loss. Finite exact
gradient-flow intervals may intervene. For every compatible dataset,

\[
\Pr\!\left\{L_\infty>0\ \text{and}\
\liminf_k\|S_k\|_{\mathcal H}<\infty\right\}=0.
\]

Therefore positive limiting loss forces the norm to tend to infinity
almost surely. Infinitely many visits to some bounded ball suffice for
fitting; strong precompactness is unnecessary. Uniform norm tightness
along a deterministic infinite subsequence also suffices.

The closure-specific mechanism is a uniformly positive chance to propose
loss below any prescribed positive threshold while the state norm stays
in a fixed bounded ball. The controls form a compact family even though
the population ball is not compact.

Recurrence from canonical initialization is not proved. Full support
is essential to this proof; the result is not stated for uniformly
bounded perturbations or minibatch SGD.

Proof: [NOISE_GLOBAL_PROGRESS.md](NOISE_GLOBAL_PROGRESS.md), Sections 3--4.
Check: [NOISE_GLOBAL_REVIEW.md](NOISE_GLOBAL_REVIEW.md).

## 6. Modified acceptance: unconditional almost-sure fitting

Keep the same fixed full-support Gaussian law. Fix 0<theta<1. At each
positive-loss stage, hold the state fixed during unsuccessful trials and
accept only a proposal reducing loss by a factor at most theta. Optional
finite exact-GF intervals can be taken before the trial loop.

Every stage completes after finitely many proposals almost surely, and

\[
L_J\le\theta^J L_0.
\]

With continuing trials at fixed finite time intervals during each waiting
loop and finite stated GF intervals, every positive accuracy is reached
in finite elapsed algorithm time almost surely. Hence L(t) tends to zero
almost surely. This holds from every state in the physical Hilbert space,
including canonical initialization, without a recurrence, boundedness,
or parameter-convergence assumption.

The guarantee is geometric per completed stage, not per proposal or
unit of physical GF time. No uniform time rate or finite unconditional
expected hitting time is proved. Rare large Gaussian draws may be
essential. This is an eventual global-search guarantee for the modified
algorithm; it does not establish zero-loss convergence for autonomous GF,
SGD, or bounded infinitesimal noise.

Proof: [NOISE_GLOBAL_PROGRESS.md](NOISE_GLOBAL_PROGRESS.md), Section 5.
Check: [NOISE_GLOBAL_REVIEW.md](NOISE_GLOBAL_REVIEW.md).

## Supporting exclusions and supersession

- Nearby lower loss, even a cubic descent direction, does not by itself
  imply a null deterministic basin. Abstract analytic squared-loss
  counterexamples establish this limitation; they are not closure basins.
- Minibatch sampling does not automatically supply escape noise: at
  (w,0,0) every sample gradient vanishes, including at many strict
  saddles of the actual closure.
- Even absence of bad local minima does not alone imply global fitting
  under the original accepted Gaussian rule: an auxiliary analytic scalar
  squared-loss example has positive-probability escape to infinity with
  positive limiting loss. It is not a closure trajectory counterexample.

Sources: [ESCAPE_AND_LIMITS.md](ESCAPE_AND_LIMITS.md),
[HARMONIC_ROUTE.md](HARMONIC_ROUTE.md),
[NOISE_OBSTRUCTION.md](NOISE_OBSTRUCTION.md).

For the original full-support rule, result 5 supersedes the earlier
precompactness-based fitting consequence and makes the local accumulation
theorem a supporting result. Result 6 does not supersede result 5:
it changes the acceptance rule. The bounded-radius local-noise theorem
also remains a distinct, narrower-support result.

## What remains open

For canonical autonomous gradient flow: zero limiting loss for every
compatible finite dataset, universal bad-basin classification, and a
general exponentially decaying potential in physical GF time.

For the original accept-every-improvement Gaussian process: whether
positive-loss norm escape can occur from canonical initialization.

The modified acceptance theorem settles eventual fitting for its own
algorithm. It leaves practical waiting-time estimates and purely local
escape mechanisms unresolved.

