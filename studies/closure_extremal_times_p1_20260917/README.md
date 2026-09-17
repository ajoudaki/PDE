# Extremal data geometry and hitting times for the p=1 closure

Started 2026-09-17. Research only; no promotion.

## Question and scope

Determine what difficult balanced binary training configurations force about
physical gradient-flow hitting times and the possible growth of a loss-controlling
Lyapunov potential with a geometry-independent decay rate. Separate the initial
loss neighborhood, a fixed substantial improvement, and the small-loss tail.

The target is the exact canonical bias-free two-hidden-tanh p=1 population
closure on the normalized input circle, with complete initialization correlations,
eta=1/4096 normalization, full evolving w,c,M, the actual transpose, and
unhalved probability-weighted square loss. Inputs are x=sqrt(2)u. Labels are
+/-1 and probabilities sum to one, with half the mass at each label.

This is a new extremal-configuration direction. Scientific repository inputs
are established docs/ and code/ only, plus this study's own future artifacts.
No unpromoted result from another study is imported. Any two-input anchor used
here must be derived anew from the canonical equations. Conversation statements
about earlier results are not proof dependencies.

## Initial research contract

The central observable is tau(ell)=inf{t>=0: L(t)<=ell}, with inf empty=infinity.
Seek explicit families, rigorous lower bounds, and matching upper bounds where
available. A divergence lower bound alone is not a sharp asymptotic or a global
maximizer theorem. Since collisions are permitted as limits, first determine
whether the proposed unconstrained maximization has a finite maximum.

For potential comparisons, declare L<=h(Phi) with h fixed and increasing and
Phi(t)<=exp(-lambda t)Phi(0), with lambda independent of input geometry. A
geometry-dependent h or power can hide difficulty and must not be left implicit.
No future trajectory or oracle endpoint may define a proposed state functional.

The analytical routes are (1) exact comparison and energy-based delay bounds,
(2) signed moment cancellation in balanced clusters, (3) complete rederivation
of a symmetric two-input anchor and its hitting-time/tail consequences. Work is
sequential. No subagents or experiments have been launched. No numerical campaign
is planned; any later diagnostic requires its own resource and validity contract.

## Sources and process

Read AGENTS.md, RESEARCH_WORKFLOW.md Part 1, research and rigorous-mathematics
skills and applicable references, docs/README.md and docs/NOTATION.md.
Canonical scientific inputs: docs/global_nonlinear.md C.4.7.9 state, equations,
well-posedness and energy, C.4.7.10 D.3 compatible normalization/existence;
docs/observable_p1.md complete exact initialization and physical metric.

Root owns all files in this flat study. Existing unrelated working-tree changes
are preserved. HEAD at start: 379ede09d8bcc53a8efedfac53672e3d0711ade2; index empty.
No Git write, established-material edit or promotion is authorized by this work.

## Current results

The complete argument is [extremal_hitting_times.md](extremal_hitting_times.md).
The two-input convergence anchor is rederived from the canonical equations in
[two_input_anchor.md](two_input_anchor.md). These are author-checked internal
results; no independent review or promotion is claimed.

| Claim | Scope and result |
|---|---|
| Physical escape-time principle | If label correlation is at most b_R in the radius-R physical ball at initialization and 2b_R<1-ell, then tau(ell)>=R^2/(2b_R). Exact nonlinear energy argument. |
| Close opposite-label pair | For fixed ell<1, tau(ell)>=c/delta, uniformly in the center orientation. A reflection subfamily is separately proved to fit, so arbitrarily long finite hitting times really occur. |
| Balanced three-input obstruction | Angles -delta,0,+delta, labels +,-,+, weights 1/4,1/2,1/4: tau(ell)>=c/delta^2. The inputs are distinct and the exact initialized features represent their labels. Training convergence and a matching upper time bound remain open. |
| Initial-loss neighborhood | For the triple, tau(1-epsilon)>=c min(delta^-2,epsilon delta^-4). At each fixed dataset, tau(1-epsilon)~epsilon/(4||sum mu y H0||^2) when that norm is nonzero. The two limits cannot be interchanged. |
| Higher signed cancellations | Alternating binomial weights on N=r+1 equally spaced angular offsets cancel moments through r-1, with initialized dissipation of order delta^(2r) at centers with nonzero rth initialized feature derivative. r=N-1 is maximal moment cancellation for N fixed distinct offsets. No higher-order long-time bound is inferred. |
| Necessary potential growth | A common lambda>0 and a fixed comparison L<=h(Phi) require Phi0>=h^-1(ell) exp(lambda tau(ell)). The triple forces at least exp(c/delta^2) initial growth; this is necessary, not sufficient or sharp. |
| Small-loss pair tail | For each fixed admitted reflection pair, tau(ell)=(4K_*)^-1 log(1/ell)+O(1), where K_* is its derived fitted full gradient strength. Its delta dependence remains unbounded by a useful sharp estimate here. |
| Unconstrained extremum | Sup tau(ell)=infinity already over pairs known to fit; the balanced representable triple family also has infinite supremum by its lower bound. There is no finite worst-case time under the stated unconstrained data class. |

The potentially useful new design constraint is an ESSENTIAL initial singularity
if a geometry-independent exponential rate is required. Adding finitely many
polynomial inverse-separation terms cannot satisfy that normalization. A
geometry-dependent decay rate is another way to encode difficult data; the two
normalizations must not be conflated. Large initial size can cover a long
transient but cannot repair a vanishing terminal exponential exponent under a
fixed power comparison to loss.

The local landscape escape quantity in the main proof is determined by the
current state and fixed data. It supplies a necessary lower bound on remaining
time; no Lyapunov derivative is asserted for it. Likewise a time upper bound
alone cannot upper-bound an arbitrary candidate potential, because it can be
multiplied by an arbitrary positive data-dependent factor.

## Verification and limitations

[validation.md](validation.md) records the complete author audit, source and proof
hashes, topology checks and exact finite arithmetic. Reproduce the arithmetic with
`python studies/closure_extremal_times_p1_20260917/check_algebra.py` from the root.
This is a deterministic check of identities, not an experiment or proof of flow
convergence. [manifest.sha256](manifest.sha256) records the final input versions.

The generic-convergence question is not resolved. In particular the triple's
delta^-2 bound is a LOWER bound, not its true asymptotic time. No globally slowest
configuration, matching upper growth order, or common-rate potential has been
constructed. The best next obligation is a matching or separating upper bound
for one fixed substantial-loss threshold on the balanced three-point family;
its terminal rate must be analyzed separately. No compatible nonconvergent
initialized trajectory has been constructed.

No experiment, subagent, Git write or established-material edit was performed.
