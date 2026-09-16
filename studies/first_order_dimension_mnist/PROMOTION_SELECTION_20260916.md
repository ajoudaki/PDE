# Independent relevance and placement selection, 2026-09-16

Selector: Codex scoped agent `/root/select_a`, distinct from this study's
authors and from the proposed assembler. This is Part 2 step 1 selection,
not a correctness certification, paired adversarial review, integration review,
or promotion approval. No scientific candidate or established file was edited.

## Decision

**Accept a narrowed general-dimension p=1 theory/implementation component for
Package A assembly, including its GPU solver as a core deliverable. Accept
reusable comparison methods for a narrow MNIST contribution to Package B.
Hold numerical MNIST/PCA conclusions until a standalone maintained producer
and independent fresh reproduction exist.** Preserve the original study.

The useful addition is an explicit, inexpensive specialization of established
observable equations: general-dimension p=1 Gaussian coefficients, their
block normalization, a precisely scoped antithetic representation, and a
reusable GPU implementation of the same finite equations. It is not another
C-H1–4 theorem, a second presentation of the circle hierarchy, or a general-d
trained-network convergence result. Fixed p=1 retains truncation error.

The user clarified that the circle varying-p GPU solver and this general-d p=1
solver are complementary core components of A. This selector assesses only
the latter. No other study or its selection was consulted. A common supplied-
state contraction backend is scientifically justified by the common H3.N2
equations, arbitrary feature dimensions and the shared actual transpose; it
is an integration choice requiring its own complete checks. The two
initializers, admissible observations and convergence scopes must remain
distinguishable. Torch may be an optional installation dependency without
making the requested GPU implementation an optional campaign artifact.

## Selection by component

