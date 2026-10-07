# Smaller complete decoder: checked improvement, fast-query target still open

2026-10-06. Current-study result, internally checked under the inherited
scientific inputs. This is not promotion into the maintained book.

The new Taylor-source construction uses logarithmic power **5** numerical
words for internal retained storage and peak post-initialization memory.
Those words have growing precision: the total internal memory is
logarithmic power **17/2 bits**,
so the absolute integer bit exponent **9** suffices. It accepts previously
unseen inputs and does not replay training. Its query bound still contains
a factor **n**. It therefore does **not** resolve the requested combination
of small storage and logarithmic query work.

The proof is [FAST_COMPOSITION.md](FAST_COMPOSITION.md). Its
[assembly reconstruction](FAST_COMPOSITION_CHECK.md) found no remaining
gap in the stated composition after the physical-noise and whole-sphere
cap corrections. That reconstruction was author-style, with disclosed
supervisory suggestions, not a blind independent review. The corrected
[Taylor source](FAST_TAYLOR_NOISE.md) and
[uniform-query component](FAST_UNIFORM_QUERY.md) have separate bounded
independent checks. All these checks retain the inherited source,
dense-center and random-generator theorems as inputs.
The subsequent [physical-query grid](FAST_PHYSICAL_QUERY_GRID.md), with
its [bounded independent check](FAST_PHYSICAL_QUERY_GRID_CHECK.md),
reduces query work further without changing the source or precision.

## Shared setup and accuracy

Use dense width n, m training inputs in dimension d, fixed depth L >= 2,
positive population feature-Gram gap gamma, label RMS
Y=||y||_2/sqrt(m), and confidence 1-delta. The m >= d training inputs
span R^d and have norm sqrt(d). The dense network has independent Gaussian
initial matrices, zero readout, mean squared loss, and block mobilities
(n,1,...,1,n). Every layer learns nonlinearly.

Keep the complete original source/dense/compact intersection of label
allowances. Its consequence 16Ym/gamma <= 1 is not a replacement for that
intersection. The known-zero-label case has the exact zero predictor.
Activations may be unbounded. For their supplied analytic strip width a,
the explicit envelope is

\[
 \beta=\max\left\{10,1+\max_{j\le L}|\phi_j(0)|,16/a,
 \max_{j\le L,\,k=1,2}
 \sup_{|\operatorname{Im}z|\le a/2}|\phi_j^{(k)}(z)|\right\}.
\]

Only one shared logarithm is needed:

\[
 Z=\log(en)+\log\!\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}{\delta}\right).
\]

The success event controls the worst prediction error over the **entire
sphere and physical training trajectory, including the fitted endpoint**.
The reference is an independently initialized dense run and the tolerance
is the inherited dense-pair **upper-certificate scale**, as in
[QUADRATIC_RESOURCE_RESULT.md](QUADRATIC_RESOURCE_RESULT.md). It is not
near-1/n fidelity to a specified dense realization, a guarantee relative
to the realized discrepancy of two particular runs, or merely a fixed-query
probability statement. Test inputs and their labels are not used at setup;
no test labels are used later either.

The state stores selected finite row packets, a coordinate metric, acquired
scalar training summaries, the current clock/coefficient information, and
query seeds. It is a response circuit, not an ordinary tiny neural network.
Training acquires summaries autonomously. Querying evaluates the current
response description without advancing that training recursion or retrieving
discarded dense weights. Setup may inspect the completed virtual source;
this is not a strictly online compressor or a proved practical training
speedup.

## Complete internal costs

These are **bits and bit operations**, not unit-cost real coordinates.
All O constants are universal. External evaluation and description costs
are explicit additions in the next section. The retained model size is

\[
 O\!\left(
 \beta^{710L}(m+d+2)^3(1+m/\gamma)^7 Z^{17/2}
 \right).
 \tag{1}
\]

The same bound includes peak memory during training and during one query.
It counts fixed arrays, all retained randomness, and live query scratch.

For comparison with the old model's scalar-coordinate convention, the
actual construction uses at most

\[
 O\!\left(\beta^{405L}(m+d+2)^2(1+m/\gamma)^4Z^5\right)
 \quad\text{finite numerical words}.
\]

Each word has up to
O(beta^(303L)(m+d+2)(1+m/gamma)^3 Z^(7/2)) bits. This is an explicitly
variable-precision word count, not a constant-bit machine-word or
unit-cost arithmetic claim. The derivation is direct: with the assembly's
actual word size w=CR Theta, its space is
O(R^2+(d+L+2)R Theta) words. Fixed bitstrings are packed into those finite
words, with ceilings/padding counted. No information is packed into an
arbitrary exact real. Total bits remain (1), and all work below remains
bit operations. The fifth-power word count cannot be substituted for (1).

**Initialization.** Generate the finite virtual source and build the model.
Its work and peak memory are, respectively,

\[
 O\!\left(n\beta^{1920L}(m+d+2)^8
                     (1+m/\gamma)^{19}Z^{23}\right),
 \tag{2}
\]
\[
 O\!\left(\beta^{910L}\left[
 n(m+d+2)^2(1+m/\gamma)^5Z^6
 +(m+d+2)^4(1+m/\gamma)^9Z^{11}\right]\right).
 \tag{3}
\]

**Training.** Perform all scheduled compact updates, excluding requested
queries. The total work is

\[
 O\!\left(\beta^{1720L}(m+d+2)^7
                     (1+m/\gamma)^{17}Z^{41/2}\right).
 \tag{4}
\]

This includes the finite source schedule and tail freezing; it is not
merely one vector-field evaluation with an uncounted integration step
number. There is no recalibration phase. Peak memory is (1).

