# Independent promotion selection: circle comparison and computational scope

Date: 2026-09-16. Selector: `/root/select_b`, a fresh scoped context, neither an
author nor an assembler of this study. This is workflow Part 2, step 1: a
relevance/placement decision, not an adversarial promotion review or approval.
The selector wrote only this report and its generated check record. No established
file, candidate implementation, or Git state was changed.

## Decision

**Accept a narrowed comparison-method package for assembly.** Its distinct value
is a reproducible comparison of actual finite-network and closure predictions
and hidden activation geometry on identical ordered inputs. Keep it as a small
measurement/analysis layer around existing dynamics. Do not copy the study's
campaign-wrapper chain into the library.

**Keep the varying-order circle GPU closure as a core computational target,
separate from the comparison layer.** Within this selector's permitted source
scope, however, no such GPU closure implementation exists: every study
`*CLOSURE.py` delegates evolution to maintained NumPy `pde.observable_solver`.
The Torch/CUDA sources implement actual dense finite networks. Consequently this
report cannot select, reject, or certify a GPU closure implementation from a
different originating study. A fresh selector must inspect that source under
its own boundary. This is a missing-input/placement limitation, not a judgment
that the circle GPU solver is optional or scientifically unimportant.

**Hold numerical example claims until fresh maintained reproduction.** A bounded
T=40 representative circle comparison is viable in principle; the complete
thirty-degree configuration menu below is the best existing single example
because it includes order-5 quadrature controls and unfavorable order trends.
Historical outputs establish neither current reproducibility nor promotion
readiness. No dynamics were rerun by this selector. Do not promote historical
speed ratios, ideal-closure accuracy, monotone order convergence, generalization,
or long-time settling.

## Inputs and actual read coverage

Allowed scientific inputs were this study and its generated namespace, plus
established `docs/` and `code/`. No other study contents, history, chat-derived
research, or reviewer verdicts were consulted. The supervisor's messages about
available Python/CUDA environments and another selector's source ownership were
coordination only, not scientific evidence.

Read completely, repairing truncated initial combined reads:

- `AGENTS.md`, both parts of `RESEARCH_WORKFLOW.md`, `docs/README.md`,
  `docs/NOTATION.md`, `code/README.md`, and this study's `README.md`.
- Required research-state skill `/etc/codex/skills/investigate-conjectures/SKILL.md`
  and its `references/evidence-ledger.md`.
- `WIDE_GPU_20260914_PLAN.md`, `WIDE_GPU_20260914_REPORT.md`,
  `GRAM_20260914_PLAN.md`, `GRAM_20260914_REPORT.md`,
  `ARC30_20260914_PLAN.md`, `ARC30_20260914_REPORT.md`,
  `LONG_20260914_PLAN.md`, `LONG_20260914_REPORT.md`, and
  `LONG_20260914_SANITY_SCOPE.md`.
- `WIDE_GPU_20260914_NETWORK.py`, `WIDE_GPU_20260914_CLOSURE.py`,
  `WIDE_GPU_20260914_ANALYSIS.py`, `GRAM_20260914_NETWORK.py`,
  `GRAM_20260914_CLOSURE.py`, `GRAM_20260914_ANALYSIS.py`,
  `ARC30_20260914_PREPARE.py`, `ARC30_20260914_NETWORK.py`, and
  `ARC30_20260914_CLOSURE.py`.
- Maintained `code/pde/finite_network.py`, `code/pde/observable_solver.py`,
  `code/pde/observable_initialization.py`, and
  `code/scripts/validate_observable_horizon.py`.

Established theorem placement was checked in `docs/global_nonlinear.md`, lines
11441–11525 (C-H1 model/statement), 12084–12160 (C-H2 statement and dictionary
opening), 12555–12625 (C-H3 statement and family opening), 13982–14060 (C-H4
family/target), 15553–15736 (complete D.5 implementation/storage/validation), and
21314–21430 (C.5 model and beginning of matched-loss theorem). The rest of that
chapter, including the dependency proof bodies, was not reread. This is not a
fresh proof audit of established C-H1–4 or C.5.

All study Python/Markdown sources were searched for loss-matching and relevant
timing, memory, checkpoint and GPU terms. Search excerpts from unread scripts
are locators, not full implementation review. LONG producers/analyzers, ARC30
analysis/check/plot scripts, other plotters/verifiers, the relocation archive,
and unlisted maintained modules/tests were not read completely. Their reported
scientific results below remain attributed to the read reports, not independently
reproved or reproduced here.

