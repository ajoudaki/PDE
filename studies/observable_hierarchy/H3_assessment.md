# Milestone C-H3 assessment

Status: **INCOMPLETE**. The bounded reference computation below is a useful
component, not the requested arbitrary-accuracy autonomous nonlinear solver.
Two fresh complete isolated scientific reviews pass the explicitly bounded
components and identify the full milestone as not met. Separate capsule
integration review is recorded below. No full C-H3 acceptance or promotion is
asserted. This assessment closes the bounded attempt and preserves its gaps.

## Recovered foundation and preserved target

H2 has been promoted as C.4.7.9. Recovery checked its complete v3 theorem,
prototype/tests/notes, contract, dependency proofs, correction/review and
promotion records. The live five-file package matched the approved hashes,
and all seven dependency excerpts matched their maintained sources. H2's valid
completed audits were not repeated. The bounded residual preflight used its
prototype for a new source/representation question.

All new positive claims retain the exact bias-free two-hidden-layer tanh
model, Gaussian initialization, mobilities (n,1,n), residual f-y, unhalved loss
and physical T=1/200. The two action orientations are those of the same reused
Gaussian action. Finite-network identification retains the actual finite
random readout; there is no new finite-width error-rate claim.

The decisive H2 gap was the source error (H2.10): it vanishes qualitatively
but is defined using the unknown exact path. It cannot be evaluated as a
numerical stopping criterion. The present work removed a short-time stability
constant obstacle, and evaluated a small alternative approximation, but did
not complete the general source-defect producer or its terminating refinement.

## Useful evaluated reference component

The law, times, null signals, positive thresholds, tolerances, resource cap
and stopping rules were fixed in H3_contract.md before any trajectory. The law
is the exact orthogonal reference, with equal masses at (sqrt(2)e1,+1) and
(sqrt(2)e2,-1). It is inside every positive H2 neighborhood. Observation times
are 0,1/400,1/200, and the restart is at 1/400.

The autonomous coefficient system uses the initialized kernel readout and a
quadratic Duhamel increment for the two hidden layers. Its finite integral
remainder compares the approximate hidden fields directly with the actual
nonlinear population GF. The initialized forward and reverse response terms
are retained. Both motion measurements use the same initial/current population
coordinates, followed by the reverse triangle inequality for paired RMS.
No change of marginal distributions is used as a substitute for pairing.

For prediction, the code uses the cheaper initialized-kernel observation with
its own uniform error to nonlinear GF. A degree-seven Gaussian Hermite
composition gives a whole-circle evaluator with certified positive omitted
spectral mass, rather than a sampled angular maximum. The coefficient integrals
are one-dimensional and include rigorous Gaussian tails, Simpson remainders,
initial covariance uncertainty and outward arithmetic. The proof uses Gaussian
L2 completeness and finite integral remainders, not temporal analyticity.

The current candidate's final-time enclosures and errors are:

| Quantity | Enclosure / absolute error bound |
|---|---:|
| First training-averaged paired RMS | [4.4732053e-6,4.5182496e-6] |
| Second training-averaged paired RMS | [6.6076920e-6,6.7410684e-6] |
| First RMS error | <2.252213e-8 |
| Second RMS error | <6.668817e-8 |
| Whole-circle prediction change, positive witness at e1 | >.0011791368 |
| Uniform time/whole-circle prediction error, including input enclosure | <7.376364e-6 |

The whole-circle signal lower bound uses the separately accurate e1 evaluation;
it does not claim that e1 maximizes the circle norm. The delivered circle
function has a uniform error certificate. Its input-box interface includes
irrational directions through certified coordinate enclosures.

The repaired primary reference run took 6.169790 seconds: 6.166815 for
initialization and .002975 for coefficient evolution, checkpoint write/reload
and output enclosures. Peak RSS was 17836 KiB. The separate initialized circle
compiler took 4.437536 seconds, peak RSS 17380 KiB. Both use 60 decimal digits
and standard-library outward interval arithmetic. The combined independent
reproductions have the following externally measured costs; both initialize
all moments and circle coefficients afresh, write/reload the midpoint state,
continue, and evaluate the certified observations:

| Independent reproduction | CPU seconds | Wall seconds | Peak RSS KiB |
|---|---:|---:|---:|
| Scientific reviewer A | 10.72 | 20.52 | 18,728 |
| Scientific reviewer B | 10.67 | 20.47 | 18,720 |

