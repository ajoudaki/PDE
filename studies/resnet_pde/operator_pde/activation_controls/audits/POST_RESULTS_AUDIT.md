# Independent post-results audit

## Verdict

The sealed evidence and frozen decision rule support the analyzer's
`identity_only` verdict.

- Exact identity dynamics are decisively rejected by learned-Gram and output
  evolution in the sole confirmatory C2 case.
- The loss curve does not pass the stronger joint \(S>2E\) rule, although the
  user's weaker \(S>E\) inequality and the activation-contrast prediction do
  pass.
- The gain-matched L2 control remains below the 5% Gram tolerance. Therefore
  the experiment does not reject every linearization explanation.

## Independently checked central numbers

- C2 Gram separation from C0: 36.385%; one-sided 95% LCB 35.271%.
- Matched C2 PDE Gram error: 1.095%; one-sided 95% UCB 1.090%.
- C2 Gram \(S-2E\): one-sided 95% LCB 33.709%.
- Matched C0 PDE Gram error: one-sided 95% UCB 2.214%.
- C2 output separation: 12.707%; matched PDE error 2.917%; all four
  preregistered identity bounds pass.
- C2 loss separation: 9.891%; matched PDE error 4.988%, UCB 9.154%;
  \(S-2E\) does not pass.
- C2 versus L2 dense Gram separation: 3.458%, with 95% bounds 3.245% and
  3.670%. This tested linear surrogate is statistically confined below 5%.
- \(H-1.5E\): one-sided 95% LCB 1.792%, so the matched nonlinear PDE has the
  preregistered resolved advantage even though the full-nonlinearity rule
  fails.
- Equal-loss-progress C2-versus-C0 Gram separation: 27.136%, LCB 25.914%;
  clock-margin LCB 24.019%.

All PDE numerical discrepancies are below 1%. The \(L=64\) physical-depth
control passes. The \(n=256\) result remains diagnostic because it uses only
four paired seeds.

## Interpretation guardrails

The defensible wording is:

1. exact identity/deep-linear dynamics are rejected for Gram and output;
2. a broader effective-gain deep-linear explanation remains viable at 5%;
3. L2 is optimal only for the frozen initialization-Gaussian distribution,
   not over all times, depths, or adaptive linear surrogates;
4. the \(3.16\times\) point advantage over L2 is descriptive, while the
   preregistered inferential statement establishes an advantage greater than
   \(1.5\times\).

The processed analysis was rerun from the sealed raw archives and reproduced
all outputs byte-for-byte.

