# Held-out ordered-limit reference audit

## Bottom line

The preregistered L-shaped finite-grid audit is complete, with no protocol
deviation and no PDE coefficient fitting.

Neither exact-network Cauchy step is statistically resolved:

| Exact comparison | Gram-increment sup | pooled \(q_{95}\) | stratified \(q_{95}\) | frozen decision |
|---|---:|---:|---:|---|
| \(n=256\to512\), fixed \(L=32\) | 0.009350 | 0.009967 | 0.010306 | not resolved |
| \(L=32\to64\), fixed \(n=256\) | 0.004226 | 0.008568 | 0.008978 | not resolved |

The depth result is strong evidence of stability at the available finite
grid: the gap is \(0.67\%\) of the approximately \(0.64\) feature motion.
The width result is sampling-limited: its gap is close to, but below, the
curvewise threshold and its maximum occurs early at \(t=0.28\), not at the
plateau.

Against the deeper pooled \(n=256,L=64,S=64\) reference:

- P5 has Gram-increment gap \(0.006564\), below pooled/stratified
  \(q_{95}=0.007073/0.007112\);
- P15 has gap \(0.008481\), above those thresholds.

Thus P5 is not statistically distinguished from this finite deeper
reference, while P15 is. This is evidence about two fixed PDE
discretizations and finite exact references, not proof that P5 is the
limiting PDE.

## Frozen data and validation

The preregistration and executable were hashed while both held-out paths
were absent:

- `ORDERED_LIMIT_PREREGISTRATION.md`:
  `59363300631483c0992f71c7b29c6e437fac32e768fc5de3225b01312ed69a47`;
- `ordered_limit_update.py`:
  `b22a39ebac2b0183399dec19a87e5910a60fafda2498185e6453ccc1660f6673`.

Held-out archives:

| Block | File SHA-256 | Runtime | Feature motion |
|---|---|---:|---:|
| \(n=512,L=32,S=16\), seeds 14000--14015 | `004a2a686565bfd29e7d552f427c2d27fb4e504f869de9bc50b7985812de54f0` | 2170.9 s | 0.635114 |
| \(n=256,L=64,S=48\), seeds 12000--12047 | `b8ee6f4637a3dee51a43e24e631de554f0726f2fbc63efbe1606f1063cce67f0` | 1376.9 s | 0.637155 |

Both pass full ZIP decompression, exact metadata/seed/time-grid validation,
bitwise recomputation of every stored mean and SEM, finiteness,
Gram/tangent-kernel symmetry and PSD, and loss monotonicity. Their minimum
individual Gram eigenvalues are \(0.831\) and \(0.700\); minimum
tangent-kernel eigenvalues are \(2.292\) and \(1.958\).

Both are operationally flat by \(t=4\). Mean \(t=4\to8\) output/Gram drifts
are \(3.53/3.15\times10^{-7}\) for the \(n=512\) block and
\(2.19/2.22\times10^{-7}\) for the new \(L=64\) block.

## Exact Cauchy comparisons

The primary statistic is

\[
D_G^{\rm inc}(A,B)
=
\max_{t,s}
\|[G_A(s,t)-G_A(s,0)]-[G_B(s,t)-G_B(s,0)]\|_F.
\]

Whole network trajectories were resampled for 2,000 replicates. The
two-sample bootstrap centers both independently resampled means around their
full means, so the thresholds include uncertainty from both sides.

| Comparison | observed | pooled \(p\) | stratified \(p\) | max location | terminal gap |
|---|---:|---:|---:|---|---:|
| width \(256\to512\) at \(L=32\) | 0.009350 | 0.0750 | 0.0905 | \(t=.28,s=.9375\) | 0.005441 |
| depth \(32\to64\) at \(n=256\) | 0.004226 | 0.6237 | 0.6167 | \(t=8,s=1\) | 0.004226 |

The new \(L=64,S=48\) block alone gives depth gap \(0.005340\); the old
\(S=16\) block gives \(0.004359\). Pooling them gives \(0.004226\).
The acquisition-block Gram-increment difference is \(0.006644\).

The three predeclared S16 slices of the new L64 block are visibly noisy:
their P5 gaps are \(0.010688\), \(0.005769\), and \(0.019690\), and their
pairwise Gram-increment distances range from \(0.010181\) to \(0.026588\).
This is why the pooled whole-trajectory uncertainty, rather than any
favorable subblock, controls the conclusion.

The two predeclared S8 halves of the \(n=512\) block give P5 gaps
\(0.011397\) and \(0.009634\), and their mutual Gram-increment distance is
\(0.008444\). The width result therefore remains reference-noise limited.

## P5 and P15 against every pooled reference

