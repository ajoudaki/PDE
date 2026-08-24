# Results: GPU high-moment middle-query audit

- All preregistered solver checks valid: **True**.
- Formal support criterion: **True**.
- Formal evidence-against criterion: **False**.

The table reports the cluster-bootstrap point estimate and 95% CI
for the moment-growth exponent of `R2`, followed by `m12/(2 m6)`.

| horizon | width | alpha (95% CI) | m12/(2m6) (95% CI) |
|---:|---:|---:|---:|
| 1 | 256 | 0.424 [0.416, 0.431] | 0.672 [0.668, 0.677] |
| 1 | 512 | 0.420 [0.409, 0.434] | 0.672 [0.664, 0.681] |
| 1 | 1024 | 0.412 [0.404, 0.419] | 0.666 [0.662, 0.670] |
| 1 | 2048 | 0.408 [0.399, 0.417] | 0.663 [0.658, 0.668] |
| 2 | 256 | 0.357 [0.350, 0.364] | 0.644 [0.640, 0.649] |
| 2 | 512 | 0.348 [0.341, 0.356] | 0.639 [0.635, 0.644] |
| 2 | 1024 | 0.346 [0.340, 0.352] | 0.638 [0.634, 0.641] |
| 2 | 2048 | 0.348 [0.341, 0.355] | 0.638 [0.634, 0.642] |
| 4 | 256 | 0.264 [0.260, 0.268] | 0.604 [0.602, 0.607] |
| 4 | 512 | 0.259 [0.256, 0.262] | 0.602 [0.600, 0.604] |
| 4 | 1024 | 0.259 [0.255, 0.262] | 0.602 [0.600, 0.604] |
| 4 | 2048 | 0.261 [0.256, 0.266] | 0.603 [0.600, 0.605] |
| 8 | 256 | 0.169 [0.167, 0.171] | 0.566 [0.565, 0.567] |
| 8 | 512 | 0.167 [0.166, 0.169] | 0.565 [0.565, 0.566] |
| 8 | 1024 | 0.167 [0.165, 0.169] | 0.565 [0.564, 0.566] |
| 8 | 2048 | 0.169 [0.167, 0.172] | 0.566 [0.565, 0.568] |

This experiment supplies empirical weight only.  In particular, a
support result does not prove the missing signed causal-predictor or
joint-leverage estimate and changes no theorem rung by itself.
