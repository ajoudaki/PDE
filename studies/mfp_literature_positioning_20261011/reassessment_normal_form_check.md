# Independent check of the initial-jet specialization

The proposed specialization is valid, conditional on the scalar-limit and source-response theorem stated in the supplied manuscript sections. The required qualification is that the admitted gradient contractions are generated from the same polynomial class of observables, without an intervening nonlinear function of a derivative field, an updated preactivation, or scalar feedback. The bound is on the dimension of each final activation-moment integral. It does not bound the number of moments, their derivative orders, or the size of the compilation.

This check used only `paper_MFP/main.tex`, lines 598–807 and 1148–1420, and the relevant implementation in `paper_MFP/code/pde/mfp_compiler.py` and `paper_MFP/code/pde/mfp_expr.py`, together with the required mathematical skills. It does not independently reprove the manuscript's probabilistic limit theorem.

Fix the sample count $m$, input dimension $d$, hidden depth $L$, and requested jet order $R$, independently of width $n$. Use the manuscript's zero-bias network

\[
z_a^{(1)}=W^{(1)}x_a/\sqrt d,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi(z_a^{(\ell)}),\qquad
f_{n,a}=W^{(L+1)\top}h_a^{(L)}/n.
\]

The first matrix has independent $N(0,1)$ entries; the independent, untied hidden matrices have entries $N(0,1/n)$; the independent stored readout has entries $N(0,\tau^2)$ for fixed $\tau$. Distinct layers have their canonical vector types. All derivatives of $\phi\in C^\infty$ have polynomial growth. The block mobilities are $n\kappa_1,\kappa_2,\ldots,\kappa_L,n\kappa_{L+1}$, with fixed multipliers. Let $\mathcal L_n$ be polynomial in the outputs and fixed labels. An admissible observable here is built by a fixed finite use of polynomial arithmetic, allowed coordinate products, normalized averages and contractions, and admitted gradients of expressions in this same class, starting from the original network quantities. “Polynomial” does not remove the activation already present in $h=\phi(z)$.

Define its moving physical-time jet by

\[
O_{n,[r]}=\frac1{r!}\left.\frac{d^r}{dt^r}O_n(\theta_n(t))\right|_{t=0},
\qquad \dot\theta_n=-M_n\nabla\mathcal L_n(\theta_n),
\]

where $M_n$ is the stated block mobility. Then every $O_{n,[r]}$, $0\le r\le R$, has a deterministic limit in every finite $L^p$, and its expectation converges to that limit. The limit is a finite polynomial in the fixed constants and atoms

\[
\mathbb E_{Z\sim N(0,\Sigma^{(\ell)})}
\prod_{j=1}^{s}\phi^{(r_j)}(Z_{a_j}),
\qquad
\Sigma^{(1)}_{ab}=x_a^\top x_b/d,
\qquad
\Sigma^{(\ell+1)}_{ab}
=\mathbb E_{Z\sim N(0,\Sigma^{(\ell)})}\phi(Z_a)\phi(Z_b).
\]

The finite lists $s,r_j,a_j,\ell$ depend on the observable and requested jet. Only the original forward covariance recursion appears inside these final integrals.

To prove this, first differentiate the finite network. For every derivative order $k\ge0$,

\[
D[\phi^{(k)}(z_a^{(\ell)})][v]
=\phi^{(k+1)}(z_a^{(\ell)})Dz_a^{(\ell)}[v].
\]

The argument remains the original current-state preactivation. Product rules, matrix-action rules, and the manuscript's reverse-adjoint rules introduce only polynomial operations, matrix actions, normalized averages, and activation derivatives at these same arguments. Matrix gradients are finite normalized rank-one sums; their allowed contractions reduce to products of normalized vector pairings. Thus gradients, contractions, and physical differentiation preserve this class. Polynomial loss and fixed mobilities give a gradient field in the class as well.

For an unnormalized derivative, set $Q_0=O_n$ and $Q_{r+1}=DQ_r[V_n]$, with $V_n=-M_n\nabla\mathcal L_n$. This recursion differentiates the previously inserted field wherever it occurs. In particular, $Q_2=D^2O_n[V_n,V_n]+DO_n[DV_n[V_n]]$. Induction proves that the moving jet, including its field-variation terms, has only nonlinear nodes $\phi^{(k)}(z_a^{(\ell)}(0))$. Dividing by $r!$ changes only a fixed coefficient. A finite Taylor construction gives the same result without an analyticity assumption. The width limit is applied after this exact finite differentiation; no interchange of differentiation and a width limit is needed.

Next construct the original forward pass before evaluating the differentiated program. Its preactivations are centered Gaussian sources, or Gaussian linear combinations of the first-layer roots, and have exactly the displayed covariances. On each layer type, adjoin those linear combinations as Gaussian integration coordinates. This is valid even if the enlarged Gaussian covariance is singular.

Inductively, every representative field is a finite sum of a polynomial in the Gaussian roots and auxiliary sources multiplied by products of activation derivatives at that layer's original $m$ preactivations. Its deterministic coefficients are polynomial in previously evaluated scalars. A new matrix call adds one Gaussian source and response terms whose coefficients are expectations of formal source derivatives of already constructed fields. Its covariance entries are expectations of products of already constructed input fields. Both integrands remain in the same class. Formal source derivatives are taken in the original source expressions, holding earlier deterministic coefficients fixed; adjoining integration coordinates does not alter those derivatives.

