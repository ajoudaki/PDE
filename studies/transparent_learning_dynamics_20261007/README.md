# Transparent dynamics of deep nonlinear feature learning

2026-10-07. New user-directed research question, distinct from optimizing
compression. Work is confined to this study. No book edits or promotion.

## Research contract

Find an autonomous dynamical system whose state and interactions are meaningful
learning observables, rather than relabeled weights, and whose predictions
track the canonical dense gradient flow at its variability scale.
Fixed validation inputs may be declared initially and evolved passively with
no labels or training weight. The latest user clarification permits larger
state: further compression is not the current objective. A history-state
system must declare its full history as state, not call a few unclosed
moments a finite Markov ODE. Efficient unseen-input decoding is not required.

The reference has arbitrary fixed hidden depth, sphere inputs, analytic
activations with bounded strip derivative (values may be unbounded), independent
Gaussian initialization and exactly zero readout. Its forward normalization,
mean squared loss, block mobilities and existing label/width conditions are
retained. The target horizon includes the fitted endpoint. The desired error
is a maximum over the declared training and validation panel, or the stronger
whole-sphere norm if available. Labels enter driving sums only at training
indices. A scalar predictor guarantee must not be presented as a theorem
about every hidden feature.

Interpretability requires actual definitions of retained observables and an
explicit causal interaction law; neither an unclosed kernel hierarchy, a
trajectory table, a hidden dense oracle, nor an invertible weight renaming
alone resolves the question. An exact identity, an autonomous closure, its
comparison theorem, and the scientific explanation are separate claims.

## Authority and sources

The user authorized new theoretical work, diverse creative routes, persistence
toward resolution, and use of the current compression results. No literature
search is authorized or planned. The latest user request explicitly authorizes
controlled numerical training experiments and analytical approximations, and
pauses global-proof work. Deterministic identity checks accompany the numerical
work. Study inputs are its new derivations,
the maintained `docs/` setup/notation, and the explicitly user-invoked integrated
compression construction. No other research study is imported.

The integrated study is currently being updated by another task. Its README
reports a proof-completion pass in progress. We do not edit its files and do
not assume an audit PASS. Any transfer of its accuracy theorem will identify
that dependency and its status separately from exact new algebra.
Initial observed RESULT SHA-256:
`e78d8e7f7a741054bdd6d0b2f66190dbc12cd4e358822e2155007933b9d27ffa`.

## Parallel routes and ownership

| Route | Question | Owner / file |
|---|---|---|
| Causal observable geometry | Exact label-driven kernel/response interactions and closure obstruction | `observable_geometry` / `OBSERVABLE_GEOMETRY.md` |
| Relational quotient | Can compressed dynamics become an autonomous similarity system with transparent nonlinear algebra? | `relational_quotient` / `RELATIONAL_QUOTIENT.md` |
| Response and memory | Alternative causal response/history system, including noncommuting training forces | `response_memory` / `RESPONSE_MEMORY.md` |
| Synthesis | Compare routes, derive independent mechanism, audit guarantees and non-vacuity | Lead / `RESULT.md` and this README |

Each initial route is prompt-only and independent of the other routes; they
must disclose gaps rather than retrieve hidden prior research. Main is sole
writer of shared current notes. No Git transaction is requested.

## Current state

The latest deliverable is
[FROZEN_QUADRATURE_RESULT.md](FROZEN_QUADRATURE_RESULT.md): independent
integration of three frozen causal histories with32,768freshsamples each.
Lower-layer discrepancies nominally halve, but the prescribed fresh-resolution
gate still fails; upper effects are mixed. This is a necessary-moment audit,
not an improved coupled solver. All four runs including exact reproduction
are complete; global proofs and two-input cubic work remain paused.

The latest coupled-model deliverable is
[RESIDUAL_FILTER_RESULT.md](RESIDUAL_FILTER_RESULT.md): the separately bounded
16-input numerical repair is complete at 16 dense and eight causal runs.
The refined dense reference passes its checked mesh test and saved losses
are stable throughout, but lower-layer mean similarity errors remain 27–31%
on the matched filtered mesh. Particle effects and causal mesh changes are
unresolved. This is progress, not a full-system accuracy pass or a global
theorem. Global proofs and two-input cubic work remain paused.

The preceding deliverable is
[MULTISAMPLE_TRAJECTORY_RESULT.md](MULTISAMPLE_TRAJECTORY_RESULT.md): fixed
4/8/16-input panels with four passive inputs, full similarity-trajectory
comparisons, and a retained16-input numerical failure. Its52-run campaign is
closed. The separate numerical-repair contract and its outcome are below.

The preceding deliverable is
[UNEQUAL_RESIDUALS_RESULT.md](UNEQUAL_RESIDUALS_RESULT.md): unequal-label and
correlated-input tests, an ordered-response approximation with a retained
passive failure, and an exact passive-source decomposition showing layer
compensation and changing activation sensitivity. Its bounded campaign is
closed at26 dense and16 causal runs; global proofs remain paused.

The preceding deliverable is
[BEYOND_INITIALIZATION_RESULT.md](BEYOND_INITIALIZATION_RESULT.md): controlled
dense/population comparisons and a checked initialization-derived cubic clock.
The full candidate remains intact. Its training-mode reduction works well in
the tested symmetric example but has a resolved passive-output failure at the
larger amplitude; those passive observables must not be dropped. Global-proof
work remains paused. See the experiment contract and evidence paths below.

The preceding user-facing conceptual deliverable is
[CANDIDATE_SYSTEM.md](CANDIDATE_SYSTEM.md): one explicit causal feature--response
system, its closed first-tangent update, and a worked nonlinear two-hidden-layer
example with two interacting training samples and a passive input. Its rigorous
form is a discrete history-state population system. The example identifies
label-product-signed, derivative-gated cross-sample feature writes; it is not
only a statement that a kernel changes. The original full-trajectory
dense-variability guarantee is still missing.

The current result is [RESULT.md](RESULT.md). The broad explanatory research
goal remains open; an exact geometric realization is now proved and internally
checked, not merely conjectured.

Established in this study:

- Ordinary feature/velocity Grams can miss the first nonlinear response.
  The missing activation-times-sensitivity Gram has an explicit example.
- Ordered sample forces can differ despite identical force totals; the
  first nonlinear response has an explicit initialized response-Gram formula.
