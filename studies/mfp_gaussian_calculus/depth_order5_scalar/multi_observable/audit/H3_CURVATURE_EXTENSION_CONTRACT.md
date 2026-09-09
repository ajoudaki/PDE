# Pre-results extension of the hostile H=3 sine gate

**Frozen after the original three-width result was classified inconclusive and
before generating any width-512 sample.**

Date: 2026-08-19.

## Why an extension is necessary

The original hostile contract used widths `64,128,256` but required comparison
of an affine `1/n` extrapolation with an `intercept+1/n+1/n^2` extrapolation.
Three points saturate the latter model.  This is a design defect, not negative
evidence about the recurrence.  The original result and its inconclusive label
remain frozen.

## Added cell

- same normalized-sine activation, `H=3`, and observed layers `2,3`;
- one new width, `n=512`;
- exactly 1,024 independent networks;
- seed `23_000_000 + replicate`, `replicate=0,...,1023`;
- the same exact fourth-order jet oracle and the same four primary quantities;
- no sample exclusion except a recorded nonfinite value, which makes the panel
  inconclusive.

The allocation matches the original per-width allocation.  It was selected
before observing any width-512 value.  Existing widths and their raw values are
not replaced or reweighted except through their recorded standard errors.

## Frozen operational form of the old curvature gate

For each primary quantity fit, by inverse-variance weighted least squares,

\[
 m_n=\alpha+\beta/n
 \quad\hbox{and}\quad
 m_n=\widetilde\alpha+\widetilde\beta/n+\gamma/n^2.
\]

Call curvature both statistically resolved and materially consequential only
when

\[
 |\gamma|/\operatorname{se}(\gamma)>2
 \quad\hbox{and}\quad
 |\widetilde\alpha-\alpha|>
 2\max\{\operatorname{se}(\alpha),\operatorname{se}(\widetilde\alpha)\}.
\]

If both conditions hold for any primary quantity, the panel is
**inconclusive** and requires larger widths.  This explicitly instantiates the
original phrase “statistically resolved monotone curvature large enough to move
the intercept by more than two fitted standard errors.”  No threshold from the
original contract is relaxed.

The panel passes only if, for all four quantities:

1. the exact finite-width identity residual is at most `1e-9` for every
   regenerated old sample and every new sample;
2. all values are finite and the old raw panel is reproduced to scaled error at
   most `1e-12`;
3. `se(alpha) <= 0.10*max(1,abs(target))`;
4. the curvature condition above is false; and
5. `abs(alpha-target)/se(alpha) <= 4`.

If a primary `z` lies in `(3,6]`, the original contract's one permitted complete
independent replication remains mandatory before a final pass/fail decision.
This extension does not spend that replication unless the trigger occurs.

The result is empirical evidence only.  It cannot replace atomwise,
equality-partition, transpose-response, or uniform-integrability audits.
