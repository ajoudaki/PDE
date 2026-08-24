# GPU causal susceptibility-trace results

- Numerical audits valid: **True**.
- Frozen formal-support rule: **True**.
- Frozen evidence-against rule: **False**.
- These are empirical statements only; C3--C5 remain proof obligations.

## Main medians

| horizon | width | TV | signed | negative TV | half-probe discrepancy |
|---:|---:|---:|---:|---:|---:|
| 1 | 128 | 0.446334 | 0.446334 | 0 | 0.05997 |
| 1 | 256 | 0.459911 | 0.459911 | 0 | 0.02284 |
| 1 | 512 | 0.453111 | 0.453111 | 0 | 0.01919 |
| 2 | 128 | 0.702499 | 0.702499 | 0 | 0.04112 |
| 2 | 256 | 0.71822 | 0.71822 | 0 | 0.02551 |
| 2 | 512 | 0.706102 | 0.706102 | 0 | 0.01234 |
| 4 | 128 | 0.972473 | 0.972473 | 0 | 0.04789 |
| 4 | 256 | 0.956008 | 0.956008 | 0 | 0.03399 |
| 4 | 512 | 0.990734 | 0.990734 | 0 | 0.02011 |

## Frozen fits

- T=1 width slope: 0.0109, 95% CI [-0.0033, 0.0402].
- T=2 width slope: 0.0037, 95% CI [-0.0436, 0.0419].
- T=4 width slope: 0.0134, 95% CI [-0.0437, 0.1041].
- T=4, n=128 mesh-divergence exponent: -0.0281, 95% CI [-0.1007, 0.0963].
- Pooled half-probe discrepancy: median 0.0312, 95th percentile 0.0918.

## Mechanism diagnostic

Across all main orbit/time coefficients, the negative fraction was 0; the observed range was [0.00212733, 0.018908].  This motivates, but does not establish, a positivity/passivity proof search.
