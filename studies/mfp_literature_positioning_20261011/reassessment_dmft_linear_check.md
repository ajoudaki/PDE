# Independent check of the two-hidden-layer linear feature-kernel jet

The manuscript's coefficient is consistent with the full response-preserving DMFT equations of Bordelon and Pehlevan, but not with the explicit linear small-feature-learning formula printed in Appendix P.1.1. In the manuscript's half-mean-loss clock, the coefficient of physical time squared is

\[
J_{2,ab}=9\lambda_a\lambda_b,
\qquad \lambda_a=\frac1m\sum_cG_{ac}y_c.
\]

Thus, for the manuscript's two samples, \(J_{2,12}=\frac94(G_{11}y_1+G_{12}y_2)(G_{12}y_1+G_{22}y_2)\). The full journal equations give this same coefficient. The printed equation (P.4) instead gives \(4\lambda_a\lambda_b\). This is a specific internal discrepancy between the explicit perturbative formula and the response-preserving equations, not a counterexample to the full DMFT.

## Scope and sources

This was a scoped independent calculation. Scientific inputs were the network, clock, and feature-kernel passages in `paper_MFP/main.tex`, and the supplied journal PDF `data/generated/mfp_literature_positioning_20261011/reassessment_dmft/journal-nsf.pdf`, with its adjacent text extraction. No previous study reports, audits, compiler outputs, or other agents' findings were read. Required canonical-notation and rigorous-mathematics skills were applied.

The journal source is *Self-consistent dynamical field theory of kernel evolution in wide neural networks*, J. Stat. Mech. (2023) 114009, DOI 10.1088/1742-5468/ad01b0. The comparison uses the setup and response definitions (1)–(5), (13)–(15), the complete relevant Appendix F, and Appendix P. I visually verified the consequential equations on printed pages 6, 9, 38, 59, 60, and 65. PDF page numbers are one greater than printed page numbers. Rendered evidence and an independent numerical check are in `data/generated/mfp_literature_positioning_20261011/reassessment_dmft_linear_check/`.

## Network and clocks

Let \(x_a\in\mathbb R^d\) and \(y_a\in\mathbb R\), \(a=1,\ldots,m\), be fixed data, with \(G_{ab}=x_a^\top x_b/d\). For two hidden layers, identity activation, and no biases, write

\[
v_a=W^{(1)}x_a/\sqrt d,\qquad z_a=Wv_a,
\qquad f_{n,a}=w^\top z_a/n,
\qquad K_{n,ab}=z_a^\top z_b/n.
\]

Here \(W^{(1)}\in\mathbb R^{n\times d}\), \(W=W^{(2)}\in\mathbb R^{n\times n}\), and \(w=W^{(3)}\in\mathbb R^n\). Their independent initial entries have laws \(N(0,1)\), \(N(0,1/n)\), and \(N(0,1)\), respectively. Consequently the sample vectors \(v_a\) share the covariance \(\mathbb E[v_av_b^\top]=G_{ab}I\); they are not independent trainable sample variables.

The manuscript uses

\[
\mathcal L_n=\frac1{2m}\sum_c(f_{n,c}-y_c)^2,
\qquad
(\dot W^{(1)},\dot W,\dot w)
=-(n\nabla_{W^{(1)}}\mathcal L_n,
\nabla_W\mathcal L_n,n\nabla_w\mathcal L_n).
\]

Dots in the finite-network derivation below mean this physical clock \(t\).

In the journal, the unscaled hidden matrix has unit-variance entries and appears divided by \(\sqrt N\); the output is \(w^{L\top}h^L/(\gamma\sqrt N)\), with \(\gamma=\gamma_0\sqrt N\), and raw parameter mobility is \(\gamma^2\). Set \(N=n\), \(L=2\), identify the journal's \(W^0\) with \(W^{(1)}\), its \(W^1/\sqrt n\) with \(W\), and its \(w^2\) with \(w\). At \(\gamma_0=1\), this reproduces the manuscript architecture and stored-parameter mobilities exactly.

The journal initially defines \(\Delta_a=-\partial\mathcal L/\partial f_a\), allowing loss normalizations to be absorbed there. Its squared-loss specialization in Appendix F identifies \(\Delta=y-f\), which is the half-sum loss convention. Denote that journal clock by \(\tau\). Then

\[
\tau=t/m\quad(\gamma_0=1),
\qquad [t^2]K(t)=[\tau^2]H^2(\tau,\tau)/m^2.
\]

Equivalently one can keep the same clock in both sources and use \(\Delta=(y-f)/m\) in the journal. For the unhalved mean squared loss, the velocity doubles and the second coefficient is four times the half-mean coefficient. None of these changes alters the ratio \(9/4\) between the full equations and the printed perturbative coefficient.