- A finite multiplication algebra closes nonlinear operations exactly, but
  its generic full form and a redundant anchored Gram lift retain the map
  information rather than achieving a new observable reduction.
- A singularity-free shear/polar construction gives an autonomous ODE in
  response Grams and rotating coactivation tensors, with exact source-runtime
  prediction equality, no new layer-rank assumptions, and polynomial overhead
  in the compressed dimension. Its signed overlap law and frame-qualified
  deformation/rotation mechanism are explicit.

The last result is an explanatory geometric representation, not a claim that
complete transfer information has disappeared. That distinction is stated at
the top of RESULT.md and is the remaining scientific bottleneck.

The independent first-round routes were frozen before cross-pollination.
The completed construction is in `SINGULARITY_FREE_POLAR.md`; its full-rank
domain extension supersedes the restricted domain of `MOMENT_ROUTE.md`.
`POLAR_AUDIT.md` and `POLAR_MECHANISM.md` independently reconstruct its algebra
and mechanism. `GRAM_PARTICLE_LIFT.md` records a rejected redundant state lift.
These are internal checks, not publication/promotion reviews.

Lead verification command:
`python studies/transparent_learning_dynamics_20261007/polar_identity_check.py`.
It passed three deterministic multilayer/rectangular cases, including
rank-deficient maps and nondiagonal SPD metrics. It checks local identities
and derivatives, not the external compression theorem or a training experiment.

The concurrently maintained integrated source was observed again at SHA-256
`479e29117ab6b8d4da6ae0a194cfe7dadf5b1267c217c6491f8fe1d05bbd3ccf`.
Its current audit/proof-completion changes are not silently treated as this
study's independent source audit. The exact transformation theorem needs only
the supplied runtime; its dense certificate is an explicitly inherited input.

Next authorized research action: determine whether meaningful, directly
sample-indexed coactivation/response observables can replace complete nonlinear
orientation information at dense-variability accuracy, with fixed nonzero labels
and without a hidden transfer matrix or a prerecorded trajectory.

## Aggregate-response continuation

The next independent routes were frozen before comparison:

- Causal Gaussian conditioning: CAUSAL_GAUSSIAN_ROUTE.md.
- Kinetic observable laws: KINETIC_OBSERVABLE_ROUTE.md.
- Typical Gram-information obstruction: TYPICAL_GRAM_INFORMATION.md.

Subsequent developments and their qualifications:

| Result | Status and boundary |
|---|---|
| Exact two-sided initialized Gaussian query law | Derived; finite forward/backward transcripts, not an independent-noise ansatz |
| Actual finite-width matrix-free force memory | FINITE_RESPONSE_MEMORY.md; exact Euler joint law internally checked; raw random records still width-dependent |
| Rank-robust clipped finite-program aggregate law | RANK_ROBUST_FINITE_PROGRAM.md; scoped audit passed; fixed program only |
| Actual unclipped neural finite-history law | UNCLIPPED_FINITE_HISTORY.md; scoped audit passed; bounded derivative gates permit one-sided RMS comparison without original higher moments |
| Quantitative fixed-program refinement | FIXED_HISTORY_RATE.md; scoped audit passed for \(n^{-1/2}\log^{2Q+2}(en)\) error at fixed \(Q\); no growing-program or all-time claim |
| Typical Gram-only obstruction | TYPICAL_GRAM_FIXED_TIME.md; internally checked fixed-time \(n^{-1/2}\) lower bound, superseding the earlier logarithmic-loss trajectory rate for this model |
| Adaptive scalar-circuit concentration | ADAPTIVE_SIGNAL_CONCENTRATION.md; internally checked bounded-class bound; coefficient adaptation allowed, population clipping and dynamical stability remain separate |
| Shallow kinetic all-time comparison | KINETIC_OBSERVABLE_ROUTE.md; candidate on an explicit additional small-label subclass, not the full original source scope |
| Sequential-force signature closure | RESPONSE_SIGNATURE_CLOSURE.md; conditional theorem, not a full-class closure or a proved polylogarithmic state bound |
| Inverse-Gram-free causal response law | RESPONSE_GAUSSIAN_CLOSURE.md; finite-program equivalence internally checked, including singular histories and total derivatives |
| Common Hilbert realization | RESPONSE_HILBERT_REALIZATION.md; scoped internal audit passed; compatible meshes, bounded initialized actions and adjoints |
| Continuous all-time aggregate limit | CONTINUOUS_RESPONSE_LIMIT.md; scoped internal audit passed **conditional on stated finite-width carrier/operator/tail premises**; qualitative convergence only |

The fixed-time obstruction includes arbitrary fixed small nonzero labels and
all measurable predictors from the specified initialization Gram. It does not
rule out an \(O(n^{-1/2})\) population approximation or enriched response state.
The unclipped law identifies actual deep feature learning on each fixed finite
Euler mesh, including passive inputs, without substituting a clipped proxy.

The information audit also distinguishes a causal source computation from
offline replay using a metric selected from its completed future field table.
The latter can inherit a source compression certificate, but discarding future
scalar answers does not erase future-table information in the selected metric.
No claim of counterfactual-control closure is inferred from that replay.

The main result now reflects these advances and the still-open scientific
goal. Inverse-Gram regression coordinates have now been eliminated from the
finite-program formulation. The continuous-time law also has a conditional
qualitative foundation. The highest-leverage remaining step is a growing-history,
gap-robust quantitative comparison and controlled response measures, followed
by a finite explanatory closure. No new experiment, Git transaction, book edit,
or promotion occurred in this continuation.

Additional current proof work:

- CAUSAL_KERNEL_DYNAMICS.md specializes the response theorem to the full
  neural forward/backward circuit. Its same-time response is an explicit
  carrier-weighted curvature recursion, transmitted through squared gates.
  This lead specialization awaits a scoped audit.
- OSGOOD_RESPONSE_STABILITY.md proves conditional dimension-free continuity
  and residual-weighted stability from exponential or square-exponential
  carrier budgets. The budgets and finite residual mass are separate premises.
- DEEP_LINEAR_SPECTRAL_DYNAMICS.md derives a restricted exact spectral
  covariance dynamics for two linear hidden layers. The lead read it fully;
  it awaits an independent check and cannot substitute for the nonlinear target.
