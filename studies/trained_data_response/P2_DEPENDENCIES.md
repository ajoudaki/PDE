# Additional frozen established dependencies for P2

These complete units supplement P1_SECTION.md and P1_DEPENDENCIES.md.
They contain no study verdict or other-study result. Line spans refer to
the current established input with the recorded SHA-256.

<!-- BEGIN docs/README.md:1-278; SHA256 88757537ae600ebf79cf265288d6ca3034254caba236b4dcb055a21dd568c721 -->
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
| [Global nonlinear learning](global_nonlinear.md) | The same activation `1+arctan(z)/10`, every separately fixed hidden depth `L>=3`, one input and label one: global compact-time joint limit, fitting, persistent nonaffinity and hidden activity. Broad two-layer activation-transform limits allow orthogonal data, with an affine-first arbitrary-data exception and distinct GD step conditions. A separate fixed-depth C1,1 theorem is local for arbitrary fixed data and subGaussian roots; its strict-activity corollary keeps extra Gaussian and nondegeneracy hypotheses. A separate local two-hidden-tanh theorem admits every bounded-label law on the normalized input circle: quantitative training-law and replacement stability, a precisely ordered expected generalization-gap bound, simultaneous sampling/width/raw-GD consistency without relative growth restrictions, and an open nonlazy family. A separate fitted-reference transfer gives whole-circle endpoint approximation and risk at most 1/4 at T=40 for an explicit, extremely small binary-law neighborhood, with early paired hidden activity; it does not construct global perturbed-law population dynamics. At that fitted reference, a separate response theorem captures actual finite-GF data derivatives on each fixed horizon and the whole circle, with uniformly bounded population homogeneous propagation and total-variation forcing control. |
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
that feature learning outperforms frozen or linear models. Section C.4.6
separately captures actual finite-GF data derivatives at this trained reference
on each fixed horizon, with a population homogeneous propagator bounded
uniformly in time. Its total-variation forcing bound gives response control
linear in the horizon; it constructs neither nonlinear changed-law population
flows nor a finite-contamination remainder.
A global input-population theorem and a dense Gaussian joint depth/width/time
theorem remain outside the established scope; this is not an impossibility result.

Future additions should enlarge this library through proved statements with
explicit dependencies and consistent notation. Each result should say which
inputs, initialization, mobilities, observables, topology and horizons it covers;
whether learning remains nonlinear and nonlazy; and exactly what restartability
means. Numerical evidence requires its full generation commands, configurations
and seeds. No currently included theorem relies on a numerical figure or a
generated coefficient table.

<!-- END P2 EXCERPT -->

<!-- BEGIN docs/NOTATION.md:1-98; SHA256 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b -->
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

<!-- END P2 EXCERPT -->

<!-- BEGIN docs/global_nonlinear.md:2924-3440; SHA256 3f32122dea7915e25e4abc7abe9d74017d535badfa5abbe1939e84fe2b100bdf -->
### C.2. Complete weighted response and tail proof

Within this proof unit, unqualified section and equation numbers are local.

Fix a finite number \(L\ge2\) of hidden layers and a finite dataset with
weights \(\omega_a>0\), \(\sum_a\omega_a=1\). Suppose
\(|G_{ab}|\le g\). No inverse Gram matrix is used. Each activation
\(\phi^{(\ell)}\) is \(C^2\), with

\[
\max_\ell\bigl(|\phi^{(\ell)}(0)|+
\|\phi^{(\ell)\prime}\|_\infty+
\|\phi^{(\ell)\prime\prime}\|_\infty\bigr)<\infty.
\]

The first-layer root vector has uniformly subGaussian scalar marginals.
The readout root \(W_0^{(L+1)}\) is subGaussian. Roots and initial middle
matrices are independent, and the middle matrices have independent
Gaussian entries with variance \(\sigma_\ell^2/n\).
The lemma below only uses the marginal subGaussian bounds on the resulting
first preactivations and readout.

All constants are independent of the Euler mesh, the number of mesh points,
the number of inputs, the individual weights, and covariance ranks. They
can depend on fixed depth, activation bounds, \(g\), initialization bounds,
learning constants, and the preliminary RMS/residual bounds. A common
existence time across datasets does not imply a width limit for a dataset
whose size increases with width.

#### Exact recursions and hypotheses

For mesh \(\Delta\), write the population forward and backward operations
as

\[
H_{a,k}^{(\ell)}=\phi^{(\ell)}(Z_{a,k}^{(\ell)}),\qquad
P_{a,k}^{(L)}=W_k^{(L+1)},\qquad
\delta_{a,k}^{(\ell)}=
\phi^{(\ell)\prime}(Z_{a,k}^{(\ell)})P_{a,k}^{(\ell)}.
\tag{1}
\]

For \(\ell<L\), \(P_{a,k}^{(\ell)}=
(W_k^{(\ell+1)})^*\delta_{a,k}^{(\ell+1)}\). The Euler updates at the
two ends are

\[
Z_{a,k+1}^{(1)}=Z_{a,k}^{(1)}
-2\kappa_1\Delta\sum_b\omega_bG_{ab}r_{b,k}
\delta_{b,k}^{(1)},
\tag{2}
\]
\[
W_{k+1}^{(L+1)}=W_k^{(L+1)}
-2\kappa_{L+1}\Delta\sum_b\omega_b r_{b,k}H_{b,k}^{(L)}.
\tag{3}
\]

For every middle layer the update is

\[
W_{k+1}^{(\ell)}=W_k^{(\ell)}
-2\kappa_\ell\Delta\sum_b\omega_b r_{b,k}
\delta_{b,k}^{(\ell)}\otimes H_{b,k}^{(\ell-1)}.
\tag{4}
\]

For the lemma, the residuals in these recursions can be any deterministic
numbers with \(|r_{a,k}|\le R\). All deterministic residuals, contractions,
response coefficients, and Gaussian covariance laws are frozen in every
derivative below. There is no derivative through expectations.

Assume on a preliminary time interval \([0,T_{\rm ball}]\) that all source
RMS norms \(\|H_{a,k}^{(\ell)}\|_{L^2}\) and
\(\|\delta_{a,k}^{(\ell)}\|_{L^2}\) are at most \(S\), uniformly in mesh.
In particular the training-memory coefficient bound is

\[
J=2\max_\ell\kappa_\ell R S^2,
\tag{5}
\]

and all Gaussian innovations below have standard deviations at most
\(S\max_\ell\sigma_\ell\).

For each initial middle matrix introduce forward slots
\(\xi_{a,k}^{(\ell)}\) and backward slots
\(\eta_{a,k}^{(\ell)}\). Their covariances are

\[
\mathbb E[\xi_{a,k}^{(\ell)}\xi_{b,s}^{(\ell)}]
=\sigma_\ell^2\mathbb E[H_{a,k}^{(\ell-1)}H_{b,s}^{(\ell-1)}],
\quad
\mathbb E[\eta_{a,k}^{(\ell)}\eta_{b,s}^{(\ell)}]
=\sigma_\ell^2\mathbb E[\delta_{a,k}^{(\ell)}\delta_{b,s}^{(\ell)}].
\tag{6}
\]

Different matrix/orientation families are independent Gaussian families;
each family's own times and inputs are generally dependent. The
coordinate space of hidden population \(\ell\) uses its adjacent slots
\(\xi^{(\ell)}\) and \(\eta^{(\ell+1)}\), with the appropriate root at
the first/last layer. These are distinct neuron populations, not paired
finite-width coordinates.

Define unscaled expected derivatives

\[
A_{ak,bs}^{(\ell)}=
\mathbb E\frac{\partial\delta_{a,k}^{(\ell)}}
{\partial\xi_{b,s}^{(\ell)}},\qquad s\le k,
\quad
C_{ak,bs}^{(\ell)}=
\mathbb E\frac{\partial H_{a,k}^{(\ell-1)}}
{\partial\eta_{b,s}^{(\ell)}},\qquad s<k.
\tag{7}
\]

The exact local response representation is

\[
Z_{a,k}^{(\ell)}=\xi_{a,k}^{(\ell)}+
\sum_{b,s<k}F_{ak,bs}^{(\ell)}\delta_{b,s}^{(\ell)},
\tag{8}
\]
\[
P_{a,k}^{(\ell-1)}=\eta_{a,k}^{(\ell)}+
\sum_{b,s\le k}D_{ak,bs}^{(\ell)}H_{b,s}^{(\ell-1)},
\tag{9}
\]

where

\[
F_{ak,bs}^{(\ell)}=
\sigma_\ell^2 C_{ak,bs}^{(\ell)}
-2\kappa_\ell\Delta\omega_b r_{b,s}
\mathbb E[H_{b,s}^{(\ell-1)}H_{a,k}^{(\ell-1)}],
\tag{10}
\]
\[
D_{ak,bs}^{(\ell)}=
\sigma_\ell^2 A_{ak,bs}^{(\ell)}
-\mathbf1_{s<k}2\kappa_\ell\Delta\omega_b r_{b,s}
\mathbb E[\delta_{b,s}^{(\ell)}\delta_{a,k}^{(\ell)}].
\tag{11}
\]

For compact cap notation only, put
\(\widetilde A^{(\ell)}=\sigma_\ell^2 A^{(\ell)}\) and
\(\widetilde C^{(\ell)}=\sigma_\ell^2 C^{(\ell)}\).
Thus the sigma factors never enter the trained terms.

#### SubGaussian sums without maxima of Gaussian histories

For a scalar random variable define

\[
\mathcal N(U)=\sup_{p\ge2}\frac{\|U\|_{L^p}}{\sqrt p}.
\tag{12}
\]

It is a norm, and \(\mathcal N(U)\le B\) implies

\[
\mathbb E\exp\bigl(U^2/(8eB^2)\bigr)\le4/3,
\quad
\mathbb E e^{\lambda|U|}\le(4/3)e^{2e\lambda^2B^2}.
\tag{13}
\]

Indeed the \(r\)-th term in the first exponential series is at most
\((2r)^r/((8e)^rr!)\le4^{-r}\); the second inequality follows by
\(\lambda|U|\le U^2/(8eB^2)+2e\lambda^2B^2\). The case \(B=0\) is
understood as \(U=0\).

If each \(U_{b,s}\) has \(\mathcal N(U_{b,s})\le B\), Jensen applied
with weights \(\Delta\omega_b/(k\Delta)\) gives

\[
\mathbb E\exp\left(\lambda\Delta
\sum_{s<k}\sum_b\omega_b|U_{b,s}|\right)
\le(4/3)\exp(2e\lambda^2T^2B^2),\qquad k\Delta\le T.
\tag{14}
\]

This requires no independence over time or inputs. The maximum of Gaussian
coordinates or of a Gaussian history is never bounded in this argument.

#### The simultaneous field and response bounds

We prove that there exist fixed finite caps \(a_\ell,c_\ell\), constants
\(B_H,B_{P,\ell}\), and \(T_0>0\), with \(T_0\le T_{\rm ball}\), such
that at every mesh point up to \(T_0\)

\[
\sum_{b,s\le k}|\widetilde A_{ak,bs}^{(\ell)}|\le a_\ell,
\qquad
|\widetilde C_{ak,bs}^{(\ell)}|\le c_\ell\Delta\omega_b,
\tag{15}
\]
\[
\mathcal N(H_{a,k}^{(\ell)})\le B_H,
\qquad
\mathcal N(P_{a,k}^{(\ell)})\le B_{P,\ell}.
\tag{16}
\]

Set \(f_\ell=c_\ell+J\) for \(\ell\ge2\), and \(f_1=1\).
Under the response caps,

\[
|F_{ak,bs}^{(\ell)}|\le f_\ell\Delta\omega_b,
\qquad
\sum_{b,s\le k}|D_{ak,bs}^{(\ell)}|\le a_\ell+JT.
\tag{17}
\]

Choose a constant \(K\ge2\), depending only on the fixed bounds in the
lemma, large enough to dominate every root/innovation \(\mathcal N\)-norm
after applying an activation and every coefficient in (2)--(3). Fix this
\(K\) once. The triangle inequality for \(\mathcal N\), (1)--(3), and
(8)--(9) give the following bounds using only already constructed fields:

\[
\mathcal N(H_{a,k}^{(1)})\le K+KT\sup_{b,s<k}
\mathcal N(P_{b,s}^{(1)}),
\tag{18}
\]
\[
\mathcal N(H_{a,k}^{(\ell)})\le K+Kf_\ell T
\sup_{b,s<k}\mathcal N(P_{b,s}^{(\ell)}),\quad 2\le\ell\le L,
\tag{19}
\]
\[
\mathcal N(P_{a,k}^{(\ell)})\le K+(a_{\ell+1}+JT)
\sup_{b,s\le k}\mathcal N(H_{b,s}^{(\ell)}),\quad\ell<L,
\tag{20}
\]
\[
\mathcal N(W_k^{(L+1)})\le K+KT
\sup_{b,s<k}\mathcal N(H_{b,s}^{(L)}).
\tag{21}
\]

Take

