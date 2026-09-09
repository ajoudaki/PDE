# Protocol: depth-three linear network with frozen Gaussian readout

Status: frozen before the derivation, 20 August 2026.

## Canonical model

Use the standard equal-width, one-sample, three-hidden-layer identity network

\[
X=u,\qquad Z=n^{-1/2}WX,\qquad
T=n^{-1/2}VZ,\qquad f_n=n^{-1}A^TT.
\]

The entries of \(A,V,W,u\) are independent standard Gaussians at
initialization.  Freeze \(A\) for all time and train \(V,W,u\) with the same
unit block metric and feature generator \(n\nabla f_n\).  For physical time,
use

\[
\dot\theta=-\eta n\nabla_\theta(y_\star-f_n)^2
\]

over the trainable blocks only.

## Target

Determine whether the width-first output and MSE loss admit the same
autonomous, restartable, O(1) single-source IDE as the established
two-hidden-layer scalar-output model.

The closure may retain the realized frozen-readout norm at finite width, but
the limiting source and state must be deterministic and independent of
width.  The target is uniform convergence in probability on compact
physical-time intervals, followed by global analysis of the limiting
physical trajectory.

## Claim ladder

- C1: contracting the adjacent trainable matrix with the frozen readout gives
  an exact closed finite-width subsystem.
- C2: after a scalar normalization and constant feature-time change, that
  subsystem is exactly the two-hidden-layer characteristic.
- C3: Gaussian initialization gives precisely the same deterministic spectral
  source in the width limit.
- C4: the inherited IDE generates the actual frozen-readout depth-three MSE
  loss on compact physical horizons and globally in limiting physical time.

## Non-vacuity and falsifiers

The proof may not replace the random readout by its mean.  It must condition
on the realized readout and show that only an accessible scalar statistic
survives.  A surviving dependence on the readout orientation, on the
orthogonal rows of \(V\), or on an \(n\)-dimensional evolving operator would
falsify the proposed witness.

The fully trainable depth-three model is outside this contract.  Freezing the
readout is a genuine model restriction and any term restored by training it
must be displayed explicitly rather than hidden in the claim boundary.
