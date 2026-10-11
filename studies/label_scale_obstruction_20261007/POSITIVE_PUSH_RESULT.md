# Stronger positive search: dependent triples and the remaining escape problem

2026-10-11. Theoretical continuation of the same investigation. These are
study results, not promoted material. The requested unconditional
arbitrary-label Gaussian fitting theorem, or a genuine large-width
Gaussian nonfitting counterexample, remains open.

## 1. Fixed model and question

The inputs \(x_a\) are unit vectors, with no two parallel or antiparallel,
and \(X=[x_1,\ldots,x_m]\). Labels \(y\in\mathbb R^m\) are fixed
independently of width and initialization, with no amplitude restriction.
The two-hidden-layer network and loss are
\[
 f=\frac1n\tanh\!\bigl(W\tanh(AX)\bigr)^\top w,
 \qquad \mathcal L=\frac{\|f-y\|^2}{m},
\]
where \(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\),
and \(w\in\mathbb R^n\). Training has block mobilities \((n,1,n)\).
Initialization is independent \(A_{jk}\sim N(0,1)\),
\(W_{ij}\sim N(0,1/n)\), and exactly \(w=0\). Unit inputs absorb
the maintained book's input normalization; no layer or mobility is changed.

The positive targets are to remove input independence from the existing
Gaussian convergence-or-escape result, or to prove uniform-in-time
parameter boundedness and thus fitting for the input classes already
covered by finite-critical-limit avoidance. A decisive negative target retains
the earlier probability requirement: one fixed admissible dataset and
constants \(c,p>0\), independent of width, such that
\[
 \liminf_{n\to\infty}
 \Pr\{\lim_{t\to\infty}\mathcal L_n(t)\ge c\}\ge p,
\]
with actual initial learning and hidden-feature motion. The time limit
comes first. A specially initialized trajectory, a stationary point,
or a Gaussian event whose probability may vanish with width does not
settle that target.

## 2. New landscape theorem without input independence

**Theorem.** For any three pairwise nonparallel unit inputs, any labels,
and width \(n\ge3\), there is no finite local minimum with
\[
                 0<\mathcal L<\frac{\|y\|^2}{3}.
\]
In particular, the inputs may all lie in a two-dimensional plane, with
arbitrary angles subject only to the nonparallel condition. Neither
orthogonality, equal label magnitudes, nor a small-label hypothesis is
used. The assertion is deterministic and holds at every finite parameter
configuration in this loss range.

The strict upper endpoint is the zero-output starting loss. For nonzero
labels, canonical Gaussian training decreases the loss strictly initially
almost surely, so this is the relevant interval for a later finite
positive-loss limit. The initial decrease does **not** make the theorem
a statement that every such limit is avoided.

The complete new proof is Theorem 7 of
[DEPENDENT_INPUT_PUSH.md](DEPENDENT_INPUT_PUSH.md). Its minimal-circuit
dependencies are proved in
[DEPENDENT_GEOMETRY_RENEWAL.md](DEPENDENT_GEOMETRY_RENEWAL.md), and
its independent-input case is in
[TANH_NECESSARY_GEOMETRY.md](TANH_NECESSARY_GEOMETRY.md).
The root reconstructed all three sources. A separate complete internal
reconstruction passed without a requested correction, as recorded in
[THREE_SAMPLE_LANDSCAPE_CHECK.md](THREE_SAMPLE_LANDSCAPE_CHECK.md).
No promotion review is asserted.

Here is the proof structure, with the key new step made explicit.

1. For three dependent nonparallel inputs, the only input relation has
   three nonzero coefficients, each smaller in absolute value than the
   sum of the other two. This follows from unit lengths and the strict
   triangle inequality.
2. The minimal-circuit ridge lemma and exact compensating changes of
   \(W\) exclude a positive-loss local minimum whose first-feature
   matrix has rank two. Rank zero has the starting loss. At a remaining
   putative minimum below starting loss, flat middle-weight variations
   and the positive-semidefinite Hessian test force all first-feature
   rows to be signed copies of one nonzero profile.
3. After the exact tanh neuron-sign symmetries, write this profile as
   \(u\in\mathbb R^3\). The accessible first-feature variations form a
   two-dimensional plane. There are two cases: three distinct nonzero
   magnitudes in \(u\), or one zero coordinate and two equal nonzero
   magnitudes.
4. In the distinct-magnitude case, both the first-layer ridge curvature
   and the top-layer residual curvature are indefinite on that plane.
   A putative nonnegative full Hessian would require one dominant
   readout coefficient and all the others of the opposite sign.
   This mixed-sign possibility is not discarded by assumption.
   Compensating the first-feature scaling through \(W\), and completing
   the square in that scaling, instead supplies a strictly negative
   quadratic form in the remaining neuron variations. The surviving
   top-layer correction has at most one positive direction. Killing
   the prediction differential leaves dimension \(n-1\ge2\), so a
   nonzero variation makes the full loss Hessian negative.
