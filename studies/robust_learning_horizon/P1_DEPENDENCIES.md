# Complete frozen mathematical dependencies

The new proof uses the stated specializations of these complete units. Older arctangent and equal-label scopes remain as stated; their different architectures are not silently substituted. Their proofs are supplied to expose the dependencies and adaptations.

# Frozen source: docs/NOTATION.md lines 1–98

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


# Frozen source: docs/global_nonlinear.md lines 1841–2452

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



# Frozen source: docs/global_nonlinear.md lines 3835–5257

### C.4. Training-law stability for two hidden tanh layers

Within each C.4.1–C.4.4 proof unit, unqualified section and equation numbers are
local. The typed abbreviations w, A, c denote the full first row, W^(2),
and W^(3), respectively; they do not change the canonical normalization.

This section proves a local quantitative statement about the actual nonlinear
learning algorithm. The proof retains the Gaussian matrix action and its
adjoint and permits every training law on the compact observation space.

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

The conclusion concerns finite-time training-law stability with genuine
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


# Frozen source: docs/special_data_limits.md lines 134–1349

## I. Opposite labels at the orthogonal and antiparallel angles

Both hidden activations are \(\arctan\). The proof covers exactly the two
geometries in the theorem, not intermediate nonzero correlations.
Simultaneous reversal of both labels and readout gives the other
opposite-label ordering with the same initialized law and all conclusions.

### I.1. Model, normalization and theorem


**I.1.1. Finite model and physical clock.** Fix a positive integer \(d\), two
deterministic inputs \(x_1,x_2\in\mathbb R^d\) with
\(\|x_1\|_{\mathbb R^d}=\|x_2\|_{\mathbb R^d}=\sqrt d\), and
\[
 G_{ab}=d^{-1}x_a^Tx_b,\qquad G_{12}=\rho\in\{0,-1\},
 \qquad (y_1,y_2)=(1,-1).
 \tag{I.1}
\]
The case \(\rho=0\) requires \(d\ge2\). At \(\rho=-1\), necessarily
\(x_2=-x_1\). The two hidden widths are both \(n\). Independently initialize
\[
 V^{(1)}_{n,ij}(0)\sim N(0,1/d),\qquad
 W^{(2)}_{n,ij}(0)\sim N(0,1/n),\qquad
 W^{(3)}_{n,i}(0)\sim N(0,n^{-2}),
 \tag{I.2}
\]
where the shapes are \(n\times d,n\times n,n\), respectively.
\(W^{(3)}_n\) denotes the rescaled readout used in the following prediction;
no further readout rescaling is understood. Put
\[
 \phi(z)=\arctan z,\qquad \phi'(z)=\frac1{1+z^2},
 \qquad \phi''(z)=\frac{-2z}{(1+z^2)^2},\qquad B=\pi/2.
 \tag{I.3}
\]
For \(a=1,2\),
\[
 \begin{aligned}
 z^{(1)}_{n,a}&=V^{(1)}_nx_a,& h^{(1)}_{n,a}&=\phi(z^{(1)}_{n,a}),\\
 z^{(2)}_{n,a}&=W^{(2)}_nh^{(1)}_{n,a},&h^{(2)}_{n,a}&=\phi(z^{(2)}_{n,a}),\\
 f_{n,a}&=\frac1n(W^{(3)}_n)^Th^{(2)}_{n,a},&r_{n,a}&=f_{n,a}-y_a,\\
 \mathcal L_n&=r_{n,1}^2+r_{n,2}^2.&&
 \end{aligned}                                                   \tag{I.4}
\]
All activations act coordinatewise. Define the backward fields without
residual factors by
\[
 \delta^{(2)}_{n,a}=W^{(3)}_n\phi'(z^{(2)}_{n,a}),\qquad
 q^{(1)}_{n,a}=(W^{(2)}_n)^T\delta^{(2)}_{n,a},\qquad
 \delta^{(1)}_{n,a}=\phi'(z^{(1)}_{n,a})q^{(1)}_{n,a}.
 \tag{I.5}
\]
The raw updates, with every quantity on the right evaluated at step
\(k\), are exactly
\[
 \begin{aligned}
 V^{(1)}_{n,k+1}&=V^{(1)}_{n,k}
       -\frac{2\eta_n}{d}\sum_a r_{n,ka}\delta^{(1)}_{n,ka}x_a^T,\\
 W^{(2)}_{n,k+1}&=W^{(2)}_{n,k}
       -\frac{2\eta_n}{n}\sum_a r_{n,ka}\delta^{(2)}_{n,ka}
                                                   (h^{(1)}_{n,ka})^T,\\
 W^{(3)}_{n,k+1}&=W^{(3)}_{n,k}
       -2\eta_n\sum_a r_{n,ka}h^{(2)}_{n,ka},\qquad \eta_n=n^{-2}.
 \end{aligned}                                                   \tag{I.6}
\]
Thus physical time is \(t=k\eta_n\), without an additional time change.
Between nodes interpolate these three raw parameter arrays linearly,
and recompute (I.4)--(I.5) from the interpolated arrays. Velocities at
interior nodes mean right velocities, and at a terminal node mean left
velocities. The actual Gaussian readout in (I.2) is retained throughout.

For precision, (I.6) is gradient descent for loss SUM in the parameter
metric
\[
 \|(E^{(1)},E^{(2)},E^{(3)})\|_{\mathrm{par},n}^2
  =\frac d n\|E^{(1)}\|_F^2+\|E^{(2)}\|_F^2
                                      +\frac1n\|E^{(3)}\|_{\ell^2}^2.
 \tag{I.7}
\]
Indeed the ordinary Euclidean gradients are respectively
\((2/n)\sum r_a\delta^{(1)}_ax_a^T\),
\((2/n)\sum r_a\delta^{(2)}_a(h^{(1)}_a)^T\), and
\((2/n)\sum r_ah^{(2)}_a\); applying the inverse metric gives (I.6).
Specifying this metric is essential: ordinary Euclidean descent on all
three displayed rescaled arrays would be a different model. Finite
gradient flow means the right sides of (I.6) divided by \(\eta_n\).

**I.1.2. Spaces and the population equations.** The two finite neuron
spaces are separate copies of \(\mathbb R^n\). We use ordinary
Euclidean norms and display empirical normalization explicitly:
\[
 \frac1n v^Tw,\qquad
 \frac1n\|v\|_{\ell^2}^2=\frac1n\sum_i|v_i|^2.
 \tag{I.8}
\]
In particular \(W^{(2)}_n\) acts by ordinary matrix multiplication;
there is no extra \(1/n\) in its action. Its adjoint is its actual
transpose. For two probability spaces to be constructed, write
\(\mathcal H_\ell=L^2(\Omega_\ell,\mu_\ell)\),
\(\|v\|_{\mathcal H_\ell}^2=\mathbb E_\ell|v|^2\). Products are
pointwise on the indicated space. The rank-one operator
\[
 (v\otimes h)e=v\mathbb E_1[he],\qquad
 \|v\otimes h\|_{\mathrm{op}}=\|v\otimes h\|_{\mathrm{HS}}
                =\|v\|_{\mathcal H_2}\|h\|_{\mathcal H_1}
 \tag{I.9}
\]
is \(vh^T/n\) at finite width. The finite Hilbert--Schmidt norm is
the ordinary Frobenius norm; the finite operator norm is the ordinary
Euclidean operator norm.
In the infinite spaces, the operator norm is
\(\sup_{\|e\|_2=1}\|We\|_2\), and the squared Hilbert--Schmidt norm
is \(\sum_j\|We_j\|_2^2\) for an orthonormal basis of the domain.
For (I.9), expansion of \(h\) in that basis gives the asserted norm
identity directly.

The population state consists of a first-row field
\(V^{(1)}(t)\in L^2(\Omega_1;\mathbb R^d)\), a bounded operator
\(W^{(2)}(t):\mathcal H_1\to\mathcal H_2\) with Hilbert--Schmidt
increments, and \(W^{(3)}(t)\in\mathcal H_2\). Set
\[
 \begin{aligned}
 Z^{(1)}_a&=V^{(1)}x_a,&H^{(1)}_a&=\phi(Z^{(1)}_a),\\
 Z^{(2)}_a&=W^{(2)}H^{(1)}_a,&H^{(2)}_a&=\phi(Z^{(2)}_a),\\
 f_a&=\mathbb E_2[W^{(3)}H^{(2)}_a],&r_a&=f_a-y_a,\\
 \delta^{(2)}_a&=W^{(3)}\phi'(Z^{(2)}_a),&
 Q^{(1)}_a&=W^{(2)*}\delta^{(2)}_a,\\
 \delta^{(1)}_a&=\phi'(Z^{(1)}_a)Q^{(1)}_a,&\mathcal L&=\sum_a r_a^2.
 \end{aligned}                                                   \tag{I.10}
\]
The star is the actual Hilbert adjoint on these two separate spaces.
The autonomous physical equations are
\[
 \begin{aligned}
 \dot V^{(1)}&=-\frac2d\sum_a r_a\delta^{(1)}_ax_a^T,
 &\dot Z^{(1)}_a&=-2\sum_b G_{ab}r_b\delta^{(1)}_b,\\
 \dot W^{(2)}&=-2\sum_a r_a\delta^{(2)}_a\otimes H^{(1)}_a,
 &\dot W^{(3)}&=-2\sum_a r_aH^{(2)}_a.
 \end{aligned}                                                   \tag{I.11}
\]
Initialize the first row by independent \(N(0,1/d)\) coordinates,
write \(G_a=V^{(1)}(0)x_a\), and initialize \(W^{(3)}(0)=0\).
The initial \(W^{(2)}(0)\), including its joint law with every generated
field and its adjoint, is constructed in Section I.3; an arbitrary bounded
operator does not suffice.

**I.1.3. Theorem I.1 (special-angle limit and observable scope).** There are countably
generated spaces and this canonical operator, with
\(\|W^{(2)}(0)\|_{\mathrm{op}}\le8\), on which (I.11) has a unique
solution for all finite \(t\ge0\). Its law is deterministic and is the
full-sequence limit in probability of (I.6), and also of finite gradient
flow from (I.2), on every fixed \([0,T]\), \(T<\infty\). It is unique
from each reached state, with the entire state retained at restart.

Here is the precise joint meaning of this limit. In each neuron
population separately, empirical same-neuron tuples include both samples
and all their hidden forward and backward fields. Their path laws on
\(C([0,T];\mathbb R^j)\), with the supremum norm, converge in every
fixed Wasserstein order \(1\le p<\infty\). In population 1 the tuple
may contain \(V^{(1)},Z^{(1)}_a,H^{(1)}_a,Q^{(1)}_a,
\delta^{(1)}_a\); in population 2 it may contain
\(W^{(3)},Z^{(2)}_a,H^{(2)}_a,\delta^{(2)}_a\). Finite lists of
times, fields, and continuous polynomial-growth tests converge jointly.
No artificial pairing of neurons in different populations is asserted.
Here the order-\(p\) Wasserstein distance on a metric space is the
infimum, over all couplings of the two probability laws, of
\((\mathbb E[\operatorname{dist}(X,Y)^p])^{1/p}\).

