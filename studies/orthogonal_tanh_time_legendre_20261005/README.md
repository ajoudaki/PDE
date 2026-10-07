# Orthogonal tanh data: time changes and the angular storage exponent

Started 2026-10-05. Owner: the current Codex task. No shared-file edits,
training experiments, Git mutations, or delegated work are part of this study.

## Question and scope

Can a transformed training clock and Legendre polynomials substantially
reduce the compact model's storage power from `log(n)^(3d+2)` toward
`log(n)^d` or less? The reference is the same initialized canonical dense
network, with two width-n tanh hidden layers, zero initial readout, m
orthogonal sphere inputs in dimension d (m <= d), and small fixed labels
of arbitrary signs. The desired error is uniform over the input sphere
and all physical training times, including the fitted endpoint, at the
existing root-width scale.

The user permits relevant previous compression proofs as scientific inputs.
The particular inputs used here are the source-space and runtime definitions
in `studies/closure_sampling_20261003/STORAGE_QUADRATIC_IMPROVEMENT.md`
and the source dimension derivation in
`studies/closure_sampling_20261003/SPHERICAL_SOURCE_DIMENSION_ROUTE.md`.
The current Quarto index and notation, repository workflow, research skill,
rigorous-math skill, and canonical neural notation instructions were read.
Other concurrent studies are not inputs. Earlier conversation claims are
context, not proof dependencies.

## Current result and its limits

[RESULT.md](RESULT.md) proves a source-space obstruction directly for the
actual finite Gaussian initialization. For each fixed d >= 2, a fixed
linear space approximating the entire first-layer feature vector uniformly
over sphere queries to empirical RMS error O(n^-1/2) needs at least
`c_d log(n)^(3(d-1)/2)` dimensions with high probability. The space may be
chosen arbitrarily using every initialized neuron. Thus the result is not
a lower bound restricted to independent sampling.

The current construction retains a full quadratic metric on that space.
Consequently its all-retained storage has a lower scale
`c_d log(n)^(3d-3)`. No time reparameterization or temporal polynomial basis
can remove this initialization constraint. This obstructs the requested
reduction of the coefficient 3 to 1 within that construction.

This is **not** a lower bound for arbitrary autonomous predictors, nor for
their learned state alone when the quadratic metric is changed. In
particular the initialized predictor is zero: approximating its hidden
features is a stronger requirement than approximating predictions.
[TIME_AND_PREDICTION_ROUTES.md](TIME_AND_PREDICTION_ROUTES.md) separates
the time-coordinate issue from the possible observable-only escape route.

Status: author-derived proof, with the source hash, reconstruction checks,
and limitations recorded in [CHECK.md](CHECK.md). No independent promotion
review has taken place. No improved all-time predictor compressor is claimed.

## Next useful action

A substantial further reduction would need to avoid preserving the whole
hidden-feature source space, or avoid its full quadratic storage. The
orthogonal-data scalar onset formula identifies one possible route, but a
closed autonomous approximation controlling its subsequent nonlinear
feedback has not been established. Merely replacing Chebyshev by Legendre
or stretching training time cannot resolve that remaining question.
