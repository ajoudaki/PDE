# q=2/q=3 closures and their scalar continuations on the two alternating tasks

Completed 2026-09-30. This is the precommitted continuation in
[HIGHER_ORDER_EXPERIMENT_PLAN.md](HIGHER_ORDER_EXPERIMENT_PLAN.md).
Both higher orders were run on both tasks, first assessed against the
unchanged dense references, and only then scalarized. No task, order,
seed, switch, Fourier cutoff, or final time was tuned after observing the
results. These are internally checked numerical results, not promoted
theorems or a population-limit experiment.

**Result:** the same principled terminal scalar construction applies to
q=2 and q=3, and tracks both closures accurately at the primary 0.01-MSE
switch on both tasks. q=2 substantially repairs the previous dense-output
discrepancy and meets the predeclared endpoint criterion on both tasks.
q=3 improves the dense loss curve further but has larger final circle
prediction errors than q=2, missing the predeclared RMS criterion.

## Exact construction and setup

[HIGHER_ORDER_SCALAR.md](HIGHER_ORDER_SCALAR.md) derives the construction
from the manuscript's actual learning-speed moment closure, including the
unit prefix, moving clock, normalization and all dilation couplings. Its
[internal mathematical check](HIGHER_ORDER_SCALAR_CHECK.md) passed.
The complete producer also passed its
[source audit](HIGHER_ORDER_SOURCE_CHECK.md).

At order q, the derivative of the reconstructed middle matrix depends on
the endpoint memory sums with weights 1,3,...,2q-1. Consequently the exact
training residual and each query output have the same response form as
at q=1. At the handoff, freeze the training response matrix, norm-response
vector and query-response functions, then evolve

    residual_dot = -response_matrix @ residual
                   + norm(residual) * norm_response.

The full network before the switch still uses every matched pair of
memory modes; replacing its matrix by the product of the endpoint sums
would be incorrect. Both new closures were trained from initialization,
not constructed by appending modes to a previously trained q=1 model.

The experiment uses n=1024, m=8, two tanh hidden layers, no biases, exact
zero initial readout, and seed 20260920. The saved A and W0 arrays were
verified exactly against the original initializer. The two tasks are:

* Two outliers: angles 15,27,39,51,63,75,165,285 degrees.
* Quadrant: angles 10,20,30,40,50,60,70,80 degrees.

Both have alternating labels +1,-1,+1,-1,+1,-1,+1,-1 in that order.
The exact binary64 inputs are in `circle_task_inputs.json`. Physical
inputs are sqrt(2) times the unit-circle vectors; the implementation
receives already-normalized vectors and does not divide them again.

Each new full closure was independently integrated at steps 1/8 and 1/16
to the original common dense/q1 final time: 244.5 for outliers and 346.375
for quadrant. All new full closures fitted by those times. The previously
checked dense references were reused, including their numerical refinement.
Predictions use the same 8192 midpoint-shifted circle queries.

Every order/task has switches at first coarse MSE crossings 0.1, 0.01
(primary), and 0.001. Refined runs use those identical physical switch
times. The scalar integrator is DOP853 with rtol=1e-10 and atol=1e-12.
Its finite query readout uses the same 32 odd Fourier frequencies as the
q1 campaign, built from 2048 handoff samples without future outputs.

## First comparison: full closure versus dense

The maximum loss error is over all saved common physical times, including
early training. Circle errors compare signed predictions at the final
common time; they are not ground-truth test risks.

| Task | Order | Maximum training-MSE error versus dense | Final circle RMS | Final circle maximum error | Sign disagreement |
|---|---:|---:|---:|---:|---:|
| Outliers | 1, prior reference | 0.229457 | 0.236240 | 0.454632 | 2.515% |
| Outliers | 2 | 0.071120 | 0.029691 | 0.062508 | 0.195% |
| Outliers | 3 | 0.034207 | 0.072136 | 0.147641 | 0.586% |
| Quadrant | 1, prior reference | 0.206613 | 0.381049 | 0.565709 | 1.660% |
| Quadrant | 2 | 0.091964 | 0.041206 | 0.077626 | 0.269% |
| Quadrant | 3 | 0.039564 | 0.052467 | 0.078977 | 0.293% |

The prespecified dense endpoint criterion is RMS <=0.05 and sign
disagreement <=1%. q=2 passes both tasks. q=3 passes the sign criterion
but fails the RMS criterion on both; the quadrant failure is small but
remains a failure. All four full closures fit: their final MSEs are
3.018e-12, 2.409e-13, 6.810e-10 and 1.170e-11 in table order, versus
dense MSEs 9.877e-14 and 4.426e-13 for the respective tasks.

