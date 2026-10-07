# A repeatable prior-block decoder with a counted short seed

2026-10-06. Author construction for the current dense-budget continuation.
This note supplies the numerical/randomness interface for
`RECALIBRATION_FREE_MOMENTS.md`. It is not a dense-trajectory theorem by
itself. No experiment, cryptographic assumption or dense-root oracle is used.

## 1. The statistical interface

Fix the complete training source, independently of the decoder seed. At
each of its finitely many current prefixes let `mu` be the standard
Gaussian packet law and let `nu` be a proof-only row law. The algorithm
does not evaluate a density, normalizer, or expectation under `nu`.
For this note write these laws as \(\mu,\nu\). The supplied conditions are

\[
 D(\nu\Vert\mu)\le h,\qquad
 \mathbb E_\nu UU^T\preceq I_R,\qquad |G(z;\theta)|\le B.
 \tag{1}
\]

Here \(U\) is the vector of whitened history marks, of dimension \(R\);
\(\theta\) is the current query context, including input, patch time and
guarded intermediate query moments. Packet dimension, history dimension,
and the number of prefixes are explicitly bounded. The target vector is
\(\mathbb E_\nu[UG(\cdot;\theta)]\). Scalar second-moment tests are
covered by taking one mark equal to one and replacing \(B\) by the
corresponding scalar bound.

The statistical block lemma in the companion note proves the following.
Put \(h_+=\max\{h,1/n\}\) and take
\(s=\lfloor 1/(128h_+)\rfloor\), at sufficiently large width so
\(s\ge1\). A coordinatewise median of \(J\) independent blocks,
each the mean of \(s\) iid prior packets, has vector error at most

\[
 C B\sqrt{R h_+}
 \tag{2}
\]

with failure at most \(R2^{-J/2}\) for each fixed context. Constants
can be enlarged to cover integer parts. The reason is a change of law
on one whole block: \(D(\nu^{\otimes s}\Vert\mu^{\otimes s})\le1/128\),
so a second-moment success event under \(\nu^{\otimes s}\) still has
fixed high probability under \(\mu^{\otimes s}\). Independence is
required inside these statistical blocks. Pairwise-independent rows are
not a substitute for that change-of-law argument.

This note replaces the full random tape of that algorithm by a short
stored seed without making such a substitution.

For finite implementation, use a certified dyadic upper bound
\(h_+\le\widehat h\le2h_+\) on the deterministic information bound,
and take \(s=\lfloor1/(128\widehat h)\rfloor\). The same lemma holds
with an enlarged absolute constant in (2). This avoids an exact floor
test on a transcendental expression and does not ask for the inaccessible
realized posterior entropy. All subsequent row-count bounds are unchanged.

## 2. Verified generator interface and its exact access condition

We use Nisan's unconditional block-generator theorem: a finite-state test
with at most \(2^S\) states between successive random blocks can be
fooled to error \(\varepsilon\) using
\(O((S+\log N+\log\varepsilon^{-1})\log N)\) seed bits for \(N\)
blocks. Block length may be enlarged to the same parenthesized quantity.
There is no bound on computation within a block. The recursive generator
uses two-universal Toeplitz hashes with linear-size descriptions. A block
is obtained by at most \(O(\log N)\) hashes; schoolbook convolution gives
quadratic bit cost per hash and linear scratch.

Source: [Nisan, *Pseudorandom generators for space-bounded computation*,
Sections 2--4, especially Lemmas 1--3 and Theorem 1](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf).
The original statements and proofs were read, including the universal-hash
variance argument, induction on block concatenation and final error choice.
No repeated-read guarantee is imported.

In this application **one generator block supplies one Gaussian row**.
All bits needed for that row are retained while evaluating its finite
circuit, then discarded. Only the running means, completed block means,
fixed query context, coefficients and counters survive to the next row.
Thus the test reads its random blocks once and satisfies precisely the
verified theorem. Internal reuse of the currently stored block is allowed.

The same stored seed is restarted for another context or another query.
This does not require a theorem for a machine that rereads an old tape:
each fixed-context statistical test is a separate one-pass test. A finite
union bound, not a many-pass simulation, establishes one seed event for
all contexts. No test in that union streams over the context list.

## 3. Finite contexts avoid assuming continuity of rounded decisions

Assume for the moment the following counted circuit bounds, subsequently
supplied by `EXPLICIT_COMPILER_EXPONENT.md` and the physical moment bridge:

