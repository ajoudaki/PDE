# Controlled root-width fluctuations over a bounded query domain

This extends the proved training-query fluctuation estimate in POPULATION_CAVITY_ATTEMPT.md to passive unseen inputs. It retains two tanh hidden layers, orthonormal fixed training inputs, Gaussian initialization, and zero initial readout. The centering is the finite-width mean; population bias is a separate issue.

## Statement

Let \(b:[0,S]\to\mathbb R^m\) be deterministic, \(b(0)=0\), \(S\le1\), and \(\sum_a|b_a'(u)|\le1\) almost everywhere. Run the actual dense controlled equations (1) of CONTROLLED_FEEDBACK_STABILITY.md. If \(\|x\|/\sqrt d\le B\), then
\[
\mathbb E\sup_{0\le u\le S}
 |f_n^b(u,x)-\mathbb E f_n^b(u,x)|^2
\le \frac{C_B S^2}{n}.
\tag{1}
\]
The constant is uniform over the fixed query ball and over deterministic controls; it does not put a supremum over controls inside the expectation.

For any probability law \(\mu\) supported in this ball, Tonelli gives
\[
\mathbb E\int\sup_{u\le S}
 |f_n^b(u,x)-\mathbb E f_n^b(u,x)|^2\,d\mu(x)
\le \frac{C_B S^2}{n}.
\tag{2}
\]
This is the all-time-inside-input-integral form needed by the study. It is not a supremum over all query inputs.

## 1. Passive first-layer coordinates

Write \(v=x/\sqrt d=\sum_a c_a v_a+v_\perp\), where \(c_a=v_a^\top v\), \(\nu=\|v_\perp\|\), and \(\sum_a|c_a|+\nu\le(\sqrt m+1)B\). The initialized first preactivations at training inputs and the orthogonal query root may be represented by \(m+1\) independent standard Gaussian columns \(Z_{0,a}\), \(\zeta_0\). The query first preactivation is exactly
\[
z_x^{(1)}(u)=\nu\zeta_0+\sum_a c_a F^{-1}(p_a(u)),
\qquad p_a(0)=F(Z_{0,a}).
\tag{3}
\]
If \(\nu=0\), the unused column \(\zeta_0\) may still be included. Define query features \(h_x=\tanh z_x^{(1)}\), \(g_x=\tanh(Wh_x)\), responses
\[
\delta_x=w\odot(1-g_x^2),\quad k_x=W^\top\delta_x,\quad
\delta_x^{(1)}=(1-h_x^2)\odot k_x.
\]
None of these query quantities drives training.

## 2. Finite query carrier moments

Use the same hidden-matrix operator projection as in the checked training-query proof: \(W_0^\Pi=\Pi_K(G/\sqrt n)\), where \(G\) has iid standard Gaussian entries, and \(\Pi_K\) is Frobenius projection onto the operator ball of radius \(K\). It is nonexpansive. The projected and original systems coincide on \(E_n=\{\|G/\sqrt n\|_{\rm op}\le K\}\), whose complement has probability \(Ce^{-cn}\).

Conditional on every fixed first-root array, the original-matrix cavity proof extends to the passive response \(\delta_x\), as follows. Delete first-layer neuron \(i\), retaining normalization \(n\), and fix all first roots and all other columns of \(W_0\). The deleted Gaussian column remains independent of the cavity. Formula (3) restricted to retained neurons is a \(C_B\)-Lipschitz function of the training transformed coordinates. Thus the normalized cavity state difference \(O(Sq_i/\sqrt n)\), plus the missing query contribution \(W_i h_{x,i}\), implies
\[
\|\delta_x^b-\delta_x^{-i,b}\|_2\le C_B S q_i,
\quad q_i=\|W_{0,i}\|_2+S^2/\sqrt n.
\]
The cavity query response has RMS at most \(S\); its RMS Lipschitz constant in the uniform integrated-control metric is at most \(C_B\). These follow respectively from \(\|w\|_\infty\le S\), bounded gates, and the checked control-path Lipschitz estimate together with (3).

Consequently,
\[
k_{x,i}^b=W_{0,i}^\top\delta_x^{-i,b}+R_{x,i}^b,
\qquad |R_{x,i}^b|\le C_B S\quad\hbox{on }E_n.
\]
Conditional on the cavity, the first term is a Gaussian process indexed by the same deterministic control class as in FINITE_TAIL_ROUTE.md. Its variance is at most \(S^2\), and its increment metric is bounded by \(C_B\|b-c\|_\infty\). The identical covering and Gaussian increment summation from that proof, with this changed constant, gives coordinate square-exponential moments for the supremum over controls, with constants depending on \(B\) but not \(n\) or the fixed root values.

For the projected system outside \(E_n\), the crude deterministic bound \(|k_{x,i}^\Pi|\le C S\sqrt n\) is enough. Combining it with \(Ce^{-cn}\) and the preceding good-event moments yields
\[
\mathbb E_G\sup_{u\le S}\frac1n\sum_i|k_{x,i}^\Pi(u)|^4
\le C_B S^4.
\tag{4}
\]
The same assertion holds for training carriers. Their already-proved displacement moments also give, for every fixed \(p<\infty\),
\[
\sup_{a,i}\mathbb E_G
 \exp\!\left(p\sup_{u\le S}|p_{a,i}^\Pi(u)-p_{a,i}(0)|\right)
\le C_p.
\tag{5}
\]
The constants in (4)–(5) are uniform over deterministic first roots. No Gaussian conditioning is applied to the projected matrix itself off \(E_n\).

## 3. Exact activity derivative

Let \(s_x=1-h_x^2\), \(s_a=1-h_a^2\). Chain-rule differentiation of the actual controlled dense forward pass gives
\[
\frac{d f_n^b(u,x)}{du}=\sum_a b_a'(u)\Lambda_{xa}(u),
\]
\[
\Lambda_{xa}
=\frac{g_x^\top g_a}{n}
 +\frac{\delta_x^\top\delta_a}{n}\frac{h_x^\top h_a}{n}
 +c_a\frac{(s_x\odot k_x)^\top(s_a\odot k_a)}n.
\tag{6}
\]
For example, under \(db_a\), (3) changes by \(c_a s_a\odot k_a\,db_a\), which produces the last term. The readout and hidden-matrix updates produce the other two terms. Thus (6) is the true query-to-training tangent pairing.

## 4. Gaussian matrix variance

Fix all first roots. A change of initial hidden matrix gives a controlled-state variation \(D_X\le C\|\Delta W_0\|_F\), in the sum of transformed-coordinate RMS, readout RMS and hidden Frobenius variations. By (3), the query feature and carrier RMS variations are at most \(C_BD_X\).

In differentiating (6), the only terms not bounded by \(C_BD_X\) are gate variations multiplied by \(k_xk_a\). Cauchy--Schwarz and Hölder bound them by
\[
C_BD_X
\left(1+\left(\frac1n\sum_i|k_{x,i}|^4\right)^{1/2}
          +\left(\frac1n\sum_i|k_{a,i}|^4\right)^{1/2}\right).
\]
For instance \((n^{-1}\sum k_x^2k_a^2)^{1/2}\) is at most the geometric mean of the two displayed fourth-moment square roots. Since \(G\mapsto\Pi_K(G/\sqrt n)\) is \(n^{-1/2}\)-Lipschitz, almost-everywhere Gaussian gradients satisfy
\[
\|\nabla_G\Lambda_{xa}^\Pi\|_F^2
\le \frac{C_B}{n}
\left(1+\frac1n\sum_i|k_{x,i}^\Pi|^4
          +\frac1n\sum_i|k_{a,i}^\Pi|^4\right).
\]
The Gaussian variance inequality used and proved in POPULATION_CAVITY_ATTEMPT.md, together with (4), yields
\[
\operatorname{Var}_G(\Lambda_{xa}^\Pi\mid Z_0,\zeta_0)
\le C_B/n.
\tag{7}
\]

## 5. First-root variance and its weights

This step concerns two deterministic first-root arrays, before averaging over \(G\). For an increment \(U\), define
\[
J_z(a,U)=F^{-1}(F(a)+U).
\]
Since \((F^{-1})'(p)=\operatorname{sech}^2(F^{-1}(p))\) and
\(\big|\partial_p\log (F^{-1})'(p)\big|\le2\),
\[
|\partial_aJ_z(a,U)|\le e^{2|U|},\qquad
|\partial_UJ_z(a,U)|\le1.
\tag{8}
\]
The analogous training-feature function has derivative bound \(e^{4|U|}\), as proved in the earlier fluctuation note.

Writing \(U_a=p_a-p_a(0)\), the difference of training features is bounded by an exponentially weighted deterministic first-root difference plus the increment difference. Minkowski's inequality and (5) imply that the weighted forcing RMS has \(L^p(G)\) norm at most
\[
C_p\frac{\|\Delta Z_0\|_F}{\sqrt n}.
\]
Subtracting the controlled increment equations and applying their uniform Lipschitz estimate bounds the RMS increment, readout and matrix differences in \(L^p(G)\) by the same expression. Formula (8) and (3) then bound all query forward RMS differences by
\[
\frac{C_{B,p}}{\sqrt n}
\big(\|\Delta Z_0\|_F+\|\Delta\zeta_0\|_2\big).
\tag{9}
\]
Top-response and carrier differences obey (9) as well by bounded matrices and bounded readout coordinates.

To compare (6), use its two-factor product expansion. Gate differences multiplied by \(k_xk_a\) are bounded by their RMS difference times \((n^{-1}\sum k_x^2k_a^2)^{1/2}\). Taking expectation, Cauchy--Schwarz applies (9) with \(p=2\) and (4); all other factors have deterministic RMS bounds. Therefore the matrix-averaged function \(\mathbb E_G\Lambda_{xa}^\Pi\) is \(C_B/\sqrt n\)-Lipschitz in the Euclidean first-root array.

A second Gaussian variance inequality, followed by total variance and (7), gives
\[
\operatorname{Var}(\Lambda_{xa}^\Pi(u))\le C_B/n.
\tag{10}
\]
The weighted perturbations in this argument are deterministic before averaging over \(G\). No random multiplier norm is bounded by averaging its diagonal entries.

## 6. Whole-activity supremum and projection removal

Since \(b\) is deterministic, (10) and \(\sum_a|b_a'|\le1\) imply
\(\operatorname{Var}(\partial_u f_n^{\Pi,b}(u,x))\le C_B/n\) almost everywhere. The projected derivative is deterministically bounded, so differentiation passes through expectation by dominated integration.

The centered prediction starts at zero. Cauchy--Schwarz in activity gives
\[
\mathbb E\sup_{u\le S}
 |f_n^{\Pi,b}(u,x)-\mathbb Ef_n^{\Pi,b}(u,x)|^2
\le S\int_0^S
\operatorname{Var}(\partial_u f_n^{\Pi,b}(u,x))\,du
\le C_BS^2/n.
\]
Both projected and unprojected controlled predictions have absolute value at most \(S\), because \(\|w\|_\infty\le S\) and tanh features are bounded. They coincide on \(E_n\); removing the projection therefore adds only \(C S^2e^{-cn}\) to the mean-square bound, absorbable in \(C S^2/n\). This proves (1), and (2) follows by Tonelli.

## Scope

The result concerns one prescribed deterministic control, a full activity interval, and any fixed bounded query law. A deterministic physical-time residual history can be reparametrized by total variation, so its full physical-time supremum is included. The proof does not substitute a random adaptive control into a pointwise probabilistic result. CONTROLLED_FEEDBACK_STABILITY.md supplies that separate deterministic transfer.

The finite-width mean bias is not controlled by this fluctuation theorem. A local edge-response assumption that controls it is stated separately in DECISIVE_CONDITIONAL_ROUTE.md. No experiment or manuscript edit was used.
