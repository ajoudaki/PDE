# Independent \(L=2,B=2\) Gaussian-normal-form derivation

**Status:** independently frozen before comparison with
‘B2_GAUSSIAN_NORMAL_FORM.md’  
**Model:** ‘FINITE_WIDTH_DIRECTIONAL_PROGRAM.md’, arbitrary
\(Q^0\succeq0\) and \(c\in\mathbb R^2\)  
**Activation:** no Hermite approximation; the algebra uses
\(\phi,\phi',\phi'',\phi'''\)

This note derives the width limit of the exact finite-width scalar
\(C_{n,c}=D_c^3g_c\). All batch vectors below are columns. Products of two
vectors without a matrix between them are coordinatewise, and
\(\operatorname{Diag}(v)\) is the diagonal matrix with diagonal \(v\).
Indices \(s,t\) range over \(\{1,2\}\).

The proof has three steps: peel the reused middle matrix into column and row
Gaussian blocks with explicit transpose responses; contract every auxiliary
Gaussian by finite Wick or Stein identities; and insert the resulting
\(U\)- and \(Z\)-expectations into the exact scalar program.

## 1. Literal atom grammar and dependency order

Let

\[
U\sim N(0,Q^0),\qquad x_r=\phi^{(r)}(U),\quad 0\le r\le3,
\tag{1.1}
\]

and define

\[
Q=\mathbb E_U[x_0x_0^T],\qquad
D_1=\mathbb E_U[x_1x_1^T].
\tag{1.2}
\]

Let

\[
Z\sim N(0,Q),\qquad y_r=\phi^{(r)}(Z),\qquad
\mathbf C=\operatorname{Diag}(c).
\tag{1.3}
\]

Set

\[
w=\mathbf C y_1,\qquad e=\mathbf C y_2,\qquad
f=\mathbf C y_3,\qquad \rho=c^Ty_0,
\tag{1.4}
\]

and

\[
D=\mathbb E_Z[ww^T],\qquad
K=Q^0\odot D_1,\qquad L=Q+K.
\tag{1.5}
\]

Both \(K\) and \(L\) are symmetric. The order (1.1)--(1.5) is important:
\(Q\) is a \(U\)-atom, \(D\) a \(Z\)-atom, and all later objects are finite
algebraic contractions of these two atom families.

Every expectation is literal. For example,

\[
\mathbb E_U\!\left[\prod_j\phi^{(r_j)}(U_{i_j})\right]
=\mathcal I(Q^0;\mathbf i,\mathbf r),\qquad
\mathbb E_Z\!\left[\prod_j\phi^{(r_j)}(Z_{i_j})\right]
=\mathcal I(Q;\mathbf i,\mathbf r).
\tag{1.6}
\]

All matrix products below are sums over two-valued indices. Expanding them
therefore yields a finite polynomial in (1.6), without an inverse of \(Q^0\)
or \(Q\). Singular input and hidden-layer covariances are included.

## 2. Column block and tangent inputs

The backward channel has the limiting column law

\[
G\sim N(0,D),\qquad G\perp U.
\tag{2.1}
\]

For fixed \(U\), put

\[
B(U)=Q^0\operatorname{Diag}(x_1),\qquad
h=B(U)G,\qquad
\Sigma(U)=B(U)D B(U)^T.
\tag{2.2}
\]

The three first-layer tangent inputs are

\[
\dot x=x_1h,\qquad \ddot x=x_2h^{\odot2},\qquad
x^{(3)}=x_3h^{\odot3}.
\tag{2.3}
\]

Their contracted covariance and response matrices are

\[
V_{st}=\mathbb E_U[x_{1,s}x_{1,t}\Sigma_{st}],
\tag{2.4}
\]

\[
N_{st}=\mathbb E_U[x_{0,s}x_{2,t}\Sigma_{tt}],
\tag{2.5}
\]

