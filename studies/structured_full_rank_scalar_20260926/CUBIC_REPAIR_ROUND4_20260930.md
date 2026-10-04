# Explicit extension: exact quadratic hidden-feature curvature

The three predeclared rounds have finished without meeting the practical
repair target (circle RMS at most 0.05 on both difficult tasks). The best
joint result remains the bounded-Gram model, 0.2403 / 0.2527; retaining one
additional readout direction gives 0.1239 / 0.4765 with its gate. Preserve
these failures. This is an explicit extension of the previous stopping
rule under the user's request to iterate on a very small number of omitted
terms, not a predeclared successful branch.

There is a specific remaining omission: all the tested response models
linearize the hidden feature map in hidden-weight displacement. Test the
exact second directional derivative of that map at initialization. It
contains both activation curvature and the mixed changes of the two
hidden layers. The coefficient is derived, not fitted from dense training.

Use the same initial hidden-gradient span as the bilinear model, whitened
in its canonical optimization metric. For feature/readout contraction F,
retain F=A+L eta+eta^T H eta/2. Evolve readout coefficients and eta by the
exact gradient flow of this surrogate's squared loss. The Hessian adds
static coefficients but **no evolving states**. The derivation, coefficient
cost, cutoff, and algebra checks must be recorded before integration in
CUBIC_QUADRATIC_FEATURE_ROUTE_20260930.md. A quadratic feature map remains
a local approximation; its gradient-flow structure alone does not imply
fidelity to the dense network or bounded tanh features.

Freeze two variants: initial training-feature readout span (p=m), and that
span plus the already specified single terminal cubic response mode
(p=m+1). No mode selection using dense outputs, damping fit, parameter
sweep, or degree beyond two. Retain all numerically nonzero hidden Gram
directions at the fixed relative 1e-12 threshold and report the rank. Train
only near_pair_sin9, cluster_triple_cos9, cluster_triple_cos1 initially.
The unchanged mechanism gate permits the six-task transfer only if one
variant improves both difficult original RMS errors by at least a factor
three without smooth-case regression over 0.02. The practical target stays
0.05. A failed gate ends this extension; do not quietly add further modes.

Use the existing n=1024, seed=1 coefficients and dense fitted endpoints,
MSE target 0.001, rtol=1e-8, atol=1e-10, first step 0.01, max step 10,
physical time cap 3000, and ten-second integration budget per run.
Coefficient construction has a thirty-second budget per task and 2 GiB
memory cap. Degree-one agreement and finite-difference Hessian checks are
implementation checks, not additional trained candidates. Numerical
replicates at rtol=1e-9, atol=1e-11 remain authorized for improvements.

Report training state count p+d (d <= mp), static tensor entries, and
initial width-dependent coefficient cost separately. Passive test inputs
use a static contraction of the trained state, so this model has no query
ODE states. Compare raw fitted function differences over the same 256
circle points; passive points never enter the training loss.

Products: cubic_feedback_repair_20260930/round4/ and clearly named checks.
Finish with an honest synthesis even if this last specific correction
fails: the task is not solved merely by reducing a large error.
