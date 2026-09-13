# Revised C-H3: resource accounting and recorded-run postprocessing

2026-09-13. Author analysis of the fixed predeclared validation records; no new
trajectory, initialization campaign, Git write or maintained-code edit was
performed for this report. The original compiler and original static report
are unchanged. This report distinguishes measured costs of the recorded
`bb786034689619d667177fff9cc548262b8d2651` implementation from symbolic costs
of the corrected candidate.

The output is a finite approximation of the H2 population equations. Population
points discretize same-layer joint laws. They are not neural width or paired
rows of a neural middle matrix. All limits and observations retain physical
time `T=1/200`, the stated tanh architecture and unhalved loss, and the fixed
represented two-arc law family, including its nonorthogonal atomic endpoints.

## 1. Counts for the initializer

Write Q for initialization quadrature nodes, P1,P2 for population nodes,
d1,d2 for retained feature counts, N for Chebyshev degree, m for represented
data nodes, and B for the input block size. The implementation currently uses
equal population counts P1=P2=P, but the runtime formulas below display the
separate counts. All these numbers are independent of neural width.

The polynomial core has

```
d1_core = binomial(N+4,4),   d2_core = binomial(N+2,2).
```

The bounded exhaustive prefix adds at most N+1 retained words across the
populations, with literal duplicates suppressed. It can add unretained
dependencies to the dictionary DAG. The first three observed orders have

| N | d1 | d2 | d1*d2 | Dictionary DAG nodes |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 5 | 3 | 15 | 14 |
| 2 | 15 | 6 | 90 | 41 |
| 3 | 35 | 10 | 350 | 83 |

These counts are present in every original corresponding record. They are
actual feature counts, not numerical ranks. There is no eigenmode deletion.
The chosen ridge is `eta_N=1/[1024(N+1)^2]`.

### Fast core and tails introducing no new action

The first population's complete initialized Gaussian tuple has dimension
four, `(g1,g2,zeta1,zeta2)`, and the second has dimension two, `(xi1,xi2)`.
The two source-response constants and the forward variance are determined
by Q-point Gaussian integrals. The raw feature tables and their two active
named-source partials are evaluated on these joint tuples. The contraction
uses the contained bounded-integrand identity

```
C = E2[partial_xi psi2] E1[psi1 h]^T
    + E2[psi2 H] E1[partial_zeta psi1]^T.
```

Each derivative list has two columns. The second summand retains the reverse
response. Extra forward innovations are integrated out only of this scalar
contraction; they are not set to zero in an asserted action law. No tensor
quadrature is formed, and adding core polynomial features does not increase
these Gaussian dimensions.

Chebyshev recurrences use `O((Q+P)N)` work for the fixed six core coordinates;
forming their fixed-coordinate products and two partials uses
`O((Q+P)(d1+d2))` work. A no-new-action tail costs its own finite DAG evaluation,
with cached values and two partials per node. The raw Grams cost
`O(Q(d1^2+d2^2))`. The small response contractions cost
`O(Q(d1+d2)+d1*d2)`. These counts omit elementary-function and scalar-precision
cost, treated below. The implementation's resource estimator is deliberately
larger, including an `(N+1)(d1+d2)` factor and both Q/P workspaces.

Inverse-Cholesky normalization additionally costs

```
O(d1^3+d2^3)                         factorization/triangular inverses,
O(P1*d1^2+P2*d2^2)                  transforming population feature rows,
O(d2^2*d1+d2*d1^2)                  D=T2 C T1^T.
```

The last right transpose is essential. Raw Q Grams and the raw contraction
are reused while the marks are replayed at P. In the fast implementation,
large Q raw/derivative tables are explicitly released before P replay;
small Gram/coefficient arrays remain. A conservative workspace bound is
`O((Q+P)(d1+d2+N+L_tail)+d1^2+d2^2+d1*d2)`. The temporary partial arrays have
exactly two components per feature. Initialization's Q and population P
are separate numerical axes.

All 12 recorded trajectories used this fast path. Their metadata says
`initialization_strategy=tanh-core-bounded-contractions` and
`epsilon_cov_used=false`. They do not measure generic source-compiler
throughput or source-regularization removal.

### Generic bounded-word source program

