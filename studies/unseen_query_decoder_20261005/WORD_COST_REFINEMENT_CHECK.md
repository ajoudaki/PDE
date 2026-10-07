# Bounded reconstruction of the word-cost refinement

2026-10-07. Reused author context, not a blind or complete independent proof
review. This agent previously extracted theorem qualifications, authored the
implementation scheduling note, and reconstructed confidence separation.
The inherited scientific and finite-source theorems are accepted at their
stated component boundaries.

**Verdict.** The clean \(nY\ge1\) word-operation and memory tables,
exact caching, heap schedule and generator streaming check out. The existing
bit bounds remain valid. One qualification is needed in Section 7's
small-label accuracy transfer: after enlarging the field count, retain the
actual numerical Gaussian RMS failure gate with that enlarged count. The
original scientific width by itself does not discharge it for arbitrarily
tiny positive labels. This does not invalidate the clean table or the
conditional small-label resource formulas.

## 1. Frozen inputs and scope

The candidate `WORD_COST_REFINEMENT.md` was read completely at SHA-256
`af3d1447185914e008f1ac225ed3d04392ff8c73d7e1b52a27106760c8e220f3`.
Its notation distinguishes confidence moment order \(p\) from word bits
\(w\); this distinction is maintained below. \(n\) is dense width,
\(R\) the bounded number of fields/calls/coordinates, \(J\) the odd
source ensemble size, and \(L\) hidden depth. The remaining physical
parameters and assumptions are unchanged from the accepted composition.

Read completely for this task: the candidate, `SANE_METRIC_PACKETS.md`, and
`test_streamline_kernels.py`. `CLOSURE_COMPOSITION_COSTS.md`,
`SOURCE_SEED_EXACT_QUERY.md`, `SANE_DECODER_CORE.md`, and
`FAST_LOCAL_PRECISION_TEST.md` had already been read completely in this
author context and were reused at their current versions. The affine
convolution and recursive generator definition were checked against Nisan,
Sections 2.2 and 3.3, pp. 452 and 454--455, in the
[primary paper](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf).
The generator's probability theorem remains an accepted baseline interface;
this task checks the output-preserving traversal and work count.

No other refinement author's source, other study, scientific experiment,
maintained code or Git history was read. Only this report was written.

## 2. Actual operations behind the word counts

### Wide metric integers remain wide

The metric routine's input table has \(O(w)\)-bit entries, but its
fraction-free minors, common determinant and metric numerators have
\(O(Rw)\) bits. They therefore occupy \(O(R)\) words. The candidate
does not treat them as unit-cost integers.

For \(k\)-limb operands, schoolbook multiplication and normalized radix
division take \(O(k^2)\) declared word operations. The division estimate
in the candidate is valid. Write a normalized divisor as
\(v=aB^{k-1}+b\), with \(a\ge B/2\) and \(0\le b<B^{k-1}\),
and a partial dividend as \(u=sB^{k-1}+r\), with
\(0\le r<B^{k-1}\) and \(u<Bv\). The trial quotient
\(\widehat q=\min(B-1,\lfloor s/a\rfloor)\) cannot underestimate
\(\lfloor u/v\rfloor\). Moreover
\(\widehat q aB^{k-1}\le u\) and
\(\widehat q b<B^k\le2v\), so
\(\widehat qv-u<2v\). At most two downward corrections suffice.
The selected radix keeps each trial division inside the constant-word
primitive. Normalization, subtraction and carry work are included.

The metric source specifies an \(O(R^3)\)-operation small rank test,
not elimination on an expanded full-width table. Its wide arithmetic gives
\(O(nR^5)\) word work over the initial scan. Its common-denominator
adjugate algorithm uses \(O(q^3)\) operations on \(O(q)\)-word
integers, hence \(O(q^5)\) words of work for rank \(q\).
A full coefficient scan costs \(O(nq^4)\) and dominates since \(q\le n\).
There are \(O(qw)\) determinant-improvement swaps. The resulting
\(O(nR^5w)\) work and \(O(nR+R^3)\) peak words follow.
In particular the residual factor \(w\) in the swap count is retained.

### Packed hashes and depth-first generation