\[
B_H=2K,\qquad B_{P,L}=2K,\qquad
B_{P,\ell}=4K(1+a_{\ell+1})\quad(\ell<L).
\tag{22}
\]

Once response caps have been chosen, (18)--(21) preserve these field caps
if \(JT\le1\), \(2KT\le1\), and
\(f_\ell T B_{P,\ell}\le1\) for every \(1\le\ell\le L\).
For (20), its right side is at most
\(K+2K(a_{\ell+1}+1)\le4K(1+a_{\ell+1})\).
For each finite mesh all \(\mathcal N\)-norms are finite before this
estimate: the causal magnitude recursions bound each field by a finite
deterministic linear combination of absolute roots/innovations, since
\(|\phi(z)|\le M(1+|z|)\) and \(|\delta|\le M|P|\).

#### Full forward-slot derivative rows

Fix a layer \(2\le\ell\le L\). Differentiate only with respect to its
own forward slots \(\xi^{(\ell)}\); hold the adjacent backward slots and
roots fixed. Let

\[
v_{a,k}^{(\ell)}=
\sum_{b,s\le k}\left|
\frac{\partial Z_{a,k}^{(\ell)}}{\partial\xi_{b,s}^{(\ell)}}
\right|,\qquad
V_k^{(\ell)}=\max_{a,u\le k}v_{a,u}^{(\ell)}.
\tag{23}
\]

The maximum here is a maximum of derivative row sums, not of random
backward fields. Write \(d_\ell=1+a_{\ell+1}\) if \(\ell<L\), and
\(d_L=1\). Let \(M\ge1\) dominate all activation bounds.

For \(\ell<L\), direct differentiation of (9) gives

\[
\sum_{b,s}\left|
\frac{\partial P_{a,u}^{(\ell)}}{\partial\xi_{b,s}^{(\ell)}}
\right|
\le M(a_{\ell+1}+JT)V_u^{(\ell)}.
\tag{24}
\]

For the last layer, differentiating the integrated readout update (3)
instead gives a bound \(2\kappa_{L+1}RMTV_u^{(L)}\).
The product rule in (1), with these bounds, proves for a fixed constant
\(C\) depending only on the lemma's data that

\[
\sum_{b,s}\left|
\frac{\partial\delta_{a,u}^{(\ell)}}
{\partial\xi_{b,s}^{(\ell)}}\right|
\le C\bigl(|P_{a,u}^{(\ell)}|+d_\ell\bigr)V_u^{(\ell)}.
\tag{25}
\]

The first term in (8) has derivative row sum exactly one. Its memory has
only earlier times. By the entrywise estimate (17),

\[
V_k^{(\ell)}\le1+Cf_\ell\Delta\sum_{u<k}
\left(d_\ell+\sum_b\omega_b|P_{b,u}^{(\ell)}|\right)V_u^{(\ell)}.
\tag{26}
\]

To justify the prefix maximum, the bound for every earlier time is no
larger than the displayed right side because every summand is nonnegative.
Discrete Gronwall gives

\[
V_k^{(\ell)}\le
\exp\left(Cf_\ell T d_\ell+
Cf_\ell\Delta\sum_{u<k}\sum_b\omega_b|P_{b,u}^{(\ell)}|\right).
\tag{27}
\]

Using (14), then Cauchy--Schwarz in (25), yields

\[
\sum_{b,s\le k}|\widetilde A_{ak,bs}^{(\ell)}|
\le C(B_{P,\ell}+d_\ell)
\exp\left(Cf_\ell T d_\ell+
Cf_\ell^2T^2B_{P,\ell}^2\right).
\tag{28}
\]

Here and in the remaining estimates choose one \(C\ge1\) large enough
for all displayed inequalities, and fix it before choosing response caps.
There are finitely many algebraic bound types; neither \(C\) nor \(K\)
depends on a response cap. Notice that (28) uses
\(\|P_{a,k}^{(\ell)}\|_{L^2}\|V_k^{(\ell)}\|_{L^2}\), not the
\(L^2\)-norm of a maximum over the input index or time.

#### A single backward-slot pulse

Fix \(\ell\ge2\), one input \(b\), one time \(s\), and differentiate
the local coordinate functions of layer \(\ell-1\) with respect to the
single slot \(\eta_{b,s}^{(\ell)}\). Put

\[
D_k=\max_{a,u\le k}\left|
\frac{\partial Z_{a,u}^{(\ell-1)}}
{\partial\eta_{b,s}^{(\ell)}}\right|.
\tag{29}
\]

It vanishes for \(k\le s\). Differentiating (9) and (1) gives, pointwise,

\[
\left|\frac{\partial\delta_{a,u}^{(\ell-1)}}
{\partial\eta_{b,s}^{(\ell)}}\right|
\le M\mathbf1_{a=b,u=s}
+C\bigl(|P_{a,u}^{(\ell-1)}|+d_{\ell-1}\bigr)D_u.
\tag{30}
\]

Indeed the derivative of the direct Gaussian term in (9) is precisely
\(\mathbf1_{a=b,u=s}\); the derivative of its response has magnitude
at most \(M(a_\ell+JT)D_u\). The other product-rule term is bounded by
\(M|P_{a,u}^{(\ell-1)}|D_u\).

For \(\ell=2\), insert (30) in the accumulated update (2). Its direct
pulse has magnitude at most \(2\kappa_1gRM\Delta\omega_b\).
For \(\ell\ge3\), insert it in (8) for layer \(\ell-1\); the direct
pulse has magnitude at most \(Mf_{\ell-1}\Delta\omega_b\).
Both cases therefore obey, for \(k>s\),

\[
D_k\le Cf_{\ell-1}\Delta\omega_b+
Cf_{\ell-1}\Delta\sum_{u<k}
\left(d_{\ell-1}+\sum_a\omega_a|P_{a,u}^{(\ell-1)}|\right)D_u.
\tag{31}
\]

Here \(f_1=1\). Gronwall, (14), and the bounded activation derivative
give

\[
\frac{|\widetilde C_{ak,bs}^{(\ell)}|}{\Delta\omega_b}
\le Cf_{\ell-1}
\exp\left(Cf_{\ell-1}T d_{\ell-1}+
Cf_{\ell-1}^2T^2B_{P,\ell-1}^2\right).
\tag{32}
\]

The factor \(\Delta\omega_b\) is retained from one source pulse. There
is no factor \(1/\omega_b\) in any constant and no sum of unweighted
Gaussian absolute values.

#### Cap selection and literal construction order

First choose the forward-response caps from bottom to top:

\[
c_2=4C,\qquad c_\ell=4C(c_{\ell-1}+J),\quad3\le\ell\le L.
\tag{33}
\]

These use only the \(T=0\) prefactors in (32), which do not contain any
backward cap. Next choose the backward-response caps from top to bottom:

\[
a_L=4C(2K+1),\qquad
a_\ell=4C(4K+1)(1+a_{\ell+1}),\quad 2\le\ell<L.
\tag{34}
\]

These dominate four times the \(T=0\) prefactors of (28), using (22).
All caps are now fixed finite numbers. Choose \(T_0>0\) satisfying

\[
T_0\le\min(T_{\rm ball},1),\quad JT_0\le1,\quad2KT_0\le1,
\quad f_\ell T_0 B_{P,\ell}\le1\quad(1\le\ell\le L),
\tag{35}
\]

and such that every exponent on the right sides of (28) and (32) is at
most \(\log2\) when \(T=T_0\). Each exponent tends to zero with \(T\)
after the caps have been fixed; there are finitely many of them. Thus this
choice gives a strictly positive time depending only on the stated data.
Equations (28) and (32) then improve their respective response caps by a
factor of two.

For completeness, this is an induction on the actual causal construction,
not a bootstrap that assumes all future tails:

1. At time \(k\), \(W_k^{(L+1)}\) and \(Z_{a,k}^{(1)}\) use only
   histories before \(k\). Verify their bounds from (18), (21).
2. Construct the current forward layers in order \(2,\ldots,L\).
   Before constructing layer \(\ell\), its coefficient
   \(\widetilde C^{(\ell)}\) is computed from the already constructed
   \(H^{(\ell-1)}\). Estimate (32) uses only past
   \(P^{(\ell-1)}\), whose tails and backward response caps are known,
   and the current lower-layer forward cap, which is already known.
   Equation (19) then verifies the current \(H^{(\ell)}\) bound using
   only past \(P^{(\ell)}\). This constructs the current innovations'
   source covariances too.
3. Construct the current backward layers in order \(L,\ldots,2\).
   At the top \(P^{(L)}=W^{(L+1)}\) is already bounded. At a lower
   layer \(\ell\), the current \(P^{(\ell)}\) was just constructed
   using the current higher response \(\widetilde A^{(\ell+1)}\);
   (20) verifies its cap. Hence (25)--(28) use known current
   \(P^{(\ell)}\) tails and known upper response coefficients. They
   verify the current \(\widetilde A^{(\ell)}\) cap, after which (9)
   constructs \(P^{(\ell-1)}\).
4. Apply (2)--(3) for the next step and repeat.

At \(k=0\) there is no forward response memory. The same top-down
backward construction starts from the readout root; (28) has \(V_0=1\).
Thus the induction starts without zero-readout or centered-readout
assumptions. Neither a current forward coefficient nor a current backward
coefficient needs its own unconstructed value. This proves (15)--(16).

In particular, for some fixed \(c_*,C_*>0\),

\[
\sup_\Delta\sup_{k\Delta\le T_0}\max_{a,\ell}
\mathbb E\exp\left(c_*|P_{a,k}^{(\ell)}|^2\right)\le C_*.
\tag{36}
\]

The same statement holds for every hidden activation and, by (2) and
(8), every preactivation. It implies the uniform RMS cutoff-tail bound
\(\|P\mathbf1_{|P|>R}\|_{L^2}\le C e^{-cR^2}\), after decreasing
\(c\). No bound on a maximum over neurons, dataset elements, or time was
proved or needed.

The proof also holds for arbitrary deterministic positive step lengths
\(\Delta_s\) with total time at most \(T_0\): replace every source factor
\(\Delta\omega_b\) at time \(s\) by \(\Delta_s\omega_b\), and replace
\(k\Delta\) by \(\sum_{s<k}\Delta_s\). The Jensen weights in (14) become
\(\Delta_s\omega_b/\sum_{u<k}\Delta_u\); the single-slot pulse in (31) is
exactly \(\Delta_s\omega_b\); every Gronwall estimate uses only total
time. Nothing else changes. Consequently (36) also holds for fields
recomputed at an affine Euler-state interpolation time: append one final
Euler update of length \(\theta\Delta\), \(0<\theta<1\), to the preceding
full steps, and evaluate the full forward/backward network there. The
constants are independent of \(\theta\). This bounds each interpolation
time; it is not a tail bound for a supremum of the path.

#### Consequences and boundaries

The depth extension therefore supplies the required Gaussian-tail part of
the reference comparison for smooth globally Lipschitz activations,
including when their values and the initial readout are unbounded. The
remaining proof must provide the preliminary RMS/operator ball, the
common operator realization, the oracle interpolation comparison, and its
order of limits. This proof unit does not certify those separate steps.

The exact same lemma holds when each \(2r_{a,k}\) in (2)--(4) is replaced
by any deterministic coefficient uniformly bounded on the preliminary
ball. This permits a general-loss theorem once that theorem proves the
required boundedness and feedback Lipschitz estimate for the loss
derivative.

The constants only use uniform bounds on \(\phi\)'s value at zero and
its first two derivatives. Thus this lemma is uniform under smooth
mollifications of globally Lipschitz \(C^{1,1}\) activations. Passing from
the mollified flows to the original activation still requires the
separate stability argument. ReLU has discontinuous derivative and is not
covered by this lemma or this mollification statement.

The proof is for every fixed finite depth; its constants can grow rapidly
with depth. It proves neither a depth-uniform interval nor arbitrary-depth
strict feature activity. Those are different claims.

The response rule in (6)–(11) follows from A.2 at each fixed finite C2 program. Named sources and deterministic coefficients are frozen when differentiating. This handles singular covariances and does not invoke an all-moment scalar-feedback theorem.


<!-- END P2 EXCERPT -->

<!-- BEGIN docs/global_nonlinear.md:3836-6897; SHA256 3f32122dea7915e25e4abc7abe9d74017d535badfa5abbe1939e84fe2b100bdf -->
### C.4. Training-law stability for two hidden tanh layers

Within each C.4.1–C.4.4 proof unit, unqualified section and equation numbers are
local. The typed abbreviations w, A, c denote the full first row, W^(2),
and W^(3), respectively; they do not change the canonical normalization.

Sections C.4.1–C.4.4 prove a local quantitative statement about the actual nonlinear
learning algorithm. The separate fixed-accuracy extension is in C.4.5.
Section C.4.6 identifies actual finite-GF data derivatives at that fitted
reference on each fixed horizon and bounds the population homogeneous
propagator uniformly in time. The local theorem retains the Gaussian matrix
action and its adjoint and permits every training law on the compact
observation space.

