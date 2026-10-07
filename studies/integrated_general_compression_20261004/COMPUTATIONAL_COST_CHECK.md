# Computational-cost extension: scoped checks

Date: 2026-10-06. Status: internally checked for the stated arithmetic
implementations and memory contract. This is not a promotion review,
floating-point analysis, performance benchmark or re-audit of every
prediction-error proof.

## Scope and current claim

The user requested initialization, training and inference costs in the
single integrated document, followed by inverse-interface and final
compression tables. The author added:

- Part II: supplied-order costs for dense, Legendre and Harmonic models.
  Warmup includes dense-reference creation; training discards warmup-only
  arrays. Both report total peak resident memory. A query reports only
  additional peak workspace at an inference-ready state.
- Explicit Harmonic initial-jet, Chebyshev, spherical-harmonic, spatial
  quadrature and temporal quadrature orders; source size/rank, activation
  backend, arithmetic model and alternative time-memory executions.
- Part III: derivations for factored jets, temporal-map compilation,
  separated harmonics, source selection, assembly, metric caches,
  matrix-free update-Gram action and effective-readout query caching.
- Inverse and common-accuracy tables, using only the existing inverse
  width/budget choices. Harmonic warmup retains the remaining setup
  orders; no epsilon-only efficient warmup claim is made.

The implementations use classical matrix arithmetic and the explicitly
specified scalar primitives. Numerical constants hide no structural,
activation-routine, stage-count or precision dependence. Gaussian
sampling and activation operations are separately qualified. The
quadrature-node generation count covers the elementary angular Riemann
rule in the source proof, not arbitrary quadrature-rule construction.
Cache refresh is not charged as free query work.

The prediction-error theorem, label/width assumptions and model
constructions were not strengthened or weakened by this cost addition.
The separate previously requested method renaming is included in the
same scoped commit; its earlier check is preserved in
[TERMINOLOGY_UPDATE_CHECK.md](TERMINOLOGY_UPDATE_CHECK.md).

## Version binding

All paths below are in this study.

| Input | SHA-256 |
|---|---|
| Final RESULT.md | c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278 |
| Final README.md | fc99baed4da861ba13194d820d1477c08dd328b4e25680aefa8d77cb3d3d64e7 |
| cost_algebra_check.py | d2cf4bdff31fb212c50c3dca30d1c2707f5e0b0594491eebb840f9d49b762128 |
| Earlier rename-only RESULT snapshot | 9c4bc51b9e78489cc9ce910024993994759fefd6652e4f2a16789e5640c32f2d |
| Original audited RESULT at predecessor commit | e24e2f519bd597159f1745ce46e9f9ad27c8772e9ef80807907b63557401c562 |

The predecessor commit is
7ee13decc7ff43d289ec64c0b2463906afbb3090.
The four original INTEGRATED_*_AUDIT reports remain byte-identical to
that commit and retain their own frozen-input qualifications. Neither
their hashes nor the rename-only report is presented as a review of
the new cost sections.

## Reviewers, allowed inputs and corrections

The root author assembled the derivations and tests. Scientific inputs
for this extension were the existing integrated construction and its
relevant definitions/proofs, not new research from other studies.

| Scoped check | Allowed scientific inputs | Outcome |
|---|---|---|
| harmonic_runtime_cost_audit | New headline, Part II and Part III cost sections; relevant current Harmonic definitions and continuation map | PASS at final RESULT hash |
| legendre_dense_cost_audit | New cost tables/proofs; current dense/Legendre definitions and inverse prescriptions | Scoped PASS; final hash confirmed |
| jet_initialization_cost | Continuation of the prior jet-cost derivation, current warmup/cost proof and algebra script | Verification PASS, with backend scratch qualification requested and applied |

These were scoped author-side checks. The jet-cost checker had
participated in the preceding derivation and is not described as an
independent attempt. The other scoped checkers first reconstructed their
assigned execution costs and then inspected the written sections.
No reviewer reconstructed every analytic dependency of the original
prediction-error theorem as part of this addition.

