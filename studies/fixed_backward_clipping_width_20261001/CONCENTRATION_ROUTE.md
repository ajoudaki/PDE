# Fixed-clipping concentration route

This is a scoped theoretical derivation, not a promotion or a claim that the population-width target is proved. Its scientific inputs are the current `paper/main.tex`, `paper/results.tex`, the initialization portion of `paper/proof_alltime.tex`, and the relevant complete passages in `docs/index.qmd`, `docs/notation.qmd`, and `docs/02-gaussian-reuse.qmd` (especially A.1–A.3). No other study or sibling report was used. The solve-math-rigorously and investigate-conjectures skills, including their research-contract and adversarial-audit references, were read.

Supervisor feedback corrected an initial misreading of the clipping contract: this revised report uses the hard clip throughout. The earlier smooth-cap variant and its statement about the absence of an identity interval are superseded. The supervisor also requested an explicit verification of the Gaussian Poincare source; the cited A.3 passage does contain its proof, which is reproduced below in the precise bounded-Lipschitz form used here.

## Conclusion and exact scope

For every fixed positive hard clipping scale M, sufficiently small fixed labels, and an initial readout-feature Gram gap, the actual q=1 clipped two-hidden-layer flow has a width-independent, all-time initialization-to-prediction Lipschitz bound on a Gaussian initialization event of probability at least 1−C/n. The same argument gives an integrable-in-time bound for the Lipschitz constant of the prediction velocity. Consequently, for all sufficiently large n, one obtains an all-time n^−1/2 fluctuation bound around a deterministic finite-width center, and around the finite-width mean conditional on the good initialization event. This is stronger than fixed-time concentration.

It does **not** yield an n^−1/2 error to the actual infinite-width predictor. That conclusion still requires a quantitative population bias estimate. Concentration by itself also does not identify the population target or prove that the deterministic centers converge.

The all-time concentration proof below applies to every fixed test input and uniformly after integrating over a bounded input set. Its direct extension to a test law uses a fourth input moment, because the velocity sensitivity constant grows at most quadratically in the input norm. A merely finite second moment is not established by this route. Neither unconditioned all-time mean control outside the good event nor Gaussian exponential tails are asserted.

## 1. The actual clipped equations

Let φ=tanh, ψ=sech², and C_M(u)=max(−M,min(M,u)), applied coordinatewise. Fix m training inputs x_a∈R^d and labels y_a, and put G_ab=x_a^T x_b/d. All vector norms below are ordinary Euclidean norms, with every width normalization displayed. A pairing written out as u^T v/n is within one physical layer.

The evolving variables are A∈R^{n×d}, w∈R^n, v_a,k_a∈R^n, and τ∈R. Set

\[
 B=W_0+\frac1{mn}\sum_a v_a k_a^T,\quad
 \alpha_a=Ax_a/\sqrt d,\quad h_a=\phi(\alpha_a),\quad
 z_a=Bh_a,\quad g_a=\phi(z_a),\quad
 f_a=w^Tg_a/n,\quad r_a=f_a-y_a,\quad
 \rho=\|r\|_2/\sqrt m.
\]

The clipped residual-excluding backward signals are recursively

\[
 d_a=C_M(w\odot\psi(z_a)),\qquad
 \ell_a=C_M\bigl(\psi(\alpha_a)\odot B^Td_a\bigr).
\]

Thus the lower backward signal uses the already clipped upper signal, and B^T is the transpose of the same matrix B used forward. The ODE is

\[
 \dot A=-\frac2m\sum_a r_a\ell_a x_a^T/\sqrt d,\quad
 \dot w=-\frac2m\sum_a r_a g_a,\quad
 \dot v_a=-2r_a d_a,\quad
 \dot k_a=\frac\rho\tau(h_a-k_a),\quad \dot\tau=\rho.
 \tag{1}
\]

Initialize A_0 with independent N(0,1) entries, W_0=G_0/√n with independent standard Gaussian entries in G_0, independently of A_0, and w(0)=v_a(0)=0, k_a(0)=h_a(0), τ(0)=1. These k,v variables equal the paper's raw q=1 moments through k_a=\bar h_a/τ and v_a=−2\barδ_a. Clipping is a modification of the dynamics, not a proof-only truncation. The hard clip equals the identity on [−M,M]; in particular the upper clip is exactly inactive whenever ||w||_∞≤M.

