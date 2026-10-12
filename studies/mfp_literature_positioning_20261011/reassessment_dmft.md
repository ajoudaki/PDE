# Independent reassessment of DMFT relative to MFP

Review completed 2026-10-11. Scope: the complete current `paper_MFP/main.tex`; the complete 55-page NeurIPS camera-ready manuscript, arXiv:2205.09653v3; and the complete 70-page JSTAT 2023 article, including all appendices, plus its cover. No previous review or other study was consulted. Required mathematical-presentation and rigorous-solution skills were applied. The comparison below distinguishes an external paper's derivation, consequences supplied by its cited Tensor Programs foundation, and additional calculations made in this review.

The journal was read completely through the author PDF's cached browser text, then obtained as the identical titled, numbered publisher edition from the [NSF public repository](https://par.nsf.gov/servlets/purl/10541946). Journal page references below are **printed page numbers**, so the PDF page number is one larger. The [author copy](https://pehlevan.seas.harvard.edu/sites/g/files/omnuum6471/files/pehlevan/files/bordelonpehlevan_jstat_2023.pdf) and [DOI](https://doi.org/10.1088/1742-5468/ad01b0) identify the edition. The conference version is [arXiv v3](https://arxiv.org/pdf/2205.09653v3). The paper-linked [implementation](https://github.com/Pehlevan-Group/dmft_wide_networks) was inspected at commit `d6b075182c4127ccf60f74c2139af36de26defc4`; the official NeurIPS code supplement was also retrieved. Relevant Tensor Programs statements were checked in the [TP IV supplement](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf), §§G, L.

**Assessment.** DMFT is very close to MFP at the level of the Gaussian source-response mechanism. It already supplies forward/backward source fields, covariance self-consistency, expected source derivatives, an implementation of those derivatives, and symbolic perturbation calculations involving Gaussian covariance derivatives. MFP should not be positioned as introducing that mechanism, or as making derivatives of feature-learning observables accessible for the first time. The defensible distinction is a systematically specified finite language, exact finite-width differentiation and moving-jet closure, a stated all-finite-\(L^p\) expectation theorem with uniform moments and singular queries, and an executable symbolic expectation graph. Those are useful additions; their value does not require denying the existing DMFT/TP calculus.

There is also a material qualification: DMFT's published **linear perturbative shortcut** is inconsistent with its full response equations already at the second initial feature-kernel derivative. The full equations recover MFP's linear check. Thus the comparison should credit the full framework while avoiding uncritical reuse of every published perturbative formula.

