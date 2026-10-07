# Word costs for the same finite exact-query decoder

2026-10-07. Scoped author refinement, conditional on the scientific and
finite-implementation interfaces of `CLOSURE_COMPOSITION_COSTS.md` and
`SOURCE_SEED_EXACT_QUERY.md`. This is a resource proof, not an independent
validation or promotion of those interfaces. No neural experiment was run.

The retained model uses six powers of the shared logarithm in numerical
words, with a further logarithm for its outer seed. Exact streaming,
caching and pivot selection also reduce work. The word precision is stated
separately. No bit-work bound is divided wholesale by the word length.

The bounded reconstruction in `WORD_COST_REFINEMENT_CHECK.md` verifies the
clean-table ledger and exact schedules. Its required tiny-label numerical
RMS qualification is included in Section 7 below. The combined current
interface, including fixed per-member confidence, is
`STREAMLINED_METHOD_RESULT.md`.

## 1. Parameters, precision and computation model

Keep dense width \(n\), \(m\ge d\ge1\) training inputs spanning
\(\mathbb R^d\) on its radius-\(\sqrt d\) sphere, depth \(L\ge2\),
positive population feature-Gram gap \(\gamma\), activation envelope
\(\beta\ge10\), label RMS \(Y=\|y\|_2/\sqrt m\), and failure
probability \(0<\delta<1/4\). The Gaussian initialization, zero readout,
nonlinear training in every layer, complete original upper-label
intersection, and independent dense reference are unchanged. Activation
values may be unbounded. Zero labels have the exact zero predictor.

Use the confidence allocation and moment order of the composition note:

\[
 \rho=2^{-20}\delta,\qquad
 p=\max\left\{1,\left\lceil
 \frac{\log(4emL/\rho)}{\log(64e^2)}\right\rceil\right\}.
 \tag{1}
\]

Thus \(p\) is a confidence moment order, never a number of numerical
bits. For substitution write

\[
 D=m+d+2,\quad G=1+m/\gamma,\quad c=d+1,
\]
\[
 Z=\log(en)+\log\left(e+\frac{D\beta^{100L}G}{\delta}\right),
 \qquad \Lambda=\log(e+cZ).
 \tag{2}
\]

Initially take \(nY\ge1\); Section 7 covers all other labels. The
composed construction supplies a constant-factor certificate \(R\ge2\)
for actual named fields, calls, coordinates and layers, and a sufficient
common word size that can be chosen as

\[
 R\le Cp\beta^{201L}DGZ^{5/2},\qquad
 w=\left\lceil C_{\rm word}\beta^{110L}Z\right\rceil.
 \tag{3}
\]

The universal constant in \(w\) includes integer ranges, local guards,
exact dyadic accumulation and address/counter bits. A numerical scalar
and any constant-factor expanded scalar occupy \(O(1)\) words. Integers
of \(O(Rw)\) bits occupy \(O(R)\) words, not one word.

One word operation is reading/writing a word, comparison, addition,
subtraction, Boolean operations, a shift by at most the word size, a
full word product returned in two words, or integer quotient/remainder
on a constant number of words. These are explicit word-RAM primitives;
division is not an unspecified real-number oracle. There is no primitive
matrix function, Gaussian sampler, activation, arbitrary-length integer
operation or carryless polynomial multiplication. A supplied activation's
actual word work and workspace remain external costs. Fixed-length
multiple-word arithmetic has constant cost under these conventions.

## 2. Exact packed hashes and complete generator streams

For a \(t\)-bit Toeplitz hash with its affine offset, keep the defining
\(2t-1\) diagonal bits and \(t\) offset bits packed. Each input bit
selects whether to XOR a contiguous \(t\)-bit window of the diagonal
string into the output. Each output word of such a window is obtained
from at most two stored words by shifts and masking. Looping over the
\(t\) input bits therefore costs

\[
 C t\left\lceil t/w\right\rceil
 \quad\text{word operations, with }C\left\lceil t/w\right\rceil
 \text{ scratch words}.
 \tag{4}
\]

This is the same binary convolution, with no approximation and no
table of exponentially many bit patterns. It saves one word factor;
ordinary integer multiplication alone does not justify a second one.

The generator used in the source is the recursive generator

\[
 G_0(x)=x,\qquad
 G_k(x;h_1,\ldots,h_k)=
 G_{k-1}(x;h_1,\ldots,h_{k-1})\,\Vert\,
 G_{k-1}(h_k(x);h_1,\ldots,h_{k-1}).
 \tag{5}
\]

