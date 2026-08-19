# Independent joint fixed-depth/fixed-batch Gaussian recursion

**Status.** Audited theorem for every separately fixed hidden depth \(H\) and
batch size \(B\), under the polynomially-smooth activation envelope in
Section 9. The exact rational evaluator, both accepted one-axis reductions,
and the genuinely joint \(H=3,B=2\) nonlinear gate all pass. This note was
frozen before comparison with FIXED_H_FIXED_B_GNF_TEMPLATE.md; the two
independently written recursions agree in every checked index orientation,
direct term, response term, and terminal contraction. The independent
project-level hostile audit accepts the probability bridge and loss map.

The construction is pointwise in a fixed hidden depth \(H\) and a fixed batch
size \(B\). It uses the original generic activation; there is no Hermite or
polynomial approximation. Polynomial activations occur only in the exact
audit backend.

## 1. Model, indices, and contractions

Batch indices are Greek letters
\(\alpha,\beta,\gamma,\delta\in\{1,\ldots,B\}\), and neuron indices are
\(i,j\in\{1,\ldots,n\}\). A coordinate representative of an \(n\times B\)
program array is a row in \(\mathbb R^{1\times B}\). Row vectors multiply
response matrices on the right:

\[
 (uM)_\beta=\sum_\alpha u_\alpha M_{\alpha\beta}.
 \tag{1.1}
\]

For matrices of the same size, put

\[
 \langle M,N\rangle_F
 =\sum_{\alpha,\beta}M_{\alpha\beta}N_{\alpha\beta}.
 \tag{1.2}
\]

All covariance matrices below are symmetric, but response matrices need not
be. A response orientation therefore cannot be changed merely by
transposing notation.

With \(Q^0=X^TX/d_0\succeq0\), raw Gaussian parameter matrices, and raw
readout \(a\), the network is

\[
\begin{aligned}
 z^1&=W^1X/\sqrt{d_0},&
 x^1&=\phi(z^1),\\
 z^\ell&=W^\ell x^{\ell-1}/\sqrt n,&
 x^\ell&=\phi(z^\ell),\qquad 2\leq\ell\leq H,\\
 f_\beta&=n^{-1}\sum_i a_i x^H_{i\beta},&
 g_c&=\sum_\beta c_\beta f_\beta .
\end{aligned}
\tag{1.3}
\]

Let

\[
 D_c=n\nabla g_c\mathbin\cdot\nabla,\qquad
 A_{H,c}=\lim_{n\to\infty}D_cg_c,\qquad
 C_{H,c}=\lim_{n\to\infty}D_c^3g_c.
\tag{1.4}
\]

The identity that separates the calculation is exact at finite width. If
\(v_c=n\nabla g_c\), \(\widehat g_c(s)=g_c(\theta+s v_c)\), and

