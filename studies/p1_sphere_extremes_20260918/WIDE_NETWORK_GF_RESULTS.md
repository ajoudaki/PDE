# Quick wide-network GF check of the seven-input configuration

2026-09-18. Empirical finite-network result, not a p=1 closure or infinite-
time theorem. The numerical plan was frozen in `wide_network_gf_plan.md`
before implementation and execution. All three prescribed runs completed
in 44.884 seconds, under the 240-second numerical budget, with peak process
RSS 157.36 MiB and two BLAS threads. No additional training run was made.

## Main result

Both canonical finite initializations fitted the seven labels to the
predeclared loss tolerance 1e-6. Neither trajectory remained at 48/49.

| Run | Seed | Final physical time | Initial loss | Final loss |
|---|---:|---:|---:|---:|
| Main | 20260918 | 59.46867991097213 | 1.0000027880060407 | 9.4819222019187e-7 |
| Tenfold tighter replay | 20260918 | 59.46867991097213 | 1.0000027880060407 | 9.47466248513646e-7 |
| Second seed | 20260919 | 61.51812593814426 | 1.0000022093118812 | 9.305026839894122e-7 |

All seven predictions had the correct sign. The main terminal predictions,
in data order, were

```text
 1.000508624   0.998190598   0.999444053
-0.999961444  -0.998416753  -0.999520273  -1.000239455
```

The second seed's smallest signed margin was 0.9979120914. Its largest
absolute prediction error was therefore approximately 0.00209. Initial
outputs were small random values; they were not manually set to zero.

The constant-prediction benchmark is 48/49=0.9795918367. In the main
saved trajectory, the first accepted point below that level was at time
3.2015859452; first accepted points below .5, .1 and .01 were at times
20.8577174772, 26.1398444947 and 33.9401135509. These are sampled crossing
times, not certified or interpolated hitting times.

## Model and numerical checks

This is the actual bias-free dense network, with two hidden tanh layers of
width1024 and 1,052,672 trainable scalar parameters. Inputs are
x(theta)=sqrt(3)(1,cos(theta),sin(theta))/sqrt(2). Positive angles are
0,2pi/3,4pi/3; negative angles are pi/4,3pi/4,5pi/4,7pi/4. Every mass is
1/7. Use raw first normalization 1/sqrt(3), output normalization 1/1024,
canonical Gaussian variances (1,1/1024,1/1024^2), unhalved mean-square loss,
and physical gradient mobilities (1024,1,1024). All weights evolved.

The optimized NumPy RHS was independently compared with the maintained
`pde.finite_network.flow_velocity` at initialized and nontrivial small
states and at every completed wide endpoint. The small-state maximum
block discrepancies were below1.6e-16. Endpoint errors were also below the
predeclared tolerance. The directional loss derivative agreed with minus
the physical squared speed to relative error3.90e-10; the independently
formed maintained kernel gave the same speed to rounding precision.

An embedded Bogacki--Shampine RK3(2) method approximated GF in float64.
The main tolerances were rtol2e-5, atol2e-8, in block physical norms scaled
by learned displacement. Both tolerances were divided by ten for the
same-seed replay. The replay covered the exact main final time. Across
all common checkpoints, including that endpoint, the largest absolute
prediction difference was4.4052870389554855e-5, below the1e-3 validity
threshold. Final loss differed by7.259716782240752e-10, below2e-5.
The second seed used the main tolerance and did not receive a separate
refinement run, as specified before execution.

Every saved accepted loss strictly decreased. No trial was rejected by the
loss-increase guard; rejections were for the embedded integration error.
Accepted/rejected step counts were193/116,256/97 and188/54. Thus the guard
did not alter the accepted trajectory through a loss-based rejection in
these runs. The full dense matrix remained trainable and its actual
transpose was used throughout.

This was not effectively frozen-feature training: paired activation RMS
changes, averaged over neurons and the seven inputs, were0.40636 and
0.46791 in the first and second hidden layers for the main run, and
0.41851 and0.47539 for the second seed. The main physical parameter
displacements were2.53573,2.27092,3.44442 for W1,W2,c respectively.

The scoped read-only checker verified the canonical scaling, optimized
equations, embedded integrator coefficients, FSAL reuse, block error norm,
and replay design without identifying a substantive bug. The lead then
reanalyzed each saved CSV: all stored losses exactly matched the direct
mean squared prediction errors at float64 evaluation, times strictly
increased, all arrays were finite, and all labels were fitted in sign.
These are numerical checks, not rigorous discretization-error bounds.

## Reproduction and evidence

From the repository root, using a fresh output directory:

```sh
timeout 250s env OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 python studies/p1_sphere_extremes_20260918/wide_network_gf.py --output data/generated/p1_sphere_extremes_20260918/wide_network_gf_20260918_01
```

The recorded execution used Python3.10.12, NumPy1.26.4 and SciPy1.13.0,
with HEAD019e3630237e33f58b9636c0aa67a039bebf0182. The numerical implementation
uses NumPy; SciPy is recorded but its solver was not used. The output path
above now exists; a repeat must choose a new path. The process exited0.

Raw evidence is in
`data/generated/p1_sphere_extremes_20260918/wide_network_gf_20260918_01/`:
the manifest, all accepted-step trajectory CSVs, final parameter/data NPZs,
unit RHS/gradient/energy checks, replay comparison, post-analysis checks,
per-run summaries, and aggregate `results.json`.

* Script SHA256: `59220182d3e1aee797f12cc46241d6ea7cb2f08947c3399bb9549c9c7e409850`.
* Plan SHA256: `a5168c82ac195f5aea56c9b93c594e5455c70992066fca32057310424d279377`.
* Manifest SHA256: `76501d8a777e32d11f91cbc8fab7702499bfe231baabca0b1d565c08596f72d2`.
* Aggregate results SHA256: `c9a16d01b3483f23b35931b6dc2891ca8862e5cff4d0ed00d8d501a3512d5d61`.
* Post-analysis checks SHA256: `3d266562dc5e4abc203d55eec74b79be79de2897dfca7171d5d079099784872b`.

## What this changes

For this fixed geometry, these two width1024 networks from canonical
finite Gaussian initialization numerically fitted. Remaining near48/49
is contradicted for their observed, checked trajectories. The specific
width, two seeds and finite horizons do not determine an infinite-width
limit, an infinite-time probability, or behavior at every latitude C.

In particular the experiment does not establish reachability, nonreachability
or basin size of the constructed fixed-p=1 equilibrium. That equilibrium
belongs to a different autonomous closure. Its existence, cubic descent,
special noncanonical converging trajectories and unresolved canonical
reachability remain as stated in the theoretical reports. No mathematical
claim is upgraded solely on the basis of these numerical losses.
