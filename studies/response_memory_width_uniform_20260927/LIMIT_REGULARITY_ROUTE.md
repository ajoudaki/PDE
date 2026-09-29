# What dense population regularity can and cannot supply

Scoped analysis, 27 September 2026. Inputs: the current `paper/main.tex`, `paper/comparison_appendix.tex`, and `docs/notation.qmd`. No other study results were used. This note analyzes the existing tanh architecture and its original clocks; it does not change the manuscript or claim a Gaussian closure theorem.

The conclusions have three different strengths:

1. A width-uniform bound in the **raw parameter norm** is false for the learning-speed closure with arbitrary finite initializations, even for perfectly replicated tanh networks having an exact smooth population limit. This is a counterexample to a proposed conclusion in that norm.
2. Dense population existence, arbitrarily smooth dense paths, and strong convergence of the finite dense paths and response fields do **not** imply a uniform Lipschitz or one-sided stability bound in the normalized parameter norm. An explicit stationary tanh example below proves this. Its response-memory closure is exact, so it is a counterexample to a proposed proof implication, **not** a counterexample to the normalized response-memory theorem.
3. A local (C^1) population vector field on a specified Banach space gives a tube bound for that population vector field. It gives no automatic bound for its finite-width approximations. Establishing the bridge for canonical Gaussian initialization remains additional mathematical work. Merely calling the limiting flow “well behaved” does not perform that work.

## 1. Norms and what the existing proof actually needs

For a parameter difference (v=(v_1,v_2,ldots,v_L,v_w)), write explicitly

\[
 \lVert v\rVert_{\mathrm{mob}}^2
 =\frac{\lVert v_1\rVert_F^2}{n}
  +\sum_{\ell=2}^L\lVert v_\ell\rVert_F^2
  +\frac{\lVert v_w\rVert_2^2}{n}.
\]

This is the Hilbert norm induced by the inverse of the canonical mobility matrix. Hidden increments use ordinary Frobenius norm: the matrix (uv^T/n) has Frobenius norm ((\lVert u\rVert_2/\sqrt n)(\lVert v\rVert_2/\sqrt n)), agreeing with the Hilbert–Schmidt norm of the corresponding population rank-one operator. Dividing hidden Frobenius norm by another factor of (n) would change the question.

The current proof has two independent parts. First, projection identities control the accumulated perturbation in

\[
 \dot{\widehat\theta}=F_n(\widehat\theta)+E,
 \qquad E_1=E_w=0.
\]

Second, stability converts that perturbation into trajectory error. A uniform Lipschitz estimate on a common tube is sufficient, but stronger than necessary. The one-sided estimate

\[
 \langle u-v,F_n(u)-F_n(v)\rangle_{\mathrm{mob}}
 \le \Lambda_T\lVert u-v\rVert_{\mathrm{mob}}^2
 \tag{1}
\]

is enough: differentiating the squared error, dividing by its norm when nonzero, and using an arbitrarily small regularization at zero gives

\[
 \sup_{t\le T}\lVert\widehat\theta(t)-\theta(t)\rVert_{\mathrm{mob}}
 \le e^{\max(\Lambda_T,0)T}\int_0^T\lVert E(t)\rVert_{\mathrm{mob}}\,dt.
 \tag{2}
\]

The constants and tube radius in this statement must be independent of (n). A first-exit argument then derives closure boundedness; it need not be assumed.

For a gradient flow, (1) follows from a uniform lower bound on the loss Hessian in this metric. There is no need to appeal to nonnormal matrices: after the constant mobility change of coordinates, the Jacobian is a negative symmetric Hessian. Negative loss curvature can nevertheless give arbitrarily large **positive** eigenvalues of that Jacobian.

## 2. A genuine obstruction in raw parameter norm

Consider a width-one, two-hidden-layer tanh network on (d=m=x=y=1), with

\[
 W^{(1)}(0)=a>0,\qquad W^{(2)}(0)=b>0,\qquad w(0)=0.
\]

For width (n), repeat the first weight and readout (n) times and replace the middle scalar (b(t)) by the matrix (b(t)\mathbf1\mathbf1^T/n). Dense gradient flow preserves this family exactly: every neuron has the same forward and backward response, and the scalar equations are precisely the width-one equations. The population limit is that same smooth three-variable flow. The initialized middle operator has norm (b), independently of width.

The original learning-speed response-memory closure also preserves this family exactly, for every fixed finite (P): the residual and hence the clock are unchanged, all moment vectors are repeated copies, and the reconstruction has the required (1/n) scaling. Thus its scalar readout discrepancy is the same at every width, while its raw readout-vector discrepancy is (\sqrt n) times that scalar discrepancy.

Here is a direct verification that the discrepancy is nonzero for **every finite** (P), rather than an appeal to generic behavior. Put

