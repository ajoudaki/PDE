# Global-proxy reference analysis

This directory is the offline postprocessor for a finite-width global-curve
reference.  It does not discover run directories, run a network, inspect a
scientific result on import, or choose a parameter point.  An explicit
`summary.json` and its frozen configuration are required.

The original Stage-2 campaign produced no analyzable scientific NPZ: its first
neural point stopped fail-closed because the declared physical-time horizon
could not reach the final output node.  That branch remains closed.  The
separately named successor-02 protocol now has a machine-readable, pre-run
analysis contract.  `pilot_runner.py` consumes that contract without changing
or reinterpreting the original run.

Before opening any NPZ, the runner checks the production config, successor
protocol, analysis document, production unlock, current reference sources,
summary, exact point set, and every recorded SHA-256 binding.  It then runs
exactly the frozen 2,000 whole-pair resamples for each point and the three
separately seeded two-width trend bootstraps.  Raw trajectories and bootstrap
samples are never rewritten.

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

## Frozen successor-02 entry point

After a complete, hash-bound scientific run exists, invoke:

```bash
python studies/stieltjes_conjecture/numerics/global_proxy_campaign/analysis/run_frozen_pilot.py \
  --summary studies/stieltjes_conjecture/numerics/global_proxy_campaign/reference/runs/canonical_pilot_successor02_20260813/summary.json \
  --config studies/stieltjes_conjecture/numerics/global_proxy_campaign/reference/configs/FROZEN_SUCCESSOR_02.json \
  --analysis-config studies/stieltjes_conjecture/numerics/global_proxy_campaign/reference/configs/FROZEN_SUCCESSOR_02_ANALYSIS.json \
  --output studies/stieltjes_conjecture/numerics/global_proxy_campaign/reference/runs/canonical_pilot_successor02_20260813/analysis_result.json
```

The output is one compact JSON certificate containing input/source hashes,
bands and width unions, every rational and Taylor comparison, paired
step-halving, ordinary/output-clock overlap, projection and diagnostic trends,
the Stage-2 resolution gate, per-prefix classifications, and the exact overall
three-way result.  The writer refuses to overwrite an existing result.  Any
provenance or numerical-analysis failure emits only an inconclusive failure
certificate and a nonzero exit code.

## Synthetic verification

No scientific trajectory is read by the test suite.  From the repository
root:

```bash
pytest -q studies/stieltjes_conjecture/numerics/global_proxy_campaign/analysis/tests
```

The fixtures verify hash-gated ingestion, validation-only rejection,
pair-lineage resampling, reproducible simultaneous bands, exact recovery of a
known `1/n` width limit, rational/Taylor accounting, exact coarse-lineage
restriction for step halving, trend intervals, projection/overlap gates, and
fail-closed verdicts.  They use synthetic arrays only.
