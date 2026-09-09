# Independent activity and fixed-program source audit

Audited 2026-09-05 from `/tmp/GENERAL_ACTIVATION_ACTIVITY.md` (373 lines), the relevant activity and Gaussian-conditioning passages of `/tmp/THREE_INPUT_LOCAL_LIMIT_PROOF.md` (661 lines), and the primary Tensor Programs III PDF and local TeX source. The solve-math-rigorously skill was read. This audit does not certify the separate mesh-uniform existence argument.

The conditional strict-activity argument passes. Its sufficient activation class is **both activations nonaffine, continuously differentiable, with bounded continuous first derivatives**. Bounded activation values, second derivatives, oddness, analyticity, monotonicity, and derivatives bounded away from zero are unnecessary for this part. Thus both unbounded nonaffine globally Lipschitz C1,1 activations are included, provided the claimed strong flow has independently been constructed. The Gaussian first-weight initialization, independent Gaussian middle matrix, zero limiting stored readout, positive scales, pairwise nonparallel normalized inputs, and every label nonzero suffice. No all-depth or nonzero-readout activity theorem is established here.

## Exact weighted-loss version

For L = sum_a omega_a(f_a-y_a)^2 with omega_a>0, set p_a=omega_a y_a in this audit only. This symbol is the weighted label, not a residual, derivative, or extra network field. The sum of the weights may be normalized to one for the existence estimates, but activity does not require that normalization. Every training sum in the source flow must acquire omega_b. The three unweighted kernel blocks remain

\[
K_{ab}^{(1)}=G_{ab}\mathbb E[\delta_a^{(1)}\delta_b^{(1)}],\quad
K_{ab}^{(2)}=\mathbb E[H_a^{(1)}H_b^{(1)}]\mathbb E[\delta_a^{(2)}\delta_b^{(2)}],\quad
K_{ab}^{(3)}=\mathbb E[H_a^{(2)}H_b^{(2)}],
\]

with physical K=kappa_1 K^(1)+kappa_2 K^(2)+kappa_3 K^(3). Consequently

\[
\dot f_a=-2\sum_bK_{ab}\omega_b r_b,\qquad
\dot L=-4\sum_{a,b}\omega_a r_aK_{ab}\omega_b r_b.
\]

In source equations (4), (8), (18)–(21), replace y by p throughout, including the direction used in kernel quadratic forms. In full, writing Y_a=Z_{0,a}^{(2)} and Q_ab=E[H_{0,a}^{(1)}H_{0,b}^{(1)}], define

\[
S=\sum_b p_b\phi^{(2)}(Y_b),\quad
U_a=S(\phi^{(2)})'(Y_a),\quad
P_a=(W_0^{(2)})^*U_a,\quad
B_a=(\phi^{(1)})'(Z_{0,a}^{(1)})P_a,
\]
\[
T_a=\sum_bG_{ab}p_bB_b,\quad
M_a=\sum_bp_bQ_{ab}U_b,\quad
A_a=(\phi^{(1)})'(Z_{0,a}^{(1)})T_a,\quad
R_a=\kappa_2M_a+\kappa_1W_0^{(2)}A_a.
\]

All expectations are on the appropriate one of the two neuron populations. Let V_ab=E[U_aU_b] and D_ab=E[B_aB_b]. The onset expansions, with exact factors, are

\[
\begin{aligned}
W^{(3)}(t)&=2\kappa_3tS+o_{L^2}(t),\\
\delta_a^{(2)}(t)&=2\kappa_3tU_a+o_{L^2}(t),\\
\delta_a^{(1)}(t)&=2\kappa_3tB_a+o_{L^2}(t),\\
Z_a^{(1)}(t)-Z_{0,a}^{(1)}&=2\kappa_1\kappa_3t^2T_a+o_{L^2}(t^2),\\
W^{(2)}(t)-W_0^{(2)}&=2\kappa_2\kappa_3t^2\sum_bp_bU_b\otimes H_{0,b}^{(1)}+o_{\mathrm{op}}(t^2),\\
Z_a^{(2)}(t)-Y_a&=2\kappa_3t^2R_a+o_{L^2}(t^2).
\end{aligned}
\]

