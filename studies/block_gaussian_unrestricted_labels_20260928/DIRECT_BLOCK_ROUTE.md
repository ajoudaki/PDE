# Direct block route: exact particle form and finite-time localization

This route began as a fresh prompt-only derivation. No other study artifact, external source, or experiment was used. During completion, the coordinator communicated its matching state-envelope calculation, suggested the logarithmic block-size regime, and identified the necessary coordinate-maximum factor in the backward stability estimate. The final artifact incorporates that coordination and is not an isolated independent review. The object is the specified finite response-memory closure, with every learned matrix entry permitted to change. The main theorem concerns its prediction limit as the number of aligned blocks tends to infinity at fixed block size and memory order. It does **not** identify this closure with full gradient flow, take the memory order to infinity, or assert an all-time bound.

The principal conclusions are:

* The aligned architecture is exactly an interacting system of finite-dimensional blocks, despite its dense learned matrices.
* Its memory energy and finite-time state envelopes require no small-label hypothesis and can be independent of the memory order.
* For bounded initial hidden-block operator norms, a complete particle-coupling argument gives a prediction mean-square error of order the reciprocal number of blocks, uniformly over a fixed time interval. The constants below are explicit.
* Conditioning Gaussian blocks supplies a precise localization inequality, but ordinary Gronwall estimates do not by themselves close the unbounded-tail limit. Memory energy alone also does not make stability uniform in memory order.

## 1. Setup and exact finite-block equations

Write the number of blocks as \(N\), so the width is \(n=Nk\); this avoids confusing it with the supplied memory variable \(B\). Fix \(L\ge2\), \(m,d,k,q\ge1\), data \((x_a,y_a)_{a=1}^m\), and a twice continuously differentiable activation satisfying

\[
 |\phi|\le M,\qquad |\phi'|\le a_1,\qquad |\phi''|\le a_2,
 \qquad M\ge1.
\]

The bounded derivatives are an explicit hypothesis; boundedness and \(C^2\) smoothness alone would not imply them. Tanh satisfies the hypothesis. Put \(X=\max_a\|x_a\|/\sqrt d\), \(Y=\|y\|_2/\sqrt m\), and use the block norm \(|v|_k=\|v\|_2/\sqrt k\). Let \(G_{\ell b}\) be the fixed initial hidden block, \(U_b\in\mathbb R^{k\times d}\) the current first-layer rows, and \(v_b\in\mathbb R^k\) the current readout block. Set

\[
 \alpha_j=2j+1,\quad
 M_{\ell,a,j,b}=B_{\ell,a,j,b}/\tau,\quad
 N_{\ell,a,j,b}=C_{\ell,a,j,b}/\tau.
\]

For an array \(D=(D_{a,j})\), use

\[
 \|D\|_{\alpha,k}^2
 =\frac1m\sum_{a=1}^m\sum_{j=0}^{q-1}\alpha_j|D_{a,j}|_k^2.
\]

The same notation without \(k\) is used for scalar arrays. An individual sample's moment norm omits the average over \(a\). Write \(\langle g\rangle_N=N^{-1}\sum_b g_b\).

For \(\ell\ge2\), define the scalar arrays

\[
 F_{\ell,a,c,j}
 =\left\langle k^{-1}M_{\ell,c,j,b}^{\mathsf T}h_{\ell-1,a,b}\right\rangle_N,
 \quad
 H_{\ell,a,c,j}
 =\left\langle k^{-1}N_{\ell,c,j,b}^{\mathsf T}\delta_{\ell,a,b}\right\rangle_N.
\]

The exact forward and backward equations are

\[
\begin{aligned}
 z_{1,a,b}&=U_bx_a/\sqrt d,\\
 z_{\ell,a,b}&=G_{\ell b}h_{\ell-1,a,b}
 -\frac{2\tau}{m}\sum_{c,j}\alpha_jN_{\ell,c,j,b}F_{\ell,a,c,j},\\
 h_{\ell,a,b}&=\phi(z_{\ell,a,b}),\\
 f_a&=\left\langle k^{-1}v_b^{\mathsf T}h_{L,a,b}\right\rangle_N,\\
 \delta_{L,a,b}&=v_b\odot\phi'(z_{L,a,b}),\\
 \delta_{\ell-1,a,b}&=\phi'(z_{\ell-1,a,b})\odot
 \left[G_{\ell b}^{\mathsf T}\delta_{\ell,a,b}
 -\frac{2\tau}{m}\sum_{c,j}\alpha_jM_{\ell,c,j,b}H_{\ell,a,c,j}\right].
\end{aligned}
\]

