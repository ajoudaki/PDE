# Frozen established dependencies from docs/global_nonlinear.md

Source SHA-256: `7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465`.
Only the exact complete sections listed below are included.

<!-- SOURCE docs/global_nonlinear.md:1840-1898; A.1-A.4, complete -->

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



<!-- SOURCE docs/global_nonlinear.md:1903-2274; B.1 complete GF construction; GD bridge excluded -->

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


<!-- SOURCE docs/global_nonlinear.md:3982-4207; C.4.1 complete full-row transport -->

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


<!-- SOURCE docs/global_nonlinear.md:5475-5782; C.4.5.1 sections 1-3, complete reference endpoint -->

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


<!-- SOURCE docs/global_nonlinear.md:5999-6595; C.4.5.1 section 5 and complete C.4.5.2 -->

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



<!-- SOURCE docs/global_nonlinear.md:7652-8258; C.4.6.3 sections 1-6, complete source/moment proofs -->

##### C.4.6.3. Actual finite weighted queries and admissible forcing

The field and clock notation is that of C.4.6.1. The following argument
retains the actual finite Gaussian readout throughout physical GF. It uses
one-column deletion only as a comparison, and leaves the learned cavity
flow, its residuals, and both matrix orientations intact.

###### 1. Source theorem

For every fixed finite physical `T`, put

\[
 E_n=\{\|A_{0,n}\|_{op}\le10,
          \|c_{0,n}\|_\infty\le1,
          \|g_n\|_F/\sqrt n\le2\}.
 \tag{C.4.6.S3}
\]

Its probability tends to one. The matrix assertion follows from the
contained sphere-net Gaussian estimate in special-data III.F.2; the root
assertion is the iid second-moment law; and
`P(max_j |c0,j|>1)<=2n exp(-n²/2)`. In particular (C.4.6.S3) retains the actual
small Gaussian readout.

**Finite source theorem.** For each finite `p>=1,T<infinity`, there is a
finite deterministic `C_(p,T)` such that

\[
 \mathbb E\left[\mathbf1_{E_n}\frac1n\sum_{i=1}^n
       \sup_{t\le T,u\in S^1}|Q_{n,i}(t,u)|^p\right]
       \le C_{p,T},\qquad n\ge1.                         \tag{C.4.6.S4}
\]

The constants can be chosen with `C_(p,T)^(1/p)<=C_T sqrt(p)` for `p>=2`.
The supremum concerns query **values**; it does not assert Gaussian tails
for input derivatives. Set `N_(n,i)=sup_(t<=T,u)|Q_(n,i)(t,u)|`. Then

\[
 \sup_{t\le T}|X_{n,ia}(t)|\le3T N_{n,i},\qquad
 \sup_{t\le T}|w_{n,i}(t)|\le |g_{n,i}|+6T N_{n,i},
 \tag{C.4.6.S5}
\]

and all finite moments, averaged over coordinates and restricted to `E_n`,
of the following envelopes are bounded independently of width:

\[
 N_{n,i},\quad (1+|g_{n,i}|+N_{n,i})^k,\quad
 \{\cosh^2g_{n,ia}+6T N_{n,i}\}N_{n,i},\quad
 (|g_{n,i}|+6T N_{n,i})N_{n,i}.                    \tag{C.4.6.S6}
\]

Here `k` is any separately fixed finite positive integer. Products of a
fixed number of these envelopes have the same property. These are actual
finite-GF estimates, before any width limit.

**Population source theorem.** For the established reference of C.4.5,
there is a finite `M_*` such that

\[
 \sup_{t\ge0,u\in S^1}
 \left(\sum_{a=1}^2
     \|\cosh^2 w_a(t)Q(t,u)\|_{L^2(\Omega_1)}^2\right)^{1/2}
 \le M_* .                                                 \tag{C.4.6.S7}
\]

The proof below gives an entirely explicit, very large upper bound from
`s_dagger<=10`; alternatively (C.4.6.S7) defines the precise reference quantity
consumed by the forcing theorem. It is not a numerical evaluation of the
actual trained endpoint.

For the shared forcing (C.4.6.T5), equivalently `b_sigma=integral b d sigma`
with `b(t,u,y)=-2r(t,u,y)q(t,u)`, the source estimate is as follows.

Then `b_sigma` is continuous in physical time, is linear in `sigma`, and

\[
 \sup_{t\ge0}\|b_\sigma(t)\|_{\mathcal V}
 \le 2(Y+\sqrt{10})\sqrt{M_*^2+11}\,\|\sigma\|_{TV}.
 \tag{C.4.6.S10}
\]

Total variation denotes total mass of the variation measure, with no
factor of one half. The estimate applies in particular to `nu-nu_*`, of
mass at most two. It imposes no support size, atom weight, Gram or
orthogonality restriction on the perturbing law. The same finite forcing
has bounded normalized moments and weighted uniform integrability on
`E_n`, uniformly over `t<=T` and inputs, with constants depending on `T,Y`.

Section C.4.6.3, §8 states the precise width identification and quadrature conclusion.
The actual derivative identification using these source estimates is
proved in C.4.6.4.

###### 2. Exact physical equations and deterministic reference bounds

The mean loss is `R=(r1²+r2²)/2`. From the stored-weight mobilities the exact
finite reference equations, and their population counterparts, are

\[
 \dot w_a=-r_a\phi'(w_a)Q_a,\quad
 \dot X_a=-r_aQ_a,\quad
 \dot K=-\sum_{a=1}^2r_a\delta_a\otimes H_a^1,\quad
 \dot c=-\sum_{a=1}^2r_aH_a^2 .                    \tag{C.4.6.S11}
\]

Here `Q_a=Q(e_a)`; the two factors of the general `-2 integral` cancel the
two atom weights. Since `F'=1/phi'`, the clock identity in (C.4.6.S11) is exact.
For a general law the corresponding first clock field is
`-2 integral r u_a phi'(w.u)Q(u)/phi'(w_a)`, which gives (C.4.6.T5), with its
displayed sign and normalization. No probability-law derivative is used
to establish these identities.

On (C.4.6.S3), initially `|f_a|<=1`, hence `R(0)<=4`. The true raw energy identity
gives `R(t)<=4` and raw path displacement at most `2sqrt(T)` up to time T.
Therefore, simultaneously for all `t<=T`,

\[
 \|A(t)\|_{op}\le B:=10+2\sqrt T,\quad
 \|c(t)\|_2/\sqrt n\le C:=1+2\sqrt T,
 \quad\|w(t)\|_F/\sqrt n\le W:=2+2\sqrt T,
 \tag{C.4.6.S12}
\]

and `||K||F<=2sqrt(T)`. Moreover `sum_a|r_a|<=4`, `|r_a|<=sqrt(8)<3`.
Integration of `dot c` yields

\[
 \|c(t)\|_\infty\le H:=1+4T.                    \tag{C.4.6.S13}
\]

The raw energy identity follows directly by differentiating the finite
loss and substituting its three negative metric gradients; the three
metric terms are `||dot w||F²/n`, `||dot A||F²`, `||dot c||²/n`.
It prevents finite-time escape for the smooth finite-dimensional field.
These statements also hold for the column-deleted flow below, because it
has the same labels and readout, and its initial matrix norm is no larger.

For passive queries all these bounds are independent of u. Directly from
(C.4.6.S11),

\[
 \|\dot w\|_F/\sqrt n\le4BC,\quad
 \|\dot K\|_F\le4C,\quad \|\dot c\|_\infty\le4.
 \tag{C.4.6.S14}
\]

The chain and product rules in finite dimensions give

\[
 \|\partial_t Z^2(u)\|_2/\sqrt n\le4C(1+B^2),\qquad
 \|\partial_t\delta(u)\|_2/\sqrt n
        \le D_t:=4+8HC(1+B^2),
 \tag{C.4.6.S15}
\]

and factor subtraction gives

\[
 \|\delta(t,u)-\delta(t,v)\|_2/\sqrt n
       \le D_u|u-v|,\quad D_u:=2HBW.
 \tag{C.4.6.S16}
\]

Thus `(t,u)->delta(t,u)` is Lipschitz in normalized L², with deterministic
constants on (C.4.6.S3). Only the first-row **RMS** occurs in (C.4.6.S16). This fact,
applied to the independent cavity, is what permits a whole-circle Gaussian
query-value estimate without bounds on pointwise input derivatives.

###### 3. Delete one initialized column, retaining the entire learned flow

Fix neuron i in population 1. Let `a_i=A0 e_i`, an ordinary vector with iid
entries `N(0,1/n)`. Run the full reference GF with the initialized matrix

\[
 \widetilde A_0=A_0-a_i e_i^T
 \tag{C.4.6.S17}
\]

and the same initialized `g,c0`. Denote this flow by tildes. In particular
`tilde K` is trained; no neuron, activation, residual or learned rank is
removed. The flow is independent of the random column `a_i` conditionally
on all remaining initialized variables. Uniqueness of the finite ODE
establishes that measurability and independence.

Define the cavity-good event

\[
 E_n^i=\{\|\widetilde A_0\|_{op}\le10,
            \|c_0\|_\infty\le1,\ \|g\|_F/\sqrt n\le2\}.
 \tag{C.4.6.S18}
\]

It is measurable with respect to the remaining variables, and `E_n` is a
subset of `E_n^i`, because right multiplication by `I-e_i e_i^T` is a
contraction. Conditional Gaussian estimates are always made on (C.4.6.S18),
not by falsely conditioning on an event involving `a_i`.

Set `m_i=||a_i||2`, `epsilon_i=m_i/sqrt(n)` and

\[
 Z_i(t,u)=a_i^T\widetilde\delta(t,u),\qquad
 Z_i^\#=\sup_{t\le T,u\in S^1}|Z_i(t,u)|.
 \tag{C.4.6.S19}
\]

These are scalar probes of the cavity, not replacements for actual query
answers. Their conditional covariance is exactly
`tilde delta(t,u)^T tilde delta(s,v)/n`. Both orientations of the actual
matrix remain in the comparison that follows.

Let

\[
 x=\sum_a\|X_a-\widetilde X_a\|_2/\sqrt n,\quad
 k=\|K-\widetilde K\|_F,\quad
 z=\|c-\widetilde c\|_2/\sqrt n,\quad d=x+k+z.
 \tag{C.4.6.S20}
\]

There is no small operator-norm claim for `A0-tilde A0`. Instead its
forward action on a bounded feature has RMS at most `epsilon_i`. Its
reverse action on a cavity backward field has RMS
`|Z_i(t,e_a)|/sqrt(n)`. With `delta_cav` denoting full minus cavity, add and
subtract factors in precisely this order:

\[
 \delta_{\rm cav} Z_a^2=A\delta_{\rm cav} H_a^1
         +(K-\widetilde K)\widetilde H_a^1
         +a_i\widetilde H_{a,i}^1,
\]
\[
 \delta_{\rm cav} Q_a=A^T\delta_{\rm cav}\delta_a
          +(K-\widetilde K)^T\widetilde\delta_a
          +e_i Z_i(t,e_a).
 \tag{C.4.6.S21}
\]

The second identity deliberately uses the full A in the first term, so
that no uncontrolled column-dependent reverse error appears. On `E_n`,
the deterministic state bounds for both flows yield

\[
 \sum_a\|\delta_{\rm cav} H_a^1\|_2/\sqrt n\le x,
 \quad V:=\sum_a\|\delta_{\rm cav} Z_a^2\|_2/\sqrt n
                      \le Bx+2k+2\epsilon_i,
\]
\[
 D:=\sum_a\|\delta_{\rm cav}\delta_a\|_2/\sqrt n\le2z+2H V,
\]
\[
 P:=\sum_a\|\delta_{\rm cav} Q_a\|_2/\sqrt n
       \le BD+2Ck+\frac1{\sqrt n}\sum_a|Z_i(t,e_a)|,
\]
\[
 R_{\rm cav}:=\sum_a|r_a-\widetilde r_a|\le2z+CV.
 \tag{C.4.6.S22}
\]

For the last inequality use `f-tilde f=<delta_cav c,H2>+
<tilde c,H2-tilde H2>`. The first uses `|j_X|<=1`, with the same roots.
The velocity differences from (C.4.6.S11) satisfy

\[
 \sum_a\|\delta_{\rm cav}\dot X_a\|_2/\sqrt n\le BC R_{\rm cav}+3P,
\]
\[
 \|\delta_{\rm cav}\dot K\|_F\le C R_{\rm cav}+3(D+Cx),\qquad
 \|\delta_{\rm cav}\dot c\|_2/\sqrt n\le R_{\rm cav}+3V.
 \tag{C.4.6.S23}
\]

For example the rank difference is bounded by
`||delta_cav delta||2/sqrt(n)+C||delta_cav H1||2/sqrt(n)` before its residual
factor. These estimates include the changed residuals; the cavity has
not been driven by the full flow's residuals.

Write `D0=1+B+C+H+3`, `L=100D0^4`. Substitution of (C.4.6.S22) into (C.4.6.S23)
gives the explicit overestimate

\[
 \dot d\le Ld+\frac L{\sqrt n}
       \left(m_i+\sum_a|Z_i(t,e_a)|\right)
       \quad\hbox{for almost every }t,\qquad d(0)=0.
 \tag{C.4.6.S24}
\]

To check the constant, `V<=3D0 d+2epsilon_i`,
`D<=8D0² d+4D0 epsilon_i`,
`P<=10D0³d+4D0²epsilon_i+sum|Z_i|/sqrt(n)`,
`R_cav<=5D0²d+2D0epsilon_i`.
The three resulting d coefficients sum to at most `81D0^4`, and the
`epsilon_i` coefficients to at most `36D0³`. Norms of absolutely
continuous finite curves obey the derivative bound by the velocity norm,
which justifies (C.4.6.S24) also at zeros of a component norm. Multiplying its
integral form by the integrating factor gives