\[
 T_{n,H,c}=\widehat g_c'''(0),\qquad
 \mathcal H_{n,H,c}=n\|\nabla^2g_c\,v_c\|^2,
\tag{1.5}
\]

then

\[
 \boxed{D_c^3g_c=2T_{n,H,c}+4\mathcal H_{n,H,c}.}
 \tag{1.6}
\]

Thus only a frozen forward three-jet and one differentiated reverse pass
must be peeled. Equation (1.6), rather than a frozen-gradient
approximation, produces the moving-field coefficient.

## 2. Matrix/transpose rule with explicit batch orientation

Write \(A=W/\sqrt n\). For actual chronological uses

\[
 F^r_\beta=A u^r_\beta,\qquad T_\gamma=A^Tv_\gamma,
\tag{2.1}
\]

the coordinate rule is

\[
 [F^r_\beta]=\widehat F^r_\beta+
 \sum_{\gamma:T_\gamma\prec F^r_\beta}
 [v_\gamma]\,
 \mathbb E\!\left[
 \frac{\partial[u^r_\beta]}{\partial\widehat T_\gamma}
 \right],
\tag{2.2}
\]

\[
 [T_\gamma]=\widehat T_\gamma+
 \sum_{r,\beta:F^r_\beta\prec T_\gamma}
 [u^r_\beta]\,
 \mathbb E\!\left[
 \frac{\partial[v_\gamma]}{\partial\widehat F^r_\beta}
 \right].
\tag{2.3}
\]

The same-orientation innovation covariances are

\[
 \operatorname{Cov}(\widehat F^r_\beta,\widehat F^s_\delta)
 =\mathbb E[u^r_\beta u^s_\delta],
 \qquad
 \operatorname{Cov}(\widehat T_\gamma,\widehat T_\kappa)
 =\mathbb E[v_\gamma v_\kappa].
\tag{2.4}
\]

The derivatives in (2.2)--(2.3) are syntactic derivatives of named program
variables. Consequently neither rule uses a covariance inverse, even when
some batch columns coincide. Fresh forward and transpose innovations may be
chosen independent; the displayed responses carry their leading
cross-orientation dependence. Two different transpose uses of the same
matrix have the source cross covariance recorded explicitly in Section 6.

## 3. Base forward and reverse covariance passes

Starting from \(Q^0\), define

\[
 Z_\ell\sim N(0,Q^{\ell-1}),\qquad
 Q^\ell_{\alpha\beta}
 =\mathbb E[
 \phi(Z_{\ell,\alpha})\phi(Z_{\ell,\beta})
 ],
\tag{3.1}
\]

\[
 E^\ell_{\alpha\beta}
 =\mathbb E[
 \phi'(Z_{\ell,\alpha})\phi'(Z_{\ell,\beta})
 ].
\tag{3.2}
\]

Let \(R_\ell\) be the base reverse carrier and set

\[
 \Delta_\ell=\phi'(Z_\ell)\odot R_\ell,\qquad
 \mathsf B_\ell=\mathbb E[R_\ell^TR_\ell],\qquad
 \mathsf P_\ell=\mathbb E[\Delta_\ell^T\Delta_\ell].
\tag{3.3}
\]

At the top \(R_H=a c^T\). Centered-readout parity kills the candidate base
transpose response, so

\[
 \mathsf B_H=cc^T,\qquad
 \mathsf P_\ell=\mathsf B_\ell\odot E^\ell,\qquad
 \mathsf B_{\ell-1}=\mathsf P_\ell\quad(\ell\geq2).
\tag{3.4}
\]

The \(R_\ell\)'s can be represented by mutually independent centered
Gaussian rows, independent of the base forward preactivation at their own
layer. Define

\[
 \Theta^0=Q^0,\qquad
 \Theta^\ell=Q^\ell+\Theta^{\ell-1}\odot E^\ell.
\tag{3.5}
\]

Then

\[
 \boxed{
 A_{H,c}=c^T\Theta^Hc
 =c^TQ^Hc+\sum_{\ell=1}^H
 \langle\mathsf P_\ell,Q^{\ell-1}\rangle_F.}
\tag{3.6}
\]

## 4. Frozen forward four-jet block

Let \(Z_\ell^{[r]},X_\ell^{[r]}\) denote ordinary derivatives at zero along
the frozen line \(\theta+s v_c\). The bracket labels derivative order, not a
Taylor coefficient. Entrywise,

\[
\begin{aligned}
 X_\ell^{[0]}&=\phi(Z_\ell^{[0]}),\\
 X_\ell^{[1]}&=\phi'(Z_\ell^{[0]})\odot Z_\ell^{[1]},\\
 X_\ell^{[2]}&=\phi''(Z_\ell^{[0]})\odot(Z_\ell^{[1]})^2
 +\phi'(Z_\ell^{[0]})\odot Z_\ell^{[2]},\\
 X_\ell^{[3]}&=\phi'''(Z_\ell^{[0]})\odot(Z_\ell^{[1]})^3
 +3\phi''(Z_\ell^{[0]})\odot Z_\ell^{[1]}
      \odot Z_\ell^{[2]}
 +\phi'(Z_\ell^{[0]})\odot Z_\ell^{[3]}.
\end{aligned}
\tag{4.1}
\]

At layer one take \(Z_1^{[0]}\sim N(0,Q^0)\), independently of
\(R_1\sim N(0,\mathsf B_1)\), and set

\[
 Z_1^{[1]}=\Delta_1Q^0,\qquad
 Z_1^{[2]}=Z_1^{[3]}=0.
\tag{4.2}
\]

Store all sixteen \(B\times B\) covariance blocks

\[
 (G_\ell^{rs})_{\alpha\beta}
 =\mathbb E[
 X_{\ell,\alpha}^{[r]}X_{\ell,\beta}^{[s]}
 ],
 \qquad 0\leq r,s\leq3,
\tag{4.3}
\]

and all four response matrices

\[
 (J_\ell^r)_{\alpha\beta}
 =\mathbb E\!\left[
 \frac{\partial X_{\ell,\beta}^{[r]}}
      {\partial R_{\ell,\alpha}}
 \right].
\tag{4.4}
\]

