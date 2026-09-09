# Preregistered exploratory calculation

The calculation below is mechanism-finding only and cannot certify the
two-hidden-layer theorem.

## Proxy

Use the exactly decoupled one-hidden-layer particle recursion

\[
 a^+=a+h\phi(z),\qquad z^+=z+h a\phi'(z),
 \qquad (a_0,z_0)\sim N(0,I_2),
\]

and `F_N(h)=E[a_N phi(z_N)]`.  Compare the common-initialization fine and
coarse schedules at `h=rho/t`.

## Fixed candidates and controls

- identity;
- `(x+lambda sin(x^3))/RMS`, `lambda=0.1,0.25`;
- `(x+lambda sin(x^5))/RMS`, `lambda=0.05,0.1`.

Use `rho in {0.02,0.05}`, horizons through the largest finite value before
floating-point overflow, and at least `2^20` fixed-seed Gaussian particles.

## Decision rule

- A growing high quantile with a sample mean dominated by the largest few
  particles is evidence of a rare-tail mechanism, not evidence for an
  expectation lower bound.
- Stable means across increasing sample sizes provide evidence against the
  natural oscillatory candidate at the tested horizons, not a proof.
- No conclusion for the full `L=2` OMFP network may be drawn unless the
  response and lower-feature terms are controlled analytically.

