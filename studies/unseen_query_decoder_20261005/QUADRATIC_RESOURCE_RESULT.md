# Explicit compact memory with dense-budget construction and updates

2026-10-06. Constructive result under the current study's inherited dense
and physical-source certificates. The new implications passed an
[isolated mathematical review](QUADRATIC_RESOURCE_ISOLATED_REVIEW.md)
and a separate [isolated numerical review](QUADRATIC_NUMERICS_ISOLATED_REVIEW.md),
in addition to the scoped author cross-checks. These are internal checks
under the stated inherited interfaces, not fresh proofs of every source
theorem or promotion into the maintained book. No experiment or
implementation benchmark is asserted.

The expensive calibration is unnecessary. A new decoder uses the observed
history Grams and robust averages of streamed Gaussian-prior rows. Its
posterior row law is a proof device only: no density, normalizer, or fitted
distribution is calculated. Streaming rational support reduction also
replaces the exhaustive initialization search.

## Setup, comparison, and computational convention

Let \(n\) be dense hidden width, \(L\ge2\) fixed depth, and
\(0<\delta<1\) the failure probability. Keep the original independent
Gaussian initialization, zero readout, mean squared loss, block mobilities
\((n,1,\ldots,1,n)\), and nonlinear learning of every hidden layer.
The fixed training data have \(m\ge d\) inputs spanning
\(\mathbb R^d\), each of norm \(\sqrt d\). Keep the original positive
initial unweighted feature-Gram gap and full small-label condition. The
activations are strip analytic with the original bounded first derivative;
their values need not be bounded.

Write \(b_n(\delta)\) for the inherited dense-versus-independent-dense
upper error certificate displayed in [RESULT.md](RESULT.md). Every constant
\(C\) below may depend on the fixed dataset, \(m,d,L\), initial gap,
labels, activations, and confidence, but not on \(n\). None of the
displayed numerical logarithmic exponents depends on these parameters.
No small or polynomial fixed-parameter prefactor is being claimed.

Work uses the same prescribed activation/derivative and fixed-data
primitives as the dense comparison. The stated memory counts finite
numerical descriptions, retained randomness and arithmetic workspace,
but not the internal implementation of an externally provided primitive.
For fully charged bit complexity the primitive costs must be added, as
specified below. Analyticity alone is not a computational oracle theorem.

## Result

There is a randomized, present-state response model satisfying the
following deliberately conservative explicit resource bounds:

| Resource | Bound |
|---|---:|
| Total retained model information | \(C\log^{245}(en)\) bits |
| Retained model plus peak training or query workspace | \(C\log^{722}(en)\) bits |
| Complete initialization / warmup work | \(Cn\log^{1700}(en)\) |
| Peak temporary initialization memory | \(C[n\log^{108}(en)+\log^{600}(en)]\) bits |
| Work of all compact acquisition updates through the terminal patch | \(C\log^{1700}(en)\) |
| Work per unseen-input query | \(Cn\log^{2100}(en)\) |

The update bound excludes optional queries and bounds each individual
update as well. There is **no recalibration step** at initialization,
during training, or during querying. The preprocessing packet array is
discarded before compact evolution. Peak initialization memory is not
claimed to be polylogarithmic.

At every sufficiently large individual width, with probability at least
\(1-\delta\),

\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
|f_{\rm compact}(t,x)-f_n(t,x)|
\le 3b_n(\delta/256).
\tag{1}
\]

The event covers the entire sphere, all physical training times, and the
fitted endpoint; later adaptive query selection is allowed. No test input
or test label is required during preprocessing or training. Decoding reads
the current acquired summaries and stored seed, not a dense root, a table
of future answers, or a replay of the scalar training updates. The model
is autonomous in the same finite, clocked, restartable algorithmic sense
as the preceding construction, not an ordinary smaller gradient-flow net.

In particular the combined memory exponent can be taken as

\[
\boxed{k=722.}
\tag{2}
\]

This is an extracted upper bound, not an optimal exponent or a model
order to tune. The earlier finite-panel exponent five is not proved for
this unseen-sphere-input construction.

For each fixed admissible problem,
\(n\log^{2100}(en)=o(n^2)\). Consequently the initialization work,
every training update, and every query are eventually bounded by
\(O(Ln^2+dn)\), with the prescribed compact post-initialization memory.
The threshold includes all inherited conditions, the numerical and
probability conditions below, and these elementary cost comparisons.
It is unquantified and potentially enormous. The assertion is asymptotic;
it is not a useful dense-cost crossover at practical widths.

## Proof assembly

### 1. Counted physical and numerical compiler

The corrected short physical program has at most
\(C\log^8(en)\) named row fields and matrix calls, and at most
\(C\log^{16}(en)\) scalar history summaries. Its two-orientation
Gaussian conditioning uses matrices of dimension at most
\(C\log^{16}(en)\), with the explicit artificial noise floors.