The generic compiler first forms the finite union of both raw dictionaries
and all terminal `A0 psi1` / `A0* psi2` calls. Let L be its canonicalized node
count, S its named-source count, and E its scalar/response-edge count.
The response links give `E<=2L+S^2`. Each new call uses persistent Q-point
operand arrays, forms a Gram extension plus `epsilon_cov I`, appends a
Cholesky row and computes a frozen-source derivative expectation by reverse
AD. Previous source variables are not recomputed. One conservative count is

```
O(Q*S*E + Q*S^2 + S^3)
```

before final raw Grams/contractions and normalization. Source covariance
work is quadratic in S times Q; dense triangular solves sum to cubic S
work. AD traverses the finite graph per call, skips only exact zero response
arithmetic, and retains every named coordinate. It does not store a
Q-by-L-by-S derivative tensor. The compiler retains at most one P replay cache
alongside its Q values, so its workspace is

```
O((Q+P)(L+S+d1+d2)+S^2+d1^2+d2^2+d1*d2).
```

Both orientation contractions come from that same complete source union.
The forward C is selected once, and runtime uses its transformed matrix and
transpose. The separate `C_reverse` is a diagnostic; it is not a fitted or
independently substituted reverse map. At finite Q and epsilon the two
numerical estimates need not coincide. Neither is claimed to be an exact
canonical contraction before the stated numerical limits.

The explicit size limits can reject a requested finite order. Such rejection
does not silently narrow the dictionary or remove modes. It also does not
make arbitrary high orders practical. In this particular encoding, the first
new bounded source wrapper occurs at code 60 (`sin(A0 1)`), so a literal
degree/prefix coupling first meets it only after the core has become very
large. Generic small fixtures are statically tested separately. The finite
convergence hierarchy and demonstrated first-order practicality are distinct
claims; no bound converts an accuracy target into a manageable N.

## 2. Nonlinear RHS, Heun steps and input blocking

Let

```
K = ceil(m/B),
R = 2P1+P2+d1*d2
```

be the number of input blocks and the number of moving scalar coordinates.
An explicit Heun step evaluates the whole nonlinear RHS twice and creates
one provisional moving state before the final update. Gates, readout,
residuals and both action orientations are recomputed from the current or
provisional state. The fixed input law and frozen marks are shared by stage
states. There is no saved path and no runtime Gaussian source call.

The corrected candidate explicitly evaluates

```
b2 @ (M @ a),       b1 @ (M.T @ d).
```

Consequently one RHS has algebraic work

```
O(m*(P1*d1+P2*d2+d1*d2))
```

plus gate evaluation, fixed-array validation, and O(R) velocity initialization.
There are O(m(P1+P2)) scalar activation/gate evaluations. The coefficient
arrays for one block are d1-by-B and d2-by-B; field arrays are P1-by-B and
P2-by-B. The additional block workspace is
`O(B(P1+P2+d1+d2))`. The three accumulated velocities occupy O(R). Heun's
provisional state, two velocity triples and endpoint update require only a
constant number of R-sized buffers. A conservative live-step allowance is
six R-sized arrays in addition to fixed marks and block work; the exact peak
also depends on NumPy expression temporaries and the caller retaining the
input state. `evolve` makes an initial full state copy, so its input state and
copied fixed marks can coexist until the call returns.

For n_t steps the evolution work is twice n_t RHS evaluations plus O(n_t R)
updates. There is no factor depending on an earlier transcript length. The
within-step convention interpolates only the two endpoints of the containing
step. The validation driver separately retains midpoint/final/restarted
states for its restart check; that extra diagnostic memory is not the minimum
continuation state.

The recorded `bb78603` code instead used left-associated expressions

```
(b2 @ M) @ a,       (b1 @ M.T) @ d.
```

For every input block these form P2-by-d1 and P1-by-d2 temporaries. Their
additional per-block work is
`O((P1+P2)d1*d2)`, followed by block contractions with cost
`O(B(P2*d1+P1*d2))`, in addition to the usual coefficient formation. Thus
the old recorded RHS is bounded by

```
O(K*(P1+P2)*d1*d2
  +m*(P1*d1+P2*d2+P2*d1+P1*d2+d1*d2)).
```

