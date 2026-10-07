# Streamlined exact-query compression: words, width, and implementation

2026-10-07. Current-study synthesis. The refinements below retain the
scientific component boundaries of `TWO_GAP_CLOSURE_RESULT.md`; they are
not a new independent proof of those components or promotion into the book.
The separate reconstruction reports are linked at the end. This note
supersedes the earlier resource presentation, not its scientific assumptions.

**Outcome.** Report numerical words and word operations, with sufficient
precision stated separately. Exact generator streaming, cached metric
products, and indexed spectral pivots reduce actual work. Separate member
confidence from reference confidence. Replace the sufficient source-width
power 20,000 by 1,100, or use its sharper factorized form. None of these
changes supplies a practical onset, ordinary-machine-precision guarantee,
or measured GPU speedup.

## 1. One setup and notation

Keep dense width \(n\), training count \(m\), dimension \(d\), fixed
hidden depth \(L\ge2\), population feature-Gram gap \(\gamma>0\),
label RMS \(Y=\|y\|_2/\sqrt m\), and failure allowance
\(0<\delta<1/4\). Training inputs span \(\mathbb R^d\), have norm
\(\sqrt d\), and \(m\ge d\). The Gaussian initialization, zero
readout, mean-square loss, mobilities \((n,1,\ldots,1,n)\), and nonlinear
learning in every hidden layer are unchanged.

The analytic activation class permits unbounded values. For its common
strip width \(a\), retain

\[
 \beta=\max\left\{10,1+\max_j|\phi_j(0)|,16/a,
 \max_{j,\,r=1,2}\sup_{|\operatorname{Im}z|<a/2}
                       |\phi_j^{(r)}(z)|\right\}.
\]

Retain the **complete original intersection of fitting and source label
conditions**, with the same finite recurrences in
`FULL_FINITE_SOURCE_PROBABILITY.md`, Section 1. It is not replaced by a
smaller convenient power cap. The present refinement introduces no new
scientific restriction on positive \(Y\). At \(Y=0\), the predictor
is exactly zero and the nontrivial construction is unnecessary.

Only two extra recurring resource quantities are needed:

\[
 p=\max\left\{1,\left\lceil
 \frac{\log(2^{22}emL)}{\log(64e^2)}\right\rceil\right\},
 \qquad
 Z=\log(en)+\log\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}\delta\right).
 \tag{1}
\]

The moment order \(p\) is for implemented source members and has **no
\(\delta\)**. Reference confidence still enters the width condition
below. For the clean resource table take \(nY\ge1\), exactly as before;
Section 4 retains the small-positive-label alternative.

Every suppressed multiplicative constant in resource bounds is universal.
No \(n,m,d,\gamma,Y,L,\beta,\delta\) dependence is put inside it.
Activation-evaluation and external-description costs are explicitly separate.

## 2. The method in three phases

1. **Initialization.** Generate a finite virtual source from its generated
   member block, independently of the dense reference, and inspect its
   completed finite training computation. Select original row
   packets and a small positive metric reproducing its required empirical
   inner products to the prescribed accuracy. Retain those packets, the
   metric, scalar noise marks, finite instructions and short seeds. Discard
   the full row table and completed future-answer table. Repeat sequentially
   for the whole-source ensemble.
2. **Training.** Advance the selected packets and scalar state using the
   retained metric. Cache each already-created selected field and its metric
   product. Fields keep their creation-time scalar arguments. On the replay
   event the finite scalar acquisitions equal the source's acquisitions;
   future answers are not stored in the running state.
3. **Querying.** From the current state and seeds, regenerate the source's
   rows in order. Stream the empirical contractions for the unseen input
   and keep the full conditional covariance correction in both matrix
   orientations. Prepare coefficients once per context, use a constant
   number of passes per layer, and take the median across complete sources.
   This evaluates row instructions; it does **not** rerun scalar training.

No test input or test label is needed in advance. Setup remains offline:
it may inspect completed virtual training. It does not compress an arbitrary
specified dense weight realization into a seed. The accuracy comparison is
to an **independent** dense reference drawn with the original initialization.
No dense-weight oracle or uncounted trajectory archive is retained.

The main exposition no longer needs the abandoned high-dimensional
quadratures, passive population estimator, entropy route, or repeated passive
queries sharing one source. They remain historical files, not executed
subroutines. Exact empirical contractions, noise/grids, finite sampler,
completed-call chronology, full covariance correction, metric replay,
finite-transcript generation and whole-source amplification remain necessary.

## 3. Word costs and precision

Choose a numerical word of sufficient length

