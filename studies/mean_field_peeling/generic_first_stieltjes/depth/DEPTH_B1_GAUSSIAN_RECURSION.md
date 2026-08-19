# Arbitrary fixed depth, one-sample Gaussian-normal-form recursion

**Status.** Independently audited exact fixed-\(H\), \(B=1\) theorem under
the polynomially-smooth activation envelope.  The response-aware proof IR
and the separately contracted one-dimensional-atom recurrence agree through
\(H=4\) on polynomial and smooth nonlinear controls.  This note is
separate from `EXACT_FIXED_DEPTH_PROGRAM.md`, which is the finite-width
moving-gradient compiler.  No Hermite or polynomial approximation of the
activation is used.

We take one input with \(q_0=\|x\|^2/d_0\geq0\), \(H\geq1\) hidden layers,
one shared activation \(\phi\), standard-Gaussian raw weights, and

\[
 z^1=W^1x/\sqrt{d_0},\qquad
 z^\ell=W^\ell x^{\ell-1}/\sqrt n,\qquad
 x^\ell=\phi(z^\ell),\qquad
 f_n=n^{-1}a^Tx^H.
\tag{1.1}
\]

Let \(D_n=n\nabla f_n\cdot\nabla\).  The goal is

\[
 A_H=\lim_{n\to\infty}D_nf_n,
 \qquad C_H=\lim_{n\to\infty}D_n^3f_n.
\tag{1.2}
\]

All limits below hold almost surely and in every finite \(L^p\).  In
particular they also give limits of expectations.

## 1. Exact source identity

Put \(v=n\nabla f_n\), let \(\widehat f_n(t)=f_n(\theta+tv)\) be the
**frozen** parameter line, and define

