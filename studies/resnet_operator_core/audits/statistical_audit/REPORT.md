# Independent statistical audit of the dense operator-PDE simulations

> **Compact-edition provenance note.** This audit was written against the
> original 689 MB release. Its inventory statements about current raw NPZ
> directories, `reference_noise_bootstrap_distributions.npz`, and
> `ordered_limit_bootstrap_distributions.npz` refer to that full release, not
> to this compact source-first edition. The compact bundle intentionally omits
> raw trajectories and bootstrap arrays while retaining the complete
> regeneration and verification code, compact tables, and audit report. The
> canonical protocol regenerates the omitted files locally.

## Bottom line

The new code has genuinely simulated a width-independent, autonomous
operator-Galerkin PDE candidate.  The stored curves are numerically stable,
restartable, non-lazy, and remain flat through the long-horizon continuation.
The agreement with independently generated dense-network ensemble means is
close in relative terms, but the enlarged held-out reference now resolves a
small systematic discrepancy.

After a protocol was frozen, a third \(n=256,L=32\) exact block added 64
previously unseen seeds, giving \(S=128\) in total. The primary
initialization-cancelled hidden-Gram increment discrepancy is
\(7.243\times10^{-3}\), or \(1.143\%\) of the PDE feature motion. It exceeds
the curvewise 95% reference-noise threshold under both pooled and
block-stratified bootstraps. Thus the current fixed PDE is statistically
distinguishable from the finite \(n=256,L=32\) mean in this observable.
Output, loss, absolute-Gram, and tangent-kernel discrepancies remain below
their corresponding thresholds.

This does **not** by itself refute the ordered width-then-depth PDE
conjecture. The detected difference can contain finite-width/depth bias and
finite PDE basis/depth/cubature error. It does rule out describing the
current curves as statistically indistinguishable in every primary
observable, and it strengthens the need for a cofinal nested-\(P\) PDE
refinement before claiming arbitrary-accuracy convergence.

No PDE coefficient was fitted, tuned, or estimated in this audit.

## Data and metrics

The audit reads every current NPZ archive under:

- `results/raw`;
- `audits/numerics`.

It also analyzes the paired conditional-variance data in
`paired_W_conditional_variance_hp.csv`.

For two output curves the primary error is

\[
\max_t \|f_1(t)-f_2(t)\|_2.
\]

For hidden Grams it is

\[
\max_{t,s}\|G_1(s,t)-G_2(s,t)\|_F.
\]

When depth grids differ, both curves are linearly interpolated on the same
257-point normalized-depth grid.  RMS, terminal, initialization, tangent
kernel, and initial-centered discrepancies are recorded separately in the
CSV tables.

Exact-network uncertainty is reported as the empirical standard error of the
ensemble mean.  For every raw \(m=3\) ensemble, 500 fixed-seed nonparametric
bootstrap resamples estimate the 95th percentile of the full-curve sup error
of the sample mean.  These bootstrap values measure only Monte Carlo
uncertainty of a particular finite-\((n,L)\) mean.  They do not include
finite-width bias, finite-depth bias, PDE truncation bias, or QMC error.

The held-out \(S=128\) update additionally uses the frozen protocol in
`REFERENCE_NOISE_PREREGISTRATION.md`: 2,000 pooled and 2,000
within-acquisition-block stratified bootstrap replicates, with full
time/depth trajectories resampled as indivisible units. Its results are in
`REFERENCE_NOISE_UPDATE.md`.

Pointwise SEM-normalized residuals are included as diagnostics, not as global
p-values: time, depth, samples, and Gram entries are strongly correlated.

## 1. PDE numerical error budget

