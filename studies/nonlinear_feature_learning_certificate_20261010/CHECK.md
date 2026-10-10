# Fresh reconstruction and adversarial check

Date: 2026-10-10. This is an internal second derivation, not an independent
review.

## Scope audit

The counterexample uses two unit-sphere inputs in dimension one, fixed
arbitrary depth at least two, Gaussian initialization, zero readout, and the
paper's mobilities. Every activation is analytic and nonaffine. The last
activation is shifted but its derivative remains even. A sufficiently narrow
strip avoids the poles of `tanh`, so the activation and derivative envelopes
hold. The fixed positive label can be chosen below the paper's label cap.

For the last layer, the two population features are \(1+U\) and \(1-U\),
where \(U\) is a nonconstant odd function of a nondegenerate centered Gaussian.
Their Gram eigenvalues are \(2\) and \(2\mathbb E U^2\), so the required gap is
strictly positive. No assumption in the current compression scope excludes
antipodal inputs or equal labels.

## Direct flow reconstruction

Let the two predictions be \(a+b\) and \(a-b\). Opposite preactivations and
even activation derivatives make the two residual-free backward responses
equal. Substitution into the exact flow gives

\[
 \dot w=-2(a-\varepsilon)\mathbf 1-2bu,
\]

and makes every hidden velocity proportional to \(b\). At initialization,
\(b=0\). The only symmetry-breaking scalar is the empirical mean of the odd
last-layer feature. Conditional independence and centering give it variance
at most \(1/n\).

Over the complete trajectory, the paper's width-uniform real bounds give

\[
 \text{hidden path length}'\le C|b|,
 \qquad
 |b'|\le C\{\text{initial feature mean}
             +\text{hidden path length}+|b|\}.
\]

The exact even/odd output equations add a nonnegative hidden-kernel damping
term. Variation of constants, followed by a small-label bootstrap, makes the
time integral of the odd output and the complete hidden path length sampling
order. Both therefore vanish in probability uniformly for all training times.
Because the one-dimensional input sphere consists exactly of the two
antipodal inputs, this also covers every possible query in the counterexample.

Freezing the initial tangent kernel freezes the last-layer odd feature. Its
two scalar output equations have the same limiting system as the nonlinear
network. Both converge uniformly over all nonnegative times to
\(a(t)=\varepsilon(1-e^{-2t})\), \(b(t)=0\). This verifies that the example
simultaneously defeats hidden-motion and frozen-kernel-separation claims.

## Independent algebraic reconstruction of the onset identity

Use Euclidean mobility coordinates and split the prediction Jacobian into
hidden and readout blocks. At zero readout, the hidden block, the hidden
velocity, and the first time derivative of the readout block all vanish.
Writing \(A\) locally for the time derivative of the hidden Jacobian gives

\[
 \ddot\theta_{\rm hid}(0)=\frac2m A^\top y.
\]

Twice differentiating the tangent Gram, its hidden block contributes
\(2\|A^\top y\|^2\) in the label direction. Linearity in the readout and
equality of mixed derivatives show that the changing readout-feature block
contributes the same amount. Hence

\[
 y^\top\ddot K(0)y
 =4\|A^\top y\|^2
 =m^2\|\ddot\theta_{\rm hid}(0)\|^2.
\]

The nonlinear and frozen-kernel outputs have equal first and second
derivatives. Their third-derivative difference is
\((2/m)\ddot K(0)y\). Taylor's factor \(1/6\) therefore yields exactly

\[
 y^\top\{f_n(t)-f_{\rm NTK}(t)\}
 =\frac m3\|\ddot\theta_{\rm hid}(0)\|^2t^3+o(t^3).
\]

The sign is nonnegative and the coefficient vanishes precisely when the
aggregate initial hidden acceleration vanishes. This identity alone does not
give a width-uniform positive lower bound; such a theorem additionally needs a
positive limiting acceleration and a uniform Taylor remainder.

## Verdict

The negative result is decisive for the exact current scope. A positive
feature-learning theorem must add a condition that excludes the displayed
symmetry or directly lower-bounds the relevant hidden-response contraction.
The current top feature-Gram gap is insufficient. No paper wording or theorem
has been changed in this study.
