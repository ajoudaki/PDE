# Independent complete scientific review R1-B

**Verdict: PASS for the frozen candidate and its stated scope.** I found no
blocking scientific or implementation defect. This is a complete review of
the assembled theorem, its five proof units, the executable realization and
the necessary maintained dependencies. It is not an acceptance of a wider
data family, growing dimensions, a numerical error rate, or a simultaneous
limit not asserted by the candidate. It is not promotion approval.

## Independence, frozen inputs and coverage

The assignment was `REVIEW_ASSIGNMENT_R1.md`. I used the original
`REVIEW_INPUTS_R1.json` and the subsequently supplied
`REVIEW_DEPENDENCY_SUPPLEMENT_R1.json`. The latter supplies three transitive
package imports; it changes no candidate scientific input. All 30 original
hashes matched before substantive review. All 33 hashes matched after the
supplement was supplied, before independent checks, and at final review
completion. The final verification record is
`data/generated/cx1_many_point_closure_20260919/review_r1_b/input_hashes_after_review.json`.
The input files and Git index were not modified.

I read neither study history nor its README, correction records, prior
reviews, other reviewers' findings, other studies, chats or Git history.
The review used the required `solve-math-rigorously` and
`investigate-conjectures` skills, including the applicable research-contract
and adversarial-audit instructions. No external scientific source was needed:
the required theorem dependencies are contained in the frozen inputs.

Complete candidate coverage:

| Input | Coverage |
| --- | --- |
| `THEOREM.md` | Entire statement, all quantifiers and all five conclusions. |
| `REFERENCE_PROOF.md` | Entire file, including local construction, signed symmetry, feature/physical clocks, strong endpoint, initial reused-action algebra, activity remainder, nonaffinity, finite GF and the standalone stronger GD-step condition. |
| `PERTURBATION_PROOF.md` | Entire file, including all displayed constants, both source bootstraps, the explicit radius, strong completion, arbitrary-competitor uniqueness, empirical tails and the finite-capture interface. |
| `FINITE_CAPTURE_PROOF.md` | Entire file, including the actual random readout, proxy construction, width-independent bounds, limit order, actual raw GD and all observation transfers. |
| `CX1_CLOSURE_PROOF.md` | Entire file, including complete-hierarchy sufficiency, dictionary density/enrichment, all fixed-order equations, convergence, numerical limit order, arithmetic/workspace/bit costs and conditional interface. |
| `ASSEMBLY_PROOF.md` | Entire file, including constants for risk, paired motion, variance/nonaffinity, final radius and nonorthogonal examples. |
| `cx1_closure.py`, `test_cx1_closure.py` | Entire files. Checked producer/consumer interfaces and all seven semantic tests by source inspection. |
| `check_reference_constants.py`, `validate_trajectories.py`, `VALIDATION_PLAN.md`, `VALIDATION.md` | Entire files. The operational driver was inspected, not rerun. |

Complete maintained mathematical units read and audited were:

- `docs/special_data_limits.md`, III.F.1–III.F.11: fixed Gaussian programs,
  singular sources, same-matrix responses, common carriers, actual adjoints,
  operator/HS completion and scalar calculus.
- `docs/global_nonlinear.md`, A.1–A.4; complete B.1; complete C.3 including
  the weighted correction; C.4.1; C.4.5.1 and C.4.5.2 including the full exact
  rational certificate; C.4.7.1–C.4.7.5; C.4.7.8; C.4.7.9; and complete
  C.4.7.10 parts A–D.
- The complete notation contract and `docs/observable_p1.md`; the relevant
  model, observable-closure, numerical, precision, restart and general-d
  contracts in `code/README.md`; and the computational-milestone contract in
  `docs/README.md`.

Complete maintained executable modules read were `observable_arithmetic.py`,
`observable_fixed.py`, `observable_compiler.py`, `observable_initialization.py`,
`observable_words.py`, `observable_solver.py`, and `observable_closure.py`.
The supplemental `pde/__init__.py`, `finite_network.py` and
`gaussian_moments.py` were also read completely to close the eager-import
lineage. The frozen `observable_laws.py`, `observable_p1_initialization.py`,
`observable_torch_circle.py` and `observable_torch_p1.py` are not imported by
this candidate or its tested runtime and do not supply a theorem step; their
hashes were verified, but I make no separate review claim about those unused
implementations. General-d conclusions here are proved by the candidate;
they are not inferred from the narrower maintained p=1 or two-dimensional
theorems.

