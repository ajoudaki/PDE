# Nonlinear activation, separation, and continuation additions

These fragments extend the global nonlinear and special-data chapters. Each probability statement takes width to infinity at a fixed depth, fixed finite dataset, fixed activation, and fixed finite physical horizon. Constants uniform over a parameter class do not assert a probability supremum over that class. Layer populations are separate. Initialized actions and their adjoints are constructed jointly; only trained increments are Hilbert--Schmidt.

The packages are: a global two-hidden-layer activation transform and its affine-first arbitrary-data exception; a local fixed-depth C1,1 theorem and its Gaussian strict-activity corollary; separated two-sample offset, odd, and general-shape theorems; all-fixed-depth odd perturbations; the three-sample odd-gain theorem; and exact moderate-amplitude identities, local limits, finite-algorithm estimates, strong endpoints, and conditional continuation.

The finite Gaussian construction, including rank loss, causal bounded-derivative scalar feedback, common generated spaces, and adjunction, is the contained proof in **special-data Section III.F**. The observation and same-width comparison arguments are **Section III.V**. They are mathematical dependencies within the chapter. Their coordinate hypotheses are verified below; neither theorem is applied directly to an instruction with unbounded derivative. Equation numbers inside each numbered fragment are local to that fragment.

For the two-sample and odd-gain fragments using first-coordinate notation \(V^1\) or \(w\), the exact conversion to the notation contract is
\[
 V^1=W^{(1)}/\sqrt d,\qquad z_a^1=V^1x_a,
 \qquad \frac d n\|dV^1\|_F^2=\frac1n\|dW^{(1)}\|_F^2.
\]
A displayed first matrix with entry variance \(1/d\), including a locally named \(W^1\), always means this \(V^1\). For finite vectors, any rank-one symbol u tensor v or \(u\otimes v\) means the matrix uv^T/n; its population counterpart is the rank-one action q -> u E[vq]. The stored readout is \(C=W^{(L+1)}\), and \(f_a=C^Th_a^L/n\). The half-sum loss in those fragments is explicitly \(\frac12\sum_a(f_a-y_a)^2\); its raw mobilities in canonical coordinates are \((n,1,\ldots,1,n)\). The broad two-layer theorem instead uses the unhalved sum, and the general local theorem uses its stated weighted mean. Their factors of two are retained. An auxiliary feature time or normalized time is never the raw GD step.

There are 46 proof units after the common lemmas. They are organized as follows.

| Fragments | Result to insert | Destination and exact scope |
|---|---|---|
| A, B | Continuous-value Gaussian specialization; activation transform; affine-first exception | Global nonlinear: L=2, bounded top activation/readout, orthogonal data; arbitrary fixed input geometry for an affine first activation. Exact raw GD uses eta_n sqrt(n)->0, or eta_n->0 in the affine exception. |
| C | Local C1,1 limit, finite-GF corollary, strict Gaussian activity | Global nonlinear: fixed L,m,d, subGaussian first/readout roots and arbitrary fixed data on one positive interval; activity has its additional stated Gaussian/nondegeneracy assumptions. |
| D | Offset separation theorem | Special data: L=3,m=2, rho in [-1,1-delta], binary labels, a delta-selected coefficient, full compact-physical-time GF/GD bundle. |
| E | Odd perturbations at e<=c_poly delta^2 | Special data: L=3,m=2, two-sided separation, all binary labels; convex and unit-Gaussian-energy variants. |
| F | General nonodd/linear-growth shapes and affine positivity | Special data: L=3,m=2, e<=c_dyn delta^(31/8); a further shape cutoff gives persistent nonaffinity. Affine positivity is an exact separate lemma. |
| G | Odd perturbations at all fixed depths | Special data: each fixed L>=4; explicit depth-dependent coefficient/exponent, full GF/GD and motion bundle. |
| H | One odd large-gain activation for all fixed depths | Special data: m=3, fixed L>=2, two-sided separation and binary labels; gain depends on separation, not depth. |
| I | Moderate sine initialization/local limit/finite algorithms/endpoints/conditional global construction | Exact calibrated coefficient 2/5; no unconditional global population theorem is asserted. |
| J | Bounded learned memories and simultaneous-coordinate obstruction | Exact identities or conditional necessary inequalities at their displayed model scopes. |

The term “full bundle” in this table means the explicitly stated same-layer path and field/velocity Wasserstein-2 laws, finite collections of times, all true kernel blocks, fixed generated actions/adjoints, predictions, loss, second moments and integrated squared speeds. It excludes cross-layer neuron pairing, cross-width operator-norm convergence, a growing query language and an infinite-time/width interchange. B and C retain their own narrower observable statements.

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

## C. A local fixed-depth theorem and strict Gaussian activity

The local theorem permits subGaussian first weights and readout, arbitrary fixed data, zero middle variances and frozen blocks as stated. The separate strict-activity corollary requires Gaussian first weights, positive variances and mobilities, zero population readout, nonzero labels and pairwise nonparallel unit inputs. These are additional hypotheses of that corollary.

For fixed C2 Euler programs, A.1–A.2 prove their value and named-source response formulas. Direct iid subGaussian tuples are roots. No Gaussian quantile representation is needed. The response estimates below are uniform over meshes; this uniformity is proved separately from the fixed-program result. Mollification then gives C1,1 activations.

For squared loss, the theorem for every deterministic vanishing GD mesh also gives finite GF: for each fixed width, smooth finite-dimensional Euler convergence allows a deterministic mesh smaller than 1/n with probability of GF/GD discrepancy exceeding 1/n smaller than 1/n. Apply the every-mesh theorem to this diagonal sequence. The finite squared-loss flow exists globally: at fixed width, energy controls its Euclidean parameter length on every finite interval, even with frozen blocks, and its locally Lipschitz field extends from a finite endpoint. The diagonal yields the same local population GF limit, in exactly the observable topologies C.1 states. For the separate general separable-loss extension, use the preliminary local ball on its high-probability initialization event, with stopping outside that event; no global finite-GF claim follows for a loss unbounded below.

### C.1. Local fixed-depth C1,1 theorem

Within this proof unit, unqualified section and equation numbers are local.

#### Statement and exact finite model

Fix integers d,m and L>=2. There are L hidden layers, each of width n. The m
inputs x_a in R^d are fixed, with ||x_a||_2/sqrt(d)<=X and
G_ab=x_a^top x_b/d. Their Gram matrix may be singular and inputs may coincide.
For squared loss assume |y_a|<=Y. Choose positive weights omega_a with
sum_a omega_a=1 and use

    L_n = sum_a omega_a (f_n,a-y_a)^2,       r_n,a=f_n,a-y_a.

This declares a change from summed loss. For summed loss on m examples, the
same statement applies after multiplying physical time by m.

Each activation phi^(ell):R->R is C^1, with bounded derivative and globally
Lipschitz derivative. Fix common finite bounds

    |phi^(ell)(0)|<=D0,
    |phi^(ell)'(s)|<=D1,
    |phi^(ell)'(s)-phi^(ell)'(t)|<=D2 |s-t|.

The activations themselves need not be bounded. In particular their growth is
at most linear. Nonaffinity is not required for existence.

Concrete examples include arctan, tanh, logistic sigmoid, softplus, exact GELU,
and SiLU, with different choices in different layers. For softplus,
phi'=s and phi''=s(1-s), where s is the logistic sigmoid evaluated at the
argument. For exact GELU phi(t)=t Phi(t),
phi'(t)=Phi(t)+t varphi(t) and phi''(t)=(2-t^2)varphi(t), where Phi and
varphi are the standard normal distribution function and density. For SiLU,
phi(t)=t s(t), phi'(t)=s(t)+t s(t)(1-s(t)) and
phi''(t)=2s(t)(1-s(t))+t s(t)(1-s(t))(1-2s(t)). These derivatives are bounded
because Gaussian and logistic tails dominate the displayed polynomial
factors. The C1,1 class also contains a quadratic smoothing of ReLU: zero for
t<=0, t^2/2 for 0<=t<=1, and t-1/2 for t>=1. Its derivative is bounded and
1-Lipschitz although its second derivative does not exist at both junctions.

For the principal initialization take independent Gaussian first weights
W^(1)_0,ij~N(0,sigma_1^2), independent middle matrices
W^(ell)_0,ji~N(0,sigma_ell^2/n), 2<=ell<=L, and independent readout entries
W^(L+1)_0,j distributed as a fixed random variable with

    sup_(p>=2) (E|W^(L+1)_0,j|^p)^(1/p)/sqrt(p) <= B_out < infinity.

Zero, bounded, and nonvanishing Gaussian readout are all allowed. The first
weights may more generally be iid centered subGaussian variables, with a fixed
subGaussian bound B_in. This extension is justified below; the strict-activity
corollary will use Gaussian first weights. All initialization groups are
independent. Sigma values may be zero in the existence theorem.

Define, with coordinatewise activation,

    z^(1)_a=W^(1)x_a/sqrt(d),       h^(1)_a=phi^(1)(z^(1)_a),
    z^(ell)_a=W^(ell)h^(ell-1)_a,  h^(ell)_a=phi^(ell)(z^(ell)_a), 2<=ell<=L,
    f_n,a=(W^(L+1))^top h^(L)_a/n.

W^(L+1) is always the stored rescaled readout. In particular, for L=2 it is
W^(3), and f_n,a=(W^(3))^top h^(2)_a/n.

The backpropagated fields omit the loss derivative:

    delta^(L)_a=W^(L+1) phi^(L)'(z^(L)_a),
    delta^(ell)_a=phi^(ell)'(z^(ell)_a)
                       [(W^(ell+1))^top delta^(ell+1)_a], ell<L.

Thus delta^(ell)_a=n partial f_n,a/partial z^(ell)_a. Choose fixed finite
kappa_ell>=0. Stored-weight gradient-descent rates are

    eta_n (n kappa_1, kappa_2, ..., kappa_L, n kappa_(L+1)).

The exact updates are

    W^(1)_(k+1)=W^(1)_k
        -(2 eta_n kappa_1/sqrt(d)) sum_b omega_b r_n,b,k delta^(1)_b,k x_b^top,
    z^(1)_a,k+1=z^(1)_a,k
        -2 eta_n kappa_1 sum_b omega_b G_ab r_n,b,k delta^(1)_b,k,
    W^(ell)_(k+1)=W^(ell)_k
        -(2 eta_n kappa_ell/n) sum_b omega_b r_n,b,k
                             delta^(ell)_b,k (h^(ell-1)_b,k)^top, 2<=ell<=L,
    W^(L+1)_(k+1)=W^(L+1)_k
        -2 eta_n kappa_(L+1) sum_b omega_b r_n,b,k h^(L)_b,k.                 (1)

Use physical time t=k eta_n, interpolate these parameters linearly, and
recompute forward quantities between grid points.

There is T_*>0 depending only on L, X, Y, D0,D1,D2, the initialization bounds
and the kappa values, such that for EVERY eta_n>0 tending to zero the following
conclusions hold on [0,T_*]:

1. A unique strong population flow exists in the field/operator state described
   below. It is autonomous and retains each matrix together with its adjoint.
2. Predictions, loss, and all kernel entries converge in probability uniformly
   in time to their population values.
3. Separately for each neuron population, empirical laws of the joint m-input
   hidden paths converge in Wasserstein distance of order two for the uniform
   path norm. This applies to both preactivations and activations.
4. Integrated squared hidden speeds converge. Fixed finite, correctly typed
   forward/adjoint probes assembled from Lipschitz coordinate maps, linear
   combinations, and products of a bounded factor and an L2 field also have
   their joint continuous quadratic-growth measurements converge, provided
   the bounded factors are continuous functions of their arguments.

The constants do not depend on n, eta_n, m, d, or a smallest Gram eigenvalue
when the stated bounds remain fixed. Here m,d and the inputs are nevertheless
fixed in the convergence assertion: no uniform convergence rate for growing
datasets or dimension is claimed. Probe length is fixed; arbitrary products of
two unbounded factors are not part of the probe assertion.

#### Population state, construction, and preliminary norm bounds

There is a separate probability space for coordinates in each hidden layer.
The field Z^(1)_a belongs to the first, W^(L+1) to the last. For 2<=ell<=L,
W^(ell) is a bounded linear map from the mean-square space at layer ell-1 to
the one at layer ell. Its adjoint is denoted (W^(ell))^*. Expectations pair
variables belonging to the same population. Define

    (u tensor v)V = u E[v V].

This is the population version of the finite map u v^top/n. The population
forward and backward formulas are those above with uppercase Z,H, expectation
in place of b^top c/n, and * in place of top. In particular

    f_a=E[W^(L+1) H^(L)_a],
    P^(L)_a=W^(L+1),
    P^(ell)_a=(W^(ell+1))^* delta^(ell+1)_a, ell<L,
    delta^(ell)_a=phi^(ell)'(Z^(ell)_a) P^(ell)_a.

The limiting equations are

    dot Z^(1)_a=-2 kappa_1 sum_b omega_b G_ab r_b delta^(1)_b,
    dot W^(ell)=-2 kappa_ell sum_b omega_b r_b
                                  delta^(ell)_b tensor H^(ell-1)_b, 2<=ell<=L,
    dot W^(L+1)=-2 kappa_(L+1) sum_b omega_b r_b H^(L)_b.                    (2)

A strong solution means these integral equations hold in L2 for the fields
and in operator norm for the matrices, continuously in time. The initial first
roots have the law of (W^(1)_0 x_a/sqrt(d))_a for a single row. For Gaussian
weights this is N(0,sigma_1^2 G). The initial operators are constructed from
the joint matrix/transpose limits, not replaced by independent backward maps.

Centered independent subGaussian first entries have uniformly subGaussian projections:
their moment bounds give E exp(t W_ij)<=exp(C B_in^2 t^2); independence then
gives E exp(t sum_j u_j W_ij)<=exp(C B_in^2 t^2 sum_j u_j^2).
Thus each initial Z^(1)_a has a marginal subGaussian bound depending only on
B_in X. No assumption of iid neuron coordinates after matrix reuse is made.

To obtain common spaces for different meshes, take the countable union of the
programs for rational meshes, their finite unions, rational linear
combinations and the coordinate operations needed here (including clipped
products). Their laws are consistent under deletion of instructions. Realize
these countably many laws jointly on each population and take the L2 closure
of the resulting fields. Operator inequalities pass from finite width to each
finite collection. Indeed a 1/4-net in each unit sphere gives

    P(||W^(ell)_0||_op>M)
       <=2*9^(2n)*exp[-n M^2/(8 sigma_ell^2)] -> 0                       (3)

for a sufficiently large fixed M (zero variance needs no bound). Since
||W^(ell)_0 v||_2/sqrt(n)<=M ||v||_2/sqrt(n), second-moment convergence gives
||W^(ell)_0 V||_L2<=M||V||_L2 on the generated span, hence on its closure.
The same argument gives the transpose map. The exact finite adjunction
identity passes to the limit and identifies it with the adjoint. Coordinate
operations extend wherever needed by clipping and L2 limits.

For the following fixed-computation response statements use A.1–A.2, with arbitrary iid subGaussian tuples admitted directly as roots.
For two states on these same spaces use the distance

    d(theta,theta_tilde)=max_a ||Z^(1)_a-Ztilde^(1)_a||_L2
       +sum_(ell=2)^L ||W^(ell)-Wtilde^(ell)||_op
       +||W^(L+1)-Wtilde^(L+1)||_L2.                                    (4)

At finite width replace every field L2 norm by ||b||_2/sqrt(n). No operator
distance between a finite matrix and a population operator is asserted.

Here is an explicit preliminary interval on which these norms stay bounded.
Let S be the maximum of the individual norms entering the state (not the
distance). Choose S0 so the initial norms are <=S0 with probability tending to
one, uniformly in the bound parameters, and are <=S0 in the population.
First-weight concentration is needed only over fixed m. Set B=2S0+2 and

    h_1=D0+D1 B,       h_ell=D0+D1 B h_(ell-1),
    d_ell=D1^(L-ell+1) B^(L-ell+1),
    R0=B h_L+Y.

On S<=B, all ||H^(ell)_a||_L2<=h_ell, ||delta^(ell)_a||_L2<=d_ell,
and |r_a|<=R0. The same inequalities hold at finite width. The norm of each
state velocity is therefore bounded by the corresponding member of

    2 kappa_1 X^2 R0 d_1,
    2 kappa_ell R0 d_ell h_(ell-1) (2<=ell<=L),
    2 kappa_(L+1) R0 h_L.

Let V0>=1 bound their sum. On

    T_ball=min(1,(B-S0)/(4 V0)),                                       (5)

Euler trajectories with mesh <=T_ball remain in S<=B through time 2 T_ball:
up to the first possible exit the cumulative increment is at most 2T_ball V0,
strictly less than B-S0. The same first-exit argument works for integral
solutions. It also bounds interpolation speeds, with a constant depending on
L. This requires only operator and RMS bounds, including for the readout.

#### The additional estimate uniform in the time mesh

The fixed-depth response lemma in Fragment C.2 derives,
on a further interval T_response>0, for every population Euler mesh Delta,

    sup_(k Delta<=T_response) max_(a,ell)
          E exp(c |P^(ell)_a,k|^2) <= C.                                (6)

It proves this for unbounded activations as well as nonvanishing subGaussian
readout. Its precise recurrences and noncircular choice of constants are part
of this proof, not an additional hypothesis of the theorem.

The important bounds in that derivation are entrywise response coefficients
|C^(ell)_(ak,bs)|<=c_ell Delta omega_b and bounded row sums of A^(ell).
SubGaussian norms of the forward fields and backward fields are bootstrapped
together. A derivative in a single backward slot starts with a pulse carrying
Delta omega_b. Every later random growth coefficient appears in a weighted
time sum Delta sum_(s,b) omega_b |P^(ell)_b,s|. Jensen's inequality bounds its
exponential using marginal subGaussian estimates; independence over time is
not assumed and no maximum of Gaussian fields over the mesh is taken.

Set T_*<=min(T_ball,T_response), with any additional reductions specified in
the lemma. The constants are functions of the displayed bounds only. In
particular they do not contain Delta or m.

#### Localization, existence, and uniqueness

Forward fields and predictions are Lipschitz in (4) on the ball S<=B, with
a constant depending on fixed depth and bound parameters. This follows by
expanding W H-Wtilde Htilde=(W-Wtilde)H+Wtilde(H-Htilde), and using
||phi(Z)-phi(Ztilde)||_L2<=D1||Z-Ztilde||_L2.

Backward fields require a cutoff. For any reference field Ptilde,

    ||[phi'(Z)-phi'(Ztilde)] Ptilde||_L2
       <=D2 R ||Z-Ztilde||_L2
           +2D1 ||Ptilde 1_(|Ptilde|>R)||_L2.                            (7)

Write a delta difference as

    phi'(Z)(P-Ptilde)+[phi'(Z)-phi'(Ztilde)]Ptilde.

For ell<L the difference P^(ell)-Ptilde^(ell) is bounded by
B||delta^(ell+1)-deltatilde^(ell+1)||_L2+C d; at ell=L it is a readout
difference. Downward substitution yields

    max_(a,ell)||delta^(ell)_a-deltatilde^(ell)_a||_L2
       <=C(1+R)d+C sum_(ell=1)^L max_a
                  ||Ptilde^(ell)_a 1_(|Ptilde^(ell)_a|>R)||_L2.

Each backward step multiplies the previous difference only by bounded
activation derivatives and bounded operators. The new cutoff term is added;
there is no power R^L. Outer-product differences satisfy
||u tensor v-utilde tensor vtilde||_op
 <=||u-utilde||_L2 ||v||_L2+||utilde||_L2 ||v-vtilde||_L2.
Together with (6), this proves for the vector field in (2)

    ||F(theta)-F(theta_reference)||
       <=C(1+R)d(theta,theta_reference)+C exp(-c R^2),                    (8)

when the reference is a population Euler grid state. Only the reference needs
the tail estimate.

Compare two piecewise linear population Euler interpolants. At time t their
assigned velocities are F evaluated at their respective preceding grid
states. These states differ by at most their interpolant distance plus
C(Delta+Delta'). Apply (8) directly to these grid states and integrate:

    sup_(t<=T_*) d(theta^Delta(t),theta^Delta'(t))
       <=C exp[C(1+R)T_*]
           ((1+R)(Delta+Delta')+exp(-cR^2)).                             (9)

First fix R and send both meshes to zero; then send R to infinity. Since
exp(CRT_*-cR^2)->0, the paths are Cauchy in the complete field/operator spaces.

All coordinate products occurring in F are continuous on these spaces.
For the only subtle product, if Z_j->Z and P_j->P in L2, split
phi'(Z_j)P_j-phi'(Z)P into the bounded multiplier times P_j-P and
[phi'(Z_j)-phi'(Z)]P. The latter converges in L2 by convergence in probability,
boundedness of phi', and uniform integrability against the single integrable
variable P^2. Thus F is continuous; on the compact range of a convergent
sequence of continuous paths this continuity is uniform. The Euler integral
equations pass to (2), giving a strong solution. All P fields converge at
fixed times; Fatou transfers (6) to the solution uniformly in time.

For any other strong solution with the same initial state, (5) bounds its
norms on this interval. Apply (8) with the constructed solution as reference.
Their distance is <=C exp(CRT_*-cR^2) for every R, hence zero. This proves
uniqueness without assuming tails of the competing solution.

Equations (2) use only the current fields, operators, and adjoints. More
precisely, the closed spaces generated by a current state under these
operations and clipped products contain all its subsequent Euler
approximations and their limits. Equal current joint action laws identify
these spaces by an L2 isometry intertwining the operators and coordinate
operations. Uniqueness identifies their subsequent laws. This is autonomy
and restartability on the constructed interval, not a finite scalar closure.

#### From the population flow to every vanishing-step finite GD sequence

Fix a rational coarse mesh Delta, independently of eta_n. Expand

    W^(ell)_k=W^(ell)_0-2 kappa_ell Delta
          sum_(s<k,b) omega_b r_b,s delta^(ell)_b,s tensor H^(ell-1)_b,s.   (10)

Build a finite oracle computation using the same sampled initial arrays as
actual GD. In its expanded matrix actions replace all scalar contractions
and residuals by their deterministic population Euler values. This is a
fixed finite program, so the stated theorem gives joint empirical convergence
of every needed node, contraction, second moment, and continuous quadratic
tail cutoff. Its coefficients are a proof device determined by the population
Euler equations; they are not the coefficients of the final autonomous flow.

Construct proxy parameters from the oracle's first-layer/readout nodes and
the finite rank expansion corresponding to (10), with u v^top/n. Applying a
proxy matrix to an oracle node differs from its prescribed oracle action by
finitely many terms of the form

    -2 kappa_ell Delta omega_b r_b,s delta^(ell)_b,s,oracle
       ((h^(ell-1)_b,s,oracle)^top h^(ell-1)_a,k,oracle/n
                         -E[H^(ell-1)_b,s H^(ell-1)_a,k]),               (11)

and transpose actions have the corresponding delta contractions. At fixed
Delta, their scalar errors vanish and their vector RMS norms are bounded.
Consequently all proxy forward quantities are consistent in RMS. To transfer
backpropagation with an unbounded readout, use (7) against oracle P nodes and
proceed downward through layers. At any fixed cutoff the errors vanish, and
the empirical oracle tails converge to the tails in (6); sending that cutoff
to infinity proves the recomputed proxy delta fields are consistent in RMS.
This also proves consistency of its vector field and residuals.

The proxy grid fields therefore have reference tails with limiting upper
bound C exp(-cR^2), after harmless changes in constants. For example if
||v-u||_2/sqrt(n)=e_n then

    ||v 1_(|v|>2R)||_2/sqrt(n)
       <=2 e_n+2||u 1_(|u|>R)||_2/sqrt(n).

Its grid and interpolated norm/speed bounds have limiting upper bounds
independent of Delta, by (5), (10), and the fixed-mesh consistency. Enlarge
the comparison ball by a fixed amount if necessary.

Compare actual GD and the proxy interpolant using their assigned grid
velocities. The actual preceding fine-grid state and reference preceding
coarse-grid state are at distance at most the interpolant distance plus
C(eta_n+Delta). The actual-to-proxy vector-field difference obeys (8), now
with empirical reference tails and fixed-mesh errors. Thus

    sup_(t<=T_*) d_n(theta_n^GD(t),theta_n^proxy,Delta(t))
       <=C exp[C(1+R)T_*]
          ((1+R)(eta_n+Delta)+exp(-cR^2)+o_P(1)).                         (12)

Here o_P(1) is at fixed R,Delta. Initial distance is zero because the oracle
uses the same roots. A vanishing initialization perturbation contributes its
distance to the right side. The actual GD requires only its RMS/operator
ball, not a maximum coordinate bound or an empirical tail theorem for a
growing number of steps.

The limit order is: n->infinity with R,Delta fixed, then Delta->0, then
R->infinity. Equation (12), (9), and fixed-mesh empirical convergence prove
the joint width/step limit. There is no condition such as eta_n sqrt(n)->0.

Predictions follow by the forward Lipschitz bound. Define the kernel blocks

    K^(1)_ab=G_ab E[delta^(1)_a delta^(1)_b],
    K^(ell)_ab=E[H^(ell-1)_a H^(ell-1)_b]
                      E[delta^(ell)_a delta^(ell)_b], 2<=ell<=L,
    K^(L+1)_ab=E[H^(L)_a H^(L)_b],
    K=sum_(ell=1)^(L+1) kappa_ell K^(ell).

Their finite counterparts use b^top c/n in every contraction. Backward RMS
consistency and Cauchy--Schwarz give uniform convergence of these entries.
For Omega=diag(omega_1,...,omega_m), direct differentiation gives

    dot f=-2 K Omega r,        dot L=-4 (Omega r)^top K (Omega r).         (13)

Each block is positive semidefinite, being a parameter-gradient Gram matrix.

For completeness, the extra observable steps do not demand higher moments
of actual GD. The population parameter velocities converge uniformly in L2
and operator norm by (8). Recursively,

    dot Z^(ell)_a=dot W^(ell) H^(ell-1)_a
                    +W^(ell)[phi^(ell-1)'(Z^(ell-1)_a) dot Z^(ell-1)_a]   (14)

is continuous in the state and parameter velocity in the stated norms.
The bounded-multiplier product is justified by the same fixed-reference
uniform-integrability argument used after (9). On the compact population
time path these velocities form a compact L2 family, hence have uniformly
vanishing L2 tails. For each fixed Delta, oracle evaluations of these
velocities are fixed finite programs and have convergent empirical cutoff
moments. Localizing their bounded-multiplier products, first using (12),
then passing Delta to zero, proves convergence of the integrated squared
hidden speeds. No exponential estimate for these derived velocities is
needed; cutoffs here occur after state stability, outside Gronwall.

At any grid with cell length at most epsilon, each absolutely continuous
coordinate path obeys

    sup_(s,t in one cell)|z(t)-z(s)|^2
         <=epsilon integral_cell |dot z(u)|^2 du.

After averaging over neurons and summing over cells, the error of grid
reconstruction in squared uniform path norm is <=C epsilon, uniformly in n
on the ball. Fixed-time empirical joint laws converge in Wasserstein distance
of order two by fixed-program convergence and their second moments. Combining
this with grid reconstruction proves assertion 3. Activations follow from
their Lipschitz bounds. The same cutoff induction proves assertion 4: an
operator amplifies L2 errors by at most B, Lipschitz functions preserve them,
and bounded-factor products use the compact reference L2 family's uniform
integrability. This explains the stated restriction on products.

#### Removing second differentiability; losses and initialization perturbations

First the proof above is for C2 activations with bounded first two
derivatives. For a C1 activation whose derivative is globally Lipschitz,
convolve with a smooth compactly supported probability density of scale
epsilon. Then

    ||phi_epsilon-phi||_infinity<=C D1 epsilon,
    ||phi_epsilon'-phi'||_infinity<=C D2 epsilon,
    ||phi_epsilon'||_infinity<=D1,    ||phi_epsilon''||_infinity<=D2.

The response lemma and T_* depend only on these bounds, uniformly in
epsilon. Include rational smoothing scales in the common program family.
The comparison (8) between different smoothings has an additional
C(1+R)(epsilon+epsilon') term: forward differences gain O(epsilon), and
backward differences use (7) plus the uniform difference of derivatives.
The same ordered limits construct a strong flow for the original activation,
inherit (6), and prove uniqueness. Compare finite GD for the original
activation with the fixed smooth oracle by the identical estimate, adding
C(1+R)epsilon inside (12). Taking n,Delta,epsilon,R in that order proves the
same joint limit for C1,1 activations. ReLU's discontinuous derivative does
not satisfy this argument.

More general separable losses are allowed: use sum_a omega_a ell_a(f_a),
where every ell_a is C1 and its derivative is locally Lipschitz, with common
finite bounds and Lipschitz constants on bounded prediction intervals.
Replace every 2r_b in (1),(2),(10)--(12) by ell_b'(f_b). The preliminary ball
uses sup_(a,|f|<=B h_L)|ell_a'(f)| in place of 2R0; prediction stability uses
the corresponding local Lipschitz constant. In response differentiation these
oracle coefficients are frozen, so every response estimate uses only their
bound and the pulse still carries Delta omega_b. The proof is unchanged
with exactly these replacements. No convexity or global growth assumption
on the loss is required on this short interval. For this loss,
dot f_a=-sum_b K_ab omega_b ell_b'(f_b), and
dot L=-sum_ab omega_a ell_a'(f_a) K_ab omega_b ell_b'(f_b).

Finally (12) also allows perturbing the sampled initial arrays by an amount
tending to zero in probability in (4), and changing the kappa constants by
vanishing amounts. The actual initial arrays need only the resulting RMS
and operator bounds. In particular zero population readout covers finite
Gaussian readout sigma_out n^(-beta) g for EVERY beta>0, and indeed any
readout perturbation with ||W^(L+1)_0||_2/sqrt(n)->0 in probability. This
does not assert universality for different O(1) non-Gaussian middle matrices:
such a replacement need not be small in operator norm.

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

### C.3. Gaussian strict-activity corollary

Within this proof unit, unqualified section and equation numbers are local.

This proof unit proves the strict nontriviality part of the two-hidden-layer population result. It is conditional on existence of the population gradient flow with the mean-square continuity specified below. It does not, by itself, establish an existence theorem or a width limit for its whole activation class.

The useful conclusion is broad: **bounded, nonconstant, continuously differentiable activations with bounded derivatives are sufficient**, in both hidden layers. Neither activation needs to be odd, analytic, monotone, or strictly monotone. Derivatives may change sign and may vanish on intervals. Thus bounded nonconstant \(C^2\) activations with bounded derivatives certainly qualify. A broader conditional version allows unbounded activations with bounded continuous derivatives, provided both activations are nonaffine.

#### Setup and conclusion

Fix \(m<\infty\) inputs \(x_a\in\mathbb R^d\) with
\[
\frac{\|x_a\|_2^2}{d}=1,
\qquad
G_{ab}=\frac{x_a^\top x_b}{d},
\qquad |G_{ab}|<1\quad(a\ne b).
\]
The Gram matrix \(G\) may be singular. Let every label \(y_a\) be a nonzero real number; arbitrary sign labels are included. Fix \(\sigma_1,\sigma_2,\kappa_1,\kappa_2,\kappa_3>0\).

Use \(\phi^{(1)}\) and \(\phi^{(2)}\) for the two activations. In the simple sufficient class both are bounded, nonconstant, continuously differentiable, with bounded derivatives. Initialize the first-layer population roots by
\[
Z_{0,a}^{(1)}
=\frac{\sigma_1 g^\top x_a}{\sqrt d},
\qquad g\sim N(0,I_d),
\]
the middle action by the joint forward/adjoint limit of an independent matrix with entries \(N(0,\sigma_2^2/n)\), and the rescaled population readout by \(W_0^{(3)}=0\).

The network quantities are
\[
H_a^{(1)}=\phi^{(1)}(Z_a^{(1)}),
\qquad
Z_a^{(2)}=W^{(2)}H_a^{(1)},
\qquad
H_a^{(2)}=\phi^{(2)}(Z_a^{(2)}),
\]
\[
f_a=\mathbb E[W^{(3)}H_a^{(2)}],
\qquad r_a=f_a-y_a,
\qquad L=\sum_a r_a^2,
\]
\[
\delta_a^{(2)}=W^{(3)}(\phi^{(2)})'(Z_a^{(2)}),
\qquad
\delta_a^{(1)}
=(\phi^{(1)})'(Z_a^{(1)})(W^{(2)})^*\delta_a^{(2)}.
\]
Suppose the limiting flow satisfies
\[
\begin{aligned}
\dot Z_a^{(1)}
&=-2\kappa_1\sum_bG_{ab}r_b\delta_b^{(1)},\\
\dot W^{(2)}
&=-2\kappa_2\sum_b r_b\delta_b^{(2)}\otimes H_b^{(1)},\\
\dot W^{(3)}
&=-2\kappa_3\sum_b r_bH_b^{(2)},
\end{aligned}\tag{1}
\]
where \((u\otimes v)V=u\mathbb E[vV]\). Write \(\|U\|_{L^2}=\sqrt{\mathbb E[U^2]}\) for root-mean-square size; the operator norm measures its largest amplification. Require continuity of the field variables in mean square and of the middle action in operator norm, with the corresponding integral equations valid in those norms. The bounded continuous activation derivatives then justify the directional chain rules used below. The two neuron populations remain separate; every expectation pairs coordinates of the same layer.

There is a fixed \(T_*>0\) on which the following hold:

- For every input, both hidden preactivations move nontrivially. Their RMS speeds are positive for every \(0<t\le T_*\), of order \(t\); their squared displacements are of order \(t^4\).
- The trained middle matrix moves nontrivially when applied to each fixed initial first-layer activation.
- All three kernel blocks are positive definite for \(0<t\le T_*\), and each block is nonconstant.
- The summed loss has a uniformly negative slope, including at initialization.
- Every hidden marginal has variance and best-affine-fit error for its activation bounded below by positive constants on \([0,T_*]\).

The time and constants depend on the fixed data, activations, labels, and positive parameters, but not on width or learning rate. Strict positivity is not claimed uniformly as the inputs become parallel, labels approach zero, or other nondegeneracy parameters approach their boundaries.

#### Why the first activation Gram matrix is positive definite

The key geometric fact needs no high derivatives or analyticity.

**Bounded ridge-function independence.** If \(\phi\) is bounded, continuous, and nonconstant, then the functions
\[
w\longmapsto\phi\!\left(\frac{w^\top x_a}{\sqrt d}\right),
\qquad a=1,\ldots,m,
\]
are linearly independent whenever the inputs are pairwise nonparallel.

To prove it, suppose a linear combination with coefficients \(c_a\) is zero for every \(w\), and select \(a\) with \(c_a\ne0\). For every \(b\ne a\), set
\[
\xi_{ab}
=
\frac{x_a/\sqrt d-G_{ab}x_b/\sqrt d}{1-G_{ab}^2}.
\]
Then
\[
\frac{x_a^\top\xi_{ab}}{\sqrt d}=1,
\qquad
\frac{x_b^\top\xi_{ab}}{\sqrt d}=0.
\]
For a vector \(v\), let \(\Delta_v F(w)=F(w+v)-F(w)\). Apply the commuting differences
\[
\prod_{b\ne a}\Delta_{h\xi_{ab}}
\]
to the proposed linear identity. Every term other than the \(a\)-th is killed by one of these differences. Each difference shifts the \(a\)-th scalar argument by \(h\). Therefore
\[
\Delta_h^{m-1}\phi(s)=0
\qquad\text{for every }s,h\in\mathbb R.
\tag{2}
\]
For fixed \(s,h\), the bounded sequence \(a_j=\phi(s+jh)\), \(j\ge0\), has vanishing \((m-1)\)-st differences. This forces it to be constant: its \((m-2)\)-nd difference is constant; if that constant were nonzero, the next lower difference would grow linearly, contradicting boundedness of every difference of a bounded sequence. Repeating gives \(a_{j+1}=a_j\). For \(m=2\) this is immediate from (2), and \(m=1\) is immediate from nonconstancy. Consequently \(\phi(s+h)=\phi(s)\) for every \(s,h\), contradicting nonconstancy. This proves the claim.

Now define
\[
Q_{ab}=\mathbb E[H_{0,a}^{(1)}H_{0,b}^{(1)}].
\tag{3}
\]
If \(c^\top Qc=0\), then \(\sum_a c_a\phi^{(1)}(\sigma_1g^\top x_a/\sqrt d)=0\) almost surely. Continuity and the full support of \(\sigma_1g\) make this an identity for all \(w\). The preceding argument forces \(c=0\). Hence \(Q\) is positive definite, even when \(G\) is singular.

There is a useful broader version. If \(\phi^{(1)}\) is nonaffine and continuously differentiable with bounded derivative, then its derivative is bounded, continuous, and nonconstant. Differentiate a putative ridge identity in a direction \(v\) with \(v^\top x_a\ne0\) for all \(a\); such a direction avoids finitely many proper hyperplanes. It gives a linear identity among the ridge functions of \((\phi^{(1)})'\), with coefficients \(c_a v^\top x_a/\sqrt d\). Bounded ridge-function independence again makes every \(c_a=0\). Thus \(Q\succ0\) also holds for unbounded nonaffine first activations with bounded continuous derivative.

#### Positive response covariances, including activation flat parts

Write
\[
Y_a:=Z_{0,a}^{(2)}.
\]
The tuple \(Y\) is centered Gaussian with covariance \(\sigma_2^2Q\), so it has full support in \(\mathbb R^m\). Define the following recurring quantities:
\[
\begin{aligned}
S&=\sum_a y_a\phi^{(2)}(Y_a),
&U_a&=S(\phi^{(2)})'(Y_a),\\
P_a&=(W_0^{(2)})^*U_a,
&B_a&=(\phi^{(1)})'(Z_{0,a}^{(1)})P_a,\\
V_{ab}&=\mathbb E[U_aU_b],
&D_{ab}&=\mathbb E[B_aB_b].
\end{aligned}\tag{4}
\]

The matrix \(V\) is positive definite. Suppose \(\sum_a c_aU_a=0\) almost surely. Continuity and Gaussian full support imply, for every \(s\in\mathbb R^m\),
\[
\left(\sum_a y_a\phi^{(2)}(s_a)\right)
\left(\sum_a c_a(\phi^{(2)})'(s_a)\right)=0.
\tag{5}
\]
Where the first factor is nonzero, the second is zero. If the first factor is zero and some \((\phi^{(2)})'(s_a)\ne0\), its corresponding partial derivative \(y_a(\phi^{(2)})'(s_a)\) is nonzero; arbitrarily close points have a nonzero first factor, so continuity again makes the second factor zero. If all activation derivatives at that point vanish, the second factor is already zero. Consequently
\[
\sum_a c_a(\phi^{(2)})'(s_a)=0
\qquad\text{for every }s.
\]
The derivative \((\phi^{(2)})'\) is nonconstant, because a bounded nonconstant activation cannot have constant derivative. Varying one coordinate forces each \(c_a=0\). No division by \(S\) was used: \(S\) is allowed to vanish on a set of positive probability.

For the broader conditional class, boundedness of \(\phi^{(2)}\) can be replaced here by nonaffinity and a bounded continuous derivative. The derivative remains nonconstant, and all the necessary moments exist because \(\phi^{(2)}\) has at most linear growth on the Gaussian input.

Conditioning the initial Gaussian matrix on its initial forward calls gives
\[
P_a
=
\sum_c H_{0,c}^{(1)}
\left[Q^{-1}\mathbb E[YU_a]\right]_c
+\Gamma_a,
\qquad
\Gamma\sim N(0,\sigma_2^2V),
\tag{6}
\]
where \(\Gamma\) is independent of the first-layer roots. This is the reused-transpose response, not a replacement of the transpose by an independent matrix. The deterministic response in (6) retains the information from the initial forward uses.

For any deterministic \(c\ne0\), the conditional Gaussian covariance gives
\[
\begin{aligned}
\mathbb E\left[\left(\sum_a c_aB_a\right)^2\right]
&\ge
\sigma_2^2\lambda_{\min}(V)
\sum_a c_a^2
\mathbb E[((\phi^{(1)})'(Z_{0,a}^{(1)}))^2]\\
&>0.
\end{aligned}\tag{7}
\]
Each final expectation is positive: a continuously differentiable nonconstant function has a nonzero derivative on an interval, and every first-layer Gaussian marginal has full support. Therefore \(D\succ0\), even if the derivative is zero on large sets or changes sign.

#### Each input moves in both hidden layers

Set
\[
T_a=\sum_bG_{ab}y_bB_b,
\qquad
M_a=\sum_b y_bQ_{ab}U_b,
\]
\[
A_a=(\phi^{(1)})'(Z_{0,a}^{(1)})T_a,
\qquad
R_a^\kappa
=\kappa_2M_a+\kappa_1W_0^{(2)}A_a.
\tag{8}
\]
Each \(T_a\) is nonzero in mean square. Its coefficient vector against \(B\) has \(a\)-th entry \(G_{aa}y_a=y_a\ne0\), and \(D\succ0\).

Each \(R_a^\kappa\) is also nonzero, but this requires more than positivity of an aggregate sum. Subtract the mean-square projection of \(A_a\) onto \(\operatorname{span}\{H_{0,b}^{(1)}\}\):
\[
\alpha_a=Q^{-1}\mathbb E[H_0^{(1)}A_a],
\qquad
A_a^\perp
=A_a-\sum_b\alpha_{a,b}H_{0,b}^{(1)}.
\tag{9}
\]
Conditional on the first-layer roots, \(A_a\) is linear in \(\Gamma\) with coefficients
\[
c_b
=(\phi^{(1)})'(Z_{0,a}^{(1)})
G_{ab}y_b
(\phi^{(1)})'(Z_{0,b}^{(1)}).
\]
Its \(a\)-th coefficient is
\[
c_a=y_a((\phi^{(1)})'(Z_{0,a}^{(1)}))^2,
\]
which is nonzero with positive probability. Since \(V\succ0\),
\[
\mathbb E[(A_a^\perp)^2]
\ge
\mathbb E\operatorname{Var}(A_a\mid Z_0^{(1)})
=\sigma_2^2\mathbb E[c^\top Vc]>0.
\tag{10}
\]

Conditioning the same initial matrix on both sets of known calls,
\[
W_0^{(2)}H_{0,b}^{(1)}=Y_b,
\qquad
(W_0^{(2)})^*U_b=P_b,
\]
gives the next forward response
\[
W_0^{(2)}A_a
=
\sum_b\alpha_{a,b}Y_b
+\sum_b\beta_{a,b}U_b
+\sigma_2\sqrt{\mathbb E[(A_a^\perp)^2]}\,\gamma_a,
\qquad
\beta_a=V^{-1}\mathbb E[PA_a^\perp].
\tag{11}
\]
Here \(\gamma_a\) is standard Gaussian independent of the previous second-layer coordinates. The formula is the finite Gaussian conditional mean plus the unused matrix randomness: the input component in (9) has the displayed squared norm, while projection of the fresh output off finitely many previous output directions disappears in normalized mean square. Positive definiteness of \(Q,V\) justifies both inverses. A separate marginal calculation for each \(a\) is sufficient; independence between the different \(\gamma_a\) is not claimed.

The term \(M_a\) depends only on \(Y\), and hence cannot cancel this independent Gaussian component. Therefore
\[
\mathbb E[(R_a^\kappa)^2]
\ge
\kappa_1^2\sigma_2^2\mathbb E[(A_a^\perp)^2]
>0.
\tag{12}
\]
The learned-matrix contribution \(M_a\) is separately nonzero: its coefficient vector \((y_bQ_{ab})_b\) against \(U\) has nonzero \(a\)-th entry \(y_aQ_{aa}\), and \(V\succ0\).

At initialization \(r_a(0)=-y_a\) and \(W^{(3)}(0)=0\). Dividing the integral equations by the indicated powers of \(t\) gives
\[
\begin{aligned}
W^{(3)}(t)&=2\kappa_3tS+o_{L^2}(t),\\
\delta_a^{(2)}(t)&=2\kappa_3tU_a+o_{L^2}(t),\\
Z_a^{(1)}(t)-Z_{0,a}^{(1)}
&=2\kappa_1\kappa_3t^2T_a+o_{L^2}(t^2),\\
W^{(2)}(t)-W_0^{(2)}
&=2\kappa_2\kappa_3t^2
\sum_b y_bU_b\otimes H_{0,b}^{(1)}+o_{\mathrm{op}}(t^2),\\
Z_a^{(2)}(t)-Y_a
&=2\kappa_3t^2R_a^\kappa+o_{L^2}(t^2).
\end{aligned}\tag{13}
\]
For example the readout equation first gives its \(t\)-coefficient. Multiplication by the bounded continuous derivative gives the backward \(t\)-coefficient. The first-layer and middle-matrix integrals then start at order \(t^2\). In the last equation, the learned-matrix term is \(\kappa_2M_a\), while the moving first activation gives \(\kappa_1W_0^{(2)}A_a\). Bounded derivatives justify these activation difference quotients by dominated convergence along mean-square converging increments.

Direct substitution in (1) also gives
\[
\frac{\dot Z_a^{(1)}(t)}t
\longrightarrow 4\kappa_1\kappa_3T_a,
\qquad
\frac{\dot Z_a^{(2)}(t)}t
\longrightarrow 4\kappa_3R_a^\kappa
\quad\text{in }L^2.
\tag{14}
\]
Thus every hidden RMS speed is bounded above and below by positive constants times \(t\), on a fixed sufficiently short interval. For the first layer,
\[
\mathbb E[(Z_a^{(1)}(t)-Z_{0,a}^{(1)})^2]
=4\kappa_1^2\kappa_3^2\mathbb E[T_a^2]t^4+o(t^4),
\]
\[
\int_0^t\mathbb E[|\dot Z_a^{(1)}(s)|^2]\,ds
=\frac{16}{3}\kappa_1^2\kappa_3^2\mathbb E[T_a^2]t^3+o(t^3).
\tag{15}
\]
For the second layer replace \(\kappa_1^2\mathbb E[T_a^2]\) by \(\mathbb E[(R_a^\kappa)^2]\). In particular the speed is zero initially, not bounded below by a positive constant as \(t\downarrow0\). It is nonzero at every fixed positive time in the asserted interval.

#### The kernel, loss, and surviving nonlinearity

The physical kernel is \(K=\kappa_1K^{(1)}+\kappa_2K^{(2)}+\kappa_3K^{(3)}\), with
\[
K_{ab}^{(1)}=G_{ab}\mathbb E[\delta_a^{(1)}\delta_b^{(1)}],
\]
\[
K_{ab}^{(2)}
=\mathbb E[H_a^{(1)}H_b^{(1)}]
\mathbb E[\delta_a^{(2)}\delta_b^{(2)}],
\qquad
K_{ab}^{(3)}=\mathbb E[H_a^{(2)}H_b^{(2)}].
\tag{16}
\]
Let \(\circ\) denote entrywise matrix multiplication. Although \(G\) may be singular, \(G\circ D\) is positive definite. Decompose \(G=\sum_j v_jv_j^\top\). Then
\[
G\circ D
=\sum_j\operatorname{diag}(v_j)D\operatorname{diag}(v_j)
\succeq
\lambda_{\min}(D)\operatorname{diag}(G_{11},\ldots,G_{mm})
=\lambda_{\min}(D)I.
\tag{17}
\]
The same argument makes \(Q\circ V\) positive definite, since its diagonal entries \(Q_{aa}\) are positive. Define
\[
A_1=y^\top(G\circ D)y>0,
\qquad
A_2=y^\top(Q\circ V)y>0.
\tag{18}
\]
Adjunction yields
\[
\sum_a y_a\mathbb E[U_aR_a^\kappa]
=\kappa_1A_1+\kappa_2A_2.
\tag{19}
\]
The kernel expansions are therefore
\[
\begin{aligned}
\kappa_1K^{(1)}(t)
&=4\kappa_1\kappa_3^2t^2(G\circ D)+o(t^2),\\
\kappa_2K^{(2)}(t)
&=4\kappa_2\kappa_3^2t^2(Q\circ V)+o(t^2),\\
y^\top K^{(3)}(t)y
&=\mathbb E[S^2]
+4\kappa_3(\kappa_1A_1+\kappa_2A_2)t^2+o(t^2),\\
y^\top K(t)y
&=\kappa_3\mathbb E[S^2]
+8\kappa_3^2(\kappa_1A_1+\kappa_2A_2)t^2+o(t^2).
\end{aligned}\tag{20}
\]
The initial readout block is positive definite: a linear dependence among \(\phi^{(2)}(Y_a)\) would hold for all \(Y\) by full support, and varying one coordinate forces its coefficient to zero. All three blocks are therefore positive definite for sufficiently small positive time. The first two start at zero with positive definite \(t^2\) coefficients, and the third increases in the label direction. Each block, and the total kernel, is nonconstant.

The summed loss satisfies
\[
L(0)=\sum_a y_a^2,
\qquad
-\dot L(0)=4\kappa_3\mathbb E[S^2]>0.
\]
Continuity allows the time interval to be shortened so that
\[
-\dot L(t)\ge2\kappa_3\mathbb E[S^2]>0
\qquad(0\le t\le T_*).
\tag{21}
\]
This does not assert that every individual residual magnitude decreases.

Every initial hidden marginal is a nondegenerate Gaussian. A bounded nonconstant continuous activation cannot agree with an affine function on its full support. Thus the best-affine-fit error
\[
\inf_{\alpha,\beta}
\mathbb E[(\phi^{(\ell)}(Z)-\alpha Z-\beta)^2]
=
\operatorname{Var}(\phi^{(\ell)}(Z))
-\frac{\operatorname{Cov}(Z,\phi^{(\ell)}(Z))^2}
{\operatorname{Var}(Z)}
\tag{22}
\]
is initially positive. The same is true for the broader nonaffine activation class. Bounded derivatives make both activations globally Lipschitz, so these moments vary continuously along the mean-square continuous paths. All \(2m\) variances and all \(2m\) affine-fit errors retain common positive lower bounds on a possibly shorter \([0,T_*]\).

#### Sufficient checks beyond the simple activation class

The positivity argument uses the following concrete sufficient conditions, rather than monotonicity or analyticity:

1. The initial first-activation Gram matrix \(Q\) is positive definite.
2. On the full-support second-layer Gaussian tuple, the Gram matrix \(V\) of \(U_a=S(\phi^{(2)})'(Y_a)\) is positive definite.
3. For every input, \(\mathbb E[((\phi^{(1)})'(Z_{0,a}^{(1)}))^2]>0\).
4. For the separate nonlinear-fit conclusion, each activation is nonaffine on its initial Gaussian support.

These checks are sufficient, not necessary. In conjunction with bounded continuous derivatives and the assumed strong flow, they yield the calculations above. The bounded nonconstant activation class guarantees all of them automatically for pairwise nonparallel inputs and nonzero labels. More broadly, both activations may be unbounded but nonaffine with bounded continuous derivatives: the differentiated ridge argument proves the first check, the proof of (5) proves the second, and Gaussian initialization plus linear growth supplies the required initial moments. This broader statement concerns strict activity conditional on existence; it must not be used to enlarge an independently proved existence theorem without checking that theorem's hypotheses.

Some excluded cases show why nondegeneracy matters. Identical inputs with opposite labels can give \(S=0\) identically and a frozen zero-readout system. Antiparallel inputs with odd activations and equal labels can do the same. A constant first activation has zero first-layer derivative; a constant second activation has zero backward derivative. An affine first activation can make \(Q\) singular when there are more inputs than their linear span dimension. An affine second activation has identical derivative functions, so \(V\) has rank at most one for \(m>1\). Such cases can still have some learning, but the full collection of strict conclusions above is not automatic. Finally, allowing a zero label can invalidate the per-input initial activity assertion, for example for an orthogonal input decoupled from the other labeled inputs.


#### Weighted-loss activity and the exact kernel direction

For the weighted loss in C.1, \(\mathcal L=\sum_a\omega_a(f_a-y_a)^2\), put \(p_a=\omega_a y_a\) in this paragraph. Retain every hypothesis of C.3, including Gaussian first weights, zero population readout and nonzero labels. The unweighted kernel blocks in C.3 are unchanged, and
\[
 \dot f_a=-2\sum_bK_{ab}\omega_b r_b,\qquad
 \dot{\mathcal L}=-4\sum_{a,b}\omega_a r_aK_{ab}\omega_b r_b.
\]
In C.3's definitions of S,U,B,T,M,A and R, and its onset expansions, replace each training label y_b by p_b. Then, with \(D_{ab}=E[B_aB_b]\), \(V_{ab}=E[U_aU_b]\),
\[
 A_1=p^\top(G\circ D)p>0,\qquad A_2=p^\top(Q\circ V)p>0,
\]
\[
 p^\top K(t)p=\kappa_3 ES^2+
 8\kappa_3^2(\kappa_1A_1+\kappa_2A_2)t^2+o(t^2),
 \qquad-\dot{\mathcal L}(0)=4\kappa_3 ES^2>0.
\]
This substitution is justified directly in the raw equations: the factor at initialization is \(-\omega_b r_b(0)=\omega_b y_b\); every first nonzero hidden term is obtained by integrating that factor against the first readout term. All positive-definiteness arguments only require the corresponding p_a to be nonzero, which follows from positive weights and nonzero labels. In the upper-layer acceleration the learned term is a function of the original upper forward tuple, while the forward image of the lower-layer increment has an independent Gaussian component of positive variance. Multiplying by the upper activation derivative preserves a positive squared norm because that derivative is nonzero with positive Gaussian probability. Thus every sample's activation, as well as its preactivation, has nonzero order-t^2 displacement and order-t speed. The quadratic kernel direction is p, not y, for this weighted statement. No initialization variance is inserted in the trained rank-one terms.

## D. Uniformly separated two-sample offset activations

This family has three hidden layers, activation 1+z+e arctan(z), binary labels and rho in [-1,1-delta], 0<delta<=2. In particular the antipodal endpoint is admitted. The complete source and endpoint arguments are included below; the finite Gaussian and observation dependencies are the contained chapter proofs III.F and III.V. Constants are selected from delta before choosing a dataset. The coefficient is small; no practical-amplitude conclusion is asserted.

### D.1. Separated-angle offset theorem

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Statement and the exact model

Fix \(0<\delta\le2\). There is \(e_\delta>0\), depending only on
\(\delta\), with the following property. Choose any fixed
\(0<e\le e_\delta\) and use
\[
                 \phi_e(z)=1+z+e\arctan z                 \tag{1}
\]
in all three hidden layers. For every fixed \(d\ge1\), every two
deterministic inputs and labels satisfying
\[
 x_1,x_2\in\mathbb R^d,\quad \|x_a\|^2/d=1,\quad
 \rho=x_1^Tx_2/d\in[-1,1-\delta],\quad y_a\in\{-1,1\},     \tag{2}
\]
the full L3 population/GF/raw-GD theorem below holds. Correlations not
realizable at a particular \(d\) impose no requirement. The endpoint
\(\rho=-1\) is included.

Here is the finite model, fixing all normalizations. At width \(n\),
let \(W^1\in\mathbb R^{n\times d}\), \(W^2,W^3\in\mathbb R^{n\times n}\),
and \(C\in\mathbb R^n\). Initialize all entries independently with laws
\[
 W^1_{ij}\sim N(0,1/d),\quad W^2_{ij},W^3_{ij}\sim N(0,1/n),
 \quad C_i\sim N(0,n^{-2}).                              \tag{3}
\]
Use \(\frac{( u)^\top(v)}{n}=u^Tv/n\). For \(a=1,2\), define
\[
 z_a^1=W^1x_a,\quad h_a^\ell=\phi_e(z_a^\ell),\quad
 z_a^2=W^2h_a^1,\quad z_a^3=W^3h_a^2,\quad
 f_a=\frac{( C)^\top(h_a^3)}{n},\quad r_a=f_a-y_a.
\]
Nonlinearities and vector products act coordinatewise. Backward vectors
exclude the residual:
\[
 b_a^3=C\phi_e'(z_a^3),\quad
 b_a^2=\phi_e'(z_a^2)(W^3)^Tb_a^3,\quad
 b_a^1=\phi_e'(z_a^1)(W^2)^Tb_a^2.                        \tag{4}
\]
The loss is \(\mathcal L=(r_1^2+r_2^2)/2\). Its gradient flow uses
\[
 \|\dot\Theta\|_{\rm raw}^2
 =\frac dn\|\dot W^1\|_F^2+\|\dot W^2\|_F^2
       +\|\dot W^3\|_F^2+\frac{\|\dot C\|_2^2}{n},
\]
and therefore has equations
\[
 \dot W^1=-\frac1d\sum_a r_ab_a^1x_a^T,\quad
 \dot W^\ell=-\frac1n\sum_a r_ab_a^\ell(h_a^{\ell-1})^T
       \quad(\ell=2,3),\quad
 \dot C=-\sum_a r_ah_a^3.                                \tag{5}
\]
Raw GD is simultaneous Euler for exactly (5), with step \(\eta_n=n^{-2}\).
Raw parameters are interpolated linearly at physical times \(k\eta_n\);
hidden fields are recomputed from that interpolation. Hidden velocities
at nodes are right derivatives, with left derivatives at the terminal
endpoint. The finite readout in (3) is never reset to zero.

The conclusions are:

1. **Global population flow.** On the canonical generated Gaussian action
   spaces there is one autonomous uncut population solution for all
   \(t\ge0\). It is strong, has bounded primal quantities on compact
   intervals, is unique against bounded-primal strong competitors on
   the same action spaces, and has unique continuation from each reached
   state. Its state consists of a first-layer \(\mathbb R^d\)-valued
   field, two bounded operators with actual adjoints and Hilbert--Schmidt
   training increments, and a readout field. These are finitely many
   objects, not a claim of finite scalar dimension.
2. **Joint limits.** For every deterministic \(T<\infty\), finite GF and
   the exact raw GD converge along the full width sequence in probability
   to that flow, with the observable scope specified in Section 2.
   Predictions, loss, all four raw kernel blocks, hidden paths, and the
   stipulated recomputed hidden velocities and squared speeds converge.
   Both orientations of both initialized and trained actions are retained.
3. **Nontriviality.** At every finite physical time, every layer/sample
   has strictly positive best affine activation-approximation error.
   Every hidden parameter block and each sample's hidden features have
   nonzero initial acceleration, and the projected total kernel changes
   near zero. This is a positive small-time feature-learning certificate,
   not nonzero velocity at every later individual instant.

The same \(e\) works for all data in (2) and every finite \(T\).
Convergence and stability constants may depend on the fixed data,
\(d,e,T\). There is no supremum over datasets inside a probabilistic
limit, no interchange of \(T\to\infty\) and \(n\to\infty\), and no
selection of one activation for all \(\delta>0\). The activation is (1),
not the different bounded one-sample activation \(1+\arctan(z)/10\).

#### 2. Population notation, observables, and the supplied lemmas

Write \(H_\ell=L^2(\Omega_\ell,\mu_\ell)\), \(\ell=1,2,3\), for three
separate neuron spaces. Inner products use the indicated layer's
probability measure. There is no coordinatewise pairing of neurons in
different layers. The first weight field is
\(w\in L^2(\Omega_1;\mathbb R^d)\). The current actions are
\(A:H_1\to H_2\), \(B:H_2\to H_3\), and the readout is \(C\in H_3\).
For \(u\in H_j,v\in H_i\), \(u\otimes v:H_i\to H_j\) maps \(q\)
to \(u\langle v,q\rangle_i\).

Population equations are (4)--(5), replacing normalized finite sums by
these inner products, transposes by actual adjoints, and normalized
outer products by \(\otimes\). The initial readout is zero in this
limit. Initial action norms are at most 10 on the canonical generated
spaces. The first projected pair is centered Gaussian with covariance
\(\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)\).
These are conclusions of the canonical construction, not extra
initialization assumptions.

The four raw kernel blocks are
\[
 K^1_{ab}=\rho_{ab}\langle b_a^1,b_b^1\rangle_1,\quad
 K^2_{ab}=\langle b_a^2,b_b^2\rangle_2\langle h_a^1,h_b^1\rangle_1,
\]
\[
 K^3_{ab}=\langle b_a^3,b_b^3\rangle_3\langle h_a^2,h_b^2\rangle_2,
 \qquad K^4_{ab}=\langle h_a^3,h_b^3\rangle_3,             \tag{6}
\]
where \(\rho_{aa}=1\) and \(\rho_{12}=\rho_{21}=\rho\).
Their convergence and prediction/loss convergence are uniform on
\([0,T]\). For each layer, empirical joint two-sample
preactivation/feature path laws converge in
\(\mathcal W_2(C([0,T];\mathbb R^4))\), with the supremum norm.
The joint same-layer laws including recomputed preactivation and feature
velocities converge in \(\mathcal W_2\), uniformly in time; fixed finite
collections of times also have joint \(\mathcal W_2\) convergence.
Second moments and integrated squared speeds converge. Operator
statements concern canonical generated probes, their joint laws and
both actions, and strong comparisons of learned increments on common
spaces. They do not assert operator-norm convergence of unrelated
finite matrices under an unspecified cross-width identification.

* **Affine/radial facts:** Fragment D.4, Sections 3--7,
  constructs the affine \(\phi_0=1+z\) scalar-feature gradient path.
  For \(g=\frac12\sum_a y_af_a\), feature time \(s\), and
  \(\kappa_0=\|\frac12\sum_a y_ah^3_{a,0}\|_3^2\), it gives
  \(g'\ge\kappa_0\), \(\|C'\|_3^2\ge\kappa_0\),
  \(\int_0^s\|\Theta'\|_{\rm raw}^2=g(s)\), and a bounded affine
  path through its first hit \(S\) of \(g=3/2\). It proves Gaussianity
  of its hidden preactivations, the common/contrast identities used
  below, and the initial kernel formula (7).
* **Uniform parameter interface of the response lemma:**
  Fragment D.2, Sections 3--8, and
  Fragment D.3, Sections 1--7, show that if
  affine Euler prefixes of duration at most \(s_0\) obey primal bound
  \(p\ge1\), there is \(\mathcal E(p,s_0)>0\), independent of the
  correlation, labels, width, mesh and caps, such that every
  \(0\le e\le\mathcal E(p,s_0)\) has bounded nonlinear response
  coefficients and \(\|Q\|_{L^q}\le K\sqrt q\), \(q\ge2\), for the
  actual readout and both reverse queries. Its auxiliary backward gate
  is \(q+e(1+z^2)^{-1}\tau_R(q)\), with only the nonlinear part clipped.
  Learned memories and current-source returns are retained.
* **Comparison and global bridge:**
  Fragment D.5, Sections 1--4, gives
  raw strong comparison with the affine path, cap removal, physical
  time conversion, uniqueness and restart, and finite GF/raw-GD and
  observable limits, when response tails and the endpoint margin
  \(g_{e,R}(S)>1\) hold. special-data Section III.V supplies its
  velocity bridge.
* **Initial motion:** Fragment D.6 proves the stated
  initial feature and parameter motion and changing-kernel certificate
  for every fixed \(e>0\), every \(\rho<1\), and both label sectors,
  once the regular population path exists.

The response lemma's parameter interface can be checked explicitly.
Its equation (4) permits
\[
 A_0=2(24p^2\exp{36p^2s_0}+\tfrac92p^4),\qquad
 M_0=2s_0(8p^2\exp{36p^2s_0}+p^4).
\]
Its equation (65) permits
\[
 \mathcal E(p,s_0)=
 \min\left\{1,\frac1{480p^2s_0\exp{36p^2s_0}},
                    \frac1{2K \exp{Ks_0}}\right\},          \tag{R}
\]
where one \(K\ge1\) is obtained from the finite stage estimates using
only \(p,s_0,A_0,M_0\). No lower covariance eigenvalue enters. Geometry
enters there only through
\(\|\Gamma\operatorname{diag}(y/2)\|_{\infty\to\infty}\le1\).
Thus fixed numerical \(p,s_0\) select one threshold, not uncontrolled
pointwise choices. Below \(s_0>0\).

#### 3. A uniformly bounded affine reference interval

Fix arbitrary data satisfying (2). For the affine model,
\[
 \kappa_0=
 \begin{cases}(7+\rho)/2,&y_1=y_2,\\
               (1-\rho)/2,&y_1=-y_2.
 \end{cases}                                            \tag{7}
\]
In either case \(\kappa_0\ge\delta/2\). Put
\[
 S_\delta=3/\delta,\qquad R_\delta=3/\sqrt{2\delta},
 \qquad U=11+R_\delta.                                  \tag{8}
\]
Until the first affine hit of \(g=3/2\), the radial and energy
estimates give
\[
 S\le\frac{3}{2\kappa_0}\le S_\delta,\qquad
 \|\Theta(s)-\Theta(0)\|_{\rm raw}
 \le\sqrt{s\,g(s)}\le\frac{3}{2\sqrt{\kappa_0}}
 \le R_\delta.                                         \tag{9}
\]
Existence through the hit follows from the polynomial affine field's
bounded-ball local Lipschitzness and its strong endpoint energy
estimate, as proved in the affine lemma. This uses no nonlinear
continuation.

Every projected first-layer norm, both current action norms, and the
readout norm on \([0,S]\) are at most \(U\): their initial bounds are
1, 10, 10, 0, and the raw displacement controls their changes. The full
initial first-row norm \(\sqrt d\|w_0\|_{L^2}=\sqrt d\) need not be
bounded independently of \(d\); only its projections and raw displacement
enter activation selection.

The endpoint \(S\) may depend on the data. No affine path is extended
beyond its own hit to \(S_\delta\). Every use of \(S_\delta\) below
is an upper bound on the duration of its prefixes.

#### 4. Uniform nondegeneracy and a positive nonlinear margin

For the affine reference set
\(M_\ell=(z_1^\ell+z_2^\ell)/2\),
\(D_\ell=(z_1^\ell-z_2^\ell)/2\), and \(v_D=(1-\rho)/2\).
For opposite labels \(y=(\sigma,-\sigma)\),
\[
 D_2=AD_1,\qquad D_3=BD_2,\qquad C'=\sigma D_3.
\]
The radial lower bound \(\|C'\|^2\ge\kappa_0=v_D\) and
\(\|A\|,\|B\|\le U\) give, for every \(s\in[0,S]\),
\[
 \|D_3\|^2\ge v_D,\qquad
 \|D_2\|^2\ge v_D/U^2,\qquad
 \|D_1\|^2\ge v_D/U^4.                                 \tag{10}
\]
These also hold at zero. Affine sign symmetry gives
\(E D_\ell=E[M_\ell D_\ell]=0\), and hence
\(\operatorname{Var}(z_a^\ell)=\operatorname{Var}(M_\ell)+\|D_\ell\|^2\).
For same labels, the affine contrast is frozen in each population,
has variance \(v_D\), and has zero common/contrast covariance: this is
the conditional-Gaussian argument in equation (44) of the affine lemma.
Both sectors therefore satisfy
\[
 \operatorname{Var}(z_{a,0}^{\ell}(s))\ge m^2,\qquad
                m=\frac{\sqrt{\delta/2}}{U^2}>0.         \tag{11}
\]
The subscript 0 here denotes the affine activation, not initial time.
No input Gram inverse is used, including at \(\rho=-1\).

Affine forward propagation and the bound \(U\) give
\[
 \|z_{a,0}^1\|_2\le U,\quad
 \|z_{a,0}^2\|_2\le2U^2,\quad
 \|z_{a,0}^3\|_2\le3U^3=:L.                             \tag{12}
\]
For a scalar variable with positive variance, define
\[
 \mathcal R(Z)=\inf_{\alpha,\beta\in\mathbb R}
 E[(\arctan Z-\alpha-\beta Z)^2]
 =\operatorname{Var}(\arctan Z)
 -\frac{\operatorname{Cov}(Z,\arctan Z)^2}
                {\operatorname{Var}(Z)}.                \tag{13}
\]
For \(G\sim N(0,1)\), define
\[
 \eta=\min_{|\mu|\le L,\ m\le\sigma\le L}
                         \mathcal R(\mu+\sigma G).       \tag{14}
\]
This depends only on \(\delta\) and is positive. Coupling all variables
using the same \(G\), bounded Lipschitz arctangent and the lower variance
bound make (13) continuous in \((\mu,\sigma)\). A zero error would
identify arctangent with an affine function Gaussian-almost everywhere,
and hence everywhere by full support and continuity, contrary to its
nonconstant derivative. Compactness of this explicit parameter
rectangle then gives a positive minimum. Affine Gaussianity and
(11)--(12) imply, uniformly over all reference intervals,
\[
                    \mathcal R(z_{a,0}^{\ell}(s))\ge\eta. \tag{15}
\]
Compactness is used on Gaussian parameters, not on an unspecified
pointwise threshold.

Here is a quantitative stability version. Suppose
\(\|Z-Z_0\|_2\le t\), \(\operatorname{sd}(Z_0)\ge m\), and
\(\mathcal R(Z_0)\ge\eta\). If \(t\le m/2\), then
\(\operatorname{sd}(Z)\ge m/2\), because centering is an orthogonal
projection in \(L^2\). The optimal regression slope for arctangent
of \(Z\) has magnitude at most \(\pi/m\), by Cauchy--Schwarz and
\(\operatorname{sd}(\arctan Z)\le\pi/2\). Using its intercept and slope
as a competitor for \(Z_0\), the triangle inequality gives
\[
 \sqrt{\mathcal R(Z_0)}
 \le\sqrt{\mathcal R(Z)}+(1+\pi/m)t.
\]
Consequently
\[
 t\le\min\left\{m/2,\frac{\sqrt\eta}{2(1+\pi/m)}\right\}
       \quad\Longrightarrow\quad\mathcal R(Z)\ge\eta/4.   \tag{16}
\]
No Gaussianity of \(Z\) is required in this stability statement.

#### 5. Selecting one coefficient from the separation alone

All constants in this section depend only on \(\delta\). Set
\[
 b=4U,\quad Q=40b^3S_\delta \exp{9b^2S_\delta},\quad
 J=12b^2Q+\pi b^2,\quad O=10b^3Q+b(J+\pi/2).              \tag{17}
\]
Affine Euler on its reference interval has projected primal bound
\(2U\) for sufficiently fine meshes, by its bounded-ball Euler
estimate. Source-baseline equation (32) supplies the finite-array
affine bound
\[
                         p=11+2U+4S_\delta(2U)^3.        \tag{18}
\]
Apply the response lemma at these fixed numerical arguments to select
\(\mathcal E(p,S_\delta)>0\). Mesh families for a dataset stop at its
own \(S\); all durations are at most \(S_\delta\). Thus (18) verifies
the affine premise without assuming a uniform-in-data limit theorem.

Define
\[
 e_\delta=\frac12\min\left\{
  1,\mathcal E(p,S_\delta),\frac b{4Q},\frac1{4O},
  \frac m{2J},\frac{\sqrt\eta}{2(1+\pi/m)J}
                                      \right\}>0.       \tag{19}
\]
This uses only finite bounds from the response lemma and the fixed
Gaussian minimization (14). It uses no actual input pair, trajectory,
width, or physical horizon. An optimal coefficient or numerical
optimization is unnecessary.

We verify every smallness use. For \(0<e\le e_\delta\), compare an
auxiliary nonlinear-cap feature flow with its affine reference on
the same canonical action spaces. On a projected primal ball of
radius \(b\), the direct comparison in the supplied bridge gives,
in the sum of raw component difference norms,
\[
                    \sup_{s\le S}E(s)\le Qe.             \tag{20}
\]
The affine path has primal bound \(U=b/4\). The restriction
\(Qe<b/4\) leaves strict room before nonlinear exit. A stopped
comparison therefore proves existence and (20) through \(S\) for
every finite cap, uniformly in that cap. The same estimate holds
for sufficiently fine Euler prefixes. Only the affine vector field
is used for the Lipschitz comparison.

For completeness, (20) gives a preactivation comparison with the
explicit constant \(J\). Both states have projected primal sizes
at most \(b\), and \(\|h_e^1\|\le4b\), \(\|h_e^2\|\le7b^2\),
\(\|h_e^3\|\le10b^3\). First \(\|z_e^1-z_0^1\|\le E\).
Expanding the second-layer action gives
\[
 \|z_e^2-z_0^2\|
 \le4b\|A_e-A_0\|_{\rm op}
           +b(\|z_e^1-z_0^1\|+\pi e/2)
 \le5bE+(\pi/2)be.
\]
The third-layer expansion gives
\[
 \|z_e^3-z_0^3\|
 \le7b^2E+b(5bE+(\pi/2)be+(\pi/2)e)
 \le12b^2E+\pi b^2e.
\]
Hence for every layer and sample,
\[
                    \sup_{s\le S}\|z_e^\ell-z_0^\ell\|_2\le Je.
                                                               \tag{21}
\]
The subscript 0 on an operator in these comparisons denotes its
affine-reference current value, not its initialized value.

For the projected prediction, Cauchy--Schwarz and
\(\sum_a|y_a/2|=1\) give
\[
 |g_{e,R}(S)-g_0(S)|
 \le10b^3E(S)+b(J+\pi/2)e\le Oe<1/4.
\]
Thus \(g_{e,R}(S)>5/4\) for every finite cap. The response lemma
supplies actual cap- and mesh-uniform subGaussian bounds on
\(C,q^2,q^1\), because \(e\le\mathcal E(p,S_\delta)\).
Every premise has been discharged with constants selected before
the data.

Equations (19),(21),(16) give
\(\mathcal R(z_e^\ell(s))\ge\eta/4\). After cap removal the same
strong comparison gives this for the uncut path. Absorbing \(1+Z\)
into the free affine approximant gives the exact identity
\[
 \inf_{\alpha,\beta}E[(\phi_e(Z)-\alpha-\beta Z)^2]
                         =e^2\mathcal R(Z).
\]
The uncut feature path therefore satisfies
\[
 \inf_{a,\ell,\ s\in[0,S]}\ \inf_{\alpha,\beta}
 E[(\phi_e(z_a^\ell(s))-\alpha-\beta z_a^\ell(s))^2]
                          \ge e^2\eta/4>0.               \tag{22}
\]

#### 6. The global flow, raw GD and observables

We detail the application of the supplied bridge, so that the affine
reference is not mistaken for the target dynamics.

The response \(L^q\) estimates give Gaussian \(L^2\) tail bounds for
the actual incoming fields. The asymmetric cap comparison has error
at most
\[
                 C\exp\{C(1+eR)S-cR^2\}\longrightarrow0. \tag{23}
\]
Only the reference path requires tails; a competitor does not. Thus
the cap family converges strongly, including its Hilbert--Schmidt
increments and raw directions, to an autonomous uncut \(C^1\)
feature-gradient path through \(S\).

The endpoint margin and constructed sample symmetry give a first
hit \(s_*<S\) of \(g=1\). Radial coercivity applies to this actual
strong gradient path. Its initial projected kernel is positive for
both label sectors, including \(\rho=-1\), by the initial Gaussian
calculation in the affine/radial lemma. Thus \(g'>0\) before fitting.

For this population path, \(f_a=y_ag\). Define
\[
 t(s)=\int_0^s\frac{du}{2(1-g(u))},\qquad 0\le s<s_*.     \tag{24}
\]
Its inverse satisfies \(ds/dt=2(1-g)\), converting the feature
gradient to exactly the population loss gradient (5). The kernel
is continuous and bounded on \([0,S]\); hence for some finite \(M\),
\(1-g(s)\le M(s_*-s)\). The integral (24) diverges at \(s_*\).
This single path therefore supplies every finite physical horizon,
and the nonaffinity margin (22) holds at every such time with no
further restriction on \(e\).

The finite dynamics do not have exact sample symmetry. As required
by the bridge, they are compared with same-width fixed-cap physical
systems using both actual residuals at every update. Fixed-program
Gaussian identification, deterministic fixed-cap Euler errors, and
stopped comparisons identify these references. On each fixed
physical \([0,T]\), cap-removal error has the form
\(C_T\exp(C_TR-cR^2)\), which tends to zero for every finite \(T\)
without further amplitude smallness. The same asymmetric
physical-field estimate proves uniqueness against any bounded-primal
strong physical competitor, including a nonsymmetric one. Applying
it at a reached time proves unique restart there.

For exact raw GD the extra reference-comparison error is
\(C_{R,T}\eta_n\). Width tends to infinity at each fixed cap and
auxiliary mesh, deterministic Euler estimates remove the auxiliary
mesh, and then the cap is removed. This identifies the full diagonal
scheme \(\eta_n=n^{-2}\), without a Gaussian theorem for a growing
number of queries. The small random finite readout (3) is retained.

The fixed-cap velocity lemma requires bounded primal paths,
bounded-derivative coordinate maps at fixed cap, and the fixed-program
construction, all supplied here. To remove the cap for velocities,
its deterministic comparison first fixes a truncation of a reference
preactivation velocity. Population cap velocities converge strongly
to the uncut velocity, whose \(L^2\) time image is compact. Sending
the cap to infinity at fixed truncation, then the truncation to
infinity, controls products of a gate difference and that velocity.
This is the ordered limit in the bridge's Section 4; it requires
no growth bound on cap-dependent moment constants. It yields
the velocity and second-moment scope in Section 2; products of
strongly converging \(L^2\) factors give (6).

For path laws the bridge uses
\[
 \|x-I_hx\|_{C([0,T])}^2
                         \le4h\int_0^T|x'(t)|^2\,dt,
\]
where \(I_h\) interpolates on a fixed observation grid. Averaging
this coupling bound, using the squared-speed bounds and then sending
the observation mesh to zero, upgrades finite-time laws to the
claimed path-space \(\mathcal W_2\) limits. Hidden velocities and
path laws are not inferred merely from weak state convergence.

The initial-motion lemma applies to every positive \(e\) in (19).
It retains the full Gaussian source and both reused-transpose
returns; its relevant feature-Gram matrices are positive even at
antipodal inputs. If \(V\) denotes initial hidden acceleration in
feature time, it gives nonzero blocks and sample feature accelerations,
and
\[
 \kappa(s)=\kappa(0)+2s^2\|V\|_{\rm hidden}^2+o(s^2),
                         \quad \|V\|_{\rm hidden}>0,
\]
where \(\kappa=\frac14y^T(\sum_{\ell=1}^4K^\ell)y\).
Since \(s(t)=2t+o(t)\), the certificate holds at small positive
physical times. It needs only \(e>0\), with no further
data- or \(T\)-dependent threshold. Together with (22), it discharges
all nontriviality requirements. The conclusions of Section 1 follow.

#### 7. Logical extent

The quantifier proved is
\[
 \forall\delta\in(0,2]\ \exists e_\delta>0\
 \forall e\in(0,e_\delta]\
 \forall(d,x_1,x_2,y_1,y_2)\text{ satisfying (2)}\
 \forall T<\infty.
\]
Each limit is one global autonomous trajectory whose restrictions
give the compact-time convergence assertions. This is not convergence
uniformly over the whole half-line. The proof gives no positive
lower bound for \(e_\delta\) as \(\delta\downarrow0\), and does not
show that such a bound is impossible. It does not turn the known
nonlazy certificate into perpetual nonzero motion at each instant,
or identify (1) with the earlier bounded one-sample activation.

The fixed Gaussian action and singular-query construction is III.F with A.1–A.2. The observable bridge is III.V. D.2–D.6 verify the model-specific hypotheses.

### D.2. Exact two-sample source system and affine probe proof

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Raw coordinates, labels, and the finite program

Write

\[
 c_a=y_a/2,\qquad
 R_x=(\rho_{ab})_{a,b=1}^2=
 \begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},
 \qquad -1\le\rho<1.
\]

Thus \(\sum_a|c_a|=1\) and
\(\sum_b|c_b\rho_{ab}|\le1\). Use a positive mesh
\(0=s_0<\cdots<s_N\le S\), with
\(h_j=s_{j+1}-s_j\). Equal steps give \(h_j=\Delta\).
The symbols \(W_{2,j},W_{3,j},C_j\) denote the two hidden matrices and
the rescaled readout. A finite rank-one operator is
\(u\otimes v=uv^T/n\), and \(\frac{( u)^\top(v)}{n}=u^Tv/n\).

At initialization, \(W_{2,0},W_{3,0}\) are the two independent Gaussian
matrices with entry variance \(1/n\), independent of the first-layer
root. A first-layer neuron has
\(w_0\sim N(0,I_d/d)\) and
\(Z^{(1)}_{0,a}=w_0\cdot x_a\), so its two coordinates have covariance
\(R_x\). The stated readout initialization has normalized norm
\(O_{\mathbb P}(n^{-1})\) and population limit zero. Initially take
\(C_0=0\) in the displayed population/source programs; the small finite
readout is treated below.

The uncut forward and backward calls are

\[
 H^{(1)}_{j,a}=\phi(Z^{(1)}_{j,a}),\quad
 Z^{(2)}_{j,a}=W_{2,j}H^{(1)}_{j,a},\quad
 H^{(2)}_{j,a}=\phi(Z^{(2)}_{j,a}),
\]
\[
 Z^{(3)}_{j,a}=W_{3,j}H^{(2)}_{j,a},\quad
 H^{(3)}_{j,a}=\phi(Z^{(3)}_{j,a}),\quad
 \delta^{(3)}_{j,a}=C_j\phi'(Z^{(3)}_{j,a}),
\]
\[
 q^{(2)}_{j,a}=W_{3,j}^T\delta^{(3)}_{j,a},\quad
 \delta^{(2)}_{j,a}=\phi'(Z^{(2)}_{j,a})q^{(2)}_{j,a},\quad
 q^{(1)}_{j,a}=W_{2,j}^T\delta^{(2)}_{j,a},\quad
 \delta^{(1)}_{j,a}=\phi'(Z^{(1)}_{j,a})q^{(1)}_{j,a}.
\]

Products within a vector/population are coordinatewise. The stated
label-directed feature Euler updates are exactly

\[
 Z^{(1)}_{j+1,a}=Z^{(1)}_{j,a}
       +h_j\sum_b c_b\rho_{ab}\delta^{(1)}_{j,b},
\tag{1}
\]
\[
 W_{\ell,j+1}=W_{\ell,j}
       +h_j\sum_b c_b\delta^{(\ell)}_{j,b}
                              \otimes H^{(\ell-1)}_{j,b},
 \quad \ell=2,3,
\]
\[
 C_{j+1}=C_j+h_j\sum_b c_b H^{(3)}_{j,b}.
\tag{2}
\]

Equivalently the first field updates by
\(w_{j+1}=w_j+h_j\sum_b c_b\delta^{(1)}_{j,b}x_b/d\).
Taking its inner product with \(x_a\) gives (1), including the factor
\(1/d\) in the stated model. No scalar change of first-layer coordinates is
made. In particular, two separate applications of the one-sample
transformation would not give (1).

For \(\rho=-1\), \(x_2=-x_1\), and (1) preserves
\(Z^{(1)}_{j,2}=-Z^{(1)}_{j,1}\). Everything below uses \(R_x\) directly;
there is no division by \(1+\rho\), \(1-\rho\), or \(\det R_x\).

These are the feature equations with coefficients \(c_a=y_a/2\).
The contract's physical equations instead have coefficients
\(-r_a=y_a-f_a\). For the uncut system, adjunction and the raw metric
give

\[
 \frac{df_a}{ds}=\sum_b c_b K_{ab},\qquad
 K_{ab}=\sum_{\ell=1}^4K^{(\ell)}_{ab},
\]
\[
 K^{(1)}_{ab}=\rho_{ab}\,\mathbb E_1[\delta^{(1)}_a\delta^{(1)}_b],
 \quad
 K^{(2)}_{ab}=\mathbb E_2[\delta^{(2)}_a\delta^{(2)}_b]
                     \mathbb E_1[H^{(1)}_aH^{(1)}_b],
\]
\[
 K^{(3)}_{ab}=\mathbb E_3[\delta^{(3)}_a\delta^{(3)}_b]
                     \mathbb E_2[H^{(2)}_aH^{(2)}_b],\qquad
 K^{(4)}_{ab}=\mathbb E_3[H^{(3)}_aH^{(3)}_b].
\tag{3}
\]

For example, differentiating \(\mathbb E_3[C H^{(3)}_a]\), then
substituting each forward derivative and moving each matrix through its
inner product, gives successively the four terms in (3). The first-layer
term is \(\sum_b c_b\rho_{ab}\mathbb E_1[\delta^{(1)}_a\delta^{(1)}_b]\)
by (1). Thus the off-diagonal blocks have the stated raw normalization.
A single physical clock would require the physical coefficient vector
to be proportional to \((c_1,c_2)\) along the trajectory; this proof unit makes
no such additional assertion.

#### 2. The main route's nonlinear-part clips in raw coordinates

Use precisely the activation and backward map specified by main:

\[
 \phi_e(z)=1+z+e\arctan z,\qquad
 \mathcal D_R(z,q)=q+e g(z)\tau_R(q),\qquad
 g(z)=\frac1{1+z^2},\quad e\ge0.
\]

Here \(\tau_R\) is a smooth clip, \(|\tau_R'|\le1\),
\(|\tau_R(q)|\le\min\{|q|,2R\}\), equal to the identity on
\([-R,R]\). The forward activation is always \(\phi_e\), with no clip.
Replace only the backward coordinate maps by

\[
 \delta^{(3)}_{j,a}=\mathcal D_R(Z^{(3)}_{j,a},C_j),\qquad
 \delta^{(2)}_{j,a}=\mathcal D_R(Z^{(2)}_{j,a},q^{(2)}_{j,a}),\qquad
 \delta^{(1)}_{j,a}=\mathcal D_R(Z^{(1)}_{j,a},q^{(1)}_{j,a}).
\tag{4}
\]

All linear backward terms remain intact. At \(e=0\), (4) is the exact
uncut affine backward calculation at every clipping level. With
\(\tau_R(q)=q\), (4) becomes the uncut gate
\(\phi_e'(z)q\).

For fixed \(R\), the partial derivatives are

\[
 \partial_z\mathcal D_R(z,q)=e g'(z)\tau_R(q),\qquad
 \partial_q\mathcal D_R(z,q)=1+e g(z)\tau_R'(q).
\]

Since \(|g'|\le1\), their absolute values are at most \(2eR\) and
\(1+e\). Thus this coordinate map is globally Lipschitz. In the raw
first-layer update the uncontrolled uncut multiplier would be
\(e g'(Z^{(1)})q^{(1)}\). It is the nonlinear part involving
\(q^{(1)}\) that must additionally be clipped, alongside the part
involving \(q^{(2)}\) in the middle layer. At the top the analogous
multiplier is \(e g'(Z^{(3)})C\); the top instance of (4) clips this
nonlinear readout contribution too. An \(L^2\) primal bound on a
multiplier alone does not bound its multiplication operator on \(L^2\).
This explains all three cap locations without imposing a cap on any
linear term or on the forward activation.

Both \(\phi_e\) and (4) are continuously differentiable globally
Lipschitz coordinate instructions with bounded first derivatives at
fixed \(R,e\). On bounded operator and vector-norm sets,
matrix actions and the rank-one updates are locally Lipschitz, since

\[
 \|u\otimes v-\widetilde u\otimes\widetilde v\|_{\rm op}
 \le\|u-\widetilde u\|_2\|v\|_2
        +\|\widetilde u\|_2\|v-\widetilde v\|_2.
\]

This supplies the local Lipschitz flow/Euler comparison on such sets.
It does not by itself assert global boundedness for an unbounded
activation, or cutoff removal for a nonlinear model.

#### 3. Two-sample source representation at a fixed mesh

Index every Gaussian source by both time and sample. There are four
mutually independent centered Gaussian groups

\[
 \xi^{(2)}=(\xi^{(2)}_{j,a}),\quad
 \xi^{(3)}=(\xi^{(3)}_{j,a}),\quad
 \zeta^{(1)}=(\zeta^{(1)}_{j,a}),\quad
 \zeta^{(2)}=(\zeta^{(2)}_{j,a}),
\]

independent also of the first-layer Gaussian pair. The pair belongs to
population 1, \((\xi^{(2)},\zeta^{(2)})\) to population 2, and
\(\xi^{(3)}\) to population 3; \(\zeta^{(1)}\) belongs to population 1.
Separate populations have no paired neuron coordinates. For \(\ell=2,3\),

\[
 \mathbb E[\xi^{(\ell)}_{j,a}\xi^{(\ell)}_{v,b}]
    =\mathbb E_{\ell-1}[H^{(\ell-1)}_{j,a}H^{(\ell-1)}_{v,b}],
\]
\[
 \mathbb E[\zeta^{(\ell-1)}_{j,a}\zeta^{(\ell-1)}_{v,b}]
    =\mathbb E_\ell[\delta^{(\ell)}_{j,a}\delta^{(\ell)}_{v,b}].
\tag{5}
\]

These are full second moments of the matrix inputs, including means and
all cross-sample terms. They can be singular.

The raw bottom recursion is

\[
 Z^{(1)}_{k,a}=Z^{(1)}_{0,a}
   +\sum_{j<k}h_j\sum_b c_b\rho_{ab}
       \mathcal D_R(Z^{(1)}_{j,b},q^{(1)}_{j,b}).
\tag{6}
\]

For \(\ell=2,3\), define the deterministic two-sample coefficient arrays

\[
 A^{(\ell)}_{ka,jb}
   =\mathbb E_{\ell-1}
       \frac{\partial H^{(\ell-1)}_{k,a}}
            {\partial\zeta^{(\ell-1)}_{j,b}}
       +h_j c_b\,
          \mathbb E_{\ell-1}[H^{(\ell-1)}_{k,a}H^{(\ell-1)}_{j,b}],
 \quad j<k,
\tag{7}
\]
\[
 D^{(\ell)}_{ka,jb}
   =\mathbb E_\ell
       \frac{\partial\delta^{(\ell)}_{k,a}}
            {\partial\xi^{(\ell)}_{j,b}}
     +\mathbf1_{j<k}h_j c_b\,
          \mathbb E_\ell[\delta^{(\ell)}_{k,a}\delta^{(\ell)}_{j,b}],
 \quad j\le k.
\tag{8}
\]

We use \(D\) for the coefficient called `b` in the one-sample proof,
to reserve \(B\) for the primal bound below. The complete scalar equations
are

\[
 Z^{(\ell)}_{k,a}=\xi^{(\ell)}_{k,a}
       +\sum_{j<k}\sum_b A^{(\ell)}_{ka,jb}\delta^{(\ell)}_{j,b},
\]
\[
 q^{(\ell-1)}_{k,a}=\zeta^{(\ell-1)}_{k,a}
       +\sum_{j\le k}\sum_b D^{(\ell)}_{ka,jb}H^{(\ell-1)}_{j,b},
 \qquad \ell=2,3,
\tag{9}
\]

together with \(H^{(\ell)}=\phi_e(Z^{(\ell)})\), (4), (6), and

\[
 C_k=\sum_{j<k}h_j\sum_b c_bH^{(3)}_{j,b}.
\tag{10}
\]

Every derivative in (7)--(8) is the derivative of the explicit finite
scalar expression, holding all deterministic coefficients and covariance
parameters fixed. A source coordinate has its own formal argument even
when its Gaussian law equals another coordinate or is identically zero.
No derivative of a covariance square root is taken. Notice that the
response parts of (7)--(8) have no extra factor \(c_b\); label factors
already enter their derivative paths through (6) and (10). Only the
learned-rank additions have the explicit factor \(h_jc_b\).

Here is the precise extension of the finite-program dependency. Unroll
both trained matrices into their independent initial matrices and the
rank-one sums in (2). The extra forward term is

\[
 \sum_{j<k,b}h_jc_b\delta^{(\ell)}_{j,b}
                 \frac{( H^{(\ell-1)}_{j,b})^\top(H^{(\ell-1)}_{k,a})}{n},
\]

and the extra transpose term is

\[
 \sum_{j<k,b}h_jc_bH^{(\ell-1)}_{j,b}
                 \frac{(\delta^{(\ell)}_{j,b})^\top(\delta^{(\ell)}_{k,a})}{n}.
\]

For each initial matrix, the Gaussian conditioning rule of the dependency
states that an answer to \(Wh\) has limiting form

\[
 \xi_h+\sum_{j,b}u_{j,b}\,
                     \mathbb E\partial_{\zeta_{j,b}}h,
\tag{11}
\]

where \(u_{j,b}\) are its previously queried transpose inputs and
\(\operatorname{Cov}(\zeta)=\mathbb E[uu^T]\). The hypotheses there are a
fixed finite program, iid root tuples independent of the Gaussian
matrices with finite second moments, and globally Lipschitz continuously
differentiable coordinate instructions with bounded first derivatives.
They hold for (4). Multiple sample slots just add finitely many matrix
queries. Both matrices, both orientations, and the joint first-layer root
are retained. Equation (11) follows there by conditioning on both
orientations, projecting away reference forward inputs, and using Gaussian
integration by parts against the reference transpose-source group. Interleaving
the other independent matrix does not discard any derivative path.

Freeze the finitely many learned contractions at the expectations
constructed causally by (5)--(10). Applying (11) to that program and then
adding its learned terms gives (7)--(9). Each frozen contraction concerns
nodes already available. Fixed-step empirical convergence of these nodes
makes the actual contraction errors tend to zero. The rank-one norm
inequality and a finite induction through the coordinate and matrix
instructions then transfer the same joint empirical \(W_2\) limit to
the actual feedback program.

The chronological order at a time is: both layer-2 forward queries, both
layer-3 forward queries, both layer-3 transpose queries, both layer-2
transpose queries, then the parameter updates. Therefore the forward
response sums have \(j<k\) and the transpose response sums have \(j\le k\).
There is no artificial triangular order between the samples at a given
stage. All coefficients required at a stage have been determined by the
previous stages of this order.

Singular query Gram matrices, including those at \(\rho=-1\) and from a
zero readout, are covered by the dependency's fixed-program independent
query-noise regularization and its continuous zero-noise limit. Its
hypotheses continue to hold for the pair of root coordinates and the clips
here. That argument uses continuity of Gaussian covariance square roots
and of the formal finite expressions, without inverting a limiting
singular Gram matrix. Individual coefficients follow the stated formal
extension convention; their contracted corrections are invariant.

For the uncut affine activation, the same argument applies directly:
after the learned contractions are frozen, every coordinate instruction
is affine and has a bounded derivative. The finite induction transferring
contractions uses only finitely many finite norms. It requires no
mesh-uniform primal assumption to identify any one fixed mesh. At that
mesh, changing the initial readout by \(O_{\mathbb P}(n^{-1})\) changes
the calculation by \(o_{\mathbb P}(1)\) through this same induction.

#### 4. The derivative rows and current-time returns

The following equations specify the derivative paths that replace the
one-sample calculation for (4). Write
\(d^{(\ell)}_{j,a}=\phi_e'(Z^{(\ell)}_{j,a})\), and set
\(m^{(1)}=q^{(1)},m^{(2)}=q^{(2)},m^{(3)}=C\), with the readout shared
between samples. Define the local backward partial derivatives

\[
 p^{(\ell)}_{j,a}
   =e g'(Z^{(\ell)}_{j,a})\tau_R(m^{(\ell)}_{j,a}),\qquad
 v^{(\ell)}_{j,a}
   =1+e g(Z^{(\ell)}_{j,a})\tau_R'(m^{(\ell)}_{j,a}).
\]

For \(\ell=3\), the notation \(m^{(3)}_{j,a}\) means \(C_j\).
For a bottom source \(\zeta^{(1)}_{v,b}\), put
\(J_{k,a}=\partial_{\zeta^{(1)}_{v,b}}Z^{(1)}_{k,a}\).
Then \(J_{0,a}=0\), \(\partial H^{(1)}_{k,a}=d^{(1)}_{k,a}J_{k,a}\), and

\[
 J_{k+1,a}=J_{k,a}+h_k\sum_u c_u\rho_{au}
 \left[
 p^{(1)}_{k,u}J_{k,u}
 +v^{(1)}_{k,u}
   \left(\mathbf1_{(k,u)=(v,b)}
    +\sum_{j\le k,w}D^{(2)}_{ku,jw}d^{(1)}_{j,w}J_{j,w}\right)
 \right].
\tag{12}
\]

In particular the direct current query has a cross-sample effect

\[
 \frac{\partial H^{(1)}_{k+1,a}}
      {\partial\zeta^{(1)}_{k,b}}
 =h_k c_b\rho_{ab}
   d^{(1)}_{k+1,a}v^{(1)}_{k,b}.
\tag{13}
\]

For a source in population 2, let \(\partial\) denote its formal
derivative. The exact middle recursions are

\[
 \partial Z^{(2)}_{k,a}
  =\partial\xi^{(2)}_{k,a}
       +\sum_{j<k,b}A^{(2)}_{ka,jb}\partial\delta^{(2)}_{j,b},
\]
\[
 \partial q^{(2)}_{k,a}
  =\partial\zeta^{(2)}_{k,a}
       +\sum_{j\le k,b}D^{(3)}_{ka,jb}d^{(2)}_{j,b}
                                      \partial Z^{(2)}_{j,b},
\]
\[
 \partial\delta^{(2)}_{k,a}
  =p^{(2)}_{k,a}\partial Z^{(2)}_{k,a}
      +v^{(2)}_{k,a}\partial q^{(2)}_{k,a}.
\tag{14}
\]

For a population-3 source,

\[
 \partial Z^{(3)}_{k,a}
  =\partial\xi^{(3)}_{k,a}
       +\sum_{j<k,b}A^{(3)}_{ka,jb}\partial\delta^{(3)}_{j,b},
\]
\[
 \partial C_k=\sum_{j<k,b}h_jc_b d^{(3)}_{j,b}
                                      \partial Z^{(3)}_{j,b},
\]
\[
 \partial\delta^{(3)}_{k,a}
  =v^{(3)}_{k,a}\partial C_k
       +p^{(3)}_{k,a}\partial Z^{(3)}_{k,a}.
\tag{15}
\]

All sums over samples in (12)--(15) are retained. In particular the
current middle transpose return is the full block

\[
 D^{(3)}_{ka,kb}
    =\mathbf1_{a=b}\,\mathbb E[p^{(3)}_{k,a}],
\]
\[
 D^{(2)}_{ka,kb}
  =\mathbf1_{a=b}\,
       \mathbb E[p^{(2)}_{k,a}]
    +D^{(3)}_{ka,kb}\,
       \mathbb E[v^{(2)}_{k,a}d^{(2)}_{k,b}].
\tag{16}
\]

Thus the same-time return through the other matrix is present, including
its sample indices. For this particular explicit Euler schedule the
off-diagonal entries in the current block are zero: \(C_k\) uses only
strictly earlier top features, and each current forward preactivation
has only its own current formal forward source. Equation (16) proves
these zeros; cross-sample source correlations do not turn formal partial
derivatives into derivatives along the Gaussian support. Earlier-time
blocks are generally full. Equations (13)--(16) retain the actual
cross-sample propagation and do not assume independent sample copies.

#### 5. Affine primal hypothesis and a deterministic response estimate

From now on set \(\phi_0(z)=1+z\) and remove every clip. Then

\[
 \delta^{(3)}_a=C,\qquad
 \delta^{(2)}_a=W_3^TC,\qquad
 q^{(1)}_a=W_2^TW_3^TC.
\tag{17}
\]

These are identities on the actual unperturbed affine network. The
formally named sample sources remain separate, as required in Section 3.

Here is a precise primal-bound hypothesis, using the usual normalized
finite vector norm \(\frac{\|v\|_2}{\sqrt n}=\|v\|_2/\sqrt n\).

**Primal hypothesis P(B,S).** Let \(B\ge1\). For every mesh under
consideration with \(s_N\le S\), the actual unforced affine Euler states
satisfy, with probability tending to one as width tends to infinity,

\[
 \max_{k\le N}
 \max\{\max_a\frac{\|Z^{(1)}_{k,a}\|_2}{\sqrt n},
        \|W_{2,k}\|_{\rm op},\|W_{3,k}\|_{\rm op},\frac{\|C_k\|_2}{\sqrt n}\}
 \le B.
\tag{18}
\]

The same \(B\) is used for all meshes. The width limit here is at each
fixed mesh; a probability bound uniform over an increasing number of
meshes is not required. A strict margin can always be supplied by
enlarging an available bound. Section 8 explains how a population primal
bound supplies (18), so this formulation does not require an additional
operator-norm convergence theorem.

For two states use the norm of their difference

\[
 d(\theta,\widetilde\theta)
  =\max_a\frac{\|Z^{(1)}_a-\widetilde Z^{(1)}_a\|_2}{\sqrt n}
    +\|W_2-\widetilde W_2\|_{\rm op}
    +\|W_3-\widetilde W_3\|_{\rm op}
    +\frac{\|C-\widetilde C\|_2}{\sqrt n}.
\tag{19}
\]

All forthcoming deterministic estimates hold identically for population
\(L^2\) norms and bounded actions. Put

\[
 b=2B,\qquad L=9b^2=36B^2,\qquad E=\exp(LS).
\tag{20}
\]

On the ball with each of the four primal sizes at most \(b\),

\[
 \frac{\|H^{(1)}_a\|_2}{\sqrt n}\le2b,\quad
 \frac{\|H^{(2)}_a\|_2}{\sqrt n}\le3b^2,\quad
 \frac{\|H^{(3)}_a\|_2}{\sqrt n}\le4b^3,
\]
\[
 \frac{\|\delta^{(3)}_a\|_2}{\sqrt n}\le b,\quad
 \frac{\|\delta^{(2)}_a\|_2}{\sqrt n}\le b^2,\quad
 \frac{\|q^{(1)}_a\|_2}{\sqrt n}\le b^3.
\]

Let \(\mathcal V_0\) be the four-component raw affine vector field from (1)--(2).
Its four components have Lipschitz constants, with respect to (19),
bounded respectively by \(b^2,2b^2,3b^2,3b^2\). To verify this, write
the individual state differences as \(u,v,w,t\) in the order in (19).
The forward and backward differences obey

\[
 \frac{\|\Delta H^{(1)}_a\|_2}{\sqrt n}\le u,\quad
 \frac{\|\Delta H^{(2)}_a\|_2}{\sqrt n}\le bu+2bv,
\]
\[
 \frac{\|\Delta H^{(3)}_a\|_2}{\sqrt n}\le b^2u+2b^2v+3b^2w,
 \quad
 \frac{\|\Delta\delta^{(2)}_a\|_2}{\sqrt n}\le b(w+t),
\]
\[
 \frac{\|\Delta q^{(1)}_a\|_2}{\sqrt n}\le b^2(v+w+t).
\]

Insert these inequalities into the updates, use the rank-one difference
inequality, \(\sum|c_a|=1\), and
\(\sum_b|c_b\rho_{ab}|\le1\). The matrix-2 component is bounded by
\(b^2u+2b^2w+2b^2t\), and the matrix-3 component by
\(b^2u+2b^2v+3b^2t\). This gives the claimed constants and hence

\[
 d(\mathcal V_0(\theta),\mathcal V_0(\widetilde\theta))
       \le Ld(\theta,\widetilde\theta),
 \qquad \|\mathcal V_0(\theta)\|\le10b^3.
\tag{21}
\]

Here the first notation means the sum/max component norm, applied to the
two vector-field values. No coordinate supremum or matrix Frobenius
bound growing with width enters (21).

Next add external vector errors to exactly one class of intermediate
answers: to \(Z^{(2)}_{j,a}\), \(Z^{(3)}_{j,a}\),
\(q^{(2)}_{j,a}\), or \(q^{(1)}_{j,a}\), immediately after its trained
matrix call and before using the answer. This is also an additive error
after its unrolled initial-matrix answer and learned correction. Later
calls and parameter updates are recomputed. If the errors at a time
have norm at most \(e_j\), the change of the vector field at a fixed
state in this ball is bounded by \(\kappa e_j\), where

| Source/answer perturbed | Affected update components | \(\kappa\) |
| --- | --- | ---: |
| \(\xi^{(2)} / Z^{(2)}\) | \(W_3,C\) | \(2b\) |
| \(\xi^{(3)} / Z^{(3)}\) | \(C\) | \(1\) |
| \(\zeta^{(2)} / q^{(2)}\) | \(Z^{(1)},W_2\) | \(3b\) |
| \(\zeta^{(1)} / q^{(1)}\) | \(Z^{(1)}\) | \(1\) |

For example, a middle forward error \(e_a\) adds
\(C\otimes\sum_a c_ae_a\) to the \(W_3\) update and
\(W_3\sum_a c_ae_a\) to the \(C\) update, each of norm at most \(be_j\).
A middle transpose error adds at most \(be_j\) to the first-layer
update and \(2be_j\) to the \(W_2\) update. This proves the table.

Take errors \(\varepsilon\alpha_{j,a}g\), where
\(|\alpha_{j,a}|\le1\) are deterministic and \(g\) is a single vector
in the population where the answers live. The same vector is reused at
all chosen times and sample slots. Discrete Gronwall applied to (21)
and the table gives

\[
 d(\theta^\varepsilon_k,\theta^0_k)
       \le \kappa S E|\varepsilon|\frac{\|g\|_2}{\sqrt n}.
\tag{22}
\]

If only one source time \(j<k\) is perturbed, the sharper bound is
\(\kappa h_jE|\varepsilon|\frac{\|g\|_2}{\sqrt n}\). Indeed the error is introduced
in the state update at time \(j\), with its factor \(h_j\), and subsequent
factors are bounded by \(\prod_{r>j}(1+Lh_r)\le E\).

The comparison remains in the ball used in its derivation. On (18) and
\(\frac{\|g\|_2}{\sqrt n}\le2\), choose fixed \(|\varepsilon|\) so small that
\(2\kappa S E|\varepsilon|<B/2\). Induction through the recurrence
gives this same strict bound at every next node, starting from zero
state difference. Thus the perturbed state cannot leave the ball of
radius \(b=2B\). This justifies (22) without a primal assumption on a
perturbed trajectory. The case \(S=0\) has no state update and is direct.

#### 6. The Gaussian probe identity for formal derivatives

This section proves the connection used to convert (22) into source
bounds. It uses finite differences; no interchange of a width limit with
an unproved derivative or normalized-trace limit is needed.

Fix a mesh, an output coordinate expression \(V\) in one population, and
one of the source groups in that same population. Denote this group by
\(\eta=(\eta_{j,a})\). Take an iid \(N(0,1)\) vector \(g\), independent
of the entire initial network, and insert the errors
\(\varepsilon\alpha_{j,a}g\) at the corresponding answers as above.
There is no pairing of this vector with coordinates in another layer.
Run both the unperturbed and perturbed finite programs, sharing the
initial matrices and roots.

At any fixed \(\varepsilon\), apply Section 3 to the perturbed program
with \(g\) as an extra root in its own population. Use its own query
slots and coefficient recursion, so the formal convention is exactly
the one in (7)--(9). Consequently

\[
 \frac{( g)^\top(V^\varepsilon_n)}{n}
       \ \longrightarrow\ \mathbb E[G V^\varepsilon]
       \quad\hbox{in probability},
\tag{23}
\]

where \(G\sim N(0,1)\). The scalar source groups of the perturbed
program are independent of this root. Their deterministic covariance
parameters and learned/source coefficients may depend on \(\varepsilon\).
This independence is exactly the independent-root conclusion of the
finite Gaussian conditioning rule, and does not assert independence
between a trained answer and the root that was inserted into it.

For the affine activation, with these deterministic coefficients fixed,
every scalar coordinate is an affine function of the root tuple and
the four Gaussian groups. This follows by finite induction from
(6), (9), (10), since every gate is the constant one. Let

\[
 T_{V,ja}(\varepsilon)=\partial_{\eta_{j,a}}V^\varepsilon
\]

be its deterministic formal coefficient. The only explicit appearances
of \(G\) in the scalar instructions are the inserted additions
\(\varepsilon\alpha_{j,a}G\). Their positions are exactly those of the
named source arguments. Differentiating this affine expression with
respect to \(G\), with the deterministic coefficients fixed, yields

\[
 \partial_G V^\varepsilon
       =\varepsilon\sum_{j,a}\alpha_{j,a}T_{V,ja}(\varepsilon),
 \qquad
 \mathbb E[G V^\varepsilon]
       =\varepsilon\sum_{j,a}\alpha_{j,a}T_{V,ja}(\varepsilon).
\tag{24}
\]

For the second equality, write the affine expression as
\(U+\varepsilon(\sum\alpha T)G\), where \(U\) is independent of
\(G\), then use \(\mathbb EG=0\), \(\mathbb EG^2=1\).
Equivalently it is the one-dimensional Gaussian integration-by-parts
identity. This establishes the probe identity, including its coefficient
normalization and which formal derivatives it measures.

For completeness, \(T_{V,ja}(\varepsilon)\to T_{V,ja}(0)\) at this
fixed mesh. Induct through the causal order in Section 3: affine
coordinate coefficients are continuous functions of earlier
deterministic coefficients; their second moments are continuous
functions of those coefficients and the earlier covariance entries.
Expected formal derivatives are their deterministic affine
coefficients. These observations pass every next covariance and
coefficient continuously. Gaussian square-root continuity, including
at singular covariance, supplies a joint realization if one is wanted.
There is no inverse covariance in this induction.

Since \(V^0_n\) is independent of the new root, conditionally on the
unperturbed network this pairing is centered Gaussian with variance
\(\frac{\|V^0_n\|_2^2}{n}/n\). Its tight normalized norm, supplied by the
unperturbed fixed-program limit, therefore gives
\(\frac{( g)^\top(V^0_n)}{n}\to0\) in probability. If a stability estimate gives

\[
 \frac{\|V^\varepsilon_n-V^0_n\|_2}{\sqrt n}
       \le C|\varepsilon|\frac{\|g\|_2}{\sqrt n}
\]

on events of probability tending to one, Cauchy--Schwarz gives
\(|\frac{( g)^\top(V^\varepsilon_n-V^0_n)}{n}|/|\varepsilon|
\le C\frac{\|g\|_2^2}{n}\).
First take width to infinity at fixed nonzero \(\varepsilon\), using
(23)--(24) and \(\frac{\|g\|_2}{\sqrt n}\to1\). Then send \(\varepsilon\to0\) by the
just-proved finite-program continuity. The conclusion is

\[
 \left|\sum_{j,a}\alpha_{j,a}
               \mathbb E\partial_{\eta_{j,a}}V^0\right|\le C.
\tag{25}
\]

The signs may now be chosen as
\(\alpha_{j,a}=\operatorname{sgn}T_{V,ja}(0)\), with zero at a zero
coefficient. They are deterministic for this fixed mesh. Equation (25)
then bounds the entire absolute derivative row. A single nonzero
\(\alpha_{j,a}\) yields the one-entry estimate from the single-time
version of (22).

This argument covers off-support formal directions as well. Even if two
unperturbed sources coincide, the prescribed additive errors can be
different at their two query slots; (24) differentiates the exact named
finite expressions. No nonsingularity of any source group is assumed.

#### 7. Explicit mesh-uniform affine source bounds

Assume P(B,S), and retain \(E=\exp(36B^2S)\). All the following bounds hold
for every output sample \(a\), every mesh, and every \(k\le N\).
The affine formal derivatives are deterministic, so the absolute value
of their expectation equals their expected absolute value.

The four rows entering (7)--(8) satisfy

\[
\begin{aligned}
 \sum_{j<k,b}\left|\mathbb E
      \frac{\partial H^{(1)}_{k,a}}{\partial\zeta^{(1)}_{j,b}}\right|
       &\le SE,\\
 \sum_{j<k,b}\left|\mathbb E
      \frac{\partial H^{(2)}_{k,a}}{\partial\zeta^{(2)}_{j,b}}\right|
       &\le24B^2SE,\\
 \sum_{j\le k,b}\left|\mathbb E
      \frac{\partial\delta^{(2)}_{k,a}}{\partial\xi^{(2)}_{j,b}}\right|
       &\le8B^2SE,\\
 \sum_{j\le k,b}\left|\mathbb E
      \frac{\partial\delta^{(3)}_{k,a}}{\partial\xi^{(3)}_{j,b}}\right|
       &\le SE.
\end{aligned}
\tag{26}
\]

Here is the substitution into (25). For bottom transpose forcing,
\(H^{(1)}\) changes by at most the state difference, and \(\kappa=1\).
For middle transpose forcing, \(H^{(2)}\) changes by at most
\(2b\) times the state difference and \(\kappa=3b\), giving
\(6b^2SE=24B^2SE\). For middle forward forcing,
\(\delta^{(2)}=W_3^TC\) changes by at most \(b\) times that difference
and \(\kappa=2b\), giving \(2b^2SE=8B^2SE\). For top forward forcing,
\(\delta^{(3)}=C\) changes by at most the difference and \(\kappa=1\).
None of these four outputs has a direct contribution from the current
source in its indicated group. In particular the two current derivative
blocks in the last two rows are identically zero.

For every fixed \(j<k\) and source sample \(b\), the corresponding
single entry in each row of (26) is bounded by the same expression with
\(S\) replaced by \(h_j\), while keeping \(E=\exp(36B^2S)\). This is a
mesh-scale bound on the entries, as well as a bound on their row sums.

Two useful forward-source row bounds, proved by the same argument, are

\[
 \sum_{j\le k,b}\left|
       \mathbb E\frac{\partial Z^{(2)}_{k,a}}{\partial\xi^{(2)}_{j,b}}
                         \right|
       \le1+16B^2SE,
\qquad
 \sum_{j\le k,b}\left|
       \mathbb E\frac{\partial Z^{(3)}_{k,a}}{\partial\xi^{(3)}_{j,b}}
                         \right|
       \le1+12B^2SE.
\tag{27}
\]

The constants are the output Lipschitz constants \(2b,3b^2\) times
\(\kappa=2b,1\), respectively. The added one is the direct source at
the current output query. Since \(H=1+Z\), (27) also holds for the
corresponding features. These bounds control expected absolute rows
as well, by the deterministic-derivative observation above.

The unperturbed primal bounds imply
\(\|H^{(1)}\|_2\le2B\), \(\|H^{(2)}\|_2\le3B^2\),
\(\|\delta^{(2)}\|_2\le B^2\), \(\|\delta^{(3)}\|_2\le B\).
Cauchy--Schwarz in the learned terms of (7)--(8), followed by
\(\sum_b|c_b|=1\), therefore gives the complete coefficient row bounds

\[
 \sum_{j<k,b}|A^{(2)}_{ka,jb}|\le S(E+4B^2),\qquad
 \sum_{j<k,b}|A^{(3)}_{ka,jb}|\le S(24B^2E+9B^4),
\]
\[
 \sum_{j\le k,b}|D^{(2)}_{ka,jb}|\le S(8B^2E+B^4),\qquad
 \sum_{j\le k,b}|D^{(3)}_{ka,jb}|\le S(E+B^2).
\tag{28}
\]

In addition, for \(j<k\),

\[
 |A^{(2)}_{ka,jb}|\le h_j(E+2B^2),\qquad
 |A^{(3)}_{ka,jb}|\le h_j(24B^2E+\tfrac92B^4),
\]
\[
 |D^{(2)}_{ka,jb}|\le h_j(8B^2E+\tfrac12B^4),\qquad
 |D^{(3)}_{ka,jb}|\le h_j(E+\tfrac12B^2),
 \qquad D^{(2)}_{ka,kb}=D^{(3)}_{ka,kb}=0.
\tag{29}
\]

In the notation used for main's continuation bootstrap, one may take
the following common entry and backward-row constants:

\[
 A_* =24B^2\exp(36B^2S)+\tfrac92B^4,\qquad
 M_* =S\bigl(8B^2\exp(36B^2S)+B^4\bigr).
\]

They give \(\lvert A^{(\ell)}_{ka,jb}\rvert\le A_*h_j\) for
\(\ell=2,3\), and
\(\sum_{j\le k,b}\lvert D^{(\ell)}_{ka,jb}\rvert\le M_*\).
If a forward block means a whole \(2\times2\) matrix with fixed times
\(k,j\), its maximum absolute row sum, and also its Euclidean operator
norm, are at most \(2A_*h_j\). Thus \(A=2A_*\), \(M=M_*\) meet that
block convention. These constants concern the actual affine baseline;
they are independent of the nonlinear-part cap since (4) at \(e=0\)
does not depend on that cap.

These are explicit finite constants for every finite \(B,S\). They do
not depend on the number of steps, the smallest step, or a covariance
condition number. Their only use of labels and input geometry was through
\(\sum|c_a|=1\) and \(\sum_b|c_b\rho_{ab}|\le1\). Thus the same formulas
apply at the antipodal endpoint and to opposite labels.

#### 8. Interpreting a population or continuous-time primal bound

If the supplied primal bound is formulated on the actual population
affine Euler states, suppose its precise content is

\[
 \max_{k,a}\|Z^{(1)}_{k,a}\|_2\le B_0,\quad
 \max_k\{\|W_{2,k}\|_{\rm op},\|W_{3,k}\|_{\rm op},\|C_k\|_2\}
      \le B_0,\qquad B_0\ge1,
\tag{30}
\]

uniformly over the considered meshes on \([0,S]\). These actions can
be realized by the dependency's common-action construction with the
affine coordinate maps and joint two-sample roots: finite unions remain
finite programs; normalized Gaussian operator bounds and finite
adjunction pass to the countable generated probe spaces, then extend
by continuity. Affine maps satisfy its coordinate hypotheses directly.

Section 3 already gives fixed-mesh convergence of every field used in
the learned updates. The dependency's Gaussian net estimate supplies
\(\|W_{2,0}\|_{\rm op},\|W_{3,0}\|_{\rm op}\le10\) with probability
tending to one. At a fixed mesh, exact unrolling and these empirical
norm convergences consequently give

\[
 \max_k\|W_{2,k}^{(n)}\|_{\rm op}
    \le10+2SB_0^3+o_{\mathbb P}(1),\qquad
 \max_k\|W_{3,k}^{(n)}\|_{\rm op}
    \le10+3SB_0^3+o_{\mathbb P}(1).
\tag{31}
\]

For the first inequality, each summand is bounded by
\(h_j|c_b|\frac{\|\delta^{(2)}_{j,b}\|_2}{\sqrt n}\frac{\|H^{(1)}_{j,b}\|_2}{\sqrt n}\), whose
limit is at most \(2h_j|c_b|B_0^3\); sum the finitely many terms.
The second uses \(B_0\cdot3B_0^2\). The first-layer and readout
norms converge to values at most \(B_0\) at these finitely many nodes.
Thus P(B,S) holds with the explicit substitution

\[
 B=11+B_0+4SB_0^3.
\tag{32}
\]

The slack in (32) absorbs all fixed-mesh convergence errors. Equations
(26)--(29) with this value are therefore consequences of the population
primal bound (30) alone. No independent assumption about convergence of
the trained matrix operator norms was inserted.

If only a continuous affine population trajectory is initially known
to obey a bound \(B_0\) on \([0,S]\), (21) supplies the usual bounded-set
Euler comparison on that same action space. More explicitly, on a
larger ball with bound \(b\), the vector field is bounded by
\(10b^3\) and is \(9b^2\)-Lipschitz. Integrating the exact flow over
one step shows a local Euler error at most
\(45b^5h_j^2\). The error recurrence and
\(\sum_j h_j^2\le S|\pi|\), where \(|\pi|=\max_jh_j\), give total
error at most \(45b^5S\exp(9b^2S)|\pi|\). Choose \(b>B_0\) and then
\(|\pi|\) small enough that this is less than the distance to the ball
boundary. The same first-exit induction as after (22) justifies the
comparison. Hence a continuous-trajectory bound supplies a uniform
Euler bound for all sufficiently fine meshes. A bound on arbitrary
coarse Euler steps is not inferred from a flow bound.

### D.3. Complete nonlinear source perturbation proof

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Statement, norms, and the exact program

Fix \(S<\infty\), \(B\ge1\), labels \(y_a\in\{-1,1\}\), and
\(-1\le\rho<1\). Write
\[
 c=(y_1/2,y_2/2)^T,\qquad
 \Gamma=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},
 \qquad P=\Gamma\operatorname{diag}(c),\qquad
 \mathbf1=(1,1)^T.
\]
For rectangular matrices use the maximum absolute row-sum norm
\(|T|=\max_i\sum_j|T_{ij}|\); it is submultiplicative for compatible
sizes. Thus \(|P|\le1\), \(|c^T|=1\), and \(|\mathbf1|=1\).
For a time row of blocks use
\[
 |T_{k\bullet}|_{\mathrm r}=\sum_{j\le k}|T_{kj}|.
 \tag{1}
\]
In particular, this is a sum of block norms, not a maximum over sample
rows after the time sum. For sample pairs \(X\), write
\(\|X\|_p=(\mathbb E|X|_\infty^p)^{1/p}\).

Take any positive mesh \(0=s_0<\cdots<s_N\le S\), with
\(h_j=s_{j+1}-s_j\) for \(j<N\). Set \(h_N=0\) solely as a convention
for zero current-source forcing terms; no terminal step is taken.
Forward coefficient blocks are extended by zero for \(j\ge k\).
The mesh family is assumed to satisfy the affine
primal hypothesis P(B,S), equation (18) of the baseline note: at each
fixed mesh, the actual affine finite-width Euler trajectory obeys
\[
 \max_{k,a}\frac{\|Z^{(1),0}_{k,a}\|_2}{\sqrt n}\le B,\quad
 \max_k\{\|W^0_{2,k}\|_{\rm op},\|W^0_{3,k}\|_{\rm op},
                     \frac{\|C^0_k\|_2}{\sqrt n}\}\le B
 \tag{2}
\]
on events whose probability tends to one. A common population action
version of this hypothesis is also sufficient, by equations (30)--(32)
of that note. A bounded continuous affine trajectory supplies (2) only
for sufficiently fine meshes, as explained there; arbitrary coarse
Euler stability is not asserted.

Assume the actual affine source coefficients satisfy
\[
 |a^{\ell,0}_{kj}|\le A_0h_j\quad(j<k),\qquad
 |b^{\ell,0}_{k\bullet}|_{\mathrm r}\le M_0,
 \qquad \ell=2,3.                                      \tag{3}
\]
This is not an additional unproved operator-to-response implication:
the baseline note proves it under (2). In our particular block norm a
safe substitution from its (26)--(29) is
\[
 A_0=2\left(24B^2e^{36B^2S}+\tfrac92B^4\right),\qquad
 M_0=2S\left(8B^2e^{36B^2S}+B^4\right).                 \tag{4}
\]
The second factor 2 accounts for
\(\sum_j\max_a\sum_b|b_{ka,jb}|\le
2\max_a\sum_{j,b}|b_{ka,jb}|\).
One may instead supply any constants satisfying (3).

Use precisely
\[
 \phi_\epsilon(z)=1+z+\epsilon\arctan z,\qquad
 g(z)=(1+z^2)^{-1},\qquad
 \mathcal D_{\epsilon,R}(z,q)=q+\epsilon g(z)\tau_R(q),
 \tag{5}
\]
where \(0\le\epsilon\le1\), \(R<\infty\),
\(|\tau_R'|\le1\), \(|\tau_R(q)|\le\min(|q|,2R)\), and
\(\tau_R(q)=q\) on \([-R,R]\). Monotonicity of the clip, if imposed,
is harmless but not needed. The forward maps are not clipped.

There are three separate coordinate populations. In their respective
populations the exact source equations are
\[
 Z^1_k=Z^1_0+\sum_{r<k}h_rP\delta^1_r,
 \qquad H^1_k=\phi_\epsilon(Z^1_k),\qquad
 q^1_k=\zeta^1_k+\sum_{v\le k}b^2_{kv}H^1_v,
 \tag{6}
\]
\[
 Z^2_k=\xi^2_k+\sum_{r<k}a^2_{kr}\delta^2_r,
 \qquad H^2_k=\phi_\epsilon(Z^2_k),\qquad
 q^2_k=\zeta^2_k+\sum_{v\le k}b^3_{kv}H^2_v,
 \tag{7}
\]
\[
 Z^3_k=\xi^3_k+\sum_{r<k}a^3_{kr}\delta^3_r,
 \qquad H^3_k=\phi_\epsilon(Z^3_k),\qquad
 C_k=\sum_{r<k}h_rc^TH^3_r.                            \tag{8}
\]
Here \(\delta^1=\mathcal D(Z^1,q^1)\),
\(\delta^2=\mathcal D(Z^2,q^2)\), and
\(\delta^3_a=\mathcal D(Z^3_a,C)\). All such maps act coordinatewise.
The initial pair has covariance \(\Gamma\), and \(C_0=0\).
The four centered Gaussian groups are independent of one another and of
the first-layer root. Inside a group all sample/time correlations are
retained, including singular covariances. Their covariances are exactly
the second moments specified in baseline equation (5).

In entries, the coefficient rules are
\[
 a^\ell_{ka,jb}
 =\mathbb E\partial_{\zeta^{\ell-1}_{j,b}}H^{\ell-1}_{k,a}
       +h_jc_b\mathbb E[H^{\ell-1}_{k,a}H^{\ell-1}_{j,b}],
 \quad j<k,                                           \tag{9}
\]
\[
 b^\ell_{ka,jb}
 =\mathbb E\partial_{\xi^\ell_{j,b}}\delta^\ell_{k,a}
       +\mathbf1_{j<k}h_jc_b
                    \mathbb E[\delta^\ell_{k,a}\delta^\ell_{j,b}],
 \quad j\le k.                                       \tag{10}
\]
Derivatives freeze every deterministic coefficient and covariance
parameter, and differentiate named formal source arguments separately.
In particular, the response term does not acquire an extra column label.

**Conclusion.** There exist \(\epsilon_*>0\) and \(K<\infty\), depending
only on \(B,S,A_0,M_0\), such that for every mesh covered by (2), every
finite cap, and \(0\le\epsilon\le\epsilon_*\), the actual coefficients
obey
\[
 \max_{\ell,k,j<k}
   \frac{|a^\ell_{kj}-a^{\ell,0}_{kj}|}{h_j}\le K\epsilon,
 \qquad
 \max_{\ell,k}|b^\ell_{k\bullet}-b^{\ell,0}_{k\bullet}|_{\mathrm r}
       \le K\epsilon.                                \tag{11}
\]
In particular they obey (3) with fixed enlarged constants. Their actual
coordinate laws satisfy, uniformly in these meshes, caps, and amplitudes,
\[
 \sup_k\left(\|C_k\|_p+\|q^2_k\|_p+\|q^1_k\|_p\right)
       \le K\sqrt p,\qquad p\ge2.                    \tag{12}
\]
The same bound holds for all the displayed forward fields and deltas.
Here “actual” means the canonical source program, rather than an affine
surrogate or a law with prescribed independent coordinates. Source
coefficients do not carry a finite-width index. All constants and the
choice of amplitude are independent of width; an unconditional
subGaussian assertion about every finite-width neuron is not being made.

The proof first bounds primal states and source variances, then proves
moment and derivative estimates on bounded coefficient prefixes. Exact
affine recursions at those same coefficients reduce their perturbation
to a deterministic Volterra estimate. A stage-by-stage induction closes
the prefix bounds without a continuity argument.

#### 2. Primal comparison and the learned-moment errors

This step does not assume any response bound. Put \(b=2B\ge2\) and use
the state-distance norm (19) of the baseline note. On the ball with all
four primal sizes at most \(b\), the following loose bounds hold:
\[
 \|H^1_\epsilon\|_2\le3b,\quad
 \|H^2_\epsilon\|_2\le4b^2,\quad
 \|H^3_\epsilon\|_2\le5b^3,
\]
\[
 \|\delta^3_\epsilon\|_2\le2b,\quad
 \|q^2_\epsilon\|_2\le2b^2,\quad
 \|\delta^2_\epsilon\|_2\le4b^2,\quad
 \|q^1_\epsilon\|_2\le4b^3,\quad
 \|\delta^1_\epsilon\|_2\le8b^3.                       \tag{13}
\]
These are per sample; they also hold in normalized finite-vector norms.
Indeed \(|\phi_\epsilon(z)|\le1+|z|+\pi/2\),
\(|\mathcal D(z,q)|\le2|q|\), and each matrix action has norm at most
\(b\).

At the *same* raw state the forward differences from the affine queries
are bounded by
\[
 \tfrac\pi2\epsilon,\qquad
 \tfrac\pi2(b+1)\epsilon,\qquad
 \tfrac\pi2(b^2+b+1)\epsilon                            \tag{14}
\]
in layers 1, 2, and 3. Backward induction, using
\(|\mathcal D(z,q)-q|\le\epsilon|q|\), bounds the differences in
\(\delta^3,q^2,\delta^2,q^1,\delta^1\) by respectively
\[
 \epsilon b,\quad \epsilon b^2,\quad3\epsilon b^2,
 \quad3\epsilon b^3,\quad7\epsilon b^3.                \tag{15}
\]
For example the middle delta difference is at most
\(\epsilon\|q^2_\epsilon\|_2+
\|q^2_\epsilon-q^2_0\|_2\le3\epsilon b^2\).

For a learned update use
\[
 \|u\otimes v-\widetilde u\otimes\widetilde v\|_{\rm op}
 \le\|u-\widetilde u\|_2\|v\|_2
          +\|\widetilde u\|_2\|v-\widetilde v\|_2.
\]
Insert (13)--(15), \(\sum_a|c_a|=1\), and \(|P|\le1\) into the four
updates. Their total vector-field difference is at most
\(30b^3\epsilon\). The affine vector field is \(9b^2\)-Lipschitz on
this ball, by the explicit estimates (20)--(21) of the baseline note.
Consequently, at a node before any primal exit,
\[
 d_{k+1}\le(1+9b^2h_k)d_k+30b^3\epsilon h_k,
 \qquad d_0=0,
\]
and finite iteration gives
\[
 d_k\le30b^3S e^{9b^2S}\epsilon.                       \tag{16}
\]
Choose the amplitude so this is at most \(B/2\). Induction proves the
same estimate at the next node from a state already inside the ball, so
the perturbed state stays a positive distance from its boundary. No
Lipschitz constant of the nonlinear vector field, and thus no cap, enters
this comparison.

Combining (14)--(16) with the affine query Lipschitz estimates bounds
every forward/backward query difference by \(K_{B,S}\epsilon\) in
\(L^2\), and bounds their \(L^2\) norms by \(K_{B,S}\). At fixed width this
holds on the affine events (2). At a fixed mesh and cap it passes to the
joint population construction for the two programs sharing their initial
matrices and roots. The conditioning dependency applies: there are
finitely many queries, independent Gaussian initial matrices, iid joint
roots with finite second moments, and the coordinate maps (5) are \(C^1\)
and globally Lipschitz with bounded derivatives for each fixed cap.
Learned contractions are then transferred by the finite induction in
baseline Section 3. In particular this is a coupling of actual programs;
it does not compare square roots of covariance matrices of growing size.

The covariance identities now give a bound \(\sigma^2=K_{B,S}^2\) for
every scalar source variance. For any two of the queries whose products
occur in (9)--(10), Cauchy--Schwarz in that joint coupling gives
\[
 |\mathbb E[U_\epsilon V_\epsilon]-\mathbb E[U_0V_0]|
 \le\|U_\epsilon-U_0\|_2\|V_\epsilon\|_2
       +\|U_0\|_2\|V_\epsilon-V_0\|_2
 \le K_{B,S}\epsilon.                                \tag{17}
\]
Thus a learned forward-block error is at most \(K\epsilon h_j\),
and a full learned backward-row error is at most \(KS\epsilon\).
The factor \(c_b\) is retained in taking these bounds; its absolute
column sum is one.

#### 3. Coordinate moments under a coefficient bound

Fix finite constants \(A,M\ge1\). For now assume the coefficients needed
to construct a specified prefix satisfy
\[
 |a^\ell_{kr}|\le Ah_r,
 \qquad |b^\ell_{k\bullet}|_{\mathrm r}\le M.           \tag{18}
\]
All estimates in this section and the next depend only on
\(A,M,\sigma,S\). A symbol \(K\) may be enlarged using only these
quantities. No estimate uses the number of mesh points or the cap.

A centered Gaussian with variance at most \(\sigma^2\) has \(L^p\)
norm at most \(2\sigma\sqrt p\), for \(p\ge2\). This follows, for example,
by integrating the bound \(\mathbb P(|X|>t)\le2e^{-t^2/(2\sigma^2)}\).
The norm of a two-coordinate maximum is at most the sum of the two
coordinate norms. Hence all source-pair norms, and the initial root-pair
norm, are bounded by \(K\sqrt p\), with arbitrary correlations allowed.

For the middle layer, put
\(U_k=\max_{v\le k}\|H^2_v\|_p\); this is a maximum of deterministic
norms, not a random maximum over source times. Equations (7) and (18) give
\[
 \|q^2_r\|_p\le K\sqrt p+MU_r,
 \qquad
 \|H^2_k\|_p\le K\sqrt p+2A\sum_{r<k}h_r\|q^2_r\|_p.
\]
Taking the maximum of the latter inequalities and enlarging nonnegative
sums to the final index gives
\[
 U_k\le K(1+2AS)\sqrt p+2AM\sum_{r<k}h_rU_r.
 \tag{19}
\]
Finite iteration bounds this by \(K\sqrt p\,e^{2AMS}\), and then bounds
\(q^2,H^2,Z^2,\delta^2\) by \(K\sqrt p\).

At the bottom, (6) gives
\[
 \|q^1_r\|_p\le K\sqrt p+M\max_{v\le r}\|H^1_v\|_p,
\]
\[
 \|H^1_k\|_p\le K\sqrt p+2\sum_{r<k}h_r\|q^1_r\|_p.
 \tag{20}
\]
The same finite iteration, with coefficient \(2M\), bounds
\(H^1,Z^1,q^1,\delta^1\).

At the top, write \(V_k=\max_{v\le k}\|C_v\|_p\). From (8),
\[
 \|Z^3_k\|_p\le K\sqrt p+2A\sum_{r<k}h_r\|C_r\|_p,
\]
\[
 \|C_k\|_p\le KS\sqrt p
          +2A\sum_{r<k}h_r\sum_{v<r}h_v\|C_v\|_p
 \le KS\sqrt p+2AS\sum_{v<k}h_vV_v.                  \tag{21}
\]
Taking the deterministic maximum and iterating gives the same conclusion
for \(C,Z^3,H^3,\delta^3\). These proofs also apply to incomplete prefixes
whenever the rows actually used have been bounded: \(H^1_k\) uses only
past \(b^2\); \(H^2_k\) uses current \(a^2\) and past \(b^3\); \(C_k\)
uses only earlier top forward instructions; \(q^2_k\) additionally uses
current \(b^3\); and \(q^1_k\) additionally uses current \(b^2\).

These moment bounds are subGaussian bounds for the possibly noncentered
fields. Explicitly, if \(\|X\|_p\le K\sqrt p\), then expansion of the
exponential and \(m!\ge(m/\mathrm e)^m\) give
\[
 \mathbb E\exp\{X^2/(4\mathrm e K^2)\}
 \le1+\sum_{m\ge1}
       \frac{K^{2m}(2m)^m}{(4\mathrm eK^2)^m m!}\le2.
 \tag{22}
\]

#### 4. Formal derivatives and the repaired envelope

For each layer set
\[
 G^\ell_r=\operatorname{diag}(\phi_\epsilon'(Z^\ell_{r,a})),
 \quad V^\ell_r=\operatorname{diag}
       (1+\epsilon g(Z^\ell_{r,a})\tau_R'(m^\ell_{r,a})),
\]
\[
 L^\ell_r=\operatorname{diag}
       (\epsilon g'(Z^\ell_{r,a})\tau_R(m^\ell_{r,a})),
 \quad m^1=q^1,\quad m^2=q^2,\quad m^3_a=C.
\]
Using \(|g'|\le1\),
\[
 |G-I|\le\epsilon,\quad |V-I|\le\epsilon,
 \quad |G|,|V|\le2,\quad |L^\ell_r|\le\epsilon Q_r,
 \tag{23}
\]
where \(Q_r=|q^1_r|_\infty\), \(|q^2_r|_\infty\), or \(|C_r|\) in
the relevant population. In particular all derivatives below are formal
derivatives of the specified source equations, not derivatives along a
singular Gaussian support.

For a bottom transpose source at time \(j\), let
\(J_{k,j}=\partial_{\zeta^1_j}Z^1_k\), a \(2\times2\) block. Its exact
recursion is
\[
 J_{k,j}=\sum_{r<k}h_rP\left[
 L^1_rJ_{r,j}+V^1_r\left(I\mathbf1_{r=j}
             +\sum_{v\le r}b^2_{rv}G^1_vJ_{v,j}\right)\right].
 \tag{24}
\]
It vanishes for \(k\le j\). For \(k>j\), (18) and (23) give
\[
 |J_{k,j}|\le2h_j+
       \sum_{r<k}h_r(\epsilon Q_r+4M)
                      \max_{v\le r}|J_{v,j}|.         \tag{25}
\]

In the middle, for any source perturbation the exact equations are
\[
 J_k=I^\xi_k+\sum_{r<k}a^2_{kr}
       \left[L^2_rJ_r+V^2_r\left(I^\zeta_r
                +\sum_{v\le r}b^3_{rv}G^2_vJ_v\right)\right].
 \tag{26}
\]
Here \(J=\partial Z^2\), and \(I^\xi,I^\zeta\) denote the appropriate
direct source derivative. For one transpose source \(j\), the forcing
has norm at most \(2Ah_j\), and \(J_k=0\) for \(k\le j\). Its analogue
of (25) has coefficient \(A(\epsilon Q_r+4M)\).

For the full row of forward-source derivatives put
\(u_k=\sum_{j\le k}|\partial_{\xi^2_j}Z^2_k|\).
Summing (26) in this norm instead gives
\[
 u_k\le1+A\sum_{r<k}h_r(\epsilon Q_r+4M)
                                  \max_{v\le r}u_v.   \tag{27}
\]
All time rows may be padded with zeros to a common length in taking
these sums, so no factor equal to their length appears.

At the top write \(J_{k,j}=\partial_{\xi^3_j}Z^3_k\) and
\(T_{k,j}=\partial_{\xi^3_j}C_k\), the latter a \(1\times2\) block.
The exact equations, including both label signs, are
\[
 J_{k,j}=I\mathbf1_{k=j}
       +\sum_{r<k}a^3_{kr}
            (V^3_r\mathbf1 T_{r,j}+L^3_rJ_{r,j}),
 \qquad
 T_{k,j}=\sum_{r<k}h_rc^TG^3_rJ_{r,j}.                \tag{28}
\]
For their row sums \(u_k,t_k\), respectively,
\[
 t_k\le2\sum_{r<k}h_ru_r,\qquad
 u_k\le1+2A\sum_{r<k}h_rt_r
                    +A\epsilon\sum_{r<k}h_rQ_ru_r
 \le1+\sum_{r<k}h_r(4AS+A\epsilon Q_r)
                                      \max_{v\le r}u_v. \tag{29}
\]

To justify the exponential estimate used for (25), (27), and (29),
if \(x_k\le f+\sum_{r<k}h_r\lambda_r\max_{v\le r}x_v\), with
nonnegative \(\lambda_r\), its increasing majorant satisfies
\(w_0=f\), \(w_{k+1}=(1+h_k\lambda_k)w_k\).
Induction bounds all \(x_k\) by \(w_k\), and
\(w_k\le f\exp(\sum_{r<k}h_r\lambda_r)\).
Consequently all the preactivation derivatives just considered obey
\[
 |J_{k,j}|\le Kh_j\mathcal E_k
 \quad\hbox{for an individual transpose source},\qquad
 u_k+t_k\le K\mathcal E_k
 \quad\hbox{for a forward-source row},
 \tag{30}
\]
where, in the appropriate population, one can use
\[
 \mathcal E_k=
 \exp\left\{K s_k+K\epsilon\sum_{r<k}h_rQ_r\right\}.
 \tag{31}
\]
The constant \(K\) can for instance dominate
\(2A+4AM+4AS+4M+2S+2\). It is fixed before any mesh is chosen.

There is a correction to the envelope proposed in the route note. The
backward outputs themselves contain \(L_kJ_k\). For the middle and top
forward-source derivative rows, (23), (26), and (28) give only
\[
 \sum_j|\partial_{\xi^2_j}\delta^2_k|
       \le K(1+\epsilon|q^2_k|_\infty)\mathcal E_k,
 \qquad
 \sum_j|\partial_{\xi^3_j}\delta^3_k|
       \le K(1+\epsilon|C_k|)\mathcal E_k.             \tag{32}
\]
The current-coordinate factor is not contained in the past-time
exponential (31). Dropping it would be unjustified.

It causes no integrability loss. To see this without a source-time
maximum, let \(t=s_k\le S\), and suppose \(S>0\). Convexity gives, for
every \(\lambda\ge0\),
\[
 \exp\left(\lambda\sum_{r<k}h_rQ_r\right)
 \le1-t/S+\sum_{r<k}(h_r/S)e^{\lambda S Q_r}.          \tag{33}
\]
Equation (22) and
\(uQ\le Q^2/L^2+u^2L^2/4\) show
\(\mathbb E e^{uQ_r}\le2e^{u^2L^2/4}\) for a uniform \(L\).
Thus for every fixed finite \(p\ge1\),
\[
 \sup_k\|\mathcal E_k\|_p<\infty,
 \qquad
 \sup_k\|(1+Q_k)\mathcal E_k\|_p<\infty.             \tag{34}
\]
The second assertion uses Hölder with \(2p,2p\), and the moments in
Section 3. Its constants can depend on \(p\), but not on cap or mesh.

#### 5. Derivative comparison at the same coefficient arrays

In this section the deterministic arrays \(a,b\) stay fixed. A superscript
\(\mathrm{aff}\) means the derivative system with \(G=V=I,L=0\), at
these arrays. It need not be the derivative system at the actual affine
baseline arrays. It is deterministic and does not depend on which
Gaussian realization is used.

We prove
\[
 \left|\mathbb E\partial_{\zeta^1_j}H^1_k
                  -\partial_{\zeta^1_j}H^{1,\mathrm{aff}}_k\right|
 +\left|\mathbb E\partial_{\zeta^2_j}H^2_k
                  -\partial_{\zeta^2_j}H^{2,\mathrm{aff}}_k\right|
       \le K\epsilon h_j,                            \tag{35}
\]
\[
 \sum_{j\le k}
 \left|\mathbb E\partial_{\xi^\ell_j}\delta^\ell_k
                   -\partial_{\xi^\ell_j}
                                      \delta^{\ell,\mathrm{aff}}_k\right|
       \le K\epsilon,\qquad \ell=2,3.                \tag{36}
\]
The estimates also hold with expectation outside the sum of block norms
of the random derivative differences.

Here are the error equations and their bounds. In (26), subtracting the
affine equation leaves its affine feedback on \(J-J^{\mathrm{aff}}\)
plus the three terms
\[
 \sum_{r<k}a^2_{kr}\left[
 (V_r-I)I^\zeta_r+L_rJ_r
 +(V_r-I)\sum_{v\le r}b^3_{rv}G_vJ_v
                 +\sum_{v\le r}b^3_{rv}(G_v-I)J_v\right].
 \tag{37}
\]
In (24) the identical bracket is multiplied by \(h_rP\), and its affine
feedback is \(\sum_{r<k}h_rP\sum_{v\le r}b^2_{rv}
(J_{v,j}-J^{\mathrm{aff}}_{v,j})\).
By (23) and (30), the bracket's accumulated forcing is bounded by
\[
 K\epsilon f\left(1+\sum_{r<k}h_r(1+Q_r)\mathcal E_r\right),
 \tag{38}
\]
where \(f=h_j\) for a single transpose source and \(f=1\) for a full
forward-source row. In the single-source case the first term of (37)
appears only at \(r=j\), with its factor \(h_j\); all other derivatives
vanish through time \(j\) and thereafter carry the factor \(h_j\) in
(30). This verifies the source-step factor even for unequal meshes.
All terms with \(G_v-I\) use the increasing envelope
\(\mathcal E_v\le\mathcal E_r\) when \(v\le r\).

The affine feedback is bounded by \(K\sum_{r<k}h_r\max_{v\le r}d_v\),
where \(d_v\) is the norm of the derivative difference under
consideration. The forcing (38) is increasing in \(k\). Applying the
finite majorant argument above to it, or expanding the same finite
products, gives
\[
 d_k\le K\epsilon f e^{KS}
           \left(1+\sum_{r<k}h_r(1+Q_r)\mathcal E_r\right).
 \tag{39}
\]
Its expectation is \(K\epsilon f\), by (34) and the sum of step sizes.
Multiplication by \(G_k\) to obtain a feature derivative adds at most
\(\epsilon|J_k|\), so this proves (35).

For completeness the top subtraction has the equations
\[
 \Delta J_k=\sum_{r<k}a^3_{kr}
       [\mathbf1\Delta T_r+(V_r-I)\mathbf1 T_r+L_rJ_r],
\]
\[
 \Delta T_k=\sum_{r<k}h_rc^T
                     [\Delta J_r+(G_r-I)J_r].        \tag{40}
\]
Their row-norm affine feedback reduces, by substituting the second
equation in the first and using \(\sum h_r\le S\), to at most
\(AS\sum_{r<k}h_r\max_{v\le r}|\Delta J_v|_{\rm r}\).
The remaining terms are bounded by (38) with \(f=1\). Thus (39), with
enlarged constants, bounds both top derivative rows as well.

Finally, at the middle backward output, the derivative difference is
\[
 L_kJ_k+(V_k-I)\sum_{v\le k}b^3_{kv}G_vJ_v
 +\sum_{v\le k}b^3_{kv}(G_v-I)J_v
 +\sum_{v\le k}b^3_{kv}(J_v-J^{\mathrm{aff}}_v).
 \tag{41}
\]
There is no direct transpose-source forcing when taking a forward-source
row. At the top it is
\[
 L_kJ_k+(V_k-I)\mathbf1 T_k+\mathbf1\Delta T_k.         \tag{42}
\]
The current terms \(L_kJ_k\) have expected row norm at most
\(K\epsilon\mathbb E[Q_k\mathcal E_k]\), which is bounded by
\(K\epsilon\) using (34). The other terms are bounded by (30), (39),
and the row bound \(M\). This proves (36), including its current-source
entries. No derivative of a cap, covariance, or coefficient is omitted;
cap derivatives enter only through \(V\) as prescribed in (23).
#### 6. Exact deterministic coefficient stability

We now compare coefficient arrays, rather than source realizations. The
following four deterministic recursions are the complete affine
derivative systems at arbitrary fixed arrays \(a,b\). They also fix all
block orientations and sample labels.

Let \(F_{k,j}\) be the bottom \(\zeta^1_j\)-to-\(H^1_k\) derivative,
\(V_{k,j}\) the middle \(\zeta^2_j\)-to-\(H^2_k\) derivative, and
\(U_{k,j}\) the middle \(\xi^2_j\)-to-\(H^2_k\) derivative. In this
section \(V\) denotes this derivative array, not the local diagonal gate
matrix of Section 4. They satisfy
\[
 F_{k,j}=h_jP\mathbf1_{j<k}
       +\sum_{r<k}h_rP\sum_{v\le r}b^2_{rv}F_{v,j},
 \tag{43}
\]
\[
 V_{k,j}=a^2_{kj}\mathbf1_{j<k}
       +\sum_{r<k}a^2_{kr}\sum_{v\le r}b^3_{rv}V_{v,j},
 \tag{44}
\]
\[
 U_{k,j}=I\mathbf1_{k=j}
       +\sum_{r<k}a^2_{kr}\sum_{v\le r}b^3_{rv}U_{v,j}.
 \tag{45}
\]
All arrays are zero beyond their causal support. The top
\(\xi^3_j\)-to-\(C_k\) derivative \(T_{k,j}\in\mathbb R^{1\times2}\)
satisfies
\[
 T_{k,j}=h_jc^T\mathbf1_{j<k}
       +\sum_{r<k}h_rc^T\sum_{v<r}a^3_{rv}\mathbf1 T_{v,j}.
 \tag{46}
\]
Indeed its top preactivation derivative is
\(I\mathbf1_{k=j}+\sum_{v<k}a^3_{kv}\mathbf1 T_{v,j}\), which gives
(46) on inserting it into the readout sum. The affine top delta
derivative is \(\mathbf1 T_{k,j}\). The affine middle delta derivative is
\[
 W_{k,j}=\sum_{v\le k}b^3_{kv}U_{v,j}.                \tag{47}
\]
In particular, \(T_{k,\bullet}\) depends on \(a^3_{r,\bullet}\) only
for \(r<k\), whereas \(U_{k,\bullet}\) depends on current \(a^2_k\) and
past \(b^3_r\). The product (47) uses current \(b^3_k\); it uses no
current \(b^2_k\).

For these deterministic systems, (18) and finite iteration give
\[
 |F_{k,j}|\le e^{MS}h_j,\qquad
 |V_{k,j}|\le Ae^{AMS}h_j\quad(j<k),
 \tag{48}
\]
\[
 |U_{k\bullet}|_{\rm r}\le e^{AMS},\qquad
 |T_{k\bullet}|_{\rm r}\le S e^{AS^2}.                \tag{49}
\]
For example the row inequality for \(U\) is
\(u_k\le1+AM\sum_{r<k}h_r\max_{v\le r}u_v\).
For \(T\), (46) yields
\(t_k\le S+A\sum_{r<k}h_r\sum_{v<r}h_vt_v
\le S+AS\sum_{v<k}h_vt_v\).
The other two estimates follow in the same explicit way from their
forcing sizes \(h_j\) and \(Ah_j\), respectively, and feedback
coefficients \(M\) and \(AM\). Denote the constants on the right of
(48)--(49) by \(K_F,K_V,K_U,K_T\), omitting their factors \(h_j\).

Use a superscript 0 on \(F,V,U,T,W\) to mean the same recursions at the
actual baseline arrays. Combining (17), (35)--(36), and (9)--(10) gives
the exact difference identities
\[
 a^2_{kj}-a^{2,0}_{kj}=F_{k,j}-F^0_{k,j}+\eta^2_{kj},
 \qquad
 a^3_{kj}-a^{3,0}_{kj}=V_{k,j}-V^0_{k,j}+\eta^3_{kj},
 \tag{50}
\]
\[
 b^3_{kj}-b^{3,0}_{kj}=\mathbf1(T_{k,j}-T^0_{k,j})+\nu^3_{kj},
 \qquad
 b^2_{kj}-b^{2,0}_{kj}=W_{k,j}-W^0_{k,j}+\nu^2_{kj},
 \tag{51}
\]
where
\[
 |\eta^\ell_{kj}|\le K\epsilon h_j,
 \qquad |\nu^\ell_{k\bullet}|_{\rm r}\le K\epsilon.
 \tag{52}
\]
The remainders have been bounded in Sections 2 and 5; (52) is not a new
stability assumption. In particular, they retain all nonlinear current
returns and all learned-moment differences, with their column labels.

Define nonnegative deterministic discrepancies
\[
 \alpha^\ell_k=\max_{j<k}
                  \frac{|a^\ell_{kj}-a^{\ell,0}_{kj}|}{h_j},
 \qquad
 \beta^\ell_k=|b^\ell_{k\bullet}-b^{\ell,0}_{k\bullet}|_{\rm r},
\]
\[
 E_k=\beta^2_k+\beta^3_k,\qquad
 I_k=\sum_{r<k}h_rE_r.                                \tag{53}
\]
An empty maximum is zero. We next prove bounds for each current
discrepancy in the actual construction order. The increasing quantity
\(I_k\) uses only completed, strictly earlier backward rows.

**First forward row.** Subtract (43) at the two arrays, expanding
\(b^2F-b^{2,0}F^0=(b^2-b^{2,0})F+b^{2,0}(F-F^0)\). For each \(j<k\),
\[
 \frac{|F_{k,j}-F^0_{k,j}|}{h_j}
 \le K_F\sum_{r<k}h_r\beta^2_r
       +M\sum_{r<k}h_r
             \max_{v\le r}\frac{|F_{v,j}-F^0_{v,j}|}{h_j}.
 \tag{54}
\]
Terms with \(v\le j\) vanish. The first term is increasing with \(k\);
finite iteration therefore bounds (54) by \(K_Fe^{MS}I_k\).
The first identity (50) now gives
\[
 \alpha^2_k\le K(\epsilon+I_k).                       \tag{55}
\]
Only \(b^2_r\) for \(r<k\) was used, including in the nonlinear
derivative estimate producing \(\eta^2_k\).

**Second forward row.** Expanding the feedback in (44) as
\[
 a^2b^3V-a^{2,0}b^{3,0}V^0
 =(a^2-a^{2,0})b^3V
       +a^{2,0}(b^3-b^{3,0})V
       +a^{2,0}b^{3,0}(V-V^0)
\]
and using (48) gives, with \(d^j_k=|V_{k,j}-V^0_{k,j}|/h_j\),
\[
 d^j_k\le(1+MSK_V)\alpha^2_k
       +AK_V\sum_{r<k}h_r\beta^3_r
       +AM\sum_{r<k}h_r\max_{v\le r}d^j_v.            \tag{56}
\]
For example the first feedback term uses

\(\sum_{r<k}|a^2_{kr}-a^{2,0}_{kr}|
  \sum_{v\le r}|b^3_{rv}|\,|V_{v,j}|/h_j
\le MSK_V\alpha^2_k\).

Thus the current forward-row discrepancy multiplies a finite time
integral; it is not an extra unknown on the left of (55).
Insert (55) at each already available time. Since
\(\epsilon+I_v\le\epsilon+I_k\) for \(v\le k\), the forcing in (56)
is bounded by \(K(\epsilon+I_k)\). Finite iteration gives
\(d^j_k\le K(\epsilon+I_k)\), and the second identity (50) proves
\[
 \alpha^3_k\le K(\epsilon+I_k).                       \tag{57}
\]
This uses current \(a^2_k\) and only past \(b^3_r\).

**Top backward row.** Let
\(t_k=|T_{k\bullet}-T^0_{k\bullet}|_{\rm r}\).
The forcing \(h_jc^T\) cancels exactly in (46). Expanding the remaining
products in the order
\((a^3-a^{3,0})\mathbf1 T+a^{3,0}\mathbf1(T-T^0)\),
and summing the source blocks, gives
\[
 t_k\le SK_T\sum_{r<k}h_r\alpha^3_r
                  +AS\sum_{v<k}h_vt_v.              \tag{58}
\]
The factor \(S\) in the feedback follows by exchanging the finite
nonnegative sums:
\(\sum_{r<k}h_r\sum_{v<r}h_vt_v
=\sum_{v<k}h_vt_v\sum_{v<r<k}h_r\le S\sum_{v<k}h_vt_v\).
Finite iteration of (58), followed by (57), yields
\[
 t_k\le K\sum_{r<k}h_r\alpha^3_r
      \le K(\epsilon+I_k),
\]
because \(\sum_{r<k}h_r I_r\le S I_k\).
The first identity (51) therefore gives
\[
 \beta^3_k\le K(\epsilon+I_k).                        \tag{59}
\]
There is no current \(\alpha^3_k\) in (58). The nonlinear remainder at
this stage uses the current \(a^3_k\) bound, already established at the
previous stage, but uses no \(b^3_k\) bound.

**Middle backward row.** Let
\(u_k=|U_{k\bullet}-U^0_{k\bullet}|_{\rm r}\).
Subtracting (45) and making the same three-product expansion as in (56)
gives
\[
 u_k\le MSK_U\alpha^2_k
       +AK_U\sum_{r<k}h_r\beta^3_r
       +AM\sum_{r<k}h_r\max_{v\le r}u_v.              \tag{60}
\]
There is no direct-source difference. Equations (55) and (53) bound its
forcing by \(K(\epsilon+I_k)\), so finite iteration gives
\[
 u_k\le K(\epsilon+I_k).                              \tag{61}
\]
Now use the exact product (47), in the form
\[
 W_k-W^0_k=(b^3_k-b^{3,0}_k)U+b^{3,0}_k(U-U^0).
\]
Submultiplicativity in the block-row norm gives
\[
 |W_{k\bullet}-W^0_{k\bullet}|_{\rm r}
 \le K_U\beta^3_k+
                   \sum_{v\le k}|b^{3,0}_{kv}|u_v
 \le K_U\beta^3_k+M_0\max_{v\le k}u_v.
 \tag{62}
\]
Combining (59)--(62) and the second identity (51) proves
\[
 \beta^2_k\le K(\epsilon+I_k).                        \tag{63}
\]
The current \(b^3_k\) is allowed here because it has just been bounded
by (59). The current \(U_k\) in (62) depends only on current \(a^2_k\)
and past \(b^3_r\), so it creates no new unknown backward row. In fact
the affine baseline satisfies \(b^{3,0}_{kk}=0\); the estimate remains
valid even without exploiting that zero.

Taking one constant large enough for all these explicitly derived
inequalities gives, at each completed time,
\[
 \alpha^2_k,\alpha^3_k,\beta^2_k,\beta^3_k
      \le K(\epsilon+I_k),\qquad
 E_k\le K\epsilon+K\sum_{r<k}h_rE_r.                 \tag{64}
\]
This is the desired deterministic causal stability bound. It was derived
from the actual coefficient identities, not from continuity of a finite
system or an assumed Lipschitz constant in its growing dimension.

#### 7. Closing the coefficient bounds, including current returns

Fix \(A=A_0+1\), \(M=M_0+1\), and the variance bound from Section 2.
Choose \(K\ge1\) large enough for every stage inequality in (64) using
these fixed constants. For \(S>0\), define
\[
 \epsilon_*=
 \min\left\{1,
       \frac{B}{60b^3S e^{9b^2S}},
       \frac{1}{2K e^{KS}}\right\},\qquad b=2B.
 \tag{65}
\]
The middle term closes the primal comparison (16). For \(S=0\), take
any \(\epsilon_*\le1\): there are no updates and all backward inputs
and response coefficients are zero.

Here is a literal induction establishing that the bounded prefixes used
above exist through every stage. Suppose all four coefficient rows have
been constructed and bounded at times \(r<k\), and satisfy
\[
 E_r\le K\epsilon\prod_{v<r}(1+Kh_v).
 \tag{66}
\]
The telescoping product identity implies
\[
 \epsilon+I_k
 \le\epsilon\left[1+\sum_{r<k}Kh_r
                         \prod_{v<r}(1+Kh_v)\right]
 =\epsilon\prod_{r<k}(1+Kh_r)
 \le\epsilon e^{KS}.                                \tag{67}
\]
At time \(k\), perform the following four stages in order.

1. Construct \(a^2_k\). Its response uses \(Z^1_k,H^1_k\) and bottom
   derivative paths whose last backward input is at time \(k-1\).
   Equations (20), (24)--(25), and (35) require only past \(b^2\), so
   (55) applies before any bound on this new forward row is assumed.
   Equations (65), (67) give \(\alpha^2_k\le1/2\), hence
   \(|a^2_{kj}|\le(A_0+1/2)h_j<Ah_j\).
2. Construct \(a^3_k\). The just-bounded \(a^2_k\) constructs \(Z^2_k,H^2_k\).
   Their transpose-source derivative paths use only \(q^2_r\), \(r<k\).
   Thus (19), (26), and (35) give (57) using current \(a^2_k\) and past
   \(b^3\). It yields \(\alpha^3_k\le1/2\), hence the required \(a^3\)
   bound. In particular no bound on current \(q^2_k\) has been used here.
3. Construct \(b^3_k\). The readout \(C_k\) and the current \(Z^3_k\) are
   available. The top moment and derivative estimates (21), (28)--(34),
   and (40), (42) use \(a^3\) through time \(k\), now bounded, and no
   backward row. Equation (59) gives \(\beta^3_k\le1/2\), so
   \(|b^3_{k\bullet}|_{\rm r}<M\). This row now defines \(q^2_k\), whose
   subGaussian bound follows from (19) with the current \(H^2_k\).
4. Construct \(b^2_k\). All inputs to its middle derivative equation,
   including current \(q^2_k\) and \(b^3_k\), are now bounded as required.
   Equations (41) and (60)--(63) give \(\beta^2_k\le1/2\), hence its
   row bound. Only now is the current \(q^1_k\) defined and bounded using
   (20).

All learned moments required at a stage are moments of fields already
constructed at that stage; (17) has bounded them independently of this
induction. The bound on \(E_k\) in (64), together with (67), proves
(66) for the newly completed time. At \(k=0\) all forward rows are empty.
Since \(C_0=0\), the top delta and its source derivatives vanish,
\(b^3_{0\bullet}=0\), and the middle backward inputs and their responses
also vanish. Thus \(b^2_{0\bullet}=0\), giving the induction base.

For clarity, the exact current-source blocks computed by this schedule
are, in entries, with \(p^\ell_{k,a}=(L^\ell_k)_{aa}\),
\(v^\ell_{k,a}=(V^\ell_k)_{aa}\), and
\(d^\ell_{k,a}=(G^\ell_k)_{aa}\),
\[
 b^3_{ka,kb}=\mathbf1_{a=b}\mathbb E p^3_{k,a},
 \tag{68}
\]
\[
 b^2_{ka,kb}=\mathbf1_{a=b}\mathbb E p^2_{k,a}
               +b^3_{ka,kb}\mathbb E[v^2_{k,a}d^2_{k,b}].
 \tag{69}
\]
To check these directly, \(C_k\) does not depend on current \(\xi^3_k\)
and \(\partial_{\xi^3_k}Z^3_k=I\), proving (68). Similarly
\(\partial_{\xi^2_k}Z^2_k=I\) and
\(\partial_{\xi^2_k}q^2_k=b^3_{kk}G^2_k\), proving (69).
The factor order and the column sample \(b\) in \(d^2_{k,b}\) are fixed
by this matrix product. Thus off-diagonal current entries are zero for
this schedule, while earlier blocks can be full. From (23) and Section 3,
\(|b^3_{kk}|\le K\epsilon\) and
\(|b^2_{kk}|\le K\epsilon+4|b^3_{kk}|\le K\epsilon\).
These are included in (36), (51), and the row estimate; they were never
dropped or solved by an implicit inverse.

Equations (66)--(67) prove (11), after absorbing \(e^{KS}\) in its
constant. The coefficient bounds now hold on the entire program, so
Section 3 proves (12) on the entire program. Equations (30), (32), and
(34) also prove uniform expected absolute response bounds:
\[
 \mathbb E|\partial_{\zeta^{\ell-1}_j}H^{\ell-1}_k|
       \le Kh_j\quad(j<k),\qquad
 \mathbb E\sum_{j\le k}|\partial_{\xi^\ell_j}\delta^\ell_k|
       \le K,\quad \ell=2,3.                        \tag{70}
\]
No random supremum over Gaussian source times occurs in these estimates.

### D.4. Symmetry, radial coercivity, affine endpoint and nondegeneracy

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Normalization and scalar reduction

Write
\[
G_{ab}=x_a^Tx_b/d,\qquad
G=\begin{pmatrix}1&\rho\\ \rho&1\end{pmatrix},\quad -1\le\rho<1,
\qquad y_1=\sigma,\quad y_2=\sigma\tau,
\]
where \(\sigma\in\{-1,1\}\) and \(\tau=y_1y_2\in\{-1,1\}\).
Let \(\pi\) interchange the samples. Same labels mean \(\tau=1\);
opposite labels mean \(\tau=-1\).

Use three separate population spaces
\(\mathcal H_\ell=L^2(\Omega_\ell)\), a first weight field
\(w\in L^2(\Omega_1;\mathbb R^d)\), bounded actions
\(A:\mathcal H_1\to\mathcal H_2\),
\(B:\mathcal H_2\to\mathcal H_3\), and readout \(C\in\mathcal H_3\).
Set
\[
z_a^{(1)}=w\cdot x_a,\quad h_a^{(1)}=\phi(z_a^{(1)}),\quad
z_a^{(2)}=Ah_a^{(1)},\quad h_a^{(2)}=\phi(z_a^{(2)}),
\]
\[
z_a^{(3)}=Bh_a^{(2)},\quad h_a^{(3)}=\phi(z_a^{(3)}),\qquad
f_a=\langle C,h_a^{(3)}\rangle_3.
\]
The projected feature and scalar objective are
\[
H=\frac{y_1h_1^{(3)}+y_2h_2^{(3)}}2,\qquad
g=\langle C,H\rangle_3=\frac{y_1f_1+y_2f_2}2.                 \tag{1}
\]
We prove below that the constructed symmetric population path obeys
\(f_a=y_ag\). On that path the stated model's normalization gives
\[
L=\frac{(f_1-y_1)^2+(f_2-y_2)^2}{2}=(1-g)^2,\qquad
\dot\Theta=-\sum_a(f_a-y_a)\nabla f_a=2(1-g)\nabla g.        \tag{2}
\]
Our feature-time convention is therefore
\[
\Theta'=\nabla g,\qquad ds/dt=2(1-g).                       \tag{3}
\]
The projected kernel in this convention is \(y^TKy/4\).

#### 2. Symmetry before uncut uniqueness

### Finite clipped Euler

Because the inputs have identical norm, the orthogonal involution
\[
u=\frac{x_1-x_2}{\|x_1-x_2\|},\qquad Q=I-2uu^T
\]
satisfies
\[
Qx_1=x_2,\quad Qx_2=x_1.                                  \tag{4}
\]
Indeed, \(\|x_1-x_2\|^2=2d(1-\rho)\) and
\((x_1-x_2)^Tx_1=d(1-\rho)\). The formula includes \(\rho=-1\).

At finite width define
\[
\mathcal T(W^{(1)},A,B,C)=(W^{(1)}Q,A,B,\tau C).
\]
With the dataset and labels held fixed,
\[
h_a^{(\ell)}(\mathcal T\Theta)=h_{\pi a}^{(\ell)}(\Theta),
\quad f_a(\mathcal T\Theta)=\tau f_{\pi a}(\Theta),
\]
\[
r_a(\mathcal T\Theta)=\tau r_{\pi a}(\Theta),\qquad
\delta_a^{(\ell)}(\mathcal T\Theta)
   =\tau\delta_{\pi a}^{(\ell)}(\Theta).                   \tag{5}
\]
Here \(y_{\pi a}=\tau y_a\), and the backward fields are linear in
the readout. No oddness of the activation is needed.

In each hidden update the signs in \(r_a\delta_a\) cancel.
For the first block also use \(x_{\pi a}^T=x_a^TQ\).
The readout update acquires the sign \(\tau\). Thus the raw
vector field is equivariant under \(\mathcal T\).

The scalar objective (1) is itself invariant under \(\mathcal T\),
since \(y_{\pi a}=\tau y_a\). This transformation is an isometry
of the raw parameter metric, so its scalar gradient is equivariant
as well. The Euler and limit arguments below therefore apply both
to physical loss updates and to auxiliary scalar feature updates,
using the corresponding equivariant clips.

The same calculation applies to finite clipped Euler provided:

- both samples use identical deterministic coordinate instructions;
- clips of sign-changing slots in (5) are odd, including any clipped
  readout, residual, or backward factor;
- additional norm cutoffs are invariant under \(\mathcal T\).

For example, to obtain a globally Lipschitz finite coordinate program,
cap preactivation arguments identically for both samples and cap
unbounded scalar factors before multiplication. Bottom updates remain
sums of scalar factors times the fixed input vectors; do not clip
the weight vector componentwise in a basis that breaks \(Q\)-equivariance.
For the smooth activations considered here this supplies suitable
fixed finite programs. Uniform removability of those auxiliary clips
is a separate issue.

For the resulting one-step map \(E_{R,\Delta}\),
\[
E_{R,\Delta}\mathcal T=\mathcal T E_{R,\Delta}.              \tag{6}
\]
Gaussian initialization is invariant under \(W^{(1)}\mapsto W^{(1)}Q\),
independently of the other blocks. The zero readout is invariant under
its sign change. Induction in (6) proves the joint path-law identity
\[
(\Theta_0,\ldots,\Theta_N)\overset{\rm law}=
(\mathcal T\Theta_0,\ldots,\mathcal T\Theta_N).              \tag{7}
\]
The small independent centered Gaussian finite readout in the stated model
also satisfies (7); its population limit is zero.

Equation (7) generally does not give \(f_2=\tau f_1\) in one finite
realization. With exactly zero initial readout, one raw physical Euler
step leaves the hidden state unchanged and gives
\[
C_1=\Delta\sigma(h_{1,0}^{(3)}+\tau h_{2,0}^{(3)}),
\]
\[
f_{1,1}-\tau f_{2,1}
=\Delta\sigma\left(\frac{\|h_{1,0}^{(3)}\|_2^2}{n}
                        -\frac{\|h_{2,0}^{(3)}\|_2^2}{n}\right),
\qquad \frac{\|v\|_2^2}{n}=n^{-1}\sum_i v_i^2.                      \tag{8}
\]
Those empirical diagonal norms need not agree. An exactly invariant
finite realization or an imposed pairing would be an additional
initialization condition. Even at \(\rho=-1\), the exact identity
\(z_2^{(1)}=-z_1^{(1)}\) does not equate shifted top feature norms.

### Deterministic population laws

The fixed-program input from the cited local proof is the following:
a fixed finite transcript of calls to independent Gaussian matrices
in both orientations, suitable Lipschitz coordinate instructions with
bounded derivatives, and iid finite-moment root tuples has deterministic
limiting same-layer joint empirical laws, including second moments.
Empirical scalar feedback is handled by causal freezing of already
constructed limiting contractions and finite induction. Singular query
Grams are treated at fixed transcript length.

In the present application, the root tuple contains either the entire
first weight row \(N(0,I_d/d)\), or its two projections with covariance
\(G\). It has all moments; the two hidden matrices have the required
independent Gaussian laws; and the auxiliary clips give the required
coordinate instructions. Adding a second sample adds finitely many
queries to the same matrices. In particular, singularity at \(\rho=-1\)
does not require a Gram inverse. This invokes only the finite-program
dependency, not a two-sample mesh-uniform estimate or uncut theorem.

Pass (7) to a deterministic limiting joint law of sample and time
slots. That law is invariant under the simultaneous transformations
(5). Second-moment convergence gives deterministic contractions
\[
f_{a,k}=\tau f_{\pi a,k},\qquad f_{a,k}=y_ag_k.              \tag{9}
\]
More explicitly, if \(F_n\) has a law invariant under \(F\mapsto\tau PF\)
and converges in probability to deterministic \(F\), its limiting
laws are both \(\delta_F\) and \(\delta_{\tau PF}\), forcing equality.
A random limit would not give that conclusion.

One may realize this symmetry exactly on the canonical population
spaces. Close the countable action/probe collection under the root
transformation and sample exchange. Its invariant joint law defines
measure-preserving involutions and composition operators \(U_\ell\)
on \(\mathcal H_\ell\). They are unitary involutions and commute
with pointwise coordinate functions. With \(w\) written as a column
field, initially
\[
U_1w_0=Qw_0,\qquad U_2A_0=A_0U_1,\qquad
U_3B_0=B_0U_2,\qquad C_0=0.                               \tag{10}
\]
The action identities first hold on paired matrix-query nodes and
extend to all generated \(L^2\) vectors by boundedness of the actions.

Direct induction in the population Euler updates preserves
\[
U_1w=Qw,\quad U_2A=AU_1,\quad U_3B=BU_2,\quad U_3C=\tau C,
\]
\[
U_\ell h_a^{(\ell)}=h_{\pi a}^{(\ell)},\qquad
U_\ell\delta_a^{(\ell)}=\tau\delta_{\pi a}^{(\ell)}.         \tag{11}
\]
For instance, conjugating a hidden update
\(\sum_a r_a\delta_a\otimes h_a\) gives
\(\sum_a r_a\tau\delta_{\pi a}\otimes h_{\pi a}\), the original
update because \(r_{\pi a}=\tau r_a\). The first/readout blocks
follow from the same substitutions used in (6). The prediction
identity follows from
\(\langle C,U_3h_a\rangle=\langle U_3C,h_a\rangle\).
This is an induction from the initial state, not a uniqueness argument.

Every strong fixed-clip mesh limit, and every subsequently constructed
strong uncut limit, inherits these identities. Joint-law symmetry
passes under weak convergence; contractions additionally require their
moment convergence. Thus the claim applies to limits of the symmetric
approximations on their constructed intervals. Extending it to every
arbitrary uncut solution requires a separate selection or uniqueness
result.

In this realization, \(C,H\) lie in the \(\tau\)-eigenspace of \(U_3\);
the other feature sector is orthogonal to \(C\). This does not equate
the two hidden sample fields or pair neurons from different layers.
The scalar objective still uses the full paired hidden state.

#### 3. Strong Hilbert radial coercivity

Let \(\mathcal X,\mathcal Y\) be real Hilbert spaces, and let
\(g(\vartheta,C)=\langle C,H(\vartheta)\rangle_{\mathcal Y}\).
Assume along a strong solution that bounded linear maps
\(J_s:\mathcal X\to\mathcal Y\) give
\[
C'=H(\vartheta),\qquad \vartheta'=J_s^*C,\qquad
\frac d{ds}H(\vartheta(s))=J_s\vartheta'(s),\qquad C(0)=0.   \tag{12}
\]
Then
\[
C''=J_sJ_s^*C,\qquad
\langle C,C''\rangle=\|J_s^*C\|_{\mathcal X}^2\ge0.         \tag{13}
\]
Sufficient strong regularity is that both curves are \(C^1\), the
feature chain rule holds strongly, and its right-hand side is
continuous. A Fréchet \(C^1\) feature map suffices but is not necessary.

The radial conclusion itself needs only
\[
C\in C^1([0,S);\mathcal Y),\quad
C'\in AC_{\rm loc}((0,S);\mathcal Y),\quad
\langle C,C''\rangle\ge0\quad\hbox{a.e.}                  \tag{14}
\]
Absolute continuity is strong/Bochner absolute continuity. Under (14),
with \(h_0=\|C'(0)\|=\|H(\vartheta_0)\|\),
\[
\|C(s)\|\ge sh_0,\qquad \|C'(s)\|\ge h_0
\quad(0\le s<S).                                         \tag{15}
\]

Proof: set \(r_\epsilon=(\|C\|^2+\epsilon^2)^{1/2}\). On compact
subintervals of \((0,S)\), strong Hilbert differentiation and
Cauchy--Schwarz give, almost everywhere,
\[
r_\epsilon''
=\frac{\|C'\|^2+\langle C,C''\rangle}{r_\epsilon}
 -\frac{\langle C,C'\rangle^2}{r_\epsilon^3}
\ge\frac{\epsilon^2\|C'\|^2}{r_\epsilon^3}
   +\frac{\langle C,C''\rangle}{r_\epsilon}\ge0.             \tag{16}
\]
Thus \(r_\epsilon\) is convex. Uniform convergence to \(r=\|C\|\),
then continuity at zero, makes \(r\) convex on \([0,S)\).
Since \(C(s)=sC'(0)+o(s)\), \(r'_+(0)=h_0\).
Convexity gives \(r(s)\ge sh_0\). For \(h_0>0\), \(r(s)>0\) for
\(s>0\), so
\[
h_0\le r'(s)=\frac{\langle C,C'\rangle}{\|C\|}
             \le\|C'(s)\|.
\]
For \(h_0=0\), (15) is immediate. This proves the claim, including
zeros of \(C\), without finite-dimensional compactness or coordinate
summation.

For (12), the scalar chain rule also yields
\[
g'=\|H\|^2+\|J_s^*C\|^2=\|\Theta'\|^2\ge h_0^2.           \tag{17}
\]
Alternatively \(g=\langle C,C'\rangle=rr'\ge sh_0^2\).
The conclusion is a uniform lower bound on feature speed/norm; it
does not assert that \(\|C'\|\) itself is monotone or that features
are pointwise positive.

The clipped backward equation need not be a gradient equation, and
explicit Euler need not preserve (13), (16), or (17). The symmetry
argument operates at clipped Euler level; this lemma operates on a
constructed strong uncut gradient path, or on finite uncut GF.

#### 4. Application in the raw population metric

The affine hidden Hilbert space has coordinates
\[
\vartheta=(w-w_0,A-A_0,B-B_0),\qquad
\|\dot\vartheta\|_{\mathcal X}^2
=d\,\mathbb E_1\|\dot w\|_{\mathbb R^d}^2
 +\|\dot A\|_{\rm HS}^2+\|\dot B\|_{\rm HS}^2.              \tag{18}
\]
Add \(\|\dot C\|_3^2\) for the full state. This matches the stated model.
The initial actions need only be bounded. Trained rank-one increments
are Hilbert--Schmidt since
\(\|u\otimes v\|_{\rm HS}=\|u\|\|v\|\), including for their Bochner
integrals.

It suffices for the following regularity argument that
\(\phi\in C^1(\mathbb R)\) have bounded continuous derivative.
It has at most linear growth; the features are therefore in \(L^2\)
at every affine Hilbert state. Forward propagation is locally
Lipschitz in (18), using bounded current actions,
\(\|M\|_{\rm op}\le\|M\|_{\rm HS}\), and the Lipschitz activation.
Features and their bounded linearizations are bounded on bounded
affine state balls.

Here is the strong chain rule actually needed. If \(z(s)\) is
\(L^2\)-valued \(C^1\), \(v=z'(s)\), and
\[
a_h=\int_0^1\phi'(z(s)+u[z(s+h)-z(s)])\,du,
\]
then
\[
\frac{\phi(z(s+h))-\phi(z(s))}{h}
   =a_h\frac{z(s+h)-z(s)}h.
\]
The multipliers are uniformly bounded and converge in probability
to \(\phi'(z(s))\). Split the difference from \(\phi'(z(s))v\)
into \(a_h[(z(s+h)-z(s))/h-v]\) and
\([a_h-\phi'(z(s))]v\).
The first tends to zero in \(L^2\) by strong differentiability.
For the second, truncate the fixed \(L^2\) vector \(v\), pass to
the limit with bounded multipliers, and then remove its \(L^2\) tail.
This also proves continuity of the resulting derivative. Bounded
bilinear operator actions obey the strong product rule.

For a hidden variation \((v,M_2,M_3)\), the notation \(J=DH\) means
the following bounded directional linearization with this path
chain rule:
\[
\dot z_a^{(1)}=v\cdot x_a,\quad
\dot h_a^{(1)}=\phi'(z_a^{(1)})\dot z_a^{(1)},
\]
\[
\dot z_a^{(2)}=M_2h_a^{(1)}+A\dot h_a^{(1)},\quad
\dot h_a^{(2)}=\phi'(z_a^{(2)})\dot z_a^{(2)},
\]
\[
\dot z_a^{(3)}=M_3h_a^{(2)}+B\dot h_a^{(2)},\quad
J(v,M_2,M_3)=\frac12\sum_a y_a\phi'(z_a^{(3)})\dot z_a^{(3)}.
                                                               \tag{19}
\]
This does not claim Fréchet differentiability of a nonlinear
Nemytskii map on all of \(L^2\).

Set
\[
\delta_a^{(3)}=C\phi'(z_a^{(3)}),\quad
\delta_a^{(2)}=\phi'(z_a^{(2)})B^*\delta_a^{(3)},\quad
\delta_a^{(1)}=\phi'(z_a^{(1)})A^*\delta_a^{(2)}.
\]
Taking adjoints in (19) gives
\[
J^*C=\left(
 \frac1{2d}\sum_a y_a\delta_a^{(1)}x_a,\quad
 \frac12\sum_a y_a\delta_a^{(2)}\otimes h_a^{(1)},\quad
 \frac12\sum_a y_a\delta_a^{(3)}\otimes h_a^{(2)}
\right).                                                    \tag{20}
\]
In particular,
\[
(z_a^{(1)})'=\frac12\sum_bG_{ab}y_b\delta_b^{(1)}.          \tag{21}
\]
The off-diagonal coupling is retained. At \(\rho=-1\) this preserves
\(z_2^{(1)}=-z_1^{(1)}\) and requires no Gram inverse.

The scalar \(g\) is \(C^1\) in the affine Hilbert norm. Formulae
(19)--(20) first give its directional gradient \((J^*C,H)\).
This gradient is norm continuous: use the fixed-factor truncation
argument for bounded gates, successively backwards, and the
rank-one difference inequality in HS norm. Integrating the
directional derivative along a line segment then gives
\[
g(\Theta+v)-g(\Theta)-\langle\nabla g(\Theta),v\rangle
=\int_0^1\langle\nabla g(\Theta+uv)-\nabla g(\Theta),v\rangle\,du
=o(\|v\|).
\]
This proves scalar Fréchet differentiability without the stronger,
generally false \(L^2\)-feature assertion. For a constructed strong
solution of (20), the forward chain rule makes \(C\) strongly \(C^2\)
and proves (13), (17). It does not require an uncut uniqueness theorem.

The raw sample-kernel blocks are
\[
K^{(1)}_{ab}=G_{ab}
       \langle\delta_a^{(1)},\delta_b^{(1)}\rangle_1,
\]
\[
K^{(2)}_{ab}=\langle\delta_a^{(2)},\delta_b^{(2)}\rangle_2
               \langle h_a^{(1)},h_b^{(1)}\rangle_1,
\]
\[
K^{(3)}_{ab}=\langle\delta_a^{(3)},\delta_b^{(3)}\rangle_3
               \langle h_a^{(2)},h_b^{(2)}\rangle_2,\qquad
K^{(4)}_{ab}=\langle h_a^{(3)},h_b^{(3)}\rangle_3.
\]
Each is a Gram matrix in its parameter block, hence positive
semidefinite, including at \(\rho=-1\). Define
\[
\kappa_\ell=\frac14y^TK^{(\ell)}y,\qquad
\kappa=\sum_{\ell=1}^4\kappa_\ell
      =\|J^*C\|^2+\|H\|^2=g'.                             \tag{22}
\]
For example,
\[
\kappa_1\big|_{\rho=-1}
=\frac14\|y_1\delta_1^{(1)}-y_2\delta_2^{(1)}\|_1^2.
\]
Population symmetry gives equal diagonal entries in every block, so
\(y\) is its sum or difference eigenvector. Radial coercivity gives
\[
\kappa_4(s)=\|H(s)\|^2\ge\|H(0)\|^2=:\kappa_0.            \tag{23}
\]
At zero initial readout all hidden backward fields and hidden kernel
blocks vanish. Thus the initial total projected kernel equals
\(\kappa_0\).

#### 5. Initial projected kernels

Initial Gaussian propagation uses uncentered second moments, including
the constant activation shift. Let
\[
q_\ell=\mathbb E(h_{a,0}^{(\ell)})^2,\qquad
c_\ell=\mathbb E h_{1,0}^{(\ell)}h_{2,0}^{(\ell)},\qquad
q_0=1,\quad c_0=\rho.
\]
At each layer the initial preactivation pair is centered Gaussian
with diagonal \(q_{\ell-1}\) and off-diagonal \(c_{\ell-1}\).

For the affine comparator \(\phi_0(z)=1+z\),
\(q_\ell=1+q_{\ell-1}=\ell+1\) and
\(c_\ell=1+c_{\ell-1}=\ell+\rho\). Therefore
\[
K^{(4)}(0)=\begin{pmatrix}4&3+\rho\\3+\rho&4\end{pmatrix},
\qquad
\kappa_0=
\begin{cases}
(7+\rho)/2,&\tau=1,\\
(1-\rho)/2,&\tau=-1.
\end{cases}                                                \tag{24}
\]
These are \(3\) and \(1\) at \(\rho=-1\). The unprojected
eigenvalues are \(7+\rho\) and \(1-\rho\); (24) is half of those.
The affine model is a comparator, not an admissible nonlinear
resolution of the main contract.

For \(\phi_e=1+\psi_e\), \(\psi_e(z)=z+e\arctan z\), take any
fixed finite real \(e\). The function \(\psi_e\) is odd, continuous,
nonconstant, and of at most linear growth. If \((U,V)\) is centered
Gaussian with common variance \(q>0\), covariance \(c\), the new
moments satisfy
\[
\widetilde q-\widetilde c
 =\frac12\mathbb E[(\psi_e(U)-\psi_e(V))^2],\qquad
\widetilde q+\widetilde c
 =2+\frac12\mathbb E[(\psi_e(U)+\psi_e(V))^2]\ge2.             \tag{25}
\]
For \(-q<c<q\), the pair has positive density on every open rectangle.
Continuity and nonconstancy give an open rectangle where the two
function values differ, proving positivity of the first expression.
For \(c=-q\), \(V=-U\) almost surely, and that expression is
\(2\mathbb E\psi_e(U)^2>0\). A nonconstant odd continuous function
cannot vanish almost everywhere under a Gaussian with positive
variance.

Starting at \(q_0=1,c_0=\rho<1\), (25) thus gives positive contrast
at the first layer, even at \(\rho=-1\). Also \(q_\ell+c_\ell>0\),
so subsequent preactivation pairs satisfy
\(-q_\ell<c_\ell<q_\ell\). Induction through all three layers yields
\[
\kappa_0^{\rm opp}=(q_3-c_3)/2>0,\qquad
\kappa_0^{\rm same}=(q_3+c_3)/2\ge1.                        \tag{26}
\]
In particular any universally fixed \(e>0\) has strictly positive
initial contrast for every \(\rho<1\), including \(-1\).

For \(e\ge0\), \(\psi_e'\ge1\) and oddness give
\[
|\psi_e(u)-\psi_e(v)|\ge|u-v|,\qquad
|\psi_e(u)+\psi_e(v)|\ge|u+v|.
\]
Thus \(q_\ell-c_\ell\ge q_{\ell-1}-c_{\ell-1}\) and
\(q_\ell+c_\ell\ge2+q_{\ell-1}+c_{\ell-1}\), so
\[
\kappa_0^{\rm opp}\ge(1-\rho)/2,\qquad
\kappa_0^{\rm same}\ge(7+\rho)/2.                          \tag{27}
\]
These are initial-kernel calculations, not a nonlinear response
estimate or a separation bound uniform as \(\rho\uparrow1\).

#### 6. Pre-target feature budget, energy, and physical clock

On any constructed strong uncut feature path with \(\kappa_0>0\),
\[
g'(s)\ge\kappa_0,\quad g(s)\ge\kappa_0s,\quad
g(s)<1\ \Longrightarrow\ s<S_0:=1/\kappa_0.                \tag{28}
\]
For \(e\ge0\), sufficient deterministic pre-target budgets are
\[
S_0\le
\begin{cases}
2/(7+\rho),&\text{same labels},\\
2/(1-\rho),&\text{opposite labels}.
\end{cases}                                                \tag{29}
\]
The entire pre-target feature interval is therefore bounded in terms
of the fixed pair. No arbitrary extra interval after the target is
needed to define the physical clock.

For \(0\le u<v\) before the target, the exact gradient identity gives
\[
\int_u^v\|\Theta'(s)\|^2\,ds=g(v)-g(u),\qquad
\|\Theta(v)-\Theta(u)\|
\le\sqrt{(v-u)[g(v)-g(u)]}\le\sqrt{v-u},                    \tag{30}
\]
and in particular
\[
\|\Theta(s)-\Theta(0)\|\le\sqrt{s\,g(s)}\le\sqrt{S_0}.       \tag{31}
\]
Hence a pre-target branch approaching a finite endpoint is strongly
Cauchy and has finite energy and length. Completeness gives a finite
affine Hilbert limit: first field/readout in \(L^2\), trained matrix
increments in HS norm and therefore operator norm, and every forward
feature in \(L^2\). This rules out state-norm blow-up and loss of
strong convergence along this single path. No compactness of bounded
Hilbert balls is asserted.

The gradient is bounded on the ball (31), by bounded gates, bounded
actions, and bounded forward \(L^2\) norms in (20). Its norm
continuity gives a finite limiting velocity at the endpoint, so the
path extends to the endpoint itself as a strong solution.

The continuation claim has a precise additional hypothesis. If local
existence is available at every such reached state, a maximal
pre-target endpoint with limiting \(g<1\) can be extended, and a first
hit \(s_*\le S_0\) follows. This uses local existence, not uniqueness.
For a smooth finite-dimensional scalar feature equation, local
Lipschitzness gives that existence. A continuous vector field on an
infinite Hilbert space does not by itself have a general Peano
existence theorem; the nonlinear population argument must supply its
own reached-state construction and control of its solution class.
The energy bound does not replace that work or apply automatically
to clipped Euler.

Suppose now that the symmetric feature path has been constructed
through a finite state with \(g(s_*)=1\). Its continuous kernel is
bounded on \([0,s_*]\), say \(\kappa_0\le g'\le M<\infty\).
Define
\[
t(s)=\int_0^s\frac{du}{2[1-g(u)]},\qquad 0\le s<s_*.
                                                               \tag{32}
\]
Since \(1-g(s)=\int_s^{s_*}g'(u)\,du\le M(s_*-s)\), this integral
diverges as \(s\uparrow s_*\). Its inverse is a global physical
clock with \(s(t)<s_*\) for every finite \(t\). Along that path,
\[
1-g(t)=\exp\!\left[-2\int_0^t\kappa(s(v))\,dv\right]
 \le e^{-2\kappa_0t},\qquad L(t)\le e^{-4\kappa_0t}.        \tag{33}
\]
The scalar clock is unique on this given feature path because its
right-hand side is \(C^1\). This is not a uniqueness or width-limit
claim for the full two-sample system.

#### 7. Affine baseline: positive hidden variances through a target margin

This section concerns the scalar feature ascent of (1) with
\(\phi_0(z)=1+z\). Finite auxiliary systems used in its proof also
ascend this scalar \(g\); they are not asserted to equal finite-width
two-sample loss training. The latter distinction is necessary because
(8) generally prevents an exact finite-width scalar loss reduction.

### Existence on a compact interval through \(g=1+\gamma\)

In the affine model, \(H\) is a finite sum of continuous multilinear
expressions in the hidden Hilbert variables. For example these include
\(B{\bf1}\), \(BA{\bf1}\), and \(BA(w\cdot x_a)\), with bounded
initial actions plus HS variations. Thus \(g\) is a continuous
polynomial on the affine Hilbert space, and its gradient is locally
Lipschitz with bounded derivatives on bounded balls.

This gives local strong existence and uniqueness in infinite dimension:
on a closed ball around the initial state, let the vector field have
bound \(M\) and Lipschitz constant \(L\). For a time interval of length
less than the radius divided by \(M\), and less than \(1/L\), the
integral map on continuous curves in that ball maps it into itself and
is a contraction. Its fixed point solves the ODE. This construction
also applies at any finite reached state.

Fix any finite \(b=1+\gamma>1\), independent of width or \(e\).
While \(g<b\), the radial and energy arguments give
\[
s<b/\kappa_0,\qquad
\int_0^s\|\Theta'\|^2=g(s)<b,\qquad
\|\Theta(s)-\Theta(0)\|\le b/\sqrt{\kappa_0}.               \tag{34}
\]
If a maximal branch stopped before hitting \(b\), (30), with \(b\)
in place of \(1\), would give a finite strong endpoint; the preceding
local construction would extend it. A branch staying below \(b\)
for arbitrarily large feature time contradicts \(g(s)\ge\kappa_0s\).
Hence there is a unique first hit
\[
S_b\le b/\kappa_0,\qquad g(S_b)=b,
\]
and a strong bounded affine baseline on \([0,S_b]\). Its local
existence/uniqueness has now been justified, rather than imported
from an unconstructed nonlinear equation. Finite Euler convergence
on this interval follows from the same bounded-ball Lipschitz
estimate and the integral equation.

### Common and contrast coordinates

To avoid confusing dimension \(d\) with a contrast vector, write
\[
m=(x_1+x_2)/2,\qquad v=(x_1-x_2)/2,\qquad m\cdot v=0,
\]
\[
v_M=\|m\|^2/d=(1+\rho)/2,\qquad
v_D=\|v\|^2/d=(1-\rho)/2>0.
\]
Define the common and contrast preactivations
\[
M_\ell=(z_1^{(\ell)}+z_2^{(\ell)})/2,\qquad
D_\ell=(z_1^{(\ell)}-z_2^{(\ell)})/2.
\]
For the affine network they satisfy the exact identities
\[
M_1=w\cdot m,\quad D_1=w\cdot v,\quad
M_2=A({\bf1}+M_1),\quad D_2=AD_1,
\]
\[
M_3=B({\bf1}+M_2),\quad D_3=BD_2,\qquad
z_a^{(\ell)}=M_\ell+(-1)^{a-1}D_\ell.                     \tag{35}
\]
Initially \(M_1,D_1\) are independent Gaussian fields of variances
\(v_M,v_D\); \(v_M=0\) is permitted. Initial forward Gaussian
propagation gives
\[
\mathbb E D_{\ell,0}=0,\qquad \|D_{\ell,0}\|_\ell^2=v_D
\quad(\ell=1,2,3).                                       \tag{36}
\]

### Opposite labels

Now \(H=\sigma D_3\) and
\[
g=\sigma\langle C,BAD_1\rangle.
\]
The feature equations reduce exactly to
\[
C'=\sigma D_3,\quad
B'=\sigma C\otimes D_2,\quad
A'=\sigma B^*C\otimes D_1,\quad
D_1'=\sigma v_D A^*B^*C,\quad M_1'=0.                     \tag{37}
\]
These are a deep linear scalar feature objective, with bottom
metric factor \(v_D\). The constants cancel in the objective, but
remain in the common preactivations (35).

The transformation \(D_{1,0}\mapsto-D_{1,0}\) preserves initialization.
In (37) it sends \(D_\ell,C\) to their negatives and leaves \(A,B,M_1\)
unchanged. This is already an exact finite Euler equivariance;
it passes to the constructed affine flow. The common fields in
(35) are unchanged by that transformation. Consequently each
deterministic population joint law satisfies
\[
\mathbb E D_\ell(s)=0,\qquad
\mathbb E[M_\ell(s)D_\ell(s)]=0.
\]
Thus
\[
\operatorname{Var}(z_a^{(\ell)}(s))
=\operatorname{Var}(M_\ell(s))+\|D_\ell(s)\|_\ell^2.        \tag{38}
\]

By (24), \(g'(s)\ge\kappa_0=v_D\), hence \(g(s)>0\) for every
\(s>0\). If any of \(D_1,D_2,D_3\) were zero in its Hilbert space,
the bounded-action identities in (35) would give \(D_3=0\), hence
\(g=0\), a contradiction. All three contrast norms are therefore
positive for \(s>0\); they are positive at zero by (36).
Strong continuity and compactness of the time interval imply
\[
b_D:=\min_{\ell=1,2,3}\ \min_{0\le s\le S_b}
               \|D_\ell(s)\|_\ell>0.
\]
Together with (38),
\[
\inf_{a,\ell,\,0\le s\le S_b}
     \operatorname{Var}(z_a^{(\ell)}(s))\ge b_D^2>0.       \tag{39}
\]
This includes \(\rho=-1\), where \(v_D=1\) and \(M_1=0\).
The bound may depend on the fixed pair and on \(b\).

### Same labels

Here
\[
H=\sigma({\bf1}+M_3),\qquad
g=\sigma\langle C,{\bf1}+B[{\bf1}+A({\bf1}+M_1)]\rangle.
\]
The scalar objective and its training equations depend only on
\(M_1,A,B,C\). Explicitly,
\[
C'=\sigma({\bf1}+M_3),\quad
B'=\sigma C\otimes({\bf1}+M_2),\quad
A'=\sigma B^*C\otimes({\bf1}+M_1),
\]
\[
M_1'=\sigma v_M A^*B^*C,\qquad D_1'=0.                    \tag{40}
\]
Thus the contrast root is frozen and independent of the information
that drives this scalar training. Independence at the root alone
does not assert independence of trained matrices from their own
initial disorder. The following conditional fixed-Euler argument
handles that dependence before taking a continuous-time limit.

Let
\(\mathscr F_n=\sigma(M_{1,0},A_0,B_0)\), with the readout initially
zero. Every step of the finite scalar affine Euler prefix
\(M_1,A,B,C\) is measurable with respect to \(\mathscr F_n\).
Meanwhile \(D_0=D_{1,0}\) is an independent
\(N(0,v_DI_n)\) vector. For every \(\mathscr F_n\)-measurable matrix
\(T_n\),
\[
\mathbb E[\frac{\|T_nD_0\|_2^2}{n}\mid\mathscr F_n]
       =\frac{v_D}{n}\|T_n\|_F^2.                        \tag{41}
\]
This is the exact normalization: a bounded ordinary Frobenius
increment has conditional squared RMS action \(O(n^{-1})\), not
an asserted \(O(n^{-1})\) Frobenius norm.

On a fixed finite Euler prefix, bounded initial operator norms and
bounded \(\frac{\|M_{1,0}\|_2}{\sqrt n}\) give bounds on all field norms and
on the ordinary Frobenius norms of the learned increments by
finite induction in (40). Each matrix increment has Frobenius norm
equal to the product of its two factors' RMS norms times its step
size. These bounds can depend on the fixed prefix; no mesh-uniform
response estimate is used. The energy bound gives corresponding
bounds for an exact scalar gradient path on a bounded target interval.
In particular \(\|A_s-A_0\|_F,\|B_s-B_0\|_F\) and current operator
norms are bounded at each Euler node \(s\). Therefore
\[
\|B_sA_s-B_0A_0\|_F
\le\|B_s-B_0\|_F\|A_s\|_{\rm op}
  +\|B_0\|_{\rm op}\|A_s-A_0\|_F
\]
is bounded as well. Applying (41) to the two difference matrices gives
\[
\frac{\|(A_s-A_0)D_0\|_2}{\sqrt n}\longrightarrow0,\qquad
\frac{\|(B_sA_s-B_0A_0)D_0\|_2}{\sqrt n}\longrightarrow0                 \tag{42}
\]
in probability, on the usual bounded-initial-operator events.
These events and the scalar-training bounds can be taken
\(\mathscr F_n\)-measurable, so conditioning is legitimate.
Pass these identities through the deterministic fixed-program law.
They state exact zero action of each learned difference on the
contrast root in the population Euler program.

At initialization \(D_0,A_0D_0,B_0A_0D_0\) have deterministic
same-layer Gaussian limits of variance \(v_D\). For example,
conditional on \(D_0\), the coordinates of \(A_0D_0\) are independent
centered Gaussians of variance \(\frac{\|D_0\|_2^2}{n}\); this variance converges
to \(v_D\). Conditional on \(A_0D_0\), the same argument applies to
the independent \(B_0\). Combining with (42), the contrast field in
each layer equals its initial field in every population Euler prefix.
Strong Euler convergence on the affine interval, already justified
by its polynomial gradient, preserves that equality at every time.
In particular its variance remains \(v_D\).

One must also check covariance with the common field. For
\(\mathscr F_n\)-measurable \(q_n\), \(P_n\), with bounded
\(\frac{\|q_n\|_2}{\sqrt n}\) and \(\|P_n\|_{\rm op}\),
\[
\mathbb E[\frac{( q_n)^\top(P_nD_0)}{n}\mid\mathscr F_n]=0,
\]
\[
\mathbb E[\frac{( q_n)^\top(P_nD_0)}{n}^2\mid\mathscr F_n]
=\frac{v_D}{n^2}\|P_n^Tq_n\|_2^2
\le\frac{v_D}{n}\|P_n\|_{\rm op}^2\frac{\|q_n\|_2^2}{n}.            \tag{43}
\]
Take \(P_n=I,A_s,B_sA_s\), and \(q_n={\bf1}\) or the
corresponding \(M_\ell(s)\). Fixed-program convergence proves zero
contrast mean and zero common--contrast covariance at every
population Euler node. Strong Euler convergence and continuity of
inner products preserve them on the full affine interval. Therefore
\[
\operatorname{Var}(z_a^{(\ell)}(s))
=\operatorname{Var}(M_\ell(s))+v_D\ge v_D
=\frac{1-\rho}{2}>0                                     \tag{44}
\]
on the whole affine interval.

In particular, the proposed same-label argument is sound after
specifying scalar training, conditional independence, and the
normalization (41). HS boundedness without that independence would
not suffice: a learned rank-one operator built from the contrast
itself could have a nonvanishing action on it. No assertion here
makes the Gaussian initial actions independent of the training path.

### Gaussianity and the arctangent affine-approximation error

Positive variance by itself would not ensure positive best affine
approximation error: a two-point law would be a counterexample.
The affine baseline also has Gaussian preactivation laws, as can
be justified at the finite-program level.

At each finite population Euler prefix for the affine model, every
forward, backward, or evolving vector field is an affine function
of finitely many jointly Gaussian source coordinates in its layer.
To see the induction, all
coordinate activation and gate operations are affine or constant.
After unrolling a trained matrix into its initial action plus
rank-one updates, each learned contribution is a previous coordinate
times a deterministic population contraction. A new initial-matrix
call, by the finite Gaussian-conditioning dependency, is a Gaussian
innovation plus response terms that are linear combinations of
previous coordinates with deterministic coefficients. No product
of two varying same-neuron coordinates is needed outside a scalar
population contraction. This proves the induction, allowing
singular Gaussian source covariances.

Bounded-interval strong Euler convergence for the polynomial affine
gradient passes these joint Gaussian laws and their second moments
to the exact affine path. A strong \(L^2\) limit of Gaussian vectors
is Gaussian: its means and covariances converge, and their Gaussian
characteristic functions converge to that of the limiting vector.
Thus each \(z_a^{(\ell)}(s)\) is Gaussian. Equations (39) and (44)
make its variance uniformly positive on \([0,S_b]\).

For a square-integrable real variable \(Z\) of positive variance,
define
\[
\mathcal R(Z)=\inf_{\alpha,\beta\in\mathbb R}
 \mathbb E[(\arctan Z-\alpha-\beta Z)^2]
=\operatorname{Var}(\arctan Z)
 -\frac{\operatorname{Cov}(Z,\arctan Z)^2}{\operatorname{Var}(Z)}.
                                                               \tag{45}
\]
The equality follows by first minimizing over the intercept to center
both variables, then minimizing the quadratic in the slope.
For a nondegenerate Gaussian \(Z\), \(\mathcal R(Z)>0\):
a zero minimum would say that \(\arctan z\) equals one affine
function Gaussian-almost everywhere. Positive density and continuity
would extend that identity to every real \(z\), contrary to the
nonconstant derivative \(1/(1+z^2)\).

The variance and covariance in (45) are continuous under strong
\(L^2\) convergence; here \(\arctan\) is bounded and Lipschitz.
The denominators are bounded below by (39) or (44).
Strong time continuity and compactness therefore give
\[
\eta_b:=\min_{a,\ell,\,0\le s\le S_b}
                 \mathcal R(z_{a,\mathrm{aff}}^{(\ell)}(s))>0,
                                                               \tag{46}
\]
Here \(z_{a,\mathrm{aff}}^{(\ell)}\) denotes the affine baseline.

This supplies the baseline needed for a separately proved \(O(e)\)
comparison. Precisely, if the main argument constructs a nonlinear
path on this same interval and proves
\[
\sup_{a,\ell,s\le S_b}
 \|z_{a,e}^{(\ell)}(s)-z_{a,\mathrm{aff}}^{(\ell)}(s)\|_2\le K|e|,
                                                               \tag{47}
\]
then all second moments remain bounded. Standard deviation is
1-Lipschitz under \(L^2\) distance, because it is the norm of the
orthogonal projection onto the mean-zero subspace. Thus (47)
preserves a positive variance lower bound for sufficiently small
fixed \(|e|\). Boundedness and Lipschitzness of arctangent give
\(O(|e|)\) changes in each variance and covariance in (45);
its denominator stays bounded away from zero. Consequently
\[
\inf_{a,\ell,s\le S_b}\mathcal R(z_{a,e}^{(\ell)}(s))
\ge\eta_b/2
\]
for sufficiently small fixed \(|e|\). Also
\[
\inf_{\alpha,\beta}
 \mathbb E[(\phi_e(Z)-\alpha-\beta Z)^2]
=e^2\mathcal R(Z),                                       \tag{48}
\]
by absorbing \(1+Z\) into the free affine coefficients and rescaling
them (the equality is also valid at \(e=0\)).

Equations (46)--(48) are a conditional transfer statement. They
neither prove the nonlinear state comparison (47) nor control its
response recursion. Likewise a separately proved \(O(e)\) output
comparison at \(S_b\) would preserve a positive margin above \(g=1\).
The fixed affine interval through \(1+\gamma\), its positive hidden
variances, and its positive arctangent approximation error have been
established here.

### D.5. Primal comparison, cap removal and physical limits

Within this proof unit, unqualified section and equation numbers are local.

#### 1. A direct comparison, without comparing bad multipliers

The raw Hilbert state consists of the first weight field, HS increments
of W^(2),W^(3) around their bounded initial actions, and C=W^(4).
For differences use the sum of sqrt(d)||dw||_L2, the two HS norms, and
||dC||_L2. This controls each first preactivation difference since
||x_a||/sqrt(d)=1. At finite width these are sqrt(d/n)||dW^(1)||_F,
the two ordinary Frobenius norms, and ||dC||/sqrt(n). Initial matrix
HS norms need not be bounded; only their operator norms are used.

Let V_{epsilon,R} be the feature vector field with p_a=y_a/2 and
D_{epsilon,R}(z,q)=q+epsilon tau_R(q)/(1+z^2) in every backward gate.
Suppose each first preactivation norm, both matrix operator norms, and
the readout norm are at most B>=1. The following inequalities hold on
that ball, in both finite normalized norms and population L2 norms.
Compare epsilon and zero at the SAME state. For 0<=epsilon<=1,

    ||H^1_e|| <=4B,       ||H^1_e-H^1_0|| <=2 epsilon,
    ||H^2_e|| <=7B^2,     ||H^2_e-H^2_0|| <=4 epsilon B,
    ||H^3_e|| <=10B^3,    ||H^3_e-H^3_0|| <=6 epsilon B^2.

These follow successively from |phi_e(z)-(1+z)|<=pi epsilon/2 and
the bounded matrix actions. Likewise |D_e,R(z,q)-q|<=epsilon|q|
gives successively

    ||delta^3_e|| <=2B,   ||delta^3_e-delta^3_0|| <=epsilon B,
    ||delta^2_e|| <=4B^2, ||delta^2_e-delta^2_0|| <=3epsilon B^2,
    ||delta^1_e|| <=8B^3, ||delta^1_e-delta^1_0|| <=7epsilon B^3.

For example the middle incoming q differs by at most epsilon B^2;
the middle gate adds at most 2epsilon B^2. No comparison of
phi'(Z_e)-phi'(Z_0) multiplied by an uncontrolled q occurs here.
The rank-one difference inequality now gives component differences
at most 7,14,11,6 times epsilon B^3, respectively. Thus

    ||V_{epsilon,R}(Theta)-V_0(Theta)|| <=40epsilon B^3,
    ||V_{epsilon,R}(Theta)|| <=50B^3.                     (1)

The sum-norm Lipschitz bound for V_0 on this ball is 9B^2, as follows
by the four component estimates in Fragment D.2 (the first
field norm uses sum |p_a| ||x_a||/sqrt(d)=1). The same bound holds
in HS rather than operator differences, since rank-one HS norms
are products of field L2 norms and ||M||_op<=||M||_HS.

For affine and nonlinear Euler programs with the SAME initial state,
comparison until exit from the ball consequently gives

    E_{k+1}<=(1+9B^2 h_k)E_k+40epsilon B^3 h_k,
    max_{s_k<=S} E_k <=40epsilon B^3 S exp(9B^2 S).        (2)

The identical integral Gronwall bound holds for their strong flows.
Choose B so the affine flow has primal bound strictly below B/2 on
[0,S], and use affine Euler convergence for all sufficiently fine
meshes. If the right side of (2) is less than B/4, the usual first-exit
induction closes with a strict margin; this holds uniformly in R.
Fixed R vector fields are locally Lipschitz on the raw Hilbert state,
so they have local strong solutions and this comparison extends them
through S. A bounded vector field along a finite interval gives a strong
endpoint, and local Lipschitzness permits continuation at that endpoint.

The initial fields/operators can be realized on one common generated
space containing all the countably many cap/mesh programs and the
affine programs; this is the explicit common-action construction of
the baseline dependency. Thus (2) is a strong comparison on a common
space, not a comparison of marginal Gaussian covariances. A fixed
epsilon can be selected before this construction; no uncountable
simultaneous collection or width-dependent activation is necessary.

Let S be the affine first hit of g_0=3/2. The radial/affine proof in D.4 supplies a finite S and a finite primal bound. Equation (2)
and the same-state query estimates imply O(epsilon) strong differences
in every forward/backward query and their scalar second moments,
uniformly in R and sufficiently fine mesh. Shrinking a fixed epsilon
once makes g_{epsilon,R}(S)>5/4 for all R. The shrinkage can depend on
the fixed input pair, since S and B do. No universality follows.

#### 2. The precise additional premise and removal of auxiliary caps

RESPONSE-TAIL PREMISE: for some fixed positive epsilon as above, the
actual nonlinear feature Euler programs on [0,S] satisfy mesh- and
cap-independent Gaussian tail bounds for each sample's incoming
q^(1), q^(2), and the shared C, in the following norm form:

    sup_{R,k,a} || |Q_{R,k,a}| 1_{|Q_{R,k,a}|>u} ||_L2
          <= C exp(-c u^2),  u>=u_0.                    (3)

Q ranges over those three groups; constants may depend on S,epsilon,
and the input pair. Appropriate changes of c,C convert subGaussian
Lp bounds into (3): Markov with p proportional to u^2 bounds tails,
and integration bounds their second moment. This premise must be
proved for the actual nonlinear programs, not all inputs of an
initial Gaussian action. Fragment D.3 supplies
this proof with precisely the bounded affine premise established in
Part 1 and the two baseline notes. Fixed-cap Euler convergence passes (3) to
their strong feature flows (use continuous truncated-square bounds).

For R'>=R, or for R'=infinity, the exact asymmetric gate difference is

 D_{e,R'}(z_A,q_A)-D_{e,R}(z_B,q_B)
  =(q_A-q_B)+e g'(z_A)[tau_{R'}(q_A)-tau_{R'}(q_B)]
    +e[g'(z_A)-g'(z_B)]tau_R(q_B)
    +e g'(z_A)[tau_{R'}(q_B)-tau_R(q_B)],                 (4)

where g=arctan. The incoming difference coefficient is at most 2;
the z difference coefficient is at most 4eR; and the last term is
bounded by 2e|q_B|1_{|q_B|>R}. Successively substitute the forward
state bounds and then the three backward gates. At each stage the
previous incoming error is multiplied only by a bounded matrix norm
and 2, not by R. The new R factor multiplies a forward-state error
which already has an R-independent bound. Thus

    ||V_{e,R'}(Theta_A)-V_{e,R}(Theta_B)||
       <= C_B(1+eR)||Theta_A-Theta_B||
          +C_B e sum_Q || |Q_B|1_{|Q_B|>R} ||_L2.         (5)

This holds if both states have bounded primal sizes, with no tail
condition on A. All rank products use L2 times L2 in HS norm. It also
proves local Lipschitzness for each fixed R on arbitrary raw states.

Combining (3),(5) and Gronwall gives

    sup_{s<=S} ||Theta_{R'}(s)-Theta_R(s)||
          <= C exp(C(1+eR)S-cR^2).                      (6)

Hence the cap family converges strongly on the full fixed interval,
including matrix increments in HS norm. Formula (5) and the Gaussian
tail imply uniform convergence of the vector fields as well. The
limit is a C1 strong solution of the uncut, autonomous raw gradient
equation. An arbitrary competing bounded-primal strong solution on
a compact interval is compared to Theta_R by (5) with R'=infinity.
It has the same initial state and requires no tail hypothesis of its
own. Sending R to infinity proves uniqueness.

The same argument proves uniqueness after any reached time s_0: the
initial discrepancy of the cap reference from the reached uncut state
obeys (6), and multiplication by exp(CR(S-s_0)) still makes it vanish.
The already constructed path supplies existence after reached states.
No claim of local existence at every point of the full L2 state space
is needed or made. Initial actions remain part of the finite collection
of state operators; there is no external trajectory oracle.

Symmetry passes from the Euler constructions, so f_a=y_a g on this
path. It is a true uncut gradient path and the radial argument applies.
It has a first hit s_*<S of g=1, with positive projected kernel bounded
below by its initial value. The physical clock ds/dt=2(1-g) covers all
finite t and stays below s_*. This constructs one uniquely restartable
population physical flow, conditional precisely on (3).

#### 3. Why the genuine two-residual finite dynamics also matter

The finite system is NOT exactly symmetric and cannot use that scalar
clock. At fixed R, define its physical vector field using both actual
residuals, with D_{e,R} in each backward gate and the original readout
update. On a bounded primal ball, its vector field is Lipschitz with
constant C_B(1+eR): predictions are locally Lipschitz by forward
propagation and Cauchy--Schwarz. The same asymmetric estimate (5)
holds for physical fields, with changed B-dependent constants. There
is still only one linear R loss.

The population physical fixed-cap reference exists for every finite
T. Indeed its symmetric feature path satisfies g_R(0)=0 and
g_R(S)>5/4. Let s_R be its first hit of 1. Before it, 1-g_R>0, so
t(s)=integral_0^s du/[2(1-g_R(u))] is increasing. The bounded derivative
of g_R implies 1-g_R(s)<=M_R(s_R-s); hence t diverges at s_R. This
does not assume g_R is a gradient ascent or monotone. Its inverse
reparametrizes the symmetric cap feature path into the two-residual
physical field. The uniform primal bound and tails are inherited from
the entire feature interval [0,S].

For fixed R and physical T, the finite fixed-cap physical GF/Euler
programs converge to this reference as follows. At each fixed mesh,
finite-program joint empirical second moments identify all forward,
backward, velocity, and kernel slots, with residual contractions frozen
causally. To obtain bounded finite matrix operators, do not assume
operator-norm convergence of trained matrices. Unroll them: the initial
operators have bound 10 with probability tending to one; their learned
increments are bounded by the sum of step size times the product of
the two update-factor RMS norms. Those finitely many norms converge
to the reference norms. Refining the mesh gives their integrals, bounded
by C_B T because all update norms are bounded on the population path.
The first and readout fields have converging norms at those nodes.
This supplies a finite-width primal ball of radius B_T with slack,
uniformly over sufficiently fine meshes (width tends to infinity first).

On that larger ball, deterministic Euler--flow error is at most
C_{B_T,R,T}|mesh|, independent of width. The proof is the integral
local defect bound (1/2)L M h^2 and discrete Gronwall. A stopped
comparison plus the just-certified norm slack prevents exit. Taking
width to infinity at fixed mesh, then mesh to zero, therefore identifies
the actual finite fixed-cap physical GF on [0,T]. It likewise handles
any sufficiently fine Euler step including eta_n=n^-2. This is a
triangular convergence argument, not a growing-transcript Gaussian
identification claim.

For clarity, uniform-in-time tail convergence of the reference incoming
Q is available at fixed R. Its L2 time modulus follows from the locally
Lipschitz D_{e,R}, bounded vector field, and bounded matrix actions.
The positive-part tail norm ||(|Q|-u)_+||_L2 is 1-Lipschitz in Q. A
finite time net and fixed-program second-moment convergence thus give
uniform-time convergence of these tail norms. Using a threshold u=R/2
dominates the raw |Q|1_{|Q|>R} tail up to a factor 2, retaining Gaussian
decay in the population reference by (3).

Compare the actual uncut finite GF against its SAME-WIDTH physical
fixed-cap reference, using (5). Until exit from a larger primal ball,
the error is bounded by an exp(C_{B_T,T}R) factor times the reference
tail error. Take width to infinity at fixed R, use (3), then send R
to infinity. The result tends to zero, and the strict state/length
margin prevents exit with probability tending to one. This proves
full-sequence joint convergence in probability; no subsequence choice
of population solutions is involved.

For raw exact GD, compare its parameter interpolation directly to the
same finite fixed-cap GF. Its derivative at time t is the uncut vector
field at the preceding GD node k eta_n. Apply the asymmetric estimate
there against the cap reference at k eta_n. The difference from the cap
reference derivative at t is at most L_R M_R eta_n. Thus the same
stopped Gronwall estimate has one extra vanishing C_{R,T} eta_n term.
This avoids any n-dependent Lipschitz constant of the uncut field.
No F-coordinate correction arises: the raw algorithm is exactly Euler
for the physical raw equations. Hidden objects are recomputed from
the raw interpolation, in the stated raw model.

#### 4. Observables and nontriviality obligations

Strong parameter-state comparison implies forward-field convergence by
the Lipschitz activation and bounded actions. The asymmetric gate
estimate and the reference tails give all backward fields and raw
velocities. Matrix increments converge in HS and both matrix directions
on converging L2 probes follow from their uniform operator bounds.
Products of two converging L2 fields have converging expectations, so
all four 2-by-2 raw kernels, including off-diagonals, are retained.

The same claim for hidden velocities uses the actual product/chain rule.
For example dot Z^2_a=dot W^2 H^1_a+W^2[phi'(Z^1_a) dot Z^1_a].
special-data Section III.V supplies the fixed-cap empirical law and
uniform-time reference tails. Its exact deterministic comparison (III.V.29)
says that two bounded states/directions with discrepancies a,b have
total hidden-velocity error at most

    K[b+(1+M)a+sum_{ell,a} ||(|P_ref^(ell)_a|-M)_+||_L2],

where P_ref is the reference PREACTIVATION velocity, and K depends only
on bounded primal/raw-direction sizes and the activation, not on the
cap or the truncation level M. Its proof is the three-layer product
rule, truncating the reference factor in a gate difference. This is
also valid at finite width with RMS norms.

There is an important ordering point in removing R for velocities:
do NOT assume the explicit fixed-cap velocity moment constants grow
slowly enough in R. Instead, population cap paths and raw directions
already converge uniformly in the strong state norm to the uncut path
and direction, by (5)--(6) in physical time. The uncut forward chain
rule gives continuous L2 hidden velocities. Apply the deterministic
comparison with the UNCUT population velocity as reference. Its compact
L2 time image has uniformly vanishing tail norms: cover that image by
a finite L2 net and use that the positive-part tail norm is 1-Lipschitz.
First send R to infinity at fixed M, then send M to infinity. This
proves uniform strong convergence of population cap hidden velocities
to the uncut hidden velocities. In particular their tail norms are
uniformly vanishing as M grows for all sufficiently large R.

For the finite uncut system versus its same-width cap reference, raw
state AND raw-direction errors have width-limit upper bounds tending
to zero with R; (5) bounds the latter by C(1+eR) times (6) plus the
Gaussian tail. Apply the deterministic velocity comparison with that
finite cap reference. At fixed R,M its empirical velocity tail norms
converge uniformly in time by the fixed-cap bridge. Take width to
infinity, then R to infinity at FIXED M, using the population velocity
convergence just proved, and finally M to infinity. All error terms
vanish. This supplies the uncut hidden-velocity convergence without
any uncontrolled product of a cap-dependent moment constant and an
R-dependent state error. Node conventions are right derivatives,
terminal left derivatives, including the actual directions of the
raw interpolated GD rather than the vector field at its current state.

The hidden preactivation and feature PATH laws converge in
W_2(C([0,T])) with its supremum norm, not only in finite-time laws.
Here is the extra tight approximation needed for that assertion.
For any scalar absolutely continuous path x and its piecewise-linear
interpolant I_h x on a uniform observation grid of mesh at most h,

    sup_t |x(t)-I_h x(t)|^2 <=4h integral_0^T |x'(t)|^2 dt.

This follows on each grid interval by Cauchy--Schwarz applied to the
two increments from its endpoints, then bounds their interval energy
by the total energy. Averaging over finite neurons, or over a population,
gives a squared path-space W_2 coupling cost at most 4h times integrated
RMS speed squared. On the stopped bounded primal balls all those speeds
are uniformly bounded by forward product rules and bounded gates,
including the raw GD directions. The no-exit estimates already proved
remove the stopping with probability tending to one. At fixed h, joint
node empirical W_2 convergence passes through the linear interpolation
map into C([0,T]). Let h decrease to zero in the triangle inequality.
This proves the claimed path-space W_2 convergence for both samples
jointly in each layer. Integrated squared velocities converge by the
uniform-time velocity law and bounded second moments.

All-time strict nonaffinity is furnished, for the angle-specific route,
by the Gaussian nondegeneracy proved in D.4 on [0,S]. Its best affine
arctangent approximation error has a positive minimum. The strong
O(epsilon) state comparison in Part 1 preserves that positive error
for sufficiently small fixed epsilon. For phi_e the error is epsilon^2
times the arctangent error, so it is positive uniformly on the full
feature interval and hence at every finite physical time.


D.1 verifies the uniform angle-dependent choice, and D.6 proves the initial-motion conclusions.

### D.6. Offset initial motion

Within this proof unit, unqualified section and equation numbers are local.

Let phi(z)=1+z+epsilon arctan z with a fixed epsilon>0, and put
p_a=y_a/2. The proof works for every fixed rho in [-1,1), including
opposite labels and antipodal inputs. All expectations below are within
the displayed neuron population. Write W^(4)=C and
H=(y_1 H^(3)_1+y_2 H^(3)_2)/2. The scalar feature direction is the
gradient of g=E_3[C H] in the raw metric.

#### 1. Initial forward pairs and the first transpose return

At layer one the Gaussian preactivation pair has covariance Gamma.
Its feature pair has strictly positive definite uncentered second-moment
matrix. Indeed, for -1<rho<1 a vanishing linear combination of the two
features would vanish on all R^2, which is impossible for a nonconstant
activation. At rho=-1, write phi(z)=1+psi(z) with psi odd and strictly
increasing. A vanishing combination of phi(Z),phi(-Z) would say
(u_1+u_2)+(u_1-u_2)psi(Z)=0, forcing u_1=u_2=0. Subsequent fresh forward
Gaussian calls thus give nondegenerate Gaussian preactivation pairs in
populations two and three. Their feature Gram matrices are positive
definite by the same full-support argument. All these variables have
every finite moment.

Define, in population three,

    beta^(3)_a = H_0 phi'(Z^(3)_{a,0}).

Their uncentered second-moment matrix S_3 is positive definite. To prove
this, suppose E[(u_1 beta^(3)_1+u_2 beta^(3)_2)^2]=0. The preactivation
pair has positive density everywhere. Continuity makes

    [p_1 phi(z_1)+p_2 phi(z_2)]
        [u_1 phi'(z_1)+u_2 phi'(z_2)] = 0

an identity on R^2. For each fixed z_2, the first factor, as a function
of z_1, is strictly monotone and has at most one zero. Thus the second
factor vanishes for every z_1 by continuity. Its derivative in z_1
gives u_1 phi''(z_1)=0. Since epsilon>0 and phi'' is not identically
zero, u_1=0. Positivity of phi' then gives u_2=0. This proves S_3>0.

The reused transpose of W^(3)_0 is NOT a fresh iid-coordinate claim.
The fixed-program rule gives the joint empirical-average limit

    (W^(3)_0)^* beta^(3)_a
       = G^(2)_a + sum_b H^(2)_{b,0}
                              E_3[partial_{z_b} beta^(3)_a],       (1)

where (G^(2)_1,G^(2)_2) is centered Gaussian with covariance S_3 and
independent of the initial population-two forward sources. The second
term is precisely the response forced by the previous two forward uses;
the first is the unexplored Gaussian randomness. Formula (1) uses full
second moments, not the residual after projection onto forward features.

For clarity the two derivatives in this expression are exactly

    partial_{z_b} beta^(3)_a
       = p_b phi'(z_b) phi'(z_a)
           + 1_{a=b} [sum_c p_c phi(z_c)] phi''(z_a).

They have finite expectations. The output beta is an unbounded smooth
coordinate instruction with polynomially bounded derivatives, so the
bounded-derivative version of the dependency is applied first to smooth
caps. Removal at this SINGLE fixed transcript is justified by Gaussian
moments and the matrix operator bound: forward cap differences vanish
in RMS; backward input differences vanish in RMS; the transpose changes
by at most its bounded operator norm times that RMS difference. The
displayed expected derivatives converge by Gaussian dominated bounds.
This is a fixed-transcript argument, not mesh-uniform removal.

#### 2. The second transpose return cannot lose the noise

Set

    beta^(2)_a = phi'(Z^(2)_{a,0}) (W^(3)_0)^* beta^(3)_a.

Conditionally on the initial population-two forward pair, its covariance
is diag(phi'(Z^(2)_{1,0}),phi'(Z^(2)_{2,0})) S_3 diag(phi').
Since phi'>=1, its minimum eigenvalue is at least lambda_min(S_3)>0.
Consequently its uncentered second-moment matrix S_2 is positive definite.

Reusing the transpose of W^(2)_0 in turn gives

    (W^(2)_0)^* beta^(2)_a
       = G^(1)_a + sum_b H^(1)_{b,0}
                         E_2[partial_{xi^(2)_b} beta^(2)_a],       (2)

where G^(1) has covariance S_2 and is independent of the initial
population-one root pair. The derivative in (2) freezes all deterministic
response coefficients and covariances from (1); it includes the actual
dependence of its response term on H^(2). The Gaussian source G^(2) is
an independent named source in this derivative. All expressions have
finite moments; the same finite-transcript cap argument justifies (2).
Define beta^(1)_a=phi'(Z^(1)_{a,0}) (W^(2)_0)^* beta^(2)_a.

#### 3. Nonzero acceleration in every hidden parameter block

The following tensors and first-layer field are well-defined:

    V^(1) = (1/d) sum_a p_a beta^(1)_a x_a,
    V^(2) = sum_a p_a beta^(2)_a tensor H^(1)_{a,0},
    V^(3) = sum_a p_a beta^(3)_a tensor H^(2)_{a,0}.         (3)

A population tensor u tensor v acts on w as u E[v w]. Finite tensors
are u v^T/n. Its HS norm is the product of the two ordinary L2 norms.

The hidden feature map H has bounded linearization J_0 from the raw
hidden metric to population-three L2; direct differentiation and
adjunction give V=J_0^* H_0. This is a bounded directional linearization
with a strong path chain rule, not a claim of Frechet differentiability
of a nonlinear L2 Nemytskii map.

Both V^(2),V^(3) have strictly positive HS norm. For each, the squared
norm is sum_{a,b} p_a p_b E[beta_a beta_b] E[H_a H_b]. Both Gram
matrices are positive definite, and diag(p) is invertible, so this
equals the positive trace of the product of two positive definite
matrices. For V^(1), conditional covariance from (2) gives

    d E_1 ||V^(1)||^2
       >= lambda_min(S_2) sum_a p_a^2 ||x_a||^2/d
       = lambda_min(S_2)/2 > 0.                           (4)

This bound does not invert Gamma and holds for antipodal inputs.

On any constructed strong feature path for which the initial backward
fields satisfy delta^(ell)_a(s)=s beta^(ell)_a+o_L2(s), (3) implies

    hidden_state(s)=hidden_state(0)+(s^2/2)V+o(s^2),
    C(s)=s H_0+o_L2(s).                                  (5)

These initial derivative limits follow, for example, when the path is
strongly continuous in state, C(s)/s->H_0 in L2, and gates are bounded
and continuous: apply the fixed-factor multiplier convergence backwards,
using bounded current operators and phi'>0. Thus a C1 strong solution
with C'=H suffices; an Lp-in-time differentiability assumption is not
silently required. The hidden vector field divided by s converges by
the rank-one difference bound. Integrating proves (5).

In particular every hidden parameter block moves at order s^2. This is
not a kernel or frozen-hidden-layer limit; epsilon stays strictly
positive independently of width and physical time.

#### 4. Hidden features and the kernel also move

The initial hidden preactivation acceleration in sample a at layer one
is sum_b Gamma_ab p_b beta^(1)_b. Conditionally on Z^(1)_0, its variance
is at least lambda_min(S_2) sum_b Gamma_ab^2 p_b^2 phi'(Z_b)^2, hence
at least lambda_min(S_2)/4. It is nonzero for each sample.

Let U^(ell)_a denote the acceleration of Z^(ell)_a obtained by applying
the forward linearization to V, and use phi'(Z^(ell)_{a,0}) U^(ell)_a
for the feature acceleration. Product rules and adjunction give

    sum_a p_a E_2[beta^(2)_a U^(2)_a]
         = d E_1||V^(1)||^2 + ||V^(2)||_HS^2 > 0,
    sum_a p_a E_3[beta^(3)_a U^(3)_a]
         = ||V||_hidden^2 > 0.                            (6)

For the first equality, expand U^(2)_a=V^(2)H^(1)_a+
W^(2)_0[phi'(Z^(1)_a)(V^(1) dot x_a)]. The two terms give the two
squared norms by (3). The second equality adds the third matrix block
to the same calculation. Thus at least one sample acceleration in each
upper layer is nonzero. The initialization/sample-reflection symmetry
maps their joint law by exchanging samples, and maps U to the exchanged
U. Their squared norms are equal. Both sample accelerations are
therefore nonzero. Since phi'>=1, every hidden feature acceleration
is nonzero as well.

Finally the projected output kernel and total kernel satisfy

    kappa_4(s)=E_3[H(s)^2]
        =kappa_0+s^2 ||V||_hidden^2+o(s^2),
    kappa(s)=kappa_0+2s^2 ||V||_hidden^2+o(s^2).             (7)

Indeed H(s)=H_0+(s^2/2)J_0 V+o_L2(s^2), and
E[H_0 J_0 V]=||J_0^*H_0||^2=||V||^2. The sum of the three hidden
kernel blocks is the squared hidden gradient, s^2||V||^2+o(s^2).
The strong path chain rule gives the expansion of H from (5), or by
integrating H'=J_s hidden_state'. Bounded gates and fixed-factor
convergence suffice for J_s V->J_0 V.

The physical clock has s(t)=2t+o(t) initially, so the same conclusions
hold at positive sufficiently small physical times. Equation (7) is a
strict feature-learning certificate, not a claim that every separate
hidden velocity is nonzero at every later time. The latter stronger
property is not proved here. Nonaffinity of the activation under the
hidden distributions for ALL finite times is a separate requirement;
the affine-baseline nondegeneracy/approximation-error argument in
Fragment D.4 supplies it only after nonlinear comparison
and continuation have actually been constructed.

## E. The two-sample odd family at the second-power scale

In the exact model E.2, set
\[
 \eta_*={4\cdot404e^{-1}\over27\pi405^4},\quad
 C_0=1296000e^{1404},\quad C_z=1500C_0,\quad C_g=14400C_0,
\]
\[
 c_* =\min\{1/2,[2C_0(8\sqrt2)^3]^{-1},
 [4C_g(8\sqrt2)^{11/4}]^{-1},
 \sqrt{\eta_*}/[2C_z(8\sqrt2)^{7/2}]\},
\]
\[
 H=10^{30}(1+C_0+C_z+C_g+e^{1410})^4,
 \qquad c_{\rm poly}=\min\{1/4,c_*,10^{-70}H^{-400}\}.
\]
These are exact sufficient constants. In E.1, the reference to a primal/nonaffinity constant means precisely this c_*. For 1/2<=a<=1 and 0<e<=c_poly delta^2, the theorem includes the full bundle E.2 and loss at most exp(-delta t/32). All positive amplitudes up to the threshold are admitted. The convex mixture and Gaussian-energy normalization are both proved in E.11. The absolute regression bound is e^2 eta_*/4.

The proof uses actual Gaussian answer probes to identify affine responses, the weighted two-sector supersolution, and all current transpose terms. In particular the closure norm charges the active top backward defect by M^3 J_3^+, as displayed in E.1 and E.8. Deterministic diagonal coefficient arrays do not make random sample gates diagonal.

### E.1. Odd activation at the second-power separation scale

Within this proof unit, unqualified section and equation numbers are local.

#### 1. The theorem and explicit coefficient

Retain the precise finite model, initialization, raw metric, population
spaces and conclusions of
Fragment E.2. There are two deterministic
inputs with squared norm d, arbitrary binary labels, and three hidden
layers using the same activation. In particular, the initialized finite
readout is retained and raw GD is simultaneous raw Euler with step n^-2.

Define exactly the previous numerical constants
\[
 C_0=1296000\exp(1404),\qquad C_z=1500C_0,\qquad C_g=14400C_0,
\]
\[
 H=10^{30}(1+C_0+C_z+C_g+\exp(1410))^4,
 \qquad c_{\rm poly}=\min\{1/4,c_*,10^{-70}H^{-400}\}.       \tag{1}
\]
Here c_* is the explicit primal/nonaffinity constant displayed at the beginning of Fragment E. It is fixed before
choosing the data or any trajectory.

For every \(0<\delta\le1\), every such two-input dataset with
\[
 |\rho|=|\langle x_1,x_2\rangle/d|\le1-\delta,
\]
and all
\[
 \tfrac12\le a\le1,\qquad 0<e\le c_{\rm poly}\delta^2,
 \qquad \phi_{a,e}(z)=az+e\arctan z,                       \tag{2}
\]
the complete theorem E.2 holds. Consequently every
\[
 0<\theta_\delta\le c_{\rm poly}\delta^2,\qquad
 \phi_\delta(z)=(1-\theta_\delta)z+
                         \theta_\delta\arctan z           \tag{3}
\]
is admissible. The threshold includes every smaller positive amplitude.

The conclusions include one autonomous global strong population flow,
uniqueness against nonsymmetric bounded-primal strong competitors on
the same canonical action spaces, restart from every reached state,
and full-width-sequence joint GF/raw-GD convergence in probability on
every fixed finite physical interval. All original action orientations
and actual adjoints, all four full sample kernel matrices, prediction
and loss limits, same-layer preactivation/feature path and velocity
laws, second moments and integrated squared speeds are retained.
Activation-regression nonaffinity holds at every finite physical time;
the original initial hidden-block/sample/layer motion certificates hold.

The amplitude depends on delta alone. The width convergence is for each
fixed dataset and finite interval. Exponent two is sufficient; its
optimality and a practical-size prefactor are not established. The
three-input analysis is separate and does not assert the analogous
complete theorem.

#### 2. Exact scale and a weighted primal comparison

Fold labels by oddness and set
\[
 r=\sqrt{(1+y_1y_2\rho)/2},\quad \lambda=a^3r,
 \quad M=\left(\frac3{\sqrt2\lambda}\right)^{1/4}>1.
\]
The affine normalized clock is \(t=\lambda s\). Its first prediction
target 3/2 occurs at \(T<2\), with feature duration \(S=T/\lambda\).
The preceding affine proof gives
\[
 S\le M^4,\qquad r=\frac3{\sqrt2a^3}M^{-4},\qquad
 M\le24^{1/4}\delta^{-1/8}.                              \tag{4}
\]
Negative powers of r below use this exact intrinsic M, not a uniform
upper envelope substituted into an identity.

Let \(w(t)=\sqrt{1+\|D_0(t)\|^2}\). The fourth-power affine
propagator proof, including its radius-one tube, gives
\[
 G(t,u)\le\exp(2100)\frac{w(t)^3}{w(u)^3}.
\]
At a common raw state in that tube, the capped nonlinear field differs
from the affine field by at most \(Ce\,w(u)^3\) in feature time,
uniformly in cap. Duhamel's inequality in normalized time therefore
proves
\[
 E(t):=\|\Theta_e(t)-\Theta_0(t)\|_{\rm raw,sum}
 \le C\frac e\lambda w(t)^3\int_0^tdu
 \le H\frac e\lambda w(t)^3.                            \tag{5}
\]
This comparison differentiates only the affine field. Every primary
norm is bounded by a numerical multiple of w on the tube. The previous
restriction \(e\le c_*\delta^{7/4}\), which is implied by (2),
already closes the tube and supplies the endpoint/nonaffinity margins.
Thus (5) is a valid improvement on the actual capped program, before
any new source bootstrap closes. At the endpoint it is \(O(eM^7)\),
improving the earlier \(O(eM^{12})\) comparison. Deterministic Euler
approximation transfers the estimate to sufficiently fine fixed meshes.

Fragment E.9 proves the needed consequences of (5) in full.
For clarity, an important distinction is between the active and inactive
sample combinations. With \(P=(z_1+z_2)/2\), \(Q=(z_1-z_2)/2\),
oddness and the Lipschitz bound for arctangent give
\[
 \left|\frac{\arctan(P+Q)+\arctan(P-Q)}2\right|\le|P|.
\]
Consequently the active first and second feature discrepancies are
bounded by \(Ce\,w^3\) and \(Ce\,w^4\), while their affine norms
are bounded by \(Crw\) and \(Crw^2\). Their active learned-moment
strict-density errors are therefore bounded by
\[
 Ce\,r w^4\le Ce,\qquad Ce\,r w^6\le CeM^2.             \tag{6}
\]
The inactive forward errors have larger bounds but only need a fixed
strict-density margin in the coefficient comparison.

The actual raw L2 incoming-field bounds remain
\[
 \|q^1\|_2\le HM^3,\qquad
 \|q^2\|_2\le HM^2,\qquad \|C\|_2\le HM.
\]
The inactive backward fields are smaller: their top and middle norms
are \(O(eM)\) and \(O(eM^2)\). The common readout makes the top
contrast purely nonlinear; applying the actual bounded adjoint and
then the next capped gate gives the middle contrast bound. These
facts concern actual source output laws, not a formal affine covariance
comparison.

#### 3. Weighted affine kernels and a source box with distinct sectors

Fragment E.8 proves the following exact deterministic
interface. It uses the existing independent-root source probes, with
injection costs evaluated at their own source time and output costs at
the terminal time. In normalized active coordinates, strict densities
obey
\[
 F(t,u),T(t,u)\le C\frac{w(t)^3}{w(u)^3},\qquad
 V(t,u),W(t,u)\le C\frac{w(t)^4}{w(u)^2}.
\]
All current resolvent identities remain present. The affine B3 also
contains its learned-moment term \(Cw(t)w(u)\), which is retained
when multiplying kernels.

The radial estimates imply
\[
 \int w\le C,\qquad \int_0^t w^2\le C\log(\mathrm e w(t)),
 \qquad\int_0^t w^4\le Cw(t)^2,
 \qquad\int_u^T w^{-2}\le Cw(u)^{-4}.
\]
The exact identities \(FL=F+FB_3V\) and \(RF=F+VB_3F\), followed
by these weighted integrals, give
\[
 (FL)(t,u)\le C\frac{w(t)^3}{w(u)^2},\qquad
 (RF)(t,u)\le C\frac{w(t)^4}{w(u)^3}.                  \tag{7}
\]
This avoids the much larger estimate obtained by multiplying uniform
endpoint bounds. Every inequality holds on sufficiently fine positive
meshes, with no minimum-step assumption.

At the same outer beta reference as before, use active backward excess
radius \(H^{-100}M^3\) and inactive radius \(H^{-100}M^{-4}\).
Active forward coefficients are bounded by that affine beta reference;
inactive forward coefficients have their baseline plus density one.
The normalized active backward excess has size \(O(rH^{-100}M^3)\).
Weighted Neumann ratios cost at most this quantity times
\(C\log(\mathrm e30M)\), so they stay uniformly small. The inactive
integration row costs \(M^4\) and is controlled by its separate
radius. Thus this larger box retains the precise forward and backward
transfer bounds needed for the source proof.

Let \(E_2^\pm,E_3^\pm\) bound the two signed forward coefficient
defects in strict density, and \(J_2^\pm,J_3^\pm\) the two backward
defects in complete causal row norm, including current diagonals.
The supersolution companion proves the sufficient criterion
\[
 \begin{split}
 \mathcal D={}&M^{10}(E_2^++E_3^+)+M J_2^++M^3J_3^+\\
 &+E_2^-+E_3^-+M^4(J_2^-+J_3^-)
 \le H^{-200}.                                          \tag{8}
 \end{split}
\]
It uses exactly the previous positive beta supersolution, reconstructing
backward coefficients by \(W^*-W=a^2LJ_3R^*\). Causal weights in
(7) control the two strict factors around an arbitrary backward row
error. The \(VJ_3V\) term is also retained; it is why (8) charges
\(M^3J_3^+\). Signed coefficients are handled by the positive
finite chronological map, rather than assuming positivity of the
actual nonlinear blocks. The comparison gives strict interior margins
in both sectors.

#### 4. Source response with all random sample mixing retained

Fragment E.9 supplies the complete source calculation on that box.
All deterministic coefficient blocks are sector diagonal by the
existing exchange-equivariance induction. Individual random gates mix
the sectors. A scalar enlarged gain is not substituted for those gates.

First, the actual source covariance bounds from Section 2 give inactive
reverse Gaussian scales \(CeM^2,CeM\), and active forward Gaussian
scales \(CM^{-3},CM^{-2}\). The latter follow from (5), the r factors
in the affine active fields, and the sufficient condition
\(eH^{200}M^{16}\le1\). Solving the exact same-array value equations
then gives incoming subGaussian exponents
\[
 q^1:\ M^{10},\qquad q^2:\ M^9,\qquad C:\ M^7.           \tag{9}
\]
These are uniform individual-time norms, not a norm of a random time
supremum. The source derivative exponential consequently requires only
\(eCM^{14}\) small. The numerical condition used below is stronger.

For each local source population, with \(U=(I-a^2KB)^{-1}K\) and
\(L=(I-a^2BK)^{-1}\), the exact derivative identities are
\[
 J-J_{\rm aff}=U[\Delta V I^\zeta+PJ],\qquad
 D\delta-D\delta_{\rm aff}=L[\Delta V I^\zeta+PJ],
\]
\[
 P=L_{\rm gate}+a\Delta V B+aB\Delta G+\Delta V B\Delta G.
                                                               \tag{10}
\]
The gate perturbations are bounded by \(Ce\), and the curvature
term by \(CeQ\). The fixed coefficient arrays and covariances are
frozen in every named-source derivative, as in the original source
construction.

The calculation separates diagonal paths from paths that leave a
sector and return. A sector change introduces a perturbative gate;
a return introduces a second one. Weighted affine kernels bound the
diagonal terms. The off-diagonal terms are estimated with their two
e factors and the already controlled exponential moments. No current
backward factor or terminal feature gate is discarded. Raw L2 bounds
are used after the exponential has been controlled; higher source
moments are used where two unbounded multipliers occur.

The complete sufficient forcing table, including learned moments, is
\[
\begin{array}{c|cc}
 & + & -\\ \hline
 E_2 & H^{200}eM^3 & H^{200}eM^{13}\\
 E_3 & H^{200}eM^5 & H^{200}eM^{11}\\
 J_2 & H^{200}eM^{15} & H^{200}eM^3\\
 J_3 & H^{200}eM^{12} & H^{200}eM
\end{array}                                                   \tag{11}
\]
under \(eH^{200}M^{16}\le1\). Backward row estimates mean
\(\max_k E[\sum_{j\le k}|\text{defect}_{kj}|]\), with the
terminal-time maximum outside expectation. This quantity controls the
row norm of the deterministic expected coefficients.

The companion checks every value, derivative, covariance and numerical
factor. In particular the bounded gate perturbations involving B in
(10) remain present, and the inactive learned backward moments begin
quadratically in e because their affine fields vanish.

#### 5. Numerical closure and the complete theorem

By (4),
\[
 M^{16}\le24^4\delta^{-2}.
\]
The unchanged choice (1)--(2) therefore gives
\[
 eM^{16}\le10^{-70}24^4H^{-400},\qquad
 eH^{200}M^{16}\le10^{-70}24^4H^{-200}<1.             \tag{12}
\]
Combining (8) and (11), every term in \(\mathcal D\) is at most
\(H^{200}eM^{16}\). There are eight terms, so
\[
 \mathcal D\le8H^{200}eM^{16}
 \le8\cdot24^4\cdot10^{-70}H^{-200}<H^{-200}.          \tag{13}
\]
The actual largest exponent is 16, from the active middle-backward
term; the active second-forward and top-backward terms cost 15.
It is useful here to retain the numerical factor \(24^4\), rather
than replace it by H and unnecessarily spend another power of H.

At fixed cap and sufficiently fine fixed mesh, continue the actual
source program continuously in amplitude from zero to e. At a proposed
first exit from the box, (11)--(13) apply, and the positive supersolution
puts all inequalities strictly inside. This contradiction closes the
source construction uniformly in cap and mesh.

The remaining original bridges now have their required inputs: bounded
primal feature paths through their endpoint, uniform incoming-field
subGaussian tails, and endpoint prediction at least 5/4. Asymmetric cap
comparison constructs the uncut autonomous strong feature flow; its
first-hit clock constructs one global physical population flow. The
physical comparison retains both actual residuals and proves
nonsymmetric bounded-primal uniqueness and restart from reached states.
No reference exponent-four response threshold is imposed after replacing its
source proof by the present one.

At fixed cap/auxiliary mesh, the original Gaussian conditioning,
singular-query, common-action and adjunction arguments apply to the
same model. Width is taken first; deterministic Euler estimates remove
the auxiliary mesh; asymmetric comparison removes the cap. The actual
finite Gaussian readout is retained. Raw GD has its original
\(C_{R,T}n^{-2}\) reference error. No growing-transcript Gaussian law
or cross-width trained operator-norm convergence is invoked.

The original velocity bridge retains product-query truncation and the
order of cap removal at fixed reference-velocity truncation, then
truncation removal. The uncut velocity has a compact continuous L2 time
image. This gives the original velocity/path laws, second moments and
integrated speeds, together with all kernels and both action
orientations. The reference absolute regression margin and initial-motion
proof require no further amplitude restriction. The normalization
\((z+r_0\arctan z)/\|G+r_0\arctan G\|_2\) also remains covered for
\(0<r_0\le c_{\rm poly}\delta^2\), since its gain lies in [1/2,1]
and its nonlinear coefficient is at most r_0.

### E.2. Exact odd finite model and complete observable bundle

Within this proof unit, unqualified section and equation numbers are local.

Here e_delta means c_poly delta^2, phi(z)=az+e arctan(z), and the initialization is retained by both algorithms.

Here are the finite model and metric. At width \(n\), initialize all
entries independently:
\[
 W^1_{ij}\sim N(0,1/d),\quad W^2_{ij},W^3_{ij}\sim N(0,1/n),
 \quad C_i\sim N(0,n^{-2}),
\]
where \(W^1\in\mathbb R^{n\times d}\), \(W^2,W^3\in\mathbb R^{n\times n}\).
With \(\frac{( u)^\top(v)}{n}=u^Tv/n\), define
\[
 z_i^1=W^1x_i,\quad h_i^\ell=\phi_{a,e}(z_i^\ell),\quad
 z_i^2=W^2h_i^1,\quad z_i^3=W^3h_i^2,\quad
 f_i=\frac{( C)^\top(h_i^3)}{n},\quad r_i=f_i-y_i.
\]
All products between neuron vectors in a layer are coordinatewise. Put
\[
 b_i^3=C\phi'(z_i^3),\quad
 b_i^2=\phi'(z_i^2)(W^3)^Tb_i^3,\quad
 b_i^1=\phi'(z_i^1)(W^2)^Tb_i^2.
\]
The loss \(\mathcal L=\frac12\sum_i r_i^2\) uses the raw metric
\[
 \|d\Theta\|_{\rm raw}^2
 =\frac dn\|dW^1\|_F^2+\|dW^2\|_F^2+\|dW^3\|_F^2+\frac{\|dC\|_2^2}{n}.
\]
Thus its exact gradient flow is
\[
 \dot W^1=-\frac1d\sum_i r_i b_i^1x_i^T,\quad
 \dot W^\ell=-\frac1n\sum_i r_i b_i^\ell(h_i^{\ell-1})^T
 \quad(\ell=2,3),\quad \dot C=-\sum_i r_i h_i^3.           \tag{5}
\]
Raw GD is simultaneous Euler for (5) at step \(\eta_n=n^{-2}\).
Interpolate raw parameters linearly at times \(k\eta_n\); recompute
hidden fields from this interpolation. At nodes use right hidden
derivatives and at a terminal endpoint use left derivatives. Retain
the initialized finite random readout throughout both algorithms.

The conclusions are as follows.

1. One autonomous, uncut, strong \(C^1\) population flow exists for all
   \(t\ge0\) on the canonical generated Gaussian action spaces. Its
   bounded-primal strong solution is unique on these spaces, including
   against nonsymmetric competitors, and has unique continuation from
   each reached state.
2. On every fixed finite physical interval, GF and raw GD converge
   jointly in probability along the full width sequence to this flow,
   with all observables and topologies in Section 2.
3. At every finite physical time every sample and hidden layer has
   strictly positive best affine activation-regression error. Every
   hidden parameter block and every sample's preactivation and feature
   in every hidden layer has nonzero initial physical acceleration.
   The projected total kernel changes near zero. These are initial
   feature-learning claims, not perpetual nonzero velocity claims.

The constants selecting \(a,e\) are independent of angle, labels,
dimension, width, caps, meshes and physical horizon. Each convergence
assertion concerns a fixed dataset and fixed \(T<\infty\); it is not a
supremum over datasets or convergence uniformly over the whole half-line.

#### 2. Population objects and observable scope

There are three separate canonical neuron spaces
\(H_\ell=L^2(\Omega_\ell,\mu_\ell)\). The state is
\[
 w\in L^2(\Omega_1;\mathbb R^d),\quad A:H_1\to H_2,
 \quad B:H_2\to H_3,\quad C\in H_3,
\]
with bounded actions, their actual adjoints, and Hilbert--Schmidt learned
increments. For \(u\in H_j,v\in H_i\),
\((u\otimes v)q=u\langle v,q\rangle_i\). Replace the normalized sums,
transposes and outer products in the finite equations by these inner
products, adjoints and rank-one actions. The metric on increments is
\(d\|dw\|_2^2+\|dA\|_{\rm HS}^2+\|dB\|_{\rm HS}^2+\|dC\|_2^2\).
The canonical initial actions have norms at most 10, \(C(0)=0\), and
the initial first projected pair has covariance
\(\Gamma=\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)\).
These are the constructed initialization law, not new hypotheses on
the finite model.

All four raw kernel matrices, including their off-diagonal entries, are
\[
 K^1_{ij}=\Gamma_{ij}\langle b_i^1,b_j^1\rangle_1,\quad
 K^2_{ij}=\langle b_i^2,b_j^2\rangle_2\langle h_i^1,h_j^1\rangle_1,
\]
\[
 K^3_{ij}=\langle b_i^3,b_j^3\rangle_3\langle h_i^2,h_j^2\rangle_2,
 \qquad K^4_{ij}=\langle h_i^3,h_j^3\rangle_3.             \tag{6}
\]
They and the predictions/loss converge uniformly on \([0,T]\).
For each layer, the empirical joint two-sample preactivation/feature
path law converges in \(\mathcal W_2(C([0,T];\mathbb R^4))\), with the
supremum norm. The joint same-layer law including recomputed
preactivation/feature velocities converges in \(\mathcal W_2\) uniformly
in time, and jointly for each fixed finite collection of times. Second
moments and integrated squared speeds converge. Both orientations of
initialized and trained actions on their canonical generated probes
are retained. Strong comparisons of learned increments use common
spaces. No cross-layer neuron pairing, continuous-path velocity law,
or cross-width operator-norm identification is asserted.


### E.3. Odd symmetry, affine active core and frozen inactive fields

Within this proof unit, unqualified section and equation numbers are local.

Fix \(0<\delta\le1\), \(\|x_1\|^2=\|x_2\|^2=d\), and
\(|\rho|\le1-\delta\), where \(\rho=x_1^Tx_2/d\). Write
\(y_1=\sigma,y_2=\sigma\tau\), with \(\sigma,\tau\in\{-1,1\}\).
All raw metrics, initialization laws, forward actions, and backward
adjoints have the normalizations in the supplied two-sample theorem.
The population readout initially vanishes; the finite raw model's
small random readout is retained.

#### 1. Exact label folding and population scalar reduction

Every odd differentiable activation has even derivative. At any parameter
state, induction through the forward and backward equations gives
\[
z^\ell(-x)=-z^\ell(x),\quad h^\ell(-x)=-h^\ell(x),\quad
f(-x)=-f(x),\quad b^\ell(-x)=b^\ell(x).
\]
Replace the dataset by
\(\widetilde x_j=y_jx_j,\widetilde y_j=1\). Then
\(\widetilde h_j^\ell=y_jh_j^\ell\),
\(\widetilde f_j=y_jf_j\),
\(\widetilde r_j=y_jr_j\), and
\(\widetilde b_j^\ell=b_j^\ell\). Consequently
\[
\widetilde r_j\widetilde b_j^1\widetilde x_j^T
=r_jb_j^1x_j^T,\qquad
\widetilde r_j\widetilde b_j^\ell
(\widetilde h_j^{\ell-1})^T=r_jb_j^\ell(h_j^{\ell-1})^T,\qquad
\widetilde r_j\widetilde h_j^3=r_jh_j^3.
\]
Thus finite raw GF and simultaneous raw Euler/GD have exactly the same
parameter trajectory after label folding, including the original finite
readout. The folded correlation is \(\widetilde\rho=\tau\rho\).

Let \(R\) be the orthogonal reflection exchanging the folded inputs:
\[
v=\widetilde x_1-\widetilde x_2,\qquad
R=I-2vv^T/\|v\|^2.
\]
The angle condition ensures \(v\ne0\). Acting by \(R\) on the first
weight field exchanges both folded samples through all hidden layers.
The scalar objective
\[
g(\Theta)=\tfrac12\sum_j y_j f_j
         =\tfrac12\sum_j\widetilde f_j
\]
and physical loss are invariant. The reflection is an isometry of the
raw metric, so both gradient vector fields are equivariant. Identical
sample clips and odd clips on sign-changing slots preserve this fact
at fixed-cap finite Euler level. Gaussian initialization is invariant.

The limiting fixed-program predictions are deterministic contractions.
Since their approximating laws are sample-exchange invariant, those
deterministic predictions must be invariant:
\(\widetilde f_1=\widetilde f_2=g\). Explicitly, an exchange-invariant
random pair converging in probability to a deterministic pair forces
that pair to equal its exchange. Canonical population action spaces
closed under the paired queries realize the invariance by
measure-preserving involutions. Euler induction and strong limits
preserve it exactly on the constructed path, as in the supplied symmetry
proof. This uses no uniqueness of an unconstructed uncut flow.

Undoing the fold gives \(f_j=y_jg\) and \(\mathcal L=(1-g)^2\)
for both uncut and capped constructed paths. For the uncut gradient
fields it yields
\[
f_j=y_jg,\qquad \mathcal L=(1-g)^2,\qquad
\dot\Theta=2(1-g)\nabla g.
\]
The feature equation is \(\Theta'=\nabla g\), with
\(ds/dt=2(1-g)\) and \(g'=y^TKy/4\). A finite realization generally
does not satisfy this population scalar prediction identity.
For a cap, the feature equation is instead \(\Theta'=V_R\) and the
physical equation is \(\dot\Theta=2(1-g)V_R\); the scalar clock is the
same but the gradient and kernel-derivative identities are not asserted.

#### 2. Initial kernels for the odd family

Let \(q_0=1,c_0=\rho\), and let \(q_\ell,c_\ell\) be the initial
diagonal and off-diagonal feature second moments. Gaussian propagation
gives a centered preactivation pair \((U,V)\) with diagonal
\(q_{\ell-1}\) and covariance \(c_{\ell-1}\). Oddness gives
\[
q_\ell\pm c_\ell
=\tfrac12\mathbb E[(\phi_{a,e}(U)\pm\phi_{a,e}(V))^2].
\]
Since \(\phi_{a,e}'\ge a\),
\[
|\phi_{a,e}(u)-\phi_{a,e}(v)|\ge a|u-v|,\qquad
|\phi_{a,e}(u)+\phi_{a,e}(v)|\ge a|u+v|,
\]
the second inequality following by replacing \(v\) by \(-v\).
Therefore
\[
q_\ell\pm c_\ell\ge a^2(q_{\ell-1}\pm c_{\ell-1}),\qquad
q_3\pm c_3\ge a^6(1\pm\rho)>0.
\]
All hidden kernel blocks initially vanish because \(C(0)=0\). Hence
\[
\kappa_{a,e}(0)=\tfrac14y^TK^4(0)y
=\frac{q_3+\tau c_3}{2}
\ge a^6\frac{1+\tau\rho}{2}\ge\frac{\delta}{128}. \tag{1}
\]
The two strict moment eigenvalues also verify nonsingularity of every
initial preactivation pair. For \(e=0\) these recursions are exact:
\[
q_\ell=a^{2\ell},\qquad c_\ell=a^{2\ell}\rho,\qquad
\kappa_{a,0}(0)=a^6(1+\tau\rho)/2. \tag{2}
\]
Equal labels activate \(a^6(1+\rho)\); opposite labels activate
\(a^6(1-\rho)\). The absolute-angle condition treats both without an
offset: at antipodal inputs an odd network cannot fit equal nonzero
labels, and at identical inputs it cannot fit opposite labels.

#### 3. Affine active and inactive equations

Define
\[
u=(x_1+\tau x_2)/2,\quad v=(x_1-\tau x_2)/2,\quad
v_u=(1+\tau\rho)/2,\quad v_v=(1-\tau\rho)/2.
\]
Then \(u\cdot v=0\), \(\|u\|^2/d=v_u\),
\(\|v\|^2/d=v_v\), and \(v_u,v_v\ge\delta/2\).
For the affine activation \(az\), put
\[
P_\ell=(z_1^\ell+\tau z_2^\ell)/2,\qquad
Q_\ell=(z_1^\ell-\tau z_2^\ell)/2.
\]
Their forward identities are
\[
P_1=w\cdot u,\ Q_1=w\cdot v,\quad
P_2=aAP_1,\ Q_2=aAQ_1,\quad
P_3=aBP_2,\ Q_3=aBQ_2. \tag{3}
\]
Thus \(H=\frac12\sum_j y_jh_j^3=\sigma aP_3\) and
\(g=\sigma a^3\langle C,BAP_1\rangle\). Taking its gradient in the
raw metric gives exactly
\[
\begin{aligned}
C'&=\sigma aP_3,\\
B'&=\sigma a^2C\otimes P_2=\sigma a^3C\otimes(AP_1),\\
A'&=\sigma a^3B^*C\otimes P_1,\\
P_1'&=\sigma v_u a^3A^*B^*C,\qquad Q_1'=0.
\end{aligned} \tag{4}
\]
Indeed \(w'=(\sigma a^3/d)(A^*B^*C)u\); contraction with \(u\)
produces \(v_u\), and contraction with \(v\) vanishes. These equations
depend only on \((P_1,A,B,C)\), never on the inactive root \(Q_1(0)\).

Both label sectors are explicit:

* If \(y_1=y_2\), \(P_\ell\) is the common field and \(Q_\ell\) the
  contrast; \(v_u=(1+\rho)/2,v_v=(1-\rho)/2\).
* If \(y_1=-y_2\), \(P_\ell\) is the contrast and \(Q_\ell\) the common
  field; \(v_u=(1-\rho)/2,v_v=(1+\rho)/2\).

#### 4. Uniform affine interval through \(g=3/2\)

The affine objective is a continuous polynomial on the affine raw
Hilbert space. Its gradient is locally Lipschitz, with bounded
derivatives on bounded balls uniformly for \(a\in[1/2,1]\).
Picard contraction on such a ball supplies strong local existence and
uniqueness, including at every finite reached state.

Write the hidden state as \(\vartheta\), and \(J_s\) for the bounded
linearization of \(H\). The gradient equations are
\(C'=H,\vartheta'=J_s^*C\), and the strong chain rule gives
\[
C''=J_sJ_s^*C,\qquad \langle C,C''\rangle=\|J_s^*C\|^2\ge0,
\qquad g'=\|C'\|^2+\|J_s^*C\|^2=\|\Theta'\|_{\rm raw}^2.
\]
Twice differentiating \((\|C\|^2+\epsilon^2)^{1/2}\), using
Cauchy--Schwarz and \(\langle C,C''\rangle\ge0\), proves convexity.
Letting \(\epsilon\downarrow0\) gives convexity of \(\|C\|\).
Its initial right slope is \(\|H(0)\|\), because
\(C(0)=0,C'(0)=H(0)\). Thus \(\|C'(s)\|\ge\|H(0)\|\) and
\[
g'\ge\kappa_0,\qquad
\int_0^s\|\Theta'(r)\|_{\rm raw}^2\,dr=g(s),\qquad
\kappa_0=a^6v_u\ge\delta/128. \tag{5}
\]

The first hit \(S\) of \(g=3/2\) exists. Before that hit,
\(s\le3/(2\kappa_0)\), and the energy is at most \(3/2\).
A finite maximal endpoint below the target has a strong limit since
\[
\|\Theta(v)-\Theta(u)\|_{\rm raw}
\le\sqrt{(v-u)[g(v)-g(u)]}\le\sqrt{\tfrac32(v-u)}.
\]
Local existence at that reached state extends the branch. An
arbitrarily long branch below the target contradicts \(g(s)\ge\kappa_0s\).
Cauchy--Schwarz then gives, on the entire closed interval \([0,S]\),
\[
S\le S_\delta:=192/\delta,\qquad
\|\Theta(s)-\Theta(0)\|_{\rm raw}
\le\frac3{2\sqrt{\kappa_0}}
\le R_\delta:=12\sqrt2/\sqrt\delta. \tag{6}
\]
Set
\[
U=11+R_\delta. \tag{7}
\]
Initial first-layer projected norms are one, action norms are at most
ten, and the readout vanishes. Raw displacement controls each projected
change by \(\|\Delta w\cdot x_j\|_2\le\sqrt d\|\Delta w\|_2\),
and operator changes by Hilbert--Schmidt norms. Consequently
\[
\max_j\|z_j^1(s)\|_2,\ \|A(s)\|_{\rm op},\
\|B(s)\|_{\rm op},\ \|C(s)\|_2\le U. \tag{8}
\]
The full initial \(\sqrt d\|w_0\|_2\) need not be dimension-independent;
only its projections and raw displacement enter these constants.
Each reference path stops at its own hit \(S\), never being extended
to the uniform duration upper bound \(S_\delta\).

#### 5. Active lower bounds and frozen inactive Gaussian fields

Since \(C'=\sigma aP_3\), the radial bound implies
\(a^2\|P_3\|^2\ge a^6v_u\). Using (3) and (8) backwards gives
\[
\|P_3\|^2\ge a^4v_u,\qquad
\|P_2\|^2\ge a^2v_u/U^2,\qquad
\|P_1\|^2\ge v_u/U^4. \tag{9}
\]
Every active hidden field therefore remains nonzero.

A stronger variance bound comes from exact population freezing of the
inactive fields. This requires independence, not merely bounded learned
Hilbert--Schmidt increments. In a fixed finite affine scalar-Euler
prefix with zero initial readout, let
\(\mathscr F_n=\sigma(P_{1,0},A_0,B_0)\). Equations (4) make all
active training fields \(\mathscr F_n\)-measurable. Orthogonality of the
Gaussian input projections makes \(Q_0=Q_{1,0}\) an independent
\(N(0,v_vI_n)\) vector. For an \(\mathscr F_n\)-measurable matrix \(T_n\),
\[
\mathbb E[\frac{\|T_nQ_0\|_2^2}{n}\mid\mathscr F_n]
=\frac{v_v}{n}\|T_n\|_F^2. \tag{10}
\]
On bounded-initial-operator events, each fixed Euler prefix has bounded
field norms and ordinary Frobenius norms of its learned increments.
The normalization is
\(\|\Delta s\,p q^T/n\|_F=\Delta s\frac{\|p\|_2}{\sqrt n}\frac{\|q\|_2}{\sqrt n}\). Moreover
\[
\|B_sA_s-B_0A_0\|_F
\le\|B_s-B_0\|_F\|A_s\|_{\rm op}
+\|B_0\|_{\rm op}\|A_s-A_0\|_F.
\]
Apply (10) to \(A_s-A_0\) and \(B_sA_s-B_0A_0\).
Their normalized actions on \(Q_0\) tend to zero in probability.
The deterministic joint fixed-program limit therefore gives exact
Hilbert-space identities at population Euler nodes:
\[
Q_1(s)=Q_0,\qquad Q_2(s)=aA_0Q_0,\qquad
Q_3(s)=a^2B_0A_0Q_0. \tag{11}
\]
Strong bounded-interval Euler convergence for the affine polynomial
field preserves (11) at every \(s\in[0,S]\). Initial Gaussian matrix
propagation then gives
\[
Q_\ell(s)\sim N(0,a^{2(\ell-1)}v_v). \tag{12}
\]

For \(\mathscr F_n\)-measurable \(p_n,T_n\), conditional Gaussianity gives
\[
\mathbb E[\frac{( p_n)^\top(T_nQ_0)}{n}\mid\mathscr F_n]=0,\qquad
\mathbb E[\frac{( p_n)^\top(T_nQ_0)}{n}^2\mid\mathscr F_n]
\le\frac{v_v}{n}\|T_n\|_{\rm op}^2\frac{\|p_n\|_2^2}{n}. \tag{13}
\]
Use \(T_n=I,aA_s,a^2B_sA_s\) and \(p_n=P_\ell(s)\), and also
\(p_n=\mathbf1\). Fixed-program convergence and then strong affine
Euler convergence give
\[
\mathbb E Q_\ell(s)=0,\qquad
\mathbb E[P_\ell(s)Q_\ell(s)]=0. \tag{14}
\]
As \(z_1^\ell=P_\ell+Q_\ell\) and
\(z_2^\ell=\tau(P_\ell-Q_\ell)\), one obtains
\[
\operatorname{Var}(z_j^\ell(s))
=\operatorname{Var}(P_\ell(s))+a^{2(\ell-1)}v_v
\ge\delta/32,\qquad j=1,2. \tag{15}
\]
Here \(a^4\ge1/16\) and \(v_v\ge\delta/2\). The frozen field is the
contrast for equal labels and the common field for opposite labels.

All affine preactivations are Gaussian, not merely of positive
variance. In a finite affine population Euler prefix, every forward,
reverse, and evolving field is linear in finitely many joint Gaussian
source coordinates in its layer. Inductively, the gate \(a\) is
constant, the activation is linear, unrolled rank-one memories multiply
previous fields only by deterministic scalar contractions, and each
new initialized matrix call is a Gaussian innovation plus linear
Gaussian-conditioning response terms. No product of varying neuron
coordinates occurs outside a scalar contraction. Strong Euler
convergence passes their means, covariances, and Gaussian
characteristic functions to the exact affine path.

Their means vanish: changing \(P_{1,0}\) to its negative sends
\(P_\ell,C\) to their negatives and leaves \(A,B\) fixed in (4).
The invariant initialization and deterministic limiting laws force
zero active means; (14) supplies zero inactive means. Finally,
\[
\|z_j^1\|_2\le U,\qquad
\|z_j^2\|_2\le aU^2\le U^2,\qquad
\|z_j^3\|_2\le a^2U^3\le U^3. \tag{16}
\]
Thus every affine marginal has form \(\nu G\), \(G\sim N(0,1)\), with
\[
m:=\sqrt{\delta/32}\le\nu\le L:=U^3. \tag{17}
\]

#### 6. Uniform Gaussian nonaffinity and perturbative transfer

For a square-integrable real variable \(Z\) with positive variance, put
\[
\mathcal R(Z)=\inf_{\alpha,\beta}\mathbb E[(
\arctan Z-\alpha-\beta Z)^2]
=\operatorname{Var}(\arctan Z)
-\frac{\operatorname{Cov}(Z,\arctan Z)^2}{\operatorname{Var}(Z)}.
\]
Define a constant depending only on \(\delta\):
\[
\eta_\delta=\min_{m\le\nu\le L}\mathcal R(\nu G)>0. \tag{18}
\]
Coupling by the same \(G\), boundedness and Lipschitzness of arctangent,
and the denominator bound \(m^2\) show continuity on this compact
interval. Zero residual would identify arctangent with an affine
function Gaussian-almost everywhere. Positive density and continuity
would then extend the identity to all of \(\mathbb R\), contradicting
the nonconstant derivative. Thus the minimum is positive and
\[
\inf_{a\in[1/2,1]}\ \inf_{j,\ell,s\le S}
\mathcal R(z_{j,a,0}^\ell(s))\ge\eta_\delta. \tag{19}
\]
The endpoint \(S\) in each term is that affine reference's own endpoint.

The transfer estimate needs no Gaussianity of the perturbed variable.
Suppose \(\|Z-Z_0\|_2\le t\),
\(\operatorname{sd}(Z_0)\ge m\), and
\(\mathcal R(Z_0)\ge\eta_\delta\). Then
\[
t\le t_\delta:=
\min\left\{m/2,\frac{\sqrt{\eta_\delta}}{2(1+\pi/m)}\right\}
\quad\Longrightarrow\quad \mathcal R(Z)\ge\eta_\delta/4. \tag{20}
\]
Indeed centering is an orthogonal projection, so standard deviation is
1-Lipschitz and \(\operatorname{sd}(Z)\ge m/2\). The optimal slope for
regressing \(\arctan Z\) on \(Z\) has absolute value at most
\(\operatorname{sd}(\arctan Z)/\operatorname{sd}(Z)\le\pi/m\).
Using its intercept and slope as a competitor for \(Z_0\) gives
\[
\sqrt{\mathcal R(Z_0)}
\le\sqrt{\mathcal R(Z)}+(1+\pi/m)t,
\]
proving (20). Absorbing \(aZ\) into the free affine approximant gives
the exact identity
\[
\inf_{\alpha,\beta}\mathbb E[(
\phi_{a,e}(Z)-\alpha-\beta Z)^2]=e^2\mathcal R(Z). \tag{21}
\]
Consequently a separately proved comparison
\(\|z_{j,a,e}^\ell-z_{j,a,0}^\ell\|_2\le Je\), uniform on these
reference intervals with \(J\) depending only on \(\delta\), gives
the uniform positive activation-regression margin
\(e^2\eta_\delta/4\) whenever \(0<e\le t_\delta/J\).
The constants in (6), (7), (17), (18), and (20) precede the slope,
dataset, labels, dimension, width, and physical horizon.

#### 7. Range variants and the physical clock

The same core proof works for \(a\in[1/2,2]\).
The lower kernel bound, \(S_\delta,R_\delta,U\), and variance lower
bound remain unchanged; replace \(L=U^3\) by \(L=4U^3\).
Separate response estimates must use upper gate bound two.

The convex mixture \(\psi_\lambda=(1-\lambda)z+\lambda\arctan z\),
\(0<\lambda\le1/2\), is covered by
\(a=1-\lambda\in[1/2,1]\), \(e=\lambda\). For its Gaussian
energy-normalized version, put
\(N_\lambda=\|\psi_\lambda(G)\|_2\). Since
\(|\psi_\lambda(z)|\le|z|\), one has \(N_\lambda\le1\).
The nonnegative cross term in its squared norm gives
\(N_\lambda\ge1-\lambda\). Consequently
\[
\frac{1-\lambda}{N_\lambda}\in[1/2,1],\qquad
\frac\lambda{N_\lambda}\le2\lambda.
\]
Thus \(\psi_\lambda/N_\lambda\) belongs to the same broad family,
and choosing \(\lambda\le\min\{1/2,e_\delta/2\}\) satisfies any
separately obtained coefficient threshold \(e_\delta\). Both
coefficients are positive and no activation offset occurs.

If the separate nonlinear construction provides a strong feature path
through \(S\) with \(g(S)>1\), (1) and radial coercivity give \(g'>0\)
and a first hit \(s_*<S\) of one. The compact path has bounded continuous
kernel, say \(g'\le M\), and hence
\(1-g(s)=\int_s^{s_*}g'(r)\,dr\le M(s_*-s)\). Therefore
\[
t(s)=\int_0^s\frac{dr}{2[1-g(r)]}\longrightarrow\infty
\quad(s\uparrow s_*).
\]
Its inverse gives the exact population loss flow for every physical
time, while staying inside the constructed feature interval.
This implication is conditional on the uncut nonlinear construction;
it does not replace response control, cap removal, uniqueness, or
finite GF/GD observable arguments.

### E.4. Polynomial affine bounds and absolute regression margin

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Exact normalization of the active affine problem

Use the notation of Fragment E.3: `v=v_u=(1+tau_label rho)/2`,
`r=sqrt(v)`, `P_1=w dot u`, and `sigma=y_1`. Define

\[
 p=P_1/r,\qquad D=\sigma C,\qquad
 \lambda=a^3r,\qquad t=\lambda s,
 \qquad F=\langle D,BAp\rangle.
\]

Here `s` is the original feature time and `t` is only an auxiliary time in this
note. In particular `g=lambda F`, and

\[
 \frac{\sqrt\delta}{8\sqrt2}\le\lambda\le1.
\]

The first raw metric on active increments becomes exactly `||dp||_2^2`:
`d ||dw||_2^2 = ||dP_1||_2^2/v = ||dp||_2^2` for increments parallel to `u`.
All first-layer directions perpendicular to `u` are constant in the affine
flow. In normalized time its four equations are exactly

\[
 \dot p=A^*B^*D,\quad
 \dot A=B^*D\otimes p,\quad
 \dot B=D\otimes Ap,\quad
 \dot D=BAp.                                                   \tag{1}
\]

The four component spaces carry the `L2`, HS, HS, `L2` metrics. The canonical
initialization has

\[
 \|p_0\|=1,\quad \|A_0\|,\|B_0\|\le10,\quad D_0=0,
 \quad\|B_0A_0p_0\|=1.                                       \tag{2}
\]

The last equality is the initial Gaussian forward norm identity already in
the existing affine proof. No finite random readout is reset: (1) describes
the zero population limit of that readout, as in the original construction.

#### 2. Exact balance identities and their consequences

Put `c=||D||`. Differentiating bounded-operator identities in (1) gives

\[
 BB^*-D\otimes D=B_0B_0^*,
\]
\[
 AA^*-B^*B=A_0A_0^*-B_0^*B_0,
\]
\[
 A^*A-p\otimes p=A_0^*A_0-p_0\otimes p_0.                    \tag{3}
\]

There are no traces of infinite-dimensional identity operators in this
argument. Scalar differentiation also gives

\[
 \|p\|^2=1+c^2,\qquad \frac d{dt}c^2=2F.                    \tag{4}
\]

The first two balances imply

\[
 \|B\|^2\le100+c^2,\qquad \|A\|^2\le200+c^2.              \tag{5}
\]

The first and third balances, using positivity of the initialized Gram
operators and `||p_0||=1`, give the more useful lower bounds

\[
 \|B^*D\|^2=c^4+\langle D,B_0B_0^*D\rangle\ge c^4,
\]
\[
 \|Ap\|^2=\|p\|^4+\langle p,(A_0^*A_0-p_0\otimes p_0)p\rangle
 \ge\|p\|^4-\|p\|^2=c^2(1+c^2).                            \tag{6}
\]

Because (1) is gradient ascent for `F`,

\[
 \dot F=\|BAp\|^2+\|B^*D\|^2\|p\|^2
       +c^2\|Ap\|^2+\|A^*B^*D\|^2
 \ge2c^4(1+c^2).                                           \tag{7}
\]

In particular `F>=0`. Equations (4) and (7), with zero initial values, imply

\[
 F^2\ge\frac23c^6+\frac12c^8,
 \qquad F\ge c^4/\sqrt2.                                   \tag{8}
\]

For a direct verification without division at `c=0`, the derivative of the
difference on the first line is
`2F [dot F-2c^4(1+c^2)] >= 0`.

The existing radial argument specializes to `D''=J J* D`, where `J` is the
hidden derivative of `BAp`. Thus `c` is convex, with initial right slope one
by (2). Consequently

\[
 c(t)\ge t,\qquad \dot c=F/c\ge c^3/\sqrt2\quad(t>0).       \tag{9}
\]

#### 3. Duration, norm, and integrated curvature bounds

Let `T` be the first normalized-time hit of `F=3/(2lambda)`, and set

\[
 M=\left(\frac3{\sqrt2\lambda}\right)^{1/4}>1.
\]

Before this hit, (8) gives `c<=M`. If the hit has not occurred before `c=1`,
that level is reached by time one, and (9) bounds the remaining duration by
`sqrt2 integral_1^M c^{-3} dc`. Therefore

\[
 T<2,\qquad S=T/\lambda\le2/\lambda,
 \qquad \sup_{t\le T}c(t)\le M.                            \tag{10}
\]

These also prove existence through the hit. Indeed, before it all four
vector-field components are bounded by a constant depending on `M`, by (5),
so their raw increments have a strong limit at a finite maximal endpoint.
Local polynomial-field existence continues the solution there. An unbounded
branch below the target contradicts (9) and the bound `c<=M`.

The same change of variable yields

\[
 \int_0^T c^2\,dt\le1+\sqrt2\log M,
 \quad
 \int_0^T(200+c^2)\,dt\le401+\sqrt2\log M.                 \tag{11}
\]

The contribution before `c=1` is at most one. Afterwards use
`dt/dc<=sqrt2/c^3`.

All affine primal norms used in the original proof are bounded by

\[
 R(t)=\sqrt{200+c(t)^2}.                                   \tag{12}
\]

For the first sample projections, `Q_1` is constant and
`z_i^1= +/- (r p +/- Q_1)`. Since `||Q_1||=sqrt(1-r^2)`, Cauchy--Schwarz
already gives `||z_i^1||<=sqrt(2+c^2)<=R`; the stronger existing Gaussian
orthogonality identity is unnecessary here.

The full raw displacement is also `O(M)`, not just the operator displacement.
For example, before `c=1`, both `||dot A||HS` and `||dot B||HS` are at most
201 and the duration is at most one. After `c=1`, each is at most
`c(200+c^2)`, whose time integral is at most

\[
 \sqrt2\int_1^M(200/c^2+1)\,dc\le\sqrt2(200+M).
\]

Thus each learned HS increment is at most `500 M`. The first raw increment
is `||p-p_0||<=3M` and `||D||<=M`, giving the convenient sum bound `1100 M`.
This verifies strong continuation with constants uniform in the input
dimension.

For the affine objective in the original raw metric, its Hessian has
zero diagonal blocks and six pairs of cross blocks. Each cross block has
norm at most `lambda R^2`: it is the product of the other two factors of
`lambda <D,BAp>`. In the sum of the four component norms, its operator norm
is at most `3lambda R^2`. The same bound holds on the full raw first-layer
space, because projection onto the normalized `u` direction is a contraction
and the affine objective annihilates the orthogonal directions. Hence

\[
 \int_0^S\|\nabla^2g(\Theta_0(s))\|\,ds
 \le1203+3\sqrt2\log M.                                  \tag{13}
\]

The affine variational propagator is therefore polynomial in `1/lambda`.
Crucially, the factor `lambda` in the Hessian is retained. A bound on the
unscaled Hessian by a polynomial primal radius would lose this conclusion.

#### 4. Full raw comparison with the original capped nonlinear field

Fix any cap. Let `Theta_e` be its original feature-time path for
`phi(z)=az+e atan z`, and `Theta_0` the affine path with the same `a`. Use
the sum norm of the original raw first-layer increment, two HS increments,
and readout. Let `E(s)=||Theta_e(s)-Theta_0(s)||_sum`. Stop at `E=1` if that
occurs, and put

\[
 b(s)=R(\lambda s)+1.
\]

Every state on the line between the two paths has all relevant primal
norms at most `b`. This includes the normalized active first coordinate `p`:
raw first-layer distance bounds its difference with constant one. No
symmetry or affine inactive-field identity is imposed on `Theta_e`.
The affine field depends only on `p,A,B,D`, even on those nonsymmetric
nearby states.

The existing term-by-term, cap-uniform same-state comparison remains valid:

\[
 \|V_{a,e,Rcap}(\Theta)-V_{a,0}(\Theta)\|_{sum}
 \le40e b^3.                                               \tag{14}
\]

It uses only `|atan|<=pi/2`, `|phi'-a|<=e`, and `|tau_Rcap(q)|<=|q|`.
Thus an odd divided-difference estimate, though available, is not needed
to gain the essential `lambda` in the stability coefficient. Subtract the
affine fields after making (14), rather than differentiating the nonlinear
field. This gives the integral/Dini inequality

\[
 E'\le3\lambda b^2 E+40e b^3.                              \tag{15}
\]

Since `R>=sqrt(200)>14`,

\[
 b^2\le(7/6)(200+c^2),\quad
 \int_0^S3\lambda b^2ds\le(7/2)(401+\sqrt2\log M)
 \le1404+5\log M.                                        \tag{16}
\]

Also `b^2<=235 M^2` and `b^3<=3600 M^3`. Gronwall and `S<=2/lambda` now give

\[
 E(s)\le288000\exp(1404)e\lambda^{-1}M^8
       =C_0 e\lambda^{-3},
 \qquad C_0=1296000\exp(1404).                             \tag{17}
\]

Consequently the explicit restriction

\[
 0\le e\le\min\{1/2,\lambda^3/(2C_0)\}                  \tag{18}
\]

closes the tube with `E<=1/2` and gives capped strong existence/comparison
through the entire affine endpoint. In delta-only form it is sufficient
that

\[
 e\le\frac{\delta^{3/2}}{2C_0(8\sqrt2)^3},
 \qquad
 E(s)\le C_0(8\sqrt2)^3 e\delta^{-3/2}.                   \tag{19}
\]

The proof is cap uniform. It gives continuous population capped paths, and
bounded-mesh versions follow by discrete variation of constants and then
mesh refinement. A separate source-response bound is still required to
remove caps with the desired probabilistic/tail properties.

#### 5. Forward and scalar endpoint estimates

Directly expanding the actual forward equations on the tube yields

\[
 \|z_{i,e}^1-z_{i,0}^1\|\le E,
\]
\[
 \|z_{i,e}^2-z_{i,0}^2\|\le2b E+(\pi/2)e b,
\]
\[
 \|z_{i,e}^3-z_{i,0}^3\|\le3b^2 E+\pi e b^2.               \tag{20}
\]

For example the last line follows by bounding the propagated second-layer
difference by `b` times its norm, the `B`-difference term by `E R^2`, and
the third-layer arctangent term by `(pi/2)e b`. Because `b>=1`, the stated
bound dominates their sum. Combining (17), `b^2<=235 M^2`, and
`M^2<1.5lambda^{-1/2}`, gives the convenient uniform bound

\[
 \max_{i,\ell,s\le S}\|z_{i,e}^\ell-z_{i,0}^\ell\|
 \le C_z e\lambda^{-7/2},\qquad C_z=1500 C_0.              \tag{21}
\]

For the scalar prediction, same-state forward comparison gives
`||h_e^3-h_0^3|| <= (pi/2)e(b^2+b+1)`. Therefore
`|g_e(Theta_e)-g_0(Theta_e)| <= 5e b^3`.
For the affine state difference retain its exact coefficient:
`|g_0(Theta_e)-g_0(Theta_0)| <= lambda b^3 E`.
Together these imply

\[
 |g_e(S)-3/2|\le C_g e\lambda^{-11/4},
 \qquad C_g=14400 C_0.                                    \tag{22}
\]

Indeed `b^3<=3600M^3`, `lambda E+5e<=2C_0e lambda^{-2}`,
and `M^3=(3/sqrt2)^{3/4}lambda^{-3/4}<2lambda^{-3/4}`.
Their product is bounded by the displayed constant.
It is enough to require `e<=lambda^{11/4}/(4C_g)` for endpoint margin `1/4`.

#### 6. Absolute Gaussian variance and nonaffinity margins

The apparent degeneration of the affine marginal variance with `delta` is
also removable. Radial convexity gives `||BAp||=||dot D||>=dot c>=1`.
Together with (5) and (6), this implies

\[
 \|Ap\|^2\ge\max\{c^2(1+c^2),(100+c^2)^{-1}\}\ge1/101.     \tag{23}
\]

For the last inequality split at `c^2=1`. The existing affine Gaussian
construction and frozen inactive-field orthogonality now give, for both
samples,

\[
 \operatorname{Var}(z_i^1)=v\|p\|^2+(1-v)\ge1,
\]
\[
 \operatorname{Var}(z_i^2)=a^2\{v\|Ap\|^2+(1-v)\}\ge1/404,
\]
\[
 \operatorname{Var}(z_i^3)=a^4\{v\|BAp\|^2+(1-v)\}\ge1/16. \tag{24}
\]

Thus every affine marginal is `sigma G` with `sigma>=m_*:=1/sqrt(404)`,
independently of `delta`, and no upper variance bound is needed for the
following nonaffinity estimate.

Let `H_3(G)=G^3-3G` and `h(sigma)=E[atan(sigma G)H_3(G)]`. Gaussian integration
by parts, with integrable polynomial bounds justifying differentiation,
gives

\[
 h(\sigma)=-2\sigma^3 E\frac{G^2}{(1+\sigma^2G^2)^2},
 \qquad
 h'(\sigma)=-2\sigma^2 E\frac{G^4}{(1+\sigma^2G^2)^2}<0.     \tag{25}
\]

For the derivative, first differentiate under the expectation and then use
`E[G^4 k(G)]=3E[G^2 k(G)]+E[G^3 k'(G)]` with
`k(G)=(1+sigma^2G^2)^{-1}`. For the first identity use
`E[H_3 f]=E[(G^2-1)f']` and then
`E[(G^2-1)k]=E[G k']`.

Since `H_3` is orthogonal to both `1` and `G` and has squared norm six,
Cauchy--Schwarz gives

\[
 \mathcal R(\sigma G)\ge h(\sigma)^2/6\ge h(m_*)^2/6.
\]

On `|G|<=1`, the standard normal density is at least
`exp(-1/2)/sqrt(2pi)`, so

\[
 E[G^2\mathbf1_{|G|\le1}]\ge
       \frac{2\exp(-1/2)}{3\sqrt{2\pi}}.
\]

Equation (25) consequently proves the explicit absolute lower bound

\[
 \mathcal R(\sigma G)\ge\eta_*:=
 \frac{4\exp(-1)}{27\pi}\frac{m_*^6}{(1+m_*^2)^4}
 =\frac{4\cdot404\exp(-1)}{27\pi\,405^4}>0
 \qquad(\sigma\ge m_*).                                  \tag{26}
\]

The square root of this regression residual is 1-Lipschitz in `W_2`. Here is
a self-contained verification. An optimal slope for regressing `atan Z` on
`Z` lies in `[0,1]`, by

\[
 \operatorname{Cov}(Z,\arctan Z)
 =\tfrac12E[(Z-Z')(\arctan Z-\arctan Z')]
 \in[0,\operatorname{Var}(Z)],
\]

where `Z'` is an independent copy. At zero variance choose slope zero.
For every `beta in [0,1]`, `z -> atan z-beta z` is 1-Lipschitz, since its
derivative is between `-beta` and `1-beta`. Using either variable's optimal
intercept and slope as a competitor for the other therefore proves

\[
 |\sqrt{\mathcal R(Z)}-\sqrt{\mathcal R(Z_0)}|
 \le\|Z-Z_0\|_2.                                         \tag{27}
\]

Equations (21), (26), and (27) preserve at least half of the square-root
margin, and hence `R(z_e)>=eta_*/4`, whenever

\[
 e\le\frac{\sqrt{\eta_*}}{2C_z}\lambda^{7/2}.              \tag{28}
\]

For a completely explicit delta-only restriction, define

\[
 c_*:=\min\left\{\frac12,
 \frac1{2C_0(8\sqrt2)^3},
 \frac1{4C_g(8\sqrt2)^{11/4}},
 \frac{\sqrt{\eta_*}}{2C_z(8\sqrt2)^{7/2}}\right\}>0.
\]

Then

\[
                  0<e\le c_*\delta^{7/4}                 \tag{29}
\]

simultaneously implies the tube restriction (18), endpoint margin `1/4`
from (22), and nonlinear regression margin `e^2 eta_*/4`. This follows from
`lambda>=sqrt(delta)/(8sqrt2)` and
`delta^{7/4}<=delta^{3/2},delta^{11/8}` on `(0,1]`.
Thus a polynomial coefficient restriction with exponent `7/4` suffices for
**all primal affine comparison, endpoint, and nonaffinity work**. For the
convex mixture take `a=1-e`; all estimates are uniform in that choice.

This improves the earlier exponent `13/4`, which unnecessarily used the reference
`delta`-dependent lower variance bound. The change uses the already proved
inactive-field freezing and Gaussianity, without strengthening the model.

#### 7. Why the original feature time cannot be logarithmic

The normalized-time argument also locates the necessary growth. While
`c<=1`, (5) and (4) give
`||dot D||<=sqrt(101*201*2)<202` and `F<202c`. If `lambda<=1/200`, the target
`3/(2lambda)` exceeds 202, so the flow must first reach `c=1`, which takes
normalized time at least `1/202`. Hence

\[
 S\ge\frac1{202\lambda}\qquad(\lambda\le1/200).            \tag{30}
\]

For `c>=1`, the same product bounds give `F<202c^4`, so its terminal readout
also satisfies `c(T)>[3/(404lambda)]^{1/4}` for small `lambda`. Thus the
rates `S=O(lambda^{-1})` and `c=O(lambda^{-1/4})` are sharp up to constants
from this model's initial bounds. The mechanism that permits a polynomial
comparison is integrated curvature, not logarithmic original feature time.

### E.5. Actual affine source probes, positivity and three enlargement scales

Within this proof unit, unqualified section and equation numbers are local.

Here \(r=\sqrt{(1+y_1y_2\rho)/2}\), \(\lambda=a^3r\), \(m=(3/(\sqrt2\lambda))^{1/4}\) is the actual endpoint scale and \(M=24^{1/4}\delta^{-1/8}\) is its uniform envelope. Thus \(1<m\le M\); only \(r\asymp m^{-4}\) is used. The symbols \(C_B,H_{\rm num}\) refer to the explicit H in Fragment E. In other units M denotes the actual endpoint scale, as defined there.

#### 2. Exact normalization of both sample sectors

Fold the labels, so the controls are ((1/2,1/2)). Work in the
mean/contrast basis

\[
 Q={1\over2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
 Q^{-1}=2Q,\qquad S_0=\operatorname{diag}(r,r_-),\quad
 r_-=\sqrt{1-r^2}.
\]

Both diagonal entries of $S_0$ are positive under the angle hypothesis.
Use $t=\lambda s$, with mesh steps $\Delta t_j=\lambda h_j$, and
denote its strict integration matrix by $H$:

\[
 H_{kj}=\Delta t_j I_2\quad(j<k).
\]

For fields, define

\[
 Qz^\ell=a^{\ell-1}S_0x_\ell,\qquad
 Qh^\ell=a^\ell S_0\widehat h_\ell,\qquad
 Q\delta^\ell=a^{4-\ell}rS_0^{-1}d_\ell.
\tag{1}
\]

In the affine case $\widehat h_\ell=x_\ell$, and, with $D=C$ after
folding,

\[
 x_1=(p,p_-),\quad x_2=(Ap,A_0p_-),\quad
 x_3=(BAp,B_0A_0p_-),
\]
\[
 d_3=(D,0),\quad d_2=(B^*D,0),\quad
 d_1=(A^*B^*D,0).
\tag{2}
\]

The frozen inactive identities are the canonical Gaussian identities
proved in Fragment E.3, not a claim that arbitrary bounded actions
preserve independence. In particular all inactive normalized forward
standard deviations at beta one are one. At beta initialization they
are respectively $\beta,\beta^2,\beta^3$.

These transformations also normalize the full, possibly nonlinear,
raw updates exactly:

\[
 x_1'=d_1,\qquad
 A'=\sum_{i=+,-}d_{2,i}\otimes\widehat h_{1,i},\qquad
 B'=\sum_{i=+,-}d_{3,i}\otimes\widehat h_{2,i},\qquad
 D'=\widehat h_{3,+},
\tag{3}
\]

where prime denotes normalized time. For example

$Q R_xQ^{-1}/2=S_0^2$, so the first raw update divided by its field
scale becomes $S_0^{-1}S_0^2a^3rS_0^{-1}/\lambda=I$.
For the second matrix update, each sample-sector factor contributes

$(a^2r/s_i)(as_i)/\lambda=1$. The third matrix has the same
factor. The readout update gives $a^3r/\lambda=1$.

This verifies that the sample normalization changes neither the raw
metric nor the algorithm. It is merely a re-expression of its equations.
The actual affine state on the active four-component space obeys

\[
 p'=A^*B^*D,\quad A'=B^*D\otimes p,\quad
 B'=D\otimes Ap,\quad D'=BAp.
\tag{4}
\]

#### 3. Exact normalized source arrays

In this section write $A_2,A_3,B_3,B_2$ for the source arrays after
the fixed $Q\cdot Q^{-1}$ sample change of basis. Define

\[
 \widehat A_2=arS_0^{-1}A_2S_0^{-1},\qquad
 \widehat A_3={r\over a}S_0^{-1}A_3S_0^{-1},
\]
\[
 \widehat B_3={a\over r}S_0B_3S_0,\qquad
 \widehat B_2={1\over ar}S_0B_2S_0.
\tag{5}
\]

For example $z^2=\xi^2+A_2\delta^2$, after $1$, gives

$x_2=\widehat\xi^2+\widehat A_2d_2$. Transforming the formal
derivative $\partial h^1/\partial\zeta^1$ gives the identical
factor in $5$. Therefore neither variance factors nor gain factors are
being hidden in a redefinition of the formal derivatives.

Set $P_+=\operatorname{diag}(1,0)$. The exact transformed maps are

\[
 \widehat F=(I-H\widehat B_2)^{-1}H,
 \quad \widehat R=(I-\widehat A_2\widehat B_3)^{-1},
 \quad \widehat L=(I-\widehat B_3\widehat A_2)^{-1},
\]
\[
 \widehat V=\widehat R\widehat A_2,
 \quad \widehat T=HP_+(I-\widehat A_3HP_+)^{-1},
 \quad \widehat W=\widehat B_3\widehat R.
\tag{6}
\]

All gain factors cancel. The coefficient equations at Gaussian matrix
variance $\beta^2$ are

\[
 \widehat A_2=\beta^2\widehat F+\widehat M_{A2},\quad
 \widehat A_3=\beta^2\widehat V+\widehat M_{A3},\quad
 \widehat B_3=\beta^2\widehat T+\widehat M_{B3},\quad
 \widehat B_2=\beta^2\widehat W+\widehat M_{B2}.
\tag{7}
\]

The four learned-moment entries are exactly

\[
 (\widehat M_{A2})_{kj}=\Delta t_j\,\mathbb E[x_{1,k}x_{1,j}^T],
 \quad
 (\widehat M_{A3})_{kj}=\Delta t_j\,\mathbb E[x_{2,k}x_{2,j}^T],
\]
\[
 (\widehat M_{B3})_{kj}=\Delta t_j\,\mathbb E[d_{3,k}d_{3,j}^T],
 \quad
 (\widehat M_{B2})_{kj}=\Delta t_j\,\mathbb E[d_{2,k}d_{2,j}^T].
\tag{8}
\]

To check the sample factor, the original learned matrix is

$(h_j/2)\mathbb E[H_kH_j^T]$. Its $Q\cdot Q^{-1}$ transform is

$h_j\mathbb E[(QH_k)(QH_j)^T]$, since $Q^{-1}=2Q^T$.
Then $1$ and $5$ give $\Delta t_j$, as displayed.

The normalized Gaussian sources likewise have covariance matrices

$\beta^2\mathbb E[\widehat h\widehat h^T]$ or

$\beta^2\mathbb E[dd^T]$, with no sample condition number. Their
largest affine standard deviation is $O(m^2)$; $d_1=O(m^3)$ is
an output field, not a fresh source covariance input.

All baseline source arrays are diagonal in the sample sectors. Their
inactive entries can be computed exactly:

\[
 \widehat F_-=H,\quad
 \widehat A_{2,-}=2\beta^2H,\quad
 \widehat V_-=2\beta^2H,\quad
 \widehat A_{3,-}=3\beta^4H.
\tag{9}
\]

Every inactive backward array is zero. All four inactive resolvents
are identity. Thus the inactive normalization introduces no large
affine constants even when $r_-\ll r$, or conversely.

#### 4. Affine geometry and enlargement

The assigned affine proof supplies, up to its own target time $T<2$,

\[
 \|p\|,\|A\|,\|B\|,\|D\|\le Cm,
 \quad \|Ap\|,\|B^*D\|\le Cm^2,
 \quad \|BAp\|,\|A^*B^*D\|\le Cm^3.
\tag{10}
\]

The normalized raw variational propagator is bounded by

$G\le C m^5$, because the integrated radius-one tube Hessian is

$1404+5\log m$. Its restriction to any later initial time obeys
the same bound. The time-dependent estimate, rather than a constant
Lipschitz estimate $\exp(Cm^2T)$, is essential here.

Let $R_*=\sqrt{200+m^2}$, and take

\[
 \beta_*=1+{1\over10^5R_*^2}.
\tag{11}
\]

The reference exists an additional $1/(1000R_*^2)$ units of normalized
time on a ball of component sizes at most $2R_*$, by the local
polynomial vector-field bound $32R_*^3$. Its added integrated tube
Hessian is bounded by an absolute constant. Homogeneity gives

$\Theta_\beta(t)=\beta\Theta_1(\beta^2t)$, and

$\beta_*^2T-T\le6(\beta_*-1)<1/(1000R_*^2)$.
Consequently the whole same interval $0\le t\le T$ is valid for

$1\le\beta\le\beta_*$, with the same bounds $10$ and

$G\le Cm^5$. Also $(\beta_*-1)^{-1}\le Cm^2$.

Strong affine Euler approximation gives these estimates, enlarged by
an absolute factor, on every sufficiently fine mesh. Each fixed-mesh
finite-program width limit is taken separately; nothing here asserts
uniform probability control over growing transcripts or operator-norm
convergence of trained finite matrices.

#### 5. The normalized probe certificate

For this section all densities use $\Delta t_j$, and hats are omitted.
Use the sum norm of the four active raw state components in $4$. A
single error inserted at time $j$ first changes an update with its
factor $\Delta t_j$. Thereafter its state variation is bounded by

$G$ times that initial increment. The following table gives the
injection cost and the relevant output Lipschitz cost. Factors denoted
by $C$ are numerical and independent of $m$.

| Injected normalized answer | Updates affected | Injection cost | Output | Output cost |
|---|---|---:|---|---:|
| $\zeta^1$ in $d_1$ | $p$ | $1$ | $p$ | $1$ |
| $\zeta^2$ in $B^*D$ | $p,A$ | $Cm$ | $Ap$ | $Cm$ |
| $\xi^3$ in $BAp$ | $D$ | $1$ | $D$ | $1$ |
| $\xi^2$ in $Ap$ | $B,D$ | $Cm$ | $B^*D$ | $Cm$ |

For example the second row changes (p') by $A^*e$ and (A') by

$e\otimes p$, each $O(m\|e\|_2)$. The fourth changes (B')
by $D\otimes e$ and (D') by $Be$. These are the normalized
versions of the exact four answer probes already proved in E.5.

Insert an independent standard Gaussian field $G_0$ in the population
of the answer/output, with arbitrary deterministic signs at finitely
many source slots. The finite-difference identity of the source proof
converts the deterministic response bounds into signed sums of formal
derivatives. Taking signs of those deterministic expected derivatives
gives the row bound. A single slot gives strict density. This yields

\[
 |F|_d,|T|_d\le CG\le Cm^5,
 \qquad |V|_d,|W|_d\le Cm^2G\le Cm^7.
\tag{12}
\]

The actual coefficients include moments $8$, of respective density
orders $m^2,m^4,m^2,m^4$. Therefore

\[
 |A_2|_d,|B_3|_d\le Cm^5,
 \qquad |A_3|_d,|B_2|_d\le Cm^7.
\tag{13}
\]

Since $T<2$, the same exponents bound their row norms.

For $R$, use the fourth answer probe and observe its $Ap$ output,
rather than $B^*D$. For $L$, use the second probe and observe

$B^*D$, rather than $Ap$. The current direct derivative is identity;
every strict derivative has cost $Cm^2G\Delta t_j$. Hence

\[
 |R|_r,|L|_r\le 1+CTm^2G\le Cm^7.
\tag{14}
\]

For $R_3=(I-A_3HP_+)^{-1}$, use the existing $\xi^3$ probe and
observe $BAp$. Its output Lipschitz cost is $Cm^2$, while its
injection cost is one, so again

\[
 |R_3|_r\le Cm^7.
\tag{15}
\]

For completeness, $R_1=(I-HB_2)^{-1}$ admits the same proof with a
finite affine coordinate-program probe. Add $\varepsilon\alpha_jG_0$
to the first preactivation immediately before using it in the forward
calls, retaining the original integrated first-state variable separately.
Its source equation is $p=\xi^1+Hd_1$, with $d_1=\zeta^1+B_2p$;
therefore its frozen-array forward-source derivative is $R_1$.
The perturbation changes the $A,B,D$ updates with cost $Cm^2$,
and the future $p$ output has cost one, plus its current identity.
Thus

\[
 |R_1|_r\le Cm^7.
\tag{16}
\]

This use of the probe identity does not require a new random-matrix
operation. The independent Gaussian root is inserted into an ordinary
affine coordinate instruction. The same fixed-program conditioning,
finite difference, and independent-root proof applies. Reflection

$(\varepsilon,G_0)\mapsto(-\varepsilon,-G_0)$ makes the original
source covariance and learned-moment parameters even in the amplitude,
so their first variation does not contribute. As in the supplied probe
lemma, no Gaussian covariance square root is differentiated and no
derivative is interchanged with an uncontrolled width limit.

Likewise add $\varepsilon\alpha_jG_0$ to the backward readout answer
used in $d_3$, retaining the integrated $D$ state separately. The
frozen-array derivative of $x_3$ is $U=R_3A_3$. The $p,A,B$
updates each have injection cost $Cm^2$, and the output $BAp$
has cost $Cm^2$. There is no current output injection. Consequently

\[
 |U|_d\le Cm^4G\le Cm^9.
\tag{17}
\]

Only the active sample sector needs the large probe bounds. The exact
inactive formulas $9$ handle all the other baseline entries.

A proposed shortcut from beta positivity alone would be insufficient. Since

$B_3'=2T+T A_3'T+M_{B3}'$, one has

$T A_3'T\le B_3'$, but this alone does not control $A_3TA_3$.
Thus it must **not** be substituted for the actual top probe without
another argument. The proof of $17$ here is the explicit coordinate
probe just given; no unproved beta shortcut is used.

#### 6. Beta positivity and actual coupled inverse

Still use normalized time and omit hats. At a fixed affine mesh all
active coefficient entries and learned moments are nonnegative
polynomials in beta. This follows by expanding the normalized ascent
updates into raw Gaussian coordinates: their polynomial coefficients
are nonnegative, and every nonzero Wick pairing has nonnegative variance
weight. The chronological affine source recursions preserve positivity.
This is positivity after Gaussian expectation, not positivity of a
sample of the initialized weights.

Let $C'=(A_2',A_3',B_3',B_2')$ denote the beta derivative at one.
Differentiating $7$, with the normalized mesh held fixed, gives

\[
 (I-J_0)C'=(2F+M_{A2}',2V+M_{A3}',2T+M_{B3}',2W+M_{B2}').
\tag{18}
\]

There is no missing mesh or gain derivative. Scaling all initialized
raw hidden parameters changes the initialized-matrix return variance
to $\beta^2$, and all the normalized integration operators in $6$
are beta independent.

Every active component of the forcing in $18$ is at least

$2\Delta t_j$ at strict times: $F,V,T,W\ge H$ on the active
sector. Also, for any polynomial $f(\beta)=\sum c_k\beta^k$
with $c_k\ge0$,

\[
 f'(1)\le{f(\beta_*)-f(1)\over\beta_*-1}
 \le {f(\beta_*)\over\beta_*-1}.
\tag{19}
\]

Combining $11$--$13$ yields

\[
 |A_2'|_d,|B_3'|_r\le Cm^7,\qquad
 |A_3'|_d,|B_2'|_r\le Cm^9.
\tag{20}
\]

The finite causal inverse $ (I-J_0)^{-1}$ is entrywise nonnegative.
For active forward forcing of density at most $q$, with zero backward
forcing, compare its absolute value entrywise to $q/2$ times the
forcing in $18$. This proves

\[
 \|(I-J_0)^{-1}(E_2,E_3,0,0)\|\le Cm^9q.
\tag{21}
\]

This is a bound on the coupled inverse itself. A raw variational
estimate alone would not imply it.

The derivative of the second equation in $7$ gives, entrywise,

\[
 A_3'\ge R A_2'L\ge 2RFL.
\tag{22}
\]

Since $R,L\ge I$ on the active sector, $20$ implies

\[
 |FL|_d,|RF|_d,|RFL|_d\le Cm^9.
\tag{23}
\]

The inactive identities $9$ give the same bound for the full baseline
sample matrices.

Arbitrary backward-row forcing is handled by the exact shift

\[
 \widetilde Y_3=Y_3-J_3,\qquad
 \widetilde Y_2=Y_2-LJ_3R-J_2,
\]
\[
 \widetilde E_2=E_2+FJ_2F+FLJ_3RF,
 \qquad \widetilde E_3=E_3+VJ_3V.
\tag{24}
\]

The sandwich estimate, with duration $T<2$, gives

$\max(|\widetilde E_2|_d,|\widetilde E_3|_d)\le Cm^{18}q$.
Equations $21$ and $24$ then give an active full inverse bound

$Cm^{27}$, including reconstruction, since

$|LJ_3R|_r\le Cm^{14}q$.

In every non-active sample sector $TX_3T=WX_2W=0$, so it has no
feedback ladder. One determines $Y_3$, then $Y_2$, then $X_2$,
then $X_3$ by direct substitution. This proves a polynomial bound
without a variance inverse. A conservative explicit full-sector bound
is $Cm^{39}$: $24$ gives $X_2$ density at most $Cm^{18}q$, and

\[
 |RX_2L|_d
 \le |R|_r\bigl(|X_2|_d+T|X_2|_d|B_3|_r|V|_d\bigr)
 \le Cm^{19}|X_2|_d.
\]

Thus $Cm^{37}q$ already suffices for $X_3$; $Cm^{39}$ leaves
absolute slack. The right factor $L$ is expanded as $I+B_3V$
here: a row bound on $L$ alone does not bound the strict density of

$X_2L$. This distinction prevents a false mixed-sector estimate.

The positive supersolution E.7 uses the product bounds (23); the conservative full inverse above is an additional affine estimate.

#### 7. Conversion back to original feature-time bounds

All actual affine baseline arrays are diagonal in the sample sectors,
so the row norms of $R_1,R,L,R_3$, which transform by diagonal
similarity, do not change. On the active sector $5$ reduces to

\[
 A_2={r\over a}\widehat A_2,\quad
 A_3=ar\widehat A_3,\quad
 B_3={1\over ar}\widehat B_3,\quad
 B_2={a\over r}\widehat B_2.
\tag{25}
\]

These same factors apply respectively to $F,V,T,W$. For strict
densities there is the additional factor

$\Delta t_j/h_j=\lambda=a^3r$; row norms have no such factor.
Therefore the active bounds are

\[
 |F|_{d,s}\le Cr^2m^5,\quad |V|_{d,s}\le Cr^2m^7,
 \quad |T|_{r,s}\le Cm^5/r,\quad |W|_{r,s}\le Cm^7/r.
\tag{26}
\]

Using $r\asymp m^{-4}$ gives the active orders

$m^{-3},m^{-1},m^9,m^{11}$. The inactive forward entries, by $9$,
have original-time density $O(r_-^2)\le O(1)$. Learned forward
moments satisfy the same upper bounds: their active densities are

$O(r^2m^2)$ and $O(r^2m^4)$, and their inactive densities are

$O(r_-^2)$. This proves the full forward bounds in Section 1.

The top $U$ transforms like $A_3$; hence $17$ gives

\[
 |U|_{d,s,+}\le Cr^2m^9\le Cm.
\tag{27}
\]

The products $FL,RF,RFL$ transform like $F$, and $23$ yields
the same bound $Cr^2m^9\le Cm$. Their inactive densities are
again $O(1)$. Since $m\le M$, all bounds in the certificate
follow uniformly over the data. Every beta-enlarged reference obeys
the same estimates. Section 8 extends the beta-derivative argument
from beta one to every beta in $[1,b_3]$, including the first and
second intrinsic comparison scales, using the common enlarged
reference from Section 4.

This certificate supplies no restriction on a nonlinear amplitude by
itself. Its useful conclusion for the proposed improvement is that all
the weaker original-time affine exponents requested by the affine construction are
valid, including the top strict transfer and the beta product bounds.

#### 8. Explicit common prefactor and three intrinsic beta scales

For this numerical certificate, keep $m$ as the **actual dataset endpoint
scale**, and $M=24^{1/4}\delta^{-1/8}$ only as its upper envelope.
Set exactly as in the existing quantitative proof

\[
 C_0=1296000e^{1404},\qquad C_z=1500C_0,\qquad C_g=14400C_0,
\]
\[
 H_{\mathrm{num}}=
 10^{30}(1+C_0+C_z+C_g+e^{1410})^4.
\tag{28}
\]

Thus $H_{\mathrm{num}}$ is the reference $C_B$, not an unspecified new
constant. It can serve as a common coefficient in **every affine bound
in the first table**, including the sharpened powers in its middle
column. It also bounds the $L_3$ row discussed below.

Use the three proof-auxiliary scales

\[
 b_j=1+\frac{j}{10^6(200+m^2)},\quad j=1,2,3,
 \qquad b_{\rm far}=1+\frac1{10^5(200+m^2)}.
\tag{29}
\]

They are allowed to depend on the dataset. Only the ultimately chosen
activation amplitude must depend on $\delta$ alone. Since $m>1$,

\[
 H_{\mathrm{num}}^{-1}m^{-2}
 \le b_{j+1}-b_j
 =\frac1{10^6(200+m^2)}
 \le H_{\mathrm{num}}m^{-2},
\tag{30}
\]

also with $b_0=1$. All four scales are in the common extension established
in Section 4. Each $b_j$ leaves at least

\[
 b_{\rm far}-b_j\ge \frac7{10^6(200+m^2)}
 \ge\frac1{3\cdot10^7m^2}
\tag{31}
\]

units of beta room. For a nonnegative-coefficient polynomial, at any
$b\in[1,b_3]$,

\[
 f'(b)\le\frac{f(b_{\rm far})}{b_{\rm far}-b}
 \le 3\cdot10^7m^2f(b_{\rm far}).
\tag{32}
\]

This provides all product bounds from beta differentiation uniformly on
the smaller three scales, not only at beta one.

Here is ample numerical accounting behind the common coefficient. On
the enlarged family and sufficiently fine meshes, take the bound on
each primary component to be $100m$, and the variational propagator
to be $4e^{1410}m^5$. The maximum injection and output Lipschitz costs
in the proof are each at most $3(100m)^2$. Their product times the
propagator is at most $4\cdot10^9e^{1410}m^9$. A factor $100$ covers
the fixed two-sample changes of basis, the scaled Gaussian variances,
the identity term of each row, and the Euler strict margin. Therefore
$10^{12}e^{1410}$ dominates all normalized probe and coefficient
prefactors. Learned moments have smaller prefactors and powers.

The beta derivative costs at most $3\cdot10^7m^2$ by $32$, so
$10^{21}e^{1410}$ dominates the derivative prefactors. Converting
strict densities back to original time uses $a^{-1}\le2$ and

\[
 r=\frac{3}{\sqrt2a^3}m^{-4},
 \qquad r^2\le288m^{-8},\qquad r^{-1}\le m^4.
\tag{33}
\]

Thus the numerical coefficient $10^{25}e^{1410}$ dominates every
entry in the first table, uniformly for beta in $[1,b_3]$.
Finally

\[
 10^{25}e^{1410}<10^{30}e^{5640}\le H_{\mathrm{num}}.
\tag{34}
\]

This proves the stated explicit prefactor certificate. The high
degrees in the optional full coupled-inverse estimate in Section 6
can of course require products of $H_{\mathrm{num}}$; $34$ is a
common prefactor assertion for the affine input table, not an assertion
that every subsequent polynomial manipulation costs only one factor.

The additional backward top resolvent is

\[
 L_3=(I-K_3A_3)^{-1},\qquad
 \widehat L_3=(I-HP_+\widehat A_3)^{-1}.
\tag{35}
\]

For the same independent Gaussian probe inserted into the top backward
answer, the frozen normalized equations are

\[
 d_3=E D+\varepsilon\alpha_jG_0,\qquad
 ED=HP_+x_3,\qquad x_3=\xi^3+A_3d_3.
\]

Thus the derivative of $d_3$ with respect to the added answer is
$L_3$. Its current term is identity. The future output $D$ has
Lipschitz cost one and the state injection cost is at most
$3(100m)^2$. The same signed Gaussian-probe bound yields

\[
 |\widehat L_3|_r\le 1+CTm^2G\le
 H_{\mathrm{num}}m^7.
\tag{36}
\]

The baseline is sample diagonal, so diagonal similarity under $5$
does not change its row norm. Hence $|L_3|_r\le H_{\mathrm{num}}m^7$
in original time as well. The inactive block is exactly identity.

### E.6. Weighted affine propagator

Within this proof unit, unqualified section and equation numbers are local.

Here M=(3/(sqrt(2) lambda))^(1/4), lambda=a^3 r, r=sqrt((1+y_1 y_2 rho)/2), and H=C_B is the constant at the start of E. The weighted propagator uses w_beta(t)=sqrt(beta^2+||D_beta(t)||^2).

#### 1. All four gradient terms improve the radial lower bound

At beta=1 write z=||D||^2, F=<D,BAp>, K=A0* A0-p0 tensor p0, J=A0 A0*-B0*B0, and K_B=B0B0*. The active normalized system is exactly

    p'=A*B*D,  A'=B*D tensor p,  B'=D tensor Ap,  D'=BAp.

The existing balances give

    ||p||^2=1+z,  A*A=p tensor p+K,
    AA*=B*B+J,    BB*=D tensor D+K_B.

The initial hypotheses ||A0||,||B0||<=10 and ||p0||=1 imply

    -I<=K<=100 I,  -100 I<=J<=100 I,  0<=K_B<=100 I.

Let s_A=||Ap||^2 and s_B=||B*D||^2. Then

    z(1+z)<=s_A<=(z+101)(z+1),
    z^2<=s_B<=z^2+100z.

The upper bound on s_A follows from A*A<=p tensor p+100I, which also slightly improves the reference operator bound for A. The two matrix-gradient terms obey

    ||A'||_HS^2=s_B(1+z)>=z^3+z^2,
    ||B'||_HS^2=z s_A>=z^3+z^2.

For the readout gradient, using B*B=AA*-J and Cauchy--Schwarz against p,

    ||D'||^2=||BAp||^2
      >=||A*Ap||^2-100s_A
      >=s_A^2/(1+z)-100s_A
      >=z^2(1+z)-100(z+101)(z+1)
       =z^3-99z^2-10200z-10100.

No monotonicity of the quadratic in s_A is assumed: its positive term is bounded below and its negative term separately bounded below by the upper bound on s_A. For the bottom gradient, BB*D=zD+K_BD and K_B>=0 give

    ||p'||^2=||A*B*D||^2
      >=||BB*D||^2-100s_B
      >=z^3-100z^2-10000z.

Since the system is gradient ascent for F,

    F'>=4z^3-197z^2-20200z-10100,              (1)
    z'=2F,  F>=0.

Integrating (1) without dividing by F or z gives

    F^2 >= P(z):=z^4-(197/3)z^3-10100z^2-10100z.   (2)

Indeed the derivative of F^2-P(z) equals 2F[F'-P'(z)]>=0 and its initial value is zero. The reference middle-gradient estimate also gives F>=z^2/sqrt(2). These two bounds imply the convenient global inequality

    F>=z^2-100z.                                  (3)

For 0<=z<=200, z^2/sqrt(2)>=z^2-100z because 1-1/sqrt(2)<1/2. For z>=200,

    P(z)-(z^2-100z)^2
      =z^2[(403/3)z-20100-10100/z]>0;

the bracket is increasing and positive at 200, and z^2-100z>=0. Thus (2) gives (3) also in this range.

#### 2. A two-time M^3 propagator with an explicit constant

At scale beta, homogeneity gives Theta_beta(t)=beta Theta_1(beta^2t), F_beta=beta^4 F_1(beta^2t), and c_beta=||D_beta||=beta c_1(beta^2t). Therefore (3) becomes

    F_beta>=c_beta^4-100 beta^2 c_beta^2.

For w_beta=sqrt(beta^2+c_beta^2),

    (log w_beta)'=F_beta/(beta^2+c_beta^2)
      >= c_beta^2-101 beta^2.                    (4)

The existing enlargement applies on the same normalized interval 0<=t<=T<2 for

    beta_j=1+j/[10^6(200+M^2)], j=1,2,3,
    beta_far=1+1/[10^5(200+M^2)].

All these beta are at most 1.001. Put R_beta=sqrt(200 beta^2+c_beta^2). Every affine component has norm at most R_beta. In the sum of the four raw increment norms, the affine Hessian is bounded by 3R_beta^2: its six pairs of off-diagonal blocks are products of the remaining two factors, and every column has three such blocks. The affine objective annihilates inactive first-layer directions, so this is also the full raw metric bound.

On a raw radius-one tube, the Hessian is bounded by 3(R_beta+1)^2. From (4), for any s<=t<=T,

    integral_s^t 3 R_beta^2 du
       <=3 log[w_beta(t)/w_beta(s)]+903 beta^2(t-s)
       <3 log[w_beta(t)/w_beta(s)]+1810.          (5)

The reference radial inequalities c_1(t)>=t and c_1'>=c_1^3/sqrt(2) imply on its entire existence interval

    integral c_1 dt <=1+sqrt(2).

Before c_1 first reaches one the duration is at most one and c_1<=1. Afterwards substitute dt<=sqrt(2)c_1^(-3) dc_1 and integrate to any terminal value. Homogeneity yields integral_0^T c_beta dt<=1+sqrt(2). Hence

    integral_0^T R_beta dt
      <=sqrt(200) beta T+1+sqrt(2)<31.

Combining this with (5),

    integral_s^t 3(R_beta+1)^2 du
      <=3 log[w_beta(t)/w_beta(s)]+2100.          (6)

Consequently the raw variational propagator, and the finite-difference tube comparison relevant to the probes, have the two-time bound

    G_beta(t,s)<=exp(2100)[w_beta(t)/w_beta(s)]^3. (7)

The already established enlargement keeps the continued beta-one primary components below 2sqrt(200+M^2); after the beta factor, w_beta(T)<=30M. Also w_beta(s)>=beta>=1. Thus a safe common global bound is

    G_beta(t,s)<=10^5 exp(2100) M^3.             (8)

The radius-one term in (6) is integrated as 6R_beta+3. Replacing (R_beta+1)^2 by a fixed multiple of R_beta^2 would unnecessarily increase the logarithmic coefficient and lose the exact exponent three.

The same estimate with an extra factor four holds on every sufficiently fine positive Euler mesh. One first applies uniform bounded-set Euler approximation over the compact beta interval and then approximates the deterministic integral in (6). The mesh may depend on the fixed dataset and bound M. This statement requires no uniform width probability estimate for a growing transcript. At each fixed mesh the original finite-program width limit and then the independent-root amplitude limit are taken in their prescribed order.

#### 3. The actual affine source arrays

Use the exact normalization of Fragment E.5. Densities in this paragraph use normalized steps Delta t_j=lambda h_j. Every source probe is an additive independent standard Gaussian root inserted at its named answer instruction. Perturbed programs recompute all subsequent calls and updates. The probe identity is the original Fragment D.2, equations (23)--(25): at fixed nonzero amplitude epsilon, take the fixed-program width limit, pair the output with the root, and only afterwards let epsilon tend to zero. The identity measures the deterministic formal derivatives with coefficient/covariance arrays frozen. No identification of an arbitrary raw tangent with a source derivative is used.

The existing injection and output costs are unchanged. Bottom transpose -> p and top forward -> D have product cost 1. Middle transpose -> Ap and middle forward -> B*D have product cost C M^2. The six forward/backward resolvent probes have product cost C M^2, and the top backward -> BAp probe has product cost C M^4. Each strict pulse carries its original Delta t_j. Reusing the same independent root with signs at all source slots bounds full absolute rows, including their direct identity where present.

Substituting (8) gives the following normalized-time bounds. They are uniform on the three inner beta scales.

| Affine object | Strict density or full row bound |
|---|---:|
| F,T,A2,B3 density | H M^3 |
| V,W,A3,B2 density | H M^5 |
| B3,T complete rows | H M^3 |
| B2,W complete rows | H M^5 |
| R1,R,L,R3,L3 complete rows | H M^5 |
| U=R3 A3 density | H M^7 |

The coefficient bounds add the actual learned moments, with density exponents 2,4,2,4, respectively. Their powers are lower than the displayed response powers. The inactive sector remains explicit: F_-=H_time, A2_-=2beta^2 H_time, V_-=2beta^2 H_time, A3_-=3beta^4 H_time, and all inactive affine backward arrays vanish. Inactive resolvents are identity.

The beta-positivity proof is unchanged. At a fixed mesh all active entries and learned moments are nonnegative polynomials in beta, and

    A3_beta'>=2 beta^3 R_beta F_beta L_beta.

The available beta gap has inverse at most 3*10^7 M^2. Since normalized A3 has density H M^5 before beta differentiation, the same direct coefficient argument yields

    |FL|d, |RF|d, |RFL|d <= H M^7.               (9)

Here H in (9) is still one common numerical prefactor, as counted below, rather than multiplying a previously saturated bound H by another H and silently reducing it.

#### 4. Original-time table and the useful active bounds

On the active sector, the exact factors are

    A2=(r/a) A2_hat,  A3=ar A3_hat,
    B3=(ar)^(-1) B3_hat,  B2=(a/r) B2_hat,

with the identical transformations for F,V,T,W. Strict densities have the additional factor lambda=a^3 r. Resolvents transform by diagonal similarity and their diagonal-sector rows do not change. U transforms like A3; FL,RF,RFL transform like F. Thus, with every common numerical constant at most the original H:

| Original-time object | Active sector | Full two-sample bound |
|---|---:|---:|
| F,A2 density | H M^-5 | H |
| V,A3 density | H M^-3 | H |
| T,B3 complete row | H M^7 | H M^7 |
| W,B2 complete row | H M^9 | H M^9 |
| R1,R,L,R3,L3 complete rows | H M^5 | H M^5 |
| U density | H M^-1 | H |
| FL,RF,RFL density | H M^-1 | H |

The inactive contribution to the final three strict transfers is O(1), not M^-1. The small active densities must be retained when making the active positive supersolution. Useful additional active row bounds are |F|r<=H M^-1 and |V|r<=H M; these follow directly from the normalized rows and the factor r. If obtained by multiplying the original-time density by the interval length, they give the same powers.

For the numerical check, on the enlarged reference take every primary bound as 100M. Formula (8), with a factor four for the Euler margin, costs at most 4*10^5 exp(2100) M^3. The largest product of injection/output costs is 9*(100M)^4, so 4*10^14 exp(2100) dominates every normalized probe prefactor. A factor 10^3 covers two-sample basis changes, duration <=2, current identities, beta<=1.001, gains, and moment additions. A further factor 3*10^7 handles beta differentiation. Conversion back to original time uses r^2<=288 M^-8 and r^-1<=M^4; another factor 10^4 is more than sufficient. Thus 10^30 exp(2100) dominates every displayed original-time coefficient, response, and beta-product prefactor. Since 10^30 exp(2100)<10^30 exp(5640)<=H, the table retains the existing explicit numerical envelope H.

#### 5. Consequence for positive closure, and the remaining nonlinear obligation

The active supersolution algebra in Fragment E.7 now has the following power count, using the same genuine strict/row/strict sandwich estimate and retaining arbitrary current diagonals:

    |F J2 F|d <= C M^(-6) q,
    |(FL) J3 (R*F)|d <= C M^2 q,
    |V J3 V|d <= C M^(-2) q.

Here the duration contributes M^4; the two active FL/RF densities each contribute M^-1. The relative active forcing divides by the unchanged lower bound F_kj,V_kj>=c M^-8 h_j. Thus the first-forward relative defect is C M^10 q, the second is at most C M^8 q, and the beta scale margin is c M^-2. Active forward closure needs q<=c M^-12.

Backward reconstruction has |L J3 R*|r<=C M^10 q. With active outer backward excess radius c0 M^-2, q<=c M^-12 also makes the backward supersolution interior. The active Neumann ratio uses |V|r<=C M, so that outer radius gives C c0 M^-1. Choose a separate inactive outer radius c0 M^-5, because its integration row is O(M^4); q<=c M^-12 is more than sufficient for its direct forced construction. The separate nonlinear source and positive-supersolution arguments use these distinct active/inactive outer radii.

A deliberately rounded numerical version can retain q<=H^-20 M^-12, active radius H^-10 M^-2, and inactive radius H^-10 M^-5. Exact H bookkeeping can follow the published closure ledger with the revised powers; there is ample spare prefactor in the ultimate c_poly= min(1/4,c_*,10^-70 H^-400).

This proof unit proves the new affine input and its actual derivative identification, but does not by itself prove the full delta^4 theorem. The separate response lemma in Fragment F.4 supplies forcing q<=C e M^19 on this outer box. Its source-value triangle estimates retain incoming subGaussian exponents q1:M^15, q2:M^13, C:M^11, used to control derivative-envelope moments under e M^19 smallness. For the final product E[Q E], it uses the much smaller actual raw L2 incoming bounds M^3,M^2,M and Holder with the envelope's L2 bound. It retains the deterministic B-gate contributions as well. Thus the largest derivative defect is e M^17 and the learned-moment row defect e M^19 dominates. No additional covariance-domination lemma is necessary. Together with the independent positive closure at q<=c M^-12, that separate response result gives total cost e M^31, within the target budget e M^32.

### E.7. Exact active backward-forcing supersolution and inactive sector

Within this proof unit, unqualified section and equation numbers are local.

#### 2. Why diagonal sample sectors suffice for the full theorem

Freference labels and use constant controls (1/2,1/2). Let P denote sample interchange. The initial sample covariance commutes with P, the scalar readout is unchanged by interchange, and the same activation and cap act in both sample slots.

Induct through the actual finite source program. If the previous deterministic coefficients and Gaussian covariances are invariant under simultaneous interchange, then interchanging every sample-indexed root and named source argument interchanges each newly constructed sample pair, while leaving C unchanged. Its law is invariant because the Gaussian covariances are invariant. A learned covariance block consequently satisfies P M P=M. A formal derivative block transforms as P J P by the ordinary chain rule, with the deterministic arrays and covariances frozen; taking expectation therefore gives P E[J] P=E[J]. This proves invariance of the new coefficient blocks and then of the new Gaussian covariances. The induction starts at the exchange-invariant initial Gaussian pair and zero population readout.

Hence every actual deterministic coefficient block, at every amplitude, cap and fixed mesh, is diagonal in the orthonormal (+,-) basis. This assertion does not say that individual random gates are diagonal in that basis. Those gates can mix the two sectors and must be retained in the nonlinear defect estimate.

The two scalar coefficient sectors may therefore be treated separately. All arbitrary temporal backward forcing in each sector, including current diagonals, remains admissible below. No lemma for externally prescribed off-diagonal sample forcing is claimed or needed. The nonsymmetric physical uniqueness assertion is unchanged: it is proved by the original asymmetric raw-state comparison, not by this source-sector reduction.

#### 3. Two products controlled by the positive scaling derivative

All active affine coefficients and learned moments are nonnegative polynomials in beta at a fixed Euler mesh. This is the same Wick-positivity statement proved in Fragment E.5. Their beta derivatives are nonnegative.

Write primes for beta derivatives at a scale beta<=beta_out. Differentiating the scaled coefficient equations and retaining only positive terms yields

    A2_beta' >= 2 beta F_beta,
    A3_beta' >= beta^2 a^2 R_beta A2_beta' L_beta
              >= 2 beta^3 a^2 R_beta F_beta L_beta.

Since R_beta,L_beta>=I entrywise,

    F_beta L_beta <= R_beta F_beta L_beta,
    R_beta F_beta <= R_beta F_beta L_beta.

For every polynomial f with nonnegative coefficients and b>beta>=1,

    f'(beta) <= f(b)/(b-beta).

Indeed f is convex and increasing on [1,infinity), so (b-beta) f'(beta)<=f(b)-f(beta)<=f(b). With b=beta_far, the enlarged coefficient certificate and the M^(-2) scale gap give |A3_beta'|_d<=C M^9. Since a>=1/2, we obtain

    |F_beta L_beta|_d + |R_beta F_beta|_d <= C M^9.       (A)

The estimate is much smaller than multiplying the individual density and row envelopes. It is the positive weight which the direct supersolution uses.

In the active sector K1_kj=a^2 v h_j and K3_kj=a^2 h_j. Positivity also gives

    F_beta,kj >= a^2 v h_j >= c M^(-8) h_j,
    V_beta,kj >= a^4 v h_j >= c M^(-8) h_j.             (B)


#### 4. Exact supersolution for arbitrary active backward row forcing

Fix beta=beta_in. Suppress beta subscripts temporarily. Let E2,E3 be nonnegative strict kernels of density at most q; let J3,J2 be arbitrary nonnegative causal kernels of row norm at most q. In particular J3,J2 may have nonzero current diagonals.

We prove that the forced unit-variance coefficient system

    C <= T0(C)+M_1+(E2,E3,J3,J2)

in the causal comparison sense is dominated by a concrete supersolution whenever q<=c M^(-32). The same conclusion applies to absolute values of a signed solution: the finite polynomial expansions imply |T0(C)|<=T0(|C|).

Set

    A2*=A2_beta, A3*=A3_beta,
    B3*=B3_beta+J3,
    R*=(I-a^2 A2_beta B3*)^(-1),
    W*=a^2 B3* R*,
    B2*=B2_beta+(W*-W_beta)+J2.                       (C)

Every added kernel is nonnegative. The B3 equation is automatically dominated because T depends only on A3, and

    T_beta+M_1,B3+J3 <= B3_beta+J3.

The B2 equation is dominated exactly because

    W*+M_1,B2+J2
      <= B2_beta+(W*-W_beta)+J2=B2*.

Here we used M_beta>=M_1 and beta^2>=1. There is no approximation of the backward forcing and no replacement by strict densities.

The resolvent identities are

    R*=(I-V_beta J3)^(-1) R_beta,
    W*-W_beta=a^2 L_beta J3 R*.

As |V_beta|_r<=C M^11, the first inverse has row norm at most two whenever C M^11 q<=1/2. Thus (A) gives

    |R* F_beta|_d <= C M^9,
    |R*|_r <= C M^11,
    |W*-W_beta|_r <= C M^22 q.                      (D)

Put D_B=B2*-B2_beta. Then

    F_beta D_B F_beta
      = F_beta J2 F_beta
        +a^2(F_beta L_beta) J3 (R* F_beta).

The first sandwich has density at most C M^18 q, while the second has density at most C M^22 q. Dividing entrywise by the lower bound (B) proves

    F_beta D_B F_beta <= eta F_beta,
    eta=C M^30 q.                                  (E)

If eta<=1/2, the finite geometric expansion yields

    F(B2*)-F_beta <= eta/(1-eta) F_beta <=2 eta F_beta.

For clarity, this follows term by term: (F_beta D_B)^n F_beta<=eta^n F_beta, beginning with (E). No operator inverse norm is paid.

Likewise

    V_beta J3 V_beta <= C M^26 q V_beta,

since its density is at most S(CM^7)^2q=CM^18q and (B) costs M^8. Hence

    V(A2*,B3*)-V_beta <= C M^26 q V_beta.

Finally E2<=C M^8 q F_beta and E3<=C M^8 q V_beta. The affine scaled equations leave forward slack

    A2_beta-(F_beta+M_1,A2) >= (beta^2-1)F_beta,
    A3_beta-(V_beta+M_1,A3) >= (beta^2-1)V_beta.

Since beta^2-1>=c M^(-2), the two forward inequalities hold for q<=c M^(-32), after decreasing the universal c. Thus (C) is a supersolution for all four coefficient equations.

A finite induction through the original order A2_k,A3_k,B3_k,B2_k compares any signed actual coefficient solution to this positive supersolution. Its output bounds are

    |A2_actual|<=A2_beta, |A3_actual|<=A3_beta,
    |B3_actual|<=B3_beta+J3,
    |B2_actual|<=B2_beta+(W*-W_beta)+J2,

and the positive backward excess has row norm at most C M^22 q. This comparison does not require entrywise density bounds for J2 or J3.

#### 5. Inactive scalar sector

At the affine inactive reference K3=0, B3_0=B2_0=0, and |A2_0|_d+|A3_0|_d<=C. Both affine backward learned moments vanish. Also K1 has density at most one. The affine learned forward kernels are nonnegative and have bounded density.

For the same arbitrary forcing E2,E3,J3,J2 as above, take

    A2*=A2_0+u H, A3*=A3_0+w H,
    B3*=J3,
    R*=(I-a^2 A2* J3)^(-1),
    B2*=a^2 J3 R*+J2,

where H_kj=h_j for j<k, and u,w are sufficiently large universal multiples of (1+S)q, with the multiple for w larger than that for u.

If C(1+S)q<=1/2 then |R*|_r<=2, |B2*|_r<=3q, and the exact identities

    F*=K1+K1 B2* F*,
    V*=a^2 A2*+(a^2 A2*) J3 V*

give |F*-K1|_d<=C S q and |V*-a^2 A2*|_d<=C S q. The choices of u,w therefore dominate both forward equations. T=0 makes the B3 equation automatic, and B2 was defined to dominate its equation exactly. Consequently

    |B3_actual|_r+|B2_actual|_r <=Cq,
    |A2_actual-A2_0|_d, |A3_actual-A3_0|_d
      <=C(1+S)q <=C M^4 q

in the positive-majorant sense (equivalently, |A_actual| is at most A0 plus the displayed strict kernel). Current diagonals are included throughout.

### E.8. Weighted transfer and distinct-sector closure

Within this proof unit, unqualified section and equation numbers are local.

Write H for the unchanged explicit numerical envelope in Fragment E. In particular H > 10^30 exp(5640). Put

    r=sqrt((1+y1 y2 rho)/2), lambda=a^3 r,
    M=(3/(sqrt(2) lambda))^(1/4), 1/2<=a<=1.

Thus r is between fixed numerical multiples of M^-4. Normalized time is t=lambda s, with steps dt_j=lambda h_j. The common normalized endpoint satisfies T<2 and M>1. All deterministic source coefficient blocks are diagonal in the mean/contrast sample basis by the existing exchange-equivariance proof. Individual random gates need not be diagonal.

#### 1. Weighted affine certificate from the existing actual probes

Fix one of the same beta references as in Fragment E and write

    w(t)=sqrt(beta^2+||D_beta(t)||^2).

It is nondecreasing, at least one, and at most 30M on the common interval. The already proved two-time raw propagator is

    G_beta(t,s) <= exp(2100) [w(t)/w(s)]^3.

The exact independent-root source probes from the reference source certificate are used here. An injected answer at time s costs its local raw norms at s; its output Lipschitz cost uses the raw norms at t. Every primary norm is at most 15w. Therefore, in the active normalized source algebra, the following strict-density bounds hold with one numerical coefficient K=H:

    F(t,s) <= K w(t)^3/w(s)^3;
    V(t,s), W(t,s) <= K w(t)^4/w(s)^2;
    T(t,s) <= K w(t)^3/w(s)^3;
    B3(t,s) <= K [w(t)^3/w(s)^3+w(t)w(s)];
    (R-I)(t,s), (L-I)(t,s) <= K w(t)^4/w(s)^2.       (1)

A notation such as F(t,s) denotes F_kj/dt_j for j<k. Each resolvent has its current identity. For example, the middle transpose probe has injection cost C w(s) and Ap output cost C w(t); the middle forward probe has the same costs with B*D as output. R and L use precisely these same probes with their alternative output, as in the existing certificate. T has unit injection/output costs. The B3 learned-moment density is E[D_t D_s], bounded by w(t)w(s). Hence (1) is about the actual frozen formal source derivatives, not a generic raw tangent substituted for them.

The constants are numerical: the reference 4 exp(2100) Euler/probe factor, products of local bounds 15w, fixed two-sample changes of basis, gains in [1/2,1], and moment additions are below H. K=H also leaves room for all the elementary integrals below. No covariance derivative or covariance square root is differentiated.

The radial inequality c'>=c^3/sqrt(2) after c=1, homogeneity, and duration T<2 give

    integral_0^t w(u) du <= K,
    integral_0^t w(u)^2 du <= K log(exp(1) w(t)),
    integral_0^t w(u)^4 du <= K w(t)^2,
    integral_s^T w(u)^(-2) du <= K w(s)^(-4).        (2)

For the last estimate, if c(s)>=1, use w>=c and dt<=sqrt(2)c^-3 dc to integrate c^-5, then compare w(s) and c(s) by a factor at most two. If c(s)<1, the part up to c=1 has duration at most two, the remaining tail is bounded, and w(s)<=2. The other three statements split at c=1 and integrate c^-2, c^-1 and c respectively. All numerical constants are less than K.

The same inequalities, enlarged by a factor two absorbed in K, hold for sufficiently fine positive Euler meshes. For each fixed M the continuous weights are positive and continuous on a compact interval, so all tail Riemann sums in (2) converge uniformly in their lower endpoint. The mesh may depend on M and beta, but no lower bound on any positive step is used. The finite-program width limit is still taken at fixed mesh.

The current-plus-strict resolvent row estimates following from (1),(2) are

    |R_t|row, |L_t|row <= K^2 w(t)^4.              (3)

The bottom resolvent has row <=K^2 w(t)^3 from its own reference coordinate probe (injection w(s)^2, output one). No improvement to the top forward row is asserted: it can have order M^5. None is needed in this deterministic closure.

### Full weighted source-transfer interface

The additional reference coordinate probes give the following normalized strict densities and complete row bounds, with fixed coefficients at most K^2:

| Transfer | Strict density | Complete row |
|---|---|---|
| R1-I | w(t)^3/w(s) | R1: w(t)^3 |
| R2-I, L2-I | w(t)^4/w(s)^2 | R2,L2: w(t)^4 |
| Rtop-I | w(t)^5/w(s)^3 | Rtop: w(t)^5 |
| Ltop-I | w(t)^3/w(s) | Ltop: w(t)^3 |
| Utop=Rtop A3 | w(t)^5/w(s) | Utop: w(t)^5 |

For R1, add an independent Gaussian field to the first preactivation before its forward calls: the raw update insertion cost is C w(s)^2 and the p output cost one. For Rtop, the xi3 answer injection costs one and the BAp output costs C w(t)^2. For Ltop, inject the top backward answer used in d3, with update cost C w(s)^2, and observe the integrated D state; the current source derivative is identity. The same top-backward probe with BAp output gives Utop and no current identity. These are exactly the reference permitted independent-root probes, now with their time-dependent costs retained.

In original feature time, active forward-transfer rows consequently obey

    F row <=K^3 r w(t)^3,
    V row <=K^3 r w(t)^4,
    Utop row <=K^3 r w(t)^5.                       (3a)

The active backward coefficient rows obey

    B3 row <=K^3 r^-1 w(t)^3,
    B2 row <=K^3 r^-1 w(t)^4.                     (3b)

The B3 moment uses integral w<=K. The B2 moment is bounded by w(t)^2 integral w(s)^2 ds<=K w(t)^2 log(exp(1) w(t))<=C K w(t)^4. All current identities are retained separately in resolvents. Inactive baseline resolvents are identity, all inactive baseline backward coefficients vanish, and inactive F,V,Utop have bounded original strict density and row at most K M^4.

The coefficient arrays A2,A3 also have their learned moments, so their normalized strict densities are respectively bounded by

    K [w(t)^3/w(s)^3+w(t)w(s)],
    K [w(t)^4/w(s)^2+w(t)^2 w(s)^2].              (3c)

On the outer box of Section 3, R1,R2,L2 retain the stated weighted complete-row bounds, while F,V retain both their row and strict-density bounds, by the displayed exact resolvent identities. No strict-density bound is claimed for R1-I or R2-I on this nonlinear box: arbitrary backward row errors need not carry a past-column mesh factor. The strict affine R/L bounds used in Section 2 apply to affine references only. L2 on the nonlinear box has its separately proved strict-right-factor identity in Section 3. Top Rtop,Ltop,Utop only depend on the forward A3 bound and are bounded by the beta2 baseline. Backward coefficient excess R_a adds at most H^-100 M^3 to (3b). Since r^-1 is bounded below by a numerical multiple of M^4 and w(t)>=1, this excess is dominated even by the pointwise right sides of (3b). Thus the weighted incoming source-row bounds persist as well as their global M^7,M^8 consequences. Inactive perturbed forward/transpose transfer rows are O(M^4), and its forward/backward resolvent rows are O(1). A causal inactive backward excess can include current diagonals and need not have a strict density.

#### 2. Two weighted products replace the beta-derivative bound

In the normalized active algebra all gain factors cancel. The exact identities are

    L=I+B3 V,  R=I+V B3,
    F L=F+F B3 V,  R F=F+V B3 F.                  (4)

They hold for the full causal arrays, including the identity returns. Every coefficient in the affine reference is nonnegative. Inserting (1) in the first triple product yields the two integrands

    K^3 [w(t)^3/w(s)^2] w(q),
    K^3 [w(t)^3/w(s)^2] w(u)^(-2) w(q)^5,

integrated over s<q<u<t. The first integral is bounded by T integral w <=2K. In the second, reverse the nonnegative sums/integrals and use

    integral_q^t w(u)^(-2) du <= K w(q)^(-4),

then integral w <=K. Thus

    (F L)(t,s) <= K^6 w(t)^3/w(s)^2.              (5)

For V B3 F the two integrands are

    K^3 [w(t)^4/w(s)^3] w(u),
    K^3 [w(t)^4/w(s)^3] w(u)^(-1) w(q)^4.

Integrate the first directly. In the second use integral_0^u w(q)^4 dq<=K w(u)^2, then integral w<=K. This proves

    (R F)(t,s) <= K^6 w(t)^4/w(s)^3.              (6)

Equations (5),(6) are much stronger than the reference endpoint density M^7. The proof explicitly retains the learned-moment part of B3; dropping that part would give an unjustified estimate.

#### 3. Weighted stability permits a larger active outer radius

Use the same inner/outer beta scales beta1,beta2 from the power-four proof. At beta2 impose the forward inequalities |Aell|<=Aell,beta2. For active backward kernels impose

    |Bell| <= Bell,beta2 + Jell,
    Jell>=0 causal, |Jell|row <= R_a:=H^-100 M^3.  (7)

For the inactive sector impose its affine forward baseline plus density one and backward row radius

    R_i:=H^-100 M^-4.                             (8)

The reference source box had smaller radii. The point is to prove all transfer estimates directly on this larger box.

Normalized backward excess scales as

    J2_hat=(r/a) J2,  J3_hat=ar J3.

Thus every normalized excess row is at most 2r R_a. The positive reference resolvent identities imply

    F*=F_b+F_b J2_hat F*,
    V*=V_b+V_b J3_hat V*,
    R*=R_b+V_b J3_hat R*,
    R1*=R1_b+F_b J2_hat R1*.

For F* use the weight w(t)^3/w(s)^3. The new weighted Neumann ratio is bounded by C r R_a T: the factor w(v)^3/w(u)^3 is at most one when v<=u. For V*, use weight w(t)^4/w(s)^2. Its ratio is bounded by

    C r R_a integral_0^T w(u)^2 du
       <=H^40 r R_a log(exp(1) 30M).                  (9)

The same ratio controls R* with row weight w(t)^4. Since r<=C M^-4 and log(exp(1) 30M)<=C M, (7) makes both ratios smaller than H^-50. Hence the weighted F,V,R,R1 bounds remain at most twice their affine values.

The reverse resolvent is treated with its exact one-sided identity

    L*=L_b+L_b J3_hat V*.

Using the identity-plus-strict decomposition of L_b, the causal bound w(v)<=w(u), and (2) gives row <=2K^2 w(t)^4 after fixed powers of K are enlarged to H^40. The same computation gives its strict-density weight w(t)^4/w(s)^2; the arbitrary current diagonal of J3 is permitted because the right factor V* is strict. This does not assume that multiplication by an arbitrary right row kernel preserves density.

Top transfers depend only on A3 and remain bounded by monotonicity. The active original F and V densities remain respectively O(M^-5) and O(M^-4), hence bounded by the older power-four envelopes. Backward excess R_a=H^-100 M^3 is below their original active baseline envelopes M^9 and M^7. Therefore every full-sample source transfer bound used in the power-four response proof remains valid (indeed several improve).

For the inactive sector, its integration duration is O(M^4), its baseline forward densities are bounded, and (8) gives a Neumann ratio below H^-50. Its reference bounded strict transfers and identity-scale resolvent rows therefore persist.

This proves that (7),(8) are legitimate outer boxes for the existing source moment/derivative proof. Every transfer bound needed by the response calculation, including the complete-row and forward strict-density bounds in (3a),(3b), may be delivered with the single common numerical prefactor H^40; the affine strict-density assertions for R1-I and R2-I are excluded from any nonlinear outer-box claim; the underlying products above are strictly below that envelope. The final response lemma must count that prefactor explicitly. It does not assume that the random gates preserve either sector.

#### 4. Exact supersolution with distinct forcing types

Let E2+,E3+ denote bounds on active forward strict-density defects in original feature time, and J2+,J3+ bounds on active complete causal row defects. The minus superscripts denote the analogous inactive defects. The defects may be signed; take their absolute values before the comparison. Backward current diagonals are included.

Use exactly the reference positive supersolution at beta1:

    A2*=A2_b, A3*=A3_b, B3*=B3_b+J3,
    R*=(I-a^2 A2_b B3*)^-1,
    W*=a^2 B3* R*,
    B2*=B2_b+(W*-W_b)+J2.                         (10)

The backward inequalities hold exactly by affine beta positivity and beta^2>=1. The only forward increments to estimate are

    F_b J2 F_b,
    a^2(F_b L_b) J3 (R*F_b),
    V_b J3 V_b,

plus E2,E3.

We first bound R*F_b in normalized coordinates. From

    R*F_b=R_bF_b+V_b J3_hat(R*F_b),

and (6), its weight w(t)^4/w(s)^3 is stable when

    H^40 r J3+ log(exp(1) 30M) <=1/2.                 (11)

Indeed a causal J3_hat row is at most 2r J3+, and its right argument at v<=u has weight at most w(u)^4/w(s)^3. The remaining integral is integral w(u)^2 du. Thus (6), with twice its constant, applies also to R*F_b.

For the J2 sandwich, the same causal ordering gives in normalized density

    |F_hat J2_hat F_hat|(t,s)
      <=H^40 r J2+ w(t)^3/w(s)^3.                (12)

The integration over its first time variable costs only T<2, because w(v)^3/w(u)^3<=1. For the J3 sandwich, use (5),(6) to get

    |(F_hat L_hat) J3_hat(R*F_hat)|(t,s)
      <=H^40 r J3+ [w(t)^3/w(s)^3] log(exp(1) w(t)).   (13)

The remaining integral is integral w(u)^2 du. These estimates apply unchanged to an arbitrary current diagonal in J2 or J3.

Converting a normalized F-type strict density to original time multiplies by a numerical factor times r^2. As w(t)<=30M and w(s)>=1, (12),(13) therefore imply

    |F J2 F|density <=H^40 M^-9 J2+,
    |(FL) J3(R*F)|density
       <=H^40 M^-9 log(exp(1) 30M) J3+.               (14)

The reference active lower bounds F_kj,V_kj>=H^-2 M^-8 h_j now give relative errors bounded by

    H^45 M^-1 [J2+ + log(exp(1) 30M) J3+].             (15)

For V J3 V, the same causal calculation gives normalized density

    <=H^40 r J3+ w(t)^4/w(s)^2 log(exp(1) w(t)).

Its original density is at most H^40 M^-8 log(exp(1) 30M) J3+, so its relative error is at most H^45 log(exp(1) 30M) J3+. This second-forward error needs M^2 log(M) J3+, one extra M power beyond (15). To retain a simple integer interface below, it is sufficient to charge J3+ M^3.

The direct forward forcing gives relative errors H^2 M^8 E2+ and H^2 M^8 E3+. Available beta slack is at least H^-1 M^-2. Hence all forward inequalities in (10) hold strictly provided

    H^100 [M^10(E2+ + E3+) + M J2+ + M^3 J3+] <=1. (16)

This corrects the preliminary M^2 J3 interface: the V J3 V second-forward term has the larger weighted endpoint w(t)^4. It must not be dropped.

The finite geometric expansion justifying the first-forward comparison is the same reference entrywise argument: if F_b D_B F_b<=eta F_b, then (F_b D_B)^n F_b<=eta^n F_b. Condition (16) makes eta<1/2 and the summed increment below half the beta slack. The V expansion uses its own relative bound in the same way.

#### 5. Backward reconstruction and the inactive sector

The exact backward reconstruction is

    W*-W_b=a^2 L_b J3 R*.

In normalized time R* has row <=H^40 w(v)^4. At a left time u, J3_hat R* thus has row <=H^45 r J3+ w(u)^4. The strict part of L_b has density <=K w(t)^4/w(u)^2, so (2) yields

    |L_b J3_hat R*|row(t)
      <=H^50 r J3+ w(t)^4 log(exp(1) w(t)).

The original B2 conversion cancels r. Therefore

    |W*-W_b|row <=H^55 J3+ M^4 log(exp(1) 30M).        (17)

Under the stronger numerical form of (16) stated below, (17) and the direct J2+ addition are below R_a/2. Thus the forward beta1 reference and all reconstructed backward coefficients lie strictly inside the beta2 box (7). The reference beta derivative lower bound supplies the same strict forward margin H^-3 M^-10 h_j at every positive mesh step.

In the inactive sector K3=0, both affine backward arrays vanish, and the reference exact construction gives

    B3*=J3-, B2*=a^2 J3- R*+J2-,
    A2*=A2_0+u Htime, A3*=A3_0+w Htime,

with

    u<=H^20 [E2- + M^4(J2-+J3-)],
    w<=H^30 [E2-+E3-+M^4(J2-+J3-)].              (18)

To check this, first bound R* by two when its integration-row times J3- is small. Then B2* row is at most 3(J2-+J3-), F*-K1 density at most C S(J2-+J3-), and V*-a^2 A2* density at most C S(J2-+J3-); choose u then w larger than these terms and the direct E forcing. This is a triangular comparison, not a coupled inverse bound. It includes the current backward diagonals.

Consequently the following single typed criterion is sufficient for the complete deterministic supersolution and strict interiority:

    M^10(E2+ + E3+) + M J2+ + M^3 J3+
      + E2-+E3- + M^4(J2-+J3-) <= H^-200.        (19)

Every numerical product above is at most H^55; fixed sums, the beta margin, r-conversion factors, and log(exp(1) 30M)<=10M fit within H^100. The H^-200 criterion leaves at least H^-45 relative slack against the H^-100 outer radii. In particular J3+<=H^-200 M^-3 makes (17) at most H^-140 M^2, below R_a/2; J2+<=H^-200 M^-1 is smaller still. The inactive backward rows from (18) are below R_i/2 and its added forward densities below one half.

The finite chronological A2,A3,B3,B2 comparison applies to actual signed coefficient arrays because |T0(C)|<=T0(|C|). The amplitude-homotopy first-exit argument is therefore uniform in cap and sufficiently fine fixed mesh, exactly as in the existing theorem.


### E.9. Full two-sector nonlinear response, including current returns

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Precise interface and conclusion

Write H for the unchanged explicit numerical constant in Fragment E, so H>10^30 exp(5640). Let

    r=sqrt((1+y1 y2 rho)/2), lambda=a^3 r,
    M=(3/(sqrt(2)lambda))^(1/4), 1/2<=a<=1.

Thus r is between fixed numerical multiples of M^-4 and the original feature duration S is at most M^4. Write w(t)=sqrt(1+||D_0(t)||^2) on normalized affine time t=lambda s. Its beta enlargements have the same estimates, w>=1 and w<=30M. Work at arbitrary cap and a sufficiently fine positive mesh, taking the existing fixed-program limits in their original order.

The independent weighted closure supplies a deterministic sector-diagonal outer box, with all the following transfer prefactors at most H^40:

| Transfer | Active bound | Inactive bound |
| --- | --- | --- |
| F/a^2=U1 strict density | M^-5 | 1 |
| V/a^2=U2 strict density | M^-3 | 1 |
| Utop strict density | M^-1 | 1 |
| F row | M^-1 | M^4 |
| V row | M | M^4 |
| Utop row | M^3 | M^4 |
| R1 row | M^3 | 1 |
| R2,L2 row | M^4 | 1 |
| Rtop row | M^5 | 1 |
| Ltop row | M^3 | 1 |
| B2 row | M^9 | H^-100 M^-4 |
| B3 row | M^7 | H^-100 M^-4 |

The table deliberately weakens several of the new weighted bounds: the sharper active V row is O(1), and B2 row is O(M^8), but neither improvement is needed here. The top local B is E H_c, with active row at most H^5 M^4 and inactive row zero. All backward rows include current diagonals. Inactive resolvents need only the bounded numerical prefactor H^40.

A sufficient condition for the estimates below is

    e H^200 M^16 <= 1.                                      (1)

Let E2+,E3+ denote active forward strict-density forcing, and J2+,J3+ active complete backward row forcing, after subtracting the exact affine formulas at the actual deterministic arrays. Use minus signs for the inactive forcing. Then the complete forcing, including learned moments, obeys

    E2+ <= H^200 e M^3,    E3+ <= H^200 e M^5,
    E2- <= H^200 e M^13,   E3- <= H^200 e M^11,
    J2+ <= H^200 e M^15,   J3+ <= H^200 e M^12,
    J2- <= H^200 e M^3,    J3- <= H^200 e M.                 (2)

The incoming source fields have cap/mesh-uniform subGaussian scales H^94 M^10, H^94 M^9, H^94 M^7 for q1,q2,C. The derivative exponential moments needed by the reference cap-removal bridge are bounded uniformly through order eight. Every constant is numerical and independent of the data, cap, mesh, and width.

#### 2. Weighted raw comparison and actual forward/backward norms

The reference same-state capped field comparison is

    ||V_e(Theta)-V_0(Theta)||raw <=40 e (R(t)+1)^3,

and its radius-one affine propagator is

    G(t,u)<=exp(2100)[w(t)/w(u)]^3.

All primary affine norms are at most 15w. Variation of constants in normalized time therefore gives

    E(t):=||Theta_e(t)-Theta_0(t)||raw
       <=40(e/lambda) exp(2100) w(t)^3
          integral_0^t [(R(u)+1)/w(u)]^3 du
       <=H^5 (e/lambda) w(t)^3.                            (3)

Here (R+1)/w is numerically bounded and T<2. Condition (1) closes the raw radius-one tube. This comparison is on arbitrary nearby raw states: it does not assume that nonlinear inactive fields freeze. The finite-mesh estimate follows by discrete variation of constants and uniform Riemann approximation on the fixed compact M-dependent interval; all constants remain cap uniform.

The affine inactive Gaussian fields have bounded norms, whereas the active forward fields have norms at most C r w, C r w^2, C r w^3 at the three layers. Hence each affine sample forward field has norm at most H. Direct propagation of (3) gives samplewise forward differences at most H^6(e/lambda)w^3, H^6(e/lambda)w^4, H^6(e/lambda)w^5. Under (1), actual H1,H2,H3 therefore have bounded L2 norms, say H^10.

There is a stronger active estimate. For odd 1-Lipschitz arctan, set

    Psi(P,Q)=[atan(P+Q)+atan(P-Q)]/2.

Then |Psi(P,Q)|<=|P| pointwise, since it is half the difference of atan(Q+P) and atan(Q-P). The first active preactivation is exactly r p_e even in the nearby nonlinear state: projection onto the normalized active input direction has norm at most its raw first-layer norm. Therefore

    ||H1,e,+-H1,0,+||2 <=C r(E+e w)<=H^10 e w^3,
    ||H2,e,+-H2,0,+||2 <=C r(w E+e w^2)<=H^10 e w^4.     (4)

For the second line propagate the first through A_e, compare the affine A_0 action, and again use |Psi|<=|P|. No product of arbitrary unbounded L2 functions is estimated in this step. In particular (1) gives

    ||H1,e,+||2 <=H^10 r w,
    ||H2,e,+||2 <=H^10 r w^2.                            (5)

Indeed the relative error in (4) is bounded by H^10 e M^6, which (1) makes small.

Raw operator bounds and bounded capped gates give

    ||q1||2<=H^10 w^3, ||q2||2<=H^10 w^2, ||C||2<=H^10 w. (6)

Backward contrast has an extra e without any source-tail assumption. The readout C is common to both samples, and

    delta3,- = (e/2) tau(C)[g(Z3,1)-g(Z3,2)],

where g(z)=(1+z^2)^-1 and |tau(q)|<=|q|. Thus ||delta3,-||2<=C e w. Applying B_e^* gives ||q2,-||2<=C e w^2. The exact formula delta2=a q2+e g(Z2)tau(q2) then gives

    ||delta2,-||2<=H^10 e w^2,
    ||delta3,-||2<=H^10 e w.                             (7)

These identities retain the cap and require no Gaussian covariance domination. At each fixed program the actual raw L2 norms are the norms of the corresponding named source output laws, by the original construction.

#### 3. Learned-moment forcing

The four learned moments are exactly h_j times the two-time covariances of H1,H2,delta3,delta2, with fixed gain/sample factors already recorded in the preceding source normalization. Those factors are bounded by H. For active forward moments, (4),(5) imply

    MA2,+ discrepancy density <=H^30 e r M^4 <=H^35 e,
    MA3,+ discrepancy density <=H^30 e r M^6 <=H^35 e M^2. (8)

For example the first covariance difference is bounded by
C e r[w(t)^3 w(s)+w(t)w(s)^3], using the actual and affine active norms. The second has the analogous powers four and two. The inactive (and full-sample) forward discrepancies satisfy the sufficient bounds H^35 e M^7 and H^35 e M^8, from (3) and the bounded actual forward norms.

Backward differences obey

    ||delta3,e-delta3,0||2 <=H^15(e/lambda)w^3,
    ||delta2,e-delta2,0||2 <=H^15(e/lambda)w^4.             (9)

The second estimate expands B_e^*delta3,e-B_0^*delta3,0 and the bounded gate correction. In particular it uses only bounded operators on L2.

The radial estimates imply

    integral_0^t w <=H,
    integral_0^t w^2 <=H log(exp(1) w(t)),
    integral_0^t w^3 <=H w(t),
    integral_0^t w^4 <=H w(t)^2.                          (10)

They follow by splitting at ||D||=1 and using c'>=c^3/sqrt(2); all are uniform on the common enlarged interval and sufficiently fine meshes.

At fixed terminal t, (9) and the product difference inequality give for the top backward learned row

    H^30 e lambda^-2 [w(t)^3 integral w(s)ds
                     +w(t) integral w(s)^3 ds]
       <=H^35 e M^11.                                  (11)

The integrals here use normalized time. The two lambda^-1 factors come respectively from (9) and original feature-time integration. The middle backward learned row is at most

    H^30 e lambda^-2 [w(t)^4 integral w(s)^2ds
                     +w(t)^2 integral w(s)^4ds]
       <=H^35 e M^12 log(exp(1) 30M)<=H^40 e M^13.           (12)

These estimates hold for either sector and every terminal row. They are stronger than using a supremum density times the whole duration.

For the inactive backward moments use (7), since the affine counterpart vanishes identically. Their rows are at most H^35 e^2 M^6 log(exp(1) 30M)<=H^40 e^2 M^7 at middle, and H^35 e^2 M^5 at top. They are smaller than the inactive bounds claimed in (2) under (1).

#### 4. Actual sector Gaussian scales and improved source tails

The primitive Gaussian source covariances are the actual feature/backward L2 covariance matrices. Combining (5),(7) with the initial root gives the following standard deviations, with prefactor at most H^10:

| Source | Active | Inactive |
| --- | --- | --- |
| Z1 initial | r | 1 |
| zeta1 | M^2 | e M^2 |
| xi2 | M^-3 | 1 |
| zeta2 | M | e M |
| xi3 | M^-2 | 1 |

These estimates preserve arbitrary time correlations and singular covariance matrices. They are direct bounds on each Gaussian variable; no covariance square-root derivative or independence between times is used.

The exact same-array source value identities are

    Z1=R1 Z1,initial+(F/a)zeta1
         +e(F/a^2)[d1+a B2 atan(Z1)],
    Z2=R2 xi2+(V/a)zeta2
         +e(V/a^2)[d2+a B3 atan(Z2)],
    Z3=Rtop xi3+e Utop[d3+a E H_c atan(Z3)].              (13)

Here |d_l|<=|q_l| (or |C| at top). Solve the linear Gaussian part separately in each deterministic sector. At bottom the active costs are M^3 r and M^-1 M^2, hence at most M; its inactive cost is 1+e M^6. At middle the active costs are M^4 M^-3 and M M, hence at most M^2; its inactive cost is 1+e M^5. At top the active cost is M^5 M^-2=M^3 and its inactive cost is bounded.

The nonlinear terms may be bounded in the full sample norm. With p>=2, writing Z_l,p for the supremum of the individual Lp norms rather than a random time supremum, the resulting inequalities are

    Z1,p <=H^51 M sqrt(p)+ e H^81 M^13 Z1,p,
    Z2,p <=H^51 M^2 sqrt(p)+e H^81 M^11 Z2,p,
    Z3,p <=H^51 M^3 sqrt(p)+e H^81 M^8 Z3,p.             (14)

The bounded-atan additive terms are covered under (1). For instance at bottom the largest nonlinear self product is the full F row M^4 times B2 row M^9. Each transfer has coefficient H^40, so H^81 covers the product and fixed gains. Gaussian prefactors H^10 and one transfer H^40 fit H^51 after the fixed gains and sums.

Absorption yields Z1,p,Z2,p,Z3,p bounded by H^52 times M,M^2,M^3 times sqrt(p). Substitution into

    q1=zeta1+B2(aZ1+e atan Z1),
    q2=zeta2+B3(aZ2+e atan Z2),
    C=H_c(aZ3+e atan Z3)

gives incoming Lp and subGaussian bounds with coefficient at most H^94 and powers

    q1: M^10, q2: M^9, C: M^7.                          (15)

The subGaussian assertion follows by expanding exp(Q^2/L^2) and using the even-p estimates. It does not assert that an arbitrary bounded L2 action preserves tails.

#### 5. Exact derivative equations and a two-sector majorant

For any one local population use

    Z=xi+K delta, q=zeta+B Hfeat,
    Hfeat=phi(Z), delta=Dcap(Z,q),
    R=(I-a^2KB)^-1, U=RK, L=(I-a^2BK)^-1.

The pairs (K,B) are (H_P,B2),(A2,B3),(A3,E H_c). With deterministic arrays and covariances frozen, the exact identities from the reference proof are

    J=Jaff+U[DeltaV I_zeta+P J],
    Ddelta-Ddelta_aff=L[DeltaV I_zeta+P J],
    Jaff=R I_xi+a U I_zeta,
    P=Lgate+a DeltaV B+a B DeltaG+DeltaV B DeltaG.         (16)

In original sample coordinates G=aI+DeltaG and V=aI+DeltaV are diagonal gates, and Lgate=e diag(g'(Z)tau(q)). In the mean/contrast basis they need not be diagonal. Every entry of DeltaG,DeltaV has modulus at most C e and every entry of Lgate at time k is at most C e Q_k. The deterministic B,U,R,L are sector diagonal. Thus, writing b=9,7,4 at the three populations, all blocks of P are bounded by the local curvature e Q and causal gate terms e H^40 M^b. Crucially the -- block has the sharper structure

    P-- = Lgate-- + a DeltaV-- B- + a B- DeltaG--
          + DeltaV-- B- DeltaG-- + DeltaV-+ B+ DeltaG+-. (17)

The large B+ enters (17) only with two e factors. This identity retains the full current B diagonal and is valid at every finite mesh.

Let q_sg=10,9,7 be the powers in (15), and put

    I_k=sum_{r<k} h_r[Q_r+H^40 M^b],
    E_k=exp(e H^81 I_k).                                (18)

The intentionally larger H^81 rate covers all full and sector majorants below. By weighted Jensen, the subGaussian scales (15), and S<=M^4, moments through order eight of E_k are at most two under (1). Indeed the largest coefficient before fixed-moment factors is e H^175 M^14: 81+94=175 and 4+10=14. The spare H^25 M^2 in (1) handles every fixed constant. No random supremum over source times is introduced. Also ||I_k||p<=H^96 M^(4+q_sg) sqrt(p), for each fixed p used below.

For completeness, a smaller rate H^45 is sufficient if the factor H^40 multiplying B is kept inside I as written; H^81 is convenient for the moment ledger but must not be charged twice in cross-generation constants. In subsequent cross estimates use this sharper H^45 rate. It comes from U's H^40 coefficient, fixed two-sample sums/gains, and the full causal row bound on B already included in I. The same E in (18) dominates this smaller-rate majorant.

Here is the precise sector estimate for a single transpose source in active sector at slot j. Let u=M^-5 at bottom and u=M^-3 at middle. After padding histories by zeros, the positive running-maximum inequality is bounded by the rank-one two-by-two matrix

    K_u = diag(u,1) [[1,1],[1,1]].

Its scalar increasing clock is e H^45 I_k. The direct source column is bounded by H^45 h_j (u+e u,e). A finite causal product is bounded entrywise by the corresponding matrix exponential; K_u^2=(1+u)K_u and 0<u<=1. Therefore

    |J++,kj| <=H^50 u h_j E_k,
    |J-+,kj| <=H^100 e h_j(1+u I_k) E_k.                (19)

One can verify (19) directly using exp(tK_u)=I+[(exp((1+u)t)-1)/(1+u)]K_u. This is an elementary matrix causal majorant, not a diagonal-gate assumption. Chronological B terms are bounded by their row norms times the past running maximum; strict U supplies h_r and the time ordering. Every single transpose-source term retains h_j and vanishes for k<=j.

At the fixed moments used below, (19) implies cross-derivative bounds H^200 e h_j M^9 at bottom and H^200 e h_j M^10 at middle, with its explicit envelope retained. The explicit coefficient H^196 follows from the displayed H^100 cross prefactor and H^96 clock moment. We use H^196 in the numerical products below; H^200 is only the final rounded interface.

For an inactive full forward-source column, the direct affine derivative has row in the inactive sector at most H^40 and its active part is zero. The same matrix formula, now with no DeltaV I_zeta term, gives

    |J--,k,row| <=H^50 E_k,
    |J+-,k,row| <=H^95 e u I_k E_k.                     (20)

At middle u=M^-3, q_sg=9; at top u=M^-1, q_sg=7. In both cases the cross derivative has fixed-moment size at most H^196 e M^10. Current forward-source identity terms remain in J--; (20) does not discard them.

Finally, for arbitrary full forward-source rows the reference scalar majorant gives base H^50 M^4 at middle and H^50 M^5 at top, times E_k. For each pair of times the actual raw L2 bounds (6) and Holder give

    E[Q_r E_k]<=H^12 M^2 at middle,
    E[Q_r E_k]<=H^12 M at top,                         (21)

and H^12 M^3 at bottom. Independence is unnecessary. Products containing a cross derivative use its I_k factor and the fixed source moments (15), with Holder and the available eighth exponential moment.

#### 6. Forward derivative forcing

Consider a single active transpose source. In the ++ part of (16), the direct bounded-gate source term is at most C e u h_j. For the diagonal return use (19), (21), and the B+ row. Its expected strict density is bounded by

    C e u^2 S [M^qraw+M^b],

where (u,qraw,b)=(M^-5,3,9) or (M^-3,2,7). These powers are e M^3 at bottom and e M^5 at middle.

For the cross return, use the second line of (19), the source moments (15), and Holder. Its bounds are

    H^350 e^2 M^18 at bottom,
    H^350 e^2 M^20 at middle.                          (22)

The powers are respectively -5+4+10+9 and -3+4+9+10: strict active U, time duration, incoming subGaussian Q (which dominates B), and the first cross generation. Direct offdiagonal source injection and terminal feature gate contributions are smaller. By (1), (22) is at most H^150 e M^2 and H^150 e M^4. Multiplication by the terminal feature gate G adds its diagonal O(e) difference and the offdiagonal e J-+ term; both are covered by the preceding bounds.

Thus active derivative forcing is at most H^180 e M^3 and H^180 e M^5. Adding (8) gives the active E bounds in (2).

For inactive forward forcing, the previous full-sample single-transpose proof is already sufficient. It uses U full density O(1), the raw L2 bound (21), and deterministic B rows, hence gives H^180 e M^13 and H^180 e M^11. The source-envelope premise is now (18), valid under (1). Adding inactive learned forward moments from Section 3 leaves these bounds unchanged. A sharper inactive argument is possible but unnecessary for the closure interface.

#### 7. Backward derivative forcing, including current returns

For an active full forward-source row, apply the second identity in (16) before taking norms. At middle L+ has row M^4 and J has base M^4; at top they have powers M^3 and M^5. The bounded-gate terms retain the full B row, and (21) controls the single curvature factor. Consequently

    middle active defect <=H^180 e M^(4+4+7)=H^180 e M^15,
    top active defect <=H^180 e M^(3+5+4)=H^180 e M^12.   (23)

This controls the sum of absolute expected entries by the expected absolute row for each terminal time, then takes the terminal-time supremum outside expectation. No random time maximum is asserted. Learned rows (11),(12) are smaller than (23).

For an inactive forward-source row, L- has bounded row and use (17),(20). The curvature term in P-- J-- costs H^140 e M^2 at middle and H^140 e M at top, by (21). The B- terms cost at most H^140 e because its row is small. The two-offdiagonal diagonal gate term costs H^140 e^2 M^7 at middle and H^140 e^2 M^4 at top.

The remaining cross return P-+ J+- has, by (15),(20), bounds

    H^350 e^2 M^19 at middle,
    H^350 e^2 M^17 at top.                            (24)

Here the cross derivative has power ten, and the final incoming source powers are nine and seven. Under (1), (24) is bounded by H^150 e M^3 and H^150 e M. Thus the inactive backward defects are bounded by H^180 e M^3 and H^180 e M. The quadratic inactive learned rows from Section 3 are smaller.

Equations (17),(20) include j=k: the inactive direct forward-source identity is retained; L includes its identity; all B diagonal terms are included; and U alone is strict. Arbitrary causal row excess may concentrate on an arbitrarily short past step. No minimum step or backward strict-density assumption is used anywhere.

#### 8. Numerical ledger and consequence

Here is one consistent rounded ledger accounting for the delivered H^40 transfer prefactors:

| Item | Prefactor sufficient |
| --- | --- |
| Weighted primal norms, actual Gaussian input scales | H^10 |
| Value leading terms; self products | H^51; H^81 |
| Absorbed Z1,Z2,Z3 | H^52 |
| Incoming Lp/subGaussian scales | H^94 |
| Clock fixed moments | H^96 |
| Global derivative exponential rate | H^81 |
| Sharper rate for cross-generation bookkeeping (B coefficient inside I) | H^45 |
| Direct derivative bases | H^50 |
| Single-insertion derivative defects | H^140 |
| One cross derivative, including its clock moment | H^196 |
| Two-insertion defects before amplitude reduction | H^350 |
| Two-insertion defects after e H^200 M^16<=1 | H^150 |
| Learned moments and all final forcing after fixed sums | H^200 |

Every entry comes from the displayed finite products. For example the incoming scale is H^52 times the B-row H^40 plus fixed sums, hence H^94. The global envelope coefficient is H^(81+94)=H^175 before fixed factors and duration, covered by H^200. A cross derivative uses the direct H^50, sharper rate H^45 and clock H^96, fitting H^196. Returning it through U or L (H^40), one incoming source (H^94), and fixed sums gives at most H^335, below H^350. Single-insertion products use at most two H^40 resolvents/transfers, one H^50 derivative base and fixed sums, fitting H^140. Multiplying a two-insertion term e^2 H^350 by (1) removes H^200 and sixteen M powers, leaving e H^150. These numerical margins avoid treating a saturated H^40 prefactor as if it were H.

The independent typed closure criterion is

    M^10(E2+ +E3+) + M J2+ + M^3 J3+
       +E2-+E3-+M^4(J2-+J3-) <=H^-200.                (25)

Inserting (2) gives a left side at most 8 H^200 e M^16. Thus a sufficient single selection is

    8 H^400 e M^16 <=1.                              (26)

It implies the moment/response condition (1) as well. Since M^16<=24^4 delta^-2, the unchanged prefactor

    c_poly=min{1/4,c_*,10^-70 H^-400}

and e<=c_poly delta^2 give 8 H^400 e M^16<=8*10^-70*24^4<1. The numerical factor 24^4 is retained explicitly; replacing it by H would needlessly exhaust the exact H budget.

By the weighted closure proof E.8, (25) excludes every first exit along the cap/mesh amplitude homotopy. The reference primal endpoint/nonaffinity hypothesis e<=c_*delta^(7/4) is implied by delta^2. The original cap removal, autonomous global physical flow, nonsymmetric uniqueness/restart, full-sequence GF/raw-GD population limits, kernels/actions/adjoints, same-layer path/velocity laws and moments, and original initial-motion certificates then use exactly their reference bridges. No further smallness condition or change of model is introduced.

This interface therefore suffices for both delta^3 and delta^2. Its mathematical boundary is the independent weighted affine/outer-box/typed-closure certificate; no claim is made here about three inputs or exponents below two.

### E.10. Odd-family cap and finite-algorithm bridge

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Precise extended source statement

Let

\[
\phi_{a,e}(z)=az+e\arctan z,\qquad
\tfrac12\le a\le1,\quad 0\le e\le1,
\]
\[
D_{a,e,R}(z,q)=a q+e g(z)\tau_R(q),\qquad g(z)=(1+z^2)^{-1}.
\]

Use the existing smooth odd clips: \(|\tau_R|\le\min(|q|,2R)\),
\(|\tau_R'|\le1\), and \(\tau_R(q)=q\) for \(|q|\le R\).
Let there be two samples, a PSD unit-diagonal correlation matrix \(\Gamma\),
a deterministic positive mesh of total duration at most \(S>0\), and
frozen controls \(c_k\in\mathbb R^2\) with \(\|c_k\|_1\le1\).
Write \(P_k=\Gamma\operatorname{diag}(c_k)\), so \(|P_k|_\infty\le1\).

Assume the actual affine Euler programs, with activation \(az\), the SAME
control sequence and mesh, obey the finite-array primal hypothesis
\(\mathsf P(P,S)\), with \(P\ge1\), from baseline equation (18). Bounds
are required at each fixed mesh on events of probability tending to one;
a uniform probability assertion over growing transcripts is unnecessary.

There are \(E_*(P,S)>0\) and \(K(P,S)<\infty\), independent of
\(a\in[1/2,1]\), correlation, controls, meshes, and caps, such that, for
\(0\le e\le E_*\), the actual canonical nonlinear source programs have
bounded forward response blocks and backward response time rows, and

\[
\sup_{k,R}\left(\|C_k\|_p+\|q_k^2\|_p+\|q_k^1\|_p\right)
\le K\sqrt p,\qquad p\ge2.
\]

The same holds for the forward fields and deltas. This is a population
source assertion, not a uniform exponential-moment assertion for every
finite-width neuron. The lower gain bound 1/2 is not needed by this lemma;
it is useful in the separate affine/nondegeneracy arguments.

The proof is the controlled response proof with the following verified
changes. No covariance inverse or positive constant offset occurs.

#### 2. Source representation and affine coefficients

Keep controlled-response equations (8)–(9) exactly, with two sample slots,
\(H=\phi_{a,e}(Z)\), and \(\delta=D_{a,e,R}(Z,q)\). Covariances are full
second moments of the actual matrix-input fields. A zero feature mean is
allowed; singular source covariances, including the zero initial reverse
sources, are treated by the existing independent-query regularization.
Formal source arguments stay distinct at rank drops. The generic
conditioning theorem requires globally Lipschitz C1 coordinate maps with
bounded first derivatives at fixed cap, and iid initial root tuples with
finite second moments independent of the Gaussian matrices. Here

\[
|\phi'_{a,e}|\le2,\quad |D_q|\le2,\quad |D_z|\le2eR,
\quad |\phi_{a,e}(z)|\le |z|+\pi/2.
\]

These verify the hypotheses. Removing the affine constant does not remove
any source or learned-memory term. In particular the coefficients remain

\[
\mathsf A^\ell_{ki,vj}
=E\partial_{\zeta^{\ell-1}_{v,j}}H^{\ell-1}_{k,i}
+h_v c_{v,j}E[H^{\ell-1}_{k,i}H^{\ell-1}_{v,j}],
\]
\[
\mathsf B^\ell_{ki,vj}
=E\partial_{\xi^\ell_{v,j}}\delta^\ell_{k,i}
+\mathbf1_{v<k}h_vc_{v,j}E[\delta^\ell_{k,i}\delta^\ell_{v,j}].
\]

All deterministic controls, arrays and covariances are frozen in these
formal derivatives. Finite empirical-feedback identification is causal
and uses their converging contractions, not derivatives of the controls.
For the present two-label scalar feature path one simply takes constant
\(c_i=y_i/2\).

At e=0 the equations are linear in the source arguments, with affine
identity gates replaced by aI. For example
\(\delta^3=aC\), \(\delta^2=a^2 B^*C\), and
\(\delta^1=a^3A^*B^*C\). On a primal ball of radius b>=1, every affine
forward/backward norm, state Lipschitz estimate, answer-perturbation
estimate, and output Lipschitz estimate used in baseline Sections 5–7 is
bounded above by its displayed a=1, offset=1 bound. This assertion follows
term by term: the removed affine constant contributed only nonnegative
addends to the norm estimates, and every additional gain is in [0,1].
In particular the raw affine field is 9b^2-Lipschitz and bounded by
10b^3 in the existing sum norm. The four answer perturbation constants
2b, 1, 3b, 1 from the baseline table remain valid. Their Gaussian probe
identity is unchanged: the program is affine in the new independent
Gaussian root, whether its deterministic affine constant is zero or not.
It yields the same mesh factors and row sums.

Put \(F=\exp(36P^2S)\). For constant \(c_i=y_i/2\), admissible block/time-row
bounds are exactly the existing ones:

\[
A_0=2(24P^2F+\tfrac92P^4),\qquad
M_0=2S(8P^2F+P^4).
\tag{1}
\]

For arbitrary frozen controls with \(\|c_k\|_1\le1\), the conservative
choice \(A_0=2(24P^2F+9P^4)\), with the same \(M_0\), avoids the
individual bound \(|c_i|=1/2\) in baseline equation (29). Either choice
is uniform in a. The factor 2 converts scalar output rows into the sum of
maximum row-sum norms of two-by-two time blocks.

If a bounded continuous affine reference has projected primal bound U,
then sufficiently fine population Euler arrays have bound 2U by the
9b^2 bounded-ball Euler estimate. Baseline Section 8 still gives the
finite-array premise with

\[
P=11+2U+4S(2U)^3.
\tag{2}
\]

Indeed initial finite operator norms are at most 10 with probability
approaching one; exact rank-one unrolling bounds learned operator
increments by the finite sums of update-factor RMS products. Their
population limits have the reference upper bounds 2S(2U)^3 and 3S(2U)^3, and
are smaller for the zero-offset affine activation. This does not infer
operator-norm convergence of trained matrices.

#### 3. Uniform primal perturbation and derivative closure

At a common state of primal size at most b>=1, the original conservative
same-state table remains valid, uniformly in a and cap:

\[
\begin{array}{c|ccc}
 &1&2&3\\ \hline
\|H_e^\ell\|_2&4b&7b^2&10b^3\\
\|H_e^\ell-H_0^\ell\|_2&2e&4eb&6eb^2
\end{array}
\]
\[
\|\delta_e^3\|_2\le2b,\quad
\|\delta_e^2\|_2\le4b^2,\quad
\|\delta_e^1\|_2\le8b^3,
\]
\[
\|\delta_e^3-\delta_0^3\|_2\le eb,\quad
\|\delta_e^2-\delta_0^2\|_2\le3eb^2,\quad
\|\delta_e^1-\delta_0^1\|_2\le7eb^3.
\]

For example the middle backward difference is at most
\(a\|q_e^2-q_0^2\|_2+e\|q_e^2\|_2\le eb^2+2eb^2\).
The four raw-update differences are at most 7,14,11,6 times eb^3,
by the rank-one HS norm inequality. Thus

\[
\|V_{a,e,R,c}(\theta)-V_{a,0,c}(\theta)\|_{\mathcal X}
\le40eb^3,\qquad \|V_{a,e,R,c}\|_{\mathcal X}\le50b^3.
\tag{3}
\]

These also hold in finite normalized norms. Comparison with the affine
field, using only that field's 9b^2 Lipschitz constant, gives

\[
\sup_{s_k\le S}\|\theta^e_k-\theta^0_k\|_{\mathcal X}
\le40eb^3S\exp(9b^2S).
\tag{4}
\]

For the finite-array premise \(\mathsf P(P,S)\), take b=2P. A sufficient
restriction for discrepancy at most P/2 is

\[
e\le [640P^2S\exp(36P^2S)]^{-1}.
\tag{5}
\]

This is a deliberately conservative replacement of the original 480
restriction, consistent with using 40 instead of the sharper 30 in the
perturbation source. For a continuous reference of bound U and b=4U,
(4) supplies the raw strong comparison with
\(Q=40b^3S\exp(9b^2S)\), precisely as in the two-input proof.
All actual source variances are now bounded independently of cap, mesh,
and a; for example the oversized scalar standard-deviation bound
\(\sigma=8b^3\) suffices on the closed primal ball.

For the response induction write A=A_0+1 and M=M_0+1. The derivative
matrices are exactly

\[
G=aI+e\operatorname{diag}(g(Z)),\quad
V=aI+e\operatorname{diag}(g(Z)\tau_R'(q)),\quad
L=e\operatorname{diag}(g'(Z)\tau_R(q)).
\]

Hence \(|G-aI|,|V-aI|\le e\), \(|L|\le eQ_r\), and all upper derivative
bounds are the a=1 bounds with d_a=a+1 replaced by 2. The exact affine
recursions (11) and all-index recursions (17) of the controlled-response
proof remain exact. The offset had derivative zero, so it never occurred
in them. Its moment inequalities (19) remain upper bounds, since the
constant term in \(|H|\) decreases from a+e*pi/2 to e*pi/2. No monotonicity
of an actual trajectory in a is asserted or needed.

More explicitly, choose K0 depending only on sigma large enough to bound
every pair of Gaussian-source coordinates by K0*sqrt(p). The reference
Volterra moment bounds may be replaced by the following uniform bounds:

\[
\max_{v\le k}\|H_v^1\|_p
\le K_0(1+2S)e^{2MS}\sqrt p,
\]
\[
\max_{v\le k}\|H_v^2\|_p
\le K_0(1+2AS)e^{2AMS}\sqrt p,
\qquad
\max_{v\le k}\|C_v\|_p
\le K_0 S e^{2AS^2}\sqrt p.
\tag{6}
\]

Enlarge K0 to absorb the bounded arctangent terms. The two q norms then
use \(\|q^i_k\|_p\le K_0\sqrt p+M\max_{v\le k}\|H_v^i\|_p\).
These give a cap/mesh/gain-uniform subGaussian Q_r. The derivative envelope
is \(\exp\{Ks_k+Ke\sum_{r<k}h_rQ_r\}\); backward outputs retain the
necessary current factor \(K(1+eQ_k)\). Its finite moments follow from
these subGaussian bounds and the convexity inequality in Section 3.4 of
the controlled-response proof, without a random supremum over time.

The exact same-array affine bounds (21) in that proof can be replaced by

\[
K_F=e^{MS},\quad K_V=Ae^{AMS},\quad
K_U=e^{AMS},\quad K_T=Se^{AS^2}.
\tag{7}
\]

They dominate their displayed gain-dependent formulas. Likewise each
coefficient in inequalities (22)–(26) is dominated by the expression
obtained by setting all unindexed a and a^2 equal to one. The perturbative
forcing estimates remain Ke*h_j for one transpose-source slot and Ke
for a full forward-source row. All current L_k J_k contributions are
retained and have expectation O(e) by (6) and the envelope moments.

Consequently the literal chronological order

\[
\alpha_k^2,\quad \alpha_k^3,\quad \beta_k^3,\quad \beta_k^2
\]

satisfies, with one K=K(P,S,A_0,M_0)>=1 independent of a,

\[
\alpha_k^2,\alpha_k^3,\beta_k^3,\beta_k^2
\le K(e+I_k),\qquad
I_k=\sum_{r<k}h_r(\beta_r^2+\beta_r^3),
\]
\[
E_k:=\beta_k^2+\beta_k^3
\le Ke+K\sum_{r<k}h_rE_r.
\tag{8}
\]

K is chosen from the finite displayed algebra and the just-bounded
envelope moments with a replaced by its upper bound; it is not a
pointwise threshold later optimized over a. Discrete Gronwall and the
four-stage induction of the supplied proof now apply verbatim. An
admissible uniform response threshold is

\[
E_*(P,S)=\min\left\{1,
\frac1{640P^2S e^{36P^2S}},
\frac1{2K e^{KS}}\right\}>0.
\tag{9}
\]

The current returns still are

\[
(\mathsf B^3_{kk})_{ij}=\mathbf1_{i=j}EL^3_{k,i},
\]
\[
(\mathsf B^2_{kk})_{ij}=\mathbf1_{i=j}EL^2_{k,i}
+(\mathsf B^3_{kk})_{ij}E[V^2_{k,i}G^2_{k,j}].
\]

They are O(e); they are neither discarded nor inverted. This proves the
extended controlled source lemma with the stated quantifiers.

#### 4. Cap removal and global physical conversion

For R'>=R, allowing R'=infinity, the exact asymmetric difference is

\[
\begin{aligned}
D_{a,e,R'}(z_A,q_A)-D_{a,e,R}(z_B,q_B)
={}&a(q_A-q_B)\\
&+e g(z_A)[\tau_{R'}(q_A)-\tau_{R'}(q_B)]\\
&+e[g(z_A)-g(z_B)]\tau_R(q_B)\\
&+e g(z_A)[\tau_{R'}(q_B)-\tau_R(q_B)].
\end{aligned}
\]

Its L2 norm is at most

\[
2\|q_A-q_B\|_2+2eR\|z_A-z_B\|_2
+2e\||q_B|\mathbf1_{|q_B|>R}\|_2.
\tag{10}
\]

The original 4eR bound also remains safe. Successive substitution through
forward propagation and the three backward gates yields exactly the
reference form

\[
\|V_{R'}(\theta_A)-V_R(\theta_B)\|_{\mathcal X}
\le C_b(1+eR)\|\theta_A-\theta_B\|_{\mathcal X}
+C_be\sum_Q\||Q_B|\mathbf1_{|Q_B|>R}\|_2.
\tag{11}
\]

C_b can be independent of a. There is one factor R, not its third power:
only a forward-state difference gets the R coefficient at a gate; an
incoming backward discrepancy is multiplied by at most 2.
The source lemma gives Gaussian L2 tails for the reference Q. Therefore
cap paths and their raw directions converge strongly on the complete
fixed feature interval, with error bounded by
\(C\exp(C(1+eR)S-cR^2)\). The asymmetric estimate compares any other
bounded-primal uncut strong solution to the cap reference and requires
no tails of the competitor. It proves uniqueness, including restart
from any reached state, on the same generated action spaces.

For the physical bridge the following are sufficient additional inputs
from the new scalar-symmetry argument:

1. The feature flow and every cap feature flow satisfy f_i=y_i*g,
   with g(0)=0, on a bounded interval [0,S].
2. The uniform raw comparison gives g_R(S)>1, for every cap and for
   the uncut path.

**No nonlinear radial lower bound is needed for global physical
existence at this stage.** Let s_R be the first hit of 1. Continuity
implies g_R(s)<1 for s<s_R. Boundedness of its derivative gives
\(1-g_R(s)\le M_R(s_R-s)\). Hence

\[
t_R(s)=\int_0^s\frac{du}{2(1-g_R(u))}
\]

diverges as s approaches s_R. Its inverse solves ds/dt=2(1-g_R), and
reparametrizes the feature path into the exact two-residual physical
field for all finite times. Monotonicity of g_R is unnecessary; the
capped feature field need not be a gradient. The argument equally
applies to the uncut path. Uniform compact primal bounds and reference
incoming tails are inherited from the complete feature interval.
Physical-field local Lipschitzness at fixed cap follows from (11) and
the locally Lipschitz prediction contractions. On every fixed physical
[0,T], (11) has the same form, with constants depending on T. The
Gaussian tail defeats exp(C_T R) for every finite T, without further
smallness of e. Uniqueness against nonsymmetric physical competitors
uses their individual residuals in this physical estimate, and does
not assume their scalar symmetry.

#### 5. Finite GF, raw GD, hidden velocities, and path laws

The generic conditioning/common-action construction does not need a
positive activation offset or a gain >=1. Its coordinate hypotheses were
checked in Section 2. The canonical action bounds and actual adjoints
follow from finite Gaussian operator bounds and finite transpose
identities on the countable generated probes. No claim is made that all
uncountably many choices of a have been realized simultaneously.

The physical fixed-cap reference has bounded paths and source moments.
At any fixed physical mesh, the finite source law identifies both actual
finite residuals and every learned contraction. Exact rank-one
unrolling bounds finite current operators by their initial bound plus
sums of products of update-factor RMS norms. A larger finite primal
ball with slack therefore contains the coarse finite reference on
high-probability events. Fixed-cap raw Euler local defects are bounded
by L_R M_R h^2/2, with constants independent of width. Stopped Gronwall
removes the auxiliary mesh and identifies finite fixed-cap GF.

The genuine uncut finite system is compared to that same-width cap
reference by the finite version of (11). Width goes to infinity at
fixed cap, then the cap goes to infinity. The strict bounded-ball
margin precludes exit. Raw GD is simultaneous Euler in the original raw
coordinates; its parameter interpolant has direction equal to the
uncut field at its preceding node. The additional cap-reference error
is C_{R,T}*eta_n. With eta_n=n^{-2}, the same stopped estimate converges,
without requiring an uncut Lipschitz constant uniform in width or a
Gaussian theorem for a growing transcript. The initialized finite
readout remains iid N(0,n^{-2}), whose RMS norm is O_P(n^{-1}); it is not
reset to zero. Its limit is the zero population readout by fixed-program
stability. These are full-width-sequence convergence-in-probability
arguments, not subsequence selection.

Every fixed-cap velocity-lemma hypothesis holds with the same elementary
bounds:

\[
|\phi(z)|\le \pi/2+|z|,\quad |\phi'|\le2,
\quad |\phi''|\le e\le1,
\quad |D|\le2|q|,\quad |D_z|\le2eR,\quad |D_q|\le2.
\]

The source-response and probe derivations use upper bounds only. The
appended forward queries are still W_2*U^1 and W_3*U^2, with
U^ell=phi'(Z^ell)*P^ell and P^ell the actual preactivation velocity.
Their source corrections and learned-memory terms stay present.
Unbounded-product velocity instructions must still first be smoothly
truncated as in Sections 4–5 of the supplied velocity proof; direct
application of the bounded-derivative conditioning theorem to those
products would be invalid. The published truncation argument applies
with the derivative bounds above.

The deterministic hidden-velocity comparison remains

\[
\|\mathcal V-\overline{\mathcal V}\|_{\mathrm{sum},2}
\le K\left[d_1+(1+M)d_0+
\sum_{\ell,i}\|(|\bar P_i^\ell|-M)_+\|_2\right],
\tag{12}
\]

where d_0 and d_1 are raw-state and raw-direction discrepancies. K is
independent of cap and truncation M on bounded primal/direction sets.
It follows by the three-layer product rule and truncating only the
reference preactivation-velocity factor in a gate difference. The
factor is a single M because each such product is added at its layer.

The order of limits is essential. First compare population cap
velocities to the uncut population velocity. The latter is continuous
in L2, by the trajectory chain rule with bounded continuous phi', and
has a compact L2 time image. Such an image has uniformly vanishing
positive-part tail norms: the tail map is 1-Lipschitz, so a finite L2
net reduces this to finitely many fixed L2 variables. Apply (12), take
R to infinity at fixed M, then M to infinity. For finite velocities,
take width first at fixed R,M, use the fixed-cap velocity law/tail
convergence, then R to infinity at fixed M, and finally M to infinity.
This proves uniform-time joint same-layer W2 velocity convergence,
fixed-finite-time joint W2 convergence, squared-speed and integrated
squared-speed convergence. It makes no unsupported estimate on the
growth of cap-dependent fourth-moment constants.

The actual raw-interpolant direction is used at GD times, with right
node derivatives and terminal left derivatives. Products of converging
L2 fields give the four raw kernel blocks and the prediction/loss
contractions. The path-space upgrade uses

\[
\|x-I_hx\|_{C([0,T])}^2\le4h\int_0^T|x'(t)|^2dt,
\]

averaged over neurons/populations, together with the just-proved speed
bounds and fixed-grid joint W2 convergence. The tuple has both samples'
preactivations and features in a given layer. No across-layer neuron
pairing or operator-norm convergence of unrelated finite matrices is
asserted.

### E.11. Odd initial motion, endpoint obstructions and Gaussian normalization

Within this proof unit, unqualified section and equation numbers are local.

Fix
\[
 \phi(z)=az+e\arctan z,\qquad \tfrac12\le a\le1,\quad e>0,
 \qquad |\rho|\le1-\delta,\quad 0<\delta\le1.
\]
Use the raw model and metric, two labels \(y_i\in\{-1,1\}\), and put \(p_i=y_i/2\), \(\tau=y_1y_2\). The restriction \(\delta\le1\) is the nonvacuous range for this symmetric separation. All second derivatives are identified by their time coordinate below.

#### 1. Forward nondegeneracy and a useful initial kernel bound

The first preactivation pair is nondegenerate centered Gaussian. For any nondegenerate centered Gaussian pair \((U,V)\) with equal marginal variance and any \((u_1,u_2)\ne0\), a zero \(L^2\) norm of \(u_1\phi(U)+u_2\phi(V)\) would, by positive Gaussian density and continuity, give the identity
\[
 u_1\phi(s)+u_2\phi(t)=0\quad\text{for every }s,t\in\mathbb R.
\]
Differentiating separately, and using \(\phi'>0\), forces both coefficients to vanish. Thus the feature Gram is positive definite. Induction through the two fresh forward calls makes every initialized preactivation pair nondegenerate Gaussian and every initialized feature Gram positive definite.

Here is a uniform lower bound, which does not require a Gram inverse. Let \(q_0=1,c_0=\rho\) and let \(q_\ell,c_\ell\) be the common feature second moment and cross moment after layer \(\ell\). Since \(\phi'\ge a\) and \(\phi\) is odd,
\[
 |\phi(u)-\phi(v)|\ge a|u-v|,\qquad
 |\phi(u)+\phi(v)|\ge a|u+v|.
\]
Each initialized Gaussian pair is exchangeable, so
\[
 q_\ell\pm c_\ell
 =\tfrac12E[(\phi(U)\pm\phi(V))^2]
 \ge a^2(q_{\ell-1}\pm c_{\ell-1}).
\]
Consequently
\[
 q_\ell\pm c_\ell\ge a^{2\ell}(1\pm\rho),\qquad
 \kappa_0:=\left\|\sum_i p_i h^3_{i,0}\right\|_3^2
 =\frac{q_3+\tau c_3}{2}
 \ge\frac{a^6\delta}{2}\ge\frac\delta{128}>0.
\]
These bounds hold for both label sectors. They are lower bounds, not formulas for a shifted activation. In particular the reference affine initial formula \((7+\rho)/2\) must not be reused here. For the odd affine reference \(\phi(z)=az\), the exact formula is
\[
 \kappa_{0,\mathrm{aff}}=a^6(1+\tau\rho)/2.
\]

#### 2. Full transpose covariances survive oddness

Write \(H_0=\sum_i p_i h^3_{i,0}\), \(D_i^\ell=\phi'(Z^\ell_{i,0})\), and
\[
 \beta_i^3=H_0D_i^3,\qquad S_3=E_3[\beta^3(\beta^3)^T].
\]
The matrix \(S_3\) is strictly positive definite even in the same-label sector. Indeed, a zero quadratic form would imply the everywhere identity
\[
 [p_1\phi(z_1)+p_2\phi(z_2)]
 [u_1\phi'(z_1)+u_2\phi'(z_2)]=0.
\]
For each fixed \(z_2\), the first factor has at most one zero as a function of \(z_1\), because \(p_1\ne0\) and \(\phi'>0\). The second factor vanishes off that point and hence everywhere by continuity. Differentiating it in \(z_1\) gives \(u_1\phi''(z_1)=0\) for every \(z_1\). Since
\[
 \phi''(z)=-2ez/(1+z^2)^2
\]
is not identically zero, \(u_1=0\); positivity of \(\phi'\) then gives \(u_2=0\).

Let \(B_0:H_2\to H_3\) be the initialized top action. The fixed finite-program transpose identity is
\[
 B_0^*\beta_i^3
 =G_i^2+\sum_jh^2_{j,0}\,T_{ij},\qquad
 T_{ij}=E_3[\partial_{z_j}\beta_i^3],
\]
where the joint Gaussian pair \(G^2\) has covariance **\(S_3\) itself**, and is independent of the initialized population-two forward sources. Explicitly,
\[
 \partial_{z_j}\beta_i^3
 =p_j\phi'(z_j)\phi'(z_i)
 +\mathbf1_{i=j}\Big(\sum_kp_k\phi(z_k)\Big)\phi''(z_i).
\]
Replacing \(S_3\) by the covariance remaining after regression on the forward features is incorrect. The finite-rank source-space projection from Gaussian matrix conditioning has negligible normalized coordinate effect in the infinite-width limit; the deterministic response above remains, and the coordinate Gaussian innovation has the full second-moment covariance.

Define
\[
 \beta_i^2=D_i^2\left(G_i^2+\sum_jh^2_{j,0}T_{ij}\right),
 \qquad S_2=E_2[\beta^2(\beta^2)^T].
\]
Conditionally on the initial population-two forward pair,
\[
 \operatorname{Cov}(\beta^2\mid Z^2_0)
 =\operatorname{diag}(D^2)S_3\operatorname{diag}(D^2)
 \succeq a^2\lambda_{\min}(S_3)I.
\]
Thus \(S_2\succeq a^2\lambda_{\min}(S_3)I>0\). The second initialized transpose has the form
\[
 A_0^*\beta_i^2
 =G_i^1+\sum_jh^1_{j,0}E_2[\partial_{\xi_j^2}\beta_i^2],
 \qquad \operatorname{Cov}(G^1)=S_2,
\]
with \(G^1\) independent of the population-one root pair. In this derivative the deterministic coefficients \(T\) and Gaussian covariances are held fixed, and \(G^2\) is an independent named source. The derivative includes the actual \(h^2\)-dependence of the response term. Finally,
\[
 \beta_i^1=D_i^1A_0^*\beta_i^2.
\]
All derivative expectations are finite: the activation grows at most linearly, all positive-order derivatives used here are bounded, and the source variables have Gaussian moments. The source lemma's single-transcript smooth-cap argument therefore applies without a new mesh-uniform assertion. Oddness changes no step of these identities.

#### 3. Every hidden block has nonzero feature-time acceleration

Define, in the raw hidden metric,
\[
 V^1=\frac1d\sum_i p_i\beta_i^1x_i,\qquad
 V^2=\sum_i p_i\beta_i^2\otimes h^1_{i,0},\qquad
 V^3=\sum_i p_i\beta_i^3\otimes h^2_{i,0}.
\]
If \(F\) is the relevant initial feature Gram and \(S\) the corresponding beta Gram, then
\[
 \|V^\ell\|_{\mathrm{HS}}^2
 =\operatorname{tr}(S\operatorname{diag}(p)F\operatorname{diag}(p))>0
 \quad(\ell=2,3),
\]
since both matrices in this trace product are positive definite. For the first block, condition on the first forward pair and use the Gaussian innovation of covariance \(S_2\). This gives
\[
 dE_1\|V^1\|_{\mathbb R^d}^2
 \ge a^2\lambda_{\min}(S_2)
       \sum_i p_i^2\frac{\|x_i\|^2}{d}
 =\frac{a^2\lambda_{\min}(S_2)}2>0.
\]
The deterministic conditional means contribute a nonnegative term. No input Gram inverse is used.

On a strong feature-time solution \(\Theta'=\nabla g\) with the stated chain rule and bounded gates,
\[
 C(s)=sH_0+o_{L^2}(s),\qquad
 b_i^\ell(s)=s\beta_i^\ell+o_{L^2}(s).
\]
For example, propagate \(C(s)/s\to H_0\) backwards, using operator-norm continuity of trained actions, bounded gates, and convergence of a bounded multiplier acting on each fixed \(L^2\) factor. The hidden vector field divided by \(s\) tends to \(V\), so integration yields
\[
 \vartheta(s)=\vartheta(0)+\tfrac12s^2V+o_{\mathrm{raw}}(s^2).
\]
Every hidden parameter **block** therefore has nonzero second derivative. This does not claim that every scalar first-layer coordinate changes: directions orthogonal to the input span are unchanged by the raw update.

#### 4. Every sample in every hidden layer has nonzero acceleration

Let \(U_i^\ell\) be the initial feature-time preactivation acceleration obtained by applying the forward linearization to \(V\). At the bottom,
\[
 U_i^1=\sum_j\Gamma_{ij}p_j\beta_j^1.
\]
Its conditional variance is bounded below by
\[
 \operatorname{Var}(U_i^1\mid Z^1_0)
 \ge a^2\lambda_{\min}(S_2)\sum_j\Gamma_{ij}^2p_j^2
 \ge a^2\lambda_{\min}(S_2)/4>0.
\]
For the upper layers, product rules and actual adjoints give
\[
 \sum_i p_i\langle\beta_i^2,U_i^2\rangle_2
 =dE\|V^1\|^2+\|V^2\|_{\mathrm{HS}}^2>0,
\]
\[
 \sum_i p_i\langle\beta_i^3,U_i^3\rangle_3
 =\|V\|_{\mathrm{hidden}}^2>0.
\]
For instance \(U_i^2=V^2h_i^1+A_0(D_i^1U_i^1)\); pairing the first term produces \(\|V^2\|^2\), and moving \(A_0\) to its actual adjoint in the second produces the first-block norm. The next layer adds \(\|V^3\|^2\).

Hence at least one sample has nonzero acceleration in each upper layer. To obtain **each** sample, use the existing input reflection \(Qx_1=x_2\), \(Qx_2=x_1\) and the raw isometry
\[
 (w,A,B,C)\longmapsto(Qw,A,B,\tau C).
\]
Its initialization law is invariant, and it preserves the scalar objective. It sends \(\beta_i^\ell\) to \(\tau\beta_{\pi i}^\ell\), \(V^1\) to \(QV^1\), leaves \(V^2,V^3\) unchanged, and sends \(U_i^\ell\) to \(U_{\pi i}^\ell\). Thus the two \(U\)-fields have equal squared population norms. Both must be nonzero. Since \(D_i^\ell\ge a>0\), the feature acceleration \(D_i^\ell U_i^\ell\) is nonzero for every layer and sample as well. This symmetry works for both \(\tau=1\) and \(\tau=-1\); no even component of the activation is used.

#### 5. Kernel change and the physical-time factors

Writing \(J_0\) for the bounded directional linearization of \(H\), adjunction gives \(V=J_0^*H_0\). Therefore
\[
 \kappa_4(s)=\|H(s)\|^2
 =\kappa_0+s^2\|V\|^2+o(s^2),
\]
\[
 \kappa(s)=\frac14y^TK(s)y
 =\kappa_0+2s^2\|V\|^2+o(s^2).
\]
The first coefficient follows from \(H(s)=H_0+(s^2/2)J_0V+o(s^2)\). The projected sum of hidden kernel blocks is \(s^2\|V\|^2+o(s^2)\). The total projected kernel thus changes strictly near zero.

The exact population reduction has \(ds/dt=2(1-g)\). Since \(g(0)=0\) and \(g'_s(0)=\kappa_0\),
\[
 s'(0)=2,\qquad s''(0)=-4\kappa_0.
\]
Consequently the physical hidden acceleration is \(4V\), the physical sample preactivation/feature accelerations are respectively \(4U_i^\ell\) and \(4D_i^\ell U_i^\ell\), and
\[
 \kappa_4(t)=\kappa_0+4t^2\|V\|^2+o(t^2),\qquad
 \kappa(t)=\kappa_0+8t^2\|V\|^2+o(t^2).
\]
For the readout, \(C_s'(0)=H_0\ne0\) and \(C_s''(0)=0\), but physical time gives
\[
 \dot C(0)=2H_0,\qquad \ddot C(0)=-4\kappa_0H_0\ne0.
\]
The latter follows directly by differentiating \(\dot C=2(1-g)H\), because the initial hidden velocity and hence \(\dot H(0)\) vanish. Thus **all four parameter blocks have nonzero physical initial acceleration**, while only the three hidden blocks have nonzero feature-time initial acceleration. The finite random readout remains the original one; these statements concern its population-zero initial limit.

#### 6. Genuine endpoint obstructions and the extra odd symmetry

There is no interior counterexample from oddness. A more direct exact finite-width reduction explains the label sectors: replace \((x_i,y_i)\) by \((y_ix_i,1)\). Every bias-free odd network obeys \(f(-x)=-f(x)\), so the two losses are identical functions of all raw parameters, with identical gradients and trajectories. The transformed correlation is \(\tau\rho\). Thus the two label sectors reduce to one another by \(\rho\mapsto-\rho\), and the separation \(|\rho|\le1-\delta\) treats them equally.

At the excluded endpoint \(\rho=-1\) with equal labels, the top hidden features are opposite at every finite width and every parameter state, so \(H\equiv0\). The population trajectory started at \(C=0\) is stationary with positive loss. At \(\rho=1\) with opposite labels the same obstruction occurs because the two features coincide. These are genuine counterexamples to carrying the reference one-sided separation \(\rho\le1-\delta\) over to an odd witness for all labels. By contrast, antipodal opposite labels and identical same labels reduce to a compatible single input. Their initial Grams are singular, so the positive-definite proof above does not cover those compatible endpoints, although that is irrelevant to the symmetric separated theorem.

An additional simultaneous hidden-sign/readout-sign symmetry can force odd hidden marginal means to vanish. It does not force their squared accelerations to vanish. The explicit positive quantities in Sections 3–4 settle that distinction.

#### 7. Convex mixing and unit Gaussian energy

Let \(G\sim N(0,1)\). Here Gaussian energy means \(E[\phi(G)^2]\). Put
\[
 m=E[G\arctan G],\qquad b=E[(\arctan G)^2].
\]
Since \(0<|\arctan z|<|z|\) for \(z\ne0\),
\[
 0<b<m<1.
\]
Cauchy–Schwarz is strict because \(\arctan G\) is not proportional to \(G\), so \(m^2<b\). Gaussian integration by parts also gives \(m=E[(1+G^2)^{-1}]\), if that alternative formula is wanted.

For the genuine positive convex mixture
\[
 \psi_r(z)=(1-r)z+r\arctan z,\qquad 0<r\le1,
\]
pointwise strict contraction gives \(|\psi_r(G)|<|G|\) almost surely. Hence
\[
 E[\psi_r(G)^2]
 =(1-r)^2+2r(1-r)m+r^2b<1.
\]
Thus a nontrivial convex mixture of these two specific functions cannot simultaneously have unit Gaussian energy. The only unit-energy member of the closed convex segment is \(r=0\), the identity.

There are two equivalent convenient parameterizations of the normalized witness.

**Normalize the convex mixture.** Let
\[
 N_r=\|\psi_r(G)\|_2,\qquad
 \phi_r(z)=\psi_r(z)/N_r=a_rz+e_r\arctan z,
\]
\[
 a_r=(1-r)/N_r,\qquad e_r=r/N_r.
\]
For \(0<r\le1/2\),
\[
 1-r<N_r<1,
 \qquad \tfrac12\le1-r<a_r<1,
 \qquad 0<e_r<\frac r{1-r}\le2r.
\]
The first strict lower bound follows from the positive cross term in \(N_r^2\). For any theorem threshold \(e_\delta>0\), choosing
\[
 0<r\le\min\{1/2,e_\delta/2\}
\]
therefore ensures \(a_r\in[1/2,1]\), \(0<e_r\le e_\delta\), and exact unit energy. The normalized weights obey
\[
 a_r+e_r=1/N_r>1.
\]
They are positive weights, but they no longer sum to one.

**Normalize an identity perturbation.** Equivalently let
\[
 D_r=\|G+r\arctan G\|_2
     =\sqrt{1+2mr+br^2},\qquad
 \phi_r(z)=\frac{z+r\arctan z}{D_r}.
\]
For \(0<r\le1\), \(1<D_r<1+r\le2\). Thus
\[
 a_r=D_r^{-1}\in[1/2,1),\qquad
 e_r=rD_r^{-1}\in(0,r),\qquad
 a_r+e_r=(1+r)/D_r>1.
\]
The choice \(0<r\le\min\{1,e_\delta\}\) gives the desired parameter rectangle and exact unit energy. These two parameterizations are related by replacing the first mixing parameter by \(r/(1+r)\).

If unit Gaussian energy is imposed, every initial layer has scalar preactivation law \(N(0,1)\): it holds at the bottom, the feature second moment is one, and each next fresh Gaussian action has that variance. This adds no requirement that trained preactivations remain Gaussian or have unit variance.

## F. General activation shapes and exact affine positivity

The broad shape theorem admits nonodd, linearly growing C2 shapes with |psi(0)|, ||psi'|| and ||psi''|| at most one. Its exponent is 31/8, with the explicit constants below. Odd-label folding is replaced by the typed sample bases in F.2. F.7 supplies coordinate identities only; all learned-moment estimates use the direct raw argument F.3. The affine positivity table F.6 is an additional exact result. It does not assert an improved nonlinear threshold.

### F.1. General C2 shape theorem with linear growth

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Exact model and the essential theorem

Fix \(0<\delta\le1\), \(x_1,x_2\in\mathbb R^d\) with
\(\|x_i\|^2=d\), \(|\rho|\le1-\delta\), \(\rho=x_1^Tx_2/d\),
and \(y_i\in\{-1,1\}\). Initialize independent entries
\[
 W^1_{ij}\sim N(0,1/d),\quad W^2_{ij},W^3_{ij}\sim N(0,1/n),
 \quad C_i\sim N(0,n^{-2}).
\]
At width \(n\), use
\[
 z_i^1=W^1x_i,\quad h_i^\ell=\phi(z_i^\ell),\quad
 z_i^2=W^2h_i^1,\quad z_i^3=W^3h_i^2,\quad
 f_i=\frac{( C)^\top(h_i^3)}{n},\quad r_i=f_i-y_i,
\]
where \(\frac{( u)^\top(v)}{n}=u^Tv/n\). The backward fields are
\[
 b_i^3=C\phi'(z_i^3),\quad
 b_i^2=\phi'(z_i^2)(W^3)^Tb_i^3,\quad
 b_i^1=\phi'(z_i^1)(W^2)^Tb_i^2.
\]
The loss is \(\mathcal L=(r_1^2+r_2^2)/2\) and the raw metric is
\[
 \|d\Theta\|_{\rm raw}^2
 =\frac dn\|dW^1\|_F^2+\|dW^2\|_F^2+\|dW^3\|_F^2+\frac{\|dC\|_2^2}{n}.
\]
Its exact physical gradient flow is
\[
 \dot W^1=-d^{-1}\sum_i r_i b_i^1x_i^T,\quad
 \dot W^\ell=-n^{-1}\sum_i r_i b_i^\ell(h_i^{\ell-1})^T
 \quad(\ell=2,3),\qquad \dot C=-\sum_i r_i h_i^3.
\]
Raw GD is simultaneous Euler for these equations with step \(n^{-2}\).
Raw parameters are interpolated linearly; hidden fields are recomputed
from them. At nodes use right velocities, terminal-left at the final
endpoint. The finite readout is retained throughout.

Define
\[
 \mathcal A=\{\psi\in C^2(\mathbb R):
 |\psi(0)|\le1,\ \|\psi'\|_\infty\le1,\ \|\psi''\|_\infty\le1\}.
 \tag{1}
\]
Then \(|\psi(z)|\le1+|z|\). Boundedness of the shape, oddness,
monotonicity, analyticity and tail limits are not required.

**Theorem A (one uniform coefficient for global dynamics).**
There is an explicit universal \(c_{\rm dyn}>0\), defined in (4),
such that every fixed
\[
 a\in[1/2,1],\quad \psi\in\mathcal A,\quad
 0<e\le c_{\rm dyn}\delta^{31/8},\qquad
 \phi(z)=az+e\psi(z)                                     \tag{2}
\]
used in all three hidden layers has these properties:

1. There is one autonomous global strong population loss flow on the
   canonical generated Gaussian action spaces. It is unique against
   bounded-primal strong competitors on the same spaces, including
   nonsymmetric ones, and continues uniquely from reached states.
   Its state is a first-layer field, two bounded actions with actual
   adjoints and Hilbert--Schmidt learned increments, and a readout field.
   The state is infinite-dimensional.
2. On each fixed physical interval \([0,T]\), actual finite GF and
   raw GD converge jointly, along the full width sequence in probability,
   to this flow. Predictions, loss and all four true raw kernel blocks
   converge uniformly in time. Both orientations of the actions are
   retained on generated probes. At each layer the joint two-sample
   preactivation/feature path law converges in
   \(\mathcal W_2(C([0,T];\mathbb R^4))\), with supremum norm.
   Same-layer fields and recomputed velocities converge jointly in
   \(\mathcal W_2\), uniformly in time and at any fixed finite collection
   of times. Second moments and integrated squared speeds converge.
3. The population predictions satisfy \(f_i=y_i g\), and
   \(\mathcal L(t)\le\exp(-\delta t/2048)\).

The coefficient is independent of the shape within \(\mathcal A\),
actual angle, labels, dimension, width, caps, meshes and horizon.
Convergence constants may depend on the fixed shape, data and \(T\).
There is no probability supremum over this class or over the infinite
time half-line, and no cross-width operator-norm convergence assertion.

#### 2. Additional nonaffinity and initial feature learning

For \(G\sim N(0,1)\), define
\[
 \mathcal R_\psi(Z)=\inf_{\alpha,\beta}
 E[(\psi(Z)-\alpha-\beta Z)^2],\qquad
 \eta_\psi=\min_{1/\sqrt{404}\le\nu\le260}\mathcal R_\psi(\nu G).
 \tag{3}
\]
Every globally nonaffine \(\psi\in\mathcal A\) has \(\eta_\psi>0\).

**Theorem B (persistent nonaffinity).** For a globally nonaffine
shape in Theorem A, impose additionally
\(e\le c_{\rm NL}(\psi)\delta^{31/8}\), with (4). Then
\[
 \inf_{t\ge0,i,\ell}\inf_{\alpha,\beta}
 E[(\phi(z_i^\ell(t))-\alpha-\beta z_i^\ell(t))^2]
 \ge e^2\eta_\psi/4>0.
\]

Every globally nonaffine shape in Theorem A also has nonzero population
initial acceleration in every hidden parameter block and every
sample/layer's preactivation and feature. The readout has nonzero initial
velocity, and the projected total kernel changes at small positive time.
This initial-motion statement needs no additional \(\eta_\psi\) cutoff.
It does not assert nonzero hidden velocity at every later instant.

Thus global dynamics has a shape-uniform coefficient; the quantitative
persistent nonaffinity margin has a separate shape obligation.

#### 3. Explicit sufficient constants

Set
\[
 C_0=1296000\exp(1404),\quad C_z=1500C_0,\quad C_g=14400C_0,
\]
\[
 H=10^{30}[1+C_0+C_z+C_g+\exp(1410)]^4,\qquad K=H^2,
\]
\[
 c_{\rm dyn}=\min\left\{
 \frac14,\frac1{2C_0(8\sqrt2)^3},
 \frac1{4C_g(8\sqrt2)^{11/4}},
 \frac12\,24^{-31/4}K^{-46}\right\},\qquad
 c_{\rm NL}(\psi)=
 \frac{\sqrt{\eta_\psi}}{4C_z(8\sqrt2)^{7/2}}.             \tag{4}
\]
These numbers are positive and chosen before the data. The coefficient
rule is polynomial in separation, but its numerical prefactor is still
extremely small. It is sufficient, not necessary or optimal, and does
not certify a practically moderate nonlinear amplitude.

#### 4. Detailed proof components and their interfaces

The architecture is: control an affine reference up to prediction
\(3/2\); preserve its endpoint margin under the nonlinear perturbation;
bound every actual source-response coefficient; remove auxiliary caps;
convert its first-fitting feature interval to all physical times; then
apply the exact finite-algorithm and observable comparisons.

The complete extra derivations are in these companions:

- Fragment F.2, Sections 2--4, proves sample
  symmetry for arbitrary scalar activations, with different fixed bases
  for forward and backward sample slots. This replaces odd label
  folding. It also bounds actual affine Gaussian marginal standard
  deviations in \([1/\sqrt{404},260]\), independently of \(\delta\).
- Fragment F.3, Sections 2--4, derives the raw
  perturbation constant, forward/prediction bounds and all learned
  Gram discrepancies for linearly growing shapes. It uses raw typed
  coordinates without dividing by a small inactive sample variance.
- Fragment F.3, Sections 5--6, proves the source-value inequalities
  and verifies the derivative/sector interfaces, including current
  transpose returns and arbitrary causal backward row errors.
- Fragment F.2, Sections 5 and 7, and Fragment F.3,
  Sections 1, 6 and 7, establish regression, initial motion, and
  uniform shape subclasses.

The affine balance and actual-source proofs are E.3–E.6; F.4–F.5 prove response and closure. Cap removal, physical conversion and observables are E.10 and III.V. F.7 supplies only the exact coordinate transformations. F.3 supplies all raw learned-moment bounds.

Here is the complete assembly. Define
\[
 v=(1+y_1y_2\rho)/2,\quad \lambda=a^3\sqrt v,\quad
 M=[3/(\sqrt2\lambda)]^{1/4}.
\]
This is the actual endpoint scale, with
\(1<M\le24^{1/4}\delta^{-1/8}\). The affine feature interval has
duration \(S\le M^4\), with each dataset stopped at its own first
hit \(g=3/2\). Polynomial Hilbert-space local existence and the
gradient-energy endpoint estimate give affine continuation to that hit.
The exact balances and integrated curvature supply the inherited
affine/source certificate.

For linearly growing shapes the same-state raw forcing is at most
\(40eb^3\), as derived in Fragment F.3 Section 2.
Only the affine field is differentiated in the comparison.
The reference raw tube also bounds the normalized active first root by \(b\);
this bound is used for the affine prediction comparison, not inferred
from the unnormalized sample projections.
The resulting estimates are
\[
 E_{\rm raw}\le C_0e\lambda^{-3},\qquad
 \max_{i,\ell}\|z_{i,e}^\ell-z_{i,0}^\ell\|_2
       \le C_ze\lambda^{-7/2},\qquad
 |g_{e,R}(S)-3/2|\le C_ge\lambda^{-11/4}.                 \tag{5}
\]
Since \(\lambda\ge\sqrt\delta/(8\sqrt2)\), the first three entries
of \(c_{\rm dyn}\) close the raw radius-one tube and give
\(g_{e,R}(S)\ge5/4\), uniformly in the cap.

The direct raw typed calculation gives learned-moment strict density
errors at most \(KeM^{15}\) and complete backward row errors at most
\(KeM^{19}\). It avoids the invalid inference
\(e/\sqrt\delta\lesssim eM^4\) when the inactive variance can vanish
independently of \(v\).

The affine transfer certificate and the positive sector supersolution
concern affine arrays, so they are unchanged by the shape. On their
coefficient box, the newly checked value equations give, for \(p\ge2\),
\[
 \|q_k^1\|_p\le K^{10}M^{15}\sqrt p,\quad
 \|q_k^2\|_p\le K^{10}M^{13}\sqrt p,\quad
 \|C_k\|_p\le K^{10}M^{11}\sqrt p.
\]
Bounded \(\psi'\) and \(\psi''\) give the same random derivative
envelope, whose moments are bounded if \(eK^{22}M^{19}\le1\).
After controlling the envelope, Cauchy--Schwarz uses the smaller
actual primal \(L^2\) bounds \(KM^3,KM^2,KM\). The complete
coefficient forcing is therefore
\[
 q_{\rm def}\le K^{30}eM^{19}.
\]
The supplied sector supersolution closes if
\(q_{\rm def}\le K^{-16}M^{-12}\). Its hypotheses retain signs,
both sample sectors, all past named source slots, current returns
and the single-source time-step factor; the companions check each
shape substitution. Our choice gives
\[
 eM^{31}\le K^{-46}/2,\quad
 eK^{22}M^{19}\le K^{-24}M^{-12}/2<1,\quad
 q_{\rm def}\le K^{-16}M^{-12}/2.                        \tag{6}
\]
Continuity in amplitude at fixed cap and sufficiently fine fixed mesh,
followed by a first-exit contradiction, proves cap- and mesh-uniform
source bounds. These yield Gaussian tails for the actual incoming
fields; the tails are conclusions rather than assumptions.

The supplied asymmetric cap comparison has error
\(C\exp(CR-cR^2)\) on this feature interval and requires tails only
of the reference. It constructs a strong uncut autonomous
feature-gradient path through \(S\). Its sample symmetry gives
\(f_i=y_i g\). At its first hit \(s_*<S\) of \(g=1\), bounded
\(g'\) implies \(1-g(s)\le C(s_*-s)\). Hence
\[
 t(s)=\int_0^s[2(1-g(u))]^{-1}\,du
\]
diverges at \(s_*\). Its inverse converts the feature gradient into
exactly the physical loss flow for every \(t\ge0\).
The initialized odd/even Gaussian decomposition gives
\(\kappa(0)\ge\delta/8192\); the strong radial identity gives
\(g_s'\ge\kappa(0)\). Thus
\(\dot{\mathcal L}=-4g_s'\mathcal L\) proves Theorem A's rate.

The physical comparisons retain both actual finite residuals.
On each fixed \([0,T]\), their cap-removal cost is
\(C_T\exp(C_TR-cR^2)\), so no additional activation restriction
depends on \(T\). They prove uniqueness against nonsymmetric
bounded-primal strong competitors and reached-state restart.
Width is taken at fixed cap and auxiliary mesh; deterministic Euler
estimates remove that mesh; then the cap is removed. Actual raw GD
adds the prescribed \(C_{R,T}n^{-2}\) reference error.

The fixed-cap observation bridge uses linear growth, bounded first
two derivatives and its named product-query truncations, all checked
here. For velocities, first fix a reference-velocity truncation,
remove the cap, then remove that truncation, using the compact
\(L^2\) time image of the uncut velocity. The grid inequality
\(\|x-I_hx\|_\infty^2\le4h\int_0^T|x'|^2\) upgrades finite-time
laws to the path-space Wasserstein laws. Kernel contractions use
converging same-layer \(L^2\) factors. This proves the asserted
observable scope, rather than deducing it from raw energy alone.

No step so far uses nonaffinity or \(\eta_\psi\), so the whole
class \(\mathcal A\) shares \(c_{\rm dyn}\). For Theorem B,
the affine variance interval makes \(\eta_\psi>0\). Square-root
regression error is 2-Lipschitz under coupled \(L^2\) distance.
Equation (5) and \(c_{\rm NL}\) give
\(\mathcal R_\psi(z)\ge\eta_\psi/4\). Absorbing the affine part
gives exactly the factor \(e^2\). This holds through \(S\), hence
at every physical time. Initial motion uses
\(\phi'\ge1/4\), nonconstant \(\phi'\), and the actual Gaussian
transpose returns as proved in Fragment F.2 Section 7.
It imposes no quantitative \(\eta_\psi\) cutoff. Both theorems follow.

### F.2. Typed sample symmetry, Gaussian margins and initial activity

Within this proof unit, unqualified section and equation numbers are local.

The bounded-shape specialization starts with psi in C_b^2 and max(||psi||_infinity,||psi_prime||_infinity,||psi_second||_infinity)<=1, phi(z)=az+e psi(z), a in [1/2,1], and sufficiently small e. It gives the displayed sufficient fourth-power cutoff. The general linearly growing class and sharper 31/8 cutoff are proved in F.3; only the exact symmetry, Gaussian and activity arguments of this unit are used for that extension.

#### 2. Scalar symmetry without oddness

Absorb \(y_1\) into the readout, an isometry of the raw metric and of its centered Gaussian initialization, and write \(y=(1,\tau)\), \(\tau=y_1y_2\in\{-1,1\}\). Let \(P\) exchange the two sample slots and let \(Q_x\) be the orthogonal input reflection exchanging the normalized inputs. Such a reflection exists because the two inputs have equal norm (their sum and difference are orthogonal).

The raw transformation

\[
(w,A,B,C)\longmapsto(Q_xw,A,B,\tau C)
\]

preserves the scalar feature objective
\(g=\frac12\sum_i y_if_i\) and its raw metric. Indeed it sends forward fields to their exchanged fields, predictions to \(\tau Pf\), and \(\tau Py=y\). It preserves the Gaussian initialization law. At each fixed Euler/cap transcript this is an exact equivariance. Deterministic limiting contractions therefore satisfy \(f_2=\tau f_1\), so \(f_i=y_ig\), without first invoking uniqueness of an unconstructed population flow.

For arbitrary scalar \(\phi\), forward fields transform as \(Pz,Ph\). Backward fields transform as \(\tau Pq,\tau P\delta\). For the auxiliary gate

\[
D_R(z,q)=aq+e\psi'(z)\tau_R(q),
\]

this is still exact because the same scalar \(\psi'\) is used at both samples and the clipping function \(\tau_R\) is odd. Oddness of the *clip*, not of the activation, is used here. Hence the cap feature paths have the same scalar prediction symmetry.

Once the constructed feature path reaches \(g=1\) from below on a bounded interval, the physical clock
\(dt/ds=[2(1-g(s))]^{-1}\) diverges at its first hit because \(g'\) is bounded there. This gives the exact physical flow for every finite physical time. Scalar symmetry by itself supplies neither the bounded feature interval nor the required source-tail/width bridge; those are supplied in Sections 5–6.

#### 3. Typed sample bases: exact replacement for odd label folding

Set

\[
Q=\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad
Y=\operatorname{diag}(1,\tau),\quad
Q_f=QY,\quad Q_b=Q,\quad
v=(1+\tau\rho)/2.
\]

Use \(Q_f\) for forward sample slots \(z,h,\xi\), and \(Q_b\) for backward slots \(q,\delta,\zeta\). The names forward/backward refer to the type of the sampled neuron field, not the direction in which a coefficient is multiplied. Then

\[
Q_f\Gamma\operatorname{diag}(y/2)Q_b^{-1}
=\operatorname{diag}(v,1-v),
\]

\[
\sum_i(y_i/2)\delta_i\otimes h_i
=\sum_{\alpha=+,-}(Q_b\delta)_\alpha\otimes(Q_fh)_\alpha,
\qquad \tfrac12\sum_i y_i h_i=(Q_fh)_+,
\qquad Q_b(C,C)^T=Ce_+.
\]

The tensor identity follows from \(Q_b^TQ_f=Y/2\), so includes every factor of two. Put \(S=\operatorname{diag}(\sqrt v,\sqrt{1-v})\), \(r=\sqrt v\), and \(\lambda=a^3r\). The exact normalized equations of Fragment F.7 hold after replacing its single Q by Qf for forward slots and Qb for backward slots:

\[
z^\ell=a^{\ell-1}Q_f^{-1}Sx^\ell,\quad
h^\ell=a^\ell Q_f^{-1}S\widehat h^\ell,
\]
\[
\delta^\ell=a^{4-\ell}rQ_b^{-1}S^{-1}d^\ell,\quad
q^\ell=a^{3-\ell}rQ_b^{-1}S^{-1}\widehat q^\ell.
\]

With normalized time \(t=\lambda s\), these give exactly

\[
x^2=A\widehat h^1,\quad x^3=B\widehat h^2,
\quad\widehat q^3=Ce_+,\quad
\widehat q^2=B^*d^3,\quad\widehat q^1=A^*d^2,
\]
\[
\partial_t x^1=d^1,\quad
\partial_t A=\sum_\alpha d^2_\alpha\otimes\widehat h^1_\alpha,
\quad\partial_t B=\sum_\alpha d^3_\alpha\otimes\widehat h^2_\alpha,
\quad\partial_t C=\widehat h^3_+.
\]

At \(e=0\), the normalized active four-component affine system, the frozen inactive fields, all positive beta-scaling arguments, and their numerical affine bounds are therefore precisely the reference ones.

There is also an exact source-coefficient symmetry. A forward response block \(\mathsf A\), mapping backward named sources to forward fields, and a backward response block \(\mathsf B\), mapping forward sources to backward fields, obey

\[
P\mathsf A=\mathsf A(\tau P),\qquad
(\tau P)\mathsf B=\mathsf BP.
\]

At each fixed source transcript, this follows by the chain rule under the previous exact involution, keeping the deterministic arrays and covariances fixed during each formal derivative. Learned moments obey the same identities: forward learned blocks are forward Gram matrices times \(\operatorname{diag}(y/2)\), and backward blocks are backward Gram matrices times that same diagonal matrix. Full second-moment covariances commute with P. Induction over the source transcript therefore preserves both covariance symmetry and the response intertwiners, including singular Gaussian sources.

Now

\[
Q_fPQ_f^{-1}=Q_b(\tau P)Q_b^{-1}
=\tau\operatorname{diag}(1,-1).
\]

Thus \(Q_f\mathsf A Q_b^{-1}\) and \(Q_b\mathsf BQ_f^{-1}\) commute with \(\operatorname{diag}(1,-1)\), and are diagonal in the two sample sectors. For opposite labels, the original blocks anti-commute with ordinary exchange; treating them as commuting in one common sample basis would be wrong. The two different bases repair exactly that issue.

The current return \(E[D_z]\) has the backward-from-forward type and satisfies the second intertwiner. It is included, not set to zero. Random gates remain full two-by-two maps; only deterministic expected coefficient blocks become sector diagonal.

#### 4. New affine variance bound independent of delta

For the affine active system let \(p\) be the normalized active first root and let \(D\) be the sign-adjusted readout. Write \(R=\|D\|^2\). The existing exact balances give

\[
\|p\|^2=1+R,\quad
A^*A=p\otimes p+A_0^*A_0-p_0\otimes p_0,
\quad BB^*=D\otimes D+B_0B_0^*.
\]

Since the initialized action norms are at most ten,

\[
\|Ap\|^2\le(R+101)(R+1),\qquad
\|BAp\|^2\le(R+100)(R+101)(R+1).
\]

The existing affine radial estimate \(F\ge\|D\|^4/\sqrt2\), with \(g=\lambda F\le3/2\) on the reference interval, yields

\[
R\le\sqrt{\frac3{\sqrt2a^3\sqrt v}}
\le\sqrt{12\sqrt2}\,v^{-1/4}<5v^{-1/4}.
\]

The frozen inactive fields and zero active/inactive covariance give the exact marginal formulas

\[
\operatorname{Var}(z_i^1)=v(1+R)+1-v,
\]
\[
\operatorname{Var}(z_i^2)=a^2[v\|Ap\|^2+1-v],\quad
\operatorname{Var}(z_i^3)=a^4[v\|BAp\|^2+1-v].
\]

Because \(vR^k\le5^k\) for \(k=1,2,3\) and \(0<v\le1\), expansion gives

\[
\operatorname{Var}(z_i^1)\le6,\quad
\operatorname{Var}(z_i^2)\le636,\quad
\operatorname{Var}(z_i^3)\le66780<260^2.
\]

For the last two bounds the expansions are
\(1+100v+102vR+vR^2\) and
\(1+10099v+10301vR+202vR^2+vR^3\).

The existing lower bounds require no activation substitution because this reference is affine: \(\|BAp\|\ge1\) by the radial readout inequality, while

\[
\|Ap\|^2\ge\max\{R(1+R),(100+R)^{-1}\}\ge1/101.
\]

Thus every actual affine marginal is centered Gaussian \(\nu G\) with

\[
\boxed{1/\sqrt{404}\le\nu\le260.}
\]

This fixed compact interval is the key new nonaffinity fact. Large initialized/action-space operator envelopes do not force the actual forward marginals to range over arbitrarily large variances as delta shrinks.

#### 5. Nonaffinity and a safe explicit coefficient

Define

\[
\mathcal R_\psi(Z)=\inf_{\alpha,\beta}E[(\psi(Z)-\alpha-\beta Z)^2],
\quad
\eta_\psi=\min_{1/\sqrt{404}\le\nu\le260}\mathcal R_\psi(\nu G).
\]

For each bounded continuous nonconstant \(\psi\), \(\eta_\psi>0\). Continuity in \(\nu\) follows by dominated convergence for the Gaussian regression formula (the variance stays positive). A zero residual would identify \(\psi\) with an affine function on the full support of a nondegenerate Gaussian. Continuity extends that equality everywhere, and boundedness makes the affine function constant, a contradiction.

An optional entirely explicit witness is any \(b\ge1\) with

\[
J_b(\psi)=\inf_{\alpha,\beta}\int_{-b}^b[\psi(x)-\alpha-\beta x]^2dx>0.
\]

Such b exists for every bounded nonconstant continuous function. Gaussian density on this interval yields

\[
\eta_\psi\ge\frac{e^{-202b^2}}{260\sqrt{2\pi}}J_b(\psi)>0.
\]

No tail-limit condition is used. Compactly supported and oscillatory shapes are included.

For any coupled square-integrable X,Y and a one-Lipschitz shape,

\[
|\sqrt{\mathcal R_\psi(X)}-\sqrt{\mathcal R_\psi(Y)}|
\le2\|X-Y\|_2.
\]

Indeed the optimal regression slope has absolute value at most one by the independent-copy identity
\(\operatorname{Cov}(X,\psi(X))=\frac12E[(X-X')(\psi(X)-\psi(X'))]\). Its residual map \(\psi(x)-\beta x\) is two-Lipschitz. Test one optimizer on the other coupled variable and reverse the roles. Constant variables are covered by choosing slope zero.

Let C0,Cz,Cg,H be the actual numerical constants in the existing power-four proof:

\[
C_0=1296000e^{1404},\quad C_z=1500C_0,\quad C_g=14400C_0,
\]
\[
H=10^{30}(1+C_0+C_z+C_g+e^{1410})^4.
\]

Define

\[
c_{*,\psi}=\min\left\{\frac14,
\frac1{2C_0(8\sqrt2)^3},
\frac1{4C_g(8\sqrt2)^{11/4}},
\frac{\sqrt{\eta_\psi}}{4C_z(8\sqrt2)^{7/2}}\right\},
\]

\[
\boxed{c_\psi=\min\{c_{*,\psi},10^{-70}H^{-400}\}.}
\]

The reference pointwise primal forcing estimates remain valid because \(|\psi|\le1<\pi/2\), \(|\psi'|\le1\), \(|\psi''|\le1\). Hence the reference raw radius-one comparison and endpoint estimates hold with the same constants. Under \(e\le c_\psi\delta^4\), we have \(e\le c_{*,\psi}\delta^{7/4}\), so the raw tube closes, \(g_{e,R}(S)\ge5/4\), and

\[
\sup_{i,\ell,s\le S}\|z_{i,e,R}^\ell-z_{i,0}^\ell\|_2
\le C_z e(8\sqrt2)^{7/2}\delta^{-7/4}
\le\sqrt{\eta_\psi}/4.
\]

Consequently \(\mathcal R_\psi(z_{i,e,R}^\ell)\ge\eta_\psi/4\). Absorbing az into the regression competitor gives the activation error \(e^2\eta_\psi/4\). Strong cap removal preserves it, and the first-hit clock preserves it for all finite physical times.

These constants are explicit sufficient constants, still extremely small. This extension preserves the polynomial delta dependence; it does not solve the numerical-prefactor problem.

#### 6. Every shape-dependent source/limit occurrence

The exact normalized forward and backward maps now are

\[
\mathcal H_\ell(x)=a^{-\ell}S^{-1}Q_f\phi(a^{\ell-1}Q_f^{-1}Sx),
\]
\[
\mathcal D_{\ell,R}(x,q)=a^{\ell-4}r^{-1}SQ_b
D_R(a^{\ell-1}Q_f^{-1}Sx,a^{3-\ell}rQ_b^{-1}S^{-1}q).
\]

Qf and Qb have exactly the reference Q operator norms, as do their inverses. The deviations from the affine maps therefore obey the reference normalized bounds with \(\varepsilon=64e/\sqrt\delta\): bounded forward error, first-derivative error at most epsilon, backward-value and q-derivative errors at most epsilon times the reference factors, and x-derivative at most \(\varepsilon|q|\). The gates are still applied in original sample coordinates. Their random sector matrices are not assumed diagonal. The global-delta bound is not converted to an intrinsic e M^4 bound: the inactive variance can be small independently of v. All original-time learned-moment estimates below instead use Fragment F.3, Section 4, which works directly in raw typed coordinates without dividing by sample variances.

The source value substitutions are exact with
\(h(Z)=\psi(Z)\) and \(d(Z,q)=\psi'(Z)\tau_R(q)\). They use only \(|h|\le\pi/2\) and \(|d|\le|q|\), both satisfied. In the derivative equations replace the reference g and g-prime by \(\psi'\) and \(\psi''\):

\[
G=aI+e\operatorname{diag}(\psi'(Z)),\quad
V=aI+e\operatorname{diag}(\psi'(Z)\tau_R'(q)),\quad
L=e\operatorname{diag}(\psi''(Z)\tau_R(q)).
\]

The typed versions are respectively forward-to-forward, backward-to-backward, and backward-from-forward. Their deviations satisfy exactly \(|G-aI|,|V-aI|\le e\), \(|L|\le eQ\). These are the only activation inputs into the same-array derivative defect identities. Signs of \(\psi'\) or \(\psi''\) do not occur in their estimates; signed actual coefficient arrays are compared in absolute value to the positive *affine* supersolution. The affine beta positivity proof is unchanged because its activation is az.

Thus all power-four interfaces retain the same constants and powers:

\[
\|q^1\|_2\le HM^3,\quad\|q^2\|_2\le HM^2,\quad\|C\|_2\le HM,
\]
\[
\|q^1\|_p\le H^{10}M^{15}\sqrt p,\quad
\|q^2\|_p\le H^{10}M^{13}\sqrt p,\quad
\|C\|_p\le H^{10}M^{11}\sqrt p,
\]

and the complete coefficient forcing \(q_{\rm def}\le H^{30}eM^{19}\) under \(eH^{22}M^{19}\le1\). The sector supersolution requires \(q_{\rm def}\le H^{-16}M^{-12}\). Since \(M^{32}\le24^8\delta^{-4}\) and \(24^8<H\), the displayed choice \(e\le10^{-70}H^{-400}\delta^4\) verifies both inequalities with the same strict slack as the reference proof. Amplitude homotopy at each fixed cap/transcript closes the construction. Current returns, both matrix orientations, all learned memories, singular source covariances and the source-time mesh factor remain in this calculation.

At fixed cap, \(\phi\) and DR are C1 coordinate maps with bounded first derivatives:

\[
|\phi'|\le2,\quad |D_q|\le2,\quad |D_z|\le2eR,
\quad|\phi(z)|\le|z|+1.
\]

C2 of psi supplies continuity of those derivatives; no third derivative is used. The asymmetric gate estimate becomes

\[
\|D_{R'}(z_A,q_A)-D_R(z_B,q_B)\|_2
\le2\|q_A-q_B\|_2+2eR\|z_A-z_B\|_2
+2e\||q_B|\mathbf1_{|q_B|>R}\|_2.
\]

It uses the Lipschitz bound on psi-prime from bounded psi-double-prime. The source subGaussian tails therefore defeat the cap amplification, producing the same strong cap removal, physical uniqueness/restart and finite GF/raw-GD comparison. The velocity bridge uses only linear growth, bounded first and second derivatives, product-query truncation, and the ordered removal of cap and reference-velocity truncation. All are unchanged. Existence of finite GF alone is not used to identify any population limit.

#### 7. Initial motion and a kernel lower bound without oddness

Every initialized preactivation pair is nondegenerate centered Gaussian: its feature Gram is positive definite because \(\phi'>0\), full Gaussian support, and differentiation of a hypothetical identity \(u_1\phi(s)+u_2\phi(t)\equiv0\) force both coefficients zero. This induction works with nonzero feature means because source covariances are full second moments.

For the elementary initial kernel bound, decompose \(\phi=\phi_o+\phi_e\) into its odd and even parts. If \(m=a-e\ge1/4\), then \(\phi_o'\ge m\). For a centered Gaussian pair (U,V), simultaneous sign reversal makes the odd/even cross terms vanish. Therefore for each sign,

\[
E[(\phi(U)\pm\phi(V))^2]
\ge E[(\phi_o(U)\pm\phi_o(V))^2]
\ge m^2E[(U\pm V)^2].
\]

Layerwise iteration gives \(\kappa(0)\ge m^6\delta/2\ge\delta/8192\). After construction, the radial gradient identity gives \(g_s'\ge\kappa(0)\), and \(\mathcal L=(1-g)^2\) then obeys \(\mathcal L(t)\le\exp[-4\kappa(0)t]\le\exp[-\delta t/2048]\).

The reference initial-motion proof uses nonconstant phi-prime only when proving positive definiteness of the top beta Gram. It remains valid: bounded nonconstant C2 psi cannot have psi-double-prime identically zero, since then psi would be an affine bounded function and hence constant. The identity
\([p_1\phi(z_1)+p_2\phi(z_2)][u_1\phi'(z_1)+u_2\phi'(z_2)]=0\)
forces u1=u2=0 by strict monotonicity of the first factor in each coordinate and nonconstant phi-prime. The full reused-transpose covariance and deterministic derivative response formulas require only phi-prime, phi-double-prime, their bounds and Gaussian moments. Their conditional variance lower bounds hold with m replacing a. Thus all hidden parameter blocks have nonzero initial acceleration.

The forward linearization/adjunction identities still give positive aggregate upper-layer acceleration. The same raw swap/readout-sign involution from Section 2 equates the two sample acceleration norms for any scalar phi, so every sample/layer acceleration is nonzero. Since phi-prime is bounded below, feature accelerations are nonzero too. The projected-kernel expansion and its physical-time factors are unchanged.


### F.3. Linear-growth forcing, moments and numerical closure

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Class and exact threshold

Let

\[
\mathcal A=\{\psi\in C^2(\mathbb R):
|\psi(0)|\le1,\quad\|\psi'\|_\infty\le1,
\quad\|\psi''\|_\infty\le1\}.
\]

Then \(|\psi(z)|\le1+|z|\). Assume psi is not globally affine; bounded nonconstancy is replaced by this exact requirement. Set

\[
\eta_\psi=\min_{1/\sqrt{404}\le\nu\le260}
\inf_{\alpha,\beta}E[(\psi(\nu G)-\alpha-\beta\nu G)^2]>0.
\]

The fixed interval is proved in the preceding note. Positivity follows from full Gaussian support and global nonaffinity. Continuity of the Gaussian regression formula follows by dominated convergence using \(|\psi(\nu G)|\le1+260|G|\), including integrands with G and squared psi. Consequently no boundedness or tail-limit assumption is needed here.

Let C0,Cz,Cg,H be the constants in Section 5 of the preceding note, and put \(\bar H=H^2\). Define

\[
c_{\rm primal,\psi}=\min\left\{\frac14,
\frac1{2C_0(8\sqrt2)^3},
\frac1{4C_g(8\sqrt2)^{11/4}},
\frac{\sqrt{\eta_\psi}}{4C_z(8\sqrt2)^{7/2}}\right\},
\]

\[
c_{\rm source}=\tfrac12\,24^{-31/4}\bar H^{-46},
\qquad c_\psi=\min\{c_{\rm primal,\psi},c_{\rm source}\}.
\]

Subject to the existing power-four affine/source coefficient inequalities cited in the preceding note, the full two-sample L3 theorem, with precisely its original architecture, initialization, metric and raw GD, holds for

\[
\boxed{\phi(z)=az+e\psi(z),\quad a\in[1/2,1],
\quad0<e\le c_\psi\delta^{31/8},\quad|\rho|\le1-\delta.}
\]

The exponent 31/8 simply retains the existing source estimate's power count \(19+12=31\), rather than rounding it to 32 and then delta to the fourth power. It does not constitute a new stronger source estimate. The fourth-power version is included because \(\delta^4\le\delta^{31/8}\) for \(0<\delta\le1\).

There are two separate improvements: the scalar shape class is now all nonaffine C2 functions with bounded first two derivatives, after normalization; and the sufficient exponent is stated without rounding. The universal prefactor remains extremely small, even with the lighter direct source restriction. This is not a practical-mixing result.

#### 2. Direct same-state forcing with linear growth

Work on a common raw primal ball of radius \(b\ge1\), with first projections, A,B and C each bounded by b. Take \(e\le1/4\). Write a subscript 0 for the affine field evaluated at this same state. Triangle inequalities give

\[
\|h_e^1\|\le\tfrac32b,\quad
\|h_e^2\|\le\tfrac{17}{8}b^2,\quad
\|h_e^3\|\le\tfrac{93}{32}b^3<4b^3,
\]

where, for example, \(\|h_e^1\|\le(5/4)b+1/4\), and then
\(\|h_e^2\|\le(5/4)(3b^2/2)+1/4\le17b^2/8\).

The same-state forward discrepancies satisfy

\[
\|h_e^1-h_0^1\|\le2eb,
\quad\|h_e^2-h_0^2\|\le\tfrac92 eb^2,
\quad\|h_e^3-h_0^3\|\le\tfrac{61}{8}eb^3.
\]

For the last bound, propagate the preceding discrepancy with norm b and bound the new term by \(e[1+(17/8)b^3]\), giving \((9/2+25/8)eb^3=61eb^3/8\).

The cap gate always obeys \(\|D_R(z,q)\|\le(a+e)\|q\|\le5\|q\|/4\), without using a sign of psi-prime. Thus

\[
\|\delta_e^3\|\le\tfrac54 b,\quad
\|\delta_e^2\|\le\tfrac{25}{16}b^2,
\]
\[
\|\delta_e^3-\delta_0^3\|\le eb,
\quad\|\delta_e^2-\delta_0^2\|\le\tfrac94 eb^2,
\quad\|\delta_e^1-\delta_0^1\|\le\tfrac{61}{16}eb^3.
\]

Expand each outer product with the nonlinear forward factor and affine backward factor. Since the controls have l1 norm one, the four raw update differences are bounded, respectively, by

\[
\tfrac{61}{16}eb^3,\quad
\left(\tfrac94\tfrac32+2\right)eb^3
=\tfrac{43}{8}eb^3,
\]
\[
\left(\tfrac{17}{8}+\tfrac92\right)eb^3
=\tfrac{53}{8}eb^3,\quad\tfrac{61}{8}eb^3.
\]

Their sum is \(375eb^3/16<24eb^3<40eb^3\). Thus the exact reference raw forcing constant 40 survives; no C3 assumption is introduced.

Only the affine field is differentiated in the comparison, so the reference integrated affine Hessian estimate yields the unchanged

\[
E_{\rm raw}\le C_0 e\lambda^{-3},\qquad
\lambda=a^3\sqrt v,\quad v=(1+y_1y_2\rho)/2.
\]

This closes the radius-one tube under the first primal restrictions stated above.

#### 3. Forward and prediction bounds with the displayed numerical constants

Across the nonlinear and affine states in the tube, direct action expansions give

\[
\|z_e^1-z_0^1\|\le E,
\quad\|z_e^2-z_0^2\|\le2bE+2eb^2,
\]
\[
\|z_e^3-z_0^3\|\le3b^2E+\tfrac92 eb^3.
\]

The reference affine tube bounds are \(b^2\le235M^2\), \(b^3\le3600M^3\), where

\[
M=(3/(\sqrt2\lambda))^{1/4},\quad M^2<1.5\lambda^{-1/2},
\quad M^3<1.84\lambda^{-3/4}.
\]

Therefore the last line is bounded by
\((1057.5C_0+29808)e\lambda^{-7/2}\), which is smaller than
\(C_z e\lambda^{-7/2}\), since \(C_z=1500C_0\) and \(C_0\) exceeds the required numerical constant. The lower layers obey the same upper bound. This verifies the reference Cz despite the extra growth term.

The reference raw radius-one tube also bounds the normalized active first root p by b: its norm change is controlled by raw first-layer displacement. This bound is stronger than a bound on the unnormalized sample projections and is used in the next affine prediction estimate.

At a common state, the projected prediction perturbation is at most
\(8eb^4\). The affine state comparison retains its factor lambda:
\(|g_0(\Theta_e)-g_0(\Theta_0)|\le\lambda b^3E\).
Using \(b^4\le235^2M^4\), \(M^4=3/(\sqrt2\lambda)<2.122\lambda^{-1}\), and \(\lambda\le1\), their sum is below

\[
(10^6+6624C_0)e\lambda^{-11/4}
< C_g e\lambda^{-11/4},\qquad C_g=14400C_0.
\]

Hence the same numerical primal restrictions give \(g_{e,R}(S)\ge5/4\). The two-Lipschitz square-root regression estimate from the preceding note remains valid because psi is one-Lipschitz. It yields activation regression error at least \(e^2\eta_\psi/4\) throughout the feature interval. All these comparisons are cap uniform.

#### 4. Raw learned moments avoid the inactive-variance issue

One must not infer \(e/\sqrt\delta\lesssim eM^4\) for the *intrinsic* M above: when \(v\) approaches one, the inactive variance \(1-v\) can be arbitrarily small while M stays bounded. The crude S-inverse norm bound in the reference normalized-gates note only proves that statement with its global delta envelope, not with this intrinsic M. No such inverse is needed for the original-time source coefficients.

Use the typed Qf,Qb bases from the preceding note, without normalizing by S. Their norm conversion costs are fixed numerical constants. Across the actual nonlinear and affine states,

\[
\|\Delta h^1\|\le E+2eb,\qquad
\|\Delta\delta^3\|\le E+eb,
\]
\[
\|\Delta h^2\|\le2bE+\tfrac92eb^2,\qquad
\|\Delta\delta^2\|\le2bE+\tfrac94eb^2.
\]

The second backward inequality follows by first expanding B-star times delta3 and then adding its local e-weighted gate term. These bounds require only \(b\le16M\) and \(E\le C_0e\lambda^{-3}\le C_0eM^{12}\).

For each Gram entry, \(|\langle u,u'\rangle-\langle v,v'\rangle|\) is bounded by the sum of two products with one discrepancy factor. The forward h1 and backward delta3 Grams therefore have error
\(C(bE+eb^2)\); the forward h2 and backward delta2 Grams have error
\(C(b^3E+eb^4)\). Explicitly the largest coefficient from the displayed factors is below 15 before the harmless two-slot conversions. A single bound

\[
32(b^3E+eb^4)h_j
\le32(4096C_0+65536)eM^{15}h_j
\le\bar H eM^{15}h_j
\]

covers every learned coefficient discrepancy, including the control factor (which has magnitude 1/2). Only strict learned terms carry h_j, exactly as in the source formulas. The total original feature duration satisfies \(S\le M^4\), so the corresponding backward row error is at most \(\bar H eM^{19}\).

This establishes the needed intrinsic learned-moment input directly, with no small inactive denominator, no assumption on random sample-gate diagonality, and no unproved estimate on a normalized nonlinear remainder. It applies to both the bounded and linear-growth shape classes.

#### 5. Source values with linear growth: the self terms have the same powers

On the power-four sector box, replace H by the enlarged \(K=\bar H\). The already proved affine/source transfers then obey

\[
|R_i|_r,|L_i|_r\le K^2M^5,\quad
|F|_r,|V|_r,|U_{\rm top}|_r\le K^3M^4,
\]
\[
|B_2|_r\le K^2M^9,\quad|B_3|_r\le K^2M^7,
\quad|EH_c|_r\le KM^4.
\]

Primitive Gaussian standard deviations in their source order are at most
\(K,KM^2,KM,KM,KM^2\). The exact source identities remain

\[
Z_1=R_1Z_{1,0}+(F/a)\zeta_1
+e(F/a^2)[d_1+aB_2\psi(Z_1)],
\]
\[
Z_2=R_2\xi_2+(V/a)\zeta_2
+e(V/a^2)[d_2+aB_3\psi(Z_2)],
\]
\[
Z_3=R_{\rm top}\xi_3+eU_{\rm top}[d_3+aEH_c\psi(Z_3)].
\]

Here \(|d_j|\le|q_j|\), and
\(q_1=\zeta_1+B_2(aZ_1+e\psi(Z_1))\), with the analogous formulas for q2 and C. For \(p\ge2\), write Zjp for the supremum of individual Lp norms, not the norm of a random time supremum.

At the bottom, \(|\psi(Z)|\le1+|Z|\) gives

\[
\|q_1\|_p\le KM^2\sqrt p+2K^2M^9Z_{1p}+eK^2M^9,
\]

so the nonlinear bracket is bounded by
\(KM^2\sqrt p+3K^2M^9Z_{1p}+2K^2M^9\).
Multiplying by the row bound \(4K^3M^4\) for F/a2 shows that its self coefficient is at most \(12eK^5M^{13}\). The remaining forcing terms are at most

\[
K^3M^5\sqrt p+2K^4M^6\sqrt p
+4eK^4M^6\sqrt p+8eK^5M^{13}.
\]

For K at least 100 and \(eK^{22}M^{19}\le1\), this is at most \(K^6M^6\sqrt p\), and the self coefficient is at most \(eK^6M^{13}\). Thus the reference bottom inequality remains valid.

At the middle the identical calculation replaces the backward row exponent 9 by 7 and gives self coefficient at most \(12eK^5M^{11}\). Its direct forward source has power \(5+1=6\), hence

\[
Z_{2p}\le K^6M^6\sqrt p+eK^6M^{11}Z_{2p}.
\]

At the top, the bracket is bounded by \(3KM^4Z_{3p}+2KM^4\), so its self coefficient is at most \(3eK^4M^8\); the direct forward source has power \(5+2=7\). Thus

\[
Z_{1p}\le K^6M^6\sqrt p+eK^6M^{13}Z_{1p},
\quad Z_{3p}\le K^6M^7\sqrt p+eK^6M^8Z_{3p}.
\]

Under the stated source smallness all three self coefficients are below 1/2. Absorption yields exactly the reference moment exponents:

\[
\|q_1\|_p\le K^{10}M^{15}\sqrt p,\quad
\|q_2\|_p\le K^{10}M^{13}\sqrt p,\quad
\|C\|_p\le K^{10}M^{11}\sqrt p.
\]

The direct raw primal L2 bounds remain \(KM^3,KM^2,KM\), because h and delta obey the same ball envelopes. These are the smaller norms used after bounding the perturbative exponential, as in the existing response proof.

#### 6. Response defects, exact numerical closure, and downstream limits

The random gate derivatives depend only on psi-prime and psi-double-prime, whose bounds are unchanged. The reference same-array single-insertion identities, the full current returns, the perturbative exponential envelope, and the Cauchy–Schwarz step with actual primal L2 therefore remain unchanged. Section 4 supplies the only learned-moment input that needed extra attention. With K=Hbar the complete defect bound is

\[
q_{\rm def}\le K^{30}eM^{19}
\quad\text{provided }eK^{22}M^{19}\le1.
\]

The existing positive sector supersolution requires
\(q_{\rm def}\le K^{-16}M^{-12}\). It is sufficient to impose

\[
eM^{31}\le\tfrac12K^{-46}.
\]

Indeed then the defect is at most \(K^{-16}M^{-12}/2\), while
\(eK^{22}M^{19}\le K^{-24}M^{-12}/2<1\). Also
\(M\le24^{1/4}\delta^{-1/8}\), so exactly the stated
\(e\le\frac12 24^{-31/4}K^{-46}\delta^{31/8}\) implies the intrinsic restriction. The exponent and prefactor follow from these inequalities, with no unstated lower bound on a mesh step.

For strict amplitude homotopy closure, all bounded-primal comparisons hold on the proposed source box and the supersolution returns bounds strictly inside it. At each fixed cap and sufficiently fine fixed mesh the coefficients depend continuously on e, including linearly growing C2 shapes by the displayed growth/derivative bounds and Gaussian moments. A first exit is contradicted. The previous fixed-program construction and then strong cap removal apply.

The generic conditioning maps are globally Lipschitz C1 at fixed cap, because phi has linear growth and bounded first derivative, while DR has bounded first derivatives. The velocity query proof uses bounded phi-prime and phi-double-prime and its original product-query truncation. The asymmetric cap comparison uses bounded psi-double-prime and unchanged incoming-field subGaussian tails. Thus the first-hit clock, all-time physical existence, nonsymmetric uniqueness/restart and every stipulated GF/GD/path/velocity/adjoint observable limit have the same proofs as the bounded-class note.

The initial-motion proof also extends verbatim with the already checked substitutions: global nonaffinity of C2 psi is equivalent to psi-double-prime not being identically zero, while phi-prime is at least 1/4. At initialization all needed expectations are finite under linear growth. The odd/even decomposition argument in the preceding note gives the same lower kernel bound without assuming psi odd.

#### 7. Uniform classes and examples

The natural norm on differences is

\[
\|u\|_* = \max\{|u(0)|,\|u'\|_\infty,\|u''\|_\infty\}.
\]

For \(\nu\le260\), Minkowski and \(|u(z)|\le|u(0)|+\|u'\|_\infty|z|\) give
\(\|u(\nu G)\|_2\le261\|u\|_*\).
Distance to the affine regression subspace therefore gives

\[
|\sqrt{\mathcal R_{\psi+u}(\nu G)}-
\sqrt{\mathcal R_\psi(\nu G)}|\le261\|u\|_*.
\]

For a nonaffine center of norm strictly below one, a ball of radius at most
\(\min\{(1-\|\psi\|_*)/2,\sqrt{\eta_\psi}/522\}\)
stays in the normalized class and has a common regression margin at least \(\eta_\psi/4\). The same activation coefficient c(delta) works throughout that full, nonodd, infinite-dimensional ball.

Unbounded examples already normalized into the class include
\(\psi(z)=\log(1+e^z)\) and \(\psi(z)=\sqrt{1+z^2}\). Their derivative bounds follow directly: softplus has derivative sigmoid in (0,1), second derivative at most 1/4 and value log2 at zero; the square-root shape has derivative z/sqrt(1+z2), second derivative (1+z2)^(-3/2), and value one at zero. The bounded oscillatory, saturating and compact-support examples from the preceding note are all included as well.

For arbitrary global C2 psi with finite first/second derivative bounds and finite value at zero, divide by
\(B=\max\{1,|\psi(0)|,\|\psi'\|_\infty,\|\psi''\|_\infty\}\)
and require eB to satisfy the normalized coefficient restriction. Any affine component of psi is allowed; only a wholly affine psi fails the nonaffinity conclusion.

### F.4. Actual-primal L2 response estimate

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Exact input interface

Throughout, M=(3/(sqrt(2) a^3 sqrt(v)))^(1/4)>1 is the actual dataset endpoint scale, and H=C_B is the numerical constant in the quantitative theorem. Duration S is at most H M^4. Keep every original sample slot, forward and transpose named source, current return, cap, and positive mesh step.

The following same-array transfer bounds are needed on the outer coefficient box:

| Quantity | Bound |
|---|---:|
| strict density F,A2,V,A3 | H^2 |
| strict density Utop=Rtop A3 | H^2 |
| row R1,R2,Rtop,L2,Ltop | H^2 M^5 |
| row B2 | H^2 M^9 |
| row B3 | H^2 M^7 |
| row E Hc | H M^4 |

Here R1=(I-a^2 H_P B2)^(-1), R2=(I-a^2 A2 B3)^(-1), Rtop=(I-A3 K3)^(-1), L2=(I-a^2 B3 A2)^(-1), Ltop=(I-K3 A3)^(-1), and K3=a^2 E Hc. The strict density bounds imply rows of F,V,Utop at most H^3 M^4. Factors a^(-j), j<=4, are numerical because a>=1/2.

These bounds are full sample-block bounds. For random gates use the full two-by-two sample matrices; no claim of sample-diagonal random gates is made. Deterministic exchange symmetry only supplies the scalar-sector coefficient box from which the displayed bounds are proved. In particular, the true improved affine active Utop density is O(M^-1), and its inactive density is O(1), so the full bound H^2 is valid. The corresponding active F,V densities are O(M^-5), O(M^-3). Persistence on the larger nonlinear outer box belongs to the separate positive-supersolution argument; the response proof needs only the displayed interface.

The independently proved primal tube gives the actual cap/mesh source output norms

    sup_k ||q1_k||_2 <= H M^3,
    sup_k ||q2_k||_2 <= H M^2,
    sup_k ||C_k||_2  <= H M.

These are bounds on the actual capped program, not on the formal same-array affine comparison. For example q1=A* delta2 and q2=B* delta3, with ||delta_l||_2<=(a+e)||q_l||_2 and ||delta3||_2<=(a+e)||C||_2; the operator/readout/feature bounds give the displayed powers. The bounds |tau_R(q)|<=|q| and e<=1 make these estimates cap uniform. Their identity with the named source output laws holds at each fixed source program, as in the original bridge. Thus they are available before cap removal and before the new coefficient bootstrap closes.

Primitive Gaussian sources have standard deviations bounded, in their usual order, by

    Z1_initial: H;  zeta1: H M^2;
    xi2: H M;      zeta2: H M;   xi3: H M^2.

No independence beyond the existing source construction is required for the estimates below. Their arbitrary temporal correlations and singular covariance matrices cause no problem. Finally, every strict learned-moment discrepancy is at most H e M^15 h_j, hence each backward learned-moment row discrepancy is at most H^2 e M^19.

#### 2. Cap-uniform subGaussian source moments

Put h(Z)=arctan Z and d(Z,q)=g(Z) tau_R(q), so |h|<=pi/2 and |d|<=|q|. Exact same-array affine elimination in the nonlinear value equations gives

    Z1=R1 Z1_initial+(F/a) zeta1
       + e(F/a^2)[d1+a B2 h1],
    Z2=R2 xi2+(V/a) zeta2
       + e(V/a^2)[d2+a B3 h2],
    Z3=Rtop xi3+e Utop[d3+a E Hc h3].

The incoming fields satisfy exactly

    q1=zeta1+B2(a Z1+e h1),
    q2=zeta2+B3(a Z2+e h2),
    C=Hc(a Z3+e h3).

For p>=2 denote the supremum over k of the individual Lp norms of Zi_k by Zi,p. This is not an Lp norm of a random supremum over time. The input table yields

    Z1,p <= H^6 M^6 sqrt(p)+e H^6 M^13 Z1,p,
    Z2,p <= H^6 M^6 sqrt(p)+e H^6 M^11 Z2,p,
    Z3,p <= H^6 M^7 sqrt(p)+e H^6 M^8 Z3,p.

For example the bottom Gaussian term F zeta1 has power 4+2=6, and its nonlinear self term has power 4+9=13. The middle direct forward term has power 5+1=6, its self term power 4+7=11; the top has power 5+2=7 and self power 4+4=8. The e-weighted Gaussian and bounded-atan additive terms are covered by the displayed leading terms under e H^6 M^13<=1/2.

Absorbing all three self terms gives Zi,p <= H^7 M^{zi} sqrt(p), with z=(6,6,7). The incoming fields therefore satisfy

    ||q1_k||_p <= H^10 M^15 sqrt(p),
    ||q2_k||_p <= H^10 M^13 sqrt(p),
    ||C_k||_p  <= H^10 M^11 sqrt(p).                 (1)

Thus their subGaussian scales are at most H^11 times these powers. Indeed the usual power-series expansion of exp(Q^2/L^2), with the even-p versions of (1), converges uniformly when L is a sufficiently large fixed multiple of its displayed coefficient. This argument proves the subGaussian claim; it does not assume that an arbitrary L2 action preserves Gaussian tails.

#### 3. Formal derivatives with both current and source-time factors

For one local population use

    Z=xi+K delta, q=zeta+B Hfeat,
    Hfeat=phi(Z), delta=Dcap(Z,q).

The pairs (K,B) are (H_P,B2), (A2,B3), (A3,E Hc). Define

    R=(I-a^2 K B)^(-1), U=R K,
    L=(I-a^2 B K)^(-1).

All three U strict densities are at most H^3. The relevant forward/backward R,L rows are at most H^2 M^5; at bottom only R is needed. Let b=(9,7,4) be the powers for B.

Freeze deterministic coefficients and source covariances. Write J for the formal derivative of Z in named source directions, with direct source matrices Ixi,Izeta. Set

    G=aI+DeltaG, Vgate=aI+DeltaV,
    Lgate=e diag(g'(Z) tau_R(q)),
    P=Lgate+a DeltaV B+a B DeltaG+DeltaV B DeltaG.

The gate bounds, including arbitrary caps, are

    |DeltaG_k|+|DeltaV_k| <= C e,
    |Lgate_k| <= C e Q_k,

where Q_k is the two-sample absolute incoming field norm (or |C_k| at top). No scalar-sector projection is applied to these random gates. Solving the affine part exactly gives

    J=Jaff+U[DeltaV Izeta+P J],
    Jaff=R Ixi+a U Izeta,                           (2)

    Ddelta-Ddelta_aff=L[DeltaV Izeta+P J].          (3)

To verify (3), before elimination its right-hand side is DeltaV Izeta+PJ+a^2 B(J-Jaff); substituting (2) yields (I+a^2 B U)[...]=L[...]. This uses the backward resolvent in its correct orientation and retains the current term in L.

For a single bottom/middle transpose slot j, J_k=0 for k<=j, and the direct forcing in (2) is bounded by H^3 h_j. For a full middle/top forward-source row, the direct forcing has row norm at most H^3 M^5; pad rows by zeros at future slots. The strictness of U and the full causal B-row bound yield

    |J_k| <= H^3 h_j E_k             (transpose slot),
    |J_{k,bullet}|_r <= H^3 M^5 E_k (full forward row),

    E_k=exp{H^6 e sum_{r<k} h_r(Q_r+M^b)}.          (4)

Here is the chronological bound explicitly. The Lgate part of UPJ costs at most C e sum_{r<k}h_r Q_r |J_r|. The other terms cost at most C e M^b sum_{r<k}h_r max_{s<=r}|J_s|. Replacing the derivative norm by its running maximum gives a scalar causal inequality whose majorant is the initial forcing times product_r(1+H^6 e h_r(Q_r+M^b)); the product is at most (4). The transpose initial factor h_j remains in every term. This reasoning includes any causal current B_rr, since r<k in U and the B history satisfies s<=r. It introduces no random time supremum of Q.

For the three source populations, the largest integrated stochastic powers in (4) are 4+(15,13,11)=(19,17,15); the deterministic powers are 4+b=(13,11,8). Consequently the explicit condition

    e H^22 M^19 <= 1                               (5)

ensures E E_k^8 <= 2, after the harmless numerical slack already built into H. One direct proof is weighted Jensen:

    exp(t sum_{r<k}h_r Q_r)
      <=1-s_k/S+sum_{r<k}(h_r/S) exp(t S Q_r).

Apply the subGaussian estimate (1) to each summand. The rate prefactor H^6, duration H, and subGaussian prefactor H^11 multiply to H^18; the spare H^4 in (5) controls factors 8, fixed two-sample conversions, and the scalar Gaussian exponential estimate. The same bound proves any lower fixed moment used below. It also implies value absorption in Section 2.

Now use the stronger, actual primal L2 bounds from Section 1. For every pair of times k,r, Cauchy-Schwarz gives

    E[Q_r E_k] <= ||Q_r||_2 ||E_k||_2
       <= H^2 M^{q_primal},
    q_primal=(3,2,1).                              (6)

This is the exponent improvement. It needs no independence between Q_r and E_k. In particular it applies with r=k and at the original source time, so terminal and source-time multipliers remain present. If an intermediate use of Hölder keeps two such explicit multipliers, the available eighth moments in (4) and the corresponding fixed Lp source bounds provide the original finite-moment truncation requirements; the single derivative defects (2)-(3) themselves contain only one explicit Q factor and use exactly (6).

#### 4. All four derivative defects

For a single bottom/middle transpose source, subtract Jaff in (2). The term U DeltaV Izeta has density at most H^4 e. For UPJ insert the transpose bound in (4), apply (6) to Lgate, and apply the deterministic B-row bound to the other three terms. The sum of time weights is at most H M^4. Hence

    E|J_k-Jaff,k| <= H^20 e h_j M^4
                        (M^{q_primal}+M^b).

Since b=9 at bottom and b=7 at middle, this gives strict-density bounds H^20 e M^13 and H^20 e M^11. Multiplying the output by its feature gate G adds only H^4 e h_j; thus the two forward coefficient derivative defects satisfy

    A2 defect density <= H^21 e M^13,
    A3 defect density <= H^21 e M^11.               (7)

For middle/top backward coefficients the source is a complete forward-source row, so Izeta=0. Identity (3), the row bound for L, the forward derivative row bound in (4), and (6) give

    max_k E[sum_{j<=k}|(Ddelta-Ddelta_aff)_{kj}|]
       <= H^19 e M^5 M^5 (M^{q_primal}+M^b).

The resulting powers are

    B2 defect row <= H^19 e M^17,
    B3 defect row <= H^19 e M^14.                   (8)

The deterministic gate terms a DeltaV B and a B DeltaG are retained: they are why the middle exponent here is 17 rather than the tempting but incomplete 12. The maximum over terminal times is outside expectation: for each fixed k, expand the deterministic L row, sum the absolute j entries, and apply (6) uniformly to every pair of times appearing in PJ. This gives the displayed bound uniformly in k. Consequently it bounds max_k sum_{j<=k}|E[(Ddelta-Ddelta_aff)_{kj}]|, which is the deterministic coefficient row norm. No expectation of a random maximum over k is claimed. It includes j=k. In particular Lgate_k J_kk is explicitly controlled using Q_k in (6), and current B_kk factors occur in the retained causal B row. No strict-density estimate for arbitrary backward forcing, nor a minimum step, has been assumed.

Adding the learned-moment density H e M^15 and backward row H^2 e M^19 yields the complete actual coefficient forcing interface

    q <= H^30 e M^19,                              (9)

under (5). It applies to every amplitude along the fixed-cap, fixed-mesh homotopy as long as the source transfer table holds. The response estimates compare with the affine formulas at the exact same deterministic arrays, so there is no uncounted coefficient displacement term.

#### 5. Numerical and theorem interface

The deliberately rounded H ledger is:

| Step | Prefactor |
|---|---:|
| outer transfer bounds | H^2 (rows of strict kernels H^3) |
| Gaussian Lp inputs | H^2 |
| value leading/self inequalities | H^6 |
| absorbed Zi | H^7 |
| incoming Q Lp | H^10 |
| incoming subGaussian scales | H^11 |
| derivative initial factor | H^3 |
| exponential rate before time integration | H^6 |
| E[Q_r E_k], using actual primal L2 | H^2 |
| transpose defect | H^20 |
| feature defect | H^21 |
| backward full row defect | H^19 |
| full forcing, including learned moments | H^30 |

Each entry follows from the displayed products and sums. The excess H powers cover a^(-j)<=16, two sample slots and basis changes, fixed Gaussian constants, and factors at most 10^6, using H>=10^30. There is no exponential depending on M except the e-weighted one in (4), already controlled by (5).

If the independent supersolution supplies the strict outer-box closure at

    q <= H^-C M^-12

for any fixed C comfortably below 350, then (9) is compatible with eM32 <=10^-70 H^-399: indeed q M12 <= H^30 eM31 <=10^-70 H^-369. Condition (5) also holds. Since M32 <=24^8 delta^-4 and 24^8<H, the unchanged prefactor e<=c_poly delta^4 implies that smallness.

This proof unit supplies the new response part, not the new affine G3 proof or the coefficient supersolution. Once those interfaces are checked, all original cap removal, clocks, nonsymmetric uniqueness and restart, full-width GF/raw-GD limits, action/kernel/path/velocity laws, and nonaffinity/motion conclusions use exactly the reference bridges. The only replacement is (9) and its verified smallness condition (5).

### F.5. Positive sector supersolution with explicit numerical margins

Within this proof unit, unqualified section and equation numbers are local.

Write H=C_B for the original explicit numerical constant. In particular H >= 10^30. M always means the intrinsic endpoint scale

    M=(3/(sqrt(2) a^3 r))^(1/4),  r=sqrt(v),  1/2<=a<=1.

Thus r=3/(sqrt(2)a^3) M^-4 exactly. The uniform delta envelope is used only in the final paragraph.

The decisive points are separate active/inactive outer radii, the improved affine strict densities in the active sector, and using the raw primal L2 bound in Holder AFTER bounding the derivative exponential's moments. The latter does not require an improved subGaussian estimate or a covariance perturbation estimate.

#### 1. Exact input interface

Use original feature-time steps h_j, strict density |K|d=max_{j<k}|K_kj|/h_j, and complete causal row norm |Q|r=max_k sum_{j<=k}|Q_kj|. Current diagonals of all backward errors are admitted.

The required improved affine certificate, for beta=b1,b2,b3 and beta_far from Fragment E.5 Section 8, is the following. Every displayed coefficient is at most H:

    S <= H M^4;
    active |A2|d,|F|d <= H M^-5;
    active |A3|d,|V|d <= H M^-3;
    active |B3|r,|T|r <= H M^7;
    active |B2|r,|W|r <= H M^9;
    |R1|r,|R2|r,|L2|r,|Rtop|r,|Ltop|r <= H M^5;
    active |Utop|d <= H M^-1;
    active |F L2|d,|R2 F|d <= H M^-1.

The inactive forward densities, including Utop, are at most H, and its affine backward arrays vanish; its resolvents are identity. The same probe argument as the existing certificate produces these orders by replacing its G=M^5 by G=M^3. The product bound follows from beta positivity, A3 density M^-3, and beta gap M^-2. The exact top probe, including Ltop, is still required; no product-of-row-norm shortcut is substituted.

The intrinsic beta gaps obey b_(j+1)-b_j >= H^-1 M^-2. Active lower bounds, independent of the sharper upper bounds, are

    F_kj,V_kj >= H^-2 M^-8 h_j.                       (1)

Gaussian source standard deviations remain <=H times 1,M^2,M,M,M^2 for (Z1_initial,zeta1,xi2,zeta2,xi3). The established raw tube supplies

    ||q1_k||2 <= H M^3, ||q2_k||2 <= H M^2,
    ||C_k||2 <= H M.                                 (2)

These follow by applying the actual bounded raw actions: q2=B*delta3 and q1=A*delta2, with all gates bounded, |tau_R(q)|<=|q|, and raw A,B,C bounded by constant times M. They also hold in the fixed-cap, sufficiently fine fixed-mesh source laws, by their existing raw/source identification. Only second moments are used here. The reference learned-memory discrepancy remains <= H e M^15 h_j at strict entries, and hence <= H^2 e M^19 in backward row norm.

#### 2. The outer box and all source transfers on it

All actual deterministic source coefficient blocks are sample diagonal by the exchange-equivariance induction in Fragment E.7 Section 2. Random gates can mix the two sectors; all value and derivative bounds below retain full two-by-two gate norms.

At beta=b2 define the outer box by:

* active |Aell| <= Aell,b2 entrywise;
* active |Bi| <= Bi,b2+Ji entrywise for nonnegative causal Ji with |Ji|r <= ra:=H^-10 M^-2, i=2,3;
* inactive |Aell| <= Aell,1+Htime entrywise, where Htime_kj=h_j for j<k;
* inactive |Bi|r <= ri:=H^-10 M^-5, i=2,3.

Equivalently the active Ji can be the positive part of |Bi|-Bi,b2. No density estimate on Ji is assumed.

On the active majorant, with subscript b denoting beta=b2,

    F=Fb+Fb J2 F, V=Vb+Vb J3 V,
    R2=R2b+Vb J3 R2,
    L2=L2b+L2b J3 V,
    R1=R1b+Fb J2 R1.

The two Neumann row ratios are bounded by

    |Fb|r |J2|r <= H^-8 M^-3,
    |Vb|r |J3|r <= H^-8 M^-1,

because |Fb|r<=H^2 M^-1 and |Vb|r<=H^2 M. Hence active F,V retain strict densities at most 2H M^-5,2H M^-3. R1,R2 retain rows at most 2H M^5. For the reverse resolvent use its exact identity: |L2|r<=H M^5(1+ra |V|r)<=2H M^5. This avoids the invalid claim that a right row multiplier preserves strict density. Rtop,Ltop,Utop depend only on A3 and are bounded directly by monotonicity.

In the inactive sector, A densities are <=2H, while S ri<=H^-9 M^-1. Every relevant Neumann ratio is at most 2H^-8 M^-1; F,V,Utop have bounded strict densities, forward/reverse resolvents have bounded rows, and K3 vanishes. In particular no M^-2 inactive radius is being used.

After the fixed two-sample norm conversion, the following full-sector bounds all have prefactor H^2 (enlarging this to H^3 for gain factors is harmless):

    |F|d,|V|d,|Utop|d <= H^2,
    |R1|r,|R2|r,|L2|r,|Rtop|r,|Ltop|r <= H^2 M^5,
    |B2|r <= H^2 M^9, |B3|r <= H^2 M^7.

Thus the larger active outer radius does not enlarge the source moment or derivative exponents. The inactive radius is separate and remains small enough.

#### 3. Positive supersolution with arbitrary backward row defects

For nonnegative forward strict defects E2,E3 of density <=q and arbitrary nonnegative causal backward defects J3,J2 of row <=q, fix beta=b1. Use the following positive affine construction:

    A2*=A2b, A3*=A3b, B3*=B3b+J3,
    R*=(I-a^2 A2b B3*)^-1,
    W*=a^2 B3*R*, B2*=B2b+(W*-Wb)+J2.              (3)

The backward inequalities hold exactly, because the learned affine moments increase with beta and the affine variance multiplier beta^2 exceeds one. All added arrays are nonnegative.

The finite causal identities are

    R*=(I-Vb J3)^-1 R2b,
    W*-Wb=a^2 L2b J3 R*,
    Fb(B2*-B2b)Fb
       =Fb J2 Fb+a^2(Fb L2b)J3(R*Fb).              (4)

The single sandwich inequality used here is

    |U Q V|d <= S |U|d |Q|r |V|d.                  (5)

It follows by expanding the entries and using the strict right factor's h_j. It holds for every positive-step mesh, including arbitrary current diagonals in Q.

Under q<=H^-16 M^-12, |Vb|r q<=H^2 M q<1/2. The numerical ledger is:

| Quantity | Upper bound |
|---|---|
| R* row | H^2 M^5 |
| R*Fb density | H^2 M^-1 |
| Fb J2 Fb density | H^3 M^-6 q |
| (Fb L2b)J3(R*Fb) density | H^4 M^2 q |
| Fb(B2*-B2b)Fb density | H^5 M^2 q |
| eta defined by Fb(B2*-B2b)Fb<=eta Fb | H^7 M^10 q |
| Vb J3 Vb relative to Vb | H^5 M^6 q |
| E2/Fb, E3/Vb | H^2 M^8 q |
| W*-Wb row | H^3 M^10 q |
| either total backward excess in (3) | H^4 M^10 q |

The first five lines use only (4),(5) and the exact active bounds; the relative lines use (1). Since eta<1/2, termwise positivity gives

    F(B2*)-Fb <= [eta/(1-eta)] Fb <=2eta Fb.

Indeed [Fb(B2*-B2b)]^n Fb<=eta^n Fb by induction. No norm of a coupled inverse is inserted. The V expansion gives the corresponding relative increment <=2H^5 M^6q.

The total first-forward relative error is <=H^8 M^10 q, and the total second-forward error is <=H^7 M^8q. Available slack is

    A2b-(Fb+M_A2,1) >= (beta^2-1)Fb,
    A3b-(Vb+M_A3,1) >= (beta^2-1)Vb,
    beta^2-1 >= H^-1 M^-2.

Therefore

    q <= H^-16 M^-12                              (6)

puts both forward errors below half the available slack. This proves (3) is a supersolution. Finite chronological comparison also applies to signed coefficients because |T0(C)|<=T0(|C|).

The inactive proof is unchanged, with

    A2*=A2,1+u Htime, A3*=A3,1+w Htime,
    B3*=J3, R*=(I-a^2 A2*J3)^-1,
    B2*=a^2 J3R*+J2,
    u=H^3 M^4 q, w=H^5 M^4 q.

Under (6) the Neumann ratio is <1/2, backward rows are <=3q, and the forward increments have the stated densities. This construction includes all current backward diagonals.

The supersolution lies strictly inside the outer box. In the active sector its backward excess is <=H^4 M^10q<=H^-12 M^-2<ra/2. In the inactive sector 3q<ri/2 and u,w<1/2. Integrating the positive beta derivatives supplies the entrywise forward margin

    Aell,b2,kj-Aell,b1,kj >= H^-3 M^-10 h_j>0.

These margins hold at each fixed mesh without a lower bound on h_j.

#### 4. Full nonlinear response and the raw-L2 improvement

On the outer box the exact value identities in Fragments E.9 and F.4 Section 3 apply. Using the full-sector bounds from Section 2, one obtains

    Z1,p <= H^6 M^6 sqrt(p)+e H^6 M^13 Z1,p,
    Z2,p <= H^6 M^6 sqrt(p)+e H^6 M^11 Z2,p,
    Z3,p <= H^6 M^7 sqrt(p)+e H^6 M^8 Z3,p.

For instance the bottom leading terms cost M^5 and M^4 M^2=M^6, and its self term costs M^4 M^9=M^13. The middle leading terms cost M^5 M=M^6 and M^4 M=M^5; its self term is M^4 M^7=M^11. The top has M^5 M^2=M^7 and self term M^4 M^4=M^8.

Under e H^22 M^19<=1 these self terms absorb. Consequently the incoming fields obey

    ||q1_k||p <= H^10 M^15 sqrt(p),
    ||q2_k||p <= H^10 M^13 sqrt(p),
    ||C_k||p  <= H^10 M^11 sqrt(p), p>=2.            (7)

The corresponding subGaussian scales have prefactor H^11. These are suprema of deterministic Lp norms, not random temporal suprema.

For each local population let R=(I-a^2KB)^-1, U=RK, L=(I-a^2BK)^-1. Here |U|d<=H^3 in all three populations; the full forward-source row and both middle/top backward resolvents have row bound H^3 M^5. The exact derivative identities, including terminal and source current factors, are

    J=Jaff+U[DeltaV Izeta+P J],
    delta_derivative-delta_aff_derivative
         =L[DeltaV Izeta+P J],
    Jaff=R Ixi+aU Izeta,
    P=Lgate+a DeltaV B+aB DeltaG+DeltaV B DeltaG.

Gates satisfy |DeltaG|,|DeltaV|<=Ce and |Lgate_k|<=Ce Q_k. They may mix sample sectors. Strictness of U and the causal product majorant give

    |J_kj| <= H^3 h_j E_k       (single transpose source),
    |J_k,bullet|r <= H^3 M^5 E_k (full forward-source row),
    E_k=exp{e H^6 sum_(r<k) h_r(Q_r+M^b)},

where b=(9,7,4) and the Q subGaussian powers are (15,13,11). Therefore the stochastic integrated exponents are (19,17,15), and the deterministic ones are (13,11,8). The weighted Jensen argument of the existing response proof, with rate H^6, duration H, and subGaussian scale H^11, shows that moments through order eight of E are <=2 whenever

    e H^22 M^19 <=1.                               (8)

At this point use (2), rather than the larger scales in (7):

    E[Q_r E_r] <= ||Q_r||2 ||E_r||2
                  <= H^2 M^qraw,
    qraw=(3,2,1).                                  (9)

If extra terminal or source-time multipliers are retained in a product, use the corresponding higher envelope moments and the available raw fixed moments only when established; they are not needed for the coefficient estimates below. The two exact derivative identities above reduce every coefficient error to a single P insertion and a single derivative envelope. Thus (9), with one Q, suffices. No raw Lp claim beyond L2 is made.

For a single bottom/middle transpose source, the expected defect has density

    e H^20 M^[4+max(qraw,b)],

because the two U density factors carry power zero and time integration costs M^4. Hence the two feature derivative defects have density <=H^21 e M^13 and H^21 e M^11, including the direct source and terminal feature gates.

For the middle/top backward coefficients use the exact L P J identity with Izeta=0 and the complete forward-source row, not a bound on its pieces before solving the backward resolvent. The two row factors cost M^5 each, yielding

    B2 derivative row defect <=H^21 e M^17,
    B3 derivative row defect <=H^21 e M^14.           (10)

The gate-curvature contributions alone are smaller: powers 12 and 11. The dominant terms in (10) are the bounded gate perturbations times the deterministic B row powers 7 and 4. The estimates include j=k. Precisely the estimate is max_k E[sum_{j<=k}|(delta_derivative-delta_aff_derivative)_{kj}|], with the terminal-time maximum outside expectation. It bounds the deterministic coefficient row norm max_k sum_{j<=k}|E[(delta_derivative-delta_aff_derivative)_{kj}]|. No random temporal maximum is taken inside expectation.

Finally add the independently proved learned-memory errors. Their strict densities are <=H e M^15, and complete backward rows <=H^2 e M^19. Thus all four coefficient forcing components satisfy

    q <= H^30 e M^19,                              (11)

under (8), uniformly in cap and sufficiently fine fixed mesh. The reference H^30 budget is ample: value absorption uses H^6, derivative rate H^6, envelope base H^3, duration H, and raw-L2 expectation at most H^2; every displayed product and fixed sum fits below H^21 before the final H^30 rounding.

#### 5. Homotopy and the delta-only amplitude

At each fixed cap and sufficiently fine mesh, continue the actual source program in amplitude te, 0<=t<=1. It begins strictly inside the outer box. At a proposed first exit, (8),(11) apply, and the exact positive supersolution of Section 3 puts every boundary inequality strictly inside, provided

    H^30 e M^19 <= H^-16 M^-12,
    equivalently e M^31 <= H^-46.                  (12)

This contradicts first exit. The proof retains deterministic sample exchange symmetry, random gate mixing, arbitrary causal backward forcing including current diagonals, and no smallest-step hypothesis.

The existing cap removal, scalar physical clock, nonsymmetric uniqueness/restart, full-width GF/raw-GD, action/kernel/path/velocity laws and initial-motion/nonaffinity bridges now apply with the sharpened affine certificate E.6. The reference primal restriction e<=c_* delta^(7/4) is automatic under the proposed delta^4 amplitude.

Indeed M<=24^(1/4)delta^-1/8 implies M^32<=24^8 delta^-4, and 24^8<H. With the unchanged displayed numerical constant

    c_poly=min(1/4,c_*,10^-70 H^-400),
    e<=c_poly delta^4,

one has e M^32<=10^-70 H^-399. Since M>1, this implies both (8) and (12), with very large strict margins. Thus this closure establishes the complete power-four amplitude once the improved affine input is verified; the deterministic box and nonlinear response have no remaining exponent gap.

### F.6. Exact affine positivity and transfer table

Within this proof unit, unqualified section and equation numbers are local.

#### 2. Exact normalized affine setup

Work only in the active mean/contrast sample sector after label folding
and the exact normalization already displayed in the power-ten source
certificate. Let \(H\) denote the strict integration matrix on an arbitrary
positive finite mesh, \(H_{kj}=h_j\) for \(j<k\). The normalized total
duration is \(T\le2\). All quantities below are scalar time arrays in
this active sector. The inactive sector is handled separately by its
explicit affine formulas.

Scale the initial first root and the two initial Gaussian matrices by
\(\beta\in[1,1.001]\). Let the primary affine fields be
\(p,A,B,C\), with

\[
 x_2=Ap,\quad x_3=BAp,\quad q_2=B^*C,\quad q_1=A^*B^*C.
\]

The source equations, with all deterministic arrays frozen, are exactly

\[
 p=\mathbf1 p_0+Hq_1,\quad q_1=\zeta_1+B_2p,
\]
\[
 x_2=\xi_2+A_2q_2,\quad q_2=\zeta_2+B_3x_2,
\]
\[
 x_3=\xi_3+A_3C,\quad C=Hx_3. \tag{2.1}
\]

The five groups \(p_0,\zeta_1,\xi_2,\zeta_2,\xi_3\) are mutually
independent centered Gaussian groups; \(\operatorname{Var}p_0=\beta^2\),
and

\[
 \operatorname{Cov}(\xi_{2,k},\xi_{2,j})
 =\beta^2\mathbb E[p_kp_j],\qquad
 \operatorname{Cov}(\xi_{3,k},\xi_{3,j})
 =\beta^2\mathbb E[x_{2,k}x_{2,j}]. \tag{2.2}
\]

The other source covariances are likewise \(\beta^2\) times the
corresponding backward-input second moments. Their covariance matrices
may be singular. No inverse covariance matrix is used here.

Define the actual affine transfer arrays

\[
 R_1=(I-HB_2)^{-1},\quad F=R_1H,\quad
 W_1=B_2R_1,\quad L_1=(I-B_2H)^{-1},
\]
\[
 R=(I-A_2B_3)^{-1},\quad V=RA_2,\quad
 W=B_3R,\quad L=(I-B_3A_2)^{-1},
\]
\[
 R_3=(I-A_3H)^{-1},\quad
 T_3=HR_3,\quad L_3=(I-HA_3)^{-1},\quad U=R_3A_3.
\tag{2.3}
\]

The subscript in \(T_3\) avoids confusing this transfer with the duration
\(T\). The arrays are finite causal polynomials because all products in
the inverses are strict triangular. The exact coefficient equations are

\[
 A_2=\beta^2F+M_1,\quad A_3=\beta^2V+M_2,
\quad B_3=\beta^2T_3+N_3,\quad B_2=\beta^2W+N_2,
\tag{2.4}
\]

where, at strict entries,

\[
 (M_1)_{kj}=h_j\mathbb E[p_kp_j],\quad
 (M_2)_{kj}=h_j\mathbb E[x_{2,k}x_{2,j}],
\]
\[
 (N_3)_{kj}=h_j\mathbb E[C_kC_j],\quad
 (N_2)_{kj}=h_j\mathbb E[q_{2,k}q_{2,j}].
\tag{2.5}
\]

The existing finite affine positivity argument applies here: normalized
ascent has positive scalar coefficients; expansion in the independent
Gaussian initialized coordinates gives nonnegative covariance terms by
Wick pairing; chronological Gaussian conditioning and (2.4) preserve
nonnegative entries. This is positivity of deterministic contractions
and source arrays, not positivity of realized Gaussian weights. In
particular all covariance entries occurring below are nonnegative.
Passing the finite-width expected contractions to their deterministic
fixed-mesh limits uses uniform integrability: every fixed affine Euler
prefix has polynomial bounds in its Gaussian initialized operator and
root norms, which have moments of every fixed order uniformly in width.

For a causal array let \(|K|_r=\max_k\sum_{j\le k}|K_{kj}|\), and
for a strict array let \(|K|_d=\max_{j<k}|K_{kj}|/h_j\).
The proof uses only

\[
 |AB|_d\le |A|_r|B|_d
\tag{2.6}
\]

when \(B\) is strict, and elementary row submultiplicativity. It never
asserts that multiplication by an arbitrary row-bounded array on the
right preserves strict density.

#### 3. Positivity converts raw variances into actual response rows

For a nonnegative deterministic row \(a_j\) and a centered Gaussian
group \(Z_j\) with every covariance entry at least \(m^2\),

\[
 \mathbb E\left(\sum_j a_jZ_j\right)^2
 =\sum_{i,j}a_ia_j\mathbb E[Z_iZ_j]
 \ge m^2\left(\sum_j a_j\right)^2. \tag{3.1}
\]

Only an entrywise lower bound on covariance is used. This is not a
positive lower bound on its smallest eigenvalue: perfectly correlated
sources are admissible.

Solving (2.1) at the actual coefficient arrays gives

\[
 p=R_1\mathbf1p_0+F\zeta_1,\quad
 q_1=W_1\mathbf1p_0+L_1\zeta_1,
\]
\[
 x_2=R\xi_2+V\zeta_2,\quad q_2=W\xi_2+L\zeta_2,
\]
\[
 x_3=R_3\xi_3,\quad C=T_3\xi_3. \tag{3.2}
\]

All arrays in (3.2) are nonnegative; every resolvent is at least the
identity entrywise. Independence makes the covariance contributions
from different source groups add without cross terms. The covariance
contribution from the second group in each expression has nonnegative
entries. Thus

\[
 \mathbb E[p_kp_j]\ge\beta^2,
\quad \operatorname{Cov}(\xi_{2,k},\xi_{2,j})\ge\beta^4,
\quad \mathbb E[x_{2,k}x_{2,j}]\ge\beta^4,
\quad \operatorname{Cov}(\xi_{3,k},\xi_{3,j})\ge\beta^6.
\tag{3.3}
\]

Let \(P=\max_k\|p_k\|_2\), \(X=\max_k\|x_{2,k}\|_2\),
\(Y=\max_k\|x_{3,k}\|_2\), \(D=\max_k\|C_k\|_2\),
\(Q_i=\max_k\|q_{i,k}\|_2\). Applying (3.1)--(3.3) proves

\[
 |R_1|_r\le P/\beta,\quad |W_1|_r\le Q_1/\beta,
\]
\[
 |R|_r\le X/\beta^2,\quad |W|_r\le Q_2/\beta^2,
\]
\[
 |R_3|_r\le Y/\beta^3,\quad |T_3|_r\le D/\beta^3.
\tag{3.4}
\]

These bounds concern the actual frozen formal-source arrays because
(2.1)--(2.4) define those arrays exactly. No identification of an
arbitrary raw tangent with a source derivative occurs. In particular
the independent-root probe argument and the raw-Hessian exponential
are unnecessary for (3.4).

Since \(R_1,R\ge I\), positivity also gives

\[
 |B_2|_r\le Q_1/\beta,\qquad |B_3|_r\le Q_2/\beta^2.
\tag{3.5}
\]

#### 4. An explicit complete algebraic transfer table

Assume \(R_*\ge1\) bounds every primary normalized field/operator,
namely \(\|p_k\|_2,\|A_k\|_{op},\|B_k\|_{op},\|C_k\|_2\le R_*\)
at every mesh node, and also \(\beta\le R_*\). Then
\(P,D\le R_*\), \(X,Q_2\le R_*^2\), and
\(Y,Q_1\le R_*^3\). With \(T\le2\) and \(1\le\beta\le1.001\),
the following bounds hold:

| Actual normalized affine array | Bound |
|---|---:|
| \(R_1\), row | \(R_*\) |
| \(W_1,B_2\), row | \(R_*^3\) |
| \(F\), strict density | \(R_*\) |
| \(A_2\), strict density | \(2R_*^2\) |
| \(R,W,B_3\), row | \(R_*^2\) |
| \(V\), strict density | \(2R_*^4\) |
| \(A_3\), strict density | \(4R_*^4\) |
| \(L\), row | \(5R_*^4\) |
| \(R_3\), row | \(R_*^3\) |
| \(T_3\), row | \(R_*\) |
| \(L_3\), row | \(9R_*^5\) |
| \(U=R_3A_3\), strict density | \(4R_*^7\) |
| \(L_1\), row | \(3R_*^3\) |
| \(RF\), strict density | \(R_*^3\) |
| \(FL\), strict density | \(3R_*^3\) |
| \(RFL\), strict density | \(3R_*^5\) |

Proof of the entries not already in (3.4)--(3.5):
\(F=R_1H\) gives its density bound. Cauchy--Schwarz gives
\(|M_1|_d\le P^2\), so
\(|A_2|_d\le\beta P+P^2\le2R_*^2\). Then
\(|V|_d\le |R|_r|A_2|_d\le2R_*^4\), and
\(|A_3|_d\le\beta^2|V|_d+X^2\le4R_*^4\).
Here \(2\beta^2+1<4\) throughout the stated beta range.

The identities

\[
 L=I+WA_2,\quad L_3=I+T_3A_3,
\quad L_1=I+W_1H
\]

give the displayed reverse rows by multiplication of row norms and
\(|A_i|_r\le T|A_i|_d\). The density bound for \(U\) follows by
left multiplication of \(A_3\) by \(R_3\). Likewise
\(|RF|_d\le R_*^3\).

The improvement for \(FL\) uses a genuine cancellation in the positive
coefficient equations. Equation (2.4) gives \(B_2\ge\beta^2W\), while

\[
 FB_2=R_1-I.
\]

Consequently, entrywise,

\[
 FL=F+FWA_2
 \le F+\beta^{-2}(R_1-I)A_2. \tag{4.1}
\]

Taking strict densities on the right proves
\(|FL|_d\le R_*+2R_*^3\le3R_*^3\). Left multiplication by
\(R\) proves the final \(RFL\) bound. No beta differentiation or
inverse beta gap appears in (4.1).

The interval \(1\le\beta\le1.001\) in this lemma is an algebraic
conditional range: a primal bound on a common interval is still required
for every beta to which the lemma is applied. The reference continuation proof
supplies that bound only for its narrower family
\(\beta-1=O(M^{-2})\), not for every beta up to 1.001 on the original
endpoint interval. No such wider continuation assertion is made here.

The table is conditional only on the actual affine primal bound, which
the existing balance/continuation argument supplies. For exact
continuous time with initial Gaussian actions bounded by ten,
\(\|A\|^2\le101\beta^2+\|C\|^2\) follows directly from
\(A^*A=p\otimes p+(A_0^*A_0-p_0\otimes p_0)\); the other primary
bounds are smaller. Thus one may take
\(R_*=(101\beta^2+\max\|C\|^2)^{1/2}\), with an arbitrarily small
additional fixed margin for sufficiently fine Euler meshes. All finite
mesh conclusions then remain uniform over that sufficiently fine class.

#### 5. Original-time consequences of the affine table

Retain the original slope range \(1/2\le a\le1\). Let
\(r=\sqrt{(1+y_1y_2\rho)/2}\), \(\lambda=a^3r\),
and \(M=(3/(\sqrt2\lambda))^{1/4}\). In the active sector the exact
normalizations give

\[
 A_2=(r/a)\widehat A_2,\quad A_3=ar\widehat A_3,
\quad B_3=(ar)^{-1}\widehat B_3,\quad B_2=(a/r)\widehat B_2.
\]

A normalized strict density gets an additional factor \(\lambda\)
on return to original feature time. Products \(FL,RF\) transform like
\(F\); \(U\) transforms like \(A_3\). Therefore, using only
\(R_*=O(M)\), the proved table implies the following orders, with
explicit algebraic constants obtainable from Section 4 and the existing
common enlarged-interval primal radius:

| Original-time active array | Order |
|---|---:|
| \(F\), density | \(M^{-7}\) |
| \(A_2\), density | \(M^{-6}\) |
| \(V,A_3\), density | \(M^{-4}\) |
| \(B_3\), row | \(M^6\) |
| \(B_2\), row | \(M^7\) |
| \(R_1,R,R_3,L,L_3\), respective rows | \(M,M^2,M^3,M^4,M^5\) |
| \(U\), density | \(M^{-1}\) |
| \(FL,RF\), density | \(M^{-5}\) |

These orders and the numerical normalized table are proved above.
#### 6. Activation-design boundary

Centering the odd arctangent perturbation can improve derivative
constants by a modest factor. For example

\[
 \phi_e(z)=z+e(\arctan z-z/2)
 =(1-e/2)z+e\arctan z
\]

has \(1-e/2\le\phi'_e\le1+e/2\). The choice \(e=1/2\) is
\(\phi(z)=3z/4+\arctan(z)/2\), an explicit moderate candidate in the
same odd shape family. The present affine positivity lemma does not
prove the desired global population limit for this candidate.

Merely making curvature tiny on the Gaussian bulk cannot certify strong
nonlinearity there. If an odd \(C^2\) activation has
\(\|\phi''\|_\infty\le K\), Taylor's theorem gives
\(|\phi(z)-\phi'(0)z|\le Kz^2/2\), hence

\[
 \inf_b\mathbb E[(\phi(G)-bG)^2]\le 3K^2/4.
\]

Thus a practical activation cannot be justified simply by hiding a
microscopic curvature coefficient inside a nominally order-one shape
coefficient. Bounded or piecewise-localized curvature still needs a
new cap-independent control of the actual \(q\)-weighted derivative
response when the nonlinear amplitude is moderate.

### F.7. Exact sample normalization and gate maps

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Exact transformed finite and population feature equations

Fold labels using oddness as in the existing theorem. Both controls in
feature time s are 1/2. Write
\[
v=(1+\rho_{\rm folded})/2,\quad r=\sqrt v,\quad
u=\sqrt{1-v},\quad S=\operatorname{diag}(r,u),\quad
Q=\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]
Both r,u are at least \(\sqrt{\delta/2}\). Here S is a two-by-two
sample matrix, not an interval length. Let \(e_+=(1,0)^T\),
\(\lambda=a^3r\), and \(t=\lambda s\). Matrices acting on neurons
commute with the displayed sample matrices.

For layer \(\ell=1,2,3\) define normalized preactivations, features,
backward fields and incoming backward fields by
\[
z^\ell=a^{\ell-1}Q^{-1}Sx^\ell,\qquad
h^\ell=a^\ell Q^{-1}S\widehat h^\ell,
\]
\[
\delta^\ell=a^{4-\ell}rQ^{-1}S^{-1}d^\ell,\qquad
q^\ell=a^{3-\ell}rQ^{-1}S^{-1}\widehat q^\ell.
\tag{1}
\]
The readout remains C. The actual cap acts in the original sample
coordinates inside the definitions below.

Put A=W2, B=W3. The equations are exactly
\[
x^2=A\widehat h^1,\quad x^3=B\widehat h^2,\qquad
\widehat q^3=Ce_+,\quad \widehat q^2=B^*d^3,\quad
\widehat q^1=A^*d^2,
\]
\[
\partial_t x^1=d^1,\quad
\partial_t A=\sum_{\alpha=+,-}d_\alpha^2\otimes
                  \widehat h_\alpha^1,\quad
\partial_t B=\sum_{\alpha=+,-}d_\alpha^3\otimes
                  \widehat h_\alpha^2,\quad
\partial_t C=\widehat h_+^3.                         \tag{2}
\]
These equations hold at the finite level and on the common population
actions; the finite cap/Euler program uses its own transformed mesh.
They are a change of coordinates and time for the same feature field.

For example, the first projected covariance is S^2, so its normalized
s-derivative is \(S Q\delta^1=\lambda d^1\).
Moreover
\(\tfrac12\sum_i\delta_i^\ell\otimes h_i^{\ell-1}
=\sum_\alpha(Q\delta^\ell)_\alpha\otimes
(Qh^{\ell-1})_\alpha
=\lambda\sum_\alpha d^\ell_\alpha\otimes
\widehat h^{\ell-1}_\alpha\).
The readout derivative is \(h_+^3=\lambda\widehat h_+^3\).
This verifies all factors in (2).

For affine activation, \(\widehat h^\ell=x^\ell\) and
\(d^\ell=\widehat q^\ell\). The normalized active equations are exactly
the homogeneous four-component system in the earlier polynomial
proof. The normalized inactive first root has variance one and its
reference fields are frozen, as in the original inactive-field lemma.

#### 2. The normalized nonlinear maps and their derivatives

The forward map is
\[
\mathcal H_\ell(x)
=a^{-\ell}S^{-1}Q
 \phi_{a,e}(a^{\ell-1}Q^{-1}Sx)=x+\mathcal R_\ell(x).
\tag{3}
\]
The capped backward map is
\[
\mathcal D_{\ell,R}(x,q)
=\frac{a^{\ell-4}}r SQ\,
 D_{a,e,R}(a^{\ell-1}Q^{-1}Sx,\,
                 a^{3-\ell}rQ^{-1}S^{-1}q),           \tag{4}
\]
where the original scalar capped gate is
\(D_{a,e,R}(z,q)=aq+e(1+z^2)^{-1}\tau_R(q)\).
All scalar functions in (3)--(4) act on the two sample coordinates.
The caps satisfy \(|\tau_R(q)|\le|q|\), \(|\tau_R'|\le1\).

Use the Euclidean sample norm and its operator norm. The identities
\(\|Q\|=1/\sqrt2\), \(\|Q^{-1}\|=\sqrt2\), the bounds
\(\|S\|\le1\), \(\|S^{-1}\|\le\sqrt{2/\delta}\), and
\(1/2\le a\le1\) give the following simultaneous bounds with
\(\varepsilon=64e/\sqrt\delta\):
\[
|\mathcal R_\ell(x)|\le\varepsilon,\qquad
\|D\mathcal H_\ell(x)-I\|\le\varepsilon,
\]
\[
|\mathcal D_{\ell,R}(x,q)-q|\le\varepsilon|q|,\quad
\|\partial_q\mathcal D_{\ell,R}-I\|\le\varepsilon,\quad
\|\partial_x\mathcal D_{\ell,R}\|\le\varepsilon|q|.
\tag{5}
\]
These estimates are uniform in the cap.

For detail, the first bound is at most
\(e a^{-\ell}(\pi/\sqrt2)\|S^{-1}\|\).
The two gate-derivative deviations have norm at most
\((e/a)\|S\|\|S^{-1}\|\).
Writing \(g(z)=(1+z^2)^{-1}\), the last derivative has prefactor
\(e a^{2\ell-5}/r\) times
\(SQ\operatorname{diag}(g'(z)\tau_R(q_{\rm raw}))Q^{-1}S\).
Since \(|g'|\le1\) and
\(|q_{\rm raw}|\le\sqrt2 a^{3-\ell}r\|S^{-1}\||q|\),
its norm is at most
\(\sqrt2 e a^{\ell-2}\|S\|^2\|S^{-1}\||q|\).
Each displayed elementary bound is below (5). There is no lost
inverse r in addition to the one condition-number factor.

These are coordinate identities and the global-delta gate bound. For an intrinsic dataset scale M, e/sqrt(delta) is not replaced by e M^4: inactive variance need not be controlled by M. The direct raw moment proof F.3 supplies the needed bound.

## G. Two-sample odd perturbations at every fixed finite depth

Each depth is fixed before width tends to infinity. The quantitative coefficient can depend on depth and separation. The depth-three row of the general ledger is subsumed by E.1; the new depth conclusions start at four. The complete general ledger is retained to make its induction and constants checkable. The action constant two follows from A.3.

For the all-depth balances and motion arguments, replace the terminal index four in G.5–G.6 by L. Every displayed adjacent-balance identity is indexed by one neighboring pair; the same differentiation applies to each j=2,...,L. The forward norm-ratio induction and reverse norm-ratio induction each traverse these pairs once. With initialized action norms at most two, each adjacent quadratic-form difference has norm at most four, so the total loss at an interior ratio is at most 4(L-2). Thus every raw gradient block has squared norm at least (c^2-4(L-2))_+^L. This gives G.2's all-block inequality; the full four-layer derivation and general indexing are included in G.5.

The motion proof G.6 also extends literally: positive definiteness starts at the top two-sample Gram, descends through each complete transpose identity, and gives positive hidden block norms. The adjunction identity sums those block norms up to the current layer. Exchange symmetry equates the two sample acceleration norms at each layer. This proves every sample/layer claim for arbitrary fixed L, while the depth-dependent numerical construction is supplied independently by G.1–G.3. Observation-query induction adds one action at each layer, exactly as in III.V; it does not require an Lp operator bound.

### G.1. Odd perturbations at every separately fixed finite depth

Within this proof unit, unqualified section and equation numbers are local.

#### 1. The result and explicit constants

Let L count hidden layers. Define
\[
p_3=\frac{31}{8},\qquad p_4=\frac92,\qquad p_5=\frac{21}{4},
\qquad p_L=9-\frac{43}{2(L+1)}\quad(L\ge6),\qquad
E_L=2(L+1)p_L.                                           \tag{1}
\]
In particular E3=31, E4=45, E5=63, E6=83.

Here is an explicit numerical prefactor for every fixed L. Put
\[
b_L=2^{L-1}\sqrt{(L-1)!},\qquad
D_L=3\,2^{2L-2}\sqrt{2(L-1)!},\qquad
\eta_L={4\,4^{L-1}e^{-1}\over27\pi(4^{L-1}+1)^4}.        \tag{2}
\]
Retain the exact reference constants
\[
C_0=1296000e^{1404},\quad C_z=1500C_0,\quad C_g=14400C_0,
\quad H=10^{30}(1+C_0+C_z+C_g+e^{1410})^4.                \tag{3}
\]
For L>=7 let
\[
\rho_L={1\over100(L+1)},\qquad B_L=4\sqrt{L(L-1)},
\]
\[
\mathcal C_L=e^{1/200}b_L\left[
 \sqrt L\,\operatorname{arsinh}(B_L)
 +{L\over2}\log(1+B_L^2)+{\rho_L\pi L\over2}\right]+2L,
\]
\[
H_L=\max\left\{H,10^{100}(8L)^L,{4\over\eta_L},
 \exp\big(\mathcal C_L+1000L^2\log(10L)\big)\right\}.
                                                               \tag{4}
\]
For 3<=L<=6 set H_L=H. These values also exceed the elementary
source and regression constants required below. Define
\[
                 c_L=H_L^{-100}D_L^{-2p_L}.              \tag{5}
\]
All constants in (1)--(5) depend only on L; c_L<1/4.

**Theorem.** For every fixed integer L>=3, every 0<delta<=1, every
fixed pair of deterministic inputs and binary labels satisfying
\[
\|x_i\|^2=d,\qquad |x_1^Tx_2/d|\le1-\delta,
\qquad y_i\in\{-1,1\},                                 \tag{6}
\]
every activation
\[
\phi_{a,e}(z)=az+e\arctan z,\qquad
\frac12\le a\le1,\qquad 0<e\le c_L\delta^{p_L}          \tag{7}
\]
has the full population/GF/raw-GD conclusions stated in Section 2.
For the stated convex mixture set a=1-theta and e=theta.

Moreover, the **same reference** c_poly suffices in place of c_L for every
3<=L<=6. Here c_poly is exactly
\[
\min\{1/4,c_*,10^{-70}H^{-400}\},
\]
with c_* and H defined at the beginning of Fragment E.
Only its displayed upper bound is used here. Consequently:

| Hidden depth | Sufficient bound with the unchanged reference prefactor |
|---|---|
| 3 | 0<theta<=c_poly delta^(31/8) |
| 4 | 0<theta<=c_poly delta^(9/2) |
| 5 | 0<theta<=c_poly delta^(21/4) |
| 6 | 0<theta<=c_poly delta^(83/14) |

In particular **one choice theta<=c_poly delta^10 works at all four
depths 3,4,5,6**. This statement does not extend that same numerical
prefactor to all larger depths. For every fixed finite L, the common
exponent nine is sufficient with the explicit depth-dependent c_L,
because p_L<9 and delta^9<=delta^{p_L}. The stronger powers in (1)
are sufficient bounds, not a claim of optimality.

#### 2. Exact model and complete conclusions

Write \(\rho=x_1^Tx_2/d\) and \(\Gamma_{ij}=x_i^Tx_j/d\).
At width n, initialize independently
\[
W^1_{ij}\sim N(0,1/d),\quad W^\ell_{ij}\sim N(0,1/n)
\ (2\le\ell\le L),\quad C_i\sim N(0,n^{-2}).
\]
With \(\frac{( u)^\top(v)}{n}=u^Tv/n\), use
\[
z_i^1=W^1x_i,\quad h_i^\ell=\phi(z_i^\ell),\quad
z_i^\ell=W^\ell h_i^{\ell-1},\quad
f_i=\frac{( C)^\top(h_i^L)}{n},
\]
\[
b_i^L=C\phi'(z_i^L),\qquad
b_i^\ell=\phi'(z_i^\ell)(W^{\ell+1})^Tb_i^{\ell+1}.
\]
The loss is \(\mathcal L=\frac12\sum_i(f_i-y_i)^2\), and the raw
metric is
\[
\|d\Theta\|_{\rm raw}^2={d\over n}\|dW^1\|_F^2
 +\sum_{\ell=2}^L\|dW^\ell\|_F^2+\frac{\|dC\|_2^2}{n}.
\]
Thus, writing r_i=f_i-y_i, the physical flow is exactly
\[
\dot W^1=-d^{-1}\sum_i r_i b_i^1x_i^T,\quad
\dot W^\ell=-n^{-1}\sum_i r_i b_i^\ell(h_i^{\ell-1})^T,
\quad \dot C=-\sum_i r_i h_i^L.                          \tag{8}
\]
GD is simultaneous raw Euler with step n^-2. Interpolate raw parameters
linearly, recompute hidden fields, and use right hidden derivatives at
nodes and left derivatives at a terminal endpoint. The finite random
readout is retained throughout.

The conclusions are the following, with all width limits taken for
each fixed dataset, fixed L and fixed finite physical horizon T:

1. One autonomous global strong C1 population flow exists on L separate
   canonical neuron L2 spaces, with L-1 bounded initialized adjacent
   actions, their genuine adjoints and HS learned increments. It is
   unique against bounded-primal strong competitors on those spaces,
   including nonsymmetric ones, and restarts uniquely from reached states.
2. GF and the prescribed raw GD converge along the full width sequence
   in probability. Predictions, loss, all L+1 raw kernels and the stated
   generated action probes converge uniformly in time. Same-layer joint
   field/velocity laws converge in Wasserstein-2 uniformly in time and
   jointly at fixed finite collections of times, including second moments
   and integrated squared speeds. The two-sample (z,h) path law in each
   layer converges in Wasserstein-2 for the uniform path norm. There is
   no across-layer neuron pairing or across-width operator-norm claim.
3. Every layer and sample obeys, at every finite physical time,
   \[
   \inf_{\alpha,\beta}\mathbb E[(
        \phi(z_i^\ell)-\alpha-\beta z_i^\ell)^2]
                         \ge e^2\eta_L/4>0.             \tag{9}
   \]
   For the convex mixture through L6, the reference constant
   \(\eta_*={4\cdot404e^{-1}\over27\pi405^4}\) from the
   L3 proof can replace eta_L. Every hidden raw block and every sample's
   layer preactivation and feature has nonzero initial acceleration;
   the projected total kernel changes to second order. Perpetual
   nonzero velocity is not asserted.
4. The loss satisfies
   \[
   \mathcal L(t)\le e^{-2a^{2L}\delta t}.                \tag{10}
   \]
   For the stated convex mixture and L<=6, this implies the reference
   weaker bound exp(-delta t/32).

The kernel terms are
\[
K^1_{ij}=\Gamma_{ij}\frac{( b_i^1)^\top(b_j^1)}{n},\qquad
K^\ell_{ij}=\frac{( b_i^\ell)^\top(b_j^\ell)}{n}
              \frac{( h_i^{\ell-1})^\top(h_j^{\ell-1})}{n},
\quad 2\le\ell\le L,
\quad K^{L+1}_{ij}=\frac{( h_i^L)^\top(h_j^L)}{n}.          \tag{11}
\]
No limit is uniform over the infinite physical time axis or over
growing depth; the population trajectory itself is global.

#### 3. Affine geometry, constants, and the intrinsic scale

Odd label folding preserves the exact finite raw loss. Reflection
exchanging the folded inputs and deterministic population contractions
give f_i=y_i g for the constructed limit, before uniqueness is invoked.
Feature time s uses the fixed-control field grad g, where
g=(1/2)sum_i y_i f_i. Let
\[
r=\sqrt{(1+y_1y_2\rho)/2},\quad \lambda=a^Lr,
\quad M=\left({3b_L\over2\lambda}\right)^{1/(L+1)}>1.    \tag{12}
\]
After dividing the first active projection by r and changing auxiliary
time to t=lambda s, the affine objective and exact raw equations are
\[
F=\langle D,A_L\cdots A_2p\rangle,
\quad p'=d_1,\quad A_j'=d_j\otimes x_{j-1},\quad D'=x_L,
\]
where x_1=p, x_j=A_jx_{j-1}, d_L=D and d_j=A_{j+1}^*d_{j+1}.

Fragment G.2 establishes canonical initialized action norm
at most two, using the stated Gaussian norm theorem with its hypotheses
checked. Adjacent Gram balances give
\[
\|p\|^2=1+c^2,\quad \|A_j\|^2\le c^2+4(L-j+1),
\quad(c^2)'=2F,\qquad c=\|D\|.
\]
The new all-radius bound follows by Cauchy in every gradient block:
\[
F'\ge F^2\left[{1\over c^2}+{1\over1+c^2}
                       +\sum_{k=1}^{L-1}{1\over4k+c^2}\right].
\]
Using F^2/c^2->1 at time zero and integrating with respect to c^2 yields
\[
F^2\ge c^2(1+c^2)\prod_{k=1}^{L-1}\left(1+{c^2\over4k}\right),
\quad F\ge c^{L+1}/b_L.                                \tag{13}
\]
Together with radial convexity c'>=1, this proves strong continuation
through the first affine hit g=3/2, with duration S and
\[
S\le2M^{L+1},\qquad M^{L+1}\le D_L\delta^{-1/2}.        \tag{14}
\]

The companion bounds the raw Hilbert Hessian using the actual separate
block norm bounds. For 3<=L<=6, on a radius-1/100 raw tube,
\[
\int\|\nabla^2F\|dt\le5100+L\log M.
\]
It checks all numerical forcing, probe and beta-family factors below
10^80 exp(5200)<H. At general fixed L the corresponding integral is
at most mathcal C_L+L log M on a tube of radius rho_L. Section 7 of
the companion gives explicit forcing and beta gaps, with every primitive
prefactor bounded by (4). In particular, uniformly in the backward cap,
\[
\|\Theta_e-\Theta_0\|_{\rm raw}\le H_L eM^{2L+2},\qquad
\|z_{e,i}^\ell-z_{0,i}^\ell\|_2\le H_L eM^{2L+\ell+1},
\quad |g_e(S)-3/2|\le H_L eM^{2L+1}.                   \tag{15}
\]
Original forward fields have bounded L2 norms H_L; incoming backward
fields have L2 norms at most H_L M^{L+1-ell}. These estimates are
proved before the coefficient-response argument.

The exact answer-probe normalization, including current direct terms
and both orientations, gives the following original-time exponents.
Set d0=L+1, t0=2L-1, and u_i=(2i-L-4)_+. Every local resolvent row
has bound H_L M^t0; local strict-transfer density has bound H_L M^u_i;
the local backward row at population i<L has exponent
b_i=4L-1-2i, and the top readout integration row has b_L=d0 in
this local notation. Adjacent beta gaps are at least
H_L^-1 M^{-(L-1)}. Every active strict transfer V_i, i<L, has lower
bound M^{-2(L+1)}h_j at source slot j. These are the precise premises
discharged for Fragment G.3, with H_L substituted for that
companion's generic prefactor H.

#### 4. Source tails recovered from the primal bounds

For every fixed finite depth the exact source program has 2(L-1)
coefficient families: forward strict arrays A2,...,AL and backward
causal arrays BL,...,B2, in that chronological order. Covariances use
full second moments; each coefficient is its actual formal source
derivative plus its learned moment. All current transpose returns are
retained. Fragment G.3 states the equations, including the
recursive current returns, on L distinct neuron spaces.

At the same deterministic coefficient arrays, a local population obeys
\[
Z=\xi+K\delta,\quad q=\zeta+B\phi(Z),\qquad
R=(I-a^2KB)^{-1},\ L_0=(I-a^2BK)^{-1},\ U=RK.
\]
Put h=arctan Z and d_gate=(1+Z^2)^{-1}tau_R(q). The combinations
\[
Z_G=R\xi+aU\zeta,\qquad q_G=L_0\zeta+aBR\xi
\]
are centered Gaussian, although Z and q need not be. The exact identities
\[
Z-Z_G=eU[d_{gate}+aBh],\qquad
q-q_G=e[aBUd_{gate}+L_0Bh]                              \tag{16}
\]
and the already proved primal L2 bounds show that Z_G has bounded
variance and q_G has L2 norm O(M^{L+1-i}), provided
eH_L^20 M^{5L-2}<=1. Gaussian moments then give the corresponding
sqrt(p) bounds. Applying (16) again in Lp and absorbing its small
q term proves
\[
\|Z_i\|_p\le H_L^{12}\sqrt p,\qquad
\|q_i\|_p\le H_L^{12}M^{L+1-i}\sqrt p.                 \tag{17}
\]
This argument needs no independence between the Gaussian and nonlinear
remainders and is uniform in cap and sufficiently fine fixed mesh.

Formal differentiation freezes all deterministic arrays, covariances
and named slots. The exact cancellation is
\[
J-J_0=U[\Delta V I_\zeta+P J],\qquad
\partial\delta-\partial\delta_0=L_0[\Delta V I_\zeta+P J],
\]
\[
P=N+a\Delta V B+aB\Delta G+\Delta V B\Delta G.           \tag{18}
\]
Here N contains e times an incoming field. Both other B-gate terms
are retained, including full random sample-sector mixing. In particular
the improved q moments cannot replace their deterministic B-row power.
The strict derivative envelope and weighted marginal moment bounds
give complete backward defects
\[
\|J_j\|_{row}\le H_L^{40}eM^{Q_j},\qquad
Q_j=8L-3-2j\ (2\le j<L),\quad Q_L=5L-1.                \tag{19}
\]
The independently bounded learned moments are included. The companion
also proves each forward strict-density defect, with its actual h_j.

#### 5. Controlling a chain of response terms without multiplying all bounds

Fix the inner beta reference. Positive affine coefficient recursion
gives A_{i+1}>=beta^2 V_i, where V_i=a^2R_iK_i. Hence
\[
R_{i+1}V_i\le(\beta^2a^2)^{-1}V_{i+1},\qquad
V_iL_{i+1}\le(\beta^2a^2)^{-1}V_{i+1}.                  \tag{20}
\]
Also R_i=I+V_iB_{i+1}. Expanding the rightmost factor of a product
and applying (20) repeatedly bounds a whole product by an identity
plus a sum of single strict transfers times backward rows. Thus the
row power for R_j...R_i and its reverse orientation is at most
\[
\min\{(j-i+1)t0,\ u_j+d0+b_i\}.                       \tag{21}
\]
The numerical chain factors, at most (8L)^L, are included in H_L.

For arbitrary nonnegative complete-row defects J_j, keep the forward
arrays at the inner reference and define backward excesses recursively:
\[
\Delta_L=J_L,\qquad
\Delta_i=J_i+a^2L_i\Delta_{i+1}R_i^*.                   \tag{22}
\]
This is an exact backward supersolution. Scale all J's by alpha in
[0,1] and impose simultaneously V_i^*<=2V_i and
\[
\|\Delta_i\|_{row}\le H_L^{-20}M^k,
\qquad k=\min(L-2,4).                                 \tag{23}
\]
Since A_{i+1}>=beta^2 V_i^*/2, (20)--(21) also hold for starred
products with finite factors at most 8 per step. Identities R*=I+V*B*
and L*=I+B*V* preserve the local row power t0 because
max_{i<L}(u_i+d0)+k<=t0. No small inverse assumption is used: all
strict-causal Volterra inverses at fixed mesh are finite polynomials.

The contribution of J_j to the bottom excess has exponent
\[
Q_j+2\min\{(j-2)t0,\ u_{j-1}+5L-4\}.                 \tag{24}
\]
For every forward loop V_i Delta_{i+1} V_i, both strict sides
compress by (20), preserving source-step densities. Its relative
bound, including the active lower density and beta slack, requires
only eH_L^60 M^{12L-5}<=1. Direct forward defects require less.
These inequalities strictly improve V_i^*<=2V_i and (23), so the
auxiliary homotopy closes.

For the actual coefficient homotopy, the outer box explicitly bounds
the positive transfer built from absolute active arrays by 2V_beta,out.
This is essential for the larger row radius (23). On this box the
source estimates apply. Chronological comparison with the inner
supersolution puts all actual coefficients, and their positive
transfers, strictly inside the outer box. The inactive sector has a
separate small backward box and explicit increasing forward margins;
Fragment G.3 constructs its finite triangular supersolution
without dividing by the inactive variance. First exit is impossible.

The exact arithmetic is:

| L | Maximum backward-excess power from (24) | k | Forward restriction | Sufficient E_L |
|---|---:|---:|---:|---:|
| 3 | 24 | 1 | 31 | 31 |
| 4 | 47 | 2 | 43 | 45 |
| 5 | 66 | 3 | 55 | 63 |
| 6 | 87 | 4 | 67 | 83 |
| L>=6 | 18L-21 | 4 | 12L-5 | 18L-25 |

For general L>=6 the j=5 term attains 18L-21; the companion bounds
every other term explicitly. Every value, derivative, learned-moment,
inactive-sector, beta-slack and supersolution restriction is implied by
\[
                        eH_L^{100}M^{E_L}\le1.         \tag{25}
\]
This proves the complete cap/mesh-uniform source construction.

#### 6. Closing the constants and the full population theorem

Equations (5), (7) and (14) give directly
\[
eH_L^{100}M^{E_L}
\le c_LH_L^{100}D_L^{E_L/(L+1)}=1.                     \tag{26}
\]
The unused powers in the preceding estimates make all required
inequalities strict. In particular (15) is below half the raw tube
radius, its endpoint discrepancy is below 1/4, and its preactivation
discrepancy is below sqrt(eta_L)/2. To check the last claim, (25)
gives H_L e M^{3L+1}<=H_L^-99, and H_L>=4/eta_L. The explicit
H also satisfies this requirement for L<=6. The displayed eta_* may be
used for convex gains through L6 by the stronger variance bound below.

For 3<=L<=6, D_L<=D_6<48000 and E_L/(L+1)<=83/7<12.
Since 48000^12<H, the reference coefficient satisfies
\[
c_{poly}H^{100}D_L^{E_L/(L+1)}
 \le10^{-70}H^{-299}<1.                                \tag{27}
\]
This proves the unchanged-prefactor assertions, with the smaller
exponents in the table, as well as the original power ten.

Fragment G.4 supplies the full fixed-L bridge, using the
actual generic Gaussian-conditioning theorem from the earlier proof.
It applies to the finite list of L-1 independent initial matrices,
each used in both orientations, and handles singular source laws by
finite-query regularization. Finite transpose identities on generated
spaces give genuine adjoints. Fixed-cap bounded derivatives and the
strict affine tube yield capped strong solutions and Euler limits.

The asymmetric backward comparison multiplies forward-state errors
by one factor (1+eR), independently of the number of backward steps.
With (17), its cap error is bounded by
C exp(C(1+eR)S-cR^2), tending to zero for each fixed L. States and
directions converge strongly to an autonomous uncut C1 feature path
through g(S)>5/4. The same estimate, retaining both physical residuals
and using tails only from the reference, proves uniqueness against
nonsymmetric bounded-primal competitors and restart from reached states.

At the first hit s_* of g=1, bounded g' makes
\(\int_0^s[2(1-g(u))]^{-1}du\) diverge. Its inverse gives the global
physical flow. Radial convexity and the initialized inequality
\(q_L\pm\chi_L\ge a^{2L}(1\pm\rho)\), where
\(q_L=\mathbb E[(h_1^L)^2]\) and
\(\chi_L=\mathbb E[h_1^Lh_2^L]\) at initialization, give (10).

Width is taken at fixed cap and finite auxiliary transcript; deterministic
stopped Euler comparison removes the mesh, then reference tails remove
the cap. The raw-GD consistency error is C_{L,R,T}n^-2. The finite
readout has RMS O_P(n^-1) and is retained until its zero population
limit. Appending L-1 clipped velocity queries in layer order and
removing their clips in the specified order gives the fixed-cap velocity
laws. The deterministic comparison uses a single reference-velocity
truncation factor; compactness of the uncut L2 time image removes it.
L2 products give (11), second moments and integrated speeds; fixed-grid
joint W2 convergence and the path interpolation inequality give the
same-layer path laws. No growing-transcript theorem is used.

Finally, positive Wick expansion of finite affine Euler programs and
inactive-field freezing give Gaussian affine marginal variance at least
a^{2(ell-1)}. The third-Hermite bound is eta_L, and the square root of
the arctangent regression residual is 1-Lipschitz in L2 coupling.
Equation (15) therefore gives (9). For a>=3/4 and ell<=6, the variance
is greater than 1/404, retaining the displayed eta_*.

The top initialization backward full second-moment Gram is positive
definite because phi' is positive and nonconstant. Each of the L-1
actual reused transpose formulas has a Gaussian term with the full
preceding backward second moment, plus its complete derivative response.
Conditional covariance propagates positivity down every layer. Its
positive contraction with the preceding forward Gram proves nonzero
acceleration of each hidden block. Adjunction and exchange then prove
both sample accelerations in every layer. With V the aggregate hidden
feature-time acceleration,
\[
\kappa(s)=\kappa(0)+2s^2\|V\|^2+o(s^2),\qquad
\kappa(t)=\kappa(0)+8t^2\|V\|^2+o(t^2),\quad\|V\|>0.
\]
This completes all parts of the theorem.

#### 7. Depth dependence and limits of the result

For L>=6, p_L increases to nine. Thus (5) proves an explicit
depth-dependent prefactor with a depth-independent sufficient exponent
nine. The prefactor is conservative: its logarithm satisfies
\[
\log(c_L^{-1})=O\!\left(2^L\sqrt{(L-1)!}\,L\log L
                              +L^2\log L\right).
\]
This is an upper bound on the size of the sufficient restriction, not
a necessary deterioration. It proves neither optimality of p_L nor
impossibility of much better depth dependence.

No common positive prefactor for all finite depths is established here.
The convex initialization asymptotic also rules out positive depth-uniform
absolute regression margins or an exponential loss bound beginning at time
zero for that family. Here is the complete argument. Fix \(0<\theta\le1\),
put \(\phi_\theta(z)=(1-\theta)z+\theta\arctan z\), \(q_0=1\), and
\(q_{k+1}=\mathbb E\phi_\theta(\sqrt{q_k}G)^2\) for standard Gaussian
\(G\). Fresh forward Gaussian conditioning gives this initialization
recursion. For \(z\ne0\), \(0<|\phi_\theta(z)|<|z|\), so \(q_k\)
decreases. Dominated convergence and the strict inequality imply its limit
is zero. Integrating \(t^4/(1+t^2)\) gives
\(|\arctan z-z+z^3/3|\le|z|^5/5\). Squaring the resulting expansion
and taking Gaussian moments yields
\[
 q_{k+1}=q_k-2\theta q_k^2+O_\theta(q_k^3),\qquad
 q_{k+1}^{-1}-q_k^{-1}\longrightarrow2\theta.
\]
Averaging the increments proves \(q_k\sim1/(2\theta k)\). Every absolute
activation regression residual is at most its second moment and therefore
vanishes with depth. At zero readout only the readout block of the
initialized two-sample kernel survives, so it is the feature Gram \(Q_L\).
Cauchy--Schwarz gives \(-\mathcal E'(0)=y^TQ_Ly\le4q_L\to0\) for
half-sum loss and binary labels, while \(\mathcal E(0)=1\). A fixed positive
exponential decay rate valid from time zero would contradict this derivative
bound. This does not exclude a common activation yielding qualitative
learning at each separately fixed finite depth; no such small-perturbation
prefactor is established here.

### G.2. Complete affine all-depth constants

Within this proof unit, unqualified section and equation numbers are local.

The initialized-action assertion is Lemma A.3.

#### 2. Balances and a new all-radius coercivity inequality

For L>=3 let r=sqrt((1+y1 y2 rho)/2), lambda=a^L r, and t=lambda s. Set x1=p, xj=A_j x_{j-1}, dL=D, dj=A_{j+1}^*d_{j+1}, and F=<D,xL>. The normalized raw equations are

p'=d1, A_j'=d_j tensor x_{j-1}, D'=xL.

The adjacent balances differentiated in the depth-four certificate now give

||p||^2=1+c^2, ||A_j||^2 <= c^2+4(L-j+1), (c^2)'=2F,

where c=||D||. Also c'>=1: D''=J_h J_h^* D makes c convex and its initial right derivative equals one.

Write

b_L=2^{L-1} sqrt((L-1)!),
Q_L(c)=sqrt(1+c^2) product_{k=1}^{L-1} sqrt(4k+c^2),
S_L(c)=1/(1+c^2)+sum_{k=1}^{L-1}1/(4k+c^2).

Cauchy gives F<=||p|| ||grad_p F||, F<=c||grad_D F||, and, for every matrix block, F<=||A_j||op ||grad_{A_j}F||HS. Hence, for c>0,

F' >= F^2 [c^{-2}+S_L(c)].

To integrate this without a spurious initial constant, use w=c^2. The equations and initialized forward norm one imply c(t)/t ->1 and F(t)/t ->1, so F^2/w ->1. Since d(F^2)/dw=F', integration from w=epsilon and then epsilon down to zero yields

F^2 >= c^2(1+c^2) product_{k=1}^{L-1}(1+c^2/(4k)),

c' = F/c >= Q_L(c)/b_L >= c^L/b_L,
F >= c^{L+1}/b_L.                                          (A)

The use of operator norms for matrix blocks is essential: no infinite-dimensional Hilbert--Schmidt norm of an initialized action is used.

The all-block Gram-ratio argument also gives, with K_L=4(L-2),

F'>=(L+1)(c^2-K_L)_+^L, F>=(c^2-K_L)_+^{(L+1)/2}.       (B)

Indeed each forward/backward adjacent norm ratio loses at most four, and every gradient block then has squared norm at least (c^2-K_L)_+^L. Differentiate F^2-(c^2-K_L)_+^{L+1} to obtain the second assertion.

Let T be the first time F=3/(2 lambda), and define

M=(3 b_L/(2 lambda))^{1/(L+1)}.

Then c<=M before T, and

T<=1+b_L/(L-1), S=T/lambda <= 2 M^{L+1},
r=(3 b_L/(2 a^L)) M^{-(L+1)},
M^{L+1} <= D_L delta^{-1/2}, D_L=3*2^{2L-2}sqrt(2(L-1)!). (C)

The harmless factor two in the S bound follows from 2(1+b_L/(L-1))/(3b_L)<2. For L5, b5<79 and D5<5400; for L6, b6<351 and D6<48000. These are strict elementary numerical bounds. Bounded primary norms and rank-one HS derivatives permit continuation to the target, exactly as in the depth-four certificate; (A) precludes an infinite branch below the target.

#### 3. Explicit integrated Hessian: unchanged H works at both depths

Use the Hilbert direct-sum raw norm, and stop nonlinear comparison at distance rho0=1/100. This norm is equivalent to the earlier sum norm by factors at most sqrt(7) at L5/L6, absorbed below. An inactive first-root variation has zero affine Hessian contribution, so the estimate covers the full nonsymmetric raw state.

Let the L hidden primary norm bounds be r_0=sqrt(1+c^2), r_k=sqrt(4k+c^2), k=1,...,L-1. On this tube replace them by r_k+rho0 and replace the readout norm by c+rho0. Put Qtilde=product(r_k+rho0), Stilde=sum(r_k+rho0)^{-2}. The Hessian has a readout--hidden star block and a hidden--hidden block. Their operator norms are bounded respectively by Qtilde sqrt(Stilde) and (c+rho0)Qtilde Stilde. This follows by bounding each off-diagonal block by the product of the complementary primary norms; for the hidden--hidden block use the rank-one positive matrix with entries (c+rho0)Qtilde/[(r_i+rho0)(r_j+rho0)], retaining its diagonal only for an upper bound. Therefore

||Hess F|| <= Qtilde [sqrt(Stilde)+(c+rho0)Stilde].

Since sum 1/r_k <= (L+1)/2,
Qtilde/Q_L <= exp(rho0(L+1)/2), Stilde<=S_L.

Combine this with (A). Through c=8, the integrated Hessian is at most

E_L := exp((L+1)/200)b_L [sqrt(L) asinh(8)
 + (1/2)log(65) + (1/2)sum_{k=1}^{L-1}log(1+16/k)
 + (pi/200)(1+(1/2)sum_{k=1}^{L-1}k^{-1/2})].             (D)

We used S_L<=L/(1+c^2), integrated c S_L exactly, and bounded integral_0^8 S_L by (pi/2)[1+(1/2)sum k^{-1/2}]. Direct elementary bounds give E_5<1100 and E_6<5070. To verify the latter without numerical quadrature, use b6<351, exp(7/200)<1.036, sqrt6<2.45, asinh8<2.777, half log65<2.088, and half[log17+log9+log(19/3)+log5+log(21/5)]<4.962, and the final pi-term <0.042. Their product is less than 5070. For L5 the same bounds, deleting the final term in each sum, and b5<79, sqrt5<2.237, exp(.03)<1.031 give less than 1100.

For c>=8, L<=6, (B) implies

dt/dc <= c^{-L}(1-16/c^2)^{-7/2} <= c^{-L}(1+208/c^2).

The last step uses the mean value theorem and (7/2)(4/3)^{9/2}<13 on 0<=16/c^2<=1/4. All primary norms are at most sqrt(c^2+20). The crude Hessian sum bound thus yields

||Hess F|| <= L(sqrt(c^2+20)+.01)^{L-1}
 <= L c^{L-1}(1+.1/c+100/c^2).

Indeed the logarithm of the last power ratio is at most 50/c^2+.05/c<.8 and exp(u)<=1+2u for 0<=u<=.8. Multiplying the previous two estimates and integrating the non-1/c terms from 8 to infinity gives less than

6[.1/8+154/64+20.8/(3*512)+5200/4096]<23.

Consequently, for every 3<=L<=6 and any terminal c<=N with N>=1,

integral ||Hess F|| dt <= 5100 + L log N.                 (E)

For a terminal c below eight, (D) already proves this. Original-time Hessians acquire lambda and ds=dt/lambda, so (E) is also the exact original-time raw Hessian integral. Thus G<=exp(5100)M^L before T, and G<=2^L exp(5100)M^L on an extension with c<=2M.

The common numerical H defined at the beginning of Fragment E obeys

H>=10^30 exp(5640).

All primitive prefactors below can be bounded by 10^80 exp(5200), which is less than H. In particular there is no new L5/L6 prefactor replacing H.

#### 4. Primal and enlarged-family estimates

For L5/L6, primary norms before the target are <=5M, and the extended/enlarged family below has primary norms <=20M. The integrated norm of any learned HS increment is <=10^8 M. To see this, before c=1 the derivative bound (20+c^2)^{L/2} and duration <=1 cost at most 21^3. Afterwards combine (A) with (sqrt(20+c^2))^L <= (c+sqrt20)^L to bound its time integral by b_L(1+sqrt20)^L M <10^8 M. The endpoint increments are smaller.

The same-state capped-versus-affine vector-field discrepancy is <=10^6 e(sqrt(20+c^2)+.01)^L. This follows by telescoping at most six forward gates and at most six backward gates, using |arctan|<=pi/2 and |tau_R(q)|<=|q|; each primary factor is at most the displayed bound and the sum of the resulting finitely many coefficients is below 10^6. Projection onto an RMS-unit input has raw norm <=1. Integrating this forcing, applying (E), and using lambda^{-1}<=M^{L+1} proves

E_raw <= H e M^{2L+2},                                  (F)
||Delta z^ell||_2+||Delta h^ell||_2 <= H e M^{2L+ell+1},
|g_e(S)-3/2| <= H e M^{2L+1}.

Here E_raw may be either the Hilbert or sum norm, after the fixed factor <=sqrt7. Require H e M^{3L+1}<=1/200 to close the tube and bound all actual forward fields. The last prediction bound retains the affine gradient factor lambda: lambda M^L E_raw has power 2L+1, while the direct gate discrepancy e M^L is smaller.

Original affine backward fields have norm <=C M^{L+1-ell}, and their capped nonlinear discrepancies are <=H e M^{3L+2-ell}. The learned coefficient errors therefore satisfy

|Delta M_Aell|_density <= H e M^{2L+ell},
|Delta M_Bell|_density <= H e M^{4L+3-2ell},
|Delta M_Bell|_row <= H e M^{5L+4-2ell}.                  (G)

The forward fields in their original normalization are bounded by constants independent of M: their active factors are a^{ell-1}r xell with r=C_L M^{-(L+1)}, and their inactive parts are frozen initial Gaussian products. The usual finite-Euler telescoping proof of inactive freezing uses bounded ordinary Frobenius norm of each learned product difference and conditional second moments; its finite number of terms is now at most six. This is also why no M^{ell-1} cost multiplies the learned forward moment error in (G).

For beta_j=1+j 10^{-14} M^{-(L-1)}, j=1,2,3, and beta_far=1+10^{-12}M^{-(L-1)}, use the exact homogeneity Theta_beta(t)=beta Theta_1(beta^{L-1}t). Because T<=72 and, on c<=2M, c'<=10^5 M^L, the base path exists for at least 10^{-5}M^{-(L-1)} beyond T without crossing c=2M. Every enlarged-time increment is below 10^{-8}M^{-(L-1)}, so these families exist on the same interval. Adjacent beta gaps and the far margin are at least 10^{-14}M^{-(L-1)}. Positive Wick-coefficient polynomials give

f'(beta)<=10^{14} M^{L-1} f(beta_far).

Fine-mesh limits preserve this estimate with a fixed factor. This factor, 2^L from (E), normalization factors a^{-O(L)}, and the at most six probe factors all fit the preceding 10^80 exp(5200) allowance. More explicitly, taking every primary bound as 100M gives every forcing/output probe bound <=7(100M)^5; their product times 64 exp(5100), even after 10^14 beta differentiation, sample-coordinate factors below 2^30, and a further 10^20 allowance for moment additions and norm conversions, is less than 10^80 exp(5200).

#### 5. Exact source powers

The source-coordinate normalization is

Q z^ell=a^{ell-1} S0 xell,
Q delta^ell=a^{L+1-ell} r S0^{-1} dell,
Ahat_ell=a^{L+2-2ell}r S0^{-1} Aell S0^{-1},
Bhat_ell=a^{2ell-L-2}r^{-1} S0 Bell S0,

where S0=diag(r,sqrt(1-r^2)). A strict density receives the extra time factor lambda. On the active coordinate, original forward strict densities therefore receive a^{2ell-2}r^2, and original backward row norms receive a^{L+2-2ell}r^{-1}. Inactive forward densities are bounded constants, and inactive backward coefficients vanish. Thus no inverse inactive variance is hidden.

An answer insertion at population ell has raw forcing cost M^{L-ell} for a forward answer and M^{ell-1} for a backward answer. Observing xell costs M^{ell-1}; observing dell costs M^{L-ell}. The independent fresh-Gaussian probe argument identifies the frozen-array derivative: reflection makes covariance and learned-moment first variations vanish; deterministic source signs give row norms; a single source gives the actual strict density. This is the reference argument with finitely many additional matrix calls, retaining the first preactivation and current readout cases.

With G<=H M^L the resulting table is

| Quantity | Original norm and bound |
|---|---|
| Aell and V_{ell-1}, 2<=ell<=L | strict density H M^{(2ell-L-6)_+} |
| Bell and W_ell, 2<=ell<=L | row H M^{4L+1-2ell} |
| every local R_ell,L_ell | row H M^{2L-1} |
| U_ell, 1<=ell<=L | strict density H M^{(2ell-L-4)_+} |
| backward Gaussian innovation at population ell<L | standard deviation H M^{L-ell} |
| every original forward Gaussian innovation | standard deviation H |

Beta differentiation adds at most L-1 to the listed exponent and retains numerical prefactor H by the explicit allowance above. The table does not multiply several different entries by H without accounting for the resulting power of H in a later argument.

In the active sector positivity also gives V_i >= a^{2i}r^2 I_s. Since r=3b_L/(2a^L) M^{-(L+1)} and i<=L-1, this implies the useful strict lower density

V_i >= M^{-2(L+1)} I_s.                                 (H)

This holds at each strict slot, independently of the smallest mesh step, and also for every enlarged initialization.

#### 6. Nonaffinity margin

The finite affine Euler polynomials have nonnegative coefficients in independent centered initialized Gaussian entries and contain their original initialized path polynomial. Every Wick expectation in the extra squared norm and cross terms is nonnegative. Fixed-mesh uniform integrability, fixed-program convergence of second moments, and strong Euler convergence therefore give ||xell||^2>=1. Inactive freezing and orthogonality yield Var z_i^ell >= a^{2(ell-1)}.

For the stated convex family e=theta, a=1-theta, theta<=1/4, all L<=6 have a^{2(ell-1)}>1/404. Thus the displayed eta_* nonaffinity margin survives the same forward discrepancy restriction as in the L3/L4 proofs. The compact-gain interval a in [1/2,1] instead has the explicit variance floor 1/1024 at L6; its third-Hermite margin can be substituted if that stronger compact-gain formulation is desired.

#### 7. A fully explicit general fixed-depth affine version

For arbitrary fixed L>=3, retain b_L, M, D_L in (A)--(C). Set rho_L=1/[100(L+1)], B_L=4sqrt(L(L-1)), and define

C_L=exp(1/200)b_L [sqrt(L)asinh(B_L)+(L/2)log(1+B_L^2)+rho_L*pi*L/2]+2L.

The exact argument behind (D) bounds the integral through B_L by the bracketed expression. For c>=B_L, K_L/c^2<=1/(4L). The derivative of (1-u)^{-(L+1)/2} is <=L there, giving dt/dc<=c^{-L}(1+4L(L-2)/c^2). Also

(sqrt(c^2+4(L-1))+rho_L)^{L-1}
<=c^{L-1}[1+2(L-1)rho_L/c+4(L-1)^2/c^2].

The exponent before this last linearization is below 1/4; the two integrable products beyond L/c contribute less than 2L. Hence

integral ||Hess F||dt <= C_L+L log M.

The following explicit accounting supplies every remaining numerical primitive constant. Write J=10L, and note the elementary inequalities

b_L <= (2sqrt(L))^{L-1} <= J^L,
1+b_L/(L-1) <= 2b_L <= J^L,
3b_L/(2a^L) <= J^{2L},
D_L <= J^{2L}, rho_L^{-1}=100(L+1) <= J^3.              (I)

On c<=M, every primary norm is at most 2sqrt(L)M. On c<=2M it is at most 3sqrt(L)M. The enlarged families constructed next have primary norms at most JM.

### 7a. Explicit beta family and derivative gap

Set

h=J^{-4L} M^{-(L-1)},
beta_j=1+j h/10, j=1,2,3,
beta_far=1+h.

On c<=2M we have c'<=Q_L(c)<=J^L M^L. Hence the base solution continues for at least J^{-L} M^{-(L-1)} beyond T before it can leave c<=2M. Bounded primary norms and HS derivatives justify this continuation independently of the target stopping rule. Because Lh<1/4,

(beta_far^{L-1}-1)T <= 2Lh J^L
 <= (1/2)J^{-L} M^{-(L-1)}.

Thus all these beta-scaled paths exist over the original interval. Their exact representation is Theta_beta(t)=beta Theta_1(beta^{L-1}t). Their raw propagators are bounded by 2^L exp(C_L) M^L. The adjacent gaps and far margin are at least h/10, so their reciprocals are at most

10J^{4L} M^{L-1} <= J^{5L} M^{L-1}.                     (J)

Consequently the nonnegative-beta-polynomial derivative argument supplies f'(beta)<=J^{5L}M^{L-1}f(beta_far), with an additional factor at most two on sufficiently fine meshes. There is no smallest-step dependence. Beta differentiation of the primitive source entries therefore adds power L-1 in M and a numerical factor at most 2J^{5L}.

### 7b. Explicit integrated forcing and primal factors

Let b(c)=sqrt(4(L-1)+c^2)+rho_L. At a raw state within rho_L of the reference, every primary norm is bounded by b(c). Telescoping the capped versus affine backward chains gives a discrepancy at layer ell bounded by

e L 2^L b(c)^{L+1-ell}.

Indeed each capped gate differs from multiplication by a by at most e in its operator bound, while each complete factor has bound a+e<=3/2. Telescoping the forward gates gives discrepancy at most 2e L b(c)^{ell-1}, because |arctan|<=pi/2 and the full matrix actions have norms at most b(c). The full forward norm is at most (2b(c))^ell. Products in a matrix gradient, and the endpoint gradients, therefore show that the sum of all raw vector-field discrepancies for the two samples is at most

F_L e b(c)^L, F_L=8(L+1)^2 4^L <= J^{2L}.              (K)

This deliberately overestimates the first projection factor, whose raw norm is at most one, and includes both sample contributions in the feature-time symmetric path. The estimate requires only a in [1/2,1], 0<=e<=1/2, and the cap property |tau_R(q)|<=|q|.

Before c=1 the elapsed time is at most one. Afterwards (A) gives dt/dc<=b_L c^{-L}. Since b(c)<=c+3sqrt(L),

integral_0^T b(c)^L dt
 <= (4sqrt(L))^L [1+b_L M]
 <= 2b_L(4sqrt(L))^L M <= J^{3L} M.                    (L)

Combining (K)--(L), lambda^{-1}<=M^{L+1}, the propagator exp(C_L)M^L, and conversion between Hilbert and sum norms, proves

E_raw <= exp(C_L)J^{6L} e M^{2L+2}.                    (M)

Taking the larger bound exp(C_L)J^{10L} also covers the enlarged family. Stop at E_raw=rho_L; the condition that the right side of (M) is at most rho_L/2 closes the stop. Each forward/backward field telescope costs at most J^{3L} beyond (M), giving numerical prefactor exp(C_L)J^{13L} for the powers already displayed in (F)--(G). The affine prediction telescope retains the factor lambda, exactly as in Section 4.

The original affine forward fields are bounded by

1+[3b_L/(2a^L)](2sqrt(L))^L <= J^{3L},

using inactive freezing and the original active factor r. Requiring the forward discrepancy to be at most one bounds the nonlinear fields by J^{4L}. The backward affine chain bound has numerical coefficient at most J^L. Forming the learned forward or backward moments, and then multiplying by S<=2M^{L+1} for a complete strict row, therefore yields all learned-moment bounds with a common numerical coefficient at most exp(C_L)J^{30L}. Their M powers are precisely (G).

### 7c. Explicit probe and normalization factors

With enlarged primary norms at most JM, any forcing or output probe cost has numerical coefficient at most J^{2L}; there are at most L chain summands, and L J^L<=J^{2L}. Pairing the two costs with the propagator 2^L exp(C_L)M^L costs at most exp(C_L)J^{5L}.

The original forward density scale contains r^2; its M-independent coefficient is at most [3b_L/(2a^L)]^2<=J^{4L}. The original backward row scale contains r^{-1}; its M-independent coefficient is 2a^L/(3b_L)<=1, and any remaining power of a costs at most 2^{2L}<=J^{2L}. Local resolvent similarities cancel exactly on the diagonal sample sectors. The inactive forward coefficient is bounded by L beta^{2L} and costs at most J^{2L}. Orthogonal sample-coordinate changes, direct identity terms, sums of the learned moment and derivative terms, and equivalence of the at most L+1 block norms together cost at most J^{3L}. Thus every source table entry before beta differentiation has numerical coefficient at most exp(C_L)J^{15L}. Adding the beta factor in (J) and the fixed factor two from sufficiently fine meshes gives at most exp(C_L)J^{21L}. This also covers the moment beta derivatives, because their finite affine Wick expansions are nonnegative and their undifferentiated bounds were already at most exp(C_L)J^{30L}; their differentiated coefficient is at most exp(C_L)J^{36L}.

No estimate in this bookkeeping multiplies two propagators. The same-state forcing, output telescopes, learned-moment comparison, source-probe estimate, and first beta derivative each contain the single propagator or a beta-polynomial derivative of a single bounded source entry. Later products of separate primitive bounds belong to the nonlinear source-closing argument and must be counted there.

### 7d. One explicit common prefactor

The preceding factors, the beta-gap reciprocal, rho_L^{-1}, original forward Gaussian bounds and backward Gaussian chain factors are all dominated by

H_L=exp(C_L+1000L^2 log(10L)).                            (N)

Indeed each displayed primitive product costs at most exp(C_L)J^{100L}, and 100L<=1000L^2 for every L>=3. This deliberately generous exponent also contains the explicit continuation and time-scale factors in (I)--(J). The preceding derivation, rather than an unspecified number of combinatorial factors, is the justification for (N).

Thus the arbitrary fixed-depth affine certificate has all powers (C), (F), (G), and the source table, with the single explicit prefactor (N). Its growth is log H_L=O(2^L sqrt((L-1)!) L log L). It does not itself prove a full all-depth activation amplitude: the source-closing powers of H_L and M are separate obligations.

Finally, the sharper numerical Section 3 calculation works for every 3<=L<=6, not merely L5/L6: the expression (D) increases with L, the displayed early integral is bounded by its L6 value, and all tail inequalities use only L<=6 and K_L<=16. The beta, forcing and probe estimates in Sections 4--5 use at most six layers. Therefore the unchanged original H may be used for all 3<=L<=6, while (N) is an explicit option for arbitrary fixed L.

### G.3. All-depth source response and compressed positive chains

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Affine interface

Write d=L+1, t=2L-1, u_i=(2i-L-4)_+, and M>1. Let H≥10^100(8L)^L dominate every numerical affine constant, every elementary source coefficient constant, the common beta-gap reciprocal, and the original-forward and initial source norms. Assume on three nested initialization references beta_in<beta_out<beta_far:

* duration S≤H M^d;
* beta gaps ≥H^-1 M^-(L-1);
* local affine resolvent rows R_i,L_i≤H M^t;
* local strict transfer densities V_i=a²R_iK_i≤H M^u_i;
* active lower bound V_i,kj≥H^-2 M^-2d h_j for i<L;
* backward coefficient B_(i+1) rows≤H M^b_i, b_i=4L-1-2i for i<L, while the top readout integrator has row≤HM^d;
* original affine forward fields have bounded second moments H, original delta_i norms≤H M^(L+1-i), and primitive backward Gaussian source zeta_i standard deviations≤H M^(L-i);
* capped nonlinear raw comparison E≤H eM^(2L+2), forward differences≤H eM^(2L+i+1), backward differences≤H eM^(3L+2-i).

Strict density means sup |T_kj|/h_j, causal row means sup sum_j |T_kj|. All bounds include the full two-sample matrix norm. The expected deterministic coefficients diagonalize in mean/contrast sectors; individual random gates are kept as full matrices.

The affine probe identities originate in the L4 affine certificate, Section 9. Fragment G.2 here supplies their explicit prefactors and the full interface for all fixed finite depths. In the assembled theorem substitute H_L for this proof unit's H.

#### 2. Exact source system and defect powers

For i=2,...,L, introduce forward source xi_i and backward source zeta_(i-1). Exactly as at depth four:

    Z1=Z1_0+H_P delta1,
    Zi=xi_i+A_i delta_i,
    qi=zeta_i+B_(i+1) H_i  (i<L),
    qL=EC, C=H_c H_L,
    H_i=phi(Zi), delta_i=D(Zi,qi).

A_i is strict and B_i causal. Gaussian covariances are the full second moments of the corresponding lower H and upper delta fields. Coefficients are beta² times expected named-slot formal derivatives, plus their learned second moments with the original h_j c_j normalization. The current B_L return is E N_L, and recursively current B_i is E N_i plus B_(i+1),kk E[Vgate_i G_i]. The exact construction order is A2,...,AL,BL,...,B2.

The number of independent initialized matrices is finite. Each initial matrix is conditioned in both orientations; its new query constrains that matrix alone. Thus the existing finite-program conditional projection proof applies literally after changing this finite number, without adding independence between repeated queries.

For any fixed coefficient arrays, let R=(I-a²KB)^-1, L=(I-a²BK)^-1, U=RK, V=a²U. With gate perturbations DeltaG,DeltaV and N=e diag(g'(Z)tau_R(q)), set

    P=N+a DeltaV B+a B DeltaG+DeltaV B DeltaG.

The exact identities are

    J-Jaff=U[DeltaV I_zeta+P J],
    Ddelta-Ddelta_aff=L[DeltaV I_zeta+P J],
    Jaff=R I_xi+aU I_zeta.

No expected derivative is replaced by a derivative of an already expected scalar. Current gates and the full random sample matrices remain in P.

The naive separate-source row estimate is avoidable. The independently proved primal comparison gives the *actual* norms ||Z_i||2≤H and ||q_i||2≤H M^m_i, where m_i=L+1-i (including m_L=1). Freeze the deterministic coefficient arrays and put

    Z_G=R xi+aU zeta,
    q_G=L zeta+aBR xi.

These are centered Gaussian vectors even though the two displayed Gaussian combinations may be correlated. The exact identities are

    Z-Z_G=eU[d+aB h],
    q-q_G=e[aBU d+LB h],
    h=atan(Z), d=g(Z)tau_R(q).

Use |h|≤pi/2, |d|≤|q|, and a²BU=L-I. The first remainder is bounded in L2 by H^6 e[M^(u_i+d+m_i)+M^(u_i+d+b_i)]. The second is bounded by H^6 e[M^(t+m_i)+M^(t+b_i)]. Here b_L=d and otherwise b_i=4L-1-2i. Since

    max_i(u_i+d+b_i)≤5L-2,
    max_i(t+b_i-m_i)≤5L-4,
    max_i(u_i+d+m_i)≤2L+1,

smallness e H^20 M^(5L-2)≤1 implies ||Z_G||2≤H^8 and ||q_G||2≤H^8 M^m_i. A centered Gaussian's p norm is at most its L2 norm times a fixed multiple of sqrt(p). Apply the same two exact identities in Lp. First absorb the q feedback e aBU d using eH^4M^t≤1/2, then use the q bound in the Z identity. This proves

    ||Z_i||p≤H^12 sqrt(p),
    ||q_i||p≤H^12 M^m_i sqrt(p), p≥2.

This reasoning uses the already established raw L2 comparison and deterministic coefficient bounds. It does not assume Gaussianity of Z or q, or any independence between the Gaussian and nonlinear remainders. It is cap and mesh uniform, and gives subGaussian marginal tails by the Gaussian moment criterion.

The strict derivative envelope must still retain the deterministic B-gate terms in P. Thus put w_i=max(m_i,b_i), so w_i=b_i at all populations for L≥3. The exponent of the moment restriction is max_i(u_i+d+w_i)=5L-2. Weighted Jensen and the marginal subGaussian q bounds control the random factor; the deterministic B factors contribute this same polynomial restriction. This is not a pathwise Gaussian maximum.

Consequently every forward defect A_(i+1) has strict density at most H^40 eM^f_(i+1), with

    f_(i+1)=max(2u_i+d+w_i, 2L+i+1), i=1,...,L-1.

Every backward defect J_j has complete causal row at most H^40 eM^Q_j, with

    Q_j=8L-3-2j, 2≤j<L;
    Q_L=5L-1.

These are the powers 2t+w_j. The derivative estimate explicitly bounds all of N J, DeltaV B J, B DeltaG J, and DeltaV B DeltaG J; only the N term uses the sharper q exponent m_i. No unproved cancellation of the other gate terms is invoked.

The learned-moment errors are smaller: forward density eM^(2L+j), backward density eM^(4L+3-2j), hence backward row eM^(5L+4-2j). Their prefactors fit H^40 after enlarging H to absorb fixed-depth sums. The assumed e bound also keeps the nonlinear original forward norms bounded, validating the raw L2 source bounds used above.

#### 3. The positive supersolution and elementary chain compression

Fix the beta_in affine coefficients A_i,B_i. Their active entries are nonnegative. Keep A_i*=A_i and recursively, from the top down, set

    B_L*=B_L+J_L,
    B_i*=B_i+[W_i(A_i,B_(i+1)*)-W_i(A_i,B_(i+1))]+J_i,
    W_i=a²B_(i+1)R_i.

All J_i are nonnegative absolute defect majorants. Put Delta_i=B_i*-B_i. At finite mesh all local inverses are finite Volterra polynomials; the construction exists continuously for every scaled defect alpha J, alpha∈[0,1]. There is no hidden denominator assumption.

The exact telescoping resolvent identity is

    Delta_i=J_i+a²L_i Delta_(i+1) R_i*.

Thus the contribution of J_j to Delta_i is a^(2(j-i)) L_i...L_(j-1) J_j R_(j-1)*...R_i*.

Affine positivity gives A_(i+1)≥beta² V_i. Therefore

    R_(i+1)V_i≤(beta²a²)^-1 V_(i+1),
    V_i L_(i+1)≤(beta²a²)^-1 V_(i+1).

If V_i*≤2V_i entrywise, the starred counterparts hold with factor2(beta²a²)^-1≤8. Consequently all strict chains compress, with an overall factor at most8^L.

A useful bound for a chain with no strict factor is obtained by expanding its rightmost resolvent. Since R_i=I+V_i B_(i+1),

    R_j...R_i = R_j...R_(i+1)
                 +R_j...R_(i+1)V_i B_(i+1).

Compress the strict product in the second term, and repeat. This yields

    R_j...R_i ≤ I+8^L sum_(k=i)^j V_j B_(k+1).

The analogous identity holds for L_i...L_j. For starred chains use V_j* and B_(k+1)*. If their local row/density powers are unchanged, this proves the row exponent

    r(i,j)=min((j-i+1)t, u_j+d+b_i).

The factors from sums and compression are bounded by H^4; when using the first, uncompressed alternative below it is needed only for chains of length at most two, costing at most H^4 as well.

#### 4. Wider box and noncircular bootstrap

The small-radius box used at L4 was sufficient but is not necessary. Define

    k=min(L-2,4),  r0=H^-20 M^k.

For the auxiliary J-amplitude homotopy impose both

    |Delta_i|_r≤r0,
    V_i*≤2V_i entrywise,  i<L.

Inside this box the original affine resolvent powers persist without a Neumann assumption. Indeed,

    R_i*=I+V_i* (B_(i+1)+Delta_(i+1)),
    L_i*=I+(B_(i+1)+Delta_(i+1)) V_i*.

Their baseline terms are at most twice R_i,L_i. The added row has size at most2H M^(u_i+d) r0. Since

    max_(i<L)(u_i+d)+k≤2L-1=t,

both rows remain bounded by H²M^t. The B_i* row powers also persist because k≤4<b_i. This validates every chain estimate in Section3 on the bootstrap box.

For Delta2, the J_j term has row exponent

    D_j=Q_j+2 min((j-2)t,u_(j-1)+5L-4).

All other Delta_i are bounded by the same maximum D=max_jD_j. Hence |Delta_i|_r≤H^60 eM^D.

For a forward loop V_i Delta_(i+1) V_i, both strict sides compress. On the starred right, first use V_i≤V_i*, then the starred compression, then V_(j-1)*≤2V_(j-1). Thus the J_j contribution has density at most

    H^50 e M^(d+2u_(j-1)+Q_j).

After division by the lower bound on V_i and reserving the beta gap, all forward conditions are implied by

    e H^60 M^(12L-5)≤1.

The maximum follows from 4L+2+2u_(j-1)+Q_j≤12L-5. Direct forward defects need at most power8L-1. In particular V_i Delta_(i+1) V_i≤eta V_i with eta≤1/4, and the finite positive Volterra series implies

    V_i*≤(1-eta)^-1 V_i≤(4/3)V_i.

If e H^82 M^(D-k)≤1, the backward rows improve to |Delta_i|_r≤r0/2. These strict improvements exclude a first exit of the auxiliary homotopy, establishing the supersolution.

For the actual nonlinear coefficient homotopy, include an analogous local-transfer constraint in the outer box: the positive Volterra transfer formed from absolute active arrays must be at most2V_i,beta_out. Besides |A_i|≤A_i,beta_out, require |B_i|≤B_i,beta_out+J_i^out with J_i^out nonnegative of row at most r0. These transfer constraints are continuous at fixed mesh. They imply the same row/density bounds via R=I+VB and L=I+BV, so Section2 applies at a first exit. The supersolution constructed at beta_in then dominates all absolute actual coefficients by chronological induction. It also bounds their positive absolute transfer by at most(4/3)V_i,beta_in, strictly inside2V_i,beta_out. The beta gaps give strict forward entrywise margins proportional to h_j, with no smallest-step requirement. Thus first exit is impossible.

The inactive sector uses a separate *small* backward box. Put Qmax=8L-7 and eta=H^40 eM^Qmax. Give every inactive backward coefficient the row radius r_in=H^10 eta. Give each inactive forward coefficient a fixed increasing strict-density margin (for instance2^i at level i) beyond its reference, absorbed in H. Since

    S H r_in≤H^52 eM^(9L-6)≪1,

all inactive local resolvent rows are≤2, and strict transfer densities are bounded by twice their fixed forward bounds. No active-sector lower bound or wide-transfer condition is used here.

Choose the inactive strict forward coefficients in advance as A_i*=A_i,0+c_i(1+S)eta I, where I_kj=h_j for j<k and c_i=H²(8L)^i. Then construct the backward coefficients by backward finite recursion. The affine inactive backward coefficients vanish. Starting from J_L, the equation B_i*=a²B_(i+1)*R_i*+J_i increases backward row bounds by at most a factor2 at each stage, hence they are≤2^L eta≤H eta. Every forward change is the sum of its direct defect, an inherited preceding forward change, and a term bounded by C S eta from the small reverse coefficients. The chosen increasing c_i dominate these finite inequalities. Induction therefore bounds all forward density increments by (8L)^L H²(1+S)eta≤H^4(1+S)eta. These are strictly below every fixed forward margin, while the reverse rows are strictly below r_in/2. The same estimates also validate the assumed resolvent bound, by first exit or the finite positive Volterra series. Here eH^100M^E≤1 implies the displayed smallness since E≥9L-6 for every depth listed below. This explicit small inactive box closes independently of the larger active backward radius.

#### 5. Exponent calculation

For L3:

    (Q2,Q3)=(17,14),
    chain powers=(0,5),
    (D2,D3)=(17,24),
    D=24, k=1, backward power23,
    forward power12L-5=31, hence E3=31.

For L4:

    (Q2,Q3,Q4)=(25,23,19),
    chain powers=(0,7,14),
    (D2,D3,D4)=(25,37,47),
    D=47, k=2, backward power45,
    forward power12L-5=43, hence E4=45.

For L5:

    (Q2,Q3,Q4,Q5)=(33,31,29,24),
    chain powers=(0,9,18,21),
    (D2,D3,D4,D5)=(33,49,65,66),
    D=66, k=3, E=63.

For L6:

    (Q2,Q3,Q4,Q5,Q6)=(41,39,37,35,29),
    chain powers=(0,11,22,26,26),
    (D2,D3,D4,D5,D6)=(41,61,81,87,81),
    D=87, k=4, E=83.

For every L≥6, D=18L-21. The j=5 term attains it. For j=2,3,4 the powers are8L-7,12L-11,16L-15. For j≥5 but j<L, compressed chains give

    D_j≤18L-11-2j+2(2j-L-6)_+≤18L-21.

At the top D_L≤17L-21≤18L-21. Hence

    E_L=18L-25, L≥6,
    E_3=31, E_4=45, E_5=63.

The forward supersolution power12L-5 is smaller at every L≥4; it determines E3. All source values, primal comparisons, gate moments including both B-gate terms, learned defects, forward beta slack and auxiliary homotopies are closed by the single convenient sufficient condition

    e H^100 M^E_L≤1.

If M≤A_L delta^(-1/[2(L+1)]), this becomes

    e≤H^-100 A_L^-E_L delta^p_L,
    p3=31/8, p4=9/2, p5=21/4,
    p_L=9-43/[2(L+1)] for L≥6.

In particular p6=83/14, and the common exponent9 works for every finite depth with this depth-dependent prefactor. This does not prove a depth-independent prefactor or a single fixed activation for all depths. The formula is the sharpest power justified by the displayed ledger, not an optimality claim.

Fragment G.1, Section 6, verifies the numerical inequality c_poly H^100 A_L^E_L<1 at L3 through L6, where A_L=D_L^(1/(L+1)); it is a separate constant calculation.

### G.4. Fixed-depth limits, moments and initial-motion induction

Within this proof unit, unqualified section and equation numbers are local.

#### A. The remaining population bridge is valid for every fixed finite L

Assume the quantitative affine/source construction supplies, on one compact feature interval [0,S], uniformly in the backward cap and fine fixed Euler meshes: a raw primal ball with strict slack; marginal subGaussian tails of the L incoming fields; an affine endpoint g0(S)=3/2 with discrepancy below 1/4; and preactivation discrepancy Ez below one half of an explicit Gaussian regression residual square root. Then every conclusion of Fragment G.6 extends by finite induction to L populations and L−1 adjacent Gaussian actions.

The finite Gaussian conditioning theorem actually concerns finitely many independent Gaussian matrices, not a fixed number three. A query constrains only its named matrix. Its common generated spaces therefore give L separate L2 spaces, bounded adjacent initialized actions, and their genuine adjoints. The raw learned increments are Hilbert–Schmidt. At a fixed cap the local gate satisfies |Dq|≤2 and |Dz|≤2eR, so bounded-action forward propagation and reverse induction make the raw field locally Lipschitz on the primal ball. The cap/mesh-uniform ball continues the capped strong solution through S.

For two capped or uncut states A,R on a common ball, the asymmetric gate estimate is

  ||D_A(Z_A,q_A)−D_R(Z_R,q_R)||2
  ≤2||q_A−q_R||2+2eR||Z_A−Z_R||2
      +2e|| |q_R|1_{|q_R|>R} ||2.

First bound all forward differences by C_{L,b} times the raw state difference. Induct backward from C through L gates. A reverse discrepancy is multiplied by a bounded action and the fixed gate bound 2; the R factor multiplies only the already bounded forward discrepancy. Consequently the raw direction difference is at most

  C_{L,b}(1+eR)||Theta_A−Theta_R||raw
    +C_{L,b}e sum_{i=1}^L || |q_{R,i}|1_{|q_{R,i}|>R} ||2.

There is one power of R, not R^L. Gaussian reference tails defeat exp(C_{L,b}RS). This gives strong cap removal, uniqueness against arbitrary bounded-primal strong competitors on the same spaces, including nonsymmetric physical competitors with their separate residuals, and restart from reached states.

Odd label folding and exchange equivariance imply f_i=y_i g for the constructed limit. The physical clock ds/dt=2(1−g) is global because g(0)=0 and g(S)>5/4, and the first-hit inverse clock diverges. This assertion does not require monotonicity of capped g.

At the uncut state, writing H=sum_i(y_i/2)h_i^L and g=<C,H>, the actual adjoint gives C'=H and C''=JJ*C. Radial convexity yields ||H||≥||H0|| and g'≥κ0=||H0||². Initialization gives κ0≥a^{2L}δ/2. Thus

  loss(t)≤exp(−2a^{2L}δt).

For convex a=1−theta≥3/4, L5 and L6 retain the reference weaker rate exp(−δt/32), since 2(3/4)^12>1/32. No depth-uniform positive rate follows for arbitrarily large L.

All finite-GF/raw-GD and observable bridges use a fixed finite number L of products and queries. Finite-cap width limits precede cap removal; the GD consistency error is C_{L,R,T} n^{-2}. The actual random finite readout is retained and has RMS O_P(n^{-1}). There are L+1 raw kernel terms. Velocity queries are appended in layer order, clipping each new phi'(Z)P query, removing earlier inner clips with the current outer clip fixed, and then removing that outer clip. The product-rule comparison has one velocity truncation factor M times the state discrepancy and a sum of L reference tails. A compact L2 time image gives uniform tail removal. Integrated speed bounds then give same-layer path W2 laws by the interpolation bound 4h∫|x'|². Every such assertion fixes L before sending width to infinity.

#### B. Explicit nonaffinity at every fixed depth

At a positive affine Euler mesh, every active forward coordinate is its initialized Gaussian path polynomial plus another polynomial with nonnegative coefficients. Every Gaussian monomial expectation is nonnegative. Thus E(||x_l(k)||_Euclidean^2/n)≥1. Fixed-program moment convergence is justified by uniform integrability: the finite polynomial degree gives a fixed polynomial bound in initialized operator and root norms, whose moments are uniformly bounded. Strong affine Euler convergence yields ||x_l(s)||²≥1.

Inactive fields freeze by telescoping the L−1 matrix factors; each learned correction has bounded ordinary Frobenius norm and has vanishing normalized action on the independent inactive Gaussian root. Hence every affine marginal is centered Gaussian with

  Var Z_i^l=a^{2(l−1)}[v||x_l||²+(1−v)]≥a^{2(l−1)}.

For all a≥1/2, let B_L=4^{L−1} and

  eta_L=4 B_L exp(−1)/(27 pi (B_L+1)^4).

The third-Hermite test proves inf_{alpha,beta}E[(atan(sigma G)−alpha−beta sigma G)²]≥eta_L whenever sigma²≥1/B_L. The integration-by-parts identity is

  E[atan(sigma G)(G³−3G)]
       =−2 sigma³ E[G²/(1+sigma²G²)²].

After u=sigma G substitution its absolute value is monotone in sigma. Restriction to |G|≤1 at sigma=B_L^{-1/2}, followed by division by E(H3²)=6, gives the displayed constant. Regression slopes belong to [0,1], so the square-root residual is 1-Lipschitz under L2 coupling. Therefore Ez≤sqrt(eta_L)/2 implies the activation regression error≥e²eta_L/4.

For requested convex gains a≥3/4 and L≤6, a^{2(L−1)}≥(3/4)^10>1/404. The displayed eta_* with B=404 is therefore retained without modification.

#### C. Initial motion induction is independent of the quantitative amplitude threshold

Every initialized feature pair has a positive definite Gram matrix, by Gaussian full support and phi'>0. Put H0=sum p_i h_i^L, beta_i^L=H0 phi'(Z_i^L), and descend beta_i^l=phi'(Z_i^l)A_{l+1,0}* beta_i^{l+1}. The top full second-moment matrix S_L=E beta^L(beta^L)^T is positive definite because phi'' is not identically zero. The actual reused-matrix conditioning identity at each downward step is

  A_{l+1,0}* beta_i^{l+1}=G_i^l+sum_j h_j^l T_ij,
  Cov G^l=S_{l+1},

where G^l is independent of the local initialized forward pair and T is the full expected formal derivative, with named slots and coefficients frozen. In particular the covariance is the full second moment, not a residual covariance. Conditional covariance then gives S_l≥a² lambda_min(S_{l+1})I>0.

Every hidden acceleration block has squared raw norm tr(S_l diag(p)F_{l−1}diag(p))>0. The forward-acceleration recurrence and adjunction give sum_i p_i<beta_i^l,U_i^l>=sum_{j≤l}||V_j||raw²>0; exchange makes both sample norms equal, so both are nonzero. Multiplication by phi'≥a gives nonzero feature acceleration. The total projected kernel satisfies κ(s)=κ0+2s²||V||raw²+o(s²), hence κ(t)=κ0+8t²||V||raw²+o(t²). All these are fixed-finite-L statements.

#### E. Further sharpening: recover Gaussian source scales from raw primal L2 bounds

The following Gaussian-part lemma is used in Fragment G.3, which gives its explicit prefactors and sufficient smallness condition.

Assume the proved cap-uniform raw comparison implies, at each actual coefficient list under consideration,

  ||Z_i||2≤C_L, ||q_i||2≤C_L M^{L+1−i}.

Write h=atan Z, d_gate=g(Z)tau_R(q), so |h|≤pi/2 and |d_gate|≤|q|. At those SAME deterministic arrays,

  Z=Z_G+e U[d_gate+aBh], Z_G=Rxi+aU zeta,
  q=q_G+e[a B U d_gate+L B h], q_G=L zeta+aBRxi.

Top zeta is zero and top B is the fixed readout integration kernel; the formulas remain valid. Z_G and q_G are centered Gaussian because their arrays are frozen and their named source groups are jointly centered Gaussian. This is an identity for their actual common law, not an independent-covariance substitution.

Use the primitive powers |U_i|density≤C_L M^{u_i}, |B_i|row≤C_L M^{b_i}, |R_i|row+|L_i|row≤C_L M^h, where b_i=4L−1−2i for i<L and b_L=L+1. With d=L+1, h=2L−1, u_i=max(0,2i−L−4), one checks

  d+u_i+b_i≤5L−2,
  h+b_i−(L+1−i)≤5L−2,
  d+u_i+(L+1−i)≤5L−2.

The L2 triangle inequality and e C_L M^{5L−2} sufficiently small therefore give

  ||Z_G||2≤C_L,
  ||q_G||2≤C_L M^{L+1−i}.

Gaussian moments give corresponding sqrt(p) bounds. In the exact q equation, the coefficient on ||q||p is e|aBU|row≤e C_L M^{5L−2}; absorb it. The bounded h term is covered by the same smallness and the displayed Gaussian q scale. Return to the exact Z equation. Thus for every finite p≥2,

  ||Z_i||p≤C_L sqrt(p),
  ||q_i||p≤C_L M^{L+1−i}sqrt(p).

The estimates concern deterministic suprema of marginal norms, not random time suprema. They immediately give cap/mesh-uniform marginal subGaussian tails with the much sharper primal q power. Their premises are already available from the raw affine tube comparison before any source response estimates; this avoids circularity.

The Gaussian-part sharpening only reduces the incoming-field contribution to the derivative defects. It does NOT remove the deterministic gate terms a DeltaV B+a B DeltaG+DeltaV B DeltaG from P. Their row bound costs e M^{b_i}; therefore the previously proposed exponent 5L−1−i alone was invalid. The corrected derivative-only row exponent is 2h+max(L+1−i,b_i), namely

  Q_i=8L−3−2i (2≤i<L), Q_L=5L−1.

The learned-moment row exponent 5L+4−2i is no larger at every layer for L≥3. Any still sharper derivative bound must control the deterministic B-gate terms separately, for example via an actually proved positive-affine gain derivative; it cannot simply replace their B power by the incoming-field moment power. The invalid exponent assignment is excluded to make the retained deterministic B-gate contribution explicit.

### G.5. Adjacent balances, norm ratios and source-probe derivation

Within this proof unit, unqualified section and equation numbers are local.

This supporting derivation uses the auxiliary four-layer scale M in (1) and the weaker initialized norm bound four, which follows from A.3. Its ratio and probe identities are used at general depth with the norm-two constants and scale explicitly recalculated in G.2. The two numerical scales are not identified.

Write
\[
v=(1+y_1y_2\rho)/2,\quad r=\sqrt v,\quad
\lambda=a^4r,\quad t=\lambda s,\quad
M=\left(\frac{3\sqrt5}{2\lambda}\right)^{1/5}.
\tag{1}
\]
\[
\|p_0\|=1,\quad \|A_{j,0}\|\le4\ (j=2,3,4),\quad
D_0=0,\quad \|A_{4,0}A_{3,0}A_{2,0}p_0\|=1.
\tag{3}
\]

#### 2. Exact equations and balances

After odd label folding, let p be the active first projection divided by
r, and let D be the signed readout. Put
\[
x_1=p,\quad x_j=A_jx_{j-1}\ (j=2,3,4),\qquad
d_4=D,\quad d_j=A_{j+1}^*d_{j+1}\ (j=1,2,3).
\]
The normalized affine objective is \(F=\langle D,x_4\rangle\), and
the original prediction is g=\lambda F. Its raw gradient equations are
exactly
\[
p'=d_1,\qquad A_j'=d_j\otimes x_{j-1}\ (j=2,3,4),
\qquad D'=x_4.
\tag{4}
\]
All primes in this proof unit denote t derivatives. The five component metrics
are L2, HS, HS, HS, L2. In particular normalizing the first projection
gives its exact raw metric, since its squared raw length is
\(\|dP_1\|^2/v=\|dp\|^2\).

Differentiating both sides, with no infinite-dimensional traces, proves
\[
A_4A_4^*-D\otimes D=A_{4,0}A_{4,0}^*,
\]
\[
A_jA_j^*-A_{j+1}^*A_{j+1}
=A_{j,0}A_{j,0}^*-A_{j+1,0}^*A_{j+1,0}
\quad(j=2,3),
\]
\[
A_2^*A_2-p\otimes p=A_{2,0}^*A_{2,0}-p_0\otimes p_0.
\tag{5}
\]
For example the derivative of A_jA_j^* is
\(d_j\otimes x_j+x_j\otimes d_j\). The derivative of
A_{j+1}^*A_{j+1} is the same expression, since
\(A_{j+1}^*d_{j+1}=d_j\). The endpoint computations give the other
two identities. If c=\|D\|, scalar differentiation gives
\[
\|p\|^2=1+c^2,\qquad (c^2)'=2F,
\tag{6}
\]
and successive use of (5) gives
\[
\|A_4\|^2\le16+c^2,\quad \|A_3\|^2\le32+c^2,
\quad \|A_2\|^2\le48+c^2.
\tag{7}
\]
Thus every primary norm is bounded by \(R=\sqrt{48+c^2}\).

There are two coercivity estimates, both needed below. The outer
balances imply
\[
\|d_3\|^2\ge c^4,\qquad
\|x_2\|^2\ge c^2(1+c^2).
\]
The A3 gradient alone therefore gives
\[
F'=\|\nabla F\|^2\ge c^6(1+c^2),\qquad
F^2\ge c^8/4+c^{10}/5,\qquad F\ge c^5/\sqrt5.
\tag{8}
\]
To verify the middle inequality without division at zero, differentiate
\(F^2-c^8/4-c^{10}/5\) and use (6); its derivative is nonnegative
and its initial value is zero.

A sharper large-c estimate uses *all* balances. If
\(q_j=\|x_j\|^2/\|x_{j-1}\|^2\), the first outer balance gives
q2\ge c^2. For j=2,3, (5) and the initial norm bound imply
\[
\|x_{j+1}\|^2
\ge \|A_j^*x_j\|^2-16\|x_j\|^2
\ge \frac{\|x_j\|^4}{\|x_{j-1}\|^2}-16\|x_j\|^2.
\]
Hence q_{j+1}\ge q_j-16. At c^2>32 these ratios are positive,
and
\[
\|x_j\|^2\ge(c^2-32)^j\quad(j=1,2,3,4).
\tag{9}
\]
The backward ratios obey the same calculation in reverse order:
\(\|d_3\|^2/\|d_4\|^2\ge c^2\), and each additional matrix
decreases the ratio by at most sixteen. Thus
\[
\|d_j\|^2\ge(c^2-32)^{5-j}\quad(j=1,2,3,4).
\tag{10}
\]
Each of the five gradient components in (4) has squared norm at least
\((c^2-32)^4\). Consequently
\[
F'\ge5(c^2-32)_+^4,\qquad
F^2\ge(c^2-32)_+^5.
\tag{11}
\]
The latter follows by differentiating
\(F^2-(c^2-32)_+^5\), including the region below the threshold.
No balance from depth three was assumed without differentiation.

#### 3. Target, duration, and integrated Hessian

Writing the hidden variables collectively as h, the chain rule gives
\(D''=J_hJ_h^*D\), where J_h is the derivative of x4. Thus
\(\|D\|\) is convex: differentiating
\(\sqrt{\|D\|^2+\epsilon^2}\) twice gives a nonnegative result,
and then let epsilon decrease to zero. Its initial right slope is one
by (3). Therefore
\[
c(t)\ge t,\quad c'(t)=F/c\ge1,\quad
c'(t)\ge c^4/\sqrt5\quad(t>0).
\tag{12}
\]
Let T be the first hit F=3/(2\lambda). By (8), c\le M before it.
The level c=1 is reached by time one unless the target was reached
earlier. Integration of (12) afterwards gives
\[
T\le1+\sqrt5/3<2,\quad S=T/\lambda\le2/\lambda<M^5,
\quad c(T)\le M,
\tag{13}
\]
\[
r=\frac{3\sqrt5}{2a^4}M^{-5},\quad
r^2\le2880M^{-10},\quad r^{-1}\le M^5,
\quad M\le76^{1/5}\delta^{-1/10}.
\tag{14}
\]
These estimates also prove existence through the target. Indeed, on a
branch below it the primary operator bounds are finite; the rank-one
HS derivatives and the endpoint derivatives are bounded. Their raw
increments have strong limits at any finite maximal endpoint, and
local existence for the polynomial field continues from that point.
An infinite branch below the target contradicts (12).

Set b=R+1. Every cross block of the Hessian of F has norm at most b^3
on the radius-one raw tube around the affine reference. In the sum norm
the full Hessian norm is at most 4b^3. First,
\[
b^3\le c^3+3c^2+75c+500.
\tag{15}
\]
For this, use
\((48+c^2)^{3/2}\le c^3+72c+48^{3/2}\), obtained from
\(\sqrt{u+v}\le\sqrt u+\sqrt v\) after differentiation in u;
then expand (R+1)^3. The constant term is less than 500.

Before c=1, b^3\le512 and the elapsed time is at most one. Between
one and any terminal c at most sixteen, (12) therefore gives
\[
\int b^3dt\le512+\sqrt5\{3+75/2+500/3+\log16\}<982.
\tag{16}
\]
For c\ge16, (11) gives
\[
\frac{dt}{dc}\le c^{-4}(1-32/c^2)^{-5/2}
\le c^{-4}(1+128/c^2).
\tag{17}
\]
The final inequality follows by the mean value theorem: the derivative
of (1-u)^(-5/2) is at most four for 0\le u\le1/8.
Multiplying (15) by (17), the integrable terms have total integral
from sixteen to infinity at most
\[
\frac3{16}+\frac{75}{2\cdot16^2}+\frac{500}{3\cdot16^3}
+\frac{128}{2\cdot16^2}+\frac{384}{3\cdot16^3}
+\frac{9600}{4\cdot16^4}+\frac{64000}{5\cdot16^5}<1.
\]
Only the term c^{-1} remains. Equations (16)--(17) imply, for the
whole interval and also for any extension with terminal readout c\le N,
\[
\int 4b^3dt\le4000+4\log N\qquad(N\ge1).
\tag{18}
\]
For terminal c\le16 the left side is less than3928, so this statement
also covers that case. In original time the Hessian is multiplied by
\lambda and ds=dt/\lambda. Therefore the same integrated estimate
holds for the original raw affine Hessian. The affine variational
propagator, and the affine part of the radius-one comparison, have bound
\[
G\le e^{4000}M^4.
\tag{19}
\]
The power four, rather than nine, uses the large-c ratio argument.

The learned HS increments are O(M). A convenient explicit verification
is \(\|A_j'\|_{HS}\le R^4\): before c=1 their integrated norm is
at most49^2; after c=1 integrate
\(\sqrt5(48+c^2)^2c^{-4}\). This is bounded by
\(\sqrt5(M+96+768)\), hence by 5000M. The endpoint raw increments
are at most3M and M. These estimates also justify raw strong extension.

#### 4. Cap-uniform primal and learned-moment comparison

Let E(s) be the sum of the original raw component distances from the
affine path. Stop at E=1. On this tube, the same bounded arctangent
and capped-gate expansion as in the depth-three proof gives
\[
\|V_{a,e,Rcap}(\Theta)-V_{a,0}(\Theta)\|_{sum}
\le500 e b^4,\qquad 0\le e\le1/2.
\tag{20}
\]
For completeness, write each capped backward step as
\(a q+e\tau_{Rcap}(q)/(1+z^2)\). Its excess over a q has norm
at most e\|q\|. The forward excess at each step has norm at most
e\pi/2. Recursing over at most four gates bounds each backward
product by (3/2)^4 times its affine primary product, and its gate
excess by 4(3/2)^3 e times that product. The three possible earlier
forward insertions in a matrix gradient have total coefficient at
most (\pi/2)(1+3/2+(3/2)^2)(3/2)^4. The sum of these bounds over
the five raw blocks is below 500 e b^4. Projection onto either
RMS-unit input has raw norm at most one. Thus (20) includes the
first block and uses no symmetry of the nearby state.

Subtract the affine fields after this same-state estimate. Equations
(18)--(20) give
\[
E(s)\le500 e e^{4000}M^4\lambda^{-1}\int_0^T b^4dt.
\]
Since b\le c+8, the interval before c=1 contributes at most4096.
Afterwards the expansion of (c+8)^4 and (12) give
\[
\int_0^T b^4dt
\le4096+\sqrt5\{M+32\log M+384+1024+4096/3\}
\le11000M.
\]
Consequently, with the deliberately ample common numerical H,
\[
E\le H eM^{10}.
\tag{21}
\]
The sharper unabsorbed prefactor is at most
\(5.5\cdot10^6e^{4000}\), since \(\lambda^{-1}\le M^5\).
The requirement H eM^10\le1/2 closes the tube and gives existence
through S for every cap.

Forward expansion on this tube yields, for 1\le\ell\le4,
\[
\|z^\ell_e-z^\ell_0\|_2+
\|h^\ell_e-h^\ell_0\|_2
\le H eM^{\ell+9}\le H eM^{13}.
\tag{22}
\]
One may retain the explicit prefactor from (21) while multiplying by
the finitely many powers of b\le8M and the at most four telescoping
terms; the result is still below H. For the prediction, retain the
exact affine coefficient \lambda:
\[
|g_e(S)-3/2|
\le \lambda b^4 E+10 e b^4\le H eM^9.
\tag{23}
\]
Here the first term uses the sum norm; no unnecessary factor five
is required because every partial derivative is at most \lambda b^4.

Every *original*, unnormalized affine forward field is bounded by an
absolute constant independent of M. In fact the active field at layer
\ell is a^{\ell-1}r x_\ell, and
\(\|x_\ell\|\le R^\ell\le7^\ell M^\ell\), whereas
\(r\le24\sqrt5 M^{-5}\). The inactive field is the frozen
initial Gaussian product with variance a^{2(\ell-1)}(1-v).
This freezing extends to A4A3A2 by telescoping the product difference:
at every fixed affine Euler prefix the learned product difference has
bounded ordinary Frobenius norm, and its normalized action on the
independent inactive Gaussian root tends to zero. Conditional second
moments also give orthogonality to the active fields. Thus (22), under
H eM^13\le1, bounds the actual nonlinear forward fields by another
absolute constant independent of M.

The original backward fields obey
\[
\|\delta^\ell_0\|_2\le C M^{5-\ell},\qquad
\|\delta^\ell_e-\delta^\ell_0\|_2
\le H eM^{14-\ell}\quad(1\le\ell\le4).
\tag{24}
\]
The second inequality telescopes the affine matrix/readout product,
whose derivative costs M^{4-\ell}, and uses (21); gate excesses are
smaller. It also bounds the nonlinear capped fields on the tube.
Consequently actual learned-moment coefficient errors, measured in
original strict density, satisfy
\[
|\Delta M_{A_\ell}|_d\le H eM^{\ell+8}
\quad(\ell=2,3,4),
\]
\[
|\Delta M_{B_\ell}|_d\le H eM^{19-2\ell}
\quad(\ell=2,3,4).
\tag{25}
\]
For example the largest backward moment compares two \delta^2
factors: their norms cost M^3, their difference costs eM^12, hence
the density error is eM^15. The complete original-time row error
costs at most the additional S\le M^5; thus its largest order is
H eM^20. These are bounds on learned moments themselves and do not
presuppose bounds on formal source-response coefficients.

#### 5. Absolute nonaffinity margin

Convexity gives \(\|x_4\|=\|D'\|\ge1\). If c^2\le1,
\(\|x_2\|^2\ge[(16+c^2)(32+c^2)]^{-1}\ge1/561\);
if c^2\ge1, the outer balance gives \|x2\|^2\ge2.
For x3, if c^2\le17 use
\(\|x_3\|^2\ge(16+c^2)^{-1}\ge1/33\).
If c^2\ge17, the forward-ratio inequality gives
\[
\|x_3\|^2\ge c^2(1+c^2)(c^2-16)\ge306.
\]
Thus all affine sample preactivations, which are centered Gaussian
by the affine finite source program and its strong Euler limit, satisfy
\[
\operatorname{Var}z_i^1\ge1,\quad
\operatorname{Var}z_i^2\ge1/2244,\quad
\operatorname{Var}z_i^3\ge1/528,\quad
\operatorname{Var}z_i^4\ge1/64.
\tag{26}
\]
The variance is
\(a^{2(\ell-1)}[v\|x_\ell\|^2+(1-v)]\), by the inactive
freezing and orthogonality just proved.

The Gaussian initialization in fact gives a stronger bound than (26),
which is useful for keeping the reference regression constant unchanged.
At every fixed normalized affine Euler mesh, each finite-width
coordinate of p and each A_j is a polynomial with nonnegative
coefficients in the independent centered Gaussian coordinates of
p0,A20,A30,A40. This follows inductively from (4), because the steps
and every 1/n normalization are positive. D0 is zero, and transposition
introduces no signs. Each forward coordinate x_ell equals its original
initialized path polynomial P0 plus a polynomial R with nonnegative
coefficients. Every monomial expectation in 2P0R+R^2 is zero or a
product of nonnegative even Gaussian moments. Therefore
\[
E\frac{\|x_{\ell,k}\|_2^2}{n}\ge E\frac{\|x_{\ell,0}\|_2^2}{n}=1.
\tag{26a}
\]
The final equality follows by conditioning through the independent
initial Gaussian layers. At fixed Euler mesh the norm recursions bound
every forward field by a fixed polynomial in the initial operator norms
and the initial RMS norm of p. Those initial norms have uniformly bounded
moments of every fixed order: the net argument (2) with a larger threshold
gives the operator tails, and the chi-square moment formula gives the
first-root bound. Thus these second moments are uniformly integrable.
Fixed-program convergence of second moments and
then strong affine Euler convergence give \(\|x_\ell(t)\|^2\ge1\).
Together with the frozen inactive variance this proves
\[
\operatorname{Var}z_i^\ell(t)\ge a^{2(\ell-1)}\ge1/64.
\tag{26b}
\]
This proof concerns expected polynomial coefficients, not positivity
of realized Gaussian matrix entries. In particular the exact reference
variance lower bound 1/404, and its reference eta_* from the quantitative
proof, are valid at depth four without modification. The explicit
balance-only margin (27) below remains an independent weaker option.

Put m_*^2=1/2244. The third-Hermite test from the quantitative proof
is self-contained and gives
\[
\mathcal R(\sigma G)
\ge\eta_4:=\frac{4\cdot2244e^{-1}}{27\pi\,2245^4}>0
\qquad(\sigma\ge m_*),
\tag{27}
\]
where \(\mathcal R(Z)=\inf_{\alpha,\beta}E[(\arctan Z-\alpha-\beta Z)^2]\).
Explicitly, integration by parts gives
\(E[\arctan(\sigma G)(G^3-3G)]
=-2\sigma^3E[G^2/(1+\sigma^2G^2)^2]\), whose absolute value is
increasing in sigma; restricting at sigma=m_* to |G|\le1 gives (27).
The optimal regression slope belongs to [0,1], so
z\mapsto arctan z minus that slope times z is 1-Lipschitz. Using
each regression minimizer as a competitor for the other variable proves
\[
|\sqrt{\mathcal R(Z)}-\sqrt{\mathcal R(Z_0)}|
\le\|Z-Z_0\|_2.
\]
Therefore H eM^13\le\sqrt{\eta_4}/2 preserves regression error at
least e^2\eta_4/4 for the nonlinear activation in every sample/layer
through the reference feature interval. This applies to the cap limit
once the separate strong cap-removal argument has been established.

#### 6. A common enlarged affine initialization family

The normalized gradient field is homogeneous of degree four. Hence
the reference started from all hidden parameters multiplied by beta
and zero readout is exactly
\[
\Theta_\beta(t)=\beta\Theta_1(\beta^3t).
\tag{28}
\]
Take
\[
\beta_j=1+\frac{j}{10^7(48+M^2)^{3/2}}\quad(j=1,2,3),
\qquad
\beta_{far}=1+\frac1{10^6(48+M^2)^{3/2}}.
\tag{29}
\]
The original path extends beyond T for at least 1/(2704M^3) while
c\le2M: on that region its derivative c'=F/c is at most
\(R^4\le(48+4M^2)^2\le2704M^4\). If c starts below M,
that bound precludes its reaching 2M sooner; bounded raw derivatives
give existence until this exit. For beta in (29),
\(\beta^3T-T\le8(\beta-1)<1/(2704M^3)\).
Thus every enlarged path exists on the same original interval.
Homogeneity carries variational propagators to the extended base
path, and (18) gives a bound \(16e^{4000}M^4\).
Primary norms and raw increment bounds remain C M.

Adjacent scale gaps and the remaining far margin are bounded below by
\[
\frac1{10^7\,49^{3/2}M^3}>\frac1{4\cdot10^9M^3}.
\tag{30}
\]
At every fixed chronological affine mesh, Wick expansion gives
nonnegative-coefficient beta polynomials for the active coefficient
entries. Therefore, for beta\le beta3,
\[
f'(\beta)\le
\frac{f(\beta_{far})}{\beta_{far}-\beta}
\le4\cdot10^9 M^3 f(\beta_{far}).
\tag{31}
\]
Fine-mesh Euler estimates retain these bounds with a fixed absolute
factor: local polynomial fields and their variational equations
converge on the just-established common compact interval. There is
no mesh-dependent beta gap and no smallest-step requirement.

#### 7. Exact source normalization and probe powers

Use the same sample matrix Q as the earlier source certificate and
\(S_0=\operatorname{diag}(r,\sqrt{1-r^2})\). For every hidden layer,
\[
Qz^\ell=a^{\ell-1}S_0x_\ell,\quad
Qh^\ell=a^\ell S_0\widehat h_\ell,\quad
Q\delta^\ell=a^{5-\ell}rS_0^{-1}d_\ell.
\tag{32}
\]
The full raw matrix updates then become
\(A_\ell'=\sum_{i=+,-}d_{\ell,i}\otimes\widehat h_{\ell-1,i}\),
because the product of their field factors is a^4r=\lambda.
The first-state and readout equations become x1'=d1 and
D'=\widehat h_{4,+}. This verifies normalization for the possibly
nonlinear program as well; it does not rescale the optimizer.

For source arrays, use script A and B to distinguish them from trained
matrix actions. Their exact transformations are
\[
\widehat{\mathsf A}_\ell
=a^{6-2\ell}rS_0^{-1}\mathsf A_\ell S_0^{-1},\qquad
\widehat{\mathsf B}_\ell
=a^{2\ell-6}r^{-1}S_0\mathsf B_\ell S_0.
\tag{33}
\]
In particular, on the active diagonal entry,
\[
\mathsf A_\ell=a^{2\ell-6}r\widehat{\mathsf A}_\ell,
\qquad
\mathsf B_\ell=a^{6-2\ell}r^{-1}\widehat{\mathsf B}_\ell.
\tag{34}
\]
The original strict density has one additional factor
\(\Delta t_j/h_j=\lambda\); hence forward densities obtain the
factor \(a^{2\ell-2}r^2\). Backward rows do not obtain this time
factor. The learned moments become exactly normalized time steps
times E[x_{\ell-1,k}x_{\ell-1,j}^T] or E[d_{\ell,k}d_{\ell,j}^T].

Here is the complete elementary probe cost rule for four populations:

| Injected answer at population ell | Raw-state forcing cost | Observed x_ell cost | Observed d_ell cost |
|---|---:|---:|---:|
| forward x_ell | C M^(4-ell) | C M^(ell-1), plus current identity | C M^(4-ell) |
| backward d_ell | C M^(ell-1) | C M^(ell-1) | C M^(4-ell), plus current identity |

For example a perturbation in x_ell enters precisely the later matrix
and readout updates, with complementary chain products of total degree
4-ell. A perturbation in d_ell enters precisely the first-state and
earlier matrix updates, with complementary products of degree ell-1.
The output costs are obtained by differentiating their chain products.
This explicitly includes inserting a forward coordinate answer at the
first preactivation and a backward answer at the top readout while
retaining the integrated state separately.

To turn these deterministic bounds into source coefficient bounds, use
the finite-program independent-Gaussian probe identity, as follows. Add epsilon times a fresh standard Gaussian root,
with arbitrary deterministic signs at a finite set of source slots,
to the indicated answer. Reflection of that root shows that covariance
and learned-moment parameters are even functions of epsilon. Their
first variation is zero, so the first answer variation is precisely
the formal derivative with those arrays frozen. Take the inner product
of the output with the fresh root. Taking signs of the deterministic
expected derivatives gives the row norm; a single insertion gives a
strict density, with its actual time step. The bounds above and (19)
supply the estimate before taking epsilon to zero. The current identity
terms are retained. This calculation uses only ordinary affine coordinate
instructions and the three independent initialized matrix actions; its
proof is unchanged by appending the third matrix call. It differentiates
neither a covariance square root nor a width limit.

Consequently the following are valid uniformly on the enlarged family,
including the derivative-only transfers associated with each coefficient:

| Source array | Normalized strict density (hence row) | Original-time norm needed |
|---|---:|---:|
| script A2, its forward transfer | H M^4 | strict density H |
| script A3, its forward transfer | H M^6 | strict density H |
| script A4, its forward transfer | H M^8 | strict density H |
| script B4, its backward transfer | H M^4 | row H M^9 |
| script B3, its backward transfer | H M^6 | row H M^11 |
| script B2, its backward transfer | H M^8 | row H M^13 |
| every local forward/backward source resolvent | row H M^7 | row H M^7 |
| top strict transfer x4 from d4 | strict density H M^10 | strict density H |

The normalized forward moments have powers M^2,M^4,M^6, and
the normalized backward moments have powers M^2,M^4,M^6 in top-to-bottom
order, smaller than the listed derivative powers. The local resolvent
power is 4+(ell-1)+(4-ell)=7. The top transfer power is 4+3+3=10.

All affine baseline arrays are sample diagonal. Therefore similarity
in (33) leaves their local resolvent row norms unchanged. The inactive
backward coefficients vanish. With normalized integration matrix I_t,
the inactive forward coefficients are exactly
\[
\widehat{\mathsf A}_{2,-}=2\beta^2I_t,\quad
\widehat{\mathsf A}_{3,-}=3\beta^4I_t,\quad
\widehat{\mathsf A}_{4,-}=4\beta^6I_t.
\]
Their original densities are bounded by absolute constants, since
the transform produces bounded powers of a, beta, and 1-v. Thus no
inverse inactive variance is hidden in the source table.

Every original forward Gaussian innovation has an absolute bounded
standard deviation. Its active factor is r times the corresponding
normalized earlier forward field, at most C r M^(ell-1), and the
inactive factor is bounded by freezing. The original backward Gaussian
innovations zeta1,zeta2,zeta3 have respective standard deviation bounds
\(C M^3,C M^2,C M\). There is no fresh top backward innovation.
The full incoming backward fields can be one power larger; they must
not be identified with these Gaussian sources.

For numerical accounting, initial/extended primary norms can be bounded
by 100M, a forcing or output probe cost by 5(100M)^3, and the propagator
by 16e^{4000}M^4. Multiplying the two largest costs, adding learned
moments, retaining direct terms, changing sample coordinates, and
converting density scales costs less than 10^20e^{4100}. The beta
derivative gap costs at most 4\cdot10^9M^3, still less than the
common numerical allowance 10^30e^{4200}. This is below
\[
H=10^{30}(1+C_0+C_z+C_g+e^{1410})^4
\ge10^{30}e^{5640}.
\tag{35}
\]
Thus H is a valid common prefactor for the primitive affine table,
primal estimates and their beta-differentiated versions with the
additional indicated M^3 power. Products of several such bounds in a
later nonlinear comparison can, of course, require powers of H.

#### 9. General fixed L and the precise depth dependence

For L\ge2 hidden layers, use the same definitions with
\(F=\langle D,A_L\cdots A_2p\rangle\), degree L+1, and
\(\lambda=a^Lr\). Differentiation proves all adjacent balances in
(5), now with j=2,...,L-1. The operator bounds are
\[
\|A_j\|^2\le16(L-j+1)+c^2,\quad \|p\|^2=1+c^2.
\]
Exactly the same forward/backward ratio argument gives, with
\(K_L=16(L-2)\),
\[
F'\ge(L+1)(c^2-K_L)_+^L,\qquad
F\ge(c^2-K_L)_+^{(L+1)/2}.
\tag{37}
\]
The radial inequality remains c'\ge1. One can choose
\[
M_L=\sqrt{K_L+(3/2)^{2/(L+1)}}\,\lambda^{-1/(L+1)},
\]
which bounds c at the target. Initial and late parts of the time
integral give T\le C_L. For sufficiently large c depending only on L,
\[
dt/dc\le c^{-L}(1+C_L/c^2).
\]
On the radius-one tube the Hessian has norm at most
\(L(\sqrt{16(L-1)+c^2}+1)^{L-1}\). Its product with dt/dc is
L/c plus an integrable O_L(c^-2) remainder. The earlier bounded
c interval is controlled by dt/dc\le1. Thus
\[
\int\|\nabla^2F\|dt\le C_L+L\log M_L,
\quad G\le e^{C_L}M_L^L.
\tag{38}
\]
This proves polynomial propagation for every fixed depth; it does not
leave an exponential in the long original time. The same integrated
forcing calculation gives
\[
E\le C_L eM_L^{2L+2},\qquad
\|\Delta z^\ell\|\le C_L eM_L^{2L+\ell+1}.
\tag{39}
\]
Homogeneity gives beta room of order M_L^{-(L-1)}. The elementary
probe exponents become
\[
|\mathsf A_\ell|_{d,s}\le
C_L M_L^{\max(0,2\ell-L-6)},\qquad
|\mathsf B_\ell|_{r,s}\le C_L M_L^{4L+1-2\ell},
\]
\[
|\text{local resolvent}|_r\le C_L M_L^{2L-1},\qquad
|\text{top strict transfer}|_{d,s}
\le C_L M_L^{\max(0,L-4)}.
\tag{40}
\]
For L4 the smaller M in (1), supplied by (8), and the explicit
4000 constant are preferable to the generic M_L construction.

Uniformity in arbitrary L is not supplied by this route: the early
curvature constant C_L, the primary and probe combinatorial constants,
the factors a^{-L}, the beta gap power L-1, and the source powers in
(40) all depend on L. This identifies a limitation of this certificate,
not impossibility of a depth-independent theorem or a counterexample
to exponent ten.


### G.6. Complete fixed-depth motion and observable proof

Within this proof unit, unqualified section and equation numbers are local.

Use the four-layer version of G.1, p_i=y_i/2 and the affine/source premises already verified in G.2–G.3. The proof below has one step per layer; the introduction to G gives its complete arbitrary-fixed-L indexing.

#### 5. Every initial hidden block and every sample-layer accelerates

This part only needs e>0, |rho|<1 and the constructed regular path.
At initialization every feature Gram is positive definite: a zero
linear combination of phi(U),phi(V) for a nondegenerate Gaussian pair
would hold at every real pair by full support and continuity, and
separate differentiation contradicts phi'>0. Induction through all
three fresh forward matrices proves this at all four hidden layers.

Put D_i^l=phi'(Z_i^l(0)), H_0=sum_i p_i h_i^4(0), and

    beta_i^4=H_0 D_i^4,
    beta_i^l=D_i^l A_{l+1,0}* beta_i^{l+1}, l=3,2,1,
    S_l=E_l[beta^l (beta^l)^T].

First S_4 is positive definite. A null vector u would give everywhere

 [p_1 phi(z_1)+p_2 phi(z_2)] [u_1 phi'(z_1)+u_2 phi'(z_2)]=0.

For fixed z_2 the first factor has at most one zero in z_1. Continuity
forces the second factor to vanish for every pair; differentiating in
z_1 and using phi'' not identically zero gives u_1=0, then u_2=0.

The three complete initialization transpose identities are, successively,

 A_{l+1,0}* beta_i^{l+1}
   =G_i^l+sum_j h_j^l(0) T^{l+1}_{ij},
 T^{l+1}_{ij}=E_{l+1}[partial_{xi_j^{l+1}} beta_i^{l+1}],
 Cov(G^l)=S_{l+1},  l=3,2,1.                          (5.1)

G^l is independent of the local initialized forward pair. Its covariance
is the full second moment S_{l+1}, not a residual covariance after
regression on forward features. Named Gaussian arguments, deterministic
response coefficients and covariance parameters are frozen in the formal
derivative. In particular at both middle populations the derivative
includes the actual h^{l+1}-dependence of the already present response
term. Products in this fixed finite initialization transcript can be
smoothly truncated first; Gaussian moments and bounded activation
derivatives justify their removal. The generic finite conditioning law
therefore proves (5.1) for the actual reused matrix, not a fresh surrogate.

Conditionally on the local forward pair,

 Cov(beta^l | Z^l)=diag(D^l) S_{l+1} diag(D^l)
                   >= a^2 lambda_min(S_{l+1}) I.

Induction proves S_3,S_2,S_1 positive definite. Define hidden raw blocks

 V^1=(1/d)sum_i p_i beta_i^1 x_i,
 V^l=sum_i p_i beta_i^l tensor h_i^{l-1}(0), l=2,3,4.

If F_{l-1} is the preceding feature Gram, then

 ||V^l||HS^2=tr(S_l diag(p) F_{l-1} diag(p))>0.

At the first layer the same identity uses the input Gram Gamma and the
raw factor d. Both matrices are positive definite, so every hidden raw
block is nonzero. No input covariance inverse is used.

The strong backward equations and bounded gates give

 C(s)=sH_0+o_L2(s),  b_i^l(s)=s beta_i^l+o_L2(s).

Thus the hidden state satisfies

 hidden_theta(s)=hidden_theta(0)+(s^2/2)V+o_raw(s^2).    (5.2)

Let U_i^l denote its corresponding preactivation acceleration. The
forward recurrence is

 U_i^1=sum_j Gamma_ij p_j beta_j^1,
 U_i^l=V^l h_i^{l-1}(0)+A_{l,0}(D_i^{l-1} U_i^{l-1}).

Adjunction and the beta recursion give, successively for every l,

 sum_i p_i <beta_i^l,U_i^l>_l
                   =sum_{j=1}^l ||V^j||raw^2 > 0.     (5.3)

Hence some sample accelerates in each layer. After label folding the
input reflection exchanges the samples and preserves the objective and
initial law; it therefore equates their squared acceleration norms.
In the original label sectors multiplying a field by y_i does not alter
its norm. Both sample accelerations are nonzero. Since D_i^l>=a, each
feature acceleration D_i^l U_i^l is nonzero too.

Writing V=J_0*H_0, equation (5.2) and the trajectory chain rule give

 H(s)=H_0+(s^2/2)J_0 V+o_L2(s^2),
 kappa_readout(s)=kappa_0+s^2||V||raw^2+o(s^2),
 kappa_total(s)=kappa_0+2s^2||V||raw^2+o(s^2).           (5.4)

The hidden projected kernels contribute the other s^2||V||^2 term.
Since s'(0)=2, physical hidden block and sample preactivation/feature
accelerations are respectively 4V,4U_i^l,4D_i^l U_i^l, and

 kappa_total(t)=kappa_0+8t^2||V||raw^2+o(t^2).

The readout has physical initial velocity 2H_0 and physical initial
acceleration -4 kappa_0 H_0, both nonzero. These are block and sample
statements, not claims that every scalar parameter coordinate moves or
that velocity stays nonzero at every later time.

#### 6. Finite GF, simultaneous raw GD, all five kernels and path laws

At any fixed cap and fixed physical mesh the Gaussian conditioning law
applies to a finite transcript with all three matrices and both actual
residuals. Exact rank-one unrolling bounds each current action by its
initialized norm plus the sum of products of the update-factor RMS
norms; adding the third matrix adds precisely one such finite sum.
A larger primal ball with slack contains the coarse finite references
with probability tending to one. On this ball the capped raw field is
bounded and Lipschitz with constants independent of width. Its Euler
local defect is at most KM h^2/2; stopped Gronwall removes the auxiliary
mesh and identifies fixed-cap finite GF.

The finite form of (3.2) compares genuine uncut GF to this same-width cap
reference. Send width to infinity at a fixed cap, transfer its reference
tail norms by the fixed-cap law, then send the cap to infinity. The
Gaussian tail defeats exp(K_T R), and the strict stopping margin excludes
exit. At any fixed width GF itself cannot have a finite-time raw-norm
blowup: the loss identity bounds integral ||dot theta||raw^2 by its
initial loss, and Cauchy--Schwarz bounds finite-time raw displacement.
Local smooth finite-dimensional existence then continues it.

For genuine raw GD the interpolant direction is the uncut field at the
preceding node. Comparing to the fixed-cap reference incurs an additional
K_{R,T} eta_n, uniformly in width, and eta_n=n^-2 tends to zero. This
uses the exact five raw blocks and does not replace the algorithm by a
scalar clock or a different metric. It also avoids invoking a Gaussian
conditioning theorem for a growing transcript. The initialized finite
readout remains iid N(0,n^-2); its normalized RMS is O_P(n^-1), so the
fixed-program stability limit is the zero population readout. These
arguments use the full width sequence in probability.

The five raw kernel contributions, including all off-diagonal entries,
are now

 K^1_ij=Gamma_ij <b_i^1,b_j^1>_1,
 K^l_ij=<b_i^l,b_j^l>_l <h_i^{l-1},h_j^{l-1}>_{l-1}, l=2,3,4,
 K^5_ij=<h_i^4,h_j^4>_4.

They, predictions and loss converge uniformly on each fixed [0,T] by
products of the converging L2 fields and the bounded-action comparisons.
Both initialized and trained orientations on their generated probes
are retained. No cross-width operator-norm convergence is asserted.

For completeness the extra velocity layer does not require an unproved
Lp bound for an initialized Gaussian action. At fixed cap, primary
source response rows obey the same nonlinear independent-Gaussian probe
bound Kh_j for past slots and K for current slots. This follows from
capped raw Lipschitz stability with an inserted Gaussian answer, followed
by Gaussian integration by parts with all contractions frozen. The
all-index derivative seminorm R(F)=sum_eta |partial_eta F| obeys the
four-layer causal inequalities

 R(Z^l_k) <= 1+K sum_{j<k}h_j R(delta^l_j),
 R(C_k) <= K sum_{j<k}h_j R(H^4_j),
 R(q^l_k) <= 1+K R(H^l_k)+K sum_{j<k}h_j R(H^l_j),
 R(H^l_k) <= 2 R(Z^l_k),
 R(delta^l_k) <= 2eR R(Z^l_k)+2 R(q^l_k),

with the evident root adjustment at l=1 and q^4=C. Taking the maximum
of the forward seminorms and C, substituting the reverse inequalities,
and exchanging the two strict sums gives U_k<=K+K sum_{j<k}h_j U_j.
Discrete Gronwall gives a mesh-uniform pathwise bound on every primary
derivative row. The same inequalities with Lp norms give primary
moments K sqrt(p). Constants here may depend on the fixed cap and T.

Write P^l=dot Z^l and U^l=phi'(Z^l)P^l. The exact recursions are

 P^1=dot w x,
 P^l=dot A_l H^{l-1}+A_l U^{l-1}, l=2,3,4.

Append observations after the complete primary transcript, in the order
A_{2,0}U^1, A_{3,0}U^2, A_{4,0}U^3; add learned increments explicitly.
These queries do not feed back into training. At each layer the initial
action source is a Gaussian gamma^l with variance E|U^{l-1}|^2, with its
full cross moments with earlier forward queries, plus the actual formal
response-weighted reference reverse inputs. The new gamma^l is a separate named
forward argument, so its formal reverse-source derivatives vanish.

Inductively P^{l-1} has bounded Lp moments and its needed local reverse
source derivative row has finite expected absolute sum. Then

 partial_eta U^{l-1}
 =phi''(Z^{l-1})P^{l-1} partial_eta Z^{l-1}
                     +phi'(Z^{l-1}) partial_eta P^{l-1}

has bounded expected row sum by the primary pathwise bound. Thus the new
response row is bounded. Its scalar formula expresses P^l as a Gaussian
source plus a bounded deterministic row of primary delta fields and
rank-update terms whose scalar contractions are bounded. Hence P^l has
Lp norm K sqrt(p). Its local reverse-source derivatives are bounded by
the primary derivative row, because its response coefficients and named
new gamma^l are frozen. This closes the induction through the third
observational query. In particular node fourth moments are bounded at
each fixed cap uniformly in the auxiliary mesh.

To apply the original bounded-derivative conditioning theorem rigorously,
first use phi'(Z) tau_M(P) in each query. Its first derivatives are bounded
at fixed M. Remove the query clips in layer order using the bounded
initialized L2 actions, the just-derived derivative-row domination, and
Gaussian covariance square-root continuity. Expected source derivatives
converge by dominated convergence, including at singular source laws.
For a later query keep its outer clip fixed while removing earlier inner
clips, then remove that outer clip. This proves the asserted joint W2
laws for all three observations without assuming Lp boundedness of a
Gaussian operator or applying the theorem directly to unbounded products.

Finally the deterministic four-layer product-rule comparison is

 ||velocity_A-velocity_B||sum,2
 <= K[d_1+(1+M)d_0+sum_{l,i}||(|P^l_{B,i}|-M)_+||_2],  (6.1)

where d_0,d_1 are raw state and raw direction differences. At a gate
product split phi'(Z_A)P_A-phi'(Z_B)P_B into its bounded-gate difference
in P and a gate difference times P_B; truncate only that reference P_B.
Every layer adds one M d_0 term and propagates earlier errors through
bounded actions. It never multiplies two M factors.

The uncut population velocity is L2-continuous by the trajectory chain
rule and has compact L2 time image. Its positive-part L2 tails vanish
uniformly: that tail map is 1-Lipschitz, and a finite L2 net reduces the
claim to finitely many fixed variables. Apply (6.1) first to cap versus
uncut population paths, sending cap to infinity at fixed M and then M
to infinity. For finite paths take width first at fixed cap and M, then
the cap limit at fixed M, then the final M limit. This proves uniform-time
joint same-layer W2 velocity laws and joint W2 laws at any fixed finite
set of times, including second moments and integrated squared speeds.
No control of the growth of cap-dependent fourth-moment constants is
required. GD uses the actual recomputed hidden fields along the raw
interpolant, right derivatives at nodes and terminal-left derivatives.

For each layer the joint two-sample preactivation/feature path law lies
in W2(C([0,T];R^4)) with the supremum norm. To obtain it, use fixed-grid
joint W2 convergence and

 ||x-I_h x||_infinity^2 <= 4h integral_0^T |x'(t)|^2 dt.

Average this inequality over neurons and use the established integrated
speed bounds, then send the grid size to zero. This is a same-layer path
law, not an across-layer neuron coupling or a continuous-path velocity
law. Every convergence assertion fixes the dataset, finite depth four,
and finite physical horizon before sending width to infinity.


### G.7. Chronological source identities with all gate derivatives

Within this proof unit, unqualified section and equation numbers are local.

This unit supplies the literal four-layer source and differentiation identities. Its conservative four-layer estimates assume the complete interface and box displayed in its Sections 2–3. G.5 verifies that interface. The arbitrary-depth construction G.3 uses its own larger box and recalculated bounds; the exact cancellations here hold in either construction.

#### 1. Exact four-layer source system

Use two label-folded samples, controls c=(1/2,1/2), and a finite positive feature-time mesh (h_j), total length S. Write P=Gamma diag(c), H_P,kj=h_jP for j<k, H_c,kj=h_j c^T, and E=(1,1)^T. Four independent population spaces are used; there is no cross-layer coordinate pairing. At fixed cap define

    phi(z)=az+e atan(z), D(z,q)=aq+e g(z) tau_R(q), g(z)=(1+z²)^−1.

The source equations, with sample slots retained, are

    Z1_k=Z1_0+sum_{j<k}h_j P delta1_j,
    Z2_k=xi2_k+sum_{j<k}A2_kj delta2_j,
    Z3_k=xi3_k+sum_{j<k}A3_kj delta3_j,
    Z4_k=xi4_k+sum_{j<k}A4_kj delta4_j,
    Hℓ_k=phi(Zℓ_k),
    q1_k=zeta1_k+sum_{j≤k}B2_kj H1_j,
    q2_k=zeta2_k+sum_{j≤k}B3_kj H2_j,
    q3_k=zeta3_k+sum_{j≤k}B4_kj H3_j,
    C_k=sum_{j<k}h_j c^T H4_j,
    deltaℓ_k=D(Zℓ_k,qℓ_k) (ℓ=1,2,3),
    delta4_k=D(Z4_k,E C_k).

There are six mutually independent centered Gaussian source groups xi2,xi3,xi4,zeta1,zeta2,zeta3, also independent of the first root. Their full time/sample covariance rules are

    Cov(xiℓ_ki,xiℓ_vj)=E_{ℓ−1}[H^{ℓ−1}_ki H^{ℓ−1}_vj],
    Cov(zeta^{ℓ−1}_ki,zeta^{ℓ−1}_vj)=E_ℓ[deltaℓ_ki deltaℓ_vj], ℓ=2,3,4.

At Gaussian initialization scale beta, both displayed covariances and derivative-only response corrections receive the appropriate beta² initial-matrix factor. All learned moments retain their original raw h_j c_j normalization.

For ℓ=2,3,4 the six exact coefficients are

    Aℓ_ki,vj = beta² E_{ℓ−1}[∂_{zeta^{ℓ−1}_vj}H^{ℓ−1}_ki]
                 + h_v c_j E_{ℓ−1}[H^{ℓ−1}_ki H^{ℓ−1}_vj], v<k,
    Bℓ_ki,vj = beta² E_ℓ[∂_{xiℓ_vj}deltaℓ_ki]
                 + 1_{v<k} h_v c_j E_ℓ[deltaℓ_ki deltaℓ_vj], v≤k.

At actual initialization beta=1. In every formal derivative all arrays, Gaussian covariances, controls, and previous scalar contractions are frozen; named slots remain distinct even for singular source covariances. The original finite readout is unchanged and has zero population limit.

These equations follow by unrolling each of the three trained matrices into its independent initial matrix plus rank-one updates, and applying the finite conditioning rule to all three matrices in both orientations. The conditioning theorem in the cited L3 file is explicitly proved for finitely many independent Gaussian matrices; its conditional projection proof says that a query adds a linear constraint only to the matrix being queried. Thus the new third matrix is covered by that theorem's actual hypotheses, rather than an inference from the file's title.

Let Gℓ=∂_z phi(Zℓ), Vℓ=∂_qD(Zℓ,qℓ), and Nℓ=∂_zD(Zℓ,qℓ). For ℓ=4 use q4=EC. At beta=1 the exact current returns are

    (B4_kk)_ij=1_{i=j} E N4_ki,
    (B3_kk)_ij=1_{i=j} E N3_ki +(B4_kk)_ij E[V3_ki G3_kj],
    (B2_kk)_ij=1_{i=j} E N2_ki +(B3_kk)_ij E[V2_ki G2_kj].

There is no current C dependence on xi4_k, because C uses strictly earlier times. The other two identities include the current higher backward return. All past derivative paths and all learned moments remain present. The chronological construction order is A2_k,A3_k,A4_k,B4_k,B3_k,B2_k.

Exchange equivariance proves that every deterministic coefficient block is diagonal in mean/contrast sample coordinates: induct on this chronological order, interchange all sample-indexed Gaussian roots and named slots, and use invariance of Gaussian covariances, learned contractions, and expected formal derivatives. Individual random gates are full 2×2 matrices in this basis; the estimates below retain their full matrix norms. Physical competitors need not be symmetric.

#### 2. Affine interface actually needed

Let v=(1+y1 y2 rho)/2, r=sqrt(v), lambda=a^4r, and

    M=(3sqrt(5)/(2lambda))^(1/5)>1.

The required affine certificate, uniform on common enlarged beta paths and sufficiently fine fixed meshes, is

    S≤H M5, M≤76^(1/5) delta^−1/10,
    beta_in−1, beta_out−beta_in, beta_far−beta_out ≥H^−1 M^−3,
    active primary sizes ≤H M,
    affine variational propagator, including the radius-one tube, ≤H M9.

Here H is exactly the reference C_B, not a new free constant. Superscripts M5 etc. denote powers. The normalized homogeneous-degree-five affine proof must establish the H prefactors; the source proof does not infer them from unspecified constants.

For strict U write |U|d=max_{j<k}|U_kj|/h_j; for causal Q write |Q|r=max_k sum_{j≤k}|Q_kj|. The affine transfer certificate needed is

| Quantity | M power, prefactor H |
|---|---:|
| A2,V1 density, full sample norm | 0 |
| A3,V2 density | 1 |
| A4,V3 density | 3 |
| B2,W2 complete row | 18 |
| B3,W3 complete row | 16 |
| B4,W4 complete row | 14 |
| R_i,L_i complete rows, i=1,...,4 | 12 |
| U_i density, i=1,...,4 | 0,1,3,5 |

Definitions are K1=H_P, K_i=A_i for i≥2, local B_i^loc=B_{i+1} for i<4 and B4^loc=EH_c;

    R_i=(I−a²K_i B_i^loc)^−1,
    L_i=(I−a²B_i^loc K_i)^−1,
    U_i=R_i K_i, V_i=a²U_i,
    W_i=a²B_i^loc R_i (i=2,3,4).

The coefficient map is

    (A2,A3,A4,B4,B3,B2)
       =beta²(V1,V2,V3,W4,W3,W2)+learned_moments.

The active sharper forward density powers are −1,1,3, but the full sample bottom bound 0 is used everywhere below. The inactive affine backward coefficients vanish; inactive forward densities are bounded by H. Every active V_i entry is at least H^−2 M^−10 h_j, i=1,2,3.

The source standard deviations in the full sample norm are O(1) for Z1_0,xi2,xi3,xi4 and O(M3,M2,M1) for zeta1,zeta2,zeta3. This uses the special original-variable scaling: active affine forward fields are r times polynomials of degree at most four in primary variables, while r is proportional to M^−5; inactive fields remain fixed. It cannot be replaced by the generic bound H M^ℓ without losing the target ledger.

The independently supplied primal comparison is raw discrepancy ≤H eM15, forward discrepancy at layer ℓ ≤H eM^(ℓ+14), and learned backward density discrepancy ≤H² eM^(24−2ℓ), ℓ=2,3,4. Hence the largest learned backward row defect is H³ eM25. Learned forward defects are smaller. Under eM100 sufficiently small, actual forward-source standard deviations remain O(1).

#### 3. The precise coefficient box and local transfer persistence

Take active |A_i|≤A_i,beta_out entrywise, and |B_i|≤B_i,beta_out+J_i with nonnegative causal J_i and |J_i|r≤r0, where

    r0=H^−20 M^−9.

Inactive forward densities have fixed positive slack beyond their affine values; inactive backward rows are ≤r0. On this box all table bounds in Section 2 hreference with prefactor H². Indeed, for i=1,2,3,

    V_i*=V_i,b+V_i,b J_{i+1} V_i*,
    R_i*=R_i,b+V_i,b J_{i+1} R_i*,
    L_i*=L_i,b+L_i,b J_{i+1} V_i*.

The largest row norm of V_i,b is HM3 times S≤HM5, so every ratio is at most H^−18M^−1. The last identity, used after bounding V_i*, preserves the L_i power 12. Top transfers depend only on A4 and are dominated by positivity. Inactive ratios are O(Sr0). This proves persistence in the specified box, including arbitrary concentrated or current backward errors; it does not claim such errors have strict densities.


#### 4. Same-array source values and exact backward cancellation

For a local population write Z=xi+K delta, q=zeta+B H, H=phi(Z), delta=D(Z,q). Top zeta is zero. Solving the affine part at the actual coefficient arrays gives exactly

    Z=R xi +a U zeta +e U[d+aB h],
    h=atan(Z), d=g(Z)tau_R(q).

Since |h|≤pi/2 and |d|≤|q|, the table gives four inequalities

    Z_i,p ≤H^8 M12 sqrt(p)+ eH^8 M23 Z_i,p.

The exponent 23 is the largest (density U0 +duration5 +backward row18); the other self exponents are 22,22,15. Absorption gives

    ||Z_i,k||p≤H^9 M12 sqrt(p), all four i,
    ||q1_k||p≤H^12 M30 sqrt(p),
    ||q2_k||p≤H^12 M28 sqrt(p),
    ||q3_k||p≤H^12 M26 sqrt(p),
    ||C_k||p ≤H^12 M17 sqrt(p).

These are suprema of deterministic Lp norms over time, never a random time supremum. Power-series expansion gives corresponding subGaussian bounds with prefactor H13.

Freeze arrays/covariances and set J=∂Z, Ixi=∂xi, Izeta=∂zeta. Let

    G=aI+DeltaG, Vgate=aI+DeltaV,
    N=e diag(g'(Z)tau_R(q)),
    P=N+a DeltaV B+a B DeltaG+DeltaV B DeltaG.

Every random gate is kept as a full sample matrix. Exact subtraction of the same-array affine derivative yields

    J−Jaff=U[DeltaV Izeta+P J], Jaff=R Ixi+aU Izeta,
    ∂delta−∂delta_aff=L[DeltaV Izeta+P J].

The second identity follows from ∂delta−∂delta_aff=DeltaV Izeta+P J+a²B(J−Jaff) and L=I+a²BU. It uses no relation between different layers and therefore holds separately at both middle populations. It retains the current N_k J_k term.

Let (u,b,q) be the local powers of U density, B row, and incoming field. They are

    population 1: (0,18,30),
    population 2: (1,16,28),
    population 3: (3,14,26),
    population 4: (5,5,17).

Strict U gives the derivative envelope

    |single transpose J_kj|≤H³ M^u h_j E_k,
    |full forward derivative row J_k|r≤H³ M12 E_k,
    E_k=exp{eH^6 M^u sum_{r<k}h_r(Q_r+H²M^b)}.

The elementary product majorant proves this directly; all feedback through nonlocal B carries the preceding derivative. Weighted Jensen with weights h_r/S and the marginal subGaussian bound controls fixed moments through order eight under

    e H30 M35 ≤1.

The powers u+5+q are 35,34,34,27. In particular the bottom entry is 35, not 34. Deterministic powers u+5+b are 23,22,22,15. Holder gives E[Q_r E_r]≤H14 M^q, including any required source and terminal factors.

For a single transpose source, the expected feature derivative defect density has power 2u+5+q. For a complete forward-source backward output, the exact L identity has power 12+12+q. Thus, after also adding the independent learned moments, one may take

    forward A2 defect d2≤H40 eM35,
    forward A3 defect d3≤H40 eM35,
    forward A4 defect d4≤H40 eM37,
    backward B4 row defect q4≤H40 eM41,
    backward B3 row defect q3≤H40 eM50,
    backward B2 row defect q2≤H40 eM52.

All current diagonals are included. The numerical H40 is conservative: source value absorption costs H8, incoming moments H14, derivative base H3, transfer H2, duration H, and at most two finite sample/gain sums; their product is below H25. The remaining H15 covers learned moments, sums over four populations, and the fixed moment orders. There is no angle-dependent exponential in these prefactors.


## H. One three-sample odd large-gain activation at all finite depths

Unlike G, this theorem selects one activation a(z+arctan z) from separation alone and uses it at every separately fixed finite depth. The gain is large. The cubic Gram geometry overlaps the initialization results in special-data Section V; it is used here as a hypothesis discharged for a global dynamical theorem. The new contents are the gain-normalized primal/source estimates, complete global limit and all-depth motion. A.3 supplies the sharp initialized norm constants without an external concentration import.

### H.1. One odd large-gain activation for three samples at all fixed depths

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Model and statement

Let 0<delta<=1. Fix three inputs x_i in R^d with ||x_i||²=d,
Gamma_ij=x_i^T x_j/d, and |Gamma_ij|<=1-delta for i!=j. Labels y_i are
arbitrary elements of {-1,1}. Let L>=2 be any fixed finite hidden depth.
Use independent Gaussian initialization

    W^1_jk ~ N(0,1/d), W^ell_jk ~ N(0,1/n) (2<=ell<=L),
    C_j ~ N(0,n^-2).

The network is z_i^1=W^1 x_i, h_i^ell=phi(z_i^ell),
z_i^ell=W^ell h_i^(ell-1), f_i=(C^T h_i^L)/n, where (u^T v)/n=u^Tv/n.
The loss is E=||f-y||²/2. The raw metric is

    (d/n)||Delta W^1||_F² + sum_(ell=2)^L ||Delta W^ell||_F²
      + (||Delta C||_Euclidean^2/n).

Both GF and simultaneous raw GD with physical step n^-2 train every
block in this metric. GD interpolates raw parameters linearly and
recomputes hidden fields from those interpolated parameters.

Define the absolute constants and the activation

    eta0 = 1/(108*pi*exp(1)),
    lambda = eta0*delta²/3 = delta²/(324*pi*exp(1)),
    a_delta = 10^10/lambda = 324*pi*exp(1)*10^10*delta^-2,
    phi_delta(z) = a_delta*(z+atan z).                         (1)

The same a_delta and the same activation are used at all hidden layers,
and for every L>=2. In particular there is no small nonlinear-to-linear
coefficient ratio: the ratio is one.

**Theorem.** In the canonical population construction associated with
this finite Gaussian initialization, (1) has the following properties.

1. A global strong C^1 raw-Hilbert GF exists. It is unique among strong
   solutions with bounded primal quantities on compact intervals, without
   sample symmetry restrictions. Continuation from any reached state is
   unique in that class.
2. Its loss satisfies, for every t>=0,

       E(t) <= (3/2) exp[-lambda*a_delta^(2L)*t].             (2)

3. For every fixed finite dataset, L and physical horizon, finite GF and
   the stated raw GD converge along the full width sequence in probability
   to this same population flow. This includes predictions, loss, all L+1
   true raw kernel blocks, same-layer hidden paths in W2 with the uniform
   path norm, uniformly-in-time joint hidden-state/velocity laws in W2,
   joint laws at finitely many times, second moments, integrated squared
   speeds, and fixed finite generated probes using either orientation of
   the adjacent actions. The initialized actions have genuine adjoints;
   learned increments are Hilbert--Schmidt. No cross-width operator-norm
   convergence is asserted.
4. For every sample i and hidden layer ell,

       inf_(t>=0) inf_(alpha,beta in R)
       E[(phi_delta(z_i^ell(t))-alpha-beta*z_i^ell(t))²]
                    >= a_delta²*eta0/4 > 0.                 (3)

   Every hidden block and every sample's preactivation and feature field
   has a nonzero initial right second derivative. The initial hidden
   first derivatives are zero. For p=y/3 and the sum K of all raw kernel
   blocks,

       p^T K(t)p = p^T K(0)p + 18*t²*||V||_hidden²+o(t²),
       ||V||_hidden>0,                                      (4)

   with V defined in Fragment H.4.

This is global population existence and fitting together with finite-width
convergence on each compact time interval. It makes no simultaneous
infinite-width/infinite-depth or infinite-time/width assertion. Assertion
(3) is an absolute regression gap; no depth-uniform relative fraction of
activation energy is asserted.

The proof uses cubic input features to obtain a depth-independent initial
Gram bound, large gain to keep the entire fitting path close to its own
nonlinear initialization, and a direct nonlinear source estimate to
construct that path. The normalization below changes neither the raw
metric nor the trained algorithm.

#### 2. Exact normalization

Write a=a_delta and set

    Z_i^ell=z_i^ell/a^(ell-1), H_i^ell=h_i^ell/a^ell,
    K_ell=a^(ell-1),
    psi_ell(z)=z+K_ell^-1 atan(K_ell*z),
    F_i=<C,H_i^L>, so f_i=a^L F_i.                          (5)

The raw parameters, including the ORIGINAL readout C, are unchanged.
Then Z^ell=W^ell H^(ell-1), H^ell=psi_ell(Z^ell). At the bottom it is
convenient only notationally to write u_i=x_i/sqrt(d) and w=sqrt(d)W^1:
the bottom raw metric becomes its normalized L2 metric and Z_i^1=w.u_i.

For an auxiliary control c with ||c||_1<=3, use the raw gradient field
sum_i c_i grad F_i. Its backward recursion is

    q_i^L=C, d_i^ell=psi_ell'(Z_i^ell)q_i^ell,
    q_i^ell=(W^(ell+1))*d_i^(ell+1).

The update is C'=sum_i c_i H_i^L, each middle block has derivative
sum_i c_i d_i^ell tensor H_i^(ell-1), and w'=sum_i c_i d_i^1 u_i.
All blocks have the same raw metric. Since grad f_i=a^L grad F_i,
physical GF is exactly this control field with c_i=-r_i after the time
change s=a^L t. Equivalently, on the accumulated residual clock

    v(t)=a^L integral_0^t ||r(u)||_1 du,

the control is c=-r/||r||_1 and has norm one. At r=0 the physical field
vanishes; no differentiability of this normalized control is used.

The clipped auxiliary backward gates used in this proof are

    D_(ell,R)(z,q)=q+g(K_ell*z)tau_R(q), g(x)=(1+x²)^-1,

where tau_R is smooth, odd, 1-Lipschitz, equals q for |q|<=R and obeys
|tau_R(q)|<=min(|q|,2R). They satisfy

    |D|<=2|q|, |D_q|<=2, |D_z|<=K_ell|q|,
    |D_z|<=2K_ell R, 1<=psi_ell'<=2.                       (6)

For fixed L,a,R the clipped raw field is locally Lipschitz. These are
auxiliary layer-scaled clips; removing them recovers exactly (5) and the
original raw flow. The original finite random readout is retained in
both actual training algorithms; C(0)=0 refers to its population limit.

#### 3. Uniform initialization geometry

Put s_delta=delta(2-delta). For each i!=j set

    v_ij=(u_i-Gamma_ij*u_j)/sqrt(1-Gamma_ij²).

The vectors have norm one, are perpendicular to u_j, and satisfy
u_i.v_ij>=sqrt(s_delta). For {i,j,k}={1,2,3}, the unit tensor
R_i=u_i tensor v_ij tensor v_ik pairs to zero with u_j^tensor3 and
u_k^tensor3, and pairs to at least s_delta with u_i^tensor3. Therefore
for T=sum_i c_i u_i^tensor3, |c_i|s_delta<=||T||. Sum the three squared
inequalities to obtain

    Gamma^(circ3) >= s_delta² I/3 >= delta² I/3.            (7)

This allows singular Gamma. For G standard Gaussian and H3(G)=G³-3G,
Gaussian integration by parts twice gives

    E[atan(sigma G)H3(G)]
       = -2sigma³ E[G²/(1+sigma²G²)²].                      (8)

The cubic coefficient b3(sigma) is (8)/sqrt(6). Substituting x=sigma G
and restricting the integral to |x|<=1, for every sigma>=1,

    |b3(sigma)|
       = (2/sqrt(12*pi)) integral_R
            x²/(1+x²)² exp[-x²/(2sigma²)] dx
       >= (2/sqrt(12*pi))*exp(-1/2)*(1/6),
    b3(sigma)² >= eta0.                                    (9)

Here the integral lower bound uses (1+x²)²<=4 and integral_-1^1 x²dx=2/3.
For sigma=1 the cubic chaos of psi_1(G)=G+atan G is b3(1)H3(G)/sqrt(6).
The remaining chaos is orthogonal across all three sample coordinates:
E[H3(Z_i)H3(Z_j)]/6=Gamma_ij³ and Gaussian conditional expectation gives
the same cubic projection coefficient for cross terms. Thus the first
normalized feature Gram obeys

    Q_1(0) >= b3(1)² Gamma^(circ3) >= lambda I.              (10)

At each next initialized layer the normalized Gaussian preactivation
triple has covariance Q_(ell-1)(0) and equal positive marginal variance
q. The linear Gaussian regression coefficient of psi_ell is

    c=E[Z psi_ell(Z)]/q >=1.

The residual is orthogonal to every coordinate of that Gaussian triple,
so Q_ell(0)>=c² Q_(ell-1)(0)>=Q_(ell-1)(0). Consequently

    Q_L(0)>=lambda I                                      (11)

for every L>=2, with the same lambda. In raw variables each initialized
preactivation has variance at least a^(2(ell-1)), hence at least one.

#### 4. Explicit controlled primal bounds

Let

    T0=12/lambda, S=a^-L*T0, F=8^L.                        (12)

The source lemma in Fragment H.2 applies on this control interval
because

    a=10^10/lambda >=10^8(1+12/lambda).                      (13)

For completeness the independent primal estimates used here do not
assume source bounds or a clipped energy identity. The canonical
initialized action norms are at most 2, and it suffices to bound them
by 3. Finite initialized norms <=3 and first projection norms <=2 hold
with probability tending to one. Stop at hidden joint raw displacement
D=1. All current adjacent norms are then <=4 and bottom projection
norms <=3. Using (6),

    ||H_i^ell||_2<=8^ell, ||q_i^ell||_2<=8^(L-ell)||C||_2,
    ||C(v)||_2<=3Fv,
    D(v)<=3sqrt(L)F²v².                                    (14)

For instance each individual hidden block speed is bounded by F||C||
when ||c||_1<=3: 3*2*8^(L-ell)*8^(ell-1)<=F, with the same bound for the
bottom block. Summing squares over the L blocks and integrating C gives
an even smaller constant than in (14). On a positive Euler mesh use
sum_j h_j v_j<=v_k²/2. Thus the estimates exclude a first discrete
overshoot as well as a continuous first exit. The finite zero-readout
comparison program obeys them; for the actual finite C(0) its vanishing
initial norm is added until the fixed-cap bridge removes that error.

Telescoping each forward layer against its own initialized state gives

    ||Z_i^ell-Z_i^ell(0)||_2<=4*8^(ell-1)D,
    ||H_i^ell-H_i^ell(0)||_2<=8^ell D.                      (15)

Indeed the preactivation difference is at most
8^(ell-1)D+3*2 times the preceding preactivation difference; the displayed
bound is preserved by induction and holds at ell=1. With Q_L the
normalized top feature Gram, (14)-(15) yield

    ||Q_L-Q_L(0)||op <=6F²D
                    <=18sqrt(L) F^4 S².                    (16)

Let J_h be the true hidden differential of F=(F_1,F_2,F_3), and U_h,R
the clipped hidden direction map from coefficient vectors. Each
sample's hidden gradient has joint norm at most sqrt(L)F||C||. Since
there are three samples, both operator norms are <=sqrt(3L)F||C||,
and therefore

    ||J_h U_h,R||op <=3L F²||C||²
                    <=27L F^4 S².                         (17)

Finally, (15) and a>=1 give a bound in ORIGINAL preactivation coordinates:

    max_(i,ell) ||z_i^ell-z_i^ell(0)||_2
         <= a^(L-1)F D <=3sqrt(L)(512/a)^L T0²/a.            (18)

All these estimates are uniform in cap and apply to every control prefix.

Here is an explicit arithmetic check with comfortable slack, uniform in
L>=2. We have 0<lambda<1 and a=10^10/lambda. For 0<q<=1/4, the sequence
Lq^L decreases for L>=2, and sqrt(L)q^L<=Lq^L<=2q². Consequently

    18sqrt(L)(4096/a²)^L T0²
       <=36*(4096/a²)²*(144/lambda²) <lambda/4,
    27L(4096/a²)^L T0²
       <=54*(4096/a²)²*(144/lambda²) <lambda/4,
    3sqrt(L)(64/a²)^L T0² <1/4,
    3sqrt(L)(512/a)^L T0²/a
       <=6*(512/a)²*(144/lambda²)/a <sqrt(eta0)/2.            (19)

For example the largest numerator in the first two lines is less than
1.4*10^11, whereas a^4*lambda²=10^40/lambda². The last line is at most
3*10^8*lambda/10^30. These inequalities also verify the stopped primal
ball premise with strict slack. By (11), (16), (17),

    Q_L >=3lambda I/4, ||J_h U_h,R||op<=lambda/4.            (20)

#### 5. Global fitting for clipped flows and the nonlinear source estimate

The clipped physical raw direction is -a^L times the normalized update
field with coefficients r. Differentiating the actual predictions
f=a^L F along that direction gives exactly

    rdot=-a^(2L)(Q_L+J_h U_h,R)r.                           (21)

The hidden contribution need not be symmetric or positive. Its absolute
operator bound in (20) is enough. Before v(t) reaches S,

    (d/dt)||r||² <= -lambda*a^(2L)||r||²,
    ||r(t)||<=sqrt(3)exp[-lambda*a^(2L)t/2],
    v(t)<=a^L*sqrt(3) integral_0^infinity ||r(t)||dt
         <=6/(lambda*a^L)=S/2.                             (22)

Thus the controlled-budget stop cannot occur. Bounded clipped raw
speeds give a strongly Cauchy endpoint at any finite maximal physical
time; local Lipschitz existence from that endpoint continues the path.
Every clipped population flow is global. This did not assign the true
loss-energy identity to a clipped update.

The key new analytic estimate is proved in Fragment H.2. In the
normalization (5), with F=8^L, it constructs the ACTUAL strict forward
response densities and causal backward rows on every positive mesh,
uniformly in the incoming-field caps. Its constants obey

    alpha_ell=32^ell*3F²,
    b_ell=2048^(L-ell+1)B0, B0<=4F*T0/a,
    alpha_ell S b_ell
       <=24576*(1048576/a)^L*64^-ell*T0²/a.                 (23)

Condition (13) makes the last product <10^-10 and the associated
random derivative exponential parameter <10^-8 at every layer and
every finite depth. The crucial estimate retains actual Gaussian
covariances and current transpose returns: at the SAME source arrays,
the Gaussian part of q_ell has scale controlled by its already proved
raw L2 scale plus b_ell/K_ell. The bounded forward nonlinear remainder
atan(K_ell Z)/K_ell compensates the curvature K_ell. Strict production
then improves each coefficient radius, rather than assuming it remains
bounded. The proof supplies full local identities and constants.

Rewriting a fine physical Euler mesh by h_j=a^L Delta t_j||r_j||_1 and
c_j=-r_j/||r_j||_1 reproduces its normalized clipped updates. Freeze
these deterministic causal contractions in named-source derivatives.
The strict budget S/2 and fixed-cap Euler convergence imply sum h_j<S
on sufficiently fine meshes on each physical horizon. The source
lemma therefore yields, for fixed L,a, constants M,c>0 independent of
physical time and cap, for all normalized incoming fields Q,

    sup_(R,t) ||Q_R(t)||_p<=M sqrt(p), p>=2,
    sup_(R,t) ||Q_R(t)1_(|Q_R(t)|>u)||_2<=M exp(-cu²).       (24)

No temporal independence and no random time-maximum bound is used.

#### 6. Global population and finite-algorithm bridges

Fragment H.3 states the finite-depth bridge precisely and checks
its hypotheses here. Its local source is the finite adaptive Gaussian
conditioning construction in the existing self-contained manuscript,
special-data Section III.F and Fragment A, together with the fully derived cap/velocity/path
arguments in special-data Section III.V. Those arguments handle finitely many named
independent matrices by induction, and apply to the layer-dependent
bounded-derivative psi_ell in (5). The following are the substantive
verification steps, not additional assumptions.

* Finite clipped programs have bounded C^1 coordinate derivatives,
  deterministic causal scalar contractions, finitely many independent
  Gaussian matrices used in both orientations, and the required
  singular-query regularization. They give common L2 layer spaces,
  bounded initialized actions and genuine adjoints. Their learned
  rank-one integrals are Hilbert--Schmidt.
* (14), (19), (22) give global clipped reference paths, compact-time
  bounds and strict continuation slack. (23)-(24) give the cap-independent
  tails required for removal. The one-sided gate comparison has one
  factor R, not R^L, and uses tails of the reference only. Its error is
  C_T exp(C_T R-cR²). Hence clipped paths and their raw velocities are
  uniformly Cauchy in the raw Hilbert norm on each compact interval.
* The same comparison against any bounded-primal uncut competitor proves
  uniqueness and reached-state restart, with its own residual vector.
  No folding/exchange symmetry, positive input-Gram assumption or
  affine fitting clock is used.
* At fixed cap, coarse-mesh fixed-program width convergence and
  width-independent raw Euler stability give the finite GF/GD limits.
  The independent finite random readout has RMS O_P(n^-1), which is
  retained before this comparison. Ordered truncations for each appended
  true-backward and velocity product give the true raw kernels and
  velocity laws. State/velocity compactness and integrated speed bounds
  give the path laws. All iteration counts are finite once L and the
  observation horizon are fixed.

Taking the strong cap limit in (22) proves (2). The limiting vector
field is the actual raw gradient by the scalar predictor differential
and genuine adjunction, so its exact energy identity also holds.
Fragment H.3 spells out the estimates, observation definitions
and the order of limits; no different training scheme is substituted.

#### 7. Absolute nonaffinity and initial motion

For a square-integrable real X, write

    R(X)=inf_(alpha,beta) E[(atan X-alpha-beta X)²].

Every optimal regression slope can be chosen in [0,1]. When Var(X)>0,
this follows from the independent-copy identity for covariance and
0<=(atan x-atan y)/(x-y)<=1; when Var(X)=0 choose slope zero. If b is
such a slope at Y, the function atan x-bx is 1-Lipschitz, and testing
Y's optimal affine predictor at X shows

    sqrt(R(X)) <= sqrt(R(Y))+||X-Y||_2.

Interchanging X and Y proves that sqrt(R) is 1-Lipschitz under L2
coupling. By the cubic test (8)-(9), R(sigma G)>=eta0 for every sigma>=1.
Combine the initialized variances after (11) with (18)-(19) to get
R(z_i^ell(t))>=eta0/4, first for every clipped path and then for its
strong limit. Absorbing the linear a*z into the free affine predictor
gives (3).

Fragment H.4 proves (4) and all individual initial-motion claims
by induction on initialized Gaussian queries. Positive top feature
Gram and the nonconstant positive activation derivative give a positive
definite top backward Gram. Actual transpose returns preserve a fresh
positive Gaussian covariance at every lower layer. Each new forward
acceleration query has a Gaussian innovation orthogonal to the original
forward features, of strictly positive variance; it cannot cancel with
the current backward return. This supplies every sample's motion for
generic triples without permutation symmetry.

#### 8. Scope and comparison with the convex mixture

Excluding rho=-1 removes the direct antipodal oddness obstruction.
It does not imply positive input-Gram eigenvalues for three inputs:
three planar unit vectors at angles 120 degrees still sum to zero.
Nevertheless (7)-(10) show that their nonlinear initialized features
are independent. There is no counterexample here to the positive odd
convex mixture.

The new theorem uses a second device: a large overall gain. In (1),
phi_delta=2a_delta*[(1/2)z+(1/2)atan z]. Dividing by 2a_delta changes
the hidden features at every layer and changes their raw gradient
dynamics. Thus the theorem neither establishes an energy-normalized
activation nor proves a threshold for the exact unit-sum mixture.

The power delta^-2 in the sufficient gain is derived explicitly, uniformly
over all fixed finite depths. No matching necessary gain lower bound is
proved; the initialized cubic separation scale delta² is a different
claim whose sharpness does not establish gain optimality. A numerical
prefactor of approximately 2.77*10^13 in (1) is deliberately conservative.

### H.2. Direct large-gain source response

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Exact normalization and statement

Fix finite hidden depth L>=2 and three RMS-unit inputs. Put rho=a^(-L), K_l=a^(l-1),

    X_l=H_l/a^l, Y_l=Z_l/a^(l-1),
    psi_l(y)=y+K_l^(-1) atan(K_l y).

The raw hidden parameters are unchanged. Initially set the linear time coordinate u=a^L t and retain the ORIGINAL raw readout C. Write s for a general controlled clock; choosing s=u gives the physical residual controls below. The exact controlled equations are

    C'=sum_i c_i X_(L,i),
    V_l'=sum_i c_i d_(l,i) tensor X_(l-1,i), 2<=l<=L,
    w'=sum_i c_i d_(1,i) u_i,
    d_l=psi_l'(Y_l)q_l,
    q_L=C, q_l=A_(l+1)^*d_(l+1),
    Y_l=A_l X_(l-1), X_l=psi_l(Y_l), Y_1=<w,u>.

Actual outputs are f_i=a^L<C,X_(L,i)>. Original GF has c_i=y_i-f_i. The lemma allows ANY deterministic bounded controls ||c(s)||_1<=3.

**Lemma.** The case T=0 is trivial. Let T>0, S=a^(-L)T, and a>=10^8(1+T). Then on [0,S], incoming-field-capped source constructions and their finite Euler programs have strict raw hidden-ball slack, cap/mesh-uniform marginal subGaussian fields, integrable source derivatives, and the explicit actual coefficient box below. The gain condition is independent of L; each width limit still fixes finite L and a first. The displayed source construction has the population initialization C(0)=0. The finite Gaussian readout is retained when applying the width bridge.

The existing finite-depth population bridge therefore gives the strong uncut controlled population flow on this interval. A global original-GF application separately needs an accumulated residual-clock bound. This lemma alone does not assert fitting.

#### 2. Primal slack without capped energy

Assume initialized adjacent action norms <=3 and first-layer input projection norms <=2 (these bounds also hold with probability tending to one in the finite Gaussian model). Stop when the joint raw norm of HIDDEN parameter increments reaches one. Then current action norms <=4 and ||Y_1||_2<=3. Since |psi_l(y)|<=2|y|, all forward norms are <=F=8^L.

For smooth clips |tau_R(q)|<=|q|, |tau_R'|<=1 use

    D_(l,R)(z,q)=q+g(K_l z)tau_R(q), g(v)=(1+v^2)^(-1).

Thus |D|<=2|q|. A common normalized incoming cap Rcap corresponds to raw layer-dependent caps a^(L-l)Rcap, because the original raw incoming field at layer l is a^(L-l)q_l. These caps are an approximation scheme for the unchanged raw GF, not a change of metric. Readout integration gives, without energy,

    ||C(s)||_2<=3Fs<=R, R=3FS,
    ||q_(l,i)||_2<=Q_l=8^(L-l)R,
    ||d_(l,i)||_2<=2Q_l.

Each hidden update block has norm <=F R. The joint hidden displacement is therefore <=

    3sqrt(L) F^2 S^2 =3sqrt(L)(64/a^2)^L T^2 <1/4.

This excludes first exit, also at arbitrary finite Euler nodes by summing their step lengths. Under the gain condition, max_l Q_l<=1/2, so max_l ||d_l||_2<=1. Actual preactivation L2 norms are <=F independently of source coefficient bounds.

#### 3. Exact local source system

Freeze deterministic source arrays, controls and source covariances. At layer l write

    Y_l=xi_l+mathcalA_l d_l,
    q_l=zeta_l+mathcalB_(l+1) X_l,
    X_l=psi_l(Y_l), d_l=D_(l,R)(Y_l,q_l).

mathcalA_l is strict and mathcalB_(l+1) causal. At the bottom xi_1 is the repeated Gaussian root and mathcalA_1 has blocks h_j Gamma diag(c_j), strict density <=3. At the top zeta_L=0 and mathcalB_(L+1) is the readout integrator with causal row <=3S. Remaining primitive groups are the original jointly centered Gaussian groups, with full second-moment covariances and the named-slot convention if singular.

For an internal initialized matrix the exact coefficients are

    (mathcalA_(l+1,kj))_uv
      =E partial_(zeta_(l,j,v)) X_(l,k,u)
       +h_j c_(j,v) E[X_(l,k,u)X_(l,j,v)], j<k,

    (mathcalB_(l,kj))_uv
      =E partial_(xi_(l,j,v)) d_(l,k,u)
       +1_(j<k)h_j c_(j,v)E[d_(l,k,u)d_(l,j,v)], j<=k.

All current returns are included. Within each time row the order is mathcalA_2,...,mathcalA_L,mathcalB_L,...,mathcalB_2.

Use the induced infinity norm on three-sample blocks and full row sums. Locally assume strict density alpha for mathcalA_l and causal row b for mathcalB_(l+1). Let r=alpha S b.

#### 4. Same-array Gaussian-part identity

Write

    r_l=K_l^(-1)atan(K_l Y_l), |r_l|<=pi/(2K_l),
    e_l=g(K_l Y_l)tau_R(q_l), |e_l|<=|q_l|.

Thus X_l=Y_l+r_l and d_l=q_l+e_l. At the SAME actual coefficient arrays put

    Rloc=(I-mathcalA_l mathcalB_(l+1))^(-1),
    U=Rloc mathcalA_l,
    Lloc=(I-mathcalB_(l+1)mathcalA_l)^(-1),
    Y_G=Rloc xi_l+U zeta_l,
    q_G=Lloc zeta_l+mathcalB_(l+1)Rloc xi_l.

These are centered Gaussian combinations of frozen-source groups. Exact elimination gives

    Y_l-Y_G=U e_l+U mathcalB_(l+1)r_l,
    q_l-q_G=mathcalB_(l+1)U e_l+Lloc mathcalB_(l+1)r_l.

For r<=1/8 the two resolvent rows are <=2, |U|row<=2alpha S, and |mathcalB U|row<=2r. Consequently

    ||q_l-q_G||_p<=2r||q_l||_p+pi b/K_l.

The independently proved actual L2 bound implies

    ||q_G||_2<=2Q_l+4b/K_l.

Gaussian moments and absorption give, for p>=2,

    max_i ||q_(l,i)||_p<=20(Q_l+b/K_l)sqrt(p),
    ||K_l max_i|q_(l,i)|||_p<=W_l sqrt(p),
    W_l=60(n_l+b), n_l=K_l Q_l.

The bounded nonlinear remainder pi/(2K_l) compensates the local curvature K_l. No independence between Gaussian and remainder is needed.

Likewise,

    max_i ||Y_(l,i)||_p
      <=[F+50alpha S(Q_l+b/K_l)]sqrt(p).

In the actual box below the bracket is <=2F, so ||X_(l,i)||_p<=4F sqrt(p). These are suprema of marginal norms, not random time maxima.

#### 5. Exact source derivatives and coefficient production

With G=diag psi_l'(Y), V=diag partial_q D, N=diag partial_z D,

    ||G||,||V||<=2,
    ||N_k||<=K_l max_i|q_(l,k,i)|.

Any named source Jacobian J of Y obeys exactly

    J=I_xi+mathcalA_l[NJ+V(I_zeta+mathcalB_(l+1)GJ)].

Current mathcalB_(l+1,kk) is retained. Strict mathcalA_l prevents a current algebraic loop. Finite Volterra iteration gives

    ||partial_xi Y_(l,k)||row<=E_k,
    ||partial_(zeta_j)Y_(l,k)||<=2alpha h_j E_k, j<k,
    E_k=exp(4alpha b S
             +alpha sum_(r<k)h_r K_l max_i|q_(l,r,i)|),

    ||partial_xi d_(l,k)||row
      <=(K_l max_i|q_(l,k,i)|+4b)E_k.

The subGaussian criterion and weighted Jensen (no temporal independence) give

    E exp(u|Z|)<=2exp(2 exp(1)M^2u^2)

when ||Z||_p<=M sqrt(p). If alpha S b<=10^(-9) and alpha S W_l<=10^(-6), safe production bounds are

    alpha_(l+1,new)<=3F^2+16alpha,
    b_(l-1,new)<=512(n_l+b)+3S.

For the reverse response, Cauchy--Schwarz bounds its expectation by

    sqrt(2)(sqrt(2)W_l+4b)
       exp(4alpha b S+4exp(1)alpha^2 S^2 W_l^2)
       <512(n_l+b).

The reverse learned contraction is <=3S since ||d_l||_2<=1; the forward learned density is <=3F^2.

#### 6. Explicit box uniform over finite depths

For a>=8,

    n_l=3F(T/a)(8/a)^(L-l),
    nmax=3FT/a.

Set

    B0=nmax+3S<=4FT/a,
    alpha_l=32^l *3F^2,
    b_l=2048^(L-l+1)B0, 1<=l<=L.

Here b_l bounds incoming mathcalB_(l+1). Actual top row 3S is strictly inside b_L and bottom density 3 is strictly inside alpha_1.

Keeping every depth factor,

    alpha_l S<=3(2048/a)^L T,
    alpha_l S b_l
      <=24576(1048576/a)^L 64^(-l)T^2/a
      <=384(1048576/a)^L T^2/a.

For a>=10^8(1+T), L>=2,

    alpha_l S<10^(-8),
    alpha_l S b_l<10^(-10),
    alpha_l S W_l<10^(-8).

Indeed n_l<=B0<=b_l/2048, so W_l<=61b_l. All preceding estimates apply and strictly improve the box:

    alpha_(l+1,new)<=3F^2+16alpha_l
                       <=17alpha_l<32alpha_l=alpha_(l+1),
    b_(l-1,new)<=512(n_l+b_l)+3S
                   <514b_l<2048b_l=b_(l-1).

Chronological induction proves the ACTUAL box on every finite mesh. A forward row uses previously constructed reverse history; a reverse row is built after the current higher reverse row. There is no circular radius premise and no smallest-step denominator.

### H.3. Canonical construction, cap removal and complete observation limits

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Finite programs and common action spaces

A program has a fixed finite number of instructions on layer-typed
vectors: independent Gaussian roots; fixed C^1 coordinate maps with
bounded continuous first derivatives; linear combinations; applications
of any of the L-1 initialized independent Gaussian adjacent matrices or
their transposes; and causal scalar feedback from same-layer inner
products through locally Lipschitz scalar maps. Each fixed program's
within-layer joint empirical laws, including second moments, converge
in probability in W2 along the full width sequence. An oriented matrix
call on input h is represented by its centered Gaussian source plus the
sum of its expected named derivatives against earlier opposite-orientation
sources, multiplied by those opposite inputs. Each oriented source
group's covariance is the FULL Gram of its actual inputs. Different
oriented groups are independent. Named slots remain separate even when
source covariances are singular; all scalar feedback, expectations and
covariances are frozen in those derivatives.

Here is why the existing proof applies to L-1 matrices. Conditional on
previous queries of a particular Gaussian matrix, its unused block is
P_left G P_right; all other matrices remain separately conditioned
through their own transcripts. The next query is the conditional mean
plus this independent Gaussian innovation. Empirical bounded-test and
second-moment concentration identify its next scalar law. Query-input
perturbation by independent Gaussian noise makes each provisional Gram
invertible. Fixed-program bounded-operator stability removes that noise;
positive-semidefinite square-root continuity couples the limiting
covariances at singularities. Induction counts instructions, not layers.
Adding finitely many matrices only adds finitely many such steps. No
source-covariance inverse remains in the final identity.

A countable language including all rational linear combinations,
bounded smooth coordinate probes, integer clips, rational meshes and
both action orientations generates one probability space per layer.
Finite-program consistency supplies their joint cylinder laws. On the
dense span of generated fields, the finite norm and inner-product
identities pass to the limit. Hence each initialized action extends
boundedly to its layer L2 space, and its reverse is its genuine Hilbert
adjoint. Approximation by bounded smooth cylinder functions gives density
in L2. These are the canonical initialization spaces, not arbitrary
bounded operators with the same norms.

The population parameter space is the first-layer vector L2 space,
the affine spaces A_(ell,0)+HS(H_(ell-1),H_ell), and the top readout H_L.
The raw metric is the one in Fragment H.1. Rank-one velocities have norm
||u tensor v||HS=||u||_2||v||_2, so continuous raw updates integrate in
HS. Their reversed increments are their actual adjoints.

In our application, every psi_ell has bounded continuous derivative and
every fixed clipped backward gate D_(ell,R) has bounded continuous first
derivatives. Scalar physical feedback is the residual vector, a locally
Lipschitz function of inner products on bounded primal balls. All the
finite-program hypotheses have therefore been checked. The effective
residual-clock controls are frozen only in formal source derivatives;
the physical residual feedback remains part of the actual dynamics.

#### 2. Fixed-cap existence and asymmetric comparison

For fixed finite L,a,R, forward and backward induction on a bounded
primal ball gives a raw locally Lipschitz field. The first projection
map is bounded in the raw metric; every next layer uses a bounded
action, a Lipschitz activation and continuous bilinear evaluation.
The clipped gates are globally Lipschitz. Each rank-one update is
locally Lipschitz by

    ||u tensor v-u' tensor v'||HS
       <=||u-u'||_2||v||_2+||u'||_2||v-v'||_2.

The integral map is a contraction on a sufficiently short interval.
Strong Cauchy endpoints and the uniform primal bounds extend the clipped
solution. Fragment H.1 Sections 4--5 establish its global continuation with
strict residual-clock slack, independently of all cap-removal arguments.

For R'>=R, including R'=infinity, the normalized gates obey

    |D_(ell,R')(z,q)-D_(ell,R)(z',q')|
      <=2|q-q'|+2K_ell R|z-z'|
           +2|q'|1_(|q'|>R).                              (25)

To verify (25), first change q to q' in D_(ell,R'), which costs at most
2|q-q'|. In the remaining nonlinear term use the decomposition

    [g(K_ell z)-g(K_ell z')]tau_R(q')
       +g(K_ell z)[tau_R'(q')-tau_R(q')],

where tau_R' in this display denotes the clip at level R', not a
derivative. Bounded g', |tau_R|<=2R, and equality of both clips inside
[-R,R] give the other two terms. This asymmetric decomposition requires
tail control only of the reference state (z',q').

Forward state differences are bounded by C times the raw state
difference. Backward substitution through any finite L multiplies an
existing discrepancy only by a bounded action and the gate's q-Lipschitz
constant 2. Every newly introduced factor R multiplies a FORWARD
discrepancy already bounded separately. It does not multiply a previous
R term. Rank-one updates and residual feedback then give

    ||F_R'(Theta)-F_R(Theta')||raw
      <=C_(L,a,b)(1+R)||Theta-Theta'||raw
         +C_(L,a,b) sum_Q ||Q(Theta')1_(|Q(Theta')|>R)||_2.  (26)

Here F_R' means the field at cap R', b denotes the common primal ball,
and the finite sum runs over the reference's incoming fields. The same
bound holds for all backward field differences. Physical gain factors
are fixed constants a^L. Coefficient differences in residual feedback
are bounded by the already controlled forward and readout differences.

Fragment H.2 and Fragment H.1 (24) provide Gaussian reference tails
uniformly in time and cap. Integrating (26) and Gronwall's inequality
therefore gives on each physical [0,T]

    sup_(t<=T)||Theta_R'(t)-Theta_R(t)||raw
       +sup_(t<=T)||F_R'(Theta_R'(t))-F_R(Theta_R(t))||raw
                       <=C_T exp(C_T R-cR²).               (27)

Polynomial factors in R are absorbed into C_T exp(C_T R). Thus paths
and raw velocities are uniformly Cauchy. Their limit is strong C^1 and
satisfies the uncut equations by (26) and bounded-multiplier continuity.
Taking integer caps and horizons gives one consistent global solution.

For any other strong uncut solution with bounded primal quantities on
[0,T], compare it to the same clipped reference using (26). Only its
primal bound enters C_T; its own tails are not assumed. Equation (27)
forces equality in the limit. At a reached time t0, the initial error
against the clipped reference is already of the form (27), and another
factor exp(C_T R) still tends to zero. This proves uniqueness of
continuation from that state. No arbitrary-state L2 local theorem for
the uncut vector field is used.

#### 3. Strong chain rule and raw gradient identification

If X(t) is a strong C^1 L2 curve and psi is C^1 with bounded continuous
derivative, then psi(X(t)) is strong C^1 and has derivative psi'(X)X'.
Indeed integrate X' to obtain almost-everywhere absolutely continuous
coordinate versions and apply the scalar chain rule. The multiplier
product is L2-continuous: if X_k->X and P_k->P in L2, split

    psi'(X_k)P_k-psi'(X)P
      =psi'(X_k)(P_k-P)+[psi'(X_k)-psi'(X)]P.

Boundedness treats the first term; convergence in probability and an
integrable |P|² dominator treat the second. The coordinate integral
identity passes to L2. Repeating with the continuous bilinear action
product rule proves the strong forward chain rule at all L layers.

The scalar predictor's hidden directional derivative pairs each raw
increment against the corresponding backward rank-one field. This
follows by repeated Hilbert adjunction and Cauchy--Schwarz; all gates
are bounded and all fields are L2. The first-block factor is 1/d in
the original w coordinates. The scalar derivative is continuous in
the raw state: the same bounded-multiplier argument treats varying
backward fields. Consequently the limiting autonomous equations are
the raw Hilbert gradient flow of the stated squared loss, and its
energy identity follows by the scalar chain rule. No Frechet
differentiability of the activation map on a whole L2 ball is asserted.

#### 4. Fixed-cap finite GF and raw GD

At a fixed cap and physical horizon, take a coarse mesh of finitely
many time steps. The finite-program theorem identifies its full-width
limit. Scalar feedback uses all three residuals, not a prescribed
population residual in place of the actual finite residual. A sufficiently
large finite primal ball contains these coarse nodes with high
probability: first-layer and readout norms converge, and each hidden
matrix increment is bounded by the sum of its rank-one update lengths,
whose finitely many contractions converge.

On that enlarged ball the clipped field has norm M0 and Lipschitz
constant L0 independent of width. The exact GF/Euler local defect for
a step h is <=L0 M0 h²/2. Iteration gives a uniform state error bounded
by C_T times the mesh size, with first-exit slack keeping all states
in that ball. This proves finite GF versus the coarse Euler program,
and simultaneous raw Euler with fine step n^-2 versus that GF. It
does not apply fixed-program convergence to n² growing instructions.
Take width first at the coarse mesh, then send that fixed mesh size
to zero. The population coarse Euler program converges by the same
Hilbert-space estimate. Its limit is the unique clipped solution.

The actual finite Gaussian C_n(0) has E(||C_n(0)||_Euclidean^2/n)=n^-2. Its initial
discrepancy from the zero-readout finite comparator is O_P(n^-1).
The fixed-cap Lipschitz comparison bounds the propagated discrepancy
by exp(L0 T)O_P(n^-1). Thus zero is the population initial readout;
neither actual finite GF nor actual finite GD is initialized at zero
by substitution.

For the uncut finite algorithms, apply (26) with the finite clipped
reference. At fixed cap, the finite empirical incoming tails converge
to their population reference tails, using continuous truncations and
second-moment convergence. Uniformity in time comes from a finite time
net and the fixed-cap strong moduli described below. Finite first-exit
comparison then gives limsup-width errors of the form (27). For GD,
the discrete version has the same single factor R and a vanishing
fixed-cap O(n^-2) consistency term; the hidden fields are recomputed
from the raw linear interpolation. Send width to infinity first and
then R to infinity. This gives both algorithms the same full-sequence
limit. A subsequence argument upgrades any almost-sure extracted
comparisons to convergence in probability of the original full sequence.

#### 5. True kernels, velocities and paths

For the original raw model let b_i^ell be the TRUE backward fields.
The L+1 kernel blocks are

    K^1_ij=Gamma_ij <b_i^1,b_j^1>,
    K^ell_ij=<b_i^ell,b_j^ell><h_i^(ell-1),h_j^(ell-1)>,
                 2<=ell<=L,
    K^(L+1)_ij=<h_i^L,h_j^L>.

Every inner product is within its designated layer. These are the true
raw kernels even when observed at an auxiliary clipped state; clipped
update fields are not substituted for their b fields.

The fixed-cap observation proof in special-data Section III.V V.3--V.6 has these
premises: bounded clipped primal states on the observation interval;
bounded continuous coordinate derivatives; deterministic causal
source coefficients; finite-dimensional Gaussian query perturbations
continuous under vanishing perturbation; and the already proved
fixed-mesh primary width laws. All were verified in Sections 1--4.
Its depth induction proceeds as follows.

A fresh independent Gaussian probe added to any named answer slot
changes the recomputed clipped raw trajectory by C epsilon, or by
C h_j epsilon if inserted only at a strictly past time j. Gaussian
integration by parts with deterministic coefficients frozen bounds
the ABSOLUTE ROW OF EXPECTED source derivatives, after choosing signs,
by C or C h_j. Current reverse responses are retained and constructed
in descending layer order. With these deterministic rows bounded,
differentiate the local source equations pointwise. Bounded gate
derivatives and the strict forward time order yield a discrete
Volterra inequality U_k<=C+C sum_(j<k)h_j U_j for the maximum primary
absolute derivative row. Summation of nested time integrals costs at
most the fixed horizon. The L-1 backward levels are a finite causal
substitution, so U_k<=C exp(CT). Repeating with Lp norms gives primary
source bounds C sqrt(p). No matrix Lp-to-Lp action bound is assumed.

Append instantaneous velocity queries in ascending layer order. With
P_i^ell=dot z_i^ell and U_i^ell=phi'(z_i^ell)P_i^ell,

    P_i^1=dot w.x_i,
    P_i^ell=dot A_ell h_i^(ell-1)+A_ell U_i^(ell-1).

The learned action part is an explicit rank integral. For each newly
appended initialized-action call, its reverse-source derivative is a
sum of the previously bounded derivatives and a bounded gate derivative
times the incoming velocity. Its Gaussian source variance is the actual
L2 norm of that incoming query. The preceding layer and primal raw
direction bounds control this norm before any higher-layer velocity
estimate is invoked. Induction yields fixed-cap marginal C_(L,R,T)
sqrt(p) bounds for appended velocities on population fine meshes and
flows. Same-family joint time and sample covariances are retained.

Products phi'(Z)P do not have globally bounded derivatives in (Z,P).
The observation proof therefore uses phi'(Z)tau_M(P), a legitimate
bounded-derivative instruction, and removes the clips in the following
order: keep the new outer query cap M fixed while removing all earlier
inner velocity caps, then remove M using the proved marginal tail
bounds. True-backward observations use the same descending ordered
truncation. This verifies the fixed-program laws of the unbounded
products rather than assuming them. The construction uses L steps,
each already supplied with the previous step's norm and tail estimate.

For a state/direction pair and a reference pair, the deterministic
product comparison has the form

    ||phi'(Z)P-phi'(Z0)P0||_2
       <=C||P-P0||_2+C M||Z-Z0||_2
                  +C||P0 1_(|P0|>M)||_2.                  (28)

It follows by splitting P0 at M and using bounded phi' and phi''.
Forward induction leaves one M times the primary state discrepancy,
plus the reference velocity tails. At fixed cap, the proved moment
bounds and raw Lipschitz state/direction estimates yield a uniform
L2 time modulus for velocities (a square-root modulus suffices).
This justifies passage from finite time nets to uniform-in-time
state/velocity empirical W2 laws. In the cap-removal step, the uncut
reference's velocity image is compact in L2 by the strong chain rule,
which implies uniform L2 tail removal. Equation (28), with state/raw
direction convergence first and M then sent to infinity, transfers
these velocity laws to the uncut flow. It does not require an unproved
cap-uniform pointwise bound on the entire velocity path.

All true kernel terms are continuous functions of the corresponding
convergent L2 backward and feature pairs, so their convergence is
uniform on the physical horizon. Joint observations at any fixed finite
collection of times are included by appending that finite list before
the fixed-program limit. The same applies to fixed finite generated
probes formed from layer-typed bounded-derivative maps, contractions
and either action orientation. Second moments and integrals of squared
speeds follow from the uniform W2 state/velocity convergence.

Finally, a continuous coordinate path X with square-integrable speed
and its piecewise-linear interpolation on a mesh of size h obey

    ||X-Interp_h X||_infinity² <=4h integral_0^T |X'(t)|²dt.

This is the intervalwise Cauchy--Schwarz estimate and the triangle
inequality between endpoints. Apply it inside each empirical layer
law and inside the population law. Fixed-mesh joint laws converge;
the integrated speed bounds make both interpolation errors uniformly
small as h decreases. This proves W2 convergence in the uniform path
norm, without replacing a supremum of marginal moments by a moment of
a random time supremum.

Every estimate above is for fixed finite L,a and a fixed physical
horizon. Width precedes the auxiliary cap and observation-truncation
limits. The common activation in Fragment H.1 is independent of L, but
the bridge constants and the width needed for a prescribed accuracy
need not be uniform in L. This distinction completes the theorem's
stated quantifiers.

### H.4. Every sample and layer moves initially at arbitrary fixed depth

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Setup and statement

Fix an integer L>=2 and three normalized inputs u_i=x_i/sqrt(d), with

    ||u_i||=1, Gamma_ij=<u_i,u_j>, |Gamma_ij|<=1-delta (i!=j), delta>0.

Only feasible data are quantified over. Let y_i in {-1,1}, p_i=y_i/3, and take the same activation in every hidden layer,

    phi(z)=a(z+atan z), a>0.

The argument in fact works for phi(z)=a z+e atan z with any independent a,e>0. In the stated odd-gain case e=a. Write A_l:H_(l-1)->H_l for the canonical initialized action of W^l, l=2,...,L, including its genuine adjoint. The first initialized projection tuple Z^1 has law N(0,Gamma), and recursively

    h_i^l=phi(Z_i^l), Z_i^l=A_l h_i^(l-1) (l>=2),
    D_i^l=phi'(Z_i^l), Q_l=(<h_i^l,h_j^l>)_(ij).

All objects in this proof unit are at initialization unless a time argument is displayed. Set

    H=sum_i p_i h_i^L,
    beta_i^L=D_i^L H,
    q_i^l=A_(l+1)^* beta_i^(l+1), beta_i^l=D_i^l q_i^l (l<L),
    S_l=(<beta_i^l,beta_j^l>)_(ij).

The raw hidden directions are

    V^1=d^(-1)sum_i p_i beta_i^1 x_i,
    V^l=sum_i p_i beta_i^l tensor h_i^(l-1), 2<=l<=L.

Their sample preactivation/feature directions are

    U_j^1=V^1 dot x_j=sum_i Gamma_ji p_i beta_i^1,
    t_j^l=D_j^l U_j^l,
    U_j^l=V^l h_j^(l-1)+A_l t_j^(l-1), 2<=l<=L.

Every V^l, every U_j^l, and every t_j^l is nonzero in its appropriate raw, HS, or L2 norm. No sample permutation symmetry or scalar residual clock is assumed.

For any canonical strong physical gradient flow from C(0)=0 with the strong chain rule, these yield

    (theta_h^l)''(0)=9 V^l, (z_j^l)''(0)=9 U_j^l,
    (h_j^l)''(0)=9 t_j^l,

as strong right derivatives. If K_total is the actual sum of all L hidden kernel blocks and the readout block, then

    p^T K_total(t)p=p^T K_total(0)p+18 t^2 ||V||_hidden^2+o(t^2),

where ||V||_hidden^2=d||V^1||_2^2+sum_(l=2)^L ||V^l||_HS^2>0.

#### 2. Initial forward Grams are positive, including singular Gamma

Let G be standard normal, H_3(z)=z^3-3z, and

    b_3=E[atan(G)H_3(G)]/sqrt(6)
       =(1-2 E[(1+G^2)^(-1)])/sqrt(6) !=0.

The equality follows by Gaussian integration by parts. Strict Jensen gives E[(1+G^2)^(-1)]>1/2, hence b_3!=0.

The cubic tensor lift of three absolutely separated lines satisfies

    Gamma^(circ 3)>=[delta^2(2-delta)^2/3] I_3.

A direct verification uses, for each i and the other indices j,k,

    v_ij=(u_i-Gamma_ij u_j)/sqrt(1-Gamma_ij^2),
    R_i=u_i tensor v_ij tensor v_ik.

Then ||R_i||=1, <u_l^(tensor 3),R_i>=0 for l!=i, and the i-th pairing is at least delta(2-delta). Applying Cauchy--Schwarz to sum_l c_l u_l^(tensor 3) and summing the resulting three inequalities proves the bound. This never inverts Gamma.

Projecting the first features onto cubic Gaussian chaos gives, for phi=a z+e atan z,

    Q_1>=e^2 b_3^2 Gamma^(circ 3)>0.

At every following layer the three centered Gaussian preactivations have a common positive marginal variance. The coefficient of the orthogonal projection of phi(Z_i) onto the Gaussian first chaos is at least a, because z atan z>=0. The orthogonal residual contributes a positive semidefinite Gram. Therefore

    Q_l>=a^2 Q_(l-1)>0, 2<=l<=L.

In particular Z^l has full three-dimensional Gaussian support for every l>=2 and H!=0. For e=a,

    ||H||_2^2 >= a^(2L)b_3^2 delta^2(2-delta)^2/9.

Neither singularity of the first Gaussian tuple nor cancellation of an affine label direction invalidates this positivity.

#### 3. Backward Grams, all parameter blocks, and bottom sample motion

Because L>=2, Z^L has a positive Gaussian density on R^3. If v^T S_L v=0, continuity implies the identity

    [sum_i p_i phi(z_i)] [sum_i v_i phi'(z_i)]=0 on R^3.

The first factor has no open zero set: its derivative in each coordinate is p_i phi'(z_i), which never vanishes. Consequently the second factor vanishes everywhere. Differentiating in coordinate i gives v_i phi''(z_i)=0 for every z_i. Since e>0 and phi'' is not identically zero, v_i=0. Thus S_L is positive definite.

The exact reused-transpose initialization rule, with its returns retained, is

    q_i^l=zeta_i^l+sum_k R^l_ik h_k^l, 1<=l<L.

The coefficient matrices R^l are deterministic Gaussian response coefficients. The primitive reverse group zeta^l is centered Gaussian with full covariance S_(l+1), independently of the forward groups and roots. These are canonical same-matrix identities, not independent replacements for A_(l+1)^*. For explicit dependency checking, their initial coefficients are constructed downwards by

    R^(L-1)_ik=p_k E[D_i^L D_k^L]+1_(i=k) E[H phi''(Z_i^L)],
    R^l_ik=1_(i=k) E[phi''(Z_i^(l+1))q_i^(l+1)]
                +R^(l+1)_ik E[D_i^(l+1)D_k^(l+1)], l<L-1.

These identities follow by differentiating beta_i^(l+1) in the named Z_k^(l+1) slot with other primitive source groups frozen. They retain both the local current curvature term and the next-layer return. No current response is inverted or discarded.

Conditionally on Z^l,

    Cov(beta^l | Z^l)=diag(D^l) S_(l+1) diag(D^l)
                    >=a^2 lambda_min(S_(l+1)) I_3.

The return term is measurable in Z^l and does not change this conditional covariance. Induction from S_L>0 gives S_l>0 for every l. In particular

    Cov(beta^1 | Z^1)>=a^2 lambda_min(S_2) I_3.

This remains true when Z^1 is singular. It implies

    d||V^1||_2^2>=a^2 lambda_min(S_2) sum_i p_i^2>0,
    ||U_j^1||_2^2>=a^2 lambda_min(S_2) sum_i Gamma_ji^2 p_i^2
                  >=a^2 lambda_min(S_2)p_j^2>0.

For every hidden matrix block,

    ||V^l||_HS^2=tr(diag(p) S_l diag(p) Q_(l-1))>0, 2<=l<=L.

Here Q_(l-1) and S_l are positive definite and diag(p) is invertible. The trace of the product of two positive definite matrices is positive: conjugating one by the positive square root of the other makes this explicit. Thus all hidden parameter blocks and all bottom samples already have strictly positive direction norm.

#### 4. Every upper sample: a recursive exact return formula

For each fixed sample j define deterministic coefficients

    c^1_ji=Gamma_ji p_i,
    c^l_ji=p_i (Q_(l-1))_ij
              +c^(l-1)_ji E[D_j^(l-1)D_i^(l-1)], 2<=l<=L.

For l>=2, let xi_(t_j^(l-1)) be the primitive forward source associated with the added call A_l t_j^(l-1), in the same Gaussian source group as Z^l. We claim the exact identity

    U_j^l=xi_(t_j^(l-1))+sum_i c^l_ji beta_i^l.             (A)

At the bottom,

    partial_(zeta_i^1) t_j^1=D_j^1 c^1_ji D_i^1.

The same-matrix forward return rule is consequently

    A_2 t_j^1=xi_(t_j^1)+sum_i beta_i^2 c^1_ji E[D_j^1D_i^1].

Adding V^2 h_j^1=sum_i p_i (Q_1)_ij beta_i^2 proves (A) for l=2.

Suppose (A) holds at layer l<L. Every named A_l-forward source is independent of the primitive A_(l+1)-reverse group zeta^l. The coefficients in (A) are deterministic. The initialized backward field beta_i^l=D_i^l(zeta_i^l+sum_k R^l_ik h_k^l) depends on zeta^l with derivative D_i^l. Hence

    partial_(zeta_i^l)t_j^l=D_j^l c^l_ji D_i^l.

The next forward return is exactly

    A_(l+1)t_j^l=xi_(t_j^l)+sum_i beta_i^(l+1)c^l_ji E[D_j^lD_i^l].

Adding the matrix-block contribution V^(l+1)h_j^l proves (A) at layer l+1. This establishes (A) through every fixed depth. The second term in c^l is the genuine same-matrix return; omitting it would give a different and incorrect formula.

#### 5. Positive innovations persist through every layer

Regress xi_(t_j^(l-1)) on the three original forward sources Z^l in its own action group. Their covariance is Q_(l-1)>0, so this regression has a well-defined independent Gaussian remainder epsilon_(l,j). Its variance is exactly

    sigma_(l,j)^2=inf_(b in R^3)||t_j^(l-1)-sum_i b_i h_i^(l-1)||_2^2. (B)

The equality is the covariance rule for forward queries of the same initialized Gaussian action, not an assumption that different calls use different matrices.

For l=2 the features h_i^1 are measurable with respect to Z^1. Therefore (B), conditional variance, and Section 3 give

    sigma_(2,j)^2
       >=E Var(t_j^1 | Z^1)
       =E[(D_j^1)^2 sum_(i,k) c^1_ji D_i^1 (S_2)_ik D_k^1 c^1_jk]
       >=a^4 lambda_min(S_2) sum_i Gamma_ji^2 p_i^2
       >=a^4 lambda_min(S_2)p_j^2>0.                    (C)

The remainder epsilon_(2,j) is independent of Z^2 and the independent reverse group zeta^2 (when L>2). Formula (A) expresses all other terms in U_j^2 as functions of those reference variables. At L=2, beta^2 is a function of Z^2 alone. Thus epsilon_(2,j) cannot cancel in U_j^2.

Now assume l>=2 and l<L. After regression, (A) has the form

    U_j^l=epsilon_(l,j)+F_(l,j)(Z^l,zeta^l),

where epsilon_(l,j) is independent of (Z^l,zeta^l), has variance sigma_(l,j)^2, and F_(l,j) is a measurable function of the displayed reference variables. Consequently

    Var(t_j^l | Z^l,zeta^l)=(D_j^l)^2 sigma_(l,j)^2.

Each h_i^l is measurable in Z^l. Applying (B) at layer l+1 yields

    sigma_(l+1,j)^2>=E Var(t_j^l | Z^l,zeta^l)
                    =E[(D_j^l)^2]sigma_(l,j)^2
                    >=a^2 sigma_(l,j)^2>0.             (D)

Its new Gaussian remainder is independent of Z^(l+1) and zeta^(l+1), or of Z^L alone at the final layer. Formula (A) again prevents cancellation. This proves U_j^l!=0 for every j and l=2,...,L, with the concrete bound

    ||U_j^l||_2^2>=sigma_(l,j)^2
                   >=a^(2l)lambda_min(S_2)p_j^2>0.

Together with the bottom estimate this covers every sample and layer. Since D_j^l>=a, all feature directions t_j^l are nonzero as well.

Different samples' added forward sources may be correlated; the proof needs only each remainder's independence from the original forward tuple and the separate reverse group. It does not assume that the three added remainders are mutually independent. One may establish the argument in a separate fixed transcript for each j, then include the finite union of those queries on the common canonical space.

#### 6. Why the augmented finite programs and innovations are valid

The initialization program has finitely many action calls for fixed L and three samples. Every original backward field has the form of a bounded smooth gate multiplying a finite sum of Gaussian sources and linear-growth functions of Gaussian forward sources. Formula (A) has that form too. All fields appearing in the added queries therefore have every finite moment.

The inputs t_j^l are not asserted to be globally Lipschitz functions of all named sources. To apply the derivative-valid fixed-program theorem, smoothly clip each unbounded incoming factor, use its bounded-derivative finite program, and remove the clips. Canonical action operator bounds give convergence of the actual forward and transpose answers in L2. The source derivatives required above are explicitly D_j^l c^l_ji D_i^l, which are bounded because phi' is bounded and c^l is deterministic. More generally the clipped return terms have integrable finite-source envelopes. Dominated convergence therefore passes the response coefficients. The converging finite covariance Grams identify the joint source limits using continuity of positive semidefinite square roots, without a pseudoinverse-continuity claim.

The positive innovation also follows directly from finite Gaussian conditioning. For the action A_l, condition on its previous forward calls A_l V=Y and reverse calls A_l^T U=Q. The forward inputs V include the three h_i^(l-1); the reverse inputs U include the three beta_i^l. On adding t=t_j^(l-1), the unused Gaussian part of the action answer contains

    (||(I-P_V)t||_Euclidean/sqrt(n)) P_(U-perp) g_n,

where g_n is an independent standard Gaussian vector. The removed projection has expected normalized squared length rank(U)/n, which tends to zero for this fixed transcript. The residual input norm converges to the strictly positive variance in (B). If other finitely many new queries are included, their joint Gaussian covariance gives the same marginal regression on the original three sources; no assertion that a later query is independent of earlier added queries is needed. This confirms that reuse and transpose conditioning cannot erase the innovation proved in (C)--(D).

Actual adjunction is retained at every step. These are calls of the initialized canonical Gaussian actions and their adjoints, not arbitrary bounded operators substituted for the initialization.

#### 7. Physical acceleration and the exact kernel coefficient

Let a canonical strong physical solution with the strong chain rule be given. Since C(0)=0, its predictions vanish and r_i(0)=-y_i=-3p_i. The readout equation implies

    C'(0)=3H, C(t)/t -> 3H in H_L.

All initial hidden velocities vanish. Bounded multiplication by the gates, strong forward convergence, and operator-norm convergence of the HS action increments give, backward from the top,

    b_i^l(t)/t -> 3 beta_i^l in H_l.

For completeness, if D(t) are uniformly bounded multipliers converging in probability to D(0) and q(t)->q(0) in L2, then D(t)q(t)->D(0)q(0) in L2: split the difference into the multiplier acting on q(t)-q(0) and (D(t)-D(0))q(0), and use dominated convergence on the second. Apply this at each gate, and split each changed action into its fixed initial action and a vanishing operator-norm increment.

Dividing each raw hidden update by t now gives

    theta_h'(t)/t -> 9V,
    theta_h(t)=theta_h(0)+(9/2)t^2 V+o_raw(t^2).

The exact strong forward chain rule, applied successively to the L layers, gives

    (z_j^l)'(t)/t -> 9U_j^l,
    (h_j^l)'(t)/t -> 9D_j^l U_j^l.

Thus the strong right second derivatives at zero exist and are precisely the stated nonzero accelerations. No second Frechet derivative of the ambient L2 Nemytskii map is assumed.

Let J denote the bounded hidden directional linearization of H(theta_h)=sum_i p_i h_i^L at initialization. Genuine adjunction gives J^*H=V. The preceding chain rule gives

    H'(t)/t -> 9JV,
    H(t)=H+(9/2)t^2 JV+o_L2(t^2),
    ||H(t)||_2^2=||H||_2^2+9t^2||V||_hidden^2+o(t^2).

The hidden part g_h(t) of the raw gradient of sum_i p_i f_i satisfies g_h(t)/t->3V, so

    ||g_h(t)||_hidden^2=9t^2||V||_hidden^2+o(t^2).

Finally the exact raw kernel identity is

    p^T K_total(t)p=||g_h(t)||_hidden^2+||H(t)||_2^2.

Adding the two contributions proves the coefficient 18. Because every hidden block is nonzero, ||V||_hidden>0, and the projected total kernel strictly increases from its initial value at all sufficiently small positive physical times. This is the actual kernel along training, with no scalar-clock or permutation argument.

## I. Moderate sine: exact identities, local limits and continuation partials

Fix the two-sample, three-hidden-layer model E.2 with the sine activation specified below, half-sum loss, actual Gaussian finite readout of variance n^-2 and raw GD step n^-2. The coefficient 2/5 is fixed; it is not replaced by a perturbative coefficient. I.1–I.4 are unconditional within their displayed scopes. The endpoint result assumes an already existing strong population path; it does not construct a restart. I.5's global strong population theorem assumes its explicit cap-uniform exponential-tail condition. That condition remains open for the prescribed initialized sine dynamics. Its ambient examples concern arbitrary bounded raw states, not states shown to be reached by training.

### I.1. Relative nonlinearity and a moderate calibrated activation

Within this proof unit, unqualified section and equation numbers are local.

#### 1. A distribution-independent measure

For any scalar random variable Z with 0<Var(Z)<infinity and any activation
phi with finite positive variance, define

    N_phi(Z) = inf_(b,c) E[(phi(Z)-b-cZ)^2] / Var(phi(Z)).

This fraction is invariant under a nonzero affine change of the output
phi. It measures the feature variance left after its best affine fit.

Suppose phi(z)=az+e psi(z), a>e L>=0, and psi is L-Lipschitz.
Then, for every such Z,

    0 <= N_phi(Z) <= (e L/(a-e L))^2.                 (1)

Proof. For independent copies Z,Z',

    Var(psi(Z)) = E[(psi(Z)-psi(Z'))^2]/2
                 <= L^2 Var(Z).

Also phi is increasing with secant slope at least a-e L, so

    Var(phi(Z)) = E[(phi(Z)-phi(Z'))^2]/2
                  >= (a-e L)^2 Var(Z).

Absorbing az into the best affine fit gives the exact numerator
e^2 inf_(b,c) E[(psi(Z)-b-cZ)^2], at most e^2 Var(psi(Z)).
Dividing proves (1). No Gaussian hypothesis is used.

Thus a theorem with a microscopic e/a controls a class that is
quantitatively close to affine on every input law. Allowing e=1 while
making a very large does not resolve this issue. This observation is
compatible with nonzero feature motion: even a deep affine network can
learn features and change its kernel.

#### 2. An explicit moderate nonlinear candidate

Let G be standard Gaussian, fix omega>0, and set

    b_omega = omega exp(-omega^2/2),
    r_omega(z) = sin(omega z)-b_omega z,
    v_omega = (1-exp(-2 omega^2))/2
                          -omega^2 exp(-omega^2).

The Gaussian characteristic function gives

    E[G sin(omega G)] = b_omega,
    E[sin(omega G)^2] = (1-exp(-2 omega^2))/2.

For completeness the characteristic function follows by differentiating
I(t)=E exp(itG), applying integration by parts to get I'(t)=-tI(t),
and using I(0)=1. Differentiation is dominated by |G|. Taking real
parts and differentiating at omega gives both displayed moments.

Consequently E r_omega(G)=E[G r_omega(G)]=0 and
E r_omega(G)^2=v_omega>0. Positivity follows because sine is not an
affine function on the full Gaussian support.

For b>0 define the single activation

    Phi_(b,omega)(z) = [z+b r_omega(z)]/sqrt(1+b^2 v_omega).

It has exactly unit initialized Gaussian second moment, and

    N_Phi(G) = b^2 v_omega/(1+b^2 v_omega).          (2)

The derivative is bounded below by

    [1-b omega(1+exp(-omega^2/2))]/sqrt(1+b^2 v_omega).

Thus strict monotonicity holds when b omega(1+exp(-omega^2/2))<1.
For example omega=2 and b=2/5 satisfy this inequality, since
exp(-2)<1/4. They give approximately 6.4 percent nonlinear variance
at initialized unit Gaussian input, with coefficients of moderate size.
Equation (2), not a numerical training experiment, gives this value.

Because its unit Gaussian second moment is exactly one, the initialized
Gaussian variance remains one through every hidden layer. The same
nonlinear fraction therefore holds in all three initialized layers.
The companion Fragment I.2 derives the exact correlation map
and its strict contraction toward zero.

This is an affine function plus a bounded smooth sine perturbation,
so its shape is eligible for a perturbative activation-class theorem
after normalizing derivative bounds. The moderate value b=2/5 is NOT
certified by that theorem's smallness condition. Proving the global
trained result for a fixed candidate of this size remains a distinct
research obligation.

### I.2. Exact sine initialization at every layer

Within this proof unit, unqualified section and equation numbers are local.

This is an initialization lemma only, for the original independent Gaussian middle matrices. It does not assert a trained-flow theorem.

Use the activation and notation in Fragment I.1:

\[
 r(z)=\sin(\omega z)-\omega e^{-\omega^2/2}z,
\quad v=\mathbb E r(G)^2,
\quad \Phi(z)=\frac{z+b r(z)}{\sqrt{1+b^2v}}.
\]

Let `(G_1,G_2)` be standard Gaussians of correlation c in [-1,1], and put a=omega^2. The identity `sin u sin v=[cos(u-v)-cos(u+v)]/2` and the Gaussian characteristic function give

\[
\mathbb E[\sin(\omega G_1)\sin(\omega G_2)]
=e^{-a}\sinh(ac).
\]

Gaussian regression gives `E[G1 sin(omega G2)]=c omega exp(-a/2)`; at singular endpoints this follows directly from `G2=+/-G1`. Therefore

\[
R(c):=\mathbb E[r(G_1)r(G_2)]
=e^{-a}[\sinh(ac)-ac],\qquad v=R(1)>0.               \tag{1}
\]

The cross terms between the linear part and r vanish for every c, so the exact correlation update is

\[
F(c)=\mathbb E[\Phi(G_1)\Phi(G_2)]
=\frac{c+b^2R(c)}{1+b^2v}.                           \tag{2}
\]

This also proves `E Phi(G)^2=1`, so each subsequent initialized Gaussian preactivation has variance one. Hence all initialized marginal activation nonlinear fractions equal `b^2v/(1+b^2v)`, at all three hidden layers.

For 0<c<1, the absolutely convergent power series yields

\[
\frac{R(c)}c=e^{-a}\sum_{k\ge1}
               \frac{a^{2k+1}c^{2k}}{(2k+1)!}
<e^{-a}\sum_{k\ge1}\frac{a^{2k+1}}{(2k+1)!}=v.
\]

All terms are positive and `b>0`, so `0<F(c)<c`. Oddness gives `|F(c)|<|c|` for -1<c<0 as well; F(0)=0 and F(+/-1)=+/-1.

For the original initial pair with correlation rho, the top feature Gram is therefore

\[
K^4_0=\begin{pmatrix}1&F^{\circ3}(\rho)\\F^{\circ3}(\rho)&1\end{pmatrix},
\qquad
\lambda_{\min}(K^4_0)=1-|F^{\circ3}(\rho)|
\ge1-|\rho|.                                         \tag{3}
\]

For either binary label pair, the projected initial kernel satisfies

\[
\kappa_0=\frac14y^TK^4_0y
=\frac12[1+y_1y_2F^{\circ3}(\rho)]
\ge\frac12(1-|\rho|)\ge\delta/2.                    \tag{4}
\]

At population initialization the other raw kernel blocks vanish because C0=0. The usual fixed-depth Gaussian initialization induction suffices to identify these initialized laws: condition on the preceding feature matrix, use independence of the next centered Gaussian matrix, and pass its covariance entries by the law of large numbers at each of the fixed three layers. No growing-time transcript or trained Gaussianity is assumed.

For omega=2, b=2/5, this supplies one strictly increasing, moderately nonlinear activation, with the same approximately 6.4% nonlinear variance at every initialized layer and initial separation no worse than the input separation. The lemma does not prove that the trained preactivations stay Gaussian, that the initialized variance persists, or that the nonlinear fraction remains positive during training.

### I.3. Direct local source construction at fixed moderate sine amplitude

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Exact activation and auxiliary caps

Write

\[
 s_0=\sqrt{1+4v/25},\qquad
 \alpha=(1-4e^{-2}/5)/s_0,\qquad \beta=2/(5s_0),
 \qquad \Phi(z)=\alpha z+\beta\sin(2z).
\]

Here `v=(1-e^{-8})/2-4e^{-4}>0`. Since `e^{-2}<1/4`,

\[
 \alpha-2\beta=(1-4e^{-2}/5-4/5)/s_0>0.
\]

Thus Phi is a strictly increasing smooth bijection. The estimates

\[
 \Phi(0)=0,\quad |\Phi(z)|\le2|z|,\quad
 |\Phi'(z)|\le2,\quad |\Phi''(z)|\le2                 \tag{1}
\]

are sufficient below. The actual nonlinear coefficient beta is retained.

Use an auxiliary smooth odd contraction tau_R, with `|tau_R(q)|<=|q|`, `|tau_R'|<=1`, equal to q on `[-R,R]`, and bounded by `2R`. The backward gate is

\[
 D_R(z,q)=\alpha q+2\beta\cos(2z)\tau_R(q).             \tag{2}
\]

It obeys `|D_R(z,q)|<=2|q|`, `|partial_q D_R|<=2`, and
`|partial_z D_R|<=2|q|`. For every fixed R its derivatives are bounded. This is the original gate when R is removed; it does not cap the affine part or reset the readout.

Work first in feature time, with `c=(y_1/2,y_2/2)` and `P=Gamma diag(c)`, so `|P|<=1`, `sum|c_a|=1`. At finite width use the actual prescribed finite readout. Its population initial limit is zero; this replacement is made only after fixed-program convergence, not in the finite algorithms.

#### 2. A cap-independent small primal interval

Let B=20, L=2 and N=2. The initial operator norms are at most 10 with probability tending to one, and the two first preactivation norms are at most 2. The initial readout norm tends to zero. On a primal ball with each first preactivation norm, both operator norms and the readout norm at most B, direct forward and backward induction gives, for each sample,

\[
 \|h^1\|_2\le LB,\quad \|h^2\|_2\le L^2B^2,
 \quad \|h^3\|_2\le L^3B^3,
\]
\[
 \|\delta^3\|_2\le L\|C\|_2,
 \quad \|q^2\|_2\le LB\|C\|_2,
 \quad \|\delta^2\|_2\le L^2B\|C\|_2,
 \quad \|q^1\|_2\le L^2B^2\|C\|_2.
                                                               \tag{3}
\]

Every one of the four parameter update norms is at most `L^3 B^3`; the first projected fields acquire at most this size per sample because `|P|<=1`. Consequently a sufficiently short interval, for example

\[
 S\le (100L^3B^3)^{-1},                                  \tag{4}
\]

stays inside that primal ball, for every fixed cap and sufficiently fine mesh. This follows directly by summing Euler increments up to the first exit; no nonlinear Lipschitz constant is used. The same estimate holds for the fixed-cap strong flow. In the population,

\[
 \|C(t)\|_2\le L^3B^3S.                                  \tag{5}
\]

The covariance rules for the four Gaussian groups now show that there is one explicit constant

\[
 D=2^{10}B^5                                             \tag{6}
\]

such that the Lp norm of each forward Gaussian source pair and the first root pair is at most `D sqrt(p)`, and the Lp norm of each backward Gaussian source pair is at most `D S sqrt(p)`, for every p>=2. Correlations and singular covariance matrices are retained. Indeed, each scalar Gaussian Lp norm is at most twice its standard deviation times sqrt(p); sum over two samples and use (3)--(5). D also bounds every forward primal L2 norm, and `D S` bounds every backward primal L2 norm used in learned moments. These are actual finite-program source variances, obtained from the bounded primal calculation, not assumed coordinate tails.

#### 3. Direct source estimate at fixed moderate amplitude

Set

\[
 A_2=M_3=100D^2,\qquad A_3=M_2=100D^2 A_2,\qquad A=A_3.
                                                               \tag{7}
\]

Consider the exact source programs on `[0,S]`, with arbitrary sufficiently fine positive mesh. A forward coefficient bound means

\[
 |a^2_{kj}|\le A_2h_j,\quad |a^3_{kj}|\le A_3h_j\quad(j<k),
                                                               \tag{8}
\]

and a backward bound means

\[
 \sum_{j\le k}|b^3_{kj}|\le M_3 S,\qquad
 \sum_{j\le k}|b^2_{kj}|\le M_2 S.                    \tag{9}
\]

Here each block uses maximum absolute sample row sum, and the time row uses the sum of these block norms. In particular, the current block is included.

It suffices to take

\[
 S\le S_0:=\min\left\{1,(100L^3B^3)^{-1},
 (4L^6B^6)^{-1},(10000 D A^2)^{-1/2}\right\}.          \tag{10}
\]

All constants are fixed numbers for the actual moderate activation. No separation-dependent reduction of beta is made.

### 3.1 Moments on a bounded coefficient prefix

Let `U_l=max_{k in prefix} ||Z^l_k||_p/sqrt(p)`. From the exact source equations, (1), (8), (9) and the covariance bounds,

\[
 U_1\le D+LD S^2+L^2M_2 S\sum_r h_r U_{1,r},
\]
\[
 U_2\le D+A_2LD S^2+A_2L^2M_3 S\sum_r h_rU_{2,r},
\]
\[
 U_3\le D+A_3L^2S\sum_rh_rU_{3,r}.
\]

The same inequalities apply to deterministic prefix maxima. Iterating the positive Volterra majorant, with (10), gives

\[
 \max_{l,k}\|Z^l_k\|_p\le10D\sqrt p.                  \tag{11}
\]

For example, the middle bound is
`(D+A_2LD S^2) exp(A_2L^2M_3 S^2) sqrt(p)`, which is less than `10D sqrt(p)` under (10). No supremum over Gaussian times is taken.

The current input equations and the integrated readout then give

\[
 \|C_k\|_p\le20D S\sqrt p,
\]
\[
 \|q^2_k\|_p\le21D M_3 S\sqrt p,
 \qquad \|q^1_k\|_p\le21D M_2 S\sqrt p.               \tag{12}
\]

These estimates only use rows already needed to construct the current field; they may therefore be applied in the causal four-stage order below.

### 3.2 Formal derivative bounds with the current multiplier retained

Let `G=Phi'(Z)`, `V=partial_q D_R(Z,Q)`, and `L_curv=partial_z D_R(Z,Q)`. Then

\[
 |G|,|V|\le2,\qquad |L_{\rm curv}|\le2|Q|.             \tag{13}
\]

The exact derivative recursions cited above imply the following bounds. A bottom transpose-source preactivation derivative is at most

\[
 Lh_j\,\mathcal E_k;
\]

a middle transpose-source preactivation derivative is at most

\[
 A_2Lh_j\,\mathcal E_k;
\]

a complete middle or top forward-source preactivation derivative row is at most `mathcal E_k`. The top readout derivative row is at most `L S mathcal E_k`. One common majorant, in the appropriate population, is

\[
 \mathcal E_k=\exp\left\{8A^2S^2+
             2A\sum_{r<k}h_r |Q_r|_\infty\right\}.     \tag{14}
\]

For the top use Q=C; for the middle and bottom use their respective incoming fields. These inequalities follow by substituting (8)--(9) into the exact recursions and iterating
`x_k<=f+sum_{r<k}h_r lambda_r max_{v<=r}x_v`.
The strict source-time factor h_j is retained because the single-source forcing enters once at step j; there is no forcing at unavailable source times.

For clarity, (12) is already a pair-maximum bound, so no extra sample factor is needed in (14). A random variable with `||Q||_p<=K sqrt(p)` satisfies
`E exp(Q^2/(4 e K^2))<=2` by expanding its exponential. Hence
`E exp(uQ)<=2 exp(e K^2u^2)` for u>=0. Jensen with weights h_r/S proves

\[
 E\mathcal E_k^4
 \le2\exp\{32A^2S^2+e(168DA^2S^2)^2\}<16,
                                                               \tag{15}
\]

where (12), `M_2=A`, and (10) were used. Thus `||mathcal E_k||_4<2`, uniformly in cap, mesh and source covariance degeneracy.

The middle backward-output derivative row contains the current term

\[
 L_{{\rm curv},k}J_k,
\]

and the top row contains the corresponding `L_curv,k J_k+V_k 1 T_k`. They cannot be discarded. Cauchy--Schwarz, (12), and (15) give

\[
 E\sum_j|\partial_{\xi^3_j}\delta^3_k|
 \le 2N\|C_k\|_2+2L^2S
 \le (40\sqrt2 ND+2L^2)S,                            \tag{16}
\]

and, once the current b3 row is available,

\[
 E\sum_j|\partial_{\xi^2_j}\delta^2_k|
 \le2N\|q^2_k\|_2+2L^2M_3S
 \le(42\sqrt2 ND M_3+2L^2M_3)S.                     \tag{17}
\]

The complete current blocks are therefore controlled as well. Their actual formulas are

\[
 b^3_{ka,kb}=\mathbf1_{a=b}E[L^3_{{\rm curv},k,a}],
\]
\[
 b^2_{ka,kb}=\mathbf1_{a=b}E[L^2_{{\rm curv},k,a}]
       +b^3_{ka,kb}E[V^2_{k,a}G^2_{k,b}].             \tag{18}
\]

These are computed causally, without an implicit current-time inverse.

### 3.3 Literal closure in the four-stage order

The learned forward density is at most D^2, and a complete learned backward row is at most `D^2 S^3`, by the raw L2 bounds in Section 2 and `sum|c_a|=1`.

At each time k:

1. The bottom transpose response, including its feature derivative, is at most `2L^2 h_j` in expectation. Hence
   `|a2_kj|/h_j<=2L^2+D^2<A_2/2`.
   Only strictly past b2 rows are needed.
2. The middle transpose response is at most `2A_2L^2 h_j` in expectation. Hence
   `|a3_kj|/h_j<=2A_2L^2+D^2<A_3/2`.
   This uses the just bounded current a2 row and past b3 rows.
3. Equations (16) and the learned moment estimate give
   `|b3_k|_row< M_3 S/2`.
   This uses available current a3 but no current backward row. It then constructs q2_k and supplies (12) for that field.
4. Equation (17) plus its learned moment gives
   `|b2_k|_row< M_2 S/2`.
   The available current b3 row is retained. It then constructs q1_k.

All strict inequalities follow from D>=100, the choices (7), N=L=2, and S<=1. At time zero the forward rows are empty, C0=0 and both backward rows vanish. This supplies an induction through every time and every stage. Consequently (8)--(12) hold for the full programs on `[0,S_0]`, uniformly in R and fine mesh.

This is a genuine moderate-amplitude local source estimate. It is not the reference affine perturbation argument with a hidden beta restriction.

#### 4. Local uncut consequences and their scope

From (12), all three incoming-field tail norms have Gaussian decay, uniformly in cap and mesh. For (2), the reference-only asymmetric gate estimate is

\[
 |D_{R'}(z_A,q_A)-D_R(z_B,q_B)|
 \le L|q_A-q_B|+C R|z_A-z_B|
       +C|q_B|\mathbf1_{|q_B|>R},                    \tag{19}
\]

for R'>=R, including R'=infinity. The forward field is Lipschitz with linear growth. On the primal ball, propagation and rank-one update estimates therefore give the same cap comparison cost `C exp(CR-cR^2)` as the cited bridge. Thus a unique strong uncut feature flow exists on `[0,S_0]`, with restart uniqueness inside that already constructed interval, on the common Gaussian action spaces. The exact fixed-cap GF/GD and observable bridges apply to this activation because their hypotheses are precisely linear growth, bounded first two derivatives, and the established reference tails.

The third restriction in (10) gives `|g_R(s)|<=L^6B^6S<=1/4`, directly from (3),(5). Hence the symmetric physical clock has speed `ds/dt=2(1-g_R)` between 3/2 and 5/2 while this interval is used. In particular the physical interval `[0,S_0/3]` is covered. Both actual finite residuals remain in the finite physical comparison, as in the cited bridge. The local theorem includes the finite readout, reused matrices and the named joint GF/GD observables.

Nothing in this argument bounds source coefficients for all S or all physical T. The small S in (10) is a local construction interval, not an activation choice; selecting it does not prove the stated global result.

#### 5. Exact sine averaging at the current return

There is a precise reason why Gaussian sine cancellation at initialization does not automatically control the trained source response.

At top source time k, let F_{k-1} be the sigma field of the strictly past top Gaussian source coordinates. All deterministic coefficient arrays are fixed. The readout C_k and the learned part of Z3_k are measurable with respect to this field. Gaussian regression gives, for each sample a,

\[
 Z^3_{k,a}=\mu_{k,a}+\eta_{k,a},
\]

where mu is past-measurable and eta is independent of the past, centered Gaussian, with deterministic variance sigma_{k,a}^2; this includes sigma=0. Since `Phi''=-4 beta sin(2z)`, the exact uncut conditional return is

\[
 E[\Phi''(Z^3_{k,a})C_k\mid F_{k-1}]
 =-4\beta e^{-2\sigma_{k,a}^2}C_k\sin(2\mu_{k,a}).     \tag{20}
\]

For the capped program replace C_k by tau_R(C_k) in (20). Both signs are possible in this expression as a function of its adapted mean and readout; sine periodicity alone supplies neither zero mean nor a negative sign. This observation is not an assertion that arbitrary adapted means and readouts are attainable by the neural flow.

Moreover,

\[
 \sigma_{k,a}^2
 \le E[(\xi^3_{k,a}-\xi^3_{k-1,a})^2]
 =E[(H^2_{k,a}-H^2_{k-1,a})^2].                       \tag{21}
\]

The first inequality uses the previous source itself as a candidate Gaussian linear predictor; the equality is the exact source covariance rule. On any raw bounded Euler prefix, the last quantity is at most `C_B^2 h_{k-1}^2`: the four update sizes are bounded independently of R by (3), and two forward Lipschitz propagations bound a one-step feature difference by `C_B h`. Therefore the damping factor in (20) is at least

\[
 e^{-2C_B^2 h_{k-1}^2},                               \tag{22}
\]

which approaches one as the mesh is refined. The current innovation is not a fresh variance-one Gaussian at every training instant. Applying the initialization factor e^{-2} at all trained times would be incorrect.

The identity `Phi''=-4(Phi-alpha z)` also does not remove the current multiplier: it rewrites it as `-4(Phi(Z)-alpha Z)Q`, whose second factor is still unbounded. Strict monotonicity does permit a scalar one-control coordinate cancellation. For correlated two-input control the exact Lie bracket obstruction in Fragment J.1, Section 3, prevents simultaneous straightening of the two vector fields unless the activation is affine.

#### 6. What continuation would require

The local proof gains its small quantities from `C0=0`, backward source variances O(S^2), and backward rows O(S). At a reached positive time, these quantities are nonzero. The existing Gaussian source history must be retained. Restarting the local proof with a fresh independent Gaussian initialization would change the model.

A sufficient global source program would establish, for each finite physical T and a raw stopping radius B, cap- and mesh-independent finite bounds on the actual forward response densities and complete backward response rows (or directly strong enough incoming-field tails). Constants may depend arbitrarily on T,B and this fixed activation. Under such a bound, the moment and derivative estimates above remain valid with finite constants, and the reference-only cap comparison removes the cap. Approximate energy can then remove the raw stop. This last source bound is not proved by the local bootstrap.

A plausible but unproved continuation criterion is that all existing source response row bounds, their moment envelopes and the needed history moduli stay finite at every finite reached time. A rigorous endpoint extension would have to retain the entire causal history and control new responses against every reference source column. Bounded primal energy does not supply these quantities, and this proof unit does not claim a generic reached-state local existence theorem from an arbitrary L2 endpoint.

The present mathematical progress is therefore: a direct moderate-sine local population construction and exact obstruction to automatic trained Gaussian phase averaging. The stated strong global joint population/GF/GD limit remains open in this route.

### I.4. Finite algorithms and strong finite-time population endpoints

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Candidate and elementary constants

Put

\[
 v=(1-e^{-8})/2-4e^{-4},\qquad N=\sqrt{1+4v/25},
\qquad \Phi(z)=az+b\sin(2z),
\]
\[
 a=(1-4e^{-2}/5)/N,\qquad b=2/(5N).
\]

Here `v>0`, since it is the variance of the nonzero Gaussian-orthogonal residual `sin(2G)-2e^{-2}G`. In particular `N>1`. The exact derivatives are

\[
 \Phi'(z)=a+2b\cos(2z),\qquad
 \Phi''(z)=-4b\sin(2z).
\]

Since `e^2>4`,

\[
 0<m:=(1/5-4e^{-2}/5)/N\le\Phi'(z)<2,
 \qquad |\Phi''(z)|<2,
 \qquad \Phi(0)=0,\quad |\Phi(z)|\le2|z|.       \tag{1}
\]

No small coefficient or condition on the observation horizon is used in (1). The lemmas below in fact apply to any C2 activation with `phi(0)=0`, `||phi'||_infinity<=2` and `||phi''||_infinity<=2`; the lower slope is not needed for them. They hold for any input correlation in `[-1,1]`, so in particular for the separated inputs.

#### 2. Raw norm and estimates on a primal ball

At finite width use the exact raw norm from the stated model. A normalized vector has norm `(||u||_Euclidean/sqrt(n))=||u||_Euclidean/sqrt(n)`. Suppose

\[
 \max_i\frac{\|z_i^1\|_2}{\sqrt n},\quad \|W^2\|_{op},\quad
 \|W^3\|_{op},\quad\frac{\|C\|_2}{\sqrt n}\le B,\qquad B\ge1.      \tag{2}
\]

The following bounds follow successively from (1):

| Field | Norm bound |
|---|---:|
| `h^1` | `2B` |
| `z^2,h^2` | `2B^2,4B^2` |
| `z^3,h^3` | `4B^3,8B^3` |
| `delta^3,q^2` | `2B,2B^2` |
| `delta^2,q^1,delta^1` | `4B^2,4B^3,8B^3` |

The sample maximum is implicit in this table. Since the labels have modulus one,

\[
 \sum_i|r_i|\le16B^4+2\le18B^4.                  \tag{3}
\]

Let `V=-grad_raw L` be the actual physical vector field. Each of its four parameter blocks has raw norm at most `144B^7`, and hence

\[
 \|V\|_{raw}\le576B^7.                           \tag{4}
\]

For a middle block this uses

\[
 \|u\otimes h\|_F=\frac{\|u\|_2}{\sqrt n}\frac{\|h\|_2}{\sqrt n}.
\]

For the first block,

\[
 \sqrt{d/n}\,\|d^{-1}u x_i^T\|_F=\frac{\|u\|_2}{\sqrt n}
\]

because `||x_i||^2=d`. Thus no dimension or width factor enters (4). The same argument applies to population fields, with Hilbert--Schmidt norms of the learned increments.

#### 3. A dimension-explicit raw Lipschitz estimate

At width n, let two states both satisfy (2), and let `d_0` be their raw distance. Forward differences satisfy

\[
 \frac{\|\Delta z^1\|_2}{\sqrt n}\le d_0,\quad
 \frac{\|\Delta h^1\|_2}{\sqrt n}\le2d_0,\quad
 \frac{\|\Delta z^2\|_2}{\sqrt n}\le4Bd_0,\quad
 \frac{\|\Delta h^2\|_2}{\sqrt n}\le8Bd_0,
\]
\[
 \frac{\|\Delta z^3\|_2}{\sqrt n}\le12B^2d_0,\quad
 \frac{\|\Delta h^3\|_2}{\sqrt n}\le24B^2d_0,\quad
 \sum_i|\Delta r_i|\le64B^3d_0.                    \tag{5}
\]

For example,

`Delta z^2=W^2 Delta h^1+Delta W^2 h_tilde^1`,

and `||Delta W^2||op<=||Delta W^2||F<=d_0`. The last inequality in (5) uses

`|Delta f_i| <= (||Delta C||_Euclidean/sqrt(n)) (||h_i^3||_Euclidean/sqrt(n)) + (||C_tilde||_Euclidean/sqrt(n)) (||Delta h_i^3||_Euclidean/sqrt(n)) <=32B^3 d_0`.

For the backward gates, use

\[
 \frac{\|\Phi'(z)q-\Phi'(\widetilde z)\widetilde q\|_2}{\sqrt n}
 \le2\frac{\|q-\widetilde q\|_2}{\sqrt n}
       +2\|\widetilde q\|_\infty\frac{\|z-\widetilde z\|_2}{\sqrt n},
 \quad \|u\|_\infty\le\sqrt n\frac{\|u\|_2}{\sqrt n}.
\]

Substitution of (5) and the field bounds gives, in causal order,

\[
 \frac{\|\Delta\delta^3\|_2}{\sqrt n}\le26\sqrt n B^3d_0,\quad
 \frac{\|\Delta q^2\|_2}{\sqrt n}\le28\sqrt n B^4d_0,\quad
 \frac{\|\Delta\delta^2\|_2}{\sqrt n}\le72\sqrt n B^4d_0,
\]
\[
 \frac{\|\Delta q^1\|_2}{\sqrt n}\le76\sqrt n B^5d_0,\quad
 \frac{\|\Delta\delta^1\|_2}{\sqrt n}\le160\sqrt n B^5d_0.         \tag{6}
\]

For instance the middle gate difference is at most

`2(28 sqrt(n) B^4)d_0 + 2(sqrt(n) 2B^2)(4B)d_0 <=72 sqrt(n) B^4 d_0`.

Expanding each rank-one update and its residual then gives respective raw block Lipschitz bounds

\[
 3392\sqrt n B^9,\quad3248\sqrt n B^9,\quad
 2672\sqrt n B^9,\quad944\sqrt n B^9.
\]

Their sum is 10256. Consequently the conservative bound

\[
 \|V(\Theta)-V(\widetilde\Theta)\|_{raw}
 \le11000\sqrt n B^9\|\Theta-\widetilde\Theta\|_{raw}        \tag{7}
\]

holds whenever the two states satisfy (2). The primal set (2) is convex in the raw parameters, so the same bound controls the entire segment joining them. This is a finite-width estimate; its `sqrt(n)` factor is not dropped in a population argument.

#### 4. Unconditional finite-time raw-GD energy

Fix an observation horizon T and an initialization with primal bounds at most `b_0>=1` and loss `E_0`. Put

\[
 R=\sqrt{2(T+1)E_0}+2,\qquad B=b_0+R+1,
 \qquad h=n^{-2}.
\]

Assume n is sufficiently large that

\[
 11000B^9n^{-3/2}\le1,\qquad576B^7n^{-2}\le1.      \tag{8}
\]

Then the actual simultaneous raw GD iterates through time T, and one additional endpoint if necessary, satisfy

\[
 \mathcal L(\Theta_k)\le E_0,\qquad
 \sum_{j<k}h\|V(\Theta_j)\|_{raw}^2\le2E_0,
\]
\[
 \|\Theta_k-\Theta_0\|_{raw}
 \le\sqrt{2khE_0}\le\sqrt{2(T+1)E_0}.             \tag{9}
\]

Proof. Stop provisionally before raw distance R from initialization. A raw displacement of size R changes either initial operator norm, the readout norm, or a first-layer sample norm by at most R, so (2) holds with room to spare. The second inequality in (8) and (4) keep the next Euler segment inside the larger primal ball B. Taylor's formula for the scalar loss and (7) give

\[
 \mathcal L(\Theta+hV)\le\mathcal L(\Theta)
      -h\|V\|_{raw}^2+	frac12(11000\sqrt n B^9)h^2\|V\|_{raw}^2
 \le\mathcal L(\Theta)-\tfrac12h\|V\|_{raw}^2.
\]

Summing proves the first two claims in (9). Cauchy--Schwarz for the sum of raw increments proves the third, which is strictly below R. This closes the induction and removes the stop. No population flow, tail bound, convergence theorem, or fixed-width comparison with continuous GF was assumed.

Under the prescribed random initialization, one may take `b_0=10`, `E_0<=2` on events with probability tending to one. Initial first-layer sample norms converge to one, the initial Gaussian action norms are bounded with probability tending to one, the readout norm tends to zero, and the two predictions tend to zero. Thus (8)-(9) give bounds uniform in width on events with probability tending to one for every fixed T.

This proves stable finite-horizon raw GD at the prescribed step; it does not identify its strong population limit.

#### 5. Finite GF and weak path-law tightness

At every fixed width the finite-dimensional smooth vector field is locally Lipschitz. Its true gradient-flow energy identity is

\[
 \mathcal L(t)+\int_0^t\|\dot\Theta(s)\|_{raw}^2ds=E_0,
 \quad
 \|\Theta(t)-\Theta(0)\|_{raw}\le\sqrt{tE_0}.       \tag{10}
\]

It therefore cannot escape in finite time and is global. This is finite-dimensional existence only.

On any primal ball B, for a differentiable raw path write `s(t)=||dot Theta(t)||raw`. Successive forward differentiation gives

\[
 \frac{\|\dot z^1\|_2}{\sqrt n}\le s,\quad\frac{\|\dot h^1\|_2}{\sqrt n}\le2s,
 \quad\frac{\|\dot z^2\|_2}{\sqrt n}\le4Bs,\quad\frac{\|\dot h^2\|_2}{\sqrt n}\le8Bs,
\]
\[
 \frac{\|\dot z^3\|_2}{\sqrt n}\le12B^2s,\qquad
 \frac{\|\dot h^3\|_2}{\sqrt n}\le24B^2s.                        \tag{11}
\]

These inequalities hold almost everywhere also for linearly interpolated raw GD, with hidden fields recomputed from the interpolated parameters in the stated raw model. Equations (9)-(11), together with initialized second-moment bounds, uniformly bound the average squared H1([0,T]) norm of the joint four-coordinate same-layer paths `(z_1,h_1,z_2,h_2)`.

Closed bounded H1 balls on a finite one-dimensional time interval have compact images in C([0,T]); this follows directly from the pointwise bound and the modulus `|x(t)-x(s)|<=sqrt(|t-s|)||x'||_L2`, followed by the Arzela--Ascoli theorem. Markov's inequality for the empirical average H1 norm therefore gives tightness of the empirical path laws in the weak topology on probability measures on C([0,T];R4), on the above high-probability events.

This is not W2 compactness: a bounded mean squared H1 norm does not by itself make squared path norms uniformly integrable. It does not identify a deterministic subsequential law, kernels, adjoints, or velocity laws.

#### 6. Strong endpoint reduction for the population problem

Fix the canonical generated action spaces and initial bounded actions `A_0,B_0`. Work in the complete raw affine Hilbert state space

\[
 \mathfrak X=(\hbox{first-layer L2 field})\times
 HS(\mathcal H_1,\mathcal H_2)\times
 HS(\mathcal H_2,\mathcal H_3)\times\mathcal H_3,
\]

with actions `A=A_0+Delta A`, `B=B_0+Delta B`. The first factor may equivalently retain the full normalized first-layer weight field; unused directions are fixed. HS convergence implies operator-norm convergence.

**Continuity lemma.** For the candidate Phi, the complete forward/backward calculation and the true raw gradient are continuous on this raw state space. On a bounded raw set they have finite L2 or HS norms bounded by a polynomial in the primal bounds.

Proof. Forward continuity follows from the global Lipschitz property of Phi and bounded-action continuity. For the only less immediate map, if `(z_j,q_j)->(z,q)` in L2 x L2, then

\[
 \|\Phi'(z_j)q_j-\Phi'(z)q\|_2
 \le2\|q_j-q\|_2+\|[\Phi'(z_j)-\Phi'(z)]q\|_2\to0.   \tag{12}
\]

The last term tends to zero because `z_j->z` in measure, Phi' is continuous, and its square times `q^2` is bounded by `16q^2`, an integrable function. A subsequence argument or dominated convergence after almost-everywhere subsubsequence convergence gives the conclusion for the full sequence. Apply (12) in backward causal order; rank-one products are continuous from L2 x L2 to HS. This proves the lemma.

The scalar prediction is continuously Frechet differentiable in the raw state with the usual backpropagated gradient. To check the potential issue from Nemytskii nonlinearities, for any fixed `q in L2` use

\[
 |\Phi(z+u)-\Phi(z)-\Phi'(z)u|
 \le\min\{|u|^2,4|u|\}.
\]

Pair with q and split at `|q|>K`. The quadratic remainder on `|q|<=K` is at most `K||u||_2^2`; the Lipschitz remainder on the q-tail is at most `4||q 1_{|q|>K}||_2 ||u||_2`. Divide by `||u||_2`, let `||u||_2->0` at fixed K, then let K tend to infinity. Telescoping the three layers gives the stated scalar Frechet derivative. Its continuity is (12).

**Strong endpoint lemma.** Suppose a strong physical population solution has been constructed on `[0,T_*)`, with `T_*<infinity`. Then there exist a raw state `Theta_* in X` and a raw velocity `V_*` such that

\[
 \Theta(t)\to\Theta_*\quad\hbox{in the full raw Hilbert norm},
 \qquad V(\Theta(t))\to V_*=V(\Theta_*)
           \quad\hbox{in the raw norm},            \tag{13}
\]

as `t->T_*`. Every forward field, incoming backward field, gate output, and actual action/adjoint on a converging L2 probe has a corresponding strong limit.

Proof. The true energy identity gives, for `0<=s<t<T_*`,

\[
 \|\Theta(t)-\Theta(s)\|_{raw}
 \le\sqrt{(t-s)\int_s^t\|\dot\Theta(u)\|_{raw}^2du}
 =\sqrt{(t-s)[\mathcal L(s)-\mathcal L(t)]}.        \tag{14}
\]

Since the loss is nonnegative and decreasing, (14) makes the state Cauchy at the finite endpoint. Completeness produces Theta_*. The continuity lemma gives all the other claims. In fact the path extended by Theta_* is differentiable from the left at T_* with derivative V_*: integrate the converging velocities and divide by the time increment.

For every one of the finitely many incoming-field paths `q(t)` so extended, the image of `[0,T_*]` is a compact subset of L2. It follows that

\[
 \lim_{R\to\infty}\sup_{0\le t\le T_*}
 \|q(t)1_{|q(t)|>R}\|_2=0.                        \tag{15}
\]

For completeness, cover the compact image by finitely many L2 balls of radius eta. If `||q-f||_2<=eta`, split the q-tail according to `|f|>R/2`; on the remaining part `|q|<=2|q-f|`. This bounds the q-tail by `2eta+2||f 1_{|f|>R/2}||_2`. The finitely many reference tails vanish, followed by eta. Thus (15) is qualitative uniform integrability; no exponential tail rate is inferred.

The endpoint lemma rules out raw-state divergence and divergence of the raw velocity as a mechanism of failure of a finite-time strong extension. It does not supply local existence at Theta_*: continuity of a vector field on an infinite-dimensional Hilbert space is not an ODE existence or uniqueness theorem. The current source construction additionally needs a quantitative response/tail certificate, and (15) does not provide one. It must also retain all Gaussian histories when restarted; resetting C or the reverse-field sources would change the model.

#### 7. Why positive bounded slope does not make the missing step routine

Even for this strictly increasing analytic Phi and Gaussian variables, the backward multiplication map is not locally Lipschitz on the ambient L2 state space. Let G be a standard Gaussian, `q=G`, `z=G`, and consider

\[
 \mathcal B(z,q)=\Phi'(z)q.
\]

There are disjoint intervals `I_j` going to positive infinity on which `sin(2z)>=3/4`; they all have positive Gaussian probability. Shorten them slightly so a fixed sufficiently small positive increment u remains in a larger interval with `sin(2z)>=1/2`. Put `E_j={G in I_j}` and `z_j=G+u 1_{E_j}`. The mean-value theorem and `Phi''=-4b sin(2z)` imply

\[
 \|\mathcal B(z_j,G)-\mathcal B(G,G)\|_2
 \ge2b\,\inf I_j\,u\,\mathbb P(E_j)^{1/2},
 \qquad \|z_j-G\|_2=u\mathbb P(E_j)^{1/2}.
\]

The perturbation norm tends to zero, but the ratio tends to infinity. The original q and z have Gaussian tails and every finite moment. This does not disprove uniqueness or the target theorem; it invalidates the shortcut of treating the raw L2 gradient as locally Lipschitz merely because Phi', Phi'' are bounded and Phi'>0.

The two-input first-layer controls also cannot generally be simultaneously flattened by a point coordinate change when rho is nonzero: their Lie bracket is nonzero for this Phi. The already supplied exact bracket calculation in Fragment J.1, Section 3, applies because Phi' is positive and nonconstant. This is another route obstruction, not a counterexample to the actual physical flow.

#### 8. Local source route and its restart boundary

The raw source formulas suggest a nonperturbative local bootstrap that differs from the reference arctan coordinate transform. With population C(0)=0 and a stopped primal radius B, physical residual sum at most P, and `D=||Phi'||_infinity`,

\[
 \|C(t)\|_2\le P D^3B^3t,\quad
 \|\delta^3(t)\|_2\le P D^4B^3t,\quad
 \|\delta^2(t)\|_2\le P D^5B^4t.
\]

Thus reverse Gaussian source standard deviations are O(t). A local coefficient box has forward entries `|A_{k,j}|<=A_* h_j` and complete backward row sums `sum_j |D_{k,j}|<=D_* t_k`. In that box the source value equations give `||C||_p,||q^1||_p,||q^2||_p<=C t sqrt(p)` for small t, and the random response envelope has exponent O(t^2) times a Gaussian envelope. This closes only a short-time certificate after the expected-derivative and single-source h_j bounds are checked. The complete short-time source calculation is supplied in Fragment I.3; this paragraph alone is only its motivation.

At a reached positive time the reverse fields are not zero and the existing named Gaussian query histories remain part of the state. The O(t) initialization argument cannot simply be repeated from zero. One would need a tail or response estimate propagated from the actual reached state, with a continuation mechanism that cannot accumulate at a finite physical time. Equations (13)-(15) give a strong raw endpoint and qualitative tails, but not that quantitative restart certificate.

The exact remaining implication for this route is therefore:

> A finite-time raw strong endpoint produced by true loss dissipation admits an uncut local strong continuation on the same generated Gaussian action spaces, with enough causal tail/stability control to identify the finite algorithms and all requested observables.

That statement is not proved here. The finite-width GF/GD bounds, the strong endpoint reduction, and the local source theorem I.3 must not be promoted to the stated all-finite-time population result.

### I.5. Conditional global continuation and exact ambient obstructions

Within this proof unit, unqualified section and equation numbers are local.

#### 1. Exact activation and scope

Write the prescribed activation, without modifying its amplitude, as

\[
\Phi(z)=A z+B\sin(2z),\qquad
D=\sqrt{1+\tfrac4{25}v},\quad
A=\frac{1-\frac45e^{-2}}D,\quad B=\frac{2}{5D},
\]
\[
v=\frac{1-e^{-8}}2-4e^{-4}.
\]
Then

\[
\Phi'(z)=A+2B\cos(2z),\quad
m:=A-2B>0,\quad L:=A+2B<\infty,\quad
\|\Phi''\|_\infty=4B.
\]
Indeed \(A-2B=[1/5-(4/5)e^{-2}]/D>0\), since \(e^2>4\).
The activation is globally bi-Lipschitz, smooth, odd, and an affine function plus a bounded perturbation. These properties alone do not supply any of the reachability estimates below.

The model is exactly the two-input, three-hidden-layer Gaussian network and raw metric in Fragment F.1, Section 1. Population incoming fields are

\[
q_i^3=C,\quad b_i^3=\Phi'(z_i^3)q_i^3,\quad
q_i^2=(W^3)^*b_i^3,\quad b_i^2=\Phi'(z_i^2)q_i^2,\quad
q_i^1=(W^2)^*b_i^2,\quad b_i^1=\Phi'(z_i^1)q_i^1.
\]
The two original finite residuals remain in every physical update.

#### 2. Exact unconditional finite-width bounds

Every finite-width GF has a smooth finite-dimensional vector field. Its true raw-gradient energy identity is

\[
\mathcal L_n(t)+\int_0^t\|\dot\Theta_n(s)\|_{\rm raw}^2 ds
=\mathcal L_n(0),
\]
\[
\|\Theta_n(t)-\Theta_n(0)\|_{\rm raw}
\le\sqrt{t\mathcal L_n(0)}.
\]
Thus there is no finite-time raw escape, so finite-width GF is global. At each fixed \(T\), current middle action norms are bounded by their initialized operator norms plus \(\sqrt{T\mathcal L_n(0)}\). Forward induction uses \(|\Phi(z)|\le L|z|\), and backward induction uses \(|\Phi'|\le L\). These give dimension-independent compact-time bounds on all normalized forward/backward second moments and true raw kernel blocks on the usual high-probability initialization event. Here \(\mathcal L_n(0)\to1\).

These are bounds on actual finite trajectories. They do not imply strong canonical compactness, tail uniform integrability, uniqueness, or the finite-width limit.

#### 3. Reference-only comparison with one truncation factor

Let \(X,Y\) be two states on one canonical raw ball, or at the same finite width and initialization. There is a constant \(C_M\), depending on the ball, activation and fixed dataset, such that, with \(a=\|X-Y\|_{\rm raw}\),

\[
\sum_{i,\ell}(\|z_i^\ell(X)-z_i^\ell(Y)\|_2+
\|h_i^\ell(X)-h_i^\ell(Y)\|_2)+\sum_i|r_i(X)-r_i(Y)|
\le C_M a. \tag{3.1}
\]
This follows by the exact decomposition
\((W-\bar W)h+\bar W(h-\bar h)\), the HS-to-operator bound, and Lipschitzness of \(\Phi\).

For a smooth clip \(\tau_R\) with \(|\tau_R|\le|q|\), \(|\tau_R'|\le1\), \(\tau_R(q)=q\) on \(|q|\le R\), and \(|\tau_R|\le2R\), use precisely

\[
D_R(z,q)=Aq+2B\cos(2z)\tau_R(q).
\]
At each layer the capped incoming field is recursively recomputed using the capped higher backward field. In particular, the tail assumption below is about these actual recursively computed inputs.

For \(R_1,R_2\ge u\), including infinite caps,

\[
|D_{R_1}(z,q)-D_{R_2}(\bar z,\bar q)|
\le L|q-\bar q|+8Bu|z-\bar z|
+C_B|\bar q|\mathbf1_{|\bar q|>u}. \tag{3.2}
\]
To prove this, first change \(q\) inside \(D_{R_1}\), using its \(q\)-Lipschitz constant \(L\). In the remaining difference replace both clips by \(\tau_u(\bar q)\); outside \(|\bar q|\le u\) this costs at most a fixed multiple of \(B|\bar q|\), and the retained gate difference is bounded by \(4B|z-\bar z|\,2u\). Every tail belongs to the reference \(Y\).

Start at \(q^3=C\). Applying (3.2), then descending using

\[
\|q_i^\ell(X)-q_i^\ell(Y)\|_2
\le C_M a+C_M\|b_i^{\ell+1}(X)-b_i^{\ell+1}(Y)\|_2,
\]
shows

\[
\sum_{i,\ell}\|b_{R_1,i}^\ell(X)-b_{R_2,i}^\ell(Y)\|_2
\le C_M(1+u)a+C_M\sum_{i,\ell}
\|q_{R_2,i}^\ell(Y)\mathbf1_{|q_{R_2,i}^\ell(Y)|>u}\|_2.
\]
The factor \(u\) multiplies only a forward difference at each descent; it never multiplies the preceding backward discrepancy. Thus the factor remains linear in \(u\), not cubic in \(u\). Rank-one gradient difference estimates and (3.1) yield

\[
\|F_{R_1}(X)-F_{R_2}(Y)\|_{\rm raw}
\le C_M(1+u)a+C_M\sum_{i,\ell}
\|q_{R_2,i}^\ell(Y)\mathbf1_{|q_{R_2,i}^\ell(Y)|>u}\|_2.
\tag{3.3}
\]
Here \(F_R\) is the actual physical capped loss vector field. The full actual residual difference was retained.

#### 4. A conditional global theorem requiring only exponential tails

Fix \(T\). Let \(\chi_M\) be a smooth function of the squared raw increment norm, taking values in \([0,1]\), equal to one on a prescribed ball and zero outside a slightly larger ball. Consider the global fixed-cap population ODEs

\[
\dot X_R=\chi_M(X_R)F_R(X_R),\qquad X_R(0)=0
\]
for increments from the canonical initialization. Fixed-cap local Lipschitzness and this scalar cutoff give global solutions; bounded action norms follow from the cutoff radius. The cutoff is a causal scalar contraction at fixed finite programs. No energy dissipation of these capped paths is assumed.

Assume that their actual incoming fields satisfy

\[
\sup_{R\ge1,\,t\le T,\,i,\ell}
\|q_{R,i}^\ell(t)\mathbf1_{|q_{R,i}^\ell(t)|>u}\|_2
\le K_T e^{-c_Tu},\qquad u\ge0. \tag{ET}
\]
The constants can depend on the fixed activation, dataset, horizon and cutoff radius, but not the cap. Gaussian tails are unnecessary here.

Multiplying (3.3) by the common cutoff adds only a term \(C_Ma\), because all capped fields have uniform raw bounds on this ball. Let \(a(t)=\|X_{R_1}(t)-X_{R_2}(t)\|_{\rm raw}\), \(R=\min(R_1,R_2)\), \(\eta=e^{-c_TR}\). Then for every \(0\le u\le R\),

\[
D^+a\le C[(1+u)a+e^{-c_Tu}]. \tag{4.1}
\]
Set \(z=a+\eta\). While \(z\le1\), choose
\(u=c_T^{-1}\log(1/z)\in[0,R]\). Equation (4.1) gives

\[
D^+z\le C_1z\log(e/z).
\]
With \(w=\log(e/z)\), this implies \(w(t)\ge w(0)e^{-C_1t}\), or

\[
\sup_{t\le T}a(t)
\le e\exp[-c_TR e^{-C_1T}] \tag{4.2}
\]
for all sufficiently large \(R\), the right side itself ensuring that \(z\le1\). This proves uniform Cauchy convergence on arbitrary finite horizons. The same comparison with a fixed fraction of \(R e^{-C_1T}\) in place of \(u\) makes the raw velocities Cauchy as well.

To identify the limit vector field, at each fixed reference cap compare the limit state with that cap using (3.3) and then let the cap increase. Bounded-multiplier continuity identifies all uncapped backward products. The limit is a strong \(C^1\) solution of

\[
\dot X=\chi_M(X)F_\infty(X).
\]
The true loss now obeys its exact identity

\[
\dot{\mathcal L}=-\chi_M\|\nabla\mathcal L\|_{\rm raw}^2,
\quad
\int_0^T\|\dot X\|_{\rm raw}^2dt
\le\int_0^T\chi_M\|\nabla\mathcal L\|_{\rm raw}^2dt
\le\mathcal L(0)=1.
\]
Consequently \(\|X(t)\|\le\sqrt T\). Choose \(\chi_M=1\) on a ball of radius strictly greater than \(\sqrt T\), with a larger support radius. The cutoff is then inactive along the constructed limit. This removes the stopping device without assuming a false capped energy identity or using arbitrary prescribed residual controls.

For uniqueness, compare any bounded-primal strong uncut competitor to the same capped reference by (3.3). The competitor has infinite cap and needs no tail estimate. The regularized Osgood argument yields equality with the limit. At reached times it also gives unique continuation, because the initial cap discrepancy in (4.2), though enlarged by another Osgood exponent, still vanishes. Integer horizons therefore produce a single global canonical strong physical solution.

The existing fixed-cap finite-program, mesh and generated-probe construction applies to this fixed \(\Phi\): its value has linear growth and its first two derivatives are bounded; at each fixed cap all required coordinate derivatives are bounded. If the supplied finite-algorithm and observable bridges are reassembled with (4.2) replacing Gaussian cap removal, they yield the same compact-time full-sequence joint GF/GD conclusions. Their cap comparison is one-reference sided; no tail hypothesis is required for actual finite uncut competitors after fixed-cap reference tails have been transferred by finite-program convergence. This report proves the core population conditional implication, not a completed independent audit of every such observable bridge.

The main unsolved assertion is (ET), or a weaker sufficient modulus. None of the preceding finite-width energy estimates proves it.

#### 5. A prescribed-activation focusing example on raw balls

This is an ambient construction, not a trajectory or a counterexample to the desired theorem.

Keep the two lower layers at their exact initialized values. Let \(h=h_1^2\) be the first sample's initialized second-layer feature, so \(\frac{\|h\|_2^2}{n}\to1\). Let \(G=W_0^3\), independent of the lower layers, and take a column \(J\), either fixed or uniform independently. Write \(g_i=\sqrt n\,G_{iJ}\), iid standard Gaussians. Choose target top preactivations

\[
z_i=\begin{cases}0,&g_i\ge0,\\ \pi/2,&g_i<0,\end{cases}
\qquad
P=\frac{(z-Gh)\otimes h}{\frac{\|h\|_2^2}{n}}.
\]
The tensor convention is \(u\otimes h=uh^T/n\). Thus \((G+P)h=z\) exactly, and

\[
\|P\|_F=\|P\|_{\rm op}
=\frac{\frac{\|z-Gh\|_2}{\sqrt n}}{\frac{\|h\|_2}{\sqrt n}}=O_{\mathbb P}(1).
\]
Choose \(C=\mathbf1+C_0\), a raw readout displacement exactly one from the actual tiny initialized readout. For sample 1,

\[
\Phi'(z_i)=A+2B\operatorname{sign}(g_i).
\]
Consequently the immutable transpose contribution satisfies

\[
\frac{(G^*[\Phi'(z)C])_J}{\sqrt n}
=\frac1n\sum_i g_i[A+2B\operatorname{sign}(g_i)]+o_{\mathbb P}(1)
\longrightarrow 2B\sqrt{2/\pi}>0. \tag{5.1}
\]
The tiny-readout correction is bounded by the initialized operator norm times \(L\frac{\|C_0\|_2}{\sqrt n}\), hence vanishes in this normalization. The learned transpose correction is

\[
P^*[\Phi'(z)C]
=h\,\frac{\frac{( z-Gh)^\top(\Phi'(z)C)}{n}}{\frac{\|h\|_2^2}{n}}.
\]
Its scalar coefficient is \(O_{\mathbb P}(1)\), and \(h_J/\sqrt n\to0\) in probability. Thus (5.1) holds for the full \(q_1^2=(G+P)^*[\Phi'(z)C]\) as well.

All raw increments, action norms, normalized forward/backward second moments, and the two-sample loss are bounded in probability. The second sample shares the same new matrix and is controlled by its operator norm; it need not be assigned a separate activation or matrix. Nevertheless, for every fixed threshold \(u\),

\[
\liminf_{n\to\infty}\frac1n\sum_j(q_{1,j}^2)^2
\mathbf1_{|q_{1,j}^2|>u}\ge\frac{8B^2}{\pi}>0
\]
in the usual probabilistic lower-bound sense. Because \(\Phi'\ge m>0\), the corresponding middle backward field retains a square-tail defect at least \(m^2 8B^2/\pi\).

For random \(J\), the construction can be made invariant under the middle-layer neuron permutations. Exchangeability therefore does not repair the inference. The construction proves only that raw energy-ball bounds, a bounded sine perturbation, positive derivatives, and exchangeability cannot imply the needed tail estimate for all ambient states. Reachability by true GF is an additional and unresolved restriction.

#### 6. Weak compactness does not identify this exact loss

Here is an exact failure of weak lower semicontinuity of the original two-sample loss on its ambient raw Hilbert state space, again not along initialized trajectories.

The initialized second-layer sample Gram is positive definite when \(|\rho|<1\). Choose dual fields \(h_1^\#,h_2^\#\) satisfying
\(\langle h_i^\#,h_j^2\rangle=\delta_{ij}\). Any prescribed pair of \(L^2\) top preactivation fields is realizable from the initialized top action by a sum of two HS rank-one increments.

Use \(C=y_1\mathbf1\), and set the base top preactivation of sample 1 to \(z_*=1/A\), sample 2 to \(\Phi^{-1}(y_1y_2)\). Since \(A>2/\pi\), one has \(0<z_*<\pi/2\), and so
\(\Phi(z_*)=1+B\sin(2/A)>1\). For a simple bound proving \(A>2/\pi\), note \(v<1/2\), \(D<\sqrt{27/25}<26/25\), \(e^{-2}<1/7\), hence \(A>(31/35)(25/26)>4/5>2/\pi\).

Let \(R_k\) be mean-zero Rademacher fields with \(R_k\rightharpoonup0\) in the nonatomic top-layer \(L^2\) space; for instance an orthonormal Rademacher sequence. Perturb only the top action by

\[
\Delta W_k^3=\frac\pi4 R_k\otimes h_1^\#.
\]
These HS increments converge weakly to zero. The sample-1 prediction becomes exactly

\[
y_1E\Phi(z_*+\tfrac\pi4R_k)
=y_1\{A z_*+B\sin(2z_*)\cos(\pi/2)\}=y_1.
\]
The second prediction remains \(y_2\). Therefore every perturbed state has zero loss, while its weak limit has strictly positive loss. The true raw loss is not weakly lower semicontinuous on this ambient Hilbert space. An unqualified weak-compactness/minimizing-movement existence argument is consequently unavailable. This does not exclude stronger compactness of the actual approximants.

#### 7. Positive derivative does not make the raw gradient locally Lipschitz or semiconvex

The same dual-field device isolates the first sample's top preactivation. At an ambient state with \(C=G\), a centered unit Gaussian top-layer field, take its top preactivation constant \(z_* =\pi/4\); make the second sample's top preactivation constant too. Then both predictions are zero and the residuals are \(-y_i\). Take \(y_1=1\), which is enough to refute an activation-uniform ambient statement.

For variations of only the first top preactivation, the restricted first loss is

\[
E(z)=\tfrac12(\langle G,\Phi(z)\rangle-1)^2,
\quad \nabla_z E=r(z)G\Phi'(z).
\]
It has a continuous \(L^2\) gradient, but is not locally Lipschitz at the stated base. Fix a small nonzero scalar \(s\) with
\(|\Phi'(z_*+s)-\Phi'(z_*)|\ge c|s|\). Let
\(E_R=\{G>R\}\), \(h_R=s\mathbf1_{E_R}\). Then \(\|h_R\|_2\to0\), while

\[
\|G[\Phi'(z_*+h_R)-\Phi'(z_*)]\|_2
\ge cR\|h_R\|_2.
\]
The residual change is
\((\Phi(z_*+s)-\Phi(z_*))E[G\mathbf1_{E_R}]\). Its contribution to the gradient difference, divided by \(\|h_R\|_2\), tends to zero by Gaussian square-tail integrability. Thus the gradient-to-state difference quotient is unbounded. Embedding through \(h_R\otimes h_1^\#\) changes raw norms only by fixed positive factors and gives the same conclusion for the full network gradient block.

For semiconvexity, take \(E_R=\{G<-R\}\) and the unit direction
\(v_R=\mathbf1_{E_R}/\sqrt{P(E_R)}\). Its second directional derivative is

\[
E''(z_*)[v_R,v_R]
=\big(E[G\Phi'(z_*)v_R]\big)^2
- E[G\Phi''(z_*)v_R^2]
=\big(E[G\Phi'(z_*)v_R]\big)^2
+4B E[G\mid G<-R]\to-\infty.
\]
The first term tends to zero because it is bounded by a constant times \(E[G^2\mathbf1_{G<-R}]\). Hence no finite lower Hessian bound, and no local semiconvexity constant, holds in this ambient raw norm. This refutes importing a generic locally-Lipschitz or semiconvex Hilbert-gradient theorem merely from positivity of \(\Phi'\).

## J. Exact bounded-memory and coordinate partials

The bounded-memory identities hold on any existing strong path with the displayed bounded activation and zero population readout; the finite version includes the actual initial readout term. The coordinate obstruction concerns simultaneous straightening for arbitrary controls. None of these statements asserts a new global population construction.

### J.1. Exact bounded-activation learned memories and coordinate obstruction

Within this proof unit, unqualified section and equation numbers are local.

#### 1. A moderate candidate and what can actually be proved

One structurally different candidate is

\[
\phi(z)=1+\tanh z.
\]

It has bounded value and first two derivatives, is strictly increasing, and is not selected close to an affine activation. Odd `tanh` is another candidate under the stipulated exclusion of both endpoint correlations. The results below apply to every bounded C2 activation with bounded first and second derivatives; they do not prove the desired global theorem for either candidate.

Write `M=||phi||_infinity`, `D=||phi'||_infinity`. The three population spaces are separate probability spaces, with `A:H1->H2`, `B:H2->H3`, and readout `C in H3`. In the stated model,

\[
\delta_a^3=C\phi'(z_a^3),\qquad
q_a^2=B^*\delta_a^3,\quad
\delta_a^2=\phi'(z_a^2)q_a^2,\qquad
q_a^1=A^*\delta_a^2.
\]

The raw physical updates are

\[
\dot C=-\sum_a r_a h_a^3,\quad
\dot B=-\sum_a r_a\delta_a^3\otimes h_a^2,\quad
\dot A=-\sum_a r_a\delta_a^2\otimes h_a^1.
\]

Let `J(t)=integral_0^t sum_a |r_a(s)| ds`. All the following statements hold on any interval on which a strong raw solution exists and the displayed integrals are defined. They therefore apply to genuine finite-dimensional gradient flow without assuming population construction, and conditionally to any already-constructed strong population path. For the population initialization, `C(0)=0`.

### Exact bounded-memory lemma

For every such path,

\[
\|C(t)\|_\infty\le M J(t),\qquad
\|\delta_a^3(t)\|_\infty\le DM J(t).                 \tag{1}
\]

The trained top increment has an integral kernel, between the separate populations, satisfying

\[
\|(B(t)-B_0)(\omega_3,\omega_2)\|_\infty
 \le \tfrac12 DM^2J(t)^2.                            \tag{2}
\]

Consequently the middle incoming field admits the *exact* decomposition

\[
q_a^2(t)=B_0^*\delta_a^3(t)+m_a^2(t),\qquad
\|m_a^2(t)\|_\infty
 \le\tfrac12 D^2M^3J(t)^3.                          \tag{3}
\]

The bottom incoming field likewise has an exact decomposition

\[
q_a^1(t)=A_0^*\delta_a^2(t)+m_a^1(t),                 \tag{4}
\]

where

\[
\|m_a^1(t)\|_\infty
\le M\int_0^t\sum_b |r_b(s)|
       \|\delta_b^2(s)\|_2\|\delta_a^2(t)\|_2\,ds.   \tag{5}
\]

In particular, if `sup_{a,s<=T} ||delta_a^2(s)||_2 <= N_T`, then

\[
\sup_{a,t\le T}\|m_a^1(t)\|_\infty\le M J(T)N_T^2.  \tag{6}
\]

Proof. Integrating the readout equation and using `|h|<=M` proves (1). The top increment kernel is

\[
(B(t)-B_0)(\omega_3,\omega_2)
=-\int_0^t\sum_b r_b(s)\delta_b^3(s,\omega_3)
                                  h_b^2(s,\omega_2)ds.
\]

Its absolute value is at most `DM^2 integral_0^t J(s) dJ(s)`, which equals the right side of (2). Applying its adjoint to `delta_a^3(t)` and using (1) proves (3). For the next increment, adjunction of its exact rank-one integral gives

\[
 m_a^1(t)=-\int_0^t\sum_b r_b(s)h_b^1(s)
                \langle\delta_b^2(s),\delta_a^2(t)\rangle_2 ds.
\]

Bound `h_b^1` by M and use Cauchy--Schwarz. This proves (5)-(6). No independence assumption, source-response approximation, or coordinate pairing occurs.

At finite width the same proof uses the kernel `n(B-B0)_{ij}` and normalized sums. A nonzero initial readout adds `||C0||_infinity` to (1) and the corresponding term `DM||C0||_infinity J(t)` to (2). The actual prescribed initial readout has coordinate supremum tending to zero in probability, since its entries have variance `n^-2`.

### Compact-time physical constants

For a true gradient flow the exact energy identity and initial loss E0 give

\[
\mathcal L(t)\le E_0,\qquad
J(T)\le 2\sqrt{E_0}\,T,
\qquad
\|\Theta(t)-\Theta(0)\|_{\rm raw}\le\sqrt{TE_0}.       \tag{7}
\]

The residual inequality uses `sum|r_a| <= sqrt(2) sqrt(r_1^2+r_2^2)=2sqrt(L)`. Thus all constants in (1)-(6) are finite on every finite physical interval, independently of input separation. For example, when `||B0||op<=b0`,

\[
\|\delta_a^2(t)\|_2
\le D\|B(t)\|_{\rm op}\|\delta_a^3(t)\|_2
\le D^2M(b_0+\sqrt{TE_0})J(T),                       \tag{8}
\]

which supplies an explicit N_T in (6).

This is stronger trajectory information than a raw Hilbert ball: the actual learned top kernel is bounded pointwise, and both learned reverse-memory terms are bounded pointwise. It places all remaining possible reverse-field concentration in the two reused frozen Gaussian actions `B0*delta3` and `A0*delta2`. The physical residuals were retained in every step. It does not give approximate energy for a nongradient backward-cap flow automatically.

#### 2. Why bounded inputs to a reused Gaussian matrix are not enough

There is an exact obstruction to inferring tails for `B0*delta3` merely from bounded delta3 and a bounded Gaussian operator norm.

Let `W_n` have independent N(0,1/n) entries and choose J uniformly from `{1,...,n}`, independently. Set

\[
 v_i=\operatorname{sign}(W_{iJ}),\qquad q=W_n^T v.
\]

Then `||v||infinity=1`, but

\[
q_J=\sum_i|W_{iJ}|,\qquad
\frac{q_J}{\sqrt n}\longrightarrow\sqrt{2/\pi}
\quad\hbox{in probability}.                          \tag{9}
\]

Indeed, condition on J and apply the weak law to the independent absolute standard normal variables `sqrt(n)|W_iJ|`. Therefore, for every fixed u,

\[
\liminf_{n\to\infty}\frac1n\sum_j q_j^2
          \mathbf1_{\{|q_j|>u\}}\ge 2/\pi
\quad\hbox{in probability}.                          \tag{10}
\]

A precise reading of (10) is that, for each eta>0, the probability that its left finite-n expression exceeds `2/pi-eta` tends to one. The single selected coordinate proves this. The arrays can be made exchangeable under input- and output-coordinate permutations: J is uniform and the definition uses only signs of its selected column. Thus coordinate exchangeability does not repair the conclusion. The Gaussian matrix operator norm still has its ordinary bounded high-probability behavior, and `(||q||_Euclidean/sqrt(n))<=||W_n||op`; there is no contradiction with L2 control.

This is not a counterexample to the neural dynamics. The selected-column input is not asserted to be produced by the actual smooth finite-time training program. It is a rigorous obstruction to a proposed general lemma that would ignore adaptedness, causal source response, or the special origin of delta3. Adding any uniformly bounded memory to q leaves the concentrated coordinate contribution nonvanishing. Therefore (1)-(8), although useful, do not by themselves identify the population or remove backward caps.

#### 3. A two-input obstruction to the one-input change of variables

The bounded-arctangent one-input local source proof simplifies the first-layer differential equation using `F'=1/phi'`; the transformed first field then has no `phi'' q` in its vector field. That cancellation does not extend to correlated two-input raw training by any C2 point-coordinate diffeomorphism that would remove both arbitrary incoming controls.

Assume `beta=phi'>0`, `|rho|<1`, and write

\[
\Gamma=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad
\dot z=\Gamma\begin{pmatrix}\beta(z_1)u_1\\\beta(z_2)u_2\end{pmatrix}.
\]

The controls contain the actual residual/backward factors; this statement concerns simultaneous simplification for all possible controls. Define

\[
X_1(z)=\beta(z_1)\Gamma e_1,\qquad
X_2(z)=\beta(z_2)\Gamma e_2.
\]

If `rho != 0`, a C2 diffeomorphism that sends both vector fields to constant vector fields exists on all of R2 only when phi is affine. In fact the bracket is

\[
[X_1,X_2]
=\rho\beta(z_1)\beta'(z_2)\Gamma e_2
 -\rho\beta(z_2)\beta'(z_1)\Gamma e_1.                \tag{11}
\]

To prove the necessity without invoking an external differential-geometric theorem, suppose `DF X_b=c_b` are constant. Differentiate `DF X_2=c_2` in direction X_1, differentiate `DF X_1=c_1` in direction X_2, and subtract. The symmetric second derivatives of F cancel, leaving `DF [X_1,X_2]=0`. Invertibility gives a zero bracket. The two columns of Gamma are independent; `rho!=0` and positive beta therefore force `beta'(z_1)=beta'(z_2)=0` for every pair z. Thus beta is constant. Conversely affine phi already has constant vector fields.

When rho=0, the componentwise coordinate `F_a(z)=integral_0^{z_a} du/beta(u)` does straighten both fields wherever it is a diffeomorphism; bounded positive beta ensures its image is all R for each component. For nonzero rho the same attempted coordinate gives off-diagonal factors `rho beta(z_b)/beta(z_a)`, so the curvature-dependent response has merely moved into those factors.

This is a route obstruction, not a statement that a two-sample theorem is false. It excludes a tempting exact gauge reduction as a way to make a moderately nonlinear two-sample raw flow affine in its arbitrary incoming controls. Replacing Gamma by the identity would change the original metric and is not authorized. The interval `|rho|<=1-delta` contains nonzero correlations, so the orthogonal special case alone cannot discharge the target.

#### 4. What survives and what is still missing

The bounded-activation class has a concrete structural advantage over the near-affine unbounded-value class: the readout, top trained kernel, and learned reverse-memory terms admit the exact finite-horizon bounds above without any small nonlinear amplitude. This is a reasonable nonperturbative class to investigate while preserving initialization, all trained layers, and the raw metric.

The new sufficient missing lemma is now sharply localized: exploit the actual causal neural origin of delta3 and delta2 to obtain cap-independent tails or an adequate stability modulus for the two *reused initial Gaussian adjoint actions*. Boundedness, energy, action norm, and exchangeability alone cannot imply that lemma, by (9)-(10). The original source coefficients are one possible language for this missing causal control, but their global closure has not been proved here. The existing near-affine source-response smallness cannot simply be deleted.

A successful proof must additionally remove caps for a stopped physical construction, recover enough approximate energy to remove the stop, identify both orientations of the Gaussian actions, and verify the exact raw-GD and hidden-velocity bridges. The existing finite-program/common-action machinery is a dependency for those steps, not an already-discharged conclusion for tanh. No practical positive epsilon(delta), global uniqueness, reached-state continuation, or population/raw-GD identification has been proved in this proof unit.