The Harmonic review required an explicit restriction of cheap
node/weight generation to the elementary angular Riemann rule. It also
requested charging node/basis evaluation during coefficient-block
replay. Both were added. The jet review requested that activation peak
workspace include derivative-generation scratch, not just persistent
series coefficients; that correction was added. Explicit rational
normalization recurrences were included to avoid an uncounted special
function oracle. The Harmonic reviewer reread and accepted all these
corrections at the final RESULT hash.

The dense/Legendre reviewer found no substantive issue in the supplied
warmup, streamed factor/RHS, prefix-sum, query, memory, oracle-call or
inverse-substitution statements. Its final hash confirmation explicitly
retains that scope and does not certify the intervening Harmonic edits.

## Executed deterministic algebra checks

Run from the repository root:

~~~bash
python studies/integrated_general_compression_20261004/cost_algebra_check.py
~~~

Environment: Python 3.10.12, NumPy 1.26.4; NumPy float64 arithmetic;
fixed random seed 20261006. The test writes no files. Success means every
maximum entrywise discrepancy divided by the larger of one and the
reference magnitude is at most 2e-11.

Observed result: exit zero, PASS, 104 checks. Largest normalized
discrepancy: 4.7197205501497826e-15.

The check families are:

1. Materialized dense jet action versus direct and cached factored
   convolutions, including transpose action.
2. Continued time-coordinate power recurrence versus polynomial
   convolution; compiled temporal projection versus explicit finite
   reconstruction/quadrature; preservation of paired linear images.
3. Selected-metric inverse, selected adjoint and isometry identities.
4. Ninety separated-harmonic normalization cases in dimensions 3, 5
   and 7, compared against a 64-point Gauss-Legendre polynomial-integral
   oracle. This is a finite algebra check, not a proposed production
   quadrature or quadrature error theorem.
5. Legendre running-prefix and streamed-factor actions versus direct
   sums/materialized matrices.
6. Harmonic matrix-free update-Gram action versus its explicitly
   constructed sample Gram, using unequal layer widths and nonidentity
   positive metrics; cached inference and training interpolation.

The tests verify finite execution identities against separately
expressed formulas. They neither benchmark the asymptotic complexity
nor prove stability, analytic approximation accuracy or a training-step
count.

## Mechanical preservation and structure checks

The author ran:

- Extraction of every original displayed and inline mathematical
  expression from the predecessor RESULT, stripping equation tags and
  applying only the public compact-to-Harm predictor-label mapping.
  All 480 original displays and 2,108 original inline expressions occur
  unchanged and in their original order in the extended document.
- Preservation of every original explicit fragment anchor, uniqueness
  of current anchors/equation tags, paired math delimiters, local-link
  resolution and rejection of ASCII control characters.
- Byte-preservation check of the four original audit reports against
  the predecessor commit.
- Scoped whitespace validation and the deterministic algebra script.

Final RESULT structure: 74 unique explicit anchors, 190 unique equation
tags, 503 paired display delimiters, 2,422 paired inline delimiters and
49 resolved local links. README has 9 resolved local links. All original
anchors remain available.

The expression-preservation check is a regression check, not a claim
that unchanged formulas alone certify surrounding prose. The scoped
reviewers separately checked the added cost arguments and qualifications.

No full Markdown/TeX render or numerical training experiment was run.
The required canonical-notation skill remained inaccessible with
permission denied, as recorded in the existing study; no compliance
with its unread contents is claimed. The accessible rigorous-math
workflow and the user's explicit presentation requirements were used.

## Remaining limits and write scope

These are upper bounds for explicit implementations, not global
time/memory optima. They do not quantify efficient accuracy-certified
jet or quadrature choices, finite-precision requirements, conditioning
of exact rank/selection operations, numerical-integration accuracy or
the number of training steps. Fixed-problem inverse exponents do not
become simultaneous growing-data results.

The root is the only Git writer for this update. Commit scope is this
study's RESULT, README, terminology record, cost check record and test
script only. The maintained book, paper, original proof audits,
other studies and concurrent maintenance edits are outside scope.