The concatenation and affine convolution family are explicitly specified
in Nisan's original paper, Sections 2.2 and 3.3, pp. 452 and 454–455:
[primary source](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf).
Its probability theorem is used only through the already supplied
finite-transcript and median tests.

Traverse (5) depth first, keeping the current argument and pending
right-child arguments on a stack. Induction on \(k\) shows that the
ordered output blocks are identical to independent root-to-leaf
regeneration. Each internal node requires one hash. Pad a stream of
\(N\) blocks to \(2^{\lceil\log_2N\rceil}<2N\), emit the first
\(N\), and ignore the rest. Even traversing the whole padded tree uses
fewer than \(2N\) hashes. With the seed and stack counted, its bounds are

\[
 W_{\rm stream}(N,t)\le CNt\lceil t/w\rceil,
 \qquad
 M_{\rm stream}(N,t)\le C\lceil t/w\rceil\log(N+2).
 \tag{6}
\]

Frame flags, levels and counters add \(O(\log(N+2))\) words and
are absorbed. Every query makes full row streams; it may restart this
same traversal for each of its constant number of passes per layer.
It does not request an arbitrary sparse set of row indices. The outer
member generator is also streamed in member order. While a member is
processed, its outer traversal is suspended with its stack retained.
This changes neither random bits nor their order. It does not assert
independence of generated rows or apply a one-pass theorem to repeated
reading of the implemented stream.

## 3. Exact numerical work at word precision

**Metric construction.** The selected-packet construction uses
\(O(Rw)\)-bit minors and at most \(CRw\) determinant-improvement
swaps. Arithmetic on \(k\) words costs \(O(k^2)\) word operations
by schoolbook multiplication and normalized radix long division.
Here is the latter's relevant justification. In radix \(B\), normalize
the first digit of a positive \(k\)-digit divisor \(v\) to \(a\ge B/2\).
For a partial dividend \(u<Bv\), the estimate from its leading two
digits divided by \(a\), clipped to \(B-1\), overestimates
\(\lfloor u/v\rfloor\) by at most
two: the omitted divisor tail changes the trial product by less than
\(B^k\le2v\). Thus each quotient digit takes \(O(k)\) limb work
including at most two corrections, and \(O(k)\) digits take
\(O(k^2)\). Choose radix \(2^{\lfloor w/4\rfloor}\) so these
short trial products/divisions fit the declared primitives.

A rank test uses \(O(R^3)\) integer operations on \(O(R)\) words,
so the streaming rank scan takes \(O(nR^5)\) word work. For a
rank-\(q\) selected square block, one adjugate takes \(O(q^5)\),
and a complete coefficient scan takes \(O(nq^4)\); \(q\le n\)
makes the latter dominate. Multiplying by \(O(qw)\) swaps, and
including the final exact metric scan/rounding, gives

\[
 W_{\rm metric}\le CnR^5w,
 \qquad M_{\rm metric}\le C(nR+R^3).
 \tag{7}
\]

The \(w\) in the swap count remains. Expanded integers and the
noncompact temporary table remain charged. All finite rank decisions,
determinant comparisons and rounded final metric entries are unchanged.

**Spectral macros.** Use the source's finite largest-pivot Jacobi
routine with its existing precision, rounding and iteration cap.
For an \(r\)-square matrix it takes at most \(Cr^2w\) rotations.
Store the independent off-diagonal entries in an indexed max-heap,
ordered by absolute value and then the same fixed lexicographic
tie rule as a full scan. One rotation changes only \(O(r)\) entries,
so updating this heap costs \(O(r\log(r+2))\) word operations.
Its \(O(r^2)\) indices and heap entries fit the existing matrix space.

Maintain the exact dyadic squared off-diagonal norm by subtracting the
old squares and adding the new squares of those changed entries.
It needs \(O(w)\) bits and \(O(r)\) word work per rotation. Comparing
it with the squared residual tolerance gives exactly the decision of
a recomputed exact norm. Thus the residual test does not hide an
\(r^2\) scan. This supplies the same pivot, stopping decision and
rounded matrices as the corresponding full-scan finite implementation.

Matrix/basis updates cost \(O(r)\) word operations. The fixed-precision
scalar roots used for a rotation are computed by the elementary
digit-by-digit integer-root procedure, with \(O(w)\) shifts,
comparisons and subtractions; they are not unit cost. Including final
reconstruction, a spectral macro consequently costs

