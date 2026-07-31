# Frozen protocol: third \(n=256,L=32\) reference block

Protocol frozen before reading the block with `seed_start=10000`.

## Immutable model and PDE target

- Exact architecture: canonical dense Euclidean-\(\mu\)P residual-tanh
  network, \(n=256,L=32\), \(m=3\), \(y=(0.8,-0.55,0.35)\).
- Existing exact blocks: `seed_start=6000`, \(S=32\), and
  `seed_start=8000`, \(S=32\).
- New held-out block: `seed_start=10000`, \(S=64\).
- Full pool: concatenate all raw seeds with equal per-seed weight,
  \(S=128\). No seed rejection or outlier deletion.
- PDE: the already completed
  `pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz`.
- No PDE coefficient, state, basis, \(P,N,M,R\), time step, quadrature seed,
  time window, or observable is changed after seeing the new block.
- Comparison interval: every stored sample on \(0\le t\le8\).
- The PDE Gram is linearly interpolated from its 17 normalized-depth nodes
  onto the exact reference's 33 nodes. These grids are nested.

## Preregistered curve metrics

For a reference pool \(A\), with ensemble means
\(\bar f_A,\bar G_A,\bar\Theta_A\):

1. Output:
   \[
   D_f(A)=\max_t\|f_{\rm PDE}(t)-\bar f_A(t)\|_2.
   \]
2. Output after initialization: the same maximum restricted to \(t>0\).
3. Loss of the mean predictor:
   \[
   D_{\mathcal L}(A)=\max_t
   \left|
   \mathcal L_{\rm PDE}(t)
   -\frac12\|\bar f_A(t)-y\|_2^2
   \right|.
   \]
4. Absolute hidden Gram:
   \[
   D_G^{\rm abs}(A)=
   \max_{t,s}\|G_{\rm PDE}(s,t)-\bar G_A(s,t)\|_F.
   \]
5. Primary variance-reduced feature metric:
   \[
   D_G^{\rm inc}(A)=\max_{t,s}
   \left\|
   [G_{\rm PDE}(s,t)-G_{\rm PDE}(s,0)]
   -
   [\bar G_A(s,t)-\bar G_A(s,0)]
   \right\|_F.
   \]
6. Terminal absolute and increment Gram errors.
7. Tangent-kernel sup error
   \(\max_t\|\Theta_{\rm PDE}-\bar\Theta_A\|_F\).
8. PDE and reference terminal feature motion, and
   \(D_G^{\rm inc}\) divided by PDE feature motion.

Absolute-Gram error is secondary because independently sampled exact
ensembles carry visible \(t=0\) Gram offsets. The Gram-increment error is the
primary reference-noise decision metric.

## Pools and block-stability checks

Metrics will be reported for:

- each block separately: 6000/S32, 8000/S32, 10000/S64;
- existing pool 6000+8000/S64;
- full pool 6000+8000+10000/S128;
- all leave-one-block-out pools:
  - omit 6000, \(S=96\);
  - omit 8000, \(S=96\);
  - omit 10000, \(S=64\).

Every pair of blocks will also be compared directly using the same output,
loss-of-mean, absolute-Gram, Gram-increment, and tangent-kernel sup norms.
No block may be dropped from the primary S128 result because it looks
unfavorable.

## Bootstrap

- Replicates: \(B=2000\), fixed pseudorandom seed `2026072310000`.
- Primary bootstrap: nonparametric resampling of individual seed trajectories
  from the full S128 pool, with replacement.
- Sensitivity bootstrap: stratified resampling within each of the three
  original blocks at their original sizes (32, 32, 64), then pooling with
  equal per-seed weights.
- The complete time/depth trajectory of each seed is resampled as one unit.
  Time points, depth nodes, samples, and Gram entries are never independently
  resampled.
- For outputs, absolute Grams, Gram increments, and tangent kernels, each
  bootstrap statistic is the sup norm of the bootstrap mean minus the full
  pooled mean.
- For loss of the mean predictor, each bootstrap replicate first forms its
  output mean, then computes the loss curve, then takes the sup difference
  from the full-pool loss-of-mean curve.
- Report the 90%, 95%, and 99% quantiles and the centered-bootstrap
  tail probability
  \[
  \widehat p=\frac{1+\#\{T_b\ge D_{\rm observed}\}}{B+1}.
  \]

## Frozen decision language

- For the primary Gram-increment metric, call the discrepancy
  **statistically resolved at the curvewise 5% level** only if it exceeds
  the 95% threshold under both pooled and stratified bootstrap schemes.
- Call it **not statistically resolved** if it is at or below either 95%
  threshold.
- Output, loss-of-mean, absolute Gram, and tangent kernel are classified
  separately as secondary metrics; no uncorrected union of secondary tests
  is used to overturn the primary conclusion.
- Regardless of the result, this tests the PDE against the finite
  \(n=256,L=32\) mean. It does not remove finite-width, finite-depth,
  finite-\(P\), or PDE cubature bias.
