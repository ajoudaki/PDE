# Scalar response compression with terminal stability

2026-09-30. Continuation of the structured full-rank scalar-compression study.
This note records internally checked mathematical results, not promoted book
material. No network training experiments were run in this continuation.

## Research target and decision

The target is a second compression of the fixed-k Gaussian-block P1 population
system. Its recurrent coordinates must be scalar observables or response
aggregates. A density grid, representative blocks, Monte Carlo populations,
or a complete large moment expansion does not answer the efficiency question.
At comparable observable accuracy, the requested size is smaller than a sampled
population width. A useful arbitrary-accuracy sequence for a fixed task is
stronger than independence of width at a single accuracy level.

The user's terminal-stage intuition leads to a valid quantitative theorem.
It also suggests a much smaller active-phase construction: organize retained
states by successive residual responses, rather than total degree in all
neuron coordinates. A concrete instance captures the first feature-learning
correction with a moving positive-semidefinite kernel. It has an all-time
error theorem in a small-label regime and an arbitrary-input decoder.

The decision remains constructive, but the claim is deliberately limited.
These results do not prove an efficient arbitrary-accuracy scalar hierarchy
for a fixed strong-learning task, or convergence to the fully dense iid-
Gaussian model after replacing its initialization by fixed-size blocks.

## Why stopping alone did not fix the previous truncations

The implemented selective aggregate dynamics already stop at zero residual.
In `true_aggregate_ode.py`, every local response derivative has a factor R,
sigma, or a derivative field D. At R=0, sigma=0 and the defining D rows also
vanish. With the default `row_envelope` penalty, its coefficient vanishes
as well. `selective_runtime_fast.py` preserves those same rows and envelopes.
Thus the recent fitted-but-inaccurate scalar outputs cannot be explained
simply by a missing zero-residual stopping condition.

The exact P1 output equation has the form

\[
\dot r=-Kr+\rho d,\qquad \rho=\|r\|_{\rm RMS}.
\]

The nonsymmetric K and the extra rho term retain the difference between
current forward features and their stored history average. They cannot be
discarded solely to obtain a positive kernel. A wrong training-to-test
response can accumulate a finite but large error before both systems stop.
The new proofs control this error source, in addition to stopping.

## Result one: the terminal phase can be replaced by a small scalar ODE

The complete statement and proof are in
[TERMINAL_FREEZE_THEOREM_20260930.md](TERMINAL_FREEZE_THEOREM_20260930.md), with
an independent check in
[TERMINAL_FREEZE_AUDIT_ACTIVITY_ROUTE_20260930.md](TERMINAL_FREEZE_AUDIT_ACTIVITY_ROUTE_20260930.md).

At a handoff, suppose the actual residual operator has positive margin

\[
\lambda_0=\lambda_{\min}(\operatorname{sym}K_0)
                -\|d_0\|_{\rm RMS}>0,
\]

and its coefficient variation is bounded by learning activity,

\[
\|\dot K\|+\|\dot d\|_{\rm RMS}\le A\rho.
\]

With a sufficiently small handoff residual, the frozen learned response

\[
\dot{\bar r}=-K_0\bar r+\|\bar r\|_{\rm RMS}d_0
\]

tracks the remaining exact dynamics. For a passive output, freeze its
current response coefficients in the corresponding output equation.
If their variation and sizes are bounded by B and M as specified in the
theorem, then

\[
\sup_{t\ge0}|f(t,u)-\bar f(t,u)|
\le \frac{2}{\lambda_0^2}
       \left(B+\frac{MA}{\lambda_0}\right)\rho_0^2.
\]

The estimate covers all subsequent physical time and the final prediction.
The smallness and state-tube hypotheses are explicit in the theorem. This is
O(handoff MSE), with uniform constants required for that asymptotic statement.
It justifies simplifying the terminal stage after feature learning has been
tracked accurately. It does not provide the missing accurate active phase.
A continuum of test inputs also needs a finite representation of the frozen
query coefficient functions; that representation is not free.

