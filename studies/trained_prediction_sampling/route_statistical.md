# Statistical route: integrated forcing and a degenerate interaction kernel

**Status:** conditional theorem with a complete probabilistic argument; the neural-dynamics hypotheses listed below remain open under the supplied facts. This is an independent candidate for supervisor checking, not an internally checked or established result.

**Input scope:** the supervisor's self-contained assignment only. No study artifacts, established scientific text, other routes, external scientific sources, or Git history were read. Required process inputs were `AGENTS.md`, `RESEARCH_WORKFLOW.md`, the `solve-math-rigorously` and `investigate-conjectures` skills, and the latter's research-contract, adversarial-audit, and proof-search-orchestration references. No experiments or Git operations were performed. Only this assigned report was written.

## 1. Target and strongest conclusion

Let \(\mathcal Z=\mathbb S^1\times[-Y,Y]\), let \(P\) be any Borel probability on \(\mathcal Z\), and let \(P_m=m^{-1}\sum_{i=1}^m\delta_{Z_i}\), where the \(Z_i\) are iid with law \(P\), independent of initialization. The requested map is the prediction at actual trained time \(T=40\), \(F(P)\in H=L^2(\mathbb S^1)\). The target is a centered influence \(I_P\in L^2(P;H)\) from the nonlinear dynamics and

\[
 F(P_m)-F(P)=\frac1m\sum_{i=1}^m I_P(Z_i)+r_m,
 \qquad \sqrt m\,r_m\longrightarrow0\quad\text{in probability},
\]

followed by the Hilbert-space CLT and, if possible, \(m\mathbb E\|r_m\|_H^2\to0\). The endpoint time is fixed before the sample limit; no finite-width/sample joint limit is asserted.

The useful mechanism found here is that the empirical derivative acting on the first response is a **doubly centered two-sample kernel**. Its size is \(O_{L^2}(m^{-1})\). One need not prove operator-norm convergence of empirical derivatives or uniform Fréchet differentiability of the endpoint map over laws. This removes a real empirical-process requirement, but does not supply the missing stability and Taylor estimates for the actual state evolution.

Two additional conclusions are derived directly from the supplied architecture: its population forcing has a bounded raw-state norm on finite reached trajectories, and its prediction observable has a Taylor remainder of order \(\|\delta\theta\|_E^{2-2/p}\) under uniform \(Q\in L^p\), \(p>2\). Uniform sub-Gaussian \(Q\) improves the latter to \(O(\|\delta\theta\|_E^2\sqrt{\log(e/\|\delta\theta\|_E)})\). The decisive remaining obstacle is the state response, not the last prediction map or the Hilbert CLT.

The assertion for every Borel \(P\) is still open. Bounded continuity of \(F\) and finite-width identification only on a neighborhood \(U\) do not establish the existence or identification of \(F(P)\) outside \(U\), much less any derivative there.

## 2. Actual vector field and its first-response candidate

Write a datum as \(a=(u,y)\), reserving \(\zeta\) for the second preactivation. The latent spaces are probability spaces, as in the mean-field interpretation. The raw state space is

\[
 E=L^2(\Omega_1;\mathbb R^2)\oplus
   \operatorname{HS}(H_1,H_2)\oplus L^2(\Omega_2),
 \qquad \theta=(w,K,c),\quad A=A_0+K.
\]

Here \(A_0:H_1\to H_2\) is the supplied bounded initialized action, and its actual adjoint is used. Put

\[
 h=\phi(w\cdot u),\quad \zeta=Ah,\quad b=\phi(\zeta),\quad
 d=c\phi'(\zeta),\quad Q=A^*d,\quad
 f=\langle c,b\rangle,\quad e=f-y,
 \qquad \phi=\tanh.
\]

The vector field for one observation is

\[
 G(\theta,a)=-2\bigl(e\phi'(w\cdot u)Qu,
                         e\,d\otimes h,
                         e\,b\bigr),
 \qquad \dot\theta_P=P G(\theta_P,\cdot),
 \quad \theta_P(0)=(g,0,0).
\]

All responses below are around the **trained population path** \(\theta_P(t)\). They retain the changing features, kernel, and readout. There is no frozen-feature replacement.

For a direction \(v=(v_w,v_K,v_c)\), the algebraic first variations are

\[
\begin{aligned}
 h_v&=\phi'(w\cdot u)(v_w\cdot u),\\
 \zeta_v&=v_Kh+Ah_v, & b_v&=\phi'(\zeta)\zeta_v,\\
 d_v&=v_c\phi'(\zeta)+c\phi''(\zeta)\zeta_v,
 & Q_v&=v_K^*d+A^*d_v,\\
 f_v&=\langle v_c,b\rangle+\langle c,b_v\rangle.
\end{aligned}
\]