The loss-curve and selected-function comparisons give different rankings.
Increasing q from two to three reduces the maximum loss-curve discrepancy
on both tasks, but increases the final unseen-output RMS discrepancy.
Thus neither successful fitting nor closer loss-curve agreement implies
a closer final function. This is an observed finite-order behavior, not
a theorem of nonmonotonicity for every task or initialization. The remaining
training-loss differences also mean that q=2's endpoint pass must not be
described as uniform high-accuracy tracking of the entire dense trajectory.

## Second comparison: scalar versus its actual higher-order closure

Primary switch: training MSE first reaches 0.01. All RMS and maximum
errors below include the finite Fourier representation used by the actual
729-number evaluator.

| Task | Order | Switch time | Scalar/closure RMS | Scalar/closure maximum | Scalar/dense RMS | Scalar/dense sign disagreement |
|---|---:|---:|---:|---:|---:|---:|
| Outliers | 2 | 155.125 | 0.003195 | 0.013357 | 0.030104 | 0.195% |
| Outliers | 3 | 150.750 | 0.002980 | 0.014424 | 0.072177 | 0.562% |
| Quadrant | 2 | 241.375 | 0.006704 | 0.031080 | 0.044545 | 0.195% |
| Quadrant | 3 | 231.875 | 0.005750 | 0.024063 | 0.050326 | 0.220% |

All four primary scalarizations meet the separate scalar/closure criterion:
RMS <=0.01 and maximum <=0.05. Both q2 scalar models also meet the dense
criterion. Both q3 scalar models still fail its RMS criterion. The latter
errors are primarily present in the full closures before scalarization;
RMS components need not add and can partly cancel.

The maximum scalar-versus-closure training-MSE errors after handoff are
0.00017746, 0.00015661, 0.00017869 and 0.00019815. The respective final
internal scalar MSEs are 6.39e-11, 4.98e-12, 7.04e-9 and 2.50e-10.
These describe the autonomous residual ODE. They must not be confused
with the training MSE of its finite Fourier query function.

At the primary switch, leaving the query function static would give circle
RMS errors 0.07244, 0.06981, 0.07567 and 0.06856 versus the full closure.
The actual scalar continuation improves these by factors 22.7, 23.4, 11.3
and 11.9. The improvement exceeds both the prescribed factor-two control
criterion and numerical sensitivity by a wide margin.

## Freezing error, spatial error, and switch sensitivity

The diagnostic untruncated query observer uses exact handoff coefficients
on the test panel; it is not the exported finite model. It separates the
error of frozen dynamics from the error of representing query functions.

| Task | Order | Primary untruncated freezing RMS | Primary Fourier-only RMS | Fourier function training MSE |
|---|---:|---:|---:|---:|
| Outliers | 2 | 0.001610 | 0.002731 | 6.922e-6 |
| Outliers | 3 | 0.001406 | 0.002551 | 5.933e-6 |
| Quadrant | 2 | 0.003877 | 0.005508 | 4.490e-5 |
| Quadrant | 3 | 0.003106 | 0.004892 | 3.576e-5 |

The finite Fourier function does not meet the 1e-6 training-fit threshold
in any of these primary cases, even though its prediction errors are small
and its internal residual has fitted. All twelve finite Fourier predictors,
including the early and late switches, fail that training-fit threshold.
Exact training-query observers satisfy
their algebraic consistency identity to at most 7.90e-14; the discrepancy
therefore comes from the finite spatial representation, not a missing
term in the residual equation.

All four early 0.1 switches fail scalar/closure fidelity. Their RMS errors
are 0.02240, 0.02410, 0.03455 and 0.02979. Early quadrant internal residuals
also remain above 1e-6 at the observation horizon. All four late 0.001
switches pass scalar/closure fidelity. Their untruncated freezing errors
drop to 0.0001574, 0.0001215, 0.0004169 and 0.0003029, while total finite
model errors remain 0.002764, 0.002632, 0.005485 and 0.004851. Thus later
switching reduces the dynamical error; at the late prescribed switch,
Fourier representation error dominates. All twelve switches and every metric
are preserved in the analysis tables, including these failures.

The primary sufficient Euclidean contraction diagnostics are +0.013706,
-0.032416, +0.026682 and -0.001723 in table order. In particular, q3 does
not satisfy that sufficient margin test at any of the three switches.
Its observed scalar convergence is numerical evidence, not an application
of the Euclidean terminal theorem. Even the positive q2 margins do not
verify the full theorem's state-tube bounds and small-tail inequalities.
No new metric certificate was fitted after seeing these results.

## Numerical and artifact validation

The frozen producer is `higher_order_circle_experiment.py`, SHA256
`1773a2428b83af247c1b7eb360bcbce95f6eb9ef563322160998f3c18cd1a30a`.
It imports only hash-verified helpers from the earlier same-study producer.
The current manuscript SHA256 remains
`fa44deda090a456640b64080767511003dc8bc385790ccc49fd039c931a67605`.

