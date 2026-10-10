# A sharper upper-bound route for the unchanged Legendre method

Date: 2026-10-10. Status: exact primitive and comparison lemmas; the improved spectral estimate remains open. This is a scoped theoretical calculation in the existing study. Its scientific inputs are `paper/compact.tex`, `paper/compact_legendre.tex`, `paper/compact_fitting.tex`, `paper/compact_foundations.tex`, and `ORIGINAL_OUTPUT_ANALYSIS.md`. No experiment, paper modification, alternative clock, changed prefix, or modified evolution is used.

The target is the paper's unchanged residual-RMS-clock construction, with unit prefix and the stated activation class, fixed depth and data, positive fixed labels satisfying the existing cap, and all-time whole-sphere prediction error negligible relative to independent dense-run variability. The question is whether an order \(q=n^a\), with \(a<1/10\), can be justified. The known onset lower bound \(q^{-10}\) does not answer this question.

The useful new bridge below is that the supremum of the signed defect primitive can replace the total variation of the defect in the stability argument. It costs only a factor polynomial in the square root of the time horizon, besides the already present subpolynomial stability factor. Consequently a sufficiently strong cross-tail estimate would transfer to the requested observable. This calculation does **not** establish such an estimate with power greater than five.

## Exact defect primitive

Use the network, residuals, and mobility coordinates of the paper. Write

\[
\theta_D=(W_D^{(1)}/\sqrt n,W_D^{(2)},\ldots,W_D^{(L)},w_D/\sqrt n),
\]

and use hats for the reconstructed Legendre state. Let
\(\widehat\rho=\|\widehat r\|_2/\sqrt m\) and
\(\tau(t)=1+\int_0^t\widehat\rho(s)\,ds\). For each training sample and hidden interface, the proof histories are

\[
h_a(\tau(t))=\widehat h_a(t),\qquad
b_a(\tau(t))=\frac{\widehat r_a(t)}{\widehat\rho(t)}\widehat\delta_a(t).
\]

Their prefix values are \(h_{0,a}\) and zero on \([0,1]\). All layer indices below are retained when needed. For an interval \([0,A]\), let \(\Pi_q^A\) denote the ordinary orthogonal Legendre projection onto degrees below \(q\), and define the matrix

\[
R_\ell(A)=\frac{2}{mn}\sum_{a=1}^m
\int_0^A
[(I-\Pi_q^A)b_a^{(\ell)}](\xi)
[(I-\Pi_q^A)h_a^{(\ell-1)}](\xi)^\top\,d\xi,
\qquad 2\le\ell\le L.                                      \tag{1}
\]

Let \(R(t)\) be the parameter tuple with zero first-layer and readout blocks and hidden blocks \(R_\ell(\tau(t))\). Then

\[
R(0)=0,\qquad \dot R(t)=\mathcal E(t),                       \tag{2}
\]

where \(\mathcal E\) is exactly the physical defect in the paper.

Indeed orthogonality gives

\[
\int_0^A bh^\top-\int_0^A(\Pi_q^A b)(\Pi_q^A h)^\top
=\int_0^A[(I-\Pi_q^A)b][(I-\Pi_q^A)h]^\top.
\]

Differentiating the right side, its interior derivative terms vanish: each differentiated projection is still a polynomial of degree below \(q\), and the other factor is orthogonal to every such polynomial. The resulting derivative is the product of the two endpoint projection errors. Multiplication by \(\dot\tau=\widehat\rho\) gives the defect formula. At \(A=1\) the backward history vanishes, so (2) has no integration constant. Equivalently, reconstruction is the uncompressed integral of its own gradient updates plus (1).

This identity is exact for the moving interval and the actual closure histories. It is not an error estimate for dense histories substituted in place of those histories.

## Primitive-forcing stability

The following deterministic lemma avoids differentiating \(R\) in its bound.

Let \(F\) map a finite-dimensional Euclidean parameter space into sample space with norm \(\|u\|_m^2=m^{-1}\sum_a u_a^2\). Set

\[
r=F(\theta)-y,\quad r_D=F(\theta_D)-y,\quad
J=DF(\theta),\quad J_D=DF(\theta_D),\quad d=\theta-\theta_D.
\]

Suppose

\[
\dot\theta=-2J^*r+\dot R,\qquad
\dot\theta_D=-2J_D^*r_D,\qquad \theta(0)=\theta_D(0),\quad R(0)=0,
\]

and for constants \(K,B\ge0\), throughout \([0,T]\),

\[
\begin{aligned}
\|r-r_D-J_Dd\|_m&\le K\|d\|^2/2,\\
\|J-J_D\|&\le K\|d\|,\qquad \|J_D\|\le B.
\end{aligned}                                                \tag{3}
\]

The operator norms in (3) use the specified parameter and sample norms. Write

\[
\varepsilon_T=\sup_{t\le T}\|R(t)\|,\qquad
I_T=K\int_0^T(\rho_D+4\rho)\,dt,
\quad \rho_D=\|r_D\|_m,\quad\rho=\|r\|_m.
\]

