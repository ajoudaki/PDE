# First-thrust result: the ordinary proxy captures the available benefit

The preregistered significance discriminator **failed on the first fixed
seed**, so this witness is stopped. Full-horizon differentiation of the
width-512 dense learner selected a schedule that reduced independent test MSE
by **0.603%**, below the required 5%. A schedule obtained from the ordinary
width-128 dense proxy and applied to the same width-512 learner reduced test
MSE by **0.637%**, recovering 105.6% of the reference benefit. There is no
observed decision-quality advantage that response memory needs to recover.

This is a negative result for the proposed fixed witness, not a no-go theorem
for response-memory sensitivity or curriculum control. It also does not
establish that the proxy is statistically superior: its numerical advantage
is small, and only one initialization was run. The consequential finding is
that the strong ordinary alternative preserves the modest available benefit.

## What was compared

MNIST digits 3 and 8 provide 128 training, 512 validation and 2,048 test images,
with no image shared across splits. Each split is balanced by digit. Images
are average-pooled to 14 by 14 and receive a two-column nuisance strip. In
training source A the strip is exactly balanced within each class; in source
B it identifies the class perfectly. Both sources have 64 images. Validation
and test strips are balanced independently of the class.

Both networks have two tanh hidden layers, Gaussian initialization, zero
readout and the paper's canonical block mobilities. Eight coefficients set
smooth source-weight pulses paired between early and late training windows.
Every schedule preserves integrated source exposure. The objective is final
validation MSE at physical time 80. The forward map is 1,600 fixed Heun steps
of size 0.05, differentiated exactly by checkpointed automatic differentiation
through explicitly written RHS equations. All arithmetic is float64.

For a method's validation gradient `g`, its tested schedule is
`u=-0.25*g/max(abs(g))`. This rule was fixed before any outcome, and no
line search or outer optimization was performed. Both candidate schedules
restart the same width-512 target network from exactly the same initial
weights. Test data do not select the schedules.

| Schedule applied to the width-512 target | Validation MSE | Test MSE | Test accuracy | Relative test-MSE decrease |
|---|---:|---:|---:|---:|
| Equal source mixing | 0.3348878774 | 0.3410251242 | 88.2324% | — |
| Width-512 full-horizon gradient | 0.3330530719 | 0.3389691992 | 88.3301% | 0.6029% |
| Width-128 full-horizon proxy gradient | 0.3329848516 | 0.3388539266 | 88.3789% | 0.6367% |

The standalone proxy's own test MSE, 0.3439840956, is not the primary comparison.
The relevant result is its transferred schedule on the identical target.
All eight gradient signs agree between widths, although the vectors are not
identical (cosine 0.93935). Thus exact gradient-vector fidelity is not necessary
to preserve this decision's benefit. The outcome is compatible with the
ordinary explanation that both randomly initialized learners discover a
similar useful population-level source schedule; this experiment does not
prove a population limit or that explanation's uniqueness.

## Numerical and physical checks

At zero controls, the target's automatic directional derivative along the
unit all-ones direction is `0.00162391983623`. The centered finite difference
at epsilon 0.001 is `0.00162391900044`, giving relative discrepancy
`5.147e-7`, well below the preregistered 2% threshold. This validates one
direction of the implemented discrete gradient, not the continuous-time
gradient or every gradient component.

The target's terminal training MSE is 0.0159229, below 0.02. Its first- and
second-hidden-layer activation RMS movements are 0.44624 and 0.52476, both
above 0.10. The negative screen therefore cannot be attributed to frozen
features, an untrained network, or a failed basic derivative check. Dataset
checks confirm exact split sizes, no repeated image indices across splits,
source A strip-label correlation zero, source B correlation one, and
validation/test correlation zero.

The protocol made step-halving, epsilon-halving, early-window gradient
diagnostics and memory-order work conditional on a consequential difference
between the exact target schedule and the strong proxy. That condition did
not occur. None of those computations was run. In particular, the present
result neither establishes nor excludes an early-to-late sign reversal.
There is no response-memory accuracy result hidden in this report.

## Cost and scope

The width-512 gradient evaluation took 11.14 seconds and peaked at 514.7 MiB
of allocated GPU tensors. The width-128 gradient took 8.24 seconds and peaked
at 105.7 MiB. These are measured standalone computations with Python/kernel
overhead; they are not asymptotic scaling claims or optimized runtime results.
The proxy needs less memory and was already sufficient without receiving
additional search budget. The two intervention reruns and two directional
check reruns took about 2.62 seconds each. Total recorded computation was
29.85 seconds, with process startup and data loading additional, well within
the 30-GPU-minute/45-wall-minute envelope. The GPU process exited normally.

Single-seed sampling uncertainty, the selected image domain, finite horizon,
particular bounded schedule family and its small fixed amplitude limit the
scope. Failure to reach 5% does not show that all possible curricula have
small benefits. Nevertheless the precommitted task offered neither the
required useful effect size nor a failure of the strongest ordinary proxy.
Changing the data geometry, horizon, schedule amplitude or initial-state
problem now would constitute a new decision, not confirmation of this witness.

## Reproduction and evidence

Run from the repository root using the existing environment:

```bash
CUDA_VISIBLE_DEVICES=0 PYTHONDONTWRITEBYTECODE=1 /home/amir/miniconda3/bin/python -u studies/response_memory_delayed_training_credit_20261002/run_screen.py
```

The executed process also had an external 1,500-second timeout. No packages
were installed. Python was 3.10.14, PyTorch 2.9.0+cu130, CUDA runtime 13.0 and
NumPy 1.26.4 on one RTX 3090. Source SHA256 at execution was
`552b8414a77d0641ac7c45a40a8879dfe797788e1f65f9c88ec0e56eaea3ced1`;
protocol SHA256 was
`cf66e2fd1ceffb1f9d572a0a7a63b4812c806b12e9218c3723d0f7a1483e48f3`.
The dataset NPZ SHA256 was
`8562bc988c7834db4d8e9af4f7542118da16f7ddbf20b25ebf3a41f798609d8c`.
Archive hashes are recorded separately. The producer has not been changed
after this execution.

Study-owned evidence is under
`data/generated/response_memory_delayed_training_credit_20261002/`:

- `first_discriminator.json`: complete gradients, controls, metrics and stop decision.
- `directional_check.json`: analytic and finite-difference values and perturbation results.
- `*_predictions.npz`: raw train/validation/test predictions for the reference, proxy and both interventions.
- `dataset.npz`, `dataset_provenance.json`: exact image indices, strips, source labels, inputs and archive hashes.
- `environment.json`, `run.log`: software, device, source/protocol hashes and chronological outputs.

The author stops this witness without running q=1, q=2, q=4, the tangent
ablation or additional seeds. No mathematical statement has been promoted,
and no broad research goal is marked complete.
