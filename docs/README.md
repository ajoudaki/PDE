# Established theory: a reading guide

This is a modular mathematical library, not a chronological research diary.
Start with [shared notation](NOTATION.md); each chapter then states its exact
model, hypotheses, claim and proof. A local theorem, a special-data theorem and
a benchmark for a different architecture are not interchangeable.

## The scientific question

Can a deep, genuinely nonlinear network with learned hidden features be
understood as a discretization of an autonomous, uniquely restartable
population evolution? The desired comparison is joint in width and the actual
gradient-descent step, uniform on each finite physical-time interval, and
includes internal representations and the two directions of reused matrices,
not just predictions.

There are three subsequent questions. Does that evolution fit the training
labels? Can the fixed depth and finite dataset be replaced by controlled depth
and input-population limits? Finally, what property of the learned features
explains risk on unseen data? A precise training equation or vanishing training
loss is not by itself a generalization theorem.

The intended dense-network question retains correlated data, ordinary Gaussian
initialization, nonlinear activations and genuine hidden learning. Freezing
features, imposing orthogonality or whitening, or changing the architecture to
make a proof easy would answer a different question. Explicitly separated
linear and residual-particle benchmarks are useful comparisons, not substitutes.

## Chapters and their exact roles

| Chapter | Established content and scope |
|---|---|
| [Finite dynamics and energy](finite_dynamics.md) | Exact all-depth, finite-batch gradients, raw kernel blocks and dissipation; global finite-width GF for `C^2` activations; finite-horizon norm bounds under bounded slopes. |
| [Gaussian and flow calculus](gaussian_calculus.md) | Exact conditioning, empirical transpose laws, finite-order gradient identities and rational Gaussian moments; complete width identification for each fixed-depth, fixed-length feature-ascent program with order-one stored readout. Also proves limits of same-space product norms and explains why Taylor divergence does not exclude smooth ODEs. No growing-program/GF inference. |
| [Arctangent operator limits](arctan_limits.md) | One input and label one, small stored readout: global joint L=2 limit and complete local L=3 limit, with their own step conditions and observable contracts. Also contains a global auxiliary population/width theorem at each fixed backward-query cap, on finite feature-time horizons. This is not the uncut optimizer. |
| [Global nonlinear learning](global_nonlinear.md) | The same activation `1+arctan(z)/10`, every separately fixed hidden depth `L>=3`, one input and label one: global compact-time joint limit, fitting, persistent nonaffinity and hidden activity. |
| [Special-data limits](special_data_limits.md) | Opposite-label L2 arctangent at orthogonal/antipodal inputs; equal-label shifted-arctangent L3 at all admitted correlations; and a three-sample bounded-shape/gain family at every fixed depth. Exact loss clocks and distinct activity/fitting claims are stated separately. |
| [Linear dynamics and closure boundaries](linear_dynamics.md) | L=3, one input, order-one stored readout: global operator-valued population/GF/GD limit and fitting; nonclosure only in the precisely specified bounded-contraction scalar/local-PDE encoding classes. |
| [Continuous depth](continuous_depth.md) | A different, scalar-particle residual architecture: global characteristic GF and joint width/depth convergence under explicit parameter regularity. Not the dense Gaussian matrix architecture and not a joint GD-step theorem. |
| [Finite optimization and controls](finite_optimization_and_controls.md) | Canonical L=3 arctangent finite GF and exact GD fitting with finite endpoints on proved Gaussian events; a separate energy-compatible finite projection, integrated L1 defect and exactness at a sufficient cap C sqrt(n). No projection population/GD limit. |

Read the first two chapters as common mathematical foundations. The nonlinear
chapters carry their complete source-identification and stability proofs; a
reader need not reconstruct a probability argument from an earlier report.
The linear and continuous-depth chapters clarify what an operator representation
can retain and which conclusions are architecture-dependent. The finite-controls
chapter separates optimization from population identification. The accompanying
[implementation guide](../code/README.md) describes the finite reference and
exact Gaussian arithmetic; code execution is not needed to check the proofs.

## Comparison of mathematical targets

Several distinct targets are often conflated:

- A fixed finite Gaussian computation identifies finitely many matrix calls;
  it does not automatically control a growing number of GD steps.
- A formal self-consistency equation identifies a candidate; its well-posedness
  and convergence from actual networks are additional obligations.
- A fixed-kernel approximation does not establish learned hidden features.
- A finite number of function or operator fields is not a finite number of
  scalar moments. Restricted nonclosure can coexist with an operator limit.
- Compact-time convergence and optimization are separate. If population loss
  tends to zero, choose a finite `T` for a desired loss accuracy first; uniform
  approximation on `[0,T]` then transfers that accuracy to sufficiently wide
  networks with sufficiently small steps. This does not give a bound uniform
  over arbitrary growing `T_n` or convergence of final parameter endpoints.

These are distinctions between mathematical claims, not an assertion that an
entire literature lacks a particular theorem or that the library establishes
priority over all prior work. No such novelty claim is needed by any proof here.

## Scope and future development

The global uncut dense L=3 arctangent population theorem for general correlated
datasets is not asserted. Neither are a general input-population limit, a dense
Gaussian joint depth/width/time theorem, or a generalization theorem. Their
absence is not an impossibility result.

Future additions should enlarge this library through proved statements with
explicit dependencies and consistent notation. Each result should say which
inputs, initialization, mobilities, observables, topology and horizons it covers;
whether learning remains nonlinear and nonlazy; and exactly what restartability
means. Numerical evidence requires its full generation commands, configurations
and seeds. No currently included theorem relies on a numerical figure or a
generated coefficient table.