Its extra workspace contains `O(P2*d1+P1*d2)` entries. The original paired
frozen-upper observation had the analogous left association. The coordinator
changed these associations after the runs; the exact-real equations agree,
but floating arithmetic and measured runtime can change. Every timing below
belongs to the old association. None is relabelled as a measurement of the
corrected candidate. Independent reproduction of the corrected candidate is
a separate future validation step.

Neither version forms a P2-by-P1 matrix: the only evolving matrix is d2-by-d1
M. These counts expose every finite factor multiplication rather than treating
an action as a unit-cost oracle.

## 3. Retained state, words, and precision storage

The saved state arrays are `(b1,g,w,p1,b2,c,p2,M,D)`. They contain

```
S_state = P1*(d1+5)+P2*(d2+2)+2*d1*d2
```

real scalars. The finite data representation adds 4m scalars: two normalized
input components, label and probability per atom. Initialization returns
`P*(d1+d2+4)+d1*d2` scalars before the solver adds its moving copies. Static
metadata is a finite JSON record of configuration and counts, not a source
tape. Exact restart files separately encode every working scalar and the
represented law; they contain no clock or target trajectory.

For float64, array payload is exactly `8*S_state` bytes. This excludes ndarray
object headers, metadata objects, package imports and temporary buffers. The
reported `metadata_utf8` is encoded JSON size, not Python dictionary heap size.
The process peak RSS includes all of these plus the validation driver's
retained states, observations, allocator behavior and interpreter/libraries.
It must not be equated with the state payload.

Object arrays first store one pointer per entry. Decimal entries additionally
own Decimal scalar objects. A rational `Fixed` entry stores an object with
references to integer `units`, integer decimal `scale=10**digits`, and its
precision. The current retained-array counter includes

```
ndarray pointer payload
+ sum(sizeof(each scalar object))
+ sum(sizeof(units integer)+sizeof(scale integer)) for Fixed entries.
```

It counts per-entry integer storage, without deduplicating shared immutable
integers, and does not include the common precision integer separately per
entry. It remains retained-object accounting rather than exact unique process
heap accounting. For a magnitude bounded by R, the units integer has
`O(digits+log(1+R))` bits and scale has O(digits) bits. The old recorded counter
included object pointers and Fixed shells but omitted units and scale integers.
That omission is corrected by decoding the saved exact final restart, applying
the current byte counter, and separately reporting each component; no solver
step is performed.

Initialized words and the code decoder's cache are process-level objects
outside those state arrays. Core dictionaries have the DAG counts tabulated
above and are transient after ordinary initialization. A retained generic
compiler additionally owns its finite DAG, scalar coefficients and word-object
mapping until explicitly discarded. The current exact-word module's static
decoded-prefix cache starts with four roots and grows with every requested
code and its dependencies. For the intended prefix through N it has at most
`max(4,N+1)` entries, including invalid-code markers. Valid entries retain
Word slots, parent-reference tuples, cached hashes, operation references and
exact Fraction scalars/envelopes. Rational numerator/denominator bit sizes
must be counted as well as their pointer shells. Direct additional decoder
requests can enlarge that process cache; no claim bounds arbitrary user
requests by the current solver's N. The recorded first three orders query
only the first four natural codes. A restart requires no full earlier
dictionary cache or initialization program.

There is no hidden infinite field in this accounting: the Gaussian carriers
are initialization integration domains with explicit finite sample arrays,
words are finite syntax, and all runtime population arrays and coefficient
matrices are counted.

## 4. Elementary arithmetic and temporary series

Scalar-operation counts do not by themselves bound high-precision bit work.
Float64 uses fixed-size hardware and NumPy elementary functions. Decimal
operations use digit-dependent scalar storage and operation costs; no timing
constant independent of requested precision is asserted.

The rational backend is an actual executable refinement. Its retained values
are fixed-point integers, but elementary-function routines use temporary exact
Fractions. Addition/multiplication/division of these intermediate numerators
and denominators have costs depending on their bit lengths. These Fractions
are not bounded by the storage of one final Fixed scalar.

Concretely:

- `sqrt` uses integer square root of `units*scale`.
- `ln` first performs finitely many powers-of-two shifts to [1,2], then an
  atanh series with ratio at most 1/9; it also evaluates the log-two term.
  Term count depends on precision and the shift count.
- `exp` scales the magnitude to at most 1/2, sums an exact rational series,
  and applies finitely many exact squarings, then possibly a reciprocal.
  The guard and term count depend on precision and input magnitude. Numerator
  and denominator bit lengths can grow considerably during exact squaring.