Define A_1=p^top(G circ D)p and A_2=p^top(Q circ V)p; both are strictly positive. Then

\[
\begin{aligned}
\kappa_1K^{(1)}(t)&=4\kappa_1\kappa_3^2t^2(G\circ D)+o(t^2),\\
\kappa_2K^{(2)}(t)&=4\kappa_2\kappa_3^2t^2(Q\circ V)+o(t^2),\\
p^\top K^{(3)}(t)p&=\mathbb E S^2+4\kappa_3(\kappa_1A_1+\kappa_2A_2)t^2+o(t^2),\\
p^\top K(t)p&=\kappa_3\mathbb E S^2+8\kappa_3^2(\kappa_1A_1+\kappa_2A_2)t^2+o(t^2),\\
-\dot L(0)&=4\kappa_3\mathbb E S^2>0.
\end{aligned}
\]

There is no extra sigma_2^2 on either trained rank-one term. Sigma_1 enters through the first root distribution; sigma_2 enters through Q-to-Y covariance and the reused initial-matrix laws below. The learning multipliers kappa_1,kappa_2,kappa_3 stay separate from these initialization scales.

## Positive-definiteness audit

The finite-difference ridge argument is sound, including singular input Gram matrices. Put u_a=x_a/sqrt(d). For b!=a, the vector v_ab=(u_a-G_ab u_b)/(1-G_ab^2) has u_a^top v_ab=1 and u_b^top v_ab=0. Applying all differences in the directions h v_ab isolates the selected ridge term. A bounded sequence with identically vanishing finite differences of fixed order is constant, so bounded continuous nonconstant ridge functions are linearly independent. For an unbounded nonaffine C1 activation with bounded derivative, differentiate a proposed relation in a direction not perpendicular to any u_a; its derivative is bounded, continuous, nonconstant, and the preceding argument applies. Gaussian full support turns an almost-sure relation into a pointwise relation. Therefore Q is positive definite for the full asserted activation class. The m=1 case is handled directly.

Since Cov(Y)=sigma_2^2 Q, Y has full support in R^m. To verify V, assume c^top U=0. The identity

