# Preregistered exploratory computation

## Purpose

The computation is a mechanism discriminator, not a proof.  It tests whether
natural smooth residual oscillations exhibit a width-stable rare-tail growth
signal before a custom activation is attempted.

## Candidates fixed before running

After RMS normalization under `G~N(0,1)`:

1. `phi(x)=x` (control);
2. `phi(x)=x+0.25 sin(x)` (globally Lipschitz control);
3. `phi(x)=x+lambda sin(x^3)`, `lambda in {0.1,0.25,0.5}`;
4. `phi(x)=x+lambda sin(x^5)`, `lambda in {0.05,0.1}`.

## Grid and statistic

- `t in {1,2,3,4,6,8,12,16}`;
- `rho in {0.02,0.05,0.1}` and `h=rho/t`;
- common-random-number comparison of `F_{2t}(h)` and `F_t(2h)`;
- widths `n in {64,128,256}` with at least eight independent seeds;
- primary diagnostic: raw endpoint `Delta_t(rho/t)` and its width/seed
  stability;
- secondary diagnostic: subtraction of the explicit cubic coefficient
  computed by Gaussian quadrature from the established `L=2` formula.

## Falsifiers

- A signal that decreases with width or is carried by one seed is rejected.
- NaN/overflow is not evidence.
- Growth only after a fixed positive total-time instability is not a local
  counterexample.
- Failure of these natural candidates does not prove the conjecture; it
  redirects the search to a tailored activation.

## Success criterion

Only a reproducible trend of
`|Delta_t-kappa_t h^3|/(t^5 |h|^5)` increasing with `t`, stable across
widths and seeds, counts as evidence worth a proof attempt.

