# Direct Gaussian Transport: Scope and No-Go

## Proposed route

One might push the initialization Gaussian measure through the finite-width
gradient ODE, write a Gaussian continuity equation for its law, and invoke a
DiPerna--Lions/Ambrosio-type regular Lagrangian-flow theorem.  If uniform in
width, that would provide existence, stability, and mesh removal without an
explicit response expansion.

## Audit conclusion

This is not a primary completion mechanism for the present mean-field
scaling.  The standard Gaussian transport hypotheses deteriorate with width
already on the nonlinear two-layer calibration rung:

1. the drift's Gaussian Sobolev norm and its divergence contain sums over
   `n` active coordinates and scale at least as `sqrt(n)` in the natural
   standardized source coordinates;
2. the negative Gaussian divergence contains unbounded products of Gaussian
   top weights with adaptive gate fields, for which the positive exponential
   integrability required by the standard compressibility theorem is not
   uniform and can fail outright at the demanded exponent;
3. the formal infinite-width drift is not Cameron--Martin valued when all
   source coordinates are retained;
4. projecting to empirical observables does not close the continuity
   equation, because persistent forward/transpose reuse creates tied Wishart
   and response words not determined by a finite marginal law.

These are hypothesis failures, not merely missing estimates in an otherwise
applicable theorem.  Rescaling the source coordinates can move the powers of
`n` between the drift and reference Gaussian covariance but does not create a
uniform Cameron--Martin/Sobolev estimate.

## What survives

Gaussian transport may still be useful **after** a cavity/traffic calculus has
already established uniform reachable Sobolev and divergence certificates.
At that point it can package uniqueness or stability of a projected limiting
flow.  It cannot produce the missing adaptive-source control by itself, and
using it as the main theorem would assume the heart of the target in its
hypotheses.

Claim level: direct theorem invocation is falsified for the present scaling;
transport remains a conditional downstream wrapper.

