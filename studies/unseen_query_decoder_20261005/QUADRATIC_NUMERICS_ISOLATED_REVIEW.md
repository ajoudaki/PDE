# Independent numerical and resource review

2026-10-06. Isolated review, not a promotion review.

**Verdict: conditional PASS for the numerical and resource deductions.** The
six supplied files contain sufficient computational interfaces to support
retained information \(C\log^{245}(en)\), post-initialization peak information
\(C\log^{722}(en)\), initialization work \(Cn\log^{1700}(en)\), total compact
update work \(C\log^{1700}(en)\), and query work \(Cn\log^{2100}(en)\), under
their explicitly stated source/statistical hypotheses and fixed-primitive
convention. I found no unresolved numerical interface defeating these
exponents. This verdict does not establish the inherited neural, physical,
posterior-comparison, or dense-trajectory error statements.

The qualification concerning primitives is substantive: these are bounds
for the specified numerical interpreter with externally supplied activation,
derivative, and fixed-data precision access. They are not universal fully
charged bit-complexity bounds following from strip analyticity alone. The
resource result states this boundary explicitly.

## Scope and inputs

I reconstructed the computational consequences from the complete frozen
inputs below, without using their assertions of proof status as evidence:

- `EXPLICIT_COMPILER_EXPONENT.md`;
- `FAST_SMALL_MATRIX_FUNCTIONS.md`;
- `SHORT_SEED_PRIOR_BLOCKS.md`;
- `QUADRATIC_INITIALIZATION.md`;
- `RECALIBRATION_FREE_MOMENTS.md`, including its complete Section 10;
- `QUADRATIC_RESOURCE_RESULT.md`.

The external generator source was Nisan, *Pseudorandom generators for
space-bounded computation*, Combinatorica 12 (1992), 449–461, read through
the supplied [original paper](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf).
The relevant source check is its finite-state block definition and Lemma 3,
not merely the space-bounded corollary.