| Comparison | \(\max_t\|\Delta f\|_2\) | \(\max_{t,s}\|\Delta G\|_F\) | \(\max_t\|\Delta\Theta\|_F\) |
|---|---:|---:|---:|
| RK4 \(\Delta t=.02\) vs \(.01\) | \(6.83\times10^{-8}\) | \(1.09\times10^{-7}\) | \(3.56\times10^{-7}\) |
| depth \(N=16\) vs \(32\) | \(2.05\times10^{-4}\) | \(8.45\times10^{-4}\) | \(6.63\times10^{-3}\) |
| earlier empirically whitened basis \(P=5\) vs \(15\) | \(3.68\times10^{-3}\) | \(7.44\times10^{-3}\) | \(4.19\times10^{-2}\) |
| clean hybrid basis \(P=5\) vs \(15\), fixed \(M=81,R=128\) | \(1.12\times10^{-3}\) | \(2.76\times10^{-3}\) | \(2.07\times10^{-2}\) |
| clean hybrid P15 fast cubature \(R=128\) vs \(256\) | \(6.04\times10^{-4}\) | \(9.65\times10^{-4}\) | \(7.68\times10^{-3}\) |
| base cubature \(M=256\) vs \(512\), fixed \(R=128\) | \(1.53\times10^{-4}\) | \(7.83\times10^{-4}\) | \(6.32\times10^{-3}\) |
| fast cubature \(R=128\) vs \(256\), fixed \(M=256\) | \(1.12\times10^{-4}\) | \(1.16\times10^{-3}\) | \(6.32\times10^{-3}\) |
| maximum pairwise spread over 3 QMC scrambles at \(M=256,R=128\) | \(1.32\times10^{-3}\) | \(2.13\times10^{-3}\) | \(3.71\times10^{-2}\) |
| tensor GH versus high-resolution QMC | \(1.03\times10^{-2}\) | \(1.94\times10^{-2}\) | \(1.46\times10^{-1}\) |

The time integrator is decisively below every scientifically relevant error
scale.  Depth refinement is also clean: the \(N=8\to16\) and
\(N=16\to32\) output differences are respectively
\(4.06\times10^{-4}\) and \(2.05\times10^{-4}\), while the Gram differences
are \(1.68\times10^{-3}\) and \(8.45\times10^{-4}\).  This near factor of
two is consistent with first-order depth discretization.

At the current resolution the operator basis, not RK4, is the largest clean
one-axis model-resolution effect. A later hybrid compiler supplies a
well-conditioned nested \(m=3\) step from \(P=5\) to \(P=15\), at fixed
\(M=81,R=128\), and a separate isolated P15 \(R=128\to256\) check. The
complete-cubic P35 stress run changes the base cubature size and latent cloud
from that clean pair, so it is not a third point of a cofinal one-axis
\(P\)-sequence.

The independent tensor-GH/QMC difference remains important. Its output and
absolute-Gram differences are nearly the same size as the current
PDE-versus-reference output and absolute-Gram discrepancies; its Gram
difference is about 2.7 times the primary Gram-increment discrepancy. The GH
and QMC resolutions differ, so this is not a pure one-axis refinement, but
it prevents a claim that cubature-systematic error is already negligible.

The earlier QMC basis sequence remains complicated by empirical whitening:
its raw Hermite Gram error grows substantially with \(P\) before whitening.
The hybrid P5/P15 pair repairs that particular diagnostic, but one clean
step still cannot establish arbitrary-\(P\) convergence. Moreover, the
held-out reference audit below finds that P15 moves farther from every
pooled finite-network reference, so the observed finite-reference error is
not monotonically decreasing with this basis step.

## 2. Exact-network reference uncertainty and limit checks

Fresh exact ensembles materially improve the reference audit.  At \(L=32\)
the stored widths are \(n=64,96,128,256\); independent \(n=128\) and
\(n=256\) archives were pooled only after preserving and checking each
separately.
There are also fixed-width depth pairs \(n=64:L=16,32\) and
\(n=256:L=32,64\).

Representative full-curve 95% bootstrap thresholds for the exact mean are:

| Exact ensemble | output sup threshold | Gram sup threshold | Gram-increment sup threshold |
|---|---:|---:|---:|
| \(n=64,L=16,S=64\) | \(4.25\times10^{-2}\) | \(7.98\times10^{-2}\) | \(1.53\times10^{-2}\) |
| pooled \(n=128,L=32,S=96\) | \(2.51\times10^{-2}\) | \(4.64\times10^{-2}\) | \(8.58\times10^{-3}\) |
| \(n=256,L=32,S=32\) | \(3.47\times10^{-2}\) | \(6.05\times10^{-2}\) | \(1.08\times10^{-2}\) |
| pooled \(n=256,L=32,S=128\) | \(1.60\times10^{-2}\) | \(2.91\times10^{-2}\) | \(4.98\times10^{-3}\) |
| pooled \(n=256,L=64,S=64\) | — | — | \(7.07/7.11\times10^{-3}\) |
| \(n=512,L=32,S=16\) | — | — | \(9.22\times10^{-3}\) |