\[
J^{(3)}_{st}
=3Q^0_{ts}\mathbb E_U[x_{1,s}x_{3,t}\Sigma_{tt}],
\qquad L_3=3N+J^{(3)}.
\tag{2.6}
\]

Indeed,

\[
\mathbb E\!\left[\frac{\partial\dot x_t}{\partial G_s}\right]
=K_{st},\qquad
\mathbb E\!\left[\frac{\partial\ddot x_t}{\partial G_s}\right]=0,\qquad
\mathbb E\!\left[\frac{\partial x^{(3)}_t}{\partial G_s}\right]
=J^{(3)}_{st}.
\tag{2.7}
\]

The middle equality is centered-\(G\) parity; the last is the conditional
second-moment contraction in (2.6).

## 3. Complete row Gaussian block

Let \((Z,\Gamma,\Omega,\Lambda)\) be a centered \(8\)-dimensional Gaussian
block, independent of \((U,G)\), with \(2\)-by-\(2\) covariance blocks

\[
\operatorname{Cov}\!\begin{pmatrix}Z\\\Gamma\\\Omega\\\Lambda\end{pmatrix}
=\begin{pmatrix}
Q&0&N&0\\
0&V&0&P_{13}\\
N^T&0&W_2&0\\
0&P_{13}^T&0&W_3
\end{pmatrix}.
\tag{3.1}
\]

Wick's rule gives the otherwise terminally unused blocks

\[
(W_2)_{st}
=\mathbb E_U\!\left[x_{2,s}x_{2,t}
(\Sigma_{ss}\Sigma_{tt}+2\Sigma_{st}^2)\right],
\tag{3.2}
\]

\[
(P_{13})_{st}
=3\mathbb E_U[x_{1,s}x_{3,t}\Sigma_{st}\Sigma_{tt}],
\tag{3.3}
\]

\[
(W_3)_{st}
=\mathbb E_U\!\left[x_{3,s}x_{3,t}
(9\Sigma_{ss}\Sigma_{tt}\Sigma_{st}+6\Sigma_{st}^3)\right].
\tag{3.4}
\]

All omitted cross blocks vanish by odd \(G\)-parity. In particular,
\(\operatorname{Cov}(Z,\Gamma)=\operatorname{Cov}(\Gamma,\Omega)\)
\(=\operatorname{Cov}(Z,\Lambda)=\operatorname{Cov}(\Omega,\Lambda)=0\).

Let \(A_0\sim N(0,1)\) be independent of (3.1), and put \(p=A_0w\). The
first three top-preactivation tangents are

\[
\zeta\Rightarrow A_0Lw+\Gamma,\qquad
\sigma\Rightarrow\Omega,\qquad
\tau\Rightarrow A_0L_3^Tw+\Lambda.
\tag{3.5}
\]

The direct term \(PQ_n\) contributes \(Qp\), and the response of \(A\dot
X_0\) contributes \(Kp\). Moreover
\(\mathbb E[x_0\dot x^T]=0\) and
\(\mathbb E[x_0\ddot x^T]=N\). Thus the first term of the finite-width
\(\sigma\) vanishes, while the direct first term of \(\tau\) is \(3N^Tp\).

## 4. Differentiated transpose channel

Put

\[
\ell=Lw,\qquad r=e\odot\ell.
\tag{4.1}
\]

The limiting differentiated top source is

\[
b=\rho w+A_0e\odot(A_0\ell+\Gamma)
=\rho w+A_0^2r+A_0\operatorname{Diag}(e)\Gamma.
\tag{4.2}
\]

Contracting \(A_0\) and \(\Gamma\) gives

\[
\begin{aligned}
\Beta=\mathbb E_Z\big[&\rho^2ww^T
+\rho(wr^T+rw^T)+3rr^T\\
&+\operatorname{Diag}(e)V\operatorname{Diag}(e)\big].
\end{aligned}
\tag{4.3}
\]

The response of \(A^T\dot P\) along \(X_0\) is

