# Local-precision decoder: smaller memory and batched unseen queries

2026-10-06. Lead-author synthesis, internally checked under the inherited
scientific and finite-generator interfaces. The source, passive transport,
and complete resource assembly have passed bounded reconstruction.
This is not promotion into the maintained book.

The [assembly check](FAST_LOCAL_ASSEMBLY_CHECK.md) reconstructs the complete
pair schedule, finite prior, batched estimator, seed and scratch memory,
parameter powers, and tanh implementation. It discloses prior component
review context; it is not a fresh isolated review. The frozen component
drafts retain their pre-review status wording. This synthesis and the
dated checks give the current status without changing their frozen proofs.

The construction has logarithmic power **six in internal bits**, including
retained randomness and peak working memory during training and querying.
It has logarithmic power **five in finite numerical words**, whose bit
length is explicitly counted. Batched query moments reduce the internal
query work to width times logarithmic power **four**, plus logarithmic
power **29/2** preparation. It uses no training replay.

This does **not** resolve logarithmic query time. Nor do the parameter
powers below imply a practical crossover width. The previous complete
variant is preserved in [FAST_EFFICIENCY_RESULT.md](FAST_EFFICIENCY_RESULT.md).

## Shared setting and guarantee

The parameters are dense width \(n\), number of training examples \(m\),
input dimension \(d\), fixed depth \(L\ge2\), positive initial population
feature-Gram gap \(\gamma\), label RMS \(Y=\|y\|_2/\sqrt m\), and
failure probability \(\delta\). The \(m\ge d\) training inputs span
\(\mathbb R^d\) and lie on the radius-\(\sqrt d\) sphere. The dense
model has independent Gaussian initial matrices, zero readout, mean
squared loss, and mobilities \((n,1,\ldots,1,n)\). All layers learn;
no initialized-feature or frozen-kernel replacement is made.

Keep the full original intersection of source, fitting, and compact-model
label conditions. The consequence \(16Ym/\gamma\le1\) is not a
replacement for that intersection. If all labels vanish, the predictor
is exactly zero. Otherwise retain the stated nonzero-label width gates.

Activations are analytic in their supplied strip, with bounded first and
second derivatives on the half-strip; their values need not be bounded.
For a common strip width \(a\), define the same explicit envelope

\[
 \beta=\max\left\{10,1+\max_{j\le L}|\phi_j(0)|,16/a,
 \max_{j\le L,\,k=1,2}
 \sup_{|\operatorname{Im}z|\le a/2}|\phi_j^{(k)}(z)|\right\}.
\]

Use one shared logarithm:

\[
 Z=\log(en)+\log\!\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}{\delta}\right).
\]

At every sufficiently large individual width, the success event controls
the worst prediction error over the entire sphere and the entire physical
training trajectory, including the fitted endpoint. The comparison is to
an independently initialized dense run at the inherited dense-pair
**upper-certificate scale**. It is not near-\(1/n\) approximation of a
specified initialized run, or a guarantee relative to the actual realized
discrepancy of two runs. Test inputs are unseen until querying. No test
labels are needed at any stage.

The retained model is a finite response circuit: selected row packets,
a coordinate metric, acquired scalar summaries, present clock/coefficient
information, and query seeds. Its training updates are autonomous. A query
uses this present state without rerunning the scalar training recursion.
Initialization may inspect the completed virtual source; this is not
strictly online compression.

## Explicit internal costs

The units are bits and bit operations. All suppressed multiplicative
constants are absolute. Activation/data evaluation and description costs
are additional, explicitly charged below.

The final model size, also bounding peak memory during training and one
query, is

\[
 O\!\left(\beta^{530L}(m+d+2)^3(1+m/\gamma)^5 Z^6\right).
 \tag{1}
\]

The numerical-word count is at most
\(O(\beta^{410L}(m+d+2)^2(1+m/\gamma)^4Z^5)\), with
at most \(O(\beta^{110L}(d+1)(1+m/\gamma)Z)\) bits per word.
This does not assert constant-bit words or unit-cost real arithmetic.
Fixed bitstrings use finite packing only; their bits are included in (1).

**Initialization — generate the source and build the model.** Work:

\[
 O\!\left(n\beta^{1340L}(m+d+2)^8
                  (1+m/\gamma)^{13}Z^{31/2}\right).
 \tag{2}
\]

Peak memory:

\[
 O\!\left(\beta^{730L}\left[
 n(m+d+2)^2(1+m/\gamma)^3 Z^{7/2}
 +(m+d+2)^4(1+m/\gamma)^7 Z^{17/2}\right]\right).
 \tag{3}
\]

**Training — perform all scheduled compact updates.** Total work,
excluding requested queries:

\[
 O\!\left(\beta^{1230L}(m+d+2)^7
                   (1+m/\gamma)^{12}Z^{29/2}\right).
 \tag{4}
\]

This counts the complete finite update schedule and tail freezing, not
only one vector-field evaluation. There is no uncounted integration step
number or separate recalibration phase. Peak memory is (1).

**Querying — predict at one unseen input using the present state.** Work:

\[
 O\!\left(
 n\beta^{450L}(d+1)^4(1+m/\gamma)^4 Z^4
 +\beta^{1230L}(m+d+2)^7(1+m/\gamma)^{12}Z^{29/2}
 \right).
 \tag{5}
\]

Peak memory is (1). Multiple queries pay the sum of their work; the same
success event already covers adaptively chosen sphere queries.

For orientation only, fixing the other parameters gives these integer
width envelopes. The omitted factors are precisely the explicit ones
above, not newly hidden parameter constants.