The current exact-reference Cauchy differences are:

| Exact comparison | output sup | absolute-Gram sup | Gram-increment sup |
|---|---:|---:|---:|
| pooled \(n=128\) vs pooled \(n=256\), fixed \(L=32\) | \(1.45\times10^{-2}\) | \(4.86\times10^{-2}\) | \(1.24\times10^{-2}\) |
| pooled \(L=32,S=128\) vs \(L=64,S=64\), fixed \(n=256\) | \(1.03\times10^{-2}\) | \(4.41\times10^{-2}\) | \(4.23\times10^{-3}\) |
| pooled \(n=256,S=128\) vs \(n=512,S=16\), fixed \(L=32\) | \(2.99\times10^{-2}\) | \(4.40\times10^{-2}\) | \(9.35\times10^{-3}\) |
| original \(n=256,L=32,S=32\) vs \(n=256,L=64,S=16\) | \(1.54\times10^{-2}\) | \(7.84\times10^{-2}\) | \(4.681\times10^{-3}\) |

The raw absolute-Gram comparisons are dominated by independent finite-sample
initialization offsets.  Subtracting each ensemble's \(t=0\) Gram gives the
much smaller increment gaps above.  In particular, the
\(L=32\to64\) increment gap \(4.681\times10^{-3}\) is only about \(0.73\%\)
of the roughly \(0.64\) feature motion.  This is meaningful positive
evidence for depth stability.

The preregistered two-sample pooled/stratified thresholds are
\(8.57/8.98\times10^{-3}\) for the depth gap and
\(9.97/10.31\times10^{-3}\) for the width gap. Thus neither observed Cauchy
gap is statistically resolved. That is not evidence that either is zero;
the \(n=512\) reference in particular has only 16 trajectories.

The enlarged \(L=32\) reference is now quiet enough to detect the current
PDE Gram-motion discrepancy, but the width/depth Cauchy data still do not
support a reliable extrapolation in \(1/n\), \(1/L\), or a joint
width-then-depth limit.

## 3. PDE versus exact-network curves

The strongest primary comparison uses the fixed
\(P=5,N=16,M=256,R=128\) high-cubature PDE against the pooled
\(n=256,L=32,S=128\) exact ensemble. The PDE's \(N=16\to32\)
discretization difference is separately small
(\(2.05\times10^{-4}\) in output and \(8.45\times10^{-4}\) in Grams).
The direct PDE/reference discrepancies are:

\[
\max_t\|\Delta f(t)\|_2=1.0753\times10^{-2},
\]

\[
\max_{t,s}\|\Delta G(s,t)\|_F=1.9408\times10^{-2}.
\]

The preregistered pooled/stratified 95% thresholds are respectively
\(1.535/1.568\times10^{-2}\) for output and
\(2.920/2.898\times10^{-2}\) for absolute Grams. Thus neither secondary
full-curve discrepancy is resolved against exact-reference sampling error.

The maximum output discrepancy occurs at \(t=0\), where the finite exact
ensemble has a nonzero sample mean while the moment-matched PDE cubature has
the analytic zero mean.  Absolute Grams similarly carry independent
initialization noise.  After subtracting each curve's initial Gram, the
maximum discrepancy in training-induced Gram motion is

\[
7.2433\times10^{-3}.
\]

The PDE's feature motion is \(0.6338\), while the exact ensemble's is
\(0.6399\).  The increment discrepancy is therefore \(1.143\%\) of the PDE
feature motion. Its pooled and stratified 95% thresholds are
\(5.017\times10^{-3}\) and \(4.940\times10^{-3}\), with centered-bootstrap
tail probabilities \(0.00350\) and \(0.00200\). It is statistically resolved
under the frozen two-scheme decision rule.