For fixed n the vector field is locally Lipschitz, including at ρ=0. Moreover |g|,|h|≤1, |d|,|ell|≤M, and k remains a coordinatewise weighted average of values in [−1,1]. If u(t)=max_i|w_i(t)|, then ρ≤u+Y, where Y=||y||_2/√m, and the upper Dini derivative satisfies u'≤2(u+Y). Thus u≤Y(e^{2t}−1), and all other velocities have finite bounds on each finite interval. The flow exists for every finite time for every finite initialization. Its behavior as t→∞ outside the good event is not used.

The relevant clipping estimate is global. For F_M(p,z)=C_M(pψ(z)), the coordinate partial derivatives satisfy almost everywhere

\[
 |\partial_pF_M|\le1,\qquad
 |\partial_zF_M|
 \le2|p\psi(z)|\mathbf 1_{\{|p\psi(z)|<M\}}\le2M.
 \tag{2}
\]

Indeed ψ'(z)=−2tanh(z)ψ(z); on an unsaturated interval the derivative in z is therefore at most 2|pψ(z)|≤2M, and on a saturated interval it vanishes. Each coordinate restriction is locally absolutely continuous, including across clipping corners. Integrating these almost-everywhere derivative bounds separately in p and z proves |F_M(p,z)−F_M(p',z')|≤|p−p'|+2M|z−z'|. Thus F_M is jointly globally Lipschitz with constants (1,2M). No differentiability of the hard clip at ±M is assumed or subsequently needed.

## 2. Good initialization and finite activity

Assume the deterministic initial top-feature covariance satisfies Q^(2)/m≽2λI_m for some λ>0. Fix K_0 sufficiently large. Define

\[
 \mathcal G_n=\{\|W_0\|_{op}\le K_0,\quad
 \Gamma_0:=(g_a(0)^Tg_b(0)/(mn))_{a,b}\succeq\lambda I_m\}.
 \tag{3}
\]

For this bounded smooth activation,

\[
 \Pr(\mathcal G_n^c)\le C/n.
 \tag{4}
\]

Here are sufficient quantitative details, avoiding an unquantified law of large numbers. The empirical first-feature covariance Q_{1,n} has mean Q^(1) and mean-square Frobenius error at most m²/n, since its entries are averages of bounded iid variables. Given A_0, the second preactivation rows are iid N(0,Q_{1,n}), and the second feature covariance has conditional mean T(Q_{1,n}) and conditional mean-square error at most m²/n. For T_ab(Q)=E[tanh(Z_a)tanh(Z_b)], Gaussian interpolation gives