For each \(\ell\geq2\), introduce one fresh \(4B\)-dimensional centered
Gaussian block
\(F_\ell=(F_\ell^0,F_\ell^1,F_\ell^2,F_\ell^3)\) with

\[
 \operatorname{Cov}(F_{\ell,\alpha}^r,F_{\ell,\beta}^s)
 =(G_{\ell-1}^{rs})_{\alpha\beta}.
\tag{4.5}
\]

It is independent of \(R_\ell\sim N(0,\mathsf B_\ell)\). Define, with the
orientation fixed as in (1.1),

\[
 \Lambda_\ell^r
 =J_{\ell-1}^r+rG_{\ell-1}^{0,r-1},
 \qquad 1\leq r\leq3.
\tag{4.6}
\]

The full response-aware transition is

\[
 Z_\ell^{[0]}=F_\ell^0,\qquad
 Z_\ell^{[r]}=F_\ell^r+\Delta_\ell\Lambda_\ell^r.
\tag{4.7}
\]

In components,

\[
 Z_{\ell,\beta}^{[r]}=F_{\ell,\beta}^r
 +\sum_\alpha\Delta_{\ell,\alpha}
 \left\{
 (J_{\ell-1}^r)_{\alpha\beta}
 +r(G_{\ell-1}^{0,r-1})_{\alpha\beta}
 \right\}.
\tag{4.8}
\]

The \(J\) term is the unique earlier transpose response for \(A^\ell\); the
\(rG\) term is the literal derivative of the moving rank-one weight. After
(4.1), expectations (4.3)--(4.4) close the next layer.

## 5. Forward parity and the NTK response identity

Simultaneously negate every base reverse-carrier innovation and every odd
forward innovation \(F_\ell^1,F_\ell^3\), leaving
\(F_\ell^0,F_\ell^2\) fixed. Induction in (4.1)--(4.8) gives

\[
 X_\ell^{[r]}\longmapsto(-1)^rX_\ell^{[r]}.
\tag{5.1}
\]

Therefore

\[
 G_\ell^{rs}=0\quad(r+s\text{ odd}),\qquad
 J_\ell^r=0\quad(r\text{ even}).
\tag{5.2}
\]

In particular \(\Lambda_\ell^2=0\), so
\(Z_\ell^{[2]}=F_\ell^2\). Direct differentiation with the row convention
gives

\[
 J_\ell^1=\Theta^{\ell-1}\odot E^\ell,\qquad
 \Lambda_{\ell+1}^1
 =J_\ell^1+G_\ell^{00}
 =\Theta^\ell.
\tag{5.3}
\]

For example,

\[
 \frac{\partial X_{\ell,\beta}^{[1]}}
 {\partial R_{\ell,\alpha}}
 =\phi'(Z_{\ell,\beta})\phi'(Z_{\ell,\alpha})
 \Theta^{\ell-1}_{\alpha\beta},
\tag{5.4}
\]

which verifies both indices in (5.3).

The formal derivative in (4.4) can be eliminated from the executable
recurrence. Define the coefficient matrices

\[
 L_1^1=Q^0,\qquad L_1^2=L_1^3=0,\qquad
 L_\ell^r=\Lambda_\ell^r\quad(\ell\geq2),
\tag{5.5}
\]

and the local random matrices

\[
 (U_\ell^r)_{\alpha\beta}
 =\phi'(Z_{\ell,\alpha}^{[0]})(L_\ell^r)_{\alpha\beta}.
\tag{5.6}
\]

Direct differentiation of (4.1), with \(U_\ell^2=0\), gives the completely
explicit response update

