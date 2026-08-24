# GPU first-passage cooperative-drift audit

**Status:** completed under the frozen preregistration on 23 August 2026.

## Frozen verdict

The experiment is **inconclusive under its preregistered formal rule**:

- `eligible = false`;
- `formal_support = false`;
- `evidence_against = false`.

The decisive cell was feature horizon \(T=4\), threshold \(L=2\), and width
\(n=4096\).  It contained 2,430 first passages but only 4 first passages in
the open-and-misaligned state.  The frozen rule required at least 25 such
events.  The rarity that motivated the mechanism therefore also prevents the
experiment from formally adjudicating it.

## Diagnostics at their actual claim level

Across the four primary widths \(512,1024,2048,4096\), the \(L=2\) cells had
9,648 first passages and 26 open-and-misaligned passages.  Every one of those
26 exceptional passages had positive cooperative drift at the crossing.  At
\(n=4096\), the four exceptional passages had median resolution time \(0.14\),
median opposing-bath ratio \(0.0718\), zero median occupation of both the
open-misaligned tube and the stricter opposing slow tube, and no observed
occupation of the stricter tube.

At \(L=1.5\), there were 32,066 primary-run passages and 113
open-and-misaligned passages.  Cooperative drift was positive in all but one
of the 113; the width-4096 fraction was \(24/25=0.96\).  The width-4096 median
resolution time was \(0.16\), and median occupation of both tubes was zero.
At \(L=3\), there were 111 primary-run passages and none was open and
misaligned.

These observations are **diagnostically consistent** with rapid alignment or
gate closure, and they provide no sampled example of a persistent opposing
slow tube at \(L=2\).  They do not estimate the rare-event probability well
enough for the frozen formal criterion, and they prove no stopping-time,
Orlicz, convergence, or contract statement.

## Numerical audits

- All output files record the preregistered simulator hash
  `dab03c5944bf7cc30b052d73d2e684cab3f4b5af6b1eb37bd0a323e5f8ec91fa`,
  which matches the preserved simulator.
- The common-draw step-halving audit had maximum probability discrepancy zero,
  maximum median-resolution discrepancy \(0.0025\), and zero occupation
  discrepancy, all below the frozen tolerances.
- The common-draw float32/float64 audit had zero probability discrepancy,
  median-resolution discrepancy below \(6\times10^{-9}\), and zero occupation
  discrepancy.
- Maximum algebraic residuals were \(1.14\times10^{-6}\) in float32 and
  \(4.45\times10^{-16}\) in float64, below the frozen \(10^{-4}\) and
  \(10^{-9}\) limits.
- The centered finite-difference diagnostics had maximum relative discrepancy
  below \(3.90\times10^{-4}\) in float32 and \(1.46\times10^{-10}\) in
  float64.

The machine-readable result is
`GPU_FIRST_PASSAGE_COOPERATIVE_RESULTS_2026-08-23.json`; the raw `.npz`
outputs, simulator, analyzer, and frozen preregistration are preserved beside
this report.