## Direct finite-network derivation

Define the deterministic scalars and random initial vector

\[
\lambda_a=\frac1m\sum_cG_{ac}y_c,
\qquad \rho=\frac1{m^2}\sum_{c,e}y_cG_{ce}y_e,
\qquad s=\frac1m\sum_cy_cv_c,
\qquad B=WW^\top.
\]

The predictions tend to zero in every fixed finite moment. For example, conditioning first on \(W,v_a\) gives \(\mathbb E_w f_{n,a}^2=\|Wv_a\|^2/n^2\), hence \(\mathbb E f_{n,a}^2=G_{aa}/n\). The analogous fixed higher-moment bounds follow by Gaussian pairing. The fixed-degree normalized contractions occurring below have bounded moments by the same pairing argument. Hölder's inequality therefore allows initial residual values to be replaced by \(-y_c\) in the limiting expected jets. This replacement concerns residual values, not an assumption that the residual stays frozen during differentiation.

With that replacement, the first velocities are

\[
\dot W=ws^\top/n,\qquad
\dot w=Ws,\qquad
\dot v_a=\lambda_a W^\top w,
\qquad
\dot z_a=k_aw+\lambda_a Bw,
\qquad k_a=s^\top v_a/n\longrightarrow\lambda_a.
\]

The first kernel derivative has zero limiting expectation by readout centering. For the product of first feature velocities, conditioning on \(W,v\) and using \(\mathbb E[ww^\top]=I\) yields

\[
\lim_{n\to\infty}\mathbb E\frac{\dot z_a^\top\dot z_b}{n}
=\lambda_a\lambda_b\lim_{n\to\infty}
\mathbb E\frac{\operatorname{tr}(I+B)^2}{n}
=5\lambda_a\lambda_b.
\]

Indeed \(\mathbb E\operatorname{tr}B/n=1\) and \(\mathbb E\operatorname{tr}B^2/n=2+1/n\). The latter identity is obtained by pairing the four Gaussian entries in \(\sum_{i,j,k,l}W_{ik}W_{jk}W_{jl}W_{il}\): the three pairings contribute \(n,n,1\) before division by \(n\).

Residual derivatives make no surviving contribution to the expected pairing \(z_a^\top\ddot z_b/n\). One can see this without assuming those derivatives vanish. The exact tangent kernel entering \(\dot f\) is even in the centered readout \(w\), whereas the per-residual feature velocity is linear in \(w\). After replacing the initial residual values by \(-y\), the residual-derivative part of the second feature derivative is odd in \(w\), while \(z_a\) is independent of \(w\); its expectation is zero. Terms arising from the discarded initial predictions vanish by the preceding moment bounds.

It remains to differentiate the displayed first velocities while holding the initial label coefficients fixed. Then

\[
\dot s=\rho W^\top w,
\quad
\dot k_b=\rho\,w^\top z_b/n+\lambda_b w^\top Ws/n,
\quad
\dot B=\{w(Ws)^\top+(Ws)w^\top\}/n.
\]

The three terms with nonzero limiting pairings against \(z_a\) are

\[
k_bWs,
\qquad \lambda_b(Ws)(w^\top w/n),
\qquad \lambda_b BWs.
\]

Since \(\mathbb E[v_as^\top\mid W]=\lambda_a I\), their limiting pairings contribute, respectively,

\[
\lambda_a\lambda_b,
\qquad \lambda_a\lambda_b,
\qquad 2\lambda_a\lambda_b.
\]

The terms involving \(w\dot k_b\) or \(w(Ws)^\top w/n\) have vanishing normalized pairings. For example, the conditional variance of \(w^\top z_a/n\) is \(\|z_a\|^2/n^2=O_{L^p}(n^{-1})\); Cauchy–Schwarz then bounds the relevant products. Consequently

\[
\lim_n\mathbb E\frac{z_a^\top\ddot z_b}{n}
=4\lambda_a\lambda_b,
\]

and the factorial-normalized kernel coefficient is

\[
J_{2,ab}
=\frac12\lim_n\mathbb E\frac{
\ddot z_a^\top z_b+2\dot z_a^\top\dot z_b+z_a^\top\ddot z_b}{n}
=\frac{4+10+4}{2}\lambda_a\lambda_b
=9\lambda_a\lambda_b.
\]

This calculation requires neither whitening nor invertibility of \(G\). If one of the two \(\lambda\)'s vanishes, both compared scalar coefficients vanish and that entry cannot discriminate the formulas.

## Expansion of the full journal equations

Use the journal's half-sum clock \(\tau\) and its notation \(H^\ell=\Phi^\ell\) for linear features. The journal's \(G^\ell\) is a backward covariance, distinct from the input Gram \(G=K^x\). The zero-feature-learning residual is \(\Delta_0(\tau)=\exp[-(L+1)G\tau]y\), since the initial tangent kernel is \((L+1)G\). Define causal integral operators \(\bar C\) and \(\bar D\) explicitly by

