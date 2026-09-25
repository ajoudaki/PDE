# Scalar-only aggregate experiment: implementation works, full-path accuracy fails

2026-09-25. Continuation explicitly authorized by the user. All eight
predeclared configurations and 64 primary integrations completed. The proposed
order-4 scalar closure fails the frozen practical-accuracy criteria on every
configuration through physical time 128, despite passing numerical refinement
gates. This is adverse evidence for this particular terminal-derivative closure,
not an impossibility result for scalar aggregation in general.

## What was actually implemented

[SCALAR_AGGREGATE_CANDIDATE_THEORY.md](SCALAR_AGGREGATE_CANDIDATE_THEORY.md)
derives the observable-generator hierarchy directly from canonical dense
gradient flow. For g_a=B grad f_a, D_a=g_a dot grad, define
Theta_ab=D_b f_a, C_abc=D_c Theta_ab, and Q_abcd=D_d C_abc.
The implemented order-4 system is

    f'     = -(2/M) Theta (f-y),
    Theta' = -(2/M) C contracted with (f-y),
    C'     = -(2/M) Q contracted with (f-y),
    Q'     = 0.

The tensor derivative indices are ordered, including the derivative of the
sample-dependent vector field itself. All coefficients are computed once
from the original initialization by analytic bivariate differentiation.
No coefficient is fitted to a dense training trajectory. Order 2 freezes
Theta (the frozen-kernel control); order 3 freezes C; order 4 freezes Q.

This is a concrete scalar-only approximation to original dense dynamics.
It is not an exact algebraic collapse of the existing finite-P Legendre
population model. Its new approximation is freezing the highest retained
generator derivative. It inherits no history-covariance approximation theorem.

The reduced RHS uses only sample-indexed scalar tensors and labels. It does
not store or reconstruct neuron populations, parameters, initialized dense
matrices, or quadrature particles. Unit tests disable the neural field routines
while evaluating the reduced RHS and verify its storage contract. One-time
initialization does temporarily use the actual initialized dense network;
that cost is included separately below.

## Model, cases and stopping rule

The [protocol](SCALAR_AGGREGATE_PROTOCOL.md) was frozen before the pilot and
research trajectories. Three tanh hidden layers, all blocks trained, Gaussian
standard deviations (1,1/sqrt(n),1/sqrt(n),1/n), output c^T h3/n,
unhalved MSE and mobilities (n,1,1,n). Circle input rows are already x/sqrt(2).
Draw order is w,W2,W3,c using NumPy default_rng.

Two literal cases from this study's deep_circle_cases.json were fixed:

- equal_mixed_odd: four quotient inputs at 0,45,90,135 degrees, labels +,+,-,+.
- quadrant_alternating: eight inputs at 10,20,...,80 degrees, alternating labels.

Widths 128 and 256, seeds 20260920 and 20260927 give eight configurations.
Each pairs a fresh dense reference with all three scalar orders, each at
rtol 1e-7 and 1e-9 (atol=rtol/100), DOP853, max_step 2 and T=128.
All comparisons use identical physical times: 262 fixed sample times on the
full horizon. This is a finite-width, training-output comparison. It does
not test unseen inputs or generalization, population convergence or width4096.

Primary prediction error is max over saved times of RMS across training
samples of the scalar-minus-dense predictions. The loss metric is max absolute
MSE difference over those times. These are sampled-time maxima, not rigorous
continuous-time supremum bounds. Practical agreement required prediction
error <=0.1 and loss error <=0.05; error >0.2 or loss difference >0.1 is adverse.
All listed full-horizon results satisfy their separate numerical gates.

## Full-horizon results

| Case | Width | Seed | Frozen-kernel prediction error | Order-3 prediction error | Order-4 prediction error | Order-4 loss error | Order-4 verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| Four-input mixed | 128 | 20260920 | 0.876432 | 0.877606 | 0.692114 | 0.515917 | Adverse |
| Four-input mixed | 128 | 20260927 | 0.848394 | 0.848872 | 0.571352 | 0.410711 | Adverse |
| Four-input mixed | 256 | 20260920 | 0.841025 | 0.840791 | 0.414292 | 0.300888 | Adverse |
| Four-input mixed | 256 | 20260927 | 0.866724 | 0.867158 | 0.828069 | 0.718088 | Adverse |
| Eight-input alternating | 128 | 20260920 | 0.928965 | 0.928525 | 0.895164 | 0.883457 | Adverse |
| Eight-input alternating | 128 | 20260927 | 0.788949 | 0.789043 | 0.735479 | 0.762677 | Adverse |
| Eight-input alternating | 256 | 20260920 | 0.861542 | 0.861542 | 0.859377 | 0.860134 | Adverse |
| Eight-input alternating | 256 | 20260927 | 0.765838 | 0.765672 | 0.861704 | 0.839344 | Adverse |