\[
\begin{aligned}
 (J_\ell^0)_{\alpha\beta}&=0,\\
 (J_\ell^1)_{\alpha\beta}
 &=\mathbb E[
 \phi'(Z_{\ell,\beta}^{[0]})(U_\ell^1)_{\alpha\beta}
 ],\\
 (J_\ell^2)_{\alpha\beta}
 &=\mathbb E[
 2\phi''(Z_{\ell,\beta}^{[0]})
 Z_{\ell,\beta}^{[1]}(U_\ell^1)_{\alpha\beta}
 ]=0,\\
 (J_\ell^3)_{\alpha\beta}
 &=\mathbb E\!\left[
 3\phi'''(Z_{\ell,\beta}^{[0]})
 (Z_{\ell,\beta}^{[1]})^2(U_\ell^1)_{\alpha\beta}\right.\\
 &\hspace{4em}\left.
 +3\phi''(Z_{\ell,\beta}^{[0]})
 Z_{\ell,\beta}^{[2]}(U_\ell^1)_{\alpha\beta}
 +\phi'(Z_{\ell,\beta}^{[0]})(U_\ell^3)_{\alpha\beta}
 \right].
\end{aligned}
\tag{5.7}
\]

Thus (4.4) is semantic notation, not a request for numerical
differentiation.

## 6. Differentiated reverse pass and all transpose responses

Let tildes denote derivatives of the reverse program along the same frozen
line. The top carrier and every source are

\[
 \widetilde R_H=(X_H^{[0]}c)c^T,
\tag{6.1}
\]

\[
 \widetilde\Delta_\ell
 =\phi''(Z_\ell^{[0]})\odot Z_\ell^{[1]}\odot R_\ell
 +\phi'(Z_\ell^{[0]})\odot\widetilde R_\ell.
\tag{6.2}
\]

Define

\[
 (\boldsymbol\beta_\ell)_{\alpha\beta}
 =\mathbb E[
 \widetilde\Delta_{\ell,\alpha}
 \widetilde\Delta_{\ell,\beta}
 ],
 \qquad
 (S_\ell)_{\alpha\beta}
 =\mathbb E[
 \Delta_{\ell,\alpha}
 \widetilde\Delta_{\ell,\beta}
 ],
\tag{6.3}
\]

and, for \(\ell\geq2\),

\[
 (\rho_\ell^r)_{\alpha\beta}
 =\mathbb E\!\left[
 \frac{\partial\widetilde\Delta_{\ell,\beta}}
      {\partial F_{\ell,\alpha}^r}
 \right],
 \qquad0\leq r\leq3.
\tag{6.4}
\]

The base and differentiated transpose innovations of the same raw matrix
have the complete joint covariance

\[
 \operatorname{Cov}
 \begin{pmatrix}
 \widehat R_{\ell-1}\\
 \mathcal E_{\ell-1}
 \end{pmatrix}
 =
 \begin{pmatrix}
 \mathsf P_\ell&S_\ell\\
 S_\ell^T&\boldsymbol\beta_\ell
 \end{pmatrix}.
\tag{6.5}
\]

Before cancellation, the transpose rule and the direct differentiated
weight give

\[
 \widetilde R_{\ell-1}
 =\mathcal E_{\ell-1}
 +X_{\ell-1}^{[0]}\mathsf P_\ell
 +\sum_{r=0}^3X_{\ell-1}^{[r]}\rho_\ell^r.
\tag{6.6}
\]

The direct term has orientation

\[
 [\dot A^{\ell T}\Delta_\ell]_\beta
 =\sum_\alpha X_{\ell-1,\alpha}^{[0]}
 (\mathsf P_\ell)_{\alpha\beta}.
\tag{6.7}
\]

The four terms in the last sum of (6.6) are exactly the responses to the
four earlier forward uses
\(F_\ell^0,F_\ell^1,F_\ell^2,F_\ell^3\); none is hidden in a covariance.

The parity involution makes \(\Delta_\ell\) odd and
\(\widetilde\Delta_\ell\) even, hence

\[
 S_\ell=0.
\tag{6.8}
\]

At the top, \(\widetilde R_H\) depends only on \(F_H^0\). Inductively, if
the upper transition has the form derived below, then
\(\widetilde R_\ell\) depends only on a fresh \(\mathcal E_\ell\) and
\(F_\ell^0\). Thus \(\widetilde\Delta_\ell\) contains \(F_\ell^1\) but no
\(F_\ell^2,F_\ell^3\), and

\[
 \rho_\ell^2=\rho_\ell^3=0
 \quad\text{syntactically}.
\tag{6.9}
\]

Moreover

\[
 \frac{\partial\widetilde\Delta_{\ell,\beta}}
 {\partial F_{\ell,\alpha}^1}
 =\mathbf1_{\alpha=\beta}
 \phi''(Z_{\ell,\beta})R_{\ell,\beta},
\tag{6.10}
\]

whose expectation vanishes because \(R_\ell\) is centered and independent
of \(Z_\ell^{[0]}\). Hence

\[
 \rho_\ell^1=\rho_\ell^2=\rho_\ell^3=0,\qquad
 \boldsymbol\chi_\ell=\mathsf P_\ell+\rho_\ell^0,
\tag{6.11}
\]

and the closed transition is

\[
 \boxed{
 \mathcal E_{\ell-1}\sim N(0,\boldsymbol\beta_\ell),\qquad
 \widetilde R_{\ell-1}
 =\mathcal E_{\ell-1}
 +X_{\ell-1}^{[0]}\boldsymbol\chi_\ell.}
\tag{6.12}
\]

By (6.8), \(\mathcal E_{\ell-1}\) is jointly independent of the base reverse
innovation \(R_{\ell-1}\). Equations (6.1)--(6.4) and (6.11)--(6.12),
evaluated from \(\ell=H\) down to \(1\), determine every
\(\boldsymbol\beta_\ell\) and
needed response through finite local Gaussian expectations. No additional
state appears at depth three or beyond.

The remaining formal derivative in (6.4) also has a closed local formula.
Initialize
\(\boldsymbol\chi_{H+1}=cc^T\) and
\(\mathcal E_H=0\), so that
\(\widetilde R_\ell
=\mathcal E_\ell+X_\ell^{[0]}\boldsymbol\chi_{\ell+1}\)
includes the top rule (6.1). For \(\ell\geq2\), abbreviate
\(\phi^{(k)}_{\ell,\alpha}
=\phi^{(k)}(F_{\ell,\alpha}^0)\). Then

\[
\begin{aligned}
 (\rho_\ell^0)_{\alpha\beta}
 ={}&\mathbf1_{\alpha=\beta}
 \mathbb E[
 \phi'''_{\ell,\beta}Z_{\ell,\beta}^{[1]}R_{\ell,\beta}
 +\phi''_{\ell,\beta}\widetilde R_{\ell,\beta}
 ]\\
 &+(\Lambda_\ell^1)_{\alpha\beta}
 \mathbb E[
 \phi''_{\ell,\alpha}\phi''_{\ell,\beta}
 R_{\ell,\alpha}R_{\ell,\beta}
 ]\\
 &+(\boldsymbol\chi_{\ell+1})_{\alpha\beta}
 \mathbb E[
 \phi'_{\ell,\alpha}\phi'_{\ell,\beta}
 ].
\end{aligned}
\tag{6.13}
\]