Fix Y>0. Inputs are `x(alpha)=sqrt(2)(cos(alpha),sin(alpha))` in R²;
`u=x/sqrt(2)` and `G(x,x')=u·u'`. The observation space is
`Z=sqrt(2) S^1 x [-Y,Y]`, with metric
`d_Z((x,y),(x',y'))=|x-x'|/sqrt(2)+|y-y'|`. The Wasserstein distance
`W1(mu,nu)` is the infimum over couplings of the expectation of this metric.
No restriction is imposed on atom counts, atom weights, correlations,
coincident inputs, labels conditional on input, or Gram ranks.

The finite network has equal hidden width n, no biases, and

\[
 z^1(x)=W^{(1)}x/\sqrt2,\quad h^1(x)=\tanh z^1(x),\quad
 z^2(x)=W^{(2)}h^1(x),\quad h^2(x)=\tanh z^2(x),\quad
 f_n(x)=(W^{(3)})^Th^2(x)/n.
\]

All entries and blocks are independent initially, with variances
`W^(1):1`, `W^(2):1/n`, `W^(3):1/n²`, and zero Gaussian means. All blocks
train by mean squared loss, with stored-weight mobilities `(n,1,n)`.
Raw GD updates all blocks from the same preceding state, with physical
step eta. Parameters are interpolated linearly and forward quantities are
recomputed. Initialization is independent of random training observations.

**Theorem.** There exist `T_*>0`, `C<infinity` depending only on Y and this
fixed model, with the following properties.

1. On common canonical Gaussian action spaces there is a strong autonomous
   population flow for every law mu. Its state is a full first-row field
   `w in L²(Omega_1;R²)`, a bounded action
   `A: L²(Omega_1)->L²(Omega_2)` and stored readout `c in L²(Omega_2)`.
   Its initialized action is the actual joint forward/transpose limit of
   the Gaussian middle matrix, and its reverse is the Hilbert adjoint.
   Initial state is `(g,A_0,0)` with `g~N(0,I_2)`; the finite random
   readout is retained and has vanishing normalized RMS. The integral
   equations are (T1)–(T2) and (P5) below. The state is continuously differentiable
   in the sum of full-row L², action operator norm and readout L²; it is
   unique among strong continuous integral solutions on these initialized
   spaces. At reached states it is uniquely restartable on the remaining
   local interval in the stated bounded-state class. Learned action
   increments are Hilbert–Schmidt, while the initialized action need not be.

2. For `0<q=W1(mu,nu)<=1`, the entire state and all forward hidden fields
   obey the modulus `Cq exp(C sqrt(log(e/q)))` in their stated norms,
   uniformly in time, and the forward fields uniformly in input. In
   particular

   \[
   \sup_{t\le T_*,\,x\in\sqrt2S^1}|f_\mu(t,x)-f_\nu(t,x)|
   \le Cq\exp(C\sqrt{\log(e/q)}).
   \]

   For q=0 the flows agree. For q>1 their predictions differ by at most
   2B, where B is the fixed common state bound defined in the proof. No
   logarithmic expression is evaluated beyond its stated domain.

