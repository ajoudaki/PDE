# Internal check of the compatible-data theorem

Date: 2026-10-10. This is a fresh author-side reconstruction, not an
independent review.

Revision note: this earlier author check overlooked the distinction between
scalar analyticity and Fréchet smoothness on the population \(L^2\) space.
The fresh scoped reports `AUDIT_ACTIVITY.md` and `AUDIT_TIME.md` identified
that gap and supplied strong directional little-o expansions. The repaired
`COMPATIBLE_RESULT.md` now uses those expansions, exact normalization, an
explicit transpose-conditioning calculation, and the parameter-norm transfer.
The originally asserted higher-order big-O remainders are not retained.

## Algebraic reconstruction

At zero readout, all hidden velocities and all feature velocities vanish.
Let \(B_a^{(\ell)}\) be the initial time derivative of the backward response,
with the harmless common factor \(2/m\) removed. Direct differentiation gives

\[
 B_a^{(L)}
 =\left(\sum_b y_bH_b^{(L)}\right)\phi_L'(Z_a^{(L)}),
\qquad
 B_a^{(\ell)}
 =\phi_\ell'(Z_a^{(\ell)})
   (W_0^{(\ell+1)})^*B_a^{(\ell+1)}.
\]

Full Gaussian support and nonaffinity make the top response Gram positive.
The conditional fresh component of each reused Gaussian transpose propagates
positive definiteness down through every layer. This checks the only delicate
dependence issue: the transpose is not replaced by an independent matrix.

The exact hidden accelerations are

\[
 \ddot W^{(1)}(0)=\frac4{m^2}\sum_a y_aB_a^{(1)}v_a^\top,
\]

\[
 \ddot W^{(\ell)}(0)
 =\frac4{m^2n}\sum_a y_aB_a^{(\ell)}
                    h_a^{(\ell-1)}(0)^\top
 \quad(\ell\ge2).
\]

Their squared mobility norms are positive multiples of the Schur products
displayed in the main proof. Pairwise nonparallel inputs are used only to make
the first forward Gram positive. For the first weight block, the input Gram
itself may be singular; its unit diagonal and the positive response Gram still
make their Schur product positive definite.

For the feature claim, let \(R_a^{(\ell)}\) be the preactivation acceleration.
Pairing its forward recursion with \(y_aB_a^{(\ell)}\), then using the exact
adjoint recursion, yields

\[
 \sum_a y_a\mathbb E[B_a^{(\ell)}R_a^{(\ell)}]
 =\frac{m^2}{4}\sum_{j\le\ell}
   \|\ddot W^{(j)}(0)\|_{\rm mob}^2,
\]

with normalized population pairings and the first-row mean-square/later
Hilbert--Schmidt mobility norms. Every term is nonnegative and every block acceleration is
nonzero, so the left side is positive. This rules out cancellation between a
layer's learned-link motion and propagated lower-layer motion.

The feature acceleration is
\(\phi_\ell'(Z_a^{(\ell)})R_a^{(\ell)}\). Analytic nonaffinity makes
\(\phi_\ell'\ne0\) almost surely under each initial Gaussian marginal, so a
nonzero preactivation tuple cannot be killed by the activation derivative.

The fixed-positive-time conclusion uses the maintained local fixed-depth
population theorem, rather than a width-uniform complex Taylor disk. That
theorem gives a width-independent real interval and uniform convergence of
the hidden path laws. Strong directional expansion is performed along the
population flow; strict population inequalities are then transferred back to
finite width. This avoids incorrectly treating the compression paper's
shrinking complex radius as width independent.

As a deterministic algebra check, the acceleration and adjoint recursions were
evaluated directly for seed 7 with \(m=d=3\), \(n=64\), four hidden tanh
layers and three nonzero labels. At layers one through four, the absolute
difference between the two sides of the finite-width version of the adjoint
identity was respectively

\[
 6.94\cdot10^{-18},\quad0,\quad1.39\cdot10^{-17},\quad0.
\]

This checks the normalization and cancellation identity numerically; it is not
used as evidence for the positivity theorem.

Finally, the previously derived exact identity

\[
 y^\top(f_n-f_{{\rm NTK},n})
 =\frac m3\|\ddot\theta_{\rm hid}(0)\|^2t^3+o(t^3)
\]

has a positive limiting coefficient because every hidden block contributes a
positive amount. The sign and factor \(m/3\) were recomputed directly from
the tangent-Gram differential equation.

## Adversarial boundary checks

- Affine activations fail because their derivatives do not generate a
  full-rank response Gram. They are explicitly excluded.
- Constant activations are affine and therefore excluded.
- Approaching parallel or antiparallel inputs can send the lower bounds to
  zero. No uniform geometric constant is claimed.
- A nonzero label vector is enough for layerwise activity. It is not enough to
  force every individual sample to move; a zero-labelled orthogonal component
  is a counterexample to that stronger statement.
- Gaussian second-moment normalization does not prove activity. It only keeps
  the initial marginal variances at a fixed scale.
- The result is local in physical time. It certifies the regime and rules out
  frozen-kernel equivalence; it does not claim a positive lower bound on
  feature displacement at the fitted endpoint.

## Verdict

The compatible-data theorem is algebraically consistent with the paper's
network normalization and mobility scaling. Its Gaussian conditioning step is
the established forward/transpose action calculation used in the maintained
book. The result remains author-derived and has not undergone an independent
promotion review.
