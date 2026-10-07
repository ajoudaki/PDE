# Bounded check of scheduling identities and kernel fixtures

2026-10-07. **PASS at the stated scheduling and algebraic-fixture scope.**
No actionable correctness defect was found in the assigned implementation
design or its five deterministic tests. The tests pass. They do not
implement or certify the complete finite source/query interpreter, its
probabilistic guarantees, finite-word arithmetic, total memory use, or
hardware speedup.

This is a scoped check with reused current-study context, not a blind
independent scientific review. No other new review was inspected. The
only write is this report; neither design nor code was changed.

## 1. Exact tiling and the retained finite semantics

The design's scheduling claim, IMPLEMENTATION_STREAMLINE.md lines
174--192, is correct under its explicit assumptions: fixed acquired
arguments, identical finite field values, exact aligned products and sums,
no accumulator overflow, and unchanged named rounding points.

To check the identity directly, write one pair's finite operands as
\(u_i=a_i2^{-f_u}\), \(v_i=b_i2^{-f_v}\), with integer \(a_i,b_i\).
The source reduction is

\[
 Q_h\!\left(\frac{2^{-f_u-f_v}}n\sum_{i=1}^n a_i b_i
                    +\eta\widehat e\right).
\]

Any partition of the indices and any regrouping of the exact integer
sum preserves its numerator. Performing the rational division, adding
the same finite mark, and applying the same fixed-tie rounding rule
therefore preserves the next scalar. Induction over scalar acquisitions
then preserves every transcript-dependent field and guard decision.
Different operand exponents can be aligned before addition with the same
argument. The displayed accumulator allowance pays for the worst-case
absolute sum, hence also every partial sum under an arbitrary ordering.

For compact training the finite rounded metric is fixed, so
\(u^\top\widehat Mv\) is likewise an exact sum of dyadic triple products.
For an affine completed matrix answer, regrouping its exact affine sum
does not alter its prescribed answer rounding. This does not identify
the rounded metric with the exact source metric: equality with the source
transcript remains the separate rounding-boundary event in
FAST_LOCAL_PRECISION_TEST.md, Section 3.

The design preserves that distinction. It retains the same scalar marks,
metric tolerance, field evaluations and grids, and applies the generated
packet replay argument before the outer-generator replacement. The
replay proof requires fresh scalar noise independent of the whole packet
array and prior marks; it does not require different generated packets to
be independent. This is precisely the extension stated in
SOURCE_SEED_EXACT_QUERY.md, Section 3.

The exact-sum identity is a semantic statement about regrouping. It does
not imply that every possible parallel reduction tree has the same peak
space. The bounded-memory implementation must also obey the separate
output-block and workspace schedule discussed next.

## 2. Retained, device, and total memory

Let \(R\) bound fields and packet coordinates, \(w\) bound numerical word
bits with guards, \(J\) be the ensemble size, \(A\) be inner-generator
block bits, and \(b\) be member-input bits, as in the design.
Its one-workspace tile bound is

\[
 C(b+A+R^2w+tRw),\qquad 1\le t\le\min(n,R).
\]

Since \(A\le CR^2w\) and \(tR\le R^2\), the transient amount is
\(O(b+R^2w)\). It fits the retained-plus-peak envelope

\[
 C\{JR^2w+b\log(J+2)\},
\]

because \(J\ge1\) and \(\log(J+2)\ge\log3>0\). The final \(J\) scalar
predictions also fit. This verifies the arithmetic in design (1) and
(5), at the inherited row-evaluator workspace interface.

The design explicitly excludes materializing \(tR^2\) row-pair products.
Products must be consumed in blocks into the shared accumulators.
Parallel partial reductions are permitted only when their live intermediate
sums also fit that workspace. Constant double buffering is harmless.

The additional \(gA\) generator and
\(a_{\rm eval}\mathcal S_\phi(w)\) evaluator charges correctly expose
concurrency. A generator per row would add \(tA\), potentially larger than
the tile field buffer. Concurrent member decoding duplicates member-block
and coefficient scratch. Concurrent user queries duplicate live query
state. The note does not silently include any of these schedules in the
one-workspace bound.

Setup remains materially different. The additional
\(C(nRw+R^3w)\) peak agrees with the finite-table selection and exact
rational construction in SANE_METRIC_PACKETS.md, Sections 4.2--4.3,
after the local word-precision substitution. Sequential member setup
avoids multiplying that full temporary table by \(J\); all retained
member states still count. A host-resident table remains part of total
memory even when only a tile is resident on the device. The design
states these qualifications explicitly at lines 242--248.

No allocator, limb layout, GPU buffer manager, or live-memory tracer is
implemented by the test fixture. Its Python object storage is not an
implementation of these bit-memory envelopes.

## 3. Query chronology and removed historical machinery

The query schedule at design lines 124--162 agrees with
SOURCE_SEED_EXACT_QUERY.md, Section 3. Each member regenerates random
input and evaluates old row instructions using already acquired,
creation-time scalar arguments. It forms new empirical contractions by
streaming rows and appends passive forward calls. It never recomputes
training scalar updates or reveals discarded future scalar answers to a
current-prefix query.

The learned increment
\(\Delta W=TCS^\top/n\) is evaluated through its actual empirical
contraction \(S^\top h/n\). The initialized-matrix call retains the
complete \(U\widetilde T\widehat t\) covariance correction; coefficients
are prepared before fresh innovation moments are acquired. The scalar
barrier and constant number of streams per layer are inherited from
the exact-query construction. Tiling does not reduce the number of
scalar dependency barriers.