\[
 T_{ab}(Q)-T_{ab}(Q')
 =\frac12\int_0^1\sum_{ij}(Q-Q')_{ij}
 E[\partial_{ij}(\tanh Z_a\tanh Z_b)]\,ds,
\]

where Z has covariance Q'+s(Q−Q'). The Hessian is bounded, so T is Lipschitz in Frobenius norm with a constant depending only on m. The identity follows first for positive definite covariances by differentiating their densities and integrating by parts twice, and for singular covariances by adding εI and bounded convergence. Consequently E||Γ_0−Q^(2)/m||_op²≤C/n. Markov's inequality proves the Gram part of (4). The initialized matrix norm estimate in Gaussian-reuse A.3 gives P(||W_0||_op>K_0)≤C/n as well.

For clarity, the small-label fitting estimate needed below can be derived directly for (1). Put S(t)=∫_0^tρ. Until S reaches a fixed small s_*, contraction |C_M(u)|≤|u| gives

\[
 \|w\|_\infty\le2S,\quad
 \|v_a\|_\infty\le2\sqrt m S^2,\quad
 \|k_a\|_\infty\le1,\quad 1\le\tau\le1+S,
\]
\[
 \|B-W_0\|_F\le2\sqrt m S^2,\qquad
 \|\ell_a\|_2/\sqrt n\le2\|B\|_{op}S.
 \tag{5}
\]

For example |dot v_ai|≤2√mρ·2S, whose integral is 2√mS². The first-weight velocity is at most CSρ in normalized Frobenius norm. Differentiating B in (1) shows ||dot B||_F≤C(S+S²)ρ, since ||dot k_a||_2/√n≤2ρ/τ. Therefore ||dot g_a||_2/√n≤CSρ while S≤s_*≤1. The top-feature Gram changes by at most CS². The exact prediction derivative gives

\[
 \dot r=-2\Gamma(t)r+e(t),\qquad
 \|e(t)\|_2/\sqrt m\le CS(t)^2\rho(t),
 \quad \Gamma_{ab}=g_a^Tg_b/(mn).
 \tag{6}
\]

Choose s_* so the Gram drift and the last term leave a strictly positive contraction rate κ. Taking Y small enough that Y/κ<s_*/2 then closes the activity bootstrap:

\[
 \rho(t)\le Ye^{-\kappa t},\qquad
 S(\infty)\le Y/\kappa<s_*/2.
 \tag{7}
\]

The constants in this fitting calculation may be chosen independent of M, since only contraction of clipping was used. The sensitivity constants below do depend on fixed M. This verifies the finite-activity premises rather than assuming fitting from clipping alone.

## 3. Exact residual kernels and why their Lipschitz bounds close

Let p_b=w⊙ψ(z_b), which is the **ordinary derivative of the output**, not a clipped training signal. Define scalar matrices

\[
 K^0_{ba}=g_b^Tg_a/n,
\]
\[
 K^A_{ba}=G_{ab}\,p_b^TB(\psi(\alpha_b)\odot\ell_a)/n,
\]
\[
 K^v_{ba}=(p_b^Td_a/n)(k_a^Th_b/n),
\]
\[
 Q_b=\frac1{m\tau}\sum_a(p_b^Tv_a/n)
                 ((h_a-k_a)^Th_b/n).
\]

Directly differentiating f_b and the reconstructed B gives the exact identity

\[
 \dot r_b=-\frac2m\sum_a r_a
       (K^0_{ba}+K^A_{ba}+K^v_{ba})+\rho Q_b.
 \tag{8}
\]

On the tube (5), K^A,K^v=O(s_*²) and Q=O(s_*³), in fixed m-dimensional norms. More importantly, these kernels are Lipschitz in normalized state distance with width-independent constants C_M.

The potentially problematic term is K^A. Writing it as a scalar contraction of p_b with B(ψ(α_b)⊙ell_a) avoids taking an infinity norm of B^Tp_b. Indeed ell_a is coordinatewise bounded by M, w is bounded by 2s_*, B has bounded operator norm, and (2) bounds changes of ell_a in normalized Euclidean norm. Thus the change of ψ(α_b)⊙ell_a is bounded by the change of ell_a plus 2M times the change of α_b. Every remaining factor in this contraction is controlled in normalized Euclidean norm. This is the place where fixed clipping closes the width-independent estimate despite reuse of the Gaussian matrix and its transpose.

## 4. All-time pairwise stability

Compare two initializations in G_n with the same data and labels. A superscript j=1,2 denotes their trajectories. Set ε=||W_0^1−W_0^2||_op and

\[
 D=\|A^1-A^2\|_F/\sqrt n+\|w^1-w^2\|_2/\sqrt n
 +\sum_a(\|v_a^1-v_a^2\|_2+\|k_a^1-k_a^2\|_2)/\sqrt n
 +|\tau^1-\tau^2|,\quad E=D+\varepsilon,
\]
\[
 R=\|r^1-r^2\|_2/\sqrt m.
\]

Reconstruction gives ||B^1−B^2||_op≤C E. Subtracting (1), using (2), and separating coefficient changes from residual changes gives, in upper Dini derivatives,

\[
 D'\le C_M\rho^1 E+C_MR.
 \tag{9}
\]

For the residual difference, subtract (8), retaining −2Γ^1(r^1−r^2) as the coercive term. The other terms multiplying r^1−r^2 or ρ^1−ρ^2 have norm at most Cs_*², by the smallness estimates after (8). All coefficient differences multiplying r^2 or ρ^2 have norm at most C_M E. Reducing s_* if necessary yields

\[
 R'\le-\kappa_1R+C_M\rho^2E,\qquad R(0)=0,
 \tag{10}
\]

where κ_1>0 is independent of width and time. No derivative of r/ρ is used.

Integrating (10) first yields ∫_0^tR≤(C_M/κ_1)∫_0^tρ^2E. Substituting in the integral form of (9), and applying scalar Gronwall with the integrable coefficient C_M(ρ^1+ρ^2), proves

\[
 \sup_{t\ge0}E(t)\le C_ME(0).
 \tag{11}
\]

Using (7) once more in the convolution form of (10), for some c>0,

\[
 R(t)\le C_M(1+t)e^{-ct}E(0).
 \tag{12}
\]

The initialization k_a(0)=tanh(A_0x_a/√d) is Lipschitz in A_0, so E(0)≤C(||A_0^1−A_0^2||_F/√n+||W_0^1−W_0^2||_op). Since W_0=G_0/√n, this is bounded by C/√n times the Euclidean distance between all standard Gaussian root coordinates (A_0,G_0).

For any passive query x, define α_x,h_x,z_x,g_x by the same trained A,B and let f(t,x)=w^Tg_x/n. Formula (11) implies

\[
 \sup_{t\ge0}|f^1(t,x)-f^2(t,x)|
 \le C_M(1+\|x\|/\sqrt d)E(0).
 \tag{13}
\]

Replacing the output index b by x in (8) gives an exact query-velocity formula. Its scalar kernels are again Lipschitz, but the simple bound now grows quadratically in ||x||/√d: G_ax contributes one power and the change of ψ(Ax/√d) can contribute another. Equations (7), (11), and (12) consequently give

\[
 |\dot f^1(t,x)-\dot f^2(t,x)|
 \le C_M(1+\|x\|^2/d)(1+t)e^{-ct}E(0).
 \tag{14}
\]

This estimates the actual time derivative of the query prediction, not a discretization. A separate direct estimate gives |dot f(t,x)|≤C(1+||x||/√d)Ye^{−κt} on G_n.

## 5. All-time concentration with a precisely specified center

Let Z collect the standard Gaussian roots. On the closed good set G_n, a_x(t,Z)=dot f_n(t,x) is Lipschitz in Z with constant

\[
 L_x(t)/\sqrt n,\qquad
 L_x(t)=C_M(1+\|x\|^2/d)(1+t)e^{-ct}.
\]

Extend a_x(t,·) from G_n to all Gaussian root space by the scalar McShane extension, and clip that extension to the interval ±C(1+||x||/√d)Ye^{−κt}. The clipping does not change its values on G_n or increase its Lipschitz constant. Denote the result by a_x^ext. One can take the McShane infimum over a fixed countable dense subset of G_n; the restriction is continuous, so this produces a jointly measurable function of t,x,Z. Define

\[
 F_n^{ext}(t,x)=\int_0^t a_x^{ext}(s,Z)\,ds,
 \qquad c_n(t,x)=E F_n^{ext}(t,x).
 \tag{15}
\]

On G_n, this is exactly f_n(t,x), because the actual initial prediction is zero. The center c_n is deterministic and may depend on n and the specified extension.

Gaussian Poincare, in the exact Lipschitz form proved in Gaussian-reuse A.3, states that Var b(Z)≤L² for an L-Lipschitz real function b of any finite standard Gaussian vector. Here is the needed contained proof. For bounded smooth b with bounded gradient, define the Ornstein–Uhlenbeck semigroup P_s b(z)=E[b(e^{−s}z+√(1−e^{−2s})Z')], with Z' an independent standard Gaussian vector. Gaussian integration by parts and differentiation under the bounded integrals give

\[
 -\frac d{ds}E[(P_sb)(Z)^2]=2E\|\nabla P_sb(Z)\|_2^2,
 \qquad \nabla P_sb=e^{-s}P_s\nabla b.
\]

As s→∞, P_s b(z)→Eb(Z), by dominated convergence. Integrating the first identity and using the second, Jensen's inequality, and Gaussian invariance gives

\[
 \operatorname{Var}b(Z)
 =2\int_0^\infty E\|\nabla P_sb(Z)\|_2^2ds
 \le2\int_0^\infty e^{-2s}E\|\nabla b(Z)\|_2^2ds
 \le L^2.
\]

For bounded L-Lipschitz b, smooth convolution preserves the Lipschitz constant and converges uniformly to b; its variances converge, proving the same bound without pointwise differentiability of b. All these hypotheses hold for each bounded a_x^ext(t,·). Consequently

\[
 \operatorname{Var}(a_x^{ext}(t,Z))\le L_x(t)^2/n.
\]

The crucial all-time step is integration of velocities, not a union bound over separate time marginals. Pathwise,

\[
 \sup_{t\ge0}|F_n^{ext}(t,x)-c_n(t,x)|
 \le\int_0^\infty|a_x^{ext}(s,Z)-Ea_x^{ext}(s,Z)|\,ds.
\]

Minkowski's integral inequality and the preceding variance bound prove

\[
 E\sup_{t\ge0}|F_n^{ext}(t,x)-c_n(t,x)|^2
 \le\frac1n\left(\int_0^\infty L_x(s)\,ds\right)^2
 \le\frac{C_M(1+\|x\|^2/d)^2}{n}.
 \tag{16}
\]

For the actual flow this implies, for every η>0,

\[
 \Pr\{\sup_{t\ge0}|f_n(t,x)-c_n(t,x)|>\eta\}
 \le C/n+C_{M,x}/(n\eta^2).
 \tag{17}
\]

No concentration statement for a Banach-valued Gaussian map has been assumed. Equations (14)–(16) supply the missing control of the temporal supremum explicitly.

One may also use the true conditional finite-width mean

\[
 m_n^{good}(t,x)=E[f_n(t,x)\mid G_n].
\]

The extension has an all-time absolute bound C(1+||x||/√d)Y, and equals the actual trajectory on G_n. Therefore sup_t|c_n−m_n^good|≤C_x P(G_n^c)=O_x(n^−1), and (16) implies

\[
 E[\sup_{t\ge0}|f_n(t,x)-m_n^{good}(t,x)|^2\mid G_n]
 \le C_{M,x}/n.
 \tag{18}
\]

The unconditioned mean E f_n(t,x) is well defined at every fixed finite t, using the deterministic bound Y(e^{2t}−1). On each fixed horizon it differs from the extension mean by O_T(P(G_n^c)), so concentration around that unconditioned finite-width mean also holds on each compact horizon. The constants obtained this way are not uniform in time. Uniform all-time control of the actual unconditioned mean requires additional control outside G_n.

Integrating (16) over any test law with ∫||x||⁴dμ<∞ gives the paper's placement of the supremum inside the integral:

\[
 E\int\sup_{t\ge0}|F_n^{ext}(t,x)-c_n(t,x)|^2\,d\mu(x)
 \le C_{M,\mu}/n.
 \tag{19}
\]

The corresponding actual-flow statement holds on G_n. This includes circles, spheres, and any bounded input domain. Equation (19) is an integrated bound, not a supremum over a continuum of x. A spatial supremum would require an additional entropy or spatial-derivative argument.

## 6. The remaining population-rate obligation

For the actual fixed-M clipped population predictor f_M, the exact necessary decomposition is

\[
 f_n-f_M=(f_n-c_n)+(c_n-f_M).
 \tag{20}
\]

The first term is O_P(n^−1/2) in the all-time metrics established above. The second is a deterministic population-identification/bias term. Even if a separate theorem proves c_n→f_M, it does not give the missing rate. The scalar example X_n=n^−1/4+n^−1/2tanh(Z) has root-width fluctuations and converges to zero, but its error to zero is not root width. This is a logical counterexample to inferring a population rate from concentration and convergence, not a counterexample to the clipped neural dynamics.

A completion would need, for example,

\[
 \left(\int\sup_{t\ge0}|c_n(t,x)-f_M(t,x)|^2d\mu(x)\right)^{1/2}
 \le C_{M,\mu}/\sqrt n,
\]

for the population process obtained from the same A_0,W_0 reuse, the same transpose, and the same clipping placement. Fixed finite-program Gaussian laws and qualitative ODE passage can identify a limit, but give no such rate without estimates uniform under time-mesh refinement. Replacing the reused matrix by independent forward/backward Gaussian maps, identifying the center with its limit by definition, or invoking exponential fitting alone would each skip this obligation.

The bounded route therefore closes all-time stability and centered root-width fluctuations on the small-label event. It leaves quantitative bias, full population identification if not supplied separately, the merely-second-moment test-law extension, and an all-time unconditional-mean statement unproved. The main unresolved obligation for the requested n^−1/2 population prediction rate is the quantitative bias estimate in (20).