- `sin` and `cos` compute rational Machin pi, reduce the input, and sum a
  Taylor series. Pi, range reduction, and the running rational sum have their
  own precision-dependent intermediate sizes.
- Halton generation retains exact digit numerators/denominators before
  conversion; Box–Muller uses log, square root and trigonometric evaluations.

At any fixed finite numerical program and positive regularizers these loops
terminate under the supplied elementary-arithmetic arguments, but this report
gives no uniform efficient bit-complexity or elementary-series memory bound.
One may count actual series terms and multiply integer-operation counts by
their realized bit costs. The implementation's array estimate such as
`scalar_count*(192+digits)` estimates retained array/object storage; it is not
a certificate covering every transient exact rational numerator/denominator.
Peak RSS from the executed runs includes those transients. The declared
external RSS/time ceilings provide operational stopping, not a proved
accuracy-to-resource map.

## 5. Original measurements and labelled postprocessing corrections

The read-only analyzer is `H3_v2_analyze.py`; it accepts a plan, a run directory,
and a fresh output directory. It verifies each configuration and plan hash,
checks every recorded artifact hash, reads NPZ with `allow_pickle=False`,
recomputes paired RMS motion from saved same-population arrays and weights,
and lists every comparable declared pair. It imports no training integrator.
With `--recount-state`, it imports only the canonical restart loader/byte
counter to reconstruct saved values and calculate storage/mark diagnostics.

For the existing 12 records, outputs are

- `data/generated/observable_hierarchy/H3_v2_author_analysis_20260913_01/summary.json`;
- `data/generated/observable_hierarchy/H3_v2_author_analysis_20260913_01/summary.md`.

All 12 configurations and all retained output hashes matched. All 12 records
report operational pass and exact midpoint restart under the original
working arithmetic and step partition. Worker totals sum to 18.8436 CPU
seconds and 18.8743 wall seconds; the supervisor charged 19.49 CPU seconds,
which includes its sampled accounting. Maximum recorded worker peak RSS was
57,339,904 bytes (54.6836 MiB). Tiny float phase CPU times were recorded as
zero at the timing resolution; they are kept as recorded, not replaced with
invented positive durations. Total times also include observations, restart
checks and file operations, so they are not just initialization plus evolution.

Some representative original measurements are:

| Run | Init CPU s | Evolve CPU s | Total CPU s | Retained state bytes |
| --- | ---: | ---: | ---: | ---: |
| atom_n1 | 0.08918 | 0.05598 | 0.21311 | 123120 |
| atom_n2 | 0.10272 | 0.05598 | 0.25863 | 230816 |
| atom_n3 | 0.10127 | 0.06796 | 0.32116 | 431584 |
| arc_n2 | 0.09719 | 0.09994 | 0.34102 | 230816 |
| arc_n2_joint_refine | 0.36387 | 1.22720 | 2.56239 | 918944 |
| tiny_decimal40 | 0.03382 | 0.02797 | 0.18173 | 30240 |
| tiny_rational24 | 0.61298 | 0.64368 | 4.38307 | 36672, corrected |
| tiny_rational36 | 1.30042 | 1.31536 | 9.39320 | 38972, corrected |

The rational records originally said 17,280 bytes for each tiny state. The
postprocessed corrections add 19,392 bytes at 24 digits and 21,692 bytes at
36 digits for their integer units/scales. Float64 and Decimal retained-array
counts did not change. The exact working values and original timings are
unchanged by this bookkeeping correction.

The predeclared plan also requested initialization conditioning diagnostics,
but the original records did not store the raw Q Grams or their condition
numbers. They cannot be recovered from a normalized mark table without the
discarded normalization transform. The added diagnostics are explicitly the
P-rule frozen normalized-feature Gram `b_l^T diag(p_l)b_l`, calculated in
float64 from exact restart values, together with `||D||2` and `max|b_l|`.
They do not substitute for the missing original raw-Q diagnostics or certify
conditioning at other orders. For the Q=2048/P=1024 base runs:

