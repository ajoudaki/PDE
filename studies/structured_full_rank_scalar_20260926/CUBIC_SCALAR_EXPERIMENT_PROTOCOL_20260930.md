# Direct scalar response ODE comparison with dense Gaussian training

2026-09-30. User-authorized implementation and empirical comparison. This
continues the scalar-response investigation in this study. Freeze before
candidate implementation or training. Root owns candidate/driver/README;
scoped agents inventory existing references and independently audit formulas.

## Decision question

Does the newly derived cubic-response, positive-kernel scalar ODE reproduce
the fitted test function of a canonical dense Gaussian network at n=1024 on
the study's existing circle tasks? Does its first feature-learning correction
improve over the frozen initial-kernel predictor on those same references?

The small-label theorem does not guarantee this unit-label experiment.
Failure would reject this particular low-order approximation in that regime,
not arbitrary scalar compression. Success would be finite-task evidence,
not a population-limit or order-convergence theorem.

## Model, coefficient provenance and comparison

Use the exact formulas in KERNEL_SCALAR_ROUTE_20260930.md: evolve r,z,the
antisymmetric part of J, and the third response integrals P. No neuron arrays,
histogram, density, reference forcing or Fourier approximation may enter
the scalar vector field. Use the full arbitrary-query decoder and its
training-alias completion. Readout starts at zero in the derived surrogate.

For this direct comparison, compute the finite contraction coefficients from
the SAME initial first weights and FULL Gaussian middle matrix as the dense
reference: dense_compare.initialize(1024,1,'gaussian'). The algebraic formulas
apply to a full finite matrix as well as blocks. This avoids adding a block-
initialization replacement error. It does not establish width-uniform
Gaussian-population compression. Initial coefficient construction may depend
on width; retain only scalar tensors for subsequent ODE evolution.

The dense reference uses the canonical tiny initial readout N(0,1/n²).
Record its initial output discrepancy from the zero-readout surrogate.
One predeclared zero-readout dense control below measures this convention's
effect; do not silently change the reference convention.

Activation tanh; normalized circle inputs (cos θ,sin θ); unhalved training
MSE; mobilities (n,1,n); fully unrestricted dense middle training. The primary
comparison uses each method's first training-MSE crossing at 0.001, matching
the latest available reference runs. This is a fitted threshold endpoint,
not an exact infinite-time endpoint.

## Fixed task panel and controls

Use seed1 on these nine existing tasks, with their exact saved angles/labels:
pair_cos3, pair_orthogonal_cos1, near_pair_sin9, cluster_triple_cos9,
cluster_triple_cos1, triple_wide_mixed, quartet_mixed, broad_ridge6,
alternating3. Reuse the verified complete dense checkpoints in
data/generated/structured_full_rank_scalar_20260926/all_tasks_j2_20260927/references/.
Do not select tasks or initialization seeds after inspecting candidate results.

For bias-free tanh, exact antipodal duplicate examples with opposite labels
may be combined with their original multiplicity. For alternating3 all
multiplicities equal two, so its six-sample gradient is exactly the uniform
three-representative gradient. Preserve and report this architectural identity;
do not add a ridge to hide singularity. Other conditioning failures are reported.

The frozen initial-kernel control uses the same initial Gram/cross-Gram and
the same MSE threshold. It requires only matrix exponentials/eigendecomposition,
not another dense training run.

## Primary observable and interpretation

Primary metric is the UNNORMALIZED circle RMS
sqrt(mean((f_scalar(theta)-f_dense(theta))²)) on 256 uniform angles, with
128-point subsampling as a quadrature check. Save both predictions and plot
the functions, training locations, and differences. Teacher test error is
not the fidelity metric. Report training MSE, fit status, flow time, state
count, coefficient count/bytes, initialization and evolution runtime.

Descriptive screen bands for labels on their existing scale: RMS≤0.05 is
close; RMS>0.15 is poor; intermediate values are partial accuracy. These are
operational bands, not universal scientific thresholds. A fitted training
loss by itself is not success. Improvement over the frozen-kernel control is
a separate comparison; a failed control is not grounds to relax fidelity.

## Numerical validity and predeclared checks

Float64, one BLAS thread. Scalar RK45 with rtol1e-8, atol1e-10, physical-time
cap3000, maximum step10, first threshold crossing refined by the solver's
dense interpolant. No adaptive model parameters or coefficient fitting.
Report initial-Gram eigenvalues/condition; reject condition>1e12 rather than
silently regularizing. Retain failures and partial endpoints.

Before task runs, verify the initializer and decoder against explicit
small finite-matrix contractions, the one-sample scalar reduction, positive
kernel and exact training aliases. Independently audit tensor orientations.
On the first two panel tasks, repeat only scalar integration at rtol1e-9,
atol1e-11 using identical coefficients; require circle-output RMS change
below1e-4 or label numerical uncertainty explicitly. If the 256/128 RMS
change exceeds1e-3 on a task, evaluate the SAME endpoints on512 angles
once, without retraining, and report the refinement.

Two fresh dense numerical checks are authorized within this protocol:
pair_cos3 seed1 n1024 at MSE0.001 with rtol1e-6, atol1e-9, first from canonical
initial readout, then from zero readout, using identical first/middle weights.
They quantify saved-reference solver and small-readout effects, respectively.
They do not replace or tune the primary saved reference.

## Budgets and stopping

At most nine primary scalar runs, two scalar tolerance checks, and the two
specified dense controls. No seed sweep, label-amplitude sweep or new order
search. Scalar evolution budget10 seconds/run; coefficient construction
budget30 seconds/task; dense control budget40 seconds/run; total experiment
budget240 wall seconds excluding source development. Use bounded query
batches and at most2 GiB process memory. Stop failed configurations cleanly
and retain their last accepted endpoint. Do not extend budgets to force a fit.

Store fresh products under
data/generated/structured_full_rank_scalar_20260926/cubic_scalar_20260930/.
Never overwrite previous experiment data. Record source/configuration hashes,
command, environment, reused checkpoint hashes, endpoint arrays and all outcomes.
At completion update the study README with the measured answer and limits.
