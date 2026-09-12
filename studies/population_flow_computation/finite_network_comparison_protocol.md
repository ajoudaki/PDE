# Independent finite-network comparison protocol (not executed)

This is a prospective bounded validation protocol. Finite-network training and
broad sweeps were excluded from the current authorization; none was run. A new
explicit authorization and recorded budget are required before execution. The
source solver's twelve-trajectory budget is already spent.

## Fixed scientific contract

Use exactly two hidden tanh layers, input dimension two, no bias, independent
Gaussian stored initialization with variances (1,1/n,1/n^2), output divided by n,
unhalved squared loss and physical mobilities (n,1,n). In particular draw the
actual finite readout. Setting it to zero would change the comparison model.
Each trajectory keeps one law fixed for its entire duration. A law quadrature
changes that law and is a separate error axis, not a time-dependent minibatch.

The maintained `pde.finite_network` API supplies `initialize`, `forward`,
`backward` and `flow_velocity`; `code/README.md` states their conventions.
The existing `gd_step` is a simultaneous Euler/GD update, not an exact GF
solution. Interpret its step-refined interpolants as a numerical GF comparison
only after an independent time-discretization check.

For unequal masses, use the explicit weighted physical right side below or
extend a study-owned wrapper after inspecting the complete maintained producer.
Do not silently replace unequal masses by the maintained uniform mean.
With u_a=x_a/sqrt(2), let

    h1_a=tanh(W1 u_a), h2_a=tanh(W2 h1_a),
    f_a=c^T h2_a/n, r_a=f_a-y_a,
    delta2_a=c*sech^2(W2 h1_a),
    delta1_a=(W2^T delta2_a)*sech^2(W1 u_a).

Then

    c'  = -2 sum_a p_a r_a h2_a,
    W2' = -(2/n) sum_a p_a r_a delta2_a h1_a^T,
    W1' = -2 sum_a p_a r_a delta1_a u_a^T.

All blocks use the preceding state in a simultaneous Euler step. Verify these
factors against analytic loss derivatives before any comparison campaign.
For the two equal-mass reference atoms the maintained `flow_velocity` applies
directly with `TANH` and default unit kappas.

## Prospective smallest comparison campaign

An initial authorization could cover reference-law widths n=128,256,512 with
three independent prescribed seeds each, physical T=40 and h=.05, followed by
the same three n=256 seeds at h=.025. This is twelve finite trajectories and
12,000 physical steps. These are proposed settings, not a demonstrated accuracy
or timing claim. Preregister a ten-minute wall limit, a one-GiB process target,
single-thread numerical libraries and failure/stop conditions before running.
Start with one pilot inside that budget; stop if projected resource use exceeds
it. Include producer, configuration and environment hashes in each fresh output
directory. Do not authorize a wider law sweep by implication.

Keep the small-readout Gaussian root, first/second initialized weights, and all
current raw finite parameters only in this independent finite reference run.
They are never an input to the source solver. Finite-network raw matrix storage
is n^2+3n scalars, plus activations, integration workspace and retained snapshots;
its O(n^2 m) work per RHS evaluation is separate from the source solver's cost.
Save checkpoints at t=0,5,...,40, with their storage charged explicitly.

## Observations and separation of errors

Compare predictions on the same 65 circle directions and nine physical times
used by the existing source diagnostics. Label this a grid comparison. A grid
maximum is not a continuous circle/time maximum. Any uniform statement needs
proved spatial/temporal moduli and corresponding mesh error terms.

For each layer retain paired initialized/current vectors at the four requested
directions, including cross-input pairs and hidden squared motions. In the
finite network compute Z0=W2(0) H0 and Z=W2 H, and separate current initialized
and learned actions as W2(0) H and (W2-W2(0)) H. Compute reverse queries with
the transpose of those same matrices. Do not sample fresh matrices for reverse
or initial/current observations. Keep lower and upper joint empirical laws
separate; equal neuron indices across layers do not define a population pairing.
Compare named moments and a declared finite family of joint tests, rather than
claiming that matching marginals or a few moments proves joint W2 convergence.

Report the following independently:

* Finite GF integration: same initialized finite model, h versus h/2.
* Finite width: distribution over seeds at fixed law/time integration, with
  width-dependent means and spread. No effective width rate is supplied by C.4.7.
* Source solver: P, h, s, history length, query order and precision separately.
  Reuse the already recorded outcomes until more source runs are authorized.
* Data quadrature: identical nonlinear law with two deterministic quadratures;
  charge their W1 input errors. This would be a separately authorized extension.
* Passive Gaussian integration and observation draws: quadrature bound or
  joint-query sampling uncertainty, not hidden inside the source sample axis.

Agreement would be independent empirical evidence for identification. It would
not prove C.4.7's existence, a finite-width rate, the source solver's requested
accuracy, broader-law existence, or generalization. A disagreement surviving
each numerical refinement is actionable adverse evidence; do not fit a closure
to remove it. The current study has no outcomes from this protocol.