The candidate's hash is the affine binary convolution from Nisan's
definition. For each of \(t\) input bits it XORs a contiguous output
window of \(\lceil t/w\rceil\) words, with at most two source-word
reads per shifted window word. Its \(O(t\lceil t/w\rceil)\) work
requires no carryless multiplication primitive. Final masking handles a
partial word exactly. These assertions concern actual packed operations,
not division of a bit-work envelope by \(w\).

For fixed hash functions and root block, the recursive concatenation gives
the left subtree before the hashed right subtree. Depth-first traversal
therefore returns exactly the same ordered blocks as root-to-leaf
regeneration, by induction on depth. A padded tree has fewer than \(2N\)
internal nodes for \(N\) requested blocks. A pending right argument per
level, the current argument and the seed cost
\(O(\lceil t/w\rceil\log(N+2))\) words. Stack flags fit the same
bound. Thus the extra root-to-leaf depth factor disappears from full-stream
work, while it remains in seed/stack memory. Suspending an outer traversal
while consuming one member and its inner stream is accounted for in the
two simultaneous stacks. No independence assertion changes.

### Jacobi heap and exact residual

One plane rotation changes only entries in two rows/columns. Untouched
entries already lie on the fixed grid, so re-rounding them does not change
their values. Updating those \(O(r)\) independent off-diagonal entries
in an indexed heap takes \(O(r\log(r+2))\) word operations. A fixed
lexicographic tie rule matches the full-scan pivot. An indexed heap is
essential: indefinitely accumulating stale heap entries would not satisfy
the claimed space bound.

Maintain
\(2\sum_{i<j}A_{ij}^2\) exactly, subtracting old squares and adding new
squares. It equals the squared off-diagonal Frobenius norm. Its bit length
is at most a constant multiple of the input word length plus \(\log r\),
which is \(O(w)\) under the word certificate. Compare this exact number
with the exact squared stopping threshold. Thus both stopping and pivot
decisions match the same finite full-scan implementation. Updates must be
made from the saved old rows before overwriting them; the required linear
scratch fits the matrix budget.

The inherited iteration cap is \(O(r^2w)\). Each rotation costs
\(O(r\log(r+2)+w)\): matrix/basis updates are linear in \(r\),
and the digit-by-digit scalar root takes \(O(w)\) word operations.
Adding final reconstruction gives
\(O(r^3w\log(r+2)+r^2w^2)\) work and \(O(r^2)\) words, as
claimed. No eigenvalue-separation assumption or constant-time square root
has been introduced. This uses the inherited local precision certificate
to ensure all constant-factor expanded scalar operands have \(O(w)\) bits.

### Selected-field caches and Gaussian conversion

Each old field retains its creation-time arguments. Caching that field on
the selected packets therefore changes no later operand. With the rounded
metric fixed, caching \(z_v=\widehat Mv\) exactly also changes no pair:
\(u^\top z_v=\sum_{a,b}u_a\widehat M_{ab}v_b\) by finite
distributivity. No rounding is inserted into the cache. The sums/products
need a constant expansion of \(w\), including \(\log R\) guards.
The \(O(R)\) cached vectors use \(O(R^2)\) words; their formation
and all \(O(R^2)\) pair requests cost \(O(R^3)\) ordinary word
operations. Induction over acquisitions includes guards and the original
innovation-before-answer chronology. The private cache is not supplied to
the query's conditional coefficient calculation.

The inherited Gaussian converter performs \(O(w)\) bisections and
\(O(w)\) finite series terms per bisection at \(O(w)\) bits, including
the cutoff and cancellation guards. Those arithmetic operations are
constant-word operations in the declared machine, giving \(O(w^2)\)
per coordinate. This does not make Gaussian conversion free. The tanh
specialization uses its supplied finite series interface; general analytic
activation work and scratch stay external.

## 3. Expanded powers, seeds and peaks

Use exactly the candidate's definitions
\[
 D=m+d+2,\quad G=1+m/\gamma,\quad c=d+1,\quad
 Z=\log(en)+\log(e+D\beta^{100L}G/\delta),
\]
\[
 \Lambda=\log(e+cZ),\quad
 R\le Cp\beta^{201L}DGZ^{5/2},\quad
 w=\lceil C_{\rm word}\beta^{110L}Z\rceil.
\]
The inner block is \(A\asymp R^2w\), the depth is \(E=O(Z)\),
and the member block satisfies
\(b\le C(R^2wE+\log(N_{\rm ext}/\delta))\).
The latter code term is absorbed in the displayed envelopes; it is not
discarded as a zero-cost seed. The constructive block choices are at least
one word, so ceilings cost only constants.