| PDE | Exact reference | seeds | Gram-increment gap | reference \(q_{95}\) | decision |
|---|---|---:|---:|---:|---|
| P5 | \(n=256,L=32\) | 128 | 0.007243 | 0.005062 / 0.004981 | resolved |
| P5 | \(n=256,L=64\) | 64 | 0.006564 | 0.007073 / 0.007112 | not resolved |
| P5 | \(n=512,L=32\) | 16 | 0.009897 | 0.009216 | narrowly resolved |
| P15 | \(n=256,L=32\) | 128 | 0.009202 | 0.005062 / 0.004981 | resolved |
| P15 | \(n=256,L=64\) | 64 | 0.008481 | 0.007073 / 0.007112 | resolved |
| P15 | \(n=512,L=32\) | 16 | 0.011730 | 0.009216 | resolved |

The P5-versus-\(n=512\) decision is modest rather than overwhelming:
observed/threshold is \(1.074\), with bootstrap tail probability \(0.0280\).
A separate fresh-seed 5,000-replicate sensitivity gave
\(q_{95}=0.009065\) and \(p=0.0284\), confirming the frozen result.

P5's gap decreases from \(0.007243\) at pooled \(L=32\) to \(0.006564\) at
pooled \(L=64\), but that change cannot be interpreted as a convergence
rate: the two exact references are finite, correlated through neither
seeds nor widths, and the L-shaped grid has no \(n=512,L=64\) corner.

## P15-versus-P5 direction

The signed preregistered improvement is

\[
I(E)=D_G^{\rm inc}(P5,E)-D_G^{\rm inc}(P15,E).
\]

All intervals are strictly negative:

| Reference | observed \(I\) | pooled 95% interval | stratified 95% interval | decision |
|---|---:|---:|---:|---|
| \(n=256,L=32,S=128\) | -0.001959 | [-0.002176, -0.001114] | [-0.002184, -0.001300] | P15 farther |
| \(n=256,L=64,S=64\) | -0.001917 | [-0.002298, -0.000412] | [-0.002296, -0.000393] | P15 farther |
| \(n=512,L=32,S=16\) | -0.001833 | [-0.002505, -0.001289] | not applicable | P15 farther |

So increasing from the fixed P5 to the fixed P15 PDE does not improve the
held-out finite-reference match. This conclusion is stable across the wider
and deeper references.

It is not evidence that an infinite-\(P\) PDE cannot converge. A clean
hybrid P5-to-P15 solver comparison moves the PDE curves by only
\(0.001124\) in output and \(0.002761\) in Grams, while an isolated P15
fast-cubature \(R=128\to256\) change moves them by
\(0.000604/0.000965\). These are genuine convergence diagnostics, but the
finite-reference direction shows that P5's current agreement is not
monotonically improved by the next basis level.

The complete-cubic P35 run uses a different base cubature size and latent
cloud from the clean M81 P5/P15 pair. It is valuable as a stress test but
must not be presented as the third point of a one-axis cofinal basis
sequence.

## Interpretation boundary

This is the available exact grid:

\[
(256,32)\longrightarrow(512,32),
\qquad
(256,32)\longrightarrow(256,64).
\]

It lacks \((512,64)\), a second width step, and a second depth step.
Consequently:

- the unresolved width and depth gaps are evidence of finite-grid
  compatibility, not proof that either gap is zero;
- the depth comparison is still at finite \(n=256\);
- the width comparison is still at finite \(L=32\);
- the P5/L64 non-rejection is not identification of the limit PDE;
- the P15-farther result concerns these displayed finite PDEs and exact
  references, not the existence of an accuracy-dependent PDE family;
- no \(1/n\), \(1/L\), or \(1/P\) extrapolation is justified.

The strongest honest conclusion is:

> The genuine P5 operator PDE remains quantitatively close to all held-out
> exact curves and is statistically compatible with the deeper pooled
> finite-network reference, while the exact width/depth Cauchy gaps
> themselves remain unresolved. The current data support finite-grid
> stability but do not establish the ordered limit. P15 is consistently
> farther from every pooled exact reference, so monotone basis convergence
> toward the dense-network curves is not demonstrated.

## Reproducible outputs

- `ORDERED_LIMIT_PREREGISTRATION.md`: frozen protocol;
- `ordered_limit_update.py`: analysis source;
- `ordered_limit_validation.csv`: file hashes and integrity/plateau checks;
- `ordered_limit_curve_metrics.csv`: all pooled deterministic metrics;
- `ordered_limit_block_metrics.csv`: acquisition, leave-one-out, and
  deterministic subblock results;
- `ordered_limit_pairwise_blocks.csv`: exact block heterogeneity;
- `ordered_limit_one_reference_bootstrap.csv`: exact-mean thresholds;
- `ordered_limit_cauchy_bootstrap.csv` and
  `ordered_limit_cauchy_decisions.csv`: two-sample width/depth tests;
- `ordered_limit_pde_decisions.csv`: P5/P15 classifications;
- `ordered_limit_p15_improvement.csv` and
  `ordered_limit_p15_decisions.csv`: signed closeness tests;
- `ordered_limit_bootstrap_distributions.npz`: all frozen bootstrap draws;
- `ordered_limit_summary.json`: machine-readable synthesis.