\[
 A=\tanh a,\quad Q=\operatorname{sech}^2a,\quad
 H=\tanh(bA),\quad D=\operatorname{sech}^2(bA).
\]

At small positive time, both flows satisfy

\[
 w(t)=2Ht+O(t^2),\qquad
 h^{(1)}(t)=A+2bQ^2HD\,t^2+O(t^3),
\]

and the residual-weighted backward history is (b_{\rm hist}(t)=-2HDt+O(t^2)). On the unit prefix, the forward history is the constant (A), and the backward history is zero. For each fixed finite (P), endpoint evaluation of the polynomial projection is a bounded functional near (t=0). Consequently, the changed forward history contributes only (O_P(t^3)) to its endpoint projection, and the backward history contributes only (O_P(t^2)). Hence

\[
 h^{(1)}-h^{(1)*}=2bQ^2HD\,t^2+O_P(t^3),\qquad
 b_{\rm hist}-b_{\rm hist}^*=-2HDt+O_P(t^2).
\]

The exact defect identity therefore gives

\[
 E_2(t)=-8bQ^2H^2D^2\,t^3+O_P(t^4).
\]

Integrating the physical error equation and then the readout equation yields

\[
 \widehat W^{(2)}-W^{(2)}=-2bQ^2H^2D^2t^4+O_P(t^5),
\]
\[
 \widehat w-w=-\frac45AbQ^2H^2D^3t^5+O_P(t^6).
 \tag{3}
\]

For completeness, feedback into the first-layer error starts at order (t^6): a middle-layer error of order (t^4) is multiplied by the readout of order (t) in its velocity. The leading readout error therefore comes from (2AD(\widehat W^{(2)}-W^{(2)})), giving (3). All leading coefficients are nonzero.

For any fixed finite (P), choose a sufficiently small (t_P>0) at which (3) is nonzero. Then

\[
 \sup_n\sup_{t\le T}\lVert\widehat\theta_{n,P}(t)-\theta_n(t)\rVert_2=\infty
\]

for every (T>0). This rules out a width-independent threshold and constant in a raw-norm (P^{-1}) bound. Normalized readout error and predictor error stay unchanged under replication, so this argument does not rule out their width-uniform bounds. The original joint clock is not replication invariant because it uses an unnormalized response speed; the argument above is specifically a theorem about the learning-speed closure, and is not silently transferred to that clock.

## 3. A stationary tanh family with unbounded transverse growth

This example uses fixed data, fixed depth, bounded readout, uniformly bounded source operators, and source operators converging in operator norm. Every dense trajectory is stationary. Even all normalized backward fields converge strongly. Nevertheless, no uniform version of (1) can hold in a neighborhood of these paths.

Fix (a,c>0), (0<\alpha<1/2), and even widths (n). Let (s\in\{-1,1\}^n) have equally many signs of each type. Set

\[
 x_j=\sqrt2(1,t_j),\qquad(t_1,t_2,t_3)=(-1,0,1),\qquad
 (y_1,y_2,y_3)=(-1,2,-1).
\]

Take first-layer rows ((a,0)), readout (w=\mathbf1), and

\[
 W_n^{(2)}=
 \frac{c}{A}\frac{s\mathbf1^T}{n}
 +n^{\alpha-1}\mathbf1
       \left(e_1^T-\frac{\mathbf1^T}{n}\right),
 \qquad A=\tanh a.
 \tag{4}
\]

For every training input, (h^{(1)}=A\mathbf1), (z^{(2)}=cs), and (h^{(2)}=\tanh(c)s), so (f_j=0). Write (Q=\operatorname{sech}^2a) and (D=\operatorname{sech}^2c). Then

\[
 \delta^{(2)}=D\mathbf1,\qquad
 \delta^{(1)}=QD n^\alpha\left(e_1-\frac{\mathbf1}{n}\right).
 \tag{5}
\]

The residuals are ((1,-2,1)). Their sum and their input-weighted sum both vanish. The readout and hidden-matrix velocities therefore vanish, and the first-layer velocity vanishes as well. These are exact stationary dense solutions, with constant loss (2).

The second term of (4) has both operator and Frobenius norm

\[
 n^{\alpha-1/2}\sqrt{1-1/n}\longrightarrow0.
\]

After putting the populations on a common probability space with a fixed balanced sign function, the first term is a fixed rank-one operator. The source operators converge in operator norm and Hilbert–Schmidt norm. The first-layer and readout fields are constant in (n); all forward fields converge exactly; and (5) converges to zero in normalized (L^2), since its norm is (QD n^{\alpha-1/2}\sqrt{1-1/n}). Every time derivative of every dense field is zero. Thus the dense limit is regular in substantially stronger senses than mere predictor convergence.

