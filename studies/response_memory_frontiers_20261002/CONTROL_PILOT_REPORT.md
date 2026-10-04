# Controlled-response-memory pilot: bounded positive result

The frozen pilot passed its stated discriminator on one nonlinear adaptation
problem and one initialization. Orders 3 and 7 accurately predicted full
switched training continuations while their individual credit histories had
substantial projection error. Averaging the control and freezing the tangent
kernel both produced much larger function errors. This supports the practical
mechanism on this instance. It does not establish better intervention decisions
or a useful worst-case numerical certificate.

The candidate, full internally derived theorem and preregistration remain
unchanged in `CONTROL_CANDIDATE.md`, SHA256
`cebe78cac01f339a1abb497982acc4a7ed678cf3ad429022e15c3b9a02acb78d`.
All twelve allowed trajectories completed; aggregate elapsed time was
267.264 seconds, against a 1200-second cap. GPU 0 was released afterward.
No additional training followed the result.

## What was measured

The model has two trainable tanh hidden layers of width 512, canonical
mobilities and Gaussian initialization. It first learned eight correlated
inputs on an old arc, reaching MSE (10^{-3}\) at physical time 54.1747.
Each continuation started from that same physical checkpoint, then trained on
the union of the old and new eight-point lists for physical time 24.
The old/new replay weights had the same exposure on each half-horizon,
with 2, 8 or 32 burst periods per half. Every control switch was explicitly
resolved by the solver.

The main quantity is maximum-over-saved-time RMS prediction discrepancy on
512 passive inputs, relative to the dense continuation under the *same*
control. Saved times include all switches and a common uniform mesh.

| Burst periods per half | Memory (q=3\) | Memory (q=7\) | Checkpoint NTK | Dense averaged control |
|---:|---:|---:|---:|---:|
| 2 | (1.494\times10^{-4}\) | (3.959\times10^{-5}\) | 0.04141 | 0.05207 |
| 8 | (1.227\times10^{-4}\) | (2.303\times10^{-5}\) | 0.04099 | 0.02309 |
| 32 | (1.213\times10^{-4}\) | (1.164\times10^{-5}\) | 0.04078 | 0.005619 |

For the averaged-control comparison, the final analysis uses exact shared
saved times. This is a conservative lower bound on its maximum over the full
union of saved times; it avoids penalizing that control for interpolation
error. In this run it gives the same displayed maxima as the preliminary
interpolated comparison. The averaging baseline is another dense nonlinear
training continuation, not an output moving average.

The average-control errors at 2 and 8 periods exceed the preregistered 0.02
threshold and are much larger than the memory errors. Thus the positive result
is not explained solely by the high-frequency averaging limit. The frozen
kernel is built at the actual trained checkpoint and includes every parameter
block with its canonical mobility. Its piecewise-constant controlled residual
ODE is evaluated by matrix exponentials, so a weakly implemented frozen
baseline does not account for this gap.

![Prediction errors over the controlled continuation](../../data/generated/response_memory_frontiers_20261002/control_pilot_20261002/prediction_errors.png)

## Evidence for the paired-history mechanism

The maximum hidden-activation displacement from the checkpoint is about 0.243
RMS in every continuation, exceeding the frozen 0.10 feature-motion gate.
Credit histories here mean (b_a=u_a r_a\delta_a/\rho_u\), where
\(\rho_u^2=m^{-1}\sum_a(u_ar_a)^2\). The following are their *terminal*
relative (L^2\) projection errors in each model's own clock, not errors
in a post hoc fit to a dense trajectory:

| Periods | Credit error, (q=3\) | Feature error, (q=3\) | Credit error, (q=7\) | Feature error, (q=7\) |
|---:|---:|---:|---:|---:|
| 2 | 0.3296 | 0.02695 | 0.2384 | 0.007476 |
| 8 | 0.3257 | 0.02674 | 0.2318 | 0.006471 |
| 32 | 0.3242 | 0.02655 | 0.2288 | 0.005869 |

These figures support the predicted separation: accurate interaction dynamics
does not require a comparably accurate credit-history reconstruction. They do
*not* show that credit reconstruction gets worse as switching frequency
increases; it decreases slightly here. The zero-backward prefix at a nonzero
readout checkpoint contributes a common initial jump, so the total credit
projection error cannot be attributed entirely to the control switches.

