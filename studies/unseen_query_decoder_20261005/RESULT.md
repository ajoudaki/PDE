# Unseen-input decoding from a compact present state

## Latest resource strengthening

The newest checked parameter-explicit table is
[GAP_REFINED_PHASE_COSTS.md](GAP_REFINED_PHASE_COSTS.md). A real one-sided
gradient estimate lowers the algebraic sample/gap power in memory from
five to two, in initialization/all-training work from thirteen/twelve to
five, and in query preparation from ten to four. The streaming query term
has no algebraic sample/gap factor. Its
[source reconstruction](GAP_SOURCE_CHECK.md) and
[transport reconstruction](GAP_TRANSPORT_CHECK.md) pass under the listed
inherited interfaces. Bit memory remains logarithmic power six, numerical
words power five; query work still includes n. No new label restriction or
storage increase is introduced. The scientific width and dense-certificate
absorption onset remain potentially exponential and unquantified, and
general activation/data/certificate interfaces keep their explicit costs.
This is a bounded internal research result, not promotion.

The preceding parameter-explicit table is
[EXPLICIT_PHASE_COSTS.md](EXPLICIT_PHASE_COSTS.md). It removes an unnecessary
dimension factor from numerical precision and caches completed historical
coefficients, reducing query preparation from logarithmic power 29/2 to 12.
Memory remains logarithmic power six in bits, five in counted numerical
words. Initialization, all training updates, and one query each have explicit
time and peak-memory factors. Its precision and scheduling checks preserve
all source, label, input and error qualifications. The sufficient scientific
width and dense-certificate absorption onset are still not polynomially
controlled; arbitrary activation/data interfaces still need actual costs.

The preceding checked variant is
[FAST_LOCAL_EFFICIENCY_RESULT.md](FAST_LOCAL_EFFICIENCY_RESULT.md): retained
and peak post-initialization memory have logarithmic power **six in bits**,
or power **five in explicitly variable-precision numerical words**.
Query work is n times logarithmic power **four** plus preparation of
power **29/2**. Initialization work is n times power **31/2**, and all
compact updates together cost power **29/2**.
All major-parameter factors, finite-word precision, external evaluator
costs and inherited width/accuracy qualifications are stated there.
Its [bounded assembly reconstruction](FAST_LOCAL_ASSEMBLY_CHECK.md)
also checks a tanh evaluator whose costs fit these powers, while retaining
the other explicit input and certificate charges. Prior review context
is disclosed; this is not a fresh isolated promotion review.
It does **not** prove logarithmic query work or fifth-power total bits.

The preceding checked variant is preserved in
[FAST_EFFICIENCY_RESULT.md](FAST_EFFICIENCY_RESULT.md); its larger costs
are superseded by this local-precision, batched-query implementation.

The following resource paragraphs describe earlier variants, whose larger
bounds remain valid but are not the newest efficiency ledger.

Use [COST_CONTRACT.md](COST_CONTRACT.md) as the current cost-reporting
interface for both logarithmic methods. Every displayed resource `C` there
is universal. Actual activation/data evaluators, certificate acquisition,
tiny-label normalization, output-scale representation and query input are
charged separately. The panel memory schedule is now specified without a
quadratic quadrature-weight cache. Exact-real panel counts are not promoted
to a finite-bit, accuracy-certified numerical-training theorem.

The subsequent [parameter-explicit resource analysis](PARAMETER_EXPLICIT_RESOURCES.md)
exposes polynomial algorithmic factors in sample count, dimension and
inverse gap, under the same supplied activation/data interfaces. The
degrees are large, not three or four. It also gives a separately counted
exact-real initialization and runtime for the earlier finite-panel model.
It does not make the inherited stochastic success threshold or dense-error
onset polynomial, and does not promote real-coordinate panel counts to
finite-bit simulation bounds.

The current dense-certificate-scale resource result is
[QUADRATIC_RESOURCE_RESULT.md](QUADRATIC_RESOURCE_RESULT.md), completed
2026-10-06 under the inherited dense/physical source interfaces, with two
isolated internal checks. It gives explicit combined retained/peak
post-initialization memory exponent **722**, initialization work
\(Cn\log^{1700}(en)\), all compact update work
\(C\log^{1700}(en)\), and query work \(Cn\log^{2100}(en)\).
All are eventually within dense quadratic work; recalibration is eliminated.
Its whole-sphere/all-time error is \(3b_n(\delta/256)\), with the
benchmark defined below.

The new warmup samples an independent original-law virtual source and uses
streaming rational selection. It still inspects a completed finite source,
uses noncompact temporary warmup memory, and does not compress a specified
dense realization at near-\(1/n\) error. Fixed-parameter constants and
width thresholds remain unquantified. The logarithmic exponents use the
stated activation/data-primitive convention; evaluator costs are separate.