The two concurrent reproductions were pinned to the same available CPU,
accounting for wall time near twice CPU time. Both ran under the predeclared
one-core, 8-GiB, 900-second cap. Each passed all 16 supplied tests; A also passed
eight independent attack groups, B six extra tests. Those extra deterministic
checks were separately budgeted and are itemized in their original reports.
No additional empirical producer was executed by either integration reviewer.

The main divisions have certified positive denominators: q is about .39429449
and the scalar kernel k about .23645041. Their inverses are modest. No
singular Gram inverse or thresholded covariance rank enters this reference
calculation. Roundoff is included at every elementary operation. The original
first run's nearest-rounded final total-error sum and in-memory restart were
corrected before freezing; its source and result remain preserved, and the
second run actually reloads the complete midpoint JSON.

## Error and state accounting at the bounded scope

The nonlinear approximation error is the proved Duhamel/kernel remainder;
its bound does not vanish by refining numerical integration. Gaussian tails
and Simpson integration remainders are recorded separately for every moment.
The finite reference input-law integral is exact. Coefficient time integration
uses an exact closed-form semigroup, with exponential evaluation enclosed, so
there is no unaccounted time-discretization truncation. Finite arithmetic and
initial covariance uncertainty propagate in the interval endpoints. The circle
certificate separately charges its two discarded Hermite masses, coefficient
and covariance errors, current readout uncertainty, input-coordinate error and
final output conversion. Full C-H3's more general error decomposition remains
an unmet requirement, not an assumption imported from this reference result.

The reference numerical state contains b,beta (two intervals), seven frozen
contraction intervals, exact rational elapsed certificate time, precision and
the original initialization as certificate origin. The circle adds q,v and
eight spectral coefficient intervals. Initialization streams a fixed number
of accumulators; it stores no quadrature tensor. The source fields defining
the limited observations are implicit finite initialized Gaussian expressions.
There is no neural trajectory, fitted coefficient or runtime arbitrary-action
oracle. Restart preserves all endpoints and the accumulated analytical origin.

At the declared degree/precision, all arrays and moment buffers have fixed
size; quadrature streams its samples and no step history is retained. The
executed state and kernel contain 19 intervals/38 Decimal endpoints and occupy
2,123 and 2,883 serialized bytes respectively. Exact rational polynomial
evaluation has degree at most 49; its integer storage depends on supplied
coordinate and rational time bit lengths. The validated uniform accuracy
uses the specified one/two-step evolution, not an unlimited number of restarts
at the same precision. Arbitrary new rational time encodings must also be
counted as inputs. The measured RSS includes interpreter, integrator,
serialization and certificate buffers. This is a storage statement for the
limited scalar reference interface. It is **not** a
storage theorem for a solver retaining every requested joint population or
arbitrary observation graph: those interfaces are absent.

## Why the full milestone remains incomplete

1. There is no implemented procedure accepting every positive epsilon and
   refining the nonlinear closure until a computable certificate succeeds.
   The useful reference has a fixed analytical certificate floor. H2's
   qualitative convergence does not fill this gap.
2. No explicit positive numerical subfamily radius inside the original H2
   neighborhood has been proved. A computable arc family would include both
   nonorthogonal atomic and nonatomic laws once such a radius is known, but
   that conditional construction is not the requested supported family.
3. General finite admissible same-population observation tuples, general law
   integration, both full retained joint populations and a corresponding total
   solver storage bound are not implemented or certified. The broader finite
   equations in the theory are not a certified exploratory API.

Three materially different approaches were developed before selecting the
bounded reference. The a priori route uses saturated circuit covers and
dictionary approximation; its complete useful constant/implementation chain
is missing and its literal cover has enormous sufficient cost. The residual
route uses an original-action lift and computable approximate-tail barriers;
its represented-field Gaussian integration/defect producer remains missing.
The short-time route avoids those costs and succeeds at the fixed reference
accuracy, but its fixed-order remainder does not supply arbitrary refinement.
The Hermite observation compiler improves that route's circle evaluation;
it does not refine the nonlinear dynamics.

The residual feasibility investigation gives a precise narrower obstruction.
The literal float64 H2 API stops at order 1074, before relevant new bounded
upper features at codes 1340 and 1470. An exact conditional-innovation argument
gives initial full readout-velocity defect >1/2500 for every such order. The
proposed uniform residual barrier therefore has value >2e-6 at T and cannot
certify the requested 1e-7 motion tolerance through that generic bound. This
lower-bounds that certificate, not the actual motion error. Different
dictionaries, arithmetic, componentwise bounds and closures are not excluded.
The static preflight also shows why zero sampled tails and small tensor
initialization time are not population error certificates. This scoped
implementation obstruction is study-internal evidence; the two complete
scientific reviews below cover the positive frozen component and its stated
conditional stability proof, not every portfolio or feasibility argument.

