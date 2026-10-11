# Nonparallel endpoint route: nonlinear lift and the remaining source-span condition

2026-10-11. Bounded positive proof attempt; internally derived partial result, not a promoted theorem.

## 1. Outcome and contract

The actual-network endpoint lower bound can be restarted at the second hidden matrix without any off-training-span hypothesis. A sufficient replacement is that the returned first-layer test feature retains a positive normalized distance from the **actual forward-query span of the finite training oracle**. Section 3 proves a quantified implication, with the original label cap and an eventual width threshold.

I have not proved this source-span condition from nonparallel input directions. The missing implication is precise: initialized augmented Gram positivity controls projection onto the \(m\) initial training feature vectors, whereas the endpoint proof requires projection onto the growing, adaptive collection of training Taylor-source vectors. These are different spaces. The first actual source jets and a full-span tanh approximation lemma below explain why an argument using only initial rank or the algebra of training ridge functions does not close that implication. Neither observation is a negative result about the requested full-span endpoint theorem.

The canonical model is

\[
z^{(1)}(v)=W^{(1)}v,\qquad
z^{(j)}(v)=W^{(j)}h^{(j-1)}(v),\qquad
h^{(j)}(v)=\phi_j(z^{(j)}(v)),\qquad
f_n(\sqrt d\,v)=n^{-1}w^\top h^{(L)}(v).
\]

The residuals are \(r_a=f_n(\sqrt d\,v_a)-y_a\), the loss is \(m^{-1}\sum_a r_a^2\), and the mobilities are \((n,1,\ldots,1,n)\). Initialization, normalized inputs, fixed depth \(L\ge2\), layerwise nonaffine strip-analytic activations, bounded strip derivatives, and unbounded activation values where allowed are unchanged. Set

\[
Y=\|y\|/\sqrt m>0,\qquad
\lambda=\gamma/m>0,\qquad
Y\le\lambda\beta^{-30L}.
\]

All data, labels, activations and the unit test direction \(v\) are fixed before \(n\to\infty\). The proposed extension assumes the training directions are pairwise nonparallel and \(v\) is nonparallel to each of them. It allows \(v\in S:=\operatorname{span}\{v_a\}\), including \(S=\mathbb R^d\).

Inputs used here are Section 2 of TEST_PANEL_DENSE_ROUTE.md and its off-span check; the canonical network and real fitting statements and proof in paper/compact.tex and paper/compact_fitting.tex; and the authorized general_nonlinear_endpoint_lower_20261010 finite-oracle, exact Gaussian-conditioning, projected-innovation, projected-scalar, and readout-moment modules. No other active route note, experiment, or altered architecture is used. The rigorous-proof, conjecture-investigation and canonical-notation skills govern the distinction between the proved implication and its open hypothesis.

## 2. Exact full-span conditional reduction

Let \(\mathcal T_n\) be the transcript of the specific finite Taylor-oracle algorithm from Section 6 of GELU_SILU_FLOW_ROUTE.md. Its returned parameters satisfy

\[
\|\widehat\theta_n-\theta_\infty\|_{\mathrm{par}}
\le C n^{-16}
\]

with probability tending to one. Its forward and transpose query spans for each initialized hidden matrix are \(V_j\) and \(U_j\), with a deterministic rank envelope

\[
\dim V_j,\dim U_j\le r_n
=O_{\mathrm{problem}}(\log(en)^{9/2})=o(n).
\]

For \(v\in S\), the returned first preactivation \(\widehat W^{(1)}v\), hence the vector \(\widehat h^{(1)}(v)\), is already \(\mathcal T_n\)-measurable. The first-layer training actions determine \(W_0^{(1)}v\) even when the list of training directions is linearly dependent. All learned first-layer increments are also known. There is therefore no conditionally fresh first-layer Gaussian to which the old first innovation lemma could be applied.

The exact two-sided Gaussian representation nevertheless survives:

\[
\widehat W^{(j)}
=A_j+(I-P_{U_j})G'_j(I-P_{V_j}),\qquad j\ge2,
\]

where the known parts and projections are transcript measurable and the residual matrices \(G'_j\) are conditionally independent, with independent \(N(0,1/n)\) entries. Define the decisive first-layer residual

\[
R_n(v):=
\frac{\|(I-P_{V_2})\widehat h^{(1)}(v)\|}{\sqrt n}.
\tag{1}
\]

Conditional on the transcript, the second preactivation is exactly

\[
\widehat z^{(2)}(v)
=A_2\widehat h^{(1)}(v)
+R_n(v)(I-P_{U_2})g_2,\qquad g_2\sim N(0,I_n).
\tag{2}
\]

Thus a fresh hidden Gaussian is still available when \(v\) lies in the input training span. Its scale is \(R_n(v)\), not the initial augmented Gram's Schur complement. For an off-span query the same formula holds after additionally exposing its first-layer query Gaussian; the present route concerns the full-span case, where no such extra exposure is needed.

## 3. Proved restart theorem, with a quantified failure term

Use the original measurable good-transcript conditions

\[
\max_{j\ge2}\|A_j\|_{\mathrm{op}}\le40,\qquad
\|\widehat w\|/\sqrt n\ge E:=Y/(4H),\qquad
\frac1n\sum_i\widehat w_i^4\le
M_4:=16\beta^{114L}(Ym/\gamma)^4+1.
\]

Here \(H=\max_{0\le j\le L}\sqrt{Q^{(j)}_{11}}\ge1\). Add the measurable condition

\[
\|\widehat h^{(1)}(v)\|/\sqrt n\le H_1:=3H.
\]

It has probability tending to one by real fitting, the returned parameter error, and the first activation's Lipschitz bound. These conditions are used for conditioning; the original full fitting and approximation events are used only to justify their probability and later transfer.

Fix \(0<\eta\le H_1\). On \(R_n(v)\ge\eta\), set \(\eta_1=\eta\). For \(2\le j\le L-1\), define recursively, with \(G_0\sim N(0,1)\),

\[
\begin{aligned}
c_j&=|\phi_j(0)|,\qquad s_j=\sup_{\mathbb R}|\phi_j'|,\\
B_j&=40H_{j-1},\qquad K_j=s_jH_{j-1},\\
\omega_j&=
\min_{\substack{|b|\le2B_j+1\\
u\in[\eta_{j-1}/\sqrt2,H_{j-1}]}}
\operatorname{Var}\phi_j(b+uG_0),\\
\eta_j&=\sqrt{\omega_j/32},\qquad
H_j=c_j+42s_jH_{j-1}.
\end{aligned}
\tag{3}
\]

The minima are positive by nonconstancy and compactness. Their intervals are nonempty: initially \(\eta\le H_1\); then Gaussian Poincare gives \(\omega_j\le s_j^2H_{j-1}^2\le H_j^2\), hence \(\eta_j\le H_j\). When \(L=2\), no recursive step is needed.

Apply the projected-innovation lemma to (2), then successively to the other lower query layers. At layer \(j\), the preactivation-removal and next feature-removal projectors have rank at most \(r_n\). For each fixed \(\eta>0\), all conditions

\[
r_n\le n/8,\qquad
r_n\le\omega_jn/(4K_j^2),\qquad
n\ge8K_j^2/\omega_j
\]

hold eventually. Conditional on a good transcript with \(R_n(v)\ge\eta\), the total lower-layer failure probability is at most

\[
\frac1n\sum_{j=2}^{L-1}
\left(\frac{32K_j^2}{\omega_j}+\frac29\right).
\tag{4}
\]

The empty sum is zero. On success, the final scalar representation has mean RMS at most \(B:=40H_{L-1}\) and fresh Gaussian scale in
\([\sigma_-,\sigma_+]=[\eta_{L-1},H_{L-1}]\).

For the final scalar module put

\[
\begin{aligned}
\mathcal R&=\max\{1,4B\sqrt{M_4}/E^2\},\\
d_{\mathcal R}&=
\min_{\substack{|a|\le\mathcal R\\u\in[\sigma_-/2,\sigma_+]}}
\left\{\operatorname{Var}\phi_L(a+uG_0)
-\big(\mathbb E[G_0\phi_L(a+uG_0)]\big)^2\right\},\\
v_0(\eta)&=d_{\mathcal R}E^2/16>0.
\end{aligned}
\tag{5}
\]

The positive Hermite-tail argument and the rank-defect condition are exactly those of the projected-scalar module. It gives, uniformly over the successful conditioning, a small-ball bound with leading term \(2c/\sqrt{2\pi v_0(\eta)}\) for radius \(c\) after multiplying the output by \(\sqrt n\), and remainder \(C_\eta n^{-1/4}\).

For the actual-endpoint transfer, both true and returned first-layer operator norms divided by \(\sqrt n\) are bounded on the high-probability fitting/approximation event. For any fixed unit \(v\),

\[
\|(\widehat W^{(1)}-W_\infty^{(1)})v\|/\sqrt n
\le\|\widehat\theta-\theta_\infty\|_{\mathrm{par}}.
\]

Forward subtraction with bounded hidden operators and Lipschitz activations, followed by subtraction of the normalized readout pairing, therefore gives

\[
|\widehat f_n(\sqrt d\,v)-f_n(\infty,\sqrt d\,v)|
\le C\|\widehat\theta-\theta_\infty\|_{\mathrm{par}}
=O(n^{-16}).
\tag{6}
\]

This deterministic estimate needs no off-span component and no fresh Gaussian at the first layer. It is invoked after, not inside, the Gaussian conditioning.

Averaging the small-ball estimate over an independent second run's endpoint, using radius \(2c\) for the approximant, and charging fitting/transfer failures yields the quantitative conclusion

\[
\begin{aligned}
\Pr\{&\text{both runs fit and }
|f_n(\infty,\sqrt d\,v)-\widetilde f_n(\infty,\sqrt d\,v)|
\ge c/\sqrt n\}\\
&\ge
1-\Pr\{R_n(v)<\eta\}
-\frac{4c}{\sqrt{2\pi v_0(\eta)}}
-C_\eta(n^{-1/4}+n^{-1})-o(1).
\end{aligned}
\tag{7}
\]

Here \(\eta>0\) is fixed before width tends to infinity. Constants may depend on the fixed problem, query and \(\eta\). Only the first run needs an auxiliary approximant.

In particular, the following condition is sufficient for the requested endpoint conclusion:

\[
\lim_{\eta\downarrow0}\limsup_{n\to\infty}
\Pr\{R_n(v)<\eta\}=0.
\tag{8}
\]

For each \(\delta>0\), first choose \(\eta\) so the eventual residual failure is at most \(\delta/4\), then take
\(c_\delta=\delta\sqrt{2\pi v_0(\eta)}/16\), and finally take \(n\) large enough for the remaining errors to be at most \(\delta/2\). A fixed deterministic lower bound for \(R_n(v)\) with probability tending to one would be stronger than needed.

This theorem neither strengthens the label cap nor changes the actual network. Its unresolved assumption is (8). Its width onset is eventual, not claimed polynomial in the listed parameters.

## 4. Exactly what the initialized augmented Gram supplies

Let

\[
T_n=[h_0^{(1)}(v_1),\ldots,h_0^{(1)}(v_m)],\qquad
q_n=h_0^{(1)}(v),\qquad
\mathcal U_n=\operatorname{range}T_n.
\]

Suppose the augmented empirical Gram converges in probability to a positive-definite matrix \(Q_{\mathrm{aug}}^{(1)}\). The separate initialized-rank route is responsible for proving this hypothesis from the specified nonparallel geometry; no such proof is assumed to prove anything about later sources.

Writing its blocks as \(Q_{TT},q_{Tv},q_{vv}\), positivity and continuity of inversion give

\[
\frac{\|(I-P_{\mathcal U_n})q_n\|^2}{n}
\ \xrightarrow{\mathbb P}\
s(v):=q_{vv}-q_{Tv}^{\top}Q_{TT}^{-1}q_{Tv}>0.
\tag{9}
\]

The finite oracle's initial forward evaluation ensures \(\mathcal U_n\subseteq V_2\). The resulting comparison is an **upper** bound,

\[
\operatorname{dist}(q_n,V_2)
\le\operatorname{dist}(q_n,\mathcal U_n),
\]

not the lower bound needed for (8). More explicitly, put

\[
e_n=(I-P_{\mathcal U_n})q_n,\qquad
\mathcal E_n=V_2\cap\mathcal U_n^\perp.
\]

Orthogonal decomposition gives the exact identity

\[
\frac{\operatorname{dist}(q_n,V_2)^2}{n}
=\frac{\|e_n\|^2}{n}
-\frac{\|P_{\mathcal E_n}e_n\|^2}{n}.
\tag{10}
\]

Initial positivity controls the first term. It provides no bound on the second, adaptive-source term. In addition, (1) involves the returned query feature rather than \(q_n\); the triangle inequality gives only

\[
R_n(v)\ge
\left(\frac{\|e_n\|^2-\|P_{\mathcal E_n}e_n\|^2}{n}\right)^{1/2}
-\frac{\|\widehat h^{(1)}(v)-q_n\|}{\sqrt n}.
\tag{11}
\]

The fitting displacement estimate bounds the last term by
\(8F_1Y^2/\lambda^{3/2}+o(1)\), in the notation of the fitting proof. This is a fixed small quantity, not a quantity tending to zero with width. The original cap depends on the training gap and not on \(s(v)\), which can tend to zero as a permissible test direction approaches a training direction. More importantly, even an extra query-dependent motion bound would leave the projection term in (10) uncontrolled.

## 5. Concrete actual-source calculation: the first nonzero jet

This calculation uses the actual fully trained model at arbitrary depth. Define the initialized diagonal gates and the readout-to-first-layer backward map by

\[
D_a^{(j)}=\operatorname{diag}\phi_j'(z_{a,0}^{(j)}),\qquad
B_a=D_a^{(1)}W_0^{(2)\top}D_a^{(2)}
\cdots W_0^{(L)\top}D_a^{(L)}.
\]

Because \(w(0)=0\), every hidden weight velocity and every hidden feature velocity vanishes at zero. The readout velocity is

\[
b_0:=\dot w(0)=\frac2m\sum_c y_c h_{c,0}^{(L)}.
\]

The exact backward response is a time-dependent version of \(B_a\) multiplied by \(w\). Its derivative at zero is therefore
\(\dot\delta_a^{(1)}(0)=B_ab_0\); the derivative of the backward map contributes zero because it multiplies \(w(0)\). Differentiating the canonical first-layer flow and using \(r_a(0)=-y_a\) gives

\[
\ddot W^{(1)}(0)=\frac2m\sum_a y_aB_ab_0v_a^\top.
\]

For every training direction \(v_b\), the chain rule consequently yields

\[
\ddot h_b^{(1)}(0)=
\frac2m\sum_a y_a(v_a^\top v_b)D_b^{(1)}B_ab_0.
\tag{12}
\]

The term involving \(\phi_1''\) vanishes because \(\dot z_b^{(1)}(0)=0\). These are the genuine degree-two first-layer forward jets queried by the finite Taylor algorithm once its order is at least three. They contain products of training-coordinate gates and hidden backward fields. Thus the actual source family is not described merely by the list of initialized ridge features.

For labels \(y=Y\xi\) with fixed shape \(\|\xi\|/\sqrt m=1\), (12) has the form \(Y^2 u_b\), where \(u_b\) depends on initialization, geometry and \(\xi\), but not on \(Y\). Whenever \(u_b\ne0\), its queried linear span contains that same direction for every \(Y>0\). Smallness of the jet's magnitude therefore gives no smallness of its normalized direction. This is a specific reason that the real fitting motion estimate, by itself, cannot control the additional projection in (10).

This calculation does not establish that the extra directions absorb the test residual. It identifies actual source vectors that a successful separation argument must handle.

## 6. A proved limitation of coarse ridge-algebra separation

One proposed structural bridge is to show that a nonparallel test ridge lies outside the closed span of all functions naturally generated by the training ridges. At the level of the full training-coordinate algebra, this is false even for an allowed activation. This does **not** identify that algebra with the actual temporal source span.

**Lemma.** Let \(g\sim N(0,I_d)\), let \(v\in\operatorname{span}\{v_a\}\), and take \(\phi_1=\tanh\). This activation is admissible: on \(|\operatorname{Im}z|<\pi/4\), the identity \(|\cosh(x+iy)|^2=\sinh^2x+\cos^2y\ge1/2\) gives \(|\tanh' z|\le2\), and there are no poles in that strip. Then

\[
\tanh(g^\top v)
\in\overline{
\mathbb R[\tanh(g^\top v_1),\ldots,\tanh(g^\top v_m)]
}^{\,L^2}.
\tag{13}
\]

No independence among the training projections is needed.

**Proof.** Choose fixed coefficients \(c_a\) with \(v=\sum_a c_av_a\), and set \(U_a=\tanh(g^\top v_a)\in(-1,1)\). Then

\[
\tanh(g^\top v)
=\tanh\!\left(\sum_a c_a\operatorname{arctanh}U_a\right).
\]

For \(0<\varepsilon<1\), clip each coordinate to \([-1+\varepsilon,1-\varepsilon]\) before applying \(\operatorname{arctanh}\). The resulting function \(F_\varepsilon\) is bounded by one and Lipschitz on the entire cube \([-1,1]^m\). Its values at \(U\) converge pointwise to the displayed test ridge as \(\varepsilon\downarrow0\); bounded convergence gives \(L^2\) convergence.

Each \(F_\varepsilon\) is uniformly approximable by polynomials on that cube. For completeness, after mapping the cube to \([0,1]^m\), its multivariate Bernstein polynomial is the expectation of \(F_\varepsilon\) at independent binomial-grid coordinates. Lipschitz continuity and the bound on their total variance give a uniform error at most a constant times \(\sqrt{m/N}\), where \(N\) is the binomial degree per coordinate. Hence these are genuine polynomial approximants with error tending to zero. Substituting \(U\), then letting \(\varepsilon\downarrow0\), proves (13).

Thus full-span nonparallel ridge independence at initialization does not imply a surviving component outside the closed training-coordinate algebra. For this activation, the relevant nonlinear feature lift is itself already a function of the training projections. Any successful argument must use a smaller and quantitatively controlled space tied to the **actual training-time source functions**.

The actual temporal span may be strictly smaller than this algebra. Neither (12) nor (13) proves that it is dense, or that (8) fails. Conversely, neither gives a nonzero distance from that temporal span.

## 7. Exact remaining implication

The open bridge is (8) for the particular finite Taylor transcript, or another demonstrably sufficient fresh-innovation construction for the same fully trained flow. Proving only an initial Gram gap, only a sublinear oracle rank, or only small hidden motion does not establish it. One needs a quantitative control of how the actual adaptive source directions project onto the test's nonlinear feature residual, accounting also for the returned first-layer motion.

What is proved here is the exact conditional reduction (2), the restarted endpoint estimate (7), the initialized-span distinction (9)–(11), the genuine source-jet formula (12), and the algebra-closure lemma (13). The requested nonparallel/full-span endpoint theorem remains open in this route. No stronger label condition, frozen hidden layers, width-dependent labels, polynomial onset, or negative full-span theorem is claimed.
