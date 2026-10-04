# First consequence gate: stop this intervention witness

The feature-alignment intervention did **not** provide consequential restoration
of adaptability in the fixed digits test. Its first-probe held-out integrated
MSE was 29.4439, only 0.252% below the untouched closure's 29.5182. Changing that
closure's scalar speed from one to four did better, at 29.1878. Ordinary aligned
factors at speed four achieved 29.1329; dense flow at speed four achieved 29.0886.
The candidate was 1.22% worse than the strongest permitted rival, rather than
the preregistered 25% improvement. Stop this witness; no further seeds, task
search, refinement campaign or promotion is warranted by this result.

This is a single-seed negative screen with deterministic implementation checks,
without the fresh empirical reproduction required for internally checked status.
It is not an independent review or a theorem excluding other optimizer-state policies. The study tested
a new learner intervention, not hidden state in dense gradient flow.

## What was executed

PROTOCOL.md was written before outcomes. A width-256, two-hidden-layer tanh
learner with the exact order-one sample-indexed memories trained on 80 fixed
class-balanced sklearn digits images. Four hundred disjoint images supplied
held-out metrics. Twelve predetermined balanced binary class partitions were
followed by two new partitions; every block lasted training time 64. We used
float64 midpoint RK2, dt=0.1, seed zero, and physical GPU1. All 22 continuation
arms started from the same physical A,B,w. Factor-gradient directions were
normalized to the contemporaneous dense middle-matrix gradient norm, and the
strong factor baseline included a balanced SVD factorization. Scalar speeds
0.25,1,4 were given oracle selection using probe outcomes.

Two pre-comparison launch failures were repaired: NumPy indices were converted
to native integers for JSON, and NumPy 1.26's trapz replaced unavailable
trapezoid. The latter launch computed only its first warm-up block. Incomplete
artifacts remain under generated/seed0; the authoritative complete run is
generated/seed0_run2. No continuation outcomes were used to change the design.
The orthogonal Procrustes control and balanced-SVD competitor were incorporated
before continuation outcomes. The complete successful run took 39.3 seconds;
including failed starts, GPU process usage remained far below 20 minutes.

## All fixed comparisons

Integrated held-out squared error is lower when adaptation is better. The second
probe continues the first without another intervention.

| State/update rule | Scalar speed | Probe 1 integral | Probe 2 integral | Probe 1 final accuracy |
|---|---:|---:|---:|---:|
| Feature-aligned closure, candidate | 1 | 29.443897 | 20.532381 | 85.50% |
| Orthogonally aligned closure | 1 | 29.702214 | 20.646110 | 85.00% |
| Untouched closure | 1 | 29.518245 | 20.718058 | 85.25% |
| Clock refresh | 1 | 31.568105 | 21.218244 | 85.00% |
| Ordinary factors | 1 | 29.778295 | 21.152348 | 86.50% |
| Aligned ordinary factors | 1 | 29.503262 | 21.214506 | 86.75% |
| Orthogonally rotated ordinary factors | 1 | 29.778295 | 21.152348 | 86.50% |
| Balanced-SVD ordinary factors | 1 | 29.773018 | 21.783790 | 85.75% |
| Dense gradient flow | 1 | 29.337529 | 21.026823 | 86.25% |
| Norm-balanced closure | 1 | 29.588170 | 21.284849 | 85.25% |
| Untouched closure | 0.25 | 30.979295 | 25.080092 | 85.00% |
| Untouched closure | 4 | 29.187751 | 19.595565 | 85.50% |
| Clock refresh | 0.25 | 32.914036 | 25.224231 | 85.50% |
| Clock refresh | 4 | 31.285843 | 20.175727 | 85.50% |
| Ordinary factors | 0.25 | 31.179377 | 25.618361 | 86.00% |
| Ordinary factors | 4 | 29.405979 | 20.264260 | 86.50% |
| Aligned ordinary factors | 0.25 | 30.891824 | 25.472517 | 85.50% |
| Aligned ordinary factors | 4 | 29.132903 | 20.339331 | 87.00% |
| Balanced-SVD ordinary factors | 0.25 | 31.018118 | 25.451504 | 85.75% |
| Balanced-SVD ordinary factors | 4 | 29.501705 | 20.895152 | 85.75% |
| Dense gradient flow | 0.25 | 30.584168 | 24.773651 | 86.00% |
| Dense gradient flow | 4 | 29.088564 | 20.126461 | 86.00% |

## Interpretation and validity

The orthogonal closure intervention was worse than leaving the histories alone.
The corresponding ordinary-factor trajectories agreed to a maximum difference
of 4.44e-16 in saved metrics. This is the expected equivariance control: rotating
both factors orthogonally changes neither their product nor ordinary factor
gradient flow. The different closure trajectory therefore reflects the fixed
sample-indexed history writes, but that difference was not useful in this test.
No claim of novelty from gauge conditioning follows. The simple clock refresh
also worsened held-out performance; the actual defeating controls were ordinary
learning-rate changes and factor learning, not a successful clock restart.

Autograd checked the physical A,w mobility n, middle-matrix gradient, factor
gradients and the exact order-one velocity identity; maximum discrepancy was
5.56e-17. All interventions preserved the current function to <1.10e-13 on the
held-out inputs, consistent with the exact matrix-product invariance. Every
arm remained finite. At the checkpoint tau was 92.3251, relative first-feature
movement from initialization was 1.2055, and final warm-up training MSE was
8.85e-5. In the dense speed-one continuation, the middle layer supplied 56.96%
of integrated gradient dissipation on probe one and 49.47% on probe two.
Thus the designated feature-motion, fitting and hidden-learning gates passed.

The untreated learner already reduced new-probe training MSE from 0.7992 below
0.1 within three units of training time; the candidate reached the same
threshold at the same saved time. This test did not establish pre-existing
plasticity collapse relative to a fresh learner. Its defensible negative is
that the proposed intervention offers no meaningful gain after the prescribed
representation drift. It does not exclude a benefit in a separately justified
pathological regime. The 0.252% numerical difference is not asserted as a robust
advantage: no refinement or replication was run, because it was nowhere near
the preregistered consequence threshold and ordinary controls already surpassed
it. Fixed-rank state is not a guarantee of improved adaptation.

The frozen dense initialized matrix still requires n² fixed numbers. Only the
response-memory learned state has the proposed compression interpretation.

## Reproduction

The producer is run_digits_gate.py. The successful invocation was:

```sh
CUDA_VISIBLE_DEVICES=1 /home/amir/miniconda3/bin/python studies/response_memory_plasticity_intervention_20261002/run_digits_gate.py --device cuda:0 --out data/generated/response_memory_plasticity_intervention_20261002/seed0_run2 --max-seconds 1050
```

The generated config records source/protocol SHA-256 hashes, environment and
exact split indices. checkpoint.pt stores the shared aged state. Each warm-up
and continuation has a raw .npy time series; results.json contains every metric.
summarize_digits_gate.py reproduces comparison.csv, decision.json and the
adaptation_comparison figure. No shared code, paper, book or Git index changed.