Together, (5.7), (6.2)--(6.3), and (6.13) make every response update an
explicit Gaussian expectation involving derivatives through order three.

## 7. Terminal straight and Hessian contractions

The straight-line term is

\[
 \boxed{
 T_{H,c}=\mathbb E\!\left[
 \sum_\alpha R_{H,\alpha}X_{H,\alpha}^{[3]}
 \right]
 +3c^TG_H^{02}c.}
\tag{7.1}
\]

The readout block is

\[
 \mathcal H_{a,c}=c^TG_H^{11}c.
\tag{7.2}
\]

For the first and later raw weight matrices,

\[
 \mathcal H_{W^1,c}
 =\langle\boldsymbol\beta_1,Q^0\rangle_F,
\tag{7.3}
\]

\[
 \mathcal H_{W^\ell,c}
 =\langle\boldsymbol\beta_\ell,Q^{\ell-1}\rangle_F
 +\langle\mathsf P_\ell,G_{\ell-1}^{11}\rangle_F,
 \qquad2\leq\ell\leq H.
\tag{7.4}
\]

Before parity, (7.4) contains the two oriented cross contractions made from
\(S_\ell\) and \(G_{\ell-1}^{01}\), together with their transposes. Both
vanish by (5.2) and (6.8); no mixed Hessian term is discarded without a
certificate. Therefore

\[
 \mathcal H_{H,c}=c^TG_H^{11}c
 +\langle\boldsymbol\beta_1,Q^0\rangle_F
 +\sum_{\ell=2}^H
 \left\{
 \langle\boldsymbol\beta_\ell,Q^{\ell-1}\rangle_F
 +\langle\mathsf P_\ell,G_{\ell-1}^{11}\rangle_F
 \right\},
\tag{7.5}
\]

and

\[
 \boxed{C_{H,c}=2T_{H,c}+4\mathcal H_{H,c}.}
\tag{7.6}
\]

## 8. Gaussian-normal-form emission

