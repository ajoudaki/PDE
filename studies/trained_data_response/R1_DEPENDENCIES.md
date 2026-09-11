# Complete frozen dependency inputs

These verbatim excerpts contain the invoked mathematical proofs. Chapter equation numbering is local to each source proof unit.

<!-- BEGIN docs/README.md:1-273 -->

# Established theory: a reading guide

This is a modular mathematical library, not a chronological research diary.
Start with [shared notation](NOTATION.md); each chapter then states its exact
model, hypotheses, claim and proof. A local theorem, a special-data theorem and
a benchmark for a different architecture are not interchangeable.

## The scientific question

The project concerns two related mysteries. The first is training: how a deep
network follows an organized learning trajectory through a highly nonconvex
parameter space. The second is more demanding: why the representations selected
by that trajectory can be useful on examples that did not participate in
training. A theory of successful optimization is an important starting point,
but it does not answer the second question. This book presently develops tools
and exact-capture results for the first, while keeping the second as the reason
for studying the internal dynamics rather than only the training loss.

Can a deep, genuinely nonlinear network with learned hidden features be
understood as an approximation of an autonomous, uniquely restartable
population evolution? The desired comparison is joint in width and the actual
gradient-descent step, uniform on each finite physical-time interval, and
includes internal representations and the two directions of reused matrices,
not just predictions.

The limiting object should simplify the description without deleting the
mechanism under investigation. A finite number of function or operator fields
can organize an infinite-dimensional state. It need not collapse to finitely
many scalar moments. Its forward and adjoint actions must remember that the
same matrices are used repeatedly in forward propagation, backpropagation and
training. After reuse, a new matrix output contains a response determined by
previous uses together with unexplored Gaussian randomness; declaring it an
independent fresh Gaussian would remove part of the learning dynamics.

Width and time perform different roles in this approximation. Finite width
provides random empirical populations and matrix actions, not necessarily a
spatial grid. Raw GD is a time discretization in the actual trainable
parameters. A width theorem for every separately fixed number of updates does
not supply estimates uniform in the growing number of updates needed when
the step tends to zero. Conversely, a finite-width continuous flow alone says
nothing about the existence or uniqueness of its population limit. A joint
theorem must connect these approximations with an explicit step condition,
topology, mode of convergence and observable contract.

The resulting equations should support restart from their stated admissible
states, with uniqueness there. A convergent endpoint of an already existing
path does not by itself construct or identify the subsequent path. Nor is a
candidate self-consistency equation a convergence theorem. These obligations
are part of exact capture, not optional refinements after finding attractive
formal equations.

### What the theory must preserve

The intended dense-network question retains correlated data, ordinary Gaussian
initialization, nonlinear activations and genuine hidden learning. Freezing
features, imposing orthogonality or whitening, or changing the architecture to
make a proof easy would answer a different question. Explicitly separated
linear and residual-particle benchmarks are useful comparisons, not substitutes.

This is a mechanism-preservation requirement, not a list of forbidden tricks
whose omissions invite equivalent replacements. The population/GF regime is
useful because finite networks can be compared with it. Normalizing input
lengths leaves their angles and correlations available to the theory. By
contrast, forcing all samples to be orthogonal, discarding the Gaussian matrix
bulk, or prescribing a special low-rank initialization can remove precisely the
interactions the main question seeks to explain. Such models may still be
valuable benchmarks if their different role is explicit.

Nonlinearity must be checked on the distributions actually visited, not only
in the written activation formula. Hidden learning requires motion of the
relevant representations at the claimed scale, not merely a nonzero activation
derivative or moving readout. A nonzero initial acceleration, positive gate
mass, persistent feature velocity and a lower bound on relative nonlinear
strength are distinct properties. A fixed-depth theorem with nonzero absolute
nonaffinity need not retain a uniform relative nonlinear contribution as depth
or an activation gain changes. The chapters state these distinctions instead
of treating all activity certificates as equivalent.

Smoothness and boundedness assumptions can define useful sufficient classes;
their role should be exposed in the estimates. Failure of an estimate for one
activation is not evidence that the whole learning regime is impossible.
Likewise, allowing constants to depend on a fixed correlated dataset is not
the same as proving uniformity over nearly coincident samples. Identical inputs
with incompatible labels obstruct exact interpolation by a deterministic
predictor, but do not obstruct defining its dynamics. Noisy data also require
a suitable achievable-risk target rather than an assumption that all noise
can be removed.

### Approximation through a prescribed training accuracy

Capturing the path and proving that it fits are separate tasks. Energy
dissipation alone gives a nonincreasing loss; it does not exclude a positive
limiting loss. A fitting argument needs additional control along training,
for example in the actual residual direction. Initial conditioning by itself
does not supply that control at later times.

Once compact-time loss approximation and population fitting are both proved
for the same model, they combine without interchanging an infinite training
time and the width limit. To make this precise, let `mathcal L(t)` be the
deterministic population loss and let `mathcal L_(n,eta_n)(t)` denote the loss
of the interpolated raw-GD network, under the chapter's admissible joint
scaling. Suppose the latter converges in probability uniformly on every fixed
finite interval and `mathcal L(t)` tends to zero. For any `epsilon>0`, choose
one finite `T_epsilon` with `mathcal L(T_epsilon)<=epsilon/2`. Then

\[
\mathbb P\{\mathcal L_{n,\eta_n}(T_\varepsilon)>\varepsilon\}
\le
\mathbb P\left\{\sup_{0\le t\le T_\varepsilon}
|\mathcal L_{n,\eta_n}(t)-\mathcal L(t)|>\varepsilon/2\right\}
\longrightarrow0.
\]

The inclusion of events proves the assertion directly. It gives high-probability
accuracy at a prescribed finite time and path approximation up to that time,
provided the theorem includes the corresponding path observables. The same
argument applies to finite-width GF when its approximation is proved, or to
an attainable positive loss benchmark with the inequalities shifted by that
benchmark. It does not give one width sufficient for every accuracy, an
arbitrary growing-horizon bound, exact zero loss in finite time, or convergence
of final parameter endpoints. Quantitative width and step requirements require
quantitative approximation estimates in addition to this argument.

### Beyond fixed depth and a fixed dataset

Two further population questions should remain visible. A continuous-depth
description would organize representations across layers, typically with an
explicit residual scaling. An input-population description would replace a
fixed training list by a sampling distribution. Neither follows by simply
renaming an index in a fixed-depth, fixed-batch theorem. They require estimates
uniform in the new parameter, a specified architecture and sampling model, and
control of the interaction between the limits. Sequential width/depth limits
at initialization do not establish joint trained width/depth/time convergence.
The continuous-depth chapter therefore identifies its different architecture
before stating its positive result.

The bridge toward generalization begins with the learned map on passive test
inputs: inputs evaluated by the trained weights but absent from the updates.
One can then ask what the trajectory selects among predictors that fit the
training data, and whether that selection helps for a specified distribution.
Transport, variational or action-based descriptions are possible research
tools, not established explanations here. A generic energy identity or a
unique evolution has explanatory force for generalization only after an
additional argument connects the selected representations to out-of-sample
risk. Finite training correlations and successful transfer-panel experiments
alone would not establish that connection.

## Chapters and their exact roles

| Chapter | Established content and scope |
|---|---|
| [Finite dynamics and energy](finite_dynamics.md) | Exact all-depth, finite-batch gradients, raw kernel blocks and dissipation; global finite-width GF for `C^2` activations; finite-horizon norm bounds under bounded slopes. Separate L2 one-sample QI/IQ/QQ and differentiated RMS identities include full gradients/kernels, Lax operators, an orientation witness and balance laws. Separate half-square-loss, order-one-readout results give a frozen quadratic joint initial layer, a reached finite ReLU classical obstruction, and local compactness of actual ReLU Euler outputs. |
| [Gaussian and flow calculus](gaussian_calculus.md) | Exact conditioning, empirical transpose laws, rational Gaussian moments and fixed-program width identification with order-one stored readout. Also finite moving physical-flow jets at arbitrary fixed depth/batch through order five, typed held-fixed preactivation Hessians, exact weighted contraction trees and Gaussian forests with all-moment concentration, polynomial Gaussian fourth-order heads, simultaneous fixed-program quadratic loss-GD closure, a width-first quadratic initial layer, exact shallow identity GD and positive Stieltjes measure, a regenerated frozen-first-block Stieltjes certificate, and exact-compiler cubic step-doubling coefficients with explicit fifth-order remainders for fixed depth/update count. Finite loss-GD pullback words and a separate convex-region comparison bound retain the moving residual. An explicit forest proof extends the Stieltjes witness to an existential interval of positive metrics; canonical factorial growth rules out uniform convergence of a prescribed Taylor-loss family. These annealed formal results remain distinct from positive-time network convergence. A sharp shallow feature-step bound is uniform in update count, with a restricted dyadic expected-output limit. No growing reused-matrix program or physical-loss GF inference. An identity-only theorem at every separately fixed depth proves an explicit update-uniform fifth-order remainder and local operator-state flow after the fixed-program width limit; its separate deterministic energy-ball witness refutes a proposed activation-stability bound. A separate exact three-query law proves failure of uniform higher-moment bounds, conditional on a common action realization for the corresponding operator conclusion. Exact integrated-query perturbation and adaptive transcript results include a contained matrix-concentration proof, causal filtering, own-history rank bounds, and same-cap comparison for R_n=o(log n). They do not remove caps or supply a common varying-cap population limit. |
| [Arctangent operator limits](arctan_limits.md) | One input and label one, small stored readout: global joint L=2 limit and complete local L=3 limit, with their own step conditions and observable contracts. Also contains a global auxiliary population/width theorem at each fixed backward-query cap, on finite feature-time horizons. This is not the uncut optimizer. |
| [Global nonlinear learning](global_nonlinear.md) | The same activation `1+arctan(z)/10`, every separately fixed hidden depth `L>=3`, one input and label one: global compact-time joint limit, fitting, persistent nonaffinity and hidden activity. Broad two-layer activation-transform limits allow orthogonal data, with an affine-first arbitrary-data exception and distinct GD step conditions. A separate fixed-depth C1,1 theorem is local for arbitrary fixed data and subGaussian roots; its strict-activity corollary keeps extra Gaussian and nondegeneracy hypotheses. A separate local two-hidden-tanh theorem admits every bounded-label law on the normalized input circle: quantitative training-law and replacement stability, a precisely ordered expected generalization-gap bound, simultaneous sampling/width/raw-GD consistency without relative growth restrictions, and an open nonlazy family. A separate fitted-reference transfer gives whole-circle endpoint approximation and risk at most 1/4 at T=40 for an explicit, extremely small binary-law neighborhood, with early paired hidden activity; it does not construct global perturbed-law population dynamics. |
| [Population limits and correlated-data geometry](special_data_limits.md) | Opposite-label L2 arctangent at orthogonal/antipodal inputs; equal-label shifted-arctangent L3 at all admitted correlations; and a three-sample bounded-shape/gain family at every fixed depth. A separate generic-correlation L2 arctangent theorem proves strong first-layer GF/raw-GD compactness and no kinetic defect, not a unique population limit. Initialization comparisons separately prove sharp odd-mixture conditioning, convex-offset collapse despite scalar nonaffinity, and calibrated sequential width/depth geometry. Separate plateau proofs give a protected Gram, continuous-time row confinement, selected conditional path-law compactness, and finite fitting/restart obstructions. A near-identity family has conditional necessary fitting-distance and time bounds. Further complete global families include separated two-sample offset activations, the odd delta-squared scale and its normalization variants, general-shape and every-fixed-depth perturbations with their own cutoffs, and a three-sample odd large-gain theorem. Moderate sine has exact initialization, a local limit, finite controls and conditional continuation. Further sections contain order-one Gaussian-readout L2 natural-gate GF limits, equal-label sech-gate L3 transfer, order-one-readout tanh short-time/zero-label results, unit-mobility sin-plus-cosine formal coefficients, global given-space affine references with qualified fitting, conditional Osgood continuation, and same-array response estimates. Reached local sech-gradient irregularity, ambient metric/response obstructions and the separate auxiliary first-Euler obstruction retain their distinct scopes. |
| [Linear dynamics and exact-capture comparisons](linear_dynamics.md) | Existing L3 one-input operator/GF/GD theorem, fitting and restricted nonclosure; plus shallow nonlinear characteristics with compact-time output/loss error rates and bounded-activation particle coupling, a contained L2 linear spectral GF system with fitting, and the operator GF limit at every separately fixed linear depth, including trace-norm increment control. These added one-input, order-one-readout GF theorems have no raw-GD or arbitrary-data extension. |
| [Continuous depth](continuous_depth.md) | A different, scalar-particle residual architecture: global characteristic GF and joint width/depth convergence under explicit parameter regularity. A separate section derives finite dense-ResNet gradient/energy/response identities and supplied-trajectory factorial tails, retaining the actual matrices and a separate source-error term. A coherent dense `W/n` kernel model also has a complete global strong-carrier flow with fixed endpoints. A distinct finite-source conditional transport model has complete adjoint, variational, kernel, energy and parity identities, with its regularity and uniqueness premises explicit. These dense and finite-source results supply no width/depth approximation or joint GD-step theorem. |
| [Finite optimization and controls](finite_optimization_and_controls.md) | Canonical L=3 arctangent finite GF and exact GD fitting with finite endpoints on proved Gaussian events; a separate energy-compatible finite projection, integrated L1 defect and exactness at a sufficient cap C sqrt(n). Also mixed-activation L2 finite-GF fitting at every interior correlation with opposite labels, and permanent first-gate mass on an augmented event. A separate prescribed-Hilbert-space capped flow has conditional exponential-tail continuation; its Gaussian action construction and finite-network identification are not supplied. Exact integrated-query memories and supplied-path time covers are also included, with causal stability and derivative/kernel gaps explicit. Full finite tangent geometry adds intrinsic-volume control and its Gaussian expectation, an exact hidden-projection factor, and a deterministic reachable signed-Hessian obstruction. Further squared-log response bounds, a complete reused-Gaussian initialization law and actual small-time positive-curvature estimates have their own finite scopes. Moderate sine has raw-GD energy bounds, weak path tightness and strong endpoints conditional on an existing population path. No population/GD extension for the projection or mixed-activation results. |

Read the first two chapters as common mathematical foundations. The nonlinear
chapters carry their complete source-identification and stability proofs; a
reader need not reconstruct a probability argument from an earlier report.
The linear and continuous-depth chapters clarify what an operator representation
can retain and which conclusions are architecture-dependent. The finite-controls
chapter separates optimization from population identification. The accompanying
[implementation guide](../code/README.md) describes the finite reference, moving
jets, quadratic/RMS state evaluators, a frozen-quadratic half-loss step, and exact Gaussian/certificate/Euler
arithmetic. Code execution is not needed
to check the proofs; the displayed certificate has a complete reproduction
command and independent checking routes.

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

The same care applies to the value of intermediate results. Exact finite
identities, Gaussian-response calculus, correct computational recurrences,
initialization bounds and scoped representation obstructions are substantive
results even when they do not deliver a global nonlinear limit. An auxiliary
clipped flow can isolate the estimate that is missing for the uncut system.
However, a comparison for caps increasing with width does not alone construct
one common population limit. An obstruction to a specified scalar encoding
does not forbid an operator representation. These distinctions guide what is
worth proving and incorporating, not merely how finished theorems are named.

## Orientation to prior work

The following primary sources provide non-exhaustive context, not theorem
dependencies of the chapters. Their hypotheses are not imported to complete
any proof in this library. The useful comparison is between precise models and
limits, rather than labels such as “mean field,” “DMFT” or “deep.”

