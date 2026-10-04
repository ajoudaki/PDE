# Input geometry route: finite autonomous compression without a rank assumption

Scope: prompt-only independent theoretical route. No repository research, external papers, or experiments were used. The arguments below are internally derived, not independently reviewed or promoted results.

## Main result and what it does not say

For a fixed finite network, finite training horizon, compact input domain, and bounded second label moment, one can replace any empirical or population data measure by a finite list of input cells, their masses, and their label totals. Training the original nonlinear network on these statistics gives a finite autonomous ODE whose trajectory approximates the original gradient flow to arbitrary prescribed accuracy. The number of cells depends on the input covering number and network regularity, not on the number of data points. All trainable hidden features continue to train, and the realized Gaussian initialization is retained exactly.

This establishes an existence and constructive approximation statement independent of data count `m`. It does not establish useful computational efficiency, uniformity in width `n`, a fixed-size representation for every accuracy, an all-time theorem, or compression of arbitrary raw label fields. It also does not by itself construct a width-independent population-neuron limit. Those are distinct questions.

The natural structural quantity here is the metric entropy of the input domain as seen by the functions entering the gradient. Matrix rank can be large even when this metric entropy permits accurate discretization.

## 1. A finite autonomous partition theorem

Let `(X,d)` be a compact metric input space, and let `P` be a probability measure on `X × R`, with

\[
\mathbb E_P y^2\le Y_2<\infty,\qquad Y_1=\sqrt{Y_2}.
\]

An empirical dataset is included by taking `P=m^{-1} Σ_a δ_(x_a,y_a)`. Nothing below requires its support to be finite. Let `θ ∈ R^p` collect every trainable network parameter, including all trainable hidden weights; `p` may depend on width and depth. The fixed architecture defines a scalar output `f_θ(x)`. Assume:

1. `f` is twice continuously differentiable in `θ`, jointly continuous in `(θ,x)`, with jointly continuous first and second parameter derivatives.
2. On each bounded parameter ball, both `f_θ` and `∇_θ f_θ` have a common input modulus of continuity. The quantitative version below assumes common Hölder exponent `α ∈ (0,1]`.
3. The mobility `D` is a constant symmetric positive-definite `p × p` matrix; write `d_* = ||D||`.

The canonical squared-loss flow is

\[
L_P(\theta)=\mathbb E_P(f_\theta(x)-y)^2,
\qquad
\dot\theta=F_P(\theta)
=-2D\,\mathbb E_P[(f_\theta(x)-y)\nabla_\theta f_\theta(x)].
\tag{1}
\]

Fix the actual initialization `θ₀`, including the actual sampled Gaussian matrices; no averaging or resampling occurs. Fix `T < ∞`. Put

\[
B=\sup_{x\in X}|f_{\theta_0}(x)|+\sqrt{Y_2},
\qquad R=\sqrt{Td_*}\,B+1,
\qquad \Theta=\{\theta:\|\theta-\theta_0\|\le R\}.
\tag{2}
\]

On this explicitly specified ball choose finite constants