| Phase | Internal work | Peak internal memory, including model |
|---|---:|---:|
| Initialization | \(n\log^{16}(en)\) | \(n\log^4(en)+\log^9(en)\) |
| Training, all updates | \(\log^{15}(en)\) | \(\log^6(en)\) |
| Querying, one unseen input | \(n\log^4(en)+\log^{15}(en)\) | \(\log^6(en)\) |

## Evaluators, input precision, and width qualifications

In this paragraph alone write \(b\) for the common sufficient precision
and argument-length allowance:

\[
 b=\left\lceil C\beta^{110L}(d+1)(1+m/\gamma)Z\right\rceil.
\]

Multiply each following call count by the actual work of the supplied
activation/data evaluator at that precision and range:

| Phase | Activation/data calls, up to an absolute factor |
|---|---:|
| Initialization | \(n\beta^{603L}(m+d+2)^3(1+m/\gamma)^6Z^{15/2}\) |
| Training, all updates | \(\beta^{804L}(m+d+2)^4(1+m/\gamma)^8Z^{10}\) |
| Querying, one input | \((L+1)[n+\beta^{402L}(m+d+2)^2(1+m/\gamma)^4Z^5]\) |

Add one live evaluator workspace to the peak-memory bounds and all
retained evaluator, input, scale, and certificate descriptions to model
storage. Charge certificate acquisition/verification, obtaining query/time
inputs, and output writing separately. Bare analyticity supplies no
finite-bit activation-evaluation complexity bound in terms of \(\beta\)
alone. Gaussian sampling and its finite inverse-CDF arithmetic are already
counted internally, not offered as free primitives.

For \(\phi_j=\tanh\), a
[direct certified evaluator](FAST_TANH_EVALUATION.md) uses \(O(b^3)\)
bit work and \(O(b)\) scratch. Multiplying by the activation call counts
above stays within (2), (4), and (5); its workspace stays within the
memory bounds. Thus no larger powers are needed for tanh evaluation.
Data access, certificates, descriptions, scale handling, and input/output
remain charged separately. This specialization does not assert that an
arbitrary allowed analytic activation has the same evaluation complexity.

For absolute-precision raw-label access, normalization needs \(b\) plus
\(\lceil\log_2(16\sqrt m)\rceil\) plus
\(\lceil\log_2\max(1,1/Y)\rceil\) fractional bits. The output scale
\(Y\) and writing the scaled prediction also count. Thus there is no
hidden internal power of \(1/Y\), but tiny-label input costs are not
declared zero. The complete external-interface conventions remain those
of [COST_CONTRACT.md](COST_CONTRACT.md).

Retain all original scientific width conditions, as well as

\[
 nY\ge1,\qquad
 n\ge\max\{1,e^{-1}\sqrt{1+66\beta^{100L}m/\gamma}\}.
\]

The block-sampling gate and the enlarged statistical remainder are
specified in [the resource assembly](FAST_LOCAL_COMPOSITION.md) and
[the passive proof](FAST_FINITE_PASSIVE.md). They are not dropped when
the blocks are shortened. Absorbing the extra fixed-power logarithmic
remainder into the dense-pair certificate uses its inherited eventual-width
comparison. The stochastic threshold and the onset of that comparison
remain unquantified. These are fixed-problem width asymptotics, not uniform
guarantees for labels or data varying with width.

## Why the improvement works, and what remains unresolved

The source and the compact model now reproduce the same quantized scalar
training tape exactly on the success event. Physical source errors are
handled locally, so precision need not pay for the sensitivity of an
expanded history circuit. At a new input, old row marks are evaluated by
the exact same finite interpreter; only the new passive operations need
local numerical approximation.

All block moment vectors are accumulated together. Their temporary array
fits the existing memory allowance and avoids repeated packet passes.
The prescribed statistical block length is charged explicitly. This is a
time-saving schedule for the existing estimator, not a claim that a
high-dimensional Gaussian integral is one operation.

The checked components are [finite-source transport](FAST_FINITE_SOURCE_BRIDGE.md),
[exact finite replay](FAST_LOCAL_PRECISION_TEST.md),
[finite posterior bookkeeping](FAST_FINITE_POSTERIOR.md), and
[passive unseen-query transport](FAST_FINITE_PASSIVE.md). Their bounded
checks are [source](FAST_FINITE_SOURCE_CHECK.md),
[replay](FAST_LOCAL_PRECISION_CHECK.md),
[posterior](FAST_FINITE_POSTERIOR_CHECK.md), and
[passive](FAST_FINITE_PASSIVE_CHECK.md). The passive
review found and corrected the distinction between population error and
the larger vector sampling error. That correction is retained explicitly.

The main remaining gap is a fast evaluator of the complete nonlinear
query expectation. [Exact Gaussian contractions](FAST_QUERY_STRUCTURE.md),
[training-moment controls](FAST_QUERY_CONTROL_VARIATE.md), and the
[correlated multilevel recurrence](FAST_MULTILEVEL_QUERY.md) supply partial
mechanisms and scoped failures. They neither extend to a logarithmic-work
decoder for the full class nor prove that such a decoder is impossible.
The multilevel recurrence, in particular, is not a substitute for the
full learned trajectory.

The research and rigorous-proof skills were used to separate the proved
interfaces from the unresolved query target; canonical notation keeps
the headline parameters shared and temporary proof symbols local.

After the assembly check, only the status/link passages and its already
checked tanh specialization were added to this synthesis. Equations
(1)--(5), parameter definitions, evaluator counts, and width/accuracy
qualifications are unchanged from the checked synthesis hash recorded
in FAST_LOCAL_ASSEMBLY_CHECK.md.
