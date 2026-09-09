# Authorized activation-design branch

The user has explicitly broadened the research target from canonical
arctangent to finding ONE strictly nonlinear, non-lazy three-hidden-
layer instance with an unconditional joint mean-field/gradient-flow
limit on every finite physical horizon. Activation design is now
authorized; no numerical experiments are authorized. This does not
prove or supersede the old arctangent theorem, which remains open.

We retain the stronger existing observable and dynamics contract:
one input and target 1; equal widths n; all four blocks trained;
independent z^(1)_0 entries N(0,1), W^(2)_0 and W^(3)_0 entries
N(0,1/n), and RESCALED W^(4)_0 entries N(0,n^-2). Predictor
f_n=(W^(4))^T h^(3)/n, loss (f_n-1)^2. Raw exact GD uses eta_n=n^-2
and the original layerwise factors. Raw parameters are interpolated,
with hidden objects recomputed. The residual is outside the deltas.

The proposed single activation, in EVERY hidden layer, is

    phi(z) = 1 + (1/10) arctan(z).

Its parameter is fixed, not width-, time-, mesh-, or accuracy-dependent.
It is analytic, bounded, strictly increasing and nonaffine on every
nonempty interval. The bounds

    5/6 < phi < 7/6,
    0 < phi' <= 1/10,  |phi''| <= 1/5

will be used. The continuous natural coordinate is
F(z)=10(z+z^3/3); then F'=1/phi', and
(phi composed with F^-1)'=(phi')^2 <=1/100.
This is NOT an exact change of raw GD.

Feature-time equations retain their original form:
z^(1)'=delta^(1), W^(ell)'=delta^(ell)(h^(ell-1))^T/n for ell=2,3,
W^(4)'=h^(3); ds/dt=2(1-f). The candidate strategy is to prove
mesh- and clipping-uniform scalar response bounds on feature time
[0,3/2], remove auxiliary clipping entirely, and then use the positive
activation floor to keep every finite physical horizon strictly inside
that interval. The final model and dynamics must contain NO clipping.

Completion still requires finite fields/operators (not finitely many
scalar coordinates), autonomy and unique restart, full-sequence joint
MF/GF/exact-GD convergence, predictions/loss, both directions of both
hidden matrices, all four raw kernel blocks, hidden paths/velocities,
and genuine limiting feature learning. A small fixed nonlinear
coefficient is not itself a non-laziness proof: hidden movement and
kernel change must be established without a width-vanishing factor.
The limiting activations must not become effectively affine through
collapse of the hidden distributions, at initialization or any finite
physical time.

No original arctangent master proof or ledger is rewritten as if this
activation had always been its model. Candidates remain unaudited until
fresh-context proof-only adversarial reviews certify their exact scope;
a partial PASS is not a full theorem PASS. No source agents resume.

Primary internal dependency to be adapted, not silently invoked for a
different activation:
/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md
SHA256 f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4.
