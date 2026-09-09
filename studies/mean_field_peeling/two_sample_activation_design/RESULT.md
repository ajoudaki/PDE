# Result and practical scope

2026-09-08. Three independent complete-proof reviews returned PASS with
no required repairs; scope and reports are in
[REVIEW_STATUS.md](REVIEW_STATUS.md).

The investigation produces a broader positive theorem with polynomial
separation dependence. It does not establish the desired global theorem
for a fixed moderately nonlinear activation.

## The broad positive result

In the original two-input, three-hidden-layer Gaussian raw-training
model, let \(|\rho|\le1-\delta\), \(0<\delta\le1\), with normalized
inputs and arbitrary binary labels. Choose
\[
 \phi(z)=az+e\psi(z),\qquad a\in[1/2,1],
\]
where \(\psi\in C^2(\mathbb R)\) satisfies
\[
 |\psi(0)|\le1,\qquad \|\psi'\|_\infty\le1,\qquad
 \|\psi''\|_\infty\le1.
\]
One universal sufficient rule is
\[
                 0<e\le c_{\rm dyn}\delta^{31/8}.
\]
The exact \(c_{\rm dyn}>0\) is in
[PROOF.md, equation (4)](PROOF.md). It is independent of the shape
within this normalized class, dimension, actual angle, labels, width,
time mesh and observation horizon.

The theorem gives one global autonomous strong population flow,
uniqueness and reached-state continuation, and the original joint
finite-GF/raw-GD limits on every fixed finite physical interval,
including the kernel, hidden path, velocity, second-moment and action
observables. It is not a probability supremum over all datasets or
over the entire infinite time half-line.

The shape may be nonodd, nonmonotone, oscillatory, compactly supported,
bounded, or linearly growing. Examples include sine, cosine, tanh,
smooth bumps, softplus, and \(\sqrt{1+z^2}\), with normalization as
needed. These are shapes in an affine-plus-perturbation activation;
the result does not certify their unmodified use as the full activation.
ReLU is not included because it is not \(C^2\).

If the shape is globally nonaffine, every hidden block and every
sample/layer has nonzero population initial acceleration. A positive
activation nonaffinity margin for all physical times additionally uses
the explicit Gaussian regression condition in Theorem B. A common
margin gives a common coefficient for infinite-dimensional open shape
classes. Global population existence itself does not need that margin.

## What improved, and what did not

The main new steps are:

1. Different fixed sample bases for forward and backward fields remove
   the need for oddness. This retains current transpose returns and
   the actual two residuals in finite physical training.
2. Actual affine hidden marginal variances stay in a fixed positive
   interval independent of delta. A Gaussian regression obligation
   therefore replaces arctangent-specific behavior.
3. Direct raw learned-moment bounds avoid division by a small inactive
   sample variance. This replaces an insufficient intrinsic-scale
   inference in the old normalized-moment route.
4. Explicit growth estimates extend bounded shapes to the full class
   with bounded first two derivatives. No bounded-value or third
   derivative hypothesis is required.

The exponent \(31/8=3.875\) retains the existing response power count
\(19+12=31\) without rounding to 32. It is an improvement of the
sufficient rule, not evidence of a sharp threshold. The previous
fourth-power arctangent proof is a substantive mathematical dependency;
its results are not presented here as new discoveries.

The practical concern remains. Evaluating the exact constants gives
\[
                    \log_{10}c_{\rm dyn}\simeq-230954.3591.
\]
This is vastly too small for a practical-amplitude claim, despite the
polynomial dependence on delta. It is a sufficient proof cutoff, not
evidence that larger coefficients fail.

The relevant scale-invariant diagnostic is
\[
 \mathcal N_\phi(Z)
 =\frac{\inf_{\alpha,\beta}E[\phi(Z)-\alpha-\beta Z]^2}
        {\operatorname{Var}(\phi(Z))}.
\]
[RELATIVE_NONLINEARITY.md](RELATIVE_NONLINEARITY.md) proves
\(\mathcal N_\phi(Z)\le[e/(a-e)]^2\) for every nondegenerate
input law in the normalized derivative class. A large affine gain
therefore cannot resolve the practical issue merely by permitting
a larger absolute perturbation coefficient.

## New mechanisms toward a practical theorem

[AFFINE_POSITIVITY.md](AFFINE_POSITIVITY.md) proves an algebraic
affine source-response certificate. Independence and entrywise
covariance positivity let actual second moments bound response rows,
avoiding the old exponential propagator estimate. Its improved
nonlinear closure is still provisional, so its constants have not
been silently substituted into the global theorem.

[BOUNDED_ACTIVATION_ROUTE.md](BOUNDED_ACTIVATION_ROUTE.md) explores
bounded activations such as tanh without a small nonlinear coefficient.
The physical loss feedback yields pointwise bounds on the readout,
the learned top kernel and both learned reverse-memory terms. This
localizes the remaining tail issue to the reused initial Gaussian
adjoints. The note proves that energy, bounded input and coordinate
exchangeability alone cannot control those tails; their actual causal
neural origin must be used. It also proves why the one-input coordinate
straightening cannot remove both controls at a nonzero correlation.
These are route results, not impossibility results for neural training.

A separate explicit candidate keeps a meaningful nonlinear fraction:
\[
 r(z)=\sin(2z)-2\exp(-2)z,\quad
 v=\frac{1-\exp(-8)}2-4\exp(-4),\qquad
 \Phi(z)=\frac{z+(2/5)r(z)}{\sqrt{1+(4/25)v}}.
\]
It is strictly increasing and has exactly unit initialized Gaussian
variance at every layer. Its nonlinear variance fraction is exactly
\[
 \frac{(4/25)v}{1+(4/25)v}\simeq0.06389055,
\]
at every initialized hidden layer. Its initialized correlations move
strictly toward zero, and the smallest eigenvalue of the top feature
Gram is at least delta. The complete calculation is in
[SINE_INITIALIZATION.md](SINE_INITIALIZATION.md).

These are initialization facts for a single moderate activation.
The global trained population/GF/GD theorem for this candidate remains
open. Initial kernel nondegeneracy does not prove global source control.

## Research-state ledger

| Claim | Mathematical status and scope |
| --- | --- |
| Broad class, polynomial coefficient, full original global-limit conclusions | Proved in PROOF and its two companions; three independent complete-proof PASS reviews |
| Persistent nonaffinity | Additional explicit Gaussian regression margin and coefficient restriction |
| Removing exponential loss from the affine source certificate | Proved conditional affine lemma |
| Moderate calibrated sine activation | Proved initialization geometry and nonlinear fraction |
| Bounded activation physical-memory controls | Proved on existing strong trajectories, and for the actual finite flows |
| Moderate-amplitude global trained theorem | Open |
| Necessity or optimality of the small coefficient | Not established |

The highest-leverage remaining proof obligation is a compact-time
stability/tail estimate for the actual physical-feedback source fields
at a moderate coefficient. It must retain their causal dependence on
the reused Gaussian matrices. Obtaining it would address the global
population identification directly, without buying control by forcing
rapid fitting close to an affine trajectory.
