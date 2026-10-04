# Significance challenge: the ensemble-size grid inflates the advantage

The completed primary screen passes its frozen powers-of-two grid, but that
grid excludes a materially cheaper ordinary competitor. This changes the
scientific interpretation: **a twofold advantage over strong cheap alternatives
is not established**, despite the registered 3.76-fold result.

Root identified the issue after reading the complete cost table. At width2048,
the Gaussian K=16 prediction estimate is0.002594, narrowly above0.0025. There
is no scientific reason to forbid averaging18 independent trajectories.

For an observable vector X from one trajectory, let V be its sample variance
(with squared norm averaged over observable entries), and let d² be the squared
distance of the16-run mean from the finite reference. The original estimator
for a fresh K-run mean is

    E_K = d² + (1/K - 1/16) V.

Conditional on a fixed independent reference, this is unbiased for expected
squared error for any positive integer K. Its square root is not unbiased;
neither is a minimum selected across estimated costs. K>16 extrapolates the
estimated bias and variance, rather than directly measuring a fresh ensemble.
Reference uncertainty and finite-width bias remain as in the primary report.

Applying exactly this estimator to all integer K=1,...,256 gives:

| Cheapest estimated eligible choice | Width | K | Cost | Prediction RMS | Gram RMS |
|---|---:|---:|---:|---:|---:|
| Gaussian |2048|18|12.5657s|0.00243114|0.00126213|
| Fast quarter-circle |16384|3|7.43971s|0.00225777|0.00124794|

The estimated speedup is **1.689**, below the twofold significance criterion.
The K=18 competitor needs only two more replicas than the largest registered
ensemble. Thus the earlier bootstrap's1000/1000 twofold successes describe the
restricted search grid, not robustness to this ordinary alternative.

This is a post-result analytical challenge, not a newly preregistered campaign,
fresh18-run measurement, or proof that the true speedup is1.689. No new GPU
experiment or bootstrap was run. The calculation is enough to withdraw the
broader twofold interpretation and keep this route at supporting-application
level. More candidate widths, better variance reduction, and different kernels
could change the optimum further. The frozen primary result remains preserved.

Producer: [analyze_population_cost_integer_grid.py](analyze_population_cost_integer_grid.py).
Run with the existing conda Python from the repository root; its output directory
must be fresh. Evidence is
data/generated/response_memory_fast_mixing_20261002/population_cost_integer_grid01/integer_grid.json,
including input/producer hashes and every condition. An independent algebraic
ceiling formula checked each loop-selected minimal K. This analysis has not
received independent review. No further experiment follows by default.