- SHALLOW_GLOBAL_RESPONSE_RATE.md is assigned to remove the shallow
  kinetic proof's extra absorption cap by a time-weighted Gronwall argument.
- GAP_FREE_RESPONSE_STEP.md is assigned to establish a quantitative
  Gaussian response step without positive history-gap constants.
- CONTINUOUS_SUSCEPTIBILITY.md is assigned to justify response measures,
  including possible same-time atoms, rather than treating formal derivative
  sums as an already proved continuous equation.

### User-directed conceptual checkpoint

The user explicitly reprioritized one closed candidate and a worked nonlinear
example before further proof expansion. The broad rate/continuum projects were
therefore paused after freezing their current notes. The new bounded checks are:

- CANDIDATE_CLOSURE_CHECK.md: full local laws and joint first tangent fields
  close the finite chronological system; averaged response kernels alone do not.
- TWO_LAYER_MECHANISM_CHECK.md: complete initialized two-layer tanh
  calculation, including both layers' cross-Gram accelerations and passive
  response. It concerns finite-width initial derivatives followed by their
  width limit, not an interchange with a positive-time limit.
- CANDIDATE_SYSTEM.md records autonomy, loss and accuracy qualifications
  alongside the equations. No all-time root-width theorem is claimed.

The latest user request supersedes the global-proof priority: understand this
same candidate throughout learning through controlled experiments and
analytical approximations before pursuing its full-trajectory guarantee.

## Beyond-initialization experiment contract (2026-10-07)

Global-proof efforts are paused. Their frozen drafts are not upgraded by this
experimental phase. In particular SECOND_FORWARD_RESPONSE_STEP.md and
NONLINEAR_RESPONSE_CONTINUATION.md remain unreviewed; the latter also has an
identified old-history vector-norm constants issue. No global conclusion is
inferred from them.

Decision: does the present causal system describe label-signed feature writes,
their saturation as residuals disappear, and passive-input representation
motion beyond initialization? Does removing initialized reciprocal feedback
have a different effect from removing learned middle-matrix memory?

The smallest nondegenerate testbed is the checked two-hidden-layer tanh example:
unit inputs e1,e2 and passive (2e1+e2)/sqrt(5), zero readout, canonical Gaussian
weights and mobilities, labels a(1,1) or a(1,-1). Fixed a=0.15 tests the
small-label expansion; a=0.6 tests nonlinear corrections. These are numerical
test amplitudes, NOT certified instances of the original conservative label
cap. Depth, data and activation are unchanged across controls.

H1: the full response law matches dense Euler ensembles within sampling and
width uncertainty; its first nonlinear approximation predicts signed feature
changes over a non-infinitesimal horizon. H0: apparent explanation is only an
initial-time effect, or an omitted reciprocal/memory channel is immaterial.
Output accuracy alone cannot decide this: primary observables are changes in
both training cross-feature Grams, passive output, and the three tangent-kernel
blocks. Secondary observables are passive feature movement and gated update
strength versus initial saturation.

Controls: high-accuracy dense RK4 with step-halving; dense Euler on the same
mesh as the causal solver; frozen-middle-matrix dense dynamics; frozen-feature
readout flow; and, if solver validity passes, causal dynamics with reciprocal
terms removed. A local-affine activation control may isolate moving derivative
gates but must be reported as a changed transductive model, not a legitimate
approximation theorem. Same initial dense draw is reused for paired controls.

Primary horizon T=24, dense RK4 step 0.1 with 0.05 refinement. Numerical pilots
may choose causal Euler step 0.4, 0.2 or 0.1 according to runtime/conditioning;
Euler time bias is measured against dense Euler, not assigned to the closure.
Dense widths 256,512,1024 with seeds 101,202,303,404; population quadrature
sizes 1024,4096 (8192 only if the sampling floor masks the comparison), seeds
1701,1702,1703. Pilot width128/population256 checks implementation only.

Validity gates: no nonfinite values; exact finite identities within 1e-9
relative-to-unit scale; RK4 refinement errors below 1% of the paired feature
change or 1e-5 absolute; report every PSD truncation and its covariance defect.
For population comparisons use an uncertainty envelope equal to three ensemble
standard errors plus measured refinement change plus observed dense-width mean
change. Agreement inside that envelope is empirical support, not a theorem;
systematic discrepancy beyond it on two seeds/resolutions is a failure of the
tested numerical candidate; conditioning or unresolved sampling error means
inconclusive. A mechanism effect must exceed that envelope and have consistent
sign across replicas. Label-amplitude refinement compares scaled changes at
0.15 and 0.6; an additional 0.075 run is allowed if the expansion's leading
order is unresolved. No fit to future dense trajectories is permitted.

Budget: at most 80 dense trajectories and 24 causal trajectories, single-thread
BLAS, at most 30 minutes cumulative numerical wall time and 4 GiB peak per
process. Stop at the budget even if inconclusive. Fix implementation bugs with
unit tests, preserve failed outputs, then rerun the same configuration; do not
search for favorable geometry. All runs and source hashes go under
data/generated/transparent_learning_dynamics_20261007/beyond_initialization_v1/.
No book edits, promotion or Git commit is authorized by this experiment.

Analytical diagnostic branch, fixed before its trajectory comparison: the
small-label frozen-kernel residual clock overpredicts late feature change,
while the squared *measured integrated residual* organizes the three declared
amplitudes. That measured clock is diagnostic, not an autonomous predictor.
Test instead the cubic, initialization-derived autonomous clock
u'=Y-nu*u-kappa*u^3, where nu and kappa are computed from explicit initial
Gaussian moments (no coefficient fitted to later dense data). Its output and
both feature-Gram trajectories will be compared with all already declared
amplitudes. This is a new finite-order approximation, not a new global theorem.
All original failed/less-accurate frozen-clock predictions are retained.

