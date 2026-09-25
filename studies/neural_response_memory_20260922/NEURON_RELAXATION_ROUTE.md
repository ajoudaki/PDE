# Activity-clock neuron response memories: independent algebraic audit

This is a theory-only scoped report. The scientific inputs are the supervisor's finite canonical network and the supervisor's proposed Legendre history encoder and activity-clock modification. No other study, book, external source, or experiment was used. The research and rigorous-math skills were applied. The construction below originated with the supervisor; this report independently derives its identities, well-posedness, plateau condition, and remaining gap.

**Conclusion.** The proposed memory coefficients are genuine causally evolving neuron states with an explicit stable linear encoder. Their factors are determined by neuron histories, rather than independently trained dictionary factors. At every finite truncation the resulting nonlinear surrogate is globally well posed at finite width. Finite total residual activity implies convergence of all its neuron and memory states. Its learned middle-layer operator has an exact, explicit truncation defect. This is not yet a fully compressed realization of the canonical network: the original middle-layer operator and its actual transpose still act on current neurons. Canonical loss dissipation and accuracy at a specified finite memory size also require further estimates.

## 1. Finite canonical target and conventions

Let both hidden layers have width (n), and let the training samples be indexed by (a=1,\ldots,m), with positive weights \(\rho_a\). Zero-weight samples may be omitted. Write \(S=\sum_a\rho_a>0\), \(\bar x_a=x_a/\sqrt d\), and

\[
h_a=\tanh(W_1\bar x_a),\quad z_a=W_2h_a,
\quad H_a=\tanh z_a,\quad f_a=n^{-1}c^TH_a,
\]
\[
r_a=f_a-y_a,\quad \delta_a=c\odot(1-H_a^2),
\quad q_a=W_2^T\delta_a,
\quad g_a=(1-h_a^2)\odot q_a.
\]

The loss is \(L=\sum_a\rho_ar_a^2\). The specified flow is

\[
\dot W_1=-2\sum_a\rho_ar_ag_a\bar x_a^T,
\quad \dot W_2=-\frac2n\sum_a\rho_ar_a\delta_ah_a^T,
\quad \dot c=-2\sum_a\rho_ar_aH_a.
\tag{1}
\]

Throughout this report the **normalized outer product** is

\[
(u\otimes v)w=u\,\frac{v^Tw}{n},\qquad
u\otimes v=uv^T/n.
\tag{2}
\]

Thus the middle equation in (1) is \(\dot W_2=-2\sum_a\rho_ar_a\delta_a\otimes h_a\). An unnormalized matrix outer product would require an explicit factor \(1/n\) in every operator formula below.

## 2. Explicit memory encoder

For \(k\geq0\), let

\[
\ell_k(u)=\sqrt{2k+1}\,P_k(2u-1),\quad 0\leq u\leq1,
\qquad b_k=\ell_k(1)=\sqrt{2k+1},
\]

where \(P_k\) is the degree-\(k\) Legendre polynomial. These polynomials are orthonormal in \(L^2[0,1]\). For a vector-valued source \(J(s)\), define its normalized history coefficient

\[
Z_k(a)=\frac1a\int_0^a\ell_k(s/a)J(s)\,ds.
\tag{3}
\]

Differentiating (3) gives

\[
a\frac{dZ_k}{da}=b_kJ(a)-\sum_{j=0}^kA_{kj}Z_j,
\quad
A_{kk}=k+1,\quad A_{kj}=b_kb_j\ (j<k).
\tag{4}
\]

