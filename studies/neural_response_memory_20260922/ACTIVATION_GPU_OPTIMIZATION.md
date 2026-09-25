# Bounded GPU optimization of the activation continuation

The user requests a principled search for simple speed improvements, ideally
10--20x, while retaining the same results. This is an implementation
continuation of the activation experiment, not a new scientific model.
GPU 1 remains prohibited until explicit user release. The current scheduler
is paused; its active GPU-0 trajectory finishes normally before profiling.
All completed and capped evidence remains intact.

First measure a complete accepted trial and its RHS, state validation,
physical error calculation and candidate loss. Use a retained mature SELU
P3 state at width4096; distinguish CPU launch/synchronization overhead,
actual device computation and the number of accepted time steps. Do not
attribute small steps to a specific error block without measuring it.

Test one small implementation candidate: keep the same float64 ATen
arithmetic and adaptive Heun controller, group validity/error/loss transfers,
and replay fixed tensor operations through CUDA graphs. Keep dynamic scalar
step combinations outside capture if necessary to preserve their arithmetic.
No model, activation, seed, initialization, optimizer, physical clock,
precision, tolerances, maximum step, stopping criterion or observation grid
is loosened merely to manufacture a speedup. A learning-rate or optimizer
change is not generally an equivalent implementation of this experiment.

Use at most1800 additional GPU-0 wall seconds for profiling and deterministic
equivalence checks, separately recorded from the original scientific campaign
budget. First compare individual complete trials and short evolving runs;
then reproduce a fitted GELU P3 trajectory from its original initialization
and compare accepted steps, error ratios, saved events and circle predictions.
Check nonsmooth activations on retained states as well. Claim bitwise
equivalence only where actually tested; otherwise report numerical differences
and judge against the existing accuracy requirements. Report setup/capture
cost separately and measure complete-step or trajectory speed, not only one
accelerated kernel.

Stop after profiling and this candidate unless the measurement identifies
another comparably small, concrete fix. Avoid a compiler/framework rewrite,
custom GPU kernels, broad hyperparameter search or new training algorithm.
Adopt a candidate only after its equivalence and actual speed are checked;
retain the original implementation as the reference. A10--20x gain is a
desired outcome, not a promised result.

Root owns profiling, bounded execution, comparison and this report.
`activation_engine` owns the new optional fast-step implementation and small
CPU equivalence checks. Frozen campaign producers are initially unchanged.

## Measured outcome and adoption (2026-09-25)

The bounded search found a practical **2.0--2.4x closure speedup**, with
numerical agreement at roundoff scale in the checks below. It did not find a
justified10--20x execution improvement. The search is complete; no optimizer,
learning-rate, precision or tolerance change is adopted.

At the retained SELU P3 state, one original trial costs32.56ms. Ten fixed
matrix products account for approximately25ms. The low-rank learned increments
do not eliminate the two dense4096-by4096 initialized matrices. Each fixed
matrix multiplies only eight training vectors; ordinary matrix multiplication
was inefficient at this shape. Replacing it with one batched matrix-vector
operation is a small change and provides most of the improvement. Transposes
are still the actual initialized-matrix transposes. Circle-query products and
the dense-model implementation retain their original kernels.