The bounded phase's result and interpretation are now in
BEYOND_INITIALIZATION_RESULT.md. Numerical source code was frozen during the
campaign; all controls, coarse/fine trajectories and the plotting-only failed
analysis attempt are retained. Internal implementation and evidence audits
are CAUSAL_NUMERICAL_AUDIT.md and EXPERIMENT_EVIDENCE_CHECK.md. The cubic-clock
coefficient has its separate analytic check; passive Gaussian coefficients
were independently frozen before their comparison and expose a moderate-label
failure of the reduced approximation. This failure is not a failure of the
full candidate. No global proof work resumed and no commit was performed.
The predeclared sampling-floor branch used the final two population8192 runs;
the phase is stopped at77 dense and23 saved causal runs plus its one small
causal timing pilot. Numerical trajectory time totals about491 seconds and
maximum observed process RSS about1.25 GiB. All trajectory/source checksums and
the last refinement are in the run directory's final_manifest/. The numerical
run budget is closed; further experiments need a separately recorded phase.

## Unequal-residual and passive-mechanism phase (2026-10-07)

The next goal continuation follows the user's latest experimental priority,
not the superseded global-proof priority. The previous turn was progress:
it implemented and tested the candidate, found a useful cubic training clock,
and resolved its passive-output failure at moderate labels. Its campaign stays
closed. This is a separate bounded continuation of the same investigation.

Decision: what additional response information matters when training residuals
do not share a single clock, and what creates the passive output's nonlinear
correction beyond the training-mode cubic? H1: the full causal system preserves
these effects, while accumulated residuals alone may lose ordering information.
H0: the symmetric success is a special-case coincidence, or passive mismatch
is only mis-timing and disappears after correcting the residual clock.

Two fixed tests (not a geometry search): (A) orthogonal inputs e1,e2 with
unequal labels (0.6,-0.3); (B) correlated inputs e1,(0.6,0.8), same labels.
The passive input remains (2,1)/sqrt(5). The first changes only label symmetry;
the second also restores nonorthogonal input interactions. The original
opposite-label (0.6,-0.6) example supplies a passive-mechanism diagnostic
reference, not a re-opened run selection. Tanh, depth2, zero-readout Gaussian
initialization and all normalizations are unchanged. As before these are
exploratory finite examples, not instances certified by the conservative
theorem label cap.

Primary metrics: complete training/passive output curves, all current hidden
Grams, per-sample accumulated deficits, their antisymmetric ordered integral,
and passive nonadditivity f3−a*f1−b*f2 with v3=a*v1+b*v2. Exact within-path
decompositions separate readout on the initial passive feature from moving
passive features, and middle-weight feature velocity from propagated lower
feature velocity. A changed control's endpoint difference is not called an
additive full-path contribution. No coefficient may be fitted to the future
reference trajectory.

Dense RK4: widths512,1024, seeds101,202,303, step0.1, horizon24. Check step0.05
for seed101 of each new case. Dense Euler at step0.4 uses width1024 and the
same three seeds. Original symmetric mechanism traces use width512 seeds101,
202; matched frozen-middle and local-affine traces may use those two seeds.
Population: N4096, step0.4, seeds1701,1702,1703 for each new case; N1024 at
steps0.4 and0.2, seeds1701,1702, for separate refinement; reciprocal-off
N4096 in the correlated case uses1701,1702. No broad sweep or unseen-case
selection. Secondary initialization-only coefficient integration is capped
at60 seconds and512 MiB; a proposed approximation is frozen before testing it.

Validity/decision rules: exact finite diagnostics must agree within1e-9 on
unit scale; RK4 step refinement below1e-5 or1% of the mechanism contrast;
nonfinite states invalidate a run. Report Gaussian covariance truncation and
finite-population dependence separately. Fixed-Euler agreement is assessed
against three combined run-level standard errors plus measured particle and
dense-width refinement changes, a diagnostic envelope not a confidence theorem.
An effect must exceed numerical refinement and be sign-consistent over seeds
to support the mechanism. Failure/inconclusiveness is retained, never corrected
by fitting a completed trajectory. A changing residual direction by itself
does not prove that every observable needs ordered memory.

Budget and stop: at most28 dense trajectories and16 causal trajectories,
single-thread BLAS,20 minutes summed numerical wall time,4 GiB peak per process.
Stop at the first exhausted bound or after the declared comparisons. Bug fixes
require deterministic tests and the same configuration; no favorable case
replacement. Generated outputs go to
data/generated/transparent_learning_dynamics_20261007/unequal_residuals_v1/.
Main owns shared notes/experiments. Scoped agents own
ASYMMETRIC_RESPONSE_APPROXIMATION.md and PASSIVE_NONLINEARITY_DIAGNOSTICS.md.
No global proof expansion, external literature, shared-book edit or commit.

### Phase-2 outcome and stop

The declared campaign is closed at26 dense and16 causal trajectories, plus
one initialization-only quadrature/approximation program. Summed numerical
wall time was336.5 seconds; maximum process RSS677812 KiB. No cohort failed
or was replaced. Coefficient tensors and the six-state ordered closure were
frozen before their comparison with dense outputs. Both cubic variants miss
passive prediction in case A; retaining ordered response alone did not improve
that error. Full causal/dense matched-Euler mean comparisons stayed within the
predeclared descriptive sampling/refinement envelope in both new geometries.

UNEQUAL_RESIDUALS_RESULT.md records exact passive source identities, additive
same-path measurements, the separate ablation compensation effect, and the
Euler-versus-continuous diagnostic correction. ASYMMETRIC_RESPONSE_APPROXIMATION.md
and PASSIVE_NONLINEARITY_DIAGNOSTICS.md contain complete local derivations.
PHASE2_INSTRUMENTATION_CHECK.md records independent bounded code/identity tests.
PHASE2_APPROXIMATION_EVIDENCE_CHECK.md separately reconstructs tensor indices
and numerical claims; its missing-plus transcription finding was corrected in
the main report without any change to frozen numerical sources.
The generated analysis and checksums are in unequal_residuals_v1/analysis/.
No full-trajectory theorem was attempted or inferred, and no commit was made.

## Nonlinear-gate continuation phase (2026-10-07)

Previous goal turn: progress. It verified broader fixed-mesh causal comparisons,
resolved a failed ordered-cubic passive approximation, and measured additive
passive learning sources and layer compensation. Those cohorts stay closed.
This phase follows the user's continuing analytical/experimental priority;
global proof work stays paused.