The more general proof tool is
[TERMINAL_ACTIVITY_ROUTE_20260930.md](TERMINAL_ACTIVITY_ROUTE_20260930.md).
For aggregate error E and residual error R, inequalities

\[
E'\le a\rho E+bR+\epsilon_x\rho,
\qquad
R'\le-\lambda R+c\rho E+\epsilon_r\rho
\]

close on E+bR/lambda. Their amplification is exponential in total activity,
not elapsed physical time. The note also proves bounded clock mismatch and
states exactly where residual contraction is an additional assumption.

## Result two: a small moving-kernel construction with a source bound

The complete construction and proof are in
[KERNEL_SCALAR_ROUTE_20260930.md](KERNEL_SCALAR_ROUTE_20260930.md); the separate
proof check is
[KERNEL_SCALAR_AUDIT_ACTIVITY_ROUTE_20260930.md](KERNEL_SCALAR_AUDIT_ACTIVITY_ROUTE_20260930.md).
The Gaussian population-flow dependency and extension to bounded C²
activations with bounded first two derivatives are proved in
[KERNEL_POPULATION_EXISTENCE_20260930.md](KERNEL_POPULATION_EXISTENCE_20260930.md).
That supporting proof received a complete separate check in
[KERNEL_POPULATION_EXISTENCE_AUDIT_20260930.md](KERNEL_POPULATION_EXISTENCE_AUDIT_20260930.md).

Assume zero population readout at initialization and labels y=a ybar. Keep
the residual r, its integral z, and the ordered second integral J:

\[
\dot z=r,\qquad \dot J=rz^T.
\]

The symmetric part is redundant, because J+J^T=zz^T. Its skew part records
the order in which different residual channels acted. These are scalar
response histories, not neuron representatives or a population density.

The exact equations explain the choice. Initially the readout grows as
an integral of residuals. First-layer and middle-layer feature velocities
then multiply a current residual by that readout, producing precisely the
ordered integrals J. The associated changing kernel is determined by one
initial tangent-response Gram tensor S and the initial output-feature Gram
K0. The middle-weight part of S is a product of two population expectations,
which is essential because learned connections cross the Gaussian blocks.

Two matrices M(J) and N(z), defined explicitly in the proof, give the first
changing-kernel correction K0+M+M^T+N. Here N is PSD. The completion

\[
\widehat K=(I+K_0^{-1}M)^T K_0(I+K_0^{-1}M)+N
\]

is always PSD and changes the approximation only at the next omitted order.
The training ODE is

\[
\dot r=-\frac2m\widehat K r,\qquad
\dot z=r,\qquad \dot J=rz^T.
\]

Loss is nonincreasing, every state derivative vanishes at r=0, and the
feature kernel genuinely evolves. These facts alone are not the accuracy
proof. The essential additional result is a derived error source:

\[
\left\|\dot f_{\rm P1}+\frac2m\widehat K(z,J)r\right\|
\le C\left(\int_0^t\|r(s)\|ds\right)^4\|r(t)\|.
\]

If K0 is positive definite and a is sufficiently small, both dynamics have
total activity O(a). Residual damping and an integrated feedback estimate
then give

\[
\sup_{t\ge0,\ |x|\le1}|f_{\rm P1}(t,x)-\widehat f(t,x)|
\le Ca^5.
\]

The theorem covers the Gaussian-block population, with finite Gaussian
moment constants, and the entire input disk. It does not substitute a
bounded maximum over infinitely many block matrices. The loss-curve error
is O(a^6). Integrating the residual difference also gives an O(a^5) error
in the accumulated-activity clock, uniformly for all physical time.
The displayed construction was derived for tanh; the linked bounded-C²
extension uses the same response tensor and scalar ODE with phi and phi'
in its initialization coefficients.

Third response integrals P'_{a;bc}=r_aJ_bc allow decoding any new input
through known initialization coefficient functions. A correction using K0
enforces exact equality between the training prediction and the test decoder
when the query is a training input. There is no evolved test mesh.