\[
\begin{aligned}
|f_\theta(x)|&\le M_0,&
\|\nabla_\theta f_\theta(x)\|&\le M_1,&
\|\nabla_\theta^2 f_\theta(x)\|&\le M_2,\\
|f_\theta(x)-f_\theta(x')|&\le H_0d(x,x')^\alpha,&
\|\nabla_\theta f_\theta(x)-\nabla_\theta f_\theta(x')\|
&\le H_1d(x,x')^\alpha.
\end{aligned}
\tag{3}
\]

These constants depend on the architecture, actual initialization, input geometry, `Y₂`, and `T`, but not on `m`. Smooth activation networks on a compact Euclidean input domain satisfy these assumptions. Bounds can be poor at large width/depth or large parameter radius; smoothness alone does not promise favorable constants.

Choose input nodes `ξ₁,…,ξ_N ∈ X` and a measurable partition `A₁,…,A_N` with

\[
x\in A_j\ \Longrightarrow\ d(x,\xi_j)\le h.
\]

For example, a finite `h`-cover gives such a partition by assigning each point to its first covering ball. Retain only

\[
p_j=P(x\in A_j),\qquad
b_j=\mathbb E_P[y\mathbf 1_{x\in A_j}].
\tag{4}
\]

The autonomous compressed evolution is

\[
\dot\theta_h
=-2D\sum_{j=1}^N
\bigl(p_j f_{\theta_h}(\xi_j)-b_j\bigr)
\nabla_\theta f_{\theta_h}(\xi_j),
\qquad \theta_h(0)=\theta_0.
\tag{5}
\]

Terms with `p_j=0` have `b_j=0` and can be omitted. Equivalently, this trains the same network on weighted examples `(ξ_j,b_j/p_j)`; the labels can be arbitrary and need not vary smoothly with `x`. Equation (5) is a finite autonomous, restartable program. Its coefficients are obtained from the source data before training and contain no future trajectory values.

Define

\[
\delta_h=2d_*h^\alpha\bigl[M_1H_0+(M_0+Y_1)H_1\bigr],
\qquad
\Lambda=2d_*\bigl[M_1^2+(M_0+Y_1)M_2\bigr],
\]

and `Q_T(Λ)=(e^{ΛT}-1)/Λ`, with `Q_T(0)=T`. Then

\[
\sup_{0\le t\le T}\|\theta(t)-\theta_h(t)\|
\le\delta_h Q_T(\Lambda),
\tag{6}
\]

and

\[
\sup_{0\le t\le T}\sup_{x\in X}
|f_{\theta(t)}(x)-f_{\theta_h(t)}(x)|
\le M_1\delta_h Q_T(\Lambda).
\tag{7}
\]

Thus choosing `h` so that the right side of (6), or (7), is at most a prescribed `ε` gives data-count-independent complexity `N ≤ N_X(h)`, where `N_X(h)` is the input covering number.

### Proof, including the parameter-region and source-error steps

Both vector fields are locally Lipschitz in parameters. Differentiating under the expectation is justified on compact parameter balls by the derivative bounds and `E|y| ≤ Y₁`. Along (1),

\[
\frac{d}{dt}L_P(\theta(t))
=-\dot\theta(t)^TD^{-1}\dot\theta(t)
\le-\frac{\|\dot\theta(t)\|^2}{d_*}.
\]

Since the loss is nonnegative and `L_P(θ₀) ≤ B²`, integration and Cauchy–Schwarz give

\[
\|\theta(t)-\theta_0\|
\le \int_0^t\|\dot\theta(s)\|ds
\le\sqrt{td_*L_P(\theta_0)}
\le\sqrt{Td_*}B.
\tag{8}
\]

The same argument applies to (5): define `q(x)=ξ_j` on `A_j` and use the nonnegative loss `E_P(f_θ(q(x))-y)²`, whose gradient is exactly (5) and whose initial value is at most `B²`. Both trajectories therefore stay strictly inside `Θ`. The bound also prevents finite-time escape; local existence extends to the required finite horizon. This parameter-region estimate uses initial data and loss, rather than an unknown future parameter trajectory.

Write `J_θ=∇_θ f_θ`. For every `θ ∈ Θ`,

\[
\begin{aligned}
\|f_\theta(x)J_\theta(x)-f_\theta(q(x))J_\theta(q(x))\|
&\le(M_1H_0+M_0H_1)h^\alpha,\\
\mathbb E_P\bigl[|y|\|J_\theta(x)-J_\theta(q(x))\|\bigr]
&\le Y_1H_1h^\alpha.
\end{aligned}
\]

These give `sup_Θ ||F_P-F_h|| ≤ δ_h`. This is the small source error; it does not follow merely from stability.

For either data measure, the derivative of `(f-y)J` with respect to `θ` is

\[
JJ^T+(f-y)\nabla_\theta^2 f.
\]

Its expected norm is at most `M₁²+(M₀+Y₁)M₂`. The convexity of `Θ` then gives parameter Lipschitz constant `Λ` for the vector fields. If `e(t)=||θ(t)-θ_h(t)||`, the integral equations imply

\[
e(t)\le\int_0^t(\Lambda e(s)+\delta_h)ds.
\]

Multiplying the corresponding scalar differential inequality by `e^{-Λt}` and integrating gives (6). Integrating `J` along the line segment joining the two parameter vectors gives (7).

### Computation, continuum inputs, and finite precision

For empirical data, (4) is computed in one pass. Preprocessing must read the original data; the result does not claim sublinear input-reading cost. Afterwards, storage and per-step evaluation use only `N` nodes, `2N` statistics, and the ordinary network state. Width and depth still determine network storage and work.

For a population law, (4) requires cell probabilities and first label totals. These are source-measure statistics, not a training-trajectory oracle. A claim of an actual numerical algorithm requires that the population law be supplied in an effective form from which these finitely many statistics can be computed to prescribed tolerance. An arbitrary abstract probability measure supplies no such computability guarantee. The mathematical approximation theorem applies to every such measure; the effective implementation claim has this additional input-access hypothesis.

The approximation does not need arbitrary-precision encoding of the dataset. If stored coefficients obey

\[
\sum_j|p_j-\widehat p_j|\le a,
\qquad
\sum_j|b_j-\widehat b_j|\le b,
\]

then the extra vector-field error on `Θ` is at most

\[
2d_*M_1(M_0a+b).
\tag{9}
\]

Choose rational approximations with nonnegative normalized masses and sufficiently small errors. The same stability estimate, with a first-exit argument using the one-unit reserve in (2), ensures finite-precision coefficients achieve any positive target tolerance. Numerical time-discretization error is another separately controllable approximation axis.

## 2. Which response fields this also controls

For each hidden unit or other indexed observable, suppose `G_θ(x)` is uniformly Lipschitz in `θ` on `Θ` with constant `K_θ` and Hölder in `x` with constant `K_x`. The piecewise reconstruction

\[
\widehat G_t(x)=G_{\theta_h(t)}(\xi_j),\qquad x\in A_j,
\]

satisfies

\[
\sup_{t\le T,x\in X}
\|G_{\theta(t)}(x)-\widehat G_t(x)\|
\le K_\theta\delta_hQ_T(\Lambda)+K_xh^\alpha.
\tag{10}
\]

This includes instantaneous hidden preactivations, activations, and finite-order parameter response quantities for which the required derivatives are bounded. Bounds uniform over units require uniform constants across those units; a bound for fixed width does not prove that.

For a specific history field

\[
H_t(x)=\int_0^t G_{\theta(s)}(x)\,ds,
\]

store `H_j(0)=0` and evolve `\dot H_j=G_{θ_h}(ξ_j)` alongside (5). This remains finite and autonomous, and

\[
\sup_{t\le T,x\in X}|H_t(x)-H_{j(x)}(t)|
\le T\bigl[K_\theta\delta_hQ_T(\Lambda)+K_xh^\alpha\bigr].
\tag{11}
\]

More complicated history fields need their defining evolution and a closure/stability argument. Smoothness of the network output alone does not prove a bound for every named response history. A field with `k` independent input arguments can be discretized on `X^k`, potentially costing `N^k`; this is independent of `m` but may be infeasible. Continuous-time histories are not automatically finite-memory states; (11) works because this particular history has a local ODE.

The basis functions `1_{A_j}(x)` are fixed input coordinates. The values at the nodes and every hidden network feature evolve. A fixed coordinate chart therefore does not imply frozen neuronal features.

If a requested field contains arbitrary raw labels, such as `y(x)` itself, the assumptions above do not permit its uniform reconstruction by cell averaging. Squared-loss training avoids that requirement because labels enter (1) linearly through the signed measure

\[
\nu(A)=\mathbb E_P[y\mathbf1_{x\in A}].
\]

This distinction is essential: the theorem controls the whole parameter and prediction trajectory, and the regular response observables just specified; it does not compress an arbitrary label function in the supremum norm.

## 3. What complexity should control

The partition result uses `N_X(h)`. If `N_X(h) ≤ C h^{-d_eff}`, then state size scales at worst like a constant times

\[
\left(\frac{Q_T(\Lambda)\,[M_1H_0+(M_0+Y_1)H_1]}{\varepsilon}\right)^{d_{\rm eff}/\alpha},
\]

with the relevant output constants added when needed. This exposes the curse of dimension and the horizon dependence. Intrinsic dimension is useful only together with an actual uniform covering estimate; merely naming a manifold or its dimension does not provide one.

One can use the geometry actually seen by training. On `Θ`, define the pseudometric

\[
\rho_\Theta(x,x')
=\sup_{\theta\in\Theta}
\|f_\theta(x)J_\theta(x)-f_\theta(x')J_\theta(x')\|
+Y_1\sup_{\theta\in\Theta}\|J_\theta(x)-J_\theta(x')\|.
\tag{12}
\]

For `Y₁=0` the label term vanishes. A partition with `ρ_Θ(x,q(x)) ≤ η` gives source error at most `4d_*η`: the expected product difference is at most `η`, and the label-weighted Jacobian difference is at most `E|y|·η/Y₁≤η` when `Y₁>0`. Thus inputs that are indistinguishable by all reachable gradient integrands may share a representative even if they are far apart in the raw Euclidean metric. The covering complexity of `(X,ρ_Θ)` is more canonical than matrix rank. Computing or bounding this pseudometric efficiently is a separate problem; its definition is not itself an efficient algorithm. The explicit Hölder construction above avoids needing a trajectory-dependent metric.

Spatial Sobolev or analytic bounds can improve approximation rates when they yield approximation estimates in a norm strong enough to control the gradient integrals. A Sobolev norm that does not control continuity cannot simply be substituted into the uniform-cell proof for arbitrary input measures: such measures may concentrate on the exceptional set. Analytic structure can justify high-order coordinates, but one must still control derivative approximation and nonlinear error propagation. A small Barron norm similarly needs an explicit integration/derivative approximation theorem; the name of the norm does not provide closure.

The image `{x↦G_θ(x): θ∈Θ}` is a parameterized set of functions. Its parameter count can bound its nonlinear description length without making its linear rank small. In fact, representing the instantaneous field by the original `θ` is already an exact nonlinear description at fixed width. The remaining challenge is evaluating the data expectation from finite source statistics. History fields can escape this finite-dimensional image and need an additional causal representation.

## 4. Exact special case: polynomial input algebra, without frozen features

Suppose there are `L` hidden layers, each activation is a polynomial of degree at most `s`, and the readout is affine. With arbitrary trainable weights and biases, the network output is a polynomial in `d` input coordinates of degree at most `q=s^L`:

\[
f_\theta(x)=\sum_{|\beta|\le q}c_\beta(\theta)x^\beta.
\tag{13}
\]

This degree bound follows by induction: affine combinations do not increase the input degree, and composition with a degree-`s` polynomial multiplies it by at most `s`. Differentiating with respect to parameters changes coefficients but not input exponents.

Assume `E||x||^{2q}<∞` and `Ey²<∞`. These ensure finiteness of all the following moments, using Cauchy–Schwarz for mixed moments:

\[
M_\gamma=\mathbb E x^\gamma\quad(|\gamma|\le2q),
\qquad
B_\beta=\mathbb E[yx^\beta]\quad(|\beta|\le q).
\]

Substitution of (13) into (1) gives the exact autonomous equation

\[
\dot\theta
=-2D\left[
\sum_{|\alpha|,|\beta|\le q}
c_\alpha(\theta)\,\nabla_\theta c_\beta(\theta)M_{\alpha+\beta}
-\sum_{|\beta|\le q}\nabla_\theta c_\beta(\theta)B_\beta
\right].
\tag{14}
\]

The number of stored input statistics is at most

\[
\binom{d+2q}{2q}+\binom{d+q}{q},
\]

independent of `m` and width. The parameter state and coefficient evaluation still depend on width. All hidden features remain trainable; only the monomial coordinate functions are fixed. The Gaussian initialization is reused exactly in `θ₀` and hence in `c(θ₀)`.

Equation (14) is exactly the original gradient flow for this polynomial architecture, with no time-horizon approximation. Equality holds throughout the common interval of existence; the squared-loss energy bound prevents finite-time parameter escape, yielding global existence under these finite-moment assumptions. Exact real-valued moment availability is a mathematical premise; numerical rounding again gives finite-horizon approximate equality. Replacing a nonpolynomial activation by a polynomial would change the model and needs a separate approximation theorem; this exact result does not license that substitution silently.

## 5. An obstruction to universal exact finite moment lists

Even one smooth nonpolynomial neuron can have an infinite-dimensional family of gradient integrands. On `X=[0,1]`, take `f_θ(x)=e^{θx}`, `y=0`, scalar `D=1`. Its exact velocity is

\[
F_\mu(\theta)=-2\int x e^{2\theta x}\,d\mu(x).
\tag{15}
\]

Suppose the data are summarized only by a fixed finite list `∫φ_j dμ`, with the `φ_j` independent of `θ`, and that these summaries are intended to determine (15) for every probability measure and every `θ` in a nonempty open interval.

The functions `x e^{2θx}` for distinct `θ` are linearly independent. Indeed, after dividing a vanishing finite linear combination by `x` for `x>0`, differentiate the resulting combination of exponentials at `x=0` to orders `0,…,r-1`. This gives a Vandermonde linear system in the distinct numbers `2θ₁,…,2θ_r`, whose determinant `∏_{i<j}(2θ_j-2θ_i)` is nonzero. All coefficients therefore vanish.

Consequently some `g(x)=x e^{2θ*x}` lies outside the finite-dimensional span `V=span{1,φ₁,…,φ_K}`. There exists a finitely supported signed measure `σ` that annihilates `V` but not `g`: choose a basis of `V`, select finitely many evaluation points making its evaluation matrix invertible, interpolate `g` at those points, and choose one extra point where that interpolant differs from `g`. Evaluation at the extra point minus the corresponding linear combination of the basis-point evaluations is the required `σ`.

Since `σ(1)=0`, its positive and negative parts have the same nonzero mass. Normalize them to probability measures `μ_+` and `μ_-`. They have the same proposed summary statistics but different values of (15) at `θ*`. Thus a universal exact fixed finite list of linear data statistics cannot close this nonpolynomial family.

This is a no-go result for the stated finite-moment representation. It is not a no-go result for finite-accuracy approximation, adaptive data summaries, a single prescribed initialization, or every regular nonlinear finite encoding. In particular, one must not use it to reject the partition theorem or the broad existence of other admissible finite surrogates.

## 6. Why finite-time validity does not imply all-time validity

The factor `Q_T(Λ)` grows with the time horizon. Energy decay does not by itself replace it with a time-uniform bound. A small perturbation can move a trajectory off a stationary saddle and into a distant basin.

For a direct squared-loss example with a nonlinear hidden feature, let

\[
f_{a,b}(x)=a\tanh(b+x),\qquad y=1,\qquad (a(0),b(0))=(0,0),\qquad D=I.
\]

For the one-point law `x=0`, the exact gradient vanishes at initialization and the trajectory stays `(0,0)` forever. Replace `x=0` by `x=h>0`. Writing `s=b+h` and `r=a\tanh s-1`, the perturbed equations are

\[
\dot a=-2r\tanh s,\qquad
\dot s=-2ra\operatorname{sech}^2s.
\]

Initially `\dot a=2\tanh h>0`. While `r<0`, `a` and `s` are nondecreasing and `s≥h`; moreover

\[
\dot r=-2r\left(\tanh^2s+a^2\operatorname{sech}^4s\right).
\]

The expression in parentheses is at least `tanh²h`, so `r→0` provided the trajectory continues. Continuation and boundedness follow from the invariant

\[
a^2-\sinh^2s=-\sinh^2h:
\]

the function `a\tanh s=\sqrt{\sinh^2s-\sinh^2h}\tanh s` increases from zero to above one at a finite `s`, and `r` approaches zero without crossing it. Thus the perturbed prediction at the common test input `x=h` converges to one, whereas the original prediction at that input stays zero. The vector fields converge uniformly on compact parameter sets as `h→0`, yet the supremum over all times and inputs of the prediction discrepancy is at least one for every `h>0`.

This example establishes the insufficiency of smoothness and loss descent for all-time perturbation control. It does not establish impossibility of every all-time compression scheme, nor an almost-sure obstruction for Gaussian initialization: the displayed initialization is an exact saddle. A width-dependent or probabilistic long-time theorem would need additional stability and basin-separation information.

If a stronger system satisfies the contractive estimate

\[
\langle\theta-\eta,F(\theta)-F(\eta)\rangle
\le-\lambda\|\theta-\eta\|^2\quad(\lambda>0)
\]

on a common invariant region, the same source-error argument yields `e(t)≤δ_h(1-e^{-λt})/λ`. This is an explicit sufficient condition for all-time control, but it is a new assumption and is not generally available for deep-network training.

## Status and decisive missing bridge

- Internally proved: arbitrary-accuracy, finite-horizon partition approximation of the full fixed-width nonlinear gradient-flow parameter and prediction trajectory, with `m`-independent complexity and no label smoothness assumption.
- Internally proved: corresponding approximation for regular instantaneous fields and for the explicitly specified integral history field.
- Internally proved: exact finite moment closure for polynomial activation architectures.
- Internally proved within its stated representation class: fixed finite linear data statistics cannot exactly encode every gradient field of the exponential neuron family.
- Not established: width-uniform constants; a finite closure of an unspecified population response-history equation; efficient rates in high intrinsic dimension; or all-time control in general.

The highest-value bridge is to write the actual per-neuron response-history equations and show that their input regularity constants and finite-dimensional causal state can be bounded uniformly in the intended width limit. Without that bridge, fixed-width data compression is rigorous but does not settle the stronger population-field question.