Thus the candidate \(J_t(a)v=D_\theta G(\theta_P(t),a)v\) is

\[
-2\begin{pmatrix}
 f_v\phi'(w\cdot u)Qu+
 e\{\phi''(w\cdot u)(v_w\cdot u)Q+\phi'(w\cdot u)Q_v\}u\\
 f_v d\otimes h+e(d_v\otimes h+d\otimes h_v)\\
 f_v b+e b_v
\end{pmatrix}.
\tag{2.1}
\]

This is an algebraic formula on directions for which every product belongs to the specified space. It is **not** a claim that \(J_t(a)\) is a bounded operator on all of \(E\).

If the actual population linear response is well posed, set

\[
 L_t=P J_t,\qquad g_t(a)=G(\theta_P(t),a),
\]

and define \(v_t(a)\) by

\[
 \dot v_t(a)=L_tv_t(a)+g_t(a)-Pg_t,
 \qquad v_0(a)=0.
\tag{2.2}
\]

The derivative of the prediction observable \(\Phi(\theta)(u)=f_\theta(u)\) is

\[
 (B_tv)(u)=\langle v_c,b\rangle+
            \langle d,v_Kh\rangle+
            \langle Q,\phi'(w\cdot u)(v_w\cdot u)\rangle.
\tag{2.3}
\]

The influence candidate is

\[
 I_P(a)=B_Tv_T(a).
\tag{2.4}
\]

The next sections give precise sufficient conditions under which this candidate is an actual contamination derivative and is the first term of the sample expansion. Neither assertion is inferred from formal differentiation alone.

## 3. Abstract dynamic conditions that suffice

Fix \(P\) and \(T<\infty\). Constants may depend on \(P,T\), initialization, and the chosen state norm, but not on \(m\). Let \(X\) be a separable Hilbert space controlling the state errors; it may be \(E\) if the required estimates hold there. If another space is used, its embedding into the raw state and all products in (2.1) must be proved. Define

\[
 \mathscr X=L^2([0,T];X),\qquad
 \delta_m(t)=\theta_{P_m}(t)-\theta_P(t),\qquad
 D_m(t)=\sup_{s\le t}\|\delta_m(s)\|_X.
\]

Here are explicit sufficient conditions. They concern source estimates and reached trajectories, rather than differentiability of a map on a whole neighborhood of probability laws.

**D1. Actual solutions and integrated forcing.** The actual population and empirical solutions exist through \(T\), share initialization, and their difference is a continuous \(X\)-valued path. The function \(a\mapsto g_\cdot(a)\) is strongly measurable and belongs to \(L^2(P;\mathscr X)\). Equations and source integrals below hold in \(X\), at least in the mild sense. Measurability of the endpoint statistic is included.

**D2. Linear response and empirical propagation.** The population problem with operator \(L_t=PJ_t\) has an evolution \(U_P(t,s)\) on \(X\) satisfying \(\sup_{s\le t\le T}\|U_P(t,s)\|\le S_P<\infty\). For \(L_{m,t}=P_mJ_t\), the zero-initial-value equation \(\dot x=L_{m,t}x+q\) is well posed for the sources used below and satisfies, on every prefix,

\[
 \sup_{s\le t}\|x(s)\|_X
       \le S_m\int_0^t\|q(s)\|_X\,ds,
 \qquad S_m=O_{\mathbb P}(1).
\tag{3.1}
\]

Boundedness of every \(J_t(a)\) on \(X\) is sufficient, but is not required by this formulation. If unbounded operators are used, domains, the evolution, and the asserted mild identities must actually be justified; the notation does not solve those questions.

**D3. A reached-chord Taylor estimate.** Let

\[
 R_m(t)=P_m\{G(\theta_{P_m}(t),\cdot)
                     -G(\theta_P(t),\cdot)-J_t(\cdot)\delta_m(t)\}.
\]

For some fixed \(r>0\), \(\alpha>0\), and \(C_m=O_{\mathbb P}(1)\), whenever \(D_m(t)\le r\),

\[
 \int_0^t\|R_m(s)\|_X\,ds\le C_mD_m(t)^{1+\alpha}.
\tag{3.2}
\]

It is enough to prove this along actual population/empirical trajectory pairs. A uniform Taylor theorem on all ambient state-space directions is unnecessary. A quadratic estimate corresponds to \(\alpha=1\).

**D4. A two-sample response kernel, including its diagonal.** Formula (2.2) defines

\[
 v_t(a)=\int_0^t U_P(t,s)[g_s(a)-Pg_s],ds.
\tag{3.3}
\]

The products \(J_t(a)v_t(b)\) are well defined and strongly measurable, and all necessary Bochner integrals can be interchanged. In particular require

\[
 \int J_t(a)v_t(b)\,P(db)=0
 \quad\text{for }P\text{-almost every }a
 \quad\text{in the relevant time-space sense}.
\tag{3.4}
\]

For bounded linear \(J_t(a)\), (3.4) follows from \(Pv_t=0\); for unbounded operators it is a genuine domain/integration requirement. Define the \(\mathscr X\)-valued kernel

\[
 k_t(a,b)=J_t(a)v_t(b)-\int J_t(c)v_t(b)\,P(dc).
\tag{3.5}
\]

Require

\[
 \mathbb E\|k(Z,Z')\|_{\mathscr X}^2<\infty,
 \qquad
 \mathbb E\|k(Z,Z)\|_{\mathscr X}^2<\infty,
\tag{3.6}
\]

where \(Z,Z'\) are independent with law \(P\). The diagonal assumption is separate: for nonatomic \(P\), integrability under \(P\otimes P\) says nothing about values on the diagonal. For the probability-only result its second moment can be weakened to \(\mathbb E\|k(Z,Z)\|_{\mathscr X}<\infty\).

**D5. The actual observable.** For a bounded linear \(B_T:X\to H\), some \(\beta>0\), and a constant \(C_\Phi\), the actual endpoint chords satisfy, when \(\|\delta_m(T)\|_X\le r\),

\[
 \|\Phi(\theta_P(T)+\delta_m(T))-
      \Phi(\theta_P(T))-B_T\delta_m(T)\|_H
       \le C_\Phi\|\delta_m(T)\|_X^{1+\beta}.
\tag{3.7}
\]

More generally, an \(o(\|\delta\|_X)\) deterministic modulus is enough for the probability conclusion. Section 7 verifies a quantitative version in raw \(E\) from the supplied moment information.

These conditions are checkable dynamic estimates, but D2--D4 are major unproved obligations for the target. They are not claimed to follow from endpoint continuity or finite latent moments.

## 4. Proof of the sample expansion

### 4.1 The source has the ordinary sample scale

Put \(\Delta_m=P_m-P\) and

\[
 A_m=\int_0^T\|\Delta_mg_t\|_X\,dt.
\]

Independence, centering, and the Hilbert norm give

\[
 \mathbb E\|\Delta_mg\|_{\mathscr X}^2
  =\frac1m\mathbb E\|g(Z)-Pg\|_{\mathscr X}^2,
 \qquad A_m^2\le T\|\Delta_mg\|_{\mathscr X}^2.
\tag{4.1}
\]

Consequently \(A_m=O_{\mathbb P}(m^{-1/2})\). There is no supremum over an arbitrary function class or empirical-process entropy assumption here.

### 4.2 A local bootstrap proves the state rate

The exact difference equation is

\[
 \dot\delta_m=L_{m,t}\delta_m+\Delta_mg_t+R_m(t),
 \qquad \delta_m(0)=0.
\tag{4.2}
\]

On any prefix on which \(D_m(t)\le r\), D2--D3 imply

\[
 D_m(t)\le S_m\{A_m+C_mD_m(t)^{1+\alpha}\}.
\tag{4.3}
\]

Fix \(\varepsilon>0\). Tightness gives a finite \(K\ge1\) such that \(S_m,C_m\le K\) with probability at least \(1-\varepsilon\) for all sufficiently large \(m\). Choose

\[
 d=\min\{r/2,(2K^2)^{-1/\alpha}\}.
\]

On that event and \(A_m<d/(4K)\), a first time with \(D_m(t)=d\) would give from (4.3)

\[
 d\le KA_m+K^2d^{1+\alpha}<d/4+d/2,
\]

a contradiction. Hence \(D_m(T)<d\) and (4.3) gives \(D_m(T)\le2KA_m\). Since the source threshold fails with probability tending to zero and \(\varepsilon\) is arbitrary,

\[
 D_m(T)=O_{\mathbb P}(m^{-1/2}).
\tag{4.4}
\]

This argument does not infer a small solution from an algebraic inequality with two branches: continuous paths starting at zero and the first-exit argument rule out the large branch.

### 4.3 The empirical first response

Define

\[
 \xi_m(t)=\frac1m\sum_{i=1}^m v_t(Z_i).
\]

By (3.3), \(Pv_t=0\), \(\dot\xi_m=L_t\xi_m+\Delta_mg_t\), and \(\xi_m(0)=0\). Let \(\eta_m=\delta_m-\xi_m\). Subtracting this equation from (4.2) gives the exact residual equation

\[
 \dot\eta_m=L_{m,t}\eta_m+
                (P_m-P)J_t\xi_m+R_m(t),
 \qquad \eta_m(0)=0.
\tag{4.5}
\]

The mixed empirical term is

\[
 (P_m-P)J_t\xi_m
       =\frac1{m^2}\sum_{i,j=1}^m k_t(Z_i,Z_j).
\tag{4.6}
\]

Both marginals of \(k\) vanish: the first by its definition, and the second by (3.4). This is the source of the extra factor \(m^{-1/2}\) beyond an ordinary sample average.

### 4.4 Direct bound for the degenerate kernel

Let \(K_m=m^{-2}\sum_{i,j}k(Z_i,Z_j)\in\mathscr X\). Separate indices \(i\ne j\) from the diagonal. In the expansion of

\[
 \mathbb E\Big\|\sum_{i\ne j}k(Z_i,Z_j)\Big\|_{\mathscr X}^2,
\]

two summands with disjoint index sets have zero inner-product expectation by independence and centering. Summands sharing exactly one index also have zero expectation: condition on the shared sample and use the zero appropriate marginal for the other two independent samples. Only the identical ordered pair or its reversal can survive. Cauchy--Schwarz bounds each surviving expectation by \(\mathbb E\|k(Z,Z')\|_{\mathscr X}^2\). There are at most \(2m(m-1)\) such terms. For the diagonal, Jensen's inequality gives

\[
 \mathbb E\Big\|m^{-2}\sum_i k(Z_i,Z_i)\Big\|_{\mathscr X}^2
       \le m^{-2}\mathbb E\|k(Z,Z)\|_{\mathscr X}^2.
\]

Thus, using \(\|x+y\|^2\le2\|x\|^2+2\|y\|^2\),

\[
 \mathbb E\|K_m\|_{\mathscr X}^2
 \le\frac4{m^2}\mathbb E\|k(Z,Z')\|_{\mathscr X}^2+
       \frac2{m^2}\mathbb E\|k(Z,Z)\|_{\mathscr X}^2.
\tag{4.7}
\]

Since \(\|K_m\|_{L^1_tX}\le\sqrt T\|K_m\|_{\mathscr X}\), (4.6) is \(O_{L^2}(m^{-1})\). With only an integrable diagonal, its contribution is still \(O_{\mathbb P}(m^{-1})\) by Markov's inequality.

### 4.5 Finish the expansion

Apply (3.1) to (4.5), then use (3.2), (4.4), and (4.7):

\[
 \sup_{t\le T}\|\eta_m(t)\|_X
  \le S_m\{\|K_m\|_{L^1_tX}+C_mD_m(T)^{1+\alpha}\}
  =O_{\mathbb P}(m^{-1}+m^{-(1+\alpha)/2})
  =o_{\mathbb P}(m^{-1/2}).
\tag{4.8}
\]

D5 and (2.4) now give

\[
 F(P_m)-F(P)=\frac1m\sum_i I_P(Z_i)+r_m,
\]

with

\[
 \|r_m\|_H
 =O_{\mathbb P}\bigl(m^{-1}+m^{-(1+\alpha)/2}
                              +m^{-(1+\beta)/2}\bigr)
 =o_{\mathbb P}(m^{-1/2}).
\tag{4.9}
\]

The propagator bound in (3.3) gives

\[
 \sup_t\|v_t(a)\|_X
  \le S_P\sqrt T\|g(a)-Pg\|_{\mathscr X},
\]

so \(I_P\in L^2(P;H)\); its mean is zero because \(Pv_T=0\). This completes the conditional probability theorem.

## 5. When this is an actual contamination influence

The previous theorem identifies the correct empirical first term under D1--D5. Equality with an actual contamination derivative needs an additional deterministic verification; it is not automatic from statements involving only iid samples.

For a fixed \(a\), set \(P_\epsilon=(1-\epsilon)P+\epsilon\delta_a\), \(0\le\epsilon\le1\). Suppose the actual \(P_\epsilon\)-flow exists for all sufficiently small \(\epsilon\). Require the analogues of D2--D3 for these trajectory pairs with uniformly bounded propagation and Taylor constants as \(\epsilon\downarrow0\), and require

\[
 g(a)-Pg\in L^1([0,T];X),\qquad
 (J(a)-PJ)v(a)\in L^1([0,T];X).
\tag{5.1}
\]

The first-exit proof, with forcing \(\epsilon[g(a)-Pg]\), yields \(\sup_t\|\theta_{P_\epsilon}(t)-\theta_P(t)\|_X=O(\epsilon)\). Subtract \(\epsilon v(a)\) from this difference. Its equation has the \(P_\epsilon J\) linear part and source

\[
 \epsilon^2(J(a)-PJ)v(a)+R_\epsilon.
\]

The source integral is \(O(\epsilon^2+\epsilon^{1+\alpha})=o(\epsilon)\). Propagation and the observable Taylor estimate give

\[
 \frac{F(P_\epsilon)-F(P)}{\epsilon}\longrightarrow I_P(a)
       \quad\text{in }H.
\tag{5.2}
\]

If these estimates hold for \(P\)-almost every \(a\), (2.4) is an actual contamination influence for sampling purposes. If a derivative at every datum is requested, verify them for every datum; an almost-everywhere kernel alone cannot establish that stronger version. This is a one-sided derivative along probability-preserving contamination, not a claim of uniform Fréchet differentiability on signed measures.

## 6. Hilbert CLT and its covariance

Under the theorem's conditions, let \(I=I_P(Z)\). Its covariance is

\[
 C_Ph=\mathbb E[\langle I,h\rangle_H I],\qquad h\in H,
\tag{6.1}
\]

which is positive and self-adjoint. For any orthonormal basis \((e_j)\), Tonelli's theorem and Parseval's identity give

\[
 \sum_j\langle C_Pe_j,e_j\rangle
       =\mathbb E\sum_j|\langle I,e_j\rangle|^2
       =\mathbb E\|I\|_H^2<\infty.
\]

Thus it is trace class, with trace \(\mathbb E\|I\|_H^2\). Its nonnegative spectral values \(\lambda_j\) define an \(H\)-valued centered Gaussian

\[
 \mathcal G_P=\sum_j\sqrt{\lambda_j}\,N_je_j,
\]

where the \(N_j\) are independent standard normal variables. The series converges in \(L^2\), because its tail second moment is the tail sum of the \(\lambda_j\); its covariance is (6.1). Zero eigenvalues and the completely degenerate case are permitted.

Here is the finite-dimensional approximation proof of the needed CLT. Put \(S_m=m^{-1/2}\sum_i I_P(Z_i)\), and let \(\Pi_N\) project onto any first \(N\) basis vectors. The finite-dimensional iid CLT gives \(\Pi_NS_m\Rightarrow\Pi_N\mathcal G_P\): for each fixed linear combination, a centered scalar summand \(X\) has finite variance and

\[
 \mathbb E e^{itX/\sqrt m}
   =1-\frac{t^2\mathbb EX^2}{2m}+o(m^{-1});
\]

the remainder follows by dominated convergence from the second-order exponential Taylor remainder divided by \(X^2/m\). Taking the \(m\)-th power gives the Gaussian characteristic function in every finite-dimensional direction.

Moreover, independence and centering give, uniformly in \(m\),

\[
 \mathbb E\|(1-\Pi_N)S_m\|_H^2
       =\mathbb E\|(1-\Pi_N)I\|_H^2\longrightarrow0.
\]

The Gaussian has the same tail second moment. For every bounded 1-Lipschitz function \(q:H\to\mathbb R\), projection therefore changes either expectation by at most \((\mathbb E\|(1-\Pi_N)I\|^2)^{1/2}\). First let \(m\to\infty\) at fixed \(N\), using the finite-dimensional conclusion; then let \(N\to\infty\). This proves convergence against bounded Lipschitz tests, hence weak convergence on the separable Hilbert space. Finally (4.9) gives

\[
 \sqrt m\,[F(P_m)-F(P)]\Rightarrow\mathcal G_P.
\tag{6.2}
\]

If the limiting initialization is a genuinely random external environment retained by \(F\), this argument is conditional on that environment. Independence of the sample permits the conditional argument, but an unconditional Gaussian mixture need not be Gaussian. An ordinary unconditional Gaussian limit requires deterministic limiting covariance, or an additional argument removing that randomness. If the specified mean-field initialization is a fixed probability-space construction and \(F\) is deterministic, no such qualification is needed.

## 7. What the supplied architecture already controls

### 7.1 The raw-state forcing is bounded on the population path

Since \(|\phi|,|\phi'|\le1\),

\[
 \|h\|_2,\|b\|_2\le1,\quad
 |f|\le\|c\|_2,\quad \|d\|_2\le\|c\|_2,\quad
 \|Q\|_2\le\|A\|\|c\|_2.
\]

In particular, with \(R=\|c\|_2+Y\),

\[
 \|G(\theta,a)\|_E
       \le2R\sqrt{\|Q\|_2^2+\|c\|_2^2+1}.
\tag{7.1}
\]

Along an existing solution, the readout equation gives

\[
 \|c_t\|_2\le2\int_0^t(\|c_s\|_2+Y)\,ds
       \le Y(e^{2t}-1).
\]

The same integral formula holds pointwise in \(\Omega_2\), so, starting from zero,

\[
 \|c_t\|_\infty\le2\int_0^t(\|c_s\|_2+Y)\,ds
       \le Y(e^{2t}-1).
\tag{7.2}
\]

Also \(\|\dot K_t\|_{\rm HS}\le2(\|c_t\|_2+Y)\|c_t\|_2\). Thus \(\|K_t\|_{\rm HS}\) and \(\|A_t\|\le\|A_0\|+\|K_t\|_{\rm HS}\) are bounded over the fixed horizon. The constants are crude but finite, uniform over data laws for which the actual solution exists. Equation (7.1) proves \(g\in L^q(P;L^2_tE)\) for every finite \(q\), indeed a uniform bound in the datum. These estimates do not prove existence, uniqueness, or differentiation of the flow.

### 7.2 The observable has a genuine raw-state Taylor estimate

Fix a reached state with \(\|c\|_\infty<\infty\), bounded \(A\), and \(\sup_u\|Q(u)\|_p<\infty\) for some \(p>2\). Let \(v=(v_w,v_K,v_c)\in E\), \(\rho=\|v\|_E\le1\), and use a tilde for the features at \(\theta+v\). Pointwise Taylor and Lipschitz bounds give

\[
 \widetilde h-h=h_v+R_h,
 \qquad |R_h|\le C\min\{|v_w\cdot u|^2,|v_w\cdot u|\},
 \qquad \|\widetilde h-h\|_2\le\|v_w\|_2.
\]

Since \(\widetilde\zeta-\zeta=A(\widetilde h-h)+v_K\widetilde h\),

\[
 \|\widetilde\zeta-\zeta\|_2\le(\|A\|+1)\rho.
\]

Expand the outer activation in the scalar prediction and subtract (2.3). The remainder is the sum of

\[
 \langle v_c,\widetilde b-b\rangle,
 \quad\langle c,\widetilde b-b-\phi'(\zeta)(\widetilde\zeta-\zeta)\rangle,
 \quad\langle d,v_K(\widetilde h-h)\rangle,
 \quad\langle Q,R_h\rangle.
\tag{7.3}
\]

The first three terms have absolute value at most \(C\rho^2\): use Cauchy--Schwarz and the activation Lipschitz bound for the first, \(c\in L^\infty\) and \(|\widetilde b-b-\phi'(\zeta)(\widetilde\zeta-\zeta)|\le C|\widetilde\zeta-\zeta|^2\) for the second, and the operator bound for \(v_K\) for the third.

For the last term let \(p'=p/(p-1)\in(1,2)\). For every \(s\ge0\), \(\min(s^2,s)^{p'}\le s^2\). Hence

\[
 \|R_h\|_{p'}\le C\|v_w\|_2^{2/p'},\qquad
 |\langle Q,R_h\rangle|
       \le C\|Q\|_p\rho^{2-2/p}.
\]

Uniformity in \(u\) gives, for the finite circle measure,

\[
 \|\Phi(\theta+v)-\Phi(\theta)-Bv\|_H
       \le C_p\rho^{2-2/p}.
\tag{7.4}
\]

Also (2.3) bounds \(B:E\to H\) using only \(\sup_u\|Q(u)\|_2\), \(\|c\|_2\), and \(\|h\|_2\le1\). Thus (7.4) is an actual Fréchet derivative of the prediction observable in raw \(E\); the Hölder exponent for its remainder is \(\beta=1-2/p>0\). This conclusion concerns the prediction as a function of the state, not the trained endpoint as a function of the law.

If instead \(\sup_u\|Q(u)\|_{\psi_2}<\infty\), split the last term of (7.3) at \(|Q|=R\). The low part is at most \(CR\rho^2\). The high part is at most \(C\rho\|Q\mathbf1_{|Q|>R}\|_2\). A sub-Gaussian tail \(\mathbb P(|Q|>s)\le2e^{-s^2/(2\sigma^2)}\) gives by integration

\[
 \|Q\mathbf1_{|Q|>R}\|_2
      \le\sqrt2\,(R^2+2\sigma^2)^{1/2}e^{-R^2/(4\sigma^2)}.
\]

Choosing \(R=2\sigma\sqrt{\log(1/\rho)}\) for sufficiently small \(\rho\) yields

\[
 \|\Phi(\theta+v)-\Phi(\theta)-Bv\|_H
        \le C\rho^2\sqrt{\log(e/\rho)}.
\tag{7.5}
\]

This strengthens the final-observable estimate but does not repair a missing state estimate.

### 7.3 Why state moments do not verify D2--D4

The first component of (2.1) contains multiplication by

\[
 e\,\phi''(w\cdot u)Q.
\]

A sub-Gaussian function need not be essentially bounded. Multiplication by an unbounded function is not a bounded map \(L^2\to L^2\): normalized indicators of sets on which its absolute value exceeds \(n\) have unit input norm and output norm at least \(n\). For example, \(Q(s)=\sqrt{\log(1/s)}\) on \((0,1)\) is sub-Gaussian and has every finite moment, but defines an unbounded multiplication operator. Taking a nonzero constant value of \(\phi''(w\cdot u)\) preserves this obstruction.

This example is an obstruction to an inference from moment bounds, not a counterexample trajectory of the supplied network. Special relations along the actual flow could overcome it, but they must be proved. In particular, changing to an \(L^p\) norm merely moves the product estimate to a higher moment unless an invariant space or a closed response estimate is established.

The same issue affects \(J_t(a)v_t(b)\) and especially its diagonal. Finiteness of each reached state's moments is not a quantitative moment bound for first variations, a propagator estimate, or the superlinear reached-chord estimate (3.2).

## 8. Exceptional empirical laws and the moment strengthening

### 8.1 Leaving a neighborhood has exponentially small probability

Suppose only a \(W_1\)-open neighborhood \(U\) of \(P\) is relevant, and choose \(\rho>0\) with \(B_{W_1}(P,\rho)\subset U\). Compactness of \(\mathcal Z\) gives a finite measurable partition into \(N\) sets, each mapped to a representative at distance at most \(\rho/4\). Let \(D\) be the diameter of \(\mathcal Z\); assume \(D>0\), as the zero-diameter case is trivial. Coupling to representatives and then coupling the finite probability vectors gives

\[
 W_1(P_m,P)\le\rho/2+
          \frac D2\sum_{j=1}^N|P_m(C_j)-P(C_j)|.
\]

Therefore \(W_1(P_m,P)\ge\rho\) implies that at least one frequency differs by at least \(\rho/(DN)\). For a Bernoulli sample average, the logarithm of the centered moment-generating function has second derivative at most \(1/4\), so it is at most \(\lambda^2/8\); exponential Markov and optimization give each two-sided tail at threshold \(a\) at most \(2e^{-2ma^2}\). A union bound yields

\[
 \mathbb P(P_m\notin U)
  \le2N\exp\{-2m\rho^2/(D^2N^2)\}.
\tag{8.1}
\]

Thus arbitrary values assigned outside \(U\) do not change convergence in probability or in distribution when the statistic is otherwise defined. But if the actual flow outside \(U\) has not been constructed, one has proved a result for an extension, not the existence of the originally requested actual statistic on every event.

### 8.2 Sufficient conditions for \(m\mathbb E\|r_m\|^2\to0\)

Here is a usable strengthening, with all tail requirements exposed. Suppose:

1. D1--D5 hold with \(0<\alpha,\beta\le1\), and the structural constants \(S_m,C_m\), local radius, and observable constant have deterministic uniform bounds on events \(\mathcal E_m\) satisfying \(\mathbb P(\mathcal E_m^c)=o(m^{-1})\).
2. \(g(Z)\in L^4(P;\mathscr X)\), and both moments in (3.6) are finite.
3. The actual endpoint statistic is uniformly bounded in \(H\), including the complement of \(\mathcal E_m\); alternatively an explicitly bounded extension is used there.

For centered iid Hilbert variables \(Y_i\), expansion of the fourth power gives

\[
 \mathbb E\Big\|\sum_{i=1}^mY_i\Big\|^4
 \le m\mathbb E\|Y_1\|^4+
       3m(m-1)(\mathbb E\|Y_1\|^2)^2.
\]

Indeed, after expanding \(\|\sum_iY_i\|^2\), centering removes the terms with an index occurring only once; the remaining cross inner products are bounded by Cauchy--Schwarz. Applying this to \(Y_i=g(Z_i)-Pg\) in \(\mathscr X\) proves

\[
 \mathbb EA_m^4=O(m^{-2}).
\tag{8.2}
\]

Intersect \(\mathcal E_m\) with the fixed small-source event required in the first-exit proof. Its complement adds \(O(m^{-2})\) probability by (8.2). Call the resulting event \(\mathcal A_m\). On \(\mathcal A_m\), \(D_m(T)\le C A_m\), and (4.8)--(4.9), (4.7), and Lyapunov's inequality yield

\[
 \mathbb E[\|r_m\|_H^2\mathbf1_{\mathcal A_m}]
       \le C\{m^{-2}+m^{-(1+\alpha)}+m^{-(1+\beta)}\}
       =o(m^{-1}).
\tag{8.3}
\]

The population propagator and bounded \(B_T\) also imply \(I_P\in L^4(P;H)\), so the same fourth-moment bound gives

\[
 \mathbb E\Big\|m^{-1}\sum_i I_P(Z_i)\Big\|_H^4=O(m^{-2}).
\]

Using the definition of \(r_m\), boundedness of the endpoint, and Cauchy--Schwarz on the exceptional event, one obtains

\[
 m\mathbb E[\|r_m\|_H^2\mathbf1_{\mathcal A_m^c}]
 \le C m\mathbb P(\mathcal A_m^c)+
          C\mathbb P(\mathcal A_m^c)^{1/2}\longrightarrow0.
\tag{8.4}
\]

The endpoint bound in item 3 can instead be replaced by the direct tail condition \(m\mathbb E[\|F(P_m)-F(P)\|_H^2\mathbf1_{\mathcal A_m^c}]\to0\), where \(\mathcal A_m\) includes both structural localization and the small-source condition. Equations (8.3)--(8.4) prove the moment strengthening. They also imply

\[
 m\mathbb E\|F(P_m)-F(P)\|_H^2\longrightarrow
       \operatorname{tr}C_P.
\]

Tightness of random stability constants alone gives no moment conclusion: it supplies neither uniform integrability nor the needed quantitative exceptional-event bound. Exponential law localization from (8.1) is helpful only if the dynamic estimates have actually been proved uniformly throughout that neighborhood.

## 9. Remaining obligations and route decision

| Obligation | Status from the supplied prompt | What would resolve it |
|---|---|---|
| Actual \(P\)- and \(P_m\)-flows at every Borel \(P\) through \(40\), with identification as the requested trained limit | Supplied only locally in law, and not enough to infer all-law existence | A well-posedness/identification theorem for the stated architecture and clock |
| Bounded raw forcing and quantitative final-observable Taylor estimate | Derived above along existing reached paths | Supervisor check against the complete established architecture |
| Population linear response with the actual adjoint and source | Formal formula (2.1)--(2.2); well-posedness unproved | A closed reached-direction space or direct evolution estimate |
| Empirical linear propagation (3.1), tight uniformly in sample size | Not supplied | An energy, weighted-space, or other actual linear evolution bound |
| Superlinear reached-chord remainder (3.2) | Not supplied | A quantitative estimate controlling products of state differences along actual coupled flows |
| Off-diagonal response kernel and separate diagonal bound (3.6) | Not supplied | Bounds on \(J_t(a)v_t(b)\), with domain/Fubini justification and same-datum control |
| Contamination derivative identification | Conditional Section 5 | Deterministic contamination versions of the same stability/Taylor estimates |
| Hilbert CLT once the expansion holds | Proved in Section 6 | No additional model-specific condition beyond deterministic/conditional interpretation |
| \(L^2\) remainder | Conditional Section 8 | Quantitative localization/tails or suitable moments of dynamic constants |

**Adversarial checks.** A point-mass law gives zero centered source and zero covariance, consistent with \(P_m=P\) almost surely. The diagonal of the interaction kernel was not discarded. Random empirical operators were not replaced by their population means. The nonlinear empirical path, rather than a linear surrogate endpoint, occurs in the exact difference equation. Existence and domain assumptions were separated from formal derivatives. Local-in-law identification was not extended to arbitrary laws by continuity. The raw-state multiplication obstruction was treated as a failure of an inference, not as a counterexample to the neural target.

**Registry recommendation:** retain this route as a conditional probabilistic reduction with two useful elementary estimates. It removes the need for a uniform empirical operator law and isolates a strictly concrete next task: prove closed state-response propagation and a superlinear Taylor estimate along the actual population/empirical pair. Without that result, further CLT or leave-one-out machinery does not resolve the target.