\[
 T_{n,H}=\widehat f_n'''(0),\qquad
 \mathcal H_{n,H}=n\|\nabla^2f_n\,v\|^2.
\tag{1.3}
\]

Differentiating \(D_n=n\nabla f_n\cdot\nabla\), including the variation of
its vector field, gives the finite-width identity

\[
 D_n^3f_n=2T_{n,H}+4\mathcal H_{n,H}.
\tag{1.4}
\]

Thus it suffices to Gaussianize a frozen order-three forward jet and the
first derivative of the reverse jet.

## 2. The response-aware matrix rule

The following rule fixes every transpose/Onsager coefficient used later.
For one matrix \(A=W/\sqrt n\), list its uses in their actual program order.
If

\[
 F_j=Au_j,\qquad T_k=A^Tv_k,
\]

then their limiting coordinate representatives have the recursive form

\[
 [F_j]=\widehat F_j+
 \sum_{k:T_k\prec F_j}[v_k]\,
 \mathbb E\!\left[\partial_{\widehat T_k}[u_j]\right],
\tag{2.1}
\]

\[
 [T_k]=\widehat T_k+
 \sum_{j:F_j\prec T_k}[u_j]\,
 \mathbb E\!\left[\partial_{\widehat F_j}[v_k]\right].
\tag{2.2}
\]

The forward innovations are jointly centered Gaussian with

\[
 \operatorname{Cov}(\widehat F_i,\widehat F_j)
 =\mathbb E[[u_i][u_j]],
\tag{2.3}
\]

and the transpose innovations satisfy the analogous formula with the
\(v_k\)'s.  In the chronological program below, the fresh forward and
transpose innovation blocks can be taken independent; all leading
cross-orientation dependence is carried by the displayed response sums.
Different raw matrices have independent innovation blocks.  Derivatives in
(2.1)--(2.2) are
**syntactic partial derivatives** of the already constructed coordinate
program.  This formulation uses no covariance inverse and remains valid when
an innovation Gram is singular.

Equations (2.1)--(2.3) are the Gaussian-conditioning/Stein form of the
Tensor-Program transpose rule.  They can also be proved directly, one use at
a time, by Gaussian integration by parts in the entries of \(W\).  There is
only one earlier opposite-orientation use in every forward transition below;
the differentiated reverse transition sees exactly four earlier forward
uses.  Consequently (2.1)--(2.2) enumerate, rather than suppress, all
possible response branches.

## 3. Base covariance and reverse pass

First compute the ordinary NNGP and derivative atoms

\[
 Z_1\sim N(0,q_0),\qquad
 q_\ell=\mathbb E[\phi(Z_\ell)^2],\qquad
 d_\ell=\mathbb E[\phi'(Z_\ell)^2],
\qquad Z_{\ell+1}\sim N(0,q_\ell).
\tag{3.1}
\]

All displayed Gaussian variables in (3.1) may be chosen independent.  Let
\(R_\ell\) be the coordinate representative of the reverse carrier entering
layer \(\ell\), and let

\[
 \Delta_\ell=\phi'(Z_\ell)R_\ell,
 \qquad b_\ell=\mathbb E[R_\ell^2],
 \qquad p_\ell=\mathbb E[\Delta_\ell^2].
\tag{3.2}
\]

The top readout gives \(b_H=1\).  Applying (2.2) to the base reverse pass,

\[
 b_{\ell-1}=p_\ell,\qquad p_\ell=d_\ell b_\ell,
 \qquad \ell=H,H-1,\ldots,2.
\tag{3.3}
\]

There is no omitted response in (3.3): the only candidate is
\(\mathbb E[\partial_{Z_\ell}\Delta_\ell]\), and it is zero because
\(R_\ell\) is centered and independent of \(Z_\ell\).  Induction therefore
shows that the \(R_\ell\)'s are independent centered Gaussians, independent
of all base forward preactivations, with

\[
 b_\ell=\prod_{j=\ell+1}^H d_j,\qquad
 p_\ell=\prod_{j=\ell}^H d_j.
\tag{3.4}
\]

Define the scalar NTK recursion

\[
 \Theta_0=q_0,\qquad \Theta_\ell=q_\ell+d_\ell\Theta_{\ell-1}.
\tag{3.5}
\]

Then already

\[
 A_H=q_H+q_0p_1+\sum_{\ell=2}^Hq_{\ell-1}p_\ell
     =\Theta_H.
\tag{3.6}
\]

## 4. Frozen forward jet: one four-Gaussian block per layer

Write \(Z_\ell^{[r]}\) and \(X_\ell^{[r]}\) for the \(r\)-th ordinary
derivatives at zero of the frozen-line preactivation and activation,
respectively.  Thus \(X_\ell^{[0]}=\phi(Z_\ell)\).  At the first layer,

\[
 Z_1^{[1]}=q_0\Delta_1,\qquad
 Z_1^{[2]}=Z_1^{[3]}=0,
\tag{4.1}
\]

and at every layer the scalar chain rule is

\[
\begin{aligned}
 X_\ell^{[1]}&=\phi'(Z_\ell)Z_\ell^{[1]},\\
 X_\ell^{[2]}&=\phi''(Z_\ell)(Z_\ell^{[1]})^2
                 +\phi'(Z_\ell)Z_\ell^{[2]},\\
 X_\ell^{[3]}&=\phi'''(Z_\ell)(Z_\ell^{[1]})^3
 +3\phi''(Z_\ell)Z_\ell^{[1]}Z_\ell^{[2]}
 +\phi'(Z_\ell)Z_\ell^{[3]}.
\end{aligned}
\tag{4.2}
\]

After constructing layer \(\ell\), store only

\[
 G^\ell_{rs}=\mathbb E[X_\ell^{[r]}X_\ell^{[s]}],
 \qquad 0\leq r,s\leq3,
\tag{4.3}
\]

and the four response derivatives

\[
 a^\ell_r=\mathbb E\!\left[
       \partial_{R_\ell}X_\ell^{[r]}\right].
\tag{4.4}
\]

For \(\ell\geq2\), introduce one centered Gaussian block

\[
 F_\ell=(F_{\ell0},F_{\ell1},F_{\ell2},F_{\ell3})
 \sim N(0,G^{\ell-1}),
 \tag{4.5}
\]