\[
 C\{r^3w\log(r+2)+r^2w^2\}\text{ word operations},
 \qquad Cr^2\text{ words}.
 \tag{8}
\]

The source uses \(O(R)\) such coefficient phases; a new query layer
uses \(O(1)\). The protected matrix map and its accuracy are unchanged.
The source's \(R^4\) allowance for all ordinary coefficient arithmetic
also covers cubic rank-list norm/projection contractions per phase.

**Gaussian and activation values.** A finite Gaussian coordinate uses
\(O(w)\) bisections, each evaluating \(O(w)\) exponential-series
terms with word arithmetic and the original certified interval test.
Its work is \(O(w^2)\) and its scalar scratch is \(O(1)\) words.
The supplied tanh series uses \(O(w)\) word operations and
\(O(1)\) live words. Neither statement applies to an arbitrary
supplied analytic activation evaluator.

## 4. Cache only already-created selected fields and exact metric products

Let \(q\le CR\) selected packets and rounded metric
\(\widehat M\in\mathbb R^{q\times q}\) be the original compact
acquisition state. When a new named dyadic field is created, compute
and store its selected vector \(v\in\mathbb R^q\) once, with its
immutable creation-time scalar arguments. Also store the exact dyadic
vector

\[
 z_v=\widehat Mv.
 \tag{9}
\]

For any requested pair with an already-created vector \(u\), evaluate
\(u^\top z_v\), add the same scalar-noise mark, and perform the same
outer grid rounding. By finite distributivity,

\[
 u^\top z_v=\sum_{a,b}u_a\widehat M_{ab}v_b
           =u^\top\widehat Mv
 \tag{10}
\]

as an exact dyadic number. `FAST_LOCAL_PRECISION_TEST.md`, Section 3,
explicitly permits this exact bilinear schedule. No internal rounding is
inserted into (9). Its product/sum bit lengths are \(O(w+\log R)=O(w)\),
including a constant-factor expansion for the final triple products.

All \(O(R)\) selected fields and their \(z_v\) vectors use
\(O(R^2)\) words. Their creation costs \(O(R^3)\) ordinary row
operations and at most \(O(R^2)\) activation calls. Computing every
\(z_v\) costs \(O(R^3)\), and all \(O(R^2)\) requested pairs
cost another \(O(R^3)\), including any constant-factor mandatory
repeats. Intrinsic innovation contractions remain inside their original
matrix call, with coefficients frozen; batching does not move them
past the answer or introduce a new coefficient solve.

This cache contains only past/current fields, never future scalar
answers. Induction over field creations and acquisitions proves literal
equality to the uncached exact-bilinear finite program for every seed,
including guarded branches. The same source good event and rounding
boundary argument therefore apply. Queries continue to use the permitted
scalar transcript and regenerated source rows; they do not use the
private metric cache as conditioning data and do not replay training.

## 5. Complete modular word ledger

Use the source's odd ensemble size \(J\), inner block length \(A\),
member block length \(b\) in bits, and inner depth \(E\):

\[
 J\le CcZ,\quad E=1+\lceil\log_2(n+2)\rceil\le CZ,
 \quad A\asymp R^2w,
 \quad b\le C\{R^2wE+\log(N_{\rm ext}/\delta)\},
 \tag{11}
\]

where \(\log(N_{\rm ext}/\delta)\le CcZ\). Constructive block
choices satisfy \(A,b\ge w\); padding to whole words costs only
universal constants. Put \(\lambda_J=\log(J+2)\), only in this ledger.
Retained and peak training/query word memory are bounded by

\[
 M_{\rm ret},M_{\rm train},M_{\rm query}
 \le C\left\{JR^2+\left\lceil b/w\right\rceil\lambda_J\right\}.
 \tag{12}
\]

This counts all \(J\) models and caches, the outer seed, the suspended
outer traversal, the current member block, its inner seed/traversal,
coefficient scratch, exact accumulators and final scalar median array.
The inner stack is \(O(AE/w)\le O(b/w)\); the outer stack is
\(O((b/w)\lambda_J)\). Initialization processes members sequentially,
so its peak is (12) plus \(C(nR+R^3)\), without a factor \(J\)
on this temporary table.

Let \(W_{\rm outer}=CJb\lceil b/w\rceil\). Applying the actual
algorithms above, the internal phase work has the modular bounds