Allowed generated evidence examined was limited to
`reference_constants_01/record.json`,
`closure/deterministic_v4/results.json`, and `operational_02/record.json`
with its declared output/source hashes. No earlier validation run was used
to support a scientific inference. All ten declared operational output hashes
and eight declared operational source hashes matched.

## Exact accepted hypotheses and conclusion

The result fixes separately `1 <= m <= d`, arbitrary binary labels, uniform
training weights and a separately fixed unit-direction configuration in the
displayed positive neighborhood of distinct axes. The initialized stored
variances are `(1,1/n,1/n^2)`, the prediction is `c^T h2/n`, the first input
is normalized by `sqrt(d)`, the loss is the unhalved mean square and the
physical mobilities are `(n,1,n)`. The population first row is the entire
`R^d` row, and the two action orientations belong to the same initialized
Gaussian matrix. Only the learned increment is HS.

Under precisely these conditions, the arguments support canonical strong
flow and reached restart through `T=5m`, the stated strict loss and activity
and nonaffinity margins, actual finite-GF capture, and actual simultaneous
raw-GD capture whenever `eta_n -> 0`. The finite random readout is retained.
They also support the complete observable hierarchy, autonomous finite
population closures and the stated iterated numerical/order convergence,
including whole-sphere predictions and fixed typed joint observations in W2.

## Claim-by-claim adversarial audit

### 1. Reference construction, clocks and learning

`REFERENCE_PROOF.md` §§2–5 preserves all inactive first-row coordinates and
uses an actual action/adjoint pair. The clock map has derivative
`j_X=sech^2(j)`; local Lipschitz estimates apply on the stated clock/raw ball,
with bounded readout. The construction does not replace a random dense
matrix by an independent reverse action. The scalar clock representation
also identifies raw competitors, rather than assuming a coordinate chart
for them without proof.

The signed permutation in §3 uses the label factors
`epsilon_a=y_a y_pi(a)`. This establishes the one-scalar prediction symmetry
for mixed labels as well as all-equal labels. The argument includes `m=1`;
it does not require a second distinct training sample. Factors `1/m` remain
in both the reference feature field and its first derivative. In particular,
`b_s=||h||^2+||J* c||^2`, the lower bound is `v/m`, and the physical clock
is `s_t=2(1-b)`. These factors produce `T=5m` and reference risk below
`exp(-4)<1/16`; they do not silently use a sum or half-mean loss.

The endpoint argument bounds total raw path length by the product of the
feature-time and prediction increments. Together with the readout and action
bounds this gives the strong endpoint and whole-sphere passive prediction
control. This is sufficient for the later finite-horizon use and is not an
unstated uniform-in-width endpoint limit.

### 2. Both-layer motion and visited-law nonaffinity

In §6, the first reused reverse call has the nonzero conditional response
in (6.4). The next forward call retains both its old-forward projection and
the reverse response in (6.5). The covariance `C` is positive definite:
full support and the nonconstant coordinate gates force every coefficient
of a vanishing linear combination to be zero. This works for `m=1`.
The independent fresh Gaussian component therefore gives the displayed
lower bounds for both leading activation coefficients. No independence of
the different fresh residuals is needed or asserted.

I checked that the lower bound
`C_aa=[d0+(m-1)v r0]/m^2 >= c_*/m` uses `d0>0` in the one-anchor case.
The upper-layer lower bound concerns actual activation motion after its
outside gate, not only motion of preactivation. The explicit remainder in
§7, with its cutoff-dependent coefficient and subsequent choice of cutoff,
produces the stated positive `s0`, `t_act` and `a_m` before any limit.
The physical-clock lower bound used at `t_act=s0/2` has the correct direction.

The best-affine error is handled as
`Var(tanh Z)-Cov(Z,tanh Z)^2/Var(Z)` with a positive variance floor.
Gaussian full support makes the reference affine error strictly positive;
the L2 perturbation estimates in the reference and assembly units preserve
both variance and this error. The asserted uniform lower bound at the
activity time follows for each anchor and both layers. A claim about all
later times is not being imported.

### 3. Noncircular source cap and explicit supported radius

This is the most delicate interface. The dependence order in
`PERTURBATION_PROOF.md` §§4–7 is sound:

1. The physical-clock reference is constructed independently, with the
   fixed-m anchor weights and same-root Lipschitz estimates (P11)–(P13).
   A fresh independent pulse and finite-array Gaussian integration by parts
   identify its source responses. Frozen named-source derivatives are used,
   including singular covariance cases. The impulse mass is `h/m`.
2. The clock cap (P14) gives actual reference-flow Gaussian-plus-bounded
   tails by strong convergence and the cross-program source isometry. This
   precedes any assumption about a raw-reference source cap.
3. Raw Euler can consequently be compared to that reference without a raw
   cap, obtaining the unconditional state discrepancy `eta_h -> 0`.
4. A temporary raw cap gives moment and pulse estimates. The transformed
   defect (P19) retains its cancellation, and differentiating that integral
   gives (P20)–(P23). At the injection step the quotient by `h/m` leaves
   a factor proportional to `h`, not its inverse. The subsequent defect
   sum is `O(hmax)`. The transformed pulse propagation (P24) has bounded
   deterministic coefficients. Equations (P25)–(P26) compare it to the
   already capped clock system and close the raw-reference first-failure
   argument. They do not posit bounded raw pulse maxima.
5. Only then is the perturbed system compared to the raw reference.
   Equations (P31)–(P36) preserve the time/atom masses and keep the current
   unknown response row off the right side. Gaussian exponential estimates
   control a time/atom sum, not a pointwise maximum of a growing transcript.
   Current passive probes do not inject additional training mass.

The cutoff estimate (P38) depends only on the raw reference tails and the
unconditional perturbed raw ball. Thus its use to close the perturbed cap
does not assume the tails it is intended to establish. I checked the
explicit (P39) choice: with `A=1+Gamma+H+Z`, `S>=1`, `b=4SA`, the negative
quadratic tail exponent dominates `Gamma(1+b)+Z+log(4 Gamma H)`.
The input term is bounded by `exp(-Z-4) X exp(-X)` with
`X=Gamma(1+b)`. The chosen radius makes both terms small enough for the
strict first-failure margin in (P36). The radius is positive and independent
of width, mesh, closure order and numerical precision. It is not claimed to
be practically resolvable.

The mesh threshold needed for the raw-reference comparison may remain
qualitative. That does not make the displayed geometric radius implicit:
the latter depends on the explicit cap value `B_cl+1`, not on an unevaluated
inverse continuity modulus or a guessed mesh threshold.

### 4. Strong completion, uniqueness and passive observations

Proximity to one reference alone would not construct a solution. The proof
instead compares any two refined raw meshes for the same or nearby law in
(P42), using their now-uniform query tails. Fixed cutoff, mesh refinement,
then removal of cutoff proves a genuine strong Cauchy property. The limit
equation follows by bounded multipliers and strong convergence of the
complete raw fields; this gives a strong solution and its energy identity.
The source isometry and strong backward-field convergence transfer the
Gaussian-plus-bounded decomposition to the reached flow.

Uniqueness at a reached restart uses a one-reference cutoff inequality
against an arbitrary strong raw competitor. It does not require the
competitor to satisfy the source bootstrap. Compactness of the sphere,
the finite separately fixed row dimension and the raw speed bounds justify
the passive-input and time nets. No compactness of an infinite-dimensional
raw ball, or uniform theorem for `d -> infinity`, is used.

### 5. Actual finite GF and actual raw GD

`FINITE_CAPTURE_PROOF.md` §§2–4 supplies a distinct stronger bridge than the
standalone reference chart argument. The actual readout has a
width-independent infinity bound from (F2). The learned middle increment
and complete first row have width-independent Frobenius/RMS speed bounds.
Initial operator, row-RMS and readout-infinity events have probability tending
to one; no bound on a growing collection of source derivatives is required.

For each fixed proof mesh, the proxy is one finite Gaussian program. Its
parameters retain the actual initial first rows and matrix, and its readout
adds the actual finite random initial readout to the oracle increment.
Thus the raw comparison starts at zero error. Recomputed proxy fields and
velocities have vanishing RMS defects on this fixed program; finite-rank
middle increments are compared using their double-Gram identity (F6).

The one-reference estimate (F8) truncates only the proxy backward query.
Actual and proxy readouts already have common infinity bounds. In (F10),
the discrepancy between interpolated raw states and their left endpoints
is bounded by a constant times `h+eta_n`, with no factor `sqrt(n)`.
The probability argument chooses the cutoff first, then a fixed proxy
mesh, then takes `n -> infinity` with `eta_n -> 0`. All Gaussian-program
limits remain fixed-program limits. This establishes the advertised
actual-GD condition without applying such a theorem to `1/eta_n` calls.
The stronger sufficient condition in the standalone reference proof is
therefore neither a contradiction nor an unacknowledged premise of the
assembled statement.