Decision: is the passive cubic failure mainly a truncation of tanh on a useful
initialized feature-motion direction, or does learning significantly change
the preactivation motion itself? Keep the same two-hidden-layer Gaussian tanh
network and original orthogonal panel e1,e2,(2,1)/sqrt5. Evaluate the proposed
initialization-only continuation in PASSIVE_NONLINEARITY_DIAGNOSTICS.md:
upper features tanh(Z+u²L/2), where L is the exact initialized second derivative
along the residual-free symmetric orbit; integrate the corresponding readout.
Use the existing unfitted cubic training clock and reconstruct the passive
output from its geometric training part plus the nonlinear passive defect.
The matched control keeps only its exact finite-initialization cubic defect.
Neither predictor may read a later dense weight, output, or fitted coefficient.
Before execution, the local derivative check identifies one additional matched
control needed for attribution: multiplying quadratic features by their cubic
integrated readout retains a known fifth-order cross-product even without
reevaluating tanh. Record that polynomial-product control too; full tanh versus
this product isolates activation curvature beyond the same polynomial fields.
The primary full-tanh versus cubic success criterion remains unchanged.

H1: retaining the full activation on the initialized quadratic displacement
reduces the passive prediction error materially, identifying activation
truncation as a major missing ingredient. H0: the displacement/readout geometry
changes enough that evaluating tanh on this fixed direction fails to repair
the model. A diagnostic third outcome is clock error or finite-width asymmetry;
test both with the actual measured mode clock, explicitly as diagnostic only.

Primary metric: per-seed maximum passive-output error on [0,24], compared with
the matched finite-initialization cubic control. H1 support requires at least
50% reduction in the width512 opposite-label Y=.6 mean error, reduction in each
of its three seeds, and the same improvement direction for the two width1024
checks. Failure to improve that cohort disfavors this explicit continuation;
intermediate/inconsistent improvements are inconclusive for H1. It does not
falsify nonlinear resummation in general or the full causal system. Control
cases Y=.15 opposite labels and Y=.6 equal labels test scope, not case selection.

Primary mechanism diagnostics, fixed in advance: compare true upper and lower
preactivation displacements with their initialized quadratic predictions at
the measured mode clock; record projection on the initialized direction and
the orthogonal remainder; separate passive readout-weighted feature error
from readout error on the same dense path. A least-squares scalar projection
on the fixed initial direction is permitted only as an explicitly labeled
oracle diagnostic, never a predictor. Do not interpret this diagnostic as
an initialization-only construction. Actual asymmetric residual accumulation
is recorded and not silently forced to zero.

Run plan: width512 seeds101,202,303 for the three cases (.15,-),(.6,-),(.6,+),
width1024 seeds101,202 for (.6,-), and step-halving width1024 seed101 for
(.6,-):12 new dense trajectories total. RK4 step.1 and refinement.05, horizon24.
All predictor coefficients use the same initialized draw as their dense
reference. Readout quadrature order32, checked against64 at each saved point;
fixed cubic-clock constants come from the previously frozen Gaussian integrals.
No new full causal solver cohort. Source hashes and raw diagnostics go under
data/generated/transparent_learning_dynamics_20261007/gate_continuation_v1/.

Validity: finite derivative checks <=1e-8; dense step-refinement output error
<=1e-5; quadrature refinement <=1e-7 for output curves; nonfinite states fail.
Readout/feature decomposition must reconstruct its actual comparison <=1e-10.
Comparisons to prior matching dense predictions verify producer consistency.
Budget:12 dense runs, at most10 minutes summed numerical wall,512 MiB per
process, one BLAS thread. Stop after declared comparisons or first budget hit;
no post-result case/order search. A repeated seed for exact reproducibility
may use one additional run only if all scientific runs fit the same time cap.
Analytical work is local and bounded: main owns code/report; scoped agent owns
NONLINEAR_GATE_CONTINUATION.md. No global proofs, book edits or Git commit.

### User-directed stop of two-input approximation work

The user now explicitly requests the next bounded phase on4–16 training inputs,
nontrivial geometry, varied labels and several passive inputs, with full-trajectory
feature-Gram comparisons at every hidden layer. No further two-input cubic
refinement is authorized. The12 already launched dense trajectories finished;
their raw outputs remain under gate_continuation_v1/. No additional replication,
new approximation variant, or continued campaign is launched. The local derivation
is frozen in NONLINEAR_GATE_CONTINUATION.md and the partial static code check in
GATE_CONTINUATION_CODE_CHECK.md. These do not replace the full causal system.

## Multisample feature-trajectory phase (2026-10-07)

User-directed continuation of the same system. Keep two nonlinear tanh hidden
layers and the complete causal feature-response law unchanged; generalize only
the implementation's hard-coded sample/panel dimensions and preserve physical
learning factor2/m. Global proofs and two-input cubic refinement are paused.

Testbeds fixed before training: m=4,8,16, input dimension8. Build16 unit training
vectors from four nonorthogonal cluster centers, with fixed Gaussian perturbation
seed6201 and amplitude.65, ordered round-robin by cluster. The three panels use
the firstm entries. Labels have a fixed mixed-sign four-round pattern and varied
magnitudes .25+.075*((5i) mod7), independent of any initialized network or result.
Use4 passive unit inputs: normalized v0+v1, v0−.6v1, v2+v3, and e5+e6−e7.
None has a label or training force. Center vectors and all arrays are explicitly
defined in multisample_experiment.py and saved with every run. No geometry search,
orthogonalization, special initialization, or label-threshold certificate.

Predictions to test BEFORE execution (hypotheses, not theorems):

1. The full causal system tracks the evolving uncentered feature similarities
   at BOTH hidden layers, separately for training–training and training–passive
   blocks, throughout the saved horizon. Primary error is maximum-over-time
   entrywise and block-RMS discrepancy of ensemble means; report absolute Grams
   and changes from each realization's initialization separately. Mean pairwise
   dense discrepancies supply a descriptive variability comparator, not a bound.
2. The exact initialization-derived Gram acceleration predicts a substantial
   part of the early feature-change direction beyond the first infinitesimal
   step. Do NOT predict each sign from label products on correlated data.
   Test cosine alignment between actual Gram change and initialized acceleration
   in each block/layer; record how long it survives. Hypothesis threshold is
   cosine>=.7 at20% loss reduction; report separately at50% and80%, without
   assuming the latter must pass. Include off-diagonal TT results so a diagonal
   norm change cannot manufacture alignment. No coefficient fitted to later data.
