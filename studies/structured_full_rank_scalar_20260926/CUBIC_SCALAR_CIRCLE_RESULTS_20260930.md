# Cubic scalar ODE versus fitted dense Gaussian circle outputs

2026-09-30. **The construction captures several test functions with very few
evolving states, but fails badly on two of the strong-learning tasks.** All
nine scalar models fit the training data to MSE 0.001. Therefore fitting and
stable stopping do not, by themselves, preserve the dense test function.

This is an empirical implementation of the proposed cubic-response scalar
ODE in [the derivation](KERNEL_SCALAR_ROUTE_20260930.md), not a population
sample, histogram, or new polynomial hierarchy. Its small-label theorem
does not guarantee accuracy on these existing unit-scale labels.

## What was compared

The dense reference is the bias-free two-hidden-layer tanh network,

\[
h_1(x)=\phi(W_1x),\qquad h_2(x)=\phi(W_2h_1(x)),\qquad
f(x)=W_3^\top h_2(x)/n,
\]

with normalized circle inputs, canonical gradient-flow mobilities (n,1,n),
n=1024, seed 1, and unrestricted training of the middle matrix. The input
normalization is already included in the circle convention; no additional
division by sqrt(2) is applied. Both methods use the same training inputs
and labels. Each stops at its own first **MSE 0.001** crossing, corresponding
to training RMSE about 0.03162. These are threshold-fitted endpoints, not
infinite-time limits or comparisons at equal physical time.

The scalar initializer computes the response contractions from the **same
initial first weights and full Gaussian middle matrix** used by the dense
reference. Thus this experiment does not also replace Gaussian initialization
by blocks. The finite contraction identities apply to a general finite
matrix; the earlier block-population theorem does not automatically supply
a unit-label, dense-Gaussian population guarantee for this experiment.

During evolution the scalar vector field retains only residuals, their
integrals, antisymmetric second integrals, and third response integrals,
together with fixed aggregate tensors. It has no access to neurons, dense
weights, a reference trajectory, or test samples. The circle queries are
passive evaluations of the arbitrary-query decoder. There is no Fourier
approximation and no teacher test-error metric.

The measured fidelity is

\[
\left[\frac1{256}\sum_{j=0}^{255}
  \left(f_{\rm scalar}(2\pi j/256)-f_{\rm dense}(2\pi j/256)\right)^2
\right]^{1/2}.
\]

This is an **unnormalized** quadrature estimate of circle RMS difference.
The frozen initial-kernel predictor is a separate cheap control, stopped
at MSE 0.001 or physical time 3000. It is not used to force or fit the
scalar coefficients. Its one incomplete fit is explicitly identified below.

Nine cached dense endpoints were verified by hashes and exact replay of
their saved predictions; see [the inventory](CUBIC_REFERENCE_INVENTORY_20260930.md).
The scalar starts with zero readout, whereas the canonical finite dense
network has its tiny random initial readout. Its initial output RMS is
1.4079e-5. Fresh controls below quantify this difference on the pair task.

## Results

| Task | Original training samples | Evolving scalar states, including decoder integrals | Scalar–dense circle RMS | Frozen-kernel–dense circle RMS |
|---|---:|---:|---:|---:|
| Opposite-label pair, pair_cos3 | 2 | 13 | 0.121253 | 0.332349 |
| Orthogonal pair, pair_orthogonal_cos1 | 2 | 13 | 0.045205 | 0.072473 |
| Close opposite-label pair, near_pair_sin9 | 2 | 13 | **1.205628** | 2.050391 |
| Oscillating cluster, cluster_triple_cos9 | 3 | 36 | **1.337774** | 1.526839* |
| Smooth cluster, cluster_triple_cos1 | 3 | 36 | 0.042561 | 0.079609 |
| Wide mixed triple, triple_wide_mixed | 3 | 36 | **0.007535** | 0.032342 |
| Mixed quartet, quartet_mixed | 4 | 78 | 0.039916 | 0.036615 |
| Broad ridge, broad_ridge6 | 6 | 243 | 0.043183 | 0.067454 |
| Alternating circle, alternating3 | 6 | 36 | 0.089800 | 0.100456 |

Every scalar and dense endpoint reached the requested MSE. Eight frozen
controls also fitted; *the oscillating cluster frozen control reached
time3000 at MSE0.00749024, so its RMS is not a matched-target comparison*.
Scalar decoded training outputs reproduce the
ODE residuals to at most 2.15e-14. Accepted scalar loss histories are
monotone in all nine runs.

For alternating3, the six samples comprise three exact antipodal pairs with
opposite labels. Bias-free tanh is odd, and all pair multiplicities are two.
Using three representatives therefore preserves the exact uniform training
gradient. This removes architectural duplicates, not a numerical ridge or
an approximation. All other tasks keep every training sample.

The new correction improves circle fidelity over the frozen kernel on seven
of eight tasks where both methods fit, and is also lower than the incomplete
cluster control. That improvement is insufficient on the two difficult
cases. Five tasks have RMS below the protocol's descriptive 0.05 band;
two are between 0.05 and 0.15, and two exceed 1.2. The same clustered input
geometry succeeds with smooth labels and fails with oscillating labels.
This distinguishes the label-dependent feature-learning demand from input
geometry alone.