Predictions, loss, and all three kernel blocks converge uniformly in
\(t\in[0,T]\), in probability, to
\[
 \begin{aligned}
 K^{(1)}_{ab}&=G_{ab}\mathbb E_1[\delta^{(1)}_a\delta^{(1)}_b],\\
 K^{(2)}_{ab}&=\mathbb E_2[\delta^{(2)}_a\delta^{(2)}_b]
                      \mathbb E_1[H^{(1)}_aH^{(1)}_b],\\
 K^{(3)}_{ab}&=\mathbb E_2[H^{(2)}_aH^{(2)}_b],\qquad
 K=K^{(1)}+K^{(2)}+K^{(3)}.
 \end{aligned}                                                   \tag{I.12}
\]
The finite formulas use precisely (I.8). For either matrix orientation,
the assertion also includes any fixed finite collection of admissible
probes and their joint field laws in Wasserstein order 2. An admissible
probe is formed by a fixed finite program from the initialization, independent
iid roots with every finite moment, deterministic linear combinations,
smooth globally Lipschitz coordinate maps with bounded first derivatives,
empirical products with factor \(1/n\), actions of \(W^{(2)}_n(0)\) or its transpose,
and the learned rank integrals at prescribed times. Its instructions,
scalar coefficients, and additional-root laws are fixed as width varies,
apart from the explicitly specified model normalizations; arbitrary
width-dependent amplification of the vanishing initial readout is not
an admissible instruction. Limits of such
probes are admitted when their approximation errors vanish in ordinary
normalized \(L^2\), uniformly in probability at finite width, and in
population \(L^2\). This definition includes the unbounded velocity
probes proved admissible in Section I.4; it does not quantify over arbitrary
width-dependent directions. At population level actions are those of
\(W^{(2)}(t)\) and \(W^{(2)*}(t)\).

Every preactivation and activation velocity in (I.73) has joint
Wasserstein-2 convergence
at fixed times, convergence in integrated mean square under the
approximations used below, and convergence of its squared normalized
norm uniformly in time in probability. The same holds for the readout
velocity. The raw parameter speeds converge in their metrics
\[
 \frac d n\|\dot V^{(1)}_n\|_F^2,\qquad
 \|\dot W^{(2)}_n\|_F^2,\qquad
 \frac1n\|\dot W^{(3)}_n\|_{\ell^2}^2,                       \tag{I.13}
\]
and so do their time integrals and the individual hidden-velocity
energies. The squared sizes of parameter increments converge in the
analogous quadratic metrics; the middle statement concerns
\(W^{(2)}(t)-W^{(2)}(0)\),
not a Hilbert--Schmidt norm of the initial operator. There is no claim
of operator-norm convergence between matrices of different dimensions.

At every finite \(t\ge0\), for each \(\ell=1,2\) and sample \(a\),
\[
 \inf_{u,v\in\mathbb R}
  \mathbb E_\ell[(\phi(Z^{(\ell)}_a(t))-uZ^{(\ell)}_a(t)-v)^2]>0.
 \tag{I.14}
\]
At every physical \(t>0\), all four preactivation speeds, all four
activation speeds, both hidden-parameter speeds and the readout speed
are strictly positive in their stated norms. The limiting population
hidden speeds at zero are zero. The full kernel is nonconstant on every sufficiently short
interval starting at zero: in the label direction its first nonzero
change has a strictly positive quadratic coefficient in physical time.

The proof first constructs the deterministic global flow for a specified
operator. It then proves the finite Gaussian program law, builds the
canonical operator, and obtains global bounded Gaussian remainders by
fresh-root forcing. Deterministic mesh comparisons give the full
observable limit. Finally the exchange symmetry, Gaussian tails, and
an initial expansion prove (I.14), strict motion, and kernel change.

### I.2. Deterministic flow, restart, and the raw discretization