The JSON/CSV produced by analyze_scalar_aggregate.py retain full precision;
the table above is rounded for reading. The four-input n256 seed20260920
cell improves by more than a factor two over the frozen kernel, but its
absolute error remains far above the practical threshold. That one relative
improvement is not presented as an accurate approximation.

## Where agreement breaks down

Through T=1, maximum order-4 prediction error is below 0.0002 in all eight
configurations. On the four-input cases it already reaches 0.387--0.512 by
T=8, and its first sampled crossing of error 0.1 occurs at t=5 or 5.5.
The alternating cases stay within 0.0054 through T=8, but reach 0.054--0.071
by T=32 and 0.735--0.895 through T=128. Their first sampled error-0.1
crossings are t=35.5--38. These are descriptive results at predeclared prefixes,
not a revised success criterion or a claim about exact crossing times.

Dense hidden features move substantially: the maximum sampled RMS changes
across the configurations range from 0.324 to 0.635 in layer 1, 0.375 to 0.709
in layer 2, and 0.476 to 0.607 in layer 3. Every configuration meets the
predeclared dense-motion and frozen-kernel-disagreement gate. The failure is
therefore observed through nonlinear feature learning, not just at a nearly
frozen initial network.

The order-4 learning kernel loses positive semidefiniteness in six of eight
configurations; its smallest sampled eigenvalue reaches about -0.746.
Loss increases at some sampled intervals in five configurations. No clipping,
PSD repair or fitted damping was applied. Those diagnostics are consistent
with a terminal derivative law that does not preserve the evolving physical
kernel constraints. They do not prove that indefiniteness is the sole cause:
the two cases whose reduced kernel stays positive also fail path accuracy.

Endpoint fitting alone would hide a major part of this failure. On all four
mixed-input cases, both dense and order-4 systems reach very small training
loss by T=128, despite maximum trajectory errors of 0.414--0.828. On the
alternating cases, final dense loss is approximately 0.0043,0.0948,0.0288,0.2802
in table order, while order 4 ends near 0.888,0.857,0.877,0.898. The same-time
output and loss curves, rather than matched fitted endpoints, decide this test.

## Scalar counts and measured cost

| Samples M | Evolving order-4 scalars | Fixed Q entries | Logical aggregate total | Initial-state copy + labels |
|---:|---:|---:|---:|---:|
| 4 | 84 | 256 | 340 | 88 |
| 8 | 584 | 4096 | 4680 | 592 |

The implementation additionally retains the small initial scalar vector and
labels; the solver uses its own stages and saved observations. Counts 340/4680
do not mean that those are the entire process allocations. They do establish
that the evolved model and its fixed terminal coefficients are independent of
neuron width. For comparison, dense moving parameter counts are 33152 at n128
and 131840 at n256. Initializer work still scales with the dense network.

Across these runs, coefficient initialization takes 0.029--0.285 seconds;
fine order-4 integration plus sampled observations takes 0.082--0.121 seconds.
The corresponding fine dense runs take 0.974--9.123 seconds. These particular
implementations are faster in the reduced representation, but the scientific
approximation fails; this is not an accuracy-matched speedup claim.

The full 64-run primary campaign takes 66.565 measured wall seconds including
initialization, integration, observations and serialization (final log clock;
campaign.json records 66.561 seconds immediately before final serialization).
Integration plus
observations totals 62.363 seconds, and initializers total 0.996 seconds.
The recorded process high-water RSS reaches 213544960 bytes (about 204 MiB).
This is a cumulative process high-water mark, not per-model isolated peak
memory. Execution uses one CPU worker and one BLAS thread, float64; no CUDA
device is available. Python is /home/amir/miniconda3/bin/python, version 3.10.14;
NumPy 1.26.4 and SciPy versions are retained in each configuration receipt.

## Verification, branches and claim status

- Seven engine unit tests pass, including finite-difference derivatives and a
  scalar-runtime test with neural evaluation deliberately disabled.
- The independent algebra checker passes 82 checks against a separately
  written Torch/autograd oracle at both two and three hidden layers.
  Largest direct discrepancy is 2.00e-15; directional finite differences agree
  to 8.78e-9. The moving-direction contribution and noncommuting derivative
  indices are tested on nondegenerate examples.