![Fitted circle output functions](../../data/generated/structured_full_rank_scalar_20260926/cubic_scalar_20260930/circle_functions.png)

## Why the failures matter

The positive kernel guarantees nonincreasing training loss, and every state
stops at zero residual. Both properties survive these experiments. They
do **not** bound the passive test-output error when the omitted feature
response is large.

An independent saved-state diagnostic finds that the spectral norm of
the dimensionless feature correction K0^{-1}M is approximately 4.06 for
near_pair_sin9 and 13.04 for cluster_triple_cos9. These are far outside the
small-motion sufficient regime used in the proof. The decoder's added
initial-kernel interpolation term, which enforces consistency with the
completed training dynamics, has circle RMS about 1.099 and 1.268 on those
two tasks. Thus a correction that is provably higher order in the small-label
regime becomes large here. Removing it after seeing the results would
change the construction and abandon its training-output consistency; no
such modification was made or credited as a successful run.

These observations reject this **particular low-order approximation as a
general replacement on the tested strong-learning tasks**. They do not
prove that every scalar compression fails. No higher response order,
width limit, seed ensemble, or population-closure error decomposition was
tested in this panel.

## Cost and numerical checks

All nine primary scalar runs, initialization, saved endpoints and the two
predeclared scalar tolerance checks completed in **1.782 seconds total**.
Individual coefficient construction took 0.097–0.197 seconds and primary
ODE integration 0.017–0.074 seconds, using float64 and one BLAS thread.
These timings are not an end-to-end population-limit complexity guarantee.

The training-only dynamic count is 2m+m(m−1)/2. The arbitrary-query decoder
adds m^3 shared dynamic integrals, yielding 13–243 states in this panel.
Static training tensors are additional storage: 336–21,360 bytes, excluding
small eigenvalue/index metadata. Precomputing coefficients for all 256
circle points and training aliases takes another 20,640–465,312 bytes.
These query coefficients are not ODE states. Exact finite-realization
coefficient initialization still requires width-dependent work, and decoding
new, previously uninitialized queries still requires access to that initial
realization or another representation of its coefficient functions.

The checks include:

- Independent finite parameter-gradient contractions, query tensor
  permutations, positive-kernel completion, training aliases, zero-residual
  stopping and a one-sample polynomial integral identity.
- Independent reconstruction of the difficult cluster's coefficients from
  the initial random streams; explicit-loop decoded outputs agree within
  4.1e-12. All nine saved metrics and hashes were checked independently.
- On the first two tasks, reducing scalar rtol/atol from 1e-8/1e-10 to
  1e-9/1e-11 changes circle predictions by only 3.24e-11 and 1.13e-11 RMS.
- After observing the two large errors, a separately recorded
  [numerical-check extension](CUBIC_NUMERICAL_CHECK_ADDENDUM_20260930.md)
  authorized exactly two further solves using those tasks' saved coefficients
  and the tighter tolerance. Their circle predictions change by only
  2.04e-11 and 9.27e-11 RMS, confirming the failures are numerically stable.
  These checks took0.17s and did not change the model or primary results.
- Comparing 128-point and 256-point circle RMS changes the reported error
  by at most 3.80e-8. The protocol's refinement trigger was not met.
- A fresh pair_cos3 dense solve at tighter tolerances differs from the
  cached dense reference by 4.35e-7 circle RMS. An otherwise identical
  zero-readout dense solve differs from the fresh canonical solve by
  1.22e-5. Both controls fit in 3.77 seconds total. These controls establish
  small solver/readout effects on that task, not all tasks.

The [independent implementation audit](CUBIC_DECODER_IMPLEMENTATION_AUDIT_20260930.md)
records its direct checks and diagnostic limits. The protocol is
[CUBIC_SCALAR_EXPERIMENT_PROTOCOL_20260930.md](CUBIC_SCALAR_EXPERIMENT_PROTOCOL_20260930.md).

## Files and reproduction

Implementation: [cubic_scalar_ode.py](cubic_scalar_ode.py).
Task runner: [run_cubic_scalar_circle.py](run_cubic_scalar_circle.py).
Small identities: [check_cubic_scalar_ode.py](check_cubic_scalar_ode.py).
Dense controls: [run_cubic_dense_controls_20260930.py](run_cubic_dense_controls_20260930.py).
Saved-endpoint plotting: [plot_cubic_scalar_circle.py](plot_cubic_scalar_circle.py).

Products, including source hashes, environment/configuration, every endpoint,
training histories, static coefficients, RMS table, PDF and PNG:
`data/generated/structured_full_rank_scalar_20260926/cubic_scalar_20260930/`.
The primary runner intentionally refuses to overwrite a completed run.

Commands used from the repository root:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python studies/structured_full_rank_scalar_20260926/check_cubic_scalar_ode.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python studies/structured_full_rank_scalar_20260926/run_cubic_scalar_circle.py
OPENBLAS_NUM_THREADS=1 python studies/structured_full_rank_scalar_20260926/plot_cubic_scalar_circle.py
```

The plot uses the installed ReportLab backend. No model parameters were
selected from the observed test errors, and no failed task was discarded.