Now vary only the second coordinate of the first row of (W^{(1)}), in the direction (v_1=\sqrt n\,e_1e_2^T). This direction has mobility norm one. Set

\[
 R=\tanh''a<0,\quad J=\tanh''c<0,\quad
 a_n=\frac{c}{An},\quad b_n=n^{\alpha-1}(1-1/n).
\]

For a sample with second input coordinate (t), direct differentiation gives

\[
 Df[v]=DQ\sqrt n\,b_n t,
\]
\[
 D^2f[v,v]=
 \left(DR n b_n+2JQ^2\frac cA b_n\right)t^2
 =:H_n t^2.
\]

Indeed (W^{(2)}e_1=a_ns+b_n\mathbf1); in the term containing (\tanh''(cs)=Js), the average of (s(a_ns+b_n)^2) is (2a_nb_n). This proves the displayed expression without neglecting the second-layer curvature.

For unhalved mean squared loss,

\[
 D^2\mathcal L[v,v]
 =\frac43D^2Q^2n b_n^2+\frac43H_n
 =\frac43DR n^\alpha(1+o(1))\longrightarrow-\infty.
 \tag{6}
\]

The first term tends to zero because (2\alpha-1<0). As the flow is a gradient flow in the mobility metric,

\[
 \langle v,DF_n v\rangle_{\mathrm{mob}}
 =-D^2\mathcal L[v,v]\longrightarrow+\infty.
\]

Thus the variational equation has an increasingly large positive eigenvalue at the dense path itself. This is a symmetric-Hessian instability, not a nonnormal transient-growth example. Equation (6) excludes both a uniform Lipschitz estimate and a uniform one-sided estimate on any neighborhoods containing these states.

**Exact scope of the obstruction.** Both response-memory closures are stationary in this example. For the learning-speed closure, all forward histories are constant, so their projection errors vanish, including at the zero backward prefix. For the joint closure both histories, with matching prefixes, are constant. Their matrix defects vanish. The counterexample therefore proves that dense-path regularity cannot be promoted to uniform off-path stability by logic alone. It does not prove that the memory defect excites the unstable directions, nor that normalized trajectory or predictor tracking fails. A theorem exploiting the special form and correlations of the memory defect remains possible.

The example uses arbitrary deterministic initialization with order-one readout. Multiplying the readout by any fixed positive small constant changes the coefficient but preserves the divergence. It does not satisfy the canonical independent Gaussian law or its width-vanishing initial stored readout. It must not be advertised as a high-probability Gaussian counterexample.

## 4. Why local population (C^1) regularity is stronger than path regularity

There are three different statements:

* A path (\theta_\infty(t)) is smooth or has bounded variation.
* A limiting vector field (F_\infty:U\subset X\to X) is locally (C^1) on an open neighborhood of that path in a specified Banach space.
* The finite vector fields (F_n), in compatible norms, have a common tube and uniformly bounded derivatives there.

The first does not imply the second. The second implies a bounded derivative on some tube around the compact image of the path **for that single vector field**: at each point, continuity of the derivative supplies a neighborhood on which its norm is bounded; take a finite cover of the compact path and shrink to a common tube radius. Integrating the derivative on sufficiently short line segments gives a local uniform Lipschitz estimate. It does not imply the third statement. The example in Section 3 directly disproves a transfer based solely on convergent paths and sources.

There is also a concrete functional-analytic issue. On an atomless probability space, the tanh Nemytskii map is Lipschitz (L^2\to L^2), but it is not Fréchet differentiable at zero. If (E_k) have probabilities decreasing to zero and (u_k=\mathbf1_{E_k}), then

\[
 \frac{\lVert\tanh(u_k)-u_k\rVert_{L^2}}
      {\lVert u_k\rVert_{L^2}}=1-\tanh(1)>0.
\]

Directional differentiation would require the derivative at zero to be the identity. The displayed sequence prevents a Fréchet remainder estimate. Consequently, smooth scalar activation and bounded (L^2) population fields do not establish a (C^1) population vector field in the normalized Hilbert topology.

The more specific backpropagation difficulty is the product

\[
 (\phi'(z)-\phi'(\widetilde z))\,(W^*\delta).
\]

Bounds on (W:L^2\to L^2) and on (\delta\) in (L^2) control (W^*\delta\) only in (L^2). They do not bound multiplication by that field as an operator on (L^2). Section 3 realizes this issue inside the actual network, while every dense time derivative is zero.

Using an (L^\infty)-type Banach algebra can legitimately make some population vector fields (C^1). But the initialized source and its true adjoint must act boundedly on the chosen space, and the assumptions must include the required response multipliers. For finite Gaussian matrices, the full (\ell^\infty\to\ell^\infty) norm is a row absolute sum, generally increasing with width. Thus choosing that topology is a substantial model/initialization hypothesis, not a consequence of the usual (L^2\) operator bound. Likewise, arbitrary finite (L^p) moments do not turn an unbounded multiplier into a bounded (L^2\) operator.

