# J2 coverage inventory and representative circle-task screen

2026-09-27. The user explicitly requests testing the remaining toy circle
tasks, preferably with scalarization depth J2, to locate remaining failures
or low-training-loss/high-circle-error cases. This continues the same study.
Before any new training, the user further directed efficiency, no nearly
duplicate/rotated tasks, and no rabbit holes after failure. The executed
screen is therefore the representative subset below, not all17 tasks.

## Frozen scope and controls

Use the exact name/configuration union of `circle_tasks.TASKS` and
`geometry_tasks.TASKS`:17 distinct tasks. Reuse the three completed J2
MSE0.001 scalar/control comparisons from `selective_tighter_20260927`.
Attempt six new representatives: pair_cos3, near_pair_sin9,
cluster_triple_cos9, quartet_mixed, broad_ridge6, alternating3, in that order.
They distinguish moderately separated opposite labels, closely separated
opposite labels, a sharp three-point cluster, four irregular constraints,
six smooth constraints, and six alternating constraints. The first two
change separation by a factor of three, not merely rotation. The existing
three cases cover smooth labels and spread-out mixed triples.

The other eight untested J2/MSE0.001 tasks remain explicitly untested:
pair_cos1, triple_cos3, triple_mixed, quartet_broad, sharp_ridge8,
alternating5, multiscale12, alternating9. Do not describe this screen as
complete17-task coverage. Do not add higher-sample cases after a size failure.
No task, angle or label is changed after seeing outcomes.

Keep tanh, k4, memory P1, J2, zero missing-moment boundary, protected essential
feedback, dependency_depth0, canonical scaling, seed1 and n1024 initial
contractions/reference width. The stopping target is core training MSE0.001
(RMSE approximately0.03162). Include64 passive circle probes and passive
copies of every training input. Runtime scalar states must remain aggregate
contractions and the clock; no population/density/dictionary substitute.

Primary metric: raw circle RMS against the matched k4/P1 block population
closure. Also report scalar–Gaussian and block–Gaussian RMS. Both controls
use the same task and target. Resume verified matching checkpoints where
available; otherwise initialize/run the unchanged reference equations.
Reuse completed scalar comparisons without rerunning them. A previous
one-query template may be reused only when its exact scientific configuration
matches; a checkpoint without the full requested query panel is not silently
treated as a complete state for this experiment.

## Screens and numerical checks

Distinguish fitted comparisons, partial training, and inability to construct
or evaluate an ODE within the resource cap. A fitted Gaussian circle
discrepancy<=0.1 is a coarse-accuracy case; >0.3 is a high-error case;
intermediate errors remain visible. The main question is coverage, so no
selected case is omitted from the final table because it fails to fit or compile.
These screens do not establish a general convergence or impossibility claim.
Report core/passive training losses and maximum same-input disagreement;
the existing0.05 inconsistency flag stays fixed.

Preserve float64 RK45, scalar rtol1e-5/atol1e-7, maximum scaled RMS over
the shared core, each passive block and clock; reference solvers unchanged.
Check exact initialization/checkpoint provenance, finite values, independent
decoding of saved states, and passive independence. Compare64/32angle RMS;
a change>0.001 is a quadrature flag, not an invitation to silently discard
the result. No extra seed, order, model change or numerical rerun.

Exact computational shortcuts may reuse query-independent initial tree
messages and evaluate the common training RHS once rather than once per
passive query. They must preserve the chosen contractions, coefficients,
clipping/penalty rule and vector field, with checks against the previous
implementation and saved initial states before training. They are not a
new scientific approximation. Frozen earlier implementations remain intact.

## Budgets and complete accounting

Each new scalar task: hard compilation ceiling60seconds including constructor,
at most100000 template contractions and1000000 retained terms; initialization
at most90seconds; training at most45seconds and physical time3000. Retain
the last accepted state on timeout. Before initialization/evolution, record
the full query-panel size and reject >2million evolving scalars or estimated
peak evaluation workspace>1GiB. Report such tasks as resource-limited, not
as accurate, divergent, or trained. Do not shrink the task or query panel.

At most six new scalar trainings and twelve selected reference evaluations,
each reference with45seconds additional training. BLAS1; at most one scalar
and one reference job concurrently. Scalar training<=270seconds, reference
training<=180seconds, campaign wall ceiling12minutes from first execution.
All selected task names receive a result/status record, including any budget skip.
No repeated stopped run or further order sweep is authorized by this protocol.

New namespace:
`data/generated/structured_full_rank_scalar_20260926/all_tasks_j2_20260927/`.
Root owns protocol, exact RHS shortcut, synthesis and README. Scalar runner
owns exact initializer shortcut and new scalar driver/records. Reference
runner owns control inventory/driver/records. Independent checker owns
coverage and raw-result audits. Sources stay within this study; no Git writes
or maintained model/API changes. Stop after this screen and its read-only audits.