Equations (3.1)--(7.6) are a compact Gaussian-expectation DAG. A forward
layer integrates one \(4B\)-dimensional Gaussian block and one
\(B\)-dimensional reverse carrier. A reverse layer additionally integrates
one \(B\)-dimensional differentiated-reverse innovation. The retained
algebraic state is \(O(B^2)\) per layer: sixteen \(G^{rs}\) blocks, four
\(J^r\) blocks, and the reverse covariance/response blocks.

To remove raw auxiliary Gaussian coordinates and emit literal activation
atoms, repeatedly use the inverse-free Wick--Stein identity. If
\(Y_1,\ldots,Y_m\) are auxiliary centered Gaussian coordinates and
\(Z\in\mathbb R^B\) is the activation argument, then

\[
\begin{aligned}
 \mathbb E[Y_1Y_2\cdots Y_mF(Z)]
 ={}&
 \sum_{j=2}^m\operatorname{Cov}(Y_1,Y_j)
 \mathbb E\!\left[
 \prod_{k\ne1,j}Y_kF(Z)
 \right]\\
 &+\sum_{\alpha=1}^B
 \operatorname{Cov}(Y_1,Z_\alpha)
 \mathbb E\!\left[
 \prod_{k\ne1}Y_k\,\partial_{Z_\alpha}F(Z)
 \right].
\end{aligned}
\tag{8.1}
\]

Each step lowers auxiliary degree, so it terminates at atoms

\[
 \mathcal I(Q;(i_1,r_1),\ldots,(i_m,r_m))
 =\mathbb E_{Z\sim N(0,Q)}
 \prod_{j=1}^m\phi^{(r_j)}(Z_{i_j}).
\tag{8.2}
\]

Their covariance entries are earlier scalar DAG nodes, so recursively
flattening the construction gives a finite polynomial in literal
\(B\)-dimensional activation atoms. Equation (8.1) never inverts \(Q\), and
therefore covers singular and repeated inputs.

The compact recursion itself evaluates only
\(\phi,\phi',\phi'',\phi'''\). After parity, \(F_\ell^2\) is the only
auxiliary forward-jet coordinate that can both occur explicitly and have
nonzero covariance with the activation argument \(F_\ell^0\). Each
\(X_\ell^{[r]}\) is at most linear in \(F_\ell^2\), so a stored Gram
integrand contains at most two such factors. Therefore (8.1) applies at
most two base derivatives to an integrand that initially uses derivatives
through order three. This also covers every terminal and reverse family:
\(T_{H,c}\) contains only one \(X^{[3]}\), hence at most one explicit
\(F^2\); \(\boldsymbol\beta_\ell\) and \(\rho_\ell^0\) use only
\(F^0,F^1,R,\mathcal E\); and the Hessian terminal uses only
\(G^{11}\) and \(\boldsymbol\beta\). The fully activation-only atom list
consequently uses at most \(\phi^{(5)}\). The all-derivative hypothesis in
Section 9 is kept
because it is the clean hypothesis of the cited tensor-program theorem, not
because this order-three formula needs an unbounded derivative order.

The size of a flat monomial list can still grow rapidly with \(H\). The
claim is finite recursive computability, not an \(O(H)\) bound for the
flattened formula.

## 9. Fixed-\(H,B\) probability claim and boundary

Assume:

1. \(H\) and \(B\) are fixed independently of \(n\);
2. \(Q^0\succeq0\) is deterministic, with singularity allowed;
3. the readout and all raw weight matrices are mutually independent standard
   Gaussians with the normalization in (1.3);
4. \(\phi\in C^\infty\), and every derivative has polynomial growth.

For fixed \(H,B\), the base pass, four-jet, differentiated reverse pass, and
all normalized products in (1.5) form a finite
NETSOR\({}^T+\) program. The chronological uses of every
\(A^\ell,(A^\ell)^T\) are exactly those enumerated in (4.7) and (6.6).
The transpose master rule gives (2.2)--(2.4), hence the displayed recursion.
The polynomially-smooth tensor-program convergence theorem gives
almost-sure and every-finite-\(L^p\) convergence of all scalar contractions.
Finite arithmetic then yields (3.6) and (7.6), while \(L^1\) convergence
gives the corresponding limits of expectations.

The independent audit in DEPTH_FIXED_BATCH_HOSTILE_AUDIT.md confirms this
precise NETSOR\({}^T+\) mapping and its chronological response registry
against the external theorem statement. The probability claim therefore
rests on the fixed-program theorem, not merely on the passing polynomial
contractions.