[EXPLICIT_COMPILER_EXPONENT.md](EXPLICIT_COMPILER_EXPONENT.md) gives
a cached row/coefficient graph of size \(C\log^{56}(en)\), global
logarithmic sensitivity \(C\log^{58}(en)\), and scalar-history
amplification with logarithm \(C\log^{74}(en)\). At requested
precision \(b\), the complete row calculation has work
\(C(b+2+\log^{58}(en))^{16}\) and workspace
\(C(b+2+\log^{58}(en))^6\). Matrix inverses, roots, positive-part
projections, Sylvester solves and finite-precision resets are explicitly
counted; no matrix oracle or reciprocal-gap-length iteration is used.

### 2. Near-linear source generation and selection

[QUADRATIC_INITIALIZATION.md](QUADRATIC_INITIALIZATION.md) generates
the exact finite Gaussian row-source law using independent row packets,
empirical moments and small matrices. It does not form dense initialized
mixers. Matrix-answer noise, scalar-summary noise and finite arithmetic
are separate perturbations covered by the inherited physical coupling.

With \(P\le C\log^{16}(en)\) summaries, stream their rational row
contributions through affine support reduction, retaining at most
\(P+1\) positive weighted packets. One inserted point creates at most
one dependence. Ratio elimination deletes a support point, and an exact
integer-prefix/Cramer representation resets the remaining weights.
Thus their bit lengths are polynomial in \(P\), entry precision and
\(\log n\), rather than growing with the number of eliminations.
The weighted panel reproduces the implemented rounded source tape exactly.

Prefix and entry precisions \(C\log^{100}(en)\) dominate the
\(C\log^{74}(en)\) amplification. The row compiler then uses work
\(C\log^{1600}(en)\) and scratch \(C\log^{600}(en)\).
Source sweeps and support reconstruction take
\(Cn\log^{1616}(en)\) work; support reduction itself is bounded by
\(Cn\log^{428}(en)\). All subsequent weighted summary updates cost
\(C\log^{1632}(en)\) work. These imply the rounded exponents in
the resource table. The stored \(n\) source packets use
\(Cn\log^{108}(en)\) bits during warmup and are then discarded,
except for the selected panel.

### 3. No computed posterior law

[RECALIBRATION_FREE_MOMENTS.md](RECALIBRATION_FREE_MOMENTS.md) uses
the actual one-row marginal of the ideal summary posterior solely for
proof. Exchangeability and the entropy identity give both an
absolute-polylogarithmic full-array information bound and that bound
divided by \(n\) for one row, on one event for all prefixes.

The observed pair-moment tables, with a small explicitly chosen positive
buffer, dominate both the posterior-marginal and empirical Grams.
Whitened history marks therefore have second-moment matrices at most
identity. The change of coordinates preserves the mean exactly; the buffer
negligibly increases its norm bound and changes the variance. Section 10
of that note explicitly chooses the ridge and counts the enlarged
whitening graph: sensitivity degrees 58 and 74 are preserved, so
precisions 100 and 120 remain sufficient.
This argument is pointwise in every numerical prefix in the
certified error ball: it does not condition the posterior on privately
selected packets.

A statistical block of iid Gaussian-prior rows has small total variation
distance from the corresponding posterior-marginal product if its length
is at most a small constant divided by the one-row entropy bound.
Chebyshev under the latter law and this change of measure give constant
success probability under the readily sampled prior. Coordinatewise
medians of independent blocks amplify it. The algorithm estimates the
needed posterior moments without evaluating the posterior or its density.

The finite-rank Gaussian covariance correction costs root-width error.
Weak Gaussian moment propagation is Lipschitz in variance, so fixed-depth
nonlinearity amplifies the moment error only by a fixed logarithmic power,
not by successive square roots. The posterior-to-center interval argument
then gives, with the short-seed implementation below,

\[
2b_n(\delta/256)+C\log^{C_L}(en)/\sqrt n.
\tag{3}
\]

The error exponent \(C_L\) may depend on depth; none of the resource
exponents does. For fixed nonzero labels, the positive
\(\exp(CY^2\sqrt{\log(en)})\) factor in the inherited certificate,
where \(Y=\|y\|_2/\sqrt m\), eventually absorbs the logarithmic
remainder. This yields (1). Zero labels use the exact zero predictor.

### 4. One finite seed for every query and time

[SHORT_SEED_PRIOR_BLOCKS.md](SHORT_SEED_PRIOR_BLOCKS.md) supplies the
full numerical randomness interface. Quantized input, patch time and
guarded intermediate-moment contexts have log cardinality at most
\(C\log^{116}(en)\). Use that many statistical blocks and
\(C\log^{120}(en)\) Gaussian/arithmetic precision bits.
The Gaussian cutoff and discretization failure are small enough for the
entire finite-context union, and deterministic context rounding is handled
through the exact circuit, not continuity of a rounded median algorithm.

