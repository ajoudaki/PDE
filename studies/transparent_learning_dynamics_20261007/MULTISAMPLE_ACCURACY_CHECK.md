# Multisample accuracy arithmetic check

2026-10-07. Independent read-only recomputation of the saved full-system
accuracy and numerical-refinement statistics. The inspected inputs were
`analyze_multisample_experiment.py`, the saved summary and blockwise CSV,
42 selected raw trajectory archives, and the campaign's 52 metadata records.
No new scientific trajectory was run, and no producer or analysis source was
edited. This is not an independent reproduction of the campaign.

All 12 blockwise accuracy rows and all three numerical-refinement rows agree
with independent raw-array arithmetic to at most \(2.23\times10^{-16}\).
The tabulated relative errors concern differences between ensemble-mean
feature changes on the same Euler mesh. They do not measure individual-network
accuracy or establish a continuous-time approximation. The 16-sample case has
56.8--67.4% relative mean-change RMS error and fails every checked RK4 refinement
gate. False sustained-envelope flags do not reverse those findings.

## Frozen evidence and scope

| Artifact | SHA-256 |
|---|---|
| `analyze_multisample_experiment.py` | `dc316e4c2a9e9b621786013379e47bc47961f49aa41178ababa7cb0f568e47c2` |
| `analysis/summary.json` | `5c22f3aa8492afd421762c27fc4c324d60810363956619ed9f585a0ab9f1aee6` |
| `analysis/blockwise_accuracy.csv` | `f5c353f6d2f92d08f86e4cec2e01f3c7da2088d019a57e616d38b64e73cb0afa` |

The paths under `analysis/` are relative to
`data/generated/transparent_learning_dynamics_20261007/multisample_v1/`.
The analysis source was updated during the audit to add a second figure and
time-resolved CSV. Its numerical functions were inspected again and remained
unchanged. The final summary records the source hash shown above.

All 52 metadata records have successful exit status, with 30 dense and 22
causal runs. Every recorded implementation/mode pair is valid: none uses the
silent unsupported-mode combinations identified in the implementation audit.
Each numerical source has one consistent recorded hash across these runs:

- `multisample_experiment.py`:
  `eb58b62ca466649989067cd1287aa199b99b41899b59536cec02baa186c78b2d`.
- `causal_panel_simulator.py`:
  `e3eec0c1e7f7692460c804dedc1cce2476324a9c2013b35123efe5db7afd522a`.
- `causal_population_simulator.py`:
  `4431bef401087ca0e0f0bd465f1d31d88e7486403ec18d331eab8bbc035e5d76`.

Exactly 42 raw `trajectory.npz` archives were used in the recomputation below.
Their aggregate manifest digest is
`c7166023b991f7f6d2a3a706823b03b64048da0c7dead9ec49e2e67f8f51ae74`.
For reproducibility, compute the SHA-256 of each entire archive, sort its path
relative to `multisample_v1`, form one UTF-8 line
`relative/path/trajectory.npz HEX_DIGEST\n` per archive, concatenate those
lines, and SHA-256 that concatenation. The file families are listed in the
reproduction procedure below. Two endpoint entries of the sorted manifest are:

```text
causal_m16_n1024_s1701_h0.4_euler_full/trajectory.npz d9d7f4c616f259cd1b0782fb1cafc51c9203aec3f3dbb59ade7d0099dcd4becb
dense_m8_n512_s303_h0.4_euler_full/trajectory.npz 6dcb3663f42d704d8e6ed85113c746d1cb6bf627fd94872e7e2dd831bdbf91ed
```

## What the reported norms mean

Each layer contributes an uncentered feature Gram. `TT` contains all \(m^2\)
training-training entries, including diagonals and both symmetric off-diagonal
copies. `TP` contains the \(4m\) training-passive entries, with training index
first. These are not normalized correlation coefficients.

For a chosen block, let \(D_r(k)\) be its flattened dense array from width
1024 and seed \(r\in\{101,202,303\}\), and let \(C_s(k)\) be its causal
array from 512 particles and seed \(s\in\{1701,1702,1703\}\). The bars
denote averages of these three arrays. Define changes separately within each
realization:

\[
\Delta D_r(k)=D_r(k)-D_r(0),\qquad
\Delta C_s(k)=C_s(k)-C_s(0).
\]

The reported change-error array is
\(E(k)=\overline{\Delta C}(k)-\overline{\Delta D}(k)\).
For a block with \(b\) entries, the two reported error norms are

\[
e_{\rm entry}=\max_{k,i}|E_i(k)|,\qquad
e_{\rm RMS}=\max_k\sqrt{\frac1b\sum_{i=1}^bE_i(k)^2}.
\]

Thus the RMS is over block entries first, then maximized over saved time.
It is not an RMS over both time and entries, and it is not evaluated only at
the endpoint. The absolute-error rows apply the same norms to
\(\bar C(k)-\bar D(k)\), without subtracting initialization.