Grouping scalar checks and replaying three CUDA graphs reduces Python/driver
dispatch and host synchronization. On the measured SELU P3 state, graphs alone
give1.13x. Combining them with the batched products gives2.38x. Dynamic Heun
step combinations remain outside capture, so the original Python-float
step arithmetic and adaptive controller remain in force. The graph buffers
follow the long-lived input/output requirements in the
[PyTorch CUDA graph documentation](https://docs.pytorch.org/docs/main/notes/cuda.html#cuda-graphs).
The captured profiler lacked individual CUPTI kernel events; its CPU table is
not evidence of isolated GPU compute time. Synchronized wall benchmarks below
are the performance evidence.

| Retained state | Original complete trial | Fast complete trial | Ratio |
|---|---:|---:|---:|
| SELU P3, coarse |32.840ms|13.804ms|2.38x|
| ReLU P3, fine |32.193ms|13.755ms|2.34x|
| SELU P1, fine |35.339ms|17.836ms|1.98x|
| Sigmoid P3, pilot |32.269ms|13.826ms|2.33x|

These are medians of three repetitions on GPU0 at width4096, with every trial
including both RHS evaluations, Heun combinations, physical error control,
finite/activity checks and candidate loss. They are not whole-campaign speed
ratios. Graph capture is separately recorded and costs less than0.3s per case.
Padding and alternative matrix layouts did not improve the original kernel;
larger padding was slower. No custom kernel or compiler framework was added.

The complete fine-tolerance GELU P3 outlier fit takes **51.450s versus104.062s**
including observations, a2.02x ratio. Both runs reach MSE0.001 with2,862 accepted
steps and one rejection. Across all ten saved8192-point circle panels, the
largest prediction difference is3.793e-13. Maximum accepted-time difference is
5.87e-11, and the largest final-state block difference is1.65e-10. This complete
fit compares the original GPU1 result with the new GPU0 result on the same GPU
model; the preceding within-GPU0 trial benchmarks control for device choice.
The new fit's capture cost is0.218s. The reduction order of batched products
differs: these are numerical-equivalence results, not bitwise equality.

The graph-only version is bitwise equal in the tested trials and evolutions.
For the adopted batched version,50 prescribed steps for ReLU/SELU-P1/sigmoid and
100 for SELU-P3 produce maximum state discrepancies at most8.89e-15 and training
prediction RMS discrepancies below1e-16. These short checks do not promise
identical adaptive decisions near every activation kink or error threshold.
Six CPU equivalence fixtures additionally cover all activations and P1--P3.
Independent reconstruction of both physical matrices passes for all ten saved
panels in each complete GELU trajectory. The first replay launch omitted the
required deterministic CUBLAS environment and failed before comparisons;
`replay.json` preserves that failure, and correctly configured `replay02.json`
passes both trajectories. The scoped [internal check](ACTIVATION_GPU_OPTIMIZATION_CHECK.md)
records the arithmetic, buffer-lifetime, archive and provenance review.

Small accepted steps remain a separate cost. At the sampled mature ReLU/SELU
states, the largest error-control components are backward-history and
first-layer state blocks, not only the learned physical-matrix norm. Rejection
counts and observation overhead are small in the slow primary runs. Increasing
steps by loosening tolerances would alter the existing accuracy contract;
switching optimizer would alter the experiment. Neither is needed for the
execution improvement, and no claim that kink crossings alone explain the
small steps has been established.

The fresh generation3 continuation uses the fast runner for remaining moment
primary/refinement runs. Dense runs retain the reference implementation.
Repetitions use their selected original's actual runner/backend. Every run
records either the exact original four-source set or the explicit six-source
fast set; all declared hashes are checked. Previous controller/analyzer bytes
are retained in `activation_circle_engine_check01/execution_adoption_source_snapshot01`.
The69-addition/15-deletion adoption patch passes14 CPU fixtures and retains
38 completed logical primary configurations,26 remaining configurations,
47 prior attempts including pilots/interruption, and9330.716923080385s prior
integration charge. No completed/capped trajectory is overwritten or rescued.
The300s wall cap is unchanged; a faster capped run can therefore reach later
physical time. Scientific comparisons still require shared loss/time events
and the original refinement gates, rather than comparing unequal cap endpoints.
All subsequent work remains on GPU0 until the user releases GPU1.

Evidence directories under `data/generated/neural_response_memory_20260922/`:
`activation_gpu_profile01`, `activation_gpu_matmul01/02`,
`activation_gpu_fast_benchmark01`, `activation_gpu_cross_activation01`, and
`activation_gpu_validation01`. These are execution validation, excluded from
the scientific campaign inventory. In `activation_gpu_matmul01`, the retained
`executed_source.py` exactly matches the original recorded source hash; the
current matrix benchmark adds the later batched/split-product candidates.
Scientific continuation outputs use `activation_circle_primary_continuation02`
and `activation_circle_finish03`, with stage03 analysis/repeat/audit products.

The user subsequently explicitly released GPU1: “you can resume using both
GPUs”, and instructed proceeding with experiments because the current speedup
is sufficient. The running generation3 resource policy now authorizes both
devices; `activation_circle_finish03/user_gpu1_reauthorization01.json` retains
the instruction and policy hashes. This supersedes the GPU0-only restriction
above from that point onward. No further performance search is planned.