Nisan's verified block finite-state generator supplies one Gaussian row
per random block. Only \(C\log^{244}(en)\) state bits survive between
rows; the larger row-evaluation scratch is discarded. Its seed has
\(C\log^{245}(en)\) bits. Restarting it at another query means
another fixed-context one-pass test; no repeated-read PRG theorem is
assumed. A union of those tests covers the seed-dependent intermediate
contexts and all later adaptive inputs on one seed event.

The explicit row work and space exponents are 1920 and 720 at this
precision. Including every block, moment call, hash, median and counter
gives query work \(Cn\log^{2052}(en)\) and retained-plus-peak
workspace \(C\log^{722}(en)\). The resource table rounds the work
exponent up to 2100. The program/panel description needs at most
\(C\log^{156}(en)\) bits, including rational weight descriptions;
the seed consequently dominates total retained information.

### 5. Reference, probability, and endpoint

Warmup samples a fresh virtual source with the original dense Gaussian
law, independently of the requested dense reference. The dense-pair
certificate supplies a deterministic proof-only center. Both the
posterior interval argument for the virtual source and the actual
reference compare directly to this same center, giving (3) without
an extra dense-pair triangle radius. Neither the center nor a dense
reference realization is evaluated or stored.

For an explicit confidence allocation, assign failure at most
\(\delta/256\) to the virtual-source dense-center event and at most
another \(\delta/256\) in total to all other complete-source failures.
The posterior maximal inequality at threshold \(1/32\), including the
terminal reveal of source success, costs at most \(\delta/4\).
The entropy and conditional-noise maximal bounds cost \(\delta/8\)
each; the complete numerical-seed event costs at most \(\delta/4\).
The independent reference-center event costs \(\delta/256\).
Their sum is \(193\delta/256<\delta\), with all source and finite
sampling errors assigned to those stated groups. The conditional interval
losses use fixed small thresholds and change error constants, not this
outer probability sum.

Gaussian hybrid expectations are conditioned on the finite observable
transcript; restrictions inside them are transcript-measurable operator
and Gram events. Small realized matrix norms, dense-center success and
private acquisition success enter separate posterior failure bounds,
not an additional conditioning of the Gaussian matrix law.
Conditional query intervals are used to compare
deterministic centers at each point, not union-bounded over a continuum.
Completed time patches and the frozen fitting tail include every physical
time and the endpoint. The probability is joint over the dense reference,
virtual source and decoder seed, at each sufficiently large width, not
one event across infinitely many widths.

## Boundaries that have not disappeared

- Warmup may inspect the completed finite **virtual** source computation.
  This is still offline source-dependent compression, not a strictly
  online compressor starting before training.
- The new initialization theorem does not read a specified dense matrix
  realization and reproduce its particular trained trajectory. That
  stronger matched-root task would still incur the dense matrix actions
  in the supplied method. The guarantee here is exactly the random
  dense-reference upper-certificate scale, not near-\(1/n\) accuracy.
- Initialization workspace is allowed to be noncompact; all retained
  state and post-initialization peak workspace are compact and counted.
- Constants and width thresholds remain dependent on all fixed problem
  parameters and unquantified. Large explicit log powers do not imply a
  practical speedup.
- The activated primitive convention is unchanged. If a precision
  evaluator itself takes time \(T(b)\) and space \(S(b)\), add its
  calls at \(b=C\log^{120}(en)\): at most
  \(Cn\log^{188}(en)T(C\log^{120}(en))\) query work and
  \(S(C\log^{120}(en))\) extra peak space suffice. Initialization
  additionally costs at most
  \(Cn\log^{72}(en)T(C\log^{100}(en))\), and all compact updates
  at most \(C\log^{88}(en)T(C\log^{100}(en))\), with the
  corresponding single-call workspace added. Primitive outputs
  remain rounded to the counted finite interface. A fixed polynomial-time
  evaluator keeps eventual dense-scale work, but an absolute internal
  bit-space exponent uniform over arbitrary evaluator degrees is not
  supplied by analyticity.

These boundaries distinguish the proved asymptotic resource interface
from implementation efficiency and from a claim about exact compression
of an arbitrary given dense realization.

The author cross-checks are
[initialization and updates](QUADRATIC_INITIALIZATION_CHECK.md) and
[row compiler and short seed](SHORT_SEED_COMPILER_CHECK.md). The separate
isolated reports above specify their frozen input versions and dependency
boundaries. The numerical value 722 is derived from counted implementations;
it is not a numerical experiment or a claim of optimality.