These formulas follow by inserting the supplied outer-product reconstruction and using \(n=Nk\). In particular, the learned contribution couples every pair of blocks. No training mask has been introduced.

Let \(\mathcal K_q\) be the moment matrix

\[
 (\mathcal K_qD)_j=(j+1)D_j+\sum_{i<j}\alpha_iD_i,
 \qquad (\mathcal Ih)_j=h.
\]

The block state evolves by

\[
\begin{aligned}
 \dot\tau&=\rho=\|f-y\|_2/\sqrt m,\\
 \dot v_b&=-\frac2m\sum_a r_ah_{L,a,b},\\
 \dot U_b&=-\frac2m\sum_a r_a\delta_{1,a,b}x_a^{\mathsf T}/\sqrt d,\\
 \dot M_{\ell,a,b}&=\frac\rho\tau
       (\mathcal Ih_{\ell-1,a,b}-\mathcal K_qM_{\ell,a,b}),\\
 \dot N_{\ell,a,b}&=\frac{r_a}\tau\mathcal I\delta_{\ell,a,b}
       -\frac\rho\tau\mathcal K_qN_{\ell,a,b}.
\end{aligned}
\]

Initially \(\tau=1\), \(v_b=0\), all \(N\) vanish, and only \(M_{\ell,a,0,b}=h_{\ell-1,a,b}(0)\) is nonzero. Initial activations are computed from the initial block network, so this initialization is local to each block and uses no population interaction.

There are \(2(L-1)m^2q+m\) empirical scalar interactions. Each evolving block has \(kd+k+2(L-1)mqk\) real coordinates, in addition to its fixed Gaussian matrices. Forward interactions are evaluated in increasing layer order and backward interactions in decreasing order, so the construction has no implicit algebraic loop.

Replacing block averages by expectations defines the corresponding nonlinear one-block law equation. Its interaction list is finite; its evolving probability law is not a finite-dimensional deterministic scalar closure. The complete random matrices \(G_{\ell b}\) are retained. Each matrix is reused at every time and appears through its transpose in backpropagation. Its correlations with all states generated from it are retained. Only different initial blocks are independent; neuronwise independence within a block or fresh Gaussian redraws would change this system.

## 2. Memory energy and arbitrary-label finite-time envelopes

For one sample and block, let \(E_D=\sum_j\alpha_j|D_j|_k^2\) and \(S_D=\sum_j\alpha_jD_j\). For the unnormalized equation

\[
 \dot D_j=u-\frac\rho\tau
 \left(jD_j+\sum_{i<j}\alpha_iD_i\right),
\]

direct expansion gives the exact identity

\[
 \dot E_D=\frac\rho\tau E_D
       +2k^{-1}S_D^{\mathsf T}u-\frac\rho\tau|S_D|_k^2.
\]

Indeed, the diagonal identity \(\alpha_j^2-\alpha_j=2j\alpha_j\) combines with the off-diagonal terms to produce \(|S_D|_k^2-E_D\). Consequently, for \(\rho>0\),

\[
 \frac{d}{dt}(E_D/\tau)
 =\frac{|u|_k^2}{\rho}
 -\frac\rho{\tau^2}\left|S_D-\frac\tau\rho u\right|_k^2
 \le\frac{|u|_k^2}{\rho}.
\]

When \(\rho=0\), both relevant sources vanish, and the identity is interpreted by its nonsingular preceding form. Applying it to the two supplied sources yields

\[
 \sum_j\alpha_j|M_{\ell,a,j,b}(t)|_k^2\le M^2,
\]

\[
 \sum_j\alpha_j|N_{\ell,a,j,b}(t)|_k^2
 \le\frac1{\tau(t)}\int_0^t
       \frac{r_a(s)^2}{\rho(s)}|\delta_{\ell,a,b}(s)|_k^2\,ds.
\]

Here and below \(r_a^2/\rho=0\) at \(\rho=0\). Since \(r_a^2\le m\rho^2\), a uniform response envelope \(|\delta_{\ell,a,b}|_k\le D_\ell\) implies

\[
 \|N_{\ell,b}\|_{\alpha,k}\le\sqrt m D_\ell.
\]