The remainder of this file records the earlier Fourier theorem and first
dense-budget variant, including their distinct sharper remainder and their
historical runtime limitations. Those runtime limitations are superseded
by the linked new construction **at the dense upper-certificate scale**;
the new result does not claim their literal \(2b_n+1/n\) error.

## Earlier constructions

2026-10-06. **An absolute-polylogarithmic retained-storage and decoding-space
construction is proved under the inherited dense certificates.** It decodes
unseen inputs from compressed current response information, without rerunning
the scalar training evolution. The complete argument has passed an isolated
internal reconstruction. This is not promotion into the maintained book.

The important limitation is upfront: preprocessing may run and inspect the
finite dense training computation. No preprocessing speedup or memory saving
is proved. The original Fourier decoder below can be extremely slow.
The new [dense-forward-budget variant](DENSE_BUDGET_RESULT.md) removes
that query-time limitation at the same dense-upper-bound error scale:
it uses absolute-polylogarithmic retained storage and peak query workspace,
and \(Cn^{3/2}\log^k(en)=o(n^2)\) primitive query work, for absolute
\(k\). Its guarantee is \(3b_n(\delta/256)\), not the original
literal \(2b_n(\delta/32)+1/n\). The unchanged setup and probability
qualifications apply; preprocessing remains expensive and the sufficient
width remains unquantified. Neither variant is an efficient end-to-end
training algorithm.

## Setup and guarantee

Keep dense width \(n\), fixed depth \(L\ge2\), \(m\ge d\) training
inputs spanning \(\mathbb R^d\) on the radius-\(\sqrt d\) sphere, and
the original labels. The network has the original independent Gaussian
initialization, zero readout, mean squared loss, and block mobilities
\((n,1,\ldots,1,n)\). The construction retains the original nonlinear
feature-learning dynamics; it does not replace them by initialized
features or a frozen kernel.

The activations remain real-valued on the real axis and analytic on a strip
with bounded first derivative there; activation values may be unbounded.
Retain the original positive unweighted initial feature-Gram gap
\(\gamma\) and the **full original small-label allowance**, without a new
smallness condition. Write \(Y=\|y\|_2/\sqrt m\) and let
\(0<\delta<1\) be the failure probability. Zero labels give the exact zero
predictor separately. The precise inherited physical/source assumptions are
listed in [the short-program proof](SHORT_CAUSAL_TRAINING_PROGRAM.md).

Throughout, \(C\) may depend on the fixed dataset, \(m,d,L,\gamma,Y\),
activations and confidence, but not on \(n\). The integer \(k\) below is
absolute: it does not depend on dimension, sample count or depth. This is
not a claim that the fixed-parameter prefactors are small or polynomial.

For clarity define the one reused error benchmark: the inherited
dense-versus-independent-dense upper certificate is

\[
b_n(\delta)=
\frac{CY}{\sqrt n}\exp\!\bigl(CY^2\sqrt{\log(en)}\bigr)
\sqrt{8\log\!\frac{8(n+1)(1+2n)^d}{\delta}}
+\frac{CY}{n}.
\]

Its constants have their inherited meaning; no sharper sample/gap
dependence is asserted here. The new compact model satisfies, with
probability at least \(1-\delta\),

\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
|f_{\rm compact}(t,x)-f_n(t,x)|
\le 2b_n(\delta/32)+\frac1n,
\]

while both its retained storage and its peak decoding workspace are at most

\[
C[\log(en)]^k.
\]

One event controls every sphere query and the entire physical trajectory,
including the fitted endpoint. Test inputs need not be declared during
preprocessing or training; no test labels are used. This is the existing
dense-variability **upper-bound scale**, not near-\(1/n\) matched-reference
accuracy and not a comparison to the realized discrepancy of a particular
pair of dense runs.

The statement holds at every sufficiently large individual width. Its
threshold may depend on all fixed problem parameters and remains
unquantified. It is not one event over infinitely many independent widths.
The construction is parameterwise, with supplied finite certified bounds
from the inherited estimates. A uniform compiler extracting those bounds
from arbitrary activation code and raw data is not claimed.

The displayed bound counts scalar registers using the fixed activation
evaluation primitives, as in the dense model. A bit-space version also
holds with counted polynomial-space precision interfaces for activations,
fixed data, and query/time inputs; its absolute exponent may depend on that
evaluation order. Bare analyticity alone cannot imply computability.
This numerical distinction is not an extra mathematical activation
restriction in the scalar-register theorem.

## What the compact model actually stores and does