independent of \(R_\ell\) and of the blocks belonging to other matrices.
The four entries are the fresh parts of
\(A^\ell X_{\ell-1}^{[r]}\).  Formula (2.1), followed by the literal product
rule for \(A^\ell(t)X_{\ell-1}(t)\), gives the complete transition

\[
 Z_\ell^{[0]}=F_{\ell0},
\tag{4.6}
\]

\[
 Z_\ell^{[r]}=F_{\ell r}
 +\lambda_{\ell r}\Delta_\ell,
 \qquad
 \lambda_{\ell r}
 =a^{\ell-1}_r+rG^{\ell-1}_{0,r-1},\qquad 1\leq r\leq3.
\tag{4.7}
\]

The first summand in \(\lambda_{\ell r}\) is the transpose response; the
second is the direct rank-one weight-direction term.  Thus every response is
explicitly registered.  Equations (4.2)--(4.7), followed by the finite
Gaussian expectations (4.3)--(4.4), are the bottom-up straight-jet
recursion.

There is a useful exact parity certificate.  Simultaneously negate all base
reverse carriers and all odd forward innovations.  Then

\[
 X_\ell^{[r]}\mapsto(-1)^rX_\ell^{[r]}.
\tag{4.8}
\]

Consequently

\[
 G^\ell_{rs}=0\quad(r+s\text{ odd}),\qquad
 a^\ell_r=0\quad(r\text{ even}),
\tag{4.9}
\]

so \(Z_\ell^{[2]}=F_{\ell2}\).  Moreover

\[
 a^{\ell-1}_1=d_{\ell-1}\Theta_{\ell-2},qquad
 \lambda_{\ell1}=\Theta_{\ell-1}.
\tag{4.10}
\]

Keeping the unsimplified (4.7) is nevertheless useful: it identifies the
zero branches rather than silently deleting them.

## 5. Differentiated reverse pass

Let \(\widetilde R_\ell\) and \(\widetilde\Delta_\ell\) be the derivatives,
along the same frozen direction, of the reverse carrier and source.  At the
top,

\[
 \widetilde R_H=X_H^{[0]},
\tag{5.1}
\]

and at every layer

\[
 \widetilde\Delta_\ell
 =\phi''(Z_\ell)Z_\ell^{[1]}R_\ell
  +\phi'(Z_\ell)\widetilde R_\ell.
\tag{5.2}
\]

Define

\[
 \beta_\ell=\mathbb E[\widetilde\Delta_\ell^2],
 \qquad
 \rho_{\ell r}=\mathbb E\!\left[
    \partial_{F_{\ell r}}\widetilde\Delta_\ell\right]
 \quad(\ell\geq2,\ 0\leq r\leq3).
\tag{5.3}
\]

When passing from layer \(\ell\) to \(\ell-1\), introduce the fresh
transpose innovation

\[
 E_{\ell-1}\sim N(0,\beta_\ell).
\tag{5.4}
\]

The differentiated matrix product has the exact response expansion

\[
 \widetilde R_{\ell-1}
 =E_{\ell-1}+p_\ell X_{\ell-1}^{[0]}
  +\sum_{r=0}^3\rho_{\ell r}X_{\ell-1}^{[r]}.
\tag{5.5}
\]

Here \(p_\ell X_{\ell-1}^{[0]}\) is the direct
\((\dot A^\ell)^T\Delta_\ell\) term, while the sum is precisely the four
branches in (2.2), one for each earlier forward use (4.5).

Parity gives the complete simplification certificate

\[
 \mathbb E[\Delta_\ell\widetilde\Delta_\ell]=0,
 \qquad \rho_{\ell1}=\rho_{\ell2}=\rho_{\ell3}=0.
\tag{5.6}
\]

The first equality says that the new transpose innovation is uncorrelated,
hence jointly independent, of the earlier base transpose innovation
\(R_{\ell-1}\).  The \(r=2,3\) responses vanish because (5.2) never uses
those innovations; the \(r=1\) derivative is
\(\phi''(Z_\ell)R_\ell\), whose expectation is zero.  Therefore (5.5) is
equivalently