To verify every coefficient, expand \(\ell_k+u\ell_k'\) in the orthonormal basis. Its leading coefficient is \(k+1\), giving the diagonal. For \(j<k\), integration by parts gives

\[
\int_0^1\ell_j(\ell_k+u\ell_k')du
=[u\ell_j\ell_k]_0^1-\int_0^1u\ell_j'\ell_kdu
=b_jb_k.
\]

The remaining integral vanishes because \(u\ell_j'\) has degree at most \(j<k\). Hence the first \(P\) coefficients form an **exact closed encoder**: their evolution never requires a coefficient of degree \(P\) or higher. Exact encoding of these coefficients does not mean that truncating an operator built from them is exact.

## 3. Activity clock and learned operator

Choose \(a_0>0\) and set

\[
R(t)=\sqrt{L(t)},\qquad
a(t)=a_0+\int_0^t2R(s)ds.
\tag{5}
\]

Where \(R>0\), the two required sources for each sample are

\[
F_a=\frac{r_a}{R}\delta_a,\qquad G_a=h_a.
\tag{6}
\]

Extend each source constantly over a dummy clock interval \([0,a_0]\), using its value at physical time zero. If \(R(0)=0\), take \(F_a(0)=0\); the whole system is then stationary. Set

\[
U_{ak}(0)=\mathbf1_{k=0}F_a(0),\qquad
V_{ak}(0)=\mathbf1_{k=0}G_a(0),\quad 0\leq k<P.
\]

The physical-time encoder is most usefully written without any division by \(R\):

\[
\dot U_{ak}=\frac2a\left(b_kr_a\delta_a-R\sum_{j\leq k}A_{kj}U_{aj}\right),
\tag{7}
\]
\[
\dot V_{ak}=\frac{2R}{a}\left(b_kh_a-\sum_{j\leq k}A_{kj}V_{aj}\right),
\qquad \dot a=2R.
\tag{8}
\]

These equations are defined at \(R=0\) and all vanish there. The reconstructed middle-layer operator is

\[
\widehat W_{2,P}
=W_{2,0}
-\sum_a\rho_a\left[
a\sum_{k=0}^{P-1}U_{ak}\otimes V_{ak}
-a_0F_a(0)\otimes G_a(0)\right].
\tag{9}
\]

Use this operator in every forward action and its **actual transpose** in every backward action; evolve \(W_1,c\) by their equations in (1). Equations (7)–(9) then define a closed nonlinear surrogate provided actions by \(W_{2,0}\) and \(W_{2,0}^T\) remain available.

The evolving interaction in (9) has a diagonal core \(-a\,\mathrm{diag}(\rho_a)\otimes I_P\), in convention (2), plus a fixed rank-at-most-\(m\) dummy correction. The core size is \(mP\), not merely \(P\). Memory storage is proportional to \(nmP\). No coefficient is fitted using a future trajectory.

For the exact canonical history, completeness and orthogonality of the \(\ell_k\) give the bilinear Parseval identity

\[
\int_0^{a(t)}F_a(s)\otimes G_a(s)ds
=a(t)\sum_{k=0}^{\infty}U_{ak}(t)\otimes V_{ak}(t).
\tag{10}
\]

Indeed, apply scalar Parseval to each pair of vector entries; on a finite horizon the sources are square-integrable. Since \(da=2Rdt\), subtracting the dummy interval turns (10) into precisely the integral of the middle equation in (1). Thus (9) with all coefficients is an exact representation, including the initial correction and normalization.

## 4. Exact defect at finite memory size

Write \(b=(b_0,\ldots,b_{P-1})^T\), \(U_a=[U_{a0},\ldots,U_{a,P-1}]\), and similarly \(V_a\). Define endpoint reconstructions and residuals by

\[
\widehat F_a=U_ab,\quad \widehat G_a=V_ab,
\quad e_{Fa}=F_a-\widehat F_a,
\quad e_{Ga}=G_a-\widehat G_a.
\]

The encoder matrix obeys the exact identity

\[
A+A^T=I+bb^T.
\tag{11}
\]

The off-diagonal entries are \(b_kb_j\); on the diagonal, \(2(k+1)=1+b_k^2\). Substituting (4) and then (11) gives

\[
\frac d{da}(aU_aV_a^T)
=F_a\widehat G_a^T+\widehat F_aG_a^T-\widehat F_a\widehat G_a^T
=F_aG_a^T-e_{Fa}e_{Ga}^T.
\tag{12}
\]

Consequently the finite surrogate follows

\[
\dot{\widehat W}_{2,P}
=-2\sum_a\rho_ar_a\delta_a\otimes h_a+E_P,
\quad
E_P=2R\sum_a\rho_ae_{Fa}\otimes e_{Ga}.
\tag{13}
\]

At \(R=0\), define the product in (13) by its zero value; (7)–(9) already define the nonsingular dynamics. Equation (13) is a precise closure defect, evaluated on the surrogate's own history.

This also exposes the dissipation issue. Gradients below are gradients of the ordinary loss of the reconstructed network. Since the mobilities in (1) are \((n,1,n)\),

\[
\dot L=-n\|\nabla_{W_1}L\|_F^2
-\|\nabla_{W_2}L\|_F^2
-n\|\nabla_cL\|^2
+\langle\nabla_{W_2}L,E_P\rangle_F.
\tag{14}
\]

The last term has no established sign. Therefore well-posedness is not a proof of canonical loss dissipation. For example, Young's inequality gives only the weaker bound obtained by replacing the last two middle-layer terms with \(-\tfrac12\|\nabla_{W_2}L\|_F^2+\tfrac12\|E_P\|_F^2\).

Along any specified history, the operator error has the direct bound

\[
\|W_2-\widehat W_{2,P}\|_F
\leq\frac an\sum_a\rho_a
\left(\sum_{k\geq P}\|U_{ak}\|^2\right)^{1/2}
\left(\sum_{k\geq P}\|V_{ak}\|^2\right)^{1/2}.
\tag{15}
\]

This tends to zero at each fixed finite history by Parseval. Equation (15) compares truncations of the same supplied history. It is not by itself an error estimate for the self-consistently evolved surrogate. Moreover, small \(L^2\) tails alone do not bound the endpoint residuals in (13). Rates need temporal regularity, and width-independent rates need width-independent regularity or compactness assumptions.

## 5. Global well-posedness of the finite surrogate

**Proposition.** For finite \(n,m,P\), finite initial parameters and data, positive sample weights, and \(a_0>0\), equations (7)–(9), together with the stated \(W_1,c\) equations, have a unique solution for every finite physical time.

**Proof.** Regard \(W_1,c,a,U,V\) as the state, with the dummy correction fixed at initialization. The reconstructed operator (9) is polynomial in these states. All network functions are smooth except for \(R\), which is the Euclidean norm of the smooth vector \((\sqrt{\rho_a}r_a)_a\) and is locally Lipschitz. Since \(a\geq a_0\), the right sides (7)–(8) are locally Lipschitz. Local existence and uniqueness therefore reduce global existence to excluding finite-time escape of the state.

Let \(C(t)=\max_j|c_j(t)|\), \(Y=\max_a|y_a|\). Since \(|H_{aj}|\leq1\),

\[
|f_a|\leq C,\qquad |r_a|\leq C+Y,
\qquad |\dot c_j|\leq2S(C+Y).
\]

The integral inequality for \(C+Y\) yields

\[
C(t)+Y\leq(C(0)+Y)e^{2St}.
\tag{16}
\]

Also \(R\leq\sqrt S(C+Y)\), so \(a\) is bounded on every fixed interval \([0,T]\). Denote the resulting bounds by \(C_T\) and \(a_T\).

The encoder is exactly the first \(P\) moments of its own driving sources, including the dummy interval. If the clock has a flat interval, assigning its source arbitrarily at that single clock value does not affect any integral. For each second-layer neuron \(j\),

\[
\sum_a\rho_a|F_{a,j}|^2
=\sum_a\rho_a\frac{r_a^2}{R^2}|\delta_{a,j}|^2
\leq C_T^2,
\qquad
\sum_a\rho_a|G_{a,i}|^2\leq S.
\tag{17}
\]

The same bounds hold on the dummy interval. The square norm of an orthogonal projection is no larger than that of the original function; applying this to (3) gives

\[
\sum_{a,k<P}\rho_a|U_{ak,j}|^2\leq C_T^2,
\qquad
\sum_{a,k<P}\rho_a|V_{ak,i}|^2\leq S.
\tag{18}
\]

Thus all memory coordinates remain bounded, and Cauchy–Schwarz gives

\[
|\widehat W_{2,P;ji}-W_{2,0;ji}|
\leq\frac{\sqrt S}{n}(a_TC_T+a_0C(0)).
\tag{19}
\]

This bound is even independent of \(P\). Hence

\[
|q_{a,i}|\leq C_T\left[
\sum_j|W_{2,0;ji}|+\sqrt S(a_TC_T+a_0C(0))\right]
\]

is finite. With \(X=\max_a\|\bar x_a\|\), the first equation of (1) now bounds every row velocity of \(W_1\) on \([0,T]\). Therefore \(W_1\) also cannot escape in finite time. All state components stay in a bounded set with \(a\geq a_0\); local continuation extends the unique solution past every finite \(T\). ∎

This proposition is finite-width well-posedness. The column-sum bound involving \(W_{2,0}\) is not asserted to be uniform over arbitrary widths or initializations.

## 6. What plateaus are actually proved

For a frozen source, (4) in logarithmic clock \(\tau=\log(a/a_0)\) reads

\[
\frac{dZ}{d\tau}=bJ-AZ.
\]

The triangular matrix \(A\) has distinct eigenvalues \(1,\ldots,P\), so its homogeneous elementary modes are powers \((a(s)/a(t))^j\), \(j=1,\ldots,P\). These are real decaying modes when the clock tends to infinity. They are not fixed exponential modes in physical time. Nonnormal mixing and variable forcing can still produce transients.

Since \(Ae_0=b\), a constant source has equilibrium \(Z=e_0J\). More generally, if a bounded clock-source converges to \(J_\infty\) and \(a\to\infty\), dominated convergence in (3) gives \(Z_0\to J_\infty\) and \(Z_{k>0}\to0\).

There is also a stronger plateau statement that applies to the entire nonlinear surrogate under one explicit condition:

**Proposition.** If the surrogate satisfies

\[
\int_0^\infty R(t)dt<\infty,
\tag{20}
\]

then \(a,U,V,W_1,c,\widehat W_{2,P}\) all converge, as do every finite-sample forward and backward neuron state. The limiting training residual is zero.

**Proof.** The clock converges to a finite value. Cauchy–Schwarz gives \(\sum_a\rho_a|r_a|\leq\sqrt S R\), so

\[
|\dot c_j|\leq2\sqrt S R.
\]

Thus \(c\) has finite total variation and is uniformly bounded. With \(a\) bounded, (17)–(19) give uniform bounds on all memories, the reconstructed operator, and \(q\). Equations (7)–(8), using \(|r_a|\leq R/\sqrt{\rho_a}\), bound each memory derivative by a constant times \(R\). Hence each memory has finite total variation and converges. The same argument applied to \(\dot W_1\), with bounded \(q\), proves convergence of \(W_1\). Formula (9) gives convergence of the operator. All forward and backward states are continuous functions of these finite limiting parameters, so they converge. In particular \(R\) has a limit; its integrability forces that limit to be zero. ∎

Condition (20) is not established by the encoder. Merely \(R(t)\to0\) does not imply finite total activity; it also does not force \(r_a/R\) to converge. Consequently no unconditional plateau claim follows from vanishing residual alone. At exactly zero residual the ODE freezes, which is a correct property but is not a proof that nonzero initial residual reaches zero in finite time.

## 7. Both neuron populations and the remaining scientific gap

The essential operator histories are first-layer forward states \(H^1_a=h_a\) and normalized second-layer backward states \((r_a/R)\Delta^2_a=(r_a/R)\delta_a\). If all four streams are desired, also carry histories of \(H^2_a=H_a\) and \((r_a/R)\Delta^1_a=(r_a/R)g_a\), using exactly the same encoder and the cancellation used in (7). These extra histories remain neuronwise ODE states. They do not, by their mere inclusion, remove a missing operator action.

In particular, current responses still require

\[
z_a=W_{2,0}h_a+\text{memory-factor actions},
\qquad
q_a=W_{2,0}^T\delta_a+\text{transposed memory-factor actions}.
\]

Thus a generic dense initial operator has not been compressed. Replacing these actions by an unrelated adjoint would change the target. Replacing the initial operator by a finite approximation is a separate approximation axis requiring a specified norm, initialization class, and propagated error bound. This report does not supply that missing result.

The construction is algebraically a moving factor representation, but its content is different from training free factors: the factors are uniquely specified polynomial moments of causal neuron histories, with fixed coefficient matrices and an exact integration identity. Their adaptation records changes in the true neural sources. This distinction is substantive; it does not eliminate the initial-operator gap or the need to bound finite-memory feedback error.

Finally, all finite dimensions above count **finite training samples**. For population-risk training, replacing \(\sum_a\rho_a\) by an integral produces a continuum of sample-indexed memory states. A finite small core then additionally requires a justified approximation of that input integral. Compressing time histories does not automatically compress the input distribution or the neuron populations.