The relative RMS is a ratio of two separately maximized norms:

\[
\frac{\max_k\operatorname{RMS}(E(k))}
     {\max_k\operatorname{RMS}(\overline{\Delta D}(k))}.
\]

It is not the maximum pointwise relative error. Its numerator and denominator
can attain their maxima at different times. The feature-change curve itself
is the RMS of the ensemble-mean change, not the mean RMS movement of individual
networks.

The dense variability summary is the mean over the three seed pairs of each
pair's own maximum-in-time block RMS difference. The time-resolved variability
curve instead averages pairwise RMS differences at each time. Taking the
maximum of that curve need not equal the scalar variability summary because
maximum and averaging do not commute. Both calculations are correct in the
source, but they are different statistics. Neither is the standard error of
the ensemble mean.

## Independently reproduced accuracy values

| Training samples | Layer | Block | Maximum mean-change RMS error | Maximum dense mean-change RMS | Relative error |
|---:|---:|---|---:|---:|---:|
| 4 | 1 | TT | 0.00472701 | 0.05598699 | 8.443% |
| 4 | 1 | TP | 0.00385844 | 0.04596656 | 8.394% |
| 4 | 2 | TT | 0.00429891 | 0.12017822 | 3.577% |
| 4 | 2 | TP | 0.00421282 | 0.09811286 | 4.294% |
| 8 | 1 | TT | 0.00538048 | 0.04576135 | 11.758% |
| 8 | 1 | TP | 0.00538428 | 0.04873327 | 11.048% |
| 8 | 2 | TT | 0.00628846 | 0.10197450 | 6.167% |
| 8 | 2 | TP | 0.00644322 | 0.10550451 | 6.107% |
| 16 | 1 | TT | 0.06030140 | 0.09524541 | 63.312% |
| 16 | 1 | TP | 0.05751881 | 0.09640330 | 59.665% |
| 16 | 2 | TT | 0.07510917 | 0.11151396 | 67.354% |
| 16 | 2 | TP | 0.08248397 | 0.14511326 | 56.841% |

All absolute/change maximum-entry errors, pairwise-dense summaries, and CSV
field mappings were also recomputed. No arithmetic discrepancy was found.
Comparing these mean errors to individual dense-pair variability does not
establish accurate predictions for each realized dense network. In particular,
the large dense variability at 16 samples cannot be used to dismiss its large
relative mean-change error.

## Envelope flags

At each saved time and block entry, the analysis uses

\[
\text{envelope}=3\sqrt{s_D^2/3+s_C^2/3}
+|C_{1024,1701}-C_{512,1701}|
+|\bar D_{512}-\bar D_{1024}|,
\]

where \(s_D^2,s_C^2\) are unbiased sample variances across three draws.
For change rows, every array in this formula is first replaced by its change
from its own initialization. The particle term uses one same-seed pair, and
the width term uses three-draw means. Their saved norms match independent
recomputation.

This is a pointwise diagnostic envelope. Three draws, one particle-refinement
pair, and an additive width difference do not make it a simultaneous confidence
band, a certified numerical error bound, or a convergence rate.

The code subtracts this envelope from the absolute mean error and flags an
excess only when the same entry exceeds a threshold at three consecutive
nonzero saved times. The absolute threshold is 0.005. The relative threshold
is 20% of the maximum absolute entry of the dense ensemble-mean feature change
over the entire block and time interval, not 20% of a local entry or local-time
change. All sustained flags independently recompute as false.

Some pointwise excesses are nevertheless positive. At \(m=16\), layer 1,
TT, the maximum absolute-row excess is 0.0180191 and the change-row excess is
0.00543221. Consequently, “no sustained threshold violation” is accurate;
“every error stays inside the envelope” is not. The envelope test also omits
time-step discrepancy, appropriate only when described as a diagnostic for
the same-Euler-mesh comparison. It cannot clear a failed continuous-flow
refinement gate.

## Dense numerical refinement

The numerical gate compares width-512, seed-101 RK4 runs at normalized steps
0.1 and 0.05. The fine grid sampled every second point exactly equals the
coarse normalized-time grid. Sampling the fine grid every eighth point exactly
equals the normalized-step-0.4 Euler grid. These alignments were checked
directly from saved arrays.

For output, the gate is maximum-entry refinement error at most
\(\max(10^{-5},0.01\max|f_{\rm fine}|)\). For each feature block, it is at
most \(\max(10^{-5},0.01\max|C_{\rm fine}-C_{\rm fine}(0)|)\).
The maxima run over the inspected saved times and the indicated entries.

| \(m\) | Output refinement error | Output threshold | All output/feature gates |
|---:|---:|---:|---|
| 4 | \(6.2164\times10^{-8}\) | 0.00624985 | Pass |
| 8 | \(1.4251\times10^{-6}\) | 0.00848704 | Pass |
| 16 | 0.03510486 | 0.01206708 | Fail |