| Component | Distinct value and duplication | Decision and smallest destination | Assumptions, cost and conditions |
|---|---|---|---|
| General-d p=1 initialized joint law, Grams, raw action contraction and inverse-Cholesky bands | Established C.4.7.10.B already supplies the d=2 construction, source-response rule and Cholesky orientation. New value is factorization into repeated scalar blocks for every positive d, eliminating d-dimensional quadrature and dense empirical-Gram normalization. | **Accept, narrow.** Add a short self-contained general-d p=1 subsection immediately after C.4.7.10.B's initialization construction; reference existing equations rather than repeat the hierarchy/convergence proofs. A separate NumPy-only `code/pde/observable_p1_initialization.py` is the smallest implementation addition. | Gaussian coordinate probes, tanh, fixed p=1 ridge 1/4096; lower `(G,R)` joint dependence and independent population carriers; retain the reverse-response term and right Cholesky transpose. Exact coefficient target is distinct from finite working quadrature. No trained-network identification theorem. |
| Exact antithetic folding | Established text notes polynomial parity but does not give this general-d finite-rule representation and its invariant-state conditions. | **Accept, narrow.** One proposition adjoining the initializer subsection and explicit representation metadata in the initializer/backend. | Even nominal P; P/2 independent base draws per population plus simultaneous negative partners; odd moving w,c, odd nonconstant features, zero constant M row/column. Arbitrary finite input rows/labels are allowed; data symmetry is unnecessary. Cannot fold arbitrary supplied states or claim equivalence to P iid draws. |
| General-d GPU prediction, physical RHS and Heun | Existing `observable_solver` has the equations, own-state restart and a NumPy circle implementation. New value is arbitrary d, arbitrary supplied feature dimensions, device-resident blocked contractions and bounded workspace. | **Accept for author cleanup.** A compact `code/pde/observable_torch.py` with a p=1 construction wrapper; deterministic CPU and CUDA checks in `code/tests/`. Do not copy campaign dispatch into the library. | Bias-free two-hidden tanh; U=x/sqrt(d); unhalved weighted squared loss; complete dense M and its actual transpose; float32/float64 and explicit arithmetic policy. This implements the finite approximation, not exact GF integration. No universal speed or accuracy guarantee. |
| Actual-network GPU comparator | Finite network formulas and Gaussian initialization already exist in `finite_network`. GPU full-batch comparison is distinct and necessary for a reproducible benchmark. | **Accept, narrow.** A small optional Torch two-hidden-tanh reference module, or a clearly separated finite-network adapter in the GPU package; retain NumPy `finite_network` as independent oracle. | Stored variances `(1,1/n,1/n²)`, output cᵀh2/n, mobilities `(n,1,n)`, random finite readout retained, complete middle n-by-n matrix, simultaneous Heun stages. It is a numerical GF comparator, not literal raw GD. |
| Observations, storage and restart | Definitions largely duplicate H3/H40. General-d counts, antithetic semantics, cached contractions and GPU resource reporting need an explicit extension. | **Merge into the new API contract and a short book/API subsection.** | Save complete current/frozen arrays, population weights, finite data, arithmetic/reduction settings and representation metadata. Folded raw pair arrays require negative partners to denote the full signed joint law. Finite panels give no whole-domain error certificate. |
| Prediction-fidelity comparison methods | Equal-time comparisons, all individual seed pairs, within-class diagnostics and train-loss-only matching are useful reusable methods. Existing mathematical matched-loss C.5 result is a different question and should not be repeated. | **Accept, narrow, methods only.** One small NumPy analysis module plus an explicit-input producer/analyzer recipe, normally documented in `code/README.md`. Optional empirical book paragraph only after reproduction. | Same image IDs, declared reference, no calibration, no selection by output agreement. Distinguish equal time, separately selected checkpoints, fixed-reference train-loss matching and common-loss matching of all systems. Seed ranges are descriptive. |
| MNIST three-seed prediction fidelity and centered PCA98 comparison | Useful finite proof of operation on high-dimensional correlated data; distinctly broader computation than the supported circle laws. Existing internal checks do not replace promotion reproduction. | **Hold for a named gate.** If included, select one compact original-versus-PCA n=P=4096 example and its four comparisons; avoid repeating the whole 2048/4096 campaign chronology. | Must regenerate data, PCA, full selected trajectories and analysis from maintained source in a fresh standalone edition, with numerical controls and all declared seeds. No archive-only reproduction. If unavailable within authorized bounds, exclude numerical conclusions while continuing A and methods. |
| Historical timing factors and broad practical-superiority claims | Recorded timings are implementation/hardware/workload observations. They do not give matched-fidelity cost, cost-to-accuracy or architectural superiority. | **Defer the hardware-specific tables; decline broader inferences.** A bounded benchmark recipe is useful without fixed headline ratios. | Fresh synchronized GPU timing, matched physical horizon, full initialization/stage/data/checkpoint accounting, same-GPU comparisons and variability disclosure. No comparison of unequal horizons presented as an algorithmic speedup. |

## Scientific scope that must survive assembly

The exact initializer proof should include all of `INITIALIZATION_THEORY.md`'s
coefficient derivation, excluding campaign check history. In particular,
`R_i=sqrt(tau) Z_i+alpha tanh(G_i)` retains reuse, and the raw k-band
`alpha beta+tau gamma` includes the reverse-to-forward response. Independence
and parity yield the complete population Gram blocks; they do not justify
zeroing empirical off-diagonal entries of a finite sampled Gram. The positive
ridge and Cauchy–Schwarz give the strictly positive Cholesky denominator.
The initially repeated bands of D impose no sparsity or rank constraint on M.

The existing finite source proof in `global_nonlinear.md` Section 3 and H3.1
is the required established dependency. Assemble the general-d specialization
with its hypotheses explicitly checked. Do not infer a higher-order general-d
hierarchy, coordinate-rotation invariance of fixed p=1, a long-time Gaussian
population construction, or agreement with actual trained networks from it.

The scalar integration currently uses a normalized truncated Gaussian rule
on [-10,10] with 128/256 Gauss–Legendre nodes. Refining nodes at fixed cutoff
approaches that truncated law. The omitted Gaussian mass is not a certified
error bound for the composed coefficients. Retain numerical approximation
metadata and the absence of a tolerance selector; no new quadrature theorem
is needed merely to promote the exact identities and this disclosed method.
The general-d initializer differs at finite resolution from the established
Halton empirical-Gram initializer even at d=2. Oracle tests should compare
the same coefficient target or explicitly report this difference.

