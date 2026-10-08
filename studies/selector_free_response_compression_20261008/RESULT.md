# A more intrinsic nonlinear reduction: what closes and what does not

There is an elegant exact reduced dynamical skeleton, but not yet a
cheaper same-scope replacement for coordinate selection. The open issue
is how to encode its nonlinear law, not the consistency of forward and
backward propagation.

## One potential, two consistent operations

At one layer, let \(U\in\mathbb R^{n\times R}\) be a fixed basis for
the source space, normalized by \(U^\top U/n=I\). For reduced
preactivation coordinates \(z\in\mathbb R^R\), define

\[
\Psi(z)=\frac1n\sum_{i=1}^n\int_0^{(Uz)_i}\phi(v)\,dv.
\]

Then

\[
\nabla\Psi(z)=\frac1nU^\top\phi(Uz),\qquad
\nabla^2\Psi(z)=\frac1nU^\top
   \operatorname{diag}(\phi'(Uz))U.
\]

Use the gradient as the reduced activation and the Hessian as its
backward action. This gives a genuine autonomous network with exact
forward/backward differentiation. Under exact containment of the dense
forward/backward sources and their paired initialized mixer images, its
ordinary Euclidean gradient flow reproduces the dense panel trajectory
in the same physical time. The canonical first-layer/readout mobilities
cancel the normalization of the lifted basis exactly.

The complete model, initialization, proof and costs are in
[INTRINSIC_ROUTE.md](INTRINSIC_ROUTE.md). No future dense observations or
passive labels enter the initialization definition.

## Why this does not yet give a new compression theorem

The exact potential needs \(nR\) basis entries and width-dependent
evaluation. Compiling a degree-\(k\) scalar primitive into a polynomial
in \(R\) coordinates can require \(\binom{R+k}{k}\) coefficients.
Calling that object a potential does not remove its inventory. Nor does
low temporal rank imply a cheap state-dependent nonlinear function.

There are two precise outstanding obligations:

1. Represent the potential, its gradient and Hessian action on the
   reachable reduced states with a small counted initializer and runtime.
2. Prove propagation of approximate source defects and fitting under the
   existing full label allowance, including the all-time endpoint error.

The polynomial construction has dimension-free local activation and
derivative error bounds, but these two obligations are not inferred from
them. Its global existence and stability must not be borrowed unchanged
from the different, corrected-selector optimizer.

## Why coordinate selection has a structural role

For any nonaffine analytic activation, a linear reduction satisfying
\(T\phi(z)=\phi(Tz)\) on an open ambient set has at most one nonzero
entry in each row. Mixed derivatives prove this directly. Coordinate
evaluation is special because it preserves each nonlinear gate exactly;
the metric then repairs inner products on the low-rank response space.

Thus the matrix construction is not merely an arbitrary way of choosing
a basis. It simultaneously retains pointwise nonlinear calculus and
compresses the necessary pairings. The obstruction does not apply to
changed reduced activations, approximate identities on a trajectory, or
nonlinear reductions. The potential above is a concrete way around exact
commutation, with an explicit remaining price.

See [ALGEBRAIC_OBSTRUCTION.md](ALGEBRAIC_OBSTRUCTION.md) for complete
proofs, including the characterization of finite coordinatewise-product
algebras and the limits of each statement.

## Status

These algebraic results and the conditional exact-capture theorem were
reconstructed by the lead after the scoped candidate was frozen. This is
an internal theoretical check, not promotion or a new empirical claim.
The source-rank improvement in the related clock study uses the existing
selector, not an unproved replacement by this potential. Near-second-power
storage and an equally efficient selector-free nonlinear evaluator remain
separate open questions.
