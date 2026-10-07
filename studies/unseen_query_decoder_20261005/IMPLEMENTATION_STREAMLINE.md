# An executable core and bounded-memory scheduling

2026-10-07. Scoped author design for the existing unseen-query study. This
note reorganizes the current finite algorithm and derives exact scheduling
identities. It supplies no implementation, experiment, independent review,
promotion, new accuracy theorem, or GPU speedup claim.

The useful implementation target is a deterministic finite interpreter with
three phases: acquire each source and its selected metric; advance its
compact scalar state; regenerate source rows for a new query. The numerical
contract must be fixed before acquisition. Row tiling, shared coefficient
preparation, and exact reduction trees preserve that contract. Replacing its
samplers, grids, rank decisions, or rounding arithmetic requires additional
validation and sometimes a different probabilistic proof.

## 1. Contract and units

Keep the physical network, independent Gaussian initialization, zero
readout, all trained hidden layers, mean-square loss, mobilities, analytic
activation class, full fitting/source label intersection, and all width and
confidence gates of `TWO_GAP_CLOSURE_RESULT.md`. The prediction comparison
remains uniform over the input sphere and real physical time, including the
fitted endpoint, against an independent dense network at the same width.
Its explicitly instantiated mesh coefficient does not make its leading
dense coefficients numerical functions of the advertised parameters.

Setup may inspect a completed independent virtual source. It is not online.
A query receives the current compact state and retained seeds, uses no test
label, and does not integrate training again. The exact zero-label branch,
small-positive-label precision charges, finite access interfaces, and
unpromoted status remain. None of these qualifications is changed here.

Use the cost notation of `CLOSURE_COMPOSITION_COSTS.md`: dense width is
\(n\), hidden depth is \(L\), \(R\) bounds the actual named fields,
calls and packet coordinates, \(w\) is bits per numerical word including
integer parts and accumulation guards, and \(J\) is the odd ensemble size.
The training count is \(m\), input dimension is \(d\), population
feature-Gram gap is \(\gamma>0\), label RMS is
\(Y=\|y\|_2/\sqrt m\), activation envelope is \(\beta\), and total
failure allowance is \(\delta\), as in the preserved theorem.
The confidence moment order is \(p\); it is not \(w\). There are
\(P\le CR^2\) scalar reductions and at most \(CR\) selected packets
per member. Constants \(C\) below are absolute implementation envelopes,
not claims about practical instruction counts.

For the inner row generator let
\[
 E=1+\lceil\log_2(n+2)\rceil,\qquad
 A\le CR^2w,\qquad
 b\le C\{R^2wE+\log(N_{\rm ext}/\delta)\}.
\]
Here \(A\) is a generator block size in bits, \(b\) is a full member
input block in bits, and \(N_{\rm ext}\) is the proof's finite input/time
code count. The retained internal memory envelope is
\[
 M_{\rm ret}=C\{JR^2w+b\log(J+2)\}.
 \tag{1}
\]
It counts all member states and the outer seed. It is not a setup-memory
bound. These quantities have their explicit parameter substitutions in
`CLOSURE_COMPOSITION_COSTS.md`, equations (9)--(14).

## 2. The finite program in three phases

### Acquire the source and metric

Choose the complete source/query precision schedule first: physical answer
noise, ordinary and innovation scalar grids, answer grid, Gaussian cutoff
and precision, coefficient tolerances, metric tolerance, and all finite
guards. In particular the old source moments must already have the accuracy
needed by a future query. Tightening only query arithmetic does not repair
a coarse source.

For each outer-generated member block, construct its finite source from its
inner seed. A named row field is a deterministic instruction together with
its creation-time scalar arguments. Those arguments never change when later
scalars are appended. An ordinary scalar update has the form
\[
 C_a=Q_{h_a}\left(\frac1n\sum_{i=1}^n
 u_a(i;C_{<a})v_a(i;C_{<a})+\eta\widehat e_a\right),
 \tag{2}
\]
where \(Q_{h_a}\) is the specified nearest-grid rule, and the products
and sum are exact before division and final rounding. Each scalar mark
\(\widehat e_a\) has its assigned finite law and logical position.
Branch decisions and guards are part of the finite transcript.