**Querying.** Predict at one unseen sphere input using the current state.
The work is

\[
 O\!\left(\beta^{1720L}(m+d+2)^7(1+m/\gamma)^{17}
                         [nZ^{20}+Z^{41/2}]\right).
 \tag{5}
\]

Peak memory is (1). Multiple requested queries pay the sum of their work.
The one success event already covers adaptively chosen sphere queries.

For orientation only, fixing every problem parameter other than n gives
the following integer envelopes. The explicit parameter factors are
(1)--(5), not hidden new constants.

| Phase | Internal work | Peak internal memory, including model |
|---|---:|---:|
| Initialization | \(n\log^{23}(en)\) | \(n\log^6(en)+\log^{11}(en)\) |
| Training, all scheduled updates | \(\log^{21}(en)\) | \(\log^9(en)\) |
| Querying, one unseen input | \(n\log^{20}(en)+\log^{21}(en)\) | \(\log^9(en)\) |

The common prefactor convention in this orientation table is O with the
already displayed parameter factors. The bounds are eventually smaller
than quadratic dense-width work for fixed parameters; they do not give a
practical crossover width. The sample/gap powers 17 and 19 and activation
powers above remain large. They have not been relabelled as small constants.

## Evaluators, inputs and thresholds still count

A sufficient common activation/data precision and argument-length
allowance, denoted b in this paragraph, is

\[
 b=\left\lceil C\beta^{303L}(m+d+2)
                         (1+m/\gamma)^3 Z^{7/2}\right\rceil.
\]

Multiply the following call counts by the actual supplied evaluator work
at this precision and range:

| Phase | Activation/data calls, up to a universal factor |
|---|---:|
| Initialization | \(n\beta^{603L}(m+d+2)^3(1+m/\gamma)^6Z^{15/2}\) |
| Training, all updates | \(\beta^{804L}(m+d+2)^4(1+m/\gamma)^8Z^{10}\) |
| Querying, one input | \(n\beta^{505L}(m+d+2)^3(1+m/\gamma)^5Z^6\) |

Add one live evaluator workspace to peak memory and all retained evaluator,
input, and certificate descriptions to storage. Charge acquiring/verifying
certificates, obtaining query/time inputs, and writing outputs separately.
Bare analyticity does not provide a free finite-bit activation evaluator.
The phase-specific modular counts and precision derivation are in the
checked assembly, Sections 3--5.

Raw-label normalization needs b plus
ceil(log2(16 sqrt(m))) plus ceil(log2 max(1,1/Y)) fractional bits from
absolute-precision label access. The representation of the output scale Y
also counts. There is no internal unreported power of 1/Y, but these input
and output costs are not zero.

The theorem is at every sufficiently large **individual** width. Keep
all inherited scientific and deterministic width gates, including the
explicit nonzero-label and horizon conditions

\[
 nY\ge1,\qquad
 n\ge\max\{1,e^{-1}\sqrt{1+66\beta^{100L}m/\gamma}\}.
\]

The block-sampling gate is exactly (2) of the checked assembly. Its
statistical remainder must satisfy the original explicit eventual-width
comparison with the dense-pair certificate; merely writing
n^(-1/2+o(1)) would not prove that comparison. The inherited stochastic
threshold and that comparison's onset remain unquantified. No coefficient
in (1)--(5) is hidden in this threshold.

## Why the remaining query problem is substantive

The current decoder integrates nonlinear Gaussian response functions.
Time-history compression supplies a compact description of those functions;
it does not by itself supply a cheap integral. The checked sampler still
needs a width-scale number of rows, up to explicit logarithmic factors.
Calling that integral one operation would hide the principal cost.

[FAST_QUERY_STRUCTURE.md](FAST_QUERY_STRUCTURE.md) derives exact fast
Gaussian contractions for actual early feature-learning terms, and a
collective-statistic evaluator for one nonlinear learned-mean expression.
The same author investigation exhibits actual higher-order terms whose
natural correlated contraction graph grows with the order. It establishes
neither fast evaluation of the full trajectory nor a lower bound against
all possible decoders. The direct panel-extension and simple truncated
response-memory routes also remain incomplete for their previously
recorded reasons.

The new component and assembly checks close the smaller construction
above. They do not close the requested logarithmic-query theorem.

Two further routes were pursued without substituting their partial results
into the cost theorem:

- [FAST_LOCAL_PRECISION_TEST.md](FAST_LOCAL_PRECISION_TEST.md) quantizes
  the noisy scalar summaries. Gaussian boundary avoidance then lets a
  rounded selected metric reproduce the entire finite source tape
  **exactly**, with local metric precision. The complete finite source,
  Gaussian-law and passive-decoder precision bridges still need to fit
  one schedule before this can reduce the full cost table. Its
  [bounded independent check](FAST_LOCAL_PRECISION_CHECK.md) accepts
  that scoped replay lemma, not the full local-precision decoder.
- [FAST_QUERY_CONTROL_VARIATE.md](FAST_QUERY_CONTROL_VARIATE.md) tests
  the natural proposal to reuse training-pair moments as query control
  variates. An admissible nonlinear network leaves a fixed positive
  residual variance for this control family, even with its full training
  history. An exact Gaussian averaging rule repairs the particular
  missing periodic information but leaves the later nonlinear integral.
  This is an author-derived limitation of that control family, not an
  impossibility theorem for general decoders.

The research and rigorous-proof workflows were used to keep source lemmas,
conditional assembly, finite-bit accounting, and the unresolved fast-query
target separate. The canonical-notation workflow keeps the headline
parameter list fixed and numerical certificates local to their derivations.