5. In the zero/equal-magnitude case, the compensated scaling directions
   have zero quadratic form but a nonzero mixed block. Positive
   semidefiniteness would force \(W^\top w=0\), contradicting the
   nonzero prediction. Zero readouts and zero entries of \(W^\top w\)
   are handled by arbitrarily small constant-loss variations inside
   the same minimizing neighborhood.

This closes the former mixed-sign local-minimum gap for all input
triangles, not just signed regular triangles. It does not assert that
every bad critical point has enough negative Hessian directions for
Gaussian avoidance.

## 3. Why this is not yet a Gaussian fitting theorem

The previously checked result remains:
for linearly independent inputs and
\(n\ge\max\{1,2m-4\}\), arbitrary fixed labels satisfy
\[
 \mathcal L_\infty>0
 \ \Longrightarrow\
 \|(A(t),W(t),w(t))\|\longrightarrow\infty
 \quad\text{almost surely}.
\]
Its source and analytic convergence-or-escape assembly are
[GAUSSIAN_RANK_ONE_COMPLETION.md](GAUSSIAN_RANK_ONE_COMPLETION.md) and
[GAUSSIAN_RANK_ONE_COMPLETION_CHECK.md](GAUSSIAN_RANK_ONE_COMPLETION_CHECK.md).

There are two separate remaining obligations for dependent triples:

- Exclude convergence to finite positive-loss critical points that are
  not local minima, under the exact zero-readout Gaussian law.
- Exclude positive-loss escape to infinity.

The first obligation cannot be silently discharged by ordinary
random-initialization saddle avoidance. There are \(n\) readout
coordinates fixed to zero, so this law is singular in the full parameter
space. The checked argument needs at least \(n\) unstable directions,
together with the actual initial flow's transversality to that slice.
Only \(n-1\) directions do not suffice for that dimensional argument.
The separate audit
[GAUSSIAN_SLICE_RECHECK.md](GAUSSIAN_SLICE_RECHECK.md) verifies this
distinction and supplies a noncanonical analytic countermodel to the
weaker geometric inference. That countermodel is not a neural-network
failure example.

For general dependent data there is also a stronger pointwise mixed-index
estimate in Section 2 of
[DEPENDENT_INPUT_PUSH.md](DEPENDENT_INPUT_PUSH.md). It controls the
high-rank residual-backward strata with a width threshold depending on
input rank rather than sample count. The exceptional low-rank strata
remain; it is not a general input-independence removal.

The further pointwise result in
[DEPENDENT_INDEX_EXTENSION.md](DEPENDENT_INDEX_EXTENSION.md) does reach
the full \(n\)-direction index for three samples when the first features
and active top features both have rank two, the residual has no zero
coordinate, and each zero readout has the specified nonzero mixed
derivative. The latter qualification is vacuous when every readout is
nonzero. Its proof uses top-row curvature and active-readout variations
to cancel the entire prediction differential. The root reconstructed
this author-checked note; it has not had a separate complete review.
Rank-one active top features and the other exceptional cases remain,
so this partial avoidance criterion does not close the triple theorem.

## 4. New boundedness reduction for two correlated inputs

The boundedness route was pursued in the original two-input system, with
arbitrary labels and correlation \(\rho=x_1^\top x_2\in(-1,1)\).
For one first-layer row, let \(p_1,p_2\) be its two preactivations and
let \(R=\|W_{:,j}\|^2\) be the squared norm of its middle-layer column.
The exact balance now has a coercive integrating factor:
\[
 F_\rho(p_1,p_2)=\frac12\left[
 \frac{\log\cosh(p_1+p_2)}{1+\rho}
 +\frac{\log\cosh(p_1-p_2)}{1-\rho}\right],
\]
\[
 \frac n2\dot R
 =\cosh(p_1+p_2)\cosh(p_1-p_2)\,\dot F_\rho .
\]
Thus the column norm and this coercive first-layer potential increase
or decrease together instantaneously. In particular,
\[
 F_\rho(t)\le F_\rho(0)+
       \frac n2\int_0^t\max\{\dot R(s),0\}\,ds.
\]
The potential controls \(\max\{|p_1|,|p_2|\}\), so bounded readout
and finite cumulative increases of every middle-column squared norm
imply boundedness of all parameters. The prior two-input Gaussian
theorem implies fitting almost surely on that event.

Neither of those trajectory conditions has been proved automatically.
The new result does sharpen the escape alternative: outside the same
Gaussian null set, if \(W,w\) stay bounded but loss does not vanish,
some middle-column squared norm must
have infinite cumulative increases **and** infinite cumulative decreases.
Bounded, eventually monotone column norms cannot produce this escape.