- The independent saved-run audit passes 2294 checks over 64 trajectories,
  16768 observations and 320 saved checkpoints. It reconstructs dense
  predictions, kernels and feature movements using the older independently
  checked Torch engine, and rescored scalar losses, errors and numerical gates.
  Its maximum checked discrepancy is 4.27e-14.
- All 24 scalar/dense comparisons pass the prescribed coarse/fine gates.
  No conditional numerical refinement is triggered. The largest relevant
  order-4 dense prediction sensitivity is 0.000241, far below the observed
  0.414--0.895 discrepancies. These refinement sensitivities are diagnostics,
  not rigorous error bounds.
- A fresh first-configuration initializer and fine order-4 repetition reproduce
  all saved scalar coefficients and scientific arrays bit-for-bit. Restarting
  from its own saved scalar state at t=1 changes sampled predictions by at
  most 4.63e-8 RMS and loss by at most 1.26e-10.
- Every dense configuration meets the nonlinear motion/control gate, so the
  conditional T=512 extension is not triggered. The bounded campaign is done;
  no post-result model tuning or additional approximation was run.

Exact algebra and implementation consistency are internally checked within
the recorded scope. Practical full-horizon accuracy is rejected for this
candidate on the eight finite-width tests. Existence of another effective
scalar closure, higher-order convergence, broader tasks, unseen inputs, and
population-limit identification remain open. These are study results only;
no maintained-source change, promotion or Git-index write occurred.

## Artifacts and reproduction

Source: scalar_aggregate_engine.py, test_scalar_aggregate_engine.py,
scalar_aggregate_run.py, repeat_scalar_aggregate.py, analyze_scalar_aggregate.py
and check_scalar_aggregate.py. The complete checker report is
[SCALAR_AGGREGATE_CHECK.md](SCALAR_AGGREGATE_CHECK.md).

Generated directories, all under data/generated/neural_response_memory_20260922:

- scalar_aggregate_pilot01: bounded n32 feasibility pilot, with its original
  runner hash before primary reporting fixes.
- scalar_aggregate_primary01: all new initializers, trajectories, checkpoints,
  source snapshots, configuration receipts, numerical comparisons and summaries.
- scalar_aggregate_reproduction01: independent repetition, own-state restart
  and frozen-branch decisions.
- scalar_aggregate_analysis01: tables, full-precision metrics, PNG/PDF figures.
- scalar_aggregate_tests01 and scalar_aggregate_audit01: deterministic test
  receipts, independent derivative and saved-output audit records.

Direct views: [representative curves](../../data/generated/neural_response_memory_20260922/scalar_aggregate_analysis01/scalar_aggregate_main.png),
[all eight configurations](../../data/generated/neural_response_memory_20260922/scalar_aggregate_analysis01/scalar_aggregate_all_eight.png),
[full-precision table](../../data/generated/neural_response_memory_20260922/scalar_aggregate_analysis01/summary.csv),
and [prefix errors](../../data/generated/neural_response_memory_20260922/scalar_aggregate_analysis01/prefix_errors.csv).

All commands run from /home/amir/Codes/PDE, with a fresh output name on replay:

```bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
export PYTHONDONTWRITEBYTECODE=1
/home/amir/miniconda3/bin/python -B -m unittest discover \
  -s studies/neural_response_memory_20260922 -p test_scalar_aggregate_engine.py -v
/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/scalar_aggregate_run.py \
  --mode pilot --output data/generated/neural_response_memory_20260922/scalar_aggregate_pilot_new --budget 120
/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/scalar_aggregate_run.py \
  --mode campaign --output data/generated/neural_response_memory_20260922/scalar_aggregate_primary_new --budget 3500
/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/repeat_scalar_aggregate.py \
  --primary data/generated/neural_response_memory_20260922/scalar_aggregate_primary_new \
  --out data/generated/neural_response_memory_20260922/scalar_aggregate_reproduction_new
/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/check_scalar_aggregate.py \
  --runs data/generated/neural_response_memory_20260922/scalar_aggregate_primary_new \
  --reproduction data/generated/neural_response_memory_20260922/scalar_aggregate_reproduction_new \
  --out data/generated/neural_response_memory_20260922/scalar_aggregate_audit_new
/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/analyze_scalar_aggregate.py \
  --input data/generated/neural_response_memory_20260922/scalar_aggregate_primary_new \
  --output data/generated/neural_response_memory_20260922/scalar_aggregate_analysis_new
```

The 3500-second primary command is below the frozen cumulative 3600-second
budget, leaving room for the pilot/reproduction. The executed total remains
under 70 seconds before separate analysis and audit. The completed campaign
does not authorize repeating these commands except for an explicit new request.