The independent dynamic counts are:

| Training inputs m | Training states | States including arbitrary-query decoder |
|---:|---:|---:|
| 2 | 5 | 13 |
| 3 | 9 | 36 |
| 9 | 54 | 783 |

The general counts are m(m−1)/2+2m and that number plus m^3. For one
input, identities reduce the entire dynamics further to one scalar, as
derived in the construction note. Static training coefficients require
O(m^4) storage and a direct evaluation uses O(m^4) operations. Computing
the Gaussian contractions and arbitrary-query coefficient functions has
a separate cost.

## Efficiency and applicability limits

This is a finite response expansion about initialization. Although it
captures the first feature-learning correction rather than freezing the
initial kernel, its test function lies in a finite span of initial response
coefficient functions. It is not a demonstrated escape from the limitations
of such spans for large feature movement. Its justification is the explicit
small-activity source bound, not a claim that initial response expansions
are universally expressive.

The O(a^5) error does not tend to zero by making coefficient integration
more accurate at fixed a. A useful arbitrary-order extension for a fixed
unit-label task remains open. Small initial Gram eigenvalues can make the
proved amplitude range very restrictive. No successful prediction on the
previous difficult tasks is claimed.

The displayed state counts can beat population sampling in the proved
regime. This does not establish an end-to-end runtime advantage. For
example, coefficient accuracy O(a^4) is needed to preserve O(a^5) output
accuracy. Plain Monte Carlo initialization can require O(a^-8) samples to
obtain that accuracy, although those samples are discarded rather than
evolved. An initial-data integration cost cannot be hidden by counting only
the subsequent ODE. Any comparison using population sampling error
O(a/sqrt(b)) is conditional on that sampling estimate and its variance
constants; it is not a finite-width theorem proved by the new note.

All accuracy statements compare with the same fixed-k block P1 target.
The separate errors from P1 memory compression and replacing fully dense
Gaussian initialization remain outside this new theorem.

## Checks and independent alternative

The mathematical audit rederived the tangent tensor, P1 lag error,
Gaussian weighted remainders, all-time feedback absorption and passive
decoder. No blocking error was found under the stated small-amplitude
hypotheses. This is an internal scoped audit, not a promotion review.

[cubic_scalar_algebra_check_20260930.py](cubic_scalar_algebra_check_20260930.py)
checks the same contractions using explicit finite matrices. It integrates
no ODE and trains no network. The initial tangent Gram, PSD completion and
decoder-derivative gaps were 1.11e-16, 6.80e-17 and 2.78e-17, respectively.
Halving a perturbation reduced the omitted kernel term by approximately
16, as required for its fourth-order remainder. The saved result is
`data/generated/structured_full_rank_scalar_20260926/cubic_scalar_algebra_20260930.json`.
These checks support algebraic correctness, not empirical accuracy of a
trained scalar surrogate.

A separate independent route,
[SUBLINEAR_ACTIVITY_ROUTE_20260930.md](SUBLINEAR_ACTIVITY_ROUTE_20260930.md),
proves a finite passive-memory construction with
O(epsilon^-1 log(1/epsilon)) modes when the unresolved kernel has a
computable positive relaxation spectrum of bounded mass. The route did not
derive that spectral property for P1. It is retained as a conditional
mechanism, not presented as a second successful P1 construction.

## Current answer to the broader research question

There is now a concrete, very small scalar response system with a proved
all-time approximation guarantee in a nontrivial but weak-feature-learning
regime. There is also a general terminal-stage reduction theorem explaining
why infinite physical training time need not require infinite scalar memory.

The strong-learning, efficient, arbitrary-accuracy version of the user's
question is not resolved. Neither the prior failures nor the new restricted
success proves a general impossibility or a general solution. The remaining
constructive obligation is specific: retain an affordable set of evolving
response information whose residual-weighted omission can be bounded over
large feature movement. Positive kernels and zero-loss stopping must be
preserved, but they do not replace that source bound.