Apply the existing exact finite-table selection routine, retaining at most
\(CR\) original packets and a rounded positive metric
\(\widehat M\). Retain also the member's scalar noise marks,
instruction templates, scalar coefficient arrays, and initialized compact
state. Discard the completed future scalar-answer table and full row table.
Keep the outer seed that can regenerate the member input and inner seed.
The metric construction is an inherited algorithmic interface; this note
does not replace its exact rank and selection operations.

### Advance only the selected packets and scalar state

Run the same chronology on selected packets, replacing the empirical pair
in (2) by
\[
 u_a(I;\widehat C_{<a})^\top\widehat M
 v_a(I;\widehat C_{<a}).
 \tag{3}
\]
Use the original retained scalar marks and the same rounding grids.
`FAST_LOCAL_PRECISION_TEST.md`, Section 3, gives literal equality of the
acquired scalar values on its replay event. The proof uses a uniform metric
error and the fresh-noise rounding-boundary estimate; it does not need a
well-conditioned selected metric or independence of the selected packets.
For the generated source, the conditional argument is applied before the
outer-generator transfer, as specified in `SOURCE_SEED_EXACT_QUERY.md`.

The evolving state consists of the acquired scalar prefix, selected-packet
fields, current coefficients and patch/clock counters. Future scalar answers
are absent. Thus the update is autonomous from that state and the fixed
finite instructions. Scalar marks are retained, so updates do not regenerate
an outer block. Preserve dimensionless patch coefficients: shrinking a patch
does not justify storing physical derivatives multiplied by inverse powers
of its length. The confidence refinement remains the existing patch-count
factor \(p\), degree addition \(\lceil\log_2p\rceil\), and extra
\(O(\log p)\) precision.

### Decode an unseen query by regenerating rows

Process members sequentially and retain only their \(J\) final scalar
predictions. For each member regenerate its input block, then evaluate its
source rows from the seed and immutable acquired arguments. Only fields in
the current acquired prefix are used; setup's discarded future answers
cannot enter a query during training.

At each passive hidden-layer call, first stream the empirical pairs needed
for the learned increment and conditioning coefficients. For a learned
increment represented as \(\Delta W=T C S^\top/n\), with columns of
\(T,S\) old named fields and \(C\) its acquired coefficient matrix,
compute \(S^\top h/n\) from all regenerated rows, then evaluate
\(T C(S^\top h/n)\) rowwise.

Prepare the initialized-matrix conditional mean and covariance correction
once at this fixed context. With old reverse-query fields \(U\), the
finite call is
\[
 \widehat t=Q_{h_t}(U^\top\widehat g/n+\eta\widehat e),\qquad
 \widehat y=Q_{h_y}(\widetilde m+
                 U\widetilde T\widehat t+c\widehat g).
 \tag{4}
\]
The coefficients \(\widetilde m,\widetilde T,c\) are prepared from
the acquired finite physical Gram table before exposing this innovation.
The first pass supplies prerequisite pairs, another the innovation
contractions, and a subsequent pass forms the answer and required new pairs.
A constant number of passes per layer suffices. Re-evaluation uses saved
scalar arguments, not scalar training updates. Finally acquire the readout
pair and take the median across complete source models.

The full \(U\widetilde T\widehat t\) term, physical noise floor,
and separation of innovation moments from same-call coefficient solves are
essential. Intermediate prefixes inside (4) are not asserted to have a
Gaussian posterior. The completed-call coupling and its common finite
postprocessing provide the needed law. All regenerated coordinates and
scalar marks have stable logical indices independent of tile size, execution
lane, query order, or retry count.

## 3. Exact tiling and its counted cost