Finite network and closure initializations are different finite objects: the
network stores its independent Gaussian readout and the closure starts at zero,
the limiting small-readout value. Equal seed numbers do not couple them.
P is population integration count, n neural width, d input dimension and p
closure order. Use these symbols consistently in new text; distinguish old
equations' order N and precision p through an explicit local notation mapping.

## Smallest reusable API and cleanup obligations

The existing `ClosureEngine` is a good source, but not a finished maintained
boundary. Retain a constructor from full joint marks and D, initialization of
w,c,M, preparation of U and weighted data, prediction, RHS, simultaneous Heun,
paired observations/Grams and own-state serialization. Keep kernel association
choices explicit and both orientations tied to the same matrix. Freeze marks
by contract and prevent stale caches after any supported mutation.

Before freezing a candidate:

1. Remove repository-relative `studies/` and `data/generated/` assumptions,
   sibling-script imports, historical pilot-gate reads and automatic copying
   of every study file. Public calls should use explicit input/output paths,
   own their declared arrays and preserve the existing NumPy-only import path.
2. Supply validation consistent with the claimed public contract. The current
   network constructor/RHS has almost no domain validation; closure hot paths
   trust already-prepared tensors. Define prepared-data immutability and finite
   boundary checks. Test zero/nonunit/duplicate inputs, invalid shapes/steps,
   probability semantics, saturated arithmetic, unequal populations and dense
   nontrivial supplied states. Do not promise the NumPy reference's specialized
   extreme-range derivative/scaling behavior when the Torch implementation uses
   ordinary `1-tanh²` and matrix products.
3. Persist nominal/stored P, antithetic/folded status and inactive constants as
   required restart metadata when those interpretations are claimed. Current
   `save_restart` keeps them only in optional caller metadata. Dynamics can
   restart from the arrays without knowing P; scientific interpretation cannot.
4. Return population/input weights with pair observations. For folded states,
   either return an explicitly typed folded law with deterministic unfolding
   or return both signs with half base weights. Current positive-half pair
   arrays support even Gram/RMS quantities but alone do not describe the full
   signed empirical joint law. Never reinterpret those arrays as the latter.
5. Keep numerical equivalence, own-state restart and measured performance
   claims separate. Identical-device/reduction restart is the appropriate
   exact-working-state claim; cross-platform bitwise continuation is not implied.
6. Extract tests from `ENGINE_CHECK.py`: NumPy supplied-state oracle, independent
   autograd physical metric and energy identity, nontrivial folding, blocking/
   association equivalence and resumed continuation. Keep the full finite-network
   NumPy oracle and producer initialization tests. A CPU pass alone does not
   validate the requested CUDA backend; perform bounded CUDA checks too.

The existing analysis functions also need a compact explicit-input boundary.
For example `error_metrics` divides by an arbitrary floor at zero reference
RMS and guards correlation using reference RMS rather than reference standard
deviation; a nonzero constant reference can consequently produce NaN. Define
zero-reference relative error and constant/empty-class correlation explicitly,
and reject incompatible shapes, IDs or nonfinite data. Loss matching must
retain attainable-range checks, earliest-tie convention, actual loss mismatch
and bracket sensitivity; do not extrapolate missing targets.

## Complete cost contract

Write K1,K2 for retained feature counts and P1,P2 for stored population rows.
The backend supports these independently of d. Count moving state, frozen
marks, cached bases, stages, data, observations and output separately.
For equal unfolded populations, K1=2d+1 and K2=d+1. Moving state has
`P(d+1)+(d+1)(2d+1)` scalars; current engine/state with its two caches has
`P(8d+7)+2(d+1)(2d+1)` scalars. For folded nominal P, put B=P/2 independent
base rows: moving state has `B(d+1)+2d²` scalars, and the cached engine/state
has `8Bd+3B+4d²`. These sums count tensor entries, not deduplicated allocator
storage, and exclude data, stages, observations and checkpoints.