**I.2.1. The special-angle coordinate.** Introduce the one auxiliary
scalar function and its inverse
\[
 F(z)=z+z^3/3,\qquad U_a=F(Z^{(1)}_a),\qquad Z^{(1)}_a=F^{-1}(U_a).
 \tag{I.15}
\]
The finite version is \(u_{n,a}=F(z^{(1)}_{n,a})\).
Since \(F'\ge1\), its inverse is defined on all of \(\mathbb R\),
is 1-Lipschitz, and has derivative \(\phi'(F^{-1}(u))\).
The function \(\phi(F^{-1}(u))\) has derivative
\(\phi'(F^{-1}(u))^2\), also bounded by 1. Further,
\(|\phi|\le B\), \(0<\phi'\le1\), and \(|\phi''|\le1\).
All source derivatives used below are continuous; repeated scalar
differentiation of these rational expressions supplies bounded
higher derivatives when needed. The Gaussian root satisfies
\(\mathbb E F(G_a)^2=1+2+15/9=14/3\).
The moments used here follow by scalar Gaussian integration by parts:
\(\mathbb E G^{2j}=(2j-1)\mathbb E G^{2j-2}\), starting with
\(\mathbb E1=1\).

For \(\rho=0\), with prescribed integrable controls \(c_a\), use
\[
 \dot U_a=c_aQ^{(1)}_a,\qquad
 \dot W^{(2)}=\sum_a c_a\delta^{(2)}_a\otimes H^{(1)}_a,
 \qquad \dot W^{(3)}=\sum_a c_aH^{(2)}_a.                    \tag{I.16}
\]
Physical feedback is \(c_a=-2r_a\). The cancellation
\(F'(Z)\phi'(Z)=1\) makes (I.16) exactly (I.11).

For \(\rho=-1\), at every raw parameter state,
\[
 Z^{(\ell)}_2=-Z^{(\ell)}_1,\quad H^{(\ell)}_2=-H^{(\ell)}_1,
 \quad f_2=-f_1,\quad
 \delta^{(\ell)}_2=\delta^{(\ell)}_1,\quad Q^{(1)}_2=Q^{(1)}_1.
 \tag{I.17}
\]
These identities follow from opposite inputs, odd activations, and even
derivatives, and require no restriction on the readout. Retain one
independent first field in (I.16), replace the summed control by
\(c=c_1-c_2\), and use sample 1 in every right side. Physical feedback
is \(c=-4r_1\); the factor four is forced by loss SUM. Equivalently,
on the invariant two-sample state,
\(\dot U_a=\sum_b G_{ab}c_bQ^{(1)}_b\).

The first row is reconstructed, including its unchanged orthogonal
component, by
\[
 V^{(1)}(t)=V^{(1)}(0)+\sum_{a=1}^{m_\rho}
             (Z^{(1)}_a(t)-G_a)x_a^T/d,
 \quad m_\rho=2\ (\rho=0),\quad m_\rho=1\ (\rho=-1).
 \tag{I.18}
\]
Thus \(d\mathbb E_1|\dot V^{(1)}|^2=\sum_{a=1}^{m_\rho}
\|\dot Z^{(1)}_a\|_{\mathcal H_1}^2\); at finite width it is
\((d/n)\|\dot V^{(1)}_n\|_F^2\). Opposite sample fields do not count
the same first-matrix motion twice.

**I.2.2. Ordinary \(L^2\) stability.** Use the Banach norm
\[
 \sum_{a=1}^{m_\rho}\|\Delta U_a\|_{\mathcal H_1}
   +\|\Delta W^{(2)}\|_p+\|\Delta W^{(3)}\|_{\mathcal H_2},
 \qquad p=\mathrm{op}\text{ or }\mathrm{HS}.                 \tag{I.19}
\]
For \(p=\mathrm{HS}\) the operator coordinate is its increment from
the fixed initial operator. Suppose two states have operator norms at
most \(a_0'\) and readout essential suprema at most \(M\). Write
\(e_a=\|U_a-\widetilde U_a\|_2\),
\(e_W=\|W^{(2)}-\widetilde W^{(2)}\|_p\), and
\(e_3=\|W^{(3)}-\widetilde W^{(3)}\|_2\), where each unmarked
\(L^2\) norm is on the field's own probability space. Direct subtraction
gives
\[
 \begin{aligned}
 \|Z^{(1)}_a-\widetilde Z^{(1)}_a\|_2,
 \|H^{(1)}_a-\widetilde H^{(1)}_a\|_2&\le e_a,\\
 \|Z^{(2)}_a-\widetilde Z^{(2)}_a\|_2,
 \|H^{(2)}_a-\widetilde H^{(2)}_a\|_2&\le a_0'e_a+Be_W,\\
 \|\delta^{(2)}_a-\widetilde\delta^{(2)}_a\|_2
              &\le e_3+M(a_0'e_a+Be_W),\\
 \|Q^{(1)}_a-\widetilde Q^{(1)}_a\|_2
              &\le a_0'e_3+M(a_0')^2e_a+M(a_0'B+1)e_W,\\
 \|\delta^{(2)}_a\otimes H^{(1)}_a
      -\widetilde\delta^{(2)}_a\otimes\widetilde H^{(1)}_a\|_p
              &\le Be_3+M(Ba_0'+1)e_a+MB^2e_W,\\
 |f_a-\widetilde f_a|&\le Be_3+M(a_0'e_a+Be_W).
 \end{aligned}                                                   \tag{I.20}
\]
For example, split the delta difference into the readout difference
times \(\phi'\) and the bounded second readout times the difference
of \(\phi'\). Split a rank difference into two rank-one terms and
apply (I.9). These proofs use neither a bound on \(Q^{(1)}\) in
\(L^\infty\) nor a bounded \(L^p\) action of the operator for \(p\ne2\).
They prove local Lipschitz bounds for the transformed physical field,
depending only on \(a_0',M\), uniformly in width.

To construct a solution despite the \(L^\infty\) ball not being open
in \(L^2\), replace occurrences of the readout in predictions and
deltas by its pointwise clipping to \([-M,M]\). Clipping is
1-Lipschitz in \(L^2\). On a small ball in (I.19) the resulting vector
field is bounded and Lipschitz. On continuous paths staying in that
ball, its integral map preserves the ball if time times the drift bound
is less than the radius, and contracts if time times the Lipschitz
constant is less than 1. Successive iterates are a geometrically Cauchy
sequence in the complete path space. The limit solves the equation;
the same inequality proves uniqueness. For integrable controls use
their accumulated absolute integral instead of interval length.

The readout integral gives
\[
 \|W^{(3)}(t)-W^{(3)}(0)\|_\infty\le BS(t),\quad
 S(t)=\int_0^t\sum_a|c_a(v)|\,dv,                            \tag{I.21}
\]
where the reduced case uses \(S=\int|c|\). Choosing \(M\) larger
than the initial readout bound and an initially short interval makes
the clipping inactive. This constructs the original solution. If two
solutions stay in fixed bounds, subtraction of their integral equations
gives
\[
E(t)\le E(0)+C\int_0^t\sum_a|c_a|E
                  +C\int_0^t\sum_a|c_a-\widetilde c_a|.
\]
Iterating this inequality, or multiplying its absolutely continuous
scalar majorant by \(\exp(-C S(t))\), proves
\[
 E(t)\le e^{CS(t)}\left(E(0)+C\int_0^t\sum_a
                                      |c_a-\widetilde c_a|\right).
 \tag{I.22}
\]
Here \(C\) is a scalar bound depending on the two state bounds,
not the input Gram. For physical feedback, (I.20) instead gives
\(E(t)\le e^{C_Tt}E(0)\). If the initial operators agree, operator
differences may be measured in Hilbert--Schmidt norm. If they differ,
measure their initial difference in operator norm. Their evolved
increments relative to the respective initial operators may still
be compared in Hilbert--Schmidt norm: in the rank-difference estimate
(I.20), bound the full operator difference by the initial operator-norm
difference plus the Hilbert--Schmidt difference of those increments,
and apply the same integral inequality.

**I.2.3. Global extension and energy.** Put
\(a_0=\|W^{(2)}(0)\|_{\mathrm{op}}\),
\(b_2=\|W^{(3)}(0)\|_2\), \(b_\infty=\|W^{(3)}(0)\|_\infty\).
Integration of the rank equation and (I.21) gives
\[
 \begin{aligned}
 \|W^{(3)}(t)\|_2&\le b_2+BS(t),&
 \|W^{(3)}(t)\|_\infty&\le b_\infty+BS(t),\\
 \|W^{(2)}(t)-W^{(2)}(0)\|_p
     &\le Bb_2S(t)+\tfrac12B^2S(t)^2,&
 \|W^{(2)}(t)\|_{\mathrm{op}}
     &\le a_0+Bb_2S(t)+\tfrac12B^2S(t)^2,\\
 \sum_a\|U_a(t)-U_a(0)\|_2
     &\le\int_0^{S(t)}(a_0+Bb_2v+B^2v^2/2)(b_2+Bv)\,dv.
 \end{aligned}                                                   \tag{I.23}
\]
These bounds imply extension on any finite interval of finite action:
the derivative is bounded by an integrable scalar times a fixed
constant, so the state has a limit in (I.19) at any finite candidate
endpoint. The readout is also Cauchy in \(L^\infty\) by (I.21).
The local construction at that limit extends the solution.

Here and below composition can be differentiated along a \(C^1\)
\(L^2\) curve when the scalar map has bounded continuous derivative.
To prove this, replace \(v(t+h)\) by \(v(t)+h\dot v(t)\); the
Lipschitz bound makes the difference-quotient error tend to zero.
For the fixed direction \(\dot v(t)\), scalar difference quotients
converge pointwise and are bounded by a constant times \(|\dot v(t)|\).
Dominated convergence of their squares proves the \(L^2\) chain rule.
This is a statement along curves, not an assertion of Fréchet
differentiability of every composition map on \(L^2\).

Differentiate (I.10) and move \(W^{(2)}\) through its actual adjoint.
The three parameter contributions give, respectively, the three blocks
in (I.12), hence
\[
 \dot f=-2Kr,\qquad
 \dot{\mathcal L}=-4r^TKr
  =-\left(\sum_{a=1}^{m_\rho}\|\dot Z^{(1)}_a\|_2^2
       +\|\dot W^{(2)}\|_{\mathrm{HS}}^2
       +\|\dot W^{(3)}\|_2^2\right).                         \tag{I.24}
\]
Each block is positive semidefinite: it is the Gram of
\((x_a/\sqrt d)\otimes\delta^{(1)}_a\), of
\(\delta^{(2)}_a\otimes H^{(1)}_a\), or of \(H^{(2)}_a\),
respectively. In the antiparallel reduction the first term in (I.24)
contains one field. For \(R_0=\sqrt{L(0)}\),
\[
 \|r(t)\|_{\mathbb R^2}\le R_0,\quad
 S(t)\le2\sqrt2R_0t,\quad
 \int_0^T\left(\sum_{a=1}^{m_\rho}\|\dot Z^{(1)}_a\|_2^2
  +\|\dot W^{(2)}\|_{\mathrm{HS}}^2+\|\dot W^{(3)}\|_2^2\right)dt
                =L(0)-L(T).                                 \tag{I.25}
\]
Equations (I.23)--(I.25) prove global existence. For population zero
readout, \(L(0)=2\), \(S(t)\le4t\), and in particular
\[
 \|W^{(3)}(t)\|_\infty\le4Bt,\qquad
 \|W^{(2)}(t)\|_{\mathrm{op}}\le8+8B^2t^2.                  \tag{I.26}
\]

Uniqueness also holds among ordinary \(L^2\) solutions of the original
integral equations, rather than only the transformed class. Such a
solution has continuous residuals; its readout integral gives a local
essential bound. Its first equation has the form
\(\dot Z=c\phi'(Z)Q\), with \(cQ\) integrable in \(L^2\).
Fubini supplies an absolutely continuous scalar representative at
almost every neuron. The scalar chain rule there gives
\[
 F(Z(t))=F(Z(0))+\int_0^t c(v)Q(v)\,dv                       \tag{I.27}
\]
with right side in \(L^2\). Thus it belongs to the transformed class
and is unique by (I.22). At every reached state the hypotheses remain
valid. Local uniqueness and concatenation prove autonomous restart
without resetting any field, readout, or operator. For antiparallel
abstract fields, their raw first derivatives sum to zero, so initial
opposition is preserved as well.

**I.2.4. Euler and raw GD.** Denote the transformed state by \(Y\) and
its physical field by \(\mathcal G\), only in this paragraph. On a
fixed horizon (I.20)--(I.25) give a bounded drift and a Lipschitz constant
\(C_T\). Therefore
\[
 \|Y(t+h)-Y(t)-h\mathcal G(Y(t))\|\le C_T h^2.               \tag{I.28}
\]
For a mesh with largest step \(h\), subtraction of updates and iteration
of \(e_{k+1}\le(1+C_T h_k)e_k+C_T h_k^2+\|d_k\|\) yields
\[
 \max_{t_k\le T+h}e_k\le e^{C_T(T+1)}
                          \left(C_T(T+1)h+\sum_k\|d_k\|\right).
 \tag{I.29}
\]
These estimates hold for untruncated iterates by the following
first-exit argument. Stop at the first residual norm exceeding
\(R_0+1\). Up to its candidate update, the discrete action is at
most \(2\sqrt2(R_0+1)(T+1)\). The explicit readout and rank updates
give (I.23) with discrete action: the half coefficient follows from
\(\sum_k\alpha_k\sum_{j<k}\alpha_j
=( (\sum\alpha_k)^2-\sum\alpha_k^2)/2\).
Hence (I.20) gives fixed constants through that candidate node. When
the right side of (I.29) is sufficiently small, (I.20) makes its residual
within \(1/2\) of the exact residual; it cannot exit. This proves
width-independent \(O_T(h)\) transformed Euler convergence, including
transformed velocities, for all sufficiently small \(h\).

At a raw node an independent first coordinate has increment
\(v=\eta c\phi'(z)q\), with \(c=-2r_a\) or \(-4r_1\).
The exact polynomial identity is
\[
 F(z+v)-F(z)=\eta cq+
       \eta^2c^2z\phi'(z)^2q^2+\tfrac13\eta^3c^3\phi'(z)^3q^3.
 \tag{I.30}
\]
There is no defect in the other two coordinates. On fixed residual,
operator, and readout bounds, \(\frac{\|q\|_{\ell^2}}{\sqrt n}\le C_T\) and
\(\|q\|_\infty\le\sqrt n C_T\). Since
\(|z|\phi'(z)^2\le1\), the defect norm is at most
\(C_T(\eta^2\sqrt n+\eta^3n)\). Its accumulated norm for
\(\eta=n^{-2}\) is \(O_T(n^{-3/2})\). The same first-exit
argument closes these bounds and, by (I.29), compares raw GD to the
finite flow with exactly the same initialization by
\[
 \sup_{t\le T}\left(\sum_a\frac{\|u^{\rm GD}_{n,a}-u^{\rm GF}_{n,a}\|_{\ell^2}}{\sqrt n}
   +\|W^{(2),\rm GD}_n-W^{(2),\rm GF}_n\|_F
   +\frac{\|W^{(3),\rm GD}_n-W^{(3),\rm GF}_n\|_{\ell^2}}{\sqrt n}\right)
                          =O_T(n^{-3/2}).                    \tag{I.31}
\]
For the raw interpolation the cubic coordinate differs from the
linear interpolation of its endpoints by
\((\theta^2-\theta)zv^2+(\theta^3-\theta)v^3/3\).
The same bound controls this term. Its derivative error is bounded
by \(C_T(\eta\sqrt n+\eta^2n)\), so transformed velocities in
(I.31) also converge at that rate.

Original first velocities use a product for which the finite estimate
\[
 \frac{\|\phi'(z)q-\phi'(\widetilde z)\widetilde q\|_{\ell^2}}{\sqrt n}
 \le\frac{\|q-\widetilde q\|_{\ell^2}}{\sqrt n}+
                      \|\widetilde q\|_\infty\frac{\|z-\widetilde z\|_{\ell^2}}{\sqrt n}
 \tag{I.32}
\]
is sufficient. It gives \(O_T(n^{-1})\), using (I.31). Apply the same
estimate to \(\dot h^{(1)}=\phi'(z^{(1)})\dot z^{(1)}\), then use
\[
 \dot z^{(2)}=\dot W^{(2)}h^{(1)}+W^{(2)}\dot h^{(1)},\qquad
 \dot h^{(2)}=\phi'(z^{(2)})\dot z^{(2)}.                    \tag{I.33}
\]
All original hidden-velocity errors are \(O_T(n^{-1})\); rank and
readout velocity errors are \(O_T(n^{-3/2})\). Their norms are uniformly
bounded. The inequality
\(|\|v\|^2-\|w\|^2|\le(\|v\|+\|w\|)\|v-w\|\) transfers these
bounds to energies. Kernels compare at \(O_T(n^{-1})\) for block 1
and \(O_T(n^{-3/2})\) for blocks 2 and 3. The exact energy identity
(I.24) is a flow identity; no exact loss identity for discrete GD is used.

These comparisons hold with probability tending to one under (I.2).
Indeed a \(1/4\)-net of the Euclidean unit sphere has at most \(9^n\)
points: disjoint balls of radius \(1/8\) around a maximal separated
set fit in the ball of radius \(9/8\). Approximating both arguments
of a bilinear form gives the norm bound twice its maximum on the net.
Each fixed bilinear form of \(W^{(2)}_n(0)\) has variance \(1/n\).
The Gaussian exponential moment and Markov's inequality give
\(\mathbb P(|N(0,1)|>u)\le2e^{-u^2/2}\). Hence
\[
 \mathbb P(\|W^{(2)}_n(0)\|_{\mathrm{op}}>t)
       \le2\exp(2n\log9-nt^2/8),                            \tag{I.34}
\]
and
\[
 \mathbb P(\|W^{(3)}_n(0)\|_\infty>1)\le2ne^{-n^2/2},\quad
 \mathbb P(\|W^{(3)}_n(0)\|_\infty>\sqrt{6\log n}/n)
                                                   \le2n^{-2}\ (n\ge2).
 \tag{I.35}
\]
In particular the events with initial bounds 8 and 1 have probability
tending to one, uniformly supplying all constants in (I.31).

### I.3. Canonical Gaussian construction and global response bounds

**I.3.1. Fixed meshes and the scalar law to be proved.** Initially use
zero finite readout as an auxiliary comparison, leaving both Gaussian
matrices and the first-row roots unchanged. Fix a finite deterministic
mesh \(0=t_0<\cdots<t_N\), with steps \(h_k=t_{k+1}-t_k\).
At each node compute (I.10), using finite normalized operations when
appropriate, put \(\gamma_{ka}=-2h_k(f_{ka}-y_a)\), and update
\[
 \begin{aligned}
 U_{k+1,a}&=U_{ka}+\sum_b G_{ab}\gamma_{kb}Q^{(1)}_{kb},\\
 W^{(2)}_{k+1}&=W^{(2)}_k+
                 \sum_b\gamma_{kb}\delta^{(2)}_{kb}\otimes H^{(1)}_{kb},\\
 W^{(3)}_{k+1}&=W^{(3)}_k+\sum_b\gamma_{kb}H^{(2)}_{kb},
 \quad U_{0a}=F(G_a),\quad W^{(3)}_0=0.
 \end{aligned}                                                   \tag{I.36}
\]
At \(G=I\) this is transformed Euler. At \(\rho=-1\) its unforced
state satisfies (I.17) by induction, so it is transformed Euler for the
reduced physical system. Away from that invariant state (I.36) will only
be an auxiliary finite program, with no claim to be the raw flow.

The following recursion specifies the limiting joint law of every
fixed such program. On population 1 take the full Gaussian first row
and a centered jointly Gaussian source family \((\zeta_{ka})\)
independent of that row. On population 2 take a centered jointly
Gaussian source family \((\xi_{ka})\). The source groups are independent;
within a group all sample and time covariances must be retained.
The scalar expressions are
\[
 \begin{aligned}
 U_{ka}&=F(G_a)+\sum_{r<k,b}G_{ab}\gamma_{rb}Q^{(1)}_{rb},
 &H^{(1)}_{ka}&=\phi(F^{-1}(U_{ka})),\\
 Z^{(2)}_{ka}&=\xi_{ka}+
                    \sum_{r<k,b}a_{ka,rb}\delta^{(2)}_{rb},
 &H^{(2)}_{ka}&=\phi(Z^{(2)}_{ka}),\\
 W^{(3)}_k&=\sum_{r<k,b}\gamma_{rb}H^{(2)}_{rb},
 &\delta^{(2)}_{ka}&=W^{(3)}_k\phi'(Z^{(2)}_{ka}),\\
 Q^{(1)}_{ka}&=\zeta_{ka}+\sum_{r\le k,b}b_{ka,rb}H^{(1)}_{rb},
 &f_{ka}&=\mathbb E_2[W^{(3)}_kH^{(2)}_{ka}].
 \end{aligned}                                                   \tag{I.37}
\]
Here the deterministic coefficients, including learned ranks, are
\[
 \begin{aligned}
 a_{ka,rb}&=\alpha_{ka,rb}+
                  \gamma_{rb}\mathbb E_1[H^{(1)}_{ka}H^{(1)}_{rb}],
 &\alpha_{ka,rb}&=\mathbb E_1[\partial_{\zeta_{rb}}H^{(1)}_{ka}],
 &&r<k,\\
 b_{ka,rb}&=\beta_{ka,rb}+\mathbf1_{r<k}\gamma_{rb}
                         \mathbb E_2[\delta^{(2)}_{ka}\delta^{(2)}_{rb}],
 &\beta_{ka,rb}&=\mathbb E_2[\partial_{\xi_{rb}}\delta^{(2)}_{ka}],
 &&r\le k.
 \end{aligned}                                                   \tag{I.38}
\]
Their source covariances are the uncentered input second moments
\[
 \mathbb E_2[\xi_{ka}\xi_{vb}]
       =\mathbb E_1[H^{(1)}_{ka}H^{(1)}_{vb}],\qquad
 \mathbb E_1[\zeta_{ka}\zeta_{vb}]
       =\mathbb E_2[\delta^{(2)}_{ka}\delta^{(2)}_{vb}].        \tag{I.39}
\]
The same rule gives cross-run covariances when different fixed meshes
or probes use the same initial matrix. Both forward answers precede
both reverse answers at a node; all updates follow them. This order
makes the recursion causal, not an implicit fixed-point prescription.

Each formal derivative differentiates the complete earlier coordinate
expression, holding all selected expectations, scalar feedback values,
response coefficients, and covariance parameters fixed. It does not
differentiate their selection. In particular
\[
 \begin{aligned}
 \partial U_{ka}&=\sum_{r<k,b}G_{ab}\gamma_{rb}\partial Q^{(1)}_{rb},\\
 \partial H^{(1)}_{ka}&=\phi'(F^{-1}(U_{ka}))^2\partial U_{ka},\\
 \partial W^{(3)}_k&=\sum_{r<k,b}\gamma_{rb}
                                \phi'(Z^{(2)}_{rb})\partial Z^{(2)}_{rb},\\
 \partial\delta^{(2)}_{ka}&=\phi'(Z^{(2)}_{ka})\partial W^{(3)}_k
                    +W^{(3)}_k\phi''(Z^{(2)}_{ka})\partial Z^{(2)}_{ka},\\
 \beta_{ka,kb}&=\mathbf1_{a=b}
                        \mathbb E_2[W^{(3)}_k\phi''(Z^{(2)}_{ka})].
 \end{aligned}                                                   \tag{I.40}
\]
The current reverse term and the past readout derivative are both
present. Formally distinct sample slots remain distinct even at
singular covariance. At zero the reverse sources have variance zero,
but their formal slots are retained.

We next prove that (I.37)--(I.39) is the full-sequence empirical law of
the finite program against every continuous polynomial-growth test,
and in every finite Wasserstein order. This proof is specialized to
the present one-matrix, arctangent model.

**I.3.2. Elementary all-order moments for a fixed program.** All constants
in this paragraph may depend on the finite number of instructions.
The readout has a deterministic coordinate bound, independent of the
root values and width, because
\[
 \|W^{(3)}_{k+1}\|_\infty
       \le(1+4B^2h_k)\|W^{(3)}_k\|_\infty+4Bh_k.             \tag{I.41}
\]
Indeed \(|f_{ka}|\le B\|W^{(3)}_k\|_\infty\), and each summand
in its update is bounded by \(2h_k B(B\|W^{(3)}_k\|_\infty+1)\).
The same bound holds after independent Gaussian query perturbations,
since \(\phi\) stays bounded. Thus the map
\(w\phi'(z)\) can, for graph estimates, be replaced by
\(\tau(w)\phi'(z)\), where a smooth bounded \(\tau\) agrees with
the identity on an interval strictly larger than this deterministic
range. This changes no program value and makes that coordinate map
globally Lipschitz. Store \((V^{(1)}(0),F(G_1),F(G_2))\) as one
iid root tuple. It has every finite moment; no derivative of the cubic
root map with respect to its underlying Gaussian is needed.

Unroll every learned operator into its initial matrix plus finitely
many ranks. The graph now uses globally Lipschitz coordinate maps,
initial matrix actions in either direction, normalized contractions,
and polynomial scalar arithmetic and scalar-times-vector operations.
Adjoin finitely many independent Gaussian roots for the regularizations
below. Conditional on all root arrays \(R\), let
\(K_R=1+\sum_j\frac{\|R_j\|_{\ell^2}}{\sqrt n}\), and write the initial matrix as
\(E/\sqrt n\), with unscaled standard Gaussian entries in \(E\).
For each vector node \(x\) and scalar node \(c\), finite induction
gives a polynomial \(P\), independent of width, such that
\[
 \begin{aligned}
 \frac{\|x\|_{\ell^2}}{\sqrt n}+|c|&\le P(K_R+\|W^{(2)}_n(0)\|_{\mathrm{op}}),\\
 \|\partial_E x[v]\|_{\ell^2}&\le
           P(K_R+\|W^{(2)}_n(0)\|_{\mathrm{op}})\|v\|_{\ell^2},\\
 |\partial_E c[v]|&\le n^{-1/2}
           P(K_R+\|W^{(2)}_n(0)\|_{\mathrm{op}})\|v\|_{\ell^2}.
 \end{aligned}                                                   \tag{I.42}
\]
Here a matrix direction is vectorized. The induction uses these exact
estimates: an initial action has differential
\(W^{(2)}_n(0)\partial x[v]+n^{-1/2}v x\), whose second term has
Euclidean norm at most \(\|v\|_F\frac{\|x\|_{\ell^2}}{\sqrt n}\). For a contraction,
\[
 |\partial[(1/n)x^Ty][v]|
 \le n^{-1/2}(\frac{\|y\|_{\ell^2}}{\sqrt n}\|\partial x[v]\|_{\ell^2}
                     +\frac{\|x\|_{\ell^2}}{\sqrt n}\|\partial y[v]\|_{\ell^2}).
\]
For a scalar-times-vector node the \(n^{-1/2}\) scalar derivative
cancels the \(\sqrt n\) in the vector norm. Lipschitz coordinate
maps and polynomial scalar operations preserve the estimates. The same
induction gives Euclidean Lipschitz dependence on stored root arrays,
with polynomial constant in their normalized norms and the matrix norm.

We use the following dimension-independent Gaussian inequality, and
include its proof. For a smooth scalar function \(X(E)\), for
\(p\ge1\) and finite right-hand side,
\[
 \mathbb E|X(E)-\mathbb E X(E)|^p
 \le(\pi/2)^p\mathbb E|N(0,1)|^p\,
                                 \mathbb E\|\nabla X(E)\|_{\ell^2}^p.
 \tag{I.43}
\]
Take an independent copy \(E'\), rotate
\(E_\theta=E\cos\theta+E'\sin\theta\), and integrate the derivative
of \(X(E_\theta)\) from 0 to \(\pi/2\). Its orthogonal velocity
\(-E\sin\theta+E'\cos\theta\) is an independent standard Gaussian.
Integral Hölder, then conditional Gaussian integration of that velocity,
bounds \(\mathbb E|X(E')-X(E)|^p\) by the right side of (I.43).
Conditional Jensen gives (I.43). Smooth approximation gives the same
bound for Lipschitz functions. Polynomial domination in the present
finite graphs justifies all integrals. Equation (I.34), integrated over
its tail, gives uniform moments of every order for the matrix norm.

To control conditional means with the non-Gaussian stored root, put
\(m_i(R)=\mathbb E_E x_i(R,E)\). Transposing two neurons \(i,j\)
of the output population and the corresponding matrix indices gives
\(m_i(R^{ij})=m_j(R)\). The root Lipschitz bound therefore gives
\[
 |m_i(R)-m_j(R)|\le P(K_R)
                  \sum_{l\text{ in this population}}|R_{li}-R_{lj}|.
\]
Also \(\frac{\|m(R)\|_{\ell^2}}{\sqrt n}\le P(K_R)\). Average over \(j\) and use
Cauchy--Schwarz to get
\[
 |m_i(R)|\le P(K_R)\left(1+\sum_l|R_{li}|\right).             \tag{I.44}
\]
If that population has no roots its conditional means are simply equal.
Apply (I.43) conditionally on \(R\), use (I.42) and (I.44), and integrate
over the roots. Jensen bounds every moment of their normalized norms
by a higher coordinate moment; Hölder handles products. Thus, for each
fixed graph and every finite \(p\),
\[
 \sup_n\mathbb E|x_i|^p<\infty,
 \qquad \sup_n\mathbb E\frac1n\sum_i|x_i|^p<\infty.          \tag{I.45}
\]
This holds for empirical-feedback graphs, their deterministic-coefficient
versions, and the auxiliary graphs with query-noise coefficient in
\([0,1]\). It concerns random program nodes, not an \(L^p\) norm of
the matrix acting on arbitrary inputs.

**I.3.3. Gaussian conditioning, projections, and source responses.** For
this paragraph only, write the initial matrix as \(W\), and collect
old forward inputs in a matrix \(V\), old reverse inputs in a matrix
\(J\), with observed answers \(WV=Y\), \(W^TJ=P\). When their
Grams are invertible, conditional on the transcript,
\[
 W\ \overset d=\ Y(V^TV)^{-1}V^T
   +J(J^TJ)^{-1}P^TP_{V^\perp}
   +P_{J^\perp}\widetilde W P_{V^\perp},                    \tag{I.46}
\]
where \(\widetilde W\) is an independent matrix with the same Gaussian
entry law. To verify this, vectorize the matrix. Orthogonal Gaussian
projection onto the linear constraint space gives its conditional mean;
the orthogonal residual is independent. The displayed mean satisfies
both constraints because \(J^TY=P^TV\), and the residual is exactly
their common null component. Adaptivity adds no further condition:
given earlier answers, a new query is already measurable, so observing
its answer adds just its linear constraint. This proves (I.46) inductively.

For a new forward input \(h\), put
\[
 \lambda_n=(V^TV)^{-1}V^Th,\quad h_\perp=h-V\lambda_n,
 \quad \nu_n=(J^TJ/n)^{-1}(P^Th_\perp/n),\quad
 \sigma_n=\frac{\|h_\perp\|_{\ell^2}}{\sqrt n}.
\]
Then its answer is conditionally
\(Y\lambda_n+J\nu_n+\sigma_nP_{J^\perp}e\), for a fresh iid
standard Gaussian \(e\). Interchanging the two populations gives the
reverse rule, with the same original matrix. If a projection \(P_0\)
has rank at most the fixed number \(j\) of previous queries, then for
\(p\ge2\)
\[
 \mathbb E[\frac1n\|\sigma_nP_0e\|_{\ell^p}^p\mid\text{transcript}]
  =\frac{\mathbb E|N|^p\sigma_n^p}{n}\sum_i(P_0)_{ii}^{p/2}
  \le\frac{j\mathbb E|N|^p\sigma_n^p}{n},
 \quad \|v\|_{\ell^p}^p=\sum_i|v_i|^p.                 \tag{I.47}
\]
This follows from \(0\le(P_0)_{ii}\le1\) and
\(\sum_i(P_0)_{ii}\le j\). Equation (I.45) and
\(\sigma_n\le\frac{\|h\|_{\ell^2}}{\sqrt n}\) make it tend to zero. For \(p<2\) use
the \(p=2\) bound and the probability-space norm inequality.

After this negligible projection is removed, the added coordinates
are independent Gaussians conditional on the transcript. If a test
has growth \(C(1+|x|^d)\), its empirical conditional variance, on an
event bounding both the regression coefficients and the innovation
standard deviation, is at most
\[
 \frac Cn\left(1+\frac1n\sum_i|\text{old tuple}_i|^{2d}\right).
 \tag{I.48}
\]
For general unbounded probe inputs the latter event can be imposed
first and then removed: \(\sigma_n\le\|h\|_{\ell^2}/\sqrt n\)
and (I.45) give tightness. Conditional Chebyshev proves concentration.
Its conditional expectation
is the old empirical average of the Gaussian-integrated test. This is
continuous in the old coordinates and coefficients and has uniform
polynomial growth on compact coefficient sets. Uniform continuity on
a ball and the estimate
\[
 \frac1n\sum_i|x_i|^d\mathbf1_{|x_i|>R}
       \le R^{d-q}\frac1n\sum_i|x_i|^q\qquad(q>d)             \tag{I.49}
\]
justify convergence of those expectations and restoration of the
projection. The root step is Chebyshev's inequality for iid tuples.
Coordinate maps preserve polynomial-growth tests. This proves empirical
induction for nonsingular limiting query Grams.

To identify the source form of this induction, let old forward inputs
be \(h_r\), reverse inputs \(v_s\), with respective Gaussian sources
\(\xi_r,\zeta_s\). The rule is
\[
 Wh=\xi_h+\sum_s v_s\mathbb E[\partial_{\zeta_s}h],\qquad
 W^Tv=\zeta_v+\sum_r h_r\mathbb E[\partial_{\xi_r}v].        \tag{I.50}
\]
The covariance of any two forward sources is the inner product of
their inputs, and the analogous statement holds for reverse sources.
Here is the calculation. Subtract the least-squares old-forward-input
projection from \(h\), obtaining \(h_\perp\). Every old reverse
answer is \(\zeta_s\) plus a linear combination of old forward inputs.
Thus its inner product with \(h_\perp\) is
\(\mathbb E[\zeta_s h_\perp]\). For a Gaussian vector of covariance
\(\Gamma\),
\[
 \mathbb E[\zeta F_0(\zeta)]=\Gamma\mathbb E[\nabla F_0(\zeta)].
 \tag{I.51}
\]
Write \(\zeta=Le\) and integrate each independent scalar Gaussian
coordinate by parts to prove (I.51); polynomial growth and bounded
derivatives make boundary terms vanish. Conditioning on independent
roots is legitimate. More explicitly, let \(\lambda_r\) be the
limiting least-squares coefficients and let
\(\Gamma_v=(\mathbb E[v_sv_{s'}])_{s,s'}\). The limiting coefficient
of the reverse-input columns in (I.46) is
\[
 \nu=\Gamma_v^{-1}\mathbb E[\zeta h_\perp]
       =\mathbb E[\nabla_\zeta h]
                   -\sum_r\lambda_r\mathbb E[\nabla_\zeta h_r].
\]
The old forward answers have decompositions
\(Wh_r=\xi_r+\sum_s v_s\mathbb E[\partial_{\zeta_s}h_r]\),
with unavailable derivatives zero. Substituting them into
\(\sum_r\lambda_rWh_r+\sum_s\nu_sv_s\) cancels the last sum
in the displayed expression for \(\nu\), giving (I.50).
The new full source is the old source
projection plus a fresh Gaussian with variance \(\mathbb E h_\perp^2\).
Consequently its full variance is \(\mathbb E h^2\), not that variance
minus a response term. The reverse proof interchanges the populations.
Every source is a deterministic linear combination of older sources
of its own group and a fresh independent Gaussian; the two source
groups remain independent of one another and of all local roots.

**I.3.4. Singular query Grams and empirical feedback.** Add \(\epsilon\)
times a fresh independent Gaussian root to the input of each initial
matrix query, revealing that root immediately before the query. Keep
the same initial matrix and leave the explicit learned rank factors
unperturbed. At fixed \(\epsilon>0\) every new limiting Gram Schur
complement is at least \(\epsilon^2\), because the fresh root is
independent of the previous same-direction input span and of the
unperturbed new input. At width larger than the number of old queries
the finite Grams are nonsingular almost surely. Thus (I.46)--(I.50) apply.

Couple the two actual finite graphs with the same matrix and roots.
Finite graph subtraction, using (I.42) and the contraction inequality
\[
 |\frac1n x^Ty-\frac1n(x')^Ty'|
 \le\frac{\|x-x'\|_{\ell^2}}{\sqrt n}\frac{\|y\|_{\ell^2}}{\sqrt n}+\frac{\|x'\|_{\ell^2}}{\sqrt n}\frac{\|y-y'\|_{\ell^2}}{\sqrt n},
 \tag{I.52}
\]
gives \(\frac{\|x_n^\epsilon-x_n^0\|_{\ell^2}}{\sqrt n}\le\epsilon P(K_n)\), where
\(K_n\) includes normalized root norms and the matrix norm and has
all finite moments. For \(p>2\), choose \(q>p\) and
\(1/p=\theta/2+(1-\theta)/q\). Hölder gives
\[
 \left(\frac{\|x_n^\epsilon-x_n^0\|_{\ell^p}}{n^{1/p}}\right)
 \le\left(\frac{\|x_n^\epsilon-x_n^0\|_{\ell^2}}{\sqrt n}\right)^\theta
                    \left(\frac{\|x_n^\epsilon-x_n^0\|_{\ell^q}}{n^{1/q}}\right)^{1-\theta}.
 \tag{I.53}
\]
Equation (I.45) bounds the second factor in probability uniformly in
width and \(\epsilon\in[0,1]\). Thus all these empirical errors tend
to zero uniformly in probability as \(\epsilon\downarrow0\). Truncation
by (I.49) transfers every continuous polynomial-growth test.

On the scalar side use (I.50), which contains no inverse covariance.
At each causal step, previously selected coefficients converge and
are bounded. Expressions have polynomial growth in the root/source
tuple, continuous dependence on coefficients, and bounded continuous
formal source derivatives on each compact coefficient set. This
follows by the chain rules (I.40): the cubic root is a stored root,
the other maps are Lipschitz with bounded derivatives, and the readout
factor has the deterministic bound (I.41). The same statements hold
for the finitely many extra Lipschitz probe instructions.

Positive semidefinite covariance square roots are continuous in fixed
dimension, including at singularity. Indeed their norms are bounded
for a convergent covariance sequence. Each subsequential limit squares
to the limiting covariance and is positive semidefinite; diagonalizing
that covariance shows its nonnegative square root is unique. Therefore
the whole sequence of square roots converges. Couple sources by those
square roots applied to a fixed standard Gaussian vector, independently
of the roots. Dominated convergence proves convergence of coordinate
moments and of the expected formal derivatives. Each next covariance
is an input Gram and remains positive semidefinite. This inductively
proves continuity of the entire finite scalar law as \(\epsilon\to0\).
The positive-noise theorem and (I.53) then prove the zero-noise theorem
by a triangle inequality, first taking width to infinity, then noise
to zero. This includes exactly zero and redundant queries.

Formal slots must not be deleted at a rank drop. If
\(\Gamma=\mathbb E[vv^T]\) and \(\lambda\in\ker\Gamma\), then
\(\sum_s\lambda_sv_s=0\) almost surely. An ambiguity in a derivative
vector in that null direction changes no contracted response in (I.50).
The explicit-expression convention fixes individual coefficients; their
use at zero covariance has just been justified by actual perturbed
finite programs, rather than an inverse-Gram assumption.

Finally, learned ranks satisfy the exact identities
\[
 \begin{aligned}
 W^{(2)}_kh&=W^{(2)}_0h+
            \sum_{r<k,b}\gamma_{rb}\delta^{(2)}_{rb}
                                          \mathbb E_1[H^{(1)}_{rb}h],\\
 W^{(2)*}_kv&=W^{(2)*}_0v+
            \sum_{r<k,b}\gamma_{rb}H^{(1)}_{rb}
                                          \mathbb E_2[\delta^{(2)}_{rb}v].
 \end{aligned}                                                   \tag{I.54}
\]
Select every scalar contraction in causal order by its expectation
under the already constructed scalar law. This defines a deterministic
coefficient program. Its empirical contractions converge by the preceding
proof. Couple it with the actual feedback program. On bounded \(K_n\),
(I.52), the Lipschitz coordinate inequalities and the matrix norm bound
show by finite induction that every RMS discrepancy is bounded by a
constant times the sum of the finitely many contraction errors. These
vanish in probability. Increase the bound on \(K_n\); its complement
has arbitrarily small probability by the moment bounds. Apply (I.45),
(I.49), and (I.53) to upgrade from RMS to all polynomial-growth tests.
Substituting (I.50) into (I.54) gives precisely (I.37)--(I.39), with all learned
terms in (I.38). This proves actual-feedback identification.

For completeness it also proves Wasserstein convergence. Truncate
to a large ball, partition that ball into finitely many cells of small
diameter and zero limiting boundary mass, and approximate cell
indicators by continuous functions. Their empirical masses converge.
Match common mass inside each cell and couple the unmatched bounded
mass arbitrarily. Coupling tail mass through the origin bounds the
remaining cost by a constant times the two \(p\)-tails, which vanish
by (I.49) with \(q>p\). Sending width, cell diameter, and tail cutoff
to their respective limits proves the stated convergence in probability.

**I.3.5. One common space and an actual bounded adjoint.** Enumerate a
countable family of finite programs, all using the same initial matrix
and roots. Include dyadic meshes on all integer horizons, intermediate
fields, both initial-matrix orientations applied to every generated
node, rational linear combinations, constants, and a countable dense
family of bounded smooth cylinder functions. Include any fixed countable
collection of requested independent probe roots. Close this list in
stages; every instruction has finitely many parents, and every finite
initial sublist is covered by the finite-program proof. A Gaussian source
itself can be included by subtracting its selected response from its
matrix answer.

Construct sources in this order. Their covariances with earlier sources
are input Grams. Subtract the projection onto the earlier Gaussian span
and use a fresh independent standard Gaussian for the nonnegative
residual variance. At zero variance retain the formal slot without a
new random draw. Countably many independent Gaussian variables and
roots can be realized on a probability space explicitly: split the
independent binary digits of a uniform point of \((0,1)\) into countably
many infinite subsequences to obtain independent uniforms, then use
their quantile maps. Finite binary cylinder probabilities verify this
construction; binary ambiguities form a null set. Use separate spaces
for the first roots/reverse sources and the second roots/forward sources.

For a queried input \(h\), let its limiting initial forward answer be
\(a(h)\); for a reverse input \(v\), let its initial reverse answer be
\(b(v)\), only in this construction. Every finite rational combination
satisfies
\[
 \left\|\sum_i t_i a(h_i)\right\|_2
       \le8\left\|\sum_i t_i h_i\right\|_2,
 \quad
 \left\|\sum_j s_j b(v_j)\right\|_2
       \le8\left\|\sum_j s_j v_j\right\|_2,
 \quad
 \mathbb E_2[a(h)v]=\mathbb E_1[hb(v)].            \tag{I.55}
\]
The finite identities hold exactly and the inequalities hold on the
event \(\|W^{(2)}_n(0)\|\le8\), whose probability tends to one by
(I.34). All involved Gram entries converge to deterministic quantities.
A strict violation of (I.55) would contradict these two facts. Approximate
real coefficients by rationals. In particular a zero-norm relation
among inputs gives a zero-norm relation among answers, so the proposed
linear actions are well defined.

The queried-input spans are dense in the two generated \(L^2\) spaces.
To check this without an implicit density assumption, events approximable
in measure by finite-cylinder events form a class closed under complements
and countable unions: first approximate a finite union, then use
continuity of probability for its increasing limit. They therefore
include the sigma field generated by the countable tuple. Rational
threshold rectangles generate the finite-dimensional Borel sets.
One-sided smooth threshold approximations converge to their indicators,
even when a coordinate has an atom. Products of these approximations
are bounded smooth cylinder functions in the closure of the chosen
countable family. Truncating and approximating simple functions proves
density in \(L^2\).

Extend both linear maps by (I.55) to their completions. The last identity
in (I.55), passed to the completions, says that the reverse extension is
exactly the adjoint of the forward extension. Call the forward operator
\(W^{(2)}(0)\). It is bounded by 8 and uniquely specified on these
generated spaces. Adding an unused query changes no earlier marginal:
both constructions give the full-sequence empirical limit of that
same finite marginal. Therefore different enumerations give the same
joint laws, with measure-preserving identifications on the generated
function spaces and the corresponding isometries of \(L^2\).
This is the required canonicity. It does not identify a Gaussian matrix
with an iid continuum kernel or with an operator bounded on every
\(L^p\).

Apply Section I.2 on these spaces with \(U_{0a}=F(G_a)\) and zero
readout. This gives a single global autonomous flow. Each of the
constructed finite-mesh scalar programs satisfies its Euler equations
on these same spaces, with this same operator and adjoint, by (I.54)--(I.55).
Consequently, for largest mesh step \(h\),
\[
 \sup_{t\le T}\left(\sum_a\|U_a^h(t)-U_a(t)\|_2
       +\|W^{(2),h}(t)-W^{(2)}(t)\|_{\mathrm{HS}}
       +\|W^{(3),h}(t)-W^{(3)}(t)\|_2\right)\le C_T h.
 \tag{I.56}
\]
Any further fixed mesh can be adjoined to the countable family and
obeys the same bound. The flow is not defined by selecting a width
subsequence, nor by restarting a fresh operator at each mesh.

**I.3.6. Global expected-response bounds by actual fresh-root forcing.**
This step is needed for the all-time nontriviality assertions; primal
\(L^2\) bounds alone do not imply it. Fix \(T\), and consider every
finite partition through \(T\) with largest step at most 1. Equation
(I.41) gives the deterministic bound
\[
 \|W^{(3)}_k\|_\infty\le M_T
       :=B^{-1}(e^{4B^2(T+1)}-1).
 \tag{I.57}
\]
Thus \(|\gamma_{ka}|\le2h_k(BM_T+1)\) and the total absolute
sum of the \(\gamma\)'s is at most
\(4(T+1)(BM_T+1)\). On the event \(\|W^{(2)}_n(0)\|\le8\),
the rank updates bound all operator norms by a deterministic constant
depending only on \(T\). These bounds also hold for the forced programs
below. Subtraction of one step of (I.36), using (I.20) and (I.52), gives a
state Lipschitz factor \(1+C_T h_k\) in (I.19). For this auxiliary
comparison use the sum over both first-sample coordinates in that norm.
It includes the changes
in residuals and in every rank update. With both sample coordinates
retained it also holds off the antiparallel invariant state, because
\(\|G\|\le2\) and the transformed update is linear in the backward
answers. This auxiliary off-invariant program need not be raw GF.

First add \(\epsilon e\), with a fresh iid \(N(0,1)\) root array
on population 1, to the complete reverse answer \(q^{(1)}_{n,sb}\)
at one node, before its descendants are computed. Keep every matrix
entry and all earlier answers fixed. Only the first state update changes
immediately, by RMS at most \(C_T h_s|\epsilon|\frac{\|e\|_{\ell^2}}{\sqrt n}\).
Multiplying the later factors \(1+C_T h_k\) gives, for \(k>s\),
\[
 \frac{\|h^{(1),\epsilon}_{n,ka}-h^{(1),0}_{n,ka}\|_{\ell^2}}{\sqrt n}
                 \le C_T h_s|\epsilon|\frac{\|e\|_{\ell^2}}{\sqrt n}.              \tag{I.58}
\]
Next perform instead the analogous insertion into the complete forward
answer \(z^{(2)}_{n,sb}\), using a fresh population-2 root. Its
immediate changes in activations, deltas, predictions, and residuals
are at most \(C_T|\epsilon|\frac{\|e\|_{\ell^2}}{\sqrt n}\). The actual transpose bounds
the immediate reverse-answer changes by the same quantity. Every
state update has its factor \(h_s\), so at later nodes
\[
 \frac{\|\delta^{(2),\epsilon}_{n,ka}-\delta^{(2),0}_{n,ka}\|_{\ell^2}}{\sqrt n}
                 \le C_T h_s|\epsilon|\frac{\|e\|_{\ell^2}}{\sqrt n}\qquad(k>s).
 \tag{I.59}
\]
At the current node the delta change is at most
\(M_T|\epsilon|\frac{\|e\|_{\ell^2}}{\sqrt n}\), and other current sample deltas have
no direct change. These are finite-width estimates for the actual
empirical-feedback programs, not estimates for arbitrarily extended
functions off a Gaussian support.

We now extract the coefficient with the order of limits specified
explicitly. Fix the mesh and a nonzero \(\epsilon\). Apply the proved
finite-program theorem jointly to the forced and unforced runs and
the new root \(e\), taking \(n\to\infty\) first. In its own population
the new root occurs in the scalar expression only through replacement
of the designated source slot by \(\zeta_{sb}+\epsilon e\), or
\(\xi_{sb}+\epsilon e\), respectively. The construction in (I.50)
makes all Gaussian source groups independent of the local root \(e\).
Their covariances and the selected response and feedback coefficients
may depend on \(\epsilon\), but are deterministic and constant as
functions of that local coordinate. Induction through the complete
coordinate expression therefore gives, with these selected quantities
held fixed,
\[
 \partial_e X^\epsilon
          =\epsilon\partial_{\mathrm{slot}}X^\epsilon,
 \qquad
 \mathbb E[eX^\epsilon]
          =\epsilon\mathbb E[\partial_{\mathrm{slot}}X^\epsilon].
 \tag{I.60}
\]
The second equality is one-dimensional Gaussian integration by parts
in the fresh root. It remains valid if the old source covariance is
singular. The unused root is independent of the unforced expression,
so \(\mathbb E[eX^0]=0\). Passing the finite Cauchy--Schwarz inequality
\(|\frac1n e^T(X_n^\epsilon-X_n^0)|
\le\frac{\|e\|_{\ell^2}}{\sqrt n}\frac{\|X_n^\epsilon-X_n^0\|_{\ell^2}}{\sqrt n}\) to the joint limit in
(I.58)--(I.59), and using \(\mathbb E e^2=1\), bounds (I.60) divided by
\(|\epsilon|\) by \(C_T h_s\). Only now let \(\epsilon\to0\).
The fixed-mesh coefficient and formal-derivative continuity proved in
3.4 identifies the limit with exactly (I.38), including initial slots
of variance zero. We have proved
\[
 |\alpha_{ka,sb}|\le C_T h_s\ (s<k),\qquad
 |\beta_{ka,sb}|\le C_T h_s\ (s<k),\qquad
 |\beta_{ka,kb}|\le M_T\mathbf1_{a=b}.                       \tag{I.61}
\]
In particular no derivative transverse to the support of an unforced
singular Gaussian law was inferred from that law. The order was fixed
mesh, nonzero forcing, width limit, integration by parts in the fresh
independent root, and finally forcing tending to zero. Feedback was
included in the finite estimates (I.58)--(I.59); selected scalar values
were correctly held fixed only in the local derivative (I.60).

Adding the learned terms in (I.38) now gives
\[
 |a_{ka,sb}|+|b_{ka,sb}|\le C_T h_s\ (s<k),\qquad
 |b_{ka,kb}|\le M_T\mathbf1_{a=b}.                           \tag{I.62}
\]
Thus the absolute sums of all complete past and current response rows
are bounded on every finite horizon, uniformly in the number of mesh
queries. No local-in-time response bootstrap is being extended without
an estimate.

**I.3.7. Bounded Gaussian remainders at every finite time.** From (I.37),
(I.39), (I.57), and (I.62), all mesh fields have decompositions
\[
 Z^{(2)}_{ka}=\xi_{ka}+S_{ka},\qquad
 Q^{(1)}_{ka}=\zeta_{ka}+R_{ka},\qquad
 |S_{ka}|+|R_{ka}|\le C_T.                                  \tag{I.63}
\]
Their Gaussian variances are exactly
\(\|H^{(1)}_{ka}\|_2^2\) and \(\|\delta^{(2)}_{ka}\|_2^2\).
Consequently
\[
 U_{ka}=F(G_a)+\sum_{r<k,b}G_{ab}\gamma_{rb}\zeta_{rb}
                                      +E_{ka},\qquad |E_{ka}|\le C_T.
 \tag{I.64}
\]
The Gaussian sum is independent of the first-row roots, with variance
at most \(C_T\); no independence from its bounded remainder is claimed.
The inverse Lipschitz bound gives
\(|F^{-1}(U_{ka})|\le|G_a|+|\sum G\gamma\zeta|+C_T\).
Thus the first and second preactivations and \(Q^{(1)}\) have uniform
Gaussian upper-tail bounds, and \(U\) has all moments with a
cubic-Gaussian bound.

These decompositions pass to the already constructed common-space
flow, not just to subsequential marginal laws. From the cross-program
version of (I.39), the source assignments are Gaussian isometries:
\[
 \|\xi_h-\xi_{h'}\|_2=\|h-h'\|_2,
 \qquad \|\zeta_v-\zeta_{v'}\|_2=\|v-v'\|_2.               \tag{I.65}
\]
They extend by completion on the closed input spans. Equation (I.56)
and (I.20) give uniform-in-time \(L^2\) convergence of their inputs,
so their sources converge too. Subtract from the convergent fields in
(I.63). An \(L^2\) limit of variables bounded by \(C_T\) is bounded
by \(C_T\): choose a subsequence with summable squared errors and
use Markov's inequality to obtain almost-everywhere convergence.
Riemann sums in (I.64) converge in \(L^2\). Limits of jointly Gaussian
linear combinations remain Gaussian because variances and characteristic
functions converge; independence from the root persists by factorization
of joint characteristic functions. We obtain, for every \(t\le T\),
\[
 \begin{aligned}
 Z^{(2)}_a(t)&=\xi_a(t)+S_a(t),& |S_a(t)|&\le C_T,\\
 Q^{(1)}_a(t)&=\zeta_a(t)+R_a(t),& |R_a(t)|&\le C_T,\\
 \mathbb E_2[\xi_a(t)\xi_b(v)]
       &=\mathbb E_1[H^{(1)}_a(t)H^{(1)}_b(v)],&&\\
 \mathbb E_1[\zeta_a(t)\zeta_b(v)]
       &=\mathbb E_2[\delta^{(2)}_a(t)\delta^{(2)}_b(v)],&&\\
 U_a(t)&=F(G_a)+\sum_b G_{ab}\int_0^t c_b(v)\zeta_b(v)\,dv+E_a(t),
 &|E_a(t)|&\le C_T,
 \quad c_b=-2r_b.
 \end{aligned}                                                   \tag{I.66}
\]
The representations hold almost surely at each deterministic finite
time. Jointly measurable versions give the product-almost-everywhere
identities used for time integration; no common exceptional-set claim
stronger than these laws and integral statements is needed here.
The sources are centered Gaussian processes with their full time and
sample covariances, and \(\zeta\) is independent of the whole first
row. Their \(L^2\) continuity makes the displayed Gaussian integrals
well defined. Essential remainder bounds are uniform over each fixed horizon,
with a constant depending on that horizon;
joint measurable representatives follow from \(L^2\)-continuous
approximations, and Fubini suffices for the time integrals. These are
the global representation properties used below, now proved rather
than imposed as hypotheses.



# Frozen source: docs/special_data_limits.md lines 3785–4326

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



# Frozen source: docs/finite_dynamics.md lines 1–227

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



# Frozen source: docs/finite_optimization_and_controls.md lines 1–345

# Finite optimization and energy-compatible controls

This chapter proves finite-width optimization for the canonical three-hidden-layer
arctangent network: global gradient-flow coercivity and fitting, exact raw-GD
coercivity and fitting at step \(\eta_n=n^{-2}\), and convergence of every
parameter to a finite interpolating endpoint. It also proves a global
finite-dimensional theorem for an auxiliary metric projection, its integrated
\(L^1\) equation defect, and eventual exact agreement with the canonical flow
at each fixed width. All proof ingredients and Gaussian initial conditions are
given below.

Sections 10–11 add a different, two-hidden-layer mixed-activation model at
every fixed interior correlation with opposite labels. They prove actual
finite-GF fitting and finite parameter limits, with explicit initialization
events and width-independent bounds on those events. A separately augmented
event gives permanent positive first-gate mass. These are not population/GD
results, and gate mass is not a certificate of nonzero feature velocity.

The conventions agree with [NOTATION.md](NOTATION.md), the general identities
in [finite_dynamics.md](finite_dynamics.md), and the
[three-hidden-layer arctangent model](arctan_limits.md#l3-local).
Sections 1–11 concern finite widths. Section 12 separately proves global
dissipative capped flows on prescribed Hilbert spaces and continuation under
an explicit exponential-tail premise. It assumes a bounded initial middle
operator on those spaces; it does not construct canonical Gaussian actions.
Section 13 returns to the finite L3 arctangent model, retaining exact trained
memories and proving time covers for four integrated initial-matrix queries
along a supplied path. It leaves causal approximation, nonlinear stability
and derivative/kernel convergence as separate requirements.
Section 14 derives the full finite tangent geometry: polynomial nuclear-norm
and intrinsic-volume bounds, their Gaussian expectations, an exact hidden
projection factor, and a deterministic reachable signed-Hessian obstruction.
The projection factor and Gaussian-typical signed control remain separate.
None of these control results asserts a global uncut three-layer population
flow or a population/GD limit for the finite metric projection. No width
limit is interchanged with infinite training time.

## 1. Canonical model, metric, and clocks

Fix a positive integer \(n\), one input \(x=1\), and one target \(y=1\).
Thus \(L=3\) and \(m=d=1\). Put \(c=\pi/2\) and
\(\phi(z)=\arctan z\). Coordinatewise,
\[
 |\phi|\le c,\qquad \phi(0)=0,\qquad
 \phi'(z)=\frac1{1+z^2},\qquad |\phi'|\le1,\qquad |\phi''|\le2.
 \tag{1.1}
\]
The raw state is
\(\theta=(z^{(1)},W^{(2)},W^{(3)},W^{(4)})\), where
\(z^{(1)}=W^{(1)}\) and the stored readout \(W^{(4)}\) are in
\(\mathbb R^n\), and the two middle matrices are in
\(\mathbb R^{n\times n}\). Define
\[
 h^{(1)}=\phi(z^{(1)}),\quad z^{(2)}=W^{(2)}h^{(1)},\quad
 h^{(2)}=\phi(z^{(2)}),\quad z^{(3)}=W^{(3)}h^{(2)},\quad
 h^{(3)}=\phi(z^{(3)}),
\]
\[
 f_n=\frac{(W^{(4)})^Th^{(3)}}n,\qquad
 r_n=f_n-1,\qquad \mathcal L_n=r_n^2.
 \tag{1.2}
\]
At a fixed width write \(f=f_n\), \(r=r_n\). The norm \(\|\cdot\|_2\) is the
ordinary Euclidean norm and \(\|v\|_\infty=\max_i|v_i|\). Matrix norms are
explicitly operator or Frobenius norms, and every factor \(1/n\) or
\(1/\sqrt n\) is displayed. For the diagonal
matrices \(D_\ell=\operatorname{diag}(\phi'(z^{(\ell)}))\), let
\[
 \delta^{(3)}=D_3W^{(4)},\qquad q^{(2)}=(W^{(3)})^T\delta^{(3)},\qquad
 \delta^{(2)}=D_2q^{(2)},\qquad
 \delta^{(1)}=D_1(W^{(2)})^T\delta^{(2)}.
 \tag{1.3}
\]
These are derivatives of the prediction:
\(\delta^{(\ell)}=n\,\partial f/\partial z^{(\ell)}\). They contain no
residual. In fact the chain rule, applied from the readout downwards, gives
\[
 df=\frac{(\delta^{(1)})^Tdz^{(1)}}n
    +\sum_{\ell=2}^3\frac{(\delta^{(\ell)})^T(dW^{(\ell)})h^{(\ell-1)}}n
    +\frac{(h^{(3)})^TdW^{(4)}}n.
\]
The block mobilities are \(n,1,1,n\), with all fixed
\(\kappa_\ell=1\); their parameter quadratic form is
\[
 \frac{\|dz^{(1)}\|_2^2}{n}
 +\|dW^{(2)}\|_{\rm F}^2+\|dW^{(3)}\|_{\rm F}^2
 +\frac{\|dW^{(4)}\|_2^2}{n}.
 \tag{1.4}
\]
Define the feature vector field
\[
 \mathcal G(\theta)=\left(
 \delta^{(1)},\ \frac{\delta^{(2)}(h^{(1)})^T}{n},\
 \frac{\delta^{(3)}(h^{(2)})^T}{n},\ h^{(3)}\right).
 \tag{1.5}
\]
The canonical physical gradient flow and exact simultaneous raw GD are
\[
 \frac{d\theta}{dt}=-2r\,\mathcal G(\theta),\qquad
 \theta_{k+1}=\theta_k-2\eta_n r_k\mathcal G(\theta_k),
 \qquad \eta_n=n^{-2},\quad t_k=k\eta_n.
 \tag{1.6}
\]
Every block on the right is evaluated before the update. Between GD nodes the
raw parameters are linearly interpolated and the hidden quantities recomputed.
The GD fitting inequalities proved below apply at the nodes.

Feature time \(s\) solves \(d\theta/ds=\mathcal G(\theta)\). Its relation
to physical gradient flow is \(ds/dt=2(1-f)=-2r\) while this is positive;
positivity will be proved. For GD, \(\alpha_k=2\eta_n(1-f_k)\) and
\(s_k=\sum_{j<k}\alpha_j\) are computational clock variables. They neither
change the raw update nor discretize a transformed coordinate. In particular,
the continuous identity for \(F(z)=z+z^3/3\) is not used as an exact GD rule.

## 2. Global feature flow and readout acceleration

**Lemma 2.1 (finite feature existence and exact action).** For every finite
initial state, (1.5) has a unique solution for all \(s\ge0\). Define
\[
 \mathsf A_2=\frac{\|h^{(1)}\|_2^2}{n}I+W^{(2)}D_1^2(W^{(2)})^T,
\]
\[
 \mathsf A_3=\frac{\|h^{(2)}\|_2^2}{n}I
       +W^{(3)}D_2\mathsf A_2D_2(W^{(3)})^T,
 \qquad P=D_3\mathsf A_3D_3.
 \tag{2.1}
\]
All three matrices are positive semidefinite. A prime on a state variable in
this section denotes \(d/ds\). Then
\[
 (z^{(2)})'=\mathsf A_2\delta^{(2)},\qquad
 (z^{(3)})'=\mathsf A_3\delta^{(3)},\qquad
 (W^{(4)})''=(h^{(3)})'=PW^{(4)},
 \tag{2.2}
\]
and the exact scalar kernel is
\[
 \begin{aligned}
 K_n=f'&=\frac{\|h^{(3)}\|_2^2}{n}+
                \frac{(W^{(4)})^TPW^{(4)}}{n}\\
 &=\frac{\|h^{(3)}\|_2^2}{n}
  +\frac{\|\delta^{(3)}\|_2^2\|h^{(2)}\|_2^2}{n^2}
  +\frac{\|\delta^{(2)}\|_2^2\|h^{(1)}\|_2^2}{n^2}
  +\frac{\|\delta^{(1)}\|_2^2}{n}\\
 &=\frac{\|(z^{(1)})'\|_2^2}{n}
   +\|(W^{(2)})'\|_{\rm F}^2+\|(W^{(3)})'\|_{\rm F}^2
   +\frac{\|(W^{(4)})'\|_2^2}{n}.
 \end{aligned}
 \tag{2.3}
\]

**Proof.** The raw vector field is smooth. On a sufficiently small closed ball,
its integral map on continuous paths is a contraction when the time interval
is smaller than the reciprocal of its Lipschitz constant and its bounded
speed keeps paths in the ball. This proves local existence and uniqueness.
To exclude finite escape, set
\(\varepsilon=\|W^{(4)}(0)\|_2/\sqrt n\) and
\(M_j=\|W^{(j)}(0)\|_{\rm op}\), \(j=2,3\). Successive integration of
(1.5), using \(\|uv^T/n\|_{\rm F}=\|u\|_2\|v\|_2/n\), gives
\[
 \frac{\|W^{(4)}(s)\|_2}{\sqrt n}\le\varepsilon+cs,
 \qquad
 \|W^{(3)}(s)\|_{\rm op}
 \le M_3+c\varepsilon s+\frac{c^2s^2}{2}=:\mathcal M_3(s),
\]
\[
 \|W^{(2)}(s)\|_{\rm op}
 \le M_2+c\int_0^s\mathcal M_3(u)(\varepsilon+cu)\,du
 =:\mathcal M_2(s),
\]
\[
 \frac{\|z^{(1)}(s)-z^{(1)}(0)\|_2}{\sqrt n}
 \le\int_0^s\mathcal M_2(u)\mathcal M_3(u)(\varepsilon+cu)\,du.
 \tag{2.4}
\]
The matrix increment bounds also hold in Frobenius norm. These are finite
polynomials on bounded intervals. At fixed \(n\), they bound all raw
parameters in a compact set; the smooth field is bounded there, so a solution
has a finite limit at a proposed finite endpoint. The local construction
extends it, proving global existence.

Differentiating \(h^{(1)}\) gives
\((h^{(1)})'=D_1^2(W^{(2)})^T\delta^{(2)}\). The two terms in the
product derivative of \(W^{(2)}h^{(1)}\) give \(\mathsf A_2\delta^{(2)}\).
Differentiating \(W^{(3)}h^{(2)}\), and then applying \(D_3\), gives (2.2).
Matrices of the form \(BB^T\), nonnegative scalar multiples of the identity,
and congruences of positive semidefinite matrices are positive semidefinite;
this verifies the positivity in (2.1). Differentiating (1.2) using (2.2)
proves the first line of (2.3). Expanding (2.1) gives its four kernel blocks.
The rank-one Frobenius identity above gives its squared-speed expression. ∎

In particular, wherever \(g(s)=\|W^{(4)}(s)\|_2/\sqrt n>0\),
\[
 g'=\frac f g,\qquad
 g''=\frac{\|h^{(3)}\|_2^2/n-(g')^2+(W^{(4)})^TPW^{(4)}/n}{g}\ge0.
 \tag{2.5}
\]
The first two numerator terms have nonnegative sum by Cauchy–Schwarz, and
the last is nonnegative by (2.1). This is convexity of the readout norm on
its nonzero intervals, with no assertion about individual coordinate signs.

## 3. Canonical gradient-flow coercivity, fitting, and endpoints

**Theorem 3.1 (zero and small stored readout).** There are two deterministic
initialization cases.

For zero readout \(W^{(4)}(0)=0\), assume
\(\mu=\|h^{(3)}(0)\|_2^2/n>0\). Then for all feature times,
\[
 \frac{\|W^{(4)}(s)\|_2}{\sqrt n}\ge s\sqrt\mu,
 \quad \frac{\|h^{(3)}(s)\|_2^2}{n}\ge\mu,
 \quad f(s)\ge\mu s,\quad K_n(s)\ge\mu.
 \tag{3.1}
\]

For nonzero readout fix \(0<b\le c\) and \(M_2,M_3\ge0\), and assume
\(\|h^{(3)}(0)\|_2/\sqrt n\ge b\) and
\(\|W^{(j)}(0)\|_{\rm op}\le M_j\) for \(j=2,3\). Define
\[
 L_3=M_3+c+c^2/2,\qquad L_2=M_2+cL_3(1+c/2),
 \qquad B=c^2+L_3^2(c^2+L_2^2),
\]
\[
 \sigma=\min\{1,\sqrt{b/(8cB)}\},\qquad
 \varepsilon_{\rm GF}=\min\{1,b\sigma/16\}.
 \tag{3.2}
\]
If \(\varepsilon=\|W^{(4)}(0)\|_2/\sqrt n\le\varepsilon_{\rm GF}\), then
\[
 \frac{\|h^{(3)}(s)\|_2^2}{n}\ge\mu:=b^2/4,
 \qquad K_n(s)\ge\mu\qquad(s\ge0).
 \tag{3.3}
\]
No coordinatewise initial readout bound is required.

In either case put \(f_0=f(0)\), \(e_0=1-f_0>0\). There is a unique
feature time \(s_*\in(0,e_0/\mu]\) with \(f(s_*)=1\). Physical gradient
flow exists for every \(t\ge0\), has \(s(t)\uparrow s_*\), and satisfies
\[
 0<e(t):=1-f(s(t))\le e_0e^{-2\mu t},\qquad
 \mathcal L_n(t)\le e_0^2e^{-4\mu t},
\]
\[
 s(t)\le\frac{e_0}{\mu}(1-e^{-2\mu t}),\qquad
 s_*-s(t)\le\frac{e(t)}\mu.
 \tag{3.4}
\]
There is a finite endpoint \(\theta_\infty=\theta(s_*)\) with prediction one,
and the following estimates display all four parameter blocks:
\[
 \begin{aligned}
 &\frac{\|z^{(1)}(s(t))-z^{(1)}(0)\|_2^2}{n}
  +\sum_{\ell=2}^3\|W^{(\ell)}(s(t))-W^{(\ell)}(0)\|_{\rm F}^2
  +\frac{\|W^{(4)}(s(t))-W^{(4)}(0)\|_2^2}{n}
  \le\frac{e_0^2}{\mu},\\
 &\left[\frac{\|z^{(1)}(s(t))-z^{(1)}_\infty\|_2^2}{n}
  +\sum_{\ell=2}^3\|W^{(\ell)}(s(t))-W^{(\ell)}_\infty\|_{\rm F}^2
  +\frac{\|W^{(4)}(s(t))-W^{(4)}_\infty\|_2^2}{n}\right]^{1/2}
  \le\frac{e(t)}{\sqrt\mu}.
 \end{aligned}
 \tag{3.5}
\]

**Proof.** In the zero-readout case, smoothness gives
\(W^{(4)}(s)=s h^{(3)}(0)+o(s)\) and \(g'(0+)=\sqrt\mu\).
Convexity (2.5) implies \(g'\ge\sqrt\mu\), \(g\ge s\sqrt\mu\) up to
any first later zero of \(g\); the latter bound excludes such a zero.
Now \(\|h^{(3)}\|_2/\sqrt n\ge g'\), \(f=gg'\), and (2.3) give (3.1).
If the excluded initial \(\mu\) is zero, all four velocities vanish and
the unique solution is stationary.

For small readout, (2.4) bounds the two matrix norms on \([0,1]\) by
\(L_2,L_3\), and (2.1) gives \(\|P\|_{\rm op}\le B\). Integrating
\((h^{(3)})'=PW^{(4)}\) once and twice yields
\[
 \frac{\|h^{(3)}(s)-h^{(3)}(0)\|_2}{\sqrt n}
 \le B(\varepsilon s+cs^2/2),
\]
\[
 \frac{\|W^{(4)}(s)-W^{(4)}(0)-s h^{(3)}(0)\|_2}{\sqrt n}
 \le B(\varepsilon s^2/2+cs^3/6).
 \tag{3.6}
\]
Since \(\varepsilon\le b\sigma/16\le c\sigma\) and
\(Bc\sigma^2\le b/8\), the first bound is at most \(3b/16\) for
\(s\le\sigma\). The second, including the initial readout, gives
\[
 \frac{\|W^{(4)}(\sigma)-\sigma h^{(3)}(0)\|_2}{\sigma\sqrt n}
 \le b/16+b/12=7b/48.
 \tag{3.7}
\]
In particular \(W^{(4)}(\sigma)\ne0\). For any nonzero Euclidean vector
\(x\), Cauchy–Schwarz and the triangle inequality give
\(x^Ty/\|x\|_2\ge\|y\|_2-2\|x-y\|_2\). Apply this with
\(x=W^{(4)}(\sigma)/(\sigma\sqrt n)\),
\(y=h^{(3)}(0)/\sqrt n\), and then use (3.6) for the feature change:
\[
 g'(\sigma)\ge b-2(7b/48)-3b/16=25b/48>b/2.
 \tag{3.8}
\]
Convexity (2.5) preserves this lower bound for later times and prevents a
later zero of \(g\). The initial feature estimate and
\(\|h^{(3)}\|_2/\sqrt n\ge g'\) prove (3.3).

In the small-readout case \(|f_0|\le c\varepsilon\le c^2/16<1\);
in the zero-readout case \(f_0=0\). The bound \(f'\ge\mu\) and continuity
give the unique \(s_*\), with \(s_*\le e_0/\mu\). The scalar equation
\(\dot s=2(1-f(s))\), \(s(0)=0\), has a locally Lipschitz right-hand
side. It is positive before \(s_*\). Uniqueness prevents reaching the
constant solution \(s=s_*\) in finite time. Its bounded state gives global
continuation; a limit below \(s_*\) would have positive clock speed and is
impossible. Differentiation gives \(\dot e=-2K_n(s(t))e\), hence (3.4)
by integration. The last bound in (3.4) also follows directly from
\(e(t)=\int_{s(t)}^{s_*}K_n(u)\,du\).

Integrating (2.3) shows that feature action between any \(s_1<s_2\) equals
\(f(s_2)-f(s_1)\). Cauchy–Schwarz applied jointly to the four weighted
parameter derivatives bounds the corresponding squared displacement by
\((s_2-s_1)[f(s_2)-f(s_1)]\). Take first \(s_1=0,s_2=s(t)\), and then
\(s_1=s(t),s_2=s_*\), to get (3.5). In fact the remaining path length,
computed by integrating the square root of the last line of (2.3), is at most
\(\sqrt{(s_*-s(t))e(t)}\le e(t)/\sqrt\mu\). The initial state determines
this endpoint; uniqueness among all interpolating network states is not
asserted. Finally \(|W_i^{(4)}(s(t))-W_i^{(4)}(0)|\le cs(t)\le ce_0/\mu\).
∎

**Corollary 3.2 (lower-layer moments and backward energy).** Let positive
\(\widehat M_2,\widehat M_3\) bound the matrix operator norms on this
physical trajectory, for instance
\(\widehat M_j=1+M_j+e_0/\sqrt\mu\). Then
\[
 \frac{\|h^{(2)}\|_2^2}{n}\ge\frac\mu{\widehat M_3^2},\qquad
 \frac{\|h^{(1)}\|_2^2}{n}
 \ge\frac\mu{\widehat M_2^2\widehat M_3^2},\qquad
 \int_0^{s_*}\frac{\|q^{(2)}(s)\|_2^2}{n}\,ds
 \le\frac{\widehat M_3^4e_0}{\mu}.
 \tag{3.9}
\]
Indeed \(|\phi(z)|\le|z|\) propagates the top feature lower bound through
the two forward matrices. The third-layer matrix kernel block in (2.3)
is at least \(\mu\|\delta^{(3)}\|_2^2/(n\widehat M_3^2)\); its integral
is at most the total action \(e_0\). Use
\(\|q^{(2)}\|_2\le\widehat M_3\|\delta^{(3)}\|_2\) to obtain (3.9).
These are second moments, not empirical variances or coordinate tail bounds.



# Frozen source: docs/global_nonlinear.md lines 2923–3439

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

