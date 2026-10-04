# Initialized learning gate, frozen before execution

2026-10-02. This is an empirical discriminator, not a claim of Gaussian
universality or a practical benchmark victory. Initial allowance: 24 trained
trajectories, 30 GPU-process minutes on GPU1. GPU0 belongs to the independent
control investigation. No hyperparameter search. A failed mechanism gate stops
the efficiency campaign. Numerical refinement is reserved separately below.

## Model and correspondence

Two hidden tanh layers, scalar output, no biases, square loss averaged over m
examples. Width n, input dimension d. The first matrix A is the paper's W^(1),
and w its readout. Store the paper's raw order-one moments H_a=bar h_(a,0)
and D_a=bar delta_(a,0), and clock tau. At a query x,

    h=tanh(Ax/sqrt(d)),
    z=W0 h - 2 sum_a D_a (H_a^T h)/(m n tau),
    g=tanh(z), f=w^T g/n.

Initialize A with iid N(0,1), w=D=0, tau=1, H_a=h(x_a).
For training examples r_a=f_a-y_a, rho=sqrt(mean r_a²),

    delta_a=w odot (1-g_a²),
    ell_a=(1-h_a²) odot [W0^T delta_a
                 -2 sum_b H_b (D_b^T delta_a)/(m n tau)],
    dot A=-2 mean_a r_a ell_a x_a^T/sqrt(d),
    dot w=-2 mean_a r_a g_a,
    dot H_a=rho h_a, dot D_a=r_a delta_a, dot tau=rho.

This is exactly the manuscript's q=1 closure, with unit forward prefix and
zero backward prefix. Only W0's law changes. The structured operator is (3)
of REUSE_THEORY.md with additional independent outer row and column
permutations; forward and transpose use its same arrays. This amendment is
made BEFORE implementation or any training: the extra permutations align the
candidate with the ensemble in Wang--Zhong--Fan, arXiv2206.13037v3,
Proposition D.1(b1). That theorem's applicability to this training system is
still being audited; it is not assumed here. Four laws:
iid Gaussian entries N(0,1/n), flat spectrum, quarter-circle spectrum,
Gaussian-diagonal core spectrum normalized to mean squared singular value1.

## Data and allocation

Use the bundled sklearn handwritten digits, classes3 and8. This real-data
gate is deliberately small; it is not a modern image-classification benchmark.
Fixed stratified split: 32 training images per class, all remaining images
are held out. Split seed7301. Subtract the training mean image, then normalize
each centered image to Euclidean norm sqrt(64); no test statistics used.
Labels -1 for3,+1 for8. Save exact arrays and indices, software version/hash.

Widths512 and2048, seeds7401,7402,7403, four mixer laws =24 trajectories.
Within a width/seed all laws share A and input data; structured laws also
share signs/permutations. Gaussian W0 is independent. This pairing does NOT
make matrix realizations close. Forward law is compared across ensembles.

Integrate physical time T=40 using Heun dt=0.02, float32, no TF32. Save
predictions and activations every2 time units. Use a CUDA graph only after
ordinary eager/captured one-step equality checks. Record train/held-out MSE,
classification error, RMS displacement of both hidden features, initial
feature Gram, total fixed/moving array counts, allocator peak and wall time.
For every initialized feature set compute the exact fixed-feature readout
trajectory through its kernel eigendecomposition as a cheap no-training
control. Its readout mobility is the same n.

Run width512 first. At that width every run must be finite. If all laws have
first-layer motion below0.03 RMS or improve held-out MSE by less than5% over
their own fixed features, this gate has not tested useful feature learning:
stop and record an inconclusive result rather than scaling for speed alone.

## Checks, criteria and stopping

Before training: fast forward/transpose versus explicitly materialized matrices
at width128, relative errors below3e-6 in float32; dot-product adjoint check;
float64 autograd oracle for A,w physical velocities; q1 reconstruction
velocity versus dense update plus exact product defect. Wrong factors stop.

Numerical reserve: at most4 further trajectories, two at dt=0.01 (Gaussian
and quarter-circle seed7401 at largest completed width), and fresh-directory
exact reproductions of their original dt. Tolerance: max prediction RMS
change<0.002; identical-seed reproduction<1e-6. These runs test numerical
reliability; a failed threshold is not repaired by a new scientific setting.

The spectral hypothesis earns a next-stage test only if quarter-circle mean
prediction/feature/Gram trajectories lie closer to Gaussian than BOTH flat
and Gaussian-diagonal alternatives, with the direction consistent at both
widths. Across-initialization variation must be reported; three seeds cannot
establish universality. A split outcome is inconclusive. No positive efficiency
claim without useful feature learning, numerical parity, and measured end-to-end
benefit. Strong direct-factor/dynamical-low-rank controls and a larger real-data
task would still be required before calling this an architectural advance.

All results, source hashes and failed attempts stay in a fresh generated run
directory. Compilation time and warmed training time are reported separately.

## Artifact repair after the initial run (not a changed scientific setting)

The initial 24 trajectories completed in training01, but producer v1 retained
only scalar feature-motion/Gram summaries, not the promised activations.
Predictions and those summaries are available; the full feature/Gram comparison
is not. A code review identified this omission. Preserve v1 as
fast_training_v1.py and its original outputs. The corrected producer retains
both training-layer activations at every saved time, from which the evolving
feature Gram matrices can be reproduced exactly. Repeat the same24 runs in a
fresh directory; this is an explicit additional24-run reproduction allowance,
not a new seed, setting or relaxed criterion. Initial outputs have been seen:
mean predictions favor quarter-circle at both widths; one scalar Gram summary
does not favor it at width512. Thus the full original gate remains unsettled.
The total time allowance remains30GPU-process minutes (first run used15seconds).