I read the required research and rigorous-mathematics skills and the
adversarial-audit reference. The required custom notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` returned
`Permission denied`. I used the assignment's stated fallback: preserve the
supplied symbols, define new objects locally, and make the reviewed
calculations self-contained. I did not read the study README, other study
artifacts, prior reviews, Git history, maintained-source dependencies, or
the neural reference behind the inaccessible skill. No experiment or
candidate-file edit was performed.

For this review, let \(\ell=\log(en)\). Constants may depend on the fixed
problem and confidence. The supplied computational sizes are

\[
R=O(\ell^8),\quad P=O(\ell^{16}),\quad D=O(\ell^8),\quad
N=O(\ell^{56}),\quad r=O(\ell^{16}),
\]

where \(R\) bounds named fields, \(P\) summaries, \(D\) Gaussian packet
coordinates, \(N\) mathematical graph instructions, and \(r\) the largest
materialized matrix dimension. These are inherited program-size
hypotheses. The review checks their numerical consequences rather than
independently deriving them from the original neural flow.

## Matrix arithmetic and precision

The noncommuting rounded-Newton issue is resolved in
`FAST_SMALL_MATRIX_FUNCTIONS.md`, Section 3. For a symmetric positive
matrix \(A\) with \(aI\preceq A\preceq MI\), the exact iterates commute
with \(A\), but only that reference sequence is diagonalized. The computed
iteration uses the symmetric map

\[
F(X)=\tfrac12\operatorname{sym}(X+AX^{-1}).
\]

If its current error is at most \(a/4\), the computed matrix retains a
positive spectral floor, and the inverse-difference identity gives

\[
\|F(X)-F(X_j)\|_F
\le (\tfrac12+Ma^{-2})\|X-X_j\|_F.
\]

Thus the stated grid condition controls both forward error and every
subsequent inverse's domain. No commutativity of computed matrices is
needed. The reference contraction needs only logarithmically many steps.

The rational cost calculation in `EXPLICIT_COMPILER_EXPONENT.md`, Section 6,
also survives reconstruction. With

\[
h=2+r+p+b_0+\log_2M+\log_2(1/a),
\]

the inverse input has \(O(h)\)-bit integer entries after clearing its
dyadic denominator. Minors have \(O(h^2)\) bits. Reduced Schur entries are
ratios of minors, so exact pivoting does not introduce unchecked recursive
denominator growth. Computing all cofactors takes \(O(h^5)\) rational
operations. Charging \(O(h^6)\) per operation gives inverse time
\(O(h^{11})\).

Newton uses \(O(h)\) iterations and an \(O(h^2)\)-bit private grid. Its
inverse minors then have \(O(h^3)\) bits, giving \(O(h^9)\) per rational
operation, \(O(h^{14})\) per inversion, and \(O(h^{15})\) for the root.
Multiplication by \(A\) uses the inverse's common determinant denominator;
there is no product of unrelated entry denominators. A constant number of
matrix arrays occupies \(O(h^5)\) bits.

Crucially, the final root is rounded back to the requested ordinary
operand precision. The private \(O(h^2)\) precision is not carried into
the next macro. Positive-part and radial-cap outputs use the specified
PSD-preserving interface. For the positive part, the error-\(v\) root of
\(A^2+v^2I\), followed by the added \(vI\), gives an actual PSD dyadic
output; subsequent cap scaling is nonnegative and exact. Sylvester
systems include their full Kronecker dimension in \(r\).

With \(\mathcal H=2+b+C\ell^{58}\), at most \(N\le C\mathcal H\)
macros therefore cost \(C\mathcal H^{16}\) time. Cached ordinary
outputs and one macro's private scratch fit \(C\mathcal H^6\) bits.
This proves the advertised row exponents 1600/600 at precision
\(b=O(\ell^{100})\), and 1920/720 at \(b=O(\ell^{120})\).

## Exact support reduction and initialization

The support algorithm in `QUADRATIC_INITIALIZATION.md`, Section 2, avoids
both support enumeration and a sequence of growing exact rational
denominators. On insertion, the old support columns are independent; if
the enlarged set is dependent, its nullspace has dimension one. The
minimum positive ratio step deletes at least one column having nonzero
null coefficient. Any dependence among the survivors would extend to a
different null vector vanishing at that deleted coordinate, a
contradiction. Tied minima do not invalidate this argument.

After each insertion, the integer prefix sum and an invertible support
minor determine the unique weights by Cramer's rule. If the input
integer coordinates have \(\beta\) bits, each weight has

\[
O\bigl(P[\beta+\log n+\log(P+2)]\bigr)
\]

bits, uniformly over all insertions. Recomputing this representation is
essential. It is supplied explicitly. The proof uses determinant
expansions only to bound sizes, and polynomial elimination to compute
them.

At the chosen precision, \(\beta=O(\ell^{100})\), so weights use
\(O(\ell^{116})\) bits each and \(O(\ell^{132})\) bits in total. The
selection cost bound is

\[
n(P+2)^8[\beta+\log n+\log(P+2)]^3=O(n\ell^{428}).
\]

For the implemented finite source, support reduction matches every
coordinate of the rounded row-contribution vector exactly. Induction
through the same deterministic row evaluator, noise marks, and final
rounding reproduces the implemented source prefix exactly. It is not a
claim to store continuous Gaussians exactly. The separate deterministic
coupling recurrence controls the difference from the ideal real source.

There are \(nP\) row evaluations in source execution and again at most
\(nP\) in contribution reconstruction. Their combined work is
\(O(n\ell^{1616})\). The \(nD\) stored packet coordinates cost
\(O(n\ell^{108})\) bits. The row scratch is \(O(\ell^{600})\), and
selection scratch is smaller. All \(P\) compact updates evaluate at most
\(P+1\) retained packets each, costing \(O(\ell^{1632})\). Exact weighted
sums of the bounded support do not alter these dominant bounds.

The source-to-Gaussian-matrix-law representation is an inherited
hypothesis here. Under it, the construction samples a fresh virtual
source; it does not read and compress an arbitrary specified dense
matrix realization. The numerical claims do not require such a read.

## Whitening, additional gaps, and Gaussian generation

The query-whitening interface is present in
`RECALIBRATION_FREE_MOMENTS.md`, Section 10. It must be included; the
original training-only compiler by itself would not establish the query
exponents.

With \(\overline X\) a dyadic upper bound for \(X\) and
\(\log X=O(\ell^2)\), the prescribed ridge is
\(\tau=\overline X^{-512}\). The raw coefficient and Gram bounds give

\[
\|A_0\|\le\overline X^{102},\qquad q\le\overline X^{202}.
\]

Consequently the buffered mixer perturbation has bound
\(C\overline X^{102+101-256}=C\overline X^{-53}\), and the displayed
variance perturbation has bound \(C\overline X^{-310}\). Each fixed-depth
polynomial in the physical feature bound is eventually absorbed by one
additional factor of \(\overline X\). These losses are below the stated
inverse-polynomial error budget. The safe positive-part extension has
floor \(\tau\) on arbitrary guarded inputs.

Whitened marks, coefficients, and row partial sums have fixed powers of
\(\overline X\) as bounds. Their logarithms remain \(O(\ell^2)\).
The added graph fits the existing \(O(R^7)\) count, and the inverse-root
Lipschitz factor \(\tfrac12\tau^{-3/2}\) changes constants rather than
logarithmic degrees. Thus the sensitivity degrees 58 and 74 remain
valid. The chosen noise gives information upper bound \(O(\ell^{90})\);
history precision degree 100 and query precision degree 120 dominate
the resulting error requirements.

Finite Gaussian generation also fits the counts. The query cutoff has
\(T^2=O(\ell^{120})\). Taking the uniform precision with a sufficiently
larger constant makes

\[
e^{T^2/2}2^{-b}+2^{-b'}
\]

smaller than the required coordinate tolerance after row sensitivity.
The iid tail union over rows, packet coordinates, and contexts is bounded
by \(\exp[-c\ell^{120}+C\ell^{116}+O(\ell)]\), hence is negligible.
This estimate belongs to the truly random finite baseline; it need not
be asserted separately for independent rows after PRG substitution.

The stated scalar CDF construction need not conceal a large polynomial
degree. Put \(p=C(T^2+b+b'+1)\). An exponential Taylor polynomial of
degree \(O(p)\) gives the required CDF precision, using symmetry around
zero for its integration constant. At a dyadic bisection point of
\(O(p)\) bits, the integrated terms have a common denominator with
\(O(p^2)\) bits: use the dyadic denominator, the largest factorial, and
the product of the odd integration denominators. Intermediate reduced
rationals then have \(O(p^2)\) bits. Even cubic-cost fraction arithmetic
gives \(O(p^7)\) per CDF call and \(O(p^8)\) for \(O(p)\) bisection
steps. CDF error intervals handle an ambiguous comparison by returning
the already sufficient quantile interval. Gaussian normalization can be
computed by the stated convergent scalar series and a scalar root at
smaller cost. This is below the row time/space allowances, even after
all \(D\) coordinates. The initialization Box–Muller construction has
smaller precision and similarly fits its dominant row-work bound.

## Generator applicability and simultaneous tests

The original paper permits a finite-state transition to be an arbitrary
function of the current block; only information surviving between blocks
is constrained. Its block lemma, with block length \(q\), applies when
state bits and generator recursion depth are at most a constant times
\(q\), with error exponentially small in \(q\). These facts support the
application's use of large temporary row scratch. The recursive generator
uses sampled hash descriptions; it does not require finding or certifying
a good seed. [Nisan, Sections 2–4](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf).

For this application \(J=O(\ell^{116})\) statistical blocks retain at
most \(R=O(\ell^8)\) coordinates, each of \(O(\ell^{120})\) bits.
Thus completed block means cost \(O(\ell^{244})\) bits. Counters,
current context, retained prefixes, and ordinary coefficient arrays fit
below that bound. For example, the very loose cached-output bound
\(Nr^2O(\ell^{120})\) has degree \(56+32+120=208\). The larger
private matrix scratch is discarded before reading the next random row.

The tester under true randomness has no generator seed in its state.
After substitution, the real decoder stores that seed separately, as
counted below. Internal reuse of the current row's block is permitted.
It would be invalid to retain or reread a previous random row outside
the counted state; the specified estimator does neither.

There are at most \(nJ\) row blocks for each fixed vector-moment test,
so generator depth is \(O(\ell)\). Choosing random-block length
\(q=C\ell^{244}\) covers both the state and all \(O(\ell^{128})\)
bits needed for one Gaussian row. It also makes fooling error smaller
than the reciprocal of the finite context count. The seed length is
\(O(q\ell)=O(\ell^{245})\). Direct leaf computation takes at most
\(O(\ell)\) Toeplitz hashes at quadratic cost in \(q\), or
\(O(\ell^{489})\) work per row. No search over seeds appears.

The finite-context count includes guarded intermediate moments, not just
the external query. Fixed source prefixes and their inaccessible target
moments are frozen before the independent seed is drawn. Each target
coordinate is bounded by the supplied second-moment hypothesis and can
be approximated to \(O(\ell^{120})\) bits in the proof tester. The
tester is allowed nonuniform finite transition labels; it is not part
of the decoder's computed inputs. Using a comparator margin larger than
statistical and arithmetic errors transfers a correct failure bound.

Applying the generator separately to these fixed tests and taking their
finite union is valid. Restarting the seed for a later context does not
ask one tester to reread its random tape. Because the union includes
every possible guarded intermediate code, it also covers the actual
seed-dependent contexts. No independence between different contexts or
later adaptive queries is needed. The continuity argument concerns the
exact population maps before arithmetic, not a rounded median program.

## Reconstructed resource totals and limits

| Quantity | Reconstructed bound | Stated enclosing bound |
|---|---:|---:|
| Retained panel, exact weights, instructions | \(C\ell^{156}\) bits | Included in retained state |
| Stored generator seed | \(C\ell^{245}\) bits | \(C\ell^{245}\) retained bits |
| Initialization row scans | \(Cn\ell^{1616}\) work | \(Cn\ell^{1700}\) |
| Support elimination | \(Cn\ell^{428}\) work | Included above |
| Temporary initialization storage | \(C[n\ell^{108}+\ell^{600}]\) bits | Same |
| All compact updates | \(C\ell^{1632}\) work | \(C\ell^{1700}\) |
| Query row evaluation | \(Cn\ell^{1920+116+16}=Cn\ell^{2052}\) work | \(Cn\ell^{2100}\) |
| All query block generation | \(Cn\ell^{489+116+16}=Cn\ell^{621}\) work | Included above |
| Post-initialization row scratch | \(C\ell^{720}\) bits | \(C\ell^{722}\) peak including retained state |

Sorting the completed block means, numerical comparisons, and counters
are smaller than the dominant row bound. Sampling and storing the
generator's initial seed costs only its already counted number of bits.

If primitive implementations are charged, their costs must be added. The
supplied graph count gives at most \(Cn\ell^{188}\) primitive calls per
query at \(C\ell^{120}\) precision, as stated in the result. The same
counting gives \(Cn\ell^{72}\) calls during initialization and
\(C\ell^{88}\) calls during compact updates, at \(C\ell^{100}\)
precision. One primitive's peak scratch must also be added. An arbitrary
polynomial-space or polynomial-time implementation degree cannot be
absorbed into a universal exponent 722 or 2100 without an additional
degree bound.

For fixed admissible problem parameters every displayed logarithmic
power is fixed, and \(\ell^{2100}/n\to0\). The eventual dense-work
comparison follows. It says nothing quantitative about a practical
crossover width. Initialization workspace remains noncompact; it is
not included in the post-initialization peak claim.

No major numerical defect or missing computational proof interface was
found in the assigned scope. The conditional resource verdict should not
be promoted to a verification of the full approximation theorem or to
an unconditional activation-evaluator complexity theorem.

## Frozen-input identifiers

SHA-256 values of the reviewed files:

```text
93510e4e88f9c632e9c439715b655d4ea6dc1701aae655f0a30d45cbf7f4ba3a  EXPLICIT_COMPILER_EXPONENT.md
3f2a2edb247853d55a64bb3812828d2e57f0ceca2f5effbce56cb31bfdbab47c  FAST_SMALL_MATRIX_FUNCTIONS.md
f63da50dd1e9e9dc0ed0bb4e80eab4abfd27e2fe445b3521b648f1d8417b241f  SHORT_SEED_PRIOR_BLOCKS.md
fa97b8cee8bd97c89f098a6776e6b797b0acdbcca9d0470da5e0cceac405f6e8  QUADRATIC_INITIALIZATION.md
710989a20ec43db01612c5957bcc1ca181249cdbd08db3fea6addc3ec1a081ea  RECALIBRATION_FREE_MOMENTS.md
97afc75b34e57e38a5ceb6a0984d435ee6485fd9218e3313b1dbbb10807ff0d3  QUADRATIC_RESOURCE_RESULT.md
```

## Narrow final-version delta check

2026-10-06. At the supervisor's request, I read the complete updated
QUADRATIC_RESOURCE_RESULT.md and SHORT_SEED_PRIOR_BLOCKS.md, without
following their new review/check links or consulting other files.
The numerical verdict is unchanged: conditional PASS with the scope and
primitive-cost qualifications above.

The new finite implementation chooses a certified dyadic
\(h_+\le\widehat h\le2h_+\) and
\(s=\lfloor1/(128\widehat h)\rfloor\). For sufficiently large widths,
\(h_+\le1/512\), so

\[
\frac1{512h_+}\le s\le\frac1{128h_+}\le n,
\qquad sh\le\frac1{128}.
\]

The first lower bound uses \(\lfloor u\rfloor\ge u/2\) for \(u\ge2\).
Thus the product-relative-entropy comparison is preserved and the
statistical error changes only by a fixed factor. The exact floor now
acts on a rational dyadic quantity. No realized posterior entropy is
computed, and the row, seed, time, and space exponents are unchanged.

The added primitive overheads agree with the independent counts above:
\(nP N=O(n\ell^{72})\) calls for initialization and
\(P(P+1)N=O(\ell^{88})\) calls for all compact updates, at precision
\(C\ell^{100}\). The query overhead remains
\(O(n\ell^{188})\) calls at precision \(C\ell^{120}\).

The mean-coordinate clarification and explicit reference to the
whitening addendum do not add numerical work: positive buffered Gram
square roots and their inverses cancel in the mean representation, while
the reviewed bounds control its transformed coefficient norm and the
variance modification. The explicit outer confidence sum is arithmetically
correct, \(64+32+32+64+1=193\) in units of \(\delta/256\).
The physical conditioning and interval claims remain inherited
interfaces within this numerical review.

Final reviewed SHA-256 values:

    e753d74e80bb4061d10c2c7f735e33991382d93f27c6c638a35c80afac695ccd  QUADRATIC_RESOURCE_RESULT.md
    78e5f21ce787adac48b5ca745f330af92c87330934dd1634132c0b2308c35201  SHORT_SEED_PRIOR_BLOCKS.md