3. Let `mu_S=m^(-1) sum_i delta_(x_i,y_i)` and `f_S=f_mu_S`. Samples
   differing in one observation satisfy

   \[
   \sup_{t\le T_*,x}|f_S(t,x)-f_{S'}(t,x)|
   \le\frac C m\exp(C\sqrt{\log(em)}).
   \]

   Define `R_mu(g)=int (g(x)-y)² dmu` and
   `Rhat_S(g)=m^(-1)sum_i(g(x_i)-y_i)²`. For iid observations from mu,

   \[
   \sup_{t\le T_*}\left|\mathbb E_S
   [R_\mu(f_S(t))-\widehat R_S(f_S(t))]\right|
   \le\frac C m\exp(C\sqrt{\log(em)}).
   \]

   The expectation and time supremum have exactly this order.

4. For every deterministic sequence of empirical laws lambda_k converging
   in W1 to mu, every `n_k->infinity`, and every `eta_k->0`, actual finite
   GD satisfies

   \[
   \sup_{t\le T_*,x}|f_{n_k,\eta_k,\lambda_k}(t,x)-f_\mu(t,x)|
     \longrightarrow0\quad\hbox{in probability}.
   \]

   In particular this holds for iid samples of any sizes m_k tending to
   infinity, independent of initialization. No relative growth restriction
   is required among n_k, m_k and eta_k. The finite empirical training loss
   and population risk both converge uniformly in time, in probability,
   to `R_mu(f_mu(t))`. This assertion also retains the paired initial/current
   activation displacement observations described next.

5. Define

   \[
   J_\ell(\mu,t)=\int\mathbb E_\ell
   |H^\ell_\mu(t,x)-H^\ell_0(x)|^2\,d\mu(x,y),\qquad\ell=1,2.
   \]

   For the reference
   `mu_0=½ delta_(sqrt(2)e1,Y/2)+½ delta_(sqrt(2)e2,Y/2)` there are a
   specified positive time t_0<=T_*, a radius r_0>0 and j_0>0, defined
   from its actual flow in Section C.4.4, such that
   `J_ell(mu,t_0)>=j_0/2` for both layers whenever
   `W1(mu,mu_0)<r_0`. For the finite networks in assertion 4 converging
   to any such mu, both corresponding training-averaged squared RMS
   displacements exceed j_0/4 with probability tending to one. The family
   is open relative to all admissible laws and contains correlated and
   nonatomic laws.

The preceding local theorem concerns finite-time training-law stability with genuine
nonlinear hidden learning. It does not assert activity for every law,
fitting, endpoint selection, a risk reduction, excess-risk control,
feature-learning superiority, global-time control, or quantitative
finite-width replacement or approximation rates.

The proof first compares changed-law vector fields using only weighted
individual reference tails. It builds the common strong flow by completing
finite training laws in the full state topology, then compares actual GD
directly to a fixed finite reference oracle. A ghost-sample exchange proves
the precise statistical assertion. Finally an actual-flow expansion and
positive adjunction identity give nonzero representation displacement,
which state continuity transfers to an open family. The dependencies are the complete [Gaussian-program proofs](special_data_limits.md#iiif-fixed-finite-gaussian-programs-common-actions-and-strong-differentiation)
in special-data III.F.1–9, the value/response extensions A.1–A.2 and weighted
response proof C.2 above, and [finite dynamics §§1–4](finite_dynamics.md)
for the exact raw equations.


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

##### 3. Continuity of the field and integration against a law

Use the common ball B=24, velocity bound V and first-exit interval (T4)–(T5).
The forward state/input comparison, including predictions, is (T8)–(T9).
These estimates hold for all laws and do not involve Gram inverses.

The backward fields are jointly continuous in \((\theta,x)\) with values
in the corresponding \(L^2\) spaces. Here is the necessary product detail.
For \(Z_j\to Z\), \(Q_j\to Q\) in \(L^2\), and bounded continuous \(b\),

\[
 b(Z_j)Q_j-b(Z)Q=b(Z_j)(Q_j-Q)+(b(Z_j)-b(Z))Q.
\]

The first term tends to zero in \(L^2\). For the second, restrict to
\(|Q|\le M\), use bounded convergence in probability there, and bound the
complement by \(2\|b\|_\infty\|Q1_{|Q|>M}\|_2\).
Let \(j\to\infty\) and then \(M\to\infty\). Apply this first to
\(\delta^2\), then use operator/adjoint continuity for \(P^1\), and then
apply it to \(\delta^1\). The same argument works when \(x_j\to x\).
Compactness of the circle shows that for \(\theta_j\to\theta\) this
continuity is uniform over \(x\): a contrary sequence has a subsequence of
inputs converging to one input, contradicting joint continuity.

Each integrand in (T2) is therefore continuous as a Banach-valued function
of \(z=(x,y)\) on the compact data space. Its range is compact and hence
separable; uniform boundedness makes it Bochner integrable. This argument
also resolves measurability despite the possibly nonseparable ambient
operator space. The middle integrand can in fact be integrated in the
Hilbert–Schmidt norm, since
\(\|v\otimes h\|_{\rm HS}=\|v\|_2\|h\|_2\) and the corresponding
rank-one difference bound is the same in that norm. Thus every learned
increment of a strong solution constructed below is Hilbert–Schmidt;
\(A_0\) itself need not be.

We shall use joint continuity

\[
 \theta_j\to\theta,\quad\mathcal W_1(\mu_j,\mu)\to0
 \quad\Longrightarrow\quad
 F_{\mu_j}(\theta_j)\to F_\mu(\theta)\text{ in }\mathcal E.
\tag{P9}
\]

To prove it, uniform continuity just established makes the change in the
integrand caused by \(\theta_j\to\theta\) uniformly small on \(\mathcal Z\).
For the remaining fixed continuous Banach-valued function \(g\), take a
coupling with mean distance \(q_j+o(1)\to0\). If
\(\omega_g(a)=\sup_{d(z,z')\le a}\|g(z)-g(z')\|\), then

\[
 \left\|\int g\,d\mu_j-\int g\,d\mu\right\|
 \le\omega_g(a)+2\|g\|_\infty(q_j+o(1))/a.
\]

First let \(j\to\infty\) and then \(a\downarrow0\). This proves (P9)
without invoking differentiability of a nonlinear map on all of \(L^2\).

##### 4. Finite reference flows and the comparison estimate

For a fixed finite probability law
\(\nu=\sum_{a=1}^m\omega_a\delta_{(x_a,y_a)}\), discard zero weights
and combine identical atoms if desired. For each rational mesh \(\Delta>0\)
construct the full-state Euler recursion

\[
 \theta^\Delta_{\nu,k+1}=\theta^\Delta_{\nu,k}
                 +\Delta F_\nu(\theta^\Delta_{\nu,k}),\qquad
 \theta^\Delta_{\nu,0}=\theta_0,
\tag{P10}
\]

and interpolate the three parameters linearly between its grid points.
At every separately fixed mesh there are finitely many calls. Expanding
the learned middle action as a finite sum of rank-one increments rewrites
these calls using only \(A_0,A_0^*\), coordinate maps and deterministic
population contractions. These are the fixed neural programs represented
in Section 2. Each contraction is computed from earlier generated nodes;
no prospective trajectory value is supplied. The full first-row update
is included literally in this recursion. Projection on \(u_b\) gives
the first equation of C.2, since \(u_a\cdot u_b=G_{ab}\). Thus its
active fields obey precisely the equations to which that lemma applies,
without requiring the active directions to span \(\mathbb R^2\).
All full-row Euler velocities have the bound (T4)–(T5).

The C.2 response bound applies here with \(L=d=2\),
\(|G_{ab}|\le1\), marginal first preactivation variance one, zero population
readout, bounded tanh and its first two derivatives, and all mobilities one.
The preliminary source RMS and residual bounds are (T4). Its complete
weighted argument supplies numbers \(\gamma_0,C_0,T_{\rm response}>0\), depending
only on these bounds and \(Y\), for which every separately fixed finite law
and all its Euler mesh states satisfy

\[
 \sup_{\Delta}\sup_{k\Delta\le T_*}\max_a
 \mathbb E_1 e^{\gamma_0|P^1_{\theta^\Delta_{\nu,k}}(x_a)|^2}\le C_0,
 \qquad \sup_{\Delta}\sup_{k\Delta\le T_*}
 \mathbb E_2 e^{\gamma_0|c^\Delta_{\nu,k}|^2}\le C_0,
\tag{P11}
\]

where
\(0<T_*\le\min(T_{\rm ball},T_{\rm response})\).
The constants do not depend on \(m\), the atom weights or Gram rank.
The C.2 proof uses weighted sums of individual subGaussian marginal bounds;
it makes no estimate of a maximum over a data set or Gaussian history.
The full-row updates change none of its active projected recursions.
C.2's hypotheses therefore remain exactly verified.

For later use, define the *integrated individual tail norm*

\[
 \tau_\nu(\bar\theta,R)=
 \|\bar c1_{|\bar c|>R}\|_2+
 \int\|P^1_{\bar\theta}(x)1_{|P^1_{\bar\theta}(x)|>R}\|_2\,d\nu(x,y).
\tag{P12}
\]

Section C.4.1 proves, at finite width and on these population spaces,

\[
 \|F_\mu(\theta)-F_\nu(\bar\theta)\|_{\mathcal E}
 \le C(1+R)\bigl(D(\theta,\bar\theta)+\mathcal W_1(\mu,\nu)\bigr)
       +C\tau_\nu(\bar\theta,R).
\tag{P13}
\]

Its proof couples \((x,y)\) with \((x',y')\), uses (T8)–(T9), cuts off only
the reference backward factors, and includes the explicit changed input
factor in \(\delta^1(x)u-\bar\delta^1(x')u'\).
In particular no Gaussian tail bound for \(\theta\) is a hypothesis.
From (P11) the Euler-grid reference tails are bounded by
\(C e^{-cR^2}\). Compare two Euler interpolants for the same finite law.
At time \(t\), each assigned velocity uses its preceding grid state.
Their grid-state distance is at most their interpolant distance plus
\(V(\Delta+\Delta')\), by (T4)–(T5). Apply (P13) at these grid states,
integrate, and use scalar Gronwall. With fixed \(a,c,C>0\),

\[
 \sup_{t\le T_*}D(\theta^\Delta_\nu(t),\theta^{\Delta'}_\nu(t))
 \le Ce^{aR}\bigl((1+R)(\Delta+\Delta')+e^{-cR^2}\bigr).
\tag{P13a}
\]

Fix \(R\), send the meshes to zero, and then send \(R\to\infty\).
The paths are Cauchy in the complete full-state path space. Their limit
\(\theta_\nu\) satisfies the strong integral equation (P5): the
preceding grid states converge uniformly to this continuous path, and
continuity of \(F_\nu\), uniformly on this convergent family of compact
path ranges, passes their integrated assigned velocities to
\(\int_0^t F_\nu(\theta_\nu(s))ds\). This also proves strong \(C^1\)
regularity. At a fixed time, the reference backward fields at preceding
grid states converge in \(L^2\) by Section 3. Taking an almost surely
convergent subsequence and applying Fatou to (P11) transfers its bounds
to the finite-law flow. Hence
\(\tau_\nu(\theta_\nu(t),R)\le C e^{-cR^2}\), uniformly in time.

Integrating (P13) for two resulting finite-law solutions from their common
initial state now gives

\[
 \sup_{t\le T_*}D(\theta_\lambda(t),\theta_\nu(t))
 \le C e^{aR}\bigl((1+R)\mathcal W_1(\lambda,\nu)+e^{-cR^2}\bigr),
 \qquad R\ge1.
\tag{P14}
\]

For completeness, set \(L_R=C(1+R)\) and
\(b_R=C(1+R)q+C e^{-cR^2}\). The integral inequality is
\(D(t)\le\int_0^t(L_RD(s)+b_R)ds\).
Iterating it, or differentiating its scalar upper comparison, gives
\(D(t)\le b_R t e^{L_Rt}\), which is (P14).

##### 5. Completion in the training law and identification of the equation

Every probability measure on the compact \(\mathcal Z\) admits finitely
supported approximations \(\nu_j\) with \(\mathcal W_1(\nu_j,\mu)\le1/j\):
take a finite \(1/j\)-net, partition measurably by the first nearest eligible
net point, and move the measure in each cell to that point. The transport
cost is at most \(1/j\); no boundary-zero assumption is needed. One may
choose the net points from a fixed countable dense set of input angles and
labels. The finite laws' weights need not be rational.

For fixed \(R\), (P14) bounds the limiting Cauchy error by
\(C e^{aR-cR^2}\). Let \(R\to\infty\). Thus \(\theta_{\nu_j}\) is
Cauchy in \(C([0,T_*];\mathcal E)\), which is complete. Let
\(\theta_\mu\) be its limit. It stays in the common ball and its forward
fields converge uniformly in time and input by (T8)–(T9).

The vector fields converge uniformly in time:

\[
 \sup_{t\le T_*}\|F_{\nu_j}(\theta_{\nu_j}(t))-
                         F_\mu(\theta_\mu(t))\|_{\mathcal E}\to0.
\tag{P15}
\]

Indeed a contrary subsequence has times \(t_j\to t\). Uniform state
convergence and continuity of the limiting curve give
\(\theta_{\nu_j}(t_j)\to\theta_\mu(t)\), so (P9) contradicts the
nonvanishing field difference. Equation (P15) passes the finite-law integral
equations to (P5). The field there is continuous in time, so the result is
a strongly \(C^1\) solution. This proves existence of the autonomous
equation, rather than only Cauchy convergence of its scalar predictions.

It remains to transfer the tails in exactly the strength needed for
uniqueness. For fixed \(t\), backward continuity in Section 3 gives

\[
 \sup_x\|P^1_{\nu_j}(t,x)-P^1_\mu(t,x)\|_2\to0,
 \qquad \|c_{\nu_j}(t)-c_\mu(t)\|_2\to0.
\tag{P16}
\]

For \(M<\infty\), the function
\(b_M(s)=\min\{e^{\gamma_0s^2},M\}\) is bounded and globally Lipschitz.
Equation (P16) therefore shows uniform-in-input convergence of its
expectations. The function
\(x\mapsto\mathbb E_1 b_M(P^1_\mu(t,x))\) is continuous, so weak
convergence of \(\nu_j\) passes its integral to \(\mu\). From (P11),

\[
 \int\mathbb E_1 b_M(P^1_\mu(t,x))\,d\mu(x,y)\le C_0.
\]

Let \(M\uparrow\infty\) by monotone convergence. The same argument for
the readout proves

\[
 \sup_{t\le T_*}\int\mathbb E_1 e^{\gamma_0|P^1_\mu(t,x)|^2}\,d\mu(x,y)
 \le C_0,
 \qquad
 \sup_{t\le T_*}\mathbb E_2 e^{\gamma_0|c_\mu(t)|^2}\le C_0.
\tag{P17}
\]

The supremum is legitimate because the preceding argument holds separately
for every \(t\) with the same constants. No common almost-sure bound on
all times or inputs is asserted. In particular (P17) is an *integrated*
input-law bound, not a pointwise continuum-wide subGaussian statement.

The elementary bound
\(s^2 1_{|s|>R}\le C e^{-\gamma_0R^2/2}e^{\gamma_0s^2}\), followed by
Cauchy–Schwarz over \(\mu\), implies

\[
 \sup_{t\le T_*}\tau_\mu(\theta_\mu(t),R)\le C e^{-cR^2}.
\tag{P18}
\]

This is precisely the reference-tail estimate used by (P13).

##### 6. Uniqueness, restart and quantitative law continuity

Let \(\widetilde\theta\) be any other strong solution of (P5) on the
same initialized spaces with initial state \(\theta_0\). Its components
are continuous in the topology (T3), its integrals have the meaning in (T2),
and no tail condition is imposed on it. The first-exit bound (T5)
keeps it in the common ball. Apply (P13) with \(\mu=\nu\), constructed
\(\theta_\mu\) as reference, and (P18). Gronwall gives

\[
 \sup_{t\le T_*}D(\widetilde\theta(t),\theta_\mu(t))
 \le C e^{aR-cR^2}\quad\hbox{for every }R\ge1.
\]

Sending \(R\to\infty\) proves equality. It also proves independence of
the chosen finite-law approximating sequence: (P14) applied across two
approximating sequences gives the same conclusion directly.

For any two arbitrary laws, (P13) and (P18) prove (P14) with
\((\lambda,\nu)\) replaced by \((\mu,\nu)\). For
\(0<q=\mathcal W_1(\mu,\nu)\le1\), choose

\[
 R=K\sqrt{\log(e/q)},\qquad K\ge1,\qquad cK^2\ge2.
\]

Then \(e^{-cR^2}\le q^2\), while
\(1+K\sqrt{\log(e/q)}\le C e^{C\sqrt{\log(e/q)}}\).
Substitution yields

\[
 \sup_{t\le T_*}D(\theta_\mu(t),\theta_\nu(t))
 \le Cq\exp\bigl(C\sqrt{\log(e/q)}\bigr).
\tag{P19}
\]

Constants depend only on \(Y\) and the frozen model and support bounds.
For \(q=0\), the laws coincide and the solutions are identical; the right
side is interpreted as its zero limit. For \(q>1\), the common ball gives
\(D\le6B\), and in particular \(D\le6Bq\). The training-law distance \(\mathcal W_1\) is at most \(2+2Y\).

Equation (T8)–(T9) now proves the requested whole-input prediction bound and,
more strongly, the same modulus for the \(L^2\) displacement between
the two forward hidden fields, uniformly over time and the circle.
For \(q>1\) the prediction difference is at most \(2B\).

The equation depends only on the current \((w,A,c)\), its coordinate
functions and the fixed training law. At a time \(s<T_*\), restrict the
constructed path to \([s,T_*]\). The preceding uniqueness argument applied
on this interval, with initial distance zero and this path as reference,
gives unique restart among strong solutions staying on the common ball.
No extra response history must be supplied. More intrinsically, close the
current full-row coordinates, readout, actions and adjoints under the same
coordinate operations; their generated \(L^2\) spaces contain their
subsequent Euler constructions and limits. To justify this last statement
without presupposing Gaussian tails for restarted Euler trajectories,
compare such an Euler trajectory directly against the existing solution
as reference. At each time its preceding grid state differs from its
interpolated state by at most \(V\Delta\). Equation (P13), with reference
tails (P18) at that time, gives the upper error
\(Ce^{aR}((1+R)\Delta+e^{-cR^2})\). Sending \(\Delta\to0\) and then
\(R\to\infty\) proves convergence to the reference continuation. The
Euler law integrals also stay in the generated spaces: their continuous
integrands are limits of finite weighted sums using a dense countable
set of input directions, and the generated spaces are closed.
Equal current generated joint laws define the isometry described in
Section 2 and intertwine the equation. Uniqueness identifies their future
laws. This is a restart claim
on the constructed local interval, not global-time well-posedness from
every arbitrary operator state.



#### C.4.3. Actual GD, simultaneous limits and statistics

##### 1. Uniform finite initialization and the common ball

Use `S0=11`, `B=24`, the velocity bound V and the first-exit interval
(T5) from Section C.4.1. The event bounding all initialized block norms
has probability tending to one and depends only on the initialization.
In particular the actual finite readout satisfies

\[
 \mathbb E\frac{\|W^{(3)}_{n,0}\|_2^2}{n}=n^{-2}.
\tag{A1}
\]

The bounds (T4)–(T5) apply to every training law and every sufficiently
small actual GD mesh. Use a fixed enlarged comparison ball for the proxy
below, reducing the common T_* if needed. This keeps every constant
independent of the actual dataset, width and step; no finite-GD energy
inequality is assumed.

##### 2. The fixed finite reference proxy

Fix a finite probability law
`nu=sum_(b=1)^J omega_b delta_(u_b,y_b)`, positive weights summing to one,
and a positive rational proof mesh Delta. These remain fixed as n tends
to infinity. Let the population Euler states for nu and Delta be denoted
`Theta^(nu,Delta)_s`. They use zero initial population readout.

Use the same initialized first and middle arrays as actual GD. Construct
the following finite deterministic-coefficient oracle: replace its scalar
residuals and within-layer contractions by the corresponding population
Euler values, expand the trained middle matrix into initialized action
plus accumulated rank-one updates, and perform the resulting finite list
of actions and coordinate operations. Denote its nodes by superscript o.
The oracle readout root is zero. Define actual finite proxy parameters by

\[
\begin{split}
 \bar W^1_{n,k}&=W^1_{n,0}
 -2\Delta\sum_{s<k,b}\omega_b r_{b,s}
               \delta^{1,o}_{b,s}u_b^T,\\
 \bar W^2_{n,k}&=W^2_{n,0}
 -\frac{2\Delta}{n}\sum_{s<k,b}\omega_b r_{b,s}
               \delta^{2,o}_{b,s}(h^{1,o}_{b,s})^T,\\
 \bar W^3_{n,k}&=W^3_{n,0}
 -2\Delta\sum_{s<k,b}\omega_b r_{b,s}h^{2,o}_{b,s}.
\end{split}\tag{A3}
\]

Interpolate these parameters linearly. In particular the proxy and actual
network have exactly the same initial arrays, including the random readout.
The small readout in (A3) is an additive parameter term, and not a change to
the actual algorithm. Its RMS tends to zero by (A1) and Markov's inequality.

At fixed `(nu,Delta)` the program has finitely many instructions. The
fixed-program theorem III.F.1–7 and global-nonlinear A.1–2 apply: tanh is
smooth with bounded first two derivatives, the gates are bounded smooth
functions times L2 fields, and the roots are Gaussian. Every same-layer
tuple and second moment of oracle nodes converges in probability. For a
proxy middle action applied to an oracle node, its discrepancy from the
prescribed oracle action is a finite sum of terms

\[
 -2\Delta\omega_b r_{b,s}\delta^{2,o}_{b,s}
 \left[\frac{(h^{1,o}_{b,s})^Th^{1,o}_{a,k}}n
             -\mathbb E_1(H^1_{b,s}H^1_{a,k})\right].
\tag{A4}
\]

Each bracket tends to zero; each multiplying node has bounded RMS in
probability. The transpose expansion has the same form with the corresponding
backward contraction. First-row oracle consistency is exact for its input
projections, since (A3) retains the whole root row and exact factors u_b.
Forward induction and (A4) give consistency of recomputed proxy forward
fields. Recomputed proxy backward fields converge by descending induction:
for any reference oracle field p, with the fixed activation phi=tanh,

\[
 \|[\phi'(z)-\phi'(\bar z)]p\|_2
 \le 2R\|z-\bar z\|_2+2\|p\mathbf1_{|p|>R}\|_2.
\tag{A5}
\]

For each fixed cutoff take n to infinity using oracle cutoff second moments;
then remove that cutoff. This controls the only unbounded multiplier. The
readout discrepancy in this step includes exactly the vanishing RMS in (A1).
Thus assigned proxy velocities differ from `F_nu(barTheta_n,k)` by o_P(1)
uniformly over the fixed finite coarse grid in D_n's block norm.

More precisely, for each fixed cutoff R, the reference tail sum satisfies

\[
 \max_k\sum_b\omega_b\sum_{\ell=1}^2
 \frac{\|\bar P^\ell_{b,k}
             \mathbf1_{|\bar P^\ell_{b,k}|>R}\|_2}{\sqrt n}
 \le C e^{-cR^2}+o_{\mathbb P}(1).
\tag{A6}
\]

Here and subsequently an inequality with o_P(1) means its positive excess
over the deterministic bound tends to zero in probability. To verify (A6)
without a discontinuous-test assertion, use
`||v 1_|v|>R|| <= 2||v-p|| + 2||p 1_|p|>R/2||`, and dominate the latter
by a continuous positive-part cutoff at R/4. The oracle cutoff moments
converge; C.2 bounds their population values by a Gaussian tail. Constants
are enlarged and c reduced once. These are individual weighted tails.

The proxy full-row and readout norms and its rank-one velocity norms are
bounded, with limiting upper bounds uniform in Delta and nu. For the middle
block use its initial norm plus the sum of the normalized rank-one norms
in (A3); their limiting total is bounded by the integral velocity bound.
For first rows and readout use the same triangle inequality and the full
root-row second moment. These observations place the proxy in a fixed
enlarged comparison ball and bound its interpolation speed independently
of Delta, with probability tending to one at fixed `(nu,Delta)`.

##### 3. Direct comparison with arbitrary growing data and every vanishing step

Let lambda_k be arbitrary deterministic finite probability laws such that
`W1(lambda_k,mu)->0`, let `n_k->infinity`, and let `eta_k->0`. The atom count
and weights of lambda_k are unrestricted. Choose the fixed reference nu above
so that `W1(mu,nu)<=delta`. At each time compare actual GD's preceding fine
state with the proxy's preceding coarse state. Their D_n distance is bounded
by their interpolant distance plus `C(eta_k+Delta)`. The transport estimate
of Section C.4.1, (A6), and the assigned-velocity error give

\[
\begin{split}
\sup_{t\le T_*}D_{n_k}(\Theta^{GD}_{k}(t),\bar\Theta^{nu,\Delta}_{n_k}(t))
\le C e^{aR}\bigl[(1+R)
 \{\eta_k+\Delta+\mathcal W_1(\lambda_k,\nu)\}
 +e^{-cR^2}+o_{\mathbb P}(1)\bigr].
\end{split}\tag{A7}
\]

This follows by integrating assigned velocities and iterating
`E(t)<=C(1+R) integral_0^t E(s)ds + b`; the exponential series bounds E by
`b exp(C(1+R)T_*)`. Initial discrepancy is zero. The o_P(1) is at fixed
`(nu,Delta,R)`. The first-exit ball in section 1 already bounds actual GD
using only initialized arrays; no Gaussian tail theorem is applied to it.
In particular no maximum over lambda_k's observations or fine GD history
occurs. The same proof would cover GF with eta_k=0.

On the comparison ball, all forward fields in RMS and scalar predictions
are uniformly Lipschitz in the full state and in u, and uniformly Lipschitz
in time along parameter interpolants of bounded speed. For instance
`||z1(u)-z1(v)||<=B|u-v|`,
`||z2(u)-z2(v)||<=B²|u-v|`, and `|f(u)-f(v)|<=B³|u-v|`.
The normalized finite versions are identical. A fixed finite input net,
then a fixed finite time net, therefore transfers fixed-program proxy
prediction convergence to

\[
 \sup_{t\le T_*,u\in S^1}
 |\bar f^{nu,\Delta}_n(t,u)-f^{nu,\Delta}(t,u)|
 \longrightarrow0\quad\hbox{in probability}.
\tag{A8}
\]

At each chosen time and passive input, append its forward evaluation to the
same fixed oracle program. Proxy recomputation follows (A4); at an interior
coarse time the parameters have the affine coefficients from (A3). This
identifies precisely the prediction of the population parameter interpolant,
rather than interpolation of predictions. Its Lipschitz bounds justify the
two nets and remove them after the fixed-program width limit.

The population comparison gives

\[
 \sup_t D(\Theta^{nu,\Delta}(t),\Theta_\mu(t))
 \le C e^{aR}\{(1+R)(\Delta+\delta)+e^{-cR^2}\}.
\tag{A9}
\]

Combining (A7)–(A9), `W1(lambda_k,nu)<=W1(lambda_k,mu)+delta`, and forward
Lipschitz continuity proves the required convergence. The order is explicit:
take k to infinity at fixed delta, fixed finite nu, fixed Delta and R;
send Delta to zero; send delta to zero through finite reference laws;
then send R to infinity. Equivalently, for a desired positive error choose
R first sufficiently large for the Gaussian remainder, then delta and Delta
small enough, and only afterwards take k large. No program whose length
grows with k is passed through a fixed-program theorem. There is no
comparison in operator norm between different spaces or different widths.

##### 4. Random observations, the two risks, and their limits

For a law rho and bounded predictor g define

\[
 R_\rho(g)=\int(g(x)-y)^2\,\rho(dx,dy),\qquad
 \widehat R_S(g)=\frac1m\sum_{i=1}^m(g(x_i)-y_i)^2.
\tag{A10}
\]

For any fixed bounded state ball these integrands have a uniform Lipschitz
constant on the joint observation space: if `|g|<=B` and g has input
Lipschitz constant L in u, the difference of squared residuals is at most
`2(B+Y)(L|u-v|+|y-z|)`. Thus for deterministic lambda_k as above, uniformly
on `[0,T_*]`, both the actual empirical training loss
`R_lambda_k(f_(n_k,eta_k,lambda_k)(t))` and its population risk under mu
converge in probability to `R_mu(f_mu(t))`. Indeed predictor uniform error
changes either risk by at most `2(B+Y)` times that error on the initial
high-probability ball; changing lambda_k to mu for the limiting predictor
costs at most `C W1(lambda_k,mu)`. Also
`R_lambda_k(f_lambda_k(t)) -> R_mu(f_mu(t))` and
`R_mu(f_lambda_k(t)) -> R_mu(f_mu(t))` uniformly in time by law stability.

For iid observations of size m from mu, `W1(mu_S,mu)->0` in probability.
Here is an elementary proof sufficient for arbitrary atomic or singular mu.
Partition the compact observation space into finitely many Borel cells of
diameter at most epsilon, and choose a representative in each nonempty cell.
Push both laws to these representatives. Each push costs at most epsilon.
If p_j are true cell masses and p_hat_j empirical masses, their discrete
W1 distance is at most `(diam Z)/2 sum_j |p_hat_j-p_j|`: match the common
mass at each representative and couple remaining masses arbitrarily.
Each empirical cell mass has variance at most 1/(4m), so this finite sum
tends to zero in probability (even in mean). Then let epsilon go to zero.
No boundary-zero partition is needed, since the observations are iid and
the same fixed Borel cells are used for their indicators.

The proof of (A7) is uniform in the actual training law on the event
`W1(mu_S,mu)<=epsilon`: its remaining random errors involve only the fixed
reference program and initialized arrays. Initialization independent of S
has the required unconditional Gaussian law for this reference and the
required joint model. A union bound with the event just proved therefore
extends (A7)–(A10) to arbitrary `n_k,m_k->infinity`, `eta_k->0`. This does
not require a uniform-in-data fixed-program theorem, or a rate for W1.

##### 5. Sample replacement and the exactly ordered expected gap

Let `rho(q)=C q exp(C sqrt(log(e/q)))` for `0<q<=1`, with constants enlarged
as in Section C.4.2, and rho(0)=0. For q>1 use the uniform predictor bound.
The observation space has diameter at most `L_Z=2+2Y`. If S and S' differ
in one observation, match their other m-1 observations and couple the last
two. This gives `W1(mu_S,mu_S')<=L_Z/m`. Law stability and the uniform
predictor bound imply, for every m>=1,

\[
 \sup_{t\le T_*,x\in\sqrt2S^1}|f_S(t,x)-f_{S'}(t,x)|
 \le \beta_m:=\frac{C}{m}\exp(C\sqrt{\log(em)}).
\tag{A11}
\]

For m>=L_Z use the unspecialized cutoff estimate with `q<=L_Z/m`.
Taking `R=K sqrt(log(em))` gives (A11) directly. Finitely many smaller m are
covered by enlarging C. Coincident data, identical replacement and q=0
are included. These are the deterministic infinite-width learning maps
`f_S=f_mu_S`; no quantitative finite-width replacement estimate follows.

For any observation z=(x,y), the squared-loss difference for two such
predictors is at most `2(B+Y) beta_m`, uniformly in z and time. Let
`S=(Z_1,...,Z_m)` be iid from mu and let `Z_i'` be an independent copy.
Write `S^(i)` for S with coordinate i replaced by `Z_i'`. All quantities
are measurable: the law-to-predictor map is continuous by law stability,
empirical-law formation is continuous in each observation, and the risks
are integrals of bounded continuous functions. With
`ell(g,z)=(g(x)-y)^2`, independence gives, at each fixed deterministic t,

\[
\begin{split}
\mathbb E_S[R_\mu(f_S(t))-\widehat R_S(f_S(t))]
 &=\frac1m\sum_i\mathbb E_{S,Z_i'}
      [\ell(f_S(t),Z_i')-\ell(f_S(t),Z_i)]\\
 &=\frac1m\sum_i\mathbb E_{S,Z_i'}
      [\ell(f_{S^{(i)}}(t),Z_i)-\ell(f_S(t),Z_i)].
\end{split}\tag{A12}
\]

The second equality exchanges the iid pair `(Z_i,Z_i')` while leaving all
other observations fixed. It uses the fact that the algorithm is the same
measurable empirical-law map for both samples. Every summand has absolute
value at most `2(B+Y) beta_m` by (A11). Taking absolute value of the
expectation and then the supremum over deterministic t yields

\[
 \sup_{t\le T_*}\left|\mathbb E_S
  [R_\mu(f_S(t))-\widehat R_S(f_S(t))]\right|
 \le\frac{C}{m}\exp(C\sqrt{\log(em)}).
\tag{A13}
\]

No expectation of an absolute gap or a time supremum has been taken.
This conclusion gives neither excess risk, useful risk reduction,
endpoint selection, nor superiority over another learning model.

##### 6. Representation observables in the joint limit

For ell=1,2 let

\[
 J_{\ell,n}(t;\lambda)=\int
 \frac{\|h^\ell_n(t,x)-h^\ell_n(0,x)\|_2^2}{n}\,\lambda(dx,dy).
\tag{A14}
\]

The integrand is bounded by 4, is uniformly Lipschitz in input on the ball,
and its change between two same-width states with the same initialization
is at most C D_n by the forward estimates and
`| ||v||²-||w||² | <= (||v||+||w||)||v-w||`.
For the fixed proxy its value at finitely many inputs and times converges
by joint oracle second moments including time zero. Input and time nets
then give uniform convergence of the whole integrand to the population
Euler integrand, just as in (A8). Coupling the input laws and using (A7)
therefore proves

\[
 \sup_{t\le T_*}|J_{\ell,n_k}(t;\lambda_k)-J_{\ell}(t;\mu)|
 \longrightarrow0\quad\hbox{in probability}.
\tag{A15}
\]

This holds for the deterministic and independent iid cases above. It
supplies the width-persistent representation displacement required by
Section C.4.4. It asserts no convergence of individual finite neurons to
population coordinates and requires no such artificial coupling.


#### C.4.4. An open family with hidden representation motion

##### 1. State and observables

Use the common fields (T1) from Section C.4.1. Write
`H_0^(ell)(x)` for their common initialized activations, and retain the
notation `W^(2)=A`, `W^(3)=c` in this proof unit.
For `ell=1,2` define the training-input averaged squared displacement and RMS
displacement

\[
 J_\ell(\mu,t)=\int_{\mathcal Z}
 \|H_\mu^{(\ell)}(t,x)-H_0^{(\ell)}(x)\|_{L^2(\Omega_\ell)}^2
 \,\mu(dx,dy),\qquad
 A_\ell(\mu,t)=\sqrt{J_\ell(\mu,t)}.                       \tag{1}
\]

The coordinate pairing at the two times is the same neuron population,
not an arbitrary coupling of the two activation marginal laws. Since tanh
is bounded by one, `0<=J_ell<=4`.

The common bounded-state interval supplies a deterministic `B>=1` such that
`||w_mu(t)||_2<=B` and `||W_mu^(2)(t)||_op<=B` for all laws and times under
consideration, including initialization. The 1-Lipschitz property of tanh
then gives, with `rho(x,x')=|x-x'|/sqrt(2)`,

\[
 \|H_\mu^{(1)}(t,x)-H_\mu^{(1)}(t,x')\|_2\le B\rho(x,x'),
 \qquad
 \|H_\mu^{(2)}(t,x)-H_\mu^{(2)}(t,x')\|_2\le B^2\rho(x,x').   \tag{2}
\]

Thus one may use `K=B^2` in both layers, for all laws, times and initialization.
These estimates use the full first-row field; controlling only projections
on a fixed training list would not justify them.

##### 2. An explicit reference law and actual-flow expansion

Fix `y_0=Y/2>0` and

\[
 x_1=\sqrt2(1,0),\qquad x_2=\sqrt2(0,1),\qquad
 \mu_0=\tfrac12\delta_{(x_1,y_0)}+
       \tfrac12\delta_{(x_2,y_0)},\qquad p=y_0/2=Y/4.          \tag{3}
\]

The Gram is `G=I_2`, and `p` is the label multiplied by its atom weight.
All constants below may depend on this reference and on `Y`.
Suppress `mu_0` in the notation. Set

\[
 h_a=\tanh g_a,\qquad q_0=\mathbb E\tanh^2 g_1>0,
 \qquad \xi_a=W_0^{(2)}h_a\quad (a=1,2).
\]

Oddness and independence of the lower Gaussian roots give
`E[h_a h_b]=q_0 1_(a=b)`. The first forward Gaussian calculation gives
independent `xi_1,xi_2~N(0,q_0)` in the second population. This calculation
can also be read directly at finite width: conditioned on the first-layer
arrays, each row output is Gaussian with covariance
`(h_a^T h_b/n)_(a,b)`, which converges to `q_0 I_2`; row averages of bounded
continuous functions concentrate conditionally, and Gaussian second moments
give the same conclusion for quadratic-growth tests. No trained matrix has
been replaced by an independent map.

With `phi=tanh` and `phi'(s)=sech^2(s)`, define the following fields,
each in its displayed layer:

\[
 S=p(\tanh\xi_1+\tanh\xi_2),\qquad U_a=S \phi'(\xi_a)
       \quad\hbox{in }L^2(\Omega_2),
\]
\[
 P_a=(W_0^{(2)})^*U_a,\qquad
 T_a=p \phi'(g_a)P_a,\qquad C_a=p \phi'(g_a)^2P_a
       \quad\hbox{in }L^2(\Omega_1),
\]
\[
 M_a=pq_0U_a,\qquad R_a=M_a+W_0^{(2)}C_a,\qquad
 E_a=\phi'(\xi_a)R_a
       \quad\hbox{in }L^2(\Omega_2).                       \tag{4}
\]

All these fields are well defined: `S,U_a` are bounded, the initial action
and its adjoint are bounded on the generated `L2` spaces, and every remaining
multiplier is bounded. The exact weighted physical equations are

\[
 \dot Z_a^{(1)}=-\sum_b G_{ab}r_b\delta_b^{(1)},\qquad
 \dot W^{(2)}=-\sum_b r_b\delta_b^{(2)}\otimes H_b^{(1)},
 \qquad \dot W^{(3)}=-\sum_b r_bH_b^{(2)},                 \tag{5}
\]

where `r_b=f_b-y_0`, `delta_b^(2)=W^(3)phi'(Z_b^(2))` and
`delta_b^(1)=phi'(Z_b^(1))(W^(2))*delta_b^(2)`. The factors in (5) are
`-2 omega_b=-1`, since this is a two-point mean loss.

The strong integral equations and continuity give

\[
 \begin{aligned}
 W^{(3)}(t)&=2tS+o_{L^2}(t),&
 \delta_a^{(2)}(t)&=2tU_a+o_{L^2}(t),\\
 \delta_a^{(1)}(t)&=2t \phi'(g_a)P_a+o_{L^2}(t),&
 Z_a^{(1)}(t)-g_a&=2t^2T_a+o_{L^2}(t^2),\\
 H_a^{(1)}(t)-h_a&=2t^2C_a+o_{L^2}(t^2),&
 W^{(2)}(t)-W_0^{(2)}
   &=2t^2\sum_b p U_b\otimes h_b+o_{\rm op}(t^2),\\
 Z_a^{(2)}(t)-\xi_a&=2t^2R_a+o_{L^2}(t^2),&
 H_a^{(2)}(t)-\tanh\xi_a&=2t^2E_a+o_{L^2}(t^2).
 \end{aligned}                                                        \tag{6}
\]

Here is the justification of every passage needed for (6). Divide the
readout integral in (5) by `t` and use `r_b(0)=-y_0`, continuity and
`H_b^(2)(0)=tanh xi_b`. The limit is `y_0 sum_b tanh xi_b=2S`.
If `V_t->V` in `L2` and `a_t->a` in probability with uniformly bounded
`a_t`, then `a_t V_t->a V` in `L2`: bound the part multiplying `V_t-V`
by the uniform multiplier bound, and split the part multiplying `V` at
`|V|<=M`, then let `M` increase. Apply this fact to `phi'(Z_a^(2)(t))`, and
then to the continuous adjoint and lower gate. It gives the two backward
limits in (6). Integrating `s` times a field converging in `L2` uses
`integral_0^t s ds=t^2/2`, which proves the lower preactivation and matrix
limits, including their factors `2p`.

For either activation difference use the identity

\[
 \frac{\tanh(z+v_t)-\tanh z}{t^2}
 =\frac{v_t}{t^2}\int_0^1 \phi'(z+s v_t)\,ds.
\]

If `v_t/t^2` converges in `L2`, its right side converges to the limit
multiplied by `phi'(z)`, by the bounded-multiplier argument. Finally expand
`W(t)H_a(t)-W_0h_a` as `(W(t)-W_0)h_a+W_0(H_a(t)-h_a)` plus the product of
the two increments; the latter is `O_L2(t^4)`. The matrix term is
`2t^2 sum_b p U_b E[h_bh_a]=2t^2 M_a`. This gives the upper two limits.
These steps derive (6) along the existing actual flow; no formal power-series
existence argument is used.

##### 3. Strict positivity of both activation displacements

Actual adjunction and independence of the upper initial Gaussian coordinates
give, for each `a`,

\[
 \langle h_a,P_a\rangle_1
 =\langle\xi_a,U_a\rangle_2
 =p\,\mathbb E[\xi_a\tanh\xi_a\,\phi'(\xi_a)]>0.             \tag{7}
\]

The other summand in `S` contributes zero, since its tanh has mean zero and
is independent of `xi_a`. In the remaining expectation the integrand is
strictly positive whenever `xi_a!=0`; the nondegenerate Gaussian gives
probability one to that event. It is integrable because it is at most
`|xi_a|`. Thus `P_a` is nonzero in `L2`. Since `p>0` and `phi'(g_a)>0` almost
surely, `C_a=p phi'(g_a)^2 P_a` is also nonzero. In particular

\[
 c_1^2=\tfrac12\sum_{a=1}^2\|C_a\|_2^2>0.               \tag{8}
\]

For the upper layer, adjunction yields the positive identity

\[
 \begin{aligned}
 p\sum_a\langle U_a,R_a\rangle_2
 &=p^2q_0\sum_a\|U_a\|_2^2
   +p\sum_a\langle P_a,C_a\rangle_1\\
 &=p^2q_0\sum_a\|U_a\|_2^2
   +p^2\sum_a\mathbb E[\phi'(g_a)^2 P_a^2]>0.                \tag{9}
 \end{aligned}
\]

Its left side is `p sum_a E[S E_a]`. Consequently the `E_a` cannot all
vanish in `L2`, and

\[
 c_2^2=\tfrac12\sum_{a=1}^2\|E_a\|_2^2>0.               \tag{10}
\]

This proves precisely the averaged upper-layer assertion needed here; an
individual upper-input activity assertion is unnecessary. Formula (9) also
retains both upper-preactivation contributions, from the moving middle
matrix and from the moving lower representation.

By (6), (8) and (10),

\[
 A_\ell(\mu_0,t)=2c_\ell t^2+o(t^2),\qquad \ell=1,2.     \tag{11}
\]

There exists `tau in (0,T_*]` such that
`A_ell(mu_0,t)>=c_ell t^2` for both layers and all `0<t<=tau`.
For a completely specified choice from the actual reference solution, let
`s_0` be the supremum of `s in (0,T_*]` such that

\[
 \left|t^{-2}A_\ell(\mu_0,t)-2c_\ell\right|\le c_\ell
 \quad(\ell=1,2;\ 0<t\le s).
\]

Equation (11) gives `s_0>0`; take `tau=s_0/2` and the fixed positive
observation time `t_0=tau/2`. No explicit numeric lower bound on `t_0` is
claimed. The constants `c_ell` are the positive Gaussian-action expressions
(8), (10), rather than fitted or numerically selected quantities.

##### 4. Transport continuity and the open family

Section C.4.2 proves this precise state conclusion: on common generated Gaussian spaces, for `q=W_1(mu,nu)<=1`,

\[
 \sup_{t\le T_*}\bigl(\|w_\mu(t)-w_\nu(t)\|_2+
 \|W_\mu^{(2)}(t)-W_\nu^{(2)}(t)\|_{\rm op}\bigr)
 \le C\,\omega(q),\qquad
 \omega(q)=q\exp(C\sqrt{\log(e/q)}),\quad\omega(0)=0.       \tag{12}
\]

It suffices equally to use any established modulus tending to zero in (12).
The forward formulas on the bounded state ball imply

\[
 \sup_{t,x,\ell}
 \|H_\mu^{(\ell)}(t,x)-H_\nu^{(\ell)}(t,x)\|_2
 \le C_H\omega(q).                                      \tag{13}
\]

Indeed the lower difference is bounded by the first-row difference; the
upper preactivation difference is at most the matrix difference times
`||H_mu^(1)||_2<=1`, plus `B` times the lower difference. Applying tanh
preserves these bounds.

To compare (1), first hold the training law fixed and change the evolved
state. Each activation displacement has norm at most two, so its squared
norm changes by at most `4C_H omega(q)`. Next hold the state `nu` fixed
and change the averaging law. Equation (2) bounds the difference of
displacement fields at `x,x'` by `2K rho(x,x')`; therefore their squared
norms differ by at most `8K rho(x,x')`. Integrating against any coupling
of `mu,nu` and taking the infimum gives

\[
 \sup_{t\le T_*}|J_\ell(\mu,t)-J_\ell(\nu,t)|
 \le 4C_H\omega(q)+8Kq,\qquad\ell=1,2.                  \tag{14}
\]

The joint transport cost dominates `rho`; labels need not be deterministic
functions of inputs for this argument. Approximate minimizers suffice, so
existence of an optimal coupling need not be invoked. The same proof is
valid for atoms, coincident inputs and singular Grams.

Set `j_0=min(c_1^2,c_2^2)t_0^4>0`. Choose a radius `r_0 in (0,1)` such
that `4C_H omega(q)+8Kq<j_0/2` for all `0<q<r_0`; such a radius exists
because the displayed expression tends to zero. Then the relative open set

\[
 \mathcal U=\{\mu\in\mathcal P(\mathcal Z):
                  \mathcal W_1(\mu,\mu_0)<r_0\}          \tag{15}
\]

satisfies, at the specified time `t_0`,

\[
 J_\ell(\mu,t_0)\ge j_0/2,
 \qquad A_\ell(\mu,t_0)\ge\sqrt{j_0/2}>0,
 \quad\mu\in\mathcal U,\quad\ell=1,2.                  \tag{16}
\]

The same construction works at any chosen reference time in `(0,tau]`,
with its own neighborhood and positive margin. For example, spreading each
reference atom over a sufficiently short input arc and a sufficiently short
label interval preserves membership in (15), so the open family contains
nonatomic laws. Moving the second reference input through a sufficiently
small nonzero angle gives correlated two-input laws in (15).

##### 5. Transfer to actual finite networks

For a finite network trained on an empirical law `lambda_n`, with its actual
random initial readout, define

\[
 J_{n,\eta,\ell}(t)=\int_{\mathcal Z}\frac1n
 \|h_{n,\eta,\lambda_n}^{(\ell)}(t,x)
       -h_{n,\lambda_n}^{(\ell)}(0,x)\|_2^2\,\lambda_n(dx,dy).
                                                               \tag{17}
\]

Section C.4.3, (A14)–(A15), proves the paired initial/current activation
observable limit, for every deterministic empirical approximation and every
independent iid sample sequence in the theorem:

\[
 \sup_{t\le T_*}|J_{n,\eta_n,\ell}(t)-J_\ell(\mu,t)|
       \longrightarrow0\quad\hbox{in probability}.       \tag{18}
\]

That proof explicitly retains both times in the fixed oracle's joint
second moments; it does not infer (18) from predictor convergence.

For iid empirical laws independent of initialization, use the corresponding
in-probability joint-limit statement with these same observations. In
particular, for every `mu in U` and either deterministic empirical
approximation or iid sampling, (16), (18) imply

\[
 \Pr\{J_{n,\eta_n,\ell}(t_0)\ge j_0/4
                 \text{ for both }\ell=1,2\}\longrightarrow1. \tag{19}
\]

Thus both hidden activation displacements stay bounded away from zero as
width increases, at a physical time and activity margin independent of
width, sample count and GD step. The finite initialization is the one in
the theorem: its readout RMS has squared expectation `1/n^2`, hence tends
to zero in probability and is covered by the initialization-perturbation
comparison. It has not been set to zero in (17).

This result asserts finite-time motion of both hidden representations on an
open family. It asserts no activity for every law, no fitting, no risk
improvement, no endpoint selection and no global-time property. In
particular a law with zero conditional label mean can have the stationary
zero-readout population solution, consistently with the stated scope.

#### C.4.5. Robust whole-circle prediction after substantial learning

This theorem extends the prediction and risk scope of the local C.4 result by comparison with one fitted reference. It does not extend the local population-flow theorem for arbitrary laws. Equation numbers are local to each of the statement and three proof units below.

##### Exact statement

Use two tanh hidden layers of common width n, input dimension two, no biases,
and the stored-weight forward map
\[
 z^1=W^1x/\sqrt2,\quad h^1=\tanh z^1,\quad
 z^2=W^2h^1,\quad h^2=\tanh z^2,\quad f_n=(W^3)^Th^2/n.
\]
Initialize all entries/blocks independently, centered Gaussian with variances
(1,1/n,1/n²). Train all blocks with mobilities (n,1,n), unhalved mean squared
loss and physical time. Raw GD updates all stored blocks from the preceding
state; interpolate raw weights linearly and recompute activations.
The actual finite initial readout is retained.

Let Z=sqrt(2)S¹ x {-1,+1}, with joint transport cost
|x-x'|/sqrt(2)+|y-y'|, and set
\[
 \nu_*=\tfrac12\delta_{(\sqrt2e_1,1)}
       +\tfrac12\delta_{(\sqrt2e_2,-1)},\qquad
 T=40,\qquad \delta=\exp\{-\exp(3000)\}.                         \tag{1}
\]

The population reference has a unique global autonomous flow on its canonical
Gaussian action spaces. Its whole-circle predictor tends to a continuous
limit f_*^infinity. To characterize this endpoint, solve the autonomous
feature equation in Section C.4.5.1 (R4)–(R5), starting from the full independent
standard Gaussian first row, the actual initialized middle Gaussian action
and its adjoint, and zero limiting readout. Stop at the unique first feature
time s_dagger at which b=<c,(H2_1-H2_2)/2>=1; evaluate that state on every
circle input. Then 0<s_dagger<=10, and
\[
 \sup_x|f_*(t,x)-f_*^\infty(x)|\le17\sqrt{10}e^{-t/5},\qquad
 R_{\nu_*}(f_*(t))\le e^{-2t/5}.                               \tag{2}
\]
The endpoint interpolates the reference labels, is odd under x->-x, and
satisfies f∞(Px)=-f∞(x) when P swaps input coordinates. Its input Lipschitz
constant in x/sqrt(2) is less than 76. This specifies the selected prediction
through the actual dynamics; it asserts no uniqueness among interpolants.

For every fixed law mu with W1(mu,nu_*)<delta, let lambda_k be any deterministic
empirical laws converging to mu in W1. Their observation counts, support
degeneracies and atom weights have no further restrictions. Take n_k->infinity
and eta_k>0 with eta_k sqrt(n_k)->0; put t_k=floor(T/eta_k)eta_k. Then
\[
 \Pr\left\{
 \sup_{x\in\sqrt2S^1}|f_{n_k,\eta_k,\lambda_k}(t_k,x)-f_*^\infty(x)|\le1/4,\
 R_\mu(f_{n_k,\eta_k,\lambda_k}(t_k))\le1/4,\
 R_{\lambda_k}(f_{n_k,\eta_k,\lambda_k}(t_k))\le1/4
 \right\}\longrightarrow1.                                   \tag{3}
\]
Probability here is over initialization. The same conclusion holds for iid
samples of any sizes m_k->infinity from the fixed mu, independent of
initialization, with probability over both samples and initialization.
There is no relative sample/width growth restriction or finite-width rate.
The displayed GD condition is sufficient; no removal is required.

At the fixed physical time t_act=1/200 define the paired, training-averaged
squared RMS displacement
\[
 J_{\ell,k}(t)=\int_Z\frac1{n_k}
 \|h^\ell_{n_k,\eta_k,\lambda_k}(t,x)
                 -h^\ell_{n_k,\lambda_k}(0,x)\|_2^2\,d\lambda_k(x,y).
                                                                    \tag{4}
\]
The two times use the same network and neuron indices, not a coupling chosen
between marginal laws. In both deterministic and iid settings,
\[
 \Pr\{J_{1,k}(t_{\rm act})\ge10^{-13},\
       J_{2,k}(t_{\rm act})\ge10^{-13}\}\longrightarrow1.        \tag{5}
\]
Thus both paired RMS norms exceed sqrt(10^-13) independently of width/sample
count. This holds jointly with (3). One may replace t_act by its preceding
GD node, by the same bounded-velocity estimate. No displacement at T is
claimed. The opposite-label reference itself has each averaged paired RMS
strictly greater than 1/2500000 at t_act.

##### Strict numerical margins and transfer

The exact rational Gaussian certificate gives m>=1/10. The reference proof
gives
\[
 17\sqrt{10}e^{-8}<.019<1/32,\qquad e^{-16}<1/1024.             \tag{6}
\]
In Section C.4.5.3 choose
\[
 B=12,\quad K=40000000,\quad d_0=10^{-18},\quad R=e^{2900},\quad
 M_Q=225400e^{2880}+180,\quad H=16(4+M_Q).                     \tag{7}
\]
The elementary bounds M_Q<e^2893, H<e^2897, K<e^18,
1+R<e^2901 and R²/4096>e^5791 give R>4M_Q+20 and R>101. Therefore
\[
 \log\{KH e^{K(1+R)-R^2/4096}\}
 <2915+e^{2919}-e^{5791}<-100,
\]
\[
 \log\{K(1+R)e^{K(1+R)}\delta\}
 <2919+e^{2919}-e^{3000}<-100.                                \tag{8}
\]
For example e>2 already separates the last exponentials by far more than
3019. Also e^-100<10^-18/4, using the single positive term 100^16/16! in
the series for e^100. These are the two strict bounds in Section C.4.5.3 (15).
The same estimates give
\[
 L_{\rm risk}\delta<1/256,\quad 8B^2\delta<10^{-18},
 \qquad L_{\rm risk}=44928.                                  \tag{9}
\]

Compare actual GD to actual finite GF on nu_* with the same initialized
arrays. Since limsup W1(lambda_k,nu_*)<delta, the stopped comparison gives
\[
 \left(\sup_{t\le40}D_{n_k}(\theta_{GD,k}(t),\bar\theta_{n_k}(t))
                                       -d_0/2\right)_+
 \longrightarrow0\quad\hbox{in probability}.                 \tag{10}
\]
Its complete proof, including the finite actual-state bounds, initial
readout, reference tails, auxiliary-mesh order and stopping argument, is
Section C.4.5.3. The reference is raw GF, so its raw-field defect is zero.
Transformed Euler is used only as an auxiliary width-identification tool.

Whole-circle reference convergence and the full-state estimates imply
\[
 \left(\sup_x|f_k(T,x)-f_*^\infty(x)|-1/16\right)_+
 \longrightarrow0\quad\hbox{in probability},                 \tag{11}
\]
because the deterministic bound is .019+B²d0<1/16. The circle extension uses
the full first row and uniform input Lipschitz bounds. Replacing T by t_k
costs at most a fixed state-speed/prediction constant times eta_k.
The finite predictor is bounded by 12 and Lipschitz in normalized input
with constant 1728 on the comparison event. Its squared-loss integrand has
joint Lipschitz constant Lrisk. At the reference atoms f∞ equals the label.
Thus (9),(11) give
\[
 (R_\mu(f_k(t_k))-1/128)_+\longrightarrow0,\quad
 (R_{\lambda_k}(f_k(t_k))-1/128)_+\longrightarrow0
                      \quad\hbox{in probability}.            \tag{12}
\]
The two deterministic contributions are (1/16)² and Lrisk delta<1/256;
for the empirical risk use W1(lambda_k,nu_*)<=delta+o(1). These strict
bounds prove (3), not just convergence to its thresholds. Both limiting
initial binary-label risks are one, because the initial predictor is
uniformly bounded by the vanishing readout RMS.

For activity, changing the evolved state with initialization fixed changes
the paired squared-displacement integrand by at most 4(B+1)D_n. Changing
its input changes it by at most 8B²|u-v|. These follow from displacement
RMS<=2 and the forward input/state bounds in Section C.4.5.3. Coupling lambda_k
to nu_*, retaining the separate paired-observable reference convergence,
and using its strict RMS margin gives
\[
 J_{\ell,k}(t_{\rm act})\ge(1/2500000)^2-2(B+1)d_0-8B^2\delta
                                            -o_{\mathbb P}(1).       \tag{13}
\]
The deterministic right side exceeds 1.59*10^-13, proving (5) with slack.
The opposite-label activity computation is proved anew in Section C.4.5.1;
C.4's equal-label example is not substituted for it.

For iid samples, compact Borel partitions and the variance bound for each
empirical cell mass prove W1(lambda_k,mu)->0 in probability, as detailed
in Section C.4.5.3. Its other random events involve only the fixed reference
and initialization. Union bounds give (3),(5) in joint probability.
Each claim is for every fixed mu and sequence. No uniform failure probability
over laws, almost-sure joint limit, global population flow for mu or endpoint
for mu is asserted.

##### Geometric meaning, scale and limitations

An admitted nonorthogonal law moves the second reference input by the angle
a=delta/2, retaining its label and the first atom. Its cost is at most
a/2=delta/4; the off-diagonal input Gram is -sin(a), which is nonzero.

For an admitted nonatomic law replace each input atom by uniform arc length
on the arc of angular radius a=delta/4 around it, retaining its associated
label, and then flip each binary label independently with probability
p=delta/8. The coupling costs at most a+2p=delta/2<delta. More generally
a+2p<delta suffices; arbitrary extra contamination of mass rho costs at most
4rho. Thus no orthogonality, two-atom, Gram-inverse or weight-lower-bound
condition is imposed on perturbed laws.

The explicit radius is mathematically positive, but extremely small:
\[
 \log_{10}(1/\delta)=e^{3000}/\log 10,\qquad
 \log_{10}\log_{10}(1/\delta)
 =3000/\log 10-\log_{10}(\log10)\approx1302.52.
\]
This is far below a practically useful neighborhood. The dominant loss is
the fresh-root stability exponential followed by a cutoff comparison.
A bounded targeted improvement used the reference energy path length and
integrated a time-dependent coefficient, reducing the response exponent
to 2880. Its conservatism is likely substantial; its sharpness is not
assessed by this proof. No training experiment or parameter sweep was run.

The theorem establishes whole-circle robustness after substantial risk
reduction for an open family with nonlinear moving hidden features. It
does not show that feature motion causes that reduction, superiority to
linear or frozen-feature learning, or useful risk on a uniform-circle
teacher distribution. It gives no arbitrary-accuracy guarantee for one
fixed perturbed law. A radius shrinking with accuracy would not give that
stronger conclusion.



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


##### C.4.5.3. Transfer to actual raw GD

###### 1. Exact fields and comparison constants

Put `u=x/sqrt(2)` and `phi=tanh`. On the canonical two population spaces use
the full state `theta=(w,A,c)`, where `w in L2(Omega_1;R2)`,
`A:L2(Omega_1)->L2(Omega_2)` is bounded and `c in L2(Omega_2)`. Set

\[
 Z^1(u)=w\cdot u,\quad H^1(u)=\phi(Z^1(u)),\quad
 Z^2(u)=AH^1(u),\quad H^2(u)=\phi(Z^2(u)),\quad
 f(u)=\langle c,H^2(u)\rangle,
\]
\[
 r(u,y)=f(u)-y,\quad \delta^2(u)=c\phi'(Z^2(u)),\quad
 Q(u)=A^*\delta^2(u),\quad \delta^1(u)=\phi'(Z^1(u))Q(u).
\]

The unhalved mean-loss field, with exactly the prescribed mobilities, is

\[
 F_\lambda(\theta)=-2\left(
 \int r\delta^1u\,d\lambda,
 \int r\delta^2\otimes H^1\,d\lambda,
 \int rH^2\,d\lambda\right).                                      \tag{1}
\]

The rank-one action is `(v tensor h)g=v E_1[hg]`. The distance is

\[
 D(\theta,\bar\theta)=\|w-\bar w\|_{L^2(\Omega_1;\mathbb R^2)}
 +\|A-\bar A\|_{op}+\|c-\bar c\|_{L^2(\Omega_2)}.                 \tag{2}
\]

For two networks of the same width replace the three norms respectively by
`||W1-W1bar||F/sqrt(n)`, `||W2-W2bar||op`, and
`||W3-W3bar||2/sqrt(n)`; call this `D_n`. The finite rank is `v h^T/n`.
There is no comparison in operator norm across widths or carriers.

Here is an explicit version of the maintained C.4 transport lemma. Suppose
each individual state norm in (2) is at most `B=12`; the norms in this premise
are of each state component, not of a difference. Define
`tau_R(v)=||v 1_(|v|>R)||2` and

\[
 \mathcal T_R(\bar\theta)
 =\tau_R(\bar c)+\tfrac12\sum_{a=1}^2\tau_R(\bar Q(e_a)).
\]

For any probability law lambda on the binary observation space, any `R>=1`,
and the fixed reference nu_* of the question,

\[
 \|F_\lambda(\theta)-F_{\nu_*}(\bar\theta)\|_{(2)}
 \le 10^6\{(1+R)[D(\theta,\bar\theta)+W_1(\lambda,\nu_*)]
                         +\mathcal T_R(\bar\theta)\}.             \tag{3}
\]

This holds also in the normalized finite norms, with the same constant.
Here are arithmetic details making the constant checkable. For a coupling
pair `(u,y),(v,z)`, set `h=|u-v|`, `d=D`, and `l=|y-z|`. Then

\[
 \|Z^1-\bar Z^1\|_2\le B(d+h),\quad
 \|Z^2-\bar Z^2\|_2\le B(B+1)(d+h),\quad
 |r-\bar r|\le B^3(d+h)+l.                                      \tag{4}
\]

The bounds use `|phi|,|phi'|<=1` and `Lip(phi')<=2`. For any fixed reference
field v, splitting at `|v|=R` gives
`||[phi'(z)-phi'(zbar)]v||2 <=2R||z-zbar||2+2tau_R(v)`.
Writing `a=B(B+1)=156`, successive subtraction therefore gives

\[
 \|\delta^2-\bar\delta^2\|_2
 \le313(1+R)(d+h)+2\tau_R(\bar c),
\]
\[
 \|\delta^1-\bar\delta^1\|_2
 \le3792(1+R)(d+h)+24\tau_R(\bar c)+2\tau_R(\bar Q(v)).           \tag{5}
\]

For the lower, middle and readout integrands, respectively, the coefficients
of `(1+R)(d+h+l)` before the overall factor 2 are at most

\[
 B^2(B^3+1)+(B+1)3792+(B+1)B^2,
\]
\[
 B(B^3+1)+(B+1)313+(B+1)B^2,
 \qquad B^3+1+(B+1)a.
\]

Twice their sum is less than `10^6`. The total reference-tail coefficient
is at most `4(B+1)(B+1)=676`, also below `10^6`. These decompositions include
the explicit changed input vector in `r delta^1 u`. Integrating the estimates
against a coupling and taking the infimum of its cost proves (3).
No maximum over actual observations, positive Gram eigenvalue or atom-weight
bound occurs. The full Gaussian row enters (4) only through its L2 norm.

For same-input prediction and activation comparisons on this ball,

\[
 \sup_u|f_\theta(u)-f_{\bar\theta}(u)|\le2B^2D,
 \quad\sup_u\|H^\ell_\theta(u)-H^\ell_{\bar\theta}(u)\|_2
 \le(B+1)D\quad(\ell=1,2).                                    \tag{6}
\]

Every such predictor has `|f|<=B` and Lipschitz constant at most `B^3` in u.
Thus its binary squared-loss integrand has joint Lipschitz constant

\[
 L_{risk}=2(B+1)B^3=44928,\qquad
 |R_\lambda(f)-R_\rho(f)|\le L_{risk}W_1(\lambda,\rho).           \tag{7}
\]

###### 2. Actual finite reference GF and uniform observable passage

Let `bar theta_n(t)` be the actual finite gradient flow on nu_*, started from
exactly the same three initialized arrays as the network to be compared.
In particular its finite readout is not zero. Finite dynamics §§1–4 gives
global existence and the exact raw-metric energy identity. With probability
tending to one, initialization satisfies

\[
 \|W^1_0\|_F/\sqrt n\le2,\quad\|W^2_0\|_{op}\le3,\quad
 \|W^3_0\|_2/\sqrt n\le1/4,\quad\|W^3_0\|_\infty\le1.
                                                                    \tag{8}
\]

The first/readout assertions follow from Gaussian second moments and the
Gaussian union bound; the sharp matrix bound is proved in global-nonlinear
A.3. Initial loss is at most `25/16`. Up to `T=40`, every block displacement
in its raw metric is at most `sqrt(40*25/16)<8`, by energy and Cauchy–Schwarz.
Consequently each reference component norm is strictly below 11. Its readout
coordinate bound is at most `1+2T sqrt(25/16)=101`, because the mean absolute
residual is bounded by the square root of the nonincreasing loss. These
bounds apply to the actual finite flow, including its nonzero readout.

For this particular reference, B.1 applies with two orthogonal inputs,
sigma_1=sigma_2=1, beta=1, both activations tanh and kappa_i=1/2 to convert
its sum loss into the present mean loss. Its construction uses the same
fixed first Gaussian pair and initialized action with its actual adjoint.
Its unique population flow is the one in Section C.4.5.1. The two active lower
projections determine the full first row since they are precisely its two
columns. Thus all passive circle inputs are evaluated using the same trained
row, without creating extra training observations.

We spell out the additional uniform observations needed here. At fixed
auxiliary transformed mesh Delta, append finitely many passive forward
evaluations and the active queries `Q_a=A* [c phi'(Z2_a)]` to B.1's oracle
program. Its value theorem A.1 and complete III.F fixed-program construction
give the joint node laws and second moments. The readout product can be
clipped beyond its proven coordinate bound, so it is globally Lipschitz in
its varying arguments. The transformed same-root comparison bounds the
finite-flow/mesh error uniformly in width; learned action differences use
operator norm. Its forward estimates also control the passive directions.
The Q difference is bounded in L2 by

\[
 \|A-\widetilde A\|_{op}\|c\|_2+
 \|\widetilde A\|_{op}
 (\|c-\widetilde c\|_2+2\|\widetilde c\|_\infty
                                  \|Z^2-\widetilde Z^2\|_2).
                                                                    \tag{9}
\]

First take width to infinity with Delta fixed, then remove Delta. This proves
the fixed-time joint second-moment limits for Q, the forward fields and paired
initial/current activations. It does not apply a finite-program theorem to
the growing actual GD transcript.

The passage is uniform in physical time. On (8), the reference has uniformly
bounded raw velocities on `[0,40]`, by (1) and the preceding bounds. Strong
curve differentiation gives `dot Z2=dot A H1+A phi'(Z1)dot Z1`, and
`dot delta2=dot c phi'(Z2)+c phi''(Z2)dot Z2`. Their L2 norms are uniformly
bounded using `|c|<=101`. Differentiating `Q=A*delta2` then bounds its L2
time-Lipschitz constant independently of width. The population proof is
identical. Norms of positive-part cutoffs of Q inherit this Lipschitz constant.
A fixed finite time grid followed by its refinement therefore extends every
needed cutoff second-moment comparison uniformly in time. Forward evaluations
are Lipschitz in input with constants bounded by the state norms. A fixed
finite input net, after the time net, proves

\[
 \sup_{t\le40,u\in S^1}|\bar f_n(t,u)-f_*(t,u)|\longrightarrow0
                         \quad\text{in probability}.              \tag{10}
\]

The same argument for the bounded squared displacement integrand, retaining
the same neuron at time zero and current time in the fixed programs, gives

\[
 \sup_{t\le40,u}\left|\frac1n
 \|\bar h^\ell_n(t,u)-h^\ell_n(0,u)\|_2^2
 -\mathbb E_\ell|H^\ell_*(t,u)-H^\ell_0(u)|^2\right|
 \longrightarrow0\quad\text{in probability}.                       \tag{11}
\]

Here no individual finite neuron is coupled with an invented population neuron.

The response proof supplies, on the reference feature segment through its
interpolating endpoint, `Q_a=G_a+E_a`, with `G_a` centered Gaussian of variance
at most 16, `|E_a|<=M_Q`, and

\[
 M_Q=225400e^{2880}+180<e^{2893}.                                  \tag{12}
\]

Also `|c_*|<=10`. For `R>=4M_Q+20`, elementary Gaussian integration gives

\[
 \sup_{t\le40}\mathcal T_R(\bar\theta_n(t))
 \le H e^{-R^2/4096}+o_{\mathbb P}(1),\qquad H=16(4+M_Q).          \tag{13}
\]

Every `o_P(1)` here is at fixed R and on one fixed reference. To check the
constants, if `G` has variance at most `sigma²`, then
`E exp(G²/(4sigma²))<=sqrt(2)`. Splitting `Q=G+E` and using
`x²<=8sigma² exp(x²/(8sigma²))` bounds
`tau_r(Q)<=8(sigma+M_Q)exp(-r²/(64sigma²))` for `r>=2M_Q`.
At finite width `tau_R(Q_n)<=2||(|Q_n|-R/2)_+||2` and this latter norm
converges uniformly in time to its population counterpart by (9) and the
time-grid argument. Take sigma=4 and r=R/2. The readout has no tail at
R>101 at finite width on (8). Our final R is much larger. This proves (13).

###### 3. Raw GD comparison, stopping, and limit order

Actual finite raw GD is exactly
`theta_(j+1)=theta_j+eta F_lambda(theta_j)` for (1). It does not update a
transformed clock. For completeness its states have a width-independent
bound on every fixed horizon, for any probability law. If c_j is its readout
RMS, then `1+c_(j+1)<=(1+2eta)(1+c_j)`. Hence `c_j<=2e^(2(T+1))` for
initial c_0<=1 and nodes through T+eta, eta<=1. Writing this bound as C_T,
the middle norm is at most `3+2(T+1)(C_T+1)C_T=:A_T`, and the full-row RMS
is at most `2+2(T+1)(C_T+1)A_T C_T`. These estimates follow directly from
successive raw increments, not a GD energy inequality.

Sharper constants in the comparison come from stopping at the first time
`D_n(theta_GD(t),bar theta_n(t))=1`. Before that time both states have
individual norms at most B=12. The GD preceding-node state also lies there:
its preceding time has not exited. Both interpolant speeds on this prefix
are bounded by

\[
 V=2(B+1)(B^2+B+1)=4082.
\]

At time t the GD preceding state differs from its interpolant by at most
V eta. Apply (3) against the actual reference GF at t, integrate the velocity
difference, and use (13). Initial distance is exactly zero. With
`K=40*10^6=40000000` and `q=W1(lambda,nu_*)`, Gronwall gives, on the stopped
interval,

\[
 \sup_{t\le40}D_n(\theta_{GD}(t),\bar\theta_n(t))
 \le K e^{K(1+R)}\{(1+R)(q+V\eta)
                           +H e^{-R^2/4096}+o_{\mathbb P}(1)\}.   \tag{14}
\]

The supremum in (14) is first understood up to the stopping time. If its
right side is strictly less than one, continuity excludes that stopping
time, and the estimate holds through 40. All probabilities in (14) come from
initialization and the one fixed reference; the bound otherwise applies to
every actual law with the displayed q. A stochastic actual law is therefore
handled on its event controlling q, without any law-dependent width theorem.

The limit order is: fix T, the reference, the cutoff R and an auxiliary
accuracy; establish the reference GF observations by fixed transformed mesh,
width limit, then mesh removal; use those resulting reference statements in
(14) and send the actual width to infinity and its step to zero. Auxiliary
proof meshes never become actual GD steps. No transformed Euler increment is
claimed to equal a raw GD increment; (14) compares actual raw GD directly to
actual raw GF. The sufficient condition `eta_k sqrt(n_k)->0` requested in
the primary theorem is permissible. In fact this particular final comparison
uses only `eta_k->0`, because B.1 is used for the reference GF, not for an
actual reference GD sequence.

###### 4. Remaining assembly interface

The numerical error tolerance, the exact certified radius, activity time and
positive activity margin are fixed in the theorem above using Section C.4.5.1 and
Section C.4.5.2. For any tolerance d0<1, it suffices to choose R and delta with

\[
 K H\exp(K(1+R)-R^2/4096)\le d_0/4,\qquad
 K(1+R)\exp(K(1+R))\delta\le d_0/4.                             \tag{15}
\]

Then for any deterministic empirical sequence lambda_k with
`W1(lambda_k,mu)->0`, `W1(mu,nu_*)<delta`, the positive excess of the full
time-uniform same-width state distance over d0/2 tends to zero in probability.
There is no assertion that perturbed trajectories converge to a unique global
population trajectory. Equations (6), (7), (10), (11) transfer the observable
conclusions without that assertion.

For iid empirical laws of sizes m_k->infinity, independent of initialization,
`W1(lambda_k,mu)->0` in probability. A direct proof partitions the compact
observation space into finitely many Borel cells of diameter epsilon, moves
each law to the same representatives at cost at most epsilon, and bounds the
remaining transport by half the diameter (at most 4) times the sum of cell
mass discrepancies. Each empirical cell mass has variance at most 1/(4m_k).
First send m_k to infinity at fixed partition, then epsilon to zero. A union
bound with the initialization/reference events proves the same joint limits
for arbitrary width/sample growth rates. This gives probability tending to
one for every fixed mu and sequence. No numerical finite-width rate, almost
sure joint convergence or uniform failure probability over laws is asserted.


<!-- END P2 EXCERPT -->