## 5. A legitimate conditional construction, and the missing bridge

The existing proof does yield a useful abstract theorem if the hypotheses are stated at the correct level. Suppose a family of finite or population realizations has, on a common tube around its dense paths:

1. uniformly bounded normalized forward/backward response norms, hidden operator norms, residuals, and dense velocities divided by residual;
2. a uniform one-sided estimate (1), or a uniform Lipschitz estimate;
3. for the joint clock, a uniform bound on the derivative of the **normalized** response map (\Psi/\sqrt{nm}), a uniform positive lower bound on the initial residual, and a uniform derivative bound for the predictor.

Assume local existence for the finite-order memory equations. None of these assumptions is a bound on a memory trajectory. Stop that trajectory on leaving the tube; the proof works on the stopped interval and then rules out its exit for a width-independent sufficiently large (P).

For the learning-speed clock, the manuscript's forward derivative recursion becomes independent of width after replacing its vector bounds (\alpha_\ell,\beta_\ell) by (\alpha_\ell/\sqrt n,\beta_\ell/\sqrt n), and (Z_\ell) by (Z_\ell/n). Hidden operator bounds replace raw initialized Frobenius bounds. The endpoint factor (P) still cancels the forward projection factor (P^{-1}). Thus the stopped accumulated defect is at most (C_T/P). Equation (2) gives (C_T'/P), and first exit gives continuation. This establishes an actual theorem from hypotheses 1–2 without assuming closure stability or boundedness separately.

For the original joint clock, do not pretend that its unnormalized clock has a width-independent length. Use the weighted Jackson estimate already derived in the comparison appendix. With insertion mass (M_T) and normalized variation (V_T), it gives

\[
 \int_0^T\sum_{\ell=2}^L\lVert E_\ell\rVert_F\,dt
 \le \frac{C_J^2M_T}{P^2}
       \left(\frac{M_T}{\sqrt{nm}}+V_T\right)^2.
\]

The coarse projection-energy bound first controls total parameter variation independently of (P). Hypothesis 3 then bounds (V_T). Combining this inequality with (2), followed by first exit, yields a width-independent (P^{-2}) bound for the **unchanged** original joint-clock algorithm. This part does not require a width-independent raw clock length.

A population (C^1) neighborhood theorem can supply these hypotheses for a single population realization if its norms also control the response maps and products. It can then prove a population response-memory theorem. That is mathematically meaningful, but it is distinct from proving the finite-width uniform estimate.

A sufficient transfer mechanism would be a common Banach-space realization with uniformly bounded embeddings/projections, exact or (C^1)-consistent representation of (F_n) by (F_\infty), and the corresponding response-map bounds. Then differentiation and operator-norm convergence transfer the tube constants. These are assumptions about **maps on neighborhoods**, not merely trajectories. In the canonical Gaussian architecture, such a common realization and its neighborhood estimates have not been derived in this note. Assuming them without proof would restate much of the missing problem.

## 6. Deterministic versus Gaussian, and the unresolved theorem

The raw-norm counterexample and transverse-instability example concern deterministic finite initializations. They are valid within the stated canonical tanh architecture and mobility, so they exclude unrestricted deterministic inferences. They do not exclude a width-uniform high-probability theorem for the prescribed independent Gaussian initialization.

A high-probability result must state its quantifiers, for example: for every (T\) and confidence parameter (\varepsilon>0), constants (C_{T,\varepsilon},P_{0,T,\varepsilon}) independent of (n) give the desired estimate on events of probability at least (1-\varepsilon). Dense convergence in probability alone gives no such bound for closure error. Finite empirical maxima, bounded normalized moments, and bounds restricted to the structured memory defect are different forms of control; none may be substituted for another.

The most promising distinction is that (1) controls **every** perturbation, whereas the closure generates very special finite-rank perturbations built from its own forward/backward histories. The stationary example makes this distinction exact: the worst transverse directions exist, but the defect is identically zero. A successful Gaussian theorem may establish stability only for those structured perturbations, using their correlations with the initialized operators. Another route may work in stronger weighted norms in which the random multipliers are controlled, then transfer only the desired trajectory/predictor observable back to the normalized norm. Neither route follows from dense population existence alone, and neither is completed here.

Accordingly, a rigorous final statement at present is: **raw-norm width independence is untenable in the arbitrary-initialization scope; normalized/predictor width independence is not refuted, but dense-limit regularity and dense convergence alone do not justify the stability step. Explicit local population (C^1) structure can support a population theorem, while its transfer to canonical Gaussian finite networks remains an independent proof obligation.**
