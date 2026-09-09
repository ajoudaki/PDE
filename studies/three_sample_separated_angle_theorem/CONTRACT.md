# Three separated inputs: proof contract

Date: 2026-09-07. This document fixes the research scope. The completed
mathematical result and final independent audits are in PROOF.md and
REVIEW_STATUS.md; this contract is not itself proof evidence.

Target: extend the full population/GF/raw-GD result in
../two_sample_separated_angle_theorem/PROOF.md to three fixed deterministic
inputs x_1,x_2,x_3 with ||x_a||^2/d=1 and x_a^T x_b/d<=1-delta for all
distinct a,b, and every y in {-1,1}^3. A single activation is selected from
delta alone, independently of actual data, dimension, width and physical
horizon. Empty geometric classes impose no requirements.

The finite model, Gaussian initialization, raw metric and simultaneous GD
step n^-2 are unchanged. The loss becomes (1/2) sum_{a=1}^3 (f_a-y_a)^2;
every gradient sum has three sample terms. All hidden layers use the same
activation. The population objects remain three canonical neuron spaces,
two initialized bounded actions with actual adjoints and HS learned
increments, the first vector field, and the readout field.

Required conclusions: one global strong autonomous population flow,
uniqueness and reached-state continuation; full width-sequence convergence
in probability of GF and raw GD on every fixed finite physical interval;
all four 3x3 raw kernel blocks, predictions/loss, both action orientations,
joint same-layer three-sample hidden paths in W2(C([0,T];R^6)), specified
velocity laws and second moments/integrated speeds; positive nonaffinity
and initial all-layer/all-sample feature-learning certificates. No claim
of convergence uniformly on the infinite half-line or uniformly over
datasets is inserted.

The activation-design request permits a fixed affine gain as well as a
nonzero nonlinear perturbation. One route studies
phi(z)=a_delta(1+z)+e_delta arctan(z). This is a change of witness activation,
not of architecture, raw optimizer, loss, or initialization. Success with
this family must not be reported as a proof for the unit-slope family
1+z+e_delta arctan(z).

Authorized work: theoretical derivation, local proof artifacts, and
independent adversarial agents (continuing the user's earlier request).
No numerical experiment, original-task resumption, external posting or
Git commit is included. Supplied mathematical proofs may be reused only
after checking the three-sample hypotheses and the new activation.

Routes: geometry and direct counterexample search; affine/large-gain
kernel control; nonlinear source/continuation extension. A failure of
two-sample symmetry is a proof-route obstruction, not a counterexample
to the requested theorem. A deterministic bounded-state estimate alone
does not establish the population construction or velocity limit.