The narrative removals in design Section 5 are justified at this runtime
scope. The exact-source query executes neither the earlier population
expectation replacement nor the passive sample estimator, so their
quadrature, passive sample-size gate, and root-width comparison remainder
do not belong in its executable path. Its median is over complete source
members, not repeated passive queries sharing one source. The candidate
transcript verifiers and center-dependent bad-median tests are proof
objects; source/query execution does not enumerate them.

One distinction should be preserved when shortening future summaries:
removing the **cofactor-based general interpreter** is not removing every
adjugate or determinant calculation. The retained exact metric-selection
routine still uses fraction-free elimination, determinant-improving row
swaps, and common-denominator inverse/adjugate computations during setup.
The design keeps that routine and its rational workspace explicitly; it
does not make the broader removal claim.

The separate-spectrum matrix routine, finite normal conversion, and tanh
evaluator are inherited interfaces in the design. This check does not
reconstruct their proofs or implementation from unassigned sources.
The design makes no new certification claim for a replacement library
routine, Philox generator, floating-point reduction, numerical rank
threshold, or adaptive truncation.

## 4. What the executable tests actually establish

The command

~~~
python3 -B studies/unseen_query_decoder_20261005/test_streamline_kernels.py
~~~

completed with exit code zero: all five tests passed. The run was a
deterministic algebra check, not a neural experiment or performance
benchmark. No output or bytecode files were created.

| Test and source lines | Actual coverage | Not established |
|---|---|---|
| Packed Toeplitz, 110--121 | 480 fixed parameter combinations: widths \(1,2,3,7,8,15,16,33\), four inputs, three coefficient strings, and five chunk sizes. Compares identical low-width output bits. | Universal hashing probability, random seed distribution, fixed-width machine implementation, or speedup. |
| Generator stream, 123--137 | Depths zero through seven and four seeds; every yielded leaf agrees with independent indexed evaluation. Checks exactly \(2^E-1\) hash calls and at most \(E+1\) stack entries for depth \(E\). | A randomness theorem, arbitrary large cases by testing alone, padding/non-power-of-two output handling, byte-space measurement, or bounded storage of the test harness's output list. |
| Cached metric pairs, 139--154 | 384 exact pair comparisons over dimensions one through six, with a constructed PSD dyadic metric and eight immutable field vectors. | Metric selection, rounding/replay probability, finite-word capacity, cache invalidation logic, or end-to-end training. |
| Exact tiling, 156--162 | One fixed list of 37 signed dyadic summands and seven tile sizes, including a short final tile and a tile larger than the list. | Arbitrary reduction-tree implementation, scalar division/noise/rounding, boundary ties, overflow, guards, or complete transcript equality. |
| Indexed heap, 164--180 | Dimensions one through nine and 80 update rounds each; maximum pivot and deterministic tie order match a full scan. Heap and position-map entry counts remain fixed. | Jacobi rotations, convergence, numerical residuals, PSD preservation, machine memory, or updates made by bypassing the setter. |

Code inspection also supports the tested identities without relying solely
on those examples:

* In the packed hash, output bit \(j\) is the XOR of coefficient bit
  \(i+j\) over input bits \(i\) that equal one, exactly matching the
  reference parity computation. The last chunk may extend beyond the
  output width; the final mask removes those excess bits. Positive
  width and positive chunk size are the intended domain.
* The recursive generator visits the identity child before the hashed
  child at each level. Its leaf order therefore matches the most
  significant-bit-first indexed path. A full depth-\(E\) binary tree
  has \(2^E-1\) internal nodes, each executing one hash. The explicit
  stack has at most one pending right sibling per level.
* A cached vector \(\widehat Mv\) gives exactly the same bilinear form
  \(u^\top\widehat Mv\) because every multiplication and addition is
  rationally exact. This remains valid only while that field vector
  and the metric are unchanged.
* The heap setter changes one unordered off-diagonal key, updates both
  symmetric matrix entries, and restores the order by an upward then
  downward repair. Swaps update both position-map entries. Calling the
  setter after each individual change is essential; externally changing
  many matrix entries first would invalidate its single-key premise.

The use of Python's arbitrary-precision integers and Fraction is
appropriate for these reference identities, but removes precisely the
finite-capacity failure mode excluded by the scheduling theorem's
no-overflow hypothesis. The test docstring accurately limits its claim.
The design's statement that a full finite-program/tile fixture remains
unimplemented is consistent with the presence of these smaller algebraic
tests.

## 5. Conclusion and frozen scope

The bounded scheduling identity, memory accounting, concurrency caveats,
absence of training replay, and narrowed historical-removal claims check.
There is no new full-interpreter, numerical precision, probability, GPU,
or runtime certification to infer from this result. The untested complete
transcript, guarded-branch, residual/PSD, and live-workspace checks remain
future implementation work exactly as the design states.

Complete assigned inputs and their SHA-256 hashes:

| File | SHA-256 |
|---|---|
| IMPLEMENTATION_STREAMLINE.md | 3063f9e9b86d7e0676c537cbf6741011ddf83b0c4830969f38b6ef21fcfaef01 |
| test_streamline_kernels.py | c3e7ae1f8567cb9872ee4ffeceb53dcac0b5d39add80a65df551525835e64619 |
| SOURCE_SEED_EXACT_QUERY.md | 877823e5b1032b93ec60a95e4f879c35aeac616d0983cfb269eef0429b84b524 |
| FAST_LOCAL_PRECISION_TEST.md | af2a238a3ea1ed73059fd61321ca8408ce487399542156dc44e5e06f5a3e2f91 |
| SANE_METRIC_PACKETS.md | 1683563689c824593613cb636590ae3180f4cc897913c8ed5acb3c12170adeea |

The canonical-notation, neural-network, rigorous-math and adversarial-audit
instructions were already read in this scoped agent context and reused.
No other new review, unassigned scientific source, older study, archived
book, external API documentation, GPU benchmark, or Git operation was used.