Then

\[
\sup_{t\le T}\|d(t)\|
\le\varepsilon_T\left[
1+e^{2I_T}\sqrt{4I_T+2K\int_0^T\rho\,dt+2B^2T}\right].       \tag{4}
\]

To prove this, put \(z=d-R\), \(v=-2J^*r\), and \(v_D=-2J_D^*r_D\). The same signed subtraction as in the paper gives

\[
\langle d,v-v_D\rangle
\le-2\|r-r_D\|_m^2
+K(\rho_D+3\rho)\|d\|^2.                                  \tag{5}
\]

For completeness, writing \(S=r-r_D-J_Dd\), the equality before this inequality is

\[
-2\|r-r_D\|_m^2
+2\langle r-r_D,S\rangle_m
-2\langle r,(J-J_D)d\rangle_m.
\]

The two assumptions in (3), together with \(\|r-r_D\|_m\le\rho+\rho_D\), prove (5). Exact vector-field subtraction also gives

\[
\|v-v_D\|
\le2B\|r-r_D\|_m+2K\rho\|d\|.
\]

Because \(\dot z=v-v_D\), Young's inequality therefore yields

\[
\begin{aligned}
\tfrac12\partial_t\|z\|^2
&=\langle d,v-v_D\rangle-\langle R,v-v_D\rangle\\
&\le-\|r-r_D\|_m^2
 +K(\rho_D+4\rho)\|d\|^2
 +(B^2+K\rho)\varepsilon_T^2.
\end{aligned}
\]

Set \(a(t)=K(\rho_D+4\rho)\) and use
\(\|d\|^2\le2\|z\|^2+2\varepsilon_T^2\). Dropping the negative term gives

\[
\partial_t\|z\|^2
\le4a(t)\|z\|^2+
2[2a(t)+B^2+K\rho(t)]\varepsilon_T^2.
\]

Integration with \(z(0)=0\), followed by \(\|d\|\le\|z\|+\varepsilon_T\), proves (4). No bound on \(\int\|\dot R\|\) or \(\sup\|\dot R\|\) was used.

## Application to the original all-time observable

On the event already used in `compact_legendre.tex`, its actual dense-to-closure gradient subtraction proves (3) with

\[
K=K_0+K_1M=O_{\rm problem}(1+\sqrt{\log(en)}),
\]

where \(K_0,K_1,M\) are the explicitly defined coefficients in that proof. The proof bounds each training output gradient difference by \(K\|d\|\); sample RMS therefore gives the full operator bound in (3). Its segment remainder proves the first bound. The real fitting tube bounds the dense gradient blocks and supplies \(B=O_{\rm problem}(1)\).

With \(\lambda=\gamma/m\), the paper gives

\[
\int_0^\infty\rho_D\le2Y/\lambda,\qquad
\int_0^\infty\widehat\rho\le4Y/\lambda.
\]

Consequently \(I_T\le18KY/\lambda\), uniformly in the horizon, and (4) implies

\[
\sup_{t\le T}\|\widehat\theta(t)-\theta_D(t)\|
\le n^{o(1)}(1+\sqrt T)\varepsilon_T.                       \tag{6}
\]

Here and below \(n^{o(1)}\) is for each fixed admissible problem and is independent of \(q,T\), apart from factors displayed explicitly. In particular it does not hide a power of \(q\). Whole-sphere output subtraction multiplies (6) by a fixed-problem constant.

The extension beyond a finite horizon also has no order-dependent constant. Let \(\kappa=\lambda/4\), and let \(\mathcal F\) denote the dense gradient vector field evaluated on the closure state. The fitting proof supplies

\[
-\partial_t\widehat\rho^2\ge\|\mathcal F\|^2/2,
\qquad \widehat\rho(u)\le\widehat\rho(t)e^{-\kappa(u-t)},
\qquad \|\mathcal E(u)\|\le C_E\widehat\rho(u),
\]

with \(C_E\) independent of \(q,n\) for the fixed problem. Integrating the first inequality against \(e^{\kappa(u-t)}\) gives

\[
\int_t^\infty e^{\kappa(u-t)}\|\mathcal F(u)\|^2\,du
\le4\widehat\rho(t)^2.
\]

Weighted Cauchy--Schwarz and integration of the defect bound now give

\[
\int_t^\infty\|\dot{\widehat\theta}(u)\|\,du
\le\left(2/\sqrt\kappa+C_E/\kappa\right)\widehat\rho(t).
\]

The dense parameter tail is already supplied by its fitting lemma. The real forward/readout subtraction bounds therefore imply, for every \(T\ge0\),

\[
\|f_{\rm Leg}-f_n\|_*
\le n^{o(1)}(1+\sqrt T)\varepsilon_T
   +C_{\rm problem}Y e^{-\kappa T}.                         \tag{7}
\]

This includes the fitted endpoint and all sphere queries. For any fixed desired power \(p>0\), choosing

\[
T_q=(p+1)\log(eq)/\kappa
\]