There is an exact obstruction to the most direct invariant approach.
For \(\rho\ne0\), no nonconstant \(C^2\) function of only
\((p_1,p_2,R)\) is conserved for every possible backward forcing.
The proof uses the nonzero Lie bracket of the two forcing fields.
It does not rule out an invariant of the full network or a bound using
the actual residual feedback. A slow-loop construction also shows that
this balance plus finite squared speed alone does not force boundedness;
the construction is explicitly not a neural-network trajectory.
All derivations and qualifications are in
[BOUNDED_ESCAPE_PUSH.md](BOUNDED_ESCAPE_PUSH.md).

## 5. Negative search: a nonlinear exclusion, not a failure example

The negative route tested a fully trained invariant family with common
first-layer responses and separate top-neuron weights and readouts.
When first responses are positive, residuals change sign only from
negative to positive as those responses increase, and two top neurons
are strictly ordered in both positive weight and positive readout,
the smaller top weight cannot increase strictly to infinity while
both readouts remain positive and bounded.
The proof allows the common first layer and residuals to evolve.
For an actual all-positive saturation escape, boundedness of the two
readouts follows from loss monotonicity and nonnegative neuron
contributions at fixed width.

The full nonlinear proof is in
[GAUSSIAN_FAILURE_PUSH.md](GAUSSIAN_FAILURE_PUSH.md). It removes the
previous unproved derivative-ratio hypothesis in this residual-ordering
class. It does not exclude reverse-ordered neurons, sign-changing
contributions, nonmonotone motion, or general feature geometry.
The invariant family itself is Gaussian-null; no capture estimate for
the canonical Gaussian initialization is inferred.

Consequently, neither this exclusion nor the invariant obstruction in
Section 4 is a genuine negative result of the type requested. No new
fixed-data nonfitting event with probability bounded away from zero as
width grows has been proved.

## 6. Evidence and supersession

| Claim | Current status |
|---|---|
| No below-starting-loss local minimum for any nonparallel triple, \(n\ge3\) | New deterministic theorem; separate whole-proof internal reconstruction passed |
| Arbitrary-label Gaussian convergence-or-escape for independent inputs | Prior internally checked theorem, retained unchanged |
| Arbitrary-label Gaussian fitting for all nonparallel triples | Open: finite saddle avoidance and escape remain |
| All-time parameter boundedness under arbitrary labels | Open; new exact balance and variation reduction are conditional |
| Robust canonical Gaussian late-training failure | Open; the tested ordered saturation mechanism is excluded under its stated hypotheses |

The triple theorem supersedes the general-triple local-minimum-open
wording in the earlier dependent-geometry renewal source. It does not
supersede that source's warning about Gaussian avoidance or escape.
The new row-basis index bound sharpens the earlier dimension-subtraction
bound on its stated strata. The nonlinear saturation proof replaces
a conditional derivative-ratio estimate only in the explicitly
ordered-residual class.

The research program has not reached either requested terminal outcome.
The next bottleneck for the new triple class is a canonical-slice
avoidance argument for all remaining finite bad critical points; even
that would leave the independent all-time escape obligation.
No compression theorem, small-label qualification, maintained-book
statement, optimizer, or initialization law has been changed.
No simulation, staging, or commit was performed.

## 7. Audit provenance

The root led the synthesis and reconstructed the new proofs. The scoped
dependent-input route wrote DEPENDENT_INPUT_PUSH.md and
DEPENDENT_INDEX_EXTENSION.md. After those derivations, the separate
bounded-escape route reconstructed the frozen triple theorem and its
complete required dependencies in THREE_SAMPLE_LANDSCAPE_CHECK.md;
the checked source hash is
5c98619efefa4e1a8e3e3ac058d622b6f346d87f06bdfa31647c17e51805a7fb.
This was an internal continuation check, not a fresh promotion review.

The bounded-escape and Gaussian-failure routes wrote their respective
push notes. The root reconstructed both; the bounded-escape route also
checked the other route's nonlinear saturation argument. The
Gaussian-failure route separately rechecked the existing slice-avoidance
argument, then audited this synthesis's claim scope. That audit restored
the explicit almost-sure qualification on the bounded-middle
infinite-variation consequence. It accepted the triple theorem only as
a supplied claim and did not substitute for its separate proof check.

The existing BOUNDEDNESS_RENEWAL.md, DEPENDENT_GEOMETRY_RENEWAL.md,
and GAUSSIAN_TRAPPING_RENEWAL.md were complete same-study scientific
inputs. They were not counted as new work of this push. No unpromoted
research was imported from another study.
