# Independent internal check of the directional analysis

2026-10-10. This is an internal mathematical reconstruction check, not
promotion and not a review of any other study or the integrated theorem.

The lead assembled the candidate after three initially independent scoped
theoretical routes, then cross-checked their concrete outputs. A fresh
isolated reviewer read the complete two-file packet and required skills,
without the study README, prior reports, route discussion, or other studies.
The lead also checked all normalizations and the conditional Gaussian
calculation. No simulation or external theorem was used.

Final audited inputs:

- `DIRECTIONAL_COERCIVITY.md`, SHA256
  `c4ce45038d01256d2f16ef92059e09cff3efa8592fa2d2ea366dd0c78fbdef8c`.
- `LABEL_SCALE.md`, SHA256
  `1200de05dd2b3b5f6c785a2a4110950468bcaa50289f1fd4be2565980f5785d3`.

The reviewer read both original inputs completely, followed by the expressly
identified amended blocks. The final verdict was **PASS for the stated
deterministic identities, local results, and conditional fitting criteria**,
with no remaining mathematical correctness issue within this packet.

## Corrections and amendments checked

The initial review requested three clarifications, all applied and verified:

1. Width-asymptotic tail horizons require a fixed exponent, a
   width-independent positive rate constant and, for total rather than
   elapsed time, a width-independent upper bound on the onset time.
2. A lower bound on every weighted derivative moment gives a full tangent
   gap; a lower bound only on their residual-weighted average gives
   directional coercivity. These conclusions are now explicitly separated.
3. The cosine bad-state example has zero **top-layer** activation derivatives;
   its linear first activation has derivative one.

The reviewer separately verified two subsequent refinements: the
residual-weighted consequence of the last-block inequality, and the
direction-only window condition. For the latter, the vector is held fixed
at the beginning of the time window. This is precisely the vector used in
the proof, so the same contraction and path-length conclusions follow.

## Coverage and observed conclusions

- D1--D5: the normalized rate identity, negative residual-turning term,
  finite-time nonstationarity argument and residual-Hessian contraction
  have the correct signs and factors of `m`.
- D6--D7: feature and hidden-Jacobian contributions each give
  `2||grad s||^2/m^2`; together they produce the stated negative cubic loss
  correction and quartic scaling in a label multiplier.
- D8--D12: the target-cost liminf criterion, including the linear-cost-growth
  case, its converse, approximate-target sign and ridge order of limits
  are valid. They remain conditional on the explicitly stated cost bounds.
- D13: the dependent Gaussian decomposition, all three limiting acceleration
  entries and the negative leading contraction are correct. Activation
  parameters are fixed before taking width to infinity. The result is an
  initial increase of target representation cost, not a failure of fitting.
- D14--D16: the exact hidden-block contribution, tensor-product positivity,
  residual-weighted inequality, realizable rescue example, moment estimate
  and varying-cohort quantifiers are correct. Population density assumptions
  are not silently transferred to adaptive finite-width empirical laws.
- D17--D18 and D17-directional: the time-window contraction, exponential
  residual tail and finite metric path are valid under the stated bounds.
  Holding the starting residual direction fixed is essential to the stated
  relaxation and is explicit in the final text.
- D19--D20: the decay estimates, finite-path threshold `p<2`, residual-
  integrability threshold `p<1` and qualified polynomial horizon estimates
  are correct.

## What this check does not establish

It does not establish that Gaussian training satisfies any proposed
persistent-excitation, target-cost or residual-rate hypothesis. It does not
prove arbitrary-label multi-input fitting, unchanged all-time compression,
incompressibility, or eligibility for promotion. The final note and README
retain these limitations explicitly.
