# Composition of the shorter source and the smaller decoder core

2026-10-06. Scoped author follow-up after the first freeze of
`SANE_DECODER_CORE.md`. The frozen core has SHA-256
`4174c39dc2f0fb89e3bc03559c6a88664e2305d7f3c5b583bcfa8b123ad33b2a`.
It is unchanged while under separate examination. This note adds final
dyadic weights and composes its candidate lemmas with
`SANE_INTEGRATED_COLLOCATION.md`, read completely, and the existing
`FINITE_PRECISION_SOURCE_SELECTION.md`, also read completely under the
supervisor's expanded scope. No experiment, Git operation, maintained
source edit or promotion occurred.

The resulting candidate counts are substantially smaller than the current
checked contract. They still do not prove `log^4` or `log^5` resources.
The worst remaining initialization term is the existing exact support
selection, not query integration or a matrix-function oracle.

## 1. Positive dyadic final weights

Let the exact rational selection produce `q <= P+1` weights
`p_1,...,p_q >= 0` with sum one. For an integer `b>=1`, set

\[
 \widehat p_j=2^{-b}\lfloor 2^b p_j\rfloor\quad(2\le j\le q),
 \qquad \widehat p_1=1-\sum_{j=2}^q\widehat p_j.           \tag{1}
\]

Every rounded weight is nonnegative, the sum remains exactly one, and

\[
 \sum_{j=1}^q|\widehat p_j-p_j|
   =2\sum_{j=2}^q(p_j-\widehat p_j)
   \le2(q-1)2^{-b}.                                     \tag{2}
\]

For `q=1` the exact weight is one and no rounding is needed. For any
bounded row test `|F|<=B_F`, equation (2) gives

\[
 \left|\sum_j\widehat p_jF(z_j)-\sum_jp_jF(z_j)\right|
 \le2B_F(q-1)2^{-b}.                                    \tag{3}
\]

Apply Lemma 1 of the frozen core to the complete weighted causal program.
Each convex-average phase acquires the additive error (3). There are at
most `C R` phases and its logarithmic amplification is `C R chi`.
Therefore `b=C R Theta`, with sufficiently large universal constant,
makes the induced error fit the existing retained-history and common-Gram
budgets. Here `Theta` is defined by equation (1) of the core, including
the logarithmic ridge, confidence and target-accuracy terms. This is the
same positive common-grid operation already allowed by the finite
selection note; it never divides by a selected weight.

The original exact common-denominator weights are used only during
construction and conversion (1). They are then discarded. Each retained
weight has `O(R Theta)` bits instead of `O(P R Theta)` bits. Actual
offline division of the exact integer descriptions is still charged to
initialization. This changes the retained base bound to

\[
 S_{\rm base}\le B_{\rm in}+C R^4\Theta,                 \tag{4}
\]

since the largest retained array is the `qD <= C R^3` selected packet
coordinates at `C R Theta` bits. Current histories, scalar noises,
dyadic weights, causal instruction templates and coefficient arrays are
smaller. Original data/evaluator descriptions retained by the decoder
are included in `B_in`, with their actual lengths.

## 2. Updated modular resource ledger

All quantities in this section retain the frozen core's definitions.
Let `Q <= C(L+1)` be the number of vector/scalar moment estimators per
query and `k <= d+1+C L R` its varying context dimension. The precision,
block and generator choices remain

\[
 p_a,p_{\rm ctx}\le C R\Theta,\quad
 w,J,F\le C(L+1)R^2\Theta,\quad
 A\le C(L+1)R^3\Theta,\quad E\le C\Theta.                 \tag{5}
\]

The ordinary query implementation stores its `J r_h` block means.
The optional implementation finds exactly the same dyadic medians by
threshold-search passes. Its accuracy follows from the same one-pass
bad-event tests, as proved in the core; no repeated-read generator
theorem is asserted.

The candidate internal bounds are

\[
\begin{array}{c|c}
\text{resource}&\text{bound apart from original interfaces}\\\hline
\text{retained bits}&B_{\rm in}+C[R^4\Theta+(L+1)R^3\Theta^2]\\
\text{retained plus peak, stored medians}&
 B_{\rm in}+C(L+1)^2R^5\Theta^2\\
\text{retained plus peak, threshold-search medians}&
 B_{\rm in}+C(L+1)[R^4\Theta+R^3\Theta^2]\\
\text{one query, stored medians}&C n(L+1)^6R^{11}\Theta^5\\
\text{one query, threshold-search medians}&C n(L+1)^7R^{14}\Theta^6.
\end{array}                                               \tag{6}
\]

The peaks include the retained model, coefficient preparation, matrix
scratch, current context, row packets, all actually retained block
means, hash scratch and stored seed. They do not count a proof-test
space bound as the decoder's actual workspace.

For clarity the remaining initialization and acquisition costs can also
be exposed under the same candidate core. The unchanged exact streaming
selection has

\[
 W_{\rm select}\le Cn(P+2)^8v_a^3\le CnR^{19}\Theta^3,
 \qquad
 S_{\rm select}\le C(P+2)^3v_a\le C R^7\Theta,            \tag{7}
\]