The comparison network has `nd+n²+n` moving scalars; this engine also retains
an equally sized initial state for paired observations. Data add O(md), Heun
keeps a bounded number of state copies, and k-input panel Grams/pairs can add
O(Pk+k²) storage. Fixed-resolution state does not grow with elapsed steps.
Prediction archives emitted by campaign code do grow with saved observations
and are not needed by the autonomous state.

Coefficient construction costs O(q²) integration work/storage after scalar
rule generation; the present dense Gauss–Legendre node routine can cost O(q³).
Mark generation is O(Pd); dense D materialization costs O(d²). Direct RHS
work is O(m(Pd+d²)), with alternative O(Pd²) precontractions whose formation
and cached workspace must be included. Multiply by the actual Heun step
count for a physical horizon. Thus P=n removes the n² state term only at
fixed d; it provides no uniform joint d,n advantage or cost-to-accuracy bound.

## MNIST/PCA methods and empirical gate

The preferred maintained example is one fixed digit pair (3 versus 5), fixed
split seed and three scientific initialization seeds, original U and centered
training-only PCA98, p=1 and n=P=4096. Keep four separate comparisons:
original closure/original network, PCA closure/PCA network, PCA closure/
original network and PCA network/original network. Their references must
use identical image IDs. Report individual closures and all seed pairs, not
only ensemble agreement; overall correlation alone is misleading with two
separated labels. Within-class metrics and worst errors belong alongside RMS.

Centered PCA scores are `(U-mean_train) V^T`, consumed directly as the new
U=x_new/sqrt(d_new); no extra dimension multiplier or row renormalization is
allowed. The reported 98% concerns centered variance. Centering also changes
scale and origin in a bias-free nonlinear model; the comparison does not
isolate discarded variance or imply preservation of original predictions.

For a retained empirical paragraph, maintain acquisition with checksum checks,
raw IDX parsing, deterministic split/normalization, train-only PCA transform,
producer, stopping/observation configuration, full bounded numerical controls,
checkpoint replay and independent analysis. All recipe dependencies must be
obtainable without this study or archived trained outputs. The current
`DATA.py`, `RUN.py`, `BATCH.py`, `PILOT_GATE.py` and analyzers fail that standalone
condition through fixed study paths and retained-run dependencies; they are
source material for cleanup, not a ready maintained recipe.

The study reports historical complete 2048 same-configuration reproductions;
its 4096 and PCA full runs have half-step controls and saved-weight replay,
with same-step bitwise repetition only on the T100 timing prefixes. These are
different checks. This selection does not independently verify all those
historical records. Fresh promotion reproduction must execute the selected
claim's producer and analysis; redrawing retained arrays is insufficient.

Full fixed-T100 performance ratios must stay separate from T600 or matched-loss
fidelity. Comparing all systems at one attainable training loss is useful,
but does not establish equality of learned maps, a pure clock change,
time-to-matched-fidelity savings, or an explanation of generalization.

Historical full4096 and PCA continuations consumed approximately 45.52 and
35.74 summed GPU-process minutes respectively, including their declared controls
and, for PCA, timing wave. These are study-reported costs, not estimates or
authorization for a new campaign. Narrowing the selected example can avoid
repeating 2048 history, toy runs and redundant timing tables. If complete
selected-claim reproduction cannot fit the current authorized budget, defer
the numerical paragraph; do not lower the gate or run a new research search.

The supervisor reports that the documented interpreter
`/home/amir/miniconda3/bin/python` supports Torch 2.9.0+cu130 and that an
approved out-of-sandbox check sees two RTX3090 GPUs. Thus the named remaining
gate is candidate cleanup/review/reproduction, not a presumed hardware absence.
This selector did not execute GPU training or independently repeat that access
check.

## Selector verification and read coverage

One existing deterministic initializer check was executed, once, into fresh
`data/generated/first_order_dimension_mnist/promotion_selection_20260916_initializer/`.
It used `/home/amir/miniconda3/bin/python -B`, `PYTHONPATH=code`, bytecode off,
one BLAS/OpenMP thread, RLIMIT_CPU=120 seconds and RLIMIT_AS=512 MiB.
The source was executed unchanged with `--check --output` pointing to that
directory. Its purpose and fixed cases/thresholds were those in the read
initializer's precommitment: dense normalization at d=1,2,7,17 with iid and
paired folded/unfolded rules; fixed-seed folding; 128/256 scalar refinement;
and d=2 comparison with the maintained initializer at fixed replay marks.