\[
 \widetilde R_{\ell-1}
 =E_{\ell-1}+\chi_\ell X_{\ell-1}^{[0]},
 \qquad \chi_\ell=p_\ell+\rho_{\ell0}.
\tag{5.7}
\]

Equations (5.1)--(5.7) recursively determine \(\beta_H,\ldots,\beta_1\)
top down through explicit local Gaussian expectations.

## 6. Terminal normal form

The straight third derivative is

\[
 T_H=\mathbb E[R_HX_H^{[3]}]+3G^H_{02}.
\tag{6.1}
\]

The readout, hidden-matrix, and first-matrix Hessian-square blocks are

\[
 \mathcal H_{a}=G^H_{11},
\tag{6.2}
\]

\[
 \mathcal H_{W^\ell}
 =q_{\ell-1}\beta_\ell+p_\ell G^{\ell-1}_{11},
 \qquad 2\leq\ell\leq H,
\tag{6.3}
\]

\[
 \mathcal H_{W^1}=q_0\beta_1.
\tag{6.4}
\]

Before parity, (6.3) also contains
\(2\mathbb E[\Delta_\ell\widetilde\Delta_\ell]
G^{\ell-1}_{01}\); both factors vanish by (4.9) and (5.6).  Hence

\[
 \mathcal H_H=G^H_{11}+q_0\beta_1
 +\sum_{\ell=2}^H
   \left(q_{\ell-1}\beta_\ell+p_\ell G^{\ell-1}_{11}\right),
\tag{6.5}
\]

and the requested coefficient is

\[
 \boxed{A_H=\Theta_H,\qquad C_H=2T_H+4\mathcal H_H.}
\tag{6.6}
\]

Equations (3.1)--(6.6) are a finite dependency DAG.  Each layer uses one
four-dimensional forward Gaussian block, one one-dimensional base reverse
Gaussian, and in the top-down pass one one-dimensional differentiated-reverse
Gaussian.

## 7. Literal activation-atom emission

Intermediate blocks such as \(F_\ell\) are an IR, not terminal atoms.  To
emit the literal Gaussian normal form, expand every local expression into
monomials in the auxiliary Gaussian coordinates times products of
\(\phi^{(r)}(F_{\ell0})\), and repeatedly apply