At 16 samples, every feature block also fails:

| Layer/block | Maximum-entry refinement error | Threshold |
|---|---:|---:|
| 1/TT | 0.00330277 | 0.00097209 |
| 1/TP | 0.00322976 | 0.00081749 |
| 2/TT | 0.00733339 | 0.00196282 |
| 2/TP | 0.00892384 | 0.00190296 |

Its Euler-versus-fine-RK4 maximum-entry feature differences are also large:
0.23343, 0.20188, 0.37314, and 0.41881 for those four blocks. These are
differences between two saved numerical schemes, not errors against an exact
continuous trajectory. The available 16-sample evidence does not control the
continuous-flow interpretation. It does not, by itself, identify why that
comparison is unresolved.

The 4- and 8-sample RK4 checks pass for this particular width and seed. They
do not establish dense numerical control uniformly over all widths/seeds,
nor convergence of the causal Euler system to a continuum law. The causal
step-halving diagnostic is a single 256-particle comparison; its raw-array
arithmetic was verified, but it is not a mesh-uniform population convergence
certificate.

## Reproduction procedure and limits

The independent calculation ran in a read-only isolated Python process from
the repository root, with the command prefix

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -
```

It imported NumPy and the standard library, not the analysis module, and did
not call any producer. For each \(m=4,8,16\), it opened these full-mode raw
archive families:

- Dense Euler, normalized step 0.4, widths 512 and 1024, seeds 101, 202, 303.
- Causal Euler, normalized step 0.4, 512 particles, seeds 1701, 1702, 1703.
- Causal Euler, normalized step 0.4, 1024 particles, seed 1701.
- Causal Euler, normalized steps 0.4 and 0.2, 256 particles, seed 1701.
- Dense RK4, normalized steps 0.1 and 0.05, width 512, seed 101.

Paths follow
`{kind}_m{m}_n{n}_s{seed}_h{h}_{method}_full/trajectory.npz`.
Loading only the required NumPy archive members avoided materializing unrelated
history arrays. The check extracted TT/TP by explicit slicing, flattened only
their entry axes, subtracted each realization's own initial state for change
rows, and recomputed the formulas given above. Sample variances were calculated
from explicit squared deviations divided by two. Sustained flags were checked
by explicit time-window and entry loops, independently of the source's Boolean
slice expression. CSV fields were compared to the recomputed values.

The same process recomputed every saved output/feature refinement norm and
gate, Euler bias, maximal training-kernel eigenvalues, and fine/coarse final
relative losses in the three numerical rows. The largest scalar difference
from the saved summary was \(2.220446049250313\times10^{-16}\). Raw archives
were streamed in 1 MiB chunks for the manifest hashes. A separate metadata
pass verified counts, exit statuses, valid modes, and consistent source hashes.

The summary's control-mechanism, initial-direction, and readout-memory sections
were not independently recomputed in this arithmetic audit. Their source
formulas were visible, but that is not a substitute for raw-data verification.
In particular, first-saved loss crossings in those sections need not equal
interpolated crossing values from a separate diagnostic. The audit therefore
supports the checked accuracy/refinement arithmetic and its stated limits,
not every interpretation in a complete scientific campaign report.

## Bounded check of the result report

The coordinator subsequently supplied `MULTISAMPLE_TRAJECTORY_RESULT.md` for
a check of its headline, blockwise-accuracy section, numerical-resolution
section, and 52-run accounting. Those sections agree with the independent
recomputation above. They explicitly distinguish ensemble-mean same-Euler
agreement from individual-path or continuum guarantees and retain the failed
16-sample result. The envelope claim is appropriately stated as absence of
sustained threshold violations, rather than universal pointwise containment.

The records independently sum to 557.8346692994237 seconds, with maximum
reported process peak RSS 5882.88671875 MiB. These are recorded execution
measurements; this audit did not replay the runs or independently time them.
Metadata contain 52 successful records and the expected valid implementation/
mode combinations. They cannot establish the absence of unrecorded activity
outside this artifact collection.

The maximum recorded covariance-factor error is
\(5.59587304271858\times10^{-9}\), and maximum discarded innovation variance
is \(1.931416406186145\times10^{-12}\). The latter rounds to
\(1.93\times10^{-12}\); a minor correction from the report's initial
\(1.94\times10^{-12}\) wording was requested. Neither quantity estimates
particle sampling error.

One wording clarification was requested: the quoted scalar dense comparator
is the mean of three pairwise maximum-time block RMS differences. It should
not be described as the maximum of the time-resolved mean-pairwise curve.
This concerns the order of reductions, not an arithmetic defect. Mechanism
sections being finalized by the coordinator and another checker were not
independently reaudited in this bounded claims check.
