# Preregistered jet-calibrated stopped-flow test

Frozen before computing any jet-corrected curves.

## Decision question

Can the already simulated canonical one-sample quadratic feature-ascent
trajectories yield a numerically calibrated finite-width proxy for the
mean-field function

\[
R(x)=\frac{K(\sqrt{x})-111}{x},
\]

accurate enough that a Loewner sign test is interpretable?

This tests a particular stopped, robust, finite-width witness.  It does not
test the existence of a Stieltjes measure unless all calibration gates pass.

## Canonical data and contract

Only the saved trajectories from the independent common-clock run are used:

- widths `64, 128, 256` and antithetic-pair counts `140, 70, 70`;
- feature times `0, 0.00005, ..., 0.003`;
- output nodes `y=(0.04,0.08,0.12,0.16)`;
- the canonical equations

  \[
  z=n^{-1/2}Wu^2,\quad f=n^{-1}\sum_i a_i z_i^2,
  \]

  \[
  a'=z^2,\quad
  W'=2n^{-1/2}(az)(u^2)^\top,\quad
  u'=4n^{-1/2}u\odot W^\top(az).
  \]

The finite-width expectation is not used: polynomial gradient ascent has a
positive-probability finite-time blow-up tail.  The empirical object is the
same stopped/robust typical-flow proxy as in the common-clock run, now with a
predeclared initialization control variate.

## Jet control variate

For each antithetic pair `r`, compute its exact finite-width Taylor jet from
the initialization equations, using ordinary Taylor coefficients.  If

\[
g_{r,n}(s)=c_{r,0}+c_{r,2}s^2+O(s^4),
\]

replace it by

\[
g^{\rm cv}_{r,n}(s)
=g_{r,n}(s)+(111-c_{r,0})+(842592-c_{r,2})s^2.
\]

Here `111=F'(0)` and `842592=F'''(0)/2` are exact audited mean-field
coefficients.  No positive-time trajectory value is used to choose the
correction.  The control variate therefore enforces `R(0)=68.386656927...`;
that equality is an implementation check, not independent evidence.

The next coefficient

\[
R'(0)=-6.844249882\ldots
\]

is *held out*.  It is not used in the correction.  Reproducing it is the
scientific calibration gate.

## Frozen estimators

Primary aggregation is seven-block coordinatewise median-of-means with the
old cutoff `111 sqrt(n)`.  Sensitivities are five blocks and the full
arithmetic mean.  The common clock is always constructed from the same
aggregated curve:

\[
F_n^{\rm cv}(s)=\int_0^sG_n^{\rm cv}(t)\,dt,
\qquad K_n^{\rm cv}(F_n^{\rm cv}(s))=G_n^{\rm cv}(s).
\]

For numerical stability, fit

\[
R_n^{\rm cv}(x)=R(0)+xq_n(x)
\]

over `0.02 <= F <= 0.18`, with primary polynomial degree three for `q` and
degrees two and four as sensitivities.  This representation imposes only the
calibration coefficient already used by the control variate.

The held-out estimate is `q_n(0)`.  Width extrapolations in `1/n` and
`1/sqrt(n)` are reported but neither may rescue a failed individual-width
gate unless they agree within their sampling uncertainty.

## Pass, fail, and inconclusive rules

1. **Implementation gate:** the fitted/extrapolated `R(0)` must differ from
   `68.386656927...` by at most `0.5%` for every primary width.
2. **Held-out coefficient gate:** at width 256, the primary estimate and its
   95% pair-bootstrap interval must contain `-6.844249882...`; degrees two,
   three, and four and five-/seven-block choices must agree in sign.  The
   interval width must be at most `10` (absolute units).
3. **Clock/fit gate:** all four output nodes are bracketed, the clock is
   increasing, fit maximum residual is below `5e-3`, and half-step effects
   inherited from the earlier run remain below the statistical scale.
4. Only if all three gates pass may the four-node Loewner matrices be called
   evidence.  A negative direction is a falsifier only if its discovery
   direction has a held-out 99% upper confidence bound below zero and the sign
   survives aggregation and fit-degree sensitivities.

Failure of any calibration gate makes the Loewner result **inconclusive**.

## Budget and stopping

- Reuse saved trajectories; regenerate initial conditions only to calculate
  exact order-five per-sample jets.
- At most `2000` deterministic pair-bootstrap resamples per reported width.
- No new trajectory simulation unless this first test passes its held-out
  coefficient gate.
- Stop after this gate decision.  Do not tune the fit window or nodes after
  seeing the result.

