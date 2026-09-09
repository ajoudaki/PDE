# Preregistered probe result

The exact finite-width simulator in `pilot_finite_width.py` was run with
common random initialization at widths `64,128`.  A second implementation,
`particle_omfp_probe.py`, directly followed the inverse-free Gaussian DAG and
carried the source Jacobians defining `rho` and `sigma`.

## Observations

- Identity and `x+0.25 sin(x)` behaved as stable controls.
- At total time `rho=0.005`, `x+0.25 sin(x^3)` was mostly control-like but
  had occasional paired discrepancies one to two orders larger than its
  median.
- `x+0.05 sin(x^5)` was strongly tail dominated.  In the finite-width run
  with 16 seeds, typical paired discrepancies were around `10^-3`, while
  individual values reached `2.5*10^-1` even at `rho=0.005`.  At `rho=0.05`,
  some trajectories overflowed and others reached magnitudes between
  `10^3` and `10^29`.
- In the Gaussian-DAG particle probe for `x+0.05 sin(x^5)`, `rho=0.005`,
  and the first fine pair (`t=1`), two independent 200,000-particle runs
  produced terminal lower Grams about `1.5*10^3` and `1.6*10^4`, and output
  estimates about `-1.7*10^16` and `-1.4*10^19`; the coarse one-step outputs
  stayed near `3*10^-2`.

## Interpretation under the preregistered falsifiers

The means do not stabilize across seeds and are carried by extreme
observations.  Therefore these numbers are **not** evidence for the value,
sign, or even practical Monte Carlo estimability of the width-first
expectation.  They do support the proposed rare-tail mechanism and reject a
typical-trajectory stability argument.  In particular, truncating the tails
would erase precisely the population that can decide the uniform theorem.

No theorem in the final status relies on this computation.