The entire `WIDE_GPU_20260914_INPUTS.json` was loaded by its prescribed reader;
all eight literal arrays, hashes, times, shapes and laws passed validation. This
was programmatic array coverage, not a manual reading of every hexadecimal
literal. Three retained records were read completely:
`WIDE_GPU_20260914_202109Z/network/arcs_n8192_s11/record.json`,
`GRAM_20260914_v1/network/arcs_n8192_s11/record.json`, and
`GRAM_20260914_v1/closure/arcs_N5/record.json`. Four named historical run
directories were inventoried for existence only. No historical trajectories
were loaded or used to claim independent reproduction.

The starting shared HEAD was `04b61a12795734cbfc93830bf0a164bab7d101c4`.
The checkout had unrelated tracked modifications and untracked studies;
these were observed only as Git safety metadata and preserved.

## Distinct value and overlap with established material

| Component | Already established | Useful addition and decision |
|---|---|---|
| Closure model and initialization | C-H1 information, C-H2 closure, C-H3 numerical limits, C-H4 fixed-family T=40 extension; NumPy initializer, solver, transpose action, paired observations and restart | Reuse. No new closure theorem, dictionary, ridge, or duplicate CPU solver belongs in B. |
| Passive predictions | Maintained `predict` evaluates supplied circle inputs; H4 archives training and circle predictions | Add explicit shared sample identifiers/order and finite-network-versus-closure discrepancies, preserving per-input predictions. |
| Hidden geometry | Maintained finite `forward` returns hidden arrays; closure paired observations expose weighted initial/current fields; finite jets already have local Gram coefficients | Add same-time input-index Grams for both layers, their increments, weighted matrix errors and frozen-initial-Gram baseline across whole trajectories. This is not another jet API. |
| Matched training loss | Established C.5 has a proved early-time comparison for a different prescribed design and comparator | No general numerical checkpoint selector exists in the read comparison sources. Accept a small explicit selector/analysis contract for assembly, not a new theorem or an already demonstrated empirical result. |
| Time/memory | H4 already separates initialization, evolution, observation, checkpoints/restart, retained bytes, structural workspace and RSS | Extend these conventions to both measured systems; no second general campaign framework is needed. Historical GPU and closure measurements are not directly equivalent. |
| Circle GPU closure | Not present in the allowed study; NumPy circle engine is established | Core computational target needs its own originating-source selection and CPU-oracle review. No arbitrary-order GPU claim follows from the finite-network CUDA runner. |

The passive circle in this study has no independently specified target labels.
Its predictions are validation of agreement between computations, not empirical
test risk, classification accuracy, or generalization. Mean training loss is
the mean of individual seed losses, not loss recomputed from the mean predictor.
The frozen-Gram baseline predicts a static representation only; it is not a
trained frozen-feature or NTK loss comparison.

## Required reusable contract

Preserve the bias-free two-hidden-layer tanh architecture, independent stored
Gaussian variances `(1,1/n,1/n²)`, output `c.T @ h2 / n`, mobilities `(n,1,n)`,
and residual `f-y`. All blocks train. Loss is the unhalved weighted mean square
and time is physical GF time. Heun is a numerical approximation of that vector
field; it is neither exact flow nor an assertion about raw GD. The finite
random initial readout remains random even though the limiting closure readout
starts at zero.

Inputs in closure/study code are rows of `u=x/sqrt(2)`; the maintained finite
API consumes columns of `x` and divides by `sqrt(d)` itself. The adapter must
prevent double normalization and preserve correlations without whitening.
Keep exact working inputs, labels, training probabilities, passive input order,
seed, Gaussian generator/draw order, float64 source draws and subsequent dtype
conversion. Using the same seed alone is insufficient to promise bitwise
initialization identity between separately coded formulas.

For an evaluation panel of K inputs, a finite layer uses `H.T @ H / n`; its
closure counterpart uses `H.T @ diag(p_layer) @ H`. Training/input weights are
not factors inside these entries. They enter a panel metric such as
`sqrt(sum_ab q[a]*q[b]*(G[a,b]-G_ref[a,b])**2))`. Preserve full training-plus-circle
matrices or explicitly declare a reduced panel; do not silently discard cross
blocks. For the source example the order is 16 training inputs followed by 128
passive directions, without deduplication.

`G(t)-G(0)` subtracts each method's own initialization. It is not the Gram of
`H(t)-H(0)`, and does not recover general cross-time feature products. Keep
absolute error, per-sample prediction differences, seed/width variation and
small-denominator handling explicit. Relative errors are undefined near zero,
not zero. A finite saved-time maximum is not a continuous-time supremum.