\[
\left(\sum_b p_b\phi^{(2)}(s_b)\right)
\left(\sum_a c_a(\phi^{(2)})'(s_a)\right)=0
\]

holds everywhere. If the first factor vanishes but some activation derivative does not, its corresponding partial derivative p_a(phi^(2))'(s_a) is nonzero, since all p_a!=0. Such points are limits of points where the first factor does not vanish. If all derivatives vanish, the second factor already vanishes. Hence the second factor vanishes everywhere. Varying one coordinate and using nonconstancy of the derivative forces every c_a=0. This argument allows positive-measure zero sets of S and intervals on which the activation is flat. The required moments exist because phi^(2) has at most linear growth and Y is Gaussian.

The condition all labels nonzero is sufficient, not a necessary characterization. In fact V remains positive definite for any nonzero label vector: first vary coordinates whose labels vanish on a cylinder where S!=0, forcing their c_a to zero, and then use the preceding continuity argument on the active coordinates. Nevertheless all labels nonzero are useful and sufficient for the source's **per-input** first-layer activity proof. Do not replace that condition by merely y!=0 without revisiting the per-input argument.

## Reused Gaussian matrix audit

Source equation (6) is correct:

\[
P_a=\sum_cH_{0,c}^{(1)}[Q^{-1}\mathbb E(YU_a)]_c+\Gamma_a,
\qquad \operatorname{Cov}(\Gamma)=\sigma_2^2V,
\]

and Gamma is independent of the first population roots. In particular its covariance is the full sigma_2^2 V, not a covariance obtained by subtracting a projection of U onto Y.

For a finite explanation, write the initial first-layer calls as the columns of h and their outputs as y=W_0^(2)h. Conditioning on h,y gives

\[
W_0^{(2)}=yh^++\widetilde W P_{h^\perp}.
\]

Here the residual matrix is Gaussian and independent after conditioning. Each U column is a coordinate function of y. Thus W_0^(2)top U has conditional mean h(h^top h)^(-1)y^top U, and conditional covariance on its input-coordinate side is sigma_2^2(U^top U/n) tensor P_(h-perp). The projection removes only a fixed-dimensional input subspace; its normalized mean-square contribution goes to zero. Joint empirical convergence makes the normalized contractions deterministic. This yields the displayed population law with full V. It preserves the deterministic response caused by reuse; replacing the transpose by an independent matrix would discard that response.

Conditional on the first roots, B has noise coefficients diag((phi^(1))'(Z_0^(1)))Gamma. Consequently

\[
c^\top Dc\ge\sigma_2^2\lambda_{\min}(V)
\sum_ac_a^2\mathbb E[((\phi^{(1)})'(Z_{0,a}^{(1)}))^2]>0
\]

for c!=0. Every final expectation is positive because a nonconstant C1 function has nonzero derivative on an interval and each Gaussian marginal has full support.

The next forward call in source equation (11) is also correct. Set

\[
\alpha_a=Q^{-1}\mathbb E[H_0^{(1)}A_a],\quad
A_a^\perp=A_a-\sum_b\alpha_{a,b}H_{0,b}^{(1)},\quad
\beta_a=V^{-1}\mathbb E[PA_a^\perp].
\]

Then its marginal law is

\[
W_0^{(2)}A_a=\sum_b\alpha_{a,b}Y_b+
\sum_b\beta_{a,b}U_b+
\sigma_2\sqrt{\mathbb E[(A_a^\perp)^2]}\,\gamma_a,
\]

where gamma_a is independent of prior second-population coordinates. The finite conditional mean after additionally revealing W_0^(2)top U=P is obtained by adding U(U^top U)^(-1)P^top P_(h-perp). The remaining Gaussian matrix is projected on the left away from U and on the right away from h. Applying it to A_a^perp gives variance sigma_2^2 E[(A_a^perp)^2]; the fixed-rank output projection disappears in normalized mean square. Adaptivity of A_a to P is permitted because all these previous calls are conditioned upon. Independent gamma_a for different a are not asserted or required.

Conditional on the first roots, A_a has Gamma coefficient vector

\[
c_b=(\phi^{(1)})'(Z_{0,a}^{(1)})G_{ab}p_b(\phi^{(1)})'(Z_{0,b}^{(1)}).
\]

Its a-th entry is p_a((phi^(1))'(Z_(0,a)^(1)))^2 and is nonzero with positive probability. Therefore

\[
\mathbb E[(A_a^\perp)^2]\ge\mathbb E\operatorname{Var}(A_a\mid Z_0^{(1)})
=\sigma_2^2\mathbb E[c^\top Vc]>0.
\]

The learned-matrix term M_a is a function of Y, so it cannot cancel this fresh noise. In particular E[R_a^2]>=kappa_1^2 sigma_2^2 E[(A_a^perp)^2]>0. Also M_a!=0 in L2 because its coefficient vector against U has nonzero diagonal entry p_aQ_aa. Thus the middle matrix changes when applied to each initial H_(0,a)^(1).

## Strong-flow and nonlinearity checks

The assumed flow should be explicitly defined on [0,T_0], with the field integral equations holding in L2 and the middle equation in operator norm. Bounded continuous derivatives make the resulting vector field continuous along these paths: for example W^(3)(t)(phi^(2))'(Z^(2)(t)) is L2-continuous by splitting the W difference from multiplication of a fixed L2 field by bounded derivatives converging in probability. Rank-one operator products are continuous by the product of L2 norms. Hence the paths are continuously differentiable in the required norms.

No global Frechet differentiability of a Nemytskii map on L2 is needed. If v_t/epsilon_t ->v in L2, epsilon_t->0, and phi is C1 with bounded continuous derivative, split v_t/epsilon_t-v from the fixed direction v in the integral identity for phi(z+v_t)-phi(z). The first term is bounded by sup|phi'| times the L2 difference. In the second, bounded derivative differences converge in probability and are multiplied by fixed v in L2. Truncating v and then using bounded convergence proves

\[
\frac{\phi(z+v_t)-\phi(z)}{\epsilon_t}\longrightarrow\phi'(z)v\quad\text{in }L^2.
\]

This establishes every directional expansion above for unbounded activations too. Continuity of inner products justifies all kernel coefficients.

The first two kernel blocks begin at zero and have positive definite t^2 coefficients, because a positive definite D multiplied entrywise by a positive semidefinite G with diagonal one remains positive definite. Explicitly G=sum_j v_jv_j^top gives G circ D>=lambda_min(D) I. The same calculation proves Q circ V positive definite. The readout block is initially positive definite: varying individual coordinates in an identity sum_a c_a phi^(2)(Y_a)=0 forces c=0. It stays positive definite by continuity, and its weighted-label quadratic form has strictly positive t^2 coefficient. Thus each block and total K is nonconstant. The source does **not** claim monotonicity of every kernel entry or every residual magnitude.

A useful strengthened conclusion is that the actual activation fields move, not only their preactivations. Their leading coefficients are

\[
H_a^{(1)}(t)-H_{0,a}^{(1)}=2\kappa_1\kappa_3t^2A_a+o_{L^2}(t^2),
\]
\[
H_a^{(2)}(t)-H_{0,a}^{(2)}=2\kappa_3t^2(\phi^{(2)})'(Y_a)R_a+o_{L^2}(t^2).
\]

The first coefficient is nonzero by the conditional-variance argument. For the second, conditioning on prior second-population coordinates gives

\[
\mathbb E[((\phi^{(2)})'(Y_a)R_a)^2]
\ge\kappa_1^2\sigma_2^2\mathbb E[(A_a^\perp)^2]
\mathbb E[((\phi^{(2)})'(Y_a))^2]>0.
\]

Each corresponding RMS speed is proportional to t on a sufficiently short positive interval. The constants and smaller interval may depend on the fixed inputs and labels. No lower bound uniform near parallel inputs or zero labels is justified.

The best-affine-fit claim passes. Initially every hidden preactivation is a nondegenerate Gaussian, so nonaffinity and continuity prohibit zero affine-fit error. Along an L2-continuous path the first and second moments of Z and globally Lipschitz phi(Z) vary continuously. The regression formula is therefore continuous while Var(Z)>0, and both variance and error retain positive lower bounds on a short interval. This conclusion neither requires Gaussian marginals after training nor asserts that every distribution remains Gaussian.

## Tensor Programs III hypothesis check

The primary source is [Tensor Programs III, Setup 2.2, Theorem 2.10, Box 1, and Remarks 2.11–2.12](https://arxiv.org/pdf/2009.10685), checked directly on PDF pages 7–10 (printed 6–9), with local `/tmp/tp3src/NetsorT2.tex` as a second representation. For a fixed program, independent Gaussian matrices with entry variance sigma_W^2/n and iid jointly Gaussian vector roots give almost-sure empirical convergence for polynomially bounded coordinate functions and measurements. Singular root covariance is permitted; no extra rank-stability assumption remains. Box 1 gives covariance sigma_W^2 E[UV] and opposite-direction response coefficients. Formal differentiation follows the written program, with deterministic scalar coefficients fixed. Nondifferentiable coordinate functions are allowed via the covariance/pseudoinverse interpretation. This theorem does not control a growing number of time steps or itself construct continuous-time dynamics.

Application details: freeze a finite Euler mesh and its deterministic population residuals/contractions. The Gaussian first preactivations and Gaussian readout can be supplied as joint Gaussian roots, with a zero root represented by a degenerate Gaussian. Linear combinations, activations of at most linear growth, bounded activation derivatives, and coordinate multiplication are polynomially bounded. Finite composition preserves this condition. Every needed squared field or pairwise contraction is a polynomially bounded measurement. Reusing a matrix and its transpose is part of the theorem. Roots from different neuron populations can be placed in independent coordinate tuples; only same-population operations and measurements are subsequently used.

For C2 activations with bounded first and second derivatives, differentiation with respect to a matrix-innovation slot involves finitely many sums and products of polynomially bounded fields and bounded derivatives; those derivatives are integrable. No nonsingular Gaussian covariance is needed for the fixed-program theorem. Response estimates using derivatives should retain the literal causal recursion, rather than silently identifying distinct but correlated Gaussian slots.

### Scalar subGaussian root encoding

An arbitrary fixed scalar subGaussian law is also admissible as a *derived* root. Let F be its distribution function, let Phi be the standard Gaussian distribution function, and set T(g)=F^(-1)(Phi(g)), with generalized quantile. Then T(g) has the required law for g standard Gaussian. If P(|X|>s)<=C exp(-cs^2), the two tail bounds imply

\[
|T(g)|\le C_1\sqrt{\log\frac{C_2}{\min(\Phi(g),1-\Phi(g))}}
\le C_3(1+|g|).
\]

For the final inequality one may use the elementary lower bound 1-Phi(v)>=int_v^(v+1) exp(-s^2/2)ds/sqrt(2pi)>=exp(-(v+1)^2/2)/sqrt(2pi) for v>=0. Enlarging constants handles bounded s and the median. Hence T is a measurable, linearly bounded coordinate function, even for atomic or asymmetric laws. Supply independent Gaussian vectors, apply T coordinatewise, and run the fixed program. In particular any fixed iid subGaussian stored-readout law, independent of other initialization, is included. Iid scalar subGaussian first-weight entries are similarly encoded by d Gaussian roots per neuron, followed by d scalar transforms and the fixed input projections. These arguments do not change the Gaussian middle matrix hypothesis.

The root transform need not be differentiable: the response derivatives used in the training proof are with respect to matrix-generated Gaussian slots, while the independent initial root slots are held fixed. The fixed-program theorem itself imposes no continuity requirement on the transform. A vanishing readout scale depending on n is better handled as an initial perturbation of its zero-limit root; it is not a fixed coordinate function for purposes of Theorem 2.10.

### Finite-dimensional root tuples

If a more general joint root tuple X in R^q is wanted, with q fixed and each marginal subGaussian, it can also be encoded by finitely many Gaussian roots with a linearly bounded measurable map. Here is the argument rather than an appeal to middle-matrix universality. Its radius R=|X| has a subGaussian tail by the union bound. First sample R by its quantile at Phi(g_1). Conditional on R=r, sample the angular variable X/R on the unit sphere using Phi(g_2); choose a fixed direction when r=0. Such a measurable conditional sampler can be built by recursively splitting the sphere into countably many nested finite dyadic partitions: use the conditional masses to partition [0,1], retain the cell selected by the uniform number at each refinement, and take the unique limiting point. Conditional masses exist simultaneously for this countable collection; their consistency holds outside one null set of radii, on which the sampler can be assigned an arbitrary direction. The result is a measurable map T(g_1,g_2) with |T(g_1,g_2)|=F_R^(-1)(Phi(g_1))<=C(1+|g_1|). Coordinate functions of T therefore satisfy the polynomial-growth hypothesis. This gives exact sampling of an arbitrary fixed joint subGaussian law and preserves dependence within the tuple. Its polynomial-growth constant may depend on q, which is fixed for the convergence theorem; any claimed dataset-size-independent existence horizon must separately use marginal or weighted estimates.

The activity proof still needs its initial nondegeneracy conditions. Merely substituting arbitrary subGaussian first roots does not guarantee Q>0 or positive derivative moments; for instance a finitely supported first-root law can miss every interval where the derivative is nonzero. Gaussian initialization suffices automatically. General initial laws can be considered only with explicit checks of Q, V, derivative moments, and activation nonaffinity on the initial supports.

## Disposition

No substantive mathematical defect was found in the source activity proof. Its weighted version must change all training sums and the tested kernel direction as recorded above. Its scope must remain conditional on the independently proved strong flow, and restricted to two hidden layers and zero limiting stored readout for these onset formulas. The Tensor Programs III fixed-program input assumptions are satisfied for Gaussian roots and for the subGaussian derived-root constructions above. They give no automatic non-Gaussian middle-matrix universality and no mesh-uniform continuous-time theorem.