No constant in these inequalities grows with \(q\).

The bounded activation also gives, without loss descent,

\[
 |v_b(t)|_k\le2M(\tau(t)-1),\quad
 |f_a(t)|\le2M^2(\tau(t)-1),\quad
 \rho(t)\le Y+2M^2(\tau(t)-1).
\]

For any fixed \(T\), define

\[
 P=Ye^{2M^2T},\qquad
 S=1+\frac{Y}{2M^2}(e^{2M^2T}-1),\qquad
 V=2M(S-1).
\]

Then \(\rho\le P\), \(1\le\tau\le S\), and \(|v_b|_k\le V\) on \([0,T]\). These bounds hold for all finite labels, all block realizations, and every memory order.

If \(\|G_{\ell b}\|_{\rm op}\le R\), put

\[
 D_L=a_1V,\qquad K_\ell=\sqrt mD_\ell,
 \qquad
 D_{\ell-1}=a_1(R+2SMK_\ell)D_\ell
 \quad(\ell=L,\ldots,2).
\]

Descending through the backward recursion proves \(|\delta_{\ell,a,b}|_k\le D_\ell\). At the induction step, the weighted scalar-contraction norm is at most \(K_\ell D_\ell\), and the local \(M\)-norm is at most \(M\). This proves the displayed recurrence. In particular, \(U_b-U_b(0)\) has normalized Frobenius norm at most \(2XPTD_1\). All states therefore remain finite on every finite interval. The constants depend on \(R,L,m,T,Y,\phi\), but not on \(N,k,q\).

For an actual finite Gaussian realization, the maximum of its finitely many block norms is finite almost surely, so this argument already proves finite-width, finite-time global continuation. That statement alone is not a width-uniform Gaussian estimate.

## 3. Complete bounded-coefficient particle theorem

**Theorem.** Assume the initial blocks are iid, \(\|G_\ell\|_{\rm op}\le R\) almost surely, and the first-layer initialization is arbitrary iid across blocks, possibly Gaussian and unbounded. Within a block, arbitrary correlations in initialization are allowed. Use the prescribed initialization above. There is a unique nonlinear block-law solution and a unique finite-block solution on every finite interval. Let \(f^{(N)}\) be the finite prediction and \(f^{(\infty)}\) the law prediction. Then

\[
 \sup_{0\le t\le T}\mathbb E\|f^{(N)}(t)-f^{(\infty)}(t)\|_m^2
 \le \frac{C}{N},\qquad \|z\|_m^2=m^{-1}\sum_a z_a^2.
\]

Here is one explicit, deliberately conservative choice of \(C\). This specifies all dependence rather than concealing it in a generic regularity constant.

First define forward sensitivity constants

\[
 Z_1=X,\qquad A_1=a_1X,
\]

\[
 \begin{aligned}
 Z_\ell={}&(R+2SK_\ell M)A_{\ell-1}
 +2K_\ell M^2+2SM^2+2SK_\ell M+2SK_\ell,\\
 A_\ell={}&a_1Z_\ell \qquad(\ell=2,\ldots,L),\\
 F={}&M+VA_L+1.
 \end{aligned}
\]

Define backward sensitivity constants by

\[
 J_L=a_1+a_2VZ_L,
\]

\[
 \begin{aligned}
 J_{\ell-1}={}&a_2\sqrt{k}(R+2SMK_\ell)D_\ell Z_{\ell-1}\\
 &+a_1\big[(R+2SMK_\ell)J_\ell
 +2MK_\ell D_\ell+2SK_\ell D_\ell+2SMD_\ell+2SM\big].
 \end{aligned}
\]

For \(\ell=2,\ldots,L\), set

\[
 L^M_\ell=P(qA_{\ell-1}+q^2)+(F+P)M(q+q^2),
\]

\[
 L^N_\ell=q[D_\ell(F+P)+PJ_\ell]+Pq^2+(F+P)q^2K_\ell.
\]

Finally set

\[
 \Lambda=F+2(MF+PA_L)+2X(D_1F+PJ_1)
       +\sum_{\ell=2}^L(L^M_\ell+L^N_\ell),
\]

\[
 \Gamma=m\left[(L-1)M^2+\sum_{\ell=2}^LK_\ell D_\ell+VM\right],
 \qquad
 C=2F^2\Gamma^2(1+\Lambda^2T^2e^{2\Lambda T}).
\]