3. Removing reciprocal return changes feature-similarity trajectories and passive
   predictions even if training loss remains small. In m8 test full versus
   no-return causal laws using two matched seed identifiers; this is an
   intervention, not an additive same-trajectory contribution or another dense
   gradient model. Judge each layer/block, not only loss or endpoint output.
4. Learned middle writes and activation sensitivity have distinct effects.
   In m8, freezing W is predicted to shift later feature motion toward layer1;
   the exact initial lower acceleration is unchanged, so no initial effect is
   asserted. Anchored-affine activation controls retain weight learning but remove
   gate drift; test their TP-Gram changes and passive predictions against full
   tanh. These are changed controls, not substitutes for the target system.

Physical horizon T=9.6m, equivalently 2t/m in[0,19.2]. Primary Euler timestep
dt=.2m gives48 updates. Dense trajectories: widths512,1024, seeds101,202,303,
for eachm (18runs). High-accuracy dense checks use width512 seed101 eachm,
RK4 dt=.05m and refinement .025m (6runs). Dense m8 controls frozen-W and
anchored-affine use width512 seeds101,202 at Euler dt=.2m (4runs), with seed101
each refined to dt=.1m (2runs). Total dense cap30.

Causal trajectories: N512 particles, seeds1701,1702,1703 eachm (9runs);
N1024 seed1701 eachm for particle refinement (3runs); N256 seed1701 eachm
at dt=.2m and .1m for matched particle/step refinement (6runs). In m8, no-return
and no-learned-middle controls use N512 seeds1701,1702 (4runs). Total causal
cap22. Statistical comparisons use ensembles, not equality of unpaired random
realizations; same seed identifiers across ablations need not preserve an exact
Gaussian common-random coupling after factorization rank changes.

Numerical gates: deterministic generalized producer/derivative/memory checks
<=1e-8; exact reduction to old two-input program; no nonfinite fields; dense RK4
step-refinement Gram/output discrepancies <=1e-5 or1% of measured change;
report Euler bias independently and match discretizations for primary accuracy.
Record all Gaussian factor truncation/rank/covariance diagnostics. Use float64,
one BLAS thread. Numerical-only tiny pilots are allowed for producer validation,
not changing data or selecting favorable outcomes.

Accuracy decision: for eachm/layer/block, compare mean discrepancy at every saved
time with3combined run SE plus measured particle-size and dense-width changes.
This is a diagnostic envelope, not a confidence theorem. Systematic excess above
.005 absolute or20% of dense feature drift at at least3 consecutive nonzero
times is a discrepancy to investigate; otherwise report resolution-limited
agreement. Also report errors normalized by actual feature drift, because a
loose envelope must not conceal failure to capture learning. No scalar maximum
over all blocks may replace the per-layer/per-block tables. A mechanism effect
must exceed numerical refinement and have consistent direction over its two
seeds; otherwise mark inconclusive or contradicted, not confirmed.

Hard budget:30 dense+22 causal scientific runs;45 minutes summed numerical wall;
12 GiB peak perprocess and at most2 simultaneous causal processes. Stop at the
budget or completion of declared comparisons. If a prescribed Euler mesh is
unstable, preserve and label it; use only the already declared half-step cohort
to diagnose, with no unannounced longer-horizon or new-grid sweep. If loss has
not fitted by the horizon, report that limitation and full observed learning
interval rather than claiming an endpoint/global result.

Generated evidence: data/generated/transparent_learning_dynamics_20261007/
multisample_v1/. Main owns dataset/dense driver, analysis and shared notes;
scoped implementation agent owns causal_panel_simulator.py; mechanism agent
owns MULTISAMPLE_MECHANISM_PREDICTIONS.md. No old frozen sources, shared book,
other study, external literature or Git index is edited.

### Multisample phase completed: mixed outcomes

The predeclared30 dense+22 causal runs finished with frozen source hashes,
557.835 seconds summed numerical execution and5882.9 MiB largest process RSS.
No additional scientific grid/seed runs were launched after failed checks.
MULTISAMPLE_TRAJECTORY_RESULT.md is the current report;
analyze_multisample_experiment.py produces the blockwise table, full49-time
error curves and static figures from saved arrays alone. All52 saved mode
pairings are valid. The frozen general driver has an unsupported-mode dispatch
defect documented in MULTISAMPLE_IMPLEMENTATION_CHECK.md; it affects none of
these runs and is not silently treated as a valid ablation.

For m4/m8, the full law tracks both layers and both blocks at3.6–11.8% of
dense feature-change RMS, with the explicit qualification that these are
ensemblemeans on a matched Euler mesh. Dense RK4 references pass refinement,
but causal Euler step bias is not zero. For m16,57–67% relative errors and
large step sensitivity prevent a fullhorizon accuracy conclusion. Its dense
RK4 pair also fails the declared gate. No-sustained-excess under a large
sampling/width envelope is not accepted as success for this unstable case.

Mechanisms: early initial-direction prediction passes in all panels, but
the direction turns later; middle-write removal shifts motion downward;
reciprocal removal yields more individual lower displacement but weaker
offdiagonal associations at matched loss. The last diagnostic is explicitly
post-test and lacks ablation-specific mesh refinement. Late affine controls
are numerically unresolved, although an early-stage contrast survives the
available refinements. No global proof or new two-input approximation.

MULTISAMPLE_ACCURACY_CHECK.md independently recomputes the main arithmetic
from the saved data; MULTISAMPLE_MECHANISM_CHECK.md independently analyzes
mechanisms/refinement. Neither is an independent rerun of the full campaign
or promotion. Current next action is a separately bounded numerical-stability
repair of the same law on the unresolved panel; no automatic extra cohort
is authorized by this record. Persistent global research objective remains
open, with its proof project paused at the user's request.

## Residual-filtered integration phase (2026-10-07)

Previous goal turn: progress. The multisample campaign found informative4/8
tracking and mechanisms, but16-input time-step instability. The user-directed
goal continuation now pursues numerical repair of this same system. The old
52-run campaign is not reopened. No global proofs, two-input approximation,
other dataset search, book edit, or Git transaction.