* All 55 tiny checks passed for the final producer. They cover raw versus
  normalized moments, full matrix versus endpoint derivative, noninitial
  query derivatives, q1 parity, initialization and zero-residual stopping.
* Every new coarse/fine gate passed. Maximum full-closure endpoint RMS
  sensitivity was 2.75e-8, common-time MSE sensitivity 7.70e-9, and primary
  scalar endpoint RMS sensitivity 1.12e-7. No 1/32 run was needed.
  Original dense sensitivities were at most 3.77e-9 in endpoint RMS and
  4.37e-9 in training MSE. These are far smaller than the reported errors.
* An independent implementation using materialized B and the manuscript's
  raw moment equations reconstructed all four fine endpoints and all twelve
  fine handoffs. All sixteen state checks passed, including full-circle
  endpoint outputs and raw-moment query velocities. It did not import the
  producer.
* Independent analysis recomputed all metrics and Fourier/observer outputs:
  414 artifact checks passed over 70 hashed files. Stage preservation was
  additionally verified by 49 exact file-hash matches between the closure
  stage and the scalar-stage copies, including every endpoint/handoff and
  the original curve/summary files.
* All four primary handoffs were exported to standalone 729-number models.
  The copied standalone evaluator received only its model, query angles and
  elapsed duration. Its endpoint circle output differed from the campaign
  by at most 9.60e-13; endpoint state difference was at most 7.26e-13.

Recorded numerical component times: full-closure stage 260.358 s, scalar
stage 3.037 s, raw-state check 3.439 s, independent analysis 8.680 s,
standalone exports/checks 1.520 s, and stage preservation 0.056 s, plus
the subsecond tiny checks and source/input copying. This remained well
inside the precommitted 3600-second budget. Producer peak RSS was
108.3 MiB in the full stage and 86.1 MiB in the scalar stage; separate
analysis/checker peak RSS was not recorded. Numerical BLAS work used at
most two threads per process. The training worker was sequential.

## Counts, artifacts and reproducibility

The terminal evaluator uses 17 moving scalars (8 residuals, 8 residual
integrals, one norm integral) and 712 fixed numbers (64 training-response
entries, 8 norm-response entries and 640 Fourier coefficients), for 729
total at either q. The full pre-switch moving counts are 35,841 for q2
and 52,225 for q3, plus the fixed 1,048,576-entry mixer. Dense has
1,051,648 moving parameters in this setup. These are exact representation
counts at one width, not an end-to-end complexity or width-uniform theorem.

All following generated paths are relative to
`data/generated/scalar_terminal_closure_20260930/`:

| Artifact | Path |
|---|---|
| Frozen closure stage, all eight runs | `higher_order_closures_01/` |
| Scalar stage, all orders/tasks/switches and original copies | `higher_order_scalars_01/` |
| Independent metrics, JSON/CSV, plots and full switch report | `higher_order_analysis_01/` |
| Independent raw-state audit and stage-preservation hashes | `higher_order_raw_checks_01/` |
| Final producer tiny checks | `higher_order_checks_02/` |
| Four primary standalone scalar models and checked evaluator | `higher_order_portable_01/` |

Plots: [final circle predictions](../../data/generated/scalar_terminal_closure_20260930/higher_order_analysis_01/final-predictions.png),
[loss trajectories](../../data/generated/scalar_terminal_closure_20260930/higher_order_analysis_01/losses.png),
[every switch and error component](../../data/generated/scalar_terminal_closure_20260930/higher_order_analysis_01/errors-by-switch.png).
The [generated report](../../data/generated/scalar_terminal_closure_20260930/higher_order_analysis_01/REPORT.md)
and [analysis JSON](../../data/generated/scalar_terminal_closure_20260930/higher_order_analysis_01/analysis.json)
retain all comparisons and failure flags.

Reproduce from the repository root using the conda Python executable and
fresh output directories. Run `higher_order_circle_experiment.py --check`
first, then its `--reference .../circle_width1024_02 --output NEW_CLOSURES`
stage, inspect full-closure comparisons, and then its
`--scalar --run NEW_CLOSURES --output NEW_SCALARS` stage. Supply the
remaining budget explicitly. Run `check_higher_order_saved.py --run
NEW_CLOSURES --output NEW_CHECKS`, `analyze_higher_order_circle.py --run
NEW_SCALARS --output NEW_ANALYSIS`, and `export_higher_order_scalar.py
--run NEW_SCALARS --output NEW_EXPORTS` for the independent checks and
standalone models. All scripts are in this study.

No manuscript, maintained book/code, Git index, commit or push was changed
by this continuation.
The conclusion is restricted to one seed, two finite tasks, fixed finite
times and the stated circle grid. Full-width training still produces the
handoff: this does not supply a scalar approximation from initialization
or establish a sublinear-cost approximation of complete dense training.