Same-time comparisons must use a shared declared physical schedule. Off-mesh
source observations interpolate adjacent *states* and then reevaluate nonlinear
fields; the interpolant never feeds evolution. Linear interpolation of saved
Grams or predictions is a different postprocessing convention.

For matched-loss comparison, predeclare thresholds using training information
only and retain the selected times and actual achieved losses. The smallest
safe default is the first saved checkpoint at or below each threshold, with
its preceding bracket and a disclosed loss mismatch. Thresholds not attained,
invalid/nonfinite records, plateaus, nonmonotone sampled losses and incomplete
runs need explicit statuses; no nearest future endpoint or extrapolation may be
substituted. If interpolation is offered, name exactly what is interpolated and
retain its bracket/error limitations. Specify whether matching is per seed or
against an averaged loss curve; these operations do not commute. Never use
passive predictions or Gram agreement to choose a favorable checkpoint.

Matched training loss is not matched prediction/Gram accuracy. Neither loss
matching nor fixed-horizon completion supports a cost-to-accuracy claim without
a separately specified accuracy target and its applicable controls.

## Timing, memory and maintenance cost

The historical GPU run records one worker wall duration and peak Torch allocated
memory. Its wall timer starts before setup/initialization and includes observations,
serialization and checking. The closure additionally records initialization,
evolution and observation phases plus process RSS. For example, the retained
arcs/N5 Gram closure record reports about 21.78 seconds total, while the inspected
width8192 seed11 GPU Gram record reports about 36.61 seconds. Their ratio is not
a matched-accuracy speedup or a matched phase benchmark.

A reusable measurement recipe must declare initialization/preprocessing and
CPU-to-device transfer boundaries, synchronize CUDA at timed boundaries, separate
evolution, observation, output/checkpoint work and end-to-end cost, and record
hardware, versions, thread settings, dtype and TF32 policy. Include failure and
timeout costs rather than dropping them. CPU time and wall time are distinct.
GPU allocated/reserved memory, host process RSS, retained dynamic/frozen arrays,
temporary workspace and output storage have different meanings and must retain
their labels. Do not compare GPU allocator bytes to CPU RSS as a total-memory
ratio. Fixed state size does not imply fixed archive size when every Gram is saved.

Maintenance burden is modest for pure array metrics and observation adapters;
it becomes large if the WIDE→GRAM→ARC30→LONG monkey-patching, fixed historical
paths, host-specific Python executables, repeated manifests, and superseded
campaign stops are promoted. Extract the contracts, not that orchestration.
Torch should stay optional and absent from ordinary NumPy package imports.

Smallest placement: a compact NumPy comparison module (for example
`code/pde/comparison.py`) with tests and a short guide section; use existing
finite `forward` and closure observation/state primitives. A small public
closure Gram observer may fit in `observable_solver.py` if that avoids relying
on private `_fields`; it must retain backend/numerical scope. A maintained
producer/analyzer and one frozen JSON example plan belong under `code/scripts/`
and `code/validation/`. Extend the existing implementation discussion near
C.4.7.10 D.5 only with a short empirical-method note if needed; do not add a new
theory chapter or duplicate C-H1–4.

The independently selected circle GPU engine should be a separate optional
backend module around the established initialized state, with public conversions,
observations and restart conventions if those pass its own review. Share only
scientifically neutral infrastructure such as phase timers, array validation and
serialization schemas when semantics actually agree. Different-dimensional
solver derivations cannot be shared merely because both use Torch.

## Circle order scope and deterministic checks

Here the task's order `p` corresponds to maintained hierarchy order `N`, not a
population/input probability. The maintained dictionary accepts positive integer
orders subject to explicit feature, DAG, prefix, integration, work and memory
allowances. It has no promise that every accepted order is practically affordable.
When the exhaustive word prefix introduces additional actions, initialization
switches to the complete Gaussian compiler. Therefore “supports arbitrary order”
would conceal a material implementation and resource boundary.

This selector executed the existing deterministic Gram fixture and complete
literal-input decoder, then initialized only orders 1,3,5 at Q=1024, P=512.
All checks passed. Dimensions were `(5,3)`, `(35,10)`, `(128,21)`; N=5 retains
tail codes 4 and 5, and all three used the fast core. Ridges were exactly the
prescribed float64 evaluations of `1/[1024(N+1)^2]`; no modes were deleted.
The observer fixture checks explicit weighted entries, population permutation,
PSD, diagonal/RMS identity, blocked field reconstruction and no state mutation.
Evidence is [deterministic_checks.json](../../data/generated/wide_network_closure_comparison/PROMOTION_SELECTION_20260916_v1/deterministic_checks.json).

