# Longer thirty-degree GPU sanity check

All eight networks and eight closures reached **T=640**, sixteen times the original
horizon, in **555 seconds of simulation wall time**. Loss and Gram-error curves
flatten substantially, with a remaining slow tail. This answers the user's mild
sanity check; it does not establish equilibrium or a limiting Gram matrix.
The [user's scope clarification](LONG_20260914_SANITY_SCOPE.md) superseded the
requirement to wait for every threshold in the [original plan](LONG_20260914_PLAN.md).

![Loss and both training Gram errors on linear physical time](../../data/generated/wide_network_closure_comparison/LONG_20260914_v1/figures_T000640/sanity_linear_time.png)

The left panel shows actual width8192 network mean loss in blue and representative
closure losses in the other colors. The middle and right panels show each closure's
error against the actual network mean Gram for hidden layers 1 and 2. Lower is
better. The dotted line marks the old T=40 endpoint; shading marks 480–640. Time
is linear, while the loss axis is logarithmic. All eight closures and individual
networks remain in the [complete loss plot](../../data/generated/wide_network_closure_comparison/LONG_20260914_v1/figures_T000640/all_loss_curves.png)
and [complete Gram/increment comparison](../../data/generated/wide_network_closure_comparison/LONG_20260914_v1/figures_T000640/all_gram_and_increment_errors.png).

The training set remains the same 16 inputs: eight with label +1 around 0° and
eight with label −1 around 90°, sampled within ±30°. Labels are simple and
linearly separable. The passive circle still contains 128 points. Network widths
are 2048 and 8192 with seeds 11, 29 and 47; the other two network runs check time
step and precision. Closure orders are N=1,3,5, with the same quadrature refinements
and time-step controls. “Finest N5” uses Q=4096 initialization nodes and P=2048
population nodes. This exploratory geometry and time horizon have no claimed H4
theorem guarantee.

For each layer, the network observable is
Gℓ(a,b;t)=hℓ(xa;t)·hℓ(xb;t)/n. Its reference is the mean of the three seeded
network matrices at the stated width. Matrix error is ||Gclosure−mean Gnetwork||F/m,
with m=16 for training and m=128 for the circle. Loss is the weighted mean squared
training residual, without a factor 1/2; network mean loss averages the three
individual losses. G(t)−G(0) is also compared separately in the full output.

| At T=640, against width8192 mean | Training loss | Layer 1 Gram error | Layer 2 Gram error |
|---|---:|---:|---:|
| Actual network mean | 0.00005745 | — | — |
| N1 | 0.00008537 | 0.040296 | 0.028467 |
| N3 | 0.00007521 | 0.040954 | 0.064720 |
| N5, base quadrature | 0.00008346 | 0.045050 | 0.065784 |
| N5, finest quadrature | 0.00008504 | 0.040014 | 0.050431 |
| Frozen initial network Gram | — | 0.391288 | 0.497727 |

The finest closure's terminal Gram errors are 9.78× and 9.87× smaller than the
frozen baseline. Its circle errors are 0.038320 and 0.050751. Higher order still
does not improve every observable: N1 has the smallest terminal layer-2 Gram error
among these runs. The frozen baseline only predicts Grams; it is not an NTK loss
simulation. See the [comparison including frozen baselines](../../data/generated/wide_network_closure_comparison/LONG_20260914_v1/figures_T000640/loss_and_gram_errors.png).

From 480 to 640, finest N5 training Gram errors rise from 0.038380 to 0.040014 and
0.048053 to 0.050431. Its actual Grams move by 0.005858 and 0.010276 in matrix RMS.
Across every individual run, layer and panel, that late Gram movement ranges from
0.005038 to 0.010497. Thus the Grams themselves are still moving. Network mean loss
falls from 0.00008880 to 0.00005745; finest N5 loss falls from 0.00015459 to
0.00008504. Those absolute changes are small, but the relative reductions remain
35% and 45%. “Flattening” is more accurate than “fully settled.”

The original strict two-window test fails 314 of 416 conditions. That diagnostic
was retained unchanged; the user-directed stop is separate. Time-step and precision
controls pass the 0.002 cutoff, with worst cumulative discrepancy 0.000233.
Quadrature remains unresolved: the finest N5 refinement comparison reaches
0.006879. These checks support the computed comparison without certifying the
exact closure limit or long-time convergence.

The old runs had no restart states, so all 16 configurations were replayed through
40 and matched their archived scalar and Gram observations exactly. The same Heun
dynamics then advanced through 80,160,320,640, saving full matrices and actual-state
checkpoints at each stage. After 40, primary time steps are 0.05 and the existing
half-step controls use 0.025. There are 286 unique saved observation times.
The [independent arithmetic check](../../data/generated/wide_network_closure_comparison/LONG_20260914_v1/independent_final_check.json)
uses raw arrays without the main analysis or plots. The
[final verification](../../data/generated/wide_network_closure_comparison/LONG_20260914_v1/final_verification.json)
compares its numbers, validates completed artifact hashes and preserves all 445
earlier files. These are internal checks, not promotion review.

The [layer-1](../../data/generated/wide_network_closure_comparison/LONG_20260914_v1/figures_T000640/layer1_gram_evolution.png)
and [layer-2](../../data/generated/wide_network_closure_comparison/LONG_20260914_v1/figures_T000640/layer2_gram_evolution.png)
matrix figures show the passive circle at 0,40,320,640: top row actual network mean,
middle finest N5, bottom their difference. All sources remain flat in this study;
arrays, checkpoints and plots remain under LONG_20260914_v1. Exact commands and
source hashes are in long_campaign.json, supervisor.json and each stage record.
Reproduction should use a fresh prepared namespace and only stages 40–640 for this
scope. The original supervisor follows the stricter plan unless stopped at this
user cap. Four just-launched T=1280 workers were cancelled before any saved
observations; their logs and zero-step metadata are preserved and excluded from
all results. No further simulation is pending.