\[
\begin{aligned}
 &\mathbb E\!\left[G_{i_1}\cdots G_{i_m}F(Z)\right]\\
 &\quad=\sum_{s=2}^m
 \operatorname{Cov}(G_{i_1},G_{i_s})
 \mathbb E\!\left[\prod_{r\ne1,s}G_{i_r}F(Z)\right]\\
 &\qquad+\operatorname{Cov}(G_{i_1},Z)
 \mathbb E\!\left[\prod_{r\ne1}G_{i_r}F'(Z)\right].
\end{aligned}
\tag{7.1}
\]

Choose \(G_{i_1}\) to be an auxiliary coordinate, not the activation
argument \(Z=F_{\ell0}\).  Every application reduces the number of raw
auxiliary factors, so (7.1) terminates.  Its leaves are exactly

\[
 \mathcal I(q_{\ell-1};r_1,\ldots,r_m)
 =\mathbb E_{Z\sim N(0,q_{\ell-1})}
   \prod_{j=1}^m\phi^{(r_j)}(Z).
\tag{7.2}
\]

This inverse-free Wick--Stein recursion also covers \(q_{\ell-1}=0\) and
singular \(G^{\ell-1}\).  Thus (3.1)--(6.6), with (7.1), emits a literal
finite polynomial in one-dimensional Gaussian activation atoms: no raw
readout, carrier, or auxiliary Gaussian coordinate remains.

The deterministic implementation is ‘gnf_recursion.py’.  It isolates the
one activation argument with a high-order Gauss--Hermite rule, integrates the
remaining polynomial Gaussian coordinates with a small exact rule, and
propagates (4.4) and (5.3) by analytic dual formulas rather than finite
differences.  ‘test_gnf_recursion.py’ checks (9.2), exact equality with the
accepted \(H=2\) polynomial and smooth-activation evaluators, and the
deep-linear formula (9.5).

### 7.1 Preferred fully contracted scalar recurrence

The four-Gaussian construction is the proof IR, but the terminal coefficient
needs only three bottom-up scalars and two top-down scalars per layer.  For
\(Z_\ell\sim N(0,q_{\ell-1})\), define the nine semantically named local
atoms

\[
\begin{array}{lll}
 u_\ell=\mathbb E\phi'^4,&
 v_\ell=\mathbb E[\phi\phi''],&
 m_\ell=\mathbb E[\phi\phi''\phi'^2],\\
 r_\ell=\mathbb E[\phi'''\phi'],&
 s_\ell=\mathbb E[\phi''^2],&
 j_\ell=\mathbb E[\phi'''\phi'^3],\\
 e_\ell=\mathbb E[\phi''^2\phi'^2],&
 h_\ell=\mathbb E[\phi'^2\phi^2],&
 w_\ell=\mathbb E[\phi''\phi'^2\phi].
\end{array}
\tag{7.3}
\]

All functions in (7.3) are evaluated at \(Z_\ell\).  The names \(m_\ell\)
and \(w_\ell\) deliberately represent the same commutative Gaussian atom,
but retain its two distinct response roles.

Put

\[
 V_\ell=G^\ell_{11},\qquad
 M_\ell=G^\ell_{02},\qquad
 J_\ell=a^\ell_3.
\tag{7.4}
\]

At the first layer,

\[
 V_1=q_0^2b_1u_1,\qquad
 M_1=q_0^2b_1m_1,\qquad
 J_1=3q_0^3b_1j_1.
\tag{7.5}
\]

For \(2\leq\ell\leq H\), Wick contraction of (4.2)--(4.7) gives

\[
 V_\ell=d_\ell V_{\ell-1}
 +\Theta_{\ell-1}^2b_\ell u_\ell,
\tag{7.6}
\]

\[
 M_\ell=v_\ell V_{\ell-1}
 +\Theta_{\ell-1}^2b_\ell m_\ell
 +(d_\ell+v_\ell)M_{\ell-1},
\tag{7.7}
\]

\[
\begin{aligned}
 J_\ell={}&3\Theta_{\ell-1}V_{\ell-1}r_\ell
 +3\Theta_{\ell-1}^3b_\ell j_\ell\\
 &+3\Theta_{\ell-1}M_{\ell-1}(r_\ell+s_\ell)
 +(J_{\ell-1}+3M_{\ell-1})d_\ell.
\end{aligned}
\tag{7.8}
\]

In particular,

\[
 T_H=J_H+3M_H.
\tag{7.9}
\]

For the reverse contraction initialize

\[
 \beta_{H+1}=0,\qquad \chi_{H+1}=1,\qquad V_0=0,
\tag{7.10}
\]

and, for \(\ell=H,H-1,\ldots,1\), compute

\[
\begin{aligned}
 \beta_\ell={}&b_\ell V_{\ell-1}s_\ell
 +3\Theta_{\ell-1}^2b_\ell^2e_\ell
 +d_\ell\beta_{\ell+1}\\
 &+\chi_{\ell+1}^2h_\ell
 +2\Theta_{\ell-1}\chi_{\ell+1}b_\ell w_\ell,
\end{aligned}
\tag{7.11}
\]

\[
 \rho_{\ell0}
 =\Theta_{\ell-1}b_\ell(r_\ell+s_\ell)
 +\chi_{\ell+1}(v_\ell+d_\ell),
\qquad
 \chi_\ell=p_\ell+\rho_{\ell0}.
\tag{7.12}
\]

Substituting \(V_\ell\) and \(\beta_\ell\) into (6.5) completes the preferred
literal one-dimensional-atom GNF.  The independent implementation
‘gnf_audit_reference.py’ uses exactly (7.3)--(7.12), not the four-Gaussian
quadrature.  Its hostile cross-test matches the proof-IR evaluator through
\(H=4\), separately for \(A_H,T_H,\mathcal H_H,C_H\), for affine,
quadratic, cubic, sine, and tanh activations.

## 8. Atomwise reduction to the accepted \(H=2\) formula

For \(H=2\), write the accepted atom names from
`L2_B1_GAUSSIAN_NORMAL_FORM.md`.  Then

\[
 b_1=p_2=d_2,\qquad \Theta_1=q_1+q_0d_1=c,
\tag{8.1}
\]

and layer one gives

\[
 G^1_{11}=q_0^2d_2e_1,qquad
 G^1_{02}=q_0^2d_2m_1,qquad
 a^1_1=q_0d_1,qquad
 a^1_3=3q_0^3d_2j_1.
\tag{8.2}
\]

Therefore the layer-two block in (4.5) is the accepted block with the
dictionary
\[
 (F_{20},F_{21},F_{22},F_{23})
 =(Z,q_0\Gamma,q_0^2\Omega,q_0^3\Lambda),
\]
and

\[
 Z_2^{[1]}=q_0\Gamma+c\,a\phi'(Z),\qquad
 Z_2^{[2]}=q_0^2\Omega,
\tag{8.3}
\]

\[
 Z_2^{[3]}=q_0^3\Lambda+\kappa\,a\phi'(Z),\qquad
 \kappa=3q_0^2d_2m_1+3q_0^3d_2j_1.
\tag{8.4}
\]

The top differentiated source (5.2) is the accepted \(B\) field.  Its
variance and base-forward response are, atom for atom,

\[
 \beta_2=\tau,qquad
 \rho_{20}=\alpha,qquad
 \chi_2=d_2+\alpha=k,
\tag{8.5}
\]

using the notation of equations (3.2)--(3.4) in that document.  Hence
\(E_1\) is its fresh \(\Eta\), (5.7) is the accepted
\(\dot R=\Eta+k\phi(U)\), and (5.2) at layer one is the accepted
first-layer \(\dot S\).  Equations (6.1) and (6.5) consequently give

\[
 T_2=S_\star,qquad \mathcal H_2=H_\star,qquad
 C_2=2S_\star+4H_\star,
\tag{8.6}
\]

with every covariance and response atom identified, not merely the final
scalar compared.

## 9. Exact controls

For \(H=1\), direct expansion of (4.1)--(6.6) gives, with
\(U\sim N(0,q_0)\),

\[
 A_1=\mathbb E[\phi(U)^2]+q_0\mathbb E[\phi'(U)^2],
\tag{9.1}
\]

\[
\begin{aligned}
 C_1=\mathbb E\big[&
 4q_0^2\phi'^4+4q_0\phi^2\phi'^2\\
 &+14q_0^2\phi\phi''\phi'^2
   +12q_0^3\phi''^2\phi'^2\\
 &+6q_0^3\phi'''\phi'^3\big](U).
\end{aligned}
\tag{9.2}
\]

For the constant activation, \(A_H=\phi^2\) and \(C_H=0\).  For
\(\phi(x)=x\),

\[
 A_H=(H+1)q_0,qquad T_H=0,
\tag{9.3}
\]

\[
 G^\ell_{11}=q_0^2\sum_{k=1}^{\ell}k^2,qquad
 \beta_\ell=q_0\sum_{k=1}^{H-\ell+1}k^2,
\tag{9.4}
\]

and therefore

\[
 C_H=8q_0^2\sum_{k=1}^H(H-k+1)k^2
 =\frac23H(H+1)^2(H+2)q_0^2.
\tag{9.5}
\]

This gives \(C_H/q_0^2=8,48,160,400\) for \(H=1,2,3,4\).

## 10. Fixed-depth theorem and proof boundary

Assume \(\phi\in C^\infty\) and every derivative has polynomial growth.
For every **fixed** \(H\), the straight jet, differentiated reverse jet, and
all normalized products in (1.3) form a finite NETSOR\({}^T+\) program with
reused \(A^\ell,(A^\ell)^T\), scalar moments, and polynomially-smooth
coordinate maps.  Independent Gaussian weights satisfy Setup 3.6 of
Golikov--Yang, *Non-Gaussian Tensor Programs*.  Theorem 3.7 therefore gives
almost-sure and every-finite-\(L^p\) convergence of each scalar moment.  The
transpose part of its master theorem is exactly (2.1)--(2.3).  Finite
arithmetic then proves (3.1)--(6.6), and \(L^1\) convergence gives the
annealed coefficient.

This theorem is pointwise in fixed \(H\).  It does **not** prove:

1. convergence when \(H=H(n)\) grows with width;
2. error bounds, integrability constants, or numerical conditioning uniform
   in depth;
3. an \(O(H)\) bound on the size of the fully expanded atom polynomial.

The recursive numerical state has constant matrix dimension per layer, so a
Gaussian-expectation oracle evaluates the DAG with \(O(H)\) layer
transitions.  In contrast, expanding (7.1) into a flat literal monomial list
can grow rapidly with \(H\); no linear symbolic-size bound is claimed.

## 11. One-label physical-loss corollary

Let \(y_\star\in\mathbb R\) be fixed,
\(L_n=(y_\star-f_n)^2\), and evolve parameters by the physical MSE flow

\[
 \dot\theta=2\eta(y_\star-f_n)n\nabla f_n.
\tag{11.1}
\]

At finite width put
\[
 r_n=y_\star-f_n,\qquad
 K_n=D_nf_n,\qquad J_n=D_n^2f_n,\qquad C_n=D_n^3f_n.
\]
Applying the derivation \(2\eta r_nD_n\) before taking a limit gives

\[
 L_n'=-4\eta r_n^2K_n,
\tag{11.2}
\]

\[
 L_n''=16\eta^2r_n^2K_n^2-8\eta^2r_n^3J_n,
\tag{11.3}
\]

\[
 L_n'''=-64\eta^3r_n^2K_n^3
+112\eta^3r_n^3K_nJ_n
-16\eta^3r_n^4C_n.
\tag{11.4}
\]

The coefficient \(112=64+48\) is universal finite-width product-rule
algebra; it is not permissible to omit that term before the parity audit.
Flipping every readout coordinate sends

\[
 (f_n,K_n,J_n,C_n)\mapsto(-f_n,K_n,-J_n,C_n).
\tag{11.5}
\]

Hence \(K_nJ_n\) and \(f_n^2K_nJ_n\) are odd and have exactly zero
expectation at every width.  Expanding

\[
 r_n^3K_nJ_n
 =(y_\star^3-3y_\star^2f_n+3y_\star f_n^2-f_n^3)K_nJ_n
\tag{11.6}
\]

removes the first and third summands exactly by (11.5); the remaining two
vanish in the width limit by Hölder, since the fixed-\(H\) \(L^p\) theorem
gives \(f_n\to0\) in every finite \(L^p\) and uniform moments of \(K_n,J_n\).
The same theorem justifies the remaining products.  With
\(\mathcal J_3[h](t)=\sum_{k=0}^3h^{(k)}(0)t^k/k!\), it gives the
coefficientwise limit

\[
\begin{aligned}
\lim_{n\to\infty}\mathcal J_3[\mathbb E L_n](t)
={}&y_\star^2
 -4\eta y_\star^2A_Ht
 +8\eta^2y_\star^2A_H^2t^2\\
 &-\left(
 \frac{32}{3}\eta^3y_\star^2A_H^3
 +\frac83\eta^3y_\star^4C_H
 \right)t^3\pmod{t^4}.
\end{aligned}
\tag{11.7}
\]

Thus no new Gaussian atom is needed for an arbitrary scalar label.  Equation
(11.7) is a statement about the first four Taylor coefficients at \(t=0\);
it does not assert convergence of the finite-width loss at any fixed
positive time.
