# Preregistered normalized-sine Gamma_04 regression

Frozen before generating the Monte Carlo data.  The symbolic Gamma_04 JSON
hash is
`724da08f11bc3ec71b90ad12305a5e1ebed4f00a2a7e116f99f7d6ce02a401b5`.

## Decision question

Does the independently contracted post-R3 head predict the annealed
large-width fourth derivative of the hidden squared RMS in a genuinely
nonpolynomial, two-hidden-layer network?

## Hypotheses and mechanism

- H1: the frozen M-only head is the population limit.  At hidden depth
  H=2, layer l=2, normalized sine therefore has
  `Q4 = -2454.0373996768317`.
- H0: an omitted equality/transpose-response family produces a different
  large-width intercept.

H=2 is the smallest test with a hidden matrix, its transpose in backprop,
and a nontrivial post-R3 response.  B=1 and unit input Gram preserve the
scope of the claimed recurrence.

## Primary metric

For each network, compute `Q_2^(4)(0)` by the exact ordinary-series solution
of feature ascent, not by finite differencing.  At widths
`n=(32,64,128,256)`, use 2,000 independently seeded networks per width.  Fit
the four sample means to `alpha + beta/n` by weighted least squares with the
empirical standard errors of the means.  The primary statistic is
`z=(alpha-Q4_prediction)/SE(alpha)`.

`Q_l^(2)`, `Gamma_04`, and the first hidden layer are frozen secondary
diagnostics; they do not change the primary decision.

## Gates and decision rule

- Pass: `|z| <= 3` and the weighted affine residual goodness-of-fit p-value
  is at least 0.01.
- Fail: `|z| >= 5` with goodness p at least 0.01, or the conditional
  replication below again has `|z| >= 3` with the same sign.
- Inconclusive: any overflow/nonfinite derivative, goodness p below 0.01,
  or `3 < |z| < 5` before replication.

If the first run is inconclusive solely because `3 < |z| < 5` or goodness
fails, the only authorized branch is 1,000 additional networks at widths
384 and 512 followed by one affine refit.  No other model, activation,
width, or fit order may be selected after inspecting results.

## Budget and reproducibility

Primary seeds are `17000000 + 100000*n + replicate`, for replicate
`0,...,1999`.  Conditional seeds use the same formula and replicates
`2000,...,2999`.  The hard budget is 10,000 networks.  Raw per-network
statistics, source hashes, and the exact command are retained.  A pass is
empirical support for this head on this test only; it is not the annealed
limit theorem.