* packet and mark dimensions are at most \(C\log^8(en)\);
* at most \(C\log^{16}(en)\) prefixes and moment-call indices occur;
* the number of coordinates in a query context is at most
  \(C\log^{16}(en)\);
* context range logarithms and exact row continuity-bound logarithms are
  at most \(C\log^{74}(en)\);
* row dependence on a variance coordinate can be one-half-Hölder at zero;
  dependence on the Gaussian packet is Lipschitz on the specified caps;
* a requested precision of \(b\) bits can be served in time
  \(C(2+b+\log^{58}(en))^{16}\) and space
  \(C(2+b+\log^{58}(en))^6\), counting the coefficient/matrix interpreter
  but treating the original activation evaluations as primitives.

Quantize every varying context coordinate with \(C\log^{100}(en)\)
fractional bits. Fixed prefix coefficients have that precision as well.
Only finite grid contexts are passed to the sampling routine. Including
range bits, signs, call indices and all acquired prefixes, the logarithm
of the number of possible contexts is at most

\[
 C\log^{116}(en). \tag{3}
\]

These grids are not stored or searched by the implementation. At a query,
round its actual context once and evaluate that context. The change of the
exact moment due to this rounding is negligible: even a one-half-Hölder
bound gives at most
\(\exp(C\log^{74}(en)-c\log^{100}(en))\).
The physical moment recurrence separately transports this error. We do
not assert that the rounded arithmetic program, a median, or a branch
decision is Lipschitz. Source-prefix acquisition error is handled by
the companion's parameterwise comparison to the same ideal posterior,
not by conditioning on private selected packets.

Choose an odd number \(J\le C\log^{116}(en)\) of statistical blocks,
large enough that the failure in (2), summed over (3) and all vector
coordinates, is at most a prescribed fixed fraction of \(\delta\).
The constants may depend on the fixed confidence. Every block has
\(s\le n\) rows. All guarded intermediate moment values are included
in (3); therefore the one resulting event covers the actual seed-dependent
values encountered later in the query recursion.

## 4. Finite Gaussian rows at a sufficiently small failure probability

Generate one Gaussian coordinate from a uniform dyadic cell midpoint,
using the Gaussian quantile clipped at

\[
 T^2=C\log^{120}(en). \tag{4}
\]

Use \(C\log^{120}(en)\) uniform bits per coordinate, with a larger
constant than that in \(T^2/(2\log2)\), and evaluate quantiles and row
functions to \(C\log^{120}(en)\) bits. The usual within-cell coupling
to an exact uniform has Gaussian-coordinate error at most