It is a weighted response-circuit model, not an ordinary small neural net.
Its state consists of a selected set of Gaussian row packets and positive
weights, the already acquired scalar response summaries, and a finite
instruction circuit with a clock. All fixed marks, program parameters,
precision and decoding scratch count.

The selected packet count \(q\) and raw packet/history entries obey

\[
q\le C[\log(en)]^{16},\qquad
\text{raw packet/history entries}\le C[\log(en)]^{24}.
\]

These are not the complete workspace bound: numerical evaluation and
precision increase the absolute exponent. In particular, **this proof
does not give \(\log^5 n\)**. No numerical value of the complete
exponent \(k\) has yet been extracted and audited; it is a fixed
complexity exponent, not an order the user chooses. The
[explicit accounting](EXPONENT_ACCOUNTING.md) identifies the remaining
compiler-degree bookkeeping. The existence-of-an-absolute-exponent claim
is unchanged.

During compact evolution, weighted packet averages acquire the next scalar
response summary autonomously. Only acquired summaries are retained; there
is no table of future outputs and no width-\(n\) forward/backward history.
Preprocessing may depend on the completed finite source computation, so
this is not a strictly online compressor starting before source training.

At query time the summaries are fixed constants in the response circuit.
The decoder evaluates a conditional distribution for the new point and
returns a numerically certified approximate median. It integrates out
unretained row information using streamed Fourier integrals. It does not
retrieve dense weights, regenerate missing training summaries, or advance
the training recursion. Evaluating historical response functions at new
arguments is allowed and may require enormous computation; no efficient
query-time bound is asserted.

The clock selects a completed polynomial training patch. Its coefficients
are acquired at that patch's opening. After the terminal patch, the state
freezes and serves the fitted tail and endpoint. Thus autonomy here means
a finitely scheduled, restartable algorithm with a clock, not an asserted
smooth gradient-flow ODE.

## Why the proof closes

1. Analytic physical training and its fitting tail yield a causal nonlinear
   program with at most \(C\log^8(en)\) initialized matrix calls, uniformly
   accurate on the sphere through the endpoint.
2. Tiny hidden noise makes the exact two-orientation Gaussian conditioning
   formulas nondegenerate. They eliminate dense matrices in favor of iid
   row packets and a polynomial number of scalar moments. This is an exact
   finite-width law, not an assumed population limit.
3. Positive weighted selection compresses acquisition of those moments.
   A rational finite-precision construction avoids hidden exact-rank or
   infinite-precision weight assumptions.
4. The fixed-prefix conditional likelihood factors through a single-row
   Fourier integral raised to the \(n\)th power. Streaming the integrals
   and counted small-matrix routines gives the memory bound. Density guards
   make the numerical algorithm defined even off its success event.
5. The dense-pair theorem supplies a proof-only common center. A maximal
   inequality for the nested summary prefixes and robust posterior medians
   transfer its bound to every query and time on one event. No uncountable
   union of fixed-query error events is used.

The [complete statement and assembly](CURRENT_STATE_DECODER_CANDIDATE.md)
links every component proof. Its historical filename is retained for
traceability; it now contains the corrected final assembly.
The [isolated full-chain review](CURRENT_STATE_DECODER_FULL_REVIEW.md)
and [separate numerical check](FOURIER_ROW_PROGRAM_NUMERICAL_CHECK.md)
record the reconstructed claims and their qualifications.

## What remains open

The [earlier efficient-query continuation](EFFICIENT_QUERY_PROGRESS.md)
targeted time polynomial in the compact description; that stronger target
remains open. The later user-authorized dense-forward budget is now met by
the [streamed calibrated-moment decoder](DENSE_BUDGET_RESULT.md), whose
[complete assembly](DENSE_BUDGET_DECODER_CANDIDATE.md) retains the physical
scope, current-state interface and complete-trajectory/sphere norm. Its
numerical and probabilistic checks are linked there. The short nonlinear
response expansion is still not itself a compact evaluator.

The earlier exponent five for undeclared sphere queries, practical decoding
time, efficient or strictly online preprocessing, sharp fixed-parameter
prefactors and a numerical width threshold remain open. This construction
does not establish near-\(1/n\) matched-reference accuracy or a storage
lower bound. The earlier finite-panel theorem is neither retracted nor
extended by assertion.

This result supersedes the earlier open status through the finite-width
noisy-row and conditional-integral route. Earlier identities, failed
witnesses and partial results are preserved in
[HISTORICAL_ROUTE_RESULTS.md](HISTORICAL_ROUTE_RESULTS.md); their missing
population-limit bridge is not assumed by the new proof. No experiments,
implementation benchmark, Git mutation or maintained-book change were made.