The claim is pointwise. It supplies no uniform estimate when \(H=H(n)\) or
\(B=B(n)\), no uniform conditioning guarantee, and no bound on flat symbolic
expansion size. Under only finitely many activation derivatives, the
algebraic recursion still exists, but the annealed limit requires a separate
uniform-integrability theorem.

## 10. Independent executable gates

### 10.1 Analytic reductions on both accepted axes

When \(B=1\), every displayed matrix becomes a scalar. The exact dictionary
to DEPTH_B1_GAUSSIAN_RECURSION.md is

\[
 \mathsf B_\ell=b_\ell,\qquad
 \mathsf P_\ell=p_\ell,\qquad
 G_\ell^{rs}=G^\ell_{rs},\qquad
 J_\ell^r=a^\ell_r.
\]

Then (4.6) is
\(\lambda_{\ell r}=a^{\ell-1}_r+rG^{\ell-1}_{0,r-1}\),
(6.11)--(6.12) are
\(\chi_\ell=p_\ell+\rho_{\ell0}\) and
\(\widetilde R_{\ell-1}=E_{\ell-1}+\chi_\ell X_{\ell-1}^{[0]}\),
and (7.1)--(7.6) are exactly its terminal equations (6.1)--(6.6).
Thus the joint recursion reduces atomwise, rather than only numerically, to
the accepted arbitrary-depth one-sample recursion.

When \(H=2\), the dictionary to
b2/B2_GAUSSIAN_NORMAL_FORM.md is

\[
\begin{gathered}
 Q^1=\mathsf Q,\qquad
 \mathsf P_2=\mathsf D,\qquad
 J_1^1=\mathsf L,\qquad
 G_1^{11}=\mathsf G,\\
 G_1^{02}=\mathsf M,\qquad
 J_1^3=\mathsf N,\qquad
 \Lambda_2^1=\mathsf K=\mathsf Q+\mathsf L,\qquad
 \Lambda_2^3=\boldsymbol\kappa=3\mathsf M+\mathsf N.
\end{gathered}
\]

The reverse dictionary is

\[
 \boldsymbol\beta_2=\beta,\qquad
 \rho_2^0=\rho,\qquad
 \boldsymbol\chi_2=\mathsf D+\rho=\chi.
\]

Consequently (7.1) is its \(T_c\), while (7.2)--(7.4) are its
\(H_{a,c},H_{W,c},H_{U,c}\), with the same source/output index orientation.

### 10.2 Exact audit backend

The audit implementation fixed_batch_polynomial_reference.py was written
directly from Sections 1--7 using sparse multivariate polynomials and exact
rational Isserlis contraction. It does not call either accepted one-axis
evaluator. Run:

    python -m studies.mean_field_peeling.generic_first_stieltjes.depth.run_fixed_batch_gates

The four gate families are:

1. **\(H=2\), arbitrary fixed batch.** NTK, straight term, readout Hessian,
   middle Hessian, first-layer Hessian, and \(C_c\) agree exactly, block by
   block, with b2/contracted_gnf_polynomial_reference.py for constant,
   linear, affine, quadratic, and cubic activations.
2. **\(B=1\), arbitrary fixed depth.** Through \(H=4\), all four terminal
   scalars agree with the separately contracted recurrence in
   gnf_audit_reference.py for linear, affine, quadratic, and
   \(x+x^2/10\).
3. **Genuinely joint nonlinear gate.** For

   \[
   H=3,\quad
   Q^0=\begin{pmatrix}1&1/3\\1/3&4/3\end{pmatrix},\quad
   c=(2/3,-1/4)^T,\quad
   \phi(x)=x+x^2/10,
   \tag{10.1}
   \]

   the independent exact result is

   \[
   A_{3,c}
   =\frac{307537184532813623}{164025000000000000},
   \tag{10.2}
   \]

   \[
   C_{3,c}
   =
   \frac{68550715812209572302778459455166819}
   {1261134404296875000000000000000000}
   \approx54.35639181569145.
   \tag{10.3}
   \]

   Every entry of \(S_\ell\) and every
   \(\rho_\ell^1,\rho_\ell^2,\rho_\ell^3\) is exactly zero. Exact
   batch-permutation equivariance, degree-two/four channel homogeneity, and
   absence of inactive-channel leakage also pass. A rank-one repeated-input
   Gram with two nonzero channel entries reduces to the accepted \(B=1\)
   result with channel factors
   \((\sum_\alpha c_\alpha)^2\) and
   \((\sum_\alpha c_\alpha)^4\).
