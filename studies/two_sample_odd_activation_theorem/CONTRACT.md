# Two inputs separated from both correlation endpoints

2026-09-07. This is a proof contract, not a completed theorem certificate.

Interpret the user's condition as |rho|<=1-delta, with 0<delta<=1.
Use two deterministic RMS-unit inputs, all binary labels, the original
three-hidden-layer network, independent Gaussian initialization, raw
gradient metric, and simultaneous raw GD step n^-2. There are no additive
biases or activation offsets. All hidden layers use the same activation.

Target: prove the complete global population/GF/raw-GD result, including
canonical bounded actions and adjoints, strong uniqueness and reached-state
continuation, all previously specified kernel/path/velocity observables,
uniform nonaffinity, and nonzero initial motion of every hidden parameter
block and each sample's features in every hidden layer. Initial acceleration
claims concern hidden blocks; the readout has a nonzero initial velocity.

Proposed uniform family: phi(z)=a z+e arctan(z), a in [1/2,1],
0<e<=e_delta, with e_delta depending only on delta. Activation coefficients
must be fixed independently of actual angle, labels, dimension, width,
auxiliary caps/meshes, and physical horizon. Convergence is on each finite
physical interval; no infinite-time uniform width limit is claimed.

This family should imply a genuine convex mixture
(1-theta)z+theta arctan(z), with 0<theta small depending on delta.
Also check the earlier unit Gaussian second-moment request using
(z+r arctan(z))/sqrt(E[(G+r arctan(G))^2]), G standard Gaussian.
The normalized positive coefficients need not sum to one. A nontrivial
convex mixture and exact unit Gaussian second moment cannot hold together.

Authorized scope: theoretical derivation, local mathematical artifacts,
and independent adversarial agents. No numerical experiments, optimizer or
initialization changes, original-task resumption, external publication or
Git commit. The previous two- and three-input results remain unchanged.

Required final status: complete audited proof for the precise target, or
an explicit counterexample/remaining mathematical gap. The old antipodal
counterexample alone is not evidence against the restricted data class.