Fixed typed joint observation graphs pass through the same coupled proxy
and retain both action directions. The full-sphere prediction estimate has
a uniform finite raw Lipschitz bound, and the finite net argument applies
to every fixed d. W2 convergence controls the paired second moments and
the variance/covariance quantities needed to transfer smaller strict
motion/nonaffinity margins.

### 6. Hierarchy sufficiency and genuine density

`CX1_CLOSURE_PROOF.md` §2 uses joint laws of a typed countable language,
not an unsupported moment-determinacy claim. Rational trigonometric tests
determine finite coordinate laws, their cylinder functions are L2 dense,
and the actual action extends with its true adjoint to the reducing
observable subspaces. The full initial row is retained. Equality of complete
reached observable states induces the requisite carrier isometry and
intertwining; restart uniqueness then gives predictive sufficiency.

The finite dictionary in §3 contains both a polynomial core and every valid
bounded word in an increasing exhaustive natural-code prefix. The code
dependencies strictly decrease and the scalar code exhausts the rationals.
Duplicates are retained consistently with ridge normalization. The density
proof uses the tail; it does not mistakenly treat the low-dimensional
polynomial core as the entire generated carrier. The strict polynomial
enrichment and the nonzero added action coupling are separately justified
by full-support laws and the odd-polynomial argument.

With inverse-lower-Cholesky normalization,
`D=L2^{-1} C L1^{-T}` has the correct right transpose. The filters are
contractions, and the fixed-word ridge estimate implies strong convergence
to the identity on the observable subspaces. Strong convergence is used
only on compact target curves or finite-rank approximations to HS curves;
operator-norm convergence of the initialized action is not claimed.

### 7. Closed finite equations, convergence and numerical realization

The exact finite population state consists of the joint marks and current
fields together with the full feature-indexed matrix. Its row and readout
fields are not forced into a feature expansion. The moving matrix is
unrestricted and its actual transpose is used. The weighted L2/Frobenius
gradient calculation gives the energy identity and global fixed-order
continuation. The number of retained fields/entries does not grow with
elapsed steps; the exact population law is nevertheless distinct from its
finite quadrature realization.

The vanishing consistency source in (16) is produced by strong filter
convergence on compact target sets. The lower-gate estimate (17) truncates
only the target query. Osgood propagation of the exponential tail controls
the full supplied horizon; the proof explicitly avoids using a fixed-cutoff
Gronwall bound beyond what its tail decay permits. This closes the
fixed-order-to-target approximation without assuming the omitted source
is already small. The induction over typed observation graphs preserves
same-population initialized/current pairs and both action orientations.

The numerical producer compiles the complete joint source program at every
admitted order. It does not continue to use the core-only contraction
formula when the tail adds an action. The positive source regularizer and
positive feature ridge have separate roles. Singular source laws are reached
by removing the former in the specified order; no positive mode is discarded.
Population replay holds the coefficient rule fixed and preserves complete
joint marks. The deterministic Gaussian rule, finite arithmetic refinement,
finite-dimensional time scheme and optional coordinate representation are
covered by their corresponding convergence arguments. Their order is
precision, time mesh, optional input representation, population integration,
coefficient integration, source regularizer, then dictionary order.

The implementation follows those equations. Its dimension adapter supplies
all Gaussian coordinates, its iterative exponent enumeration avoids a Python
recursion dimension ceiling, and inherited numerical evolution dispatches to
the candidate's dimension-general state and data methods. Save/load preserves
hexadecimal float, Decimal or fixed-point working values and all frozen
marks, without replaying an initializer. Resource limits reject an
allocation; they do not silently replace the mathematical hierarchy.
The stated scalar work, retained-state/workspace and fixed-configuration bit
costs account for the generic source program, full Grams, dense coefficients,
quadrature and arithmetic. They are not cost-to-accuracy bounds.

### 8. Final assembly and nonorthogonal scope