The factor \(\sqrt{k}\) is necessary in this estimate: a block RMS bound on a backward carrier gives a coordinate maximum bound only after multiplication by \(\sqrt{k}\). The readout obeys the stronger coordinatewise bound \(\|v_b\|_\infty\le V\), so no such factor is needed in \(J_L\). There is no other dependence on \(k\) in these recurrences. In particular, for fixed remaining parameters, \(\Lambda=\Lambda_0+\Lambda_1\sqrt{k}\) with finite nonnegative constants \(\Lambda_0,\Lambda_1\), and \(C=O((1+k)e^{c\sqrt{k}})\). Since \(N=n/k\), the stated error is \(Ck/n\) when expressed using total width. The result concerns fixed \(q\); its stated constant can grow exponentially in \(q^2T\).

### Proof

The local vector field is locally Lipschitz: \(\phi\) and \(\phi'\) are Lipschitz with the displayed constants, the norm defining \(\rho\) is Lipschitz, and \(\tau\ge1\). This also holds for the law equation on the Banach space of bounded increments from the possibly unbounded initial \(U(0)\), together with the other bounded state coordinates. Picard iteration on a ball gives a solution for a sufficiently short interval because the integral map has Lipschitz constant equal to the interval length times the local vector-field Lipschitz constant. The envelopes of Section 2 keep all increment coordinates in a finite ball on each fixed interval. Repeating the local construction therefore proves existence and uniqueness up to any \(T\). No bound on \(U(0)\) is needed because every occurrence of it outside its additive increment is through globally bounded or globally Lipschitz activation functions.

Couple each finite block to a copy of the law solution with exactly the same initial block. The comparison copies are iid, driven by the deterministic law interactions. Let \(\mathcal E(t)\) be the sum of the absolute clock error and the empirical RMS error in the block state, using normalized Frobenius norm for \(U\), \(|\cdot|_k\) for \(v\), and \(\|\cdot\|_{\alpha,k}\) for each moment array.

At the comparison copies, let \(\xi^F_{\ell,a}(t)\) and \(\xi^H_{\ell,a}(t)\) be empirical-minus-population errors of the scalar arrays \(F\) and \(H\), respectively. These arrays have squared norm \(\sum_{c,j}\alpha_j|\cdot|^2/m\). Let \(\xi^f_a\) be the analogous prediction error. Define

\[
 \eta(t)=\sum_{\ell=2}^L\sum_a
       (\|\xi^F_{\ell,a}(t)\|_\alpha+\|\xi^H_{\ell,a}(t)\|_\alpha)
       +\sum_a|\xi^f_a(t)|.
\]

The corresponding single-block random vectors have norms at most \(M^2\), \(K_\ell D_\ell\), and \(VM\). Independence and centering eliminate cross terms in the squared norm of their sample averages, giving, at every deterministic time,

\[
 \mathbb E\eta(t)^2\le\Gamma^2/N.
\]

This variance estimate is independent of \(q\); it is a Hilbert-space estimate, not a coordinatewise union bound.

For completeness, the algebraic stability estimates generating the constants are as follows. The forward interaction difference has norm at most

\[
 M\mathcal E+M(\text{previous activation RMS error})+\|\xi^F\|_\alpha.
\]

The backward interaction difference has norm at most

\[
 D_\ell\mathcal E+K_\ell(\text{current response RMS error})+\|\xi^H\|_\alpha.
\]

These follow by adding and subtracting the product formed from the comparison moments and actual activation or response, then applying Cauchy–Schwarz first over moment indices and then over blocks. All moment comparisons retain their average over the memory-sample index \(c\); no bound on an individual sample's moment error is extracted from that average. Activation and response error estimates hold for each target sample \(a\), and are then maximized over \(a\). In source terms such as \(r_a\Delta\delta_a\), the dataset RMS is at most \(\rho\max_a\|\Delta\delta_a\|_{L^2(b)}\). Thus these transitions introduce no unrecorded \(\sqrt m\) factor.

Substitution in the forward and backward equations gives preactivation, activation, and response RMS errors at most \(Z_\ell(\mathcal E+\eta)\), \(A_\ell(\mathcal E+\eta)\), and \(J_\ell(\mathcal E+\eta)\). At the backward Hadamard product, use

\[
 |(\phi'(z)-\phi'(\bar z))\odot b|_k
 \le a_2\|b\|_\infty|z-\bar z|_k,
 \qquad \|b\|_\infty\le\sqrt{k}|b|_k.
\]

This gives precisely the displayed \(\sqrt{k}\) term in \(J_{\ell-1}\); replacing it by an RMS bound without that factor would be invalid. The terms \(2SK_\ell\) and \(2SM\) in the recurrences account for the forward and backward sampling errors. Prediction error and clock-speed error are at most \(F(\mathcal E+\eta)\).

In weighted moment norm, \(\|\mathcal I\|=q\) because \(\sum_{j<q}\alpha_j=q^2\). Also \(\|\mathcal K_q\|\le q^2\). To check the latter, conjugate by the diagonal matrix with entries \(\sqrt{\alpha_j}\). The resulting diagonal entries are \(j+1\) and its lower entries are \(\sqrt{\alpha_i\alpha_j}\). Its squared Frobenius norm is

\[
 \sum_{j=0}^{q-1}(j+1)^2+\sum_{i<j}\alpha_i\alpha_j
 =\frac{q^4}{2}-\frac{q^3}{3}+\frac{q^2}{2}+\frac q3
 \le q^4.
\]

Since \(|\rho/\tau-\bar\rho/\bar\tau|\le(F+P)(\mathcal E+\eta)\), substitution in the moment equations gives the constants \(L^M_\ell,L^N_\ell\). The readout, first-layer, and clock equations give the remaining terms of \(\Lambda\). Thus the upper right derivative satisfies

\[
 D^+\mathcal E(t)\le\Lambda(\mathcal E(t)+\eta(t)),\qquad \mathcal E(0)=0.
\]

Integrating the inequality after multiplication by \(e^{-\Lambda t}\) gives

\[
 \sup_{s\le T}\mathcal E(s)
 \le\Lambda e^{\Lambda T}\int_0^T\eta(s)\,ds,
 \quad
 \mathbb E\sup_{s\le T}\mathcal E(s)^2
 \le\frac{\Lambda^2T^2e^{2\Lambda T}\Gamma^2}{N}.
\]

Combining this with the fixed-time prediction bound and \((a+b)^2\le2a^2+2b^2\) proves the theorem.

The stronger order of supremum and expectation also follows here, with an additional explicit constant. Put

\[
 B_M=PM(q+q^2),\qquad
 B_{N,\ell}=P(qD_\ell+q^2K_\ell).
\]

These bound the normalized moment velocities. Readout and first-layer velocities are at most \(2MP\) and \(2XPD_1\). Define activation-velocity bounds recursively by

\[
 \mathcal V_1=2a_1X^2PD_1,
\]

\[
 \mathcal V_\ell
 =a_1\big[(R+2SK_\ell M)\mathcal V_{\ell-1}
       +2PK_\ell M^2+2SB_{N,\ell}M^2+2SK_\ell MB_M\big].
\]

Differentiating the forward recursion proves \(|\dot h_{\ell,a,b}|_k\le\mathcal V_\ell\). In this differentiation, the derivative of the forward scalar-interaction vector has norm at most \(MB_M+M\mathcal V_{\ell-1}\). Thus the individual law-copy forward-summary and prediction velocities are bounded by

\[
 \mathcal W_\ell=MB_M+M\mathcal V_{\ell-1},
 \qquad \mathcal W_f=2M^2P+V\mathcal V_L.
\]

All these constants are independent of \(k\) and grow at most quadratically in \(q\), with the remaining parameters fixed. Bounded derivatives justify differentiating the corresponding expectations. For any iid Hilbert-valued law-copy summary \(g_b(t)\) with \(\|g_b(0)\|\le b_0\), \(\|\dot g_b(t)\|\le b_1\), the centered sample error \(\xi\) satisfies

\[
 \mathbb E\sup_{t\le T}\|\xi(t)\|^2
 \le 2b_0^2/N+2T^2b_1^2/N.
\]

Indeed, write \(\xi(t)=\xi(0)+\int_0^t\dot\xi(s)\,ds\), apply the squared triangle and integral Cauchy–Schwarz inequalities, and use the iid variance identity at time zero and at each derivative time. For prediction summaries \(g_b(0)=0\), the bound improves to \(T^2b_1^2/N\).

Let \(\eta_F\) retain only the forward-interaction and prediction terms of \(\eta\). Minkowski's inequality gives

\[
 \mathbb E\sup_{t\le T}\eta_F(t)^2\le\Gamma_{\rm path}^2/N,\qquad
 \Gamma_{\rm path}
 =m\left[\sum_{\ell=2}^L\sqrt{2M^4+2T^2\mathcal W_\ell^2}
                +T\mathcal W_f\right].
\]

The prediction estimate uses only forward interactions, and hence is at most \(F(\mathcal E+\eta_F)\). Combining the last display with the already proved state-supremum estimate proves

\[
 \mathbb E\sup_{t\le T}
 \|f^{(N)}(t)-f^{(\infty)}(t)\|_m^2
 \le\frac{C_{\rm path}}N,\qquad
 C_{\rm path}=2F^2\left[
       \Lambda^2T^2e^{2\Lambda T}\Gamma^2+\Gamma_{\rm path}^2\right].
\]

In particular \(C_{\rm path}=O((1+k)e^{c\sqrt k})\) for fixed remaining parameters. This argument supplies the required time-uniform sampling estimate rather than interchanging supremum and expectation.

The same theorem covers passive predictions on bounded test inputs. For a test point \(x\), compute its forward activations and scalar forward interactions using the trained state; add no training residual, moment source, or backward equation. For \(\|x\|/\sqrt d\le X_{\rm test}\), replace \(X\) in the constants by \(X_*=\max(X,X_{\rm test})\). Adding the test forward summaries and prediction to the sampling estimate increases both sampling constants by at most the factor \(1+1/m\). Thus

\[
 \mathbb E\sup_{t\le T}|f^{(N)}(x,t)-f^{(\infty)}(x,t)|^2
 \le (1+1/m)^2 C_{\rm path}(X_*)/N.
\]

This is a bound at each test point with a uniform constant, not a supremum over test inputs. For any fixed probability measure \(\mu\) supported on that bounded input set, integration and the nonnegative-integrand interchange give the same bound for \(\mathbb E\int\sup_{t\le T}|f^{(N)}(x,t)-f^{(\infty)}(x,t)|^2\,d\mu(x)\).

## 4. What this proves for Gaussian blocks, and what it does not

For iid entries \(G_{ij}\sim N(0,1/k)\), an elementary net argument gives

\[
 p_k(R):=\Pr(\|G\|_{\rm op}>R)
 \le\min\{1,\,2\,81^k e^{-kR^2/8}\}.
\]

To verify the constants, take a \(1/4\)-net of the unit sphere with at most \(9^k\) points, obtained by the disjoint-ball volume bound. Approximating both maximizing unit vectors shows \(\|G\|_{\rm op}\le2\max_{u,v\text{ in the net}}|u^{\mathsf T}Gv|\). Each fixed bilinear form is Gaussian with variance \(1/k\); its two-sided exponential tail and the union bound give the formula.

Let \(f^{(\infty,R)}\) be the law solution when each initial hidden block is conditioned to have operator norm at most \(R\). Let \(f^{(N,G)}\) use the original Gaussian initialization. Conditional on every hidden block satisfying the bound, the original initialization is exactly a product of the conditioned block laws. Moreover, both predictions have absolute value at most \(MV\) on \([0,T]\). The theorem therefore gives the rigorous localization inequality

\[
 \sup_{t\le T}\mathbb E\|f^{(N,G)}(t)-f^{(\infty,R)}(t)\|_m^2
 \le\frac{C(R,k)}N
 +4M^2V^2\min\{1,\,2N(L-1)81^k e^{-kR^2/8}\}.
\]

The reference prediction on the right depends on \(R\) and \(k\). For fixed \(k,R\), the event that every Gaussian block is bounded has probability tending to zero as \(N\) grows. Increasing \(R\) requires both a useful balance between \(C(R,k)/N\) and the displayed tail term, and an identification of a limit of \(f^{(\infty,R)}\). Neither follows from the theorem's rapidly growing Gronwall constant. Reporting the bounded-coefficient theorem as the full fixed-\(k\) Gaussian particle limit would be incorrect.

The same localization inequality holds with \(\mathbb E\sup_{t\le T}\) in place of \(\sup_{t\le T}\mathbb E\), if \(C\) is replaced by \(C_{\rm path}\).

There is, however, a valid joint-regime corollary for the original Gaussian finite systems. Fix \(R\) such that \(\gamma_R=R^2/8-\log81>0\), fix \(A>1/\gamma_R\), and set \(k_N=\lceil A\log N\rceil\). Since the preceding sensitivity recurrence has \(\Lambda=\Lambda_0+\Lambda_1\sqrt{k}\), the same localization bound proves

\[
 \sup_{t\le T}\mathbb E\|f^{(N,G,k_N)}(t)
       -f^{(\infty,R,k_N)}(t)\|_m^2
 \le N^{-1+o(1)}+O(N^{1-A\gamma_R})\longrightarrow0.
\]

The constants implicit in this last display depend only on the fixed \(R,A,q,m,L,T,Y,X,\phi\); the explicit preceding formulas supply them. This statement makes no small-label assumption. Its deterministic comparison prediction belongs to a family of conditioned block-law equations whose block dimension grows with \(N\). It neither proves a fixed-dimensional closure independent of total width nor identifies a dense-Gaussian population limit. It is an auxiliary, explicitly quantified regime in which the Gaussian tail issue and the finite-block sampling error can both be controlled.

There is a useful route around maximum-block bounds for **a priori moments**, distinct from particle coupling. For any finite configuration put \(S_b=\max_{\ell\ge2}\|G_{\ell b}\|_{\rm op}\). Define nonnegative polynomials recursively by

\[
 p_L(s)=a_1V,\quad Q_\ell=\langle p_\ell(S_b)^2\rangle_N,\quad
 p_{\ell-1}(s)=a_1\big[s p_\ell(s)+2SM\sqrt m\,Q_\ell\big].
\]

The same energy argument gives \(|\delta_{\ell,a,b}|_k\le p_\ell(S_b)\): the local response term contributes \(S_bp_\ell(S_b)\); the empirical contraction contributes at most \(2SM\sqrt m\,Q_\ell\). Every coefficient is a finite polynomial expression in finitely many empirical powers of \(S_b\). Thus fixed-depth Gaussian moment bounds can be built without controlling \(\max_bS_b\). This deals with state growth and learned feedback in the envelope calculation. It does not automatically bound the difference of two trajectories: the latter contains products of state errors with the same reused large block coefficients.

## 5. Exact remaining obligations

1. **Original Gaussian particle coupling at fixed block size.** A stability or uniqueness estimate must propagate differences using the polynomial moment envelopes, without the maximum-block Gronwall constant. Alternatively, a cutoff argument must exhibit an actual radius sequence for which both its stability and tail errors vanish. Finite moments of states alone do not establish either step. The logarithmically growing block-size corollary above has a conditioned comparison family and does not close this fixed-\(k\) obligation.
2. **Memory-order-uniform stability.** The energy identity removes \(q\) from state bounds and sampling variances. When two clocks differ, the normalized difference equation contains \((\rho/\tau-\bar\rho/\bar\tau)\mathcal K_q\bar M\), and similarly for \(N\). An energy bound on \(\bar M\) does not control \(\mathcal K_q\bar M\) independently of \(q\). A separate reachable-state regularity or common-clock argument is required. The displayed theorem makes no such claim.
3. **Accuracy relative to full training.** The theorem is a law-of-large-numbers result for the specified finite-memory equations. A source estimate for the omitted response-history modes, plus stability, is needed to compare them with the original gradient flow. Increasing width does not supply that source estimate.
4. **All-time prediction control.** The established envelopes grow with \(T\), and the reconstructed hidden dynamics were not shown to decrease the original training loss. An integrable long-time stability mechanism or another dissipative estimate is required before replacing a fixed interval by all time. Finite labels do not obstruct the finite-time theorem, but arbitrary-label all-time accuracy is not proved.
5. **Dense-block limit.** No argument here identifies a limiting block law as \(k\to\infty\). The main particle theorem sends \(N\to\infty\) at fixed \(k\). The auxiliary logarithmic regime compares to a changing conditioned family. A single dense Gaussian matrix is a different limit problem, with a different independence structure.

Accordingly, the direct block structure and energy identity do remove a small-label condition from the explicit finite-time bounded-coefficient particle theorem and from finite-time state-envelope calculations. A logarithmically growing block regime also admits a proved original-Gaussian estimate against an explicitly conditioned comparison family. These results do not, by themselves, prove the original-Gaussian fixed-block width limit, convergence of the finite-memory approximation, or an arbitrary-label all-time result.