\[
 \boxed{w=\left\lceil C_{\rm word}\beta^{110L}Z\right\rceil
       \quad\text{bits}.}
 \tag{2}
\]

This is a **sufficient, not necessary**, precision bound. It covers ranges,
guards, exact dyadic accumulation and counters. It is logarithmic in width
at fixed problem parameters, but is not a 32/64-bit sufficiency result.
Setup can use exact integers of \(O(Rw)\) bits, where locally
\(R\le Cp\beta^{201L}(m+d+2)(1+m/\gamma)Z^{5/2}\); they cost
\(O(R)\) words and multiword operations. They are not free single scalars.

One word operation means a read/write, comparison, addition/subtraction,
Boolean operation, shift, full product returned in two words, or quotient
and remainder on a constant number of words. Long arithmetic, scalar roots,
Gaussian conversion and matrix functions are expanded into these primitives.
An arbitrary activation is not a unit-cost oracle. Thus a word operation
here need not be a single instruction on present hardware.

Define the displayed retained-size envelope

\[
 \boxed{M=p^2\beta^{402L}(m+d+2)^2(1+m/\gamma)^2Z^6
             [d+1+\log(e+(d+1)Z)]\quad\text{words}.}
 \tag{3}
\]

The final retained internal model has size at most a universal multiple of
\(M\). It includes all members, seeds, current scalar state, selected
packets, caches, and the normalized \(m(d+1)\)-entry training table.

Each table entry is an upper bound up to a universal multiplicative factor.
Work is in word operations; peak memory includes the retained model.

| Phase | Work | Peak memory, in words |
| --- | --- | --- |
| Initialization — build the compact model | \(n(d+1)p^5\beta^{1115L}(m+d+2)^5(1+m/\gamma)^5 Z^{29/2}\) | \(M+np\beta^{201L}(m+d+2)(1+m/\gamma)Z^{5/2}+p^3\beta^{603L}(m+d+2)^3(1+m/\gamma)^3Z^{15/2}\) |
| Training — complete all compact updates | \((d+1)p^4\beta^{914L}(m+d+2)^4(1+m/\gamma)^4 Z^{12}\log(e+p\beta^{201L}(m+d+2)(1+m/\gamma)Z^{5/2})\) | \(M\) |
| Querying — predict at one unseen input | \((d+1)p^4\beta^{914L}(m+d+2)^4(1+m/\gamma)^4[(L+1)nZ^{12}+Z^{14}]\) | \(M\) |

The training row counts the **complete prescribed finite update schedule**,
not one ODE right-hand-side evaluation. Initialization memory is not
polylogarithmic; its temporary source table still costs a factor of \(n\).
Arbitrarily many queries pay their individual costs. Concurrent queries or
members do not have free scratch space.

For fixed problem parameters and positive label scale, this is

\[
 \begin{array}{ll}
 \text{retained / training / query memory:}&
       O(\log^6(en)\log\log(e^e+n))\ \text{words},\\
 \text{initialization work:}&O(n\log^{29/2}(en)),\\
 \text{complete training work:}&
       O(\log^{12}(en)\log\log(e^e+n)),\\
 \text{one-query work:}&O(n\log^{12}(en)+\log^{14}(en)).
 \end{array}
 \tag{4}
\]

An absolute integer power seven bounds the word storage. Multiplying the
stored words by (2) recovers the seventh power and outer logarithm **in
bits**. Changing units is not a physical storage saving. The scheduling
improvements in Section 6 do reduce actual work; the earlier bit upper
bounds also remain valid for the improved implementation.

## 4. Costs not hidden by the table

For tanh, the explicitly supplied finite evaluator is absorbed in the
table. For a general supplied analytic activation, multiply its actual
word cost per value call by the following sufficient call counts, and add
one live evaluator's workspace:

\[
\begin{array}{ll}
 \text{initialization:}&
 n(d+1)p\beta^{201L}(m+d+2)(1+m/\gamma)Z^{7/2},\\
 \text{training:}&M,\\
 \text{querying:}&
 (d+1)(L+1)\big[np\beta^{201L}(m+d+2)(1+m/\gamma)Z^{7/2}
 +p^2\beta^{402L}(m+d+2)^2(1+m/\gamma)^2Z^6\big].
\end{array}
 \tag{5}
\]

The training call envelope in (5) is slightly looser than the sharp
display in `WORD_COST_REFINEMENT.md`, Section 7; it uses the already defined
\(M\). Jets and activation interpolation are already counted in the
field and operation bounds. There is no uncharged spatial quadrature order.