reduces the second term to \(O_{\rm problem}(Yq^{-p-1})\). Thus an independently proved estimate

\[
\varepsilon_{T_q}\le Y n^{o(1)}q^{-p}                       \tag{8}
\]

would give all-time error \(Y n^{o(1)}q^{-p}\), absorbing the logarithmic factor when \(q\) is a fixed power of \(n\). The established lower bound on dense variability would then prove the required relative accuracy whenever \(ap>1/2\) for \(q=\lceil n^a\rceil\). To obtain some \(a<1/10\) by this route requires \(p>5\). A \(p=5\) result alone does not suffice.

## What the existing history bounds actually imply

For any history family \(g_a\in\mathbb R^n\), use the aggregate history norm

\[
\|g\|_{A,\mathrm{hist}}^2
=\frac1{mn}\sum_a\int_0^A\|g_a(\xi)\|_2^2\,d\xi.
\]

Cauchy--Schwarz in (1) gives the exact bound

\[
\|R_\ell(A)\|_F
\le2\|(I-\Pi_q^A)b^{(\ell)}\|_{A,\mathrm{hist}}
       \|(I-\Pi_q^A)h^{(\ell-1)}\|_{A,\mathrm{hist}}.         \tag{9}
\]

The proved forward estimate is \(F_h/q\). The proved backward estimate, including the same-clock dense-response comparison used in the paper, is

\[
\frac{b_0+b_1\sqrt{\log q}}q
+B_d\sqrt{a_0}\sup_{t\le T}D(t),
\]

where \(a_0,F_h,b_0,b_1,B_d,D\) are exactly the quantities defined in that proof. Hence (9) and (6) yield the same \(q^{-2}\) forcing order and an absorbable \(q^{-1}D\) feedback. For \(q\) polynomial in \(n\), the absorption threshold remains \(n^{o(1)}\) on \(T=O(\log q)\). The primitive lemma by itself does not improve the established power.

To improve (9), one must either prove sharper tails of the actual histories or exploit cancellation in their signed pairing. These are extra scientific claims. Physical-time analyticity of the dense source is not an estimate for derivatives in the residual clock of the closure histories.

## Precise unclosed bridges

1. **Onset regularity.** The initial readout vanishes, so the backward history begins to first order and a forward feature begins to second order after the unit prefix. On a regular interior join, these unequal orders suggest stronger spectral decay than the existing weighted first-derivative inequality. Even that local observation does not establish uniform derivative bounds for the entire \(q\)-dependent closure trajectory. Differentiating its pointwise defect differentiates the moving endpoint projection and can introduce positive powers of \(q\).

2. **Signed cross-tail cancellation.** Unequal onset orders can put the leading Legendre coefficients in different oscillatory phases. This is a potential gain over (9), but a theorem must be uniform in the current endpoint \(A=\tau(t)\), including the regime \(A-1=O(q^{-2})\). It must also bound remainders for the actual histories. The primitive identity eliminates the subsequent need to estimate total variation; it does not prove that the primitive is small.

3. **The terminal residual clock.** The stated hypotheses supply residual decay and a bound on the physical-time speed of the normalized residual, not a positive lower bound on a separation between its decay rates. For example, the purely linear residual path \(r(t)=c_1e^{-\mu t}v_1+c_2e^{-\nu t}v_2\), for orthonormal \(v_1,v_2\), \(c_1c_2\ne0\), and \(0<\mu<\nu\), has remaining activity proportional to \(e^{-\mu t}\), while its normalized direction has a correction of order \(e^{-(\nu-\mu)t}\). Expressed in remaining activity, this is a fractional power with exponent \((\nu-\mu)/\mu\). The assumptions impose no uniform positive lower bound on that ratio. This example identifies a missing regularity implication; it is not asserted to be an actual counterexample trajectory of the neural closure.

4. **Dense-to-closure substitution.** Substituting dense histories in (1) is not automatic. At equal physical time their states are close, but the dense and closure residual clocks differ. The map from physical time to the closure clock has derivative \(1/\widehat\rho\), which becomes unbounded near fitting. The existing weighted first-derivative argument cancels this denominator once. A higher-order estimate must display the corresponding cancellations rather than assume bounded clock derivatives. The same issue survives if one evaluates dense features on the closure clock.

5. **Width dependence of higher forward derivatives.** Bounded real activation derivatives and parameter RMS speeds alone do not provide width-independent higher feature derivatives: a term \(\phi''(z)\odot(z')^{\odot2}\) requires more than an RMS bound on \(z'\). A crude RMS-to-coordinate conversion loses a factor \(\sqrt n\). The supplied probabilistic source theorem controls actual dense responses, not the closure carriers or all parameter states in a neighborhood. A closure regularity bootstrap must address this distinction.

These are major missing estimates for this upper route, rather than evidence that the requested theorem is false. The exact comparison mechanism (7) is now available: the decisive remaining target is the signed primitive estimate (8) with \(p>5\), or a direct observable cancellation that improves on the parameter primitive. No such estimate is established here.
