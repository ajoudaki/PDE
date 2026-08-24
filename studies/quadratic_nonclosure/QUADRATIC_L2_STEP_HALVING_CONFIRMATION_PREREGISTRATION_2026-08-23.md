# Quadratic L=2: separately declared step-halving confirmation

**Frozen after the primary grid was evaluated and before this confirmation
was run:** 23 August 2026.

This is not folded retroactively into the preregistered primary verdict.  The
primary experiment remains formally inconclusive because its paired
maximum-predictor gate was (0.0100)--(0.0124) at four widths, against a
frozen cutoff of (0.0100).  All other primary numerical gates passed.  The
successive Euler discrepancies contracted by factors (2.01)--(2.02), so a
single, narrowly scoped numerical-resolution confirmation is justified.

## Frozen confirmation

Run only the new step size

\[
 \Delta=0.000625
\]

for the unchanged widths (128,256,512,1024,2048), keys (8101,ldots,8106),
initialization salt `20260824`, exact quadratic architecture and simultaneous
metric-GD update, and horizon (T=2).  There is no new width, seed,
normalization, clipping, or scientific threshold.

Compare the new trajectories against the already frozen
\(\Delta=0.00125\) trajectories.  The confirmation passes only if:

1. every new trajectory is finite through its first (f=.95) crossing or
   through (T=2);
2. at every width, the 95th percentile paired maximum predictor discrepancy
   is at most (0.01);
3. median paired hitting-time discrepancies are at most (0.005) for
   (q=.25,.50,.75,.90);
4. the new fine-step loss never increases by more than (10^{-5}), and its
   median normalized one-step flow defect is below (0.01).

As a diagnostic rather than a pass condition, report the ratio between the
old \((.0025,.00125)\) and new \((.00125,.000625)\) maximum-discrepancy
medians.  First-order Euler convergence predicts a ratio near two.

If these gates pass, apply the *unchanged* primary width criteria to the new
fine trajectories.  This can establish a confirmatory qualitative result,
but does not alter the historical primary verdict.  No further step-size,
width, seed, or cutoff extension will be made in this experiment family.