The following substitutions reproduce the leading terms:

| Actual modular contribution | Parameter envelope |
| --- | --- |
| \(JR^2+(b/w)\log(J+2)\) | \(Cp^2\beta^{402L}D^2G^2Z^6(c+\Lambda)\) words |
| \(JnR^5w\) | \(Cnc p^5\beta^{1115L}D^5G^5Z^{29/2}\) work |
| \(JR^4w\log(R+2)\) | \(Cc p^4\beta^{914L}D^4G^4Z^{12}\log(e+p\beta^{201L}DGZ^{5/2})\) work |
| \(JnA^2/w\) | \(Cnc p^4\beta^{914L}D^4G^4Z^{12}\) work |
| \(Jb^2/w\) | \(Cc p^4\beta^{914L}D^4G^4Z^{14}\) work |

For example \(5(201)+110=1115\) and
\(1+5(5/2)+1=29/2\); \(4(201)+110=914\) and
\(1+4(5/2)+1=12\). The complete-training companion \(JR^3w^2\)
has activation exponent \(823L\), logarithmic exponent \(21/2\),
and only \(p^3D^3G^3\). It is bounded by the displayed training term
using the explicit major-parameter envelopes, without assuming actual
\(w\le R\). The other Gaussian, ordinary arithmetic and coefficient
terms have smaller corresponding envelopes. Since
\(\log(R+2)\le CZ\), their stated pure-power absorptions also hold.

The inner stack has \(O(AE/w)\) words and fits one member block;
the suspended outer stack and its seed need
\(O((b/w)\log(J+2))\) words. All \(J\) member states, selected
field/metric-product caches, exact accumulators, coefficient scratch and
the \(J\)-scalar median array fit the two displayed retained terms.
Sequential setup adds \(O(nR+R^3)\) words, not \(J\) copies of that
temporary table. The substituted extra peak terms are precisely
\(O(np\beta^{201L}DGZ^{5/2}+p^3\beta^{603L}D^3G^3Z^{15/2})\).

Multiplying retained words by the stated sufficient precision recovers the
old \(\beta^{512L}Z^7\) bit envelope. For work, the metric's actual
wide-integer bit cost remains its original bound; heap comparisons cost
\(O(r^3w^2\log(r+2))\le O(r^4w^2)\) bits; rotation arithmetic
retains \(O(r^3w^3)\) bits. Exact caches fit the old arithmetic bounds,
and full-stream generation executes fewer of the same hashes. This proves
preservation of the old bit envelopes from the actual operations; the loose
rule of multiplying every refined word operation by \(w^2\) is not used.

## 4. Required small-label qualification

Candidate Section 7 replaces \(Z\) by
\(Z_Y=Z+\log_+(1/(nY))\) for \(0<nY<1\), including degree and
field-count enlargement. This is the correct conservative resource
substitution. However, the finite-source/query numerical coupling also has
the inherited additional failure term
\[
 C(R+L+1)e^{-c_g n},\qquad c_g>0,
 \tag{1}
\]
where \(R\) must now be the enlarged actual/sufficient field count.
The clean polynomial RMS gate was derived using the clean \(Z\) envelope.
It cannot simply be reused independently of \(Y\) after this substitution.

For fixed \(n\) and the other parameters, \(Z_Y\) has no uniform upper
bound as \(Y\downarrow0\). Thus the supplied envelope
\(R\le Cp\beta^{201L}DGZ_Y^{5/2}\) does not make (1) uniformly
small at that fixed width. This is a failure of the stated sufficient
probability accounting, not evidence that actual prediction fails or that
the scientific source theorem acquires an inverse-label restriction.

The precise qualification for the final accuracy transfer is:

> On the tiny-positive-label branch, the substituted resource formulas and
> accuracy conclusion retain all finite-source numerical gates, in particular
> \(C(R+L+1)e^{-c_g n}\) below its allocated failure probability with the
> enlarged \(R\). The scientific source-width condition is unchanged.