Add actual data/certificate acquisition, query/time access, output work,
and their live scratch. If external evaluator/data/scale/certificate
descriptions use \(B\) bits beyond the counted finite table, add
\(\lceil B/w\rceil\) retained words. This local \(B\) is a supplied
description length, not a universal constant. Raw-label access requires
fractional precision at least

\[
 w+\lceil\log_2(16\sqrt m)\rceil+
       \lceil\log_2\max(1,1/Y)\rceil.
 \tag{6}
\]

For \(0<nY<1\), the conservative alternative replaces \(Z\) by
\(Z+\log_+(1/(nY))\) in precision, degree/field counts, code counts,
and the resource table. It is not merely a precision correction. Use the
modular finite-source Gaussian-RMS condition with the **enlarged** actual
field count, rather than assuming the clean-table width gate automatically
covers an arbitrarily tiny label. The clean theorem below keeps
\(n\ge1/Y\), as in the baseline; at each fixed positive label scale this
does not alter the eventual width-asymptotic claim. The physical source
probability theorem itself has no lower-label premise.

## 5. Width and accuracy: what is preserved and improved

Only in this width paragraph define the reference proof's moment order

\[
 p_{\rm ref}=\max\left\{1,\left\lceil
 \frac{\log(2^{22}emL/\delta)}{\log(64e^2)}\right\rceil\right\}.
\]

A sufficient enclosing width for the clean table and unchanged comparison is

\[
 \boxed{n\ge\max\left\{
 C_*\left[
 \frac{2^{20}\beta^{2000L}}\delta
 (1+m/\gamma)^4(m+d+p_{\rm ref}+1)^4
 \right]^{1100},\quad Y^{-1},\quad C_{\rm num}
 \right\}.}
 \tag{7}
\]

Take the integer ceiling. Here \(C_*\) is universal and pays the
unchanged implementation RMS constants. The absolute \(C_{\rm num}\)
is determined by the chosen total numerical allocation: if that coefficient
is \(A_{\rm num}\), take
\(C_{\rm num}=\max\{1,(A_{\rm num}/32)^{1/9}\}\).
Neither constant hides problem parameters. The old enclosing power was
20,000. Thus its displayed activation power falls from
\(\beta^{40,000,000L}\) to \(\beta^{2,200,000L}\).
Both are single exponentials in \(L\), not double exponentials; the new
one remains enormous.

For the sharper scientific gate, locally put
\(\rho=2^{-20}\delta\) and
\(\mathcal A=\beta^{2000L}(1+m/\gamma)^4
(m+d+p_{\rm ref}+1)^4\). It suffices for the source to require

\[
 n\ge\left\lceil\max\left\{
 [2\mathcal A(2000\log(2\mathcal A))^{16}]^{1000},
 64mL/\rho\right\}\right\rceil.
 \tag{8}
\]

The separate implementation RMS, horizon, numerical-absorption and optional
quadratic-work gates stay as listed in `WIDTH_GATE_REFINEMENT.md`, Section 6.
Do not drop them when using (8). The simple enclosing gate (7) already
dominates them. Neither variant changes the inner source estimate or proves
that the width is practically attainable.

The final error is unchanged: at every admissible **individual** width,
with probability at least \(1-\delta\),

\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |\widehat f(t,x)-f_n^{\rm independent}(t,x)|\le3b_n,
 \tag{9}
\]

including the fitted endpoint and unseen/adaptively chosen inputs on the
same simultaneous event. Here the original dense upper certificate is

\[
 b_n=
 \frac{c_0Y}{\sqrt n}
 e^{c_1Y^2\sqrt{\log(en)}}
 \sqrt{8\log\!\frac{2048(n+1)(1+2n)^d}{\delta}}
 +c_{2,\rm mesh}\frac Yn,
 \qquad
 32\le c_{2,\rm mesh}\le C\beta^{4L}(1+m/\gamma).
 \tag{10}
\]

**Important boundary:** the inherited leading coefficients \(c_0,c_1\)
have not been turned into explicit functions of all major parameters by
this cleanup. They are not asserted universal. The resource table has
explicit parameter dependence; the leading error certificate is still an
imported structural certificate. Matching this upper-certificate scale is
not a lower-bound comparison to actual dense variability, a sharp-rate
claim, or an \(n^{-1}\) error theorem. No extra unquantified stochastic
width threshold is introduced by these resource refinements.

## 6. Short proof architecture and exact improvements

The proof needs four interfaces: the finite physical training-source event;
finite source/metric scalar replay; exact source-row querying with the full
conditional covariance; and finite-transcript generation plus whole-source
amplification. The existing physical modulus and tail extend the coded
event to the whole sphere and all physical time. The fixed numerical
\(Yn^{-10}\) remainder is absorbed using the explicit mesh term, not
by waiting for the leading exponential error factor to grow.

