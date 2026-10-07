# Internal reconstruction check

2026-10-07. This check is not promotion or a review of the integrated result.

Checked artifact: `LABEL_SCALE.md`, SHA256
`1200de05dd2b3b5f6c785a2a4110950468bcaa50289f1fd4be2565980f5785d3`.

A fresh isolated scoped reviewer read the complete candidate and required
proof/notation instructions, without the study README, route discussion,
other studies, or prior verdicts. The review covered all seven sections.
The lead also reconstructed the mean-loss factors and Gaussian calculation.

Verdict: **PASS for the restricted mathematical statements.**

- Global finite-time existence follows from the exact nonnegative-loss
  dissipation identity and the fixed positive mobility metric.
- The one-sample proof is correct, but it is a known baseline and not an
  answer to the user's multi-input question.
- The rank-one matrix identity, initial hidden acceleration, label-direction
  improvement, and relative-mobility change under label rescaling check out.
- The explicit nonglobal minima have positive initial population Gram gap.
  Gaussian capture probability at large width is not proved. The displayed
  equilibrium predictor itself has an exact width-one realization.
- For the nonlinear two-input Gaussian example, the coefficient `2Y^2`,
  conditional orthogonal Gaussian decomposition, conditional variance,
  random-covariance sample limits, eigenvector replacement and strict
  negative-sign argument all check out. The finite-width eigenvalue is
  simple and the inverse in the decomposition exists almost surely for
  `n>=2`.

One defect was found and corrected during review: the displayed initial
acceleration formula had lost the plus sign between its two contributions.
The later derivation already used the correct sum. The final hash above
includes the corrected sign and explicit simplicity/rank explanations.

No arbitrary-label multi-input fitting theorem, unchanged all-time
compression theorem, large-width Gaussian non-fitting counterexample, or
incompressibility lower bound is proved. The reviewer explicitly confirmed
that the note does not claim any of these. Correspondence with other book
or integrated-study passages was outside this isolated check's scope.
