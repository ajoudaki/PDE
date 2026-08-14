# FP32 Euler Stage V — completed numerical-method audit

Status: **FAILED / INCONCLUSIVE for (h=5\times10^{-6})**.  Both frozen
trajectories completed under their caps and matched closely at the curve
level, but the finer step failed four preregistered rounding/driver gates.
This is a numerical-method result, not evidence for or against the Stieltjes
conjecture.

## Frozen execution

The same hash-identical (n=8192) antithetic lineage was integrated to
(t=0.024) with explicit Euler in deterministic IEEE FP32:

| step | internal wall | elapsed | peak GPU | terminal mean output |
|---:|---:|---:|---:|---:|
| (10^{-5}) | 60 s | 15.251 s | 2.001 GiB | 0.99921325 |
| (5\times10^{-6}) | 120 s | 24.897 s | 2.001 GiB | 0.99907249 |

Through mean output (y=0.9), the symmetric maximum relative discrepancies
between coarse and fine curves were only

\[
2.03375\times10^{-4}\quad\text{for }K_{\rm eff},
\qquad
2.03837\times10^{-4}\quad\text{for the normalized-progress kernel},
\]

and (1.94\)--(2.19\times10^{-4}) for the three direct kernel components.
Thus ordinary plotted curves alone would have suggested excellent agreement.

## Why the fine point failed

The per-step audit showed the opposite trend:

| diagnostic through (y=0.9) | (h=10^{-5}) | (h=5\times10^{-6}) | fine gate |
|---|---:|---:|---:|
| max driver defect | 0.0008580 | 0.0033142 | fine improves coarse |
| RMS driver defect | 0.0001198 | 0.0003330 | (le0.003) |
| cumulative driver defect | 0.0000444 | 0.0002575 | (le0.001) |
| max unchanged (a) fraction | 0.05420 | 0.07544 | (le0.05) |
| max unchanged sampled-(W) fraction | 0.65076 | 0.75317 | (le0.75) |
| minimum sampled-(W) update cosine | 0.99510 | 0.98517 | (ge0.995) |

The fine point failed the driver-improvement, (a)-unchanged,
sampled-(W)-unchanged, and sampled-(W)-cosine gates.  Halving an FP32 step
therefore moved the computation farther into its rounding floor even though
the aggregate curve changed little.  No (h=2.5\times10^{-6}) retry is
allowed; older matched validation had already shown that it can be worse.

## Consequence for later work

The original Stage-V verdict remains failed and (h=5\times10^{-6}) is not
authorized for production.  A separate post-hoc engineering review found that
(h=10^{-5}) may be usable for a breadth-first panel with proxy gaps at least
2%, because:

- its fresh driver max/RMS/cumulative defects were
  0.0858% / 0.0120% / 0.00444%;
- its sampled-(W) update cosine was 0.99510 and aggregate norm ratios were
  within 0.011% of one;
- an independent matched (n=4096), eight-pair comparison with FP32 RK4 had
  0.0318% effective-kernel error through (y=0.9) and 0.1211% only after the
  (y=0.99) stress node was included.

This does **not** repair Stage V.  Any later (h=10^{-5}) campaign must be a
new, prospectively frozen successor, carry a conservative 0.20% nodewise
kernel envelope, add its measured cumulative-driver allowance to output/loss
bounds, and classify boundary contact as inconclusive.  It does not
automatically validate multi-input or hidden-observable comparisons.

## Provenance

- frozen source manifest:
  `a683d8403f3120c5dfe79e88d93607658dc01304a2616f368311187d6a8c4361`;
- local execution unlock:
  `28dd7ad5a3b5c4b338cb2c922bd526edc06a94f025cc24deeffe5084ac411850`;
- coarse manifest / raw arrays:
  `7df9a1fc9b7c5bf0a12e485f9543a127d69b9712433e43e3ab184cf41dffbbec` /
  `3fe09255efb6bb769d840ca6287a4ff06767c5fe95d3c5634b0c1fff51ca5d2b`;
- fine manifest / raw arrays:
  `2dc6bbf47a13cc637d29394d051f839587d579dfa148af5f000cc4f3f0035088` /
  `721d3b93275a1d4f6a0909ccd1f50ec93db0b78a437ac7db76d15e3432d0ad35`;
- exact decision JSON:
  `3f1c7adfe24b8f68f40ea87b26e77f6131a15bab1daf6393001e15aec3ea3117`.

Raw arrays remain ignored local artifacts.  The compact one-attempt ledger,
decision result, and point manifests are tracked; array hashes and all
decision-level scalars are preserved without adding binary trajectory data
to Git.