where `v_a=O(R Theta)` includes source entry precision and `log n`.
Rounding the final weights costs less than (7): there are at most
`P+1` divisions of integers with `O(P v_a)` bits. No exact intermediate
selection representation is omitted from peak initialization memory.

Source sweeps and reconstruction scan at most `nP` packet-stage pairs.
At each pair the prepared row graph costs `C R^2p_a^2` bit operations.
Coefficients depend only on already committed scalar arguments, so one
retains their numerical vectors and computes each new conditioning
coefficient once when its fields become available. The total coefficient
preparation is at most `C(R^5p_a^2+R^4p_a^3)`.
Generating all `nD+P` Gaussian packet/noise coordinates costs at most
`C(nD+P)p_a^4` by the finite sampler lemma. These observations give

\[
 W_{\rm init}\le
 C\{nR^{19}\Theta^3+(nR^5+R^6)\Theta^4\},               \tag{8}
\]
\[
 S_{\rm init}\le B_{\rm in}
 +C\{nR^2\Theta+R^7\Theta+(L+1)R^3\Theta^2\}.           \tag{9}
\]

The `nR^2Theta` term is the temporary full packet array. Its noncompact
size is allowed only during initialization, as in the original contract.
The seed is generated once independently of the completed source and
remains explicitly in (9).

For all compact acquisition updates, there are `Pq <= C R^4`
packet-stage evaluations. Their dyadic-weighted sums use a common grid
with `C p_a` bits, including accumulator integer positions. Their work
is bounded by the row evaluations. Incrementally prepared coefficients
give

\[
 W_{\rm updates}\le C(R^8\Theta^2+R^7\Theta^3).           \tag{10}
\]

The scalar histories and their old coefficients are immutable after
creation. That is what makes incremental preparation valid; this
schedule does not revise old field definitions from a later prefix.
Equation (10) counts every scheduled acquisition update through the
terminal patch, not one field evaluation or one training step.

The source/updated rows use at most `C R` activation or derivative calls
per packet-stage. Actual additional evaluator/data work is therefore

\[
\begin{split}
 &C nR^3 T_{\phi,\rm data}(C R\Theta)
                                     &&\text{initialization},\\
 &C R^5 T_{\phi,\rm data}(C R\Theta)
                                     &&\text{all updates},\\
 &C n(L+1)^2R^3\Theta\,
         T_{\phi,\rm data}(C(L+1)R^2\Theta)
                                     &&\text{stored-median query},\\
 &C n(L+1)^3R^6\Theta^2\,
         T_{\phi,\rm data}(C(L+1)R^2\Theta)
                                     &&\text{threshold-search query}.
\end{split}                                              \tag{11}
\]

Fixed input values and current query coordinates are prepared once to
their required precision and retained in the counted data/context arrays;
they are not fetched afresh for every multiplication. Add their actual
acquisition work and descriptions. Their preparation call counts fit
the displayed safe evaluator allowances. Add a single evaluator's peak
scratch to each phase, together with actual certificate, input/time, and
output-format costs. These additions are not universal constants.

## 3. Compatibility of the shorter collocation source

`SANE_INTEGRATED_COLLOCATION.md` changes the step size using the proved
operator bound

\[
 \left\|\int_0^s I_K b(u)\,du\right\|
        \le\frac{\pi}{2\sqrt2}\max_j\|b_j\|<2\max_j\|b_j\|.
\]

It keeps the same Chebyshev-root nodes, finite Picard chronology,
positive endpoint weights, normalized state, cap identities and fitted
tail. With `h=min(r_tau/4,1/(8 Lambda))` the node contraction is at
most `1/4`. This replaces the old stricter contraction constant but
still gives a geometric perturbation sum bounded by a universal number.
The endpoint recurrence remains
`e_next <= (1+2h Lambda)e + local_error`, so the accumulated factor
is bounded by `exp(2 Lambda T)` since the step lengths sum to `T`.

The physical matrix-noise allocation from
`PHYSICAL_PARAMETER_ACCOUNTING.md` already pays for `Lambda T`, the
desired `n^(-10)` margin, and the explicitly bounded field perturbation
from matrix-answer noise. Consequently increasing its universal constant
retains that allocation for this source: no new inverse power of the
step size or of the interpolation degree is introduced. The fresh
Gaussian RMS failure union uses the new actual call count `R`, which
only decreases under the displayed upper envelope.

The two-orientation Gaussian formulas require a finite predictable
sequence of matrix queries. At Picard iteration `j+1`, all arguments
are functions of the previous iteration and already observed quantities.
The new step size and fixed iteration count preserve predictability.
Old fields still retain their old scalar arguments. Thus the same row
packet/source law and the same exchangeable noisy-summary likelihood
have the same hypotheses. The positive dyadic panel is compared
deterministically to the ideal continuous-noise summary law; that ideal
law is not replaced by the rounded acquisition law inside the posterior
argument.