\[
\begin{aligned}
 W_{\rm init}\le{}&CJ\{nR^5w+(nR+R^2)w^2
       +R^4w\log(R+2)+R^3w^2+R^4+nR^2
       +nA\lceil A/w\rceil\}+W_{\rm outer},\\
 W_{\rm train}\le{}&CJ\{R^4w\log(R+2)+R^3w^2+R^4\},\\
 W_{\rm query}\le{}&CJ(L+1)\{n[A\lceil A/w\rceil+Rw^2+R^2]
        +R^3w\log(R+2)+R^2w^2+R^3\}\\
 &\quad+W_{\rm outer}+CJ\log(J+2).
\end{aligned}
 \tag{13}
\]

All training means the complete finite update schedule. Its scalar marks
are already retained, so it does not regenerate member blocks. Median
sorting uses word comparisons. Every constant number of passes per
hidden layer is counted. The source's old bit envelopes remain valid:
the same metric arithmetic has its old bit cost; heap maintenance costs
\(O(r^3w^2\log(r+2))\le O(r^4w^2)\) bits, and numerical rotation
updates still cost \(O(r^3w^3)\); caching only removes operations;
streaming removes repeated hashes. This comparison uses the actual
primitive bit costs, not the looser product of every word count by
\(w^2\).

## 6. Fully substituted word bounds

Define the displayed retained-memory bound

\[
 M_{\rm word}=Cp^2\beta^{402L}D^2G^2Z^6(c+\Lambda).
 \tag{14}
\]

Substituting (3) and (11) into every term of (12)–(13) gives:

| Phase | Internal word operations | Peak internal words, including the model |
|---|---|---|
| Initialization | \(Cnc p^5\beta^{1115L}D^5G^5Z^{29/2}\) | \(M_{\rm word}+C[np\beta^{201L}DGZ^{5/2}+p^3\beta^{603L}D^3G^3Z^{15/2}]\) |
| Complete training | \(Cc p^4\beta^{914L}D^4G^4Z^{12}\log(e+p\beta^{201L}DGZ^{5/2})\) | \(M_{\rm word}\) |
| One query | \(Cc p^4\beta^{914L}D^4G^4[(L+1)nZ^{12}+Z^{14}]\) | \(M_{\rm word}\) |

Retained words are at most \(M_{\rm word}\), at the sufficient
\(w\) in (3). If a pure-power training envelope is preferred, its row
is at most \(Cc p^4\beta^{914L}D^4G^4Z^{13}\).

Here are the substitutions that determine the largest terms. The two
memory terms are \(JR^2\) and \(R^2E\log(J+2)\), giving (14).
The metric term is \(JnR^5w\), with activation exponent
\(5(201)+110=1115\) and logarithmic exponent
\(1+5(5/2)+1=29/2\). The training spectral term is
\(JR^4w\log(R+2)\), giving \(914L\), \(Z^{12}\) and the displayed
logarithm. Its \(JR^3w^2\) companion has lower exponents in every
positive parameter. The streamed inner and outer hashes are respectively
\(JnR^4w\) and \(JR^4wE^2\), giving \(Z^{12}\) and \(Z^{14}\).
Finally \(\log(R+2)\le CZ\) for the sufficient envelope (3), since
\(p\le CZ\) and each parameter logarithm in (3) occurs in (2).
This verifies the remaining absorptions without assuming an inequality
between unspecified actual \(R\) and \(w\).

For fixed \(m,d,\gamma,\beta,L,\delta\), the bounds reduce to
\(O(Z^6\log(e+Z))\) retained words, \(O(nZ^{29/2})\) initialization
work, \(O(Z^{12}\log(e+Z))\) complete training work, and
\(O(nZ^{12}+Z^{14})\) query work, with \(w=O(Z)\) bits per word.
These are word bounds; the retained bit bound still has the extra
precision factor and the outer seed logarithm.

## 7. External interfaces, small labels and scientific equivalence

For arbitrary supplied activations let \(\mathcal V_\phi^{\rm word}(w)\)
and \(\mathcal S_\phi^{\rm word}(w)\) be their actual word work and
scratch at the required range and precision. Sufficient value-call
counts remain

\[
 N_{\phi,\rm init}\le CJnR,\quad
 N_{\phi,\rm train}\le CJR^2,\quad
 N_{\phi,\rm query}\le CJ(L+1)(nR+R^2).
 \tag{15}
\]

