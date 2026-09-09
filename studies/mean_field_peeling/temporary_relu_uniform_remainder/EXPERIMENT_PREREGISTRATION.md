# ReLU kink-order probe (evidence only)

## Decision question

For the exact finite-width `q=1`, two-hidden-layer network, does the paired
defect `Delta_1(h)=E[f_2(h)-f_1(2h)]` contain a nonzero `h|h|` term, or does
the coarse/fine chronology cancel it so that the first term is cubic?

## Competing predictions

- `H_kink`: `Delta_1(h)/(h|h|)` approaches a nonzero width-stable value.
- `H_cancel`: that quotient tends to zero; `Delta_1(h)/h^3` is the first
  potentially stable quotient.

This test does not decide the all-`t` theorem and will not be presented as a
width-limit proof.

## Testbed and metric

Use the exact finite-width simultaneous ascent equations, RMS-normalized
ReLU and leaky ReLU, common initialization across the fine/coarse pair and
across all tested step sizes.  Test widths `32,64,128`, at least 4096 seeds,
and `h=0.04,0.02,0.01`.  Record means and standard errors of

`Delta/h^2`, `Delta/h^3`, and the oddness check
`(Delta(h)+Delta(-h))/h^2`.

## Validity gates

1. Every trajectory must be finite.
2. The oddness residual must be statistically compatible with zero.
3. A claimed order must have the same trend at the two largest widths and
   exceed two standard errors at two adjacent step sizes.
4. Failure of these gates is inconclusive.

## Branch and stopping rule

Run this single grid only.  Use its result solely to choose which analytic
boundary term to derive.  No searched activation or parameter grid is
allowed.