The query's raw Grams, positive floor, whitening, bounded mean mixers,
and guarded moment recurrence are unchanged mathematical functions.
The spectral algorithm evaluates these functions to their allocated
errors. It uses no new approximation to the physical Gaussian covariance.
The low-entropy product-block lemma therefore retains its original
product-law hypothesis for the iid baseline. The one-pass median tests
transfer that baseline as in the core without replacing it by a
pairwise-independent law.

These checks are the precise conditional interface substitution. They
do not independently prove the inherited stochastic source/fitting
events, their thresholds, the physical passive-query cap, or the final
comparison of the statistical logarithmic remainder with the dense-pair
certificate. Those assumptions remain visible exactly as in the cost
contract. Fresh review of the new deterministic lemmas is still required.

## 4. Major-parameter substitution

Let `ell=log(en)` and use the cost contract's larger

\[
 Z=\ell+\log\!\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}{\delta}\right).
\]

The fixed normalized accuracy exponent ten changes only universal
constants in this `Z`. The shorter physical source and existing
logarithmic numerical certificate give

\[
 R\le C\beta^{301L}(m+d+2)(1+m/\gamma)^3 Z^{9/2},
 \qquad
 \Theta\le C\beta^{200L}(1+m/\gamma)Z^2.                 \tag{12}
\]

The factor `L` in the physical call count was bounded explicitly by
`beta^L`; no problem-dependent constant is hidden here. All powers in
the following table follow from (6)--(12). Multiply each non-input row
by the same universal `C beta^(7000L)`; add the supplied interfaces.

| Resource | Remaining factor |
|---|---:|
| Retained bits | `(m+d+2)^4 (1+m/gamma)^13 Z^20` |
| Retained plus peak with stored medians | `(m+d+2)^5 (1+m/gamma)^17 Z^(53/2)` |
| Retained plus peak with threshold-search medians | `(m+d+2)^4 (1+m/gamma)^13 Z^20` |
| Initialization work | `n (m+d+2)^19 (1+m/gamma)^60 Z^(183/2)` |
| Peak initialization bits | `n (m+d+2)^2 (1+m/gamma)^7 Z^11 + (m+d+2)^7 (1+m/gamma)^22 Z^(67/2)` |
| All compact updates | `(m+d+2)^8 (1+m/gamma)^26 Z^40` |
| One query with stored medians | `n (m+d+2)^11 (1+m/gamma)^38 Z^(119/2)` |
| One query with threshold-search medians | `n (m+d+2)^14 (1+m/gamma)^48 Z^75` |

For verification, a factor `(L+1)^j R^u Theta^v` contributes powers

\[
 (m+d+2)^u(1+m/\gamma)^{3u+v}Z^{(9/2)u+2v}
\]

and activation exponent at most `(j+301u+200v)L`, up to universal
constants. The largest displayed exponent is the selection term's
`(301*19+200*3)L=6319L`, below the common `7000L`.
Terms with lower physical-parameter powers in (8)--(10) are dominated
directly by the corresponding displayed envelope, since all displayed
bases are at least one; no parameter cost is moved into a width
threshold.

Sufficient ordinary source and query precision/argument allowances are

\[
 b_a\le C\beta^{501L}(m+d+2)(1+m/\gamma)^4Z^{13/2},
\]
\[
 b_q\le C\beta^{803L}(m+d+2)^2(1+m/\gamma)^7Z^{11}.       \tag{13}
\]

Choose the constants large enough for the local error allocations. Actual
evaluator costs are obtained from (11) at these precisions. In particular
an arbitrary evaluator's work or scratch cannot be hidden inside the
factor `beta^(7000L)`.

There is no internal inverse-label polynomial. The raw-label precision
to obtain normalized labels still needs the explicit additional
`log_2 max(1,1/Y)` and `log m` positions in the cost contract. The
output scale and input certificates retain their actual acquisition and
representation costs. The exactly known `Y=0` case uses the zero model.

The explicit sampling-width condition remains
`n >= 512 max(K_*,1)` for the chosen entropy certificate, along with
the original source and statistical-comparison conditions. Reducing
`R` or scalar-noise precision improves the numerical certificate but
does not make the inherited stochastic threshold effective.

## 5. Meaning of the improvement

The original mathematical activation and label classes are preserved.
Uniformity still concerns all sphere inputs, all physical times and the
fitted endpoint on one inherited source/seed event. The model's seed is
repeatable, and queries use current summaries and row functions without
replaying scalar training. The whole source is used offline only as
already permitted by the original contract.

The candidate logarithmic powers 20, 53/2, 40, 119/2, 75 and 183/2
are actual algorithmic bit counts under the supplied interfaces, not a
renaming of a large parameter or an exact-real reinterpretation. They
remain large. The stored packet array alone contains `qD` entries
under this selected-row representation; changing that representation,
or greatly reducing the physical history, is still necessary to reach
the user's fourth- or fifth-power target. These counted costs are upper
bounds and do not establish a lower bound on other admissible models.

Status: internally derived conditional composition, awaiting fresh
independent reconstruction of the frozen core and the shorter-source
lemma. The checked `COST_CONTRACT.md` has not been changed. This note
does not report a completed low-exponent solution or a practical
dense-cost crossover.