These checks establish neither trajectories nor GPU equivalence. A GPU candidate
must separately preserve the complete initializer output, dictionary including
redundancies, ridge/normalization, fixed marks, both actual action directions,
Heun clock, passive observations and complete own-state restart. CPU comparison
must cover all selected orders 1,3,5, nonuniform weights/nonorthogonal inputs,
nonzero readout and middle updates, observations, several steps and restart.
Larger claimed ranges require their own inspection and checks. This report
supplies no arbitrary-order GPU support assertion.

## Representative empirical recipe and acceptance limits

The smallest existing single-data campaign with relevant N5 controls is the
ARC30 T=40 menu: eight finite networks and eight closures. Preserve its exact
16 equal-weight inputs `z_j=(2j-7)/7*tan(pi/12)`, stereographic map and quarter
turn, eight +1 then eight -1 labels, original 128-direction panel and 206 saved
times. It is linearly separable and outside the proved H4 supported neighborhood.

Finite primaries use widths 2048/8192, seeds 11/29/47, float32, step .01;
controls use width8192 seed11 step .005 and width2048 seed11 float64 step .01.
Preserve matched source draws, disabled TF32/reduced accumulation, all three
trained blocks, and float64 Gram accumulation. Closure primaries are N=1,3,5,
Q/P=1024/512, step .005. Preserve N3's separate doubled-Q/P and half-step
controls, N5 Q/P=2048/1024 and 4096/2048 refinements, and the finest N5 half-step.
No additional seeds, orders, quadrature search or T=640 continuation is needed.

Use the original bounded envelope: 600 seconds per worker, 2400 global wall
seconds, at most 2400 summed worker seconds per family, 18 GiB GPU allocated
per worker, one worker per GPU, at most four network CPU threads and one closure
numerical thread, and 4 GiB output. Freeze maintained plan and sources first;
run into a fresh standalone-edition `data/established/<run>/`, recording producer
and analysis commands, input/source/output hashes, completion and stopped runs.
This is a proposed bounded reproduction recipe, not execution authorization
created by this selection report.

Before promotion the maintained input producer must regenerate panel/time/data
from retained source/configuration without reading old archives. Current ARC30
preparation obtains panel/times from the previous GRAM run, and network checks
consult previous initialization records. Those are valid study provenance but
not acceptable maintained runtime dependencies. Preserve literal configuration
or executable construction and independently check the resulting values. The
maintained analyzer must likewise operate without history, prior verdicts,
study imports, or prior analyzed arrays.

The supervisor first reported CUDA unavailable in the default environment, then
reported successful device access with `/home/amir/miniconda3/bin/python` and
two RTX3090 cards under the permitted execution route. That resolves a potential
environment obstacle in coordination; this selector did not independently run
a CUDA check. The historical GPU recipe is therefore eligible for attempted
bounded reproduction, not already reproduced. A smaller CPU example can validate
operation, but changed width/dtype is a different instance and cannot inherit
the historical wide-network agreement or timing numbers.

Retain full adverse outcomes. The source ARC30 report says finer N5 training
Gram errors are about .01924/.01952, while the relevant last quadrature comparison
still exceeds .002 for both Grams. Higher order improves some observables and
worsens others. The earlier narrow-arc monotonic trend is not a general order
claim. N3 controls do not bound N5; even N5 refinement differences are diagnostics,
not certified true errors. Reproducing unresolved diagnostics is a valid empirical
example if its wording remains unresolved, but it cannot establish resolved
ideal-closure accuracy. Report every frozen run, seed, width, order and control.

The T=640 report remains study evidence only: the user reduced its intended stop,
the strict settling test failed, and feature Grams still drifted. Neither the
long continuation machinery nor any equilibrium assertion is selected. A radial
viewer adds no necessary scientific capability and is deferred. No new research
campaign is recommended to rescue a stronger promotion claim.

## Remaining promotion gates

Assembly must supply the actual compact API, supported ranges, tests, complete
dependencies and archive-independent recipe. New matched-loss and timing
contracts require deterministic adversarial cases, not claims of existing source
coverage. Empirical conclusions require fresh producer-and-analyzer reproduction.
Two fresh complete independent scientific reviews and a separate assembled-edition
integration review remain required. Final concrete user approval follows those
gates; this selection is not permission to edit established book/code.