The exact source bound from the accumulated product of history errors is
about 0.043--0.044 for (q=3\) and 0.0066--0.0085 for (q=7\). It is
conservative relative to observed prediction errors and still requires a
stability factor to become a trajectory bound. Nothing in this pilot turns
that source diagnostic or the theorem's large Gronwall constant into a tight
operational retention certificate.

## Numerical checks and validity limits

An algebra check at a nontrivial raw moment state compared the derivative of
the reconstructed hidden matrix with dense controlled gradient flow plus the
derived product defect. Maximum absolute discrepancy was
(4.86\times10^{-17}\). All raw velocities were exactly zero under a
zero drive. These checks exercise the normalization and clock-pausing formulas.

All training used float64 adaptive Heun, maximum step (1/64\), block-RMS
absolute/relative error tolerances (10^{-8}\)/(10^{-6}\), and explicit
event clipping. The reserved twelfth trajectory refined the largest-error
closure, (q=3\) at two periods, with half the maximum step and quarter
tolerances. Its maximum prediction change was (1.53\times10^{-7}\), well
below the frozen 0.005 numerical-sensitivity gate and the displayed closure
error. This is a numerical diagnostic, not a certificate for continuous time.
Only one closure was refined. The dense reference and the (q=7\) runs have
not yet had independent refinement, and a common implementation bug has not
been excluded by independent reproduction.

The preregistration allowed one seed and one task. Consequently PASS means
the stated empirical witness passed; it does not imply universal small-order
accuracy, convergence at arbitrary width, all-time control, or a theorem
about intervention gradients. No scientific setting, threshold or control was
changed after looking at the outcome.

## Practical consequence and cost

An additional recorded observable gives a useful direction for a later
decision test. New-task terminal passive RMSE is approximately 0.02222 for all
three dense continuations. Their maximum old-function drift is different:

| Periods | Maximum old-function RMS drift | New-task terminal RMSE |
|---:|---:|---:|
| 2 | 0.14420 | 0.022226 |
| 8 | 0.14706 | 0.022216 |
| 32 | 0.12473 | 0.022221 |

The whole continuation therefore contains retention information that terminal
new-task loss alone misses. A retention threshold selected after reading this
table would be exploratory. This pilot did not optimize a policy, establish
improved continual-learning performance, or run a held-out policy-ranking test.

At this width and sample count, the main moving arrays require 264,192 scalars
per dense branch, 51,201 at (q=3\), and 116,737 at (q=7\), excluding
64 optional diagnostic scalars in each memory branch. The fixed checkpoint
hidden matrix has another 262,144 scalars shared among branches. Thus (q=3\)
uses about 19.4% and (q=7\) about 44.2% of the dense moving-state count.
These are explicit array counts, not measured peak allocator memory.

This implementation did not accelerate individual trial trajectories. Dense
continuations took 2.6--3.0 seconds; (q=3\) took 23--27 seconds and
(q=7\) took 37--43 seconds. The compressed system still applies the dense
checkpoint matrix, evolves more RHS objects, and uses more adaptive steps
(including error-controlled diagnostic accumulators). The demonstrated benefit
is reduced evolving storage with accurate counterfactual predictions, not lower
runtime. Whether batched trial planning is useful under an actual memory budget
remains to be tested against sequential dense rollouts and a dynamical low-rank
approximation with matched storage.

## Reproduction and next decision

The source is `control_pilot.py`; its exact hash, environment and candidate hash
are saved in the run's `config.json`. `control_analyze_pilot.py` produces the
comparison figure and conservative final reduction. The original frozen
candidate was not rewritten to reflect this result.

```bash
env CUDA_VISIBLE_DEVICES=0 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  /home/amir/miniconda3/bin/python -u \
  studies/response_memory_frontiers_20261002/control_pilot.py \
  --device cuda:0 \
  --output data/generated/response_memory_frontiers_20261002/control_pilot_20261002

/home/amir/miniconda3/bin/python \
  studies/response_memory_frontiers_20261002/control_analyze_pilot.py \
  data/generated/response_memory_frontiers_20261002/control_pilot_20261002
```

Raw predictions, per-run diagnostics, terminal states, resource counts and
failures/status are retained under
`data/generated/response_memory_frontiers_20261002/control_pilot_20261002/`.
`analysis.json` contains the explicit PASS gates; `status.json` contains
the final count, elapsed budget and refinement result; `task_metrics.json`
contains the descriptive retention table.

The next useful action is an independent dense numerical replay and fresh
theorem review, followed, only if separately authorized, by a frozen policy-
ranking test with a new initialization. The theorem's control-uniformity and
this pilot's empirical utility remain separate claims.