Yang and Hu's *Tensor Programs IV* studies infinite-width feature-learning
parameterizations and gives discrete-training limit formulas. It is directly
relevant to retaining nonlinear hidden learning under matrix reuse. A
fixed-program identification result must still be supplemented by estimates
uniform in a refining time mesh to obtain the particular joint GF target here;
this is an additional obligation, not a claim that tensor-program methods
cannot contribute to optimization theory.
[Tensor Programs IV](https://proceedings.mlr.press/v139/yang21c/yang21c.pdf).

Rigorous nonlinear multilayer mean-field theory is not absent from the
literature. Nguyen and Pham develop a neuronal-embedding framework with
trajectory approximation and optimization results in specified setups; their
all-depth optimization conclusions include special correlated initializations.
Comparing such a result with this book requires matching the hidden-sum
normalization, initial laws, training metric and surviving Gaussian actions,
not merely counting hidden layers or observing that both limits are nonlinear.
[A Rigorous Framework for the Mean Field Limit of Multilayer Neural Networks](https://arxiv.org/pdf/2001.11443v3).

Nor is every DMFT result only a formal physics calculation. Celentano, Cheng
and Montanari prove bounded-time high-dimensional trajectory limits described
by DMFT for a class of random-design flows. Their applications include shallow
networks with a fixed number of hidden units while input and sample dimensions
grow. This is a rigorous, relevant comparison, but a different limit from
training all hidden Gaussian matrices at diverging width and fixed input data.
[The high-dimensional asymptotics of first order methods with random data](https://web.stanford.edu/~chen96/papers/fom_dynamics.pdf).

For particle/measure descriptions, Chizat and Bach connect a many-particle
gradient flow to optimization under explicit structural and initialization
conditions, including single-hidden-layer applications. This is a useful
precedent for combining approximation and fitting; the logical strategy is
not itself a novelty claim. Extending exact capture to nested learned matrix
actions requires additional structure beyond a shallow particle description.
[On the Global Convergence of Gradient Descent for Over-parameterized Models using Optimal Transport](https://arxiv.org/pdf/1805.09545v2).

Linear and kernel descriptions remain informative comparisons, but neither
alone explains nonlinear feature learning. Conversely, a nonlinear population
equation does not by itself prove optimization or generalization. A serious
comparison records architecture, initialization, data model, parameterization,
optimizer, horizon, topology and observable scope side by side. This book
makes no comprehensive literature-exclusion or priority claim.

## Scope and future development

The global uncut dense L=3 arctangent population theorem for general correlated
datasets is not asserted. The local two-hidden-tanh result in
[Global nonlinear learning, Section C.4](global_nonlinear.md#c4-training-law-stability-for-two-hidden-tanh-layers)
proves a local input-population limit and bounds the absolute value of the expected
train–test gap, with the time supremum outside the expectation. Its local theorem
does not bound the expected absolute gap or excess risk. Section C.4.5 separately
proves useful-risk reduction and whole-circle robustness at a fixed time near
one fitted opposite-label reference. Its certified neighborhood is extraordinarily
small; it supplies neither a global perturbed-law population flow nor evidence
that feature learning outperforms frozen or linear models.
A global input-population theorem and a dense Gaussian joint depth/width/time
theorem remain outside the established scope; this is not an impossibility result.

Future additions should enlarge this library through proved statements with
explicit dependencies and consistent notation. Each result should say which
inputs, initialization, mobilities, observables, topology and horizons it covers;
whether learning remains nonlinear and nonlazy; and exactly what restartability
means. Numerical evidence requires its full generation commands, configurations
and seeds. No currently included theorem relies on a numerical figure or a
generated coefficient table.

<!-- END EXCERPT -->

<!-- BEGIN docs/NOTATION.md:1-98 -->

# Shared notation and model conventions

This file is the notation contract for the established library. A chapter may
introduce a typed auxiliary variable, but must not silently change these
conventions. A theorem's stated initialization, loss and learning rates override
no other theorem: different models are explicitly distinguished.

## Network, data and layers

`L` counts hidden layers, `m` samples, `d` input coordinates and `n` hidden width.
These quantities are fixed separately unless a theorem explicitly takes their
limit. Samples are `(x_a,y_a)`, with `x_a` in `R^d` and scalar label `y_a`.
The input Gram is `G_ab = x_a^T x_b/d`; normalized inputs have `G_aa=1`.
No diagonalization, whitening, orthogonality or nonsingularity is implicit.

The finite first matrix has shape `n` by `d`, the hidden matrices have shape
`n` by `n`, and the stored readout is a vector of length `n`:

\[
z_a^{(1)}=W^{(1)}x_a/\sqrt d,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)}\quad(2\le\ell\le L),
\qquad h_a^{(\ell)}=\phi^{(\ell)}(z_a^{(\ell)}),\qquad
f_{n,a}=\frac{(W^{(L+1)})^T h_a^{(L)}}n.
\]

For the one-input datum `x=1`, `d=1`, the first preactivation and first weight
vector coincide. A common activation is written `phi`; layer-dependent
activations retain their layer superscripts. Write activation derivatives
explicitly as `phi'` rather than introducing a second name for the derivative.

The residual is always `r_a=f_a-y_a`. It is not part of the backpropagated
derivative. In a finite network define

\[
\delta_a^{(L)}=W^{(L+1)}\odot(\phi^{(L)})'(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=(\phi^{(\ell)})'(z_a^{(\ell)})\odot
(W^{(\ell+1)})^T\delta_a^{(\ell+1)}.
\]

Thus `delta_a^(ell)=n partial f_(n,a)/partial z_a^(ell)`. The main squared-loss
convention is `mathcal L_n = m^{-1} sum_a r_(n,a)^2`. Sum or half-sum losses
must be stated where used and change physical time by the corresponding factor.

## Populations, operators and norms

Finite hidden coordinates are lower-case `z^(ell), h^(ell)`; population
coordinates are capitalized `Z^(ell), H^(ell)`. Every hidden layer has its own
probability space `Omega_ell` and expectation `E_ell`. An expectation contracts
only objects in the same population. Population weight operators and the
population readout retain the layer-indexed symbol `W^(ell)`; their operator or
random-variable types are stated explicitly. Population backward coordinates
may be written `Delta^(ell)`; plain `Delta` without a layer is a proof mesh.

Finite transpose is `T`; a population Hilbert-space adjoint is `*`. These are
the actual two directions of the same operator, not independent random maps.
Initial Gaussian population actions can be bounded without being Hilbert–Schmidt;
the trained increments may belong to a smaller operator class.

Use ordinary finite Euclidean, Frobenius and operator norms. A finite RMS is
`||v||_2/sqrt(n)` and a finite normalized pairing is `u^T v/n`; do not hide
these factors in new norm or inner-product symbols. A population norm is
`||U||_(L^p(Omega_ell))=(E_ell |U|^p)^(1/p)`. Typed abstract Hilbert spaces in
the linear or operator constructions use ordinary Hilbert norms and pairings.

The population rank-one operator `U tensor V` means
`g -> U E[V g]`; its finite coordinate representative is `u v^T/n`.
The Wasserstein distances between laws are written `mathcal W_p`, with the
underlying Euclidean or path metric stated; they are not weight matrices.

## Initialization and clocks

The nonlinear small-readout convention has independent first weights
`N(0,1)`, hidden-matrix entries `N(0,1/n)`, and **stored** readout entries
`N(0,1/n^2)`. Its limiting initial readout is zero. A chapter using order-one
stored readout states that different initialization explicitly. Equal limiting
initial predictions do not identify the two regimes.

`t` is physical training time, `eta_n` the actual GD step and `Delta` an
auxiliary proof discretization. `kappa_ell` denotes a fixed positive mobility
multiplier. For the preceding first-weight convention the block mobilities are
`n kappa_1, kappa_2,...,kappa_L,n kappa_(L+1)`. Raw GD updates the weights,
which are linearly interpolated; hidden quantities are then recomputed.

For one sample, unit mobilities and label one, feature time obeys
`ds/dt=2(1-f)=-2r` on an interval where this is positive. It is not a new
optimizer. The arctangent coordinate change `F(z)=z+z^3/3` is exact for the
continuous flow only. For `phi(z)=1+arctan(z)/10`, the corresponding primitive
is `F(z)=10(z+z^3/3)`. Neither turns exact raw GD into exact transformed Euler.

## Scope of a limit statement

Every result specifies the physical horizon, mode and topology of convergence,
step condition, observables and restart domain. Compact-time means each fixed
finite `[0,T]`, not one bound valid for all time or for an arbitrary growing
sequence `T_n`. A local theorem remains local. Loss decay, population existence,
finite-width approximation, nonaffinity and hidden feature motion are separate
claims. A fixed finite number of operator or function fields is not a
finite-dimensional scalar state.

<!-- END EXCERPT -->

<!-- BEGIN docs/finite_dynamics.md:1-227 -->

# Exact finite dynamics and the energy estimate

The conventions are those of [the shared notation](NOTATION.md). This chapter
proves finite identities for arbitrary depth and a fixed dataset. Sections 1–4
prove global finite-width gradient-flow existence and width-independent
finite-horizon norm bounds under their smoothness assumptions. These statements
do not by themselves identify an infinite-width
trajectory. No empirical assertion or population approximation is used here.

Sections 5–7 give separate one-sample, two-hidden-layer quadratic/identity
and differentiated RMS models: exact gradients, kernels, Lax identities,
balance laws and finite physical-flow continuation. Their state matrices
retain width; no population or spectrum-only closure is asserted.

Sections 8–9 use separate order-one-readout, half-square-loss models. They
prove a frozen-bottom quadratic joint initial layer, a reached finite ReLU
classical-flow obstruction, and positive local compactness of actual ReLU
Euler outputs. Frozen, fully trained, classical and subsequential statements
retain their distinct scopes.

## 1. Model and learning metric

Fix positive integers `L,m,d,n`, data `(x_a,y_a)` for `1<=a<=m`, and positive
constants `kappa_1,...,kappa_(L+1)`. Use the forward equations in NOTATION.md and
the mean squared loss

\[
\mathcal L_n=\frac1m\sum_{a=1}^m r_{n,a}^2,
\qquad r_{n,a}=f_{n,a}-y_a.
\]

Each activation is a real `C^2` function. The finite state consists of all raw
weight entries. Its gradient flow is `dot theta=-D grad mathcal L_n`, where
the constant diagonal operator `D` multiplies the first and last blocks by
`n kappa_1` and `n kappa_(L+1)`, respectively, and middle block `ell` by
`kappa_ell`. Gradients of matrix functions use the ordinary Frobenius pairing.

Backpropagation gives the exact derivatives

\[
\nabla_{W^{(1)}} f_{n,a}
=\frac{\delta_a^{(1)}x_a^T}{n\sqrt d},\qquad
\nabla_{W^{(\ell)}} f_{n,a}
=\frac{\delta_a^{(\ell)}(h_a^{(\ell-1)})^T}{n}\quad(2\le\ell\le L),
\qquad
\nabla_{W^{(L+1)}} f_{n,a}=\frac{h_a^{(L)}}n.
\tag{1}
\]

To verify (1), differentiate the readout first. Its derivative with respect to
`z_a^(L)` is `delta_a^(L)/n`. At a lower layer, differentiating
`z_a^(ell+1)=W^(ell+1) phi^(ell)(z_a^(ell))` multiplies this derivative by
`diag((phi^(ell))'(z_a^(ell))) (W^(ell+1))^T`, giving the stated backward
recursion. A variation of `W^(ell)` produces
`d z_a^(ell)=d W^(ell) h_a^(ell-1)`; at the first layer it produces
`d W^(1) x_a/sqrt(d)`. Taking their scalar products with `delta_a^(ell)/n`
proves all three formulas.

Consequently the exact physical flow is

\[
\begin{aligned}
\dot W^{(1)}&=-\frac{2\kappa_1}{m\sqrt d}
  \sum_a r_{n,a}\delta_a^{(1)}x_a^T,\\
\dot W^{(\ell)}&=-\frac{2\kappa_\ell}{mn}
  \sum_a r_{n,a}\delta_a^{(\ell)}(h_a^{(\ell-1)})^T
  &&(2\le\ell\le L),\\
\dot W^{(L+1)}&=-\frac{2\kappa_{L+1}}m
  \sum_a r_{n,a}h_a^{(L)}.
\end{aligned}
\tag{2}
\]

Exact GD of step `eta` adds `eta` times the right side of (2), with every
quantity evaluated at the same pre-update state. Recomputing one block before
updating the next would be a different algorithm.

## 2. Raw kernel blocks and dissipation

Define the mobility-weighted block kernel by
`K_(n,ab)^(ell)=<grad_(W^(ell)) f_(n,a),D_ell grad_(W^(ell)) f_(n,b)>`.
The identity `<u v^T,p q^T>_F=(u^T p)(v^T q)` and (1) give

\[
\begin{aligned}
K_{n,ab}^{(1)}&=\kappa_1\frac{x_a^Tx_b}{d}
                   \frac{(\delta_a^{(1)})^T\delta_b^{(1)}}n,\\
K_{n,ab}^{(\ell)}&=\kappa_\ell
 \frac{(h_a^{(\ell-1)})^T h_b^{(\ell-1)}}n
 \frac{(\delta_a^{(\ell)})^T\delta_b^{(\ell)}}n
 &&(2\le\ell\le L),\\
K_{n,ab}^{(L+1)}&=\kappa_{L+1}
                    \frac{(h_a^{(L)})^T h_b^{(L)}}n.
\end{aligned}
\tag{3}
\]

Each block is positive semidefinite: for any real sample coefficients `c_a`,
its quadratic form is the squared norm of
`D_ell^(1/2) sum_a c_a grad_(W^(ell)) f_(n,a)`.
With `K_n=sum_ell K_n^(ell)`, the chain rule now gives

\[
\dot f_{n,a}=-\frac2m\sum_b K_{n,ab}r_{n,b},\qquad
\frac{d}{dt}\mathcal L_n=-\frac4{m^2}r_n^T K_n r_n
=-\|D^{-1/2}\dot\theta\|_2^2.
\tag{4}
\]

In particular the last equality is the exact weighted energy identity

\[
\mathcal L_n(t)+\int_0^t\left[
 \frac{\|\dot W^{(1)}\|_F^2}{n\kappa_1}
 +\sum_{\ell=2}^{L}\frac{\|\dot W^{(\ell)}\|_F^2}{\kappa_\ell}
 +\frac{\|\dot W^{(L+1)}\|_2^2}{n\kappa_{L+1}}
\right]du=\mathcal L_n(0).
\tag{5}
\]

There is no factor of the residual inside `delta` or inside (3).

## 3. Global finite-width existence

For every finite initial state the flow (2) has a unique solution for all
`t>=0`. Indeed its vector field is locally Lipschitz: the finite composition
defining the loss is `C^2`. The local existence argument is the contraction
mapping for the integral equation on a closed ball of continuous curves, with
time small enough that the locally bounded Lipschitz field maps the ball into
itself and has contraction constant less than one. This also gives uniqueness.

On any interval of this solution, (5) and Cauchy–Schwarz imply

\[
\|D^{-1/2}(\theta(t)-\theta(s))\|_2
\le\sqrt{t-s}\left(\int_s^t
             \|D^{-1/2}\dot\theta(u)\|_2^2du\right)^{1/2}
\le\sqrt{(t-s)\mathcal L_n(0)}.
\tag{6}
\]

If its maximal forward endpoint were a finite `T`, (6) would make `theta(t)`
Cauchy as `t` tends to `T`. The metric in (6) is equivalent to the Euclidean
metric at fixed `n`, since all mobilities are positive. Its limit is a finite
state. The same local contraction construction at that state extends the
solution past `T`, a contradiction. This proves global existence without a
bounded-activation assumption. It does not assert global stability of GD.

For each `t<=T`, applying (6) blockwise gives

\[
\frac{\|W^{(1)}(t)-W^{(1)}(0)\|_F}{\sqrt n}
\le\sqrt{\kappa_1T\mathcal L_n(0)},\quad
\|W^{(\ell)}(t)-W^{(\ell)}(0)\|_F
\le\sqrt{\kappa_\ell T\mathcal L_n(0)},\quad
\frac{\|W^{(L+1)}(t)-W^{(L+1)}(0)\|_2}{\sqrt n}
\le\sqrt{\kappa_{L+1}T\mathcal L_n(0)}.
\tag{7}
\]

The middle inequality applies to `2<=ell<=L`. It also bounds the operator
norm of each trained middle increment, since operator norm is at most
Frobenius norm. For arbitrary `s<t`, the corresponding bounds hold with
`T` replaced by `t-s`; thus these parameter paths have a uniform square-root
modulus when initial loss is uniformly bounded.

## 4. What is uniform in width

Suppose now the first derivatives of all activations are bounded, the fixed
inputs have bounded RMS norm, and the initial first/readout RMS norms and
middle operator norms are at most a constant independent of `n`. Assume also
`mathcal L_n(0)<=C`. Then on every finite `[0,T]` all preactivation,
activation and backward-vector RMS norms, and every entry of (3), are bounded
by a finite constant independent of `n`.

Here is the complete induction. From (7) the first Frobenius norm divided by
`sqrt(n)`, readout RMS and middle operator norms are bounded. Therefore

\[
\frac{\|z_a^{(1)}\|_2}{\sqrt n}
\le\frac{\|W^{(1)}\|_F}{\sqrt n}\frac{\|x_a\|_2}{\sqrt d},\qquad
\frac{\|z_a^{(\ell)}\|_2}{\sqrt n}
\le\|W^{(\ell)}\|_{\rm op}
       \frac{\|h_a^{(\ell-1)}\|_2}{\sqrt n}.
\]

If `b_ell=sup |(phi^(ell))'|`, the fundamental theorem of calculus gives
`|phi^(ell)(z)|<=|phi^(ell)(0)|+b_ell |z|`. The triangle inequality transfers
each preactivation RMS bound to an activation RMS bound and closes the forward
induction. The reverse induction is

\[
\frac{\|\delta_a^{(L)}\|_2}{\sqrt n}
\le b_L\frac{\|W^{(L+1)}\|_2}{\sqrt n},\qquad
\frac{\|\delta_a^{(\ell)}\|_2}{\sqrt n}
\le b_\ell\|W^{(\ell+1)}\|_{\rm op}
               \frac{\|\delta_a^{(\ell+1)}\|_2}{\sqrt n}.
\]

Cauchy–Schwarz in each pairing in (3) proves the kernel-entry bounds. The
depth is fixed; this argument supplies no depth-uniform constants.

These initial bounds hold with probability tending to one for the independent
Gaussian initialization in NOTATION.md. First-block squared RMS is a sum of
`nd` Gaussian squares divided by `n` and tends to `d` by the elementary law
of large numbers; stored-readout squared RMS tends to zero. For a middle
matrix, a `1/4`-net of the unit sphere has at most `9^n` points, by disjoint
radius-`1/8` balls and a volume comparison. Approximating both vectors in a
bilinear form by net points bounds the operator norm by twice the largest net
bilinear form. Each fixed form is `N(0,1/n)`. The Gaussian exponential bound
and a union bound give

\[
\mathbb P(\|W^{(\ell)}(0)\|_{\rm op}>M)
\le 2\,9^{2n}e^{-nM^2/8}.
\]

Choose fixed sufficiently large `M` and use a union bound over the fixed depth.
The forward induction at time zero then bounds the initial activations, and
`|f_(n,a)(0)|<=||W^(L+1)(0)||_2 ||h_a^(L)(0)||_2/n` bounds initial loss.
This supplies the claimed high-probability initial event.

Uniform RMS bounds do not control multiplication by an unbounded coordinate
function in the population space. Thus (5)–(7) establish useful a priori
estimates but do not replace the source-identification and response-stability
proofs needed for a nonlinear population theorem.


<!-- END EXCERPT -->

<!-- BEGIN docs/special_data_limits.md:3785-4326 -->

### III.F. Fixed finite Gaussian programs, common actions and strong differentiation

This part treats every fixed finite hidden depth L. All instruction lists and the number of initialized matrices are fixed before width tends to infinity. Its elementary proofs do not assert uniformity for a depth or transcript length growing with width.

#### III.F.1. Finite programs and convergence of their empirical laws

There are \(L\) types of length-\(n\) vectors, one for each hidden layer. Operations combining coordinates may combine only vectors of the same type. For each \(2\le\ell\le L\), let
\[
 W^{(\ell)}_n:\mathbb R^n_{\ell-1}\longrightarrow\mathbb R^n_\ell
\]
be mutually independent matrices with independent \(N(0,1/n)\) entries.
Their transposes are reused as the reverse actions of these same matrices.

Each layer may have a fixed finite tuple of root vectors. Its coordinate tuples are independent and identically distributed, have finite second moment, and are independent of all matrices. Tuples in different layers are independent. Constants are also allowed. In the network application, the first-layer root is a Gaussian vector \(w_0\in\mathbb R^d\) with covariance \(I_d\); the three root preactivations are \(u_i^T w_0\). Here \(w_0=\sqrt d V^{(1)}(0)\) in the isometric bottom coordinates of Part III.M. Additional independent Gaussian roots may be added to any layer when a proof requires probes or regularization.

A deterministic-coefficient program is a fixed finite ordered list of instructions of the following forms:

1. apply a fixed \(C^1\) function \(F:\mathbb R^m\to\mathbb R\) with bounded first partial derivatives, coordinate by coordinate, to previously available vectors of one layer;
2. multiply a previously available vector by \(W^{(\ell)}_n\) or \(W^{(\ell)}_n^T\) for any \(2\le\ell\le L\), with the appropriate types;
3. form a fixed real linear combination of previous same-layer vectors.

The first condition implies a global Lipschitz bound and at most linear growth for each coordinate instruction. The bound may depend on that instruction. Root tuples themselves need not be generated by such functions.

Write
\[
\frac{1}{n}\langle u,v\rangle_{\mathbb R^n}=\frac1n\sum_{\alpha=1}^n u_\alpha v_\alpha,
\qquad \frac{\|u\|_2^2}{n}=\frac{1}{n}\langle u,u\rangle_{\mathbb R^n}.
\]
For same-layer nodes \(v^1_n,\ldots,v^m_n\), their empirical law is
\[
\widehat\mu_n=\frac1n\sum_{\alpha=1}^n
 \delta_{(v^1_{n,\alpha},\ldots,v^m_{n,\alpha})}.
\]
Here \(\mathcal W_2\) uses the Euclidean distance on \(\mathbb R^m\).

**Theorem III.F.1 (fixed finite Gaussian program).** Every such program has deterministic joint limiting laws of all its same-layer node tuples, and
\[
\mathcal W_2(\widehat\mu_n,\mu)\longrightarrow0
\quad\hbox{in probability}
\tag{III.F.2}
\]
along the full width sequence. In particular every within-layer pairwise contraction converges to the corresponding limiting second moment. The scalar laws are given by the source rule in Section III.F.4. Query Grams may be singular. Finite collections of programs sharing the same matrices and roots converge jointly by applying the assertion to their finite union.

We prove this theorem in Sections III.F.2–III.F.5. The following elementary facts make explicit the probabilistic mode of convergence used in its proof.

If \(X_\alpha\) are iid and \(E|X_1|<\infty\), their averages converge in probability to their expectation: truncate \(X_\alpha\) at level \(M\), use the variance bound \(O(M^2/n)\) for the bounded variables, and bound the mean absolute truncation error by \(E[|X_1|1_{|X_1|>M}]\). First send \(n\) to infinity and then \(M\) to infinity. This proves the required initial weak convergence and second-moment convergence of root empirical laws.

For probability measures on a finite-dimensional Euclidean space, weak convergence together with convergence of second moments implies \(\mathcal W_2\) convergence. One direct proof is as follows. Continuous truncations of \(|x|^2\) show that the second moments outside sufficiently large balls are uniformly small. Inside a ball partition space into finitely many sets of diameter at most \(\eta\), choosing boundaries of zero limiting measure. Weak convergence makes their masses converge. Couple the common mass within each partition cell, at cost at most \(\eta^2\), and couple the remaining masses arbitrarily. The unmatched mass inside the ball vanishes; its cost is bounded by the squared diameter of the ball times that mass. The tails have arbitrarily small cost by \(|x-y|^2\le2|x|^2+2|y|^2\). Sending the ball radius and then the partition resolution to their limits proves the claim. A countable family of bounded Lipschitz tests determines weak convergence, by approximation on compact balls and tightness. For random measures the same argument applies in probability, or along an almost surely convergent subsubsequence of every subsequence.

Two arrays on the same neuron indices satisfy
\[
\mathcal W_2^2(\widehat\mu_n,\widehat\nu_n)
\le\frac1n\sum_\alpha |X_{n,\alpha}-Y_{n,\alpha}|^2,
\tag{III.F.3}
\]
using the coupling that pairs equal indices. These facts require no assertion that trained coordinates are independent.

#### III.F.2. An explicit Gaussian operator norm bound

**Lemma III.F.2.** For an \(n\times n\) matrix \(W_n\) with independent \(N(0,1/n)\) entries,
\[
\Pr(\|W_n\|_{\rm op}>10)
\le 2\,9^{2n}e^{-100n/8}\longrightarrow0.
\tag{III.F.4}
\]

**Proof.** A maximal \(1/4\)-separated subset \(\mathcal N\) of the Euclidean unit sphere is a \(1/4\)-net. Balls of radius \(1/8\) about its points are disjoint and lie in the ball of radius \(9/8\), so volume comparison gives \(|\mathcal N|\le9^n\). For unit \(u,v\), choose \(u_0,v_0\in\mathcal N\) within \(1/4\). Then
\[
|u^TW_nv-u_0^TW_nv_0|
\le\tfrac12\|W_n\|_{\rm op}.
\]
Taking the supremum gives \(\|W_n\|_{\rm op}\le2\max_{u_0,v_0\in\mathcal N}|u_0^TW_nv_0|\). For a fixed pair the displayed scalar is \(N(0,1/n)\). Its exponential moment is \(Ee^{t u_0^TW_nv_0}=e^{t^2/(2n)}\); Markov's inequality optimized at \(t=ns\) yields \(\Pr(|u_0^TW_nv_0|>s)\le2e^{-ns^2/2}\). A union bound at \(s=5\) proves (III.F.4). The exponent is negative since \(2\log9<12.5\). The same bound applies to transposes, and a finite union bound handles all matrices. ∎

The same argument for a threshold \(t\ge10\) gives
\[
\Pr(\|W_n\|_{\rm op}>t)
\le2\exp\{n(2\log9-t^2/8)\}
\le2e^{-nt^2/16}\le2e^{-t^2/16}.
\tag{III.F.4a}
\]
Consequently every fixed positive moment is bounded uniformly in width:
\[
\sup_{n\ge1}E\|W_n\|_{\rm op}^p
\le10^p+2p\int_{10}^\infty t^{p-1}e^{-t^2/16}\,dt<\infty.
\tag{III.F.4b}
\]
The integration formula follows by writing \(X^p=\int_0^Xpt^{p-1}dt\) for nonnegative \(X\) and interchanging nonnegative integrals. Hölder's inequality then gives uniform fixed-order moments for every fixed polynomial in finitely many such operator norms. For a standard Gaussian vector \(g_n\), Jensen's inequality also gives \(E\frac{\|g_n\|_2^p}{n^{p/2}}\le E|G|^p\) when \(p\ge2\).

A useful consequence identifies normalized traces without a concentration theorem for functions of matrix entries. Let \(T_n\) be any random real \(n\times n\) matrix independent of \(g_n\sim N(0,I_n)\), with \(\sup_nE\|T_n\|_{\rm op}^2<\infty\). Conditional on \(T_n\),
\[
E_g\frac{1}{n}\langle g_n,T_ng_n\rangle_{\mathbb R^n}=\frac1n\operatorname{tr}T_n,
\quad
\operatorname{Var}_g\!\left(\frac{1}{n}\langle g_n,T_ng_n\rangle_{\mathbb R^n}\right)
=\frac{2}{n^2}\left\|\frac{T_n+T_n^T}{2}\right\|_F^2
\le\frac{2}{n}\|T_n\|_{\rm op}^2.
\tag{III.F.4c}
\]
To verify the variance, replace \(T_n\) by its symmetric part, diagonalize it orthogonally, and use that the transformed Gaussian coordinates are independent with \(\operatorname{Var}(G^2)=2\). Therefore the difference between this probe and the normalized trace tends to zero in \(L^2\). If the probe is a fixed finite program, Theorem III.F.1 identifies its deterministic limit and hence the trace limit in probability. A fixed polynomial in the initialized actions and their adjoints satisfies the operator moment hypothesis by (III.F.4b), and its application to the probe is such a program. Uniform moments of order greater than one upgrade convergence of these normalized traces to convergence of their expectations: split at a large absolute threshold and use the higher-moment bound to make the first-moment tails uniformly small. The same observation supplies uniform integrability of every fixed polynomial expression needed for finite-degree moment calculations.

#### III.F.3. Exact adaptive Gaussian conditioning

Let the current transcript consist of all revealed roots and all previously computed vectors. For one matrix \(W\), collect its earlier forward and reverse observations as
\[
WV=Y,\qquad W^TU=Q.
\tag{III.F.5}
\]
The columns of \(V\) and \(U\) are the respective query inputs, with output columns in \(Y\) and \(Q\). Conditioned on the transcript they are fixed. Empty column lists are allowed; terms involving them are omitted.

It is necessary to justify this conditioning for adaptive inputs. Initially the conditional laws of the matrices are independent Gaussian laws. Suppose this is true, with the linear constraints already observed, at a particular instruction. A coordinate operation is measurable from the transcript and reveals no new randomness. At a matrix call its input is also measurable from the transcript. Conditional on the transcript, the new answer is a linear observation of only the queried matrix. Conditioning a product of the current conditional laws on this observation leaves the other factors unchanged and conditions only the queried factor. Thus induction preserves independence of the residual matrix factors and adds exactly the indicated linear constraint. A freshly revealed independent root likewise does not alter these residual laws. This argument conditions successively, and does not assume that an adaptive input was independent of the matrix before the transcript was fixed.

Suppose first that \(V^TV\) and \(U^TU\) are invertible. Let \(P_V=V(V^TV)^{-1}V^T\), and similarly define \(P_U\). Then
\[
W\mid\mathcal H\ \overset d=
M+P_{U^\perp}\widetilde W P_{V^\perp},
\quad
M=Y(V^TV)^{-1}V^T
 +U(U^TU)^{-1}Q^TP_{V^\perp},
\tag{III.F.6}
\]
where \(\widetilde W\) is an independent copy of the original matrix.

Here is a direct verification of the Gaussian projection behind (III.F.6). The compatibility relation is \(U^TY=Q^TV\), because both sides equal \(U^TWV\). It gives \(MV=Y\) and \(M^TU=Q\). The homogeneous solutions of (III.F.5) are exactly matrices \(K=P_{U^\perp}KP_{V^\perp}\). Both summands defining \(M\) are orthogonal in Frobenius inner product to that subspace. Hence \(M\) is the unique minimum-Frobenius-norm solution. Vectorize \(W\), whose law is an isotropic Gaussian in \(\mathbb R^{n^2}\). In an orthonormal basis adapted to the homogeneous solution subspace its coordinates are independent Gaussians; conditioning on the orthogonal coordinates leaves independent Gaussians on the homogeneous subspace and fixes the other coordinates to those of \(M\). This proves (III.F.6). It also proves the same assertion with orthogonal projections and minimum-norm solutions when column lists are linearly dependent; the nonsingular formula is the only one whose coefficients we take to a width limit.

For a new forward input \(h\), put
\[
\alpha_n=(V^TV)^{-1}V^Th,
\quad h_\perp=h-V\alpha_n,
\quad
\beta_n=(U^TU/n)^{-1}(Q^Th_\perp/n).
\]
Equation (III.F.6) becomes
\[
Wh=Y\alpha_n+U\beta_n
 +\frac{\|h_\perp\|_2}{\sqrt n}P_{U^\perp}g
\quad\hbox{in conditional law},
\tag{III.F.7}
\]
with \(g\sim N(0,I_n)\) independent of the transcript. The reverse formula follows by interchanging the two sides.

Assume provisionally that every query Gram has a positive definite limit. Inductively all contractions of old nodes converge. Thus the coefficients in (III.F.7), and \(\frac{\|h_\perp\|_2}{\sqrt n}\), converge in probability to deterministic limits. Inverting a positive definite fixed-size matrix is continuous, for instance by a Neumann-series expansion about its invertible limit.

The projection removed from the fresh noise is negligible:
\[
E[\frac{\|P_Ug\|_2^2}{n}\mid\mathcal H]
=\frac{\operatorname{rank}U}{n}.
\tag{III.F.8}
\]
The multiplying variance factor is bounded in probability, so conditional Markov's inequality makes its contribution vanish in normalized mean square. After this removal and replacement of convergent coefficients by their limits, the new coordinate is a deterministic linear combination \(m_\alpha\) of old same-layer nodes plus \(\sigma g_\alpha\).

For a bounded Lipschitz test \(\psi\) of the old tuple and this new coordinate, conditional independence of \(g_\alpha\) gives variance at most \(4\|\psi\|_\infty^2/n\) for its empirical average. Its conditional mean is the old empirical average of the bounded continuous function
\[
x\longmapsto E_G\psi(x,m(x)+\sigma G),
\]
which converges by the induction hypothesis. For the new second moment expand
\[
\frac1n\sum_\alpha(m_\alpha+\sigma g_\alpha)^2
=\frac{\|m\|_2^2}{n}+\frac{2\sigma}{n}\sum_\alpha m_\alpha g_\alpha
 +\frac{\sigma^2}{n}\sum_\alpha g_\alpha^2.
\]
The middle term has conditional variance \(4\sigma^2\frac{\|m\|_2^2}{n}/n\), and the last average has variance \(2/n\). All relevant norms are bounded in probability. We obtain weak convergence and second-moment convergence, hence (III.F.2). Coordinate instructions preserve this convergence because their Lipschitz constants bound the transport cost. This completes the induction under the provisional positive-definiteness assumption.

#### III.F.4. Source-response identity and formal derivatives

For every oriented initialized matrix introduce a centered Gaussian source group indexed by its calls. Sources for different orientations, including a matrix and its transpose, are independent groups; they are also independent of the root tuples. Within a forward group for \(W\), the source attached to input \(h\) has covariance with the source attached to input \(v\) equal to \(E[hv]\). Within the reverse group the analogous covariance is \(E[uv]\) for the corresponding reverse inputs. These are uncentered second moments of inputs and centered covariances of sources.

The scalar node of a new forward call is
\[
\mathscr W h=\xi_h+\sum_{s:\,W^Tu_s\text{ already called}}
 u_s\,E[\partial_{\zeta_s}h].
\tag{III.F.9}
\]
The scalar node of a reverse call is
\[
\mathscr W^*u=\zeta_u+\sum_{r:\,Wv_r\text{ already called}}
 v_r\,E[\partial_{\xi_r}u].
\tag{III.F.10}
\]
An input is its explicit expression in named source coordinates and roots, obtained by unrolling previous scalar instructions. A derivative in (III.F.9) or (III.F.10) differentiates that expression. Previously computed expectations, coefficients, covariance entries, mesh sizes, and any deterministic control values are held fixed. Each named source remains a separate formal argument, including when the joint source covariance is singular. An unavailable source has derivative zero. Derivative paths through other matrices' earlier calls remain part of the expression.

The recursion is causal. At a call, its input and its source derivatives are already defined; their expectations determine the response coefficients. The source covariance extension is the Gram extension of the corresponding input list and is therefore positive semidefinite. A Gaussian group with that extended covariance exists: if the old covariance is \(K\), the new cross-covariance is \(b\), and the new variance is \(v\), positivity implies \(b\in\operatorname{ran}K\) and \(v-b^TK^+b\ge0\). To see the range assertion, test positivity on \((tu,1)\) with \(Ku=0\) and arbitrary \(t\). Completing the square on \(\operatorname{ran}K\) gives the second assertion. Consequently the new coordinate can be represented as \(b^TK^+\xi+\sqrt{v-b^TK^+b}\,G\), with a fresh standard normal \(G\). Here a pseudoinverse is used only to construct one fixed finite Gaussian law; no continuity of pseudoinverses is asserted.

**Lemma III.F.3 (source rule).** Under the positive-definiteness assumption of Section III.F.3, (III.F.9) and (III.F.10) give exactly the scalar laws obtained there.

**Proof.** Consider a forward call and use the notation of (III.F.7). Write old forward inputs as \(v_r\), old reverse inputs as \(u_s\), and their scalar outputs, by induction, as
\[
y_r=\xi_r+\sum_s D_{rs}u_s,
\qquad D_{rs}=E[\partial_{\zeta_s}v_r],
\]
\[
q_s=\zeta_s+\text{a deterministic linear combination of old }v_r.
\]
All old source lists are padded by zeros for unavailable indices. Let \(\alpha\) be the limiting least-squares coefficient from (III.F.7), and let \(h_\perp=h-\sum_r\alpha_rv_r\). Orthogonality gives \(E[v_rh_\perp]=0\). Therefore
\[
E[q_sh_\perp]=E[\zeta_sh_\perp].
\tag{III.F.11}
\]
Let \(G_U=(E[u_su_t])_{st}\), the covariance matrix of \(\zeta\). Gaussian integration by parts gives
\[
E[\zeta h_\perp]=G_U E[\nabla_\zeta h_\perp].
\tag{III.F.12}
\]
For completeness, the one-dimensional identity \(E[Gf(G)]=E[f'(G)]\) follows by integration by parts against the standard normal density. The boundary term vanishes for a function of at most linear growth with bounded derivative. Represent a possibly singular Gaussian vector as \(\zeta=T G\), apply this identity in each independent standard normal coordinate of \(G\), and sum using \(TT^T=G_U\). Conditioning on independent roots and the other source groups proves (III.F.12) in the present setting. Every derivative is integrable: at a fixed finite instruction, its norm is bounded by a deterministic finite expression in earlier coefficients and the bounded derivatives of coordinate maps.

The limiting coefficient of \(U\) in (III.F.7) is consequently
\[
\beta=E[\nabla_\zeta h]-\sum_r\alpha_r E[\nabla_\zeta v_r].
\]
Substitution of the old \(y_r\) decompositions in (III.F.7) cancels the second term exactly. The answer becomes
\[
\xi_h+\sum_su_sE[\partial_{\zeta_s}h],
\qquad
\xi_h=\sum_r\alpha_r\xi_r+\sigma G,
\quad \sigma^2=E[h_\perp^2].
\]
Since the old \(\xi\) covariance is the Gram of the \(v_r\),
\[
E[\xi_h\xi_r]=E[hv_r],
\quad
E[\xi_h^2]=E\Big(\sum_r\alpha_rv_r\Big)^2+E[h_\perp^2]=E[h^2].
\]
The fresh normal is independent of all old roots and source groups. Thus adjoining it preserves independence of distinct oriented source groups. The reverse calculation is the same after interchanging the two layers. Interleaving calls of different matrices does not alter this calculation, because Section III.F.3 established the conditional independence of their residual factors. ∎

Independence of source groups does not assert that the answers of a matrix and its transpose are independent. Their response terms encode their dependence. Nor does it assert that a source is independent of all later inputs; later scalar inputs can be functions of that source.

#### III.F.5. Singular queries without a rank-stability assumption

**Lemma III.F.4 (regularization of a fixed program).** The conclusions of Theorem III.F.1 and the formulas (III.F.9)–(III.F.10) hold when any of the limiting input Grams is singular.

**Proof.** For every matrix call introduce a new independent standard Gaussian input vector \(\chi\), revealed immediately before that call, and replace its input \(h\) by \(h+\varepsilon\chi\). Each call has a distinct noise vector. The other instructions are unchanged.

At fixed \(\varepsilon>0\), the new noise is independent of the old transcript and of the unperturbed part of the current input. If \(V\) is the list of prior same-orientation inputs, the normalized squared distance from \(h+\varepsilon\chi\) to \(\operatorname{span}V\) is
\[
\frac{\|P_{V^\perp}h\|_2^2}{n}
 +2\varepsilon\frac{1}{n}\langle P_{V^\perp}h,\chi\rangle_{\mathbb R^n}
 +\varepsilon^2\frac{\|P_{V^\perp}\chi\|_2^2}{n}.
\]
Conditionally, the cross term has variance \(4\varepsilon^2\frac{\|P_{V^\perp}h\|_2^2}{n}/n\). The last norm squared has mean \(1-\operatorname{rank}V/n\) and variance at most \(2/n\). Thus every limiting new squared distance is at least \(\varepsilon^2\). Induction gives positive definite limiting query Grams, so Sections III.F.3–III.F.4 apply to the perturbed program. Equivalently, in its scalar law the new independent root adds \(\varepsilon^2\) to the Schur complement of the old input Gram.

Couple the perturbed and original finite programs with the same matrices and roots. On the event that all initialized matrix norms are at most 10 and that all of the finitely many fresh noise vectors have normalized norms at most 2, propagate errors instruction by instruction. A coordinate instruction multiplies the previous error by its fixed Lipschitz constant; a linear combination contributes the sum of coefficient magnitudes times previous errors; a matrix call contributes at most ten times the input error plus \(20\varepsilon\). Consequently
\[
\max_{\text{nodes }v}\frac{\|v_n^\varepsilon-v_n\|_2}{\sqrt n}
\le C\varepsilon,
\tag{III.F.13}
\]
where \(C\) is finite and independent of \(n\) and \(0<\varepsilon\le1\). The event has probability tending to one by Lemma III.F.2 and the elementary second-moment calculation for Gaussian noise norms.

We next show that the scalar recursion itself is continuous at \(\varepsilon=0\); this step concerns covariances and derivatives, not inverses of empirical Grams. Induct on its finitely many instructions. Each scalar node is a \(C^1\) expression in the finite named source list and roots. If earlier deterministic coefficients remain in a compact set, the expression and its first source derivatives have uniform bounds: the expression has at most linear growth in the root and source coordinates, and its derivatives have a finite deterministic bound. This follows directly by applying the coordinate derivative bounds and the linear response formulas in the previous instructions. The values and first derivatives are continuous in their arguments and in the earlier coefficient list.

By induction, the covariance entries for the next source, which are second moments of old scalar inputs, converge as \(\varepsilon\downarrow0\). If positive semidefinite matrices \(K_j\to K\) have fixed size, then \(K_j^{1/2}\to K^{1/2}\). To verify this without a regularity assumption on eigenvalues, their positive square roots are bounded. Every convergent subsequence of these square roots has a positive semidefinite limit \(T\) with \(T^2=K\). A positive semidefinite matrix has a unique positive semidefinite square root: diagonalize it, observe that any such \(T\) commutes with \(K=T^2\), and restrict to its eigenspaces. Hence every subsequential limit is \(K^{1/2}\), which proves convergence.

Represent the full finite source prefix for each \(\varepsilon\) as \(K_\varepsilon^{1/2}G\) using one standard Gaussian vector for each oriented group, independently of the roots. This couples the source prefixes in \(L^2\). The uniform linear-growth bounds and Lipschitz constants for node expressions then give their \(L^2\) convergence. More explicitly, split the node difference into a change of arguments at fixed coefficients, bounded by the common Lipschitz constant, and a change of coefficients at fixed arguments. The latter converges pointwise and is bounded by a constant times one plus the norm of the finite root/source list, an \(L^2\) dominator. First source derivatives converge in probability and are uniformly bounded, so their expectations converge. This proves convergence of the next response coefficient and closes the induction. At zero noise the resulting expression is exactly (III.F.9)–(III.F.10) for the original formal program.

Let \(\mu^\varepsilon\) be the perturbed scalar law of a selected tuple and \(\mu^0\) the zero-noise law just constructed. We have \(\mathcal W_2(\mu^\varepsilon,\mu^0)\to0\). By (III.F.3), (III.F.13), and the proved fixed-\(\varepsilon\) limit,
\[
\mathcal W_2(\widehat\mu_n,\mu^0)
\le C_m\varepsilon
 +\mathcal W_2(\widehat\mu_n^\varepsilon,\mu^\varepsilon)
 +\mathcal W_2(\mu^\varepsilon,\mu^0)
\]
on an event of probability tending to one. Choose \(\varepsilon\) first, let \(n\to\infty\), and then let \(\varepsilon\downarrow0\). This proves the full-sequence convergence in probability, including singular Grams, and finishes Theorem III.F.1. ∎

The derivative convention has a precise invariant meaning on singular supports. If a source vector \(\zeta\) has covariance \(G\), and \(u\) is the vector of the associated reverse inputs with \(E[uu^T]=G\), then
\[
E[\zeta f]=G E[\nabla f],\qquad
u^Tv=0\text{ a.s. for every }v\in\ker G.
\tag{III.F.14}
\]
The second identity follows from \(E[(u^Tv)^2]=v^TGv=0\). If two admissible smooth formal expressions agree on the Gaussian support, their expected derivative vectors differ by an element of \(\ker G\), by the first identity. Their contracted corrections therefore agree. Individual derivative coefficients need not agree. None of this implies that pseudoinverses converge at rank loss.

#### III.F.6. Causal scalar feedback

The deterministic-coefficient theorem also identifies programs with the following causal scalar feedback. At finitely many stages, compute inner products of already available same-layer nodes, apply locally Lipschitz functions to the resulting finite scalar list, and use the resulting numbers as coefficients of subsequent linear combinations. Assume all scalar operations are defined on a neighborhood of their deterministic limiting arguments; divisions require a nonzero limiting denominator. Require the actual finite operation to be defined everywhere it is used, or assign an arbitrary measurable fallback outside that neighborhood. Convergence of its arguments makes the exceptional event have probability tending to zero. The physical algorithms themselves use no division. Coefficients may multiply unbounded vector nodes, because their perturbations can be estimated by the vector's normalized \(L^2\) norm.

To prove this extension, construct an oracle program by replacing each scalar feedback value by its limiting deterministic value, computed from earlier scalar nodes. The construction is causal and therefore not an implicit fixed-point definition. Theorem III.F.1 identifies this oracle. At the next scalar step use
\[
|\frac{1}{n}\langle u,v\rangle_{\mathbb R^n}-\frac{1}{n}\langle\bar u,\bar v\rangle_{\mathbb R^n}|
\le\frac{\|u-\bar u\|_2}{\sqrt n}\frac{\|v\|_2}{\sqrt n}
 +\frac{\|\bar u\|_2}{\sqrt n}\frac{\|v-\bar v\|_2}{\sqrt n}.
\tag{III.F.15}
\]
At the next scalar multiplication use
\[
\frac{\|c u-\bar c\bar u\|_2}{\sqrt n}
\le |c|\frac{\|u-\bar u\|_2}{\sqrt n}+|c-\bar c|\frac{\|\bar u\|_2}{\sqrt n}.
\]
All oracle norms and finitely many oracle coefficients are bounded in probability; initial operator norms are bounded with probability tending to one. Inductively, these inequalities show that actual coefficients converge to oracle coefficients, actual node errors vanish in normalized \(L^2\), and actual norms remain bounded in probability. Local Lipschitzness of scalar operations suffices by restricting to a compact neighborhood of their deterministic limiting arguments. Equation (III.F.3) transfers every oracle empirical law to the actual program.

#### III.F.7. Common generated probability spaces and actual adjoints

We now fix the data and activation parameters. Construct a countable language of finite deterministic-coefficient programs. Include every root coordinate required by the model; constants; rational linear combinations; applications of the initialized matrices in both directions; the finitely many layer activations and fixed integer-level clips; and, for each arity, a countable family of bounded smooth globally Lipschitz functions dense among continuous functions on compact sets. One explicit such family is obtained by taking piecewise polynomial approximations on rational grids, multiplying by smooth compactly supported cutoffs, smoothing with fixed rational-scale mollifiers, and retaining rational coefficients and rational scales. Clipped products may be included in the same family. Close the language under finite composition. Additional countable lists of fixed programs, probes, caps, time meshes, or coefficient values can be included at the start.

This language is countable and admits a causal enumeration with finite stages. Enumerate its root slots, functions, and numerical coefficients first; at stage \(m\), add the finitely many expressions with at most \(m\) instructions using only the first \(m\) listed items, in dependency order. Every finite expression occurs at some stage. Repeated instructions may be treated as separate named copies. Running the scalar construction on this list realizes all its nodes on a product probability space with countably many independent standard Gaussian coordinates, together with the root tuples. Section III.F.4 gives the successive Gaussian extensions, including zero conditional variance. At each layer retain only the sigma-field generated by that layer's node coordinates; call the resulting probability space \((\Omega_\ell,\mu_\ell)\) and put
\[
\mathcal H_\ell=L^2(\Omega_\ell,\mu_\ell).
\tag{III.F.24}
\]
One can equivalently take the law of the countable tuple of generated coordinates. Its finite-dimensional marginal laws are those from Theorem III.F.1: any finite family is part of a finite program, and unused computations change none of the finite-width vectors. Thus different causal enumerations produce the same generated laws up to the coordinate identification. No arbitrary extra Gaussian directions are added to \(\mathcal H_\ell\).

For every rational combination \(u\) of generated nodes, include its forward and reverse answer nodes. The finite inequality \(\frac{\|W^{(\ell)}_nu_n\|_2}{\sqrt n}\le10\frac{\|u_n\|_2}{\sqrt n}\) holds with probability tending to one. Both squared norms have deterministic limits by Theorem III.F.1, so
\[
\|\mathscr W^{(\ell)}_0u\|_{\mathcal H_\ell}\le10\|u\|_{\mathcal H_{\ell-1}}.
\tag{III.F.25}
\]
The same holds for every other action orientation. Linearity of the finite matrices and convergence of squared differences give linearity of the assignments: for example the limiting squared norm of the difference between the answer to \(u+v\) and the sum of answers is zero. If two expressions represent the same \(L^2\) input, (III.F.25) shows that their answers represent the same output. Real linearity on the real span follows either from finite real-coefficient probes or from rational approximation.

The span of generated nodes is dense in \(\mathcal H_\ell\). Here are the measure-theoretic details. Cylinder sets depending on finitely many coordinates generate its sigma-field. The sets whose indicators can be approximated in \(L^2\) by finite linear combinations of cylinder indicators form a monotone class: under increasing unions or decreasing intersections, indicator convergence in \(L^2\) follows from the continuity of probability measures. They contain the cylinder algebra, hence all generated measurable sets. Simple functions and truncation then approximate every \(L^2\) variable by functions of finitely many coordinates. For a finite Borel probability law on \(\mathbb R^m\), bounded continuous functions are dense in \(L^2\): approximate an indicator by a compact subset inside an open superset whose probability difference is small, and use the continuous distance-ratio function that is one on the compact set and zero outside the open set. Such compact/open approximations follow by first restricting to large boxes and then approximating Borel sets using finite unions of rational boxes; their class is again a monotone class. Finally approximate bounded continuous functions on compact boxes by the included smooth family and control the complement by boundedness and its small probability. All approximants are generated nodes or linear combinations of them.

Consequently (III.F.25) extends uniquely by \(L^2\) completion to a bounded linear map
\[
W^{(\ell)}_0:\mathcal H_{\ell-1}\to \mathcal H_\ell,\qquad
\|W^{(\ell)}_0\|\le10,\qquad 2\le\ell\le L.
\tag{III.F.26}
\]
The reverse assignments extend in the same way. At finite width,
\(\frac{1}{n}\langle v_n,W^{(\ell)}_nu_n\rangle_{\mathbb R^n}=\frac{1}{n}\langle W^{(\ell)}_n^Tv_n,u_n\rangle_{\mathbb R^n}\).
Pass to the limiting pairwise contractions for generated \(u,v\); then use their density and the bounds (III.F.26). This gives
\[
\langle v,W^{(\ell)}_0u\rangle_{\mathcal H_\ell}
=\langle (W^{(\ell)}_0)^*v,u\rangle_{\mathcal H_{\ell-1}},\qquad 2\le\ell\le L.
\tag{III.F.27}
\]
The starred maps are therefore exactly the Hilbert-space adjoints. They are not resampled reverse matrices.

There is no contradiction between these bounded actions and Gaussian initialization. The actions describe all finite generated probes and their joint laws, including adaptive probes. They are not an assertion that every random \(L^2\) input is independent of an initialized action. An adaptive input generally has the response correction in (III.F.9).

Fixed programs with arbitrary real coefficients and arbitrary globally Lipschitz coordinate instructions are represented on these same spaces. Approximate their coefficients by rationals and their coordinate functions on larger compact sets by the dense family. For a Lipschitz target \(g\), select bounded smooth approximants \(g_m\) with accuracy \(1/m\) on the radius-\(m\) ball and a common envelope \(|g_m(x)|\le C(1+|x|)\). Cutting off \(g\) on the radius-\(2m\) ball, mollifying at a sufficiently small scale, and rationally approximating on that ball gives such a sequence with a slightly enlarged fixed envelope. Choose the countable dense family to include these rational cutoff approximants. At a fixed scalar input, the approximation error tends to zero in \(L^2\) by linear growth and the input's finite second moment. Inductively propagate these errors: every matrix call uses the norm bound 10, and each target coordinate instruction uses its Lipschitz bound to control a change of input before approximating the instruction at the limiting input. The identical finite-array error argument holds in probability by Theorem III.F.1 and convergence of the required tail second moments. This proves the agreement of the common-space calculation with its fixed-program width limit.

#### III.F.8. Hilbert–Schmidt increments and the raw state space

For Hilbert spaces \(H,K\), the Hilbert–Schmidt norm of an operator \(T:H\to K\) is
\[
\|T\|_{\rm HS}^2=\sum_j\|Te_j\|_K^2,
\tag{III.F.28}
\]
where \((e_j)\) is an orthonormal basis. This value does not depend on the basis: expand each scalar coefficient \(\langle Te_j,f_k\rangle\) in a basis \((f_k)\) of \(K\), use Parseval twice, and interchange the nonnegative double sum. In particular \(\|T\|_{\rm op}\le\|T\|_{\rm HS}\), since for a unit vector completed to an orthonormal basis its image squared norm is one summand of (III.F.28). The normed space of such operators is complete: a Cauchy sequence has Cauchy matrix coefficients in \(\ell^2\) of two basis indices, whose limit defines an operator by Cauchy–Schwarz and has the limiting Hilbert–Schmidt norm.

For \(u\in K,v\in H\), define
\[
(u\otimes v)q=u\langle v,q\rangle_H.
\]
Parseval gives
\[
\|u\otimes v\|_{\rm HS}=\|u\|_K\|v\|_H,
\quad
(u\otimes v)^*=v\otimes u,
\tag{III.F.29}
\]
and
\[
\|u\otimes v-\tilde u\otimes\tilde v\|_{\rm HS}
\le\|u-\tilde u\|\|v\|+\|\tilde u\|\|v-\tilde v\|.
\tag{III.F.30}
\]
For a Hilbert–Schmidt \(T\), expansion in an orthonormal basis also gives
\[
\langle u\otimes v,T\rangle_{\rm HS}=\langle u,Tv\rangle_K.
\tag{III.F.31}
\]
At width \(n\), using the normalized inner product on both layers, the orthonormal basis is \((\sqrt n\,e_j)_{j=1}^n\); (III.F.28) is then the ordinary Frobenius norm of the matrix. The rank-one action is \(uv^T/n\). Thus this is the exact population counterpart of the raw matrix metric.

The affine raw parameter space in the isometric first coordinates is
\[
 \mathcal P=L^2(\Omega_1;\mathbb R^d)
 \times\prod_{\ell=2}^L
 (W^{(\ell)}_0+\mathcal S_2(\mathcal H_{\ell-1},\mathcal H_\ell))\times \mathcal H_L,
                                                        \tag{III.F.32}
\]
with increment norm
\[
 \|\Delta\theta\|_{\rm raw}^2
 =\|\Delta w\|_2^2+\sum_{\ell=2}^L\|\Delta W^{(\ell)}\|_{\rm HS}^2
                                  +\|\Delta W^{(L+1)}\|_2^2.     \tag{III.F.33}
\]
Only the learned action increments are Hilbert--Schmidt. This is
isometric to the original raw metric because \(w=\sqrt d V^{(1)}\).
Continuous rank-one velocities have strong integrals: their Riemann
sums are Cauchy by uniform continuity on compact intervals and
completeness. The norm of the integral is bounded by the integral of
the norm, and its derivative is the continuous integrand. Formula
(III.F.30) passes uniform factor convergence to HS velocity and integral
convergence. For measurable integrable velocities the same statements
follow by approximation by step functions. Thus learned forward and
reverse increments are actual adjoints throughout.

#### III.F.9. Strong multiplier continuity and the chain rule

**Lemma III.F.5 (bounded multiplier).** Suppose \(z_m\to z\) in probability, \(v_m\to v\) in \(L^2\), and \(b\) is bounded and continuous. Then
\[
b(z_m)v_m\longrightarrow b(z)v\quad\hbox{in }L^2.
\tag{III.F.34}
\]

**Proof.** The term \(b(z_m)(v_m-v)\) has norm at most \(\|b\|_\infty\|v_m-v\|_2\). For the remaining term first restrict to \(|v|\le M\); bounded convergence in probability implies convergence in \(L^2\) of the bounded multiplier difference there. The complement has squared norm at most \(4\|b\|_\infty^2E[|v|^2 1_{|v|>M}]\). Send \(m\) to infinity and then \(M\) to infinity. Bounded convergence in probability used here follows from the elementary estimate \(E|X_m|^2\le\eta^2+K^2\Pr(|X_m|>\eta)\) when \(|X_m|\le K\). ∎

**Lemma III.F.6 (strong chain rule along curves).** Let \(z:I\to L^2(\Omega)\) be strongly \(C^1\), and let \(\phi\in C^1(\mathbb R)\) have bounded derivative. Then \(\phi(z(t))\) is strongly \(C^1\), with
\[
\frac d{dt}\phi(z(t))=\phi'(z(t))\dot z(t).
\tag{III.F.35}
\]

**Proof.** Set \(v_h=(z(t+h)-z(t))/h\to\dot z(t)\) in \(L^2\). The scalar fundamental theorem of calculus gives
\[
\frac{\phi(z(t+h))-\phi(z(t))}{h}
=v_h\int_0^1\phi'(z(t)+rh v_h)\,dr.
\]
The multiplier is bounded by \(\|\phi'\|_\infty\). It converges in probability to \(\phi'(z(t))\): \(|hv_h|\to0\) in probability; restrict \(z(t)\) to a large compact interval and use uniform continuity of \(\phi'\) on a slightly larger interval. The proof of Lemma III.F.5 applies to this bounded convergent multiplier, and yields the derivative. Lemma III.F.5 applied to \(z(t),\dot z(t)\) also proves continuity of the resulting velocity. ∎

This conclusion is a curve chain rule, and makes no claim that the pointwise nonlinear map is Fréchet differentiable from all of \(L^2\) to \(L^2\). Bounded \(\phi'\) is sufficient for the curve result. A jointly measurable velocity may also be integrated coordinatewise: Fubini and \(E\int_I|v(t)|^2dt<\infty\) give absolutely continuous coordinate paths almost surely, agreeing with the \(L^2\) integral. This permits the ordinary scalar chain rule almost everywhere for an absolutely continuous \(L^2\) curve with integrable squared speed.

For bounded-operator curves \(A(t)\) differentiable in Hilbert–Schmidt or operator norm and strongly differentiable \(h(t)\in H\),
\[
\frac d{dt}[A(t)h(t)]=\dot A(t)h(t)+A(t)\dot h(t).
\tag{III.F.36}
\]
Subtract the proposed derivative from the difference quotient. The first error is the operator derivative error applied to fixed \(h(t)\); the second is a uniformly bounded operator applied to the strong derivative error of \(h\); and the cross product is bounded by \(\|A(t+h)-A(t)\|\,\|(h(t+h)-h(t))/h\|\), which tends to zero. This proves (III.F.36).

#### III.F.10. Scalar prediction and feature energy are continuously differentiable

Let \(\rho_\ell\in C^2(\mathbb R)\) have bounded first and second
derivatives for each of the finitely many layers. They may have
nonzero offsets and different bounds at different layers. Define
\(Y_i^1=w\cdot u_i\), \(X_i^\ell=\rho_\ell(Y_i^\ell)\),
\(Y_i^\ell=W^{(\ell)} X_i^{\ell-1}\) for \(\ell\ge2\), and
\(F_i=\langle W^{(L+1)},X_i^L\rangle_L\). Put
\[
 q_i^L=W^{(L+1)},\quad d_i^\ell=\rho_\ell'(Y_i^\ell)q_i^\ell,
 \quad q_i^\ell=(W^{(\ell+1)})^*d_i^{\ell+1}\ (\ell<L).
                                                        \tag{III.F.38}
\]
**Theorem III.F.7.** The scalar map \(F_i:\mathcal P\to\mathbb R\)
is continuously Fréchet differentiable, with
\[
 dF_i[\Delta\theta]
 =\langle d_i^1,u_i\cdot\Delta w\rangle_1
  +\sum_{\ell=2}^L\langle d_i^\ell,
                         \Delta W^{(\ell)} X_i^{\ell-1}\rangle_\ell
  +\langle X_i^L,\Delta W^{(L+1)}\rangle_L,                       \tag{III.F.39}
\]
and raw gradient blocks
\[
 \nabla_w F_i=d_i^1u_i,\qquad
 \nabla_{W^{(\ell)}}F_i=d_i^\ell\otimes X_i^{\ell-1},\qquad
 \nabla_{W^{(L+1)}} F_i=X_i^L.                            \tag{III.F.40}
\]
**Proof.** For a fixed \(v,z\in L^2\), a function \(\rho\) with
\(L_1=\|\rho'\|_\infty,L_2=\|\rho''\|_\infty<\infty\), and
an increment \(q\in L^2\), its scalar Taylor remainder obeys both
\(L_2|q|^2/2\) and \(2L_1|q|\) bounds. Hence
\[
 |E[v\{\rho(z+q)-\rho(z)-\rho'(z)q\}]|
 \le \tfrac12L_2M\|q\|_2^2
   +2L_1\|v\mathbf1_{|v|>M}\|_2\|q\|_2
                         =o(\|q\|_2),                   \tag{III.F.41}
\]
where first \(q\to0\) at fixed \(M\), then \(M\to\infty\).

On a raw neighborhood, forward induction bounds every field
increment by \(O(\eta)\), with \(\eta=\|\Delta\theta\|_{\rm raw}\):
the bottom is linear, every activation is Lipschitz, and
\(\Delta(A X)=\Delta A X+A\Delta X+\Delta A\Delta X\),
with \(\|\Delta A\|_{\rm op}\le\eta\). Start from
\(\Delta F_i=\langle\Delta W^{(L+1)},X_i^L\rangle+
\langle W^{(L+1)},\Delta X_i^L\rangle+O(\eta^2)\).
At level \(\ell\), apply (III.F.41) with fixed incoming weight
\(q_i^\ell\) to replace its weighted feature difference by
\(\langle d_i^\ell,\Delta Y_i^\ell\rangle\), at cost
\(o(\eta)\). If \(\ell\ge2\), expand its action difference;
its mixed term is \(O(\eta^2)\), and adjunction changes the
remaining propagated term to
\(\langle q_i^{\ell-1},\Delta X_i^{\ell-1}\rangle\).
This is the induction invariant for the next lower level. At
\(\ell=1\) the bottom projection is exactly linear. Summing the
finitely many remainders proves (III.F.39). The rank-one identity
(III.F.31) proves (III.F.40). Forward continuity, Lemma III.F.5 at each backward
gate, bounded action continuity and (III.F.30) prove continuity of every
gradient block. This proves the assertion. \(\square\)

For \(H(\theta_h)=\sum_i p_i X_i^L\), the scalar functional
\(\mathcal E=\|H\|^2/2\) is also continuously Fréchet differentiable.
Indeed \(\Delta H=O(\eta)\), so
\(\Delta\mathcal E=\langle H,\Delta H\rangle+O(\eta^2)\).
Apply the same downward weighted expansion with fixed top weight
\(H\) and coefficients \(p_i\). Its gradient is precisely the
backward rank-one expression with readout replaced by \(H\).
The same multiplier continuity proves continuity of this gradient.
No Fréchet derivative of an \(L^2\)-valued Nemytskii map is used.

In the network of Part III.M, take \(\rho_\ell=\chi_\ell\).
The original predictors are \(f_i=a^LF_i\), so their raw gradients
are exactly \(a^L\nabla F_i\). Thus a strong solution of the stated
uncut equations is the raw Hilbert gradient flow of
\(\mathcal L=\tfrac12\sum_i(f_i-y_i)^2\), and
\[
 \dot f=-Kr,\qquad
 \dot{\mathcal L}=-\left\|\sum_i r_i\nabla f_i\right\|_{\rm raw}^2
                =-r^TKr,\quad
 K_{ij}=\langle\nabla f_i,\nabla f_j\rangle_{\rm raw}.
                                                        \tag{III.F.43}
\]
This establishes the true gradient/kernel identities; existence
of the uncut flow is a separate conclusion of Parts III.G and III.V.

#### III.F.11. Fixed-cap local existence and Euler approximation

For each fixed cap, the normalized backward gates in Part III.S are
\(C^1\) with bounded first derivatives. Forward induction and
backward substitution therefore make the raw field locally
Lipschitz on any bounded primal ball. Rank-one updates use (III.F.30),
and physical residual differences use (III.F.15). No derivative of
an uncut \(L^2\)-valued product is needed.

For an autonomous cap field with norm bound \(M_0\) and Lipschitz
constant \(L_0\) on a ball of radius \(b\), its integral map preserves
that ball and is a contraction for \(tM_0\le b\), \(tL_0<1\).
Uniformly converging Picard iterates give a unique strong \(C^1\)
solution. Bounded raw speed gives a strongly Cauchy finite endpoint,
from which the same construction continues whenever a primal bound
is available. For measurable bounded deterministic controls, the
same contraction gives a strongly absolutely continuous path and
its equation almost everywhere.

The one-step Euler defect is at most \(L_0M_0h^2/2\), by integrating
\(\|F(\theta(t+s))-F(\theta(t))\|\le L_0M_0s\).
Iteration of the discrepancy recurrence gives
\[
 \max_k E_k\le e^{L_0T}
        (E_0+\tfrac12 L_0M_0T\max_kh_k).                  \tag{III.F.45}
\]
The constants are width independent on a specified primal ball
and the initialized norm event. This compares a fine raw algorithm
to a fixed auxiliary transcript; the finite-program theorem is
never applied directly to a transcript growing with width.

Whenever the incoming tuple already has its joint \(\mathcal W_2\)
limit, or the later reference estimates give uniformly vanishing
incoming second-moment tails, a final value observation \(q\rho'(z)\)
is treated by clipping \(q\), applying Theorem III.F.1, and removing
the clip using those tails and bounded actions. Mere boundedness
of \(L^2\) norms is not substituted for this tail premise. Whenever a source derivative
of such an unbounded product is needed, the later Parts III.V and III.N
supply the stronger derivative-valid truncation argument explicitly.


<!-- END EXCERPT -->

<!-- BEGIN docs/global_nonlinear.md:1840-2453 -->

## A. Contained probability and continuity specializations

### A.1. Continuous, at-most-linear value instructions

**Lemma.** Extend the finite-program value conclusion of Section III.F to a fixed finite program whose coordinate maps are continuous and satisfy \(|F(x)|\le C(1+|x|)\). Roots are iid finite-second-moment tuples, independent of the initialized Gaussian matrices. Every fixed same-layer tuple converges in probability in \(\mathcal W_2\). The action interpretation is the continuous extension of the actions already constructed in Section III.F. This assertion gives values and second moments, without asserting a formal-derivative formula for these extra instructions.

**Proof.** If \(X_j\to X\) in \(L^2\), continuity and the linear envelope imply \(F(X_j)\to F(X)\) in \(L^2\). Indeed \(|X_j|^2\) is uniformly integrable; uniform continuity on compact balls gives convergence in probability, and the linear envelope supplies uniform integrability of the squared outputs. The same argument proves continuity of pushforward in \(\mathcal W_2\).

Choose smooth compactly supported \(F_R\) converging locally uniformly to \(F\), with a common envelope \(C'(1+|x|)\). Such maps follow by a cutoff on the radius-\(2R\) ball, mollification, and increasing \(R\); each has a finite bounded first derivative. At a fixed limiting input \(X\), \(\|F_R(X)-F(X)\|_2\to0\). Once a prefix has its joint \(\mathcal W_2\) law, its empirical squared approximation error also converges, because \(|F_R-F|^2\) is continuous with at most quadratic growth.

Induct through the finite instructions. Coordinate instructions pass by the pushforward argument. For a matrix instruction, approximate its entire already constructed input prefix by bounded-derivative programs. At finite width the output RMS error is at most the initialized operator bound times the input RMS error; the identical bound holds on the generated population spaces. Thus the matrix outputs are Cauchy in the required law and agree with the extended action. To construct prefix approximants, first choose the current smooth map to achieve its desired limiting error, and only then choose the preceding-prefix tolerance smaller than that error divided by the smooth map's Lipschitz constant. This order avoids any assumption that cutoff Lipschitz constants are uniform. Finite unions of the approximant programs give joint laws, so the induction retains all desired same-layer tuples and both orientations. Let width tend to infinity at each fixed approximant and then remove its approximation. The finite number of instructions completes the proof. \(\square\)

For the activation flow \(J(s,z)\) below, \(|J(s,z)|\le|z|+M|s|\) and joint continuity are sufficient for this lemma. Its possible \(\exp(L|s|)\) sensitivity to the frozen root is not assumed bounded. No response derivative of \(J\) is used. Feedback in that application is transferred separately by the same-root clock stability estimate proved in the two-layer fragment.

### A.2. Fixed neural programs with unbounded backward products

For a **fixed** program with subGaussian root marginals, C2 activations with bounded first and second derivatives, and products \(b(z)q\) with bounded C1 \(b,b'\), the values in A.1 also have the ordinary named-source response formulas obtained by truncating each such product. This is a fixed-program specialization, not an all-moment theorem for arbitrary scalar-feedback programs.

Here are the derivative details. Freeze deterministic coefficients and covariance parameters. Replace each product by \(b(z)\tau_R(q)\), where \(|\tau_R(q)|\le|q|\), \(|\tau_R'|\le1\), and the clip equals the identity on larger and larger compact intervals. At fixed \(R\), every coordinate instruction meets Section III.F's bounded-derivative hypotheses. In the finite scalar recursion, every value has a linear envelope in the finite root/source list, uniformly in the clips while earlier coefficients stay in a compact set. Each first named-source derivative has a polynomial envelope in that list: the only extra factor introduced by differentiating a product is \(|q|\), and there are only finitely many instructions. The clip derivative is bounded by one.

Proceed chronologically in this scalar recursion. Second moments of earlier inputs converge; hence the next finite covariance matrix converges. Couple its Gaussian sources by their positive-semidefinite square roots. The square roots converge even at rank loss, as proved in Section III.F. On this coupling the roots have all moments, and the Gaussian sources have uniformly bounded moments of every fixed order. Local C1 convergence of the clipped expressions and the polynomial derivative envelopes imply convergence in probability and uniform integrability of their first derivatives. Their expectations therefore converge. This identifies the next response coefficient, keeps it bounded, and closes the finite induction. Values agree with A.1 by its same-array RMS approximation and bounded actions. Roots are never differentiated; arbitrary subGaussian iid root tuples are admitted directly as roots. This proves the stated derivative specialization without a quantile-map differentiation or a claim about empirical higher moments.

Locally Lipschitz scalar contractions can be replaced causally by their deterministic limiting values. In the local theorem below their actual finite feedback is recovered by the separately proved one-reference tail comparison. In capped training programs Section III.F already proves this feedback passage directly. No assertion concerning an increasing transcript is needed.

### A.3. Sharp initialized action constant with a contained proof

For an \(n\times n\) matrix \(G\) of independent standard Gaussians,
\[
 E\|G\|_{op}\le2\sqrt n,\qquad
 \Pr\{\|G/\sqrt n\|_{op}>2+\varepsilon\}
 \le (\varepsilon^2n)^{-1}.
\]
Thus every fixed collection of finite initialized actions has norm at most three with probability tending to one, and their canonical generated actions have norm at most two. This supplies the constants used in the odd-gain and fixed-depth affine arguments.

For completeness, compare Gaussian processes \(X_{u,v}=u^TGv\) and \(Y_{u,v}=g^Tu+h^Tv\) on pairs of unit vectors. If \(\alpha=u^Tu'\), \(\beta=v^Tv'\), their increment-variance difference is \(2(1-\alpha)(1-\beta)\ge0\). On a finite net, the Gaussian comparison follows by interpolating the independent processes in \(E[b^{-1}\log\sum_i\exp(bZ_i)]\). Gaussian integration by parts makes the derivative equal to
\(\frac b4 E\sum_{i,j}p_ip_j(d_Y(i,j)^2-d_X(i,j)^2)\ge0\), where the \(p_i\) are softmax weights. Let \(b\to\infty\), then increase the finite nets. Continuity and integrability give \(E\sup X\le E\sup Y=E\|g\|+E\|h\|\le2\sqrt n\).

The Gaussian Poincare inequality needed for the probability bound also has a short proof. For smooth bounded \(f\), let \(P_tf(x)=E f(e^{-t}x+\sqrt{1-e^{-2t}}Z)\). Integration by parts against the Gaussian density gives
\[
 -\frac d{dt}E(P_tf)^2=2E|\nabla P_tf|^2,
 \qquad \nabla P_tf=e^{-t}P_t\nabla f.
\]
Integrate from zero to infinity and apply Jensen and Gaussian invariance to obtain \(\operatorname{Var}f\le E|\nabla f|^2\). Smooth cutoff approximations extend it to Lipschitz \(f\). The spectral norm is one-Lipschitz in the Frobenius coordinates, so \(\operatorname{Var}\|G\|_{op}\le1\); Chebyshev proves the displayed bound. Finite norm inequalities pass to each generated input, then to their countable dense span. Taking rational \(\varepsilon\downarrow0\) gives the canonical constant two. No exponential matrix-concentration theorem is imported.

### A.4. Scalar gradient and strong-chain rules

For bounded continuous \(b\), if \(Z_j\to Z\), \(Q_j\to Q\) in \(L^2\), then
\[
 \|b(Z_j)Q_j-b(Z)Q\|_2\to0.
\]
Subtract the varying \(Q\) first; for the other term truncate the fixed \(Q\) and use bounded convergence. The same proof is uniform over a compact \(L^2\) family using a finite net. Hence bounded activation derivatives give the strong chain rule along C1 \(L^2\) curves, and bounded actions with Hilbert--Schmidt derivatives obey \((WH)'=W'H+WH'\). This does not assert Frechet differentiability of a nonlinear activation map on the whole \(L^2\) space.

For a scalar prediction, Frechet differentiability in the raw Hilbert metric does hold under the bounded-derivative hypotheses used below. For a fixed reverse factor \(q\), the scalar Taylor remainder is bounded by
\[
 \tfrac12 L M\|h\|_2^2+2D\|q\mathbf1_{|q|>M}\|_2\|h\|_2.
\]
Here \(D\) bounds the derivative and \(L\) its Lipschitz constant. First take \(\|h\|_2\downarrow0\), then \(M\to\infty\). Expand the finite number of action/activation products and use \(\|\Delta W\|_{op}\le\|\Delta W\|_{HS}\). This proves the true scalar derivative, its backward-adjoint formula, and continuity of that gradient. Every energy identity below consequently belongs to the specified raw metric.


## B. Global two-layer limits beyond one activation

The theorem below uses the unhalved sum loss and the displayed positive block constants. Orthogonal input projections are essential to its nonlinear first-layer coordinate proof. Its affine-first corollary admits every fixed Gram matrix, including singular matrices. Width identification uses the value lemma A.1; no formal sensitivity formula for the activation transform is invoked.

### B.1. Global two-hidden-layer activation transform

Within this proof unit, unqualified section and equation numbers are local.

#### The theorem and the network

Fix \(m<\infty\) inputs \(x_a\in\mathbb R^d\) satisfying
\[
\frac{x_a^\top x_b}{d}=\mathbf 1_{\{a=b\}},
\qquad 1\le a,b\le m.
\]
Fix labels \(y_a\in\mathbb R\) and positive constants \(\kappa_1,\kappa_2,\kappa_3\), independent of width and step size. Allow different activations in the two hidden layers:

- \(\phi^{(1)}\) is continuously differentiable, and \((\phi^{(1)})'\) is bounded and globally Lipschitz. The activation itself need not be bounded, monotone, or odd.
- \(\phi^{(2)}\) is bounded and continuously differentiable, and \((\phi^{(2)})'\) is bounded and globally Lipschitz.

The dimensions are \(W^{(1)}\in\mathbb R^{n\times d}\), \(W^{(2)}\in\mathbb R^{n\times n}\), and \(W^{(3)}\in\mathbb R^n\). The readout \(W^{(3)}\) is the rescaled readout throughout. Define
\[
\begin{aligned}
z_a^{(1)}&=\frac{W^{(1)}x_a}{\sqrt d},
&
h_a^{(1)}&=\phi^{(1)}(z_a^{(1)}),\\
z_a^{(2)}&=W^{(2)}h_a^{(1)},
&
h_a^{(2)}&=\phi^{(2)}(z_a^{(2)}),\\
f_{n,a}&=\frac{(W^{(3)})^\top h_a^{(2)}}{n},
&
r_{n,a}&=f_{n,a}-y_a,
\qquad L_n=\sum_{a=1}^m r_{n,a}^2.
\end{aligned}
\]
The residual-free backpropagated derivatives are
\[
\delta_a^{(2)}
=
W^{(3)}\odot(\phi^{(2)})'(z_a^{(2)}),
\qquad
\delta_a^{(1)}
=
(\phi^{(1)})'(z_a^{(1)})
\odot(W^{(2)})^\top\delta_a^{(2)}.
\]
Thus \(\delta_a^{(\ell)}=n\,\partial f_{n,a}/\partial z_a^{(\ell)}\). The exact updates are
\[
\begin{aligned}
z_{a,k+1}^{(1)}
&=
z_{a,k}^{(1)}
-2\kappa_1\eta_n r_{n,a,k}\delta_{a,k}^{(1)},\\
W_{k+1}^{(2)}
&=
W_k^{(2)}
-\frac{2\kappa_2\eta_n}{n}
\sum_{a=1}^m
r_{n,a,k}\delta_{a,k}^{(2)}(h_{a,k}^{(1)})^\top,\\
W_{k+1}^{(3)}
&=
W_k^{(3)}
-2\kappa_3\eta_n
\sum_{a=1}^m r_{n,a,k}h_{a,k}^{(2)}.
\end{aligned} \tag{1}
\]
The first equation uses orthogonality. In the original first weights, it follows from
\[
W_{k+1}^{(1)}
=
W_k^{(1)}
-\frac{2\kappa_1\eta_n}{\sqrt d}
\sum_{a=1}^m r_{n,a,k}\delta_{a,k}^{(1)}x_a^\top.
\]

Initialize independently by
\[
W_{0,ij}^{(1)}\sim N(0,\sigma_1^2),
\qquad
W_{0,ji}^{(2)}\sim N(0,\sigma_2^2/n),
\]
where the variances are fixed and finite. The following readout initializations are allowed:

- A vanishing Gaussian readout
  \[
  W_{0,j}^{(3)}\sim N(0,\sigma_3^2n^{-2\beta}),
  \qquad \beta>0.
  \]
  Here \(\beta\) describes the decay of the standard deviation. Gaussian tail bounds give
  \[
  \|W_0^{(3)}\|_\infty
  =
  O_{\mathbb P}(n^{-\beta}\sqrt{\log n})
  \longrightarrow0.
  \]
  The original initialization has \(\beta=1\).
- More generally, an independent readout whose coordinate supremum tends to zero in probability. Its population initialization is zero.
- A fixed bounded readout law: the coordinates are iid with a law supported on \([-B_0,B_0]\), independently of the other initialization. The population starts from that law. A perturbation whose coordinate supremum tends to zero may also be added, giving a finite initial supremum at most \(B_0+o_{\mathbb P}(1)\).

An arbitrary bounded iid law is admitted directly as a root tuple in A.1. The bounded nonvanishing option does **not** include an untruncated \(O(1)\) Gaussian readout: that initialization lacks the population supremum bound used in this proof.

For every fixed \(T<\infty\), the population equations have a unique autonomous gradient-flow solution on \([0,T]\). For every sequence
\[
\eta_n>0,
\qquad
\eta_n\sqrt n\longrightarrow0,
\]
the exact GD trajectories on the clock \(t=k\eta_n\) converge to that solution. Interpolate the finite parameters linearly and recompute the forward pass between steps.

The conclusion includes predictions, summed loss, all kernel-block entries, same-layer joint hidden path laws with their second moments, and fixed finite collections of continuous globally Lipschitz forward/adjoint measurements. Products in these measurement constructions must have bounded varying factors; the unbounded backward fields and their quadratic measurements are included through the tail argument below. Integrated squared hidden speeds converge as well. Convergence is in probability, uniformly in time for the stated pointwise measurements. No claim about arbitrary higher-growth measurements is needed.

The step condition is sufficient, not claimed necessary. These activation assumptions alone do not force nonlinearity or motion: they intentionally include a constant or affine first activation. Additional assumptions for strict feature learning appear at the end.

#### A scalar coordinate that removes the first-layer gate

Let \(J(s,z)\) solve
\[
\frac{\partial J(s,z)}{\partial s}
=
(\phi^{(1)})'(J(s,z)),
\qquad
J(0,z)=z,
\qquad s\in\mathbb R.
\tag{2}
\]
Write
\[
M_1=\|(\phi^{(1)})'\|_\infty,
\qquad
L_1=\operatorname{Lip}((\phi^{(1)})').
\]
The bounded Lipschitz scalar vector field has a unique global solution in both time directions. Integration and the scalar difference inequality give
\[
|J(s,z)-J(t,z)|\le M_1|s-t|,
\qquad
|J(s,z)|\le |z|+M_1|s|,
\tag{3}
\]
\[
|J(s,z)-J(s,w)|
\le e^{L_1|s|}|z-w|.
\]
In particular, \(J\) is jointly continuous. Uniqueness gives the flow identity
\[
J(s,J(t,z))=J(s+t,z),
\]
because both sides solve the same scalar equation as functions of \(s\), with the same value at \(s=0\). Also,
\[
|\phi^{(1)}(J(s,z))-\phi^{(1)}(J(t,z))|
\le M_1^2|s-t|. \tag{4}
\]

For each input introduce a clock displacement \(X_a^{(1)}(0)=0\), keeping the fixed Gaussian root \(Z_{0,a}^{(1)}\), and set
\[
Z_a^{(1)}(t)
=
J(X_a^{(1)}(t),Z_{0,a}^{(1)}).
\tag{5}
\]
The population network is
\[
\begin{aligned}
H_a^{(1)}&=\phi^{(1)}(Z_a^{(1)}),
&
Z_a^{(2)}&=W^{(2)}H_a^{(1)},\\
H_a^{(2)}&=\phi^{(2)}(Z_a^{(2)}),
&
f_a&=\mathbb E[W^{(3)}H_a^{(2)}],
\qquad r_a=f_a-y_a,\\
\delta_a^{(2)}
&=
W^{(3)}(\phi^{(2)})'(Z_a^{(2)}),
&
\delta_a^{(1)}
&=
(\phi^{(1)})'(Z_a^{(1)})
(W^{(2)})^*\delta_a^{(2)}.
\end{aligned}
\]
Its transformed equations are
\[
\begin{aligned}
\dot X_a^{(1)}
&=-2\kappa_1 r_a(W^{(2)})^*\delta_a^{(2)},\\
\dot W^{(2)}
&=-2\kappa_2\sum_{a=1}^m
r_a\delta_a^{(2)}\otimes H_a^{(1)},\\
\dot W^{(3)}
&=-2\kappa_3\sum_{a=1}^m r_aH_a^{(2)}.
\end{aligned} \tag{6}
\]
Here the rank-one action is explicitly
\[
(u\otimes v)V=u\,\mathbb E[vV].
\]
Every expectation pairs coordinates of the same layer. The first-layer and second-layer populations are separate.

The initial \(W_0^{(2)}\) is the bounded forward-and-adjoint action obtained from the joint limits of finite Gaussian matrix calculations, as described below. It is **not** an ordinary continuum matrix or integral kernel with iid Gaussian entries. The notation records its action on generated population fields, together with its adjoint.

The scalar chain rule converts (6) into the ordinary first-layer equation
\[
\dot Z_a^{(1)}=-2\kappa_1 r_a\delta_a^{(1)}.
\tag{7}
\]
Conversely, any solution of (7) in the bounded state class used below has representation (5). Indeed, Cauchy–Schwarz and Fubini make its backward coefficient integrable in time at almost every coordinate. For an integrable scalar coefficient \(b(t)\), the equation
\[
\dot z(t)=b(t)(\phi^{(1)})'(z(t))
\]
has the solution
\[
z(t)=J\!\left(\int_0^t b(s)\,ds,z(0)\right).
\]
Differentiation verifies the equation, and the Lipschitz difference inequality with integrable coefficient \(|b(t)|L_1\) proves uniqueness. Thus the scalar coordinate changes neither the original gradient flow nor its possible solutions.

When \((\phi^{(1)})'>0\), one can use
\[
F'(z)=\frac1{(\phi^{(1)})'(z)},
\qquad
J(s,z)=F^{-1}(F(z)+s).
\]
But the displacement formulation does not require
\(\mathbb E[F(Z_0^{(1)})^2]<\infty\). The rapid growth of this integral for an erf activation therefore places no restriction on its Gaussian initialization variance.

#### Global existence, uniqueness, and autonomy

For a population variable \(U\), write
\[
\|U\|_{L^2}:=\sqrt{\mathbb E[U^2]}.
\]
The operator norm is its largest amplification of this root-mean-square size. Compare two states with the same fixed first-layer roots using
\[
\begin{aligned}
d={}&
\sum_{a=1}^m
\|X_a^{(1)}-\widetilde X_a^{(1)}\|_{L^2}\\
&+\|W^{(2)}-\widetilde W^{(2)}\|_{\mathrm{op}}
+\|W^{(3)}-\widetilde W^{(3)}\|_{L^2}.
\end{aligned} \tag{8}
\]
At finite width replace every population \(L^2\) norm by the ordinary Euclidean norm divided by \(\sqrt n\); denote this distance by \(d_n\).

On sets with bounded clock \(L^2\) norms, matrix operator norms, and readout suprema, the transformed vector field is Lipschitz in (8), with a constant independent of width. The key bounds are as follows. Equation (4) controls first-activation differences, and
\[
\|H_a^{(1)}\|_{L^2}
\le
|\phi^{(1)}(0)|
+M_1\|Z_{0,a}^{(1)}\|_{L^2}
+M_1^2\|X_a^{(1)}\|_{L^2}.
\tag{9}
\]
Adding and subtracting one factor bounds the forward matrix difference. The second-layer backward difference satisfies
\[
\begin{aligned}
\|\delta_a^{(2)}-\widetilde\delta_a^{(2)}\|_{L^2}
\le{}&
\|(\phi^{(2)})'\|_\infty
\|W^{(3)}-\widetilde W^{(3)}\|_{L^2}\\
&+
\|\widetilde W^{(3)}\|_\infty
\operatorname{Lip}((\phi^{(2)})')
\|Z_a^{(2)}-\widetilde Z_a^{(2)}\|_{L^2}.
\end{aligned}
\tag{10}
\]
Its adjoint response is Lipschitz by the operator bound. The output uses boundedness and Lipschitz continuity of \(\phi^{(2)}\). Finally,
\[
\|u\otimes v-\widetilde u\otimes\widetilde v\|_{\mathrm{op}}
\le
\|u-\widetilde u\|_{L^2}\|v\|_{L^2}
+
\|\widetilde u\|_{L^2}\|v-\widetilde v\|_{L^2}.
\]
These estimates prove local existence and uniqueness by contracting the integrated equations on a short interval. A common readout supremum bound defines a closed complete set under (8), and its integral update preserves that bound after the interval is made short enough.

The chain rule and the adjoint identity give
\[
\dot f=-2Kr,
\qquad
\dot L=-4r^\top Kr\le0,
\tag{11}
\]
where
\[
K=\kappa_1K^{(1)}+\kappa_2K^{(2)}+\kappa_3K^{(3)}
\]
and
\[
\begin{aligned}
K_{ab}^{(1)}
&=\mathbf1_{\{a=b\}}\,
\mathbb E[\delta_a^{(1)}\delta_b^{(1)}],\\
K_{ab}^{(2)}
&=\mathbb E[H_a^{(1)}H_b^{(1)}]\,
  \mathbb E[\delta_a^{(2)}\delta_b^{(2)}],\\
K_{ab}^{(3)}
&=\mathbb E[H_a^{(2)}H_b^{(2)}].
\end{aligned}
\tag{12}
\]
Each block is the Gram matrix of the corresponding parameter gradients. Thus \(\|r(t)\|_2\le\|r(0)\|_2\).

Let \(B_2=\|\phi^{(2)}\|_\infty\). The readout equation yields
\[
\|W^{(3)}(t)\|_\infty
\le
\|W^{(3)}(0)\|_\infty
+
2\kappa_3B_2\sqrt m\,\|r(0)\|_2t.
\tag{13}
\]
On any prescribed finite horizon \(T\), this bounds every \(\delta_a^{(2)}\), both in mean square and in supremum. Equations (6) and (9) then give
\[
\|\dot X_a^{(1)}\|_{L^2}
\le C_T\|W^{(2)}\|_{\mathrm{op}},
\qquad
\|\dot W^{(2)}\|_{\mathrm{op}}
\le C_T\left(1+\sum_a\|X_a^{(1)}\|_{L^2}\right).
\tag{14}
\]
The fixed initial root norms are absorbed into \(C_T\). Adding and integrating these inequalities gives a linear Gronwall bound on the clock norms and matrix operator norm throughout \([0,T]\). No finite-time blow-up or loss of the bounded-state conditions is possible. The solution therefore extends uniquely to every finite horizon.

The original state is autonomous as well. At a restart time, take the current \(Z_a^{(1)}\) as the new roots in (5), set the new clocks to zero, and repeat the same argument. The original equations require only current fields and the current matrix action and adjoint. More formally, the closed spaces generated from current fields by the bounded coordinate operations and these actions contain the future integral construction. Equal current joint action laws give an isometry of these spaces that preserves the equations. Uniqueness then gives equal future action laws. Earlier clock values and the original initialization are not additional information needed for the future.

###### Identifying the population action and passing to the width limit

Use A.1 for the fixed finite value programs, jointly for both matrix orientations. The transform is continuous with at most linear growth in (clock, root). Its exponential root sensitivity is not a bounded-derivative hypothesis and no response derivative of that transform is taken. Empirical residual/contraction feedback is identified by the same-root oracle comparison below.

For clarity, the common initial action is constructed before solving the flow. Collect the finite calculations for rational meshes, their finite unions, and a countable closure under the coordinate operations and bounded continuous measurements used here. The fixed-program theorem gives consistent finite joint laws, realized on one coordinate space for each layer. Exact finite linear identities pass to these laws. A Gaussian matrix operator bound implies, with a fixed sufficiently large \(M\),
\[
\|W_0^{(2)}V\|_{L^2}
\le M\|V\|_{L^2}
\]
for every generated \(V\); the same holds for the transpose action. For example the finite bound follows from two \(1/4\)-nets and a union bound,
\[
\mathbb P\!\left(\|W_0^{(2)}\|_{\mathrm{op}}>M\right)
\le
2\,9^{2n}
\exp\!\left(-\frac{nM^2}{8\sigma_2^2}\right)
\longrightarrow0
\]
when \(\sigma_2>0\); the action is zero when \(\sigma_2=0\).
Hence the actions are well-defined on variables equal in mean square and extend to the closures of the generated spans. The finite transpose identity passes to
\[
\mathbb E[U\,W_0^{(2)}V]
=
\mathbb E[((W_0^{(2)})^*U)V].
\tag{15}
\]
This identifies the forward and backward actions as adjoints on the same two fixed spaces. It is the initial object used in (6).

For a proof mesh \(\Delta\), Euler applied to (6) has error \(O_T(\Delta)\), uniformly in width and also in the population space. The bounded vector field and its Lipschitz constant give a one-step error \(C_T\Delta^2\), so
\[
e_{k+1}\le(1+C_T\Delta)e_k+C_T\Delta^2.
\]
Summation gives the stated error. A first-exit argument keeps the clock and matrix inside slightly larger bounds; the readout supremum is controlled separately by its update, as in (13).

At fixed \(\Delta\), expand the trained matrix as its initialization plus finitely many rank-one updates. Construct the oracle using the population residuals and every population contraction in those expansions. The fixed-program theorem identifies all its joint node laws and quadratic contractions. Applying its proxy matrix to an oracle vector differs from the prescribed node by finitely many terms of the form
\[
-2\kappa_2\Delta r_{b,s}\,
\delta_{b,s,\mathrm{oracle}}^{(2)}
\left[
\frac{
(h_{b,s,\mathrm{oracle}}^{(1)})^\top
h_{a,k,\mathrm{oracle}}^{(1)}
}{n}
-
\mathbb E[H_{b,s}^{(1)}H_{a,k}^{(1)}]
\right].
\tag{16}
\]
Each scalar discrepancy vanishes and each vector has bounded root-mean-square norm. The corresponding transpose discrepancies use contractions of two second-layer backward fields. Thus recomputed proxy quantities approach the oracle nodes.

The state estimate (8) transfers this identification to finite Euler with empirical feedback. All factors involving the readout can be clipped beyond its proven supremum bound without changing any oracle value. For comparisons the roots stay fixed: \(J\) and its first activation are uniformly Lipschitz in their changing clock arguments. A joint global Lipschitz bound in the frozen root is neither asserted nor needed.

Consequently, taking \(n\to\infty\) at fixed \(\Delta\), and then \(\Delta\to0\), proves the population limit of the finite continuous flow on every \([0,T]\).

#### The bridge from exact GD

A scalar estimate makes the discrete argument work even when the first derivative vanishes or changes sign. In the following calculation only, write
\[
A=(\phi^{(1)})',
\qquad L=\operatorname{Lip}(A),
\qquad
z^+=z+\eta A(z)b.
\]
If \(L\eta|b|\le1/2\) and \(A(z)\ne0\), then for \(0\le s\le1\),
\[
|A(z+s\eta A(z)b)-A(z)|
\le L\eta|A(z)b|
\le \frac{|A(z)|}{2}.
\]
The whole segment stays in the same interval where \(A\ne0\). Define its exact scalar-flow clock increment by
\[
\Delta X=\int_z^{z^+}\frac{du}{A(u)}.
\]
Then \(z^+=J(\Delta X,z)\). Substitution in the integral gives
\[
\begin{aligned}
|\Delta X-\eta b|
&\le
\eta|b|\int_0^1
\left|
\frac{A(z)}{A(z+s\eta A(z)b)}-1
\right|\,ds\\
&\le L\eta^2b^2.
\end{aligned} \tag{17}
\]
If \(A(z)=0\), the raw step fixes \(z\). Set \(\Delta X=\eta b\); the same exact representation holds because \(J(s,z)=z\) at an equilibrium. If \(L=0\), the derivative is constant and there is no coordinate defect or step restriction.

Apply (17) to each coordinate with
\[
b_a
=
-2\kappa_1r_{n,a}
(W^{(2)})^\top\delta_a^{(2)}.
\tag{18}
\]
The raw GD trajectories themselves have width-independent bounds on \([0,T]\). First,
\[
|r_{n,a}|
\le |y_a|+B_2\|W^{(3)}\|_\infty
\]
and the readout update give a discrete Gronwall bound on its supremum. This bounds \(\delta_a^{(2)}\). The first raw update then has root-mean-square increment at most \(C_T\eta_n\|W^{(2)}\|_{\mathrm{op}}\), while the matrix operator increment is at most
\[
C_T\eta_n
\left(
1+\sum_a\frac{\|z_a^{(1)}\|_2}{\sqrt n}
\right).
\]
Adding these bounds gives a second discrete linear Gronwall estimate. The initial root RMS and matrix operator norm are bounded with probability tending to one, and the allowed readout initializations have the requisite high-probability uniform supremum bound. On these events,
\[
\frac{\|b_a\|_2}{\sqrt n}\le C_T,
\qquad
\|b_a\|_\infty\le C_T\sqrt n.
\tag{19}
\]
Thus \(\eta_n\sqrt n\to0\) enforces the scalar step condition throughout the interval.

Lift the raw iterates recursively by these exact clock increments, starting from \(x_{a,0}^{(1)}=0\). The scalar flow identity ensures
\[
z_{a,k}^{(1)}
=
J(x_{a,k}^{(1)},z_{a,0}^{(1)})
\]
exactly at every step. The lifted first update differs from transformed Euler by at most
\[
\begin{aligned}
L\eta_n^2
\left(\frac1n\sum_i b_{a,i}^4\right)^{1/2}
&\le
L\eta_n^2\|b_a\|_\infty
\frac{\|b_a\|_2}{\sqrt n}\\
&\le C_T\eta_n^2\sqrt n
\end{aligned}
\tag{20}
\]
in root-mean-square norm.

It is important that the clocks themselves stay in the common Lipschitz region, including when \(J\) has equilibria and cannot be inverted. Summing their exact increments gives
\[
\begin{aligned}
\frac{\|x_{a,k}^{(1)}\|_2}{\sqrt n}
&\le
\sum_{j<k}
\left[
\eta_n\frac{\|b_{a,j}\|_2}{\sqrt n}
+
L\eta_n^2\|b_{a,j}\|_\infty
\frac{\|b_{a,j}\|_2}{\sqrt n}
\right]\\
&\le C_T(1+\eta_n\sqrt n),
\qquad k\eta_n\le T.
\end{aligned}
\tag{21}
\]
Thus the transformed stability constant remains width-independent.

The other parameter updates are already Euler updates for (6). Add their ordinary \(O_T(\eta_n^2)\) local flow error and sum the stable recurrence:
\[
\sup_{t\le T}
d_n\!\left(
\text{lifted GD}(t),\text{finite flow}(t)
\right)
\le
C_T(\eta_n+\eta_n\sqrt n).
\tag{22}
\]
At interpolation times, the scalar flow segment and the linear raw segment differ by the same vanishing bound; the state movement inside one step is \(O_T(\eta_n)\). This proves the raw GD bridge without a moment assumption on an unshifted scalar transform.

Combining (22), the fixed-mesh oracle limit, and the two \(O_T(\Delta)\) mesh errors proves the joint width/step conclusion.

For the remaining quadratic measurements, the backward fields
\[
(W^{(2)}(t))^*\delta_a^{(2)}(t)
\]
form a compact time-indexed family in \(L^2\). Their squared tails therefore vanish uniformly as the clipping threshold grows. Clip before multiplying by \((\phi^{(1)})'(Z_a^{(1)})\), pass the resulting bounded Lipschitz measurements through the proved limit, and remove clipping. Fixed-grid second-moment convergence and state continuity give the corresponding finite empirical tail control. This supplies kernel entries and squared hidden velocities without assuming sub-Gaussian tails.

For completeness, uniform velocity-energy bounds also supply the path-law assertion. For a time grid of spacing \(h\), let \(\pi_h t\) be its preceding grid point. Cauchy–Schwarz on each coordinate gives
\[
\frac1n\sum_i
\sup_{t\le T}
|z_i(t)-z_i(\pi_h t)|^2
\le
h\int_0^T
\frac{\|\dot z(t)\|_2^2}{n}\,dt.
\tag{23}
\]
The population counterpart replaces the empirical average by expectation. The parameter bounds above and the bounded activation derivatives bound these integrals uniformly for each hidden layer. Piecewise-linear reconstruction from the same grid satisfies an analogous estimate with a fixed additional factor. At fixed grid size the joint laws converge with second moments; letting \(h\to0\) gives convergence of the hidden path laws with their second moments in the uniform path norm. The clipped backward-field argument likewise identifies the integrated squared speeds.

#### Examples and the input-geometry boundary

Either layer may use arctan, tanh, logistic sigmoid, erf with fixed nonzero input scaling, softsign \(z/(1+|z|)\), or the smooth saturation \(z/\sqrt{1+z^2}\). Sine and cosine also qualify, despite derivative zeros and sign changes. Softsign is not twice continuously differentiable at zero, but
\[
\frac{d}{dz}\frac{z}{1+|z|}
=
\frac1{(1+|z|)^2}
\]
is continuous, bounded, and globally Lipschitz, which is enough.

In the first layer only, affine functions, softplus, GELU, and SiLU also qualify: their derivatives are bounded and globally Lipschitz although the activations are unbounded. ReLU, leaky ReLU, hard tanh, and derivative-jump activations are not covered by this theorem.

For a general input Gram matrix
\[
G_{ab}=\frac{x_a^\top x_b}{d},
\]
the first-layer equation becomes
\[
\dot Z_a^{(1)}
=
-2\kappa_1\sum_b
G_{ab}r_b
(\phi^{(1)})'(Z_b^{(1)})
(W^{(2)})^*\delta_b^{(2)}.
\tag{24}
\]
With a nonlinear first activation, the right side is not the \(a\)-th activation derivative times one scalar backward coefficient. The scalar-coordinate proof therefore does not give a global-time arbitrary-angle theorem.

There is a verified exception. If
\[
\phi^{(1)}(z)=cz+d_0,
\]
then
\[
\dot Z_a^{(1)}
=
-2\kappa_1c\sum_b
G_{ab}r_b(W^{(2)})^*\delta_b^{(2)}.
\tag{25}
\]
The troublesome multiplication by a varying first-layer derivative has disappeared. In the raw state
\((Z_1^{(1)},\ldots,Z_m^{(1)},W^{(2)},W^{(3)})\),
the vector field is Lipschitz on the same bounded sets. The bounds (13)–(14) hold with raw first-layer norms and constants depending on the fixed \(G\). The fixed-program initialization allows the possibly singular Gaussian covariance \(\sigma_1^2G\). The same oracle and mesh proof therefore gives a global population limit for **any fixed finite normalized input configuration**, including singular Gram matrices.

In this affine case, raw GD is already ordinary Euler for the Lipschitz raw vector field, so the sufficient step condition improves to \(\eta_n\to0\). All the preceding readout restrictions remain. This exception does not give a nonlinear first layer: its best affine-fit error is exactly zero.


<!-- END EXCERPT -->

<!-- BEGIN docs/global_nonlinear.md:3972-4296 -->

#### C.4.1. Full-row transport comparison

##### 1. State, finite interpretation, and exact field

Write `u=x/sqrt(2)`, so `|u|=1`, and put `phi=tanh`. Let
`H_1=L2(Omega_1)` and `H_2=L2(Omega_2)` be real probability Hilbert spaces
with their coordinate operations. A population state is

\[
 \theta=(w,A,c)\in L^2(\Omega_1;\mathbb R^2)
       \times\mathcal B(H_1,H_2)\times H_2.
\]

The vector field preserves the affine class `A=A_0+K` where `K` is a
norm-limit of finite-rank operators: the rank-one integrand in (T2) is
continuous on the compact data support, so finite simple approximations
converge in operator norm, as do their time integrals. Define

\[
\begin{aligned}
 Z^1_\theta(u)&=w\cdot u,& H^1_\theta(u)&=\phi(Z^1_\theta(u)),\\
 Z^2_\theta(u)&=A H^1_\theta(u),& H^2_\theta(u)&=\phi(Z^2_\theta(u)),\\
 f_\theta(u)&=\langle c,H^2_\theta(u)\rangle_{H_2},&
 r_\theta(u,y)&=f_\theta(u)-y,\\
 P^2_\theta(u)&=c,&\delta^2_\theta(u)&=\phi'(Z^2_\theta(u))c,\\
 P^1_\theta(u)&=A^*\delta^2_\theta(u),&
 \delta^1_\theta(u)&=\phi'(Z^1_\theta(u))P^1_\theta(u).
\end{aligned}                                                   \tag{T1}
\]

All pairings use a single neuron population. The population rank-one
operator is `(a tensor b)v=a E_1[bv]`. For a probability law `mu` of `(u,y)`
on `S^1 x [-Y,Y]`, the exact mean-square-loss physical vector field is

\[
 F_\mu(\theta)=\left(
 -2\int r_\theta\delta^1_\theta u\,d\mu,
 -2\int r_\theta\delta^2_\theta\otimes H^1_\theta\,d\mu,
 -2\int r_\theta H^2_\theta\,d\mu\right).                         \tag{T2}
\]

In the first integral the scalar field multiplies the explicit input
vector `u`, producing a two-component row. For a finite network, take
`w=W^(1)`, `A=W^(2)`, `c=W^(3)`, replace field norms by the Euclidean or
Frobenius norm divided by `sqrt(n)`, inner products by `a^T b/n`, and
rank-one actions by `a b^T/n`. Formula (T2) then gives exactly the raw
stored-weight mobilities `(n,1,n)`, as follows from
`docs/finite_dynamics.md` §§1–2. Raw GD is
`theta_(j+1)=theta_j+eta F_mu(theta_j)` with all three blocks evaluated at
the preceding state. Parameter interpolation does not interpolate hidden
features: (T1) is recomputed at the interpolated parameters.

On a common carrier define

\[
 D(\theta,\bar\theta)=\|w-\bar w\|_{L^2(\Omega_1;\mathbb R^2)}
                  +\|A-\bar A\|_{\rm op}+\|c-\bar c\|_{L^2(\Omega_2)}. \tag{T3}
\]

For two networks of the same width, its finite counterpart is

\[
 D_n(\theta,\bar\theta)
 =\frac{\|W^{(1)}-\bar W^{(1)}\|_F}{\sqrt n}
  +\|W^{(2)}-\bar W^{(2)}\|_{\rm op}
  +\frac{\|W^{(3)}-\bar W^{(3)}\|_2}{\sqrt n}.       \tag{T3a}
\]

The finite norms in (T3a) are ordinary Frobenius, operator and Euclidean
norms. This distance controls the full first matrix. No cross-width or
finite-to-population operator distance is used anywhere in this proof.

The bound `|phi|<=1`, `|phi'|<=1`, and `Lip(phi')<=2` will be used throughout.
If every individual state norm is at most `B>=1`, then, for every input,

\[
 \|H^1\|_2,\|H^2\|_2\le1,\quad
 \|\delta^2\|_2\le B,\quad \|P^1\|_2,\|\delta^1\|_2\le B^2,
 \quad |f|\le B,\quad |r|\le B+Y.                                \tag{T4}
\]

Consequently the sum of the three velocity norms is at most
`V=2(B+Y)(B^2+B+1)`. If initial individual norms are at most `S_0`, choose
`B=2S_0+2` and

\[
 T_{\rm ball}=\min\{1,(B-S_0)/(4V)\}>0.                          \tag{T5}
\]

The integral-flow first-exit argument and the sum of Euler increments show
that both stay inside this ball up to `2T_ball` for Euler mesh at most
`T_ball`: before a putative first exit the increment of each norm is at most
`2T_ball V<(B-S_0)`. Piecewise affine interpolants have speed bounded by
`V`. These bounds hold for every probability law and every finite empirical
law, regardless of its cardinality.

For the specified initialization, `||W^(1)_0||_F^2/n` tends in probability
to `2`, and `||W^(3)_0||_2^2/n` has expectation `n^(-2)`. The initialized
middle operator is bounded with probability tending to one by the elementary
sphere-net argument in finite dynamics §4. Thus a fixed `S_0` gives a common
high-probability finite ball, independent of the training data. The population
root is the full row `w_0=(g_1,g_2)` with independent standard normals and
`c_0=0`. Retaining the second root coordinate remains necessary even if a
reference training law sees only the first coordinate.

##### 2. The one-reference transport estimate

For a field `P`, write `tau_R(P)=||P 1_{|P|>R}||_2`. If the reference
state is `bar theta`, set

\[
 \mathfrak T_{\nu,R}(\bar\theta)
 =\tau_R(\bar c)+\int\tau_R(P^1_{\bar\theta}(u'))\,
                                  \nu(du',dy').                    \tag{T6}
\]

At finite width these are individual empirical neuron RMS tails. In
particular, for a finite reference law with weights `omega_b`, the second
term is the weighted sum of the individual reference tails, not a tail of a
maximum over the reference inputs or over the actual dataset.

**Transport lemma.** On the ball above, for every `R>=1`, every two laws
`mu,nu`, and every two states on the same carrier,

\[
 \|F_\mu(\theta)-F_\nu(\bar\theta)\|_{T3}
 \le C(1+R)\bigl(D(\theta,\bar\theta)+\mathcal W_1(\mu,\nu)\bigr)
       +C\mathfrak T_{\nu,R}(\bar\theta).                           \tag{T7}
\]

Here `W1` uses `|u-u'|+|y-y'|`, and `C` depends only on `B,Y`. The same
constant works for the normalized finite-network norms and actions. Only
the reference state requires tails.

**Proof.** Fix any coupling `pi` of the two laws, and abbreviate
`h=|u-u'|`, `D=D(theta,bar theta)`. Keeping the full first row gives

\[
 \|Z^1_\theta(u)-Z^1_{\bar\theta}(u')\|_2
 \le\|w-\bar w\|_2+\|\bar w\|_2 h\le D+Bh.
\]

The activation is 1-Lipschitz. Expanding
`A H^1-bar A bar H^1=(A-bar A)H^1+bar A(H^1-bar H^1)` therefore gives

\[
 \max_{\ell=1,2}\bigl(\|Z^\ell_\theta(u)-Z^\ell_{\bar\theta}(u')\|_2
          +\|H^\ell_\theta(u)-H^\ell_{\bar\theta}(u')\|_2\bigr)
       \le C(D+h),                                                   \tag{T8}
\]
\[
 |f_\theta(u)-f_{\bar\theta}(u')|\le C(D+h),\qquad
 |r_\theta(u,y)-r_{\bar\theta}(u',y')|
                         \le C(D+h)+|y-y'|.                         \tag{T9}
\]

For any two preactivations and any reference field `bar P`, pointwise
splitting at `|bar P|=R` gives

\[
 \|[\phi'(Z)-\phi'(\bar Z)]\bar P\|_2
       \le2R\|Z-\bar Z\|_2+2\tau_R(\bar P).                        \tag{T10}
\]

For the top backward field, split its difference as
`phi'(Z^2)(c-bar c)+[phi'(Z^2)-phi'(bar Z^2)]bar c`. Thus

\[
 \|\delta^2_\theta(u)-\delta^2_{\bar\theta}(u')\|_2
       \le C(1+R)(D+h)+2\tau_R(\bar c).                             \tag{T11}
\]

Expanding the adjoint difference, and using (T4), bounds the corresponding
`P^1` difference by `B` times (T11) plus `BD`. Split the first backward
field in the same way, now applying (T10) to `P^1_bar theta(u')`. The result is

\[
 \|\delta^1_\theta(u)-\delta^1_{\bar\theta}(u')\|_2
 \le C(1+R)(D+h)
       +C\tau_R(\bar c)+2\tau_R(P^1_{\bar\theta}(u')).                \tag{T12}
\]

There is one power of `R`: the earlier backward error is multiplied only
by a bounded operator and bounded activation derivative. The new gate
cutoff adds an `R` term and does not multiply that earlier error by `R`.

For the first-weight integral the exact decomposition is

\[
\begin{aligned}
 r\delta^1u-\bar r\bar\delta^1u'
  &=(r-\bar r)\delta^1u
    +\bar r(\delta^1-\bar\delta^1)u
    +\bar r\bar\delta^1(u-u').
\end{aligned}
\]

The row-field norm of a product `P u` equals `||P||_2 |u|`. Therefore
(T4), (T9), and (T12) bound this difference by
`C(1+R)(D+h+|y-y'|)` plus the two reference tails. This verifies the
explicit changing-input factor in the first-weight gradient.

For the middle integral use the identity

\[
 r\delta^2\otimes H^1-\bar r\bar\delta^2\otimes\bar H^1
 =(r-\bar r)\delta^2\otimes H^1
 +\bar r(\delta^2-\bar\delta^2)\otimes H^1
 +\bar r\bar\delta^2\otimes(H^1-\bar H^1)
\]

and `||a tensor b||_op=||a||_2||b||_2`. Equations (T4), (T8), (T9),
and (T11) give the same bound. The readout integral uses
`rH^2-bar r bar H^2=(r-bar r)H^2+bar r(H^2-bar H^2)` and needs no tail.
Integrate these three estimates against `pi`. Every tail depends only
on the second marginal, so its integral is exactly (T6). Taking the
infimum of the coupling costs proves (T7); existence of an optimal
coupling is unnecessary. All the norm inequalities also hold under the
finite normalized pairings, proving the finite assertion. ∎

The full Gaussian first-row root is not multiplied by a backward field
in this argument. It enters (T8) only through its RMS norm. In particular,
no unproved Gaussian estimate for products of root and backward fields,
no Gaussian maximum over observations, and no Gram inverse is hidden in
(T7).

#### C.4.2. Canonical strong population evolution

##### 1. Initial state and strong equation

Use the fields, exact vector field and full-state topology (T1)–(T3).
Write \(\mathcal H_i=L^2(\Omega_i)\) for the two layer spaces and
\(\mathcal E=L^2(\Omega_1;\mathbb R^2)\times
\mathcal B(\mathcal H_1,\mathcal H_2)\times\mathcal H_2\)
for the complete state space with the sum norm (T3).
Section 2 constructs the two probability spaces, the full first-row Gaussian
root `w_0=(g_1,g_2)~N(0,I_2)`, and the initialized middle action A_0 with
its actual adjoint. Put `theta_0=(w_0,A_0,0)`. The strong equation is

\[
 \theta_\mu(t)=\theta_0+\int_0^t F_\mu(\theta_\mu(s))\,ds.
\tag{P5}
\]

The integral is in full-row L2, middle operator norm and readout L2.
Section 3 proves the required strong integrability and continuity. These
are the same unhalved mean-loss equations and physical clock as (T2).

##### 2. One compatible initialized Gaussian action space

Start the countable language of III.F.7 with the full independent Gaussian
pair \((g_1,g_2)\) at population 1, a zero readout at population 2, constants,
both orientations of one initialized matrix, rational linear combinations,
tanh, smooth clipped products, and a countable family of smooth bounded
globally Lipschitz coordinate functions dense on each finite compact box.
Close under finite composition. The actual finite roots are the two columns
of \(W^{(1)}_0\), and the actual finite action is the same matrix
\(W^{(2)}_0\) in both orientations. They have the required independent laws.

The deterministic finite-program theorem III.F.1, including the proof of
singular-query regularization in III.F.5, identifies the joint limiting law
of every finite collection of these programs. Finite unions share the same
initialized arrays; deleting unused instructions changes no finite vector.
Consequently these joint laws are compatible. The chronological Gaussian
extension construction of III.F.4 and III.F.7 realizes the countable language
on two generated probability spaces. It does not sample a fresh independent
backward answer: independent oriented *source groups* acquire the response
corrections in equations (III.F.9)–(III.F.10).

For clarity, the operator-completion step uses three concrete facts from that
proof. The finite initialized norm obeys

\[
 \mathbb P(\|W^{(2)}_0\|_{\rm op}>10)
 \le2\,9^{2n}e^{-100n/8}\longrightarrow0.
\]

Second-moment convergence passes the inequality
\(\|W^{(2)}_0v\|_2/\sqrt n\le10\|v\|_2/\sqrt n\)
to every rational combination of generated nodes. Exact finite linear
identities and zero squared differences make the limiting assignment
linear and well-defined on its \(L^2\) classes. Generated smooth cylinder
functions are dense in each generated \(L^2\) space: cylinder simple
functions approximate measurable functions, bounded continuous functions
approximate finite-dimensional Borel functions in \(L^2\), and the included
smooth functions approximate those on compact boxes, with tails removed by
truncation. Thus the assignment extends to a bounded map \(A_0\), of norm
at most 10. The reverse assignments extend in the same way. Passing the
exact finite normalized identity

\[
 v^TW^{(2)}_0h/n=((W^{(2)}_0)^Tv)^Th/n
\]

through the finite-program theorem and then through density identifies the
reverse map with \(A_0^*\).

This language can be fixed independently of the training law. Arbitrary
real directions \(u\in S^1\) are limits of rational linear combinations of
the retained root pair; their initial projections have the joint law
\(\mathbb E[(w_0\cdot u)(w_0\cdot v)]=u\cdot v\).
Arbitrary real coefficients in each separately fixed program are obtained
by rational approximation. For continuous coordinate instructions of at
most linear growth, including the backward products in (T1), A.1 supplies
the extension by smooth clipping and \(L^2\) completion. Its proof chooses
one fixed approximation before taking width to infinity and then removes
the approximation, so no growing-program assertion is introduced here.
The response formulas for these fixed neural programs are those in A.2:
bounded derivatives of tanh and its derivative meet the stated hypotheses.

As a result all rational finite laws and rational-mesh Euler calculations,
their finite unions and full first-row updates belong to one common action
realization. A countable list of additional finite laws may equally be
included. Alternatively the preceding completion represents each of their
fixed calculations directly. This construction also includes any finite
list of passive input directions. There is no data-law-dependent arbitrary
extension of the initialized operator and no comparison of a finite matrix
to a population operator in operator norm.

Different causal enumerations have the same finite generated laws because
their finite arrays agree. Their generated spaces are therefore identified
by the \(L^2\) isometry sending each named coordinate expression to its
counterpart. The isometry preserves coordinate operations and intertwines
the actions and adjoints. This is the precise canonical-realization claim.


<!-- END EXCERPT -->

<!-- BEGIN docs/global_nonlinear.md:5465-6585 -->

##### C.4.5.1. The opposite-label reference and its endpoint

###### 1. Full state and exact feature equation

Put `u=x/sqrt(2)`. Work on the canonical generated probability spaces
`H_1=L2(Omega_1)` and `H_2=L2(Omega_2)` with the initialized bounded
Gaussian action `A_0:H_1->H_2` and its actual adjoint. Its operator norm is
at most two, by A.3. The full first row is `w=(w_1,w_2)`, initially
`(g_1,g_2)` with independent standard normal coordinates. The population
readout is `c(0)=0`; this is the limit of the specified finite random
readout, not a modification of finite initialization. Write `A=A_0+K`.
The increment metric is

\[
 \|(v,B,d)\|_{\rm raw}^2
 =\|v\|_{L^2(\Omega_1;\mathbb R^2)}^2+\|B\|_{\rm HS}^2+\|d\|_2^2.       \tag{R1}
\]

Only the increment `K` is Hilbert–Schmidt. Its finite counterpart is exactly
`||dW1||F²/n+||dW2||F²+||dW3||²/n`. This follows because rank-one population
operators have finite representative `uv^T/n` and HS norm `||u||2||v||2`.

Let `phi=tanh`, and, for `a=1,2`, write

\[
 Z_a^1=w_a,\quad H_a^1=\phi(w_a),\quad Z_a^2=AH_a^1,\quad
 H_a^2=\phi(Z_a^2).
\]
\[
 y_1=1,\ y_2=-1,\qquad h=\frac12(H_1^2-H_2^2),\quad
 b=\langle c,h\rangle=\frac12(f_1-f_2).
\]

For hidden increments `(v,B)`, define the bounded linear map into `H_2`

\[
 J(v,B)=\frac12\sum_{a=1}^2y_a \phi'(Z_a^2)
              \{BH_a^1+A(\phi'(Z_a^1)v_a)\}.                          \tag{R2}
\]

This is the directional differential of `h`; an unrestricted Frechet
statement for an L2-valued Nemytskii map is neither used nor true in general.
Pairing each term with a fixed `c` and using the actual adjoint gives

\[
 J^*c=\left(
  (\tfrac12y_a \phi'(Z_a^1)A^*(\phi'(Z_a^2)c))_{a=1,2},\quad
  \tfrac12\sum_a y_a(\phi'(Z_a^2)c)\otimes H_a^1\right).               \tag{R3}
\]

The HS adjunction is
`<q tensor v,B>HS=<q,Bv>2`; thus (R3) uses exactly (R1).
Consider the autonomous feature equation

\[
                 c_s=h,\qquad (w,K)_s=J^*c.                  \tag{R4}
\]

It has a unique global solution for every finite feature horizon. Here is
the necessary specialization of B.1, including the change from its sum loss.
Let `j(X,g)` solve `j_X=phi'(j)`, `j(0,g)=g`. Its scalar vector field is
bounded by one and Lipschitz, so it exists for all real `X`. It obeys
`|j(X,g)-j(Y,g)|<=|X-Y|`. Set `w_a=j(X_a,g_a)` and solve

\[
 (X_a)_s=\tfrac12y_a A^*(\phi'(Z_a^2)c),\quad
 K_s=\tfrac12\sum_a y_a(\phi'(Z_a^2)c)\otimes H_a^1,\quad c_s=h.       \tag{R5}
\]

On bounded clock-L2/operator/readout-supremum sets these equations are
Lipschitz in the sum of clock L2, operator norm, and readout L2 distances:
`H1` is Lipschitz in the clock with constant one; `H2` is Lipschitz in its
preactivation; and
`||phi'(Z2)c-phi'(Z2bar)cbar||2<=||c-cbar||2+2||cbar||infty||Z2-Z2bar||2`.
The rank-one difference estimate and bounded action/adjoint then control
all three right sides. The closed readout-supremum condition is complete
in L2 and its integral update preserves an enlarged bound on a short
interval. Contraction of that integral map gives local existence and
uniqueness. Moreover, directly from (R5),

\[
 \|c(s)\|_\infty\le s,\quad \|K(s)\|_{\rm HS}\le s^2/2,
 \quad \|A(s)\|_{\rm op}\le2+s^2/2,
\]
\[
 \|w(s)-w(0)\|_2
 \le {1\over\sqrt2}\int_0^s(2+v^2/2)v\,dv.                  \tag{R6}
\]

The same bound holds for the clock norm in the last display. These
polynomials prevent escape from the required bounded sets on every finite
horizon; the integrated equations give a strong limit at a finite proposed
endpoint and the same local construction extends it. Rank-one continuity
upgrades `K` to a strongly C1 HS curve. Bounded-multiplier continuity
upgrades `w` to a strongly C1 L2 curve and proves (R4). Conversely, the
scalar equation `w_s=B(s)phi'(w)` has the unique representation
`j(integral B,g)`: Fubini makes `B` integrable at almost every coordinate,
and the scalar integral Lipschitz inequality gives uniqueness. Thus these
are the actual raw feature equations, not an alternative optimizer.

The Gaussian action used here is the canonical common action of B.1:
countably many finite generated programs, their finite unions, both matrix
orientations, and passive input probes are realized jointly before
completion. Continuous at-most-linear value instructions `j` are admitted
by A.1. The same-root Lipschitz estimate just given supplies the empirical
feedback passage. No bounded derivative with respect to the Gaussian root
is required. At a current state, resetting clock zero and retaining the
current raw fields/action gives the same unique continuation, so the raw
reference is autonomous and restartable. This construction supplies a
complete actual-state endpoint characterization below; it encodes no
future trained trajectory in its coefficients.

###### 2. Symmetry, fitting, and the two clocks

Let `P(u_1,u_2)=(u_2,u_1)`. The raw transformation
`(w,A,c)->(wP,A,-c)` maps predictions to `-f(Pu)`. Direct substitution in
(R3)–(R4) shows that it preserves the feature vector field, since `h`
changes sign and the two labels exchange signs. It also preserves the
physical vector field for the probability law
`nu_*=1/2 delta_(e1,+1)+1/2 delta_(e2,-1)` in normalized inputs.
The initial full-row Gaussian law is invariant under swapping its two
coordinates; the independent initialized matrix law is unchanged and
`c0=0` changes to itself. At the generated-action level this statement is
obtained by adjoining the swapped version of every finite program to the
same countable construction. Finite joint laws are invariant; hence the
coordinate swap is a probability-space isometry that respects coordinate
operations, the action and its adjoint. The unique integral construction
commutes with it. Therefore the deterministic predictions satisfy

\[
                 f(Pu)=-f(u),\qquad f_1=b=-f_2.                \tag{R7}
\]

This is symmetry of the population action law, not pointwise symmetry of a
particular finite initialized network. No such finite symmetry is assumed.
Oddness of both activations also gives `f(-u)=-f(u)`.

For the mean squared loss the reference residuals are `(b-1,1-b)`.
The exact physical equations of C.4.1 therefore equal `2(1-b)` times
(R4). The correct clock is

\[
                 {ds\over dt}=2(1-b),\qquad s(0)=0.           \tag{R8}
\]

To prove that this clock is legitimate through all physical times, first
work with the globally defined feature equation. The strong curve chain
rule gives `h_s=J(w,K)_s`. Indeed bounded continuous multiplication is
strongly continuous on a fixed L2 vector after truncating that vector;
the scalar fundamental theorem of calculus then proves
`(phi(z))_s=phi'(z)z_s` for strongly C1 L2 curves. Differentiating a bounded
operator times a strongly C1 vector by adding and subtracting its factors
gives the ordinary product rule. Applied successively to (R2) this gives

\[
 c_{ss}=JJ^*c,\qquad
 b_s=\|h\|_2^2+\|J^*c\|_{\rm hidden}^2
                  =\|\theta_s\|_{\rm raw}^2.                 \tag{R9}
\]

The metric in the second term is the row-L2 plus HS hidden metric from
(R1). No derivative of `J` is taken in (R9).

Set `m=||h(0)||2²`. Initially the two first features are independent odd
functions of independent standard normals, so their Gram is `q I_2`, where

\[
 q=E\tanh^2G,\qquad v=E\tanh^2(\sqrt qG),\qquad m=v/2.        \tag{R10}
\]

The initial second preactivations are independent `N(0,q)` by the initial
forward Gaussian law. The elementary certificate in §5 proves

\[
                         m\ge m_0:=1/10.                     \tag{R11}
\]

On every interval where `g=||c||2>0`, differentiating its scalar norm gives

\[
 g_s=b/g,\qquad
 g_{ss}=\frac{\|h\|_2^2-(g_s)^2+\|J^*c\|_{\rm hidden}^2}{g}
                                                          \ge0.\tag{R12}
\]

Cauchy–Schwarz gives the inequality. Since `c(s)=s h(0)+o_L2(s)` and
`h(s)->h(0)`, one has `g_s(0+)=sqrt(m)`. Consequently on its first
positive interval `g_s>=sqrt(m)` and `g>=s sqrt(m)`. It cannot reach zero
again at a positive endpoint, so this interval is all positive feature
times. Again by Cauchy–Schwarz, `||h||2>=g_s`, and (R9) gives

\[
                         b_s\ge m\ge m_0.                    \tag{R13}
\]

Hence there is exactly one first feature time `s_dagger` with `b=1`, and
`0<s_dagger<=1/m<=10`. On `[0,s_dagger)`, define

\[
 t(s)=\int_0^s\frac{dv}{2(1-b(v))}.                           \tag{R14}
\]

Its integrand is positive. Since `b_s` is continuous and bounded on the
compact feature interval `[0,s_dagger]`, say by `K`,
`1-b(s)<=K(s_dagger-s)`; thus the integral diverges as
`s->s_dagger`. Its inverse is defined for every `t>=0` and obeys (R8).
It is the unique B.1 physical reference by uniqueness of the original raw
equation. Writing `e(t)=1-b(s(t))`, differentiation gives

\[
 e_t=-2b_s e,\quad 0<e(t)\le e^{-2m t}\le e^{-t/5},\qquad
 R_{\nu_*}(f_*(t))=e(t)^2\le e^{-2t/5}.                       \tag{R15}
\]

There is no finite physical time at which the residual first vanishes:
the displayed linear scalar equation with locally bounded coefficient
and initial value one keeps it positive. This also checks the clock sign.

###### 3. Actual endpoint and uniform prediction convergence

By (R9) and Cauchy–Schwarz, for `0<=s_1<=s_2<=s_dagger`,

\[
 \|\theta(s_2)-\theta(s_1)\|_{\rm raw}
 \le\sqrt{(s_2-s_1)(b(s_2)-b(s_1))}.                          \tag{R16}
\]

The state is already globally defined in feature time. Its endpoint is
precisely the solution of (R4)–(R5) stopped at the uniquely characterized
first level `b=1`; denote it `(w_dagger,A_dagger,c_dagger)`. Define on the
whole circle

\[
 f_*^\infty(\sqrt2u)
 =\langle c_\dagger,\tanh(A_\dagger\tanh(w_\dagger\cdot u))\rangle.
                                                                  \tag{R17}
\]

Thus (R17) is a characterization through the actual autonomous dynamics,
including its initialized Gaussian action and adjoint. It is not merely a
name for an unknown prediction limit. It gives `f∞(sqrt2 e1)=1`,
`f∞(sqrt2 e2)=-1` and the two symmetries in (R7).

Equations (R13),(R16) imply

\[
 s_\dagger-s(t)\le e(t)/m,\qquad
 \|\theta(s(t))-\theta(s_\dagger)\|_{\rm raw}\le e(t)/\sqrt m.
                                                                  \tag{R18}
\]

In particular throughout this interval

\[
 \|c\|_2\le\sqrt{10},\quad \|A\|_{op}\le2+\sqrt{10},\quad
 \|w\|_2\le\sqrt2+\sqrt{10},\quad \|c\|_\infty\le10.           \tag{R19}
\]

For any `|u|=1`, strong directional differentiation and the same
adjunction as above give three raw gradient blocks for `f(u)` with norms
at most `||A||op||c||2`, `||c||2`, and one, respectively. Equivalently,
add and subtract the three endpoint factors and use the one-Lipschitz
activations. The straight segment between two reference states retains
(R19). Integrating the scalar derivative along this segment proves

\[
 \sup_{|u|=1}|f_\theta(u)-f_{\bar\theta}(u)|
 \le C\|\theta-\bar\theta\|_{\rm raw},\quad
 C=\sqrt{1+10\{1+(2+\sqrt{10})^2\}}<17.                       \tag{R20}
\]

This holds simultaneously for all inputs; no finite grid substitutes for
the circle. Combining it with (R15),(R18),

\[
 \sup_{x\in\sqrt2S^1}|f_*(t,x)-f_*^\infty(x)|
 \le 17\sqrt{10}\,e^{-t/5}.                                  \tag{R21}
\]

The explicit choice

\[
                              T=40                           \tag{R22}
\]

therefore has endpoint error less than `1/32`: `17 sqrt(10)e^-8<.019<1/32`.
Its reference risk is at most `e^-16<1/1024`. These are strict margins.
For example the elementary Taylor lower sum for `e^8` already proves the
stated inequalities, so no numerical solver for the trained flow is used.

Input regularity also follows directly from the full-row norm:

\[
 |f_\theta(\sqrt2u)-f_\theta(\sqrt2v)|
 \le\sqrt{10}(2+\sqrt{10})(\sqrt2+\sqrt{10})|u-v|<76|u-v|.    \tag{R23}
\]

The endpoint satisfies the same estimate. Also `||f||infty<=sqrt10`.
For binary labels, `(f(u)-y)^2` is therefore Lipschitz in the prescribed
joint transport cost with constant at most
`2(sqrt10+1) max(76,1)<633`; use
`|(a-y)^2-(b-z)^2|<=2(sqrt10+1)(|a-b|+|y-z|)`.
This proves the exact input regularity needed for risk transport.

For a general target error `epsilon>0`, the same reference component gives
`T(epsilon)=max(0,5 log(17 sqrt10/epsilon))`. Changed-law radii for this
choice remain a separate comparison conclusion and may shrink with epsilon.

###### 4. Both hidden activations move at the fixed time 1/200

This section uses the actual opposite-label reference and retains paired
initial/current observations. Put `Y_a=A0 H0_a^1`; let

\[
 h_0=(\tanh Y_1-\tanh Y_2)/2,\quad
 U_a=h_0\phi'(Y_a),\quad P_a=A_0^*U_a,\quad
 V_a=\phi'(g_a)^2P_a,
\]
\[
 R_a=qU_a+A_0V_a,\qquad
 a_0=E\phi'(G)^4,\quad r_0=E\phi'(\sqrt qG)^2.                \tag{R24}
\]

All fields are typed: `U,R` live in layer two, and `P,V` in layer one.
The Gaussian integration certificate proves `q>.39`, `q<.4`,
`v>.2`, `a0>.3`, and `r0>.6`.

Here is a complete fixed initial reuse calculation establishing positivity
and the needed moments. Let `C_ab=E[U_a U_b]`. Gaussian conditioning on
the first two forward calls gives

\[
 P_a=\sum_{b=1}^2p_{ab}\tanh g_b+\Gamma_a,\quad
 p_{ab}=E[Y_bU_a]/q,\quad \Gamma\sim N(0,C),                  \tag{R25}
\]

independently of `(g1,g2)`. This is the actual transpose response, not a
fresh-matrix replacement. For completeness, the finite conditional
Gaussian matrix has its mean fixed on the two forward query directions
and independent Gaussian randomness on their orthogonal complement.
Applying its transpose to `U` gives the first term in (R25) and a Gaussian
with covariance `E[UU^T]`; projections onto the finitely many old first
query directions have expected squared RMS `O(1/n)` and disappear.
The joint initial forward Gram is `q I`, so no inverse at a degeneracy is
involved here. Bounded smooth `U(Y)` permits the fixed-program law and
contractions. Truncating the products by bounded gates and using their
fixed Gaussian moment envelopes permits the same conclusion for `V`.

The matrix `C` is positive definite. If `z1 U1+z2 U2=0` almost surely,
Gaussian full support and continuity give
`(tanh Y1-tanh Y2)(z1 phi'(Y1)+z2 phi'(Y2))=0` everywhere.
On the dense open set `Y1!=Y2` the second factor vanishes and continuity
extends this identity everywhere. Varying each coordinate and using the
nonconstant function `phi'` forces `z1=z2=0`.

Let `alpha_b=E[H0_b^1 V_a]/q`,
`V_a^perp=V_a-sum alpha_b H0_b^1`, and
`sigma_a²=E[(V_a^perp)²]`. Conditioning the same Gaussian matrix on the
forward calls and the reverse calls in (R25) gives

\[
 A_0 V_a=\sum_b\alpha_bY_b+\bar d\,U_a+\sigma_a\gamma_a,
 \quad \bar d=E\phi'(G)^2,                                  \tag{R26}
\]

where `gamma_a` is standard normal independent of the old layer-two
coordinates, for each fixed `a`. Independence between `gamma1,gamma2`
is not claimed. To verify the response coefficient, the conditional
matrix formula gives `C^-1 E[P V_a^perp]` for the coefficient of `U`.
The deterministic part of each `P_b` is in the span of the first forward
inputs and pairs to zero with `V_a^perp`. The remaining pairing is
`E[Gamma_b Gamma_a] E phi'(G)^2=C_ba bar d`; multiplication by `C^-1`
gives `bar d` in coordinate `a`. The unused Gaussian input variance is
`sigma_a²`. Its finite output projection off the two old reverse input
directions again has vanishing RMS. These calculations prove (R26)
without suppressing either reused response term.

Conditional variance in (R25) and projection off functions of the roots
give

\[
 \|V_a\|_2^2\ge C_{aa}a_0,\qquad
 \sigma_a^2\ge C_{aa}a_0,\qquad
 \|\phi'(Y_a)R_a\|_2^2\ge C_{aa}a_0 r_0.                    \tag{R27}
\]

The last inequality conditions on the old second-layer coordinates in
(R26); all its other terms are functions of those coordinates. By
independence and oddness of the initial `Y1,Y2`,

\[
 C_{aa}=\tfrac14 E[(\tanh^2Y_a+v)\phi'(Y_a)^2]
                          \ge vr_0/4>3/100.                  \tag{R28}
\]

Thus each of the two first-order-in-`s²` coefficients has norm at least

\[
 \tfrac14\|V_a\|_2>1/100,\qquad
 \tfrac14\|\phi'(Y_a)R_a\|_2>1/100.                          \tag{R29}
\]

For explicit remainder bounds, (R25) gives `sum_b|p_ab|<=2/sqrt q<4`
and `Caa<=1`. It can be coupled so that `|P_a|<=4+|G|`, and hence
`||P_a||4<6`. For `R>=8` and `z=R-4`, the elementary Gaussian tail
integration yields

\[
 \tau_R(P_a):=\|P_a1_{|P_a|>R}\|_2
 \le\{(4z+68/z)e^{-z^2/2}\}^{1/2}.                           \tag{R30}
\]

Indeed `(|G|+4)^2<=2G²+32`,
`Pr(|G|>z)<=2phi_G(z)/z`, and
`E[G²1_|G|>z]<=2(z+1/z)phi_G(z)`; then drop the density factor
`1/sqrt(2pi)<1`. At `R=10`, the right side is less than `1/1000`.
By bounded action `||V_a||2<=||P_a||2<=2`.
In (R26), the Gaussian linear term has L4 norm at most
`3^(1/4)||V_a||2<3`, the fresh Gaussian term has L4 norm below three,
and `(q+bar d)U_a` has supremum at most two. Therefore `||R_a||4<8`.

We now prove an explicit small-feature-time expansion using only these
fixed initial tails. For `0<=s<=1`, (R6) gives

\[
 \|A\|_{op}\le5/2,\quad \|c\|_\infty\le s,\quad
 \|K\|_{HS}\le s^2/2,\quad
 \|w_a-g_a\|_2\le5s^2/8,
\]
\[
 \|Z_a^2-Y_a\|_2\le7s^2/4,\quad
 \|c-sh_0\|_2\le7s^3/12,\quad
 \|\phi'(Z_a^2)c-sU_a\|_2\le5s^3,
\]
\[
                  \|A^*(\phi'(Z_a^2)c)-sP_a\|_2\le11s^3.           \tag{R31}
\]

For the middle line, `H1` and `H2` are one-Lipschitz, so
`||h(s)-h0||2<=7s²/4`; integrate and then use the two-Lipschitz
second gate. The last line uses `||A||<=5/2`, `||K||<=s²/2`
and the sharper `49s³/12` bound preceding the rounded `5s³`.

Truncate the *fixed initial* `P_a` at `R`. Then

\[
 \|(\phi'(Z_a^1(s))-\phi'(g_a))P_a\|_2
 \le(5R/4)s^2+2\tau_R(P_a).
\]

Subtract `y_a s phi'(g_a)P_a/2` from the first raw feature velocity in
(R3), integrate, and use (R31). The preactivation remainder is bounded by
`(44+5R)s^4/32+tau_R(P_a)s²/2`. For the activation, compare first with
the artificial increment `y_a s² phi'(g_a)P_a/4`; its scalar tanh Taylor
remainder has L2 norm at most `s^4||P_a||4²/16`, since `|phi''|<=2`.
Consequently

\[
 \|H_a^1(s)-H_a^1(0)-y_as^2V_a/4\|_2
 \le\tfrac12\tau_R(P_a)s^2+{116+5R\over32}s^4.                \tag{R32}
\]

The middle velocity differs from
`(s/2)sum y_a U_a tensor H_a^1(0)` by at most `45s³/8` in HS norm:
use (R31), `||U||2<=1`, and `||H1-H10||2<=5s²/8`.
After integration its remainder is at most `45s^4/32`.
Expanding `(A0+K)(H10+Delta H1)` now gives
`Z2_a-Y_a=y_as²(q U_a+A0V_a)/4` with remainder at most
`tau_R(P_a)s²+[2(116+5R)/32+55/32]s^4`. The `55/32` consists of
`45/32` from the middle increment and `5/16` from `K Delta H1`.
The scalar tanh remainder adds `s^4||R_a||4²/16<=4s^4`. Thus

\[
 \|H_a^2(s)-H_a^2(0)-y_as^2\phi'(Y_a)R_a/4\|_2
 \le\tau_R(P_a)s^2+{415+10R\over32}s^4.                      \tag{R33}
\]

At `R=10` and `s<=1/100`, (R29)–(R33) show, for both layers and each
reference input,

\[
           \|H_a^\ell(s)-H_a^\ell(0)\|_2\ge s^2/200.         \tag{R34}
\]

In fact the error coefficient is at most
`.001+(515/32)10^-4<.003<.005`, strictly below half the coefficient
lower bound `.01`.

Choose the fixed **physical** time

\[
                       t_{\rm act}=1/200.                   \tag{R35}
\]

Since `||c(s)||2<=s` and `||h||2<=1`, one has `0<=b(s)<=s`
before the level `b=1`. The clock therefore satisfies
`1-e^-2t<=s(t)<=2t`. At (R35),
`199/20000<=s(t_act)<=1/100`; the lower bound uses
`1-e^-a>=a-a²/2`. Hence the paired RMS averaged over the reference law,

\[
 D_{\ell,*}(t)=\left\{\frac12\sum_{a=1}^2
 E_\ell|H_a^\ell(t)-H_a^\ell(0)|^2\right\}^{1/2},
\]

obeys the explicit strict margin

\[
              D_{\ell,*}(t_{\rm act})>1/2{,}500{,}000,
              \qquad \ell=1,2.                              \tag{R36}
\]

The average uses paired initial and current coordinates on the same layer
population. It is not the Wasserstein distance between separate marginals.
By B.1 the reference finite networks retain this paired observable:
with their actual random initial readout, widths tending to infinity and
actual steps satisfying `eta sqrt(n)->0`, its finite squared value
`(2n)^-1 sum_(a,i)|h_ai^ell(t)-h_ai^ell(0)|²` converges in probability
to `D_(ell,*)²` at this physical time. In particular its RMS exceeds half
(R36) with probability tending to one. Whole-circle law perturbation and
averaging under a nearby `mu`, or its empirical laws, require the separate
transport component; (R36) supplies the positive reference margin for it.
No claim of displacement at time `T=40` is needed or made here.

###### 5. Reproducible rational Gaussian certificate

This is deterministic constant evaluation, not a training experiment.
For `0<=x<=18`, put `S80(x)=sum_(j=0)^80 x^j/j!`. Then

\[
 S_{80}(x)\le e^x\le S_{80}(x)
       +{x^{81}/81!\over1-x/82}.                             \tag{R37}
\]

The upper remainder follows because every subsequent term ratio is at
most `x/82<1`. Quadrature arguments are at most eight; the separate
initial-tail verification uses argument eighteen. Partition `[0,4]` into 1,000 intervals of width `1/250`.
The Gaussian density decreases there and its value at zero lies between
`.3988` and `.3990`; the program certifies the two squared inequalities
using rational alternating bounds for
`pi=16 arctan(1/5)-4 arctan(1/239)`. This identity follows from the tangent
addition formula: `tan(4 arctan(1/5))=120/119`, so subtracting
`arctan(1/239)` gives tangent one at an angle in `(0,pi/2)`.
The alternating arctangent remainder bounds follow by integrating the
finite geometric identity for `1/(1+x²)` from zero to each positive
argument. Use tanh at left endpoints and density at right
endpoints for lower bounds on increasing squared tanh. For decreasing
powers of sech, both right endpoints give lower bounds. For the upper
bound on `q`, use the opposite endpoints and add `1/10000`; the missing
two-sided Gaussian tail beyond four is at most `2phi_G(4)/4<1/10000`.
The function `(E-1)/(E+1)` increases for `E>=1`, whereas
`4E/(E+1)^2` decreases there. Thus (R37) supplies rational bounds for
all required gates. Since `.624²<.39` and `.633²>.4`, the resulting lower
bounds imply the exact `v,a0,r0` bounds used above.

The following complete Python program uses exact rational arithmetic,
rounding each summand outward to denominator `10^12` to prevent growth of
unneeded common denominators. Its assertions are exact integer/rational
comparisons. Decimal output is only a readable summary.

```python
from fractions import Fraction as F
N = 1000
cache = {}
def expb(x):
    if x in cache:
        return cache[x]
    t = S = F(1)
    for j in range(1, 81):
        t = t*x/j
        S += t
    upper = S + t*x/81/(1-x/82)
    cache[x] = (S, upper)
    return S, upper
# Density bounds, with no floating point pi dependency.
def atanb(x):
    lo = sum((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(20))
    return lo, lo+x**41/41
a, b = atanb(F(1,5))
c, d = atanb(F(1,239))
pi_lo, pi_hi = 16*a-4*d, 16*b-4*c
assert 2*pi_hi*F(3988,10000)**2 < 1
assert 2*pi_lo*F(399,1000)**2 > 1
# Two-sided Gaussian tail beyond four is at most phi_G(4)/2.
e8_lo, _ = expb(F(8))
assert F(399,1000)/(2*e8_lo) < F(1,10000)
# Verify the two additional elementary margins used in the proof.
assert F(35334,1000)/expb(F(18))[0] < F(1,1000000)
assert 17*F(3163,1000)/e8_lo < F(1,32)
D = 10**12
def low(z):
    v = z*D
    return F(v.numerator//v.denominator, D)
def high(z):
    return -low(-z)
qlo = qhi = vlo = alo = rlo = F(0)
for j in range(N):
    l, r = F(j,250), F(j+1,250)
    el, _ = expb(2*l)
    _, er = expb(2*r)
    _, dr = expb(r*r/2)
    dl, _ = expb(l*l/2)
    tl, tr = (el-1)/(el+1), (er-1)/(er+1)
    wl = 2*F(3988,10000)/250/dr
    wu = 2*F(399,1000)/250/dl
    qlo += low(wl*tl**2)
    qhi += high(wu*tr**2)
    ev, _ = expb(2*F(624,1000)*l)
    _, ee = expb(2*F(633,1000)*r)
    tv = (ev-1)/(ev+1)
    sa, sr = 4*er/(er+1)**2, 4*ee/(ee+1)**2
    vlo += low(wl*tv**2)
    alo += low(wl*sa**4)
    rlo += low(wl*sr**2)
print([float(z) for z in (qlo, qhi+F(1,10000), vlo, alo, rlo)])
assert qlo > F(39,100) and qhi+F(1,10000) < F(2,5)
assert vlo > F(1,5) and alo > F(3,10) and rlo > F(3,5)
```

Executed with Python 3.10.12, exit zero. Output:

```text
[0.392108947877, 0.396376711612, 0.233120735618,
 0.339792209687, 0.631761866359]
```

The displayed standard-library Python program is the complete reproduction procedure. Its exact rational comparisons certify the weaker bounds m>=.1, a0>.3 and r0>.6 used above. No numerical training solver is needed.


##### C.4.5.2. Quantitative reference response tails

###### 1. Exact feature equations and the bounded reference interval

Put `sigma_1=1`, `sigma_2=-1`, and `phi=tanh`. Let `J` be the global
scalar solution

\[
 J_X(X,g)=\operatorname{sech}^2 J(X,g),\qquad J(0,g)=g,
 \quad H(X,g)=\tanh J(X,g).                                      \tag{R1}
\]

Here `X` is a clock argument; `g` is a fixed Gaussian first-row root.
For each fixed `g`, scalar existence and uniqueness follow from boundedness
and global Lipschitz continuity of `sech²`. In particular
`|J(X,g)|<=|g|+|X|`, `|J(X,g)-J(Y,g)|<=|X-Y|`, and
`H_X=sech⁴ J`, so `|H_X|<=1`. There is no globally bounded derivative
assumption in the root `g`.

The feature equations on the two separate neuron probability spaces are

\[
\begin{aligned}
 H_a^1&=H(X_a,g_a),& Z_a^2&=A H_a^1,&H_a^2&=\phi(Z_a^2),\\
 \delta_a&=c\phi'(Z_a^2),& Q_a&=A^*\delta_a,\\
 X_{a,s}&=\tfrac12\sigma_a Q_a,&
 A_s&=\tfrac12\sum_a\sigma_a\delta_a\otimes H_a^1,&
 c_s&=\tfrac12\sum_a\sigma_a H_a^2 .
\end{aligned}                                                     \tag{R2}
\]

The initialized action and its adjoint are the common Gaussian action,
and `X(0)=0,c(0)=0`. The rank action is
`(v tensor h)z=v E_1[hz]`. At finite width it is `v h^T/n`.
These equations are the actual reference flow under
`ds/dt=2(1-b)`, up to its feature endpoint `s_infty`. They are also a
well-defined auxiliary autonomous feature system beyond that endpoint,
but no estimate below requires that extension.

Write `m=|| (H_1^2(0)-H_2^2(0))/2 ||_2²`. The reference fitting proof
establishes

\[
 m\ge1/10,\quad 0<s_\infty\le1/m\le10,\quad
 \|\theta(s)-\theta(0)\|_{\rm raw}\le\sqrt{s\,b(s)}\le\sqrt{10}
 \quad(0\le s\le s_\infty).                                      \tag{R3}
\]

The raw increment norm is the square sum of the full first-row L2 norm,
the middle Hilbert–Schmidt norm and the readout L2 norm. Therefore
`||A-A_0||HS<=sqrt(10)`, `||c||2<=sqrt(10)`, and (R2) independently gives
`||c(s)||infinity<=s`. The canonical initialized action has norm at most
two; its finite counterpart has norm at most three with probability
tending to one, by the contained proof in global nonlinear A.3.

Only meshes with terminal point at most `s_infty` will be used. For all
sufficiently fine such meshes, their population Euler paths have
`||A-A_0||HS<sqrt(10)+1/10`, `||c||2<sqrt(10)+1/10`.
Here is why the Hilbert–Schmidt assertion follows from the clock proof.
Replace the action difference in B.1's metric by the Hilbert–Schmidt norm
of its learned increment. The forward and adjoint difference bounds still
hold because `||K||op<=||K||HS`; the rank difference bound is identical in
these two norms. The same integrated contraction argument and Euler
recurrence give convergence in this stronger metric on each bounded
interval. This argument applies to (R2), whose controls are fixed signs
instead of residual feedback. Its elementary global finite-feature bounds
are `||c||infinity<=s`, `||A||op<=||A_0||op+s²/2`, and
`sum_a ||X_a||2<=integral_0^s ||A(v)||op v dv`. They provide the bounded
sets needed before using (R3).

At each fixed mesh the finite-program value theorem identifies every
contraction in the finitely many learned ranks. Their HS norm squared is
the finite double sum of the corresponding two Gram entries. Thus the
finite learned increments have the same HS bounds, with an arbitrarily
small slack, with probability tending to one. The finite unforced mesh
therefore lies strictly inside

\[
 \|A\|_{\rm op}<7,\qquad \|c\|_2<4,\qquad
 \|c(s_k)\|_\infty\le s_k .                                      \tag{R4}
\]

The finite initial readout is set to zero only for these auxiliary source
programs. The actual-network reference bridge at the end retains the
specified finite Gaussian readout.

###### 2. The source rule for the tanh clock, including zero forcing

At a fixed mesh with steps `h_k`, set `gamma_ka=h_k sigma_a/2` and make
both forward calls before both reverse calls, followed by simultaneous
updates (R2). On population 1 retain the entire root `(g_1,g_2)`. The scalar
source recursion is

\[
\begin{aligned}
 X_{ka}&=\sum_{r<k}\gamma_{ra} Q_{ra},&H^1_{ka}&=H(X_{ka},g_a),\\
 Z^2_{ka}&=\xi_{ka}+\sum_{r<k,b}a_{ka,rb}\delta_{rb},&
 c_k&=\sum_{r<k,b}\gamma_{rb}\phi(Z^2_{rb}),\\
 \delta_{ka}&=c_k\phi'(Z^2_{ka}),&
 Q_{ka}&=\zeta_{ka}+\sum_{r\le k,b}b_{ka,rb}H^1_{rb},\\
 a_{ka,rb}&=\alpha_{ka,rb}+\gamma_{rb}E_1[H^1_{ka}H^1_{rb}],&
 \alpha_{ka,rb}&=E_1[\partial_{\zeta_{rb}}H^1_{ka}],\\
 b_{ka,rb}&=\beta_{ka,rb}+1_{r<k}\gamma_{rb}E_2[\delta_{ka}\delta_{rb}],&
 \beta_{ka,rb}&=E_2[\partial_{\xi_{rb}}\delta_{ka}].
\end{aligned}                                                     \tag{R5}
\]

The centered source covariances, also between programs sharing the initial
matrix, are

\[
 E_2[\xi_{ka}\xi_{vb}]=E_1[H^1_{ka}H^1_{vb}],\qquad
 E_1[\zeta_{ka}\zeta_{vb}]=E_2[\delta_{ka}\delta_{vb}].             \tag{R6}
\]

The reverse Gaussian group is independent of the full first-row root.
Sources in different orientations belong to independent groups; the actual
matrix answers are dependent through their response terms. Formal
derivatives hold selected expectations, contraction coefficients and
covariances fixed. All named slots are retained even at zero variance.
Their complete chain rules include

\[
\begin{aligned}
 \partial X_{ka}&=\sum_{r<k}\gamma_{ra}\partial Q_{ra},&
 \partial H^1_{ka}&=\operatorname{sech}^4 J(X_{ka},g_a)\partial X_{ka},\\
 \partial c_k&=\sum_{r<k,b}\gamma_{rb}\phi'(Z^2_{rb})\partial Z^2_{rb},&
 \partial\delta_{ka}&=\phi'(Z^2_{ka})\partial c_k
             +c_k\phi''(Z^2_{ka})\partial Z^2_{ka},\\
 \beta_{ka,kb}&=1_{a=b}E_2[c_k\phi''(Z^2_{ka})].
\end{aligned}                                                     \tag{R7}
\]

We justify this source statement, rather than inferring it from values.
Choose a smooth root clipping function `chi_R` equal to the identity on
`[-R,R]`, with bounded image and `|chi_R'|<=1`, and replace `H(X,g)` by
`H(X,chi_R(g))`. Positivity of the scalar gate gives the exact identity

\[
 J_g(X,g)=\frac{\operatorname{sech}^2 J(X,g)}{
                         \operatorname{sech}^2 g}.
\]

One may derive it by differentiating the scalar ODE and solving its scalar
linear variational equation, or by differentiating
`F(J)=F(g)+X`, where `F(z)=z/2+sinh(2z)/4`.
Thus the clipped-root map has bounded first derivatives in both arguments.
Its `X` derivative stays bounded by one uniformly in `R`. Clip the readout
factor smoothly, with the clipping map equal to the identity on an open
neighborhood of the deterministic interval `[-10,10]`; since
`||c||infinity<=s_k<=10`, this changes no program value. All resulting
coordinate instructions now have bounded first derivatives, so III.F.1–5
applies, including its complete Gaussian conditioning proof and its
zero-query-noise argument. Expanding the learned ranks gives exactly (R5).

There is a uniform bound on every first *source* derivative of every fixed
scalar graph while earlier selected coefficients lie in a compact set.
Indeed the recursion has finitely many steps, `H_X` is bounded by one,
`|phi'|<=1`, `|phi''|<=2`, the readout is bounded, and every matrix node
is a source plus a finite linear combination of earlier nodes. Induction
through (R7) gives a finite deterministic bound. This bound is independent
of `R`: derivatives with respect to the root are never taken.

Now remove the root clipping chronologically. A convergent finite
covariance matrix has convergent positive-semidefinite square roots:
boundedness gives subsequential limits, each limit is a nonnegative square
root of the same matrix, and diagonalization gives its uniqueness. Couple
source prefixes using these square roots and fixed standard Gaussians.
At each finite instruction the expressions converge in probability.
The source derivative bound just proved gives uniform integrability of
their derivatives, so expected derivatives converge. Values are bounded or
have a common linear envelope in the finite source/root list, yielding L2
convergence. This closes the chronological induction for both coefficients
and values, even at a singular covariance. In particular the limit of (R7)
is precisely its displayed uncut expression.

These scalar values are the actual finite-program limits. For completeness,
on the same finite arrays the direct change of a first activation caused
by root clipping, at a fixed clock, has RMS at most
`2 [n^(-1) sum_i 1_{|g_ai|>R}]^(1/2)`. The rest of its change is bounded
by the clock RMS change because `|H_X|<=1`. Initial operator bounds and
finite graph subtraction then propagate these errors through every node.
The empirical Gaussian tail frequency converges by the elementary iid
law of large numbers. At each fixed clipping level the finite-program
theorem already applies; first let width grow, then remove clipping.
This identifies the scalar limit above with the uncut value limit.
Scalar contractions are treated in their causal order: their difference
is bounded by the two RMS errors times the bounded RMS factors, so the
same finite induction includes their actual empirical feedback. No
all-moment finite-width theorem or derivative in `g` is used.

Exactly the same argument covers a fresh root added with coefficient
`epsilon` to one complete query answer. For a fixed finite graph its
coefficients and expected source derivatives are continuous as
`epsilon->0`: the causal induction, covariance square-root coupling and
uniform source derivative bounds apply unchanged for `|epsilon|<=1`.
The expression convention fixes derivatives of variance-zero slots.
This continuity is what permits the final zero-forcing limit below.

###### 3. Explicit fresh-root pulse estimates

For two states with the same first roots, use

\[
 d=x+a+z,\quad x=\sum_{a=1}^2\|X_a-\bar X_a\|_2,\quad
 a=\|A-\bar A\|_{\rm op},\quad z=\|c-\bar c\|_2 .              \tag{R8}
\]

At finite width use explicitly
`x_n=sum_a ||X_na-bar X_na||_2/sqrt(n)`,
`a_n=||A_n-bar A_n||op`, and
`z_n=||c_n-bar c_n||_2/sqrt(n)`.
All finite Euclidean norms retain their ordinary meaning.

Suppose both states satisfy `||A||op<=M`, `||c||2<=C`, and
`||c||infinity<=s`. At a feature time `s`, factor subtraction gives

\[
\begin{aligned}
 \sum_a\|\Delta Z_a^2\|_2&\le2a+Mx,\\
 \sum_a\|\Delta\delta_a\|_2&\le2z+4sa+2sMx,\\
 \sum_a\|\Delta Q_a\|_2&\le2Ca+M(2z+4sa+2sMx).
\end{aligned}                                                     \tag{R9}
\]

For example the first term in the final line is the change of action
applied to a backward field of norm at most `C`; both such fields occur.
The three velocity differences, in the order of (R8), are consequently
bounded by

\[
\begin{aligned}
 \Delta F_X&\le sM^2x+(C+2sM)a+Mz,\\
 \Delta F_A&\le(sM+C/2)x+2sa+z,\\
 \Delta F_c&\le(M/2)x+a.
\end{aligned}                                                     \tag{R10}
\]

In the middle line the rank-one difference has norm at most
`||Delta delta||2+C||Delta H^1||2`. This verifies the estimate in
operator norm and also for a HS action difference. With `M=7,C=4`, the
sum is at most `L(s)d`, where

\[
 L(s)=\max\{8,5+16s,11/2+56s\}\le8+56s,
 \qquad E:=\exp(8S+28S^2),\quad S=10.                           \tag{R11}
\]

For a mesh ending by `S`, the subsequent Euler amplification is at most
`prod_k(1+h_k L(s_k))<=exp(sum_k h_k(8+56s_k))<=E`, since the
left Riemann sum of the increasing integrand is no larger than its
integral. Thus `E=exp(2880)`.

The required ball is legitimate for forcing. First choose the unforced
mesh sufficiently fine for (R4). At that fixed mesh and sufficiently
large width, all its state bounds hold with positive slack on an event
whose probability tends to one. Finite same-array subtraction, initially
using the crude global feature bounds, shows that the forced graph stays
within the ball `M=7,C=4` for all sufficiently small fixed `|epsilon|`
on this event and on `||e||2/sqrt(n)<=2`. The permitted epsilon may depend
on the fixed mesh but not on width. All later estimates therefore use
the uniform constants (R11). The readout supremum bound survives every
forcing exactly, because every readout increment is still a difference
of two bounded tanh activations. This is a local forcing argument at
zero, not a claim that arbitrary forcing preserves the energy identity.

Insert `epsilon e` into the complete reverse answer `Q_jb`, keeping all
earlier answers and the matrix fixed and recomputing its descendants.
The only immediate state increment is `h_j sigma_b epsilon e/2` in its
clock. Therefore, for `k>j`,

\[
 \frac{\|H^{1,\epsilon}_{n,ka}-H^{1,0}_{n,ka}\|_2}{\sqrt n}
       \le\tfrac12h_j E|\epsilon|\frac{\|e_n\|_2}{\sqrt n} .     \tag{R12}
\]

Instead insert the fresh root into one complete forward answer `Z^2_jb`.
Its activation changes in RMS by at most
`|epsilon| ||e_n||2/sqrt(n)`, its delta by at most
`2s_j |epsilon| ||e_n||2/sqrt(n)`, and its reverse answer by at most
`2Ms_j |epsilon| ||e_n||2/sqrt(n)`. The three immediate state changes have
total distance at most `h_j P |epsilon| ||e_n||2/sqrt(n)`, where

\[
 P=(M+1)S+1/2=161/2.
\]

At a later node a single delta difference is at most
`z+2s(a+M x)<=K d`, with

\[
 K=\max\{1,2SM\}=140.
\]

Consequently, for `k>j`,

\[
 \frac{\|\delta^\epsilon_{n,ka}-\delta^0_{n,ka}\|_2}{\sqrt n}
           \le h_j P K E |\epsilon|\frac{\|e_n\|_2}{\sqrt n} .  \tag{R13}
\]

We now extract the named coefficients with the precise order of limits.
Fix the mesh and a sufficiently small nonzero epsilon; apply the proved
joint value/source theorem to the forced and unforced graphs and the root,
letting width tend to infinity first. In its own population the new root
enters the complete scalar expression only through replacement of the
specified named source slot by that slot plus `epsilon e`. All Gaussian
source groups are independent of this local root. Their selected
covariances and all selected coefficients may depend on epsilon, but
are deterministic, and are held fixed under coordinate differentiation.
Induction through the expression gives

\[
 \partial_e V^\epsilon=\epsilon\partial_{\rm slot}V^\epsilon,
 \qquad E[eV^\epsilon]=\epsilon E[\partial_{\rm slot}V^\epsilon].  \tag{R14}
\]

The second identity is one-dimensional Gaussian integration by parts
conditional on the other roots and source groups. Its boundary term
vanishes, since these output values and first derivatives are bounded
at a fixed graph. The unused root is independent of the unforced graph,
so `E[eV^0]=0`. Passing the finite Cauchy–Schwarz pairing inequality to
the joint W2 limit in (R12) or (R13), and using `E[e²]=1`, bounds (R14)
after division by `|epsilon|`. Only then let epsilon tend to zero. The
coefficient and derivative continuity proved in Section 2 gives exactly

\[
 |\alpha_{ka,jb}|\le h_j E/2\ (j<k),\qquad
 |\beta_{ka,jb}|\le h_j P K E\ (j<k),\qquad
 |\beta_{ka,kb}|\le2S\,1_{a=b}.                                 \tag{R15}
\]

This order does not infer a derivative transverse to an unforced singular
support from its value law. The fresh root, the finite forcing estimate,
the source-form identity and the zero-forcing continuity each have a
separate role.

###### 4. Explicit Gaussian remainders and their passage to the flow

The two source variances in (R6) are at most `1` and `C²=16`. The
forward response remainder is bounded by
`S²(E+1)`, using (R15), `|delta|<=S` and `|E[H^1 H^1]|<=1`.
For a reverse answer, all past response coefficients have total absolute
sum at most `2S P K E`. Its learned coefficients have total absolute sum
at most `S C²`, since `|E[delta delta']|<=C²`. The two current
source coefficients contribute at most `2S` in total (only the matching
current sample occurs). Since `|H^1|<=1`,

\[
 Z^2_{ka}=\xi_{ka}+B_{ka},\quad |B_{ka}|\le100(E+1),\qquad
 Q_{ka}=\zeta_{ka}+D_{ka},\quad |D_{ka}|\le B_Q,
 \quad B_Q:=225400e^{2880}+180 .                                 \tag{R16}
\]

All constants are independent of the mesh, its number of nodes and width.
Their statements for mesh scalar laws require only sufficiently fine
meshes ending by `s_infty`, as already specified.

For clarity this decomposition passes to the already constructed common
flow, not merely to marginal subsequences. Adjoin a countable refining
mesh family to the common Gaussian language. Cross-program covariance
(R6) gives
`||xi_H-xi_H'||2=||H-H'||2` and
`||zeta_delta-zeta_delta'||2=||delta-delta'||2`.
These Gaussian source assignments extend by isometry to the closures of
their input spans. The transformed Euler convergence, strong multiplier
continuity and the bounded readout give uniform-in-time L2 convergence of
`H` and `delta`; therefore the sources converge too. Subtracting them
from the convergent actual fields shows that the remainders converge in
L2. An L2 limit of variables bounded in absolute value by `B_Q` has that
same bound: take an almost surely convergent subsequence, obtained by
choosing summable squared errors and applying Markov's inequality.
The analogous statement applies to the forward remainder. Hence at every
deterministic `s<=s_infty`,

\[
 Q_a(s)=\zeta_a(s)+D_a(s),\quad |D_a(s)|\le B_Q,\quad
 \operatorname{Var}\zeta_a(s)=\|\delta_a(s)\|_2^2\le10.            \tag{R17}
\]

The final variance improves from 16 to 10 by (R3). The Gaussian process
retains all cross-time/sample covariances and is independent of the whole
first-row root. No independence of the bounded remainder and the Gaussian
part is asserted. Jointly measurable representatives follow from the L2
continuous approximations; Fubini suffices for all time integrals.

For `R>=B_Q`, (R17) yields the explicit tail estimate

\[
 \sup_{s\le s_\infty,a}
 \|Q_a(s)1_{|Q_a(s)|>R}\|_2
 \le 4(\sqrt{10}+B_Q)
          \exp\!\left(-\frac{(R-B_Q)^2}{80}\right).               \tag{R18}
\]

To verify it, put `sigma=sqrt(10)` and write a standard normal `G`.
The relevant second moment is at most
`E[(sigma |G|+B_Q)² 1_{|G|>(R-B_Q)/sigma}]`.
Use `(u+v)²<=2u²+2v²`,
`1_{|G|>a}<=exp((G²-a²)/4)`,
`E exp(G²/4)=sqrt(2)` and
`E G² exp(G²/4)=2sqrt(2)`; these two Gaussian integrals follow by
completing the square and differentiating its elementary integral.
Taking square roots gives a bound no larger than the right-hand side
of (R18). A smaller actual source variance only decreases the original
dominating second moment under the coupling `zeta=sigma_actual G`.
If `R>=10` the readout tail is zero. Thus (R18) supplies the precise
individual reference tails in C.4.1 (T6); no maximum over training data
or whole circle is needed there.

These constants record a bounded targeted improvement. The elementary
global feature estimate `||A||<=3+S²/2` in the same argument gives a
far larger exponent. Restricting to the proved reference feature endpoint,
using its raw energy path length to obtain (R4), and integrating the
time-dependent stability coefficient reduces it to 2880. The resulting
remainder is still enormous: `log B_Q<2893`. This is a mathematical
certificate, with no claim of a useful-size empirical neighborhood.

###### 5. Using actual finite reference GF rather than transformed raw GD

Let `bar theta_n(t)` be the actual finite reference GF, from the stated
Gaussian initialization, including the random readout of variance `1/n²`.
B.1 applies with sum-loss mobilities `kappa_1=kappa_2=kappa_3=1/2`,
which gives exactly the present mean-loss physical equations. Its GF
width conclusion identifies the two active projections, the action
measurements and the readout. The two orthogonal projections determine
the full first row. No infinite-width input-law limit is used here.

For each fixed physical horizon `T`, reference finite GF has a
high-probability bound on the readout supremum, action norm, and all
three raw velocity norms, uniformly on `[0,T]`. One direct source is
finite risk dissipation followed by
`||c'||infinity<=2sqrt(R_n(0))` and the bounded-activation velocity
inequalities. These imply uniform L2 time-Lipschitz bounds for the two
reference backward answers. Indeed

\[
 \dot Q_a=\dot A^*\delta_a+A^*\dot\delta_a,\qquad
 \dot\delta_a=\dot c\,\phi'(Z_a^2)
                    +c\phi''(Z_a^2)\dot Z_a^2,
\]

and
`dot Z_a²=dot A H_a¹+A[phi'(Z_a¹)dot Z_a¹]`.
Every right-hand side has bounded L2 norm using only the stated finite
state and readout-supremum bounds. The population path has the same
continuity. This step needs no Gaussian tail estimate for an input
derivative or root derivative.

Here is a detailed uniform-time tail transfer. Define
`v_R(q)=q-clip_R(q)`; it is 1-Lipschitz. For `R>0`,

\[
 |q|1_{|q|>2R}\le2|v_R(q)|\le2|q|1_{|q|>R}.                    \tag{R19}
\]

At a fixed finite time grid, B.1 gives convergence of the empirical
averages of `|v_R(Q_a)|²`, which are continuous at-most-quadratic
measurements. One may obtain them equally by truncation and the backward
quadratic observable conclusion of that theorem. The time-Lipschitz
estimate extends their RMS norms from the finite grid to every time,
since `| ||v_R(Q(t))||2-||v_R(Q(t_j))||2 |<=||Q(t)-Q(t_j)||2`.
First let width grow at the fixed grid, then refine the grid. From (R18)
and (R19), for every fixed `R>=B_Q` and every positive `epsilon`,

\[
 \Pr\left\{\sup_{t\le T,a}\tau_{2R}(Q_{n,a}(t))
   >8(\sqrt{10}+B_Q)e^{-(R-B_Q)^2/80}+\epsilon\right\}\longrightarrow0.
                                                                    \tag{R20}
\]

The top readout tail vanishes on a high-probability event once its fixed
finite-horizon supremum bound is exceeded. This supplies finite empirical
reference tails for C.4's comparison with arbitrary actual networks.

Using this actual GF reference avoids treating transformed Euler as
exact raw GD. The reference derivative is the raw vector field exactly.
In a comparison with the piecewise affine actual GD path, the sole
algorithmic discrepancy is replacing its preceding state by its current
interpolated state; the raw finite-horizon velocity bound controls that
change. The reference construction's auxiliary meshes are fixed before
width tends to infinity, and removed afterwards. Actual GD steps remain
separate. A sufficient actual-step condition may be retained as
`eta_k sqrt(n_k)->0`, as in B.1; this response component alone claims
neither a rate nor removal of that restriction.

The component concludes a quantitatively bounded Gaussian response tail
for the fixed fitted reference and its finite-GF approximation. It does
not construct a global population flow for perturbed laws, and it does
not claim that whole-circle input derivatives have Gaussian tails.



<!-- END EXCERPT -->