Exit status 0; `passed=true`; Python 3.10.14, NumPy 1.26.4; check wall time
4.664684 seconds. Maximum dense discrepancy was 7.21645e-16, folding arrays
agreed exactly, maximum scalar refinement difference 1.54099e-13, and the
largest finest maintained-d2 difference was 0.000425679 (threshold 0.005).
Full fresh output is `initializer_check.json` in the preceding directory.
This verifies an existing finite algebra check, not the complete candidate,
CUDA behavior, MNIST training, or a Gaussian integration error bound.

Complete textual reads:

- `AGENTS.md`; all of `RESEARCH_WORKFLOW.md`; `docs/README.md`;
  `docs/NOTATION.md`; `code/README.md`; this study's `README.md`.
- `/etc/codex/skills/solve-math-rigorously/SKILL.md` and
  `/etc/codex/skills/investigate-conjectures/SKILL.md`; the latter's
  `references/evidence-ledger.md`, `references/adversarial-audit.md`, and
  `references/decisive-experiments.md`.
- Established `code/pde/observable_initialization.py`,
  `code/pde/observable_solver.py`, `code/pde/finite_network.py`.
- Study `INITIALIZATION_THEORY.md`, `P1_INITIALIZATION.py`, `P1_ENGINE.py`,
  `NETWORK_ENGINE.py`, `ENGINE_CHECK.py`, `MODEL_SCOPE_CHECK.md`,
  `COMPUTE_REPORT.md`, `PLAN.md`, `RUN.py`, `BATCH.py`, `DATA.py`,
  `PILOT_GATE.py`, `ANALYZE.py`, `VALIDATION_ANALYSIS.py`,
  `MATCHED_LOSS.py`, `MATCHED_LOSS_PLAN.md`, `WIDTH_COMPARE.py`,
  `SPEED_ANALYZE.py`, `REPORT.md`, `PCA_DATA.py`, `PCA_BATCH.py`,
  `PCA_ANALYZE.py`, `PCA_PLAN.md`, `PCA_REPORT.md`,
  `FULL_4096_CHECK.md`, `PCA_RUN_CHECK.md`, `PCA_DATA_CHECK.md`.
- The new initializer check JSON was read in full.

Complete selected established proof units in `docs/global_nonlinear.md`:
Section 3, lines 281–504; C.4.7.9 parts 3–4, lines 12249–12377;
C.4.7.10.B, lines 13161–13430; C.4.7.10.C.1, lines 13431–13522;
C.4.7.10.C.5–C.6, lines 13852–13981; C.4.7.10.D.5,
lines 15553–15736. The heading inventory was also inspected.
Truncated guide reads were repaired with overlapping complete reads.

Unread complement: all other studies, all novelty-debate documents, all
other established proof bodies/modules/tests, remaining study review reports,
the complete 874-line `REPLAY.py`, old raw numerical outputs and old generated
source snapshots. The mandatory README contains a summary of a broader
novelty debate; no linked debate/history was followed and none is used to
support selection. Old internal check reports listed above were read openly
as study evidence; this is a selector assessment and cannot serve as a blind
promotion review. Two fresh complete candidate reviews must include all actual
dependencies, producer/tests/recipes, and cannot substitute this read scope.

Initial metadata-only Git check found HEAD
`04b61a12795734cbfc93830bf0a164bab7d101c4`, an empty staged list and concurrent
working-tree changes. No Git index, branch, commit or other author's file was
changed. Only this report and the selector's new generated check were written.

## Next authorized handoff

An author may assemble the narrow A component and generic comparison methods
inside this originating study, fixing the named API/representation gaps and
supplying complete frozen dependencies. Select a numerical example only if
its full maintained reproduction is affordable and authorized. Then obtain
the workflow's two fresh complete adversarial reviews, standalone checks,
independent integration review and approval of the concrete final package.
No live `docs/` or `code/` integration is authorized by this selection.