Alternatively retain the clean branch's explicit \(n\ge1/Y\) condition.
A different uniform small-label RMS proof would be new work and is not
provided by exact caches, heaps or generator traversal. Read conditionally
with the displayed gate, the candidate's small-label resource and equivalence
statements are valid. Read as an unconditional extension of the clean width
gate to all positive labels, Section 7 is not established. The main author
also identified this point during the check; it was then verified directly
against the baseline finite-source failure and cost formulas.

## 5. Executed finite checks and their limits

Executed, without output files:

```sh
python3 -B studies/unseen_query_decoder_20261005/test_streamline_kernels.py
```

Observed: all five tests passed (packed hash, recursive generator stream,
cached metric pairs, exact tiled sums, indexed pivot heap). These tests
compare finite algebraic outputs. They do not implement the complete neural
source, finite Gaussian converter, spectral solver or a word-RAM backend,
and do not certify the asymptotic counts merely by passing.

Two further deterministic arithmetic checks were run in an in-memory
`python3 -B` process. They left no files. For radices \(2,4,8,16\) and
one- and two-digit divisors, the script enumerated every normalized divisor
and every integer partial dividend \(0\le u<Bv\). All 406400 quotient
estimates lay between the true quotient and that quotient plus two; the
largest observed overestimate was two. This corroborates the division proof
above rather than replacing it.

The second check reused the supplied heap class for dimensions 1 through 9
and 80 deterministic update stages per dimension. For each changed symmetric
entry it updated the exact rational residual by
\(2(a_{\rm new}^2-a_{\rm old}^2)\), then compared both that residual
and the heap pivot to complete recomputation after each stage. All 4927
entry changes passed. The entry formula and changed-row sequence were those
of `test_indexed_heap_matches_scan` in the supplied test file. Rank-one/empty
off-diagonal heaps and exact ties were included. This is not a test of
rounded Jacobi rotations or precision sufficiency.

Source hashes not already fixed by the candidate were:

| Source | SHA-256 |
| --- | --- |
| `CLOSURE_COMPOSITION_COSTS.md` | `2abd031ffc3f1548fd8cd92b0bc6e3594463327db09321104fb2110953ee44b0` |
| `SOURCE_SEED_EXACT_QUERY.md` | `877823e5b1032b93ec60a95e4f879c35aeac616d0983cfb269eef0429b84b524` |
| `SANE_METRIC_PACKETS.md` | `1683563689c824593613cb636590ae3180f4cc897913c8ed5acb3c12170adeea` |
| `SANE_DECODER_CORE.md` | `701de0d9ed9a429e6f9d771a9e4a96854872c9600509866a617da70690139fa4` |
| `FAST_LOCAL_PRECISION_TEST.md` | `af2a238a3ea1ed73059fd61321ca8408ce487399542156dc44e5e06f5a3e2f91` |
| `test_streamline_kernels.py` | `c3e7ae1f8567cb9872ee4ffeceb53dcac0b5d39add80a65df551525835e64619` |

All mathematical claims here are scoped to the explicit word model and
accepted baseline interfaces. In particular these results do not establish
32/64-bit sufficiency, GPU performance, polylogarithmic setup memory,
logarithmic query work, or uniform evaluator time for arbitrary analytic
activations. The candidate, existing implementation and confidence notes,
Git index and concurrent changes were left untouched.

## Corrected-input recheck, 2026-10-07

The updated candidate was checked at SHA-256
`9f807a490f9b6676d2a382992b71c8e9aeb65c983831e34241786a11b2eb7226`.
This follow-up read the corrected small-label passage in Section 7 and
the opening/final status paragraphs; it did not reopen the broader audit.
The original frozen-input hash, finding and deterministic test results
above are preserved.

Section 7 now explicitly requires
\(C(R+L+1)e^{-c_g n}\) below the allocated numerical failure allowance
using the enlarged tiny-label field count. It also states that the clean
polynomial RMS gate is not automatically uniform over arbitrarily small
positive labels and retains the alternative clean \(n\ge1/Y\) gate.
The scientific source-width condition remains unchanged. This is exactly
the missing qualification identified in Section 4 of this report.

**Corrected verdict: PASS at the stated component boundaries, including
the explicitly conditional tiny-label alternative.** The required
qualification is resolved; no unresolved correction remains from this
bounded word-cost reconstruction. The status paragraphs accurately identify
the bounded reconstruction and do not recast it as a blind promotion
review. No arithmetic or scheduling test was rerun for this textual
correction, and no broader scientific or implementation guarantee is added.