Consider one pass with fixed acquired arguments. Buffer \(t\) rows, with
\(1\le t\le\min(n,R)\), in a field-major array of at most \(CR\)
words per row. Shared coefficient arrays and running pair accumulators each
use \(O(R^2w)\) bits. Do not materialize all \(tR^2\) row-pair
products: generate products in output blocks and accumulate immediately.
One row generator workspace is reused while filling the tile. Double
buffering changes only an absolute constant.

**Exact scheduling identity.** If the field evaluator returns the same
dyadic bit strings for the same arguments, and signed integer accumulators
never overflow, tiling and any tree of exact partial sums produce precisely
the untiled transcript. Indeed write finite field values as integers times
their declared powers of two. After aligning exponents, the numerator of
each empirical pair is an integer sum. Integer addition is associative and
commutative, so partitioning or regrouping the rows changes no numerator.
Apply division by \(n\), the scalar mark, and \(Q_{h_a}\) only after
the full reduction. This gives the same next scalar and branch decision.
Induction over the chronological scalar instructions proves the claim for
the whole finite program. The same argument applies to (3), which has
exact dyadic metric products, and to final affine sums in (4).

For example, fields of absolute size at most \(B_f\) with \(f\)
fractional bits require at most
\(2f+2\lceil\log_2(B_f+1)\rceil+
\lceil\log_2(n+1)\rceil+C\) signed accumulator bits for their
unnormalized pair sum. The existing word certificate includes such bounds.
Rounding each tile mean and then summing does not satisfy the identity.

With one live row-generator workspace, the added tile scratch is
\[
 C\{b+A+R^2w+tRw\}.
 \tag{5}
\]
Since \(A\le CR^2w\), \(t\le R\), and (1) pays for \(b\),
this preserves the stated retained-plus-peak training/query envelope, up to
an absolute constant. If \(g\) generator instances or \(a_{\rm eval}\)
activation evaluators run concurrently, add
\(CgA+a_{\rm eval}\mathcal S_\phi(w)\), where
\(\mathcal S_\phi\) is actual evaluator scratch. The simple certified
choice is \(g=1\); more concurrency is allowed only inside an explicitly
budgeted pool. Launching one full generator per buffered row silently adds
\(tA\) bits. Launching all members simultaneously likewise duplicates
their transient member-block and coefficient workspace.

For one tile the internal bit work is bounded by
\[
 C t\{A^2E+Rw^4+R^2w^2\},
 \tag{6}
\]
plus \(CtR\mathcal V_\phi(w)\) for a general evaluator. The three
terms are row hashing, finite Gaussian conversion, and field evaluation
with exact pair reduction. A short final tile only lowers this count.
Coefficient preparation for each passive layer costs
\(C(R^4w^2+R^3w^3)\) internally. Summing tiles, layers and members
recovers, without claiming a work reduction,
\[
\begin{aligned}
 T_{\rm query}\le{}&CJ(L+1)
 \{n(A^2E+Rw^4+R^2w^2)+R^4w^2+R^3w^3\}\\
 &+CJb^2\log(J+2)+CJw\log(J+2).
\end{aligned}
 \tag{7}
\]
General evaluator work, input/certificate access and answer output remain
additional. The internal formula and activation counts are the final
exact-query ones, not the older passive-sampling counts.

This layout exposes parallel work across buffered rows, fields whose
predecessors are complete, pair accumulators and integer limbs. A scalar
acquisition is still a global dependency barrier. Small conditioning solves
are shared once per context; no solve is repeated for each row. Selected
packet training has no factor \(n\), but its small number of packets
can limit hardware occupancy. Batching multiple user queries would multiply
their live query states and requires its own memory ledger; it is not free
parallelism in (1).

Setup has an additional \(C(nRw+R^3w)\)-bit peak, from the temporary
source table and exact metric construction, and a leading
\(CJnR^5w^3\) work term. Members are acquired sequentially. The same
tile schedule can bound device-resident row buffers, but a host-resident
table still counts toward total memory. Eliminating that table would require
a separately justified metric-selection algorithm; no polylogarithmic total
setup-memory claim follows here.