\[
 \sqrt{2\pi}\,e^{T^2/2}2^{-b}+2^{-b'}
 \tag{5}
\]

when the exact Gaussian lies in the clipping interval. Both positive
integers \(b,b'\) are chosen with sufficiently large fixed constants
in the displayed logarithmic power. This error times the exact capped
row Lipschitz bound is smaller than \(n^{-10}\). Accumulation over
at most \(n\) terms only adds \(O(\log n)\) bits.

For a fixed context the probability that any Gaussian in its truly random
row experiment lies outside the clipping interval is at most
\(2JsD e^{-T^2/2}\), where \(D\le C\log^8(en)\) is the packet
dimension. It is \(\exp(-c\log^{120}(en))\), after enlarging constants
and width. This is small enough to sum over all contexts in (3).
Using only an \(O(\sqrt{\log n})\) cutoff would not justify this
particular per-context union argument.

The scalar Gaussian-quantile routine is the finite interval CDF/bisection
construction already supplied in `DENSE_BUDGET_ROBUST_CUBATURE.md` and
its numerical inputs. For completeness, integration on \([-T,T]\) of
the exponential Taylor polynomial gives absolute CDF precision with
polynomially many terms in \(T^2+b+b'\); the positive lower density on
this interval converts it to the requested coordinate precision.
This has polynomial time and space and fits the much larger row-interpreter
bounds used here. No stored quantile table is needed.

Under truly random finite blocks, the implemented estimate consequently
has the error (2), plus negligible deterministic rounding, for all the
finite contexts except on total probability at most the allocated
fraction of \(\delta\).

To apply the generator per context, define a Boolean failure test against
its proof-only exact target moment. The target lies in a known bounded
interval by (1), so it has a rational approximation to much better than
the allowed error with \(C\log^{120}(en)\) bits. It is a hardwired
threshold of the **proof test**, not an oracle or retained coefficient
of the decoder. Use separate success/failure margins so this threshold
rounding cannot affect the assertion. Nonuniform finite-state tests are
covered by the generator theorem.

## 5. Count every retained bit and operation

Between row blocks, storing all \(J\) completed block means in
\(R\) coordinates with \(C\log^{120}(en)\) bits each costs at most
\(C\log^{244}(en)\) bits. Current contexts, retained scalar prefixes,
small cached coefficient arrays and counters fit below this bound.
The source panel and its instructions have their separate smaller
counts in the compiler/initialization notes. A generator block therefore
has length at most \(C\log^{244}(en)\), enough for both the state
bound and the \(C\log^{128}(en)\) Gaussian-row bits. Enlarging its
constant makes its fooling error small enough for (3).

There are at most \(n C\log^{116}(en)\) rows per vector integral.
The generator seed uses at most \(C\log^{245}(en)\) bits. Hash
evaluation for every row and every one of at most
\(C\log^{16}(en)\) moment calls costs at most
\(n C\log^{621}(en)\) bit operations: charge
\(C\log^{489}(en)\) per generated block, then add 116 and 16.

At requested precision \(C\log^{120}(en)\), the row interpreter uses
at most \(C\log^{1920}(en)\) operations and
\(C\log^{720}(en)\) live bits/register storage. It clears this
scratch before requesting the next independent random block. The entire
query therefore has bounds

\[
 \text{work}\le C n\log^{2052}(en),\qquad
 \text{retained state plus peak query workspace}
       \le C\log^{722}(en). \tag{6}
\]

The extra two powers in the space display allow conservative instruction
addressing and scalar arithmetic bookkeeping. Sorting the block means,
matrix recomposition and deterministic context rounding fit below (6).
These are deliberately loose, **enumerated** exponents, not assignments
to an unspecified polynomial. The largest exponent comes from a very
conservative rational matrix interpreter, not from input dimension or
network depth. The constants remain fixed-problem dependent.

The seed is sampled once, independently of the complete training source.
Apply the generator guarantee to each fixed finite-context failure test
and sum over (3). Include finite-Gaussian coupling and median failures.
This gives one seed event of probability at least \(1-\delta\), with
an appropriate local failure allocation, on which every prefix/context
estimate has (2) plus negligible rounding. Subsequent adaptive query
selection is covered because the implemented decoder is one fixed,
repeatable function of that seed and current state.

For every fixed problem, \(n\log^{2052}(en)=o(n^2)\). This is an
eventual dense-budget bound, not a useful practical crossover estimate.
All loops have finite prescribed lengths; a bad-state guard uses the same
resource cap and a fixed dummy answer. No rejection-sampling stopping
time, infinite integral, fitted density or scalar-training replay appears.

## 6. Numerical scope and assembly dependencies

The explicit exponents in (6) use the displayed compiler interface and the
query-whitening extension in Section 10 of
`RECALIBRATION_FREE_MOMENTS.md`. The complete assembly and its isolated
internal checks are linked from `QUADRATIC_RESOURCE_RESULT.md`.
The original arithmetic/activation-primitive convention
is unchanged. If a supplied activation evaluator itself uses space
\(O(b^e)\), its internal workspace contributes a further
\(O(\log^{120e}(en))\); a universal bound over arbitrary evaluator
degrees does not follow. A bit-time claim needs the corresponding time
interface. Analyticity alone is not a computability assumption.

The exact physical passive-query comparison, buffered-Gram moment bound,
and whole-trajectory probability event are the companion's obligations.
This note proves the short-seed implementation only under those interfaces.
It specifically does not rerun the earlier repeated-read dense evaluator
in `PRG_RECOMPUTATION_AUDIT.md`; that obstruction remains valid for that
different access pattern.

Actual scientific inputs: the complete original Nisan paper; the current
study's `DENSE_BUDGET_ROBUST_CUBATURE.md`, `PRG_RECOMPUTATION_AUDIT.md`,
`EFFICIENT_QUERY_INFORMATION.md`, `FAST_SMALL_MATRIX_FUNCTIONS.md`,
`PHYSICAL_NOISY_PROGRAM_BRIDGE.md`, and the supervisor's explicitly stated
compiler and posterior-block interfaces. New companion proofs will be
read completely before final assembly. Research/proof skills were applied;
the custom notation skill remained permission denied. No other study,
code, experiment or Git operation was used for this numerical sublemma.