| N | P-Gram condition 1 | P-Gram condition 2 | D operator norm | max abs b1 | max abs b2 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 1.03168 | 1.00646 | 1.38418 | 3.13426 | 2.01317 |
| 2 | 1.17478 | 1.02854 | 1.38510 | 5.84039 | 3.68726 |
| 3 | 1.69956 | 1.13151 | 1.40828 | 8.45270 | 5.50030 |

The final predictions were saved only on 128 circle directions at `T=1/200`.
All comparison statements here concern that panel, not a whole-circle supremum
or time-uniform quantity. On the arc law, the N1/N2 panel difference is
`9.98e-7`, whereas N2/N3 differs by `7.88e-5`. At N2, doubling only Heun steps
changes the panel by `2.70e-12`; the declared joint Q/P/input/time refinement
changes it by `5.99e-6`. A small difference between two choices does not bound
either choice's error. No monotone accuracy conclusion follows from these
orders or refinements.

Paired RMS hidden motions in the base runs are approximately `2.28e-6` to
`2.74e-6`, depending on layer/order/law. These are motions of the computed
finite closures. They are recomputed from the saved frozen/current pairs on
each population's own rows; no independent coupling or cross-population
pairing is substituted. Postprocessing the float64 diagnostic arrays differs
from the high-precision recorded RMS scalars by at most about `1.8e-18` in
the tiny precision runs. Decimal40/rational24/rational36 saved prediction
arrays coincide after rounding to float64; that observation does not prove
their exact working states or errors coincide below the saved precision.

## 6. Source provenance, tests and reproduction

Every original record gives the same five module hashes below; these and the
producer hash were checked against Git objects at
`bb786034689619d667177fff9cc548262b8d2651` using only the assigned study paths.
These hashes, rather than current source timestamps, identify the measured
implementation.

| Recorded source | SHA-256 |
| --- | --- |
| H3_v2_fixed.py | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| H3_v2_arithmetic.py | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| H3_v2_compiler.py | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| H3_v2_initialization.py | `f4b580fc7dcbe4206ec626d4b20df37030e8e0c13cffbd08b49d7de611772e10` |
| H3_v2_solver.py | `bc82b22b948e65cc1ca7bfca4d45defcde59ef30f882f7a04a5a113a21b44ea8` |
| H3_v2_validate.py | `fcf25664808589f6f1a9e85e4c17d103328325d9026a4d879c29e36b0787bb0f` |

The current counter/loader used for the labelled memory and mark diagnostics
had solver hash `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605`.
It includes the corrected probability validation and storage accounting, plus
the newly parenthesized products. The latter are not executed by this read-only
restart postprocessor. No new trajectory timings are attached to that hash.

`H3_v2_compiler_tests.py` is a canonical-import-only unittest suite, with no
study loader, workspace path or output-file dependency. Its nine tests cover
the previous static checks, now using exact initialized Words: full grammar,
both action directions, frozen named AD checked by finite differences,
persistent source values, Q/P replay, dependent and zero sources, two precision
backends, and preallocation resource rejection. All nine passed in 0.848
seconds under the candidate loader. The compiler itself remains at its
original hash above. The test file hash is
`8a5955ad47df01a6110e8b5f3b64264b414e8ee70696e7f93250dcdf9dbb17cb`.

The analyzer hash is
`6c0ae411f567a94ff51e286a09c8f2fec2b90c5d73055ee083c6699f65e75347`.
Its 12-record processing used 0.190 CPU seconds and ran no trajectory. The
assigned postprocessing ceiling was 10 CPU minutes. The exact commands from
the shared checkout are:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B studies/observable_hierarchy/H3_v2_candidate_loader.py studies/observable_hierarchy/H3_v2_compiler_tests.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B studies/observable_hierarchy/H3_v2_candidate_loader.py studies/observable_hierarchy/H3_v2_analyze.py --plan studies/observable_hierarchy/H3_v2_run_plan.json --runs data/generated/observable_hierarchy/H3_v2_author_validation_20260913 --output data/generated/observable_hierarchy/H3_v2_author_analysis_20260913_01 --recount-state --source-revision bb786034689619d667177fff9cc548262b8d2651
```

For a fresh repeat, choose a new output directory; the analyzer refuses to
overwrite one. In an installed canonical package the test and analyzer run
directly, without the study candidate loader. The source-revision argument is
a provenance label; record/source hashes are the authoritative checks. All
original plan, records, observation arrays and exact restarts remain unchanged.