Their explicit substitutions are, respectively,
\(Cnc p\beta^{201L}DGZ^{7/2}\),
\(Cc p^2\beta^{402L}D^2G^2Z^6\), and
\(Cc(L+1)[np\beta^{201L}DGZ^{7/2}
+p^2\beta^{402L}D^2G^2Z^6]\).
Multiply by actual evaluator work, and add one live evaluator workspace.
The tanh implementation above is absorbed by the table.

Let \(B_{\rm ext}\) count retained external description bits, including
all delimiters/addresses not already charged, and let actual word work
and scratch for phase data/certificate/query/time/output access be
\(W_{\rm access,phase}\), \(M_{\rm access,phase}\). Add
\(\lceil B_{\rm ext}/w\rceil\) retained/peak words, the evaluator
scratch and access scratch to phase peaks, and
\(N_{\phi,\rm phase}\mathcal V_\phi^{\rm word}(w)
+W_{\rm access,phase}\) to phase work. An external bit-time bound is
not automatically divided by \(w\). The normalized finite training
table fits the internal count, while its acquisition is still charged.
Raw labels require at least

\[
 w+\lceil\log_2(16\sqrt m)\rceil
   +\lceil\log_2\max(1,1/Y)\rceil
 \tag{16}
\]

fractional precision; retain the actual output-scale description.

For \(0<nY<1\), set \(Z_Y=Z+\log_+(1/(nY))\) and replace \(Z\)
by \(Z_Y\) throughout the sufficient counts, precision, code count and
table. This retains the conservative degree/field enlargement from
`CLOSURE_COMPOSITION_COSTS.md`; changing only precision would not be
justified. No new lower-label assumption is added to the scientific
theorem. At \(Y=0\) use its existing exact zero branch.

For this tiny-label alternative, retain the numerical Gaussian RMS gate
\(C(R+L+1)e^{-c_g n}\) below its allocated failure allowance, with
\(c_g>0\) universal and \(R\) the enlarged field count. The clean
polynomial sufficient RMS gate was proved using \(nY\ge1\); it is
not automatically sufficient uniformly over arbitrarily small positive
labels after replacing \(Z\) by \(Z_Y\). The scientific source-width
condition itself is unchanged. Alternatively keep the clean table and its
explicit \(n\ge1/Y\) gate.

The generator traversal and hashes are identical for every fixed seed;
the selected-field and bilinear caches preserve every finite scalar;
and the spectral implementation preserves the chosen finite pivot,
residual test and rounded output. The sufficient numerical schedule and
source/query coupling allocations are unchanged. Therefore all original
scientific width gates, the full label intersection, the whole-sphere
and all-physical-time event including the fitted endpoint, adaptive
query permission and the \(3b_n\) independent-dense upper-certificate
comparison carry over with exactly the same error and failure probability.
Those conclusions remain conditional on the inherited scientific proofs;
this resource argument supplies no additional probability theorem.

The word model, activation/data interfaces and initialization temporary
table are material qualifications. This does not prove polylogarithmic
query work, a sixth-power bit model, or bounded-time evaluation for the
full analytic activation class.

## Read scope and status

Read completely: the eight assigned files
`CLOSURE_COMPOSITION_COSTS.md`, `SOURCE_SEED_EXACT_QUERY.md`,
`GAP_REFINED_PHASE_COSTS.md`, `FAST_LOCAL_RESOURCE_CHECK.md`,
`FAST_SMALL_MATRIX_FUNCTIONS.md`, `FAST_TANH_EVALUATION.md`,
`SHORT_SEED_PRIOR_BLOCKS.md`, and `EXPLICIT_PHASE_COSTS.md`.
To expose the actual algorithms behind their bit envelopes, also read
the same study's `SANE_METRIC_PACKETS.md`, `SANE_DECODER_CORE.md`, and
`FAST_LOCAL_PRECISION_TEST.md`. The supervisor explicitly authorized
checking the linked primary Nisan paper; its complete thirteen pages
were read, with the recursive definition checked on its original page.
Canonical-notation instructions, their neural reference and the rigorous
mathematics skill were applied. No other study, book, code, new cleanup
artifact, review verdict or Git history was read. Only this file was
written. The separate bounded reconstruction is recorded in
`WORD_COST_REFINEMENT_CHECK.md`, with its context and scientific boundaries
explicitly disclosed; this is not a blind promotion review.