## 4. Numerical components and realistic obstacles

**Small matrices and rank.** Use the separate spectra of the two history
matrices from `SANE_DECODER_CORE.md`, Section 3. Their denominators have the
form \(\sigma^2+k_j+q_i\); no matrix of the product history dimension
need be stored. Prepare the coefficient vectors once. The residual-controlled
Jacobi construction in its Section 4 gives a finite implementation with
explicit orthogonality and reconstruction residuals. It does not require
distinct eigenvalues or stable individual eigenvectors. Preserve symmetric
rounding and construct PSD outputs by exact products of nonnegative factors;
uncontrolled final entrywise rounding can lose positivity.

The artificial floor \(\sigma>0\) is a numerical/probabilistic design
parameter and may be tiny. A well-behaved output does not prove harmless
conditioning of intermediate solves. The metric need not be inverted, but
its exact table selection does require exact rank decisions and may have
\(O(Rw)\)-bit rational intermediates. A floating-point rank threshold,
truncated SVD, or discarded small eigenvalue is a different selection or
conditioning map. Positive floors and the full covariance correction cannot
be removed as a performance shortcut under the current proof.

**Precision.** The final table uses
\(R\le Cp\beta^{201L}(m+d+2)(1+m/\gamma)Z^{5/2}\) and
\(w\le C\beta^{110L}Z\) as sufficient constructive envelopes, where
\(Z\) is defined in `CLOSURE_COMPOSITION_COSTS.md` (2). These are
conservative theorem parameters, not practical machine-word prescriptions.
Use the actual certified local tolerances when instantiating a finite
program. The tiny-label branch replaces \(Z\) conservatively by
\(Z+\log_+(1/(nY))\), including any needed patch/degree changes.
Ordinary 32- or 64-bit arithmetic has not been certified by these statements.

An exact limb implementation can parallelize the finite operations while
keeping their declared rounding points. Fusing arithmetic is semantically
safe only if it introduces no extra rounding and removes none of the named
roundings. Replacing exact reductions by ordinary floating-point matrix
multiplication, atomic summation or fused multiply-add changes the finite
map unless a separate error argument covers it. A numerical closeness test
alone does not establish the transcript equality used by the generator and
metric replay proofs.

Adaptive Taylor order, early stopping or empirical-rank compression changes
the finite program. Such a variant needs an a priori bound on every branch's
field/transcript size, fixed logical random-coordinate assignments, and a
local forcing/truncation certificate compatible with its new schedule. An
observed small last coefficient alone supplies none of those guarantees.
These changes can be explored in an explicitly uncertified prototype;
they are not consequences of exact row tiling.

**Gaussian conversion and randomness.** The certified sampler uses finite
uniform bits, clipping, a normal-CDF approximation and certified inverse-CDF
bisection. Its conservative cost is \(O(Rw^4)\) per row; this can dominate
the visible neural arithmetic. The inner generator uses
\(O(A^2E)\) bit work per row, and outer regeneration contributes the
separate term in (7). These costs and multiword arithmetic are serious
practical bottlenecks even when row field evaluation is parallel.

A standard counter-based generator such as Philox may be useful in a future
engineering prototype, but its statistical quality is not the unconditional
finite-transcript generator guarantee imported here. Replacing the inner
or outer generator requires a new guarantee or an explicitly empirical
mode. Keeping genuinely independent full random packets instead would have
to charge their storage or provide a different regeneration argument.
Likewise a hardware normal sampler or library inverse CDF needs a coupling,
cutoff and precision bound matching the finite source contract. No particular
GPU library or current API is recommended by this architecture note.

**Activations.** For tanh, `FAST_TANH_EVALUATION.md` supplies a finite
\(O(w^3)\)-work, \(O(w)\)-scratch evaluator; those costs fit the final
table with its current call counts. Its older phase call counts are not
reused. A library tanh or low-degree approximation needs its own certified
range and error. For general analytic activations the evaluator description,
work and scratch remain explicit external inputs. An analytic envelope does
not imply a fast evaluator.

