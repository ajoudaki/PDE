# Hybrid finite-width / DMFT mean-field campaign

## Frozen research contract

This campaign asks whether the canonical one-input, two-hidden-layer,
quadratic network has a regular deterministic output-coordinate kernel and,
if so, whether that kernel is compatible with the Stieltjes rational
hierarchy computed from the exact MFP jet.

The canonical finite-width model is

\[
z_i=n^{-1/2}\sum_jW_{ij}u_j^2,
\qquad
f_n=n^{-1}\sum_i a_i z_i^2,
\]

with independent standard-Gaussian initialization and ordinary label-one
squared-loss gradient flow.  No rank-one conditioning, clipping, stopped
median, fresh-noise substitution, or altered optimizer may replace the
ordinary ensemble in the primary Gaussian-width branch.

Four objects must remain distinct.

1. **Formal jet.**  The exact fixed-order MFP derivatives and their formal
   Stieltjes/Jacobi transforms.
2. **Practical prelimit.**  The observable finite-width curve over the tested
   range through width 8192.
3. **Bounded-readout matched limit.**  Finite networks and DMFT initialized
   from the same explicitly truncated readout law.
4. **Literal Gaussian width-first limit.**  The limit at fixed positive time
   with the unbounded Gaussian readout law, if it exists as a regular curve.

Evidence for one object does not identify another without an explicit
bridge.  In particular, an algebraic fit through width 8192 cannot certify
the literal Gaussian limit, and a finite-population DMFT cannot silently
stand in for an unbounded Gaussian expectation.

## Exact finite-width estimands

Let

\[
m_n(t)=\mathbb E f_n(t),
\qquad m_n(t_n(y))=y.
\]

The primary natural-loss estimand is