The changes within those interfaces are small and inspectable:

- **Confidence.** Every implemented complete source experiment needs only
  fixed bad-output probability before the whole-source median. Only the
  independent reference needs the confidence-dependent source moment order.
  A common real physical good set fixes the same comparison center. This
  removes \(\delta\) from the implemented \(p\), not from \(Z\) or width.
- **Seed traversal.** Depth-first traversal emits exactly the same recursive
  generator blocks, using fewer than twice the number of rows in hashes
  rather than regenerating a root-to-leaf path separately for every row.
  Both nested traversal stacks and retained seeds are charged.
- **Packed hashing.** Binary Toeplitz hashes use word shifts/XOR on stored
  coefficient windows. No carryless-multiplication oracle is assumed.
- **Cached products.** Store each acquired field and its exact dyadic metric
  product. Distributivity preserves every acquired scalar and its final
  rounding. No future field is cached and no intermediate rounding is added.
- **Spectral pivots.** An indexed heap with fixed tie-breaking updates only
  changed matrix entries; an exact cached residual sum avoids a second full
  scan. The same finite Jacobi pivots, stopping decision and rounded output
  are obtained. There is no accumulating stale-entry history.
- **Width algebra.** Keep the original scientific map/remainder bounds but
  solve their actual absorption inequality
  \(\mathcal A\log(en)^{16}\le n^{1/1000}\), together with the
  confidence gate \(n\ge64mL/\rho\). This yields (8) and hence (7).

The detailed modular algorithms, substitutions and wide-integer charges are
in `WORD_COST_REFINEMENT.md`. The confidence proof is in
`CONFIDENCE_SEPARATION_REFINEMENT.md`; the gate-by-gate audit is in
`WIDTH_GATE_REFINEMENT.md`. These are conditional improvements to the
existing component theorem, not a re-audit of its entire scientific ancestry.

## 7. An implementation that can be investigated honestly

The exact finite program has a useful execution layout: field-major row
tiles, shared small-matrix coefficient preparation, blocked contractions,
exact reduction trees, and sequential source members with an explicitly
budgeted workspace pool. Selected-packet training uses dense small matrices.
Queries stream regenerated rows in a constant number of passes per layer.
This exposes parallel row, field, contraction and integer-limb work without
adding a stored dense network or replaying scalar training.

Exact tile regrouping preserves the finite transcript when all accumulator
bits and named rounding points are preserved. A tile of at most the field
count fits the existing training/query memory. Host-side setup tables still
count in total peak memory even if the device tile is small. Scalar
acquisitions remain dependency barriers; unbounded GPU concurrency would
violate the workspace claim.

The serious practical obstacles are **not** just constant prefactors:
certified word length, high field-count powers, exact rank/determinant
selection, finite Gaussian conversion, and the theorem's generator.
A mixed-precision GPU prototype with practical random generators, stable
rank thresholds and adaptive orders is plausible engineering, but is a
different finite program. Without a new stability/coupling justification or
empirical evidence it cannot inherit the present theorem silently.

Consequently this round establishes cleaner exact scheduling and lower
resource envelopes, not a demonstrated scalable neural compressor. The
bounded next implementation target is an exact finite-call reference plus
a tiled backend, followed by a separately labeled practical prototype.
`IMPLEMENTATION_STREAMLINE.md` specifies that boundary and the memory ledger.

## 8. Checks and reproducibility

`test_streamline_kernels.py` contains five deterministic CPU exact-algebra
tests: packed Toeplitz hashing versus a bit reference; depth-first generator
sequence/hash count/stack bound; cached metric bilinear equality; exact tiled
reductions; and indexed-heap pivots versus full scans including ties. Run:

```sh
python3 -B studies/unseen_query_decoder_20261005/test_streamline_kernels.py
```

These tests are corroboration of small implementation identities, not a
neural experiment, a benchmark, GPU evidence, or a test of the probability
theorem. Separate bounded reconstructions are recorded in
`CONFIDENCE_SEPARATION_CHECK.md`, `WORD_COST_REFINEMENT_CHECK.md`,
`WIDTH_GATE_REFINEMENT_CHECK.md`, and `IMPLEMENTATION_STREAMLINE_CHECK.md`.
Their contexts are explicitly disclosed; they are not blind promotion
reviews. No historical proof file is deleted and no maintained book or API
is changed.

The final assembly received a separate read-only check against the three
refinement author notes. It found no resource substitution or gate mismatch;
its wording correction distinguishing generated members from independent
pre-generator experiments is included above. This is an assembly check at
the supplied interfaces, not an additional independent scientific review.