\[
(\bar Cg)_a(\tau)=\int_0^\tau du\,
\sum_cG_{ac}\Delta_{0,c}(u)g(u),
\qquad
(\bar Dh)(\tau)=\int_0^\tau du\,
\sum_c\Delta_{0,c}(u)h_c(u).
\]

At \(\gamma_0=0\), the covariances are \(H^0_{ab}(\tau,\sigma)=G_{ab}\) and \(G^{\ell,0}(\tau,\sigma)=1\). The response definitions in (14) include a factor \(\gamma_0^{-1}\). Their leading limits therefore need not vanish even though the unnormalized functional responses are of order \(\gamma_0\).

Equations (F.2) and (F.4), with \(A^0=B^L=0\), imply

\[
A^{\ell,0}=C^{\ell,0},\qquad
B^{\ell-1,0}=D^{\ell,0},
\]

and hence the recursions

\[
C^{\ell,0}=C^{\ell-1,0}+\bar C=\ell\bar C,
\qquad
D^{\ell,0}=D^{\ell+1,0}+\bar D=(L+1-\ell)\bar D.
\]

For \(L=2\), the four needed leading operators are thus

\[
C^{1,0}=\bar C,\quad D^{1,0}=2\bar D,
\qquad C^{2,0}=2\bar C,\quad D^{2,0}=\bar D.
\]

In particular, the backward response \(B^{1,0}=\bar D\) affects the first-layer feature covariance, and the forward response \(A^{1,0}=\bar C\) affects the second layer. Both must be retained.

Expanding the first resolvent identity in (F.4) gives the coefficient \(H^{\ell,2}\) of \(\gamma_0^2\):

\[
H^{\ell,2}=H^{\ell-1,2}
+C^{\ell,0}D^{\ell,0}H^0
+H^0D^{\ell,0\top}C^{\ell,0\top}
+C^{\ell,0}\mathbf1\mathbf1^\top C^{\ell,0\top}.
\]

This identity includes the preceding layer's covariance correction, the two response-feedback terms, and the product of the first feature perturbations. Keeping all four terms and using \(H^{0,2}=0\) yields

\[
\begin{aligned}
H^{1,2}&=2\{\bar C\bar D H^0+H^0\bar D^\top\bar C^\top\}
+\bar C\mathbf1\mathbf1^\top\bar C^\top,\\
H^{2,2}&=4\{\bar C\bar D H^0+H^0\bar D^\top\bar C^\top\}
+5\bar C\mathbf1\mathbf1^\top\bar C^\top.
\end{aligned}
\]

Define \(a_b=\sum_cG_{bc}y_c\). Since \(\Delta_0(u)=y+O(u)\) at the origin,

\[
\begin{aligned}
(\bar C\bar D H^0)_{ab}(\tau,\sigma)
&=\tfrac12a_aa_b\tau^2+\text{terms of total time degree at least three},\\
(\bar C\mathbf1\mathbf1^\top\bar C^\top)_{ab}(\tau,\sigma)
&=a_aa_b\tau\sigma+\text{terms of total time degree at least three}.
\end{aligned}
\]

The full equations therefore give the second-degree two-time polynomial

\[
H^2_{ab}(\tau,\sigma)
=G_{ab}+\gamma_0^2a_aa_b
\{2\tau^2+5\tau\sigma+2\sigma^2\}
+\text{higher time degrees}.
\]

On the time diagonal the coefficient is \(9\gamma_0^2a_aa_b\). At \(\gamma_0=1\), \(\tau=t/m\), this is exactly \(9\lambda_a\lambda_b\), including the factorial normalization. The first-layer time-diagonal coefficient is \(3\gamma_0^2a_aa_b\); the second layer adds \(6\gamma_0^2a_aa_b\).

This computation is a formal local consequence of the supplied DMFT equations. It does not establish positive-time convergence or exchange time differentiation with the width limit. The finite-width calculation above independently establishes the expected initial coefficient. The local-time coefficient is proportional to \(\gamma_0^2\) for arbitrary fixed \(\gamma_0\): additional resolvent feedback involves additional causal integrals and cannot contribute at time degree two. Thus the comparison is not justified by merely substituting \(\gamma_0=1\) into an uncontrolled positive-time small-\(\gamma_0\) approximation.

## What Appendix P does and does not agree with

The text immediately before (P.2) declares the leading \(C^\ell\) and \(D^\ell\) to be independent of layer. The definitions immediately after (P.2) identify their actions precisely with \(\bar C\) and \(\bar D\) above, without the leading response contributions. Equation (P.4) then gives

