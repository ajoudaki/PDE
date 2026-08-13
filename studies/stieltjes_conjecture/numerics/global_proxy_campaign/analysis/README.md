# Global-proxy reference analysis

This directory is the offline postprocessor for a finite-width global-curve
reference.  It does not discover run directories, run a network, inspect a
scientific result on import, or choose a parameter point.  An explicit
`summary.json` and its frozen configuration are required.

The current campaign produced no analyzable scientific NPZ: its first neural
point stopped fail-closed before arithmetic because the declared physical-time
horizon could not reach the final output node.  Under the frozen stopping
rule, that neural branch is closed.  This package therefore remains validated
infrastructure for a separately named future campaign; it must not be used to
rescue or reinterpret the closed run.

## Estimator and uncertainty

`reference_data.py` verifies NPZ hashes and preserves the adjacent antithetic
pair axis.  For every physical-flow bootstrap resample it recomputes the
resampled ensemble mean-output clock and then forms

\[
K_{\mathrm{eff},n}(y)
=\frac{\mathbb E[(1-f_n)K_n]}{1-\mathbb E[f_n]}.
\]

It never bootstraps a precomputed ratio or replaces this quotient by a product
of means.  `bootstrap.py` resamples whole pair lineages and constructs a
studentized max-absolute-deviation simultaneous band on the log-kernel scale.
Invalid common-grid resamples are counted and can be made an exact fail-closed
gate.

The same pass records:

- pair-kernel coefficient of variation and relative standard error;
- the squared-loss Jensen gap;
- stored output variance;
- transverse symmetry leakage when a multi-input engine supplies it.

## Width sensitivity

`width.py` implements the four frozen sensitivity views:

1. linear extrapolation in `1/n`;
2. linear extrapolation in `1/sqrt(n)`;
3. `1/n` after leaving out the smallest width;
4. the top width without extrapolation.

`union_width_estimates` takes their nodewise outer union.  The `1/n` central
curve may be used for error summaries, but the narrower band of a favored fit
cannot replace this union in a protocol decision.

## Proxy comparisons and decisions

`comparison.py` evaluates every accepted S-fraction level, every nested
lower/upper bracket, and every equal-information Taylor control on the common
output grid.  It reports sup-log kernel error, physical hitting-time error,
output and absolute-loss error, and the terminal `4 K(y_max)` rate error.  The
two fixed-parity rational subsequences are audited separately.

`decide_protocol_bracket` implements the frozen three-way rule:

- compatible only when the complete simultaneous sensitivity-union band is
  inside the rational bracket at every node;
- contrary only when all validity gates pass and the same signed escape is
  also present at both largest valid widths;
- inconclusive for overlap, missing replication, or any failed gate.

The generic `DecisionThresholds` API is for a future protocol that supplies
all numerical thresholds explicitly.  It intentionally has no scientific
defaults.

## Synthetic verification

No scientific trajectory is read by the test suite.  From the repository
root:

```bash
pytest -q studies/stieltjes_conjecture/numerics/global_proxy_campaign/analysis/tests
```

The fixtures verify hash-gated ingestion, validation-only rejection,
pair-lineage resampling, reproducible simultaneous bands, exact recovery of a
known `1/n` width limit, rational/Taylor accounting, and fail-closed verdicts.