\[
\mathcal R=\mathbb E_Z\!\left[
ww^T+\operatorname{Diag}(\rho e+f\odot\ell)
+\operatorname{Diag}(e)L\operatorname{Diag}(e)\right].
\tag{4.4}
\]

Its \((s,t)\) entry is explicitly

\[
\mathbb E\!\left[\frac{\partial b_t}{\partial Z_s}\right]
=\mathbb E_Z[
w_sw_t+\delta_{st}(\rho e_t+f_t\ell_t)+e_sL_{st}e_t].
\tag{4.5}
\]

The response along \(\dot X_0\) vanishes:

\[
\mathbb E\!\left[\frac{\partial b_t}{\partial\Gamma_s}\right]
=\delta_{st}\mathbb E[A_0e_t]=0.
\tag{4.6}
\]

There is no dependence on \(\Omega\) or \(\Lambda\). The fresh part is
\(\Eta\sim N(0,\Beta)\). It is independent of \(G\), since

\[
\mathbb E[pb^T]=0
\tag{4.7}
\]

by \(A_0\)-parity. Since \(D\) and \(\mathcal R\) are symmetric, define

\[
\Chi=D+\mathcal R.
\tag{4.8}
\]

Then

\[
\dot R\Rightarrow\Chi x_0+\Eta,\qquad
\dot S\Rightarrow x_2hG+x_1(\Chi x_0+\Eta).
\tag{4.9}
\]

Equations (2.7), (4.4), and (4.6) list every possible nontrivial
opposite-orientation response. The initial response of \(A^TP\) along \(X_0\)
is also zero because
\(\mathbb E[\partial p_t/\partial Z_s]
=\delta_{st}\mathbb E[A_0c_ty_{2,t}]=0\).

## 5. Fully contracted Gaussian normal form

No auxiliary coordinate \(A_0,G,\Gamma,\Omega,\Lambda,\Eta\) remains in this
section. The inverse-free Stein identity

\[
\mathbb E[g(Z)\Omega_s]
=\sum_tN_{ts}\mathbb E[\partial_{Z_t}g(Z)]
\tag{5.1}
\]

and finite Wick contraction give

\[
\begin{aligned}
T_c={}&3\mathbb E_Z\sum_s
f_s(\ell_s^3+\ell_sV_{ss})\\
&+3\mathbb E_Z\sum_{s,t}N_{ts}
(\delta_{st}f_s\ell_s+e_sL_{st}e_t)\\
&+\mathbb E_Z[w^TL_3^Tw]\\
&+3\mathbb E_Z\sum_s\rho e_s(\ell_s^2+V_{ss})\\
&+3\mathbb E_Z\sum_{s,t}N_{ts}
(w_tw_s+\delta_{st}\rho e_s).
\end{aligned}
\tag{5.2}
\]

For verification,
\(\partial_{Z_t}(e_s\ell_s)
=\delta_{st}f_s\ell_s+e_sL_{st}e_t\) and
\(\partial_{Z_t}(\rho w_s)
=w_tw_s+\delta_{st}\rho e_s\), so (5.2) contains no unevaluated derivative.

The readout and middle-weight Hessian blocks are

\[
H_{a,c}=\mathbb E_Z[(w^T\ell)^2+w^TVw],
\tag{5.3}
\]

\[
H_{W,c}=\operatorname{tr}(\Beta Q)+\operatorname{tr}(DV).
\tag{5.4}
\]

The mixed rank-one term in \(H_{W,c}\) vanishes because both
\(\mathbb E[pb^T]\) and \(\mathbb E[\dot x\,x_0^T]\) are zero.

For the first-layer block define

\[
\mathcal J(U)=DB(U)^T,\qquad
\mu_s(U)=x_{2,s}\mathcal J_{ss}(U),\qquad
q(U)=\operatorname{Diag}(x_1)\Chi x_0,
\tag{5.5}
\]

and