Decision: can a consistent residual-filtered integrator remove the coarse
16-input instability while retaining both hidden-layer similarity trajectories?
H1: much of the failed comparison was the unstable Euler integration; after
repair, causal/dense same-integrator means track within20% of dense movement
in each TT/TP layer block, subject to particle/width uncertainty. H0: a large
systematic blockwise discrepancy persists after stable integration. A third
outcome is unresolved particle or time bias; neither outcome changes a global
theorem. This is a numerical method for the same flow, not a new learning
mechanism or a fixed-step claim of equivalence to ordinary gradient descent.

Method fixed before new runs: at each current full-model state, form the
training kernel K=C2+C1*D2+S*D1 and replace raw training deficit c=y-f in
the step's learned writes by solve(I+hK,c), h=2dt/m. Retain raw deficits
separately. Recompute K, all fields, memory and reciprocal sensitivities each
step; all historical writes and formal frozen-coefficient tangents use the
stored filtered deficits. Passive inputs are evaluated but excluded from
the solve and forcing. Dense uses the same filtered-deficit parameter update.
The continuous vector field is unchanged to first order as h tends to zero;
unconditional nonlinear stability or high-order accuracy is NOT assumed.
The finite-linearized residual contraction and implementation must pass
deterministic checks before scientific execution.

Keep the exact previous16-input dimension8 geometry, labels, initialization,
four passive inputs, and normalized horizon19.2. Primary filtered step.2.
Dense filtered: widths512/1024, seeds101/202/303 (6runs). Dense RK4 step.025
on those same widths/seeds (6runs), plus step.0125 width512 seed101 (1run).
Filtered dense step.4,.1,.05 width512 seed101 (3runs). Dense total16.
Full causal filtered N256 step.2 seeds1701/1702/1703 (3runs), N128 step.2
and.1 seed1701 (2runs), N512 step.2 seed1701 (1run), N256 step.4 seed1701
(1run). If all complete within budget, one exact fresh-run reproduction of
N256 step.2 seed1701 (1run). Causal total cap8. No new controls/geometry.

Numerical validity: no nonfinite fields; I+hK solve defect<=1e-10 on unit
scale; producer Euler-equivalence and frozen-response probes<=1e-8; exact
filtered-write readout reconstruction<=1e-10. Dense RK4 reference must pass
the existing1e-5 or1% Gram/output-change refinement gate. Report every loss
increase, and call a scheme unstable if any exceeds.001 of initial loss.
Report filtered dense mesh bias against RK4 and causal step-halving separately.
Only call the latter resolved at the former1e-5 or1% criterion; a stable
same-filtered-mesh comparison does not clear a failed continuum accuracy gate.
Report Gaussian factor errors and discarded variances, particle-size changes,
and dense-width changes separately. Predeclared accuracy metric stays max-time
entrywise and blockRMS for absolute Grams and changes from initialization;
TT includes diagonals, with offdiagonal supplementary checks. Three-run means
and their sampling envelopes are descriptive, not high-probability guarantees.

Hard budget:16dense+8causal scientific runs,30minutes summed numerical wall,
12GiB perprocess, one causal process at a time, single-thread float64. At most
one further tiny deterministic validation process at a time. Stop at first
budget violation or after declared runs, including failed validity results.
No extra mesh, horizon, population, integrator or seed is selected after seeing
scientific outcomes. A memory preallocation estimate limits every run.
Generated outputs: data/generated/transparent_learning_dynamics_20261007/
residual_filter_v1/. Frozen sources remain untouched. Main owns new numerical
source, driver, analysis and sharednotes; scoped agent owns
RESIDUAL_FILTER_INTEGRATOR_CHECK.md. Reproduction uses a fresh outputdirectory.

### Residual-filtered phase completed: stability repaired, accuracy unresolved

All 24 prescribed scientific runs completed within the cap: 1277.38 seconds
summed numerical execution and 10790.6 MiB maximum process RSS. No additional
scientific run was added after inspecting outcomes. All saved arrays are
finite and all saved raw losses are nonincreasing. The width-512 seed-101
dense RK4 .025/.0125 check resolves hidden similarities below 1e-8; this
does not separately certify every width-1024 ensemble reference.

Same-filtered-mesh errors in layer-1 TT/TP and layer-2 TT/TP are respectively
27.33%,31.41%,17.39%,12.37% of dense mean feature-Gram movement. Thus the
predeclared all-block 20% target fails in layer 1. At matched 99% mean-loss
reduction, lower offdiagonal/TP errors against RK4 remain28.75%/31.30%:
the causal mismatch is not removed by the timing diagnostic, even though
individual feature-displacement magnitudes are close.

The alternative explanation remains live: one 256-to-512 particle change
exceeds the measured primary mean discrepancy in every block, and the
128-particle .2/.1 comparison fails all four 1%-entry gates. Same-seed mesh
changes include adaptive Gaussian representation changes; they do not isolate
deterministic time error. Even the finest filtered dense mesh fails its
stricter 1%-entry gate. No population continuum claim follows from stable loss
or from no sustained excess beyond the broad descriptive uncertainty envelope.

The exact filtered-write readout identity holds to2e-15; using the raw
residual incorrectly gives .17148 error. A fresh repeated causal run matches
all19 arrays exactly. RESIDUAL_FILTER_EVIDENCE_CHECK.md independently
recomputes complete saved-array statistics; this is not a full campaign rerun.
RESIDUAL_FILTER_INTEGRATOR_CHECK.md audits the linearized step and discloses
an off-campaign Boolean guard issue that affects none of the full-model runs.

Current phase classification: progress, not proof or accuracy closure. The
next numerical question is separating population quadrature from step bias
without replacing the causal mechanism. The current cohort is closed;
global proofs and two-input cubic refinement remain paused.

## Fresh-quadrature self-consistency audit (2026-10-07)

Previous goal turn: progress. Stable stepping repaired the 16-input reference
and exposed a lower-layer similarity discrepancy; time and population
integration errors remain unresolved. The current continuation selects a
cheaper diagnostic before another adaptive training campaign. Global proofs,
two-input cubic analysis and mechanism-removing approximations remain paused.

Decision question: do fresh, higher-resolution Gaussian population averages
reproduce the coefficients and observables of the recorded causal trajectory
at its existing step? This isolates a self-consistency defect of that finite
particle computation without changing the dataset, horizon, or memory law.
It is not a new autonomous solver and does not separate continuous-time bias.

