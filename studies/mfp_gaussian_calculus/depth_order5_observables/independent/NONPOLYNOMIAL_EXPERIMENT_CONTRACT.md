# Preregistered smooth-nonpolynomial regression for the `Gamma_04` head

**Status:** frozen before the population prediction is evaluated and before
the regression is run.

## Decision question and hypotheses

For the normalized sine activation

\[
 \phi(x)=\frac{\sin x}{\sqrt{(1-e^{-2})/2}},
\]

does the frozen deterministic head predict the large-width intercept of the
exact finite-width hidden-layer quantity

\[
 \Gamma_{04,n}^{H}=n^{-1}\langle X_H^{(0)},X_H^{(4)}\rangle
\]

at hidden depth `H=2`?  This activation preserves every unit forward Gram,
is smooth and nonpolynomial, and has nonzero derivatives of arbitrarily high
order.

`H1` is the frozen-head population prediction.  `H0` is that an omitted
equality/transpose-response branch produces a different intercept.

## Pre-experiment validity gate

Before any population comparison, two independently implemented finite-width
ordinary-series oracles must agree seedwise through feature order four at
widths `1,2,5` for a polynomial activation.  The frozen head must also agree
exactly with the independently canonicalized population compiler at depths
`H=1,2,3,4`.

## Primary design and metric

Use widths `n=(16,32,64,128)` and independent standard-Gaussian networks with
sample counts `(1200,800,400,150)`.  The seed blocks and exclusion rules are
fixed in the runner before the first prediction is loaded.  For every
network compute the exact ordinary power-series jet, not finite differences.

At each width estimate the mean and its standard error, then fit

\[
 \mathbb E\Gamma_{04,n}^{H}=\gamma_{04}^{H}+c_1/n
\]

by inverse-variance weighted least squares.  The primary statistic is

\[
 z=\frac{\widehat\gamma_{04}^{H}-\gamma_{04}^{H,\mathrm{GNF}}}
          {\operatorname{SE}(\widehat\gamma_{04}^{H})}.
\]

## Gates, decision rule, and stopping

All samples must be finite.  A chi-square fit p-value below `0.01`, a seedwise
oracle failure, or fewer than 95% valid samples makes the result
inconclusive.

- Pass: every validity gate passes and `|z| <= 3`.
- Fail: every validity gate passes and `|z| > 5`.
- Inconclusive: otherwise.

No activation, layer, width, fit model, threshold, or sample count may be
changed after prediction inspection.  The hard budget is 2,550 networks;
there is no adaptive extension branch.

## Claim consequence

A pass supplies empirical finite-width support only.  It does not prove the
equality-partition contraction or the uniform-integrability bridge.  A fail
rejects the current witness or scaling bridge, not the existence of some
other finite observable head.