\[
K_{\mathrm{eff},n}(y)=
\frac{\mathbb E[(1-f_n(t_n(y)))K_n(t_n(y))]}{1-y}
=\frac{m_n'(t_n(y))}{2(1-y)}.
\]

The independent curve-aligned diagnostic uses each realization's normalized
progress toward the label:

\[
\widetilde K_n^{\mathrm{prog}}(y)=
\mathbb E\!\left[K_n(\tau_n^{\mathrm{prog}}(y))\right],
\qquad
f_n(\tau_n^{\mathrm{prog}}(y))
=f_n(0)+(1-f_n(0))y.
\]

For every realization with \(f_n(0)\ne1\), the right-hand side lies between
the initial output and the label and is reached along the monotone physical
flow whenever that flow is valid.  This avoids silently conditioning away
paths initialized above an absolute node.  Since \(f_n(0)\to0\), it has the
same proposed deterministic limit as the absolute output coordinate.

If a regular deterministic mean-field curve exists, both quantities must
converge to the same function.  Mean direct kernel at a common physical time
is retained only as an additional diagnostic.

At initialization the exact finite-width expectations are

\[
\mathbb E K_{a,n}(0)=27+288/n,
\quad
\mathbb E K_{W,n}(0)=36+384/n,
\quad
\mathbb E K_{u,n}(0)=48+672/n,
\]

and therefore

\[
\mathbb E K_n(0)=111+1344/n.
\]

These quantities may be used as preregistered or cross-fitted control
variates.  Their coefficients may not be chosen for agreement with the
Stieltjes proxies.

## Competing hypotheses

- **H-reg:** the bounded-readout network and correctly derived DMFT have a
  common regular limit; as the readout cutoff is removed, the output kernel
  and positive subtarget hitting times stabilize.
- **H-tail:** bounded-readout limits are regular, but removing the readout
  cutoff drives a Riccati/extreme-tail boundary layer, shrinking subtarget
  hitting times and preventing a regular unbounded-Gaussian curve.
- **H-num:** apparent disagreement is produced by width, sampling,
  discretization, response-kernel, or self-consistency error and cannot be
  interpreted scientifically.

The existing tagged-site Riccati analysis establishes H-tail only
conditionally on an unproved tagged-DMFT/finite-width identification.  It is
a live adversarial alternative, not an accepted theorem about the network
limit.

## Branch W: coupled float64 width ladder

The authorized production viability stage uses fresh, hash-bound float64
runs at

\[
(n,R)=(2048,16),(4096,16),(8192,16),
\]

with true counter-indexed common random numbers across widths and ordinary
antithetic readout pairs.  Width 1024 is represented only by the existing
validation-only artifacts and has zero fresh-run budget.  Width 16384 is a
held-out branch and is not authorized by this protocol.

The frozen output grid is

\[
0,\ .1,\ .25,\ .5,\ .75,\ .9,\ .95,\ .99.
\]

Nodes through .9 are inferential.  The .95 and .99 nodes are tail-sensitive
descriptive diagnostics and cannot authorize escalation by themselves.

The analysis must retain, without post-result selection:

- top-width/no-extrapolation;
- affine \(1/n\);
- affine \(1/\sqrt n\);
- leave-smallest-width sensitivity;
- paired adjacent-width bootstrap uncertainty;
- both primary kernel estimands above;
- raw and exact-initialization-controlled estimates.

An optional \(1/n+1/n^2\) fit may be reported only as a prespecified
sensitivity result; three widths cannot make it primary.

### Numerical gates

- float64 only;
- analytic-gradient/kernel regression against automatic differentiation;
- exact nested-array and antithetic identities;
- time-step halving on a preregistered subset;
- monotone mean output and nonincreasing mean loss;
- finite positive component kernels;
- no rank-one projection in the primary branch;
- failures and exclusions retained with hashes.

### Width-16384 authorization gate

Width 16384 remains closed unless all of the following hold under the exact
machine-readable definitions in the hash-frozen width child protocol.  The
resolution discriminator is evaluated at \(y=.9\); all nodes through .9
must still pass numerical and estimator-validity gates.

1. paired 4096-to-8192 corrections are statistically resolved;
2. estimator disagreement contracts with width;
3. leaving out width 2048 does not materially move the extrapolated band;
4. the frozen correction-model union is narrower than the accepted
   three-moment bracket
   \([162.239411,163.060383]\) at \(y=0.9\);
5. step error is below one quarter of the width-model union.

Failure of any gate closes width 16384 as inconclusive; it is not evidence
against the conjecture.

### Width budget

The cumulative viability budget is at most 3300 GPU wall-seconds of
successful or failed production points, with per-point caps 180, 720, and
2400 seconds for widths 2048, 4096, and 8192 respectively.  Validation and
compile time do not authorize extra production.  Width 16384 has zero budget
until the authorization gate is audited independently.

## Branch D: bounded-readout DMFT

The DMFT must be derived in discrete causal time before a continuous-time
implementation is trusted.  It must retain two representative populations,
two-time correlations, and reciprocal response/Onsager kernels generated by
reuse of the same initial middle-layer matrix.  A covariance-only
fresh-Gaussian closure is an explicit ablation, not an admissible DMFT.

The first scientific target uses cutoff \(A=3\) and the symmetric conditional law
\(a(0)\sim N(0,1)\mid |a(0)|\le A\), without variance renormalization, and
feature time only through output \(y\le0.5\).  The matched finite-width branch
must use exactly the same law.  Physical loss is reconstructed
afterward from

\[
T(y)=\int_0^y\frac{du}{2(1-u)K(u)}.
\]

### Mandatory pre-run gates

1. exact initialization decomposition \(27+36+48=111\) in the Gaussian
   limit and the corresponding exact truncated moments at finite \(A\);
2. a discrete response/contact derivation with a response-free ablation;
3. reproduction of exact MFP \(F^{(3)}(0)\) and \(F^{(5)}(0)\) in the
   Gaussian-limit audit, preferably \(F^{(7)}(0)\);
4. independent verification of \(F'=K\);
5. PSD covariance and causal-response checks.

No positive-time DMFT trajectory is scientific if these gates fail.

### Resolution ladder and stops

The predeclared possible numerical ladder is

\[
(L,S)=(64,2^{12}),\ (128,2^{14}),\ (256,2^{16}),
\]

where \(L\) is the time grid and \(S\) the effective population.  Only the
first point is initially authorized.  The second is authorized only if the
self-consistency residual contracts, population tails are stable, and all
pre-run gates pass.  The third has zero budget in this protocol; evidence
from the first two may only propose it under a new independently audited,
hash-frozen child protocol.  Stop after 30 self-consistency iterations at
any level whose residual fails to contract.

The initial DMFT compute budget is 600 wall-seconds.  A successful first
stage may authorize exactly one 1800-second run at \((128,2^{14})\); no
\((256,2^{16})\), unbounded-Gaussian, or \(y>0.5\) run is authorized here.

## Matched bridge and tail removal

The matched finite-width/DMFT comparison and the cutoff sequence
\(A\to\infty\) are conditional branches.  Passing both W and bounded D stages
does not execute them automatically: each requires a new independently
audited, hash-frozen child protocol with a new explicit budget.  The
Stieltjes predictions are kept blinded from solver tuning and
extrapolation-model selection.

Possible classifications are:

- **pass for bounded bridge:** independently valid bounded network and DMFT
  bands overlap under refinement;
- **tail support:** validated cutoff hitting times contract consistently with
  the conditional \(\log A/A\) mechanism;
- **regular support:** validated kernels and hitting times stabilize over a
  preregistered cutoff sequence;
- **inconclusive:** any numerical, response, tail, width, or bridge gate
  fails.

None of these finite experiments proves all-order Hankel positivity.  A
regular-support result would strengthen the global-identification evidence;
a validated tail-support result would disfavor the strongest global
Stieltjes-to-training identification while leaving the formal moment
conjecture intact.