## 5. What can leave the current exposition

The main implementation narrative can omit the earlier high-dimensional
Fourier/tensor quadrature, condition-number-length matrix series,
cofactor-based general interpreter, prior/posterior moment replacement,
passive population estimator and its root-width remainder, entropy-based
generalization route, and medians of repeated queries on one shared source.
They are not executed by the final exact finite-source query algorithm.
The old sixth-power memory table and old passive block-size gates likewise
do not describe it. Their files need not be deleted; a short provenance
note suffices when documenting the current construction.

Keep the exact empirical contractions, both matrix orientations and their
covariance correction, immutable field arguments, noise/grid schedule,
completed-call chronology, safe future-used marks, finite sampler,
metric replay, guard semantics, source-transcript generator and whole-source
ensemble. The finite scientific source probability, tail/endpoint argument,
physical sphere/time coding, and declared dense mesh coefficient also remain
essential theorem dependencies. A compact runtime description must not
silently remove their assumptions from the theorem statement.

The generator's hardwired candidate-transcript verifiers and bad-median
tests belong in the proof appendix. They are not executed or stored by the
model. In particular one does not enumerate exponentially many transcripts,
feed the unknown dense proof center to the decoder, or assert a one-pass
generator theorem directly for its repeated-row-read execution.

## 6. Claim boundary and next implementation artifact

| Change or claim | Status and decisive condition |
| --- | --- |
| Tile row evaluations and regroup exact reductions | Exact scheduling identity proved here, provided no overflow and identical field bits/rounding points |
| Reuse one prepared coefficient block within a fixed context | Existing finite construction; coefficients must precede fresh innovations |
| Preserve (1) with tile buffers | Derived here for \(t\le R\), one generator workspace, and separately charged evaluator concurrency |
| Remove old passive machinery from the current narrative | Supersession-aware exposition; no historical files deleted |
| GPU kernels reproduce the specified finite program | Unimplemented; requires bitwise transcript/guard tests and counted workspace |
| Floating-point reductions, Philox, adaptive truncation or empirical-rank compression | Useful possible prototype substitutions; not certified by this theorem |
| Speedup, 32/64-bit sufficiency, practical onset or polylog setup memory | Not established or measured |

The smallest useful next artifact, if implementation is authorized, is a
finite-program reference interpreter plus a tile backend for one completed
matrix call and its exact pair reductions. Validation would compare complete
finite transcripts across tile sizes and reduction trees, exercise zero and
rank-deficient histories and guarded branches, check matrix residual/PSD
certificates, and measure actual live scratch. Such a fixture would test
scheduling and arithmetic semantics; it would not test the neural theorem
or establish GPU speedup. No such implementation or experiment was run here.

## Input and authorship record

The seven assigned implementation sources were read completely:
`SOURCE_SEED_EXACT_QUERY.md`, `CLOSURE_COMPOSITION_COSTS.md`,
`SANE_DECODER_CORE.md`, `FAST_LOCAL_PRECISION_TEST.md`,
`FAST_FINITE_SOURCE_BRIDGE.md`, `FAST_SMALL_MATRIX_FUNCTIONS.md`, and
`FAST_TANH_EVALUATION.md`. Previously assigned final synthesis, numerical
benchmark, finite-source statement and bounded assembly report supplied
the theorem qualifications. Earlier open/passive statements in the local
component notes were interpreted at their stated component scope, using the
later exact-source route for the present runtime. No linked scientific file,
other study, cleanup author's artifact, external API source or experiment
was consulted for this design.

Canonical-notation instructions and their neural reference, rigorous-proof
instructions, research-contract/evidence/audit instructions and the shared
workflow were applied. HEAD/index/status were checked before writing; the
two unrelated dirty files were left untouched. Only this assigned note was
written. The scheduling proof and accounting above are author derivations,
not independent validation of either this note or inherited theorem inputs.