\[
\mathcal A_{st}(U)=x_{2,s}x_{2,t}\left[
D_{st}\Sigma_{st}
+\mathcal J_{ss}\mathcal J_{tt}
+\mathcal J_{st}\mathcal J_{ts}\right].
\tag{5.6}
\]

These are the three Wick pairings of
\(\mathbb E[G_sG_th_sh_t\mid U]\). Therefore

\[
\begin{aligned}
H_{U,c}=\mathbb E_U\operatorname{tr}\Big\{Q^0\big[&\mathcal A
+q q^T+\operatorname{Diag}(x_1)\Beta\operatorname{Diag}(x_1)\\
&+\mu q^T+q\mu^T\big]\Big\}.
\end{aligned}
\tag{5.7}
\]

The directional initialization NTK and requested correction are

\[
A_c=\mathbb E_Z[\rho^2]+\operatorname{tr}(DL),
\tag{5.8}
\]

\[
C_c=2T_c+4(H_{a,c}+H_{W,c}+H_{U,c}).
\tag{5.9}
\]

Equations (1.1)--(1.6), (2.2), (2.4)--(2.6), (4.1), (4.3)--(4.4), and
(5.2)--(5.9) are a finite dependency DAG consisting solely of literal
two-dimensional Gaussian expectations of \(\phi\) and its derivatives. This
is a Gaussian normal form in the proof-contract sense, not merely an
auxiliary-Gaussian representation.

Under the polynomially-smooth envelope, the exact finite program and the
\(L^p\) Tensor Program theorem cited in the parent probability ledger give
\(C_{n,c}\to C_c\) almost surely and in every finite \(L^p\). Under only
finite-order pseudo-Lipschitz regularity, the same annealed caveat as for
\(B=1\) applies.

## 6. Exact reduction to \(B=1\)

Take \(c=(1,0)^T\), and write \(q_0=Q^0_{11}\). Then