The maximum occurs at \(t=8,s=1\), an original node of both depth grids.
It is block-stable: the three acquisition blocks give Gram-increment gaps
\(0.00808\), \(0.00617\), and \(0.00786\), and deleting any one block gives
\(0.00673\)--\(0.00785\). The prior \(S=64\) result was
\(0.00673\) against a \(0.00739\) threshold; the held-out data did not drive
the gap toward zero, while the uncertainty contracted enough to resolve it.
The maximum gap between the PDE loss and the loss of the exact mean predictor
is \(1.85\times10^{-3}\), which is not resolved.

The final held-out ordered-grid audit adds two materially different
references:

| PDE/reference | Gram-increment gap | curvewise 95% threshold | decision |
|---|---:|---:|---|
| P5 vs pooled \(n=256,L=64,S=64\) | \(6.564\times10^{-3}\) | \(7.073/7.112\times10^{-3}\) | not resolved |
| P5 vs \(n=512,L=32,S=16\) | \(9.897\times10^{-3}\) | \(9.216\times10^{-3}\) | narrowly resolved |
| P15 vs pooled \(n=256,L=64,S=64\) | \(8.481\times10^{-3}\) | \(7.073/7.112\times10^{-3}\) | resolved |
| P15 vs \(n=512,L=32,S=16\) | \(1.173\times10^{-2}\) | \(9.216\times10^{-3}\) | resolved |

The signed preregistered P5-minus-P15 closeness statistic is strictly
negative against all three pooled references. Its 95% intervals are
\([-0.00218,-0.00111]\) for \(n=256,L=32\),
\([-0.00230,-0.00039]\) for \(n=256,L=64\), and
\([-0.00250,-0.00129]\) for \(n=512,L=32\). Thus P15 is statistically
farther than P5 on every held-out finite-reference axis. This blocks a claim
that the present basis sequence monotonically converges toward the dense
curves.

The two exact Cauchy gaps themselves remain unresolved:
\(9.350\times10^{-3}\) for \(n=256\to512\) at \(L=32\), and
\(4.226\times10^{-3}\) for \(L=32\to64\) at \(n=256\). The available exact
grid is L-shaped and lacks the \(n=512,L=64\) corner, so neither result
establishes the ordered limit. Full preregistered details are in
`ORDERED_LIMIT_UPDATE.md`.

For the higher-cubature \(N=L=16\) PDE against the
\(n=64,L=16,S=64\) exact mean, the T=8 discrepancies are

\[
\max_t\|\Delta f(t)\|_2=2.56\times10^{-2},
\qquad
\max_{t,s}\|\Delta G(s,t)\|_F=4.79\times10^{-2}.
\]

They are again below the corresponding bootstrap thresholds
\(4.25\times10^{-2}\) and \(7.98\times10^{-2}\).

The \(m=2\) pilot tells the same qualitative story.  Depending on width and
cubature, its best stored discrepancies are about \(0.009\)--\(0.015\) in
output and \(0.020\)--\(0.022\) in Grams.  Those scales are comparable to
the ensemble SEM and observed width-to-width movement.  The \(m=2\)
\(P=4\to10\) QMC-512 difference is small
(\(5.69\times10^{-5}\) output and \(4.19\times10^{-4}\) Gram), but it is a
different sample count and does not replace the missing \(m=3\) cofinal
\(P\) study.

The statistically correct conclusion is therefore:

> The fixed PDE reproduces the qualitative curve shape and hidden feature
> motion to about one percent, but its initialization-cancelled Gram-motion
> curve is now statistically distinguishable from the finite
> \(n=256,L=32\) ensemble mean. The experiment does not yet determine whether
> that small difference vanishes under PDE refinement and the ordered
> width-then-depth limit.

## 4. Long-horizon and plateau audit

The long-horizon result is strong for the fixed PDE candidate.

From \(t=8\) through \(t=32\), the continued \(P=5,N=16,M=256,R=128\)
trajectory moves by at most

\[
5.00\times10^{-13}
\]

in output and

\[
4.24\times10^{-13}
\]

in hidden-Gram Frobenius norm.  The total earlier Gram motion is \(0.634\),
so the tail/total ratio is \(6.68\times10^{-13}\).  The loss at \(t=8\) is
\(1.25\times10^{-25}\) and reaches numerical zero.