\[
 \sqrt n\sup_{t\le T}d(t)
       \le J_T(m_i+2Z_i^\#),\qquad J_T:=LT e^{LT}.
 \tag{C.4.6.S25}
\]

This is the small response to deleting one initialized column that an
operator-norm comparison alone would miss.

For an arbitrary passive input u, the first row still obeys
`||delta_cav(w.u)||2/sqrt(n)<=x`, so the same forward subtraction gives

\[
 \|\delta(t,u)-\widetilde\delta(t,u)\|_2/\sqrt n
            \le4D0^2(d(t)+\epsilon_i).
 \tag{C.4.6.S26}
\]

The learned transpose contribution has an exact, coordinatewise bound:

\[
 (K(t)^T\delta(t,u))_i
   =-\int_0^t\sum_a r_a(v)H_{a,i}^1(v)
       \frac{\delta_a(v)^T\delta(t,u)}n\,dv,
 \qquad |(K(t)^T\delta(t,u))_i|\le4TC^2.
 \tag{C.4.6.S27}
\]

Using `Q_i=a_i^T delta+(K^T delta)_i`, (C.4.6.S25)–(C.4.6.S27), and `m_i<=10` on
`E_n`, gives

\[
 N_{n,i}\le A_T Z_i^\#+B_T\quad\hbox{on }E_n,
\]
\[
 A_T=1+80D0^2J_T,\qquad
 B_T=400D0^2(J_T+1)+4TC^2.
 \tag{C.4.6.S28}
\]

No independence of the actual `delta` and `a_i` has been assumed. Their
dependence is exactly the error controlled in (C.4.6.S26).

###### 4. A contained Gaussian maximum bound

Here are all probability ingredients beyond the initialized operator
bound. If `G_1,...,G_N` are centered jointly Gaussian scalars with
variances at most `v²`, no independence among them is required for

\[
 \Pr\{\max_j|G_j|>r\}\le2N e^{-r^2/(2v^2)}.
 \tag{C.4.6.S29}
\]

This follows by applying the scalar Gaussian exponential moment and
Markov's inequality to each tail and taking a union bound. Consequently,
for `p>=2`,

\[
 \|\max_j|G_j|\|_{L^p}
       \le v\{\sqrt{2\log(2N)}+2\sqrt p\}.
 \tag{C.4.6.S30}
\]

For detail, put `a=v sqrt(2log(2N))` and `V=(max|G_j|-a)_+`.
Equation (C.4.6.S29) implies `P(V>r)<=exp(-r²/(2v²))`.
For `m=ceil(p/2)`, integrating this tail against `2m r^(2m-1)` gives
`E V^(2m)<=(2v²)^m m!`; the integral follows by substituting
`q=r²/(2v²)` and integrating by parts m times. Since `m!<=m^m`,
monotonicity of probability-space Lp norms gives
`||V||p<=||V||_(2m)<=v sqrt(2m)<=v sqrt(2p)`, because
`2m<=p+2<=2p` for `p>=2`. Minkowski gives (C.4.6.S30), with slack in the
constant 2. The case `v=0` is zero.

Suppose a continuous centered Gaussian process `Z(q)`, `q in [0,1]^2`,
has variance at most `C²` and
`||Z(q)-Z(q')||L² <= L0 ||q-q'||_1`. Use square grids of spacing `2^-k`
and round each grid point down to its parent on the preceding grid.
There are at most `4^(k+1)` grid points at level k. Parent increments
have standard deviation at most `2L0 2^-k`. Formula (C.4.6.S30), followed by
Minkowski, bounds the sum over k of their maxima in Lp by

\[
 2L0\sum_{k\ge1}2^{-k}
  \{\sqrt{2\log(2\cdot4^{k+1})}+2\sqrt p\}
       \le60L0\sqrt p.
 \tag{C.4.6.S31}
\]

The inequality follows for instance from `sqrt(k+2)<=k+2` and
`sum_(k>=1) k2^-k=2`, `sum_(k>=1)2^-k=1`. The four level-zero corner
values cost at most `4C sqrt(p)` by (C.4.6.S30). The telescoping sums and
continuity at each q therefore give

\[
 \|\sup_q|Z(q)|\|_{L^p}
                \le64(C+L0)\sqrt p.                    \tag{C.4.6.S32}
\]

This proof works conditionally on arbitrary fixed coefficients. Here,
conditional on all variables except column `a_i`, the process (C.4.6.S19) is
a finite linear combination of independent Gaussians, with continuous
coefficients. On `E_n^i`, (C.4.6.S12), (C.4.6.S15)–(C.4.6.S16) apply to the cavity. Parameterize
`t=T q1`, `u=(cos(2pi q2),sin(2pi q2))`. Thus (C.4.6.S32) gives

\[
 \left(\mathbb E_{a_i}[(Z_i^\#)^p]\right)^{1/p}
       \le C_Z\sqrt p,\qquad
 C_Z:=64\{C+T D_t+2\pi D_u\},\quad\hbox{on }E_n^i.
 \tag{C.4.6.S33}
\]

Since `E_n subset E_n^i`, (C.4.6.S28), conditioning, and then (C.4.6.S33) prove

\[
 \left(\mathbb E[\mathbf1_{E_n}N_{n,i}^p]\right)^{1/p}
     \le (B_T+A_T C_Z)\sqrt p=:C_T\sqrt p.
 \tag{C.4.6.S34}
\]

This bound is the same for every i and n; averaging proves (C.4.6.S4). It has
not inferred empirical moments from RMS convergence or exchangeability.
It used the reached continuous reference flow and its quantitative
column-deletion sensitivity. The selected-column concentrating examples
in special-data J.1 and the three-query obstruction in Gaussian calculus
therefore do not contradict it: those arbitrary adapted queries do not
satisfy (C.4.6.S24) with the present constants.

###### 5. Clock weights, products and actual finite uniform integrability

For each fixed g,

\[
 \partial_X\cosh^2 j(X,g)=2\tanh j(X,g),
 \qquad \cosh^2 j(X,g)\le\cosh^2g+2|X|.
 \tag{C.4.6.S35}
\]

The derivative identity follows from `j_X=sech² j`; its absolute value is
at most two, and integration gives the inequality for either sign of X.
This exact estimate avoids an unnecessary exponential in `|X|`. Integrating
`dot X_a=-r_a Q_a` with `|r_a|<=3` proves (C.4.6.S5). The factor 6 in its row
bound is an upper bound for `3sqrt(2)`.

Every Gaussian root has every polynomial and linear-exponential moment.
In particular
`E exp(q|G|)<=E exp(qG)+E exp(-qG)=2exp(q²/2)`.
For any fixed p, the moment of `cosh²g_a N_i` on `E_n` is bounded by
Hölder using the `2p` moments of both factors. No independence between
the evolved query and g is required. The same reasoning applies to all
products in (C.4.6.S6). For example, with

\[
 P_{n,i,a}:=(\cosh^2g_{n,ia}+6T N_{n,i})N_{n,i},
 \tag{C.4.6.S36}
\]

one obtains

\[
 \sup_n\mathbb E\left[\mathbf1_{E_n}\frac1n\sum_i
                          P_{n,i,a}^{p}\right]<\infty.
 \tag{C.4.6.S37}
\]

For the finite source coordinate in (C.4.6.T5), `|r(t,u,y)|<=C+Y` and
`|u_a|,phi'(w.u)<=1`, so its supremum over `t,u,|y|<=Y` is bounded by
`2(C+Y)P_(n,i,a)`. Given any `p>2`,

\[
 \mathbb E\left[\mathbf1_{E_n}\frac1n\sum_i
     P_{n,i,a}^{2}\mathbf1_{P_{n,i,a}>R}\right]
       \le C_{p,T}R^{-(p-2)}.                         \tag{C.4.6.S38}
\]

Markov's inequality shows that these empirical square tails tend to zero
in probability, uniformly in width on `E_n`, as R tends to infinity.
Outside `E_n` the probability tends to zero as n grows. Thus the ordered
statement needed for width passage is

\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
 \Pr\left\{\sup_{t,u,|y|\le Y}
       \frac1n\sum_i |b_{X,a,n,i}(t,u,y)|^2
                     \mathbf1_{|b_{X,a,n,i}|>R}>\varepsilon\right\}=0.
 \tag{C.4.6.S39}
\]

One can put the supremum inside the coordinate envelope as in (C.4.6.S38), so
the stated form follows. The same argument proves weighted tails involving
`|w|Q` or any separately fixed polynomial of the displayed envelopes.
These estimates make no assertion that a bounded initialized Gaussian
action maps every Lp input boundedly into Lp.

###### 6. Uniform population bounds from the bounded feature segment

The established physical reference equals the autonomous feature flow

\[
 X_{a,s}=\tfrac12y_a Q_a,\quad
 K_s=\tfrac12\sum_a y_a\delta_a\otimes H_a^1,\quad
 c_s=\tfrac12\sum_a y_aH_a^2,
 \tag{C.4.6.S40}
\]

restricted to `0<=s<s_dagger`, where `s_dagger<=10`, with
`ds/dt=2(1-b)>0`. This is C.4.5.1's actual reference and endpoint, not a
new prescription for physical finite GF. To bound the population sources
uniformly in physical time, apply the preceding cavity argument to the
**auxiliary finite feature equation** (C.4.6.S40) on `0<=s<=S=10`, initialized
with `c0=0`. Only this auxiliary equation has zero finite readout.

Its elementary deterministic bounds, on
`{||A0||op<=10, ||g||F/sqrt(n)<=2}`, are

\[
 \|c(s)\|_\infty\le S,\quad \|K(s)\|_F\le S^2/2,\quad
 B=10+S^2/2,\quad C=H=S+1,
\]
\[
 \|w(s)\|_F/\sqrt n\le
 W:=2+10S^2/2+S^4/8.                               \tag{C.4.6.S41}
\]

Indeed `sum_a |y_a/2|=1`, so `||c_s||infty<=1`,
`||K_s||F<=s`, and
`sum_a ||X_(a,s)||2/sqrt(n)<= (10+s²/2)s`. Integration and
`|j(X,g)-g|<=|X|` give (C.4.6.S41). These bounds prove existence on the entire
finite feature interval as in B.1's transformed integral construction.

The proof of (C.4.6.S21)–(C.4.6.S28) now uses the same fixed controls in both flows;
all residual-difference terms vanish. The retained upper bound `L=100D0^4`
remains valid. The velocity bounds (C.4.6.S14)–(C.4.6.S16) remain upper bounds, since
the absolute sum of feature controls is at most one rather than four.
Consequently the formulas (C.4.6.S28), (C.4.6.S33), (C.4.6.S34), with `T` replaced by S and
the constants (C.4.6.S41), give a number `C_*<infinity` such that

\[
 \mathbb E\left[\mathbf1_{E_n^{feat}}\frac1n\sum_i
      \sup_{s\le S,u}|Q^{feat}_{n,i}(s,u)|^p\right]
         \le(C_*\sqrt p)^p,\qquad p\ge2.             \tag{C.4.6.S42}
\]

Every quantity in this crude bound is explicitly given above. No numerical
flow solution is hidden in `C_*`, and no fitting property of the finite
feature flow is assumed.

We detail how this reaches the *canonical* population flow. On each fixed
transformed Euler mesh, append finitely many passive forward and reverse
queries to the oracle program in B.1. The first-row transform is continuous
with at most linear growth in `(X,g)`, hence global-nonlinear A.1 applies.
Readout products can be clipped outside a fixed open neighborhood of the
bound in (C.4.6.S41), so they meet the fixed-program hypotheses. Both matrix
orientations belong to the same III.F construction. Same-root transformed
stability controls the finite-feature-flow/mesh error uniformly in width.
The corresponding population error tends to zero in clock L², increment
HS and readout L²; the HS assertion is proved in C.4.5.2, §1. Passive Q
errors follow by factor subtraction with bounded readout. Width first at
fixed mesh, then mesh removal, therefore gives the joint empirical W2
limits for every finite list of `(g,X,w,Q(s,u))`.

For a finite list of rational parameter pairs `(s_j,u_j)`, apply this
convergence to the bounded continuous test
`min(R,max_j |Q(s_j,u_j)|^p)`. Its empirical average converges in
probability to the deterministic population expectation; since the test
is bounded, the expectations converge as well. Multiplication by
`1_(E_n^feat)` changes the expectation by at most
`R P((E_n^feat)^c)`, which vanishes. Equation (C.4.6.S42) and monotone convergence,
first in R and then in the finite rational lists, give a population
envelope

\[
 N^\#:=\sup_{(s,u)\in\mathcal D}|Q(s,u)|,
 \qquad\|N^\#\|_{L^p}\le C_*\sqrt p,             \tag{C.4.6.S43}
\]

where `mathcal D` is any fixed countable dense parameter set including
the active directions. This envelope is a statement about simultaneous
representatives on that countable set. For any other fixed deterministic
`(s,u)`, L² continuity of Q supplies an almost surely convergent subsequence
from the dense set; thus `|Q(s,u)|<=N#` in its L² equivalence class.
Fubini gives the bound almost everywhere for any fixed deterministic
observation measure. No assertion of pointwise continuous sample paths
for the population Q, or of Gaussian input-derivative tails, is needed.
The map into L² is jointly continuous and is the canonical action map.

Integration of (C.4.6.S40), followed by Fubini, gives almost surely
`sup_s |X_a(s)|<=S N#/2`, for the absolutely continuous active clocks.
Thus (C.4.6.S35) gives, in every deterministic passive-input equivalence class,

\[
 |\cosh^2w_a(s)Q(s,u)|
          \le(\cosh^2g_a+S N^\#)N^\#.
 \tag{C.4.6.S44}
\]

Hölder, `||N#||4<=2C_*`, and
`||cosh²G||4<=(2e^32)^(1/4)=2^(1/4)e^8` imply the explicit bound

\[
 M_*\le\sqrt2\{2^{5/4}e^8 C_*+4S C_*^2\},\qquad S=10.
 \tag{C.4.6.S45}
\]

The physical path stays in this feature segment, so (C.4.6.S7) holds for all
physical times. The reference quantity M_w in (C.4.6.T8) satisfies
`M_w<=M_*`; using the input weights `sum_a u_a²=1` gives the sharper
forcing constant in (C.4.6.T9). This reasoning establishes a uniform population source
bound, separately from the fixed-physical-horizon finite estimate (C.4.6.S4).
It does not claim uniform-in-time finite-width convergence.


<!-- SOURCE docs/global_nonlinear.md:12994-15322; C.4.9 complete theorem and all proof units -->

#### C.4.9. Nonlinear prediction selection during a finite added-data episode

This result concerns the whole-circle prediction selected by actual nonlinear
training after a fixed amount of learning from a component whose mixture weight
vanishes. The physical training law is unchanged throughout each run. The
limiting episode is a constrained gradient flow with evolving hidden features;
its initialization is the established fitted reference state, obtained from
the original initialization by a justified initial-layer limit.

##### Model, determining equation and theorem

Use the canonical bias-free network with two tanh hidden layers,

\[
 u=x/\sqrt2\in S^1,\quad h^1_n=\tanh(W^1_nu),\quad
 h^2_n=\tanh(W^2_nh^1_n),\quad f_n=(W^3_n)^Th^2_n/n.
\]

Initialize every entry and block independently, centered Gaussian with stored
variances \((1,1/n,1/n^2)\). Use mobilities \((n,1,n)\), the unhalved mean square,
and physical gradient flow. Keep the actual finite initial Gaussian readout.
Set

\[
 \nu_*={1\over2}\delta_{(\sqrt2e_1,1)}
             +{1\over2}\delta_{(\sqrt2e_2,-1)},\qquad
 \mu_{\epsilon,\alpha,y}=(1-\epsilon)\nu_*+\epsilon\nu_{\alpha,y},
\]
\[
 \nu_{\alpha,y}=\delta_{(\sqrt2u_\alpha,y)},\quad
 u_\alpha=(\cos\alpha,\sin\alpha),\quad
 |\alpha-\pi/4|\le1/1216,\quad 3/8\le y\le5/8.
 \tag{NS1}
\]

This fixed compact parameter rectangle has nonempty interior in location and
label. All its added inputs are nonorthogonal to both reference inputs. Its
labels are admitted for every fixed \(Y\ge1\). All actual mixture flows begin
at the original Gaussian initialization and use that same mixture throughout.

Let \(H_1=L^2(\Omega_1)\) and \(H_2=L^2(\Omega_2)\) be the canonical generated
Gaussian action spaces, with initialized action \(A_0:H_1\to H_2\) and its true
Hilbert adjoint. Their construction is by the joint Gaussian finite-program
law, including the response to every reused forward and transpose call.
The raw state is \(\theta=(w,K,c)\), where
\(w\in L^2(\Omega_1;\mathbb R^2)\), \(K:H_1\to H_2\) is Hilbert–Schmidt,
\(c\in H_2\), and \(A=A_0+K\). Only the increment is Hilbert–Schmidt.
Use the squared metric \(\|\Delta w\|_2^2+\|\Delta K\|_{HS}^2+\|\Delta c\|_2^2\).

The established reference endpoint \(\theta_\dagger\) is explicitly determined
from \((g,A_0,0)\), \(g\sim N(0,I_2)\), by the reference feature equation:
write \(\phi=\tanh\), \(H^1(u)=\phi(w\cdot u)\), \(H^2(u)=\phi(AH^1(u))\),
\(\delta(u)=c\phi'(AH^1(u))\), and \(Q(u)=A^*\delta(u)\). Starting at
\((w,K,c)=(g,0,0)\), solve

\[
 \partial_s w={1\over2}\sum_{a=1}^2 y_a\phi'(w\cdot e_a)Q(e_a)e_a,
 \quad \partial_sK={1\over2}\sum_{a=1}^2y_a\delta(e_a)\otimes H^1(e_a),
 \quad \partial_sc={1\over2}\sum_{a=1}^2y_aH^2(e_a),
\]

where \(y_1=1,y_2=-1\), and stop at the unique first \(s=s_\dagger\le10\)
with \(\langle c,(H^2(e_1)-H^2(e_2))/2\rangle=1\). The global clock construction
in C.4.5 proves well-posedness of this prescription and identifies it with the
physical reference endpoint. Put \(F_*(\sqrt2u)=f_{\theta_\dagger}(u)\).
The zero readout in this population initialization is the limit of the actual
finite readout and imposes no finite-network reset.

For every state used below, define its current raw prediction gradient

\[
 g_\theta(u)=\left(
   \phi'(w\cdot u)Q(u)u,\quad \delta(u)\otimes H^1(u),\quad H^2(u)
                    \right),
\]
\[
 G_\theta=(g_\theta(e_1),g_\theta(e_2)),\quad
 M_\theta=G_\theta^*G_\theta,\quad
 \Pi_\theta=I-G_\theta M_\theta^{-1}G_\theta^*.
 \tag{NS2}
\]

The inverse exists throughout the asserted episode. The determining evolution
and reconstruction are

\[
 {d\bar\theta_{\alpha,y}\over d\tau}
   =-2\big(f_{\bar\theta_{\alpha,y}}(u_\alpha)-y\big)
                  \Pi_{\bar\theta_{\alpha,y}}g_{\bar\theta_{\alpha,y}}(u_\alpha),
 \qquad \bar\theta_{\alpha,y}(0)=\theta_\dagger,
 \tag{NS3}
\]
\[
 P_{\alpha,y}(\tau,\sqrt2u)
   =\left\langle\bar c(\tau),
      \tanh\big((A_0+\bar K(\tau))\tanh(\bar w(\tau)\cdot u)\big)\right\rangle.
 \tag{NS4}
\]

Every coefficient in (NS3) is computed from the specified current state and
the established initialized action. In particular its projection and all
hidden features are recomputed along the evolution. There is no coefficient
supplied by an unknown changed-law trajectory.

**Theorem.** There exist \(\epsilon_0,\tau_0,a,j>0\), uniform over the parameter
rectangle (NS1), with these properties.

1. Equation (NS3) has a unique strong solution on \([0,\tau_0]\) in a fixed
   neighborhood of \(\theta_\dagger\). It is constructed on the canonical
   initialized carrier with its full retained reference history. It preserves
   the two reference predictions exactly. It determines (NS4) over the whole
   circle.

2. For every \(0<\epsilon<\epsilon_0\), the original-initialization mixture
   population GF exists and is unique through \(T_\epsilon=\tau_0/\epsilon\).
   For every \(0<\tau_-<\tau_0\),
   \[
    \sup_{(\alpha,y)}\sup_{\tau_-\le\tau\le\tau_0}
      \|\theta_{\mu_{\epsilon,\alpha,y}}(\tau/\epsilon)
                    -\bar\theta_{\alpha,y}(\tau)\|_{\rm raw}\longrightarrow0.
    \tag{NS5}
   \]
   The same convergence holds for predictions uniformly over the entire
   circle and for the finite named hidden observations stated below.
   The exclusion of \(\tau=0\) records the genuine initial layer; no pretraining
   stage is imposed on any actual run.

3. With \(R_\nu(f)=\int(f(x)-y)^2\,d\nu(x,y)\), the selected finite-episode
   prediction satisfies
   \[
      R_{\nu_{\alpha,y}}(F_*)
       -R_{\nu_{\alpha,y}}(P_{\alpha,y}(\tau_0))\ge a.
    \tag{NS6}
   \]
   This is risk on the added component itself, without its factor \(\epsilon\).
   For \((v_1,v_2,v_3)=(e_1,e_2,u_\alpha)\), its paired upper-hidden change is
   \[
    {1\over3}\sum_{i=1}^3
      \|H^2_{\bar\theta_{\alpha,y}(\tau_0)}(v_i)
                         -H^2_{\theta_\dagger}(v_i)\|_2^2\ge j.
    \tag{NS7}
   \]
   Both states use the same initialized primitives. The hidden displacement
   therefore measures adaptation caused by the added law after reference fitting.

4. For every separately fixed \(\epsilon\in(0,\epsilon_0)\) and law in (NS1),
   actual finite GF converges in probability to the mixture population
   prediction in \(C([0,T_\epsilon]\times\sqrt2S^1)\), with the joint
   same-layer internal observations needed for paired hidden measurements.
   Consequently, for every such fixed law and every \(\eta>0\),
   \[
    \lim_{\epsilon\downarrow0}\limsup_{n\to\infty}
     \Pr\!\left\{\sup_x|f_{n,\mu_\epsilon}(T_\epsilon,x)
                       -P_{\alpha,y}(\tau_0,x)|>\eta\right\}=0.
    \tag{NS8}
   \]
   Train a reference network with the same initial arrays, including readout,
   and define the directly paired finite observable
   \[
    J_{2,n,\epsilon}={1\over3n}\sum_{i=1}^3
      \|h^2_{n,\mu_\epsilon}(T_\epsilon,\sqrt2v_i)
                    -h^2_{n,\nu_*}(T_\epsilon,\sqrt2v_i)\|_2^2.
    \tag{NS9}
   \]
   In the same iterated order it converges in probability to (NS7)'s
   population quantity. In particular the probability that the added-risk
   gain is at least \(a/2\) and \(J_{2,n,\epsilon}\ge j/2\) tends to one.

The constants need not be numerically practical. The theorem asserts one fixed,
nonzero slow-time episode, not a final endpoint for the changed law. It gives
no simultaneous width/contamination rate and no raw-GD extension. The scale
\(\tau=\epsilon t\) follows from the stable reference-residual equations and
the remaining tangential force, as proved below.

##### Proof architecture

The proof first establishes a Gaussian source bound for a small perturbation
of the reference in integrated control mass, uniformly in physical horizon.
A protected Gaussian-row argument then proves strict endpoint conditioning.
Together these facts construct (NS3) and continue the actual mixture through
(NS5). An exact residual identity proves selection on the slow clock.
A fixed-readout hidden contrast and the exact risk derivative yield (NS6)–(NS7).
Finally a same-array, one-reference cutoff comparison identifies actual finite
GF and the paired observations in (NS8)–(NS9).

Equation labels and auxiliary constants are local to each proof unit below.
All finite vector norms are ordinary Euclidean norms; normalization factors
are displayed in the finite-state metric.


##### Proof unit A. Uniform source control in accumulated training force

###### A.1. Statement with the exact control and approximation conventions

Keep the canonical two-hidden tanh carrier, Gaussian action \(A_0\)
with its actual adjoint, \(w(0)=g\sim N(0,I_2)\), \(K(0)=0,c(0)=0\),
and \(A=A_0+K\). The raw Hilbert metric is
\[
 \|\Delta\theta\|_{\rm raw}^2
 =\|\Delta w\|_2^2+\|\Delta K\|_{\rm HS}^2+\|\Delta c\|_2^2.
\]
For each \(u\in S^1\), define
\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad
 H^2(u)=\phi(Z^2(u)),\quad
 \Delta^{(2)}(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\Delta^{(2)}(u),
\]
\[
 g_u(\theta)=
 \bigl(\phi'(w\cdot u)Q(u)u,\,
       \Delta^{(2)}(u)\otimes H^1(u),\,H^2(u)\bigr),\qquad\phi=\tanh.
 \tag{CT1}
\]
This is the actual raw gradient of the scalar prediction. It retains
the original architecture and both orientations of the reused matrix.

Fix finitely many directions \(u_1=e_1,u_2=e_2,u_3,\ldots,u_J\)
on the circle. They need not be distinct, separated, or orthogonal.
For a physical interval \(I=[0,T]\), where \(T\) is arbitrary and may
also be infinite, let \(a_j(t)\) be deterministic integrable controls.
The comparison controls are the complete reference history
\[
 a_{*,1}(t)=e_*(t),\qquad a_{*,2}(t)=-e_*(t),\qquad
 a_{*,j}(t)=0\quad(j\ge3),
 \qquad e_*=1-f_*(e_1)>0.
 \tag{CT2}
\]
Its total absolute mass is the reference feature length, at most
\(s_\dagger\le10\). Only finiteness of this bound is necessary below.
The controlled equation is
\[
 \theta'(t)=\sum_{j=1}^J a_j(t)g_{u_j}(\theta(t)).
 \tag{CT3}
\]

**Controlled source-tube theorem.** There are \(\delta>0\), \(h_0>0\),
\(B<\infty\), \(M<\infty\), and \(c>0\), depending only on the
reference feature segment and the canonical model, with the following
properties. They are independent of \(T\), the number of time steps,
and the minimum nonzero control coefficient.

Assume
\[
 q:=\int_I\sum_j|a_j(t)-a_{*,j}(t)|\,dt\le\delta.
 \tag{CT4}
\]
Use the common dominating measure
\[
 ds=\sum_j(|a_j(t)|+|a_{*,j}(t)|)\,dt.
 \tag{CT5}
\]
On a finite partition in this control clock with maximal interval
length at most \(h_0\), take exact integrated coefficients
\[
 \gamma_{kj}=\int_{I_k}a_j(t)\,dt,\qquad
 \bar\gamma_{kj}=\int_{I_k}a_{*,j}(t)\,dt
 \tag{CT6}
\]
and run raw Euler with these coefficients and the same initialization.
Every passive backward-source row at every node satisfies
\[
 |\beta_{ku,ku}|+\sum_{s<k,j}|\beta_{ku,sj}|\le B,\qquad
 \sup_{u\in S^1}\tau_R(Q_k(u))\le M e^{-cR^2},\quad R\ge1.
 \tag{CT7}
\]
The corresponding readout tails have the same bound after enlarging
\(M\). Current passive slots are distinguished as described below.
Zero controls and padding are permitted. The estimate retains all
source slots from the entire reference history.

The assertion here is a finite-program source bound. Proof unit C constructs
the required strong nonlinear trajectories from these bounds; proof unit D
identifies actual finite GF. No probability supremum over random finite-network
feedback controls is asserted by this source estimate.

###### A.2. Why control time is a legitimate common parameter

Set \(L_*=10\), reducing it to the actual reference bound if desired.
From (CT4),
\[
 \int_I\sum_j|a_j|\le L_*+q,\qquad
 S:=\int_I\sum_j(|a_j|+|a_{*,j}|)\le2L_*+q.
 \tag{CT8}
\]
The increasing cumulative distribution of (CT5) is continuous.
Where its density is positive, divide each control by that density;
the resulting coefficients \(b_j(s),\bar b_j(s)\) satisfy
\[
 \sum_j(|b_j(s)|+|\bar b_j(s)|)=1
 \quad\hbox{for almost every }s.
 \tag{CT9}
\]
Flat parts carry zero control and zero state change. A generalized
inverse gives the control-clock integral equations, and substitution
in the Lebesgue integral recovers physical time. Equivalently all
formulas can first be proved for step functions and passed in \(L^1\).
This change introduces no optimizer or future state information:
the controls in this theorem are prescribed deterministic functions.

For coefficient arrays define
\[
 m_{kj}=|\gamma_{kj}|+|\bar\gamma_{kj}|,\quad
 m_k=\sum_jm_{kj},\quad
 q_{\rm disc}=\sum_{k,j}|\gamma_{kj}-\bar\gamma_{kj}|.
 \tag{CT10}
\]
Then \(\sum_km_k\le2L_*+q\), \(q_{\rm disc}\le q\), and
\(m_k\le h_0\). A slot with \(m_{kj}=0\) can be omitted or retained
with zero coefficient. For a nonzero slot \(p=(s,j)\), put
\[
 e_p=\frac{|\gamma_p-\bar\gamma_p|}{m_p}\in[0,1],
 \qquad \sum_pm_pe_p=q_{\rm disc}.
 \tag{CT11}
\]
There is no division by a reference coefficient. In particular
(CT11) handles a genuinely new direction, whose reference control
is zero, and vanishing actual controls.

###### A.3. Exact named-source equations and inactive slots

At each node all active forward calls precede its reverse calls.
Both compared programs use the same training-slot index set.
For a passive current query append one otherwise unused forward and
reverse pair; call its one direct forward slot \(ku\).
Old unused passive queries may be discarded because their values
were never used by an update. Their formal derivatives in every
later state are zero. They do not accumulate a diagonal response
at subsequent times.

With the deterministic controls, contractions, covariances and
response coefficients frozen under named differentiation, the
source equations are
\[
 \begin{aligned}
 w_{k+1}&=w_k+\sum_j\gamma_{kj}
             \phi'(w_k\cdot u_j)Q_{kj}u_j,\\
 c_{k+1}&=c_k+\sum_j\gamma_{kj}\phi(Z^2_{kj}),\\
 K_{k+1}&=K_k+\sum_j\gamma_{kj}\Delta^{(2)}_{kj}\otimes H^1_{kj},
 \end{aligned}                                                   \tag{CT12}
\]
\[
 \begin{aligned}
 Z^2_{ku}&=\xi_{ku}+\sum_{p<k}F_{ku,p}\Delta^{(2)}_p,&
 F_{ku,p}&=\alpha_{ku,p}
                  +\gamma_p\mathbb E_1[H^1_{ku}H^1_p],\\
 Q_{ku}&=\zeta_{ku}+\sum_{p\le k}D_{ku,p}H^1_p,&
 D_{ku,p}&=\beta_{ku,p}
          +{\bf1}_{p<k}\gamma_p\mathbb E_2[\Delta^{(2)}_{ku}\Delta^{(2)}_p],
 \end{aligned}                                                   \tag{CT13}
\]
where \(p<k\) means an earlier time index. At the passive current
time the sum has its one distinguished slot; at an active output
all other current beta coefficients are zero. Specifically
\[
 \alpha_{ku,p}=\mathbb E_1[\partial_{\zeta_p}H^1_{ku}],\qquad
 \beta_{ku,p}=\mathbb E_2[\partial_{\xi_p}\Delta^{(2)}_{ku}],\qquad
 \beta_{ku,ku}=\mathbb E_2[c_k\phi''(Z^2_{ku})].
 \tag{CT14}
\]
An identical input does not merge its formal current name with an
earlier source. A singular covariance also does not merge those
names.

For lower pulses \(v_{k;p}=\partial_{\zeta_p}w_k\),
\[
 \begin{aligned}
 v_{k+1;p}=v_{k;p}+\sum_j\gamma_{kj}u_j\bigg[
 &\phi''(w_k\cdot u_j)Q_{kj}(u_j\cdot v_{k;p})\\
 &+\phi'(w_k\cdot u_j)
 \left({\bf1}_{(k,j)=p}
   +\sum_{q\le k}D_{kj,q}\phi'(w_{t(q)}\cdot u_q)
                                    (u_q\cdot v_{t(q);p})\right)
 \bigg].
 \end{aligned}                                                   \tag{CT15}
\]
For upper pulses,
\[
 \begin{aligned}
 C_{k;p}&=\sum_{q<k}\gamma_q\phi'(Z^2_q)U_{q;p},\\
 U_{ku;p}&={\bf1}_{ku=p}+\sum_{q<k}F_{ku,q}V_{q;p},\\
 V_{ku;p}&=\phi'(Z^2_{ku})C_{k;p}
                   +c_k\phi''(Z^2_{ku})U_{ku;p}.
 \end{aligned}                                                   \tag{CT16}
\]
These formulas follow directly by differentiating (CT12)–(CT13);
they are also C.4.7.N7–N8 without its residual specialization.
They do not differentiate a residual or any covariance.

If \(\gamma_p=0\), a lower pulse has no injection and remains zero.
An upper pulse at that time can affect its own current \(V\), but
its influence on later states is zero: the update coefficient is
zero and its lower F coefficient into all later queries is zero.
Chronological induction in (CT15)–(CT16) proves this assertion.
Thus retaining arbitrarily many zero slots changes neither the cap
nor the later coefficient rows.

The two programs are realized jointly using the same initialized
arrays and the common source construction III.F. The source
covariances, including cross-program entries, satisfy
\[
 \|\xi_i-\bar\xi_i\|_{L^p}
 =\|N(0,1)\|_{L^p}\|H^1_i-\bar H^1_i\|_2,\qquad
 \|\zeta_i-\bar\zeta_i\|_{L^p}
 =\|N(0,1)\|_{L^p}\|\Delta^{(2)}_i-\bar\Delta^{(2)}_i\|_2.
 \tag{CT17}
\]
This is subtraction of the two uncentered-input Gram covariances,
not a Lipschitz assertion about matrix square roots. To construct the
joint law one takes the finite union of the two programs.
The scalar expression of either branch depends only on its own
named slots and shared roots; extra calls in the other branch have
zero formal derivatives there. The cross covariances nevertheless
couple the two Gaussian lists. Their entire old source history is
present in (CT13)–(CT17). No source is refreshed at a splice or restart.

###### A.4. A horizon-independent reference raw anchor

The reference coefficients obey
\(\bar\gamma_{k1}=-\bar\gamma_{k2}\ge0\) and have total mass at most
\(L_*\). Remove zero steps and put \(h_k=2\bar\gamma_{k1}\).
The reference raw program is exactly feature Euler with total
feature length at most \(L_*\); physical pauses have disappeared.

Here is a proof of its uniform raw source cap. This also isolates
the anchor needed below; no nearby-law source estimate enters.
Let \(F'(w)=1/\phi'(w)\), and \(J_X=\phi'(J)\), \(J(0,g)=g\).
Feature clock Euler is
\[
 X_{a,k+1}=X_{a,k}+\tfrac12h_ky_aQ_{ka},\quad
 K_{k+1}=K_k+\tfrac12h_k\sum_ay_a\Delta^{(2)}_{ka}\otimes H^1_{ka},
 \quad c_{k+1}=c_k+\tfrac12h_k(H^2_{k1}-H^2_{k2}),
 \tag{CT18}
\]
with \(w_a=J(X_a,g_a)\), \(y_1=1,y_2=-1\).
Direct sums give \(\|c_k\|_\infty\le L_*\) and
\(\|K_k\|_{\rm HS}\le L_*^2/2\), hence a bounded action.
The lower-feature map has clock derivative norm at most one,
including a passive direction:
\[
 H^1(u)=\phi(u_1J(X_1,g_1)+u_2J(X_2,g_2)).
 \tag{CT19}
\]
Its derivative in \(X\) has components bounded by \(|u_j|\).

Subtract two clock programs after one fresh pulse.
The forward differences are bounded by the clock difference plus
the HS increment difference. The upper gate subtraction obeys
\[
 \|c\phi'(Z)-\bar c\phi'(\bar Z)\|_2
 \le\|c-\bar c\|_2+2L_*\|Z-\bar Z\|_2.
 \tag{CT20}
\]
Actual adjunction and the rank difference identity give a fixed
Lipschitz constant \(L_{\rm cl}<\infty\) for all three clock
velocities. Thus the post-pulse amplification is at most
\(E_{\rm cl}=e^{L_{\rm cl}L_*}\), uniformly in the mesh.
A reverse-answer pulse at old slot \(p\) changes the clock by at
most \(|\bar\gamma_p|\) times its RMS. A forward-answer pulse
changes its activation and gate, and hence all immediate updates,
by at most \(C|\bar\gamma_p|\) times its RMS. The readout supremum
and action bounds survive the forcing: the readout still updates
by bounded tanh functions and the middle updates have norm bounded
by their control mass times \(L_*\).
Consequently the later passive first-feature response and upper
backward response are at most \(C|\bar\gamma_p|\).

At each fixed graph, add a fresh standard Gaussian \(z\) at that
complete answer with amplitude \(q\), take the fixed-program width
limit first, and pair the observed difference with \(z\).
In its source expression, \(z\) occurs only as
\({\rm slot}+qz\); conditional Gaussian integration by parts yields
\(\mathbb E[zV^q]=q\mathbb E[\partial_{\rm slot}V^q]\).
The unforced output is independent of \(z\).
The fixed-graph source coefficients are continuous at zero forcing:
clip the root, use the bounded clock derivatives, retain the
bounded readout, and remove the clip by the finite causal
covariance-square-root argument in C.4.5.2.R5–R7.
Each fixed graph has a deterministic source-derivative bound
independent of the root clip. Hence its derivative expectations
converge. Taking \(q\to0\) after width gives
\[
 |\alpha^{\rm cl}_{ku,p}|+|\beta^{\rm cl}_{ku,p}|
 \le C|\bar\gamma_p|\quad(p<k),\qquad
 |\beta^{\rm cl}_{ku,ku}|\le2L_*.
 \tag{CT21}
\]
This proves a finite \(B_{\rm cl}\) for all prefixes through \(L_*\),
uniformly over passive queries and covariance rank.

Clock Euler converges to the globally existing reference feature
clock equation on \([0,L_*]\), by its bounded-set Lipschitz
comparison and the direct integral equation. The Gaussian source
isometry and (CT21) pass Gaussian-plus-bounded reverse-query
decompositions to this flow. Thus the actual reference feature flow
has active Gaussian tails on this compact feature segment, even
if its length exceeds the fitting endpoint.

Compare reference raw Euler with that existing flow using the
one-reference gradient cutoff estimate. Their discrepancy is
\(\eta_h\to0\) as the largest feature step tends to zero; only
reference-flow tails enter. Clock Euler has the same property.
Under a temporary cap on preceding raw source rows, transform a
raw first-coordinate step to its clock. Its exact defect is
\[
 R_h(w,b)=F(w+hb\phi'(w))-F(w)-hb
 =h^2b^2\phi'(w)^2
       \int_0^1(1-v)F''(w+vhb\phi'(w))\,dv,
 \tag{CT22}
\]
with \(b=y_aQ_a/2\). The elementary hyperbolic bounds give
\[
 |R_h|\le Ch^2b^2e^{2h|b|},\quad
 |\partial_pR_h|
 \le Ch^2e^{2h|b|}(1+h|b|)
       \{b^2|\partial_pw|+|b||\partial_pb|\}.
 \tag{CT23}
\]
The temporary-cap Gaussian decomposition and pulse estimates in
section 5 give all fixed moments of these factors. At the direct
injection step, division by its mass
\(|\bar\gamma_p|=h_s/2\) leaves a bound \(Ch_s\).
At later steps the normalized pulse is bounded in every fixed
moment. Since \(\sum_kh_k^2\le L_*h_{\max}\), the summed
normalized defect is at most \(C_Bh_{\max}\) in \(L^2\).
The summed undifferentiated defect has the same bound.

For completeness the transformed lower pulse recursion has
deterministic propagation
\[
 \chi_{k+1;p}
 =\chi_{k;p}+\sum_a\bar\gamma_{ka}e_a
 \left({\bf1}_{(k,a)=p}
    +\sum_{q\le k}D_{ka,q}J_q\chi_{t(q);p}\right)
    +\partial_pR_k,
 \tag{CT24}
\]
where \(J_q\) is the bounded clock derivative of its first feature.
Clock Euler has the same equation with the last term zero.
Its normalized pulses are pointwise bounded by
\(C\exp(CB_{\rm cl}L_*)\).
Differences of clock gates are \(O(\eta_h)\) in \(L^2\);
the D-row difference is the beta-row difference plus \(C\eta_h\).
Subtract (CT24), divide by \(|\bar\gamma_p|\), sum its defects,
and apply deterministic discrete Gronwall. Summing the resulting
alpha differences over source masses, and then subtracting the
upper equations (CT16), gives
\[
 E_k\le C_B\left(\eta_h+h_{\max}
                   +\sum_{j<k}h_jE_j\right).
 \tag{CT25}
\]
There is no current unknown on the right. Put \(B=B_{\rm cl}+1\);
choose \(h_{\max}\) so that Gronwall makes \(E_k\le1/2\).
At the first potentially failed raw row the past cap suffices
for (CT23)–(CT25), so that row cannot fail.
This proves a reference raw cap \(B_*<\infty\).
Because this argument is on feature length \(\le L_*\), its
constants do not depend on physical horizon or on pauses.
Extra zero-control directions have no past response, by section 3.

###### A.5. Temporary-cap moments and control transport

The estimates here are for arbitrary controlled raw programs,
not just the reference. Set \(M_0=\|A_0\|\le2\), \(L=L_*+1\), and restrict \(q\le1\).
The total absolute coefficient mass is at most \(L\).
Directly from (CT12),
\[
 \|c_k\|_\infty\le L,\quad
 \|K_k\|_{\rm HS}\le L^2/2,\quad
 \|A_k\|\le M_0+L^2/2,\quad
 \|w_k\|_2\le\sqrt2+(M_0+L^2/2)L^2/2.
 \tag{CT26}
\]
These bounds do not assume a cap. Under a temporary cap \(B\),
(CT13) gives
\[
 Q_{ku}=\zeta_{ku}+J_{ku},\qquad
 \mathbb E\zeta_{ku}^2\le L^2,\qquad
 |J_{ku}|\le D_B:=B+L^3.
 \tag{CT27}
\]
For \(Z=\sum_p|\gamma_p||Q_p|\), Jensen and the scalar Gaussian
exponential moment imply
\[
 \mathbb E e^{\lambda Z}
 \le2e^{\lambda LD_B+\lambda^2L^4/2},\qquad\lambda\ge0.
 \tag{CT28}
\]
It follows from (CT15) and \(1+x\le e^x\) that
\[
 \max_{j\le k}|v_{j;p}|
 \le|\gamma_p|\exp(D_BL+2Z).
 \tag{CT29}
\]
Thus all normalized pulses \(v_{\cdot;p}/m_p\) have all fixed
moments, with one common bound. The same holds for the barred
program. In particular
\[
 |\alpha_{ku,p}|\le C_B|\gamma_p|,\qquad
 |F_{ku,p}|\le C_B|\gamma_p|.
 \tag{CT30}
\]
From (CT16), the pointwise sum of the absolute U derivatives is
at most \(e^{C_BL^2}\); the corresponding C and V row sums are
bounded by \(C_B\). For a single old upper pulse, the direct
current V value has size at most \(2L\). Its first later C/F
terms have the factor \(|\gamma_p|\), and the remaining
propagation has total coefficient mass at most \(L\).
Consequently
\[
 |\beta_{ku,p}|\le C_B|\gamma_p|\quad(p<k),\qquad
 \sum_p|V_{ku;p}|+\sum_p|C_{k;p}|+\sum_p|U_{ku;p}|\le C_B.
 \tag{CT31}
\]
The last three bounds are pointwise. The first is deterministic.
These are the single-pulse and row-sum inductions of (CT16);
they do not require a positive lower bound for \(|\gamma_p|\).

Equations (CT27), (CT30), and (CT12) also give all fixed marginal
moments of \(Q,Z^2\) and the time maximum of \(|w|\).
For the latter, use
\(\sup_k|w_k|\le|g|+\sum_p|\gamma_p||Q_p|\).
For \(Z^2\), use its Gaussian source of variance at most one,
(CT30), and \(|\Delta^{(2)}|\le L\).
No \(L^p\) operator estimate beyond \(p=2\) is invoked.

**Raw proximity before the source bootstrap**

For the two programs on the same mesh let
\(d_k=\|\theta_k-\bar\theta_k\|_{(1)}\), the raw sum norm.
Every \(g_u\) has a common raw norm bound by (CT26).
The same-input gradient comparison is
\[
 \|g_u(\theta)-g_u(\bar\theta)\|_{(1)}
 \le C(1+R)d+C\tau_R(\bar Q(u))
 \tag{CT32}
\]
for \(R\ge L\). The upper gate uses bounded \(\bar c\), and
the only unbounded lower gate multiplier is \(\bar Q\).
This is the explicit split on \(|\bar Q|\le R\) and its
complement, followed by the rank difference identity.

Subtract updates as
\[
 \sum_j(\gamma_{kj}-\bar\gamma_{kj})g_{u_j}(\theta_k)
 +\sum_j\bar\gamma_{kj}
                  [g_{u_j}(\theta_k)-g_{u_j}(\bar\theta_k)].
 \tag{CT33}
\]
Only the second term needs tails, and only its two reference axes
occur. Section 4 therefore gives
\[
 \eta:=\max_kd_k\le\Phi(q_{\rm disc}),\qquad
 \Phi(q)\longrightarrow0\quad(q\downarrow0),
 \tag{CT34}
\]
uniformly in admitted meshes. Explicitly before cutoff choice the
bound is \(Ce^{C(1+R)L_*}(q_{\rm disc}+L_*e^{-cR^2})\).
Choose \(R\) proportional to \(\sqrt{\log(e/q_{\rm disc})}\);
at zero discrepancy both recursions are identical.
This proof uses no nearby-program source cap.

**The weighted beta-row comparison**

Define at the same passive output input
\[
 E_k=\sup_u\left(
 |\beta_{ku,ku}-\bar\beta_{ku,ku}|
 +\sum_{p<k}|\beta_{ku,p}-\bar\beta_{ku,p}|\right).
 \tag{CT35}
\]
We prove, under a cap on the preceding rows,
\[
 E_k\le C_B\left(
    \eta^{1/16}+q_{\rm disc}+\sum_{j<k}m_jE_j\right).
 \tag{CT36}
\]
Every constant in this estimate depends on \(B,L\), not on
physical horizon or the number of source slots.

Here are the complete product and mass estimates. Direct
forward/action subtractions and bounded readouts imply uniformly
at matched inputs
\[
 \|\mathrm d H^1\|_2+\|\mathrm d Z^2\|_2
 +\|\mathrm d\Delta^{(2)}\|_2+\|\mathrm d Q\|_2\le C\eta.
 \tag{CT37}
\]
The \(L^{24}\) bounds just proved, interpolated with (CT37), give
an \(L^{12}\) difference bound \(C_B\eta^{1/11}\) for \(w,Q,Z^2\).
For bounded gates their \(L^2\) difference and pointwise bound give
at least \(C_B\eta^{1/6}\). On \(\eta\le1\) each is bounded by
\(C_B\eta^{1/16}\). The explicit products below require at most
three \(L^{12}\) factors, followed by multiplication by an \(L^4\)
integrating factor. No bound on a maximum of query differences
or a larger-moment interpolation exponent is needed.

The D-row difference has the exact decomposition
\[
 \mathrm d D_{i,p}=\Delta\beta_{i,p}
 +{\bf1}_{p<i}\left[
   (\gamma_p-\bar\gamma_p)\mathbb E(\bar\Delta^{(2)}_i\bar\Delta^{(2)}_p)
    +\gamma_p\Delta\mathbb E(\Delta^{(2)}_i\Delta^{(2)}_p)\right].
 \tag{CT38}
\]
Thus its deterministic row sum is at most
\(E_k+C(q_{\rm disc}+\eta)\).

Subtract (CT15). Its linear propagation of the pulse difference
has coefficient at step \(j\) at most
\[
 D_B\sum_a|\gamma_{ja}|
      +2\sum_a|\gamma_{ja}||Q_{ja}|.
 \tag{CT39}
\]
The product of the resulting amplification factors has all fixed
moments by (CT28). Its forcing consists of exactly:
the direct injection difference \(\gamma_p-\bar\gamma_p\);
update coefficient differences; outside gate differences;
the difference of \(Q\); D-row differences (CT38); and the
inside past-gate differences.
An unchanged normalized barred pulse is bounded by the common
random envelope in (CT29). In the first-gate term, subtract
\(\phi''Qv\) as propagation plus
\((\mathrm d\phi'')\bar Q\bar v+\phi''(\mathrm d Q)\bar v\).
In its memory term subtract
\(\phi'\sum D\phi'_qv_q\) into propagation and the three
differences of its outside gate, D, and inside gate.
These exhaust every term.

After division by \(m_p\), the injection cost is \(e_p\).
Coefficient-change costs sum to \(C_Bq_{\rm disc}\), since
every such term is multiplied by \(|\gamma-\bar\gamma|\).
Field/gate costs are bounded by \(C_B\eta^{1/16}\) after
Hölder. For an inside-gate sum, take its \(L^p\) norm by
Minkowski before summing its deterministic D coefficients;
the D-row sum is bounded by \(D_B\).
No maximum of a gate difference over old source slots is taken.
The beta discrepancy cost is
\(C_B\sum_{j<k}m_jE_j\).
Multiplying by the random amplification (CT39) and using
Cauchy–Schwarz proves
\[
 \left\|\frac{\max_{i\le k}|v_{i;p}-\bar v_{i;p}|}{m_p}\right\|_2
 \le C_B\left(e_p+\eta^{1/16}+q_{\rm disc}
                              +\sum_{j<k}m_jE_j\right).
 \tag{CT40}
\]
The required product norms use at most a gate difference, a query,
and a normalized pulse. Their \(L^{12}\) bounds give \(L^4\)
forcing; (CT39) has an \(L^4\) bound, giving the asserted \(L^2\)
product. Coefficient-only and D-row terms require fewer factors.

Taking expected first-feature derivatives in (CT40), subtracting
the outside bounded gate, and summing over \(p\), gives
\[
 \sup_u\sum_{p<k}|\alpha_{ku,p}-\bar\alpha_{ku,p}|
 \le C_B\left(\eta^{1/16}+q_{\rm disc}
                              +\sum_{j<k}m_jE_j\right).
 \tag{CT41}
\]
Here \(\sum_pm_pe_p=q_{\rm disc}\) and
\(\sum_pm_p\le2L_*+1\). This is precisely where normalization by
the common source mass matters. The F-row difference has the same
bound, by (CT13), (CT37), and coefficient variation.

Set \(G_k=\eta^{1/16}+q_{\rm disc}+\sum_{j<k}m_jE_j\) and
\[
 W_k=\max_j\left\|\sum_p|V_{kj;p}-\bar V_{kj;p}|\right\|_2.
 \tag{CT42}
\]
The maximum is over output fields only; there is no random
maximum over Gaussian source history. Subtract (CT16):
\[
 \begin{aligned}
 \mathrm d U_{i;p}
 &=\sum_{q<i}(\mathrm d F_{i,q})\bar V_{q;p}
                 +\sum_{q<i}F_{i,q}\mathrm d V_{q;p},\\
 \mathrm d C_{k;p}
 &=\sum_{q<k}\bigl[
  (\gamma_q-\bar\gamma_q)\phi'(\bar Z_q^2)\bar U_{q;p}
  +\gamma_q\mathrm d\phi'(Z_q^2)\bar U_{q;p}
  +\gamma_q\phi'(Z_q^2)\mathrm d U_{q;p}\bigr],\\
 \mathrm d V_{i;p}
 &=\phi'(Z_i^2)\mathrm d C_{k;p}
       +\mathrm d\phi'(Z_i^2)\bar C_{k;p}
       +c_k\phi''(Z_i^2)\mathrm d U_{i;p}\\
 &\hspace{4mm}
       +\bigl[(c_k-\bar c_k)\phi''(\bar Z_i^2)
                    +c_k\mathrm d\phi''(Z_i^2)\bigr]\bar U_{i;p}.
 \end{aligned}                                                   \tag{CT43}
\]
The direct current U impulses cancel after pairing the distinguished
slots. Use (CT31)'s pointwise barred row bounds, (CT30)'s density
\(|F_{i,q}|\le C_Bm_q\), the coefficient mass bound, and
(CT37), then sum (CT43) over \(p\) and take \(L^2\).
The first line contributes \(C_BG_k+C_B\sum_{q<i}m_qW_{t(q)}\).
The second contributes its coefficient variation \(C_Bq_{\rm disc}\),
its gate variation \(C_B\eta\), and the same integrated U-row
discrepancy; exchanging two finite sums costs at most the total
mass \(2L_*+1\). The third line contributes \(C_B\eta\) and the
same two row errors. Therefore
\[
 W_k\le C_BG_k+C_B\sum_{j<k}m_jW_j.
 \tag{CT44}
\]
Discrete Gronwall in total mass, and monotonicity of \(G_k\), give
\(W_k\le C_BG_k\). A passive output obeys the same (CT43);
its past terms use the active \(W_j\), so its row difference has
the same bound. Taking expectations proves (CT36).
Its diagonal can also be checked directly from (CT14), with
an \(L^2\) difference at most \(C\eta\).

Everything used for the lower estimates at node \(k\) concerns
earlier Q rows. Its current alpha is then constructed; the upper
equations use only earlier V rows and that alpha.
Current \(Z^2\) moments follow from this new F-row and bounded
\(\Delta^{(2)}\), not from a presumed current beta cap.
Thus (CT36) is causal and is valid at the first potentially failed
current beta row.

The row functions extend continuously to all passive directions.
Indeed \(|\phi'(w\cdot u)u-\phi'(w\cdot v)v|
\le C(1+|w|)|u-v|\). Taking expectations against a normalized
lower pulse and using its \(L^2\) bound gives an alpha difference
at most \(C_B|\gamma_p||u-v|\). The contraction term has the
same bound, so the F-row has a summed Lipschitz bound.
In (CT16) the old V rows are unchanged when only the current
passive input varies; the changed F-row and the \(L^2\)-Lipschitz
current upper gates, multiplied by the pointwise old derivative
row bounds, give a beta-row Lipschitz estimate.
Thus a dense countable set of passive inputs suffices for the
common construction, with the asserted supremum supplied by
continuity. This makes no continuity claim for a random
supremum of Gaussian queries.

###### A.6. Closing the uniform cap

Choose \(B=B_*+1\), where section 4 supplied the reference raw cap.
At every preceding prefix satisfying that cap, (CT34) and (CT36)
give
\[
 E_k\le C_B e^{C_B(2L_*+1)}
                      \bigl(\Phi(q)^{1/16}+q\bigr).
 \tag{CT45}
\]
Choose \(\delta>0\) small enough that this is at most \(1/2\)
for \(q\le\delta\). The zero initial readout gives zero initial
beta rows. At the first potential failure the current row is
at most \(B_*+1/2<B\), a contradiction. This proves the
coefficient assertion of (CT7), including every old source slot.

Equation (CT27) then gives Gaussian tails: for \(R\ge2D_B\),
\(|Q|>R\) implies \(|\zeta|>R/2\), and integrating the scalar
Gaussian tail bounds
\(\mathbb E[(|\zeta|+D_B)^2{\bf1}_{|\zeta|>R/2}]\)
by \(Ce^{-cR^2}\). Taking a square root and reducing \(c\)
gives (CT7); enlarge \(M\) for \(1\le R<2D_B\) and for the
bounded readout. No independence of the bounded remainder and
the Gaussian part is needed.

Here \(\mathrm d X=X-\bar X\) denotes a comparison difference;
\(\Delta^{(2)}\) is the typed upper backward field.


###### A-supplement.4. Named-coefficient continuity in the reference raw anchor

The reference anchor (CT21)–(CT25) uses three different limits.
Their order matters:

- At a fixed clock Euler graph and nonzero fresh forcing,
  width tends to infinity.
- At that fixed graph the forcing tends to zero, after
  establishing continuity of its named coefficient.
- Only after a mesh-uniform coefficient bound has been
  proved is the clock/raw Euler mesh refined.

There is no assertion that zero-forcing continuity is uniform
over a growing graph. The finite pulse norm bound is uniform
in the mesh, which is the property used to obtain the final cap.

For the first limit, smoothly clip the Gaussian first roots
and use an inactive smooth readout clip equal to identity on
a neighborhood of the deterministic readout interval.
The clock coordinate map \(J(X,g)\) obeys
\[
 J_X=\phi'(J),\qquad
 J_g=\frac{\phi'(J)}{\phi'(g)}.
 \tag{A9}
\]
After clipping g both derivatives are bounded at each fixed
clip level. The passive first feature is
\(\phi(u_1J(X_1,g_1)+u_2J(X_2,g_2))\), whose source-relevant
X derivatives are bounded independently of the root clip.
Thus the contained finite Gaussian program and its source rule
apply to the clipped forced and unforced graphs.

At any fixed graph, all named source derivatives have a finite
deterministic envelope while previous selected coefficients
remain in a compact set. This follows inductively:
the lower clock feature derivatives are bounded, the upper
tanh derivatives are bounded, the readout is bounded by total
feature length, and each action answer is its source plus a
finite linear combination with fixed coefficients.
Root derivatives are never taken in this induction.

Now remove the root clip chronologically. Earlier second
moments converge, so the next finite covariance matrix
converges. Its nonnegative square root converges even at rank
loss, by bounded subsequences and uniqueness of a nonnegative
square root. Couple on a common finite standard Gaussian list.
Node values and source derivatives converge in probability.
The deterministic derivative envelope gives uniform
integrability of derivatives, so their expectations converge.
The same argument is uniform over forcing amplitudes in a
fixed compact interval at this fixed graph. In particular it
proves coefficient continuity at zero forcing.
This is the complete continuity mechanism used by
C.4.5.2.R5–R7, not continuity of a pseudoinverse.

The fresh root z remains independent of all centered source
groups in the scalar construction. The latter's selected
covariances may depend on forcing amplitude q, but are
deterministic and frozen under differentiation. The only
local root insertion is \({\rm slot}+qz\), so
\[
 \partial_zV^q=q\,\partial_{\rm slot}V^q,\qquad
 \mathbb E[zV^q]=q\,\mathbb E[\partial_{\rm slot}V^q].
 \tag{A10}
\]
This validates the source extraction even for a zero-variance
or duplicated source slot. The unforced value law alone would
not determine such a transverse derivative.

For the raw-to-clock step, transformed raw variables
\(F(w)\) are an analysis device, not extra instructions to
which the at-most-linear value theorem is applied.
At a fixed raw graph each \(w\) has a linear envelope in the
finite Gaussian root/source list; its named derivatives have
polynomial envelopes. Multiplication by \(F'(w)=\cosh^2w\)
therefore has finite moments at that fixed graph.
The uniform defect estimate CT23 is stronger: after cancellation
its only exponential is \(e^{2h|b|}\), with a capped Gaussian
query b. CT28–CT29 give its required fixed moments uniformly
over all prefixes under the temporary cap.
The direct injection step has size \(h_s\), so dividing its
defect by \(|\bar\gamma_p|=h_s/2\) leaves \(O(h_s)\).
All later defect sums use
\(\sum_kh_k^2\le L_*h_{\max}\).

The source comparison CT24–CT25 then uses only:
bounded clock gates, the deterministic clock-pulse envelope,
the raw/clock raw-state difference, D-row coefficient
differences, and the summed normalized defect.
The current alpha is obtained before current beta; its
right side uses only old raw Q rows. Thus the cap bootstrap
does not assume its current conclusion.

The contained III.F source/regularization proof and C.4.5.2 clipping/forcing
argument supply these fixed-graph constructions. No all-orders jet theorem
or uniform derivative convergence of finite GF is needed for this anchor.

##### Proof unit B. Endpoint conditioning and finite nonlinear learning

For the activity implication in this unit, let \(\tau_{ex}>0\) be a common
existence interval for (NS3); proof unit C constructs it. The endpoint
conditioning and continuity estimates do not assume that existence.

###### B.2. Endpoint conditioning, with a complete proof

The supplied C.4.5–C.4.6 facts used here are

\[
 \|A_\dagger\|\le M:=2+\sqrt{10},\quad
 \|c_\dagger\|_2\le C:=\sqrt{10},\quad
 \|c_\dagger\|_\infty\le H:=10,\quad
 \|w_\dagger\|_2\le W:=\sqrt2+\sqrt{10}.
 \tag{2.1}
\]

The endpoint predictor is 76-Lipschitz, vanishes at
`(e1+e2)/sqrt(2)`, and fits `(1,-1)`. Thus, on (NS1),

\[
 |f_\dagger(u_\alpha)|\le76/1216=1/16,
 \qquad 5/16\le y-f_\dagger(u_\alpha)\le11/16.
 \tag{2.2}
\]

In particular the added-law endpoint risk is at least `25/256`, even though
its contribution to the mixture risk is only `epsilon` times that number.

C.4.6.S40–S44 supplies one nonnegative random envelope `N`, with finite
`C_*`, such that on the reference feature segment

\[
 \|N\|_p\le C_*\sqrt p\ (p\ge2),\quad
 \sup_s|X_a(s)|\le5N,\quad
 F(w_a(s))=F(g_a)+X_a(s),\quad F'(z)=\cosh^2z,
 \tag{2.3}
\]

where `g1,g2` are independent standard normals. It also gives
`||Q_dagger(u)||_4<=L4:=2C_*` uniformly over every deterministic circle
input. Its countable-source construction and Fubini supply the simultaneous
active-clock bounds in (2.3). Independence of `N` and `g` is not asserted.

Here is the endpoint first-feature independence argument in full. Fix
`v in R2` with nonzero coordinates. Markov's inequality with
`p=(R/(eC_*))^2>=2` gives

\[
 \Pr(N>R)\le\exp[-R^2/(e^2C_*^2)].
\]

The Gaussian density gives

\[
 \Pr\{|g-rv|_\infty\le1\}
    \ge {2\over\pi}\exp[-(r|v|+\sqrt2)^2/2].
\]

For all sufficiently large `r` this exceeds `Pr(N>r^2)`, so their box
intersected with `{N<=r^2}` has positive probability. On that event put
`rho=min(|v1|,|v2|)/2`; for large `r`, `|g_a|>=rho r`. The minimum of
`F'` on `[g_a-1,g_a+1]` is at least `exp(2(|g_a|-1))/4>5r^2`.
Monotonicity of `F` in (2.3) therefore gives

\[
 \sup_s|w_a(s)-g_a|
    \le20r^2e^{-2(|g_a|-1)}\le20e^2r^2e^{-2\rho r}\longrightarrow0.
 \tag{2.4}
\]

If a finite pairwise distinct, nonantipodal list `u1,...,um` satisfied
`sum a_j tanh(w_dagger.u_j)=0` almost surely, choose such a `v` also
avoiding all lines `v.u_j=0`. On the preceding positive-probability events,
the features tend uniformly to `sign(v.u_j)`. Hence

\[
                   \sum_j a_j\operatorname{sign}(v\cdot u_j)=0.
 \tag{2.5}
\]

Cross the line perpendicular to any `u_k` on the circle of `v` directions.
The pairwise distinct, nonantipodal condition means no other sign changes there. Choose points
on both sides with nonzero coordinates, also when the crossing is on an axis.
Subtracting (2.5) gives `2a_k=0` up to orientation. Thus all `a_k=0`.
The features are linearly independent.

At the endpoint define

\[
 H^1(u)=\tanh(w_\dagger\cdot u),\quad Z^2(u)=A_\dagger H^1(u),
 \quad H^2(u)=\tanh Z^2(u),\quad
 \delta(u)=c_\dagger\operatorname{sech}^2Z^2(u),\quad
 Q(u)=A_\dagger^*\delta(u).
\]

The readout is nonzero since `<c_dagger,H2(e1)>=1`. Because `Z2(u)`
is finite almost surely and its gate is strictly positive, every `delta(u)`
is nonzero in L2. The raw gradient, at this or any admissible state, is

\[
 g_\theta(u)=\big(u\operatorname{sech}^2(w\cdot u)Q(u),
                    \delta(u)\otimes H^1(u),\ H^2(u)\big).
 \tag{2.6}
\]

For a finite list, if `lambda_H` is its first-feature Gram minimum eigenvalue,
then

\[
 \left\|\sum_i a_i\delta_i\otimes H_i^1\right\|_{HS}^2
    \ge\lambda_H\sum_i a_i^2\|\delta_i\|_2^2.
 \tag{2.7}
\]

Indeed at each second-layer coordinate apply the first-feature Gram
inequality to `sum_i a_i delta_i(omega2)H_i^1` and integrate. This also
identifies the integral with the tensor's Hilbert–Schmidt norm. Thus the
middle gradient blocks, hidden gradient blocks and full gradients are
independent. No injectivity of the trained action is assumed.

The first-feature Gram is continuous in the input list by the L2 Lipschitz
bound for tanh. The fields `delta(u)` are L2-continuous: first pass input
continuity through `w_dagger`, tanh and the bounded action, then use the
bounded fixed readout in (2.1). Their nonzero L2 norms therefore have a
positive minimum on the present compact input set. Define

\[
 \kappa:=\min_{\alpha\in I}\lambda_{\min}
     \big(\langle H^1(v_i),H^1(v_j)\rangle\big)_{i,j=1}^3
       \ \min_{\alpha\in I,\,i\le3}\|\delta(v_i)\|_2^2>0.
 \tag{2.8}
\]

Continuity of the minimum eigenvalue follows from the Rayleigh formula,
`|lambda_min(B)-lambda_min(D)|<=||B-D||`; a continuous positive function
on a compact set has positive minimum. This proves every positivity step
in (2.8). It is a precisely defined endpoint constant, not an evaluated
numerical lower bound.

Consequently the endpoint three-input middle Gram is at least `kappa I`.
The full anchor Gram `M_dagger` is at least `kappa I`. Let

\[
 d_\alpha=\Pi_\dagger g_\dagger(u_\alpha),\quad
 \beta_\alpha=M_\dagger^{-1}G_\dagger^*g_\dagger(u_\alpha),\quad
 t_\alpha=(-\beta_{\alpha,1},-\beta_{\alpha,2},1).
 \tag{2.9}
\]

Since `d=sum_i t_i g_dagger(v_i)` and `|t|>=1`, (2.7) implies

\[
 \|d_\alpha\|^2\ge\|d_{\alpha,H}\|^2
       \ge\|d_{\alpha,K}\|_{HS}^2\ge\kappa.
 \tag{2.10}
\]

The hidden block `H` consists of the first row and middle increment; the
`K` subscript means only the middle increment. The upper gradient bound is

\[
 \|g_\dagger(u)\|\le L_0:=\sqrt{1+C^2(1+M^2)}<17.
\]

Therefore `||d_alpha||<=L0`, `||G_dagger||<=G0:=sqrt(2)L0`, and

\[
 |t_\alpha|\le T_0:=\sqrt{1+2L_0^4/\kappa^2}.
 \tag{2.11}
\]

###### B.3. Quantitative gradient continuity from raw distance and endpoint L4 tails

This paragraph verifies input continuity and state continuity together. Put
`d=||theta-theta_dagger||_raw`, `h=|u-v|`, `rho=d+h<=1`. Here `A-A_dagger`
is measured in HS norm, hence also bounded in operator norm. Use endpoint
quantities at `v` as fixed factors. Successive subtraction gives

\[
 \|Z^1_\theta(u)-Z^1_\dagger(v)\|_2\le a_1\rho,
 \quad\|H^1_\theta(u)-H^1_\dagger(v)\|_2\le a_1\rho,
 \quad a_1=1+W,
\]

\[
 \|Z^2_\theta(u)-Z^2_\dagger(v)\|_2,
 \ \|H^2_\theta(u)-H^2_\dagger(v)\|_2\le a_2\rho,
 \quad a_2=1+Ma_1,
\]

\[
 \|\delta_\theta(u)-\delta_\dagger(v)\|_2\le a_\delta\rho,
 \quad a_\delta=1+2Ha_2,
\]

\[
 \|Q_\theta(u)-Q_\dagger(v)\|_2\le a_Q\rho,
 \quad a_Q=C+1+Ma_\delta.
 \tag{3.1}
\]

For the backward product split it as
`(c-c_dagger)phi'(Ztheta)+c_dagger[phi'(Ztheta)-phi'(Zdagger)]`.
This uses the bounded endpoint readout, not an unproved L-infinity smallness
of the evolving readout difference. For the adjoint split use the current
backward field, whose L2 norm is at most `C+1`, in the changed-action term.

The only additional row product is a changed first gate times the fixed
endpoint `Q_dagger(v)`. For gates `b=phi'(z)-phi'(z0)`,
`|b|<=min(1,2|z-z0|)` implies

\[
 \|b\|_4\le\sqrt2\|z-z_0\|_2^{1/2},\qquad
 \|bQ_\dagger(v)\|_2\le\sqrt{2a_1}L_4\rho^{1/2}.
 \tag{3.2}
\]

This is Holder's inequality and the proved endpoint L4 bound. It does not
multiply two uncontrolled L2 increments. Also
`||Q_theta(u)||2<=(M+1)(C+1)=:Q1`. Subtracting the explicit input vector
in the row gradient, the middle rank factors and the final hidden value gives

\[
 \|g_\theta(u)-g_\dagger(v)\|\le C_g\rho^{1/2},
\]

\[
 C_g=Q_1+a_Q+a_\delta+Ca_1+a_2+\sqrt{2a_1}L_4.
 \tag{3.3}
\]

The raw Hilbert norm is bounded above here by the sum of its three component
norms. This proves uniform endpoint state/input continuity, including that
of `beta_alpha`, `t_alpha`, and `d_alpha` in (2.9). No input derivative of a
query is required.

At fixed `u`, prediction subtraction also gives

\[
 |f_\theta(u)-f_\dagger(u)|\le C_f d,
 \qquad C_f=1+Ca_2,
 \tag{3.4}
\]

uniformly on the circle. The scalar differentiation formula (2.6) along
strongly C1 raw curves follows from the strong L2 chain rule: for a fixed
direction the tanh difference quotient is dominated by its L2 direction,
and the error of replacing a C1 increment by that direction is controlled
by the one-Lipschitz activation. Differentiating the bounded action product
and the scalar readout pairing gives the three blocks in (2.6). Bounded
multiplier convergence against fixed L2 fields proves their continuity.
Explicitly, if bounded multipliers `b_k` converge in probability to `b`,
split a fixed `q in L2` at `|q|=R`. The bounded part of
`||(b_k-b)q||2` tends to zero by bounded convergence in probability; its
tail is at most `2 sup_k||b_k||infty ||q 1_(|q|>R)||2`. Let `k` grow
first and then `R` grow. Applying this fact successively to the fixed-state
backward and row factors proves continuity at any state, without requiring
an L4 bound at that state.
An ambient Frechet derivative of an L2-valued hidden map is not used.

For explicit projector estimates set

\[
 a_G=\sqrt2 C_g,\quad G_1=G_0+a_G,\quad
 a_M=(2G_0+a_G)a_G.
\]

Then `||G_theta-G_dagger||<=a_G sqrt(d)` and
`||M_theta-M_dagger||<=a_M sqrt(d)`. If
`a_M sqrt(d)<=kappa/2`, the Rayleigh formula gives
`M_theta>=kappa I/2`, and the inverse identity yields

\[
 \|M_\theta^{-1}-M_\dagger^{-1}\|
       \le(2a_M/\kappa^2)\sqrt d.
\]

Expanding the three changed factors in `G M^-1 G*` proves

\[
 \|\Pi_\theta-\Pi_\dagger\|\le C_\Pi\sqrt d,
 \quad C_\Pi={2a_GG_1\over\kappa}
       +{2G_0a_MG_1\over\kappa^2}+{G_0a_G\over\kappa}.
 \tag{3.5}
\]

Writing `d_theta,alpha=Pi_theta g_theta(u_alpha)`, it follows that

\[
 \|d_{\theta,\alpha}-d_\alpha\|\le C_d\sqrt d,
 \qquad C_d=C_g+C_\Pi L_0.
 \tag{3.6}
\]

All constants are uniform over (NS1).

###### B.4. The hidden contrast and its derivative along the reached path

Keep the endpoint readout and coefficients fixed during the episode:

\[
 O_\alpha(\theta)=\sum_{i=1}^3 t_{\alpha,i}
                 \langle c_\dagger,H^2_\theta(v_i)\rangle.
 \tag{4.1}
\]

This functional depends only on hidden parameters. Its raw gradient is
`o_alpha(theta)=(sum_i t_i h_i^fixed(theta),0)`, where `h_i^fixed` is the
first-row/middle portion of (2.6) with the readout set to `c_dagger`.
The proof is the strong curve chain rule just given, with a fixed bounded
readout in the scalar pairing. In particular

\[
 o_\alpha(\theta_\dagger)=(d_{\alpha,H},0),\qquad
 \|o_\alpha(\theta)-o_\alpha(\theta_\dagger)\|
       \le C_o\sqrt d,\quad C_o=\sqrt3T_0 C_g.
 \tag{4.2}
\]

For the last inequality apply (3.3) to the auxiliary state `(w,A,c_dagger)`
and sum its three hidden-gradient differences using
`sum|t_i|<=sqrt(3)|t|`. Thus derivative continuity of this hidden contrast
uses only raw distance and fixed endpoint L4 tails, even if the evolved
query field is known only through the constructed source-regular flow.

The field in (NS3) is continuous on the neighborhood under consideration:
(3.3) and its fixed-state bounded-multiplier proof give gradient continuity,
and (3.5) gives inverse/projector continuity. A raw-continuous solution of
the strong integral equation therefore has a continuous raw derivative.
Its two hidden maps are strongly C1 by the chain rule above. Consequently

\[
 {d\over d\tau}O_\alpha(\theta(\tau))
       =\langle o_\alpha(\theta(\tau)),V_{\alpha,y}(\theta(\tau))\rangle.
 \tag{4.3}
\]

At the endpoint, writing `r_dagger=f_dagger(u_alpha)-y`, (2.2) and (2.10)
give the uniform strictly positive value

\[
 O_\alpha'(0)=-2r_\dagger\|d_{\alpha,H}\|^2\ge5\kappa/8.
 \tag{4.4}
\]

This explicitly checks hidden representation motion. A nonzero hidden
parameter block is only the input to the identity, not its conclusion.

For a quantitative derivative modulus put

\[
 L_1=\sqrt{1+(C+1)^2(1+(M+1)^2)},\quad
 R_1=C+1+5/8,\quad V_1=2R_1L_1.
\]

On the unit raw ball and the invertible-Gram region, `||g_theta(u)||<=L1`,
`|f_theta(u_alpha)-y|<=R1`, and `||V_alpha,y(theta)||<=V1`, because
an orthogonal projector has norm at most one. Equations (3.4) and (3.6) give

\[
 \|V_{\alpha,y}(\theta)-V_{\alpha,y}(\theta_\dagger)\|
      \le C_V\sqrt d,
 \quad C_V=2C_fL_1+(11/8)C_d.
\]

Use (4.2), `||o_alpha(theta_dagger)||<=L0`, and the last bound in (4.3):

\[
 |O_\alpha'(\theta)-O_\alpha'(\theta_\dagger)|
       \le A_O\sqrt d,
 \qquad A_O=C_oV_1+L_0C_V.
 \tag{4.5}
\]

Here `O'(theta)` means its derivative in the actual field (NS3), not a
derivative of a frozen trajectory. This estimate supplies uniform
continuity along all the reached paths in the family.

###### B.5. A uniform, finite nonlinear episode

Choose the following positive raw radius:

\[
 \rho_0=\min\left\{1,\left({\kappa\over2a_M}\right)^2,
             {\kappa\over4C_d^2},\ {5\over32C_f},
             \left({5\kappa\over16A_O}\right)^2\right\}>0.
 \tag{5.1}
\]

Every denominator is finite and positive by its displayed definition. Let

\[
 \tau_0=\min\{\tau_{ex}/2,\rho_0/(2V_1)\}>0.
 \tag{5.2}
\]

Before a possible first exit from the raw ball of radius `rho0`, the
velocity bound `V1` gives `||theta(tau)-theta_dagger||<=V1 tau`.
If that first exit occurred by `tau0`, this distance would be at most
`rho0/2`, a contradiction. Thus all paths stay in the ball through `tau0`.
The Gram is at least `kappa I/2` there. This is a first-exit estimate for the
existing nonlinear equation, not a conclusion from the initial linear term.

Since `G_theta^*Pi_theta=0`, the chain rule applied to the two anchors proves
the anchor assertion. The choices in (5.1), (2.2), and (3.6) give throughout the interval

\[
 |r(\tau)|\ge5/32,\qquad r(\tau)<0,\qquad
 \|d_{\theta(\tau),\alpha}\|^2\ge\kappa/4.
 \tag{5.3}
\]

The exact added prediction and risk identities are

\[
 f_\theta(u_\alpha)'=-2r\|d_{\theta,\alpha}\|^2,\qquad
 (r^2)'=-4r^2\|d_{\theta,\alpha}\|^2.
 \tag{5.4}
\]

They retain every moving hidden field and the recomputed projector. Integrating
(5.3)–(5.4) gives (NS6) with

\[
 \eta_R={25\kappa\over1024}\tau_0>0,
 \qquad f_{\theta(\tau_0)}(u_\alpha)-f_\dagger(u_\alpha)
                        \ge {5\kappa\over64}\tau_0>0.
 \tag{5.5}
\]

By (4.4)–(4.5) and (5.1), `O_alpha'(theta(tau))>=gamma_O:=5kappa/16`.
Hence `Delta O_alpha>=gamma_O tau` for `0<=tau<=tau0`. Cauchy–Schwarz,
first in the second population and then in the three coefficients, yields

\[
 |\Delta O_\alpha|^2
 \le\|c_\dagger\|_2^2|t_\alpha|^2
             \sum_{i=1}^3\|\Delta H_i^2\|_2^2
 \le30T_0^2 J_{2,\alpha,y}(\tau).
 \tag{5.6}
\]

Thus (NS7) holds with the explicit positive constant

\[
 \eta_H={\gamma_O^2\tau_0^2\over30T_0^2}>0.
 \tag{5.7}
\]

This finite episode has actual upper hidden activation displacement. Its
proof uses derivative continuity of a scalar hidden contrast to retain a
strict sign over a finite interval; it does not extrapolate the initial
velocity as the finite trajectory. The interval and margins have no
`epsilon` dependence.

The whole-circle map is
`P_(alpha,y)(tau,sqrt(2)u)=<c(tau),tanh(A(tau)tanh(w(tau).u))>`.
It is jointly continuous in time and input and has a uniformly bounded input
Lipschitz constant on this episode, since it is bounded by
`||c||2 ||A||op ||w||2`. Equation (3.4) gives a uniform whole-circle
comparison to the endpoint on the local ball. This defines the prediction
to be captured; Its original-mixture identification is proved in proof unit C.

##### Proof unit C. Original-initialization continuation and slow selection

###### C.1. State and source interface

Use the state and initialized carrier in (NS2), and write its raw increment
space as \(\mathcal E\). Throughout this unit inputs in \(f_\theta(u)\)
are normalized; the reconstructed physical prediction is evaluated at
\(x=\sqrt2u\). For clarity the fields used in the comparisons are
\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad H^2(u)=\phi(Z^2(u)),
 \quad f_\theta(u)=\langle c,H^2(u)\rangle,
\]
\[
 \Delta^{(2)}(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\Delta^{(2)}(u),\quad
 g_u=(\phi'(w\cdot u)Q(u)u,\Delta^{(2)}(u)\otimes H^1(u),H^2(u)).\tag{1}
\]
The scalar prediction is continuously differentiable in the raw metric by
the contained scalar-gradient argument in A.4. Set
\[
 p=(\alpha,y)\in\mathcal P=I\times[3/8,5/8],\qquad
 I=[\pi/4-1/1216,\pi/4+1/1216].\tag{2}
\]
All constants below are uniform in this compact box. The reference feature
curve is exactly
\[
 \theta_s=\tfrac12g_{e_1}(\theta)-\tfrac12g_{e_2}(\theta),\tag{3}
\]
and C.4.5 proves the raw endpoint and residual bounds
\[
 \|\theta_*(t)-\theta_\dagger\|_{\rm raw}\le\sqrt{10}e^{-t/5},
 \qquad |r_*(t)|\le\sqrt2 e^{-t/5}.\tag{4}
\]
Its physical control is \(a_*=(e_*,-e_*,0)\), with total absolute mass
\(s_\dagger\le10\). For the three inputs \(e_1,e_2,u_\alpha\), raw Euler is
\[
 \theta_{k+1}=\theta_k+\sum_{j=1}^3\gamma_{kj}g_{u_j}(\theta_k).\tag{5}
\]
Let SCT denote the source estimate of proof unit A: there are uniform
\(\delta_{\rm src},h_{\rm src}>0\) and \(B_{\rm src}<\infty\) for all
such finite histories satisfying
\[
 \int|a(t)-a_*(t)|_1dt<\delta_{\rm src}.\tag{6}
\]
The mesh is measured by \((|a|_1+|a_*|_1)dt\). Every passive backward row,
including its distinguished current source and all old training sources,
then has the stated cap. Deterministic feedback coefficients are frozen
under named differentiation, just as in (CT12)–(CT16).

The physical reference keeps running after every finite prefix. A prefix
through \(b\) followed by appended controls has distance at most the
appended absolute mass plus \(s_\dagger-s_*(b)\), including a zero extension
after the episode. This supplies the endpoint interface without a source
reset. All subsequent constructions use this exact full-history condition.

###### C.2. Consequences of SCT and the one-reference modulus

Write \(L=\sum_{k,j}|\gamma_{kj}|\). Under (6),
\(L\le10+\delta_{\rm src}\). The elementary controlled updates give

\[
 \|c\|_\infty\le L,\quad \|K\|_{\rm HS}\le L^2/2,\quad
 \|A\|_{\rm op}\le2+L^2/2,\quad
 \|w\|_2\le\sqrt2+L^2+L^4/8.
 \tag{7}
\]

Indeed the readout increases by at most the current control mass, the middle
increment by at most that mass times the preceding readout bound, and the
row increment by at most that mass times the action/readout bounds.
Summing is bounded by the corresponding integrals in accumulated mass.
Harmless enlarged constants also cover affine interpolants and unequal
simultaneous updates. None depends on physical elapsed time.

The exact source identity C.4.7.N5 is
\(Q_{kv}=\zeta_{kv}+\sum_qD_{kv,q}H^1_q\). Its learned coefficient row has
absolute sum at most \(L\sup\|c\|_\infty^2\); its response row is bounded by
SCT. Also \(\mathbb E\zeta_{kv}^2\le\sup\|c\|_\infty^2\). Thus

\[
 Q_{kv}=\zeta_{kv}+J_{kv},\quad |J_{kv}|\le C,\quad
 \operatorname{Var}(\zeta_{kv})\le C^2,
 \qquad \tau_R(Q_{kv})\le C e^{-cR^2}\quad(R\ge1).
 \tag{8}
\]

The last estimate follows by splitting at \(R>2C\), using
\(\{|Q|>R\}\subset\{|\zeta|>R-C\}\), and integrating the scalar Gaussian
tail; enlarging the constant covers the remaining \(R\). It requires no
independence of \(J\) and \(\zeta\). In particular

\[
 \sup_{k,v}\|Q_{kv}\|_p\le C_p<\infty\qquad(2\le p<\infty).
 \tag{9}
\]

These are separate deterministic input/time bounds, not a moment bound for
an uncountable coordinate supremum.

For two raw states \(\theta,\bar\theta\) on a common bounded raw/action region,
use the equivalent sum distance \(d\). Suppose only the comparison endpoint
\(\bar\theta\) has \(\|\bar c\|_\infty\le C\) and the tails (8).
Subtract the factors in (1). The upper subtraction is

\[
 \Delta^{(2)}-\bar\Delta^{(2)}=(c-\bar c)\phi'(Z^2)
                +\bar c[\phi'(Z^2)-\phi'(\bar Z^2)].
\]

It costs \(Cd\), as do \(Q-\bar Q\) and the middle/readout blocks.
The remaining lower product is bounded by

\[
 \|[\phi'(w\cdot v)-\phi'(\bar w\cdot v)]\bar Q(v)\|_2
 \le 2R\|w-\bar w\|_2+2\tau_R(\bar Q(v)).
 \tag{10}
\]

Changing the input adds \(C|v-\bar v|\) to the forward and upper differences;
apply (10) also to the lower gate with
\(\|w\cdot v-\bar w\cdot\bar v\|_2\le
\|w-\bar w\|_2+\|\bar w\|_2|v-\bar v|\).
Consequently

\[
 \|g_v(\theta)-g_{\bar v}(\bar\theta)\|_{\rm raw}
 \le C(1+R)(d+|v-\bar v|)+C e^{-cR^2}.
 \tag{11}
\]

Only the comparison state's tails appear. Its readout supremum is likewise
the only readout supremum used in this subtraction. An arbitrary competing
strong raw solution therefore need not satisfy a new tail assumption.

For \(0<z\le1\), set
\(\omega(z)=z\sqrt{\log(e/z)}\), and extend it increasingly at larger \(z\).
Choosing \(R\) proportional to \(\sqrt{\log(e/z)}\) in (11) gives the
one-reference bound \(C\omega(z)\). The function is increasing on \((0,1]\),
and

\[
 \int_{0+}\frac{dz}{\omega(z)}=\infty.
 \tag{12}
\]

The following explicit comparison will be used repeatedly. If
\(D(t)\le\eta+C\int_0^t\omega(D(s))ds\), then, while the right side stays
below one,

\[
 D(t)\le {\cal O}_t(\eta):=
 e\exp\!\left[-\left(\sqrt{\log(e/\eta)}-Ct/2\right)^2\right].
 \tag{13}
\]

To prove it, put \(Z(t)=\eta+C\int_0^t\omega(D(s))ds\). Monotonicity gives
\(Z'\le C\omega(Z)\), and
\((\sqrt{\log(e/Z)})'\ge-C/2\). Integrate. For \(\eta=0\), replace it by a
positive number and let that number decrease to zero. For every fixed
bounded interval, \({\cal O}_t(\eta)\to0\) uniformly as \(\eta\to0\).
A first-exit argument validates staying below one when the initial error
is sufficiently small.

###### C.3. Endpoint conditioning and constrained coefficients

Let \(G(\theta):\mathbb R^2\to\mathcal E\) have columns \(g_{e_1},g_{e_2}\).
The endpoint Gram \(M_\dagger=G(\theta_\dagger)^*G(\theta_\dagger)\) is strictly
positive. This follows from proof unit B.

By joint raw gradient continuity there are \(\rho>0,\kappa>0\) such that on

\[
 {\cal N}=\{\|\theta-\theta_\dagger\|_{\rm raw}<\rho\}
 \quad\text{one has}\quad M(\theta):=G^*G\ge4\kappa I_2.
 \tag{14}
\]

Shrink \(\rho\) once and retain an interior ball for all constructed paths.
The neighborhood has bounded raw/action norms, although it need not have
bounded readout supremum. The latter bound comes from controls, not (14).
Put

\[
 B(\theta)=G(\theta)M(\theta)^{-1},\quad
 \Pi(\theta)=I-G(\theta)M(\theta)^{-1}G(\theta)^*,
\]
\[
 r_p(\theta)=f_\theta(u_\alpha)-y,\quad
 v_p(\theta)=r_p(\theta)g_{u_\alpha}(\theta),\quad
 V_p(\theta)=-2\Pi(\theta)v_p(\theta).
 \tag{15}
\]

The inverse in (15) is an ordinary two-by-two matrix inverse. The coefficients
are bounded and continuous on a slightly smaller raw neighborhood, uniformly
in \(p\). In particular

\[
 V_p(\theta)=\sum_{j=1}^3a_j(\theta,p)g_{u_j}(\theta),
 \quad (a_1,a_2)^T=2r_p M^{-1}G^*g_{u_\alpha},\quad a_3=-2r_p,
 \quad |a|_1\le A.
 \tag{16}
\]

The scalar prediction is Lipschitz on bounded raw/action sets. Equations
(11), the identity
\(M^{-1}-\bar M^{-1}=M^{-1}(\bar M-M)\bar M^{-1}\), and the bounded Gram
factors therefore give

\[
 \|V_p(\theta)-V_{\bar p}(\bar\theta)\|_{\rm raw}
 \le C\omega(d(\theta,\bar\theta)+|p-\bar p|)
 \tag{17}
\]

when \(\bar\theta\) is a tail-bearing constructed state. The same estimate
holds for the coefficient vector in (16). It does not assert an ambient
locally Lipschitz field.

###### C.4. Construction from reference prefixes, tails, and uniqueness

Choose reference physical prefixes ending at \(b_m\uparrow\infty\), with
sufficiently fine finite raw Euler approximations using exact integrated
reference controls. Their terminal states
\(\theta_m^0\) converge in raw norm to \(\theta_\dagger\), by the established
reference construction, or by (11)--(13) and SCT. Their controls approximate
the fixed reference controls on that prefix. Immediately after \(b_m\),
append the explicit Euler recursion on an interval of length \(\tau_0\)

\[
 \theta^{m,h}_{k+1}=\theta^{m,h}_k+h_k V_p(\theta^{m,h}_k).
 \tag{18}
\]

Choose once a positive \(\tau_0\) so small that

\[
 A\tau_0<\delta_{\rm src}/8,\qquad
 \tau_0\sup_{{\cal N},p}\|V_p\|_{\rm raw}<\rho/8.
 \tag{19}
\]

Take \(m\) large enough that the prefix state error is below \(\rho/8\),
its control approximation error is below \(\delta_{\rm src}/8\), and the
omitted suffix has mass below \(\delta_{\rm src}/8\). The bound on (18)'s
accumulated speed keeps all its nodes strictly inside \({\cal N}\); the
controls (16) are legitimate throughout. Equations (19) keep the entire
history strictly inside the SCT tube. Decrease its maximal control mesh
as necessary. This proves admissibility before using the tail conclusion.

Compare two appended Euler interpolants. Their preceding-node distance is
at most their current distance plus \(C(h+h')\). Equation (17), with (8)
at the comparison nodes, bounds their velocity difference by the Osgood
modulus of that quantity, plus the parameter discrepancy. Integrating and
using (13) shows they are Cauchy in \(C([0,\tau_0];\mathcal E)\), uniformly in
\(p\), as their prefix errors and meshes tend to zero. The limit is independent
of those choices. One may first use a countable dense parameter/mesh family
and its finite unions on the prescribed carrier, then extend by the same
uniform estimate; no uncountable family of independent carriers is chosen.

The joint continuity of (1) and (15) passes (18)'s integral equation to

\[
 \bar\theta_p(\tau)=\theta_\dagger+
             \int_0^\tau V_p(\bar\theta_p(s))\,ds.
 \tag{20}
\]

The convergence of the integrands is uniform: otherwise choose discrepant
times and parameters, extract a convergent parameter/time subsequence, and
apply continuity at the limiting state. Thus (20) is strongly \(C^1\), jointly
continuous in \(p,\tau\), and has one-sided derivatives at the endpoints.
All coefficients are computed from the current full state, the fixed atom,
and the retained initialized action. The reference prefix is an approximation
of its already specified initial state, not a pretraining stage imposed on
the changed-law optimizer.

The Gaussian tails survive this construction. Raw convergence gives
\(Q_m(v)\to Q(v)\) in \(L^2\), uniformly over compact parameter/time/input sets,
by bounded-multiplier continuity and compactness. For fixed \(R\),
\(q\mapsto(|q|-R)_+\) is \(L^2\)-Lipschitz and

\[
 \tau_{2R}(Q)\le2\|(|Q|-R)_+\|_2.
 \tag{21}
\]

Pass (8) through this continuous positive-part norm; (21) gives
\(\tau_R(Q)\le C e^{-c'R^2}\) with enlarged constants. Similarly
\(\|c\|_\infty\le10+\delta_{\rm src}\) passes through an almost-everywhere
subsequence. All moments (9), particularly \(L^4\) and \(L^8\), follow.
Interpolation between \(L^2\) convergence and the uniform \(L^8\) bounds
makes the query maps jointly continuous into \(L^4\).

Uniqueness requires tails only on this constructed path. If another strong
solution of (20) on the same carrier starts at \(\theta_\dagger\), compare it
with \(\bar\theta_p\) using (17) and (13). On their initial common
neighborhood the initial error is zero, so they coincide. Repeating at the
end of a common subinterval proves equality through \(\tau_0\); an earlier
exit would contradict the constructed path's strict interior bound.
The same argument proves uniqueness from every reached state on the remaining
interval. No arbitrary-state existence assertion is made.

Since the scalar predictions are \(C^1\), (20) gives
\(\partial_\tau(f(e_1),f(e_2))=G^*V_p=0\). Both anchors are fitted exactly
throughout. The whole-circle determining prediction is

\[
 P_p(\tau,\sqrt2v)=
 \langle\bar c_p(\tau),
  \phi((A_0+\bar K_p(\tau))\phi(\bar w_p(\tau)\cdot v))\rangle.
 \tag{22}
\]

The full hidden state evolves in (20). Formula (22) is not a prediction-only
closure or a frozen kernel.

###### C.5. Strong activation derivatives and absolute continuity of B

These derivative statements concern controlled reached curves, not arbitrary
ambient directions. Let a reached raw curve solve

\[
 \theta'(t)=\sum_{j=1}^3a_j(t)g_{u_j}(\theta(t)),\qquad
 m(t)=\sum_j|a_j(t)|\in L^1,
 \tag{23}
\]

and assume the uniform query tails and readout bounds just proved. All constants
below depend only on those reached bounds and the anchor gap.
The first component of (1) gives
\(\|w'(t)\|_4\le C m(t)\). Also
\(\|K'(t)\|_{\rm HS}+\|c'(t)\|_2\le C m(t)\) and the pointwise readout
formula gives \(|c'(t,\omega_2)|\le m(t)\).
Hence, for every deterministic passive input \(v\),

\[
 (H^1(v))'=\phi'(w\cdot v)\,w'\cdot v,\qquad
 (Z^2(v))'=K'H^1(v)+A[\phi'(w\cdot v)\,w'\cdot v],
\]
\[
 (H^2(v))'=\phi'(Z^2(v))(Z^2(v))',\qquad
 \Delta^{(2)}(v)'=c'\phi'(Z^2(v))+c\phi''(Z^2(v))(Z^2(v))',
\]
\[
 Q(v)'=K'^*\Delta^{(2)}(v)+A^*\Delta^{(2)}(v)'.
 \tag{24}
\]

These are strong \(L^2\) absolutely continuous identities and
\(\|Q(v)'\|_2+\|\Delta^{(2)}(v)'\|_2\le Cm(t)\). A direct justification, which
also covers merely integrable controls, is to choose the coordinatewise
absolutely continuous representatives supplied by Fubini, apply the scalar
chain rule almost everywhere, and integrate the displayed \(L^2\)-integrable
derivatives. The uniform pointwise bound on \(c\) handles its product with
\((Z^2)'\). This argument needs no \(L^\infty\) Banach-space derivative of c.

Differentiate the three blocks of (1) along (23):

\[
 (g_v)'_w=
 \{\phi''(w\cdot v)(w'\cdot v)Q(v)+\phi'(w\cdot v)Q(v)'\}\,v,
\]
\[
 (g_v)'_K=\Delta^{(2)}(v)'\otimes H^1(v)+\Delta^{(2)}(v)\otimes(H^1(v))',
 \qquad (g_v)'_c=(H^2(v))'.
 \tag{25}
\]

The only additional unbounded product is the first term in (25). Hölder gives

\[
 \|(w'\cdot v)Q(v)\|_2\le\|w'\|_4\|Q(v)\|_4\le Cm(t).
 \tag{26}
\]

All other terms are controlled by (24), bounded gates, and the rank norm
identity. Thus each anchor gradient is absolutely continuous in raw norm and
\(\|G'(t)\|_{\mathrm{op}}\le Cm(t)\).
The same coordinatewise argument, now using (26), proves the fundamental
theorem for (25); it is not a formal ambient Hessian calculation.

Ordinary finite-matrix absolute continuity and (14) now yield

\[
 M'=G'^*G+G^*G',\qquad
 B'=G'M^{-1}-GM^{-1}M'M^{-1},\qquad
 \|B'\|_{\mathrm{op}}\le Cm(t).
 \tag{27}
\]

Along (20), the coefficients (16), the query \(L^4\) continuity, and bounded
multiplier continuity show that its row velocity is jointly \(L^4\)-continuous
in \((p,\tau)\). Equations (24) show that the strong activation derivatives
are jointly \(L^2\)-continuous in \((p,\tau,v)\), including \(\tau=0\).
For example the multiplier difference is applied to one fixed limiting
velocity, and its varying velocity is subtracted first; compactness makes
this argument uniform. Consequently

\[
 H^2_{\bar\theta_p(\tau)}(v)
 =H^2_{\theta_\dagger}(v)+
   \tau\,D H^2_{\theta_\dagger}(v)[V_p(\theta_\dagger)_h]
   +o_{L^2}(\tau)
 \tag{28}
\]

uniformly on compact parameter/input sets. The derivative is the strong
curve derivative in (24). This is the uniform derivative fact needed for the
paired hidden-activation margin in proof unit B.

###### C.6. Actual original-mixture continuation in the control tube

For an existing reached mixture segment set
\(r=(f(e_1)-1,f(e_2)+1)\). The exact equations, with the two anchor weights
included, are

\[
 \theta'=-(1-\varepsilon)Gr-2\varepsilon v_p,\qquad
 r'=-(1-\varepsilon)Mr-2\varepsilon G^*v_p.
 \tag{29}
\]

The controls in (23) are
\((-(1-\varepsilon)r_1,-(1-\varepsilon)r_2,-2\varepsilon r_p)\).
On the bounded conditioned region, for \(0<\varepsilon\le1/2\),

\[
 |r(t)|\le e^{-2\kappa(t-b)}|r(b)|+C\varepsilon,\qquad
 \int_b^t|r(s)|ds\le C|r(b)|+C\varepsilon(t-b).
 \tag{30}
\]

Indeed pair the residual equation with \(r/|r|\) away from zero, use
\(M\ge4\kappa I\), and bound \(G^*v_p\). Regularization by
\(\sqrt{|r|^2+\eta^2}\) and \(\eta\downarrow0\) covers zero residuals.
In particular the post-b control mass and raw displacement are at most

\[
 \int_b^t m(s)ds+
 C^{-1}\|\theta(t)-\theta(b)\|_{\rm raw}
 \le C|r(b)|+C\varepsilon(t-b).
 \tag{31}
\]

Here and below constants may be enlarged; the sum form of (31) is only an
upper bound, not an equality.

The next two discrete steps construct that existing segment before using
its continuous estimates. In particular (30) is not used to assume the
existence it is meant to control.

**Fixed b prefix, before any changed-program cap**

Every finite raw Euler program for the three-atom mixture exists by finite
recursion. Through a separately fixed b, its elementary readout recurrence
gives \(\|c_k\|_\infty\le e^{2b}-1\); summing its bounded-gate updates gives
finite constants for its raw norm, action norm, and interpolation speed,
depending on b but not on p, \(\varepsilon\), or the mesh. This is the direct
calculation of C.4.7.NE with T replaced by this fixed b, not an extension of
that theorem's source cap.

Compare this arbitrary mixture Euler interpolant with the already existing
actual reference on \([0,b]\), using the latter as the sole tail-bearing
endpoint. Its passive Gaussian tails follow from C.4.6.S43 or SCT. The
cutoff subtraction (11), residual differences, and the preceding-node
error give, for physical maximal mesh h,

\[
 \sup_{t\le b}d(\theta_{\varepsilon,p}^{h}(t),\theta_*(t))
 \le C_b e^{C_b(1+R)b}
       \{(1+R)(\varepsilon+h)+e^{-cR^2}\}.
 \tag{32a}
\]

The law difference at the reference is \(O(\varepsilon)\), uniformly in p;
the proxy's preceding-node error is \(O(h)\). These are the two sources
inside the first brace. No tails of the mixture Euler program enter.
Choose R proportional to \(\sqrt{\log(e/(\varepsilon+h))}\), with its
constant large enough to make the Gaussian term smaller than a fixed power
of \(\varepsilon+h\). The linear-in-R amplification is sub-power.
Thus the right side defines a modulus \(\omega_b(\varepsilon+h)\to0\).

Let \(a^h_{\varepsilon,p}\) be the piecewise constant controls of this
Euler program. Uniform scalar prediction continuity and its node error imply

\[
 D_{\varepsilon,b}^{h}:=
 \int_0^b|a^h_{\varepsilon,p}(t)-a_*(t)|_1dt
 \le C_b\{\varepsilon+h+\omega_b(\varepsilon+h)\}\longrightarrow0.
 \tag{32b}
\]

Thus actual integrated coefficient closeness, not merely a raw norm
comparison, is established before applying SCT. For fixed sufficiently small
\(\varepsilon\) and all sufficiently fine meshes these prefixes lie in a
strict SCT tube. Their subsequent Euler Cauchy completion uses the now
available mixture-program tails. This proves uniform-in-p convergence of
the completed prefix to the reference as \(\varepsilon\to0\), for every
separately fixed b, however large.

**Post-b discrete residual contraction and cap first exit**

Include b as a mesh node. Continue actual-mixture Euler with its own
population residuals. Use inner stopping thresholds \(\rho/2\) for distance
from \(\theta_\dagger\) and \(\delta_{\rm src}/2\) for the integrated control
distance; the outer raw ball and source tube have radii \(\rho\) and
\(\delta_{\rm src}\). Choose the step small enough that one update from an
inner stopped node, and its full affine segment, remains in the outer
regions. Its coefficient size is uniformly bounded there by
\(C(|r_k|+\varepsilon)\); its physical step can also be made small enough
to satisfy the dominating control-mesh threshold.

The whole finite history through each such affine segment is source
admissible, so its recomputed passive queries have uniform \(L^4\) bounds.
Along that segment the constant velocity is
\(V_k=-(1-\varepsilon)G_k r_k-2\varepsilon v_{p,k}\).
Its row \(L^4\) norm, middle HS norm, and pointwise readout derivative
are bounded by \(C(|r_k|+\varepsilon)\). Apply the proof of (24)--(26) along
this affine curve, using its fixed node velocity and its current queried
fields. It gives
\(\|(g_{e_a})'\|_{\rm raw}\le C(|r_k|+\varepsilon)\).
The scalar chain rule and a second integration therefore give the exact
Euler residual expansion

\[
 r_{k+1}=[I-h_k(1-\varepsilon)M_k]r_k
       -2h_k\varepsilon G_k^*v_{p,k}+R_k,\qquad
 |R_k|\le C h_k^2(|r_k|+\varepsilon)^2.
 \tag{32c}
\]

This is a derivative along a controlled affine step; it does not assert
ambient \(C^2\) regularity. Since \(4\kappa I\le M_k\le M_{\max}I\),
choose \(h_kM_{\max}\le1\). Then
\(\|I-h_k(1-\varepsilon)M_k\|\le1-2\kappa h_k\).
The residuals are bounded on the outer region, say by \(R_{\max}\).
Use \((|r_k|+\varepsilon)^2\le(R_{\max}+1)(|r_k|+\varepsilon)\), and
decrease the maximal step so that
\(Ch_k(R_{\max}+1)\le\kappa\). Absorbing the remainder yields

\[
 |r_{k+1}|\le(1-\kappa h_k)|r_k|+C h_k\varepsilon,\qquad
 \sum_{k:\ b\le t_k<t_N}h_k|r_k|
 \le C|r_b|+C\varepsilon(t_N-b).
 \tag{32d}
\]

The sum follows by telescoping the first inequality, not by accumulating
an \(O(hT)\) error. The post-b control mass and raw displacement obey the
same right-hand bound. These estimates are uniform in mesh and horizon
while the stopped construction is in the outer regions.

On the original physical schedule, keep the reference running throughout.
The triangle inequality after b gives, through
\(T=b+\tau_0/\varepsilon\),

\[
 \int_0^T|a^h_{\varepsilon,p}-a_*|_1dt
 \le D_{\varepsilon,b}^{h}+(s_\dagger-s_*(b))
             +C|r_b|+C\tau_0.
 \tag{33}
\]

One may pad the actual program with zero controls after T; the untruncated
reference tail is still bounded by \(s_\dagger-s_*(b)\).
No independent time change of that reference is needed.

Choose b large so that the reference endpoint error, its residual, and its
remaining control mass are much smaller than the inner margins. Then choose
\(\varepsilon+h\) small in (32a)--(32b) so that the mixture prefix has the
same properties. Finally decrease \(\tau_0>0\), uniformly in p, so that
\(C\tau_0\) and its associated raw displacement use less than one quarter of
the inner margins. Equations (32d)--(33) keep a potential first exiting node
strictly inside both inner regions. This contradicts first exit.
Thus all the Euler programs continue through \(b+\tau_0/\varepsilon\) with
uniform source caps and raw bounds.

For each fixed positive \(\varepsilon\) this is a finite physical horizon.
The one-reference Osgood comparison, now with the capped Euler paths,
makes the actual-mixture Euler programs Cauchy as their physical meshes
vanish. The argument of Section 4 passes their equations, Gaussian tails,
and scalar controls to a unique strong solution of (29).
It starts from the original initial state. The physical mesh may depend on
\(\varepsilon\); no simultaneous step/perturbation limit is claimed.
The integrated bounds pass to the limit, and the exact continuous
calculation gives (30)--(31).

The choice of \(\tau_0\) works for every sufficiently large b; only the
required smallness of \(\varepsilon\) and the proof mesh depends on b.
This proves the needed original-mixture continuation rather than assuming
it, and permits the successive limits in the next section.

###### C.7. Residual identity and singular selection

Equations (29) give the exact identity

\[
 \theta'=\varepsilon V_p(\theta)+B(\theta)r'.
 \tag{34}
\]

Indeed multiplying the residual equation by \(B=GM^{-1}\) recovers the
anchor force and subtracts precisely the normal component of the added
force. By (27), on the reached segment,

\[
 \|B'(t)\|_{\mathrm{op}}\le C(|r(t)|+\varepsilon).
\]

Combining with (30) and integrating gives

\[
 \int_b^t\|B'(s)r(s)\|_{\rm raw}ds
 \le C\{|r(b)|^2+\varepsilon|r(b)|+\varepsilon^2(t-b)\}.
 \tag{35}
\]

For example \(|r|\le a e^{-2\kappa(s-b)}+C\varepsilon\); squaring and
integrating bounds \(\int|r|^2\) by
\(Ca^2+C\varepsilon a+C\varepsilon^2(t-b)\), and the additional
\(\varepsilon\int|r|\) has the same bound.

The Hilbert-space absolutely continuous product rule now legitimately yields

\[
 \theta(t)=\theta(b)+B(t)r(t)-B(b)r(b)
       +\varepsilon\int_b^t V_p(\theta(s))ds
       -\int_b^t B'(s)r(s)ds.
 \tag{36}
\]

Set \(\widetilde\theta_{\varepsilon,b,p}(\tau)
=\theta_{\varepsilon,p}(b+\tau/\varepsilon)\).
Uniformly for \(0\le\tau\le\tau_0\), (30), (35), and (36) give

\[
 \widetilde\theta_{\varepsilon,b,p}(\tau)
 =\theta_\dagger+
       \int_0^\tau V_p(\widetilde\theta_{\varepsilon,b,p}(s))ds
       +E_{\varepsilon,b,p}(\tau),
\]
\[
 \sup_{\tau,p}\|E_{\varepsilon,b,p}(\tau)\|_{\rm raw}
 \le C\{\sup_p\|\theta_{\varepsilon,p}(b)-\theta_\dagger\|_{\rm raw}
       +\sup_p|r_{\varepsilon,p}(b)|
       +\sup_p|r_{\varepsilon,p}(b)|^2+\varepsilon\}.
 \tag{37}
\]

At fixed b the right side has limit superior at most \(Ce^{-b/5}\), by
(4) and the completed-prefix consequence of (32a)--(32b). Compare (37) with
(20), putting the constructed constrained
path on the tail-bearing side of (17). Formula (13) then gives

\[
 \limsup_{\varepsilon\downarrow0}
 \sup_{p,\tau\le\tau_0}
 \|\widetilde\theta_{\varepsilon,b,p}(\tau)-\bar\theta_p(\tau)\|_{\rm raw}
 \le {\cal O}_{\tau_0}(Ce^{-b/5}).
 \tag{38}
\]

Send b to infinity. For original, unshifted slow time and any fixed
\(0<\tau_{\min}<\tau_0\), write
\(\sigma=\tau-\varepsilon b\ge0\) for small \(\varepsilon\).
Then
\(\theta_{\varepsilon,p}(\tau/\varepsilon)
=\widetilde\theta_{\varepsilon,b,p}(\sigma)\), while
\(\|\bar\theta_p(\tau)-\bar\theta_p(\sigma)\|\le C\varepsilon b\).
Equation (38) proves

\[
 \lim_{\varepsilon\downarrow0}
 \sup_{p\in\mathcal P}\sup_{\tau_{\min}\le\tau\le\tau_0}
 \|\theta_{\varepsilon,p}(\tau/\varepsilon)-\bar\theta_p(\tau)\|_{\rm raw}=0.
 \tag{39}
\]

The reference path is compared at the same physical times and tends to
\(\theta_\dagger\) uniformly on this interval. The exclusion of \(\tau=0\)
in (39) is necessary: the actual original state at physical zero is not the
fitted endpoint. The reference-prefix decomposition proves the limit and
does not change the optimizer.

The bounds for forward actions and the scalar prediction on bounded raw sets
are uniform in the circle input. They therefore turn (39) into whole-circle
prediction convergence and uniform \(L^2\) activation convergence.
The physical scale is \(t=\tau/\varepsilon\), obtained from the exact
projected force in (34). No finite-order law-response expansion has been
extended to this scale.

##### Proof unit D. Actual finite gradient flow and paired observations

###### D.1. Fixed-horizon population-to-finite bridge

Fix one positive epsilon and one admitted added law, and a finite physical
horizon T (which may equal tau0/epsilon). Suppose controlled population Euler
programs for its actual mixture GF converge strongly on [0,T] to a unique
population path theta, with the following bounds uniform in sufficiently fine
Euler partitions: ordinary raw state ball; readout essential supremum;
passive-query second-moment tails

    tau_R(Q(u)) + tau_R(c) <= C exp(-a R^2),  R>=1,

for every training and finitely named observation input. Constants may depend
on the fixed epsilon and T. Here tau_R(v)=||v 1_{|v|>R}||_2; any equivalent
soft cutoff can be used in intermediate convergence arguments. Assume all these
Euler programs live on the same initialized Gaussian carrier and use its actual
forward action and actual adjoint. Their strong limit determines predictions
by f_theta(u)=<c,tanh((A0+K)tanh(w.u))>.

Then the actual width-n mixture GF, starting at the prescribed independent
Gaussian arrays with their actual nonzero readout, converges in probability to
this prediction in C([0,T]xS1). For every finite list of times and inputs, its
first-row, forward hidden, upper gate, readout, and actual forward/adjoint-query
fields have the joint same-layer observation limits supported by the maintained
finite-program theorem and its second-moment extension. This includes paired
second-hidden activation distances between mixture and reference flows using
the same initialized arrays. No unknown finite-width endpoint is introduced.

###### D.2. Proof

At width n all vector and matrix norms are ordinary Euclidean, Frobenius or
operator norms. The raw state-increment metric is

    d_n^2=||W1-W1bar||_F^2/n+||W2-W2bar||_F^2+||c-cbar||_2^2/n.

For a finite vector q define the empirical RMS hard and soft tails

    tau_(R,n)(q)=||q 1_{|q|>R}||_2/sqrt(n),
    sigma_(R,n)(q)=||(|q|-R)_+||_2/sqrt(n).

These are distinct from the population L2 tails tau_R in D.1. All finite
field errors below use the same explicit RMS normalization. In particular,
tau_(R,n)(q)<=2 sigma_(R/2,n)(q), and sigma_(R,n) is one-Lipschitz for
the normalized Euclidean distance. Its square is a continuous empirical
second-moment observation of a fixed finite program.

The initialized middle action itself is bounded in operator norm, rather than
Frobenius norm; only its increments enter d_n. Work on initial events on which
its operator norm, the first-row second moment and initial loss are bounded.
Their probabilities tend to one by the established Gaussian initialization
bounds and laws of large numbers. The actual initial readout has entries of
standard deviation 1/n. Its maximum tends to zero in probability, because
Pr(max_j |c0,j|>eta)<=2n exp(-n^2 eta^2/2). Its normalized second moment also
tends to zero. It is retained in every finite array and proxy, never set to zero.

The finite GF is global at every n. Its smooth vector field is locally
Lipschitz in finite dimensions; unhalved loss dissipation gives
integral_0^T ||theta_n'||_raw^2 <= L_n(0). Hence its raw displacement is at most
sqrt(T L_n(0)). This bounds the action norm by its initialized norm plus the
Frobenius increment. Also |c_n'(j)|<=2 integral |f_n-y| dmu <=2 sqrt(L_n(0)),
so ||c_n(t)||_infty<=||c_n(0)||_infty+2T sqrt(L_n(0)). These bounds imply a
finite raw velocity bound on [0,T], uniform on the preceding initial events.
They justify continuation and every subsequent comparison; they do not provide
the decisive population query tails.

Fix a finite Euler partition h and freeze the *population Euler program's*
scalar training coefficients. Run that exact finite program on the actual
Gaussian arrays, including their initial readout. Call it the finite proxy.
It uses every actual middle multiplication and its actual transpose; no
independent replacement is made. The fixed-program neural law and its
at-most-quadratic observation extension show convergence of all its finitely
named fields, scalar contractions and second moments to their population
program values. The small initial readout passes by a fixed-oracle cutoff induction, rather
than a dimension-dependent finite-dimensional Lipschitz bound. First construct
the finite oracle with zero limiting readout instructions and the same actual
first/middle arrays. Its fixed nodes have the proved joint second-moment laws.
Compare the actual-readout proxy to that oracle, keeping its Gaussian readout
additively in the former. The initial raw error tends to zero. At a coordinate
update, every changed bounded gate multiplying an oracle L2 field is split at
a fixed cutoff R: its bounded part is controlled by the preceding raw error,
and its remaining normalized error by tau_(R,n) of that oracle field.
Bound this hard tail by twice sigma_(R/2,n); the normalized soft tail
converges at fixed program and R by the node's second-moment law. Its
population limit tends to zero as R tends to infinity. Direct action and rank subtractions handle the other
terms. Induction through the finite number of nodes therefore gives raw error
tending to zero at every node. Readout suprema stay bounded on the initial
events because the update is a sum of bounded tanh values and the actual
initial maximum vanishes. No uniform Lipschitz constant on arbitrary
width-dependent parameter balls is assumed. This is the fixed-program
extension used by C.4.7; the zero-readout object is only a comparison oracle,
never a replacement for an actual finite run or its actual-readout proxy.
In particular, the discrepancy between a proxy prediction at an update input
and its population coefficient's prediction tends to zero. Denote the maximum
of these finitely many discrepancies by zeta_(n,h); then zeta_(n,h)->0 in
probability for fixed h.

For clarity, the comparison can be made at every left Euler endpoint and its
affine interpolation. The interpolation stays on a common raw ball. Its
recomputed normalized soft tails of c and Q converge at a fixed cutoff to
the corresponding population L2 soft tails. One may first name a finite
additional interpolation grid; the forward/action maps are Lipschitz for
normalized finite field norms on this ball with bounded readout, and the
proxy raw interpolation speed is bounded. The soft tails sigma_(R,n)(Q)
and sigma_(R,n)(c) pass to the fixed-program limit and are one-Lipschitz
in the corresponding normalized field distances.
A finer interpolation grid and the elementary inequalities relating hard tails
at R to soft tails at R/2 give the asserted bound uniformly over interpolation
time, with enlarged constants. No growing transcript is taken before width.

Subtract actual GF from the affine proxy. The one-reference product inequality
is elementary: for a bounded Lipschitz gate b and an arbitrary comparison
vector qbar,

    ||(b(z)-b(zbar))qbar||_2/sqrt(n)
                <= C R ||z-zbar||_2/sqrt(n) + C tau_(R,n)(qbar).

Apply it to the lower gate multiplier with the proxy Q as qbar and to the
upper multiplier with proxy c. Direct bounded-operator subtraction handles Q
itself. For finite middle updates the rank identity is

    ||a b^T/n||_F=(||a||_2/sqrt(n))(||b||_2/sqrt(n)).

It is the finite counterpart of the population identity
||a tensor b||_HS=||a||_2||b||_2. Prediction residual subtraction is bounded by
the raw distance on the common ball. The frozen coefficient error contributes
zeta_(n,h), and the interpolation defect contributes O(h_max). Thus, for each
fixed cutoff R and the fixed T,

    sup_[0,T] d_n <= C_T exp(C_T R) [
       (1+R)(h_max+zeta_(n,h))
       + sup_proxy_time (tau_(R,n)(c_proxy)
                          +sum_j p_j tau_(R,n)(Q_proxy(u_j))) ].

The two finite states have identical initial arrays, so there is no initial
state error in this inequality. The actual initial Gaussian readout remains
inside both states and the harmless uniform initial bounds above.

Take n->infinity with the partition and cutoff fixed. Convergence of the
normalized soft tails, the hard-to-soft inequality above and the population
Gaussian tails bound the width limsup of the proxy-tail terms by C exp(-a'R^2);
zeta_(n,h) vanishes. For any desired
comparison error, first choose R large enough that
C_T exp(C_T R-a'R^2) is smaller than that error, then choose h_max small enough
that its amplified interpolation defect is smaller still. Both choices are
finite at every fixed positive epsilon. This proves proximity of finite GF to
the finite proxy in probability, with arbitrarily small prescribed error.
Strong population Euler completion then identifies the unique population path.
One does not send R to infinity at a fixed positive mesh, or claim uniform
width rates as epsilon tends to zero.

On each common raw ball,

    sup_u |f_theta(u)-f_thetabar(u)| <= C_T d(theta,thetabar),
    ||H2_theta(u)-H2_thetabar(u)||_2 <= C_T d(theta,thetabar).

These displays use the population raw metric and population L2 norm. Their
finite counterparts, for the two finite states under comparison, are

    sup_u |f_(n,theta)(u)-f_(n,thetabar)(u)| <= C_T d_n,
    ||h2_(n,theta)(u)-h2_(n,thetabar)(u)||_2/sqrt(n) <= C_T d_n.

The input Lipschitz constants are bounded by products of the readout, action
and first-row norms; at finite width these are ||c||_2/sqrt(n), the middle
operator norm and ||W1||_F/sqrt(n). H1 and H2 satisfy the corresponding
population L2 and finite RMS input estimates.
Consequently finite input nets upgrade proxy prediction convergence to the
whole circle, uniformly in physical time using the same velocity bounds.
This proves the claimed C([0,T]xS1) convergence.

For joint reference/mixture observations, use the union of their finite proxy
programs on the SAME Gaussian arrays and the finite-program joint law. Paired
bounded activation products are permitted second-moment observations. Both
finite flows are close to their proxies in the normalized hidden norms, so
Cauchy–Schwarz passes each mixed inner product and squared distance. Reference
capture is required only on this fixed finite T, where the established result
applies. The endpoint appears only afterwards, through the proved population
reference convergence as epsilon tends to zero and T=tau/epsilon tends to
infinity. Thus the paired finite statistic at time T converges to

    (1/m) sum_i ||H2_theta_mu(T)(u_i)-H2_theta_*(T)(u_i)||_2^2.

Combining the population selection theorem of proof unit C with the already
proved reference endpoint convergence gives its constrained-path versus latent
endpoint limit. This order keeps the actual common initialization intact.

##### Completion of the theorem

Take the common constrained existence time from proof unit C as the
\(\tau_{ex}\) used in proof unit B, and use B's smaller positive time as
our final \(\tau_0\). Decreasing a time already constructed preserves every
source bound, uniqueness statement and mixture continuation estimate. Set
\(a=\eta_R\) from (5.5) and \(j=\eta_H\) from (5.7), both in proof unit B.
They depend only on the fixed reference and parameter rectangle.

Proof unit C proves (NS5) uniformly over that rectangle, in the original
unshifted physical times \(t=\tau/\epsilon\). Its original-mixture Euler
programs verify all the population hypotheses of proof unit D for each fixed
positive \(\epsilon\). Thus D proves (NS8) and the joint same-array
observation contract. At \(T_\epsilon\), the population reference tends
strongly to \(\theta_\dagger\). The forward field inequalities therefore
identify (NS9)'s limit with (NS7), using paired programs on the same initialized
arrays, followed only then by \(\epsilon\downarrow0\).

On the common bounded prediction region, squared loss at the one added atom
is continuous. Hence the probability that
\(R_{\nu}(F_*)-R_{\nu}(f_{n,\mu_\epsilon}(T_\epsilon))\ge a/2\)
and \(J_{2,n,\epsilon}\ge j/2\) tends to one in the displayed iterated order.
This verifies every assertion of the theorem. The state reconstruction retains
the evolving hidden features and actual adjoint throughout the episode.