4. **Deep linear control.** For arbitrary fixed batch geometry, with
   \(q_c=c^TQ^0c\),

   \[
   A_{H,c}=(H+1)q_c,\qquad
   C_{H,c}=\frac23H(H+1)^2(H+2)q_c^2,
   \tag{10.4}
   \]

   exactly through every tested \(H=1,2,3,4\).

After this derivation and implementation were frozen, comparison with the
separately written FIXED_H_FIXED_B_GNF_TEMPLATE.md found no index or
response discrepancy. In particular, both derivations use
\(G^{0,r-1}\), rather than its transpose, in (4.6), and use
\(X^{[0]}\mathsf P_\ell\), rather than
\(X^{[0]}\mathsf P_\ell^T\), in (6.6).

## 11. Physical MSE loss mapping

Let \(y\in\mathbb R^B\),

\[
 \mathcal L_n=\frac1B\|y-f_n\|^2,
\tag{11.1}
\]

and first take raw-metric flow
\(\dot\theta=-n\nabla\mathcal L_n\). At the differentiated point put

\[
 r=y-f_n,\qquad d=\frac rB,\qquad
 j_\alpha=\nabla f_\alpha,\qquad
 K_{\alpha\beta}=n j_\alpha\mathbin\cdot j_\beta,
\tag{11.2}
\]

\[
 p=\nabla g_d,\qquad
 H_\alpha=\nabla^2f_\alpha,\qquad
 H_d=\sum_\alpha d_\alpha H_\alpha,\qquad
 \mathcal A=\frac1B\sum_\alpha j_\alpha\otimes j_\alpha.
\tag{11.3}
\]

Holding \(d\) frozen when forming \(C_{n,d}=D_d^3g_d\), universal
finite-width gradient-flow calculus gives

\[
\begin{aligned}
 \mathcal L_n'''(0)={}&
 -\frac{64}{B^4}r^TK^3r-16C_{n,d}\\
 &+128n^3p^T\mathcal A H_dp
 +\frac{96n^3}{B}\sum_\alpha
 (j_\alpha\mathbin\cdot p)H_\alpha[p,p].
\end{aligned}
\tag{11.4}
\]

Thus \(C_{n,d}\) alone is not the complete finite-width arbitrary-label
loss derivative. For a frozen deterministic channel, the two scalars on the
second line of (11.4) are odd under the exact involution that negates the
whole readout vector and fixes every hidden matrix. Their expectations are
zero at every finite width. They are also finite tensor programs at fixed
\(H,B\), so a deterministic limiting-value theorem forces their quenched
limits to be zero as well.

At centered initialization, all remaining terms produced by replacing the
actual \(d=(y-f_n)/B\) with the deterministic channel

\[
 c_y=\frac yB
\tag{11.5}
\]

contain at least one initial-output factor. They vanish by Hölder because
\(f_n\to0\) in every finite \(L^p\). The same finite-dimensional
polarization argument applies to the quartic map \(c\mapsto C_{n,c}\).

Now use learning-rate factor \(\eta\). Write \(\Theta^H\) for (3.5), and
insert \(c_y\) into the joint recursion. Define the formal third Taylor jet

\[
 \mathcal J_3[h](t)=\sum_{k=0}^3\frac{h^{(k)}(0)}{k!}t^k.
\tag{11.6}
\]

Then the following limit is coefficientwise, one derivative at a time:

\[
\begin{aligned}
 \lim_{n\to\infty}\mathcal J_3[
 \mathbb E\mathcal L_n
 ](t)
 ={}&\frac{y^Ty}{B}
 -\frac{4\eta}{B^2}y^T\Theta^Hy\,t
 +\frac{8\eta^2}{B^3}y^T(\Theta^H)^2y\,t^2\\
 &-\left\{
 \frac{32\eta^3}{3B^4}y^T(\Theta^H)^3y
 +\frac{8\eta^3}{3}C_{H,y/B}
 \right\}t^3
 \pmod{t^4}.
\end{aligned}
\tag{11.7}
\]

Thus the first non-NTK loss correction is

\[
 \boxed{-\frac83\eta^3C_{H,y/B}\,t^3.}
\tag{11.8}
\]

This is a coefficientwise statement at \(t=0\), not a claim about the loss
at fixed positive time. Also, for a generic activation \(C_{H,c}\) need not
be nonnegative; Stieltjes correction here names the first nonlinear feature
coefficient, not an independently proved positive moment.