The exact ensembles are already flat on \(t\in[4,8]\).  For example:

- pooled \(n=256,L=32,S=128\): mean output drift
  \(4.21\times10^{-7}\), mean Gram drift \(3.88\times10^{-7}\);
- \(n=256,L=64\): mean output drift \(5.73\times10^{-7}\), mean Gram drift
  \(5.44\times10^{-7}\).

Across individual seeds, the maximum \(t=4\to8\) output and Gram drifts in
these two ensembles are below \(2.77\times10^{-6}\) and
\(2.67\times10^{-6}\), respectively.

This rules out the interpretation that the PDE success is merely a
short-time Taylor fit: the same fixed PDE evolves through fitting and then
remains stationary for another 24 training-time units.  The direct
PDE-versus-exact comparison stops at \(T=8\), because no exact ensemble was
continued to \(T=32\).  The data therefore support global-in-simulated-time
plateau behavior, not a mathematical uniform-\([0,\infty)\) theorem.

## 5. Restart, identities, and integrity checks

The direct \(T=2\) PDE run and the serialized
\(T=1\) plus restart-to-\(T=2\) run agree to:

- \(3.42\times10^{-16}\) in output;
- \(6.30\times10^{-16}\) in Grams;
- \(4.44\times10^{-16}\) in every stored final-state array.

Across all readable archives:

- every stored numeric value is finite;
- the largest loss-identity defect is \(5.55\times10^{-17}\);
- the largest \(\dot{\mathcal L}=-e^\top\Theta e\) defect is
  \(4.44\times10^{-16}\);
- all PDE tangent kernels are positive definite, with minimum recorded
  eigenvalue \(1.53\);
- all stored mean and SEM arrays exactly equal recomputation from their raw
  ensemble members;
- Gram symmetry defects are at most \(2.22\times10^{-16}\).

The code's projected-hidden-energy diagnostic stays within
\(6.01\times10^{-5}\) of one.  This confirms an internal low-mode property
of the simulated state, but it is not a held-out test of all omitted
Hermite/response modes and should not be advertised as a proof of a small
operator tail.

An initial audit found that
`exact_ensemble_n96_L32_S48_seed2000_dt0p02_T8p0.npz` had been interrupted
before its ZIP central directory was written. The damaged copy was preserved
outside the release, the same deterministic 48-seed ensemble was regenerated
from the self-contained reference code, and the complete audit was rerun.
The current inventory reports every scanned archive as valid, with zero
salvaged and zero unreadable archives.

## 6. Depth-homogenization diagnostic

The paired-\(W\) conditional-variance experiment gives:

| Field | time | fitted log-log slope versus \(L\) |
|---|---:|---:|
| \(h\) | \(0\) | \(-1.019\) |
| \(h\) | \(0.5\) | \(-1.004\) |
| \(p\) | \(0\) | \(-0.999\) |
| \(p\) | \(0.5\) | \(-0.992\) |

All four small-sample 95% slope intervals contain \(-1\), and \(L\) times
the variance remains nearly constant from \(L=8\) to \(64\).  This is
specific, strong evidence for the required \(O(1/L)\) fast-layer
homogenization, both before and after training.

It is a necessary structural check, not a proof of the ordered
width-then-depth PDE limit or of Hermite-tail closure.

## 7. Claims that would currently overstate the evidence

The following formulations are not supported by the present experiment:

1. **“The PDE is numerically proven to equal the ordered dense limit.”**
   The finite-width/depth and finite-\(P\)/cubature errors are not separated,
   and the current PDE has a statistically resolved Gram-motion discrepancy.
2. **“Every PDE curve agrees within exact-reference noise.”**  Output, loss,
   absolute Grams, and tangent kernels do; the preregistered Gram-increment
   curve does not.
3. **“The resolved difference disproves the limiting PDE conjecture.”**  It
   compares one finite PDE discretization to one finite-\((n,L)\) mean and
   cannot identify which side supplies the bias.