`ASSEMBLY_PROOF.md` uses one common raw ball for target and reference. The
hidden-field comparison includes the change of evaluation input and of the
initial paired field. Its choice of perturbation tolerance leaves enough
room for the paired RMS lower bound before squaring. The loss estimate uses
the residual RMS triangle inequality: reference residual below `1/4` plus
prediction error below `1/8` gives strict loss below `9/64`.

The variance and best-affine-error estimates have the needed reference
variance floor; the final radius is the minimum of an explicit cap radius
and an explicit margin-preserving radius. It is fixed before all limits.
For `m>=2`, tilting the first axis toward the second gives genuinely
nonorthogonal configurations at arbitrarily small displacement. The
`m=d=1` two-point sphere exception is expressly stated. This supports the
literal family in the theorem without silently requiring a nonempty angular
neighborhood in that edge case.

## Independent checks and evidence limits

I reran the exact rational initialization certificate and independently
checked a supplied, untrained numerical state with dimension five, unequal
population sizes five and six, a full 3-by-4 action matrix, nonuniform
population/data weights including zero-weight population rows, nonorthogonal
inputs and mixed labels. This was an algebraic check, with no trajectory
experiment and no use of an initialized or fitted candidate state.

The checks completed in 3.253 seconds under a 60-second alarm and a
512-MiB address-space cap. Their record is
`data/generated/cx1_many_point_closure_20260919/review_r1_b/independent_checks.json`.

The calculation originally ran via standard input. Its numerical inputs and
checks are retained in `review_r1_b_independent_checks.py` in the flat study
folder for reproduction. The original generated scratch copy is preserved;
the two files are byte-identical, with SHA-256
`4383977cb85bfd8123af1dd5c5d19029d0021ce4211c5eae18581a70fc1060a2`.
From the checkout root, a fresh result can be produced with:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
PYTHONPATH=code:studies/cx1_many_point_closure_20260919 python -B \
studies/cx1_many_point_closure_20260919/review_r1_b_independent_checks.py \
--output data/generated/cx1_many_point_closure_20260919/review_r1_b/reproduction.json
```

| Independent check | Result |
| --- | --- |
| Exact rational certificate | All assertions passed. Reported bounds: `0.392108947877`, `0.396376711612`, `0.233120735618`, `0.339792209687`, `0.631761866359`. |
| Every moving-coordinate gradient, 43 coordinates | Maximum absolute central-difference discrepancy `1.62e-10`, below the pre-execution `2e-9` criterion. |
| Weighted energy directional identity | Absolute discrepancy `4.61e-11`, below `2e-9`. |
| Actual weighted adjunction | Absolute discrepancy `5.21e-18`, below `2e-14`. |
| Original and supplemental frozen hashes | All 33 matched. |
| Declared operational artifacts and sources | All ten output hashes and eight source hashes matched. |

The final-source seven-test record matches the frozen module and test hashes
and reports seven passes, no errors and no failures. I inspected all seven
tests and did not repeat that whole suite. The five operational runs are
consistent with their declared configurations and storage/restart checks.
Their large integration-refinement prediction difference, about `0.061`,
is explicitly acknowledged in the validation report. The small training
losses and time-step difference are not used as proof of prediction accuracy.
The nonorthogonal operational run is expressly outside any certified
membership claim for the very small proved radius.

## Findings, unresolved issues and acceptance boundary

**Critical/major findings: none. Minor changes required for this theorem:
none.** I found no unresolved scientific gap that prevents acceptance of
the frozen statement. In particular, no theorem weakening to
`eta_n sqrt(n) -> 0`, no restriction to two dimensions, no restriction to
one label pattern, and no replacement of the full dictionary by its core
is needed.

The following remain limits of the result, rather than defects:

- The neighborhood can be extremely small and has no useful numerical
  evaluation here. The result does not cover arbitrary correlations or a
  growing-dimensional regime.
- All convergence statements have the stated fixed horizon, fixed data,
  finite observation scope and iterated resolutions. No order rate,
  arbitrary simultaneous diagonal or tolerance selector is provided.
- Operational runs establish that selected finite configurations run and
  restart; they do not certify their distance to the population solution.
- This is a mathematical and source-code review supplemented by bounded
  deterministic checks, not a machine-checked formal proof or an exhaustive
  numerical assessment at all orders/precisions. No training experiment,
  literature novelty assessment or approval to promote established material
  forms part of the verdict.

Within those boundaries, the assembly closes the reference, perturbed-target,
finite-network and numerical-closure interfaces, and the candidate is ready
for the separately required promotion process.
