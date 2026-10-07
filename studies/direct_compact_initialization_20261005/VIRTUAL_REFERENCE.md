# Transferring a paired compact law to an independent dense reference

Date: 2026-10-05. Status: conditional probability theorems with complete
author proofs; the dense-pair bound, paired compression bound, admissible
direct sampler, and any required dynamical stability remain hypotheses.
This is a scoped author contribution, not an independent review or a
promotion claim.

Scientific inputs for this contribution were the supervisor's assignment
and `docs/notation.qmd`. Earlier task context was retained, but no prior
study artifact or other study was inspected for this contribution. The
proof skill `solve-math-rigorously` and the research-contract/adversarial
instructions of `investigate-conjectures` were applied. The required
canonical-notation skill remains unreadable at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`;
the previously authorized explicit-notation fallback is retained. No
experiment, Git operation, or external scientific source was used.

The main conclusion is conditional and finite-width: a good coupling of
a direct compact model to a virtual dense trajectory with the canonical
law transfers accuracy to a fresh independent dense network. The error
is the coupling error plus a dense-pair discrepancy. Reproducing the
full law of an existing paired compact initialization is one sufficient
construction of such a coupling. No dense-to-population approximation
or population bias estimate is needed, and no direct sampler is
constructed here.

## 1. Objects, information, and the comparison metric

Fix the deterministic data, dense width \(n\), permitted compact
architecture family and size bound, loss, optimizer, physical-time
convention, and observation domain. All probabilities below are
conditional on these fixed design choices. Any
dependence of the design on a requested confidence level is fixed before
applying the theorem.

Let \(Z\) denote the dense initialization randomness, and let

\[
F(Z)\in\mathcal X
\]

be its complete observed dense trajectory. The space \(\mathcal X\)
carries a jointly measurable distance \(d\), satisfying the triangle
inequality. An extended distance taking the value infinity is allowed.
For example, for a fixed input set \(\mathcal K\) and time set
\(I\subseteq[0,\infty)\), the required distance may be

\[
d(f,g)=\sup_{t\in I,\ x\in\mathcal K}|f(t,x)-g(t,x)|.
\]

If an endpoint prediction is also required, include its discrepancy in
this same distance by taking the maximum. All measurability and existence
requirements for the selected observations are hypotheses. For continuous
observations on a separable domain, the displayed supremum is measurable
when it can be reduced to a countable dense set. Every bound below uses
the same distance, domain, and physical clock.

Let \(\Theta\) be the measurable space of complete admissible compact
initializations, and let

\[
H:\Theta\longrightarrow\mathcal X
\]

be the measurable deterministic map that trains the prescribed compact
model and returns its observed trajectory. A point of \(\Theta\)
includes all weights, any fixed optimizer metric or preconditioner,
selected widths, and every retained auxiliary random quantity used by
training. If the compact width is random, \(\Theta\) can be the
disjoint union of its width-specific parameter spaces, with the
prescribed size bound imposed on every admissible member. A random
optimizer metric is distinct from the deterministic comparison distance
\(d\); any metric required to be fixed remains fixed during training.
Thus \(H\) is not a
fitted trajectory or an external forcing. If training itself is random,
its required randomness must first be included in the initialization
object, with the correct joint law and independence; equality of weight
marginals alone would then be insufficient.

A paired compression procedure supplies an initialization
\(\Phi(Z)\in\Theta\). Any extra compression randomness can be
included in \(Z\), with \(F\) ignoring those extra coordinates.
Write

\[
P=\operatorname{Law}(\Phi(Z)).
\]

A proposed direct generator returns \(G(U)\in\Theta\), with
law \(Q\), using a seed \(U\) independent of the dense network
used for comparison. Whether \(G\) is computable from only permitted
data and the known initialization law, and whether its memory, work,
coefficient precision, and output size meet the compactness contract,
are separate requirements. Calling \(Z\) a virtual seed and actually
generating the full dense initialization before applying \(\Phi\)
does not verify those requirements.

The law \(P\) concerns this full joint initialization, including
dependence between selected weights, widths, fixed metrics, and retained
selection randomness. Equal marginal laws of its pieces are insufficient.
The law of the initial prediction alone is also insufficient: equal
zero readouts can leave different hidden parameters and subsequent
dynamics. Random selection variables that are discarded still have to
be integrated out correctly to obtain the output's joint law.

Matching a few moments or contractions, or merely identifying an
asymptotic law, does not establish the required finite-width law equality
or a quantitative substitute below. If one proves that the full training
observation \(H\) is a measurable function of particular sufficient
statistics, equality of the full joint law of those statistics does
suffice. That factorization and joint-law identity require proof;
matching selected expectations is a different assertion.

## 2. A minimal virtual-reference bridge and exact-law transfer

Suppose \(Z'\) is an independent copy of \(Z\). For fixed
\(\alpha,\beta\in(0,1)\), assume finite nonnegative bounds
\(e=e(n,\alpha)\) and \(v=v(n,\beta)\) such that

\[
\mathbb P\bigl(d(H(\Phi(Z)),F(Z))>e\bigr)\le\alpha,
\tag{1}
\]

\[
\mathbb P\bigl(d(F(Z),F(Z'))>v\bigr)\le\beta.
\tag{2}
\]

These are respectively the paired compression hypothesis and the
independent dense-pair hypothesis. In particular, (2) is not merely a
bound for two densely coupled initializations.

The most general bridge needed here does not require the direct
initializer to have law \(P\). Suppose there exists a joint law of
\((\theta,V)\) with the following three properties:

- \(\theta\) has the actual direct generator's law \(Q\);
- \(V\) has exactly the canonical width-\(n\) dense trajectory
  law \(\operatorname{Law}(F(Z))\);
- \(\mathbb P(d(H(\theta),V)>e_{\mathrm{dir}})\le\alpha\)
  for a proved finite error bound \(e_{\mathrm{dir}}\).

Take a fresh canonical dense trajectory \(F(Z')\) independent of
this entire joint pair. Then (2) applies to \((V,F(Z'))\), because
they are independent with the correct common dense law. The triangle
inequality and union bound give

\[
\mathbb P\bigl(d(H(G(U)),F(Z'))>
 e_{\mathrm{dir}}+v\bigr)\le\alpha+\beta.
\tag{3a}
\]

Here the left side is the actual product experiment: its joint law is
the same as that of \((H(\theta),F(Z'))\). The two inner failure
events need not be independent. The direct initializer may be correlated
with its virtual dense trajectory, but the fresh reference must be
independent of the complete coupling, including all auxiliary randomness.
The deterministic shared data do not violate this independence.

This bridge is sufficient without matching the old compact law, and
without any population trajectory. It does not show how to construct
either an admissible direct generator or a good coupling. A proof-only
coupling is permissible; an operational procedure that secretly builds
the full virtual dense network has not thereby met the direct-generation
resource contract. Exact-law transfer is the following special case.

If \(Q=P\) and \(U\) is independent of the actual reference
\(Z'\), then

\[
\mathbb P\bigl(d(H(G(U)),F(Z'))>e+v\bigr)
\le\alpha+\beta.
\tag{3}
\]

Proof. Construct independent \(Z,Z'\) for the proof. Outside the
union of the failure events in (1) and (2), the triangle inequality gives

\[
d(H(\Phi(Z)),F(Z'))
\le d(H(\Phi(Z)),F(Z))+d(F(Z),F(Z'))
\le e+v.
\]

The union bound costs \(\alpha+\beta\); the two failure events
need not be independent. Since \(\Phi(Z)\) is independent of
\(Z'\), the joint law of \((\Phi(Z),F(Z'))\) is
\(P\otimes\operatorname{Law}(F(Z'))\). The joint law of
\((G(U),F(Z'))\) is the same product when \(Q=P\). Applying
the measurable map \((\theta,f)\mapsto(H(\theta),f)\)
transfers the preceding probability bound to the actual experiment.
No coupling between the actual generator and its actual dense reference
has been introduced. This proves (3).

For desired failure probability \(\delta\in(0,1)\), the choice
\(\alpha=\beta=\delta/2\) gives error

\[
e(n,\delta/2)+v(n,\delta/2)
\]

at failure probability at most \(\delta\). If both inputs are
instead evaluated at the same level \(\delta\), the conclusion
has failure probability at most \(2\delta\), not \(\delta\).

The intermediate dense trajectory \(F(Z)\) is used only to prove
the law-level inequality. It is not an input required by the direct
algorithm. The theorem neither computes nor estimates a population
trajectory. In particular, the two finite-width dense trajectories
share any systematic width-dependent behavior without a separate
population-bias term entering the triangle inequality.

## 3. Approximate laws in total variation

Define total variation by

\[
\|Q-P\|_{\mathrm{TV}}
=\sup_{A\subseteq\Theta\ \mathrm{measurable}}|Q(A)-P(A)|.
\]

If \(\|Q-P\|_{\mathrm{TV}}\le\varepsilon\), then under the
same independence from the reference,

\[
\mathbb P\bigl(d(H(G(U)),F(Z'))>e+v\bigr)
\le\alpha+\beta+\varepsilon.
\tag{4}
\]

Proof. For each initialization \(\theta\), let

\[
k(\theta)=
\mathbb P_{Z'}\bigl(d(H(\theta),F(Z'))>e+v\bigr).
\]

This is a measurable function with values in \([0,1]\). Equation
(3), applied to the law \(P\), says \(\int k\,dP\le
\alpha+\beta\). Since
\(k(\theta)=\int_0^1\mathbf1_{\{k(\theta)>t\}}\,dt\),
integration and the definition of total variation give

\[
\left|\int k\,dQ-\int k\,dP\right|
\le\int_0^1|Q(k>t)-P(k>t)|\,dt\le\varepsilon.
\]

This proves (4), without any continuity or stability estimate for
training. The same argument works if total variation is controlled
directly between the two trajectory laws. Initial-law total variation
implies that trajectory-law bound because the inverse image of any
measurable trajectory event is an initialization event.

For example, \(\varepsilon\le\delta/3\) and
\(\alpha=\beta=\delta/3\) give failure at most \(\delta\)
at radius \(e(n,\delta/3)+v(n,\delta/3)\). A fixed nonzero
total-variation error does not by itself support arbitrarily smaller
failure probabilities; the generator accuracy or another argument
would have to change.

## 4. Approximate laws by trajectory transport

Let \(P_H=\operatorname{Law}(H(\Phi(Z)))\) and
\(Q_H=\operatorname{Law}(H(G(U)))\). Suppose a coupling
\((X_P,X_Q)\) of \(P_H,Q_H\) obeys

\[
\mathbb P(d(X_P,X_Q)>r)\le\varepsilon
\tag{5}
\]

for some \(r\ge0\). Take this whole coupling independent of the
actual dense reference. Its \(P_H\) marginal satisfies (3).
The triangle inequality and a union bound give

\[
\mathbb P\bigl(d(H(G(U)),F(Z'))>e+v+r\bigr)
\le\alpha+\beta+\varepsilon.
\tag{6}
\]

No relationship between the coupling's \(X_P\) coordinate and a
particular dense seed is required: equation (3) has already established
the necessary independent-reference property of its marginal law.
The existence of a coupling satisfying (5) is a sufficient transport
hypothesis by itself.

For \(p\ge1\), define the Wasserstein distance using precisely
the observation distance \(d\):

\[
\mathcal W_p(P_H,Q_H)
=\inf_{\pi\in\operatorname{Cpl}(P_H,Q_H)}
 \left(\int d(f,g)^p\,\pi(df,dg)\right)^{1/p}.
\]

If \(\mathcal W_p(P_H,Q_H)\le\tau<\infty\), then for
every \(r>0\),

\[
\mathbb P\bigl(d(H(G(U)),F(Z'))>e+v+r\bigr)
\le\alpha+\beta+\left(\frac{\tau}{r}\right)^p.
\tag{7}
\]

Indeed, for every \(\eta>0\) the defining infimum supplies a
coupling with \(\mathbb E d(X_P,X_Q)^p\le\tau^p+\eta\).
On the event \(d(X_P,X_Q)>r\), the nonnegative random variable
\(d(X_P,X_Q)^p\) exceeds \(r^p\), so its probability is at
most \((\tau^p+\eta)/r^p\). Apply (6) and let
\(\eta\downarrow0\). The probability on the left depends only
on \(Q_H\) and the independent reference and therefore does not
change with the chosen coupling. No theorem asserting existence of
an optimal coupling is needed.

For \(\tau>0\), assigning transport failure \(\gamma>0\)
and taking \(r=\tau\gamma^{-1/p}\) gives radius

\[
e+v+\tau\gamma^{-1/p}
\quad\text{and failure at most}\quad\alpha+\beta+\gamma.
\tag{8}
\]

For \(\tau=0\), apply (7) at every positive \(r\) and then
let \(r\downarrow0\). The events on the left increase to the
event with threshold \(e+v\), giving the same conclusion with
zero transport radius. In particular, the equal allocation
\(\alpha=\beta=\gamma=\delta/3\) gives radius
\(e(n,\delta/3)+v(n,\delta/3)+\tau(3/\delta)^{1/p}\).

If for each fixed confidence level the two input errors and the
trajectory transport error are \(O(n^{-1/2})\), this conclusion
also has error \(O(n^{-1/2})\). That rate is conditional on those
three bounds in the actual comparison distance.

In particular, the weaker rate forms reported in the supervisor's
assignment do not meet that hypothesis automatically. If the available
bounds only have the form

\[
e(n,\alpha)=C_\alpha n^{-1}+r_n(\alpha),\qquad
v(n,\beta)=D_\beta n^{-1/2}+s_n(\beta),
\quad r_n(\alpha),s_n(\beta)=o(1),
\]

then exact-law transfer gives their sum, including both remainders.
An \(o(1)\) remainder can be \(n^{-1/4}\), for example, so this
is only an \(O(n^{-1/2})+o(1)\) estimate and does not prove a bound
\(C_{\mathrm{data},\delta}/\sqrt n\). Such a strict bound
would require an appropriate \(O(n^{-1/2})\) bound on the combined
remainder. Using (3a) instead requires both its direct-coupling error
and its dense-pair error to be controlled at that rate; sharpening the
compact side alone does not remove a dense-pair remainder. The reported
source rates were not independently verified in this scoped note.
No rate upgrade is asserted.

## 5. Parameter transport needs dynamical stability

Let \(\rho\) be an explicitly chosen parameter distance on
\(\Theta\), with all width normalizations specified when the
distance is instantiated. Small
\(\mathcal W_p^{\rho}(P,Q)\) alone does not imply small
\(\mathcal W_p^d(P_H,Q_H)\).
If widths or architecture metadata can differ, the metric must also
specify how such pairs are compared; it cannot silently compare only
the coordinates present in both parameter arrays.

A sufficient global condition is a nondecreasing modulus
\(\omega:[0,\infty)\to[0,\infty)\), finite at the radii
used, such that

\[
d(H(\theta),H(\widetilde\theta))
\le\omega(\rho(\theta,\widetilde\theta))
\quad\text{for all relevant initializations}.
\tag{9}
\]

If \(\mathcal W_p^{\rho}(P,Q)\le\tau\), the same coupling
and moment argument gives, for every \(r>0\),

\[
\mathbb P\bigl(d(H(G(U)),F(Z'))>e+v+\omega(r)\bigr)
\le\alpha+\beta+(\tau/r)^p.
\tag{10}
\]

For a global Lipschitz bound \(\omega(r)=Lr\), pushing any
parameter coupling through \((H,H)\) also directly proves
\(\mathcal W_p^d(P_H,Q_H)\le L\tau\). Thus the relevant
root-\(n\) requirement is on \(L\tau\), with its actual
dependence on width and horizon, not on \(\tau\) alone.

A useful local version allows a measurable good set
\(K\subseteq\Theta\) on which (9) holds for every pair of
points, together with
\(P(K^c)\le\zeta_P\) and \(Q(K^c)\le\zeta_Q\).
For any parameter coupling, the probability that either coordinate
leaves \(K\) is at most \(\zeta_P+\zeta_Q\), regardless
of their dependence. Consequently (10) becomes

\[
\mathbb P\bigl(d(H(G(U)),F(Z'))>e+v+\omega(r)\bigr)
\le\alpha+\beta+\zeta_P+\zeta_Q+(\tau/r)^p.
\tag{11}
\]

The mass outside \(K\) under both laws must be accounted for.
If the stability statement itself has another exceptional event, its
failure probability must also be included. All-time stability or
endpoint control cannot be inferred from a bound proved only on each
fixed finite interval.

For an elementary illustration, the smooth scalar equation
\(\dot x=x\), \(x(0)=\theta\), has trajectory
\(H(\theta)(t)=\theta e^t\). The parameter laws concentrated
at zero and at \(h>0\) have parameter Wasserstein distance \(h\),
which tends to zero. Their trajectory distance on \([0,T]\) is
\(he^T\), and their uniform distance on all \(t\ge0\) is
infinite. This does not claim instability of the neural model; it
disproves the general inference from small parameter transport and
smooth dynamics to small all-time trajectory transport.

## 6. Deterministic finite-width centers and witnesses

The dense-pair hypothesis (2) already implies a deterministic center at
the same finite width. Define

\[
a(z)=\mathbb P_{Z'}\bigl(d(F(z),F(Z'))>v\bigr).
\]

Its expectation is at most \(\beta\). Therefore some seed
\(z_0\) has \(a(z_0)\le\beta\): if \(a>\beta\)
almost surely, its expectation would be strictly greater than
\(\beta\). The deterministic dense trajectory
\(c_n=F(z_0)\) consequently satisfies

\[
\mathbb P\bigl(d(F(Z'),c_n)>v\bigr)\le\beta.
\tag{12}
\]

The center may depend on \(n\), the data, the comparison distance,
and the specified error/confidence level. Its existence does not give
a method for selecting or evaluating it, and its dense realization
need not satisfy any compact resource restriction. For example,
deterministic scalar trajectories \(F_n=(-1)^n\) have zero pair
discrepancy at every width but do not converge as \(n\to\infty\).
Thus pair concentration alone supplies neither a population limit nor
a bound for bias relative to one.

There is also a deterministic compact witness under both (1) and (2),
without assuming that a direct sampler exists. The first triangle
argument in the proof of (3) establishes

\[
\mathbb E_Z\!\left[
 \mathbb P_{Z'}\bigl(d(H(\Phi(Z)),F(Z'))>e+v\bigr)
 \right]\le\alpha+\beta.
\]

Averaging therefore supplies a seed \(z_c\) and a fixed
initialization \(\theta_c=\Phi(z_c)\) with

\[
\mathbb P_{Z'}\bigl(d(H(\theta_c),F(Z'))>e+v\bigr)
\le\alpha+\beta.
\tag{13}
\]

This is a genuine existential derandomization statement in any
admissible class that permits these fixed coefficients and imposes
only the already verified size restrictions. It does not by itself
give an explicit law-only algorithm with controlled running time,
precision, or coefficient provenance. In particular, the proof does
not identify \(z_c\), calculate \(\Phi(z_c)\), or permit its
selection by inspecting the actual reference trajectory. It also
does not provide one seed simultaneously valid for every confidence
level, width, or dataset. Those would require additional arguments.

An arbitrary favorable dense witness is insufficient. To see this at
the level of probability laws, let the dense scalar trajectory be zero
with probability \(1-\varepsilon\) and a fixed \(L>0\) with
probability \(\varepsilon\), where \(0<\varepsilon<1/2\).
Two independent dense draws disagree with probability
\(2\varepsilon(1-\varepsilon)\). Even suppose the paired
compact map reproduces every dense draw exactly, so its paired error
is identically zero. Selecting the favorable paired witness whose
dense value is \(L\) still fails against an independent dense
reference at any error radius less than \(L\) with probability
\(1-\varepsilon\). The witness's perfect paired fit does not
make it typical. Equations (12) and (13) select centers by an averaging
argument; they do not say that every successfully compressed dense
seed has the required independent-reference guarantee.

## 7. What is proved and what remains open

The minimal coupling theorem is (3a), with exact-law specialization
(3). The specialization's approximate-law versions are (4), (6),
and (7); parameter-law versions additionally require the stability
and exceptional-mass hypotheses of (9)--(11). The averaging statements
(12)--(13) establish finite-width deterministic witnesses, with the
quantifiers stated there. Each proof uses elementary integration,
the triangle inequality, or an explicitly derived probability bound;
no unverified external theorem is imported.

No dense-pair estimate, paired compression estimate, exact or
approximate direct sampling algorithm, or global neural-flow stability
estimate has been established by this note. In an application, those
are the substantive remaining obligations. A sampler must satisfy the
actual admissible-information and computational restrictions; a claim
of equality in law cannot conceal a full dense draw, future trajectory,
or an unbounded-precision encoding. A favorable witness cannot replace
the distributional hypotheses or their averaging argument.

Author checks covered product-law independence, failure-budget
allocation, total-variation normalization, nonattainment of the
transport infimum, zero transport distance, parameter-versus-trajectory
metrics, exceptional-set mass under both laws, finite-versus-all-time
scope, full joint initializer metadata, unquantified rate remainders,
and the deterministic-witness quantifiers. These are author
checks, not an independent review.

Freeze note: this candidate was frozen after the author check on
2026-10-05. Its SHA-256 is supplied with the handoff, outside the file
to avoid a self-referential hash. Any substantive edit requires a new
hash and corresponding check.
