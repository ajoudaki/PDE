# Preregistration: held-out ordered-limit reference audit

Protocol frozen before reading or testing either new exact-network archive.

## 1. Immutable data

### Held-out exact blocks

The analysis will accept exactly these two new archives:

1. `exact_ensemble_n512_L32_S16_seed14000_dt0p02_T8p0.npz`
   - width \(n=512\);
   - residual depth \(L=32\);
   - 16 trajectories with seeds 14000--14015.
2. `exact_ensemble_n256_L64_S48_seed12000_dt0p02_T8p0.npz`
   - width \(n=256\);
   - residual depth \(L=64\);
   - 48 trajectories with seeds 12000--12047.

Both must use the canonical dense Euclidean-\(\mu\)P residual-tanh model,
\(m=3\), targets \(y=(0.8,-0.55,0.35)\), \(T=8\), RK4 step \(0.02\), and
stored step \(0.04\). No seed may be rejected.

### Existing exact blocks

The fixed comparison pools are:

- \(E_{256,32}\), \(S=128\): the already audited seed blocks
  6000/S32, 8000/S32, and 10000/S64;
- \(E_{256,64}^{\rm old}\), \(S=16\): the existing seed 7000/S16
  archive;
- \(E_{256,64}\), \(S=64\): concatenate the old S16 block and the new
  seed 12000/S48 block with equal weight per seed;
- \(E_{512,32}\), \(S=16\): the new seed 14000/S16 archive.

All seeds must be distinct within each pool. Existing archives may not be
silently replaced.

### Fixed PDE curves

The only PDE curves in this audit are:

- \(P5\):
  `pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz`;
- \(P15\):
  `pde_QMC_P15_N16_M256_R128_s20260723_dt0p02_T8.npz`.

Both use the pre-existing \(N=16,M=256,R=128\), quadrature seed 20260723,
time step \(0.02\), and horizon \(8\). No coefficient, basis vector,
whitening map, cubature point, state, time window, or observable may be
changed after either held-out exact block is read. The exact trajectories
are never read by the PDE drift.

## 2. Validation before inclusion

Each held-out archive must pass:

- full ZIP decompression;
- exact metadata, array shapes, seed sequence, and \(0:.04:8\) grid;
- finite values;
- exact recomputation of stored means and SEMs;
- Gram and tangent-kernel symmetry and positive-semidefiniteness;
- no seed overlap with existing blocks;
- loss and \(t=4\to8\) plateau diagnostics already used in the main audit.

A failing archive is reported and excluded only for a specified integrity
failure, never because its scientific result is unfavorable.
Loss/plateau diagnostics are reported but do not make a scientifically
unfavorable trajectory disappear from the audit.

## 3. Frozen observables

For any curve \(X\), define its training increment

\[
\delta X(s,t)=X(s,t)-X(s,0).
\]

The primary distance between curves \(A\) and \(B\) is

\[
D_G^{\rm inc}(A,B)
=
\max_{0\le t\le8,\;0\le s\le1}
\|\delta G_A(s,t)-\delta G_B(s,t)\|_F.
\]

Also report:

- terminal \(D_G^{\rm inc}\);
- absolute-Gram sup distance;
- output sup distance;
- initialization-cancelled output distance
  \[
  D_f^{\rm inc}(A,B)
  =
  \max_t
  \|[f_A(t)-f_A(0)]-[f_B(t)-f_B(0)]\|_2;
  \]
- loss-of-mean-predictor sup distance;
- tangent-kernel sup distance;
- each curve's terminal feature motion;
- \(D_G^{\rm inc}\) divided by the first curve's feature motion.

Depth is normalized to \([0,1]\). For PDE/reference comparisons, linearly
interpolate the 17 PDE nodes to the exact grid. For
\(E_{256,32}\) versus \(E_{256,64}\), linearly interpolate every \(L=32\)
curve to the nested 65-node \(L=64\) grid. The \(L=32\) width comparison
uses its native 33-node grid. No temporal interpolation is required.

## 4. Primary comparisons

### Exact Cauchy comparisons

1. **Width at fixed depth**
   \[
   D_{\rm width}
   =
   D_G^{\rm inc}(E_{512,32},E_{256,32}).
   \]
2. **Depth at fixed width**
   \[
   D_{\rm depth}
   =
   D_G^{\rm inc}(E_{256,64},E_{256,32}).
   \]
3. Report the old \(E_{256,64}^{\rm old}\) comparison and the new
   S48 block comparison separately, plus leave-one-source-block-out
   versions of both pooled references.

These are Cauchy diagnostics, not extrapolated limit estimates. No
\(1/n\), \(1/L\), or Richardson fit will be made from one step.

### PDE comparisons

For each \(P\in\{P5,P15\}\), report \(D_G^{\rm inc}\) and every secondary
metric against:

- \(E_{256,32}\);
- \(E_{512,32}\);
- \(E_{256,64}^{\rm old}\);
- the held-out \(E_{256,64}^{\rm new}\) S48 block;
- pooled \(E_{256,64}\).

Every original acquisition block is also reported separately.

### P15-versus-P5 direction

For each pooled exact reference \(E\), define

\[
I(E)=D_G^{\rm inc}(P5,E)-D_G^{\rm inc}(P15,E).
\]

Positive \(I\) means P15 is closer; negative \(I\) means P15 is farther.
This signed improvement is fixed before the held-out blocks are read.

## 5. Blockwise diagnostics

Original files remain the acquisition blocks:

- \(E_{256,32}\): S32, S32, S64;
- \(E_{256,64}\): old S16 and held-out S48;
- \(E_{512,32}\): held-out S16.

Report:

- every PDE-versus-block metric;
- every pairwise block distance at the same \((n,L)\);
- the pooled result after deleting each source file;
- for the held-out L64 S48 block, three predeclared contiguous S16
  subblocks: seeds 12000--12015, 12016--12031, 12032--12047;
- for the held-out n512 S16 block, two predeclared contiguous S8
  sensitivity halves.

The deterministic subblocks diagnose seed stability but are not independent
data acquisitions and do not change the primary decision.

## 6. Bootstrap

- Replicates: \(B=2000\).
- Master seed: `2026072314000`.
- Whole network trajectories are resampled; time points, depth nodes,
  samples, and matrix entries are never resampled independently.

### One-reference uncertainty

For each exact pool, estimate the curvewise uncertainty of its mean using:

1. pooled individual-seed resampling;
2. source-file-stratified resampling at the original file sizes whenever
   the pool contains more than one source file.

The statistic is the sup norm of the resampled mean curve minus the full
mean curve. Apply the increment before taking the Gram sup.

### Two-reference Cauchy uncertainty

For width and depth comparisons, independently resample both exact pools and
use the centered two-sample statistic

\[
T_b=
\max_{t,s}
\left\|
[(\delta\bar G_A^b-\delta\bar G_A)
 -
 (\delta\bar G_B^b-\delta\bar G_B)](s,t)
\right\|_F.
\]

Run both:

- pooled seed resampling on each side;
- source-file-stratified resampling on every multi-file side.

### PDE discrepancy uncertainty

For each PDE/reference pair, compare the observed deterministic PDE gap to
the one-reference bootstrap uncertainty for that exact pool.

### P15-versus-P5 improvement uncertainty

For every bootstrap exact mean \(E_b\), compute

\[
I_b=D_G^{\rm inc}(P5,E_b)-D_G^{\rm inc}(P15,E_b).
\]

Report percentile 95% intervals for \(I_b\), under both pooled and
stratified schemes when available.

For all bootstrap statistics report 90%, 95%, and 99% quantiles. For a
nonnegative discrepancy \(D\), report the centered-bootstrap tail
probability

\[
\widehat p=(1+\#\{T_b\ge D\})/(B+1).
\]

## 7. Frozen decision language

1. A width or depth Cauchy gap is **statistically resolved at the curvewise
   5% level** only if its observed \(D_G^{\rm inc}\) exceeds the 95%
   centered two-sample threshold under both pooled and stratified schemes.
   It is otherwise **not statistically resolved**.
2. A PDE/reference Gram-increment gap is called resolved only if it exceeds
   the 95% one-reference threshold under both available schemes.
3. P15 is called **statistically closer** only if the 95% interval for
   \(I_b\) lies strictly above zero under both available schemes. It is
   called **statistically farther** only if both intervals lie strictly
   below zero. Otherwise its direction is unresolved.
4. Secondary observables are classified separately. No uncorrected union
   of secondary tests overturns a primary decision.

## 8. Interpretation boundaries

This experiment forms an L-shaped finite grid, not an ordered-limit proof:

\[
(256,32)\longrightarrow(512,32),
\qquad
(256,32)\longrightarrow(256,64).
\]

It does not contain \((512,64)\), a second width step, a second depth step,
or an actual \(n\to\infty\) limit at fixed \(L\). Therefore:

- a smaller width/depth gap is evidence of finite-grid stability, not a
  convergence rate;
- failure to resolve a gap is not proof that it is zero;
- a resolved gap does not say whether the next step shrinks;
- agreement with \(E_{512,32}\) is not agreement with continuous depth;
- agreement with \(E_{256,64}\) is not agreement with the fixed-\(L\)
  infinite-width law;
- P15 moving closer is not proof of \(P\)-convergence;
- P15 moving farther can reflect finite-\(P\), quadrature/whitening,
  finite-\((n,L)\), or structural closure bias;
- neither outcome proves or disproves the mathematical existence of an
  accuracy-dependent PDE family.

The scientifically valid endpoint is a quantified finite-grid Cauchy audit
and a held-out comparison of two fixed genuine PDE discretizations, with all
remaining biases named explicitly.