For each such expectation, Gaussian integration by parts gives

\[
\mathbb E[G_iF(G)]=\sum_j\operatorname{Cov}(G_i,G_j)\mathbb E[\partial_jF(G)].
\]

This holds at singular covariance by writing $G=B\gamma$ with independent standard Gaussian $\gamma$. The polynomial-growth assumptions justify integration by parts. Apply the identity to one explicit Gaussian factor outside the activations. A derivative of the remaining polynomial reduces its degree further; a derivative of an activation raises its derivative order but does not add an explicit Gaussian factor. Consequently the process terminates. Every auxiliary source disappears from the integrand and contributes only covariance factors. The remaining integrand contains activation derivatives at original preactivations of this one layer.

The covariance factors do not introduce an unresolved auxiliary law. Each was computed from inputs earlier in the acyclic program, so the same reduction has already expressed it in previously available coefficients and original activation moments. Induction over program order, followed by substitution, makes every such coefficient a finite polynomial in the stated constants and atoms. This establishes the claimed polynomial form.

Finally, an atom depends only on the distinct sample indices actually appearing among $a_1,\ldots,a_s$. Marginalizing all other Gaussian coordinates leaves a principal submatrix of $\Sigma^{(\ell)}$. Repeated occurrences of a sample index reuse the same Gaussian coordinate, however high their multiplicity or derivative orders. There are at most $m$ distinct indices. Singularities, coincident samples, and $d<m$ need no inverse covariance and create no exception. A further reduction to covariance rank may be possible, but is unnecessary for the $m$ bound.

The exact limits of this conclusion are as follows.

- **Initialization and fixed order.** Every prescribed finite initial moving jet is covered. A fixed nonzero update or positive-time state generally introduces $\phi(z_a^{(\ell)}(t))$ at new arguments. The initial-jet argument does not cover those nonlinearities, an infinite Taylor sum, or orders/depths growing with width. Particular updates that preserve the original nonlinear arguments can remain in the subclass.
- **Gradient-contraction provenance.** Allowing a gradient contraction of an arbitrary admitted nonlinear observable would make the statement too broad. For example, inserting a nonlinear function of a derivative field before taking its gradient does not inherit the original-argument restriction. The recursive polynomial-class condition above is sufficient and precise.
- **Other architectures.** The generic restricted normal form does not imply a universal $m$ bound. Its direct bound is the number of distinct designated nonlinear Gaussian arguments on one type, unless extra factorization reduces it. The canonical MLP has only its $m$ original layer preactivations on that type. Multiple vector types alone cause no problem, but extra correlated nonlinear coordinates or reused types can change this count. Tied architectures can also create response terms in later original preactivations, making those arguments non-Gaussian; their forward covariance law is not automatically the displayed untied recursion.
- **Nonpolynomial output loss.** Polynomial loss is sufficient, not necessary. Here the initial outputs converge to zero. A smooth output loss can therefore yield the same moment family at any fixed initial order after adjoining its finitely many derivatives at output zero, subject to a separate admissibility and integrability justification. These derivatives need not be polynomial in the original labels. For example, with one sample, readout-only training, $\phi=\sin$, and $\mathcal L=1-\cos(f-y)$, the initial output velocity has limit $\kappa_{L+1}\mathbb E[\sin^2(Z)]\sin y$. Thus the original polynomial dependence on labels is lost unless the extra loss-derivative values are explicitly included as coefficient data.
- **Extra nonlinear observables.** They require their own atoms or a separate identity. Even with the linear activation $\phi(z)=z$, adding the observable $\mathbb E[e^{-Z^2}]$, $Z\sim N(0,q)$, gives $(1+2q)^{-1/2}$; the original linear-activation moments and polynomial arithmetic yield only polynomials in $q$. The claimed reduction therefore cannot extend to arbitrary additional nonlinearities.
- **Cost and scaling.** The number of atoms, their multiplicities and derivative orders, the number of auxiliary sources, and expression size may grow substantially with depth and order. The result gives no efficiency bound or numerical quadrature guarantee. It also uses the fixed-root readout law above, not the manuscript's separately mentioned width-dependent small-readout initialization.

The implementation agrees with the integration-coordinate part of this argument. `GaussianCompiler.expectation` substitutes declared centered Gaussian-linear preactivation aliases before calling `gaussian_expectation(..., flat_only=True)`; `_integration_cov` computes their induced covariances; `_atom` retains only coordinates occurring in the final integrand. `mfp_expr.gaussian_expectation` enforces literal Gaussian-symbol activation arguments in this mode and removes explicit polynomial Gaussian factors by the terminating Stein recursion. These aliases are not substituted into the fields on which formal source derivatives operate. The generic compiler accepts user-declared Gaussian-linear preactivations; it does not itself establish that they are exactly the canonical MLP's original sample preactivations or certify the architectural $m$ bound. This was a static inspection, not a rerun of unchanged test suites.