**The models really overlap after normalization.** Write \(n\) for width, \(m\) for the fixed number of data points, \(d\) for input dimension, and \(L\) for the number of hidden layers. Use canonical preactivations \(z_a^{(\ell)}\) and activations \(h_a^{(\ell)}=\phi(z_a^{(\ell)})\), with fixed inputs \(x_a\) and
\[
K^x_{ab}=\frac{x_a^\top x_b}{d}.
\]
The source paper calls our \(z^{(\ell)}\) by \(h^\ell\), and calls its pregradient by \(z^\ell\). Below its pregradient is \(p^{(\ell)}\), so its gradient field is \(g^{(\ell)}=\phi'(z^{(\ell)})p^{(\ell)}\).

Let \(W^{\mathrm{BP},0},\ldots,W^{\mathrm{BP},L-1},w^{\mathrm{BP},L}\) denote the paper's raw parameters, initialized with independent standard Gaussian entries. Its Eq. (1), p. 6, gives first-layer scaling \(d^{-1/2}\), hidden scaling \(n^{-1/2}\), and output scaling \((\gamma\sqrt n)^{-1}\). The rich regime is \(\gamma=\gamma_0\sqrt n\), with fixed \(\gamma_0>0\), and the raw gradient-flow mobility is \(\gamma^2=\gamma_0^2n\). Define
\[
W^{(1)}=W^{\mathrm{BP},0},\qquad
W^{(\ell)}=\frac{W^{\mathrm{BP},\ell-1}}{\sqrt n}\quad(2\leq\ell\leq L),
\qquad
w=\frac{w^{\mathrm{BP},L}}{\gamma_0}.
\]
Then
\[
z_a^{(1)}=\frac{W^{(1)}x_a}{\sqrt d},\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
f_a=\frac{w^\top h_a^{(L)}}n.
\]
This is MFP's neural model, with readout variance \(\tau^2=\gamma_0^{-2}\). Transforming the gradient flow gives first-layer mobility \(n\gamma_0^2\), hidden-matrix mobility \(\gamma_0^2\), and readout mobility \(n\). At \(\gamma_0=1\), these are MFP's unit block multipliers. This is an exact parameter change, not merely a similarity of scaling exponents.

Loss normalization must also be matched. The theoretical DMFT equations use \(\Delta_a=-\partial\mathcal L/\partial f_a\), with an unnormalized loss sum in Appendix D.1. For half-mean square loss, \(\Delta_a=(y_a-f_a)/m\); for full-mean square loss it is \(2(y_a-f_a)/m\). Multiplying the loss by a constant rescales time and multiplies an order-\(q\) jet by that constant to power \(q\). The released nonlinear notebook uses half-mean square loss and explicitly divides its residual evolution and field updates by \(m\); its finite-network comparison also subtracts the initial prediction. That centering changes finite-width observations but disappears in this rich infinite-width limit.

The relevant input Gram can be any fixed positive semidefinite \(K^x\); whitened data are a special simplification in Appendix F, not a hypothesis of the full theory. The journal Appendix N.1–N.5, pp. 54–57, treats the fixed-dimensional first layer separately and establishes the corresponding \(\mu P\) parameterization without assuming \(d\asymp n\). The older conference Appendix N contained a first-layer discussion involving \(D\sim N\); treating that as a limitation of the current journal version would be incorrect.

The paper states twice differentiable activation at Eq. (1), but its higher perturbation calculations use additional derivatives. It does not state the all-orders polynomial-growth hypothesis needed for arbitrary-order classical jets. Its ReLU numerical examples therefore do not establish an arbitrary-order smooth derivative theorem. Neither paper lets the data count, depth, derivative order, or training-query count grow with width in the claims relevant here.

**The source-response correspondence is direct.** Define
\[
\Phi^\ell_{ab}(t,s)=\mathbb E[h_a^{(\ell)}(t)h_b^{(\ell)}(s)],
\qquad
G^\ell_{ab}(t,s)=\mathbb E[g_a^{(\ell)}(t)g_b^{(\ell)}(s)].
\]
DMFT Eqs. (13)–(14), p. 9, and (D.44), p. 34, specify independent Gaussian source families \(u^\ell,r^\ell\) with covariances \(\Phi^{\ell-1},G^{\ell+1}\), respectively, and
\[
\begin{aligned}
z_a^{(\ell)}(t)
 &=u_a^\ell(t)+\gamma_0\int_0^t\sum_b
 [A^{\ell-1}_{ab}(t,s)+\Delta_b(s)\Phi^{\ell-1}_{ab}(t,s)]
 g_b^{(\ell)}(s)\,ds,\\
p_a^{(\ell)}(t)
 &=r_a^\ell(t)+\gamma_0\int_0^t\sum_b
 [B^\ell_{ab}(t,s)+\Delta_b(s)G^{\ell+1}_{ab}(t,s)]
 h_b^{(\ell)}(s)\,ds,\\
A^\ell_{ab}(t,s)
 &=\gamma_0^{-1}\mathbb E\!\left[\frac{\delta h_a^{(\ell)}(t)}
 {\delta r_b^\ell(s)}\right],\qquad
B^\ell_{ab}(t,s)
 =\gamma_0^{-1}\mathbb E\!\left[\frac{\delta g_a^{(\ell+1)}(t)}
 {\delta u_b^{\ell+1}(s)}\right].
\end{aligned}
\]
Here \(\Phi^0=K^x\), \(G^{L+1}=1\), and \(A^0=B^L=0\). The expectations are over the source-generated fields, which generally cease to be Gaussian after training. Source independence does **not** imply independence of the resulting fields.

MFP's `eq-mfp-source-response` expresses the same structural mechanism for an arbitrary finite sequence of calls to a named Gaussian matrix and its transpose:
\[
Wh\longmapsto \xi+\sum_s U_s\,\mathbb E[\partial_{\zeta_s}H],
\qquad
W^\top u\longmapsto \zeta+\sum_r H_r\,\mathbb E[\partial_{\xi_r}U].
\]
Here \(H,U\) are the scalar representatives of vector inputs, \(\xi,\zeta\) are named Gaussian sources, and each sum runs over earlier calls in the opposite orientation. Each covariance is the corresponding uncentered input second moment. In a discretized training history the response sums become the history kernels \(A,B\); the extra \(\Delta\Phi,\Delta G\) terms arise from accumulated rank-one weight updates. This is precisely the kind of equivalence that the journal makes explicit in Appendix N.6 and Table N1, p. 57.

The derivation is substantial: the Gaussian weight average in (D.26), p. 29, creates the forward/transpose cross term; stationarity of the order-parameter action appears in (D.30)–(D.33), pp. 30–31; the Hubbard transform in (D.38)–(D.40), pp. 33–34, introduces Gaussian source fields; and Stein integration by parts produces the expected derivatives in (D.43). Appendix O, p. 58, separately sets \(A=B=0\) to define the **gradient-independence approximation**. Calling full DMFT an independence approximation would miss the central construction.

MFP's formal source derivative keeps previously computed scalar limits and covariance entries fixed, while physical differentiation propagates through scalar feedback. DMFT uses the corresponding source-response distinction. Its Appendix P.13–P.15, p. 63, additionally differentiates Gaussian expectations with changing covariance, expressing the change through an expected Hessian. It is consequently inaccurate to say that DMFT contains neither a derivative-to-Gaussian-expectation calculus nor a way to account for moving Gaussian laws.

**What is rigorous, and what remains formal.** The finite-width dynamical identities and Gaussian weight averages precede a formal large-\(n\) stationary-action argument. The paper does not prove that its continuum path integral concentrates at a unique saddle, that the full nonlinear self-consistent process has a unique solution under a stated general hypothesis set, or that its alternating numerical iteration converges. Section 7, p. 16, acknowledges the heuristic character of the physics derivation. Appendix M, p. 54, expressly leaves verification of the relevant discrete-to-continuous limit to future work. Numerical agreement cannot supply those steps.

That does **not** erase the rigorous discrete-time consequences of the Tensor Programs connection. TP IV, Theorem G.4, supplement PDF p. 14, gives almost-sure convergence of scalar outputs and empirical pseudo-Lipschitz tests for any fixed admitted program. Setup G.2 supplies Gaussian roots and independent variance-\(1/n\) matrices; Assumption L.4, PDF p. 21, requires the vector-dependent coordinate and moment functions to be pseudo-Lipschitz, and scalar-only functions to be continuous. MFP's finite expressions with smooth polynomially bounded derivatives satisfy these conditions after expansion. Thus a fixed finite rich-regime GD history can already be given rigorous scalar and empirical limits using that foundation. This is stronger than a claim of mere numerical plausibility for discrete dynamics.

The TP theorem's almost-sure conclusion, however, does not by itself establish convergence of expectations or of every finite \(L^p\) norm. Uniform integrability is an additional obligation. MFP's theorem `thm-mfp-finite-derivative-program` states all such scalar \(L^p\) limits, uniform moments of nodes, and joint empirical \(W_2\) convergence in probability; its raw-entry moment and clipping arguments are directed at precisely that upgrade. “Stronger theorem” should be qualified by the convergence mode: the quoted TP statement is almost sure, whereas MFP's displayed empirical statement is in probability.

Likewise, singular covariance is not a new phenomenon absent from TP or DMFT. TP IV Remark L.2 uses a pseudoinverse formulation, and DMFT already has singular boundary covariances such as \(G^{L+1}=11^\top\). DMFT's density manipulations use covariance inverses and determinants without providing an all-query singular-limit theorem. MFP explicitly retains distinct formal source slots and differentiates before restricting to Gaussian support, with no covariance inverse in its evaluation rule. That is a precise and useful specification, rather than grounds for saying that the earlier framework excludes singular data.

For MFP, the conclusion is restricted to its admitted finite typed programs: fixed Gaussian roots and named matrices, scalar sums/products and normalized averages, coordinate expressions formed with activation derivatives, finitely represented rank updates and directions, and fixed differentiation/update orders. It is not a theorem for every smooth function of every matrix entry. Its initialization activation-moment normal form further requires that each nonlinear argument be an original initialization preactivation. Outside that subclass it supplies a finite Gaussian expectation graph, not necessarily a polynomial in the smaller library of initialization activation moments.

**The extra work for arbitrary initial moving-flow jets can be specified exactly.** Let \(V_n(\theta)\) be the finite-width training vector field, including the chosen mobilities and loss normalization, and let \(O_n(\theta)\) be an admitted scalar observable. Put
\[
\mathscr L_{V_n}O_n=DO_n[V_n].
\]
The order-\(q\) physical-time derivative along \(\dot\theta=V_n(\theta)\) is \(\mathscr L_{V_n}^qO_n\). In particular,
\[
\mathscr L_{V_n}^2O_n
=D^2O_n[V_n,V_n]+DO_n[DV_n[V_n]],
\]
so freezing the first direction loses a term.

There is an exact finite-program bridge to the existing discrete theory. Introduce \(q\) independent formal step sizes and perform
\[
\theta_j=\theta_{j-1}+\varepsilon_jV_n(\theta_{j-1}),\quad 1\leq j\leq q.
\]
Then
\[
\left.\partial_{\varepsilon_1}\cdots\partial_{\varepsilon_q}
 O_n(\theta_q)\right|_{\varepsilon=0}
=\mathscr L_{V_n}^qO_n(\theta_0).
\]
To verify this, define \(T_\varepsilon F(\theta)=F(\theta+\varepsilon V_n(\theta))\); its derivative at zero is \(\mathscr L_{V_n}F\). Differentiating the product of \(q\) pullback operators once in each independent step size therefore gives \(\mathscr L_{V_n}^qF\). The identity is exact at each finite width and does not require a positive-time limit.

Consequently, one can obtain arbitrary **fixed** initial jets by writing a fixed training program, differentiating that finite program, and applying a TP master theorem to the expanded graph. The polynomial-growth assumptions ensure that the new coordinate functions remain in the theorem's class. This observation is an inference made in this review, not an all-order theorem claimed in the DMFT article. It makes clear both why an implementation is real work and why the observable is not inaccessible to the existing foundation.

The remaining work is to automate the derivative graph, preserve every shared-matrix occurrence and scalar-feedback path, handle gradient normalization and outer-product updates, define source derivatives at dependent queries, and prove moments sufficient to pass to expected jets. MFP performs this organization with coefficients \(\theta_{[r]}=\theta^{(r)}(0)/r!\) and the recurrence
\[
(r+1)\theta_{[r+1]}
=[t^r]V_n\!\left(\sum_{j=0}^r\theta_{[j]}t^j\right).
\]
This directly organizes finite-order differentiation; it is not a proof that the infinite Taylor series reconstructs training.

Working directly with continuum DMFT instead requires a coordinated expansion of the two-time kernels, fields, responses, and residuals, including both time arguments and boundary terms of memory integrals. Gaussian source covariances move with those coefficients. One must either include their covariance derivatives, as Appendix P already illustrates, or construct a finite joint Gaussian source representation for the jet variables. Finally one must justify the width/derivative or expectation interchange. MFP's finite-width-first route avoids needing a global continuum self-consistency or uniqueness theorem for this initial-jet task.

**A concrete check distinguishes the full DMFT from a faulty shortcut.** Consider \(L=2\), \(\phi(z)=z\), and half-mean square loss. Set
\[
\lambda_a=\frac1m\sum_bK^x_{ab}y_b.
\]
MFP's worked example gives coefficient \(9\lambda_a\lambda_b\) of \(t^2\) in the limiting last-hidden feature kernel at \(\gamma_0=1\). This is \(9/4\) times the two displayed label-weighted Gram factors when \(m=2\).

One can recover it directly from full DMFT. Write \(H^\ell=\mathbb E[z^{(\ell)}z^{(\ell)\top}]\), with time/data arguments suppressed. At \(\gamma_0=0\), \(H_0=K^x\otimes11^\top\), \(G_0=11^\top\). Let \(C_0,D_0\) be the causal update operators with kernels
\[
(C_0)_{a}(t,s)=\mathbf1_{s<t}\sum_bK^x_{ab}\Delta_b^0(s),
\qquad
(D_0)_{b}(t,s)=\mathbf1_{s<t}\Delta_b^0(s),
\]
where \(\Delta^0\) is the lazy residual and \(\Delta_b^0(0)=y_b/m\). Here \(C_0\) maps a scalar time process to a data-indexed process, and \(D_0\) maps a data-indexed process to a scalar one.

Equations (F.2)–(F.4), p. 38, imply at leading order
\[
A^\ell=C^\ell+O(\gamma_0^2),\quad
B^{\ell-1}=D^\ell+O(\gamma_0^2),\quad
C^\ell=A^{\ell-1}+C_0,\quad D^\ell=B^\ell+D_0.
\]
Using \(A^0=B^2=0\), this gives
\[
C^1=C_0,\quad C^2=2C_0,\qquad
D^2=D_0,\quad D^1=2D_0
\]
at the required order. With \(\{X,H\}_{\rm sym}=XH+HX^\top\), the same equations yield
\[
\begin{aligned}
H^1&=H_0+\gamma_0^2
\left(2\{C_0D_0,H_0\}_{\rm sym}+C_0G_0C_0^\top\right)+O(\gamma_0^4),\\
H^2&=H_0+\gamma_0^2
\left(4\{C_0D_0,H_0\}_{\rm sym}+5C_0G_0C_0^\top\right)+O(\gamma_0^4).
\end{aligned}
\]
At small \(t,s\), the two displayed operators have respective entries
\(\lambda_a\lambda_b(t^2+s^2)/2+o(t^2+s^2)\) and
\(\lambda_a\lambda_bts+o(t^2+s^2)\). Thus full DMFT gives the coefficient
\[
H^2_{ab}(t,t)=K^x_{ab}
+9\gamma_0^2\lambda_a\lambda_b\,t^2+o(t^2).
\]
Each additional memory-operator factor introduces another time integral, so the higher feature-strength orders cannot change this initial \(t^2\) coefficient. The full response construction and MFP agree on this diagnostic.

By contrast, journal (P.2)–(P.4), pp. 59–60, assume layer-independent leading \(C^\ell,D^\ell\) and give coefficient \(2\ell\gamma_0^2\lambda_a\lambda_b\), hence \(4\gamma_0^2\lambda_a\lambda_b\) at \(\ell=2\). The discrepancy is already in the coefficient of \(\gamma_0^2t^2\), so a higher-order remainder cannot fix it. The camera-ready Eqs. (144)–(146), p. 47, contain the same issue. The released linear notebook's `solve_kernels_full` retains the response recurrence, whereas its `perturb_theory_full` uses the layer-linear shortcut. This is a local inconsistency in the perturbative approximation, not evidence against the full DMFT source law.

Two smaller transcription cautions are also relevant to reuse. The final line of journal (M.8), p. 53, swaps the \(u/r\) response arguments relative to (14), (D.43)–(D.44), the preceding derivation, and the implemented Jacobians. The unnumbered NTK definition following Eq. (3), p. 6, omits the raw-gradient \(\gamma^2\) factor; (D.2)–(D.3), p. 23, identify the kernel governing prediction dynamics as \(\gamma^2\nabla f_a\cdot\nabla f_b\). Neither issue changes the intended normalization once the definitions are reconciled.

**Implementation and numerical evidence.** The article supplies more than a formal response definition. Algorithm 1, p. 22, alternates kernel estimates, Gaussian path sampling, field solves, and Jacobian estimates, with damping. The inspected nonlinear notebook implements `solve_jacobians_batched`: it propagates all four \(dz/du,dz/dr,dp/du,dp/dr\) source Jacobians, including
\[
dg=\phi'(z)\,dp+p\phi''(z)\,dz,\qquad dh=\phi'(z)\,dz.
\]
Thus the backward response and activation curvature are present. The notebook stores response operators with numerical step/feature-strength factors absorbed; copying its \(A,B\) variables into the rescaled main-text convention requires a normalization conversion.

The solver uses eigendecompositions and clips negative sampled-covariance eigenvalues to zero; it averages a finite number of source paths and uses bounded inner iterations and a fixed outer iteration count. The reviewed run requests \(1{,}000\) samples and 20 outer iterations; the source Jacobian routine batches 50 samples and permits 30 iterations. These are numerical controls, not an exact symbolic arbitrary-order query interface. The paper reports about 15 outer iterations for its three-hidden-layer nonlinear example and 5–10 for its linear solve. No contraction or error guarantee makes those empirical counts universal.

Figures 1–4 compare kernels, distributions, and prediction dynamics against wide networks and against NTK, independence, and perturbative approximations. Examples include the three-hidden-layer tanh network with \(m=10\), width 2,500 and repeated runs, and deep linear comparisons at width 1,000. The CNN experiments demonstrate agreement between widths 250 and 500 on CIFAR tasks; they should not be described as a full general-DMFT numerical solve on the whole CIFAR data set. Appendix C records the finite-network training settings.

Table 1, p. 17, quotes \(O(m^2T^2)\) kernel storage and \(O(m^3T^3)\) time for full DMFT on \(T\) time-grid points. Those scalings suppress depth, Monte Carlo sample count, and iteration count; they are not certified complexity at prescribed accuracy. The text identifies \(n\gg mT\) as the regime of advantage over the stated dense finite-network comparison. Appendix G adds spatial indices for convolutions, worsening the generic matrix cost. MFP addresses a different task: exact finite symbolic expectation graphs and, in a restricted subclass, moment polynomials. It performs no numerical quadrature and promises only finite compilation, not favorable high-order complexity. A speed comparison between these two outputs would require a separately specified common task and accuracy criterion.

The conference version also contains a formal finite-width saddle expansion in Appendix P.7, pp. 52–55, involving action Hessians, cumulants, and further source derivatives. This section is absent from the journal, whose Appendix P ends on p. 66. It is additional evidence of pre-existing symbolic derivative machinery; it is not a rigorous all-fixed-query expectation theorem, and it should not be silently attributed to the current journal edition.

**Positioning supported by this review.** A suitable claim is: “Building on Gaussian source-response descriptions of feature learning, including Tensor Programs and DMFT, we organize a finite differentiable program language whose exact finite-width derivative and moving-jet constructions admit deterministic Gaussian expectation limits, with uniform moment and \(L^p\) control under the stated hypotheses, and provide symbolic compilation.” A claim that DMFT lacks Gaussian derivative calculus, that fixed initial jets require a fundamentally new stochastic description, or that MFP proves positive-time feature-learning dynamics would not be supported.

This reassessment establishes the comparison and the displayed local consistency check. It is not a fresh certification of every line of MFP's probabilistic proof, and no released notebook was executed end to end. All source and code inspection was read-only; only this report and study-owned review scratch were written.

Reproducibility metadata: MFP source SHA-256 `a43acbc76e53a3437ed5136137fd8e5497a6d65826447c1ac95764a1cba8d38e`; camera-ready PDF `43b5f7262917ff751f8f4fe8660128973f6daace657eca1837451a4013bff92b`; journal PDF `a7820b833792081f59103aac3724f63cf8647b707831b48fa48e8a820a05cb05`. Downloads, extracted text, and the inspected code snapshot are in `data/generated/mfp_literature_positioning_20261011/reassessment_dmft/`.