Thus the persistent failure is in the current approximation/certification
implementation and the uncompleted general bridge. It is neither a refutation
of H2 nor a proved impossibility of the broader C-H3 objective. Full details
are in H3_portfolio_comparison.md and H3_residual_feasibility.md.

## Review, reproduction and promotion disposition

The independent [relevance follow-up](H3_relevance_v2.md) accepts the bounded
component for narrow assembly and standalone validation, while holding the
full C-H3 milestone. The complete frozen candidate, code, tests, canonical
dependency proofs and guides are identified by [the scientific manifest](H3_review_manifest_v1.json),
SHA256 `bc60684162353c63704644f4a543b2f644eb7a27ec6179e293a3bbbb71f241f9`.

The original [scientific review A](H3_review_a_v1.md) and
[scientific review B](H3_review_b_v1.md) each **PASS the bounded positive
claims, with no required scientific correction; full C-H3 is NOT MET**.
Both reviewers had fresh isolated contexts, were distinct from every
author/assembler and selector, and received neither internal verdicts nor
the other review. Each read all 8,119 frozen input lines, including the
complete proofs and dependencies, implementation, tests and guides. Both
independently reproduced the combined producer from frozen source in a fresh
standalone directory. The coordinator read both original reports completely,
checked their declared isolation/read scope and verified all original/copy
hashes and all 48 A and 36 B recorded output hashes. A's disclosed temporary
fixture location exception is retained in its report; the final tests used
its assigned scratch and no external research input was acquired.

The first distinct [integration review](H3_integration_v1.md) passed execution,
imports and error carry but required a documentation navigation correction:
the copied circle module named a proof file absent under that filename.
Its adverse report and packet are preserved. [Capsule manifest v2](H3_review_manifest_v2.json)
and [builder v2](H3_make_review_capsule_v2.py) correct the copied proof filename.
Every scientific proof, implementation, test, configuration and guide byte
remains identical to the paired scientific review inputs. Only the package
mapping and builder's manifest selection change. A fresh separate integration
review of this corrected scope, [integration v2](H3_integration_v2.md), **PASSes
with no required correction**. It reads all new material and the full guides,
states its precise older dependency scope and unread complement, verifies all
source/copy hashes, and passes all 16 tests plus independent static interface,
restart and cumulative-error attacks. Its harness uses 2.525909 CPU seconds,
2.499565 wall seconds and at most 20,992 KiB child RSS. The coordinator read
the original report completely and verified its exact evidence and capsule
mapping. No full canonical edition has been submitted or accepted.

[H3_review_disposition_v1.json](H3_review_disposition_v1.json) records the
scopes, original report hashes and coordinator correspondence checks.
[H3_review_evidence_sources_v1.json](H3_review_evidence_sources_v1.json) preserves
the unique handwritten reviewer scripts and preregistrations as exact UTF-8
source strings with their original paths and SHA256 hashes. The generated
execution logs and result arrays remain in the four assigned H3 review
directories; no unique review source is confined to those generated paths.

The canonical full-milestone promotion package is blocked by the named missing
requirements. The study reproduction capsule is not a canonical book/code
addition. No approval-ready full C-H3 package is offered. The original and
repaired producer records, complete proofs, code, tests and review inputs are
retained in the study; generated runs remain in its data namespace.

Reproduction from the repository root, with fresh paths and the stated cap:

```
python -B studies/observable_hierarchy/H3_shorttime_test.py
python -B studies/observable_hierarchy/H3_circle_kernel_test.py
python -B studies/observable_hierarchy/H3_reference_solver.py --output data/generated/observable_hierarchy/H3_FRESH
```

For standalone validation, build the corrected capsule from the repository
root and then follow its RUN.md:

```
python -B studies/observable_hierarchy/H3_make_review_capsule_v2.py --output data/generated/observable_hierarchy/H3_FRESH_CAPSULE
```

Both output names above must be fresh. All copied input bytes are checked
against the frozen manifest. Standalone numerical execution requires only
Python 3.10 or later and its standard library. The builder runs in the checkout;
the copied numerical modules and tests run without it or any study lookup.
Scoped commits use the shared Git writer lock; concurrent changes remain
outside this study's commits.