\[
H^\ell_{ab}(\tau,\sigma)
=G_{ab}+\ell\gamma_0^2\sum_{c,e}G_{ac}G_{be}
\{v_{ce}(\tau)+v_{ec}(\sigma)+v_c(\tau)v_e(\sigma)\}
+O(\gamma_0^4),
\]

where \(v_c(\tau)=\int_0^\tau\Delta_c(u)du\) and \(v_{ce}(\tau)=\int_0^\tau\Delta_c(u)\int_0^u\Delta_e(v)dv\,du\). Their initial expansions are \(v_c(\tau)=y_c\tau+O(\tau^2)\) and \(v_{ce}(\tau)=y_cy_e\tau^2/2+O(\tau^3)\). For \(\ell=L=2\), the resulting second-degree polynomial is

\[
G_{ab}+\gamma_0^2a_aa_b
\{\tau^2+2\tau\sigma+\sigma^2\}.
\]

Its time-diagonal coefficient is \(4\gamma_0^2a_aa_b\), hence \(4\lambda_a\lambda_b\) in the manuscript clock. The discrepancy survives both the loss-clock conversion and the division by \(2!\). A concrete nonsingular example is \(G=I_2\), \(y=(1,1)^\top\): the manuscript/full-DMFT coefficient for entry \((1,2)\) is \(9/4\), whereas (P.4) gives \(1\).

The structural error in this explicit expansion is localized: \(H^{\ell,0}\) and \(G^{\ell,0}\) are layer independent, but their equality does not imply the same for the normalized response-dependent operators \(C^{\ell,0},D^{\ell,0}\). Those operators satisfy the recursions derived above. With one hidden layer, both leading response boundary terms vanish and this particular discrepancy disappears; it is already present with two hidden layers.

Appendix P also contains more general formulas that should not be conflated with its explicit linear expression. The implicit equation (P.6), the covariance propagation in (P.20), and the terms retained in (P.22) reproduce the correct linear recursion when \(\phi(u)=u\) and the properly normalized operators from (13)–(14), (F.2)–(F.4) are supplied. In that specialization, the first perturbation product, the \(CD\) term and its transpose, and the propagated covariance remain; the terms involving \(\phi''\) vanish. These are exactly the terms used above.

There are printed local inconsistencies which prevent reading every displayed equation in F/P literally as one internally identical system:

- (F.1) has an additional \(\gamma_0\) inside the backward direct-update bracket, whereas (13), (F.2), and (F.3) do not. The comparison above explicitly uses the mutually consistent equations (13)–(15), (F.2)–(F.4), not this extra factor. At the manuscript's \(\gamma_0=1\) the extra factor has no numerical effect, but it matters in a literal small-\(\gamma_0\) reading.
- (P.21) prints response superscripts \(A^{\ell-1,1}\), \(B^{\ell,1}\) rather than the zeroth-order coefficients of the normalized responses defined in (14). It also prints a forward covariance \(\Phi^{\ell-1,0}\) in the direct term of \(D^{\ell,0}\), whereas (13) and (F.2) use the backward covariance \(G^{\ell+1,0}\). These are visible in the PDF. They are not a basis for silently replacing the explicit (P.4) by the full-response result.

This report does not certify all nonlinear perturbative formulas or all depth-scaling conclusions in Appendix P. Its definite mathematical conclusion is the two-hidden-layer linear discrepancy in (P.2)–(P.4), together with agreement between the manuscript coefficient and the full response-preserving equations. The full theory already encodes this coefficient; the coefficient cannot be presented as an effect missing from that full theory.

## Independent numerical check

The [retained check source](reassessment_dmft_linear_check.py) differentiates the finite network's full moving flow twice, including residual, first-layer, hidden-matrix, and readout changes. It imports no manuscript compiler or maintained repository code. With \(G=I_2\), \(y=(1,1)^\top\), its estimates for the coefficient of \(K_{12}\) are:

| Width | Independent initializations | Mean second coefficient | Standard error |
|---:|---:|---:|---:|
| 64 | 1000 | 2.34153 | 0.03046 |
| 128 | 600 | 2.27944 | 0.02521 |
| 256 | 300 | 2.28642 | 0.02477 |
| 512 | 120 | 2.25606 | 0.02724 |

These finite-width measurements support the analytic value \(2.25\) and distinguish it from \(1\); they are a numerical sanity check, not the proof. The seed and exact calculation are recorded in the script, and the results are saved in [finite_jet_check.json](/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/reassessment_dmft_linear_check/finite_jet_check.json). From the checkout root, run `OPENBLAS_NUM_THREADS=1 python -B studies/mfp_literature_positioning_20261011/reassessment_dmft_linear_check.py`. The coordinator moved the unchanged scratch script into the flat study source directory after this review.