4. **“The PDE converges to arbitrary accuracy as \(P,N\to\infty\).”**  There
   is clean \(N\) evidence and one clean nested P5/P15 step, but no cofinal
   \(P\) sequence; P15 moves farther from every pooled finite reference, and
   P35 changes the base cubature.
5. **“PDE numerical error is negligible.”**  RK4 error is negligible, but
   independent GH/QMC disagreement and finite-\(P\) effects are not.
6. **“Uniform all-time accuracy is established.”**  Plateau behavior is
   demonstrated through \(T=32\) for the PDE and \(T=8\) for exact
   ensembles, not for every time or every restarted neighborhood.
7. **“Near-unit projected energy certifies the omitted hierarchy.”**  It
   does not test all held-out operator, transpose-innovation, or
   high-to-low feedback modes.

The strongest accurate summary is:

> This is the first genuine width-independent operator-Galerkin neural-PDE
> simulation in the project.  It passes stringent algebraic, restart,
> refinement, nonlazy-feature, and plateau checks. Its output and absolute
> Gram curves are compatible with the current dense-network ensembles, while
> its approximately 1.14% Gram-motion error is now statistically resolved.
> P5 is statistically compatible with the deeper pooled \(n=256,L=64\)
> reference, and the held-out finite width/depth Cauchy gaps are unresolved;
> however, the L-shaped grid does not establish the ordered limit. P15 is
> consistently farther from every pooled reference. Determining whether the
> remaining error is finite-resolution or structural requires a full ordered
> reference rectangle and a cofinal nested-\(P\) experiment.

## Machine-readable outputs

- `inventory.csv`: archive hashes, shapes, metadata, and validation status;
- `data_integrity_checks.csv`: finite-value, PSD, symmetry, loss, and SEM
  recomputation checks;
- `pde_solver_convergence.csv`: all paired \(\Delta t,N,P,M,R\), method, and
  implementation comparisons;
- `qmc_replicate_summary.csv`: two- and three-scramble QMC uncertainty;
- `exact_ensemble_uncertainty.csv`: SEM and bootstrap curvewise uncertainty;
- `exact_limit_differences.csv`: width, depth, and independent-ensemble
  comparisons;
- `pde_reference_discrepancy.csv`: every stored \(m=2\) comparison and the
  main \(m=3\) comparisons;
- `plateau_tail_drift.csv`: tail drift, path length, residual, and
  tail/total ratios;
- `semigroup_checks.csv`: direct-versus-restart defects;
- `conditional_variance_by_depth.csv` and
  `conditional_variance_slopes.csv`: homogenization diagnostics;
- `headline_error_budget.csv`: selected scales in one compact table;
- `summary.json`: machine-readable run synthesis.
- `REFERENCE_NOISE_PREREGISTRATION.md`: frozen \(S=128\) protocol;
- `reference_noise_block_metrics.csv` and
  `reference_noise_block_pairwise.csv`: held-out and leave-one-block-out
  stability checks;
- `reference_noise_bootstrap.csv` and
  `reference_noise_bootstrap_distributions.npz`: all 4,000 frozen bootstrap
  results;
- `reference_noise_summary.json`: machine-readable held-out decision;
- `REFERENCE_NOISE_UPDATE.md`: focused interpretation of the resolved
  reference-noise test.
- `ORDERED_LIMIT_PREREGISTRATION.md` and `ordered_limit_update.py`: frozen
  held-out ordered-grid protocol and analysis;
- `ordered_limit_validation.csv`, `ordered_limit_curve_metrics.csv`,
  `ordered_limit_block_metrics.csv`, and
  `ordered_limit_pairwise_blocks.csv`: held-out integrity and blockwise
  results;
- `ordered_limit_one_reference_bootstrap.csv`,
  `ordered_limit_cauchy_bootstrap.csv`,
  `ordered_limit_cauchy_decisions.csv`, and
  `ordered_limit_pde_decisions.csv`: frozen uncertainty decisions;
- `ordered_limit_p15_improvement.csv`,
  `ordered_limit_p15_decisions.csv`,
  `ordered_limit_bootstrap_distributions.npz`, and
  `ordered_limit_summary.json`: P15 direction tests and machine-readable
  synthesis;
- `ORDERED_LIMIT_UPDATE.md`: focused held-out interpretation.