\[
w=(\phi'(Z_1),0)^T,\quad e=(\phi''(Z_1),0)^T,\quad
f=(\phi'''(Z_1),0)^T,\quad \rho=\phi(Z_1).
\tag{6.1}
\]

The matrices \(D,\Beta,\mathcal R,\Chi\) are supported only in entry
\((1,1)\). Although inactive intermediate covariances can contain a second
coordinate when \(Q^0_{12}\ne0\), every terminal contraction selects index
\(1\): \(G_2=\Eta_2=0\), and both terms of (4.9) vanish in coordinate \(2\).
Consequently no off-diagonal entry of \(Q^0\) survives.

With the \(B=1\) atom names, the active entries are

\[
K_{11}=q_0d,\qquad L_{11}=\alpha=Q+q_0d,\qquad
D_{11}=D,\qquad V_{11}=\nu=q_0^2r_4D,
\tag{6.2}
\]

\[
N_{11}=\kappa=q_0^2Dm,\qquad
(L_3)_{11}=3D(q_0^2m+q_0^3\ell),
\tag{6.3}
\]

\[
\Beta_{11}=\beta,\qquad
\mathcal R_{11}=S_0+\alpha S_1,\qquad
\Chi_{11}=\chi.
\tag{6.4}
\]

Substitution in (5.2) gives atom for atom

\[
\begin{aligned}
T_c=3\big[&\alpha^2P_1+\nu P_2+\kappa S_0
+\alpha^3P_3+\alpha\nu P_4+\alpha\kappa S_1\\
&+D^2(q_0^2m+q_0^3\ell)\big]=3\mathcal T_*.
\end{aligned}
\tag{6.5}
\]

The Hessian blocks reduce to

\[
H_{a,c}=\alpha^2R+\nu D,\qquad
H_{W,c}=Q\beta+\nu D,
\tag{6.6}
\]

\[
H_{U,c}=q_0(
3q_0^2D^2s+\chi^2e+\beta d+2q_0D\chi m).
\tag{6.7}
\]

Thus their sum is \(\mathcal H_*\), and (5.9) becomes

\[
C_c=6\mathcal T_*+4\mathcal H_*,
\tag{6.8}
\]

exactly the audited \(B=1\) formula.

## 7. Exact linear-activation control

Let \(\phi(x)=x\) and set \(a=c^TQ^0c\). Then

\[
Q=Q^0,\qquad D=cc^T,\qquad K=Q^0,\qquad L=2Q^0,
\tag{7.1}
\]

\[
V=(Q^0c)(Q^0c)^T,\qquad
\Beta=a\,cc^T,\qquad
\mathcal R=cc^T,\qquad
\Chi=2cc^T,\qquad T_c=0.
\tag{7.2}
\]

Writing \(v=Q^0c\), the three Hessian blocks are

\[
H_{a,c}=5a^2,\qquad H_{W,c}=2a^2,\qquad H_{U,c}=5a^2.
\tag{7.3}
\]

Indeed \(w=c\), \(\ell=2v\), and \(w^TVw=(c^Tv)^2=a^2\), giving the
first identity. The two traces in (5.4) each equal \(a^2\). Finally \(x_2=0\),
while \(q(U)=2c(c^TU)\) and the differentiated-column noise has covariance
\(a\,cc^T\), giving the last identity. Therefore

\[
A_c=3\,c^TQ^0c,\qquad C_c=48\,(c^TQ^0c)^2.
\tag{7.4}
\]

This specializes to \(A=3q_0\), \(C=48q_0^2\) for one sample and verifies
\(A_{\lambda c}=\lambda^2A_c\), \(C_{\lambda c}=\lambda^4C_c\).

## 8. Freeze declaration

Equations (1.1)--(7.4) were frozen before reading
‘B2_GAUSSIAN_NORMAL_FORM.md’ or
‘contracted_gnf_polynomial_reference.py’. Any comparison with those artifacts
is appended below and does not alter the independent grouping above.

## 9. Post-freeze comparison and falsification

After the freeze, termwise comparison with ‘B2_GAUSSIAN_NORMAL_FORM.md’ gave
the following exact dictionary:

\[
Q=Q^1,\quad D=\mathsf D,\quad K=\mathsf L,\quad L=\mathsf K,
\quad V=\mathsf G,\quad N=\mathsf M,
\quad J^{(3)}=\mathsf N,\quad L_3=\boldsymbol\kappa,
\tag{9.1}
\]

\[
W_2=\mathsf O,\qquad P_{13}=\mathsf V,\qquad W_3=\mathsf F,
\qquad \Beta=\beta,qquad \mathcal R=\rho_{\rm resp},
\qquad \Chi=\chi.
\tag{9.2}
\]

Under (9.1)--(9.2), (5.2) agrees term for term with the canonical straight
third-derivative formula, (5.3)--(5.4) agree with its readout and middle
blocks, and the three Wick pairings in (5.6) expand exactly to its
first-weight contraction. There was no algebraic, response, index-orientation,
or scaling discrepancy. In particular, the apparently transposed response in
the first-weight block is harmless because both \(D\) and \(\mathcal R\) are
symmetric, hence so is \(\Chi\).

The independent formula was then tested through the separately implemented
contracted polynomial evaluator. All twelve fixed-batch checks passed,
including exact finite-width jets, arbitrary-geometry linear activation,
the atomwise \(B=1\) reduction, zero channels, homogeneity, and the quadratic
two-input campaign. For
\(Q^0=\left(\begin{smallmatrix}1&\theta\\\theta&1\end{smallmatrix}\right)\),
\(t=\theta^2\), and \(\phi(x)=x^2\), it reproduces exactly

\[
\begin{array}{c|c|c}
c&A_c&C_c\\ \hline
(1,1)^T/2&63+20t+28t^2&
279680+423312t+788336t^2+143232t^3+50624t^4\\
(1,-1)^T/2&48-20t-28t^2&
168192-91904t-270144t^2+143232t^3+50624t^4.
\end{array}
\tag{9.3}
\]

Thus the post-freeze comparison found no mismatch to record.