H1: finite-particle self-consistency defects are material relative to the
observed dense comparison, and freshly integrated means move toward the
dense reference. H0: recorded population averages are already self-consistent
to a small fraction of the discrepancy, leaving other explanations dominant.
A third outcome is inconclusive quadrature accuracy or a material defect in
a direction that does not explain the dense discrepancy. No outcome alone
validates or falsifies the limiting causal law.

This phase tests necessary current-moment consistency, not every response
coefficient or every two-time covariance. Higher fresh sample count does not
restore covariance directions absent from the saved 256-particle Grams, or
recompute a coupled trajectory. Those limitations remain even if its measured
moment defect is small or its fresh averages move toward dense.

Freeze each previous 256-particle trajectory's filtered write coefficients,
all C1,D2,Rh,Rdelta histories and their Gaussian covariances. Re-evaluate its
local lower and upper circuits on fresh independent Gaussian populations;
keep temporal correlations within each family, lower root independent of xi,
and the upper eta family independent of both. Never recompute the filter,
residual forcing, reciprocal coefficients or covariance from the fresh
particles. Report fresh raw losses only as diagnostics, not as driving forces.
The previously saved dense paths are comparison evidence only, never inputs
to the frozen causal replay.

Fixed inputs: the same 16 training directions, dimension8, mixed-sign labels,
four passive inputs, normalized horizon19.2 and filtered step.2. Source runs
are residual_filter_v1/causal_m16_n256_s1701_h0.2_filtered and its1702/1703
counterparts. Fresh Gaussian seeds8101/8102/8103 respectively;32768 samples
per source in32 batches of1024. Repeat source1701/seed8101 once in a fresh
process/outputdirectory. Exactly4 scientific runs, at most20minutes summed
numerical execution,12GiB/process,one scientific process at a time. Stop at
the first exhausted budget or completed set, irrespective of results.

Primary metrics: current feature-Gram matrices and changes from each circuit's
own initialization, separately layer1/2 and training-training/training-passive,
including an offdiagonal training diagnostic. Report max-time blockRMS and
entry errors versus the source and versus previous same-step dense means;
report predictions and actual individual-feature displacement separately.
Compare the fresh correction's direction with the old dense discrepancy,
without confusing a frozen-coefficient replay with an improved coupled model.
Compare ensemble means across the three sources, with all single-source
results retained. No data/seed selection or trajectory coefficient fitting.

Prespecified interpretation: a fresh-minus-source change below5% of the
dense mean Gram-change RMS in all four blocks supports negligible measured
self-consistency defect. A defect above20% in a block is material only if
it also exceeds three estimated fresh-integration standard errors at its
maximum time. Intermediate cases are unresolved. To call the defect an
explanation of the original discrepancy, additionally require that the
fresh ensemble correction reduces the maximum-time dense-comparison error
by at least50% in that block. This is a descriptive diagnostic, not a
simultaneous probabilistic bound. If it moves away, retain that adverse result.

Quadrature controls: save per-batch observables, independent-half averages,
and nested first8192/16384/32768 averages. A fresh mean is considered resolved
for this diagnostic only if its three-standard-error block scale and its
two-half block difference are each below5% of dense mean Gram-change RMS;
report each failing block as unresolved even if another condition passes.
These criteria concern frozen-circuit integration, not training-law accuracy.

Implementation gates before scientific execution: exact same-primitive replay
of a tiny full causal run must match all local fields and predictions to1e-12;
zero-label and rank-deficient covariance cases must work; factor covariance
maximum-entry error must be below1e-8. Fresh factors target the saved raw Gram
with eigenvalues above1e-12 times the largest retained scale. Report negative
eigenvalues, discarded trace and reconstruction error; the original sampler's
small discarded-innovation error makes this a slightly different covariance
target, not an identical-noise rerun. All results must be finite, with frozen
write-history prediction identity below1e-10. Exact scientific repetition
must reproduce saved numerical arrays. Source hashes, commands, environment,
run status and costs are recorded. No extra scientific branch is authorized.

Main owns the contract, cohort driver, analysis and shared notes; scoped agent
owns frozen_population_replay.py, with only tiny deterministic verification
before this campaign. A separate bounded local-identity check examines Stein
response contractions, but that score estimator is NOT substituted for the
current tangent-response solver. Its potential rank/sample-count noise is a
reason not to add another uncontrolled approximation. New outputs stay under
data/generated/transparent_learning_dynamics_20261007/frozen_quadrature_v1/.

### Fresh-quadrature audit completed: sampling contribution supported, not resolved

Exactly four declared replays completed, using78.44seconds recorded wall time
and429.7MiB largest process RSS. Fresh factors reconstruct saved raw covariance
entries within2.99e-10. One fresh-process repetition matches all91non-timing
arrays exactly; same-primitive tiny replay previously matched every field and
prediction exactly. FROZEN_QUADRATURE_CHECK.md independently recomputes the
saved-batch arithmetic and explicitly distinguishes its coverage from a full
independent scientific rerun.

The lower-layer mean dense errors change from27.33%/31.41% to12.32%/15.19%
on training-training/training-passive blocks. Fresh-minus-source defects are
23.34%/27.47% of dense movement. However the3SE scales.002790/.002714 exceed
the fixed5% thresholds.002179/.001867; the passive halfdifference also
slightly exceeds its threshold. No registered explanation pass is claimed.
All single-source fresh-resolution checks fail. Upper ensemble checks resolve
the fresh integration but have intermediate12–14% corrections; passive
dense discrepancy slightly worsens from12.37% to12.90%.

The new values do not supersede the coupled model's accuracy table: all
coefficient histories, effective forces and reciprocal responses were frozen.
Missing covariance directions are not restored. Source-path uncertainty and
time bias remain separate from conditional fresh-integration uncertainty.
This phase supports sampling as a contributor but does not assign the
remaining mismatch to a faulty causal mechanism. No additional source/seed/
population run was added after the failed precision gates.

STEIN_RESPONSE_IDENTITY_CHECK.md records a bounded exact representation check,
not a new global theorem. A score-based response implementation remains
unselected because rank/sample-count noise would add an uncontrolled axis.
Next useful question: separately controlled quadrature and time integration
for the coupled law, retaining its mechanisms. Current phase is closed and
classified as progress; the original global objective remains open.
